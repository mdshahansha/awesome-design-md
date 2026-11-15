---
version: alpha
name: Supabaze-Inspired-design-analysis
description: An inspired interpretation of Supabaze's design language — an open-source database platform built on a clean white-and-near-black system with a single signature emerald-green CTA, a custom humanist sans display tier, and dense product UI mockups composited above the hero. The brand reads as quietly technical: minimal chrome, a near-monochrome palette, and the green primary acting as the only chromatic event on the page.

colors:
  primary: "#3ecf8e"
  primary-deep: "#24b47e"
  primary-soft: "#4ade80"
  ink: "#171717"
  ink-secondary: "#212121"
  ink-mute: "#707070"
  ink-mute-2: "#9a9a9a"
  ink-faint: "#b2b2b2"
  on-primary: "#171717"
  on-dark: "#ffffff"
  focus: "#707070"
  canvas: "#ffffff"
  canvas-soft: "#fafafa"
  canvas-night: "#1c1c1c"
  canvas-night-soft: "#202020"
  hairline: "#dfdfdf"
  hairline-strong: "#c7c7c7"
  hairline-cool: "#ededed"
  hairline-cool-2: "#efefef"
  hairline-cool-3: "#d4d4d4"
  accent-purple: "#6b01c2"
  accent-violet: "#644fc1"
  accent-purple-soft: "#eddbf9"
  accent-yellow: "#ffdb13"
  accent-tomato: "#ff2201"
  accent-pink: "#c7007e"
  accent-indigo: "#054cff"
  accent-crimson: "#e2005a"

typography:
  display-xxl:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1.92px
  display-xl:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1.44px
  display-lg:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.72px
  display-md:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.42px
  heading-lg:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  heading-md:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  caption:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  micro:
    fontFamily: "Circular, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  code:
    fontFamily: "ui-monospace, Menlo, Monaco, Consolas, 'Liberation Mono', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  huge: 64px

shadow:
  none: "none"
  small: "0 1px 3px rgba(0,0,0,0.06)"
  medium: "0 8px 24px rgba(0,0,0,0.08)"
  large: "0 16px 48px rgba(0,0,0,0.12)"

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
  button-primary-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-primary-green-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-secondary-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-on-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 0px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  card-feature-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-pricing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-pricing-featured:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-feature-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  code-block:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.sm}"
    padding: 16px
  pill-tag-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  pill-tag-soft:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  nav-bar-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  link-on-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
  footer-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-mute}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 24px
---

## Overview

Supabaze's design language is engineered for clarity above all else. The marketing surfaces sit on `{colors.canvas}` (pure white), with text rendered in `{colors.ink}` (`#171717` — near-black, never pure black). Across the entire system the only consistent chromatic event is the **emerald green primary** (`{colors.primary}` — `#3ecf8e`) — used as the filled CTA, occasional accent dot, and the signature highlight color in the wordmark. Everything else is a calibrated grey ladder from `#ededed` hairline-cool to `#171717` ink, with thin black-on-white typography doing most of the visual work.

Typography runs **Circular** at weight 500 for display and 400 for body. The display tier uses tight negative letter-spacing (-1.92px at 64px) to pull the rounded humanist letterforms into editorial density. There's no atmospheric gradient, no full-bleed photography, no dark-canvas marketing track — the brand commits to white.

The product itself appears as composited UI screenshots on every page: dashboard tables, SQL editors, query builders, log streams. These screenshots are the brand's argument. They sit inside `{rounded.lg}` 12px containers with subtle 1px hairlines, often arranged 2-up or in a floating "stacked panes" composition above the hero band.

**Key Characteristics:**
- Single emerald primary (`{colors.primary}` `#3ecf8e`) as the only chromatic event; everything else is monochrome.
- White canvas marketing track with greyscale hierarchy from `{colors.hairline-cool}` to `{colors.ink}`.
- Custom humanist sans display tier at weight 500 with negative letter-spacing of -1.92px to -0.42px.
- Composited product UI screenshots (dashboard, SQL editor, log stream) are the dominant decorative element — never photography, never illustrations.
- Tight 6px / 8px button radii — square-ish, technical, never pill-shaped.
- Code blocks rendered in deep `{colors.canvas-night}` (`#1c1c1c`) with monospace inline code; the brand's developer DNA is visible in every snippet.
- Pricing tiers use a dark inverted `{colors.canvas-night}` featured tier, not a green one — the green is reserved for buttons and dot accents.

## Colors

> **Source pages:** home (`/`), `/database`, `/partners/integrations`, `/partners/integrations/powersync`, `/solutions/ai-builders`, `/pricing`.

