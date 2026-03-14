---
name: changelog-generator
description: Changelog Generator — translates raw git commit history and dev notes into polished, producer-facing release notes for XO_OX plugins. Use when the user says 'changelog', 'release notes', 'what changed', 'write the changelog', 'version notes', 'what's new in this version', 'generate changelog', wants to write release notes before shipping an update, has a list of changes and wants them formatted for users, needs both a technical changelog and a producer-friendly summary, or is preparing any XO_OX release from a patch to a major version.
---

# Changelog Generator

**Dev commits → producer release notes.**

Git history tells you what changed. The Changelog Generator tells producers why they care. Every XO_OX release gets two changelog artifacts: a technical changelog (for version control and developers) and a producer-facing "What's New" section (for the site, Signal, and the plugin's about screen).

---

## Input Formats

The Generator accepts any of these as input:

1. **Raw git log**: `git log v0.9.0..HEAD --oneline` output
2. **Dev notes**: Bullet list of changes ("added filter saturation", "fixed note-off bug")
3. **Mix**: Git log + additional context the user provides
4. **Verbal description**: "We added X, fixed Y, changed Z"

---

## Changelog Architecture

### 1. Technical Changelog (for CHANGELOG.md / git tags)

Follows Keep a Changelog format:

```markdown
## [X.X.X] — YYYY-MM-DD

### Added
- [New feature or preset or parameter]

### Changed
- [Modified behavior — describe old → new]

### Fixed
- [Bug fix — describe what was broken]

### Removed
- [Anything removed — especially parameters that would affect presets]

### Deprecated
- [Still works but will be removed in future version]
```

Rules:
- One line per change
- Past tense, active voice ("Added filter saturation stage" not "filter saturation was added")
- Include file/component context when useful ("XOdyssey: added wavetable bank switching")
- Never vague ("various improvements" — always be specific)

### 2. Producer-Facing "What's New"

For the product page, plugin about screen, and Signal:

```
WHAT'S NEW IN [ENGINE] [VERSION]

[1-2 sentence headline that captures the most important change]

New in this version:
• [Change 1 — described in producer language, not dev language]
• [Change 2]
• [Change 3]

Bug fixes:
• [Fix 1 — described as what the producer would have noticed]
• [Fix 2]

[Optional: Upgrade note if presets or settings need attention]
```

Producer language rules:
- "Added filter saturation" → "Your filters now clip and saturate — push them harder for drive character"
- "Fixed note-off not clearing voices" → "Fixed: long notes no longer hang after release"
- "Increased polyphony from 6 to 8 voices" → "8-voice polyphony — thicker chords, more simultaneous layers"
- Never use: "refactored", "optimized codebase", "updated dependencies" — producers don't care

### 3. Signal Post (Social)

For major updates:

```
[ENGINE] [VERSION] is out.

[Top 3 changes in 3 short punchy sentences or bullets]

[Download link or "update now" CTA]

#XO_OX #[engine] #MPC
```

---

## Change Classification

When reading a git log or dev notes, classify each change:

| Dev language | Classification | Producer weight |
|-------------|---------------|-----------------|
| New parameter, control, or mode | Added | HIGH |
| New preset or preset pack | Added | HIGH |
| New coupling type or behavior | Added | HIGH |
| UI change, new visual element | Added | MEDIUM |
| Behavior change (how existing feature works) | Changed | HIGH if audible |
| Performance improvement | Changed | LOW (mention only in technical log) |
| Build/config change | Changed | SKIP in producer notes |
| Crash fix | Fixed | HIGH |
| Audio artifact fix (clicks, pops, denormals) | Fixed | HIGH |
| Preset loading bug | Fixed | HIGH |
| Visual/UI bug | Fixed | LOW |
| MIDI handling fix | Fixed | MEDIUM |
| Code cleanup, refactor | Internal | SKIP in both |
| Dependency update | Internal | SKIP in both |

---

## Version Numbering Guide

XO_OX follows semantic versioning:

| Increment | When | Example |
|-----------|------|---------|
| **MAJOR** (X.0.0) | Breaking preset compatibility, complete architecture change | v2.0.0 |
| **MINOR** (x.X.0) | New features, new parameters, new presets | v1.3.0 |
| **PATCH** (x.x.X) | Bug fixes, no new features | v1.3.2 |

**Preset compatibility warning**: Any change that breaks existing presets or changes parameter behavior MUST include an upgrade note. This is the most important producer-facing information in any changelog.

---

## Preset Impact Assessment

Before generating the changelog, flag any changes that affect preset compatibility:

- **Safe**: UI changes, visual bugs, crash fixes, MIDI handling, new presets added
- **Warning — test presets**: Parameter range changes, new parameters with defaults, filter behavior changes
- **Breaking — migration needed**: Parameter removal, parameter rename, schema version change

If breaking changes are present, generate a migration note:

```
UPGRADE NOTE:
This update changes [X parameter] behavior. Presets saved in v1.2 may sound different.
To restore the original sound: [specific steps]
A preset migration is available at [location if applicable].
```

---

## Protocol

1. Read the git log or accept dev notes from user
2. Classify each change (Added / Changed / Fixed / Internal)
3. Flag any preset-impacting changes
4. Recommend version number increment
5. Generate Technical Changelog (CHANGELOG.md format)
6. Generate Producer "What's New" section
7. If major release: generate Signal post
8. If breaking changes: generate upgrade note

---

## Arguments

- (none) — prompt for input (git log or dev notes), then generate full changelog package
- `--engine {name}` — scope to a specific engine in XOmnibus
- `--signal` — include Signal post in output
- `--version {X.X.X}` — use a specific version number (skip recommendation)
- `--minor` / `--patch` / `--major` — force version increment type
- `--check-presets` — specifically check for preset compatibility issues in the diff
