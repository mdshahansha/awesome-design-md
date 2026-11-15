---
version: alpha
name: Shopifi-Inspired-design-analysis
description: An inspired interpretation of Shopifi's design language — a cinematic commerce platform that runs two parallel design tracks. The marketing-hero and product-narrative pages live on near-black canvases with full-bleed photography of merchants, giant Neue Haas Grotesk display type at thin weights, and a single black-pill CTA stroked in white. The transactional pages (pricing, signup, dashboards) flip to a cream-mint canvas with pastel aloe and pistachio greens, the same pill button vocabulary, and Inter for UI body. The two tracks share typographic DNA but diverge sharply in canvas polarity — and that choice is the brand.

colors:
  primary: "#000000"
  ink: "#000000"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  canvas-night: "#000000"
  canvas-night-elevated: "#0a0a0a"
  canvas-light: "#ffffff"
  canvas-cream: "#fbfbf5"
  surface-elevated-dark: "#1e2c31"
  shade-30: "#d4d4d8"
  shade-40: "#a1a1aa"
  shade-50: "#71717a"
  shade-60: "#52525b"
  shade-70: "#3f3f46"
  hairline-light: "#e4e4e7"
  hairline-dark: "#1e2c31"
  # Focus rings. Both reuse tones the palette already owns — the brand is
  # monochrome (its accent IS its ink), so a chromatic ring would contradict
  # the first rule of the system. Drawn outside the control with a 2px offset.
  focus: "#ffffff"
  focus-on-light: "#000000"
  aloe-10: "#c1fbd4"
  pistachio-10: "#d4f9e0"
  link-cool-1: "#9dabad"
  link-cool-2: "#9797a2"
  link-cool-3: "#bdbdca"
  link-mint: "#99b3ad"

typography:
  display-xxl:
    fontFamily: "NeueHaasGrotesk Display, Helvetica, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 330
    lineHeight: 1.0
    letterSpacing: 2.4px
    fontFeature: ss03
  display-xl:
    fontFamily: "NeueHaasGrotesk Display, Helvetica, Arial, sans-serif"
    fontSize: 70px
    fontWeight: 330
    lineHeight: 1.0
    letterSpacing: 0
    fontFeature: ss03
  display-lg:
    fontFamily: "NeueHaasGrotesk Display, Helvetica, Arial, sans-serif"
    fontSize: 55px
    fontWeight: 330
    lineHeight: 1.16
    letterSpacing: 0
    fontFeature: ss03
  display-md:
    fontFamily: "NeueHaasGrotesk Display, Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 330
    lineHeight: 1.14
    letterSpacing: 0
    fontFeature: ss03
  heading-xl:
    fontFamily: "NeueHaasGrotesk Display, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.28
    letterSpacing: 0.42px
    fontFeature: ss03
  heading-lg:
    fontFamily: "NeueHaasGrotesk Display, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: 0.36px
    fontFeature: ss03
  heading-md:
    fontFamily: "NeueHaasGrotesk Display, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    fontFeature: ss03
  heading-sm:
    fontFamily: "NeueHaasGrotesk Display, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.72px
    fontFeature: ss03
  body-lg:
    fontFamily: "Inter Variable, Inter, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 550
    lineHeight: 1.56
    letterSpacing: 0
    fontFeature: ss03
  body-md:
    fontFamily: "Inter Variable, Inter, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 420
    lineHeight: 1.5
    letterSpacing: 0
    fontFeature: ss03
  body-strong:
    fontFamily: "Inter Variable, Inter, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 550
    lineHeight: 1.5
    letterSpacing: 0
    fontFeature: ss03
  caption:
    fontFamily: "Inter Variable, Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.49
    letterSpacing: 0.28px
    fontFeature: ss03
  micro:
    fontFamily: "Inter Variable, Inter, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: -0.13px
    fontFeature: ss03
  eyebrow-cap:
    fontFamily: "Inter Variable, Inter, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.72px
    fontFeature: ss03
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    fontFeature: ss03

rounded:
  xs: 4px
  sm: 5px
  md: 8px
  lg: 12px
  xl: 20px
  pill: 9999px

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
  level-0: "none"
  level-1: "0 1px 2px rgba(255,255,255,0.05), inset 0 1px 0 rgba(255,255,255,0.04)"
  level-2: "0 0 0 1px rgba(255,255,255,0.08), 0 1px 3px rgba(0,0,0,0.3), 0 5px 10px rgba(0,0,0,0.2)"
  level-3: "0 8px 8px rgba(0,0,0,0.1), 0 4px 4px rgba(0,0,0,0.1), 0 2px 2px rgba(0,0,0,0.1), 0 0 0 1px rgba(0,0,0,0.1)"
  level-4: "0 25px 50px -12px rgba(0,0,0,0.25)"

# Prescribed to match the brand's visual identity (Cinematic profile).
# Not measured from the live site. See ## Motion & Animation.
motion:
  duration-instant: 120ms
  duration-fast: 240ms
  duration-base: 400ms
  duration-slow: 600ms
  duration-emphasis: 900ms
  ease-standard: cubic-bezier(0.22, 1, 0.36, 1)
  ease-enter: cubic-bezier(0.16, 1, 0.3, 1)
  ease-exit: cubic-bezier(0.5, 0, 0.75, 0)
  stagger-step: 80ms
  duration-reduced: 150ms

components:
  button-primary-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-pill-pressed:
    backgroundColor: "{colors.shade-70}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-outline-on-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 26px
  button-outline-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-aloe-pill:
    backgroundColor: "{colors.aloe-10}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  text-input:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 12px
  card-pricing:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-pricing-featured:
    backgroundColor: "{colors.aloe-10}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-feature-cinematic:
    backgroundColor: "{colors.canvas-night-elevated}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-pistachio-band:
    backgroundColor: "{colors.pistachio-10}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-photo-frame:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 0px
  pill-tag-mint:
    backgroundColor: "{colors.aloe-10}"
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow-cap}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  pill-tag-shade:
    backgroundColor: "{colors.shade-30}"
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow-cap}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  nav-bar-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  nav-bar-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  link-on-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
  footer-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 24px
  footer-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 24px