### Brand & Accent
- **Emerald** (`{colors.primary}` — `#3ecf8e`): The signature CTA color. Filled-button background, brand wordmark accent, dot indicator.
- **Emerald Deep** (`{colors.primary-deep}` — `#24b47e`): Pressed-state lift of the primary.
- **Emerald Soft** (`{colors.primary-soft}` — `#4ade80`): Lighter emerald used in chart accents and product UI.
- **Accent Purple** (`{colors.accent-purple}` — `#6b01c2`): Rare accent used in integration logos and chart points; never a button.
- **Accent Violet** (`{colors.accent-violet}` — `#644fc1`): Secondary accent in the same role as accent purple.
- **Accent Yellow** (`{colors.accent-yellow}` — `#ffdb13`): Chart accent / status indicator only.
- **Accent Pink / Crimson / Indigo / Tomato**: Reserved for integration logos and rare chart highlights, never as system colors.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): Default page background.
- **Canvas Soft** (`{colors.canvas-soft}` — `#fafafa`): Barely-tinted off-white for alternating section bands.
- **Canvas Night** (`{colors.canvas-night}` — `#1c1c1c`): Deep near-black used in code blocks, dashboard mockups, featured pricing tier.
- **Canvas Night Soft** (`{colors.canvas-night-soft}` — `#202020`): Slightly lifted dark for nested chrome.
- **Hairline** (`{colors.hairline}` — `#dfdfdf`): 1px borders on cards and tables.
- **Hairline Strong** (`{colors.hairline-strong}` — `#c7c7c7`): Slightly darker border for emphasis.
- **Hairline Cool** (`{colors.hairline-cool}` — `#ededed`) / **Hairline Cool 2** (`#efefef`) / **Hairline Cool 3** (`#d4d4d4`): The brand's grey ladder for fine chrome work.

### Text
- **Ink** (`{colors.ink}` — `#171717`): Default body text. Near-black, never pure.
- **Ink Secondary** (`{colors.ink-secondary}` — `#212121`): Slightly cooler near-black for body emphasis.
- **Ink Mute** (`{colors.ink-mute}` — `#707070`): Secondary text and helper copy.
- **Ink Mute 2** (`{colors.ink-mute-2}` — `#9a9a9a`): Tertiary text.
- **Ink Faint** (`{colors.ink-faint}` — `#b2b2b2`): Disabled / placeholder text.
- **On Primary** (`{colors.on-primary}` — `#171717`): Text on the emerald primary fill — near-black, not white. The button reads as a "lit" surface with dark type, not a colored chip.
- **On Dark** (`{colors.on-dark}` — `#ffffff`): Text on canvas-night surfaces.

### Focus
- **Focus** (`{colors.focus}` — `#707070`): The focus ring. **Prescribed, not extracted** — the
  live site's ring was not measured. It is not a new brand colour: it reuses the hex the
  palette already owns as `{colors.ink-mute}`, chosen because it is the one tone in this
  palette that clears 3:1 against *every* surface the file defines — white `{colors.canvas}`
  (4.95:1), `{colors.canvas-soft}` (4.74:1), `{colors.canvas-night}` (3.44:1) and
  `{colors.canvas-night-soft}` (3.29:1). A single mid-luminance ring is used rather than a
  light/dark pair because this file carries two surface polarities and one value serves both.
  The emerald `{colors.primary}` is deliberately *not* the ring: it measures 2.00:1 on white,
  and the brand reserves emerald for filled CTAs.

## Typography

### Font Family

The display and UI tier is **Circular** — a proprietary geometric humanist sans by Lineto. Fallback chain: `'Helvetica Neue', Helvetica, Arial`.

For maximum brand fidelity when Circular isn't licensed, use **Inter** (open-source via Google Fonts) at weight 500 for display with `letter-spacing: -1.92px` at 64px. Inter is the closest open-source analogue to Circular's geometric humanist character.

Code blocks use **system mono** (`ui-monospace`, with Menlo / Monaco / Consolas fallbacks).

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 64px | 500 | 1.1 | -1.92px | Hero headline |
| `{typography.display-xl}` | 48px | 500 | 1.1 | -1.44px | Section opener |
| `{typography.display-lg}` | 36px | 500 | 1.15 | -0.72px | Sub-section / pricing tier |
| `{typography.display-md}` | 28px | 500 | 1.2 | -0.42px | Card title |
| `{typography.heading-lg}` | 22px | 500 | 1.2 | 0 | Compact heading |
| `{typography.heading-md}` | 18px | 500 | 1.4 | 0 | Section sub-heading |
| `{typography.body-lg}` | 18px | 400 | 1.55 | 0 | Marketing body lead |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default UI body |
| `{typography.button-md}` | 14px | 500 | 1.0 | 0 | Button label |
| `{typography.caption}` | 13px | 400 | 1.45 | 0 | Helper, footnote |
| `{typography.micro}` | 12px | 400 | 1.45 | 0 | Pill label, fine print |
| `{typography.code}` | 14px | 400 | 1.5 | 0 | Code block content |

