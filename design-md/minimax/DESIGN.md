---
version: alpha
name: MiniMax-design-analysis
description: MiniMax presents itself as a premium AI infrastructure brand through a striking duality — bold black-pill CTAs and stark white canvas for marketing, paired with vibrant gradient product cards (orange-red, magenta-pink, purple, blue) that turn each model release into a distinctive visual identity. The system uses DM Sans across all surfaces, employs an oversized 80px hero display, anchors major actions in deep near-black pills, and layers content density via a 3-column documentation grid with sidebar nav, prose body, and TOC. Coverage spans the marketing homepage, model showcase pages, developer documentation, and platform pricing surfaces.

colors:
  primary: "#0a0a0a"
  on-primary: "#ffffff"
  primary-soft: "#181e25"
  brand-coral: "#ff5530"
  brand-magenta: "#ea5ec1"
  brand-blue: "#1456f0"
  brand-blue-mid: "#3b82f6"
  brand-blue-deep: "#1d4ed8"
  brand-blue-700: "#17437d"
  brand-cyan: "#3daeff"
  brand-blue-200: "#bfdbfe"
  brand-purple: "#a855f7"
  canvas: "#ffffff"
  surface: "#f7f8fa"
  surface-soft: "#f2f3f5"
  hairline: "#e5e7eb"
  hairline-soft: "#eaecf0"
  ink: "#0a0a0a"
  ink-strong: "#000000"
  charcoal: "#222222"
  slate: "#45515e"
  steel: "#5f5f5f"
  stone: "#8e8e93"
  muted: "#a8aab2"
  success-bg: "#e8ffea"
  success-text: "#1ba673"
  on-dark: "#ffffff"
  footer-bg: "#0a0a0a"
  hairline-strong: "#767a85"
  muted-strong: "#6f717a"
  success-text-strong: "#0f7a50"
  focus: "#1456f0"
  focus-on-dark: "#ffffff"

typography:
  hero-display:
    fontFamily: DM Sans
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -2px
  display-lg:
    fontFamily: DM Sans
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.5px
  heading-lg:
    fontFamily: DM Sans
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -1px
  heading-md:
    fontFamily: DM Sans
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  heading-sm:
    fontFamily: DM Sans
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.30
  card-title:
    fontFamily: DM Sans
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
  subtitle:
    fontFamily: DM Sans
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.50
  body-md:
    fontFamily: DM Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
  body-md-bold:
    fontFamily: DM Sans
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.50
  body-sm:
    fontFamily: DM Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
  body-sm-medium:
    fontFamily: DM Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
  caption:
    fontFamily: DM Sans
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.70
  caption-bold:
    fontFamily: DM Sans
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.50
  micro:
    fontFamily: DM Sans
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
  button-md:
    fontFamily: DM Sans
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.40

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 20px
  xxxl: 24px
  hero: 32px
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
  section-lg: 80px
  hero: 96px

shadow:
  subtle: "rgba(0, 0, 0, 0.04) 0px 1px 2px 0px"
  card: "rgba(0, 0, 0, 0.08) 0px 4px 6px 0px"
  atmospheric: "rgba(0, 0, 0, 0.08) 0px 0px 22px 0px"
  modal: "rgba(36, 36, 36, 0.08) 0px 12px 16px -4px"
  purple-ambient: "rgba(44, 30, 116, 0.16) 0px 0px 15px 0px"

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
    rounded: "{rounded.full}"
    padding: "11px 24px"
  button-primary-pressed:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
  button-primary-hover:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
  button-primary-focus-visible:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    outline: "2px solid {colors.focus}"
    outlineOffset: "2px"
  button-primary-loading:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "11px 24px"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "11px 24px"
    border: "1px solid {colors.hairline}"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-medium}"
    padding: "8px 0"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 36px
    border: "1px solid {colors.hairline}"
  product-card-coral:
    backgroundColor: "{colors.brand-coral}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.hero}"
    padding: "{spacing.xxl}"
  product-card-magenta:
    backgroundColor: "{colors.brand-magenta}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.hero}"
    padding: "{spacing.xxl}"
  product-card-blue:
    backgroundColor: "{colors.brand-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.hero}"
    padding: "{spacing.xxl}"
  product-card-purple:
    backgroundColor: "{colors.brand-purple}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.hero}"
    padding: "{spacing.xxl}"
  product-card-photo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.hero}"
    padding: "{spacing.xxl}"
  card-base:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  card-feature:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
  card-recommendation:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  promo-cta-card:
    backgroundColor: "{colors.brand-coral}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.hero}"
    padding: "{spacing.section}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline-strong}"
    height: 40px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.brand-blue-deep}"
    outline: "2px solid {colors.focus}"
    outlineOffset: "2px"
  text-input-disabled:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid #d45656"
  search-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xs} {spacing.md}"
    height: 36px
    border: "1px solid {colors.hairline-strong}"
  segmented-tab:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.button-md}"
    rounded: "0"
    padding: "{spacing.md} {spacing.lg}"
    border: "0 0 2px transparent solid"
  segmented-tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "0 0 2px {colors.ink} solid"
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
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-success-accessible:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text-strong}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-new:
    backgroundColor: "{colors.brand-coral}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-beta:
    backgroundColor: "{colors.brand-blue-200}"
    textColor: "{colors.brand-blue-deep}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-code:
    backgroundColor: "{colors.brand-blue-200}"
    textColor: "{colors.brand-blue-deep}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm-medium}"
    padding: "{spacing.sm} {spacing.lg}"
  data-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  data-table-header:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.steel}"
    typography: "{typography.caption-bold}"
    padding: "{spacing.sm} {spacing.md}"
  data-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md}"
    border: "0 0 1px {colors.hairline-soft} solid"
  sidebar-nav-item:
    backgroundColor: "transparent"
    textColor: "{colors.charcoal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
  sidebar-nav-item-active:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-medium}"
  doc-toc-item:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} 0"
  ai-product-tile:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  footer-region:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-link:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxs} 0"
  hero-band-marketing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.hero-display}"
    rounded: "{rounded.lg}"
    padding: "{spacing.hero}"
  product-matrix-grid:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.hero}"
    padding: "{spacing.xxl}"
  ai-product-matrix:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xxxl}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  docs-prose-block:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.charcoal}"
    typography: "{typography.body-md}"
    padding: "{spacing.xxl}"
  models-comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  testimonial-stat-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-lg}"
    padding: "{spacing.xl}"
---

## Overview

