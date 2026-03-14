# Project Memory

## Active Project: XOverdub (ALL PROTOCOLS COMPLETE — March 2026)
- **Repo**: `~/Documents/GitHub/XOverdub/` | JUCE 8.0.12, CMake + Ninja
- **Build**: `cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release && cmake --build build`
- **Identity**: Dub synth + performance FX | Signal: Voice → Send VCA → Drive → Tape Delay → Spring Reverb → Master
- **38 params**, 40 presets, 4 pads (FIRE, XOSEND, ECHO CUT, PANIC) | auval PASS, ready for v1.0
- **Playbook**: All 10 protocols complete, 7 reusable modules documented
- **Next**: Sound testing → commit + ship

---

## Project: XOdyssey (COMPLETE — March 2026)
- **Repo**: `~/Documents/GitHub/XOdyssey/` | JUCE 8.0.12 | v0.7.0
- **Note**: Wavetable osc mode is placeholder (renders sine) — v2 work
- See [xodyssey-engine.md](xodyssey-engine.md) for full architecture

---

## Project: XOblongBob (BUILD COMPLETE — March 2026)
- **Repo**: `~/Documents/GitHub/XOblongBob/` | JUCE 8.0.4, CMake + Make
- **Build**: `cmake -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build`
- **72 source files**, 167 presets, Apple Liquid Glass UI, PlaySurface chord/scale modes
- **JUCE 8 gotchas**: atomic .load() for jmax, 1-param keyPressed, apvts.processor not getProcessor()
- **Remaining**: Smoke test, preset listening pass, MPC export validation, VST3 DAW test

---

## Project: XOverworld (DSP + UI COMPLETE — March 2026)
- **Repo**: `~/Documents/GitHub/XOverworld/` | JUCE 8.0.4, CMake + Ninja
- **Identity**: Chip synth — NES 2A03 + Genesis YM2612 + SNES SPC700 | `ow_` prefix
- **~67 params**, 8-voice poly, ERA crossfade, CRT UI, 15 color themes, 13 glitch types
- **CMake gotcha**: OSX_ARCHITECTURES must come BEFORE project(), need LANGUAGES C CXX
- **Status**: auval PASS, preset expansion in progress (target 120)

---

## Project: XOpossum → BITE (ALL 7 PHASES COMPLETE — March 2026)
- **Repo**: `~/Documents/GitHub/XOppossum/` | JUCE + CMake + Ninja | auval PASS
- **Identity**: Bass-forward character synth | Gallery code: OVERBITE | Accent: Fang White `#F0EDE8`
- **Param IDs**: Plain names (`filter_cutoff`) — NOT `poss_` prefixed. 342 presets use plain names.
- **XOmnibus**: Adapter will translate `poss_` → plain names. Do NOT rename params.
- **Plugin codes**: PLUGIN_CODE=Xpos, PLUGIN_MANUFACTURER_CODE=Xoox
- **Next**: Write XOpossumAdapter.h for XOmnibus gallery

---

## Project: XOpal → OPAL (COMPLETE — integrated into XOmnibus)
- **Repo**: `~/Documents/GitHub/XOpal/` | Granular synthesis
- **Gallery code**: OPAL | Accent: `#A78BFA` | 150 factory presets in 6 categories (Batch 1: 100, Batch 2: 50)
- **Key coupling**: OVERWORLD→OPAL, DRIFT→OPAL, OPAL→DUB
- **OpalEngine include fix**: Use `Source/DSP/` prefix in XOmnibus (not `DSP/`) — macOS FS collision with XOverworld `src/dsp/`

---

## XOmnibus (Active — March 2026)
- **Repo**: `~/Documents/GitHub/XO_OX-XOmnibus/` | 24 engines working (29 dirs, 5 Pentagon stubs broken), auval PASS
- **Presets**: 1,839+ total (counts expand frequently — verify against source before acting on specific numbers)
- **All 6 moods covered** for all engines | Gallery Model UI built
- **Master spec**: `Docs/xomnibus_master_specification.md`
- **Engine colors**: See CLAUDE.md engine table for all 31 engine accent colors (canonical source)
- **P10**: MasterFXChain (Tape Sat → LushReverb → Bus Compressor) — COMPLETE
- **P12**: PresetManager, PresetBrowserStrip, engine tile menu, window 880×562 — COMPLETE
- **Prism Sweep**: 10 rounds complete | D001-D005 RESOLVED fleet-wide | 21/23 aftertouch
- **Roadmap**: See `Docs/xomnibus_engine_roadmap.md` | BITE + OPAL + ONSET all now complete

---

## XOnset → ONSET (ALL 5 PHASES COMPLETE — March 2026)
- **Location**: `Source/Engines/Onset/OnsetEngine.h` (1534 lines) in XOmnibus repo
- **111 params**, 8 synthesis voices (Kick, Snare, CHat, OHat, Clap, Tom, Perc, FX)
- **115 factory presets**, 4 macros: MACHINE, PUNCH, SPACE, MUTATE
- See XPN tools for drum export: [xpn-tools.md](xpn-tools.md)

