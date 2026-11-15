---
version: alpha
name: Mintlify-design-analysis
description: Mintlify presents documentation infrastructure with a dual-mode aesthetic — atmospheric sky-gradient marketing heroes (cloud illustration backdrops, soft cream-to-blue washes) paired with dense developer-grade documentation surfaces. The system uses Inter for UI prose, Geist Mono for code, and a signature Mintlify green ({colors.brand-green}) reserved for accent CTAs and active states. Black-pill primary buttons dominate marketing, white-on-dark inversions appear on dark hero bands, and a 3-column documentation layout (sidebar / prose / TOC) anchors the developer experience. Coverage spans homepage, startups program, pricing comparison, and the live tabs documentation page.

colors:
  primary: "#0a0a0a"
  on-primary: "#ffffff"
  brand-green: "#00d4a4"
  brand-green-deep: "#00b48a"
  brand-green-soft: "#7cebcb"
  brand-tag: "#3772cf"
  brand-warn: "#c37d0d"
  brand-annotate: "#1ba673"
  brand-error: "#d45656"
  brand-cursor: "#888888"
  hero-sky-from: "#87a8c8"
  hero-sky-to: "#f5e9d8"
  hero-dark-from: "#1a3d4a"
  hero-dark-to: "#2d5a4f"
  testimonial-orange: "#f55a3c"
  testimonial-orange-deep: "#cc3a1f"
  canvas: "#ffffff"
  canvas-dark: "#0a0a0a"
  surface: "#f7f7f7"
  surface-soft: "#fafafa"
  surface-code: "#1c1c1e"
  hairline: "#e5e5e5"
  hairline-soft: "#ededed"
  hairline-dark: "#1f1f1f"
  hairline-strong: "#888888"
  ink: "#0a0a0a"
  charcoal: "#1c1c1e"
  slate: "#3a3a3c"
  steel: "#5a5a5c"
  stone: "#888888"
  muted: "#a8a8aa"
  on-dark: "#ffffff"
  on-dark-muted: "#b3b3b3"
  focus: "#005440"
  focus-on-dark: "#00d4a4"

typography:
  hero-display:
    fontFamily: Inter
    fontSize: 72px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -2px
  display-lg:
    fontFamily: Inter
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.5px
  heading-1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1px
  heading-2:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.5px
  heading-3:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
  heading-4:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.30
  heading-5:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 600
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
    lineHeight: 1.50
  body-md-medium:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
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
    letterSpacing: 0.5px
  button-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30
  code-md:
    fontFamily: Geist Mono
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
  code-sm:
    fontFamily: Geist Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.40
  code-inline:
    fontFamily: Geist Mono
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.30

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

shadow:
  none: "none"
  subtle: "rgba(0, 0, 0, 0.04) 0px 1px 2px 0px"
  card: "rgba(0, 0, 0, 0.08) 0px 4px 12px 0px"
  mockup: "rgba(0, 0, 0, 0.12) 0px 24px 48px -8px"
  brand-glow: "rgba(0, 212, 164, 0.08) 0px 8px 24px"

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
    padding: "10px 20px"
  button-primary-pressed:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
  button-accent-green:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
  button-on-dark:
    backgroundColor: "{colors.on-dark}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    border: "1px solid {colors.hairline}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "8px 12px"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-medium}"
    padding: "0"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 32px
    border: "1px solid {colors.hairline}"
  card-base:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  card-feature:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-help:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
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
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "2px solid {colors.brand-green}"
    shadow: "{shadow.brand-glow}"
  testimonial-card-feature:
    backgroundColor: "{colors.testimonial-orange}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.section}"
  testimonial-card-quote:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
    height: 40px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.brand-green}"
  focus-ring:
    border: "2px solid {colors.focus}"
    outlineOffset: "2px"
    rounded: "inherit"
  focus-ring-on-dark:
    border: "2px solid {colors.focus-on-dark}"
    outlineOffset: "2px"
    rounded: "inherit"
  search-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xs} {spacing.md}"
    height: 36px
    border: "1px solid {colors.hairline}"
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
  pill-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm-medium}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
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
  badge-discount:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-required:
    backgroundColor: "{colors.brand-error}"
    textColor: "{colors.on-dark}"
    typography: "{typography.micro-uppercase}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  badge-type:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.steel}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  badge-tag:
    backgroundColor: "rgba(55, 114, 207, 0.15)"
    textColor: "{colors.brand-tag}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  promo-banner:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm-medium}"
    padding: "{spacing.sm} {spacing.md}"
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
    border: "0 0 1px {colors.hairline-dark} solid"
  code-inline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.charcoal}"
    typography: "{typography.code-inline}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    border: "1px solid {colors.hairline}"
  property-row:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} 0"
    border: "0 0 1px {colors.hairline-soft} solid"
  feature-comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  feature-comparison-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.lg}"
    border: "0 0 1px {colors.hairline-soft} solid"
  sidebar-nav-item:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
  sidebar-nav-item-active:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-medium}"
  sidebar-section-header:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.micro-uppercase}"
    padding: "{spacing.md} {spacing.md} {spacing.xs}"
  doc-toc-item:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxs} 0"
  doc-toc-item-active:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-medium}"
  copy-code-button:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.xs}"
    border: "1px solid {colors.hairline-dark}"
  hero-band-sky:
    backgroundColor: "{colors.hero-sky-from}"
    textColor: "{colors.on-dark}"
    rounded: "0"
    padding: "{spacing.hero}"
  hero-band-dark:
    backgroundColor: "{colors.hero-dark-from}"
    textColor: "{colors.on-dark}"
    rounded: "0"
    padding: "{spacing.hero}"
  hero-product-mockup:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "0"
    border: "1px solid {colors.hairline-soft}"
    shadow: "{shadow.mockup}"
  logo-wall-item:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-md-medium}"
    padding: "{spacing.lg}"
  faq-accordion-item:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  footer-region:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
    border: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxs} 0"
  startup-program-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  founder-quote-card:
    backgroundColor: "{colors.testimonial-orange}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
---

## Overview

Mintlify positions itself at the intersection of polished marketing presentation and developer-grade documentation density. The home and startups pages open with cinematic atmospheric heroes — soft sky-gradient backdrops with cloud illustrations on the homepage, dark teal-to-mint gradients with a rocket launch on the startups page — that feel more like a SaaS landing aesthetic than a developer tool. Then the deeper surfaces (pricing comparison, live documentation pages) collapse into dense, high-information layouts where Inter body type carries 14–16px copy across long-form prose, syntax-highlighted code blocks, and 3-column documentation grids.

The brand's signature mint green ({colors.brand-green}) appears sparingly but decisively — on the hero "Get started" pill button, the green checkmark icons inside feature lists, the "Featured" pricing tier border, and active state indicators inside docs UI. Black-pill primary buttons dominate the marketing flow; white-on-dark inversions appear on dark hero bands. The signature pairing of Inter (body, headings) with Geist Mono (code blocks, inline references, type signatures) reinforces the developer-tool DNA without requiring a third typeface.

