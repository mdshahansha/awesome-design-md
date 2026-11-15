---
version: alpha
name: Framer-design-analysis
description: "A confident dark-canvas builder marketing site that treats the page like a working artboard — pure black surfaces, white display type set in GT Walsheim Medium with aggressive negative tracking, and a single confident blue (#0099ff) reserved for hyperlinks and selection states. The page rhythm is broken by oversized vibrant gradient atmosphere panels — magenta, violet, orange spotlights — that act as living showcase tiles, not decoration. Every CTA is a white pill on dark; every card is a translucent or charcoal surface; every section title pulls letter-spacing tight enough to feel like a poster."

colors:
  primary: "#ffffff"
  on-primary: "#000000"
  accent-blue: "#0099ff"
  ink: "#ffffff"
  text-muted: "#999999"
  canvas: "#090909"
  surface: "#141414"
  surface-raised: "#1c1c1c"
  hairline: "#262626"
  hairline-soft: "#1a1a1a"
  hairline-strong: "#6b6b6b"
  focus: "#0099ff"
  focus-on-gradient: "#000000"
  inverse-canvas: "#ffffff"
  inverse-ink: "#000000"
  gradient-magenta: "#d44df0"
  gradient-violet: "#6a4cf5"
  gradient-orange: "#ff7a3d"
  gradient-coral: "#ff5577"
  semantic-success: "#22c55e"

typography:
  display-xxl:
    fontFamily: GT Walsheim Framer Medium
    fontSize: 110px
    fontWeight: 500
    lineHeight: 0.85
    letterSpacing: -5.5px
  display-xl:
    fontFamily: GT Walsheim Medium
    fontSize: 85px
    fontWeight: 500
    lineHeight: 0.95
    letterSpacing: -4.25px
    fontFeature: ss02
  display-lg:
    fontFamily: GT Walsheim Medium
    fontSize: 62px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: -3.1px
    fontFeature: ss02
  display-md:
    fontFamily: GT Walsheim Medium
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.13
    letterSpacing: -1.0px
  headline:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: -0.8px
    fontFeature: cv05
  subhead:
    fontFamily: Inter Variable
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.01px
    fontFeature: cv11
  body-lg:
    fontFamily: Inter Variable
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.18px
    fontFeature: cv11
  body:
    fontFamily: Inter Variable
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.15px
    fontFeature: cv11
  body-sm:
    fontFamily: Inter Variable
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: -0.14px
    fontFeature: cv11
  caption:
    fontFamily: Inter Variable
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.13px
    fontFeature: cv11
  micro:
    fontFamily: Inter Variable
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: -0.12px
    fontFeature: cv11
  button:
    fontFamily: Inter Variable
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: -0.14px
    fontFeature: cv11

rounded:
  xs: 4px
  sm: 6px
  md: 10px
  lg: 15px
  xl: 20px
  xxl: 30px
  pill: 100px
  full: 9999px

spacing:
  hair: 1px
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 15px
  lg: 20px
  xl: 30px
  xxl: 40px
  section: 96px

shadow:
  light-edge: "inset 0 0.5px 0 rgba(255,255,255,0.10)"
  float: "0 10px 30px rgba(0,0,0,0.25)"
  focus-glow: "0 0 0 1px rgba(0,153,255,0.15)"

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
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 15px
  button-primary-pressed:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 15px
  button-translucent:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.xxl}"
    padding: 8px 14px
  button-icon-circular:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    size: 40px
  pricing-tab-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-muted}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 14px
  pricing-tab-selected:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 14px
  text-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px 14px
  text-input-focused:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px 14px
  pricing-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 24px
  pricing-card-featured:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 24px
  template-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 12px
  gradient-spotlight-card:
    backgroundColor: "{colors.gradient-violet}"
    textColor: "{colors.ink}"
    typography: "{typography.subhead}"
    rounded: "{rounded.xl}"
    padding: 32px
  gradient-spotlight-card-magenta:
    backgroundColor: "{colors.gradient-magenta}"
    textColor: "{colors.ink}"
    typography: "{typography.subhead}"
    rounded: "{rounded.xl}"
    padding: 32px
  gradient-spotlight-card-orange:
    backgroundColor: "{colors.gradient-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.subhead}"
    rounded: "{rounded.xl}"
    padding: 32px
  product-mockup-tile:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xl}"
    padding: 16px
  feature-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
  comparison-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 56px
  faq-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 32px
---

## Overview

Framer's marketing canvas is a near-pure black artboard. The dominant surface is `{colors.canvas}` — almost pure black with a faint warmth — and on top of it sits oversized white display type set in **GT Walsheim Medium** with letter-spacing pulled to extreme negative values (-5.5px on the 110px display, -4.25px on the 85px hero). The page reads like a poster: one assertive statement per band, generous breathing room above and below.

The single accent is `{colors.accent-blue}` — used scarcely, mostly for hyperlinks, selection halos, and a subtle blue-tinted shadow ring on focused inputs. The brand chrome itself is monochrome: white pill buttons, charcoal cards, gray secondary text. What makes Framer distinctive is the rhythm break — every few sections the page drops in a **vibrant gradient atmosphere card**: a magenta-violet spotlight, a sunset-orange wash, a coral-pink panel. These aren't section backgrounds; they're individual cards arranged in a card grid, each one a small living poster that shows what Framer can produce.

