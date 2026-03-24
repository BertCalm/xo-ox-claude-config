---
name: flywheel
description: "The Flywheel — continuous skill improvement engine that passively observes session friction, analyzes accumulated usage signals, tracks skill maturity, and triggers refinement cycles. Combines lightweight post-session logging with real-time behavioral signal detection (redirects, confusion, abandonment, resignation, delight). Use when: user says 'flywheel', 'improve my skills', 'skill analysis', 'what skills need work', 'optimize skills', 'skill health', 'library health', 'friction analysis', 'signal detection', 'skill maturity', or when the session log has 10+ entries for any single skill. Also invoke proactively at the start of sessions when the log shows patterns worth acting on, and after any session where multiple skills were invoked. The always-running quality engine for the skill ecosystem."
---

# The Flywheel

Every skill invocation is a data point. Every user redirect is a signal. Every abandoned session is a confession. The Flywheel turns all of it into skill improvements — continuously, without the user having to remember to optimize anything.

**The user's silence is data. Premature closure is data. Frustration language is data. None of it requires the user to do anything.**

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    THE FLYWHEEL                       │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌────────────────────┐                               │
│  │ LAYER 1: OBSERVE    │  ← runs during every skill   │
│  │  (always on)        │    session automatically     │
│  │  Self-corrects when │                               │
│  │  possible, logs     │                               │
│  │  what it can't fix  │                               │
│  └──────┬─────────────┘                               │
│          │ logs signals                                │
│          ▼                                             │
│  ┌────────────────────┐                               │
│  │ LAYER 2: LOG        │  session-log.jsonl            │
│  │  (append-only)      │  (existing, expanded schema) │
│  └──────┬─────────────┘                               │
│          │ periodic analysis                           │
│          ▼                                             │
│  ┌────────────────────┐                               │
│  │ LAYER 3: ANALYZE    │  triage → propose → report   │
│  └──────┬─────────────┘                               │
│          │ human approves                              │
│          ▼                                             │
│  ┌────────────────────┐                               │
│  │ LAYER 4: IMPROVE    │  edit SKILL.md, version bump │
│  └────────────────────┘                               │
└─────────────────────────────────────────────────────┘
```

---

## Layer 1: Real-Time Observation

The observation layer engages automatically during every skill session. It is architecturally invisible to the user — no meta-commentary, no feedback requests, no behavior the user can attribute to monitoring.

### What It Does During a Session

```
User activates any skill
    │
    ▼
Observation layer engages (invisible to user)
    │
    ├──▶ Detect friction signals as they occur
    │      • Redirect language ("no, I meant...")
    │      • Confusion language ("what does that mean?")
    │      • Resignation behavior (short replies after long output)
    │      • Scope expansion mid-session (missed intake variables)
    │
    ├──▶ Self-correct when possible
    │      • Rephrase a confusing question on the fly
    │      • Adjust output verbosity if resignation signals appear
    │      • Re-anchor context if the user seems lost
    │
    ├──▶ Log signals that cannot be self-corrected
    │      • Structural issues (phase ordering, missing phases)
    │      • Intake design flaws (wrong variables, missing variables)
    │      • Output format mismatches
    │      • Patterns requiring a SKILL.md edit, not a runtime fix
    │
    └──▶ Continue session normally — user sees only the skill
