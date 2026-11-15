---
version: alpha
name: Stripi-Inspired-design-analysis
description: An inspired interpretation of Stripi's design language — a financial-infrastructure brand built on a deep navy ink, an electric indigo primary, and a recurring atmospheric gradient mesh that occupies the upper third of nearly every marketing page. The system pairs the proprietary Sohne family at thin (300) weights with negative letter-spacing for editorial-density display headlines, and uses tabular-figure body type where money and numerics matter. Buttons are tight-radius pills, cards live on near-white surfaces, and the dashboard track flips polarity to a familiar dark-app shell.

colors:
  primary: "#533afd"
  primary-deep: "#4434d4"
  primary-press: "#2e2b8c"
  primary-soft: "#665efd"
  primary-bg-subdued-hover: "#b9b9f9"
  brand-dark-900: "#1c1e54"
  ink: "#0d253d"
  ink-secondary: "#273951"
  ink-mute: "#64748d"
  ink-mute-2: "#61718a"
  on-primary: "#ffffff"
  focus: "#665efd"
  canvas: "#ffffff"
  canvas-soft: "#f6f9fc"
  canvas-cream: "#f5e9d4"
  hairline: "#e3e8ee"
  hairline-input: "#a8c3de"
  ruby: "#ea2261"
  magenta: "#f96bee"
  lemon: "#9b6829"
  shadow-blue: "#003770"

typography:
  display-xxl:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.03
    letterSpacing: -1.4px
    fontFeature: ss01
  display-xl:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.96px
    fontFeature: ss01
  display-lg:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.64px
    fontFeature: ss01
  display-md:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 26px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.26px
    fontFeature: ss01
  heading-lg:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.22px
    fontFeature: ss01
  heading-md:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: -0.2px
    fontFeature: ss01
  heading-sm:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
    fontFeature: ss01
  body-lg:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
    fontFeature: ss01
  body-md:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
    fontFeature: ss01
  body-tabular:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: -0.42px
    fontFeature: tnum
  button-md:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    fontFeature: ss01
  button-sm:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    fontFeature: ss01
  caption:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: -0.39px
    fontFeature: tnum
  micro:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
    fontFeature: ss01
  micro-cap:
    fontFamily: "sohne-var, 'SF Pro Display', system-ui, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.1px
    fontFeature: ss01

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px

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
  button-primary-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-primary-pill-pressed:
    backgroundColor: "{colors.primary-press}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-on-dark:
    backgroundColor: "{colors.brand-dark-900}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline-input}"
    padding: 8px 12px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.primary}"
    focusRing: "{colors.focus}"
    padding: 8px 12px
  section-band-soft:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 64px 24px
  card-feature-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    borderColor: "{colors.hairline}"
    padding: 32px
  card-pricing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    borderColor: "{colors.hairline}"
    padding: 32px
  card-pricing-featured:
    backgroundColor: "{colors.brand-dark-900}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-cream-band:
    backgroundColor: "{colors.canvas-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-dashboard-mockup:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-tabular}"
    rounded: "{rounded.lg}"
    padding: 24px
  pill-tag-soft:
    backgroundColor: "{colors.primary-bg-subdued-hover}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.micro-cap}"
    rounded: "{rounded.pill}"
    padding: 4px 8px
  nav-bar-on-mesh:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  link-on-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
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

Stripi's design language opens with the gradient mesh. A wide horizontal band of pastel cream, sherbet orange, lavender, electric indigo, and ruby pink occupies the upper third of nearly every marketing page — the brand's instantly-recognizable atmospheric backdrop. Type and product UI mockups float above it on `{colors.canvas}` (white), with the gradient acting as both decoration and visual anchor. The lower portion of the page returns to white, with feature explanations on `{colors.canvas-soft}` (a barely-tinted cool off-white) and dashboard product mockups composited as faux IDE/console panels in deep navy.

The color system has two primary roles. **Indigo** (`{colors.primary}` — `#533afd`) is the brand's signature CTA color, used sparingly: one filled pill per band. **Deep navy** (`{colors.ink}` — `#0d253d`) is the universal body text color and the fill of dashboard mockups, the featured pricing tier, and the dark-app surfaces on the dashboard track. Ruby (`{colors.ruby}`) and magenta (`{colors.magenta}`) appear inside the gradient mesh and as accent dots in product UI mockups; they are not used as button colors.

Typography is built around **Sohne** at weight 300 with negative letter-spacing — the brand's editorial-density display signature. Display sizes (32–56px) use -1.4px to -0.64px tracking; body sizes use 0; tabular caption sizes (where money and numerics matter) use the OpenType `tnum` feature plus a tightening -0.36 to -0.42px tracking. The `ss01` stylistic set is enabled across all roles.

