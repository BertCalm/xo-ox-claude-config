---
name: historical-society
description: "The Historical Society — audit, clean, update, and optimize documentation and memory files across the XO_OX ecosystem. Dispatches parallel Archivist agents to scan memory files, CLAUDE.md guides, specs, playbooks, knowledge files, templates, and concept briefs. Fixes staleness, improves clarity, builds missing indexes, and optimizes docs to accelerate all other work. Reports to a Chief of Staff who updates the primitive>skill>context Knowledge Tree and suggests new skills. Use when: user says 'historical society', 'fix docs', 'doc audit', 'clean up documentation', 'update docs', 'check memory', 'documentation pass', 'curate', 'archive', 'librarian', or wants documentation quality improved. Also invoke after completing engine phases, before releases, when memory is bloated, when docs feel stale, or daily via /loop. The documentation-specific complement to /sweep and /board."
---

# The Historical Society

Documentation custodians for the XO_OX ecosystem. While the Board governs and the Sweep fixes, the Historical Society **curates** — treating documentation as living infrastructure that accelerates every other activity.

The Society's philosophy: every document should make someone faster. If a doc doesn't help a designer design, a builder build, or a tester test, it's either missing something or shouldn't exist.

## Arguments

- `mode`: (optional) `full` (default) — comprehensive audit across all documentation. `daily` — lightweight pass focused on staleness and drift since last run. `deep <domain>` — thorough audit of a single domain (see domains below).
- `scope`: (optional) Which repos to audit. Default: all XO_OX repos under `~/Documents/GitHub/XO*` plus memory at `~/.claude/projects/-Users-joshuacramblet/memory/`. Can specify a single repo path.
- `fix`: (optional) `true` (default) — apply safe fixes directly. `false` — report only, no changes.

## The Archivists

Five specialist agents, each responsible for a documentation domain. They dispatch in parallel, audit their domain, and return findings to the Chief of Staff.

| Archivist | Domain | What They Guard |
|-----------|--------|-----------------|
| **The Chronologist** | Time & Truth | Staleness, version drift, dates, counts that rot, status markers stuck on "WIP" |
| **The Cataloguer** | Structure & Navigation | Indexes, cross-references, broken links, discoverability, missing tables of contents |
| **The Editor** | Clarity & Quality | Prose quality, jargon density, contradictions, redundancy, readability for newcomers |
| **The Accelerator** | Velocity & Utility | Docs that should exist but don't, docs that could unblock common workflows, optimization opportunities |
| **The Archivist** | Memory & Persistence | MEMORY.md health, satellite memory files, CLAUDE.md accuracy, knowledge compendium growth |

## Protocol

### Phase 1: Census

Before dispatching Archivists, build a map of the documentation estate:

1. **Discover all XO_OX repos** — scan `~/Documents/GitHub/XO*`
2. **Inventory documentation** per repo:
   - CLAUDE.md (root guide)
   - `docs/` or `Docs/` folders (specs, plans, design docs)
   - `synth_playbook/` (agent skills, knowledge, modules, refinement logs)
   - `templates/` (design templates)
   - Concept briefs (if XOmnibus)
3. **Read memory state** — `~/.claude/projects/-Users-joshuacramblet/memory/MEMORY.md` + all satellite `.md` files
4. **Read the Knowledge Tree** — `~/.claude/skills/board/knowledge/index.md` to understand existing primitives/skills/context
5. **Check recent git activity** across repos (last 5-10 commits each) to understand what's changed since the last Society meeting

Compile this into a **Census Report** — a snapshot of what exists, how much, and when it was last touched. This gets passed to every Archivist.

### Phase 2: Dispatch Archivists

Launch all 5 Archivist agents **in parallel** using the Agent tool. Each receives the Census Report plus their domain-specific brief.

#### The Chronologist — Time & Truth

Hunts for documentation that has fallen behind reality:

- **Stale counts**: engine totals, preset totals, file counts, parameter counts — cross-reference every number in prose against the actual source of truth (directory listings, source code, git)
- **Status drift**: items marked "planned", "WIP", "in progress", "coming soon", "Phase 0" — check if they've actually been completed
- **Version mismatches**: JUCE versions, schema versions, spec versions cited in docs vs actual
- **Date archaeology**: relative dates ("last week", "recently") that are now meaningless — flag for conversion to absolute dates or removal
- **Dead references**: links to files, repos, URLs, or concepts that no longer exist
- **Completed work not documented**: check recent git commits for features/fixes that aren't reflected in docs

