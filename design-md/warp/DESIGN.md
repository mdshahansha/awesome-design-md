---
version: alpha
name: Warp-Inspired-design-analysis
description: An inspired interpretation of Warp's design language — an agentic terminal-and-development-environment brand whose surface is a warm near-charcoal canvas (a tint warmer than pure black), broken only by clean Inter typography, the occasional Instrument Serif italic moment, and dense terminal-mockup imagery; CTAs are unusually understated, with shape geometry running tighter than most marketing sites.

colors:
  primary: "#f7f5f0"
  on-primary: "#2b2622"
  ink: "#f7f5f0"
  body: "#c9c0ad"
  body-strong: "#dad2c1"
  mute: "#aea69c"
  canvas: "#2b2622"
  canvas-soft: "#383330"
  hairline: "#3f3a36"
  focus: "#f7f5f0"

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

typography:
  display-xl:
    fontFamily: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif
    fontSize: 64px
    fontWeight: 400
    lineHeight: 70.4px
    letterSpacing: -1.6px
  display-lg:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 48px
    fontWeight: 400
    lineHeight: 52.8px
    letterSpacing: -1.2px
  display-md:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 32px
    fontWeight: 500
    lineHeight: 40px
    letterSpacing: -0.8px
  display-sm:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 24px
    fontWeight: 500
    lineHeight: 32px
    letterSpacing: -0.4px
  display-serif:
    fontFamily: Instrument Serif, Georgia, "Times New Roman", serif
    fontSize: 48px
    fontWeight: 400
    lineHeight: 52px
    letterSpacing: -0.5px
  body-lg:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
  body-md:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-md-strong:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
  body-sm:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
  caption:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  code:
    fontFamily: DM Mono, ui-monospace, SFMono-Regular, Menlo, monospace
    fontSize: 13px
    fontWeight: 400
    lineHeight: 18px
  code-md:
    fontFamily: DM Mono, ui-monospace, SFMono-Regular, Menlo, monospace
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  button-md:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px

rounded:
  none: 0px
  xxs: 1px
  xs: 2px
  sm: 3px
  md: 4px
  lg: 6px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 10px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 96px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    padding: "{spacing.md} {spacing.xl}"
  nav-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary-ghost:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs}"
  text-input:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  card-content:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  card-mockup:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  download-tile:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  press-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} 0"
  job-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md-strong}"
    padding: "{spacing.lg} 0"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.5xl} {spacing.xl}"
  content-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.5xl} {spacing.xl}"
  partner-logo-tile:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  testimonial-card:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.sm} {spacing.md}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.2xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"

---


## Overview

Warp is an "agentic development environment" — a terminal application that wraps an AI agent — and its marketing site mirrors the product's posture: a single dark band running the entire page, warmer than pure black (`{colors.canvas}` `#2b2622` carries a hint of brown-beige from the brand's oklch-defined warmth value), with copy set almost entirely in Inter. The page reads more like a developer's reading-mode editor than a marketing surface.

The decoration is restrained. Two terminal screenshots open the hero (split between the two main product modes — agent + terminal). A partner-logo strip (Anthropic / OpenAI / Google / Stanford) sits below the hero on a slightly warmer tile surface. A single testimonial card with a portrait photograph. A press-coverage list. Then the page closes with download tiles for Mac / Linux / Windows. There is no gradient, no atmospheric backdrop, no illustration system.

Type is the second decisive voice. Hero display sits at 64 px Inter weight 400 with `-1.6px` tracking — restrained for a hero, deliberately quiet. The brand carries DM Mono as its monospace face for code blocks, and Instrument Serif italics occasionally appear for editorial moments. Body text is 16 px Inter at line-height 1.5, very readable.