**Key Characteristics:**
- Atmospheric gradient hero bands (sky-blue to cream on homepage; teal-to-mint on startups) provide cinematic marketing presentation
- Signature Mintlify mint green ({colors.brand-green}) reserved for accent CTAs, active states, and feature confirmations
- Black-pill primary buttons ({colors.primary} + `{rounded.full}`) for marketing CTAs
- Inter for all UI prose; Geist Mono for code blocks, inline code, and type/property signatures
- 3-column documentation layout (sidebar / prose / TOC) with dense 14px body type for long-form developer reading
- Tightly-controlled radius scale: marketing uses `{rounded.lg}` (12px), pill buttons use `{rounded.full}` — no in-between corner softening
- Vibrant testimonial card (`{colors.testimonial-orange}`) breaks color rhythm intentionally for emotional impact

## Colors

> Source pages: mintlify.com/ (homepage), /startups (program page), /pricing (comparison), /docs/components/tabs (live documentation). Token coverage was identical across all four pages.

### Brand & Accent
- **Mintlify Mint** ({colors.brand-green}): Signature accent — used on hero "Get started" pill button, green checkmarks in feature lists, featured pricing tier border accent, sidebar active indicator dots.
- **Deep Mint** ({colors.brand-green-deep}): Pressed/active variant of the mint accent.
- **Soft Mint** ({colors.brand-green-soft}): Subtle background tint for success states and confirmation surfaces.
- **Brand Tag** ({colors.brand-tag}): Documentation tag and reference color (used in `<Tabs>` JSX-style annotations and code-tag chips).
- **Brand Annotate** ({colors.brand-annotate}): Inline code annotation green (used in twoslash code annotation system).
- **Brand Warn** ({colors.brand-warn}): Code warning highlight (deprecated, caution).
- **Brand Error** ({colors.brand-error}): Red used for required-field labels and error highlight.
- **Testimonial Orange** ({colors.testimonial-orange}): Warm coral-orange used on the "Cursor" testimonial card and warm callout surfaces.

### Surface
- **Canvas White** ({colors.canvas}): Primary page and card background.
- **Canvas Dark** ({colors.canvas-dark}): Promo banner, dark inversion surfaces, code editor wrapper.
- **Surface** ({colors.surface}): Subtle section backgrounds, search-pill rest, code-inline background, sidebar active state.
- **Surface Soft** ({colors.surface-soft}): Quieter section backgrounds and FAQ accordion.
- **Surface Code** ({colors.surface-code}): Dark code-block wrapper background.
- **Hairline** ({colors.hairline}): 1px borders and primary dividers.
- **Hairline Soft** ({colors.hairline-soft}): Quieter table-row dividers and secondary section breaks.
- **Hairline Strong** ({colors.hairline-strong}) — *prescribed, not extracted*: Parallel accessible boundary for any border that is a control's only visible edge (`text-input`, `search-pill`, `button-secondary`, `button-icon-circular`). It reuses the brand's own `{colors.stone}` grey, the lightest extracted grey that clears 3:1 on both `{colors.canvas}` and `{colors.surface}`. The extracted `{colors.hairline}` and `{colors.hairline-soft}` are retained unchanged and are scoped to decoration — section breaks, table-row rules, card edges that are not the sole affordance of a control.

### Focus
- **Focus** ({colors.focus}) — *prescribed, not extracted*: Deep mint focus ring for light grounds (`{colors.canvas}`, `{colors.surface}`, `{colors.surface-soft}`, and the sky-gradient hero band). Mintlify's live surfaces ship no accessible focus ring; the brand's own `{colors.brand-green}` sits at 1.92:1 on white, so the ring is darkened down the same mint hue rather than switched to a foreign colour.
- **Focus On Dark** ({colors.focus-on-dark}) — *prescribed, not extracted*: The brand mint itself, used as the ring on `{colors.canvas-dark}`, `{colors.surface-code}` and the dark teal hero band. The file documents both light and dark signature surfaces, so one ring cannot serve both.
- Both rings are drawn **outside** the control with a 2px offset (`focus-ring`, `focus-ring-on-dark`), so each is measured against the surface behind it, per WCAG 2.2 Focus Appearance.

### Hero Atmospheric
- **Hero Sky From / To** ({colors.hero-sky-from}, {colors.hero-sky-to}): Atmospheric sky-blue to soft cream gradient on the homepage hero.
- **Hero Dark From / To** ({colors.hero-dark-from}, {colors.hero-dark-to}): Dark teal to mint gradient on the startups hero.

### Text
- **Ink** ({colors.ink}): Primary headlines and CTA text.
- **Charcoal** ({colors.charcoal}): Body text, code-inline foreground.
- **Slate** ({colors.slate}): Secondary text and metadata.
- **Steel** ({colors.steel}): Tertiary text, table headers, sidebar inactive items, footer links.
- **Stone** ({colors.stone}): Captions, twoslash cursor color, muted labels.
- **Muted** ({colors.muted}): Disabled text and decorative de-emphasis only. At 2.37:1 on `{colors.canvas}` it fails AA for any text that must be read; WCAG sets no requirement on disabled controls, which is the one place it is safe. Secondary and tertiary copy that must be read uses `{colors.steel}` (6.88:1 on canvas) or `{colors.slate}` (11.35:1) instead.
- **On Dark** ({colors.on-dark}): White text on dark surfaces (hero bands, code blocks, promo banner).
- **On Dark Muted** ({colors.on-dark-muted}): Reduced-opacity white for code-block headers and metadata on dark.

### Semantic
- Error tones derive from `{colors.brand-error}` for input borders, required-field labels, and validation messaging.

## Typography

### Font Family
**Inter** (primary): Variable typeface optimized for UI legibility. Used across every UI surface — body, headings, navigation, button labels, captions. Fallbacks: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif.

**Geist Mono** (code): Monospace typeface used inside code blocks, inline code references, type signatures (e.g. `string`, `number`, `boolean`), and property names in API documentation. Fallbacks: 'SF Mono', Menlo, Consolas, 'Geist Mono Fallback', monospace.

