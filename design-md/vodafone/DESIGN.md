---
version: alpha
name: Vodafone-Inspired-design-analysis
description: An inspired interpretation of Vodafone's design language — a telecom super-brand whose web surface alternates between editorial photography hero bands with massive uppercase display headlines and clean white content bands, anchored by the company's signature scarlet red CTA and the proprietary Vodafone display sans set at impossibly heavy 800 weight.

colors:
  primary: "#e60000"
  on-primary: "#ffffff"
  ink: "#25282b"
  body: "#7e7e7e"
  mute: "#bebebe"
  canvas: "#ffffff"
  canvas-soft: "#f2f2f2"
  on-dark: "#ffffff"
  focus: "#25282b"
  focus-on-dark: "#ffffff"

motion:
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 500ms
  ease-standard: cubic-bezier(0.4, 0, 0.2, 1)
  ease-enter: cubic-bezier(0.2, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 40ms
  duration-reduced: 150ms

typography:
  display-hero:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 144px
    fontWeight: 800
    lineHeight: 114px
    letterSpacing: -1px
  display-xxl:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 126px
    fontWeight: 800
    lineHeight: 113px
    letterSpacing: -1px
  display-xl:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 90px
    fontWeight: 800
    lineHeight: 84px
  display-lg:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 48px
    fontWeight: 300
    lineHeight: 52px
  display-md:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 40px
    fontWeight: 300
    lineHeight: 44px
  display-sm:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
  display-xs:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 24px
    fontWeight: 700
    lineHeight: 24px
  eyebrow-uppercase:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 16px
    fontWeight: 800
    lineHeight: 24px
  body-lg:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 22px
    fontWeight: 400
    lineHeight: 24px
  body-md:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
  body-md-strong:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 28px
  body-sm:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 16px
    fontWeight: 700
    lineHeight: 22px
  caption:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 16px
  caption-strong:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 14px
    fontWeight: 700
    lineHeight: 21px
  caption-uppercase:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 12px
    fontWeight: 600
    lineHeight: 16px
    letterSpacing: 0.5691px
  button-md:
    fontFamily: Vodafone, Vodafone Rg, Helvetica Neue, Arial, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px

rounded:
  none: 0px
  xs: 1px
  sm: 6px
  card: 6px
  pill-md: 32px
  pill-lg: 60px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px

components:
  divider-on-light:
    description: "The 1 px ink hairline of Elevation Level 1, declared so the boundary role is addressable: form-input outlines and column rules on light surfaces."
    borderColor: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.3xl}"
  nav-link:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill-lg}"
    padding: "{spacing.md} {spacing.2xl}"
  button-outline-red:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill-lg}"
    padding: "{spacing.md} {spacing.2xl}"
  button-outline-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill-lg}"
    padding: "{spacing.md} {spacing.2xl}"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  badge-chip:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.pill-md}"
    padding: "{spacing.xs} {spacing.md}"
  card-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  card-hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  hero-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-hero}"
    padding: "{spacing.3xl} {spacing.3xl}"
  hero-band-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  content-band-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.3xl} {spacing.3xl}"
  speechmark-logo-orb:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  divider-on-dark:
    borderColor: "{colors.on-dark}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.3xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default tier card. Mirrors card-content chrome with canvas-soft surface and a hairline border."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.body}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-pricing-tier-featured:
    description: "Featured tier — polarity-flipped to ink with white text and white pill CTA inside."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-product-selector:
    description: "Tariff-tier picker — repurposed as the brand's plan selector with badge-chip chips inside the frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-cart-drawer:
    description: "Subscription summary — line items per tariff add-on, light hairline dividers."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
    item-divider: "{colors.body}"
  ex-app-shell-row:
    description: "Sidebar nav row. Active state uses brand primary as a left-edge indicator bar."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table cell chrome. Header uses caption-uppercase mono-style eyebrow; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption-uppercase}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.body}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Mirrors card-content chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as card-content; brand uses scrim, not card shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-empty-state-card:
    description: "Empty-state illustration frame on canvas-soft with generous interior padding."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.card}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — card-content shape with caption-strong body."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Vodafone is a global telecom super-brand and its web surface delivers exactly that posture: heroic editorial photography, occasionally cropping a portrait so tight only an eye line and a phone hand are visible, with a single colossal uppercase headline floating on top in the brand's proprietary heavy display weight. The page reads like a campaign poster more than a corporate site, then breaks into a calmer content rhythm of light-canvas story cards and a single red marker (the iconic speechmark logo) drawing the eye to the brand's centre of gravity. There is no second accent colour competing — the entire decorative palette is `{colors.primary}` Vodafone red, near-black `{colors.ink}`, and the surrounding white and grayscale neutrals.

