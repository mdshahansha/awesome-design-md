---
version: alpha
name: Slack-Inspired-design-analysis
description: An inspired interpretation of Slack's design language — a workplace messaging brand built on a deep aubergine primary, with cream-lavender hero gradients, blue inline links, and pill CTAs. The system pairs a proprietary humanist sans for display with a separate utility sans for body, and stages product UI mockups inside soft pastel-mesh hero composites that act as both decoration and feature explanation.

colors:
  primary: "#4a154b"
  primary-deep: "#481a54"
  primary-press: "#611f69"
  primary-tint: "#592466"
  on-primary: "#ffffff"
  ink: "#1d1d1d"
  ink-mute: "#696969"
  link-blue: "#1264a3"
  link-hover: "#3860be"
  canvas: "#ffffff"
  canvas-cream: "#f4ede4"
  canvas-lavender: "#f9f0ff"
  surface-elev: "#ffffff"
  surface-aubergine: "#4a154b"
  hairline: "#e6e6e6"
  hairline-strong: "#000000"
  semantic-error: "#cc4117"
  semantic-success: "#007a5a"
  on-aubergine-mute: "#d9bdde"
  focus: "#1264a3"
  focus-on-dark: "#d9bdde"

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

typography:
  display-xxl:
    fontFamily: "Salesforce-Avant-Garde, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.768px
  display-xl:
    fontFamily: "Salesforce-Avant-Garde, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 58px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.464px
  display-lg:
    fontFamily: "Salesforce-Avant-Garde, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 50px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.6px
  display-md:
    fontFamily: "Salesforce-Avant-Garde, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.256px
  heading-lg:
    fontFamily: "Salesforce-Avant-Garde, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.096px
  heading-md:
    fontFamily: "Salesforce-Avant-Garde, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  heading-sm:
    fontFamily: "Salesforce-Avant-Garde, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: -0.0216px
  body-lg:
    fontFamily: "Salesforce-Sans, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: -0.0216px
  body-md:
    fontFamily: "Salesforce-Sans, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-strong:
    fontFamily: "Salesforce-Sans, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.16px
  button-lg:
    fontFamily: "Salesforce-Sans, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  button-md:
    fontFamily: "Salesforce-Sans, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0.2px
  button-cap:
    fontFamily: "Salesforce-Sans, system-ui, -apple-system, sans-serif"
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.144px
  caption:
    fontFamily: "Salesforce-Sans, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.1px
  micro-cap:
    fontFamily: "Salesforce-Sans, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.96px

rounded:
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 48px
  pill: 90px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  xxl: 24px
  huge: 28px

shadow:
  elev-1: "rgba(0,0,0,0.1) 0 5px 20px 0"
  elev-2: "rgba(0,0,0,0.1) 0 0 32px 0"
  elev-3: "rgba(0,0,0,0.2) 0 1px 10px 0"
  elev-4-inset: "rgb(97,31,105) 0 0 0 1px inset"

components:
  button-primary-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  button-primary-pill-pressed:
    backgroundColor: "{colors.primary-press}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  button-secondary-pill:
    backgroundColor: "{colors.canvas-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 10px 30px
  button-outline-aubergine:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  button-outline-on-aubergine:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
  pill-cap-shade:
    backgroundColor: "{colors.canvas-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-cap}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  card-pricing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  card-pricing-featured:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  card-feature-cream:
    backgroundColor: "{colors.canvas-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  card-aubergine-band:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.xl}"
    padding: 48px
  card-stat:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.xl}"
    padding: 32px
  nav-bar-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  link-on-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link-blue}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
  link-on-aubergine:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
  footer-aubergine:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 32px 24px
---

## Overview

Slack's design language centers on a deep aubergine primary (`{colors.primary}`) — the brand's most enduring visual asset — applied as the dominant button color, the footer band, the featured pricing tier, and the brand wordmark. Around that aubergine the system stages an unusually delicate ecosystem: cream-lavender hero canvases with soft pastel-mesh gradients (peachy oranges, lavenders, dusty greens) that pulse behind floating product UI mockups, with the actual interface chrome rendered in fine detail at 3:2 aspect.

Typography splits between two proprietary humanist sans families. The display tier runs at 700 weight at sizes 32–64px with negative letter-spacing for tight optical density on hero headlines. The UI tier uses the second family at 400–700 with slightly relaxed leading (1.55) — the brand's body copy reads quietly without competing with the aubergine moments.

Buttons are pill-shaped at 90px radius with an unusual amount of horizontal padding (28–30px), giving them a distinctly comfortable, almost over-padded feel. The primary aubergine pill is the only filled button in most contexts; secondary actions use a soft lavender pill (`{colors.canvas-lavender}`) which reads as a gentler echo of the primary surface. Inline links shift to a saturated blue (`{colors.link-blue}`) — the brand's only chromatic departure from the aubergine-and-cream world.

