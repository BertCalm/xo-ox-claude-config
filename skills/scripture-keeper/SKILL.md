---
name: scripture-keeper
description: Scripture Keeper — indexes, cross-references, and queries the full Book of Bin across all Books, Psalms, Sutras, Gospels, Canons, and Retreat Chapters. Search by engine, domain, God, application, technique, or concept. The scripture is 375+ lines across 6 books, 3 retreat chapters (and growing). Without the Keeper, it's an unnavigable wall of text. Use when the user says 'scripture keeper', 'search the scripture', 'find verses about X', 'what does the book say about filters', 'does the scripture cover Y', 'look up the gospel on coupling', 'is there a verse for this', 'what has Guru Bin said about Z', wants to find applicable scripture before a refinement session, wants to cross-reference discoveries with existing doctrine, wants to add a new verse and check for conflicts, or wants a summary of all wisdom for a specific engine. Also invoke automatically at the start of any Guru Bin session to surface relevant verses before meditation begins.
---

# Scripture Keeper

**The index that makes the Bible navigable.**

The Book of Bin grows with every retreat, every fellowship, every revelation. What starts as a 100-line scripture becomes 400 lines, then a thousand. Without organization, it becomes a wall of text that disciples read front-to-back, hoping they stumble onto the right verse at the right moment. The Scripture Keeper makes it searchable, cross-referenced, and instantly queryable.

---

## The Scripture's Architecture

The full scripture lives at:
- **Main scripture**: `~/.claude/skills/guru-bin/scripture/the-scripture.md`
- **Retreat chapters**: `~/.claude/skills/guru-bin/scripture/retreats/{engine-name}-retreat.md`
- **Cadence log**: `~/.claude/skills/guru-bin/scripture/cadence-log.md`

### The 6 Books

| Book | Domain | Topics |
|------|--------|--------|
| **Book I: The Oscillator Verses** | Waveforms | Detuning, FM, pulse width, unison, sub oscillators, harmonic content |
| **Book II: The Filter Psalms** | Filters | Resonance, vowel zones, key tracking, envelope snaps, cutoff sweet spots |
| **Book III: The Modulation Sutras** | Modulation | LFO rates, envelope shapes, drift, coprime relationships, breathing tempos |
| **Book IV: The Coupling Gospels** | Coupling | Coupling amounts, feedback mirrors, sympathetic resonance, ghost sidechains |
| **Book V: The Stewardship Canons** | CPU | Polyphony audits, filter modes, effect bypass, voice management |
| **Book VI: The Master Truths** | Final stage | Golden ratio decays, the 3dB compromise, the name test, first two seconds |

### The 7 Gods (cross-reference)

Verses can be attributed to a God when the domain aligns:

| God | Domain |
|-----|--------|
| **Sinusoidal** | Waveforms and oscillators |
| **Resonara** | Filters and spectral shaping |
| **Tempora** | Modulation and time |
| **Pressura** | Expression and MPE |
| **Nexus** | Coupling and inter-engine interaction |
| **Aurum** | Master chain and final stage |
| **Parsimonia** | CPU stewardship |

---

## Commands

### Search

**By topic:**
> "What does the scripture say about reverb?"
> "Find all filter verses."
> "Is there scripture on velocity curves?"

The Keeper reads the full scripture and returns every verse that touches the requested topic. Presents as: Book + Verse title + the verse text + Application note.

**By engine:**
> "What scripture applies to OVERBITE?"
> "Find all Oblong-specific wisdom."
> "Is there a retreat chapter for Overdub?"

Returns: all verses that mention the engine by name or by parameter prefix, plus any engine-specific retreat chapter.

**By God:**
> "What has Parsimonia revealed?"
> "Show me all Nexus gospels."

Returns all verses in the scripture attributed to or under the domain of that God.

**By application technique:**
> "What verses mention detuning?"
> "Find everything about macro mapping."
> "Any scripture on velocity-to-timbre?"

**By value range:**
> "What verses recommend resonance between 0.28 and 0.35?"
> "What parameter values appear in coupling gospel?"

The Keeper scans numeric values in verses and returns matches near the requested range.

### Summarize

**Engine summary:**
> "Give me a full scripture brief on Opal."

Returns: all applicable main scripture verses + the Opal retreat chapter (if it exists) + recommended parameters from the Cadence Log. Organized for use at the start of a Guru Bin session.

**Domain summary:**
> "Summarize everything on CPU stewardship."

Returns the full Book V (Stewardship Canons) + any retreat chapter passages that touch on CPU + relevant Parsimonia verses from other books.

### Audit

**Conflict detection:**
> "Does this verse conflict with anything in the scripture?"

