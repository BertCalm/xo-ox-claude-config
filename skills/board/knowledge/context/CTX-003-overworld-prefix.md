---
id: CTX-003
scope: XOverworld, XOmnibus
discovered: 2026-03-13
status: resolved
---
# Overworld Triple-Prefix Confusion

Three different prefixes appeared in docs for Overworld:
- `era_` (in sound design guide and some docs)
- `overworld_` (in name migration reference)
- `ow_` (the ACTUAL prefix in source code)

Only `ow_` is correct. The others were wrong and have been fixed.

## Implications
- Always verify prefixes against source code, never trust docs alone
- The name migration reference now has a gotcha entry for this

## Related Primitives
- PRIM-001: Parameter prefixes are frozen forever
- PRIM-003: Derive from source, don't hardcode
