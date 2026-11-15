---
version: alpha
name: Mistral-AI-design-analysis
description: Mistral AI brands itself with a singular signature — atmospheric sunset gradients (mustard, orange, deep red) layered over photography of mountains, plus a horizontal "sunset stripe" bar that closes every page. The system pairs warm cream-yellow surfaces ({colors.cream}) with a saturated orange primary CTA ({colors.primary}) and uses an elegant near-serif voice for hero displays. Coverage spans homepage (Frontier AI hero), Le Studio product page, Coding solutions, news article surfaces, contact form, and services tier page — all anchored by the signature gradient closing band.

colors:
  primary: "#fa520f"
  primary-deep: "#cc3a05"
  on-primary: "#ffffff"
  sunshine-300: "#ffd06a"
  sunshine-500: "#ffb83e"
  sunshine-700: "#ffa110"
  sunshine-800: "#ff8105"
  sunshine-900: "#ff8a00"
  yellow-saturated: "#ffd900"
  cream: "#fff8e0"
  cream-light: "#fffaeb"
  cream-deeper: "#fff0c2"
  beige-deep: "#e6d5a8"
  block-5: "#ffe295"
  block-6: "#ffd900"
  block-7: "#ff8105"
  ink: "#1f1f1f"
  ink-tint: "#3d3d3d"
  charcoal: "#2c2c2c"
  slate: "#4a4a4a"
  steel: "#6a6a6a"
  stone: "#8a8a8a"
  muted: "#a8a8a8"
  hairline: "#e5e5e5"
  hairline-soft: "#ededed"
  hairline-strong: "#c7c7c7"
  canvas: "#ffffff"
  surface: "#fafafa"
  surface-cream: "#fff8e0"
  surface-cream-soft: "#fffaeb"
  surface-code: "#1c1c1e"
  on-dark: "#ffffff"
  on-dark-muted: "#a8a8a8"
  on-cream: "#1f1f1f"
  footer-cream: "#fff8e0"
  link: "#fa520f"
  focus: "#8f2600"
  focus-on-dark: "#fff8e0"

typography:
  hero-display:
    fontFamily: PP Editorial Old
    fontSize: 84px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-lg:
    fontFamily: PP Editorial Old
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: -1px
  heading-1:
    fontFamily: PP Editorial Old
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  heading-2:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.5px
  heading-3:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
  heading-4:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.30
  heading-5:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.40
  subtitle:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  body-md-medium:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.55
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
  body-sm-medium:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
  caption:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.40
  caption-bold:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.40
  micro:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
  micro-uppercase:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 1px
  button-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30
  stat-display:
    fontFamily: PP Editorial Old
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: -1px
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 20px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  xxl: 32px
  xxxl: 40px
  section-sm: 48px
  section: 64px
  section-lg: 96px
  hero: 120px

shadow:
  flat: "none"
  subtle: "rgba(0, 0, 0, 0.04) 0px 1px 2px 0px"
  card: "rgba(0, 0, 0, 0.04) 0px 4px 12px 0px"
  mockup: "rgba(0, 0, 0, 0.08) 0px 12px 24px -4px"
  modal: "rgba(0, 0, 0, 0.12) 0px 16px 48px -8px"

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
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 20px"
  button-primary-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
  button-cream:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 20px"
    border: "1px solid {colors.beige-deep}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 20px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 20px"
    border: "1px solid {colors.stone}"
  button-on-cream:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 20px"
    border: "1px solid {colors.beige-deep}"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm-medium}"
    padding: "0"
  card-base:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  card-feature:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline-soft}"
  card-cream:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.beige-deep}"
  card-cream-soft:
    backgroundColor: "{colors.surface-cream-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-product:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "{shadow.card}"
  card-photographic:
    backgroundColor: "{colors.surface-code}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "0"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline-soft}"
  pricing-card-featured:
    backgroundColor: "{colors.cream}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.stone}"
    height: 44px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.primary}"
  text-area:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    border: "1px solid {colors.stone}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.primary-deep}"
  field-error-message:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.caption}"
  contact-form-panel:
    backgroundColor: "{colors.cream}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.beige-deep}"
  pill-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm-medium}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    border: "1px solid {colors.hairline}"
  pill-tab-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  segmented-tab:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm-medium}"
    padding: "{spacing.sm} {spacing.md}"
    border: "0 0 2px transparent solid"
  segmented-tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm-medium}"
    border: "0 0 2px {colors.primary} solid"
  badge-orange:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-cream:
    backgroundColor: "{colors.cream-deeper}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm-medium}"
    padding: "{spacing.sm} {spacing.md}"
  hero-band-sunset:
    backgroundColor: "{colors.sunshine-700}"
    textColor: "{colors.ink}"
    rounded: "0"
    padding: "{spacing.hero}"
  sunset-stripe-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "0"
    padding: "{spacing.lg} 0"
  cta-banner-cream:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.section}"
  code-block:
    backgroundColor: "{colors.surface-code}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  code-block-header:
    backgroundColor: "{colors.surface-code}"
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.md}"
    border: "0 0 1px rgba(255,255,255,0.08) solid"
  feature-icon-tile:
    backgroundColor: "{colors.cream}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    border: "1px solid {colors.beige-deep}"
  industry-tile:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  stat-cell:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.stat-display}"
    padding: "{spacing.lg}"
  customer-testimonial-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline-soft}"
  logo-wall-item:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-md-medium}"
    padding: "{spacing.lg}"
  faq-accordion-item:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "0 0 1px {colors.hairline} solid"
  footer-region:
    backgroundColor: "{colors.footer-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-link:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxs} 0"
  app-store-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
---

## Overview

Mistral AI carries itself with a singular, almost cinematographic visual signature — the homepage opens with "Frontier AI. In your hands." rendered in elegant near-serif display type over a photographic mountain landscape bathed in mustard-orange sunset light. Below the hero, every page closes with the same recognizable element: a horizontal "sunset stripe" gradient band running red→orange→yellow→cream that wraps the foot of the page just above the footer. This stripe is THE brand recognizer — it appears on the homepage, products/studio, solutions/coding, news articles, contact form, and services tier page without exception.

