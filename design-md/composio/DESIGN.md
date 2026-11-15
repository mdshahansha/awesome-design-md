---
version: alpha
name: Composio-design-analysis
description: A developer-tools brand for AI-agent tool integration whose marketing surfaces lean into a dark, technical aesthetic with a single deep-electric-blue voltage (`#0007cd`). The page floor is near-black (`#0f0f0f`); cards float above on subtle gray-tinted surfaces. abcDiatype carries display and body in a single sans family with weights 400-600. The brand's strongest visual signature is a four-pane terminal-style mockup (a 2×2 grid of dark code/output panels) with a central blue spotlight glow — used as the homepage hero anchor.

colors:
  primary: "#0007cd"
  primary-active: "#0005a3"
  primary-glow: "#1a26ff"
  ink: "#ffffff"
  body: "#a8a8a8"
  body-strong: "#ffffff"
  muted: "#888888"
  muted-soft: "#666666"
  hairline: "#222222"
  hairline-soft: "#1a1a1a"
  hairline-strong: "#333333"
  hairline-control: "#757575"
  focus: "#6b7bff"
  canvas: "#0f0f0f"
  canvas-deep: "#000000"
  surface-card: "#181818"
  surface-card-elevated: "#222222"
  surface-strong: "#2a2a2a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-cyan: "#00d4ff"
  accent-violet: "#7b3aed"
  semantic-error: "#ff4d4d"
  semantic-success: "#33d17a"

typography:
  display-mega:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -2.16px
  display-xl:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -1.68px
  display-lg:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1.32px
  display-md:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.96px
  display-sm:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  title-md:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.88px
    textTransform: uppercase
  code:
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  nav-link:
    fontFamily: "'abcDiatype', ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  base: 16px
  md: 20px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

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
  top-nav-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body-strong}"
    typography: "{typography.nav-link}"
    height: 64px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary-dark:
    backgroundColor: "{colors.surface-card-elevated}"
    textColor: "{colors.body-strong}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
    height: 40px
  button-outline:
    backgroundColor: transparent
    borderColor: "{colors.hairline-control}"
    textColor: "{colors.body-strong}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 9px 17px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body-strong}"
    typography: "{typography.display-mega}"
    padding: 96px
  terminal-mockup-grid:
    backgroundColor: "{colors.canvas-deep}"
    textColor: "{colors.body-strong}"
    typography: "{typography.code}"
    rounded: "{rounded.xl}"
    padding: 32px
  terminal-pane:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: 20px
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 28px
  toolkit-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body-strong}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: 20px
  toolkit-icon:
    backgroundColor: "{colors.surface-card-elevated}"
    rounded: "{rounded.md}"
    size: 40px
  spotlight-glow-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body-strong}"
    typography: "{typography.display-md}"
    rounded: "{rounded.xl}"
    padding: 48px
  code-block:
    backgroundColor: "{colors.canvas-deep}"
    textColor: "{colors.body}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: 20px
  badge-pill:
    backgroundColor: "{colors.surface-card-elevated}"
    textColor: "{colors.body-strong}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline-control}"
    focusRingColor: "{colors.focus}"
    textColor: "{colors.body-strong}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 44px
  search-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline-control}"
    focusRingColor: "{colors.focus}"
    textColor: "{colors.body-strong}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 40px
  cta-band-spotlight:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body-strong}"
    typography: "{typography.display-lg}"
    padding: 96px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  footer-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 64px 48px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
---

## Overview

Composio's marketing site reads like a serious developer-infrastructure brand — closer to Vercel or Stripe Docs in atmosphere than to a typical AI-tools startup. The base canvas is a near-black `{colors.canvas}` (#0f0f0f) holding white type and a single voltage of **deep electric blue** (`{colors.primary}` — #0007cd) carrying every primary CTA, brand wordmark, and atmospheric spotlight glow that backs the homepage hero.

Type runs **abcDiatype** as the single sans family across display, body, navigation, and captions. Display sits at weight 500 — confident but not bombastic. Code blocks and terminal mockups switch to JetBrains Mono.

