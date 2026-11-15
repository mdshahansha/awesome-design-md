---
version: alpha
name: Cursor-design-analysis
description: An AI-first code editor whose marketing site reads like a quietly-confident developer-tools brand with a warm-cream editorial canvas (`#f7f7f4`) instead of the typical dark IDE atmosphere. Near-black warm ink (`#26251e`) carries body and display alike — display sits at weight 400 with negative letter-spacing for a magazine feel rather than a bold tech voice. The single brand voltage is **Cursor Orange** (`#f54e00`) reserved for primary CTAs and the wordmark. A signature pastel timeline palette (peach, mint, blue, lavender, gold) marks AI-action stages (Thinking / Reading / Editing / Grepping / Done) — only inside in-product timeline visualizations. Cards use minimal hairlines, no shadows, generous 80px section rhythm. CursorGothic for display/body, JetBrains Mono on every code surface (which is roughly half the page).

colors:
  primary: "#f54e00"
  primary-active: "#d04200"
  ink: "#26251e"
  body: "#5a5852"
  body-strong: "#26251e"
  muted: "#807d72"
  muted-soft: "#a09c92"
  muted-accessible: "#6e6b62"
  hairline: "#e6e5e0"
  hairline-soft: "#efeee8"
  hairline-strong: "#cfcdc4"
  hairline-control: "#8f8c82"
  canvas: "#f7f7f4"
  canvas-soft: "#fafaf7"
  surface-card: "#ffffff"
  surface-strong: "#e6e5e0"
  on-primary: "#ffffff"
  focus: "#26251e"
  focus-on-dark: "#f7f7f4"
  timeline-thinking: "#dfa88f"
  timeline-grep: "#9fc9a2"
  timeline-read: "#9fbbe0"
  timeline-edit: "#c0a8dd"
  timeline-done: "#c08532"
  semantic-error: "#cf2d56"
  semantic-success: "#1f8a65"

typography:
  display-mega:
    fontFamily: "'CursorGothic', system-ui, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -2.16px
  display-lg:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.72px
  display-md:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.325px
  display-sm:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.11px
  title-md:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-tracked:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.08px
  body-sm:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'CursorGothic', sans-serif"
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
    fontFamily: "'CursorGothic', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  nav-link:
    fontFamily: "'CursorGothic', sans-serif"
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
  section: 80px

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
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
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
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 9px 17px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
  button-download:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 44px
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-mega}"
    padding: 80px
  ide-mockup-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 0
  ide-pane:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.body}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: 16px
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  comparison-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  timeline-pill-thinking:
    backgroundColor: "{colors.timeline-thinking}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  timeline-pill-grep:
    backgroundColor: "{colors.timeline-grep}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  timeline-pill-read:
    backgroundColor: "{colors.timeline-read}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  timeline-pill-edit:
    backgroundColor: "{colors.timeline-edit}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  timeline-pill-done:
    backgroundColor: "{colors.timeline-done}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  code-block:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: 20px
  pricing-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-featured:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 44px
  badge-pill:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  cta-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 96px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  footer:
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

Cursor's marketing site reads as a quietly-confident developer brand that believes in editorial calm over IDE-darkness. The base canvas is **warm cream** (`{colors.canvas}` — #f7f7f4) holding warm near-black ink (`{colors.ink}` — #26251e) for body and display alike. The single brand voltage is **Cursor Orange** (`{colors.primary}` — #f54e00) reserved for primary CTAs and the wordmark — used scarcely.

Type runs **CursorGothic** as the single sans family. Display sits at weight 400 with negative letter-spacing — a magazine-editorial voice rather than tech-bombastic. JetBrains Mono carries every code surface (and code surfaces are roughly half the page).

The brand's strongest visual signature is the **AI-timeline pill palette**: five pastel pills (peach `{colors.timeline-thinking}`, mint `{colors.timeline-grep}`, blue `{colors.timeline-read}`, lavender `{colors.timeline-edit}`, gold `{colors.timeline-done}`) marking AI-action stages inside in-product timeline visualizations. Used only in product UI — never as system action colors.