Body type is **Inter Variable**, with Framer leaning hard into Inter's character variants (`cv01`, `cv05`, `cv09`, `cv11`, `ss03`, `ss07`, `dlig`) — the result is a body voice that feels custom-tuned, with single-storey "a", straight-leg "l", and tabular figures. There's no light mode on the marketing site; the brand IS dark.

**Key Characteristics:**
- Black-canvas marketing system: `{colors.canvas}` is the surface for hero, body, pricing, FAQ, and footer alike — no light interludes.
- Massive negative letter-spacing on display sizes (-5.5px / -4.25px / -3.1px) creates a poster-grade headline cadence.
- White pill (`{components.button-primary}`) is the only primary CTA shape across the site; secondary actions live as charcoal pills (`{components.button-secondary}`) or text links.
- Oversized **gradient spotlight cards** (violet, magenta, orange, coral) act as showcase tiles inside the dark grid; they are individual cards, not section backgrounds.
- Inter Variable with bespoke OpenType character variants (`cv01/05/09/11`, `ss03/ss07`, `dlig`) used everywhere body type appears — the typographic voice is unmistakable.
- Border radius scale runs from 4px utility chips up to 100px pills and full circles, with 15–20px the default for cards and 30px for atmospheric gradient cards.
- A single chromatic accent `{colors.accent-blue}` reserved for hyperlinks, focus, and selection — never decorative.

## Colors

> Source pages: framer.com (home), /ai/, /startups/, /marketplace/templates/nudge/, /gallery/a16z-speedrun-×-tonik, /pricing.

### Brand & Accent
- **Pure White** ({colors.primary}): The brand primary surface. Every primary CTA pill, every display headline, every body line on canvas.
- **Sky Blue** ({colors.accent-blue}): The single chromatic accent. Hyperlinks, focused-input rings, and a few selection states. Never used for backgrounds or as a brand fill.

### Surface
- **Canvas** ({colors.canvas}): Default page background — near-black with a faint warmth. Footer, pricing, hero, and FAQ all sit on it.
- **Surface** ({colors.surface}): One step above canvas — pricing cards, secondary buttons, mockup tiles.
- **Surface Raised** ({colors.surface-raised}): Two steps above — featured pricing card, hero pill backdrop, selected pricing tab.
- **Hairline** ({colors.hairline}): Extracted 1px border on input groups and comparison-table dividers. Decorative only — it measures 1.32:1 on `{colors.canvas}`, so it must not be the sole boundary of a control.
- **Hairline Soft** ({colors.hairline-soft}): Extracted subtler divider — between FAQ rows and footer column rules. Decorative only — 1.14:1 on `{colors.canvas}`.
- **Hairline Strong** ({colors.hairline-strong}): **Prescribed, not extracted.** The accessible parallel to the two frozen hairlines, for any boundary that carries meaning — a text-input edge, a selected-tier outline, a table rule a reader must follow. 3.74:1 on `{colors.canvas}`.
- **Inverse Canvas** ({colors.inverse-canvas}): Pure white — used as the surface of light-on-dark pill CTAs and a small set of light-mode template thumbnails embedded in the showcase grid.
- **Inverse Ink** ({colors.inverse-ink}): Black type and glyphs on `{colors.inverse-canvas}` — the label inside a white pill CTA and any caption on a light template thumbnail. 21:1 on white.

### Focus
- **Focus** ({colors.focus}): **Prescribed, not extracted** — the ring reuses the brand's own signal blue `#0099ff` rather than inventing a colour. 6.64:1 on `{colors.canvas}`, 6.14:1 on `{colors.surface}`, 5.68:1 on `{colors.surface-raised}`, 3.00:1 on `{colors.inverse-canvas}`, so one ring serves every monochrome surface this file defines. It replaces the extracted `rgba(0,153,255,0.15)` glow, which is a decorative halo and far below 3:1.
- **Focus on Gradient** ({colors.focus-on-gradient}): **Prescribed, not extracted.** The blue ring collapses on the gradient spotlight cards (1.16:1 on `{colors.gradient-orange}`), so focus over a gradient tile is drawn in black: 3.97:1 on violet, 6.12:1 on magenta, 8.10:1 on orange, 6.82:1 on coral.

