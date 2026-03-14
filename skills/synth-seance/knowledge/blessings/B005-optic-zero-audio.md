# B005 — Optic's Zero-Audio Identity

*Blessed: 2026-03-14 | Engine: Optic | Ghost: Klaus Schulze, Don Buchla*

## The Blessed Feature

Optic generates no audio. It is a pure control-signal engine — a Comb Jelly of the XOmnibus water column, producing only modulation, coupling voltages, and visual data streams that reshape every engine it touches.

## Why It Is Protected

This is the most revolutionary concept in the XOmnibus gallery. Optic redefines what a "synth engine" can be. Adding fallback audio would destroy the paradigm — the statement that sound can be shaped by instruments that never themselves make a sound. The silence IS the identity.

## Do Not

- Add "fallback audio" for when Optic is loaded solo
- Add an oscillator "for testing purposes"
- Reclassify Optic as an "effect" rather than an "engine"
- Remove it from the gallery because it "doesn't make sound"

## Prism Sweep Implementation (Round 10B)

**Full guide written**: `Docs/optic_synthesis_guide.md` (~33k) — AutoPulse system, zero-audio identity philosophy, visual modulation taxonomy, all coupling output types documented.

**5-step onboarding path designed**: The guide includes a structured first-session path for new users encountering Optic in isolation. The path moves from "why is there no sound?" through AutoPulse → coupling → performance, without ever adding fallback audio. The onboarding path is the answer to DB002 that does not compromise the paradigm.

**D006 formally exempt**: Optic is the one engine in the fleet where D006 does not apply. It has no note-on, no velocity, no aftertouch, and no mod wheel — the `MidiBuffer` parameter in `processBlock()` is intentionally commented out. This is not a D006 violation; it is the engine's identity.

## Note

See Debate DB002 for the tension between this paradigm and accessibility. The blessing protects the zero-audio identity; the debate addresses how to onboard users without compromising it. The synthesis guide's 5-step onboarding path is the current best answer to DB002.
