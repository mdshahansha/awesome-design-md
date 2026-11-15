---
version: alpha
name: MongoDB-design-analysis
description: MongoDB carries a strong dual-mode visual identity — dark deep-teal hero bands with bright MongoDB green ({colors.brand-green}) CTAs paired with stark white documentation surfaces. The signature green pill button is unmistakable across product, pricing, learning, and AI use-case surfaces. The system uses Euclid Circular A as its display face, anchors a 3-tier pricing comparison (Free / Flex / Dedicated), and presents extensive course catalogs in card grids with colored category tags. Coverage spans homepage, Atlas product page, Community Edition, MongoDB University, AI use cases, and pricing.

colors:
  primary: "#00ed64"
  primary-deep: "#00b545"
  primary-pressed: "#008c34"
  on-primary: "#001e2b"
  brand-green: "#00ed64"
  brand-green-dark: "#00684a"
  brand-green-mid: "#00a35c"
  brand-green-soft: "#c3f0d2"
  brand-teal-deep: "#001e2b"
  brand-teal: "#003d4f"
  brand-teal-mid: "#00684a"
  accent-purple: "#7b3ff2"
  accent-orange: "#fa6e39"
  accent-pink: "#f06bb8"
  accent-blue: "#3d4f9f"
  semantic-warning-bg: "#fff8e0"
  semantic-warning-text: "#946f3f"
  canvas: "#ffffff"
  canvas-dark: "#001e2b"
  surface: "#f9fbfa"
  surface-soft: "#f4f7f6"
  surface-feature: "#e3fcef"
  hairline: "#e1e5e8"
  hairline-soft: "#eceff1"
  hairline-strong: "#c1ccd6"
  hairline-dark: "#1c2d38"
  hairline-control: "#6b7a88"
  ink: "#001e2b"
  charcoal: "#1c2d38"
  slate: "#3d4f5b"
  steel: "#5c6c7a"
  stone: "#7c8c9a"
  muted: "#a8b3bc"
  on-dark: "#ffffff"
  on-dark-muted: "#a8b3bc"
  focus: "#00684a"
  focus-on-dark: "#00ed64"

typography:
  hero-display:
    fontFamily: Euclid Circular A
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1.10
    letterSpacing: -1.5px
  display-lg:
    fontFamily: Euclid Circular A
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -1px
  heading-1:
    fontFamily: Euclid Circular A
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.5px
  heading-2:
    fontFamily: Euclid Circular A
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  heading-3:
    fontFamily: Euclid Circular A
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.30
  heading-4:
    fontFamily: Euclid Circular A
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.35
  heading-5:
    fontFamily: Euclid Circular A
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.40
  subtitle:
    fontFamily: Euclid Circular A
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
  body-md:
    fontFamily: Euclid Circular A
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  body-md-medium:
    fontFamily: Euclid Circular A
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.55
  body-sm:
    fontFamily: Euclid Circular A
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
  body-sm-medium:
    fontFamily: Euclid Circular A
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
  caption:
    fontFamily: Euclid Circular A
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.40
  caption-bold:
    fontFamily: Euclid Circular A
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.40
  micro:
    fontFamily: Euclid Circular A
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
  micro-uppercase:
    fontFamily: Euclid Circular A
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 1px
  button-md:
    fontFamily: Euclid Circular A
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
  code-md:
    fontFamily: Source Code Pro
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
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
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 22px"
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 22px"
    border: "1px solid {colors.hairline-strong}"
  button-on-dark:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 22px"
  button-secondary-on-dark:
    backgroundColor: "{colors.brand-teal-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 22px"
    border: "1px solid {colors.hairline-dark}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "8px 12px"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.brand-green-dark}"
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
  card-product-deploy:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  card-feature-dark:
    backgroundColor: "{colors.brand-teal-deep}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-course:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  card-cert:
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
    backgroundColor: "{colors.surface-feature}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "2px solid {colors.brand-green}"
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
    border: "2px solid {colors.focus}"
  search-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.steel}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline-strong}"
  search-pill-large:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.steel}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    height: 56px
    border: "1px solid {colors.hairline-strong}"
  pill-tab:
    backgroundColor: "transparent"
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
    textColor: "{colors.brand-green-dark}"
    typography: "{typography.body-sm-medium}"
    border: "0 0 2px {colors.brand-green-dark} solid"
  badge-green:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-green-soft:
    backgroundColor: "{colors.brand-green-soft}"
    textColor: "{colors.brand-green-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-popular:
    backgroundColor: "{colors.brand-teal-deep}"
    textColor: "{colors.brand-green}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  promo-banner:
    backgroundColor: "{colors.brand-teal-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm-medium}"
    padding: "{spacing.sm} {spacing.md}"
  hero-band-dark:
    backgroundColor: "{colors.brand-teal-deep}"
    textColor: "{colors.on-dark}"
    rounded: "0"
    padding: "{spacing.hero}"
  hero-platform-card:
    backgroundColor: "{colors.brand-teal-mid}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
  cta-banner-dark:
    backgroundColor: "{colors.brand-teal-deep}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.section}"
  code-block:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  code-mockup-card:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
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
  service-tile:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  why-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  customer-testimonial-card:
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
  footer-region:
    backgroundColor: "{colors.brand-teal-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  focus-ring:
    border: "2px solid {colors.focus}"
    outlineOffset: "2px"
    rounded: "{rounded.full}"
  focus-ring-on-dark:
    border: "2px solid {colors.focus-on-dark}"
    outlineOffset: "2px"
    rounded: "{rounded.full}"
  footer-link:
    backgroundColor: "{colors.brand-teal-deep}"
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxs} 0"
---