The system pairs PP Editorial Old (a near-serif elegant display face) for hero displays with Inter for everything else (body, headings, UI). Cream-yellow surfaces ({colors.cream}, {colors.surface-cream-soft}) anchor form panels and feature cards; saturated orange ({colors.primary}) carries primary CTAs; the deep mountain photography on the homepage and the dark code mockups inside Le Studio create photographic depth. Cards are rectangular with `{rounded.lg}` (12px) corners — distinctly less playful than Miro's or Mintlify's pill-buttons-everywhere approach. Buttons are also `{rounded.md}` (8px), not pills — Mistral's geometry is more sober and editorial than its peers.

**Key Characteristics:**
- Atmospheric mountain-sunset hero photography (orange-red-yellow gradient sky)
- Horizontal "sunset stripe" band ({colors.primary} → {colors.sunshine-700} → {colors.yellow-saturated} → {colors.cream}) at every page bottom
- Cream-yellow surfaces ({colors.cream}, {colors.cream-light}) for form panels and feature cards
- PP Editorial Old (or similar near-serif) for hero displays; Inter for everything else
- `{rounded.md}` (8px) buttons and `{rounded.lg}` (12px) cards — less playful, more editorial geometry
- Saturated orange primary CTA ({colors.primary}) carries every action call

## Colors

> Source pages: mistral.ai/ (homepage), /products/studio (Le Studio product), /solutions/coding (coding solution), /news/vibe-remote-agents-mistral-medium-3-5 (news), /contact (contact form), /services (services tiers). Token coverage was identical across all six pages.

### Brand & Accent
- **Mistral Orange** ({colors.primary}): Primary CTA color, brand orange
- **Orange Deep** ({colors.primary-deep}): Pressed-state and emphasis variant
- **Sunshine 300** ({colors.sunshine-300}): Atmospheric light orange-yellow
- **Sunshine 500** ({colors.sunshine-500}): Mid-spectrum sunset orange
- **Sunshine 700** ({colors.sunshine-700}): Saturated mid sunset gradient stop
- **Sunshine 800** ({colors.sunshine-800}): Deep sunset gradient stop
- **Sunshine 900** ({colors.sunshine-900}): Deepest sunset orange
- **Yellow Saturated** ({colors.yellow-saturated}): Pure brand yellow used in the sunset stripe gradient
- **Block 5/6/7** ({colors.block-5}, {colors.block-6}, {colors.block-7}): Spectrum stops along the sunset gradient (light-yellow → mid-yellow → deep-orange)

### Cream / Neutral Warm
- **Cream** ({colors.cream}): Warm yellow-cream surface for form panels, feature cards, footer
- **Cream Soft** ({colors.cream-light}): Lighter cream variant
- **Cream Deeper** ({colors.cream-deeper}): More-saturated cream for badge/tag chips
- **Beige Deep** ({colors.beige-deep}): Cream surface 1px border color

### Surface
- **Canvas White** ({colors.canvas}): Page background and card surface
- **Surface** ({colors.surface}): Subtle quieter background
- **Surface Cream** ({colors.surface-cream}): Cream-yellow tinted surface
- **Surface Code** ({colors.surface-code}): Dark code-block / IDE mockup surface
- **Hairline** ({colors.hairline}): 1px borders — **decorative only** (1.26:1 on {colors.canvas}); not the sole boundary of a control
- **Hairline Soft** ({colors.hairline-soft}): Quieter dividers — **decorative only** (1.17:1 on {colors.canvas})
- **Hairline Strong** ({colors.hairline-strong}): Card and panel border (1.69:1 on {colors.canvas}) — extracted and frozen, below the 3:1 non-text minimum
- **Stone as control boundary** ({colors.stone}): where a 1px border is the *only* boundary of an interactive control (text input, text area, outlined button), use {colors.stone} — 3.45:1 on {colors.canvas}, 3.31:1 on {colors.surface}. The hex is extracted; this *use* of it is prescribed, because no extracted hairline tone reaches 3:1.

### Text
- **Ink** ({colors.ink}): Primary headlines and body text
- **Ink Tint** ({colors.ink-tint}): Slightly softer black for hero overlay text
- **Charcoal** ({colors.charcoal}): Body emphasis
- **Slate** ({colors.slate}): Secondary text
- **Steel** ({colors.steel}): Tertiary text, captions
- **Stone** ({colors.stone}): Muted labels
- **Muted** ({colors.muted}): Disabled text and placeholders **only** (2.38:1 on {colors.canvas} — below AA for body text). Secondary and tertiary prose uses {colors.slate} (8.86:1) and {colors.steel} (5.41:1), both of which pass.
- **On Dark** ({colors.on-dark}): White text on dark surfaces
- **On Dark Muted** ({colors.on-dark-muted}): Reduced-opacity white
- **On Cream** ({colors.on-cream}): Ink text on cream surfaces

### Semantic
- **Link** ({colors.link}): Inline link color (matches primary orange)

### Focus
Prescribed, not extracted — mistral.ai ships no visible custom focus ring, so these two values are added by this audit and tuned to the palette.

- **Focus** ({colors.focus}, `#8f2600`): the deep red end of the sunset gradient. Default ring on every light and warm ground: 8.59:1 on {colors.canvas}, 8.23:1 on {colors.surface}, 8.08:1 on {colors.surface-cream}, 6.21:1 on {colors.yellow-saturated}, 4.24:1 on {colors.sunshine-700}.
- **Focus On Dark** ({colors.focus-on-dark}, reusing the brand cream `#fff8e0`): ring on dark and saturated grounds — 16.01:1 on {colors.surface-code}, 15.51:1 on {colors.ink}, 3.15:1 on {colors.primary}. The brand needs this second ring because {colors.focus} reaches only 2.57:1 on the orange `sunset-stripe-band`.
- **Geometry**: 2px ring, drawn *outside* the control with a 2px offset, so it is measured against the surface behind the control rather than the control's own fill (WCAG 2.2 Focus Appearance). Radius follows the control's own `{rounded.*}` token.
- **Over the sunset bands and full-bleed photography**, which have no single measurable colour, the ring is two-tone: a 2px {colors.focus} core with a 1px {colors.focus-on-dark} outer edge. At least one tone clears 3:1 on every band stop ({colors.focus} 4.24:1 on {colors.sunshine-700}; {colors.focus-on-dark} 3.15:1 on {colors.primary}).

## Typography

