---
version: alpha
name: xAI-Inspired-design-analysis
description: An inspired interpretation of xAI's design language — Elon Musk's frontier-AI company whose web surface is a strict near-black canvas broken only by white pill outlines, occasional warm sunset / dusk gradient accents, a custom geometric sans (Universal Sans) for display, and an uppercase tracked monospace caption face; the whole system reads as engineered-cosmic, unmarketed.

colors:
  primary: "#ffffff"
  on-primary: "#0a0a0a"
  ink: "#ffffff"
  ink-hover: "#fafaf7"
  body: "#dadbdf"
  body-mid: "#7d8187"
  mute: "#7d8187"
  hairline: "#212327"
  canvas: "#0a0a0a"
  canvas-soft: "#1a1c20"
  canvas-card: "#191919"
  canvas-mid: "#363a3f"
  accent-sunset: "#ff7a17"
  accent-sunset-soft: "#ffc285"
  accent-dusk: "#7c3aed"
  accent-twilight: "#c4b5fd"
  accent-breeze: "#a0c3ec"
  accent-midnight: "#0d1726"
  # Focus ring. Not a new brand colour: it reuses the brand's own ink
  # ({colors.ink} / {colors.primary} #ffffff), drawn 2px outside the control
  # with a 2px offset gap in {colors.canvas}. xAI carries no accent colour on
  # its marketing surface, so a chromatic ring would contradict the brand.
  focus: "#ffffff"

motion:
  # Crisp profile — prescribed (SPEC section 5), not measured from the live site.
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
    fontFamily: universalSans, Inter, system-ui, -apple-system, sans-serif
    fontSize: 96px
    fontWeight: 400
    lineHeight: 96px
    letterSpacing: -2.4px
  display-lg:
    fontFamily: universalSans, Inter, system-ui, sans-serif
    fontSize: 72px
    fontWeight: 400
    lineHeight: 72px
    letterSpacing: -1.8px
  display-md:
    fontFamily: universalSans, Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 400
    lineHeight: 48px
    letterSpacing: -1.2px
  display-sm:
    fontFamily: universalSans, Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 400
    lineHeight: 36px
    letterSpacing: -0.6px
  display-xs:
    fontFamily: universalSans, Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 28px
  body-lg:
    fontFamily: universalSans, Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
  body-md:
    fontFamily: universalSans, Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-sm:
    fontFamily: universalSans, Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  caption-mono:
    fontFamily: GeistMono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 1.4px
  caption-mono-sm:
    fontFamily: GeistMono, ui-monospace, SFMono-Regular, Menlo, monospace
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
    letterSpacing: 1.2px
  button-md:
    fontFamily: universalSans, Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px

rounded:
  none: 0px
  sm: 8px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  button-outline-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.lg}"
  button-outline-sm:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  text-input:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  card-content:
    backgroundColor: "{colors.canvas-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  card-feature-product:
    backgroundColor: "{colors.canvas-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.4xl} {spacing.xl}"
  content-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.4xl} {spacing.xl}"
  eyebrow-mono:
    textColor: "{colors.ink}"
    typography: "{typography.caption-mono}"
  divider-hairline:
    borderColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
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
    headerTypography: "{typography.caption-mono}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card; elevation is the 1 px {colors.hairline} border, never a shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape with the 1 px {colors.hairline} border; the brand defines no shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

xAI is Elon Musk's frontier-AI lab and the website wears that posture with engineered restraint: a near-black canvas `{colors.canvas}` (`#0a0a0a`) edge-to-edge, white outline pills as every interactive element, and a single proprietary geometric sans `Universal Sans` carrying every display headline at weight 400. There is no gradient hero, no atmospheric backdrop, no product screenshot. The brand reads as confidently sparse — a research lab announcing its work rather than a SaaS marketing site.

