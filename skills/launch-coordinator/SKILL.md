---
name: launch-coordinator
description: Launch Coordinator — orchestrates XO_OX product launches from pre-launch through post-launch. Builds press kits, launch timelines, announcement sequences, download pages, and beta coordination for engine releases, expansion packs, and platform milestones. Use when the user says 'launch coordinator', 'launch plan', 'ship this', 'pre-launch checklist', 'press kit', 'announcement', 'beta program', 'release notes', 'launch timeline', 'we're shipping', 'ready to release', 'V1 launch', 'how do I announce this', or is approaching a major release and needs a coordinated plan across site, community, and distribution channels.
---

# Launch Coordinator

**Every XO_OX release deserves a proper arrival.**

The Launch Coordinator builds and executes coordinated product launches — not ad hoc announcements, but sequenced campaigns that build anticipation, convert interest, and create lasting momentum. Every engine, pack, and platform milestone has a launch that matches its weight.

---

## Launch Types

| Launch Type | Weight | Timeline | Channels |
|-------------|--------|----------|---------|
| **V1.0 Platform** | Maximum | 6 weeks | All channels, press outreach |
| **New Engine** | Major | 3 weeks | Site, Signal, MPC community |
| **Expansion Pack** | Standard | 1 week | Signal, site pack page |
| **Update/Patch** | Minor | 2-3 days | Changelog, brief Signal post |
| **Beta Program** | Invitation | 1 week | Direct, select community |

---

## Pre-Launch Assessment

Before building a launch plan, assess readiness:

### Technical Readiness
- [ ] Build compiles clean, auval PASS
- [ ] All planned presets present and QA'd
- [ ] Installer tested on macOS (at minimum M1 + Intel)
- [ ] Plugin loads in Logic Pro, Ableton, MPC Software
- [ ] No P0 or P1 bugs open

### Content Readiness
- [ ] Product page complete (site/index.html or site/packs.html)
- [ ] Feature list accurate and complete
- [ ] Screenshots current (matches shipping version UI)
- [ ] Audio previews recorded (hero preset clips)
- [ ] Field Guide entry published or scheduled
- [ ] Download/purchase link functional

### Community Readiness
- [ ] Announcement copy drafted
- [ ] Signal post written
- [ ] MPC community forum post ready
- [ ] Patreon update ready (if applicable)

Flag any missing items as BLOCKERS or DESIRABLES before proceeding.

---

## Launch Timeline Template

### 6-Week V1 Platform Launch

```
Week -6: Foundation
  - Finalize feature set (freeze scope)
  - Record all hero audio clips
  - Commission/complete all screenshots

Week -5: Content
  - Publish Field Guide entry for flagship engine
  - Write all announcement copy
  - Build download/purchase page

Week -4: Beta
  - Invite 10-20 beta testers (MPC producers)
  - Share beta build + feedback form
  - Collect feedback, triage critical issues

Week -3: Polish
  - Address beta feedback
  - Final auval + installer validation
  - Finalize press kit

Week -2: Pre-Heat
  - Teaser post (Signal, MPC community)
  - "Something is coming" social without naming it
  - DM key community voices

Week -1: Countdown
  - Reveal the name + one hero audio clip
  - "Ships in 7 days" announcement
  - Patreon early access (if applicable)

Launch Day:
  - Publish download + site simultaneously
  - Signal announcement post
  - MPC community thread
  - Patreon post

Week +1: Momentum
  - Follow-up: first producer reactions
  - Field Guide post #2 (coupling or technique)
  - Address any urgent post-launch issues
```

### 3-Week Engine Launch

```
Week -3: Readiness check — build, presets, content all locked
Week -2: Teaser (name reveal + 1 clip)
Week -1: Field Guide post goes live
Launch Day: Site + Signal + MPC post simultaneously
Week +1: Follow-up coupling content
```

### 1-Week Pack Launch

```
Day -7: Pack complete, QA'd, priced
Day -5: Teaser clip on Signal
Day -3: Pack page live (preview mode)
Day 0: Full announcement + download active
```

---

## Press Kit

For major launches, produce a press kit:

```
XO_OX PRESS KIT: [Product Name]

PRODUCT OVERVIEW
Name: [Name]
Version: [X.X.X]
Platform: macOS AU/VST3, compatible with MPC Software, Logic Pro, Ableton Live
Price: [Price or "Free" or "Patreon exclusive"]
Download: [URL]

ONE-LINER
[Single sentence that captures the product — what it is, what it does, why it matters]

LONG DESCRIPTION (200 words)
[Full description for press, should include: what it is, how it's different, who it's for]

KEY FEATURES
1. [Feature]
2. [Feature]
...

TECHNICAL SPECS
- Synthesis: [type]
- Voices: [count]
- Parameters: [count]
- Presets: [count]
- Formats: AU, VST3
- Requirements: macOS 12+, Apple Silicon or Intel

AUDIO DEMOS
[Links to Soundcloud/file host]

SCREENSHOTS
[Links to hi-res screenshots]

BRAND ASSETS
Logo: [path/URL]
Brand colors: [hex values]
Press contact: [contact]
```

---

## Announcement Copy Templates

### Signal Post — Launch Day
```
[ENGINE NAME] is here.

[1-2 sentence description of what it does / what it sounds like]

[Key number stat — "X presets", "X engines", "40 parameters"]

[Call to action — "Download free", "Available now", "Grab it"]

[Link]

[2-3 relevant tags: #XO_OX #[engine] #MPC]
```

### MPC Community Post
```
[Title: Just shipped: [Name] — [1-line description]]

Hey everyone — just released [Name], a [synthesis type] plugin for MPC and DAW.

[2-3 paragraph description — more casual than press kit, producer-to-producer]

[Key things producers care about: CPU, presets, MPC compatibility]

Download / more info: [link]

Happy to answer questions. Let me know what you think.
```

---

## Beta Program

For major launches, run a structured beta:

**Beta Invite Template:**
```
Hey [name],

I'm about to ship [product] and I'd love your ears on it before it goes public.

It's a [description]. Ships in [X] weeks. Beta runs [dates].

What I'm looking for:
- Preset quality (do these sound production-ready?)
- Stability (any crashes, UI bugs)
- MPC compatibility (load in your setup, everything work?)

In exchange: your name in the credits + early access to future packs.

Interested?
```

**Beta Feedback Collection:**
Run a simple feedback pass — create a document or form with:
- Critical bugs (anything blocking use)
- Sound design notes (presets that don't work)
- UI issues
- Feature requests (for V2 backlog, not V1 scope)

---

## Arguments

- (none) — full launch assessment: what's the current launch-readiness state?
- `plan: {product name}` — build a full launch timeline for a specific product
- `press-kit: {product name}` — generate a complete press kit
- `copy: {channel}` — write announcement copy for a specific channel (signal, mpc-community, patreon)
- `beta` — design a beta program: invite criteria, feedback collection, timeline
- `checklist` — run the pre-launch readiness checklist against current project state
- `debrief` — post-launch retrospective template: what worked, what to do differently next time