**Key Characteristics:**
- A single primary "color" — really an off-white `{colors.primary}` (`#f7f5f0`) — that doubles as text on canvas and as the button-primary fill. There is no chromatic brand accent.
- Warm dark canvas (`{colors.canvas}` `#2b2622`) is the only page surface. The brand's defining tone is the brown-warmth, not pure black.
- Extremely tight button radii — 3 / 4 px (1 / 2× the brand's `{rounded.md}` 4 px base) — the brand never uses generous pill shapes for CTAs. Only icon containers use `{rounded.full}`.
- Inter sans + DM Mono mono is the canonical pairing. Instrument Serif appears as a third editorial face for occasional italics.
- Terminal-mockup imagery is the brand's only consistent decorative system — no gradients, no atmospheric overlays.
- A subtle warm tint runs through every neutral; even body text and dividers carry a hint of warmth rather than neutral gray.

## Colors

### Brand & Accent
- **Off White Primary** (`{colors.primary}` — `#f7f5f0`): The brand's "primary" is a warm off-white. Used as button-primary fill, as default text on canvas, as the wordmark color. There is no chromatic brand accent — the off-white IS the brand's distinguishing tone.

### Surface
- **Canvas** (`{colors.canvas}` — `#2b2622`): The warm dark page background. Resolved from `oklch(22.0% 0.004 84.6)`. Slightly browner than pure black, slightly warmer than a neutral gray — the warmth IS the brand's identity.
- **Canvas Soft** (`{colors.canvas-soft}` — `#383330`): A lighter warm-dark fill used for cards, mockup chrome, and partner-logo tiles.
- **Hairline** (`{colors.hairline}` — `#3f3a36`): 1 px solid divider on dark surfaces. **Extracted and frozen, and it fails WCAG as a boundary:** 1.33:1 on `{colors.canvas}` and 1.11:1 on `{colors.canvas-soft}`, both below the 3:1 a component boundary needs. This is a real property of the brand, not a documentation error. Scope it to *decoration* — card chrome, band separators, list rules, anywhere the boundary is redundant with a fill change. Where a 1 px line is the **only** boundary of an interactive control, draw it in `{colors.mute}` (5.19:1 on `{colors.canvas-soft}`, 6.23:1 on `{colors.canvas}`), which the palette already owns; no new token is needed.

### Focus
- **Focus** (`{colors.focus}` — `#f7f5f0`): the focus ring. This is `{colors.primary}` / `{colors.ink}` under a role name, not a new brand colour — the brand is monochrome and its accent *is* its paper, so the ring is drawn in that paper with a mandatory 2 px `{colors.canvas}` offset. It measures 13.74:1 on `{colors.canvas}` and 11.44:1 on `{colors.canvas-soft}`. Every surface this file defines is warm-dark, so one ring serves the whole system; no `focus-on-light` counterpart is needed.

### Text
- **Ink** (`{colors.ink}` — `#f7f5f0`): Default text on canvas — same off-white as the primary, intentionally unified.
- **Body Strong** (`{colors.body-strong}` — `#dad2c1`): Mid-emphasis body text.
- **Body** (`{colors.body}` — `#c9c0ad`): Secondary body text — captions, supporting copy, press-coverage rows.
- **Mute** (`{colors.mute}` — `#aea69c`): Lowest-priority text — timestamps, fine print, footer secondary lines. Resolved from `oklch(71.5% 0.008 84.6)`.

### Semantic
The brand doesn't surface a separate error / warning / success palette in its marketing pages. Validation cues come from the unified off-white system; in-product semantic colors live in the terminal application proper.

## Typography

### Font Family
Three faces ladder the system:
1. **Inter** for every display, body, button, link, and label role. Weights 400 / 500 are the working pair. Used with the brand's "Inter Fallback" custom face as the metric-compatible system fallback.
2. **DM Mono** for terminal mockups, command snippets, and code blocks. Weight 400 only. Loaded as `--font-dm-mono`.
3. **Instrument Serif** for occasional editorial italic moments — rare on the marketing surface, but documented as a third face for emphasised tagline-style phrases. **Abel** is also loaded as a fourth fallback for headline emphasis.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 64px | 400 | 70.4px | -1.6px | Hero headline ("Warp is the agentic development environment"). |
| `{typography.display-lg}` | 48px | 400 | 52.8px | -1.2px | Section headlines. |
| `{typography.display-md}` | 32px | 500 | 40px | -0.8px | Sub-section displays. |
| `{typography.display-sm}` | 24px | 500 | 32px | -0.4px | Card titles and lead emphasis. |
| `{typography.display-serif}` | 48px | 400 | 52px | -0.5px | Instrument Serif italic editorial moments. |
| `{typography.body-lg}` | 18px | 400 | 28px | 0 | Lead paragraphs. |
| `{typography.body-md}` | 16px | 400 | 24px | 0 | Default body. |
| `{typography.body-md-strong}` | 16px | 500 | 24px | 0 | Bold inline body. |
| `{typography.body-sm}` | 14px | 400 | 20px | 0 | Secondary body. |
| `{typography.body-sm-strong}` | 14px | 500 | 20px | 0 | Nav link / button labels. |
| `{typography.caption}` | 12px | 400 | 16px | 0 | Captions, fine print. |
| `{typography.code}` | 13px | 400 | 18px | 0 | Terminal mockup body. |
| `{typography.code-md}` | 14px | 400 | 20px | 0 | Inline command snippets. |
| `{typography.button-md}` | 14px | 500 | 20px | 0 | Button labels. |

### Principles
- **Hero display at weight 400** — the brand reads as quietly confident, not as a billboard.
- **Negative tracking is part of the voice.** `-1.6 px` at 64 px hero, scaling down through display levels.
- **Inter for narrative, DM Mono for technical.** Strict role separation.

### Note on Font Substitutes
All three faces are open or freely-loadable:
- **Inter** — load directly from Google Fonts or Vercel-hosted CDN.
- **DM Mono** — open-source on Google Fonts.
- **Instrument Serif** — open-source on Google Fonts.

## Layout

### Spacing System
- **Base unit**: 4 px (with occasional 10 px and 6 px values for button padding).
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 10 px · `{spacing.lg}` 16 px · `{spacing.xl}` 24 px · `{spacing.2xl}` 32 px · `{spacing.3xl}` 48 px · `{spacing.4xl}` 64 px · `{spacing.5xl}` 96 px.
- **Section padding**: hero / content bands use `{spacing.5xl}` 96 px on desktop.
- **Card interior**: cards sit at `{spacing.xl}` 24 px.

### Grid & Container
- Marketing content centres at roughly 1200 px width.
- Hero: 2-column at desktop (split between two terminal screenshots), stacks at mobile.
- Partner logos: 5-up wrapping flex row.
- Download tiles: 3-up at desktop (Mac / Linux / Windows), 1-up at mobile.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default for hero band. |
| Level 1 — Hairline | 1 px solid `{colors.hairline}` border on `{colors.canvas-soft}`. | Default card chrome. |
| Level 2 — Inset Card | Canvas-soft fill against canvas background with 1 px hairline. | Mockup cards, download tiles, testimonial cards. |

The brand uses surface-contrast and hairline borders for elevation; soft drop-shadows do not appear in the marketing surface.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed bands. |
| `{rounded.xxs}` | 1px | Tightest in-text indicator. |
| `{rounded.xs}` | 2px | Inline very-small chips. |
| `{rounded.sm}` | 3px | Default button radius — extremely tight. |
| `{rounded.md}` | 4px | Card chrome (the brand's `--radius` base). |
| `{rounded.lg}` | 6px | Slightly larger cards. |
| `{rounded.pill}` | 9999px | Status pills. |
| `{rounded.full}` | 9999px | Circular icon containers (`button-icon-circular`). Same value as `{rounded.pill}`; the two names are kept because the extracted source uses both. |

### Photography Geometry
- Terminal mockups: ~3:2 inside `{rounded.md}` card chrome.
- Partner logos: monochrome SVGs at consistent 24 px height inside tile cards.
- Testimonial portraits: 1:1 square inside `{rounded.md}`.

## Components

### Buttons

**`button-primary`** — the off-white CTA on dark canvas.
- Background `{colors.primary}` (off-white), text `{colors.on-primary}` (warm dark), label `{typography.button-md}`, padding `{spacing.sm} {spacing.lg}`, shape `{rounded.sm}` 3 px. Tight.
- States: default · hover (fill lifts to `{colors.body-strong}`, `{motion.duration-fast}`) · focus-visible (2 px `{colors.focus}` ring, 2 px `{colors.canvas}` offset) · pressed (fill `{colors.mute}`, `{motion.duration-instant}`) · disabled (fill `{colors.hairline}`, label `{colors.mute}`, no pointer) · loading (label swapped for a mono caret spinner, control width frozen) · error (not applicable — form-level errors are surfaced on `text-input`).

**`button-secondary-ghost`** — the ghost-style secondary used for nav and tertiary actions.
- Background `{colors.canvas}`, text `{colors.ink}`, no border, same typography / shape.
- States: default · hover (fill `{colors.canvas-soft}`, paint-only) · focus-visible (`{colors.focus}` ring) · pressed (fill `{colors.hairline}`) · disabled (label `{colors.mute}`) · loading (inherits `button-primary` behaviour).

**`button-icon-circular`** — the circular icon container.
- Background `{colors.canvas}`, ink icon, shape `{rounded.full}`. Used for nav controls (search, theme).
- States: default · hover (fill `{colors.canvas-soft}`) · focus-visible (`{colors.focus}` ring) · pressed (fill `{colors.hairline}`) · selected (theme toggle only — fill `{colors.canvas-soft}`, icon `{colors.primary}`) · disabled (icon `{colors.mute}`).

### Cards & Containers

**`card-content`** — the default content card on canvas-soft.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, padding `{spacing.xl}`, shape `{rounded.md}`.
- States: default and hover only when the card is a link (border to `{colors.mute}`, paint-only). A non-interactive `card-content` genuinely has one state: default.

**`card-mockup`** — the terminal-screenshot mockup card.
- Same chrome as `card-content` but body in `{typography.code}` (DM Mono) when text appears inside.
- States: default only. The mockup card is decorative and carries no interaction.

**`download-tile`** — the Mac / Linux / Windows download tile.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, hairline border, padding `{spacing.xl}`, shape `{rounded.md}`. Hosts a platform icon + label + download CTA.
- States: default · hover (border `{colors.mute}`) · focus-visible (`{colors.focus}` ring on the whole tile) · pressed (fill `{colors.hairline}`) · selected (the tile matching the visitor's detected platform — border `{colors.primary}`) · loading (download handshake: caret spinner in the CTA slot) · disabled (unsupported platform — label `{colors.mute}`).

**`partner-logo-tile`** — the canvas-soft tile hosting a partner logo.
- Background `{colors.canvas-soft}`, monochrome logo SVG inside, padding `{spacing.lg}`, shape `{rounded.md}`.
- States: default only. The logo tile is non-interactive.

**`testimonial-card`** — the single quote-style card with a portrait.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.md}`. Portrait 1:1 + body in `{typography.body-md}`.
- States: default only — a single static quote card.

**`press-row`** — the press-coverage list item.
- Background `{colors.canvas}` (no fill — sits on the canvas band), 1 px solid bottom border `{colors.hairline}`, body in `{typography.body-md}`, padding `{spacing.lg}` 0.
- States: default · hover (title to `{colors.ink}`, paint-only) · focus-visible (`{colors.focus}` ring inset to the row box) · pressed (title `{colors.body}`).

**`job-row`** — the "Join our team" list item (single row per open role).
- Background `{colors.canvas}`, 1 px solid bottom border, body in `{typography.body-md-strong}`, padding `{spacing.lg}` 0.
- States: default · hover (bottom border to `{colors.mute}`) · focus-visible (`{colors.focus}` ring) · pressed (fill `{colors.canvas-soft}`).

### Inputs & Forms

**`text-input`** — the dark-canvas text input.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, body in `{typography.body-sm}`, padding `{spacing.sm} {spacing.md}`, shape `{rounded.sm}`.
- States: default · hover (border `{colors.mute}`) · focus-visible (border `{colors.focus}` plus a 2 px `{colors.focus}` ring at 2 px offset; the ring, not the border, is the conformant indicator) · disabled (fill `{colors.canvas}`, text `{colors.mute}`) · loading (async validation — caret spinner in the trailing slot) · error (border and helper text `{colors.body-strong}` plus a mono `!` glyph; the brand surfaces no red, so the error cue is weight and glyph, not hue) · selected (text selection only, no control-level selected state).
- Accessibility note: the extracted `{colors.hairline}` border measures 1.11:1 against `{colors.canvas-soft}` and is not a conformant boundary on its own. The focus ring and the fill/canvas luminance step carry the affordance. See Accessibility.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.xl}`.
- States: default and a scrolled state only (hairline bottom border appears once the page scrolls past the hero). No hover or focus of its own; its children carry those.

**`nav-link`** — link items in nav.
- Background `{colors.canvas}`, text `{colors.ink}`, body in `{typography.body-sm-strong}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.sm}`.
- States: default · hover (fill `{colors.canvas-soft}`, paint-only) · focus-visible (`{colors.focus}` ring, 2 px offset) · pressed (fill `{colors.hairline}`) · selected (current route — text `{colors.primary}`, 1 px `{colors.primary}` underline) · disabled (text `{colors.mute}`).

**`footer`** — the footer band.
- Background `{colors.canvas}`, text `{colors.body}`, padding `{spacing.3xl} {spacing.xl}`. Body in `{typography.body-sm}`.
- States: container is default-only; footer links inherit `nav-link` hover, focus-visible, pressed and selected.

### Signature Components

**`hero-band`** — the dark hero band hosting the 64-px Inter headline.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.5xl} {spacing.xl}`. Headline `{typography.display-xl}` (64 px / 400 / `-1.6 px`). Below: a 2-column terminal-mockup split.
- States: default only — a static band. Its CTA cluster uses `button-primary` and `button-secondary-ghost` states.

**`content-band`** — the standard content band.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.5xl} {spacing.xl}`. Section headline `{typography.display-md}`.
- States: default only.

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

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or transition was extracted from Warp's marketing surface; the file records none. The values below are the shared **Crisp** profile from `theme-audit/SPEC.md` section 5, assigned because the brand's identity is a terminal and development environment — state change should read as instant, with no entrance choreography. Every value is referenced as a `{motion.*}` token so files sharing the profile stay comparable.

The brand is near-monochrome and flat: it has no shadow system, no gradient and no chromatic accent, so most of its state feedback is a **paint-only** change — `background-color`, `border-color`, `color`. That is permitted and is deliberately not dressed up with a scale pop, which would contradict a brand whose own Don'ts forbid generous shapes and heavy weights. Where something does move, only `transform` and `opacity` animate; never `width`, `height`, `top`, `left` or `margin`.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav-link, tile, row) | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `background-color`, `border-color`, `color` — paint only, no travel | Unchanged; the change is paint, not motion. |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `background-color` — paint only. No scale: the brand's shapes are 3–4 px and a pop reads wrong on them. | Unchanged. |
| Focus-visible | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring, 0 → 1 | Ring appears at full opacity with no transition. |
| Page / route transition | `{motion.duration-base}` 150ms in, `{motion.duration-fast}` 100ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` only. No cross-fade travel; the canvas is one continuous band and must not appear to slide. | `opacity` fade at `{motion.duration-reduced}` 100ms. |
| Modal / drawer | `{motion.duration-base}` 150ms in, `{motion.duration-fast}` 100ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(4px → 0)` (drawer: `translateX`) | Travel removed; `opacity` only at `{motion.duration-reduced}` 100ms. Scrim fades at the same duration. |
| Dropdown / nav menu | `{motion.duration-fast}` 100ms in, `{motion.duration-instant}` 60ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(2px → 0)` | Travel removed; `opacity` only at `{motion.duration-reduced}` 100ms. |
| Toast (`ex-toast`) | `{motion.duration-base}` 150ms in, `{motion.duration-fast}` 100ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(6px → 0)` | Travel removed; `opacity` only at `{motion.duration-reduced}` 100ms. Auto-dismiss timing is unchanged. |
| List enter (download tiles, press rows, job rows) | `{motion.duration-fast}` 100ms per item, `{motion.stagger-step}` 20ms between items | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px → 0)` | Travel and stagger removed; all items fade together at `{motion.duration-reduced}` 100ms. |
| List exit (filtered / removed rows) | `{motion.duration-instant}` 60ms, no stagger | `{motion.ease-exit}` | `opacity` + `transform: translateY(0 → 2px)` | Travel removed; `opacity` only at `{motion.duration-reduced}` 100ms. |
| Loading | `{motion.duration-emphasis}` 300ms per cycle, infinite while pending | linear (`steps()` for the caret) | `opacity` of a DM Mono block caret `▌`, blinking in place. The only infinite animation in the system, and the only one that is brand ambience as well as a loader — a blinking terminal caret *is* the identity. | Blink frozen; the caret stays at full opacity and the control's `aria-busy` state carries the information. |

Rules this system observes:
- Every exit is shorter than its matching entrance (150→100, 100→60, 150→100).
- Nothing animates on first paint in a way that delays content: the hero band, its headline and the two terminal mockups render at final position and full opacity. Only post-load, user-initiated changes animate.
- The blinking caret is the sole infinite animation, and it is declared above as both loader and deliberate brand ambience.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. Every translateY / translateX
     above collapses to its end position. The stagger on list enter
     collapses to 0ms. The loading caret's blink is frozen at opacity 1
     (brand ambience frozen, per SPEC section 6). */
  *, *::before, *::after {
    transition-duration: var(--motion-duration-reduced); /* 100ms */
    animation: none;
  }
  /* Kept: opacity fades, at {motion.duration-reduced} 100ms and never
     longer; and every paint-only change (background-color, border-color,
     color), which is not motion and is left exactly as specified. */
}
```

