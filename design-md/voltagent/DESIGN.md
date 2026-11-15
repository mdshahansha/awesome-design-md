---
version: alpha
name: Voltagent-Inspired-design-analysis
description: An inspired interpretation of Voltagent's design language — a developer-focused AI agent engineering platform whose surface is an unrelenting near-black canvas broken only by a single electric-green brand accent, code-editor mockups inside the hero, and a precise grid of dark feature cards that read like a documentation site dressed as marketing.

colors:
  primary: "#00d992"
  primary-soft: "#2fd6a1"
  primary-deep: "#10b981"
  on-primary: "#101010"
  ink: "#f2f2f2"
  ink-strong: "#ffffff"
  body: "#bdbdbd"
  mute: "#8b949e"
  hairline: "#3d3a39"
  hairline-soft: "#b8b3b0"
  canvas: "#101010"
  canvas-soft: "#1a1a1a"
  canvas-text-soft: "#f5f6f7"
  # Focus ring. Not a new brand colour: both values are tones the palette
  # already owns, bound to the ring job the prose already assigns them.
  # `focus` is the primary-soft green the Colors section already names as the
  # "tooltip / focus indicator" tone. `focus-on-light` is the brand's own
  # on-primary near-black, needed because `ex-pricing-tier-featured` paints a
  # light fill on which the green ring collapses to 1.67:1. Measured ratios
  # are in the Accessibility section.
  focus: "#2fd6a1"
  focus-on-light: "#101010"

shadow:
  none: none
  glow: "0 0 15px rgba(92, 88, 85, 0.2)"
  modal: "0 20px 60px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(148, 163, 184, 0.1) inset"

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

typography:
  display-xl:
    fontFamily: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif
    fontSize: 60px
    fontWeight: 400
    lineHeight: 60px
    letterSpacing: -0.65px
  display-lg:
    fontFamily: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif
    fontSize: 36px
    fontWeight: 400
    lineHeight: 40px
    letterSpacing: -0.9px
  display-md:
    fontFamily: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif
    fontSize: 24px
    fontWeight: 700
    lineHeight: 32px
    letterSpacing: -0.6px
  display-sm:
    fontFamily: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
  eyebrow-mono:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 20px
    letterSpacing: 2.52px
  eyebrow-uppercase:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: 0.45px
  body-lg:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
  body-md:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 26px
  body-md-strong:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
  body-sm:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 23px
  caption:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  caption-strong:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
  code:
    fontFamily: SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace
    fontSize: 13px
    fontWeight: 400
    lineHeight: 18px
  code-strong:
    fontFamily: SFMono-Regular, Menlo, Monaco, Consolas, monospace
    fontSize: 13px
    fontWeight: 550
    lineHeight: 16px
  button-md:
    fontFamily: Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 40px
  5xl: 48px
  6xl: 64px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.3xl}"
  nav-link:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-outline-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-ghost-green:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-pill-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  text-input:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  card-feature:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.2xl}"
  card-feature-emphasized:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  code-mockup:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  code-inline-chip:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.canvas-text-soft}"
    typography: "{typography.code}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.5xl} {spacing.3xl}"
  content-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.5xl} {spacing.3xl}"
  green-divider-band:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.4xl} {spacing.3xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.2xl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.2xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.2xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.2xl}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.2xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    shadow: "{shadow.modal}"
    rounded: "{rounded.md}"
    padding: "{spacing.2xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    shadow: "{shadow.glow}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Voltagent is an AI agent engineering platform built for developers, and the brand wears that audience proudly: a near-black `{colors.canvas}` (`#101010`) page background that runs edge-to-edge with no light-mode counterpart, a single electric-green accent (`{colors.primary}` `#00d992`) reserved for CTAs, status pills, and the brand lightning glyph, and a typography system that pairs sentence-case Inter with SF Mono for inline code and command snippets. The whole page reads like polished documentation that decided to also sell something.

The decorative system is restrained. There is no gradient mesh, no atmospheric backdrop, no illustration suite. Instead, the brand uses small typographic moments — a green code chip (`npx voltagent ...`), a 3-px outlined feature card sitting against the same near-black canvas, a green hairline divider between section bands — to mark its identity. The result is a page that feels engineered: every card has a hairline border, every snippet has a copy-to-clipboard button, every metric is rendered in a numeric monospace.

Type stays calm. Hero display sits at 60 px in regular weight with `-0.65 px` tracking — not a billboard headline, more like a documentation H1. Section headings step down to 36 px / 24 px in similar weights. Body copy is 16 px Inter at line-height 1.65 for the kind of legibility long-form devs expect. Uppercase eyebrows are common — `EVERYTHING YOU NEED` style mono-cap labels above section headlines — and they use Inter at weight 600 with wide positive tracking (`2.52 px` at 14 px).

