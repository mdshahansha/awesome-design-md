---
version: alpha
name: Meta-design-analysis
description: Meta's design system spans hardware commerce (Quest VR, Ray-Ban Meta AI glasses) and brand surfaces with a confident product-merchandising voice. The system pairs a stark white canvas with full-bleed photographic product cards, a confident Optimistic VF wordmark/headline face, dual-CTA hero patterns (black primary + outlined secondary), and a saturated cobalt blue (#0064E0) for in-product purchase actions. Pill-shaped 100px-radius buttons, generous 24-32px card rounding, and tight three-tier text hierarchy carry across homepage, product detail (PDP), buy-now configurator, and accessory subpages.

colors:
  primary: "#0064e0"
  primary-deep: "#0457cb"
  primary-soft: "#0091ff"
  on-primary: "#ffffff"
  ink-button: "#000000"
  on-ink-button: "#ffffff"
  fb-blue: "#1876f2"
  meta-link: "#385898"
  oculus-purple: "#a121ce"
  success: "#31a24c"
  success-bg: "#24e400"
  attention: "#f2a918"
  warning: "#f7b928"
  warning-bg: "#ffe200"
  critical: "#e41e3f"
  critical-strong: "#f0284a"
  canvas: "#ffffff"
  surface-soft: "#f1f4f7"
  ink-deep: "#0a1317"
  ink: "#1c1e21"
  charcoal: "#444950"
  slate: "#4b4c4f"
  steel: "#5d6c7b"
  stone: "#8595a4"
  hairline: "#ced0d4"
  hairline-soft: "#dee3e9"
  hairline-strong: "#868b92"
  disabled-text: "#bcc0c4"
  focus: "#0064e0"

typography:
  hero-display:
    fontFamily: Optimistic VF
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.16
    fontFeature: "ss01, ss02"
  display-lg:
    fontFamily: Optimistic VF
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.17
    fontFeature: "ss01, ss02"
  heading-lg:
    fontFamily: Optimistic VF
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.28
    fontFeature: "ss01, ss02"
  heading-md:
    fontFamily: Optimistic VF
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.21
    fontFeature: "ss01, ss02"
  heading-sm:
    fontFamily: Optimistic VF
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    fontFeature: "ss01, ss02"
  subtitle-lg:
    fontFamily: Optimistic VF
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.44
  subtitle-md:
    fontFamily: Optimistic VF
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.44
  body-md-bold:
    fontFamily: Optimistic VF
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: -0.16px
  body-md:
    fontFamily: Optimistic VF
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.16px
  body-sm-bold:
    fontFamily: Optimistic VF
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: -0.14px
  body-sm:
    fontFamily: Optimistic VF
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: -0.14px
  caption-bold:
    fontFamily: Optimistic VF
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
  caption:
    fontFamily: Optimistic VF
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
  button-md:
    fontFamily: Optimistic VF
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: -0.14px
  link-md:
    fontFamily: Optimistic VF
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: -0.16px

rounded:
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 16px
  xxl: 24px
  xxxl: 32px
  feature: 40px
  full: 100px
  circle: 9999px

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
  sm: 10px
  md: 12px
  base: 16px
  lg: 20px
  xl: 24px
  xxl: 32px
  xxxl: 40px
  section-sm: 48px
  section: 64px
  section-lg: 80px
  hero: 120px

components:
  button-primary:
    backgroundColor: "{colors.ink-button}"
    textColor: "{colors.on-ink-button}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 30px"
  button-primary-pressed:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-ink-button}"
  button-primary-disabled:
    backgroundColor: "{colors.disabled-text}"
    textColor: "{colors.canvas}"
  button-buy-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 30px"
  button-buy-cta-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink-deep}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 28px"
    border: "2px solid {colors.ink-deep}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink-deep}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 22px"
    border: "2px solid rgba(10, 19, 23, 0.12)"
  button-pill-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-bold}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  button-pill-tab-active:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.canvas}"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
    size: 40px
  card-product-feature:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline-soft}"
  card-feature-photo:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xxxl}"
    padding: "0"
    border: "none"
  card-promo-strip:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.section}"
  card-icon-feature:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  card-checkout-summary:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "rgba(20, 22, 26, 0.3) 0px 1px 4px 0px"
  product-thumbnail:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.base}"
    aspect-ratio: "1 / 1"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline}"
    height: 44px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.fb-blue}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.critical-strong}"
  search-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    height: 40px
  radio-option:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: "1px solid rgba(10, 19, 23, 0.12)"
  radio-option-selected:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    border: "2px solid #0143b5"
  color-swatch-circle:
    rounded: "{rounded.circle}"
    size: 32px
    border: "2px solid {colors.canvas}"
  badge-promo-yellow:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-attention:
    backgroundColor: "{colors.attention}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-critical:
    backgroundColor: "{colors.critical}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  promo-banner:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm-bold}"
    padding: "{spacing.md} {spacing.xl}"
  faq-accordion-item:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  why-buy-tile:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl} {spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  warranty-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xxl}"
    padding: "{spacing.xxl}"
  footer-region:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
    border: "1px solid {colors.hairline-soft}"
  hero-band-marketing:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.canvas}"
    typography: "{typography.hero-display}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.section-lg}"
  product-gallery-pdp:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.base}"
  color-sku-picker-row:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
  feature-icon-row:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  tech-specs-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  testimonial-customer-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline-soft}"
---

## Overview

Meta's commerce surfaces (homepage, Quest configurator, Ray-Ban product detail, prescription page) read as a confident hardware merchandiser. The brand voice is photography-first: large, full-bleed product imagery dominates above-the-fold real estate, with white space and tight typographic hierarchy carrying the rest. The system has a recognizable dual-CTA pattern — a black pill-shaped primary on marketing surfaces shifting to a saturated cobalt blue ({colors.primary}) inside the buy-now flows, paired with an outlined ghost button for secondary navigation.

Optimistic VF — Meta's variable display face — anchors the entire system, ranging from a 64px hero display down to a 12px caption. The face's `ss01` and `ss02` stylistic sets are switched on across every heading role, contributing to the brand's slightly humanist, friendly geometric character. Below 768px the system collapses cleanly: hero stacks, pill nav becomes a hamburger, three-up feature grids flatten to a single column, and product configurators drop their right-rail summary into a sticky bottom bar.

