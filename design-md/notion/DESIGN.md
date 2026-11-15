---
version: alpha
name: Notion-design-analysis
description: Notion presents itself as the all-in-one workspace through a confident, illustration-rich brand voice — anchored by a deep navy hero band ({colors.brand-navy}) decorated with brand-colored sticky-note dots and mesh wire illustrations, a signature purple pill primary CTA ({colors.primary}), and a rich palette of pastel-tinted feature cards that echo the colorful database properties of the live product. The system uses a Notion-Sans (Inter-based) typeface across every UI surface, anchors a 4-tier pricing comparison (Free / Plus / Business / Enterprise), and presents the live workspace UI mockup directly inside the hero band. Coverage spans homepage, Enterprise, Product AI, Product Agents, Startups, and Pricing surfaces.

colors:
  primary: "#5645d4"
  primary-pressed: "#4534b3"
  primary-deep: "#3a2a99"
  on-primary: "#ffffff"
  brand-navy: "#0a1530"
  brand-navy-deep: "#070f24"
  brand-navy-mid: "#1a2a52"
  link-blue: "#0075de"
  link-blue-pressed: "#005bab"
  brand-orange: "#dd5b00"
  brand-orange-deep: "#793400"
  brand-pink: "#ff64c8"
  brand-pink-deep: "#a02e6d"
  brand-purple: "#7b3ff2"
  brand-purple-300: "#d6b6f6"
  brand-purple-800: "#391c57"
  brand-teal: "#2a9d99"
  brand-green: "#1aae39"
  brand-yellow: "#f5d75e"
  brand-brown: "#523410"
  card-tint-peach: "#ffe8d4"
  card-tint-rose: "#fde0ec"
  card-tint-mint: "#d9f3e1"
  card-tint-lavender: "#e6e0f5"
  card-tint-sky: "#dcecfa"
  card-tint-yellow: "#fef7d6"
  card-tint-yellow-bold: "#f9e79f"
  card-tint-cream: "#f8f5e8"
  card-tint-gray: "#f0eeec"
  canvas: "#ffffff"
  surface: "#f6f5f4"
  surface-soft: "#fafaf9"
  hairline: "#e5e3df"
  hairline-soft: "#ede9e4"
  hairline-strong: "#c8c4be"
  ink-deep: "#000000"
  ink: "#1a1a1a"
  charcoal: "#37352f"
  slate: "#5d5b54"
  steel: "#787671"
  stone: "#a4a097"
  muted: "#bbb8b1"
  on-dark: "#ffffff"
  on-dark-muted: "#a4a097"
  semantic-success: "#1aae39"
  semantic-warning: "#dd5b00"
  semantic-error: "#e03131"
  focus: "#3a2a99"
  focus-on-dark: "#d6b6f6"

typography:
  hero-display:
    fontFamily: Notion Sans
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -2px
  display-lg:
    fontFamily: Notion Sans
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1px
  heading-1:
    fontFamily: Notion Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  heading-2:
    fontFamily: Notion Sans
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.5px
  heading-3:
    fontFamily: Notion Sans
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
  heading-4:
    fontFamily: Notion Sans
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.30
  heading-5:
    fontFamily: Notion Sans
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.40
  subtitle:
    fontFamily: Notion Sans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
  body-md:
    fontFamily: Notion Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  body-md-medium:
    fontFamily: Notion Sans
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.55
  body-sm:
    fontFamily: Notion Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
  body-sm-medium:
    fontFamily: Notion Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
  caption:
    fontFamily: Notion Sans
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.40
  caption-bold:
    fontFamily: Notion Sans
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.40
  micro:
    fontFamily: Notion Sans
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
  micro-uppercase:
    fontFamily: Notion Sans
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 1px
  button-md:
    fontFamily: Notion Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 20px
  xxxl: 24px
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
  subtle: "rgba(15, 15, 15, 0.04) 0px 1px 2px 0px"
  card: "rgba(15, 15, 15, 0.08) 0px 4px 12px 0px"
  mockup: "rgba(15, 15, 15, 0.20) 0px 24px 48px -8px"
  modal: "rgba(15, 15, 15, 0.16) 0px 16px 48px -8px"

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
    padding: "10px 18px"
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
  button-dark:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
    border: "1px solid {colors.hairline-strong}"
  button-on-dark:
    backgroundColor: "{colors.on-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
    border: "1px solid {colors.on-dark-muted}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.link-blue}"
    typography: "{typography.body-sm-medium}"
    padding: "0"
  card-base:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  card-feature:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  card-feature-yellow-bold:
    backgroundColor: "{colors.card-tint-yellow-bold}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-peach:
    backgroundColor: "{colors.card-tint-peach}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-rose:
    backgroundColor: "{colors.card-tint-rose}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-mint:
    backgroundColor: "{colors.card-tint-mint}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-sky:
    backgroundColor: "{colors.card-tint-sky}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-lavender:
    backgroundColor: "{colors.card-tint-lavender}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-yellow:
    backgroundColor: "{colors.card-tint-yellow}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-cream:
    backgroundColor: "{colors.card-tint-cream}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-agent-tile:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  card-template:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  card-startup-perk:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  pricing-card-featured:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline-strong}"
    height: 44px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.primary}"
  search-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.steel}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  pill-tab:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm-medium}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    border: "1px solid {colors.hairline}"
  pill-tab-active:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink-deep}"
  segmented-tab:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm-medium}"
    padding: "{spacing.sm} {spacing.md}"
    border: "0 0 2px transparent solid"
  segmented-tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-medium}"
    border: "0 0 2px {colors.ink} solid"
  badge-purple:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-pink:
    backgroundColor: "{colors.brand-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-orange:
    backgroundColor: "{colors.brand-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-tag-purple:
    backgroundColor: "{colors.card-tint-lavender}"
    textColor: "{colors.brand-purple-800}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-tag-orange:
    backgroundColor: "{colors.card-tint-peach}"
    textColor: "{colors.brand-orange-deep}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-tag-green:
    backgroundColor: "{colors.card-tint-mint}"
    textColor: "{colors.brand-green}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-popular:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  promo-banner:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-medium}"
    padding: "{spacing.sm} {spacing.md}"
  hero-band-dark:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    rounded: "0"
    padding: "{spacing.hero}"
  workspace-mockup-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "0"
    border: "1px solid {colors.hairline}"
    shadow: "rgba(15, 15, 15, 0.2) 0px 24px 48px -8px"
  cta-banner-light:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.section}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  comparison-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.lg}"
    border: "0 0 1px {colors.hairline-soft} solid"
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
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
  stat-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.section-sm}"
  footer-region:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.charcoal}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
    border: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxs} 0"
