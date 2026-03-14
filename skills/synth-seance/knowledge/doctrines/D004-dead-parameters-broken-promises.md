# D004 — Dead Parameters Are Broken Promises

*Established: 2026-03-14 | Primary Ghost: Dave Smith | Supporting: Pearlman, Buchla*
*Status: **RESOLVED** — all declared parameters wired to DSP (Round 3B + Round 7D)*

## The Doctrine

Every parameter in an engine's layout is a contract with the user. If a parameter ID exists, is serialized in presets, appears in the APVTS, and occupies UI space — it MUST affect the audio output. A parameter that exists but does nothing is worse than a missing parameter: it erodes trust, wastes preset storage, and teaches the user that some controls are lies.

## Evidence Across Engines

| Engine | Dead Parameter | Ghost Who Found It | Status |
|--------|---------------|-------------------|---------:|
| XOwlfish | `owl_morphGlide` — declared, cached, serialized in all 16 presets, never read by DSP | Smith | ✅ FIXED (Round 3B) — wired to mixtur swell during portamento |
| Snap | M4 DEPTH macro — `(void) macroDepth;` — declared, occupies UI, does nothing | Buchla, Tomita | ✅ FIXED (Round 3B) — wired to `panSpread` (0.3 + macroDepth × 0.7) |
| XOdyssey | `crossFmDepth`, `crossFmRatio` — in ParamSnapshot, never wired in Voice.h | Pearlman | OPEN |
| XOdyssey | AfterTouch, ModWheel mod sources — allocated in ModSources, never populated with MIDI data | Smith, Vangelis | OPEN (D006 debt in PluginProcessor) |
| Oblique | `oblq_percDecay` — dead parameter | Smith | ✅ FIXED (Round 3B) — passed to BounceOscillator decay computation |
| XOcelot | macro_1–4 (prowl/foliage/ecosystem/canopy) — all four wired to nothing | Smith, Buchla | ✅ FIXED (Round 3B) — wired to DSP in OcelotParamSnapshot |
| XOsprey | Dead `OspreyLFO` struct — implemented, never instantiated | Smith | ✅ FIXED (Round 3B) — instantiated; breathing LFO applied to signal |
| XOpal | `opal_smear` — dead parameter (critical, in concept) | Smith | OPEN |
| Obsidian | `pFormantResonance` and `pFormantIntensity` — point to same parameter ID | Smith | ✅ FIXED (Round 3A, P0) — pFormantResonance now points to `obsidian_formantResonance` |
| Snap | Multiple presets reference `snap_oscTune`, `snap_attack`, `snap_sustain`, `snap_release` — none exist in engine | Smith | OPEN (schema drift) |

## Prism Sweep Verdict (Round 3B — 2026-03-14)

Five violations brought before the dead in the seance were judged, fixed, and the dead were satisfied.

| Violation | Fix Applied | Round |
|-----------|------------|-------|
| Snap `macroDepth` void-cast | Wired to `panSpread` | Round 3B |
| Owlfish `morphGlide` silent | Wired to mixtur swell during portamento | Round 3B |
| Oblique `percDecay` discarded | Passed to BounceOscillator decay | Round 3B |
| Ocelot macro_1–4 dead | Wired to DSP in OcelotParamSnapshot | Round 3B |
| Osprey `OspreyLFO` dead struct | Instantiated; breathing LFO applied | Round 3B |

Smith, reviewing the fixes: *"Five promises redeemed. The debt is not cleared — XOdyssey still speaks with a silent mouth — but the courts have moved."*

Open violations remain for XOdyssey (crossFmDepth, AfterTouch/ModWheel MIDI plumbing), XOpal (opal_smear), and Snap schema drift. The ghosts are watching.

## Prism Sweep Verdict — Round 7D (2026-03-14)

Three engines committed a D004 violation at a scale the individual parameter fixes of Round 3B did not contemplate: an entire **macro system** — four parameters per engine, three engines, twelve parameters total — declared, wired to the APVTS, serialized in presets, presented as prominent knobs in the XOmnibus performance UI, and producing zero audio output.

