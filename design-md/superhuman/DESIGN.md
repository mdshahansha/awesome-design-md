---
version: alpha
name: Superhumon-Inspired-design-analysis
description: An inspired interpretation of Superhumon's design language — a fast-email productivity brand split between an editorial dark hero (deep indigo navy with violet-sky atmospheric backdrop and a portrait subject) and a quiet white content body with off-warm-grey ink. The system uses a single proprietary variable display sans, heavy weight 460–540 with tight tracking, and a deep-teal closing CTA band that breaks the indigo/white rhythm with a warm dark interlude. Buttons are tight rounded rectangles, pricing is sober and dense, and the brand reads more like a high-end newsletter than a SaaS app.

colors:
  primary: "#1b1938"
  primary-deep: "#0e0c1f"
  on-primary: "#ffffff"
  ink: "#292827"
  ink-mute: "#73706d"
  ink-faint: "#9a9794"
  canvas: "#ffffff"
  canvas-soft: "#fafaf8"
  surface-violet-soft: "#c9b4fa"
  surface-teal-deep: "#0e3030"
  surface-teal-mid: "#155555"
  hairline: "#e8e4dd"
  hairline-dark: "#3f3a52"
  on-dark-mute: "#bcbac9"
  on-dark-faint: "#5a5772"
  focus: "#1b1938"
  focus-on-dark: "#c9b4fa"

typography:
  display-xxl:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 64px
    fontWeight: 540
    lineHeight: 0.96
    letterSpacing: 0
  display-xl:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 460
    lineHeight: 0.96
    letterSpacing: -1.32px
  display-lg:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 540
    lineHeight: 1.14
    letterSpacing: -0.63px
  display-md:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 460
    lineHeight: 1.1
    letterSpacing: -0.315px
  heading-lg:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 460
    lineHeight: 1.2
    letterSpacing: -0.4px
  body-lg:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 540
    lineHeight: 1.5
    letterSpacing: -0.135px
  body-md:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 460
    lineHeight: 1.5
    letterSpacing: 0
  body-strong:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18.72px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  button-cap:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0
  caption:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 460
    lineHeight: 1.4
    letterSpacing: 0
  micro:
    fontFamily: "'Super Sans VF', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 540
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  huge: 64px

motion:
  duration-instant: 60ms
  duration-fast: 100ms
  duration-base: 150ms
  duration-slow: 220ms
  duration-emphasis: 300ms
  ease-standard: cubic-bezier(0.2, 0, 0.2, 1)
  ease-enter: cubic-bezier(0, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 20ms
  duration-reduced: 100ms

components:
  button-primary-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  button-primary-dark-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  button-on-dark-pill:
    backgroundColor: "{colors.surface-violet-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
  button-secondary-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  button-on-teal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.surface-teal-deep}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
  card-feature-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-pricing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-pricing-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-teal-band:
    backgroundColor: "{colors.surface-teal-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.lg}"
    padding: 64px
  card-feature-row:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  pill-tab-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-cap}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  nav-bar-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  link-on-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
  footer-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-mute}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 24px
---

## Overview

Superhumon's marketing pages open in an editorial dark register: a deep indigo navy `{colors.primary}` (`#1b1938`) canvas overlaid with a soft violet-and-sky atmospheric backdrop and a half-bleed portrait subject (often a person looking off-frame, photographed at twilight). Headlines render in `{typography.display-xxl}` (Super Sans VF at 64px / weight 540) with negative tracking, set in white over the indigo. A single rounded-rectangle CTA button anchors each band — never two, never three.

The body of every page flips to white. `{colors.canvas}` (`#ffffff`) takes over below the hero, with body type in `{colors.ink}` (`#292827` — a slightly warm dark grey, never pure black) and feature rows alternating between white and `{colors.canvas-soft}` (a barely-tinted off-white). Pricing tiers sit on this white surface; the featured tier inverts to the indigo navy, completing the brand's binary polarity.

Every page closes with a **deep-teal CTA band** (`{colors.surface-teal-deep}` — `#0e3030`). The teal is a single chromatic interlude: rich, almost-black green-blue, that breaks up what would otherwise be an indigo/white-only page. The teal band always contains the closing CTA in `{typography.display-lg}` paired with a single white-pill button.