MiniMax stages itself as a Chinese AI infrastructure brand with a sophisticated dual identity. Marketing surfaces and platform pages anchor in stark white canvas with deep-black typographic emphasis — the brand voice is confident, technical, almost editorial. But each model release gets its own vibrant gradient identity card: M2.7 in volcanic coral-red, Music 2.6 in magenta-pink, Hailuo in deep blue, Speech 2.8 in saturated orange-purple. Together these vibrant tiles read like album covers laid out on the homepage — each one declaring its own product personality.

DM Sans anchors every surface from oversized 80px hero displays down to 12px micro labels. The geometric, slightly humanist character of the face suits both the dense documentation surfaces (where 14px body type carries 1.5 line-height for long-form prose) and the high-impact marketing displays (where -2px letter-spacing tightens 80px headlines). Buttons are universally pill-shaped (`rounded-full`) with a sharp two-tier system: black-pill primary (the dominant CTA) and outline-pill secondary. Cards split into two distinct families: vibrant gradient product showcases (32px corner softening) and quiet white documentation cards (16px corner softening).

**Key Characteristics:**
- Stark monochrome palette — black ({colors.primary}) and white ({colors.canvas}) — broken open by saturated brand-color gradient cards
- Distinct product-color encoding: each model line has its own vibrant brand color (coral M2.7, magenta Music 2.6, blue Hailuo, orange Speech 2.8)
- DM Sans across the entire system; Inter as fallback
- Pill-shaped buttons ({rounded.full}) and pill-shaped tabs everywhere; rectangular forms only inside data tables and dense docs
- Hero typography uses tight 1.10 line-height with -2px letter-spacing for impact
- Documentation surfaces use a 3-column layout: left sidebar nav, center prose body, right table-of-contents
- Black promo banners ({colors.primary}) above the nav for time-bound brand moments

## Colors

> Source pages: minimax.io/ (homepage), /models/text/m27 (product showcase), platform.minimax.io/docs/guides/models-intro (documentation), /subscribe/token-plan (pricing). Token coverage was identical across all four pages.

### Brand & Accent
- **Brand Coral** ({colors.brand-coral}): Signature high-impact accent. Used on M2.7 product card, "Token Plan" hero band, promo CTA strips, and "NEW" badges. Carries the brand's most attention-grabbing energy.
- **Brand Magenta** ({colors.brand-magenta}): Secondary product-card identity (Music 2.6); used for music/audio product encoding.
- **Brand Blue** ({colors.brand-blue}): Hailuo video product identity; primary blue accent across the system.
- **Brand Blue Deep** ({colors.brand-blue-deep}): Form-control activation, link emphasis.
- **Brand Blue 700** ({colors.brand-blue-700}): Documentation tag and reference text color.
- **Brand Cyan** ({colors.brand-cyan}): Atmospheric blue for product gradients and decorative wash.
- **Brand Blue 200** ({colors.brand-blue-200}): Code badges, info-tag backgrounds.
- **Brand Purple** ({colors.brand-purple}): Speech 2.8 and minor purple-product identity; gradient mate for magenta cards.

### Surface
- **Canvas White** ({colors.canvas}): Primary page background and card surface.
- **Surface** ({colors.surface}): Subtle section backgrounds, search-pill rest, sidebar-nav active state.
- **Surface Soft** ({colors.surface-soft}): Quieter section divisions.
- **Hairline** ({colors.hairline}): 1px input border and primary divider.
- **Hairline Soft** ({colors.hairline-soft}): Quieter table-row divider and secondary section break.
- **Hairline Strong** ({colors.hairline-strong}) — **prescribed, not extracted**: Parallel accessible boundary for controls whose border is their only edge (text inputs, search pill). The extracted `{colors.hairline}` and `{colors.hairline-soft}` are scoped to decoration from here on — section breaks, table-row rules, card edges that sit beside other cues. Measures 4.29:1 on `{colors.canvas}` and 4.04:1 on `{colors.surface}`.

### Focus
- **Focus** ({colors.focus}) — **prescribed, not extracted**: The brand's own `{colors.brand-blue}` reused as the focus ring for every light surface — canvas, surface, surface-soft. Drawn as a 2px ring with a 2px offset outside the control, so WCAG 2.2 Focus Appearance measures it against the surface behind the control, not against the control's own fill. Measures 5.80:1 on `{colors.canvas}`, 5.46:1 on `{colors.surface}`, 5.23:1 on `{colors.surface-soft}`. A single ring cannot serve this file, because MiniMax ships both a white marketing canvas and black/saturated signature surfaces — hence the pair below.
- **Focus On Dark** ({colors.focus-on-dark}) — **prescribed, not extracted**: White ring, 2px with a 2px offset, for the black footer, the black promo banner and the vibrant product cards. Measures 19.80:1 on `{colors.footer-bg}`, 5.80:1 on `{colors.brand-blue}`, 3.96:1 on `{colors.brand-purple}`, 3.18:1 on `{colors.brand-coral}`, 3.06:1 on `{colors.brand-magenta}` — clearing 3:1 on every surface it can land on. Over `product-card-photo`, where the ground is photography and has no measurable colour, the ring is two-tone: `{colors.focus-on-dark}` with a 1px outer edge in `{colors.ink-strong}` (the two bands separate at 21.0:1).

### Text
- **Ink** ({colors.ink}): Primary headline and CTA text — the brand's near-black anchor.
- **Ink Strong** ({colors.ink-strong}): Pure black used in promo banners and hero displays for maximum contrast.
- **Charcoal** ({colors.charcoal}): Body text on light surfaces.
- **Slate** ({colors.slate}): Secondary text, metadata.
- **Steel** ({colors.steel}): Tertiary text, table headers, sidebar inactive items.
- **Stone** ({colors.stone}): Muted captions and tab inactive labels.
- **Muted** ({colors.muted}): Footer link text and de-emphasized labels. On the black footer it is the right tone (8.54:1); on white it is decoration only — see Accessibility.
- **Muted Strong** ({colors.muted-strong}) — **prescribed, not extracted**: Parallel accessible tone for de-emphasized text that has to sit on a light surface, where `{colors.muted}` fails AA. Measures 4.86:1 on `{colors.canvas}` and 4.58:1 on `{colors.surface}`.

### Semantic
- **Success Background** ({colors.success-bg}): Pale-green wash for success badges and confirmations.
- **Success Text** ({colors.success-text}): Deep-green ink for success badge labels. The extracted pairing fails AA at 13px — see Accessibility.
- **Success Text Strong** ({colors.success-text-strong}) — **prescribed, not extracted**: Parallel accessible green for the same badge label, 5.08:1 on `{colors.success-bg}` and 5.36:1 on `{colors.canvas}`. Used by `badge-success-accessible`.
- Error tones derive from a `#d45656` red used in input border error states (not extracted as a top-level system token).

