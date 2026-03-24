#!/usr/bin/env python3
"""
render.py — Pixel art renderer for the XO_OX project.

Reads JSON creature spec files and renders them to PNG at multiple sizes
with palette swap support. Outputs a manifest tracking all generated files.

Usage:
    python render.py creature.json -o ./out
    python render.py ./specs/ -o ./out --spritesheet --group-by-zone
    python render.py creature.json --only-variant fire
    python render.py creature.json --add-variant "neon A=#00ff00,B=#ff00ff"
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")


# ---------------------------------------------------------------------------
# Core rendering helpers
# ---------------------------------------------------------------------------

def hex_to_rgba(hex_color: str) -> tuple[int, int, int, int]:
    """Convert a #RRGGBB or #RGB hex string to an (R, G, B, 255) tuple."""
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Invalid hex color: {hex_color!r}")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return (r, g, b, 255)


def render_grid(grid: list[str], palette: dict[str, Optional[str]]) -> Image.Image:
    """
    Render a list of character rows into an RGBA PIL Image.

    Parameters
    ----------
    grid:
        List of strings; each character maps to a palette key.
        '.' (transparent) must be mapped to None in the palette.
    palette:
        Dict mapping characters to hex color strings or None (transparent).

    Returns
    -------
    PIL Image in RGBA mode.
    """
    height = len(grid)
    width = max(len(row) for row in grid) if grid else 0
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            color_hex = palette.get(ch)
            if color_hex is None:
                # Transparent — leave the pixel as (0, 0, 0, 0)
                continue
            pixels[x, y] = hex_to_rgba(color_hex)

    return img


def scale_image(img: Image.Image, factor: float) -> Image.Image:
    """
    Scale *img* by *factor* using nearest-neighbor interpolation to
    preserve pixel-art crispness.

    For non-integer factors the result is rounded to the nearest pixel.
    """
    new_w = round(img.width * factor)
    new_h = round(img.height * factor)
    return img.resize((new_w, new_h), Image.NEAREST)


def apply_palette_swap(
    base_palette: dict[str, Optional[str]],
    variant_overrides: dict[str, str],
) -> dict[str, Optional[str]]:
    """
    Return a new palette dict with *variant_overrides* merged on top of
    *base_palette*.  Keys absent from *variant_overrides* are kept as-is.
    """
    new_palette = dict(base_palette)
    new_palette.update(variant_overrides)
    return new_palette


def create_spritesheet(
    images: list[Image.Image],
    columns: int = 8,
    padding: int = 1,
) -> Image.Image:
    """
    Arrange *images* into a grid with *columns* columns and 1-pixel padding.

    All images are assumed to have the same dimensions.  If the list is
    empty, a 1×1 transparent image is returned.
    """
    if not images:
        return Image.new("RGBA", (1, 1), (0, 0, 0, 0))

    cell_w, cell_h = images[0].size
    rows = (len(images) + columns - 1) // columns

    sheet_w = columns * cell_w + (columns + 1) * padding
    sheet_h = rows * cell_h + (rows + 1) * padding
    sheet = Image.new("RGBA", (sheet_w, sheet_h), (0, 0, 0, 0))

    for idx, img in enumerate(images):
        col = idx % columns
        row = idx // columns
        x = padding + col * (cell_w + padding)
        y = padding + row * (cell_h + padding)
        sheet.paste(img, (x, y), img)

    return sheet


# ---------------------------------------------------------------------------
# Spec validation helpers
# ---------------------------------------------------------------------------

GRID_SIZES = [16, 32]
SCALE_FACTORS = {16: 2.5, 32: 2.5}  # → 40×40 and 80×80


def validate_grid(grid: list[str], expected_size: int) -> bool:
    """Return True if *grid* has the expected number of rows and columns."""
    if len(grid) != expected_size:
        return False
    for row in grid:
        if len(row) != expected_size:
            return False
    return True


# ---------------------------------------------------------------------------
# Main creature renderer
# ---------------------------------------------------------------------------