Type is the second decisive voice. `Universal Sans` carries every display at weight 400 (regular) with aggressive negative tracking (`-2.4 px` at 96 px, scaling down through the display ladder). For technical labels, eyebrows, and metric counters, the brand pairs `Geist Mono` (uppercase, 1.4 px positive tracking) — every section eyebrow reads as a code comment more than a marketing label.

Every interactive element is a pill (`{rounded.pill}` 9999 px) with 1 px white-translucent border `rgba(255, 255, 255, 0.25)`. The button shape never varies — the same translucent-white pill carries "Try Grok", "Read announcement", "Custom Voices", "Sign up now", and every "Read" anchor. The pill is the entire shape system.

**Key Characteristics:**
- A single near-black canvas (`{colors.canvas}` `#0a0a0a`) with white outline pills as the entire interactive vocabulary.
- Universal Sans weight 400 for display, Geist Mono uppercase tracked for labels — the two-face contrast IS the brand voice.
- Every button is a `{rounded.pill}` outline with translucent-white border. The brand never uses filled CTAs except for one variant (white-filled pill on Sign Up).
- Cards are tight `{rounded.sm}` 8 px rectangles in a slightly-lighter `{colors.canvas-card}` (`#191919`) fill with hairline border. No shadows.
- A muted accent palette of sunset-orange / dusk-purple / twilight-violet / breeze-blue lives in the design tokens but appears rarely on the main marketing surface — reserved for product illustrations / icons.
- Massive negative letter-spacing on display headlines (`-2.4 px` at 96 px) gives the typography a precise, gathered look.

## Colors

### Brand & Accent
- **White** (`{colors.primary}` — `#ffffff`): The brand's primary "color" — used as button outline, button-primary fill, all display text. The brand's signature is white-on-near-black.
- **Sunset Orange** (`{colors.accent-sunset}` — `#ff7a17`): A warm orange used inside product illustrations and accent moments.
- **Sunset Soft** (`{colors.accent-sunset-soft}` — `#ffc285`): The lighter variant of the sunset accent.
- **Dusk Purple** (`{colors.accent-dusk}` — `#7c3aed`): Deep purple used inside product illustrations.
- **Twilight** (`{colors.accent-twilight}` — `#c4b5fd`): Soft violet — illustrative accent.
- **Breeze Blue** (`{colors.accent-breeze}` — `#a0c3ec`): Soft blue — illustrative accent.
- **Midnight** (`{colors.accent-midnight}` — `#0d1726`): Deep blue-black for illustrative backgrounds.

### Surface
- **Canvas** (`{colors.canvas}` — `#0a0a0a`): The default near-black page background. The brand's only true surface.
- **Canvas Soft** (`{colors.canvas-soft}` — `#1a1c20`): A slightly lighter dark fill used for hovered nav items and tooltips.
- **Canvas Card** (`{colors.canvas-card}` — `#191919`): The charcoal card fill used inside product-feature cards.
- **Canvas Mid** (`{colors.canvas-mid}` — `#363a3f`): A mid-dark used for nested surfaces and code mockup backgrounds.
- **Hairline** (`{colors.hairline}` — `#212327`): 1 px solid dividers on dark surfaces. **Decorative only.** Measured against every ground this file defines it reaches 1.26:1 on `{colors.canvas}`, 1.12:1 on `{colors.canvas-card}` and 1.08:1 on `{colors.canvas-soft}` — far below the 3:1 a component boundary needs. It is an extracted brand value and is not changed here; where a hairline is the *only* boundary of an interactive control, draw that boundary in `{colors.body-mid}` (5.06:1 on canvas, 4.49:1 on `{colors.canvas-card}`, 4.36:1 on `{colors.canvas-soft}`), which the palette already owns. See Accessibility.

### Text
- **Ink** (`{colors.ink}` — `#ffffff`): Default text on canvas — pure white.
- **Ink Hover** (`{colors.ink-hover}` — `#fafaf7`): Slightly off-white used for the hover state of ink-coloured links and nav items. 18.93:1 on `{colors.canvas}`.
- **Body** (`{colors.body}` — `#dadbdf`): Secondary body text — supporting copy in lighter weight.
- **Body Mid / Mute** (`{colors.body-mid}` — `#7d8187`): Mid-emphasis body and mute text — captions, fine print.

