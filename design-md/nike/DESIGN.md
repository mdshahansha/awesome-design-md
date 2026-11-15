---
version: alpha
name: Nike-design-analysis
description: |
  A photography-first commerce system built on extreme typographic contrast — towering uppercase Futura display lockups burned into editorial campaign imagery, sitting above a dense, neutral, near-monochrome retail chrome of pill-shaped black CTAs, gray search and tag pills, and tight 8px-grid product cards. The brand's voice is athletic, kinetic, and absolute: pure black, pure white, a single soft surface gray, and a deliberately small set of semantic accents (sale red, success green, restrained category tints) — every chromatic moment is reserved for editorial photography or pricing signal, never decorative chrome.

colors:
  primary: "#111111"
  on-primary: "#ffffff"
  canvas: "#ffffff"
  soft-cloud: "#f5f5f5"
  ink: "#111111"
  charcoal: "#39393b"
  ash: "#4b4b4d"
  mute: "#707072"
  stone: "#9e9ea0"
  hairline: "#cacacb"
  hairline-soft: "#e5e5e5"
  focus: "#111111"
  focus-on-dark: "#ffffff"
  sale: "#d30005"
  sale-deep: "#780700"
  success: "#007d48"
  success-bright: "#1eaa52"
  info: "#1151ff"
  info-deep: "#0034e3"
  accent-pink: "#ed1aa0"
  accent-pink-soft: "#ffb0dd"
  accent-purple-soft: "#beaffd"
  accent-purple-pale: "#d6d1ff"
  accent-teal: "#0a7281"
  accent-pink-deep: "#4c012d"

typography:
  display-campaign:
    fontFamily: Nike Futura ND
    fontSize: 96px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: 0
    textTransform: uppercase
  heading-xl:
    fontFamily: Helvetica Now Display Medium
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  heading-lg:
    fontFamily: Helvetica Now Display Medium
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  heading-md:
    fontFamily: Helvetica Now Display Medium
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.75
    letterSpacing: 0
  body-md:
    fontFamily: Helvetica Now Text
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-strong:
    fontFamily: Helvetica Now Text Medium
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  button-lg:
    fontFamily: Helvetica Now Display Medium
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: Helvetica Now Text Medium
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  button-sm:
    fontFamily: Helvetica Now Text Medium
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  link-md:
    fontFamily: Helvetica Now Text
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.75
    letterSpacing: 0
    textDecoration: underline
  caption-md:
    fontFamily: Helvetica Now Text Medium
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: Helvetica Now Text Medium
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  utility-xs:
    fontFamily: Helvetica Neue
    fontSize: 9px
    fontWeight: 500
    lineHeight: 1.75
    letterSpacing: 0

rounded:
  none: 0px
  sm: 18px
  md: 24px
  lg: 30px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 18px
  xl: 24px
  xxl: 30px
  section: 48px

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
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 16px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.soft-cloud}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 16px 32px
    height: 48px
  button-outline-on-image:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
  button-icon-circular:
    backgroundColor: "{colors.soft-cloud}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 40px
  search-pill:
    backgroundColor: "{colors.soft-cloud}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 40px
  search-pill-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  badge-promo:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-sale-text:
    textColor: "{colors.sale}"
    typography: "{typography.caption-md}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
    padding: 0px
  product-card-image:
    backgroundColor: "{colors.soft-cloud}"
    rounded: "{rounded.none}"
  swatch-dot:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 12px
  swatch-dot-active:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 12px
  campaign-tile:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-campaign}"
    rounded: "{rounded.none}"
  category-icon-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.none}"
  member-benefit-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.none}"
  faq-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-md}"
    rounded: "{rounded.none}"
    padding: 24px 0px
  pdp-disclosure-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
    padding: 24px 0px
  utility-bar:
    backgroundColor: "{colors.soft-cloud}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.none}"
    height: 36px
  primary-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
    height: 56px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.mute}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.none}"
---

## Overview

Nike's commerce system is built on a single, almost violently simple idea: photography speaks, the chrome doesn't. Every page reads as an athletic editorial — towering uppercase Futura display lockups (`{typography.display-campaign}`) burned into full-bleed campaign imagery, with everything else (nav, filters, buttons, cards, footer) reduced to neutral typography and pill geometry on `{colors.canvas}` and `{colors.soft-cloud}`. There is no decorative gradient, no soft shadow nostalgia, no accent color used for "tone" — the system saves all chromatic energy for product photography and the small handful of moments that actually need to signal (sale price `{colors.sale}`, success `{colors.success}`, swatch dots).

The result is a layout that feels physical — campaign hero, product grid, sport tile, footer — stacked like a printed catalog rather than animated like a typical SaaS landing page. Density is high but never crowded, because the system relies on three relentless devices: square or near-square 1:1 product imagery on `{colors.soft-cloud}`, pill-shaped black CTAs (`{rounded.full}`) anchoring every actionable surface, and a tight 8px-base spacing scale that keeps cards and filters mathematically aligned across PLP, PDP, and editorial pages.

Across `/men`, the trail-running listing, the Zegama PDP, `/membership`, and Jordan Golf, the same chrome appears in identical proportions — only the photography and copy change. That is the system's signature: maximum editorial expression in the imagery, maximum mechanical restraint everywhere else.

**Key Characteristics:**
- Editorial campaign hero with `{typography.display-campaign}` (Nike Futura ND, 96px, line-height 0.9, uppercase) burned directly into full-bleed photography
- Pure black/white/single-gray UI palette: `{colors.ink}`, `{colors.canvas}`, and `{colors.soft-cloud}` carry ~95% of the chrome surface area
- Pill geometry everywhere: every CTA, search field, filter chip, and badge uses `{rounded.full}` (30px) or `{rounded.md}` (24px) — there are no sharp-cornered buttons in the system
- Product cards have zero radius, zero shadow, sit directly on `{colors.soft-cloud}` swatch backgrounds — the photograph is the card
- Two-tone CTA hierarchy: `{component.button-primary}` (black on anything light) versus `{component.button-secondary}` (`{colors.soft-cloud}` on anything bright) — never both at once on the same surface
- 8px spacing system with section rhythm at `{spacing.section}` (48px) creating consistent vertical breathing across PLP, PDP, and editorial pages
- Sale signaling is the only place a non-neutral color appears in retail chrome: `{colors.sale}` price + strike-through original price, no badge background

## Colors

> **Source pages:** `/men` (primary), `/w/mens-acg-trail-running-shoes-…`, `/t/acg-zegama-…`, `/membership`, `/w/jordan-golf-…`. The chrome palette is identical across all five — only photography varies.

