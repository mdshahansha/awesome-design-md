---
version: alpha
name: Linear-design-analysis
description: "A near-black product-focused marketing canvas built around #010102 (the deepest dark surface of any tool in this collection), light gray text (#f7f8f8), and the signature Linear lavender-blue (#5e6ad2) used as the single chromatic accent. The system reads as software-craft documentation: dense, technical, and quietly luxurious. Display type is set in the Linear custom sans (SF Pro Display fallback) at 500–700 with measured negative tracking. Cards live as charcoal panels (#0f1011) with hairline borders. The accent lavender appears on the brand mark, focus rings, and a few intentional CTAs — never decoratively. Page rhythm leans on product UI screenshots framed in dark panels rather than atmospheric color."

colors:
  primary: "#5e6ad2"
  on-primary: "#ffffff"
  primary-hover: "#828fff"
  primary-focus: "#5e69d1"
  ink: "#f7f8f8"
  ink-muted: "#d0d6e0"
  ink-subtle: "#8a8f98"
  ink-tertiary: "#62666d"
  text-dim: "#d0d6e0"
  canvas: "#010102"
  surface: "#0f1011"
  surface-1: "#0f1011"
  surface-2: "#141516"
  surface-3: "#18191a"
  surface-4: "#191a1b"
  hairline: "#23252a"
  hairline-strong: "#34343a"
  hairline-tertiary: "#3e3e44"
  hairline-control: "#6a6e78"
  focus: "#dfe3fb"
  focus-on-light: "#5e6ad2"
  inverse-canvas: "#ffffff"
  inverse-surface-1: "#f5f6f6"
  inverse-surface-2: "#f6f7f7"
  inverse-ink: "#000000"
  brand-secure: "#7a7fad"
  semantic-success: "#27a644"
  semantic-overlay: "#000000"

typography:
  display-xl:
    fontFamily: Linear Display
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -3.0px
  display-lg:
    fontFamily: Linear Display
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.8px
  display-md:
    fontFamily: Linear Display
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1.0px
  headline:
    fontFamily: Linear Display
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.6px
  card-title:
    fontFamily: Linear Display
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.4px
  subhead:
    fontFamily: Linear Display
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: -0.2px
  body-lg:
    fontFamily: Linear Text
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.1px
  body:
    fontFamily: Linear Text
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.05px
  body-sm:
    fontFamily: Linear Text
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: Linear Text
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0
  button:
    fontFamily: Linear Text
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0
  eyebrow:
    fontFamily: Linear Text
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0.4px
  mono:
    fontFamily: Linear Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
  pill: 9999px
  full: 9999px

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

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-primary-pressed:
    backgroundColor: "{colors.primary-focus}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-inverse:
    backgroundColor: "{colors.inverse-canvas}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  pricing-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  pricing-card-featured:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  feature-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  product-screenshot-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 24px
  testimonial-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  customer-logo-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-subtle}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 16px
  text-input:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  text-input-focused:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  pricing-tab-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-subtle}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 14px
  pricing-tab-selected:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 14px
  cta-banner:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    rounded: "{rounded.lg}"
    padding: 48px
  changelog-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 24px 0
  status-badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 2px 8px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 56px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-subtle}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 32px
---

## Overview

Linear's marketing canvas is the deepest dark surface in this collection — `{colors.canvas}` is #010102, essentially pure black with a faint blue tint. On top sits a four-step surface ladder (`{colors.surface-1}` through `{colors.surface-4}`) for cards, panels, and lifted tiles, with hairline borders running from `{colors.hairline}` (#23252a) up through `{colors.hairline-strong}` and `{colors.hairline-tertiary}`. Light gray text (`{colors.ink}` #f7f8f8) carries the body and headlines.