## Typography

### Font Family
**DM Sans** (primary): Geometric variable sans-serif. Used across every surface, every role. Fallbacks: Inter, Helvetica Neue, Helvetica, Arial.

DM Sans was chosen for its dual fluency: it scales cleanly from 80px hero displays (where -2px letter-spacing creates magazine-grade tightness) down to 12px micro labels (where the slightly humanist counters maintain legibility). The face has no italic variant in the brand's deployment — emphasis comes from weight (500/600/700) instead.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 80px | 600 | 1.10 | -2px | Homepage hero ("MiniMax Music 2.6") |
| `{typography.display-lg}` | 56px | 600 | 1.10 | -1.5px | Section openers, major page heroes |
| `{typography.heading-lg}` | 40px | 600 | 1.20 | -1px | Sub-page headlines ("Token Plan", "Models Overview") |
| `{typography.heading-md}` | 32px | 600 | 1.25 | -0.5px | Subsection headers ("Full-Stack Model Matrix") |
| `{typography.heading-sm}` | 24px | 600 | 1.30 | 0 | Card titles, feature headers |
| `{typography.card-title}` | 20px | 600 | 1.40 | 0 | Product-card titles, feature-tile headers |
| `{typography.subtitle}` | 18px | 500 | 1.50 | 0 | Section subtitles, lead body |
| `{typography.body-md}` | 16px | 400 | 1.50 | 0 | Primary body text |
| `{typography.body-md-bold}` | 16px | 700 | 1.50 | 0 | Body emphasis |
| `{typography.body-sm}` | 14px | 400 | 1.50 | 0 | Secondary body, table cells, navigation |
| `{typography.body-sm-medium}` | 14px | 500 | 1.50 | 0 | Active sidebar nav, button labels |
| `{typography.caption}` | 13px | 400 | 1.70 | 0 | Documentation captions, fine print |
| `{typography.caption-bold}` | 13px | 600 | 1.50 | 0 | Badge labels, table-header text |
| `{typography.micro}` | 12px | 400 | 1.50 | 0 | Footer microcopy, chip labels |
| `{typography.button-md}` | 14px | 600 | 1.40 | 0 | Pill button labels |

### Principles
- **Tight hero leading** (1.10) and aggressive negative letter-spacing on display sizes create a magazine-quality typographic display unique to MiniMax.
- **Generous body leading** (1.50) keeps long-form documentation comfortable; captions push to 1.70 for scientific-paper-grade clarity.
- **Weight discipline:** 400 (body), 500 (medium emphasis), 600 (headings/buttons), 700 (strong inline emphasis). Heavier weights are not used.
- **Single typeface** strategy — never mix DM Sans with another sans-serif. Code samples (when shown) use a system monospace fallback, but no second typeface enters the brand canvas.

## Layout

### Spacing System
- **Base unit**: 4px (8px primary increment).
- **Tokens**: `{spacing.xxs}` (4px) · `{spacing.xs}` (8px) · `{spacing.sm}` (12px) · `{spacing.md}` (16px) · `{spacing.lg}` (20px) · `{spacing.xl}` (24px) · `{spacing.xxl}` (32px) · `{spacing.xxxl}` (40px) · `{spacing.section-sm}` (48px) · `{spacing.section}` (64px) · `{spacing.section-lg}` (80px) · `{spacing.hero}` (96px).
- **Section rhythm**: Marketing pages separate at `{spacing.hero}` (96px) above-fold, then `{spacing.section-lg}` (80px) below; documentation tightens to `{spacing.section}` (64px); table rows compress to `{spacing.md}` (16px).
- **Card internal padding**: Vibrant product cards use `{spacing.xxl}` (32px); documentation cards use `{spacing.lg}–{spacing.xl}` (20–24px); promo strips expand to `{spacing.section}` (64px).

### Grid & Container
- Marketing pages use a 1280px max-width with 32px gutters.
- Homepage product matrix renders as a 4-column row of 32px-rounded gradient cards, each ~280–320px wide.
- AI Product Matrix below uses a 4-column grid with 16px-rounded white cards.
- Documentation surfaces use a 3-column layout: left sidebar nav (~220px), center prose body (~720px max-width), right TOC (~180px). Sidebar persists on desktop; collapses to drawer below 1024px.
- Token Plan / pricing pages use 2-column tabs above a 3-column tier card grid.

### Whitespace Philosophy
Marketing pages give product photography and color cards generous breathing room — `{spacing.hero}` (96px) above-the-fold creates visual oxygen for the 80px hero display. Inside documentation, whitespace tightens dramatically: section gaps drop to `{spacing.xxl}` (32px), table rows pack down to `{spacing.md}` (16px), and the sidebar nav uses `{spacing.xs}` (8px) vertical rhythm.

## Elevation & Depth

The system runs predominantly flat. Elevation is reserved for sticky panels, dropdowns, and the rare floating CTA.

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow; `{colors.hairline}` border on containers, `{colors.hairline-strong}` on controls | Default cards, table rows, form inputs |
| 1 (subtle) | `{shadow.subtle}` — `rgba(0, 0, 0, 0.04) 0px 1px 2px 0px` | Card-recommendation, hover-elevated tiles |
| 2 (card) | `{shadow.card}` — `rgba(0, 0, 0, 0.08) 0px 4px 6px 0px` | Standard feature cards, dropdowns |
| 3 (atmospheric) | `{shadow.atmospheric}` — `rgba(0, 0, 0, 0.08) 0px 0px 22px 0px` | Diffuse glow on featured product cards |
| 4 (modal) | `{shadow.modal}` — `rgba(36, 36, 36, 0.08) 0px 12px 16px -4px` | Modals, confirmation dialogs, sticky panels |

Elevation is expressed one way per layer: level 0 is border-only, levels 1–4 are
shadow-only. No component carries both a visible border and a shadow.

### Layer separation, measured

The three light grounds sit almost on top of each other: `{colors.canvas}` to
`{colors.surface}` is 1.06:1, `{colors.canvas}` to `{colors.surface-soft}` is
1.11:1, and `{colors.surface}` to `{colors.surface-soft}` is 1.04:1. That is the
brand's choice — the system is deliberately flat and reads as one white page — but
it means tone alone does not separate a panel from the page. `card-feature`, which
is the one component relying on a bare `{colors.surface}` fill with no border,
carries the weakest edge in the system. Where a panel has to be legible as a
distinct surface, give it the level-0 border or a level-1 shadow rather than the
tonal step.

