---
name: xodyssey-engine
description: XOdyssey synth engine — full architecture, build phases, and completion notes
type: project
---

# XOdyssey (XO_OX Designs)

**Status**: COMPLETE — v0.7.0 (March 2026)
**Repo**: `~/Documents/GitHub/XOdyssey/`
**Framework**: JUCE 8.0.12, C++17, CMake + Ninja
**Build**: `cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release && cmake --build build`

## Identity
Psychedelic pad-first synth — Familiar ↔ Alien journey

## Architecture
- ~130 canonical parameters (spec Section 22 + drift amendments)
- 4 macros: JOURNEY (Familiar→Alien + Climax), BREATHE, BLOOM, FRACTURE
- OscA/B: classic, wavetable, supersaw, FM modes
- Dual filter: FilterA (Cytomic SVF LP 12/24), FilterB (3-band parallel SVF formant)
- Character stages: Haze Saturation (pre-filter), Prism Shimmer (post-filter), Fracture (pre-amp)
- 7 Signature Traits: Voyager Drift, Prism Shimmer, Haze Sat, Tidal Pulse, Bloom Attack, Fracture, Climax
- Climax: per-preset JOURNEY threshold, 1-3s S-curve bloom
- 8-slot mod matrix, 3 envelopes, 3 LFOs, `drift` mod source
- 4 FX blocks: Chorus, Phaser, Delay, Reverb + Bass Integrity HPF
- 24-voice poly + legato, oldest-note stealing
- Formant filter: 3 parallel Cytomic SVF BPs, 5 vowel presets
- Wavetable: 2048-sample frames, 32-bit float WAV

## Completion Notes
- 41 source files, ~4700 lines of C++
- AU + Standalone build, auval passes
- 10 hero factory presets
- Custom 2-page UI with XOdyssey LookAndFeel
- JUCE 7 upgraded to 8.0.12 for macOS 15 compatibility
- Wavetable osc mode is placeholder (renders sine) — needs file loading in v2
- VST3, wavetable file loading, and 440 more presets deferred to v2

## Key Docs
- Spec: `docs/XOdyssey_Master_Spec_v1.0.md`
- Design: `docs/plans/2026-03-07-xodyssey-design.md`
- Playbook: `docs/XO_OX_Playbook_v1.0.md`
