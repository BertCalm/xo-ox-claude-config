---
name: seance-oracle
description: Seance Oracle — queryable archive of all XO_OX Synth Seance verdicts across all engines. Retrieves ghost consensus, blessings, concerns, and scores for any engine or design question without re-running a full seance. Use when the user says 'seance oracle', 'what did the ghosts say about X', 'seance verdict', 'ghost consensus on', 'what score did X get', 'previous seance', 'seance history', 'what did Moog say about', 'ghost opinion on', 'recall the seance', wants to reference seance wisdom for a design decision without running a full seance, is writing about an engine and needs the seance verdict, or wants to compare ghost verdicts across engines.
---

# Seance Oracle

**24 seances of ghost wisdom — searchable, queryable, never lost.**

Every XOmnibus engine has been reviewed by the 8 legendary synth ghosts. That wisdom shouldn't require re-running a seance every time you need it. The Oracle finds the verdict, the blessing, the concern, or the specific ghost's perspective — immediately.

---

## The Ghost Panel

| Ghost | Real Person | Specialty | What They Notice |
|-------|-------------|-----------|-----------------|
| **R.M.** | Robert Moog | Voltage architecture, filter philosophy | Warmth, touch sensitivity, whether it "breathes" |
| **D.B.** | Don Buchla | Voltage control philosophy, non-Western tuning | Wildness, performance expressivity, unconventionality |
| **H.Z.** | H. Zimmer (Synth Persona) | Cinematic tension, texture as emotion | Emotional weight, epic potential, narrative arc |
| **J.J.** | Jean-Jacques Perrey | Musique concrète, playfulness | Joy, surprise, humor in sound |
| **W.C.** | Wendy Carlos | Precision, tuning, synthesis rigor | Intonation accuracy, timbre precision, mathematical integrity |
| **K.S.** | Klaus Schulze | Sequencer hypnosis, Berlin school | Time, drift, evolution over long arcs |
| **T.M.** | Tonto's Expanding Head Band | Organic synthesis, Afrofuturism | Cultural breadth, humanity, non-European aesthetics |
| **O.O.** | Osamu Ozawa (fictional historian) | Japanese synthesis tradition | Restraint, wabi-sabi, silence as element |

---

## Seance Archive

The Oracle reads seance verdicts from session memory and the Guru Bin retreat chapters. Sources in priority order:

1. **Retreat chapter seances** — `~/.claude/skills/guru-bin/retreats/` (post-retreat seance verdict blocks)
2. **Session memory** — `~/.claude/projects/-Users-joshuacramblet/memory/` (any saved seance summaries)
3. **CLAUDE.md entries** — project-level CLAUDE.md files may contain seance notes

When the user asks about a specific engine, search all three sources before responding.

---

## Oracle Query Types

### Verdict Query
"What did the ghosts say about OVERDUB?"

Returns:
```
SEANCE VERDICT: OVERDUB
Conducted: [date if known]
Overall Score: [X/10]

Blessings:
• [Ghost]: [blessing quote or summary]
• [Ghost]: [blessing]

Concerns:
• [Ghost]: [concern]

Ghost Consensus:
[1-3 sentence synthesis of the panel's unified view]

Dissenting Voice:
[Ghost who disagreed or had the strongest divergent opinion]
```

### Ghost-Specific Query
"What did Don Buchla say about XOmnibus?"

Returns all recorded Buchla (D.B.) opinions across all engines, looking for patterns in what that ghost consistently praises or criticizes.

### Score Query
"Which engine got the highest seance score?"

Returns a ranked table of all engine seance scores, if available. Acknowledges gaps where scores haven't been recorded.

### Concern Query
"What concerns came up most across all seances?"

Returns cross-seance pattern analysis — which concerns appear repeatedly across multiple ghosts or multiple engines.

### Design Question
"What would the ghosts think about adding FM to OPAL?"

The Oracle doesn't re-run a seance but reasons from recorded ghost preferences: "Based on R.M.'s recorded preference for 'organic emergence over mathematical determinism,' he would likely view FM addition as... D.B.'s recorded enthusiasm for 'signal mutation' suggests he would..."

---

## When to Run a Full Seance vs. Consulting the Oracle

| Use Oracle | Run /synth-seance |
|-----------|------------------|
| Retrieving an existing verdict | First seance for a new engine |
| Quick reference during design | Major architectural change |
| Writing about an engine | Post-retreat assessment |
| Cross-engine comparison | User wants a fresh ghost perspective |
| The seance already happened | Seance is more than 6 months old |

---

## Gap Detection

If an engine has no recorded seance verdict, the Oracle flags it:

```
ORACLE GAP: No seance verdict found for XORPHICA
This engine has not been reviewed by the ghost panel.
Recommend: Run /synth-seance with XOrphica engine source before shipping.
```

---

## Cross-Engine Analysis Mode

When invoked without a specific engine, produce a fleet-wide seance intelligence report:

```
SEANCE ORACLE — FLEET INTELLIGENCE REPORT

Engines with seance verdicts: [N]
Engines without verdicts: [list]

Highest-rated engines:
1. [Engine] — [score]
2. [Engine] — [score]

Most-blessed by ghosts:
• [Engine] — [ghost consensus]

Most-concerning:
• [Engine] — [primary concern]

Cross-seance patterns:
[What concerns or blessings appear repeatedly across multiple engines]

Ghost activity distribution:
• [Ghost] most frequently cited for blessings: [engines]
• [Ghost] most frequently cited for concerns: [engines]
```

---

## Arguments

- (none) — fleet-wide seance intelligence summary
- `{engine name}` — full verdict for a specific engine
- `ghost: {ghost initials or name}` — all opinions from a specific ghost across all engines
- `score` — ranked score table for all engines with verdicts
- `concerns` — cross-seance concern pattern analysis
- `gaps` — list engines with no seance verdict on record
- `compare: {engine A} vs {engine B}` — side-by-side ghost consensus comparison