---

## Overview

Notion presents itself as the all-in-one workspace through a confident, illustration-rich brand voice. The homepage opens with **"Meet the night shift."** rendered centered over a deep navy hero band ({colors.brand-navy}), decorated with brand-colored sticky-note dots and mesh wire illustrations scattered around the headline. The signature **purple pill primary CTA** ({colors.primary}) "Get Notion free" sits at the visual center, paired with an outlined "Request a demo" secondary. Below the buttons, a real Notion workspace UI mockup card (the "Ramp HQ" kanban board) breaks out of the hero band with a deep diffuse drop shadow.

Below the hero, the page cycles through a distinctive sequence of feature sections: a dense sticky-note "Keep work moving 24/7" panel with red/blue/green/purple/teal status icons; a **bold yellow** ({colors.card-tint-yellow-bold}) "Ask your on-demand assistants" banner card flanked by orange/rose/mint pastel feature tiles showing assistant UI mockups; and a "Bring all your work together" 3-column grid with brand-colored mockups (sky-blue tutorial card, light Notion calendar, brown/rust testimonial slate). The pricing page renders 4 tiers (Free / Plus / Business / Enterprise) horizontally with one tier featured (purple-bordered) and a dense feature comparison table running below.

The system uses a Notion-Sans typeface (Inter-based) across every UI surface — humanist-geometric character that pairs naturally with the colorful illustrations. Buttons are `{rounded.md}` (8px) rectangles, NOT pills — distinguishing Notion's sober rectangular geometry from competitors that use pills universally. Cards use `{rounded.lg}` (12px) consistently.

**Key Characteristics:**
- Deep navy hero band ({colors.brand-navy}) with scattered sticky-note dots + mesh wire decorative illustrations
- **Signature purple pill** ({colors.primary}) primary CTA — Notion's recognizable "Get Notion free" button color
- Real Notion workspace UI mockup card embedded in the hero with deep drop shadow
- Bold yellow feature banner ({colors.card-tint-yellow-bold}) for high-emphasis content sections
- Pastel feature card palette (peach, rose, mint, lavender, sky, yellow) echoing the live product database properties
- Notion-Sans (Inter-based) across every UI surface
- 8px-rounded buttons (NOT pills), 12px-rounded cards — sober editorial geometry
- 4-tier pricing comparison with dense feature table
- Centered hero layout (different from the left-aligned norm of most B2B SaaS)

## Colors

> Source pages: notion.com/ (homepage), /enterprise, /product/ai, /product/agents, /startups, /pricing. Token coverage was identical across all six pages.

### Brand & Primary
- **Notion Purple** ({colors.primary}): Signature primary CTA color — the unmistakable "Get Notion free" pill button. Reserved for the dominant CTA only.
- **Purple Pressed** ({colors.primary-pressed}): Pressed-state variant
- **Purple Deep** ({colors.primary-deep}): Deeper variant for emphasis
- **Brand Navy** ({colors.brand-navy}): Hero band background — deep navy
- **Brand Navy Deep** ({colors.brand-navy-deep}): Deeper navy for promo banner
- **Brand Navy Mid** ({colors.brand-navy-mid}): Mid-spectrum navy
- **Link Blue** ({colors.link-blue}): Inline text link blue (NOT primary CTA)
- **Link Blue Pressed** ({colors.link-blue-pressed}): Pressed-state link blue

### Brand Color Spectrum (echoes live product database properties)
- **Brand Pink** ({colors.brand-pink}): Pink accent
- **Brand Pink Deep** ({colors.brand-pink-deep}): Deeper pink
- **Brand Orange** ({colors.brand-orange}): Orange accent
- **Brand Orange Deep** ({colors.brand-orange-deep}): Deeper orange-rust
- **Brand Purple** ({colors.brand-purple}): Purple accent variant
- **Brand Purple 300** ({colors.brand-purple-300}): Light purple
- **Brand Purple 800** ({colors.brand-purple-800}): Deep purple for tag text
- **Brand Teal** ({colors.brand-teal}): Teal accent
- **Brand Green** ({colors.brand-green}): Bright green
- **Brand Yellow** ({colors.brand-yellow}): Soft yellow
- **Brand Brown** ({colors.brand-brown}): Brand brown for "earthy" tints

### Card Tints (Pastel Feature Card Backgrounds)
- **Tint Peach** ({colors.card-tint-peach}): Pale peach
- **Tint Rose** ({colors.card-tint-rose}): Pale rose-pink
- **Tint Mint** ({colors.card-tint-mint}): Pale mint-green
- **Tint Lavender** ({colors.card-tint-lavender}): Pale lavender
- **Tint Sky** ({colors.card-tint-sky}): Pale sky-blue
- **Tint Yellow** ({colors.card-tint-yellow}): Pale yellow
- **Tint Yellow Bold** ({colors.card-tint-yellow-bold}): Bold yellow for high-emphasis feature banners ("Ask your on-demand assistants")
- **Tint Cream** ({colors.card-tint-cream}): Cream tint
- **Tint Gray** ({colors.card-tint-gray}): Neutral surface

