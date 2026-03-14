---
name: producers-guild
description: "The Producer's Guild — convene 12 genre specialists, a Product Manager, Market Research Consultant, Technical Architect, Ops Crew, and the Foreseer to deliver a comprehensive product enhancement roadmap for any XO_OX engine or XOmnibus feature. Use when: user asks how to improve an engine, wants a preset gap analysis, asks what features to build next, wants market positioning, needs a product roadmap, asks 'what would producers want', 'what's missing', 'what should I build next for X engine', 'how do I make X more competitive', 'feature roadmap', 'what do DJs / beatmakers / film composers need', or wants to go from maintenance mode to a genuine product upgrade. The Guild takes consumer listening and turns it into consumer prediction — it finds the needs users don't know they have."
---

# The Producer's Guild

The XO_OX ecosystem is built by one person but used by many. The Producer's Guild bridges that gap — summoning the expertise of 12 genre specialists alongside a product team to transform an engine from what it is into what it could be.

The Guild's philosophy: **listen to the market, then predict beyond it**. Feature requests tell you what users know. The Foreseer tells you what they'll want before they know it's possible.

## The Roster

### Genre Specialists (12 Panels)

Each specialist is a named expert with decades of production experience in their genre. They speak from the producer's chair — not as critics, but as collaborators who want the instrument to succeed in their world.

| # | Specialist | Genre Domain | Listening For |
|---|-----------|-------------|---------------|
| 1 | **Beatrice "Trap" Morales** | Hip-Hop / Trap / Drill | 808 sub punch, snare snap, velocity layers, sidechain behavior, low-mid separation |
| 2 | **Marcus "Deep" Williams** | Deep House / Techno / Minimal | Filter resonance character, LFO tempo sync, CPU headroom for long sets, warmth vs. sterility |
| 3 | **Kai Suzuki** | Ambient / Drone / Experimental | Evolution over time, infinite sustain, micro-tuning, controlled randomness, long release tails |
| 4 | **Sofia Chen** | Jazz / Neo-Soul / Fusion | Touch sensitivity, velocity expressivity, chord voicing, voice leading, organic imperfection |
| 5 | **Jerome "Dub" Baptiste** | Dub / Reggae / Bass Music | Send/return behavior, echo manipulation, sub bass resonance, spatial depth, tape character |
| 6 | **Amara Okonkwo** | Afrobeat / World / Global | Rhythmic complexity, timbral variety, ensemble layering, call-and-response textures |
| 7 | **Lars Eriksson** | Cinematic / Film Score / Game Audio | Dynamic range, expression mapping, MIDI CC depth, layering behavior, tension-to-release arc |
| 8 | **Priya Sharma** | Pop / Commercial / Radio | Instant gratability, polished top end, radio-ready out of box, hook-friendly presets |
| 9 | **Rico Valdez** | Latin / Electronic / Club | Groove and syncopation, energy and build, ensemble brightness, dancefloor energy |
| 10 | **Emma Blackwood** | Rock / Alternative / Indie | Grit, character, saturation behavior, unpredictability, playing feel |
| 11 | **Dr. James Thornton** | Classical / Orchestral / Acoustic Simulation | Articulation, dynamic expressivity, resonance modeling, authentic timbre, sustain pedal behavior |
| 12 | **Zero_1** | Experimental / Noise / Avant-garde | Instability, feedback exploitation, unusual timbres, extreme edge behavior, what breaks it |

### Product Team

**The Product Manager (Maya)** — Synthesizes guild input into a structured feature backlog. Categorizes by: presets, XPN export, playable surfaces, new DSP features, enhancements to existing features, coupling improvements. Scores each by guild endorsement count and estimated user impact. Produces the prioritized feature list.

**The Market Research Consultant (Derek)** — Analyzes the competitive landscape. What do Arturia, Native Instruments, Output, Spitfire, Plugin Boutique, and Splice offer that this engine doesn't? Where is there genuine market whitespace? Which features are table stakes vs. differentiated? Brings viability scoring to Maya's backlog.

**The Technical Architect (Ingrid)** — Reviews the prioritized feature list against the actual codebase architecture. Sequences features for minimum technical debt. Identifies: what can be parallelized, what has hidden dependencies, what's a performance risk, what requires new infrastructure. Ensures the roadmap is buildable in the proposed order.

**The Ops Crew (The Trio: Remy, Sam, Fio)** — Three voices focused on the ground-level reality of building: implementation complexity, integration testing requirements, regression risk, deployment sequencing. They are the ones who get paged when something breaks at 2am. They push back on scope and advocate for stability.

