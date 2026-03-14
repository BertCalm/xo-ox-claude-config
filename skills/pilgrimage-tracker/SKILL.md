---
name: pilgrimage-tracker
description: Pilgrimage Tracker — persistent multi-session campaign tracker for XO_OX engine retreats and build journeys. Shows progress across sessions, carries context forward, tracks phase completion, and maintains the canonical state of multi-session work. Use when the user says 'pilgrimage', 'tracker', 'where are we', 'what's left', 'session progress', 'campaign status', 'retreat status', 'journey progress', 'pick up where we left off', 'continue the work', 'what did we do last time', 'remaining work', or wants to track progress across multiple sessions. Also use proactively at the start of any session that continues prior work, when a retreat or build phase completes, or when the user seems unsure of what's been done vs what remains. The memory that spans sessions.
---

# Pilgrimage Tracker

**The memory that spans sessions.**

Multi-session campaigns (engine retreats, build sprints, quality sweeps) lose context between sessions. The Pilgrimage Tracker maintains a persistent, queryable record of what's been done, what's in progress, and what remains — so every session starts where the last one ended, not from scratch.

## How It Works

### At Session Start
When a session involves continuing prior work:

1. **Read the campaign file** at `~/.claude/projects/-Users-joshuacramblet/memory/pilgrimages/` — each campaign has its own tracker file
2. **Present the status** — what phase we're in, what's done, what's next
3. **Carry forward blockers** — anything flagged as blocked in the previous session
4. **Note the session number** — "This is Session 4 of the Guru Bin Pilgrimage"

### During a Session
As work progresses:

1. **Update phase status** in real-time — mark items as in-progress, complete, or blocked
2. **Capture key decisions** — anything that changes the plan
3. **Log skill invocations** — which skills were used and what they produced
4. **Track artifacts** — files created, presets generated, code written

### At Session End
Before the session closes:

1. **Write the session summary** — what was accomplished
2. **Update the campaign file** — current phase, completion percentages, blockers
3. **Set the "next session starts here" marker** — the first thing the next session should see
4. **Flag any time-sensitive items** — things that will become stale

## Campaign File Format

Each campaign lives at `~/.claude/projects/-Users-joshuacramblet/memory/pilgrimages/{campaign-name}.md`:

```markdown
---
name: {Campaign Name}
description: {One-line description}
type: project
---

# {Campaign Name}

**Status**: {Active / Paused / Complete}
**Started**: {date}
**Sessions**: {count}
**Current Phase**: {phase name}

## Progress

| Phase | Status | Sessions | Key Artifacts |
|-------|--------|----------|---------------|
| Phase 1: {name} | COMPLETE | S1-S2 | {files, presets, etc.} |
| Phase 2: {name} | IN PROGRESS (60%) | S3-S4 | {what's done so far} |
| Phase 3: {name} | QUEUED | — | — |

## Session Log

### Session {N} — {date}
- **Duration**: ~{X} min
- **Skills used**: /skill-a, /skill-b
- **Completed**: {what got done}
- **Decisions**: {any strategic choices made}
- **Blockers**: {anything blocking progress}
- **Next**: {what Session N+1 should start with}

## Blockers
- [ ] {Anything currently blocking progress}

## Key Decisions (carried forward)
- {Decision 1}: {rationale} (Session {N})
- {Decision 2}: {rationale} (Session {N})
```

## Commands

### Starting a Campaign
When the user describes a multi-session effort:
1. Create the campaign file in `pilgrimages/`
2. Define the phases based on the scope
3. Set Phase 1 as IN PROGRESS

### Checking Status
When the user asks "where are we":
1. Read the active campaign file(s)
2. Present current phase, completion %, blockers
3. Recommend what to work on next

### Resuming
When the user says "pick up where we left off" or starts a session that clearly continues prior work:
1. Read the most recent active campaign
2. Present the "next session starts here" marker
3. Load relevant context (decisions, blockers, artifacts)

### Completing a Campaign
When all phases are done:
1. Mark status as COMPLETE
2. Write a final summary with total sessions, key artifacts, decisions
3. Archive the campaign file (keep it but mark complete)
4. Suggest follow-up work if applicable

## Multiple Campaigns

Multiple campaigns can be active simultaneously. When the user asks for status, show all active campaigns with their current phase. The Ringleader decides which campaign to work on; the Tracker just reports state.

## Integration with Other Skills

- **Ringleader**: The Tracker is the Rabbit's memory. The Ringleader plans; the Tracker remembers.
- **Guru Bin**: Retreat progress is tracked per engine — which engines have been retreated, which remain
- **Post-Engine Completion**: Completion triggers a Tracker update
- **Flywheel**: The Tracker provides usage data for skill improvement analysis
