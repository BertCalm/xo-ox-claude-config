---
name: XOstinato Engine
description: XOstinato (OSTINATO) — communal world drum circle engine with 8 seats, 12 instruments, hybrid physical modeling, pattern system with live MIDI override
type: project
---

## XOstinato → OSTINATO (Phase 0 Complete — March 2026)
- **Repo**: To be created: `~/Documents/GitHub/XOstinato/`
- **Identity**: Communal drum circle engine — the fire at the center of the circle
- **Values**: Multiculturalism, peace, unity, love, community, family
- **Gallery code**: OSTINATO | Accent: Firelight Orange `#E8701A` | Prefix: `osti_`
- **Concept brief**: `~/Documents/GitHub/XO_OX-XOmnibus/Docs/concepts/xostinato_concept_brief.md`
- **Design doc**: `~/Documents/GitHub/XO_OX-XOmnibus/Docs/plans/2026-03-12-xostinato-design.md`
- **Status**: Phase 0 complete — design approved, ready for Phase 1 architecture

### Key Architecture
- **8 seats** in a circle, any of 12 instruments in any seat (no tradition restrictions)
- **12 instruments** × 3-4 articulations (48 total): Djembe, Dundun, Conga, Bongos, Cajón, Taiko, Tabla, Doumbek, Frame Drum, Surdo, Tongue Drum, Beatbox
- **Hybrid synthesis**: Exciter → Modal Membrane (6-8 resonators) → Waveguide Body → Radiation Filter
- **Pattern system**: 96 patterns (8 per instrument), authentic rhythmic traditions, live MIDI override with fade-back
- **4 macros**: GATHER (sync/tightness), FIRE (intensity/energy), CIRCLE (inter-seat interaction), SPACE (environment)
- **FX chain**: Circle Spatial Engine → Fire Stage → Gathering Reverb → Pulse Compressor
- **~140 canonical parameters** (112 per-seat + 28 global)
- **16 voices** (2 per seat for rolls/flams), CPU budget <25%
- **120 factory presets** across 7 categories
- **Key coupling**: OSTINATO×OVERDUB (World Dub), OSTINATO×OPAL (Scattered Gathering), ONSET×OSTINATO (Machine Meets Human)
- **Invoke Phase 1**: `/new-xo-engine phase=1 name=XOstinato identity="Communal drum circle engine — 8 seats, 12 world percussion instruments, hybrid physical modeling" code=XOst`