### Surface
- **Canvas White** ({colors.canvas}): Page background and primary card surface
- **Surface** ({colors.surface}): Subtle section backgrounds, search-pill rest, featured pricing tier
- **Surface Soft** ({colors.surface-soft}): Quieter section divisions
- **Hairline** ({colors.hairline}): 1px borders and primary dividers — **decorative only**; 1.28:1 on {colors.canvas}, so it cannot be the sole boundary of a control
- **Hairline Soft** ({colors.hairline-soft}): Quieter dividers — decorative only, 1.21:1 on {colors.canvas}
- **Hairline Strong** ({colors.hairline-strong}): Notion's strongest extracted 1px border, used on inputs — still only 1.74:1 on {colors.canvas}. Where a boundary must be perceivable (text field edge, control outline), draw `{colors.steel}` instead (4.54:1 on {colors.canvas}, 4.17:1 on {colors.surface}); the real brand's input border fails WCAG 1.4.11 non-text contrast and no extracted hairline tone reaches 3:1.

### Text
- **Ink Deep** ({colors.ink-deep}): Pure black for emphasis
- **Ink** ({colors.ink}): Primary headlines and body text
- **Charcoal** ({colors.charcoal}): Body emphasis (Notion's signature warm-charcoal)
- **Slate** ({colors.slate}): Secondary text
- **Steel** ({colors.steel}): Tertiary, footer links
- **Stone** ({colors.stone}): Muted labels — 2.61:1 on {colors.canvas}; decorative or disabled use only
- **Muted** ({colors.muted}): Disabled text and placeholders **only**. At 1.98:1 on {colors.canvas} and 1.82:1 on {colors.surface} this is the weakest ink in the palette and must never carry secondary or caption text. For secondary text use `{colors.slate}` (6.80:1 / 6.24:1), which the palette already owns; for tertiary text use `{colors.steel}` (4.54:1 on {colors.canvas}). Placeholder text drawn in {colors.muted} is unreadable by AA and is recorded as a real brand failure in Accessibility.
- **On Dark** ({colors.on-dark}): White text on dark surfaces — 18.06:1 on {colors.brand-navy}
- **On Dark Muted** ({colors.on-dark-muted}): Reduced-opacity white — 6.93:1 on {colors.brand-navy}

### Semantic
- **Success** ({colors.semantic-success}): Confirmation green — as a **fill or icon** only; 2.93:1 on {colors.canvas}, so it fails as text
- **Warning** ({colors.semantic-warning}): Mid-priority alerts (orange) — 3.77:1 on {colors.canvas}; text use restricted to 24px+, or 18.66px+ at weight 700
- **Error** ({colors.semantic-error}): Validation errors (red) — 4.51:1 on {colors.canvas}, passes AA for body text

### Focus
Prescribed, not extracted — no focus ring was observable on the captured pages. Both values reuse hexes the brand already owns, so no colour is invented.

- **Focus Ring** ({colors.focus}): the ring for every light surface this file defines. Same value as the extracted {colors.primary-deep}, a deep Notion purple that keeps the indicator inside the brand's signal hue. 10.65:1 on {colors.canvas}, 9.78:1 on {colors.surface}, 10.20:1 on {colors.surface-soft}, and 8.29:1–9.89:1 on every `card-tint-*` feature card.
- **Focus Ring On Dark** ({colors.focus-on-dark}): the counterpart ring for the navy hero band and black fills, since {colors.focus} reaches only 1.70:1 on {colors.brand-navy} and 1.97:1 on {colors.ink-deep}. Same value as the extracted {colors.brand-purple-300}. 10.22:1 on {colors.brand-navy}, 10.77:1 on {colors.brand-navy-deep}, 7.94:1 on {colors.brand-navy-mid}, 11.88:1 on {colors.ink-deep}.

Geometry: 2px ring with a 2px offset in the surface colour, drawn **outside** the control, so the ring is measured against the surface behind it rather than the control fill — the purple ring on a {colors.primary} button separates from the fill by only 1.62:1 and relies on that offset gap.

## Typography

### Font Family
**Notion Sans** (primary): Notion's custom Inter-based variable typeface. Fallbacks: Inter, -apple-system, system-ui, 'Segoe UI', Helvetica, sans-serif. Humanist-geometric character used across every UI surface.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 80px | 600 | 1.05 | -2px | Hero ("Meet the night shift") |
| `{typography.display-lg}` | 56px | 600 | 1.10 | -1px | Section openers |
| `{typography.heading-1}` | 48px | 600 | 1.15 | -0.5px | Page-level headlines ("Try for free") |
| `{typography.heading-2}` | 36px | 600 | 1.20 | -0.5px | Subsection headlines ("Keep work moving 24/7") |
| `{typography.heading-3}` | 28px | 600 | 1.25 | 0 | Card titles |
| `{typography.heading-4}` | 22px | 600 | 1.30 | 0 | Feature tile titles |
| `{typography.heading-5}` | 18px | 600 | 1.40 | 0 | FAQ questions |
| `{typography.subtitle}` | 18px | 400 | 1.50 | 0 | Hero subtitle |
| `{typography.body-md}` | 16px | 400 | 1.55 | 0 | Primary body text |
| `{typography.body-md-medium}` | 16px | 500 | 1.55 | 0 | Body emphasis |
| `{typography.body-sm}` | 14px | 400 | 1.50 | 0 | Secondary body |
| `{typography.body-sm-medium}` | 14px | 500 | 1.50 | 0 | Active sidebar, button labels |
| `{typography.caption}` | 13px | 400 | 1.40 | 0 | Captions, helper and validation text |
| `{typography.caption-bold}` | 13px | 600 | 1.40 | 0 | Badge labels |
| `{typography.micro}` | 12px | 500 | 1.40 | 0 | Fine print, table footnotes |
| `{typography.micro-uppercase}` | 11px | 600 | 1.40 | 1px | Eyebrow and section labels |
| `{typography.button-md}` | 14px | 500 | 1.30 | 0 | Button labels |

### Principles
- Tight hero leading (1.05) on 80px display
- Negative letter-spacing on display sizes (-2px to -0.5px)
- Generous body leading (1.55) for documentation readability
- 600 weight for headlines + 500 for buttons; 400 body

## Layout

### Spacing System
- **Base unit**: 4px (8px primary increment)
- **Tokens**: `{spacing.xxs}` (4px) through `{spacing.hero}` (120px)
- **Section rhythm**: Marketing pages use `{spacing.section-lg}` (96px); pricing tightens to `{spacing.section}` (64px)

### Grid & Container
- 1280px max-width with 32px gutters
- Pricing: 4-tier card row at desktop with dense comparison table
- Homepage: centered hero with workspace mockup below buttons; alternating colorful feature card sections

### Whitespace Philosophy
Marketing surfaces use generous breathing room between feature card bands. Workspace mockup card on hero gets full-width treatment with deep drop shadow.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow; `{colors.hairline}` border | Default cards, table rows |
| 1 (subtle) | `{shadow.subtle}` — `rgba(15, 15, 15, 0.04) 0px 1px 2px 0px` | Hover-elevated tiles |
| 2 (card) | `{shadow.card}` — `rgba(15, 15, 15, 0.08) 0px 4px 12px 0px` | Feature cards |
| 3 (mockup) | `{shadow.mockup}` — `rgba(15, 15, 15, 0.20) 0px 24px 48px -8px` | Hero workspace mockup card |
| 4 (modal) | `{shadow.modal}` — `rgba(15, 15, 15, 0.16) 0px 16px 48px -8px` | Modals, dropdowns |

Elevation is expressed one way per level: levels 1–4 are shadow-only and level 0 is border-only. A card never carries both a `{shadow.*}` value and a hairline border, with one documented exception — `workspace-mockup-card` keeps its `{colors.hairline}` edge under `{shadow.mockup}` because it sits on the navy band, where a shadow alone leaves no visible boundary.

### Decorative Depth
- Hero workspace mockup card uses deep diffuse drop shadow (Level 3) — significant elevation against the navy band
- Pastel feature cards carry their own visual weight via tint backgrounds
- Sticky-note dot illustrations and mesh wires add atmospheric decoration to navy hero

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Tag chips |
| `{rounded.sm}` | 6px | Type badges |
| `{rounded.md}` | 8px | Buttons, inputs, search-pill |
| `{rounded.lg}` | 12px | Cards, pricing tiers, agent tiles, workspace mockup |
| `{rounded.xl}` | 16px | Larger feature panels |
| `{rounded.xxl}` | 20px | Featured product showcases |
| `{rounded.xxxl}` | 24px | Larger feature cards |
| `{rounded.full}` | 9999px | Status badges, pill tabs (NOT regular buttons) |

Notion's geometry is sober-editorial — `{rounded.md}` (8px) buttons distinguish it from pill-button-everywhere brands.

## Components

> States: the extracted captures carry `button-primary-pressed`, `button-primary-disabled`, `text-input-focused`, `pill-tab-active` and `segmented-tab-active`. Hover, focus-visible, loading, selected and error were **not** observable in a static capture, so the Interaction States table below prescribes them from the extracted pressed/active variants and this file's own tokens. Prescribed rows are marked.

### Buttons

**`button-primary`** — Signature purple rectangular primary CTA, the dominant action.
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.button-md}`, padding `10px 18px`, rounded `{rounded.md}`.
- Pressed state `button-primary-pressed` deepens to `{colors.primary-pressed}`.
- Disabled state uses `{colors.hairline}` background.

**`button-dark`** — Black rectangular CTA on light backgrounds.
- Background `{colors.ink-deep}`, text `{colors.on-dark}`, typography `{typography.button-md}`, padding `10px 18px`, rounded `{rounded.md}`.

**`button-secondary`** — Outlined rectangular for secondary actions ("Request a demo").
- Background transparent, text `{colors.ink}`, border `1px solid {colors.hairline-strong}`, typography `{typography.button-md}`, padding `10px 18px`, rounded `{rounded.md}`.

**`button-on-dark`** — White button on dark hero bands.
- Background `{colors.on-dark}`, text `{colors.ink}`, typography `{typography.button-md}`, padding `10px 18px`, rounded `{rounded.md}`.

**`button-secondary-on-dark`** — Outlined button on dark.
- Background transparent, text `{colors.on-dark}`, border `1px solid {colors.on-dark-muted}`, typography `{typography.button-md}`, padding `10px 18px`, rounded `{rounded.md}`.

**`button-ghost`** — Quieter ghost button.
- Background transparent, text `{colors.ink}`, typography `{typography.button-md}`, padding `8px 12px`, rounded `{rounded.sm}`.

**`button-link`** — Inline blue text link (NOT primary purple).
- Background transparent, text `{colors.link-blue}`, typography `{typography.body-sm-medium}`, padding `0`.

### Cards & Containers

**`card-base`** — Standard content card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`card-feature`** — Feature card with larger padding.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`card-feature-yellow-bold`** — Bold yellow feature banner for high-emphasis content ("Ask your on-demand assistants").
- Background `{colors.card-tint-yellow-bold}`, text `{colors.charcoal}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`.

**`card-feature-peach`** + **`card-feature-rose`** + **`card-feature-mint`** + **`card-feature-sky`** + **`card-feature-lavender`** + **`card-feature-yellow`** + **`card-feature-cream`** — Pastel-tinted feature cards.
- Each variant uses its corresponding `card-tint-*` color as background, text `{colors.charcoal}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`.

**`card-agent-tile`** — Agent assistant tile.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`card-template`** — Template thumbnail card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.lg}`, border `1px solid {colors.hairline}`.