The brand uses no italic variants of either face — emphasis comes from weight (500/600), color shift, or background highlighting (in code references).

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 72px | 600 | 1.05 | -2px | Marketing hero display ("The intelligent Knowledge Platform") |
| `{typography.display-lg}` | 56px | 600 | 1.10 | -1.5px | Major section opener ("Built for the intelligence age") |
| `{typography.heading-1}` | 48px | 600 | 1.10 | -1px | Page-level headlines ("Pricing on your terms") |
| `{typography.heading-2}` | 36px | 600 | 1.20 | -0.5px | Section headlines ("Apply to the Mintlify startup program") |
| `{typography.heading-3}` | 28px | 600 | 1.25 | 0 | Subsection headers, "Tabs" docs page title |
| `{typography.heading-4}` | 22px | 600 | 1.30 | 0 | Card titles, larger feature headers |
| `{typography.heading-5}` | 18px | 600 | 1.40 | 0 | Smaller feature headers, FAQ question titles |
| `{typography.subtitle}` | 18px | 400 | 1.50 | 0 | Hero subtitle, lead body |
| `{typography.body-md}` | 16px | 400 | 1.50 | 0 | Primary body text |
| `{typography.body-md-medium}` | 16px | 500 | 1.50 | 0 | Body emphasis |
| `{typography.body-sm}` | 14px | 400 | 1.50 | 0 | Secondary body, table cells, navigation |
| `{typography.body-sm-medium}` | 14px | 500 | 1.50 | 0 | Active sidebar nav, button labels, tab labels |
| `{typography.caption}` | 13px | 400 | 1.40 | 0 | Helper text, fine print, code-block headers |
| `{typography.caption-bold}` | 13px | 600 | 1.40 | 0 | Badge labels |
| `{typography.micro}` | 12px | 500 | 1.40 | 0 | Footer microcopy, label chips |
| `{typography.micro-uppercase}` | 11px | 600 | 1.40 | 0.5px | Sidebar section headers, "REQUIRED" labels |
| `{typography.button-md}` | 14px | 500 | 1.30 | 0 | Pill button labels |
| `{typography.code-md}` | 14px | 400 | 1.50 | 0 | Code block content |
| `{typography.code-sm}` | 13px | 400 | 1.40 | 0 | Smaller code, type signatures |
| `{typography.code-inline}` | 13px | 500 | 1.30 | 0 | Inline `<Tabs>` references in body |

### Principles
- **Tight hero leading** (1.05) creates magazine-grade display headlines on the 72px hero
- **Negative letter-spacing** progresses inversely with size — display sizes use -2px to -1.5px; smaller headings relax to 0
- **Documentation-grade body** (1.50 line-height on 14–16px) ensures comfortable long-form reading in dense docs surfaces
- **Inter / Geist Mono pairing** — Inter for everything else, Geist Mono surgically for code references; the contrast between the two is the brand's developer-respect signal
- **Uppercase micro labels** with +0.5px letter-spacing carry sidebar section headers and "REQUIRED" annotation tags

## Layout

### Spacing System
- **Base unit**: 4px (8px primary increment)
- **Tokens**: `{spacing.xxs}` (4px) · `{spacing.xs}` (8px) · `{spacing.sm}` (12px) · `{spacing.md}` (16px) · `{spacing.lg}` (20px) · `{spacing.xl}` (24px) · `{spacing.xxl}` (32px) · `{spacing.xxxl}` (40px) · `{spacing.section-sm}` (48px) · `{spacing.section}` (64px) · `{spacing.section-lg}` (96px) · `{spacing.hero}` (120px)
- **Section rhythm**: Marketing pages use `{spacing.section-lg}` (96px) between major bands; pricing comparison tightens to `{spacing.section}` (64px); documentation surfaces use `{spacing.xxl}` (32px) between subsections
- **Card internal padding**: Standard `{spacing.xl}` (24px) for compact cards; `{spacing.xxl}` (32px) for pricing cards and feature panels; testimonial card pushes to `{spacing.section}` (64px) for hero-card presence

### Grid & Container
- Marketing pages use a 1280px max-width with 32px gutters
- Hero and feature bands often use 2-column splits (text left, illustration/mockup right)
- Pricing page renders 3 tier cards in a row at desktop (FREE / Lift Off / Custom), then a comprehensive feature comparison table below
- Documentation pages use a strict 3-column grid: left sidebar nav (~240px), center prose (~720px max-width), right TOC (~200px)
- Logo walls use 6-up rows of customer logos at 80–100px height each

### Whitespace Philosophy
Marketing surfaces give content generous breathing room — `{spacing.hero}` (120px) above-the-fold creates space for atmospheric gradient backdrops to read clearly. Documentation tightens dramatically: section gaps drop to `{spacing.xxl}` (32px), table rows pack to `{spacing.md}` (16px), sidebar nav compresses to `{spacing.xs}` (8px) vertical rhythm.

## Elevation & Depth

The system runs predominantly flat with strategic atmospheric depth.

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | `{shadow.none}`; `{colors.hairline}` border | Default cards, table rows, form inputs |
| 1 (subtle) | `{shadow.subtle}` — `rgba(0, 0, 0, 0.04) 0px 1px 2px 0px` | Hover-elevated tiles, subtle highlights |
| 2 (card) | `{shadow.card}` — `rgba(0, 0, 0, 0.08) 0px 4px 12px 0px` | Standard feature cards |
| 3 (mockup) | `{shadow.mockup}` — `rgba(0, 0, 0, 0.12) 0px 24px 48px -8px` | Hero product mockup framing — the deep diffuse drop on the homepage hero docs preview |
| 4 (brand-tinted) | `{shadow.brand-glow}` — `rgba(0, 212, 164, 0.08) 0px 8px 24px` | Featured pricing tier glow |

Elevation is expressed one way per level and the two are not mixed arbitrarily: levels 0–2 carry a `{colors.hairline}` border and no shadow or a shadow and no border, never both as competing boundaries. Level 3 is the single exception and says so — the hero mockup carries a `{colors.hairline-soft}` edge *and* `{shadow.mockup}`, because the mockup is a screenshot frame that needs a crisp edge against the gradient as well as separation from it.

### Decorative Depth
- The homepage hero uses an atmospheric photographic backdrop (cloud illustration on sky-gradient) for depth — no shadow needed; the imagery does the work
- The startups hero uses a similar treatment with a rocket-launch illustration cutting across the dark teal gradient
- Code blocks carry their own internal depth via syntax-highlighting color hierarchy on the dark surface; no shadow used

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Inline code chips, micro tags |
| `{rounded.sm}` | 6px | Sidebar nav items, type badges |
| `{rounded.md}` | 8px | Inputs, search pill, code blocks, secondary cards |
| `{rounded.lg}` | 12px | Standard cards, pricing tiers, hero mockup, FAQ items |
| `{rounded.xl}` | 16px | Larger feature panels |
| `{rounded.xxl}` | 24px | Featured product showcase tiles |
| `{rounded.full}` | 9999px | All buttons, pill tabs, badges |

The radius scale is tightly disciplined — the brand never uses a corner softening between `{rounded.md}` (8px) and `{rounded.lg}` (12px) for the same component family. Pill buttons (`{rounded.full}`) are used universally; rectangular cards use `{rounded.lg}` (12px) consistently.

### Photography Geometry
- Hero illustrations (cloud, rocket) sit on full-bleed gradient backdrops with no internal framing
- Customer logo walls use 1:1 ratio cells without rounding (logos are presented inline as wordmarks)
- Testimonial photos use 1:1 aspect with `{rounded.md}` (8px) softening
- Code editor mockup hero image uses `{rounded.lg}` (12px) corners on a hairline-bordered card with a deep diffuse drop shadow