**Key Characteristics:**
- Gradient-mesh backdrop on every marketing hero — cream/orange/lavender/indigo/ruby horizontally washed across the upper third of the page.
- Single-indigo CTA hierarchy: filled `{colors.primary}` pill is the only filled button on marketing surfaces.
- Sohne thin (weight 300) display tier with negative tracking from -1.4px to -0.2px depending on size.
- Tabular-figure body type (`tnum`) for any cell containing money or numerics — the brand's quiet financial-data signal.
- Dark-app dashboard track: deep navy product UI mockups sit composited above the white canvas, frequently with rendered code or dashboard tables inside.
- Pill-shaped buttons (`{rounded.pill}` 9999px) with tight `8px 16px` padding — short, decisive, transactional.
- Cream-band feature cards (`{colors.canvas-cream}`) introduce a warm interlude between blue/white sections without breaking the brand's chromatic logic.

## Colors

> **Source pages:** home (`/`), `/payments`, `/pricing`, `dashboard.stripe.com/register/payments`.

### Brand & Accent
- **Indigo** (`{colors.primary}` — `#533afd`): The brand's signature CTA color. Filled-pill button, link emphasis, gradient anchor.
- **Indigo Deep** (`{colors.primary-deep}` — `#4434d4`): A deeper indigo used in gradient mid-stops and as the press-state warmer alternative.
- **Indigo Press** (`{colors.primary-press}` — `#2e2b8c`): Pressed-state lift of the primary.
- **Indigo Soft** (`{colors.primary-soft}` — `#665efd`): A lighter indigo used in product-UI accents and chart highlights.
- **Indigo Subdued** (`{colors.primary-bg-subdued-hover}` — `#b9b9f9`): Pale indigo fill used as soft tag background.
- **Brand Dark 900** (`{colors.brand-dark-900}` — `#1c1e54`): The deep navy used on the featured pricing tier and dashboard chrome.
- **Ruby** (`{colors.ruby}` — `#ea2261`): Gradient accent and chart highlight; never a button.
- **Magenta** (`{colors.magenta}` — `#f96bee`): Brighter pink stop in gradient meshes.
- **Lemon** (`{colors.lemon}` — `#9b6829`): Warm sherbet stop in gradient backdrops.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): Default page background.
- **Canvas Soft** (`{colors.canvas-soft}` — `#f6f9fc`): Cool-tinted off-white used on feature bands beneath the gradient hero.
- **Canvas Cream** (`{colors.canvas-cream}` — `#f5e9d4`): Warm cream used as a feature-band fill — the brand's chromatic interlude.
- **Hairline** (`{colors.hairline}` — `#e3e8ee`): 1px borders on cards and tables. Extracted and frozen. It is a **decorative** rule only: at 1.23:1 on `{colors.canvas}` and 1.17:1 on `{colors.canvas-soft}` it does not meet the 3:1 non-text minimum, so it must never be the sole indicator of a control's extent or state.
- **Hairline Input** (`{colors.hairline-input}` — `#a8c3de`): Slightly cooler hairline used on form inputs. Extracted and frozen, and 1.82:1 on `{colors.canvas}` — the real brand's input boundary fails WCAG 1.4.11. Where the boundary is the only affordance of a field, draw it in `{colors.ink-mute}` (`#64748d`, 4.75:1 on canvas), which the palette already owns; add no new border tone.
- **Focus** (`{colors.focus}` — `#665efd`): The focus ring. This is `{colors.primary-soft}`'s hex, reused — not a new brand colour — chosen because it is the one indigo that clears 3:1 against every surface this file defines, white through deep navy. See Accessibility.

### Text
- **Ink** (`{colors.ink}` — `#0d253d`): Default body text color across the brand. Deep navy, never pure black.
- **Ink Secondary** (`{colors.ink-secondary}` — `#273951`): Secondary text on white.
- **Ink Mute** (`{colors.ink-mute}` — `#64748d`): Helper text, captions, table labels.
- **Ink Mute 2** (`{colors.ink-mute-2}` — `#61718a`): Near-equivalent to ink-mute used in nav.
- **On Primary** (`{colors.on-primary}` — `#ffffff`): Text on indigo / dark-navy surfaces.

### Semantic
The brand does not use a separate semantic color palette in the marketing system — error / success states live in dashboard-product UI specifically.

## Typography

### Font Family