The single chromatic accent is **Linear lavender-blue** `{colors.primary}` (#5e6ad2) — used on the brand mark, focus rings, and the primary CTA button. A lighter hover state (`{colors.primary-hover}` #828fff) and a focus-tinted variant (`{colors.primary-focus}` #5e69d1) extend the same hue. Linear avoids saturated greens, oranges, reds, etc. on the marketing canvas — the only semantic color is `{colors.semantic-success}` (#27a644) for status pills and the rare success indicator.

Display type runs Linear's custom sans (with `SF Pro Display` fallback) at weight 500–700 with negative letter-spacing scaling from -3.0px at 80px down to 0 at body. The body family is Linear's text cut, and a Linear Mono is reserved for code snippets in product screenshots.

The page rhythm is **dense product screenshots** — Linear's marketing leads with high-fidelity captures of the product UI (issue list, project view, dashboard) framed in `{colors.surface-1}` panels with `{rounded.xl}` 16px corners. The chrome is intentionally minimal so the app screenshots can do the heavy lifting.

**Key Characteristics:**
- **Dark-canvas marketing system** — `{colors.canvas}` (#010102) is the deepest dark in this collection.
- **Lavender-blue brand accent** (`{colors.primary}` #5e6ad2) — used scarcely on brand mark, focus, and the primary CTA.
- Four-step surface ladder (canvas → surface-1 → surface-2 → surface-3 → surface-4) carries hierarchy without shadow.
- Display tracking pulls aggressively negative (-3.0px at 80px); body holds at -0.05px.
- Cards use `{rounded.lg}` 12px corners with 1px hairline borders — never pill, rarely 16px.
- **Product UI screenshots** dominate the page. The marketing chrome is a dark frame for the app.
- No second chromatic color. No atmospheric gradients. No spotlight cards.

## Colors

> Source pages: linear.app (home), /intake, /pricing, /contact/sales, /build.

### Brand & Accent
- **Lavender-Blue** ({colors.primary}): The signature Linear accent — primary CTA, brand mark, link emphasis.
- **Lavender Hover** ({colors.primary-hover}): Lighter lavender (#828fff) — hovered state of the primary CTA.
- **Lavender Focus** ({colors.primary-focus}): Focus-ring tint (#5e69d1) — focused inputs, focused buttons.
- **Brand Secure** ({colors.brand-secure}): Muted lavender-gray (#7a7fad) — used in "Linear Security" surfaces.

### Surface
- **Canvas** ({colors.canvas}): Default page background — #010102, near-pure black with a faint blue tint.
- **Surface** ({colors.surface}): Role alias for the default card surface — the same #0f1011 as `{colors.surface-1}`. It exists so the canonical `surface` role resolves; author new work against `{colors.surface-1}`…`{colors.surface-4}` for the ladder, and against `{colors.surface}` only when you mean "whatever the default panel is".
- **Surface 1** ({colors.surface-1}): One step above canvas — feature cards, pricing cards, product screenshot panels.
- **Surface 2** ({colors.surface-2}): Two steps above — featured pricing card, hovered cards.
- **Surface 3** ({colors.surface-3}): Three steps above — line-tertiary backgrounds, sub-nav.
- **Surface 4** ({colors.surface-4}): Four steps above — bg-level-3, deepest lifted surface.
- **Hairline** ({colors.hairline}): 1px borders on cards and dividers.
- **Hairline Strong** ({colors.hairline-strong}): Stronger 1px borders — input focus rings.
- **Hairline Tertiary** ({colors.hairline-tertiary}): Tertiary borders for nested surfaces.
- **Hairline Control** ({colors.hairline-control}): **Prescribed, not extracted.** #6a6e78 — the accessible parallel to the three hairlines above, for any boundary that is the *only* thing defining an interactive control: text input edges, checkbox and radio outlines, segmented-control dividers. All three real Linear hairlines fail the 3:1 non-text contrast threshold on every surface in this file (measured in **Accessibility**), so they are scoped to decoration — card edges, section rules, table lines — where the surface lift already carries the boundary. The value sits inside Linear's own grey ramp, between `{colors.ink-tertiary}` #62666d and `{colors.ink-subtle}` #8a8f98, so it reads as the brand rather than as a borrowed grey.
- **Inverse Canvas** ({colors.inverse-canvas}): Pure white — surface of the inverse pill CTA on a small set of section openers.
- **Inverse Surface 1** ({colors.inverse-surface-1}): One step above inverse canvas.
- **Inverse Surface 2** ({colors.inverse-surface-2}): Two steps above inverse canvas.

### Text
- **Ink** ({colors.ink}): All headlines and emphasized body type — light gray #f7f8f8.
- **Ink Muted** ({colors.ink-muted}): Secondary type at #d0d6e0 — meta info on hero panels.
- **Text Dim** ({colors.text-dim}): Role alias for the secondary text tone — the same #d0d6e0 as `{colors.ink-muted}`. Present so the canonical `text-dim` role resolves to a value that clears 4.5:1 on the canvas and on all four surfaces; `{colors.ink-subtle}` and `{colors.ink-tertiary}` sit below it and are size-restricted (see **Accessibility**).
- **Ink Subtle** ({colors.ink-subtle}): Tertiary type at #8a8f98 — deselected pricing tabs, footer columns.
- **Ink Tertiary** ({colors.ink-tertiary}): Quaternary at #62666d — disabled, footnotes.

### Focus

- **Focus** ({colors.focus}): **Prescribed, not extracted.** #dfe3fb — a lavender-white ring, the brand hue pulled up to near-paper luminance. It is the one ring for the whole dark system: it clears 3:1 against the canvas, all four surfaces, *and* the lavender accent fill, which the extracted ring cannot do. Drawn as a 2px outline with a 2px `{colors.canvas}` offset so the ring never touches the control it marks.
- **Focus On Light** ({colors.focus-on-light}): **Prescribed, not extracted.** #5e6ad2 — the brand lavender itself, used as the ring on the white `{colors.inverse-canvas}` band and the two inverse surfaces, where `{colors.focus}` would sit at 1.27:1. Two rings are needed because this file documents both a near-black canvas and a pure-white inverse band; one ring cannot serve both.
- **Lavender Focus** ({colors.primary-focus}) is the ring Linear actually ships. It is kept as an extracted fact and is still correct on dark surfaces, but it measures 1.01:1 against the lavender CTA it is drawn around — which is why the prescribed pair above exists. See **Accessibility**.

### Semantic
- **Success Green** ({colors.semantic-success}): Status pills, success indicators. The only semantic color on marketing.
- **Overlay** ({colors.semantic-overlay}): Pure black overlay scrim for modals.

## Typography

### Font Family

- **Linear Display** — Linear's custom display sans; fallback `SF Pro Display, -apple-system, system-ui, Segoe UI, Roboto`. Carries display-xl through subhead.
- **Linear Text** — Linear's custom text sans (a slightly different cut tuned for body sizes); same fallback stack. Carries body sizes, button labels, captions.
- **Linear Mono** — Linear's custom mono; fallback `ui-monospace, SF Mono, Menlo`. Used for code snippets in product screenshots and for status / ID tokens.

The marketing surface treats Display and Text as one continuous voice; the family change is silent.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 80px | 600 | 1.05 | -3.0px | Largest hero headline |
| `{typography.display-lg}` | 56px | 600 | 1.10 | -1.8px | Section opener headlines |
| `{typography.display-md}` | 40px | 600 | 1.15 | -1.0px | Sub-section headlines |
| `{typography.headline}` | 28px | 600 | 1.20 | -0.6px | Pricing tier titles, CTA banner heading |
| `{typography.card-title}` | 22px | 500 | 1.25 | -0.4px | Feature card title |
| `{typography.subhead}` | 20px | 400 | 1.40 | -0.2px | Lead body, intro paragraphs |
| `{typography.body-lg}` | 18px | 400 | 1.50 | -0.1px | Hero subhead, lead paragraphs |
| `{typography.body}` | 16px | 400 | 1.50 | -0.05px | Default body |
| `{typography.body-sm}` | 14px | 400 | 1.50 | 0 | Card body, footer columns |
| `{typography.caption}` | 12px | 400 | 1.40 | 0 | Captions, meta, status |
| `{typography.button}` | 14px | 500 | 1.20 | 0 | All button labels |
| `{typography.eyebrow}` | 13px | 500 | 1.30 | 0.4px | Section eyebrow (slight positive tracking) |
| `{typography.mono}` | 13px | 400 | 1.50 | 0 | Linear Mono for code in product screenshots |

### Principles

- **Aggressive negative tracking on display** (-3.0px at 80px ≈ 4% of size).
- **Single voice from display to body.** Display-xl at 600 → body at 400 — same family, narrower weights.
- **Eyebrow uses positive tracking** (+0.4px) — contrast against the negative-tracked display marks the eyebrow as taxonomy.
- **Mono only in code contexts.** Linear Mono lives inside product screenshots — not on marketing chrome.

### Note on Font Substitutes

Linear's custom typeface isn't publicly distributed; the documented fallback `SF Pro Display, -apple-system, system-ui` is the recommended substitute on macOS. For cross-platform implementation, **Inter** at weight 500 / 600 / 700 is the closest free substitute. **Geist Sans** is also viable. For mono, **JetBrains Mono** or **Geist Mono** at weight 400 closely approximates Linear Mono.

## Layout

### Spacing System

- **Base unit**: 4px.
- **Tokens (front matter)**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- Card interior padding: `{spacing.lg}` 24px on feature/pricing cards; `{spacing.xl}` 32px on testimonial cards; `{spacing.xxl}` 48px on CTA banners.
- Pill button padding: 8px vertical · 14px horizontal — Linear's compact button spec.
- Form input padding: 8px vertical · 12px horizontal.

### Grid & Container

- Max content width sits around 1280px.
- Card grids are 3-up at desktop, 2-up at tablet, 1-up at mobile.
- Pricing tier grid is 3-up; comparison strip below shows checkmarks per tier.
- Product screenshot panels span full content width — they're the protagonist.

### Whitespace Philosophy

The dark canvas IS the whitespace. Sections separate by lift onto surface-1 panels, not by gaps in white. Within a panel, generous `{spacing.lg}` 24px gaps between content blocks; `{spacing.section}` 96px between sections.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Default for body type, hero text, footer |
| 1 (charcoal lift) | `{colors.surface-1}` background on canvas, 1px `{colors.hairline}` | Default cards, product panels |
| 2 (surface-2 lift) | `{colors.surface-2}` background, 1px `{colors.hairline-strong}` | Featured pricing card, hovered cards |
| 3 (surface-3 lift) | `{colors.surface-3}` background | Sub-nav, dropdown menus |
| 4 (focus ring) | 2px `{colors.focus}` outline + 2px `{colors.canvas}` offset | Focused input, focused button, focused card (prescribed) |
| 4-inverse (focus ring) | 2px `{colors.focus-on-light}` outline + 2px `{colors.inverse-canvas}` offset | Focus on the white inverse band (prescribed) |

Linear's depth is carried by surface ladder + hairline borders. The brand resists drop shadows on dark almost entirely — elevation here is expressed one way only, as background step plus 1px hairline, and never as a shadow. There is no `shadow:` token group because the file documents no shadow value.

**The ladder is tonal, not contrast-bearing.** Measured: canvas → `{colors.surface-1}` is 1.10:1, surface-1 → surface-2 is 1.04:1, surface-2 → surface-3 is 1.04:1, surface-3 → surface-4 is 1.01:1, and canvas → surface-4 is only 1.20:1. Levels 1–4 are therefore not reliably distinguishable from each other, and barely distinguishable from the canvas, on their own. That is a deliberate property of Linear's near-black system, not an error in the extraction — but it means the hairline border, not the fill step, is what actually draws the edge of a panel, and anything whose boundary must be *perceivable* needs `{colors.hairline-control}` rather than a surface step. Do not rely on a single level change to signal state.

### Decorative Depth

- **Product UI screenshots** dominate as decorative depth.
- **No atmospheric gradients, no spotlight cards.**
- **Subtle white edge highlight** on the top edge of lifted panels — gives the dark surface a faint "pixel rendered" feel.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Small chips, status badges |
| `{rounded.sm}` | 6px | Inline tags |
| `{rounded.md}` | 8px | All buttons, form inputs |
| `{rounded.lg}` | 12px | Pricing cards, feature cards, testimonial cards |
| `{rounded.xl}` | 16px | Product screenshot panels |
| `{rounded.xxl}` | 24px | Oversized CTA banners (rare) |
| `{rounded.pill}` | 9999px | Pricing tab toggles, status pills |
| `{rounded.full}` | 9999px | Avatar circles |

### Border Widths

Linear uses one border width. Every rule, divider and control edge in this file is **1px**; the only 2px stroke is the focus ring, and it is an `outline`, not a border, so it never shifts layout. There is no 3px or 4px step — if a boundary needs more emphasis, change the tone (`{colors.hairline}` → `{colors.hairline-control}`), not the width. The focus ring inherits the radius of the element it marks, so a `{rounded.md}` button gets an 8px ring and a `{rounded.pill}` tab gets a pill ring; the 2px offset means the ring's own outer radius reads 2px larger.

### Photography & Illustration Geometry

- Product UI screenshots dominate; they sit in `{rounded.xl}` 16px tiles with `{spacing.lg}` 24px outer padding.
- Customer logo tiles render at small sizes (~24px logo height) on `{colors.canvas}` with no border.
- Avatar circles in testimonial cards use `{rounded.full}` at 32–40px sizes.

## Components

### Buttons

**`button-primary`** — Lavender CTA. The default primary CTA across all pages.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}`, padding 8px 14px, rounded `{rounded.md}`.
- Pressed state lives in `button-primary-pressed` (background shifts to `{colors.primary-focus}`).
- Hover state lives in `button-primary-hover` (background shifts to `{colors.primary-hover}` lighter lavender).
- States — default · hover (`button-primary-hover`) · focus-visible (2px `{colors.focus}` ring, 2px `{colors.canvas}` offset) · active/pressed (`button-primary-pressed`) · disabled (background `{colors.surface-2}`, text `{colors.ink-tertiary}`, no hover) · loading (label holds its width, a 14px `{colors.on-primary}` spinner replaces the icon slot; see **Motion & Animation**) · error — none, the button does not carry error state. Hover, pressed and the two background hexes are extracted; focus-visible, disabled and loading are prescribed.

**`button-secondary`** — Charcoal button. Used for secondary CTAs ("Sign in", "Read changelog").
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.button}`, padding 8px 14px, rounded `{rounded.md}`. 1px `{colors.hairline-control}` border — this is the control case, so it takes the accessible boundary, not the decorative `{colors.hairline}`.
- States — default · hover (surface steps to `{colors.surface-2}`) · focus-visible (2px `{colors.focus}` ring, 2px `{colors.canvas}` offset) · active/pressed (surface holds at `{colors.surface-2}`, border to `{colors.hairline-tertiary}`) · disabled (text `{colors.ink-tertiary}`, border `{colors.hairline}`) · loading (as `button-primary`, spinner in `{colors.ink-subtle}`) · no selected or error state.

**`button-tertiary`** — Plain text button.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.button}`, rounded `{rounded.md}`, padding 8px 14px.
- States — default · hover (background to `{colors.surface-1}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed (text to `{colors.ink-muted}`) · disabled (text `{colors.ink-tertiary}`) · no loading, selected or error state.

**`button-inverse`** — White-on-dark inverse CTA.
- Background `{colors.inverse-canvas}`, text `{colors.inverse-ink}`, type `{typography.button}`, rounded `{rounded.md}`, padding 8px 14px.
- States — default · hover (background to `{colors.inverse-surface-1}`) · focus-visible (2px `{colors.focus-on-light}` ring, 2px `{colors.inverse-canvas}` offset — the white-surface ring, not `{colors.focus}`) · active/pressed (background to `{colors.inverse-surface-2}`) · disabled (text `{colors.ink-tertiary}`) · no loading, selected or error state.

### Pricing Tabs

**`pricing-tab-default`** + **`pricing-tab-selected`** — Pill-toggle on `/pricing`.
- Default: `{colors.canvas}` background, `{colors.ink-subtle}` text, rounded `{rounded.pill}`, padding 6px 14px.
- Selected: `{colors.surface-2}` background, `{colors.ink}` text — selected = surface lift.
- States — default · hover (text to `{colors.ink-muted}`) · focus-visible (2px `{colors.focus}` ring at `{rounded.pill}`) · active/pressed (same as selected) · selected (`pricing-tab-selected`) · disabled (text `{colors.ink-tertiary}`) · no loading or error state. Because canvas → surface-2 measures 1.14:1, selection must **also** carry `{colors.ink}` text; the fill step alone is not a perceivable selected state.

### Cards & Containers

**`pricing-card`** — Each tier on `/pricing`.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 24px. 1px `{colors.hairline}` border.

- States — default · hover (surface steps to `{colors.surface-2}`) · focus-visible (2px `{colors.focus}` ring on the card's CTA, not on the card) · selected (`pricing-card-featured`) · no active, disabled, loading or error state.

**`pricing-card-featured`** — Recommended tier — surface lift to surface-2.
- Background `{colors.surface-2}`, otherwise identical structure.
- States — this is the selected variant of `pricing-card` and has the same state set; the lift to `{colors.surface-2}` is 1.04:1 against surface-1, so the featured tier must additionally carry a 1px `{colors.hairline-control}` border or a `{colors.primary}` badge to be seen.

**`feature-card`** — Generic feature highlight tile.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 24px.
- States — genuinely two: default and hover (surface steps to `{colors.surface-2}`). It is not interactive on its own, so it has no focus-visible, active, disabled, loading, selected or error state; where the whole tile is a link, it takes `button-tertiary`'s focus-visible ring.

**`product-screenshot-card`** — The dominant card type — frames a high-fidelity Linear app UI screenshot.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.xl}`, padding 24px.
- States — genuinely two: default and loading (the screenshot slot holds its aspect ratio and fades in at `{motion.duration-base}`; no skeleton shimmer). No hover, focus-visible, active, disabled, selected or error state.

**`testimonial-card`** — Customer quote with avatar + name + role.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body-lg}`, rounded `{rounded.lg}`, padding 32px.
- States — static. Default only; no hover, focus-visible, active, disabled, loading, selected or error state.

**`customer-logo-tile`** — Small tile in the customer marquee.
- Background `{colors.canvas}`, text `{colors.ink-subtle}`, type `{typography.caption}`, rounded `{rounded.xs}`, padding 16px.
- States — genuinely two: default and hover (logo opacity 0.6 → 1.0). No focus-visible, active, disabled, loading, selected or error state unless the tile links out, in which case it takes the `{colors.focus}` ring.

**`cta-banner`** — Closing CTA panel near page bottom.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.headline}`, rounded `{rounded.lg}`, padding 48px.
- States — static container. Default only; every state lives on the `button-primary` inside it.

### Inputs & Forms

**`text-input`** + **`text-input-focused`** — Form fields on `/contact/sales` and signup overlays.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.md}`, padding 8px 12px. Resting boundary is 1px `{colors.hairline-control}` — the input's edge is the only thing that marks the field, and surface-1 sits at 1.10:1 on the canvas, so the decorative hairlines cannot carry it.
- Focused state retains the same surface; Linear's shipped ring is a 2px `{colors.primary-focus}` outline at 50% opacity. **Prescribed replacement:** a 2px `{colors.focus}` outline at full opacity with a 2px `{colors.canvas}` offset, because the shipped ring at 50% opacity over `{colors.surface-1}` is not measurable as a 3:1 indicator and the same token fails entirely when drawn around the lavender CTA.
- States — default · hover (border to `{colors.ink-tertiary}`) · focus-visible (`text-input-focused`, ring as above) · active — same as focus-visible, a text field has no separate pressed state · disabled (background `{colors.surface-2}`, text and border `{colors.ink-tertiary}`) · loading (field is read-only, trailing spinner in `{colors.ink-subtle}`) · error (**unspecified** — the inspected pages show no validation styling and the palette ships no error tone, so this state is left open rather than filled with an invented red; see **Known Gaps**) · no selected state.

### Status & Build Page

**`changelog-row`** — Each row in `/build` (changelog page) listing version, date, and changes.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.xs}`, padding 24px 0. 1px `{colors.hairline}` bottom rule — decorative here, since the row is separated by `{spacing.lg}` 24px of space as well as by the rule.
- States — default · hover (background to `{colors.surface-1}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed (no change; navigation is instant) · no disabled, loading, selected or error state.

**`status-badge`** — Small status pill.
- Background `{colors.surface-2}`, text `{colors.ink-muted}`, type `{typography.caption}`, rounded `{rounded.pill}`, padding 2px 8px.
- States — static. Default only. The badge is an output, not a control: no hover, focus-visible, active, disabled, loading, selected or error state. Its *value* may be success (`{colors.semantic-success}` dot), but that is content, not a UI state.

### Navigation

**`top-nav`** — Sticky dark bar with the Linear wordmark left, primary nav links centered, and a `button-secondary` ("Sign in") + `button-primary` ("Get started") pair right.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-sm}`, height 56px.
- States — the bar itself is static; its links carry default · hover (text `{colors.ink}` → `{colors.ink-muted}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed (no travel) · selected (current section marked by `{colors.ink}` against `{colors.ink-subtle}` siblings, never by an underline alone) · no disabled, loading or error state.

### Footer

**`footer`** — Dense link grid on `{colors.canvas}` with the Linear wordmark left.
- Background `{colors.canvas}`, text `{colors.ink-subtle}`, type `{typography.caption}`, padding 64px 32px.
- States — container static; footer links carry default · hover (text to `{colors.ink}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed (no change) · no disabled, loading, selected or error state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted from linear.app; they are the **Crisp** profile's shared values, chosen because Linear's identity is a developer tool — issue tracker chrome, keyboard-first product UI, dense screenshots — and the Crisp signature is that a state change reads as instant with no entrance choreography. Treat every value here as a specification to build to, not as a record of what Linear ships.

### Tokens

`{motion.duration-instant}` 60ms · `{motion.duration-fast}` 100ms · `{motion.duration-base}` 150ms · `{motion.duration-slow}` 220ms · `{motion.duration-emphasis}` 300ms · `{motion.ease-standard}` · `{motion.ease-enter}` · `{motion.ease-exit}` · `{motion.stagger-step}` 20ms · `{motion.duration-reduced}` 100ms.

### Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, nav link, logo tile) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`, and `background-color` as a discrete cross-fade — no `transform` | Unchanged; already opacity/colour only and under 150ms |
| Press / active | `{motion.duration-instant}` | `{motion.ease-exit}` | `transform: scale(0.99)` | Scale removed; the pressed background change remains, instant |
| Focus-visible ring | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` on the ring only — the ring's geometry never animates | Ring appears with no transition |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` 0 → 1 on the incoming view; no travel, no cross-fade of the outgoing view | Opacity fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px) → 0`; scrim `{colors.semantic-overlay}` fades `opacity` 0 → 0.6 | Travel removed; scrim and panel fade at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform` reversed — shorter than its entrance | Opacity fade at `{motion.duration-reduced}` |
| Dropdown / sub-nav enter | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` + `transform: scale(0.98) → 1`, origin at the trigger edge | Scale removed; opacity only at `{motion.duration-reduced}` |
| Dropdown / sub-nav exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` only | Unchanged |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px) → 0` | Travel removed; opacity at `{motion.duration-reduced}` |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: translateY(0 → 4px)` | Opacity only at `{motion.duration-reduced}` |
| List enter (pricing tiers, changelog rows, feature grid) | `{motion.duration-fast}` per item, `{motion.stagger-step}` 20ms between items, 6 items maximum then the rest appear together | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px) → 0` | Stagger and travel removed; the whole list fades together at `{motion.duration-reduced}` |
| List exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity`; no stagger, no travel | Unchanged |
| Loading (button spinner, screenshot slot) | spinner: 600ms per rotation, infinite — a loader, the one permitted infinite animation; screenshot fade-in: `{motion.duration-base}` | spinner: linear; fade: `{motion.ease-enter}` | spinner `transform: rotate()`; slot `opacity` 0 → 1 | Spinner is replaced by a static three-dot glyph whose `opacity` pulses at `{motion.duration-reduced}`, or by a text label; the slot fade stays at `{motion.duration-reduced}` |