```

### Self-Correction vs. Logged Signal

| Situation | Action | Example |
|-----------|--------|---------|
| User confused by a question | **Self-correct**: rephrase immediately | "Let me ask that differently..." |
| User redirects on a misunderstanding | **Self-correct**: acknowledge, course-correct | "Got it — adjusting." |
| Same question causes confusion across 3+ sessions | **Log signal**: needs SKILL.md edit | Proposal generated |
| User abandons mid-phase | **Log signal**: cannot fix a closed session | Abandonment record written |
| User's replies get shorter after long output | **Self-correct**: shorten subsequent outputs | Observation layer trims verbosity |
| Output format consistently rejected | **Log signal**: structural mismatch | Proposal generated |

---

## Layer 2: Signal Logging

Each entry in `~/.claude/skills/flywheel/session-log.jsonl` is one line of JSON.

### Expanded Schema

```json
{
  "skill": "producers-guild",
  "date": "2026-03-23",
  "context": "full platform review",
  "duration_signal": "long",
  "followed_by_correction": false,
  "user_sentiment": "positive",
  "note": "",
  "termination_type": "clean",
  "last_phase_reached": "output",
  "friction_events": [],
  "positive_signals": ["re-use"]
}
```

### Field Reference

| Field | Type | Description |
|-------|------|-------------|
| `skill` | string | Which skill was invoked |
| `date` | string | ISO date |
| `context` | string | Brief description (2-5 words) |
| `duration_signal` | `short` \| `medium` \| `long` | Rough work volume |
| `followed_by_correction` | bool | Did the user correct/redo something after? |
| `user_sentiment` | `positive` \| `neutral` \| `negative` | Inferred from user response |
| `note` | string | Specific feedback (often empty) |
| `termination_type` | `clean` \| `abandoned` \| `timeout` \| `error` | How the session ended |
| `last_phase_reached` | string | Where the skill got to |
| `friction_events` | array | Structured friction records (see taxonomy below) |
| `positive_signals` | array | `delight` \| `re-use` \| `recommendation` \| `scope-expansion-post-completion` |

**Backward compatibility**: Old entries without the new fields are valid. Analysis treats missing fields as absent, not failed.

---

## Signal Taxonomy

The agent classifies user messages during skill runs against these types. No explicit labeling by the user — inferred from language and behavior.

### Friction Signals (inferred from language)

| Signal | Detection Pattern | What It Means |
|--------|-----------------|---------------|
| **Redirect** | "no", "wait", "that's not", "I meant", "go back" | Agent misunderstood; wrong branch taken |
| **Confusion** | "what does that mean", "I don't understand", "which one" | Skill language or concept unclear |
| **Frustration** | "ugh", "why is it", "this is wrong", "come on" | Accumulated friction hitting threshold |
| **Resignation** | Very short replies after long agent output | User disengaging; going through motions |
| **Restart** | "let's start over", "forget that", "begin again" | Phase or intake fundamentally failed |
| **Clarification loop** | Same concept clarified 3+ times | Intake variable or description is broken |

### Flow Signals (inferred from behavior)

| Signal | Detection Pattern | What It Means |
|--------|-----------------|---------------|
| **Intake re-collection** | A variable answered, then re-answered | Intake question was ambiguous |
| **Phase skip request** | "skip that", "just do X", "move on" | Phase is blocking or irrelevant |
| **Phase repeat request** | "redo that", "can you do that again" | Output was wrong or incomplete |
| **Output rejection** | "that's not right", "not what I asked for" | Phase logic or output format mismatch |
| **Scope expansion** | User adds context mid-run that should have been in intake | Intake didn't capture enough upfront |

### Termination Signals (inferred from session end)

| Signal | Severity | What It Means |
|--------|----------|---------------|
| **Clean completion** | Low | Skill worked. Still capture friction events en route. |
| **Silent completion** | Medium-low | Skill finished but output may not have landed. |
| **Mid-phase abandonment** | High | Skill broke at this phase. Highest-value signal. |
| **Premature closure** | Medium | Last agent message didn't land — too long? Too complex? |
| **Frustration + completion** | High | User finished but experience was bad. They won't come back. |

### Positive Signals (also captured)

| Signal | Detection Pattern | What It Means |
|--------|-----------------|---------------|
| **Delight** | "this is great", "exactly", "perfect" | Phase or output exceeded expectations |
| **Re-use** | Same user activates same skill multiple times | Skill has become part of workflow |
| **Recommendation** | User describes sharing the skill output | High value signal |
| **Post-completion expansion** | User adds more work after clean completion | Skill built trust and appetite |

---

## Layer 3: Analysis

### When to Run

- Manually: user invokes `/flywheel`
- Proactively: at session start when log has 10+ entries for any skill
- Periodically: after every 5 sessions of any single skill

### Analysis Modes

**Mode A: Single Skill Review** — when a skill has 5+ entries since last review
```
"Review signals for producers-guild"
```

**Mode B: Cross-Skill Pattern Scan** — when multiple skills share friction types
```
"Scan for cross-skill friction patterns"
```

**Mode C: Library Health Dashboard** — periodic or on demand
```
"Show skill library health"
```

### Per-Skill Health Metrics

For each skill with 3+ entries:

| Metric | How to Compute | Action Threshold |
|--------|---------------|-----------------|
| **Invocation count** | Count entries | Low count + high value = undertriggering |
| **Correction rate** | % with `followed_by_correction: true` | > 30% = skill body revision needed |
| **Abandonment rate** | % with `termination_type: abandoned` | > 25% = critical |
| **Redirect rate** | Friction events of type `redirect` / sessions | > 2/session = intake broken |
| **Sentiment distribution** | positive / neutral / negative ratio | Mostly negative = investigate |
| **Context diversity** | Unique contexts / total invocations | Low = too narrow, consider generalizing |

### Pattern → Action Map

| Pattern | Action |
|---------|--------|
| Correction rate > 30% | Flag for skill body revision |
| Sentiment mostly negative | Read notes, identify root cause, propose rewrite |
| Low invocations but high value when used | Description optimization (undertriggering) |
| High invocations + low correction | **Healthy — leave it alone** |
| Same context every time | Too narrow — consider generalizing |
| Never invoked despite existing | Description is wrong OR skill is redundant |
| Abandonment at same phase across sessions | That phase is broken — even one repeat = review it |
| 3+ redirects on same intake variable | Rewrite that intake question |
| Resignation signals after long output | Break output into smaller confirmed steps |

### Cross-Skill Patterns

When the same friction type appears in 3+ skills at the same structural location, it's a systemic problem:

| Pattern | Location | Fix |
|---------|----------|-----|
| Confusion at intake | Across multiple skills | Shared intake conventions needed |
| Abandonment at output | Final phase across skills | Output format not matching expectation |
| "What does X mean" | Phase descriptions | Jargon in skill language; simplify |
| Resignation after long output | Any long response | Break into smaller steps |
| Scope expansion mid-session | Intake across skills | Skills need better upfront capture |

---

## Layer 4: Improvement

### Flywheel Report

When invoked, produce:

```markdown
## Flywheel Report — [Date]

