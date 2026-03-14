---
name: flywheel
description: "The Flywheel — skill improvement engine that analyzes accumulated usage data and triggers refinement cycles. Use when: user says 'flywheel', 'improve my skills', 'skill analysis', 'what skills need work', 'optimize skills', 'skill health', or when the session log has 10+ entries for any single skill. Also invoke proactively at the start of sessions when the log shows patterns worth acting on. The always-running quality engine for the skill ecosystem."
---

# The Flywheel

Every skill invocation is a data point. The Flywheel turns those data points into skill improvements — automatically, continuously, without the user having to remember to optimize anything.

## How It Works

A hook fires after every skill invocation, capturing a lightweight signal to `~/.claude/skills/flywheel/session-log.jsonl`. The Flywheel skill reads this log and identifies patterns worth acting on.

## The Session Log

Each entry in `session-log.jsonl` is one line of JSON:

```json
{"skill": "producers-guild", "date": "2026-03-14", "context": "full platform review", "duration_signal": "long", "followed_by_correction": false, "user_sentiment": "positive", "note": ""}
```

Fields:
- `skill` — which skill was invoked
- `date` — when
- `context` — brief description of what was asked (2-5 words)
- `duration_signal` — `short` | `medium` | `long` (rough sense of how much work the skill did)
- `followed_by_correction` — did the user correct or redo something after the skill ran?
- `user_sentiment` — `positive` | `neutral` | `negative` (inferred from user's response)
- `note` — any specific feedback captured (often empty)

## Analysis Protocol

When invoked (manually or at session start when log is substantial):

### 1. Read the Log
```bash
cat ~/.claude/skills/flywheel/session-log.jsonl
```

### 2. Compute Per-Skill Health

For each skill that has 3+ entries:

| Metric | How to Compute | What It Means |
|--------|---------------|---------------|
| **Invocation count** | Count entries | How much the skill is used |
| **Correction rate** | % with `followed_by_correction: true` | How often the output needs fixing |
| **Sentiment distribution** | positive / neutral / negative ratio | User satisfaction |
| **Context diversity** | Unique contexts / total invocations | Is the skill being used for varied tasks or always the same thing? |

### 3. Identify Actions

| Pattern | Action |
|---------|--------|
| Correction rate > 30% | Flag for skill body revision — something is consistently wrong |
| Sentiment mostly negative | Read the notes, identify the root cause, propose a rewrite |
| Low invocation count but high value when used | Description may need optimization (undertriggering) |
| High invocation count + low correction | Skill is healthy — leave it alone |
| Same context every time | Skill may be too narrow — consider generalizing |
| Never invoked despite existing | Either description is wrong or skill is redundant — investigate |

### 4. Produce the Flywheel Report

```markdown
## Flywheel Report — [Date]

### Skill Health Summary
| Skill | Invocations | Correction Rate | Sentiment | Action |
|-------|------------|----------------|-----------|--------|

### Recommended Improvements
1. [Skill X] — [what's wrong, what to change, why]
2. [Skill Y] — [description optimization needed]

### Skills That Are Working
[List skills with high usage, low correction, positive sentiment — don't touch these]

### New Skill Candidates
[Patterns across the log that suggest a new skill would help — e.g., "user keeps asking for X across 3 different skills, suggesting a dedicated skill would be more efficient"]
```

### 5. Execute Improvements

For skills flagged for revision:
- Read the current SKILL.md
- Read the relevant log entries (especially the notes and correction contexts)
- Propose specific changes
- If user approves, apply changes and optionally run `/skill-creator` eval cycle

For skills flagged for description optimization:
- Collect the contexts that triggered the skill (positive examples)
- Collect contexts where the skill should have triggered but didn't (if known)
- Run the description optimization loop via `/skill-creator`

## Passive vs. Active Mode

**Passive** (default): The hook logs silently. No interruption. Data accumulates.

**Active** (when invoked): Read the log, analyze, report, propose improvements.

The user never has to think about skill quality. The Flywheel thinks about it for them.

## Log Maintenance

- Keep the last 90 days of entries (older entries lose relevance)
- If the log exceeds 500 entries, summarize old entries into `flywheel/archive/` and start fresh
- Never delete data — archive it

## Values

1. **Silent accumulation, loud improvement** — the hook is invisible; the improvement cycle is visible
2. **Evidence over intuition** — every recommendation is backed by log data
3. **Don't fix what works** — skills with high satisfaction and low correction rate are left alone
4. **The user's corrections are the most valuable signal** — when they redo something after a skill runs, that's the strongest indicator of what needs to change
