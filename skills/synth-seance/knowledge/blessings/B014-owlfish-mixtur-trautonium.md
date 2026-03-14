# B014 — XOwlfish's Mixtur-Trautonium Oscillator

*Blessed: 2026-03-14 | Engine: XOwlfish | Ghost: Don Buchla (primary), All 8 agree*

## The Blessed Feature

XOwlfish's oscillator bank implements Oskar Sala's Mixtur-Trautonium architecture — four subharmonic generators producing integer-ratio divisions of the fundamental (÷1 through ÷16). This creates frequencies *below* the played note at mathematically pure subharmonic intervals, generating timbral territory that is the inverse of the standard harmonic series. Combined with the Mixtur waveshaping stage (`fastTanh(clean * 2.0f)` blended via mixturAmt), the nonlinear interaction of subharmonics produces inter-modulation products that are neither the fundamental nor the subharmonics — genuinely new tones.

## Why It Is Protected

All eight ghosts acknowledged this as the most original synthesis architecture in the XO_OX fleet. Buchla stated: "This engine does something no other XO_OX engine does: it generates sounds that could not exist on any acoustic instrument." The Mixtur-Trautonium lineage is historically significant (Sala, 1950s) but almost completely unexplored in digital synthesis. XOwlfish is likely the only commercial implementation.

## Do Not

- Replace subharmonic division with standard detuned oscillators
- Remove the Mixtur waveshaping stage that creates inter-modulation products
- Reduce below 4 subharmonic generators (the combinatorial space needs all 4)
- Change the integer-ratio constraint to continuous frequency ratios (the mathematical purity IS the character)