**Key Characteristics:**
- Stark white canvas ({colors.canvas}) carrying full-bleed product photography with `{rounded.xxxl}` (32px) corner softening on showcase tiles
- Two-tier primary button system: marketing CTAs use {colors.ink-button} pills; commerce CTAs use {colors.primary} cobalt pills inside buy-now panels
- Optimistic VF as the universal display + body face with consistent `ss01, ss02` OpenType features
- Pill-shaped buttons ({rounded.full}) and `{rounded.xxxl}`/`{rounded.feature}` cards as the dominant geometric signature
- Saturated promotional banners (yellow {colors.warning}, dark {colors.ink-deep}) used sparingly above the nav for time-bound offers
- Photographic feature cards with no card chrome (no border, no shadow) — the product imagery IS the surface treatment

## Colors

> Source pages: meta.com/ (homepage), /ai-glasses/ray-ban-meta-skyler-gen-2/ (PDP), /quest/quest-3s/buy-now/ (configurator), /ai-glasses/prescription/ (lens upsell). Token coverage was identical across all four pages — the design system is genuinely unified.

### Brand & Accent
- **Cobalt Primary** ({colors.primary}): The buy-now CTA color. Used on every "Add to cart", "Configure", "Pre-order" button inside the commerce flow and the right-rail purchase panel.
- **Deep Cobalt** ({colors.primary-deep}): Pressed-state and dark-surface variant of the cobalt primary; also the active link color.
- **Soft Cobalt** ({colors.primary-soft}): Translucent background tint for informational callouts (`{colors.primary-soft}` at 15% alpha).
- **Facebook Blue** ({colors.fb-blue}): Selected radio/checkbox state and inline form-control activation color.
- **Meta Link Blue** ({colors.meta-link}): Reserved for legacy navigation and footer link affordances.
- **Oculus Purple** ({colors.oculus-purple}): VR product accent — used inside Quest-branded surfaces for category emphasis.

### Surface
- **Canvas White** ({colors.canvas}): Page background and primary card surface.
- **Soft Cloud** ({colors.surface-soft}): Subtle product-thumbnail and warranty-card background; also the search-pill rest state.
- **Hairline Gray** ({colors.hairline}): 1px input border and form-control divider.
- **Hairline Soft** ({colors.hairline-soft}): Quieter divider used on cards, footer separators, and section breaks.
- **Hairline Strong** ({colors.hairline-strong}): **Prescribed, not extracted.** A darkened sibling of {colors.hairline} for any boundary that is the *only* boundary of an interactive control — the `text-input` edge, the `radio-option` edge, the inactive `button-pill-tab` edge. Both extracted hairlines fail the 3:1 non-text contrast minimum (measurements in Accessibility); this token clears it on both grounds the file defines. Scope the two extracted hairlines to decoration: card chrome, footer separators, section breaks, table row rules.

### Focus

- **Focus Cobalt** ({colors.focus}): **Prescribed, not extracted** — no focus ring was captured on these surfaces. The ring is the brand's own cobalt signal, drawn as a 2px solid ring with a 2px offset *outside* the control, so it is judged against the surface behind the control rather than the control's fill. One ring serves all three of this system's surface polarities (measurements in Accessibility), so no `focus-on-dark` companion is needed. Over full-bleed photography, which has no measurable colour, the ring is two-tone: 2px {colors.focus} with a 1px {colors.canvas} outer edge.

### Text
- **Deep Ink** ({colors.ink-deep}): Primary headline and body text on light surfaces.
- **Ink** ({colors.ink}): Standard body and secondary headline text.
- **Charcoal** ({colors.charcoal}): Tertiary body text and form-button labels.
- **Slate** ({colors.slate}): Section-header copy and supporting microcopy.
- **Steel** ({colors.steel}): Quieter caption text and footer link hierarchy.
- **Stone** ({colors.stone}): Disabled or de-emphasized labels.

### Semantic
- **Success** ({colors.success}): "In stock", "Free returns" affirmations.
- **Attention** ({colors.attention}): Mid-priority alerts and timed callouts.
- **Warning** ({colors.warning}): Promotional banners ("Get 25% off…") and limited-time tags.
- **Critical** ({colors.critical}): Validation errors, destructive feedback.
- **Critical Strong** ({colors.critical-strong}): Form-input error border and inline error labels.

## Typography

### Font Family
**Optimistic VF** is Meta's proprietary variable display face. Fallbacks: Montserrat, Helvetica, Arial, Noto Sans. The variable axes carry from 300 (light heading-md, used for editorial intro headlines like "Look forward") through 500 (display, hero, heading-sm) up to 700 (subtitle, body emphasis, button labels). Stylistic sets `ss01` and `ss02` are switched on across every heading role — they soften the geometry and give the type a slightly humanist breathing.

A secondary Helvetica fallback chain is used for technical microcopy (12px) inside spec sheets and footer fine print.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | OpenType | Use |
|---|---|---|---|---|---|---|
| `{typography.hero-display}` | 64px | 500 | 1.16 | 0 | ss01, ss02 | Homepage hero ("Get 25% off…", category opener) |
| `{typography.display-lg}` | 48px | 500 | 1.17 | 0 | ss01, ss02 | Section-opener display ("Made for prescriptions. Built for comfort.") |
| `{typography.heading-lg}` | 36px | 500 | 1.28 | 0 | ss01, ss02 | Subsection headlines ("Why buy from Meta", "Tech specs") |
| `{typography.heading-md}` | 28px | 300 | 1.21 | 0 | ss01, ss02 | Editorial subheads in lighter weight ("Look forward", "Built for prescriptions") |
| `{typography.heading-sm}` | 24px | 500 | 1.25 | 0 | ss01, ss02 | Card titles, feature-tile headers |
| `{typography.subtitle-lg}` | 18px | 700 | 1.44 | 0 | — | Bold callouts, FAQ question titles |
| `{typography.subtitle-md}` | 18px | 400 | 1.44 | 0 | — | Body lead and longer-line subtitles |
| `{typography.body-md}` | 16px | 400 | 1.50 | -0.16px | — | Primary body text |
| `{typography.body-md-bold}` | 16px | 700 | 1.50 | -0.16px | — | Body emphasis and link-md |
| `{typography.body-sm}` | 14px | 400 | 1.43 | -0.14px | — | Secondary body, helper text |
| `{typography.body-sm-bold}` | 14px | 700 | 1.43 | -0.14px | — | Pill tab labels, footer headings |
| `{typography.caption-bold}` | 12px | 700 | 1.33 | 0 | — | Badge labels, timestamps |
| `{typography.caption}` | 12px | 400 | 1.33 | 0 | — | Footer fine print, legal microcopy |
| `{typography.button-md}` | 14px | 700 | 1.43 | -0.14px | — | Pill button labels |
| `{typography.link-md}` | 16px | 700 | 1.50 | -0.16px | — | Inline navigation links |