The display and UI tier is **Sohne** (proprietary, licensed from Klim Type Foundry) at weights 300 (thin) and 400 (regular). The variable font (`sohne-var`) is loaded with `font-feature-settings: "ss01"` enabled globally — the stylistic set substitutes a single-story `a` and other character variants that are part of the brand's typographic signature.

When Sohne is unavailable, fall back to **SF Pro Display** at thin weights, then system-ui. For maximum brand fidelity, **Inter** (open-source) at weight 300 with `font-feature-settings: "ss01"` and `letter-spacing: -1.4px` on display sizes approximates the rhythm closely.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 56px | 300 | 1.03 | -1.4px | Hero headline |
| `{typography.display-xl}` | 48px | 300 | 1.15 | -0.96px | Section opener |
| `{typography.display-lg}` | 32px | 300 | 1.1 | -0.64px | Card title / sub-section |
| `{typography.display-md}` | 26px | 300 | 1.12 | -0.26px | Compact card title |
| `{typography.heading-lg}` | 22px | 300 | 1.1 | -0.22px | Pricing tier name |
| `{typography.heading-md}` | 20px | 300 | 1.4 | -0.2px | Section sub-heading |
| `{typography.heading-sm}` | 18px | 300 | 1.4 | 0 | Mini-section label |
| `{typography.body-lg}` | 16px | 300 | 1.4 | 0 | Marketing body lead |
| `{typography.body-md}` | 15px | 300 | 1.4 | 0 | Default UI body |
| `{typography.body-tabular}` | 14px | 300 | 1.4 | -0.42px | Money / numeric tables (uses `tnum`) |
| `{typography.button-md}` | 16px | 400 | 1.0 | 0 | Pill button label |
| `{typography.button-sm}` | 14px | 400 | 1.0 | 0 | Compact pill label |
| `{typography.caption}` | 13px | 400 | 1.4 | -0.39px | Helper, table labels |
| `{typography.micro}` | 11px | 300 | 1.4 | 0 | Fine print |
| `{typography.micro-cap}` | 10px | 400 | 1.15 | 0.1px | All-caps eyebrow |

### Principles
- **Thin weight is the brand.** Display tiers always render at weight 300. Bumping to 400+ removes the brand's editorial air.
- **Negative tracking on display.** -1.4px at 56px, scaling proportionally down to -0.2px at 20px. The negative tracking is the brand's typographic signature.
- **Tabular figures for money.** Any cell rendering currency, transaction amounts, or numeric counts uses `font-feature-settings: "tnum"` plus a tightening tracking. The brand quietly signals its financial DNA through this micro-detail.
- **`ss01` globally.** Apply `font-feature-settings: "ss01"` to the body element so the stylistic-set substitution is on for every text role.

### Note on Font Substitutes
Sohne is proprietary. Use **Inter** (open-source via Google Fonts) at weight 300 with `letter-spacing: -1.4px` and `font-feature-settings: "ss01"` for display tiers — Inter is the closest open-source analogue. For body sizes, Inter at 300 weight with `font-feature-settings: "tnum"` (where applicable) is the canonical substitute. Avoid Helvetica or system-ui defaults — they're heavier than the brand needs.

## Layout