def render_creature(
    spec: dict,
    output_dir: Path,
    *,
    only_variant: Optional[str] = None,
    extra_variants: Optional[dict[str, dict[str, str]]] = None,
) -> list[dict]:
    """
    Render all sizes and variants for one creature spec.

    Parameters
    ----------
    spec:
        Parsed JSON creature spec dict.
    output_dir:
        Root output directory.  A sub-directory named after the creature
        is created automatically.
    only_variant:
        If set, render only the base palette **and** this variant.
    extra_variants:
        Additional variants provided via --add-variant on the CLI.

    Returns
    -------
    List of manifest entry dicts (one per generated file).
    """
    name = spec["name"]
    creature_dir = output_dir / name
    creature_dir.mkdir(parents=True, exist_ok=True)

    base_palette: dict[str, Optional[str]] = spec["palette"]
    grids: dict[str, list[str]] = spec.get("grids", {})

    # Merge spec variants with any extras supplied at the CLI
    variants: dict[str, dict[str, str]] = dict(spec.get("variants", {}))
    if extra_variants:
        variants.update(extra_variants)

    # Decide which variants to render
    if only_variant is not None:
        variants_to_render = {only_variant: variants[only_variant]} if only_variant in variants else {}
    else:
        variants_to_render = variants

    manifest_entries: list[dict] = []

    for size in GRID_SIZES:
        size_key = str(size)
        if size_key not in grids:
            print(f"  [skip] {name}: no {size}×{size} grid defined")
            continue

        grid = grids[size_key]
        if not validate_grid(grid, size):
            print(
                f"  [warn] {name}: {size}×{size} grid has wrong dimensions "
                f"(rows={len(grid)}, expected={size}) — skipping"
            )
            continue

        scale = SCALE_FACTORS[size]
        scaled_size = round(size * scale)

        # --- Base palette ---
        if only_variant is None:
            img_native = render_grid(grid, base_palette)
            img_scaled = scale_image(img_native, scale)

            native_filename = f"{name}_{size}x{size}.png"
            scaled_filename = f"{name}_{scaled_size}x{scaled_size}.png"

            native_path = creature_dir / native_filename
            scaled_path = creature_dir / scaled_filename

            img_native.save(native_path)
            img_scaled.save(scaled_path)

            manifest_entries.append({
                "name": name,
                "engine": spec.get("engine"),
                "zone": spec.get("zone"),
                "variant": "base",
                "width": size,
                "height": size,
                "file": str(native_path),
            })
            manifest_entries.append({
                "name": name,
                "engine": spec.get("engine"),
                "zone": spec.get("zone"),
                "variant": "base",
                "width": scaled_size,
                "height": scaled_size,
                "file": str(scaled_path),
            })

        # --- Variants ---
        for variant_name, overrides in variants_to_render.items():
            swapped = apply_palette_swap(base_palette, overrides)
            v_native = render_grid(grid, swapped)
            v_scaled = scale_image(v_native, scale)

            v_native_filename = f"{name}_{size}x{size}_{variant_name}.png"
            v_scaled_filename = f"{name}_{scaled_size}x{scaled_size}_{variant_name}.png"

            v_native_path = creature_dir / v_native_filename
            v_scaled_path = creature_dir / v_scaled_filename

            v_native.save(v_native_path)
            v_scaled.save(v_scaled_path)

            manifest_entries.append({
                "name": name,
                "engine": spec.get("engine"),
                "zone": spec.get("zone"),
                "variant": variant_name,
                "width": size,
                "height": size,
                "file": str(v_native_path),
            })
            manifest_entries.append({
                "name": name,
                "engine": spec.get("engine"),
                "zone": spec.get("zone"),
                "variant": variant_name,
                "width": scaled_size,
                "height": scaled_size,
                "file": str(v_scaled_path),
            })

    return manifest_entries


# ---------------------------------------------------------------------------
# Spritesheet assembly
# ---------------------------------------------------------------------------

