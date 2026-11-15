---
version: alpha
name: Intercom-design-analysis
description: "An editorial customer-service marketing canvas built around a soft cream-white ground, charcoal type set in Saans (Intercom's proprietary geometric sans), and a single confident Fin Orange (#ff5600) reserved for the Fin AI brand. Cards live as floating white tiles with thin hairline borders and minimal radii (8–16px). Display headlines run Saans at weight 500 with measured negative tracking. The system reads as a careful, product-led publication: product screenshots dominate, ornament is rare, and the only place chromatic energy enters is the Fin Orange CTA."

colors:
  primary: "#111111"
  on-primary: "#ffffff"
  ink: "#111111"
  ink-muted: "#626260"
  ink-subtle: "#7b7b78"
  ink-tertiary: "#9c9fa5"
  canvas: "#f5f1ec"
  surface: "#ffffff"
  surface-1: "#ffffff"
  surface-2: "#ebe7e1"
  text-dim: "#626260"
  inverse-canvas: "#000000"
  inverse-surface-1: "#313130"
  inverse-ink: "#ffffff"
  inverse-ink-muted: "#9c9fa5"
  hairline: "#d3cec6"
  hairline-soft: "#ebe7e1"
  hairline-strong: "#857f75"
  focus: "#0007cb"
  focus-on-dark: "#65b5ff"
  fin-orange: "#ff5600"
  report-orange: "#fe4c02"
  report-blue: "#65b5ff"
  report-green: "#0bdf50"
  report-pink: "#ff2067"
  report-lime: "#b3e01c"
  report-cyan: "#03b2cb"
  brand-blue: "#0007cb"
  semantic-error: "#c41c1c"
  semantic-success: "#0bdf50"

typography:
  display-xl:
    fontFamily: Saans
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -2.0px
  display-lg:
    fontFamily: Saans
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.10
    letterSpacing: -1.4px
  display-md:
    fontFamily: Saans
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.8px
  headline:
    fontFamily: Saans
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.5px
  card-title:
    fontFamily: Saans
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  subhead:
    fontFamily: Saans
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: -0.2px
  body-lg:
    fontFamily: Saans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.1px
  body:
    fontFamily: Saans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: Saans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: Saans
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0
  button:
    fontFamily: Saans
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0
  eyebrow:
    fontFamily: Saans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0
  mono:
    fontFamily: SaansMono
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
  duration-instant: 70ms
  duration-fast: 130ms
  duration-base: 200ms
  duration-slow: 320ms
  duration-emphasis: 450ms
  ease-standard: cubic-bezier(0.3, 0, 0.2, 1)
  ease-enter: cubic-bezier(0.17, 0.89, 0.32, 1.28)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 60ms
  duration-reduced: 130ms

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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  button-primary-pressed:
    backgroundColor: "{colors.inverse-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  button-fin:
    backgroundColor: "{colors.fin-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  pricing-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  pricing-card-featured:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  feature-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  product-mockup-card:
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
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 16px
  text-input:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px 14px
  text-input-focused:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px 14px
  pricing-tab-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  pricing-tab-selected:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  faq-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  cta-banner:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    rounded: "{rounded.lg}"
    padding: 48px
  startup-discount-card:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 32px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 56px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 32px
---

## Overview