What is removed: all `transform` travel, all scale, the `{motion.stagger-step}` sequencing, and the caret blink. What remains: `opacity` fades capped at `{motion.duration-reduced}` 100ms, and all paint-only hover, press and selected feedback, which is how a monochrome brand communicates state and is not motion.

## Accessibility

### Measured contrast

All ratios computed with WCAG 2.1 relative luminance from the hexes in this file's frontmatter.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#f7f5f0` on `{colors.canvas}` `#2b2622` | 13.74:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` `#383330` | 11.44:1 | 4.5:1 | Pass |
| `{colors.body-strong}` `#dad2c1` on `{colors.canvas}` | 9.96:1 | 4.5:1 | Pass |
| `{colors.body}` `#c9c0ad` on `{colors.canvas}` | 8.29:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas-soft}` | 6.90:1 | 4.5:1 | Pass |
| `{colors.mute}` `#aea69c` on `{colors.canvas}` | 6.23:1 | 4.5:1 | Pass |
| `{colors.mute}` on `{colors.canvas-soft}` | 5.19:1 | 4.5:1 | Pass |
| `{colors.on-primary}` `#2b2622` on `{colors.primary}` `#f7f5f0` | 13.74:1 | 4.5:1 | Pass |
| `{colors.focus}` `#f7f5f0` on `{colors.canvas}` | 13.74:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.canvas-soft}` | 11.44:1 | 3.0:1 | Pass |
| **`{colors.hairline}` `#3f3a36` on `{colors.canvas}`** | **1.33:1** | 3.0:1 | **Fail — disclosed** |
| **`{colors.hairline}` on `{colors.canvas-soft}`** | **1.11:1** | 3.0:1 | **Fail — disclosed** |
| `{colors.canvas-soft}` on `{colors.canvas}` (layer step, not a text pair) | 1.20:1 | — | Informational |