Typography runs **Super Sans VF** — a proprietary variable display sans — at unusual mid-weights (460, 540, 600). The variable axes let the brand pick precise sub-default weights that read as warmer and more human than typical 400/500/700 SaaS scales. Display sizes use negative letter-spacing of -1.32px to -0.315px depending on size; line-heights are unusually tight (0.96 on 48px display).

**Key Characteristics:**
- Three-canvas system: indigo navy (`{colors.primary}`) for hero, white (`{colors.canvas}`) for body, deep teal (`{colors.surface-teal-deep}`) for closing CTA.
- Half-bleed portrait subject in the hero with violet-sky atmospheric backdrop — the brand uses a person looking off-frame as a recurring visual.
- Single CTA per band; the marketing pages never crowd actions.
- Super Sans VF at sub-default weights (460, 540, 600) — the brand's typographic warmth signature.
- Tight line-heights (0.96) on display sizes — vertical compression as editorial density.
- Off-warm-grey body ink (`#292827`) — never pure black; the brand's quiet warmth.
- Pill-shaped on-hero CTA in pale violet (`{colors.surface-violet-soft}`); rounded-rectangle CTAs everywhere else.

## Colors

> **Source pages:** home (`/`), `/products/go-ai-assistant`, `/contact-sales`, `/plans`.

### Brand & Accent
- **Primary Indigo Navy** (`{colors.primary}` — `#1b1938`): The brand's primary surface and CTA color. Hero canvas, filled rounded-rectangle button, featured pricing tier.
- **Indigo Deep** (`{colors.primary-deep}` — `#0e0c1f`): Pressed-state lift / deeper navy used in hero gradient stops.
- **Surface Violet Soft** (`{colors.surface-violet-soft}` — `#c9b4fa`): The hero pill-button fill — pale violet over the indigo canvas. Also appears in atmospheric backdrops.
- **Surface Teal Deep** (`{colors.surface-teal-deep}` — `#0e3030`): The signature closing-CTA band color. Rich green-blue, almost black.
- **Surface Teal Mid** (`{colors.surface-teal-mid}` — `#155555`): Slightly lifted teal for nested chrome inside the band.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): Default body background.
- **Canvas Soft** (`{colors.canvas-soft}` — `#fafaf8`): Barely-warm off-white for alternating feature-row bands.
- **Hairline** (`{colors.hairline}` — `#e8e4dd`): 1px borders, slightly warm grey.
- **Hairline Dark** (`{colors.hairline-dark}` — `#3f3a52`): 1px borders on dark surfaces.

### Text
- **Ink** (`{colors.ink}` — `#292827`): Default body text. Warm dark grey, never pure black.
- **Ink Mute** (`{colors.ink-mute}` — `#73706d`): Secondary text, captions.
- **Ink Faint** (`{colors.ink-faint}` — `#9a9794`): Tertiary / disabled text.
- **On Primary** (`{colors.on-primary}` — `#ffffff`): Text on dark navy / teal surfaces.
- **On Dark Mute** (`{colors.on-dark-mute}` — translucent white): Secondary text on dark.
- **On Dark Faint** (`{colors.on-dark-faint}` — translucent white): Tertiary text on dark.

## Typography

### Font Family

The display and UI tier is **Super Sans VF** — a proprietary variable sans (variable axes for weight, with the brand using sub-default 460 / 540 / 600 weights). Fallback chain is the system font stack.

For substitution use **Inter Variable** (open-source) at weight 460 / 540 / 600 — Inter's variable axes match Super Sans VF's behavior closely. Avoid fixed-weight Inter at 400 / 500 / 600 — the brand specifically picks the in-between weights.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 64px | 540 | 0.96 | 0 | Hero headline |
| `{typography.display-xl}` | 48px | 460 | 0.96 | -1.32px | Section opener on light surfaces |
| `{typography.display-lg}` | 28px | 540 | 1.14 | -0.63px | Sub-section / feature title |
| `{typography.display-md}` | 22px | 460 | 1.1 | -0.315px | Card title |
| `{typography.heading-lg}` | 20px | 460 | 1.2 | -0.4px | Compact card title |
| `{typography.body-lg}` | 18px | 540 | 1.5 | -0.135px | Marketing body lead |
| `{typography.body-md}` | 16px | 460 | 1.5 | 0 | Default UI body |
| `{typography.body-strong}` | 18.72px | 700 | 1.5 | 0 | Emphasized body |
| `{typography.button-md}` | 16px | 700 | 1.0 | 0 | Rounded-rectangle button label |
| `{typography.button-cap}` | 14px | 600 | 1.0 | 0 | Compact button label |
| `{typography.caption}` | 14px | 460 | 1.4 | 0 | Helper, footnote |
| `{typography.micro}` | 12px | 540 | 1.4 | 0 | Pill label, fine print |

