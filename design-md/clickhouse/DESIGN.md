---
version: alpha
name: ClickHouse-design-analysis
description: A high-performance database interface anchored on near-pure black canvas with electric yellow as the brand voltage. White typography in confident sans, yellow CTAs, and yellow-text stat numbers carry the brand voice across every page. Code blocks and product UI fragments embed directly in dark cards. The yellow + black pairing (and yellow used scarcely as accent) is the system's signature — brand identity without atmospheric decoration.

colors:
  primary: "#faff69"
  primary-active: "#e6eb52"
  primary-disabled: "#3a3a1f"
  ink: "#ffffff"
  body: "#cccccc"
  body-strong: "#e6e6e6"
  muted: "#888888"
  muted-soft: "#5a5a5a"
  hairline: "#2a2a2a"
  hairline-strong: "#3a3a3a"
  border-control: "#6e6e6e"
  focus: "#7a7f10"
  canvas: "#0a0a0a"
  surface-soft: "#121212"
  surface-card: "#1a1a1a"
  surface-elevated: "#242424"
  surface-yellow-band: "#faff69"
  on-primary: "#0a0a0a"
  on-dark: "#ffffff"
  on-yellow: "#0a0a0a"
  accent-emerald: "#22c55e"
  accent-rose: "#ef4444"
  accent-blue: "#3b82f6"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"

typography:
  display-xl:
    fontFamily: "Inter, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -2.5px
  display-lg:
    fontFamily: "Inter, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -2px
  display-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1.5px
  display-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -1px
  title-lg:
    fontFamily: "Inter, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  stat-display:
    fontFamily: "Inter, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1.5px
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.5px
  code:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  button:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

motion:
  duration-instant: 60ms
  duration-fast: 100ms
  duration-base: 150ms
  duration-slow: 220ms
  duration-emphasis: 320ms
  ease-standard: cubic-bezier(0.2, 0, 0, 1)
  ease-enter: cubic-bezier(0, 0, 0.1, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 20ms

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  pill: 9999px
  full: 9999px

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
    padding: 12px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 40px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
  button-icon-circular:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    size: 36px
  text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 96px
  hero-stat-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.stat-display}"
  feature-card-yellow:
    backgroundColor: "{colors.surface-yellow-band}"
    textColor: "{colors.on-yellow}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  feature-card-dark:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  code-window-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: 24px
  product-mockup-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  pricing-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-card-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  stat-callout:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.stat-display}"
  cta-band-yellow:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.lg}"
    padding: 64px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    borderColor: "{colors.border-control}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    height: 40px
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.focus}"
    rounded: "{rounded.md}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.error}"
    rounded: "{rounded.md}"
  focus-ring:
    borderColor: "{colors.focus}"
    width: 2px
    offset: 2px
    rounded: "{rounded.md}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  category-tab-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
  badge-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-yellow:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  events-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  customer-logo-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    padding: 32px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 64px
---

## Overview

ClickHouse's marketing surface is the highest-contrast interface in the database / data-platform category. The base atmosphere is **near-pure black canvas** (`{colors.canvas}` — #0a0a0a) with **electric yellow** (`{colors.primary}` — #faff69) as the singular brand voltage. The yellow handles every primary CTA, every stat-callout number, every "GET STARTED" badge — used scarcely on individual elements but generously on full-bleed yellow CTA cards. White typography in confident weight-700 sans-serif anchors the editorial body.

