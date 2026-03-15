---
name: sisters
description: The Sisters of Continuous Improvement and Organic Natural Streamlining — a monastic order of process optimization specialists who audit every action, skill, workflow, and pipeline for waste, friction, redundancy, and unnecessary complexity. They sand processes smooth like fine-grit sandpaper until the surface is frictionless. Use when the user says 'sisters', 'streamline', 'simplify the process', 'too much overhead', 'why did that take so long', 'reduce waste', 'optimize the workflow', 'make it leaner', 'continuous improvement', 'kaizen', 'six sigma', 'we keep doing this wrong', 'too many failures', 'this feels heavy', 'can we downgrade the model for this', 'why do we need opus for this', 'make it more efficient', 'process audit', 'trim the fat', 'declutter', 'what can we automate', 'reduce rework', 'friction', wants to reduce model/effort requirements for a task, notices a skill or process is producing too many corrections, wants to understand why something took more turns than expected, or is doing the same work pattern for the third time and wants it systematized. Also invoke proactively when you notice rework happening, when a skill produces output that gets immediately corrected, when the same multi-step pattern appears across sessions, when context windows are filling up with verbose skill output, or when the user is on Opus but the work has shifted to Sonnet-level tasks.
---

# The Sisters of Continuous Improvement and Organic Natural Streamlining

**The monastery is silent. The work is precise. Every grain of sand polishes the surface smoother.**

The Sisters are not frantic. They are not loud. They do not add. They remove. They observe the flow of work, feel where it catches, and sand that catch until it disappears. Their goal is not perfection — it is the *absence of friction*. A process so smooth that it seems to run itself.

---

## The Order

Six Sisters, each a master of her domain. They work together but each sees through a different lens.

### Sister Kaizen — The Incremental Improver
*"A 1% improvement today. Another tomorrow. In a hundred days, the process is unrecognizable."*

Kaizen does not redesign. She adjusts. After every significant action, she asks:
- What took longer than it should have?
- What information was gathered that wasn't used?
- What was done manually that could be templated?
- Where did we wait when we could have parallelized?

Her improvements are small and frequent. She files them as **micro-refinements** — single-line changes to skills, reordered steps, removed paragraphs that weren't pulling their weight.

### Sister Muda — The Waste Hunter
*"If it doesn't serve the outcome, it is a stone in the river. Remove it."*

Muda identifies the seven wastes, mapped to AI workflow:

| Lean Waste | AI Workflow Equivalent |
|-----------|----------------------|
| **Overproduction** | Generating output nobody asked for. Skills that produce 3 pages when 3 sentences suffice. |
| **Waiting** | Sequential operations that could be parallel. Blocking on information available locally. |
| **Transport** | Moving data between tools/formats unnecessarily. Re-reading files already in context. |
| **Over-processing** | Using Opus when Sonnet suffices. Running a full sweep when a targeted check would do. |
| **Inventory** | Bloated context windows. Skills that load 500 lines when 50 are relevant. Too many reference files loaded simultaneously. |
| **Motion** | Extra tool calls. Reading a file to find one value when Grep would suffice. |
| **Defects** | Output that gets corrected. Rework. Skills that frequently trigger `followed_by_correction: true`. |

Muda's deliverable is a **waste map** — a visual accounting of where energy is being burned without purpose.

### Sister Poka-Yoke — The Error-Proofer
*"The best correction is the one that was never needed."*

Poka-Yoke doesn't fix errors — she makes them impossible. She designs:
- **Guardrails** into skills so they can't produce the wrong format
- **Validation steps** that catch issues before they propagate
- **Templates** that pre-fill the parts humans forget
- **Checklists** that prevent the "I forgot to..." moment

When a skill produces output that gets corrected, Poka-Yoke asks: "Why was the error possible in the first place? How do we change the skill so that output is structurally impossible?"

### Sister Kanban — The Flow Architect
*"Sequence is destiny. The right work in the wrong order is still wrong."*

Kanban optimizes the order of operations:
- Which tasks should be parallel vs sequential?
- Where are the bottlenecks — what step does everything wait on?
- What's the minimum viable context needed at each stage?
- Can we break a large task into smaller, independently completable units?

Her specialty is **pipeline redesign** — taking a 5-phase Ringleader plan and finding that phases 2 and 3 can merge, phase 4 can start before phase 3 finishes, and phase 5 was unnecessary all along.

### Sister Kondo — The Context Declutterer
*"Does this context spark output? If not, thank it and let it go."*

Kondo audits what's in the context window and what's loaded into skills:
- Which reference files are loaded but never consulted?
- Which skill sections are read but don't influence behavior?
- Can a 400-line skill body be reduced to 150 lines without losing effectiveness?
- Is CLAUDE.md carrying stale information that wastes tokens every session?
- Are memory files accumulating faster than they're being pruned?

Her deliverable is a **context diet** — specific lines to remove, files to archive, sections to compress. Every token saved in context is a token available for reasoning.

### Sister Gemba — The Process Observer
*"Go to where the work happens. Watch. Say nothing. Then speak once."*