### Principles
- **Sub-default weights.** The brand picks 460 / 540 / 600 instead of 400 / 500 / 700 — a quiet warmth in the typography that distinguishes it from default SaaS systems.
- **Tight display leading.** 0.96 on 48–64px display — the type stacks unusually compact.
- **Negative tracking on display sizes.** -1.32px at 48px scaling proportionally — tightens the variable letterforms into editorial density.

### Note on Font Substitutes
**Inter Variable** (open-source via Google Fonts) is the recommended substitute. Set `font-variation-settings: "wght" 540` for display, 460 for body — Inter's variable axes match. Avoid fixed-weight Inter; the in-between weights are the brand's signature.

## Layout

### Spacing System
- **Base unit**: 8px (with 2 / 4 / 12 sub-tokens for fine work).
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.huge}` 64px.
- **Section padding**: 64–96px on most sections; closing teal band uses 96–128px for editorial weight.
- **Card internal padding**: 32px on pricing cards; 24px on alternating feature rows.

### Grid & Container
- Hero spans full viewport width with the violet-sky backdrop edge-to-edge; content centers in a ~960px column.
- Body content centers in ~960–1100px.
- Pricing collapses 3-up → 2-up → 1-up at 1024 / 768 breakpoints.

### Whitespace Philosophy
The brand uses generous editorial whitespace on both polarities — dark hero and white body. Section gaps tend toward 96px; the teal closing band gets up to 128px of vertical air. The whitespace itself is part of the brand's "considered, slow-tempo" feel.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default surface |
| 1 | `box-shadow: 0 1px 3px rgba(0,0,0,0.08)` | Subtle card lift |
| 2 | `box-shadow: 0 8px 24px rgba(0,0,0,0.12)` | Floating panels, modals |
| 3 | Atmospheric backdrop (violet-sky over indigo) | The hero's depth medium |

### Decorative Depth
The hero's depth is the **violet-sky atmospheric backdrop** — a soft indigo-to-violet-to-sky-blue radial wash that sits behind the portrait subject. Implemented as a CSS radial gradient or large background image. Below the hero, depth is minimal — the white canvas is flat.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Hairline tags |
| `{rounded.sm}` | 6px | Form inputs |
| `{rounded.md}` | 8px | Buttons (the brand's signature button shape — rounded rectangle, never pill) |
| `{rounded.lg}` | 12px | Pricing cards, feature cards |
| `{rounded.xl}` | 16px | Modal dialogs, large feature cards |
| `{rounded.full}` | 9999px | Pill tabs in feature row, hero CTA |

### Photography Geometry
The hero uses **half-bleed portrait subjects** — a person photographed at twilight, looking off-frame, occupying the right half of the hero. The portrait extends edge-to-edge vertically and stops mid-canvas horizontally; type sits on the left side. Other photography is rare; product UI mockups handle most other illustrative needs.

## Components

Only the pressed state is extracted (`button-primary-dark-pressed`). The **States** row under each entry is **prescribed** from this file's own tokens to complete the state contract; it was not measured from the live site. The focus ring in every state row is `{colors.focus}` on light grounds and `{colors.focus-on-dark}` on the indigo and teal grounds, drawn 2px outside the control with a 2px offset.

### Buttons

**`button-primary-dark`** — the dominant rounded-rectangle CTA on white surfaces.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button-md}`, padding `{spacing.md} {spacing.xl}` (12px 20px), rounded `{rounded.md}` 8px.
- Pressed state `button-primary-dark-pressed` shifts to `{colors.primary-deep}`.
- States: default · hover (lift to `{colors.primary-deep}`, `{motion.duration-fast}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (`button-primary-dark-pressed`) · disabled (fill `{colors.hairline}`, label `{colors.ink-faint}`) · loading (label holds, 1.5s indeterminate opacity pulse on a `{colors.on-primary}` dot row) · error (inherits the form's error message; the button itself keeps default fill).

**`button-on-dark-pill`** — the hero CTA in pale violet pill shape.
- Background `{colors.surface-violet-soft}`, text `{colors.primary}`, same typography, padding 12px 20px, rounded `{rounded.full}`. The pill shape only appears on the hero — body CTAs use the rounded rectangle.
- States: default · hover (opacity 0.92) · focus-visible (2px `{colors.focus-on-dark}` ring on the indigo ground, 2px offset) · active/pressed (opacity 0.85) · disabled (opacity 0.4, no pointer) · loading (indeterminate opacity pulse on the label) · error (not applicable — the hero CTA carries no validation).

**`button-secondary-outline`** — outline alternative on white.
- Background `{colors.canvas}`, text `{colors.ink}`, 1px solid `{colors.hairline-dark}` border, same shape as `button-primary-dark`. The border measures 10.83:1 on `{colors.canvas}` — this is the one boundary tone in the palette that clears the 3:1 minimum on white.
- States: default · hover (border `{colors.primary}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (background `{colors.canvas-soft}`) · disabled (border `{colors.hairline}`, label `{colors.ink-faint}`) · loading (label swaps to a pulsing dot row) · selected (border `{colors.primary}` 2px, used where the outline button acts as a segmented choice).

**`button-on-teal`** — CTA inside the closing teal band.
- Background `{colors.canvas}`, text `{colors.surface-teal-deep}`, rounded-rectangle, same typography.
- States: default · hover (opacity 0.92) · focus-visible (2px `{colors.focus-on-dark}` ring on the teal ground, 2px offset) · active/pressed (opacity 0.85) · disabled (opacity 0.4) · loading (indeterminate opacity pulse) · error (not applicable).

### Cards & Containers

**`card-feature-light`** — feature card on white.
- Background `{colors.canvas}`, padding `{spacing.xxl}`, rounded `{rounded.lg}`, 1px `{colors.hairline}` border (extracted; 1.27:1 on `{colors.canvas}`, so the border reads as decoration rather than a perceivable boundary — see Accessibility).
- States: default · hover (no fill change; the card is static copy) · focus-visible (2px `{colors.focus}` ring where the whole card is a link target). Genuinely a two-to-three-state element: no pressed, disabled, loading, selected or error state exists for it.

**`card-pricing`** — standard pricing tier card.
- Background `{colors.canvas}`, padding `{spacing.xxl}`, rounded `{rounded.lg}`, 1px `{colors.hairline}` border (extracted; 1.27:1 on white — decorative, see Accessibility).
- States: default · hover (elevation 0 → 1) · focus-visible (2px `{colors.focus}` ring on the tier's CTA, not the card) · selected (the chosen billing tier takes a 2px `{colors.primary}` border) · loading (price row shows a pulsing placeholder block while plan data resolves) · disabled (a tier unavailable on the current region drops to opacity 0.5 with `{colors.ink-faint}` copy) · error (plan fetch failure replaces the price row with a `{colors.ink}` retry line).

**`card-pricing-featured`** — inverted indigo featured tier.
- Background `{colors.primary}`, text `{colors.on-primary}`, otherwise identical to `card-pricing`.
- States: inherits every `card-pricing` state, with the focus ring swapped to `{colors.focus-on-dark}` and the selected border to `{colors.surface-violet-soft}`.

**`card-teal-band`** — the closing CTA band on every page.
- Background `{colors.surface-teal-deep}`, text `{colors.on-primary}`, padding `{spacing.huge}` 64px, rounded `{rounded.lg}` 12px (often radius-less in practice when full-bleed). Holds a single closing headline in `{typography.display-lg}` and a `button-on-teal`.

**`card-feature-row`** — alternating feature-row card on the body.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.xl}` 24px, rounded `{rounded.md}` 8px. Used in pairs/triplets to explain features below the hero.
- States: default · hover (background holds; the inner thumbnail scales to 1.01) · focus-visible (2px `{colors.focus}` ring where the row links out) · selected (row tied to the active `pill-tab-light` carries a 2px `{colors.primary}` left rule). No pressed, disabled, loading or error state.

### Inputs & Forms

**`text-input`** — standard form input.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, padding `{spacing.sm}+ {spacing.md}` (10px 12px), rounded `{rounded.sm}` 6px, 1px `{colors.hairline}` border (extracted). At 1.27:1 on `{colors.canvas}` that border is the input's only boundary and it does not meet the 3:1 non-text minimum — the real brand fails AA here. Where a perceivable boundary is required, use `{colors.hairline-dark}` (10.83:1 on white); re-binding the extracted value is held under Needs approval in the audit report.
- States: default · hover (border `{colors.ink-faint}`) · focus-visible (2px `{colors.focus}` ring, 2px offset, border `{colors.primary}`) · active (caret visible, border holds) · disabled (background `{colors.canvas-soft}`, label `{colors.ink-faint}`, no caret) · loading (field locks and shows a pulsing right-aligned dot row during async validation) · error (border and helper text `{colors.ink}` with a prescribed `{colors.primary}` 2px border — the brand defines no red, see Known Gaps) · selected (text selection uses `{colors.surface-violet-soft}` as the highlight fill, `{colors.ink}` ink, 7.98:1).

### Navigation

**`nav-bar-dark`** — top nav over the indigo hero.
- Background `{colors.primary}`, text `{colors.on-primary}`, padding `{spacing.lg} {spacing.xl}`. Logo on the left, nav center, "Get Started" `button-on-dark-pill` on the right.
- States per nav item: default · hover (opacity 0.8) · focus-visible (2px `{colors.focus-on-dark}` ring) · active/pressed (opacity 0.7) · selected (current page keeps full opacity with a 1px `{colors.on-primary}` underline). No disabled, loading or error state.

**`nav-bar-light`** — top nav on body / pricing pages.
- Background `{colors.canvas}`, text `{colors.ink}`, otherwise same structure with `button-primary-dark` on the right.
- States per nav item: default · hover (`{colors.ink-mute}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed (`{colors.ink}`) · selected (1px `{colors.primary}` underline). No disabled, loading or error state.

### Pills, Tags, and Chips

**`pill-tab-light`** — feature-row tab selector.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.button-cap}`, padding `{spacing.sm} {spacing.lg}`, rounded `{rounded.full}`. Used in the feature category picker (Mail / Channels / Code / AI / Calendar etc.) below the hero.
- States: default · hover (background `{colors.canvas-soft}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (background `{colors.hairline}`) · selected (fill `{colors.primary}`, label `{colors.on-primary}`, 16.9:1) · disabled (label `{colors.ink-faint}`) · loading (tab row shows pulsing placeholder pills while its panel resolves). No error state.

