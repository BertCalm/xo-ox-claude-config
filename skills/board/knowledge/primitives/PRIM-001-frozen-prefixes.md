---
id: PRIM-001
discovered: 2026-03-13
pillar: Brand Stewardship (D3)
severity: P0
---
# Parameter Prefixes Are Frozen Forever

Once a parameter prefix is established for an engine, it can never be renamed. The prefix is baked into every saved preset, every DAW session, every automation lane. Renaming breaks backward compatibility irreversibly.

## Evidence
- XOpossum uses `poss_` internally but the standalone uses plain snake_case IDs — the adapter layer maps between them
- Three different prefixes appeared in docs for Overworld (`era_`, `overworld_`, `ow_`) — only source code tells the truth
- `bite_` appeared in early docs but was never the real prefix — `poss_` was always correct

## Downstream Skills
- SKILL-001: How to add a new engine with correct prefix from day one
- SKILL-003: How to audit prefix consistency across docs and source