### Decorative Depth
- The vibrant gradient product cards carry their own atmospheric depth via internal radial gradients and silhouette imagery — no shadow needed; the color does the work.
- Brand-tinted shadows (`{shadow.purple-ambient}` — `rgba(44, 30, 116, 0.16) 0px 0px 15px 0px`) appear under purple-themed cards for subtle ambient lift.
- Dotted/grain textures occasionally appear inside product cards as photographic-content decoration; these are not formalized as system tokens.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Code chips, micro-controls |
| `{rounded.sm}` | 6px | Compact controls, table cells |
| `{rounded.md}` | 8px | Inputs, secondary buttons, search pill |
| `{rounded.lg}` | 12px | Documentation cards, recommendation tiles |
| `{rounded.xl}` | 16px | Standard feature cards, AI product tiles |
| `{rounded.xxl}` | 20px | Larger feature panels |
| `{rounded.xxxl}` | 24px | AI product tile feature variants |
| `{rounded.hero}` | 32px | Vibrant gradient product cards, promo CTA strip |
| `{rounded.full}` | 9999px | All buttons, all pill tabs, badges |

### Photography Geometry
- Vibrant product cards use 32px corner softening — distinct from the 16px used on quiet white cards. The doubled radius is the visual signature of "this is a featured product moment."
- Product imagery inside cards is treated as photographic content (silhouettes, dark portrait studio lighting) without rounded internal frames.
- Avatar circles (rare, in testimonials) are `{rounded.full}` — perfect circles.

## Components

> Default, pressed/active, disabled and error states below are extracted from the
> four source pages. Hover, focus-visible, loading and selected were not observable
> in a static capture, so the entries marked **prescribed** below are prescribed to
> match the brand's visual identity, not measured from the live site.

### State coverage

| Component family | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | extracted | prescribed `{colors.charcoal}` fill | prescribed 2px `{colors.focus}` ring, 2px offset | extracted `{colors.charcoal}` | extracted `{colors.hairline}` / `{colors.muted}` | prescribed — label swaps for an inline spinner, pill width frozen | n/a | n/a |
| `button-secondary` · `button-tertiary` | extracted | prescribed — border steps to `{colors.ink}` | prescribed 2px `{colors.focus}` ring, 2px offset | prescribed — fill steps to `{colors.surface}` | prescribed `{colors.muted}` label | prescribed inline spinner | n/a | n/a |
| `button-icon-circular` | extracted | prescribed `{colors.surface}` fill | prescribed 2px `{colors.focus}` ring, 2px offset | prescribed `{colors.surface-soft}` fill | prescribed `{colors.muted}` glyph | n/a | n/a | n/a |
| `text-input` | extracted | prescribed — border steps to `{colors.ink}` | extracted `text-input-focused` border + prescribed `{colors.focus}` ring | n/a | prescribed `text-input-disabled` | n/a | n/a | extracted `text-input-error` |
| `search-pill` | extracted | prescribed `{colors.surface-soft}` fill | prescribed 2px `{colors.focus}` ring, 2px offset | n/a | n/a | prescribed — results area shows a skeleton row | n/a | n/a |
| `segmented-tab` · `pill-tab` | extracted | prescribed — label steps to `{colors.ink}` | prescribed 2px `{colors.focus}` ring, 2px offset | extracted `-active` | prescribed `{colors.muted}` label | n/a | extracted `-active` is the selected state | n/a |
| `sidebar-nav-item` · `doc-toc-item` | extracted | prescribed `{colors.surface}` fill | prescribed 2px `{colors.focus}` ring, 2px offset | prescribed — label steps to `{colors.ink}` | n/a | n/a | extracted `sidebar-nav-item-active` is the selected state | n/a |
| `product-card-*` | extracted | prescribed — card lifts `scale(1.01)` | prescribed 2px `{colors.focus-on-dark}` ring, 2px offset | prescribed `scale(0.99)` | n/a | prescribed — image area fades in at `{motion.duration-base}` | n/a | n/a |
| `card-base` · `card-recommendation` · `ai-product-tile` | extracted | prescribed `{shadow.subtle}` lift | prescribed 2px `{colors.focus}` ring, 2px offset | prescribed — no press treatment on non-interactive cards | n/a | prescribed skeleton block | n/a | n/a |
| `badge-success` · `badge-new` · `badge-beta` · `badge-code` | extracted | n/a — badges are not interactive | n/a | n/a | n/a | n/a | n/a | n/a |
| `data-table-row` | extracted | prescribed `{colors.surface}` fill | prescribed 2px `{colors.focus}` ring, 2px offset | n/a | n/a | prescribed — three skeleton rows while fetching | prescribed `{colors.surface}` fill with `{colors.ink}` label | n/a |
| `promo-banner` | extracted | n/a | prescribed 2px `{colors.focus-on-dark}` ring on its inline link | n/a | n/a | n/a | n/a | n/a |
| `footer-link` | extracted | prescribed — opacity step, colour frozen | prescribed 2px `{colors.focus-on-dark}` ring, 2px offset | extracted — opacity shift only | n/a | n/a | n/a | n/a |

Badges carry genuinely one state: they are static labels, never interactive.

### Buttons

**`button-primary`** — Black pill primary CTA, the dominant action across all surfaces.
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.button-md}`, padding `11px 24px`, rounded `{rounded.full}`.
- Pressed state `button-primary-pressed` lifts to `{colors.charcoal}`.
- Disabled state `button-primary-disabled` uses `{colors.hairline}` background and `{colors.muted}` text.
- Prescribed: `button-primary-hover` shares the `{colors.charcoal}` fill; `button-primary-focus-visible` adds a 2px `{colors.focus}` ring at 2px offset; `button-primary-loading` keeps the pill at its rest width and swaps the label for an inline spinner.

**`button-secondary`** — Outlined pill secondary action, paired with primary in dual-CTA hero patterns.
- Background transparent, text `{colors.ink}`, border `1px solid {colors.ink}`, typography `{typography.button-md}`, padding `11px 24px`, rounded `{rounded.full}`.

**`button-tertiary`** — White-fill quieter pill, used for tertiary nav and informational CTAs.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline}`, typography `{typography.button-md}`, padding `11px 24px`, rounded `{rounded.full}`.

**`button-link`** — Inline text link styled as a subtle button.
- Background transparent, text `{colors.ink}`, typography `{typography.body-sm-medium}`, padding `8px 0`. Underline appears on activation.

