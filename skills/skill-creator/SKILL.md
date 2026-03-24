---
name: skill-creator
description: "The Adaptive Skill Builder — creates new skills, refines existing ones, and optimizes skill descriptions for better triggering. Use when: user says 'skill-creator', 'create a skill', 'new skill', 'build a skill', 'skill builder', 'adapt skill', 'refine skill', 'improve skill description', 'skill description', 'skill template', 'optimize triggers', 'undertriggering', 'overtriggering', 'skill eval', 'eval cycle', when the Flywheel identifies a new skill candidate or flags a skill for revision, when a user describes a repeated workflow that would benefit from a dedicated skill, or when Sister Cadence triggers skill protocol refinement. The missing link between identifying skill needs and actually building them."
---

# The Adaptive Skill Builder

> "Every workflow repeated three times is a skill waiting to be born."

The Skill Creator closes the loop in the XO_OX skill ecosystem. The Flywheel identifies what needs building or fixing. The Skill Creator builds and fixes it. Together they form a continuous improvement engine where skills evolve based on real usage data.

## The Cast

### Ada — The Architect of Skills
Ada designs skill structure. She reads the ecosystem, identifies patterns, and builds skills that fit naturally alongside the existing roster. Ada knows every skill in the ecosystem and refuses to create duplicates or near-duplicates.

### Evo — The Optimizer
Evo takes existing skills and makes them sharper. He analyzes trigger descriptions, tightens scope, fixes undertriggering (skill should fire but doesn't) and overtriggering (skill fires when it shouldn't). Evo works from Flywheel data when available, from user feedback when not.

## Modes

### Mode 1: Create — Build a New Skill

Invoked with `/skill-creator create [name]` or when the Flywheel report identifies a new skill candidate.

#### Phase 0: Intake

Before writing a single line:

1. **Name check** — Does the skill name follow XO_OX conventions? Is it memorable and descriptive?
2. **Duplicate check** — Read the full skill roster (from Ringleader's table or scan `skills/`). Does this overlap with an existing skill?
3. **Scope check** — Is this a skill (reusable workflow) or a one-off task? Skills must serve 3+ future invocations.
4. **Character check** — Does this skill need personas? Only add characters if they serve a purpose (domain specialization, multi-perspective review, or workflow stages). Simple skills don't need characters.

If any check fails, tell the user why and suggest alternatives.

#### Phase 1: Design

Gather requirements:

| Question | Why It Matters |
|----------|---------------|
| What does this skill produce? | Output format drives structure |
| When should it trigger? | Description field is the most important line in the file |
| What inputs does it need? | Arguments section |
| Which existing skills does it connect to? | Integration points |
| What model/effort level fits? | Ringleader roster entry |

#### Phase 2: Build

Create the skill following the ecosystem template:

```
skills/[name]/SKILL.md
```

**Required sections:**

```markdown
---
name: [skill-name]
description: "[comprehensive trigger description — this is the MOST important field]"
---

# [Skill Title]

[1-2 sentence purpose statement]

## [Core Sections — varies by skill type]

[The actual skill protocol, workflow, or instructions]

## Output Format

[What the skill produces — templates, tables, structured output]

## Arguments

[Optional parameters that modify behavior]

## Integration Points

| Connects To | How |
|-------------|-----|
| /skill-x | [relationship] |
```

**Description field rules:**
- Start with a clear one-sentence purpose
- List ALL trigger phrases the user might say (be generous — undertriggering is worse than overtriggering)
- Include contextual triggers ("when X happens, also invoke this skill")
- Mention proactive triggers if applicable ("invoke at session start when...")
- Keep it as one long string — the description field is a single YAML value

#### Phase 3: Validate

Run the eval cycle:

1. **Trigger test** — Read the description. Would Claude invoke this skill for each of these scenarios?
   - The obvious case (user says the skill name)
   - The indirect case (user describes the need without naming the skill)
   - The negative case (similar request that should NOT trigger this skill)
2. **Structure test** — Does the SKILL.md follow ecosystem conventions?
   - YAML frontmatter with `name` and `description`
   - Clear output format section
   - No orphan references (every mentioned file/skill exists)
3. **Integration test** — Does it fit the ecosystem?
   - Would the Ringleader know how to sequence it?
   - Is the model/effort assignment clear?
   - Does it conflict with any existing skill's domain?

Report the eval results. Fix any issues found.

#### Phase 4: Register

After the skill is created and validated:

1. **Update the Ringleader roster** — Add the new skill to `/ringleader/SKILL.md` skill roster table
2. **Update skill-ecosystem memory** — Add to `memory/skill-ecosystem.md`
3. **Update README** — Add to the skills table in `README.md`
4. **Flywheel entry** — If applicable, note the creation in the Flywheel log so it gets tracked from day one

---

### Mode 2: Refine — Improve an Existing Skill

Invoked with `/skill-creator refine [skill-name]` or when the Flywheel flags a skill for revision.

#### Step 1: Diagnose

Read the skill's SKILL.md and any available Flywheel data:

| Signal | Source | Action |
|--------|--------|--------|
| High correction rate | Flywheel log | The skill's instructions produce wrong output — read corrections to find the gap |
| Negative sentiment | Flywheel log | Something about the output format or tone is off |
| Undertriggering | Flywheel + user report | Description field needs more trigger phrases |
| Overtriggering | User report | Description is too broad — tighten scope |
| Stale references | Skill body | File paths, skill names, or protocols have changed |
| Missing integration | Ecosystem growth | New skills exist that this skill should connect to |

#### Step 2: Propose Changes

Present changes as a diff-style summary:

```
REFINE: /[skill-name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Problem: [what's wrong, backed by data]
Evidence: [Flywheel metrics or user feedback]

Changes:
  ├─ Description: [what's changing and why]
  ├─ Body: [which sections are affected]
  └─ Integration: [new connections]

Impact: [what improves after this change]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### Step 3: Apply

After user approval:
- Edit the SKILL.md with proposed changes
- Re-run the Phase 3 eval cycle from Mode 1
- Update any downstream references (Ringleader roster, memory files)

---

### Mode 3: Optimize Descriptions — Batch Trigger Tuning

Invoked with `/skill-creator optimize` or when multiple skills show triggering issues.

#### Process

1. **Scan all skill descriptions** — Read every `skills/*/SKILL.md` frontmatter
2. **Build the trigger map** — For each skill, list what phrases trigger it
3. **Identify conflicts** — Where do two skills compete for the same trigger phrase?
4. **Identify gaps** — What common user intents have no matching skill trigger?
5. **Produce the optimization report:**

```
TRIGGER OPTIMIZATION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Conflicts (same phrase → multiple skills):
  "[phrase]" → /skill-a AND /skill-b
  Resolution: [which skill should own it]

Gaps (no skill triggers for this intent):
  "[user intent]" → no matching skill
  Candidate: /[skill-name] or NEW

Undertriggered (skill exists but description misses common phrasing):
  /[skill-name] — missing: "[phrase]", "[phrase]"

Overtriggered (description too broad):
  /[skill-name] — fires for "[phrase]" but shouldn't
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

6. **Apply fixes** — After user approval, update descriptions across the ecosystem

---

### Mode 4: Evolve — Adaptive Complexity Scaling

Invoked with `/skill-creator evolve [skill-name]` or when a skill's usage pattern suggests it has outgrown its current form.

#### When to Evolve

| Signal | Evolution |
|--------|-----------|
| Skill is always invoked with the same argument | Bake the argument into the default behavior |
| Skill output is always edited the same way after | Incorporate the edit into the skill's output format |
| Users keep adding context the skill should already know | Add a knowledge directory |
| Skill handles too many domains | Split into focused skills |
| Multiple skills always run together | Create a combined pipeline skill or Ringleader shortcut |

#### Process

1. Read the skill's history (Flywheel log, git log of SKILL.md changes)
2. Identify the evolution type from the table above
3. Propose the structural change
4. After approval, execute and re-validate

---

## Skill Complexity Guide

Not every skill needs characters, phases, and knowledge directories. Match complexity to purpose:

| Complexity | When to Use | Example |
|------------|-------------|---------|
| **Minimal** (1-2 KB) | Single-purpose tool, clear input → output | `/model-advisor`, `/preset-forge` |
| **Standard** (3-6 KB) | Multi-step workflow, structured output | `/flywheel`, `/new-xo-engine` |
| **Rich** (7-15 KB) | Domain expertise, multiple personas, knowledge base | `/producers-guild`, `/community` |
| **Orchestra** (15+ KB) | Ecosystem-wide coordination, multiple modes | `/ringleader` |

Ada defaults to **Minimal** and only adds complexity when the skill genuinely needs it. Overengineered skills are harder to maintain and slower to invoke.

## Arguments

| Argument | Values | Default |
|----------|--------|---------|
| `mode` | `create`, `refine`, `optimize`, `evolve` | `create` |
| `name` | Skill name (for create/refine/evolve) | — |
| `from-flywheel` | Include Flywheel data in analysis | `false` |

## Integration Points

| Connects To | How |
|-------------|-----|
| `/flywheel` | Flywheel identifies candidates → Skill Creator builds/refines them |
| `/ringleader` | New skills are registered in the Ringleader's roster |
| `/guru-bin` | Sister Cadence triggers skill refinement when Guru Bin protocol needs updating |
| `/architect` | Governance review for skills that affect engine workflows |
| `/sisters` | Process optimization insights feed into skill evolution |

## Values

1. **Minimal viable skill** — Start small. A 20-line skill that triggers correctly beats a 200-line skill that doesn't.
2. **Description is king** — 80% of skill quality is in the trigger description. Get that right first.
3. **Evidence over aesthetics** — Refine based on data (Flywheel logs, user corrections), not gut feeling.
4. **No orphans** — Every skill connects to the ecosystem. If it can't integrate, it shouldn't exist.
5. **Evolve, don't accumulate** — Better to improve 3 skills than create a 4th that overlaps.
