---
version: alpha
name: Webflow-Inspired-design-analysis
description: An inspired interpretation of Webflow's design language — a visual web development platform whose surface contrasts a deep near-black `#080808` primary against a generous white canvas, broken by a five-stop chromatic accent system (purple / pink / blue / orange / green) that maps to the brand's product categories, and anchored by the proprietary WF Visual Sans family used at restrained 500 / 600 weights with negative tracking.

colors:
  primary: "#080808"
  on-primary: "#ffffff"
  ink: "#080808"
  ink-strong: "#222222"
  body: "#363636"
  body-mid: "#5a5a5a"
  mute: "#898989"
  mute-soft: "#ababab"
  hairline: "#d8d8d8"
  canvas: "#ffffff"
  accent-purple: "#7a3dff"
  accent-pink: "#ed52cb"
  accent-blue: "#3b89ff"
  accent-blue-deep: "#006acc"
  accent-blue-info: "#146ef5"
  accent-orange: "#ff6b00"
  accent-green: "#00d722"
  accent-yellow: "#ffae13"
  accent-red: "#ee1d36"
  focus: "#080808"
  focus-on-dark: "#ffffff"

typography:
  display-xxl:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, -apple-system, sans-serif
    fontSize: 80px
    fontWeight: 600
    lineHeight: 83.2px
    letterSpacing: -0.8px
  display-xl:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 56px
    fontWeight: 600
    lineHeight: 58.24px
  display-lg:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 44.8px
    fontWeight: 600
    lineHeight: 46.6px
  display-md:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 500
    lineHeight: 41.6px
  display-sm:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 500
    lineHeight: 31.2px
  display-xs:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 500
    lineHeight: 28px
  eyebrow-uppercase:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 15px
    fontWeight: 500
    lineHeight: 19.5px
    letterSpacing: 1.5px
  eyebrow-uppercase-sm:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 12px
    fontWeight: 500
    lineHeight: 12px
    letterSpacing: 0.6px
  body-lg:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 28.8px
    fontWeight: 400
    lineHeight: 46.08px
    letterSpacing: -0.288px
  body-md:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 25.6px
    letterSpacing: -0.16px
  body-md-strong:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 25.6px
    letterSpacing: -0.16px
  body-sm:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 22.4px
  body-sm-strong:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 22.4px
  caption:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 12.8px
    fontWeight: 550
    lineHeight: 15.36px
  caption-mono:
    fontFamily: WFVisualSans-Mono, Inconsolata, ui-monospace, SFMono-Regular, Menlo, monospace
    fontSize: 12px
    fontWeight: 400
    lineHeight: 18px
  button-md:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 25.6px
    letterSpacing: -0.16px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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

motion:
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 500ms
  ease-standard: cubic-bezier(0.4, 0, 0.2, 1)
  ease-enter: cubic-bezier(0.2, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 40ms
  duration-reduced: 150ms

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    padding: "{spacing.lg} {spacing.3xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  button-text-arrow:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "{spacing.xl} 0"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  badge-info:
    backgroundColor: "{colors.accent-blue-info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  badge-info-soft:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-blue-info}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  card-feature:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  card-feature-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  card-pricing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  hero-band-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  content-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.3xl} {spacing.3xl}"
  category-card-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  category-card-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  category-card-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  category-card-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  category-card-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body-mid}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.3xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
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
    headerBackground: "{colors.canvas}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Webflow positions itself as the visual web development platform — the marketing surface reads as a confident professional product, not a tech startup. The default page is a generous white canvas (`{colors.canvas}`) with a deep near-black `{colors.primary}` (`#080808`) for the brand's primary CTA, typography, and ink. Around this restrained primary, the brand layers a five-stop chromatic accent system — `{colors.accent-purple}` `#7a3dff`, `{colors.accent-pink}` `#ed52cb`, `{colors.accent-blue}` `#3b89ff`, `{colors.accent-orange}` `#ff6b00`, `{colors.accent-green}` `#00d722` — each mapped to one of the platform's product categories (design, CMS, hosting, ecommerce, etc.). These accents appear as full-card fills inside the product-category grid, not as button colours; the brand's primary CTA stays near-black.

