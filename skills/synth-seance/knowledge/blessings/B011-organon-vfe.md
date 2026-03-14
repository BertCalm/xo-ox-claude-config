# B011 — Organon's Variational Free Energy Metabolism

*Blessed: 2026-03-14 | Engine: Organon | Ghosts: All 8 (unanimous PASS)*

## The Blessed Feature

Organon implements Karl Friston's Variational Free Energy (VFE) principle as a synthesis engine — the instrument has a metabolic model that predicts incoming audio/MIDI and adjusts its synthesis parameters to minimize prediction error. The engine literally *learns* from what the player does, adapting its behavior over the course of a performance. This is a paradigm inversion: instead of the player programming the synth, the synth programs itself in response to the player.

## Why It Is Protected

The ghosts gave Organon an 8/8 unanimous PASS — the only engine to receive unanimous approval. Multiple ghosts noted this could be published as an academic paper. The VFE metabolism is not a gimmick; it is a genuine implementation of a neuroscience principle applied to audio synthesis, creating an instrument that is fundamentally different from every other synthesizer ever built.

## Prism Sweep Implementation (Round 6E + Round 11E)

**Full guide written**: `Docs/organon_vfe_guide.md` — Variational Free Energy metabolism deep-dive, Port-Hamiltonian modal array, prediction error minimization, and performance technique.

**Aftertouch → signalFlux → entropy cascade** (wired in Round 11): Aftertouch routes to `signalFlux` in the OrganonEngine. `signalFlux` feeds into `entropyAcceleration`, which accelerates the VFE metabolism's belief update rate. In practice: playing harder causes the instrument to learn faster. Light pressure = slow chemotroph metabolism. Hard pressure = the organism feeds, belief updates quicken, the Port-Hamiltonian array evolves rapidly. This is the most philosophically coherent aftertouch mapping in the fleet.

**Mod wheel → metabolicRate** (Round 11E): Mod wheel adds +3.0 Hz to metabolicRate at full throw. Combined with aftertouch (+0.25 signalFlux), a performer can push metabolicRate from 1.0 Hz to 6.5 Hz — building tension across a performance by accelerating the engine's own cognitive activity.

## Do Not

- Remove the VFE metabolism in favor of static parameter control
- Simplify the prediction model to reduce CPU usage (optimize the algorithm, don't remove it)
- Add a "disable metabolism" button that returns to conventional synthesis
- Reclassify Organon as an "effect" or "AI tool" rather than an engine