def build_spritesheets(
    manifest_entries: list[dict],
    output_dir: Path,
    columns: int,
    group_by_zone: bool,
) -> list[dict]:
    """
    Build sprite sheets from *manifest_entries*.

    When *group_by_zone* is True, separate sheets are produced for each
    (zone, size) combination.  Otherwise one sheet per size is produced.

    Only base-variant, native-size images are included in sheets.

    Returns a list of manifest entries for the generated sheet files.
    """
    sheet_entries: list[dict] = []

    # Gather only base-variant entries
    base_entries = [e for e in manifest_entries if e["variant"] == "base"]

    def _make_sheet(entries: list[dict], tag: str, size: int) -> Optional[dict]:
        sized = [e for e in entries if e["width"] == size and e["height"] == size]
        if not sized:
            return None
        images = [Image.open(e["file"]).convert("RGBA") for e in sized]
        sheet = create_spritesheet(images, columns=columns)
        filename = f"spritesheet_{tag}_{size}x{size}.png" if tag else f"spritesheet_{size}x{size}.png"
        path = output_dir / filename
        sheet.save(path)
        return {
            "type": "spritesheet",
            "tag": tag or "all",
            "width": size,
            "height": size,
            "count": len(images),
            "file": str(path),
        }

    if group_by_zone:
        zones = sorted({e["zone"] for e in base_entries if e.get("zone")})
        for zone in zones:
            zone_entries = [e for e in base_entries if e.get("zone") == zone]
            safe_zone = re.sub(r"[^A-Za-z0-9_-]", "_", zone).lower()
            for size in GRID_SIZES:
                entry = _make_sheet(zone_entries, safe_zone, size)
                if entry:
                    sheet_entries.append(entry)
    else:
        for size in GRID_SIZES:
            entry = _make_sheet(base_entries, "", size)
            if entry:
                sheet_entries.append(entry)

    return sheet_entries


# ---------------------------------------------------------------------------
# Spec loading utilities
# ---------------------------------------------------------------------------