### Text
- **Ink** ({colors.ink}): All headline and emphasized body type — pure white.
- **Text Muted** ({colors.text-muted}): Secondary type — gray (#999999) used for meta info, footer columns, comparison-row labels, deselected pricing tabs. Hierarchy on the dark canvas is carried by ink → text-muted contrast, not by weight changes.

### Semantic
- **Success Green** ({colors.semantic-success}): Pricing comparison-table checkmarks. Glyph fill, not surface.

### Brand Gradient (signature)
- **Gradient Magenta** ({colors.gradient-magenta}): Spotlight card variant.
- **Gradient Violet** ({colors.gradient-violet}): Spotlight card variant — most common.
- **Gradient Orange** ({colors.gradient-orange}): Spotlight card variant — sunset wash.
- **Gradient Coral** ({colors.gradient-coral}): Spotlight card variant — coral/pink.

These four sit as oversized atmospheric tiles inside otherwise monochrome card grids — a dark canvas with one or two glowing spotlight cards is a recurring page signature.

White type on these grounds is part of the brand and it does not all pass. Measured against `{colors.ink}`: violet 5.30:1, magenta 3.43:1, coral 3.08:1 — all clear the 3:1 large-text threshold at the `{typography.subhead}` 24px/400 the cards use, none clears 4.5:1. `{colors.gradient-orange}` measures 2.59:1 and clears neither. The hexes are frozen extracted anchors, so the real brand fails AA here; see Accessibility for the usage rule and the alternatives.

## Typography

### Font Family

- **GT Walsheim Framer Medium** / **GT Walsheim Medium** — Framer's display typeface. Geometric, slightly humanist, very confident at large sizes with extreme negative tracking. Fallbacks: `GT Walsheim Medium Placeholder` system font.
- **Inter Variable** — System body typeface. Used with extensive OpenType character variants: `cv01` (alternate "1"), `cv05` (alternate "g"), `cv09` (alternate "i" / "l"), `cv11` (alternate "0"), `ss03` / `ss07` stylistic sets, `dlig` discretionary ligatures, and `tnum` for numerics in tabular contexts. The result is a body voice that feels bespoke without commissioning a custom face.
- **Inter** — Used selectively for `{typography.headline}` (the 22px / 20px tier). The non-variable cut catches small tracking targets that the variable file rounds.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 110px | 500 | 0.85 | -5.5px | Largest hero headline (home, AI page) |
| `{typography.display-xl}` | 85px | 500 | 0.95 | -4.25px | Section opener headlines |
| `{typography.display-lg}` | 62px | 500 | 1.00 | -3.1px | Sub-section openers |
| `{typography.display-md}` | 32px | 500 | 1.13 | -1.0px | Card titles, smaller display |
| `{typography.headline}` | 22px | 700 | 1.20 | -0.8px | Pricing tier headlines, FAQ category titles |
| `{typography.subhead}` | 24px | 400 | 1.30 | -0.01px | Lead body next to display headlines |
| `{typography.body-lg}` | 18px | 400 | 1.30 | -0.18px | Hero subhead, lead paragraphs |
| `{typography.body}` | 15px | 400 | 1.30 | -0.15px | Default body, card descriptions |
| `{typography.body-sm}` | 14px | 500 | 1.40 | -0.14px | Pricing comparison rows, dense data |
| `{typography.caption}` | 13px | 500 | 1.20 | -0.13px | Eyebrows, footer columns, meta |
| `{typography.micro}` | 12px | 400 | 1.20 | -0.12px | Disclaimer, footnote |
| `{typography.button}` | 14px | 500 | 1.0 | -0.14px | Pill buttons |

### Principles

- **Letter-spacing scales with size, hard.** Display-xxl pulls -5.5px (5% of size); body sticks to about -1% (-0.15px on 15px). The result: posters at the top, comfortable reading at body.
- **OpenType character variants are the brand voice.** Switching off `cv11`, `ss03`, etc. visibly changes the body voice — the brand depends on them.
- **Weight stays in a narrow band.** Display sits at 500, body at 400, body-sm/caption at 500. Hierarchy is carried by size + tracking, not by 700/900 ramps.
- **Tight line-heights everywhere.** Even body runs at 1.30 — Framer's editorial tone is denser than typical SaaS marketing.

### Note on Font Substitutes

If implementing without GT Walsheim Medium, suitable open-source substitutes include **Mona Sans**, **Geist**, or **Inter** at weight 600–700 with manually tightened tracking. Mona Sans's hairline weights at 100–300 are particularly close to Framer's cleaner section openers. Inter Variable is open-source — keep it as-is and preserve the documented OpenType variants.

## Layout

### Spacing System

- **Base unit**: 5px (Framer uses non-standard 5/10/15/20/30 increments rather than the more common 4/8/16/24).
- **Tokens (front matter)**: `{spacing.hair}` 1px · `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 15px · `{spacing.lg}` 20px · `{spacing.xl}` 30px · `{spacing.xxl}` 40px · `{spacing.section}` 96px.
- Card interior padding: `{spacing.lg}` 20px on pricing cards; `{spacing.xl}` 30px on gradient spotlight cards.
- Pill button padding: 10px vertical · 15px horizontal — `{components.button-primary}`.
- Section padding (vertical): roughly `{spacing.section}` 96px on home; tighter (~64px) on pricing comparison.

### Grid & Container

- Max content width sits around the 1199px breakpoint, with side gutters that scale toward `{spacing.xl}` on desktop.
- Card grids on the home gallery use 2-up at desktop, collapsing to 1-up below 810px.
- Pricing tier grid is 4-up across the documented breakpoints; comparison table beneath it uses fixed-width left column with horizontally scrolling tier columns at narrow widths.

### Whitespace Philosophy

The dark canvas IS the whitespace. Where lighter brands lean on white air to separate sections, Framer leans on long stretches of black with a single oversized statement floating in the middle. Sections separate by mode change: a band of charcoal cards, then a band of black with a gradient spotlight, then back to charcoal — like cuts in a dark film.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Default for canvas-mounted display type, FAQ rows, footer |
| 1 (charcoal) | `{colors.surface}` lift on canvas | Pricing cards, mockup tiles, secondary buttons |
| 2 (light-edge) | `{shadow.light-edge}` 0.5px top edge + `{shadow.float}` drop | Floating product cards, modal cards |
| 3 (selected) | `{shadow.focus-glow}` ring | Focused inputs, selected option — decoration behind `{colors.focus}`, not the focus indicator |

Four shadow signatures recur across the homepage: a 1px subtle drop, a translucent blue ring, a thick near-black 2px outline (used as the active-element marker on sub-nav), and the layered light-edge + drop-shadow used for floating cards.

Elevation is expressed one way: **surface lift**. Canvas → `{colors.surface}` → `{colors.surface-raised}` carries every hierarchy step in the system. Shadow appears only at level 2, and only for things that genuinely float over content (modals, product cards lifted off the grid); a border is never used to fake a step, which is why the featured pricing card is a lift rather than an outline. The level-3 glow is a chromatic marker, not an elevation step.

Measured layer separation: `{colors.surface}` on `{colors.canvas}` is 1.08:1 and `{colors.surface-raised}` on `{colors.surface}` is 1.08:1 (1.17:1 against canvas). The lifts are deliberately almost subliminal — at these ratios the layers read as edges in peripheral vision on a calibrated display and can disappear entirely on a dimmed laptop panel, so **the surface ladder must never be the only signal that distinguishes two things**. Pair it with radius, padding or a `{colors.hairline-strong}` boundary wherever the distinction carries meaning.

### Decorative Depth

- **Gradient spotlight cards** are the dominant depth device — color saturation against black canvas substitutes for shadow-driven elevation.
- **Layered product mockups** (browser frames containing live Framer-built sites) sit inside `{colors.surface}` cards with the level-2 light-edge treatment.
- **Subtle blue ring (focus / selected)** is the only chromatic depth signal — used to mark the active state of input groups and pricing tier toggles without changing the underlying surface.

## Shapes

### Border Radius Scale

Framer's extracted radius set is unusually granular (1px, 4px, 5px, 6px, 8px, 10px, 12px, 15px, 20px, 30px, 40px, 100px). The named scale below picks the levels the marketing surface actually consumes.

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Small chip / utility radius |
| `{rounded.sm}` | 6px | Inline tag, badge |
| `{rounded.md}` | 10px | Form input, list item |
| `{rounded.lg}` | 15px | Template card thumbnails |
| `{rounded.xl}` | 20px | Pricing cards, mockup tiles |
| `{rounded.xxl}` | 30px | Gradient spotlight cards, oversized panels |
| `{rounded.pill}` | 100px | All primary text CTAs |
| `{rounded.full}` | 9999px | Circular icon buttons, avatar circles |

### Photography & Illustration Geometry

- Embedded site mockups (browser-chromed previews of Framer-built sites) sit in `{rounded.xl}` 20px tiles with `{spacing.md}` 15px interior padding.
- Gradient spotlight cards use `{rounded.xxl}` 30px corners — softer than the 20px content cards by design, to make them feel like atmospheric panels rather than tighter UI.
- Icon glyphs and sub-nav glyphs render in `{rounded.full}` circles at 32–40px sizes.

## Components

State coverage below is **prescribed, not extracted**: the inspected pages are static captures, so only default, pressed, selected and focused appear in the source material. Every other state named here is the state this system should carry, built from the tokens this file already defines. Where a component genuinely has two states, it says so.

### Buttons

**`button-primary`** — White pill on dark canvas. The primary CTA across home, pricing, AI, and gallery pages.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}`, padding 10px 15px, rounded `{rounded.pill}`.
- Pressed state lives in `button-primary-pressed` (the live site uses a transform-scale shrink rather than a darkened fill).
- States: default · hover (opacity 0.9 on the white fill) · focus-visible (2px `{colors.focus}` ring, 2px offset on `{colors.canvas}`) · active/pressed (`button-primary-pressed`, transform scale 0.97) · disabled (fill at 40% opacity, no ring, pointer events off) · loading (label swapped for a spinner, width held so the pill does not resize). No error state — the pill never reports validation.

**`button-secondary`** — Charcoal pill. Used for secondary navigation actions ("Sign in", "Talk to sales") and as the visual counterpart to the primary pill.
- Background `{colors.surface}`, text `{colors.ink}`, type `{typography.button}`, padding 10px 15px, rounded `{rounded.pill}`.
- States: default · hover (lift to `{colors.surface-raised}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed (scale 0.97) · disabled (text to `{colors.text-muted}`) · loading (spinner in place of the label).

**`button-translucent`** — Translucent / lifted secondary used on top of busy backgrounds (gallery hero, gradient cards).
- Background `{colors.surface-raised}`, text `{colors.ink}`, type `{typography.button}`, rounded `{rounded.xxl}`, padding 8px 14px.
- States: default · hover (surface opacity up one step) · focus-visible (2px `{colors.focus-on-gradient}` ring when the button sits on a gradient tile, `{colors.focus}` elsewhere) · active/pressed (scale 0.97) · disabled (40% opacity).

**`button-icon-circular`** — 40px circle for inline icon actions (carousel arrows, social links).
- Background `{colors.surface}`, text `{colors.ink}`, rounded `{rounded.full}`, size 40px.
- States: default · hover (lift to `{colors.surface-raised}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed (scale 0.94) · disabled (icon to `{colors.text-muted}`).

### Pricing Tabs

**`pricing-tab-default`** + **`pricing-tab-selected`** — The pill-toggle that switches between Basic / Pro / Business / Enterprise on `/pricing`.
- Default: `{colors.canvas}` background, `{colors.text-muted}` text, rounded `{rounded.pill}`.
- Selected: `{colors.surface-raised}` background, `{colors.ink}` text — selected = lift, not color. Surface depth communicates "active" without needing a chromatic fill.
- States: default · hover (text to `{colors.ink}`, no fill change) · focus-visible (2px `{colors.focus}` ring) · selected. The toggle has no disabled, loading or error state — four tiers are always available.

### Inputs & Forms

**`text-input`** + **`text-input-focused`** — Form fields on `/pricing` (seat-count, currency switcher) and the in-product preview surfaces.
- Background `{colors.surface}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.md}`, padding 10px 14px.
- Focused state retains the same surface; the focus ring is the level-3 blue-tinted shadow `rgba(0,153,255,0.15)` 0 0 0 1px.
- States: default · hover (1px `{colors.hairline-strong}` boundary) · focus-visible (`text-input-focused`: 2px `{colors.focus}` ring; the extracted `rgba(0,153,255,0.15)` glow stays as decoration behind it) · disabled (text to `{colors.text-muted}`, boundary to `{colors.hairline}`) · loading (inline spinner at the trailing edge while a seat count revalidates) · error (1px `{colors.gradient-coral}` boundary plus a `{typography.caption}` message in the same colour — prescribed; no error styling renders on the inspected pages, see Known Gaps).

### Cards & Containers

**`pricing-card`** — Each tier on `/pricing`.
- Background `{colors.surface}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.xl}`, padding 24px.

**`pricing-card-featured`** — The Pro tier (visually emphasized).
- Background `{colors.surface-raised}`, otherwise identical structure. The lift is one surface step up — no chromatic outline.
- States for both cards: default and selected only — the tier card is a container, not a control, so it has no hover, focus-visible, disabled, loading or error state. The CTA pill inside it carries those.

**`template-card`** — Thumbnail tile in the home "Built with Framer" gallery and `/marketplace`.
- Background `{colors.surface}`, text `{colors.ink}`, type `{typography.body-sm}`, rounded `{rounded.lg}`, padding 12px.
- States: default · hover (thumbnail scale 1.02, card lift to `{colors.surface-raised}`) · focus-visible (2px `{colors.focus}` ring on the whole tile, since the tile is one link) · loading (skeleton fill at `{colors.surface}` until the thumbnail resolves). No disabled or error state.

**`product-mockup-tile`** — Larger tile that frames a live product UI mock (Framer canvas, Workshop video, AI translate panel).
- Background `{colors.surface}`, text `{colors.ink}`, type `{typography.body-sm}`, rounded `{rounded.xl}`, padding 16px.
- States: default only — a non-interactive display frame. If the mock becomes a link, it inherits `template-card`'s hover and focus-visible.

### Gradient Spotlight Cards (signature)

The defining decorative surface of Framer's marketing — oversized atmospheric tiles dropped into otherwise monochrome card grids. Variants:

**`gradient-spotlight-card`** — violet ground (most common).
- Background `{colors.gradient-violet}`, text `{colors.ink}`, type `{typography.subhead}`, rounded `{rounded.xl}`, padding 32px. (The on-site card often pushes to `{rounded.xxl}` 30px when it spans a wider tile.)
- States for every gradient variant: default · hover (scale 1.01, no fill change — the gradient is the identity) · focus-visible (2px `{colors.focus-on-gradient}` ring, never the blue, which collapses on these grounds). No pressed, disabled, loading or error state: the tile is a showcase surface, and any control placed on it brings its own states.

**`gradient-spotlight-card-magenta`** — magenta-pink ground.
- Background `{colors.gradient-magenta}`, otherwise identical.

**`gradient-spotlight-card-orange`** — sunset-orange wash.
- Background `{colors.gradient-orange}`, otherwise identical.

(Coral pink follows the same shape with `{colors.gradient-coral}`.)

### Comparison & FAQ

**`feature-row`** + **`comparison-row`** — Single rows inside the pricing comparison table.
- `feature-row`: `{colors.canvas}` background, `{colors.ink}` text. Header rows.
- `comparison-row`: `{colors.canvas}` background, `{colors.text-muted}` text. Data rows with `{typography.body-sm}` and 1px `{colors.hairline-soft}` underlines.
- States: default only for `feature-row`; `comparison-row` adds hover (row ground to `{colors.surface}`) on touch-free viewports. Use `{colors.hairline-strong}` for the underline wherever the rule itself has to be followed across a wide table — `{colors.hairline-soft}` at 1.14:1 is decoration.

**`faq-row`** — Each accordion line in the pricing-page FAQ.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.md}`, padding 24px.
- States: default (collapsed) · hover (question to full `{colors.ink}`) · focus-visible (2px `{colors.focus}` ring on the summary row) · selected (expanded, chevron rotated). No disabled, loading or error state.

### Navigation

**`top-nav`** — Sticky bar on `{colors.canvas}` with the Framer wordmark left, primary nav links centered, and a `button-secondary` ("Sign in") + `button-primary` ("Get started for free") pair right.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-sm}`, height 56px.
- Mobile: collapses primary links into a hamburger; the two pill CTAs collapse into a single primary pill on the bar.
- States per link: default · hover (`{colors.text-muted}` to `{colors.ink}`) · focus-visible (2px `{colors.focus}` ring) · selected (current section, 2px `{colors.hairline-strong}` underline). The bar itself has no disabled, loading or error state.

### Footer

**`footer`** — Dense link grid on `{colors.canvas}` with the Framer wordmark left and 5–6 columns of caption-sized links.
- Background `{colors.canvas}`, text `{colors.text-muted}`, type `{typography.caption}`, padding 64px 32px.
- States per link: default · hover (`{colors.text-muted}` to `{colors.ink}`) · focus-visible (2px `{colors.focus}` ring). Two interactive states only — footer links are never disabled.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity; it was not measured from the live site.** Nothing here is an extracted timing function — the values are the **Calm** profile from the audit spec, chosen because this file's own voice is editorial and poster-like: one assertive statement per band, opacity-led fades, little travel. Framer is a builder tool, but the artefact documented here is its marketing canvas, and that canvas is composed, not tool-crisp.

Only `transform` and `opacity` animate. Layout properties are never transitioned — no `width`, no `height`, no `top`, no `left`, no `margin` — because a dark canvas this sparse shows reflow immediately.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, card, nav link) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`; `transform: scale(1.01)` on cards | Opacity only at `{motion.duration-reduced}`; scale dropped |
| Press (pill, icon button) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.97)` | No transform; fill opacity step at `{motion.duration-reduced}` |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the `{colors.focus}` ring | Ring appears instantly, no fade — focus must never lag |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` 0→1, `transform: translateY(8px)` on the first band only | Opacity only at `{motion.duration-reduced}`; no travel |
| Modal / drawer | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: scale(0.98)→1`; backdrop `opacity` | Opacity only at `{motion.duration-reduced}`; no scale |
| Dropdown / nav menu | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(-4px)→0` | Opacity only at `{motion.duration-reduced}`; no travel |
| Toast | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(12px)→0` | Opacity only at `{motion.duration-reduced}`; no travel |
| List enter (gallery, template grid) | `{motion.duration-base}`, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity` + `transform: translateY(12px)→0` | Stagger removed, all items fade together at `{motion.duration-reduced}` |
| List exit (filtered-out tiles) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)` | Opacity only at `{motion.duration-reduced}`; no scale |
| Loading (button spinner, tile skeleton) | 800ms per rotation, infinite | linear | `transform: rotate()`; skeleton `opacity` 0.4↔0.7 | Spinner frozen at one frame; skeleton holds a static `opacity` 0.5 |
| Display-type reveal (hero band) | `{motion.duration-emphasis}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(16px)→0` | Opacity only at `{motion.duration-reduced}`; no travel |

