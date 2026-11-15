---
version: alpha
name: Miro-design-analysis
description: Miro presents itself as the AI-powered visual workspace through a confident, almost playful brand voice — anchored by its signature canary yellow ({colors.brand-yellow}) wordmark over white canvas, broken open by colorful pastel feature tints (rose, teal, coral, orange, mint) that echo the actual sticky-note color palette used on the live whiteboard. Black-pill primary buttons dominate marketing, real Miro-board mockups serve as feature illustrations, and a 4-tier pricing grid leads into a dense comparison table. Roobert PRO carries display headlines; the system supports homepage, pricing, AI Workflows product page, agile vertical, and customer stories surfaces.

colors:
  primary: "#1c1c1e"
  on-primary: "#ffffff"
  brand-yellow: "#ffd02f"
  brand-yellow-deep: "#fcb900"
  yellow-light: "#fff4c4"
  yellow-dark: "#746019"
  brand-blue: "#4262ff"
  blue-450: "#5b76fe"
  blue-pressed: "#2a41b6"
  brand-coral: "#ff9999"
  coral-light: "#ffc6c6"
  coral-dark: "#600000"
  brand-rose: "#ffd8f4"
  rose-light: "#fde0f0"
  brand-pink: "#fde0f0"
  brand-teal: "#0fbcb0"
  teal-light: "#c3faf5"
  moss-dark: "#187574"
  brand-orange-light: "#ffe6cd"
  brand-red: "#fbd4d4"
  brand-red-dark: "#e3c5c5"
  success-accent: "#00b473"
  canvas: "#ffffff"
  surface: "#f7f8fa"
  surface-soft: "#fafbfc"
  surface-yellow: "#fff8e0"
  surface-pricing-featured: "#f5f3ff"
  hairline: "#e0e2e8"
  hairline-soft: "#eef0f3"
  hairline-strong: "#c7cad5"
  hairline-control: "#8a8d9c"
  focus: "#4262ff"
  ink-deep: "#050038"
  ink: "#1c1c1e"
  charcoal: "#2c2c34"
  slate: "#555a6a"
  steel: "#6b6f7e"
  stone: "#8e91a0"
  muted: "#a5a8b5"
  on-dark: "#ffffff"
  on-dark-muted: "#a5a8b5"
  footer-bg: "#1c1c1e"

typography:
  hero-display:
    fontFamily: Roobert PRO
    fontSize: 80px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -2px
  display-lg:
    fontFamily: Roobert PRO
    fontSize: 60px
    fontWeight: 500
    lineHeight: 1.10
    letterSpacing: -1.5px
  heading-1:
    fontFamily: Roobert PRO
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -1px
  heading-2:
    fontFamily: Roobert PRO
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.5px
  heading-3:
    fontFamily: Roobert PRO
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
  heading-4:
    fontFamily: Roobert PRO
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.30
  heading-5:
    fontFamily: Roobert PRO
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.40
  subtitle:
    fontFamily: Roobert PRO
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
  body-md:
    fontFamily: Roobert PRO
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
  body-md-medium:
    fontFamily: Roobert PRO
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
  body-sm:
    fontFamily: Roobert PRO
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
  body-sm-medium:
    fontFamily: Roobert PRO
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
  caption:
    fontFamily: Roobert PRO
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.40
  caption-bold:
    fontFamily: Roobert PRO
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.40
  micro:
    fontFamily: Roobert PRO
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
  micro-uppercase:
    fontFamily: Roobert PRO
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0.5px
  button-md:
    fontFamily: Roobert PRO
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30
  stat-display:
    fontFamily: Roobert PRO
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.10
    letterSpacing: -1.5px

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 20px
  xxxl: 28px
  feature: 32px
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
  button-primary-pressed:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
  button-yellow:
    backgroundColor: "{colors.brand-yellow}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
  button-blue:
    backgroundColor: "{colors.brand-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    border: "1px solid {colors.hairline-strong}"
  button-on-dark:
    backgroundColor: "{colors.on-dark}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "8px 12px"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.brand-blue}"
    typography: "{typography.body-sm-medium}"
    padding: "0"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 36px
    border: "1px solid {colors.hairline}"
  card-base:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  card-feature:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline-soft}"
  card-feature-yellow:
    backgroundColor: "{colors.brand-yellow}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.xxl}"
  card-feature-coral:
    backgroundColor: "{colors.coral-light}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.xxl}"
  card-feature-teal:
    backgroundColor: "{colors.teal-light}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.xxl}"
  card-feature-rose:
    backgroundColor: "{colors.rose-light}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.xxl}"
  card-customer-story:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xxxl}"
    padding: "0"
    border: "1px solid {colors.hairline-soft}"
  card-stat:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.stat-display}"
    padding: "{spacing.lg}"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  pricing-card-featured:
    backgroundColor: "{colors.surface-pricing-featured}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
    border: "2px solid {colors.brand-blue}"
  pricing-card-enterprise:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
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
    border: "2px solid {colors.brand-blue}"
  search-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xs} {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-medium}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    border: "1px solid {colors.hairline-strong}"
  pill-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm-medium}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    border: "1px solid {colors.hairline}"
  pill-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  toggle-monthly-yearly:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "4px"
  badge-promo:
    backgroundColor: "{colors.brand-yellow}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-tag-yellow:
    backgroundColor: "{colors.surface-yellow}"
    textColor: "{colors.yellow-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-tag-purple:
    backgroundColor: "{colors.surface-pricing-featured}"
    textColor: "{colors.brand-blue}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-tag-coral:
    backgroundColor: "{colors.coral-light}"
    textColor: "{colors.coral-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-success:
    backgroundColor: "{colors.success-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-discount:
    backgroundColor: "{colors.brand-yellow}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm-medium}"
    padding: "{spacing.sm} {spacing.md}"
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
  template-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline}"
  whiteboard-mockup:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "0"
    border: "1px solid {colors.hairline-soft}"
    shadow: "rgba(5, 0, 56, 0.08) 0px 12px 32px -4px"
  faq-accordion-item:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "0 0 1px {colors.hairline} solid"
  logo-wall-item:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-md-medium}"
    padding: "{spacing.lg}"
  hero-band-marketing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.hero-display}"
    rounded: "0"
    padding: "{spacing.hero}"
  cta-banner-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.feature}"
    padding: "{spacing.section}"
  industry-tile:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  capterra-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  footer-region:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-link:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxs} 0"
  app-store-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