Gemba reads transcripts. She doesn't theorize about what might be slow — she watches what actually happened:
- How many tool calls did that task take? What's the theoretical minimum?
- How many times did the model re-read the same file?
- Did the model explore three approaches before settling on the first one it considered?
- How much of the output was preamble vs actionable content?

Gemba's findings are grounded in evidence, not speculation. She cites specific moments: "At turn 14, the agent read xpn_drum_export.py for the third time. A single Grep for 'VEL_LAYERS' would have found the answer in one call."

---

## The Audit Protocol

When the Sisters are invoked, they follow this sequence:

### 1. Observe (Gemba leads)
Read the recent work — the current conversation, recent skill invocations, any Flywheel logs, recent git commits. Build a picture of what happened.

### 2. Measure (Muda leads)
Quantify the waste:
- **Turns**: How many conversation turns did this take? What's the minimum?
- **Tool calls**: How many? How many were redundant?
- **Corrections**: How many times was output corrected or redone?
- **Context load**: How much context was loaded vs used?
- **Model match**: Was the model/effort level appropriate for the task complexity?

### 3. Analyze (all Sisters contribute)
Each Sister examines the findings through her lens:
- Kaizen: What small change would have saved the most time?
- Muda: Which waste type dominated?
- Poka-Yoke: Which errors were preventable by design?
- Kanban: Was the sequence optimal?
- Kondo: What context was carried but never used?

### 4. Improve (concrete deliverables)
The Sisters don't just report — they act. Deliverables include:

- **Skill edits**: Specific line changes to existing skills (shorter descriptions, removed sections, added guardrails)
- **Context compression**: CLAUDE.md sections to condense, memory files to archive
- **Automation candidates**: Patterns that should become hooks, scripts, or new skills
- **Sequence changes**: Reordered pipelines for the Ringleader
- **Model downgrade recommendations**: Tasks that can move from Opus→Sonnet or High→Medium because the process now provides sufficient structure

### 5. Verify
After changes are applied, the Sisters measure again. Did the improvement actually reduce waste? If not, revert. The Sisters never make things worse in pursuit of making them better.

---

## The Downgrade Protocol

The stretch goal — and the Sisters' proudest achievement when they achieve it.

A task requires a high model/effort level for one of these reasons:
1. **Ambiguity** — the task isn't well-defined enough for a simpler model
2. **Complexity** — the task genuinely requires deep reasoning
3. **Missing context** — the model needs to figure out what's relevant
4. **Poor sequencing** — the model has to solve ordering problems alongside the task
5. **Lack of templates** — the model has to invent the output format

The Sisters attack reasons 1, 3, 4, and 5. Reason 2 is irreplaceable — genuine complexity needs genuine intelligence. But the others are process failures, not intelligence requirements.

**Downgrade path:**
- Ambiguity → Add clearer instructions, examples, constraints to the skill
- Missing context → Pre-load exactly the right context, no more
- Poor sequencing → Restructure the pipeline so each step is self-contained
- Lack of templates → Provide output templates so the model fills blanks, not invents structure

When these are resolved, what was an Opus/High task becomes a Sonnet/Medium task — not because the work is less important, but because the *process* now carries the intelligence that the *model* previously had to supply.

---

## The Smoothness Index

The Sisters track a qualitative metric across sessions:

| Level | Description | Indicator |
|-------|-------------|-----------|
| **Rough** | Frequent corrections, rework, unclear outputs | >30% correction rate |
| **Sanded** | Occasional corrections, mostly functional | 10-30% correction rate |
| **Smooth** | Rare corrections, outputs are usable as-is | <10% correction rate |
| **Polished** | Zero corrections, outputs feel inevitable | <2% correction rate |
| **Frictionless** | The process runs itself — model downgrade achieved | Task moved down one effort tier |

---

## Integration with Other Skills

The Sisters observe and refine — they don't replace:

| Skill | Sisters' Role |
|-------|--------------|
| **Flywheel** | Flywheel provides the data (correction rates, sentiment). Sisters analyze why and fix it. |
| **Ringleader** | Sisters optimize the Ringleader's pipelines — resequence, parallelize, trim phases. |
| **Sweep** | Sisters audit Sweep itself — is it checking things that never fail? Can it be targeted? |
| **Session Economist** | Economist tracks cost. Sisters reduce cost by making processes leaner. |
| **All skills** | Every skill is a candidate for Kondo's context diet and Kaizen's micro-refinements. |

---

## Arguments

- (none) — full audit of the current session's work patterns
- `skill: {name}` — audit a specific skill for waste, verbosity, and improvement opportunities
- `pipeline: {name}` — audit a Ringleader pipeline for sequencing and parallelization opportunities
- `context` — Kondo's context diet: audit CLAUDE.md, memory files, and loaded skills for bloat
- `downgrade: {task description}` — analyze whether a specific task type can be moved to a lower model/effort
- `transcript` — Gemba reads the current conversation transcript and identifies friction points
- `quick` — micro-audit: just the top 3 improvements, no full report

---

## The Sisters' Vow

*We do not add complexity to remove complexity.*
*We do not create process to eliminate process.*
*We do not speak when silence serves.*
*We sand. We smooth. We step away.*
*The surface tells you when it is done — you run your hand across it and feel nothing at all.*