### Rules

- Exit is always shorter than its matching entrance: `{motion.duration-fast}` out against `{motion.duration-base}` in.
- Nothing animates on first paint in a way that delays content — the hero reveal runs on type that is already laid out and already readable.
- The loading spinner is the only infinite animation. There is no brand ambience loop; the gradient spotlight cards are static grounds, not moving ones.
- Gradient spotlight cards never animate their gradient. Hover lifts the tile; the colour itself holds.
- `{motion.duration-slow}` is held in reserve for a full-bleed gallery crossfade; nothing in the marketing chrome runs that long, and no interaction in the table above reaches for it.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale — translateY on the hero reveal, page
     transition, dropdown, toast and list enter; scale on press, card hover,
     modal and list exit; the {motion.stagger-step} cascade on grids. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} 150ms. */
  /* Frozen: the loading spinner holds a single frame and the skeleton holds a
     static opacity; no looping remains anywhere in the system. */
  *, *::before, *::after {
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important;
    transition-property: opacity !important;
    transform: none !important;
  }
}
```

The focus ring is the one exception: it is not faded at all under reduced motion, because a delayed focus indicator is worse than an abrupt one.

## Accessibility

Every ratio below is computed from this file's own tokens with WCAG 2.1 relative luminance. Nothing here is measured from a rendered page: this document has no DOM, so tap targets are stated as the spec the breakpoints require, not as an observed measurement.

### Measured contrast

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` #ffffff on `{colors.canvas}` | 19.91:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface}` | 18.42:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-raised}` | 17.04:1 | 4.5:1 | Pass |
| `{colors.text-muted}` #999999 on `{colors.canvas}` | 6.99:1 | 4.5:1 | Pass |
| `{colors.text-muted}` on `{colors.surface-raised}` | 5.98:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 21.0:1 | 4.5:1 | Pass |
| `{colors.accent-blue}` on `{colors.canvas}` | 6.64:1 | 4.5:1 | Pass (hyperlink text) |
| `{colors.semantic-success}` on `{colors.canvas}` | 8.74:1 | 4.5:1 | Pass (glyph) |
| `{colors.focus}` on `{colors.canvas}` | 6.64:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 3.74:1 | 3.0:1 | Pass |
| `{colors.hairline}` #262626 on `{colors.canvas}` | **1.32:1** | 3.0:1 | **Fail — extracted, frozen, decorative only** |
| `{colors.hairline-soft}` #1a1a1a on `{colors.canvas}` | **1.14:1** | 3.0:1 | **Fail — extracted, frozen, decorative only** |
| `{colors.hairline}` on `{colors.surface}` | **1.22:1** | 3.0:1 | **Fail — extracted, frozen, decorative only** |
| `{colors.hairline-soft}` on `{colors.surface}` | **1.06:1** | 3.0:1 | **Fail — extracted, frozen, decorative only** |
| `{colors.ink}` on `{colors.gradient-violet}` | 5.30:1 | 3.0:1 large / 4.5:1 body | Pass large, fail body |
| `{colors.ink}` on `{colors.gradient-magenta}` | 3.43:1 | 3.0:1 large | Pass large only |
| `{colors.ink}` on `{colors.gradient-coral}` | 3.08:1 | 3.0:1 large | Pass large only, with no margin |
| `{colors.ink}` on `{colors.gradient-orange}` (`gradient-spotlight-card-orange`) | **2.59:1** | 3.0:1 large | **Fail at every text size — extracted, frozen** |

