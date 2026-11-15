---
version: alpha
name: mydealz Analysis
description: An analysis of mydealz's design language — a high-density German deals-community system built on a confident brand green, where a stacked white-card feed carries thousands of deals and every card wears the signature hot/cold temperature control that turns pricing into a crowd vote. Fully-round 540px pill buttons, Averta CY at two weights, cool-gray page canvas, and a compact red/blue/orange status vocabulary keep the information-dense feed scannable and playful at once.

colors:
  primary: "#30a83c"
  on-primary: "#ffffff"
  green-strong: "#197e25"
  discount-surface: "#defde4"
  hot: "#ce1736"
  cold: "#034eb1"
  warm: "#fb6001"
  premium: "#7457dd"
  canvas: "#f3f5f7"
  surface: "#ffffff"
  ink: "#000000"
  body: "#6b6d70"
  muted: "#a7a9ac"
  hairline: "#dfe1e4"
  hairline-strong: "#8a8d91"
  focus: "#197e25"
  warning-surface: "#faf9ca"
  warning-text: "#9f5c0c"

typography:
  display:
    fontFamily: Averta CY
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  heading-lg:
    fontFamily: Averta CY
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  heading:
    fontFamily: Averta CY
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  lead:
    fontFamily: Averta CY
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body:
    fontFamily: Averta CY
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  ui:
    fontFamily: Averta CY
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  caption:
    fontFamily: Averta CY
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  micro:
    fontFamily: Averta CY
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  mono:
    fontFamily: monospace
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 2px
  sm: 4px
  md: 8px
  full: 540px
  circle: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 40px

shadow:
  soft: "rgba(11,22,44,0.09) 0 4px 12px"
  deep: "rgba(0,0,0,0.38) -1px 11px 15px -11px"

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

components:
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    borderColor: "{colors.hairline}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.ui}"
    rounded: "{rounded.full}"
    padding: "0px 14px"
  button-outline-green:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.ui}"
    rounded: "{rounded.full}"
    padding: "0px 14px"
    borderColor: "{colors.primary}"
  button-outline-neutral:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.full}"
    padding: "0px 12px"
    borderColor: "{colors.hairline}"
  button-muted:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.ui}"
    rounded: "{rounded.full}"
    padding: "0px 14px"
    borderColor: "{colors.hairline}"
  button-tag:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0px 4px"
  search-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline-strong}"
    focusRing: "{colors.focus}"
  deal-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "16px"
  temperature-control:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.hot}"
    typography: "{typography.ui}"
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline}"
  temperature-up:
    textColor: "{colors.hot}"
    typography: "{typography.ui}"
  temperature-down:
    textColor: "{colors.cold}"
    typography: "{typography.ui}"
  price-lockup:
    textColor: "{colors.primary}"
    typography: "{typography.heading-lg}"
  discount-badge:
    backgroundColor: "{colors.discount-surface}"
    textColor: "{colors.green-strong}"
    typography: "{typography.ui}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-neutral-subtle:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0px 4px"
  badge-filled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    borderColor: "{colors.surface}"
  premium-badge:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.premium}"
    typography: "{typography.ui}"
    rounded: "{rounded.sm}"
  warning-badge:
    backgroundColor: "{colors.warning-surface}"
    textColor: "{colors.warning-text}"
    typography: "{typography.ui}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  text-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.full}"
    padding: "9px 35px"
    borderColor: "{colors.hairline-strong}"
    focusRing: "{colors.focus}"
  email-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "9px 16px"
    borderColor: "{colors.hairline-strong}"
    focusRing: "{colors.focus}"
  timestamp-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
  sidebar-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "16px"
  avatar:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.circle}"
    borderColor: "{colors.surface}"
  country-selector:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    borderColor: "{colors.hairline-strong}"
    focusRing: "{colors.focus}"
  footer:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"

  # ─── Examples (illustrative) — kit-mirror surfaces ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.surface}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body}"
    cellPadding: "{spacing.sm} {spacing.md}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    captionTypography: "{typography.body}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body}"

---


## Overview