### Skill Health Summary
| Skill | Uses | Correction% | Abandon% | Redirect/Session | Sentiment | Status |
|-------|------|------------|---------|-----------------|-----------|--------|

### Critical (needs immediate attention)
1. [Skill] — [what's wrong, evidence, proposed fix]

### Warning (monitor or improve)
1. [Skill] — [pattern, evidence, suggested action]

### Healthy (don't touch)
[List skills with high usage, low correction, positive sentiment]

### Maturity Updates
[Any promotion or concern recommendations — see below]

### Cross-Skill Patterns
[Systemic issues shared across multiple skills]

### New Skill Candidates
[Patterns suggesting a dedicated skill would help]
```

### Improvement Proposals

Every pattern surfaces a structured proposal. No auto-edits. Human approves.

| Pattern | Version Bump | Who Validates |
|---------|-------------|---------------|
| Wording confusion in intake (1-2 fields) | `patch` x.x.1 | User review |
| Phase logic produces wrong output | `patch` x.x.1 | User review |
| Entire phase causes abandonment | `minor` x.1.x | User review + `/skill-creator` eval |
| Core pipeline assumption is wrong | `major` x+1.x.x | User review + `/skill-creator` eval |
| Cross-skill shared pattern found | New shared convention | All affected skills |

### Executing Improvements

For skills flagged for revision:
1. Read the current SKILL.md
2. Read the relevant log entries (especially notes, friction events, correction contexts)
3. Propose specific changes with evidence
4. If user approves, apply and optionally run `/skill-creator` eval cycle

For description optimization:
- Collect contexts that triggered the skill (positive examples)
- Collect contexts where the skill should have triggered but didn't
- Run description optimization via `/skill-creator`

---

## Skill Maturity Tracking

Every skill has an implicit maturity level based on accumulated signals.

### Maturity Levels

| Level | Criteria | What It Means |
|-------|----------|---------------|
| **New** | < 3 uses | Not enough data. Observe. |
| **Beta** | 3+ uses, still showing friction | Working but rough edges |
| **Stable** | 5+ clean completions, abandon rate < 20%, correction rate < 20%, 1+ positive signal | Reliable. Core of the ecosystem. |
| **At Risk** | Was Stable, now regressing (abandon rate spiking, corrections increasing) | Something changed. Investigate. |

### Promotion Criteria (Beta → Stable)

- 5+ successful uses (clean completions)
- Abandonment rate < 20%
- Correction rate < 20%
- At least 1 positive signal (delight, re-use)
- No unresolved critical improvement proposals

### Regression Alert Triggers (Stable → At Risk)

- Abandonment rate spikes above 25%
- 3+ correction events in recent sessions
- User sentiment shifts negative

The Flywheel surfaces these as part of the report. Maturity changes are recommendations, not automatic — the user reviews and approves.

---

## Library Health Dashboard

```
┌──────────────────────────────────────────────────────────────────┐
│  🟢 guru-bin v1.0.0          8 uses   0% correction   STABLE   │
│     Abandon: 0%   Redirects: 0/session   Sentiment: positive   │
├──────────────────────────────────────────────────────────────────┤
│  🟢 producers-guild v1.0.0   3 uses   0% correction   BETA    │
│     Abandon: 0%   Redirects: 0/session   Sentiment: positive   │
├──────────────────────────────────────────────────────────────────┤
│  🟡 skill-creator v1.0.0     2 uses   50% correction  NEW     │
│     ⚠️ High correction rate — skill body or trigger eval issue  │
├──────────────────────────────────────────────────────────────────┤
│  ⚫ session-economist v1.0.0  0 uses   —              NEW      │
│     ⚠️ Never invoked — description may need optimization        │
└──────────────────────────────────────────────────────────────────┘
```

---

## Log Maintenance

- Keep the last 90 days of entries (older entries lose relevance)
- If the log exceeds 500 entries, summarize old entries into `flywheel/archive/` and start fresh
- Never delete data — archive it

---

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| `/skill-creator` | Creates and evaluates skills. Flywheel tells it WHICH skills need attention and WHY. |
| `/sisters` | Process optimization. Sisters optimize workflows; Flywheel optimizes the skills themselves. |
| `/adaptive-workflow-architect` | Designs entropy-aware architectures for new skills. Flywheel monitors whether those architectures hold up in practice. |
| `/ringleader` | Orchestrates skill pipelines. Flywheel data informs which skills the Ringleader should trust and which need caveats. |
| `/historical-society` | Documents. Flywheel surfaces when skill documentation has drifted from actual behavior. |

---

## Values

1. **Observe, don't ask** — explicit feedback forms miss the users with the most signal
2. **Silent accumulation, loud improvement** — the observation is invisible; the improvement cycle is visible
3. **Evidence over intuition** — every recommendation is backed by log data
4. **Don't fix what works** — skills with high satisfaction and low correction rate are left alone
5. **Corrections are gold** — when the user redoes something after a skill runs, that's the strongest signal
6. **Closure is a confession** — a session that ends mid-phase tells you exactly where it broke
7. **Friction compounds** — one redirect is normal; three on the same concept means the skill is broken there
8. **Cross-session patterns beat single-session noise** — one frustration might be a bad day; five at the same phase means fix it