---

## Overview

Shopifi runs two parallel design tracks that share typographic DNA and a single button vocabulary, but diverge in canvas polarity. The marketing track lives on `{colors.canvas-night}` (`#000000`) — full-bleed cinematic photography of merchants, giant `{typography.display-xxl}` headlines in Neue Haas Grotesk Display set at weight 330 (a thin, almost editorial cut), and a single CTA: a white-stroked black pill with the form `button-outline-on-dark`. The pages read like the spread of a high-end print magazine: lots of black, lots of negative space, photography that doesn't compete with text, and one and only one action per band.

The transactional track flips to `{colors.canvas-light}` and `{colors.canvas-cream}` (an off-white that's barely warmer than pure white). Pricing tiers, comparison tables, and signup flows sit on this lighter canvas, with the same pill button system but in inverse polarity (a solid black pill with white text, or a `{colors.aloe-10}` mint pill for the featured / "Start free trial" tier). The accents — `{colors.aloe-10}` mint and `{colors.pistachio-10}` pistachio — show up only on the light track, never on the cinematic dark hero pages.

Typography is split across three families. **Neue Haas Grotesk Display** at thin weights (330–500) handles every display, headline, and editorial moment — the brand's identity is that thin display cut. **Inter Variable** at 420–550 weights handles every UI body, button label, caption, and form field — utility text that doesn't fight the display. **ui-monospace** appears only in code blocks and rare technical eyebrows. Across all three families, the OpenType `ss03` stylistic set is enabled — it's the brand's character-level signature, applied universally.

**Key Characteristics:**
- Two-canvas system: `{colors.canvas-night}` for cinematic marketing, `{colors.canvas-light}` / `{colors.canvas-cream}` for transactional surfaces — never blended.
- Pill-shape (`{rounded.pill}`) is the only button shape across both tracks; rounded rectangles do not exist for buttons.
- Thin-weight (330) display typography is the signature; `{typography.display-xxl}` at 96px / weight 330 is the brand's loudest visual.
- Aloe and pistachio greens (`{colors.aloe-10}`, `{colors.pistachio-10}`) are reserved for the light track — they signal commerce, growth, transactional success.
- Photography is full-bleed, edge-to-edge, never inset in cards on the cinematic track; merchants and storefront imagery do the heavy visual lifting that gradients and illustrations would do elsewhere.
- The OpenType `ss03` stylistic set is enabled across every text role — a character-level unifier that tracks across both tracks.
- Tight letter-spacing on display sizes (2.4px positive tracking on 96px display) gives the thin weight extra optical air.

## Colors

> **Source pages:** home (`/`), `/start`, `/website/builder`, `/pricing`.

### Brand & Accent
- **Aloe** (`{colors.aloe-10}` — `#c1fbd4`): The featured-tier and "growth" accent. Used as a pill button background on light surfaces and as a feature-card fill in the pricing comparison band.
- **Pistachio** (`{colors.pistachio-10}` — `#d4f9e0`): Softer than aloe; used as a wide section band fill on the light track to signal a different category of feature without leaving the green family.
- **Cool Link Tones** (`{colors.link-cool-1}` `#9dabad`, `{colors.link-cool-2}` `#9797a2`, `{colors.link-cool-3}` `#bdbdca`, `{colors.link-mint}` `#99b3ad`): Muted footer / tertiary link colors used on dark surfaces to create a quiet hierarchy below the primary white type.

### Surface
- **Canvas Night** (`{colors.canvas-night}` — `#000000`): Pure black hero, cinematic feature pages, footer.
- **Canvas Night Elevated** (`{colors.canvas-night-elevated}` — `#0a0a0a`): Cards on cinematic surfaces, video frames.
- **Surface Elevated Dark** (`{colors.surface-elevated-dark}` — `#1e2c31`): Dark teal-shifted surface used on a small subset of dark cards to introduce subtle depth without breaking the black.
- **Canvas Light** (`{colors.canvas-light}` — `#ffffff`): Pricing, signup, comparison tables.
- **Canvas Cream** (`{colors.canvas-cream}` — `#fbfbf5`): Slightly warm off-white used on the pricing-page background canvas — invisibly different from `#ffffff` but adds editorial warmth.
- **Hairline Light** (`{colors.hairline-light}` — `#e4e4e7`): 1px borders on light cards, table dividers.
- **Hairline Dark** (`{colors.hairline-dark}` — `#1e2c31`): 1px borders on the rare dark cards that have visible chrome.

### Shade Ladder
- **Shade-30** (`{colors.shade-30}` — `#d4d4d8`): Tag / chip background on light, footer hairline on dark.
- **Shade-40** (`{colors.shade-40}` — `#a1a1aa`): Tertiary text on light, secondary text on dark.
- **Shade-50** (`{colors.shade-50}` — `#71717a`): Secondary text on light.
- **Shade-60** (`{colors.shade-60}` — `#52525b`): Tertiary text on light, deep on dark.
- **Shade-70** (`{colors.shade-70}` — `#3f3f46`): Pressed-state of the primary pill button; deep dark surface accent.

### Text
- **Ink** (`{colors.ink}` — `#000000`): All text on light canvas.
- **On Primary** (`{colors.on-primary}` — `#ffffff`): All text on dark canvas + filled-pill labels.

## Typography

### Font Family

The display tier is **Neue Haas Grotesk Display** at thin weights (330–500). When unavailable, fall back to **Helvetica** at light weight, then Arial. The thin-weight cut is the brand — no substitution should default to weight 400+.

The UI tier is **Inter Variable** at 420–550 — a variable font with sub-weight precision that lets the system span body (420), strong (550), and caption (500) without jumping to heavier tiers. Inter is open-source via Google Fonts.

The code tier is **ui-monospace**, the system mono — preferred over a webfont mono to avoid unnecessary downloads.

The OpenType `ss03` stylistic set is enabled across every role. It alters specific glyph forms (lowercase `a`, `g`, single-story numerals) for a slightly more geometric character. Apply via `font-feature-settings: "ss03"` on the body element or root.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 96px | 330 | 1.0 | 2.4px | Cinematic hero headline |
| `{typography.display-xl}` | 70px | 330 | 1.0 | 0 | Section opener on cinematic pages |
| `{typography.display-lg}` | 55px | 330 | 1.16 | 0 | Pricing-page page title |
| `{typography.display-md}` | 48px | 330 | 1.14 | 0 | Sub-section headline on light track |
| `{typography.heading-xl}` | 28px | 500 | 1.28 | 0.42px | Card title / pricing tier name |
| `{typography.heading-lg}` | 24px | 400 | 1.14 | 0.36px | Compact card title |
| `{typography.heading-md}` | 20px | 500 | 1.4 | 0.3px | Section sub-heading |
| `{typography.heading-sm}` | 18px | 500 | 1.25 | 0.72px | Eyebrow / mini-section label |
| `{typography.body-lg}` | 18px | 550 | 1.56 | 0 | Marketing body lead, large body |
| `{typography.body-md}` | 16px | 420 | 1.5 | 0 | Default UI body, pill-button labels |
| `{typography.body-strong}` | 16px | 550 | 1.5 | 0 | Emphasized body run |
| `{typography.caption}` | 14px | 500 | 1.49 | 0.28px | Helper copy, footnotes |
| `{typography.micro}` | 13px | 500 | 1.5 | -0.13px | Pricing fine print |
| `{typography.eyebrow-cap}` | 12px | 400 | 1.2 | 0.72px | All-caps eyebrow above large headlines |
| `{typography.code}` | 16px | 400 | 1.5 | 0 | Code blocks |

### Principles
- **Display thinness is the brand.** Always render display sizes at weight 330 — never 400+. The thinness is a deliberate editorial choice that makes the giant size feel quiet.
- **Display in NHGD, body in Inter.** Don't push body roles up to NHGD; don't push display roles down to Inter.
- **Tracking lifts on display.** The 96px hero gets +2.4px positive tracking — the thin glyphs need air. At 70px and below, tracking returns to 0.

### Note on Font Substitutes
Open substitutes for Neue Haas Grotesk Display: **Helvetica Now Display** (proprietary) or **Inter Display** at light weights (open-source) are the closest matches. Avoid Helvetica Neue at default weight — it's too heavy for the brand's thin tier. **Inter Variable** is open-source via Google Fonts and is the canonical body face — no substitute needed.

## Layout

### Spacing System
- **Base unit**: 8px (with denser sub-units 1, 2, 3, 4 for fine work).
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.huge}` 64px.
- **Section padding**: `{spacing.huge}` 64–128px on cinematic marketing pages (extreme negative space is the point); collapses to ~48px on transactional pages where density takes priority.
- **Card internal padding**: `{spacing.xxl}` 32px on pricing cards; `{spacing.xl}` 24px on compact tag rows.

### Grid & Container
- Cinematic hero pages use a wide max-width container (~1440–1600px) with edge-bleeding photography that escapes the container.
- Pricing collapses through 4-up → 2-up → 1-up tiers based on viewport.
- Body content centers in a ~720–840px reading column on long-form pages.

### Whitespace Philosophy
The cinematic track treats whitespace as the brand's most valuable asset — sections often have 128–192px of vertical air between content blocks, with photography filling the rest. The transactional track tightens to ~48–64px between bands because users are scanning, comparing, and acting. The contrast between the two whitespace philosophies is part of the brand voice.

## Elevation & Depth

| Level | Token | Treatment | Use |
|---|---|---|---|
| 0 | `{shadow.level-0}` | Flat, no shadow | Default surface |
| 1 | `{shadow.level-1}` | `0 1px 2px rgba(255,255,255,0.05), inset 0 1px 0 rgba(255,255,255,0.04)` | Subtle inset highlight on dark cards (a top-edge sheen) |
| 2 | `{shadow.level-2}` | `0 0 0 1px rgba(255,255,255,0.08), 0 1px 3px rgba(0,0,0,0.3), 0 5px 10px rgba(0,0,0,0.2)` | Dark elevated cards with hairline + drop shadow stack |
| 3 | `{shadow.level-3}` | `0 8px 8px rgba(0,0,0,0.1), 0 4px 4px rgba(0,0,0,0.1), 0 2px 2px rgba(0,0,0,0.1), 0 0 0 1px rgba(0,0,0,0.1)` | Stacked-shadow card on light surfaces; layered tiny shadows produce a soft halo |
| 4 | `{shadow.level-4}` | `0 25px 50px -12px rgba(0,0,0,0.25)` | Modal / floating panel on light |

### Layer Separation (measured)
Elevation on this brand is expressed one way per track, and the fills do almost
none of the work:

- Dark track: `{colors.canvas-night}` `#000000` to `{colors.canvas-night-elevated}`
  `#0a0a0a` measures **1.06:1** — the fill step is effectively invisible. The
  layer is read entirely from `{shadow.level-1}` / `{shadow.level-2}`'s
  `rgba(255,255,255,…)` top-edge sheen and 1px ring. That is deliberate (the
  cinematic track "wants flat blackness"), but it means a dark card has no
  boundary at all if shadows are suppressed.