## Components

> The earlier revision of this file carried a "no-hover policy" and documented default and pressed/active states only. That policy is withdrawn: it was a documentation convention, not an observed property of the brand, and it left every interactive component without a hover or focus-visible state. States are now named per entry below.

### Component States

Every component entry names the states it supports. `default` is implied everywhere and omitted from the list. Non-interactive surfaces that genuinely have one state say so.

| Component | States |
|---|---|
| `button-primary` | hover (lifts to `{colors.charcoal}`), focus-visible (`focus-ring`), active/pressed (`button-primary-pressed`), disabled (`button-primary-disabled`), loading (label swaps for a spinner, width held) |
| `button-accent-green` | hover (`{colors.brand-green-deep}`), focus-visible, active/pressed, disabled, loading |
| `button-on-dark` | hover (opacity shift), focus-visible (`focus-ring-on-dark`), active/pressed, disabled |
| `button-secondary` | hover (border to `{colors.hairline-strong}`), focus-visible, active/pressed, disabled |
| `button-ghost` | hover (`{colors.surface}` fill), focus-visible, active/pressed, disabled |
| `button-link` | hover (underline), focus-visible, active/pressed |
| `button-icon-circular` | hover (`{colors.surface}` fill), focus-visible, active/pressed, disabled |
| `text-input` | hover (border to `{colors.hairline-strong}`), focus-visible (`text-input-focused` + `focus-ring`), disabled, error (`{colors.brand-error}` border), loading (async validation spinner in the trailing slot) |
| `search-pill` | hover, focus-visible, active/pressed, loading (results pending) |
| `segmented-tab` | hover (text to `{colors.ink}`), focus-visible, selected (`segmented-tab-active`), disabled |
| `pill-tab` | hover, focus-visible, selected (`pill-tab-active`), disabled |
| `toggle-monthly-yearly` | hover, focus-visible, selected (thumb position) — two selectable positions only, no error or loading state |
| `faq-accordion-item` | hover (header only), focus-visible, selected (expanded) |
| `sidebar-nav-item` | hover (`{colors.surface}` fill), focus-visible, selected (`sidebar-nav-item-active`) |
| `doc-toc-item` | hover, focus-visible, selected (`doc-toc-item-active`, scroll-spy driven) |
| `copy-code-button` | hover, focus-visible, active/pressed, loading (brief "Copied" confirmation) |
| `footer-link` | hover (text to `{colors.ink}`), focus-visible |
| `logo-wall-item` | single state — a static wordmark, not interactive |
| `badge-discount`, `badge-required`, `badge-type`, `badge-tag` | single state each — static labels, not interactive |
| `card-base`, `card-feature`, `card-help`, `card-startup-perk`, `startup-program-card` | default and hover (`{shadow.subtle}`) where the whole card is a link; single state where it is not |
| `pricing-card`, `pricing-card-featured` | single state — the card is a container; its CTA carries the states |
| `testimonial-card-feature`, `testimonial-card-quote`, `founder-quote-card` | single state each — quote, portrait and attribution only, no interactive control, so no focus ring is drawn on the orange ground |
| `code-block`, `code-block-header`, `code-inline` | single state — static containers; `copy-code-button` inside the header carries the states |
| `property-row`, `feature-comparison-table`, `feature-comparison-row` | single state each — documentation tables, not interactive |
| `promo-banner` | default and a dismiss control that carries hover, focus-visible and active/pressed |
| `hero-band-sky`, `hero-band-dark`, `hero-product-mockup` | single state each — layout bands |

### Buttons

**`button-primary`** — Black pill primary CTA, the dominant action across all surfaces.
- Background `{colors.primary}`, text `{colors.on-primary}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.full}`.
- Pressed state `button-primary-pressed` lifts to `{colors.charcoal}`.
- Disabled state `button-primary-disabled` uses `{colors.hairline}` background and `{colors.muted}` text.

**`button-accent-green`** — Mint green pill for brand-emphasis CTAs (hero "Get started", featured pricing CTA).
- Background `{colors.brand-green}`, text `{colors.primary}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.full}`.

**`button-on-dark`** — White pill for use on dark hero bands (startups page "Get started").
- Background `{colors.on-dark}`, text `{colors.primary}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.full}`.

**`button-secondary`** — Outlined pill for secondary actions.
- Background transparent, text `{colors.ink}`, border `1px solid {colors.hairline}`, typography `{typography.button-md}`, padding `10px 20px`, rounded `{rounded.full}`.

**`button-ghost`** — Quieter rectangular ghost button (sidebar action, tertiary nav).
- Background transparent, text `{colors.ink}`, typography `{typography.button-md}`, padding `8px 12px`, rounded `{rounded.md}`.

**`button-link`** — Inline text link styled as a subtle button.
- Background transparent, text `{colors.ink}`, typography `{typography.body-sm-medium}`, padding `0`. Underline appears on activation.

**`button-icon-circular`** — 32×32px circular utility button (close, copy, arrow).
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline}`, rounded `{rounded.full}`.

### Cards & Containers

**`card-base`** — Standard documentation/feature card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`card-feature`** — Feature panel on light gray surface.
- Background `{colors.surface}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`.

**`card-help`** — "Need help?" CTA cards below the pricing comparison ("Quickstart guide", "Guide to technical writing", "Founder", "Sales").
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`.

**`card-startup-perk`** — Startup-program perk grid item ("Discounts and credits", "Priority support", "Startup pack", "Founder community").
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}`, border `1px solid {colors.hairline}`. Carries an icon at top, heading `{typography.heading-5}`, description `{typography.body-sm}` `{colors.steel}`.

**`pricing-card`** — Standard pricing tier card.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.
- Title `{typography.heading-3}`, price `{typography.display-lg}`, feature list `{typography.body-sm}` with green checkmark icons.

**`pricing-card-featured`** — Highlighted pricing tier (Lift Off / featured plan).
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `2px solid {colors.brand-green}`, soft brand-tinted shadow `rgba(0, 212, 164, 0.08) 0px 8px 24px`.

**`testimonial-card-feature`** — Bright orange large testimonial card with photo + quote ("Cursor — Every YC batch we consistently see the top performing startups use Mintlify to build their docs.").
- Background `{colors.testimonial-orange}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding `{spacing.section}`. Photo on right, large quote in `{typography.heading-3}` left, attribution below in `{typography.body-sm-medium}`.

**`testimonial-card-quote`** — Smaller white testimonial card on the startups page.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

**`founder-quote-card`** — Cursor founder testimonial card variant on the orange surface.
- Background `{colors.testimonial-orange}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`. Carries the specific founder portrait + quote treatment.

**`startup-program-card`** — Larger application/program card containing perks grid + apply CTA.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xxl}`, border `1px solid {colors.hairline}`.

### Inputs & Forms

**`text-input`** — Standard text field.
- Background `{colors.canvas}`, text `{colors.ink}`, border `1px solid {colors.hairline}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, height 40px.