### Where this brand fails AA, plainly

- **The two extracted hairlines fail by a wide margin.** `{colors.hairline}` at 1.32:1 and `{colors.hairline-soft}` at 1.14:1 are real values off the real site, and on a #090909 canvas they are visible as texture, not as boundaries. They are kept, scoped to decoration, and `{colors.hairline-strong}` (3.74:1, prescribed) is the token for any boundary a reader has to find — input edges, the comparison table's rules, the current-section marker.
- **`gradient-spotlight-card-orange` fails for white type at any size: 2.59:1.** This is not a mis-bound token. The card binds `{colors.ink}` exactly as its violet, magenta and coral siblings do, which is what the brand does; the orange ground is simply the lightest of the four anchors, and white on it clears neither 4.5:1 nor the 3:1 large-text floor. The hex is a frozen extracted anchor and is not changed here. Two defensible routes, both needing a brand decision: set the card's type to `{colors.on-primary}` black, which measures 8.10:1 on this ground and 3.97:1 or better on all four gradients; or darken the ground to #e05f20, which carries white at 3.60:1 for `{typography.subhead}` 24px and above. Until one is chosen, treat orange spotlight cards as image-grade decoration and keep no essential text on them.
- **White on magenta (3.43:1) and coral (3.08:1) is large-text-only.** Both clear 3:1 at the `{typography.subhead}` 24px/400 these cards use and neither clears 4.5:1, so body copy, captions and `{typography.micro}` must not sit on a gradient tile.