- `{colors.surface-elevated-dark}` `#1e2c31` against `{colors.canvas-night}`
  measures **1.46:1** — a real but very shallow step.
- Light track: `{colors.canvas-cream}` against `{colors.canvas-light}` measures
  **1.04:1**; separation there comes from `{shadow.level-3}`'s stacked halo plus
  the `{colors.hairline-light}` 1px border, never from the fill.

### Decorative Depth
On the cinematic track, depth comes from photography — full-bleed merchant imagery layered behind cards, with subtle inset top-edge highlights creating the illusion of light hitting a glass surface. On the light track, the layered tiny-shadow stack (Level 3) produces a soft, paper-like halo around pricing cards — depth without harshness.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Inputs, hairline tags |
| `{rounded.sm}` | 5px | Image containers (small) |
| `{rounded.md}` | 8px | Form inputs, video frames, smaller cards |
| `{rounded.lg}` | 12px | Pricing cards, feature cards |
| `{rounded.xl}` | 20px (top-only on some asymmetric cards) | Hero photo frames, cinematic card chrome |
| `{rounded.pill}` | 9999px | All buttons, pill tags, mint chips |

### Photography Geometry
Photography is full-bleed with no border. On cinematic pages it escapes the container entirely; on transactional pages it sits inside `{rounded.lg}` containers with no shadow. Avatar treatments in customer-logo strips are simple greyscale wordmarks at uniform height (~24–32px), aligned in a single horizontal strip.

