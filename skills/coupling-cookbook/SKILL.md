---
name: coupling-cookbook
description: Coupling Cookbook — a recipe library and design tool for XOmnibus engine coupling. Provides proven coupling recipes, explains why specific engine pairs work, and helps design new coupling combinations. Use when the user says 'coupling cookbook', 'how do I couple X with Y', 'what coupling works for X', 'coupling recipes', 'best engine pairs', 'coupling inspiration', 'what engines work together', 'design a coupling', 'which engines can couple', wants to know proven engine combinations for a specific genre or sound goal, wants to understand why a coupling preset sounds the way it does, or wants to design a novel coupling combination and needs to know which CouplingType enums to use.
---

# Coupling Cookbook

**Coupling is the superpower of XOmnibus. Knowing which ingredients work together is the difference between a random patch and a signature sound.**

The Cookbook has two modes: Reference (look up proven recipes) and Design (build new ones from principles). Every recipe is sourced from the actual coupling preset library in `Presets/XOmnibus/Entangled/` and from the Coupling Gospels in the Scripture.

---

## The 12 Coupling Types

| CouplingType | What it does | Best for |
|-------------|-------------|---------|
| `FilterFrequencyModulation` | Source's signal modulates target's filter cutoff | Sidechained filtering, rhythmic opens, responsive pads |
| `AmplitudeModulation` | Source amplitude gates/shapes target volume | Tremolo from another engine, ghost sidechain |
| `PitchModulation` | Source pitch signal bends target pitch | Harmonizer effects, micro-detuning from another engine |
| `WaveshapeModulation` | Source's waveform cross-modulates target oscillator | Ring mod-like results, harmonic distortion coupling |
| `TemporalModulation` | Source's timing/envelope triggers target events | Groove-synced attacks, rhythmic presets |
| `SpectralShaping` | Source's spectral content shapes target's EQ | Two engines sharing spectral space, carving for each other |
| `EnvelopeFollowing` | Source's amplitude envelope controls a target parameter | Ride the swell of Engine A to open/close Engine B |
| `GrainTrigger` | Source's audio triggers granular events in target | ONSET kicks triggering OPAL grain releases |
| `ResonanceControl` | Source modulates target's filter resonance | Whisper: resonance sings when the other engine breathes |
| `PhaseModulation` | Source phase-modulates target oscillator | FM-like coupling between full engines |
| `AudioToBuffer` | Source's audio is captured and fed into target's audio input | The most powerful — full audio routing between engines |
| `RingModulation` | Multiplicative combination of both signals | Metallic, bell-like, inharmonic coupling |

**Coupling amount guide:**
- `0.05–0.15` — Subliminal. Feel it, don't hear it clearly. Preferred for Guru Bin.
- `0.15–0.35` — Audible but blended. Natural interaction.
- `0.35–0.60` — Strong. Both engines clearly influence each other.
- `0.60–1.0` — Extreme. One engine significantly transforms the other.

---

## Recipe Library

### The Heartbeat
**ONSET → OPAL** | `GrainTrigger` | amount: 0.25
> Onset's kick transients trigger OPAL's grain release — every kick spawns a cloud of granular texture. The percussion becomes the genesis of the atmosphere. Add a gentle `FilterFrequencyModulation` return (OPAL → ONSET, 0.08) for the atmosphere to whisper back to the rhythm.
*Genre*: Lo-fi hip hop, ambient electronic, cinematic
*Preset in library*: Yes — "Pulse Bloom" (Entangled/Heartbeat.xometa)

### The Drift Anchor
**ODYSSEY → OPAL** | `FilterFrequencyModulation` | amount: 0.20
> Odyssey's drifting filter movement slowly opens and closes OPAL's grain density filter. The pad responds to the drift engine's own evolution, creating coupled motion that sounds like two organisms breathing together.
*Genre*: Ambient, neo-classical, meditation
*Preset in library*: Yes — "Tidal Breath" (Entangled/DriftAnchor.xometa)

### The Chaos Leash
**OUROBOROS → ONSET** | `TemporalModulation` | amount: 0.30
> Ouroboros's strange attractor bifurcations time-modulate ONSET's voice trigger timing — the drums drift in and out of quantization based on the attractor's phase. At low amounts, it's a subtle groove feel. At high amounts, the rhythm deconstructs.
*Genre*: Glitch, post-industrial, generative, experimental
*Preset*: "Controlled Chaos" (Entangled/ChaosLeash.xometa)