---

## XO_OX Aquatic Mythology (March 2026)
- Unified brand mythology: water column atlas, feliX-Oscar polarity, evolutionary lineage
- 18 engine identity cards (11 engines still need cards) | See [aquatic-mythology.md](aquatic-mythology.md)

---

## Theorem Results (Pi Day 2026) — All 3 Approved
- **XOvertone (OVERTONE)** — Continued fractions spectral engine | Accent: `#A8D8EA` | The Nautilus
- **Knot Coupling (KNOT)** — Topological bidirectional coupling mode | Accent: `#8E4585` | The Kelp Knot
- **XOrganism (ORGANISM)** — Cellular automata generative engine | Accent: `#C6E377` | The Coral Colony
- See [theorem-2026-03-14.md](theorem-2026-03-14.md) for full concepts

---

## New Engines — Status as of March 2026

### Constellation Fast Track (scaffold builds complete, adapters committed)
- **XOhm (OHM)** — [xohm-engine.md](xohm-engine.md) — Hippy Dad jam, MEDDLING/COMMUNE axis
- **XOrphica (ORPHICA)** — [xorphica-engine.md](xorphica-engine.md) — Microsound harp, siphonophore
- **XObbligato (OBBLIGATO)** — [xobbligato-engine.md](xobbligato-engine.md) — Dual wind, BOND macro
- **XOttoni (OTTONI)** — [xottoni-engine.md](xottoni-engine.md) — Triple brass, GROW macro
- **XOlé (OLE)** — [xole-engine.md](xole-engine.md) — Afro-Latin trio, DRAMA macro
- **NOTE**: These 5 have broken `REGISTER_ENGINE` macros — need centralized registration in XOmnibusProcessor.cpp

### Concept Phase (no source code yet)
- **XOstinato (OSTINATO)** — [xostinato-engine.md](xostinato-engine.md) — Communal drum circle
- **XOpenSky (OPENSKY)** — [xopensky-engine.md](xopensky-engine.md) — Euphoric shimmer, pure feliX
- **XOceanDeep (OCEANDEEP)** — [xoceandeep-engine.md](xoceandeep-engine.md) — Abyssal bass, pure Oscar
- **XOuïe (OUIE)** — [xouie-engine.md](xouie-engine.md) — Duophonic hammerhead, STRIFE↔LOVE axis

---

## XO_OX Web Presence (March 2026)
- **Domain**: XO-OX.org | 7 pages: index, packs, guide, aquarium, guide-oracle, manifesto, updates
- **Field Guide**: 14 published posts (~47K words), 16 planned
- **Signal**: Product update feed (5 inaugural posts)
- **Aquarium**: Water column atlas — 29 engines mapped across 9 depth zones
- **PENDING**: Record 20 hero preset audio clips — see [site-sample-recordings.md](site-sample-recordings.md)
- **PENDING**: Create XObese .xpn bundle + deploy to XO-OX.org
- **PENDING**: Update Patreon URL (currently placeholder `patreon.com/xoox`)
- See [xo-ox-domain.md](xo-ox-domain.md)

---

## XPN & MPC Export Tools
- See [xpn-tools.md](xpn-tools.md) for XPN suite, keygroup exporter, and XObese expansion

---

## Previous Project: Instability Synth (COMPLETE)
- `~/Desktop/synth-plugin` | 99 presets, 33 bugs fixed | See [synth-build-learnings.md](synth-build-learnings.md)

---

## Constellation Fast Track Build (Active — March 2026)
- **Tracker**: [constellation-build-status.md](constellation-build-status.md) — SP1-SP7 status table
- **Spec**: `~/Documents/GitHub/XO_OX-XOmnibus/docs/superpowers/specs/2026-03-14-constellation-fast-track-design.md`
- SP1-SP6 ✅ complete (all 5 engine scaffolds build) | SP7.1 ✅ adapters committed | SP7.2 CMake integration NEXT
- **BLOCKER**: 5 engines use broken `REGISTER_ENGINE` macro (namespace-qualified names fail token paste)

---

## V1 Scope Decision (2026-03-14)
- **Everything that exists as of 2026-03-14 EOD is V1** — nothing deferred
- Only new ideas from 2026-03-15 onward can be V2
- See [strategic-decisions-2026-03-14.md](strategic-decisions-2026-03-14.md) for full decisions

## User Preferences
- DAW: Akai MPC on macOS | Wants experimental, production-ready presets
- Bold iconic visual design | Character instruments over feature-maximal workstations
- **Plugin UI**: Light mode dominant, flexible | **Site**: HT Ammell creative control (dark ocean approved)
- Cost-conscious: ~80% monthly usage typical
- **Seance framing**: Legends possess vessels who interpret wisdom — quotes attributed to characters, homage via "inspired by"

## Model & Effort Guide
- **Opus + High**: novel DSP, new engine design, complex architecture decisions
- **Sonnet + Medium** (DEFAULT): JUCE UI, bug fixes, param wiring, build validation
- **Sonnet + Low**: JSON presets, git commits, single-file edits, read-only research
