---
name: sweep
description: "Comprehensive codebase sweep that dispatches parallel detective agents to audit and fix issues across code, documentation, UI, infrastructure, tools, presets, brand alignment, and creative depth. Invoke this skill when the user says 'sweep', 'clean up', 'polish', 'audit', 'deep clean', 'tighten up', 'review everything', 'make it rock solid', or wants a periodic quality pass across the whole project. Also use proactively after completing a major feature, before releases, or when work feels stale. Can target specific areas (e.g., `/sweep docs`) or run the full sweep (default). Can be scheduled with `/loop` (e.g., `/loop 24h /sweep`)."
---

# Sweep — Codebase Detective Squad

Deploy a team of parallel investigator agents to audit every surface of the project, fix what's safe to fix, and flag what needs human judgment.

## Arguments

- `area`: (optional) Target a specific sweep area instead of running all. One of: `code`, `docs`, `ui`, `infra`, `presets`, `brand`, `creative`, `alignment`. Default: all areas.
- `mode`: (optional) `fix` (default) — auto-fix safe issues and flag risky ones. `report` — produce findings report without making changes.
- `focus`: (optional) Free-text focus hint, e.g., "engine counts" or "stale parameter references". Narrows the sweep within the selected area(s).

## How It Works

### Phase 1: Reconnaissance

Before dispatching detectives, understand the project:

1. **Read CLAUDE.md** (and any nested CLAUDE.md files) to understand the project's identity, rules, conventions, and architecture
2. **Scan repo structure** — `ls` key directories to understand what exists (source, docs, UI, tools, presets, tests, config)
3. **Check git status** — understand what's changed recently, what branch you're on, any uncommitted work
4. **Read recent commits** (last 10-20) to understand the trajectory of recent work

This gives each detective the context they need. Compress the findings into a brief project profile that gets passed to every agent.

### Phase 2: Dispatch Detectives

Launch detective agents **in parallel** using the Agent tool. Each detective is an Explore-type or general-purpose agent given a specific brief. Launch as many as applicable in a **single message** for maximum parallelism.

The detectives don't make changes — they investigate and report findings. All fixing happens in Phase 3.

#### Detective Briefs

**1. CODE DETECTIVE** (`code`)
Search the codebase for:
- Dead code: unused functions, unreachable branches, commented-out blocks
- TODO/FIXME comments — catalog them with file:line and assess if they're stale or active
- Performance issues: unnecessary allocations, repeated work, missing caching opportunities
- Safety issues: unchecked inputs at system boundaries, potential crashes
- Convention violations: patterns that break the project's stated rules (from CLAUDE.md)
- Duplicated logic that could be consolidated

Output: List of findings, each with file:line, severity (low/medium/high), and suggested fix.

**2. DOC DETECTIVE** (`docs`)
Audit all documentation for:
- **Stale numbers**: counts, statistics, version numbers that may have drifted from reality. Cross-reference prose claims against actual file counts, directory listings, and source code.
- **Terminology drift**: inconsistent naming (check for legacy names, abbreviations, mismatched capitalization)
- **Broken cross-references**: links to files/sections/URLs that don't exist
- **Missing coverage**: features or components that exist in code but have no documentation
- **Status markers**: things marked "TODO", "WIP", "planned", "coming soon" that may already be done
- **Contradictions**: places where two docs say different things about the same topic

Output: List of findings with file:line, what's wrong, and what the correct value should be (verified from source).

**3. UI DETECTIVE** (`ui`)
Search UI code (source files, templates, HTML, config) for:
- **Stale strings**: hardcoded numbers, names, or descriptions that don't match current state
- **Hardcoded values** that should be dynamic or derived from a single source
- **Accessibility**: missing alt text, aria labels, contrast issues, keyboard navigation gaps
- **Broken links or references** in web pages, help text, about screens
- **Inconsistent styling**: mismatched fonts, colors, spacing that deviate from the design system

Output: List of findings with file:line and suggested fix.

**4. INFRA DETECTIVE** (`infra`)
Audit build system, scripts, and infrastructure:
- **Build warnings** or deprecated patterns in CMake, package.json, Makefile, etc.
- **Stale dependencies**: outdated versions, unused dependencies, missing lockfile entries
- **Script health**: Python/shell scripts with hardcoded paths, stale references, missing error handling
- **CI/CD**: workflow files that reference old branches, missing steps, inefficient pipelines
- **Environment**: config files, .env templates, gitignore gaps