### Focus
- **Focus** (`{colors.focus}` — `#ffffff`): The focus ring. **Prescribed, not extracted** — no focus treatment is recorded for this brand. It reuses the brand's own ink rather than introducing a colour: xAI's whole premise is white on near-black with no accent on the marketing surface, so a chromatic ring would be a new brand colour. Drawn as a 2 px `{colors.focus}` ring *outside* the control with a 2 px offset gap in `{colors.canvas}`, so it reads against the ground behind the control and not against a white pill fill. Measured ratios in Accessibility.

### Semantic
The brand doesn't surface a separate semantic palette on the marketing site. Validation cues use the white-on-canvas hierarchy.

## Typography

### Font Family
Two faces ladder the system:
1. **universalSans** — proprietary geometric sans used for every display, body, button, and link role. Weight 400 only on the marketing surface (the brand's restraint is part of the voice). Negative letter-spacing at display sizes is the visual signature.
2. **GeistMono** — used for uppercase section eyebrows, label captions, and metric counters. Positive tracking (1.2 – 1.4 px) at 12 – 14 px.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 96px | 400 | 96px | -2.4px | Maximum hero scale. |
| `{typography.display-lg}` | 72px | 400 | 72px | -1.8px | Sub-hero displays. |
| `{typography.display-md}` | 48px | 400 | 48px | -1.2px | Section headlines. |
| `{typography.display-sm}` | 32px | 400 | 36px | -0.6px | Card-cluster headings. |
| `{typography.display-xs}` | 20px | 400 | 28px | 0 | Inline displays. |
| `{typography.body-lg}` | 18px | 400 | 28px | 0 | Lead paragraphs. |
| `{typography.body-md}` | 16px | 400 | 24px | 0 | Default body. |
| `{typography.body-sm}` | 14px | 400 | 20px | 0 | Secondary body. |
| `{typography.caption-mono}` | 14px | 400 | 20px | 1.4px | Section eyebrow (GeistMono uppercase). |
| `{typography.caption-mono-sm}` | 12px | 400 | 16px | 1.2px | Small mono labels. |
| `{typography.button-md}` | 14px | 400 | 20px | 0 | Button label. |

### Principles
- **Weight 400 for everything.** The brand never bolds. Negative tracking + size hierarchy do the emphasis work.
- **Tight negative tracking on display sizes.** Reverting to neutral tracking loses the precision feel.
- **GeistMono uppercase for eyebrows.** Tracked positively (1.4 px) to make the mono read as a code comment.

### Note on Font Substitutes
universalSans is proprietary. Open-source substitutes:
- **Display + body** — *Inter* weight 400 with `-0.04em` to `-0.02em` letter-spacing at display sizes comes closest. *Geist* is the second-best option.
- **Mono** — *Geist Mono* is the documented brand companion; *JetBrains Mono* or *IBM Plex Mono* are alternates.

## Layout

### Spacing System
- **Base unit**: 4 px.
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 24 px · `{spacing.2xl}` 32 px · `{spacing.3xl}` 48 px · `{spacing.4xl}` 64 px.
- **Section padding**: hero / content bands at `{spacing.4xl}` 64 px on desktop.
- **Card interior padding**: `{spacing.xl}` 24 px.

### Grid & Container
- Marketing content centres at ~1200 px.
- Product / announcement card grid: 2-up at desktop, 1-up at mobile.


## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default. |
| Level 1 — Hairline | 1 px solid `{colors.hairline}` border. | Card chrome, button outlines (with translucent white). |

The brand uses no shadows. Hairline borders carry all elevation cues.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed bands. |
| `{rounded.sm}` | 8px | Card chrome (the brand's `--radius` value). |
| `{rounded.pill}` | 9999px | Every button — the brand's universal interactive shape. |
| `{rounded.full}` | 9999px | Circular icon containers. |

## Components

### Buttons

**`button-primary`** — the rare white-filled pill (used on a single Sign Up CTA).
- Background `{colors.primary}` white, text `{colors.on-primary}` near-black, 1 px solid white border, label `{typography.button-md}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.pill}` 9999 px.
- The 1 px white border sits on the white fill, so it measures 1.0:1 against it and is not a boundary. The pill's real boundary is its fill against the page: `{colors.primary}` on `{colors.canvas}` at 19.8:1. The border exists to keep the filled and outline pills dimensionally identical.
- States: default · hover (fill drops to `{colors.ink-hover}`) · focus-visible (2 px `{colors.focus}` ring, 2 px `{colors.canvas}` offset) · pressed (same fill, no travel) · disabled (fill at 40% over `{colors.canvas}`, label at 40%; exempt from contrast minima) · loading (label swapped for an in-place mono spinner, pill width frozen).

**`button-outline-on-dark`** — the canonical white-outline pill, used for every non-primary CTA.
- Background `{colors.canvas}` (transparent in practice — `rgba(0,0,0,0)`), text `{colors.ink}` white, 1 px solid `{colors.hairline}` border (translucent white at runtime), same typography / padding scale / shape.
- The extracted runtime border is `rgba(255, 255, 255, 0.25)`, which composites to `#474747` over `{colors.canvas}` — 2.13:1, still under 3:1. The token `{colors.hairline}` records the flat equivalent at 1.26:1. Both fail a non-text boundary; the white label inside carries the control's legibility at 19.8:1. For an accessible rebuild, draw this border in `{colors.body-mid}` (5.06:1 on canvas).
- States: default · hover (border to `{colors.body-mid}`, label to `{colors.ink-hover}`) · focus-visible (2 px `{colors.focus}` ring, 2 px `{colors.canvas}` offset) · pressed (border holds, label at `{colors.body}`) · disabled (label and border at `{colors.canvas-mid}`) · loading (label replaced by spinner in place).

**`button-outline-sm`** — the smaller outline pill used in card-cluster CTAs.
- Same as `button-outline-on-dark` with tighter padding `{spacing.xs} {spacing.md}`.
- States: identical ladder — default · hover · focus-visible · pressed · disabled · loading.

### Cards & Containers

**`card-content`** — the default content card.
- Background `{colors.canvas-card}` (`#191919`), text `{colors.ink}`, 1 px solid `{colors.hairline}` border, padding `{spacing.xl}`, shape `{rounded.sm}` 8 px.
- States: default and hover only — this card is content, not a control. Hover raises the border to `{colors.body-mid}`; nothing moves and nothing scales. It is never disabled, selected, loading or errored.

**`card-feature-product`** — the product-feature card (Grok / Voice / API).
- Same chrome as `card-content`. Hosts an SVG illustration + headline + body + outline pill CTA.
- States: default · hover (border to `{colors.body-mid}`; the nested pill keeps its own hover) · focus-visible on the nested CTA only, since the card itself is not focusable. The card has no pressed, disabled, selected or error state.

### Inputs & Forms

**`text-input`** — the standard text input on dark.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, body in `{typography.body-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.sm}` 8 px.
- The `{colors.hairline}` border is this input's only boundary and measures 1.08:1 against `{colors.canvas-soft}` — it is effectively invisible. The extracted binding is kept as a fact; an accessible rebuild draws the resting border in `{colors.body-mid}` at 4.36:1 (see Needs approval in the audit report).
- States: default · hover (border one step lighter) · focus-visible (2 px `{colors.focus}` ring outside the field, 2 px `{colors.canvas}` offset) · disabled (label and border at `{colors.canvas-mid}`, 1.49:1 on `{colors.canvas-soft}`; exempt) · error (border and helper text at `{colors.accent-sunset}`, 6.54:1 on `{colors.canvas-soft}`; the brand owns no red, so the sunset accent carries validation) · loading (mono spinner in the trailing slot). No selected state.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.xl}`.
- States: one state. The bar is sticky and does not change on scroll — no shrink, no background shift, no shadow.

**`nav-link`** — link items inside nav.
- Text `{colors.ink}`, set in `{typography.body-sm}`.
- States: default · hover (ink to `{colors.ink-hover}`, 18.93:1 on canvas) · focus-visible (2 px `{colors.focus}` ring with `{colors.canvas}` offset) · selected (the current section, marked by the ink staying at full `{colors.ink}` while its siblings sit at `{colors.body}`). No pressed, disabled, loading or error state.

**`footer`** — the footer band.
- Background `{colors.canvas}`, text `{colors.body}`, padding `{spacing.3xl} {spacing.xl}`. Body in `{typography.body-sm}`.
- States: one state for the band itself; its links follow the `nav-link` ladder (default · hover · focus-visible).

### Signature Components

**`hero-band`** — the dark hero with massive display headline.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.4xl} {spacing.xl}`. Headline in `{typography.display-xl}` (96 px weight 400 with `-2.4 px` tracking).

**`content-band`** — the standard content section.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.4xl} {spacing.xl}`. Section headline in `{typography.display-md}` preceded by a `{typography.caption-mono}` UPPERCASE GeistMono eyebrow.

**`eyebrow-mono`** — the uppercase tracked GeistMono label above every section headline.
- Text `{colors.ink}`, set in `{typography.caption-mono}`. The brand's signature label style.
- States: one state. The eyebrow is never interactive.

**`divider-hairline`** — the 1 px line between section bands.
- 1 px solid `{colors.hairline}`. Decorative: 1.26:1 against `{colors.canvas}`. It separates bands optically, and no information depends on seeing it.
- States: one state.

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
- States: default · hover (row fill to `{colors.canvas-soft}`) · focus-visible · selected (2 px `{colors.primary}` leading indicator, 19.8:1 on `{colors.canvas}`). No loading or error state.

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card; elevation is the 1 px {colors.hairline} border, never a shadow.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape with the 1 px {colors.hairline} border; the brand defines no shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`


## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or transition is recorded anywhere in this file's extracted content, so every value below comes from the **Crisp** profile in `theme-audit/SPEC.md` section 5. Crisp is the right fit here on its own evidence: xAI's surface is a research-lab tool, not a showroom — no photography, no gradient hero, weight-400 type, outline pills, and a single near-black canvas. State changes should read as instant; there is no entrance choreography to admire.

Two consequences of the brand's own restraint shape the table. First, xAI is near-monochrome, so most interaction feedback is a paint change — `border-color` from `{colors.hairline}` to `{colors.body-mid}`, ink from `{colors.ink}` to `{colors.ink-hover}` — and that is the hover state, not a shortfall. Second, the brand uses no shadows, so elevation never animates; modals and toasts arrive on opacity and a short translate only.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, nav link, card border) | `{motion.duration-fast}` | `{motion.ease-standard}` | `border-color`, `color` (paint only — nothing moves) | Unchanged; paint change kept at `{motion.duration-reduced}` |
| Press / active (pill) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` 1 → 0.85 | Instant opacity step, no transition |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` 0 → 1 on the 2 px `{colors.focus}` ring | Ring appears instantly, no fade |
| Page / route transition | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(8px → 0)` | Opacity only at `{motion.duration-reduced}`; no travel |
| Modal / drawer | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(12px → 0)` (drawer: `translateX`) | Opacity only at `{motion.duration-reduced}`; panel appears in place |
| Dropdown / menu | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(4px → 0)` | Opacity only at `{motion.duration-reduced}` |
| Toast | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(8px → 0)` | Opacity only at `{motion.duration-reduced}` |
| List / card-grid enter | `{motion.duration-base}` per item, `{motion.stagger-step}` 20ms stagger, capped at 6 items | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px → 0)` | Stagger dropped, all items fade together at `{motion.duration-reduced}` |
| List / card-grid exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform: translateY(0 → 4px)` | Opacity only at `{motion.duration-reduced}`; no stagger |
| Loading | 800ms linear, infinite | `linear` | `transform: rotate()` on a 1 px `{colors.body-mid}` arc; skeletons pulse `opacity` 0.4 → 0.7 | Spinner frozen; a static mono "LOADING" label in `{typography.caption-mono-sm}` replaces it. Skeleton pulse stops |