### Principles
- **Weight 500 across display.** Mid-weight reads as engineered, not decorative.
- **Negative tracking on display.** -1.92px at 64px scaling proportionally down — tightens the rounded humanist letterforms into editorial density.
- **Mono for code.** System mono families (Menlo / Monaco) — no proprietary mono webfont.

### Note on Font Substitutes
Circular is proprietary. Use **Inter** at weight 500 with `letter-spacing: -1.92px` for display tiers. **Geist Sans** (open-source from Vercel) is another close alternative for both display and body. Avoid Helvetica defaults — they're heavier and lack the geometric warmth.

## Layout

### Spacing System
- **Base unit**: 8px (with 2 / 4 / 12 sub-tokens for fine work).
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.huge}` 64px.
- **Section padding**: 64–96px on marketing surfaces.
- **Card internal padding**: 32px on feature/pricing cards.

### Grid & Container
- Marketing pages center in a ~1280px container with no edge-bleed; the brand keeps content inside the box.
- Pricing collapses 4-up → 2-up → 1-up at 1024 / 768 breakpoints.
- Product UI mockups stack 2-up or render as overlapping panes inside the same container.

### Whitespace Philosophy
The brand uses generous 64–96px section padding without atmospheric gradients filling the space — the white canvas is the design. The composited product UI mockups break up sections without requiring decoration.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat, 1px hairline — `{shadow.none}` | Default cards |
| 1 | `{shadow.small}` — `0 1px 3px rgba(0,0,0,0.06)` | Subtle card lift |
| 2 | `{shadow.medium}` — `0 8px 24px rgba(0,0,0,0.08)` | Floating composited UI mockups |
| 3 | `{shadow.large}` — `0 16px 48px rgba(0,0,0,0.12)` | Modal overlays, deep elevation |

### One Elevation Language
Depth is expressed **either** as a 1px hairline (Level 0) **or** as a shadow from the
`{shadow.*}` ladder (Levels 1–3) — never both on the same element. Flat cards on
`{colors.canvas}` carry a `{colors.hairline}` border and `{shadow.none}`; a lifted or
floating element drops the border and takes `{shadow.small}` or `{shadow.medium}`. Mixing
the two reads as a doubled edge and is the most common way this system is broken.

### Decorative Depth
The brand's depth is **product UI mockups** rather than gradients. Stacked dashboard / SQL editor / log panes composite together with subtle Level 2 shadows to suggest spatial hierarchy.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Form inputs, hairline tags |
| `{rounded.sm}` | 6px | Buttons (the brand's signature button radius), code blocks |
| `{rounded.md}` | 8px | Compact cards, alerts |
| `{rounded.lg}` | 12px | Pricing cards, feature cards, product mockups |
| `{rounded.xl}` | 16px | Modal dialogs, large container chrome |
| `{rounded.full}` | 9999px | Pill tags, avatars |

### Focus Ring Geometry
Prescribed, not extracted. `2px solid {colors.focus}` with `outline-offset: 2px`, drawn
**outside** the control so it is measured against the surface behind it rather than the
control's own fill — which is what WCAG 2.2 Focus Appearance asks for, and the only way a
ring can clear 3:1 on both white and `{colors.canvas-night}`. The ring's corner radius
follows its control's: `{rounded.sm}` on buttons and inputs, `{rounded.lg}` on cards,
`{rounded.full}` on pills. No new radius value is introduced for focus.

### Photography Geometry
The brand uses minimal photography. Customer logo strips display wordmarks at uniform height (~24–32px) in greyscale; case-study cards (rare) use 4:3 photos inset in `{rounded.lg}` containers.

## Components

### Buttons

**`button-primary-green`** — the signature CTA.
- Background `{colors.primary}`, text `{colors.on-primary}` (near-black, NOT white), type `{typography.button-md}`, padding `{spacing.sm} {spacing.lg}` (8px 16px), rounded `{rounded.sm}` 6px.
- Pressed state `button-primary-green-pressed` shifts to `{colors.primary-deep}`.
- States — default `{colors.primary}`; hover `{colors.primary-deep}`; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed `{colors.primary-deep}` with no travel; disabled `{colors.hairline}` fill with `{colors.ink-faint}` label at 50% and `cursor: not-allowed`; loading label held in place with a 16px `{colors.on-primary}` spinner replacing the label, button width frozen; error not a state of this button — the message is rendered by the owning form field. Not selected-capable.

**`button-secondary-outline`** — outline alternative on white.
- Background `{colors.canvas}`, text `{colors.ink}`, 1px solid `{colors.hairline-strong}` border, same shape.
- States — default as above; hover border steps to `{colors.ink-mute}` and fill to `{colors.canvas-soft}`; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed fill `{colors.canvas-soft}`, border `{colors.ink-mute}`; disabled border `{colors.hairline-cool}` with `{colors.ink-faint}` label; loading as the primary button. Not selected-capable, no error state.

**`button-on-dark`** — used on dark surfaces / code-block CTAs.
- Background `{colors.canvas-night}`, text `{colors.on-dark}`, same shape.
- States — default as above; hover lifts to `{colors.canvas-night-soft}`; focus-visible 2px `{colors.focus}` ring at 2px offset (3.44:1 on `{colors.canvas-night}`); active/pressed back to `{colors.canvas-night}`; disabled `{colors.canvas-night-soft}` with `{colors.ink-mute-2}` label; loading as the primary button. Not selected-capable, no error state.

**`button-link`** — text-only inline button.
- Transparent background, text `{colors.ink}` rendered in `{typography.button-md}`, no padding, with a subtle underline on hover.
- States — default no underline; hover underline appears; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed text drops to `{colors.ink-mute}`; disabled `{colors.ink-faint}`, no underline; loading and selected do not apply; no error state.

### Cards & Containers

**`card-feature-light`** — feature card on white.
- Background `{colors.canvas}`, padding `{spacing.xxl}`, rounded `{rounded.lg}` 12px, 1px `{colors.hairline}` border.
- States — this card is static unless the whole card is a link. Linked: default flat with `{shadow.none}`; hover `{shadow.small}` with the border dropped (never both); focus-visible 2px `{colors.focus}` ring at 2px offset following `{rounded.lg}`; active/pressed returns to `{shadow.none}`. No disabled, loading, selected or error state.

**`card-pricing`** — standard pricing tier.
- Background `{colors.canvas}`, padding `{spacing.xxl}`, rounded `{rounded.lg}`, 1px `{colors.hairline}` border. Title in `{typography.heading-lg}`, price in `{typography.display-md}`, body in `{typography.body-md}`, CTA `button-primary-green` pinned bottom.
- States — default as above; selected (the plan the visitor has chosen) swaps the 1px `{colors.hairline}` border for 1px `{colors.primary}` plus a `pill-tag-green` label; hover `{shadow.small}`; focus-visible ring is carried by the inner CTA, not the card; the card itself has no active/pressed, disabled, loading or error state.

**`card-pricing-featured`** — inverted dark featured tier.
- Background `{colors.canvas-night}`, text `{colors.on-dark}`, otherwise identical structure. All type on this card is `{colors.on-dark}` (17.04:1) or `{colors.ink-mute-2}` (6.06:1) — the light-track inks `{colors.ink}` and `{colors.ink-secondary}` are **never** drawn here.
- States — same set as `card-pricing`: default, hover `{shadow.medium}`, selected border `{colors.primary}`; no active/pressed, disabled, loading or error state.

**`card-feature-dark`** — feature card with deep dark fill.
- Background `{colors.canvas-night}`, text `{colors.on-dark}`, padding `{spacing.xxl}`, rounded `{rounded.lg}`. Used for code-heavy feature explanations.
- States — genuinely a two-state component: default and hover (`{shadow.medium}`). No focus-visible unless the card is a link, and no active/pressed, disabled, loading, selected or error state.

**`code-block`** — code snippet container.
- Background `{colors.canvas-night}`, text `{colors.on-dark}` rendered in `{typography.code}`. Padding `{spacing.lg}` 16px, rounded `{rounded.sm}` 6px.
- States — default; hover reveals the copy affordance; the copy control takes focus-visible (2px `{colors.focus}`, 3.44:1 on this fill) and active/pressed; loading applies to a streamed log pane only, shown as a 3-dot `{colors.ink-mute-2}` pulse; error (a failed query row in a log pane) is carried by a 2px left edge in `{colors.accent-tomato}` — **prescribed**, since this palette holds no semantic error tone (see Known Gaps). No disabled or selected state.

### Inputs & Forms

**`text-input`** — standard form input.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, padding `{spacing.sm} {spacing.md}` (8px 12px), rounded `{rounded.sm}` 6px, 1px `{colors.hairline}` border.
- **Boundary contrast.** The extracted 1px `{colors.hairline}` border measures **1.33:1** against `{colors.canvas}`, below the 3:1 a control boundary needs. The border is the input's only affordance, so for the boundary to be perceivable use the tone this palette already owns for the job — 1px `{colors.ink-mute}`, **4.95:1** on `{colors.canvas}`. That substitution is **prescribed**; `{colors.hairline}` stays the extracted fact for card and table chrome, where it is decoration rather than an affordance.
- States — default as above; hover border `{colors.ink-mute}`; focus-visible 2px `{colors.focus}` ring at 2px offset *in addition to* the border, never replacing it; active/pressed is the same as focus-visible for a text field; disabled fill `{colors.canvas-soft}`, border `{colors.hairline-cool}`, placeholder `{colors.ink-faint}`; loading (async validation) shows a 14px `{colors.ink-mute}` spinner inside the right padding; selected describes the text selection only, `{colors.primary-soft}` at 30%; error border and helper text `{colors.accent-tomato}` — **prescribed**, as this palette holds no semantic error tone (see Known Gaps).

### Navigation

**`nav-bar-light`** — top nav across the site.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg} {spacing.xl}`. Logo on the left, primary nav center, "Sign In" link + filled `button-primary-green` on the right.
- States (per nav item) — default `{colors.ink}`; hover `{colors.ink-mute}`; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed `{colors.ink-mute}`; selected (current route) keeps `{colors.ink}` with a 2px `{colors.primary}` underline (**prescribed**; emerald's extracted non-CTA uses are the wordmark accent and the dot indicator); disabled items are `{colors.ink-faint}`. No loading or error state.

### Pills, Tags, and Chips

**`pill-tag-green`** — small green pill used for "new" or featured indicators.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.micro}`, padding `{spacing.xxs} {spacing.sm}`, rounded `{rounded.full}`.
- States — a label, not a control: **default only**, with no hover, focus-visible, active/pressed, disabled, loading, selected or error state. Where the same shape is used as a filter chip it becomes interactive and inherits the `pill-tag-soft` set below.

**`pill-tag-soft`** — neutral pill on light surfaces.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, otherwise same shape.
- States — default as above; hover fill `{colors.hairline-cool}`; focus-visible 2px `{colors.focus}` ring at 2px offset following `{rounded.full}`; active/pressed fill `{colors.hairline}`; selected fill `{colors.canvas-night}` with `{colors.on-dark}` text (17.04:1), which is how the brand inverts rather than greens a chosen chip; disabled text `{colors.ink-faint}`. No loading or error state.

### Signature Components

**Composited Product UI Mockups** — multi-layer dashboard / SQL editor / log pane composites with subtle Level 2 shadows. The product is the brand's argument; mockups always sit on white canvas with no surrounding decoration.
- States — decorative imagery, so **default only**: no hover, focus-visible, active/pressed, disabled, selected or error state. The one exception is loading, where each pane holds its final box and fills with a `{colors.canvas-soft}` block until the asset resolves, so no layout shift occurs.

**`link-on-light`** — inline links in body copy.
- Text `{colors.ink}` rendered in `{typography.body-md}` with a persistent underline.
- States — default underlined `{colors.ink}`; hover `{colors.ink-mute}`; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed `{colors.ink-mute}`; visited keeps `{colors.ink}`. No disabled, loading, selected or error state.

**`footer-light`** — site-wide footer.
- Background `{colors.canvas}`, text `{colors.ink-mute}`, type `{typography.caption}`, padding `{spacing.huge} {spacing.xl}` (64px 24px). Holds 4–5 columns of link groups, social icons, and a small legal row.
- States (per footer link) — default `{colors.ink-mute}` (4.95:1 on `{colors.canvas}`); hover `{colors.ink}`; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed `{colors.ink}`. The container itself is **default only** — no disabled, loading, selected or error state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or choreography below was extracted; the values are the shared **Crisp** profile, assigned because this is a developer-tool identity — database dashboard, SQL editor, log stream — where a state change should read as instant and nothing should choreograph its way in front of the product.

### Principles
- **State change reads as instant.** Base is `{motion.duration-base}` 150ms; hover and press sit at `{motion.duration-fast}` 100ms and `{motion.duration-instant}` 60ms. Nothing on a marketing surface is slow enough to be admired.
- **No entrance choreography.** The composited product mockups do not fly, scale or stagger into place on load — they hold their final box from first paint, because the product screenshot is the argument and delaying it weakens it.
- **Transform and opacity only.** Never `width`, `height`, `top`, `left` or `margin`; a mockup pane that re-lays out mid-transition is the failure mode this rule exists to prevent. `color` and `background-color` crossfades are also permitted — they are paint-only and trigger no layout — and are the main vehicle for hover on this near-monochrome palette.
- **Exit is faster than entrance,** always, using `{motion.ease-exit}`.
- **Emerald never animates.** `{colors.primary}` does not pulse, glow or breathe; the one chromatic event on the page stays still.

### Interaction Table

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, link, nav item, chip) | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `background-color`, `color`, `opacity` | Unchanged — a paint-only crossfade carries no travel |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `background-color` only; **no** scale — the brand's square-ish 6px buttons do not pop | Unchanged |
| Focus-visible ring | `{motion.duration-instant}` 60ms | `{motion.ease-enter}` | `opacity` on the 2px `{colors.focus}` ring | Ring appears instantly at full opacity; never suppressed |
| Page / route transition | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity` only, 0 → 1; no slide | Opacity fade at `{motion.duration-reduced}` 100ms |
| Modal / drawer (enter) | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` 0 → 1 and `transform: translateY(8px) → 0` | Travel removed; opacity fade at `{motion.duration-reduced}` 100ms |
| Modal / drawer (exit) | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity` 1 → 0, no travel | Opacity fade at `{motion.duration-reduced}` 100ms |
| Dropdown / nav menu (enter) | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | `opacity` and `transform: translateY(4px) → 0` | Travel removed; opacity only at `{motion.duration-reduced}` 100ms |
| Dropdown / nav menu (exit) | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` 1 → 0 | Opacity only, 60ms |
| Toast | in `{motion.duration-base}` 150ms / out `{motion.duration-fast}` 100ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` and `transform: translateY(8px)` | Travel removed; opacity only at `{motion.duration-reduced}` 100ms |
| List enter (pricing tiers, feature cards, log rows) | `{motion.duration-fast}` 100ms per item, `{motion.stagger-step}` 20ms apart, capped at 6 items | `{motion.ease-enter}` | `opacity` and `transform: translateY(4px) → 0` | Stagger and travel removed; all items fade together at `{motion.duration-reduced}` 100ms |
| List exit | `{motion.duration-instant}` 60ms, no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | Opacity only, 60ms |
| Loading (button spinner, streamed log pane, skeleton) | 800ms linear loop | `linear` | `transform: rotate()` on the spinner; `opacity` 0.4 ↔ 1 on skeletons | Loop frozen; a static `{colors.ink-mute}` indicator remains, and text status is the primary signal |