## Components

### Buttons

**`button-primary-pill`** — the dominant CTA across the system.
- Background `{colors.primary}` (black), text `{colors.on-primary}`, type `{typography.body-md}`, padding `{spacing.md} {spacing.xl}` (12px 24px), rounded `{rounded.pill}` 9999px.
- Pressed state `button-primary-pill-pressed`: background lifts to `{colors.shade-70}`.
- States: default, hover (fill lifts toward `{colors.shade-70}`), focus-visible (2px `{colors.focus-on-light}` ring at 2px offset), active/pressed (`button-primary-pill-pressed`), disabled (fill `{colors.shade-30}`, label `{colors.shade-50}`, no pointer events), loading (label swaps for an inline spinner, width held so the pill does not resize). Only the pressed fill is extracted; the rest are prescribed here.

**`button-outline-on-dark`** — the cinematic hero CTA.
- Background `{colors.canvas-night}` (transparent on the canvas), 2px solid `{colors.on-primary}` border, text `{colors.on-primary}`, same pill geometry.
- States: default, hover (border and label hold, fill fades to `{colors.on-primary}` at 8% opacity), focus-visible (2px `{colors.focus}` ring at 2px offset outside the border), active/pressed (opacity 0.9), disabled (border and label at 40% opacity), loading (inline spinner in `{colors.on-primary}`). Prescribed here; see Known Gaps.

**`button-outline-on-light`** — the light-track equivalent.
- Background `{colors.canvas-light}`, 1px solid `{colors.ink}` border, text `{colors.ink}`, same pill geometry.
- States: default, hover (fill fades to `{colors.ink}` at 6% opacity), focus-visible (2px `{colors.focus-on-light}` ring at 2px offset), active/pressed (opacity 0.9), disabled (border and label `{colors.shade-40}`), loading (inline spinner in `{colors.ink}`). Prescribed here; see Known Gaps.

**`button-aloe-pill`** — the featured CTA on pricing pages.
- Background `{colors.aloe-10}`, text `{colors.ink}`, same pill geometry. Used for the "Start free trial" tier.
- States: default, hover (fill deepens toward `{colors.pistachio-10}`), focus-visible (2px `{colors.focus-on-light}` ring at 2px offset), active/pressed (opacity 0.92), disabled (fill `{colors.shade-30}`, label `{colors.shade-50}`), loading (inline spinner in `{colors.ink}`). Prescribed here; see Known Gaps.

### Cards & Containers

**`card-pricing`** — the standard tier card on the pricing page.
- Background `{colors.canvas-light}`, padding `{spacing.xxl}`, rounded `{rounded.lg}` 12px, 1px `{colors.hairline-light}` border. Title in `{typography.heading-xl}`, price in `{typography.display-md}`, body in `{typography.body-md}`, CTA pinned to the bottom as `button-primary-pill`.
- States: default, hover (`{shadow.level-3}` halo deepens; no travel on the card itself), selected (the tier the user is on — border swaps to 1px `{colors.ink}`), focus-visible on the card's own CTA only (the card is not itself focusable).

**`card-pricing-featured`** — the highlighted pricing tier.
- Background `{colors.aloe-10}`, otherwise identical to `card-pricing`. The mint fill (rather than a brand-color border) is the brand's distinctive featured-tier choice.
- States: default, hover, selected — same three as `card-pricing`, with the aloe fill held in every one so the featured tier never loses its signal.

**`card-feature-cinematic`** — feature card on the cinematic track.
- Background `{colors.canvas-night-elevated}`, text `{colors.on-primary}`, rounded `{rounded.lg}`, often with a top-edge inset highlight (`{shadow.level-1}`). Holds full-bleed photography or a single large statement.
- States: default, hover where the whole card is a link (inset sheen strengthens toward `{shadow.level-2}`; no travel), focus-visible (2px `{colors.focus}` ring at 2px offset). Non-linked instances have default only.

**`card-pistachio-band`** — wide horizontal band card used to highlight a category of features on the light track.
- Background `{colors.pistachio-10}`, text `{colors.ink}`, rounded `{rounded.lg}` 12px, padding `{spacing.xxl}`.
- States: default only — a static band, not a control. Any control placed inside it carries its own states.