### Signature Components

**Half-Bleed Portrait Hero** — a person photographed at twilight, occupying the right half of the indigo hero with violet-sky atmospheric backdrop behind. Type and CTA sit on the left side. The portrait is the brand's recurring visual signature.

**Closing Teal Band** — every page closes with a `card-teal-band` containing a `{typography.display-lg}` closing headline and a single `button-on-teal`. The teal is the page's resolving chord.

**`link-on-light`** — inline links on body.
- Text `{colors.ink}` rendered in `{typography.body-md}` with persistent underline.
- States: default · hover (`{colors.ink-mute}`, underline holds) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (`{colors.primary}`) · visited (no distinct tone; the brand does not differentiate). No disabled, loading, selected or error state.

**`footer-light`** — site-wide footer.
- Background `{colors.canvas}`, text `{colors.ink-mute}`, type `{typography.caption}`, padding `{spacing.huge} {spacing.xl}` (64px 24px). Holds 4 columns of link groups, social icons, and a small legal/copyright row.
- States per footer link: default (`{colors.ink-mute}`, 4.92:1 on white) · hover (`{colors.ink}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (`{colors.primary}`). No disabled, loading, selected or error state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or choreography here was extracted; the values are the shared **Crisp** profile, chosen because the product is a keyboard-driven email client whose entire promise is speed — a state change must read as already finished. The marketing pages' editorial whitespace argues for a slower register, but the product it sells does not; see the audit report for the argument.

All values resolve to the `motion:` group: `{motion.duration-instant}` 60ms · `{motion.duration-fast}` 100ms · `{motion.duration-base}` 150ms · `{motion.duration-slow}` 220ms · `{motion.duration-emphasis}` 300ms · `{motion.ease-standard}` · `{motion.ease-enter}` · `{motion.ease-exit}` · `{motion.stagger-step}` 20ms · `{motion.duration-reduced}` 100ms.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav item, link) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `background-color` | Unchanged — no travel to remove |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` (no scale — the brand's buttons do not squash) | Unchanged |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears with no transition |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` only; no cross-fade travel | Opacity fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px → 0)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform` | Travel removed; opacity only at `{motion.duration-reduced}` |
| Dropdown / menu | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: scaleY(0.98 → 1)` from the top edge | Scale removed; opacity only at `{motion.duration-reduced}` |
| Toast | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(6px → 0)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| List enter (pricing tiers, feature rows) | `{motion.duration-base}`, `{motion.stagger-step}` 20ms per item | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px → 0)` | Stagger and travel removed; one opacity fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` | Opacity at `{motion.duration-reduced}` |
| Loading (button, price row, tab panel) | 1.5s indeterminate loop | `{motion.ease-standard}` | `opacity` pulse 1 → 0.4 → 1 on a dot row or placeholder block | Loop frozen; a static placeholder at 0.6 opacity remains |
| Hero atmospheric backdrop | brand ambience, 20s loop, stated as ambience | linear | `opacity` and `transform: scale(1 → 1.02)` on the violet-sky wash | Frozen at its first frame |

### Motion Rules
- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin`.
- Every exit is shorter than its matching entrance (`{motion.duration-fast}` out against `{motion.duration-base}` in).
- Nothing animates on first paint in a way that delays content: the hero headline and CTA render at full opacity, and the list-enter stagger applies only to below-fold bands as they scroll into view.
- The only infinite animations are the loading pulse and the hero's atmospheric backdrop, which is deliberate brand ambience and is declared as such above.
- Travel distances stay at 6–8px. The brand's register is editorial stillness; large slides would read as a different product.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translate), all scale, the list stagger,
     and the hero's ambient wash, which freezes at its first frame. */
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;  /* {motion.duration-reduced} */
    transition-property: opacity, background-color, border-color, color !important;
    scroll-behavior: auto !important;
  }
}
```

What remains: opacity fades and colour changes at `{motion.duration-reduced}` 100ms, the focus ring, and a static loading placeholder. What is removed: every `translate` and `scale`, the `{motion.stagger-step}` sequencing, and the hero ambience.

## Accessibility

### Measured contrast (WCAG 2.1 relative luminance)

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` #292827 on `{colors.canvas}` #ffffff | 14.72:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` #fafaf8 | 14.08:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.surface-violet-soft}` #c9b4fa | 7.98:1 | 4.5 | Pass |
| `{colors.ink-mute}` #73706d on `{colors.canvas}` | 4.92:1 | 4.5 | Pass |
| `{colors.ink-mute}` on `{colors.canvas-soft}` | 4.71:1 | 4.5 | Pass |
| `{colors.on-primary}` #ffffff on `{colors.primary}` #1b1938 | 16.9:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.surface-teal-deep}` #0e3030 | 14.15:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.surface-teal-mid}` #155555 | 8.53:1 | 4.5 | Pass |
| `{colors.on-dark-mute}` #bcbac9 on `{colors.primary}` | 8.86:1 | 4.5 | Pass |
| `{colors.primary}` on `{colors.surface-violet-soft}` (hero pill label) | 9.17:1 | 4.5 | Pass |
| `{colors.hairline-dark}` #3f3a52 on `{colors.canvas}` | 10.83:1 | 3.0 | Pass |
| `{colors.focus}` #1b1938 on `{colors.canvas}` | 16.9:1 | 3.0 | Pass |
| `{colors.focus-on-dark}` #c9b4fa on `{colors.primary}` | 9.17:1 | 3.0 | Pass |

