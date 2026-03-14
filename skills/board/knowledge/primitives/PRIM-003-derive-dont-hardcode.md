---
id: PRIM-003
discovered: 2026-03-13
pillar: Governance (D1)
severity: P1
---
# Derive Counts From Source — Never Hardcode in Prose

Numbers in documentation (engine count, preset count, line counts) go stale the moment new work happens. The prose says "24 planned" while the source has 21 built. Nobody remembers to update the prose.

## Evidence
- CLAUDE.md said "9 standalone instruments built; 24 engines planned" when 21 engines had real DSP code
- UI status bar said "9 Engines · 1000 Presets" when there were 21 engines and 1,610 presets
- Engine roadmap said "20 engines integrated" when Ocelot (3,010 lines) was already in Source/Engines/
- Preset count "1000" appeared in 8+ locations across docs, source, and specs

## Downstream Skills
- SKILL-004: How to audit hardcoded counts across a codebase
- Automation: grep for `\b[0-9]+ engine\b` and `\b[0-9,]+ preset\b` in all docs