### Font Family
**PP Editorial Old** (display): Mistral's signature near-serif elegant display typeface used for hero displays, large numbers, and editorial section openers. Carries a slightly classical, intelligent character that contrasts the contemporary product positioning. Fallbacks: 'Times New Roman', Georgia, serif.

**Inter** (UI prose): Variable typeface for body, navigation, buttons, labels, captions. Fallbacks: ui-sans-serif, system-ui, -apple-system, sans-serif.

**JetBrains Mono** (code): Monospace for code blocks and IDE mockups. Fallbacks: 'SF Mono', Menlo, Consolas, monospace.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Family | Use |
|---|---|---|---|---|---|---|
| `{typography.hero-display}` | 84px | 400 | 1.05 | -1.5px | PP Editorial Old | Hero ("Frontier AI. In your hands.") |
| `{typography.display-lg}` | 64px | 400 | 1.10 | -1px | PP Editorial Old | Section openers |
| `{typography.heading-1}` | 52px | 400 | 1.15 | -0.5px | PP Editorial Old | Page headlines ("Get in touch with the team.") |
| `{typography.stat-display}` | 56px | 400 | 1.10 | -1px | PP Editorial Old | Stat callouts ("75%") |
| `{typography.heading-2}` | 36px | 500 | 1.20 | -0.5px | Inter | Subsection headlines |
| `{typography.heading-3}` | 28px | 500 | 1.25 | 0 | Inter | Card titles |
| `{typography.heading-4}` | 22px | 500 | 1.30 | 0 | Inter | Feature tile titles |
| `{typography.heading-5}` | 18px | 500 | 1.40 | 0 | Inter | Smaller card titles |
| `{typography.subtitle}` | 18px | 400 | 1.50 | 0 | Inter | Hero subtitle, lead body |
| `{typography.body-md}` | 16px | 400 | 1.55 | 0 | Inter | Primary body text |
| `{typography.body-md-medium}` | 16px | 500 | 1.55 | 0 | Inter | Body emphasis |
| `{typography.body-sm}` | 14px | 400 | 1.50 | 0 | Inter | Secondary body |
| `{typography.body-sm-medium}` | 14px | 500 | 1.50 | 0 | Inter | Active sidebar, button labels |
| `{typography.caption}` | 13px | 400 | 1.40 | 0 | Inter | Helper text |
| `{typography.caption-bold}` | 13px | 600 | 1.40 | 0 | Inter | Badge labels |
| `{typography.micro}` | 12px | 500 | 1.40 | 0 | Inter | Footer microcopy |
| `{typography.micro-uppercase}` | 11px | 600 | 1.40 | 1px | Inter | Section eyebrows |
| `{typography.button-md}` | 14px | 500 | 1.30 | 0 | Inter | Button labels |
| `{typography.code-md}` | 14px | 400 | 1.50 | 0 | JetBrains Mono | Code blocks |

### Principles
- **Editorial / sans pairing** — PP Editorial Old (near-serif, classical) anchors hero displays; Inter (geometric sans) carries everything else. The contrast IS the brand voice.
- **Generous body leading** (1.55 on body-md) for editorial readability across long-form pages
- **Tight hero leading** (1.05 on 84px display) creates magazine-grade typographic display
- **Negative letter-spacing** progresses with size — display sizes use -1.5px to -0.5px; smaller heads relax to 0
- **Stat-display token** (56px Editorial) for marketing stat callouts ("75% / 80% / 100%")

## Layout

### Spacing System
- **Base unit**: 4px (8px primary increment)
- **Tokens**: `{spacing.xxs}` (4px) · `{spacing.xs}` (8px) · `{spacing.sm}` (12px) · `{spacing.md}` (16px) · `{spacing.lg}` (20px) · `{spacing.xl}` (24px) · `{spacing.xxl}` (32px) · `{spacing.xxxl}` (40px) · `{spacing.section-sm}` (48px) · `{spacing.section}` (64px) · `{spacing.section-lg}` (96px) · `{spacing.hero}` (120px)
- **Section rhythm**: Marketing pages use `{spacing.section-lg}` (96px); content pages tighten to `{spacing.section}` (64px)
- **Card internal padding**: `{spacing.xl}` (24px) for compact cards; `{spacing.xxl}` (32px) for feature panels and form panels

### Grid & Container
- Marketing pages use 1280px max-width with 32px gutters
- Hero band uses 2-column split (text left, sunset photography right) on desktop
- Le Studio product page uses 3-up feature grid below the hero
- Contact page uses 1-column layout with cream form panel centered (~520px max-width)
- Services page uses 4-tier card layout with cream feature panel separator strip

### Whitespace Philosophy
Marketing surfaces give content generous breathing room — `{spacing.hero}` (120px) hero padding lets the mountain-sunset photography fill the frame. Form pages tighten dramatically: contact form panel uses `{spacing.xxl}` (32px) internal padding, fields stack on `{spacing.md}` (16px) gap.

## Elevation & Depth

The system runs predominantly flat with strategic atmospheric depth from photography.

| Level | Token | Treatment | Use |
|---|---|---|---|
| 0 (flat) | `{shadow.flat}` | No shadow; `{colors.hairline-strong}` border | Default cards, table rows |
| 0 (control) | `{shadow.flat}` | No shadow; `1px solid {colors.stone}` border | Form inputs, outlined buttons — the border is the only boundary, so it must clear 3:1 |
| 1 (subtle) | `{shadow.subtle}` | `rgba(0, 0, 0, 0.04) 0px 1px 2px 0px` | Hover-elevated tiles |
| 2 (card) | `{shadow.card}` | `rgba(0, 0, 0, 0.04) 0px 4px 12px 0px` | Standard feature cards |
| 3 (mockup) | `{shadow.mockup}` | `rgba(0, 0, 0, 0.08) 0px 12px 24px -4px` | IDE mockup, code editor frames |
| 4 (modal) | `{shadow.modal}` | `rgba(0, 0, 0, 0.12) 0px 16px 48px -8px` | Modals, dropdowns |

Elevation is expressed one way: a border at level 0, a `{shadow.*}` token above it. Borders and shadows are never mixed to express the same step, with one exception — `card-feature-product`, which carries both a `{colors.hairline-soft}` hairline and `{shadow.card}`, because the extracted page does.

