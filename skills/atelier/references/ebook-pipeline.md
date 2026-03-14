# E-Book Pipeline — Chronicle's Guide

## Philosophy

The e-book is NOT a blog post collection. It's a coherent book that happens to share DNA with the blog. A reader who has never visited XO-OX.org should be able to pick up the e-book and experience a complete, satisfying narrative. A reader who has read every blog post should find new connections, deeper context, and a through-line they didn't see in the individual posts.

## Phase Structure

Blog posts accumulate into **phases**. Each phase has:

1. **A thematic arc** — not arbitrary groupings, but a natural narrative progression
2. **A logical endpoint** — a milestone, a resolution, a turning point
3. **Enough material** — typically 8-15 blog posts worth of source material

### Example Phase Boundaries

- **Phase 1**: "The Origin" — The first 9 engines, from Instability Synth to XOmnibus. How one experiment became a universe.
- **Phase 2**: "The Deep Water" — Engines 10-18, the Prism Sweep, the Seances. How the universe became self-aware.
- **Phase 3**: "The Full Column" — Mythology completion, the water column atlas, feliX-Oscar resolution. How the universe found its story.

These are illustrative — Chronicle determines actual phase boundaries based on the content that exists.

## E-Book Creation Process

### Step 1: Phase Assessment
Chronicle reviews all blog posts in the candidate phase:
- Map the topics and their natural connections
- Identify the through-line (what story do these posts tell together?)
- Note gaps — what's missing that the blog didn't cover but the book needs?
- Identify "side quest" opportunities (see below)

### Step 2: Architecture
Design the book structure:

```
FRONT MATTER
- Title page
- Table of contents
- Introduction (NEW — not from any blog post)

MAIN CHAPTERS (derived from blog posts but restructured)
- Each chapter synthesizes 1-3 blog posts into a cohesive narrative
- Transitions between chapters are written fresh
- Technical details can go deeper than the blog format allowed

SIDE QUESTS (interspersed between main chapters)
- "The Ghost Council Speaks" — a synthesizer history sidebar drawn from Seance findings
- "Under the Hood" — technical deep dive into a DSP concept
- "Genre Atlas" — how a specific music genre connects to the engines
- "The Obscure Frequency" — little-known synthesis history, forgotten instruments, hidden influences
- "From the Workshop" — behind-the-scenes design decision stories

BACK MATTER
- Appendix: Engine reference cards (name, accent, creature, polarity, key features)
- Appendix: Glossary of XO_OX terminology
- Appendix: The Water Column Atlas (visual reference)
- Acknowledgments
- Links back to XO-OX.org for the latest
```

### Step 3: Writing
Chronicle writes the book, following these principles:

**Voice**: The same warmth and depth as the Field Guide, but with the pacing of a book. Longer paragraphs where the subject deserves it. More room to breathe. The reader is settling in, not scanning.

**The Through-Thread**: Every chapter connects to the next. The reader should feel momentum — each section makes them want to read the next. The connection might be thematic ("this engine emerged because the last one couldn't do X"), chronological ("three weeks later"), or philosophical ("but what if sound could be silent?").

**Side Quests**: These are the book's secret weapon. They're the difference between "collected blog posts" and "a real book." Each side quest should:
- Connect to the surrounding chapters (placed strategically, not randomly)
- Bring in real-world context (actual synth history, genre movements, cultural moments)
- Feel like a delightful detour that enriches the main journey
- Be 1,000-2,000 words (shorter than main chapters)

**Technical Depth**: The book can go deeper than the blog. A blog post might say "XOuroboros uses a Lorenz attractor." The book explains what a Lorenz attractor IS, why Lorenz discovered it, how it relates to weather prediction, and why it sounds like controlled chaos when you map it to sound parameters. The reader should finish the book knowing more about synthesis than when they started.

### Step 4: Production

**HTML version**: A beautifully formatted page on XO-OX.org with:
- Chapter navigation
- The full reading experience in-browser
- Responsive design (reads well on phones)
- Engine accent colors used as chapter markers

**EPUB version**: A proper e-book file that loads correctly on:
- Kindle (via .epub or .mobi conversion)
- Apple Books
- Any standard e-reader
- The EPUB should include:
  - Proper metadata (title, author "XO_OX Designs", description, cover)
  - Table of contents with working links
  - Embedded images where relevant (engine gallery cards, water column diagram)
  - Clean typography that respects e-reader settings

**Generation approach**: Use a Python script or Node tool to convert the structured markdown into EPUB format. Libraries like `pandoc` or `ebooklib` (Python) can handle this. The script should live in the site's `tools/` directory for repeatability.

### Step 5: Publication
- Add the e-book page to XO-OX.org navigation
- Create a dedicated landing page with:
  - Book cover image (HT designs this)
  - Synopsis
  - "Read Online" button → HTML version
  - "Download E-Book" button → EPUB file
  - "Download for Kindle" button → .mobi file (if generated)
- Update the Field Guide hub to reference the e-book
- Herald announces the e-book in the product update feed

## Phase Tracking

Chronicle maintains awareness of where the current phase stands:
- How many posts exist in the current phase?
- What's the emerging through-line?
- Are there enough side quest opportunities?
- Is there a natural endpoint approaching?

When a phase is ready, Chronicle proposes e-book creation to the user with:
- Proposed title
- Chapter outline
- Estimated scope
- Side quest candidates