Intercom's marketing canvas is a soft cream-white ground (`{colors.canvas}` ≈ #f5f1ec) — not pure white. The warmth is the brand's signal: this is editorial, calm, and product-focused, not bright SaaS. On top of the cream canvas sit white floating cards (`{colors.surface-1}`), thin hairline dividers (`{colors.hairline}`), and charcoal type (`{colors.ink}` #111111).

Display type is **Saans** — Intercom's proprietary geometric sans — set at weight 500 with measured negative letter-spacing (-2.0px on 72px display). Body type is the same family at weight 400. The single proprietary mono is **SaansMono**, used sparingly for code snippets and product UI screenshots embedded in the marketing surface.

The single chromatic accent is **Fin Orange** (`{colors.fin-orange}` #ff5600) — Intercom's AI-product brand color. It surfaces on the Fin product CTA, the Fin badge in pricing, and a few inline emphasis moments. It is NOT a system primary; the system primary is charcoal `{colors.ink}`. Intercom also maintains a small **report palette** (`{colors.report-blue}`, `{colors.report-green}`, `{colors.report-pink}`, `{colors.report-lime}`) used inside in-product analytics surfaces shown in mockups.

The page rhythm is heavy on **product mockups**: every section's payload is a high-fidelity screenshot of Intercom's product UI, framed in white cards with `{rounded.xl}` 16px corners. The marketing chrome is intentionally quiet so the product can be the protagonist.

**Key Characteristics:**
- **Cream canvas** (`{colors.canvas}` #f5f1ec) is the brand's defining surface — neither white nor gray, deliberately warm.
- Product-screenshot-led page rhythm: every section centers a product mockup card, marketing chrome stays minimal.
- **Saans** proprietary sans-serif carries the entire hierarchy; SaansMono for code-only contexts.
- **Charcoal** `{colors.ink}` (#111111) is the system primary — buttons, headlines, body type all sit on charcoal.
- **Fin Orange** (`{colors.fin-orange}` #ff5600) is the AI product color — used on the Fin CTA and Fin badge, never decoratively.
- Display tracking pulls aggressively negative (-2.0px on 72px); body stays at 0.
- Card corners stay modest at `{rounded.lg}` 12px and `{rounded.xl}` 16px — never pill-rounded; never square.

## Colors

> Source pages: intercom.com (home), /pricing, /helpdesk, /customers, /helpdesk/inbox.

### Brand & Accent
- **Charcoal** ({colors.ink}): The system primary surface. Headlines, body type, primary CTA pill background — all charcoal.
- **White** ({colors.on-primary}): Text on charcoal CTAs; canvas of floating cards.
- **Fin Orange** ({colors.fin-orange}): The AI-product accent. Used on the Fin CTA, Fin badge, and a small set of inline emphasis moments.
- **Report Orange** ({colors.report-orange}): A slightly different orange used inside the report / analytics palette for in-product mockups.
- **Brand Blue** ({colors.brand-blue}): Saturated brand blue (#0007cb) — used on a small set of marketing illustrations.

### Surface
- **Canvas** ({colors.canvas}): Default page background — soft cream-white #f5f1ec.
- **Surface 1** ({colors.surface-1}): Pure white — used for floating cards (pricing, feature, product-mockup).
- **Surface 2** ({colors.surface-2}): Slightly darker cream — startup-discount banner, alt-row stripes.
- **Hairline** ({colors.hairline}): 1px borders on cards — soft warm gray (#d3cec6).
- **Hairline Soft** ({colors.hairline-soft}): Even softer dividers between FAQ rows and footer columns.
- **Inverse Canvas** ({colors.inverse-canvas}): Pure black — only on the testimonial / quote callout strip.
- **Inverse Surface 1** ({colors.inverse-surface-1}): One step lighter — hovered footer items in dark contexts.

### Text
- **Ink** ({colors.ink}): All headlines, body type, button labels — charcoal #111111.
- **Ink Muted** ({colors.ink-muted}): Secondary type at #626260 — meta info, deselected pricing tabs.
- **Ink Subtle** ({colors.ink-subtle}): Tertiary type at #7b7b78 — footer columns, helper text.
- **Ink Tertiary** ({colors.ink-tertiary}): Quaternary type at #9c9fa5 — disabled, footnotes.
- **Inverse Ink** ({colors.inverse-ink}): White on black — quote-strip type.
- **Inverse Ink Muted** ({colors.inverse-ink-muted}): Light gray on black — quote-strip meta.

### Semantic & Report Palette (in-product mockups)
- **Error Red** ({colors.semantic-error}): Form validation, destructive states.
- **Success Green** ({colors.semantic-success}): Positive states (also `{colors.report-green}`).
- **Report Blue** ({colors.report-blue}): Analytics chart blue.
- **Report Pink** ({colors.report-pink}): Analytics chart pink.
- **Report Lime** ({colors.report-lime}): Analytics chart lime.
- **Report Cyan** ({colors.report-cyan}): Phone country selector accent.

The report palette appears INSIDE product UI mockups — these are Intercom's in-product chart colors, not marketing surface colors.

## Typography

### Font Family

- **Saans** — Intercom's proprietary geometric sans, fallback `Saans Fallback, ui-sans-serif, system-ui`. Carries display, body, eyebrow, and button.
- **SaansMono** — Proprietary mono, fallback `SaansMono Fallback, ui-monospace`. Used inside code snippets shown in product mockups.

The same family carries the entire hierarchy. Hierarchy is carried by size + weight + tracking, not by family change.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 72px | 500 | 1.05 | -2.0px | Largest hero headline |
| `{typography.display-lg}` | 56px | 500 | 1.10 | -1.4px | Section opener headlines |
| `{typography.display-md}` | 40px | 500 | 1.15 | -0.8px | Sub-section headlines |
| `{typography.headline}` | 28px | 500 | 1.20 | -0.5px | Pricing tier titles, CTA banner |
| `{typography.card-title}` | 22px | 500 | 1.25 | -0.3px | Card title, feature card |
| `{typography.subhead}` | 20px | 400 | 1.40 | -0.2px | Lead body, intro paragraphs |
| `{typography.body-lg}` | 18px | 400 | 1.50 | -0.1px | Hero subhead, lead paragraphs |
| `{typography.body}` | 16px | 400 | 1.50 | 0 | Default body |
| `{typography.body-sm}` | 14px | 400 | 1.50 | 0 | Card body, footer |
| `{typography.caption}` | 12px | 400 | 1.40 | 0 | Captions, meta |
| `{typography.button}` | 15px | 500 | 1.20 | 0 | Pill / square button labels |
| `{typography.eyebrow}` | 14px | 500 | 1.30 | 0 | Section eyebrow (sentence case) |
| `{typography.mono}` | 13px | 400 | 1.50 | 0 | SaansMono for code in mockups |

### Principles

- **Weight 500 carries display.** Saans at 500 reads as confident without bold.
- **Negative letter-spacing scales with size.** -2.0px at 72px (≈3% of size), down to 0 on body.
- **Line-heights tighten on display, relax on body.** 1.05 at display-xl, 1.50 at body.
- **No mono on chrome.** SaansMono lives in product UI; marketing chrome stays in Saans.
- **Eyebrow uses sentence case** at 14px / 500 weight — no all-caps tracking.

### Note on Font Substitutes

If implementing without Saans, suitable substitutes include **Söhne** (paid), **Inter** (free, weight 500), or **Geist Sans** (free). Inter at weight 500 is the closest free substitute; SaansMono can be approximated with **JetBrains Mono** at weight 400.

## Layout

### Spacing System

- **Base unit**: 8px.
- **Tokens (front matter)**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- Card interior padding: `{spacing.lg}` 24px on pricing/feature cards; `{spacing.xl}` 32px on testimonial/discount cards; `{spacing.xxl}` 48px on CTA banners.
- Pill button padding: 10px vertical · 18px horizontal.

### Grid & Container

- Max content width sits around 1280px.
- Card grids are 3-up at desktop, 2-up at tablet, 1-up at mobile.
- Pricing tier grid is 3-up; comparison strip below shows checkmarks per tier.
- Product mockup cards span full content width — they're the protagonist of every section.

### Whitespace Philosophy

The cream canvas does the work white space would in another brand. Sections separate by ample vertical breathing room (`{spacing.section}` 96px) plus the lift-onto-white cards.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Default for body type, hero text, footer |
| 1 (lift on cream) | `{colors.surface-1}` white background on `{colors.canvas}` cream | Pricing cards, feature cards, product mockups |
| 2 (hairline lift) | `{colors.surface-1}` + 1px `{colors.hairline}` border | Floating tiles with extra definition |
| 3 (deep accent) | `{colors.inverse-canvas}` true black | Quote / testimonial callout strip |

Intercom resists drop shadows. Depth is communicated by the white-on-cream surface change.

### Decorative Depth

- **Product UI mockups** dominate every section's right column or center band — these are screenshots, not illustrations.
- **No atmospheric gradients, no spotlight cards, no pastel section blocks.** The cream + white system is deliberately restrained.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Small chips, badges |
| `{rounded.sm}` | 6px | Inline tags |
| `{rounded.md}` | 8px | All buttons, form inputs |
| `{rounded.lg}` | 12px | Pricing cards, feature cards, FAQ rows |
| `{rounded.xl}` | 16px | Product mockup cards |
| `{rounded.xxl}` | 24px | Oversized CTA banners |
| `{rounded.pill}` | 9999px | Tab toggles |
| `{rounded.full}` | 9999px | Avatar circles |

### Photography & Illustration Geometry

- Product UI screenshots dominate the marketing surface; they sit in `{rounded.xl}` 16px tiles.
- Customer logo tiles render at small sizes (~24–32px logo height) on `{colors.canvas}` cream with no border.
- Avatar circles in testimonial cards use `{rounded.full}` at 40–48px sizes.

## Components

Interaction states below are **prescribed**, not extracted: the inspected marketing pages are static captures, and only `button-primary-pressed`, `text-input-focused` and `pricing-tab-selected` existed as documented variants. Every other state named here is a recommendation consistent with the brand's restraint.

### Buttons

**`button-primary`** — Charcoal CTA. The default primary CTA across all pages.
- Background `{colors.ink}`, text `{colors.on-primary}`, type `{typography.button}`, padding 10px 18px, rounded `{rounded.md}`.
- Pressed state lives in `button-primary-pressed`.
- States: default · hover (fill deepens toward `{colors.inverse-canvas}`) · focus-visible (2px `{colors.focus}` ring, 2px `{colors.canvas}` offset) · active/pressed (`button-primary-pressed`, `transform: scale(0.97)`) · disabled (`{colors.ink-tertiary}` fill, `{colors.canvas}` label, no ring, `cursor: not-allowed`) · loading (label held, inline spinner in `{colors.on-primary}`, button stays width-stable).

**`button-secondary`** — White button on cream. Used for secondary CTAs.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.button}`, padding 10px 18px, rounded `{rounded.md}`. 1px `{colors.hairline}` border.
- States: default · hover (border steps to `{colors.hairline-strong}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed (`transform: scale(0.97)`) · disabled (`{colors.ink-tertiary}` label, `{colors.hairline-soft}` border) · loading (inline spinner in `{colors.ink}`).

**`button-tertiary`** — Plain text button.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.button}`, rounded `{rounded.md}`, padding 10px 18px.
- States: default · hover (label to `{colors.text-dim}`, 1px underline) · focus-visible (2px `{colors.focus}` ring) · active/pressed (`transform: scale(0.97)`) · disabled (`{colors.ink-tertiary}` label) · loading (not supported — a tertiary button never carries an async action).

**`button-fin`** — Fin Orange CTA — reserved for Fin AI product CTAs.
- Background `{colors.fin-orange}`, text `{colors.on-primary}`, type `{typography.button}`, rounded `{rounded.md}`, padding 10px 18px.
- States: default · hover (fill deepens to `{colors.report-orange}` #fe4c02) · focus-visible (2px `{colors.focus}` ring at 3.48:1 on the orange fill) · active/pressed (`transform: scale(0.97)`) · disabled (`{colors.ink-tertiary}` fill — never a desaturated orange, which reads as a live Fin CTA) · loading (inline spinner in `{colors.on-primary}`).

### Pricing Tabs

**`pricing-tab-default`** + **`pricing-tab-selected`** — Pill-toggle on `/pricing`.
- Default: `{colors.canvas}` background, `{colors.ink-muted}` text, rounded `{rounded.pill}`.
- Selected: `{colors.surface-1}` white background, `{colors.ink}` text — selected = lift onto white.
- States: default · hover (label to `{colors.ink}`, background unchanged) · focus-visible (2px `{colors.focus}` ring inside the pill group) · active/pressed (`transform: scale(0.97)`) · selected (`pricing-tab-selected`, plus a weight step to 500 so selection is not colour-only) · disabled (`{colors.ink-tertiary}` label) · loading (the tier grid below shows skeletons; the pill itself has no loading state).

### Cards & Containers

**`pricing-card`** — Each tier on `/pricing`.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 24px.
- States: default · hover (`transform: translateY(-1px)`, no shadow — Intercom resists shadows) · focus-visible (ring on the card's CTA, not the card) · selected (`pricing-card-featured`) · loading (skeleton: `{colors.surface-2}` blocks at card radius) · disabled, active/pressed and error: not applicable — a pricing card is not an interactive control.

**`pricing-card-featured`** — Featured / recommended tier — inverts to charcoal.
- Background `{colors.ink}`, text `{colors.on-primary}`, otherwise identical structure.
- States: default (this *is* the selected state of `pricing-card`) · hover (`transform: translateY(-1px)`) · focus-visible (its CTA uses `{colors.focus-on-dark}` — `{colors.focus}` sits at 1.7:1 on charcoal and would vanish) · loading (skeleton blocks in `{colors.inverse-surface-1}`). No disabled, active/pressed or error state.

**`feature-card`** — Generic feature highlight.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 24px.
- States: two only — default and hover (`transform: translateY(-1px)`), plus focus-visible when the whole card is a link (2px `{colors.focus}` ring at the card radius). It carries no disabled, loading, selected, active/pressed or error state.

**`product-mockup-card`** — The dominant card type — frames a high-fidelity product UI screenshot.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.xl}`, padding 24px.
- States: default and loading only — the screenshot is the section's payload, so it renders with no entrance and reserves its aspect ratio with a `{colors.surface-2}` skeleton while the image decodes. No hover, focus-visible, active/pressed, disabled, selected or error state: it is presentational.

**`testimonial-card`** — Customer quote with avatar + name + company.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body-lg}`, rounded `{rounded.lg}`, padding 32px.
- States: default · hover (only where it links to a customer story: `transform: translateY(-1px)`) · focus-visible (2px `{colors.focus}` ring) · loading (skeleton with a `{rounded.full}` avatar block). No active/pressed, disabled, selected or error state.

**`startup-discount-card`** — The "Startups get 90% off" tinted card.
- Background `{colors.surface-2}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 32px.
- States: default only, as a static promotional panel. Its embedded `button-primary` carries the hover, focus-visible, active/pressed, disabled and loading states; the panel itself has none.

**`customer-logo-tile`** — Small tile in the customer marquee.
- Background `{colors.canvas}`, text `{colors.ink-muted}`, type `{typography.caption}`, rounded `{rounded.xs}`, padding 16px.
- States: default · hover (logo lifts from `{colors.text-dim}` to full `{colors.ink}` opacity) · focus-visible (2px `{colors.focus}` ring where the tile links to a customer story) · loading (tile holds its box in `{colors.surface-2}`). No active/pressed, disabled, selected or error state.

**`cta-banner`** — Closing CTA panel near page bottom.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.headline}`, rounded `{rounded.lg}`, padding 48px.
- States: default only. Hover, focus-visible, active/pressed, disabled and loading all belong to the `button-primary` and `button-fin` it contains; the panel is a container with no error state.

### Inputs & Forms

**`text-input`** + **`text-input-focused`** — Form fields on contact and search overlays.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.md}`, padding 10px 14px.
- Boundary: 1px `{colors.hairline-strong}` #857f75 (3.97:1 on white), **not** `{colors.hairline}` — the input's edge is its only affordance, and `{colors.hairline}` measures 1.57:1 there.
- States: default · hover (border to `{colors.ink}` at 20% weight) · focus-visible (`text-input-focused` plus a 2px `{colors.focus}` ring, 2px offset) · active/pressed (no distinct state; focus-visible covers it) · disabled (`{colors.surface-2}` fill, `{colors.ink-tertiary}` text, `{colors.hairline-soft}` border) · loading (field locked, trailing spinner, value preserved) · error (1px `{colors.semantic-error}` border plus a `{typography.body-sm}` message in `{colors.semantic-error}` — never colour alone).

### FAQ

**`faq-row`** — Expandable accordion row in the pricing FAQ.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.md}`, padding 24px. 1px `{colors.hairline-soft}` bottom rule.
- States: default (collapsed) · hover (question to `{colors.text-dim}`, chevron rotates) · focus-visible (2px `{colors.focus}` ring on the row header) · active/pressed (`transform: scale(0.99)` on the header) · selected (expanded; chevron rotated 180°, `aria-expanded="true"`) · disabled and loading: not supported — FAQ content ships with the page · error: not applicable.

### Navigation

**`top-nav`** — Sticky cream bar with the Intercom wordmark left, nav links centered, log-in + sign-up pair right.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-sm}`, height 56px.
- Link states: default · hover (label to `{colors.text-dim}`) · focus-visible (2px `{colors.focus}` ring, 2px `{colors.canvas}` offset) · active/pressed (`transform: scale(0.97)` on the CTA pair only) · selected (current section, weight 500 plus a 2px `{colors.ink}` underline) · disabled and loading: not supported · error: not applicable.
- Bar states: default (transparent over `{colors.canvas}`) and scrolled (1px `{colors.hairline-strong}` bottom rule once the page leaves the hero).

### Footer

**`footer`** — Dense link grid on `{colors.canvas}` cream with the Intercom wordmark left.
- Background `{colors.canvas}`, text `{colors.ink-muted}`, type `{typography.caption}`, padding 64px 32px.
- Link states: default (`{colors.text-dim}` #626260 at 5.44:1 — **not** `{colors.ink-subtle}`, which measures 3.78:1 at this 12px size) · hover (to `{colors.ink}`, underline) · focus-visible (2px `{colors.focus}` ring) · active/pressed (no travel; colour only) · disabled, loading, selected and error: not supported in the footer.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or easing curve below was extracted from intercom.com; they are the **Playful** profile values from the audit spec, chosen so the small scale-pop on press and the springy card reveal match a friendly, conversational support brand — then damped by Intercom's editorial restraint (short travel, no ornament, opacity doing most of the work).

All values reference the `motion:` token group. Only `transform` and `opacity` animate — never `width`, `height`, `top`, `left` or `margin`. Every exit is shorter than its matching entrance.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, cards, nav links) | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `opacity`, `transform: translateY(-1px)` | Travel removed; opacity only at `{motion.duration-reduced}` 130ms |
| Press / active | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.97)` | Scale removed; background swap to `button-primary-pressed` is instant |
| Focus-visible ring | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` on the `{colors.focus}` ring | Ring appears with no transition — never delayed, never faded |
| Page / route transition | `{motion.duration-base}` 200ms in · `{motion.duration-fast}` 130ms out | `{motion.ease-enter}` in · `{motion.ease-exit}` out | `opacity`, `transform: translateY(8px)` | Travel removed; cross-fade only at `{motion.duration-reduced}` 130ms |
| Modal / drawer | `{motion.duration-slow}` 320ms in · `{motion.duration-base}` 200ms out | `{motion.ease-enter}` in · `{motion.ease-exit}` out | `opacity`, `transform: scale(0.98→1)`; drawer uses `translateX(100%→0)` | Scale and slide removed; scrim and panel fade at `{motion.duration-reduced}` 130ms |
| Dropdown (nav mega-menu, pricing selector) | `{motion.duration-fast}` 130ms in · `{motion.duration-instant}` 70ms out | `{motion.ease-enter}` in · `{motion.ease-exit}` out | `opacity`, `transform: translateY(-4px) scale(0.99)` | Travel and scale removed; opacity only at `{motion.duration-reduced}` 130ms |
| Toast | `{motion.duration-base}` 200ms in · `{motion.duration-fast}` 130ms out | `{motion.ease-enter}` in · `{motion.ease-exit}` out | `opacity`, `transform: translateY(12px)` | Travel removed; fade at `{motion.duration-reduced}` 130ms |
| List enter (pricing tiers, feature cards, customer logos) | `{motion.duration-base}` 200ms, staggered `{motion.stagger-step}` 60ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Stagger and travel removed; one simultaneous fade at `{motion.duration-reduced}` 130ms |
| List exit | `{motion.duration-fast}` 130ms, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Scale removed; fade at `{motion.duration-reduced}` 130ms |
| Loading (spinner, skeleton) | 900ms spinner rotation, infinite; skeleton shimmer 1200ms, infinite | `linear` | `transform: rotate()` on the spinner; `opacity` on the skeleton | Spinner rotation replaced by an opacity pulse at `{motion.duration-reduced}` 130ms; skeleton shimmer frozen at its mid tone |

### Choreography notes

- **The press pop is the one playful gesture.** A 3% scale dip on `button-primary` and `button-fin` is the whole of Intercom's friendliness budget — there is no bounce on cards, no overshoot on hero type, no parallax on the product mockups.
- **`{motion.ease-enter}` overshoots** (`cubic-bezier(0.17, 0.89, 0.32, 1.28)`), so entrances settle slightly past their resting position. Hold the travel to 8px or less; on a 1280px editorial canvas a longer throw reads as cheap.
- **Product mockup cards never animate on first paint.** The screenshot is the payload of every section; it renders immediately and does not wait on a reveal.
- **FAQ accordion:** the panel cross-fades with `opacity` plus a `translateY(-4px)` lead-in over `{motion.duration-fast}`. The row's own height change is not animated — it resolves in one layout pass.
- **No infinite animation** anywhere except the spinner and skeleton above. Intercom has no brand ambience loop; the cream canvas is static.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translateX/Y), all scale, the 60ms list stagger,
     the press pop, and the spinner's rotation. */
  /* Kept: opacity cross-fades, capped at 130ms — {motion.duration-reduced}. */
  /* Frozen: skeleton shimmer holds its mid tone; the spinner becomes an
     opacity pulse so progress is still conveyed. */
  *, *::before, *::after {
    transition-duration: 130ms !important;
    transition-property: opacity !important;
    animation-duration: 130ms !important;
    animation-iteration-count: 1 !important;
  }
  .focus-ring { transition: none !important; }
}
```

The focus ring is exempt from the cap in both directions: it must appear instantly, so it carries no transition at all under reduced motion.

## Accessibility

### Measured contrast

Every ratio below is computed with WCAG 2.1 relative luminance from this file's own hexes. Brand hexes are extracted and frozen — the failures are real and are not fixed in place.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` #111111 on `{colors.canvas}` #f5f1ec | 16.79:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface}` #ffffff | 18.88:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-2}` #ebe7e1 | 15.33:1 | 4.5:1 | Pass |
| `{colors.text-dim}` #626260 on `{colors.canvas}` | 5.44:1 | 4.5:1 | Pass |
| `{colors.text-dim}` on `{colors.surface-2}` | 4.96:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` charcoal | 18.88:1 | 4.5:1 | Pass |
| `{colors.inverse-ink}` on `{colors.inverse-canvas}` | 21.0:1 | 4.5:1 | Pass |
| `{colors.semantic-error}` on `{colors.canvas}` | 5.29:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` #857f75 on `{colors.canvas}` | 3.53:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.surface}` | 3.97:1 | 3.0:1 | Pass |
| `{colors.ink-subtle}` #7b7b78 on canvas / on `{colors.surface}` | 3.78:1 / 4.25:1 | 4.5:1 | **Fail — real brand tone** |
| `{colors.ink-tertiary}` #9c9fa5 on canvas / on `{colors.surface}` | 2.36:1 / 2.65:1 | 4.5:1 | **Fail — real brand tone** |
| `{colors.hairline}` #d3cec6 on canvas / on `{colors.surface}` | 1.39:1 / 1.57:1 | 3.0:1 | **Fail — decorative only** |
| `{colors.hairline-soft}` #ebe7e1 on canvas / on `{colors.surface}` | 1.1:1 / 1.23:1 | 3.0:1 | **Fail — decorative only** |
| `{colors.semantic-success}` #0bdf50 on `{colors.canvas}` | 1.6:1 | 4.5:1 | **Fail — chart fill, never text** |
| `button-fin` — `{colors.on-primary}` white on `{colors.fin-orange}` #ff5600 | 3.19:1 | 4.5:1 | **Fail — real brand CTA** |