### Principles
- Negative letter-spacing on body roles (`-0.14px` to `-0.16px`) tightens the type fractionally — Optimistic VF was designed for this snug-but-not-condensed setting.
- Editorial subheads use the 300 weight to introduce visual rest between the 500-weight display headlines and the 400-weight body, creating a three-tier visual rhythm.
- All headings carry `ss01, ss02` stylistic sets together — the design treats them as a paired alternates package, never one without the other.
- Buttons, pill tabs, and footer headings share `{typography.body-sm-bold}` (14px / 700 / -0.14px), creating a tight visual relationship between interactive elements.

## Layout

### Spacing System
- **Base unit**: 4px increment with 8px as the dominant primary step.
- **Tokens**: `{spacing.xxs}` (4px) · `{spacing.xs}` (8px) · `{spacing.sm}` (10px) · `{spacing.md}` (12px) · `{spacing.base}` (16px) · `{spacing.lg}` (20px) · `{spacing.xl}` (24px) · `{spacing.xxl}` (32px) · `{spacing.xxxl}` (40px) · `{spacing.section-sm}` (48px) · `{spacing.section}` (64px) · `{spacing.section-lg}` (80px) · `{spacing.hero}` (120px).
- **Section rhythm**: Marketing sections separate at `{spacing.section-lg}` (80px); product detail sections compress to `{spacing.section}` (64px); FAQ stacks tighten further to `{spacing.xxl}` (32px).
- **Card internal padding**: Standard `{spacing.xxl}` (32px); icon-feature tiles compress to `{spacing.xl}` (24px); promo-strip cards expand to `{spacing.section}` (64px) for hero presence.

### Grid & Container
- Marketing page max-width sits around 1280px with 32–48px gutters.
- The PDP layout uses a 2-column split: hero gallery (~58% width) + sticky purchase rail (~42%, with `max-width: 380px` on the rail).
- Three-up feature grids ("Why buy from Meta") use a 24px column gap; six-up product thumbnail rows (color/SKU pickers) use a 12px gap.

### Whitespace Philosophy
Whitespace is product-photography-first. Hero sections give product imagery 50–70% of the viewport height; copy is given oxygen to breathe in `{spacing.xxl}` to `{spacing.xxxl}` blocks above and below. Inside the configurator, whitespace tightens — the buy-now panel is information-dense, with `{spacing.base}` to `{spacing.lg}` rhythm between option groups.

## Elevation & Depth

The system runs predominantly flat. Elevation is reserved for two interaction layers:

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow; `{rounded.xxxl}` rounding + `{colors.hairline-soft}` border | Default product cards, why-buy tiles |
| 1 (subtle) | `rgba(0, 0, 0, 0.2) 1px 1px 0px 0px` | Pill-tab activation indicator |
| 2 (sticky panel) | `rgba(20, 22, 26, 0.3) 0px 1px 4px 0px` | PDP right-rail purchase summary, sticky mobile checkout bar |

### Decorative Depth
- Photography-as-depth: full-bleed product imagery on `{rounded.xxxl}` cards creates atmospheric layering without shadows.
- Translucent overlays (`rgba(255, 255, 255, 0.1)` to `rgba(10, 19, 23, 0.12)`) cover dark hero photography to lift legibility of overlaid text.
- Decorative pastel tints inside accessory cards — soft pink, ice-blue, mint — appear briefly behind product cutouts but are NOT formalized as system tokens (treated as photographic content).

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | Inline checkbox marks, fine UI corners |
| `{rounded.sm}` | 4px | Tags, micro-controls |
| `{rounded.md}` | 6px | Square thumbnail rounding |
| `{rounded.lg}` | 8px | Form inputs, radio-option containers |
| `{rounded.xl}` | 16px | Standard feature cards, FAQ accordion items |
| `{rounded.xxl}` | 24px | Warranty / accessory tiles, ghost-style action cards |
| `{rounded.xxxl}` | 32px | Photographic feature cards, big promo strips |
| `{rounded.feature}` | 40px | Accessory hero panels, "Built for prescriptions" cards |
| `{rounded.full}` | 100px | Pill buttons, tab chips, badges |
| `{rounded.circle}` | 50% | Color swatches, circular icon buttons |

### Photography Geometry
- Product hero photography sits in `{rounded.xxxl}` (32px) frames more often than rectangles.
- Color/material swatches are perfect circles (`{rounded.circle}`, 32px diameter, 2px white border ring when selected).
- Square product thumbnails (`aspect-ratio: 1/1`) use `{rounded.xl}` rounding.
- Six-up "color & SKU" picker rows use 1:1 aspect tiles with `{rounded.lg}` (8px) corners — tighter than the hero photography frames to differentiate selection-grid context from showcase context.

## Components

> Pressed, disabled, selected and error states below are extracted from the captured surfaces. Hover, focus-visible and loading states were **not** captured (the pages were read statically) and are therefore **prescribed** in the state matrix below, consistent with the pressed states that were extracted. The earlier "no-hover policy" note in this file was a capture gap described as a policy; Meta's commerce surfaces do have hover affordances.

