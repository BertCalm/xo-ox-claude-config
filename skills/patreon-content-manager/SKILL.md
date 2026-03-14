---
name: patreon-content-manager
description: Patreon Content Manager — plans, schedules, and writes Patreon content for XO_OX Designs. Manages the creator economy calendar, patron tier benefits, exclusive content delivery, and the ongoing rhythm of Patreon posts. Use when the user says 'patreon content manager', 'patreon post', 'patreon update', 'what should I post to patreon', 'patreon schedule', 'patron benefits', 'exclusive content', 'patreon calendar', 'creator economy', 'patron engagement', 'patreon tier design', wants to write a Patreon post, wants to plan a month of Patreon content, needs to define patron tier benefits, or wants to make sure Patreon stays active and valuable for supporters.
---

# Patreon Content Manager

**Patrons are the people who believed before anyone else. They deserve the best content.**

The Patreon Content Manager turns the XO_OX creative process into a continuous stream of patron value — early access, behind-the-scenes, exclusive presets, and the kind of insight that makes patrons feel like they're inside the process, not watching from outside.

---

## The XO_OX Patreon Value Proposition

XO_OX Patreon is not just a tip jar. It's the inner circle. Patrons get:
- **Early access** to engines and packs before public release
- **Exclusive presets** — sounds that don't appear anywhere else
- **Behind-the-scenes** content — design sessions, decisions, dead ends
- **Direct input** — polls on engine concepts, preset directions, feature priorities
- **Field Guide extended cuts** — more technical depth than the public posts
- **The Session Log** — a monthly update on what was built and why

---

## Tier Structure

### Tier 1: The Surface (Entry)
**Positioning**: For fans who want to support without going deep.
**Benefits**: Public posts, occasional patron-only update, gratitude
**Price point**: ~$3-5/month

### Tier 2: The Twilight Zone (Core)
**Positioning**: For active producers who use XO_OX regularly.
**Benefits**: All Tier 1 + early access to engines/packs, exclusive preset pack per quarter, behind-the-scenes posts, Patreon Discord (if exists)
**Price point**: ~$10-15/month

### Tier 3: The Deep Water (Committed)
**Positioning**: For serious XO_OX users and those who want to shape the project.
**Benefits**: All Tier 2 + monthly exclusive preset pack, name in credits, direct input on engine development direction, access to beta builds
**Price point**: ~$25-30/month

---

## Content Calendar

The Patreon needs a regular cadence to stay active. Recommended monthly rhythm:

| Week | Content Type | Description |
|------|-------------|-------------|
| Week 1 | **Session Log** | What was built/shipped/discovered this month — informal, inside baseball |
| Week 2 | **Exclusive Preset Drop** | 5-10 presets with notes on why they were designed this way |
| Week 3 | **Design Dispatch** | Behind-the-scenes look at a decision, experiment, or design problem |
| Week 4 | **Early Access / Teaser** | Preview of what's coming — engine name reveal, audio clip, concept |

Plus irregular:
- **Patron Poll**: "Which engine should I focus on next?" — keep patrons in the loop
- **Beta Invite**: When something's ready for select ears before public release
- **Milestone Celebration**: When an engine ships, a pack hits a download milestone

---

## Post Templates

### The Session Log
```
[Month] in the Workshop

Hey everyone — [brief intro, 1-2 sentences about the month's energy]

This month I:
• [Shipped / built / designed X]
• [Solved / figured out Y]
• [Decided to do Z, here's why]

The most interesting thing I learned: [1 paragraph about a discovery or insight]

What's coming: [brief preview of next month]

Thanks for being here,
HT
```

### Exclusive Preset Drop
```
[Pack Name] — Patron Exclusive

[1-2 sentences about the sound character of this pack]

What's in here:
• [Preset name] — [1 sentence on what it is and when to use it]
• [Preset name] — [same]
...

How I made [specific preset]: [brief story — 1 paragraph about the design decision or happy accident]

[Attach .xometa files or .xpn bundle]
```

### Design Dispatch
```
[Title — frame it as a question or tension, e.g., "Why OVERDUB has no dry/wet control"]

[1 paragraph setting up the design question]

[2-3 paragraphs walking through the reasoning — honest about trade-offs, dead ends]

The conclusion / what I landed on: [final decision and why]

If you have thoughts on this: [invitation to comment — make it specific, not generic]
```

### Early Access / Teaser
```
[ENGINE NAME] — First Look [PATRON ONLY]

Before this goes public, I wanted to give you a preview.

[1-2 paragraphs on what it is, what makes it different]

[Audio embed or attachment]

It ships [date]. Patron download link drops [date — ideally 1 week before public].

What do you think? [specific question]
```

---

## Content Planning Protocol

When invoked for content planning:

1. **Read current state** from MEMORY.md — what's been shipped, what's coming
2. **Identify content opportunities** — engine milestones, pack drops, design experiments
3. **Generate a 4-week calendar** with specific post topics
4. **Flag any gaps** — months where nothing is happening that needs filling with behind-the-scenes content

---

## Arguments

- (none) — generate a 4-week Patreon content calendar based on current project state
- `post: session-log` — write this month's Session Log
- `post: preset-drop` — write a preset drop post (provide pack name)
- `post: dispatch: {topic}` — write a Design Dispatch on a specific design decision
- `post: teaser: {engine}` — write a teaser/early access post for a specific engine
- `tiers` — review current tier structure and recommend adjustments
- `poll: {question}` — draft a patron poll with 3-4 options
- `calendar` — generate a 3-month content calendar
