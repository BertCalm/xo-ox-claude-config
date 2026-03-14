# B012 — Osprey/Osteria ShoreSystem

*Blessed: 2026-03-14 | Engines: Osprey + Osteria | Ghosts: Buchla, Smith, Tomita*

## The Blessed Feature

The ShoreSystem is a shared 5-coastline cultural data model that both Osprey and Osteria read from simultaneously. Each coastline defines musical parameters (scales, rhythmic patterns, timbral profiles) inspired by real-world coastal cultures. When both engines are loaded, they share the same coastline state — if Osprey switches to the Mediterranean coast, Osteria responds with complementary Mediterranean parameters. This is the first shared cultural data layer between two XOmnibus engines.

## Why It Is Protected

No other synthesis platform has engines that share cultural/musical context at this level. The ShoreSystem is not just a preset bank — it is a relational data model where two engines maintain a shared understanding of "where they are" musically and culturally. This creates ensemble behavior from independent engines without explicit coupling. Smith called it "a masterwork of system design."

## Prism Sweep Implementation (Round 6F + Rounds 9F, 10J)

**ShoreSystem formally specified**: `Docs/shore_system_spec.md` — 5-coastline shared cultural coordinate system, relational data model, parameter mapping per coastline for both Osprey and Osteria.

**Osprey: 11 inaugural presets** across all 5 coastlines (Kelp Forest, Pacific Night Dive, Salt Mist, Tidal Friction, Open Water Dissolve, and 6 more). All presets include sonic DNA blocks. All 6 moods covered.

**Osteria: 10 inaugural presets** across all 5 coastlines (Mediterranean Dusk, Nordic Fjord Song, Shore Dialogue, Kora Metabolism, Last Table, and 5 more). All presets include sonic DNA blocks.

**Aftertouch wired for both engines** (Round 9F): Osprey aftertouch → shore resonance depth (+0–0.3 coastal texture). Osteria aftertouch → warmth filter depth (+0–0.3 body emphasis). The ShoreSystem now responds to continuous player gesture in both engines simultaneously — when both are loaded and sharing coastline state, performer pressure deepens both the texture and the warmth of the shared cultural moment.

## Do Not

- Remove the shared state between Osprey and Osteria
- Reduce to fewer than 5 coastlines
- Make the coastline data engine-private rather than shared
- Replace cultural data with generic parameter presets
