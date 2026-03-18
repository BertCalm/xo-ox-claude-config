---
name: skill-creator
description: Skill Creator — creates new skills and optimizes existing ones. For new skills: takes a goal or observed workflow pattern and produces a complete SKILL.md with correct YAML frontmatter, description optimized for trigger accuracy, and a well-structured body. For existing skills: runs a description optimization loop (tightening trigger language using positive/negative examples) or a body revision cycle (using Flywheel log data to fix what's wrong). Use when the user says 'skill creator', 'create a skill', 'new skill', 'write a skill', 'optimize a skill description', 'description optimization', 'skill description isn't triggering', 'fix the skill body', 'skill revision', 'improve skill X', 'the flywheel flagged X', wants to turn a repeated workflow pattern into a reusable skill, wants to improve a skill the Flywheel identified as underperforming, or wants to create a net-new skill for a capability gap. Also invoked by /flywheel when a skill needs description optimization or body revision, and by Sister Cadence when the Guru Bin protocol needs refinement.
---

# Skill Creator

**The factory for skills. The repair shop for broken ones.**

Skills are living documents. A skill with a perfect description fires at the right moment and never at the wrong one. A skill with a perfect body produces output that never needs correction. The Skill Creator handles both: building new skills from scratch and repairing existing ones using evidence from the Flywheel.

---

## Modes

### Mode 1: Create New Skill

When the user wants to turn a capability, workflow pattern, or repeated task into a reusable skill.

**Inputs:**
- Goal description: what should this skill do?
- Trigger contexts: when should it fire? (provide 3–10 example prompts)
- Optional: anti-trigger contexts — when should it NOT fire? (prevents over-triggering)

**Process:**

#### Step 1: Name the Skill
- Must be lowercase, hyphenated (e.g., `skill-creator`, `retreat-accelerator`)
- Must reflect the skill's primary action, not its character (characters are in the body)
- Check existing skill names to avoid collision

#### Step 2: Write the Description
The `description:` field is the skill's trigger. It must be long enough to cover all the contexts where the skill should fire, and specific enough to avoid firing in unrelated contexts.

**Description anatomy:**
```
[Skill Name] — [one-sentence what-it-does].
[Optional: who/what is doing it — the character or team].
Use when [explicit trigger phrases, comma separated].
Also use when [behavioral triggers — what the user is doing, not just what they say].
Also invoke [proactive triggers — when Claude should invoke it without being asked].
```

**Quality bar for descriptions:**
- Cover every major trigger phrase (nouns, verbs, intent patterns)
- Include at least 3 behavioral triggers (not just "user says X")
- Include at least 1 proactive trigger (when to invoke without being asked)
- Not so broad it fires in unrelated contexts
- Total length: 60–150 words

#### Step 3: Write the Body
The skill body is what executes when the skill fires. Structure:

```markdown
# [Skill Name]

**[One-line philosophy or tagline — what this skill believes about its domain]**

[2-3 sentence intro — the problem this solves, the perspective it brings]

---

## [Section: Core Protocol / The Team / How It Works]
[Main content]

## Arguments
- `arg_name`: description. Default: value.

## Output Format
[What the skill produces — structure, length, format]

## Integration
[How this skill connects to other skills]
```

#### Step 4: Create the File
Write the SKILL.md to `~/.claude/skills/{skill-name}/SKILL.md`.

Create the directory if it doesn't exist.

#### Step 5: Trigger Eval
After writing, run a trigger evaluation — verify the description fires on the intended contexts and not on the anti-trigger contexts:

```
TRIGGER EVAL: {skill-name}

✅ Should trigger:
  [query 1] → [PASS/FAIL]
  [query 2] → [PASS/FAIL]
  ...

❌ Should NOT trigger:
  [query 1] → [PASS/FAIL]
  [query 2] → [PASS/FAIL]

Trigger accuracy: N/M (N%)
```

If accuracy < 80%, iterate on the description and re-eval.

---

### Mode 2: Description Optimization

When the Flywheel flags a skill as under-triggering (low invocation count despite high value when used) or over-triggering (fires in wrong contexts, negative sentiment).

**Inputs:**
- Skill name
- Current description (read from the SKILL.md)
- Positive examples: contexts where the skill DID trigger correctly
- Negative examples: contexts where it should have triggered but didn't (undertriggering) OR contexts where it fired incorrectly (overtriggering)

**Process:**

1. **Read the current description**
2. **Analyze the gap** — what's the pattern in the missed/wrong triggers?
   - Undertriggering: description is too narrow, missing key phrases or intent patterns
   - Overtriggering: description is too broad, shares language with unrelated skills
3. **Propose a rewrite** — show the current vs. proposed description side-by-side
4. **Run trigger eval** on both — show improvement in accuracy
5. **Apply if accuracy improves** — write the updated description to the SKILL.md

**Rewrite principles:**
- Don't change the body — description optimization only touches the `description:` frontmatter field
- Don't add functionality — optimize trigger accuracy, don't expand scope
- Preserve the skill's identity — the voice and character stay the same

---

### Mode 3: Body Revision

When the Flywheel flags a skill as having high correction rates (correction_rate > 30%) or negative sentiment.

**Inputs:**
- Skill name
- Current SKILL.md body
- Flywheel log entries: the `context` and `note` fields from entries where `followed_by_correction: true` or `user_sentiment: negative`

**Process:**

1. **Read the correction contexts** — what was the user trying to do when they had to correct the output?
2. **Identify the root cause** — which part of the skill body produced the wrong output?
   - Wrong format? → Fix the output format section
   - Wrong scope? → Clarify what the skill does and doesn't do
   - Missing step? → Add the step that was always being done manually after
   - Wrong assumption? → Update the assumption in the protocol
3. **Propose targeted changes** — specific line edits, not a full rewrite (unless warranted)
4. **Show before/after** of the changed sections
5. **Apply if user approves** — write the updated body to the SKILL.md

**Anti-pattern: The Full Rewrite Trap**
Don't rewrite the whole skill body because one section is wrong. Identify the specific section causing corrections and fix only that. Surgical > wholesale.

---

## Skill Health Criteria

A healthy skill:
- Triggers on ≥80% of its intended contexts
- Does NOT trigger on unrelated contexts
- Produces output that requires correction < 20% of the time
- Has positive or neutral sentiment in most Flywheel entries
- Has been invoked at least 3 times (if not, evaluate if it's needed at all)

An unhealthy skill exhibits one or more of:
- correction_rate > 30% → Body Revision needed
- Sentiment mostly negative → Body Revision needed
- Very low invocation count → Description Optimization needed
- Never invoked → Consider retiring (or the description is broken)
- Always the same context → Skill may be too narrow

---

## Integration

| Skill | Relationship |
|-------|-------------|
| `/flywheel` | Primary caller — Flywheel identifies which mode to run and provides the log data |
| Sister Cadence (in `/guru-bin`) | Calls this skill when Guru Bin's protocol needs refinement |
| Any skill | Any skill's author can invoke this to improve their own skill |

---

## Arguments

- `mode`: `create` | `description` | `body`. Default: infer from context.
- `skill`: Name of the skill to optimize (for modes `description` and `body`).
- `examples`: Positive trigger examples for description optimization (comma-separated queries).
- `anti_examples`: Negative trigger examples (should NOT trigger).
