#!/usr/bin/env python3
"""
archetype_engine.py — Archetype-based pixel art generation for the XO_OX project.

Three subsystems:
  Part 1 — Archetype Extraction: pull shape templates (.#F grids) from existing pixel art.
  Part 2 — Template Compositor: apply a color palette to a template grid.
  Part 3 — Feature Overlay System: apply small grid patches (lures, spikes, etc.).

CLI Usage:
    python3 archetype_engine.py extract IMAGE_PATH --archetype NAME -o OUTPUT.json
    python3 archetype_engine.py build-library PACK_DIR --mappings MAPPINGS.json -o LIBRARY.json
    python3 archetype_engine.py compose --archetype NAME --library LIBRARY.json \\
        --palette "#ff6347,#ffffff,#1a1a2e" --signature "#ff6347" -o SPEC.json
"""

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Optional

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ALPHA_THRESHOLD = 128
CORNER_SIMILARITY_THRESHOLD = 30
TEMPLATE_CHARS = {"bg": ".", "outline": "#", "fill": "F"}
DEFAULT_SIZES = [16, 32]

# Zone split ratios for vertical (default) coloration
ZONE_TOP_RATIO = 0.30
ZONE_MID_RATIO = 0.40  # top 30% → A, middle 40% → B, bottom 30% → C

# Color keys used in render.py palette dicts
FILL_KEYS = ["A", "B", "C", "D", "E"]
OUTLINE_KEY = "#"
BG_KEY = "."


# ---------------------------------------------------------------------------
# Part 0 — Shared silhouette helpers (mirrors analyze_reference.py approach)
# ---------------------------------------------------------------------------