Output format per finding:
```
[STALE] file:line — "26 engines" → actual count is 28 (source: Docs/engine_catalog.md)
[DRIFT] file:line — "Phase 0" but repo shows 53 source files and auval passes
[DEAD] file:line — links to docs/old_spec.md which doesn't exist
```

#### The Cataloguer — Structure & Navigation

Ensures documentation is organized and findable:

- **Missing indexes**: directories with 5+ files but no README or index pointing to them
- **Broken cross-references**: `[link text](path)` where path doesn't resolve
- **Orphaned documents**: files that nothing links to and have no clear discovery path
- **Inconsistent structure**: repos that deviate from the standard layout (CLAUDE.md, docs/, synth_playbook/)
- **Missing tables of contents**: long documents (100+ lines) without navigation aids
- **Duplicate coverage**: two documents covering the same topic with no clear authority hierarchy

Output: findings with file paths, what's missing, and a suggested structural fix.

#### The Editor — Clarity & Quality

Evaluates documentation for humans reading it:

- **Jargon density**: sections that assume deep context without providing it — especially in CLAUDE.md and README files that newcomers read first
- **Contradictions**: two documents asserting different things about the same topic (parameter names, signal flow, architecture)
- **Redundancy**: the same information repeated across multiple files with no single source of truth
- **Incomplete sections**: headers with no content, stub descriptions, placeholder text
- **Prose quality**: unclear sentences, passive voice where active is clearer, walls of text that could be tables
- **Outdated terminology**: legacy names that should use canonical names (check against name migration reference)

Output: findings with specific text excerpts, what's wrong, and a rewrite suggestion.

#### The Accelerator — Velocity & Utility

The most strategic Archivist — evaluates documentation as a **tool for speed**:

- **Missing recipes**: common workflows that have no documentation (e.g., "how to add a new coupling type", "how to create a preset category")
- **Undocumented decisions**: architectural choices visible in code but not explained anywhere — future builders will waste time reverse-engineering them
- **Template gaps**: design templates that are missing for common patterns the team uses
- **Knowledge file gaps**: knowledge compendium entries that should exist based on completed work but don't
- **Coupling documentation**: cross-engine interaction patterns that are possible but not documented
- **Onboarding friction**: places where a new Claude session would struggle to understand the project without excessive exploration

The Accelerator thinks about what documentation would make the next `/new-xo-engine`, `/board`, `/sweep`, or development session measurably faster.

Output: specific documentation that should be created or enhanced, with a brief justification of what it would accelerate.

#### The Archivist — Memory & Persistence

Guards the institutional memory system:

- **MEMORY.md health**: line count (200 limit), section balance, stale entries, entries that should be promoted to satellite files
- **Satellite memory files**: accuracy, relevance, staleness — do they still reflect reality?
- **CLAUDE.md accuracy**: do per-project CLAUDE.md files match actual project state? (build commands, key files, architecture descriptions)
- **Knowledge compendium growth**: are `agent_knowledge/` files growing after each project cycle as intended?
- **Refinement log organization**: are logs timestamped, searchable, and useful for future reference?
- **Knowledge Tree currency**: are the Board's primitives, skills, and context entries still accurate?

Output: specific memory/persistence issues with current state, correct state, and suggested fix.

### Phase 3: Restoration

After all Archivists report, consolidate and act:

#### Triage

Organize findings into three tiers:

| Tier | Description | Action |
|------|-------------|--------|
| **Restore** | Objectively wrong: stale counts, broken links, dead references, status drift | Auto-fix (if `fix=true`) |
| **Curate** | Quality improvements: jargon reduction, missing indexes, structural inconsistencies | Apply safe fixes, flag subjective ones |
| **Commission** | New documentation needed: missing recipes, undocumented decisions, template gaps | Present as recommendations with priority |

#### Apply Fixes

In `fix=true` mode, make direct changes for Restore and safe Curate items:
- Update stale counts with verified numbers
- Fix broken cross-references
- Update status markers for completed work
- Add missing indexes for orphaned directories
- Update MEMORY.md entries that have drifted
- Correct CLAUDE.md inaccuracies

For each fix, note what was changed and why.

### Phase 4: Chief of Staff Report

The Chief of Staff synthesizes findings and maintains the **Knowledge Tree** (shared with the Board at `~/.claude/skills/board/knowledge/`).

#### Step 1: Update the Knowledge Tree

Review all Archivist findings and determine if any reveal:

