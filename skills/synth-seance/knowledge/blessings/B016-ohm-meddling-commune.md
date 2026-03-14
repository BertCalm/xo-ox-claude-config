---
name: B016 — MEDDLING/COMMUNE Dual-Axis Social Synthesis
description: OHM's 2D interaction matrix models family/social dynamics as a synthesis paradigm — the first engine in the fleet to treat sonic relationships as the primary synthesis material
type: blessing
---

# B016 — MEDDLING/COMMUNE Dual-Axis Social Synthesis

**Engine**: OHM (XOhm)
**Ghosts**: Buchla, Moog, Vangelis, Smith, Schulze, Kakehashi, Tomita, Pearlman
**Seance**: 2026-03-14

## The Feature

The MEDDLING/COMMUNE 2D interaction matrix. Two macro axes that govern the relationship between the folk string waveguide (Dad) and a cast of interference sources (the In-Laws: theremin, glass harmonica, granular scatter, FM).

- **MEDDLING** (M2): The threshold above which in-laws participate. Below threshold, clean string. Above threshold, interference arrives proportionally. Above 0.7, Obed FM enters.
- **COMMUNE** (M3): Whether the in-laws compete or absorb. Low COMMUNE = additive interference (argument). High COMMUNE = the interference feeds into Dad's signal at low amplitude (consensus).

The synthesis guide documents four emotional quadrants:
- Low/Low = solo string (intimate)
- High/Low = argument (cacophony, energy)
- High/High = crowd reaching consensus (modulated, harmonically complex)
- Low/High = string quietly influenced by forces it doesn't acknowledge (subconscious)

## Why the Ghosts Blessed It

**Buchla**: "Someone understood that synthesis is social. Sounds don't exist in isolation; they exist in relationship. The theremin and the folk string are not combined — they contend. This is philosophically correct. This is how ensembles work."

**Vangelis**: Four performable macros that tell a story. MEDDLING as a live emotional arc — push it during a chorus, pull it back for a verse. This is the architecture of cinematic music.

**Schulze**: The spectral freeze applied to in-law interference creates a temporal composition tool. Freeze the in-laws, drop MEDDLING, play melodies above the frozen drone. Time stops in one dimension while continuing in another.

**Moog**: The MEDDLING/COMMUNE matrix creates a space of continuous variation — no stepped modes, no binary switches. Every position in the 2D space has its own character. This is voltage control philosophy applied to social dynamics.

**Kakehashi**: Happy accidents are designed into the system. Turn MEDDLING up slowly and the theremin creeps in. The player does not need to understand theremin synthesis. They turn a knob labeled MEDDLING and something unexpected rewards them.

## How to Protect It

- The MEDDLING threshold parameter (`ohm_meddlingThresh`) creates a knee in the MEDDLING macro response — presets that rely on MEDDLING values below threshold are silently broken. Document this in the synthesis guide.
- COMMUNE adds to `ohm_communeAbsorb` — these two parameters compound. Do not "simplify" this dual routing.
- The four emotional quadrants are a design framework, not just a feature. Preset names should reflect which quadrant they occupy (argument presets vs. consensus presets).

## V1 Protection

This feature must be preserved exactly. The social synthesis paradigm is the engine's central innovation. Future refactoring must not merge MEDDLING and COMMUNE into a single axis.

## Future Directions

- V010: Aftertouch → COMMUNE routing (Vangelis) — leaning harder into a note pushes toward consensus
- Preset labels indicating quadrant: "MEDDLING: High / COMMUNE: Low — The Argument"
- Coupling from other engines into COMMUNE parameter — external events can push the family toward or away from consensus