**`text-input-focused`** — Activated state.
- Border switches to `2px solid {colors.brand-green}` — focus uses the brand mint as the activation signal.

**`search-pill`** — Documentation top-bar search.
- Background `{colors.surface}`, text `{colors.steel}`, typography `{typography.body-sm}`, rounded `{rounded.md}`, height 36px, border `1px solid {colors.hairline}`.

### Tabs

**`segmented-tab`** + **`segmented-tab-active`** — Underline-style tab navigation (used inside docs Tabs component for "First tab / Second tab / Third tab").
- Inactive: text `{colors.steel}`, transparent background, padding `{spacing.sm} {spacing.md}`. Active: text `{colors.ink}`, 2px bottom border in `{colors.ink}`.

**`pill-tab`** + **`pill-tab-active`** — Pill-style tab nav (top of pricing page: "Pricing / Roadmap").
- Inactive: background `{colors.canvas}`, text `{colors.steel}`, border `1px solid {colors.hairline}`, padding `8px 16px`, rounded `{rounded.full}`.
- Active: background `{colors.primary}`, text `{colors.on-primary}`, no border.

**`toggle-monthly-yearly`** — Two-state pill toggle (Monthly / Annual on pricing page).
- Background `{colors.surface}`, rounded `{rounded.full}`, padding `4px`. Active state moves a white pill thumb to the selected position.

### Badges & Status

**`badge-discount`** — Small green "Save 20%" badge attached to annual toggle.
- Background `{colors.brand-green}`, text `{colors.primary}`, typography `{typography.caption-bold}`, rounded `{rounded.full}`, padding `2px 8px`.

**`badge-required`** — Red "REQUIRED" label on documentation property rows.
- Background `{colors.brand-error}`, text `{colors.on-dark}`, typography `{typography.micro-uppercase}`, rounded `{rounded.sm}`, padding `2px 6px`.

**`badge-type`** — Type signature chip in documentation (e.g. `string`, `number`, `boolean`).
- Background `{colors.surface}`, text `{colors.steel}`, typography `{typography.code-sm}`, rounded `{rounded.sm}`, padding `2px 6px`.

**`badge-tag`** — Documentation tag chip (e.g. `<Tabs>` reference highlighted in body text).
- Background `rgba(55, 114, 207, 0.15)`, text `{colors.brand-tag}`, typography `{typography.caption-bold}`, rounded `{rounded.sm}`, padding `2px 8px`.

**`promo-banner`** — Sticky black promo strip ABOVE the top nav (when present).
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, typography `{typography.body-sm-medium}`, padding `{spacing.sm} {spacing.md}`.

### Code

**`code-block`** — Syntax-highlighted code container.
- Background `{colors.surface-code}`, text `{colors.on-dark}`, typography `{typography.code-md}`, rounded `{rounded.md}`, padding `{spacing.md}`.

**`code-block-header`** — Header bar above the code with language label + copy button.
- Background `{colors.surface-code}`, text `{colors.on-dark-muted}`, typography `{typography.caption}`, padding `{spacing.xs} {spacing.md}`, bottom border `1px solid {colors.hairline-dark}`.

**`code-inline`** — Inline `<Tabs>` reference in body prose.
- Background `{colors.surface}`, text `{colors.charcoal}`, typography `{typography.code-inline}`, rounded `{rounded.xs}`, padding `2px 6px`, border `1px solid {colors.hairline}`.

**`copy-code-button`** — "Copy code" button in code-block header.
- Background transparent, text `{colors.on-dark-muted}`, typography `{typography.caption}`, rounded `{rounded.sm}`, padding `{spacing.xxs} {spacing.xs}`, border `1px solid {colors.hairline-dark}`.

### Documentation Components

**`property-row`** — API property documentation row (e.g. `defaultIndex` on the Tabs page).
- Background transparent, text `{colors.ink}`, typography `{typography.body-sm}`, padding `{spacing.md} 0`, bottom border `1px solid {colors.hairline-soft}`.
- Layout: property name in `{typography.code-inline}` + type badge + optional REQUIRED badge + description below in `{typography.body-sm}` `{colors.steel}`.

**`feature-comparison-table`** — Detailed pricing-page feature comparison table.
- Background `{colors.canvas}`, text `{colors.ink}`, typography `{typography.body-sm}`, rounded `{rounded.md}`, border `1px solid {colors.hairline}`.