### Decorative Depth
- The atmospheric depth on Mistral's hero comes from the photographic mountain-sunset imagery — natural light gradient does the work
- The "sunset stripe" closing band carries depth via its multi-stop gradient (red → orange → yellow → cream)
- IDE / code mockups use dark-canvas backgrounds with subtle drop shadow

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Small chips, micro-controls |
| `{rounded.sm}` | 6px | Discount badges, compact UI |
| `{rounded.md}` | 8px | Buttons, inputs, search-pill, code blocks |
| `{rounded.lg}` | 12px | Cards, modals, panels (the dominant card radius) |
| `{rounded.xl}` | 16px | Larger feature panels |
| `{rounded.xxl}` | 20px | Featured emphasis cards |
| `{rounded.full}` | 9999px | Status badges, pill tabs (used sparingly — most buttons are NOT pills) |

The radius scale is sober and editorial — Mistral does NOT use pill buttons. `{rounded.md}` (8px) for buttons, `{rounded.lg}` (12px) for cards, `{rounded.full}` reserved for badges and the rare pill tab.

### Photography Geometry
- Hero photography is full-bleed atmospheric mountain-sunset imagery with no internal framing
- IDE/code mockups render with `{rounded.lg}` (12px) corners on dark canvas
- Customer logos wall presents wordmarks inline at consistent 60–80px height
- Product imagery (Le Studio mockup, agent UI mockups) sits in `{rounded.lg}` panels with subtle border

## Components

> Every entry below names the states it supports, drawn from default, hover, focus-visible,
> active/pressed, disabled, loading, selected and error. The extracted pages showed only default
> and pressed/active treatments; **hover, focus-visible, loading, selected and error behaviour is
> prescribed by this audit**, not measured from the live site. Focus-visible always means the
> 2px {colors.focus} ring (or {colors.focus-on-dark} on dark and saturated grounds) at a 2px
> offset, so it is not repeated in each row.

### Buttons

**`button-primary`** — Saturated-orange primary CTA, the dominant action.
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.md}`.
- Pressed state `button-primary-pressed` deepens to `{colors.primary-deep}`.
- Disabled state `button-primary-disabled` uses `{colors.hairline}` background and `{colors.muted}` text.
- States: default, hover (background lifts to {colors.sunshine-800}), focus-visible, active/pressed ({colors.primary-deep}), disabled ({colors.hairline} fill, {colors.muted} label), loading (label swaps for an inline spinner, width held)

**`button-cream`** — Warm cream-yellow secondary action, common on cream-surface sections.
- Background `{colors.cream}`, text `{colors.ink}`, border `1px solid {colors.beige-deep}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.md}`.
- States: default, hover ({colors.cream-deeper} fill), focus-visible, active/pressed ({colors.beige-deep} fill), disabled

**`button-dark`** — Dark/black primary CTA on cream surfaces.
- Background `{colors.ink}`, text `{colors.on-dark}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.md}`.
- States: default, hover ({colors.charcoal} fill), focus-visible, active/pressed ({colors.ink} at 90% opacity), disabled, loading

**`button-secondary`** — Outlined secondary action.
- Background transparent, text `{colors.ink}`, border `1px solid {colors.stone}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.md}`.
- The extracted border was `{colors.hairline-strong}` (1.69:1 on `{colors.canvas}`). Because that border is the control's only boundary, it is replaced here with the extracted `{colors.stone}` tone at 3.45:1; `{colors.hairline-strong}` is scoped to card and panel edges.
- States: default, hover (border darkens to {colors.slate}), focus-visible, active/pressed ({colors.surface} fill), disabled

**`button-on-cream`** — White button on cream-tinted backgrounds.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.beige-deep}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.md}`.
- States: default, hover ({colors.surface} fill), focus-visible, active/pressed, disabled

**`button-link`** — Inline orange text link.
- Background transparent, text `{colors.primary}`, typography `{typography.body-sm-medium}`, padding `0`. Underline on activation.
- States: default, hover (underline appears), focus-visible, active/pressed ({colors.primary-deep}). No disabled state — links are removed rather than dimmed.

### Cards & Containers

**`card-base`** — Standard content card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline-soft}`.
- States: default, hover ({shadow.subtle}) only when the whole card is a link; otherwise a static container with one state

**`card-feature`** — White feature card with larger padding.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline-soft}`.
- States: default, hover ({shadow.subtle}) when linked, focus-visible on the card as a whole when linked

**`card-cream`** — Warm cream-yellow feature card (services tiers, perk callouts).
- Background `{colors.cream}`, text `{colors.ink}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.beige-deep}`.
- States: default only — static container, two states (default, hover) when it wraps a link

**`card-cream-soft`** — Lighter cream variant.
- Background `{colors.surface-cream-soft}`, text `{colors.ink}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`.
- States: default only — static container

**`card-feature-product`** — Product showcase card with subtle elevation.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline-soft}`, shadow `rgba(0, 0, 0, 0.04) 0px 4px 12px`.
- States: default, hover ({shadow.mockup}), focus-visible

**`card-photographic`** — Photographic product card with dark background.
- Background `{colors.surface-code}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding `0` (image fills the card).
- States: default, hover (image scales 1.02 under its own overflow clip), focus-visible

**`pricing-card`** — Standard pricing tier card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline-soft}`.
- States: default, hover, focus-visible, selected (border switches to `2px solid {colors.primary}`)

**`pricing-card-featured`** — Featured pricing tier (cream background + orange border).
- Background `{colors.cream}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `2px solid {colors.primary}`.
- States: default, selected — it ships in the selected treatment; no hover lift, so the tier stays visually fixed

### Inputs & Forms

**`text-input`** — Standard text field.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.stone}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, height 44px.
- Extracted border was `{colors.hairline-strong}` (1.69:1), below the 3:1 non-text minimum for the only boundary of a field. Swapped to `{colors.stone}` (3.45:1 on `{colors.canvas}`, 3.31:1 on `{colors.surface}`) — same palette, no invented hex.
- States: default, hover (border darkens to {colors.slate}), focus-visible (`2px solid {colors.primary}` plus the external {colors.focus} ring), disabled ({colors.surface} fill, {colors.muted} text), error (`text-input-error`, `2px solid {colors.primary-deep}` with a `field-error-message` caption below), loading (read-only while the form submits)

**`text-input-focused`** — Activated state.
- Border switches to `2px solid {colors.primary}`.
- States: this IS the focus state of `text-input`; it is not a component with states of its own