## Overview

MongoDB carries a strong dual-mode visual identity — dark deep-teal hero bands with the unmistakable bright MongoDB green ({colors.brand-green}) CTA pill paired with stark white documentation and pricing surfaces. The homepage opens with "One data platform. Unlimited AI potential." headline over a deep navy hero, the green pill sitting at the visual center as the primary CTA. Lower on the page, embedded code mockup cards (terminal-aesthetic) sit on the dark hero band, breaking out into white feature cards below. The pricing page renders a 3-tier comparison (Free / Flex / Dedicated) with a featured tier highlighted in soft mint background and bright green border. The MongoDB University page presents a course catalog grid where each tile carries a colored category tag (orange, purple, green, teal) — these are MongoDB's category-encoding accent colors and are the only place outside the brand green where saturated color appears.

The system uses Euclid Circular A as its display face. The face is contemporary geometric — confident but not overly playful — and pairs naturally with both the developer-tool aesthetic of the database product and the educational positioning of the learning surfaces. Cards use `{rounded.lg}` (12px) corners; buttons use `{rounded.full}` pills universally. The brand-teal palette ({colors.brand-teal-deep}) anchors hero bands, footer, code mockups, and the dark CTA banners.

**Key Characteristics:**
- Deep navy/teal hero bands ({colors.brand-teal-deep}) with bright MongoDB green ({colors.brand-green}) CTA pills
- Stark white pricing/documentation surfaces with colored category tags for course tiles (purple, orange, green, teal)
- Euclid Circular A across every UI surface
- Pill-shaped buttons ({rounded.full}) and 12px-rounded cards
- 3-tier pricing comparison (Free / Flex / Dedicated) with featured-mint highlight tier
- Code mockup cards with terminal-aesthetic dark canvas

## Colors

> Source pages: mongodb.com/ (homepage), /products/platform/atlas-database (Atlas product), /products/self-managed/community-edition, learn.mongodb.com/ (MongoDB University), /solutions/use-cases/artificial-intelligence (AI), /pricing (3-tier comparison). Token coverage was identical across all six pages.

### Brand & Accent
- **MongoDB Green** ({colors.brand-green}): The brand's most recognizable signal — bright pill-CTA color
- **Green Dark** ({colors.brand-green-dark}): Inline link color, secondary green
- **Green Mid** ({colors.brand-green-mid}): Mid-spectrum green for atmospheric tints
- **Green Soft** ({colors.brand-green-soft}): Pale-mint background tint for success badges and featured pricing tier
- **Brand Teal Deep** ({colors.brand-teal-deep}): Deep navy-teal for hero bands, footer
- **Brand Teal** ({colors.brand-teal}): Mid-spectrum teal
- **Brand Teal Mid** ({colors.brand-teal-mid}): Lighter teal for hero platform cards

### Category Accent (Course Tags)
- **Accent Purple** ({colors.accent-purple}): Course tag for "Database & Security"
- **Accent Orange** ({colors.accent-orange}): Course tag for "Search"
- **Accent Pink** ({colors.accent-pink}): Course tag variant
- **Accent Blue** ({colors.accent-blue}): Course tag variant for atlas/cloud topics

### Surface
- **Canvas White** ({colors.canvas}): Page background and primary card surface
- **Canvas Dark** ({colors.canvas-dark}): Code-block backgrounds, dark mockup canvas
- **Surface** ({colors.surface}): Subtle section backgrounds, search-pill rest
- **Surface Soft** ({colors.surface-soft}): Quieter section divisions
- **Surface Feature** ({colors.surface-feature}): Pale mint background for featured pricing tier
- **Hairline** ({colors.hairline}): 1px borders and primary dividers
- **Hairline Soft** ({colors.hairline-soft}): Quieter dividers
- **Hairline Strong** ({colors.hairline-strong}): Stronger 1px border for inputs
- **Hairline Dark** ({colors.hairline-dark}): Border on dark surfaces
- **Hairline Control** ({colors.hairline-control}) — **prescribed, not extracted**: accessible control boundary at 4.41:1 on {colors.canvas}. The three extracted hairlines are decorative-only tones (1.15:1 to 1.63:1) and none reaches the 3:1 a control boundary needs; use this token where the border is the only thing defining an interactive control.