def load_spec(path: Path) -> Optional[dict]:
    """Load and return a creature spec from *path*, or None on error."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"[error] Could not load spec {path}: {exc}", file=sys.stderr)
        return None


def collect_specs(input_path: Path, zone_filter: Optional[str]) -> list[tuple[Path, dict]]:
    """
    Collect all spec files from *input_path* (file or directory).

    When *zone_filter* is set, only specs whose 'zone' field matches
    (case-insensitive) are included.

    Specs found in a directory are sorted by the numeric engine suffix if
    present (e.g. "ONSET" → no number; specs without numbers sort last),
    then alphabetically.
    """
    if input_path.is_file():
        spec = load_spec(input_path)
        if spec is None:
            return []
        if zone_filter and spec.get("zone", "").lower() != zone_filter.lower():
            return []
        return [(input_path, spec)]

    # Directory
    json_files = sorted(input_path.glob("*.json"))

    def engine_sort_key(path_spec: tuple[Path, dict]) -> tuple[int, str]:
        _, spec = path_spec
        engine = spec.get("engine", "")
        match = re.search(r"(\d+)$", engine)
        num = int(match.group(1)) if match else 9999
        return (num, spec.get("name", ""))

    pairs = []
    for p in json_files:
        spec = load_spec(p)
        if spec is None:
            continue
        if zone_filter and spec.get("zone", "").lower() != zone_filter.lower():
            continue
        pairs.append((p, spec))

    pairs.sort(key=engine_sort_key)
    return pairs


# ---------------------------------------------------------------------------
# CLI argument parsing helpers
# ---------------------------------------------------------------------------

def parse_add_variant(raw: str) -> tuple[str, dict[str, str]]:
    """
    Parse a --add-variant argument string like "neon A=#00ff00,B=#ff00ff"
    into (variant_name, {key: hex, ...}).
    """
    parts = raw.split(None, 1)
    if len(parts) != 2:
        raise argparse.ArgumentTypeError(
            f"--add-variant expects 'NAME KEY=#HEX,...' but got: {raw!r}"
        )
    variant_name = parts[0]
    overrides: dict[str, str] = {}
    for token in parts[1].split(","):
        token = token.strip()
        if "=" not in token:
            raise argparse.ArgumentTypeError(
                f"Expected KEY=#HEX in variant override, got: {token!r}"
            )
        key, hex_val = token.split("=", 1)
        overrides[key.strip()] = hex_val.strip()
    return variant_name, overrides


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render XO_OX pixel art creature specs to PNG.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "input",
        metavar="SPEC",
        help="Path to a JSON spec file or a directory containing spec files.",
    )
    parser.add_argument(
        "-o", "--output",
        default="./pixel-art-output",
        metavar="DIR",
        help="Output directory (default: ./pixel-art-output).",
    )
    parser.add_argument(
        "--spritesheet",
        action="store_true",
        help="Generate sprite sheet PNGs from all rendered base images.",
    )
    parser.add_argument(
        "--columns",
        type=int,
        default=8,
        metavar="N",
        help="Number of columns in sprite sheets (default: 8).",
    )
    parser.add_argument(
        "--only-variant",
        metavar="NAME",
        help="Render only the named variant (base palette is skipped).",
    )
    parser.add_argument(
        "--zone",
        metavar="ZONE",
        help="Filter specs by zone field (case-insensitive).",
    )
    parser.add_argument(
        "--add-variant",
        action="append",
        default=[],
        metavar="'NAME KEY=#HEX,...'",
        help=(
            "Inject an inline variant at render time. "
            "Example: --add-variant 'neon A=#00ff00,B=#ff00ff'. "
            "Can be repeated."
        ),
    )
    parser.add_argument(
        "--group-by-zone",
        action="store_true",
        help="Generate separate sprite sheets per zone (implies --spritesheet).",
    )

    args = parser.parse_args()

    input_path = Path(args.input).expanduser()
    output_dir = Path(args.output).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        sys.exit(f"[error] Input path does not exist: {input_path}")

    # Parse --add-variant flags
    extra_variants: dict[str, dict[str, str]] = {}
    for raw in args.add_variant:
        try:
            v_name, v_overrides = parse_add_variant(raw)
        except argparse.ArgumentTypeError as exc:
            sys.exit(f"[error] {exc}")
        extra_variants[v_name] = v_overrides

    # Collect specs
    specs = collect_specs(input_path, zone_filter=args.zone)
    if not specs:
        sys.exit("[warn] No matching specs found.")

    print(f"Rendering {len(specs)} creature(s) → {output_dir}")

    all_manifest_entries: list[dict] = []

    for spec_path, spec in specs:
        creature_name = spec.get("name", spec_path.stem)
        print(f"  → {creature_name}  ({spec.get('engine', '?')} / {spec.get('zone', '?')})")

        entries = render_creature(
            spec,
            output_dir,
            only_variant=args.only_variant,
            extra_variants=extra_variants if extra_variants else None,
        )
        all_manifest_entries.extend(entries)

    # Sprite sheets
    sheet_entries: list[dict] = []
    if args.spritesheet or args.group_by_zone:
        print("Building sprite sheets…")
        sheet_entries = build_spritesheets(
            all_manifest_entries,
            output_dir,
            columns=args.columns,
            group_by_zone=args.group_by_zone,
        )
        for se in sheet_entries:
            tag_label = f" [{se['tag']}]" if se.get("tag") and se["tag"] != "all" else ""
            print(
                f"  sheet{tag_label} {se['width']}×{se['height']} "
                f"({se['count']} sprites) → {se['file']}"
            )

    # Write manifest.json
    manifest = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total_files": len(all_manifest_entries),
        "creatures": all_manifest_entries,
        "spritesheets": sheet_entries,
    }
    manifest_path = output_dir / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)

    print(
        f"\nDone. {len(all_manifest_entries)} image(s) rendered. "
        f"Manifest → {manifest_path}"
    )


if __name__ == "__main__":
    main()
