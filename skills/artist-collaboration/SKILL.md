---
name: artist-collaboration
description: Artist Collaboration Framework — manages guest producer collaborations for co-designed XO_OX preset packs and co-created content. Structures the collaboration workflow, manages preset submission/review/integration, generates collaboration agreements, and produces co-branded content. Use when the user says 'artist collaboration', 'guest producer', 'collab pack', 'collaboration framework', 'co-designed pack', 'guest presets', 'producer collab', 'artist partnership', 'collaboration agreement', 'co-branded', wants to work with an external producer on a preset pack, wants to design a guest artist series, or wants a structured workflow for receiving and publishing collaborator contributions.
---

# Artist Collaboration Framework

**XO_OX sounds best when other minds are in the room.**

Guest producer collaborations produce sounds that HT Ammell wouldn't make alone — and that's the point. The Artist Collaboration Framework manages the entire lifecycle: from initial outreach through preset creation, review, integration, and co-branded release.

---

## The Collaboration Types

| Type | Description | Producer's Role | HT's Role |
|------|-------------|-----------------|-----------|
| **Signature Pack** | 20-40 presets, one producer's vision | Creates all presets | QA, technical integration |
| **Co-Design Pack** | Blended authorship, both contributing | Creates 50% of presets | Creates 50%, curates |
| **Artist Edition** | An existing engine or pack with guest customization | Selects/customizes presets | Technical, publishing |
| **Guest Blueprint** | Producer provides creative brief, HT implements | Provides concept, DNA directions | Implements in DSP |

---

## Collaboration Lifecycle

### Phase 1: Matchmaking
**Criteria for ideal collaborators:**
- Active on MPC or major DAW
- Sound design aesthetic compatible with XO_OX's engine territory
- Genuine interest in the specific engine(s), not just "exposure"
- Community presence (Signal, YouTube, Soundcloud) — the collaboration reaches their audience too

**Outreach template:**
```
Hi [Name],

I'm HT Ammell — I make the XO_OX Designs synthesizer plugins for MPC and DAW.

I've been following your work on [specific context — track, video, community thread]. [Specific thing that makes them a good fit] — that's exactly the kind of territory [engine name] was designed for.

I'm building a guest producer preset pack for [engine name] and I'd love to collaborate. Here's what I have in mind:
- [Brief description of the pack concept]
- [Timeline]
- [What they'd receive — credit, revenue share if applicable, featured position on site]

Would you be open to a quick call to talk about it?

HT Ammell
XO_OX Designs | XO-OX.org
```

### Phase 2: Brief
Once a collaborator agrees, produce a Creative Brief:

```
COLLABORATION BRIEF: [Pack Name]
Collaborator: [Name]
Engine(s): [Engine list]
Timeline: [Dates]

The Vision:
[1-2 paragraphs describing the sonic territory this pack should cover]

What We're Looking For:
- Mood distribution: [specific moods to emphasize]
- DNA targets: [bright / dark / textural / etc.]
- Genre territory: [genres this should serve]
- # of presets: [target count]

What to Avoid:
- [Specific sounds that already exist in the official library]
- [Any directions that conflict with brand doctrine]

Technical Requirements:
- File format: .xometa JSON
- Engine: [name] | Parameter prefix: [prefix_]
- Schema version: [current version]
- Each preset needs: name, description, mood, DNA values, tags

Resources:
- Engine documentation: [Field Guide link]
- Preset template: [provide a template .xometa file]
- Parameter list: [attach or link]

Questions? [contact method]
```

### Phase 3: Review
Apply the same review process as `/community-curator` with adjusted expectations:
- Signature collaborator presets have a higher quality bar than community submissions
- Sound character matters more than technical compliance (they need help getting the format right, not the sound)
- Provide more editorial feedback — this is a partnership, not a gatekeeper relationship

**Feedback approach:**
- Be specific about what works
- Be constructive about what to adjust
- Offer to implement technical corrections yourself (adjust parameter values, fix schema issues)
- Preserve their sound vision even when making adjustments

### Phase 4: Integration
Technical integration follows the same process as official preset creation:
- Run `/preset-qa` on all submitted presets
- Fix any schema or technical issues
- Add attribution in description + author fields
- Organize into the 6 moods
- Verify DNA values match sound character

### Phase 5: Release
Coordinate the release with the collaborator:
- They announce to their audience on their channels
- HT announces to XO_OX community
- The pack page on XO-OX.org features the collaborator prominently
- Coordinated timing: both posts go up simultaneously for maximum impact

---

## Pack Page Content

For the site pack page, a collaboration needs:

**Collaborator bio** (100 words): Written by the collaborator or with their input
**Pack philosophy** (150 words): Why this collaboration, what makes these sounds distinctive
**Featured preset** (1 preset highlighted with story): The pack's signature sound and how it was made
**Audio preview**: 60-90 second demo mix using only collaboration presets

---

## Collaboration Agreement Framework

A simple written agreement (not a formal legal document unless volumes are significant):

```
XO_OX COLLABORATION AGREEMENT

Between: HT Ammell (XO_OX Designs) and [Collaborator Name]

Pack: [Pack Name]
Engine: [Engine Name]
Delivery date: [Date]

Grant:
[Collaborator Name] grants XO_OX Designs the right to distribute the submitted presets as part of [Pack Name], both as a free download and as part of any future XO_OX product bundles.

Attribution:
[Collaborator Name] will be credited on the pack download page, in the preset description fields, and in any marketing materials for [Pack Name].

Revenue:
[Option A: Pack is free, no revenue] This collaboration is unpaid. [Collaborator Name] receives credit and exposure.
[Option B: Pack is paid] Revenue is split [X%/Y%] after payment processing fees.

Termination:
Either party may withdraw from the collaboration before final integration. Withdrawn presets will not be used.
```

---

## Arguments

- (none) — collaboration status overview: any active collaborations, pending reviews, released packs
- `outreach: {producer name}` — write a personalized outreach message for a specific producer
- `brief: {pack name}` — generate a Creative Brief for a new collaboration
- `review: {batch}` — run the collaboration preset review process
- `release: {pack name}` — generate all release content (pack page copy, announcement posts, attribution)
- `agreement: {collaborator name}` — generate a collaboration agreement
- `audit` — assess which XO_OX engines are best positioned for guest collaborations right now
