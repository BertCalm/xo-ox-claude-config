# V004 — instantaneousFreq: The Spectral Compass

*Recorded: 2026-03-14 | Engine: Origami | Ghost: Vangelis*

## The Vision

Origami computes `instantaneousFreq` from the STFT phase difference on every frame — a real-time measurement of the dominant frequency in each spectral bin — but never uses it. This computed-but-discarded value is a spectral compass pointing at the heart of the sound. It should drive:

- Pitch-aware spectral effects (transpose only harmonics, leave noise untouched)
- Formant preservation during pitch shifting
- Spectral following — one STFT operation tracking and responding to the frequency content of another
- A visual display showing the spectral landscape in real time

## Why This Matters

Most spectral effects are frequency-blind — they process magnitude without knowing what pitch each bin represents. instantaneousFreq gives Origami pitch-awareness in the spectral domain, which is the missing piece between "spectral effect" and "spectral instrument."