---

## Overview

Miro positions itself as the AI-powered visual workspace through a confident, slightly playful brand voice. The homepage opens with a stark white canvas anchored by a small canary-yellow Miro wordmark in the top-left, a black-pill primary CTA "Get started free" and a secondary "Book a demo" outline pill — then dramatic real-Miro-board mockup imagery (sticky notes, kanban, mind maps) carries the visual weight. Across deeper surfaces, the system breaks open: pastel feature cards (rose, teal, coral, yellow) echo the actual sticky-note color palette of the live whiteboard product, and customer story cards reuse those tints to differentiate brand vignettes.

Roobert PRO — Miro's custom display face — anchors every typographic surface, from the 80px hero display down to 11px micro labels. The face's slightly rounded, geometric character pairs naturally with the playful product photography and the friendly product positioning. Black-pill primary buttons (`{rounded.full}`) dominate marketing CTAs; the brand color, signature canary yellow ({colors.brand-yellow}), is reserved for the wordmark, top promo banners, and "yellow tag" feature pills — never as a primary CTA. The 4-tier pricing comparison (Free / Starter / Business / Enterprise) leads into the densest surface in the system: a feature comparison table that runs ~80 rows deep across multiple section dividers.

**Key Characteristics:**
- Stark white canvas + Miro wordmark in canary yellow ({colors.brand-yellow}) as the recognizable opening signature
- Black-pill primary CTAs ({colors.primary} + `{rounded.full}`) as the dominant interactive element
- Pastel feature cards (yellow, rose, coral, teal, mint) that echo the actual sticky-note palette
- Roobert PRO across every UI surface; geometric, slightly rounded character
- Real Miro-board mockup imagery used as feature illustrations
- 4-tier pricing card grid + dense feature comparison table
- Massive dark footer ({colors.footer-bg}) with multi-column links + app-store badges

## Colors

> Source pages: miro.com/ (homepage), /pricing/ (4-tier comparison), /products/ai-workflows/ (AI product), /agile/ (vertical landing), /customers/ (story directory). Token coverage was identical across all five pages.

### Brand & Accent
- **Miro Yellow** ({colors.brand-yellow}): The brand's recognizable canary yellow — wordmark color, top promo banner, "yellow tag" pills
- **Yellow Deep** ({colors.brand-yellow-deep}): Darker variant for hover states and emphasis
- **Yellow Light** ({colors.yellow-light}): Pale yellow background tint for tag chips
- **Yellow Dark** ({colors.yellow-dark}): Yellow-tag text color (dark olive) for chip foreground
- **Brand Blue** ({colors.brand-blue}): Action blue for inline links and featured-pricing-tier border
- **Blue Pressed** ({colors.blue-pressed}): Pressed-state blue
- **Brand Coral** ({colors.brand-coral}): Coral accent for warm callouts
- **Coral Light** ({colors.coral-light}): Pale coral for feature card backgrounds
- **Coral Dark** ({colors.coral-dark}): Coral-tag text color (deep wine)
- **Brand Rose** ({colors.brand-rose}): Soft rose-pink for feature card variants
- **Brand Teal** ({colors.brand-teal}): Brand teal
- **Teal Light** ({colors.teal-light}): Pale teal for feature card backgrounds
- **Moss Dark** ({colors.moss-dark}): Deep teal-green text color
- **Brand Pink** ({colors.brand-pink}): Pale pink for soft callouts
- **Brand Orange Light** ({colors.brand-orange-light}): Soft orange for feature card backgrounds

### Surface
- **Canvas White** ({colors.canvas}): Page background and primary card surface
- **Surface** ({colors.surface}): Subtle section backgrounds, search-pill rest
- **Surface Soft** ({colors.surface-soft}): Quieter section divisions
- **Surface Yellow** ({colors.surface-yellow}): Pale yellow-tinted surface for tag chip
- **Surface Pricing Featured** ({colors.surface-pricing-featured}): Pale lavender for featured pricing tier
- **Hairline** ({colors.hairline}): 1px borders and primary dividers
- **Hairline Soft** ({colors.hairline-soft}): Quieter table-row dividers
- **Hairline Strong** ({colors.hairline-strong}): Stronger 1px border for inputs
- **Hairline Control** ({colors.hairline-control}): **Prescribed, not extracted.** A parallel accessible boundary for controls whose border is their only edge — text inputs, filter dropdowns, the search pill. Measures 3.3:1 on {colors.canvas} and 3.1:1 on {colors.surface}, clearing the 3:1 non-text minimum that all three extracted hairlines miss. The extracted hairlines stay as documented and are scoped to decoration: table-row rules, card edges, and footer dividers, where no boundary carries meaning.

### Focus
- **Focus** ({colors.focus}): The focus ring is Miro's own action blue, the same value the file already documents as the focused-input border. A single mid-luminance ring serves every surface in this system rather than a light/dark pair: it measures 4.75:1 on {colors.canvas}, 4.47:1 on {colors.surface}, 3.58:1 on the dark {colors.primary} CTA banner and footer, and 3.2:1 or better on every pastel feature card. Drawn as a 2px ring with a 2px offset, so it is judged against the surface behind the control, not the control's own fill.

### Text
- **Ink Deep** ({colors.ink-deep}): Headlines on lighter feature cards
- **Ink** ({colors.ink}): Primary headlines and body text
- **Charcoal** ({colors.charcoal}): Body emphasis text
- **Slate** ({colors.slate}): Secondary text, metadata
- **Steel** ({colors.steel}): Tertiary text, footer links
- **Stone** ({colors.stone}): Captions, muted labels
- **Muted** ({colors.muted}): Disabled labels, input placeholders
- **On Dark** ({colors.on-dark}): White text on dark surfaces
- **On Dark Muted** ({colors.on-dark-muted}): Reduced-opacity white on dark