### Known contrast failures — the real brand does not pass AA at these points

These are extracted values, frozen as facts about the brand. They are stated here rather than corrected.

- `{colors.hairline}` #e8e4dd on `{colors.canvas}` #ffffff measures **1.27:1**, far below the 3:1 non-text minimum. This is the brand's only light-ground hairline, and it is the sole boundary of `text-input`, `card-pricing` and `card-feature-light`. On the real site those boundaries are decorative, not perceivable: **the brand fails WCAG 1.4.11 here.** Where a boundary must be seen, `{colors.hairline-dark}` (10.83:1) is the palette's own passing tone and needs no new token.
- `{colors.hairline}` on `{colors.canvas-soft}` #fafaf8 measures **1.21:1** — the alternating feature-row band and its hairline are effectively one surface.
- `{colors.hairline}` on `{colors.surface-violet-soft}` #c9b4fa measures **1.45:1**. This pair is a harness artefact rather than a real rendering: the violet is the hero pill-button fill and the atmospheric wash, and no hairline is ever drawn on it. Recorded for completeness.
- `{colors.hairline-dark}` #3f3a52 on `{colors.primary}` #1b1938 measures **1.56:1**. The token is documented as the dark-surface border, so the brand's dark-ground dividers are below the 3:1 minimum too.
- `{colors.ink-faint}` #9a9794 on `{colors.canvas}` measures **2.91:1**, below 4.5:1. Defensible only as disabled-control text (WCAG sets no minimum on disabled) or at 24px+ where 3:1 applies; it fails as tertiary body copy at 14–16px, which is how the Colors section describes it.
- `{colors.on-dark-faint}` #5a5772 on `{colors.primary}` measures **2.45:1**, below 4.5:1. Same scope: disabled or decorative on dark, never running text.
- `{colors.canvas-soft}` #fafaf8 against `{colors.canvas}` #ffffff measures **1.05:1**. The two page layers are not distinguishable by luminance alone; the band change reads only through position and padding.
- `{colors.surface-teal-mid}` #155555 against `{colors.surface-teal-deep}` #0e3030 measures **1.66:1** — nested teal chrome is a decorative step, not a perceivable boundary.