**Key Characteristics:**
- Warm cream canvas, not white. Ink is warm (#26251e), not pure black.
- Single CTA color: `{colors.primary}` (Cursor Orange #f54e00). Used scarcely.
- Display weight stays at 400 — never bold. Magazine voice.
- AI timeline pastels: 5 dedicated tokens for in-product agent action stages.
- Compact 8px CTA radius — developer dialect.
- Hairline-only depth; no drop shadows.
- 80px section rhythm.

## Colors

### Brand & Accent
- **Cursor Orange** (`{colors.primary}` — #f54e00): Primary CTA pills, wordmark, hero accent. Used scarcely.
- **Cursor Orange Active** (`{colors.primary-active}` — #d04200): Press state.

### Surface
- **Canvas** (`{colors.canvas}` — #f7f7f4): Warm cream page floor.
- **Canvas Soft** (`{colors.canvas-soft}` — #fafaf7): IDE-pane background inside mockups.
- **Surface Card** (`{colors.surface-card}` — #ffffff): Pure white card surface — slight contrast against the cream canvas.
- **Surface Strong** (`{colors.surface-strong}` — #e6e5e0): Badges, tag pills.

### Hairlines
- **Hairline** (`{colors.hairline}` — #e6e5e0): 1px divider.
- **Hairline Soft** (`{colors.hairline-soft}` — #efeee8): Lighter divider.
- **Hairline Strong** (`{colors.hairline-strong}` — #cfcdc4): Stronger panel outline.
- **Hairline Control** (`{colors.hairline-control}` — #8f8c82): **Prescribed, not extracted.** The three hairlines above are real extracted values and all three are decorative only: the strongest of them reaches 1.48:1 on `{colors.canvas}`, far below the 3:1 WCAG needs for a boundary that carries meaning. Use `{colors.hairline-control}` (3.13:1 on canvas) for any boundary that is the *only* indicator of a control — text-input outlines, secondary-button edges, checkbox and radio frames. Keep `{colors.hairline}` and `{colors.hairline-soft}` for dividers and card outlines, where the white-on-cream surface shift already carries the edge.

### Text
- **Ink** (`{colors.ink}` — #26251e): Display, body emphasis. Warm near-black.
- **Body** (`{colors.body}` — #5a5852): Default running-text.
- **Body Strong** (`{colors.body-strong}` — #26251e): Same as ink.
- **Muted** (`{colors.muted}` — #807d72): Sub-titles.
- **Muted Soft** (`{colors.muted-soft}` — #a09c92): Disabled text.
- **Muted Accessible** (`{colors.muted-accessible}` — #6e6b62): **Prescribed, not extracted.** The real `{colors.muted}` measures 3.84:1 on `{colors.canvas}` and 4.12:1 on `{colors.surface-card}` — it fails AA for body-size secondary text. `{colors.muted-accessible}` is the parallel accessible tone (4.96:1 on canvas, 5.33:1 on card) for secondary text below 18.66px. Keep `{colors.muted}` for 24px+ labels and for `{typography.caption-uppercase}` set at 18px or larger, where 3:1 applies.
- **On Primary** (`{colors.on-primary}` — #ffffff): White text on Cursor Orange.

### Focus
- **Focus** (`{colors.focus}` — #26251e): **Prescribed, not extracted** — no focus ring was observable on the captured surfaces. The ring is the brand's own warm ink, not a chromatic colour: Cursor's one voltage is already spent on the CTA, and an orange ring sits at 1.34:1 on an orange button. Ink measures 14.33:1 on `{colors.canvas}`, 15.38:1 on `{colors.surface-card}`, 12.19:1 on `{colors.surface-strong}` and 4.37:1 on `{colors.primary}` — it clears 3:1 on every light surface this file defines, the orange CTA included.
- **Focus On Dark** (`{colors.focus-on-dark}` — #f7f7f4): **Prescribed.** The cream ring for the two ink-surfaced components (`pricing-tier-featured`, `button-download`), where the ink ring would vanish at 1.0:1. Measures 14.33:1 on `{colors.ink}`.

### Timeline (AI-action signature)
- **Thinking** (`{colors.timeline-thinking}` — #dfa88f): Peach. Used inside in-product agent timeline only.
- **Grep** (`{colors.timeline-grep}` — #9fc9a2): Mint.
- **Read** (`{colors.timeline-read}` — #9fbbe0): Pastel blue.
- **Edit** (`{colors.timeline-edit}` — #c0a8dd): Lavender.
- **Done** (`{colors.timeline-done}` — #c08532): Warm gold.

### Semantic
- **Success** (`{colors.semantic-success}` — #1f8a65): Confirmation indicators.
- **Error** (`{colors.semantic-error}` — #cf2d56): Validation errors.

## Typography

### Font Family
**CursorGothic** is the licensed display + body family. Fallback: `system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif`. Code surfaces switch to **JetBrains Mono**.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-mega}` | 72px | 400 | 1.1 | -2.16px | Homepage hero h1 |
| `{typography.display-lg}` | 36px | 400 | 1.2 | -0.72px | Section heads |
| `{typography.display-md}` | 26px | 400 | 1.25 | -0.325px | Sub-section heads |
| `{typography.display-sm}` | 22px | 400 | 1.3 | -0.11px | Card group titles |
| `{typography.title-md}` | 18px | 600 | 1.4 | 0 | Component titles |
| `{typography.title-sm}` | 16px | 600 | 1.4 | 0 | List labels |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default body |
| `{typography.body-tracked}` | 16px | 400 | 1.5 | 0.08px | Tracked editorial body |
| `{typography.body-sm}` | 14px | 400 | 1.5 | 0 | Footer body |
| `{typography.caption}` | 13px | 400 | 1.4 | 0 | Photo captions |
| `{typography.caption-uppercase}` | 11px | 600 | 1.4 | 0.88px | Section labels, timeline pill labels |
| `{typography.code}` | 13px | 400 | 1.5 | 0 | Code blocks — JetBrains Mono |
| `{typography.button}` | 14px | 500 | 1.0 | 0 | CTA pill labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Top-nav menu |

### Principles
- **Display weight stays at 400.** Magazine voice, never bold.
- **Negative letter-spacing on display only.** -0.11px to -2.16px tracking.
- **JetBrains Mono on every code surface.**

### Note on Font Substitutes
CursorGothic is licensed. Open-source substitute: **Inter** at weight 400 with letter-spacing -1.5%. Or **GT Sectra** for a more editorial feel.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.base}` 16px · `{spacing.md}` 20px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- **Section padding:** 80px.

### Grid & Container
- Max content width: ~1200px.
- Editorial body: 12-column grid.
- Feature card grids: 2-up at desktop for splits, 3-up for benefits.
- Footer: 5-column at desktop.

### Whitespace Philosophy
Generous editorial pacing — closer to a print magazine than a tech site. The cream canvas has plenty of breathing room; cards within bands sit close (16-24px gap).

## Elevation & Depth

The system uses **hairline-only depth**. No drop shadows, no elevation tiers. Cards float above the canvas via 1px hairlines and the slight white-on-cream contrast.

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `{colors.canvas}` (#f7f7f4) | Body bands, footer |
| Card | `{colors.surface-card}` (#ffffff) | Content cards |
| Hairline border | 1px `{colors.hairline}` | Card outlines, dividers |
| IDE pane | `{colors.canvas-soft}` (#fafaf7) | Inside IDE mockup cards |

### Decorative Depth
- **IDE-mockup cards** are the only "elevated" element. White card on cream canvas with internal pane structure mimicking the actual Cursor editor.
- **Timeline pastel pills** add chromatic depth without surface elevation.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Reserved |
| `{rounded.xs}` | 4px | Inline tags |
| `{rounded.sm}` | 6px | Compact rows |
| `{rounded.md}` | 8px | CTA buttons, form inputs |
| `{rounded.lg}` | 12px | Cards, IDE panes |
| `{rounded.xl}` | 16px | Larger feature cards (rare) |
| `{rounded.pill}` | 9999px | Timeline pills, badges |
| `{rounded.full}` | 9999px | Avatars (rare) |

### Focus Ring

**Prescribed, not extracted.** 2px solid `{colors.focus}` with a 2px offset in `{colors.canvas}` (or `{colors.surface-card}` when the control sits on a card), so the ring never touches the control's own edge. On the two ink-surfaced components the ring is `{colors.focus-on-dark}` with a 2px offset in `{colors.ink}`. The ring follows the control's own radius — `{rounded.md}` on buttons and inputs, `{rounded.pill}` on pills, `{rounded.lg}` on cards — so it stays inside the existing radius ladder rather than adding a value to it.

## Components

### Top Navigation

**`top-nav`** — Background `{colors.canvas}`, text `{colors.ink}`, height 64px. Layout: Cursor wordmark left, primary horizontal menu (Pricing / Features / Enterprise / Blog / Forum / Careers), Sign In + Download primary CTA right.

### Buttons

**`button-primary`** — The signature Cursor Orange CTA. Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}` (14px / 500), padding 10px × 18px, height 40px, rounded `{rounded.md}` (8px).

**`button-primary-active`** — Press state. Background `{colors.primary-active}`.

**`button-secondary`** — White card pill on cream canvas. Background `{colors.surface-card}`, text `{colors.ink}`, 1px `{colors.hairline-strong}` border.

**`button-tertiary-text`** — Inline ink text link.

**`button-download`** — Larger ink-canvas CTA. Background `{colors.ink}`, text `{colors.canvas}`, padding 12px × 20px, height 44px. Used for "Download for macOS" type CTAs.

### Hero & IDE Mockups

**`hero-band`** — Background `{colors.canvas}`, full-width display headline in `{typography.display-mega}` (72px / 400 / -2.16px), subhead in `{typography.body-md}`, two CTAs (`button-download` + `button-tertiary-text`), and a centered IDE-mockup card below the hero copy.

**`ide-mockup-card`** — A white card containing a multi-pane IDE mockup (sidebar + main editor + chat panel + terminal). Background `{colors.surface-card}`, rounded `{rounded.lg}` (12px), 1px `{colors.hairline}` border, no padding (panes fill the card edge-to-edge).

**`ide-pane`** — Individual IDE pane inside the mockup. Background `{colors.canvas-soft}`, text `{colors.body}` in `{typography.code}` (JetBrains Mono 13px), rounded `{rounded.md}` (8px), padding 16px.

### Cards

**`feature-card`** — Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.title-md}`, rounded `{rounded.lg}`, padding 24px. 1px `{colors.hairline}` border.

**`comparison-card`** — Side-by-side "Cursor vs other tools" card. Same surface and rounding; internally split into 2 columns.

**`testimonial-card`** — Quote card. Background `{colors.surface-card}`, text `{colors.body}`, rounded `{rounded.lg}`, padding 24px.

### AI Timeline (signature)

**`timeline-pill-thinking`** — Peach pill. Background `{colors.timeline-thinking}`, text `{colors.ink}`, type `{typography.caption-uppercase}` (11px / 600 / 0.88px tracking, uppercase), rounded `{rounded.pill}`, padding 4px × 10px. Marks "Thinking" stage in product timeline.

**`timeline-pill-grep`** — Mint pill. Same shape, background `{colors.timeline-grep}`. Marks "Grepping" stage.

**`timeline-pill-read`** — Pastel-blue pill. Background `{colors.timeline-read}`. Marks "Reading" stage.

**`timeline-pill-edit`** — Lavender pill. Background `{colors.timeline-edit}`. Marks "Editing" stage.

**`timeline-pill-done`** — Gold pill. Background `{colors.timeline-done}`, text `{colors.on-primary}` white. Marks "Done" stage.

### Code

**`code-block`** — Inline code block. Background `{colors.surface-card}`, text `{colors.ink}` in `{typography.code}`, rounded `{rounded.lg}`, padding 20px, 1px `{colors.hairline}` border.

### Pricing

**`pricing-tier-card`** — Background `{colors.surface-card}`, rounded `{rounded.lg}`, padding 32px, 1px `{colors.hairline}` border.

**`pricing-tier-featured`** — Featured tier inverts to ink. Background `{colors.ink}`, text `{colors.canvas}`. Same shape, dark inversion signals "highlighted" without colored ribbon.

### Forms & Tags

**`text-input`** — Background `{colors.surface-card}`, text `{colors.ink}`, rounded `{rounded.md}` (8px), padding 12px × 16px, height 44px.

**`badge-pill`** — Small uppercase pill. Background `{colors.surface-strong}`, text `{colors.ink}`, type `{typography.caption-uppercase}`, rounded `{rounded.pill}`, padding 4px × 10px.

### CTA / Footer

**`cta-band`** — Pre-footer "Try Cursor now" band. Background `{colors.canvas}`, centered display headline in `{typography.display-lg}`, single Cursor Orange CTA. 96px vertical padding.

**`footer`** — Closing footer. Background `{colors.canvas}`, text `{colors.body}`. 5-column link list. 64×48px padding.

**`footer-link`** — Background transparent, text `{colors.body}`, type `{typography.body-sm}`.

### States

Only `button-primary-active` (press) was observable on the captured static site. Every other state below is **prescribed** to match the brand's logic — ink ring for focus, `{colors.primary-active}` for press, `{colors.muted-soft}` for disabled ink — and was not extracted.

| Component | States | Notes |
|---|---|---|
| `top-nav` | default, hover, focus-visible | Nav links underline on hover; container itself has one state. |
| `nav-link` (in `top-nav`) | default, hover, focus-visible, selected, disabled | Selected = current section, `{colors.ink}` at weight 600; disabled = `{colors.muted-soft}`. |
| `button-primary` | default, hover, focus-visible, pressed, disabled, loading | Hover = `{colors.primary-active}` at 60% blend; pressed = `{colors.primary-active}`; disabled = `{colors.surface-strong}` bg with `{colors.muted-soft}` ink; loading = label holds, inline spinner. |
| `button-primary-active` | pressed only | Not a component — the documented press state of `button-primary`. |
| `button-secondary` | default, hover, focus-visible, pressed, disabled, loading | Hover = `{colors.canvas-soft}` fill; boundary uses `{colors.hairline-control}`. |
| `button-tertiary-text` | default, hover, focus-visible, pressed, disabled | Hover = underline only; no fill. |
| `button-download` | default, hover, focus-visible, pressed, disabled, loading | Ink surface, so focus uses `{colors.focus-on-dark}`. |
| `hero-band` | default only | Static band — one state. |
| `ide-mockup-card` | default only | Decorative mockup; not interactive. |
| `ide-pane` | default, selected | Selected = active pane, `{colors.surface-card}` fill. |
| `feature-card` | default, hover, focus-visible, selected | Hover lifts opacity on the card's own hairline; focusable only where the whole card is a link. |
| `comparison-card` | default only | Static content. |
| `testimonial-card` | default only | Static content. |
| `timeline-pill-thinking` | default, loading | Loading is its meaning — the pill is live while the agent thinks. |
| `timeline-pill-grep` | default, loading | Same. |
| `timeline-pill-read` | default, loading | Same. |
| `timeline-pill-edit` | default, loading | Same. |
| `timeline-pill-done` | default only | Terminal stage — one state. |
| `code-block` | default, hover | Hover reveals the copy control; the block itself is not focusable, the control is. |
| `pricing-tier-card` | default, hover, focus-visible, selected | Selected = chosen plan, 1px `{colors.hairline-control}` boundary. |
| `pricing-tier-featured` | default, hover, focus-visible, selected | Ink surface; focus uses `{colors.focus-on-dark}`. |
| `text-input` | default, hover, focus-visible, disabled, error | Boundary `{colors.hairline-control}`; error = 1px `{colors.semantic-error}` plus a message in `{typography.body-sm}` — colour is never the only error signal. |
| `badge-pill` | default only | Static label. |
| `cta-band` | default only | Static band. |
| `footer` | default only | Container. |
| `footer-link` | default, hover, focus-visible | Hover = `{colors.ink}`. |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or easing curve below was extracted from Cursor's own CSS; every value is the **Crisp** profile's shared block, chosen because this is a developer-tool and IDE identity, and stated here so the document is useful to build from rather than silent.

The Crisp reading of this brand: a state change should read as already done. Cursor's page is half code surfaces and the voice is editorial-calm, not energetic — so travel stays tiny (2–4px), there is no entrance choreography on first paint, and nothing overshoots. The one place motion carries meaning rather than polish is the AI timeline, where pill stages advance as the agent works.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, nav, cards, footer links) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`; `transform: translateY(-1px)` on cards only | Opacity only at `{motion.duration-reduced}`; the 1px lift is removed. |
| Press (`button-primary` → `{colors.primary-active}`) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`, `transform: scale(0.98)` | Scale removed; colour change is instant, no fade. |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Unchanged — the ring appears instantly, never animated away. |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(4px)` | Travel removed; cross-fade at `{motion.duration-reduced}`. |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` (drawer: `translateX`) | Travel removed; fade at `{motion.duration-reduced}`. |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}`. |
| Dropdown / nav menu open | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(-4px)` | Travel removed; fade at `{motion.duration-reduced}`. |
| Dropdown close | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-instant}` — already under the cap. |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Travel removed; fade at `{motion.duration-reduced}`. |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}`. |
| List enter (feature grid, pricing tiers, timeline pills) | `{motion.duration-base}`, stagger `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(4px)` | Stagger and travel removed; all items fade together at `{motion.duration-reduced}`. |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-reduced}`. |
| Loading (inline spinner, IDE-pane skeleton) | `{motion.duration-emphasis}` loop | linear (spinner) / `{motion.ease-standard}` (skeleton) | `transform: rotate()`; skeleton `opacity` 0.4 ↔ 1 | Loop frozen; a static indicator plus the text label remains. |
| AI-timeline stage advance | `{motion.duration-base}`, stagger `{motion.stagger-step}` | `{motion.ease-standard}` | `opacity` on the outgoing pill, `opacity` on the incoming pill | Cross-fade at `{motion.duration-reduced}`; stage text still changes, so the information survives. |

### Rules
- **Compositor properties only.** Never animate `width`, `height`, `top`, `left` or `margin` — `transform` and `opacity` carry every state change here.
- **Exit is faster than entrance.** Every pair above is `{motion.duration-fast}` out against `{motion.duration-base}` in.
- **Nothing animates on first paint** in a way that delays content. Hero copy and the IDE mockup are painted, not revealed.
- **No infinite animation** except the two loaders listed above. This brand has no ambient motion; do not add any.
- **Travel stays at or below 8px.** A Crisp tool reads as responsive, not as choreographed.

### `@media (prefers-reduced-motion: reduce)`

All travel (`translateX`, `translateY`) and all scale are removed; the element simply arrives at its final position. Every remaining fade runs at `{motion.duration-reduced}` (100ms), never longer. Loader loops freeze to a static indicator and keep their text label. Focus rings, colour changes and the AI-timeline stage *text* are unaffected, so no state or information is lost — only the movement is.

## Accessibility

**Contrast is measured; focus behaviour, tap targets and reduced-motion handling are prescribed** (no rendered page was available to verify geometry).

### Measured contrast — passes

| Pair | Ratio | Required |
|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 14.33:1 | 4.5:1 |
| `{colors.ink}` on `{colors.surface-card}` | 15.38:1 | 4.5:1 |
| `{colors.body}` on `{colors.canvas}` | 6.63:1 | 4.5:1 |
| `{colors.body}` on `{colors.canvas-soft}` | 6.80:1 | 4.5:1 |
| `{colors.muted-accessible}` on `{colors.canvas}` | 4.96:1 | 4.5:1 |
| `{colors.muted-accessible}` on `{colors.surface-card}` | 5.33:1 | 4.5:1 |
| `{colors.canvas}` on `{colors.ink}` (`pricing-tier-featured`, `button-download`) | 14.33:1 | 4.5:1 |
| `{colors.ink}` on every timeline pastel (peach / mint / blue / lavender) | 7.24:1 – 8.31:1 | 4.5:1 |
| `{colors.semantic-error}` on `{colors.canvas}` | 4.70:1 | 4.5:1 |
| `{colors.hairline-control}` on `{colors.canvas}` | 3.13:1 | 3.0:1 |

### Measured contrast — real failures, disclosed

These are extracted brand values. They are not corrected in place, because a falsified hex would make this document wrong. **The real Cursor palette fails WCAG AA at each of these points.**

| Pair | Ratio | Required | Status |
|---|---|---|---|
| `button-primary`: `{colors.on-primary}` white on `{colors.primary}` #f54e00 | 3.52:1 | 4.5:1 | **Fails AA for 14px button text.** The brand's signature CTA is the failure. Passes AA Large (3:1) only at 24px+, or 18.66px+ at weight 700 — and this brand forbids bold. |
| `timeline-pill-done`: white on `{colors.timeline-done}` #c08532 | 3.16:1 | 4.5:1 | **Fails AA.** The pill's 11px uppercase label gets no large-text exemption. `{colors.ink}` on the same gold measures 4.86:1 and passes. |
| `{colors.muted}` #807d72 on `{colors.canvas}` | 3.84:1 | 4.5:1 | Fails AA below 18.66px. Use `{colors.muted-accessible}` for body-size secondary text. |
| `{colors.muted}` #807d72 on `{colors.surface-card}` | 4.12:1 | 4.5:1 | Fails AA below 18.66px. Same remedy. |
| `{colors.muted-soft}` #a09c92 on `{colors.canvas}` | 2.55:1 | 4.5:1 | Disabled-text tone. WCAG exempts disabled controls; it must never carry live text. |
| `{colors.muted-soft}` #a09c92 on `{colors.surface-card}` | 2.74:1 | 4.5:1 | Same — disabled only. |
| `{colors.hairline-strong}` #cfcdc4 on `{colors.canvas}` | 1.48:1 | 3.0:1 | Decorative only. Not a control boundary. |
| `{colors.hairline}` #e6e5e0 on `{colors.canvas}` | 1.18:1 | 3.0:1 | Decorative divider only. |
| `{colors.hairline-soft}` #efeee8 on `{colors.canvas}` | 1.08:1 | 3.0:1 | Decorative divider only. |
| `{colors.surface-card}` #ffffff on `{colors.canvas}` | 1.07:1 | — | The white-on-cream card edge is not a perceptible boundary on its own; every card therefore needs its hairline, and any card that is a control needs `{colors.hairline-control}`. |

`{colors.semantic-success}` #1f8a65 measures 4.01:1 on `{colors.canvas}` — it fails AA for body text and is for 18.66px+ or for icons, not for running confirmation copy.

### Focus ring visibility, per surface

Prescribed. 2px `{colors.focus}` with a 2px offset (see Shapes → Focus Ring).

| Surface | Ring | Ratio against surface |
|---|---|---|
| `{colors.canvas}` #f7f7f4 | `{colors.focus}` | 14.33:1 |
| `{colors.canvas-soft}` #fafaf7 | `{colors.focus}` | 14.70:1 |
| `{colors.surface-card}` #ffffff | `{colors.focus}` | 15.38:1 |
| `{colors.surface-strong}` #e6e5e0 | `{colors.focus}` | 12.19:1 |
| `{colors.primary}` #f54e00 (CTA fill) | `{colors.focus}` | 4.37:1 |
| `{colors.ink}` #26251e (`pricing-tier-featured`, `button-download`) | `{colors.focus-on-dark}` | 14.33:1 |

Every ring clears the 3:1 minimum on the surface it is drawn on. Focus is `:focus-visible` only, so pointer users never see it; it is never suppressed with `outline: none` without a replacement.

### Tap targets

Prescribed, not verified — tap-target size cannot be measured from a document. `button-primary` and `text-input` are documented at 40px and 44px height; 44 × 44px is the floor for every touch target, so `button-primary` needs 4px of additional touch padding (not visual height) on mobile. `badge-pill` and the timeline pills are not interactive and are exempt. Footer links at `{typography.body-sm}` need 44px row spacing on mobile.

### Reduced motion

See Motion & Animation → `@media (prefers-reduced-motion: reduce)`. Travel and scale are removed, fades are capped at `{motion.duration-reduced}` (100ms), loaders freeze to a static indicator with their label, and no information is conveyed by movement alone.

### Other

- Colour is never the only signal: `text-input` errors pair `{colors.semantic-error}` with a text message, and timeline stages carry their stage name as text, not only their pastel.
- The timeline pastels are decorative stage markers with ink labels at 7.24:1–8.31:1; the pastels themselves are not required to meet a contrast threshold against the canvas.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (Cursor Orange) for primary CTAs and brand wordmark.
- Keep display weight at 400. The editorial voice depends on this.
- Use the cream `{colors.canvas}` page floor — never pure white.
- Render every code surface (inline, blocks, IDE panes) in JetBrains Mono.
- Use timeline pastels only inside in-product agent visualizations — never as system action colors.

### Don't
- Don't introduce a secondary brand action color. Cursor Orange is the only one.
- Don't drop display to bold weights (700+). Magazine voice depends on 400.
- Don't add drop shadows. Hairlines + ink-on-cream contrast carry the depth.
- Don't use timeline pastels on non-timeline UI. They're scoped to the agent timeline only.
- Don't extract a CTA color from a third-party widget (cookie consent, OneTrust). The brand's CTA is what appears on actual product CTAs.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 640px | Hero h1 72→32px; IDE mockup collapses to single pane preview; feature grid 1-up; nav hamburger. |
| Tablet | 640–1024px | Hero h1 56px; IDE mockup compresses; feature grid 2-up. |
| Desktop | 1024–1280px | Full hero h1 72px; full multi-pane IDE mockup; feature grid 3-up. |
| Wide | > 1280px | Content caps at 1200px. |

### Touch Targets
- Primary CTA at 40px visual height — below the 44 × 44px floor, so it needs 4px of touch padding on mobile (see Accessibility → Tap targets).
- Download CTA and `text-input` at 44px — at the floor.

### Collapsing Strategy
- Top nav switches to hamburger below 768px.
- IDE mockup multi-pane collapses to a single primary pane preview on mobile.
- Feature grid: 3-up → 2-up → 1-up.

## Iteration Guide

1. Focus on a single component at a time.
2. CTAs default to `{rounded.md}` (8px). Cards use `{rounded.lg}` (12px).
3. Variants live as separate entries inside `components:`.
4. Use `{token.refs}` everywhere — never inline hex.
5. Hover and focus states were never observable on the captured site; the Components → States table prescribes them. Label any further state you add as prescribed too.
6. CursorGothic 400 for display, 400/500/600 for body. JetBrains Mono on every code surface.
7. Cursor Orange stays scarce.
8. Timeline pastels stay scoped to in-product agent visualizations.

## Known Gaps

- CursorGothic is a licensed typeface; Inter is the substitute.
- Real animation timings were never measured. The Motion & Animation section is the prescribed **Crisp** profile, not extracted values; the actual timeline-pill entrance and IDE-pane reveal curves remain unknown.
- No focus ring was observable on the captured surfaces. `{colors.focus}` and `{colors.focus-on-dark}` are prescribed.
- `{colors.hairline-control}` and `{colors.muted-accessible}` are prescribed accessible parallels, not brand values. The real hairlines and the real `{colors.muted}` are documented as failing AA in Accessibility.
- Tap-target sizes, overlap and layout shift cannot be verified from a document; the 44px floor stated in Accessibility is a requirement, not a measurement.
- In-app surfaces (code editor, chat panel, agent timeline) only partially captured via marketing IDE mockups.
- Form validation states beyond focus not visible on captured surfaces.
