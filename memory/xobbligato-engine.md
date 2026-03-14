---
name: XObbligato Engine
description: New XO_OX engine — dual wind instrument brothers with BOND relationship macro, post-punk energy, Peter and the Wolf inspiration, per-voice FX split
type: project
---

## XObbligato → OBBLIGATO (Phase 0 COMPLETE — March 2026)

- **Repo**: To be created: `~/Documents/GitHub/XObbligato/`
- **Identity**: Dual wind instrument engine — two mischievous brothers play post-punk winds with a sibling relationship arc
- **Gallery code**: OBBLIGATO | Accent: Rascal Coral `#FF8A7A` | Prefix: `obbl_`
- **Plugin code**: `Xobl` | Manufacturer: `Xoox`
- **Status**: Phase 0 complete — concept brief written
- **Concept brief**: `~/Documents/GitHub/XO_OX-XOmnibus/Docs/concepts/xobbligato_concept_brief.md`
- **Aquatic species**: Flying fish — dart between water and air, travel in pairs
- **Water column**: SUNLIT SHALLOWS — just below mother XOrphica's surface position
- **Family**: Sons of XOrphica (the siphonophore goddess)

### Key Architecture
- **Brother A "Peter"**: Bright flute-family winds (flute, shakuhachi, bansuri, pan flute, tin whistle, etc.)
- **Brother B "The Wolf"**: Dark reed-family winds (oboe, duduk, ney, didgeridoo, bassoon, etc.)
- **Waveguide physical modeling**: Exciter (breath/reed) → bore (delay line + filter)
- **BOND macro (M2)**: THE signature — sibling relationship arc (harmony→fight→cry→make up)
- **Per-voice FX split**: Each brother has own FX chain (A=chorus/bright delay/plate, B=phaser/dark delay/spring reverb/tape sat)
- **~41 parameters**, 12 voices (6 per brother), legato
- **4 Macros**: BREATH (excitation), BOND (relationship), MISCHIEF (punk processing), WIND (FX depth)
- **5 voice routing modes**: Alternate, Split, Layer, Round Robin, Velocity

### Family Architecture Pattern
- XOrphica (mother): splits by REGISTER (bass/treble) — horizontal
- XObbligato (sons): splits by VOICE (Brother A/Brother B) — vertical
- Same dual-FX philosophy, different split axis

### Key Couplings
- ORPHICA → OBBLIGATO (Mother & Sons), OBBLIGATO → OVERDUB (Punk Dub Winds)
- ONSET → OBBLIGATO (Wind Machine), ODYSSEY → OBBLIGATO (Wind Journey)

### Next Steps
- Phase 1: Full architecture spec
- Invoke: `/new-xo-engine phase=1 name=XObbligato identity="Dual wind instrument engine — two mischievous brothers play post-punk winds" code=Xobl`