Type carries the second decisive voice. The proprietary `WF Visual Sans Variable` family carries every display, body, and label role at weight 500 / 600 — the brand never goes heavier than semibold, never lighter than regular. Hero display sits at 80 px / weight 600 / `-0.8 px` tracking — confident but not shouting. Uppercase eyebrows in 15 px weight 500 with `1.5 px` positive tracking mark every section header.

The shape system is restrained. Buttons take a tight `{rounded.sm}` 4 px radius — neither pill nor square; the brand reads as engineered. Cards step up to `{rounded.md}` 8 px. Pill (`{rounded.full}` 9999 px) is reserved for circular icon containers. Layered drop-shadows on featured cards add modest elevation but never feel material-heavy.

**Key Characteristics:**
- A two-colour conversion hierarchy — `{colors.primary}` near-black for every primary CTA, white-on-hairline for every secondary. Chromatic accents are used as full surface fills on category cards, never as button backgrounds.
- The brand's signature is its **five-stop chromatic category palette**: purple / pink / blue / orange / green, each tied to a product surface. Used at full saturation as card fills.
- Hero typography at 80 px weight 600 with `-0.8 px` tracking — restrained, confident, never billboard-loud.
- WF Visual Sans Variable is the single family; the brand uses no separate sans for body / display. WFVisualSans-Mono / Inconsolata appears only for technical captions.
- Tight `{rounded.sm}` 4 px button geometry; cards at `{rounded.md}` 8 px. The brand never uses pill CTAs.
- Layered multi-offset drop-shadows on featured cards — the brand's only elevation cue.

## Colors

### Brand & Accent
- **Ink Black** (`{colors.primary}` — `#080808`): The brand's primary conversion colour. Every primary CTA, every heading, every wordmark. Deeper than pure black to read as branded.
- **Accent Purple** (`{colors.accent-purple}` — `#7a3dff`): One of the five chromatic category accents — used for design / build product surfaces.
- **Accent Pink** (`{colors.accent-pink}` — `#ed52cb`): Magenta accent — used for animation / interaction product surfaces.
- **Accent Blue** (`{colors.accent-blue}` — `#3b89ff`): Bright cyan-blue — used for SEO / analytics product surfaces.
- **Accent Blue Deep** (`{colors.accent-blue-deep}` — `#006acc`): The deeper blue used for emphasis links.
- **Accent Blue Info** (`{colors.accent-blue-info}` — `#146ef5`): The badge-info blue.
- **Accent Orange** (`{colors.accent-orange}` — `#ff6b00`): Used for hosting / infrastructure product surfaces.
- **Accent Green** (`{colors.accent-green}` — `#00d722`): Used for ecommerce / status-success surfaces.
- **Accent Yellow** (`{colors.accent-yellow}` — `#ffae13`): Used for warning / collaboration product surfaces.
- **Accent Red** (`{colors.accent-red}` — `#ee1d36`): Used for error / destructive states.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): The default page background.
- **Hairline** (`{colors.hairline}` — `#d8d8d8`): 1 px solid borders — card chrome and divider lines. Extracted and frozen at 1.43:1 against `{colors.canvas}`, which is below the 3:1 WCAG 1.4.11 threshold, so it is scoped to **decorative** separation only: dividers, non-interactive card chrome, table rules.
- **Mute as accessible boundary** (`{colors.mute}` — `#898989`): where a 1 px line is the *only* boundary of an interactive control — `text-input`, `button-secondary` — draw it in `{colors.mute}`, which measures 3.5:1 against `{colors.canvas}` and clears 1.4.11. No new token is introduced for this; the palette already owns a passing tone. The existing `borderColor` bindings on those components stay as extracted (`{colors.hairline}`) — re-pointing them is a brand-owner decision, logged under Needs approval in the audit report.

### Focus
- **Focus Ring** (`{colors.focus}` — `#080808`): the brand's own near-black ink, reused as the focus ring on the white canvas and on all five chromatic category-card fills. Not a new brand colour.
- **Focus Ring on Dark** (`{colors.focus-on-dark}` — `#ffffff`): the counterpart ring for the brand's near-black signature surfaces (`card-feature-dark`, `hero-band-dark`), where the ink ring would sit at 1:1.