**`button-icon-circular`** — 36×36px circular utility button (carousel arrows, share, copy).
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline}`, rounded `{rounded.full}`.

### Vibrant Product Cards

**`product-card-coral`** — M2.7 / Token Plan signature card.
- Background `{colors.brand-coral}`, text `{colors.on-dark}`, rounded `{rounded.hero}` (32px), padding `{spacing.xxl}`.
- Hosts the M2.7 wordmark in massive `{typography.display-lg}` with white tagline.

**`product-card-magenta`** — Music 2.6 product showcase.
- Background `{colors.brand-magenta}`, text `{colors.on-dark}`, rounded `{rounded.hero}`, padding `{spacing.xxl}`.

**`product-card-blue`** — Hailuo Video product showcase.
- Background `{colors.brand-blue}`, text `{colors.on-dark}`, rounded `{rounded.hero}`, padding `{spacing.xxl}`.

**`product-card-purple`** — Speech 2.8 / variant product showcase.
- Background `{colors.brand-purple}`, text `{colors.on-dark}`, rounded `{rounded.hero}`, padding `{spacing.xxl}`.

**`product-card-photo`** — Dark portrait product card (homepage S2 placement, video-emotion product).
- Background `{colors.primary}` (black with overlaid product photo), text `{colors.on-dark}`, rounded `{rounded.hero}`, padding `{spacing.xxl}`.

### Cards & Containers

**`card-base`** — Standard documentation/feature card.
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`card-feature`** — Quieter feature panel on light gray.
- Background `{colors.surface}`, rounded `{rounded.xl}`, padding `{spacing.xxl}`.

**`card-recommendation`** — "Recommended Reading" tile in documentation footer.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.lg}`, border `1px solid {colors.hairline}`.

**`promo-cta-card`** — Bright orange "Refunds of 10%..." promo strip with embedded CTA pill.
- Background `{colors.brand-coral}`, text `{colors.on-dark}`, rounded `{rounded.hero}`, padding `{spacing.section}`. Embedded button uses `button-tertiary` (white pill on coral) for the "Join Now" action.

**`ai-product-tile`** — White card in the AI Product Matrix grid (Agent, Hailuo Video, MiniMax Audio).
- Background `{colors.canvas}`, rounded `{rounded.xxxl}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`. Carries an icon/illustration top, title `{typography.card-title}`, description `{typography.body-sm}`.

### Inputs & Forms

**`text-input`** — Standard text field.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline-strong}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, height 40px. The extracted border is `{colors.hairline}` at 1.24:1 on canvas; since this border is the field's only boundary, the prescribed `{colors.hairline-strong}` replaces it here and `{colors.hairline}` stays on decorative edges.

**`text-input-focused`** — Activated state (focus-visible).
- Border switches to `2px solid {colors.brand-blue-deep}`, plus a prescribed 2px `{colors.focus}` ring at 2px offset outside the field.

**`text-input-disabled`** — Prescribed disabled state.
- Background `{colors.surface}`, text `{colors.muted}`, border `1px solid {colors.hairline}`.

**`text-input-error`** — Validation error state.
- Border switches to `1px solid #d45656`; error label below in matching red `{typography.body-sm}`.