mydealz is a deals-community feed running at maximum density: a single cool-gray canvas (`{colors.canvas}`) stacked with hundreds of white deal cards (`{colors.surface}`), each one a compact bundle of thumbnail, title, price, and social signals. The design's whole job is to make that firehose scannable, and it does it with one confident brand green (`{colors.primary}`) — the color of every price, every "Zum Deal" pill, every submit action — plus a tight status vocabulary that keeps the eye moving.

The signature move is the **temperature control**: every deal carries a pill showing a cold-blue down-arrow (`{colors.cold}`), the deal's crowd-voted temperature in hot-red (`{colors.hot}`), and a hot-red up-arrow — pricing turned into a live vote. That red/blue pairing, extended by a warm orange (`{colors.warm}`) for rising deals and a premium violet (`{colors.premium}`) for highlighted content, is the brand's playful counterweight to an otherwise businesslike grid. Discount percentages sit in soft mint pills (`{colors.discount-surface}`), so a card reads at a glance: green price, red-hot temperature, mint saving.

Geometrically the system is defined by the **fully-round 540px pill** — buttons, the search field, the temperature control, filter chips all curve to a complete radius, while content cards settle at a friendly 8px. Averta CY carries everything at just two weights (medium 500, bold 700), keeping headlines punchy and the dense body legible. Depth is minimal: cards separate with a hairline (`{colors.hairline}`) and lift on the softest shadow only when they matter.

**Key Characteristics:**
- One brand green (`{colors.primary}`) owns every action and every price — the single unifying signal across a chaotic feed
- Signature hot/cold **temperature control**: `{colors.cold}` down-vote, `{colors.hot}` up-vote and temperature reading, on every deal card
- Fully-round `{rounded.full}` (540px) pills for buttons, search, chips, and the temperature control; 8px cards
- Mint discount pills (`{colors.discount-surface}`) pairing green savings against the red-hot temperature
- Averta CY at two weights (500/700) driving a punchy, high-density type system
- Cool-gray canvas (`{colors.canvas}`) behind stacked white cards (`{colors.surface}`) — a scannable card feed, not a marketing page
- A compact accent set — `{colors.warm}` orange for rising, `{colors.premium}` violet for highlighted — kept strictly functional

## Colors