**`text-input-error`** — Invalid field (prescribed; the extracted contact form showed no validation styling).
- Border `2px solid {colors.primary-deep}`, text `{colors.ink}`, background `{colors.canvas}`. Deep sunset red is used rather than a new semantic red, since the brand defines no error colour.
- States: this IS the error state of `text-input`.

**`field-error-message`** — Validation caption below an invalid field.
- Text `{colors.primary-deep}` (5.03:1 on `{colors.canvas}`), typography `{typography.caption}`.
- States: default only.

**`text-area`** — Multi-line text area for contact form.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.stone}`, rounded `{rounded.md}`, padding `{spacing.md}`.
- States: default, hover, focus-visible, disabled, error, loading — same ladder as `text-input`

**`contact-form-panel`** — Cream-tinted form container on the contact page.
- Background `{colors.cream}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.beige-deep}`. Hosts text-inputs, text-area, submit `button-dark`.
- States: default, loading (fields go read-only and the submit button shows its loading state), error (a `field-error-message` caption per invalid field). The panel itself has no hover or selected state.

### Tabs

**`pill-tab`** + **`pill-tab-active`** — Pill-style tab nav (used sparingly on product pages).
- Inactive: background `{colors.canvas}`, text `{colors.steel}`, border `1px solid {colors.hairline}`, padding `{spacing.xs} {spacing.md}`, rounded `{rounded.full}`.
- Active: background `{colors.ink}`, text `{colors.on-dark}`.
- States: default, hover ({colors.surface} fill), focus-visible, selected (`pill-tab-active`: {colors.ink} fill, {colors.on-dark} label), disabled

**`segmented-tab`** + **`segmented-tab-active`** — Underline-style tab navigation.
- Inactive: text `{colors.steel}`, transparent background, padding `{spacing.sm} {spacing.md}`, no bottom border.
- Active: text `{colors.primary}`, 2px bottom border in `{colors.primary}`.
- States: default, hover (label darkens to {colors.ink}), focus-visible, selected (`segmented-tab-active`: 2px {colors.primary} underline), disabled

### Badges & Status

**`badge-orange`** — Saturated orange badge.
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.
- States: default only — a static label, not interactive

**`badge-cream`** — Cream-tinted tag chip.
- Background `{colors.cream-deeper}`, text `{colors.ink}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.
- States: default only — a static label, not interactive

**`badge-dark`** — Dark/black status badge.
- Background `{colors.ink}`, text `{colors.on-dark}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.
- States: default only — a static label, not interactive

**`promo-banner`** — Sticky black promo strip ABOVE the top nav.
- Background `{colors.ink}`, text `{colors.on-dark}`, typography `{typography.body-sm-medium}`, padding `{spacing.sm} {spacing.md}`. Carries one-line copy + inline CTA.
- States: default only; its inline CTA carries the `button-link` state ladder

### Code

**`code-block`** — Syntax-highlighted IDE-style code block (Le Studio page mockup, agent demos).
- Background `{colors.surface-code}`, text `{colors.on-dark}`, typography `{typography.code-md}`, rounded `{rounded.md}`, padding `{spacing.md}`.
- States: default, loading (streamed output renders progressively), selected (text selection uses the platform highlight). The copy affordance in its header carries hover and focus-visible.

**`code-block-header`** — Header bar above the code block.
- Background `{colors.surface-code}`, text `{colors.on-dark-muted}`, typography `{typography.caption}`, padding `{spacing.xs} {spacing.md}`, bottom border `1px solid rgba(255,255,255,0.08)`.
- States: default, hover (copy button reveals), focus-visible on the copy button

### Documentation Components

**`feature-icon-tile`** — Cream-yellow feature icon callout.
- Background `{colors.cream}`, rounded `{rounded.md}`, padding `{spacing.md}`, border `1px solid {colors.beige-deep}`.
- States: default only — decorative container

**`industry-tile`** — Industry-vertical tile in solutions page grid.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline-soft}`.
- States: default, hover ({shadow.subtle}), focus-visible — these tiles link into solution pages

**`stat-cell`** — Stat-row cell ("75% more / 80% better").
- Background transparent, text `{colors.ink}`, typography `{typography.stat-display}`, padding `{spacing.lg}`.
- States: default only — static display type