Type is the second decisive voice. Vodafone's custom display sans (extracted as `Vodafone`) carries every headline at impossibly heavy weight 800 in upper case for hero scale (`{typography.display-hero}` 144 px, `{typography.display-xxl}` 126 px) and at lighter weight 300 for the sub-displays that follow. Body text stays in the same family at weight 400 with neutral tracking. The contrast between display weight 800 and display weight 300 IS the brand's typographic story: a shout, then a calm sentence.

Every interactive CTA renders as a generously rounded pill (`{rounded.pill-lg}` 60 px) — Vodafone has never used a square button on its marketing surface in years, and the brand's pill scale ladder runs from 32 px (badge pills) through 60 px (CTA pills) up to 9999 px (icon circular containers). Cards stay gentler at `{rounded.card}` 6 px.

**Key Characteristics:**
- A single primary CTA color `{colors.primary}` (`#e60000`) — Vodafone Red. Pill-filled for primary, pill-outline for secondary. No third button variant.
- Massive uppercase display weight 800 (`{typography.display-hero}` and siblings) is the brand's signature. The 300-weight headline siblings (`{typography.display-lg}` / `{typography.display-md}`) handle calmer secondary moments.
- The `speechmark-logo-orb` — a red square hosting Vodafone's quotation-mark icon — is the only piece of decorative chrome that's not a CTA. It anchors the brand's centre of every page.
- Pill geometry on every interactive shape — `{rounded.pill-lg}` 60 px for buttons, `{rounded.pill-md}` 32 px for inline badges. Card chrome stays at `{rounded.card}` 6 px.
- A two-band page rhythm — `{colors.ink}` dark hero / `{colors.canvas}` light content. No mid-band greys; the brand uses surface contrast, not soft neutrals, for elevation.
- Editorial photography (real portraits, real cities, real cabling) is the only consistent decorative system — no illustration, no atmospheric gradients.

## Colors

### Brand & Accent
- **Vodafone Red** (`{colors.primary}` — `#e60000`): The single brand accent. Every primary CTA pill, every speechmark logo, every conversion target. The most iconic red in telecom — never desaturated, never used at scale for body fills (reserved for high-attention surfaces).

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): The default light content background.
- **Canvas Soft** (`{colors.canvas-soft}` — `#f2f2f2`): A near-white tint used as the badge-chip background.
- **Ink** (`{colors.ink}` — `#25282b`): The brand's near-black surface — used as the dark hero band, the nav background, and the footer fill. Doubles as the primary text color on light surfaces.

### Text
- **Ink** (`{colors.ink}` — `#25282b`): Every heading and body paragraph on light surfaces.
- **Body** (`{colors.body}` — `#7e7e7e`): Secondary body text on light surfaces — captions, metadata, supporting copy.
- **Mute** (`{colors.mute}` — `#bebebe`): The lowest-priority text color — placeholder text, low-key footer links.
- **On Dark** (`{colors.on-dark}` — `#ffffff`): All text on `{colors.ink}` surfaces (hero, footer, nav).

### Focus
- **Focus** (`{colors.focus}` — `#25282b`) and **Focus on Dark** (`{colors.focus-on-dark}` — `#ffffff`): prescribed, not extracted. They reuse `{colors.ink}` and `{colors.on-dark}` rather than adding a colour to a brand whose rule is red + ink + grayscale only; the ring is drawn outside the control with a 2 px offset. Measured ratios and the two-tone treatment over photography are in Accessibility.

### Semantic
The brand does not maintain a separate semantic palette. The primary red doubles as validation / destructive signal when needed; success / warning use are reserved for in-product contexts and are not part of the documented marketing system.

## Typography

### Font Family
A single custom face carries the entire system: **Vodafone**, the brand's proprietary display sans. The face spans weights 300 (light), 400 (regular), 600, 700, and 800 — every role in the system pulls from this one family. There is no mono companion; technical labels (rare on the marketing surface) borrow the same face at smaller sizes.