The page rhythm is monolithic: dark canvas top to bottom with subtle elevation steps via card surfaces. The brand's strongest visual signature is a **four-pane terminal-style mockup** — a 2×2 grid of dark code/output panels with a central blue spotlight glow behind them.

**Key Characteristics:**
- Single accent: `{colors.primary}` (#0007cd) for primary CTAs, wordmark, spotlight glows.
- Single sans family: abcDiatype carries everything except code (JetBrains Mono).
- Dark monolithic canvas: `{colors.canvas}` runs top to bottom; depth from `{colors.surface-card}` and `{colors.surface-card-elevated}` brightness steps.
- Terminal-mockup hero: 2×2 grid of code/output panes is the brand signature.
- Compact pill geometry: CTAs sit at `{rounded.md}` (8px), not full pills — developer-tool dialect.
- Spotlight-glow atmospheric backdrop: a radial blue glow centered behind hero content.
- 96px section rhythm.

## Colors

### Brand & Accent
- **Composio Blue** (`{colors.primary}` — #0007cd): Primary CTAs, wordmark, spotlight glow center.
- **Composio Blue Active** (`{colors.primary-active}` — #0005a3): Press state.
- **Spotlight Glow Tone** (`{colors.primary-glow}` — #1a26ff): Brighter blue used inside radial atmospheric glows.
- **Accent Cyan** (`{colors.accent-cyan}` — #00d4ff): Sparingly on data-flow visualizations.
- **Accent Violet** (`{colors.accent-violet}` — #7b3aed): Inside specific product illustrations only.

### Surface
- **Canvas** (`{colors.canvas}` — #0f0f0f): Page floor — near-black.
- **Canvas Deep** (`{colors.canvas-deep}` — #000000): Pure black for terminal mockup grids and code blocks.
- **Surface Card** (`{colors.surface-card}` — #181818): Default content card.
- **Surface Card Elevated** (`{colors.surface-card-elevated}` — #222222): Terminal panes, secondary buttons.
- **Surface Strong** (`{colors.surface-strong}` — #2a2a2a): Dropdown menus.

### Hairlines
All three extracted hairline tones are **decorative only** — they sit between 1.10:1 and 1.52:1 on `{colors.canvas}`, so none of them can carry the only visible boundary of a control. The real brand fails WCAG AA on non-text contrast here; the measured ratios are in **Accessibility**.

- **Hairline** (`{colors.hairline}` — #222222): Default 1px divider, decorative.
- **Hairline Soft** (`{colors.hairline-soft}` — #1a1a1a): Lighter divider, decorative.
- **Hairline Strong** (`{colors.hairline-strong}` — #333333): Stronger panel outline, decorative.
- **Hairline Control** (`{colors.hairline-control}` — #757575): **Prescribed, not extracted.** The accessible parallel boundary tone for anything whose edge must be seen — text and search input outlines, dropdown edges, segmented controls. Clears 3:1 on every surface this file defines.

### Focus
- **Focus Ring** (`{colors.focus}` — #6b7bff): **Prescribed, not extracted** — Composio Blue lifted until it clears 3:1 on a near-black canvas, which `{colors.primary}` (1.75:1 on `{colors.canvas}`) cannot do. A single mid-luminance ring serves every surface in this file, including the blue CTA itself, so no `focus-on-dark` pair is needed. Drawn as a 2px ring with a 2px `{colors.canvas}` offset.

### Text
- **Ink** (`{colors.ink}` — #ffffff): Display headlines.
- **Body** (`{colors.body}` — #a8a8a8): Default running-text — soft gray.
- **Body Strong** (`{colors.body-strong}` — #ffffff): Same as ink.
- **Muted** (`{colors.muted}` — #888888): Sub-titles, breadcrumbs. The lightest tone that reads as secondary text — 5.41:1 on `{colors.canvas}`, 5.01:1 on `{colors.surface-card}`.
- **Muted Soft** (`{colors.muted-soft}` — #666666): Disabled text and decorative labels **only**. It fails AA for live text (3.34:1 on `{colors.canvas}`, 3.09:1 on `{colors.surface-card}`); use `{colors.muted}` wherever the text must be read.
- **On Primary** (`{colors.on-primary}` — #ffffff): White text on blue CTAs.

### Semantic
- **Success** (`{colors.semantic-success}` — #33d17a): "Online", "active" indicators.
- **Error** (`{colors.semantic-error}` — #ff4d4d): Validation errors.

## Typography

### Font Family
The system runs **abcDiatype** (Lineto) across every text role. Code blocks switch to **JetBrains Mono**. Fallback: `ui-sans-serif, system-ui, sans-serif`.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-mega}` | 72px | 500 | 1.05 | -2.16px | Homepage hero h1 |
| `{typography.display-xl}` | 56px | 500 | 1.05 | -1.68px | Subsidiary heroes |
| `{typography.display-lg}` | 44px | 500 | 1.1 | -1.32px | Section heads |
| `{typography.display-md}` | 32px | 500 | 1.15 | -0.96px | Sub-section heads |
| `{typography.display-sm}` | 24px | 500 | 1.25 | -0.5px | Card group titles |
| `{typography.title-md}` | 18px | 600 | 1.4 | 0 | Component titles |
| `{typography.title-sm}` | 16px | 600 | 1.4 | 0 | Toolkit card titles |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default body |
| `{typography.body-sm}` | 14px | 400 | 1.5 | 0 | Footer body |
| `{typography.caption}` | 13px | 400 | 1.4 | 0 | Photo captions |
| `{typography.caption-uppercase}` | 11px | 600 | 1.4 | 0.88px | Section labels, badge pills |
| `{typography.code}` | 13px | 400 | 1.5 | 0 | Code blocks — JetBrains Mono |
| `{typography.button}` | 14px | 500 | 1.0 | 0 | CTA pill labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Top-nav menu |

### Principles
- **Display weight stays at 500.** Confident but not display-bold.
- **abcDiatype across every role.** No display/body family split.
- **JetBrains Mono on every code surface.**

### Note on Font Substitutes
abcDiatype is a Lineto licensed typeface. Open-source substitute: **Inter** at weight 500 with letter-spacing -1.5%.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.base}` 16px · `{spacing.md}` 20px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- **Section padding:** `{spacing.section}` (96px) for major bands.

### Grid & Container
- Max content width: ~1200px.
- Editorial body: 12-column grid.
- Terminal mockup grid: 2×2 equal-size panes.
- Toolkit grid: 4-up at desktop, 2-up tablet, 1-up mobile.
- Footer: 5-column at desktop.

### Whitespace Philosophy
The dark canvas creates its own depth — whitespace can stay tight without feeling crowded. 96px between bands; 24px between cards inside a band.

## Elevation & Depth

The system uses **brightness-step elevation**: surfaces step up in brightness instead of casting drop shadows. Combined with subtle radial blue glows, this creates a focused dark-mode atmosphere.

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `{colors.canvas}` (#0f0f0f) | Body bands, footer |
| Recessed | `{colors.canvas-deep}` (#000000) | Terminal mockup grid background, code blocks |
| Card | `{colors.surface-card}` (#181818) | Default content cards |
| Card elevated | `{colors.surface-card-elevated}` (#222222) | Terminal panes, secondary buttons |
| Atmospheric glow | Radial gradient using `{colors.primary-glow}` | Hero spotlight backdrop |

### How far apart the layers actually sit

Measured step ratios between adjacent layers — all brightness, no shadow, so elevation is expressed exactly one way throughout:

| Step | Ratio | Verdict |
|---|---|---|
| `{colors.canvas-deep}` → `{colors.canvas}` | 1.10:1 | Reads as a shift in large areas only |
| `{colors.canvas}` → `{colors.surface-card}` | 1.08:1 | Reads as a shift in large areas only |
| `{colors.surface-card}` → `{colors.surface-card-elevated}` | 1.12:1 | Reads as a shift in large areas only |
| `{colors.surface-card-elevated}` → `{colors.surface-strong}` | 1.11:1 | Reads as a shift in large areas only |

This is a deliberate near-black ladder, and it is honest to say that no single step is independently perceivable at the 3:1 non-text threshold. The layers work because the panes are large and adjacent. For any **small** raised element — a dropdown over a card, a toolkit icon plate on a card — add a 1px `{colors.hairline-control}` edge rather than relying on the brightness step alone.

### Decorative Depth
- **Spotlight glow backdrops** — radial blue gradient centered behind hero content.
- **Terminal-pane brightness ladder** — 2×2 mockup uses canvas-deep outer + surface-card-elevated panes.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Reserved |
| `{rounded.xs}` | 4px | Inline tags |
| `{rounded.sm}` | 6px | Compact rows |
| `{rounded.md}` | 8px | CTA buttons, form inputs |
| `{rounded.lg}` | 12px | Toolkit cards, code blocks, terminal panes |
| `{rounded.xl}` | 16px | Feature cards, terminal mockup grids |
| `{rounded.pill}` | 9999px | Section-label badges |
| `{rounded.full}` | 9999px | Avatar plates (rare) |

Compact developer-ergonomic radii — 8px CTAs, 12-16px cards. Signals "developer tool" rather than "consumer brand."

### Border & Focus Ring Widths

One ladder, two steps, no value outside it:

| Use | Width | Colour |
|---|---|---|
| Divider / decorative panel edge | 1px | `{colors.hairline}`, `{colors.hairline-soft}` or `{colors.hairline-strong}` |
| Control boundary (inputs, dropdowns, outline button) | 1px | `{colors.hairline-control}` |
| Focus ring | 2px + 2px offset | `{colors.focus}` over a `{colors.canvas}` offset |

The focus ring inherits its host's radius — `{rounded.md}` on CTAs and inputs, `{rounded.lg}`/`{rounded.xl}` on cards — so no separate ring radius scale exists.

## Components

### Top Navigation

**`top-nav-dark`** — Default top nav. Background `{colors.canvas}`, text `{colors.body-strong}`, height 64px. Layout: Composio wordmark left, primary horizontal menu (Product / Toolkits / Docs / Pricing / Customers / Blog), GitHub stars + Sign In + "Get started" right.

### Buttons

**`button-primary`** — The signature Composio Blue CTA. Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}` (14px / 500), padding 10px × 18px, height 40px, rounded `{rounded.md}` (8px).

**`button-primary-active`** — Press state. Background `{colors.primary-active}`.

**`button-secondary-dark`** — Surface-elevated secondary. Background `{colors.surface-card-elevated}`, text `{colors.body-strong}`.

**`button-outline`** — Transparent with a 1px `{colors.hairline-control}` border. The extracted `{colors.hairline-strong}` edge sits at 1.52:1 on `{colors.canvas}` and is not a usable control boundary.

**`button-tertiary-text`** — Inline text link.

### Hero & Atmospheric

**`hero-band`** — Homepage hero. Background `{colors.canvas}`, full-width display headline in `{typography.display-mega}` (72px / 500), subhead, two CTAs, and a spotlight-glow backdrop emanating from behind the centered terminal-mockup grid.

**`terminal-mockup-grid`** — The brand's strongest visual signature. 2×2 grid of dark code/output panels inside a `{rounded.xl}` (16px) container. Background `{colors.canvas-deep}`, padding 32px, gap 16px.

**`terminal-pane`** — Individual code/output panel inside the mockup grid. Background `{colors.surface-card}`, text `{colors.body}` in `{typography.code}`, rounded `{rounded.lg}` (12px), padding 20px.

**`spotlight-glow-card`** — Large feature card with centered display headline and a radial blue glow behind it. Background `{colors.surface-card}`, text `{colors.body-strong}` in `{typography.display-md}`, rounded `{rounded.xl}`, padding 48px.

### Cards

**`feature-card`** — 3-up benefit grid. Background `{colors.surface-card}`, text `{colors.body}`, type `{typography.title-md}`, rounded `{rounded.xl}`, padding 28px.

**`toolkit-card`** — 4-up toolkit grid (Slack, GitHub, Stripe, Notion, Linear, etc.). Background `{colors.surface-card}`, text `{colors.body-strong}`, type `{typography.title-sm}`, rounded `{rounded.lg}`, padding 20px. 40px square `{component.toolkit-icon}` top, toolkit name, one-line description.

**`toolkit-icon`** — Square icon plate. Background `{colors.surface-card-elevated}`, rounded `{rounded.md}`, 40px size.

**`testimonial-card`** — Quote card. Background `{colors.surface-card}`, text `{colors.body}`, rounded `{rounded.lg}`, padding 24px.

### Code

**`code-block`** — Inline code/terminal block. Background `{colors.canvas-deep}`, text `{colors.body}` in `{typography.code}`, rounded `{rounded.lg}`, padding 20px.

### Forms

**`text-input`** — Background `{colors.surface-card}`, 1px `{colors.hairline-control}` border, text `{colors.body-strong}`, rounded `{rounded.md}` (8px), padding 12px × 16px, height 44px. Focus draws a 2px `{colors.focus}` ring with a 2px `{colors.canvas}` offset; error swaps the border to `{colors.semantic-error}`.

**`search-input`** — Compact search field. Same surface, border, radius and focus ring; smaller padding, 40px height.

### Tags & Badges

**`badge-pill`** — Small uppercase pill. Background `{colors.surface-card-elevated}`, text `{colors.body-strong}`, type `{typography.caption-uppercase}`, rounded `{rounded.pill}`, padding 4px × 10px.

### CTA / Footer

**`cta-band-spotlight`** — Pre-footer band. Background `{colors.canvas}` with centered radial spotlight glow. Display headline + single primary CTA pill. 96px padding.

**`footer-dark`** — Closing footer. Background `{colors.canvas}`, text `{colors.body}`. 5-column link list. 64×48px padding.

**`footer-link`** — Background transparent, text `{colors.body}`, type `{typography.body-sm}`.

### Interaction States

The captured marketing surfaces show default and press only; everything else below is **prescribed to match the brand's visual identity and was not extracted from the live site**. Press reuses the extracted `{colors.primary-active}`, which is a real brand value. "Two states only" means the element is non-interactive static layout — default and nothing else — and that is stated rather than left blank.

| Component | States |
|---|---|
| `top-nav-dark` | default · hover (link text `{colors.body}` → `{colors.body-strong}`) · focus-visible (ring on each link) · selected (current section underline in `{colors.primary}`) |
| `button-primary` | default · hover (`{colors.primary-glow}`) · focus-visible (`{colors.focus}` ring) · active/pressed (`{colors.primary-active}`) · disabled (`{colors.surface-card-elevated}` fill, `{colors.muted-soft}` label) · loading (label held, inline spinner) |
| `button-primary-active` | the pressed variant of `button-primary` — one state by definition |
| `button-secondary-dark` | default · hover (`{colors.surface-strong}`) · focus-visible · active/pressed (`{colors.surface-card}`) · disabled · loading |
| `button-outline` | default · hover (border `{colors.hairline-control}` → `{colors.focus}`) · focus-visible · active/pressed · disabled |
| `button-tertiary-text` | default · hover (`{colors.body}` → `{colors.body-strong}`) · focus-visible · active/pressed · disabled |
| `hero-band` | default only — static layout band, two states do not apply |
| `terminal-mockup-grid` | default only — static brand illustration |
| `terminal-pane` | default · selected (active pane border `{colors.hairline-control}`) — the mockup's panes are tab-like but carry no hover |
| `feature-card` | default · hover (surface `{colors.surface-card}` → `{colors.surface-card-elevated}`) · focus-visible when the whole card is a link |
| `toolkit-card` | default · hover (surface step up) · focus-visible · selected (1px `{colors.primary}` border in the toolkit picker) · loading (skeleton at `{colors.surface-card-elevated}`) |
| `toolkit-icon` | default only — decorative plate inside `toolkit-card` |
| `spotlight-glow-card` | default · hover (glow opacity lift) when the card is a link |
| `code-block` | default · hover (copy button appears) · focus-visible on the copy button · selected (text selection in `{colors.primary}` at 30% opacity) |
| `badge-pill` | default only — non-interactive label |
| `text-input` | default · hover (border `{colors.hairline-control}` lightens) · focus-visible (2px `{colors.focus}` ring) · disabled (`{colors.muted-soft}` text) · error (`{colors.semantic-error}` border + message) |
| `search-input` | default · hover · focus-visible · disabled · loading (inline spinner while results resolve) |
| `cta-band-spotlight` | default only — static layout band; its CTA carries `button-primary` states |
| `testimonial-card` | default only — static quote card |
| `footer-dark` | default only — static layout band |
| `footer-link` | default · hover (`{colors.body}` → `{colors.body-strong}`) · focus-visible |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted from Composio's pages; they are the **Crisp** profile's shared values, chosen because the brand is a developer-tool identity whose whole voice — terminal mockups, JetBrains Mono, 8px CTAs, no drop shadows — asks for state changes that read as instant rather than choreographed.

Tokens: `{motion.duration-instant}` 60ms · `{motion.duration-fast}` 100ms · `{motion.duration-base}` 150ms · `{motion.duration-slow}` 220ms · `{motion.duration-emphasis}` 300ms · `{motion.stagger-step}` 20ms · `{motion.duration-reduced}` 100ms. Easings: `{motion.ease-standard}`, `{motion.ease-enter}`, `{motion.ease-exit}`.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, link) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`; background colour cross-fade | Unchanged — no travel to remove |
| Press | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed; colour change only, instant |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring | Ring appears with no transition |
| Page / route transition | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` only, no travel | `opacity` at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px → 0)` | Travel removed; `opacity` at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform` | Travel removed; `opacity` at `{motion.duration-reduced}` |
| Dropdown open | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` + `transform: scaleY(0.98 → 1)` from the trigger edge | Scale removed; `opacity` at `{motion.duration-reduced}` |
| Dropdown close | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | `opacity` at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px → 0)` | Travel removed; `opacity` at `{motion.duration-reduced}` |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform` | Travel removed; `opacity` at `{motion.duration-reduced}` |
| List enter (toolkit grid, search results) | `{motion.duration-fast}` per item, `{motion.stagger-step}` apart, capped at 8 items | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px → 0)` | Stagger and travel removed; one `opacity` fade at `{motion.duration-reduced}` for the whole list |
| List exit | `{motion.duration-instant}`, no stagger | `{motion.ease-exit}` | `opacity` | `opacity` at `{motion.duration-reduced}` |
| Loading (spinner, skeleton) | 800ms linear, infinite | linear | `transform: rotate()` on the spinner; `opacity` pulse on skeletons | Spinner freezes; skeletons hold a static `{colors.surface-card-elevated}` fill |
| Spotlight-glow ambience | `{motion.duration-emphasis}` on first reveal, then static | `{motion.ease-enter}` | `opacity` | Revealed at full opacity, no transition |

### Rules
- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin`.
- Every exit is shorter than its matching entrance (`{motion.duration-fast}` out against `{motion.duration-base}` in).
- Nothing animates on first paint in a way that delays content. The hero headline and terminal mockup render at full opacity; only the spotlight glow has a reveal, and it sits behind the content.
- The only infinite animation is the loading spinner. The spotlight glow is **not** ambient motion — it is a static radial gradient, revealed once.
- Crisp means no entrance choreography on marketing bands: sections do not fade in on scroll.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate, all scale, all rotation, all stagger. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (100ms). */
  /* Frozen: the loading spinner holds a static frame; skeletons stop pulsing. */
  *, *::before, *::after {
    transition-duration: 100ms !important;
    transition-property: opacity !important;
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

What is removed: the press scale, modal/drawer and toast travel, dropdown scaleY, list stagger and list travel, spinner rotation, skeleton pulse. What remains: opacity fades at `{motion.duration-reduced}` (100ms) and every colour change, which is instant at this profile anyway. No state becomes unreachable or invisible when motion is off — focus, selection and error are all carried by colour and the `{colors.focus}` ring, never by movement.

## Accessibility

### Measured contrast

Computed with WCAG 2.1 relative luminance from this file's own hexes.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` / `{colors.canvas}` | 19.17:1 | 4.5:1 | Pass |
| `{colors.ink}` / `{colors.surface-card}` | 17.76:1 | 4.5:1 | Pass |
| `{colors.body}` / `{colors.canvas}` | 8.06:1 | 4.5:1 | Pass |
| `{colors.body}` / `{colors.surface-card}` | 7.47:1 | 4.5:1 | Pass |
| `{colors.on-primary}` / `{colors.primary}` | 10.98:1 | 4.5:1 | Pass |
| `{colors.muted}` / `{colors.canvas}` | 5.41:1 | 4.5:1 | Pass |
| `{colors.muted}` / `{colors.surface-card}` | 5.01:1 | 4.5:1 | Pass |
| `{colors.focus}` / `{colors.canvas}` | 5.39:1 | 3.0:1 | Pass |
| `{colors.hairline-control}` / `{colors.canvas}` | 4.16:1 | 3.0:1 | Pass |

### Where the real brand fails AA

These are extracted, frozen values. They are stated here rather than corrected, because changing a brand's own hex would make the document wrong.

- `{colors.hairline-soft}` (#1a1a1a) on `{colors.canvas}` measures **1.10:1** against the 3.0:1 non-text minimum. Decorative dividers only.
- `{colors.hairline}` (#222222) on `{colors.canvas}` measures **1.20:1** against 3.0:1. Decorative dividers only.
- `{colors.hairline-strong}` (#333333) on `{colors.canvas}` measures **1.52:1** against 3.0:1. Decorative panel outlines only; it is not a usable control boundary, which is why `{colors.hairline-control}` exists.
- `{colors.muted-soft}` (#666666) on `{colors.canvas}` measures **3.34:1** and on `{colors.surface-card}` measures **3.09:1**, both against the 4.5:1 body-text minimum. Disabled text (exempt) and decorative labels only. For live secondary text use `{colors.muted}`.
- `{colors.muted}` (#888888) on `{colors.surface-card-elevated}` measures **4.49:1** — 0.01 short of 4.5:1. Treat as failing on that surface and use `{colors.body}` (6.69:1) inside secondary buttons and terminal panes.
- `{colors.accent-violet}` (#7b3aed) measures **3.35:1** on `{colors.canvas}` and **3.10:1** on `{colors.surface-card}`. It is illustration-only and never carries text or a control boundary.
- The elevation ladder's steps sit between 1.08:1 and 1.12:1. No layer boundary is independently perceivable; see **Elevation & Depth**.

### Focus ring visibility, per surface this file defines

`{colors.focus}` (#6b7bff), 2px, with a 2px `{colors.canvas}` offset:

| Surface | Ratio vs ring | Verdict |
|---|---|---|
| `{colors.canvas}` (#0f0f0f) | 5.39:1 | Pass |
| `{colors.canvas-deep}` (#000000) | 5.90:1 | Pass |
| `{colors.surface-card}` (#181818) | 4.99:1 | Pass |
| `{colors.surface-card-elevated}` (#222222) | 4.47:1 | Pass |
| `{colors.surface-strong}` (#2a2a2a) | 4.03:1 | Pass |
| `{colors.primary}` (#0007cd) | 3.09:1 | Pass |
| `{colors.primary-active}` (#0005a3) | 3.81:1 | Pass |

Every surface clears the 3.0:1 non-text minimum, so one ring serves the whole system and no `focus-on-dark` counterpart is required. Focus is never conveyed by colour alone inside the ring — the ring is a shape change at the element edge.

### Tap targets

Documented heights from this file: `text-input` 44px, `button-primary` / `button-secondary-dark` / `button-outline` / `search-input` 40px, `top-nav-dark` 64px, `toolkit-icon` 40px. 44px meets the 44×44 AAA target; the 40px controls meet the 24×24 AA minimum but fall 4px short of AAA, and the fix is vertical padding on the hit area rather than a taller visual pill. Rendered tap-target size cannot be verified from a document — see **Known Gaps**.

### Reduced motion

Honoured in full; see the `@media (prefers-reduced-motion: reduce)` block above. All travel, scale, rotation and stagger are removed, opacity fades are capped at `{motion.duration-reduced}` (100ms), and the loading spinner freezes.

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
| `{colors.hairline-soft}` (`#1a1a1a`) on `{colors.surface-card}` (`#181818`) | 1.02:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.hairline-strong}` (`#333333`) on `{colors.surface-card}` (`#181818`) | 1.41:1 | 3.0:1 | Fail — boundary on surface, all tones |

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` for primary CTAs, wordmark, and spotlight glows.
- Use `{rounded.md}` (8px) for every CTA — not full pills.
- Use brightness-step ladder for elevation; avoid drop shadows.
- Pair every hero with a centered radial blue spotlight glow.
- Render code, CLI commands in JetBrains Mono via `{typography.code}`.
- Use the 2×2 terminal-mockup grid as the homepage hero anchor.
- Draw every focus ring in `{colors.focus}` at 2px with a 2px `{colors.canvas}` offset.
- Use `{colors.hairline-control}` for any boundary a user has to see; keep the extracted hairlines decorative.
- Keep motion at `{motion.duration-base}` or faster — a state change should read as instant.

### Don't
- Don't introduce a secondary brand color. Cyan and violet are illustrative-only.
- Don't use full pills on CTAs.
- Don't drop display weight to 400.
- Don't add drop shadow tiers.
- Don't use canvas-deep (#000000) outside terminal/code surfaces.
- Don't use `{colors.primary}` as a focus ring — at 1.75:1 on `{colors.canvas}` it is invisible as an indicator.
- Don't set body or secondary text in `{colors.muted-soft}`; it fails AA on both `{colors.canvas}` and `{colors.surface-card}`.
- Don't add scroll-triggered entrance animations to marketing bands.
- Don't extract a CTA color from a third-party widget (cookie consent, OneTrust). The brand's CTA color is what appears on actual page CTAs.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 640px | Hero h1 72→36px; terminal mockup grid collapses to single pane; toolkit grid 1-up; nav hamburger. |
| Tablet | 640–1024px | Hero h1 56px; terminal mockup grid stays 2×2; toolkit grid 2-up. |
| Desktop | 1024–1280px | Full hero h1 72px; full 2×2 terminal mockup; toolkit grid 4-up. |
| Wide | > 1280px | Content caps at 1200px. |

### Touch Targets
- Primary CTA at 40px height — clears the 24×24 AA minimum, 4px short of the 44×44 AAA target; pad the hit area rather than growing the pill.
- Search input at 40px; `text-input` at 44px meets AAA.

### Collapsing Strategy
- Top nav switches to hamburger below 768px.
- Terminal mockup 2×2 grid collapses to a single pane on mobile.
- Toolkit grid: 4-up → 2-up → 1-up.
- Hero spotlight glow stays at every breakpoint.

## Iteration Guide

1. Focus on a single component at a time.
2. CTAs default to `{rounded.md}` (8px). Cards use `{rounded.lg}` or `{rounded.xl}`.
3. Variants live as separate entries inside `components:`.
4. Use `{token.refs}` everywhere — never inline hex.
5. Interaction states are prescribed, not extracted — see **Components → Interaction States**.
6. abcDiatype 500 for display, 400/600 for body. JetBrains Mono on every code surface.
7. Composio Blue stays scarce.

## Known Gaps

- abcDiatype is licensed; Inter is the substitute.
- **Motion is prescribed, not measured.** No duration, easing or stagger in **Motion & Animation** was extracted from the live site; they are the Crisp profile's shared values.
- **Interaction states are prescribed, not measured**, except `{colors.primary-active}` for press, which is an extracted hex.
- `{colors.focus}` and `{colors.hairline-control}` are prescribed tokens. No focus ring or accessible boundary colour was extracted from the site.
- In-product surfaces (toolkit dashboards, agent playground) are behind login walls.
- Form validation states beyond focus not visible on captured surfaces.
- Not verifiable from a document: rendered tap-target size, overlap, horizontal overflow, clipping, frame rate and layout shift. Every claim above is computed from this file's own values.