### Rules

- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin` — a near-black surface shows reflow as a visible jolt, and the focus ring is an `outline` precisely so it costs no layout.
- Every exit is shorter than its matching entrance: modal 100ms out against 150ms in, dropdown 60ms out against 100ms in, toast 100ms out against 150ms in, list 60ms out against 100ms in.
- Nothing animates on first paint in a way that delays content. Hero type and the hero product screenshot render at their final position and opacity; the list stagger applies only to content that enters after the first paint.
- No infinite animation except the loading spinner above. Linear has **no brand ambience** on this canvas — no drifting gradient, no breathing glow, no marquee that never stops. The customer logo marquee, if it scrolls, scrolls on user intent or pauses on hover and is not treated as ambience.
- Travel distances stay small — 4px to 8px. Crisp means the state change is the message; the journey is not.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and all scale, on every interaction above.
     Removed: the list stagger — lists appear as one block.
     Removed: the rotating spinner, replaced by a pulsing or static indicator.
     Frozen:  the logo marquee, which does not auto-scroll at all.
     Kept:    opacity fades only, clamped to 100ms ({motion.duration-reduced}).
     Kept:    every colour and background state change, instant.
     Kept:    the focus ring, which appears with no transition. */
  *, *::before, *::after {
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;
    transition-property: opacity, background-color, border-color, color !important;
  }
}
```