### What the failures mean

- **Intercom's hairlines fail AA for boundaries, plainly.** `{colors.hairline}` at 1.39:1 and `{colors.hairline-soft}` at 1.1:1 are extracted facts, not defects to patch. They are scoped to **decoration**: card edge definition and FAQ/footer dividers, where the white-on-cream surface change already carries the boundary. `{colors.hairline-strong}` #857f75 is a **prescribed** parallel token, not extracted from the site, and is the only boundary permitted on a control whose edge is the sole affordance — a `text-input`, a `pricing-tab-default`, a checkbox.
- **`{colors.ink-subtle}` and `{colors.ink-tertiary}` fail AA as body text.** `{colors.ink-subtle}` at 3.78:1 clears the 3:1 large-text threshold, so it is permissible at 24px+, or 18.66px+ at weight 700 — not at the 14px footer size the site uses it at. `{colors.ink-tertiary}` at 2.36:1 clears no threshold and must be treated as a disabled tone only, where WCAG sets no requirement. Use `{colors.text-dim}` #626260 (5.44:1) for any secondary text that must be read.
- **`button-fin` fails AA.** White on Fin Orange measures 3.19:1, below 4.5:1 for its 15px / weight 500 label. It clears 3:1, so the same label at `{typography.headline}` 28px would pass as large text. The fix that does not falsify the brand is type size, not a new orange.
- **`{colors.semantic-success}` is a chart fill**, drawn inside product mockups. It must never carry text or convey state by colour alone.

