---
version: alpha
name: Ferrari-design-analysis
description: A luxury-automotive brand whose marketing surfaces read as cinematic editorial. The base canvas is **near-black** (`#181818`) holding pure white display type; white-canvas bands appear only inside specific editorial contexts (preowned listings, pricing tables). The single brand voltage is **Rosso Corsa** (`#da291c`) — the iconic Ferrari racing red — used scarcely on primary CTAs, the Cavallino mark, and Formula 1 race-position highlights. Type runs **FerrariSans** at modest weights (display 500, body 400) — never bombastic. Spacing follows an explicit 8px token ladder (`xxxs` 4px through `super` 128px); generous editorial pacing throughout. The brand's strongest visual signature is the **full-bleed cinematic hero photograph** that fills the viewport top with car photography, model details, or trackside livery — followed by a tighter editorial body layout below.

colors:
  primary: "#da291c"
  primary-active: "#b01e0a"
  primary-hover: "#9d2211"
  ink: "#ffffff"
  body: "#969696"
  body-strong: "#ffffff"
  body-on-light: "#181818"
  muted: "#666666"
  muted-soft: "#8f8f8f"
  muted-strong: "#a8a8a8"
  hairline: "#303030"
  hairline-strong: "#949494"
  hairline-on-light: "#d2d2d2"
  hairline-strong-on-light: "#767676"
  hairline-soft: "#ebebeb"
  canvas: "#181818"
  canvas-elevated: "#303030"
  canvas-light: "#ffffff"
  surface-card: "#303030"
  surface-soft-light: "#f7f7f7"
  surface-strong-light: "#ebebeb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-light: "#181818"
  focus: "#fff200"
  focus-on-light: "#181818"
  accent-yellow-hypersail: "#fff200"
  accent-yellow: "#f6e500"
  semantic-info: "#4c98b9"
  semantic-success: "#03904a"
  semantic-warning: "#f13a2c"

typography:
  display-mega:
    fontFamily: "'FerrariSans', -apple-system, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -1.6px
  display-xl:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1.12px
  display-lg:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.36px
  display-md:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.195px
  title-md:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-sm:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08px
  body-md:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.1px
    textTransform: uppercase
  button:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 1.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.65px
    textTransform: uppercase
  number-display:
    fontFamily: "'FerrariSans', sans-serif"
    fontSize: 80px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1.6px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
  full: 9999px

spacing:
  xxxs: 4px
  xxs: 8px
  xs: 16px
  sm: 24px
  md: 32px
  lg: 48px
  xl: 64px
  xxl: 96px
  super: 128px

shadow:
  small: "0 4px 8px rgba(0,0,0,0.1)"

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

components:
  top-nav-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.body-on-light}"
    typography: "{typography.nav-link}"
    height: 64px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-outline-on-dark:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-outline-on-light:
    backgroundColor: transparent
    textColor: "{colors.body-on-light}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
  hero-band-cinema:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-mega}"
    padding: 0
  hero-band-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.body-on-light}"
    typography: "{typography.display-xl}"
    padding: 96px
  feature-card-photo:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: 0
  feature-card-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.body-on-light}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: 32px
  livery-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 96px
  preowned-listing-card:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.body-on-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 24px
  spec-cell:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.number-display}"
    padding: 24px 0
  race-position-cell:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.number-display}"
  race-calendar-row:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 16px 0
  driver-card:
    backgroundColor: "{colors.canvas-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: 24px
  text-input-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
    height: 48px
  text-input-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.body-on-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
    height: 48px
  badge-pill:
    backgroundColor: "{colors.canvas-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  cta-band-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 96px
  newsletter-input-band:
    backgroundColor: "{colors.canvas-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 32px
  footer-dark:
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

Ferrari's marketing site reads as cinematic editorial — closer to a luxury-magazine spread than a typical car-OEM site. The base canvas is **near-black** (`{colors.canvas}` — #181818) holding pure white display type; white-canvas bands appear only inside specific editorial contexts (preowned listings, pricing tables, dealer surfaces). The single brand voltage is **Rosso Corsa** (`{colors.primary}` — #da291c), the iconic Ferrari racing red, used scarcely on primary CTAs, the Cavallino mark, and Formula 1 race-position highlights.

Type runs **FerrariSans** as the single sans family at modest weights — display 500, body 400. CTA labels render in uppercase with generous tracking (1.1-1.4px). The brand never uses bold display copy.

The brand's strongest visual signature is the **full-bleed cinematic hero photograph** — top-of-page imagery shows car photography, model details, or trackside livery without any chrome competing with it. Headlines float over the bottom of the photo or sit in a tight band beneath. Spacing follows the explicit 8px token ladder: `xxxs` 4 / `xxs` 8 / `xs` 16 / `sm` 24 / `md` 32 / `lg` 48 / `xl` 64 / `xxl` 96 / `super` 128.