### Focus
- **Focus** ({colors.focus}) — **prescribed, not extracted**: MongoDB's own dark green, the hue the file already uses for the focused input border and the active underline tab. 6.82:1 on {colors.canvas}, 6.56:1 on {colors.surface}, 6.31:1 on {colors.surface-feature}.
- **Focus On Dark** ({colors.focus-on-dark}) — **prescribed, not extracted**: bright MongoDB green for rings on the deep-teal bands and code surfaces. 10.89:1 on {colors.brand-teal-deep}. The dual-mode identity needs both: the dark green sits at 2.52:1 on the teal band and cannot serve it.

### Text
- **Ink** ({colors.ink}): Primary headlines and body text (deep navy-teal)
- **Charcoal** ({colors.charcoal}): Body emphasis
- **Slate** ({colors.slate}): Secondary text
- **Steel** ({colors.steel}): Tertiary text, captions
- **Stone** ({colors.stone}): Muted labels
- **Muted** ({colors.muted}): Disabled, placeholders
- **On Dark** ({colors.on-dark}): White text on dark surfaces
- **On Dark Muted** ({colors.on-dark-muted}): Reduced-opacity white

### Semantic
- **Warning Background** ({colors.semantic-warning-bg}): Pale yellow callout bg
- **Warning Text** ({colors.semantic-warning-text}): Warning state copy color

## Typography

### Font Family
**Euclid Circular A** (primary): MongoDB's geometric sans-serif. Fallbacks: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif.
**Source Code Pro** (code): Monospace for code mockups. Fallbacks: 'SF Mono', Menlo, Consolas, monospace.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 72px | 500 | 1.10 | -1.5px | Hero ("One data platform") |
| `{typography.display-lg}` | 56px | 500 | 1.15 | -1px | Major section openers |
| `{typography.heading-1}` | 48px | 500 | 1.20 | -0.5px | Page-level headlines |
| `{typography.heading-2}` | 36px | 500 | 1.25 | -0.5px | Subsection headlines |
| `{typography.heading-3}` | 28px | 500 | 1.30 | 0 | Card titles |
| `{typography.heading-4}` | 22px | 500 | 1.35 | 0 | Feature tile titles |
| `{typography.heading-5}` | 18px | 600 | 1.40 | 0 | Smaller card titles, FAQ questions |
| `{typography.subtitle}` | 18px | 400 | 1.50 | 0 | Hero subtitle, lead body |
| `{typography.body-md}` | 16px | 400 | 1.55 | 0 | Primary body text |
| `{typography.body-sm}` | 14px | 400 | 1.50 | 0 | Secondary body, table cells |
| `{typography.body-sm-medium}` | 14px | 500 | 1.50 | 0 | Active sidebar, button labels |
| `{typography.caption-bold}` | 13px | 600 | 1.40 | 0 | Badge labels |
| `{typography.micro-uppercase}` | 11px | 600 | 1.40 | 1px | Section eyebrows, course category tags |
| `{typography.button-md}` | 14px | 600 | 1.30 | 0 | Pill button labels |
| `{typography.code-md}` | 14px | 400 | 1.55 | 0 | Code mockups |

### Principles
- Tight hero leading (1.10) on 72px display
- Negative letter-spacing on display sizes (-1.5px to -0.5px)
- 600 weight reserved for buttons and small emphasis (FAQ headings, badges)
- Generous body leading (1.55) for technical documentation readability

## Layout

### Spacing System
- **Base unit**: 4px (8px primary increment)
- **Tokens**: `{spacing.xxs}` (4px) through `{spacing.hero}` (120px)
- **Section rhythm**: Marketing pages use `{spacing.section-lg}` (96px); pricing tightens to `{spacing.section}` (64px)

### Grid & Container
- 1280px max-width with 32px gutters
- Pricing: 3-tier card row, dense feature comparison table below
- Learn catalog: 3-up course tile grid, 4-up certification grid
- AI use cases: 2-column hero with atmospheric illustration

### Whitespace Philosophy
Marketing surfaces give content generous breathing room — `{spacing.hero}` (120px) hero padding for deep teal bands. Pricing/learn surfaces tighten dramatically.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow; `{colors.hairline}` border | Default cards, table rows |
| 1 (subtle) | `rgba(0, 30, 43, 0.04) 0px 1px 2px 0px` | Hover-elevated tiles |
| 2 (card) | `rgba(0, 30, 43, 0.08) 0px 4px 12px 0px` | Feature cards |
| 3 (mockup) | `rgba(0, 30, 43, 0.12) 0px 12px 24px -4px` | Code mockup over hero |
| 4 (modal) | `rgba(0, 30, 43, 0.16) 0px 16px 48px -8px` | Modals, dropdowns |

