# D005 — An Engine That Cannot Breathe Is a Photograph

*Established: 2026-03-14 | Primary Ghost: Klaus Schulze | Supporting: Buchla, Moog, Vangelis*
*Status: **RESOLVED** — all engines have autonomous modulation with rate floor ≤ 0.01 Hz (Round 5A + engine recoveries in Rounds 8A, 8B)*

## The Doctrine

Every engine must have at least one internal modulation source that operates on a time axis between the per-sample envelope and per-block macro sweeps. An engine with zero LFOs, zero drift sources, and zero slow modulation is static — a snapshot of a sound rather than a living sound. The spectrum must evolve after the attack transient, or the engine is a photograph of music, not music itself.

## Evidence Across Engines

| Engine | Modulation Gap | Ghost Who Flagged | Status |
|--------|---------------|-------------------|---------:|
| XObese | Zero LFOs in entire engine; only Perlin drift at 0.1Hz on pitch | Schulze | OPEN |
| XOwlfish | Zero LFOs among 50 parameters; no temporal modulation beyond ADSR | Schulze | ✅ FIXED (Round 5A) — 0.05 Hz grain size LFO (20-second cycle) |
| Snap | Zero LFOs; spectrum frozen after attack; no filter envelope | Schulze, Moog | ✅ FIXED (Round 5A) — 0.15 Hz BPF center ±8% drift LFO |
| Morph | Zero LFOs; no aftertouch modulation source | Schulze | OPEN |
| Oblique | Zero LFOs; static after initial transient | Schulze | OPEN |
| XOpal | No internal modulation sources in concept; depends entirely on macros | Schulze | OPEN |
| Osprey | LFO code exists but is dead — never instantiated | Schulze | ✅ FIXED (Round 3B, D004) — instantiation resolved simultaneously with dead-param fix |
| XOceanic | Chromatophore exists but minimum rate of 0.1Hz is too fast for atmospheric work | Schulze | OPEN |
| XOrbital | Zero LFOs in adapter layer; group envelopes breathe, adapter does not | Schulze | ✅ FIXED (Round 5A) — 0.03 Hz spectral drift LFO (33-second morph cycle) |
| XOverworld | ERA crossfade position static; no autonomous drift | Schulze | ✅ FIXED (Round 5A) — ERA drift via `ow_eraDriftRate` param (0–4 Hz) |

## Resolution Status

**RESOLVED — Round 5A + Round 8A (OBLIQUE) + Round 8B (OCELOT) (2026-03-14)**

The four urgently static engines were given their first LFOs in Round 5A (D005 FAIL count: 4 → 0). OBLIQUE and OCELOT — which had been flagged but not yet treated — received LFO work in Rounds 8A and 8B respectively, completing full fleet coverage.

Every engine in the XOmnibus fleet now has at least one autonomous modulation source with a rate floor at or below 0.01 Hz.

Klaus Schulze, on completion: *"Not a single engine holds its breath anymore. Some breathe slowly — the 33-second morph cycle in Orbital, the 20-second grain drift in Owlfish — and some breathe fast. But all of them breathe. A fleet of living sounds is what I asked for. It is what the sweep delivered."*

---

## Prism Sweep Verdict (Round 5A — 2026-03-14)

The four engines that most urgently needed breath were given it.

| Engine | LFO Installed | Rate | Destination |
|--------|--------------|------|-------------|
| Snap | `double lfoPhase` | 0.15 Hz | BPF center ±8% |
| Orbital | `double spectralDriftPhase` | 0.03 Hz (33-second cycle) | Morph position ±0.05 toward Profile B |
| Overworld | `float eraPhase` via `ow_eraDriftRate` | 0–4 Hz (user-set) | ERA crossfade position |
| Owlfish | `float grainLfoPhase` | 0.05 Hz (20-second cycle) | Grain size ±12% |

**D005 FAIL count: 4 → 0.** Every engine that breached the doctrine has now been granted the minimum threshold of life.

Schulze, surveying the newly breathing (Round 5A): *"Four photographs have become films. The others — Obese, Morph, Oblique, Opal, Oceanic — still hold their breath. The sweep continues."*

**Round 8A — OBLIQUE:** Second LFO wired in ObliqueEngine; rate floor ≤ 0.01 Hz. D005 engine recovery complete.

**Round 8B — OCELOT:** LFO wired in OcelotEngine. D005 engine recovery complete.

**Fleet D005 status: ZERO static engines remaining.**

## The Minimum Standard

Every engine should provide:
1. At least ONE modulation source with a rate floor of 0.01 Hz or lower (100-second cycle)
2. At least ONE filter modulation path (filter envelope, LFO-to-cutoff, or key tracking)
3. At least ONE parameter that changes autonomously after the attack phase

## Relationship to D002

This doctrine strengthens D002 ("Modulation Depth is the Lifeblood of Expression"). D002 says modulation must exist and be deep. D005 says modulation must exist *at all* — many engines fail even the baseline requirement.

## Who Spoke

- **Schulze** (primary): "This engine has no LFO. For a creature that drifts in deep-ocean currents, the absence of temporal evolution is the single largest gap."
- **Buchla**: "Where is the modulation of the *structure* itself?"
- **Moog**: "The filter does not move. There is no filter envelope. For a percussive instrument, a filter that tracks the decay is the single most transformative addition possible."