### Semantic
- **Success Accent** ({colors.success-accent}): Confirmation/success indicator green
- **Brand Red** ({colors.brand-red}): Soft red for error backgrounds
- **Brand Red Dark** ({colors.brand-red-dark}): Stronger red for error borders

## Typography

### Font Family
**Roobert PRO** (primary): Miro's custom geometric sans-serif typeface. Used across every UI surface from oversized 80px hero displays to 11px micro labels. The face has a slightly rounded, friendly character that matches the brand's playful product positioning. Fallbacks: Noto Sans, -apple-system, BlinkMacSystemFont, sans-serif.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 80px | 500 | 1.05 | -2px | Marketing hero ("See how teams get great done with Miro") |
| `{typography.display-lg}` | 60px | 500 | 1.10 | -1.5px | Major section openers |
| `{typography.heading-1}` | 48px | 500 | 1.15 | -1px | Page-level headlines |
| `{typography.heading-2}` | 36px | 500 | 1.20 | -0.5px | Subsection headlines |
| `{typography.heading-3}` | 28px | 500 | 1.25 | 0 | Card titles |
| `{typography.heading-4}` | 22px | 500 | 1.30 | 0 | Feature tile titles |
| `{typography.heading-5}` | 18px | 500 | 1.40 | 0 | FAQ questions, smaller cards |
| `{typography.subtitle}` | 18px | 400 | 1.50 | 0 | Hero subtitle |
| `{typography.body-md}` | 16px | 400 | 1.50 | 0 | Primary body text |
| `{typography.body-md-medium}` | 16px | 500 | 1.50 | 0 | Logo wall labels |
| `{typography.body-sm}` | 14px | 400 | 1.50 | 0 | Secondary body, table cells |
| `{typography.body-sm-medium}` | 14px | 500 | 1.50 | 0 | Filter dropdowns, button labels |
| `{typography.caption}` | 13px | 400 | 1.40 | 0 | Helper text |
| `{typography.caption-bold}` | 13px | 600 | 1.40 | 0 | Badge labels, tag chips |
| `{typography.micro}` | 12px | 500 | 1.40 | 0 | Footer microcopy |
| `{typography.micro-uppercase}` | 11px | 600 | 1.40 | 0.5px | Section dividers in tables |
| `{typography.button-md}` | 14px | 500 | 1.30 | 0 | Pill button labels |
| `{typography.stat-display}` | 64px | 500 | 1.10 | -1.5px | "100M+ users" stat callouts |

### Principles
- **Tight hero leading** (1.05) creates magazine-grade display headlines on the 80px hero
- **Negative letter-spacing progression** — display sizes use -2px to -1.5px; smaller headings relax to 0
- **Stat-display token** (64px / 500) for marketing stat callouts
- **Single weight scale** — 400 (body), 500 (medium emphasis + headings), 600 (badges and uppercase). Roobert PRO does not use 700 in this system.

## Layout

### Spacing System
- **Base unit**: 4px (8px primary increment)
- **Tokens**: `{spacing.xxs}` (4px) · `{spacing.xs}` (8px) · `{spacing.sm}` (12px) · `{spacing.md}` (16px) · `{spacing.lg}` (20px) · `{spacing.xl}` (24px) · `{spacing.xxl}` (32px) · `{spacing.xxxl}` (40px) · `{spacing.section-sm}` (48px) · `{spacing.section}` (64px) · `{spacing.section-lg}` (96px) · `{spacing.hero}` (120px)
- **Section rhythm**: Marketing pages use `{spacing.section-lg}` (96px); pricing comparison tightens to `{spacing.section}` (64px); customer story stack uses `{spacing.xxl}` (32px)
- **Card internal padding**: `{spacing.xl}` (24px) for compact cards; `{spacing.xxl}` (32px) for feature panels

### Grid & Container
- Marketing pages use 1280px max-width with 32px gutters
- Pricing page renders 4-tier card row at desktop (Free / Starter / Business / Enterprise)
- Customer stories page uses 2-column grid with filter dropdowns
- AI Workflows page uses 2-column hero, then 3-up feature grid

### Whitespace Philosophy
Marketing surfaces give content generous breathing room — `{spacing.hero}` (120px) hero padding gives the small wordmark room to breathe. Pricing surfaces tighten dramatically.

## Elevation & Depth

The system runs predominantly flat with strategic depth on hero mockups.

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow; `{colors.hairline-soft}` border | Default cards, table rows, form inputs |
| 1 (subtle) | `rgba(5, 0, 56, 0.04) 0px 1px 2px 0px` | Subtle hover-elevated tiles |
| 2 (card) | `rgba(5, 0, 56, 0.06) 0px 4px 12px 0px` | Standard feature cards |
| 3 (mockup) | `rgba(5, 0, 56, 0.08) 0px 12px 32px -4px` | Hero whiteboard mockup framing |
| 4 (modal) | `rgba(5, 0, 56, 0.12) 0px 16px 48px -8px` | Modals, dropdowns |

### Decorative Depth
- The atmospheric depth on Miro's hero comes from the live-product-board mockup illustrations — sticky notes layered at z-offsets, color-block tints behind whiteboard frames
- Pastel feature cards carry their own visual weight via saturated background color
- Customer-story cards layer dark photographic content with overlay scrims

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Small chips, micro-controls |
| `{rounded.sm}` | 6px | Discount badges |
| `{rounded.md}` | 8px | Inputs, search-pill |
| `{rounded.lg}` | 12px | Standard cards, table containers |
| `{rounded.xl}` | 16px | Pricing cards, feature panels |
| `{rounded.xxl}` | 20px | Larger feature cards |
| `{rounded.xxxl}` | 28px | Pastel feature cards (yellow, rose, coral, teal) |
| `{rounded.feature}` | 32px | Hero CTA banner cards |
| `{rounded.full}` | 9999px | All buttons, pill tabs, badges |

