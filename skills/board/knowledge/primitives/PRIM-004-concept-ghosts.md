---
id: PRIM-004
discovered: 2026-03-13
pillar: Brand Stewardship (D3)
severity: P1
---
# Abandoned Concepts Leave Terminology Ghosts

When an engine's design pivots, the old concept's language persists across multiple files — docs, source comments, coupling descriptions, sound design guides. A single-file fix is never enough; ghosts haunt 4-8 files minimum.

## Evidence
- XOceanic pivoted from "swarm particle synthesis" (boid flocking) to "paraphonic string ensemble with chromatophore pedalboard"
- Stale swarm references found in: sound design guide, engine roadmap v3 (6 coupling descriptions), design spec, source code comments (Scatter.h "particles")
- The design spec was marked SUPERSEDED but still contained `ocean_` prefixed params throughout
- Fix required touching 5 files across 2 repos

## Downstream Skills
- SKILL-003: How to purge stale concept language after a design pivot
- Pattern: always grep for the old concept's key terms across ALL repos after a pivot