**`card-photo-frame`** — full-bleed photography container on cinematic pages.
- Background `{colors.canvas-night}`, padding 0, rounded `{rounded.xl}` 20px (often top-only). The photo IS the content; no inner padding, no overlay text inside the card.
- States: default, and where the frame is a link, hover (the image scales from 1.0 to 1.02 — see `## Motion & Animation`) and focus-visible (2px `{colors.focus}` ring at 2px offset, with a 1px `{colors.focus-on-light}` outer edge, since photography has no measurable ground colour).

### Inputs & Forms

**`text-input`** — standard text input on light surfaces.
- Background `{colors.canvas-light}`, text `{colors.ink}`, type `{typography.body-md}`, padding `{spacing.sm}+ {spacing.md}` (10px 12px), rounded `{rounded.md}` 8px, 1px `{colors.hairline-light}` border.
- States: default, hover (border darkens one step on the shade ladder), focus-visible (2px `{colors.focus-on-light}` ring at 2px offset, replacing the hairline as the visible boundary), disabled (fill `{colors.canvas-cream}`, label `{colors.shade-40}`), error (2px border in `{colors.ink}` plus an inline `{typography.caption}` message below — the palette carries no red, so error is signalled by weight and copy, never by hue), loading (field locked, inline spinner right-aligned inside the field). Only the resting border is extracted.
- The resting `{colors.hairline-light}` border measures **1.27:1** on `{colors.canvas-light}`, so at rest this input has no WCAG-visible boundary at all. See `## Accessibility`.

### Navigation

**`nav-bar-light`** — top nav on light pages.
- Background `{colors.canvas-light}`, text `{colors.ink}`, padding `{spacing.lg} {spacing.xl}`. Logo wordmark on the left, nav items center, two pill buttons on the right (`button-outline-on-light` for "Log in", `button-primary-pill` for "Start free trial").
- Nav item states: default, hover (underline appears), focus-visible (2px `{colors.focus-on-light}` ring at 2px offset), selected (current section — persistent underline in `{colors.ink}`). No disabled or loading state: nav items are always live.

**`nav-bar-dark`** — top nav on cinematic pages.
- Background `{colors.canvas-night}`, text `{colors.on-primary}`, otherwise identical structure. Two pill buttons on the right (`button-outline-on-dark` for both, with the rightmost subtly more prominent via type weight).
- Nav item states: default, hover, focus-visible (2px `{colors.focus}` ring at 2px offset), selected — mirroring `nav-bar-light` with the ring polarity flipped.

### Pills, Tags, and Chips

**`pill-tag-mint`** — small tag on light surfaces, signaling a feature category.
- Background `{colors.aloe-10}`, text `{colors.ink}`, type `{typography.eyebrow-cap}`, padding `{spacing.xs} {spacing.md}`, rounded `{rounded.pill}`.
- States: default only. These tags are labels, not controls — they have genuinely one state and no hover, focus-visible, active or disabled treatment. Where a tag becomes a filter chip it must be re-specified as a button variant.

**`pill-tag-shade`** — neutral tag on light surfaces.
- Background `{colors.shade-30}`, text `{colors.ink}`, otherwise same shape as `pill-tag-mint`.
- States: default only, as `pill-tag-mint`.

### Signature Components

**Cinematic Photography Layer** — full-bleed merchant photos on the hero. No overlay scrim, no text-on-image; instead, the type sits in clean negative space above or below the photo. The brand treats photography as an editorial spread, not as decoration.

**Stacked Tiny Shadows (Level 3 Elevation)** — pricing cards on the light track use 4 stacked tiny drop shadows (each 1–8px Y offset, 10% black) to produce a soft, layered paper halo. This is the brand's distinctive depth on light.

**`link-on-dark`** — inline link on cinematic pages.
- Color `{colors.on-primary}`, no underline by default (links rely on context); for tertiary footer links, color shifts to one of the cool muted tones (`{colors.link-cool-1}` etc.) with a persistent underline.
- States: default, hover (underline appears; colour holds), focus-visible (2px `{colors.focus}` ring at 2px offset), active/pressed (opacity 0.8), visited (no distinct treatment — the brand does not distinguish it).

**`footer-dark`** — full-page-width footer on the cinematic track.
- Background `{colors.canvas-night}`, text `{colors.on-primary}`, type `{typography.caption}`, padding `{spacing.huge} {spacing.xl}`. Contains 4–5 columns of muted-tone link groups, social icons, and a small legal row.
- States: the container has default only; its links follow `link-on-dark` (default, hover, focus-visible, active/pressed).

**`footer-light`** — equivalent on the transactional track.
- Background `{colors.canvas-light}`, text `{colors.ink}`, otherwise same structure.
- States: container default only; links take the `{colors.focus-on-light}` ring instead of `{colors.focus}`.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** No timing function, duration or choreography
below was extracted; nobody instrumented the real pages. What *is* extracted is
the identity that justifies the profile — full-bleed photography, 96px display
type at weight 330, one action per band, 128–192px of vertical air — which is
the **Cinematic** profile's signature: imagery scales slowly, type arrives late
and settles. Treat the values as a contract to build against, not as a record.

### Principles
- Animate `transform` and `opacity` only — never `width`, `height`, `top`,
  `left` or `margin`.
- Every exit is shorter than its matching entrance, so leaving never feels slow.
- Nothing animates on first paint in a way that delays content: the hero image
  is painted at its final position and only then begins its slow settle.
- The only looping motion is the loader and the hero's slow scale, and the hero
  scale is deliberate brand ambience — stated as such, and frozen under reduced
  motion.
- Cinematic durations are long. Apply them to reveals and surfaces, never to a
  control's own feedback: press stays at `{motion.duration-instant}` so the pill
  still feels mechanical.