Nothing in this file is conveyed by motion alone: every animated state above also changes a colour, a surface or a ring, so a reader with motion suppressed loses no information.

## Accessibility

Every ratio below was computed from this file's own hexes with the WCAG 2.1 relative-luminance formula. Nothing here was measured on a rendered page: overlap, clipping, frame rate, layout shift and real tap-target size are **not** verifiable from a document, so no claim is made about them.

### Key text pairs

| Foreground | Background | Ratio | Required | Verdict |
|---|---|---|---|---|
| `{colors.ink}` #f7f8f8 | `{colors.canvas}` #010102 | 19.61:1 | 4.5:1 | Pass |
| `{colors.ink}` #f7f8f8 | `{colors.surface}` / surface-1 #0f1011 | 17.90:1 | 4.5:1 | Pass |
| `{colors.ink}` #f7f8f8 | `{colors.surface-4}` #191a1b | 16.38:1 | 4.5:1 | Pass |
| `{colors.text-dim}` / `{colors.ink-muted}` #d0d6e0 | `{colors.canvas}` #010102 | 14.28:1 | 4.5:1 | Pass |
| `{colors.text-dim}` / `{colors.ink-muted}` #d0d6e0 | `{colors.surface-4}` #191a1b | 11.93:1 | 4.5:1 | Pass |
| `{colors.ink-subtle}` #8a8f98 | `{colors.canvas}` #010102 | 6.42:1 | 4.5:1 | Pass |
| `{colors.ink-subtle}` #8a8f98 | `{colors.surface-4}` #191a1b | 5.36:1 | 4.5:1 | Pass |
| `{colors.on-primary}` #ffffff | `{colors.primary}` #5e6ad2 | 4.70:1 | 4.5:1 | Pass |
| `{colors.on-primary}` #ffffff | `{colors.primary-focus}` #5e69d1 | 4.75:1 | 4.5:1 | Pass |
| `{colors.inverse-ink}` #000000 | `{colors.inverse-canvas}` #ffffff | 21.00:1 | 4.5:1 | Pass |
| `{colors.semantic-success}` #27a644 | `{colors.canvas}` #010102 | 6.58:1 | 4.5:1 | Pass |
| `{colors.brand-secure}` #7a7fad | `{colors.canvas}` #010102 | 5.43:1 | 4.5:1 | Pass |
| `{colors.primary}` #5e6ad2 as link ink | `{colors.canvas}` #010102 | 4.44:1 | 4.5:1 | **Fail by 0.06** — see below |