### Brand & Accent
- **Nike Black** (`{colors.ink}` — `#111111`): The brand's only "color." It is the primary CTA, the swatch dot, the active filter chip, the campaign overlay, the headline color, and the body text. When Nike wants to assert anything, it goes black.
- **Pure White** (`{colors.on-primary}`, `{colors.canvas}` — `#ffffff`): Equal partner to black. Carries every page background, the on-image CTA, and the inverse text on `{colors.ink}` surfaces.

### Surface
- **Soft Cloud** (`{colors.soft-cloud}` — `#f5f5f5`): The most-used non-white surface in the entire system. Product card image backgrounds, search pill, secondary CTA, utility bar, sport-category swatch tiles. It is the "color" of every product photograph's stage.
- **Hairline** (`{colors.hairline}` — `#cacacb`): **Decorative dividers only** — 1px rules between filter rows, footer columns, and PDP disclosure rows, where the row label carries the meaning and the rule is an optical separator. At 1.64:1 on `{colors.canvas}` it is below the 3:1 WCAG 1.4.11 floor, so it must never be the only boundary of an interactive control. Extracted and frozen.
- **Hairline Soft** (`{colors.hairline-soft}` — `#e5e5e5`): **Decorative only** — inset 1px shadow under sticky bars and tab strips, the only "shadow" the system uses. 1.26:1 on `{colors.canvas}`; same restriction as above.
- **Control boundary** — where a 1px edge *is* the control (filter chip, promo badge, resting search pill, swatch ring on a white colorway), draw it in `{colors.mute}` (`#707072`), which the palette already owns: 4.94:1 on `{colors.canvas}` and 4.53:1 on `{colors.soft-cloud}`. No new boundary token is introduced; Nike's own neutral ladder already contains a tone that clears the threshold.

### Focus
Nike has no accent colour — black is its only "colour" — so the focus ring is drawn in the brand's own ink or its own paper, never in an invented hue, with a mandatory 2px offset in the opposite polarity so the ring never touches the control it surrounds.
- **Focus** (`{colors.focus}` — `#111111`, the same value as `{colors.ink}`): the default ring, drawn on `{colors.canvas}` (18.88:1) and `{colors.soft-cloud}` (17.32:1). 2px ring, 2px offset gap in `{colors.canvas}`. This is the generalisation of the extracted `search-pill-focused` treatment (2px ink border plus soft-cloud halo) to every control in the system; the ring token itself is **prescribed**.
- **Focus on Dark** (`{colors.focus-on-dark}` — `#ffffff`): the counterpart ring for the system's dark grounds — `{component.campaign-tile}` and `{component.member-benefit-card}`, both filled `{colors.ink}` — where the ink ring measures 1:1 and is invisible. 18.88:1 on `{colors.ink}`; 2px ring with a 2px offset gap in `{colors.ink}`. **Prescribed.**
- Over full-bleed photography, which has no measurable colour, the ring is two-tone: 2px `{colors.focus-on-dark}` with a 1px outer edge in `{colors.focus}`.

### Text
- **Ink** (`{colors.ink}` — `#111111`): Primary text on light surfaces — headlines, product names, prices, nav.
- **Charcoal** (`{colors.charcoal}` — `#39393b`): Slightly softer body where ink is too heavy.
- **Ash** (`{colors.ash}` — `#4b4b4d`): Disabled secondary border on dark surfaces and very low-emphasis utility text.
- **Mute** (`{colors.mute}` — `#707072`): Product category subtitles ("Men's Trail Running Shoes"), footer link text, secondary metadata.
- **Stone** (`{colors.stone}` — `#9e9ea0`): Inverse secondary text on dark surfaces and lowest-emphasis utility text.

### Semantic
- **Sale** (`{colors.sale}` — `#d30005`): Discounted price color and "% off" copy — the only red in the entire retail chrome.
- **Sale Deep** (`{colors.sale-deep}` — `#780700`): Sale price hover/pressed and dark-mode sale anchor.
- **Success** (`{colors.success}` — `#007d48`): Confirmation messages, in-stock indicators, eligibility ticks.
- **Success Bright** (`{colors.success-bright}` — `#1eaa52`): Inverse success on dark surfaces.
- **Info** (`{colors.info}` — `#1151ff`): Informational link/badge accent in member-experience callouts.
- **Info Deep** (`{colors.info-deep}` — `#0034e3`): Pressed state for info accent.

### Category Accents (sport / collection chips)
These appear sparingly — almost exclusively as small chip backgrounds, swatch dots, or category illustrations in editorial tiles. They are never used as text or primary CTA color.
- **Accent Pink** (`{colors.accent-pink}` — `#ed1aa0`): SKIMS / women's collection moments.
- **Accent Pink Soft** (`{colors.accent-pink-soft}` — `#ffb0dd`): Soft tinting on member-experience tiles.
- **Accent Purple Soft** (`{colors.accent-purple-soft}` — `#beaffd`): Editorial swatch dot, soft category chip.
- **Accent Purple Pale** (`{colors.accent-purple-pale}` — `#d6d1ff`): Lightest soft-tile fill.
- **Accent Teal** (`{colors.accent-teal}` — `#0a7281`): Trail / outdoor / ACG editorial accent in lockups.
- **Accent Pink Deep** (`{colors.accent-pink-deep}` — `#4c012d`): Deepest editorial overlay tint, used as wash on heritage / Jordan tiles.

## Typography

### Font Family
- **Nike Futura ND** (display campaign only) — proprietary geometric sans for the towering uppercase headlines burned into campaign hero photography. Falls back to Helvetica Now Text Medium → Helvetica → Arial.
- **Helvetica Now Display Medium** (headings 16–32px) — modern Helvetica cut tuned for display sizes; carries every section title, PDP product name, and dialog headline.
- **Helvetica Now Text Medium** (UI 12–16px) — buttons, captions, swatch labels, badge text. The system's UI workhorse.
- **Helvetica Now Text** (body and links) — long-form body and underlined inline links.
- **Neue Frutiger Arabic** — RTL pairing for Arabic locales at `{typography.heading-lg}` and caption sizes.
- **Helvetica Neue 9px** — legal-fine-print utility row only (`{typography.utility-xs}`).