### Interaction Table

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, nav item, card) | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity`; `transform: scale(1.01)` on cards only | No scale. Opacity change only, at `{motion.duration-reduced}` 150ms |
| Press / active | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `transform: scale(0.98)` | No scale. Fill/opacity step only, at `{motion.duration-reduced}` |
| Focus-visible ring | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` (ring fades in at a fixed 2px offset) | Ring appears at full opacity immediately; offset never animates |
| Page / route transition | Enter `{motion.duration-slow}` 600ms, exit `{motion.duration-base}` 400ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`; `transform: translateY(24px)` | Cross-fade only, `{motion.duration-reduced}`. No travel |
| Modal / drawer | Enter `{motion.duration-base}` 400ms, exit `{motion.duration-fast}` 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`; `transform: scale(0.98)` for modal, `translateY(100%)` for a bottom drawer | Opacity only at `{motion.duration-reduced}`; the drawer appears in place |
| Dropdown / nav menu | Enter `{motion.duration-fast}` 240ms, exit `{motion.duration-instant}` 120ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`; `transform: translateY(-4px)` | Opacity only at `{motion.duration-reduced}` |
| Toast | Enter `{motion.duration-base}` 400ms, exit `{motion.duration-fast}` 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`; `transform: translateY(16px)` | Opacity only at `{motion.duration-reduced}` |
| List enter (pricing tiers, feature cards) | `{motion.duration-base}` 400ms per item, `{motion.stagger-step}` 80ms between | `{motion.ease-enter}` | `opacity`; `transform: translateY(16px)` | All items fade together at `{motion.duration-reduced}`; stagger drops to 0ms |
| List exit | `{motion.duration-fast}` 240ms, no stagger | `{motion.ease-exit}` | `opacity`; `transform: translateY(-8px)` | Opacity only at `{motion.duration-reduced}` |
| Loading | `{motion.duration-emphasis}` 900ms, looping | `{motion.ease-standard}` | `transform: rotate()` for the inline spinner; `opacity` 1→0.4→1 for skeleton blocks | Loop frozen. A static indicator with an `aria-busy` region replaces it |
| Hero reveal — brand ambience | `{motion.duration-emphasis}` 900ms, once on enter | `{motion.ease-enter}` | `transform: scale(1.04 → 1.0)` on the photo; headline `opacity` + `translateY(24px)` delayed by `{motion.stagger-step}` ×2 | Frozen. Photo is painted at scale 1.0, headline fades in at `{motion.duration-reduced}` |

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translate), all scale, the hero's slow settle,
     the list stagger, and every loop including the spinner rotation. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} = 150ms,
     whatever the Cinematic profile's own durations say. */
  *, *::before, *::after {
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important;
    transition-property: opacity !important;
  }
}
```

Focus rings, the pressed fill change and every state colour change survive
reduced motion — they are information, not decoration. Only their timing drops
to `{motion.duration-reduced}`.

## Accessibility

### Measured contrast

Computed with WCAG 2.1 relative luminance from this file's own hexes.

**Passing, and carrying the brand:**

| Foreground / Background | Ratio | Required |
|---|---|---|
| `{colors.on-primary}` `#ffffff` on `{colors.canvas-night}` `#000000` | 21.0:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.canvas-night-elevated}` `#0a0a0a` | 19.8:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.surface-elevated-dark}` `#1e2c31` | 14.39:1 | 4.5:1 |
| `{colors.ink}` `#000000` on `{colors.canvas-light}` `#ffffff` | 21.0:1 | 4.5:1 |
| `{colors.ink}` on `{colors.canvas-cream}` `#fbfbf5` | 20.22:1 | 4.5:1 |
| `{colors.ink}` on `{colors.aloe-10}` `#c1fbd4` | 18.02:1 | 4.5:1 |
| `{colors.ink}` on `{colors.pistachio-10}` `#d4f9e0` | 18.43:1 | 4.5:1 |
| `{colors.ink}` on `{colors.shade-30}` `#d4d4d8` | 14.21:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.shade-70}` `#3f3f46` (pressed pill) | 10.44:1 | 4.5:1 |
| `{colors.link-cool-1}` `#9dabad` on `{colors.canvas-night}` | 8.86:1 | 4.5:1 |
| `{colors.link-cool-2}` `#9797a2` on `{colors.canvas-night}` | 7.26:1 | 4.5:1 |
| `{colors.link-cool-3}` `#bdbdca` on `{colors.canvas-night}` | 11.3:1 | 4.5:1 |
| `{colors.link-mint}` `#99b3ad` on `{colors.canvas-night}` | 9.41:1 | 4.5:1 |
| `{colors.shade-40}` `#a1a1aa` on `{colors.canvas-night}` | 8.19:1 | 4.5:1 |
| `{colors.shade-50}` `#71717a` on `{colors.canvas-light}` | 4.83:1 | 4.5:1 |
| `{colors.shade-60}` `#52525b` on `{colors.canvas-light}` | 7.73:1 | 4.5:1 |

**Failing, and disclosed. The real brand fails AA at each of these points:**