### Rules
- **Transform and opacity only.** Never `width`, `height`, `top`, `left` or `margin`. Paint-only changes (`border-color`, `color`) are permitted and are the brand's main hover signal; they use the same `{motion.duration-fast}` as any other state change.
- **Exit is always shorter than its matching entrance** — `{motion.duration-fast}` out against `{motion.duration-base}` in.
- **Nothing animates on first paint.** The hero headline is painted, not revealed; a 96 px `{typography.display-xl}` line never waits on a transition.
- **No infinite animation except the loader.** The brand carries no ambient motion — no drifting starfield, no gradient breathing. Adding one would contradict the Overview's "no atmospheric backdrop".
- **Travel is small.** 4 – 12 px, never more; `{rounded.pill}` controls never scale, because a scaling pill distorts its own radius.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale on page transitions, modals, drawers,
     dropdowns, toasts and list enter/exit; the list stagger; the loader's
     rotation; the skeleton pulse. */
  /* Kept: opacity fades, clamped to {motion.duration-reduced} 100ms, and every
     paint-only state change (border-color, color) at the same 100ms — these
     carry the brand's hover and focus feedback and removing them would leave
     interactive elements with no response at all. The focus ring still
     appears instantly. */
  *, *::before, *::after {
    transition-duration: 100ms !important;   /* {motion.duration-reduced} */
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
    transition-property: opacity, border-color, color !important;
  }
}
```

## Accessibility

All ratios below are WCAG 2.1 relative-luminance measurements of the hexes in this file's own frontmatter. Contrast is computable from a document; **tap-target size, focus-order and actual rendered behaviour are not** — the notes on those are prescriptions, not observations.

### Measured contrast — passing

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 19.8:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-card}` | 17.58:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` | 17.06:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas}` | 14.31:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas-card}` | 12.71:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 19.8:1 | 4.5:1 | Pass |
| `{colors.mute}` on `{colors.canvas}` | 5.06:1 | 4.5:1 | Pass |
| `{colors.focus}` on `{colors.canvas}` | 19.8:1 | 3.0:1 | Pass |

### Measured contrast — real brand failures, disclosed

These are extracted brand values. They are **not** altered here; a falsified hex would make this document describe a product that does not exist.

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.hairline}` on `{colors.canvas}` | 1.26:1 | 3.0:1 | **Fail** — the brand's hairline is decorative; it is not a perceivable boundary |
| `{colors.hairline}` on `{colors.canvas-card}` | 1.12:1 | 3.0:1 | **Fail** — card chrome is invisible as a boundary |
| `{colors.hairline}` on `{colors.canvas-soft}` | 1.08:1 | 3.0:1 | **Fail** — and this is the `text-input`'s only boundary, so the field has no perceivable edge |
| `{colors.mute}` / `{colors.body-mid}` on `{colors.canvas-card}` | 4.49:1 | 4.5:1 | **Fail by 0.01** — passes on `{colors.canvas}` at 5.06:1; on a card, restrict it to 18 px+ (`{typography.body-lg}`), where the 3:1 large-text threshold applies |
| `{colors.mute}` on `{colors.canvas-soft}` | 4.36:1 | 4.5:1 | **Fail** — same restriction |
| `{colors.mute}` on `{colors.canvas-mid}` | 2.92:1 | 4.5:1 | **Fail** — never set mute text on `{colors.canvas-mid}`; use `{colors.body}` (8.28:1) |
| `{colors.accent-dusk}` on `{colors.canvas}` | 3.47:1 | 4.5:1 | **Fail** as text — this purple is an illustration fill only, where 1.4.3 does not apply |
| `{colors.primary}` border on `{colors.primary}` fill (`button-primary`) | 1.0:1 | 3.0:1 | **Fail, and meaningless** — a white border on a white fill is not a boundary. The pill's real boundary is its fill against the page at 19.8:1. The border is documented because it exists in the extracted CSS, keeping the filled and outline pills dimensionally identical |
| `rgba(255, 255, 255, 0.25)` outline-pill border over `{colors.canvas}` (composites to `#474747`) | 2.13:1 | 3.0:1 | **Fail** — the real runtime border of every outline pill. The white label inside carries the control at 19.8:1, but the control's own edge is below the non-text minimum |