- **New Primitives** — immutable documentation truths discovered through this audit
  - Example: "Preset counts in prose always drift within 2 weeks of a preset expansion run"
  - Example: "MEMORY.md entries for completed projects compress below useful density after 30 days"
- **New Skills** — reusable documentation procedures worth codifying
  - Example: "Post-engine-completion documentation checklist" (if the Accelerator keeps finding the same gaps)
- **New Context** — situational knowledge about specific repos/engines
  - Example: "XOverworld's CMake requires OSX_ARCHITECTURES before project() — 3 docs mention this differently"

Write new entries to `~/.claude/skills/board/knowledge/` following the existing format (see Board SKILL.md Phase 5 for templates).

Update `~/.claude/skills/board/knowledge/index.md` with new entries.

#### Step 2: Skill Gap Analysis

The Chief of Staff's signature contribution — analyzing the primitive>skill>context framework for gaps:

- **Primitives without skills**: truths we know but haven't operationalized (e.g., we know preset counts drift but have no automated check)
- **Skills without primitives**: procedures that lack foundational grounding (fragile — could break when assumptions change)
- **Context without resolution path**: situational knowledge that's been "active" too long without becoming a primitive or getting resolved
- **Recurring Accelerator findings**: if the same missing-recipe or missing-doc pattern appears across 3+ audits, recommend a new skill to prevent it

#### Step 3: Produce the Report

```
## Historical Society Report — [Date]
### Mode: [full/daily/deep]

### Census
- Repos scanned: [N]
- Documents audited: [N]
- Memory files checked: [N]

### Restorations (auto-fixed)
| File | What Changed | Why |
|------|-------------|-----|

### Curations (applied)
| File | Improvement | Impact |
|------|------------|--------|

### Commissions (recommended)
| Priority | What's Needed | What It Accelerates |
|----------|--------------|---------------------|

### Chief of Staff — Knowledge Tree Update
| Type | ID | Summary |
|------|----|---------|

### Chief of Staff — Skill Suggestions
| Suggested Skill | Signal | Expected Impact |
|----------------|--------|-----------------|

### Documentation Health Score
| Domain | Health | Trend |
|--------|--------|-------|
| Time & Truth | [GREEN/YELLOW/RED] | [improving/stable/declining] |
| Structure & Navigation | ... | ... |
| Clarity & Quality | ... | ... |
| Velocity & Utility | ... | ... |
| Memory & Persistence | ... | ... |

### Next Run Recommendations
[What the daily/next run should focus on based on today's findings]
```

### Phase 5: Persist

Save the report to `~/.claude/skills/historical-society/reports/` with the filename `[YYYY-MM-DD]-[mode].md`. Create the directory if it doesn't exist.

If running in `daily` mode, also update a rolling `latest.md` that subsequent daily runs can reference to avoid re-auditing unchanged areas.

## Daily Mode

When invoked via `/loop` or with `mode=daily`, the Historical Society runs a lighter pass:

1. **Skip full Census** — read `latest.md` from the previous run instead
2. **Focus on delta** — only scan files modified since the last run (use git to detect changes)
3. **Dispatch only relevant Archivists** — if only docs changed, skip Code-adjacent checks
4. **Chronologist always runs** — staleness is the most time-sensitive domain
5. **Archivist always runs** — memory health should be checked every run
6. **Produce a shorter report** — just the changes, restorations, and any new Knowledge Tree entries

Schedule: `/loop 24h /historical-society` for daily runs.

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| **Board** | The Society feeds the Board's Knowledge Tree. Board meetings may trigger a Society audit. Society reports inform D1 (Governance) and D8 (Design) findings. |
| **Sweep** | Sweep fixes code and surface issues. The Society goes deeper on documentation specifically — quality, utility, acceleration potential. A sweep's Doc Detective handles quick fixes; the Society handles longitudinal documentation health. |
| **Fab Five** | The Society ensures documentation substance. Fab Five ensures documentation style. |
| **New XO Engine** | After a new engine is designed, the Society audits whether all documentation was properly created. The Accelerator checks if the new engine's docs would actually help someone build on it. |

## Values

1. **Documents are tools, not trophies** — every doc should make someone faster at something specific
2. **Single source of truth** — when the same fact lives in multiple places, one must be authoritative and the rest must derive from it
3. **Staleness is debt** — an outdated doc is worse than no doc, because it misleads with confidence
4. **The Knowledge Tree grows from evidence** — primitives emerge from repeated observation, not from speculation
5. **Suggest, don't hoard** — when the Society spots a gap that a new skill could fill, it says so