- `{colors.hairline-light}` `#e4e4e7` on `{colors.canvas-light}` `#ffffff` measures **1.27:1** against a 3:1 boundary minimum, and **1.22:1** on `{colors.canvas-cream}`. This is an extracted value and it is not corrected here. Every 1px divider, table rule, pricing-card edge and — worst — the resting outline of `text-input` is below the threshold at which a sighted user can be relied on to see it. The palette already owns a tone that clears it: `{colors.shade-50}` `#71717a` measures 4.83:1 on `{colors.canvas-light}`. Re-pointing the extracted hairline is a brand decision, not an audit one, so it sits in the report under Needs approval rather than being done silently.
- `{colors.hairline-dark}` `#1e2c31` on `{colors.canvas-night}` `#000000` measures **1.46:1** against the same 3:1 minimum. Extracted, uncorrected: the rare dark card with visible chrome has no perceivable boundary.
- `{colors.hairline-dark}` on `{colors.canvas-night-elevated}` `#0a0a0a`, the fill of `card-feature-cinematic`, measures **1.38:1** — the same failure one layer up. On the dark track a card's extent is communicated by `{shadow.level-2}`'s `rgba(255,255,255,0.08)` ring, not by this hairline.
- `{colors.hairline-dark}` is the same hex as `{colors.surface-elevated-dark}`, so that nominal pair measures **1.0:1**. The two are never actually drawn against each other — the dark hairline edges cards filled with `{colors.canvas-night-elevated}` — so this pair is arithmetic rather than a rendered defect, but the collision is real and either token should be renamed or re-valued.
- `{colors.ink}` `#000000` on `{colors.canvas-night}` `#000000` measures **1.0:1**, and `{colors.ink}` on `{colors.surface-elevated-dark}` `#1e2c31` measures **1.46:1**. Neither pair renders anywhere in this brand: `{colors.ink}` is defined in `## Colors` as "all text on light canvas", and every dark surface takes `{colors.on-primary}` instead (21.0:1 and 14.39:1 above). The pairs are listed because an automated reader that matches tokens by name will generate them, and a reader should know they are not a product defect.
- `{colors.shade-40}` `#a1a1aa` is described in `## Colors` as tertiary text on light, where it measures **2.56:1** on `{colors.canvas-light}` — below 4.5:1 for body copy and below 3:1 even as large text. It is safe only on the dark track (8.19:1). On light, use `{colors.shade-50}` (4.83:1) or `{colors.shade-60}` (7.73:1) instead.
- `{colors.shade-50}` on `{colors.aloe-10}` measures **4.15:1**, so secondary text on a featured pricing card must use `{colors.ink}` or `{colors.shade-60}`, not the ladder's mid tone.

### Focus ring

The brand is monochrome — its accent *is* its ink — so there is no brand colour
for a ring to be made of without contradicting the system's first rule. Both
rings therefore reuse tones the palette already owns, and neither is a new brand
colour:

- `{colors.focus}` = `#ffffff`, the same value as `{colors.on-primary}`. Drawn on
  the cinematic dark surfaces.
- `{colors.focus-on-light}` = `#000000`, the same value as `{colors.ink}`. Drawn
  on the transactional light surfaces.

Both are drawn **outside** the control at a **2px offset** with a 2px stroke, so
each is judged against the surface behind it rather than the control fill it
surrounds — which is what WCAG 2.2 Focus Appearance asks for, and the only way a
ring can clear 3:1 on both a white canvas and a solid black pill.

| Surface the ring is drawn on | Ring | Ratio | Required |
|---|---|---|---|
| `{colors.canvas-night}` `#000000` | `{colors.focus}` | 21.0:1 | 3:1 |
| `{colors.canvas-night-elevated}` `#0a0a0a` | `{colors.focus}` | 19.8:1 | 3:1 |
| `{colors.surface-elevated-dark}` `#1e2c31` | `{colors.focus}` | 14.39:1 | 3:1 |
| `{colors.canvas-light}` `#ffffff` | `{colors.focus-on-light}` | 21.0:1 | 3:1 |
| `{colors.canvas-cream}` `#fbfbf5` | `{colors.focus-on-light}` | 20.22:1 | 3:1 |
| `{colors.aloe-10}` `#c1fbd4` | `{colors.focus-on-light}` | 18.02:1 | 3:1 |
| `{colors.pistachio-10}` `#d4f9e0` | `{colors.focus-on-light}` | 18.43:1 | 3:1 |
| `{colors.shade-30}` `#d4d4d8` (tag fill) | `{colors.focus-on-light}` | 14.21:1 | 3:1 |

Over full-bleed photography, which has no measurable colour, the ring is drawn
as two tones: 2px `{colors.focus}` with a 1px `{colors.focus-on-light}` outer
edge. The two bands separate from each other at 21.0:1, so the ring survives any
image beneath it.

### Tap targets

A rendered page is needed to confirm a tap target, so these are the file's own
stated intentions rather than measurements: `## Responsive Behavior` specifies
pill buttons at ≥ 44×44px and form fields at a 44px minimum height. 44px is the
WCAG 2.5.5 AAA figure; WCAG 2.2's AA criterion (2.5.8) asks for 24×24px. Nav
items, footer links and the `{typography.eyebrow-cap}` 12px tags are not given a
hit area anywhere in this file — see `## Known Gaps`.

### Reduced motion

Every animation in `## Motion & Animation` is suppressed or reduced under
`@media (prefers-reduced-motion: reduce)`: all travel and scale removed, the
hero's slow settle and the spinner loop frozen, the list stagger dropped to 0ms,
and opacity fades capped at `{motion.duration-reduced}` 150ms — below the
Cinematic profile's own `{motion.duration-fast}` of 240ms. State changes
themselves, focus rings included, are never suppressed.

### Other notes

- `error` on `text-input` is signalled by a 2px `{colors.ink}` border plus an
  inline `{typography.caption}` message, never by hue — the palette carries no
  red. That is a colour-independent signal, which satisfies WCAG 1.4.1.
- `{typography.display-xxl}` at weight 330 is a thin cut at 96px. Large size
  offsets the thin stroke, but the same 330 weight must never be used below
  `{typography.display-md}` 48px, which `## Do's and Don'ts` already forbids.
- `link-on-dark` carries no underline at rest and relies on context. That is a
  WCAG 1.4.1 risk for any link sitting inside a run of body copy; underline
  inline links, and reserve the context-only treatment for nav and footer
  groups, where the cool muted tones do carry a persistent underline.