Output: List of findings with file:line and suggested fix.

**5. PRESET DETECTIVE** (`presets`)
Audit data files, configuration, and presets:
- **Format consistency**: all files of the same type should follow the same schema
- **Missing fields**: required fields that are absent in some entries
- **Naming conventions**: file names and internal identifiers that break the project's naming rules
- **Orphaned files**: presets or configs that reference things that no longer exist
- **Coverage gaps**: categories or taxonomies that are unevenly filled

Output: List of findings with file path, what's inconsistent, and the expected format.

**6. BRAND DETECTIVE** (`brand`)
Check alignment with the project's stated identity and conventions:
- **Naming violations**: identifiers, file names, or labels that break stated naming conventions
- **Style guide adherence**: colors, typography, terminology that deviate from the design system
- **Voice consistency**: documentation tone, preset names, UI copy that feels off-brand
- **Identity drift**: features or descriptions that contradict the project's stated character

Output: List of findings with specific text and suggested correction.

**7. CREATIVE DETECTIVE** (`creative`)
Evaluate the depth and quality of creative content:
- **Sound design / domain guides**: are they deep enough? Do they provide actionable specifics (parameter values, sweet spots, recipes) or just surface descriptions?
- **Lore and mythology**: is the creative world consistent? Are there unexplored connections or contradictions?
- **Historical grounding**: does the project reference real domain history (synth history, music theory, art movements, etc.) where appropriate?
- **Coupling / interaction design**: are creative combinations documented? Are pairing suggestions inspired or generic?

Output: Specific suggestions for deepening content, with locations and examples.

**8. ALIGNMENT DETECTIVE** (`alignment`)
Cross-cutting consistency check:
- **Source ↔ Docs**: do documented features match what the code actually does?
- **UI ↔ Source**: do UI strings match source code constants?
- **Presets ↔ Schema**: do data files match the documented format?
- **README ↔ Reality**: does the top-level description match the actual state?
- **Inter-doc consistency**: do different documents agree on the same facts?

Output: List of contradictions with both locations and the correct resolution (verified from source).

### Phase 3: Triage and Fix

After all detectives report back, consolidate findings into three buckets:

#### Auto-Fix (Safe)
Changes that are objectively correct and low-risk:
- Stale numbers that can be verified from source (file counts, directory listings)
- Terminology corrections (legacy → canonical when the mapping is documented)
- Broken cross-references where the correct target is obvious
- Missing fields in data files where the correct value is derivable
- Dead code removal when the code is clearly unreachable

**In `fix` mode**: Make these changes directly using Edit/Write tools.
**In `report` mode**: List them as "ready to fix" with the specific change.

#### Flag for Review
Changes that need human judgment:
- Creative content improvements (deepening lore, adding history)
- Architectural suggestions (consolidating code, adding abstractions)
- Naming changes that might affect external interfaces
- Anything where two documents disagree and you're not sure which is correct

**Both modes**: Present these clearly with the trade-off or question.

#### No Action Needed
Things the detectives checked that are fine. Mention briefly so the user knows the area was audited.

### Phase 4: Report

Present a summary organized by severity:

```
## Sweep Report — [Project Name]

### Fixed (N items)
- [file:line] What was wrong → What it is now

### Needs Your Call (N items)
- [file:line] The situation + options

### All Clear
- Areas that passed inspection
```

Keep it concise. The user should be able to scan the report in under 2 minutes.

## Running Periodically

Use `/loop` to schedule regular sweeps:

```
/loop 24h /sweep           # Full daily sweep
/loop 4h /sweep docs       # Doc check every 4 hours
/loop 1h /sweep alignment  # Hourly consistency check
```

After major milestones (new feature, new engine, release prep), run a full sweep manually.

## Tips for Good Sweeps

- The more complete your CLAUDE.md, the smarter the detectives are. Project rules, naming conventions, architecture decisions — all of this informs what "correct" means.
- A targeted sweep (`/sweep docs`) is faster and cheaper than a full sweep. Use it when you know where the entropy is.
- `report` mode is useful when you want to review before any changes touch the codebase.
- After a sweep fixes things, consider a quick `/sweep alignment` to make sure the fixes didn't introduce new inconsistencies.