### Where the real brand fails AA

These are extracted Linear values. They are frozen: the hexes are facts about the brand and are not adjusted to make a ratio pass. Each failure is named with its measured ratio and the usage note that makes the value defensible.

| Foreground | Background | Measured | Required | Note |
|---|---|---|---|---|
| `{colors.ink-tertiary}` #62666d | `{colors.canvas}` #010102 | 3.62:1 | 4.5:1 | **Fails AA for body text.** Restrict to 18.66px+ at weight 700 or 24px+, where 3:1 applies, or to genuinely disabled text, which WCAG exempts. The file's own use — "disabled, footnotes" — means a 12px footnote in this tone is a real AA failure. |
| `{colors.ink-tertiary}` #62666d | `{colors.surface}` / surface-1 #0f1011 | 3.30:1 | 4.5:1 | Same restriction, and it is worse on every lift: 3.17:1 on surface-2, 3.05:1 on surface-3, 3.02:1 on surface-4. At surface-4 it is 0.02 above even the large-text floor. |
| `{colors.hairline}` #23252a | `{colors.canvas}` #010102 | 1.36:1 | 3.0:1 | **Fails 1.4.11 by a wide margin.** Decorative only: card edges, section rules, table lines, the changelog bottom rule. Never the sole boundary of a control. |
| `{colors.hairline}` #23252a | `{colors.surface}` / surface-1 #0f1011 | 1.24:1 | 3.0:1 | Same; worse on a lift than on the canvas. |
| `{colors.hairline-strong}` #34343a | `{colors.canvas}` #010102 | 1.69:1 | 3.0:1 | The file calls this "input focus rings" — it cannot serve that job. Use `{colors.focus}` for focus and `{colors.hairline-control}` for a resting control edge. |
| `{colors.hairline-strong}` #34343a | `{colors.surface}` / surface-1 #0f1011 | 1.54:1 | 3.0:1 | Same. |
| `{colors.hairline-tertiary}` #3e3e44 | `{colors.canvas}` #010102 | 1.96:1 | 3.0:1 | The strongest hairline Linear ships, and still a third short of the threshold. Decorative only. |
| `{colors.hairline-tertiary}` #3e3e44 | `{colors.surface}` / surface-1 #0f1011 | 1.79:1 | 3.0:1 | Same. |
| `{colors.on-primary}` #ffffff | `{colors.primary-hover}` #828fff | 2.87:1 | 4.5:1 | `button-primary-hover` **fails AA while hovered**, having passed at 4.70:1 at rest. The hover lightening is an extracted fact. Defensible only if the label is 18.66px+ at weight 700, which `{typography.button}` at 14px/500 is not. See **Needs approval** in the audit report. |
| `{colors.semantic-overlay}` #000000 | `{colors.canvas}` #010102 | 1.01:1 | 4.5:1 | Not a defect. This token is a modal scrim fill used at partial opacity, never text and never an interactive boundary, so 1.4.3 and 1.4.11 do not apply to it. It is recorded here because the harness measures every semantic tone as if it were text. |
| `{colors.primary}` #5e6ad2 | `{colors.canvas}` #010102 | 4.44:1 | 4.5:1 | 0.06 short for body-size link text. The lavender is the brand and is not altered. Use `{colors.ink}` with a `{colors.primary}` underline for inline links at `{typography.body}` and below, and reserve lavender ink for 24px+ emphasis. |
| `{colors.primary-focus}` #5e69d1 as a ring on the lavender CTA | `{colors.primary}` #5e6ad2 | 1.01:1 | 3.0:1 | The shipped ring is invisible on the button it most needs to mark, and at the documented 50% opacity it is weaker still on every dark surface. This is the reason `{colors.focus}` exists. |