### Photography Geometry
- Real Miro board mockups render with `{rounded.xl}` (16px) corners and a subtle drop shadow
- Customer story cards use `{rounded.xxxl}` (28px) corners with full-bleed photography
- Template card thumbnails use `{rounded.xl}` (16px) with photographic content
- Customer logos wall presents wordmarks inline at consistent 100px height

### Focus Ring Geometry
- Ring: 2px solid {colors.focus}, 2px offset outside the control, so the ring sits on the surface behind the control rather than on its fill
- Ring corner radius follows the control's own radius token — `{rounded.full}` on pills and badges, `{rounded.md}` on inputs, `{rounded.xl}` on cards — so the ring never sits outside the radius ladder
- The one exception is `text-input-focused`, which keeps its extracted inset `2px solid {colors.brand-blue}` border and carries the offset ring in addition, not instead

## Components

> Only `default`, `active`/`pressed` and `disabled` were extracted from the live pages. The `hover`, `focus-visible`, `loading`, `selected` and `error` columns below are **prescribed** — derived from the tokens this file already carries, not measured. An earlier revision of this file claimed a "no-hover policy" and documented no hover state at all; there is no such policy in this collection, and the claim is removed.

### State Coverage

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | {colors.primary} | lifts to {colors.charcoal} | 2px {colors.focus} ring, 2px offset | `button-primary-pressed` | `button-primary-disabled` | label swaps for an inline spinner, width held | n/a | n/a |
| `button-yellow` | {colors.brand-yellow} | deepens to {colors.brand-yellow-deep} | 2px {colors.focus} ring, 2px offset | 96% scale pop | {colors.hairline} bg, {colors.muted} ink | inline spinner in {colors.primary} | n/a | n/a |
| `button-blue` | {colors.brand-blue} | deepens to {colors.blue-450} | 2px {colors.focus} ring, 2px offset | {colors.blue-pressed} | {colors.hairline} bg, {colors.muted} ink | inline spinner in {colors.on-primary} | n/a | n/a |
| `button-secondary` | 1px {colors.hairline-strong} | border to {colors.hairline-control} | 2px {colors.focus} ring, 2px offset | {colors.surface} fill | {colors.muted} ink and border | inline spinner in {colors.ink} | n/a | n/a |
| `button-on-dark` | {colors.on-dark} | drops to {colors.surface} | 2px {colors.focus} ring, 2px offset — 3.58:1 on {colors.primary} | 96% scale pop | 40% opacity | inline spinner in {colors.primary} | n/a | n/a |
| `button-ghost` | transparent | {colors.surface} fill | 2px {colors.focus} ring, 2px offset | {colors.hairline-soft} fill | {colors.muted} ink | n/a | n/a | n/a |
| `button-link` | {colors.brand-blue} | underline appears | 2px {colors.focus} ring, 2px offset | {colors.blue-pressed} | {colors.muted} ink | n/a | n/a | n/a |
| `button-icon-circular` | 1px {colors.hairline} | border to {colors.hairline-control} | 2px {colors.focus} ring, 2px offset | 94% scale pop | {colors.muted} glyph | n/a | n/a | n/a |
| `text-input` | 1px {colors.hairline-strong} | border to {colors.hairline-control} | `text-input-focused` plus 2px {colors.focus} ring | n/a — inputs have no pressed state | {colors.surface} fill, {colors.muted} ink | n/a | n/a | 1px {colors.brand-red-dark} border on a {colors.brand-red} fill, message in {colors.coral-dark} |
| `search-pill` | {colors.surface} | {colors.canvas} fill | 2px {colors.focus} ring, 2px offset | n/a | {colors.muted} placeholder | results area shows a skeleton block at {colors.hairline-soft} | n/a | n/a |
| `filter-dropdown` | 1px {colors.hairline-strong} | border to {colors.hairline-control} | 2px {colors.focus} ring, 2px offset | {colors.surface} fill | {colors.muted} ink | n/a | {colors.primary} fill, {colors.on-primary} label, count chip appended | n/a |
| `pill-tab` | `pill-tab` | border to {colors.hairline-control} | 2px {colors.focus} ring, 2px offset | 96% scale pop | {colors.muted} ink | n/a | `pill-tab-active` | n/a |
| `toggle-monthly-yearly` | {colors.surface} track | thumb lightens to {colors.canvas} | 2px {colors.focus} ring on the track | thumb travels | 40% opacity | n/a | active half carries {colors.canvas} thumb | n/a |
| `faq-accordion-item` | collapsed | {colors.surface} fill on the header row | 2px {colors.focus} ring, 2px offset | 98% scale pop on the header | n/a | n/a | expanded, chevron rotated 180° | n/a |
| `card-customer-story` | 1px {colors.hairline-soft} | elevates to level 2, image scales 1.02 | 2px {colors.focus} ring, 2px offset | 99% scale | n/a | skeleton block at {colors.hairline-soft} | n/a | n/a |
| `template-card` | 1px {colors.hairline} | elevates to level 1 | 2px {colors.focus} ring, 2px offset | 98% scale pop | n/a | skeleton block at {colors.hairline-soft} | outline switches to 2px {colors.brand-blue} | n/a |
| `pricing-card` | 1px {colors.hairline} | elevates to level 2 | 2px {colors.focus} ring, 2px offset | n/a | n/a | n/a | `pricing-card-featured` | n/a |
| `badge-promo`, `badge-tag-*`, `badge-discount`, `badge-success` | default only | n/a | n/a | n/a | n/a | n/a | n/a | n/a — these are non-interactive labels with a single state |
| `logo-wall-item`, `capterra-badge`, `card-stat`, `comparison-row` | default only | n/a | n/a | n/a | n/a | n/a | n/a | n/a — static presentation, genuinely one state |

### Buttons

