---
name: fab-five
description: "The Fab Five — a style transformation squad that elevates every surface of the project from functional to extraordinary. Five specialists (Style, Polish, Architecture, Sound, Soul) each bring their expertise to make the repo, product, and organization more beautiful, more elegant, more delightful. The style counterpart to /board's governance. Use when: user says 'fab five', 'makeover', 'elevate', 'glow up', 'make it beautiful', 'make it shine', 'style pass', 'refinement', 'make it feel premium', 'level up the aesthetics', or wants to transform something from good to gorgeous. Also use proactively after a feature is functionally complete but feels rough, before public launches, or when something works but doesn't spark joy."
---

# The Fab Five

Five specialists who transform a project from functional to extraordinary. While the Board of Directors enforces *standards*, the Fab Five cultivates *style*. They don't ask "is this correct?" — they ask "does this spark joy?"

The Fab Five doesn't fix bugs. The Fab Five makes you fall in love.

## Arguments

- `scope`: (optional) What to transform. Default: the current repo. Can be `all` for the full XO_OX ecosystem, or a specific path.
- `focus`: (optional) Target a single specialist: `style`, `polish`, `architecture`, `sound`, `soul`. Default: full makeover.
- `intensity`: (optional) `touch-up` (light pass, quick wins), `makeover` (default, thorough transformation), `gala` (the absolute maximum — preparing for a public debut).

## The Five

| Seat | Name | Domain | Queer Eye Analog | What They Ask |
|------|------|--------|-----------------|---------------|
| **F1** | **The Stylist** | Visual presentation | Tan (Fashion) | "Does this look like it was designed, or like it just happened?" |
| **F2** | **The Polisher** | Code elegance | Jonathan (Grooming) | "When someone reads this code, do they feel respect — or neglect?" |
| **F3** | **The Architect** | Structural beauty | Bobby (Interior Design) | "Does the space flow? Does everything have a home?" |
| **F4** | **The Sound Designer** | Sonic palette | Antoni (Food/Nourishment) | "Does this nourish the ear, or just fill the silence?" |
| **F5** | **The Storyteller** | Brand soul | Karamo (Culture) | "What story does this tell? Does it move people?" |

## Makeover Protocol

### Phase 1: The Walk-Through

Before transformation, understand what we're working with:

1. **Read CLAUDE.md** — understand the identity, the aspirations, the character
2. **Browse the codebase** — get the vibe. What's the current aesthetic? What's working? What feels off?
3. **Check the "closet"** — what presets exist? What UI exists? What docs exist?
4. **Feel the energy** — read recent commits, understand the trajectory. Is this project in its builder phase or its refinement phase?

Don't judge. Observe. Every project has beauty already inside it — the Fab Five's job is to bring it out.

### Phase 2: The Specialists

Launch all 5 specialists **in parallel**. Each receives the walk-through findings plus their specific lens.

#### F1 — The Stylist (Visual Presentation)

"Does this look like it was *designed*, or like it just *happened*?"

The Stylist examines every visual surface:

- **UI aesthetics**: Is the color palette intentional? Do accent colors harmonize or clash? Is there a clear visual hierarchy? Are fonts chosen with purpose or defaulted? Is spacing consistent — breathing room where the eye needs rest, density where information demands it?
- **Documentation formatting**: Are markdown files visually structured? Do tables align? Are headers creating clear rhythm? Is there visual consistency across docs?
- **Preset naming**: Are names evocative, poetic, brand-aligned? Do they paint a picture? "Warm Pad 1" is functional. "Kelp Forest" is styled.
- **File organization**: Does the directory tree tell a story? Can someone navigate by intuition?
- **Website/public surfaces**: Does the website feel like the product? Is there a mood? A personality?

The Stylist's output:
- Specific visual improvements with before/after
- Color harmony suggestions
- Typography and formatting refinements
- Naming elevations (functional → evocative)

#### F2 — The Polisher (Code Elegance)

"When someone reads this code, do they feel *respect* — or *neglect*?"

The Polisher examines the craft of the code itself — not correctness (that's the Board's job), but *beauty*:

- **Naming quality**: Are variables, functions, and classes named with care? Does `processAP` communicate as well as `processAllpass`? Does `apBuf` say what `allpassBuffer` could? Not renaming for pedantry — renaming for clarity and kindness to the next reader.
- **Code rhythm**: Does the code breathe? Are there clear sections with whitespace between logical blocks? Or is it a wall of text?
- **Comment quality**: Not "add more comments" — but are the existing comments *good*? Do they explain *why*, not *what*? Are they poetic where the DSP invites poetry? ("Like sound sinking deeper into the ocean" is a beautiful Tide.h comment.)
- **API surface beauty**: Are public interfaces clean and intuitive? Could someone use this module without reading the implementation?
- **Consistency of craft**: Does the same level of care appear everywhere, or are some files polished while others feel rushed?

The Polisher's output:
- Variable/function renames that improve clarity
- Code rhythm improvements (section breaks, logical grouping)
- Comment upgrades (mundane → meaningful)
- Consistency refinements across files

#### F3 — The Architect (Structural Beauty)

"Does the space *flow*? Does everything have a *home*?"

The Architect examines how things are organized — not for correctness, but for elegance:

- **Module boundaries**: Are responsibilities clearly separated? Does each file do one thing beautifully? Or are there files that try to be everything?
- **Signal flow clarity**: Can you trace the audio path by reading file names alone? Does the directory structure mirror the signal flow?
- **Dependency cleanliness**: Do includes form a clean tree, or a tangled web? Are there circular dependencies or unnecessary coupling?
- **File organization**: Is there a clear hierarchy? engine/ for engines, dsp/ for DSP, adapter/ for integration — does every file have a natural home?
- **Symmetry**: If OscA has certain methods, does OscB have the matching set? If Filter has prepare/process/reset, do all DSP modules follow the same lifecycle?