When substituting on systems without proprietary Nike fonts: pair **Inter** (Display 700 for body chrome, Display 500 for buttons) with **Bebas Neue** or **Anton** at 96px/0.9 line-height for the campaign headline tier. Tighten letter-spacing slightly (-0.5%) on the substitute to approximate Futura ND's optical weight.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-campaign}` | 96px | 500 | 0.9 | 0 | Editorial campaign headline burned into hero photography (uppercase) |
| `{typography.heading-xl}` | 32px | 500 | 1.2 | 0 | Section headers — "FEATURED FOOTWEAR", "LATEST IN CLOTHING", PDP product title block |
| `{typography.heading-lg}` | 24px | 500 | 1.2 | 0 | Subsection / member-benefit card title, large CTA label, PDP price |
| `{typography.heading-md}` | 16px | 500 | 1.75 | 0 | Card title, FAQ row label, filter group header |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Body copy, search-pill placeholder, product description |
| `{typography.body-strong}` | 16px | 500 | 1.5 | 0 | Product card name, filter row label, primary nav link |
| `{typography.button-lg}` | 24px | 500 | 1.2 | 0 | Pressed-letter campaign CTA inside hero blocks |
| `{typography.button-md}` | 16px | 500 | 1.5 | 0 | Standard pill CTAs across the system |
| `{typography.button-sm}` | 14px | 500 | 1.5 | 0 | Compact pill CTA, badge label, geo-selector button |
| `{typography.link-md}` | 16px | 500 | 1.75 | 0 | Underlined inline link, "View Product Details" |
| `{typography.caption-md}` | 14px | 500 | 1.5 | 0 | Product subtitle ("Men's Trail Running Shoes"), filter count, footer link |
| `{typography.caption-sm}` | 12px | 500 | 1.5 | 0 | Filter chip label, badge text, color count |
| `{typography.utility-xs}` | 9px | 500 | 1.75 | 0 | Legal copyright / fine-print row at the very bottom |

### Principles
The system runs on extreme typographic contrast: a single 96px uppercase display tier reserved for editorial campaign moments, and a quiet 12–16px Helvetica Now Text/Medium tier carrying everything else. There is almost no middle ground — the jump from `{typography.heading-xl}` (32px) directly to `{typography.body-strong}` (16px) is intentional and creates the "billboard above, catalog below" effect across every page. Letter-spacing is left at 0 (Futura ND and Helvetica Now are both cut for tight optical fit at scale).

### Note on Font Substitutes
The closest open-source path to Nike's display tier is **Bebas Neue** (free, geometric condensed) at 96px / 0.9 / uppercase / 500. For UI text, **Inter** is the safest substitute — match weights 400/500 and the system reads almost identically at button and caption sizes.

## Layout

### Spacing System
- **Base unit:** 8px
- **Tokens (front matter):** `{spacing.xxs}` (2px) · `{spacing.xs}` (4px) · `{spacing.sm}` (8px) · `{spacing.md}` (12px) · `{spacing.lg}` (18px) · `{spacing.xl}` (24px) · `{spacing.xxl}` (30px) · `{spacing.section}` (48px+)
- **Universal rhythm:** every page in the set uses `{spacing.section}` (48px) as the vertical gap between major content blocks (campaign hero → trending row → featured row → shop-by-sport → latest-in-clothing → footer). PLP card grids use `{spacing.sm}` (8px) gutters. PDP disclosure rows are stacked at `{spacing.xl}` (24px) vertical padding.
- **Card internal padding:** product cards use 0px internal padding — image is full-bleed; metadata rows sit directly below with `{spacing.sm}` (8px) gap between name, subtitle, and price.

### Grid & Container
- **Max width:** ~1440px content area with edge gutters that grow to ~80px at 1920px (the system lets very wide viewports breathe rather than stretch).
- **Column patterns:** PLP listing uses 3-up at desktop, collapsing to 2-up at 1023px and 1-up at 599px. The men's home `/men` mixes a 2-up campaign hero row, a 3- or 4-up "Trending Now" row, a horizontal-scroll "Shop by Sport" rail, and a 4-up "Latest in Clothing" thumbnail grid.
- **Filter sidebar:** ~220px fixed-width left rail on PLP at desktop, collapsing into a `Hide Filters` toggle button at narrow widths.

### Whitespace Philosophy
Whitespace is a tool for separation, not for breath. Sections butt directly against each other vertically with `{spacing.section}` rhythm, and product photos tile edge-to-edge inside their grid — there is no padding wrapped around the product image itself. The "air" comes from the `{colors.soft-cloud}` background of the photograph, not from layout margin. Headlines do not have decorative whitespace above them; they sit immediately under the section divider line.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No shadow, no border | Default for cards, buttons, sections — the dominant treatment |
| 1 — Hairline divider | 1px solid `{colors.hairline}` | Filter row separators, footer column borders, PDP disclosure-row separators |
| 2 — Inset bottom-line | `box-shadow: inset 0 -1px 0 {colors.hairline-soft}` | Sticky utility/sub-nav bar bottom edge, tab strip underline |

The system has no drop-shadow elevation in its retail chrome at all. Cards do not lift on the page. The only depth cue is the 1px inset hairline on sticky strips and the contrast between full-bleed photography and `{colors.soft-cloud}` product backdrops.

### Decorative Depth
Depth in Nike's system comes entirely from photography, not from CSS effects:
- **Editorial campaign tiles** create depth via cinematic perspective — a runner on a trail, a model in a courtyard — with the Futura display headline overlaid in white or `{colors.ink}` directly on the image.
- **Product card photography** is shot on flat `{colors.soft-cloud}` to remove any background depth, so the product itself is the only thing with form on the page.
- **Sport-category tiles** on the home page are full-bleed cinematic photography with a small `{component.button-outline-on-image}` pill anchored at the bottom-left, giving a moment of crisp white pill against atmospheric image.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Cards, campaign tiles, product imagery, navigation, footer — every container in the system |
| `{rounded.sm}` | 18px | Avatar / icon container in member-benefit lockups |
| `{rounded.md}` | 24px | Search pill, search submit, filter input |
| `{rounded.lg}` | 30px | Every CTA pill — primary, secondary, on-image, filter chip, geo-selector, "Notify Me" |
| `{rounded.full}` | 9999px | Color swatch dots and circular icon buttons (back, share, favorite, carousel paddle) |

### Photography Geometry
- **Product cards:** consistent 1:1 square or near-square (~4:5 portrait on tall product crops), full-bleed within the card with no padding, sitting on `{colors.soft-cloud}` backdrop.
- **Editorial campaign hero:** ~16:9 or wider cinematic crop, full-bleed across the content max-width, with the Futura display headline burned into the lower-left or upper-left third.
- **Sport-category rail:** 4:5 portrait full-bleed thumbnails with a small CTA pill anchored bottom-left.
- **PDP main image:** square primary image with vertical thumbnail rail to its left (~5–7 thumbnails stacked at small size), enabling rapid color/angle browsing without leaving the page.
- **Avatar / category icon cards:** centered illustrated icon at ~80–96px on `{colors.canvas}` with `{typography.caption-md}` label below.

