---
name: new-xo-engine
description: Design and scaffold a new XO_OX synth engine — standalone first, XOmnibus-ready from day one. Handles ideation, architecture, scaffold, and integration prep.
---

# New XO_OX Engine — Sandbox to Gallery

Design, build, and prepare a new synth engine for eventual XOmnibus integration while developing it as an independent standalone instrument.

## Arguments
- `phase`: Which phase to run (0=ideate, 1=architect, 2=scaffold, 3=integrate, all=full process). Default: 0
- `name`: Engine name (XO + O-word, e.g., XOpossum). Required for phases 1+.
- `identity`: One-line character description. Required for phases 1+.
- `code`: 4-char JUCE plugin code. Required for phase 2+.

## Process Reference

Full process documentation: `~/Documents/GitHub/XO_OX-XOmnibus/Docs/xomnibus_new_engine_process.md`

## Phase 0: Ideate

When `phase=0` or `phase=all`:

1. **Read the gallery** — load the engine catalog from `~/Documents/GitHub/XO_OX-XOmnibus/Docs/xo_mega_tool_engine_catalog.md` to understand what sonic territory is already covered
2. **Read concept patterns** — load `~/Documents/GitHub/XOddCouple/synth_playbook/agent_knowledge/synth_concept_patterns.md` for successful concept structures
3. **Interactive concept development:**
   - Ask the user: "What sound or feeling are you chasing?" or work from provided inspiration
   - Apply the XO_OX Concept Test (XO word, one-sentence thesis, unique sound)
   - Check the gallery for sonic gaps — what territory is unoccupied?
   - Identify coupling partners — which existing engines would pair well?
4. **Write concept brief** using the template from the process doc
5. **Output:** Concept brief saved to clipboard or a temp file for review

## Phase 1: Architect

When `phase=1` or `phase=all`:

1. **Run the Synth Architect Protocol** from `~/Documents/GitHub/XOddCouple/synth_playbook/agent_skills/synth_architect_protocol.md`
2. **Additionally define XOmnibus-specific requirements:**
   - Parameter namespace prefix (e.g., `poss_` for XOpossum)
   - Macro mapping: M1=CHARACTER, M2=MOVEMENT, M3=COUPLING, M4=SPACE — what each controls
   - Coupling interface: what `getSampleForCoupling()` returns, which `CouplingType` enums are supported
   - Voice architecture: max voices, stealing strategy, legato
   - Accent color selection (check existing palette for conflicts)
   - Gallery material/texture idea
3. **Output:** Full spec + architecture blueprint + XOmnibus integration spec written to `docs/` in the project repo

## Phase 2: Scaffold & Build

When `phase=2` or `phase=all`:

1. **Invoke `/new-xo-project`** with the engine's name, identity, and code
2. **Apply dual-target modifications:**
   - Add `src/adapter/` directory with a stub adapter header
   - Ensure all parameter IDs use the namespaced format: `{shortname}_{paramName}`
   - Add `.xometa` preset template to `Presets/` directory
   - Copy `SynthEngine.h` from XOmnibus as a reference header (not linked yet)
3. **Create the initial preset** in `.xometa` format (the "Init" patch)
4. **Update CLAUDE.md** with:
   - XOmnibus integration notes
   - Parameter namespace prefix
   - Macro mapping table
   - Coupling compatibility notes
5. **Build and verify** the scaffold compiles

## Phase 3: Integration Prep

When `phase=3` or `phase=all`:

1. **Read the standalone engine's source** to understand the DSP architecture
2. **Write the adapter** (`src/adapter/XO_____Adapter.h`) implementing `xomnibus::SynthEngine`
3. **Write the integration spec** (`docs/xomnibus_integration_spec.md`)
4. **Verify presets** are all in `.xometa` format with correct namespace
5. **Run Sonic DNA computation** on all presets
6. **Output:** Integration checklist (what's ready, what's needed for Phase 4)

Phase 4 (Gallery Install) is performed manually in the XOmnibus repo — see the process doc.

## Key Design Rules

- **DSP in `.h` headers** — all audio code inline for portability
- **ParamSnapshot pattern** — cache param pointers once per block
- **No UI coupling in DSP** — engine works with just parameters
- **Namespaced IDs from day one** — `{shortname}_{paramName}` format
- **`.xometa` presets from day one** — no migration needed later
- **Macros always audible** — M1-M4 must produce change in every preset

## File References

| File | Purpose |
|------|---------|
| `~/Documents/GitHub/XO_OX-XOmnibus/Docs/xomnibus_new_engine_process.md` | Full process documentation |
| `~/Documents/GitHub/XO_OX-XOmnibus/Source/Core/SynthEngine.h` | Engine interface contract |
| `~/Documents/GitHub/XO_OX-XOmnibus/Source/Core/EngineRegistry.h` | Registration macro |
| `~/Documents/GitHub/XO_OX-XOmnibus/Source/Core/MegaCouplingMatrix.h` | Coupling types |
| `~/Documents/GitHub/XO_OX-XOmnibus/CLAUDE.md` | XOmnibus project guide |
| `~/Documents/GitHub/XOddCouple/synth_playbook/agent_skills/synth_architect_protocol.md` | Architect protocol |
| `~/Documents/GitHub/XOddCouple/synth_playbook/agent_knowledge/` | Knowledge base |