**`search-pill`** — Documentation top-bar search field.
- Background `{colors.surface}`, text `{colors.steel}`, typography `{typography.body-sm}`, rounded `{rounded.md}`, height 36px, border `1px solid {colors.hairline-strong}` (same substitution as `text-input`: this border is the control's only edge).

### Tabs

**`segmented-tab`** + **`segmented-tab-active`** — Underline-style tab navigation (Benchmark / Self-Evaluation / Multi-Agent Collaboration on the M2.7 page).
- Inactive: text `{colors.steel}`, transparent background, padding `{spacing.md} {spacing.lg}`. Active: text shifts to `{colors.ink}`, 2px bottom border in `{colors.ink}`.

**`pill-tab`** + **`pill-tab-active`** — Pricing-page tab nav (Token Plan / Audio Subscription / Video Package).
- Inactive: background `{colors.canvas}`, text `{colors.steel}`, border `1px solid {colors.hairline}`, padding `{spacing.xs} {spacing.md}`, rounded `{rounded.full}`.
- Active: background `{colors.primary}`, text `{colors.on-primary}`, no border (or matching black border).

### Badges & Status

**`badge-success`** — Pale-green confirmation badge ("Available", "Active").
- Background `{colors.success-bg}`, text `{colors.success-text}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`. The extracted pairing measures 2.95:1 — a real AA failure at 13px, kept here because it is what the brand ships.
- `badge-success-accessible` is the prescribed parallel: same fill, label in `{colors.success-text-strong}` at 5.08:1. Use it wherever the badge carries information not available elsewhere.

**`badge-new`** — Coral "NEW" / "Live" pill for fresh releases.
- Background `{colors.brand-coral}`, text `{colors.on-dark}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-beta`** — Pale-blue "BETA" / informational pill.
- Background `{colors.brand-blue-200}`, text `{colors.brand-blue-deep}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `4px 10px`.

**`badge-code`** — Inline code-style chip ("Code", "API").
- Background `{colors.brand-blue-200}`, text `{colors.brand-blue-deep}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 6px`.

**`promo-banner`** — Sticky black promotional strip ABOVE the top nav ("Invite & Earn — Rewards for Both!").
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.body-sm-medium}`, padding `{spacing.sm} {spacing.lg}`. Carries one-line copy with optional inline link.

### Data Tables

**`data-table`** — Documentation models comparison table.
- Background `{colors.canvas}`, text `{colors.ink}`, typography `{typography.body-sm}`, rounded `{rounded.md}`, border `1px solid {colors.hairline}`.

**`data-table-header`** — Top header row of the data table.
- Background `{colors.surface}`, text `{colors.steel}`, typography `{typography.caption-bold}`, padding `{spacing.sm} {spacing.md}`.

**`data-table-row`** — Body rows.
- Background `{colors.canvas}`, text `{colors.ink}`, typography `{typography.body-sm}`, padding `{spacing.md}`, bottom border `1px solid {colors.hairline-soft}`.

### Navigation

**Top Navigation (Marketing)** — Sticky white bar with logo, link list, and right-side CTAs.
- Background `{colors.canvas}`, height ~64px, bottom border `1px solid {colors.hairline-soft}`.
- Left: MiniMax wordmark + horizontal link list (Models, Product, API, Company).
- Right: black-pill "Contact Us" + outlined-pill "Login".

**Top Navigation (Documentation/Platform)** — Compressed nav with center search-pill and right-side account/upgrade CTAs.
- Background `{colors.canvas}`, height ~56px, with search-pill at center and "Documentation / Account / Subscribe" links + black-pill "Sign Up" right.

**`sidebar-nav-item`** + **`sidebar-nav-item-active`** — Documentation left rail link entries.
- Inactive: background transparent, text `{colors.charcoal}`, typography `{typography.body-sm}`, rounded `{rounded.sm}`, padding `{spacing.xs} {spacing.md}`.
- Active: background `{colors.surface}`, text `{colors.ink}`, typography `{typography.body-sm-medium}`.

**`doc-toc-item`** — Right-rail table-of-contents links.
- Background transparent, text `{colors.steel}`, typography `{typography.body-sm}`, padding `{spacing.xs} 0`. Active item color shifts to `{colors.ink}`.

### Signature Components

**`hero-band-marketing`** — Centered hero with massive 80px display + dual-CTA pair.
- Layout: centered headline in `{typography.hero-display}` ({colors.ink}), centered subtitle in `{typography.subtitle}` ({colors.steel}), centered button row (`button-primary` + `button-secondary`).

**`product-matrix-grid`** — 4-column horizontal scroll of vibrant gradient product cards (homepage "Full-Stack Model Matrix").
- Each tile uses one of the `product-card-*` variants (coral, magenta, blue, purple, photo).
- Card title in `{typography.display-lg}` (M2.7 wordmark) or `{typography.heading-lg}` (Music 2.6).
- Below the wordmark: thin tagline in `{typography.body-sm}` 80% white opacity.
- Optional badge top-right: `badge-new`.
- Card heights are uniform (~360–400px); the row scrolls horizontally on mobile.

**`ai-product-matrix`** — 4-column grid of white product tiles below the vibrant matrix (Agent / Hailuo Video / Audio / Video).
- Each tile is `ai-product-tile` chrome.
- Top: 100px-tall illustration zone (often line-art icon or 3D mark).
- Below: title in `{typography.card-title}`, description in `{typography.body-sm}` `{colors.steel}`.

**`docs-prose-block`** — Documentation main content area.
- Max-width ~720px, centered. Body in `{typography.body-md}` `{colors.charcoal}` line-height 1.6.
- Inline code in `{typography.body-md}` monospace fallback with `{colors.surface}` background and `{rounded.xs}` corners.

**`models-comparison-table`** — Documentation table comparing model sizes and features.
- Uses `data-table` chrome. Each row carries a model name (linkified, in `{colors.ink}` body-sm-medium), a description column (`{colors.charcoal}`), and a features bullet list column.

**`testimonial-stat-row`** — Stats strip ("214,000+ Enterprise Clients & Developers", "0+ Countries Served").
- Horizontal row of 4 stat cells, each cell with a large number in `{typography.heading-lg}` `{colors.ink}` and a label below in `{typography.body-sm}` `{colors.steel}`.

**`footer-region`** — Dense black-canvas multi-column footer.
- Background `{colors.footer-bg}`, padding `{spacing.section} {spacing.xxl}`.
- Top row: MiniMax wordmark ("intelligence with everyone" tagline) and social icons (X, Twitter, GitHub, etc.).
- Body: 4-column link grid (Research / Product / API / Company / News).
- Section headers in `{typography.body-sm-medium}` `{colors.on-dark}`.

**`footer-link`** — Individual link entry inside the footer column.
- Background transparent, text `{colors.muted}`, typography `{typography.body-sm}`, padding `{spacing.xxs} 0`. Active/visited states do not change color — only opacity shifts on activation.

## Motion & Animation

This motion system is **prescribed** to match the brand's visual identity and was
not measured from the live site — no timing function or duration below was
extracted from minimax.io. MiniMax carries the **Crisp** profile: a developer
platform whose documentation, API surfaces and platform console make state change
read as instant, with no entrance choreography. The vibrant product cards are the
one place the brand invites a little travel, and even there it stays under 220ms.

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

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill button, nav link, table row) | `{motion.duration-instant}` | `{motion.ease-standard}` | `background-color`, `opacity` | Unchanged — colour and opacity only, no travel to remove |
| Press (pill button, product card) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.99)` | Scale removed; the fill step alone marks the press |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring | Ring appears instantly at full opacity, never animated |
| Page / route transition (docs navigation) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` only | Opacity cross-fade at `{motion.duration-reduced}` |
| Modal / drawer (mobile nav drawer, dialogs) | `{motion.duration-slow}` in, `{motion.duration-base}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `transform: translateX/translateY`, `opacity` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Dropdown (account menu, version picker) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: scale(0.98 → 1)` | Scale removed; opacity fade at `{motion.duration-reduced}` |
| Toast (copy-to-clipboard, API-key confirmations) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: translateY(8px → 0)` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| List enter (product matrix tiles, docs search results) | `{motion.duration-base}`, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px → 0)` | Stagger and travel removed; a single opacity fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform: translateY(0 → 4px)` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Loading (spinner in `button-primary-loading`, skeleton rows) | 800ms spinner rotation, 1200ms skeleton sweep, both infinite while pending | linear spinner, `{motion.ease-standard}` sweep | `transform: rotate`, `opacity` | Both frozen; a static spinner glyph and a flat skeleton fill remain |

### Rules

- Animate `transform` and `opacity` only. Never `width`, `height`, `top`, `left`
  or `margin` — the 4-column product matrix and the 3-column docs grid both
  reflow on resize, and animating layout properties there would cost frames.
- Every exit is shorter than its matching entrance: 100ms against 150ms for
  dropdowns, toasts and route changes, 150ms against 220ms for the drawer.
- Nothing animates on first paint. The 80px hero display and the product matrix
  render at full opacity immediately; no reveal delays content.
- The only infinite animations are the loading spinner and the skeleton sweep.
  MiniMax ships no brand ambience, so none is specified here.
- The focus ring never animates in. It is drawn at full opacity on the frame the
  control takes focus.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate, all scale, the 20ms list stagger. */
  /* Frozen: the loading spinner's rotation and the skeleton sweep. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (100ms). */
  *, *::before, *::after {
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;
    transition-property: opacity, background-color, border-color, color !important;
  }
}
```

Hover and press keep their colour steps, since those are not motion. The
focus-visible ring is unaffected: it never animated in the first place.

## Accessibility

Contrast measured with the WCAG 2.1 relative-luminance formula. Every ratio below
was computed from this file's own hexes, not estimated.