### Focus ring

No focus treatment was documented for this brand, so one is prescribed. `{colors.focus}` #0007cb is Intercom's own `brand-blue`, reused rather than invented: a 2px ring with a 2px `{colors.canvas}` offset.

| Surface it is drawn on | Ring | Ratio | Required |
|---|---|---|---|
| `{colors.canvas}` cream | `{colors.focus}` | 9.87:1 | 3.0:1 |
| `{colors.surface}` / `{colors.surface-1}` white | `{colors.focus}` | 11.09:1 | 3.0:1 |
| `{colors.surface-2}` cream-dark | `{colors.focus}` | 9.01:1 | 3.0:1 |
| `{colors.fin-orange}` CTA fill | `{colors.focus}` | 3.48:1 | 3.0:1 |
| `{colors.primary}` / `{colors.ink}` charcoal CTA and featured tier | `{colors.focus-on-dark}` #65b5ff | 8.64:1 | 3.0:1 |
| `{colors.inverse-canvas}` black quote strip | `{colors.focus-on-dark}` | 9.61:1 | 3.0:1 |
| `{colors.inverse-surface-1}` #313130 | `{colors.focus-on-dark}` | 5.96:1 | 3.0:1 |

Two rings exist because the file documents both light and dark signature surfaces: #0007cb sits at 1.7:1 on charcoal and would vanish there. `{colors.focus-on-dark}` reuses the `report-blue` hex. Over a product screenshot, which has no measurable colour, draw `{colors.focus}` with a 1px `{colors.on-primary}` outer edge.