**Key Characteristics:**
- A single electric-green accent `{colors.primary}` (`#00d992`) carries every CTA, every status pill, and the brand's lightning logo. No second accent.
- Dark canvas (`{colors.canvas}` `#101010`) is the only page surface — there is no light-mode rhythm; the entire site reads as one continuous dark surface broken by feature-card boundaries.
- Hairline-bordered feature cards (`{colors.hairline}` `#3d3a39`, 1 px solid) are the brand's primary chrome — no shadows, no fills, just precise hairline rectangles.
- A signature dashed-border accent (`1px dashed rgba(79, 93, 117, 0.4)`) appears between sections as a quiet rhythm cue — the brand's only ornamental line.
- Inter + SF Mono pair carries every typographic role. SF Mono is reserved for code blocks, inline command snippets, and metric counters.
- Buttons are tight 6 px rounded rectangles (not pills); only inline status tags use the 9999 px full pill.

## Colors

### Brand & Accent
- **Electric Green** (`{colors.primary}` — `#00d992`): The single brand accent. Every primary CTA, every status pill, every "live" indicator, the brand's lightning glyph itself. Reserved.
- **Primary Soft** (`{colors.primary-soft}` — `#2fd6a1`): A slightly more muted green used inside button-ghost variants and tooltip / focus indicators.
- **Primary Deep** (`{colors.primary-deep}` — `#10b981`): The darker green used for inline link colour in body copy.

### Surface
- **Canvas** (`{colors.canvas}` — `#101010`): The default near-black page background. The only surface mode in the brand's marketing system.
- **Canvas Soft** (`{colors.canvas-soft}` — `#1a1a1a`): A slightly lighter dark fill used inside code blocks and form inputs to mark them visually distinct against the canvas.
- **Hairline** (`{colors.hairline}` — `#3d3a39`): 1 px solid borders — feature cards, buttons, dividers between rows. The brand's universal "edge" colour. **This is an extracted value and it fails WCAG non-text contrast on both of the brand's own grounds: 1.69:1 on `{colors.canvas}` and 1.54:1 on `{colors.canvas-soft}`, against the 3.0:1 a component boundary needs.** Treat it as decoration — card edges, row rules, section dividers — not as the only boundary of an interactive control.
- **Hairline Soft** (`{colors.hairline-soft}` — `#b8b3b0`): A lighter divider tint. Originally documented for rare on-light secondary contexts; it is also the palette's one boundary tone that clears 3.0:1 on dark (9.16:1 on `{colors.canvas}`, 8.38:1 on `{colors.canvas-soft}`), so it is the accessible boundary for any control whose border is its only edge — text inputs, outline buttons, selectable rows. No new token was added for this; the brand already owned a passing tone.

### Text
- **Ink** (`{colors.ink}` — `#f2f2f2`): Default text colour on the dark canvas — slightly off-white to reduce contrast strain.
- **Ink Strong** (`{colors.ink-strong}` — `#ffffff`): Pure-white text for hero headlines and high-emphasis copy.
- **Body** (`{colors.body}` — `#bdbdbd`): Secondary text — supporting copy, body paragraphs in long-form sections.
- **Mute** (`{colors.mute}` — `#8b949e`): Lowest-priority on-dark text — captions, fine print, footer secondary lines.
- **Canvas Text Soft** (`{colors.canvas-text-soft}` — `#f5f6f7`): Used inside code mockups to keep code colour just slightly cooler than the surrounding body text.

### Semantic
The brand doesn't surface a separate error / warning palette in its public marketing pages — the underlying Docusaurus default semantic palette exists in the design system but is reserved for in-product / docs contexts. Validation cues on the marketing surface use the primary green for success and a muted body grey for missing states.

## Typography

### Font Family
Two faces carry the system:
1. **Inter** for every display, body, button, and link role. Weights 400 / 500 / 600 / 700 are the working set. Used with OpenType features `"calt"` and `"rlig"` enabled across the page so the geometric Inter ligatures and contextual alternates render correctly.
2. **SF Mono** (`SFMono-Regular` with Menlo / Monaco / Consolas / Liberation Mono fallbacks) for inline code, command snippets, terminal mockups, and the brand's numeric counters. Weights 400 / 549 / 550 / 700 are present — the unusual 549 / 550 sub-bold weight gives the mono a "slightly heavier than regular" voice for emphasis.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 60px | 400 | 60px | -0.65px | Hero headline ("AI Agent Engineering Platform"). |
| `{typography.display-lg}` | 36px | 400 | 40px | -0.9px | Section headlines. |
| `{typography.display-md}` | 24px | 700 | 32px | -0.6px | Sub-section / card-title displays. |
| `{typography.display-sm}` | 20px | 600 | 28px | 0 | Card titles in dense grids. |
| `{typography.eyebrow-mono}` | 14px | 600 | 20px | 2.52px | UPPERCASE eyebrow tags ("EVERYTHING YOU NEED"). |
| `{typography.eyebrow-uppercase}` | 18px | 600 | 28px | 0.45px | Larger uppercase eyebrows above hero subsections. |
| `{typography.body-lg}` | 18px | 400 | 28px | 0 | Lead paragraphs. |
| `{typography.body-md}` | 16px | 400 | 26px | 0 | Default body paragraph. |
| `{typography.body-md-strong}` | 16px | 600 | 24px | 0 | Bolded inline body. |
| `{typography.body-sm}` | 14px | 400 | 20px | 0 | Secondary body. |
| `{typography.body-sm-strong}` | 14px | 600 | 23px | 0 | Bold caption / pill-tag labels. |
| `{typography.caption}` | 12px | 400 | 16px | 0 | Fine print. |
| `{typography.caption-strong}` | 12px | 500 | 16px | 0 | Bold caption. |
| `{typography.code}` | 13px | 400 | 18px | 0 | Code blocks, inline command snippets. |
| `{typography.code-strong}` | 13px | 550 | 16px | 0 | Emphasised inline code (the SF Mono "almost-bold" weight). |
| `{typography.button-md}` | 16px | 600 | 24px | 0 | Button labels. |