**`feature-comparison-row`** — Individual row inside the comparison table.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.lg}`, bottom border `1px solid {colors.hairline-soft}`. Section dividers in `{typography.micro-uppercase}` `{colors.steel}`.

**`sidebar-nav-item`** + **`sidebar-nav-item-active`** — Documentation left rail link entries.
- Inactive: background transparent, text `{colors.steel}`, typography `{typography.body-sm}`, rounded `{rounded.sm}`, padding `{spacing.xs} {spacing.md}`.
- Active: background `{colors.surface}`, text `{colors.ink}`, typography `{typography.body-sm-medium}`.

**`sidebar-section-header`** — Uppercase section header inside sidebar (e.g. "COMPONENTS", "PRIMITIVES").
- Background transparent, text `{colors.steel}`, typography `{typography.micro-uppercase}`, padding `{spacing.md} {spacing.md} {spacing.xs}`.

**`doc-toc-item`** + **`doc-toc-item-active`** — Right-rail table-of-contents links.
- Inactive: background transparent, text `{colors.steel}`, typography `{typography.body-sm}`, padding `{spacing.xxs} 0`.
- Active: text `{colors.ink}`, typography `{typography.body-sm-medium}`, optional left-border accent in `{colors.brand-green}`.

### Navigation

**Top Navigation (Marketing)** — Sticky white bar with logo, link list, and right-side CTAs.
- Background `{colors.canvas}`, height ~64px, bottom border `1px solid {colors.hairline-soft}`.
- Left: Mintlify wordmark + horizontal link list (Solutions, Pricing, Customers, Documentation, Changelog).
- Right: secondary "Talk to sales" + black-pill "Get Started".

**Top Navigation (Documentation)** — Compressed nav with center search-pill and right-side account/upgrade CTAs.
- Background `{colors.canvas}`, height ~56px. Search-pill at center, "Documentation / Guides / API Reference / Changelog" links + "Talk to us" + green "Get started" right.

### Signature Components

**`hero-band-sky`** — Homepage hero with atmospheric sky-blue to cream gradient and cloud illustrations.
- Background gradient `linear-gradient(180deg, {colors.hero-sky-from} 0%, {colors.hero-sky-to} 100%)`, text `{colors.on-dark}` (early portion of gradient) shifting to `{colors.ink}` further down, padding `{spacing.hero}`.
- Layout: centered hero headline in `{typography.hero-display}`, centered subtitle in `{typography.subtitle}`, centered button row (`button-accent-green` "Get started" + `button-secondary` "Talk to us"), product mockup below the buttons.

**`hero-band-dark`** — Startups hero with dark teal-to-mint gradient and rocket launch illustration.
- Background gradient `linear-gradient(135deg, {colors.hero-dark-from} 0%, {colors.hero-dark-to} 100%)`, text `{colors.on-dark}`, padding `{spacing.hero}`.
- Layout: hero headline left in `{typography.hero-display}` `{colors.on-dark}`, illustration right (rocket cutting across the gradient), button row uses `button-on-dark` (white pill) + ghost link.

**`hero-product-mockup`** — Code-editor mockup framed inside the homepage hero.
- Background `{colors.canvas}`, rounded `{rounded.lg}`, border `1px solid {colors.hairline-soft}`, deep shadow `rgba(0, 0, 0, 0.12) 0px 24px 48px -8px`.
- Carries a documentation page preview inside (sidebar on left, prose body, mock UI controls).

**`logo-wall-item`** — Customer logo cell in 6-up trust-row grids ("Anthropic / Cognition / Mintlify / Vercel / react / Lovable", "Stripe / Block / PayPal / Compound / Auth").
- Background transparent, text `{colors.steel}`, typography `{typography.body-md-medium}`, padding `{spacing.lg}`.
- Logos rendered as wordmarks with consistent vertical centering.

**`faq-accordion-item`** — Frequently-asked-questions panel item (visible on pricing page).
- Background `{colors.canvas}`, rounded `{rounded.md}`, padding `{spacing.xl}`, border `1px solid {colors.hairline-soft}`.
- Question in `{typography.heading-5}`, expanded answer in `{typography.body-md}` `{colors.steel}`, chevron icon in `{colors.steel}` 16px.

**`footer-region`** — Multi-column site footer.
- Background `{colors.canvas}`, top border `1px solid {colors.hairline}`, padding `{spacing.section} {spacing.xxl}`.
- 5 column groups (Explore / Resources / Company / Legal + brand mark column).
- Section headers in `{typography.body-sm-medium}` `{colors.ink}`, link items in `{typography.body-sm}` `{colors.steel}`.

**`footer-link`** — Individual link entry in the footer.
- Background transparent, text `{colors.steel}`, typography `{typography.body-sm}`, padding `{spacing.xxs} 0`.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or choreography below was extracted from mintlify.com; the values are the shared **Crisp** profile, assigned because Mintlify's identity is a developer tool — terminal-adjacent code surfaces, a 3-column docs grid, Geist Mono type signatures, scroll-spy TOC — and a tool's state change should read as instant rather than performed. The atmospheric marketing heroes are the brand's only non-tool register, and they are static imagery, not animation.

### Interaction Table

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, nav items, cards, links) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, and `transform: translateY(-1px)` on link-wrapped cards only | Travel removed; opacity cross-fade at `{motion.duration-reduced}` |
| Press (pill buttons, copy button, tabs) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)`, `opacity` | Scale removed; colour/opacity change applied at `{motion.duration-reduced}` |
| Focus (`focus-ring`, `focus-ring-on-dark`) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` only — the ring never scales or travels in, so keyboard position is never ambiguous | Unchanged; already opacity-only and under 150ms |
| Page / route transition (docs page to docs page) | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` on the prose column only; sidebar and TOC do not re-enter | Opacity-only at `{motion.duration-reduced}`; no cross-fade overlap |
| Modal / drawer (mobile nav drawer, contact dialog) | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `transform: translateX(-100%) → 0` for the drawer, `transform: scale(0.98) → 1` plus `opacity` for the dialog; scrim `opacity` | Travel and scale removed; scrim and panel fade at `{motion.duration-reduced}` |
| Dropdown (nav flyout, version picker, language select) | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(-4px) → 0` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Toast ("Copied", "Link copied") | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(8px) → 0` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| List enter (sidebar group expand, search results, pricing feature rows) | `{motion.duration-fast}` per item, `{motion.stagger-step}` between items, capped at 8 items | `{motion.ease-enter}` | `opacity`, `transform: translateY(4px) → 0` | Stagger and travel removed; the whole list fades in once at `{motion.duration-reduced}` |
| List exit (sidebar group collapse, search results clearing) | `{motion.duration-instant}`, no stagger | `{motion.ease-exit}` | `opacity` | Unchanged; already opacity-only and under 150ms |
| Loading (search pending, async validation, docs skeleton) | spinner 800ms linear, infinite; skeleton shimmer 1200ms linear, infinite | linear | spinner `transform: rotate()`; skeleton `opacity` pulse between 0.4 and 1 | Both infinite animations frozen; a static spinner glyph and a flat skeleton block at 0.7 opacity remain, with the loading state still announced to assistive technology |

### Rules

- Animate `transform` and `opacity` only — never `width`, `height`, `top`, `left` or `margin`. The 3-column docs grid and the comparison table are the two places where a layout-property transition would cost a frame budget this brand cannot spare.
- Every exit is shorter than its matching entrance: drawer `{motion.duration-fast}` out against `{motion.duration-base}` in, dropdown and toast `{motion.duration-instant}` out against `{motion.duration-fast}` in.
- Nothing animates on first paint. The hero headline, the product mockup and the docs prose are painted in place; there is no entrance choreography, which is the Crisp signature.
- `{motion.duration-emphasis}` (300ms) is reserved for the mobile nav drawer at full travel and is the longest duration in the system. `{motion.duration-slow}` (220ms) covers the pricing toggle thumb when the Monthly/Annual switch also re-renders the three tier cards.
- The only infinite animations are the two loaders above. This brand has no ambient motion — no drifting cloud illustration, no gradient shimmer on the hero band; the atmospheric heroes are static.
- The mint accent never animates its hue. `{colors.brand-green}` appears or does not; a colour-interpolated accent reads as a marketing flourish and contradicts the tool register.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translateX, translateY) and all scale, on every
     interaction in the table above — hover lift, press scale, drawer slide,
     dropdown and toast rise, list-enter stagger. */
  /* Removed: the {motion.stagger-step} delay chain; lists appear at once. */
  /* Frozen: both infinite loaders. The spinner holds a static glyph and the
     skeleton holds a flat block; the loading state is still announced. */
  /* Kept: opacity fades only, every one clamped to {motion.duration-reduced}
     (100ms), which is already under the 150ms ceiling. */
  /* Kept: the focus ring, at full strength and with no transition at all —
     reduced motion never costs a keyboard user their position. */
  *, *::before, *::after {
    transition-property: opacity !important;
    transition-duration: 100ms !important;  /* {motion.duration-reduced} */
    animation-play-state: paused !important;
    transform: none !important;
  }
}
```

## Accessibility

Every ratio below was computed with WCAG 2.1 relative luminance against this file's own frontmatter hexes. Where the real brand fails, the failure is stated rather than corrected — the extracted hexes are frozen facts about Mintlify, not defects in this document.

### Measured Contrast — Passing

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 19.80:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface}` | 18.48:1 | 4.5:1 | Pass |
| `{colors.charcoal}` on `{colors.surface}` | 15.88:1 | 4.5:1 | Pass |
| `{colors.slate}` on `{colors.canvas}` | 11.35:1 | 4.5:1 | Pass |
| `{colors.steel}` on `{colors.canvas}` | 6.88:1 | 4.5:1 | Pass |
| `{colors.steel}` on `{colors.surface}` | 6.42:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 19.80:1 | 4.5:1 | Pass |
| `{colors.primary}` on `{colors.brand-green}` | 10.33:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.surface-code}` | 17.01:1 | 4.5:1 | Pass |
| `{colors.on-dark-muted}` on `{colors.surface-code}` | 8.11:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.hero-dark-from}` | 11.60:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.hero-dark-to}` | 7.82:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 3.54:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.surface}` | 3.31:1 | 3.0:1 | Pass |

