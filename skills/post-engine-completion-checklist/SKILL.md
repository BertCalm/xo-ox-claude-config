---
name: post-engine-completion-checklist
description: "Post-engine completion checklist for XO_OX synth engines — runs immediately after a build cycle, Seance, or phase completion to lock in accurate documentation before facts drift. Use ANY TIME: a user says an engine is 'done', 'complete', 'finished', 'ready to ship', 'all phases built', 'auval passes', a phase number completes (Phase 4, Phase 7, etc.), after a Seance verdict is delivered, or after running /sweep or /synth-seance on a completed engine. Also invoke proactively when you notice CLAUDE.md still says 'Phase 0' but the repo has substantial source code. This is the documentation lock-in step that prevents PRIM-005 drift — without it, every 'complete' engine accumulates stale facts within days."
---

# Post-Engine Completion Checklist

Documentation decays the moment a build cycle ends. This skill exists because of PRIM-005: status fields — gallery codes, preset counts, phase markers, source file counts, accent colors — drift within days of project completion. The Historical Society finds these errors every run. This checklist prevents them at the source.

Run this immediately after: a phase is declared complete, auval passes, a Seance verdict is delivered, or the user says the engine is done.

## What to Audit

You have access to the engine's repo. Read the actual files — don't infer from memory or prior conversation.

### 1. CLAUDE.md Accuracy Pass

Read the engine's CLAUDE.md (at repo root) and verify every factual claim:

**Status marker**
- Does it say COMPLETE / ALL PHASES BUILT / BUILD COMPLETE? Update if not.
- If partially done (e.g. "Phase 4 complete, Phase 5 pending"), is the phase description accurate?

**Gallery code & accent color**
- Check the standalone CLAUDE.md header vs `~/Documents/GitHub/XO_OX-XOmnibus/CLAUDE.md` (search for the engine name in the XOmnibus list)
- Gallery code must match XOmnibus canonical name (e.g. OVERDUB not DUB, ODYSSEY not DRIFT, OVERBITE not BITE)
- Accent hex color must match XOmnibus master spec
- If inconsistent: XOmnibus CLAUDE.md wins. Update the standalone.

**Preset count**
- If the engine has a standalone Presets/ directory: count actual .xometa files (`find . -name "*.xometa" | wc -l`)
- If presets live only in XOmnibus: note that explicitly ("N presets in XOmnibus [ENGINE] category — standalone Presets/ not used")
- Never state a hardcoded count without noting where it was verified (PRIM-003)

**Source file count**
- Preferred: don't hardcode it. Use a note like "see Source/ — N+ files at last count"
- If hardcoded: verify with `find src/ Source/ -name "*.h" -o -name "*.cpp" | wc -l` and update
- If count is stale by >20%, update it

**Build command**
- Is it the single-line `cmake -B build -G Ninja ... && cmake --build build` form?
- Does it match CMakeLists.txt target?

**Seance verdict**
- If a Seance has been run: is the score and key verdict recorded?
- If no Seance: note "Seance pending" so future sessions know to schedule it

**Dead references**
- Scan for any referenced file paths (spec docs, design docs) — do they exist?
- Remove or update dead references

### 2. XOmnibus Sync (if engine is integrated)

Read `~/Documents/GitHub/XO_OX-XOmnibus/CLAUDE.md` for this engine's entry:

- Gallery code matches standalone CLAUDE.md (after your fix above)
- Accent color matches
- Engine is listed in the 9/24/26-engine count (update the count if needed)
- Adapter file exists if required (e.g. XOpossumAdapter.h)
- If adapter is missing: flag it explicitly — "XOmnibus integration incomplete: [Engine]Adapter.h not yet written"

### 3. Knowledge Compendium

Navigate to `synth_playbook/agent_knowledge/` in the engine repo. For each standard file:

| File | Minimum standard |
|------|-----------------|
| `preset_design_patterns.md` | Not a stub. Covers: category system, feature showcase progression, macro strategies, naming conventions, playability defaults |
| `architecture_patterns.md` | Not a stub. Covers: signal flow, key design decisions, voice engine pattern, parameter layout rationale |
| `dsp_techniques.md` | Covers: key DSP innovations for this engine, what makes it sound unique, pitfalls discovered |
| `coupling_patterns.md` | Covers: this engine's coupling roles (source/destination), which coupling types it excels at |

If any file is a stub (under 500 bytes or contains only template headers):
- Pull from: CLAUDE.md architecture section, any docs/ files, commit history summaries, and this conversation's context
- Write real content. A stub is worse than no file — it signals completion that isn't there.

### 4. Memory & Satellite File

Check `~/.claude/projects/-Users-joshuacramblet/memory/`:

**MEMORY.md** (index file):
- Is this engine mentioned?
- Is the status accurate? (COMPLETE, in progress, etc.)
- Does the entry point to a satellite file if the engine is significant?
- Is MEMORY.md under 200 lines? (trim if needed — move content to satellite)

**Satellite file** (recommended for any engine with >5 phases or >100 presets):
- Filename pattern: `[engine-name]-engine.md` (e.g. `xoverdub-engine.md`)
- Contents: identity, architecture summary, build command, completion notes, key docs, known deferred items
- Use the frontmatter format:
```markdown
---
name: [engine]-engine
description: [Engine] synth engine — architecture, build, and completion notes
type: project
---
```

### 5. Playbook Protocol Log

Check `synth_playbook/` for a protocol log or completion matrix:
- Are protocols marked complete? (Full Instrument Dev Cycle, DSP Stability, Preset Expansion, etc.)
- If incomplete protocols exist: flag them. Don't silently drop them.

---

## Output Format

After the audit, report:

```
## Post-Completion Checklist — [Engine Name]
**Audited**: [date]
**Build status**: [COMPLETE / Phase N complete]

### Fixed
| Item | Old | New |
|------|-----|-----|
...

### Flagged (needs action)
| Item | Issue | Recommended action |
|------|-------|-------------------|
...

### Knowledge Compendium
| File | Status | Action taken |
|------|--------|-------------|
...

### Memory/Satellite
| Item | Status |
|------|--------|
...

### Clean ✓
[What checked out and required no changes]
```

Then apply all safe fixes directly (status markers, colors, counts, gallery codes). Flag anything that requires judgment or user input.

---

## Why This Matters

Every engine in the XO_OX ecosystem has the same post-completion drift pattern:
- Gallery codes stay at the development name (DRIFT, BITE, DUB) instead of canonical (ODYSSEY, OVERBITE, OVERDUB)
- Accent colors fall behind XOmnibus master spec
- Preset counts are wrong within 2 weeks
- Knowledge files stay as stubs
- Satellite memory files aren't created

The Historical Society finds these in bulk every audit. This checklist prevents accumulation at the source.