### Focus ring visibility, surface by surface

`{colors.focus}` #dfe3fb, 2px outline with a 2px offset, measured against every surface this file defines that it can be drawn over:

| Surface | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.canvas}` #010102 | 16.41:1 | 3.0:1 | Pass |
| `{colors.surface}` / `{colors.surface-1}` #0f1011 | 14.98:1 | 3.0:1 | Pass |
| `{colors.surface-2}` #141516 | 14.38:1 | 3.0:1 | Pass |
| `{colors.surface-3}` #18191a | 13.85:1 | 3.0:1 | Pass |
| `{colors.surface-4}` #191a1b | 13.71:1 | 3.0:1 | Pass |
| `{colors.primary}` #5e6ad2 (the CTA fill) | 3.70:1 | 3.0:1 | Pass |
| `{colors.inverse-canvas}` #ffffff | 1.27:1 | 3.0:1 | **Fail — never use `{colors.focus}` here** |

On the white inverse band, `{colors.focus-on-light}` #5e6ad2 is used instead: 4.70:1 on `{colors.inverse-canvas}` #ffffff, 4.34:1 on `{colors.inverse-surface-1}` #f5f6f6, 4.38:1 on `{colors.inverse-surface-2}` #f6f7f7 — all above 3:1. Two rings are required because this file documents both a near-black canvas and a pure-white band; one ring cannot clear 3:1 on both.

Resting control boundaries use `{colors.hairline-control}` #6a6e78: 4.09:1 on `{colors.canvas}`, 3.73:1 on surface-1, 3.58:1 on surface-2, 3.45:1 on surface-3, 3.41:1 on surface-4 — above 3:1 everywhere.

### Minimum tap target

Specified, not measured — a document cannot verify a rendered hit box.

- Target: 44 × 44 CSS px for every control on touch, per WCAG 2.5.5 AAA; 24 × 24 px is the 2.5.8 AA floor and nothing in this file may fall below it.
- `button-primary` and friends at 14px/1.20 type plus 8px vertical padding compute to roughly 33px of visual height, so they need an invisible expansion to 44px on touch. The existing "CTAs hold ≥40px tap height" line in **Responsive Behavior** is 4px short of 2.5.5 and is listed as a gap.
- `pricing-tab-default` at 6px vertical padding is smaller still and must grow to ≥44px on touch, as **Responsive Behavior** already states.
- `status-badge` at 2px padding is not a control and is exempt.

### Reduced motion

Honoured in full — see the `@media (prefers-reduced-motion: reduce)` block in **Motion & Animation**. All travel and scale are removed, the list stagger is removed, the spinner stops rotating, and opacity fades are clamped to `{motion.duration-reduced}` 100ms. No information in this system is carried by motion alone.

### Other accessibility notes

- Contrast is the only automatically verifiable dimension here. Keyboard order, heading structure, landmark regions, alt text on the product screenshots and screen-reader labelling cannot be checked from a token document and are untested.
- The four-step surface ladder separates by 1.01:1 to 1.04:1 between adjacent levels (see **Elevation & Depth**). Never use a level change as the only signal of selection or state; pair it with text tone, a `{colors.hairline-control}` border, or a `{colors.primary}` marker.
- Linear ships no light marketing theme, so there is no light-mode contrast set to audit beyond the inverse band documented above.

## Do's and Don'ts

### Do

- Reserve `{colors.canvas}` (#010102) as the system's anchor surface — the faint blue tint is intentional.
- Use `{colors.primary}` lavender ONLY for: brand mark, primary CTA, focus ring, link emphasis.
- Use the four-step surface ladder for hierarchy. Avoid skipping levels.
- Pair display weight 600 with body weight 400 — Linear resists 700+ display weights.
- Apply negative letter-spacing aggressively on display.
- Use product UI screenshots as the protagonist of every section.
- Compose CTAs as `{rounded.md}` 8px corners.
- Keep state changes at `{motion.duration-instant}` to `{motion.duration-base}` — Crisp means the change reads as already done.
- Draw focus with `{colors.focus}` on dark and `{colors.focus-on-light}` on the inverse band, always with a 2px offset.
- Give any control whose edge is its only boundary a `{colors.hairline-control}` border.

### Don't

- Don't ship a light-mode marketing page.
- Don't use lavender as a section background or card fill.
- Don't introduce a second chromatic accent (orange, pink, green for marketing).
- Don't add atmospheric gradients or spotlight cards.
- Don't pill-round CTAs.
- Don't use `#000000` true black as the canvas.
- Don't combine multiple bright accents in product screenshot mockups.
- Don't use a hairline as the only boundary of an input, checkbox or segmented control — all three fail 3:1.
- Don't rely on a single surface step to signal selection; adjacent levels sit at 1.01:1 to 1.04:1.
- Don't add entrance choreography, scroll-driven reveals, parallax or ambient looping motion. There is no brand ambience on this canvas.
- Don't animate `width`, `height`, `top`, `left` or `margin`.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop-XL | 1440px | Default desktop layout |
| Desktop | 1280px | Card grid 3-up maintained |
| Tablet | 1024px | Card grid 3-up → 2-up |
| Mobile-Lg | 768px | Pricing comparison becomes accordion; nav hamburger |
| Mobile | 480px | Single-column; display-xl scales 80px → ~36px |