### Focus ring visibility, per surface this file defines

| Surface | Ring token | Ratio | Verdict |
|---|---|---|---|
| `{colors.canvas}` | `{colors.focus}` | 6.64:1 | Pass |
| `{colors.surface}` | `{colors.focus}` | 6.14:1 | Pass |
| `{colors.surface-raised}` | `{colors.focus}` | 5.68:1 | Pass |
| `{colors.inverse-canvas}` (white pill, light thumbnails) | `{colors.focus}` | 3.00:1 | Pass, exactly at the threshold |
| `{colors.gradient-violet}` | `{colors.focus-on-gradient}` | 3.97:1 | Pass |
| `{colors.gradient-magenta}` | `{colors.focus-on-gradient}` | 6.12:1 | Pass |
| `{colors.gradient-orange}` | `{colors.focus-on-gradient}` | 8.10:1 | Pass |
| `{colors.gradient-coral}` | `{colors.focus-on-gradient}` | 6.82:1 | Pass |

- The ring is 2px with a 2px offset, drawn outside the component so the pill's `{rounded.pill}` silhouette stays intact.
- `{colors.focus}` on a gradient ground measures 1.16:1 on orange and 1.77:1 on violet — never use it there; that is what `{colors.focus-on-gradient}` exists for.
- `{colors.focus-on-gradient}` is a gradient-only ring and is deliberately near-invisible on the monochrome layers — 1.05:1 on `{colors.canvas}`, 1.14:1 on `{colors.surface}`, 1.23:1 on `{colors.surface-raised}`. Those are not usable focus indicators and the ring is never drawn there; `{colors.focus}` serves every dark surface.
- The extracted `rgba(0,153,255,0.15)` 0 0 0 1px glow on focused inputs is decorative and far below 3:1. It may stay, but it is not the focus indicator.

