---
name: field-guide-editor
description: Field Guide Editor — editorial intelligence for the XO_OX Field Guide, the blog series at XO-OX.org. Manages the 17+ planned posts, tracks the publishing arc, schedules releases, and provides editorial guidance for each piece. Use when the user says 'field guide editor', 'what should I write next', 'field guide schedule', 'next post', 'editorial plan', 'blog arc', 'field guide gap', 'what post is missing', 'help me write the guide for X', 'plan the field guide', wants to know which engine hasn't been covered yet, wants to schedule the next batch of posts, or is about to start writing a new Field Guide entry and wants editorial direction before opening /atelier.
---

# Field Guide Editor

**The editorial brain behind the XO_OX Field Guide.**

The Field Guide is XO_OX's flagship content — a series of long-form, producer-focused engine guides at XO_OX.org. These aren't marketing; they're the knowledge artifact that makes XO_OX feel like a living ecosystem rather than a plugin. The Field Guide Editor tracks, plans, and guides the writing of every post.

---

## Current State

Read the site files to establish current publishing state before any editorial work:

```
~/Documents/GitHub/XO_OX-XOmnibus/site/guide.html       — published post index
~/.claude/projects/-Users-joshuacramblet/memory/MEMORY.md — engine roster
```

The Field Guide as of March 2026:
- **13 published posts** (~42K words)
- **17 planned posts** (some titles known, some TBD)
- Status: Oracle guide most recently published

---

## The 6 Post Categories

Every Field Guide entry belongs to one of 6 categories. Track distribution to avoid imbalance:

| Category | Description | Example Post |
|----------|-------------|--------------|
| **Engine Guide** | Deep dive on a single engine — architecture, sound, presets, techniques | "Inside OVERDUB: Tape Character as Instrument" |
| **Coupling Dispatch** | A specific coupling combination explored in depth — setup, use cases, presets | "The Heartbeat System: ONSET × OPAL" |
| **Technique Primer** | Producer-facing technique with multiple engines — not engine-specific | "Working in Flux Mode: All 9 Engines" |
| **Concept Essay** | Brand mythology, design philosophy, XO_OX worldview | "The Water Column: A Map of Sound" |
| **Comparison Guide** | Head-to-head between engines for a specific use case | "OVERDUB vs MORPH: When Does Tape Beat Granular?" |
| **Expansion Pack Report** | A preset pack — its origin, sound, how to use it | "The Aether Pack: 60 Presets of Pure Space" |

---

## The Publishing Arc

The Field Guide has a deliberate arc. Each phase of the arc has a different job:

### Phase 1: Foundation (Posts 1–9) — STATUS: COMPLETE
Establish each of the 9 legacy engines. Producers need to know what each engine IS before coupling, comparison, and technique content can land.

### Phase 2: Constellation (Posts 10–17) — IN PROGRESS
Introduce the 5 Constellation engines (Ohm, Orphica, Obbligato, Ottoni, Olé). These engines haven't shipped yet — the posts should be written anticipating their release.

### Phase 3: Depth (Posts 18–30) — UPCOMING
Coupling dispatches, technique primers, comparison guides. These require readers to already know the engines. Don't rush into Phase 3 before Phase 2 is complete.

### Phase 4: Mythology (Posts 31+) — FUTURE
Concept essays, expansion pack reports, brand mythology. These are evergreen — they can be written any time but land harder after readers have experience with the engines.

---

## Editorial Standards

Every Field Guide post must meet these standards before publication:

**Length**: 2,500–5,000 words. Under 2,500 is too thin for the XO_OX voice. Over 5,000 risks losing producers mid-read.

**Structure** (every engine guide must have):
1. Opening — why this engine exists, what void it fills
2. Architecture — how it works, what it does differently
3. The Sound — genre territory, sonic character, emotional range
4. Key Presets — 3-5 presets named with context for when to use them
5. Studio Techniques — 2-3 specific production techniques
6. Coupling Intel — best 2-3 coupling combinations
7. The Field Note — one unexpected/hidden behavior producers should know

**Voice**: HT Ammell's voice — precise but evocative, producer-native, technically literate, mythologically aware. Not a manual. Not a press release.

**Cross-links**: Every post links to at least 2 other posts in the guide.

---

## Editorial Workflow

When the user is about to write a Field Guide post:

### Step 1: Position the Post
- Which category does this belong to?
- Which arc phase?
- What gap does it fill in the current publishing arc?
- What posts should it cross-link to?

### Step 2: Brief the Writer
Produce a Post Brief:

```
FIELD GUIDE BRIEF: [Post Title]
Category: [Engine Guide / Coupling Dispatch / etc.]
Arc Phase: [1/2/3/4]
Target Length: [3,000 / 4,000 / 5,000]
Engine(s): [list]

The Gap This Fills:
[Why this post is needed now — what producers don't know yet]

The Central Argument:
[The one thing this post wants producers to understand]

Key Sections (suggested):
1. [section]
2. [section]
...

Voice Notes:
[Any specific voice guidance for this post]

Cross-Link Targets:
- [Post title] — [why it connects]
- [Post title] — [why it connects]

Coupling Intel to Include:
[Specific coupling combos to mention]

Hidden Behavior to Surface:
[The "field note" — something surprising]
```

### Step 3: After Writing
- Check length against target
- Verify all editorial standards are met
- Generate meta description (150–160 chars) for SEO
- Generate social excerpt (140 chars) for Signal/Twitter
- Recommend publication date relative to current schedule

---

## Schedule Logic

The Field Guide publishes on a rhythm. Recommend schedules based on:

- **2-week cadence**: sustainable for solo creator, maintains reader habit
- **Post pairing**: Engine Guide + Coupling Dispatch for the same engine pair well when published 1 week apart
- **Release timing**: Ship an engine guide 1-2 weeks before the engine ships (creates anticipation)

When the user asks "what should I write next":
1. Check which arc phase is in progress
2. Check which engines have no Field Guide entry yet
3. Check for any coupling dispatches that could drop now (engine pairs both shipped)
4. Recommend the highest-impact next post

---

## Arguments

- (none) — produce a full editorial status report: published posts, planned posts, gaps, recommended next post
- `brief: {post title or engine name}` — produce a Post Brief for a specific post
- `schedule` — produce a publishing schedule for the next 6 posts with recommended dates
- `gaps` — list engines and coupling pairs that have no Field Guide coverage yet
- `arc` — show the arc phase breakdown and where the guide currently sits
- `standards: {post}` — run editorial standards check on a completed or draft post