### State Matrix

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | yes | yes — fill lifts to `{colors.charcoal}` | yes — 2px `{colors.focus}` ring, 2px offset | yes — `button-primary-pressed` | yes — `button-primary-disabled` | yes — label swaps for a spinner, width locked | n/a | n/a |
| `button-buy-cta` | yes | yes — fill deepens toward `{colors.primary-deep}` | yes — 2px `{colors.focus}` ring, 2px offset | yes — `button-buy-cta-pressed` | yes — `{colors.disabled-text}` fill | yes — "Adding…" spinner during cart POST | n/a | n/a |
| `button-secondary` / `button-ghost` | yes | yes — border darkens to `{colors.ink-deep}` | yes — 2px `{colors.focus}` ring, 2px offset | yes — border weight holds, label drops to `{colors.charcoal}` | yes — border and label at `{colors.disabled-text}` | n/a | n/a | n/a |
| `button-pill-tab` | yes | yes — border steps to `{colors.hairline-strong}` | yes — 2px `{colors.focus}` ring, 2px offset | yes | n/a | n/a | yes — `button-pill-tab-active` | n/a |
| `button-icon-circular` | yes | yes — `{colors.surface-soft}` fill appears | yes — 2px `{colors.focus}` ring, 2px offset | yes — fill holds, icon to `{colors.ink-deep}` | yes | n/a | n/a | n/a |
| `text-input` | yes | yes — border steps to `{colors.hairline-strong}` | yes — `text-input-focused`, 2px `{colors.fb-blue}` inner border plus the `{colors.focus}` ring | n/a | yes — `{colors.surface-soft}` fill, `{colors.disabled-text}` label | n/a | n/a | yes — `text-input-error` |
| `search-pill` | yes | yes — fill lightens to `{colors.canvas}` with a `{colors.hairline-strong}` border | yes — 2px `{colors.focus}` ring, 2px offset | n/a | n/a | yes — inline spinner replaces the search glyph | n/a | n/a |
| `radio-option` | yes | yes — border steps to `{colors.hairline-strong}` | yes — 2px `{colors.focus}` ring, 2px offset | yes | yes — label at `{colors.disabled-text}` | n/a | yes — `radio-option-selected` | yes — border to `{colors.critical-strong}` |
| `color-swatch-circle` | yes | yes — ring grows 1px | yes — 2px `{colors.focus}` ring outside the 2px `{colors.canvas}` ring | yes | yes — 40% opacity, diagonal rule for out-of-stock | n/a | yes — 2px `{colors.canvas}` ring | n/a |
| `card-product-feature` / `card-feature-photo` / `why-buy-tile` | yes | yes — 1.02 scale on the image only, border to `{colors.hairline}` | yes — 2px `{colors.focus}` ring, 2px offset on the whole card when linked | n/a | n/a | yes — `{colors.surface-soft}` skeleton block in the image slot | n/a | n/a |
| `faq-accordion-item` | yes | yes — chevron darkens to `{colors.ink}` | yes — 2px `{colors.focus}` ring, 2px offset on the question row | yes — chevron rotates 180° | n/a | n/a | yes — expanded item keeps the chevron rotated | n/a |
| `badge-promo-yellow` / `badge-attention` / `badge-success` / `badge-critical` | yes | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| `product-thumbnail` | yes | yes — border appears in `{colors.hairline}` | yes — 2px `{colors.focus}` ring, 2px offset | yes | n/a | yes — `{colors.surface-soft}` skeleton until the image decodes | yes — 2px `{colors.ink-deep}` border | n/a |
| `tech-specs-table` / `testimonial-customer-card` / `promo-banner` / `footer-region` | yes | n/a (static content) | n/a | n/a | n/a | n/a | n/a | n/a |

Badges and the static content blocks above genuinely have one state each — they are non-interactive, so hover, focus-visible, pressed, disabled, loading, selected and error do not apply to them.

### Buttons

**`button-primary`** — Black pill primary CTA for marketing surfaces ("Shop", "Pre-order").
- Background `{colors.ink-button}`, text `{colors.on-ink-button}`, typography `{typography.button-md}`, padding `14px 30px`, rounded `{rounded.full}`.
- Pressed state `button-primary-pressed` flips background to `{colors.charcoal}`.
- Disabled state `button-primary-disabled` uses `{colors.disabled-text}` background.

**`button-buy-cta`** — Cobalt pill primary CTA for commerce flows ("Add to cart", "Configure", "Continue").
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.button-md}`, padding `14px 30px`, rounded `{rounded.full}`.
- Pressed state `button-buy-cta-pressed` deepens background to `{colors.primary-deep}`.
- This variant ONLY appears inside the buy-now configurator and PDP purchase rail. Marketing surfaces use `button-primary` instead.

**`button-secondary`** — Outlined ghost CTA, often paired with primary in dual-CTA hero patterns.
- Background transparent, text `{colors.ink-deep}`, border `2px solid {colors.ink-deep}`, typography `{typography.button-md}`, padding `12px 28px`, rounded `{rounded.full}`.

**`button-ghost`** — Quieter outlined variant used for tertiary CTAs.
- Background transparent, text `{colors.ink-deep}`, border `2px solid rgba(10, 19, 23, 0.12)`, typography `{typography.button-md}`, padding `10px 22px`, rounded `{rounded.full}`.

**`button-pill-tab`** + **`button-pill-tab-active`** — Top-of-page category navigation pills ("Glasses / Quest / Apps").
- Inactive: background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline}`, padding `8px 16px`, rounded `{rounded.full}`.
- Active: background `{colors.ink-deep}`, text `{colors.canvas}`. No border in active state — the dark fill replaces it.

**`button-icon-circular`** — 40×40px circular utility buttons (carousel arrows, share, favorite).
- Background `{colors.canvas}`, icon color `{colors.ink}`, rounded `{rounded.circle}`.

### Cards & Containers

**`card-product-feature`** — White feature card with product photography and copy (homepage "Designed for sport", "Advanced. Inside and out.").
- Background `{colors.canvas}`, rounded `{rounded.xxxl}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline-soft}`.

**`card-feature-photo`** — Edge-to-edge photographic showcase tile with NO chrome (homepage "Built for prescriptions" full-bleed glasses card).
- Background `{colors.canvas}` (visible only at the corners), rounded `{rounded.xxxl}`, no padding, no border. The image fills the card; copy is overlaid bottom-left in white.