Elevation is expressed one way per level and the two mechanisms do not mix: level 0 is a border with no shadow, levels 1–4 are shadow with no border.

Layer separation is small by design: `{colors.canvas}` to `{colors.surface}` is 1.04:1, `{colors.surface}` to `{colors.surface-soft}` 1.04:1, `{colors.canvas}` to `{colors.surface-feature}` 1.08:1. The layers are not distinguishable by luminance alone — the hairline border and the padding step carry the separation, and the hairlines themselves sit below 3:1 (see Accessibility). On a dark hero band the separation is the polarity flip, which is unambiguous.

### Decorative Depth
- Dark teal hero bands carry atmospheric gradient depth
- Code mockup cards on hero use canvas-dark surface with terminal aesthetic
- Pale-mint pricing-feature tier uses brand-tinted shadow

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Course category tags |
| `{rounded.sm}` | 6px | Type badges, code chips |
| `{rounded.md}` | 8px | Inputs, search-pill, code blocks |
| `{rounded.lg}` | 12px | Cards, pricing tiers, course tiles |
| `{rounded.xl}` | 16px | Larger feature panels |
| `{rounded.xxl}` | 24px | Featured product showcases |
| `{rounded.full}` | 9999px | All buttons, status badges |

### Photography Geometry
- Hero illustrations sit on full-bleed dark backgrounds
- Course tile thumbnails use `{rounded.lg}` corners
- Customer logos wall: wordmarks at consistent 60–80px height

## Components

> Hover *colour values* are not extracted — static captures cannot show them, and no hover hex below is claimed as observed. State *coverage* is documented: the matrix names every state each component supports, and states other than default and pressed/active are prescribed from the brand's own vocabulary (green pill deepens, ink underline, dark-green ring).

### State Matrix

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | yes | opacity to 0.92 | `focus-ring` | `{colors.primary-pressed}` | `button-primary-disabled` | label swaps to spinner, width held | n/a | n/a |
| `button-secondary` | yes | border to `{colors.hairline-control}` | `focus-ring` | border 2px `{colors.focus}` | 50% opacity | yes | n/a | n/a |
| `button-on-dark` / `button-secondary-on-dark` | yes | opacity to 0.92 | `focus-ring-on-dark` | `{colors.primary-pressed}` | 50% opacity | yes | n/a | n/a |
| `button-ghost` | yes | background `{colors.surface}` | `focus-ring` | background `{colors.surface-soft}` | 50% opacity | n/a | n/a | n/a |
| `button-link` | yes | underline | `focus-ring` | `{colors.brand-green-dark}` | n/a | n/a | n/a | n/a |
| `card-base` / `card-feature` / `service-tile` | yes | elevation 0 to 1 | `focus-ring` when the whole card is a link | n/a | n/a | skeleton block at `{colors.surface}` | n/a | n/a |
| `card-course` / `card-cert` | yes | elevation 0 to 1 | `focus-ring` | n/a | n/a | skeleton block | n/a | n/a |
| `pricing-card` / `pricing-card-featured` | yes | n/a | `focus-ring` on its CTA | n/a | n/a | n/a | featured tier = selected: `{colors.surface-feature}` + 2px `{colors.brand-green}` border | n/a |
| `text-input` | yes | border to `{colors.hairline-control}` | `text-input-focused` (2px `{colors.focus}`) | n/a | background `{colors.surface}`, text `{colors.muted}` | n/a | n/a | 2px border `{colors.accent-orange}` + caption in `{colors.semantic-warning-text}` |
| `search-pill` / `search-pill-large` | yes | border to `{colors.hairline-control}` | `text-input-focused` | n/a | n/a | inline spinner replaces the magnifier | n/a | no-results caption |
| `pill-tab` | yes | border to `{colors.hairline-strong}` | `focus-ring` | `pill-tab-active` | 50% opacity | n/a | `pill-tab-active` (ink fill) | n/a |
| `segmented-tab` | yes | text to `{colors.ink}` | `focus-ring` | `segmented-tab-active` | n/a | n/a | `segmented-tab-active` (2px green underline) | n/a |
| `faq-accordion-item` | yes | text to `{colors.brand-green-dark}` | `focus-ring` on its summary row | n/a | n/a | n/a | expanded = selected | n/a |
| `footer-link` / `logo-wall-item` | yes | underline / full opacity | `focus-ring-on-dark` | n/a | n/a | n/a | n/a | n/a |
| `badge-green` / `badge-green-soft` / `badge-purple` / `badge-orange` / `badge-popular` | yes | n/a — static labels, two states only (present or absent) | n/a | n/a | n/a | n/a | n/a | n/a |
| `promo-banner` / `hero-band-dark` / `hero-platform-card` / `cta-banner-dark` / `code-block` / `code-mockup-card` / `comparison-table` / `comparison-row` / `why-card` / `customer-testimonial-card` / `card-feature-dark` / `footer-region` | yes | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