**`card-startup-perk`** — Startup-program perk grid item.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`pricing-card`** — Standard pricing tier card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`pricing-card-featured`** — Featured pricing tier (Plus or Business — purple-bordered).
- Background `{colors.surface}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `2px solid {colors.primary}`.

### Inputs & Forms

**`text-input`** — Standard text field.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline-strong}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, height 44px.

**`text-input-focused`** — Activated state.
- Border switches to `2px solid {colors.primary}` (purple).

**`search-pill`** — Search bar.
- Background `{colors.surface}`, text `{colors.steel}`, typography `{typography.body-md}`, rounded `{rounded.md}`, height 44px, border `1px solid {colors.hairline}`.

### Tabs

**`pill-tab`** + **`pill-tab-active`** — Pill-style tab nav for top-level switching.
- Inactive: text `{colors.steel}`, border `1px solid {colors.hairline}`, padding `{spacing.xs} {spacing.md}`, rounded `{rounded.full}`.
- Active: background `{colors.ink-deep}`, text `{colors.on-dark}`.

**`segmented-tab`** + **`segmented-tab-active`** — Underline-style tab navigation.
- Inactive: text `{colors.steel}`, no border. Active: text `{colors.ink}`, 2px bottom border in `{colors.ink}`.

### Badges & Status

**`badge-purple`** — Purple status badge (matches primary CTA).
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-pink`** — Pink accent badge.
- Background `{colors.brand-pink}`, text `{colors.on-primary}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-orange`** — Orange accent badge.
- Background `{colors.brand-orange}`, text `{colors.on-primary}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-tag-purple`** — Soft-purple feature tag chip.
- Background `{colors.card-tint-lavender}`, text `{colors.brand-purple-800}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 8px`.