### Text
- **Ink** (`{colors.ink}` — `#080808`): Default text and headings.
- **Ink Strong** (`{colors.ink-strong}` — `#222222`): Near-black emphasis.
- **Body** (`{colors.body}` — `#363636`): Default body paragraph color.
- **Body Mid** (`{colors.body-mid}` — `#5a5a5a`): Mid-emphasis secondary text — footer lines, captions.
- **Mute** (`{colors.mute}` — `#898989`): Lower-priority text.
- **Mute Soft** (`{colors.mute-soft}` — `#ababab`): The lightest text role — placeholder text, fine print.

### Semantic
- **Info Blue** (`{colors.accent-blue-info}` — `#146ef5`): Info badge / notification.
- **Success Green** (`{colors.accent-green}` — `#00d722`): Success indicators.
- **Warning Yellow** (`{colors.accent-yellow}` — `#ffae13`): Warning states.
- **Error Red** (`{colors.accent-red}` — `#ee1d36`): Validation / destructive.

## Typography

### Font Family
A single proprietary family carries every typographic role: **WF Visual Sans Variable** (with `Arial` system fallback). Weights 400 / 500 / 550 / 600 are present; the brand never uses 700 / 800 / 900. A monospace variant — **WFVisualSans-Mono** with `Inconsolata` fallback — handles rare technical caption moments and code-style labels. OpenType features `"ss02"`, `"ss10"`, `"zero"` are enabled in the mono variant for the styled zero glyph.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 80px | 600 | 83.2px | -0.8px | Hero headline. |
| `{typography.display-xl}` | 56px | 600 | 58.24px | 0 | Sub-hero displays. |
| `{typography.display-lg}` | 44.8px | 600 | 46.6px | 0 | Section headlines. |
| `{typography.display-md}` | 32px | 500 | 41.6px | 0 | Card-cluster headlines. |
| `{typography.display-sm}` | 24px | 500 | 31.2px | 0 | Sub-section displays. |
| `{typography.display-xs}` | 20px | 500 | 28px | 0 | Inline display micro-headings. |
| `{typography.eyebrow-uppercase}` | 15px | 500 | 19.5px | 1.5px | UPPERCASE eyebrow tags above sections. |
| `{typography.eyebrow-uppercase-sm}` | 12px | 500 | 12px | 0.6px | Small uppercase metadata. |
| `{typography.body-lg}` | 28.8px | 400 | 46.08px | -0.288px | Lead paragraphs. |
| `{typography.body-md}` | 16px | 400 | 25.6px | -0.16px | Default body. |
| `{typography.body-md-strong}` | 16px | 500 | 25.6px | -0.16px | Bolded inline body. |
| `{typography.body-sm}` | 14px | 400 | 22.4px | 0 | Secondary body. |
| `{typography.body-sm-strong}` | 14px | 500 | 22.4px | 0 | Bold caption / nav-link. |
| `{typography.caption}` | 12.8px | 550 | 15.36px | 0 | Badge labels (the brand's signature 550 weight). |
| `{typography.caption-mono}` | 12px | 400 | 18px | 0 | Mono code captions. |
| `{typography.button-md}` | 16px | 500 | 25.6px | -0.16px | Button labels. |

### Principles
- **Weight ceiling at 600.** The brand never uses 700+. Confident, not loud.
- **Negative tracking at display sizes.** `-0.8 px` at 80 px, scaling through. Tight kerning is part of the voice.
- **Uppercase eyebrows mark every section.** 15 px / weight 500 / `1.5 px` positive tracking is the brand's signature label style.
- **Single family across the system.** No separate display vs body face. The variable axes do the work.

### Note on Font Substitutes
WF Visual Sans Variable is proprietary. Open-source substitutes:
- **Display + body** — *Inter* weights 400 / 500 / 600 with `font-feature-settings: "ss01"` enabled is the closest stylistic match.
- **Mono** — *Inconsolata* (the documented fallback) or *DM Mono*.

## Layout

### Spacing System
- **Base unit**: 4 px (with frequent 0.4 / 0.8 sub-multiples for fine padding).
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 20 px · `{spacing.2xl}` 24 px · `{spacing.3xl}` 32 px.
- **Section padding**: hero / content bands use `{spacing.3xl}` 32 px gutters with generous vertical spacing.
- **Card interior padding**: feature and pricing cards sit at `{spacing.3xl}` 32 px.

### Grid & Container
- Marketing container is wide (effectively edge-to-edge with `{spacing.3xl}` gutters).
- Category card grid: 2 / 3-up at desktop with mixed sizing (some larger feature cards span 2 columns).
- Pricing tier grid: 3-up at desktop, 1-up at mobile.


## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default bands. |
| Level 1 — Hairline | 1 px solid `{colors.hairline}` border on `{colors.canvas}`. | Default card chrome and input borders. |
| Level 2 — Layered Drop | Multi-stop layered shadow with subtle warm offsets — `0 84px 24px rgba(0,0,0,0), 0 54px 22px rgba(0,0,0,0.01), 0 30px 18px rgba(0,0,0,0.04), 0 13px 13px rgba(0,0,0,0.08), 0 3px 7px rgba(0,0,0,0.09)`. | Featured cards needing visible lift. |
| Level 3 — Layered Drop Strong | Deeper version of Level 2 with `0.12` final offset opacity. | Pricing / modal-level emphasis. |
| Level 4 — Heavy Modal | Extremely heavy multi-stop — `0 24px 24px rgba(0,0,0,0.26), 0 6px 13px rgba(0,0,0,0.29)` final stops. | Modal / dialog surfaces. |

### Decorative Depth
- The chromatic category cards (full-saturation purple / pink / blue / orange / green fills) provide visual depth through pure colour contrast against the white canvas.
- Layered shadow recipes are the brand's only true atmospheric effect — they're 5-stop drop-shadow stacks with very low individual opacities.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed bands. |
| `{rounded.xs}` | 2px | Tight inline pills. |
| `{rounded.sm}` | 4px | The brand's canonical button + badge + small-element radius. |
| `{rounded.md}` | 8px | Card chrome and feature / category cards. |
| `{rounded.full}` | 9999px | Circular icon containers only. |

### Border & Ring Ladder
- **Border width**: 1 px is the only stroke weight in the system; the brand draws no 2 px or heavier boundary.
- **Focus ring**: 2 px solid `{colors.focus}` (or `{colors.focus-on-dark}` on near-black surfaces), drawn **outside** the control with a 2 px offset, so the ring is judged against the surface behind the control rather than the control's own fill. Ring radius follows the control: `{rounded.sm}` + 2 px on buttons and inputs, `{rounded.md}` + 2 px on cards. No value in this ladder sits outside the radius scale.

## Components

### Buttons

**`button-primary`** — the canonical near-black CTA.
- Background `{colors.primary}` (`#080808`), text `{colors.on-primary}` white, label `{typography.button-md}` (16 px weight 500), padding `{spacing.md} {spacing.xl}`, shape `{rounded.sm}` 4 px.

**`button-secondary`** — the white outline CTA.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` border, same typography + padding + shape.

**`button-text-arrow`** — the underlined text-link CTA with arrow used in long-form sections.
- Background `{colors.canvas}`, text `{colors.ink}`, no border, body in `{typography.button-md}`, padding `{spacing.xl}` 0.

**`button-icon-circular`** — the circular icon button for carousel controls.
- Background `{colors.canvas}`, ink icon, shape `{rounded.full}`.

### Cards & Containers

**`card-feature`** — the canonical feature card on canvas.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, padding `{spacing.3xl}`, shape `{rounded.md}`. Often elevated to Level 2 shadow when featured.

**`card-feature-dark`** — the polarity-flipped feature card on near-black.
- Background `{colors.primary}`, text `{colors.on-primary}`, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`card-pricing`** — the pricing-tier card.
- Background `{colors.canvas}`, text `{colors.ink}`, hairline border, padding `{spacing.3xl}`, shape `{rounded.md}`. Layered shadow on the featured tier.

### Inputs & Forms

**`text-input`** — the canonical text input.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, body in `{typography.body-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.sm}`.
- The extracted `{colors.hairline}` border is the input's only boundary and measures 1.43:1 on `{colors.canvas}` — a real AA failure in the live brand. Build at `{colors.mute}` (3.5:1) where the control must be perceivable; see Accessibility.
- Placeholder text is the one role that uses `{colors.mute-soft}` (2.3:1 on canvas) — below AA, documented rather than fixed.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg} {spacing.3xl}`.

**`nav-link`** — link items inside `nav-bar`.
- Text `{colors.ink}`, set in `{typography.body-sm-strong}`.

**`footer`** — the footer band.
- Background `{colors.canvas}`, text `{colors.body-mid}`, padding `{spacing.3xl} {spacing.3xl}`. Body in `{typography.body-sm}`.

### Signature Components

**`hero-band`** — the white hero band.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.3xl}`. Headline in `{typography.display-xxl}` (80 px weight 600).

**`hero-band-dark`** — the polarity-flipped near-black hero band (used on some campaign pages).
- Background `{colors.primary}`, text `{colors.on-primary}`, same padding / headline scale.

**`content-band`** — the standard content band on canvas.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.3xl}`. Section headline in `{typography.display-lg}`.

