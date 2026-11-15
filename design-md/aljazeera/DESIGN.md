---
version: alpha
name: Al Jazeera Analysis
description: An analysis of Al Jazeera's design language — a hard-news editorial system built on flat white paper and dense Roboto headline stacks, signed by one saturated orange used as logo block and section-eyebrow bar, punctuated by a live-red that marks breaking coverage with timeline dots and LIVE badges, and interfaced through compact black pills; the corporate network pages extend the same identity onto a near-black canvas with royal-indigo hero panels, gold rules and amber links, and vivid teal and crimson section rails beside monochrome leadership portraiture.

colors:
  primary: "#fa9000"
  on-primary: "#ffffff"
  live-red: "#c31833"
  ink: "#000000"
  charcoal: "#333333"
  slate: "#595959"
  canvas: "#ffffff"
  soft: "#f0f0f0"
  hairline: "#d8d8d8"
  silver: "#bebebe"
  indigo: "#272967"
  night-navy: "#100e2f"
  network-canvas: "#181818"
  gold: "#dba200"
  amber: "#ffa000"
  select-gold: "#ffc500"
  rail-teal: "#00cbca"
  rail-red: "#bc0000"
  mist: "#dddddd"
  graphite: "#323232"
  # ─── Prescribed accessibility tokens — NOT extracted from the live site ───
  # Parallel accessible tokens added alongside the frozen extracted tones.
  # surface-soft: alias of soft — the one real raised fill (newsletter card)
  surface-soft: "#f0f0f0"
  # text-secondary: alias of slate — the documented secondary-text tone
  text-secondary: "#595959"
  # border-control: control boundary; hairline #d8d8d8 is decoration only
  border-control: "#595959"
  # focus: ring on light surfaces and on teal/amber chrome
  focus: "#000000"
  # focus-on-dark: ring on ink pills and the network's dark grounds
  focus-on-dark: "#ffc500"

typography:
  headline-xl:
    fontFamily: Roboto
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  headline-lg:
    fontFamily: Roboto
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  headline-md:
    fontFamily: Roboto
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  headline-sm:
    fontFamily: Roboto
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  network-display:
    fontFamily: Roboto
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  section-eyebrow:
    fontFamily: Roboto
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  label-black:
    fontFamily: Roboto
    fontSize: 14px
    fontWeight: 900
    lineHeight: 1
    letterSpacing: 0
  body:
    fontFamily: Roboto
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: Roboto
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: Roboto
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button:
    fontFamily: Roboto
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0

rounded:
  xs: 2px
  sm: 4px
  md: 10px
  lg: 18px
  xl: 22px
  full: 9999px

shadow:
  dropdown: "0 6px 12px rgba(0, 0, 0, 0.175)"

motion:
  # Prescribed to match this brand's visual identity (Calm profile).
  # Not measured from the live site.
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 600ms
  ease-standard: cubic-bezier(0.4, 0, 0.2, 1)
  ease-enter: cubic-bezier(0, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 40ms

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  xxl: 24px
  huge: 30px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 0px 15px

  logo-block:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"

  button-pill-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: 6px 17px

  button-pill-mini:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 1px 6px

  section-eyebrow-lockup:
    textColor: "{colors.slate}"
    typography: "{typography.section-eyebrow}"
    borderColor: "{colors.primary}"

  news-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.headline-md}"

  media-thumb:
    rounded: "{rounded.md}"

  live-badge:
    textColor: "{colors.live-red}"
    typography: "{typography.label-black}"
    rounded: "{rounded.xs}"

  breaking-band:
    backgroundColor: "{colors.live-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.headline-sm}"

  live-strip-item:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.silver}"

  most-popular-row:
    textColor: "{colors.ink}"
    typography: "{typography.headline-sm}"
    borderColor: "{colors.hairline}"
    padding: 16px 0px

  popular-numeral:
    textColor: "{colors.slate}"
    typography: "{typography.headline-lg}"

  newsletter-card:
    backgroundColor: "{colors.soft}"
    textColor: "{colors.ink}"
    typography: "{typography.headline-md}"
    padding: 20px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    borderColor: "{colors.slate}"
    rounded: "{rounded.xl}"
    padding: 0px 15px

  avatar-circle:
    rounded: "{rounded.full}"

  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"

  network-utility-strip:
    backgroundColor: "{colors.night-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"

  network-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.graphite}"
    typography: "{typography.body-sm}"

  network-nav-active:
    textColor: "{colors.amber}"
    typography: "{typography.body-sm}"

  network-hero-panel:
    backgroundColor: "{colors.indigo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.network-display}"
    padding: 24px

  leader-band:
    textColor: "{colors.on-primary}"
    typography: "{typography.network-display}"

  leader-card:
    backgroundColor: "{colors.network-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.headline-md}"

  section-rail-teal:
    backgroundColor: "{colors.rail-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"

  section-rail-red:
    backgroundColor: "{colors.rail-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"

  award-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.graphite}"
    typography: "{typography.headline-sm}"

  network-select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.graphite}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.select-gold}"

  network-footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.mist}"
    typography: "{typography.body-sm}"

  # ─── Examples (illustrative, kit-mirror) ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
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
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.huge}"
    captionTypography: "{typography.body}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Al Jazeera's news surface is a printing press, not a product. The page is flat `{colors.canvas}` paper packed edge-to-edge with photography and dense Roboto headline stacks; there are no shadows, no tonal card fills, no decorative gradients — hierarchy is carried entirely by type weight, rules, and the discipline of the grid. Against that severity the brand signs itself with a single saturated orange: the `{colors.primary}` logo block in the masthead and the short orange bar that fronts every section eyebrow ("MUST READ", "OPINION", "FEATURED"). Orange never fills a button and never colors a link — it is a marker pen, not a control.

