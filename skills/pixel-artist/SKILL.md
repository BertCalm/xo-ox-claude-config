---
name: pixel-artist
description: "Generate pixel art creature sprites for XO_OX engines. Designs 16x16 and 32x32 aquatic creatures from the engine mythology, renders to PNG with transparent backgrounds, creates SNES-style palette swap variants, and assembles sprite sheets. Use when the user says 'pixel art', 'creature sprite', 'engine mascot', 'pixel creature', 'sprite sheet', 'palette swap', 'SNES variant', 'color variant', 'make me a sprite', 'draw the creature', 'pixel version of', wants pixel art for any XO_OX engine, wants color variants of existing sprites, wants a sprite sheet assembled, or mentions the Tier 2 creature system. Also use when the user references specific creatures from the aquatic mythology (e.g., 'pistol shrimp for ONSET', 'anglerfish for OVERBITE')."
---

# Pixel Artist — XO_OX Creature Sprite Generator

Generate pixel art sprites for the 71 XO_OX engine creatures. Each engine has an aquatic creature identity with a signature color, water column depth, and visual description. This skill turns those descriptions into actual pixel art rendered as PNGs.

## Output Sizes

Every creature renders at 4 sizes from 2 base grids:

| Base | Scaled (2.5×) | Use Case |
|------|---------------|----------|
| 16×16 | 40×40 | Engine tiles, aquarium icons, favicon-scale |
| 32×32 | 80×80 | Detail view, site cards, marketing, coupling nodes |

The 16×16 is the iconic minimal sprite. The 32×32 adds detail (markings, expression, secondary features). Both get a 2.5× nearest-neighbor upscale for display contexts. All outputs are PNG with transparent backgrounds.

## Workflow

### 1. Pick the creature
Read `references/creature-list.md` for the full 71-engine roster. Each entry has:
- Engine name and number
- Creature name
- Pixel art description (visual features, pose, mood)
- Signature color (hex)

### 2. Design the grid
Design the creature as a character grid where each character maps to a palette color. Design at both 16×16 and 32×32 independently (do NOT just upscale 16→32 — use the extra pixels for detail).

Follow the **Design Guide** below for resolution-specific techniques.

### 3. Define the palette
Every creature gets a base palette with these slots:

| Slot | Character | Purpose |
|------|-----------|---------|
| Transparent | `.` | Background (always null/transparent) |
| Outline | `#` | Dark border defining silhouette |
| Primary | `A` | Main body color (the signature color) |
| Secondary | `B` | Accent/belly/highlight |
| Detail | `C` | Eyes, markings, special features |
| Highlight | `D` | Light reflection, glow, spark |
| Shadow | `E` | Darker shade of primary for depth |

Not every creature needs all slots. 16×16 sprites typically use 3-4 (outline + 2-3 fills). 32×32 can use all 6.

### 4. Write the JSON spec
Save as `specs/{engine_name_lower}.json`:

```json
{
  "name": "pistol_shrimp",
  "engine": "ONSET",
  "creature": "Pistol Shrimp",
  "zone": "Sunlit",
  "signature_color": "#4361ee",
  "grids": {
    "16": [
      "................",
      "......##........",
      ".....#AA#.......",
      "....#AAAA#......",
      "...#AAAAAA#.....",
      "..#BAAAAAAA#....",
      ".#BBAA##AAA#....",
      "#BBB##DD#AA#....",
      "#BBB##DD#AA#....",
      ".#BBAA##AAA#....",
      "..#BAAAAAAA#....",
      "...#AAAAAA#.....",
      "....#AAAA#......",
      ".....#AA#.......",
      "......##........",
      "................"
    ],
    "32": [
      "... (32 rows of 32 characters) ..."
    ]
  },
  "palette": {
    ".": null,
    "#": "#1a1a2e",
    "A": "#4361ee",
    "B": "#00b4d8",
    "C": "#90e0ef",
    "D": "#f72585",
    "E": "#3a0ca3"
  },
  "variants": {
    "fire": {
      "A": "#ff6b35",
      "B": "#ff9f1c",
      "D": "#ffbe0b",
      "E": "#9d0208"
    },
    "ice": {
      "A": "#a2d2ff",
      "B": "#bde0fe",
      "D": "#ffffff",
      "E": "#457b9d"
    }
  }
}
```

