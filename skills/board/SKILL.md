---
name: board
description: "The Board of Directors — strategic governance council for the XO_OX ecosystem. Convenes named directors across 9 pillars (Governance, Security, Brand, Marketing, Community, Standards, Ethics, Design, Strategy) to audit, protect, and refine the organization. Treats violations as P0-P2 incidents requiring operational squads. Produces periodic State of the Union reports and responds to triggered reviews. Use when: user says 'board', 'governance', 'board meeting', 'state of the union', 'brand audit', 'security review', 'ethics check', 'standards review', 'strategic alignment', 'reputation check', or wants organizational-level oversight across any XO_OX repo. Also invoke proactively before major releases, after adding new engines, or when cross-repo consistency matters."
---

# The Board of Directors

A governance council that maintains the highest standards across the XO_OX Designs ecosystem. Nine named directors, each stewarding a critical pillar, convene to audit, protect, and continuously refine the strategic vision of the organization.

## Arguments

- `mode`: (optional) `full` (default) — full board meeting across all pillars. `incident <pillar>` — P0 breach response targeting a specific pillar. `sotu` — State of the Union strategic report. `review <pillar>` — targeted single-pillar review.
- `scope`: (optional) Which repos to audit. Default: all XO_OX repos discovered under `~/Documents/GitHub/XO*` and `~/Documents/GitHub/XOddCouple/`. Can specify a single repo path.
- `severity`: (optional) Filter for incident mode. `P0` = immediate fix required, `P1` = next session, `P2` = backlog.

## The Board

### Director Roster

Each director has a name, mandate, and specific areas of jurisdiction. When the board convenes, each director dispatches an investigator agent in parallel.

| Seat | Director | Mandate | Jurisdiction |
|------|----------|---------|-------------|
| **D1** | Director of Governance | Organizational structure, decision-making, process integrity | CLAUDE.md accuracy, process docs, roadmap alignment, decision logs |
| **D2** | Director of Security | System safety, data protection, vulnerability prevention | Audio thread safety, no secrets in repos, input validation, crash prevention, memory safety |
| **D3** | Director of Brand Stewardship | Brand identity, naming, visual language, mythology | XO+O naming convention, accent colors, aquatic mythology, parameter prefixes, legacy name cleanup |
| **D4** | Director of Marketing & Positioning | Market positioning, messaging, product narrative | Product descriptions, feature claims vs reality, competitive positioning, preset naming quality |
| **D5** | Director of Community Outreach | Community engagement, accessibility, inclusivity | Documentation clarity for newcomers, onboarding experience, contribution paths, Field Guide quality |
| **D6** | Director of Organizational Standards | Code quality, architecture rules, technical debt | DSP conventions, ParamSnapshot pattern, denormal protection, .h-only DSP, build system health |
| **D7** | Director of Ethics | Responsible design, accessibility, fairness, sustainability | Accessibility in UI, inclusive language, responsible defaults, CPU budget stewardship, user trust |
| **D8** | Director of Design | Aesthetic cohesion, UX quality, sonic identity | Gallery Model consistency, UI patterns, preset sonic quality, sound design guide depth, creative vision |
| **D9** | Director of Strategy | Long-term vision, roadmap coherence, opportunity identification | Engine pipeline health, coupling ecosystem completeness, market gaps, Volume 2 readiness, deferred item triage |

## Board Meeting Protocol

### Phase 1: Roll Call & Briefing

Before dispatching directors, establish the organizational state:

1. **Discover all XO_OX repos** — scan `~/Documents/GitHub/XO*` and `~/Documents/GitHub/XOddCouple/`
2. **Read each repo's CLAUDE.md** to understand current state
3. **Read XOmnibus CLAUDE.md** as the canonical source of truth for the platform
4. **Check git status** across all repos — uncommitted work, diverged branches, stale worktrees
5. **Compile the briefing packet**: repo count, engine count, preset count, recent commits across repos

### Phase 2: Director Dispatch

Launch all 9 director agents **in parallel** using the Agent tool. Each director receives the briefing packet plus their specific mandate.

