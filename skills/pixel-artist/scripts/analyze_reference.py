#!/usr/bin/env python3
"""
analyze_reference.py — Image-to-pixel-art analysis pipeline for XO_OX creatures.

Takes one or more reference images of a creature and produces a JSON spec file
compatible with render.py (which takes grid + palette and renders PNGs at multiple
sizes and variants).

Pipeline stages:
  1. Load references — resize to 128×128 for normalized analysis
  2. Extract dominant colors — colorgram.py (with PIL quantize fallback)
  3. Silhouette extraction — alpha-based or corner-sample background detection
  3b. Shape descriptors — 7 metrics computed on full-resolution silhouette
  3c. Contour tracing — Moore neighborhood boundary tracing + waveform generation
  4. Shape simplification — bounding-box crop, aspect normalization, binary downscale
  5. Color mapping — per-pixel nearest-palette match (CIE LAB), outline pass
  6. Signature color integration — optional primary-color override
  7. Self-evaluation scoring

Usage:
    python3 analyze_reference.py fish.png -n blue_tang --engine OPAL --zone "Open Water"
    python3 analyze_reference.py ref1.png ref2.png -n pistol_shrimp --engine ONSET \\
        --signature-color "#4361ee" --creature "Pistol Shrimp" --zone Sunlit \\
        --preview -o specs/pistol_shrimp.json
"""

import argparse
import json
import math
import os
import sys
from pathlib import Path
from typing import Optional

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")

# Optional enhanced color packages
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


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NORMALIZE_SIZE = 128          # All references resized to this before analysis
FILL_CHARS = ["A", "B", "C", "D", "E"]
OUTLINE_CHAR = "#"
BG_CHAR = "."
DEFAULT_OUTLINE_COLOR = "#1a1a2e"
DEFAULT_COLORS = 5
DEFAULT_SIZES = [16, 32]

# Transparent corners are considered background in alpha-bearing images
ALPHA_THRESHOLD = 128

# Background similarity threshold for no-alpha images (Euclidean RGB distance)
CORNER_SIMILARITY_THRESHOLD = 30


# ---------------------------------------------------------------------------
# Stage 0 — Color helpers
# ---------------------------------------------------------------------------