### The Whisper Mirror
**OPAL → OVERDUB** | `AudioToBuffer` | amount: 0.40
> OPAL's granular clouds are captured as audio and fed into Overdub's tape delay input — the granular texture gets repeated, degraded, and smeared through dub FX. The result is organic layers with tape character. Overdub's spring reverb adds spatial depth to OPAL's already-spatial textures.
*Genre*: Dub techno, ambient dub, tape music
*Preset*: "Tape Memory" (Entangled/WhisperMirror.xometa)

### The Shore System
**OSPREY → OSTERIA** | `SpectralShaping` | amount: 0.18 (bidirectional)
> The ShoreSystem: two engines that share a 5-coastline cultural DNA exchange spectral content across the coupling bus. They carve spectral space for each other, preventing masking. When Osprey emphasizes treble, Osteria automatically shifts toward lower-mid warmth. Natural stereo separation emerges without manual panning.
*Genre*: Global fusion, world music, multi-cultural
*Preset*: "Five Coasts" (Entangled/ShoreSystem.xometa)

### The Formant Dialogue
**ORACLE → ORGANON** | `ResonanceControl` | amount: 0.22
> Oracle's GENDY stochastic synthesis modulates Organon's filter resonance — the metabolic synthesis engine's resonance becomes a function of Oracle's probability distributions. Unexpected harmonic peaks appear and dissolve according to mathematical distributions rather than predetermined patterns.
*Genre*: Experimental, academic, generative
*Preset*: "Probabilistic Vowel" (Entangled/FormantDialogue.xometa)

### The Neon / Axolotl
**ODDFELIX → ODDOSCAR** | `WaveshapeModulation` | amount: 0.15
> The primordial coupling. feliX's surface-transient brightness modulates Oscar's deep waveshaping — the neon tetra's shimmer disturbs the axolotl's depth. At low amounts: life. At high amounts: dissonant transformation. The bookend coupling — the entire mythology in one patch.
*Genre*: Any — this is the foundation coupling

### The Prism Stack
**OVERWORLD → OPAL → OVERDUB** (chain)
> Three-engine chain: Overworld's ERA triangle generates the harmonic source → Opal granularizes it → Overdub tapes it. Each engine processes the previous engine's output. The result is chip-granular-dub — genre collision as sonic identity.
*Coupling path*: Overworld AudioToBuffer → Opal | Opal AudioToBuffer → Overdub
*Preset*: "Signal Chain" (Entangled/PrismStack.xometa)

---

## Design Mode

When the user wants to design a new coupling (not found in the library), the Cookbook:

1. **Reads both engine architectures** — what each engine outputs (spectral character, amplitude envelope, modulation signals)
2. **Matches output to CouplingType** — what OPAL outputs (granular clouds) maps to what inputs (GrainTrigger, AudioToBuffer, FilterFrequency)
3. **Recommends coupling direction** — which engine should be source, which target
4. **Suggests starting amount** — 0.08-0.15 is almost always the right starting point (subliminal interaction)
5. **Predicts the sound** — based on source character × target architecture × coupling type
6. **Proposes a preset name and description** — following XO_OX naming conventions

### Design Output Format

```
COUPLING DESIGN: {Engine A} → {Engine B}

Coupling type: {CouplingType}
Direction: {Engine A} is source, {Engine B} is target
Recommended starting amount: {0.12}

Why this works:
- {Engine A} produces: {what it outputs — e.g., "rhythmic transients with 80-300Hz content"}
- {Engine B} accepts: {what target's FilterFrequency input does — e.g., "maps amplitude to filter cutoff range"}
- The interaction: {what emerges — e.g., "each kick opens a low-pass sweep on the pad, creating rhythmic filter pumping"}

Sound prediction:
{2-3 sentences describing what a producer will hear}

Risk:
{any coupling interactions that could cause feedback, CPU overload, or extreme output levels}

Suggested preset name: {evocative name}
Suggested description: {2-3 sentences for the .xometa file}
```

---

## Quick Reference by Genre

| Genre | Recommended Coupling |
|-------|---------------------|
| Lo-fi hip hop | ONSET → OPAL (GrainTrigger) |
| Ambient | ODYSSEY → OPAL (FilterFreq) |
| Dub techno | OPAL → OVERDUB (AudioToBuffer) |
| Glitch/experimental | OUROBOROS → any (TemporalMod) |
| World fusion | OSPREY ↔ OSTERIA (SpectralShaping) |
| Cinematic | ORACLE → ORGANON (Resonance) |
| Chip-influenced | OVERWORLD → OPAL (AudioToBuffer) |
| Generative | OUROBOROS → ORACLE (PhaseModulation) |