### Spacing System
- **Base unit**: 8px (with 2 / 4 / 12 sub-tokens for fine work).
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.huge}` 64px.
- **Section padding**: 64–96px on marketing surfaces; 32–48px on dashboard / product surfaces.
- **Card internal padding**: 32px on feature cards; 24px on dashboard mockups.

### Grid & Container
- Marketing pages center in a ~1200px container with the gradient mesh extending edge-to-edge above.
- Pricing collapses 4-up → 2-up → 1-up at 1024 / 768 breakpoints.
- Dashboard product mockups use their own internal grids (12-col tables, 3-col card grids) rendered as static composites.

### Whitespace Philosophy
The gradient mesh occupies the upper third of the page; the white canvas below is generously padded. Section gaps tend toward 96px, with content tightening to 32px on dashboard / pricing pages where users compare and act.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default surface |
| 1 | `box-shadow: rgba(0,55,112,0.08) 0 1px 3px` | Card lift on white |
| 2 | `box-shadow: rgba(0,55,112,0.08) 0 8px 24px, rgba(0,55,112,0.04) 0 2px 6px` | Floating panels, dashboard mockup chrome |
| 3 | Gradient mesh backdrop | The brand's primary depth medium — atmospheric color rather than literal shadow |

### Decorative Depth
The gradient mesh IS the depth system. Implemented as a layered SVG or large background image rather than CSS gradients (the actual mesh has organic blob shapes that aren't CSS-renderable). The mesh provides the brand's signature lift; literal shadows are reserved for product-UI mockups and stay subtle.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Hairline tags, table chrome |
| `{rounded.sm}` | 6px | Form inputs |
| `{rounded.md}` | 8px | Compact cards, alerts |
| `{rounded.lg}` | 12px | Pricing cards, feature cards |
| `{rounded.xl}` | 16px | Dashboard product mockup chrome |
| `{rounded.pill}` | 9999px | All buttons, tag pills |

### Photography Geometry
The brand uses **product UI mockups** more than photography. Dashboard composites render as faux IDE/terminal/dashboard chrome inside `{rounded.lg}` 12px containers with a subtle `box-shadow`. Real photography appears in customer logo strips and the rare case-study card; treated as inset 4:3 with no shadow.

## Components

### Buttons

**`button-primary-pill`** — the dominant CTA system-wide.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button-md}`, padding `{spacing.sm} {spacing.lg}` (8px 16px), rounded `{rounded.pill}` 9999px.
- Pressed state `button-primary-pill-pressed` shifts background to `{colors.primary-press}`.
- States: default · hover (background `{colors.primary-deep}`) · focus-visible (2px `{colors.focus}` ring, 2px offset, outside the pill) · active/pressed (`{colors.primary-press}`) · disabled (`{colors.primary-bg-subdued-hover}` fill, `{colors.on-primary}` label, no ring) · loading (label holds, inline indeterminate bar in `{colors.on-primary}`) · selected — not applicable, a CTA is not a toggle · error — not applicable, errors surface on the field, never on the CTA.

**`button-secondary`** — outline-style alternative.
- Background `{colors.canvas}`, text `{colors.primary}`, 1px solid `{colors.primary}` border, same pill geometry.
- States: default · hover (border and label to `{colors.primary-deep}`) · focus-visible (`{colors.focus}` ring, 2px offset) · active/pressed (`{colors.primary-press}`) · disabled (border and label `{colors.hairline-input}`) · loading (as `button-primary-pill`) · selected and error — not applicable.

**`button-on-dark`** — used on dashboard / dark surfaces.
- Background `{colors.brand-dark-900}`, text `{colors.on-primary}`, same pill geometry.
- States: default · hover (fill lifts to `{colors.primary-deep}`) · focus-visible (`{colors.focus}` ring, 3.36:1 on `{colors.brand-dark-900}`) · active/pressed (`{colors.primary-press}`) · disabled (fill `{colors.brand-dark-900}` at 40% over the navy shell, label `{colors.ink-mute}`) · loading · selected and error — not applicable.

### Cards & Containers

**`card-feature-light`** — feature explanation card on white.
- Background `{colors.canvas}`, padding `{spacing.xxl}`, rounded `{rounded.lg}` 12px, 1px `{colors.hairline}` border, optional Level 1 shadow.
- States: default · hover (Level 1 → Level 2 shadow, no travel) · focus-visible on the whole card where it is a link (`{colors.focus}` ring, 2px offset) · active/pressed (shadow returns to Level 1) · disabled, loading (skeleton bars in `{colors.hairline}`), selected and error — the static feature card carries only default, hover, focus-visible and active/pressed; the other four are genuinely absent from this component.

**`card-pricing`** — standard pricing tier.
- Background `{colors.canvas}`, padding `{spacing.xxl}`, rounded `{rounded.lg}`, 1px `{colors.hairline}` border. Title `{typography.heading-lg}`, price `{typography.display-md}`, body `{typography.body-md}`, CTA pinned bottom as `button-primary-pill`.
- States: default · hover (Level 1 → Level 2) · focus-visible (`{colors.focus}` ring on the card when the whole tier is the control) · active/pressed · selected (2px `{colors.primary}` border plus a `pill-tag-soft` eyebrow — the border is paired with the tag so selection is never colour-only) · disabled (tier greyed to `{colors.ink-mute}` labels, CTA disabled) · loading (skeleton) · error — not applicable to a pricing tier.

**`card-pricing-featured`** — the inverted dark featured tier.
- Background `{colors.brand-dark-900}`, text `{colors.on-primary}`, otherwise identical structure to `card-pricing`. The deep-navy fill is the brand's distinctive featured-tier choice.
- States: as `card-pricing`, with focus-visible drawn in `{colors.focus}` (3.36:1 on the navy fill) rather than against white.