**`category-card-purple`** — full-fill purple category card.
- Background `{colors.accent-purple}`, text white, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`category-card-pink`** — full-fill pink category card.
- Background `{colors.accent-pink}`, text white, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`category-card-blue`** — full-fill blue category card.
- Background `{colors.accent-blue}`, text white, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`category-card-orange`** — full-fill orange category card.
- Background `{colors.accent-orange}`, text white, padding `{spacing.3xl}`, shape `{rounded.md}`.
- **The real brand fails AA here.** White on `#ff6b00` measures 2.86:1. The card's own type is `{typography.display-md}` (32 px / 500), so the relaxed large-text threshold of 3:1 applies — and it still misses, by 0.14. This is an extracted binding, not a slip: the sibling `category-card-green` deliberately flips to ink text for the same reason, so the white-on-orange pairing is a documented brand decision. Left as extracted; the ink alternative (`{colors.primary}`, 7.01:1) is logged under Needs approval.

**`category-card-green`** — full-fill green category card (uses ink text for legibility against the lighter green).
- Background `{colors.accent-green}`, text `{colors.primary}` (ink), padding `{spacing.3xl}`, shape `{rounded.md}`.

**`badge-info`** + **`badge-info-soft`** — info badges in solid blue or soft outline.
- Filled: bg `{colors.accent-blue-info}` text white. Soft: bg canvas, text `{colors.accent-blue-info}`. Both at `{typography.caption}` (12.8 px weight 550) — the brand's signature 550-weight caption.

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