The icomoon icon-font is loaded for proprietary glyphs but does not render as a typographic role.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-hero}` | 144px | 800 | 114px | -1px | The hero stencil (`"STAY CONNECTED"`) — uppercase, ultra-tight tracking, brand's signature size. |
| `{typography.display-xxl}` | 126px | 800 | 113px | -1px | Slightly smaller hero variant. |
| `{typography.display-xl}` | 90px | 800 | 84px | 0 | Mid-hero scale. |
| `{typography.display-lg}` | 48px | 300 | 52px | 0 | Section-headline sub-display in the lighter weight. |
| `{typography.display-md}` | 40px | 300 | 44px | 0 | Sub-section displays. |
| `{typography.display-sm}` | 32px | 700 | 40px | 0 | Card headings, story-card titles. |
| `{typography.display-xs}` | 24px | 700 | 24px | 0 | Inline display micro-headings. |
| `{typography.eyebrow-uppercase}` | 16px | 800 | 24px | 0 | Uppercase eyebrow tags above section headlines. |
| `{typography.body-lg}` | 22px | 400 | 24px | 0 | Lead body paragraphs. |
| `{typography.body-md}` | 18px | 400 | 28px | 0 | Default paragraph body. |
| `{typography.body-md-strong}` | 18px | 600 | 28px | 0 | Bolded inline body. |
| `{typography.body-sm}` | 16px | 400 | 20px | 0 | Secondary body. |
| `{typography.body-sm-strong}` | 16px | 700 | 22px | 0 | Bolded short body. |
| `{typography.caption}` | 14px | 400 | 16px | 0 | Captions, fine print. |
| `{typography.caption-strong}` | 14px | 700 | 21px | 0 | Bold captions, badge labels. |
| `{typography.caption-uppercase}` | 12px | 600 | 16px | 0.57px | Uppercase metadata, footer eyebrows. |
| `{typography.button-md}` | 18px | 400 | 28px | 0 | Default button label. |

### Principles
- **Weight 800 + uppercase = hero voice.** This is the entire reason the brand reads as a billboard rather than a tech site.
- **Weight 300 = the calmer secondary voice.** Used at 40 – 48 px for sub-displays; never below 24 px to keep legibility.
- **Single family throughout.** The brand never mixes a serif or a mono into the typographic system. Consistency is the calm.
- **Tracking stays tight at display sizes.** `-1px` at 144 px is the brand's calibration; reverting to neutral tracking softens the stencil look.

### Note on Font Substitutes
The Vodafone display sans is proprietary. Open-source substitutes:
- **Display sans** — *Inter* weight 800 at hero scale with `letter-spacing: -1px` is the closest free match. *Geist* weight 700–800 is the second-best.
- **Lighter display weight (300)** — *Inter* weight 300 holds its line-height well at 48 px display sizes.

## Layout

### Spacing System
- **Base unit**: 4 px (mostly multiples of 4; a few 5/7 px appear inside icon-padding compensation).
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 20 px · `{spacing.2xl}` 24 px · `{spacing.3xl}` 32 px.
- **Section padding**: hero bands and content bands use `{spacing.3xl}` 32 px gutters; vertical spacing inside hero is fluid (fill-the-band).
- **Card interior padding**: story cards use `{spacing.lg}` 16 px around image + headline.
- **Inline gap**: button rows and chip rows use `{spacing.md}` 12 px between siblings.

### Grid & Container
- Marketing content uses a wide container (effectively edge-to-edge with `{spacing.3xl}` gutters on desktop, shrinking on mobile).
- Story-card grids: 2-up at desktop, 1-up at mobile.
- Hero photography fills the viewport; the headline overlays at the top-left.

### Whitespace Philosophy
The hero's massive display headline owns the whole top of the page; whitespace below is generous to let the second band breathe. Inside content cards, headline and copy hug close (`{spacing.sm}` 8 px gap), then a wider gap (`{spacing.3xl}`) before the next card. The footer band is dark and dense.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default for most cards and panels — surface contrast does the elevation work. |
| Level 1 — Hairline | 1 px solid `{colors.ink}` border. | Form inputs, the `divider-on-dark` between footer columns. |
| Level 2 — Border on Dark | 1 px solid `{colors.on-dark}` border on `{colors.ink}` surfaces. | Outline buttons sitting on the dark hero band. |

The brand does not use soft drop shadows; depth comes from polarity-flip between `{colors.ink}` and `{colors.canvas}` bands.

### Decorative Depth
- **Editorial photography**: the hero photo (real-person portrait or environment shot) is the brand's only true atmospheric effect.
- **Speechmark logo orb as visual anchor**: the red orb hosting the quote-mark icon acts as a single point of focal-depth in the centre of the otherwise-flat content rhythm.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed hero bands, footer, banner strips. |
| `{rounded.xs}` | 1px | Tightest inline indicator (rarely used). |
| `{rounded.sm}` | 6px | The brand's canonical content radius — applied to images and inputs. |
| `{rounded.card}` | 6px | Card chrome and image frames (alias for `sm`). |
| `{rounded.pill-md}` | 32px | Badge / chip pills. |
| `{rounded.pill-lg}` | 60px | The brand's signature CTA pill — every primary and secondary button. |
| `{rounded.full}` | 9999px | Circular icon containers (e.g., video play/pause). |

### Photography Geometry
- Hero portraits: edge-to-edge 16:9 or 4:3 with no internal frame.
- Story-card thumbnails: 16:9 landscape inside `{rounded.card}` chrome.
- Speechmark logo orb: square with `{rounded.sm}` corners (visually a tilted-square mark; the SVG mark itself fills the orb).

## Components

### Buttons

**`button-primary`** — the red pill CTA, brand's primary conversion target.
- Background `{colors.primary}`, text `{colors.on-primary}`, 1 px solid `{colors.primary}` border, label set in `{typography.button-md}`, padding `{spacing.md} {spacing.2xl}`, shape `{rounded.pill-lg}` 60 px.
- States: default · hover (fill darkens one step, paint-only) · focus-visible (2 px `{colors.focus}` ring, 2 px offset) · pressed (opacity 0.9) · disabled (fill at 35 % opacity, no pointer) · loading (label swaps for the inline spinner, width held) · error (the form's error text sits below; the pill itself does not change) — no selected state, the CTA is not a toggle.

**`button-outline-red`** — the secondary pill, red-text-on-white with red border.
- Background `{colors.canvas}`, text `{colors.primary}`, 1 px solid `{colors.primary}` border, same label / padding / shape as `button-primary`.
- States: default · hover (fill flips to `{colors.primary}`, label to `{colors.on-primary}`) · focus-visible (2 px `{colors.focus}` ring, 2 px offset) · pressed (opacity 0.9) · disabled (border and label at 35 % opacity) · loading (inline spinner in `{colors.primary}`) — no selected, no error state.

**`button-outline-dark`** — the tertiary pill, ink-text-on-white with ink border.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, same label / padding / shape.
- States: default · hover (fill flips to `{colors.ink}`, label to `{colors.on-dark}`) · focus-visible (2 px `{colors.focus}` ring, 2 px offset; `{colors.focus-on-dark}` when the pill sits on `hero-band-dark`) · pressed (opacity 0.9) · disabled (border and label at 35 % opacity) · loading (inline spinner in `{colors.ink}`) — no selected, no error state.

**`button-icon-circular`** — the round white icon button (video play / pause / chevron).
- Background `{colors.canvas}`, ink icon, 1 px solid `{colors.canvas}` outline (effectively borderless), shape `{rounded.full}`.
- States: default · hover (icon glyph darkens to `{colors.ink}` at full opacity) · focus-visible (2 px `{colors.focus}` ring, 2 px offset — the only boundary this control has on a white band, see Accessibility) · pressed (opacity 0.9) · disabled (icon at 35 % opacity) · selected (play/pause toggle: the glyph swaps) — no loading, no error state.

### Cards & Containers

**`card-content`** — the default story-card chrome.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg}`, shape `{rounded.card}` 6 px. Hosts a 16:9 thumbnail at the top + headline + caption.
- States: default · hover (headline underlines, thumbnail opacity 0.9 — paint and opacity only, the card never lifts) · focus-visible (2 px `{colors.focus}` ring around the whole card, 2 px offset) · pressed (opacity 0.9) · loading (skeleton: thumbnail and two text bars in `{colors.canvas-soft}`) — no disabled, no selected, no error state.