### Focus ring

The brand ships no focus ring, so both rings here are **prescribed** — each reuses a tone the palette already owns rather than introducing a new brand colour.

- `{colors.focus}` reuses the indigo navy `{colors.primary}` #1b1938. Drawn on all light grounds: `{colors.canvas}` 16.9:1, `{colors.canvas-soft}` 16.17:1, `{colors.surface-violet-soft}` 9.17:1.
- `{colors.focus-on-dark}` reuses the pale violet `{colors.surface-violet-soft}` #c9b4fa. Drawn on the dark grounds: `{colors.primary}` 9.17:1, `{colors.surface-teal-deep}` 7.68:1, `{colors.surface-teal-mid}` 4.63:1.
- Geometry: 2px ring, 2px offset, drawn **outside** the control so it is judged against the surface behind it, as WCAG 2.2 Focus Appearance asks. Two rings are needed because this file documents both a light default body and dark indigo/teal signature surfaces; no single tone clears 3:1 on #ffffff and #0e3030 at once.
- Over the half-bleed hero portrait, which has no measurable colour, the ring is two-tone: 2px `{colors.focus-on-dark}` with a 1px `{colors.primary}` outer edge.

### Tap targets

Buttons and form fields are specified at ≥ 44×44px (12px vertical padding on a 16px line-height label; fields hold a 44px minimum height) — see Responsive Behavior. This is a specification, not a measurement: no page was rendered for this audit, so actual tap-target size is unverified.