### Brand & Accent
- **Deal Green** (`{colors.primary}` — #30a83c): The brand's core. Fills every primary CTA pill, every deal price, submit actions, active links, and highlighted stats. On-color content is `{colors.on-primary}`.
- **Strong Green** (`{colors.green-strong}`): A darker green for green text on light surfaces (discount-badge label, outline-button glyphs) where the fill green would be too light.
- **Hot Red** (`{colors.hot}`): The temperature "hot" signal — the deal's degree reading and the up-vote arrow. The brand's excitement color.
- **Cold Blue** (`{colors.cold}`): The temperature "cold" signal — the down-vote arrow. Always paired against `{colors.hot}` in the temperature control.
- **Rising Orange** (`{colors.warm}`): A warm accent for rising/trending deals, sitting between cold and hot on the temperature spectrum.
- **Premium Violet** (`{colors.premium}`): Highlight accent for premium / featured content markers.
- **Discount Mint** (`{colors.discount-surface}`): The soft green pill behind a saving percentage.

### Surface
- **Canvas** (`{colors.canvas}`): The cool light-gray page ground that stacked white cards sit on.
- **Surface** (`{colors.surface}`): Pure white — every card, the nav, the footer, buttons.
- **Hairline** (`{colors.hairline}`): The extracted 1px border on cards, buttons, and dividers. It measures 1.2:1 on `{colors.canvas}` and 1.31:1 on `{colors.surface}` — far below the 3:1 a boundary needs. Treat it as **decoration only**: the card-to-card separation it provides is reinforced by the canvas gutter, not carried by the line alone.
- **Hairline Strong** (`{colors.hairline-strong}` — *prescribed, not extracted*): The accessible parallel to `{colors.hairline}`, for any boundary that is the *only* thing defining a control — the edge of a `text-input`, `email-input`, `search-pill` or `country-selector`. 3.05:1 on `{colors.canvas}`, 3.33:1 on `{colors.surface}`.
- **Focus Ring** (`{colors.focus}` — *prescribed, not extracted*): mydealz publishes no focus ring, so this one is specified here. It takes the brand's own deep green value (the same hex as `{colors.green-strong}`), given its own role name because it is drawn as a 2px ring with a 2px offset outside the control, never as a fill. One mid-luminance ring serves every ground this file defines: 4.74:1 on `{colors.canvas}`, 5.18:1 on `{colors.surface}`, 4.05:1 on the black `ex-pricing-tier-featured` fill — so no `focus-on-dark` counterpart is needed.

### Text
- **Ink** (`{colors.ink}`): True black for deal titles, headings, and primary text.
- **Body** (`{colors.body}`): Mid gray for secondary copy, metadata, muted button labels.
- **Muted** (`{colors.muted}`): Light gray for the struck-through original price and placeholder text. At 2.16:1 on `{colors.canvas}` and 2.36:1 on `{colors.surface}` it fails AA for text; the real brand uses it anyway. Scope it to **decorative or redundant** ink only — a struck-through price whose live price is stated beside it, a placeholder whose field carries a visible label. Any secondary copy that must be read uses `{colors.body}` (4.75:1 / 5.19:1).

### Semantic
- **Warning Surface / Text** (`{colors.warning-surface}` / `{colors.warning-text}`): The soft-yellow pill and amber-brown text used for expiring / caution deal states.

## Typography

### Font Family

**Averta CY** — a humanist geometric sans — carries the entire system at two weights: medium (500) for body and lead copy, bold (700) for headings, UI labels, prices, and micro-labels. A **monospace** face appears in rare technical contexts (voucher codes). There is no light or black weight; the two-weight discipline keeps the dense feed consistent.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display}` | 48px | 700 | 1.1 | 0 | Page hero headline |
| `{typography.heading-lg}` | 24px | 700 | 1.2 | 0 | Section titles, deal price |
| `{typography.heading}` | 20px | 700 | 1.25 | 0 | Card / block headings |
| `{typography.lead}` | 18px | 500 | 1.4 | 0 | Lead paragraphs, prominent links |
| `{typography.body}` | 16px | 500 | 1.5 | 0 | Body copy, deal descriptions |
| `{typography.ui}` | 14px | 700 | 1.3 | 0 | Button labels, temperature, badges |
| `{typography.caption}` | 12px | 500 | 1.3 | 0 | Metadata, timestamps |
| `{typography.micro}` | 10px | 700 | 1.2 | 0 | Micro-labels, counts |
| `{typography.mono}` | 16px | 500 | 1.4 | 0 | Voucher codes |

### Principles
- Two weights only — 500 for reading, 700 for everything that signals or acts.
- Prices and temperatures are always bold; they're the two numbers that matter most on a card.
- The dense feed leans on size and weight, never on color, for text hierarchy (color is reserved for status).

### Note on Font Substitutes
Averta CY is a commercial face. For open-source builds, **Mulish** or **Nunito Sans** (500/700) reproduce the humanist-geometric warmth with near-identical metrics; keep the two-weight split. Any system monospace substitutes for the voucher-code face.

## Layout

### Spacing System
- **Base unit**: 8px
- **Tokens (front matter)**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 40px
- Cards pad `{spacing.lg}`; card rows stack with `{spacing.sm}`–`{spacing.md}` gaps for maximum density.

### Grid & Container
A two-column shell above ~768px: the main deal feed (single stacked column of full-width cards) plus a right sidebar of coupon, news, and discussion cards. Below the breakpoint the sidebar drops and the feed goes full-width. The container is wide and content-dense rather than a narrow reading column.

### Whitespace Philosophy
Whitespace is rationed — this is an information product, not a marketing page. Cards sit close together with tight internal padding; the cool-gray canvas gutters between white cards do the separating work, and the hairline borders keep each card crisp against its neighbors.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat on `{colors.canvas}` | Page ground, footer |
| 1 | 1px `{colors.hairline}` border | Deal cards, sidebar cards, buttons, inputs |
| 2 | Soft shadow `{shadow.soft}` (`rgba(11,22,44,0.09) 0 4px 12px`) | Elevated / hovered cards, dropdowns |
| 3 | Deeper drop `{shadow.deep}` (`rgba(0,0,0,0.38) -1px 11px 15px -11px`) | Overlays, sticky bars |

Depth is hairline-first. Cards separate by border and canvas gutter; the soft 4–12px shadow is reserved for elements that lift (menus, sticky bars, elevated cards). There are no heavy shadow stacks in the resting feed.

### Decorative Depth
The brand's playfulness lives in illustration, not gradients — a green cartoon frog mascot and companion characters appear in the consent and empty-state surfaces. The palette itself is flat; there are no brand gradients.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | Tightest inline chips |
| `{rounded.sm}` | 4px | Discount / filled badges, small tags |
| `{rounded.md}` | 8px | Deal cards, sidebar cards, thumbnails, tag buttons |
| `{rounded.full}` | 540px | Buttons, search pill, temperature control, filter chips — the pill signature |
| `{rounded.circle}` | 9999px | Avatars, icon buttons |

### Focus Ring
*Prescribed — mydealz publishes no focus-ring geometry.*

| Property | Value |
|---|---|
| Color | `{colors.focus}` |
| Width | 2px |
| Offset | 2px, drawn **outside** the control so it is judged against the surface behind it, per WCAG 2.2 Focus Appearance |
| Radius | Follows the control: `{rounded.full}` on pills, search and the temperature control; `{rounded.md}` on cards and `email-input`; `{rounded.circle}` on avatars and icon buttons |

The ring never replaces a border and never fills; it sits proud of the control's own edge so a green ring on a green `button-primary` stays legible against the white or cool-gray ground, not against the fill.

### Photography Geometry
Deal thumbnails sit in `{rounded.md}` frames on the card's media column; author and community avatars are circles (`{rounded.circle}`). There is no hero photography — the product IS the card grid.

## Components

### State Coverage

Which states each entry supports. Hover and pressed feedback is *prescribed* (see Motion & Animation); the resting appearance of every entry is extracted from the live feed. A dash means the state does not exist for that entry, and several entries genuinely have one.

| Component | States |
|---|---|
| `button-primary` | default · hover (fill darkens to `{colors.green-strong}`) · focus-visible (`{colors.focus}` ring) · pressed (0.97 scale) · disabled · loading (inline spinner, label held) |
| `button-outline-green` | default · hover (`{colors.discount-surface}` tint fill) · focus-visible · pressed · disabled |
| `button-outline-neutral` | default · hover (`{colors.canvas}` fill) · focus-visible · pressed · disabled |
| `button-muted` | default · hover · focus-visible · pressed · disabled |
| `button-tag` | default · hover · focus-visible · pressed · selected (`{colors.primary}` label + border) |
| `search-pill` | default · hover · focus-visible (ring, border to `{colors.focus}`) · loading (suggestion fetch) · error |
| `text-input` / `email-input` | default · hover · focus-visible · disabled · error (`{colors.hot}` border + message) |
| `nav-bar` | default · selected (active category underlined in `{colors.primary}`); its children carry their own hover / focus-visible |
| `deal-card` | default · hover (level-1 border to level-2 `{shadow.soft}`) · focus-visible (ring on the title link) · selected (visited / expanded) · loading (skeleton) |
| `sidebar-card` | default · hover · focus-visible on its links · loading (skeleton) |
| `temperature-control` | default · hover · focus-visible (ring on each arrow) · pressed (arrow pops) · selected (the user's own vote stays filled) · disabled (voting closed on expired deals) · loading (vote in flight) · error (vote rejected, reverts with a `{colors.hot}` flash) |
| `temperature-up` / `temperature-down` | default · hover · focus-visible · pressed · selected · disabled |
| `country-selector` | default · hover · focus-visible · selected (current country) |
| `footer` | default only; its links carry hover / focus-visible |
| `price-lockup` | default only — a static lockup, no interactive states |
| `discount-badge`, `badge-neutral-subtle`, `badge-filled`, `premium-badge`, `warning-badge`, `timestamp-pill` | default only — non-interactive status chips |
| `avatar` | default · hover · focus-visible where it links to a profile; otherwise default only |

### Buttons

**`button-primary`** — the green action ("Zum Deal", "Deal-Alarm anlegen", "Hinzufügen")
- Fill `{colors.primary}`, label `{colors.on-primary}` in `{typography.ui}`, shape `{rounded.full}`, padding `0px 14px`, often with a trailing external-link or plus glyph

**`button-outline-green`** — brand-tinted secondary ("+ Beitrag")
- `{colors.surface}` fill, `{colors.primary}` label + border, `{rounded.full}`, padding `0px 14px`

**`button-outline-neutral`** — quiet chrome ("Menü")
- `{colors.surface}` fill, `{colors.ink}` label, `{colors.hairline}` border, `{rounded.full}`, padding `0px 12px`

**`button-muted`** — de-emphasized action ("Ohne Zustimmung weiter")
- `{colors.surface}` fill, `{colors.body}` label, `{colors.hairline}` border, `{rounded.full}`

**`button-tag`** — compact utility control
- `{colors.surface}` fill, `{colors.ink}` label, `{rounded.md}`, tight `0px 4px` padding

### Cards & Containers

**`deal-card`** — the feed's atom
- `{colors.surface}` on `{colors.hairline}`, `{rounded.md}`, `{spacing.lg}` padding; media-left thumbnail, bold black title, a `price-lockup`, a `temperature-control`, merchant + author line, and a `button-primary` foot with comment/share/bookmark icons

**`sidebar-card`** — coupon / news / discussion tiles
- Same white-on-hairline `{rounded.md}` chrome as `deal-card`, in the right rail

**`timestamp-pill`** — "Gepostet vor …" marker
- `{colors.canvas}` fill, `{colors.body}` `{typography.caption}`, `{rounded.md}`, pinned top-right on a card

### Inputs & Forms

**`search-pill`** — the header search
- `{colors.surface}` pill at `{rounded.full}`, `{colors.hairline}` border, `{colors.body}` placeholder in `{typography.body}`, magnifier glyph left

**`text-input`**
- `{colors.surface}` field, `{colors.ink}` text, navy-translucent border, fully-round `{rounded.full}`, padding `9px 35px`

**`email-input`**
- `{colors.surface}` field at `{rounded.md}` (square-cornered against the pill search), padding `9px 16px`

### Navigation

**`nav-bar`**
- `{colors.surface}` bar with `{colors.hairline}` bottom rule: mydealz frog logo, `button-outline-neutral` "Menü", `search-pill`, "Deal-Alarm anlegen" and "Einloggen" text links, `button-outline-green` "+ Beitrag"; a category strip (Kategorien, Gutscheine, Freebies, Deals, Diskussionen, Club) sits below

**`footer`**
- `{colors.surface}` over a `{colors.hairline}` top rule; link columns (Firma, Community, Rechtliches) in `{colors.body}` with green links, social circle icons, app-store badges, and a `country-selector`

**`country-selector`**
- `{colors.surface}` `{rounded.md}` dropdown with flag + label, `{colors.hairline}` border

### Signature Components

**`temperature-control`** — the brand's defining component
- A fully-round `{rounded.full}` pill: `temperature-down` cold-blue (`{colors.cold}`) down-arrow, the deal's temperature reading in hot-red (`{colors.hot}`), and a `temperature-up` hot-red up-arrow — the crowd's price vote made visible

**`temperature-up`** / **`temperature-down`** — the vote arrows
- Up in `{colors.hot}`, down in `{colors.cold}`, both in `{typography.ui}`

**`price-lockup`** — the deal's number
- `{colors.primary}` green current price in `{typography.heading-lg}`, a struck-through `{colors.muted}` original, and a `discount-badge`

**`discount-badge`** — the saving
- `{colors.discount-surface}` mint pill with `{colors.green-strong}` label in `{typography.ui}`, `{rounded.sm}`, `4px 8px`

**`badge-neutral-subtle`** / **`badge-filled`** — status chips
- Subtle: white / black / `{rounded.md}`. Filled: `{colors.canvas}` fill, `{colors.body}` text, `{rounded.sm}` with a white hairline

**`premium-badge`** — highlighted-content marker
- `{colors.premium}` violet label on `{colors.surface}`, `{rounded.sm}`

**`warning-badge`** — expiring / caution state
- `{colors.warning-surface}` soft-yellow pill, `{colors.warning-text}` amber-brown label, `{rounded.sm}`

**`avatar`** — author / community
- Circle (`{rounded.circle}`) on `{colors.canvas}` with a white ring

### Examples (illustrative)

> Kit-mirror demonstration surfaces. These are not brand-native components — each `ex-*` entry references the brand primitives above so every example surface is shaped by this spec rather than template defaults.

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

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or curve below was extracted from mydealz; they come from the **Playful** profile in `theme-audit/SPEC.md`, chosen because saturated colour here sits on the interactive elements themselves — the hot/cold vote arrows, the green pills, the mint saving badges — and the voice (frog mascot, crowd-voted "temperature") is informal rather than editorial.

### Principles
- The temperature vote is the one place motion carries meaning: a vote should feel like a tap that *lands*, which is what `{motion.ease-enter}`'s overshoot is for.
- Everything else is quick and almost unnoticed. This is a feed of hundreds of cards; a reveal that choreographs itself is a reveal that gets in the way.
- `transform` and `opacity` only. Never `width`, `height`, `top`, `left` or `margin` — a feed this dense cannot afford layout work mid-scroll.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays a card becoming readable.
- No infinite animation except the loading skeleton and spinner. There is no brand ambience; the palette is flat and the mascot is a static illustration.

### Interaction Table

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pills, cards, links) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `transform: translateY(-1px)` on `deal-card` | Travel removed; colour/opacity change only at `{motion.duration-reduced}` |
| Press (any pill, vote arrow) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.97)`; vote arrow releases to `scale(1.06)` then settles via `{motion.ease-enter}` | Scale removed entirely; the state change is instant |
| Focus (`{colors.focus}` ring) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring | Ring appears instantly, no fade; it is never animated away |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` on the feed column only | Cross-fade at `{motion.duration-reduced}`; no transform |
| Modal / drawer (consent sheet, mobile "Menü") | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(16px)` in, `translateY(8px)` out | Opacity only at `{motion.duration-reduced}`; sheet appears in place |
| Dropdown (`country-selector`, nav menu, search suggestions) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: scale(0.98 → 1)` from the top edge | Opacity only at `{motion.duration-reduced}` |
| Toast (`ex-toast`, "Deal gespeichert") | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(12px)` | Opacity only at `{motion.duration-reduced}`; it still auto-dismisses |
| List enter (cards appended by "Mehr laden") | `{motion.duration-base}`, staggered `{motion.stagger-step}`, capped at 5 steps | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px)` | Stagger and travel removed; the batch fades in together at `{motion.duration-reduced}` |
| List exit (filtered-out or expired card) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)` | Opacity only at `{motion.duration-reduced}` |
| Loading (card skeleton, vote spinner) | `{motion.duration-emphasis}` loop | `{motion.ease-standard}`, alternating | `opacity` 0.6 ↔ 1 on the skeleton block; `transform: rotate()` on the spinner | Pulse and rotation frozen; a static skeleton with `aria-busy` remains |

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translate), all scale — including the press pop on
     the temperature control — and the list-enter stagger.
     Frozen: the skeleton pulse and the vote spinner, which hold a static frame.
     Kept: opacity fades, capped at {motion.duration-reduced} (130ms).
     Unchanged: the focus ring, which appears instantly in both modes, and
     toast auto-dismissal, which is a timeout, not an animation. */
  *, *::before, *::after {
    transition-duration: 130ms !important;   /* {motion.duration-reduced} */
    animation-duration: 130ms !important;
    animation-iteration-count: 1 !important;
    transition-property: opacity, color, background-color, border-color !important;
    transform: none !important;
  }
}
```

## Accessibility

Contrast measured with WCAG 2.1 relative luminance on the hexes in this file's own frontmatter. Everything a rendered page would be needed for — real tap-target sizes, focus order, overflow — is in Known Gaps, not claimed here.

### Measured contrast

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `ink` on `canvas` | 19.21:1 | 4.5:1 | Pass |
| `ink` on `surface` | 21.0:1 | 4.5:1 | Pass |
| `body` on `canvas` | 4.75:1 | 4.5:1 | Pass |
| `body` on `surface` | 5.19:1 | 4.5:1 | Pass |
| `green-strong` on `discount-surface` | 4.76:1 | 4.5:1 | Pass |
| `warning-text` on `warning-surface` | 4.85:1 | 4.5:1 | Pass |
| `hot` on `surface` | 5.53:1 | 4.5:1 | Pass |
| `cold` on `surface` | 7.7:1 | 4.5:1 | Pass |
| `premium` on `surface` | 5.06:1 | 4.5:1 | Pass |
| `focus` on `canvas` | 4.74:1 | 3.0:1 | Pass |
| `focus` on `surface` | 5.18:1 | 3.0:1 | Pass |
| `hairline-strong` on `canvas` | 3.05:1 | 3.0:1 | Pass (prescribed token) |
| `hairline-strong` on `surface` | 3.33:1 | 3.0:1 | Pass (prescribed token) |

### Where the real brand fails AA

These are extracted values, frozen. mydealz genuinely fails AA at each of these points; the document's job is to say so, not to repaint the brand.

- **`button-primary`** — white `on-primary` on the brand green `primary` measures **3.09:1** against a 4.5:1 requirement at its 14px/700 `{typography.ui}` label. The single most-used control on the site is below AA for body-size text. It would clear 4.5:1 at `{colors.green-strong}` (5.18:1) with no change to the label colour.
- **`button-outline-green`** — the same green as a *label* on white measures **3.09:1**, same shortfall. `{colors.green-strong}` is already the documented answer for green text on light surfaces (5.18:1); the outline button should use it and the brand does not.
- **`price-lockup`** — the green price on `canvas` measures **2.83:1**. It is set at 24px/700, so WCAG's large-text threshold of 3:1 applies, and it misses even that by 0.17. On `surface`, where prices actually sit inside a card, the same pair reaches 3.09:1 and clears large-text AA. The failure is real only for a price rendered directly on the page floor.
- **`hairline`** — **1.2:1** on `canvas`, **1.31:1** on `surface`, against 3:1 for a boundary. Decorative here by scope: card separation is carried by the `canvas` gutter as well as the line. Any control whose edge is its only definition uses `{colors.hairline-strong}` instead.
- **`muted`** — **2.16:1** on `canvas`, **2.36:1** on `surface`, against 4.5:1. Restricted to the struck-through original price (redundant next to the live price) and to placeholder text in labelled fields. It is not an acceptable colour for secondary copy; `{colors.body}` is.
- **`warning-surface`** — the soft-yellow pill measures **1.01:1** against `canvas`. This is a background, not ink: the pair that carries text is `warning-text` on `warning-surface` at 4.85:1, which passes. The consequence is that an isolated warning pill has no visible edge on the page floor, so it is only ever used inside a card on `surface` (1.09:1 there — still edgeless, so it carries a `{colors.hairline-strong}` border when it sits alone).
- **`warm`** — rising-orange measures **3.1:1** on `surface` and **2.84:1** on `canvas`. Usable for a 24px+ numeral or an icon paired with text, never for 14px label copy.

### Focus ring visibility, per surface

| Drawn on | Ring | Ratio | Required |
|---|---|---|---|
| `{colors.canvas}` (page floor) | `{colors.focus}` | 4.74:1 | 3.0:1 |
| `{colors.surface}` (every card, nav, footer) | `{colors.focus}` | 5.18:1 | 3.0:1 |
| `ex-pricing-tier-featured` black fill (`{colors.ink}`) | `{colors.focus}` | 4.05:1 | 3.0:1 |

One ring covers all three grounds, so this file defines `focus` and no `focus-on-dark`. The ring is drawn 2px outside the control with a 2px offset, which is why it is measured against the surface behind the control and not against the control's own fill — a green ring on the green `button-primary` would be invisible measured that way, and WCAG 2.2 Focus Appearance asks for the former.

### Other

- **Tap targets**: the system's pill padding (`0px 14px` on `button-primary`) sets no height, so the rendered target cannot be verified from this document. Prescribed minimum: 44×44px for every pill, vote arrow, and card-foot icon, with hit area extended beyond the visual bounds where the glyph is smaller. See Known Gaps.
- **Reduced motion**: handled in full under Motion & Animation. Travel and scale removed, loaders frozen, opacity fades capped at `{motion.duration-reduced}` (130ms).
- **Colour is never the only signal**: hot/cold is the one place the brand leans on colour alone, and the arrows carry direction as well as hue — up/down glyphs stay distinguishable in monochrome.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` green for actions and prices — it is the single thread tying the feed together.
- Keep the `temperature-control` pairing intact: `{colors.cold}` down, `{colors.hot}` up and temperature — it's the brand's signature.
- Pill every button, chip, search, and the temperature control to `{rounded.full}`; keep content cards at `{rounded.md}`.
- Put savings in the `{colors.discount-surface}` mint badge beside the green price.
- Hold typography to Averta CY 500 / 700; bold every price and temperature.
- Separate cards with `{colors.hairline}` borders and the `{colors.canvas}` gutter, not heavy shadows.