The last two rows are genuinely single-state: they are layout and label surfaces with no interactive affordance of their own.

**`focus-ring`** / **`focus-ring-on-dark`** — the focus indicator, prescribed.
- Light surfaces: 2px `{colors.focus}` ring drawn *outside* the control with a 2px offset, so it is judged against the surface behind it and never against the control's own fill. Pill controls take `{rounded.full}`.
- Dark bands and code surfaces: 2px `{colors.focus-on-dark}` at the same 2px offset.

### Buttons

**`button-primary`** — Bright MongoDB green pill primary CTA, the dominant action.
- Background `{colors.brand-green}`, text `{colors.on-primary}` (deep navy), typography `{typography.button-md}`, padding `10px 22px`, rounded `{rounded.full}`.
- Pressed state `button-primary-pressed` deepens to `{colors.primary-pressed}`. Ink on that deepened green measures 3.93:1, below 4.5:1 — a real failure in the pressed state only, left as observed.
- Disabled state `button-primary-disabled` uses `{colors.hairline}` background.

**`button-secondary`** — Outlined pill for secondary actions.
- Background transparent, text `{colors.ink}`, border `1px solid {colors.hairline-strong}`, typography `{typography.button-md}`, padding `10px 22px`, rounded `{rounded.full}`.

**`button-on-dark`** — Bright green pill on dark hero bands.
- Background `{colors.brand-green}`, text `{colors.on-primary}`, typography `{typography.button-md}`, padding `10px 22px`, rounded `{rounded.full}`.

**`button-secondary-on-dark`** — Outlined pill on dark backgrounds.
- Fill is transparent; the declared ground is `{colors.brand-teal-deep}`, the hero band it is always drawn on. Text `{colors.on-dark}` (17.2:1 there), border `1px solid {colors.hairline-dark}`, typography `{typography.button-md}`, padding `10px 22px`, rounded `{rounded.full}`.
- The border itself sits at 1.21:1 on the band — it reads as a tint, not a boundary; the white label carries the affordance.

**`button-ghost`** — Quieter rectangular ghost button.
- Background transparent, text `{colors.ink}`, typography `{typography.button-md}`, padding `8px 12px`, rounded `{rounded.md}`.

**`button-link`** — Inline green text link.
- Background transparent, text `{colors.brand-green-dark}`, typography `{typography.body-sm-medium}`, padding `0`.

### Cards & Containers

**`card-base`** — Standard content card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`card-feature`** — Feature card with larger padding.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`card-product-deploy`** — Product deployment card ("MongoDB Atlas / Community").
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`card-feature-dark`** — Dark teal feature card on hero band.
- Background `{colors.brand-teal-deep}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`.

**`card-course`** — MongoDB University course tile.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.
- Top: colored category tag. Below: title `{typography.heading-5}`, description `{typography.body-sm}`, "Get Started →" link.

**`card-cert`** — Certification card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`pricing-card`** — Standard pricing tier card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`pricing-card-featured`** — Featured pricing tier (Flex tier, mint background + green border).
- Background `{colors.surface-feature}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `2px solid {colors.brand-green}`.

### Inputs & Forms

**`text-input`** — Standard text field.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline-strong}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, height 44px.

- The extracted boundary `{colors.hairline-strong}` measures 1.63:1 on `{colors.canvas}`, below the 3:1 a control boundary needs. The value is left as observed; for new work use `{colors.hairline-control}` (4.41:1) and keep the extracted hairlines for decorative dividers.

**`text-input-focused`** — Focus-visible state.
- Border switches to `2px solid {colors.focus}` (the same dark green the live site uses), plus the `focus-ring` offset ring.

**`search-pill`** — Standard 44px search bar.
- Background `{colors.surface}`, text `{colors.steel}`, typography `{typography.body-md}`, rounded `{rounded.md}`, height 44px, border `1px solid {colors.hairline-strong}`.

**`search-pill-large`** — Large 56px search bar (top of MongoDB University catalog).
- Background `{colors.canvas}`, text `{colors.steel}`, typography `{typography.body-md}`, rounded `{rounded.md}`, height 56px, border `1px solid {colors.hairline-strong}`.

### Tabs

**`pill-tab`** + **`pill-tab-active`** — Pill-style tab nav (top of pricing: "MongoDB Atlas / Enterprise Advanced").
- Inactive: text `{colors.steel}`, border `1px solid {colors.hairline}`, padding `{spacing.xs} {spacing.md}`, rounded `{rounded.full}`.
- Active: background `{colors.ink}`, text `{colors.on-dark}`.

**`segmented-tab`** + **`segmented-tab-active`** — Underline-style tab navigation.
- Inactive: text `{colors.steel}`, no border. Active: text `{colors.brand-green-dark}`, 2px bottom border in `{colors.brand-green-dark}`.

### Badges & Status

**`badge-green`** — Bright green badge for new product highlights.
- Background `{colors.brand-green}`, text `{colors.on-primary}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 8px`.

**`badge-green-soft`** — Pale-mint pill for success/free indicators.
- Background `{colors.brand-green-soft}`, text `{colors.brand-green-dark}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-purple`** — Purple course category tag.
- Background `{colors.accent-purple}`, text `{colors.on-dark}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 8px`.

**`badge-orange`** — Orange course category tag.
- Background `{colors.accent-orange}`, text `{colors.on-dark}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 8px`.
- This pair is a real AA failure: white on `{colors.accent-orange}` measures 2.86:1 at 13px, against 4.5:1. Both values are extracted and left as observed. `{colors.on-primary}` ink on the same orange measures 6.03:1 and is the fix if the brand will take it.

**`badge-popular`** — "Most Popular" tier indicator (dark teal pill with green text).
- Background `{colors.brand-teal-deep}`, text `{colors.brand-green}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`promo-banner`** — Dark teal sticky promo strip ABOVE the top nav.
- Background `{colors.brand-teal-deep}`, text `{colors.on-dark}`, typography `{typography.body-sm-medium}`, padding `{spacing.sm} {spacing.md}`.