### Measured Contrast — Real Failures, Disclosed

These are extracted brand values. They are recorded here, not changed.

| Foreground / Background | Ratio | Required | Note |
|---|---|---|---|
| `{colors.hairline-soft}` on `{colors.surface}` | 1.09:1 | 3.0:1 | Fails. Decorative divider only; a control's sole boundary uses `{colors.hairline-strong}`. |
| `{colors.hairline-soft}` on `{colors.canvas}` | 1.17:1 | 3.0:1 | Fails. Same scoping — table-row rules and nav underline, never a control edge. |
| `{colors.hairline}` on `{colors.surface}` | 1.18:1 | 3.0:1 | Fails. Card and section edges only. |
| `{colors.hairline}` on `{colors.canvas}` | 1.26:1 | 3.0:1 | Fails. This is the brand's real hairline, and it is the only visible boundary of `text-input`, `search-pill`, `button-secondary` and `button-icon-circular` on the live site. **Mintlify genuinely fails WCAG 1.4.11 for non-text contrast at those controls.** `{colors.hairline-strong}` is the prescribed replacement. |
| `{colors.muted}` on `{colors.surface}` | 2.22:1 | 4.5:1 | Fails. Scoped to disabled text, which WCAG exempts, and to decorative de-emphasis. |
| `{colors.muted}` on `{colors.canvas}` | 2.37:1 | 4.5:1 | Fails. Same scoping; readable secondary copy uses `{colors.steel}`. |
| `{colors.on-dark}` on `{colors.testimonial-orange}` — `testimonial-card-feature` | 3.28:1 | 4.5:1 | Fails. The quote renders at `{typography.heading-3}` (28px), so 3:1 applies to the quote itself and it passes there; the `{typography.body-sm-medium}` attribution line beneath it needs 4.5:1 and fails. |
| `{colors.on-dark}` on `{colors.testimonial-orange}` — `founder-quote-card` | 3.28:1 | 4.5:1 | Fails, same pair, smaller card. Its body copy is `{typography.body-sm}`, so nothing on this card clears 4.5:1. |
| `{colors.on-dark}` on `{colors.brand-error}` — `badge-required` | 3.99:1 | 4.5:1 | Fails. The label is `{typography.micro-uppercase}` (11px/600), nowhere near large text, so 4.5:1 applies. |
| `{colors.on-dark}` on `{colors.hero-sky-from}` — `hero-band-sky` | 2.48:1 | 4.5:1 | Fails, and fails the 3:1 large-text threshold too even at `{typography.hero-display}` (72px). On the live page the headline shifts to `{colors.ink}` as the gradient lightens, and `{colors.ink}` on `{colors.hero-sky-from}` measures 7.98:1 — but white-on-sky is what the top of the band renders, and it is not readable. |
| `{colors.stone}` on `{colors.canvas}` | 3.54:1 | 4.5:1 | Fails as body or caption text. The harness does not flag it, because `stone` matches no text-dim pattern, but the prose assigns it to captions and muted labels. It clears the 3:1 large-text threshold only at 24px+, and no caption role in this file is that large — `{typography.caption}` is 13px. Use `{colors.steel}` for any caption that must be read. |
| `{colors.on-dark-muted}` on `{colors.canvas}` — `copy-code-button` | 2.10:1 | 4.5:1 | Fails **as measured against the canvas**, which is not where this control lives. `copy-code-button` has a transparent fill inside `code-block-header`, so its real ground is `{colors.surface-code}`, where the same ink measures 8.11:1 and passes. The 2.10:1 figure is a harness fallback, logged under Shared issues in the audit report. |

### Focus Ring Visibility

Both rings are prescribed; Mintlify ships no accessible focus ring. They are drawn outside the control with a 2px offset, so each is measured against the surface behind it.

| Ring | Surface it is drawn on | Ratio | Required | Result |
|---|---|---|---|---|
| `{colors.focus}` | `{colors.canvas}` | 8.97:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.surface}` | 8.37:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.surface-soft}` | 8.59:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.hero-sky-from}` | 3.61:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.hero-sky-to}` | 7.48:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` | `{colors.canvas-dark}` | 10.33:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` | `{colors.surface-code}` | 8.87:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` | `{colors.hero-dark-from}` | 6.05:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` | `{colors.hero-dark-to}` | 4.08:1 | 3.0:1 | Pass |

`{colors.testimonial-orange}` is a third polarity and no single ring reaches 3:1 on it — `{colors.focus}` measures 1.52:1 there and `{colors.focus-on-dark}` 1.71:1. No third ring is invented, because the orange cards carry a quote, a portrait and an attribution line and no interactive control; nothing on them can take focus. If an interactive element is ever added to that surface, it needs its own ring stated here.

The brand's own activation signal, `text-input-focused`'s `2px solid {colors.brand-green}` border, measures **1.92:1** against `{colors.canvas}` and fails 1.4.11 outright. It is kept as the extracted fact and the prescribed `focus-ring` is layered outside it, so the green reads as the brand's input-active colour while the ring does the accessibility work.

### Tap Targets

The minimum interactive target in this system is 44×44px. The file's `## Responsive Behavior` section records the extracted desktop sizes that sit below it — 32px circular icon buttons, ~32px sidebar nav rows, 36px search pill, 36–40px pill buttons — and the mobile padding overrides that bring each to 44px. Whether the rendered page actually honours those overrides is not verifiable from this document; no page was rendered for this audit.

### Reduced Motion

Every prescribed interaction has a `prefers-reduced-motion: reduce` behaviour, tabulated above and expressed as a CSS rule in `## Motion & Animation`. All travel and scale are removed, both infinite loaders freeze while still announcing the loading state, and opacity fades are clamped to `{motion.duration-reduced}` (100ms). The focus ring is exempt: it stays at full strength with no transition.

### Not Verifiable Here

