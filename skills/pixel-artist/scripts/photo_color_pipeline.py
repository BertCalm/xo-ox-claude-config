#!/usr/bin/env python3
"""
photo_color_pipeline.py — Photo-to-palette extraction pipeline for XO_OX creatures.

Takes real photographs of creatures, strips backgrounds via rembg, extracts dominant
colors, cross-references across multiple source images using CIE LAB voting, and
reduces to a pixel-art-ready palette of 3-5 colors.

Pipeline stages:
  1. Source loading + background removal  (rembg silueta model)
  2. Per-image color extraction           (colorgram or PIL quantize)
  3. Cross-reference color voting         (CIE LAB clustering across sources)
  4. Palette reduction to pixel art scale (perceptual distance enforcement)
  5. Output JSON + optional preview swatch

Usage:
    python3 photo_color_pipeline.py fish1.jpg fish2.jpg fish3.jpg \\
        -n blue_tang --signature-color "#4361ee" --num-colors 3 --preview \\
        -o palettes/blue_tang.json

    python3 photo_color_pipeline.py shrimp.png --no-rembg -n pistol_shrimp
"""

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Optional

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")

try:
    from basic_colormath import get_delta_e
    _HAS_COLORMATH = True
except ImportError:
    _HAS_COLORMATH = False

try:
    import colorgram
    _HAS_COLORGRAM = True
except ImportError:
    _HAS_COLORGRAM = False

try:
    from rembg import remove as rembg_remove, new_session as rembg_new_session
    _HAS_REMBG = True
except ImportError:
    _HAS_REMBG = False


# ---------------------------------------------------------------------------
# Color math utilities
# ---------------------------------------------------------------------------

def rgb_to_linear(c: float) -> float:
    """sRGB gamma -> linear light."""
    c = c / 255.0
    if c <= 0.04045:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c: float) -> int:
    """Linear light -> sRGB gamma, clamped to [0, 255]."""
    c = max(0.0, min(1.0, c))
    if c <= 0.0031308:
        val = c * 12.92
    else:
        val = 1.055 * (c ** (1.0 / 2.4)) - 0.055
    return round(val * 255)


def rgb_to_xyz(r: int, g: int, b: int) -> tuple[float, float, float]:
    """Convert sRGB (0-255) to CIE XYZ (D65)."""
    rl = rgb_to_linear(r)
    gl = rgb_to_linear(g)
    bl = rgb_to_linear(b)
    x = rl * 0.4124564 + gl * 0.3575761 + bl * 0.1804375
    y = rl * 0.2126729 + gl * 0.7151522 + bl * 0.0721750
    z = rl * 0.0193339 + gl * 0.1191920 + bl * 0.9503041
    return x, y, z


def xyz_to_lab(x: float, y: float, z: float) -> tuple[float, float, float]:
    """Convert CIE XYZ to CIE LAB (D65 white point)."""
    xn, yn, zn = 0.95047, 1.00000, 1.08883

    def f(t: float) -> float:
        if t > 0.008856:
            return t ** (1.0 / 3.0)
        return 7.787 * t + 16.0 / 116.0

    fx, fy, fz = f(x / xn), f(y / yn), f(z / zn)
    L = 116.0 * fy - 16.0
    a = 500.0 * (fx - fy)
    b_val = 200.0 * (fy - fz)
    return L, a, b_val


def lab_to_xyz(L: float, a: float, b_val: float) -> tuple[float, float, float]:
    """Convert CIE LAB to CIE XYZ (D65)."""
    xn, yn, zn = 0.95047, 1.00000, 1.08883
    fy = (L + 16.0) / 116.0
    fx = a / 500.0 + fy
    fz = fy - b_val / 200.0

    def f_inv(t: float) -> float:
        if t > 0.2069:
            return t ** 3
        return (t - 16.0 / 116.0) / 7.787

    return f_inv(fx) * xn, f_inv(fy) * yn, f_inv(fz) * zn