### Reduced motion

Every entrance and exit respects `@media (prefers-reduced-motion: reduce)` as defined in Motion & Animation: travel, scale, stagger and the hero ambience are removed, and opacity fades are capped at `{motion.duration-reduced}` 100ms.

### Other

- Body copy never falls below 14px (`{typography.caption}`); `{typography.micro}` 12px is reserved for pill labels and fine print.
- Type at weight 460 on a 0.96 line-height display size is a tight stack; the brand accepts it as editorial density. No line-height below 0.96 anywhere.
- The brand defines no error, success or warning colour. Validation state is carried by copy and by a `{colors.primary}` 2px border, which means error state is signalled by shape and text rather than hue — acceptable for 1.4.1 but it gives the user no colour signal at all.

### Remaining measured failures

Every ratio below is computed with WCAG 2.1 relative luminance from this file's
own frontmatter hexes. These pairs were measured but not stated elsewhere in this
section. No colour and no `components:` binding was changed to produce them: the
values are extracted and frozen, so stating the number is the whole of the remedy
available without a brand-owner decision. Where a fix would mean altering a brand
tone or re-pointing a binding, that decision is listed in the audit's Needs
approval set, not taken here. Where a row says the ground was substituted, the
component states no `backgroundColor` of its own, so the page floor was measured
in its place; if the real ground is imagery, a gradient or an overlay, this file
does not record it, and the ratio describes the substitution rather than the
rendered result.

