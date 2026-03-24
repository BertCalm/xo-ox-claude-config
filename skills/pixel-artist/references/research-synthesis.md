---
name: Pixel Artist Research Synthesis
description: Compiled research from 3 agents on image-to-pixel-art algorithms, shape descriptors, and contour-to-waveform generation. Covers open-source tools, math formulas, and dependency recommendations.
---

# Pixel Artist — Technical Research Synthesis (2026-03-24)

## Dependency Tiers

| Tier | Packages | What It Unlocks |
|------|----------|----------------|
| 0 Core | Pillow + math/struct/wave (stdlib) | Rendering, basic quantization, grid gen, WAV export (16-bit) |
| 1 Enhanced | + basic-colormath + colorgram.py | Perceptual LAB color distance, better palette extraction |
| 2 Photo Mode | + rembg[cpu] with silueta model | Automatic background removal from photos |
| 3 Advanced | + numpy + hitherdither + scikit-image | Professional dithering, sub-pixel contours, FFT wavetables |

## Open-Source Tools Found

### Pixel Art Generation
- **Pyxelate** (github.com/sedthh/pyxelate) — HOG-aware structural downsampling, Bayesian GMM color reduction. Deps: numpy, sklearn, skimage.
- **SD-piXL** (SIGGRAPH Asia 2024) — AI-driven pixel art via score distillation. Deps: PyTorch (heavy).
- **Naive Pillow approach**: resize(NEAREST) + quantize() — zero deps, good baseline.

### Background Removal
- **rembg** (github.com/danielgatis/rembg, ~21.7K stars) — silueta model is 43MB, best lightweight option. Deps: onnxruntime.

### Color Analysis
- **colorgram.py** — Pillow-only, faster than color-thief, better saturation in results.
- **basic-colormath** — Pure Python ΔE2000, no numpy, 14x faster than python-colormath.
- **CIE LAB conversion** — Pure math: RGB→linearRGB→XYZ(D65)→LAB. All formulas confirmed.

### Shape Descriptors (all Pillow + math only)
- Isoperimetric quotient: 4π·A/P² (circle=1, star≈0.3)
- Crofton's perimeter: (π/4)(N₀+N₄₅+N₉₀+N₁₃₅)·px — better than naive at 16x16
- Bilateral symmetry: IoU(shape, mirror(shape)) after centroid alignment
- Solidity: area / convex_hull_area (Graham scan, pure Python)
- Elongation: √(λ₁/λ₂) from central moment eigenvalues
- Color temperature: average hue → warm/cool scale

### Contour Tracing
- **Moore Neighborhood** — ~80 lines pure Python, well-documented algorithm
- **scikit-image find_contours** — Marching squares with sub-pixel accuracy (needs numpy)

### Contour-to-Waveform (PROVEN CONCEPT)
- **The Contour Synthesizer** (github.com/yonatanrozin/the-contour-synthesizer) — Three methods: amplitude envelope, additive synthesis, direct waveform substitution. Quote: "using the contour of a shape as a custom waveform is guaranteed to produce interesting and varied timbral results."
- **Sonifyd** (Georgia Tech) — Color-to-sound additive synthesis, 80% perceptual accuracy.
- **MetaSynth** — Pioneer spectral painting tool. Used by Aphex Twin, Jon Hopkins.
- **WavePainter** (Harvard, open source) — Draw-your-own wavetable.
- **osc_gen** (Python, PyPI) — Wavetable generation library.

### Wavetable Technical Specs
- Standard sizes: 2048 (Serum), 1024 (Ableton), 256 (WaveEdit)
- Normalization: [-1, 1] bipolar (NOT [0, 1])
- Sample rate: 44100 Hz always
- Best resampling: FFT zero-pad (bandlimited, auto-looping)
- DC offset: subtract mean after resample, before normalization
- 16-point contour → 8 harmonics — sufficient for distinct timbre

### Multiple Waveforms Per Creature (ranked by musical utility)
1. **Radial contour** — distance from centroid at each angle. Naturally periodic. Most consistent.
2. **Horizontal top-edge** — Y values per column. Most visually intuitive. Richest harmonics.
3. **Interior density** — filled pixels per column. Warmer, smoother tones.
4. **Vertical contour** — X values per row. Least reliable due to symmetry.

Strategy: Generate all 4, store as 4-frame wavetable. Engine morphs between them.

### WAV Export
- 16-bit PCM: Python stdlib wave module (no deps)
- 32-bit float: Manual RIFF header via struct.pack (AudioFormat=0x0003) or scipy.io.wavfile

## Key Academic References
- Yeo & Berger, ICMC 2006 — Raster scanning image sonification
- Ciciliani — Scanline synthesis for digital images
- ACHI 2017 — Contour-to-waveform for sensory substitution
- CCRMA (Julius O. Smith) — Windowed sinc interpolation / digital audio resampling