**Plainly stated: the real xAI surface fails WCAG 2.1 AA at every component boundary.** Every hairline and every pill outline sits between 1.08:1 and 2.13:1 against its ground, where 1.4.11 asks for 3:1. Text is never the problem — white on near-black is 19.8:1. Anyone building on this document and needing AA should draw boundaries in `{colors.body-mid}` (5.06:1 on canvas, 4.36:1 on `{colors.canvas-soft}`), which the palette already owns; no new token is needed.

### Surface separation

The three dark grounds are nearly indistinguishable from each other: `{colors.canvas}` to `{colors.canvas-card}` is 1.13:1, `{colors.canvas}` to `{colors.canvas-soft}` 1.16:1, and `{colors.canvas-card}` to `{colors.canvas-soft}` 1.03:1. That is an accurate record of the brand — the layers read as one black field, and with hairlines at 1.1:1 a card has no visible edge at all. Do not treat surface-on-surface tone as a boundary cue; it is not one.

### Focus ring

Prescribed, not extracted. `{colors.focus}` `#ffffff` — the brand's own ink, reused rather than invented, because xAI has no accent colour on its marketing surface. Drawn as a 2 px ring **outside** the control with a 2 px offset gap in `{colors.canvas}`, so it is judged against the ground behind the control, per WCAG 2.2 Focus Appearance, rather than against the fill of a white pill it surrounds.