### Component States

Prescribed, not extracted: the source file documented no state styling. The treatments below are derived from the brand's own rules — near-black ink is the signal colour, 1 px is the only stroke weight, and the five accents are surface fills, never action colours.

| Component | States |
|---|---|
| `button-primary` | default · hover · focus-visible · active/pressed · disabled · loading |
| `button-secondary` | default · hover · focus-visible · active/pressed · disabled · loading |
| `button-text-arrow` | default · hover · focus-visible · active/pressed · disabled |
| `button-icon-circular` | default · hover · focus-visible · active/pressed · disabled |
| `text-input` | default · hover · focus-visible · disabled · error |
| `nav-link` | default · hover · focus-visible · selected (current section) |
| `nav-bar` | two states only: at rest and scrolled (hairline divider appears) |
| `card-feature`, `card-pricing`, `ex-pricing-tier` | default · hover · focus-visible · selected (chosen tier) |
| `card-feature-dark`, `hero-band-dark` | default · hover · focus-visible — ring drawn in `{colors.focus-on-dark}` |
| `category-card-purple` / `-pink` / `-blue` / `-orange` / `-green` | default · hover · focus-visible (whole card is a link) |
| `badge-info`, `badge-info-soft` | one state only — static labels, never interactive |
| `hero-band`, `content-band`, `footer` | no interactive states — static bands |
| `ex-toast` | default · loading (progress bar) · error (red accent rule) |
| `ex-data-table-cell` | default · hover (row) · selected (row) |

