---
name: xpn-tools
description: XPN/XPM export tools for MPC expansions — exporter, cover art, bundle builder
type: project
---

# XPN Tool Suite (XOmnibus Tools)

Located in `~/Documents/GitHub/XO_OX-XOmnibus/Tools/`

| Tool | Purpose |
|------|---------|
| `xpn_drum_export.py` | Drum program XPN builder for XOnset. 8 pads GM-layout, 4 vel layers, checklist mode |
| `xpn_cover_art.py` | Procedural cover art (2000×2000 + 1000×1000). Deps: Pillow + numpy |
| `xpn_bundle_builder.py` | Multi-engine bundler. 3 modes: custom, category, predefined (8 profiles). Engine name normalization |
| `generate_library_fills.py` | Gap fill generator for Dub/Prism, Drift, ONSET coupling, Snap, Morph |
| `generate_onset_presets.py` | XOnset drum preset generator (98 presets, 8 categories incl. World, DNA corners) |
| `site_audio_export.py` | WAV→MP3/OGG for web |

## XPN Keygroup Exporter (standalone)
- **Location**: `~/Documents/GitHub/XOdyssey/tools/xpn_exporter/xpn_export.py`
- **Purpose**: Generate MPC-compatible .xpn packs from rendered WAVs
- **Strategy**: Multi-sampled keygroup (KeyTrack=True, RootNote=0, 21 notes per preset every minor 3rd C1-C6)
- **WAV naming**: `PRESET__NOTE__v1.WAV` (double-underscore separator)
- **Format ref**: `~/Documents/GitHub/XOdyssey/docs/MPC_XPM_Format_Reference.md`

## Critical XPM Rules (learned from XObese fix)
- `KeyTrack=True` — samples transpose with pitch
- `RootNote=0` — MPC auto-detects
- Empty layer `VelStart=0` — prevents ghost triggering
- `Application=MPC-V`, full ProgramPads/PadNoteMap/PadGroupMap

## XObese MPC Expansion
- **Location**: `~/Library/Application Support/Akai/MPC/Expansions/com.xo-ox.xobese/`
- ~99 presets, WAVs correct, XPMs fixed via `XOddCouple/tools/fix_xobese_xpms.py`
- Working reference: DX-TX v2 at `~/Library/Application Support/Akai/MPC/Expansions/com.amazound.dxtxv2/`
