---
name: tutorial-studio
description: Tutorial Studio — designs and writes getting-started guides, first-hour walkthroughs, video scripts, and onboarding content for XO_OX plugins and the XOmnibus platform. Use when the user says 'tutorial studio', 'write a tutorial', 'getting started guide', 'first hour walkthrough', 'onboarding content', 'how would someone learn this', 'new user experience', 'tutorial for X', 'video script', 'beginner guide', 'first steps', wants to write documentation aimed at new users rather than experienced ones, is preparing materials for a launch, or wants to reduce the barrier to entry for a specific engine or feature.
---

# Tutorial Studio

**The gap between "downloaded" and "made a sound I love" is where XO_OX wins or loses.**

Tutorial content is producer retention. The Tutorial Studio designs and writes materials that move new users from confusion to capability — fast, satisfying, and in the XO_OX voice.

---

## Tutorial Types

| Type | Length | Format | When to Make |
|------|--------|--------|-------------|
| **Quickstart** | 300–500 words | Text/web | Every engine launch |
| **First Hour Walkthrough** | 1,200–2,000 words | Text/web | Every major platform release |
| **Video Script** | 5–10 min (750–1500 words) | Spoken script | Selected engines, launch moments |
| **Technique Card** | 150–250 words | Short form | In-app or site sidebar |
| **Reference Card** | 1 page | Structured | Parameter maps, keyboard shortcuts |
| **FAQ** | Varies | Q&A format | Post-launch, common questions |

---

## The XO_OX Learner Profile

New users are typically:
- MPC producers who've never used a traditional DAW plugin
- Experienced producers new to XO_OX specifically
- Adventurous experimenters who want to make sounds fast

They are NOT:
- Synthesis beginners (they know what an envelope is)
- Looking for manual-style exhaustive documentation
- Interested in technical details before they've heard the sound

**The rule**: Get them to a sound they love within the first 5 minutes. Everything else is optional.

---

## Quickstart Template

```markdown
# [ENGINE NAME] — First 5 Minutes

## Load a Preset
Open [ENGINE NAME] and try **[Preset Name]** from the [Category] mood. Hit a chord.
That's the baseline — now let's shape it.

## The Three Controls That Matter Most
[ENGINE NAME] has [N] parameters, but three control most of the character:

**[Control 1]** — [What it does in plain language]. Turn it up for [result], down for [result].
**[Control 2]** — [Same].
**[Control 3]** — [Same].

## Try This
[Specific action]: Open **[Preset Name]**, hold a low C, and slowly turn [Control 1] clockwise.
[What happens and why it matters — 1-2 sentences].

## Where to Go Next
Once you've explored the presets, check out [Field Guide post or technique].
For coupling ideas, [specific coupling] pairs beautifully with [ENGINE NAME].
```

---

## First Hour Walkthrough Template

Structure for XOmnibus or a major engine:

```markdown
# [PRODUCT] — Your First Hour

## Minute 1–5: Get a Sound
[Load instructions, first preset recommendation, what to listen for]

## Minute 5–15: The Architecture
[What makes this engine different from standard synthesis — explained through listening, not theory]
[Key controls — 3-5 at most]
[1 technique to try right now]

## Minute 15–30: Presets as Teachers
[How to use the preset library as an exploration tool]
[Recommended preset pairs that demonstrate contrast]
[What the 6 moods mean in practice]

## Minute 30–45: Make It Yours
[How to modify a preset — the most important parameters to tweak]
[Saving and organizing]
[First coupling experiment if platform-level]

## Minute 45–60: Where to Dig Deeper
[Field Guide links]
[Specific techniques to explore next]
[Community / Signal]
```

---

## Video Script Template

For 5–10 minute tutorial videos:

```
[TITLE: [ENGINE NAME] — Sound in 5 Minutes]

[HOOK — 0:00–0:30]
[Open with the SOUND, not the explanation. Play something great. Then say:]
"That's [ENGINE NAME]. Let me show you how I made it."

[SETUP — 0:30–1:00]
[Load the plugin. Brief what-is-this one sentence — avoid jargon]

[CORE DEMO — 1:00–4:00]
[Walk through 3-4 presets. For each: name it, play it, change one thing, explain what happened]

[KEY CONTROLS — 4:00–6:00]
[Point to 3 controls. Demo each one. Keep it under 30 seconds per control]

[MAKE SOMETHING — 6:00–8:00]
[Build something simple live. Start from a preset, make 3 changes, arrive at something new]

[WHERE TO GO NEXT — 8:00–end]
["For more, check out the Field Guide at XO-OX.org. Drop questions in the comments."]
```

---

## Voice Standards for Tutorial Content

Tutorial content uses the XO_OX voice but with specific adjustments:

**Do:**
- Lead with sound, not parameters
- Use producer-native language ("lay it back", "gets gnarly", "sits in the pocket")
- Give specific preset names and specific settings
- Celebrate the weird result, not just the intended one
- Keep technical context to the minimum needed to understand the action

**Don't:**
- Open with architecture ("OVERDUB uses a tape delay algorithm with...")
- Say "simply" — nothing is simple when you're new
- Give a parameter list before they've heard the engine
- Write for synthesis experts (they don't need tutorials)

---

## FAQ Generation Protocol

After a launch, common questions follow predictable patterns. The Studio generates a preemptive FAQ from:
1. The product's known edge cases
2. Standard new-user confusion points across XO_OX products
3. MPC-specific integration questions

Output format:
```
Q: [Question as a user would ask it — casual, natural]
A: [Direct answer, 2-3 sentences max. Link to Field Guide if relevant]
```

---

## Arguments

- `quickstart: {engine name}` — write a 5-minute quickstart guide
- `first-hour: {product}` — write a full first-hour walkthrough
- `video: {engine name}` — write a video tutorial script
- `faq: {product}` — generate a preemptive FAQ
- `technique: {technique name}` — write a short technique card
- `audit: {existing tutorial}` — review existing tutorial content against XO_OX voice and editorial standards
- (none) — assess what tutorial content is missing across all shipped products and recommend priority