### Tap targets

Specified, not measured — this file documents no rendered page.

- Pill CTAs hold a minimum 44×44px hit area at every breakpoint (14px `{typography.button}` plus 10px vertical padding plus hit-area padding).
- `button-icon-circular` is 40px on pointer viewports and grows to 44px below the 810px breakpoint.
- Pricing-tab pills hold ≥40px and gain spacing rather than shrinking when the row scrolls horizontally.

### Reduced motion

Honoured as written in Motion & Animation: all travel and scale removed, opacity fades capped at `{motion.duration-reduced}` 150ms, the loading spinner frozen on one frame, and the focus ring never faded.

### Other

- Dark canvas only. There is no light mode to check, and a forced-colors pass is undocumented — see Known Gaps.
- Hierarchy is carried by size and tracking rather than colour alone, so the `ink` / `text-muted` split is not the only signal in any component here.
- `{typography.display-xxl}` at -5.5px tracking is a brand constant; where it harms legibility, reduce the size tier and keep the percentage.

## Do's and Don'ts

### Do

- Reserve `{colors.primary}` (white) and `{colors.canvas}` (near-black) as the system's two anchor surfaces. Every band of the page chooses one or the other.
- Push display-size letter-spacing aggressively negative — `{typography.display-xxl}` at -5.5px is the brand signature, not a stylistic accident.
- Use `{colors.accent-blue}` only for hyperlinks, focus rings, and selected indicators. Never as a background or button fill.
- Drop one or two `gradient-spotlight-card` variants into a card grid; they are the brand's atmosphere device. Don't overdo it — three or more in the same viewport reads as a moodboard, not a system.
- Compose every CTA as a pill (`{rounded.pill}`); secondary actions live as charcoal pills, never as bordered ghost buttons.
- Keep body type Inter Variable with character variants `cv01`, `cv05`, `cv09`, `cv11`, `ss03`, `ss07` enabled — the brand voice depends on them.
- Use surface lift (canvas → surface → surface-raised) to mark hierarchy on dark, not opacity changes on white type.

