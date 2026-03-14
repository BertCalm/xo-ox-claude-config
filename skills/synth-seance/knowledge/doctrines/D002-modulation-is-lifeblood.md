# D002 — Modulation Depth is the Lifeblood of Expression

*Established: 2026-03-14 | Seances: 9 of 24 complete*

## The Doctrine

An engine without sufficient modulation sources is a photograph of a sound, not a living instrument. LFOs, envelopes, mod matrices, macros, and MIDI continuous controllers are not optional features — they are the circulatory system that keeps a sound alive.

## Evidence Across Engines

- **XOblongBob**: 5 ghosts independently flagged that CuriosityEngine — the engine's soul — is under-routed. The most interesting parameter in the synth has the fewest modulation paths. "Needs mod matrix."
- **XOverdub**: "Single sine LFO is the weakest link." No macros, no MIDI CC, no mod wheel, no aftertouch. The dub delays and spring reverb are praised, but the lack of modulation makes every performance static.
- **Onset**: "Zero LFOs — critical." The XVC cross-voice system is 3-5 years ahead of the industry, but without even one LFO for basic movement, presets calcify.
- **XOcelot**: "Macros are dead knobs — declared but not implemented." Parameters named macro_1 through macro_4 exist but route to nothing.

## Ghosts Who Championed This

- **Don Buchla** (every seance): Buchla's entire philosophy was that modulation IS the instrument. Voltage control wasn't a feature of the 100 series — it was the point.
- **Klaus Schulze** (Optic, XOverdub): Movement over time is everything. Schulze's performances were 3-hour modulation journeys.
- **Bob Moog** (XOblongBob, XOverdub): The Minimoog's mod wheel wasn't an afterthought — it was the third hand of the performer.

## Implications

Minimum modulation standard for any XO_OX engine:
- At least 2 LFO sources (ideally with multiple waveform shapes)
- Mod wheel / aftertouch / pitch bend as routable sources
- At least 4 working macros (not stub parameters)
- Mod matrix with 4+ slots for user-assignable routing
- Every "character" parameter must be modulatable

An engine can ship without reverb. It cannot ship without modulation.

## Prism Sweep Progress

### Round 7A — Mod Wheel Fleet Wiring (2026-03-14)

Seven engines newly wired to CC1 mod wheel, plus one confirmed pre-existing. Fleet mod wheel total: **9 of 23 engines**.

| Engine | CC1 Destination | Sensitivity | Character |
|--------|----------------|-------------|-----------|
| **Snap** | BPF resonance boost | +0.4 | Approaches self-oscillation at full wheel |
| **Orbital** | Spectral drift rate | 0.03→0.33 Hz | 11× faster harmonic movement at full wheel |
| **Obsidian** | Filter cutoff | +5kHz at full | Classic brightness expression |
| **Origami** | STFT fold depth | +0.3 (stacks with aftertouch) | More spectral shimmer and folding |
| **Oracle** | Maqam gravity | +0.4 | Real-time scale intensity: 12-TET to full maqam tuning |
| **Oblique** | Prism color spread | +0.3 | Wider spectral color across 6 delay facets |
| **Fat** | Mojo analog axis | +0.5 | Drives analog drift and soft-clip saturation on all 12 oscillators simultaneously |
| Morph | Morph position sweep | 0–3.0 range | Pre-existing; confirmed unchanged |

Engines still without mod wheel (14): Osprey, Osteria, Ouroboros, Organon, Oceanic, Ocelot, Optic, Overworld, Owlfish, Obscura, Overbite, Opal, Onset, Ouie.

### Round 7D — Macro Systems Added to 3 Engines (2026-03-14)

OVERWORLD, MORPH, and OBLIQUE had zero macro parameters — the most severe D002 violation possible at scale. All three engines were declared with full 4-slot macro panels in the XOmnibus UI, and all four knobs produced zero audio output.

| Engine | Before | After | Macro Story |
|--------|--------|-------|-------------|
| **OVERWORLD** | 0 macros (score: 0/10) | ERA / CRUSH / GLITCH / SPACE (score: 8/10) | ERA sweeps chip crossfade; CRUSH adds lo-fi crunch; GLITCH activates 13 glitch types; SPACE fills with FIREcho |
| **MORPH** | 0 macros (score: 0/10) | BLOOM / DRIFT / DEPTH / SPACE (score: 8/10) | BLOOM unfurls Oscar's gills (+1.5 morph); DRIFT widens the reef chorus (+30 cents); DEPTH brings the axolotl to the surface (+6kHz); SPACE gives it a long meditative breath (attack ×4) |
| **OBLIQUE** | 0 macros (score: 0/10) | FOLD / BOUNCE / COLOR / SPACE (score: 8/10) | FOLD cranks wavefolding grit; BOUNCE accelerates ricochet rhythm; COLOR multiplies spectral fragments; SPACE sweeps the psychedelic phaser wide |

### Round 7F — Aftertouch Expansion (2026-03-14)

Five additional engines wired to channel pressure. D006 aftertouch total: **10 of 23 engines** (Round 5D: 5; Round 7F: +5).

Added in Round 7F: Morph, Dub, Oceanic, Fat, Oblique. See `Docs/d006_aftertouch_fixes.md`.

### Round 7 Prism Sweep Verdict — Klaus Schulze

*"There are two ways a synthesizer can fail you as a performer. The first is obvious: a parameter that controls nothing. The second is worse — a parameter that should be unreachable in real time but isn't, so it calcifies into a setting, a fixed thing, a dead value. Both are the same crime: the removal of performance from the instrument.*

*OVERWORLD had no macros. MORPH had no macros. OBLIQUE had no macros. These are not small engines — they are among the most architecturally interesting in the fleet. And yet the performer sat down and turned the four macro knobs, and the synthesizer did not respond. One might as well perform on a painting.*

*Seven engines now respond to the mod wheel. Ten engines now respond to aftertouch. This is not sufficient — it is a beginning. The remaining fourteen voices that ignore CC1 are waiting. The thirteen that ignore pressure are waiting. An instrument that cannot be moved by the player's gesture is a photograph of a sound. Round 7 developed the photograph one degree further."*