This is a document, not a running page. Overlap, horizontal overflow, clipping, real tap-target geometry, frame rate and layout shift were not and cannot be measured from it. Keyboard tab order, screen-reader labelling and the live dark-mode palette are likewise unverified — see `## Known Gaps`.

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
| `{colors.hairline-dark}` (`#1f1f1f`) on `{colors.canvas-dark}` (`#0a0a0a`) | 1.20:1 | 3.0:1 | Fail — boundary, dark theme |
| best ring `{colors.focus}` (`#005440`) against `{colors.testimonial-orange}` (`#f55a3c`) | 2.74:1 | 3.0:1 | Fail — no focus ring this file declares reaches 3:1 on that surface |

## Do's and Don'ts

### Do
- Reserve `{colors.brand-green}` (Mintlify mint) for accent CTAs and active state indicators only — even one accent button per viewport carries weight
- Use `{colors.primary}` (black) as the dominant CTA on light backgrounds; switch to `button-on-dark` (white pill) on dark hero bands
- Apply `{rounded.full}` to every button and pill; never soften pill corners
- Pair Inter (UI prose) with Geist Mono (code) — never introduce a third typeface
- Use atmospheric gradient hero bands sparingly (only the homepage and startups page); keep deeper surfaces flat and dense
- Apply `{rounded.lg}` (12px) consistently on cards; use `{rounded.md}` (8px) only on compact UI like search pills and code blocks
- Keep documentation prose at `{typography.body-md}` (16px) with 1.50 line-height — never compress
- Keep state changes at `{motion.duration-fast}` or faster; this is a tool, and a tool's response should read as instant
- Draw `focus-ring` on light grounds and `focus-ring-on-dark` on `{colors.canvas-dark}`, `{colors.surface-code}` and the dark hero band, always outside the control with a 2px offset
- Use `{colors.hairline-strong}` wherever a border is a control's only visible edge; keep `{colors.hairline}` and `{colors.hairline-soft}` for decoration

### Don't
- Don't use `{colors.brand-green}` on body text or large surfaces — it loses signal
- Don't introduce additional accent colors beyond mint, tag-blue, error-red, and the testimonial orange
- Don't apply heavy shadows on flat documentation cards; reserve elevation for the hero product mockup
- Don't reduce documentation line-height below 1.50 — long-form readability suffers
- Don't combine atmospheric gradients with multiple competing color accents in the same hero — the sky/dark gradient is the brand mood; let it breathe
- Don't use Inter for code or Geist Mono for prose — the typeface assignment IS the brand voice
- Don't add entrance choreography to the hero, the product mockup or the docs prose — nothing in this system animates on first paint
- Don't animate `width`, `height`, `top`, `left` or `margin`; `transform` and `opacity` carry every transition
- Don't rely on `{colors.brand-green}` alone to signal focus — at 1.92:1 on `{colors.canvas}` it is a brand cue, not an accessible indicator
- Don't set readable secondary copy in `{colors.muted}` — it fails AA on every light surface this file defines

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile (small) | < 480px | Single column. Hero scales to 36px. Pill nav collapses to hamburger. Pricing tiers stack 1-up. Footer 1-column accordion. |
| Mobile (large) | 480 – 767px | Same as small but feature tiles render 2-up. Hero scales to 44px. |
| Tablet | 768 – 1023px | 2-column feature grids. Pill-tab nav returns. Documentation sidebar collapses to drawer. Hero scales to 56px. |
| Desktop | 1024 – 1279px | Full 3-column docs grid (sidebar / body / TOC). 3-tier pricing card row. Hero at 72px. |
| Wide Desktop | ≥ 1280px | Wider hero gutters, larger product mockup, fixed 240px sidebar. |

### Touch Targets
- Pill buttons render at 36–40px effective height — bumps to 44px on mobile via padding override
- Circular icon buttons: 32×32px desktop → 44×44px mobile
- Form inputs render at 40px height; bumps to 44px mobile
- Sidebar nav items render at ~32px tall — bump to 44px mobile drawers

### Collapsing Strategy
- **Promo banner** stays full-width; truncates at < 480px
- **Top nav** below 1024px collapses to hamburger; horizontal links move into drawer
- **Hero band**: 2-column hero (text + mockup) collapses to stacked at < 1024px; mockup rendered below text on mobile
- **Documentation grid**: 3-column desktop → sidebar-drawer at < 1024px → single-column at < 768px
- **Pricing comparison**: 3-column tiers → 1-column stacked at < 768px; comparison table becomes horizontal-scroll
- **Hero typography**: `{typography.hero-display}` (72px) → 56px tablet → 44px mobile-large → 36px mobile-small
- **Customer logo wall**: 6-up → 3-up at tablet → 2-up at mobile
- **Footer**: 5-column desktop → 2-column tablet → accordion at mobile

### Image Behavior
- Hero illustrations (cloud, rocket) lazy-load with the hero band; remain crisp at all breakpoints (SVG-based)
- Product mockup retains its aspect ratio across breakpoints; scales proportionally
- Customer logos use SVG wordmarks; remain crisp on retina displays

## Iteration Guide

1. Focus on ONE component at a time. The system has high internal consistency.
2. Reference component names and tokens directly (`{colors.primary}`, `{component-name}-pressed`, `{rounded.full}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits to catch broken refs and contrast issues.
4. Add new variants as separate `components:` entries (`-pressed`, `-disabled`, `-focused`, `-active`).
5. Default to `{typography.body-md}` for body and `{typography.subtitle}` for emphasis. Headlines step down `hero-display → display-lg → heading-1 → heading-2 → heading-3 → heading-4 → heading-5`.
6. Keep `{colors.brand-green}` confined to accent moments. If it appears on a generic surface, ask whether it earned that role.
7. Pill-shaped buttons (`{rounded.full}`) always; squared buttons signal "third-party widget" in this language.
8. Documentation prose belongs in `{typography.body-md}` 16px with 1.50 line-height — anything denser breaks the reading experience.

## Known Gaps

- Specific dark-mode token values for canvas, surface, ink, and hairline are not surfaced on these pages; the brand has not yet shipped a published dark-mode palette
- Animation and transition timings are not extracted from the live site. The `motion:` group and the whole `## Motion & Animation` section are the prescribed **Crisp** profile, assigned from the brand's developer-tool identity, and are labelled as prescribed wherever they appear
- Focus ring values (`{colors.focus}`, `{colors.focus-on-dark}`) and `{colors.hairline-strong}` are prescribed, not extracted. Mintlify's live surfaces ship no accessible focus ring and no accessible control boundary; the brand's own signals for both (`{colors.brand-green}` at 1.92:1, `{colors.hairline}` at 1.26:1) fail WCAG 1.4.11
- Keyboard tab order, visible-label association and screen-reader naming are not observable from these four pages
- Form validation success state is not explicitly captured beyond defaults — implement following standard green-border + success badge patterns
- Code syntax highlighting palette inside docs is not formalized; documentation samples carry their own twoslash-style annotation system tokens (e.g. `{colors.brand-tag}`, `{colors.brand-annotate}`, `{colors.brand-warn}`) but the full highlight scheme is not enumerated