## Components

> **Extracted versus prescribed states.** Only Default, Active/Pressed, Selected and the search pill's Focused treatment were captured from the live pages; Nike's CSS carries `--pds-color-element-hover` and `--pds-color-text-hover` but their values were not captured. Hover, focus-visible, disabled, loading and error below are therefore **prescribed** from the system's own vocabulary (ink/soft-cloud inversion, pill geometry, the focus ring defined in Colors) and are marked as such in the state table. Variants that were extracted live as separate `components:` entries in the front matter.

### Buttons

**`button-primary`** — the universal Nike CTA
- Background `{colors.ink}`, text `{colors.on-primary}`, type `{typography.button-md}`, padding `16px 32px`, height `{spacing.section}` (48px), rounded `{rounded.lg}` (30px pill).
- Used on every primary action in the system: "Sign Up", "Notify Me", "Buy", "Türkiye" geo-confirm, "Shop" overlay on sport tiles, "Continue".
- Pressed state lives in `button-primary-active` — the bg stays `{colors.ink}` while the surface shrinks to `scale(0.5)` with `opacity: 0.5` (Nike's signature "tap collapse" feedback that's extracted across all five pages).

**`button-secondary`** — soft alternative on light surfaces
- Background `{colors.soft-cloud}`, text `{colors.ink}`, type `{typography.button-md}`, padding `16px 32px`, rounded `{rounded.lg}`.
- Used as the lower-emphasis alternate when a primary CTA already exists, e.g., "United States" geo-decline next to the black "Türkiye" confirm; "Cancel" or "Discover More" on light cards.

**`button-outline-on-image`** — overlay CTA on photography
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.button-md}`, padding `12px 24px`, rounded `{rounded.lg}`.
- The crisp white pill that anchors the bottom-left of every full-bleed sport-category and editorial campaign tile.

**`button-icon-circular`** — chrome icon controls
- Background `{colors.soft-cloud}` or transparent, icon `{colors.ink}`, rounded `{rounded.full}`, size 40px.
- Used for back-arrow, carousel paddle (left/right), wishlist heart, share, and "Hide Filters" toggle.

**`filter-chip`** + **`filter-chip-active`**
- Default: background `{colors.canvas}`, text `{colors.ink}`, 1px control boundary `{colors.mute}` (4.94:1 — the chip's edge is its only affordance, so it cannot use the decorative `{colors.hairline}` at 1.64:1), type `{typography.button-md}`, rounded `{rounded.lg}`, padding `8px 16px`.
- Active: background `{colors.ink}`, text `{colors.on-primary}` — the chip flips fully inverted when selected. No middle state.

### Inputs & Forms

**`search-pill`** + **`search-pill-focused`**
- Default: background `{colors.soft-cloud}`, text `{colors.ink}`, type `{typography.body-md}`, rounded `{rounded.md}` (24px), padding `8px 16px`, height `40px`. Anchored to the right of the primary nav with a small magnifier icon.
- Focused: background `{colors.canvas}`, 2px solid border `{colors.ink}`, with a 12px outer halo of `{colors.soft-cloud}` (the system's only "focus ring" effect). The pill shape stays `{rounded.md}` so the halo reads as a soft glove, not a hard outline.

### Cards & Containers

**`product-card`**
- Container: background `{colors.canvas}`, rounded `{rounded.none}`, padding 0, no shadow.
- Image area: `{component.product-card-image}` — full-bleed product photo on `{colors.soft-cloud}` square.
- Below image (in this order with `{spacing.sm}` between): swatch dot row (3–6 dots at 12px circular), promo badge if applicable (`{component.badge-promo}` "Just In", "Coming Soon", "Recycled Materials"), product name `{typography.body-strong}` `{colors.ink}`, category subtitle `{typography.caption-md}` `{colors.mute}`, price row.
- Price row: regular price `{typography.body-strong}` `{colors.ink}`. If on sale: discounted price `{colors.sale}` followed by strike-through original `{colors.mute}` followed by "% off" in `{colors.sale}`.

**`campaign-tile`** — the brand's signature editorial unit
- Full-bleed photography with `{typography.display-campaign}` headline burned in (uppercase, 96px, line-height 0.9).
- Headline color is whichever of `{colors.canvas}` or `{colors.ink}` reads against the underlying image — not parameterized; chosen per-asset.
- A single `{component.button-outline-on-image}` pill anchored bottom-left of the tile carries the call-to-action.

**`category-icon-card`**
- Container: background `{colors.canvas}`, rounded `{rounded.none}`.
- Centered category illustration (~80px) + label `{typography.caption-md}` `{colors.ink}` directly below. Used in the "Latest in Clothing" 4–8-up icon strip on `/men`.

**`member-benefit-card`**
- Full-bleed photographic card on a dark image background; copy slot at the bottom-left with `{typography.heading-lg}` headline `{colors.on-primary}` and a `{component.button-outline-on-image}` "Explore" pill below.
- Used in the `/membership` "Member Benefits" 3-up grid.

**`swatch-dot`** + **`swatch-dot-active`**
- 12px circle, rounded `{rounded.full}`, no border in default state. Renders the colorway options on every product card and PDP color picker.
- Default: filled with the colorway's actual product color (extracted at runtime from the product image), 1px outer ring in `{colors.mute}` for white/light colorways so they remain visible on `{colors.canvas}` — the extracted ring was `{colors.hairline}` at 1.64:1, which disappears against the page on exactly the colorways that need it.
- Active: identical fill with a 2px `{colors.ink}` outer ring and 2px white interior gap, creating Nike's signature concentric-ring "selected" state. No size change between default and active.

**`badge-promo`**
- Background `{colors.canvas}` with a 1px boundary in `{colors.mute}`, text `{colors.ink}`, type `{typography.caption-sm}`, rounded `{rounded.lg}`, padding `4px 12px`. The badge sits on top of product photography, so its edge is load-bearing and the decorative `{colors.hairline}` cannot carry it.
- Sits on top of product imagery (top-left of card) with copy like "Just In", "Coming Soon", "Recycled Materials", "Member Exclusive".

**`badge-sale-text`**
- Inline price-row text in `{colors.sale}` with no background — the only "badge" in the system that has no container.

### Navigation

**`utility-bar`** — top utility strip
- Background `{colors.soft-cloud}`, text `{colors.ink}`, type `{typography.caption-sm}`, height ~36px, rounded `{rounded.none}`.
- Right-aligned cluster: "Find a Store · Help · Join Us · Sign In". Always present; never collapses.

**`primary-nav`** — main navigation
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-strong}` for nav links, height 56–64px, rounded `{rounded.none}`.
- Layout: Nike swoosh logo at left (32×32), centered nav row ("New & Featured · Men · Women · Kids · Jordan · Nike SKIMS · Sport"), right cluster (search pill, wishlist heart icon, bag icon).
- The active section gets a 2px-bottom underline in `{colors.ink}` — no background fill.