**`card-hero`** — the slightly larger card variant used as the lead story.
- Same chrome as `card-content` but headline scales to `{typography.display-sm}`.
- States: identical to `card-content` — default · hover · focus-visible · pressed · loading; no disabled, selected or error state.

### Inputs & Forms

**`text-input`** — the canonical text input.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, body in `{typography.body-sm}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.sm}` 6 px.
- States: default · hover (border stays `{colors.ink}`, cursor changes only) · focus-visible (2 px `{colors.focus}` ring, 2 px offset, border retained) · disabled (border and value at 35 % opacity) · error (border and the message below switch to `{colors.primary}`, which is also the brand's validation signal) · loading (field locked, inline spinner at the trailing edge) · selected (text selection only) — no pressed state.
- Placeholder text is `{colors.mute}` at 1.86:1 on `{colors.canvas}`, a real AA failure recorded in Accessibility.

### Navigation

**`nav-bar`** — the dark top nav, fixed to the page top.
- Background `{colors.ink}`, text `{colors.on-dark}`, padding `{spacing.lg} {spacing.3xl}`. Layout: logo left, link row right with login / search affordances.
- States: default · selected (the current section's link keeps a 2 px `{colors.primary}` underline) — the bar itself has only these two; hover, focus-visible, pressed, disabled, loading and error live on `nav-link` and on the controls inside it.

**`nav-link`** — the link items inside `nav-bar`.
- Text `{colors.on-dark}` on the `{colors.ink}` bar (declared in `components:` so the pair is measurable), set in `{typography.body-sm}`.
- States: default · hover (2 px `{colors.primary}` underline appears) · focus-visible (2 px `{colors.focus-on-dark}` ring, 2 px offset — the light ring, because the ground is `{colors.ink}`) · pressed (opacity 0.9) · selected (current section, underline persists) · disabled (label at 35 % opacity) — no loading, no error state.

**`footer`** — the dark footer band.
- Background `{colors.ink}`, text `{colors.on-dark}`, padding `{spacing.3xl} {spacing.3xl}`. Body in `{typography.body-sm}`; column eyebrows in `{typography.caption-uppercase}`.
- States: default only for the band. Its links carry default · hover (underline) · focus-visible (`{colors.focus-on-dark}` ring) · pressed · selected; no disabled, loading or error state.

### Signature Components

**`hero-band-dark`** — the dark navy/ink hero band hosting the massive display headline.
- Background `{colors.ink}` with full-bleed editorial photography overlay at reduced opacity; text `{colors.on-dark}`; padding `{spacing.3xl} {spacing.3xl}`. Headline in `{typography.display-hero}` (uppercase, weight 800).
- States: default · loading (photography fades in over `{colors.ink}` at `{motion.duration-base}`; the headline is painted immediately and never waits on the image). A band is not interactive: no hover, focus-visible, pressed, disabled, selected or error state. Controls inside it take the `{colors.focus-on-dark}` ring.

**`hero-band-red`** — the rare full-bleed red hero used on signature campaigns.
- Background `{colors.primary}`, text `{colors.on-primary}`, padding `{spacing.3xl} {spacing.3xl}`. Headline in `{typography.display-xl}`.
- States: default only — a campaign band, not a control. Controls inside it take the `{colors.focus-on-dark}` ring (white on `{colors.primary}` measures 4.81:1).

**`content-band-light`** — the white content band that follows every hero.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.3xl}`. Section headline in `{typography.display-md}` or `{typography.display-lg}` (weight 300).
- States: default only — a band, not a control. Controls inside it take the `{colors.focus}` ring.

**`speechmark-logo-orb`** — the red square hosting Vodafone's quotation-mark icon. The brand's visual anchor.
- Background `{colors.primary}`, white icon glyph, shape `{rounded.sm}`. Acts as a focal element between content bands, often near the centre of long pages.
- States: default and loading only — the orb is a mark, not a control, and its only animation is the loading spin described in Motion & Animation. No hover, focus-visible, pressed, disabled, selected or error state.

**`badge-chip`** — the inline metadata pill used for category tags inside story cards.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, label in `{typography.caption-strong}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.pill-md}` 32 px.
- States: default · selected (fill flips to `{colors.ink}`, label to `{colors.on-dark}`, when the chip is used as a filter) · hover and focus-visible only in that filter role (hover darkens the fill; focus-visible draws the 2 px `{colors.focus}` ring) · disabled (fill and label at 35 % opacity). As a static metadata tag it has one state. No pressed, loading or error state.

**`divider-on-dark`** — the 1 px hairline used between sections / columns on dark surfaces.
- 1 px solid `{colors.on-dark}` (often at 25 % opacity at the component level).
- States: default only — a rule, not a control.

**`divider-on-light`** — the light-surface counterpart, declared in `components:` so the boundary role is addressable by name.
- 1 px solid `{colors.ink}` — the Elevation Level 1 hairline already documented above, the same tone `text-input` binds as its outline. 14.82:1 against `{colors.canvas}`. States: default only.

### Examples (illustrative)

> Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`). Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently. `TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.
- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).
- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).
- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.
- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`