### Tap targets

Documented in Responsive Behavior: CTAs and pricing tab pills hold ≥40px, form inputs ≥44px. These are the file's stated intent and were **not** verified against a rendered page — tap-target size is not measurable from a document.

### Reduced motion

Honoured as specified in Motion & Animation: all travel, scale and stagger removed, opacity fades capped at `{motion.duration-reduced}` 130ms, skeleton shimmer frozen, and the focus ring left untransitioned so it never lags the keyboard.

### Known accessibility gaps

- Colour is not the only state signal anywhere documented, but no non-colour indicator is specified for `pricing-tab-selected` beyond the white lift; add a weight change.
- Error text styling is undocumented (see Known Gaps), so no error-text contrast could be measured.
- Keyboard order, landmark structure and screen-reader naming need a rendered page and are outside this audit's reach.

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
| `{colors.hairline-soft}` (`#ebe7e1`) on `{colors.surface-2}` (`#ebe7e1`) | 1.00:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.semantic-success}` (`#0bdf50`) on `{colors.surface-2}` (`#ebe7e1`) | 1.46:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.ink-tertiary}` (`#9c9fa5`) on `{colors.surface-2}` (`#ebe7e1`) | 2.15:1 | 4.5:1 | Fail — secondary text on surface, all tones |
| `{colors.ink-subtle}` (`#7b7b78`) on `{colors.surface-2}` (`#ebe7e1`) | 3.45:1 | 4.5:1 | Fail — secondary text on surface, all tones |