**Sub-nav strip** (PLP) — appears under primary nav with breadcrumb + sort + hide-filters controls.
- Same `{colors.canvas}` background with a 1px inset hairline-soft bottom edge.
- Left: breadcrumb in `{typography.caption-md}` `{colors.mute}` separated by " / ".
- Right: "Hide Filters" toggle + "Sort By: …" dropdown — both in `{typography.button-md}` with chevron icons.

**Top Nav (Mobile)**
- Hamburger menu icon (left), Nike swoosh (center), search + bag icons (right).
- Search pill collapses into an icon-only button at narrow widths; tapping expands a full-width overlay search pill with `{rounded.md}`.
- Primary nav collapses into a full-height drawer that slides in from the left, listing nav rows top-down with `{spacing.xl}` vertical padding.

### Signature Components

**`pdp-disclosure-row`** — PDP information accordion rows
- Stacked rows for "View Product Details", "Shipping & Returns", "Reviews (n)" with `{spacing.xl}` vertical padding and a 1px `{colors.hairline}` divider below each.
- Label `{typography.body-strong}` `{colors.ink}` left-aligned; chevron `{colors.ink}` right-aligned.

**`faq-row`** — `/membership` FAQ accordion
- Identical pattern to `pdp-disclosure-row` but with `{typography.heading-md}` label weight; 1px `{colors.hairline}` divider below each.

**`filter-sidebar`** — PLP left rail
- Container `{colors.canvas}`, rounded `{rounded.none}`.
- Section headers `{typography.body-strong}` `{colors.ink}` with `{spacing.lg}` (18px) vertical gap between groups.
- Active filters get a 1px ink underline; counts in parentheses use `{colors.mute}`.

**`footer`**
- Background `{colors.canvas}` with a single 1px `{colors.hairline}` top divider.
- Four columns: Resources / Help / Company / Promotions & Discounts, each with column header `{typography.body-strong}` `{colors.ink}` and link list `{typography.caption-md}` `{colors.mute}`.
- Below the columns: a horizontal rule, then a fine-print row with `{typography.utility-xs}` `{colors.mute}` (copyright, locale switcher, terms, privacy, supply-chain act).

### Component States

Extracted states are marked **(E)**; everything else is **prescribed** from the system's own ink/soft-cloud vocabulary and the focus ring defined under Colors. Travel and timing for each transition come from Motion & Animation below.

| Component | States | Treatment |
|---|---|---|
| `button-primary` | default **(E)**, hover, focus-visible, active/pressed **(E)**, disabled, loading | hover: fill holds `{colors.ink}`, label opacity to 0.85; focus-visible: 2px `{colors.focus}` ring, 2px offset; active/pressed: `{component.button-primary-active}` — `scale` collapse with `opacity: 0.5`; disabled: fill `{colors.hairline}`, label `{colors.mute}` (exempt from contrast minimums); loading: label swaps for a 3-dot `{colors.on-primary}` pulse, pill width held so the row does not reflow |
| `button-secondary` | default **(E)**, hover, focus-visible, active/pressed, disabled | hover: `{colors.soft-cloud}` to `{colors.hairline-soft}`; focus-visible: `{colors.focus}` ring; pressed: same scale collapse; disabled: label `{colors.stone}` |
| `button-outline-on-image` | default **(E)**, hover, focus-visible, active/pressed | drawn over photography, so focus-visible uses the two-tone ring (`{colors.focus-on-dark}` with a 1px `{colors.focus}` outer edge) |
| `button-icon-circular` | default **(E)**, hover, focus-visible, active/pressed, disabled | hover: `{colors.soft-cloud}` fill appears under a transparent variant; focus-visible: `{colors.focus}` ring at 2px offset outside the 40px circle |
| `search-pill` / `search-pill-focused` | default **(E)**, hover, focus-visible **(E)**, loading, error | focus-visible is the extracted treatment — `{colors.canvas}` fill, 2px `{colors.ink}` border, 12px `{colors.soft-cloud}` halo; loading: inline 3-dot pulse right of the caret; error ("no results for…"): 2px `{colors.sale}` border with the message in `{colors.sale}` below the pill |
| `filter-chip` / `filter-chip-active` | default **(E)**, hover, focus-visible, selected **(E)** | selected is the full ink inversion; there is no intermediate state. No disabled variant — an unavailable facet is removed from the rail, not greyed |
| `swatch-dot` / `swatch-dot-active` | default **(E)**, hover, focus-visible, selected **(E)**, disabled | selected: 2px `{colors.ink}` concentric ring; disabled (sold-out colorway): 45° strike in `{colors.mute}` across the dot |
| `product-card` | default **(E)**, hover, focus-visible, loading | hover: image scales inside its own frame, metadata unchanged; focus-visible: `{colors.focus}` ring around the whole card; loading: `{colors.soft-cloud}` skeleton block at the image ratio with an opacity pulse |
| `badge-promo`, `badge-sale-text` | default only **(E)** | genuinely single-state — both are non-interactive labels, so they carry no hover, focus-visible, pressed, disabled or error variant |
| `campaign-tile`, `member-benefit-card` | default **(E)**, hover, focus-visible | hover: the full-bleed image scales slowly behind a fixed headline; focus-visible: `{colors.focus-on-dark}` ring inset from the tile edge |
| `pdp-disclosure-row`, `faq-row` | default **(E)**, hover, focus-visible, selected/expanded **(E)** | hover: label to `{colors.charcoal}`; expanded: chevron rotates 180°, body reveals |
| `primary-nav` link | default **(E)**, hover, focus-visible, selected **(E)** | selected is the extracted 2px `{colors.ink}` bottom underline; hover draws the same underline at `{colors.hairline}` weight |
| `utility-bar` link, `footer` link | default **(E)**, hover, focus-visible | hover: underline appears, colour `{colors.mute}` to `{colors.ink}` |
| `filter-sidebar` | default **(E)**, loading, error | loading: group headers hold, facet rows become `{colors.soft-cloud}` skeleton bars; error (facet fetch failed): inline `{colors.sale}` retry line |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or choreography below was extracted from Nike's running pages; the only motion fact in the captured evidence is the pressed-state collapse recorded in `{component.button-primary-active}`. Everything else is the **Cinematic** profile from the audit spec, chosen because this file's own devices are cinematic ones: full-bleed editorial photography carrying every hero and category tile, a single 96px uppercase display tier burned into that photography, and a chrome deliberately stripped of decoration so the imagery is the only thing that moves.

