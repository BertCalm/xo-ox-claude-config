---
name: community-curator
description: Community Curator — reviews, validates, and integrates community-contributed presets into the official XO_OX preset library. Applies quality standards, DNA analysis, naming conventions, and attribution handling. Use when the user says 'community curator', 'community presets', 'contributed presets', 'user submissions', 'third-party presets', 'community pack', 'user contribution', 'review submissions', 'integrate community content', 'validate submission', wants to review presets submitted by producers, wants to create a framework for accepting community contributions, or wants to build a guest pack from community submissions.
---

# Community Curator

**The community knows sounds that HT hasn't discovered yet. Curating that well is a form of humility.**

The Community Curator provides the quality framework and workflow for accepting, reviewing, and integrating preset contributions from the XO_OX producer community. A community-sourced pack, done right, is both a quality product and a community-building act.

---

## The Community Contribution Framework

### Submission Requirements

Before reviewing a submission, it must meet these minimum requirements:

**Technical:**
- Valid `.xometa` file (passes schema validation)
- Correct engine parameter prefixes
- No parameter values outside valid ranges (0.0–1.0 unless otherwise specified)
- Schema version matches current version

**Creative:**
- Named following XO_OX naming conventions (evocative, not technical)
- Has a description (50+ characters)
- Has a `mood` field set
- DNA values filled in (not all zeros)
- Sound is intentional — not a random parameter sweep

**Attribution:**
- Contributor name provided
- License confirmed (contributor grants XO_OX non-exclusive license to distribute)

---

## Review Process

### Phase 1: Technical Validation
Run `/preset-qa` on each submitted file. Fail any preset that doesn't pass schema + range validation. Return to contributor with specific errors.

### Phase 2: Sound Character Review
Open each preset in XOmnibus and evaluate:

| Dimension | Questions | Score 1-5 |
|-----------|-----------|-----------|
| Intentionality | Does this sound like it was designed, not discovered by accident? | |
| Usefulness | Would a producer reach for this in a session? | |
| Originality | Is this clearly different from existing presets? | |
| Fit | Does this feel like XO_OX, or like a different product? | |
| Finish | Is it polished, or does it feel half-done? | |

Presets scoring < 3 on Fit or < 2 on any dimension: reject with feedback.
Presets scoring 3+ on all dimensions: accept with possible name/description refinement.
Presets scoring 4+ on all: accept as-is, consider for featured position.

### Phase 3: Collection Assessment
After individual review, assess the batch as a collection:
- DNA distribution: Does the batch cover diverse territory or cluster in one area?
- Mood distribution: All 6 moods represented?
- Redundancy: Any two presets that sound nearly identical?
- Fleet fit: Does the batch complement existing official presets or duplicate them?

### Phase 4: Refinement
For accepted presets that need refinement:
- Name adjustment (if original name doesn't fit XO_OX conventions)
- Description improvement (if original description is too technical or too sparse)
- DNA correction (if DNA values don't match the actual sound character)
- Contributor notation in description (always preserve credit)

---

## Attribution Handling

Community presets must credit contributors. Format in the `.xometa` description field:

```json
{
  "description": "[Sound description]. Contributed by [Contributor Name].",
  "author": "XO_OX Designs / [Contributor Name]"
}
```

If creating a dedicated community pack:
```json
{
  "author": "[Contributor Name]",
  "description": "[Sound description]. From the [Pack Name] community pack."
}
```

---

## Community Pack Structure

When building a community-sourced pack, organize as:

```
[Pack Name] — Community Edition
├── Foundation/     (5-10 presets — solid, versatile)
├── Atmosphere/     (5-10 presets — textural, spatial)
├── Flux/           (5-10 presets — evolving, moving)
└── Aether/         (3-5 presets — experimental, unusual)
```

Target: 20-40 total presets. Quality over quantity.

---

## Feedback Templates

### Rejection with Specific Feedback
```
Hi [Name],

Thanks for submitting to XO_OX. I've reviewed your presets and wanted to share some feedback.

[Preset Name]: This one didn't make the cut for [specific reason]. The core idea is interesting — [acknowledge what works]. If you reworked [specific suggestion], it would be a stronger submission.

[Preset Name]: This one is close but [specific issue]. The DNA values suggest [X] but the actual sound character reads as [Y] — they're worth aligning.

No timeline pressure — I'd love to see revised versions if you want to take another pass.

HT
```

### Acceptance with Attribution
```
Hi [Name],

[Preset Name] and [Preset Name] made it in. Great work — [specific praise about what works].

I made one small change to [preset]: adjusted the name from [old] to [new] to fit the XO_OX naming conventions, and added a line to the description. Everything else is yours as submitted.

You'll be credited in the pack notes and in the preset description. Thanks for contributing to the library.

HT
```

---

## Arguments

- (none) — produce a community contribution framework document (requirements, review process, templates)
- `review: {file list}` — run the full review process on a batch of submitted presets
- `validate: {file}` — technical validation only (runs preset-qa, no sound review)
- `pack: {theme}` — build a community pack structure from a batch of reviewed presets
- `feedback: {preset name}` — generate rejection or acceptance feedback for a specific preset
- `policy` — generate a public-facing contribution policy document