### Principles
- **Inter regular at 60 px display** is the brand's calming counter to AI marketing's tendency to shout. The light tracking and modest weight read like documentation.
- **Two-face contrast carries the technical voice.** Inter for narrative; SF Mono for anything that could be typed at a terminal.
- **Uppercase eyebrow with tracking is the brand's signature label style.** `2.52 px` at 14 px is the documented value.

### Note on Font Substitutes
- **Sans** — *Inter* is the brand's actual face; substitute is the brand itself when self-hosting is not available.
- **Mono** — *SF Mono* is Apple-system; *JetBrains Mono* or *Geist Mono* are the best free substitutes.

## Layout

### Spacing System
- **Base unit**: 4 px; small 5 / 6.4 px values appear inside code-mockup line-height compensation.
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 20 px · `{spacing.2xl}` 24 px · `{spacing.3xl}` 32 px · `{spacing.4xl}` 40 px · `{spacing.5xl}` 48 px · `{spacing.6xl}` 64 px.
- **Section padding**: hero + content bands use `{spacing.5xl}` 48 px top/bottom.
- **Card interior padding**: feature cards sit at `{spacing.2xl}` 24 px.

### Grid & Container
- Marketing container centres at roughly 1200 – 1400 px; content stays edge-to-edge in colour with horizontal gutters of `{spacing.3xl}` on desktop.
- Feature-card grids: 2-up to 3-up at desktop, 1-up at mobile.

Breakpoints, touch targets, collapsing and image behaviour now live in their own top-level `## Responsive Behavior` section, moved verbatim out of this one.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | `{shadow.none}` — no shadow, no border. | Full-bleed bands. |
| Level 1 — Hairline | 1 px solid `{colors.hairline}` border on `{colors.canvas}`. | Default for every feature card and button. |
| Level 2 — Inset Glow | `{shadow.glow}` — `0 0 15px rgba(92, 88, 85, 0.2)` subtle outer glow. | Hovering / featured cards. |
| Level 3 — Modal Stack | `{shadow.modal}` — heavy drop + inset ring. | Modal / dialog surfaces in-product. |

The ladder is expressed two ways on purpose, and the seam is worth naming: Levels 0–1 are the marketing surface and are **border-only**, which is what the Don'ts enforce; Levels 2–3 are **shadow-only** and belong to in-product and overlay chrome (`ex-modal-card`, `ex-toast`). No single element mixes a hairline with a drop shadow. Note that Level 1 carries the whole marketing elevation system on a 1.69:1 hairline over a card fill identical to the page (`card-feature` paints `{colors.canvas}` on a `{colors.canvas}` band, a 1.00:1 step), so the only thing separating a card from the page is a boundary below threshold. See Accessibility.

### Decorative Depth
- Hairline cards on dark canvas — the brand's only true elevation mode.
- A 2 px solid `{colors.primary}` green border occasionally marks "featured" or "active" status on a card.
- A 1 px dashed `rgba(79, 93, 117, 0.4)` divider sits between section bands as a quiet rhythm cue.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed bands. |
| `{rounded.xs}` | 4px | Smallest inline pills and icon chips. (Inline code chips use `{rounded.sm}`, as `code-inline-chip` binds.) |
| `{rounded.sm}` | 6px | Default button and input radius. |
| `{rounded.md}` | 8px | Card chrome, code-block chrome. |
| `{rounded.pill}` | 9999px | Inline status tags ("Live", "Beta"). |
| `{rounded.full}` | 9999px | Circular icon containers. |

## Components

### Buttons

**`button-primary`** — the electric-green CTA.
- Background `{colors.primary}`, text `{colors.on-primary}` (near-black), label `{typography.button-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.sm}` 6 px.