| State | Treatment |
|---|---|
| hover | Paint-only. Buttons shift fill to `{colors.ink-strong}` (primary) or border to `{colors.mute}` (secondary); cards raise Level 1 → Level 2 shadow. No travel, no scale. |
| focus-visible | 2 px `{colors.focus}` ring at 2 px offset — `{colors.focus-on-dark}` on near-black surfaces. Never suppressed, never replaced by a fill change alone. |
| active/pressed | Paint-only: fill darkens one ink step. The brand uses no scale pop. |
| disabled | 40 % opacity, pointer-events off. Exempt from contrast thresholds per WCAG 1.4.3. |
| loading | Label swaps for an indeterminate mono caption or a 16 px spinner in the button's own ink; the button keeps its measured width so nothing reflows. |
| selected | 1 px `{colors.primary}` boundary plus `{typography.body-sm-strong}` label; never an accent fill. |
| error | 1 px `{colors.accent-red}` boundary (4.32:1 on canvas) plus a `{typography.body-sm}` message in `{colors.accent-red}`. Colour is never the only error signal — the message carries it. |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No durations or easing curves were extracted from Webflow; every value below is the **Calm** profile block carried verbatim in `motion:`, chosen because the brand's own description is restrained and editorial — weight ceiling 600, no gradients, saturated colour confined to static card fills rather than interactive elements.

Only `transform` and `opacity` are animated for movement. Paint-only changes (`background-color`, `border-color`, `box-shadow`) are the brand's real hover signal on a near-monochrome surface and use the same duration tokens. Never animate `width`, `height`, `top`, `left` or `margin`.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav-link) | `{motion.duration-fast}` | `{motion.ease-standard}` | `background-color`, `border-color` | Unchanged — paint-only, no travel to remove |
| Hover (card lift) | `{motion.duration-base}` | `{motion.ease-standard}` | `box-shadow`, `opacity` | Shadow change only, instant |
| Press | `{motion.duration-instant}` | `{motion.ease-standard}` | `background-color` | Unchanged |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears instantly, no fade |
| Page / route transition | `{motion.duration-base}` out, `{motion.duration-fast}` in | `{motion.ease-exit}` out, `{motion.ease-enter}` in | `opacity` | Cross-fade at `{motion.duration-reduced}` |
| Modal / drawer open | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px) → 0` | Fade only at `{motion.duration-reduced}`, no translate |
| Modal / drawer close | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Fade only at `{motion.duration-reduced}` |
| Dropdown open / close | `{motion.duration-fast}` / `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px) → 0` | Fade only at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(12px) → 0` | Fade only at `{motion.duration-reduced}` |
| List / card-grid enter | `{motion.duration-base}`, `{motion.stagger-step}` per item | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px) → 0` | Fade in together at `{motion.duration-reduced}`, stagger 0 |
| List / card-grid exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-reduced}` |
| Loading (spinner, skeleton) | 1200 ms loop | linear | `transform: rotate`, `opacity` | Replaced by a static mono caption; no loop |
| Hero / section reveal on scroll | `{motion.duration-emphasis}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px) → 0` | Content renders at final position, no reveal |