**Key Characteristics:**
- Single accent: `{colors.primary}` (Rosso Corsa #da291c) for primary CTAs, the Cavallino, F1 race-position highlights. Used scarcely.
- Near-black canvas (#181818) — never pure black. White-canvas bands only inside editorial contexts.
- Single sans family: FerrariSans across every text role.
- Display weight stays at 500 — never bold.
- CTA labels render uppercase with 1.4px tracking.
- Sharp `{rounded.none}` (0px) corners on every CTA, card, and band — luxury-automotive precision.
- Full-bleed cinematic hero photography is the page chrome.
- Explicit 8px spacing token ladder with named scale (xxxs through super).
- Hairlines + photographic depth — no drop shadow tiers.

## Colors

### Brand & Accent
- **Rosso Corsa** (`{colors.primary}` — #da291c): The iconic Ferrari racing red. Primary CTA fill, Cavallino mark, F1 driver-position highlights. Used scarcely.
- **Rosso Corsa Active** (`{colors.primary-active}` — #b01e0a): Press state.
- **Rosso Corsa Hover-darker** (`{colors.primary-hover}` — #9d2211): Documented for completeness; per the no-hover policy this is not used in preview HTML.
- **Hypersail Yellow** (`{colors.accent-yellow-hypersail}` — #fff200) + **Yellow** (`{colors.accent-yellow}` — #f6e500): Sub-brand accents reserved for the Hypersail sailing program and the global focus-ring color. Not part of the main automotive palette.

### Focus Ring
The site's own global focus-ring color is the Hypersail yellow #fff200 — an extracted fact, not an invented one. It cannot serve the white editorial bands (1.17:1 on `{colors.canvas-light}`), so this file defines two rings. Both are 2px solid with a 2px offset in the surface color beneath.

- **Focus** (`{colors.focus}` — #fff200): The dark-surface ring. **15.18:1 against `{colors.canvas}`** (#181818), 11.28:1 on `{colors.surface-card}`, 4.16:1 on the `{colors.primary}` livery band. Used on every dark band, card and control.
- **Focus On Light** (`{colors.focus-on-light}` — #181818): The light-band ring, drawn in brand ink rather than an invented chromatic value. 17.76:1 on `{colors.canvas-light}`, 16.57:1 on `{colors.surface-soft-light}`, 14.89:1 on `{colors.surface-strong-light}`, 3.65:1 on `{colors.primary}` — so one ink ring clears 3:1 against every light surface this file defines, including a Rosso Corsa CTA sitting on one.
- **Over full-bleed hero photography**, which has no measurable color, the ring is two-tone: 2px `{colors.focus}` with a 1px outer edge in `{colors.focus-on-light}`.
- Ring geometry is **prescribed**, not extracted; only the yellow hex is extracted.

### Accessible Parallel Tones
The extracted utility greys below are frozen and several fail AA at the job they do. Each gets a prescribed parallel token; the original stays scoped to decoration. See `## Accessibility` for the measured ratios.

- **Muted Strong** (`{colors.muted-strong}` — #a8a8a8, prescribed): Secondary text on dark that must meet AA. 7.47:1 on `{colors.canvas}`, 5.55:1 on `{colors.surface-card}`. Use wherever `{colors.muted}` or `{colors.muted-soft}` would carry real copy.
- **Hairline Strong** (`{colors.hairline-strong}` — #949494, prescribed): Control boundary on dark — the only visible edge of an input or select. 5.85:1 on `{colors.canvas}`, 4.35:1 on `{colors.surface-card}`.
- **Hairline Strong On Light** (`{colors.hairline-strong-on-light}` — #767676, prescribed): The same job on light bands. 4.54:1 on `{colors.canvas-light}`, 3.81:1 on `{colors.surface-strong-light}`.

### Surface
- **Canvas** (`{colors.canvas}` — #181818): Near-black page floor — never pure black, slight warmth.
- **Canvas Elevated** (`{colors.canvas-elevated}` — #303030): Cards and panels on dark canvas.
- **Canvas Light** (`{colors.canvas-light}` — #ffffff): White editorial bands (preowned listings, pricing).
- **Surface Card** (`{colors.surface-card}` — #303030): Same as canvas-elevated — driver cards, livery photo plates.
- **Surface Soft Light** (`{colors.surface-soft-light}` — #f7f7f7): Light editorial alternating band.
- **Surface Strong Light** (`{colors.surface-strong-light}` — #ebebeb): Light-canvas dividers, badges.

### Hairlines
- **Hairline** (`{colors.hairline}` — #303030): 1px divider on dark — same hex as `{colors.canvas-elevated}`. **Decoration only.** At 1.35:1 on `{colors.canvas}` it is a tonal seam, not a boundary; where it is the only edge of a control, use `{colors.hairline-strong}`.
- **Hairline On Light** (`{colors.hairline-on-light}` — #d2d2d2): 1px divider on light bands. **Decoration only** — 1.51:1 on `{colors.canvas-light}`. Control boundaries use `{colors.hairline-strong-on-light}`.
- **Hairline Soft** (`{colors.hairline-soft}` — #ebebeb): Lighter divider on light bands. **Decoration only** — 1.19:1 on `{colors.canvas-light}`.

### Text
- **Ink** (`{colors.ink}` — #ffffff): Display, body emphasis on dark.
- **Body** (`{colors.body}` — #969696): Default running-text on dark.
- **Body Strong** (`{colors.body-strong}` — #ffffff): Same as ink.
- **Body On Light** (`{colors.body-on-light}` — #181818): Default text on light bands.
- **Muted** (`{colors.muted}` — #666666): Sub-titles, captions on dark. **Fails AA as text** — 3.09:1 on `{colors.canvas}`, 2.30:1 on `{colors.surface-card}`. Scope it to non-essential ornament, or substitute `{colors.muted-strong}`.
- **Muted Soft** (`{colors.muted-soft}` — #8f8f8f): Disabled link text. 5.49:1 on `{colors.canvas}` but **4.08:1 on `{colors.surface-card}`** — short of AA for body copy on a card.
- **On Primary** (`{colors.on-primary}` — #ffffff): White text on Rosso Corsa.

### Semantic
- **Info** (`{colors.semantic-info}` — #4c98b9): Info badges, callout backgrounds.
- **Success** (`{colors.semantic-success}` — #03904a): Confirmation.
- **Warning** (`{colors.semantic-warning}` — #f13a2c): Validation warnings.

## Typography

### Font Family
**FerrariSans** is the licensed single sans family across every text role. Fallback: `-apple-system, system-ui, sans-serif`. No display/body family split.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-mega}` | 80px | 500 | 1.05 | -1.6px | Homepage hero h1 |
| `{typography.display-xl}` | 56px | 500 | 1.1 | -1.12px | Subsidiary heroes |
| `{typography.display-lg}` | 36px | 500 | 1.2 | -0.36px | Section heads, livery band |
| `{typography.display-md}` | 26px | 500 | 1.5 | 0.195px | Sub-section heads |
| `{typography.title-md}` | 18px | 700 | 1.2 | 0 | Component titles |
| `{typography.title-sm}` | 16px | 500 | 1.4 | 0.08px | List labels |
| `{typography.body-md}` | 14px | 400 | 1.5 | 0 | Default body |
| `{typography.body-sm}` | 13px | 400 | 1.5 | 0 | Footer body |
| `{typography.caption}` | 12px | 400 | 1.4 | 0 | Photo captions |
| `{typography.caption-uppercase}` | 11px | 600 | 1.4 | 1.1px | Section labels, badges |
| `{typography.button}` | 14px | 700 | 1.0 | 1.4px (uppercase) | CTA pill labels |
| `{typography.nav-link}` | 13px | 600 | 1.4 | 0.65px (uppercase) | Top-nav menu items |
| `{typography.number-display}` | 80px | 700 | 1.0 | -1.6px | Race position highlights, spec values |

### Principles
- **Display weight stays at 500.** Editorial confidence, not bombastic. The cinematic photography is doing the visual heavy-lifting — type doesn't need to compete.
- **CTA labels are uppercase with 1.4px tracking.** Luxury-precision feel.
- **Nav labels are uppercase with 0.65px tracking.** Consistent with CTA voice.
- **Negative letter-spacing on display only.** -0.36px to -1.6px on display sizes; body stays at 0.

### Note on Font Substitutes
FerrariSans is licensed. Open-source substitute: **Inter** at weight 500 with letter-spacing -1%, or **Söhne** for closer humanist proportions.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxxs}` 4px · `{spacing.xxs}` 8px · `{spacing.xs}` 16px · `{spacing.sm}` 24px · `{spacing.md}` 32px · `{spacing.lg}` 48px · `{spacing.xl}` 64px · `{spacing.xxl}` 96px · `{spacing.super}` 128px.
- **Section padding:** `{spacing.xxl}` (96px) for major bands; `{spacing.super}` (128px) reserved for hero band depth.

### Grid & Container
- Max content width: ~1280px on editorial bands. Hero photography goes full-bleed.
- Editorial body: 12-column grid.
- Feature card grids: 2-up at desktop for hero splits, 3-up for benefit grids, 4-up for preowned listing tiles.
- Footer: 5-column at desktop.

### Whitespace Philosophy
Generous editorial pacing. Cinematic hero photography occupies generous viewport real-estate; body sections sit in tighter editorial layouts beneath. The canvas-light editorial bands (preowned, pricing) carry tighter density than the dark cinema bands.

## Elevation & Depth

The system uses **photographic depth + brightness-step** elevation. No drop shadows except the single soft-small tier, now carried as a token: `{shadow.small}` = `0 4px 8px rgba(0,0,0,0.1)`.

Elevation is expressed **one way — a brightness step** (canvas → `{colors.canvas-elevated}` → `{colors.canvas-light}`), with hairlines used only where two same-value surfaces meet. The measured steps: `{colors.canvas}` to `{colors.canvas-elevated}` is 1.35:1 and `{colors.canvas-elevated}` to `{colors.canvas-light}` is 13.20:1. The first step is deliberately subtle — a card reads as elevated by its photograph and its 1px edge, not by the tonal jump, which is why `{shadow.small}` exists at all.

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `{colors.canvas}` (#181818) | Body bands, footer |
| Card | `{colors.canvas-elevated}` (#303030) | Driver cards, livery plates |
| Light band | `{colors.canvas-light}` (#ffffff) | Preowned listings, pricing |
| Hairline border | 1px `{colors.hairline}` or `{colors.hairline-on-light}` | Decorative card outlines, dividers |
| Control boundary | 1px `{colors.hairline-strong}` / `{colors.hairline-strong-on-light}` | Inputs, selects — any edge that must be seen |
| Soft drop | `{shadow.small}` | Hovered cards (single shadow tier) |
| Photographic | Full-bleed cinema imagery | Hero band, livery photographs |

### Decorative Depth
- **Full-bleed cinema photography** is the brand's primary depth treatment.
- **Brand red gradient** (`linear-gradient(180deg, #a00c01, #da291c 64%)`): The Rosso Corsa gradient used inside accent bands and CTA hover states.
- **Dark grey gradient** (`linear-gradient(180deg, #3c3c3c, #030303 64%)`): Atmospheric darken used at section transitions.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Every CTA, card, band — dominant radius |
| `{rounded.xs}` | 2px | Tight badges (rare) |
| `{rounded.sm}` | 4px | Form inputs |
| `{rounded.md}` | 6px | Compact cards (rare) |
| `{rounded.lg}` | 8px | Mobile-only collapse cards |
| `{rounded.xl}` | 12px | Modal/dialog corners (rare) |
| `{rounded.full}` | 9999px | Avatar plates, badge pills |

The radius vocabulary is **sharp by default**. Sharp 0px corners are the brand button shape — never rounded pills. Pill geometry is reserved for badge labels only.

## Components

### Top Navigation

**`top-nav-on-dark`** — Default top nav on dark hero pages. Background `{colors.canvas}`, text `{colors.ink}`, height 64px. Layout: Cavallino mark left, primary horizontal menu (Models / F1 / Lifestyle / Owners / Preowned), language picker + utilities right. Menu items render uppercase with 0.65px tracking.

**`top-nav-on-light`** — White-canvas variant for editorial light bands.

### Buttons

**`button-primary`** — The signature Rosso Corsa CTA. Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}` (14px / 700 / 1.4px tracking, uppercase), padding 14px × 32px, height 48px, **rounded `{rounded.none}` (0px — sharp corners)**.

**`button-primary-active`** — Press state. Background `{colors.primary-active}`.

**`button-outline-on-dark`** — Transparent with 1px white border. Background transparent, text `{colors.ink}`, 1px white border, same sharp 0px corners.

**`button-outline-on-light`** — Transparent with 1px ink border on light bands.

**`button-tertiary-text`** — Inline text link, uppercase tracking.

### Hero Bands

**`hero-band-cinema`** — Full-bleed cinematic photograph. Background `{colors.canvas}` underneath, but the photo fills the viewport. Display headline floats over the bottom of the photo or sits in a tight band beneath, in `{typography.display-mega}` (80px / 500 / -1.6px). One primary CTA + one outline CTA. Zero padding — the photo fills edge-to-edge.

**`hero-band-light`** — White-canvas variant for editorial bands. Background `{colors.canvas-light}`, text `{colors.body-on-light}`, padding 96px.

### Cards

**`feature-card-photo`** — Image-first card. Background `{colors.canvas}`, text `{colors.ink}`, rounded `{rounded.none}`. Image fills the top edge-to-edge; title + body sit beneath in tight typography.

**`feature-card-light`** — White-canvas variant. Background `{colors.canvas-light}`, text `{colors.body-on-light}`, rounded `{rounded.none}`, padding 32px.

**`driver-card`** — F1 driver portrait card. Background `{colors.canvas-elevated}`, text `{colors.ink}`, rounded `{rounded.none}`, padding 24px. Layout: driver portrait + name + race number + team badge.

### Editorial Surfaces

**`livery-band`** — A full-width Rosso Corsa accent band. Background `{colors.primary}`, text `{colors.ink}`, type `{typography.display-lg}`, 96px padding. Used as a standout livery callout between dark editorial bands.

**`preowned-listing-card`** — Used in the preowned Ferrari listing grid. Background `{colors.canvas-light}`, text `{colors.body-on-light}`, rounded `{rounded.none}`, padding 24px. Layout: car photo top + model name + year/mileage + price.

### Spec & Race Surfaces

**`spec-cell`** — Technical spec callout. Transparent background, value in `{typography.number-display}` (80px / 700 / -1.6px white), label below in `{typography.caption-uppercase}`.

**`race-position-cell`** — F1 driver finishing position. Same number-display geometry but text in `{colors.primary}` Rosso Corsa for the brand's racing identity.

**`race-calendar-row`** — Hairline-divided row in the F1 race calendar. Layout: date column left, race name + circuit middle, results column right.

### Forms & Tags

**`text-input-on-dark`** — Background `{colors.canvas}`, text `{colors.ink}`, rounded `{rounded.sm}` (4px), padding 14px × 16px, height 48px. Border is 1px `{colors.hairline}` as extracted; because that edge is the control's only boundary and measures 1.35:1, build it with 1px `{colors.hairline-strong}` instead.

**`text-input-on-light`** — White-canvas variant. Same substitution: `{colors.hairline-strong-on-light}` in place of `{colors.hairline-on-light}` for the control edge.

**`badge-pill`** — Small uppercase pill. Background `{colors.canvas-elevated}`, text `{colors.ink}`, type `{typography.caption-uppercase}` (11px / 600 / 1.1px tracking, uppercase), rounded `{rounded.full}` (9999px), padding 4px × 12px. The only place pill geometry is used.

### Newsletter / CTA / Footer

**`newsletter-input-band`** — Newsletter signup band. Background `{colors.canvas-elevated}`, padding 32px, rounded `{rounded.sm}`. Holds an inline email input + primary CTA.

**`cta-band-dark`** — Pre-footer band. Background `{colors.canvas}`, centered display headline in `{typography.display-lg}`, single Rosso Corsa CTA. 96px padding.

**`footer-dark`** — Closing dark footer. Background `{colors.canvas}`, text `{colors.body}`. 5-column link list. 64×48px padding.

**`footer-link`** — Background transparent, text `{colors.body}`, type `{typography.body-sm}`.

### Interaction States

Only `default` and `active/pressed` are extracted — `{colors.primary-active}` (#b01e0a) is the captured press fill, and `{colors.primary-hover}` (#9d2211) is a captured hex whose behaviour was never observed, because the captured surfaces carry no hover documentation. Every other state in this table is **prescribed** to fit the brand, not measured. Focus-visible is always the ring from `## Colors` → Focus Ring: `{colors.focus}` on dark, `{colors.focus-on-light}` on light bands.

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.primary}` fill | `{colors.primary-hover}` fill | 2px `{colors.focus}` ring, 2px offset | `{colors.primary-active}` fill | 40% opacity, no pointer | label swapped for an inline 3-dot pulse, width held | n/a | n/a |
| `button-outline-on-dark` | 1px `{colors.ink}` edge | edge to `{colors.ink}`, fill to `rgba(255,255,255,0.06)` | 2px `{colors.focus}` ring | fill to `rgba(255,255,255,0.12)` | edge to `{colors.muted}`, text `{colors.muted}` | 3-dot pulse | n/a | n/a |
| `button-outline-on-light` | 1px `{colors.body-on-light}` edge | fill to `{colors.surface-strong-light}` | 2px `{colors.focus-on-light}` ring | fill to `{colors.hairline-on-light}` | edge + text to `{colors.hairline-strong-on-light}` | 3-dot pulse | n/a | n/a |
| `button-tertiary-text` | `{colors.ink}` label | 1px underline in `{colors.primary}` | 2px `{colors.focus}` ring | underline + `{colors.muted-strong}` label | `{colors.muted-soft}` label | n/a | n/a | n/a |
| `top-nav-on-dark` item | `{colors.ink}` label | 2px `{colors.primary}` underline | 2px `{colors.focus}` ring | underline held | `{colors.muted-strong}` label | n/a | current section keeps the `{colors.primary}` underline | n/a |
| `text-input-on-dark` | 1px `{colors.hairline-strong}` edge | edge to `{colors.muted-strong}` | 2px `{colors.focus}` ring, edge to `{colors.ink}` | same as focus-visible | edge + text `{colors.muted}`, fill unchanged | 2px `{colors.hairline-strong}` bottom edge pulsing in opacity | n/a | 1px `{colors.semantic-warning}` edge + message in `{colors.semantic-warning}` |
| `text-input-on-light` | 1px `{colors.hairline-strong-on-light}` edge | edge to `{colors.body-on-light}` | 2px `{colors.focus-on-light}` ring | same as focus-visible | edge + text `{colors.hairline-strong-on-light}` | opacity pulse on the bottom edge | n/a | `{colors.semantic-warning}` edge + message |
| `feature-card-photo` / `feature-card-light` | flat | photo scales to 1.03, `{shadow.small}` added | 2px ring on the card bounds | photo returns to 1.0 | n/a | grey `{colors.canvas-elevated}` block in place of the photo | n/a | n/a |
| `preowned-listing-card` | flat | `{shadow.small}` | 2px `{colors.focus-on-light}` ring | `{shadow.small}` removed | n/a | skeleton block | 2px `{colors.primary}` left edge when shortlisted | n/a |
| `driver-card` | `{colors.canvas-elevated}` fill | portrait scales to 1.03 | 2px `{colors.focus}` ring | portrait to 1.0 | n/a | skeleton block | 2px `{colors.primary}` top edge for the active driver | n/a |
| `badge-pill` | `{colors.canvas-elevated}` fill | **two states only — default and selected.** Not interactive outside filter chips. | 2px `{colors.focus}` ring (filter-chip use only) | n/a | `{colors.muted}` label | n/a | `{colors.primary}` fill, `{colors.on-primary}` label | n/a |
| `race-calendar-row` | hairline-divided row | row fill to `{colors.canvas-elevated}` | 2px `{colors.focus}` ring inset | fill held | n/a | skeleton row | 2px `{colors.primary}` left edge on the next race | n/a |
| `newsletter-input-band` | `{colors.canvas-elevated}` fill | n/a — container, not a control | ring belongs to the input inside it | n/a | n/a | submit button carries the loading state | n/a | field-level `{colors.semantic-warning}` message |
| `hero-band-cinema` / `livery-band` / `cta-band-dark` / `footer-dark` | **one state only — default.** Layout bands, not controls. Their CTAs and links carry the states above. | | | | | | | |

`spec-cell` and `race-position-cell` are **display-only — one state, default.** They render numbers and take no input.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or easing curve below was extracted from Ferrari's own CSS; they are the **Cinematic** profile values, assigned because the identity is luxury-automotive with full-bleed photography, sparse type and a slow reveal. Treat every value here as a specification to build to, not as a captured fact.

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

The long decelerate of `{motion.ease-standard}` is the point: a Ferrari surface should look like it is **settling**, the way the hero photograph settles under a headline that arrives late. Nothing snaps.

### Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (CTA, nav item, card) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`; `transform: scale(1.03)` on card photography only | No scale. Opacity only, at `{motion.duration-reduced}`. |
| Press (any button) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.99)` + `opacity` | No scale. Fill change only, no transition. |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring | Ring appears instantly at full opacity. |
| Page / route transition | `{motion.duration-slow}` out, `{motion.duration-emphasis}` for the incoming hero | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(16px)` on the body column; hero photograph `transform: scale(1.04 → 1.0)` | No travel, no scale. Cross-fade at `{motion.duration-reduced}`. |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(24px)` (modal) or `translateX(100%→0)` (drawer) | No travel. Opacity only, `{motion.duration-reduced}`. |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | same properties, reversed | Opacity only, `{motion.duration-reduced}`. |
| Dropdown / nav mega-panel open | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(-8px→0)` | Opacity only, `{motion.duration-reduced}`. |
| Dropdown close | `{motion.duration-fast}` | `{motion.ease-exit}` | same, reversed | Opacity only, `{motion.duration-reduced}`. |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(16px→0)` | Opacity only, `{motion.duration-reduced}`. |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | same, reversed | Opacity only, `{motion.duration-reduced}`. |
| List enter (feature grid, preowned tiles, race-calendar rows, driver cards) | `{motion.duration-base}` per item, `{motion.stagger-step}` 80ms between items, capped at 8 items | `{motion.ease-enter}` | `opacity` + `transform: translateY(24px→0)` | No travel, no stagger — the whole list fades in once at `{motion.duration-reduced}`. |
| List exit (filter change) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)` | Opacity only, `{motion.duration-reduced}`. |
| Loading (skeletons, 3-dot button pulse) | 1400ms loop | `{motion.ease-standard}` | `opacity` 0.4 ↔ 1.0 | Loop removed. Static skeleton at 0.6 opacity, plus a text status. |
| Brand ambience — hero photograph slow push-in | 12000ms, one pass, no loop | `{motion.ease-standard}` | `transform: scale(1.0 → 1.04)` | Removed. Photograph holds at scale 1.0. |

### Rules

- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin`.
- Every exit is shorter than its entrance: `{motion.duration-fast}` out against `{motion.duration-base}` in.
- Nothing animates on first paint in a way that delays content. The hero photograph and its headline render at final position; the push-in starts after paint and the headline settle is `opacity` only.
- The only infinite animation is the loader. The hero push-in is **deliberate brand ambience, stated as such**, and runs one pass rather than looping.
- The 80ms stagger is the Cinematic signature — a deliberately visible cascade. It is capped at 8 items so a 24-tile preowned grid never takes 2 seconds to arrive.

### `@media (prefers-reduced-motion: reduce)`

**Removed:** all `transform` travel and all scale — card hover scale, press scale, page-transition translate and hero scale, modal/drawer/dropdown/toast translate, list-enter translate, list-exit scale. The 80ms stagger is removed with it; lists fade in as one block. The loader loop and the hero push-in ambience are frozen.

**Kept:** `opacity` fades, every one of them clamped to `{motion.duration-reduced}` (150ms) regardless of the token the full-motion path uses. This is why the token exists — this file's own `{motion.duration-fast}` is 240ms and would exceed the 150ms ceiling. Focus rings, fill changes and state colour changes are unaffected: they were never travel.

## Accessibility

Contrast below is **measured** from this file's own hex values with WCAG 2.1 relative luminance. Everything about tap targets at render time, overlap or layout shift is outside what this document can verify.

### Measured contrast — key pairs

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` #ffffff on `{colors.canvas}` #181818 | 17.76:1 | 4.5:1 | Pass |
| `{colors.ink}` #ffffff on `{colors.surface-card}` #303030 | 13.20:1 | 4.5:1 | Pass |
| `{colors.body}` #969696 on `{colors.canvas}` #181818 | 6.00:1 | 4.5:1 | Pass |
| `{colors.body}` #969696 on `{colors.surface-card}` #303030 | 4.46:1 | 4.5:1 | **Fail by 0.04** — see below |
| `{colors.body-on-light}` #181818 on `{colors.canvas-light}` #ffffff | 17.76:1 | 4.5:1 | Pass |
| `{colors.on-primary}` #ffffff on `{colors.primary}` #da291c | 4.87:1 | 4.5:1 | Pass |
| `{colors.muted}` #666666 on `{colors.canvas}` #181818 | 3.09:1 | 4.5:1 | **Fail** |
| `{colors.muted}` #666666 on `{colors.surface-card}` #303030 | 2.30:1 | 4.5:1 | **Fail** |
| `{colors.muted-soft}` #8f8f8f on `{colors.canvas}` #181818 | 5.49:1 | 4.5:1 | Pass |
| `{colors.muted-soft}` #8f8f8f on `{colors.surface-card}` #303030 | 4.08:1 | 4.5:1 | **Fail** |
| `{colors.hairline}` #303030 on `{colors.canvas}` #181818 | 1.35:1 | 3.0:1 | **Fail** |
| `{colors.hairline-on-light}` #d2d2d2 on `{colors.canvas-light}` #ffffff | 1.51:1 | 3.0:1 | **Fail** |
| `{colors.hairline-soft}` #ebebeb on `{colors.canvas-light}` #ffffff | 1.19:1 | 3.0:1 | **Fail** |
| `{colors.muted-strong}` #a8a8a8 on `{colors.canvas}` #181818 | 7.47:1 | 4.5:1 | Pass (prescribed) |
| `{colors.muted-strong}` #a8a8a8 on `{colors.surface-card}` #303030 | 5.55:1 | 4.5:1 | Pass (prescribed) |
| `{colors.hairline-strong}` #949494 on `{colors.canvas}` #181818 | 5.85:1 | 3.0:1 | Pass (prescribed) |
| `{colors.hairline-strong}` #949494 on `{colors.surface-card}` #303030 | 4.35:1 | 3.0:1 | Pass (prescribed) |
| `{colors.hairline-strong-on-light}` #767676 on `{colors.canvas-light}` #ffffff | 4.54:1 | 3.0:1 | Pass (prescribed) |
| `{colors.semantic-warning}` #f13a2c on `{colors.canvas}` #181818 | 4.55:1 | 4.5:1 | Pass |
| `{colors.semantic-success}` #03904a on `{colors.canvas}` #181818 | 4.31:1 | 4.5:1 | **Fail** — 18px+ / 700 labels and icons only (3:1 applies there) |
| `{colors.semantic-info}` #4c98b9 on `{colors.canvas}` #181818 | 5.50:1 | 4.5:1 | Pass |
| `{colors.primary}` #da291c on `{colors.canvas}` #181818 | 3.65:1 | 4.5:1 | **Fail as body text** — passes 3:1 for the 80px/700 `race-position-cell` |

**The real brand fails AA at these points, and this document says so rather than hiding it.** `{colors.muted}` is the clearest case: at 3.09:1 on the near-black canvas and 2.30:1 on a card it is not a usable text colour at any size the file defines, yet the captured surfaces use it for sub-titles and captions. `{colors.hairline}` at 1.35:1 is a tonal seam rather than a boundary — correct as decoration, wrong as the only edge of a text input, which is exactly where the captured markup puts it. `{colors.body}` on a card misses AA by 0.04:1, close enough that it will pass on some rendering stacks and fail on others; treat it as failing. All four extracted hexes are frozen; the prescribed `-strong` tokens above exist to take over the jobs that need contrast.

### Focus ring visibility, per surface this file defines

| Surface | Ring | Ratio | Required |
|---|---|---|---|
| `{colors.canvas}` #181818 | `{colors.focus}` #fff200 | 15.18:1 | 3.0:1 |
| `{colors.canvas-elevated}` / `{colors.surface-card}` #303030 | `{colors.focus}` #fff200 | 11.28:1 | 3.0:1 |
| `{colors.primary}` #da291c (livery band, CTA on dark) | `{colors.focus}` #fff200 | 4.16:1 | 3.0:1 |
| `{colors.canvas-light}` #ffffff | `{colors.focus-on-light}` #181818 | 17.76:1 | 3.0:1 |
| `{colors.surface-soft-light}` #f7f7f7 | `{colors.focus-on-light}` #181818 | 16.57:1 | 3.0:1 |
| `{colors.surface-strong-light}` #ebebeb | `{colors.focus-on-light}` #181818 | 14.89:1 | 3.0:1 |
| `{colors.primary}` #da291c (CTA on a light band) | `{colors.focus-on-light}` #181818 | 3.65:1 | 3.0:1 |
| Full-bleed hero photography (no measurable colour) | two-tone: `{colors.focus}` with a 1px outer edge in `{colors.focus-on-light}` | not measurable | — |

`{colors.focus}` #fff200 is **1.17:1 on `{colors.canvas-light}`** — it must never be drawn on a white band. That is the whole reason this file carries two rings.

### Minimum tap target

Specified, not verified — this document has no rendered page. `button-primary`, both outline buttons and both text inputs are specified at 48px height, clearing the 44×44 minimum. Nav items are specified with padding for an effective 48px area; `badge-pill` at 4px × 12px padding on 11px type is **below 44px** and must be given a 44px minimum hit area wherever it is used as a filter chip. `race-calendar-row` at 16px vertical padding on 14px/1.5 body reaches roughly 53px.

### Reduced motion

See `## Motion & Animation` → `@media (prefers-reduced-motion: reduce)`. All travel and scale removed, opacity fades clamped to `{motion.duration-reduced}` 150ms, loader loop and hero push-in frozen.

### Other

- Rosso Corsa is the only signal colour; nothing in this file conveys meaning by colour alone except the `{colors.primary}` underline on the current nav item and the `{colors.primary}` left edge on a selected row. Both need a non-colour cue — `aria-current` and a text label respectively.
- `{colors.canvas-light}` bands invert the whole palette. A build must switch ink, hairline and focus tokens together, not individually.

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
| `{colors.hairline}` (`#303030`) on `{colors.canvas-elevated}` (`#303030`) | 1.00:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.semantic-success}` (`#03904a`) on `{colors.canvas-elevated}` (`#303030`) | 3.20:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.semantic-warning}` (`#f13a2c`) on `{colors.canvas-elevated}` (`#303030`) | 3.38:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.semantic-info}` (`#4c98b9`) on `{colors.canvas-elevated}` (`#303030`) | 4.08:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (Rosso Corsa) for primary CTAs, the Cavallino mark, and F1 race-position highlights.
- Set every CTA at `{rounded.none}` (0px sharp corners) — the brand's signature precision.
- Render CTA labels in uppercase with 1.4px tracking via `{typography.button}`.
- Pair every hero with a full-bleed cinematic photograph — the photograph IS the depth.
- Use the explicit 8px spacing ladder (`xxxs` through `super`) rather than ad-hoc px values.
- Keep display weight at 500 — never bold.
- Let surfaces **settle** rather than snap: `{motion.duration-base}` 400ms with `{motion.ease-standard}` is the house timing.
- Draw the focus ring in `{colors.focus}` on dark surfaces and `{colors.focus-on-light}` on light bands — switch it with the band, not per component.
- Substitute `{colors.muted-strong}` for `{colors.muted}` wherever the grey carries real copy.

### Don't
- Don't introduce a saturated brand color other than Rosso Corsa.
- Don't use rounded or pill CTAs — sharp 0px corners are the brand button.
- Don't bold display copy. The cinematic photography does the visual heavy-lifting.
- Don't use Hypersail yellow outside the Hypersail sailing program context.
- Don't use pure black canvas. The brand canvas is `{colors.canvas}` (#181818) — slightly warm.
- Don't add drop shadow tiers. Photography + brightness-step elevation carry the depth.
- Don't animate `width`, `height`, `top`, `left` or `margin` — `transform` and `opacity` only.
- Don't draw `{colors.focus}` Hypersail yellow on a white editorial band; at 1.17:1 the ring disappears.
- Don't use `{colors.hairline}` as the only boundary of a control — 1.35:1 is decoration, not an edge.
- Don't let the 80ms stagger run past 8 items; a long cascade stops reading as cinematic and starts reading as slow.
- Don't extract a CTA color from a third-party widget (cookie consent, OneTrust). The brand's CTA color is what appears on actual product CTAs, not on injected modals.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 640px | Hero photograph crops vertically; hero h1 80→32px; feature card grid 1-up; nav hamburger; preowned listing 1-up. |
| Tablet | 640–1024px | Hero h1 56px; feature card grid 2-up; preowned listing 2-up. |
| Desktop | 1024–1280px | Full hero h1 80px; feature card grid 3-up; preowned listing 4-up. |
| Wide | > 1280px | Editorial body content caps at 1280px; hero photography continues full-bleed. |

### Touch Targets
- Primary CTA at 48px height — at WCAG AAA (44 × 44).
- Nav items render uppercase with 0.65px tracking, padded for an effective 48px tap area.

### Collapsing Strategy
- Top nav switches to hamburger below 768px.
- Hero photograph reframes per breakpoint via art direction — desktop carries wide cinematic; mobile crops tighter or shifts to vertical.
- Feature card grid: 4-up → 3-up → 2-up → 1-up.
- F1 driver cards: 2-up at desktop, 1-up at mobile.

## Iteration Guide

1. Focus on a single component at a time.
2. CTAs default to `{rounded.none}` (0px sharp). Cards use `{rounded.none}` too. Pill is reserved for badges.
3. Variants live as separate entries inside `components:`.
4. Use `{token.refs}` everywhere — never inline hex.
5. Hover was never captured from the live site; `{colors.primary-hover}` is an extracted hex with no observed behaviour. Use the prescribed states in `## Components` → Interaction States.
6. FerrariSans 500 for display, 400/700 for body. Uppercase + tracking on CTAs and nav.
7. Rosso Corsa stays scarce — primary CTAs, Cavallino, race-position highlights only.
8. Use the explicit 8px named spacing ladder.

## Known Gaps

- FerrariSans is a licensed typeface; Inter at weight 500 is the documented substitute.
- Animation timings were never measured from the live site. The whole of `## Motion & Animation` is the **Cinematic** profile prescribed to the brand's identity; hero parallax, livery-band entrance and the race-position counter in particular have no captured values.
- Interaction states other than `default` and `active/pressed` are prescribed, not observed. `{colors.primary-hover}` is extracted; its behaviour is not.
- `{colors.focus}` #fff200 is extracted as the site's global focus-ring colour, but the ring's width, offset and the whole `{colors.focus-on-light}` token are prescribed.
- The `-strong` parallel tones (`{colors.muted-strong}`, `{colors.hairline-strong}`, `{colors.hairline-strong-on-light}`) are prescribed accessible substitutes, not brand values.
- Tap-target sizes in `## Accessibility` are specified heights, not rendered measurements; this document cannot verify them.
- In-product surfaces (preowned configurator, F1 telemetry overlays) only partially captured via marketing surfaces.
- Form validation states beyond focus not visible on captured surfaces.
- Hypersail yellow tokens are extracted but only appear in the Hypersail sailing program context — documented as scoped accents.