**`button-primary`** — Black pill primary CTA, the dominant action ("Get started free").
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.button-md}`, padding `12px 24px`, rounded `{rounded.full}`.
- Pressed state `button-primary-pressed` lifts to `{colors.charcoal}`.
- Disabled state `button-primary-disabled` uses `{colors.hairline}` background and `{colors.muted}` text.

**`button-yellow`** — Brand-yellow pill for moments of brand emphasis.
- Background `{colors.brand-yellow}`, text `{colors.primary}`, typography `{typography.button-md}`, padding `12px 24px`, rounded `{rounded.full}`.

**`button-blue`** — Brand-blue pill for inline action callouts.
- Background `{colors.brand-blue}`, text `{colors.on-primary}`, typography `{typography.button-md}`, padding `12px 24px`, rounded `{rounded.full}`.

**`button-secondary`** — Outlined pill for secondary actions ("Book a demo").
- Background transparent, text `{colors.ink}`, border `1px solid {colors.hairline-strong}`, typography `{typography.button-md}`, padding `12px 24px`, rounded `{rounded.full}`.

**`button-on-dark`** — White pill for dark CTA banners.
- Background `{colors.on-dark}`, text `{colors.primary}`, typography `{typography.button-md}`, padding `12px 24px`, rounded `{rounded.full}`.

**`button-ghost`** — Quieter rectangular ghost button.
- Background transparent, text `{colors.ink}`, typography `{typography.button-md}`, padding `8px 12px`, rounded `{rounded.md}`.

**`button-link`** — Inline text link.
- Background transparent, text `{colors.brand-blue}`, typography `{typography.body-sm-medium}`, padding `0`.

**`button-icon-circular`** — 36×36px circular utility button.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline}`, rounded `{rounded.full}`.

### Cards & Containers

**`card-base`** — Standard content card.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xl}`, border `1px solid {colors.hairline-soft}`.

**`card-feature`** — White feature card with larger 28px corners.
- Background `{colors.canvas}`, rounded `{rounded.xxxl}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline-soft}`.

**`card-feature-yellow`** — Pastel-yellow feature card.
- Background `{colors.brand-yellow}`, text `{colors.primary}`, rounded `{rounded.xxxl}`, padding `{spacing.xxl}`.

**`card-feature-coral`** — Pastel-coral feature card variant.
- Background `{colors.coral-light}`, text `{colors.primary}`, rounded `{rounded.xxxl}`, padding `{spacing.xxl}`.

**`card-feature-teal`** — Pastel-teal feature card variant.
- Background `{colors.teal-light}`, text `{colors.primary}`, rounded `{rounded.xxxl}`, padding `{spacing.xxl}`.

**`card-feature-rose`** — Pastel-rose feature card variant.
- Background `{colors.rose-light}`, text `{colors.primary}`, rounded `{rounded.xxxl}`, padding `{spacing.xxl}`.

**`card-customer-story`** — Customer story card.
- Background `{colors.canvas}`, rounded `{rounded.xxxl}`, padding `0` (image fills the card), border `1px solid {colors.hairline-soft}`.

**`card-stat`** — Stat-row cell for "100M+ users".
- Background transparent, text `{colors.ink}`, typography `{typography.stat-display}`, padding `{spacing.lg}`.

**`pricing-card`** — Standard pricing tier card.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`pricing-card-featured`** — Featured pricing tier (Business — lavender background + blue border).
- Background `{colors.surface-pricing-featured}`, rounded `{rounded.xl}`, padding `{spacing.xxl}`, border `2px solid {colors.brand-blue}`.

**`pricing-card-enterprise`** — Dark-canvas enterprise tier card.
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.xl}`, padding `{spacing.xxl}`.

### Inputs & Forms

**`text-input`** — Standard text field.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline-strong}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, height 44px.

**`text-input-focused`** — Activated state.
- Border switches to `2px solid {colors.brand-blue}`.

**`search-pill`** — Search bar.
- Background `{colors.surface}`, text `{colors.steel}`, typography `{typography.body-sm}`, rounded `{rounded.md}`, height 40px, border `1px solid {colors.hairline}`.

**`filter-dropdown`** — Pill-shaped filter dropdown ("Company use" / "Industry" / "Use case").
- Background `{colors.canvas}`, text `{colors.ink}`, typography `{typography.body-sm-medium}`, rounded `{rounded.full}`, padding `{spacing.xs} {spacing.md}`, border `1px solid {colors.hairline-strong}`.

### Tabs

**`pill-tab`** + **`pill-tab-active`** — Pill-style tab nav.
- Inactive: background `{colors.canvas}`, text `{colors.steel}`, border `1px solid {colors.hairline}`, padding `{spacing.xs} {spacing.md}`, rounded `{rounded.full}`.
- Active: background `{colors.primary}`, text `{colors.on-primary}`.

**`toggle-monthly-yearly`** — Two-state pill toggle (Monthly / Annual on pricing).
- Background `{colors.surface}`, rounded `{rounded.full}`, padding `4px`.

### Badges & Status

**`badge-promo`** — Yellow promo banner badge.
- Background `{colors.brand-yellow}`, text `{colors.primary}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-tag-yellow`** — Soft-yellow feature tag chip ("Yellow" tag on AI Workflows page).
- Background `{colors.surface-yellow}`, text `{colors.yellow-dark}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-tag-purple`** — Lavender feature tag chip ("AI agent" tag).
- Background `{colors.surface-pricing-featured}`, text `{colors.brand-blue}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-tag-coral`** — Coral feature tag chip variant.
- Background `{colors.coral-light}`, text `{colors.coral-dark}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-success`** — Green success indicator.
- Background `{colors.success-accent}`, text `{colors.on-primary}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-discount`** — Yellow rectangular discount pill ("Save 15%").
- Background `{colors.brand-yellow}`, text `{colors.primary}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 6px`.

**`promo-banner`** — Sticky black promo strip ABOVE the top nav.
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.body-sm-medium}`, padding `{spacing.sm} {spacing.md}`. Carries inline yellow "GET YOUR SPOT" pill.

### Tables

**`comparison-table`** — Pricing feature comparison table.
- Background `{colors.canvas}`, text `{colors.ink}`, typography `{typography.body-sm}`, rounded `{rounded.md}`, border `1px solid {colors.hairline}`.

**`comparison-row`** — Individual feature row.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.lg}`, bottom border `1px solid {colors.hairline-soft}`.