The yellow + black pairing is what makes ClickHouse instantly recognizable. Where Snowflake uses cool blue gradients and Databricks uses red + slate, ClickHouse leans hard into one electric yellow that does all the brand work. Code blocks, terminal output, and product UI fragments embed directly in dark `{colors.surface-card}` (#1a1a1a) cards across every page.

Type voice runs **Inter** at confident weights — 700 for display headlines (with negative letter-spacing -1 to -2.5px), 600 for sub-titles and buttons, 400 for body. The system has no display-serif counter-voice; everything is one geometric humanist sans, scaled and weighted for hierarchy.

**Key Characteristics:**
- Near-pure black canvas (`{colors.canvas}` — #0a0a0a) with white type. The system has no light-mode marketing surface.
- Electric yellow primary (`{colors.primary}` — #faff69). Used on primary CTAs, large stat-callout numbers ("2.8k+", "74k+"), and full-bleed yellow CTA bands.
- Inter at weight 700 for display, weight 600 for sub-titles + buttons, weight 400 for body. No serif counterpoint.
- Dark surface cards (`{colors.surface-card}` — #1a1a1a) for feature cards, code windows, and product mockups. Cards barely lighter than canvas — color-block contrast is subtle.
- Code blocks render in JetBrains Mono inside `{colors.surface-card}`. SQL syntax-highlighted in muted blues / yellows / grays.
- Stat numbers in yellow + sans-700 + huge size carry the credibility moment ("779+", "2.8k+", "47k+" community / contributor / star counts).
- Border radius is hierarchical: `{rounded.md}` (8px) for buttons, `{rounded.lg}` (12px) for content cards. No pill except in tag badges.
- Section rhythm `{spacing.section}` (96px) between major editorial bands.

## Colors

### Brand & Accent
- **Primary (Electric Yellow)** (`{colors.primary}` — #faff69): The signature brand color. All primary CTA backgrounds, large stat-callout numbers, full-bleed yellow CTA cards. The yellow is the brand.
- **Primary Active** (`{colors.primary-active}` — #e6eb52): Press / hover-darker variant.
- **Primary Disabled** (`{colors.primary-disabled}` — #3a3a1f): Desaturated dark-yellow on dark canvas.

### Surface
- **Canvas** (`{colors.canvas}` — #0a0a0a): The default page floor. Near-pure black.
- **Surface Soft** (`{colors.surface-soft}` — #121212): Section dividers, very-soft band tints.
- **Surface Card** (`{colors.surface-card}` — #1a1a1a): Feature cards, code windows, product mockups, pricing tier cards.
- **Surface Elevated** (`{colors.surface-elevated}` — #242424): Nested cards inside larger dark cards.
- **Surface Yellow Band** (`{colors.surface-yellow-band}` — #faff69): The yellow CTA card / band fill — same hex as primary.
- **Hairline** (`{colors.hairline}` — #2a2a2a): 1px borders on cards.
- **Hairline Strong** (`{colors.hairline-strong}` — #3a3a3a): Heavier divider on input underlines and emphasis.

**Both hairlines are decoration only, and the real brand fails AA here.** `{colors.hairline}` measures 1.38:1 on `{colors.canvas}` and `{colors.hairline-strong}` measures 1.74:1 — both far below the 3:1 a component boundary needs. These are the extracted values and they stay as they are. Where a hairline is the *only* boundary of an interactive control (a text input, a tab well, a focusable card), use the prescribed token below instead.

- **Border Control** (`{colors.border-control}` — #6e6e6e): **Prescribed, not extracted.** The accessible boundary for interactive controls. Measures 3.88:1 on `{colors.canvas}`, 3.67:1 on `{colors.surface-soft}`, 3.41:1 on `{colors.surface-card}` and 3.04:1 on `{colors.surface-elevated}` — clears 3:1 on every surface this file defines.
- **Focus** (`{colors.focus}` — #7a7f10): **Prescribed, not extracted.** The focus ring: `{colors.primary}` driven down into the one luminance band that clears 3:1 against *both* the black surface family and the yellow bands. Measures 4.59:1 on `{colors.canvas}`, 4.35:1 on `{colors.surface-soft}`, 4.04:1 on `{colors.surface-card}`, 3.60:1 on `{colors.surface-elevated}` and 4.02:1 on `{colors.primary}`. One ring serves the whole system, so there is no second `focus-on-dark` token. The obvious alternative — ringing in full `{colors.primary}` — reaches 18.45:1 on the canvas but collapses to 1.00:1 on a yellow CTA band, so it is not the default.

### Text
- **Ink / On Dark** (`{colors.on-dark}` — #ffffff): All headline and primary text.
- **Body** (`{colors.body}` — #cccccc): Default running-text color.
- **Body Strong** (`{colors.body-strong}` — #e6e6e6): Emphasized paragraphs.
- **Muted** (`{colors.muted}` — #888888): Footer links, captions, breadcrumbs.
- **Muted Soft** (`{colors.muted-soft}` — #5a5a5a): Tertiary text — fine print.
- **On Primary / On Yellow** (`{colors.on-primary}` / `{colors.on-yellow}` — #0a0a0a): Black text on yellow CTAs and yellow CTA bands. The high-contrast yellow + black combo is the brand action signal.

### Semantic / Accent
- **Accent Emerald** (`{colors.accent-emerald}` — #22c55e): Success states, "active" status indicators in product UI.
- **Accent Rose** (`{colors.accent-rose}` — #ef4444): Error states, "down" indicators.
- **Accent Blue** (`{colors.accent-blue}` — #3b82f6): Info states, code-syntax highlighting.

## Typography

### Font Family
The system runs **Inter** for everything — display, body, navigation, buttons, captions. **JetBrains Mono** handles code blocks. The fallback stack walks `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.

The single-family approach is deliberate: Inter at weight 700 + 600 + 400 covers the entire hierarchy without needing a serif or display counter-voice. The geometric humanist character of Inter at confident bold weight gives ClickHouse a precise, engineered feel that matches the database's performance-first positioning.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 72px | 700 | 1.05 | -2.5px | Homepage h1 ("The leading database for AI") |
| `{typography.display-lg}` | 56px | 700 | 1.1 | -2px | Section heads |
| `{typography.display-md}` | 40px | 700 | 1.15 | -1.5px | Sub-section heads, CTA-band heads |
| `{typography.display-sm}` | 32px | 700 | 1.2 | -1px | Card titles, pricing tier prices |
| `{typography.title-lg}` | 24px | 700 | 1.3 | -0.3px | Pricing plan names, larger feature titles |
| `{typography.title-md}` | 18px | 600 | 1.4 | 0 | Card titles, intro paragraphs |
| `{typography.title-sm}` | 16px | 600 | 1.4 | 0 | Small card titles, list labels |
| `{typography.stat-display}` | 56px | 700 | 1.0 | -1.5px | Stat callouts ("779+", "47k+") — ALWAYS yellow |
| `{typography.body-md}` | 16px | 400 | 1.55 | 0 | Default running-text |
| `{typography.body-sm}` | 14px | 400 | 1.55 | 0 | Footer body, fine-print |
| `{typography.caption}` | 13px | 500 | 1.4 | 0 | Badge labels, captions |
| `{typography.caption-uppercase}` | 12px | 600 | 1.4 | 1.5px | Section labels, "NEW" badges |
| `{typography.code}` | 14px | 400 | 1.55 | 0 | Code blocks — JetBrains Mono |
| `{typography.button}` | 14px | 600 | 1.0 | 0 | Standard button labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Top-nav menu items |

### Principles
Display weights stay at 700 across all sizes. Negative letter-spacing (-1 to -2.5px) is essential — Inter at weight 700 without negative tracking reads as too wide / Apple-marketing. The tightened tracking gives ClickHouse the precise, engineered feel.

Body and labels stay at weights 400 / 500 / 600. The hierarchy is built on size + weight, not on family contrast.

### Note on Font Substitutes
Inter is open-source and the documented choice. **Söhne** is a close commercial alternative if licensed. **Geist** is another modern alternative.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- **Section padding:** `{spacing.section}` (96px) between major bands.
- **Card internal padding:** `{spacing.xl}` (32px) for feature cards, pricing tiers; `{spacing.lg}` (24px) for code-window cards and event cards.

### Grid & Container
- **Max content width:** ~1280px centered.
- **Editorial body:** Single 12-column grid; hero often uses 7/5 split (h1 left, code mockup right).
- **Feature card grids:** 3-up at desktop, 2-up at tablet, 1-up at mobile.
- **Pricing grid:** 3-4 up at desktop, 1-up at mobile.

### Whitespace Philosophy
ClickHouse uses dense, slightly-compressed whitespace appropriate for a developer-tooling brand — generous enough to read editorially, tight enough to feel "engineering-grade" rather than "marketing-soft." Section rhythm at 96px is standard; card internal padding stays at 32px for feature cards.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body sections, top nav, hero |
| Soft hairline | 1px `{colors.hairline}` border | Code-window cards, content cards |
| Surface card | `{colors.surface-card}` background — no shadow | Feature cards, pricing tiers, event cards |
| Yellow band | `{colors.primary}` background — no shadow | Full-bleed yellow CTA cards / bands |

The system uses no drop shadows. Depth comes from the contrast between black canvas and `{colors.surface-card}` (a barely-lighter-than-canvas tone) — the contrast is subtle, more like an "engineering-grade dim panel" than an "elevated card."

**Measured layer separation.** `{colors.surface-soft}` on `{colors.canvas}` is 1.06:1, `{colors.surface-card}` on `{colors.canvas}` is 1.14:1, and `{colors.surface-elevated}` on `{colors.surface-card}` is 1.12:1. Those are the extracted values: the layers are *nearly indistinguishable* as fills, which is a deliberate part of the brand's flat, dim-panel look but means fill alone cannot carry elevation. Elevation is therefore expressed one way throughout — **tone plus an optional 1px hairline**, never shadow — and any card that must read as a distinct, bounded object (an interactive card, an input, a tab well) takes a 1px `{colors.border-control}` boundary rather than relying on the 1.14:1 fill step.

### Decorative Depth
- Code-window cards carry their own internal product chrome — line numbers, syntax highlighting, status bars at the bottom — adding visual density without external shadows.
- The yellow-on-black contrast does most of the elevation work for CTAs.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Reserved for badge accents |
| `{rounded.sm}` | 6px | Small inline buttons |
| `{rounded.md}` | 8px | Standard CTA buttons, text inputs |
| `{rounded.lg}` | 12px | Content cards, code-window cards, pricing tiers |
| `{rounded.pill}` | 9999px | Badge pills |
| `{rounded.full}` | 9999px / 50% | Avatars, icon buttons |

Both `{rounded.pill}` and `{rounded.full}` carry 9999px; they are kept separate because they mean different things (pill labels versus circular icon buttons and avatars), not because the values differ. Nothing sits outside the 4 · 6 · 8 · 12 ladder.

### Border Widths

| Width | Token drawn in | Use |
|---|---|---|
| 1px | `{colors.hairline}` | Decorative card edges and dividers |
| 1px | `{colors.border-control}` | Boundaries of interactive controls — inputs, tab wells, focusable cards |
| 2px | `{colors.focus}` | Focus ring only |

### Focus Ring Geometry

`{component.focus-ring}` is a 2px `{colors.focus}` ring at 2px offset, following the host element's own radius — `{rounded.md}` on buttons and inputs, `{rounded.lg}` on cards, `{rounded.pill}` on badges, `{rounded.full}` on `{component.button-icon-circular}`. The ring is never drawn inside the element, so it never shifts text.

## Components

### Top Navigation

**`top-nav`** — Black nav bar pinned to top. 64px tall, `{colors.canvas}` background. Carries the ClickHouse logo + wordmark at left, primary horizontal menu (Product, Use Cases, Pricing, Resources, Customers) center-left, right-side cluster with "Sign in" + "Get Started" `{component.button-primary}` (yellow). Menu items in `{typography.nav-link}` (Inter 14px / 500).

### Buttons

**`button-primary`** — The signature yellow CTA. Background `{colors.primary}` (#faff69), text `{colors.on-primary}` (black), type `{typography.button}` (Inter 14px / 600), padding 12px × 20px, height 40px, rounded `{rounded.md}` (8px). The yellow + black combination is iconic.

**`button-secondary`** — Dark surface card button. Background `{colors.surface-card}`, text `{colors.on-dark}`, same shape as primary.

**`button-text-link`** — Inline text button, no background. Used for "Sign in" and inline link CTAs.

**`text-link`** — Inline body links in `{colors.primary}` (yellow on dark). Underlined.

**`button-icon-circular`** — 36 × 36 circular icon button on dark.

### Cards & Containers

**`hero-band`** — Black-canvas hero with 7-5 grid: h1 + sub-headline + button row on the left, code-window or product mockup on the right. Vertical padding `{spacing.section}` (96px).

**`hero-stat-card`** — Yellow stat-display numbers ("779+", "47k+") inline on the canvas. No card surface — just yellow text in `{typography.stat-display}` (56px / 700).

**`feature-card-yellow`** — Full-bleed yellow card ("Built for every modern data challenge"). Background `{colors.primary}`, text `{colors.on-yellow}` (black), rounded `{rounded.lg}` (12px), padding `{spacing.xl}` (32px). The yellow card IS the visual emphasis.

**`feature-card-dark`** — Standard dark feature card. Background `{colors.surface-card}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding `{spacing.xl}` (32px).

**`code-window-card`** — Dark card showing a SQL code block. Background `{colors.surface-card}`, code in JetBrains Mono with syntax highlighting, rounded `{rounded.lg}`, padding `{spacing.lg}` (24px). Often the hero's right-side artifact on developer-focused pages.

**`product-mockup-card`** — Card showing actual ClickHouse product UI (query editor, dashboard, monitoring panel). Same shape as `{component.feature-card-dark}` but with embedded product chrome inside.

**`pricing-tier-card`** — Standard tier card. Background `{colors.surface-card}`, rounded `{rounded.lg}`, padding `{spacing.xl}` (32px).

**`pricing-tier-card-featured`** — The featured tier flips to `{colors.primary}` (yellow). The yellow surface IS the featured signal.

**`stat-callout`** — Inline yellow stat numbers ("779+", "2.8k+", "47k+"). Transparent background, text `{colors.primary}`, type `{typography.stat-display}`. Used as a flat layout block, not a card with surface.

**`events-card`** — Used on /company/events. Dark card with event title, date in `{typography.caption-uppercase}`, location, and a "Register" CTA. Rounded `{rounded.lg}`, padding `{spacing.lg}`.

**`customer-logo-strip`** — Horizontal monochrome customer-logo strip. Background `{colors.canvas}`, logos in `{colors.muted}`, vertical padding `{spacing.xl}` (32px).

### Inputs & Forms

**`text-input`** — Dark text input. Background `{colors.surface-card}`, text `{colors.on-dark}`, 1px `{colors.border-control}` boundary, rounded `{rounded.md}` (8px), padding 10px × 14px, height 40px. The boundary is `{colors.border-control}` and not `{colors.hairline-strong}`: at 1.53:1 against the input's own fill the extracted hairline is not visible enough to be the only edge of a control.

**`text-input-focused`** — Adds the 2px `{component.focus-ring}` in `{colors.focus}` at 2px offset; the 1px boundary stays. The earlier "border thickens to yellow" treatment is kept only as a decorative emphasis on dark surfaces — it cannot be the system ring, because it vanishes on yellow bands.

**`text-input-error`** — Boundary flips to `{colors.error}` (#ef4444, 5.26:1 on `{colors.canvas}`), with the message in `{typography.body-sm}`. Colour is never the only error signal; the message carries it.

### Tags / Badges

**`badge-pill`** — Small dark pill label. Background `{colors.surface-card}`, text `{colors.on-dark}`, type `{typography.caption}`, rounded `{rounded.pill}`.

**`badge-yellow`** — Yellow pill for "NEW", "GET STARTED" emphasis. Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.caption-uppercase}`, rounded `{rounded.pill}`.

### Tab / Filter

**`category-tab`** + **`category-tab-active`** — Dark tab navigation. Inactive: transparent + muted text. Active: surface-card background + on-dark text. Padding 8px × 14px, rounded `{rounded.md}`.

### CTA / Footer

**`cta-band-yellow`** — A pre-footer "Deploy your way" CTA band. Full yellow fill, black type, rounded `{rounded.lg}`, padding 64px. Carries an h2 in `{typography.display-md}` and a CTA — usually a black-button on the yellow surface.

**`footer`** — Black footer that closes every page. Background `{colors.canvas}`, text `{colors.muted}`. 4-column link list at desktop covering Product / Use Cases / Resources / Company. Vertical padding 64px. The ClickHouse wordmark sits at the top in `{colors.on-dark}`.

### Component States

Default and Active/pressed are extracted (the file's own `-active` / `-disabled` / `-focused` variants). **Hover, focus-visible, loading, selected and error are prescribed** — the screenshots the rest of this file was read from are static, so no interactive state was observed. A component listed as having only two states genuinely has only two.

| Component | Default | Hover | Focus-visible | Active / pressed | Disabled | Loading | Selected | Error |
|---|---|---|---|---|---|---|---|---|
| `{component.button-primary}` | `{colors.primary}` fill | fill → `{colors.primary-active}` | 2px `{colors.focus}` ring, 2px offset | `{colors.primary-active}`, no scale | `{component.button-primary-disabled}` | label swaps for a spinner in `{colors.on-primary}`, width held, pointer-events off | n/a | n/a |
| `{component.button-secondary}` | `{colors.surface-card}` fill | fill → `{colors.surface-elevated}` | 2px `{colors.focus}` ring | fill → `{colors.hairline}` | fill `{colors.surface-soft}`, text `{colors.muted-soft}` | spinner in `{colors.on-dark}` | n/a | n/a |
| `{component.button-text-link}` | `{colors.on-dark}` label | label → `{colors.primary}` | 2px `{colors.focus}` ring on the text box | label `{colors.primary-active}` | label `{colors.muted-soft}` | n/a — two-state plus disabled | n/a | n/a |
| `{component.text-link}` | `{colors.primary}`, underlined | underline thickens 1px → 2px | 2px `{colors.focus}` ring | `{colors.primary-active}` | n/a | n/a | n/a | n/a |
| `{component.button-icon-circular}` | `{colors.surface-card}` | fill → `{colors.surface-elevated}` | 2px `{colors.focus}` ring at `{rounded.full}` | fill → `{colors.hairline}` | icon `{colors.muted-soft}` | spinner replaces icon | pressed/toggled: fill `{colors.primary}`, icon `{colors.on-primary}` | n/a |
| `{component.text-input}` | 1px `{colors.border-control}` | boundary → `{colors.muted}` | 2px `{colors.focus}` ring, boundary kept | n/a — caret is the pressed signal | fill `{colors.surface-soft}`, text `{colors.muted-soft}`, boundary `{colors.hairline}` | boundary pulses opacity only | n/a | `{component.text-input-error}` — boundary `{colors.error}` + message |
| `{component.category-tab}` | transparent, `{colors.muted}` | text → `{colors.on-dark}` | 2px `{colors.focus}` ring | text `{colors.on-dark}` | text `{colors.muted-soft}`, pointer-events off | n/a | `{component.category-tab-active}` — `{colors.surface-card}` fill + `{colors.on-dark}` | n/a |
| `{component.pricing-tier-card}` | `{colors.surface-card}` | 1px `{colors.border-control}` boundary appears | 2px `{colors.focus}` ring at `{rounded.lg}` | n/a | n/a | skeleton: fill held, content at 0.4 opacity | `{component.pricing-tier-card-featured}` — `{colors.primary}` fill | n/a |
| `{component.feature-card-dark}` | `{colors.surface-card}` | boundary `{colors.border-control}` if the card is a link | 2px `{colors.focus}` ring if the card is a link | n/a | n/a | skeleton at 0.4 opacity | n/a | n/a |
| `{component.feature-card-yellow}` / `{component.cta-band-yellow}` | `{colors.primary}` fill | no hover — these are surfaces, not controls; the button inside hovers | 2px `{colors.focus}` ring on the button inside, 4.02:1 on the yellow fill | n/a | n/a | n/a | n/a | n/a |
| `{component.badge-pill}` / `{component.badge-yellow}` | static label | none | none — not focusable | none | none | none | none | **Default only.** Badges are non-interactive labels. |
| `{component.stat-callout}` / `{component.hero-stat-card}` | `{colors.primary}` number | none | none | none | none | counter holds its final value; no count-up on first paint | none | **Default only.** |
| `{component.top-nav}` | `{colors.canvas}` | per-item: label → `{colors.primary}` | per-item 2px `{colors.focus}` ring | label `{colors.primary-active}` | n/a | n/a | current section: label `{colors.on-dark}` + 2px `{colors.primary}` underline | n/a |
| `{component.code-window-card}` | `{colors.surface-card}` | copy button appears at full opacity | 2px `{colors.focus}` ring on the copy button | copy button `{colors.hairline}` | n/a | n/a | n/a | n/a |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was observed in a running ClickHouse page; every value is derived from the **Crisp** profile, assigned because this is a developer-tool and database identity — monospace code windows, SQL as the hero artifact, query-console product fragments. For a brand whose entire pitch is "fastest," motion that takes time to arrive would contradict the product. State changes read as instant; there is no entrance choreography.

### Motion Tokens

| Token | Value | Meaning |
|---|---|---|
| `{motion.duration-instant}` | 60ms | Hover and press feedback — perceptually immediate |
| `{motion.duration-fast}` | 100ms | Focus ring, tooltip, tab switch |
| `{motion.duration-base}` | 150ms | The Crisp base. Dropdowns, toasts, list items |
| `{motion.duration-slow}` | 220ms | Modal and drawer entrance — the longest thing in the system |
| `{motion.duration-emphasis}` | 320ms | Reserved. Nothing in the documented surface uses it |
| `{motion.ease-standard}` | cubic-bezier(0.2, 0, 0, 1) | Near-linear out — the Crisp bias |
| `{motion.ease-enter}` | cubic-bezier(0, 0, 0.1, 1) | Entrances: no easing in at all, straight to decelerate |
| `{motion.ease-exit}` | cubic-bezier(0.4, 0, 1, 1) | Exits: accelerate away, no lingering |
| `{motion.stagger-step}` | 20ms | List stagger. Barely a cascade — it reads as one block arriving |

### Interaction Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav link, tab, card boundary) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`, `color` / fill crossfade | Unchanged — colour change only, no travel to remove |
| Press (button, icon button) | `{motion.duration-instant}` | `{motion.ease-standard}` | fill swap to `{colors.primary-active}`; **no** `transform` scale — Crisp has no press pop | Unchanged |
| Focus (`{component.focus-ring}` appearing) | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` 0 → 1 on the ring | Ring appears instantly at full `opacity`, no fade |
| Page / route transition | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` 0 → 1 on the incoming main region only | No transition — content is simply present |
| Modal / drawer enter | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px) → 0` (drawer: `translateX`) | `opacity` only at 150ms, no travel |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + the same `transform`, reversed | `opacity` only at 100ms |
| Dropdown / menu enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(-4px) → 0` | `opacity` only at 150ms |
| Dropdown / menu exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` 1 → 0 | `opacity` only at 60ms |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(12px) → 0` | `opacity` only at 150ms |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: translateY(0 → 8px)` | `opacity` only at 100ms |
| List enter (feature grid, pricing tiers, event cards) | `{motion.duration-base}`, `{motion.stagger-step}` 20ms per item, 6 items maximum | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px) → 0` | No stagger, no travel: the whole list fades in once at 150ms |
| List exit (filtered-out items) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | `opacity` only at 100ms |
| Loading (button spinner, skeleton) | 800ms linear, infinite | linear | `transform: rotate` on the spinner; `opacity` 0.4 ↔ 0.8 on skeletons | Spinner frozen at one frame; skeleton holds a static 0.4 `opacity`. A text status ("Loading…") carries the state instead |

### Motion Rules

- Only `transform` and `opacity` are ever in a transition. Never `width`, `height`, `top`, `left` or `margin` — a code-window card must not reflow while a dropdown opens over it.
- Every exit is shorter than its matching entrance (220 → 100ms for modals, 150 → 60ms for dropdowns).
- Nothing animates on first paint in a way that delays content. In particular the yellow `{component.stat-callout}` numbers do **not** count up: the credibility number is readable the moment the band paints.
- The only infinite animation is the loading spinner. This brand has no ambient motion — no drifting gradients, no breathing glow. The black canvas stays still.
- Travel distances are deliberately tiny (4–12px). Crisp motion is about the *state change* being legible, not about things moving.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. Every translateY / translateX /
     rotate above is dropped, every stagger collapses to zero, and the
     loading spinner freezes on a single frame.                        */
  *, *::before, *::after {
    transition-duration: 100ms !important;
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transform: none !important;
  }
  /* Kept: opacity fades, capped at 150ms, and every colour / fill swap.
     Hover and press are unaffected, because Crisp never moved them.
     Loading always carries a text status, not only a spinner.          */
}
```

What is removed: all travel and all scale, all stagger, all infinite animation. What remains: `opacity` fades at 150ms or less, and every colour and fill change — hover, press, focus, selected and error all still read exactly as they do with motion on.

## Accessibility

### Measured Contrast

All ratios WCAG 2.1 relative luminance, computed from this file's own hexes.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 19.80:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.surface-card}` | 17.40:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.surface-elevated}` | 15.52:1 | 4.5 | Pass |
| `{colors.body}` on `{colors.canvas}` | 12.33:1 | 4.5 | Pass |
| `{colors.body}` on `{colors.surface-card}` | 10.84:1 | 4.5 | Pass |
| `{colors.muted}` on `{colors.canvas}` | 5.58:1 | 4.5 | Pass |
| `{colors.muted}` on `{colors.surface-card}` | 4.91:1 | 4.5 | Pass |
| `{colors.muted}` on `{colors.surface-elevated}` | 4.38:1 | 4.5 | **Fail** — do not put `{colors.muted}` on a nested elevated card below 18px |
| `{colors.muted-soft}` on `{colors.canvas}` | 2.87:1 | 4.5 | **Fail** — extracted value; 18px+ only, where 3:1 applies, and even then it is marginal |
| `{colors.on-primary}` on `{colors.primary}` | 18.45:1 | 4.5 | Pass — the brand's signature pairing is also its strongest |
| `{colors.on-primary}` on `{colors.primary-active}` | 15.43:1 | 4.5 | Pass |
| `{colors.primary}` on `{colors.canvas}` | 18.45:1 | 4.5 | Pass |
| `{colors.hairline}` on `{colors.canvas}` | 1.38:1 | 3.0 | **Fail** — extracted; decoration only |
| `{colors.hairline-strong}` on `{colors.canvas}` | 1.74:1 | 3.0 | **Fail** — extracted; decoration only |
| `{colors.border-control}` on `{colors.canvas}` | 3.88:1 | 3.0 | Pass — prescribed |
| `{colors.border-control}` on `{colors.surface-elevated}` | 3.04:1 | 3.0 | Pass — prescribed, and this is the tightest surface |
| `{colors.accent-emerald}` on `{colors.canvas}` | 8.69:1 | 4.5 | Pass |
| `{colors.accent-rose}` on `{colors.canvas}` | 5.26:1 | 4.5 | Pass |
| `{colors.accent-blue}` on `{colors.canvas}` | 5.38:1 | 4.5 | Pass |

**Stated plainly: the real ClickHouse hairlines fail AA as component boundaries, and `{colors.muted-soft}` fails AA as text.** Those are facts about the brand, not errors in this document. Anyone building on it should treat the hairlines as decoration and reach for `{colors.border-control}`, and should not use `{colors.muted-soft}` for anything a reader must read.

### Focus Ring Visibility

`{colors.focus}` (#7a7f10) on every surface this file defines:

| Surface | Ratio | Required |
|---|---|---|
| `{colors.canvas}` #0a0a0a | 4.59:1 | 3.0 |
| `{colors.surface-soft}` #121212 | 4.35:1 | 3.0 |
| `{colors.surface-card}` #1a1a1a | 4.04:1 | 3.0 |
| `{colors.surface-elevated}` #242424 | 3.60:1 | 3.0 |
| `{colors.primary}` / `{colors.surface-yellow-band}` #faff69 | 4.02:1 | 3.0 |
| `{colors.primary-active}` #e6eb52 | 3.36:1 | 3.0 |

One ring clears 3:1 on all six, so this file defines a single `focus` token and no `focus-on-dark` counterpart. Focus is never suppressed: `outline: none` without a replacement ring is forbidden anywhere in this system.

### Tap Targets

Declared sizes, read from this file's own frontmatter — not measured on a rendered page.

- `{component.button-primary}` and `{component.button-secondary}`: 40px high. Below the WCAG 2.5.5 44 × 44 target.
- `{component.text-input}`: 40px high. Same shortfall.
- `{component.button-icon-circular}`: 36 × 36 — the worst case, and the file already flags it.
- `{component.category-tab}`: 8px × 14px padding on 14px/1.4 type ≈ 36px high.

**The declared sizes do not meet 44 × 44 anywhere.** The fix that does not change the brand's visual rhythm is an invisible hit area: keep the painted 40px (or 36px) box and extend the pointer target to 44px with padding or a pseudo-element. That is prescribed, not extracted.

### Other

- **Colour is never the only signal.** Error uses `{colors.error}` *and* a message; selected uses a fill change *and* an underline or a tab well; loading uses a spinner *and* text.
- **Reduced motion** is honoured as specified in Motion & Animation above: all travel and scale removed, `opacity` fades kept at 150ms or less, spinner frozen.
- **Code blocks** in `{typography.code}` at 14px sit on `{colors.surface-card}`; syntax colours beyond `{colors.accent-blue}` were not extracted, so their contrast is unverified. See Known Gaps.

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
| `{colors.hairline}` (`#2a2a2a`) on `{colors.surface-card}` (`#1a1a1a`) | 1.21:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.hairline-strong}` (`#3a3a3a`) on `{colors.surface-card}` (`#1a1a1a`) | 1.53:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.muted-soft}` (`#5a5a5a`) on `{colors.surface-card}` (`#1a1a1a`) | 2.52:1 | 4.5:1 | Fail — secondary text on surface, all tones |

## Do's and Don'ts

### Do
- Anchor every page on the black canvas. The yellow + black pairing is the brand voltage.
- Reserve `{colors.primary}` (yellow) for primary CTAs, stat-callout numbers, and full-bleed yellow CTA bands. The yellow's scarcity at the element level + abundance at the band level is what makes it powerful.
- Use Inter at weight 700 for every display headline, with -1 to -2.5px letter-spacing.
- Show actual SQL code blocks inside `{component.code-window-card}` — ClickHouse is a database; show the query, don't paint marketing illustrations of queries.
- Use `{component.stat-callout}` numbers to establish credibility (community size, contributors, performance benchmarks). The yellow stat numbers are signature.
- Anchor every band with `{spacing.section}` (96px) vertical rhythm.

### Don't
- Don't introduce a second brand color. ClickHouse is monochromatic + yellow.
- Don't bold display weight beyond 700 or use weight 500 for headlines. The hierarchy depends on size, not on weight gradation.
- Don't use yellow for body text or large surface fills outside of intentional yellow cards.
- Don't use rounded buttons / pills outside of small badges. The standard button radius is 8px (md).
- Don't repeat the same surface mode in two consecutive bands. Black canvas → dark feature card → yellow CTA card → black canvas → code-window card.
- Don't replace SQL code mockups with abstract illustrations. The code IS the marketing voltage.
- Don't let hover or press *move* anything. Crisp motion changes fill, colour and opacity only — no scale pop, no lift. Hover styling itself is now specified; see Component States.
- Don't suppress the focus ring. `outline: none` without `{component.focus-ring}` in its place is a defect, not a style choice.
- Don't use `{colors.hairline}` or `{colors.hairline-strong}` as the only boundary of an interactive control — at 1.38:1 and 1.74:1 on the canvas they are decoration. Use `{colors.border-control}`.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav; hero h1 72→36px; code-window-card stacks below; feature grids 1-up; pricing 1-up |
| Tablet | 768–1024px | Top nav tightens; feature cards 2-up; pricing 2-up |
| Desktop | 1024–1440px | Full top-nav; 3-up feature cards; 3-4 up pricing tiers |
| Wide | > 1440px | Same as desktop with more breathing room; max content 1280px |

### Touch Targets
- `{component.button-primary}` at minimum 40 × 40px.
- `{component.button-icon-circular}` at exactly 36 × 36 — slightly under WCAG 44, visually centered.
- `{component.text-input}` height is 40px.

### Collapsing Strategy
- Top nav collapses to hamburger at < 768px.
- Hero 7-5 grid → single-column on mobile.
- Feature card grids reduce columns rather than scaling.
- Code-window cards retain font-size; horizontal scroll inside the card on mobile.
- Pricing tier cards collapse 4 → 2 → 1; featured tier yellow stays distinct.

### Image Behavior
- Code blocks inside dark mockups stay at fixed font-size; horizontal scroll on mobile rather than wrapping.
- Customer logos in monochrome strip retain native widths; row wraps on mobile.

## Iteration Guide

1. Focus on ONE component at a time. Reference its YAML key (`{component.code-window-card}`, `{component.pricing-tier-card-featured}`).
2. Variants of an existing component (`-active`, `-disabled`, `-focused`) live as separate entries.
3. Use `{token.refs}` everywhere — never inline hex.
4. Document every state a component supports — see Component States. Default and Active/pressed are extracted; hover, focus-visible, loading, selected and error are prescribed and labelled as such.
5. Display headlines stay Inter 700 with negative letter-spacing. Body stays Inter 400.
6. The yellow + black pairing is the brand contract. Don't soften with secondary accents.
7. When in doubt about emphasis: bigger Inter 700 before adding color.

## Known Gaps

- The exact yellow hex (#faff69) was sampled from the screenshot; ClickHouse may publish an official brand color slightly differently.
- Inter weight axis values beyond 400 / 500 / 600 / 700 are not formalized — only the static weights observed are documented.
- **No motion value in this file was measured.** The entire Motion & Animation section is prescribed from the Crisp profile. Whether ClickHouse actually runs code-typewriter effects or stat counter animations on the live site is unknown; this document forbids both, which may differ from the real site.
- `{colors.border-control}` and `{colors.focus}` are prescribed, not sampled. ClickHouse may publish a different focus treatment.
- Form validation states beyond `{component.text-input-focused}` and the prescribed `{component.text-input-error}` are not extracted. Hover, focus-visible, loading and selected treatments in Component States are prescribed.
- Tap-target sizes above are the values *declared* in this file's frontmatter. Nothing here was measured on a rendered page, so overlap, clipping and real hit areas remain unverified.
- The actual ClickHouse Cloud product surface (query console, monitoring dashboards, table browser) shares some tokens with the marketing site but adds many product-specific components that are out of scope.
- The customer logo strip's exact opacity / treatment varies — the muted gray is approximate.