### Measured key pairs — passing

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 19.80:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface}` | 18.63:1 | 4.5:1 | Pass |
| `{colors.charcoal}` on `{colors.canvas}` | 15.91:1 | 4.5:1 | Pass |
| `{colors.slate}` on `{colors.canvas}` | 8.10:1 | 4.5:1 | Pass |
| `{colors.steel}` on `{colors.canvas}` | 6.39:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 19.80:1 | 4.5:1 | Pass |
| `{colors.muted}` on `{colors.footer-bg}` (`footer-link`) | 8.54:1 | 4.5:1 | Pass |
| `{colors.muted-strong}` on `{colors.canvas}` | 4.86:1 | 4.5:1 | Pass (prescribed) |
| `{colors.hairline-strong}` on `{colors.canvas}` | 4.29:1 | 3.0:1 | Pass (prescribed) |
| `{colors.hairline-strong}` on `{colors.surface}` | 4.04:1 | 3.0:1 | Pass (prescribed) |
| `{colors.success-text-strong}` on `{colors.success-bg}` | 5.08:1 | 4.5:1 | Pass (prescribed) |
| `{colors.brand-blue-deep}` on `{colors.brand-blue-200}` (`badge-beta`, `badge-code`) | 4.72:1 | 4.5:1 | Pass |

### Where the real brand fails AA — disclosed, not fixed

These are extracted values. They are frozen because falsifying a brand hex would
make the document wrong; each one is stated here with its measured ratio so that
anyone building on this file knows what they are inheriting.

| Foreground / Background | Ratio | Required | Note |
|---|---|---|---|
| `hairline` `#e5e7eb` on `{colors.canvas}` | 1.24:1 | 3.0:1 | Fails. Decorative only from here on — section breaks and card edges that sit beside other cues. Controls use `{colors.hairline-strong}`. |
| `hairline-soft` `#eaecf0` on `{colors.canvas}` | 1.18:1 | 3.0:1 | Fails. Table-row rule and nav underline; decorative. |
| `hairline` on `{colors.surface}` | 1.17:1 | 3.0:1 | Fails. Same scope. |
| `hairline-soft` on `{colors.surface}` | 1.11:1 | 3.0:1 | Fails. Same scope. |
| `muted` `#a8aab2` on `{colors.canvas}` | 2.32:1 | 4.5:1 | Fails on light. This tone is built for the black footer, where it measures 8.54:1. On a light surface use `{colors.muted-strong}` (4.86:1). |
| `muted` on `{colors.surface}` | 2.18:1 | 4.5:1 | Fails. Same substitution. |
| `success-text` `#1ba673` on `{colors.canvas}` | 3.11:1 | 4.5:1 | Fails as body ink. It is a badge label on `{colors.success-bg}`, never body text on canvas. |
| `badge-success` — `success-text` on `success-bg` | 2.95:1 | 4.5:1 | Fails at 13px. The brand's real pairing. `badge-success-accessible` is the prescribed alternative at 5.08:1. |
| `success-bg` `#e8ffea` on `{colors.canvas}` | 1.05:1 | 4.5:1 | Not a real failure: `success-bg` is a fill, never an ink. Recorded here only because the harness measures every `success*` token as text on canvas — see the report's Shared issues. |
| `badge-new` — `{colors.on-dark}` on `{colors.brand-coral}` | 3.18:1 | 4.5:1 | Fails at 13px. Coral is the brand's signature signal colour and is not changed; see Needs approval in the audit report. |
| `promo-cta-card` — `{colors.on-dark}` on `{colors.brand-coral}` | 3.18:1 | 4.5:1 | Passes 3:1 for its own headline, which is 24px+; the embedded `button-tertiary` carries the accessible label. Any body copy added to this card at under 24px fails. |
| `product-card-coral` tagline — `{colors.on-dark}` at 80% opacity on `{colors.brand-coral}` | below 3.18:1 | 4.5:1 | Fails. The 14px tagline on the vibrant cards is the weakest text in the system; set it at full opacity and 18px+ bold, or move it off the coral card. |
| `product-card-magenta` wordmark — `{colors.on-dark}` on `{colors.brand-magenta}` | 3.06:1 | 3.0:1 large text | Passes only because the wordmark is 40px+. It has no margin: any 14–16px white text on magenta fails. |

### Focus ring visibility, surface by surface

Two rings, because the brand ships both a white canvas and black/saturated
signature surfaces. Both are drawn **outside** the control at a 2px offset with a
2px stroke, so each is measured against the surface behind the control rather than
against the control's own fill — which is what WCAG 2.2 Focus Appearance asks for.

| Ring | Drawn on | Ratio | Required |
|---|---|---|---|
| `{colors.focus}` | `{colors.canvas}` | 5.80:1 | 3.0:1 |
| `{colors.focus}` | `{colors.surface}` | 5.46:1 | 3.0:1 |
| `{colors.focus}` | `{colors.surface-soft}` | 5.23:1 | 3.0:1 |
| `{colors.focus-on-dark}` | `{colors.footer-bg}` / `{colors.primary}` | 19.80:1 | 3.0:1 |
| `{colors.focus-on-dark}` | `{colors.brand-blue}` | 5.80:1 | 3.0:1 |
| `{colors.focus-on-dark}` | `{colors.brand-purple}` | 3.96:1 | 3.0:1 |
| `{colors.focus-on-dark}` | `{colors.brand-coral}` | 3.18:1 | 3.0:1 |
| `{colors.focus-on-dark}` | `{colors.brand-magenta}` | 3.06:1 | 3.0:1 |
| `{colors.focus-on-dark}` + 1px `{colors.ink-strong}` outer edge | `product-card-photo` (photography, no measurable ground) | bands separate at 21.0:1 | 3.0:1 |

The ring radius follows its control: `{rounded.full}` on pills and badges,
`{rounded.md}` on inputs, `{rounded.hero}` on product cards.

### Minimum tap target

- Pill buttons: 38–40px effective height on desktop, raised to 44px on mobile by
  padding override. The 38px desktop value is below the 44×44px that WCAG 2.5.5
  AAA asks for; it clears the 24×24px of 2.5.8 AA.
- Circular icon buttons: 36×36px desktop, 44×44px mobile.
- Form inputs and the search pill: 40px and 36px desktop, both 44px mobile.
- Sidebar nav items: ~32px desktop, 44px in the mobile drawer.
- Badges are not interactive, so no target applies.

### Reduced motion

Every travel and scale listed in Motion & Animation is removed under
`@media (prefers-reduced-motion: reduce)`; opacity fades remain, capped at
`{motion.duration-reduced}` (100ms); the loading spinner and skeleton sweep
freeze. MiniMax ships no brand ambience, so there is none to freeze.

### Not measurable from this document

Overlap, horizontal overflow, clipping, rendered tap-target size, frame rate and
layout shift need a running page. Nothing above claims them.