## Do's and Don'ts

### Do
- Reserve `{colors.aloe-10}` and `{colors.pistachio-10}` for the light track only — they don't appear on cinematic black pages.
- Always use `{rounded.pill}` for buttons; never `{rounded.md}` or `{rounded.lg}`.
- Render display tiers at weight 330; bumping to 400 or 500 breaks the brand's thin-display signature.
- Use full-bleed photography on cinematic pages — let it escape the container.
- Apply `font-feature-settings: "ss03"` globally; the stylistic set is the brand's typographic signature.
- Pair black canvas with white type and white-stroked outline pills; pair light canvas with black type and filled-black pills.

### Don't
- Don't introduce a third canvas color — stick to black or light/cream. Greys, beiges, and blues are not in the system.
- Don't add drop shadows on cinematic dark cards beyond the subtle inset top-highlight; the cinematic track wants flat blackness.
- Don't shrink display tiers below `{typography.display-md}` (48px) on hero surfaces; below that they read as section heads, not display.
- Don't put aloe / pistachio greens behind type — they're surface fills, not text colors.
- Don't replace the pill shape with a rounded-rectangle button anywhere.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1440px | Full cinematic hero with edge-bleeding photography; pricing 4-up |
| Desktop | 1024–1440px | Default content max-width; pricing 4-up tightens |
| Tablet | 768–1023px | Pricing 2-up; cinematic hero photography crops |
| Mobile | < 768px | Pricing 1-up; hamburger nav; display-xxl drops to ~56–64px |

### Touch Targets
- Pill buttons hit ≥ 44×44px on mobile via 12px vertical padding × 16px line-height. WCAG AAA compliant.
- Form fields stay at the 44px minimum height across all breakpoints.

### Collapsing Strategy
- Display sizes scale down through the breakpoint stair: 96 → 70 → 55 → 48 → 36px on mobile.
- Cinematic photography crops aggressively at smaller widths, prioritizing focal subject over edge-bleed.
- Pricing tiers stair-step 4-up → 2-up → 1-up; the featured aloe tier stays visually distinguished at every step.
- Top nav collapses to hamburger below 768px; menu inherits canvas polarity.

### Image Behavior
Photography uses responsive `srcset` with art-direction crops at major breakpoints. Mobile crops favor close subjects; wide crops favor environmental / storefront context.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly (`{colors.aloe-10}`, `{button-primary-pill}-pressed`, `{rounded.pill}`).
3. Run `npx @google/design.md lint DESIGN.md` after edits.
4. Add new variants as separate entries.
5. Default body to `{typography.body-md}`; reserve `{typography.body-lg}` for marketing leads.
6. Keep the two canvas tracks separated — when designing a new page, choose cinematic OR transactional, not both.
7. The pill shape is non-negotiable; new button variants vary in fill / border / canvas, never in shape.

## Known Gaps

### No `text-dim` token, and that is the brand, not an omission
This palette has no key named `text-dim`, `muted` or `text-secondary`, and none
has been added — inventing one would put a token in a brand document that exists
only to fill a column. The brand *does* have secondary ink; it is spelled as a
numeric ladder and a link family instead:

- `{colors.shade-40}` — "tertiary text on light, secondary text on dark"
- `{colors.shade-50}` — "secondary text on light"
- `{colors.shade-60}` — "tertiary text on light, deep on dark"
- `{colors.link-cool-1}` / `-2` / `-3` / `{colors.link-mint}` — "muted footer /
  tertiary link colors used on dark surfaces to create a quiet hierarchy below
  the primary white type"

So the role is present and documented; only the naming convention differs. An
automated check that matches role names by regex will report `text-dim` as
absent. That is a property of the check, not of the brand, and the audit report
for this file raises it as a harness issue.

### Not extracted, prescribed here
- **All motion.** Every duration, easing and choreography value in
  `## Motion & Animation` is prescribed from the Cinematic profile. Nobody
  measured the live site's timing functions.
- **All focus-ring geometry.** The 2px stroke and 2px offset are prescribed. The
  ring *colours* reuse `{colors.on-primary}` and `{colors.ink}`, which are
  extracted, but the brand's real focus treatment was never captured.
- **Hover, disabled, loading, selected and error treatments** for every
  component. Only `button-primary-pill-pressed` is an extracted state; the rest
  of each `States:` line in `## Components` is prescribed to be internally
  consistent, and a brand owner should confirm it.

### Values used in prose with no token behind them
- Section padding of ~48px on transactional pages, and the 128–192px of vertical
  air on the cinematic track, are cited in `## Layout` but fall between
  `{spacing.xxl}` 32px and `{spacing.huge}` 64px, and above `{spacing.huge}`,
  with no token for either. They have been left as prose rather than adding
  ladder steps that the extraction did not record.
- Container max-widths (~1440–1600px), the reading column (~720–840px), the
  mobile display size (~56–64px) and the logo-strip height (~24–32px) are all
  ranges rather than values, so none is tokenised.

### Scale irregularities, left as extracted
- `{rounded.xs}` 4px and `{rounded.sm}` 5px sit 1px apart — effectively one step
  recorded twice. Both are kept because both appear in the extraction.
- `{rounded.xs}` is bound as the radius of `nav-bar-light`, `nav-bar-dark`,
  `footer-dark`, `footer-light` and `link-on-dark`, none of which is a rounded
  element; it reads as a default placed where no radius applies.

### Not measurable from a document
Tap-target size, overlap, horizontal overflow, clipping, frame rate and layout
shift all need a rendered page. The 44px figures in `## Responsive Behavior` are
the file's stated intent, not a measurement. Nav items, footer links and the
12px `{typography.eyebrow-cap}` tags have no stated hit area at all.