### Touch Targets

- CTAs hold ≥40px tap height across viewports.
- Pricing tab pills hold ≥36px tap height; touch viewports grow to ≥44px.
- Form inputs hold ≥44px tap target on touch.

### Collapsing Strategy

- **Top nav**: links collapse to hamburger below 768px.
- **Card grids**: 3-up → 2-up at 1024px → 1-up below 768px.
- **Pricing comparison**: per-tier accordion below 768px.
- **Display type**: `{typography.display-xl}` 80px scales toward `{typography.display-md}` 40px on mobile.

### Image Behavior

- Product UI screenshots maintain aspect ratio and never crop.
- Customer logos in the marquee may collapse from 6-up to 3-up below 768px.

## Iteration Guide

1. Focus on ONE component at a time and reference it by its `components:` token name.
2. When introducing a section, decide first which surface lift it lives on.
3. Default body to `{typography.body}` at weight 400.
4. Run `npx @google/design.md lint DESIGN.md` after edits.
5. Add new variants as separate component entries.
6. Treat lavender as scarce: brand mark, primary CTA, focus, link emphasis.
7. Lead every section with a product UI screenshot.

## Known Gaps

- The four-step surface ladder values are extracted directly from Linear's `--color-bg-level-3`, `--color-line-tint`, etc. CSS variables; they are Linear's canonical surface spec.
- Form-field error and validation styling is not visible on the inspected pages.
- Light mode is not documented because the marketing site does not ship a light theme.
- Linear's actual product UI uses a richer color-tag palette (red, orange, yellow, green, blue, purple) for issue priorities and project labels — those colors live in the in-product surfaces shown in mockups.
- The custom display, text, and mono families are proprietary; an open-source substitute is acceptable.
- **The whole Motion & Animation section is prescribed, not extracted.** No duration, easing curve or stagger was measured from linear.app; the values are the shared **Crisp** profile, and any of them may differ from what Linear ships.
- `{colors.focus}`, `{colors.focus-on-light}` and `{colors.hairline-control}` are prescribed, not extracted. Linear's own ring is `{colors.primary-focus}` at 50% opacity, which fails the 3:1 non-text threshold on the lavender CTA (1.01:1). The three prescribed tokens are the minimum needed to make focus and control boundaries perceivable without altering a single extracted hex.
- `{colors.surface}` and `{colors.text-dim}` are role aliases of `{colors.surface-1}` and `{colors.ink-muted}` with identical hexes, added so the canonical token roles resolve. They introduce no new colour.
- The "CTAs hold ≥40px tap height" figure in **Responsive Behavior** is 4px below WCAG 2.5.5's 44px target. It is kept as written because it is what the pages show; treat 44px as the implementation target.
- Tap-target size, overlap, clipping, frame rate and layout shift cannot be verified from a document. Nothing in **Accessibility** claims them as measured.
- `{colors.surface-3}` and `{colors.surface-4}` are 1.01:1 apart. They are extracted as distinct CSS variables but are not visually distinguishable, so the four-step ladder is effectively a two- or three-step ladder in practice.