### Code

**`code-block`** — Code container.
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, typography `{typography.code-md}`, rounded `{rounded.md}`, padding `{spacing.md}`.

**`code-mockup-card`** — Embedded code mockup on hero band.
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding `{spacing.lg}`. Carries terminal-aesthetic code snippet.

### Tables

**`comparison-table`** — Pricing feature comparison table.
- Background `{colors.canvas}`, text `{colors.ink}`, typography `{typography.body-sm}`, rounded `{rounded.md}`, border `1px solid {colors.hairline}`.

**`comparison-row`** — Individual feature row.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.lg}`, bottom border `1px solid {colors.hairline-soft}`.

### Documentation Components

**`service-tile`** — Tile in "Customize your deployment" 6-up grid.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`why-card`** — "Loved by builders" feature card.
- Background `{colors.surface}`, rounded `{rounded.lg}`, padding `{spacing.xl}`.

**`customer-testimonial-card`** — Customer quote card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`logo-wall-item`** — Customer logo wordmark cell.
- Background transparent, text `{colors.steel}`, typography `{typography.body-md-medium}`, padding `{spacing.lg}`.

**`faq-accordion-item`** — FAQ panel.
- Background `{colors.canvas}`, rounded `{rounded.md}`, padding `{spacing.xl}`, bottom border `1px solid {colors.hairline}`.

### Navigation

**Top Navigation (Marketing)** — Sticky white bar.
- Background `{colors.canvas}`, height ~64px, bottom border `1px solid {colors.hairline}`.
- Left: MongoDB leaf logo + "Solutions / Resources / Company / Pricing" links.
- Right: "Sign In" link + bright-green pill "Try Free" CTA.

### Signature Components

**`hero-band-dark`** — Deep teal hero band with embedded code mockup.
- Background `{colors.brand-teal-deep}`, text `{colors.on-dark}`, padding `{spacing.hero}`.
- Layout: centered headline `{typography.hero-display}`, subtitle, button row, `code-mockup-card` below.

**`hero-platform-card`** — Lighter-teal platform showcase card on dark hero.
- Background `{colors.brand-teal-mid}`, text `{colors.on-dark}`, rounded `{rounded.xl}`, padding `{spacing.xxl}`.

**`cta-banner-dark`** — Dark CTA banner at the bottom of feature pages.
- Background `{colors.brand-teal-deep}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding `{spacing.section}`.

**`footer-region`** — Dark teal multi-column footer.
- Background `{colors.brand-teal-deep}`, padding `{spacing.section} {spacing.xxl}`.
- 6-column link grid.
- Section headings in `{typography.body-sm-medium}` `{colors.on-dark}`.

**`footer-link`** — Individual footer link.
- Fill is transparent; the declared ground is `{colors.brand-teal-deep}`, the footer region it lives in. Text `{colors.on-dark-muted}` (8.06:1 there), typography `{typography.body-sm}`, padding `{spacing.xxs} 0`.

## Motion & Animation