**`badge-tag-orange`** — Soft-orange feature tag.
- Background `{colors.card-tint-peach}`, text `{colors.brand-orange-deep}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 8px`.

**`badge-tag-green`** — Soft-mint feature tag.
- Background `{colors.card-tint-mint}`, text `{colors.brand-green}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 8px`.

**`badge-popular`** — "Most Popular" tier indicator.
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`promo-banner`** — Light surface promo strip ABOVE the top nav.
- Background `{colors.surface}`, text `{colors.ink}`, typography `{typography.body-sm-medium}`, padding `{spacing.sm} {spacing.md}`. ("Developers: Get a first look at our new Developer Platform on May 13.")

### Tables

**`comparison-table`** — Pricing feature comparison table.
- Background `{colors.canvas}`, text `{colors.ink}`, typography `{typography.body-sm}`, rounded `{rounded.md}`, border `1px solid {colors.hairline}`.

**`comparison-row`** — Individual feature row.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.lg}`, bottom border `1px solid {colors.hairline-soft}`.

### Documentation Components

**`workspace-mockup-card`** — Embedded Notion workspace UI mockup on hero band ("Ramp HQ" kanban board).
- Background `{colors.canvas}`, rounded `{rounded.lg}`, border `1px solid {colors.hairline}`, deep shadow `rgba(15, 15, 15, 0.20) 0px 24px 48px -8px`. Carries actual Notion product UI mock.

**`testimonial-card`** — Customer testimonial card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`logo-wall-item`** — Customer logo wordmark cell.
- Background transparent, text `{colors.steel}`, typography `{typography.body-md-medium}`, padding `{spacing.lg}`.

**`faq-accordion-item`** — FAQ panel.
- Background `{colors.canvas}`, rounded `{rounded.md}`, padding `{spacing.xl}`, bottom border `1px solid {colors.hairline}`.

**`stat-row`** — Stats strip with bar chart visualization ("More productivity. Fewer tools.").
- Background `{colors.surface}`, text `{colors.ink}`, rounded `{rounded.lg}`, padding `{spacing.section-sm}`.

**`cta-banner-light`** — Light surface CTA banner.
- Background `{colors.surface}`, text `{colors.ink}`, rounded `{rounded.lg}`, padding `{spacing.section}`.

### Navigation

**Top Navigation (Marketing)** — Sticky white bar.
- Background `{colors.canvas}`, height ~64px, bottom border `1px solid {colors.hairline}`.
- Left: Notion "N" logo + "Product / AI / Solutions / Resources / Enterprise / Pricing / Request a demo" links.
- Right: "Get Notion free" purple button + "Log in" link.

### Signature Components

**`hero-band-dark`** — Deep navy hero band with embedded workspace mockup and decorative dots/wires.
- Background `{colors.brand-navy}`, text `{colors.on-dark}`, padding `{spacing.hero}`.
- Layout: centered headline `{typography.hero-display}`, subtitle, button row (`button-primary` purple + `button-secondary-on-dark`), `workspace-mockup-card` below.
- Atmospheric decoration: scattered colorful sticky-note dots and mesh wire illustrations around the hero content (NOT a literal pattern fill — handled per-page via SVG/illustration).

**`footer-region`** — Multi-column light footer.
- Background `{colors.canvas}`, padding `{spacing.section} {spacing.xxl}`, top border `1px solid {colors.hairline}`.
- 6-column link grid (Product / Download / Resources / Notion for / Company / Legal).

**`footer-link`** — Individual footer link.
- Background transparent, text `{colors.steel}`, typography `{typography.body-sm}`, padding `{spacing.xxs} 0`.

### Interaction States

Extracted variants are named in the Component column; everything else in this table is **prescribed** (marked *P*) and was not measured from the live site.

| Component | States | Treatment |
|---|---|---|
| `button-primary` | default, hover *P*, focus-visible *P*, pressed, disabled, loading *P* | hover deepens to `{colors.primary-pressed}`; pressed is the extracted `button-primary-pressed`; focus-visible draws the 2px `{colors.focus}` ring with 2px offset; disabled is the extracted `button-primary-disabled`; loading swaps the label for a spinner at `{motion.duration-base}` and keeps the button width fixed |
| `button-dark`, `button-on-dark`, `button-secondary-on-dark` | default, hover *P*, focus-visible *P*, pressed *P*, disabled *P* | hover shifts fill one step; focus-visible on the navy band draws `{colors.focus-on-dark}`, on light surfaces `{colors.focus}` |
| `button-secondary`, `button-ghost` | default, hover *P*, focus-visible *P*, pressed *P*, disabled *P* | hover fills with `{colors.surface}`; border moves to `{colors.steel}` so the boundary clears 3:1 |
| `button-link` | default, hover *P*, focus-visible *P*, pressed, disabled *P* | hover underlines; pressed is the extracted `{colors.link-blue-pressed}` |
| `text-input` | default, hover *P*, focus-visible, disabled *P*, error *P* | focus-visible is the extracted `text-input-focused` (2px `{colors.primary}`); error draws a 2px `{colors.semantic-error}` border plus a `{typography.caption}` message in `{colors.semantic-error}` |
| `search-pill` | default, hover *P*, focus-visible *P*, loading *P* | loading shows an indeterminate indicator; placeholder ink is `{colors.steel}`, never `{colors.muted}` |
| `pill-tab` | default, hover *P*, focus-visible *P*, selected, disabled *P* | selected is the extracted `pill-tab-active` (`{colors.ink-deep}` fill) |
| `segmented-tab` | default, hover *P*, focus-visible *P*, selected | selected is the extracted `segmented-tab-active` (2px `{colors.ink}` underline); the underline is the state carrier, not colour alone |
| `card-base`, `card-feature`, `card-agent-tile`, `card-template`, `card-startup-perk`, `testimonial-card` | default, hover *P*, focus-visible *P* | hover lifts from level 0 to `{shadow.subtle}`; these are non-interactive unless the whole card is a link, in which case focus-visible rings the card |
| `card-feature-*` (pastel tints) | default only | genuinely static decorative panels — no interactive state |
| `pricing-card` | default, hover *P*, focus-visible *P*, selected | selected is the extracted `pricing-card-featured` (2px `{colors.primary}` border + `{colors.surface}` fill) |
| `faq-accordion-item` | default, hover *P*, focus-visible *P*, selected *P* | selected = expanded; the chevron rotates and the panel reveals |
| `comparison-row` | default, hover *P* | hover tints the row with `{colors.surface}` |
| `badge-purple`, `badge-pink`, `badge-orange`, `badge-tag-*`, `badge-popular` | default only | static status labels — no interactive state |
| `promo-banner`, `cta-banner-light`, `stat-row`, `hero-band-dark`, `logo-wall-item`, `footer-region` | default only | static containers — no interactive state |
| `footer-link` | default, hover *P*, focus-visible *P* | hover darkens to `{colors.ink}` |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or transition was extracted from notion.com; the only motion fact the capture carried is the Known Gaps note recommending 150–200ms, which the **Crisp** profile's `{motion.duration-base}` (150ms) matches. Treat every value below as a specification to build to, not an observation.

Crisp is the right profile for a workspace tool: a state change should read as instant, there is no entrance choreography, and the file's own geometry is described as sober-editorial rather than springy. Values are the Crisp block from the audit spec, used verbatim so this file stays comparable with its siblings.

Animate `transform` and `opacity` only — never `width`, `height`, `top`, `left` or `margin`. Every exit is shorter than its matching entrance.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, row) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `transform: translateY(-1px)` on cards | travel removed; `opacity` only at `{motion.duration-reduced}` |
| Press | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | no scale; colour change applies immediately |
| Focus (ring appear) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the `{colors.focus}` ring | ring appears instantly, no fade |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` | `opacity` only at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` → `0` | `opacity` only at `{motion.duration-reduced}`; no travel |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform: translateY(4px)` | `opacity` only at `{motion.duration-reduced}` |
| Dropdown / menu enter | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(4px)` → `0` | `opacity` only at `{motion.duration-reduced}` |
| Dropdown / menu exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | `opacity` only at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` → `0` | `opacity` only at `{motion.duration-reduced}` |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | `opacity` only at `{motion.duration-reduced}` |
| List / grid enter (feature cards, pricing tiers) | `{motion.duration-base}`, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity`, `transform: translateY(6px)` → `0` | stagger and travel removed; all items fade together at `{motion.duration-reduced}` |
| List / grid exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` | `opacity` only at `{motion.duration-reduced}` |
| Loading (spinner, skeleton) | 800ms linear loop (spinner); `{motion.duration-slow}` skeleton pulse | linear / `{motion.ease-standard}` | `transform: rotate()` (spinner), `opacity` (skeleton) | spinner replaced by a static indicator; skeleton pulse frozen at its mid-opacity |
| Accordion expand (`faq-accordion-item`) | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` + `transform: scaleY()` on the panel, `transform: rotate(180deg)` on the chevron | panel appears with `opacity` only at `{motion.duration-reduced}`; chevron rotation removed |

### Emphasis and ambience

`{motion.duration-emphasis}` (300ms) is reserved for the hero workspace mockup card settling into place on first view — a single `opacity` + `transform: translateY(12px)` move that never delays the headline or the CTA row. Nothing else animates on first paint. There is no infinite brand ambience in this system; the only looping animation is the loader.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate, scale and rotate; all stagger; the hero
     mockup entrance; the skeleton pulse and the spinner rotation. */
  /* Kept: opacity fades only, capped at {motion.duration-reduced} (100ms). */
  *, *::before, *::after {
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;
    transition-property: opacity !important;
  }
}
```