### Don't
- Don't recolor prices or primary actions away from `{colors.primary}` green.
- Don't split the temperature pairing or recolor the vote arrows — cold is blue, hot is red, always.
- Don't introduce shadows on resting feed cards; the soft 4–12px shadow is for elements that lift.
- Don't use a third or fourth type weight — the system is 500 and 700 only.
- Don't let `{colors.warm}` orange or `{colors.premium}` violet drift into decorative use; they are functional status colors.
- Don't square off the pills — the fully-round `{rounded.full}` button is the brand's shape signature.
- Don't use `{colors.muted}` for copy anyone has to read, or `{colors.hairline}` as a control's only edge — those are the brand's two AA failures and `{colors.body}` / `{colors.hairline-strong}` are the replacements.
- Don't animate `width`, `height`, `top`, `left` or `margin`; a feed this long cannot afford layout work mid-scroll.
- Don't suppress the focus ring on the pills. It is `{colors.focus}` at 2px with a 2px outside offset, on every interactive element.

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Single-column feed; sidebar drops; nav collapses to the "Menü" pill; temperature control and CTA stack under the card body |
| Desktop | ≥ 768px | Feed + right sidebar two-column shell; full nav row with search pill and category strip |

### Touch Targets
Pill buttons (`{components.button-primary}`) and the temperature control clear a comfortable tap height; vote arrows, comment, share, and bookmark icons carry generous hit areas on the card foot.