def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert (R, G, B) integers to a lowercase '#rrggbb' hex string."""
    return f"#{r:02x}{g:02x}{b:02x}"


def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    """
    Convert a '#RRGGBB' or '#RGB' hex string to an (R, G, B) integer tuple.

    Raises ValueError if the string is not a valid hex color.
    """
    h = hex_str.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Invalid hex color: {hex_str!r}")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def color_distance(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> float:
    """
    Return perceptual distance between two (R, G, B) color tuples.

    Uses CIE LAB delta-E via basic-colormath when available, falls back to
    Euclidean RGB distance.
    """
    if _HAS_COLORMATH:
        return get_delta_e(c1, c2)
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))


def find_nearest_color(
    pixel: tuple[int, int, int],
    palette: list[tuple[int, int, int]],
) -> int:
    """
    Return the index of the closest color in *palette* to *pixel*.

    Uses CIE LAB perceptual distance (delta-E) when basic-colormath is available,
    otherwise falls back to Euclidean RGB distance.

    Parameters
    ----------
    pixel:
        (R, G, B) tuple to match.
    palette:
        List of (R, G, B) tuples to search.

    Returns
    -------
    Index into *palette* of the closest match.
    """
    best_idx = 0
    best_dist = float("inf")
    for i, color in enumerate(palette):
        d = color_distance(pixel, color)
        if d < best_dist:
            best_dist = d
            best_idx = i
    return best_idx


def is_near_black(r: int, g: int, b: int, threshold: int = 40) -> bool:
    """Return True if the color is very dark (likely a background outline)."""
    return r < threshold and g < threshold and b < threshold


# ---------------------------------------------------------------------------
# Stage 1 — Load references
# ---------------------------------------------------------------------------

def load_references(image_paths: list[str]) -> list[Image.Image]:
    """
    Load and normalize reference images to 128×128 RGBA.

    Each image is:
    - Opened from disk (supports PNG, JPG, GIF, BMP and any Pillow-supported format)
    - Converted to RGBA
    - Resized to NORMALIZE_SIZE × NORMALIZE_SIZE with LANCZOS resampling

    Parameters
    ----------
    image_paths:
        List of file-system paths to reference images.

    Returns
    -------
    List of PIL Images in RGBA mode, all 128×128.

    Raises
    ------
    SystemExit if any path cannot be opened.
    """
    print(f"[Stage 1] Loading {len(image_paths)} reference image(s)…", file=sys.stderr)
    images: list[Image.Image] = []
    for path in image_paths:
        try:
            img = Image.open(path)
        except OSError as exc:
            sys.exit(f"[error] Cannot open image {path!r}: {exc}")
        img = img.convert("RGBA")
        img = img.resize((NORMALIZE_SIZE, NORMALIZE_SIZE), Image.LANCZOS)
        images.append(img)
        print(f"  loaded: {path}", file=sys.stderr)
    return images


# ---------------------------------------------------------------------------
# Stage 2 — Extract dominant colors
# ---------------------------------------------------------------------------

def build_composite(images: list[Image.Image]) -> Image.Image:
    """
    Tile all *images* side-by-side into a single composite RGBA image.

    All images must be the same size (NORMALIZE_SIZE × NORMALIZE_SIZE).

    Parameters
    ----------
    images:
        List of same-size RGBA PIL Images.

    Returns
    -------
    A single RGBA image whose width = len(images) * image_width.
    """
    w, h = images[0].size
    composite = Image.new("RGBA", (w * len(images), h), (0, 0, 0, 0))
    for i, img in enumerate(images):
        composite.paste(img, (i * w, 0))
    return composite


def extract_dominant_colors_colorgram(
    image_paths: list[str],
    n_colors: int,
) -> list[tuple[tuple[int, int, int], float]]:
    """
    Extract dominant colors using colorgram.py for better saturation quality.

    Parameters
    ----------
    image_paths:
        Original file paths (colorgram works on-disk paths better).
    n_colors:
        Number of colors to extract.

    Returns
    -------
    List of ((R, G, B), proportion) pairs sorted by proportion descending.
    """
    # Use the first path as primary source; combine all into composite if multiple
    all_colors: list[tuple[tuple[int, int, int], float]] = []
    for path in image_paths:
        extracted = colorgram.extract(path, n_colors + 4)
        for c in extracted:
            rgb = (c.rgb.r, c.rgb.g, c.rgb.b)
            if not is_near_black(*rgb):
                all_colors.append((rgb, c.proportion))

    # Merge duplicate-ish colors (within LAB distance 10)
    merged: list[tuple[tuple[int, int, int], float]] = []
    for rgb, prop in all_colors:
        absorbed = False
        for i, (existing_rgb, existing_prop) in enumerate(merged):
            if color_distance(rgb, existing_rgb) < 10:
                # Weighted average by proportion
                total = existing_prop + prop
                blended = tuple(
                    int((existing_rgb[j] * existing_prop + rgb[j] * prop) / total)
                    for j in range(3)
                )
                merged[i] = (blended, total)
                absorbed = True
                break
        if not absorbed:
            merged.append((rgb, prop))

    merged.sort(key=lambda x: x[1], reverse=True)
    return merged[:n_colors]


def extract_dominant_colors(
    images: list[Image.Image],
    n_colors: int = DEFAULT_COLORS,
    image_paths: Optional[list[str]] = None,
) -> list[tuple[tuple[int, int, int], int]]:
    """
    Extract up to *n_colors* dominant (R, G, B) colors from the reference images.

    Strategy:
    - If colorgram is available, uses it for better saturation quality (Tier 1)
    - Otherwise tiles all reference images into a single composite
    - Strips fully-transparent pixels (alpha == 0) before quantizing
    - Uses PIL's median-cut quantize() on the opaque pixels
    - Filters out near-black colors (outline / background artifacts)
    - Sorts remaining colors by pixel frequency (most common first)

    Parameters
    ----------
    images:
        List of normalized RGBA reference images.
    n_colors:
        Maximum number of colors to extract (before near-black filtering).
    image_paths:
        Original file paths (used by colorgram if available).

    Returns
    -------
    List of ((R, G, B), count) pairs sorted by count descending.
    Each entry has a frequency >= 1.
    """
    print(f"[Stage 2] Extracting up to {n_colors} dominant colors…", file=sys.stderr)

    if _HAS_COLORGRAM and image_paths:
        print("  using colorgram.py for palette extraction", file=sys.stderr)
        try:
            color_prop_pairs = extract_dominant_colors_colorgram(image_paths, n_colors)
            # Convert proportions to pseudo-counts (multiply by 10000 for integer representation)
            result = [(rgb, int(prop * 10000)) for rgb, prop in color_prop_pairs]
            print(f"  extracted {len(result)} colors:", file=sys.stderr)
            for (r, g, b), count in result:
                print(f"    {rgb_to_hex(r, g, b)}  (prop~{count/100:.1f}%)", file=sys.stderr)
            return result
        except Exception as exc:
            print(f"  [warn] colorgram failed ({exc}), falling back to PIL quantize", file=sys.stderr)

    composite = build_composite(images)

    # Collect all opaque pixels into a flat RGB image for quantization.
    # We flatten the RGBA composite into RGB, masking out transparent pixels.
    rgba_pixels = list(composite.getdata())
    opaque = [(r, g, b) for r, g, b, a in rgba_pixels if a > 0]

    if not opaque:
        print("  [warn] No opaque pixels found — using fallback gray palette", file=sys.stderr)
        return [((128, 128, 128), 1)]

    # Build a temporary RGB image from opaque pixels for quantization.
    # We need a rectangular image; pad to a square with a dummy pixel if needed.
    side = math.ceil(math.sqrt(len(opaque)))
    # Pad opaque list to fill the square
    padded = opaque + [(0, 0, 0)] * (side * side - len(opaque))

    temp_img = Image.new("RGB", (side, side))
    temp_img.putdata(padded)

    # Quantize with median-cut. PIL returns an indexed palette image.
    # We request more colors than needed so filtering doesn't leave us short.
    quantize_n = min(n_colors + 4, 256)
    quantized = temp_img.quantize(colors=quantize_n, method=Image.Quantize.MEDIANCUT)

    # Extract palette entries: getpalette() returns flat [R,G,B,R,G,B,...] (768 values for 256 colors)
    raw_palette = quantized.getpalette()  # list of ints, length 768

    # Count pixels per palette index
    index_counts: dict[int, int] = {}
    for idx in quantized.getdata():
        index_counts[idx] = index_counts.get(idx, 0) + 1

    # Map index → (R,G,B) and filter
    color_counts: list[tuple[tuple[int, int, int], int]] = []
    for idx, count in index_counts.items():
        r = raw_palette[idx * 3]
        g = raw_palette[idx * 3 + 1]
        b = raw_palette[idx * 3 + 2]
        if is_near_black(r, g, b):
            continue
        color_counts.append(((r, g, b), count))

    # Sort by frequency descending
    color_counts.sort(key=lambda x: x[1], reverse=True)

    # Trim to requested number
    result = color_counts[:n_colors]

    print(f"  extracted {len(result)} colors:", file=sys.stderr)
    for (r, g, b), count in result:
        print(f"    {rgb_to_hex(r, g, b)}  (n={count})", file=sys.stderr)

    return result


# ---------------------------------------------------------------------------
# Stage 3 — Silhouette extraction
# ---------------------------------------------------------------------------

def _average_color(pixels: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    """Return the average (R, G, B) of a list of color tuples."""
    n = len(pixels)
    if n == 0:
        return (0, 0, 0)
    return (
        sum(p[0] for p in pixels) // n,
        sum(p[1] for p in pixels) // n,
        sum(p[2] for p in pixels) // n,
    )


def extract_silhouette(image: Image.Image) -> Image.Image:
    """
    Extract a foreground silhouette from a reference image.

    Detection strategy:
    - If the image has an alpha channel with meaningful variation, pixels with
      alpha > ALPHA_THRESHOLD are foreground.
    - If there is no alpha (or alpha is uniformly opaque), sample the 4 corner
      pixels to estimate the background color. Pixels within
      CORNER_SIMILARITY_THRESHOLD of the background mean are background;
      everything else is foreground.

    Parameters
    ----------
    image:
        An RGBA PIL Image (128×128).

    Returns
    -------
    An "L" mode PIL Image (same size) where 255 = foreground, 0 = background.
    """
    print("[Stage 3] Extracting silhouette…", file=sys.stderr)

    w, h = image.size
    mask = Image.new("L", (w, h), 0)
    mask_pixels = mask.load()
    img_pixels = image.load()

    # Check if alpha channel carries useful information.
    alpha_values = [img_pixels[x, y][3] for y in range(h) for x in range(w)]
    alpha_min = min(alpha_values)
    alpha_max = max(alpha_values)
    has_alpha_variation = (alpha_max - alpha_min) > 10

    if has_alpha_variation:
        print("  using alpha-channel silhouette", file=sys.stderr)
        for y in range(h):
            for x in range(w):
                a = img_pixels[x, y][3]
                mask_pixels[x, y] = 255 if a > ALPHA_THRESHOLD else 0
    else:
        print("  using corner-sample background detection", file=sys.stderr)
        # Sample 4 corner pixels (RGB only)
        corners = [
            img_pixels[0, 0][:3],
            img_pixels[w - 1, 0][:3],
            img_pixels[0, h - 1][:3],
            img_pixels[w - 1, h - 1][:3],
        ]
        bg_color = _average_color(corners)
        print(f"  estimated background: {rgb_to_hex(*bg_color)}", file=sys.stderr)

        for y in range(h):
            for x in range(w):
                pixel_rgb = img_pixels[x, y][:3]
                dist = color_distance(pixel_rgb, bg_color)
                mask_pixels[x, y] = 0 if dist < CORNER_SIMILARITY_THRESHOLD else 255

    fg_count = sum(1 for y in range(h) for x in range(w) if mask_pixels[x, y] == 255)
    print(f"  foreground pixels: {fg_count} / {w * h}", file=sys.stderr)
    return mask


# ---------------------------------------------------------------------------
# Stage 3b — Shape descriptors
# ---------------------------------------------------------------------------

def _rgb_to_hsv(r: int, g: int, b: int) -> tuple[float, float, float]:
    """
    Convert (R, G, B) integers [0-255] to (H, S, V) where H is in [0, 360).

    Returns
    -------
    (hue_degrees, saturation_0_1, value_0_1)
    """
    rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
    cmax = max(rf, gf, bf)
    cmin = min(rf, gf, bf)
    delta = cmax - cmin

    # Hue
    if delta == 0:
        h = 0.0
    elif cmax == rf:
        h = 60.0 * (((gf - bf) / delta) % 6)
    elif cmax == gf:
        h = 60.0 * (((bf - rf) / delta) + 2)
    else:
        h = 60.0 * (((rf - gf) / delta) + 4)

    # Saturation
    s = 0.0 if cmax == 0 else delta / cmax

    # Value
    v = cmax

    return h, s, v


def _graham_scan_convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Compute the convex hull of a list of (x, y) integer points using Graham scan.

    Returns the hull as an ordered list of (x, y) points (CCW winding).
    Returns [] if fewer than 3 points are provided.
    """
    n = len(points)
    if n < 3:
        return points[:]

    # Find lowest-then-leftmost point as pivot
    pivot = min(points, key=lambda p: (p[1], p[0]))

    def polar_angle(p: tuple[int, int]) -> float:
        return math.atan2(p[1] - pivot[1], p[0] - pivot[0])

    def dist_sq(p: tuple[int, int]) -> float:
        return (p[0] - pivot[0]) ** 2 + (p[1] - pivot[1]) ** 2

    # Sort by angle, breaking ties by distance
    sorted_pts = sorted(points, key=lambda p: (polar_angle(p), dist_sq(p)))

    # Remove points with same angle (keep farthest)
    filtered: list[tuple[int, int]] = []
    i = 0
    while i < len(sorted_pts):
        j = i + 1
        while j < len(sorted_pts) and math.isclose(
            polar_angle(sorted_pts[i]), polar_angle(sorted_pts[j]), abs_tol=1e-9
        ):
            j += 1
        # Keep the farthest point at this angle
        filtered.append(sorted_pts[j - 1])
        i = j

    if len(filtered) < 3:
        return filtered

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    hull: list[tuple[int, int]] = []
    for p in filtered:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull


def _shoelace_area(polygon: list[tuple[int, int]]) -> float:
    """Compute the area of a polygon using the Shoelace formula."""
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0


def _polygon_perimeter(polygon: list[tuple[int, int]]) -> float:
    """Compute the perimeter of a polygon."""
    n = len(polygon)
    if n < 2:
        return 0.0
    total = 0.0
    for i in range(n):
        j = (i + 1) % n
        dx = polygon[j][0] - polygon[i][0]
        dy = polygon[j][1] - polygon[i][1]
        total += math.sqrt(dx * dx + dy * dy)
    return total


def compute_shape_descriptors(
    mask_image: Image.Image,
    color_image: Image.Image,
) -> dict:
    """
    Compute 7 shape and color descriptors from the full-resolution silhouette.

    Operates on the NORMALIZE_SIZE (128×128) mask and color images, not the
    downscaled pixel-art grids.

    Parameters
    ----------
    mask_image:
        Binary "L" mode PIL Image (255 = foreground, 0 = background).
    color_image:
        RGBA PIL Image aligned with mask_image for color temperature calculation.

    Returns
    -------
    Dict with keys:
        isoperimetric_quotient (float 0-1): shape circularity
        symmetry (float 0-1): horizontal bilateral symmetry (IoU)
        solidity (float 0-1): area / convex hull area
        density (float 0-1): foreground / bounding box area
        aspect_ratio (float 0.1-10): bounding box width / height
        color_temperature (float -1 to 1): warm (+1) to cool (-1)
        convexity (float 0-1): convex hull perimeter / actual perimeter
    """
    print("[Stage 3b] Computing shape descriptors…", file=sys.stderr)

    w, h = mask_image.size
    pixels = mask_image.load()
    color_px = color_image.load()

    # Collect foreground pixels
    fg_pixels: list[tuple[int, int]] = []
    for y in range(h):
        for x in range(w):
            if pixels[x, y] == 255:
                fg_pixels.append((x, y))

    area = len(fg_pixels)

    if area == 0:
        print("  [warn] No foreground pixels — returning zero descriptors", file=sys.stderr)
        return {
            "isoperimetric_quotient": 0.0,
            "symmetry": 0.0,
            "solidity": 0.0,
            "density": 0.0,
            "aspect_ratio": 1.0,
            "color_temperature": 0.0,
            "convexity": 0.0,
        }

    # --- Bounding box ---
    min_x = min(p[0] for p in fg_pixels)
    max_x = max(p[0] for p in fg_pixels)
    min_y = min(p[1] for p in fg_pixels)
    max_y = max(p[1] for p in fg_pixels)
    bbox_w = max(1, max_x - min_x + 1)
    bbox_h = max(1, max_y - min_y + 1)
    bbox_area = bbox_w * bbox_h

    # --- Centroid ---
    cx = sum(p[0] for p in fg_pixels) / area
    cy = sum(p[1] for p in fg_pixels) / area

    # --- Perimeter (4-connected: foreground pixels with at least one background neighbor) ---
    fg_set = set(fg_pixels)
    perimeter = 0
    for (x, y) in fg_pixels:
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in fg_set:
                perimeter += 1
                break

    # --- 1. Isoperimetric quotient (spikiness) ---
    # 4π × area / perimeter²; circle = 1.0, spiky shapes → low
    if perimeter > 0:
        iq = (4 * math.pi * area) / (perimeter * perimeter)
        iq = min(1.0, max(0.0, iq))
    else:
        iq = 0.0

    # --- 2. Symmetry (horizontal bilateral IoU) ---
    # Mirror the mask horizontally, center on centroid, compute IoU
    mirrored = ImageOps.mirror(mask_image)
    mirror_px = mirrored.load()

    # Centroid-based offset for alignment
    # In the mirrored image, the centroid x becomes (w - 1 - cx)
    # We need to shift so both centroids align
    mirror_cx = w - 1 - cx
    shift_x = int(round(cx - mirror_cx))

    mirror_fg: set[tuple[int, int]] = set()
    for y in range(h):
        for x in range(w):
            if mirror_px[x, y] == 255:
                nx = x + shift_x
                if 0 <= nx < w:
                    mirror_fg.add((nx, y))

    intersection = len(fg_set & mirror_fg)
    union = len(fg_set | mirror_fg)
    symmetry = intersection / union if union > 0 else 0.0

    # --- 3. Solidity (area / convex hull area) via Graham scan ---
    # Sub-sample for performance (take every 2nd pixel if area is large)
    sample = fg_pixels if area <= 2000 else fg_pixels[::max(1, area // 2000)]
    hull = _graham_scan_convex_hull(sample)
    hull_area = _shoelace_area(hull)
    solidity = area / hull_area if hull_area > 0 else 1.0
    solidity = min(1.0, max(0.0, solidity))

    # --- 4. Density (fill ratio) ---
    density = area / bbox_area if bbox_area > 0 else 0.0
    density = min(1.0, max(0.0, density))

    # --- 5. Aspect ratio ---
    aspect_ratio = bbox_w / bbox_h if bbox_h > 0 else 1.0
    aspect_ratio = max(0.1, min(10.0, aspect_ratio))

    # --- 6. Color temperature ---
    # Convert foreground pixels to HSV, average hue, map to warm/cool scale
    hue_values: list[float] = []
    for (x, y) in fg_pixels:
        rgba = color_px[x, y]
        r, g, b = rgba[0], rgba[1], rgba[2]
        hue, sat, val = _rgb_to_hsv(r, g, b)
        if sat > 0.1 and val > 0.1:  # skip near-gray pixels
            hue_values.append(hue)

    if hue_values:
        avg_hue = sum(hue_values) / len(hue_values)
        # warm: hue < 60 (red/orange/yellow) or > 300 (red/magenta)
        # neutral: hue 60-180 (yellow-green-cyan)
        # cool: hue 180-300 (cyan-blue-violet)
        if avg_hue < 60 or avg_hue >= 300:
            color_temperature = 1.0  # warm
        elif 60 <= avg_hue < 180:
            color_temperature = 0.0  # neutral
        else:
            color_temperature = -1.0  # cool
    else:
        color_temperature = 0.0

    # --- 7. Convexity (convex hull perimeter / actual perimeter) ---
    hull_perimeter = _polygon_perimeter(hull)
    convexity = hull_perimeter / perimeter if perimeter > 0 else 1.0
    convexity = min(1.0, max(0.0, convexity))

    descriptors = {
        "isoperimetric_quotient": round(iq, 4),
        "symmetry": round(symmetry, 4),
        "solidity": round(solidity, 4),
        "density": round(density, 4),
        "aspect_ratio": round(aspect_ratio, 4),
        "color_temperature": round(color_temperature, 4),
        "convexity": round(convexity, 4),
    }

    print(f"  isoperimetric_quotient: {descriptors['isoperimetric_quotient']:.4f}", file=sys.stderr)
    print(f"  symmetry:               {descriptors['symmetry']:.4f}", file=sys.stderr)
    print(f"  solidity:               {descriptors['solidity']:.4f}", file=sys.stderr)
    print(f"  density:                {descriptors['density']:.4f}", file=sys.stderr)
    print(f"  aspect_ratio:           {descriptors['aspect_ratio']:.4f}", file=sys.stderr)
    print(f"  color_temperature:      {descriptors['color_temperature']:.4f}", file=sys.stderr)
    print(f"  convexity:              {descriptors['convexity']:.4f}", file=sys.stderr)

    return descriptors


# ---------------------------------------------------------------------------
# Stage 3c — Contour tracing and waveform generation
# ---------------------------------------------------------------------------

def trace_contour(mask_image: Image.Image) -> list[tuple[int, int]]:
    """
    Trace the outer boundary of the foreground silhouette using Moore neighborhood.

    Algorithm:
    1. Scan top-to-bottom, left-to-right for first foreground pixel (start pixel)
    2. From each current pixel, check 8 neighbors clockwise starting from the
       direction we came from (Jacob's stopping criterion)
    3. First foreground neighbor encountered = next boundary pixel
    4. Stop when we return to the start pixel from the same entry direction

    Parameters
    ----------
    mask_image:
        Binary "L" mode PIL Image (255 = foreground, 0 = background).

    Returns
    -------
    Ordered list of (x, y) pixel coordinates forming the contour.
    Returns [] if no foreground pixels found.
    """
    print("[Stage 3c] Tracing contour (Moore neighborhood)…", file=sys.stderr)

    w, h = mask_image.size
    pixels = mask_image.load()

    # 8-connected clockwise neighbor offsets starting from "up" direction
    # Order: up, up-right, right, down-right, down, down-left, left, up-left
    CLOCKWISE = [
        (0, -1),   # 0: up
        (1, -1),   # 1: up-right
        (1, 0),    # 2: right
        (1, 1),    # 3: down-right
        (0, 1),    # 4: down
        (-1, 1),   # 5: down-left
        (-1, 0),   # 6: left
        (-1, -1),  # 7: up-left
    ]

    def is_fg(x: int, y: int) -> bool:
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        return pixels[x, y] == 255

    # Find start pixel (first foreground pixel scanning top-left to bottom-right)
    start: Optional[tuple[int, int]] = None
    for y in range(h):
        for x in range(w):
            if is_fg(x, y):
                start = (x, y)
                break
        if start is not None:
            break

    if start is None:
        print("  [warn] No foreground pixels found, empty contour", file=sys.stderr)
        return []

    # For a single pixel, return just that pixel
    contour = [start]

    # Find entry direction: we entered start from "above" (a background pixel that's
    # above us) — standard initialization is to come from the left (direction index 6)
    # We start searching clockwise from the direction we came from + 1
    # Initialize: pretend we came from the left background pixel
    entry_dir = 6  # came from left

    current = start

    # Rotate clockwise starting from (entry_dir + 1) mod 8
    def next_clockwise_fg(cx, cy, from_dir):
        """Find next clockwise foreground neighbor starting after from_dir."""
        start_idx = (from_dir + 1) % 8
        for i in range(8):
            idx = (start_idx + i) % 8
            dx, dy = CLOCKWISE[idx]
            nx, ny = cx + dx, cy + dy
            if is_fg(nx, ny):
                return (nx, ny), idx
        return None, -1

    # Jacob's stopping criterion: stop when we revisit start with same entry direction
    # Also cap at w*h*2 to prevent infinite loops on degenerate masks
    max_steps = w * h * 2
    step = 0

    prev_dir = entry_dir
    while step < max_steps:
        next_pt, next_dir = next_clockwise_fg(current[0], current[1], prev_dir)
        if next_pt is None:
            break  # isolated pixel

        # Stopping criterion: returned to start from same entry direction
        if next_pt == start and contour and len(contour) > 1:
            break

        contour.append(next_pt)
        # Entry direction for next pixel = opposite of the direction we moved
        # i.e., if we moved "right" (dir 2), we came from "left" (dir 6)
        prev_dir = (next_dir + 4) % 8
        current = next_pt
        step += 1

    print(f"  contour: {len(contour)} boundary pixels", file=sys.stderr)
    return contour


def contour_to_waveform(
    contour_points: list[tuple[int, int]],
    num_samples: int = 2048,
) -> list[float]:
    """
    Convert a contour boundary to a normalized audio waveform.

    Strategy:
    - Extract Y-coordinates (top-edge profile) from the contour
    - Normalize to [-1, 1] range
    - Resample to num_samples using linear interpolation
    - Remove DC offset (subtract mean)

    Parameters
    ----------
    contour_points:
        Ordered list of (x, y) tuples from trace_contour().
    num_samples:
        Number of samples in the output waveform (default 2048, Serum standard).

    Returns
    -------
    List of floats in [-1, 1] (approximately, after DC removal).
    Returns list of zeros if no contour points.
    """
    if not contour_points:
        return [0.0] * num_samples

    # Extract Y-coordinates from contour
    y_values = [float(pt[1]) for pt in contour_points]
    n = len(y_values)

    if n == 0:
        return [0.0] * num_samples

    # Normalize Y-coordinates to [-1, 1]
    y_min = min(y_values)
    y_max = max(y_values)
    y_range = y_max - y_min
    if y_range == 0:
        normalized = [0.0] * n
    else:
        # Invert: low Y (top of image) → positive, high Y (bottom) → negative
        normalized = [1.0 - 2.0 * (v - y_min) / y_range for v in y_values]

    # Resample to num_samples via linear interpolation
    resampled: list[float] = []
    for i in range(num_samples):
        # Map output index to input index position
        t = i / (num_samples - 1) * (n - 1)
        lo = int(t)
        hi = min(lo + 1, n - 1)
        frac = t - lo
        val = normalized[lo] * (1.0 - frac) + normalized[hi] * frac
        resampled.append(val)

    # Remove DC offset
    mean = sum(resampled) / len(resampled)
    resampled = [v - mean for v in resampled]

    # Round to 5 decimal places to keep JSON compact
    return [round(v, 5) for v in resampled]


# ---------------------------------------------------------------------------
# Stage 4 — Shape simplification
# ---------------------------------------------------------------------------

def _bounding_box(mask: Image.Image) -> tuple[int, int, int, int]:
    """
    Find the bounding box of non-zero pixels in an "L" mode mask.

    Returns (left, top, right, bottom) in pixel coordinates (inclusive).
    Returns (0, 0, w-1, h-1) if the mask is entirely background.
    """
    w, h = mask.size
    pixels = mask.load()
    min_x, min_y = w, h
    max_x, max_y = 0, 0
    found = False
    for y in range(h):
        for x in range(w):
            if pixels[x, y] > 0:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                found = True
    if not found:
        return (0, 0, w - 1, h - 1)
    return (min_x, min_y, max_x, max_y)


def simplify_shape(
    mask: Image.Image,
    target_sizes: list[int],
    padding: int = 1,
) -> dict[int, Image.Image]:
    """
    Crop to bounding box, square-pad, and downscale the silhouette mask.

    Steps for each target size:
    1. Find bounding box of foreground in *mask*
    2. Crop to bounding box and add *padding* pixels on all sides
    3. Square-pad the shorter dimension to make a square image
    4. Resize to target size using LANCZOS
    5. Threshold at 128 to produce a clean binary mask

    Parameters
    ----------
    mask:
        Binary "L" mode silhouette image (255 = foreground).
    target_sizes:
        List of integer sizes (e.g. [16, 32]) to produce masks for.
    padding:
        Pixel padding added around the bounding box before squaring.

    Returns
    -------
    Dict mapping each target size to its simplified binary "L" mode PIL Image.
    """
    print(f"[Stage 4] Simplifying shape to sizes: {target_sizes}…", file=sys.stderr)

    left, top, right, bottom = _bounding_box(mask)
    crop_w = right - left + 1
    crop_h = bottom - top + 1

    # Crop to bounding box with padding
    padded_left = max(0, left - padding)
    padded_top = max(0, top - padding)
    padded_right = min(mask.width - 1, right + padding)
    padded_bottom = min(mask.height - 1, bottom + padding)

    cropped = mask.crop((padded_left, padded_top, padded_right + 1, padded_bottom + 1))
    cw, ch = cropped.size

    # Square-pad
    side = max(cw, ch)
    squared = Image.new("L", (side, side), 0)
    offset_x = (side - cw) // 2
    offset_y = (side - ch) // 2
    squared.paste(cropped, (offset_x, offset_y))

    result: dict[int, Image.Image] = {}
    for size in target_sizes:
        resized = squared.resize((size, size), Image.LANCZOS)
        # Threshold to clean binary
        pixels = resized.load()
        out = Image.new("L", (size, size), 0)
        out_px = out.load()
        for y in range(size):
            for x in range(size):
                out_px[x, y] = 255 if pixels[x, y] >= 128 else 0
        result[size] = out
        fg = sum(1 for y in range(size) for x in range(size) if out_px[x, y] == 255)
        print(f"  {size}×{size}: {fg} foreground pixels", file=sys.stderr)

    return result


# ---------------------------------------------------------------------------
# Stage 5 — Color mapping
# ---------------------------------------------------------------------------

def add_outline(
    grid: list[str],
    fg_char_set: set[str],
    outline_char: str = OUTLINE_CHAR,
    bg_char: str = BG_CHAR,
) -> list[str]:
    """
    Add outline characters to a character grid.

    Any foreground pixel (in *fg_char_set*) that is 4-connected to a background
    pixel (BG_CHAR) is replaced with *outline_char*.  The pass is non-destructive:
    it builds a new grid rather than mutating in place.

    Parameters
    ----------
    grid:
        List of equal-length strings, each character a palette key.
    fg_char_set:
        Set of characters considered foreground fill (e.g. {"A","B","C","D","E"}).
    outline_char:
        Character to use for outline pixels (default "#").
    bg_char:
        Character that represents background / transparent (default ".").

    Returns
    -------
    New list of strings with outline characters inserted.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    result = [list(row) for row in grid]

    for y in range(rows):
        for x in range(cols):
            ch = grid[y][x]
            if ch not in fg_char_set:
                continue
            # Check 4-connected neighbors
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
                    # Edge of grid counts as "adjacent to background"
                    result[y][x] = outline_char
                    break
                if grid[ny][nx] == bg_char:
                    result[y][x] = outline_char
                    break

    return ["".join(row) for row in result]


def _crop_and_resize_image(
    image: Image.Image,
    mask: Image.Image,
    target_size: int,
    padding: int = 1,
) -> Image.Image:
    """
    Crop *image* using the bounding box from *mask*, square-pad, and resize.

    Mirrors the same geometry as simplify_shape() so pixel coordinates align
    between the color image and the binary mask.

    Parameters
    ----------
    image:
        Source RGBA reference image (same size as *mask*).
    mask:
        Binary "L" silhouette mask for *image*.
    target_size:
        Output square size in pixels.
    padding:
        Pixel padding matching what was used in simplify_shape().

    Returns
    -------
    RGBA PIL Image at (target_size × target_size).
    """
    left, top, right, bottom = _bounding_box(mask)

    padded_left = max(0, left - padding)
    padded_top = max(0, top - padding)
    padded_right = min(mask.width - 1, right + padding)
    padded_bottom = min(mask.height - 1, bottom + padding)

    cropped = image.crop((padded_left, padded_top, padded_right + 1, padded_bottom + 1))
    cw, ch = cropped.size

    side = max(cw, ch)
    squared = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    offset_x = (side - cw) // 2
    offset_y = (side - ch) // 2
    squared.paste(cropped, (offset_x, offset_y))

    return squared.resize((target_size, target_size), Image.LANCZOS)


def map_colors_to_grid(
    reference_image: Image.Image,
    reference_mask: Image.Image,
    simplified_masks: dict[int, Image.Image],
    palette_rgb: list[tuple[int, int, int]],
    target_sizes: list[int],
) -> dict[int, list[str]]:
    """
    Map extracted palette colors onto the creature shape to produce character grids.

    For each target size:
    1. Crop and resize the reference image to match the simplified mask geometry
    2. For each foreground pixel, find the nearest palette color (CIE LAB) → assign fill char
    3. Background pixels get BG_CHAR
    4. Run an outline pass: fill pixels adjacent to background → OUTLINE_CHAR

    Parameters
    ----------
    reference_image:
        Best-quality RGBA reference image for color sampling (128×128).
    reference_mask:
        The raw silhouette mask corresponding to *reference_image*.
    simplified_masks:
        Dict of {size: binary "L" mask} from simplify_shape().
    palette_rgb:
        Ordered list of (R, G, B) tuples (index 0 → 'A', 1 → 'B', etc.).
    target_sizes:
        List of grid sizes to produce.

    Returns
    -------
    Dict mapping each target size to a list of strings (the character grid).
    Each row is exactly *size* characters wide.
    """
    print("[Stage 5] Mapping colors to character grids…", file=sys.stderr)
    if _HAS_COLORMATH:
        print("  using CIE LAB delta-E for color matching", file=sys.stderr)
    else:
        print("  using Euclidean RGB distance (install basic-colormath for LAB)", file=sys.stderr)

    grids: dict[int, list[str]] = {}
    fill_chars = FILL_CHARS[: len(palette_rgb)]

    for size in target_sizes:
        small_mask = simplified_masks[size]
        small_color = _crop_and_resize_image(reference_image, reference_mask, size)

        mask_px = small_mask.load()
        color_px = small_color.load()

        grid: list[list[str]] = []
        for y in range(size):
            row: list[str] = []
            for x in range(size):
                if mask_px[x, y] < 128:
                    row.append(BG_CHAR)
                else:
                    pixel_rgba = color_px[x, y]
                    pixel_rgb = pixel_rgba[:3]
                    idx = find_nearest_color(pixel_rgb, palette_rgb)
                    row.append(fill_chars[idx])
            grid.append(row)

        # Convert to strings for the outline pass
        str_grid = ["".join(row) for row in grid]
        str_grid = add_outline(str_grid, set(fill_chars), OUTLINE_CHAR, BG_CHAR)

        # Guarantee exact width (pad with BG_CHAR if needed)
        str_grid = [row.ljust(size, BG_CHAR)[:size] for row in str_grid]

        grids[size] = str_grid

        fill_count = sum(
            1 for row in str_grid for ch in row if ch in fill_chars
        )
        outline_count = sum(
            1 for row in str_grid for ch in row if ch == OUTLINE_CHAR
        )
        print(
            f"  {size}×{size}: {fill_count} fill pixels, {outline_count} outline pixels",
            file=sys.stderr,
        )

    return grids


# ---------------------------------------------------------------------------
# Stage 6 — Signature color integration
# ---------------------------------------------------------------------------

def apply_signature_color(
    palette_rgb: list[tuple[int, int, int]],
    signature_hex: str,
) -> list[tuple[int, int, int]]:
    """
    Replace the primary (index 0) palette color with *signature_hex*.

    The simpler approach: directly assign the signature color as primary (A).
    All other colors remain as extracted.

    Parameters
    ----------
    palette_rgb:
        Ordered list of (R, G, B) extracted palette colors.
    signature_hex:
        '#RRGGBB' hex string to use as the primary color.

    Returns
    -------
    New list with index-0 replaced by the signature color.
    """
    print(f"[Stage 6] Applying signature color {signature_hex}…", file=sys.stderr)
    result = list(palette_rgb)
    result[0] = hex_to_rgb(signature_hex)
    return result


# ---------------------------------------------------------------------------
# Stage 7 — Self-evaluation scoring
# ---------------------------------------------------------------------------

def evaluate_output(
    grid: list[str],
    palette: dict,
    mask: Image.Image,
    descriptors: dict,
    target_size: int,
) -> dict:
    """
    Score the pixel-art output on 5 criteria. Prints results to stderr.

    Criteria:
    - Silhouette fill: foreground fills 40-80% of grid area (score 0 or 1)
    - Color economy: ≤4 fill colors at size 16, ≤6 at size 32 (score 0 or 1)
    - Outline integrity: every fill pixel reachable from outline (score 0 or 1)
    - Aspect ratio preserved: bbox ratio within 25% of source bbox ratio (score 0 or 1)
    - Bounding box usage: creature fills >60% of its bounding box (score 0 or 1)

    Parameters
    ----------
    grid:
        List of row strings for one target size.
    palette:
        Palette dict from build_spec() (character → hex or None).
    mask:
        Full-resolution silhouette mask (for aspect ratio reference).
    descriptors:
        Shape descriptor dict from compute_shape_descriptors().
    target_size:
        Integer size of the grid (16, 32, etc.).

    Returns
    -------
    Dict with 'score' (int 0-5) and 'details' (dict of criterion → bool + description).
    """
    print(f"[Stage 7] Evaluating output ({target_size}×{target_size})…", file=sys.stderr)

    n_rows = len(grid)
    n_cols = len(grid[0]) if grid else 0
    total_pixels = n_rows * n_cols

    fill_chars_set = set(FILL_CHARS)
    fill_count = sum(1 for row in grid for ch in row if ch in fill_chars_set)
    outline_count = sum(1 for row in grid for ch in row if ch == OUTLINE_CHAR)
    fg_count = fill_count + outline_count

    details = {}

    # --- 1. Silhouette fill (40-80%) ---
    fill_ratio = fg_count / total_pixels if total_pixels > 0 else 0.0
    criterion_1 = 0.40 <= fill_ratio <= 0.80
    details["silhouette_fill"] = {
        "pass": criterion_1,
        "value": round(fill_ratio, 3),
        "description": f"Foreground fills {fill_ratio*100:.1f}% of grid (target: 40-80%)",
    }

    # --- 2. Color economy ---
    colors_used = len({ch for row in grid for ch in row if ch in fill_chars_set})
    if target_size <= 16:
        criterion_2 = colors_used <= 4
        target_desc = "≤4 at 16px"
    else:
        criterion_2 = colors_used <= 6
        target_desc = "≤6 at 32px+"
    details["color_economy"] = {
        "pass": criterion_2,
        "value": colors_used,
        "description": f"{colors_used} fill colors used (target: {target_desc})",
    }

    # --- 3. Outline integrity: every fill pixel reachable from an outline pixel ---
    # Build adjacency flood-fill from outline pixels into fill pixels
    outline_pixels: set[tuple[int, int]] = set()
    fill_pixels: set[tuple[int, int]] = set()
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == OUTLINE_CHAR:
                outline_pixels.add((x, y))
            elif ch in fill_chars_set:
                fill_pixels.add((x, y))

    # BFS from outline pixels, crossing fill pixels
    reachable: set[tuple[int, int]] = set()
    frontier = list(outline_pixels)
    visited_outline = set(outline_pixels)
    while frontier:
        cx, cy = frontier.pop()
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in fill_pixels and (nx, ny) not in reachable:
                reachable.add((nx, ny))
                frontier.append((nx, ny))

    unreachable = len(fill_pixels) - len(reachable)
    criterion_3 = unreachable == 0 or len(fill_pixels) == 0
    details["outline_integrity"] = {
        "pass": criterion_3,
        "value": unreachable,
        "description": f"{unreachable} fill pixels unreachable from outline (target: 0)",
    }

    # --- 4. Aspect ratio preserved (within 25% of source) ---
    src_aspect = descriptors.get("aspect_ratio", 1.0)
    # Compute grid bbox aspect ratio
    grid_fg_x = [x for y, row in enumerate(grid) for x, ch in enumerate(row)
                 if ch in fill_chars_set or ch == OUTLINE_CHAR]
    grid_fg_y = [y for y, row in enumerate(grid) for x, ch in enumerate(row)
                 if ch in fill_chars_set or ch == OUTLINE_CHAR]
    if grid_fg_x and grid_fg_y:
        grid_bbox_w = max(grid_fg_x) - min(grid_fg_x) + 1
        grid_bbox_h = max(grid_fg_y) - min(grid_fg_y) + 1
        grid_aspect = grid_bbox_w / grid_bbox_h if grid_bbox_h > 0 else 1.0
    else:
        grid_aspect = 1.0
    ratio_diff = abs(grid_aspect - src_aspect) / max(src_aspect, 0.01)
    criterion_4 = ratio_diff <= 0.25
    details["aspect_ratio_preserved"] = {
        "pass": criterion_4,
        "value": round(ratio_diff, 3),
        "description": (
            f"Grid aspect {grid_aspect:.2f} vs source {src_aspect:.2f} "
            f"({ratio_diff*100:.1f}% diff, target ≤25%)"
        ),
    }

    # --- 5. Bounding box usage: creature fills >60% of its bounding box ---
    bbox_fill_ratio = descriptors.get("density", 0.0)
    criterion_5 = bbox_fill_ratio > 0.60
    details["bounding_box_usage"] = {
        "pass": criterion_5,
        "value": round(bbox_fill_ratio, 3),
        "description": f"Creature fills {bbox_fill_ratio*100:.1f}% of bounding box (target: >60%)",
    }

    score = sum(1 for v in details.values() if v["pass"])

    # Print summary
    print(f"  Evaluation score: {score}/5", file=sys.stderr)
    for criterion, info in details.items():
        status = "PASS" if info["pass"] else "FAIL"
        print(f"    [{status}] {criterion}: {info['description']}", file=sys.stderr)

    if score < 3:
        print(
            f"  [WARNING] Score {score}/5 is below threshold — review output quality",
            file=sys.stderr,
        )

    return {"score": score, "details": details}


# ---------------------------------------------------------------------------
# JSON spec assembly
# ---------------------------------------------------------------------------

def build_spec(
    name: str,
    engine: str,
    creature: str,
    zone: str,
    signature_hex: str,
    grids: dict[int, list[str]],
    palette_rgb: list[tuple[int, int, int]],
    outline_hex: str = DEFAULT_OUTLINE_COLOR,
    shape_descriptors: Optional[dict] = None,
    contour_data: Optional[dict] = None,
    evaluation: Optional[dict] = None,
) -> dict:
    """
    Assemble a render.py-compatible JSON spec dict.

    The output is a superset of what render.py expects; new fields
    (shape_descriptors, contour, evaluation) are ignored by render.py.

    Parameters
    ----------
    name:
        Snake-case creature name used as JSON key and file stem.
    engine:
        Engine name string (e.g., "ONSET").
    creature:
        Display name (e.g., "Pistol Shrimp").
    zone:
        Water column zone string (e.g., "Sunlit").
    signature_hex:
        Primary color hex string.
    grids:
        Dict of {size: [list_of_row_strings]}.
    palette_rgb:
        Ordered (R,G,B) palette list; index 0 → A, 1 → B, etc.
    outline_hex:
        Hex color for the '#' outline slot.
    shape_descriptors:
        Optional dict of 7 shape metrics from compute_shape_descriptors().
    contour_data:
        Optional dict with 'points' and 'waveform_2048' from trace_contour().
    evaluation:
        Optional dict from evaluate_output() with score and details.

    Returns
    -------
    Dict ready for json.dump().
    """
    palette_dict: dict = {BG_CHAR: None, OUTLINE_CHAR: outline_hex}
    for i, rgb in enumerate(palette_rgb):
        char = FILL_CHARS[i]
        palette_dict[char] = rgb_to_hex(*rgb)

    grids_dict = {str(size): rows for size, rows in grids.items()}

    spec: dict = {
        "name": name,
        "engine": engine,
        "creature": creature,
        "zone": zone,
        "signature_color": signature_hex,
        "grids": grids_dict,
        "palette": palette_dict,
        "variants": {},
    }

    if shape_descriptors is not None:
        spec["shape_descriptors"] = shape_descriptors

    if contour_data is not None:
        spec["contour"] = contour_data

    if evaluation is not None:
        spec["evaluation"] = evaluation

    return spec


# ---------------------------------------------------------------------------
# Preview mode helpers
# ---------------------------------------------------------------------------

def save_composite_preview(images: list[Image.Image], out_dir: Path) -> None:
    """Save a side-by-side composite of the reference images."""
    composite = build_composite(images)
    # Scale up for visibility (min 256px wide)
    scale = max(1, 256 // composite.width)
    if scale > 1:
        composite = composite.resize(
            (composite.width * scale, composite.height * scale), Image.NEAREST
        )
    path = out_dir / "references_composite.png"
    composite.save(path)
    print(f"  preview: {path}", file=sys.stderr)


def save_palette_preview(
    palette_rgb: list[tuple[int, int, int]],
    outline_hex: str,
    out_dir: Path,
) -> None:
    """Save a swatch strip showing the extracted palette with hex labels."""
    swatch_w, swatch_h = 80, 60
    label_h = 20
    all_colors = [(OUTLINE_CHAR, hex_to_rgb(outline_hex))] + [
        (FILL_CHARS[i], rgb) for i, rgb in enumerate(palette_rgb)
    ]
    total_w = swatch_w * len(all_colors)
    img = Image.new("RGB", (total_w, swatch_h + label_h), (240, 240, 240))

    for i, (char, (r, g, b)) in enumerate(all_colors):
        x_off = i * swatch_w
        # Draw swatch
        for y in range(swatch_h):
            for x in range(swatch_w):
                img.putpixel((x_off + x, y), (r, g, b))
        # Draw a simple text label by rendering individual characters
        # (avoiding font dependency — draw hex digits as colored pixels)
        hex_str = rgb_to_hex(r, g, b)
        label = f"{char}: {hex_str}"
        # Use PIL's default bitmap font if available, else skip
        try:
            draw = ImageDraw.Draw(img)
            draw.text((x_off + 2, swatch_h + 2), label, fill=(40, 40, 40))
        except Exception:
            pass

    path = out_dir / "palette.png"
    img.save(path)
    print(f"  preview: {path}", file=sys.stderr)


def save_silhouette_preview(mask: Image.Image, out_dir: Path) -> None:
    """Save the binary silhouette mask, scaled up for visibility."""
    scale = max(1, 256 // mask.width)
    scaled = mask.resize((mask.width * scale, mask.height * scale), Image.NEAREST)
    path = out_dir / "silhouette.png"
    scaled.save(path)
    print(f"  preview: {path}", file=sys.stderr)


def save_simplified_previews(
    simplified_masks: dict[int, Image.Image], out_dir: Path
) -> None:
    """Save each simplified binary mask scaled up for visibility."""
    for size, mask in simplified_masks.items():
        scale = max(1, 128 // size)
        scaled = mask.resize((size * scale, size * scale), Image.NEAREST)
        path = out_dir / f"simplified_{size}.png"
        scaled.save(path)
        print(f"  preview: {path}", file=sys.stderr)


def save_mapped_previews(
    grids: dict[int, list[str]],
    palette_dict: dict,
    out_dir: Path,
) -> None:
    """
    Render the final character grids using the palette and save as PNGs.

    This lets you preview what the creature will look like before running render.py.
    Each pixel is rendered at native 1:1, then upscaled 8× with NEAREST for visibility.
    """
    for size, grid in grids.items():
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        pixels = img.load()
        for y, row in enumerate(grid):
            for x, ch in enumerate(row):
                hex_color = palette_dict.get(ch)
                if hex_color is None:
                    continue
                r, g, b = hex_to_rgb(hex_color)
                pixels[x, y] = (r, g, b, 255)

        scale = max(1, 256 // size)
        scaled = img.resize((size * scale, size * scale), Image.NEAREST)
        path = out_dir / f"mapped_{size}.png"
        scaled.save(path)
        print(f"  preview: {path}", file=sys.stderr)


def save_shape_descriptor_preview(
    mask_image: Image.Image,
    descriptors: dict,
    out_dir: Path,
) -> None:
    """
    Save an annotated shape descriptor preview image.

    Renders the silhouette with descriptor values overlaid as text.
    """
    # Scale up to 256×256 for readability
    scale = 256 // mask_image.width
    scaled_mask = mask_image.resize(
        (mask_image.width * scale, mask_image.height * scale), Image.NEAREST
    )
    # Convert to RGBA for color overlays
    preview = scaled_mask.convert("RGBA")
    draw = ImageDraw.Draw(preview)

    # Draw descriptor text in top-left
    y_offset = 4
    for key, val in descriptors.items():
        label = f"{key}: {val:.4f}" if isinstance(val, float) else f"{key}: {val}"
        try:
            draw.text((4, y_offset), label, fill=(255, 220, 50, 220))
        except Exception:
            pass
        y_offset += 12

    path = out_dir / "shape_descriptors.png"
    preview.save(path)
    print(f"  preview: {path}", file=sys.stderr)


def save_contour_preview(
    mask_image: Image.Image,
    contour_points: list[tuple[int, int]],
    out_dir: Path,
) -> None:
    """
    Save a preview image with the traced contour overlaid on the silhouette.

    Silhouette rendered in dark gray, contour pixels in bright cyan.
    """
    scale = 256 // mask_image.width
    w, h = mask_image.size
    preview = Image.new("RGBA", (w * scale, h * scale), (30, 30, 40, 255))
    draw = ImageDraw.Draw(preview)

    # Draw silhouette
    mask_px = mask_image.load()
    for y in range(h):
        for x in range(w):
            if mask_px[x, y] == 255:
                draw.rectangle(
                    [x * scale, y * scale, x * scale + scale - 1, y * scale + scale - 1],
                    fill=(80, 80, 100, 200),
                )

    # Draw contour points in cyan
    for px, py in contour_points:
        draw.rectangle(
            [px * scale, py * scale, px * scale + scale - 1, py * scale + scale - 1],
            fill=(0, 220, 220, 255),
        )

    path = out_dir / "contour_overlay.png"
    preview.save(path)
    print(f"  preview: {path}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Best reference selection
# ---------------------------------------------------------------------------

def pick_best_reference(
    image_paths: list[str],
    images: list[Image.Image],
) -> tuple[int, str, Image.Image]:
    """
    Choose the best reference image for color sampling.

    "Best" means highest original resolution. If all are equal (or only one
    image is provided), the first is returned.

    Parameters
    ----------
    image_paths:
        Original file-system paths in input order.
    images:
        Normalized 128×128 RGBA images (same order as *image_paths*).

    Returns
    -------
    (index, path, image) for the chosen reference.
    """
    best_idx = 0
    best_area = 0
    for i, path in enumerate(image_paths):
        try:
            with Image.open(path) as probe:
                area = probe.width * probe.height
            if area > best_area:
                best_area = area
                best_idx = i
        except OSError:
            pass

    return best_idx, image_paths[best_idx], images[best_idx]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="analyze_reference.py",
        description=(
            "Analyze reference images of a creature and produce a pixel-art "
            "JSON spec compatible with render.py."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "images",
        metavar="IMAGE",
        nargs="+",
        help="One or more reference image paths (PNG, JPG, GIF, BMP).",
    )
    parser.add_argument(
        "-n", "--name",
        required=True,
        metavar="NAME",
        help="Creature name in snake_case (e.g., pistol_shrimp). Used as spec key and default output filename.",
    )
    parser.add_argument(
        "--engine",
        default="",
        metavar="ENGINE",
        help="Engine name (e.g., ONSET).",
    )
    parser.add_argument(
        "--creature",
        default="",
        metavar="DISPLAY_NAME",
        help="Display name (e.g., 'Pistol Shrimp'). Defaults to --name title-cased.",
    )
    parser.add_argument(
        "--zone",
        default="",
        metavar="ZONE",
        help="Water column zone (e.g., Sunlit, The Deep).",
    )
    parser.add_argument(
        "--signature-color",
        default=None,
        metavar="#HEX",
        help="Hex color to use as primary (overrides extracted primary). E.g., '#4361ee'.",
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        metavar="OUTPUT_SPEC",
        help="Output JSON spec path (default: ./{name}.json).",
    )
    parser.add_argument(
        "--colors",
        type=int,
        default=DEFAULT_COLORS,
        metavar="N",
        help=f"Number of palette fill colors to extract (default: {DEFAULT_COLORS}, max: {len(FILL_CHARS)}).",
    )
    parser.add_argument(
        "--outline-color",
        default=DEFAULT_OUTLINE_COLOR,
        metavar="#HEX",
        help=f"Hex color for outlines (default: {DEFAULT_OUTLINE_COLOR!r}).",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Save diagnostic preview PNGs to a {name}_analysis/ directory.",
    )
    parser.add_argument(
        "--sizes",
        default="16,32",
        metavar="N,N,...",
        help="Target grid sizes, comma-separated (default: '16,32').",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point: run the full analysis pipeline and write the JSON spec."""
    args = parse_args()

    # Print dependency status
    if _HAS_COLORMATH:
        print("[Info] basic-colormath available: CIE LAB delta-E enabled", file=sys.stderr)
    else:
        print("[Info] basic-colormath not found: using Euclidean RGB distance (pip install basic-colormath)", file=sys.stderr)
    if _HAS_COLORGRAM:
        print("[Info] colorgram.py available: enhanced palette extraction enabled", file=sys.stderr)
    else:
        print("[Info] colorgram not found: using PIL quantize fallback (pip install colorgram.py)", file=sys.stderr)

    # Validate numeric arguments
    n_colors = max(1, min(len(FILL_CHARS), args.colors))
    if args.colors != n_colors:
        print(
            f"[warn] --colors clamped to {n_colors} (valid range: 1–{len(FILL_CHARS)})",
            file=sys.stderr,
        )

    try:
        target_sizes = [int(s.strip()) for s in args.sizes.split(",") if s.strip()]
    except ValueError:
        sys.exit(f"[error] --sizes must be comma-separated integers, got: {args.sizes!r}")
    if not target_sizes:
        sys.exit("[error] --sizes produced an empty list")

    # Derive defaults
    creature_display = args.creature or args.name.replace("_", " ").title()
    output_path = Path(args.output) if args.output else Path(f"./{args.name}.json")
    output_path = output_path.expanduser()

    # --- Stage 1: Load references ---
    images = load_references(args.images)

    # --- Stage 2: Extract dominant colors ---
    color_counts = extract_dominant_colors(
        images, n_colors=n_colors, image_paths=args.images
    )
    palette_rgb: list[tuple[int, int, int]] = [rgb for rgb, _ in color_counts]

    # Pad palette to n_colors if filtering removed entries
    while len(palette_rgb) < n_colors:
        palette_rgb.append((128, 128, 128))

    # --- Pick best reference ---
    best_idx, best_path, best_image = pick_best_reference(args.images, images)
    print(
        f"[Info] Best reference for color sampling: {best_path}",
        file=sys.stderr,
    )

    # --- Stage 3: Silhouette extraction ---
    silhouette_mask = extract_silhouette(best_image)

    # --- Stage 3b: Shape descriptors (on full-resolution silhouette) ---
    shape_descriptors = compute_shape_descriptors(silhouette_mask, best_image)

    # --- Stage 3c: Contour tracing and waveform generation ---
    contour_points = trace_contour(silhouette_mask)
    waveform = contour_to_waveform(contour_points, num_samples=2048)
    contour_data = {
        "points": [[x, y] for x, y in contour_points],
        "waveform_2048": waveform,
    }

    # --- Stage 4: Shape simplification ---
    simplified_masks = simplify_shape(silhouette_mask, target_sizes)

    # --- Stage 5: Color mapping ---
    grids = map_colors_to_grid(
        best_image,
        silhouette_mask,
        simplified_masks,
        palette_rgb,
        target_sizes,
    )

    # --- Stage 6: Signature color (optional) ---
    signature_hex = args.signature_color
    if signature_hex:
        try:
            hex_to_rgb(signature_hex)
        except ValueError as exc:
            sys.exit(f"[error] Invalid --signature-color: {exc}")
        palette_rgb = apply_signature_color(palette_rgb, signature_hex)
    else:
        signature_hex = rgb_to_hex(*palette_rgb[0])

    # --- Stage 7: Self-evaluation (per target size) ---
    # Use the largest size for evaluation (most detail available)
    primary_size = max(target_sizes)
    primary_grid = grids[primary_size]

    # Build palette dict for evaluation (needed for some checks)
    palette_dict_eval: dict = {BG_CHAR: None, OUTLINE_CHAR: args.outline_color}
    for i, rgb in enumerate(palette_rgb):
        palette_dict_eval[FILL_CHARS[i]] = rgb_to_hex(*rgb)

    evaluation = evaluate_output(
        grid=primary_grid,
        palette=palette_dict_eval,
        mask=silhouette_mask,
        descriptors=shape_descriptors,
        target_size=primary_size,
    )

    # Build the spec
    spec = build_spec(
        name=args.name,
        engine=args.engine,
        creature=creature_display,
        zone=args.zone,
        signature_hex=signature_hex,
        grids=grids,
        palette_rgb=palette_rgb,
        outline_hex=args.outline_color,
        shape_descriptors=shape_descriptors,
        contour_data=contour_data,
        evaluation=evaluation,
    )

    # --- Write JSON ---
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, indent=2)
    print(f"\n[Done] Spec written to: {output_path}", file=sys.stderr)
    print(f"       Run: python3 render.py {output_path} -o output/", file=sys.stderr)

    # --- Preview (optional) ---
    if args.preview:
        print("\n[Preview] Saving diagnostic images…", file=sys.stderr)
        preview_dir = output_path.parent / f"{args.name}_analysis"
        preview_dir.mkdir(parents=True, exist_ok=True)

        save_composite_preview(images, preview_dir)
        save_palette_preview(palette_rgb, args.outline_color, preview_dir)
        save_silhouette_preview(silhouette_mask, preview_dir)
        save_simplified_previews(simplified_masks, preview_dir)
        save_mapped_previews(grids, spec["palette"], preview_dir)
        save_shape_descriptor_preview(silhouette_mask, shape_descriptors, preview_dir)
        save_contour_preview(silhouette_mask, contour_points, preview_dir)

        print(f"  preview directory: {preview_dir}", file=sys.stderr)


if __name__ == "__main__":
    main()
