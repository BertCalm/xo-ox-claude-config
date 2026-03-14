---
name: pipeline-connector
description: Pipeline Connector — builds optimized multi-skill pipelines for complex XO_OX goals by identifying skill dependencies, parallelization opportunities, and the right handoffs between skills. The Ringleader's tactical planner. Use when the user says 'pipeline connector', 'build me a pipeline', 'what order should I run these skills', 'how do I connect X to Y', 'what feeds into what', 'skill dependencies', 'optimal skill order', 'what should run first', has a goal that clearly spans multiple skills and wants an execution plan before invoking the Ringleader, wants to understand how two specific skill outputs connect (e.g., what exactly does Exo Meta hand off to Guru Bin?), or is designing a new workflow and needs to understand inter-skill data flow.
---

# Pipeline Connector

**The wiring diagram between skills.**

The Ringleader knows which skills to call. The Pipeline Connector knows exactly what each skill outputs, what each skill needs as input, and how to pass that information so nothing is lost between handoffs. It's the difference between skills running sequentially by coincidence and skills running as a coherent pipeline where each stage feeds the next.

---

## Skill I/O Map

The definitive reference for what each skill produces and consumes:

| Skill | Inputs (needs) | Outputs (produces) |
|-------|---------------|-------------------|
| `/theorem` | Current ecosystem state, date | 3 concept options (name, DNA, architecture brief) |
| `/producers-guild` | Engine list, target genres | Preset gap analysis, market recommendations, priority list |
| `/synth-seance` | Engine source, presets, target question | Verdict (score, blessings, concerns), ghost consensus |
| `/board` | Any artifact (code, docs, site, presets) | Brand compliance audit, doctrine violations, approved/flagged |
| `/sweep` | Codebase path | Issue list (P0/P1/P2), fix recommendations |
| `/historical-society` | Memory + doc files | Corrections list, updated memory files |
| `/new-xo-engine` | Concept brief (from Theorem or user) | Engine source, scaffold, parameter list, preset stubs |
| `/exo-meta` | Gap analysis (from Guild) or engine name | Preset designs (names, DNA, parameter tables) |
| `/guru-bin` | Engine source, presets, or preset tables | Refinement log (old→new parameter values), scripture additions |
| `/preset-forge` | Guru Bin refinement log or parameter tables | `.xometa` preset files, optional C++ code |
| `/preset-qa` | `.xometa` files | Validation report (errors, warnings, fleet health) |
| `/retreat-accelerator` | Engine name | Retreat briefing (architecture, presets, scripture, priorities) |
| `/scripture-keeper` | Query or engine name | Relevant scripture verses, index, gap analysis |
| `/kai` | Preset library, target MPC model | XPN export packages, XPM maps, validation report |
| `/atelier` | Site files, research input | HTML/CSS changes, blog posts, Signal posts |
| `/fab-five` | Any content | Elevated content (style, polish, voice, presentation) |
| `/post-engine-completion-checklist` | Completed engine or phase | Updated CLAUDE.md, MEMORY.md, knowledge files |
| `/fleet-inspector` | (none) | Fleet health report (engine × dimension matrix) |
| `/engine-comparator` | 2+ engine names + use case | Side-by-side analysis, recommendation |
| `/dsp-profiler` | Engine name | Cost breakdown, optimization opportunities |
| `/coupling-cookbook` | Engine pair or use case | Coupling recipe, design output |
| `/pilgrimage-tracker` | Campaign name | Status report, session summary |
| `/flywheel` | (none) | Skill improvement analysis, usage patterns |

---

## Dependency Rules

### Hard Dependencies (must be sequential)

- `/theorem` → `/new-xo-engine` — concept must exist before scaffolding
- `/producers-guild` → `/exo-meta` — gap analysis feeds preset design
- `/exo-meta` → `/guru-bin` — presets must exist before refinement
- `/guru-bin` → `/preset-forge` — refinement log needed to generate files
- `/preset-forge` → `/preset-qa` — files must exist to validate
- `/new-xo-engine` → `/synth-seance` — engine must exist for ghosts to review
- `/retreat-accelerator` → `/guru-bin` (retreat mode) — briefing precedes retreat
- `/scripture-keeper` (brief) → `/guru-bin` — scripture loaded before meditation

### Soft Dependencies (preferred order, not required)

- `/synth-seance` before `/exo-meta` — ghost wisdom improves preset design
- `/board` before `/atelier` — brand check before publishing
- `/sweep` before `/post-engine-completion-checklist` — fixes before lock-in
- `/fleet-inspector` before `/retreat-accelerator` — know the gaps before choosing target

### Fully Parallelizable (no dependencies between each other)

- `/board` + `/sweep` + `/historical-society` + `/producers-guild`
- `/synth-seance` + `/producers-guild`
- `/preset-qa` + `/dsp-profiler` (different dimensions)
- `/engine-comparator` + `/coupling-cookbook`
- Any two skills working on different engines

---

## Pipeline Builder

When the user describes a goal, the Pipeline Connector produces an execution plan:

**Input**: "I want to ship a new engine concept I have and turn it into a full preset library."

**Output**:
```
PIPELINE: Engine Concept → Shipped Library

Phase 1: Validate (Sequential)
  /theorem ──→ concept brief
  (or skip if user already has concept)

Phase 2: Build (Sequential)
  /new-xo-engine ──→ engine source + parameter list

Phase 3: Review (Parallel)
  ├─ /synth-seance ──→ ghost verdict
  └─ /producers-guild ──→ preset gap analysis

Phase 4: Lock (Sequential)
  /post-engine-completion-checklist ──→ docs updated

Phase 5: Sound Design (Sequential, feeds next)
  /exo-meta (fed by Guild gap analysis) ──→ preset designs

Phase 6: Refine (Sequential pipeline)
  /retreat-accelerator ──→ briefing
  /guru-bin (retreat mode) ──→ refinement log
  /preset-forge ──→ .xometa files
  /preset-qa ──→ validation

Phase 7: Expand (Parallel)
  ├─ /kai ──→ MPC export
  └─ /atelier ──→ site update + Signal post

Handoff notes:
- Phase 3 outputs feed Phase 5 (pass Guild gap list to Exo Meta prompt)
- Phase 6 Guru Bin output (refinement log) goes directly into Preset Forge
- Phase 7 requires Phase 6 complete (files must exist before Kai exports)
```

---

## Handoff Templates

The Connector produces exact handoff prompts to pass between skills — so the receiving skill has the right context:

### Theorem → new-xo-engine
```
Using the following concept from /theorem:
Name: {name}
Synthesis: {synthesis type}
Architecture: {key DSP elements}
feliX-Oscar polarity: {value}
Target genres: {list}

Please scaffold this engine.
```

### Producers-Guild → Exo Meta
```
Based on the Producer's Guild analysis, the following preset gaps need filling:
Engine: {name}
Missing moods: {list}
Underrepresented DNA: {dimensions with gaps}
Top genre requests: {list}
Priority preset themes: {list from Guild}

Please design presets to fill these gaps.
```

### Guru Bin → Preset Forge
```
Using the following Guru Bin refinement log:
Engine: {name}
[paste the refinement table]

Mood: {recommended mood based on sound character}
DNA: {from Guru Bin's analysis}

Please forge these into .xometa files.
```

---

## Arguments

- `{goal description}` — build a pipeline for a stated goal
- `{skill A} → {skill B}` — explain the handoff between two specific skills
- `{skill name}` — show full I/O for a single skill
- `validate` — check if a proposed pipeline has dependency violations