| Surface the ring is drawn on | `{colors.focus}` ratio | Required | Result |
|---|---|---|---|
| `{colors.canvas}` | 19.8:1 | 3.0:1 | Pass |
| `{colors.canvas-card}` | 17.58:1 | 3.0:1 | Pass |
| `{colors.canvas-soft}` | 17.06:1 | 3.0:1 | Pass |
| `{colors.canvas-mid}` | 11.45:1 | 3.0:1 | Pass |
| `{colors.accent-midnight}` | 17.98:1 | 3.0:1 | Pass |

One ring serves the whole file: xAI is dark-canvas only, with no light-surface polarity, so no `focus-on-light` counterpart is needed. On the one white surface the brand renders — the `button-primary` fill — the ring's 2 px `{colors.canvas}` offset separates it from the pill (19.8:1) and the ring itself still measures against the page behind.

### Tap targets
Prescribed, not measured. Outline pills compute to roughly 32 – 40 px tall from `{spacing.sm}` padding plus a 20 px line box, which is under the 44 × 44 px of WCAG 2.5.5. Inflate the hit area with padding or a pseudo-element on touch viewports; the pill's visual size must not change, since the shape is the brand.

### Reduced motion
Every motion value in this file respects `@media (prefers-reduced-motion: reduce)`: all travel and the loader's rotation are removed, opacity fades and paint-only state changes are clamped to `{motion.duration-reduced}` 100 ms, and the focus ring appears instantly. See Motion & Animation.

### Non-colour cues
The brand signals state almost entirely by tone on a monochrome field, which is thin for anyone with low vision. Form validation uses `{colors.accent-sunset}` (6.54:1 on `{colors.canvas-soft}`) **with** a mono helper line in `{typography.caption-mono-sm}`; colour alone never carries an error.