## Motion & Animation

This motion system is **prescribed to match the brand's visual identity and was not measured from the live site** — no duration, easing curve or stagger below is an extracted fact. The values are the **Calm** profile from the audit spec, used verbatim so this file stays comparable with its siblings; the assignment fits a brand whose own description is editorial photography plus one red accent, with weight-300 sub-displays doing the calm half of the typographic story.

Motion is deliberately thin here. The brand's hover language is a paint change — a fill flipping from `{colors.canvas}` to `{colors.primary}`, a 2 px underline appearing — not travel, and the spec permits that: `background-color`, `color`, `border-color` and `box-shadow` are paint-only, so a pill that only changes colour on hover is the honest brand behaviour rather than a missing animation. Where travel exists it is `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin`.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, chip, nav link, card headline) | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `background-color`, `color`, `border-color` — paint only, no travel | Colour change kept at `{motion.duration-reduced}` 150ms; nothing to remove |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` 1 → 0.9 | Opacity step kept, shortened to `{motion.duration-reduced}`; no scale is used, so none is removed |
| Focus (focus-visible ring) | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` of the 2 px ring, plus its `box-shadow` paint | Ring appears immediately with no fade; it is never animated away |
| Page / route transition | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | `opacity` 0 → 1 on the incoming band, `transform: translateY(8px) → 0` | `opacity` only at `{motion.duration-reduced}` 150ms; no travel |
| Modal / drawer | enter `{motion.duration-base}` 250ms, exit `{motion.duration-fast}` 150ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` plus `transform: translateY(12px)` (drawer: `translateX(100%)`); scrim `opacity` only — the brand uses a scrim, not a card shadow | `opacity` only at `{motion.duration-reduced}`; panel and scrim cross-fade in place |
| Dropdown (nav menu, mobile overlay) | enter `{motion.duration-fast}` 150ms, exit `{motion.duration-instant}` 80ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` plus `transform: translateY(-4px) → 0` | `opacity` only at `{motion.duration-reduced}` |
| Toast | enter `{motion.duration-base}` 250ms, exit `{motion.duration-fast}` 150ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` plus `transform: translateY(8px) → 0` | `opacity` only at `{motion.duration-reduced}`; auto-dismiss timing unchanged |
| List enter (story-card grid) | `{motion.duration-base}` 250ms per item, `{motion.stagger-step}` 40ms between items | `{motion.ease-enter}` | `opacity` plus `transform: translateY(12px) → 0` | Stagger dropped to 0ms, travel removed, one `opacity` fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` 150ms, no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | `opacity` at `{motion.duration-reduced}`, no stagger |
| Loading (spinner, skeleton, speechmark orb) | 1200ms linear loop — the one permitted infinite animation | linear | `transform: rotate()` on the spinner; `opacity` pulse 0.6 → 1 on skeleton bars | Loop frozen; a static indicator remains and the skeleton holds one steady `opacity` |

Entrance / exit asymmetry: every exit above is shorter than its matching entrance. Nothing animates on first paint in a way that delays content — hero type is painted at once and only the photography behind it fades in.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale travel, the 40ms list stagger,
     and the infinite loading loop (frozen to a static indicator). */
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important; /* {motion.duration-reduced} */
    transform: none !important;
  }
  /* Kept: opacity fades at {motion.duration-reduced} 150ms, and every
     paint-only state change (fill, label, border, underline) at the same
     duration — those carry the brand's hover and focus meaning. */
}
```