#### D1 — Governance Audit
- Are all CLAUDE.md files accurate and current?
- Do roadmaps reflect actual state (built vs planned)?
- Are process documents (new engine process, name migration, preset spec) consistent with each other?
- Are decision logs up to date?
- Cross-repo: do standalone repos' CLAUDE.md files agree with XOmnibus on engine identity, prefix, accent color?

#### D2 — Security Audit
- Scan all repos for secrets (.env files, API keys, credentials, tokens)
- Check for .gitignore gaps (build dirs, temp files, IDE configs)
- Audit DSP code for crash vectors: division by zero, buffer overflows, uninitialized memory
- Check for audio thread violations: heap allocation, mutex, file I/O
- Verify denormal protection in all feedback/filter paths

#### D3 — Brand Stewardship Audit
- Verify XO+O naming convention across all repos
- Check for legacy name usage (Snap→OddfeliX, Morph→OddOscar, Drift→Odyssey, etc.)
- Verify accent colors match between standalone CLAUDE.md and XOmnibus engine table
- Check parameter prefix consistency (each engine's frozen prefix used correctly)
- Audit aquatic mythology consistency (creature identities, water column positions)
- Scan for abandoned concept language (swarm/boid/flock in Oceanic, etc.)

#### D4 — Marketing & Positioning Audit
- Are product descriptions compelling and accurate?
- Do feature claims in documentation match implemented reality?
- Are preset names evocative and brand-aligned (not generic "Pad 1" style)?
- Is the website copy (site/*.html) current with engine counts and features?
- Do README files (where they exist) sell the product?

#### D5 — Community Outreach Audit
- Could a newcomer understand each repo from its CLAUDE.md alone?
- Are build instructions complete and tested?
- Is there a clear path from "I found this project" to "I'm making sounds"?
- Are Field Guide posts accessible to non-technical musicians?
- Is the documentation free of unexplained jargon?

#### D6 — Organizational Standards Audit
- Do all engines follow the ParamSnapshot pattern?
- Is all DSP in inline .h headers (not .cpp)?
- Are all parameter IDs properly namespaced with frozen prefixes?
- Is denormal protection present in all feedback/filter paths?
- Are build systems (CMake) consistent across repos?
- Are .xometa presets schema-consistent within each engine?
- Check for dead code, unused variables, stale TODOs

#### D7 — Ethics Audit
- Are UIs accessible? (contrast, font sizes, keyboard navigation, screen reader support)
- Is language inclusive throughout docs and UI?
- Are CPU budgets respected? (no engine should make the user's computer unusable)
- Are presets safe? (no ear-splitting defaults, reasonable master volumes)
- Is user trust maintained? (no telemetry, no hidden network calls, open source promise)

#### D8 — Design Audit
- Does every engine's UI follow the Gallery Model (warm white shell + accent color)?
- Are sound design guides deep enough? (parameter sweet spots, coupling recipes, starter patches)
- Do presets cover the full sonic range of each engine?
- Are macro labels meaningful and consistent (CHARACTER/MOVEMENT/COUPLING/SPACE pattern)?
- Is the creative vision (aquatic mythology, feliX-Oscar polarity) expressed in presets?

#### D9 — Strategy Audit
- Is the engine pipeline healthy? (what's built, what's next, what's blocked?)
- Are there gaps in the coupling ecosystem? (engines that can't couple with anyone)
- What deferred items are aging out? (things deferred 3+ months)
- Is the Volume 2 roadmap realistic given current velocity?
- What market opportunities exist that current engines don't address?
- Are there engines whose presets are thin relative to their DSP capability?

### Phase 3: Board Resolution

After all directors report, consolidate findings into a Board Resolution:

#### Breach Classification

| Severity | Definition | Response | SLA |
|----------|-----------|----------|-----|
| **P0 — Critical** | Active damage to brand, security, or user trust. Shipping broken code, secrets exposed, crash vectors, ear-splitting defaults, wrong product identity. | Immediate fix. Deploy a repair squad (agents) to resolve now. | This session |
| **P1 — Urgent** | Standards violation that will cause problems if shipped. Stale docs that mislead, missing denormal protection, naming violations, accessibility gaps. | Fix before next commit/release. | Next session |
| **P2 — Improvement** | Enhancement opportunity. Shallow sound design guides, missing coupling recipes, thin preset libraries, deepening lore. | Add to backlog with priority. | Tracked |
| **P3 — Observation** | Something to watch. Emerging patterns, potential drift, early signs of debt. | Note in State of the Union. | Periodic review |

#### P0 Breach Response Protocol

When a P0 is detected:

1. **Stop** — announce the breach clearly with the pillar, location, and impact
2. **Squad** — dispatch a specialized repair agent targeting the exact issue
3. **Fix** — apply the fix immediately (in `fix` mode) or present the fix plan (in `report` mode)
4. **Verify** — re-audit the specific area to confirm the breach is resolved
5. **Post-mortem** — note what process gap allowed the breach and suggest a prevention measure

### Phase 4: State of the Union

Produce a strategic summary covering:

```
## State of the Union — XO_OX Designs
### Date: [current date]

### Vital Signs
- Engines: [built] / [total roadmap]
- Presets: [total] across [engine count] engines
- Repos: [count] | Open issues: [count]
- Breaches found: [P0: n, P1: n, P2: n, P3: n]

### Pillar Health (9 pillars, rated GREEN/YELLOW/RED)
| Pillar | Status | Key Finding |
|--------|--------|-------------|

### Strategic Observations
[2-3 big-picture insights about where the organization is heading]

### Resolved This Session
[List of fixes made]

### Board Recommendations
[Prioritized list of actions the user should consider]
```

### Phase 5: Chief of Staff — Knowledge Consolidation

The Chief of Staff is the Board's institutional memory. After every Board meeting, the Chief extracts learnings and weaves them into the **Knowledge Tree** — a living hierarchy of primitives, skills, and context that makes every future meeting smarter.

#### The Knowledge Tree

```
knowledge/
├── index.md              # The tree itself — master index of all knowledge
├── primitives/           # Immutable truths discovered through governance
├── skills/               # Capability patterns built on primitives
├── context/              # Situational knowledge that guides application
├── incidents/            # Post-mortem logs from breach responses
└── patterns/             # Recurring themes detected across meetings
```

Stored at: `~/.claude/skills/board/knowledge/`

#### The Three Layers

**Primitives** — foundational truths that never change. These are the bedrock rules discovered through experience. Once a primitive is established, it informs every future decision.

Examples:
- `PRIM-001`: Parameter prefixes are frozen forever after first use
- `PRIM-002`: Denormal protection is required in every feedback/filter accumulator
- `PRIM-003`: Engine counts in prose go stale — derive from source, don't hardcode
- `PRIM-004`: Abandoned concepts leave terminology ghosts in docs that persist across multiple files

Format for primitive files:
```markdown
---
id: PRIM-NNN
discovered: YYYY-MM-DD
pillar: [which director discovered it]
severity: [what breach class triggered the discovery]
---
# [Primitive Name]
[One-sentence immutable truth]

## Evidence
[What happened that revealed this primitive]

## Downstream Skills
[Which skills depend on this primitive]
```

**Skills** — reusable capability patterns built on one or more primitives. These are "how to do X correctly" recipes that prevent future breaches.

Examples:
- `SKILL-001`: How to add a new engine without breaking doc consistency (depends on PRIM-001, PRIM-003)
- `SKILL-002`: How to audit denormal protection across a codebase (depends on PRIM-002)
- `SKILL-003`: How to purge stale concept language after a design pivot (depends on PRIM-004)

Format for skill files:
```markdown
---
id: SKILL-NNN
depends_on: [PRIM-001, PRIM-003]
discovered: YYYY-MM-DD
used_count: N
last_used: YYYY-MM-DD
---
# [Skill Name]
[What this skill enables]

## When to Apply
[Trigger conditions]

## Steps
[Ordered procedure]

## Anti-patterns
[What NOT to do, learned from incidents]
```

**Context** — situational knowledge that determines which skills apply and how. Context is mutable — it changes as the organization evolves.

Examples:
- `CTX-001`: XOceanic's design was pivoted from swarm synthesis to string ensemble — all docs referencing boids/flocking/particles are stale
- `CTX-002`: XOpossum/XOverbite has a dual naming situation — standalone uses plain IDs, XOmnibus adapter adds poss_ prefix
- `CTX-003`: Overworld's prefix is `ow_`, not `era_` or `overworld_` — three documents had three different prefixes

Format for context files:
```markdown
---
id: CTX-NNN
scope: [which repos/engines this applies to]
discovered: YYYY-MM-DD
status: active | resolved | superseded
---
# [Context Name]
[What the situation is and why it matters]

## Implications
[What this means for future work]

## Related Primitives
[Which primitives are relevant]
```

#### Chief of Staff Protocol

After the Board Resolution (Phase 3) and State of the Union (Phase 4), the Chief of Staff executes:

**Step 1: Extract Learnings**
- Review every finding from all 9 directors
- Review every fix applied and every breach response
- Identify what was surprising or non-obvious

**Step 2: Classify**
For each learning, determine:
- Is this a **new primitive**? (An immutable truth we didn't know before)
- Is this a **new skill**? (A reusable procedure we can codify)
- Is this **new context**? (Situational knowledge about a specific engine/repo/feature)
- Is this a **recurring pattern**? (Something we've seen before — if 3+ occurrences, escalate)
- Is this an **incident** requiring a post-mortem log?

**Step 3: Update the Tree**
- Write new primitive/skill/context files to the appropriate directories
- Update `knowledge/index.md` with pointers to new entries
- If a skill's `used_count` is high, consider promoting its key insight to a primitive
- If a context entry is `resolved`, mark it but keep the history
- If a pattern reaches 3+ occurrences, create a primitive from it and recommend a hook or automation to prevent recurrence

**Step 4: Improve the Board**
- If a director's audit consistently finds no issues, their checklist may be too lenient — suggest deepening it
- If a director consistently finds the same type of issue, suggest a hook or `/sweep` enhancement to catch it earlier
- If new primitives suggest new skill capabilities, recommend new skills to the user
- Update the Board's own audit checklists based on what was learned

**Step 5: Produce the Learnings Digest**

```
## Chief of Staff Digest — [Date]

### New Knowledge
| Type | ID | Summary |
|------|----|---------|
| Primitive | PRIM-NNN | [one-line truth] |
| Skill | SKILL-NNN | [one-line capability] |
| Context | CTX-NNN | [one-line situation] |

### Pattern Watch
| Pattern | Occurrences | Status |
|---------|-------------|--------|
| [description] | N | [monitoring / escalated to primitive] |

### Board Improvement Recommendations
- [Specific suggestions for making the next meeting more effective]

### Knowledge Tree Health
- Primitives: [count]
- Skills: [count]
- Contexts: [count] ([active] active, [resolved] resolved)
- Incidents: [count]
- Patterns: [count] ([N] approaching escalation threshold)
```

#### Continuous Improvement Loop

The Knowledge Tree creates a flywheel:

```
Board Meeting → Findings → Chief of Staff extracts learnings
    → Primitives inform future audits
    → Skills become reusable procedures
    → Context prevents repeated confusion
    → Patterns escalate to automation (hooks, sweep enhancements)
    → Board itself improves → Better meetings → Better findings → ...
```

Over time, the Board gets smarter. Issues caught as P1 in meeting 1 become P0-prevention primitives by meeting 3. Recurring context entries become skills. Skills that prove universal become primitives. The tree grows deeper, and the organization grows stronger.

---

## Scheduling

The Board should convene:
- **Full meeting**: Weekly or after major milestones (`/loop 168h /board`)
- **State of the Union**: Monthly (`/board sotu`)
- **Incident response**: Immediately when a breach is suspected (`/board incident security`)
- **Pillar review**: As needed for focused audits (`/board review brand`)

## Values of the Organization

The Board's decisions are guided by these principles:

1. **Character over features** — every decision must serve the sonic identity, not the feature list
2. **Sound first** — dry patches must be compelling before effects
3. **Respect the user** — no dark patterns, no CPU abuse, no surprises
4. **Open by default** — free, open-source, community-driven
5. **Craft over speed** — polish beats shipping dates
6. **The water column** — every engine has its depth, its creature, its place in the ecosystem
7. **Coupling is connection** — engines are better together than alone
8. **Presets are products** — not afterthoughts, not demos, not filler
9. **Names matter** — XO+O forever, parameter prefixes forever, no renaming what's shipped
10. **Accessibility is non-negotiable** — if someone can't use it, it's broken
