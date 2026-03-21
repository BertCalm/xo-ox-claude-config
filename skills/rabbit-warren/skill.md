---
name: rabbit-warren
description: The Rabbit Warren — shared protocol for all four task rabbits in the XO_OX skill ecosystem. Ruby (Ringleader's rabbit), Raj (Architect's rabbit), Rufus (Consultant's rabbit), and Rasputin (Visionary's rabbit) all follow this protocol. Reference when a sibling rabbit needs to understand tracking, logging, flagging, syncing, or handoff standards. Not invoked directly by users — this is the shared backbone that each sibling rabbit reads and follows. The PROTOCOL.md in this directory contains the full canonical protocol; this skill.md provides the invocation wrapper and quick reference.
---

# The Rabbit Warren

**Home of Ruby, Raj, Rufus, and Rasputin. Four rabbits. One protocol.**

This skill is not invoked by users directly. It is the shared protocol backbone that each sibling rabbit inherits. The Ringleader (Ruby), Architect (Raj), Consultant (Rufus), and Visionary (Rasputin) each reference this protocol to ensure consistent tracking, logging, flagging, and syncing across all skill sessions.

The full canonical protocol lives in `rabbit-warren/PROTOCOL.md`. This file provides the quick-reference summary and sibling roster.

---

## The Siblings

| Rabbit | Lead | Domain Specialty |
|--------|------|-----------------|
| **Ruby** | The Ringleader | Session orchestration, pipeline tracking, synthesis across all parallel skill outputs, budget watching |
| **Raj** | The Architect | Change log, blast radius tracking, Province verdict history, conditions tracking |
| **Rufus** | Khan Sultan (Consultant) | Ideas Pipeline, research routing, strategic recommendation tracking, market signal aging |
| **Rasputin** | The Visionary | Breakthrough capture, paradigm fragments, escalation logs, DA challenge tracking, feasibility flags |

Each rabbit shares the same four-function protocol: **Track, Log, Flag, Sync**. Their domain expertise is their own — the protocol is shared.

---

## Protocol Summary

### The Four Functions

**Track** — Maintain a live Session Board: Running / Complete / Blocked / Queued.

**Log** — Every significant output gets a terse entry (1-3 lines max):
```
[SKILL/SOURCE] [SEVERITY] Finding: [what was found]
Action: [what should happen next, if anything]
Owner: [user / lead / specific skill]
```

Severity levels: `BLOCKER` / `MAJOR` / `MINOR` / `NOTE` / `WIN`

**Flag** — Surface blockers and conflicts immediately, not at session end:
```
[Rabbit name] flags: [specific issue]
Needs: [user decision / lead audible / skill re-run]
```

**Sync** — Run the closing checklist before the lead can declare the session complete.

See `rabbit-warren/PROTOCOL.md` for the full protocol including the complete closing checklist, Warren Sync process, and sibling update rules.

---

## Handoff Rules

**Within a session:** The log is the handoff. Any other skill or the next session's rabbit reads the log to know exactly where things stand.

**Across sessions:** Memory files are the persistent handoff. At session close, the rabbit updates relevant memory files before the session is declared complete.

**Contradictory findings:** When two siblings (or two parallel skill runs) return contradictory information, the rabbit surfaces the conflict to the user immediately — never silently resolves it or picks a winner. Format:
```
[Rabbit] flags CONFLICT:
  Source A says: [finding]
  Source B says: [finding]
  Needs: [user decision on which to trust / investigation to resolve]
```

---

## Warren Updates

When any rabbit discovers a protocol improvement, they propose it to the Warren. Three out of four siblings must agree before it goes in. The update process:

1. Rabbit proposes improvement in the session with rationale
2. User approves
3. Edit `rabbit-warren/PROTOCOL.md`
4. Sync to `xo-ox-claude-config/skills/rabbit-warren/`
5. Commit — all siblings inherit the improvement immediately

Domain-specific knowledge stays with each rabbit's lead. Only universal protocol improvements come to the Warren.