### 5. Render
```bash
# Single creature
python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/pistol_shrimp.json -o output/

# All creatures in a directory
python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/ -o output/ --spritesheet

# Specific variant only
python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/pistol_shrimp.json -o output/ --only-variant fire
```

Output structure:
```
output/
├── pistol_shrimp/
│   ├── pistol_shrimp_16x16.png
│   ├── pistol_shrimp_40x40.png        (2.5× of 16)
│   ├── pistol_shrimp_32x32.png
│   ├── pistol_shrimp_80x80.png        (2.5× of 32)
│   ├── pistol_shrimp_16x16_fire.png
│   ├── pistol_shrimp_40x40_fire.png
│   ├── pistol_shrimp_32x32_fire.png
│   ├── pistol_shrimp_80x80_fire.png
│   ├── pistol_shrimp_16x16_ice.png
│   └── ...
├── spritesheet_16x16.png
├── spritesheet_32x32.png
└── manifest.json
```

---

## Design Guide

### Silhouette-First Process

This is the most important principle: **if the creature isn't recognizable from its silhouette alone, no amount of color will save it.**

1. **Block the silhouette** — outline (`#`) only, no fills. Can you tell it's a shrimp? A whale? A jellyfish? If not, reshape.
2. **Fill the body** — primary color (`A`). The creature should now read clearly.
3. **Add the key feature** — the ONE thing that makes this creature unique (oversized claw, spiral shell, tentacles, lure). This feature gets disproportionate pixel budget.
4. **Add accents** — secondary color, eye, highlight. These are seasoning, not structure.
5. **Verify at 1:1** — zoom out to actual size. Still readable? Good.

### 16×16 Design Rules

At 16×16 you have 256 pixels. After outline and padding, maybe 80-100 pixels of actual creature. Every pixel is a design decision.

- **Padding**: Leave 1px transparent border on all sides (gives breathing room in sheets/tiles)
- **Effective canvas**: 14×14 for the creature
- **Colors**: 3-4 max (outline + primary + 1-2 accents)
- **Eyes**: 1 pixel, placed to suggest direction. Use the detail color (`C` or `D`)
- **No anti-aliasing**: Hard pixel edges only. This is the aesthetic.
- **Key feature rule**: The creature's signature feature should occupy 20-30% of the filled pixels. A pistol shrimp's claw should be HUGE relative to its body. A nautilus shell should dominate.
- **Asymmetry**: Slight asymmetry reads as life. Perfectly symmetric creatures feel static.

### 32×32 Design Rules

At 32×32 you have 1024 pixels — 4× the canvas. Do NOT just scale up the 16×16. Redesign to use the space.

- **Padding**: 1-2px transparent border
- **Colors**: 5-7 (add shadow/highlight versions of primary)
- **Eyes**: 2×2 or 3×3 with pupil. Can show expression (happy, menacing, curious)
- **Markings**: Room for spots (ocelot), stripes (clownfish), ridges (coral), patterns
- **Sub-pixel detail**: Use intermediate colors between outline and fill for implied curves
- **Pose**: Can show more dynamic poses — tentacles reaching, fins spread, tail curving
- **Shading**: Use shadow color (`E`) on undersides, highlight on top/light-facing edges

### Color Selection from Signature

Each engine has a signature color. Build the palette from it:

1. **Primary (A)**: The signature color itself
2. **Secondary (B)**: 15-20% lighter OR a complementary tone
3. **Shadow (E)**: 30-40% darker, slightly more saturated
4. **Highlight (D)**: Near-white tint of the signature, or a contrasting spark color
5. **Outline (#)**: Very dark (near-black), optionally tinted toward the signature hue
6. **Detail (C)**: For eyes/markings — either white, black, or a contrasting accent

### Zone-Specific Style Notes

**Sunlit Zone** — Bright, saturated colors. High contrast. Playful poses. Light outlines OK.
**Thermocline** — Colors begin desaturating. More mysterious poses. Moderate contrast.
**The Reef** — Warm, community feel. Rich textures. Coral/amber tones in outlines.
**Open Water** — Bold silhouettes against implied emptiness. Strong outlines.
**The Deep** — Dark palettes with bioluminescent accents. The glow IS the detail.
**The Abyss** — Near-monochrome with single bright accent. Alien shapes. Menacing or ethereal.

---

## SNES Palette Swap System

Palette swaps reuse the same pixel grid with different colors — a technique from 16-bit games where enemy variants shared sprites but swapped palettes for variety.

### Standard Variant Presets

These 8 presets are available for any creature. The outline (`#`) stays unchanged. Only fill colors swap:

| Variant | A (Primary) | B (Secondary) | D (Highlight) | E (Shadow) | Mood |
|---------|-------------|---------------|----------------|------------|------|
| `fire` | `#ff6b35` | `#ff9f1c` | `#ffbe0b` | `#9d0208` | Aggressive, warm |
| `ice` | `#a2d2ff` | `#bde0fe` | `#ffffff` | `#457b9d` | Cold, serene |
| `electric` | `#ffd60a` | `#fff3b0` | `#ffffff` | `#7b2d8e` | Energetic, crackling |
| `toxic` | `#06d6a0` | `#b5e48c` | `#d8f3dc` | `#1b4332` | Venomous, eerie |
| `shadow` | `#2b2d42` | `#3d405b` | `#8d99ae` | `#14213d` | Dark, stealthy |
| `golden` | `#e9c46a` | `#f4a261` | `#fefae0` | `#bc6c25` | Rare, precious |
| `coral` | `#e63946` | `#f4978e` | `#ffddd2` | `#a4133c` | Warm, living |
| `abyss` | `#1d3557` | `#457b9d` | `#00f5d4` | `#0d1b2a` | Deep, bioluminescent |

### Custom Variants

Users can request any custom palette. Define as a partial palette override — only specify the colors that change:

```json
"variants": {
  "synthwave": {
    "A": "#b5179e",
    "B": "#7209b7",
    "D": "#f72585",
    "E": "#3a0ca3"
  }
}
```

### Requesting Variants

Users may say things like:
- "Give me 3 color variants of the pistol shrimp" → pick 3 preset variants that suit the creature's zone
- "Make an ice version of the whale" → apply the `ice` preset
- "I want a synthwave palette for all the Abyss creatures" → custom variant across a zone
- "More variants!" → generate 2-3 new presets not yet applied

When choosing which presets to suggest, match zone to mood:
- Sunlit creatures → fire, electric, golden
- Deep/Abyss creatures → ice, shadow, abyss, toxic
- Reef creatures → coral, golden, fire
- Open Water → ice, electric, shadow

---

## Sprite Sheet Assembly

The render script can assemble all creatures into sprite sheets.

```bash
# Generate sheets organized by zone
python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/ -o output/ --spritesheet --columns 11

# Zone-specific sheets
python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/ -o output/ --spritesheet --group-by-zone
```

Sheet layout: creatures ordered by engine number, left-to-right, top-to-bottom. 2px padding between sprites. Transparent background.

---

## Batch Operations

### Generate all creatures
```bash
# Render entire fleet
python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/ -o output/ --spritesheet

# Render only a specific zone
python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/ -o output/ --zone Sunlit
```

### Add variants to existing creatures
```bash
# Add a new variant to all specs in a directory
python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/ -o output/ \
  --add-variant synthwave A=#b5179e,B=#7209b7,D=#f72585,E=#3a0ca3
```

---

## Manifest

After rendering, the script writes `manifest.json` tracking what's been generated:

```json
{
  "generated": "2026-03-24T...",
  "creatures": [
    {
      "name": "pistol_shrimp",
      "engine": "ONSET",
      "zone": "Sunlit",
      "sizes": [16, 32, 40, 80],
      "variants": ["base", "fire", "ice"],
      "files": ["pistol_shrimp/pistol_shrimp_16x16.png", "..."]
    }
  ],
  "spritesheets": ["spritesheet_16x16.png", "spritesheet_32x32.png"],
  "total_files": 42
}
```

---

## Reference-Driven Pipeline

Instead of designing pixel grids from imagination, use reference images to automatically extract colors and shapes. The `analyze_reference.py` script takes real photos/illustrations and produces JSON specs ready for `render.py`.

### How it works

```
Reference Images → Color Extraction → Shape Simplification → Grid Generation → render.py
```

1. **Source references**: Gather 2-5 images of the target creature (photos, illustrations, existing pixel art from the reference packs)
2. **Run the analyzer**: It extracts dominant colors, finds the silhouette, downscales to 16×16 and 32×32, and maps colors to a character grid
3. **Review and refine**: The output JSON spec can be hand-edited to tweak the grid before rendering
4. **Render**: Feed the spec to render.py for final PNG output at all sizes

### Usage

```bash
# Basic — analyze from reference images
python3 ~/.claude/skills/pixel-artist/scripts/analyze_reference.py \
  ref1.png ref2.png ref3.png \
  -n pistol_shrimp \
  --engine ONSET \
  --creature "Pistol Shrimp" \
  --zone Sunlit \
  --signature-color "#4361ee" \
  -o specs/pistol_shrimp.json

# With preview images showing each analysis stage
python3 ~/.claude/skills/pixel-artist/scripts/analyze_reference.py \
  ref1.png ref2.png \
  -n jellyfish \
  --preview \
  -o specs/jellyfish.json

# Using existing reference packs as source
python3 ~/.claude/skills/pixel-artist/scripts/analyze_reference.py \
  ~/Downloads/Pixel\ Gnome\ Fishing\ Pack/Salt\ Water/Clownfish.png \
  ~/Downloads/Bagatan_Tsuri_rel_2023-01-12/fishes/saltwater/clownfish.png \
  -n circular_clownfish \
  --engine ORBITAL \
  --signature-color "#ff6347" \
  -o specs/circular_clownfish.json
```

### Reference Sources

Two sources are available:

1. **Existing reference packs** (already downloaded in ~/Downloads/):
   - Pixel Gnome Fishing Pack — 52 saltwater + 16 freshwater species, clean outlines
   - Bagatan Tsuri — 154 fish sprites (abyss, freshwater, saltwater)
   - Beowulf Fishes — 171 species at 32×32, 64×64, 128×128
   - MarineAnimals — creature spritesheet
   - lilaxolotl — animated axolotl sprites
   - cursorAxolotls — axolotl cursor sprites in 4 colors

2. **Web image search** — for creatures not in the packs (siphonophore, nudibranch, barreleye). Download 3-5 images with clear backgrounds when possible.

### Best Practices for Reference Selection

- **Multiple angles**: Include side view + top view if available
- **Clear backgrounds**: PNGs with transparency work best (the silhouette extraction is cleaner)
- **Existing pixel art**: Reference pack sprites are ideal — they're already simplified
- **Mix scales**: One detailed photo + one simple illustration often gives the best palette + shape combination

### Pipeline with render.py

The analyzer outputs JSON specs in the exact format render.py expects. Chain them:

```bash
# Analyze → Render in one shot
python3 ~/.claude/skills/pixel-artist/scripts/analyze_reference.py refs/*.png -n my_creature -o specs/my_creature.json \
  && python3 ~/.claude/skills/pixel-artist/scripts/render.py specs/my_creature.json -o output/
```

---

## Dependencies

- Python 3.8+
- Pillow: `pip install Pillow` (used by both `render.py` and `analyze_reference.py`)

---

## Creature List

Read `references/creature-list.md` for the full 71-engine creature roster with descriptions, signature colors, and zone placements. The list is organized by water column zone (Sunlit → Thermocline → Reef → Open Water → Deep → Abyss) plus Kitchen Collection quads.