**The real brand fails WCAG at its hairline.** `{colors.hairline}` is an extracted value and is left exactly as extracted, including its existing `components:` bindings. It is not a conformant component boundary anywhere in this system. Two consequences, and both are honest statements about the brand rather than fixes:

1. Treat the hairline as decoration. Card chrome, band separators and list rules keep it, because in each of those places the boundary is redundant with a fill change or with spacing.
2. Where a 1 px line is the *only* boundary of an interactive control — `text-input` is the clear case — the conformant indicator is the `{colors.focus}` ring plus the `{colors.canvas-soft}`/`{colors.canvas}` fill step, and the line itself should be drawn in `{colors.mute}` (5.19:1 / 6.23:1). Re-pointing `text-input.borderColor` in the token block would change a documented fact about the real site, so it has not been done here; it is raised for a brand owner to answer.

The 1.20:1 step between `{colors.canvas}` and `{colors.canvas-soft}` is also worth stating plainly: the brand's two surfaces are nearly the same luminance, so surface contrast alone does not separate a card from the page. That is the brand's chosen flatness, and it is the reason the hairline — weak as it is — is load-bearing visually even though it is not load-bearing for conformance.

The brand surfaces no error, warning or success hue, so `text-input`'s error state cannot be signalled by colour. It is signalled by a mono `!` glyph plus `{colors.body-strong}` helper text — which also satisfies the rule that colour is never the sole carrier of meaning, by default rather than by design.