def xyz_to_rgb(x: float, y: float, z: float) -> tuple[int, int, int]:
    """Convert CIE XYZ to sRGB (0-255), clamped."""
    rl =  3.2404542 * x - 1.5371385 * y - 0.4985314 * z
    gl = -0.9692660 * x + 1.8760108 * y + 0.0415560 * z
    bl =  0.0556434 * x - 0.2040259 * y + 1.0572252 * z
    return linear_to_srgb(rl), linear_to_srgb(gl), linear_to_srgb(bl)


def rgb_to_lab(r: int, g: int, b: int) -> tuple[float, float, float]:
    """sRGB (0-255) -> CIE LAB."""
    return xyz_to_lab(*rgb_to_xyz(r, g, b))


def lab_to_rgb(L: float, a: float, b_val: float) -> tuple[int, int, int]:
    """CIE LAB -> sRGB (0-255)."""
    return xyz_to_rgb(*lab_to_xyz(L, a, b_val))


def delta_e(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> float:
    """CIE76 ΔE between two sRGB colors. Falls back to basic_colormath if available."""
    if _HAS_COLORMATH:
        try:
            return get_delta_e(c1, c2)
        except Exception:
            pass
    L1, a1, b1 = rgb_to_lab(*c1)
    L2, a2, b2 = rgb_to_lab(*c2)
    return math.sqrt((L1 - L2) ** 2 + (a1 - a2) ** 2 + (b1 - b2) ** 2)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def lighten_rgb(r: int, g: int, b: int, amount: float = 0.30) -> tuple[int, int, int]:
    """Lighten a color by `amount` in the CIE LAB L* channel (0–1 scale)."""
    L, a, b_val = rgb_to_lab(r, g, b)
    L = min(100.0, L + amount * 100.0)
    return lab_to_rgb(L, a, b_val)


def darken_rgb(r: int, g: int, b: int, amount: float = 0.30) -> tuple[int, int, int]:
    """Darken a color by `amount` in the CIE LAB L* channel."""
    L, a, b_val = rgb_to_lab(r, g, b)
    L = max(0.0, L - amount * 100.0)
    return lab_to_rgb(L, a, b_val)


# ---------------------------------------------------------------------------
# Stage 1: Source loading + background removal
# ---------------------------------------------------------------------------

_rembg_session = None  # shared session, lazy-initialized


def _get_rembg_session():
    global _rembg_session
    if _rembg_session is None:
        model_path = Path.home() / ".u2net" / "silueta.onnx"
        if not model_path.exists():
            print(
                "rembg: silueta model not found locally — downloading (~43 MB to ~/.u2net/)...",
                file=sys.stderr,
            )
        _rembg_session = rembg_new_session("silueta")
    return _rembg_session


def load_and_strip(image_paths: list[str], use_rembg: bool = True) -> list[Image.Image]:
    """
    Stage 1: Load images and remove backgrounds.

    Args:
        image_paths: List of file paths to source images.
        use_rembg: If True, run rembg on images without transparency.

    Returns:
        List of RGBA PIL Images with backgrounds removed.
    """
    if use_rembg and not _HAS_REMBG:
        print(
            "WARNING: rembg not installed — background removal skipped. "
            "Install with: pip install rembg",
            file=sys.stderr,
        )
        use_rembg = False

    results = []
    for path in image_paths:
        print(f"[stage 1] loading: {path}", file=sys.stderr)
        img = Image.open(path)

        already_has_alpha = img.mode in ("RGBA", "LA", "PA")

        if use_rembg and not already_has_alpha:
            print(f"  rembg: stripping background...", file=sys.stderr)
            session = _get_rembg_session()
            img_rgba = rembg_remove(img, session=session)
            if not isinstance(img_rgba, Image.Image):
                img_rgba = Image.fromarray(img_rgba)
            img_rgba = img_rgba.convert("RGBA")
        else:
            if already_has_alpha:
                print(f"  already has alpha channel — skipping rembg", file=sys.stderr)
            img_rgba = img.convert("RGBA")

        results.append(img_rgba)

    return results


# ---------------------------------------------------------------------------
# Stage 2: Per-image color extraction
# ---------------------------------------------------------------------------

# Colors that are clearly outlines or background remnants (to filter out)
_NEAR_BLACK_THRESHOLD = 30   # L* in LAB below this = outline black
_NEAR_WHITE_THRESHOLD = 92   # L* in LAB above this = white remnant


def _is_outline_or_background(r: int, g: int, b: int) -> bool:
    """Return True if this color is near-black (outline) or near-white (background)."""
    L, _, _ = rgb_to_lab(r, g, b)
    return L < _NEAR_BLACK_THRESHOLD or L > _NEAR_WHITE_THRESHOLD


def extract_colors_per_image(
    images: list[Image.Image],
    max_colors: int = 8,
) -> list[list[tuple[tuple[int, int, int], float]]]:
    """
    Stage 2: Extract dominant colors from each stripped image.

    Transparent pixels (alpha < 128) are ignored. Near-black outlines and
    near-white background remnants are filtered.

    Args:
        images: RGBA images with transparent backgrounds.
        max_colors: Maximum colors to extract per image before filtering.

    Returns:
        List (one per image) of [(R, G, B), proportion] sorted by proportion desc.
    """
    per_image = []

    for idx, img in enumerate(images):
        print(f"[stage 2] extracting colors from image {idx + 1}/{len(images)}", file=sys.stderr)

        rgba = img.convert("RGBA")
        pixels = list(rgba.getdata())
        visible = [(r, g, b) for r, g, b, a in pixels if a >= 128]

        if not visible:
            print(f"  WARNING: no visible pixels — skipping image {idx + 1}", file=sys.stderr)
            per_image.append([])
            continue

        total_visible = len(visible)

        if _HAS_COLORGRAM:
            # Build a temporary opaque image from visible pixels only (for colorgram)
            side = math.ceil(math.sqrt(total_visible))
            tmp = Image.new("RGB", (side, side), (0, 0, 0))
            tmp.putdata(visible + [(0, 0, 0)] * (side * side - total_visible))
            extracted = colorgram.extract(tmp, max_colors)
            raw_colors = [
                ((c.rgb.r, c.rgb.g, c.rgb.b), c.proportion)
                for c in extracted
            ]
        else:
            # PIL quantize fallback
            tmp = Image.new("RGB", (len(visible), 1))
            tmp.putdata(visible)
            quantized = tmp.quantize(colors=max_colors, method=Image.Quantize.MEDIANCUT)
            palette_data = quantized.getpalette()[:max_colors * 3]
            # Count occurrences per palette index
            counts: dict[int, int] = {}
            for px in quantized.getdata():
                counts[px] = counts.get(px, 0) + 1
            raw_colors = []
            for i in range(max_colors):
                if i not in counts:
                    continue
                r = palette_data[i * 3]
                g = palette_data[i * 3 + 1]
                b = palette_data[i * 3 + 2]
                raw_colors.append(((r, g, b), counts[i] / total_visible))

        # Filter outlines and background remnants
        filtered = [
            (color, prop)
            for color, prop in raw_colors
            if not _is_outline_or_background(*color)
        ]

        if not filtered:
            print(
                f"  WARNING: all extracted colors filtered as outline/background — "
                f"relaxing filter for image {idx + 1}",
                file=sys.stderr,
            )
            filtered = raw_colors  # fall back to unfiltered

        # Normalize proportions after filtering
        total_prop = sum(p for _, p in filtered)
        if total_prop > 0:
            filtered = [(c, p / total_prop) for c, p in filtered]

        filtered.sort(key=lambda x: x[1], reverse=True)
        print(
            f"  {len(filtered)} colors kept: "
            + ", ".join(rgb_to_hex(*c) for c, _ in filtered[:5]),
            file=sys.stderr,
        )
        per_image.append(filtered)

    return per_image


# ---------------------------------------------------------------------------
# Stage 3: Cross-reference color voting
# ---------------------------------------------------------------------------

def cross_reference_colors(
    per_image_colors: list[list[tuple[tuple[int, int, int], float]]],
    merge_threshold: float = 15.0,
) -> list[dict]:
    """
    Stage 3: Cluster colors across all source images and score by cross-source confidence.

    Colors appearing in more source images are ranked higher. Clustering uses
    CIE76 ΔE distance so perceptually similar colors (slightly different orange
    from two photos) merge into one representative.

    Args:
        per_image_colors: Output of extract_colors_per_image.
        merge_threshold: ΔE distance below which two colors are considered the same.

    Returns:
        List of cluster dicts sorted by (confidence * proportion) descending:
            {
                "color": (R, G, B),
                "hex": "#rrggbb",
                "confidence": float,   # fraction of source images that contributed
                "proportion": float,   # average proportion across contributing images
                "sources": int,        # how many images contributed
            }
    """
    num_images = len(per_image_colors)
    if num_images == 0:
        return []

    # Special case: single source — confidence is always 1.0, skip clustering across images
    if num_images == 1:
        results = []
        for color, prop in per_image_colors[0]:
            results.append({
                "color": color,
                "hex": rgb_to_hex(*color),
                "confidence": 1.0,
                "proportion": prop,
                "sources": 1,
            })
        return results

    print(f"[stage 3] cross-referencing colors across {num_images} sources", file=sys.stderr)

    # Build a flat pool tagging each color with its source image index
    pool: list[tuple[tuple[int, int, int], float, int]] = []
    for img_idx, colors in enumerate(per_image_colors):
        for color, prop in colors:
            pool.append((color, prop, img_idx))

    # Greedy clustering: assign each pool entry to the nearest existing cluster
    clusters: list[dict] = []  # each cluster: {representative, members, source_set, total_prop}

    for color, prop, img_idx in pool:
        best_idx = None
        best_dist = float("inf")
        for c_idx, cluster in enumerate(clusters):
            d = delta_e(color, cluster["representative"])
            if d < best_dist:
                best_dist = d
                best_idx = c_idx

        if best_idx is not None and best_dist < merge_threshold:
            cluster = clusters[best_idx]
            cluster["members"].append((color, prop))
            cluster["source_set"].add(img_idx)
            cluster["total_prop"] += prop
        else:
            clusters.append({
                "representative": color,
                "members": [(color, prop)],
                "source_set": {img_idx},
                "total_prop": prop,
            })

    # Build result dicts
    results = []
    for cluster in clusters:
        sources = len(cluster["source_set"])
        confidence = sources / num_images

        # Representative = member with highest individual proportion
        best_color = max(cluster["members"], key=lambda x: x[1])[0]

        avg_prop = cluster["total_prop"] / sources  # average within contributing images

        results.append({
            "color": best_color,
            "hex": rgb_to_hex(*best_color),
            "confidence": round(confidence, 4),
            "proportion": round(avg_prop, 4),
            "sources": sources,
        })

    # Sort by confidence * proportion (primary key) then confidence alone
    results.sort(key=lambda x: (x["confidence"] * x["proportion"], x["confidence"]), reverse=True)

    print(
        f"  {len(results)} clusters found "
        f"({sum(1 for r in results if r['confidence'] >= 0.6)} high-confidence)",
        file=sys.stderr,
    )
    for r in results[:6]:
        print(
            f"  {r['hex']}  confidence={r['confidence']:.0%}  "
            f"proportion={r['proportion']:.2%}  sources={r['sources']}/{num_images}",
            file=sys.stderr,
        )

    return results


# ---------------------------------------------------------------------------
# Stage 4: Palette reduction
# ---------------------------------------------------------------------------

_PALETTE_ROLES = ["A", "B", "C", "D", "E"]


def reduce_to_pixel_palette(
    voted_colors: list[dict],
    num_colors: int = 3,
    signature_color: Optional[str] = None,
    min_perceptual_distance: float = 20.0,
) -> dict[str, str]:
    """
    Stage 4: Pick the best N colors, enforce perceptual separation, apply signature,
    and auto-generate highlight + shadow.

    Args:
        voted_colors: Output of cross_reference_colors.
        num_colors: Target number of subject colors (A/B/C etc.), 3-5.
        signature_color: Optional hex override for the primary (A) color.
        min_perceptual_distance: Minimum ΔE between any two selected palette colors.

    Returns:
        Palette dict: {"#": "#1a1a2e", "A": "#hex", "B": "#hex", ...}
        Always includes outline "#" = dark anchor and auto D/E highlight/shadow
        when num_colors >= 4 or 5 respectively.
    """
    print(f"[stage 4] reducing to {num_colors}-color pixel palette", file=sys.stderr)

    selected: list[tuple[int, int, int]] = []

    for candidate in voted_colors:
        color = candidate["color"]
        # Check minimum perceptual distance from already-selected colors
        too_close = any(
            delta_e(color, s) < min_perceptual_distance for s in selected
        )
        if too_close:
            print(
                f"  skipping {rgb_to_hex(*color)} — too close to an already-selected color",
                file=sys.stderr,
            )
            continue
        selected.append(color)
        if len(selected) >= num_colors:
            break

    # Pad with generated variants if we didn't find enough distinct colors
    while len(selected) < num_colors:
        if selected:
            # Generate a lighter variant of the last selected color
            last = selected[-1]
            variant = lighten_rgb(*last, amount=0.20)
            # Avoid exact duplicates
            if all(delta_e(variant, s) >= 5.0 for s in selected):
                selected.append(variant)
            else:
                # Just lighten more aggressively until it's distinct
                variant = lighten_rgb(*last, amount=0.40)
                selected.append(variant)
        else:
            # No colors at all — use a neutral gray
            selected.append((128, 128, 128))

    # Apply signature color as primary (A)
    if signature_color:
        sig_rgb = hex_to_rgb(signature_color)
        selected[0] = sig_rgb
        print(
            f"  primary overridden with signature color {signature_color}",
            file=sys.stderr,
        )

    # Build palette dict
    palette: dict[str, str] = {"#": "#1a1a2e"}  # outline / dark anchor

    for i, color in enumerate(selected):
        if i < len(_PALETTE_ROLES):
            role = _PALETTE_ROLES[i]
            palette[role] = rgb_to_hex(*color)

    # Auto-generate D (highlight) and E (shadow) from primary if not already filled
    primary = selected[0]
    if "D" not in palette:
        palette["D"] = rgb_to_hex(*lighten_rgb(*primary, amount=0.30))
    if "E" not in palette:
        palette["E"] = rgb_to_hex(*darken_rgb(*primary, amount=0.30))

    print(f"  palette: " + "  ".join(f"{k}={v}" for k, v in palette.items()), file=sys.stderr)
    return palette


# ---------------------------------------------------------------------------
# Stage 5: Main entry point
# ---------------------------------------------------------------------------

def extract_creature_palette(
    image_paths: list[str],
    creature_name: str,
    signature_color: Optional[str] = None,
    num_colors: int = 3,
    use_rembg: bool = True,
    merge_threshold: float = 15.0,
    max_source_colors: int = 8,
) -> dict:
    """
    Full pipeline: stages 1-4, returning a structured palette result dict.

    Args:
        image_paths: Paths to source photos/images.
        creature_name: Name used in output metadata.
        signature_color: Optional hex to override the primary palette color.
        num_colors: Number of subject palette slots (A/B/C etc.).
        use_rembg: Whether to strip backgrounds via rembg.
        merge_threshold: ΔE merge threshold for cross-reference clustering.
        max_source_colors: Colors extracted per source image before filtering.

    Returns:
        {
            "creature": str,
            "palette": {"#": ..., "A": ..., "B": ..., ...},
            "color_analysis": {
                "per_image": [ [{"hex": ..., "proportion": ...}, ...], ... ],
                "voted_colors": [{"hex": ..., "confidence": ..., ...}, ...]
            },
            "num_sources": int,
            "high_confidence_colors": int,
        }
    """
    # Stage 1
    images = load_and_strip(image_paths, use_rembg=use_rembg)

    # Stage 2
    per_image_raw = extract_colors_per_image(images, max_colors=max_source_colors)

    # Stage 3
    voted = cross_reference_colors(per_image_raw, merge_threshold=merge_threshold)

    # Stage 4
    palette = reduce_to_pixel_palette(
        voted,
        num_colors=num_colors,
        signature_color=signature_color,
    )

    # Serializable per-image analysis
    per_image_serializable = [
        [{"hex": rgb_to_hex(*c), "proportion": round(p, 4)} for c, p in img_colors]
        for img_colors in per_image_raw
    ]

    # Serializable voted colors (strip non-serializable tuple)
    voted_serializable = [
        {k: v for k, v in entry.items() if k != "color"}
        for entry in voted
    ]

    high_confidence = sum(1 for v in voted if v["confidence"] >= 0.6)

    return {
        "creature": creature_name,
        "palette": palette,
        "color_analysis": {
            "per_image": per_image_serializable,
            "voted_colors": voted_serializable,
        },
        "num_sources": len(image_paths),
        "high_confidence_colors": high_confidence,
    }


# ---------------------------------------------------------------------------
# Preview generation
# ---------------------------------------------------------------------------

_SWATCH_W = 80
_SWATCH_H = 60
_LABEL_H = 20
_FONT_SIZE = 11


def _try_load_font(size: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", size)
    except Exception:
        try:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", size)
        except Exception:
            return ImageFont.load_default()


def save_preview(
    result: dict,
    stripped_images: list[Image.Image],
    output_path: str,
) -> None:
    """
    Save a color swatch preview PNG:
      Row 0: thumbnail of each stripped source image
      Row 1: all voted colors labeled with confidence %
      Row 2: final palette with role labels and hex values
    """
    font = _try_load_font(_FONT_SIZE)
    voted = result["color_analysis"]["voted_colors"]
    palette = result["palette"]
    creature = result["creature"]

    thumb_h = 120
    thumb_w = 120

    # Measure widths
    n_thumbs = len(stripped_images)
    n_voted = len(voted)
    palette_roles = list(palette.keys())  # "#", "A", "B", ...
    n_palette = len(palette_roles)

    total_w = max(
        n_thumbs * (thumb_w + 4),
        n_voted * (_SWATCH_W + 2),
        n_palette * (_SWATCH_W + 2),
    ) + 20

    row_heights = [thumb_h + _LABEL_H + 8, _SWATCH_H + _LABEL_H + 8, _SWATCH_H + _LABEL_H + 8]
    header_h = 30
    total_h = header_h + sum(row_heights)

    canvas = Image.new("RGB", (total_w, total_h), (20, 20, 30))
    draw = ImageDraw.Draw(canvas)

    # Header
    draw.text((10, 8), f"{creature} — color pipeline preview", fill=(220, 220, 220), font=font)

    y = header_h

    # --- Row 0: stripped source thumbnails ---
    draw.text((10, y + 2), "Source images (background removed):", fill=(160, 160, 160), font=font)
    y += _LABEL_H
    x = 10
    for img in stripped_images:
        thumb = img.copy()
        thumb.thumbnail((thumb_w, thumb_h), Image.LANCZOS)
        # Paste on dark background
        bg = Image.new("RGB", (thumb_w, thumb_h), (35, 35, 45))
        if thumb.mode == "RGBA":
            bg.paste(thumb, (0, 0), thumb.split()[3])
        else:
            bg.paste(thumb, (0, 0))
        canvas.paste(bg, (x, y))
        x += thumb_w + 4
    y += thumb_h + 8

    # --- Row 1: all voted colors ---
    draw.text((10, y + 2), "Voted colors (confidence %):", fill=(160, 160, 160), font=font)
    y += _LABEL_H
    x = 10
    for entry in voted:
        hex_val = entry["hex"]
        conf = entry["confidence"]
        r, g, b = hex_to_rgb(hex_val)
        draw.rectangle([x, y, x + _SWATCH_W - 1, y + _SWATCH_H - 1], fill=(r, g, b))
        label = f"{hex_val}\n{conf:.0%}"
        # Choose contrasting label color
        L, _, _ = rgb_to_lab(r, g, b)
        text_color = (10, 10, 10) if L > 50 else (240, 240, 240)
        draw.text((x + 4, y + 4), label, fill=text_color, font=font)
        x += _SWATCH_W + 2
    y += _SWATCH_H + 8

    # --- Row 2: final palette ---
    draw.text((10, y + 2), "Final palette:", fill=(160, 160, 160), font=font)
    y += _LABEL_H
    x = 10
    for role in palette_roles:
        hex_val = palette[role]
        r, g, b = hex_to_rgb(hex_val)
        draw.rectangle([x, y, x + _SWATCH_W - 1, y + _SWATCH_H - 1], fill=(r, g, b))
        L, _, _ = rgb_to_lab(r, g, b)
        text_color = (10, 10, 10) if L > 50 else (240, 240, 240)
        draw.text((x + 4, y + 4), f"{role}\n{hex_val}", fill=text_color, font=font)
        x += _SWATCH_W + 2
    y += _SWATCH_H + 8

    canvas.save(output_path)
    print(f"[preview] saved: {output_path}", file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="photo_color_pipeline.py",
        description="Extract a pixel-art palette from creature photographs.",
    )
    p.add_argument(
        "images",
        nargs="+",
        metavar="IMAGE",
        help="Source image paths (JPEG, PNG, etc.)",
    )
    p.add_argument(
        "-n", "--name",
        dest="creature_name",
        default="creature",
        help="Creature name for output metadata (default: creature)",
    )
    p.add_argument(
        "--signature-color",
        metavar="#HEX",
        default=None,
        help="Override the primary palette color with this hex value",
    )
    p.add_argument(
        "--num-colors",
        type=int,
        default=3,
        choices=[3, 4, 5],
        help="Number of subject palette colors A-C/D/E (default: 3)",
    )
    p.add_argument(
        "--no-rembg",
        action="store_true",
        help="Skip background removal (use for images already stripped)",
    )
    p.add_argument(
        "--merge-threshold",
        type=float,
        default=15.0,
        metavar="DE",
        help="ΔE merge threshold for cross-reference clustering (default: 15.0)",
    )
    p.add_argument(
        "--max-source-colors",
        type=int,
        default=8,
        metavar="N",
        help="Colors to extract per source image before filtering (default: 8)",
    )
    p.add_argument(
        "--preview",
        action="store_true",
        help="Save a color swatch preview PNG alongside the JSON output",
    )
    p.add_argument(
        "-o", "--output",
        metavar="FILE",
        default=None,
        help="Output JSON path (default: {creature_name}_palette.json)",
    )
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Validate inputs
    for path in args.images:
        if not Path(path).exists():
            sys.exit(f"ERROR: image not found: {path}")

    if args.signature_color and not args.signature_color.startswith("#"):
        args.signature_color = "#" + args.signature_color

    result = extract_creature_palette(
        image_paths=args.images,
        creature_name=args.creature_name,
        signature_color=args.signature_color,
        num_colors=args.num_colors,
        use_rembg=not args.no_rembg,
        merge_threshold=args.merge_threshold,
        max_source_colors=args.max_source_colors,
    )

    # Determine output paths
    out_json = args.output or f"{args.creature_name.replace(' ', '_')}_palette.json"
    out_path = Path(out_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"[output] palette JSON saved: {out_path}", file=sys.stderr)

    # Print palette summary to stdout (for pipe-friendly usage)
    print(json.dumps(result["palette"], indent=2))

    # Preview
    if args.preview:
        images = load_and_strip(args.images, use_rembg=not args.no_rembg)
        preview_path = out_path.with_suffix(".preview.png")
        save_preview(result, images, str(preview_path))

        # Also save stripped versions of each source image
        for i, (img, path) in enumerate(zip(images, args.images)):
            stem = Path(path).stem
            stripped_path = out_path.parent / f"{stem}_stripped.png"
            img.save(str(stripped_path))
            print(f"[preview] stripped image saved: {stripped_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