**Key Characteristics:**
- Single aubergine primary (`{colors.primary}`) reused across CTAs, the featured pricing tier, the footer band, and the wordmark — the brand's chromatic monotheism.
- Cream-lavender hero canvas (`{colors.canvas-cream}` / `{colors.canvas-lavender}`) with diffused pastel-mesh atmospheric gradients and floating UI mockups composited above.
- Pill buttons at `{rounded.pill}` (90px radius) with generous 28–30px horizontal padding — over-padded by SaaS-default standards, deliberately so.
- Tight negative letter-spacing on display sizes (-0.768px on 64px hero) for editorial-density headlines.
- Blue inline links (`{colors.link-blue}`) — the only non-aubergine chromatic accent in body type.
- Pastel-mesh gradient atmospherics: every hero band has a subtle peach-lavender-dusty-green wash behind it; product UI sits on top, never inside, the gradient.
- Statistics cards rendered in massive aubergine display type (90% / 43 / 87%) on white — quantitative emphasis through scale alone.

## Colors

> **Source pages:** home (`/`), `/features/channels`, `/pricing`, `/contact-sales`.

### Brand & Accent
- **Aubergine** (`{colors.primary}` — `#4a154b`): The brand's primary surface and CTA color. Deep, warm purple with a hint of ruby — used on filled buttons, the featured pricing tier, the footer band, and the brand wordmark.
- **Aubergine Deep** (`{colors.primary-deep}` — `#481a54`): A near-identical sibling of `{colors.primary}` extracted from a different surface; treat as functionally equivalent.
- **Aubergine Press** (`{colors.primary-press}` — `#611f69`): Pressed-state lift of the primary, slightly lighter and warmer.
- **Aubergine Tint** (`{colors.primary-tint}` — `#592466`): Border accent on aubergine-on-aubergine surfaces. Extracted and frozen; it measures **1.25:1 on `{colors.primary}`**, so it is a decorative seam only. Where a boundary on aubergine must be perceivable, draw it in `{colors.on-aubergine-mute}` (8.19:1 on `{colors.surface-aubergine}`).
- **Link Blue** (`{colors.link-blue}` — `#1264a3`): Inline link color — saturated, slightly warm blue. The only chromatic alternative to aubergine in body type.
- **Link Hover** (`{colors.link-hover}` — `#3860be`): A more saturated blue used on link hover state.

### Surface
- **Canvas White** (`{colors.canvas}` — `#ffffff`): Default content surface.
- **Canvas Cream** (`{colors.canvas-cream}` — `#f4ede4`): Warm off-white used on hero gradients and feature bands. Adds editorial warmth.
- **Canvas Lavender** (`{colors.canvas-lavender}` — `#f9f0ff`): Pale lavender tint used as the secondary-button surface and as a soft section band.
- **Surface Aubergine** (`{colors.surface-aubergine}` — `#4a154b`): The primary aubergine reused as a surface — featured pricing tier, footer, dark feature bands.
- **Hairline** (`{colors.hairline}` — `#e6e6e6`): 1px borders on cards and table dividers. Extracted and frozen. It measures **1.25:1 on `{colors.canvas}`** — well under the 3:1 a perceivable boundary needs, so treat it as *decoration*: a card edge the layout already implies, not the only thing marking an interactive control.
- **Hairline Strong** (`{colors.hairline-strong}` — `#000000`): the accessible boundary tone, 21:1 on `{colors.canvas}`. Use it wherever a boundary carries meaning rather than decoration — the `text-input` outline above all, since the hairline is that field's only edge. Origin unverified (see Known Gaps).

### Focus
- **Focus** (`{colors.focus}` — `#1264a3`): focus ring on all light grounds. This is the same hex the palette already owns as `{colors.link-blue}`, reused rather than introduced — it is not a new brand colour. 6.22:1 on `{colors.canvas}`, 5.35:1 on `{colors.canvas-cream}`, 5.61:1 on `{colors.canvas-lavender}`.
- **Focus On Dark** (`{colors.focus-on-dark}` — `#d9bdde`): focus ring on the aubergine surfaces, where the blue ring collapses. Same hex as `{colors.on-aubergine-mute}`, reused. 8.19:1 on `{colors.surface-aubergine}`.

### Text
- **Ink** (`{colors.ink}` — `#1d1d1d`): Primary body text on light surfaces. Just shy of pure black.
- **Ink Mute** (`{colors.ink-mute}` — `#696969`): Secondary text, captions, helper copy.
- **On Primary** (`{colors.on-primary}` — `#ffffff`): Text on aubergine surfaces and filled CTAs.
- **On Aubergine Mute** (`{colors.on-aubergine-mute}` — `#d9bdde`): Secondary text on aubergine surfaces — a desaturated mauve that reads as muted-light.