**`card-promo-strip`** — Dark full-width promo card with embedded copy + CTAs (homepage "Meta Quest brings the magic of virtual reality" wide strip).
- Background `{colors.ink-deep}`, text `{colors.canvas}`, rounded `{rounded.xxxl}`, padding `{spacing.section}`.

**`card-icon-feature`** — Three-up feature tile with line icon, headline, and short copy ("Free 2-day delivery", "Free 30-day returns", "Worry-free warranty", "Buy now, pay later").
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xl}`, border `1px solid {colors.hairline-soft}`.

**`card-checkout-summary`** — PDP right-rail sticky summary with title, price, color picker, "Add to cart" button.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xl}`, border `1px solid {colors.hairline-soft}`, shadow `rgba(20, 22, 26, 0.3) 0px 1px 4px 0px`.

**`product-thumbnail`** — Square product image cell used in color/SKU pickers and "People also bought" rows.
- Background `{colors.surface-soft}`, rounded `{rounded.xl}`, padding `{spacing.base}`, aspect-ratio `1 / 1`.

**`warranty-card`** — Promo callout for warranty + finance offers ("1y Warranty", "Meta Horizon+").
- Background `{colors.surface-soft}`, rounded `{rounded.xxl}`, padding `{spacing.xxl}`. Uses pastel-tinted variants for additional perks.

**`why-buy-tile`** — 4-up reassurance tile row in the lower marketing zone.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xxl} {spacing.xl}`, border `1px solid {colors.hairline-soft}`. Heading in `{typography.subtitle-lg}`, body in `{typography.body-sm}`.

### Inputs & Forms

**`text-input`** — Standard form field (footer email subscribe, support form).
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline}`, rounded `{rounded.lg}`, padding `{spacing.md}`, height 44px.

**`text-input-focused`** — Activated state.
- Border switches to `2px solid {colors.fb-blue}`.

**`text-input-error`** — Validation error state.
- Border switches to `1px solid {colors.critical-strong}`; error label below in `{colors.critical-strong}` `{typography.body-sm}`.

**`search-pill`** — Top-nav search field.
- Background `{colors.surface-soft}`, text `{colors.steel}`, typography `{typography.body-sm}`, rounded `{rounded.full}`, height 40px.

**`radio-option`** + **`radio-option-selected`** — Configurator option cards (storage, color variant, shipping option).
- Inactive: background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.lg}`, border `1px solid rgba(10, 19, 23, 0.12)`.
- Selected: border switches to `2px solid #0143b5` (deep cobalt) — the cobalt theme persists into form-control selection signaling.

**`color-swatch-circle`** — Round color/material picker (Ray-Ban frame finishes, glass colors).
- 32px diameter, `{rounded.circle}`, `2px solid {colors.canvas}` ring on selection over the swatch's own fill color.

### Badges & Status

**`badge-promo-yellow`** — Limited-time offer chip ("Limited time", "Sale").
- Background `{colors.warning}`, text `{colors.ink-deep}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-attention`** — Mid-priority status indicator ("Almost gone", "Selling fast").
- Background `{colors.attention}`, text `{colors.canvas}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-success`** — Affirmative status ("In stock", "Verified", "Free shipping").
- Background `{colors.success}`, text `{colors.canvas}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-critical`** — Urgent/destructive label ("Out of stock", "Discontinued", error chips).
- Background `{colors.critical}`, text `{colors.canvas}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`promo-banner`** — Sticky full-width promotional strip ABOVE the top nav ("Get 25% off the #1 selling AI glasses").
- Background `{colors.ink-deep}` (or `{colors.warning}` for yellow promo variants), text `{colors.canvas}` (or `{colors.ink-deep}` on yellow), typography `{typography.body-sm-bold}`, padding `{spacing.md} {spacing.xl}`. Carries one-line offer copy plus an inline CTA link.

### Navigation

**Top Navigation (Desktop)** — Sticky white bar with category pill tabs, search, account, cart.
- Background `{colors.canvas}`, height ~64px with bottom `1px solid {colors.hairline-soft}`.
- Left: Meta wordmark logo (61×14px). Center: pill-tab category nav. Right: search-pill + circular icon buttons (account, cart).

**Top Navigation (Mobile)** — Compressed to logo + hamburger + cart icon. Pill-tab nav slides into a full-screen drawer below 768px.

**Promo Banner** — Full-width strip ABOVE the nav for time-bound offers.
- Background `{colors.ink-deep}` or `{colors.warning}` (yellow), text `{colors.canvas}` or `{colors.ink-deep}`, typography `{typography.body-sm-bold}`, padding `{spacing.md} {spacing.xl}`. Carries one-line offer copy + inline link.

**Breadcrumb (PDP)** — Inline path above the product hero ("Glasses › Ray-Ban Meta › Skyler (Gen 2)").
- Typography `{typography.body-sm}`, separator dot in `{colors.stone}`, active leaf in `{colors.ink}`, parent links in `{colors.steel}`.

### Signature Components

**`hero-band-marketing`** — Full-bleed photographic hero with overlaid copy + dual-CTA pair.
- Edge-to-edge product photography on a dark or photographic background. Overlay copy in `{typography.hero-display}` white. Below the title: 1-line subtitle in `{typography.subtitle-md}` then `button-primary` + `button-secondary` pair.
- The declared ground for this component is `{colors.ink-deep}`, not `{colors.canvas}`. The hero's actual ground is a photograph, which has no measurable colour; the file's own Elevation & Depth section records that dark hero photography carries a translucent darkening overlay to lift overlaid text. `{colors.ink-deep}` is the darkest ground this file documents and is the ground every other white-on-dark component in the system binds (`card-promo-strip`, `promo-banner`, `button-pill-tab-active`), so the hero is declared against it: white on `{colors.ink-deep}` measures 18.78:1. Requirement for implementers: the photographic ground under hero type must be darkened to at least the luminance of `{colors.ink-deep}` within the type's footprint. Over an undarkened photograph the ratio is not measurable — see Known Gaps.

**`product-gallery-pdp`** — Product detail page main hero: 4-up vertical thumbnail strip on the left, large product image center, sticky purchase rail right.
- Thumbnails: 80×80px, `{rounded.lg}`, `{colors.surface-soft}` background, 1px `{colors.hairline-soft}` border (active border switches to `{colors.ink-deep}`).
- Main image area: ~720×720px on desktop, `{rounded.xxxl}` rounding, photographic surface.
- Sticky rail uses `card-checkout-summary`.

**`color-sku-picker-row`** — Six-up grid of square product variants with name + price below each.
- Tile background `{colors.surface-soft}`, rounded `{rounded.lg}`, image padded `{spacing.base}`. Active tile border switches to `2px solid {colors.ink-deep}`. Below the tile: variant name in `{typography.body-sm-bold}` and price in `{typography.body-sm}`.

**`feature-icon-row`** — Four reassurance benefits ("Free 2-day delivery", "Free 30-day returns", "Worry-free warranty", "Buy now, pay later").
- 4-column grid, each cell uses `card-icon-feature` chrome with a 32px line icon at top, headline `{typography.subtitle-lg}`, body `{typography.body-sm}`.

**`faq-accordion`** — Vertical stack of expandable Q&A items.
- Each item uses `faq-accordion-item` chrome. Question in `{typography.subtitle-lg}` left, chevron icon (`{colors.steel}`, 20px) right. Expanded answer drops in `{typography.body-md}` text below with `{spacing.base}` top padding.

**`tech-specs-table`** — Two-column key/value table for product specifications.
- Row layout: spec label (`{typography.body-sm-bold}` `{colors.ink}`) left, spec value (`{typography.body-sm}` `{colors.charcoal}`) right. Row separator `1px solid {colors.hairline-soft}`. Section headers in `{typography.heading-sm}` above each spec group.

**`testimonial-customer-card`** — Small editorial card with author + quote + photo.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline-soft}`. Avatar circle 40px, byline in `{typography.body-sm-bold}`, quote in `{typography.body-md}`.