**`customer-testimonial-card`** — Customer quote card (used inside Le Studio and Solutions pages).
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline-soft}`. Quote in `{typography.body-md}`, attribution in `{typography.body-sm}` `{colors.steel}`.
- States: default only — static quote container

**`logo-wall-item`** — Customer logo wordmark cell.
- Background transparent, text `{colors.steel}`, typography `{typography.body-md-medium}`, padding `{spacing.lg}`.
- States: default, hover (opacity 1 from 0.7) when the logo links out; default only otherwise

**`faq-accordion-item`** — FAQ panel.
- Background `{colors.canvas}`, rounded `{rounded.md}`, padding `{spacing.xl}`, bottom border `1px solid {colors.hairline}`.
- States: default, hover, focus-visible, selected (expanded, panel height is not animated — see Motion & Animation), disabled

**`app-store-badge`** — App Store / Google Play download badge.
- Background `{colors.ink}`, text `{colors.on-dark}`, typography `{typography.caption-bold}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`.
- States: default, hover, focus-visible, active/pressed

### Navigation

**Top Navigation (Marketing)** — Sticky white bar.
- Background `{colors.canvas}`, height ~64px, bottom border `1px solid {colors.hairline-soft}`.
- Left: Mistral M-mark logo + "MISTRAL AI_" wordmark + horizontal link list (Products, Solutions, Research, Blog, Customers, Company).
- Right: "Contact Sales" link + black-pill "Try Studio" CTA.
- States: default, hover (links darken to {colors.ink}), focus-visible, selected (current section), plus a mobile open/closed disclosure that is not a state of the bar itself

### Signature Components

**`hero-band-sunset`** — Atmospheric sunset hero band.
- Background gradient `linear-gradient(135deg, {colors.sunshine-700} 0%, {colors.sunshine-900} 60%, {colors.primary} 100%)` overlaid on photographic mountain landscape.
- Layout: hero headline left in `{typography.hero-display}` ({colors.ink}), subtitle in `{typography.subtitle}` ({colors.ink-tint}), button row (`button-dark` + `button-secondary`), atmospheric mountain photography right.
- States: default only — a layout band. Its buttons carry their own states.

**`sunset-stripe-band`** — Horizontal closing band at the foot of every page.
- Multi-stop gradient: `{colors.primary}` → `{colors.sunshine-700}` → `{colors.sunshine-500}` → `{colors.yellow-saturated}` → `{colors.cream}`.
- Padding `{spacing.lg} 0`. Spans full width, sits above the footer. THIS IS THE BRAND'S MOST RECOGNIZABLE SIGNATURE ELEMENT.
- States: default only — a decorative band, never interactive

**`cta-banner-cream`** — Page-bottom CTA band on cream surface.
- Background `{colors.cream}`, text `{colors.ink}`, rounded `{rounded.lg}`, padding `{spacing.section}`. "The next chapter of AI is yours." headline in `{typography.heading-1}` (PP Editorial Old), button row below.
- States: default only — a layout band

**`footer-region`** — Cream-tinted multi-column footer.
- Background `{colors.footer-cream}`, padding `{spacing.section} {spacing.xxl}`.
- 5-column link grid (Why Mistral / Explore / Build / Legal + brand mark column).
- Bottom: language picker + social icons.
- States: default only — a layout region

**`footer-link`** — Individual footer link.
- Background transparent, text `{colors.primary}`, typography `{typography.body-sm}`, padding `{spacing.xxs} 0`.
- States: default, hover (underline appears), focus-visible, active/pressed

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted from mistral.ai; the values are the **Crisp** profile's shared block, chosen because Mistral's product surface is a developer tool (Le Studio, code blocks, IDE mockups) where state change should read as instant and nothing choreographs on entry. The editorial display type is static; the motion is not.

### Tokens

| Token | Value |
|---|---|
| `{motion.duration-instant}` | 60ms |
| `{motion.duration-fast}` | 100ms |
| `{motion.duration-base}` | 150ms |
| `{motion.duration-slow}` | 220ms |
| `{motion.duration-emphasis}` | 300ms |
| `{motion.ease-standard}` | `cubic-bezier(0.2, 0, 0.2, 1)` |
| `{motion.ease-enter}` | `cubic-bezier(0, 0, 0.2, 1)` |
| `{motion.ease-exit}` | `cubic-bezier(0.4, 0, 1, 1)` |
| `{motion.stagger-step}` | 20ms |
| `{motion.duration-reduced}` | 100ms |

### Interaction inventory

| Interaction | Duration | Easing | Property | Reduced-motion |
|---|---|---|---|---|
| Hover (button, tab, link) | `{motion.duration-instant}` | `{motion.ease-standard}` | `background-color`, `opacity` | unchanged — no travel to remove |
| Press / active | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` only; no scale, Mistral's geometry is sober | unchanged |
| Focus ring appears | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring; the ring itself never animates its offset | ring appears with no fade |
| Page / route transition | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` on the content region | `opacity` at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px → 0)` | `opacity` only, `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform` | `opacity` only, `{motion.duration-reduced}` |
| Dropdown / nav menu | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(-4px → 0)` | `opacity` only, `{motion.duration-reduced}` |
| Toast enter / exit | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px → 0)` | `opacity` only, `{motion.duration-reduced}` |
| List / grid enter (feature tiles, pricing tiers) | `{motion.duration-fast}` per item, `{motion.stagger-step}` between | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px → 0)` | `opacity` only, no stagger, `{motion.duration-reduced}` |
| List / grid exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | `opacity` at `{motion.duration-reduced}` |
| FAQ accordion disclosure | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` + `transform` on the panel content; the panel's own `height` is **not** animated | `opacity` only, `{motion.duration-reduced}` |
| Loading (button spinner, streamed code block) | 800ms linear, infinite | linear | `transform: rotate` | spinner stops rotating; a static progress label replaces it |

Exit is shorter than its matching entrance in every row above. Animate `transform` and `opacity` only — never `width`, `height`, `top`, `left` or `margin`.

### Rules specific to this brand

