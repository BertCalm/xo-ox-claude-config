---
name: retreat-accelerator
description: Retreat Accelerator — pre-loads everything needed for a Guru Bin retreat in one shot, so the session starts with full context instead of 20 minutes of setup. Reads the engine's source, presets, CLAUDE.md entry, seance verdict, and existing scripture — then hands a fully-prepared briefing to Guru Bin. Use when the user says 'retreat accelerator', 'accelerate the retreat', 'prep for a retreat', 'load up [engine]', 'get ready for a guru bin retreat', 'brief me before the retreat', 'start the retreat on [engine]', wants to run a Guru Bin retreat but wants setup done first, or is about to invoke /guru-bin with mode:retreat. Also invoke proactively when Guru Bin is about to begin a Retreat (Phase R1: Pilgrimage) — the Accelerator handles the pilgrimage so Guru Bin can start at Phase R2.
---

# Retreat Accelerator

**The pilgrimage, pre-completed.**

Guru Bin's Retreat Protocol starts with Phase R1: Pilgrimage — the Flock reads everything about the engine before meditation begins. On a complex engine, that's 5-10 files, potentially thousands of lines. The Accelerator does this ahead of time, in parallel, so the retreat can begin at Phase R2: Silence the moment Guru Bin arrives.

---

## What the Accelerator Reads

For a given engine `{EngineName}`, the Accelerator reads in parallel:

### 1. Engine Source (DSP intelligence)
- `Source/Engines/{EngineName}/{EngineName}Engine.h` — full DSP source, every parameter
- If >500 lines, extracts: parameter list, signal chain summary, key methods

### 2. Existing Presets (what's been designed)
- Scans `Source/Engines/{EngineName}/Presets/` — count by mood, list names
- Scans `Presets/XOmnibus/*/` for presets where `"engines"` includes the engine
- Reports: total count, mood distribution, coverage gaps

### 3. CLAUDE.md Entry (architecture)
- Reads the engine's row in the Engine Modules table
- Reads the parameter prefix entry
- Notes any CLAUDE.md warnings or gotchas about this engine

### 4. Seance Verdict (historical guidance)
- Checks `Docs/xomnibus_landscape_2026.md` for this engine's seance entry
- Reads relevant blessing (if one exists) from the 15 Blessings list
- Notes any doctrines the seance flagged as unresolved for this engine

### 5. Scripture (doctrine that applies)
- Invokes Scripture Keeper to pull all applicable verses
- Notes which Books are most relevant based on the engine's synthesis architecture
- Loads any existing retreat chapter from `scripture/retreats/{engine-name}-retreat.md`

### 6. Cadence Log (retreat history)
- Checks `scripture/cadence-log.md` for any prior retreats on this engine
- Notes: last retreat date, key discoveries made, how many presets were created

### 7. Sound Design Guide (if exists)
- Checks `Docs/xomnibus_sound_design_guides.md` for this engine's section
- Notes: which guides exist, which are still stubs

---

## The Briefing

After reading all sources, the Accelerator produces a single **Retreat Briefing** document:

```
══════════════════════════════════════════════════════
  RETREAT BRIEFING: {EngineName}
  Prepared for Guru Bin — {date}
══════════════════════════════════════════════════════

## Engine Identity
- Gallery code: {CODE}
- Accent color: {color}
- Aquatic mythology: {creature, water column depth}
- feliX-Oscar polarity: {description}
- Parameter prefix: {prefix}_

## Architecture Summary
- Synthesis type: {what it is}
- Signal chain: {Voice → Stage → Stage → Output}
- DSP complexity: {light / medium / heavy}
- Polyphony: {N voices}
- Key parameter groups: {list}
- Hidden capabilities (not obvious from UI): {if any found in source}

## Preset Inventory
- Total presets: {N}
- Mood distribution: Foundation {N}, Atmosphere {N}, Entangled {N}, Prism {N}, Flux {N}, Aether {N}
- Coverage gaps: {moods with zero or one preset}
- Notable presets: {2-3 standout names}
- Thin coverage areas: {DNA gaps — e.g., "no high-aggression presets"}

## Seance History
- Seance verdict: {summary}
- Blessings: {if any}
- Unresolved concerns: {list}
- Ghost consensus: {what they agreed on}

## Applicable Scripture
- {N} verses from Books I-VI apply
- Most relevant Book: {Book name} — {why}
- Key verses to start with: {2-3 verse titles}
- Retreat chapter exists: {yes/no}

## Retreat Priorities (recommended)
Based on the full briefing, the Accelerator recommends Guru Bin focus on:
1. {Top priority — e.g., "Preset DNA gaps: no Aether or high-aggression presets"}
2. {Second priority — e.g., "Parameter interaction: The Finger has never explored oscA + character interaction"}
3. {Third priority — e.g., "Coupling: OPAL coupling has 3 presets but no Atmosphere variants"}

## What Guru Bin Will Find Fresh
These aspects of the engine appear unexplored in existing scripture and presets:
- {e.g., "The feedback path — no scripture covers it; likely yields new scripture verses"}
- {e.g., "Velocity curve above 100 — no presets demonstrate the ceiling behavior"}

══════════════════════════════════════════════════════
  READY FOR PHASE R2: SILENCE
══════════════════════════════════════════════════════
```

---

## Hand-Off to Guru Bin

After producing the Briefing, the Accelerator:

1. Presents the Briefing to the user
2. Asks: "Ready to begin the retreat?"
3. On confirmation, passes control to Guru Bin with the Briefing as context — Guru Bin starts at **Phase R2: Silence** (one note, C3, velocity 64, 60 seconds)
4. Guru Bin does NOT need to re-read the files — the Accelerator has already done it

---

## Fleet Retreat Scheduler

When called without a specific engine, the Accelerator looks at the full fleet and recommends which engine is most overdue for a retreat:

**Scoring factors:**
- No retreat chapter exists (+3 points)
- Last retreat was >60 days ago (+2 points)
- Preset count is below fleet average (+2 points)
- Seance flagged unresolved concerns (+1 point)
- Recent build phase completed but no retreat followed (+1 point)
- DNA coverage gaps (missing moods or extreme DNA values) (+1 point)

Reports the top 3 engines by score with their rationale. The user picks which to retreat.

---

## Arguments

- `{engine name}` — accelerate for a specific engine
- (none) — run Fleet Retreat Scheduler and recommend top 3 candidates
- `brief-only` — produce the Briefing but don't hand off to Guru Bin
- `quick` — skip the seance/scripture lookup, just read source + presets (faster, less context)