The 800ms loader loop is the only infinite animation in this system. There is no brand ambience — no drifting gradient, no breathing glow — which follows from the file's own commitment that the white canvas *is* the design.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. Every translateY above resolves to 0,
     and no transform animation runs except the loader's rotation, which is
     frozen. Stagger collapses to 0ms. */
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-property: opacity, color, background-color !important;
    transition-duration: 100ms !important;      /* {motion.duration-reduced} */
  }
}
```

**Removed:** every `transform` translate and scale, the `{motion.stagger-step}` list stagger, and the loader's rotation loop (frozen mid-frame).
**Kept:** opacity fades and paint-only `color` / `background-color` crossfades at `{motion.duration-reduced}` 100ms — never longer than 150ms; the focus ring, which appears instantly and is never suppressed; and all textual status, which is what the frozen loader falls back to.

## Accessibility

Contrast below is computed with WCAG 2.1 relative luminance from this file's own hexes. Overlap, clipping, frame rate and real tap-target size are **not** measurable from a document — the claims about them are documented intent, not verified results.

### Measured key pairs

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#171717` on `{colors.canvas}` `#ffffff` | 17.93:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` `#fafafa` | 17.18:1 | 4.5:1 | Pass |
| `{colors.ink-secondary}` `#212121` on `{colors.canvas}` | 16.10:1 | 4.5:1 | Pass |
| `{colors.ink-mute}` `#707070` on `{colors.canvas}` | 4.95:1 | 4.5:1 | Pass |
| `{colors.ink-mute-2}` `#9a9a9a` on `{colors.canvas}` | 2.81:1 | 4.5:1 | **Fail** — see below |
| `{colors.ink-faint}` `#b2b2b2` on `{colors.canvas}` | 2.12:1 | — | Exempt: placeholder / disabled only |
| `{colors.on-dark}` `#ffffff` on `{colors.canvas-night}` `#1c1c1c` | 17.04:1 | 4.5:1 | Pass |
| `{colors.ink-mute-2}` on `{colors.canvas-night}` | 6.06:1 | 4.5:1 | Pass |
| `{colors.on-primary}` `#171717` on `{colors.primary}` `#3ecf8e` | 8.98:1 | 4.5:1 | Pass — the brand's near-black-on-emerald choice is its strongest accessibility decision |
| `{colors.on-primary}` on `{colors.primary-deep}` `#24b47e` | 6.75:1 | 4.5:1 | Pass |
| `{colors.focus}` `#707070` on `{colors.canvas}` | 4.95:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.canvas-soft}` | 4.74:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.canvas-night}` | 3.44:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.canvas-night-soft}` `#202020` | 3.29:1 | 3.0:1 | Pass |

