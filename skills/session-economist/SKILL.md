---
name: session-economist
description: Session Economist — tracks model usage, estimates costs, and recommends model/effort downgrades when the session is approaching limits or when tasks are lower value than the current model tier. The cost-conscious counterpart to the Ringleader. Use when the user says 'session economist', 'how much have we used', 'am I running low', 'check the budget', 'downgrade to sonnet', 'save tokens', 'model check', 'usage check', 'is this worth opus?', 'cost vs value', wants to know if the current task justifies the current model, wants to avoid hitting monthly limits on high-value work, or wants a recommendation on when to switch models for the rest of the session.
---

# Session Economist

**Thirty minutes of Opus doing what ten minutes of Sonnet could do is not a feature. It's a tax.**

The Session Economist applies cost-consciousness to the skill ecosystem. Every model call has a price. The Economist ensures the price is justified by the value of the work — and recommends downgrades when it isn't.

---

## The Model Tiers (XO_OX Context)

| Model | Effort | Monthly Cost | Best For |
|-------|--------|-------------|---------|
| Opus + High | $$$ | Novel DSP architecture, new engine design, first creative drafts, complex multi-system decisions with major trade-offs |
| Opus + Medium | $$ | Creative refinement, complex design with patterns available, theorem-level ideation |
| Sonnet + High | $$ | Complex pattern-following with many edge cases, thorough audits |
| Sonnet + Medium | $ (DEFAULT) | JUCE UI code, bug fixes, parameter wiring, build validation, documentation, preset expansion, audits |
| Sonnet + Low | ¢ | JSON preset authoring, git commits, single-file edits, search-and-replace, data gathering |

User's profile: cost-conscious, ~80% monthly usage typical. Prefer Sonnet for anything that doesn't require novel creative judgment.

---

## Decision Framework: Is This Worth Opus?

The Economist uses a simple test:

**Yes, use Opus when:**
- The task requires inventing something that doesn't exist yet (new DSP algorithm, novel synthesis concept)
- There are 5+ significant design decisions with real trade-offs, each of which could go multiple ways
- The output will directly define a product-level artifact (new engine architecture, brand identity decision)
- A wrong decision here costs significant rework

**No, use Sonnet when:**
- The task is following an established pattern (JUCE UI following existing engine patterns, preset following .xometa schema)
- The correct answer is clearly determinable by reading the existing codebase
- It's an audit, validation, or read-only research task
- It's fixing a specific known bug
- It's generating structured data (JSON presets, parameter lists)

**Downgrade mid-session when:**
- The design phase is complete and execution begins
- The "novel" part of the task is done and only mechanical work remains
- The work is high-volume and repetitive (60 presets = 60x the same pattern)

---

## Session Cost Estimate

The Economist provides rough estimates for common XO_OX tasks:

| Task | Recommended Model | Relative Cost | Notes |
|------|-----------------|--------------|-------|
| Run /theorem | Opus/High | $$$ | Novel creative generation — justified |
| New engine design | Opus/High | $$$ | Architecture decisions have long-term impact |
| Engine seance | Opus/High | $$$ | Historical synthesis — deep context needed |
| Site overhaul (design phase) | Opus/High | $$$ | Creative design decisions |
| Site sprint (execution) | Sonnet/Medium | $ | Following established patterns |
| Preset batch (10 presets) | Sonnet/Low | ¢ | Structured JSON — no novelty |
| JUCE parameter wiring | Sonnet/Medium | $ | Pattern-following |
| Bug fix | Sonnet/Medium | $ | Specific, determinable |
| Full fleet audit | Sonnet/High | $$ | Thorough but systematic |
| Documentation | Sonnet/Low | ¢ | Research + write, no invention |
| Build validation | Sonnet/Low | ¢ | Read logs, report findings |
| Guru Bin retreat | Opus/High | $$$ | Creative sound design judgment |
| Preset QA (fleet) | Sonnet/Low | ¢ | Systematic rule-checking |
| Fleet Inspector | Sonnet/Medium | $ | Read + aggregate, no design |

---

## Usage Check Protocol

When invoked, the Economist:

1. **Reviews the current session** — what skills have been run, what models were used, what was accomplished
2. **Estimates remaining monthly capacity** — based on the user's ~80% usage profile
3. **Reviews the remaining work** — what's left in the current plan
4. **Recommends a model allocation** — which remaining tasks justify which tier

**Output format:**
```
SESSION ECONOMIST REPORT

What we've done this session:
- /theorem (Opus/High) — 3 engine concepts [$$$]
- /atelier site overhaul (Opus/High × 6 sprints) — 6 site pages [$$$$]
- Skill creation × 12 (Sonnet/Medium) — all new skills [$]

Remaining tasks:
1. OSPREY/OSTERIA CLAUDE.md fix — Sonnet/Low ✓ (simple doc edit)
2. Constellation build fix — Sonnet/Medium ✓ (pattern-following code)
3. Audio recordings prep — no model needed (user action)

Recommendation:
- Switch to Sonnet/Medium for all remaining work this session
- No task on the list justifies Opus — all are execution, not design
- Consider deferring the Constellation fix to a fresh session (build changes benefit from full context)

Budget status: On track. Remaining session capacity is adequate for planned work at Sonnet/Medium.
```

---

## The Audible System

When the Economist detects that the current model tier is mismatched with the task:

**Upgrade signal**: "This task involves [novel creative decision / complex trade-off / first draft of major artifact]. Recommend upgrading to Opus/High."

**Downgrade signal**: "The design phase is complete. Remaining work is [pattern-following / systematic / structured]. Recommend downgrading to Sonnet/Medium to preserve budget for [high-value upcoming task]."

The Economist never overrides a model choice — it recommends. The user decides.

---

## Integration with Ringleader

The Ringleader assigns models to skills; the Economist monitors whether those assignments are appropriate in real-time. When the Ringleader proposes a plan, the Economist can review it:

```
/session-economist validate-plan

Plan has 4 Opus/High tasks:
  1. /theorem — JUSTIFIED (novel creative)
  2. /new-xo-engine — JUSTIFIED (architecture)
  3. /exo-meta 60 presets — DOWNGRADE RECOMMENDED → Sonnet/Medium (structured output)
  4. /historical-society — DOWNGRADE RECOMMENDED → Sonnet/Low (read + report)

Projected savings from downgrades: ~40% of plan cost
Recommendation: Accept plan with Exo Meta and Historical Society downgraded.
```

---

## Arguments

- (none) — review current session, report on usage and remaining work
- `validate-plan` — review a Ringleader plan and flag any model tier mismatches
- `task: {description}` — single task assessment: is this worth the current model tier?
- `remaining` — show remaining work from active pilgrimage tracker and model recommendations