### Documentation Components

**`whiteboard-mockup`** — Real Miro-board UI rendered as feature illustration.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, border `1px solid {colors.hairline-soft}`, shadow `rgba(5, 0, 56, 0.08) 0px 12px 32px -4px`.

**`template-card`** — Template thumbnail card.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.md}`, border `1px solid {colors.hairline}`.

**`industry-tile`** — Industry-vertical tile.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xl}`, border `1px solid {colors.hairline-soft}`.

**`faq-accordion-item`** — FAQ panel item.
- Background `{colors.canvas}`, rounded `{rounded.md}`, padding `{spacing.xl}`, bottom border `1px solid {colors.hairline}`.

**`logo-wall-item`** — Customer logo wordmark cell.
- Background transparent, text `{colors.steel}`, typography `{typography.body-md-medium}`, padding `{spacing.lg}`.

**`capterra-badge`** — Review/rating badge in the footer.
- Background `{colors.canvas}`, text `{colors.ink}`, typography `{typography.caption}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, border `1px solid {colors.hairline}`.

**`app-store-badge`** — App store / Google Play download pill.
- Background `{colors.canvas}`, text `{colors.primary}`, typography `{typography.caption-bold}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`.

### Navigation

**Top Navigation (Marketing)** — Sticky white bar with yellow Miro wordmark + horizontal links + right-side CTAs.
- Background `{colors.canvas}`, height ~64px.
- Left: Yellow square Miro wordmark + horizontal link list (Product, Solutions, Resources).
- Right: "Login / Pricing / Contact sales" links + black-pill "Get started free".

### Signature Components

**`hero-band-marketing`** — Marketing hero band.
- Background `{colors.canvas}`, padding `{spacing.hero}`.
- Layout: centered headline in `{typography.hero-display}`, centered subtitle, centered button row, then whiteboard mockup illustration below.

**`cta-banner-dark`** — Dark CTA banner at the bottom of feature pages.
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.feature}`, padding `{spacing.section}`. Centered headline + subtitle + `button-on-dark` "Get started free".

**`footer-region`** — Massive multi-column dark footer.
- Background `{colors.footer-bg}`, padding `{spacing.section} {spacing.xxl}`.
- 6-column link grid (Product / Solutions / Tools / Resources / Company / Plans & Pricing).
- Section headings in `{typography.body-md-medium}` `{colors.on-dark}`.

**`footer-link`** — Individual link in the footer.
- Background transparent, text `{colors.on-dark-muted}`, typography `{typography.body-sm}`, padding `{spacing.xxs} 0`.

## Motion & Animation

This motion system is **prescribed to match the brand's visual identity and was not measured from the live site** — no timing function, duration or stagger below was extracted from miro.com. It applies the **Playful** profile, which fits this brand on all three of the profile's tests: saturated colour sits on interactive elements (the canary-yellow pill, the blue CTA, the pastel feature cards), the type voice is informal ("See how teams get great done"), and the product itself is a direct-manipulation canvas where a dragged sticky note is expected to settle with a little spring.

### Interaction Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, pills, cards) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, and `transform: scale(1.02)` on cards | Colour change only; scale removed, opacity cross-fade at `{motion.duration-reduced}` |
| Press (pill buttons, tabs, accordion headers) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.96)` | Scale pop removed entirely; the pressed fill applies with no travel |
| Focus (ring appearance) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the 2px `{colors.focus}` ring | Ring appears at full opacity immediately; never delayed or faded |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, plus `transform: translateY(8px)` on the incoming band | Opacity fade only at `{motion.duration-reduced}`; travel removed |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: scale(0.97 → 1)` — the overshoot in `ease-enter` gives the sticky-note settle | Opacity fade at `{motion.duration-reduced}`; no scale, no overshoot |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform: scale(1 → 0.98)` | Opacity fade at `{motion.duration-reduced}`; no scale |
| Dropdown (`filter-dropdown` menu) enter | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(-4px → 0)` | Opacity fade at `{motion.duration-reduced}`; no travel |
| Dropdown exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | Opacity fade at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px → 0)` | Opacity fade at `{motion.duration-reduced}`; no travel |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform: translateY(0 → 6px)` | Opacity fade at `{motion.duration-reduced}`; no travel |
| List enter (pricing tiers, customer-story grid, template cards) | `{motion.duration-base}` per item, `{motion.stagger-step}` between | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px → 0)` | Stagger collapses to zero; all items fade in together at `{motion.duration-reduced}` |
| List exit (filtered-out story cards) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Opacity fade at `{motion.duration-reduced}`; no scale |
| Loading (button spinner, card skeleton) | `{motion.duration-emphasis}` loop | `linear` for the spinner rotation | `transform: rotate()` on the spinner; `opacity` pulse on skeletons | Spinner frozen; skeleton pulse replaced by a static `{colors.hairline-soft}` block |
| Hero mockup ambience (sticky notes drifting at z-offsets) | `{motion.duration-emphasis}` loop | `{motion.ease-standard}` | `transform: translate()` and `opacity` | Frozen at its rest frame |

### Motion Rules

- Only `transform` and `opacity` are animated. Never animate `width`, `height`, `top`, `left` or `margin` — the comparison table and the 4-tier pricing row are wide enough that a layout-triggering property would stutter.
- Every exit is shorter than its matching entrance: modal `{motion.duration-fast}` out against `{motion.duration-base}` in, dropdown `{motion.duration-instant}` out against `{motion.duration-fast}` in.
- Nothing animates on first paint in a way that delays content. The hero headline and its CTA row render immediately; the whiteboard mockup's ambient drift starts only after the mockup has painted.
- The only infinite animations are the loading spinner, the skeleton pulse, and the hero whiteboard's sticky-note ambience. That ambience is deliberate brand atmosphere, stated as such, and it is the one place this system moves without a user action.
- The `{motion.ease-enter}` overshoot is the brand signature: a reveal that lands slightly past its mark and settles, mirroring how a dragged sticky note behaves on the real canvas. Keep it on enter only; an exit that overshoots reads as a glitch.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. No translateY on page, toast, dropdown
     or list enter; no scale pop on press; no 1.02 card hover scale; no
     overshoot from {motion.ease-enter}. */
  /* Kept: opacity cross-fades only, capped at {motion.duration-reduced} (130ms).
     Focus rings appear instantly at full opacity. */
  /* Frozen: the hero whiteboard sticky-note ambience holds its rest frame, and
     the loading spinner stops rotating — a static skeleton block at
     {colors.hairline-soft} stands in for the pulse. */
}
```

