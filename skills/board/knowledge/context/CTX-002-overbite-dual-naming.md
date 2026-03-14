---
id: CTX-002
scope: XOppossum, XOmnibus
discovered: 2026-03-13
status: active
---
# XOpossum / XOverbite Dual Naming

The standalone bass synth has a naming split:
- **Standalone repo**: `~/Documents/GitHub/XOppossum/` (note double 'p')
- **Standalone param IDs**: Plain snake_case (`filter_cutoff`, `osc_blend`, `macro_bite`)
- **XOmnibus canonical name**: OVERBITE (not BITE — BITE is legacy)
- **XOmnibus param prefix**: `poss_` (the adapter adds this)
- **Accent color**: Fang White `#F0EDE8` (not Moss Green — that was legacy)

## Implications
- Never rename standalone params to add `poss_` prefix — the adapter handles this
- When writing docs, use OVERBITE (canonical), not BITE (legacy)
- The integration spec has a dual-column parameter table mapping XOmnibus IDs to standalone IDs

## Related Primitives
- PRIM-001: Parameter prefixes are frozen forever