### Semantic
- **Error** (`{colors.semantic-error}` — `#cc4117`): Form error and destructive-action color.
- **Success** (`{colors.semantic-success}` — `#007a5a`): Inline success indicators.

## Typography

### Font Family

The display tier is **Salesforce Avant Garde** — a proprietary humanist sans with broad apertures and a slightly geometric character. When unavailable, fall back to the system font stack (`system-ui, -apple-system, BlinkMacSystemFont`).

The UI tier is **Salesforce Sans** — a separate proprietary face used for body, captions, and button labels. Same fallback chain.

Both faces are proprietary and not freely available. Substitute with **Inter** (open-source via Google Fonts) at matching weights for both display and body — Inter is the closest open analogue across both tiers.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 64px | 700 | 1.12 | -0.768px | Marketing hero headline |
| `{typography.display-xl}` | 58px | 600 | 1.25 | -0.464px | Section openers |
| `{typography.display-lg}` | 50px | 700 | 1.12 | -0.6px | Statistics callouts |
| `{typography.display-md}` | 32px | 700 | 1.25 | -0.256px | Card / feature titles |
| `{typography.heading-lg}` | 24px | 700 | 1.33 | -0.096px | Pricing tier names |
| `{typography.heading-md}` | 22px | 600 | 1.4 | 0 | Sub-section heading |
| `{typography.heading-sm}` | 18px | 600 | 1.56 | -0.0216px | Compact card title |
| `{typography.body-lg}` | 18px | 400 | 1.55 | -0.0216px | Marketing body lead |
| `{typography.body-md}` | 16px | 400 | 1.55 | 0 | Default UI body |
| `{typography.body-strong}` | 16px | 700 | 1.5 | 0.16px | Emphasized body |
| `{typography.button-lg}` | 18px | 700 | 1.0 | 0 | Hero pill button label |
| `{typography.button-md}` | 16px | 700 | 1.38 | 0.2px | Standard pill button label |
| `{typography.button-cap}` | 14.4px | 700 | 1.0 | 0.144px | Compact pill label |
| `{typography.caption}` | 14px | 400 | 1.43 | 0.1px | Helper, footnote |
| `{typography.micro-cap}` | 12px | 700 | 1.0 | 0.96px | All-caps eyebrow |

### Principles
- **Tight tracking on display.** Negative letter-spacing across 32–64px sizes; the proprietary face is wide by default, the negative tracking pulls it into editorial density.
- **Body at 1.55 leading.** Slightly relaxed for marketing readability without crossing into airy / 1.7+ territory.
- **Caps for eyebrows.** All eyebrows render uppercase with positive 0.96–0.144px tracking depending on size.

### Note on Font Substitutes
Use **Inter** (open-source Google Fonts) for both display and UI tiers — Inter at 700 weight with `-0.768px` letter-spacing closely approximates the brand's display behavior. For maximum brand fidelity, **Lato** is a softer humanist alternative that pairs well at body sizes. Avoid System UI fonts on the body — the brand's subtle warmth disappears at default weights.

## Layout