**`button-outline-on-dark`** — the hairline-on-dark secondary button.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` border, same typography / padding / shape.

**`button-ghost-green`** — text-only with green label, for tertiary actions.
- Background `{colors.canvas}`, text `{colors.primary-soft}`, no border.

**`button-pill-tag`** — the inline pill for category tags / status labels.
- Background `{colors.canvas}`, text `{colors.ink}`, hairline border, body in `{typography.body-sm}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.pill}` 9999 px.

### Cards & Containers

**`card-feature`** — the default feature card.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` border, padding `{spacing.2xl}`, shape `{rounded.md}` 8 px. The brand's most-repeated card chrome.

**`card-feature-emphasized`** — the same card with a 3 px hairline border for emphasis.
- Same chrome as `card-feature` with 3 px solid `{colors.hairline}`.

**`code-mockup`** — the dark code-editor card with copy-to-clipboard affordance.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, body in `{typography.code}` (SF Mono 13 px), padding `{spacing.xl}`, shape `{rounded.md}`.

**`code-inline-chip`** — the inline command snippet pill.
- Background `{colors.canvas-soft}`, text `{colors.canvas-text-soft}`, body in `{typography.code}`, padding `{spacing.xxs} {spacing.sm}`, shape `{rounded.sm}`.

### Inputs & Forms

**`text-input`** — the standard text input on dark.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, body in `{typography.body-sm}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.sm}` 6 px.

### Navigation

**`nav-bar`** — the sticky top nav on dark.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.3xl}`.

**`nav-link`** — link items in nav.
- Text `{colors.body}`, set in `{typography.body-sm}`.

**`footer`** — the dark footer band.
- Background `{colors.canvas}`, text `{colors.body}`, padding `{spacing.4xl} {spacing.3xl}`. Body in `{typography.body-sm}`.

### Signature Components

**`hero-band`** — the dark hero band with the 60-px Inter headline.
- Background `{colors.canvas}`, text `{colors.ink}` (with the headline at `{colors.ink-strong}` white), padding `{spacing.5xl} {spacing.3xl}`. Headline in `{typography.display-xl}` (60 px / weight 400 / `-0.65 px` tracking). Eyebrow above headline in `{typography.eyebrow-mono}` (uppercase, tracked).

**`content-band`** — the standard content band hosting feature grids.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.5xl} {spacing.3xl}`. Section headline in `{typography.display-lg}`.

**`green-divider-band`** — a thin green-glow band that occasionally separates major sections.
- Background `{colors.canvas}`, 2 px solid `{colors.primary}` top/bottom border. The brand's only chromatic divider.

### Interaction States

Every state below is a **paint-only** change plus the shared focus ring — no travel, no scale. That is a deliberate reading of a brand whose own Don'ts forbid shadows on cards and reserve the green for CTAs: on a near-monochrome dark surface the hover state *is* a border or fill shift, and inventing a scale pop to look animated would contradict the brand. Property, duration and easing for each are in Motion & Animation.

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.primary}` fill, `{colors.on-primary}` label | fill steps to `{colors.primary-soft}` | 2 px `{colors.focus}` ring, 2 px offset on `{colors.canvas}` | fill steps to `{colors.primary-deep}` | fill at 40 % opacity, label `{colors.mute}`, `cursor: not-allowed` | label opacity 0; `{colors.on-primary}` spinner centred; button keeps its measured size | n/a — not a toggle | n/a — form-level, shown on the field |
| `button-outline-on-dark` | `{colors.canvas}` fill, 1 px `{colors.hairline-soft}` border | border to `{colors.ink}` | 2 px `{colors.focus}` ring, 2 px offset | border to `{colors.primary}` | border + label to `{colors.mute}` at 50 % | spinner replaces label, border held | n/a | n/a |
| `button-ghost-green` | `{colors.primary-soft}` label, no border | label to `{colors.primary}` | 2 px `{colors.focus}` ring, 2 px offset | label to `{colors.primary-deep}` | label `{colors.mute}` | spinner in `{colors.primary-soft}` | n/a | n/a |
| `button-pill-tag` | `{colors.canvas}` fill, `{colors.hairline-soft}` border | border to `{colors.ink}` | 2 px `{colors.focus}` ring, 2 px offset | border to `{colors.primary}` | label `{colors.mute}`, border `{colors.hairline}` | n/a — static label | 2 px `{colors.primary}` border marks the chosen tag | n/a |
| `text-input` | `{colors.canvas-soft}` fill, 1 px `{colors.hairline-soft}` border | border to `{colors.ink}` | 2 px `{colors.focus}` ring, 2 px offset, border held | caret visible, border `{colors.primary}` | fill `{colors.canvas}`, border `{colors.hairline}`, text `{colors.mute}`, `readonly` | trailing spinner in `{colors.primary-soft}`, field locked | n/a — single field | 1 px `{colors.ink-strong}` border plus a `{typography.caption}` message in `{colors.ink}`; the brand ships no red, see Known Gaps |
| `card-feature` | `{colors.canvas}` fill, 1 px `{colors.hairline}` edge | adds `{shadow.glow}`; edge to `{colors.hairline-soft}` | 2 px `{colors.focus}` ring, 2 px offset — only when the card is a link | edge to `{colors.primary}` | whole card at 50 % opacity, pointer events off | skeleton rows in `{colors.canvas-soft}` | 2 px `{colors.primary}` edge (`card-feature-emphasized` chrome) | n/a |
| `nav-link` | `{colors.body}` | `{colors.ink}` | 2 px `{colors.focus}` ring, 2 px offset | `{colors.primary-soft}` | `{colors.mute}` | n/a | current route in `{colors.ink}` with a 2 px `{colors.primary}` underline | n/a |
| `ex-app-shell-row` | `{colors.canvas}` fill | fill to `{colors.canvas-soft}` | 2 px `{colors.focus}` ring, inset 2 px (row is flush to the rail) | fill `{colors.canvas-soft}`, label `{colors.ink-strong}` | label `{colors.mute}` | n/a | 2 px `{colors.primary}` `activeIndicator` on the leading edge | n/a |
| `code-mockup` | `{colors.canvas}` fill, 1 px `{colors.hairline}` | copy button becomes opaque | ring applies to the copy button, not the frame | copy button label to `{colors.primary}` | n/a — never disabled | n/a | n/a | n/a |
| `code-inline-chip` | `{colors.canvas-soft}` fill, `{colors.canvas-text-soft}` text | **two states only** — default and hover (text to `{colors.primary-soft}`). It is static inline typography, not a control, so it takes no focus, no pressed, no disabled, no loading, no selected and no error state. | — | — | — | — | — | — |
| `green-divider-band` | 2 px `{colors.primary}` rule | **one state only** — decorative, non-interactive. | — | — | — | — | — | — |

### Examples (illustrative)

> Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`). Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently. `TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.
- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).
- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).
- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.
- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`


## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or transition is recorded anywhere in the source material for this file, so every value below comes from the **Crisp** profile in `theme-audit/SPEC.md` section 5, used verbatim. Nothing here is an extracted fact; there is no extracted/prescribed seam in this file because there is nothing extracted to displace the profile.

Crisp is the right profile for this brand on SPEC's own assignment rule 2 — developer-tool identity. The evidence is in the file: an AI agent engineering platform for developers, code-editor mockups as the hero, copy-to-clipboard on every snippet, SF Mono carrying code and metrics, and a page the Overview itself calls "polished documentation that decided to also sell something." State changes should read as instant; there is no entrance choreography.

### Tokens

| Token | Value |
|---|---|
| `{motion.duration-instant}` | 60ms |
| `{motion.duration-fast}` | 100ms |
| `{motion.duration-base}` | 150ms |
| `{motion.duration-slow}` | 220ms |
| `{motion.duration-emphasis}` | 300ms |
| `{motion.ease-standard}` | cubic-bezier(0.2, 0, 0.2, 1) |
| `{motion.ease-enter}` | cubic-bezier(0, 0, 0.2, 1) |
| `{motion.ease-exit}` | cubic-bezier(0.4, 0, 1, 1) |
| `{motion.stagger-step}` | 20ms |
| `{motion.duration-reduced}` | 100ms |

### Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, nav links, cards) | `{motion.duration-fast}` | `{motion.ease-standard}` | `background-color`, `color`, `border-color` — paint only, no travel and no scale, which is what this near-monochrome brand's hover actually is | Unchanged. Nothing moves, so there is nothing to remove; the colour step still runs at `{motion.duration-fast}`. |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `background-color`, `border-color` | Unchanged — paint only. |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the 2 px `{colors.focus}` ring; `box-shadow` colour for the offset | Ring appears immediately, no fade. Visibility never depends on motion. |
| Page / route transition | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` only — no slide. Content is painted at final position on first frame, so nothing is delayed. | `opacity` cross-fade at `{motion.duration-reduced}`. |
| Modal / drawer open | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` plus `transform: translateY(8px) → none` (drawer: `translateX`) | `transform` dropped; `opacity` fade at `{motion.duration-reduced}`. |
| Modal / drawer close | `{motion.duration-fast}` | `{motion.ease-exit}` | same pair, reversed — exit is shorter than its entrance | `transform` dropped; `opacity` fade at `{motion.duration-reduced}`. |
| Dropdown / menu open | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` plus `transform: translateY(-4px) → none` | `transform` dropped; `opacity` at `{motion.duration-reduced}`. |
| Dropdown / menu close | `{motion.duration-instant}` | `{motion.ease-exit}` | same pair, reversed | `opacity` at `{motion.duration-reduced}`. |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` plus `transform: translateY(12px) → none` | `transform` dropped; `opacity` at `{motion.duration-reduced}`. |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | same pair, reversed | `opacity` at `{motion.duration-reduced}`. |
| List / card-grid enter | `{motion.duration-base}` per item, `{motion.stagger-step}` 20ms between items | `{motion.ease-enter}` | `opacity` plus `transform: translateY(6px) → none`; stagger caps at 6 items, then the rest arrive together | Stagger and `transform` both dropped; the whole grid fades in once at `{motion.duration-reduced}`. |
| List / card-grid exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` plus `transform: translateY(4px)` | `transform` dropped; `opacity` at `{motion.duration-reduced}`. |
| Loading (button spinner, inline `{colors.primary-soft}` spinner) | 700ms per revolution, infinite — the one permitted infinite animation | `linear` | `transform: rotate()` only | Rotation frozen. The spinner is replaced by a static `{colors.primary-soft}` glyph and the accessible status text; progress is announced, not animated. |
| Loading (skeleton rows in `{colors.canvas-soft}`) | `{motion.duration-emphasis}`, infinite alternate | `{motion.ease-standard}` | `opacity` 0.4 ↔ 1 | Pulse frozen at `opacity: 0.7`. |

### Rules this file follows

- Animate `transform` and `opacity` only. The brand's state changes are paint changes — `background-color`, `color`, `border-color`, `box-shadow` — which are permitted because they trigger no layout; this file never transitions a layout-driving property such as width, height, top, left or margin.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content: the hero, its 60 px headline and the code mockup are painted at final position and full opacity.
- The only infinite animations are the two loaders above. The brand ships no ambient motion — no gradient drift, no glow pulse — and should not acquire any; `{shadow.glow}` is a static hover shadow, not a breathing effect.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. Every translateY / translateX above
     resolves to none, and the list stagger collapses to zero so a grid
     arrives in one step. The spinner's rotate() and the skeleton pulse are
     frozen; the spinner becomes a static glyph beside its status text. */
  *, *::before, *::after {
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;  /* {motion.duration-reduced} */
    transform: none !important;
  }
  /* Kept: opacity fades, capped at {motion.duration-reduced} 100ms, and every
     paint-only state change — hover, press, selected and error all still read,
     because on this brand they were never motion to begin with. The focus ring
     is never faded or delayed in either mode. */
}
```

## Accessibility

Every ratio here was computed with WCAG 2.1 relative luminance from this file's own frontmatter hexes. Nothing in this section was rendered or screenshotted.

### Text contrast — all pass

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` `#f2f2f2` on `{colors.canvas}` `#101010` | 17.00:1 | 4.5 | Pass |
| `{colors.ink}` `#f2f2f2` on `{colors.canvas-soft}` `#1a1a1a` | 15.55:1 | 4.5 | Pass |
| `{colors.ink-strong}` `#ffffff` on `{colors.canvas}` | 19.03:1 | 4.5 | Pass |
| `{colors.body}` `#bdbdbd` on `{colors.canvas}` | 10.13:1 | 4.5 | Pass |
| `{colors.body}` `#bdbdbd` on `{colors.canvas-soft}` | 9.26:1 | 4.5 | Pass |
| `{colors.mute}` `#8b949e` on `{colors.canvas}` | 6.19:1 | 4.5 | Pass |
| `{colors.mute}` `#8b949e` on `{colors.canvas-soft}` | 5.66:1 | 4.5 | Pass |
| `{colors.canvas-text-soft}` `#f5f6f7` on `{colors.canvas-soft}` | 16.08:1 | 4.5 | Pass |
| `{colors.on-primary}` `#101010` on `{colors.primary}` `#00d992` | 10.28:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.primary-soft}` `#2fd6a1` | 10.20:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.primary-deep}` `#10b981` | 7.50:1 | 4.5 | Pass |
| `{colors.on-primary}` `#101010` on the `ex-pricing-tier-featured` light fill (`{colors.ink}` `#f2f2f2` used as a background) | 17.00:1 | 4.5 | Pass |

All three greens also clear the 3.0:1 non-text threshold on both grounds: `{colors.primary}` at 10.28:1 / 9.40:1, `{colors.primary-soft}` at 10.20:1 / 9.33:1, `{colors.primary-deep}` at 7.50:1 / 6.86:1 on `{colors.canvas}` / `{colors.canvas-soft}`. The brand has one accent, so there is no second signal colour hiding a failure.

### Disclosed failures — the brand's real hairline does not meet AA

These are extracted values and they are **not** corrected in place. They are stated here because that is the useful fact for anyone building on this document.

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.hairline}` `#3d3a39` on `{colors.canvas}` `#101010` | 1.69:1 | 3.0 | **Fail** — boundary, 44 % of threshold |
| `{colors.hairline}` `#3d3a39` on `{colors.canvas-soft}` `#1a1a1a` | 1.54:1 | 3.0 | **Fail** — boundary on surface, all tones |
| `{colors.canvas-soft}` `#1a1a1a` on `{colors.canvas}` `#101010` | 1.09:1 | 3.0 | **Fail** — the two surface layers are effectively one colour |