### Focus ring

- Token: `{colors.focus}` `#f7f5f0` — the brand's own paper (`{colors.primary}` / `{colors.ink}`), reused under a role name. The brand is monochrome and declares that it has no chromatic accent, so inventing a coloured ring would contradict its first rule.
- Geometry: 2 px ring, drawn **outside** the control with a mandatory 2 px `{colors.canvas}` offset. The offset is what makes it work on `button-primary`, whose fill is the same off-white: against that fill the ring measures 1.00:1, so without the dark offset it would be invisible. With the offset, the ring is judged against the surface behind it — the canvas — as WCAG 2.2 Focus Appearance asks.
- Visibility on every surface this file defines: `{colors.canvas}` 13.74:1, `{colors.canvas-soft}` 11.44:1. Both clear 3:1. There is no light surface in this system, so no second ring is required.
- The ring is never suppressed. `:focus-visible` is used so pointer users do not see it, but keyboard focus is always drawn.

### Tap targets

`button-primary` computes to ~36 px tall (8 px padding × 2 + 20 px line-height), below the 44 × 44 px floor. Mobile must inflate the hit area with additional padding or a pseudo-element, keeping the 3 px radius visually unchanged. **Not verifiable from this document** — tap-target size needs a rendered page, so this is a specification, not a measurement.