### Spacing System
- **Base unit**: 8px (with 4 / 12 / 16 / 20 / 24 / 28 sub-tokens for fine vertical rhythm).
- **Tokens**: `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 20px · `{spacing.xxl}` 24px · `{spacing.huge}` 28px.
- **Section padding**: 64–96px on marketing surfaces; tightens to 48px on transactional pages.
- **Card internal padding**: 32px on pricing cards; 48px on aubergine band cards.

### Grid & Container
- Marketing pages center in a ~1240px container with edge-bleeding pastel-mesh gradients escaping the container.
- Pricing collapses 4-up → 2-up → 1-up at 992 / 768 breakpoints.
- Statistics row: 3-column grid with massive 50px aubergine display numerals.

### Whitespace Philosophy
The pastel-mesh gradients fill most of the negative space on marketing pages — sections feel expansive without being literally empty. On transactional pages the gradients drop, and whitespace reverts to traditional 48px-section breathing room.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default surface |
| 1 | `{shadow.elev-1}` — `box-shadow: rgba(0,0,0,0.1) 0 5px 20px 0` | Floating buttons on hero |
| 2 | `{shadow.elev-2}` — `box-shadow: rgba(0,0,0,0.1) 0 0 32px 0` | Product UI mockup composites |
| 3 | `{shadow.elev-3}` — `box-shadow: rgba(0,0,0,0.2) 0 1px 10px 0` | Toast / notification chrome |
| 4 | `{shadow.elev-4-inset}` — `box-shadow: rgb(97,31,105) 0 0 0 1px inset` | Aubergine inset border (special chrome). Note: this inset ring is **not** the focus indicator — focus is the 2px outside ring in `{colors.focus}` / `{colors.focus-on-dark}` (see Accessibility), since an inset ring cannot be judged against the surface behind the control. |

### Decorative Depth
The brand's depth language is the **pastel-mesh gradient** — peach, lavender, dusty green stops blurred together at large radii to create soft atmospheric backdrops behind product UI screenshots. The gradient is the brand's flavor of "depth without shadows": the eye perceives the product mockup as floating above a luminous backdrop without any literal lift.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | Hairline tags, status pills (rare) |
| `{rounded.sm}` | 4px | Form inputs |
| `{rounded.md}` | 8px | Compact card chrome, video frames |
| `{rounded.lg}` | 12px | Mid-size cards, secondary surface |
| `{rounded.xl}` | 16px | Pricing cards, feature cards |
| `{rounded.xxl}` | 48px | Stat badge backdrops |
| `{rounded.pill}` | 90px | All buttons |

### Photography Geometry
The brand uses **product UI screenshots** more than photography. UI mockups sit on top of pastel-mesh gradients at roughly 4:3 aspect, with no shadow but with the gradient providing the "lift" the eye expects. Real photography appears in customer-logo strips and the occasional case-study card, treated as full-bleed inside `{rounded.xl}` containers.

## Components

### Buttons

**`button-primary-pill`** — the dominant CTA system-wide.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button-md}`, padding `14px 28px`, rounded `{rounded.pill}` 90px.
- Pressed state `button-primary-pill-pressed` shifts background to `{colors.primary-press}`.
- States — default `{colors.primary}`; hover `{colors.primary-deep}`; focus-visible 2px `{colors.focus}` ring at 2px offset outside the pill; active/pressed `{colors.primary-press}` with the press pop of `{motion.duration-instant}`; disabled `{colors.primary}` at 40% opacity, pointer events off; loading keeps the aubergine fill and swaps the label for a spinner in `{colors.on-primary}`; selected does not apply (a CTA is never a selectable control); error does not apply — form errors surface on `text-input`, never on the submit pill.

**`button-secondary-pill`** — the soft lavender alternative.
- Background `{colors.canvas-lavender}`, text `{colors.ink}`, padding `10px 30px`, same pill geometry. Used as the second action beside the primary aubergine pill.
- States — default `{colors.canvas-lavender}`; hover deepens the lavender fill; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed scales to 0.97 over `{motion.duration-instant}`; disabled 40% opacity; loading spinner in `{colors.ink}`; selected and error do not apply.

**`button-outline-aubergine`** — outline variant on white surfaces.
- Background `{colors.canvas}`, text `{colors.primary}`, 2px solid `{colors.primary}` border, same pill shape.
- States — default as above (border 14:1 on `{colors.canvas}`); hover fills with `{colors.canvas-lavender}`; focus-visible 2px `{colors.focus}` ring at 2px offset outside the 2px aubergine border; active/pressed border and label shift to `{colors.primary-press}`; disabled 40% opacity; loading spinner in `{colors.primary}`; selected and error do not apply.

**`button-outline-on-aubergine`** — outline on aubergine canvas.
- Background `{colors.surface-aubergine}` (transparent over the surface), text `{colors.on-primary}`, 2px solid `{colors.on-primary}` border, same pill shape.
- States — default as above; hover fills with `{colors.on-primary}` and inverts the label to `{colors.primary}`; focus-visible 2px `{colors.focus-on-dark}` ring at 2px offset (the light-ground `{colors.focus}` blue reaches only 2.25:1 here and must not be used); active/pressed scales to 0.97; disabled 40% opacity; loading spinner in `{colors.on-primary}`; selected and error do not apply.

### Cards & Containers

**`card-pricing`** — standard pricing tier card.
- Background `{colors.canvas}`, padding `{spacing.xxl}+` (32px), rounded `{rounded.xl}` 16px, 1px `{colors.hairline}` border. Title in `{typography.heading-lg}`, price in `{typography.display-md}`, body in `{typography.body-md}`, CTA pinned to bottom as `button-primary-pill`.
- The `{colors.hairline}` border is the extracted value and measures 1.25:1 on `{colors.canvas}`: decorative here, since the card's own padding and the grid carry the grouping. Re-binding it to `{colors.hairline-strong}` is a brand-owner decision, not an audit one.
- States — default flat; hover raises to elevation 1; focus-visible, when the whole card is a link, draws a 2px `{colors.focus}` ring at 2px offset; active/pressed scales to 0.99; selected marks the chosen tier with a 2px `{colors.primary}` edge; disabled, loading and error do not apply to a static pricing card.