What this means in practice: **Voltagent's real site fails WCAG 2.1 SC 1.4.11 Non-text Contrast at every component boundary.** The brand's entire chrome is 1 px `#3d3a39` hairlines, and on `#101010` that edge sits at 1.69:1. Because `card-feature` also paints `{colors.canvas}` on a `{colors.canvas}` band, a feature card is separated from the page by nothing but that sub-threshold line — a user who cannot resolve a 1.69:1 edge cannot see where one card ends and the next begins. In a text input the same hairline is the only indication that there is a field to type into.

The remedy used here needs no new token, because the palette already owned a passing boundary tone. `{colors.hairline-soft}` `#b8b3b0` measures **9.16:1** on `{colors.canvas}` and **8.38:1** on `{colors.canvas-soft}`, so the Interaction States table draws every control whose border is its only edge — `text-input`, `button-outline-on-dark`, `button-pill-tag` — with `{colors.hairline-soft}`, and leaves `{colors.hairline}` to decorative edges and row rules. The `components:` bindings in the frontmatter are left exactly as extracted: they are facts about the real site, and re-pointing them silently would make this document describe a product that does not exist. Re-binding them for real is a brand-owner decision and is recorded under Needs approval in `theme-audit/reports/A78-voltagent.md`.

`{colors.hairline-soft}` is also the nearest passing value in the brand's own palette: no synthetic hex is needed. If the dashed `rgba(79, 93, 117, 0.4)` section divider and the Level-1 card edge are to stay at the extracted tone, they are defensible only as pure decoration conveying no information — SC 1.4.11 exempts a boundary that is not needed to identify a control or its state. That exemption does not cover the text input.

### Focus ring

No file in this collection defined a focus ring before this audit; this one now does, and both values are tones the palette already owned rather than new brand colours.

| Ring | Value | Drawn on | Ratio | Required | Result |
|---|---|---|---|---|---|
| `{colors.focus}` | `#2fd6a1` — the `{colors.primary-soft}` green the Colors section already names as the tooltip / focus-indicator tone | `{colors.canvas}` `#101010` | 10.20:1 | 3.0 | Pass |
| `{colors.focus}` | same | `{colors.canvas-soft}` `#1a1a1a` | 9.33:1 | 3.0 | Pass |
| `{colors.focus-on-light}` | `#101010` — the brand's own `{colors.on-primary}` near-black | the `ex-pricing-tier-featured` light fill `#f2f2f2` | 17.00:1 | 3.0 | Pass |

Geometry: **2 px solid ring, 2 px offset, drawn outside the control** so it is judged against the surface behind it, as WCAG 2.2 SC 2.4.13 Focus Appearance asks. The offset gap is the surface colour, not the control fill. One exception, stated in the states table: `ex-app-shell-row` sits flush against the sidebar rail and takes the same 2 px ring **inset** instead, where the ring is judged against the row's own `{colors.canvas}` fill — still 10.20:1.

Why two rings, when the brand is dark-only. The green ring is correct on every surface the marketing site renders. It is wrong on exactly one surface this file declares: `ex-pricing-tier-featured` paints a light `#f2f2f2` fill, and on that ground `{colors.focus}` collapses to **1.67:1** — below threshold. `{colors.primary}` is no better at 1.65:1 and `{colors.primary-deep}` reaches only 2.27:1, so no green in the palette can serve a light ground. Hence the second ring in the opposite polarity, per SPEC section 1. A light-mode counterpart to the marketing surface is still forbidden by the Don'ts; `focus-on-light` exists for the one illustrative light fill, not as the start of a light theme.

### Tap targets

Computed from the file's own tokens, not measured on a rendered page: `button-primary` is `{spacing.md}` 12 px of vertical padding plus the 24 px line-height of `{typography.button-md}`, so 48 px — clearing both the 24 px of WCAG 2.2 SC 2.5.8 (AA) and the 44 px of SC 2.5.5 (AAA). `button-pill-tag` uses `{spacing.xs}` 4 px of vertical padding on a 20 px line-height, giving 28 px: it clears AA but not AAA, which is acceptable for an inline tag only where it is not the sole means of performing the action. Actual rendered geometry is outside what this document can verify — see Known Gaps.

### Reduced motion

Honoured in full; the rule and the exact list of what is removed and what remains are in Motion & Animation. In short: all travel, all scale and the list stagger are removed, the two loaders are frozen, opacity fades are capped at `{motion.duration-reduced}` 100 ms, and every paint-only state change plus the focus ring is untouched — none of this brand's state information was ever carried by movement.

### Other notes