- The hero mountain-sunset photography and the `sunset-stripe-band` gradient are **static**. Neither pans, parallaxes nor cycles its gradient stops. A Crisp brand does not reveal its hero slowly, and the stripe is a brand mark, not an effect.
- Nothing animates on first paint in a way that delays content: the hero headline and subtitle render at full opacity immediately.
- The only infinite animation in the system is the loading spinner. There is no brand ambience loop.
- `card-photographic` hover scales its image by 1.02 inside its own clip — `transform` only, never the card's box dimensions.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale travel, all stagger, the loading spinner's rotation. */
  /* Kept: opacity fades only, capped at {motion.duration-reduced} (100ms). */
  *, *::before, *::after {
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;
    transition-property: opacity !important;
  }
}
```

Removed under reduce: every `transform` travel and scale (modal, drawer, dropdown, toast, list enter, `card-photographic` image scale), the `{motion.stagger-step}` cascade, and the spinner's rotation. Kept: opacity fades at `{motion.duration-reduced}` (100ms) and all colour changes. Nothing in this file holds an ambient loop that needs freezing.

## Accessibility

Measured with WCAG 2.1 relative luminance from this file's own frontmatter hexes. **Mistral's extracted palette fails AA at several points and those values are not altered here** — the brand hexes are facts about the brand, so each failure is named with its ratio instead.

### Text contrast

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `ink` on `canvas` (#1f1f1f on #ffffff) | 16.48:1 | 4.5:1 | pass |
| `ink` on `surface` (#1f1f1f on #fafafa) | 15.79:1 | 4.5:1 | pass |
| `ink` on `cream` (#1f1f1f on #fff8e0) | 15.51:1 | 4.5:1 | pass |
| `charcoal` on `canvas` | 13.97:1 | 4.5:1 | pass |
| `ink-tint` on `canvas` | 10.86:1 | 4.5:1 | pass |
| `slate` on `canvas` | 8.86:1 | 4.5:1 | pass |
| `steel` on `canvas` | 5.41:1 | 4.5:1 | pass |
| `steel` on `surface` | 5.18:1 | 4.5:1 | pass |
| `stone` on `canvas` | 3.45:1 | 4.5:1 body / 3:1 at 24px+ | **fails for body text** — `stone` is scoped to 24px+ display labels and to control boundaries, never to body prose |
| `muted` on `canvas` (#a8a8a8 on #ffffff) | 2.38:1 | 4.5:1 | **fails** — real brand value, frozen. `muted` is placeholder and disabled text only; WCAG sets no requirement on disabled, and placeholders are never the only label. Secondary prose uses `slate` or `steel`. |
| `muted` on `surface` (#a8a8a8 on #fafafa) | 2.28:1 | 4.5:1 | **fails** — same scope and same reasoning as above |
| `on-dark` on `surface-code` (#ffffff on #1c1c1e) | 17.01:1 | 4.5:1 | pass |
| `on-dark-muted` on `surface-code` (#a8a8a8 on #1c1c1e) | 7.16:1 | 4.5:1 | pass |

### Non-text contrast (boundaries)

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `hairline-soft` on `surface` (#ededed on #fafafa) | 1.12:1 | 3:1 | **fails** — frozen extracted value, decorative dividers only |
| `hairline-soft` on `canvas` (#ededed on #ffffff) | 1.17:1 | 3:1 | **fails** — frozen extracted value, decorative dividers only |
| `hairline` on `surface` (#e5e5e5 on #fafafa) | 1.21:1 | 3:1 | **fails** — frozen, decorative only |
| `hairline` on `canvas` (#e5e5e5 on #ffffff) | 1.26:1 | 3:1 | **fails** — frozen, decorative only |
| `hairline-strong` on `surface` (#c7c7c7 on #fafafa) | 1.62:1 | 3:1 | **fails** — frozen; card and panel edges, where the card is also separated by padding and type |
| `hairline-strong` on `canvas` (#c7c7c7 on #ffffff) | 1.69:1 | 3:1 | **fails** — frozen; card and panel edges only |
| `stone` as control boundary on `canvas` (#8a8a8a on #ffffff) | 3.45:1 | 3:1 | pass — the accessible boundary tone for inputs and outlined buttons |
| `stone` as control boundary on `surface` (#8a8a8a on #fafafa) | 3.31:1 | 3:1 | pass |

**Plain statement:** none of Mistral's three extracted hairline tones reaches the 3:1 non-text minimum. Anyone building on this document must not rely on a hairline alone to bound an interactive control; use `{colors.stone}` there.

### Signal colour contrast

The brand orange is the single biggest accessibility cost in this palette, and it is the brand.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `on-primary` on `primary` — `button-primary` (#ffffff on #fa520f) | 3.34:1 | 4.5:1 | **fails** — frozen brand orange with white label |
| `badge-orange` (#ffffff on #fa520f) | 3.34:1 | 4.5:1 | **fails** — same frozen pair |
| `sunset-stripe-band` (#ffffff on #fa520f) | 3.34:1 | 4.5:1 | **fails** — the band is decorative and carries no essential copy; any text on it must use `{colors.ink}` (4.93:1) |
| `button-link` (#fa520f on #ffffff) | 3.34:1 | 4.5:1 | **fails** — orange link text on white |
| `footer-link` (#fa520f on #ffffff) | 3.34:1 | 4.5:1 | **fails** — orange link text on white |
| `segmented-tab-active` (#fa520f on #ffffff) | 3.34:1 | 4.5:1 | **fails** — orange active tab label on white |
| `ink` on `primary` (#1f1f1f on #fa520f) | 4.93:1 | 4.5:1 | pass — the accessible label colour on the brand orange |
| `ink` on `sunshine-700` (#1f1f1f on #ffa110) | 8.13:1 | 4.5:1 | pass — the hero band's own pairing |
| `primary-deep` on `canvas` (#cc3a05 on #ffffff) | 5.03:1 | 4.5:1 | pass — the accessible substitute for orange *text* |

At `{typography.button-md}` (14px/500) the orange pairs need 4.5:1 and reach 3.34:1. The nearest passing values are listed under **Needs approval** in the audit report; none is applied here, because changing `#fa520f` would make this document wrong about the brand.

### Focus visibility

The ring is prescribed (see Colors → Focus). 2px, drawn outside the control at a 2px offset, so it is measured against the surface behind the control rather than the control's fill.

| Surface the ring is drawn on | Ring | Ratio | Required |
|---|---|---|---|
| `canvas` #ffffff | `{colors.focus}` | 8.59:1 | 3:1 |
| `surface` #fafafa | `{colors.focus}` | 8.23:1 | 3:1 |
| `surface-cream` / `cream` #fff8e0 | `{colors.focus}` | 8.08:1 | 3:1 |
| `surface-cream-soft` #fffaeb | `{colors.focus}` | 8.23:1 | 3:1 |
| `cream-deeper` #fff0c2 | `{colors.focus}` | 7.56:1 | 3:1 |
| `beige-deep` #e6d5a8 | `{colors.focus}` | 5.91:1 | 3:1 |
| `yellow-saturated` #ffd900 (stripe stop) | `{colors.focus}` | 6.21:1 | 3:1 |
| `sunshine-700` #ffa110 (hero band) | `{colors.focus}` | 4.24:1 | 3:1 |
| `primary` #fa520f (stripe band) | `{colors.focus-on-dark}` | 3.15:1 | 3:1 |
| `ink` #1f1f1f (promo banner, dark buttons) | `{colors.focus-on-dark}` | 15.51:1 | 3:1 |
| `surface-code` #1c1c1e (code blocks) | `{colors.focus-on-dark}` | 16.01:1 | 3:1 |

Two rings are needed rather than one: no single value clears 3:1 against both `canvas` (which caps a ring at a relative luminance of 0.30) and `primary` (which admits only a ring below 0.055 or above 0.892). Over full-bleed hero photography, which has no measurable colour, the two-tone ring applies — 2px `{colors.focus}` core with a 1px `{colors.focus-on-dark}` outer edge.

### Tap targets

- Buttons: `10px 20px` padding on `{typography.button-md}` (14px/1.30) renders ~40px tall — meets the WCAG 2.2 AA 24px minimum, below the 44px AAA target. Marketing CTAs should be padded to 44px.
- Form inputs: 44px declared height — passes AAA.
- `pill-tab`: ~32px desktop, documented as bumping to 44px on mobile.
- `footer-link`: `{spacing.xxs} 0` padding on 14px/1.50 type gives ~29px — passes the 24px minimum; stack footer links at `{spacing.xs}` gaps so adjacent targets do not touch.