Removed: every `transform` — translate, scale and rotate alike — the `{motion.stagger-step}` delay on list and grid entrances, the hero mockup's entrance move, the chevron rotation, and the looping spinner and skeleton pulse, which freeze. Kept: `opacity` fades at `{motion.duration-reduced}` (100ms), the focus ring, and every colour change, which applies immediately.

## Accessibility

Ratios below are computed with WCAG 2.1 relative luminance from this file's own token values. Nothing here is a rendered measurement: tap-target size, overlap and clipping cannot be verified from a document, and the figures given for them are the file's own stated values, not observations.

### Measured contrast — passing

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 17.40:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.surface}` | 15.98:1 | 4.5:1 | pass |
| `{colors.charcoal}` on `{colors.canvas}` | 12.26:1 | 4.5:1 | pass |
| `{colors.slate}` on `{colors.canvas}` | 6.80:1 | 4.5:1 | pass — the correct token for secondary text |
| `{colors.steel}` on `{colors.canvas}` | 4.54:1 | 4.5:1 | pass (fails on `{colors.surface}`, below) |
| `{colors.on-primary}` on `{colors.primary}` | 6.57:1 | 4.5:1 | pass |
| `{colors.link-blue}` on `{colors.canvas}` | 4.57:1 | 4.5:1 | pass |
| `{colors.semantic-error}` on `{colors.canvas}` | 4.51:1 | 4.5:1 | pass, with no margin |
| `{colors.on-dark}` on `{colors.brand-navy}` | 18.06:1 | 4.5:1 | pass |
| `{colors.on-dark-muted}` on `{colors.brand-navy}` | 6.93:1 | 4.5:1 | pass |
| `{colors.charcoal}` on every `card-tint-*` | 9.54:1 – 11.38:1 | 4.5:1 | pass |
| `{colors.brand-purple-800}` on `{colors.card-tint-lavender}` | 11.06:1 | 4.5:1 | pass |
| `{colors.brand-orange-deep}` on `{colors.card-tint-peach}` | 7.70:1 | 4.5:1 | pass |

### Measured contrast — real brand failures

These are extracted values and are left unchanged. The brand genuinely fails AA at each of these points.

| Pair | Ratio | Required | Note |
|---|---|---|---|
| `hairline-soft` (#ede9e4) on `surface` (#f6f5f4) | 1.11:1 | 3.0:1 | decorative divider only |
| `hairline` (#e5e3df) on `surface` (#f6f5f4) | 1.18:1 | 3.0:1 | decorative divider only |
| `hairline-soft` (#ede9e4) on `canvas` (#ffffff) | 1.21:1 | 3.0:1 | decorative divider only |
| `hairline` (#e5e3df) on `canvas` (#ffffff) | 1.28:1 | 3.0:1 | the card border across the whole system; invisible as a boundary |
| `hairline-strong` (#c8c4be) on `surface` (#f6f5f4) | 1.59:1 | 3.0:1 | input border on tinted sections |
| `hairline-strong` (#c8c4be) on `canvas` (#ffffff) | 1.74:1 | 3.0:1 | the strongest extracted border still fails 1.4.11; draw `{colors.steel}` where a control edge must be perceivable |
| `muted` (#bbb8b1) on `surface` (#f6f5f4) | 1.82:1 | 4.5:1 | disabled/placeholder ink; never secondary text |
| `muted` (#bbb8b1) on `canvas` (#ffffff) | 1.98:1 | 4.5:1 | the weakest ink in the palette. Placeholder text in this tone is unreadable; use `{colors.steel}` for placeholders and `{colors.slate}` for secondary text |
| `semantic-success` (#1aae39) on `canvas` (#ffffff) | 2.93:1 | 4.5:1 | fill and icon tone only, never text |
| `semantic-warning` (#dd5b00) on `canvas` (#ffffff) | 3.77:1 | 4.5:1 | passes only as 24px+ text, or 18.66px+ at weight 700 |
| `search-pill` — `{colors.steel}` on `{colors.surface}` | 4.17:1 | 4.5:1 | 16px placeholder ink on the tinted search field |
| `badge-pink` — `#ffffff` on `{colors.brand-pink}` | 2.66:1 | 4.5:1 | 13px/600 label; the worst component pair in the file |
| `badge-orange` — `#ffffff` on `{colors.brand-orange}` | 3.77:1 | 4.5:1 | 13px/600 label |
| `badge-tag-green` — `{colors.brand-green}` on `{colors.card-tint-mint}` | 2.50:1 | 4.5:1 | 13px/600 tag label |

