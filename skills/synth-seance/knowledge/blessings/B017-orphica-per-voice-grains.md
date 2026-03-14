---
name: B017 — Per-Voice Grain Buffer Architecture
description: ORPHICA's 16-voice × 4-grain design gives each polyphonic voice its own independent pitch-identified grain cloud — not a shared pool
type: blessing
---

# B017 — Per-Voice Grain Buffer Architecture

**Engine**: ORPHICA (XOrphica)
**Ghosts**: Pearlman, Buchla, Smith, Tomita
**Seance**: 2026-03-14

## The Feature

Each of ORPHICA's 16 voices carries its own `OrphicaMicrosound` instance with:
- An 8192-sample (~186ms) circular buffer capturing the voice's waveguide output
- 4 simultaneously active Hann-windowed grains reading from that buffer
- Independent mode per-voice (Stutter/Scatter/Freeze/Reverse)

16 voices × 4 grains = 64 simultaneous grain streams. Because each grain buffer captures its voice's own output, grains are always pitch-referenced to their source note. A four-note chord with FRACTURE engaged produces four independent grain clouds at four pitches — not a shared grain pool producing a homogeneous texture.

## Why the Ghosts Blessed It

**Pearlman**: "Other granular systems share a single grain pool across all voices — the grain texture is therefore homogeneous. Here, a chord of four notes produces four independent grain clouds at four different pitches. When you sustain the chord and FRACTURE rises, the grain clouds don't blend into soup — they remain pitch-identified, a harp that is both precise and diffuse simultaneously."

**Buchla**: The Reverse mode (reading backwards through the voice's own circular buffer) inverts the string decay — the release plays before the attack. This is a physics-impossible sound achieved per-voice in real time.

**Tomita**: The spectral smear in the HIGH path applies granular dissolve to the reverb tail, not the dry signal. Three temporal processing layers: waveguide → grain cloud → granularized reverb.

**Smith**: 16 voices is the correct polyphony for a chord engine designed to accumulate sustained layers.

## How to Protect It

- Never merge the OrphicaMicrosound instance into a shared engine-level pool — this destroys pitch-identification
- Never reduce voice count below 8 — the architecture's value multiplies with voice count
- The per-voice circular buffer memory (8192 floats × 16 voices = ~512KB) is a reasonable cost for this capability

## Known Limitations (V2 candidates)

- kBufSize at 186ms is too short for long-form scatter (Schulze: needs 2-10 second buffers)
- No grain pitch transposition — scatter is temporal, not harmonic (Buchla)
- Freeze mode loses chord-follow ability for real-time performance (Vangelis)