### Reduced motion

Honoured in full — see Motion & Animation. All travel, scale and stagger are removed; opacity fades remain, capped at `{motion.duration-reduced}` (100ms).

### Remaining gaps

- No dark-mode palette is published by the brand, so dark-mode text contrast cannot be measured beyond the `surface-code` pairs above.
- Contrast over the hero photography and the `sunset-stripe-band` gradient is not measurable from a document; the two-tone ring and the `{colors.ink}` label rule are the mitigations.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (saturated orange) for primary CTAs and active states only
- Use the **sunset stripe band** at the foot of every page — it's the brand's most recognizable signature
- Pair PP Editorial Old (display) with Inter (UI) — never substitute either with a generic alternative
- Apply `{rounded.md}` (8px) to buttons and `{rounded.lg}` (12px) to cards consistently
- Use cream-yellow surfaces ({colors.cream}) for form panels, feature cards, and footer
- Anchor heroes with photographic mountain-sunset imagery (or its visual equivalent — atmospheric gradient sky)
- Use stat-display token (PP Editorial 56px) for stat callouts to maintain editorial character
- Draw focus with the 2px `{colors.focus}` ring at a 2px offset on light and warm grounds, and `{colors.focus-on-dark}` on `{colors.ink}`, `{colors.surface-code}` and the orange stripe
- Use `{colors.stone}` for any border that is a control's only boundary; keep `{colors.hairline}` and `{colors.hairline-soft}` decorative
- Put `{colors.ink}` on the orange, not white — `{colors.on-primary}` on `{colors.primary}` measures 3.34:1
- Keep motion at the Crisp durations: `{motion.duration-instant}` for hover and press, `{motion.duration-base}` at the slowest for a modal

### Don't
- Don't use pill-shaped buttons (`{rounded.full}`) — Mistral's geometry is sober and editorial, not playful
- Don't introduce additional accent colors beyond the orange/yellow/cream sunset palette
- Don't reduce hero leading below 1.05 — the editorial display needs that magazine-grade tightness
- Don't replace PP Editorial Old hero displays with Inter — the editorial / sans contrast IS the brand
- Don't apply heavy shadows on flat documentation cards; reserve elevation for IDE mockups
- Don't drop the sunset stripe band from any page bottom — it's the brand's continuity element
- Don't animate the hero photography or cycle the sunset stripe's gradient stops — both are static brand marks, not effects
- Don't animate `width`, `height`, `top`, `left` or `margin`; animate `transform` and `opacity` only
- Don't use `{colors.muted}` for anything a sighted user must read — it is placeholder and disabled text only, at 2.38:1
- Don't suppress the focus ring; the brand ships none today and that is the single biggest gap in this document

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile (small) | < 480px | Single column. Hero scales to 40px (PP Editorial). Pill nav collapses to hamburger. Pricing tiers stack 1-up. |
| Mobile (large) | 480 – 767px | Feature tiles 2-up. Hero scales to 52px. |
| Tablet | 768 – 1023px | 2-column feature grids. Pill-tab nav returns. Hero 64px. |
| Desktop | 1024 – 1279px | Multi-column layouts. Hero 76px. Stat row at full width. |
| Wide Desktop | ≥ 1280px | Full 84px hero presentation. |

### Touch Targets
- Buttons render at 40–44px effective height — at WCAG AAA floor with `10px 20px` padding
- Form inputs render at 44px height
- Pill tabs render at ~32px tall — bumps to 44px on mobile

### Collapsing Strategy
- **Promo banner** stays full-width; truncates at < 480px
- **Top nav** below 1024px collapses to hamburger
- **Hero band**: 2-column hero (text + photography) collapses to stacked at < 1024px
- **Pricing tiers**: 4-column desktop → 2-column tablet → 1-column mobile
- **Stat row**: 3-column → stacked at < 768px
- **Hero typography**: 84px → 64px → 52px → 40px
- **Footer**: 5-column desktop → 3-column tablet → 1-column accordion mobile
- **Sunset stripe band** stays full-width on all breakpoints

### Image Behavior
- Mountain-sunset photography uses 16:9 ratio with full-bleed scaling
- IDE mockup images maintain aspect ratio across breakpoints
- Customer logo wall presents wordmarks at consistent 60–80px height

## Iteration Guide

1. Focus on ONE component at a time
2. Reference component names and tokens directly (`{colors.primary}`, `{component-name}-pressed`)
3. Run `npx @google/design.md lint DESIGN.md` after edits
4. Add new variants as separate `components:` entries
5. Default to `{typography.body-md}` for body and `{typography.subtitle}` for emphasis. Hero displays use `{typography.hero-display}` (PP Editorial Old).
6. Keep `{colors.primary}` confined to primary CTAs, active states, and the sunset stripe band
7. Cards use `{rounded.lg}` (12px), buttons use `{rounded.md}` (8px). Pills (`{rounded.full}`) reserved for badges only.
8. Always include the sunset-stripe-band component at the foot of every page mockup.
9. Reference motion through `{motion.*}` tokens; never hardcode a duration or a cubic-bezier.
10. Give every new component a States line naming its states, and a focus-visible treatment drawn from `{colors.focus}` or `{colors.focus-on-dark}`.

## Known Gaps

- Specific dark-mode token values not surfaced; the brand has not shipped a published dark-mode palette
- Animation/transition timings were **not extracted** from the live site. The `motion:` group and the Motion & Animation section carry the shared **Crisp** profile values and are labelled prescribed throughout.
- No focus ring is visible on the live site; `{colors.focus}` and `{colors.focus-on-dark}` are prescribed by this audit, not extracted.
- Hover, focus-visible, loading, selected and error treatments are prescribed; the extracted pages showed default and pressed/active only.
- `{shadow.flat}`/`{shadow.subtle}`/`{shadow.card}`/`{shadow.mockup}`/`{shadow.modal}` are tokenised from the rgba values already written in the Elevation table; the modal and dropdown levels were inferred from the elevation ladder, not observed on a rendered modal.
- Form validation success state not explicitly captured beyond defaults
- The exact minimum tap-target heights could not be verified without a rendered page; the figures in Accessibility are computed from this file's own padding and line-height values.
- Sunset stripe band gradient stops are approximations — the actual values may vary slightly across pages but the visual rhythm is consistent