**`card-pricing-featured`** — the inverted aubergine featured tier.
- Background `{colors.surface-aubergine}`, text `{colors.on-primary}`, otherwise identical to `card-pricing`. The aubergine fill is the brand's signature featured-tier choice.
- States — default, hover (elevation 1) and selected (2px `{colors.on-primary}` edge) only; focus-visible uses `{colors.focus-on-dark}`. Disabled, loading, active and error do not apply.

**`card-feature-cream`** — feature explanation card on the cream track.
- Background `{colors.canvas-cream}`, text `{colors.ink}`, rounded `{rounded.xl}`, padding 32px.
- States — default and hover only (hover lifts the card 2px over `{motion.duration-fast}`); it is a static explanation card, so focus-visible appears only on links inside it, in `{colors.focus}`.

**`card-aubergine-band`** — large horizontal band card with aubergine fill, often containing the closing CTA of a marketing page.
- Background `{colors.surface-aubergine}`, text `{colors.on-primary}`, padding 48px, rounded `{rounded.xl}` 16px.

**`card-stat`** — statistics callout card.
- Background `{colors.canvas}`, text `{colors.primary}` rendered in `{typography.display-lg}` (50px aubergine numeral). Holds a single percentage/number with a small caption underneath.
- States — default only. It is non-interactive: no hover, focus-visible, active, disabled, selected or error state exists. Where the numeral is populated asynchronously, the loading state is a `{colors.canvas-cream}` block at the numeral's own size, pulsing opacity only.

### Inputs & Forms

**`text-input`** — standard form field.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, padding `10px 12px`, rounded `{rounded.sm}` 4px, 1px `{colors.hairline}` border.
- The extracted `{colors.hairline}` border is this field's only edge, and at 1.25:1 on `{colors.canvas}` it fails the 3:1 a control boundary needs — the real brand fails AA at this point. Draw the field in `{colors.hairline-strong}` (21:1) where the implementation can choose; the extracted binding above is left as found.
- States — default as above; hover darkens the border; focus-visible 2px `{colors.focus}` ring at 1px offset, replacing the 1px border; active is the same as focus-visible while typing; disabled 40% opacity on border and placeholder; loading shows a trailing spinner in `{colors.ink-mute}`; selected does not apply; error swaps the border and helper text to `{colors.semantic-error}` (4.84:1 on `{colors.canvas}`).

### Navigation

**`nav-bar-light`** — top nav across all marketing pages.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg} {spacing.xxl}`. Logo wordmark on the left, nav items center, two pill buttons on the right (`button-secondary-pill` for "Sign In", `button-primary-pill` for "Try For Free").
- Nav item states — default `{colors.ink}`; hover underlines in `{colors.primary}`; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed shifts to `{colors.primary-press}`; selected (current section) keeps a persistent 2px `{colors.primary}` underline; disabled 40% opacity; loading and error do not apply to navigation.

### Pills, Tags, and Chips

**`pill-cap-shade`** — small all-caps pill used as eyebrow above pricing-tier titles.
- Background `{colors.canvas-cream}`, text `{colors.ink}`, type `{typography.micro-cap}`, padding `4px 12px`, rounded `{rounded.pill}`.
- States — default only. It is a label, not a control: no hover, focus-visible, active, disabled, loading, selected or error state.

### Signature Components

**Pastel-Mesh Gradient Backdrop** — peach (`#fff0e6`-ish) + lavender (`#e9d8ff`) + dusty green stops blurred together behind hero bands. Implemented as a CSS radial-gradient stack, not a single image. Provides the brand's depth/luminosity without literal shadows.

**Floating Product UI Mockup** — product screenshots framed in `{rounded.lg}` (12px) containers, positioned above the pastel-mesh gradient with no border or shadow. The gradient does the lifting.

**Aubergine Footer Band** — every marketing page closes with a full-bleed `card-aubergine-band` containing a closing CTA in white type. The band height is generous (~480–600px on desktop) and reads as the page's signature.

**`link-on-light`** — inline links in body copy on light surfaces.
- Text `{colors.link-blue}` rendered in `{typography.body-md}`. No underline by default; underline appears on hover via the link-hover behavior.
- States — default `{colors.link-blue}` (6.22:1 on `{colors.canvas}`); hover `{colors.link-hover}` plus underline; focus-visible 2px `{colors.focus}` ring at 2px offset; active/pressed `{colors.primary-press}`; disabled `{colors.ink-mute}` with the underline removed; loading, selected and error do not apply.

**`link-on-aubergine`** — links inside aubergine surfaces.
- Text `{colors.on-primary}` with persistent underline.
- States — default, hover (`{colors.on-aubergine-mute}`) and focus-visible (2px `{colors.focus-on-dark}` ring at 2px offset) only; the underline is permanent, so no active, disabled, loading, selected or error state is defined.