### Focus ring visibility

Prescribed; see the Focus subsection under Colors. Ring is 2px with a 2px offset in the surface colour, drawn outside the control, and is measured against the surface behind it.

| Surface | Ring | Ratio |
|---|---|---|
| `{colors.canvas}` | `{colors.focus}` | 10.65:1 |
| `{colors.surface}` | `{colors.focus}` | 9.78:1 |
| `{colors.surface-soft}` | `{colors.focus}` | 10.20:1 |
| `card-tint-lavender` (weakest tint) | `{colors.focus}` | 8.29:1 |
| `card-tint-yellow` (strongest tint) | `{colors.focus}` | 9.89:1 |
| `{colors.brand-navy}` hero band | `{colors.focus-on-dark}` | 10.22:1 |
| `{colors.brand-navy-mid}` | `{colors.focus-on-dark}` | 7.94:1 |
| `{colors.ink-deep}` (`button-dark`, `pill-tab-active`) | `{colors.focus-on-dark}` | 11.88:1 |

Every surface this file defines clears 3:1 against one of the two rings. Focus is never signalled by colour alone: `segmented-tab-active` carries a 2px underline and `pill-tab-active` changes fill, so state survives without colour perception.

### Minimum tap target

Taken from this file's own stated values, not from a rendered page. `text-input` and `search-pill` declare 44px height; the Responsive Behavior section states buttons render at 40–44px effective height and pill tabs at ~32px rising to 44px on mobile. The 40px buttons and the ~32px desktop pill tabs are **below** the 44x44px target of WCAG 2.5.5 (AAA) though they meet the 24x24px minimum of 2.5.8 (AA). `footer-link` at `{spacing.xxs} 0` padding on 14px type is roughly 22px tall and needs a larger hit area than its visual box.