Rules in force: every exit is shorter than its matching entrance; nothing animates on first paint in a way that delays content — the hero renders immediately and only secondary bands reveal on scroll; the loader is the one infinite animation and the brand carries no ambient motion.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale travel, the stagger on list enter,
     the scroll reveal, and the spinner's infinite rotation.
     Kept: opacity fades, capped at {motion.duration-reduced} = 150ms,
     and every paint-only state change (background, border, shadow),
     which carries no travel and stays at its own duration token. */
  *, *::before, *::after {
    transition-duration: 150ms !important;   /* {motion.duration-reduced} */
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
    transform: none !important;
  }
}
```

## Accessibility

Measured with WCAG 2.1 relative luminance from this file's own token values. Failures are stated, not hidden.

### Key pairs — passing

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` `#080808` on `{colors.canvas}` | 20.03:1 | 4.5:1 | Pass |
| `{colors.body}` `#363636` on `{colors.canvas}` | 12.08:1 | 4.5:1 | Pass |
| `{colors.body-mid}` `#5a5a5a` on `{colors.canvas}` | 6.9:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 20.03:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.accent-purple}` | 5.33:1 | 3.0:1 (32 px display) | Pass |
| `{colors.on-primary}` on `{colors.accent-pink}` | 3.15:1 | 3.0:1 (32 px display) | Pass |
| `{colors.on-primary}` on `{colors.accent-blue}` | 3.38:1 | 3.0:1 (32 px display) | Pass |
| `{colors.primary}` on `{colors.accent-green}` | 10.25:1 | 3.0:1 (32 px display) | Pass |
| `{colors.accent-red}` on `{colors.canvas}` | 4.32:1 | 4.5:1 | **Marginal fail** — error text at 4.32:1; use it as a boundary and pair with `{colors.body}` message text |
| `{colors.mute}` on `{colors.canvas}` as a **boundary** | 3.5:1 | 3.0:1 | Pass — the accessible boundary tone |

### Disclosed failures — extracted values, frozen

These are facts about the real brand, not defects in the document. Each is left at its extracted value.

- `{colors.hairline}` `#d8d8d8` on `{colors.canvas}` measures **1.43:1**, against the 3:1 required of a component boundary. The live brand fails WCAG 1.4.11 wherever this hairline is the only boundary of a control. Scoped to decoration here; `{colors.mute}` (3.5:1) is the build-time substitute.
- `{colors.mute}` `#898989` on `{colors.canvas}` measures **3.5:1**, against the 4.5:1 required of body text. Defensible only as a non-text boundary, or as text at 24 px+ where 3:1 applies. The brand fails AA for this grey at body size.
- `{colors.mute-soft}` `#ababab` on `{colors.canvas}` measures **2.3:1**. Placeholder and fine-print role; fails AA at every size. Stated plainly: do not set readable copy in this tone.
- `category-card-orange` — white on `{colors.accent-orange}` `#ff6b00` measures **2.86:1**, below even the 3:1 large-text threshold its own 32 px `{typography.display-md}` earns. A genuine brand failure, not a binding slip (its green sibling flips to ink for exactly this reason). Ink text would measure 7.01:1.
- `{colors.accent-orange}` `#ff6b00` as text on `{colors.canvas}` measures **2.86:1**, `{colors.accent-green}` `#00d722` **1.95:1** and `{colors.accent-yellow}` `#ffae13` **1.86:1**. These three are **fill tones only**; never set type in them.
- **Manufactured pairs — not rendered by the brand.** This file defines **no raised neutral surface token at all**: light-mode cards sit at `{colors.canvas}` and are separated by a 1 px boundary plus a layered shadow. The audit harness therefore elects a `surface` from component bindings and lands on a ground the measured ink never touches. Both of its elections are disclosed here:
  - electing `{colors.ink}` `#080808` (the polarity-flipped `card-feature-dark` / `hero-band-dark` ground): `{colors.ink}` on `{colors.ink}` at **1.0:1**, `{colors.ink-strong}` `#222222` on `{colors.ink}` at **1.26:1**, `{colors.body}` `#363636` on `{colors.ink}` at **1.66:1**. The dark card's documented ink is `{colors.on-primary}` white at **20.03:1**; the light-mode greys above are never drawn on it.
  - electing `{colors.accent-green}` `#00d722` (the `category-card-green` fill): `{colors.mute-soft}` on it at **1.17:1**, `{colors.hairline}` on it at **1.37:1**, `{colors.mute}` on it at **1.79:1**. That card carries only 32 px `{colors.primary}` display type, at **10.25:1**.

### Focus ring visibility

Measured against every surface this file defines. A surface is covered when either ring clears 3:1.

| Surface | `{colors.focus}` `#080808` | `{colors.focus-on-dark}` `#ffffff` | Covered |
|---|---|---|---|
| `{colors.canvas}` `#ffffff` | 20.03:1 | 1:1 | Yes |
| `{colors.primary}` `#080808` (dark bands, dark cards) | 1:1 | 20.03:1 | Yes |
| `{colors.accent-purple}` | 3.76:1 | 5.33:1 | Yes |
| `{colors.accent-pink}` | 6.36:1 | 3.15:1 | Yes |
| `{colors.accent-blue}` | 5.92:1 | 3.38:1 | Yes |
| `{colors.accent-orange}` | 7.01:1 | 2.86:1 | Yes |
| `{colors.accent-green}` | 10.25:1 | 1.95:1 | Yes |

`{colors.focus}` reuses the brand's existing near-black ink `#080808` and `{colors.focus-on-dark}` its white — neither is a new brand colour. The ring is drawn 2 px outside the control at a 2 px offset, so it is measured against the surface behind the control, as WCAG 2.2 Focus Appearance asks, rather than against the control's own fill.

### Tap targets
`button-primary` and `button-secondary` compute to ≈ 49.6 px tall (12 px + 12 px padding + 25.6 px line-height), clearing the 44 px guidance. `button-icon-circular` at `{spacing.sm}` padding needs a declared minimum of 44 × 44 px including the hit area. **Not verifiable from this document** — no page was rendered; treat as a computed intent, not a measurement.