**`footer-aubergine`** — site-wide footer.
- Background `{colors.surface-aubergine}`, text `{colors.on-primary}` rendered in `{typography.caption}`, padding `{spacing.huge}+ {spacing.xxl}` (32px 24px). Holds 4–5 columns of `{colors.on-aubergine-mute}` link groups, social icons, and a small legal/copyright row at the bottom.
- Footer link states — default `{colors.on-aubergine-mute}` (8.19:1 on `{colors.surface-aubergine}`); hover `{colors.on-primary}` with underline; focus-visible 2px `{colors.focus-on-dark}` ring at 2px offset; active/pressed `{colors.on-aubergine-mute}` at 80% opacity; disabled, loading, selected and error do not apply.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted; they are the **Playful** profile from the audit spec, chosen because the brand puts a saturated aubergine on every interactive pill, documents a distinct press colour, and speaks in over-padded, friendly geometry. Treat every value as a proposal a brand owner can accept or reject.

Only `transform` and `opacity` are animated. Never animate `width`, `height`, `top`, `left` or `margin` — the pastel-mesh backdrop and the floating product mockup both sit in flow, and animating layout on them would shift the hero composite.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, nav item, card) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `transform: scale(1.02)` | Colour change only; no scale |
| Press (pill) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.97)` | No scale; the `{colors.primary-press}` fill alone signals the press |
| Focus (ring appears) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears with no transition — never delayed, never faded |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` | Fade at `{motion.duration-reduced}`; no travel |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px) → 0` | Fade at `{motion.duration-reduced}`; no travel, no overshoot |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform: translateY(8px)` | Fade at `{motion.duration-reduced}`; no travel |
| Dropdown (nav menu, hamburger panel) | `{motion.duration-fast}` enter / `{motion.duration-instant}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: scale(0.98) → 1` from the trigger edge | Fade at `{motion.duration-reduced}`; no scale |
| Toast / notification chrome | `{motion.duration-base}` enter / `{motion.duration-fast}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px) → 0` | Fade at `{motion.duration-reduced}`; appears in place |
| List enter (pricing tiers, feature cards) | `{motion.duration-base}`, staggered `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px) → 0` | All items fade together at `{motion.duration-reduced}`; stagger and travel removed |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Fade at `{motion.duration-reduced}`; no scale |
| Loading (button spinner, stat skeleton) | 900ms loop, infinite | linear (spinner) / `{motion.ease-standard}` (skeleton) | `transform: rotate()` on the spinner; `opacity` 0.6 → 1 on the skeleton | Spinner rotation stops and becomes a static indicator; skeleton holds a flat `{colors.canvas-cream}` fill with no pulse |

The pastel-mesh gradient does **not** animate. The Overview's language of gradients that "pulse" describes their optical softness, not a running animation — the brand has no documented ambient motion, and none is prescribed here.

Exit is shorter than its matching entrance in every row above. Nothing animates on first paint: the hero headline, the mesh backdrop and the product mockup render immediately, and list stagger applies only to content entering after the first paint.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translate), all scale, the press pop, the list
     stagger, and the loading spinner's rotation. */
  /* Kept: opacity fades, capped at 130ms via {motion.duration-reduced},
     and the focus ring, which appears instantly in both modes. */
  *, *::before, *::after {
    transition-property: opacity;
    transition-duration: 130ms;   /* {motion.duration-reduced} */
    animation-iteration-count: 1;
  }
}
```

## Accessibility

Ratios below are computed with WCAG 2.1 relative luminance from this file's own token values. Nothing here is measured from a rendered page: tap-target size, overlap and focus-order claims would need a live DOM, and the two noted below are geometric arithmetic, not observation.

### Measured contrast — key pairs

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 16.86:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-cream}` | 14.51:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-lavender}` | 15.2:1 | 4.5:1 | Pass |
| `{colors.ink-mute}` on `{colors.canvas}` | 5.49:1 | 4.5:1 | Pass |
| `{colors.ink-mute}` on `{colors.canvas-cream}` | 4.73:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 14:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary-press}` | 11:1 | 4.5:1 | Pass |
| `{colors.on-aubergine-mute}` on `{colors.surface-aubergine}` | 8.19:1 | 4.5:1 | Pass |
| `{colors.link-blue}` on `{colors.canvas}` | 6.22:1 | 4.5:1 | Pass |
| `{colors.link-hover}` on `{colors.canvas}` | 5.86:1 | 4.5:1 | Pass |
| `{colors.semantic-error}` on `{colors.canvas}` | 4.84:1 | 4.5:1 | Pass |
| `{colors.semantic-success}` on `{colors.canvas}` | 5.34:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 21:1 | 3:1 | Pass |

### Where the real brand fails AA