Urgency has its own color. `{colors.live-red}` belongs exclusively to the live apparatus: the LIVE badge beside the masthead, the breaking-coverage band, the pulsing dots of the minute-by-minute timeline, and the LIVE UPDATES labels on running stories. Actions, by contrast, are quiet black objects — compact `{colors.ink}` pills at `{rounded.lg}` for Sign up and Subscribe, a rounded `{rounded.xl}` email capsule for the newsletter — so that nothing competes with the news imagery for attention.

The corporate network pages flip the polarity while keeping the family jewelry. On a near-black `{colors.network-canvas}` canvas, a `{colors.night-navy}` utility strip and royal `{colors.indigo}` hero panels frame monochrome leadership portraiture; `{colors.gold}` rules and `{colors.amber}` active links carry the network's gilded eagle identity; and vivid vertical rails in `{colors.rail-teal}` and `{colors.rail-red}` label whole sections from the margin. It reads as the broadcast brand's title-card language applied to the web.

**Key Characteristics:**
- Flat white paper with zero elevation — `{colors.hairline}` rules and whitespace do all the separating on news surfaces
- One-color signature: `{colors.primary}` appears only as the logo block and the 8px eyebrow bar before `{typography.section-eyebrow}` labels
- A dedicated live-news color system — `{colors.live-red}` badges, bands, and timeline dots connected by a `{colors.silver}` rail
- Compact black pill controls (`{rounded.lg}`) and a `{rounded.xl}` capsule input; media thumbnails round at `{rounded.md}` while article imagery stays square
- Roboto-only hierarchy spanning 300-weight uppercase eyebrows to 900-weight LIVE and Trending labels
- The network sub-surface: `{colors.network-canvas}` dark canvas, `{colors.indigo}` hero panels, `{colors.gold}`/`{colors.amber}` gilding, and teal/crimson section rails
- Page rhythm runs white masthead → live strip → photo-dense grids → `{colors.soft}` newsletter card → white footer; network pages run navy strip → white nav → dark portrait canvas → black footer

## Colors

Source pages — the news front page, a live blog, and the network's leadership and awards pages — share one identity across two polarities.