The profile is applied with one deliberate split, which the brand's own "athletic, kinetic, absolute" voice demands: **retail chrome runs at `{motion.duration-instant}` and `{motion.duration-fast}`, editorial surfaces run at `{motion.duration-base}` through `{motion.duration-emphasis}`.** A 400ms hover on a filter chip would make a dense PLP feel broken; a 150ms hero reveal would throw away the only slow gesture the brand has. Both ends come from the same Cinematic token block, so this file stays comparable with its siblings.

Only `transform` and `opacity` are animated anywhere in the system. Never `width`, `height`, `top`, `left` or `margin` — the 8px grid and the 1:1 product ratio must not be reflowed by a transition.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover — chrome (pill CTA, chip, nav link, footer link) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | retained at `{motion.duration-reduced}`; no travel to remove |
| Hover — editorial (campaign tile, member-benefit card, product-card image) | `{motion.duration-slow}` | `{motion.ease-standard}` | `transform: scale(1.03)` inside the card frame | scale removed entirely; card is static |
| Press / active (pill CTA, icon circle, swatch dot) | `{motion.duration-instant}` | `{motion.ease-exit}` | `transform: scale()` + `opacity` (the extracted collapse) | scale removed; `opacity` step only, `{motion.duration-reduced}` |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-enter}` | `opacity` | retained unchanged — the ring must never be slower than the keypress that summoned it |
| Page / route transition (PLP → PDP, `/men` → category) | `{motion.duration-base}` out, `{motion.duration-slow}` in | `{motion.ease-exit}` out, `{motion.ease-enter}` in | `opacity` + `transform: translateY(16px)` on the content block | translate removed; cross-fade at `{motion.duration-reduced}` |
| Modal / drawer (mobile nav drawer, off-canvas filter drawer, bag overlay) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `transform: translateX(-100%)` → `0` + scrim `opacity` | slide removed; scrim and panel fade at `{motion.duration-reduced}` |
| Dropdown ("Sort By", geo-selector, size picker) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: scaleY()` from the anchored edge | scale removed; `opacity` only at `{motion.duration-reduced}` |
| Toast ("Added to Bag", "Saved to Favourites") | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px)` | translate removed; fade at `{motion.duration-reduced}`; dwell time unchanged |
| List enter (PLP grid rows, sport rail, swatch row) | `{motion.duration-base}` per item, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity` + `transform: translateY(12px)` | stagger and translate removed; the whole row fades in once at `{motion.duration-reduced}` |
| List exit (facet applied, grid re-query) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` | retained at `{motion.duration-reduced}` |
| Loading (skeleton pulse, 3-dot button loader) | 1200ms loop | `{motion.ease-standard}` | `opacity` 1 → 0.4 → 1 | frozen at a static 0.7 `opacity`; the only looping animation in the system and the only one permitted to loop |
| Campaign hero reveal (first editorial block in view) | `{motion.duration-emphasis}` image, `{motion.duration-slow}` headline at `{motion.stagger-step}` × 2 delay | `{motion.ease-enter}` | image `transform: scale(1.04)` → `1`, headline `opacity` + `transform: translateY(24px)` | all travel and scale removed; image and headline fade together at `{motion.duration-reduced}` |

Exit is shorter than its matching entrance in every row above. Nothing in the table animates on first paint in a way that delays content: the campaign hero reveal is triggered on intersection, and the headline is painted and readable before its transform resolves. The skeleton pulse and the button loader are the only infinite animations; the system has no brand ambience loop.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: every transform — the hero and product-image scale, the drawer
     slide, the page-transition and toast and list-enter translate, the dropdown
     scaleY, the press collapse. Stagger is removed with them: lists appear as
     one block, not in sequence. */
  /* Retained: opacity fades only, capped at {motion.duration-reduced} (150ms),
     which is shorter than this profile's own duration-fast of 240ms. The focus
     ring, the toast dwell time and every state colour change are unaffected. */
  /* Frozen: the skeleton and button-loader pulse hold at a static 0.7 opacity
     rather than looping. */
}
```

## Accessibility

Everything below is computed from this file's own token values with WCAG 2.1 relative luminance. Nothing here was measured from a rendered page: there is no screenshot, no DOM and no browser in this audit, so overlap, clipping, actual tap-target size and focus-order are out of scope and are listed in Known Gaps.

### Measured contrast — key pairs

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` `#111111` on `{colors.canvas}` `#ffffff` | 18.88:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.soft-cloud}` `#f5f5f5` | 17.32:1 | 4.5:1 | pass |
| `{colors.on-primary}` `#ffffff` on `{colors.ink}` | 18.88:1 | 4.5:1 | pass |
| `{colors.charcoal}` `#39393b` on `{colors.canvas}` | 11.52:1 | 4.5:1 | pass |
| `{colors.ash}` `#4b4b4d` on `{colors.canvas}` | 8.70:1 | 4.5:1 | pass |
| `{colors.mute}` `#707072` on `{colors.canvas}` | 4.94:1 | 4.5:1 | pass |
| `{colors.mute}` on `{colors.soft-cloud}` | 4.53:1 | 4.5:1 | pass — with 0.03 of margin, so neither tone may drift further |
| `{colors.sale}` `#d30005` on `{colors.canvas}` | 5.57:1 | 4.5:1 | pass |
| `{colors.success}` `#007d48` on `{colors.canvas}` | 5.21:1 | 4.5:1 | pass |
| `{colors.info}` `#1151ff` on `{colors.canvas}` | 5.76:1 | 4.5:1 | pass |
| `{colors.focus}` `#111111` on `{colors.canvas}` | 18.88:1 | 3.0:1 | pass |
| `{colors.focus}` on `{colors.soft-cloud}` | 17.32:1 | 3.0:1 | pass |
| `{colors.focus-on-dark}` `#ffffff` on `{colors.ink}` | 18.88:1 | 3.0:1 | pass |

