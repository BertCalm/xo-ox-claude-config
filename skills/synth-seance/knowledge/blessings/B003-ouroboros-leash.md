# B003 — Ouroboros's Leash Mechanism

*Blessed: 2026-03-14 | Engine: Ouroboros | Ghost: Don Buchla, Bob Moog*

## The Blessed Feature

The Leash mechanism tames chaotic attractors (Lorenz, Rossler, Chua, Aizawa) by constraining their trajectories to musically useful ranges without destroying the mathematical properties that make them sound interesting. It is a genuine control-theory solution — not a limiter, not a clipper, but a boundary that the chaos pushes against and bounces off of.

## Why It Is Protected

Without the Leash, chaos synthesis is unusable — trajectories diverge to infinity or collapse to fixed points. With a naive limiter, the mathematical beauty of the attractors is destroyed. The Leash preserves the phase-space topology while keeping the output in a musically useful range. This is the hardest engineering problem in the engine, and it's solved correctly.

## Prism Sweep Implementation (Round 10C + Round 11E)

**Full guide written**: `Docs/ouroboros_guide.md` (~30k) — Leash mechanism deep-dive, self-oscillation regions, velocity coupling output topology, all four attractor topologies.

**Aftertouch creates CC counterpoint** (Round 11E): The Leash now has a two-controller expression axis. Aftertouch subtracts −0.3 from leash (loosens the attractor — more chaos, less pitch tracking). Mod wheel adds +0.4 to leash (tightens it — more pitch tracking, less chaos). The performer can sculpt chaos vs. order in real time with both hands.

**10 inaugural presets** written in Round 11, covering all four attractor topologies (Lorenz, Rossler, Chua, Aizawa). The `Ouro_Aizawa_Mobile.xometa` preset is specifically cited in B007 documentation as the canonical demonstration of velocity coupling outputs feeding cross-engine modulation.

## Do Not

- Replace Leash with hard clipping or soft limiting
- Remove the empirically-derived bounding boxes (they took real computation to find)
- "Simplify" the attractor equations (the specific publications — Lorenz 1963, Rossler 1976, Chua 1983, Aizawa 1982 — are canonical for a reason)