**`footer-region`** — Dense multi-column site footer.
- Background `{colors.canvas}`, top border `1px solid {colors.hairline-soft}`, padding `{spacing.section} {spacing.xxl}`. Six column groups with section headings in `{typography.body-sm-bold}` `{colors.ink}` and link lists in `{typography.body-sm}` `{colors.steel}`. Bottom row contains language picker, region selector, legal links in `{typography.caption}` `{colors.stone}`.

## Motion & Animation

This motion system is **prescribed to match the brand's visual identity and was not measured from the live site** — no timing function, duration or choreography below was extracted from meta.com. It is the **Cinematic** profile, assigned because the identity is hardware-flagship (Quest VR, Ray-Ban Meta glasses) and the file's own evidence is the Cinematic tell: full-bleed product photography given 50–70% of viewport height, sparse `{typography.hero-display}` type over it, and photography-as-depth instead of shadow. The white canvas does not argue against it.

Duration and easing tokens live in the `motion:` group: `{motion.duration-instant}` (120ms), `{motion.duration-fast}` (240ms), `{motion.duration-base}` (400ms), `{motion.duration-slow}` (600ms), `{motion.duration-emphasis}` (900ms), `{motion.ease-standard}`, `{motion.ease-enter}`, `{motion.ease-exit}`, `{motion.stagger-step}` (80ms), `{motion.duration-reduced}` (150ms).

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, pill tabs, cards) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `transform: scale(1.02)` on card imagery only | Scale removed; `opacity` only at `{motion.duration-reduced}` |
| Press (all pills and controls) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)`, `opacity` | Scale removed; fill change applied with no transition |
| Focus (ring appearance) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring | Ring appears instantly, no transition — never suppressed |
| Page / route transition (PDP ↔ configurator) | enter `{motion.duration-slow}`, exit `{motion.duration-base}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(16px)` | Travel removed; cross-fade at `{motion.duration-reduced}` |
| Modal / drawer (mobile nav drawer, size guide) | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateX(100%)` (drawer) / `scale(0.96)` (modal) | Travel and scale removed; `opacity` only at `{motion.duration-reduced}` |
| Dropdown (account menu, region selector) | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px)` | Travel removed; `opacity` only at `{motion.duration-reduced}` |
| Toast ("Added to cart") | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(12px)` | Travel removed; `opacity` only at `{motion.duration-reduced}` |
| List enter (feature grids, `color-sku-picker-row`, FAQ stack) | `{motion.duration-base}` per item, `{motion.stagger-step}` between items, capped at 6 items | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px)` | Stagger and travel removed; all items fade together at `{motion.duration-reduced}` |
| List exit (filter change, variant swap) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Scale removed; `opacity` only at `{motion.duration-reduced}` |
| Loading (cart POST, image skeleton) | `{motion.duration-emphasis}` loop, infinite | `{motion.ease-standard}` | `opacity` pulse on the `{colors.surface-soft}` skeleton; `transform: rotate()` on the button spinner | Spinner rotation frozen; skeleton holds a static `{colors.surface-soft}` block, no pulse |

### Motion Rules

- `transform` and `opacity` only. Never `width`, `height`, `top`, `left` or `margin` — the hero photography scales with `transform`, never by animating its box.
- Every exit is shorter than its matching entrance (600→400 page, 400→240 modal, 240→120 dropdown, 400→240 toast, 400→240 list).
- Nothing animates on first paint in a way that delays content: the hero image and its type render immediately; the `{motion.stagger-step}` list reveal applies only to grids below the fold.
- The only infinite animations are the two loaders above. This system has no brand ambience loop.
- Hero photography is the one place the Cinematic signature is explicit: a 1.02→1.00 `transform: scale` settle over `{motion.duration-emphasis}` with `{motion.ease-enter}`, with the `{typography.hero-display}` type arriving `{motion.stagger-step}` after it.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate, all scale, all rotate, all stagger delays,
     and the hero photography settle. */
  /* Removed: the loading skeleton's opacity pulse and the spinner's rotation,
     which are frozen to a static state. */
  /* Kept: opacity fades only, at {motion.duration-reduced} (150ms), which is
     shorter than this profile's own {motion.duration-fast} (240ms). */
  /* Kept at full strength and never suppressed: the {colors.focus} ring. */
  *, *::before, *::after {
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important;
    transition-property: opacity !important;
    scroll-behavior: auto !important;
  }
}
```

