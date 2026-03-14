# JUCE Instrument Plugin — Full Specification

## Overview
JUCE-based macOS instrument plugin (AU + VST3) targeting Apple Silicon.
"Precision Analog Instability Synth" — sharp analog-inspired synth with controlled instability.

## Development Phases

### Phase 0 — Project Scaffolding
- JUCE plugin project building AU + VST3 on macOS (Apple Silicon)
- Structure: /Source/PluginProcessor.*, PluginEditor.*, Params/, DSP/, UI/
- Acceptance: Builds, loads in REAPER (VST3) and Logic (AU), blank editor window

### Phase 1 — Parameter System
- APVTS parameter layout with groups: Global, Osc1, Osc2, Sub, Noise, Mixer, Filter, AmpEnv, ModEnv, LFO1, LFO2, Character
- ParamIDs.h with compile-time constants
- Cached parameter pointers (no string lookups in processBlock)
- ParamSnapshot struct captured once per block
- Acceptance: All params in host automation, session recall works

### Phase 2 — Synth Engine Skeleton
- DSP::SynthEngine owning juce::Synthesiser
- DSP::Voice with one band-limited saw (PolyBLEP), amp ADSR, simple gain
- MIDI note + velocity mapping
- Acceptance: Clean tone, no clicks on note-on/off, CPU stable with 16 voices

### Phase 3 — Full Oscillator + Mixer
- Osc1 waveforms: Saw, Pulse (PWM), Triangle (PolyBLEP)
- Osc2 with detune + optional sync
- Sub osc (sine or square)
- Noise generator with tone control
- Mixer: Osc1/Osc2/Sub/Noise levels, Osc balance
- Acceptance: All sources audible/controllable, no aliasing at normal pitch ranges

### Phase 4 — Filter + Drive
- Filter types: LP24, LP12, HP12 with stable resonance
- Pre-filter drive, key tracking, velocity-to-cutoff
- Parameter smoothing for cutoff, resonance, drive
- Acceptance: No zipper/glitch on automation, stable resonance across polyphony

### Phase 5 — Modulation (Minimal)
- Mod ADSR + 2 LFOs (sine/triangle/square/random smooth, optional host sync)
- 6-slot modulation matrix
- Sources: LFO1, LFO2, ModEnv, Velocity, Aftertouch, ModWheel
- Destinations: OscPitch, PWM, FilterCutoff, Drive, StereoWidth, EventDepth
- Consistent internal units (pitch in cents, cutoff as musical ratio)
- Acceptance: Routings audible, stable, session recall

### Phase 6 — Character Stage
- CharacterProcessor post-sum: Edge saturation (soft clip + asymmetry), Stereo width (mid/side), Tension macro
- Acceptance: No level jumps, width collapses to mono at 0

### Phase 7 — Instability Engine (The Hook)
- Two layers:
  A) Micro instability: per-voice seeded offsets at note start (pitch/phase/tilt)
  B) Event layer: EventDepth controls probability/intensity
- Event types (3-4): micro pitch bump, harmonic tilt shift, resonance spike, HF saturation burst
- Rules: No events in first 10ms, cooldown between events, envelope-aware
- Acceptance: Subtle at low depth, noticeable but stable at high depth, deterministic recall

### Phase 8 — UI + Presets
- Single-page UI: Osc, Filter, Env, Mod, Character sections
- Resizable editor
- Preset system: load/save user presets + 30 factory presets
- Acceptance: Controls attached correctly, presets recall, no crashes/dropouts

## Parameter Specification

### Global (5 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Master Volume | -60 dB to 0 dB | -6 dB |
| Voice Count | 1-32 | 16 |
| Glide Time | 0-500 ms | 0 |
| Mono Mode | Off/On | Off |
| Legato | Off/On | Off |

### Oscillator 1 (5 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Osc1 Waveform | Saw/Pulse/Triangle | Saw |
| Osc1 Octave | -2 to +2 | 0 |
| Osc1 Semitone | -12 to +12 | 0 |
| Osc1 Fine Tune | -50 to +50 cents | 0 |
| Osc1 Level | 0-1 | 0.8 |

### Oscillator 2 (7 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Osc2 Waveform | Saw/Pulse/Triangle | Saw |
| Osc2 Octave | -2 to +2 | 0 |
| Osc2 Semitone | -12 to +12 | 0 |
| Osc2 Fine Tune | -50 to +50 cents | 0 |
| Osc2 Detune | 0-20 cents | 5 |
| Osc2 Level | 0-1 | 0.6 |
| Osc Sync | Off/On | Off |