**`card-cream-band`** — warm interlude card.
- Background `{colors.canvas-cream}`, text `{colors.ink}`, padding `{spacing.xxl}`, rounded `{rounded.lg}`. Used to break up the indigo / white rhythm with warmth. It carries no border: the cream fill is its own boundary against white (1.2:1), so the band is a colour change, never a container edge.
- States: default only — a static editorial band, with hover, focus-visible, active/pressed, disabled, loading, selected and error all absent from this component by design.

**`section-band-soft`** — full-width feature band beneath the gradient hero.
- Background `{colors.canvas-soft}`, text `{colors.ink}` (14.73:1), padding `{spacing.huge} {spacing.xl}`. This is the brand's real secondary surface: feature explanations sit on it, and cards on it return to `{colors.canvas}` white.
- States: default only — a layout band has no interactive states.

**`card-dashboard-mockup`** — composited dashboard / product UI screenshot.
- Background `{colors.canvas}`, type `{typography.body-tabular}` (with `tnum`), padding `{spacing.xl}` 24px, rounded `{rounded.lg}` 12px, Level 2 shadow. Often contains nested mini-mockups: code preview + dashboard table + chart card.
- States: default only — the composite is a static image of the product, so its inner controls render in their default state and the mockup itself has no hover, focus-visible, active/pressed, disabled, loading, selected or error state.

### Inputs & Forms