### Where this brand fails AA, stated plainly

The grey ladder is an extracted fact and is **not** altered here. It fails:

- `{colors.hairline}` `#dfdfdf` on `{colors.canvas}` measures **1.33:1**, against the 3:1 a boundary needs.
- `{colors.hairline-strong}` `#c7c7c7` on `{colors.canvas}` measures **1.69:1** — the darkest hairline in the palette, and still short of 3:1.
- `{colors.hairline-cool-3}` `#d4d4d4` on `{colors.canvas}` measures **1.48:1**.
- `{colors.hairline-cool}` `#ededed` on `{colors.canvas}` measures **1.17:1**.
- `{colors.hairline-cool-2}` `#efefef` on `{colors.canvas}` measures **1.15:1**.

The same five tones are measured again on the `{colors.canvas-soft}` `#fafafa` band, which is the file's nearest thing to a raised surface, and every one is slightly worse than on white: `{colors.hairline-strong}` **1.62:1**, `{colors.hairline-cool-3}` **1.42:1**, `{colors.hairline}` **1.28:1**, `{colors.hairline-cool}` **1.12:1**, `{colors.hairline-cool-2}` **1.10:1**. The two muted inks fall with them: `{colors.ink-mute-2}` **2.70:1** and `{colors.ink-faint}` **2.03:1** on `{colors.canvas-soft}`. A 1.04:1 band does not help a boundary — layering here rests on the tone's own edge, not on the surface under it.