This motion system is **prescribed to match the brand's visual identity and was not measured from the live site** — no timing function or duration below is an extracted fact. MongoDB is a developer-tool identity (terminal-aesthetic code mockups, a database product, documentation surfaces), so it takes the **Crisp** profile: state change reads as instant, and there is no entrance choreography competing with a code snippet.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, link) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` | Colour/opacity change applies at `{motion.duration-reduced}`; no lift |
| Press (pill button) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Instant colour change, no scale |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears instantly, never animated away |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` | Opacity-only crossfade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px) to 0` | Fade only at `{motion.duration-reduced}`, no travel |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Fade only at `{motion.duration-reduced}` |
| Dropdown / nav menu | `{motion.duration-fast}` enter, `{motion.duration-instant}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px) to 0` | Fade only at `{motion.duration-reduced}` |
| Toast | `{motion.duration-base}` enter, `{motion.duration-fast}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px) to 0` | Fade only at `{motion.duration-reduced}` |
| List enter (course grid, pricing tiers) | `{motion.duration-base}`, `{motion.stagger-step}` per item | `{motion.ease-enter}` | `opacity`, `transform: translateY(6px) to 0` | All items fade together at `{motion.duration-reduced}`, stagger dropped |
| List exit (filtered-out tiles) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | Immediate removal after a `{motion.duration-reduced}` fade |
| Loading (spinner, skeleton) | 900ms linear loop | linear | `transform: rotate` / `opacity` | Loop frozen; a static indicator and its text label remain |

**Rules this file follows**
- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin` — a code mockup card reflowing is worse than no transition at all.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content: the dark hero band and its code mockup render in place.
- The only infinite animation is the loader. The hero band's atmospheric gradient is static; there is no brand ambience loop.
- Press is an opacity deepen, not a scale pop — the pill is a brand signature and must not squash.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale travel, the list stagger, the loader loop. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (100ms);
     focus rings, which appear instantly and are never suppressed. */
}
```

## Accessibility

Measured with WCAG 2.1 relative luminance from this file's own token values.

### Key pairs — passing

| Foreground / Background | Ratio | Required |
|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 17.2:1 | 4.5:1 |
| `{colors.ink}` on `{colors.surface}` | 16.56:1 | 4.5:1 |
| `{colors.on-dark}` on `{colors.brand-teal-deep}` | 17.2:1 | 4.5:1 |
| `{colors.on-dark-muted}` on `{colors.brand-teal-deep}` | 8.06:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.brand-green}` | 10.89:1 | 4.5:1 |
| `{colors.slate}` on `{colors.canvas}` | 8.51:1 | 4.5:1 |
| `{colors.steel}` on `{colors.canvas}` | 5.41:1 | 4.5:1 |
| `{colors.brand-green-dark}` on `{colors.canvas}` | 6.82:1 | 4.5:1 |
| `{colors.semantic-warning-text}` on `{colors.semantic-warning-bg}` | 4.29:1 | 4.5:1 — marginal, see below |

### Key pairs — measured failures, stated plainly

These are extracted brand values. They are recorded, not corrected.

| Foreground / Background | Ratio | Required | Status |
|---|---|---|---|
| `{colors.hairline-soft}` on `{colors.surface}` | 1.11:1 | 3.0:1 | FAIL — decorative divider only |
| `{colors.hairline-soft}` on `{colors.canvas}` | 1.15:1 | 3.0:1 | FAIL — decorative divider only |
| `{colors.hairline}` on `{colors.surface}` | 1.22:1 | 3.0:1 | FAIL — decorative divider only |
| `{colors.hairline}` on `{colors.canvas}` | 1.27:1 | 3.0:1 | FAIL — card boundary is decorative; cards do not depend on it to be found |
| `{colors.hairline-strong}` on `{colors.surface}` | 1.57:1 | 3.0:1 | FAIL |
| `{colors.hairline-strong}` on `{colors.canvas}` | 1.63:1 | 3.0:1 | FAIL — and this one is the *only* boundary of `text-input`, so it is a real defect. Use `{colors.hairline-control}` (4.41:1) instead. |
| `{colors.muted}` on `{colors.surface}` | 2.05:1 | 4.5:1 | FAIL — placeholder and disabled only; never body copy |
| `{colors.muted}` on `{colors.canvas}` | 2.13:1 | 4.5:1 | FAIL — same scope. On the dark footer the same hex reaches 8.06:1 |
| `{colors.stone}` on `{colors.canvas}` | 3.46:1 | 4.5:1 | FAIL below 18px; usable for 18px+ labels at the 3:1 threshold |
| `button-primary-pressed` ink on `{colors.primary-pressed}` | 3.93:1 | 4.5:1 | FAIL — pressed state only, transient |
| `badge-orange` white on `{colors.accent-orange}` | 2.86:1 | 4.5:1 | FAIL — the worst pair in the file; course category tags are not AA |

`{colors.semantic-warning-bg}` is a fill, never an ink; it is never drawn as text on the canvas.

### Focus ring visibility, per surface this file defines

| Surface | Ring | Ratio | Required |
|---|---|---|---|
| `{colors.canvas}` | `{colors.focus}` | 6.82:1 | 3.0:1 |
| `{colors.surface}` | `{colors.focus}` | 6.56:1 | 3.0:1 |
| `{colors.surface-soft}` | `{colors.focus}` | 6.33:1 | 3.0:1 |
| `{colors.surface-feature}` | `{colors.focus}` | 6.31:1 | 3.0:1 |
| `{colors.brand-teal-deep}` / `{colors.canvas-dark}` | `{colors.focus-on-dark}` | 10.89:1 | 3.0:1 |
| `{colors.brand-teal}` | `{colors.focus-on-dark}` | 7.47:1 | 3.0:1 |
| `{colors.brand-teal-mid}` | `{colors.focus-on-dark}` | 4.32:1 | 3.0:1 |

The ring is drawn outside its control with a **2px offset**, so each ratio above is measured against the surface behind the ring — not against the control fill it surrounds. That is what WCAG 2.2 Focus Appearance asks for, and it is why no single ring value has to clear 3:1 against the bright green pill as well as the white page.

### Tap targets
Documented heights: pill buttons 40–44px, form inputs 44px, large search 56px, pill tabs ~32px rising to 44px on mobile. The 32px desktop pill tab is below the 44px AA target; rendered size cannot be verified from this document, so the 44px floor is a requirement here, not a measurement.

### Reduced motion
`prefers-reduced-motion: reduce` removes all translate, scale and stagger, freezes the loader loop, and caps remaining opacity fades at `{motion.duration-reduced}` (100ms). Focus rings are never animated and never suppressed.

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
| `{colors.hairline-dark}` (`#1c2d38`) on `{colors.canvas-dark}` (`#001e2b`) | 1.21:1 | 3.0:1 | Fail — boundary, dark theme |
| `{colors.semantic-warning-text}` (`#946f3f`) on `{colors.surface}` (`#f9fbfa`) | 4.39:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Use `{colors.brand-green}` (bright MongoDB green) for primary CTAs everywhere
- Pair dark-teal hero bands with bright green CTA pills
- Apply `{rounded.full}` to every button, every status badge
- Apply `{rounded.lg}` (12px) to cards consistently
- Use category accent colors (purple, orange, green, teal) ONLY for course tags
- Maintain Euclid Circular A across every UI surface
- Use code mockup cards with terminal-aesthetic content for product showcases