| Foreground / Background | Ratio | Required | Status |
|---|---:|---:|---|
| `{colors.ink-faint}` (`#9a9794`) on `{colors.canvas-soft}` (`#fafaf8`) | 2.78:1 | 4.5:1 | Fail — secondary text on surface, all tones |

## Do's and Don'ts

### Do
- Pair every hero with the violet-sky atmospheric backdrop and a half-bleed portrait subject when possible.
- Render display tiers at sub-default weights (460 / 540) — the warmth is the typographic signature.
- Use rounded-rectangle CTAs at 8px radius everywhere except the hero (where pill-shaped is the rule).
- Close every marketing page with a deep-teal CTA band.
- Use warm dark grey `{colors.ink}` for body text — never pure black.
- Apply tight 0.96 line-height on display sizes; the editorial compression is the brand.

### Don't
- Don't use pill-shaped buttons in the body of the page; the pill is hero-only.
- Don't bump display weight above 540 unless using `body-strong` (700) for emphasized inline body.
- Don't render body text in pure black — the warm grey `#292827` is part of the brand.
- Don't omit the closing teal band — every marketing page closes with it.
- Don't introduce additional accent colors beyond indigo, violet-soft, teal, and the off-warm-greys.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1440px | Half-bleed portrait at full scale; teal band 128px tall |
| Desktop | 1024–1440px | Default content max-width; pricing 3-up |
| Tablet | 768–1023px | Pricing 2-up; portrait crops tighter |
| Mobile | < 768px | Pricing 1-up; hamburger nav; display drops 64 → 36px |

### Touch Targets
- Buttons hit ≥ 44×44px on mobile via 12px vertical padding × 16px line-height. WCAG AAA.
- Form fields stay at the 44px minimum height.

### Collapsing Strategy
- Display tiers stair-step 64 → 48 → 36 → 28 → 22px.
- Half-bleed portrait crops to head-and-shoulders on mobile; atmospheric backdrop simplifies.
- Pricing tiers stair-step 3-up → 2-up → 1-up.
- Top nav collapses to hamburger below 768px.
- Closing teal band reduces vertical padding from 128 → 64px on mobile.

### Image Behavior
Hero portrait uses `srcset` with desktop / mobile crops — desktop favors the full half-bleed composition; mobile crops to head-and-shoulders.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly.
3. Run `npx @google/design.md lint DESIGN.md` after edits.
4. Default body to `{typography.body-md}`; reserve `{typography.body-lg}` for marketing leads.
5. Keep the three-canvas rhythm (indigo / white / teal) — adding a fourth canvas color breaks the system.
6. The closing teal band is non-negotiable — every marketing page resolves there.

## Known Gaps

- **Motion is entirely prescribed.** No duration, easing or choreography in this file was extracted from the live site. The `motion:` group is the shared **Crisp** profile; the interaction table is a reasoned fit to the brand, not an observation.
- **State coverage is prescribed.** Only `button-primary-dark-pressed` is an extracted state. Every other state row in Components was derived from this file's own tokens.
- **No focus ring exists in the brand.** `{colors.focus}` and `{colors.focus-on-dark}` reuse `{colors.primary}` and `{colors.surface-violet-soft}`; the real site's focus treatment is unverified.
- **No semantic palette.** The brand defines no error, success, warning or info colour, and the Don'ts forbid adding accents. The error states above therefore borrow `{colors.primary}`. A real product would need a semantic tone, and that is a brand decision, not an audit one.
- **`{colors.on-dark-mute}` and `{colors.on-dark-faint}` are described in the Colors section as "translucent white" but carry flat hexes** (#bcbac9, #5a5772). The hexes are what is measurable; the underlying alpha values were not captured.
- **Shadow values have no tokens.** Elevation & Depth states `rgba(0,0,0,0.08)` and `rgba(0,0,0,0.12)` in prose, so no `{shadow.*}` reference can be made. Adding a `shadow:` group would be the fix, but the values would still be the extracted ones.
- **Elevation is expressed two ways** — box-shadow at levels 1–2 and a 1px hairline border on cards — with no rule for which applies where. The extracted evidence does not settle it.
- **Nothing rendered.** Overlap, horizontal overflow, clipping, real tap-target size, frame rate and layout shift are all unverified; this audit read a document, not a page.
- **Brand name.** The file documents "Superhumon", which appears to be an inspired interpretation rather than a 1:1 record of a shipping site. Treated as the brand of record throughout.