- **`{colors.hairline}` (`#e6e6e6`) on `{colors.canvas}` measures 1.25:1**, against the 3:1 a component boundary needs. This is an extracted, frozen value, so it is not corrected in place. It is scoped to decoration above, and `{colors.hairline-strong}` carries the boundary job. On `text-input`, where the hairline is the field's only edge, **the real brand fails WCAG 2.1 non-text contrast.** Re-binding the extracted `text-input` and `card-pricing` borders is left to the brand owner.
- **`{colors.primary-tint}` (`#592466`) on `{colors.primary}` measures 1.25:1**, against the same 3:1. Also extracted and frozen; it is a decorative seam on aubergine-on-aubergine chrome, and `{colors.on-aubergine-mute}` carries any boundary that has to be seen.
- The same frozen hairline is weaker still on the tinted bands: **1.07:1 on `{colors.canvas-cream}`** and **1.13:1 on `{colors.canvas-lavender}`**. A card edge drawn on either band is effectively invisible, so on those grounds the boundary must come from `{colors.hairline-strong}` or from spacing alone.
- **`{colors.on-aubergine-mute}` (`#d9bdde`) on light grounds is a manufactured pair, not a real one: 1.71:1 on `{colors.canvas}` and 1.54:1 on `{colors.canvas-lavender}`.** The token names its own ground — it is drawn only on aubergine, where it reaches 8.19:1 — and the file never places it on a light surface. The actual light-ground secondary ink is `{colors.ink-mute}` at 5.49:1, which passes. These two ratios are recorded only because the harness measures every `on-*-mute` token against the light grounds.

### Focus ring visibility, per surface this file defines

`{colors.focus}` (`#1264a3`) and `{colors.focus-on-dark}` (`#d9bdde`) both reuse hexes the palette already owns — the link blue and the muted mauve — so neither is a new brand colour. Both are drawn as a 2px ring **outside** the control with a 2px offset (1px on `text-input`), so each is judged against the surface behind the control, per WCAG 2.2 Focus Appearance.

| Ring | Surface | Ratio | Required | Result |
|---|---|---|---|---|
| `{colors.focus}` | `{colors.canvas}` / `{colors.surface-elev}` | 6.22:1 | 3:1 | Pass |
| `{colors.focus}` | `{colors.canvas-cream}` | 5.35:1 | 3:1 | Pass |
| `{colors.focus}` | `{colors.canvas-lavender}` | 5.61:1 | 3:1 | Pass |
| `{colors.focus}` | `{colors.surface-aubergine}` | 2.25:1 | 3:1 | **Fail — do not use the blue ring on aubergine** |
| `{colors.focus-on-dark}` | `{colors.surface-aubergine}` | 8.19:1 | 3:1 | Pass |
| `{colors.focus-on-dark}` | `{colors.primary-press}` | 6.44:1 | 3:1 | Pass |

Two rings exist because the file documents both light and aubergine signature surfaces, and no single tone clears 3:1 on both. Draw `{colors.focus}` on `{colors.canvas}`, `{colors.canvas-cream}`, `{colors.canvas-lavender}` and `{colors.surface-elev}`; draw `{colors.focus-on-dark}` on `{colors.surface-aubergine}` and the aubergine bands, cards and footer.

### Minimum tap target

From the documented geometry alone: `button-primary-pill` at `14px 28px` padding around a `{typography.button-md}` label (16px × 1.38 = 22.08px) computes to **50.1px** of height, and `text-input` at `10px 12px` around a `{typography.body-md}` label (16px × 1.55 = 24.8px) computes to **44.8px**. Both clear the 44×44px of WCAG 2.5.5 (Enhanced, AAA) on the vertical axis, which supports the Responsive Behavior section's claim. This is arithmetic on the documented padding and leading, not a rendered measurement: real tap-target size needs a live page and is outside what this document can verify.

### Reduced motion

Every prescribed animation collapses under `@media (prefers-reduced-motion: reduce)` as stated in Motion & Animation: travel, scale, the press pop, the list stagger and the spinner's rotation are removed; opacity fades remain, capped at `{motion.duration-reduced}` (130ms). No ambient animation exists, so none needs freezing. The focus ring is never animated in either mode.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` aubergine for filled CTAs, the featured pricing tier, and the closing aubergine band — it's the brand's chromatic monotheism.
- Use `{rounded.pill}` (90px) for every button across the system — never a rounded-rectangle button.
- Pair display tiers with negative letter-spacing (`-0.768px` at 64px); the proprietary face needs the tracking pull.
- Compose hero bands with pastel-mesh gradient backdrop + floating product UI mockup; the gradient is the depth.
- Use `{colors.link-blue}` for inline links — it's the only chromatic departure from aubergine and is part of the brand voice.