## Accessibility

### Measured Contrast

Every ratio below is computed with WCAG 2.1 relative luminance from this file's own token values. **Miro's extracted utility tones genuinely fail WCAG AA, and the failures are disclosed rather than corrected** — these are real extracted values, and falsifying them would make the document wrong.

Passing pairs:

| Pair | Ratio | Required | Result |
|---|---|---|---|
| {colors.ink} on {colors.canvas} | 17.01:1 | 4.5:1 | Pass |
| {colors.ink} on {colors.surface} | 16.01:1 | 4.5:1 | Pass |
| {colors.on-primary} on {colors.primary} | 17.01:1 | 4.5:1 | Pass |
| {colors.slate} on {colors.canvas} | 6.87:1 | 4.5:1 | Pass |
| {colors.steel} on {colors.canvas} | 5.0:1 | 4.5:1 | Pass |
| {colors.yellow-dark} on {colors.surface-yellow} | 5.76:1 | 4.5:1 | Pass |
| {colors.coral-dark} on {colors.coral-light} | 9.45:1 | 4.5:1 | Pass |
| {colors.moss-dark} on {colors.teal-light} | 4.77:1 | 4.5:1 | Pass |
| {colors.primary} on {colors.brand-yellow} | 11.6:1 | 4.5:1 | Pass |
| {colors.primary} on {colors.coral-light} | 11.46:1 | 4.5:1 | Pass |
| {colors.primary} on {colors.teal-light} | 14.84:1 | 4.5:1 | Pass |
| {colors.primary} on {colors.rose-light} | 13.85:1 | 4.5:1 | Pass |
| {colors.on-dark-muted} on {colors.footer-bg} | 7.19:1 | 4.5:1 | Pass |
| {colors.hairline-control} on {colors.canvas} | 3.3:1 | 3.0:1 | Pass (prescribed token) |
| {colors.hairline-control} on {colors.surface} | 3.1:1 | 3.0:1 | Pass (prescribed token) |

Disclosed failures — the real brand does not reach AA at these points:

| Pair | Ratio | Required | Note |
|---|---|---|---|
| `hairline-soft` on `surface` | 1.07:1 | 3.0:1 | Decorative table-row rule only. Fails as a component boundary; use `{colors.hairline-control}` where the edge carries meaning. |
| `hairline-soft` on `canvas` | 1.14:1 | 3.0:1 | Decorative card and row edge only. Fails as a component boundary. |
| `hairline` on `surface` | 1.22:1 | 3.0:1 | Decorative divider only. Fails as a component boundary. |
| `hairline` on `canvas` | 1.3:1 | 3.0:1 | Decorative divider only. Fails as a component boundary; the real `search-pill`, `template-card` and `faq-accordion-item` borders sit here. |
| `hairline-strong` on `surface` | 1.54:1 | 3.0:1 | Fails as a control boundary even at its strongest extracted value. |
| `hairline-strong` on `canvas` | 1.64:1 | 3.0:1 | This is the only edge of `text-input`, `button-secondary` and `filter-dropdown` on the live site, and it fails the 3:1 non-text minimum by a wide margin. The prescribed `{colors.hairline-control}` is the accessible parallel. |
| `muted` on `surface` | 2.23:1 | 4.5:1 | Placeholder and disabled-label tone. Fails as secondary text. |
| `muted` on `canvas` | 2.37:1 | 4.5:1 | Fails as secondary text. Use `{colors.steel}` (5.0:1) or `{colors.slate}` (6.87:1) for any caption that must be read. |
| `success-accent` on `canvas` | 2.7:1 | 4.5:1 | Fails as text. Usable as a fill or an icon beside a text label, not as the label. |
| `footer-link` | 2.37:1 | 4.5:1 | `{colors.on-dark-muted}` reaches 7.19:1 on the actual dark footer it is drawn on; the 2.37:1 figure is that same ink measured against the page canvas, which is not where the component sits. Disclosed because the component declares no `backgroundColor` of its own. |
| `badge-success` | 2.7:1 | 4.5:1 | White label on {colors.success-accent}. Fails. {colors.primary} on the same green reaches 6.3:1 and is the recommended correction. |
| `badge-tag-purple` | 4.33:1 | 4.5:1 | {colors.brand-blue} on {colors.surface-pricing-featured}, a near miss on 13px text. Passes at 3:1 if the chip label is set at 18.66px/700 or larger, which it is not. |

Two tones the palette carries — {colors.brand-orange-light} and {colors.brand-red-dark} — are **never bound to an ink in `components:`**, so no text pair involving them is measurable from this file. They are documented as a feature-card background and an error border respectively; the pairs they would form were never asserted.

### Focus Ring Visibility

{colors.focus} is a single ring for every surface this file defines, drawn 2px wide at a 2px offset outside the control, so it is measured against the surface behind the control:

| Surface drawn on | Ratio | Required | Result |
|---|---|---|---|
| {colors.canvas} | 4.75:1 | 3.0:1 | Pass |
| {colors.surface} | 4.47:1 | 3.0:1 | Pass |
| {colors.surface-soft} | 4.58:1 | 3.0:1 | Pass |
| {colors.surface-yellow} | 4.47:1 | 3.0:1 | Pass |
| {colors.surface-pricing-featured} | 4.33:1 | 3.0:1 | Pass |
| {colors.primary} / {colors.footer-bg} (dark CTA banner, footer, enterprise card) | 3.58:1 | 3.0:1 | Pass |
| {colors.brand-yellow} feature card | 3.24:1 | 3.0:1 | Pass |
| {colors.coral-light} feature card | 3.2:1 | 3.0:1 | Pass |
| {colors.teal-light} feature card | 4.14:1 | 3.0:1 | Pass |
| {colors.rose-light} / {colors.brand-pink} feature card | 3.87:1 | 3.0:1 | Pass |
| {colors.brand-rose} feature card | 3.7:1 | 3.0:1 | Pass |
| {colors.brand-orange-light} feature card | 3.95:1 | 3.0:1 | Pass |