### Collapsing Strategy
The category strip and right sidebar collapse first; the nav condenses to the "Menü" pill + search + submit; deal cards reflow from a media-left row into a stacked thumbnail-over-body layout on narrow screens.

### Image Behavior
Deal thumbnails are contained in `{rounded.md}` frames on the card's media side, never full-bleed; avatars are perfect circles (`{rounded.circle}`). Merchant logos and app-store badges render inline at fixed heights.

## Known Gaps

What this document does not know, kept separate from what it does.

- **Motion is prescribed, not extracted.** Every duration, curve, stagger and reduced-motion rule in Motion & Animation comes from the **Playful** profile in the audit spec. mydealz's real timings were never measured.
- **The focus ring is prescribed.** mydealz publishes no focus indicator. `{colors.focus}`, its 2px width and 2px offset are specified here; only the colour value is brand-derived (it is `{colors.green-strong}`'s hex).
- **`{colors.hairline-strong}` is prescribed.** It is the accessible parallel to the extracted `{colors.hairline}`, not a colour the brand uses.
- **Tap-target sizes are unverifiable from this document.** Component padding is extracted but no height is; the 44×44px minimum in Accessibility is a prescription, not a measurement. Confirming it needs a rendered page.
- **Nothing here is measured from a running page**: overlap, horizontal overflow, clipping, frame rate and layout shift are all out of reach of a document audit. No claim about them appears above.
- **Button heights, line-height on buttons, and icon sizes** are absent from the token block — only horizontal padding was extracted.
- **No dark mode.** The `ex-pricing-tier-featured` description mentions a light/dark polarity flip, but this file documents one light theme only; there is no dark-mode palette, and no dark canvas, surface or text tokens exist to build one.
- **State styling is partly prescribed.** Resting appearance is extracted for every component; the hover tints, pressed scales and error treatments in the State Coverage table are specified to be consistent with the brand, not observed.
- **Averta CY is commercial**, so the metrics behind the type scale cannot be re-verified from an open-source substitute.
- **The `ex-*` entries are illustrative kit-mirror surfaces**, not brand-native components. They inherit this file's tokens but no mydealz screen contains a pricing tier, cart drawer or data table.