### Don't
- Don't add a third accent color to the system — the aubergine + blue link combination is exhaustive.
- Don't shrink button padding below `14px 28px` — the over-padded pill is part of the brand feel.
- Don't render display tiers at default tracking (0) — without negative letter-spacing the headlines read loose and unedited.
- Don't put product UI screenshots inside cards — they sit ABOVE the pastel-mesh gradient, never inside chrome.
- Don't use aubergine for body text — it's a surface and CTA color, not a type color at body sizes.
- Don't replace the pill shape with a square button anywhere.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1440px | Full-bleed pastel-mesh hero; pricing 4-up |
| Desktop | 1024–1440px | Default content max-width; pricing 4-up |
| Tablet | 768–1023px | Pricing 2-up; product UI mockups crop to focal panel |
| Mobile | < 768px | Pricing 1-up; hamburger nav; display-xxl drops 64 → 40px |

### Touch Targets
- Pill buttons hit ≥ 48×48px due to the over-padded geometry. WCAG AAA compliant.
- Form fields stay at the 44px minimum height.

### Collapsing Strategy
- Display tiers stair-step 64 → 50 → 32 → 28 → 24 across breakpoints.
- Pastel-mesh gradients re-tile on mobile to prevent the wash from disappearing entirely.
- Floating product UI mockups crop to the most actionable inner panel on mobile.
- Pricing tiers stair-step 4 → 2 → 1; aubergine featured tier stays distinguished.
- Top nav collapses to hamburger below 768px; menu inherits canvas color.

### Image Behavior
Product UI mockups use `srcset` for desktop / tablet / mobile crops; the mobile crop centers on the most actionable inner panel rather than scaling the whole composite down.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly (`{colors.primary}`, `{button-primary-pill}-pressed`, `{rounded.pill}`).
3. Run `npx @google/design.md lint DESIGN.md` after edits.
4. Add new variants as separate entries.
5. Default body to `{typography.body-md}`; reserve `{typography.body-lg}` for marketing leads.
6. Keep aubergine scarce — one filled aubergine button per viewport.
7. Pair every hero band with the pastel-mesh gradient backdrop; bare-canvas heroes read as off-brand.

## Known Gaps

- **Motion is prescribed, not extracted.** Every duration, easing curve, stagger and reduced-motion rule in Motion & Animation is the audit spec's **Playful** profile, assigned from the file's own visual signals. Nobody measured the live site's timing. The one deviation from the profile block is the loading spinner's 900ms infinite loop, which the profile does not cover.
- **`{colors.hairline-strong}` (`#000000`) has no extraction evidence.** It sits in the token block with no prose binding and no source page attributed, and pure black is an unlikely hairline for this brand. It is documented here as the accessible boundary tone because the palette needs one and nothing else in the palette can carry the job, but its origin is unverified: it may be an inherited artefact rather than a real extracted value.
- **Focus rings are prescribed.** `{colors.focus}` and `{colors.focus-on-dark}` reuse hexes the palette already owns, but the ring's existence, width (2px) and offset (2px, 1px on `text-input`) are prescriptions, not observations. No focus treatment was extracted from the site.
- **Component states are largely prescribed.** Only `hover` on links and the `button-primary-pill-pressed` fill were extracted. Every other state named in Components — focus-visible, disabled, loading, selected, error and the hover and press transforms — is a proposal consistent with the brand's geometry.
- **Typeface names are extracted but unverifiable here.** "Salesforce Avant Garde" and "Salesforce Sans" are recorded as found; no specimen or licence was checked, and the Inter and Lato substitutions are judgement, not measurement.
- **The pastel-mesh gradient's stops are approximate.** The Signature Components entry gives `#fff0e6`-ish peach and `#e9d8ff` lavender as inline hexes with a hedge, and the dusty green has no value at all. They are not tokens and nothing binds them, so no contrast claim is made about type drawn over the mesh — which is a real gap, since the hero headline sits on it.
- **No dark theme is documented.** The aubergine surfaces are a signature band inside a light system, not a dark mode. Whether the brand has a dark theme is unknown from the source pages listed in Colors.
- **Not computable from a document:** overlap, horizontal overflow, clipping, rendered tap-target size, frame rate and layout shift. The tap-target figures in Accessibility are arithmetic on documented padding and leading, nothing more.
- **Elevation is mixed.** Levels 1–3 are box-shadows and level 4 is a 1px inset ring, while the Decorative Depth note says the brand's real depth language is the gradient and uses no literal lift. The shadow values are extracted, so they are kept and are now addressable as `{shadow.elev-1}` … `{shadow.elev-4-inset}`, but the file carries two depth systems and does not say which wins where. Level 4's original use note named "button focus"; that reading is rejected in Elevation & Depth, because an inset ring cannot be measured against the surface behind the control.