One ring serves all of them because {colors.brand-blue} sits mid-luminance: light enough to clear 3:1 on the dark footer, dark enough to clear 3:1 on white. No `focus-on-dark` companion is needed, and inventing one would be a token that exists only to fill a slot. The single gap is {colors.brand-red-dark} at 2.95:1, which is an error *border* and never a surface a control is placed on.

### Minimum Tap Target

Taken from the values this file already documents, not from a rendered page:

- Pill buttons: 40–44px effective height — meets the 44px AAA floor at the top of that range and sits 4px under it at the bottom
- Form inputs: 44px — passes
- `search-pill`: 40px — passes the 24px AA minimum, under the 44px AAA floor
- `button-icon-circular`: 36×36px on desktop, 44×44px on mobile — the desktop size passes AA (24px) and fails AAA
- `filter-dropdown`: ~36px, bumping to 44px on mobile — same result

Rendered tap-target size cannot be verified from a document; these are the documented box sizes, not measured hit areas.

### Reduced Motion

The full rule is in **Motion & Animation** above. In short: all travel and all scale are removed, opacity cross-fades are capped at `{motion.duration-reduced}` (130ms), focus rings appear instantly, and the hero whiteboard's sticky-note ambience freezes at its rest frame.

## Do's and Don'ts

### Do
- Reserve `{colors.brand-yellow}` for the wordmark, top promo banner, and "yellow tag" chips
- Use `{colors.primary}` (black) as the dominant CTA on all surfaces
- Pair pastel feature cards (yellow, rose, coral, teal) with white feature cards in the same viewport
- Apply `{rounded.full}` to every button, every pill tab, every status badge
- Apply `{rounded.xxxl}` (28px) to pastel feature cards
- Use real Miro-board mockups as feature illustrations
- Maintain Roobert PRO across every UI surface
- Draw focus with the single {colors.focus} ring at 2px width and 2px offset, on every surface including the dark footer
- Use {colors.hairline-control} wherever a border is a control's only edge; keep the extracted hairlines for decoration
- Keep the `{motion.ease-enter}` overshoot on entrances only — it is the sticky-note settle, and it is the brand's one motion signature

### Don't
- Don't use `{colors.brand-yellow}` on standard CTAs or large background surfaces
- Don't introduce additional accent colors beyond yellow + brand pastels
- Don't soften corners on buttons; the pill is a brand signature
- Don't reduce hero leading below 1.05
- Don't apply heavy shadows on flat documentation cards; reserve elevation for whiteboard mockups
- Don't use stock photography — show the live product board UI
- Don't animate `width`, `height`, `top`, `left` or `margin`; `transform` and `opacity` only
- Don't let an exit run longer than its matching entrance
- Don't use {colors.muted} or {colors.success-accent} as text — both fail AA on {colors.canvas}

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile (small) | < 480px | Single column. Hero scales to 36px. Pill nav collapses to hamburger. Pricing tiers stack 1-up. |
| Mobile (large) | 480 – 767px | Feature tiles 2-up. Hero scales to 48px. |
| Tablet | 768 – 1023px | 2-column feature grids. Pill-tab nav returns. |
| Desktop | 1024 – 1279px | 4-tier pricing card row. Customer story grid 2-up. Hero at 64px. |
| Wide Desktop | ≥ 1280px | Full hero presentation, 80px hero display. |

### Touch Targets
- Pill buttons render at 40–44px effective height — at WCAG AAA floor
- Circular icon buttons: 36×36px desktop → 44×44px mobile
- Form inputs render at 44px height
- Filter dropdowns render at ~36px tall — bumps to 44px on mobile

### Collapsing Strategy
- **Promo banner** stays full-width; truncates at < 480px
- **Top nav** below 1024px collapses to hamburger
- **Hero band**: 2-column hero collapses to stacked at < 1024px
- **Pricing comparison**: 4-column tiers → 2-column tablet → 1-column mobile; comparison table becomes horizontal-scroll
- **Customer story grid**: 2-up → 1-up at < 768px
- **Hero typography**: 80px → 60px tablet → 48px mobile-large → 36px mobile-small
- **Footer**: 6-column desktop → 3-column tablet → 2-column mobile → accordion at small mobile

### Image Behavior
- Whiteboard mockups maintain aspect ratio; lazy-loaded below the fold
- Customer story photography uses 16:9 ratio with full-bleed scaling
- Logo wall presents wordmarks at consistent 100px height

## Iteration Guide

1. Focus on ONE component at a time
2. Reference component names and tokens directly
3. Run `npx @google/design.md lint DESIGN.md` after edits
4. Add new variants as separate `components:` entries
5. Default to `{typography.body-md}` for body and `{typography.subtitle}` for emphasis
6. Keep `{colors.brand-yellow}` confined to wordmark, promo banner, and yellow-tag chips
7. Pill-shaped buttons (`{rounded.full}`) always
8. When showing the product, use a real Miro-board mockup with sticky-note color tints

## Known Gaps

- Specific dark-mode token values not surfaced
- Animation and transition timings were **not** extracted from the live site. The Motion & Animation section is prescribed from the Playful profile and says so in its own first line; do not cite any duration or easing in this file as a measured Miro value.
- `{colors.hairline-control}` is prescribed, not extracted. Miro's real control borders are `{colors.hairline-strong}` at 1.64:1 and fail WCAG AA.
- Hover, focus-visible, loading, selected and error states were not extracted; the State Coverage table derives them from tokens this file already carries and is labelled prescribed
- Form validation success state not explicitly captured beyond defaults
- Sticky note color tints inside the actual whiteboard product are richer than what marketing surfaces capture