### Brand & Accent
- **Jazeera Orange** (`{colors.primary}` — #fa9000): the masthead logo block and the section-eyebrow bar. Identity, never interaction.
- **Live Red** (`{colors.live-red}` — #c31833): breaking bands, LIVE badges, timeline dots, live labels. The color of "happening now" and nothing else.
- **Gold** (`{colors.gold}` — #dba200): the network's rule and control-border gilding.
- **Amber** (`{colors.amber}` — #ffa000): active nav links on network pages.
- **Select Gold** (`{colors.select-gold}` — #ffc500): the network's heavy 3px control border on filters.
- **Rail Teal** (`{colors.rail-teal}`) and **Rail Crimson** (`{colors.rail-red}`): the vertical section-label rails beside leadership grids — broadcast lower-third colors standing on the page margin.

### Surface
- **Paper** (`{colors.canvas}` — #ffffff): the news canvas, the nav, the footer.
- **Soft** (`{colors.soft}` — #f0f0f0): the newsletter card fill and the faintest divider tone.
- **Night Canvas** (`{colors.network-canvas}` — #181818): the network pages' dark ground for portrait cards.
- **Royal Indigo** (`{colors.indigo}` — #272967): the network hero panel behind page titles.
- **Night Navy** (`{colors.night-navy}` — #100e2f): the network's slim utility strip.
- **Hairline** (`{colors.hairline}` — #d8d8d8) and **Silver** (`{colors.silver}` — #bebebe): rule tones — list dividers, card edges, and the live-timeline rail. Both are decoration only: at 1.43:1 and 1.86:1 on `{colors.canvas}` neither reaches the 3:1 a component boundary needs.

### Prescribed Accessibility Tokens (not extracted)
The live site ships no focus ring and no boundary tone that clears 3:1. These four tokens are **prescribed**, not measured; the extracted hexes above are untouched.
- **Surface Soft** (`{colors.surface-soft}` — #f0f0f0): alias of `{colors.soft}`, named as the system's one raised fill. Ink on it measures 18.43:1.
- **Text Secondary** (`{colors.text-secondary}` — #595959): alias of `{colors.slate}`, the documented secondary-text tone. 7.00:1 on `{colors.canvas}`, 6.15:1 on `{colors.surface-soft}`.
- **Border Control** (`{colors.border-control}` — #595959): the boundary tone for anything whose edge must be seen — text inputs, selects, focusable rows. Same value the file already documents for the email capsule border, so no new hue enters the palette. 7.00:1 on `{colors.canvas}`.
- **Focus** (`{colors.focus}` — #000000) and **Focus On Dark** (`{colors.focus-on-dark}` — #ffc500, the extracted select-gold): the two-ring focus system. Black suits a page whose controls are already black objects; orange is kept off interaction per the marker-pen rule.

### Text
- **Ink** (`{colors.ink}`): headlines, standing labels, and the black pill fills.
- **Charcoal** (`{colors.charcoal}` — #333333): article body text.
- **Slate** (`{colors.slate}` — #595959): secondary text, eyebrow labels, the oversized Most Popular numerals, input borders, and the monochrome logo rendering.
- **Mist** (`{colors.mist}` — #dddddd): light text on the network's dark surfaces.
- **Graphite** (`{colors.graphite}` — #323232): network body text and rules on light bands.

### Semantic
- The only semantic signal is `{colors.live-red}` for live/breaking state. There are no success or warning colors — news chrome stays neutral.

### Brand Gradient
- None. Every brand surface is a flat fill; even the network's indigo panels and gold rules are solid.

## Typography

### Font Family
Roboto carries the entire system — news and corporate alike — from 300-weight uppercase eyebrows to 900-weight status labels. The only other face is the network's custom Al-Jazeera wordmark lettering, used solely as logo art. Body text on article pages sits on Roboto's neutral 400.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.headline-xl}` | 40px | 700 | 1.2 | 0 | Live-blog and article lead headlines |
| `{typography.headline-lg}` | 32px | 700 | 1.25 | 0 | Front-page top stories |
| `{typography.headline-md}` | 24px | 700 | 1.3 | 0 | Card headlines, newsletter title |
| `{typography.headline-sm}` | 18px | 700 | 1.35 | 0 | List headlines, Most Popular rows |
| `{typography.network-display}` | 36px | 700 | 1.2 | 0 | Network page titles and leader names |
| `{typography.section-eyebrow}` | 24px | 300 | 1.2 | 0 | Uppercase section labels behind the orange bar |
| `{typography.label-black}` | 14px | 900 | 1 | 0 | Trending, LIVE, and status labels |
| `{typography.body}` | 16px | 400 | 1.5 | 0 | Article and interface body |
| `{typography.body-sm}` | 14px | 400 | 1.45 | 0 | Metadata, nav links, footer columns |
| `{typography.caption}` | 12px | 400 | 1.4 | 0 | Timestamps, credits, fine print |
| `{typography.button}` | 16px | 400 | 1 | 0 | Pill labels |

### Principles
- Weight is the hierarchy: 700 for every headline tier, 300 for the airy uppercase eyebrows, 900 reserved for tiny urgent labels — a deliberately wide 300↔900 spread inside one family.
- Headlines are set tight and dense; the system tolerates — and embraces — crowded news grids.
- Timestamps and wire-style metadata sit in `{typography.caption}` `{colors.slate}`, always subordinate to the headline block.

### Note on Font Substitutes
Roboto is open source — use it directly. The Al-Jazeera wordmark lettering is proprietary logo art; do not approximate it with a text face.

## Layout

### Spacing System
- **Base unit**: 8px with tight 2/4px steps for chrome and metadata.
- **Tokens (front matter)**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 20px · `{spacing.xxl}` 24px · `{spacing.huge}` 30px
- News density keeps gaps small — `{spacing.sm}`-`{spacing.lg}` between cards; the newsletter card pads at `{spacing.xl}`; network sections breathe at `{spacing.xxl}`+.

### Grid & Container
- The front page runs a packed 1100px multi-column news grid: lead story + secondary column + rail, then full-width bands (video carousel, features, galleries).
- Live blogs run a single reading column with a right rail; updates stack as timestamped blocks.
- Network pages run full-bleed bands: hero panels, then 4-up portrait grids with the vertical rail occupying the left margin.

### Whitespace Philosophy
Whitespace is rationed like column inches. The design deliberately runs dense — separation comes from hairline rules, timestamps, and weight contrast rather than air. Only the network pages allow generous dark voids around portraiture.

### Responsive Strategy

#### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Desktop | 1280px | Full news grid with right rail |
| Laptop | 1024px | Rail folds under; grids step to 2-up |
| Tablet | 768-992px | Nav condenses; carousels show fewer cards |
| Mobile-lg | 600px | Single-column stacking; thumbnails shift beside headlines |
| Mobile | 480px and below | Full-width media; pills persist at compact size |

#### Touch Targets
The black pills pad 6px 17px around 16px labels — keep their surrounding row spacing so targets clear 44×44. Timeline items and Most Popular rows are full-width tap zones.

#### Collapsing Strategy
The nav collapses into a hamburger while the LIVE pill and logo block persist. News grids collapse column-by-column toward the single-column mobile feed; the live timeline keeps its dot rail at every width; network portrait grids step 4 → 2 → 1 with the section rails moving above the grid.

#### Image Behavior
News photography is aggressively cropped 16:9 and 4:3, square-cornered in article grids, `{rounded.md}` in video carousels and thumb rows. Network leadership portraits are consistent studio gray, displayed in tall cards with name overlays.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | None — rules only | The entire news surface |
| Rule | 1px `{colors.hairline}` / `{colors.soft}` dividers; 1px `{colors.ink}` bottom rules | Lists, cards, section boundaries |
| Dropdown | `{shadow.dropdown}` — 0 6px 12px rgba(0, 0, 0, 0.175) | Network menus — the system's only shadow |

Shadow philosophy: news reads flat. Photography supplies all depth on the editorial side; the network's dark canvas supplies it on the corporate side. The single dropdown shadow exists for usability, not style.

### Decorative Depth
- **Photo scrims**: leadership portrait cards fade to dark at the base so white names hold contrast.
- **Section rails**: the teal and crimson vertical bars read like broadcast side-straps, giving flat pages a stage-set depth.
- **Polarity shift**: the jump from white news paper to `{colors.network-canvas}` corporate darkness is itself the system's depth move.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | LIVE badges, network buttons |
| `{rounded.sm}` | 4px | Tooltips, small tags |
| `{rounded.md}` | 10px | Video-carousel cards, thumbnail images |
| `{rounded.lg}` | 18px | The black pill buttons |
| `{rounded.xl}` | 22px | The email capsule input |
| `{rounded.full}` | 9999px | Mini count pills, circular icon buttons, avatars |

The scale is bimodal: editorial imagery and badges stay near-square (2-10px) while every control is a capsule (18-22px, full circles for icons) — buttons announce themselves by shape alone on a flat page.

### Photography Geometry
- Article grids: square-cornered 16:9 and 4:3 crops, packed edge to edge.
- Video carousel: portrait cards at `{rounded.md}`.
- Thumb rows: small 130×87 stills at `{rounded.md}` beside `{typography.headline-sm}` links.
- Opinion: circular `{rounded.full}` author avatars.
- Network: tall portrait cards with base scrims, square-cornered.

## Components

### Buttons

**`button-pill-dark`** — Sign up, Subscribe, the LIVE masthead control
- Fill `{colors.ink}`, label `{colors.on-primary}` at `{typography.button}`, rounded `{rounded.lg}`, padding 6px 17px. The standing action shape across the news surface.

**`button-pill-mini`**
- The tiny `{colors.ink}` counter pill at `{rounded.full}`, padding 1px 6px — photo-count overlays and compact toggles.

### Cards & Containers

**`news-card`**
- Square photography above or beside an `{typography.headline-md}`/`{typography.headline-sm}` ink headline with `{typography.caption}` metadata; no fill, no border — position and weight define it.

**`media-thumb`**
- The `{rounded.md}` still used in video carousels and thumb-link rows.

**`newsletter-card`**
- `{colors.soft}` panel, `{typography.headline-md}` title, supporting `{typography.body-sm}`, containing `text-input` and a `button-pill-dark`, padded `{spacing.xl}`.

**`most-popular-row`** + **`popular-numeral`**
- Ranked list rows divided by `{colors.hairline}` with an oversized `{colors.slate}` numeral at `{typography.headline-lg}` beside an `{typography.headline-sm}` headline.

**`award-card`**
- Network awards grid cell: square news photo, `{typography.headline-sm}` title, `{typography.caption}` date, `{colors.graphite}` summary.

**`leader-card`** + **`leader-band`**
- Portrait cards on `{colors.network-canvas}` with base scrims and `{colors.on-primary}` name/role text; senior leaders get full-width gray studio bands with `{typography.network-display}` names over a short white rule.

### Inputs & Forms

**`text-input`** — the email capsule
- `{colors.canvas}` fill, 1px `{colors.slate}` border, rounded `{rounded.xl}`, padding 0px 15px, `{typography.body}` text.

**`network-select`**
- The network filter control: `{colors.canvas}` fill with a heavy 3px `{colors.select-gold}` border — the system's loudest control edge.

### Navigation

**`nav-bar`** — Top Nav (Desktop, news)
- White strip: `logo-block` left (the `{colors.primary}` square with the white eagle), black `{typography.body}` links with caret dropdowns, then the LIVE pill, search, and Sign up pill right. A Trending strip runs beneath with a `{typography.label-black}` label and topic links.

**`network-utility-strip`** + **`network-nav`** + **`network-nav-active`**
- The corporate header stacks a `{colors.night-navy}` utility strip (language + social) over a white caps-link nav where the active item switches to `{colors.amber}`; the gold eagle mark sits left.

**Top Nav (Mobile)**
- News nav collapses to hamburger + logo block + LIVE pill.

**`footer`** / **`network-footer`**
- News footer: white, hairline-topped link columns with the eagle mark. Network footer: `{colors.ink}` black with `{colors.mist}` links and the gold network lockup.

### Signature Components

**`section-eyebrow-lockup`**
- The system's signature: an 8px-wide `{colors.primary}` bar flush against an uppercase `{typography.section-eyebrow}` label in `{colors.slate}`. Every editorial section opens with it.

**`live-badge`** + **`breaking-band`** + **`live-strip-item`**
- The live apparatus: a `{typography.label-black}` LIVE UPDATES label in `{colors.live-red}` (badged at `{rounded.xs}`); a full-width `{colors.live-red}` breaking band with `{colors.on-primary}` headline text; and the minute-by-minute strip — `{colors.live-red}` dots on a `{colors.silver}` rail beside timestamped `{typography.body-sm}` items.

**`section-rail-teal`** / **`section-rail-red`**
- Network section rails: full-height vertical bars in `{colors.rail-teal}` and `{colors.rail-red}` carrying rotated white uppercase labels beside portrait grids.

**`network-hero-panel`**
- The `{colors.indigo}` title panel opening network pages: `{typography.network-display}` white heading over `{typography.body-sm}` copy, set beside full-bleed photography.

**`logo-block`**
- The masthead identity: a solid `{colors.primary}` square carrying the white eagle calligraphy mark beside the wordmark. The single largest orange surface in the system.

**`avatar-circle`**
- Circular `{rounded.full}` author portraits in Opinion lists.

### Examples (illustrative)

> Kit-mirror demonstration surfaces. Each `ex-*` entry references brand-native primitives via token syntax so downstream consumers re-skin the same 10 surfaces consistently — these are illustrative compositions stamped with this brand's tokens, not components extracted from the site.

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

### State Coverage

The live pages expose no hover, pressed or disabled styling that could be read off a static capture, so every state below except `default` and the network nav's `active` is **prescribed**. The rule throughout: state is carried by opacity, the `{colors.focus}` ring and the `{colors.border-control}` edge — never by recoloring a surface orange.

| Component | States |
|---|---|
| `button-pill-dark` | default · hover (fill holds, label to 85% opacity) · focus-visible (2px `{colors.focus-on-dark}` ring inset 2px, since the fill is ink) · pressed · disabled (40% opacity, `{colors.silver}` fill) · loading (label swaps for a 3-dot pulse, width frozen) |
| `button-pill-mini` | default · hover · focus-visible (`{colors.focus-on-dark}`) · pressed · disabled. No loading or selected state — it is a counter, not a control, in most placements |
| `nav-bar` link | default · hover (1px `{colors.ink}` underline) · focus-visible (`{colors.focus}`) · pressed · selected (current section, 700 weight) |
| `network-nav` / `network-nav-active` | default · hover (`{colors.amber}`) · focus-visible (`{colors.focus}`) · active/selected (`{colors.amber}`, the one state the live pages actually show) |
| `text-input` | default (1px `{colors.border-control}`) · hover · focus-visible (2px `{colors.focus}` ring, border to `{colors.ink}`) · disabled (`{colors.surface-soft}` fill, `{colors.silver}` border) · error (1px `{colors.live-red}` border plus a `{typography.caption}` message in `{colors.live-red}`) · loading (submit pill carries the spinner, field stays live) |
| `network-select` | default (3px `{colors.select-gold}`) · hover · focus-visible (`{colors.focus}` ring outside the gold edge) · selected (chosen option, 700 weight) · disabled · error |
| `news-card` / `media-thumb` | default · hover (headline underline, image to 92% opacity — no scale, no shadow) · focus-visible (`{colors.focus}` ring around the whole card) · pressed |
| `most-popular-row` / `live-strip-item` | default · hover (headline underline) · focus-visible (`{colors.focus}`) · pressed · selected (the update currently anchored in a live blog) |
| `live-badge` / `breaking-band` | default and loading only — they are status surfaces, not controls. Loading is the dot pulse on the timeline rail |
| `newsletter-card` | default · error (field-level, see `text-input`) · loading (pill spinner). Not hoverable, not focusable, not selectable as a whole |
| `ex-toast` | enter · default · hover (pauses auto-dismiss) · focus-visible (`{colors.focus}`) · error variant (`{colors.live-red}` 3px left rule) · exit |
| `ex-data-table-cell` | default · hover (row to `{colors.surface-soft}`) · focus-visible · selected (row, 1px `{colors.ink}` left rule) · loading (skeleton rows) |
| `avatar-circle` / `logo-block` / `section-rail-teal` / `section-rail-red` / `network-hero-panel` | default only — static identity and label surfaces with genuinely one state |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** Nobody timed Al Jazeera's real transitions; every value below is an inference from the static design language, carried by the `{motion}` tokens in the frontmatter.

Profile: **Calm** — composed and editorial. It is the right read for this file: the identity is flat white paper with no shadows and no gradients, headline weight does the work, and the section-eyebrow bar is a printed mark rather than an interactive flourish. A news front page that popped and sprang on every hover would undercut the wire-service voice. Motion here is almost entirely opacity, with travel measured in single-digit pixels; the one exception is the live apparatus, where a slow pulse is the brand's only sanctioned ambience.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pills, cards, list rows) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` | Opacity change kept at `{motion.duration-fast}`; underline appears instantly |
| Press (pills, rows) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` (to 0.9) | Opacity only, `{motion.duration-instant}` — no scale at any time, in either mode |
| Focus (`{colors.focus}` / `{colors.focus-on-dark}` ring) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring is drawn with no transition; it must never lag the keyboard |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` | Cross-fade dropped to `{motion.duration-fast}`, no travel |
| Modal / drawer (nav drawer, network menu) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px)` | Travel removed; `{motion.duration-fast}` opacity fade only |
| Dropdown (nav carets, network select) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(4px)` | Travel removed; opacity fade at `{motion.duration-fast}` |
| Toast | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px)` | Travel removed; appears and leaves on a `{motion.duration-fast}` fade |
| List enter (news grid, live updates) | `{motion.duration-base}`, `{motion.stagger-step}` between items, 6 items maximum | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px)` | Stagger and travel removed; items appear at full opacity with no transition |
| List exit (filtered grids, dismissed updates) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | Removed without transition |
| Loading (pill spinner, live timeline dot, skeleton rows) | `{motion.duration-emphasis}` per cycle, infinite | `{motion.ease-standard}` | `opacity` (1 → 0.4 → 1) | Pulse frozen at full opacity; a static "Loading…" / "LIVE" label carries the state instead |

### Rules
- Only `opacity` and `transform` are ever transitioned. Never `width`, `height`, `top`, `left` or `margin` — a dense news grid cannot afford layout thrash, and nothing in this identity moves far enough to need them.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint. The masthead, the live strip and the lead story render at full opacity; the staggered list enter applies to content fetched after load, never to the initial page.
- The only infinite animation is the live-apparatus pulse — the `{colors.live-red}` timeline dot and the LIVE badge breathing at `{motion.duration-emphasis}` — and the loading indicators. That pulse is deliberate brand ambience: it is the one place the system says "happening now" without words.
- No scale on press, and no entrance choreography on the eyebrow bars. The `{colors.primary}` bar is printed, not performed.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translateY travel, all stagger, the live-dot and
     skeleton pulse (frozen at full opacity). */
  /* Kept: opacity fades, capped at 150ms. */
  *, *::before, *::after {
    transition-duration: 150ms !important;
    transition-property: opacity !important;
    animation: none !important;
  }
}
```

Removed: every `transform` travel, the `{motion.stagger-step}` cascade, and the infinite live/loading pulse. Kept: opacity fades at `{motion.duration-fast}` or less, the focus ring (untransitioned), and every text label that carries live or loading state — so no information is lost when motion is off.

## Accessibility

Measured with WCAG 2.1 relative luminance against the hexes in this file's own frontmatter. Nothing here is from a rendered page: tap-target size, overlap and clipping cannot be verified from a document, so they are stated as intent, not measurement.

### Contrast — measured
| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 21.00:1 | 4.5 | Pass |
| `{colors.charcoal}` on `{colors.canvas}` | 12.63:1 | 4.5 | Pass |
| `{colors.text-secondary}` on `{colors.canvas}` | 7.00:1 | 4.5 | Pass |
| `{colors.text-secondary}` on `{colors.surface-soft}` | 6.15:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.surface-soft}` | 18.43:1 | 4.5 | Pass |
| `{colors.border-control}` on `{colors.canvas}` | 7.00:1 | 3.0 | Pass |
| `{colors.hairline}` on `{colors.canvas}` | 1.43:1 | 3.0 | **Fail — decorative only** |
| `{colors.silver}` on `{colors.canvas}` | 1.86:1 | 3.0 | **Fail — decorative only** |
| `{colors.on-primary}` on `{colors.primary}` | 2.32:1 | 4.5 | **Fail — real brand failure** |
| `{colors.on-primary}` on `{colors.live-red}` | 6.00:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.rail-red}` | 6.69:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.rail-teal}` | 2.02:1 | 4.5 | **Fail — real brand failure** |
| `{colors.on-primary}` on `{colors.indigo}` | 13.13:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.network-canvas}` | 17.76:1 | 4.5 | Pass |
| `{colors.mist}` on `{colors.network-canvas}` | 13.07:1 | 4.5 | Pass |
| `{colors.mist}` on `{colors.ink}` | 15.46:1 | 4.5 | Pass |
| `{colors.amber}` on `{colors.canvas}` | 2.04:1 | 4.5 | **Fail — real brand failure (active nav link)** |
| `{colors.gold}` on `{colors.canvas}` | 2.29:1 | 4.5 | **Fail — decorative rules only** |
| `{colors.select-gold}` on `{colors.canvas}` | 1.59:1 | 3.0 | **Fail — real brand failure (control border)** |

Said plainly: **this brand fails AA in four places, and the document does not hide it.**
1. White on Jazeera orange is 2.32:1. The `{colors.primary}` surface is safe as the logo block, where the eagle is a trademark mark rather than text; it must not carry label text. Anything that reads as text on orange needs `{colors.ink}` instead (9.05:1).
2. White on `{colors.rail-teal}` is 2.02:1. The rotated rail labels are large display type, so 3:1 is the applicable threshold — and at 2.02:1 they miss even that. `{colors.ink}` on teal measures 10.40:1 and is the only accessible fix. `{colors.rail-red}` has no such problem.
3. `{colors.amber}` active nav links on white are 2.04:1. On the dark network grounds amber is fine; on the white nav band it is not.
4. The 3px `{colors.select-gold}` select border is 1.59:1 — the system's loudest edge is also its least visible. Pair it with the `{colors.border-control}` inner edge.

The two hairline tones stay frozen at 1.43:1 and 1.86:1 because they are extracted facts. They are scoped to decoration — list dividers, the live-timeline rail, card edges that sit beside other cues. `{colors.border-control}` is the token for any boundary that is the *only* cue, such as a text input.

### Focus ring
Two rings, because one cannot cross this system's polarity shift:
- `{colors.focus}` (#000000), 2px with a 2px offset, on every light surface and on the teal and amber chrome: 21.00:1 on `{colors.canvas}`, 18.43:1 on `{colors.surface-soft}`, 14.73:1 on a `{colors.hairline}` rule, 9.05:1 on `{colors.primary}`, 10.40:1 on `{colors.rail-teal}`.
- `{colors.focus-on-dark}` (#ffc500), 2px inset, on the ink pills and the network's dark grounds: 13.24:1 on `{colors.ink}`, 11.19:1 on `{colors.network-canvas}`, 11.76:1 on `{colors.night-navy}`, 8.28:1 on `{colors.indigo}`, 4.22:1 on `{colors.rail-red}`.
- Neither ring is ever drawn on `{colors.rail-teal}` in gold (1.27:1) — teal takes the black ring.
- The ring is never suppressed. `:focus-visible` only, so pointer users never see it, and it is drawn with no transition.

### Layers
`{colors.canvas}` to `{colors.surface-soft}` is 1.14:1 — the newsletter card is barely a layer at all. That is true to the brand, but it means the card must keep its `{spacing.xl}` padding and its own type hierarchy to read as a panel; it cannot rely on the fill alone, and it must not be given a `{colors.hairline}` edge, which at 1.43:1 would add nothing.

### Tap targets
Intent, not measurement — no rendered page exists to verify. The `button-pill-dark` pads 6px 17px around a 16px label, which computes to roughly 36px tall: short of 44×44, so its surrounding row spacing must carry the remainder. `button-pill-mini` at 1px 6px padding around 12px type cannot be a primary tap target and is documented as a counter. Timeline items and Most Popular rows are full-width tap zones.

### Reduced motion
See `@media (prefers-reduced-motion: reduce)` above. Every live and loading state has a text label, so freezing the pulse removes no information.

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
| `{colors.hairline}` (`#d8d8d8`) on `{colors.soft}` (`#f0f0f0`) | 1.25:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.silver}` (`#bebebe`) on `{colors.soft}` (`#f0f0f0`) | 1.63:1 | 3.0:1 | Fail — bound boundary |
| `components.logo-block` — its own `textColor` (`#ffffff`) on its own `backgroundColor` (`#fa9000`) | 2.32:1 | 4.5:1 | Fail — both tones are bound in this file |
| `components.network-nav-active` — its `textColor` (`#ffa000`) on the page floor (`#ffffff`) | 2.04:1 | 4.5:1 | Fail — no `backgroundColor` declared; page floor substituted as the ground |
| `components.leader-band` — its `textColor` (`#ffffff`) on the page floor (`#ffffff`) | 1.00:1 | 3.0:1 | Fail — no `backgroundColor` declared; page floor substituted as the ground |
| `components.section-rail-teal` — its own `textColor` (`#ffffff`) on its own `backgroundColor` (`#00cbca`) | 2.02:1 | 4.5:1 | Fail — both tones are bound in this file |

## Do's and Don'ts

### Do
- Keep `{colors.primary}` to identity duty — the logo block and the eyebrow bar — and let black pills carry every action.
- Reserve `{colors.live-red}` strictly for live/breaking state: badges, bands, timeline dots.
- Open every editorial section with the `section-eyebrow-lockup` (orange bar + 300-weight uppercase label).
- Keep the news surface flat: hairline rules and weight contrast, never shadows or tonal cards.
- Run photography dense and square in article grids; save `{rounded.md}` for carousels and thumbs.
- On network pages, keep the gilded family — `{colors.gold}` rules, `{colors.amber}` active links — over the dark `{colors.network-canvas}`.
- Use the wide Roboto weight spread deliberately: 300 eyebrows, 700 headlines, 900 urgent labels.

### Don't
- Don't fill buttons or links with `{colors.primary}` — orange interaction chrome breaks the marker-pen rule.
- Don't use `{colors.live-red}` decoratively; if it isn't live coverage, it isn't red.
- Don't add shadows, gradients, or card fills to news grids — density and rules are the aesthetic.
- Don't round article photography; square crops are part of the wire-service voice.
- Don't mix the network's gold/amber/indigo family into the news surface, or the orange eyebrow system into corporate pages.
- Don't soften the eyebrows — they stay uppercase, light-weight, and barred.
- Don't introduce new accent hues; the palette's color budget is spent on orange, live-red, and the network's gold and rails.
- Don't animate `width`, `height`, `top`, `left` or `margin`; opacity and `transform` carry every transition.
- Don't put label text on the `{colors.primary}` block or white text on `{colors.rail-teal}` — both fail contrast (2.32:1 and 2.02:1).
- Don't suppress the focus ring to protect the flat look; use `{colors.focus}` on light surfaces and `{colors.focus-on-dark}` on the ink pills and dark network grounds.

## Responsive Behavior

The breakpoint table, collapsing strategy, touch-target note and image behaviour live under **Layout → Responsive Strategy** above; this section adds only what belongs to state and motion at each width.

| Width | Behaviour |
|---|---|
| Desktop 1280px | Full news grid with right rail. List enter staggers at `{motion.stagger-step}`, capped at 6 items |
| Laptop 1024px | Rail folds under the main column; grids step to 2-up. Stagger unchanged |
| Tablet 768–992px | Nav condenses; carousels show fewer cards. Dropdowns still use `{motion.duration-fast}` |
| Mobile-lg 600px | Single-column stacking; thumbnails move beside headlines. Stagger drops to the first 3 items |
| Mobile ≤480px | Full-width media; pills persist at compact size. The nav drawer replaces the dropdown and uses the modal timing (`{motion.duration-base}` in, `{motion.duration-fast}` out) |

- Hover states have no touch equivalent: on pointer-coarse widths the hover opacity shift is dropped and the pressed state at `{motion.duration-instant}` is the only feedback.
- The `{colors.focus}` ring is unchanged at every width; it never shrinks to fit a compact pill.
- The live-timeline dot rail and its pulse persist at every width, as does the `{colors.primary}` logo block.
- Prescribed, not measured: these are the natural consequences of the breakpoints and motion tokens this file already states, not observed mobile behaviour.

## Known Gaps

Everything in this list is either unverifiable from a static document or absent from the live site. Nothing here is invented as fact.

- **Motion is entirely prescribed.** No duration, easing or stagger in this file was measured. The Calm profile was chosen from the visual identity (flat paper, no shadows, no gradients, weight-led hierarchy), not from a recording.
- **Nearly all states are prescribed.** Only `default` and the network nav's `active` are observable from static pages. Hover, focus-visible, pressed, disabled, loading, selected and error styling is inferred and marked as such in State Coverage.
- **No focus ring exists on the live site.** `{colors.focus}` and `{colors.focus-on-dark}` are additions, not extractions.
- **`{colors.border-control}`, `{colors.text-secondary}` and `{colors.surface-soft}` are aliases**, named so the token contract has a boundary, secondary-text and surface role. Their values are the already-extracted `{colors.slate}` and `{colors.soft}`; no new hue was introduced.
- **Not computable from a document:** tap-target size, overlap, horizontal overflow, clipping, frame rate and layout shift. The 44×44 note under Accessibility is intent.
- **Unknown type details:** no letter-spacing is stated anywhere (all tokens carry 0, which is a default rather than a measurement), and the network wordmark's own metrics are unrecorded because it is logo art.
- **Unknown colour duties:** `{colors.graphite}` and `{colors.mist}` are documented only as network body and link tones; whether they also serve as rules on light bands is not confirmed.
- **No dark mode.** The `{colors.network-canvas}` pages are a separate corporate surface, not a theme of the news pages, and no dark variant of the news front page was observed.
- **Elevation is single-shadow.** `{shadow.dropdown}` is the only real shadow in the system; no hover or modal elevation value exists, so none was invented.
- **Error and success semantics are thin.** The file documents `{colors.live-red}` as the only semantic signal; the error states in State Coverage borrow it, and no success or warning tone exists to borrow.