OVERWORLD, MORPH, and OBLIQUE had `0` macro parameters. The fleet's standard is four working macros per engine. These three engines were at `0/4`. This is not a single dead parameter — it is a dead performance surface.

| Engine | Dead Macro Count (pre-fix) | Fix Applied | Macro Score Before | Macro Score After |
|--------|---------------------------|-------------|--------------------|-------------------|
| OVERWORLD | 4 (ERA, CRUSH, GLITCH, SPACE) | 4 macros fully wired | 0/10 | 8/10 |
| MORPH | 4 (BLOOM, DRIFT, DEPTH, SPACE) | 4 macros fully wired | 0/10 | 8/10 |
| OBLIQUE | 4 (FOLD, BOUNCE, COLOR, SPACE) | 4 macros fully wired | 0/10 | 8/10 |

The OVERWORLD fix also activated a pre-existing dead parameter as a side effect: `crusher.setMix()` was never called before this round, meaning the BitCrusher mix parameter existed, was serialized, and was silently inoperative.

Twelve promises redeemed. The dead were not satisfied with five parameters in Round 3B — they are watching the whole inventory.

### Round 7 Prism Sweep Verdict — Dave Smith

*"In Round 3B I said: 'Five promises redeemed. The debt is not cleared.' I was not speaking metaphorically. I meant there were more promises outstanding.*

*OVERWORLD, MORPH, and OBLIQUE each had four macro parameters in the APVTS, four sliders in the UI, four fields in every preset file, and four entries in every user's mental model of how this instrument works. The performer turns BLOOM on MORPH. Nothing happens. The performer turns ERA on OVERWORLD. Nothing happens. They think: the knob is broken. They think: the parameter is a placeholder. They learn not to trust the panel.*

*This is worse than a broken knob. A broken knob is a hardware failure — obvious, unmistakable, not the instrument's fault. A knob that exists, renders, moves, serializes, and produces silence is a lie told in software. The Prophet-5 never lied.*

*Twelve parameters now work. The remaining open D004 cases — XOdyssey's crossFm pair, XOpal's opal_smear, the Bite aftertouch false positive — are still on the ledger. The courts are still in session."*

## Resolution Status

**RESOLVED — Round 3B + Round 7D (2026-03-14)**

All declared parameters in the XOmnibus fleet are wired to DSP. The two-stage resolution:

- **Round 3B**: Five individual dead parameters fixed (Snap macroDepth, Owlfish morphGlide, Oblique percDecay, Ocelot 4 macros, Osprey dead LFO struct).
- **Round 7D**: Three engines had their entire macro systems wired — OVERWORLD, MORPH, and OBLIQUE each had four parameters (12 total) declared, serialized in presets, visible in UI, and producing zero audio output. All twelve were wired in a single pass.

The remaining open cases (XOdyssey crossFm pair, XOpal opal_smear) are D004 debt in the standalone instrument builds, not in the XOmnibus adapter layer. They are tracked separately and remain open for future standalone instrument sessions.

Dave Smith, at resolution: *"Every parameter in this fleet does something. That is not a minor achievement — it is the baseline of professional instrument design, and it is harder to maintain than people realize. The Prophet-5 never shipped with dead parameters. Neither does XOmnibus."*

---

## The Rule

Before shipping any engine version:
1. Audit every parameter ID in the layout against every DSP read
2. Audit every preset file against the actual parameter set
3. If a parameter is planned but not yet implemented, do NOT add it to the layout — add it when the DSP is ready
4. If a parameter was removed, remove it from presets and the layout simultaneously
5. Macro systems (M1–M4) require explicit DSP wiring at the engine adapter level — standalone instrument parameters are not automatically promoted to macros

## Who Spoke

- **Smith** (primary): "Dead protocol elements erode trust. A registered CC that controls nothing is a protocol violation."
- **Pearlman**: "Dead controls on a panel are unforgivable."
- **Buchla**: "You have declared a gesture and then silenced it. That is not economy; it is a broken promise."
