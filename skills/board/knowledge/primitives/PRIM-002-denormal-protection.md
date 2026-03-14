---
id: PRIM-002
discovered: 2026-03-13
pillar: Organizational Standards (D6)
severity: P1
---
# Denormal Protection Required in Every Feedback Accumulator

Any DSP state variable that accumulates via feedback (LP filters, delay feedback, reverb damping) can drift to denormal values with quiet input, causing CPU spikes. Protection must exist at the accumulator level, not just at the block level.

## Evidence
- Tide.h LP feedback accumulators (degradationLP_L/R) had no denormal protection — fixed 2026-03-13
- Abyss.h damping state accumulators had protection only at the output, not in the feedback loop — fixed 2026-03-13
- SVFilter.h already had correct protection (lines 51-52) — this was the exception, not the rule

## Downstream Skills
- SKILL-002: How to audit denormal protection across a codebase