### Sub Oscillator (2 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Sub Level | 0-1 | 0.3 |
| Sub Wave | Sine/Square | Sine |

### Noise (2 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Noise Level | 0-1 | 0 |
| Noise Color | Dark to Bright | Mid |

### Mixer (2 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Osc Mix Balance | -1 to +1 | 0 |
| Drive (Pre Filter) | 0-1 | 0 |

### Filter (5 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Filter Type | LP24/LP12/HP12 | LP24 |
| Cutoff | 20 Hz to 20 kHz | 8 kHz |
| Resonance | 0-1 | 0.2 |
| Key Tracking | 0-100% | 50% |
| Velocity To Cutoff | 0-1 | 0.2 |

### Amp Envelope (4 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Attack | 0-5 s | 5 ms |
| Decay | 0-5 s | 300 ms |
| Sustain | 0-1 | 0.8 |
| Release | 0-10 s | 500 ms |

### Mod Envelope (5 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Mod Attack | 0-5 s | 10 ms |
| Mod Decay | 0-5 s | 300 ms |
| Mod Sustain | 0-1 | 0 |
| Mod Release | 0-10 s | 200 ms |
| Mod Env Amount | -1 to +1 | 0 |

### LFO 1 (4 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| LFO1 Wave | Sine/Triangle/Square/Random | Sine |
| LFO1 Rate | 0.1-20 Hz | 2 Hz |
| LFO1 Sync | Off/On | Off |
| LFO1 Amount | 0-1 | 0 |

### LFO 2 (4 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| LFO2 Wave | Sine/Triangle/Square/Random | Triangle |
| LFO2 Rate | 0.1-20 Hz | 5 Hz |
| LFO2 Sync | Off/On | Off |
| LFO2 Amount | 0-1 | 0 |

### Character (4 params)
| Parameter | Range | Default |
|-----------|-------|---------|
| Tension | 0-1 | 0.2 |
| Event Depth | 0-1 | 0 |
| Edge | 0-1 | 0.2 |
| Stereo Width | 0-2 | 1 |

### Instability (3 params, advanced)
| Parameter | Range | Default |
|-----------|-------|---------|
| Micro Drift | 0-1 | 0.2 |
| Event Probability | 0-1 | 0 |
| Event Intensity | 0-1 | 0.5 |

### Modulation Matrix (6 slots x source/dest/amount)
- Sources: LFO1, LFO2, ModEnv, Velocity, Aftertouch, ModWheel
- Destinations: OscPitch, PWM, FilterCutoff, Drive, StereoWidth, EventDepth

**Total: ~48-55 parameters**

## Architecture

### Signal Flow (per voice)
```
Osc1 + Osc2 + Sub + Noise → Voice Mixer → Drive → Filter → Character → Amp Envelope
```

### Key Design Rules
- UI never touches DSP directly — reads/writes parameters only
- No heap allocation in audio thread
- No mutex/locks in audio thread
- Per-block ParamSnapshot with cached parameter pointers
- Support sample rates 44.1k-192k
- State save/restore with version stamp
- Voice stealing: oldest voice
- Default 16 voices, max 32
- PolyBLEP oscillators
- SVF or Zero-Delay Feedback filter
- Parameter smoothing: cutoff, pitch, drive, modulation amounts (5-20ms)
- Never smooth envelopes

### File Structure
```
/Source
  PluginProcessor.h/.cpp
  PluginEditor.h/.cpp
  Params/
    ParamIDs.h
    ParameterLayout.h/.cpp
    ParameterState.h/.cpp
  DSP/
    SynthEngine.h/.cpp
    Voice.h/.cpp
    Oscillator.h/.cpp
    Envelope.h/.cpp
    Filter.h/.cpp
    Character.h/.cpp
    InstabilityEngine.h/.cpp
    ModMatrix.h/.cpp
    Utils/
      SmoothedValueBank.h/.cpp
      Random.h/.cpp
  UI/
    Components...
/Tests
  OfflineDSPTests.cpp
```

## MPC Compatibility Note
Plugin used in DAW, export multisampled patches for MPC Keygroup instruments.
Patches must remain stable when sampled — avoid heavy randomness.