## Do's and Don'ts

### Do
- Reserve `{colors.canvas}` (`#0a0a0a`) as the only page surface. The brand is dark-canvas only.
- Set hero headlines in `{typography.display-xl}` Universal Sans weight 400 with `-2.4 px` tracking. The precision IS the voice.
- Use `{rounded.pill}` 9999 px on every interactive element. The pill is the brand.
- Pair Universal Sans (sentence-case) with GeistMono UPPERCASE (eyebrows, labels, metric counters).
- Use white-translucent borders for outline buttons — the brand never uses solid white borders on its outline pill.

### Don't
- Don't introduce a light-mode counterpart. xAI is dark-canvas only.
- Don't bold display headlines. Weight 400 is the entire scale.
- Don't use filled buttons broadly. The brand uses outline pills almost exclusively; one Sign Up white-filled pill is the rare exception.
- Don't drop a drop-shadow on cards. Hairline borders carry elevation.
- Don't substitute Universal Sans with a generic geometric sans without adjusting letter-spacing. The negative tracking is part of the brand.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hero scales 96 → 48 px; grids 1-up; hamburger nav. |
| Desktop | ≥ 768px | Full hero + 2-up grids. |

### Touch Targets
Buttons render ~32 – 40 px tall (8 vertical padding + 20 line). Mobile inflates touch area to meet WCAG 44 × 44 px.

### Image Behavior
The brand uses sparse SVG illustrations for product moments (Grok, Voice, API). No photography on the marketing surface.

## Known Gaps

- **All motion is prescribed, none extracted.** No duration, easing curve, stagger or transition is recorded for this brand anywhere in this file's source content. The whole Motion & Animation section is the SPEC **Crisp** profile, labelled as such. Nothing in it should be cited as an observed xAI behaviour.
- **The focus treatment is prescribed.** No focus ring was extracted. `{colors.focus}` reuses `#ffffff`, a hex the palette already owns, with a prescribed 2 px width and 2 px `{colors.canvas}` offset. The real site's focus behaviour is unknown.
- **No shadow tokens, deliberately.** The brand documents no shadow values, so no `shadow:` group is defined. Two illustrative example surfaces previously described an "elevated" and a "medium" shadow with no token behind either; both now state the 1 px `{colors.hairline}` border instead, matching Elevation & Depth.
- **An unsourced "no-hover policy" line has been withdrawn.** The Ink Hover entry under Colors formerly read "filtered out per no-hover policy in component specs". No such policy exists in `README.md`, in `CONTRIBUTING.md` or anywhere else in this repo, and the same sentence appears verbatim in six other site files — it is an artefact, not an extracted fact. `{colors.ink-hover}` is an extracted token and is now documented as the hover ink it is.
- **`{colors.body-mid}` and `{colors.mute}` are the same hex** (`#7d8187`). Whether the real design system treats these as one token under two names, or whether one of them drifted, is not recoverable from this file.
- **Component state ladders are prescribed.** Only an `activeIndicator` on one illustrative surface was extracted. Every hover, focus-visible, pressed, disabled, loading, selected and error state named in Components is a reasoned prescription consistent with the brand's near-monochrome, paint-only idiom — not an observation of the live site.
- **Semantic colour is absent from the brand.** xAI surfaces no success / warning / error palette. Error states borrow `{colors.accent-sunset}`, which is an illustration accent, not a documented semantic token.
- **`{rounded.pill}` and `{rounded.full}` hold the same value** (9999 px) under two names, kept because the prose distinguishes their use (button shape vs circular icon container).
- **Not computable from a document:** rendered tap-target size, focus order, overlap, horizontal overflow, clipping, frame rate and layout shift. No claim about any of them is made here.
- **The `ex-*` surfaces are auto-derived demonstrations**, not extracted xAI components. Their note still mentions `TO_FILL` markers; none remain in this file.