So **no hairline tone in this brand reaches 3:1 on white.** For pure separation — table rules, card edges, section dividers — that is acceptable under WCAG, which sets no contrast floor on decoration. It is **not** acceptable where the hairline is a control's only boundary. The one such case in this file is `text-input`: its boundary is prescribed as 1px `{colors.ink-mute}` at **4.95:1**, a tone the palette already owns, while `{colors.hairline}` keeps its extracted role on card and table chrome. Re-binding the other hairline usages is a brand-owner decision and is listed under Needs approval in the audit report, not decided here.

`{colors.ink-mute-2}` `#9a9a9a` at **2.81:1** on white is below AA for body copy. It is defensible only as 18px+ / 14px-bold large text, where 3:1 applies — and it does not reach even that on white. Use `{colors.ink-mute}` (4.95:1) for any tertiary text that must be read on the light track; reserve `{colors.ink-mute-2}` for the dark track, where it measures 6.06:1 on `{colors.canvas-night}`.

### Two pairs this document does not render

Two further pairs measure badly but describe a composition the brand never draws, and are recorded here so they are not mistaken for real defects:

- `{colors.ink}` `#171717` on `{colors.canvas-night}` `#1c1c1c` — **1.05:1**. Every component this file binds to `{colors.canvas-night}` (`card-pricing-featured`, `card-feature-dark`, `code-block`, `button-on-dark`) sets its text to `{colors.on-dark}` at 17.04:1. The light-track ink is never placed on the dark track.
- `{colors.ink-secondary}` `#212121` on `{colors.canvas-night}` — **1.06:1**. The same reason; secondary emphasis on the dark track is `{colors.ink-mute-2}` at 6.06:1.