## Do's and Don'ts

### Do

- Reserve `{colors.canvas}` cream as the system's anchor surface — never replace with pure white.
- Lift cards from cream onto white (`{colors.surface-1}`) for hierarchy.
- Use **`button-fin`** Fin Orange ONLY on Fin AI product CTAs and Fin badges.
- Pair Saans display at weight 500 with body at 400.
- Use product UI screenshots as the protagonist of every section.
- Use `{rounded.lg}` 12px for cards and `{rounded.xl}` 16px for product mockup tiles.
- Apply negative tracking proportionally to display sizes.

### Don't

- Don't use pure white as the canvas.
- Don't use Fin Orange as a section background or as a generic primary CTA.
- Don't add drop shadows to floating cards.
- Don't introduce a second display family.
- Don't pill-round CTAs.
- Don't write all-caps tracked eyebrows.
- Don't promote the report palette colors to brand-level surfaces.
- Don't combine charcoal CTAs and Fin Orange CTAs in the same viewport.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop-XL | 1440px | Default desktop layout |
| Desktop | 1280px | Card grid 3-up maintained |
| Tablet | 1024px | Card grid 3-up → 2-up |
| Mobile-Lg | 768px | Pricing comparison becomes accordion; nav hamburger |
| Mobile | 480px | Single-column; display-xl scales 72px → ~32px |

