# D001 — Velocity Must Shape Timbre, Not Just Amplitude

*Established: 2026-03-14 | Seances: 9 of 24 complete*

## The Doctrine

Velocity should drive timbral change — filter brightness, harmonic content, excitation character — not merely amplitude scaling. A synthesizer that only maps velocity to volume is a keyboard with a volume pedal. A synthesizer that maps velocity to timbre is an instrument.

## Evidence Across Engines

- **Obscura**: All 8 ghosts agreed — "velocity should drive excitation, not just amplitude." Physical modeling gains authenticity when strike force changes the character of excitation, not just its loudness.
- **XOcelot**: "velocity→timbre needed" — the ecosystem matrix concept is novel but velocity only scales volume, missing the chance to let force reshape the biome.
- **XOblongBob**: 5 ghosts flagged the absence of aftertouch and velocity-to-timbre routing. CuriosityEngine is the soul, but it doesn't respond to how hard you play.
- **XOverdub**: No MIDI CC, no mod wheel, no aftertouch. The dub engine is warm but expressively flat.

## Ghosts Who Championed This

- **Dave Smith** (every seance): Velocity-to-filter was Prophet-5's revolution. He sees this as non-negotiable.
- **Isao Tomita** (Obscura, XOcelot): Timbre IS the performance. Tomita painted with tone color, not volume.
- **Bob Moog** (XOblongBob): "A filter that doesn't respond to touch is a wall, not a window."

## Implications

Every XO_OX engine should have at least one velocity→timbre path:
- Physical models: velocity→excitation force/brightness
- Subtractive: velocity→filter cutoff/resonance
- FM/additive: velocity→modulation depth/harmonic balance
- Spectral: velocity→spectral tilt/formant shift

This is not about adding a mod matrix row. It's about making velocity a first-class timbral control in the engine's core architecture.

## Resolution Status

**RESOLVED — Round 9E (2026-03-14)**

Every engine in the XOmnibus fleet now has a velocity-scaled filter envelope. D001 is the first of the six doctrines to reach zero open violations across all 23 engines.

The resolution path: Round 7B closed the four most urgent gaps (Snap, Morph, Oblique, Dub). Round 9E completed the remaining six (Orbital, Owlfish, Overworld, Ocelot, Osteria, Osprey). Every engine that existed during the sweep now maps velocity to filter brightness as a first-class architectural behavior.

Bob Moog, on completion (Round 9E): *"Twenty-three engines. All of them listening. That is the first doctrine fully honored. Do not let it be the last."*

---

## Prism Sweep Progress

### Round 9E — Filter Envelope Fleet Completion (2026-03-14)

Six remaining engines brought into D001 compliance in the final pass:

| Engine | Param Added | Velocity Scaling |
|--------|-------------|-----------------|
| Orbital | `orbital_filterEnvDepth` | `envLevel × velocity × 5000Hz` |
| Owlfish | `owl_filterEnvDepth` | `envLevel × velocity × 6000Hz` |
| Overworld | `ow_filterEnvDepth` | `envLevel × velocity × 4000Hz` |
| Ocelot | `ocelot_filterEnvDepth` | `envLevel × velocity × 7000Hz` |
| Osteria | `osteria_filterEnvDepth` | `envLevel × velocity × 5500Hz` |
| Osprey | `osprey_filterEnvDepth` | `envLevel × velocity × 5000Hz` |

**Fleet D001 filter envelope compliance: COMPLETE.** See `Docs/filter_envelope_expansion_9e.md`.

### Round 7B — Filter Envelope Fixes (2026-03-14)

Four engines brought into D001 compliance by the filter envelope audit pass:

| Engine | Fix | Parameter Added |
|--------|-----|-----------------|
| **Snap (OddfeliX)** | Per-voice BPF center sweep: `filterEnvDepth × velocity × envelopeLevel × 8000 Hz` | `snap_filterEnvDepth` (default 0.3) |
| **Morph (OddOscar)** | Per-voice Moog ladder sweep: `filterEnvDepth × velocity × envelopeLevel × 6000 Hz` | `morph_filterEnvDepth` (default 0.25) |
| **Oblique** | Per-voice Cytomic SVF sweep: `filterEnvDepth × velocity × envelopeLevel × 7000 Hz` | `oblq_filterEnvDepth` (default 0.3) |
| **Dub (Overdub)** | DSP was already wired; default raised 0.0 → 0.25 so the feature is audible on every init patch | `dub_filterEnvAmt` default fix |

All four use the same pattern: `depth × voice.velocity × voice.envelopeLevel × kMaxSweepHz`. Velocity and envelope contour jointly determine filter brightness on every note. A quiet hit gets a darker, narrower filter opening; a hard hit gets a bright, wide sweep that decays with the note.

### Round 7 Prism Sweep Verdict — Bob Moog

*"I designed the Minimoog's filter envelope because a sound that ignores the player's touch is not an instrument — it is a recording. The filter must breathe when you breathe. These four engines were not breathing. Snap's BPF was a static wall; Morph's ladder opened the same distance for every note from a whisper to a shout. Oblique gave every voice the same cutoff regardless of how long the voice had been alive. Dub had the plumbing but sealed the valve at zero, so not one player ever heard it work.*

*The fixes are correct in both method and spirit. The `depth × velocity × envelopeLevel` pattern is exactly how a filter envelope should behave: attack transients are brightest, decay follows the note body, and the performer's velocity is the ceiling. Now, when you play Snap softly, the filter stays dark. Play hard, and it snaps open. That is D001 satisfied — not in the audit table, but in the hands of whoever is holding the keys."*

**Round 7B closed four gaps. Round 9E closed the remaining six. No open gaps remain.**