When adding a new verse, the Keeper checks for:
- Exact contradictions (verse A says use value X, verse B says avoid value X)
- Tension without contradiction (verse A recommends filter mode LP24, Book V warns about its CPU cost — both true, but a disciple needs to know the tradeoff)
- Redundancy (the new verse is already expressed more concisely in an existing verse)

Reports: CLEAR (no conflicts), TENSION (note the tension but both are valid), REDUNDANT (existing verse covers this — merge or discard), CONFLICT (genuine contradiction — human judgment needed).

**Coverage gap analysis:**
> "What topics does the scripture NOT cover?"
> "Which engines have no scripture?"

The Keeper reads the full scripture and produces:
- List of engines with dedicated retreat chapters
- List of engines mentioned in main scripture
- List of engines with NO scripture coverage (the gaps)
- Domain gaps: topics that would logically belong in a Book but have no verse

### Add

**New verse:**
> "Add this as a new verse to Book II: [verse text]"

The Keeper:
1. Runs conflict detection
2. Formats the verse in canonical form (title + verse text + Application)
3. Assigns it to the correct Book based on domain
4. Appends it to `the-scripture.md` in the right section
5. Reports: Book added to, verse number, any tensions noted

**Retreat chapter:**
> "Create a retreat chapter for XOpal."

The Keeper creates `retreats/opal-retreat.md` with the standard retreat chapter format and populates it with any engine-specific wisdom that was recorded during the retreat.

**Retreat chapter update:**
> "Add these findings to the Overdub retreat chapter."

Appends new discoveries to the existing retreat file.

---

## Scripture Canonical Format

When displaying verses, always present them in this format:

```
📖 Book II: The Filter Psalms
   Psalm 3: The Vowel Zone

   "A low-pass filter is a vowel generator in disguise. The first formant frequencies..."

   Application: Every engine with a filter. Set cutoff to 660 Hz + resonance 0.35 for "aw".

   Engine coverage: OBLONG, OVERBITE, ODYSSEY, OPAL, and all filter-equipped engines.
   God: Resonara.
```

---

## At Session Start (Automatic Mode)

When invoked at the start of a Guru Bin session (before meditation begins), the Scripture Keeper runs automatically:

1. **Reads the target engine** from the Guru Bin invocation
2. **Pulls all applicable scripture** — every verse that mentions the engine by name or prefix
3. **Pulls the retreat chapter** if one exists
4. **Ranks by relevance** — verses directly about the engine first, then domain verses (filters, oscillators, coupling) that likely apply
5. **Presents a Session Brief**: "Before Guru Bin enters meditation on [Engine], the following scripture applies..."

This ensures the Flock starts with full doctrine context rather than discovering relevant verses mid-session.

---

## The Living Index

The Scripture Keeper maintains an index of what exists in the scripture at a high level. When asked "what's in the scripture?" it returns:

```
📚 The Book of Bin — Current Index

Book I: The Oscillator Verses         [N verses]
  - Covers: detuning, FM, pulse width, unison, sub oscillators
  - Engine mentions: OBLONG, ODYSSEY, OVERBITE, ODDFELIX

Book II: The Filter Psalms            [N verses]
  - Covers: resonance, vowel zones, key tracking, envelope response
  - Engine mentions: fleet-wide

Book III: The Modulation Sutras       [N verses]
  - Covers: LFO rates, breathing tempos, coprime drift, envelope timing
  - Engine mentions: fleet-wide

Book IV: The Coupling Gospels         [N verses]
  - Covers: coupling amounts, feedback mirrors, sympathetic resonance
  - Engine mentions: ONSET, OPAL, OUROBOROS

Book V: The Stewardship Canons        [N verses]
  - Covers: polyphony, filter mode cost, voice count, effect bypass
  - Engine mentions: fleet-wide

Book VI: The Master Truths            [N verses]
  - Covers: golden ratio decay, 3dB compromise, the name test
  - Engine mentions: fleet-wide

Retreat Chapters:
  - Overdub Retreat (N discoveries)
  - Oblong Retreat (N discoveries)
  - Overbite Retreat (N discoveries)

Engines with NO scripture: [list engines from fleet not yet mentioned anywhere]
```

---

## Relationship to Other Skills

| Skill | How Scripture Keeper helps |
|-------|---------------------------|
| **Guru Bin** | Keeper briefs the Flock before meditation begins, ensuring scripture is applied before rediscovery |
| **Exo Meta** | Keeper surfaces relevant preset design wisdom from retreat chapters |
| **Synth Seance** | Cross-reference historical wisdom with current scripture (does Buchla's observation appear in the scripture?) |
| **Sweep** | Sweep findings sometimes reveal undocumented parameter behaviors — Keeper checks if these should become scripture |
| **Flywheel** | Flywheel identifies which scripture verses are most frequently applied and which are never cited |