**`text-input`** — standard form field.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, padding `{spacing.sm} {spacing.md}` (8px 12px), rounded `{rounded.sm}` 6px, 1px `{colors.hairline-input}` border.
- Focus state `text-input-focused`: border swaps to `{colors.primary}`.
- States: default · hover (border to `{colors.ink-mute}`) · focus-visible (border `{colors.primary}` plus a 2px `{colors.focus}` ring at 2px offset) · active/pressed — the field has no distinct pressed look, so pressed is the focus-visible state · disabled (border `{colors.hairline}`, label `{colors.ink-mute}`, no ring) · loading (inline spinner at the trailing edge, field stays readable) · selected (text selection only) · error (border and helper text in `{colors.ruby}`, plus a leading icon so the error is not colour-only — prescribed; the brand's marketing palette carries no semantic set, see Known Gaps).
- The extracted 1px `{colors.hairline-input}` boundary is 1.82:1 on `{colors.canvas}`: as built, the real brand's input outline fails WCAG 1.4.11. Draw the boundary in `{colors.ink-mute}` (4.75:1) where it is the field's only affordance; the frontmatter binding is left as extracted, and re-pointing it is under Needs approval in the audit report.

### Navigation

**`nav-bar-on-mesh`** — top nav floating over the gradient hero.
- Background `{colors.canvas}` (or transparent depending on scroll), text `{colors.ink}`, padding `{spacing.lg} {spacing.xl}`. Logo wordmark on the left, primary nav center, sign-in + filled `button-primary-pill` on the right.
- Nav item states: default · hover (label to `{colors.primary}`, dropdown opens) · focus-visible (`{colors.focus}` ring, 2px offset — the ring sits on white or on the gradient mesh, so it is drawn with a 1px `{colors.on-primary}` outer edge over the mesh, which has no single measurable colour) · active/pressed · selected (current section underlined 2px in `{colors.primary}`, plus the label at weight 400 so the current item is not colour-only) · disabled, loading and error — not applicable to the marketing nav.

### Pills, Tags, and Chips

**`pill-tag-soft`** — subdued indigo tag.
- Background `{colors.primary-bg-subdued-hover}`, text `{colors.primary-deep}`, type `{typography.micro-cap}`, padding `4px 8px`, rounded `{rounded.pill}`.
- States: default · hover and active/pressed only where the tag is a filter chip · focus-visible (`{colors.focus}` ring, 2px offset) · selected (fill to `{colors.primary}`, label to `{colors.on-primary}`) · disabled (fill `{colors.hairline}`, label `{colors.ink-mute}`) · loading and error — not applicable. A static eyebrow tag genuinely has one state.
- The extracted pair measures 4.23:1 (`{colors.primary-deep}` on `{colors.primary-bg-subdued-hover}`), under the 4.5:1 AA minimum for its 10px `{typography.micro-cap}` type. The real brand fails AA here; `{colors.primary-press}` on the same fill reaches 6.18:1 and is the nearest passing ink.

### Signature Components

**Gradient Mesh Backdrop** — pastel cream → sherbet orange → lavender → indigo → ruby pink stops blurred horizontally across the upper third of the page. Implemented as SVG or a large background image — not a flat CSS gradient (the real mesh has organic blob shapes).

**Composited Dashboard Mockup** — multi-layer faux-product-UI compositions: an IDE panel on the left, a dashboard table center, a chart card on the right, all rendered at small scale inside `{rounded.lg}` containers with subtle Level 2 shadows. The composite is the brand's most-photographed feature.

**Tabular-Figure Money Type** — every number rendering money, count, or transaction value uses `font-feature-settings: "tnum"`. The brand's quiet signal that it's a financial-infrastructure platform.

**`link-on-light`** — inline links on light surfaces.
- Text `{colors.primary}` rendered in `{typography.body-md}`, no underline by default.
- States: default · hover (underline appears, colour to `{colors.primary-deep}`) · focus-visible (`{colors.focus}` ring, 2px offset) · active/pressed (`{colors.primary-press}`) · disabled (`{colors.ink-mute}`, no underline) · loading, selected and error — not applicable to an inline link.
- Because the link is set in `{colors.primary}` on white with no underline at rest, it is distinguished from body `{colors.ink}` by hue alone. The two inks differ by 2.5:1 against each other, short of the 3:1 WCAG 1.4.1 asks for colour-only distinction, so underline-on-hover is required and an underline at rest is the safer default.

**`footer-light`** — site-wide footer.
- Background `{colors.canvas}`, text `{colors.ink-mute}`, type `{typography.caption}`, padding `{spacing.huge} {spacing.xl}` (64px 24px). Holds 4–6 columns of link groups, social icons, and a small legal row.
- Footer link states: default (`{colors.ink-mute}`, 4.75:1 on white) · hover (`{colors.ink}`) · focus-visible (`{colors.focus}` ring, 2px offset) · active/pressed · disabled, loading, selected and error — not applicable.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted; they are the **Crisp** profile's shared values, chosen because the brand's identity is financial infrastructure and developer tooling — state change should read as instant, with no entrance choreography in front of content.

Tokens: `{motion.duration-instant}` 60ms · `{motion.duration-fast}` 100ms · `{motion.duration-base}` 150ms · `{motion.duration-slow}` 220ms · `{motion.duration-emphasis}` 300ms · `{motion.ease-standard}` · `{motion.ease-enter}` · `{motion.ease-exit}` · `{motion.stagger-step}` 20ms · `{motion.duration-reduced}` 100ms.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, card, link) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `transform` (shadow swap only on cards) | Colour and shadow change instantly; no transform |
| Press | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed; fill change only |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the `{colors.focus}` ring | Ring appears instantly at full opacity |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` only | `opacity` at `{motion.duration-reduced}` |
| Modal / drawer | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px)` | `opacity` at `{motion.duration-reduced}`; no travel |
| Dropdown (nav menu) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(4px)` | `opacity` at `{motion.duration-reduced}`; no travel |
| Toast | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px)` | `opacity` at `{motion.duration-reduced}`; no travel |
| List enter (pricing tiers, table rows) | `{motion.duration-base}`, staggered `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px)` | Stagger dropped; one `opacity` fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: translateY(4px)` | `opacity` at `{motion.duration-reduced}`; no travel |
| Loading | 900ms linear, infinite | linear | `transform: translateX` on a `{colors.primary-soft}` bar; `opacity` on skeleton rows | Looping motion frozen; a static `{colors.hairline}` skeleton with a text status remains |

Rules this file holds to:

- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin`.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content: the gradient mesh and the hero headline render at full opacity. The mesh is a static image, not an ambient animation.
- No infinite animation except the loading indicator above.
- At `{motion.duration-base}` 150ms, a pill's hover and press read as immediate. Do not stretch these toward the 400ms of an editorial brand — the transactional snap is part of the identity.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all transform — translate, scale and the loading bar's travel. */
  /* Retained: opacity fades, capped at {motion.duration-reduced} 100ms. */
  /* Frozen: the loading bar's infinite loop, replaced by a static skeleton
     plus a text status, so progress is still communicated. */
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;
    transition-property: opacity, background-color, border-color, color !important;
    transform: none !important;
  }
}
```

## Accessibility

### Measured contrast

Computed with WCAG 2.1 relative luminance from this file's own hexes. Failures are stated, not hidden: the extracted values are frozen facts about the real brand.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#0d253d` on `{colors.canvas}` | 15.57:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` | 14.73:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-cream}` | 12.96:1 | 4.5:1 | Pass |
| `{colors.ink-secondary}` on `{colors.canvas}` | 11.73:1 | 4.5:1 | Pass |
| `{colors.ink-mute}` on `{colors.canvas}` | 4.75:1 | 4.5:1 | Pass |
| `{colors.ink-mute}` on `{colors.canvas-soft}` | 4.49:1 | 4.5:1 | **Fail** by 0.01 — 18px+ or 14px-bold labels only on the soft band |
| `{colors.ink-mute}` on `{colors.canvas-cream}` | 3.95:1 | 4.5:1 | **Fail** — the mute ink is not usable for body copy on the cream band; use `{colors.ink-secondary}` (9.77:1) there |
| `{colors.ink-mute-2}` on `{colors.canvas-soft}` | 4.69:1 | 4.5:1 | Pass |
| `{colors.ink-mute-2}` on `{colors.canvas-cream}` | 4.13:1 | 4.5:1 | **Fail** — same restriction as `{colors.ink-mute}` |
| `{colors.on-primary}` on `{colors.primary}` | 6.19:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.brand-dark-900}` | 15.41:1 | 4.5:1 | Pass |
| `{colors.primary}` on `{colors.canvas}` (links, outline button) | 6.19:1 | 4.5:1 | Pass |
| `pill-tag-soft`: `{colors.primary-deep}` on `{colors.primary-bg-subdued-hover}` | 4.23:1 | 4.5:1 | **Fail** — the real brand fails AA on its soft tag. `{colors.primary-press}` on the same fill reaches 6.18:1 |
| `{colors.hairline}` on `{colors.canvas}` | 1.23:1 | 3.0:1 | **Fail** — decorative rule only |
| `{colors.hairline}` on `{colors.canvas-soft}` | 1.17:1 | 3.0:1 | **Fail** — decorative rule only |
| `{colors.hairline}` on `{colors.canvas-cream}` | 1.03:1 | 3.0:1 | **Fail** — effectively invisible; never draw a hairline on cream |
| `{colors.hairline-input}` on `{colors.canvas}` | 1.82:1 | 3.0:1 | **Fail** — the real brand's input boundary does not meet 1.4.11 |
| `{colors.hairline-input}` on `{colors.canvas-soft}` | 1.72:1 | 3.0:1 | **Fail** |
| `{colors.hairline-input}` on `{colors.canvas-cream}` | 1.52:1 | 3.0:1 | **Fail** |
| `{colors.primary}` against `{colors.ink}` (link vs body text) | 2.51:1 | 3.0:1 | **Fail** — links need an underline, not hue alone |

Both hairlines are extracted and frozen, and both fail the 3:1 non-text minimum on every surface this file defines. The brand draws its card and table boundaries, and its form-input outlines, in tones that are not perceivable as boundaries. Nothing here is a token to be "fixed": the palette already owns `{colors.ink-mute}` at 4.75:1 on white and 3.95:1 on cream, which clears 3:1 on all three surfaces, so where a boundary is load-bearing — the extent of a text field, the edge of a selectable card — draw it in `{colors.ink-mute}` and keep `{colors.hairline}` for decorative rules. The frontmatter bindings are left exactly as extracted; re-pointing them is a brand-owner decision, recorded under Needs approval in the audit report.

### Focus ring

- `{colors.focus}` is `#665efd`, the hex `{colors.primary-soft}` already carries. It is not a new brand colour; it is the one indigo in the palette that clears 3:1 against every surface this file defines.
- Drawn as a 2px solid ring at 2px offset **outside** the control, so WCAG 2.2 Focus Appearance measures it against the surface behind the control rather than against the control's own fill. State the offset wherever the ring is specified.
- Measured on each surface: `{colors.canvas}` 4.58:1 · `{colors.canvas-soft}` 4.34:1 · `{colors.canvas-cream}` 3.81:1 · `{colors.brand-dark-900}` 3.36:1. One ring serves all four, so this file defines no second polarity ring.
- Over the gradient mesh, which has no single measurable colour, the ring is drawn two-tone: `{colors.focus}` with a 1px `{colors.on-primary}` outer edge.
- The ring is never removed. `outline: none` without a replacement is a defect in this system.