### Reduced motion
Honoured in full: see the `@media (prefers-reduced-motion: reduce)` rule above. All travel and scale removed, opacity fades capped at `{motion.duration-reduced}` 150 ms, the loader's loop reduced to a single pass.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (`#080808`) for every primary CTA, every heading, and every wordmark. Near-black is the conversion colour.
- Use the five chromatic accents (purple / pink / blue / orange / green) as full-fill category cards, NOT as button backgrounds.
- Set hero headlines in `{typography.display-xxl}` weight 600 with `-0.8 px` tracking.
- Pair the proprietary WF Visual Sans family across every typographic role.
- Use `{rounded.sm}` 4 px for buttons, `{rounded.md}` 8 px for cards. The brand never uses pill CTAs.
- Use layered multi-stop drop-shadows on featured cards — the brand's distinctive elevation recipe.

### Don't
- Don't promote button-medium weight to 700+. The brand's weight ceiling is 600.
- Don't use chromatic accents as button backgrounds. They're surface fills, not actions.
- Don't render CTAs as pills. The brand's button geometry is tight 4 px rectangle.
- Don't introduce a sixth accent colour. The 5-stop palette is the system.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 479px | Hero stacks; all grids 1-up. |
| Mobile-Large | 479–767px | Same as Mobile. |
| Tablet | 768–991px | 2-up grids. |
| Desktop | ≥ 992px | Full multi-up grids. |

### Touch Targets
Buttons render at ~44 px (12 px vertical padding + 25.6 px line-height). WCAG AAA met.

### Collapsing Strategy
- Nav: full link row at desktop. Hamburger at mobile.
- Category card grid: 2 / 3 / 4-up at desktop, drops to 1-up at mobile.
- Pricing tier: 3 / 4-up at desktop, 1-up at mobile.

### Image Behavior
- Category cards: full-bleed solid colour fills (no photography).
- Product screenshots: 16:9 inside `{rounded.md}` card chrome.
- No portrait imagery in the marketing surface.


## Known Gaps

- **No raised surface tone.** The palette defines no `surface` / `card` neutral: every card sits at `{colors.canvas}` `#ffffff` and is separated from the page by a 1 px boundary plus a layered drop-shadow. This is the brand's real structure, so no neutral was invented to fill the role. Consequence: the audit harness resolves the `surface` role from component bindings and lands on `{colors.accent-green}`, a category-card fill, then measures text and boundary tones against a ground the brand never renders. Reported as a harness issue; the manufactured pairs are disclosed in Accessibility and labelled manufactured.
- **Motion is entirely prescribed.** No duration, easing curve, stagger or scroll-reveal timing was extracted from Webflow. The whole Motion & Animation section is the Calm profile block plus interaction mapping, and must not be cited as an observed fact.
- **Component states are prescribed.** The source documented only an active indicator on `ex-app-shell-row`. Hover, focus-visible, pressed, disabled, loading, selected and error treatments are derived from the brand's own rules, not observed.
- **Focus ring is prescribed.** Webflow's real ring was not captured. `{colors.focus}` and `{colors.focus-on-dark}` reuse existing brand tones (`#080808`, `#ffffff`); the 2 px width and 2 px offset are prescribed.
- **Shadow values carry no tokens.** Elevation & Depth states five literal `rgba(...)` stacks in prose with no `shadow:` group to reference, so `{shadow.*}` cannot be used anywhere in the file. Not added here because the stacks are multi-offset recipes rather than single values; flagged for a brand-owner decision.
- **No dark theme.** `card-feature-dark` and `hero-band-dark` are polarity-flipped *components*, not a dark mode. No dark-canvas token set exists, and none was invented.
- **Type substitutes unverified.** WF Visual Sans Variable is proprietary; the Inter / Inconsolata substitutions are stylistic judgements, with no metric matching performed.
- **Breakpoints and tap targets unverified.** The breakpoint widths, grid counts and collapsing strategy in Responsive Behavior are extracted from the source file, but the 44 px tap-target claim is computed from padding plus line-height, not measured.
- **Not computable from a document.** Overlap, horizontal overflow, clipping, real tap-target size, frame rate and layout shift all need a rendered page. No claim about them is made here.
