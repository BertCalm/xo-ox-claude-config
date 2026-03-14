---
name: Brand Site Engine Samples
description: Pending task — render 20 hero preset audio clips (3s each) from standalone synth plugins for XO-OX.org brand site
type: project
---

## Task: Record Engine Preview Samples for Brand Site

**Status**: Infrastructure built, awaiting sample recordings
**Date added**: 2026-03-12

### What's needed
- 20 short audio clips (2-3 seconds each), one per engine
- Each clip should showcase the engine's signature character — "what does this engine DO?"
- Render from standalone apps or DAW, one hero preset per engine

### Suggested hero presets per engine
Pick the most iconic-sounding preset from each engine:
- OddfeliX: sharp filter snap
- OddOscar: morphing pad
- Overdub: dub echo chord
- Odyssey: drifting psychedelic pad
- Oblong: warm fuzzy texture
- Obese: massive saturated bass
- Onset: full kit hit
- Overworld: chip arpeggio
- Opal: granular cloud
- Overbite: sub bass + bite
- Orbital: spectral shimmer
- Organon: evolving bio texture
- Ouroboros: chaotic feedback
- Obsidian: phase distortion edge
- Origami: folded harmonic
- Oracle: envelope-shaped sweep
- Obscura: resonant body
- Oceanic: tidal pad
- Optic: pulsing rhythm
- Oblique: funky prism bounce

### Workflow
1. Render WAVs from standalone apps (play a note/chord, 3 seconds)
2. Run `Tools/site_audio_export.py` to normalize + convert to MP3/OGG
3. Output lands in `site/audio/`
4. Site auto-detects samples and uses them instead of Web Audio fallback

### Tool
- `Tools/site_audio_export.py` — processes WAVs into web-ready MP3/OGG
- Input: `Tools/site_audio_raw/` (raw WAVs from standalone apps)
- Output: `site/audio/` (web-ready files)