### Reduced motion

See the `@media (prefers-reduced-motion: reduce)` rule above: all travel, scale, stagger and the caret blink are removed; opacity fades remain, capped at `{motion.duration-reduced}` 100ms; paint-only feedback is untouched.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` off-white for primary CTA pills and default text. There is no chromatic accent.
- Use tight `{rounded.sm}` 3 px or `{rounded.md}` 4 px button radii. The brand never uses generous pills for CTAs.
- Set hero headlines in Inter weight 400 with `-1.6 px` tracking. The brand reads as quietly confident.
- Pair Inter (sentence-case) with DM Mono (code blocks, terminal mockups).
- Keep the warm-dark canvas tone — pure black breaks the brand's identity.

### Don't
- Don't introduce a chromatic brand accent. The off-white-on-warm-dark IS the brand's voice.
- Don't render the hero headline in heavy weight (700+). The brand's display is intentionally light.
- Don't use generous pill CTAs. The brand's button radius is 3-4 px, almost rectangular.
- Don't replace the warm dark canvas with neutral gray or pure black. The warmth IS the brand.
- Don't drop a soft drop-shadow on cards. Hairlines + surface contrast carry elevation.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hero stacks; 1-up grids; nav hamburger. |
| Tablet | 768–1023px | 2-up grids. |
| Desktop | ≥ 1024px | Full hero split; 3-up download tiles. |

### Touch Targets
Buttons render at ~36 px tall (8 px vertical padding + 20 px line-height). Mobile inflates touch area through additional padding to meet WCAG 44 × 44 px floor.

### Collapsing Strategy
- Nav: full link row + Sign in / Download right cluster at desktop. Hamburger at mobile.
- Hero terminal-mockup split: stacks vertically at mobile.
- Press / job rows: full-width single column; stay legible at all widths.

### Image Behavior
- **Terminal mockups**: rendered as dark cards with the actual terminal UI inside (warm canvas + colored syntax). Aspect ratio ~3:2.
- **Partner logos**: monochrome SVGs on dark tile cards.
- **Testimonial portraits**: 1:1 square crop inside `{rounded.md}` card chrome.

## Known Gaps

- **Motion is prescribed, not extracted.** Nothing in the source records a duration, an easing curve or a transition for this brand. The whole `motion:` group and the Motion & Animation section are the shared **Crisp** profile, stated as prescribed in that section's first line. The one piece of it that is argued from the brand rather than from the profile table is the blinking DM Mono caret as the loading indicator, and that is an interpretation of the brand's terminal identity, not an extracted asset.
- **No semantic palette.** The brand surfaces no error, warning or success colour on its marketing pages. Error states are therefore specified with a glyph and type weight rather than hue. In-product semantic colours live in the terminal application proper and were not extracted.
- **The hairline fails WCAG and stays as extracted.** 1.33:1 on `{colors.canvas}`, 1.11:1 on `{colors.canvas-soft}`. Disclosed in Accessibility; the `components:` bindings are unchanged. Whether `text-input.borderColor` should be re-pointed to `{colors.mute}` is a brand-owner decision.
- **Tap targets, overflow and layout behaviour are unverified.** This is a document, not a running UI. The ~36 px button height is arithmetic from the padding and line-height tokens; the 44 px mobile inflation is a specification. Nothing here was rendered or measured on screen.
- **`{rounded.pill}` and `{rounded.full}` are the same value** (9999px). Both names are extracted and both are referenced, so neither was removed, but a consumer should treat them as one step in the radius ladder.
- **`{spacing.md}` 10 px sits off the 4 px base**, as does the 6 px button padding mentioned in Layout. Extracted as such; not normalised.
- **The `ex-*` examples describe shadows the brand does not have.** `ex-modal-card` says "elevated shadow" and `ex-toast` says "medium shadow", but Elevation & Depth records no shadow in the brand and there is no `shadow:` token group. Those two descriptions are auto-derived boilerplate and contradict the brand; a modal or toast in this system should be separated by the `{colors.canvas-soft}` fill step and a `{colors.mute}` boundary, not by a shadow. The descriptions were left verbatim because they are generated text, not an editorial claim.
- **No light polarity.** The file documents one canvas polarity only. `ex-pricing-tier-featured` refers to "light mode" behaviour that this token set does not define.
- **Focus ring geometry is prescribed.** The 2 px ring and 2 px offset are specified here, not extracted; the source file defined no focus ring at all.