### Reduced motion

All motion in this file is prescribed. Under `@media (prefers-reduced-motion: reduce)` every transform, stagger and loop is removed and only `opacity` fades remain, capped at `{motion.duration-reduced}` (100ms). See Motion & Animation.

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
| `{colors.semantic-success}` (`#1aae39`) on `{colors.surface}` (`#f6f5f4`) | 2.69:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.semantic-warning}` (`#dd5b00`) on `{colors.surface}` (`#f6f5f4`) | 3.46:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.semantic-error}` (`#e03131`) on `{colors.surface}` (`#f6f5f4`) | 4.14:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.link-blue}` (`#0075de`) on `{colors.surface}` (`#f6f5f4`) | 4.19:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Use `{colors.primary}` (purple) as the dominant CTA across all surfaces — it's the brand's recognizable signal
- Pair deep navy hero bands ({colors.brand-navy}) with the purple button + decorative sticky-note dots
- Use pastel feature card tints (peach, rose, mint, lavender, sky, yellow) generously
- Use `{colors.card-tint-yellow-bold}` for high-emphasis "Ask the assistant"-style banner cards
- Apply `{rounded.md}` (8px) to buttons consistently — Notion uses rectangles, not pills
- Apply `{rounded.lg}` (12px) to all card families
- Maintain Notion-Sans across every UI surface
- Use the workspace mockup card on hero bands to show actual product UI

### Don't
- Don't use the purple for body text or large background surfaces
- Don't use pill-shaped buttons; Notion's geometry is rectangular-sober
- Don't mix link-blue ({colors.link-blue}) with primary-purple ({colors.primary}) — they have distinct roles
- Don't apply heavy shadows on flat documentation cards
- Don't replace Notion-Sans with a generic Inter
- Don't set secondary or placeholder text in `{colors.muted}` — at 1.98:1 on {colors.canvas} it is unreadable; use `{colors.slate}` or `{colors.steel}`
- Don't rely on a `{colors.hairline}` border as the only boundary of an input or control; it measures 1.28:1
- Don't use `{colors.semantic-success}` or `{colors.brand-green}` as text — they are fill and icon tones
- Don't animate `width`, `height`, `top`, `left` or `margin`; transform and opacity only

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile (small) | < 480px | Single column. Hero 36px. Pricing 1-up. |
| Mobile (large) | 480 – 767px | Feature cards 2-up. Hero 48px. |
| Tablet | 768 – 1023px | 2-column feature grids. Hero 56px. |
| Desktop | 1024 – 1279px | 4-tier pricing card row. Hero 72px. |
| Wide Desktop | ≥ 1280px | Full 80px hero presentation. |

### Touch Targets
- Buttons render at 40–44px effective height
- Form inputs render at 44px height
- Pill tabs ~32px → 44px on mobile

### Collapsing Strategy
- **Promo banner** stays full-width; truncates at < 480px
- **Top nav** below 1024px collapses to hamburger
- **Hero band**: workspace mockup card moves below text/buttons on mobile
- **Pricing tiers**: 4-column → 2-column tablet → 1-column mobile
- **Feature cards**: 3-up desktop → 2-up tablet → 1-up mobile
- **Hero typography**: 80px → 56px → 48px → 36px
- **Footer**: 6-column desktop → 3-column tablet → accordion mobile

### Image Behavior
- Workspace mockup card maintains aspect ratio
- Pastel illustrations inside feature cards scale proportionally
- Customer logo wall: wordmarks at consistent 60–80px height

## Iteration Guide

1. Focus on ONE component at a time
2. Reference component names and tokens directly
3. Run `npx @google/design.md lint DESIGN.md` after edits
4. Add new variants as separate `components:` entries
5. Default to `{typography.body-md}` for body
6. Keep `{colors.primary}` (purple) as the primary CTA — distinct from `{colors.link-blue}` for inline links
7. Use `{rounded.md}` for buttons (rectangles), `{rounded.lg}` for cards, `{rounded.full}` for pill tabs/badges only

## Known Gaps

- Specific dark-mode token values not surfaced beyond hero bands
- Animation/transition timings not extracted. The Motion & Animation section is **prescribed** (Crisp profile), not observed; its 150ms `{motion.duration-base}` matches the 150–200ms this file originally recommended, but nothing in it was measured from notion.com
- Focus ring not observable in the capture. `{colors.focus}` and `{colors.focus-on-dark}` are prescribed, reusing the extracted `{colors.primary-deep}` and `{colors.brand-purple-300}` hexes
- Hover, focus-visible, loading, selected and error treatments are prescribed; only pressed, focused-input and active-tab variants were extracted. An earlier revision of this file claimed a "no-hover policy" as the reason hover was undocumented — no such policy exists in the repo's README or CONTRIBUTING, so the claim has been withdrawn and the states are documented as prescribed instead
- Tap-target sizes quoted in Accessibility are this file's own declared values; nothing was measured on a rendered page
- Form validation success state not explicitly captured
- Pastel-tint mapping (which feature uses which tint) is observation-based — the actual brand library may have more entries