### Declared failures — the real brand does not pass here

These are extracted, frozen values. They are not corrected in place, because changing them would make this document a false record of Nike's chrome.

- **`{colors.hairline}` `#cacacb` on `{colors.canvas}` measures 1.64:1**, against the 3:1 that WCAG 1.4.11 requires of a meaningful boundary. Nike's extracted divider genuinely fails. It is now scoped to decorative row rules, where the row label carries the meaning; every control whose edge is its only affordance uses `{colors.mute}` at 4.94:1 instead.
- **`{colors.hairline-soft}` `#e5e5e5` on `{colors.canvas}` measures 1.26:1.** Same verdict, same scoping: this is the inset bottom-line under sticky bars, which is a visual seam and never an interactive boundary.
- **`{colors.success-bright}` `#1eaa52` measures 3.03:1 on `{colors.canvas}`**, below the 4.5:1 required of text. The palette documents it as inverse success for dark surfaces, where it measures 6.23:1 on `{colors.ink}` and passes; drawn as text on the white canvas it fails and must not be used there.
- **`{colors.stone}` `#9e9ea0` measures 2.67:1 on `{colors.canvas}`.** The Colors section describes it as both inverse secondary text on dark surfaces — 7.06:1 on `{colors.ink}`, which passes — and "lowest-emphasis utility text", which on the white canvas fails 4.5:1 and fails even the 3:1 large-text allowance. Use `{colors.mute}` for low-emphasis text on light grounds.
- **`{colors.accent-pink}` `#ed1aa0` measures 4.00:1 on `{colors.canvas}`.** The file already forbids the category accents as text, which is the correct restriction; recorded here so the number is on the page.

### Focus ring visibility, per surface this file defines

| Surface | Ring | Ratio | Offset |
|---|---|---|---|
| `{colors.canvas}` `#ffffff` | `{colors.focus}` | 18.88:1 | 2px gap in `{colors.canvas}` |
| `{colors.soft-cloud}` `#f5f5f5` | `{colors.focus}` | 17.32:1 | 2px gap in `{colors.canvas}` |
| `{colors.ink}` `#111111` — campaign tile, member-benefit card | `{colors.focus-on-dark}` | 18.88:1 | 2px gap in `{colors.ink}` |
| Full-bleed photography — no measurable colour | two-tone: `{colors.focus-on-dark}` with 1px `{colors.focus}` outer edge | not computable | 2px gap, polarity follows the inner band |

Neither ring introduces a new brand colour: `{colors.focus}` reuses the exact value of `{colors.ink}` (`#111111`) and `{colors.focus-on-dark}` reuses `{colors.on-primary}` (`#ffffff`). They exist as named roles because a ring has to be addressable to be specified and measured, and because the two carry distinct jobs on distinct surfaces — not because Nike gained a colour.

The ring is drawn **outside** its control with a stated 2px offset, so it is judged against the surface behind it rather than against the control fill it surrounds — which is what WCAG 2.2 Focus Appearance asks for, and the only way a system whose primary CTA is solid `#111111` can have a visible ring at all. The extracted `search-pill-focused` treatment (2px `{colors.ink}` border plus a 12px `{colors.soft-cloud}` halo) is the one place the system puts the indicator on the control itself; it is kept verbatim because it is extracted, and the halo gives it the required separation from `{colors.canvas}`.

### Tap targets

Documented heights only — nothing here was measured from a rendered page, so these are the token values the file asserts, not observed hit areas. `{component.button-primary}` and `{component.button-secondary}` are 48px high, clearing the 44px WCAG 2.5.5 AAA target. `{component.search-pill}` and the filter chips are 40px, which clears the 24px of WCAG 2.5.8 AA but not 44px; the Responsive Behavior section claims padded hit areas extend them past 48px, which this audit cannot verify. `{component.button-icon-circular}` is 40px and `{component.swatch-dot}` is a 12px visual dot — the swatch is the system's smallest control by a wide margin and its real hit area is unverified.

### Reduced motion

Every transform, scale and stagger in the Motion & Animation table is removed under `@media (prefers-reduced-motion: reduce)`; opacity fades remain, capped at `{motion.duration-reduced}` (150ms), which is deliberately shorter than this file's own `{motion.duration-fast}` (240ms). The skeleton and loader pulses freeze at a static opacity. The focus ring is never slowed and never suppressed.

### Other

Colour is never the sole carrier of meaning in the extracted chrome with one exception worth naming: the sale price row distinguishes itself by `{colors.sale}` plus a strike-through on the original price plus explicit "% off" copy, so the discount survives without colour. The active filter chip inverts fill *and* text, and the selected swatch adds a concentric ring, so both read without hue. The primary-nav active indicator is a 2px underline, also not colour-dependent.

One type size is a legibility problem independent of contrast: `{typography.utility-xs}` is 9px, bound to the footer fine-print row in `{colors.mute}`. The pair passes contrast at 4.94:1, but 9px is below any reasonable floor for sustained reading. It is an extracted value and is kept; it should not be reused for anything the reader is expected to act on.

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
| `{colors.hairline-soft}` (`#e5e5e5`) on `{colors.soft-cloud}` (`#f5f5f5`) | 1.16:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.hairline}` (`#cacacb`) on `{colors.soft-cloud}` (`#f5f5f5`) | 1.50:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.success-bright}` (`#1eaa52`) on `{colors.soft-cloud}` (`#f5f5f5`) | 2.78:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Reserve `{typography.display-campaign}` exclusively for editorial campaign hero lockups — never use 96px Futura for section headers or product titles.
- Use `{component.button-primary}` (`{colors.ink}` pill) as the single primary action per viewport. Pair it at most with `{component.button-secondary}` (`{colors.soft-cloud}` pill) for a soft alternative.
- Stage every product photograph on `{colors.soft-cloud}` — the gray is the system's "studio."
- Keep all CTAs pill-shaped at `{rounded.lg}` (30px). Never introduce a square or `{rounded.sm}` button.
- Use `{colors.sale}` only on price rows — never on backgrounds, badges, or chrome.
- Stack content sections at `{spacing.section}` (48px) rhythm with no decorative dividers between them; the photography's bleed-edge is the divider.
- Anchor on-image CTAs with `{component.button-outline-on-image}` (white pill) at bottom-left — the system's universal "shop this image" position.