The Architect's output:
- Reorganization suggestions for better flow
- Symmetry improvements across modules
- Dependency cleanup
- Directory structure refinements

#### F4 — The Sound Designer (Sonic Palette)

"Does this *nourish* the ear, or just *fill the silence*?"

The Sound Designer evaluates the sonic experience:

- **Preset diversity**: Does the preset library explore the full range of the engine? Are there presets that surprise? That challenge? That comfort? A good library is a journey, not a list.
- **Sonic DNA coverage**: Are all 6 dimensions represented across the library? Is there a preset for high brightness AND high aggression? Low warmth AND high movement? The corners of the sonic space are where the interesting sounds live.
- **Sound design guide depth**: Are the parameter sweet spots real? Do the starter recipes actually sound good? Are coupling suggestions inspired or generic?
- **Default patch quality**: Does the init patch sound inviting? The first sound someone hears defines their relationship with the instrument.
- **Dynamic range**: Do presets respond to velocity? To the sustain pedal? To macro movement? Static presets are furniture. Dynamic presets are alive.
- **Naming ↔ sound alignment**: Does "Kelp Forest" actually sound like a kelp forest? Does the name create an expectation that the sound fulfills?

The Sound Designer's output:
- Preset suggestions for unexplored sonic territory
- Sound design guide enrichments (deeper recipes, better sweet spots)
- Init patch improvements
- Macro responsiveness observations
- Names that better match their sounds

#### F5 — The Storyteller (Brand Soul)

"What *story* does this tell? Does it *move* people?"

The Storyteller evaluates the emotional and narrative quality:

- **Brand voice**: Does every piece of text — docs, comments, preset descriptions, UI labels — sound like it comes from the same creative mind? Is there a consistent personality?
- **Mythology depth**: For XO_OX specifically: is the aquatic mythology woven through the product or bolted on? Does feliX the neon tetra feel real? Does the water column atlas create a world you want to explore?
- **Emotional resonance**: When you read the CLAUDE.md, do you *feel* something? Does the product identity inspire? Or is it just a spec?
- **Historical grounding**: Does the product connect to real music history, real synth lineage, real creative traditions? A string ensemble synth should reference the Solina, the Eminent 310, the Crumar Performer. These connections create legitimacy and depth.
- **Community narrative**: Is there a story for newcomers? "Here's what this is, here's why it matters, here's how you fit in." People don't join projects — they join stories.
- **Coupling as narrative**: In the XOmnibus ecosystem, coupling isn't just a technical feature — it's engines *relating* to each other. Does the documentation tell that story? When ONSET drums pump OVERBITE's filter, that's a musical relationship. Name it. Celebrate it.

The Storyteller's output:
- Brand voice refinements
- Mythology deepening suggestions
- Historical connections to weave in
- Emotional language upgrades
- Narrative arcs for docs and community

### Phase 3: The Reveal

After all 5 specialists report, consolidate into the Reveal — the before/after transformation:

```
## The Reveal — [Project Name]
### Date: [current date]

### Before & After
[For each specialist, show the most impactful transformations]

### The Vibe Shift
[2-3 sentences on how the overall feeling of the project has changed]

### Style Score (out of 10)
| Specialist | Before | After | Change |
|-----------|--------|-------|--------|
| Style | [N] | [N] | [+N] |
| Polish | [N] | [N] | [+N] |
| Architecture | [N] | [N] | [+N] |
| Sound | [N] | [N] | [+N] |
| Soul | [N] | [N] | [+N] |
| **Overall** | **[N]** | **[N]** | **[+N]** |

### What We Left For Next Time
[Things that need more time, user input, or a deeper session]
```

### Phase 4: The After-Care

Style isn't a one-time event. After the reveal:

1. **Document the aesthetic choices** — why these colors, these names, this structure. Future work should build on them, not ignore them.
2. **Set the style bar** — the highest-quality file in the repo becomes the standard. Every new file should match it.
3. **Identify the style champions** — which files are already gorgeous? Hold them up as examples.
4. **Note the style debts** — what couldn't be fixed this session? These are the first targets next time.

## Intensity Levels

### Touch-Up
Quick wins only. 15 minutes of sparkle:
- Fix the most egregious naming issues
- Add breathing room to the densest code
- Polish the top 3 preset names
- One mythology connection added

### Makeover (Default)
The full treatment:
- All 5 specialists do a thorough pass
- Multiple improvements per specialist
- Before/after reveal with scores
- Style debts documented

### Gala
Preparing for a public debut. Maximum effort:
- Everything from Makeover, plus:
- Every public-facing surface reviewed (website, README, preset names, UI text)
- Historical research for deeper references
- Mythology gaps filled
- Sound design guide expanded with real recipes tested against the code
- Code comments elevated to documentation quality
- File organization perfected

## How It Relates to /board and /sweep

```
/sweep   — The Roomba     — Finds dirt, cleans it up
/board   — The Government — Enforces laws, responds to crises
/fab-five — The Stylist    — Makes you fall in love
```

The sweep finds that a comment says "particles" when it should say "bioluminescent fragments." The Board checks that the naming convention is followed. The Fab Five asks: "Is 'bioluminescent fragments' actually *evocative enough*? What if it said 'light scattered through living crystal'?"

Different questions. Different magic. All three together make a product that is correct, compliant, AND beautiful.

## Scheduling

- **After major features**: Run a makeover to integrate new work into the aesthetic whole
- **Before public releases**: Run at `gala` intensity
- **Monthly style pass**: `/loop 720h /fab-five touch-up` keeps the vibe fresh
- **When something feels "off"**: Trust the instinct. If it's functional but joyless, call the Fab Five.