## Do's and Don'ts

### Do
- Use `{colors.primary}` (black) as the dominant CTA — it's the brand's most recognizable interactive element.
- Reserve product brand colors (`{colors.brand-coral}`, `{colors.brand-magenta}`, `{colors.brand-blue}`, `{colors.brand-purple}`) ONLY for product-identity moments — never for general buttons or text.
- Pair `{rounded.hero}` (32px) gradient cards with `{rounded.xl}` (16px) white cards in the same viewport — the radius contrast is the visual signature.
- Apply `{rounded.full}` to every button, every pill tab, every badge.
- Use `{typography.hero-display}` (80px) with -2px letter-spacing for hero displays — never compromise the leading or letter-spacing.
- Treat each model/product line as a distinct color identity. M2.7 is coral, Music is magenta, Hailuo is blue. These are brand assignments, not free choices.

### Don't
- Don't use brand-coral or brand-magenta on body text or large surfaces — they lose meaning when overused.
- Don't soften corners on buttons (anything less than `{rounded.full}`); the pill is a brand signature.
- Don't introduce a second display typeface; DM Sans handles every role.
- Don't reduce hero leading below 1.10 — the brand needs that breathing room on the 80px display.
- Don't apply heavy shadows on white cards; flat-with-borders is the documentation default.
- Don't put gradient backgrounds on standard buttons; gradients are reserved for product-card identity moments.
- Don't set 14px white text on `{colors.brand-coral}` or `{colors.brand-magenta}`; white clears only 3.18:1 and 3.06:1 there, so it is for 24px+ type only.
- Don't use `{colors.hairline}` as a control's only boundary; that job belongs to `{colors.hairline-strong}`.
- Don't animate `width`, `height`, `top`, `left` or `margin` — never on the product matrix or the docs grid. `transform` and `opacity` only.
- Don't let any entrance run longer than `{motion.duration-slow}` (220ms); MiniMax is a Crisp brand and a slow reveal reads as a different company.

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile (small) | < 480px | Single column. Hero drops to 40px. Pill nav collapses to hamburger. Product matrix horizontal-scroll. Footer 1-column accordion. |
| Mobile (large) | 480 – 767px | Same as small but AI product matrix renders 2-up. |
| Tablet | 768 – 1023px | 2-column AI product matrix. Pill-tab nav returns. Documentation sidebar collapses to drawer. |
| Desktop | 1024 – 1279px | Full 4-column product matrix; 3-column docs grid (sidebar / body / TOC). |
| Wide Desktop | ≥ 1280px | Wider hero gutters, larger product photography, fixed 220px sidebar. |

### Touch Targets
- Pill buttons render at 38–40px effective height — bumps to 44px on mobile via padding override.
- Circular icon buttons: 36×36px desktop → 44×44px on mobile.
- Form inputs render at 40px height; bumps to 44px on mobile.
- Sidebar nav items render at ~32px tall — bumps to 44px on mobile drawers.

### Collapsing Strategy
- **Promo banner** stays full-width; collapses to single line at < 480px with truncation.
- **Top nav** below 1024px collapses to hamburger; horizontal links move into drawer.
- **Documentation grid**: 3-column desktop → sidebar-drawer at < 1024px → single-column with collapsible sidebar at < 768px.
- **Product matrix**: 4-column desktop → horizontal-scroll at < 1024px (carousel-style with snap points).
- **AI Product Matrix**: 4-column → 2-column at tablet → 1-column at mobile.
- **Hero typography**: `{typography.hero-display}` (80px) → 56px at < 1024px → 40px at < 768px → 32px at < 480px.
- **Stats strip**: 4-column → 2×2 at < 768px → 1-column at < 480px.

### Image Behavior
- Product card imagery uses photographic content with internal gradient overlays; lazy-loaded below the fold.
- AI product tile illustrations are SVG-based; remain crisp at all breakpoints.
- Avatar imagery in testimonials uses 1:1 aspect ratio with `{rounded.full}` masking.

## Iteration Guide

1. Focus on ONE component at a time. The system has high internal consistency.
2. Reference component names and tokens directly (`{colors.primary}`, `{component-name}-pressed`, `{rounded.full}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits to catch broken refs and contrast issues.
4. Add new variants as separate `components:` entries (`-pressed`, `-disabled`, `-active`).
5. Default to `{typography.body-md}` for body and `{typography.subtitle}` for emphasis. Headlines step down `hero-display → display-lg → heading-lg → heading-md → heading-sm`.
6. Keep brand colors (coral, magenta, blue, purple) confined to product-card identity. If a brand color appears on a standard button or generic surface, ask whether it earned that surface.
7. Pill-shaped buttons (`{rounded.full}`) always; squared buttons signal "third-party widget" in this language.
8. Motion stays Crisp: reach for `{motion.duration-instant}` on hover and press, `{motion.duration-base}` for anything that enters, and `{motion.duration-fast}` for the matching exit. If an interaction needs more than `{motion.duration-slow}`, it is the wrong interaction for this brand.
9. Focus rings are not optional. Light surfaces take `{colors.focus}`, black and vibrant surfaces take `{colors.focus-on-dark}`, both at 2px with a 2px offset.

## Known Gaps

- Specific dark-mode token values (canvas, surface, ink, hairline) are not surfaced on these pages; the brand has not yet shipped a published dark-mode palette.
- Animation/transition timings are **not extracted**. The whole `motion:` group and the Motion & Animation section are prescribed from the Crisp profile to match the brand's tool-like identity; no duration or easing in this file was measured from minimax.io.
- Hover, focus-visible, loading and selected states were not observable in the static capture of the four source pages. Every entry marked "prescribed" in the State coverage table is an inference from the extracted default/pressed pair, not an extracted fact.
- The focus ring is prescribed. MiniMax publishes no focus treatment on these pages; `{colors.focus}` reuses the brand's own `{colors.brand-blue}` and `{colors.focus-on-dark}` is plain white, chosen to clear 3:1 on every surface this file defines rather than extracted from the site.
- `{colors.hairline-strong}`, `{colors.muted-strong}` and `{colors.success-text-strong}` are prescribed accessible parallels, not brand values. The extracted tones they sit beside are frozen and disclosed in Accessibility.
- `{rounded.xxl}` (20px) is defined in the extracted scale but no component in this file binds it; its "larger feature panels" use was observed without a specific component.
- Form validation success state is not explicitly captured beyond defaults — implement following standard green-border + success badge patterns.
- Code syntax highlighting palette inside docs is not formalized; documentation samples appear with system-default monospace and minimal coloring.