### Tap targets

Minimum 44×44px for every interactive target, reached by padding rather than by growing the label, so the pill's `8px 16px` box is preserved visually. Nothing in this file measures a rendered target, so these are specifications, not measurements.

### Reduced motion

`@media (prefers-reduced-motion: reduce)` removes all travel and scale and caps retained `opacity` fades at `{motion.duration-reduced}` 100ms; the loading indicator's loop is frozen and replaced with a static skeleton plus a text status. See Motion & Animation.

### Non-colour redundancy

Selection, current-page and error states all pair colour with a second signal — a tag, an underline, a weight change or an icon — because the brand's whole signal vocabulary is indigo on white.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` for filled CTAs and inline link emphasis — it should appear sparingly, one filled button per band.
- Apply the gradient mesh to every marketing hero; bare-canvas heroes feel off-brand.
- Render display tiers at weight 300 with negative letter-spacing — the thin tracking is the typographic signature.
- Use `font-feature-settings: "tnum"` on every money / numeric cell.
- Apply `font-feature-settings: "ss01"` globally on the body element.
- Pair every feature explanation with a composited product UI mockup; the brand's argument is "look at the actual product."

### Don't
- Don't bump display weight above 300 — at 400 the brand's editorial air collapses.
- Don't add new accent colors outside the documented gradient stops (cream / orange / lavender / indigo / ruby / magenta).
- Don't use the indigo `{colors.primary}` as a body-text color — it's a CTA and link color, not a type color at body size.
- Don't shrink button padding below `8px 16px` — the tight pill is part of the brand's transactional feel.
- Don't render money cells without `tnum` — it breaks the quiet financial-data signature.
- Don't replace the pill shape with rounded-rectangles for buttons.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1440px | Full gradient mesh edge-to-edge; dashboard composite at full scale |
| Desktop | 1024–1440px | Default content max-width; pricing 4-up |
| Tablet | 768–1023px | Pricing 2-up; dashboard composite simplifies to 2 panels |
| Mobile | < 768px | Pricing 1-up; hamburger nav; display drops 56 → 36px |