## Accessibility

### Measured contrast

Computed with WCAG 2.1 relative luminance from this file's own tokens. The extracted grey ramp is frozen: the failures below are real failures of the brand's own neutrals, not of this document, and they are recorded rather than corrected.

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` #25282b on `{colors.canvas}` #ffffff | 14.82:1 | 4.5:1 | Pass |
| `{colors.ink}` #25282b on `{colors.canvas-soft}` #f2f2f2 | 13.24:1 | 4.5:1 | Pass |
| `{colors.on-dark}` #ffffff on `{colors.ink}` #25282b | 14.82:1 | 4.5:1 | Pass |
| `{colors.on-primary}` #ffffff on `{colors.primary}` #e60000 | 4.81:1 | 4.5:1 | Pass |
| `{colors.primary}` #e60000 on `{colors.canvas}` #ffffff | 4.81:1 | 4.5:1 | Pass (label and outline-pill border alike) |
| `{colors.primary}` #e60000 on `{colors.canvas-soft}` #f2f2f2 | 4.3:1 | 4.5:1 | Fail as small text — red text on the soft band is for 24 px+ or 18.66 px/700+ only, where 3:1 applies |
| `{colors.body}` #7e7e7e on `{colors.canvas}` #ffffff | 4.06:1 | 4.5:1 | **Fail.** The brand's secondary body grey misses AA for normal text on white. Defensible only at 24 px+ (or 18.66 px bold), where the 3:1 threshold applies |
| `{colors.body}` #7e7e7e on `{colors.canvas-soft}` #f2f2f2 | 3.63:1 | 4.5:1 | **Fail.** Same grey on the soft band; still clears 3:1, so large text only |
| `{colors.mute}` #bebebe on `{colors.canvas}` #ffffff | 1.86:1 | 4.5:1 | **Fail, badly.** Placeholder and low-key footer links in this tone are unreadable for low-vision users at any size |
| `{colors.mute}` #bebebe on `{colors.canvas-soft}` #f2f2f2 | 1.66:1 | 4.5:1 | **Fail, badly.** Also below the 3:1 a boundary needs, which is why the illustrative `ex-*` hairlines were re-scoped to `{colors.body}` (3.63:1 on the soft band) |
| `button-primary` border `{colors.primary}` on its own `{colors.primary}` fill | 1.0:1 | 3.0:1 | Fail by construction — the 1 px border exists only to keep the filled pill the same box size as the outline pills. The pill's real boundary is `{colors.primary}` against `{colors.canvas}` at 4.81:1 |
| `button-icon-circular` outline `{colors.canvas}` on `{colors.canvas}` #ffffff | 1.0:1 | 3.0:1 | **Fail.** A white circular icon button has no boundary on a white band. It is intended over hero photography, where no measurable ratio exists; on `{colors.canvas}` its only perceivable edge is the focus ring. See Needs-approval note in the audit report |
| `{colors.canvas}` #ffffff vs `{colors.canvas-soft}` #f2f2f2 | 1.12:1 | — | The two light layers are not distinguishable as a boundary. That is by design: the brand elevates by polarity flip to `{colors.ink}`, not by a soft neutral step |

### Focus ring

The brand ships no extracted focus ring, so one is **prescribed** here, reusing tones the palette already owns rather than introducing a new brand colour:

- `{colors.focus}` #25282b — the same tone as `{colors.ink}`, drawn as a 2 px ring with a 2 px offset **outside** the control, so it is judged against the surface behind it: 14.82:1 on `{colors.canvas}`, 13.24:1 on `{colors.canvas-soft}`, 3.08:1 on `{colors.primary}`. All clear the 3:1 WCAG 2.2 Focus Appearance threshold.
- `{colors.focus-on-dark}` #ffffff — the same tone as `{colors.on-dark}`, for controls on the brand's dark and red signature surfaces: 14.82:1 on `{colors.ink}`, 4.81:1 on `{colors.primary}`.

Over full-bleed hero photography, which has no measurable colour, the ring renders two-tone: 2 px `{colors.focus-on-dark}` with a 1 px `{colors.focus}` outer edge, so one polarity always separates it from the image.

### Tap targets and reduced motion

- The `button-primary` pill computes to ~52 px tall from `{spacing.md}` 12 px vertical padding plus the 28 px `{typography.button-md}` line height, comfortably over the 44 px minimum. This is arithmetic from the tokens, not a measurement of a rendered page.
- Icon-only controls (`button-icon-circular`) must be padded to a 44 px hit area; the glyph itself is smaller.
- Reduced motion is honoured as specified above: all travel, scale and stagger removed, opacity fades held at `{motion.duration-reduced}` 150ms, the loading loop frozen.
- Colour is never the only signal: `nav-link` selection and card hover both carry an underline alongside the colour change, and `text-input` error pairs the red border with a text message.


## Do's and Don'ts

### Do
- Reserve `{colors.primary}` Vodafone Red for primary CTAs and the `speechmark-logo-orb`. Every conversion target uses the red pill.
- Set hero headlines in `{typography.display-hero}` weight 800 UPPERCASE with tight `-1px` tracking. That stencil look IS the brand voice.
- Use `{rounded.pill-lg}` 60 px on every interactive pill. The brand never uses square corners on CTAs.
- Cycle page surfaces in `{colors.ink}` dark hero → `{colors.canvas}` light content → `{colors.ink}` footer. Surface contrast is the depth cue.
- Pair editorial portrait photography with the massive display headline overlay — that combination IS the brand's signature.
- Render the speechmark logo orb at consistent size relative to surrounding content — it's the brand's centre of gravity on every page.

### Don't
- Don't introduce a second accent colour. The brand operates with red + ink + grayscale only.
- Don't render headlines in sentence case at hero scale. Hero display IS uppercase weight 800.
- Don't render the primary CTA as a square rectangle. The 60 px pill is non-negotiable.
- Don't drop a soft drop-shadow on cards. The brand relies on surface-colour contrast, not shadow.
- Don't substitute the speechmark logo orb with a wordmark or a different shape. The orb is the iconic mark.
- Don't pair the weight 800 display face with letter-spacing 0 at 144 px — the `-1px` tracking is part of the brand's calibration.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 600px | Hero display scales down to ~64 px; story-card grid drops to 1-up; nav collapses to hamburger. |
| Tablet | 600–1023px | Story-card grid 2-up; display headlines drop to 90 – 110 px. |
| Desktop | 1024–1399px | Full display headline at 126 – 144 px; 2-up story grid. |
| Ultra-wide | ≥ 1400px | Container caps at ~1400 px; bands stay edge-to-edge in colour. |

### Touch Targets
The `button-primary` pill renders at ~52 px tall (12 px vertical padding + 28 px line-height). All buttons comfortably meet WCAG AAA at every breakpoint.

### Collapsing Strategy
- **Nav**: full link row at desktop. Collapses to a hamburger menu at mobile; the menu opens as a dark overlay with the same link list stacked.
- **Hero**: the massive display headline scales fluidly. At mobile, the photography crop tightens to the figure's face only.
- **Story-card grid**: 2-up → 1-up at the breakpoint above.
- **Speechmark logo orb**: stays at consistent size relative to surrounding content; never shrinks below ~48 px.

### Image Behavior
- **Hero photography**: full-bleed 16:9 or 4:3 portraits at desktop; tighter crops at mobile.
- **Story-card thumbnails**: 16:9 landscape inside `{rounded.card}` 6 px chrome.
- **Speechmark orb**: always rendered as the red SVG quote-mark icon, never substituted.
- **Logo bar (if present on partner pages)**: monochrome SVGs at consistent height.

## Known Gaps

- **No extracted motion.** Every duration, easing curve and stagger in Motion & Animation is the prescribed Calm profile, not a measurement of vodafone.com. Nothing in the source file records a real timing function.
- **No extracted focus ring.** `{colors.focus}` and `{colors.focus-on-dark}` are prescribed, and reuse `{colors.ink}` and `{colors.on-dark}`; the real site's ring was never captured.
- **The grey ramp fails AA.** `{colors.body}` (4.06:1 on white) and `{colors.mute}` (1.86:1 on white) are extracted brand values and are left untouched. Any implementation that uses them for normal-size text is below AA; the nearest passing substitutes are in the audit report, not applied here.
- **No border token.** The brand has no dedicated hairline colour: boundaries reuse `{colors.ink}` on light surfaces, `{colors.on-dark}` on dark ones. `divider-on-light` declares the first of those as a component binding rather than inventing a colour.
- **No semantic palette.** Success, warning and info tones are not part of the documented marketing system; `{colors.primary}` doubles as the error signal.
- **No shadow scale.** The file documents no shadow values anywhere, so no `shadow:` group exists. That matches the brand, which flat-fills and flips polarity instead.
- **Tap targets, overflow and frame rate are unverified.** There is no rendered page behind this document, so the ~52 px pill height and the "WCAG AAA at every breakpoint" claim kept verbatim in Responsive Behavior are both arithmetic from tokens, not measurements.
- **Opacity values are prose-level.** The 25 % `divider-on-dark` and the 35 % disabled treatment are stated in prose and carry no token; they are prescribed conventions, not extracted values.
- **`ex-*` surfaces are auto-derived**, not extracted from the live site. Their hairlines were re-pointed from `{colors.mute}` (1.66:1, below the 3:1 a boundary needs) to `{colors.body}` (3.63:1). The extracted components' own bindings were left exactly as found.
