---
name: flywheel-log
enabled: true
event: stop
action: warn
---

**Flywheel — Log this session's skill usage before stopping.**

If any skills were invoked during this session (via the Skill tool), append one JSON line per skill invocation to `~/.claude/skills/flywheel/session-log.jsonl`.

Format per line:
```json
{"skill": "skill-name", "date": "YYYY-MM-DD", "context": "2-5 word summary", "duration_signal": "short|medium|long", "followed_by_correction": true|false, "user_sentiment": "positive|neutral|negative", "note": ""}
```

Rules:
- `followed_by_correction`: true if the user redid, corrected, or expressed dissatisfaction after the skill ran
- `user_sentiment`: infer from user's response (empty/neutral if unclear)
- `duration_signal`: short (<1 min), medium (1-10 min), long (>10 min)
- `note`: capture any specific feedback the user gave about the skill's output (leave empty if none)
- If no skills were used this session, skip logging entirely
- Do not ask the user — just log silently and then stop