### Touch Targets

- CTAs hold ≥40px tap height across viewports.
- Pricing tab pills hold ≥40px tap height.
- Form inputs hold ≥44px tap target on touch.

### Collapsing Strategy

- **Top nav**: links collapse to hamburger below 768px; primary CTA stays visible.
- **Card grids**: 3-up → 2-up at 1024px → 1-up below 768px.
- **Pricing comparison**: collapses into per-tier accordion below 768px.
- **Display type**: `{typography.display-xl}` 72px scales toward `{typography.display-md}` 40px on mobile.

### Image Behavior

- Product UI screenshots maintain aspect ratio and never crop.
- Customer logos in the marquee may collapse from 6-up to 3-up below 768px.

## Iteration Guide

1. Focus on ONE component at a time and reference it by its `components:` token name.
2. When introducing a section, decide first whether it sits on `{colors.canvas}` cream (default) or whether it lifts onto a `{colors.surface-1}` white card.
3. Default body to `{typography.body}` at weight 400.
4. Run `npx @google/design.md lint DESIGN.md` after edits.
5. Add new variants as separate component entries.
6. Treat Fin Orange as a product accent: Fin CTA and Fin badge only.
7. Lead every section with a product screenshot.

## Known Gaps

- The **report palette** lives in product analytics dashboards rendered inside marketing mockups; they are documented for completeness but are not brand surface colors.
- Form-field error and validation styling is not visible on the inspected pages.
- Dark mode is not documented because the marketing site does not ship a dark theme.
- The helpdesk / inbox product surfaces show in-product UI states that aren't formal marketing chrome.
- Saans and SaansMono are proprietary; an open-source substitute (Inter, Söhne, Geist) is acceptable.
