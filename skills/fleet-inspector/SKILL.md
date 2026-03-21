---
name: fleet-inspector
description: Fleet Inspector — comprehensive cross-engine health dashboard for the entire XOmnibus fleet. Scans every engine's source, presets, documentation, and build status in parallel and produces a single unified health report. Use when the user says 'fleet inspector', 'inspect the fleet', 'fleet health', 'engine status', 'what state is the fleet in', 'check all engines', 'fleet audit', 'which engines are weakest', 'what needs work across the fleet', 'give me the big picture', wants to know the state of all engines before planning work, wants to prioritize which engine to retreat on next, wants to see how engines compare on any dimension (presets, params, doctrine compliance), or is preparing a sprint plan and needs to know where the gaps are. Also invoke when MEMORY.md or CLAUDE.md engine counts seem inconsistent and a ground-truth count is needed.
---

# Fleet Inspector

**The dashboard that sees all 50 engines at once.**

The XOmnibus fleet is large enough that no one holds its full state in their head. The Fleet Inspector dispatches parallel agents to read every engine's source, presets, and documentation simultaneously, then synthesizes a single health report that shows exactly where the fleet stands — and where it needs work.

---

## What the Inspector Checks

For each engine in the fleet, the Inspector gathers:

### Source Health
- Engine source file exists and compiles (from `Source/Engines/{Name}/{Name}Engine.h`)
- Line count (proxy for DSP complexity)
- Parameter count (extracted from APVTS registration)
- Key DSP stages (oscillator count, filter type, modulation sources)
- Parameter prefix is consistent with CLAUDE.md spec

### Preset Health
- Total preset count (engine-specific folder + XOmnibus fleet)
- Mood distribution: Foundation/Atmosphere/Entangled/Prism/Flux/Aether counts
- DNA coverage: which DNA extremes (above 0.8 or below 0.2 on each axis) are missing
- Zero-duplicate confirmed: any duplicate names detected
- Init patch: does a Foundation init preset exist?

### Documentation Health
- CLAUDE.md entry exists (parameter prefix table row)
- Sound design guide section exists in `Docs/xomnibus_sound_design_guides.md`
- Engine has a row in the seance cross-reference (`Docs/seance_cross_reference.md`)
- Identity card exists in the aquatic mythology docs
- Blessing documented (if any)

### Doctrine Compliance
- D001: velocity shapes timbre (any velocity-to-filter wiring in source?)
- D002: modulation present (LFO count ≥ 2, macro count = 4)
- D003: param IDs frozen on ship (no ID changes in shipped engines — check against last-known-good state)
- D004: no dead parameters (from historical seance/sweep findings)
- D005: breathing LFO (rate floor ≤ 0.01 Hz confirmed?)
- D006: aftertouch + mod wheel wired (from fleet tracking in CLAUDE.md)

### Retreat Status
- Retreat chapter exists in `scripture/retreats/`
- Last retreat date (from cadence log)
- Awakening preset count (from retreat chapter, if exists)

---

## The Fleet Report

```
══════════════════════════════════════════════════════════════════
  FLEET INSPECTOR — {date}
  {N} engines scanned
══════════════════════════════════════════════════════════════════

## FLEET OVERVIEW

Presets:      {total} across {N} engines (avg {N}/engine)
Params:       {total} tracked parameters (avg {N}/engine)
Doctrines:    D001 ✅  D002 ✅  D003 ✅  D004 ✅  D005 ✅  D006 ✅
Retreats:     {N}/{total} engines have retreat chapters
Build:        {N}/{total} engines confirmed building

## PER-ENGINE TABLE

| Engine   | Presets | Moods | D006 | Retreat | Doc | Health |
|----------|---------|-------|------|---------|-----|--------|
| OddfeliX |  67     | 6/6   | ✅   | ✅      | ✅  | 🟢 OK  |
| Overdub  |  38     | 5/6   | ✅   | ✅      | ✅  | 🟡 GAP |
| Oracle   |  44     | 6/6   | ✅   | ❌      | ✅  | 🟡 GAP |
| Obscura  |  12     | 3/6   | ✅   | ❌      | ❌  | 🔴 LOW |
...

Legend: 🟢 OK (≥40 presets, 6 moods, all doctrines, retreat done)
        🟡 GAP (minor gaps — <40 presets, missing 1-2 moods, no retreat)
        🔴 LOW (serious gaps — <15 presets, missing 3+ moods, no doc)

## TOP GAPS

### Preset Gaps (engines most under-stocked):
1. {Engine} — {N} presets, missing: Aether, Flux
2. {Engine} — {N} presets, missing: Entangled
3. {Engine} — {N} presets, only {N} presets total

### Documentation Gaps:
1. {Engine} — no sound design guide section
2. {Engine} — no identity card
3. {Engine} — missing seance cross-reference entry

### Retreat Gaps (never been retreated):
{list of engines with no retreat chapter}

### Doctrine Gaps:
{list any remaining D001/D002/D003/D004/D005/D006 failures}

## RECOMMENDED PRIORITIES

Based on health scores, the Inspector recommends:

1. {Engine} — for Retreat Accelerator (no retreat + lowest preset count + D0X gap)
2. {Engine} — for Exo Meta preset expansion (missing {N} moods)
3. {Engine} — for Historical Society doc pass (no guide, no identity card)

══════════════════════════════════════════════════════════════════
```

---

## Filtered Views

### By health status
```
/fleet-inspector --filter red
```
Shows only 🔴 LOW engines with full detail on their gaps.

### By dimension
```
/fleet-inspector --focus presets
/fleet-inspector --focus doctrine
/fleet-inspector --focus retreats
/fleet-inspector --focus docs
```
Produces a focused report on just that dimension across all engines.

### Single engine detail
```
/fleet-inspector --engine Opal
```
Runs the full inspection on one engine and returns exhaustive detail: every preset listed by mood, every doc status, doctrine check with evidence from source code.

### Comparison mode
```
/fleet-inspector --compare Opal Organon
```
Runs the inspection on two engines side-by-side — useful when choosing which to retreat on next.

---

## Integration

| When to run | What to ask for |
|-------------|-----------------|
| Before planning a sprint | `fleet` — see the full picture |
| Before invoking retreat-accelerator | `--filter red` — pick the lowest-health engine |
| Before updating MEMORY.md/CLAUDE.md counts | `--focus presets` — ground-truth preset counts |
| After a major Exo Meta batch | `--focus presets` — verify counts updated |
| Monthly health check | `fleet` — catch drift before it becomes debt |

---

## Execution Model

The Inspector dispatches parallel subagents — one per engine — each reading that engine's files independently. Results are streamed back and aggregated into the final report. This means even a 50-engine fleet scan completes in the time it takes to read the slowest engine, not the sum of all reading times.

For large fleets (50+ engines at current scale), the Inspector batches subagents in groups of 8 to avoid overloading the context budget.
