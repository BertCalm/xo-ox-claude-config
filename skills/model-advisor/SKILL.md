# Model Advisor

Analyze the current task and recommend the optimal Claude model + effort level.

## Trigger

Use when the user invokes `/model-advisor` or asks which model to use for the current work.

## Instructions

1. Look at what the user is currently working on (from conversation context or ask them to describe it)
2. Classify the task using the rubric below
3. Give a one-line recommendation with the exact command to run

## Classification Rubric

| Task Type | Model | Effort | Examples |
|-----------|-------|--------|---------|
| Novel architecture, new engine design from scratch, complex DSP theory, multi-system coupling design, QA analysis across codebases | Opus 4.6 | High | New synth engine design, barycentric ERA system, coupling architecture |
| Pattern-following code (JUCE UI following existing style), bug fixes in known code, wiring params, build validation, code exploration | Sonnet 4.6 | Medium | Adding UI controls, fixing compile errors, adding parameters |
| Mechanical/repetitive tasks | Sonnet 4.6 | Low | JSON preset authoring, git commits, single-file edits, grep/read tasks |

**Cost optimization trigger**: If the task type just shifted from architecture → execution, suggest downgrading.

## Output Format

State the task type in one sentence, then:

```
Recommended: /model sonnet --effort medium
```

Or for opus work:
```
Recommended: /model opus --effort high
```

If already on the right model, confirm it and say nothing more.

## Proactive Use

I should suggest the model at the **start of any XO_OX session** before diving in, especially when:
- The user opens with a new feature request
- The work shifts from design → implementation
- The user mentions usage/cost (80% usage, etc.)