### Focus ring visibility, surface by surface

One ring serves the whole file: 2px `{colors.focus}` `#707070` at `outline-offset: 2px`, drawn outside the control so it is judged against the surface behind it. Measured above: **4.95:1** on `{colors.canvas}`, **4.74:1** on `{colors.canvas-soft}`, **3.44:1** on `{colors.canvas-night}`, **3.29:1** on `{colors.canvas-night-soft}` — all clear of 3:1, which is why this file needs no second polarity-named ring. The ring reuses the hex the palette already carries as `{colors.ink-mute}`; it is not a new brand colour. Because it is offset outside the control, it is never measured against a control fill — notably `{colors.primary}`, where `#707070` would reach only 2.48:1.

### Tap targets

The Responsive Behavior section documents buttons at ≥ 36×36px and form fields at a 36px minimum height. 36px is below the 44×44px of WCAG 2.5.5 (AAA) and meets 2.5.8 Target Size (Minimum, AA) at 24×24px. Rendered size cannot be verified from this document; treat 36px as the documented intent and re-measure in a build.

### Reduced motion

Honoured as specified in Motion & Animation: all travel, scale and stagger removed, the loader loop frozen, opacity and paint-only crossfades kept at `{motion.duration-reduced}` 100ms, and the focus ring always instant and never suppressed.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` emerald for filled CTAs and the wordmark accent — it should appear sparingly.
- Render display tiers at weight 500 with negative letter-spacing — the engineered tightness is part of the brand.
- Use `{rounded.sm}` 6px for buttons — square-ish radii, never pill-shaped.
- Composite product UI mockups inside `{rounded.lg}` containers with subtle Level 2 shadows.
- Use near-black `{colors.ink}` on the emerald button (not white) — the green reads as "lit" with dark type, which is the brand's idiosyncratic choice.
- Apply system mono for every code block.
- Draw the focus ring as 2px `{colors.focus}` at 2px offset, outside the control, on every interactive element on both the light and the dark track.
- Express depth as a hairline **or** a `{shadow.*}` step, never both on the same element.

### Don't
- Don't introduce additional accent colors as system colors — purples, yellows, and pinks belong inside chart points and integration logos only.
- Don't bump display weight above 500 — the brand's calibrated mid-weight breaks at 600+.
- Don't use pill-shaped buttons; the brand's button radius is square-ish 6px.
- Don't use white text on the emerald button — the brand specifically uses near-black on green.
- Don't add atmospheric gradients to hero bands — the white canvas is the design.
- Don't use `outline: none` without a replacement ring, and don't tint the ring emerald — `{colors.primary}` measures 2.00:1 on white and cannot carry a focus indicator.
- Don't animate `width`, `height`, `top`, `left` or `margin`; a mockup pane that re-lays out mid-transition is the failure this rule prevents.
- Don't choreograph entrances for the product mockups — they hold their final box from first paint.
- Don't place `{colors.ink}` or `{colors.ink-secondary}` on `{colors.canvas-night}`; the dark track's inks are `{colors.on-dark}` and `{colors.ink-mute-2}`.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1440px | Full container width; product mockups at full scale |
| Desktop | 1024–1440px | Default content max-width; pricing 4-up |
| Tablet | 768–1023px | Pricing 2-up; mockups simplify to single panel |
| Mobile | < 768px | Pricing 1-up; hamburger nav; display drops 64 → 36px |

### Touch Targets
- Buttons hit ≥ 36×36px on mobile; vertical padding scales up to maintain WCAG AA minimum.
- Form fields stay at 36px minimum height.

### Collapsing Strategy
- Display tiers stair-step 64 → 48 → 36 → 28 → 22px.
- Product UI mockups simplify to a single primary panel on mobile.
- Pricing tiers stair-step 4-up → 2-up → 1-up; dark featured tier always distinguished.

### Image Behavior
Product UI mockups use `srcset` with desktop / mobile crops; mobile crops focus on the most actionable inner panel.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly.
3. Run `npx @google/design.md lint DESIGN.md` after edits.
4. Default body to `{typography.body-md}`; use `{typography.code}` for any developer-facing snippet.
5. Keep emerald scarce; one filled green button per viewport.
6. The white-canvas commitment is non-negotiable — adding atmospheric backdrops breaks the brand.
7. Take motion values from `{motion.*}` rather than typing durations; the Crisp profile is shared with the other developer-tool files and drifting from it breaks that comparability.

## Known Gaps

- **Motion is prescribed, not extracted.** No duration, easing curve, stagger or choreography in Motion & Animation was measured from the live site. The whole `motion:` group is the shared **Crisp** profile, assigned from this file's own developer-tool identity. Treat every value as a defensible default, not a brand fact.
- **The focus ring is prescribed.** `{colors.focus}` `#707070` reuses the hex the palette already owns as `{colors.ink-mute}`; the live site's real ring colour, width and offset were not observed. The 2px width and 2px offset are prescribed, chosen so one ring clears 3:1 on both the light and the dark track.
- **No semantic colour family.** This palette has no success, warning, error or info tone. The error states named for `text-input` and `code-block` fall back to `{colors.accent-tomato}` `#ff2201` (3.83:1 on `{colors.canvas}`) as a prescribed stand-in; the real product's error styling was not observed, and a brand owner should supply a proper semantic ramp rather than promoting an integration-logo accent.
- **No `surface` token.** The brand's raised neutral is not named: light cards sit on `{colors.canvas}` white and are separated by a hairline rather than by a tone, and `{colors.canvas-soft}` `#fafafa` is a section band, not a card fill. No `surface*` token is invented here to fill the role, because doing so would describe a layer the brand does not draw. The practical consequence is that `canvas` → `surface` separation is 1.04:1 — the system leans entirely on hairlines and `{shadow.*}` for layering.
- **No hairline reaches 3:1 on white.** Recorded with measurements in Accessibility. Whether the card, table and divider hairlines should be re-bound to an accessible tone is a brand-owner decision and is left open.
- **Dark-track greys are thin.** `{colors.canvas-night}` `#1c1c1c` and `{colors.canvas-night-soft}` `#202020` separate by only 1.05:1, so nested chrome on the dark track is effectively invisible without a border. The extracted values are kept as-is.
- **Circular is proprietary.** All type metrics are recorded against Circular, which cannot be licensed openly; the Inter and Geist Sans substitutions are approximations and their real optical sizes were not compared side by side.
- **Tap targets are documented, not measured.** 36×36px is the file's stated intent; no rendered page was available to verify it, and nothing here can speak to overlap, clipping, overflow or layout shift.
- **Hover and press behaviour for the composited mockups is unobserved.** Whether the real site's dashboard panes respond to pointer input at all was not captured, so they are documented as decorative.
