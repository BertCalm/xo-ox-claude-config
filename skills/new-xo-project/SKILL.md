---
name: new-xo-project
description: Scaffold a new XO_OX Designs synth plugin project with JUCE 8, CMake, and the proven XO_OX architecture
---

# New XO_OX Project

Scaffold a new XO_OX Designs instrument plugin from the proven template.

## Arguments
- `name`: Plugin name (e.g., XOppossum, XOverdub)
- `identity`: One-line character description (e.g., "Bass-forward character synth")
- `code`: 4-char JUCE plugin code (e.g., Xops)

## Steps

1. **Create repo**: `~/Documents/GitHub/<name>/`
2. **CMakeLists.txt** from template:
   - JUCE 8.0.12 via FetchContent
   - AU + Standalone formats
   - C++17, arm64+x86_64, deployment target 12.0
   - BUNDLE_ID: `com.xo-ox.<lowercase-name>`
   - PLUGIN_MANUFACTURER_CODE: XoOx
3. **CLAUDE.md** with:
   - Project identity, build command, install command
   - "Parameter IDs are canonical" rule
   - "No heap/mutex/file I/O on audio thread" rule
   - ParamSnapshot pattern reference
   - Signal flow diagram
4. **src/Parameters.h** — empty param list scaffold with ParamSnapshot struct
5. **src/PluginProcessor.h/.cpp** — minimal working processor with APVTS
6. **src/PluginEditor.h/.cpp** — GenericAudioProcessorEditor (UI comes later)
7. **src/engine/** directory with starter files:
   - Voice.h, VoicePool.h, ParamSnapshot.h
   - Oscillator.h (PolyBLEP template from XOdyssey)
   - FilterA.h (Cytomic SVF template)
   - AmpEnvelope.h (ADSR template)
8. **src/preset/PresetManager.h** — empty preset manager scaffold
9. **.claude/settings.json** with Parameter ID protection hook
10. **docs/** directory with placeholder spec
11. **git init** + initial commit
12. **Verify**: `cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release && cmake --build build`

## Template Sources
Reference implementations live in `~/Documents/GitHub/XOdyssey/src/` — reuse the Cytomic SVF, PolyBLEP, ParamSnapshot, and envelope patterns directly.