### Don't
- Don't introduce drop shadows or card elevation. Cards sit flat on the page; the only depth cue is the 1px inset hairline on sticky bars.
- Don't use any of the category accent colors (`{colors.accent-pink}`, `{colors.accent-purple-soft}`, `{colors.accent-teal}`) for primary chrome — they belong to swatch dots, soft tile fills, and editorial moments only.
- Don't replace `{colors.ink}` with a near-black gray like `{colors.charcoal}` for a CTA — Nike's primary pill is true `#111111`.
- Don't pad inside product cards. The image is full-bleed; metadata sits directly below with `{spacing.sm}` (8px) between rows.
- Don't put two campaign-tile lockups in the same row at the same scale — Nike alternates a single full-bleed editorial tile with a 2-up or 4-up product/category grid.
- Don't underline anything other than `{typography.link-md}` inline links and the active primary-nav indicator. Buttons, headings, and prices stay un-underlined.
- Don't introduce a third button shape. Pill or icon-circular — that's the entire button shape vocabulary.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| ultrawide | 1920px+ | Content max-width holds at ~1440px; outer gutters grow to ~80px on each side |
| desktop-large | 1440px | Default desktop layout — 3-up product grid, 4-up clothing strip, full primary nav |
| desktop | 1200px | Same as large with slightly narrower outer gutters |
| desktop-small | 1024px | Filter sidebar starts compressing; sport rail shows ~3 visible tiles |
| tablet | 1023–961px | 3-up PLP collapses to 2-up; "Hide Filters" becomes a default toggle |
| tablet-narrow | 960–640px | Primary nav center cluster collapses to a hamburger drawer; search pill becomes icon-only |
| mobile-landscape | 639–600px | 2-up PLP collapses to 1-up; product cards become full-width with image and metadata stacking |
| mobile | 599–320px | Single-column everything; campaign tiles render at full screen width with shorter Futura sizes (~64px) |

### Touch Targets
All interactive elements meet WCAG AAA (44×44px minimum). Pills (`{component.button-primary}`, `{component.button-secondary}`) sit at 48px height with 32px horizontal padding. Icon-circular buttons (`{component.button-icon-circular}`) sit at 40px — Nike's PDP carousel paddle and wishlist heart sit just under AAA but above AA at 40×40, with hit-target padding extending the tappable area to 48px+. Filter-chip pills are 40px height with 16px padding.

### Collapsing Strategy
- **Primary nav:** desktop center cluster → mobile drawer triggered by hamburger at left of the swoosh.
- **PLP grid:** 3-up → 2-up → 1-up at 1023, 599, and below; gutters drop from `{spacing.sm}` to `{spacing.xs}` on mobile.
- **Filter sidebar:** 220px fixed → "Hide Filters" toggle → off-canvas full-screen filter drawer at mobile.
- **Sport rail:** desktop horizontal scroll with ~5 visible → mobile horizontal scroll with ~1.5 visible (peek-next-card pattern).
- **Section spacing:** `{spacing.section}` 48px desktop → 32px tablet → 24px mobile to keep editorial rhythm tight on small screens.
- **Editorial campaign headline:** desktop 96px → tablet 64px → mobile 48px, line-height stays at 0.9 across all sizes.

### Image Behavior
- Product imagery is responsive at the same 1:1 ratio across all breakpoints — the image scales, the ratio doesn't.
- Editorial campaign tiles use art-direction crops: a 16:9 wide hero on desktop swaps to a 4:5 portrait on mobile so the figure stays centered and the headline still has burn-in space.
- All non-critical product imagery is lazy-loaded as the user scrolls into the next grid row.

## Iteration Guide

1. Focus on ONE component at a time. Pull its YAML entry from the front matter and verify every property resolves.
2. Reference component names and tokens directly (`{colors.ink}`, `{component.button-primary-active}`, `{rounded.lg}`) — do not paraphrase color names or radii in prose.
3. Run `npx @google/design.md lint DESIGN.md` after edits — `broken-ref`, `contrast-ratio`, and `orphaned-tokens` warnings flag issues automatically.
4. Add new variants as separate component entries (`-active`, `-disabled`, `-focused`) — do not bury them inside prose. Nike's pressed state (`scale(0.5) opacity 0.5`) is intentional and must be its own entry, not a hover stand-in.
5. Default body to `{typography.body-md}`; reach for `{typography.body-strong}` for product names and primary nav links; reserve `{typography.display-campaign}` strictly for hero campaign lockups.
6. Keep `{colors.ink}` scarce per viewport — if more than one solid-black pill or block appears in the same fold, neutralize one to `{component.button-secondary}` or `{component.button-outline-on-image}`.
7. When introducing a new component, ask whether it can be expressed with the existing pill + flat-card + photography-on-`{colors.soft-cloud}` vocabulary before adding new tokens. The system's strength is that it almost never needs new ones.

## Known Gaps

- **Mobile screenshots not captured** — responsive behavior described above synthesizes Nike's known mobile pattern (hamburger drawer, 1-up grid, headline downscale) from desktop evidence and the breakpoint list extracted from tokens.
- **Hover states not documented** by system policy — Nike's CSS uses `--pds-color-element-hover` and `--pds-color-text-hover` tokens but these are not included here. The hover, focus-visible, disabled, loading and error entries in the Component States table are therefore prescribed, not extracted.
- **Motion is prescribed, not extracted** — no timing function or duration in Motion & Animation was measured from Nike's live pages. The only extracted motion fact is the pressed-state collapse in `{component.button-primary-active}`, and even there the recorded `scale(0.5)` looks more like a captured mid-transition frame than a resting value; it is kept verbatim because it is what was extracted.
- **Focus ring is prescribed** — `{colors.focus}` and `{colors.focus-on-dark}` generalise the one extracted focus treatment (`search-pill-focused`) to the rest of the system. No ring was captured on any other control.
- **Tap targets and layout are unverified** — there is no rendered page in this audit, so real hit-area size, overlap, clipping, horizontal overflow and focus order could not be checked. The heights quoted in Accessibility are token values the file asserts.
- **No dark theme is defined** — `{colors.success-bright}` and `{colors.stone}` are described as inverse tones for dark surfaces, but the file declares no dark canvas or dark surface token for them to sit on; their only measurable dark ground is `{colors.ink}`.
- **Dialog / modal styling** beyond the geo-selector and the country-confirmation pill pair could not be confirmed from the captured surfaces; bag, wishlist, and login overlays are not documented.
- **Form field styling** for checkout, sign-up, and address forms is not present in the captured surfaces — only the search pill is documented.
- **Bag and wishlist** icon-state variants (filled count badges) not visible in the captured pages.
