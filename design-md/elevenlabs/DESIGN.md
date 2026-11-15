---
version: alpha
name: ElevenLabs-design-analysis
description: A voice-AI brand whose marketing surfaces read like a quietly editorial print magazine. The base canvas is off-white (`#f5f5f5`) holding warm near-black ink (`#292524`); the brand voltage is photographic, not chromatic — soft pastel atmospheric gradient orbs (mint → peach → lavender → sky) drift through the page as the only "color" moments. Display runs Waldenburg Light at weight 300 — the editorial signature. Inter carries body, navigation, captions. CTAs are subtle: a near-black ink pill is the primary, a transparent outline is the secondary. The brand trusts atmospheric photography and modest type weights to do all of the brand work; there is no neon accent, no saturated CTA color, no developer-tools dark canvas.

colors:
  primary: "#292524"
  primary-active: "#0c0a09"
  ink: "#0c0a09"
  body: "#4e4e4e"
  body-strong: "#292524"
  muted: "#777169"
  muted-soft: "#a8a29e"
  muted-strong: "#757068"
  hairline: "#e7e5e4"
  hairline-soft: "#f0efed"
  hairline-strong: "#d6d3d1"
  hairline-control: "#8a8580"
  canvas: "#f5f5f5"
  canvas-soft: "#fafafa"
  canvas-deep: "#0c0a09"
  surface-card: "#ffffff"
  surface-strong: "#f0efed"
  surface-dark: "#0c0a09"
  surface-dark-elevated: "#1c1917"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-soft: "#a8a29e"
  focus: "#78716c"
  gradient-mint: "#a7e5d3"
  gradient-peach: "#f4c5a8"
  gradient-lavender: "#c8b8e0"
  gradient-sky: "#a8c8e8"
  gradient-rose: "#e8b8c4"
  semantic-error: "#dc2626"
  semantic-success: "#16a34a"

typography:
  display-mega:
    fontFamily: "'Waldenburg', 'Times New Roman', serif"
    fontSize: 64px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1.92px
  display-xl:
    fontFamily: "'Waldenburg', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.96px
  display-lg:
    fontFamily: "'Waldenburg', serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.17
    letterSpacing: -0.36px
  display-md:
    fontFamily: "'Waldenburg', serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.13
    letterSpacing: -0.32px
  display-sm:
    fontFamily: "'Waldenburg', serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.44
    letterSpacing: 0.18px
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.16px
  body-strong:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.16px
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: 0.15px
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.96px
    textTransform: uppercase
  button:
    fontFamily: "'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
  pill: 9999px
  full: 9999px

shadow:
  none: none
  card-hover: "0 4px 16px rgba(0, 0, 0, 0.04)"

motion:
  duration-instant: 120ms
  duration-fast: 240ms
  duration-base: 400ms
  duration-slow: 600ms
  duration-emphasis: 900ms
  ease-standard: cubic-bezier(0.22, 1, 0.36, 1)
  ease-enter: cubic-bezier(0.16, 1, 0.3, 1)
  ease-exit: cubic-bezier(0.5, 0, 0.75, 0)
  stagger-step: 80ms
  duration-reduced: 150ms

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  base: 16px
  md: 20px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

components:
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 9px 19px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-mega}"
    padding: 96px
  gradient-orb-card:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xxl}"
    padding: 32px
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 24px
  product-card-stack:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 0
  voice-row:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 12px 0
  voice-icon-circular:
    backgroundColor: "{colors.surface-strong}"
    rounded: "{rounded.full}"
    size: 32px
  pricing-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  pricing-tier-featured:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 44px
  badge-pill:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  cta-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 96px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  audio-waveform-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 64px 48px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
---

## Overview