def _average_rgb(pixels: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    """Return component-wise average of a list of (R, G, B) tuples."""
    n = len(pixels)
    if n == 0:
        return (0, 0, 0)
    return (
        sum(p[0] for p in pixels) // n,
        sum(p[1] for p in pixels) // n,
        sum(p[2] for p in pixels) // n,
    )


def _rgb_distance(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> float:
    """Euclidean RGB distance between two color tuples."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))


def extract_silhouette(image: Image.Image) -> Image.Image:
    """
    Extract a binary silhouette from a pixel art sprite.

    Returns an 'L' mode image (same size) where 255 = foreground, 0 = background.
    Uses alpha channel when present and meaningful; otherwise falls back to
    corner-sample background detection — same strategy as analyze_reference.py.
    """
    img = image.convert("RGBA")
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    mask_px = mask.load()
    img_px = img.load()

    alpha_vals = [img_px[x, y][3] for y in range(h) for x in range(w)]
    a_min, a_max = min(alpha_vals), max(alpha_vals)
    has_alpha = (a_max - a_min) > 10

    if has_alpha:
        print("  silhouette: alpha-channel mode", file=sys.stderr)
        for y in range(h):
            for x in range(w):
                mask_px[x, y] = 255 if img_px[x, y][3] > ALPHA_THRESHOLD else 0
    else:
        print("  silhouette: corner-sample background detection", file=sys.stderr)
        corners = [
            img_px[0, 0][:3],
            img_px[w - 1, 0][:3],
            img_px[0, h - 1][:3],
            img_px[w - 1, h - 1][:3],
        ]
        bg = _average_rgb(corners)
        print(f"  background estimated: #{bg[0]:02x}{bg[1]:02x}{bg[2]:02x}", file=sys.stderr)
        for y in range(h):
            for x in range(w):
                dist = _rgb_distance(img_px[x, y][:3], bg)
                mask_px[x, y] = 0 if dist < CORNER_SIMILARITY_THRESHOLD else 255

    fg = sum(1 for y in range(h) for x in range(w) if mask_px[x, y] == 255)
    print(f"  foreground pixels: {fg}/{w * h}", file=sys.stderr)
    return mask


# ---------------------------------------------------------------------------
# Part 1 — Archetype Extraction
# ---------------------------------------------------------------------------

def _crop_to_bounding_box(mask: Image.Image) -> Image.Image:
    """Crop a binary mask image to the tight bounding box of its foreground."""
    bbox = mask.getbbox()
    if bbox is None:
        return mask
    return mask.crop(bbox)


def _pad_to_square(mask: Image.Image) -> Image.Image:
    """Pad a binary mask to a square with background (0) on all sides."""
    w, h = mask.size
    side = max(w, h)
    square = Image.new("L", (side, side), 0)
    offset_x = (side - w) // 2
    offset_y = (side - h) // 2
    square.paste(mask, (offset_x, offset_y))
    return square


def _build_template_grid(binary_mask: Image.Image) -> list[str]:
    """
    Convert a binary mask (L mode, 255=fg, 0=bg) into a template grid using
    only '.', '#', and 'F' characters.

    Classification rules:
      - 0   → '.'  (transparent background)
      - 255 adjacent to at least one background pixel → '#' (outline)
      - 255 fully surrounded by foreground → 'F' (fill)

    4-connectivity is used for adjacency (no diagonals) to keep outlines clean.
    """
    w, h = binary_mask.size
    px = binary_mask.load()

    def is_fg(x: int, y: int) -> bool:
        if x < 0 or y < 0 or x >= w or y >= h:
            return False
        return px[x, y] == 255

    rows: list[str] = []
    for y in range(h):
        row = []
        for x in range(w):
            if px[x, y] == 0:
                row.append(".")
            else:
                # Check 4-connected neighbours; if any is background → outline
                neighbors_bg = (
                    not is_fg(x - 1, y)
                    or not is_fg(x + 1, y)
                    or not is_fg(x, y - 1)
                    or not is_fg(x, y + 1)
                )
                row.append("#" if neighbors_bg else "F")
        rows.append("".join(row))
    return rows


def _compute_template_metadata(grid: list[str]) -> dict:
    """
    Compute fill_ratio, aspect_ratio (width/height of bounding box), and a
    bilateral symmetry score (0–1) from a template grid.
    """
    total = sum(ch != "." for row in grid for ch in row)
    fill = sum(ch == "F" for row in grid for ch in row)
    fill_ratio = fill / total if total > 0 else 0.0

    # Bounding box of all non-bg chars
    rows_with_fg = [r for r, row in enumerate(grid) if any(ch != "." for ch in row)]
    cols_with_fg = [c for row in grid for c, ch in enumerate(row) if ch != "."]

    if rows_with_fg and cols_with_fg:
        bb_h = rows_with_fg[-1] - rows_with_fg[0] + 1
        bb_w = max(cols_with_fg) - min(cols_with_fg) + 1
        aspect_ratio = bb_w / bb_h if bb_h > 0 else 1.0
    else:
        aspect_ratio = 1.0

    # Left-right symmetry: for each row, mirror and count matching non-bg cells
    h, w = len(grid), max(len(row) for row in grid) if grid else 0
    matched = total_pairs = 0
    for row in grid:
        padded = row.ljust(w, ".")
        for x in range(w // 2):
            l, r = padded[x], padded[w - 1 - x]
            if l != "." or r != ".":
                total_pairs += 1
                if (l != ".") == (r != "."):
                    matched += 1
    symmetry = matched / total_pairs if total_pairs > 0 else 0.0

    return {
        "fill_ratio": round(fill_ratio, 3),
        "aspect_ratio": round(aspect_ratio, 3),
        "symmetry": round(symmetry, 3),
    }


def extract_archetype(
    image_path: str,
    archetype_name: str,
    target_sizes: list[int] = None,
) -> dict:
    """
    Extract a shape template from an existing pixel art sprite.

    Parameters
    ----------
    image_path:
        Path to the source sprite image.
    archetype_name:
        Identifier for this archetype (e.g. 'FISH_STANDARD').
    target_sizes:
        List of pixel dimensions to produce templates at (default [16, 32]).

    Returns
    -------
    Dict matching the archetype JSON schema:
        {archetype, source, templates: {size: [rows]}, metadata}
    """
    if target_sizes is None:
        target_sizes = DEFAULT_SIZES

    print(f"[extract_archetype] {image_path} → {archetype_name}", file=sys.stderr)

    try:
        img = Image.open(image_path).convert("RGBA")
    except OSError as exc:
        sys.exit(f"[error] Cannot open image {image_path!r}: {exc}")

    mask = extract_silhouette(img)
    cropped = _crop_to_bounding_box(mask)
    squared = _pad_to_square(cropped)

    templates: dict[str, list[str]] = {}
    for size in target_sizes:
        resized = squared.resize((size, size), Image.NEAREST)
        grid = _build_template_grid(resized)
        templates[str(size)] = grid
        print(f"  template {size}×{size}: {len(grid)} rows", file=sys.stderr)

    # Use the largest template for metadata
    largest_key = str(max(target_sizes))
    metadata = _compute_template_metadata(templates[largest_key])
    print(f"  metadata: {metadata}", file=sys.stderr)

    return {
        "archetype": archetype_name,
        "source": str(image_path),
        "templates": templates,
        "metadata": metadata,
    }


def _merge_templates(template_list: list[list[str]]) -> list[str]:
    """
    Merge multiple template grids (same size) into a consensus template.

    For each cell position: if more than 50% of sources have a foreground
    character ('#' or 'F'), the consensus is foreground.  Among foreground
    cells, '#' wins over 'F' if at least one source has '#' at that position
    (outline pixels are sticky at the boundary).
    """
    if not template_list:
        return []
    h = len(template_list[0])
    w = max(len(row) for row in template_list[0]) if h > 0 else 0
    n = len(template_list)

    rows: list[str] = []
    for y in range(h):
        row = []
        for x in range(w):
            fg_count = 0
            outline_count = 0
            for tmpl in template_list:
                cell = tmpl[y][x] if y < len(tmpl) and x < len(tmpl[y]) else "."
                if cell != ".":
                    fg_count += 1
                if cell == "#":
                    outline_count += 1
            if fg_count > n / 2:
                row.append("#" if outline_count > 0 else "F")
            else:
                row.append(".")
        rows.append("".join(row))
    return rows


def build_archetype_library(
    pack_dir: str,
    mappings: dict[str, list[str]],
    output_dir: str,
    target_sizes: list[int] = None,
) -> dict:
    """
    Build a full archetype library from a directory of reference sprites.

    Parameters
    ----------
    pack_dir:
        Root directory of the sprite pack.
    mappings:
        Dict mapping archetype names to lists of relative paths within pack_dir.
        Example: {"FISH_STANDARD": ["Salt Water/Clownfish.png", ...]}
    output_dir:
        Directory where archetype_library.json is written.
    target_sizes:
        Pixel dimensions to generate templates for (default [16, 32]).

    Returns
    -------
    The complete library dict (also saved to disk).
    """
    if target_sizes is None:
        target_sizes = DEFAULT_SIZES

    pack_path = Path(pack_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    print(f"[build_archetype_library] pack_dir={pack_dir}, archetypes={len(mappings)}", file=sys.stderr)

    library: dict[str, dict] = {}

    for archetype_name, source_paths in mappings.items():
        print(f"\n--- Archetype: {archetype_name} ---", file=sys.stderr)
        per_source_templates: dict[str, list[list[str]]] = {str(s): [] for s in target_sizes}
        valid_sources: list[str] = []

        for rel_path in source_paths:
            full_path = pack_path / rel_path
            if not full_path.exists():
                print(f"  [warn] missing: {full_path}", file=sys.stderr)
                continue
            result = extract_archetype(str(full_path), archetype_name, target_sizes)
            valid_sources.append(str(full_path))
            for size_key, grid in result["templates"].items():
                per_source_templates[size_key].append(grid)

        if not valid_sources:
            print(f"  [warn] no valid sources for {archetype_name}, skipping", file=sys.stderr)
            continue

        # Merge templates across sources
        merged_templates: dict[str, list[str]] = {}
        for size_key, grids in per_source_templates.items():
            if grids:
                merged_templates[size_key] = _merge_templates(grids)

        # Metadata from largest merged template
        largest_key = str(max(target_sizes))
        metadata = _compute_template_metadata(merged_templates.get(largest_key, []))
        metadata["source_count"] = len(valid_sources)

        library[archetype_name] = {
            "archetype": archetype_name,
            "sources": valid_sources,
            "templates": merged_templates,
            "metadata": metadata,
        }
        print(f"  merged {len(valid_sources)} source(s) → {metadata}", file=sys.stderr)

    library_path = out_path / "archetype_library.json"
    with open(library_path, "w", encoding="utf-8") as fh:
        json.dump(library, fh, indent=2)
    print(f"\n[build_archetype_library] library saved → {library_path}", file=sys.stderr)

    return library


# ---------------------------------------------------------------------------
# Part 2 — Template Compositor
# ---------------------------------------------------------------------------

def _assign_fill_zones(
    grid: list[str],
    orientation: str = "vertical",
    zone_ratios: Optional[tuple[float, float, float]] = None,
) -> list[str]:
    """
    Replace 'F' cells with zone color keys (A, B, C, …) based on position.

    Parameters
    ----------
    grid:
        Template grid using '.', '#', 'F'.
    orientation:
        'vertical' → top/middle/bottom banding (default, mimics countershading).
        'horizontal' → left/middle/right banding.
    zone_ratios:
        Three floats (top, mid, bot) that must sum to ~1.0.
        Default: (0.30, 0.40, 0.30).

    Returns
    -------
    New grid with 'F' replaced by 'A', 'B', or 'C'.
    """
    if zone_ratios is None:
        zone_ratios = (ZONE_TOP_RATIO, ZONE_MID_RATIO, 1.0 - ZONE_TOP_RATIO - ZONE_MID_RATIO)

    h = len(grid)
    w = max(len(row) for row in grid) if grid else 0
    top_end = zone_ratios[0]
    mid_end = zone_ratios[0] + zone_ratios[1]

    result = []
    for y, row in enumerate(grid):
        new_row = []
        for x, ch in enumerate(row):
            if ch != "F":
                new_row.append(ch)
                continue
            if orientation == "vertical":
                ratio = y / h if h > 0 else 0
            else:
                ratio = x / w if w > 0 else 0

            if ratio < top_end:
                new_row.append("A")
            elif ratio < mid_end:
                new_row.append("B")
            else:
                new_row.append("C")
        result.append("".join(new_row))
    return result


def _rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert (R, G, B) integers to a lowercase '#rrggbb' hex string."""
    return f"#{r:02x}{g:02x}{b:02x}"


def _hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    """Convert a '#RRGGBB' or '#RGB' hex string to an (R, G, B) tuple."""
    h = hex_str.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Invalid hex color: {hex_str!r}")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _shift_toward(
    source: tuple[int, int, int],
    target: tuple[int, int, int],
    strength: float = 0.5,
) -> tuple[int, int, int]:
    """
    Blend source color toward target by *strength* (0 = unchanged, 1 = target).
    """
    return tuple(
        int(source[i] + (target[i] - source[i]) * strength)
        for i in range(3)
    )


def compose_creature(
    archetype_template: dict,
    palette: dict[str, Optional[str]],
    feature_overlays: Optional[list[dict]] = None,
    size: int = 16,
    orientation: str = "vertical",
    zone_ratios: Optional[tuple[float, float, float]] = None,
) -> dict:
    """
    Apply a color palette to an archetype template to produce a render.py-compatible spec.

    Parameters
    ----------
    archetype_template:
        Archetype dict with 'templates' key (output of extract_archetype or from library).
    palette:
        Dict mapping character keys to hex color strings or None (for '.').
        Required keys: '.' (None), '#' (outline hex), 'A' (primary fill), 'B', 'C'.
        Optional: 'D', 'E' for extremities.
    feature_overlays:
        List of overlay definition dicts (see apply_overlay). Applied in order.
    size:
        Which template size to use (16 or 32).
    orientation:
        Fill zone direction: 'vertical' (top→bottom) or 'horizontal' (left→right).
    zone_ratios:
        (top, mid, bot) ratios for zone banding.

    Returns
    -------
    Dict with 'grid' (list[str]) and 'palette' compatible with render.py.
    Includes 'grids' key with the single size for direct use as a creature spec fragment.
    """
    size_key = str(size)
    templates = archetype_template.get("templates", {})
    if size_key not in templates:
        available = list(templates.keys())
        sys.exit(
            f"[error] Template size {size} not found in archetype "
            f"'{archetype_template.get('archetype', '?')}'. Available: {available}"
        )

    raw_grid = templates[size_key]

    # Step 1: assign fill zones (F → A/B/C)
    zoned_grid = _assign_fill_zones(raw_grid, orientation=orientation, zone_ratios=zone_ratios)

    # Step 2: apply feature overlays
    working_grid = [list(row) for row in zoned_grid]
    if feature_overlays:
        for overlay_def in feature_overlays:
            working_grid = apply_overlay(working_grid, overlay_def)

    final_grid = ["".join(row) for row in working_grid]

    # Build the full palette with defaults for any missing keys
    full_palette: dict[str, Optional[str]] = {
        ".": None,
        "#": palette.get("#", "#1a1a2e"),
        "A": palette.get("A"),
        "B": palette.get("B"),
        "C": palette.get("C"),
    }
    for key in ("D", "E"):
        if key in palette:
            full_palette[key] = palette[key]

    return {
        "grid": final_grid,
        "grids": {size_key: final_grid},
        "palette": full_palette,
        "archetype": archetype_template.get("archetype"),
    }


def compose_from_photo_palette(
    archetype_name: str,
    photo_palette: list[tuple[int, int, int]],
    signature_color: str,
    library_path: str,
    size: int = 16,
    signature_strength: float = 0.5,
    orientation: str = "vertical",
    outline_color: str = "#1a1a2e",
) -> dict:
    """
    Convenience function: load an archetype from the library, apply a photo palette,
    shift the primary color toward a signature color, and return a render.py spec dict.

    Parameters
    ----------
    archetype_name:
        Archetype identifier in the library (e.g. 'FISH_STANDARD').
    photo_palette:
        List of (R, G, B) tuples sorted by dominance (most dominant first).
        At least 3 entries expected (for A, B, C zones).
    signature_color:
        Hex string of the engine's signature color (e.g. '#9B5DE5' for XOxytocin).
    library_path:
        Path to archetype_library.json.
    size:
        Template size to use (16 or 32).
    signature_strength:
        How strongly to shift primary color toward signature_color (0–1, default 0.5).
    orientation:
        'vertical' or 'horizontal' fill zone banding.
    outline_color:
        Hex color for outline pixels (default dark navy).

    Returns
    -------
    render.py-compatible spec dict with 'name', 'grids', 'palette', 'variants', 'engine', 'zone'.
    """
    print(f"[compose_from_photo_palette] archetype={archetype_name}, size={size}", file=sys.stderr)

    lib_path = Path(library_path)
    if not lib_path.exists():
        sys.exit(f"[error] Library not found: {library_path}")
    with open(lib_path, "r", encoding="utf-8") as fh:
        library = json.load(fh)

    if archetype_name not in library:
        available = list(library.keys())
        sys.exit(
            f"[error] Archetype '{archetype_name}' not found in library. "
            f"Available: {available}"
        )

    archetype_template = library[archetype_name]

    # Ensure at least 3 colors (A, B, C); pad with last color if too few
    colors = list(photo_palette)
    while len(colors) < 3:
        colors.append(colors[-1] if colors else (128, 128, 128))

    sig_rgb = _hex_to_rgb(signature_color)

    # Shift primary (A) color toward signature
    shifted_a = _shift_toward(colors[0], sig_rgb, signature_strength)
    print(
        f"  primary: {_rgb_to_hex(*colors[0])} → {_rgb_to_hex(*shifted_a)} "
        f"(shifted {signature_strength:.0%} toward {signature_color})",
        file=sys.stderr,
    )

    palette: dict[str, Optional[str]] = {
        ".": None,
        "#": outline_color,
        "A": _rgb_to_hex(*shifted_a),
        "B": _rgb_to_hex(*colors[1]),
        "C": _rgb_to_hex(*colors[2]),
    }
    if len(colors) >= 4:
        palette["D"] = _rgb_to_hex(*colors[3])
    if len(colors) >= 5:
        palette["E"] = _rgb_to_hex(*colors[4])

    composed = compose_creature(
        archetype_template,
        palette,
        size=size,
        orientation=orientation,
    )

    # Build a full render.py-compatible spec skeleton
    spec = {
        "name": archetype_name.lower(),
        "engine": "",
        "zone": "",
        "grids": composed["grids"],
        "palette": composed["palette"],
        "variants": {},
        "_archetype": archetype_name,
        "_signature_color": signature_color,
    }
    return spec


# ---------------------------------------------------------------------------
# Part 3 — Feature Overlay System
# ---------------------------------------------------------------------------

# Built-in overlay definitions.  Custom overlays can be passed inline.
FEATURE_OVERLAYS: dict[str, dict] = {
    "anglerfish_lure": {
        "anchor": "top_center",
        "offset": (-2, -3),
        "grid": [
            ".D.",
            ".#.",
            ".#.",
        ],
    },
    "pufferfish_spikes": {
        "anchor": "edges",
        "pattern": "alternate",
    },
    "dorsal_fin": {
        "anchor": "top_center",
        "offset": (0, -2),
        "grid": [
            ".#.",
            "###",
        ],
    },
    "tail_fin": {
        "anchor": "right_center",
        "offset": (1, 0),
        "grid": [
            "#.",
            "##",
            "#.",
        ],
    },
}


def _find_anchor(
    grid: list[list[str]],
    anchor: str,
) -> tuple[int, int]:
    """
    Compute the (x, y) grid coordinate for a named anchor position.

    Anchors:
      top_center      — center column of the topmost foreground row
      bottom_center   — center column of the bottommost foreground row
      left_center     — leftmost foreground column at mid-height
      right_center    — rightmost foreground column at mid-height
      center          — centroid of all foreground pixels
    """
    h = len(grid)
    w = max(len(row) for row in grid) if grid else 0
    fg_cells = [(x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch != "."]

    if not fg_cells:
        return (w // 2, h // 2)

    if anchor == "top_center":
        top_y = min(y for _, y in fg_cells)
        top_xs = [x for x, y in fg_cells if y == top_y]
        return (sum(top_xs) // len(top_xs), top_y)

    if anchor == "bottom_center":
        bot_y = max(y for _, y in fg_cells)
        bot_xs = [x for x, y in fg_cells if y == bot_y]
        return (sum(bot_xs) // len(bot_xs), bot_y)

    if anchor == "left_center":
        left_x = min(x for x, _ in fg_cells)
        left_ys = [y for x, y in fg_cells if x == left_x]
        return (left_x, sum(left_ys) // len(left_ys))

    if anchor == "right_center":
        right_x = max(x for x, _ in fg_cells)
        right_ys = [y for x, y in fg_cells if x == right_x]
        return (right_x, sum(right_ys) // len(right_ys))

    # Default: centroid
    cx = sum(x for x, _ in fg_cells) // len(fg_cells)
    cy = sum(y for _, y in fg_cells) // len(fg_cells)
    return (cx, cy)


def apply_overlay(
    grid: list[list[str]],
    overlay_def: dict,
) -> list[list[str]]:
    """
    Apply a feature overlay to a working grid (list of list[str]).

    The overlay_def dict supports two modes:

    Patch mode (uses 'grid' key):
        Place a small grid patch at the anchor position plus offset.
        Non-'.' cells overwrite the working grid; '.' cells are skipped.

    Edge extension mode (uses 'pattern': 'alternate'):
        Extend every other edge (outline) pixel outward by 1 cell.
        Useful for pufferfish-style spikes.

    Parameters
    ----------
    grid:
        Mutable working grid (list of list[str]).  Modified in-place and returned.
    overlay_def:
        Overlay definition dict. Keys:
          'anchor' — named anchor string or 'edges'
          'offset' — (dx, dy) tuple (default (0, 0))
          'grid'   — list[str] patch (for patch mode)
          'pattern'— 'alternate' for edge-extension mode

    Returns
    -------
    The modified grid (same object).
    """
    anchor_name = overlay_def.get("anchor", "top_center")
    offset = overlay_def.get("offset", (0, 0))
    patch = overlay_def.get("grid")
    pattern = overlay_def.get("pattern")

    h = len(grid)
    w = max(len(row) for row in grid) if grid else 0

    # --- Edge extension mode ---
    if anchor_name == "edges" and pattern == "alternate":
        # Collect all outline ('#') cells on the boundary
        outline_cells = []
        for y, row in enumerate(grid):
            for x, ch in enumerate(row):
                if ch == "#":
                    outline_cells.append((x, y))

        # Extend every other outline pixel outward by 1 (alternate)
        for i, (ox, oy) in enumerate(outline_cells):
            if i % 2 != 0:
                continue
            # Determine outward direction: first background neighbor
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = ox + dx, oy + dy
                if 0 <= nx < w and 0 <= ny < h:
                    if grid[ny][nx] == ".":
                        # Check bounds before expanding
                        ex, ey = ox + dx * 2, oy + dy * 2
                        if 0 <= ex < w and 0 <= ey < h:
                            grid[ey][ex] = "#"
                        break
        return grid

    # --- Patch mode ---
    if patch is None:
        return grid  # nothing to do

    ax, ay = _find_anchor(grid, anchor_name)
    dx, dy = offset

    for py, patch_row in enumerate(patch):
        for px, ch in enumerate(patch_row):
            if ch == ".":
                continue  # transparent; skip
            gx = ax + dx + px
            gy = ay + dy + py
            if 0 <= gx < w and 0 <= gy < h:
                while len(grid[gy]) <= gx:
                    grid[gy].append(".")
                grid[gy][gx] = ch

    return grid


# ---------------------------------------------------------------------------
# CLI helpers
# ---------------------------------------------------------------------------

def _parse_hex_palette(raw: str) -> list[tuple[int, int, int]]:
    """
    Parse a comma-separated list of hex colors into (R,G,B) tuples.

    Example: "#ff6347,#ffffff,#1a1a2e"
    """
    result = []
    for token in raw.split(","):
        token = token.strip()
        try:
            result.append(_hex_to_rgb(token))
        except ValueError as exc:
            sys.exit(f"[error] Invalid palette color {token!r}: {exc}")
    return result


def _load_mappings(mappings_path: str) -> dict[str, list[str]]:
    """Load a mappings JSON file (archetype_name → [relative paths])."""
    try:
        with open(mappings_path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"[error] Cannot load mappings file {mappings_path!r}: {exc}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:  # noqa: C901 — complex but intentionally flat CLI dispatch
    parser = argparse.ArgumentParser(
        description="Archetype-based pixel art template system for XO_OX.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- extract ---
    p_extract = subparsers.add_parser(
        "extract",
        help="Extract a shape template from a single pixel art sprite.",
    )
    p_extract.add_argument("image", metavar="IMAGE_PATH", help="Source sprite image.")
    p_extract.add_argument(
        "--archetype",
        required=True,
        metavar="NAME",
        help="Archetype identifier (e.g. FISH_STANDARD).",
    )
    p_extract.add_argument(
        "--sizes",
        default="16,32",
        metavar="N[,N...]",
        help="Comma-separated template sizes in pixels (default: 16,32).",
    )
    p_extract.add_argument(
        "-o", "--output",
        default=None,
        metavar="OUTPUT.json",
        help="Output JSON file path. Defaults to stdout.",
    )

    # --- build-library ---
    p_build = subparsers.add_parser(
        "build-library",
        help="Build a full archetype library from a sprite pack directory.",
    )
    p_build.add_argument("pack_dir", metavar="PACK_DIR", help="Root directory of the sprite pack.")
    p_build.add_argument(
        "--mappings",
        required=True,
        metavar="MAPPINGS.json",
        help="JSON file mapping archetype names to relative sprite paths.",
    )
    p_build.add_argument(
        "--sizes",
        default="16,32",
        metavar="N[,N...]",
        help="Comma-separated template sizes in pixels (default: 16,32).",
    )
    p_build.add_argument(
        "-o", "--output",
        default=".",
        metavar="OUTPUT_DIR",
        help="Output directory for archetype_library.json (default: current dir).",
    )

    # --- compose ---
    p_compose = subparsers.add_parser(
        "compose",
        help="Compose a colored spec from an archetype template and a palette.",
    )
    p_compose.add_argument(
        "--archetype",
        required=True,
        metavar="NAME",
        help="Archetype name to load from the library.",
    )
    p_compose.add_argument(
        "--library",
        required=True,
        metavar="LIBRARY.json",
        help="Path to archetype_library.json.",
    )
    p_compose.add_argument(
        "--palette",
        required=True,
        metavar="#HEX[,#HEX...]",
        help="Comma-separated hex colors (most dominant first). At least 3 required.",
    )
    p_compose.add_argument(
        "--signature",
        default=None,
        metavar="#HEX",
        help="Optional engine signature color to shift the primary color toward.",
    )
    p_compose.add_argument(
        "--signature-strength",
        type=float,
        default=0.5,
        metavar="0-1",
        help="How strongly to shift toward the signature color (default: 0.5).",
    )
    p_compose.add_argument(
        "--size",
        type=int,
        default=16,
        metavar="N",
        help="Template size to use (default: 16).",
    )
    p_compose.add_argument(
        "--orientation",
        choices=["vertical", "horizontal"],
        default="vertical",
        help="Fill zone banding direction (default: vertical).",
    )
    p_compose.add_argument(
        "--outline",
        default="#1a1a2e",
        metavar="#HEX",
        help="Outline pixel color (default: #1a1a2e).",
    )
    p_compose.add_argument(
        "-o", "--output",
        default=None,
        metavar="SPEC.json",
        help="Output JSON file path. Defaults to stdout.",
    )

    args = parser.parse_args()

    # ---------- extract ----------
    if args.command == "extract":
        sizes = [int(s.strip()) for s in args.sizes.split(",") if s.strip()]
        result = extract_archetype(args.image, args.archetype, target_sizes=sizes)
        out_json = json.dumps(result, indent=2)
        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(out_json, encoding="utf-8")
            print(f"[extract] saved → {out_path}", file=sys.stderr)
        else:
            print(out_json)

    # ---------- build-library ----------
    elif args.command == "build-library":
        sizes = [int(s.strip()) for s in args.sizes.split(",") if s.strip()]
        mappings = _load_mappings(args.mappings)
        build_archetype_library(
            args.pack_dir,
            mappings,
            args.output,
            target_sizes=sizes,
        )

    # ---------- compose ----------
    elif args.command == "compose":
        photo_palette = _parse_hex_palette(args.palette)
        if len(photo_palette) < 3:
            sys.exit("[error] --palette requires at least 3 colors (A, B, C zones).")

        signature = args.signature or _rgb_to_hex(*photo_palette[0])

        spec = compose_from_photo_palette(
            archetype_name=args.archetype,
            photo_palette=photo_palette,
            signature_color=signature,
            library_path=args.library,
            size=args.size,
            signature_strength=args.signature_strength,
            orientation=args.orientation,
            outline_color=args.outline,
        )
        out_json = json.dumps(spec, indent=2)
        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(out_json, encoding="utf-8")
            print(f"[compose] saved → {out_path}", file=sys.stderr)
        else:
            print(out_json)


if __name__ == "__main__":
    main()