### Don't
- Don't use the bright green for body text or large surfaces
- Don't introduce additional accent colors beyond the brand green and category-encoding palette
- Don't soften corners on buttons; the pill is a brand signature
- Don't replace deep teal hero bands with white hero bands
- Don't apply heavy shadows on flat documentation cards; reserve elevation for code mockups
- Don't use Source Code Pro for prose

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile (small) | < 480px | Single column. Hero 36px. Pricing 1-up. Course catalog 1-up. |
| Mobile (large) | 480 – 767px | Course tiles 2-up. Hero 48px. |
| Tablet | 768 – 1023px | 2-column feature grids. Hero 56px. |
| Desktop | 1024 – 1279px | 3-tier pricing card row. 3-up course catalog. Hero 64px. |
| Wide Desktop | ≥ 1280px | Full 72px hero presentation. |

### Touch Targets
- Pill buttons render at 40–44px effective height
- Form inputs render at 44px height
- Search pill (large) renders at 56px
- Pill tabs ~32px → 44px on mobile

### Collapsing Strategy
- **Promo banner** stays full-width; truncates at < 480px
- **Top nav** below 1024px collapses to hamburger
- **Hero band**: code mockup card moves below text on mobile
- **Pricing tiers**: 3-column → 2-column tablet → 1-column mobile
- **Course catalog**: 3-up → 2-up tablet → 1-up mobile
- **Hero typography**: 72px → 56px → 48px → 36px
- **Footer**: 6-column desktop → 3-column tablet → accordion mobile

### Image Behavior
- Atmospheric AI imagery uses 16:9 ratio with full-bleed scaling
- Code mockup card content remains readable across breakpoints
- Customer logo wall: wordmarks at consistent 60–80px height

## Iteration Guide

1. Focus on ONE component at a time
2. Reference component names and tokens directly
3. Run `npx @google/design.md lint DESIGN.md` after edits
4. Add new variants as separate `components:` entries
5. Default to `{typography.body-md}` for body
6. Keep `{colors.brand-green}` as the primary CTA across all surfaces
7. Pill-shaped buttons (`{rounded.full}`) always
8. Dark-teal hero bands frame primary CTAs

## Known Gaps

- Specific dark-mode token values for canvas/surface beyond hero bands not surfaced
- Animation/transition timings not extracted. The Motion & Animation section is prescribed from the Crisp profile, not measured from the live site
- Focus ring colour and offset are prescribed; MongoDB's real `:focus-visible` treatment was not captured
- `{colors.hairline-control}` is prescribed, not observed — the real site's control borders fail 3:1
- Form validation success state not explicitly captured
- Course-tile category color mappings are observation-based