ElevenLabs reads like a quietly editorial print magazine that happens to be a voice-AI product. The base canvas is off-white `{colors.canvas}` (#f5f5f5) holding warm near-black ink `{colors.ink}` (#0c0a09). The brand voltage is **photographic, not chromatic**: soft pastel atmospheric gradient orbs (mint, peach, lavender, sky, rose) drift through the page as the only "color" moments. There is no neon accent, no saturated CTA color, no dark-canvas dev-tools atmosphere.

Type pairs **Waldenburg Light** (custom serif at weight 300) for display with **Inter** for body, navigation, captions. The display weight at 300 is the editorial signature — never bold, never heavy.

CTAs are subtle: a near-black ink pill (`{component.button-primary}`) is the primary, a transparent outline (`{component.button-outline}`) is the secondary. The brand trusts atmospheric photography and modest type weights to carry brand work.

**Key Characteristics:**
- Off-white canvas, warm near-black ink. No saturated CTA color.
- Single primary action: ink pill at `{rounded.pill}`. Atmospheric gradients carry visual brand voltage.
- Display runs Waldenburg Light at weight 300 — editorial magazine voice.
- Body runs Inter at 400 with subtle letter-spacing (+0.15-0.18px).
- Pastel gradient orbs (5 tokens: mint, peach, lavender, sky, rose) used as atmospheric brand decoration only.
- Soft pill geometry (`{rounded.pill}` for CTAs, `{rounded.xl}` for cards).
- 96px section rhythm.

## Colors

### Brand & Accent
- **Ink Primary** (`{colors.primary}` — #292524): The primary action color — warm near-black pill. Used scarcely.
- **Ink Primary Active** (`{colors.primary-active}` — #0c0a09): Press state.

### Surface
- **Canvas** (`{colors.canvas}` — #f5f5f5): Off-white page floor.
- **Canvas Soft** (`{colors.canvas-soft}` — #fafafa): Lighter band for subtle alternating sections.
- **Canvas Deep** (`{colors.canvas-deep}` — #0c0a09): Same as ink — used for the rare dark-mode hero (Agents page).
- **Surface Card** (`{colors.surface-card}` — #ffffff): Pure white card.
- **Surface Strong** (`{colors.surface-strong}` — #f0efed): Badges, voice-icon plates.
- **Surface Dark** (`{colors.surface-dark}` — #0c0a09): Dark hero/CTA band canvas.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — #1c1917): Cards on dark canvas.

### Hairlines
- **Hairline** (`{colors.hairline}` — #e7e5e4): Default 1px divider.
- **Hairline Soft** (`{colors.hairline-soft}` — #f0efed): Lighter divider.
- **Hairline Strong** (`{colors.hairline-strong}` — #d6d3d1): Stronger panel outline.
- **Hairline Control** (`{colors.hairline-control}` — #8a8580) — *prescribed, not extracted*: The boundary of an interactive control (text input, outline button). All three extracted hairlines sit under 1.5:1 on `{colors.canvas}` and cannot carry a control boundary; this parallel token measures 3.35:1 on `{colors.canvas}` and 3.65:1 on `{colors.surface-card}`. The three extracted hairlines are scoped to **decoration only** — dividers between non-interactive content.

### Text
- **Ink** (`{colors.ink}` — #0c0a09): Display, primary text.
- **Body** (`{colors.body}` — #4e4e4e): Default running-text.
- **Body Strong** (`{colors.body-strong}` — #292524): Same as primary — emphasis.
- **Muted** (`{colors.muted}` — #777169): Sub-titles. Measures 4.43:1 on `{colors.canvas}` — a 0.07 miss against AA, so scope it to 18px+ labels and use `{colors.muted-strong}` below that.
- **Muted Soft** (`{colors.muted-soft}` — #a8a29e): Disabled text **only** on light surfaces (2.31:1 on `{colors.canvas}` — below AA for live text), plus muted text on the dark bands where it reaches 7.83:1.
- **Muted Strong** (`{colors.muted-strong}` — #757068) — *prescribed, not extracted*: The accessible stand-in for `{colors.muted}` wherever a sub-title is live text at under 24px. 4.51:1 on `{colors.canvas}`, 4.91:1 on `{colors.surface-card}`.
- **On Primary** (`{colors.on-primary}` — #ffffff): White text on ink pill.
- **On Dark** (`{colors.on-dark}` — #ffffff): White text on dark hero.
- **On Dark Soft** (`{colors.on-dark-soft}` — #a8a29e): Muted off-white on dark.

### Focus
- **Focus** (`{colors.focus}` — #78716c) — *prescribed, not extracted*: No file in this collection documented a focus ring; this one is new. ElevenLabs is a monochrome brand with no accent colour, so a chromatic ring would invent brand voltage the brand refuses. Instead the ring is a single mid-luminance warm stone, chosen so that **one** token clears 3:1 against every surface this file defines — light and dark alike — rather than needing a `focus-on-dark` pair. Measured: 4.40:1 on `{colors.canvas}`, 4.60:1 on `{colors.canvas-soft}`, 4.80:1 on `{colors.surface-card}`, 4.17:1 on `{colors.surface-strong}`, 4.12:1 on `{colors.surface-dark}`, 3.65:1 on `{colors.surface-dark-elevated}`. Over the pastel gradient orbs it drops to 2.60–3.38:1, so there it is drawn two-tone — see Accessibility.

### Atmospheric Gradient Stops (signature)
- **Gradient Mint** (`{colors.gradient-mint}` — #a7e5d3): Mint green orb.
- **Gradient Peach** (`{colors.gradient-peach}` — #f4c5a8): Peach orb.
- **Gradient Lavender** (`{colors.gradient-lavender}` — #c8b8e0): Lavender orb.
- **Gradient Sky** (`{colors.gradient-sky}` — #a8c8e8): Sky-blue orb.
- **Gradient Rose** (`{colors.gradient-rose}` — #e8b8c4): Rose orb.

These appear ONLY as soft radial-gradient atmospheric orbs inside `{component.gradient-orb-card}` and as background atmospheric blooms behind hero copy. Never as button fills, never as text colors.

### Semantic
- **Success** (`{colors.semantic-success}` — #16a34a): Confirmation.
- **Error** (`{colors.semantic-error}` — #dc2626): Validation errors.

## Typography

### Font Family
**Waldenburg Light** is the licensed display serif at weight 300. **Inter** carries body, navigation, captions, and buttons. Fallback: `'Times New Roman', serif` for Waldenburg, `sans-serif` for Inter.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-mega}` | 64px | 300 | 1.05 | -1.92px | Homepage hero h1 |
| `{typography.display-xl}` | 48px | 300 | 1.08 | -0.96px | Subsidiary heroes |
| `{typography.display-lg}` | 36px | 300 | 1.17 | -0.36px | Section heads |
| `{typography.display-md}` | 32px | 300 | 1.13 | -0.32px | Sub-section heads |
| `{typography.display-sm}` | 24px | 300 | 1.2 | 0 | Card group titles |
| `{typography.title-md}` | 20px | 500 | 1.35 | 0 | Component titles — Inter |
| `{typography.title-sm}` | 18px | 500 | 1.44 | 0.18px | List labels |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0.16px | Default body — Inter |
| `{typography.body-strong}` | 16px | 500 | 1.5 | 0.16px | Emphasized body |
| `{typography.body-sm}` | 15px | 400 | 1.47 | 0.15px | Footer body |
| `{typography.caption}` | 14px | 400 | 1.5 | 0 | Photo captions |
| `{typography.caption-uppercase}` | 12px | 600 | 1.4 | 0.96px | Section labels, badges |
| `{typography.button}` | 15px | 500 | 1.0 | 0 | CTA pill |
| `{typography.nav-link}` | 15px | 500 | 1.4 | 0 | Top-nav menu |

### Principles
- **Display weight stays at 300.** Waldenburg Light is the editorial signature. Never bold display copy.
- **Subtle letter-spacing on body.** Inter at +0.15-0.18px tracking — slightly looser than default Inter for a more editorial feel.
- **Negative letter-spacing on display.** Waldenburg pulls -0.32px to -1.92px tighter on display sizes.

### Note on Font Substitutes
Waldenburg is licensed. Open-source substitute: **EB Garamond** at weight 300 (slightly more humanist) or **GT Sectra** (closer to Waldenburg's modernity). Use Inter directly for body — it's the same family ElevenLabs uses.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.base}` 16px · `{spacing.md}` 20px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- **Section padding:** 96px.

### Grid & Container
- Max content width: ~1200px.
- Editorial body: 12-column grid.
- Feature card grids: 2-up at desktop for hero splits, 3-up for benefit grids.
- Footer: 5-column at desktop.

### Whitespace Philosophy
Generous editorial pacing — print-magazine feel. 96px between bands; cards inside bands sit close (16-24px gap). The atmospheric gradient orbs occupy generous breathing space without competing with copy.

## Elevation & Depth

The system uses **hairline + soft drop**. Cards float above the off-white canvas via 1px hairlines and a single subtle shadow tier. Atmospheric depth comes from gradient orbs.

Elevation is expressed **one way**: a 1px border always, and the shadow tier only as a hover increment. There is no second shadow level and no border-only card.

The light layers are deliberately near-identical in luminance — `{colors.canvas}` to `{colors.surface-card}` is 1.09:1, canvas to `{colors.canvas-soft}` 1.04:1, canvas to `{colors.surface-strong}` 1.05:1, and `{colors.surface-dark}` to `{colors.surface-dark-elevated}` 1.13:1. **The layers are not distinguishable by fill alone.** That is the brand's intent — a print-magazine page, not a stack of panels — which is exactly why the 1px border is mandatory on every card and why the control boundary needs `{colors.hairline-control}` rather than a hairline.

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `{colors.canvas}` (#f5f5f5) | Body bands, footer |
| Card | `{colors.surface-card}` (#ffffff) | Content cards |
| Hairline border | 1px `{colors.hairline}` | Card outlines (decorative) |
| Control border | 1px `{colors.hairline-control}` | Text inputs, outline buttons — any boundary that must be seen |
| Soft drop | `{shadow.card-hover}` (`0 4px 16px rgba(0, 0, 0, 0.04)`) | Hovered cards (single shadow tier) |
| Gradient orb | Radial gradient with one of `{colors.gradient-*}` | Atmospheric depth — never a card surface |

### Decorative Depth
- **Pastel gradient orbs** are the brand's strongest atmospheric pattern. Soft radial blooms in mint, peach, lavender, sky, or rose drift through hero bands and feature sections without containing any content — they are pure atmosphere.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Reserved |
| `{rounded.xs}` | 4px | Inline tags |
| `{rounded.sm}` | 6px | Compact rows |
| `{rounded.md}` | 8px | Form inputs |
| `{rounded.lg}` | 12px | Compact cards |
| `{rounded.xl}` | 16px | Feature cards, pricing tiers |
| `{rounded.xxl}` | 24px | Gradient orb cards (extra-soft) |
| `{rounded.pill}` | 9999px | All CTA buttons, badges |
| `{rounded.full}` | 9999px | Voice icon circles, avatars |

## Components

### Interaction States

Every component below names the states it supports. A component with genuinely
two states says so rather than padding the list. The focus treatment is the same
everywhere: a 2px `{colors.focus}` ring with a 2px offset in the underlying
surface colour.

| Component | States |
|---|---|
| `top-nav` | default · hover (link ink darkens to `{colors.ink}`) · focus-visible (ring on the link) · selected (current section underlined 1px `{colors.ink}`) — no disabled, loading or error state; the nav is always live |
| `button-primary` | default · hover (`{shadow.card-hover}`, no fill change) · focus-visible · active/pressed (`{colors.primary-active}`) · disabled (`{colors.hairline-strong}` fill, `{colors.muted-soft}` label) · loading (label holds, 16px ring spinner replaces the trailing icon) — not selectable, no error state |
| `button-primary-active` | The pressed variant of `button-primary`, recorded as its own entry. One state by definition. |
| `button-outline` | default (1px `{colors.hairline-control}`) · hover (border to `{colors.ink}`) · focus-visible · active/pressed (`{colors.surface-strong}` fill) · disabled (border `{colors.hairline}`, label `{colors.muted-soft}`) · loading — not selectable, no error state |
| `button-tertiary-text` | default · hover (1px underline) · focus-visible · active/pressed (`{colors.primary-active}`) · disabled — no loading, selected or error state |
| `hero-band` | Static band. One state; nothing inside it but type, two CTAs and an orb, each with its own states. |
| `gradient-orb-card` | default · hover (orb scales to 1.02, card lifts to `{shadow.card-hover}`) · focus-visible (whole card ringed when the card is a link) — no pressed, disabled, loading, selected or error state |
| `audio-waveform-card` | default · hover (play glyph gains `{colors.ink}`) · focus-visible (on the play control) · active/pressed · loading (waveform bars hold at 40% opacity until audio is decoded) · selected (playing: 1px `{colors.ink}` border) · error (1px `{colors.semantic-error}` border, caption states the failure) · disabled (no preview available) |
| `feature-card` | default · hover (`{shadow.card-hover}`) · focus-visible when linked — no pressed, disabled, loading, selected or error state |
| `product-card-stack` | default · hover (top card lifts) · focus-visible · selected (the card brought to the front of the stack) — no disabled, loading or error state |
| `testimonial-card` | Static quote card. Two states: default and hover (`{shadow.card-hover}`) only. |
| `voice-row` | default · hover (`{colors.surface-strong}` fill) · focus-visible · active/pressed · selected (`{colors.surface-strong}` fill held, 1px `{colors.ink}` left edge) · loading (preview buffering) · disabled (voice unavailable on plan) · error (preview failed) |
| `voice-icon-circular` | Decoration inside `voice-row`. One state; it inherits the row's hover and selected treatment and is never focusable on its own. |
| `pricing-tier-card` | default · hover (`{shadow.card-hover}`) · focus-visible · selected (tier chosen: 1px `{colors.ink}` border) — no pressed, disabled, loading or error state; its CTA carries those |
| `pricing-tier-featured` | Same four states as `pricing-tier-card`, inverted on `{colors.surface-dark}`. Focus ring is the same `{colors.focus}` token — it measures 4.12:1 there. |
| `text-input` | default (1px `{colors.hairline-control}`) · hover (border to `{colors.muted}`) · focus-visible (2px `{colors.ink}` border **plus** the `{colors.focus}` ring — the border alone is not a focus indicator) · disabled (`{colors.surface-strong}` fill, `{colors.muted-soft}` text) · loading (validating: trailing spinner) · error (2px `{colors.semantic-error}` border, message below in `{typography.caption}` at `{colors.semantic-error}`) — not selectable |
| `badge-pill` | Static label. One state unless used as a filter chip, in which case it adds hover, focus-visible and selected (`{colors.primary}` fill, `{colors.on-primary}` label). |
| `cta-band` | Static band. One state; the pill inside it carries the rest. |
| `footer` | Static. One state. |
| `footer-link` | default · hover (ink to `{colors.ink}`, 1px underline) · focus-visible · active/pressed · selected (current page) — no disabled, loading or error state |

### Top Navigation

**`top-nav`** — Background `{colors.canvas}`, text `{colors.ink}`, height 64px. Layout: ElevenLabs wordmark left, primary horizontal menu (Creative / Agents / Video / Pricing / Enterprise / Docs), Sign In + "Try free" primary CTA right.

### Buttons

**`button-primary`** — Near-black ink pill. Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}` (15px / 500), padding 10px × 20px, height 40px, rounded `{rounded.pill}`.

**`button-primary-active`** — Press state. Background `{colors.primary-active}`.

**`button-outline`** — Transparent pill with 1px border. Background transparent, text `{colors.ink}`, 1px `{colors.hairline-control}` border.

**`button-tertiary-text`** — Inline ink text link.

### Hero & Atmospheric

**`hero-band`** — Background `{colors.canvas}`, full-width display headline in `{typography.display-mega}` (64px / 300 / -1.92px), subhead in `{typography.body-md}`, two CTAs, and an atmospheric gradient orb behind the centered headline.

**`gradient-orb-card`** — A large card with a soft radial-gradient orb behind centered display copy. Background `{colors.canvas-soft}`, rounded `{rounded.xxl}` (24px), padding 32px. Each variant uses one of the five gradient tokens (`gradient-mint`, `gradient-peach`, `gradient-lavender`, `gradient-sky`, `gradient-rose`).

**`audio-waveform-card`** — A waveform visualization card. Background `{colors.surface-card}`, rounded `{rounded.xl}`, padding 24px. Holds a play button + waveform glyph + voice metadata.

### Cards

**`feature-card`** — 2-up or 3-up grids. Background `{colors.surface-card}`, text `{colors.ink}`, rounded `{rounded.xl}`, padding 24px, 1px hairline border.

**`product-card-stack`** — Stacked product preview cards. Background `{colors.surface-card}`, rounded `{rounded.xl}`, no padding (children fill the card edge-to-edge).

**`testimonial-card`** — Quote card. Background `{colors.surface-card}`, text `{colors.body}`, rounded `{rounded.xl}`, padding 32px.

### Voice Library

**`voice-row`** — Horizontal row in voice list. Background transparent, 1px hairline divider. Layout: 32px circular voice icon (`{component.voice-icon-circular}`) left, voice name + accent stack, optional preview button right.

**`voice-icon-circular`** — Background `{colors.surface-strong}`, rounded `{rounded.full}`, 32px diameter. Holds initials or voice glyph.

### Pricing

**`pricing-tier-card`** — Background `{colors.surface-card}`, rounded `{rounded.xl}`, padding 32px, 1px hairline border.

**`pricing-tier-featured`** — Featured tier inverts. Background `{colors.surface-dark}`, text `{colors.on-dark}`. Same shape, dark inversion.

### Forms & Tags

**`text-input`** — Background `{colors.surface-card}`, text `{colors.ink}`, rounded `{rounded.md}` (8px), padding 12px × 16px, height 44px, 1px `{colors.hairline-control}` border (the extracted `{colors.hairline-strong}` sits at 1.49:1 against the white field and is not a usable control boundary). On focus, border thickens to 2px ink and the `{colors.focus}` ring is added outside it.

**`badge-pill`** — Background `{colors.surface-strong}`, text `{colors.ink}`, type `{typography.caption-uppercase}`, rounded `{rounded.pill}`, padding 4px × 10px.

### CTA / Footer

**`cta-band`** — Pre-footer. Background `{colors.canvas}`, centered display headline in `{typography.display-lg}`, single ink pill CTA. 96px padding.

**`footer`** — Closing footer. Background `{colors.canvas}`, text `{colors.body}`. 5-column link list. 64×48px padding.

**`footer-link`** — Background transparent, text `{colors.body}`, type `{typography.body-sm}`.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted from ElevenLabs; every value comes from the shared **Cinematic** profile, used verbatim so that files sharing the profile stay comparable. Treat it as a brief, not as a finding.

The Cinematic profile fits because the brand's own signals are cinematic ones: full-bleed atmospheric gradient orbs, display type at weight 300 with sparse copy, a 96px section rhythm and no saturated interactive colour. The entrance behaviour the brand asks for is a slow bloom and type that arrives late and settles — not a tool-like instant state change.

### Tokens

| Token | Value |
|---|---|
| `{motion.duration-instant}` | 120ms |
| `{motion.duration-fast}` | 240ms |
| `{motion.duration-base}` | 400ms |
| `{motion.duration-slow}` | 600ms |
| `{motion.duration-emphasis}` | 900ms |
| `{motion.ease-standard}` | `cubic-bezier(0.22, 1, 0.36, 1)` |
| `{motion.ease-enter}` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `{motion.ease-exit}` | `cubic-bezier(0.5, 0, 0.75, 0)` |
| `{motion.stagger-step}` | 80ms |
| `{motion.duration-reduced}` | 150ms |

### Interactions

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `box-shadow` to `{shadow.card-hover}` | Shadow change applies at `{motion.duration-reduced}`; no transform |
| Press (button, voice row) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.99)`, `opacity` | Scale removed; fill change only, instant |
| Focus ring appears | `{motion.duration-instant}` | `{motion.ease-enter}` | `opacity` on the `{colors.focus}` ring | Ring appears at full opacity with no transition — never delayed or weakened |
| Page / route transition | out `{motion.duration-fast}`, in `{motion.duration-base}` | out `{motion.ease-exit}`, in `{motion.ease-enter}` | `opacity`, `transform: translateY(12px)` on the incoming band | Travel removed; cross-fade at `{motion.duration-reduced}` |
| Modal / drawer | in `{motion.duration-base}`, out `{motion.duration-fast}` | in `{motion.ease-enter}`, out `{motion.ease-exit}` | `opacity`, `transform: translateY(16px)` (drawer: `translateX`) | Travel removed; opacity only at `{motion.duration-reduced}` |
| Dropdown (nav menu) | in `{motion.duration-fast}`, out `{motion.duration-instant}` | in `{motion.ease-enter}`, out `{motion.ease-exit}` | `opacity`, `transform: translateY(-6px)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| Toast | in `{motion.duration-base}`, out `{motion.duration-fast}` | in `{motion.ease-enter}`, out `{motion.ease-exit}` | `opacity`, `transform: translateY(12px)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| List enter (voice rows, feature cards) | `{motion.duration-base}` per item, `{motion.stagger-step}` apart | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Stagger and travel removed; the whole list fades in once at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.99)` | Scale removed; opacity only at `{motion.duration-reduced}` |
| Loading (spinner, waveform skeleton) | 900ms loop (`{motion.duration-emphasis}`) | linear | `transform: rotate` / `opacity` pulse | Rotation frozen; a static 40%-opacity skeleton stands in |
| Hero display type settle (signature) | `{motion.duration-slow}`, `{motion.stagger-step}` per line | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px)` | Travel and stagger removed; type is present at full opacity on first paint |
| Gradient orb drift (brand ambience) | 24s loop — **stated as deliberate brand ambience**, the only infinite animation besides loaders | `{motion.ease-standard}` | `transform: translate3d` + `scale(1.0 → 1.04)`, `opacity` | Frozen at its first frame; the orb stays as a static bloom |

### Rules

- **`transform` and `opacity` only.** Never `width`, `height`, `top`, `left` or `margin`. The orbs scale with `transform`, not by changing their box.
- Exit is always shorter than its matching entrance (see every row above).
- Nothing animates on first paint in a way that delays content: hero type is in the DOM and legible immediately; the settle is an opacity-and-translate flourish over already-painted text.
- No infinite animation except the loaders and the gradient-orb drift, which is declared brand ambience above.
- Hover effects never move a card's box. A card gains `{shadow.card-hover}`; it does not translate.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translate), all scale, all stagger,
     the hero type settle, and the gradient-orb drift (frozen at frame 1). */
  /* Kept: opacity fades only, capped at {motion.duration-reduced} = 150ms,
     which is shorter than this profile's own duration-fast of 240ms. */
  *, *::before, *::after {
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important;
    transition-property: opacity, color, background-color, border-color, box-shadow !important;
  }
}
```

Removed: travel, scale, stagger, the hero settle, and orb drift. Kept: opacity, colour and shadow changes at `{motion.duration-reduced}` (150ms), and the focus ring, which is never animated away under any setting.

## Accessibility

### Measured contrast (WCAG 2.1 relative luminance)

| Foreground | Background | Ratio | Required | Verdict |
|---|---|---|---|---|
| `{colors.ink}` #0c0a09 | `{colors.canvas}` #f5f5f5 | 18.12:1 | 4.5:1 | Pass |
| `{colors.ink}` #0c0a09 | `{colors.surface-card}` #ffffff | 19.76:1 | 4.5:1 | Pass |
| `{colors.body}` #4e4e4e | `{colors.canvas}` #f5f5f5 | 7.63:1 | 4.5:1 | Pass |
| `{colors.muted}` #777169 | `{colors.canvas}` #f5f5f5 | **4.43:1** | 4.5:1 | **Fail** — extracted value, frozen |
| `{colors.muted}` #777169 | `{colors.surface-card}` #ffffff | 4.83:1 | 4.5:1 | Pass |
| `{colors.muted-soft}` #a8a29e | `{colors.canvas}` #f5f5f5 | **2.31:1** | 4.5:1 | **Fail** — extracted value, frozen |
| `{colors.muted-soft}` #a8a29e | `{colors.surface-card}` #ffffff | **2.52:1** | 4.5:1 | **Fail** — extracted value, frozen |
| `{colors.muted-strong}` #757068 | `{colors.canvas}` #f5f5f5 | 4.51:1 | 4.5:1 | Pass — prescribed stand-in |
| `{colors.hairline-soft}` #f0efed | `{colors.canvas}` #f5f5f5 | **1.05:1** | 3.0:1 | **Fail** — extracted value, frozen |
| `{colors.hairline}` #e7e5e4 | `{colors.canvas}` #f5f5f5 | **1.15:1** | 3.0:1 | **Fail** — extracted value, frozen |
| `{colors.hairline-strong}` #d6d3d1 | `{colors.canvas}` #f5f5f5 | **1.37:1** | 3.0:1 | **Fail** — extracted value, frozen |
| `{colors.hairline-control}` #8a8580 | `{colors.canvas}` #f5f5f5 | 3.35:1 | 3.0:1 | Pass — prescribed stand-in |
| `{colors.on-primary}` #ffffff | `{colors.primary}` #292524 | 15.17:1 | 4.5:1 | Pass |
| `{colors.on-dark}` #ffffff | `{colors.surface-dark}` #0c0a09 | 19.76:1 | 4.5:1 | Pass |
| `{colors.on-dark-soft}` #a8a29e | `{colors.surface-dark}` #0c0a09 | 7.83:1 | 4.5:1 | Pass |
| `{colors.semantic-error}` #dc2626 | `{colors.canvas}` #f5f5f5 | 4.43:1 | 4.5:1 | Marginal fail — use at 18px+ or on `{colors.surface-card}` (4.83:1) |
| `{colors.semantic-success}` #16a34a | `{colors.canvas}` #f5f5f5 | 3.02:1 | 4.5:1 | **Fail** for text — icon and 24px+ only |

**Where the real brand fails AA, plainly:** ElevenLabs' three extracted hairlines (1.05:1, 1.15:1, 1.37:1 on the canvas) are all far below the 3:1 a visible boundary needs, and `{colors.muted-soft}` at 2.31:1 is below AA for any live text. `{colors.muted}` misses AA by 0.07 at 4.43:1. These are extracted facts about the brand and are **not** corrected in place. Two prescribed parallel tokens — `{colors.hairline-control}` and `{colors.muted-strong}` — carry the jobs that need contrast; the extracted tones stay, scoped to decoration and to disabled text.

### Focus ring visibility, per surface

One ring token, `{colors.focus}` #78716c, drawn as a 2px ring with a 2px offset in the underlying surface colour.

| Surface | Ratio vs `{colors.focus}` | Verdict |
|---|---|---|
| `{colors.canvas}` #f5f5f5 | 4.40:1 | Pass |
| `{colors.canvas-soft}` #fafafa | 4.60:1 | Pass |
| `{colors.surface-card}` #ffffff | 4.80:1 | Pass |
| `{colors.surface-strong}` #f0efed | 4.17:1 | Pass |
| `{colors.surface-dark}` / `{colors.canvas-deep}` #0c0a09 | 4.12:1 | Pass |
| `{colors.surface-dark-elevated}` #1c1917 | 3.65:1 | Pass |
| `{colors.gradient-mint}` #a7e5d3 | 3.38:1 | Pass |
| `{colors.gradient-peach}` #f4c5a8 | 3.06:1 | Pass |
| `{colors.gradient-sky}` #a8c8e8 | 2.76:1 | **Fail** — needs the two-tone treatment |
| `{colors.gradient-rose}` #e8b8c4 | 2.76:1 | **Fail** — needs the two-tone treatment |
| `{colors.gradient-lavender}` #c8b8e0 | 2.60:1 | **Fail** — needs the two-tone treatment |

A single mid-luminance ring is used rather than a `focus` / `focus-on-dark` pair because this file documents both an off-white canvas and a near-black band, and one warm stone clears 3:1 on both. Over the pastel gradient orbs and over atmospheric photography — neither of which has a measurable single colour — the ring is drawn **two-tone**: 2px `{colors.focus}` with a 1px outer edge in `{colors.ink}`, which measures 10.71:1 against the weakest orb (lavender) and carries the indicator wherever the stone alone falls short.

### Minimum tap target

- `button-primary` and `button-outline` are 40px tall. 40px clears the 24×24px WCAG 2.2 minimum and the 44px iOS guideline is met by the 4px vertical margin the 96px band rhythm already provides, giving a 48px effective target.
- `text-input` is 44px tall — passes unaided.
- `voice-icon-circular` is 32px, below 44px on its own. It is decoration and not focusable; the focusable target is the whole `voice-row`, whose 12px vertical padding brings it to 48px.
- `badge-pill` as a static label has no target requirement. As a filter chip its padding must be raised to give a 44px target.
- **Not verifiable here.** Tap-target size is a rendered-page measurement; every figure above is read off this file's own declared heights and paddings, not off a live page.

### Reduced motion

Covered in full under Motion & Animation. In summary: all travel, scale and stagger are removed, the gradient-orb ambience is frozen, loaders stop rotating and show a static skeleton, and opacity fades are capped at `{motion.duration-reduced}` (150ms). The focus ring is never animated and never suppressed.

### Known accessibility limits of this document

Overlap, horizontal overflow, clipping, real tap-target size, frame rate and layout shift cannot be judged from a document. Nothing above claims to measure them.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (ink pill) for primary CTAs.
- Use Waldenburg Light at weight 300 for every display headline. Never bold.
- Use Inter at +0.15-0.18px tracking for body — the editorial dialect.
- Use atmospheric gradient orbs (mint/peach/lavender/sky/rose) as decoration only.
- Use the pill shape for every CTA and badge.
- Use `{colors.hairline-control}` for any boundary a user has to see, and keep the three extracted hairlines for decoration.
- Let entrances take their time: `{motion.duration-base}` to `{motion.duration-slow}` with `{motion.ease-enter}`. The slow settle is the brand.

### Don't
- Don't introduce a saturated brand action color. Ink pill is the only CTA color.
- Don't bold display copy. Display sits at weight 300 — bolding shifts the brand voice from editorial to consumer-marketing.
- Don't use gradient orbs as button fills, text colors, or component backgrounds. They are pure atmosphere.
- Don't use sharp `{rounded.none}` (0px) on CTAs. Pill geometry is the brand button.
- Don't drop body Inter to weight 300 to match Waldenburg — body stays at 400/500 for legibility.
- Don't extract a CTA color from a third-party widget (cookie consent, OneTrust). The brand's CTA color is what appears on actual product CTAs.
- Don't give the focus ring a brand colour. The brand has no accent; `{colors.focus}` is a neutral warm stone on purpose.
- Don't animate `width`, `height`, `top`, `left` or `margin`. Orbs and cards move and scale with `transform` only.
- Don't use `{colors.muted-soft}` for live text on a light surface — 2.31:1. It is disabled text and dark-band muted text only.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 640px | Hero h1 64→32px; feature cards 1-up; nav hamburger; gradient orbs shrink. |
| Tablet | 640–1024px | Hero h1 48px; feature cards 2-up. |
| Desktop | 1024–1280px | Full hero h1 64px; feature cards 3-up. |
| Wide | > 1280px | Content caps at 1200px. |

### Touch Targets
- Primary pill at 40px declared height — above the 24×24px WCAG 2.2 minimum; the surrounding band rhythm brings the effective target to 48px.
- Voice icon circles 32px — not focusable themselves; the padded row is the 48px tap target.
- These are the file's own declared values. Real tap-target size needs a rendered page and is not measured here.

### Collapsing Strategy
- Top nav switches to hamburger below 768px.
- Feature grid: 3-up → 2-up → 1-up.
- Gradient orbs reduce diameter at every breakpoint but never disappear.

## Iteration Guide

1. Focus on a single component at a time.
2. CTAs default to `{rounded.pill}`. Cards use `{rounded.xl}` (16px).
3. Variants live as separate entries.
4. Use `{token.refs}` everywhere — never inline hex.
5. States are documented in the Components state table — start there, not from scratch.
6. Waldenburg 300 for display, Inter 400/500 for body.
7. Gradient orbs scoped to atmospheric decoration.

## Known Gaps

- Waldenburg is a licensed typeface; EB Garamond / GT Sectra are documented substitutes.
- Animation timings (orb drift, waveform pulse, hero entrance) were never measured from the live site. The Motion & Animation section is a **prescribed** Cinematic-profile brief, not an extracted one.
- `{colors.focus}`, `{colors.hairline-control}` and `{colors.muted-strong}` are prescribed, not extracted. The real brand documents no focus ring and no accessible boundary tone.
- `{colors.semantic-success}` (3.02:1 on the canvas) and `{colors.semantic-error}` (4.43:1) were read off a validation mockup; neither was seen at a known type size, so the size at which each is defensible is unverified.
- In-product surfaces (voice library editor, agent playground) only partially captured via marketing mockups.
- Form validation states beyond focus not visible on captured surfaces.