- No state in this file is signalled by colour alone where the colour is the only cue: `selected` pairs the green edge with a 2 px border mass change, and `error` pairs its border with a `{typography.caption}` message.
- The brand ships no red. The `error` state therefore borrows `{colors.ink-strong}` plus text, which is an honest limit of the palette rather than a design choice — see Known Gaps.
- `{typography.caption}` at 12 px is the smallest role. In `{colors.mute}` on `{colors.canvas}` it measures 6.19:1, so it passes AA for normal text at that size.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (`#00d992`) for every primary CTA, the lightning logo glyph, and live-status indicators. The green is the brand's centre of gravity.
- Use the dark `{colors.canvas}` (`#101010`) as the only page surface. There is no light-mode rhythm.
- Build cards with 1 px `{colors.hairline}` borders, not shadows. Hairlines on dark IS the brand's elevation system.
- Pair Inter (sentence-case) with SF Mono (inline code, command snippets). Every uppercase moment uses Inter at weight 600 with `2.52 px` tracking — not a separate mono.
- Use `{rounded.sm}` 6 px for buttons, `{rounded.md}` 8 px for cards, `{rounded.pill}` 9999 px only for inline status tags.
- Draw a control whose border is its only edge — text inputs, outline buttons, selectable rows — with `{colors.hairline-soft}` (9.16:1 on canvas), and keep `{colors.hairline}` for decorative edges and row rules. The extracted hairline is 1.69:1 and cannot be seen as a boundary.
- Give every interactive element the 2 px `{colors.focus}` ring at 2 px offset. It is the brand's own `{colors.primary-soft}` green, so a visible focus state costs the brand nothing.

### Don't
- Don't introduce a light-mode counterpart. The brand is dark-canvas only.
- Don't use the primary green as a body-text fill. It's CTA-only.
- Don't drop a soft drop-shadow on cards. The brand uses hairlines + occasional glow, never material shadows.
- Don't render the hero headline in heavy weight (700+). The brand's display is intentionally calm at weight 400.
- Don't animate a layout-driving property. State changes on this brand are paint changes — `background-color`, `color`, `border-color` — and anything that moves uses `transform` and `opacity` only; never width, height, top, left or margin.
- Don't add a scale pop or a springy reveal. This is a Crisp profile: state change reads as instant and there is no entrance choreography.
- Don't replace Inter or SF Mono with a different family — both faces are part of the brand's voice and pairing.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hero 60→32 px; cards 1-up; nav hamburger. |
| Tablet | 768–1023px | Cards 2-up; nav stays horizontal. |
| Desktop | ≥ 1024px | Full 3-up card grids. |

### Touch Targets
Buttons render at ~44 px tall (12 px vertical padding + 24 px line-height). Meet WCAG AAA at all breakpoints.

### Collapsing Strategy
Nav collapses to hamburger at mobile; the menu overlay keeps the same green CTA pinned at the bottom. Feature-card grids drop to 1-up; hero typography scales fluidly.

### Image Behavior
Code-editor mockups render as image-like cards with copy-to-clipboard affordances. No photography in the brand's marketing surface.

## Known Gaps

- **Motion is entirely prescribed.** No duration, easing curve, stagger or transition is recorded in this file's source material. The whole Motion & Animation section is the SPEC Crisp profile applied to this brand, labelled as such in its first line. Nothing in it should be cited as an observed Voltagent behaviour.
- **No semantic palette.** The brand surfaces no error, warning or success colour on its marketing pages — the Colors section says so explicitly, and the Docusaurus defaults it mentions are an in-product concern that was not extracted. The `error` state in the Interaction States table is therefore built from `{colors.ink-strong}` and a text message rather than a red, and `success` reuses `{colors.primary}`. A real error colour is a brand-owner decision, not something this document can invent.
- **Rendered geometry is unverifiable here.** Tap-target sizes are arithmetic from padding and line-height tokens; overlap, horizontal overflow, clipping, layout shift and frame rate need a live page and are not claimed anywhere in this file.
- **The dashed divider has no token.** `1px dashed rgba(79, 93, 117, 0.4)` appears twice in the prose as an extracted value but is an alpha composite over an unstated ground, so it is not expressible as a flat hex in `colors:` and no token was invented for it. Its measured contrast is therefore unknown.
- **Mono weight 549 is unexplained.** The Typography section records SF Mono weights 400 / 549 / 550 / 700. Only 550 is tokenised (`{typography.code-strong}`); 549 is almost certainly a variable-font artefact of the extraction rather than a designed step, but that is inference, not evidence.
- **Container width is approximate.** "Roughly 1200 – 1400 px" is as precise as the source gets; no exact max-width was extracted.
- **`{colors.hairline-soft}` has no extracted on-dark usage.** It was documented for "rare on-light secondary contexts". Using it as the accessible boundary on dark is this audit's re-scoping of an existing brand tone, not an observed behaviour — the visual consequence is a lighter, more visible card edge than the real site draws. Flagged for a brand owner under Needs approval.
- **The Examples block is illustrative.** Every `ex-*` entry was auto-derived by `scripts/derive-examples-block.mjs` to mirror a standard kit, not extracted from Voltagent. `ex-pricing-tier-featured`'s light fill in particular is a kit convention, and it is the only reason this dark-only brand needs a second focus ring at all.