### Don't

- Don't ship a light-mode marketing page. Framer's identity is dark.
- Don't introduce mid-tone gray text outside `{colors.text-muted}`. The hierarchy is binary: `ink` or `text-muted`.
- Don't use `{colors.accent-blue}` as a brand fill (e.g., a blue CTA pill). The blue is a signal color, not a surface.
- Don't square off CTAs. Pill (`{rounded.pill}`) or full circle is the brand vocabulary.
- Don't reduce the negative letter-spacing on display sizes "for accessibility". The compression is intrinsic to the brand voice; reduce the SIZE if needed, but keep the percentage.
- Don't apply gradient backgrounds to whole sections. Gradients are CARDS, not section grounds.
- Don't combine more than one chromatic accent. The palette is monochrome plus one blue plus the gradient family — not "blue, green, and red".

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop | 1199px | Default desktop layout |
| Tablet | 810px | Card grids collapse 4-up → 2-up; nav becomes hamburger |
| Mobile-Lg | 809px | Pricing comparison table becomes per-tier accordion |
| Mobile-XS | 98px | Smallest documented breakpoint — single-column everything |

### Touch Targets

- Pill buttons (`button-primary`, `button-secondary`) maintain a minimum 44px tap height across all viewports — combine `{typography.button}` 14px line-height with the documented 10px vertical padding.
- Circular icon buttons (`button-icon-circular`) are 40px on desktop and grow to 44px on touch viewports.
- Pricing-tab pills hold ≥40px tap height; below 810px they may collapse into a horizontal-scroll row instead of stacking.

### Collapsing Strategy

- **Nav**: horizontal nav with a centered link group + right-anchored pill pair collapses to a hamburger overlay below 810px. The `button-primary` stays visible on the bar.
- **Card grids**: the gallery and template-card grids go 2-up on desktop → 1-up on mobile. Gradient spotlight cards retain `{rounded.xxl}` corners at every viewport — they don't bleed.
- **Pricing comparison table**: collapses into per-tier accordions below 810px to avoid horizontal scroll.
- **Display type**: `{typography.display-xxl}` 110px scales down toward `{typography.display-lg}` 62px on tablet and `{typography.display-md}` 32px on mobile, preserving the percentage-negative letter-spacing.

### Image Behavior

- Embedded product mockups (browser frames containing live Framer-built sites) maintain their aspect ratio and never crop.
- Gradient spotlight cards keep their gradient orientations across breakpoints — the gradient direction is part of the brand spec.

## Iteration Guide

1. Focus on ONE component at a time and reference it by its `components:` token name (e.g., `{components.button-primary}`, `{components.gradient-spotlight-card}`).
2. When introducing a new section on the dark canvas, decide first which surface lift it lives on — `{colors.canvas}` for hero/FAQ, `{colors.surface}` for cards, `{colors.surface-raised}` for featured cards. The depth choice is the most consequential decision.
3. Default body to `{typography.body}` with all the documented OpenType variants; reach for `{typography.subhead}` only inside spotlight cards.
4. Run `npx @google/design.md lint DESIGN.md` after edits — `broken-ref`, `contrast-ratio`, and `orphaned-tokens` warnings flag issues automatically.
5. Add new variants as separate component entries (`-pressed`, `-featured`, `-selected`) — do not bury them in prose.
6. Treat `{colors.accent-blue}` as a single-shot signal color: hyperlinks, focus, and selection — that's it. If you find yourself reaching for a second blue, the brand is drifting.
7. Gradient spotlight cards are scarce by design. One or two per long page is the spec; three is a moodboard.

## Known Gaps

- The exact gradient stops for the spotlight cards are derived from screenshot pixels rather than from CSS variables — the production gradients are likely defined as `linear-gradient` strings on individual elements rather than as design tokens. Treat the documented `{colors.gradient-*}` hex values as base anchors, not as exact gradient specs.
- Form-field validation / error styling is not visible on the inspected pages because no error states render in the static screenshots.
- Dark mode is the only mode — no light-mode adaptation is documented because the marketing site does not ship one.
- The marketplace template detail page returned sparser CSS variable data than the other pages; surface tokens for that page were inferred from the matching home / gallery treatment rather than extracted directly.
- The whole Motion & Animation section is prescribed, not extracted. No timing function, duration or stagger in this file was measured from framer.com; they are the audit spec's Calm profile values, applied so this file is comparable with its siblings.
- Component states beyond default, pressed, selected and focused are prescribed. The source material is static captures, so hover, disabled, loading and error behaviour is specified rather than observed.
- `{colors.hairline-strong}`, `{colors.focus}` and `{colors.focus-on-gradient}` are prescribed accessible additions, not extracted brand tokens. The real site's focus signal is the sub-3:1 `{shadow.focus-glow}`.
- Forced-colors / high-contrast mode is undocumented. Nothing in the inspected pages shows how the gradient spotlight cards or the surface ladder behave when the system overrides colour.
- Tap-target sizes, overlap, clipping and frame rate cannot be verified from a document. The figures in Accessibility and Responsive Behavior are the spec to build to, not measurements.