### Touch Targets
- Pill buttons hit ≥ 40×40px on mobile via padding scaling. On smaller screens, buttons size up to 44×44px to maintain WCAG AAA.
- Form fields stay at 40px minimum height.

### Collapsing Strategy
- Display tiers stair-step 56 → 48 → 32 → 26 → 22px through the breakpoints.
- Gradient mesh re-tiles on mobile to preserve the wash without disappearing.
- Dashboard composites simplify to single-panel mockups on mobile; the multi-layer composition only renders at desktop+.
- Pricing tiers stair-step 4-up → 2-up → 1-up.

### Image Behavior
Product UI composites use `srcset` with art-direction crops at major breakpoints. Mobile crops focus on the most actionable inner panel; desktop crops show the full multi-layer composition.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly (`{colors.primary}`, `{button-primary-pill}-pressed`, `{rounded.pill}`).
3. Run `npx @google/design.md lint DESIGN.md` after edits.
4. Add new variants as separate entries.
5. Default body to `{typography.body-md}` (15px); use `{typography.body-tabular}` for any money / numeric cell.
6. Apply `ss01` globally on the body; apply `tnum` per-element on numeric content.
7. The gradient mesh is non-negotiable on marketing heroes — bare-canvas heroes break the brand.

## Known Gaps

- **All motion is prescribed.** Nothing in the Motion & Animation section was measured from the live site. The durations and easings are the audit's shared **Crisp** profile, applied because the brand's identity is financial infrastructure and developer tooling. Treat them as a starting system, not as extracted facts.
- **No semantic colour set.** The brand's marketing palette carries no success / warning / error / info tones. The `error` state specified on `text-input` uses `{colors.ruby}`, which is a gradient and chart accent in the extracted palette, not a documented error colour — it is prescribed. A real semantic ramp lives in the dashboard product UI and was not captured here.
- **`{colors.ink-mute-2}` is a near-duplicate.** `#61718a` sits 0.2:1 from `{colors.ink-mute}` `#64748d`; the two are not distinguishable in use, and the reason the brand carries both is unknown.
- **No shadow tokens.** Elevation & Depth states literal `rgba(0,55,112,...)` values and `{colors.shadow-blue}` `#003770` is the only related token; the three shadow recipes are written as raw CSS in the prose rather than as a `shadow:` group. The elevation ladder is also expressed two ways — box-shadow at Levels 1–2 and a gradient-mesh backdrop at Level 3 — which is deliberate for this brand but means "elevation" does not mean one thing.
- **The dark dashboard track is under-specified.** `{colors.brand-dark-900}` is the only dark surface token, and the dashboard shell's own canvas, surface, hairline and text tones were not extracted. Anything built on the dark track will need values this file does not have.
- **Tap targets and layout behaviour are unverified.** This is a document, not a running UI: the 44×44px minimum, the breakpoint collapse and the mesh re-tiling are specifications. No rendered page was measured.
- **The gradient mesh has no measurable colour.** Contrast of any ink or ring over the mesh cannot be computed from this file. The two-tone focus ring and the white nav fill are the mitigations; the underlying numbers are not knowable here.