## Accessibility

### Measured contrast — key pairs

All ratios below are computed with WCAG 2.1 relative luminance from this file's own frontmatter hexes.

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 16.71:1 | 4.5:1 | Pass |
| `{colors.ink-deep}` on `{colors.canvas}` | 18.78:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-soft}` | 15.13:1 | 4.5:1 | Pass |
| `{colors.charcoal}` on `{colors.canvas}` | 9.07:1 | 4.5:1 | Pass |
| `{colors.slate}` on `{colors.canvas}` | 8.59:1 | 4.5:1 | Pass |
| `{colors.steel}` on `{colors.canvas}` | 5.39:1 | 4.5:1 | Pass |
| `{colors.steel}` on `{colors.surface-soft}` | 4.88:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 5.39:1 | 4.5:1 | Pass |
| `{colors.on-ink-button}` on `{colors.ink-button}` | 21.0:1 | 4.5:1 | Pass |
| `{colors.canvas}` on `{colors.ink-deep}` (promo strip, hero band) | 18.78:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 3.43:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.surface-soft}` | 3.11:1 | 3.0:1 | Pass |
| `{colors.ink-deep}` on `{colors.warning}` (yellow promo badge) | 10.66:1 | 4.5:1 | Pass |
| `{colors.critical}` on `{colors.canvas}` | 4.61:1 | 4.5:1 | Pass |

### Where this brand genuinely fails AA

These are extracted, frozen brand values. They are disclosed here rather than corrected, because the document's job is to be true about the brand:

- `hairline` (#ced0d4) on `canvas` measures **1.54:1** against the 3:1 non-text minimum. It is the only boundary of `text-input` and of `button-pill-tab` in its inactive state, so at those two points **the real Meta commerce UI fails WCAG 1.4.11**. Use `{colors.hairline-strong}` for control boundaries; keep `hairline` for decoration.
- `hairline` (#ced0d4) on `surface-soft` measures **1.40:1** against the 3:1 minimum. Same disposition.
- `hairline-soft` (#dee3e9) on `canvas` measures **1.29:1** against the 3:1 minimum. This tone is card chrome and footer separators only, where no boundary contrast is required, so the failure is cosmetic — but it must not be used as a control edge.
- `hairline-soft` (#dee3e9) on `surface-soft` measures **1.17:1** against the 3:1 minimum. Same disposition.
- `warning` (#f7b928) on `canvas` measures **1.76:1** against the 4.5:1 text minimum. This tone is a *fill* — promo-banner and badge backgrounds carrying `{colors.ink-deep}` type at 10.66:1 — and is never drawn as text. Do not use it as a text colour.
- `warning-bg` (#ffe200) on `canvas` measures **1.30:1** against the 4.5:1 text minimum. Fill only, same disposition.
- `success-bg` (#24e400) on `canvas` measures **1.73:1** against the 4.5:1 text minimum. Fill only, same disposition.
- `success` (#31a24c) on `canvas` measures **3.28:1** against the 4.5:1 text minimum. This one **is** used as text ("In stock", "Free returns"), so the failure is real: it passes only as large text at 18.66px+ bold or 24px+ regular, which `{typography.body-sm}` (14px) does not satisfy. See Needs approval in the audit report.
- `badge-success` draws `{colors.canvas}` on `{colors.success}` at **3.28:1** against the 4.5:1 minimum for its 12px `{typography.caption-bold}` label. A real failure at the captured size.
- `badge-attention` draws `{colors.canvas}` on `{colors.attention}` at **2.01:1** against the 4.5:1 minimum for its 12px label. The worst text pair in the system; `{colors.ink-deep}` on `{colors.attention}` would measure 9.36:1, which is the fix this document recommends but does not apply, because the white label is the extracted value.
- `stone` (#8595a4) on `canvas` measures 3.07:1. It is scoped in this file to disabled and de-emphasised labels, where WCAG sets no requirement, and to the breadcrumb separator dot, which is decorative. It must not carry informational text.

### Focus ring visibility on every surface this file defines

The ring is `{colors.focus}` (#0064e0), 2px solid, with a 2px offset **outside** the control, so WCAG 2.2 Focus Appearance measures it against the surface behind the control, not against the control's own fill:

| Surface the ring is drawn on | Ratio vs `{colors.focus}` | Required | Result |
|---|---|---|---|
| `{colors.canvas}` (#ffffff) — pages, cards, inputs, nav | 5.39:1 | 3.0:1 | Pass |
| `{colors.surface-soft}` (#f1f4f7) — thumbnails, warranty cards, search pill | 4.88:1 | 3.0:1 | Pass |
| `{colors.ink-deep}` (#0a1317) — promo strip, promo banner, active pill tab, hero band | 3.49:1 | 3.0:1 | Pass |

One ring covers all three polarities, so this file defines no `focus-on-dark`. Over full-bleed photography the ring is two-tone — 2px `{colors.focus}` with a 1px `{colors.canvas}` outer edge — because a photograph has no measurable colour and neither band can be verified against it.

### Minimum tap target

These are the sizes this document **specifies**, not measurements of a rendered page — no page was rendered for this audit, so no claim here is a verification.

- Specified floor: 44×44px. Pill buttons specify 14px label plus `14px 30px` padding, which the Responsive Behavior section records as a 40–44px effective height.
- `button-icon-circular` and `search-pill` are specified at 40×40px, below the 44px floor, with a documented bump to 44×44px on mobile. On desktop they remain under the floor.
- `color-swatch-circle` is specified at 32×32px with a 12px clear hit zone, giving a specified ~56px target.
- `text-input` is specified at 44px height.

### Reduced motion

Every animation in Motion & Animation respects `@media (prefers-reduced-motion: reduce)`: all travel, scale and rotation are removed, stagger delays collapse to zero, both loaders freeze, and only `opacity` fades remain at `{motion.duration-reduced}` (150ms) — shorter than this profile's own `{motion.duration-fast}` (240ms). The `{colors.focus}` ring is never suppressed or delayed under reduced motion.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (cobalt) for buy-now CTAs only — its visual weight is meaningful precisely because it doesn't appear on marketing pages.
- Use `{colors.ink-button}` (black) for marketing-surface primary CTAs. Pair with the `button-secondary` ghost outline for the secondary action.
- Apply `{rounded.full}` to every button, every category pill, every badge, every chip — buttons are NEVER squared in Meta's system.
- Apply `{rounded.xxxl}` to photographic product cards and `{rounded.xl}` to icon-feature tiles to maintain the visible card-hierarchy contrast.
- Switch on `ss01, ss02` together for any Optimistic VF heading. Never one stylistic set without the other.
- Use the 300-weight `{typography.heading-md}` for editorial subheads — it creates the brand's signature visual rhythm against the 500-weight displays.

### Don't
- Don't use `{colors.primary}` (cobalt) for marketing-surface primary buttons — it conflicts with Meta's brand-history positioning of black-CTA-on-white-canvas marketing.
- Don't introduce additional accent colors beyond cobalt + Oculus purple. The hardware brand is deliberately monochromatic outside its product photography.
- Don't soften the corners of pill buttons below `{rounded.full}`. The pill is a brand signature.
- Don't run feature cards without rounding — `{rounded.xxxl}` is the minimum for any photographic surface.
- Don't reduce `{typography.body-md}` line-height below 1.50 — the negative letter-spacing already tightens the metric and any further compression breaks legibility.
- Don't apply heavy shadows to marketing cards. Elevation is a commerce-flow signal, not a marketing flourish.

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile (small) | < 480px | Single column. Hero text drops to `{typography.display-lg}` or smaller. Pill tabs collapse into hamburger drawer. PDP gallery stacks above purchase rail; rail becomes sticky bottom bar. |
| Mobile (large) | 480 – 767px | Same as small but feature tiles render two-up. |
| Tablet | 768 – 1023px | Two-column feature grids. Pill-tab nav returns. PDP gallery + purchase rail render side-by-side at compressed proportions (~60/40). |
| Desktop | 1024 – 1359px | Full three- and four-up feature grids; full pill-tab category nav; PDP at standard 58/42 split. |
| Wide Desktop | ≥ 1360px | Same as desktop with wider hero gutters and larger product photography. |

### Touch Targets
- Pill buttons render at 40–44px effective height (with the 14px button text + `14px 30px` padding). Above the WCAG AAA 44px floor.
- Circular icon buttons are 40×40px — at the AA floor; bumps to 44×44px on mobile via override.
- Color swatch circles are 32×32px. To hit AAA, the swatch carries a 12px clear hit zone around it (effective hit target ~56px).
- Form inputs render at 44px height to align with primary button height.

### Collapsing Strategy
- **Promo banner** stays full-width on all breakpoints; truncates with ellipsis on small mobile, retains the inline link affordance.
- **Pill-tab nav** below 768px collapses into a hamburger drawer; the active tab is rendered as a label inside the closed nav.
- **PDP layout**: gallery stacks above the purchase summary at < 1024px; the summary becomes a sticky bottom bar with price + "Add to cart" button at < 768px. The full summary remains scrollable above the sticky bar.
- **Feature grids** (3-up, 4-up) collapse to 2-up at 768–1023px and 1-up at < 768px. Card padding compresses from `{spacing.xxl}` to `{spacing.xl}` at the 1-up breakpoint.
- **Hero typography**: `{typography.hero-display}` (64px) drops to `{typography.heading-lg}` (36px) at < 768px and `{typography.heading-sm}` (24px) at < 480px.
- **Footer**: 6-column desktop layout reflows to 2-column at tablet and accordion-collapsed groups at mobile.

### Image Behavior
- Product photography uses 1:1 (thumbnails, color pickers), 4:3 (PDP gallery), and 16:9 (homepage promo strips) ratios.
- Hero photography is full-bleed with `{rounded.xxxl}` corners; lazy-loaded below the fold.
- Product variant images preserve their `{rounded.lg}` thumbnails across all breakpoints — they never go full-width on mobile.

## Iteration Guide

1. Focus on ONE component at a time. The system has high internal consistency — small precision wins compound.
2. Reference component names and tokens directly (`{colors.primary}`, `{component-name}-pressed`, `{rounded.full}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits to catch broken refs, contrast issues, orphaned tokens.
4. Add new variants as separate `components:` entries (`-pressed`, `-disabled`, `-focused`) — do not bury them inside prose.
5. Default to `{typography.body-md}` for body and `{typography.subtitle-lg}` for emphasis. Headlines step down through `hero-display → display-lg → heading-lg → heading-md → heading-sm`.
6. Keep `{colors.primary}` (cobalt) scarce. If it appears outside the buy-now flow on a viewport, ask whether the surface really needs to look like a checkout panel.
7. Pill-shaped buttons (`{rounded.full}`) always; squared buttons signal "third-party widget" in this design language and should be filtered out of any work surface.

## Known Gaps

- Selected/checked states for non-button form controls (toggle, multi-select) were not visible on the captured surfaces — implement following the cobalt-on-white pattern from `radio-option-selected`.
- Animation/transition timings are not extracted. The Motion & Animation section is prescribed from the Cinematic profile and labelled as such; nothing in it is an observed value. An earlier note in this slot recommended 150–250ms ease-out, which was also a guess and is superseded by the profile tokens.
- Hover, focus-visible and loading states were not captured. They are prescribed in the Components state matrix and labelled there.
- The `hero-band-marketing` and `card-feature-photo` grounds are photographs, which have no measurable colour. `hero-band-marketing` is declared against `{colors.ink-deep}` as the darkening requirement its white type depends on; `card-feature-photo` declares no text colour at all, so its white overlaid copy is an undeclared and therefore unmeasured pair. Neither can be verified without a rendered page.
- The focus ring is prescribed, not extracted: no focused control was captured on any of the four source pages.
- Specific dark-mode token values for canvas, surface, ink, and hairline are not defined; the brand has not surfaced a published dark-mode token set on these commerce pages.
- Pastel decorative tints inside accessory cards (soft pink, ice blue, mint) appear visually but are not formalized — treat them as photographic content, not as system colors.
