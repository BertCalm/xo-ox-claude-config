# MPC Mobile — Sage's Side Project

*iMPC Pro, MPC Beats, Akai iOS apps, and cross-platform workflow design.*
*How to create content that works across the whole Akai ecosystem.*

---

## Table of Contents
1. [The Mobile Ecosystem Overview](#1-the-mobile-ecosystem-overview)
2. [iMPC Pro 2 (iOS)](#2-impc-pro-2-ios)
3. [MPC Beats (Desktop — Free)](#3-mpc-beats-desktop--free)
4. [Akai iOS Controller Apps](#4-akai-ios-controller-apps)
5. [Cross-Platform Workflow Design](#5-cross-platform-workflow-design)
6. [Mobile-First Content Design](#6-mobile-first-content-design)
7. [Limitations and Workarounds](#7-limitations-and-workarounds)
8. [Sage's Mobile Field Notes](#8-sages-mobile-field-notes)

---

## 1. The Mobile Ecosystem Overview

Akai's mobile ecosystem extends MPC's value proposition to the phone/tablet form factor. Understanding the mobile tier helps design content that works at every level of the ecosystem — from phone to iPad to desktop to hardware.

**The tier hierarchy:**

```
MPC Hardware (Live III, Key 61, etc.)   ← Full feature set, standalone
     ↑ project sync / expansion import
MPC Software (macOS/Windows, free)      ← Full desktop, DAW plugin mode
     ↑ audio export / sample sharing
iMPC Pro 2 (iOS)                        ← Mobile production, AU plugin
     ↑ sample sharing via Files app
MPC Beats (macOS/Windows, freemium)     ← Entry-level desktop, limited tracks
```

Content designed for the bottom tier (Beats/iMPC) should sound great at the top too. Design for the constraints first — MPC hardware will always outperform them.

---

## 2. iMPC Pro 2 (iOS)

**What it is:**
A full-featured MPC-style production app for iPhone and iPad. Not a stripped-down demo — a legitimate production environment.

**Capabilities:**
- 128 pads (8×8 layout option)
- Up to 64 tracks
- AU (Audio Unit) plugin support — use third-party iOS synths
- **MPC expansion pack import** — XPN files can be loaded directly
- Full drum program and keygroup support
- Sample import from Files app, iCloud Drive, Dropbox
- Audio recording (via built-in mic or interface)
- Export as audio stems or as MPC project file

**MPC expansion import:**
1. Transfer `.xpn` file to iOS via Files app (AirDrop, iCloud Drive, etc.)
2. In iMPC Pro 2: browse to the XPN file
3. Import → programs and samples extracted into iMPC's library
4. Drum kits and keygroup programs appear immediately in browser

**XPN compatibility considerations:**
- iMPC Pro 2 supports the same XPM XML format as hardware MPC
- File size limit: keep individual samples under 50MB for fast import
- Sample count: 64+ samples per kit works fine; 200+ may slow import on older devices
- AU plugins: iMPC Pro 2 can host iOS AU plugins as additional instruments

**Performance features:**
- Note repeat (hold pad + tap for subdivisions)
- Pad mute/solo
- Swing/groove quantization
- XY performance pad (one pad controlling 2 parameters)

**Best use cases:**
- Sketching beats on phone → export project → finish on MPC hardware
- Using XPN packs designed for hardware on mobile
- Building arrangements on iPad with split keyboard + pads layout
- Live performance with iPhone as backup / additional controller

**iMPC Pro 2 vs. MPC hardware differences:**
- No real-time MIDI device sync (hardware has MIDI DIN in/out)
- Plugin count limited by device CPU (iPhone: 4-6 plugins max, iPad Pro: 12-16)
- No multi-out audio routing
- No CV/Gate
- Touch UI means no physical knob feel — gestures replace hardware controls

---

## 3. MPC Beats (Desktop — Free)

**What it is:**
A free, slightly limited version of the full MPC Software. Designed as an entry point to the MPC ecosystem.

**Free tier capabilities:**
- 2 plugin tracks (vs unlimited in MPC Software)
- 4 audio tracks
- Basic AIR instruments included
- XPN expansion pack import — works fully
- All drum programs and keygroup programs function
- Export audio (stereo mix)
- MIDI export

**MPC Beats + hardware:**
- Connect MPC hardware → MPC Beats acts as controller mode host
- Full pad grid functionality with any MPC hardware
- Limitation: plugin count still capped at 2 in Beats tier

**When to design for Beats:**
- Entry-level users will use Beats first
- XPN packs must sound great with only built-in AIR instruments or the pack's own samples
- Design for the sample-only use case — don't rely on plugin synths being available

**Upgrade path:**
MPC Beats free → MPC Software upgrade (paid) → MPC hardware → full standalone

Content designed with the upgrade path in mind gives free users a taste of what they can grow into.

---

## 4. Akai iOS Controller Apps

### APC Key 25 / APC Mini Mk2 App
- Dedicated apps for APC series controllers
- Work with iMPC Pro 2 via Core MIDI
- Standard MIDI routing

### MPK Mini App
- Companion app for MPK Mini keyboard controllers
- Provides a simplified sequencer view
- MIDI out → iMPC Pro 2 → MPC beats via Bluetooth MIDI

### Bluetooth MIDI (MPC OS 3.6+)
- MPC hardware can pair with iOS devices over Bluetooth MIDI
- iPhone as performance controller → send to MPC hardware
- Latency: 5-15ms — acceptable for sequenced/recorded parts, not for tight live performance
- Setup: MPC Settings > MIDI > Bluetooth > Enable

### iOS AUM (Audio Unit Manager — third party)
- Not Akai but widely used: AUM hosts multiple iOS AU apps including iMPC Pro 2
- Enables: iMPC Pro 2 running as AU plugin inside AUM
- iMPC Pro 2 + Fabfilter Pro-Q (iOS) + other plugins in one session on iPad Pro
- Advanced routing possible that iMPC alone can't do

---

## 5. Cross-Platform Workflow Design

The ideal XO_OX workflow is seamless across all tiers. Here's how content moves:

### Sketch → Ship Workflow

```
1. iPhone (iMPC Pro 2)
   - Sketch beat, lay down samples, rough arrangement
   - Export as audio stems OR as MPC project (portable)

2. iPad Pro or Mac (MPC Beats or MPC Software)
   - Import iPhone project
   - Flesh out arrangement, add plugin instruments
   - Mix begins here

3. MPC Hardware (Live III)
   - Import project
   - Add live performance elements (real-time pad performance)
   - Final mix + mastering
   - Export to DAW for final production
```

### XPN Pack for Cross-Platform Audiences

When designing an XPN pack intended for both mobile and hardware users:

**Mobile constraints to design around:**
- Keep per-sample file size under 30MB for smooth mobile import
- Max 4 velocity layers (mobile handles more, but 4 is the sweet spot)
- Test the kit on iPad — does it fit 128 pads well? Does it work on 16 pads?
- Include a "lite" version for iPhone: 8 pads with the best samples per instrument

**Hardware features that won't work on mobile:**
- MPCe 3D pad X/Y assignments — mobile has no 3D pad
- CV/Gate routing
- Multi-out audio configurations
- More than 12-16 simultaneous plugins

**Mobile-exclusive opportunities:**
- Touch gestures for performance (pinch = filter, swipe = pitch bend)
- AR/haptic features (iOS-only)
- iCloud sync for instant project availability everywhere

---

## 6. Mobile-First Content Design

Designing content specifically for the mobile user (not just porting desktop content):

**The mobile producer's context:**
- On the bus, in a coffee shop, waiting somewhere
- Recording ideas quickly before they disappear
- Can't make a lot of noise — headphones only
- Touch UI means coarser control than physical knobs

**Mobile-first sound design principles:**
1. **Transients over sustained tones** — mobile headphone listening emphasizes attack
2. **Mono-compatible** — most mobile listening is effectively mono (one earbud)
3. **Pre-mixed kits** — mobile producers won't mix individual elements; the kit should sound good as-is
4. **Quick-launch presets** — the best-sounding patch should be the default/init patch
5. **No CPU-heavy effects** — bake reverb/compression into the samples rather than requiring plugin FX

**Naming and organization for mobile:**
- Short, clear names (mobile screen is small)
- Category prefixes in kit names: "HH_Open_Bright.wav" sorts better than "Bright_Open_Hat.wav"
- 16-pad kits are easier to navigate on phone than 128-pad kits

---

## 7. Limitations and Workarounds

| Limitation | Platform | Workaround |
|-----------|---------|-----------|
| 2 plugin tracks max | MPC Beats (free) | Use sample-based instruments instead of plugins; upgrade to Software |
| No MIDI DIN | iMPC Pro 2 | Use Bluetooth MIDI or USB-C MIDI adapter |
| No multi-out routing | Mobile | Mix in-app; export stems separately by muting/soloing |
| MPCe 3D pads missing | Mobile, older HW | Map X/Y to aftertouch (channel pressure) — iOS supports it |
| Large sample import slow | Mobile | Compress samples to 16-bit WAV; split kit into multiple programs |
| No AU plugin sync clock | iMPC Pro | Use iMPC Pro as clock master; sync other apps to it via Ableton Link |
| iCloud project sync | Hardware → Mobile | Export MPC project as audio; no direct project file sync |
| exFAT format requirement | Hardware | iOS bypasses this — iMPC Pro imports via Files app, no formatting needed |

---

## 8. Sage's Mobile Field Notes

*Collected observations from studying the Akai mobile ecosystem:*

**What mobile gets right:**
- iMPC Pro 2 is genuinely impressive — full 128-pad MPC in your pocket
- XPN import on iOS is seamless — better onboarding than the hardware's USB workflow
- Bluetooth MIDI to hardware is a legitimate live performance tool for simple MIDI triggers
- The free tier (MPC Beats) is surprisingly capable for beat-making

**What mobile gets wrong:**
- No project file compatibility between iMPC Pro 2 and MPC Software/hardware (audio export only)
- Akai's iOS apps haven't had major updates since 2022 — falling behind competitors
- No native Apple Silicon optimization for MPC Beats on Mac
- The iOS app ecosystem around MPC is thin — competitors (GarageBand, Koala, etc.) have more cross-app integration

**Sage's mobile recommendations:**
```
1. For iPad Pro: iMPC Pro 2 is worth the cost — it's a real instrument
2. For iPhone: iMPC Pro 2 works, but Koala Sampler may feel faster for quick sketching
3. For cross-platform workflows: Ableton Link sync works well between iMPC and desktop
4. For importing existing packs: XPN import on iOS is the best mobile sampler pack experience
5. Bluetooth MIDI latency: test your specific device + MPC combo — variability is high
6. MPC Beats free: great for learning, limiting for production — upgrade is worth it
```

<!-- bible extended 2026-03 — initial build, iMPC Pro 2 iOS workflow documented -->