**The Foreseer (unnamed — speaks without a name)** — The synthesis voice. Reads all input from all panels and the product team, then transcends it. The Foreseer doesn't report what users want — they predict what users will want once they see what's possible. They identify the unforeseen issue hidden in the most promising feature. They find the revolutionary possibility disguised as a minor enhancement. They are the difference between a product roadmap and a product vision.

---

## Protocol

### Phase 1: Engine Intake

Before the Guild convenes, build a briefing document:

1. Read the engine's CLAUDE.md — identity, architecture, current features, known limitations
2. Read `synth_playbook/agent_knowledge/` files — preset patterns, DSP techniques, coupling behavior
3. Read any existing Seance verdicts (scores, recommended improvements)
4. Check the preset library — how many presets, what categories, what moods, any gaps
5. Check XPN export status — does the engine export to MPC? What format? Any known issues?
6. Note the engine's position in the aquatic mythology (depth zone, feliX-Oscar polarity, creature)

Compile a 1-page Engine Briefing that gets passed to every panel.

### Phase 2: Genre Panels (dispatch in parallel)

Launch all 12 specialists simultaneously. Each receives the Engine Briefing and answers:

1. **Strengths** — What does this engine do well for my genre? What would I reach for it for?
2. **Gaps** — What's missing that would make it indispensable vs. optional?
3. **Preset needs** — What 5-10 preset archetypes are missing from this engine for my genre?
4. **XPN export** — If I'm using this with an MPC, what would I need to trigger, layer, or perform?
5. **Playable surface** — What performance controls would make this engine feel alive in a live set?
6. **Feature requests** — Specific, actionable: "I need [feature] because [workflow]"
7. **Killer feature** — The one thing, if added, that would make producers in my genre talk about it

Each specialist speaks in their own voice — opinionated, specific, from the production chair. Not generic feedback.

### Phase 3: Product Manager Synthesis

Maya reads all 12 panel reports and produces:

**Preset Gap Analysis**
```
Category     | Missing presets                    | Guild endorsements
-------------|------------------------------------|-----------------
Hip-Hop      | Trap 808 sub-heavy pads            | 3 panels
Cinematic    | Tension stings, action hits        | 2 panels
Ambient      | Infinite evolving textures         | 4 panels
...
```

**Feature Backlog (prioritized)**
```
Priority | Feature                        | Guild votes | Effort est | Impact
---------|-------------------------------|-------------|------------|-------
1        | [Feature name]                | 8/12 panels | Medium     | High
...
```

**XPN Export Enhancements**
What would make the XPN/MPC export experience noticeably better for producers?

**Playable Surface Improvements**
New pad configurations, chord modes, arp patterns, performance macros based on guild input.

**New Features (net-new capabilities)**
Features not currently in the engine that 4+ panels requested.

**Enhancement Opportunities (existing feature upgrades)**
Current features that are "almost there" — what push would make them exceptional?

### Phase 4: Market Research

Derek analyzes:

1. **Competitive landscape** — What do top competitors offer in this sonic territory? (Name specific products, not categories)
2. **Market whitespace** — What does this engine offer that nobody else does? What's the unique selling proposition?
3. **Table stakes vs. differentiation** — Which features on Maya's list are "expected" and which are genuinely differentiating?
4. **Viability scoring** — For each feature on Maya's list: is there demonstrated market demand, or is this speculative?
5. **Priority recommendation** — Derek's version of the top 5 features, with market rationale

### Phase 5: Technical Architecture

Ingrid reviews Maya's prioritized backlog (adjusted by Derek's market scores) and:

1. **Technical feasibility** — Which features are straightforward vs. architecturally complex?
2. **Sequencing** — What order minimizes technical debt and maximizes code reuse?
3. **Dependency map** — Which features unlock other features? Which are blockers?
4. **Performance impact** — CPU budget, real-time safety, memory allocations
5. **Infrastructure needs** — New data structures, new DSP modules, new UI components required
6. **Risk flags** — Which features are likely to introduce regressions?

Output: Ingrid's sequenced technical roadmap with phase groupings.

### Phase 6: Ops Review

The Trio reviews Ingrid's technical roadmap and flags:

- Implementation complexity traps (things that look easy but aren't)
- Integration testing requirements for each feature
- Regression surface for each change
- Deployment order within phases
- "Stop doing it this way" — if any current approach creates chronic maintenance burden

The Trio is allowed to say "not yet" — if a feature is technically possible but operationally risky given current architecture, they can defer it with reasons.

### Phase 7: The Foreseer

The Foreseer receives everything — 12 panel reports, Maya's backlog, Derek's market analysis, Ingrid's architecture, the Trio's ops notes — and speaks last.

The Foreseer's contribution:

**The Unseen Issue** — The one problem nobody mentioned that will matter most. Could be a technical risk, a market risk, a user experience failure, or an identity drift. The Foreseer finds what everyone walked past.

**The Unseen Opportunity** — The possibility hidden in the data that nobody extrapolated to its full conclusion. Often a combination of two modest requests that, combined, creates something revolutionary.

**The Foreseer's Dominoes** — The Foreseer's signature method. For every major decision or feature in the roadmap, she traces the next 7 dominoes that will fall as a consequence — the causal chain of second, third, and fourth-order effects. Not "what happens next" but "what happens next, then what does that enable, then what does that force, then what new problem does that create, then what opportunity does that unlock, then who else enters the market because of that, then what does that make possible that wasn't before."

The Dominoes are written as a chain:
```
[Decision] →
  1. [Immediate consequence]
  2. [What that enables]
  3. [What that forces or forecloses]
  4. [New problem that emerges]
  5. [Opportunity that problem creates]
  6. [Who or what enters because of that]
  7. [What becomes possible that wasn't before]
```

The Foreseer runs Dominoes for the top 2-3 decisions in the roadmap — the ones with the highest consequence, positive or negative. She uses this to optimize the sequencing: build in the order that gets you to domino 7 fastest, and avoid decisions whose domino 3 forecloses something critical.

**The Prediction** — What will producers want from this engine in 18 months that they cannot articulate today? What does the trajectory of their feedback point toward, before they know it's possible?

**The Vision Statement** — One paragraph that reframes the enhancement roadmap as a product evolution narrative. Not a list of features — a direction.

---

## Output: The Guild Report

```markdown
## Producer's Guild Report — [Engine Name]
**Date**: [date]
**Panels convened**: 12 genre specialists + full product team

### Executive Summary
[2-3 sentences: what the Guild found, what the engine is, what it needs to become]

### Genre Panel Highlights
| Specialist | Verdict | Top request |
...

### Preset Gap Analysis
[Maya's table]

### Prioritized Feature Backlog
[Maya's list, adjusted by Derek's market scores and Ingrid's technical reality]

### XPN Export Enhancements
...

### Playable Surface Recommendations
...

### Technical Roadmap (Phases)
[Ingrid's sequenced plan]

### Ops Notes
[The Trio's flags]

### The Foreseer's Vision
**Unseen Issue**: [what everyone walked past]
**Unseen Opportunity**: [the hidden combination]

**The Dominoes** — for each major decision:
```
[Decision] →
  1. [Immediate consequence]
  2. [What that enables]
  3. [What that forces or forecloses]
  4. [New problem that emerges]
  5. [Opportunity that problem creates]
  6. [Who or what enters because of that]
  7. [What becomes possible that wasn't before]
```

**The Prediction**: [18-month trajectory]
**Vision Statement**: [one paragraph — a direction, not a list]

### Next Session Starting Points
[Top 3 actions that can be taken immediately]
```

---

## Arguments

- `engine`: (required) The engine to review. Can be a name (XOverdub, XOdyssey) or path to CLAUDE.md.
- `scope`: (optional) `full` (default — all phases), `presets` (preset gap only), `features` (feature backlog only), `vision` (Foreseer only)
- `quick`: (optional) `true` — skip the full genre panel dispatch, run 4 representative specialists (Marcus/Kai/Beatrice/Lars) and the Foreseer only. Use when you need directional input fast.

---

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| **Board** | Board governs strategy and standards. Guild develops product. Guild findings feed Board D8 (Design) and D5 (Sound). |
| **Synth Seance** | Seance gives historical genius perspective. Guild gives market and user perspective. Run Seance first for soul, Guild for roadmap. |
| **Sweep** | Sweep fixes what exists. Guild defines what should exist next. |
| **Historical Society** | Society ensures docs are accurate. Guild generates the product decisions that docs need to capture. |
| **New XO Engine** | Guild output can seed a new engine's identity and feature set before /new-xo-engine is invoked. |

---

## Values

1. **The producer is always right about what they feel** — but they're describing symptoms, not prescribing cures
2. **Genre crossing is the new frontier** — the most interesting feature requests come from two specialists who want the same thing for different reasons
3. **The Foreseer isn't a prophet** — they're a pattern recognizer who reads the direction, not a crystal ball
4. **Ops debt is product debt** — a feature that ships buggy costs more than one that ships late
5. **XPN export is underrated** — every genre specialist who performs live cares about it; it's not a tool feature, it's a product feature
