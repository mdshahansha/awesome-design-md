---
version: alpha
name: Renault-design-analysis
description: |
  Renault's web presence pairs the freshly-modernised Renault diamond
  (the 2021 flat-line rhombus mark) with a stark black-and-white canvas, a
  signature Sunlight Yellow accent, and the proprietary NouvelR display
  typeface. The system reads as confident, photography-first automotive — large
  hero cars on neutral or atmospheric backdrops, square-edged or barely-rounded
  containers, and a small disciplined palette where every coloured element is
  intentional. Tile grids, full-bleed banners, and a recurring "configurator"
  surface (white card, yellow accent dots, neutral product chrome) carry the
  mass-market dealership tone without crossing into luxury.

colors:
  primary: "#ffed00"
  primary-deep: "#e6d200"
  on-primary: "#000000"
  ink: "#000000"
  body: "#222222"
  charcoal: "#333333"
  mute: "#666666"
  ash: "#8a8a8a"
  stone: "#c4c4c4"
  on-dark: "#ffffff"
  on-dark-mute: "rgba(255,255,255,0.72)"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#000000"
  surface-deep: "#111111"
  hairline: "#f2f2f2"
  hairline-strong: "#000000"
  divider-dark: "rgba(255,255,255,0.16)"
  focus: "#000000"
  focus-on-dark: "#ffed00"
  badge-new: "#ffed00"
  link: "#0000ee"
  error: "#be6464"
  warning: "#f0ad4e"
  success: "#8dc572"
  info: "#337ab7"

typography:
  display-xl:
    fontFamily: NouvelR
    fontSize: 56px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0
  display-lg:
    fontFamily: NouvelR
    fontSize: 40px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0
  display-md:
    fontFamily: NouvelR
    fontSize: 32px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0
  heading-lg:
    fontFamily: NouvelR
    fontSize: 24px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0
  heading-md:
    fontFamily: NouvelR
    fontSize: 20px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0
  heading-sm:
    fontFamily: NouvelR
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  subtitle:
    fontFamily: NouvelR
    fontSize: 19.2px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-lg:
    fontFamily: NouvelR
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: NouvelR
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-sm:
    fontFamily: NouvelR
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  button-lg:
    fontFamily: NouvelR
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  button-md:
    fontFamily: NouvelR
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.144px
  button-sm:
    fontFamily: NouvelR
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.13px
  caption:
    fontFamily: NouvelR
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  overline:
    fontFamily: NouvelR
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.45
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 3px
  md: 4px
  pill: 46px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  xxl: 32px
  xxxl: 40px
  section: 80px

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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 48px
  button-primary-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 24px
  button-outline-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
  button-outline-light:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
  button-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
    height: 36px
  button-icon-square:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    size: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    padding: 0
  promo-tile-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.none}"
    padding: 32px
  promo-tile-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.none}"
    padding: 32px
  promo-tile-yellow:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.none}"
    padding: 32px
  vehicle-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0
  configurator-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 24px 0
  configurator-swatch:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.full}"
    size: 56px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 60px
  sub-nav-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 64px 24px
---

## Overview

Renault's Turkish marketing surfaces are unapologetically high-contrast: a
white canvas for browsing, a black canvas for product storytelling, and a
single Sunlight Yellow accent (`{colors.primary}` — `#ffed00`) reserved for
the most consequential actions. The brand's modernised flat diamond logo sets
the tone — geometric, confident, slightly industrial — and the system follows
suit. Square corners dominate, hairline borders are rare, and elevation is
expressed through colour blocking rather than shadow.

The typography is monolithic. Every text on the site is set in **NouvelR**,
Renault's bespoke display family, with a strong preference for weight 700 at
display sizes (with a tight `lineHeight: 0.95`) and weight 400 for body. There
is no secondary serif, no decorative italic, no script — the discipline is
the signature.

Page rhythm cycles between three surface modes: a **white catalogue mode** for
listings and configurators (`{colors.canvas}` with hairline-thin
`{colors.hairline}` dividers), a **black storytelling mode** for hero
sections, lifestyle imagery, and the lower half of campaign pages, and brief
**yellow accent moments** (`{colors.primary}` tiles, "NEW" badges, R5-coded
yellow paint shots) that punctuate the otherwise neutral palette.

**Key Characteristics:**
- Two-tone canvas system — `{colors.canvas}` (white) for browsing, `{colors.surface-dark}` (black) for storytelling — switched in full-bleed bands rather than subtle gradations.
- A single brand accent — `{colors.primary}` Sunlight Yellow — used scarcely on primary CTAs, "NEW" badges, R5 hero photography, and configurator dot indicators.
- **NouvelR everywhere**, with `{typography.display-xl}` headlines at 56px / weight 700 / `lineHeight: 0.95` so condensed multi-line headlines stack cleanly.
- Square geometry: `{rounded.xs}` (2px) on buttons, `{rounded.none}` on tiles and product cards, `{rounded.pill}` reserved exclusively for sub-nav chips and decorative badges.
- Photography-first product tiles — vehicle photos full-bleed inside otherwise neutral cards, with copy stacked beneath rather than overlaid.
- Page-level rhythm cycles white → black → yellow accent → black, with the wordmark and footer always closing on `{colors.surface-dark}`.

## Colors

### Brand & Accent
- **Sunlight Yellow** (`{colors.primary}` — `#ffed00`): the brand accent. Reserved for primary CTAs, "NEW" / "yeni" badges, configurator dot indicators, and full-bleed promotional tiles. Never decorative.
- **Sunlight Yellow Pressed** (`{colors.primary-deep}` — `#e6d200`): the active/pressed state of `{colors.primary}` buttons and tiles.
- **On-Primary** (`{colors.on-primary}` — `#000000`): label colour on top of `{colors.primary}` surfaces. Yellow always pairs with black text — never white.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): the default page background and card surface.
- **Surface Soft** (`{colors.surface-soft}` — `#f7f7f7`): subtle elevation step for grouped configurator rows and inactive form fields.
- **Surface Dark** (`{colors.surface-dark}` — `#000000`): the alternate canvas, used for hero bands, footer, and full-bleed storytelling sections.
- **Surface Deep** (`{colors.surface-deep}` — `#111111`): a one-step-up elevation inside `{colors.surface-dark}` regions for inset cards and form panels.
- **Hairline** (`{colors.hairline}` — `#f2f2f2`): the soft 1px divider between rows on white surfaces. **Decorative only** — it measures 1.12:1 on `{colors.canvas}` and 1.04:1 on `{colors.surface-soft}`, so it must never be the sole boundary of a control. It is an extracted value and is kept exactly as extracted; the file's passing boundary tone is `{colors.hairline-strong}`. See Accessibility.
- **Hairline Strong** (`{colors.hairline-strong}` — `#000000`): full-strength dividers on white, plus all card / button outlines.
- **Divider Dark** (`{colors.divider-dark}` — `rgba(255,255,255,0.16)`): the corresponding low-contrast divider used inside `{colors.surface-dark}` regions. Decorative only, at 1.44:1 once composited.

### Focus

Both rings are **prescribed, not extracted** — the captured pages show no focus
styling at all (see Known Gaps). Each reuses a value the palette already owns,
so neither introduces a new brand colour.

- **Focus** (`{colors.focus}` — `#000000`, the same ink as `{colors.ink}`): the ring on light surfaces — `{colors.canvas}`, `{colors.surface-soft}`, `{colors.surface-card}` and `{colors.primary}` tiles. 2px, drawn outside the control at a 2px offset.
- **Focus On Dark** (`{colors.focus-on-dark}` — `#ffed00`, the same yellow as `{colors.primary}`): the ring on `{colors.surface-dark}` and `{colors.surface-deep}` bands and in the footer. Same 2px / 2px-offset geometry.

### Text
- **Ink** (`{colors.ink}` — `#000000`): primary text colour on white surfaces. The same value also drives logos, icons, and outline borders — black is structural, not decorative.
- **Body** (`{colors.body}` — `#222222`): secondary body text where pure black would feel too heavy in long paragraphs.
- **Charcoal** (`{colors.charcoal}` — `#333333`): captions, metadata, and small labels.
- **Mute** (`{colors.mute}` — `#666666`): supporting text and inactive nav labels.
- **Ash** (`{colors.ash}` — `#8a8a8a`): placeholder text, disabled labels.
- **Stone** (`{colors.stone}` — `#c4c4c4`): disabled-state foreground.
- **On-Dark** (`{colors.on-dark}` — `#ffffff`): primary text on `{colors.surface-dark}` surfaces.
- **On-Dark Mute** (`{colors.on-dark-mute}` — `rgba(255,255,255,0.72)`): secondary text in dark regions; preserves the brand's high-contrast feel without resorting to mid-grey.

### Semantic
- **Error** (`{colors.error}` — `#be6464`): muted desaturated red used for inline form errors. Notably warmer than typical pure-red error states.
- **Warning** (`{colors.warning}` — `#f0ad4e`): amber alert.
- **Success** (`{colors.success}` — `#8dc572`): muted green confirmation.
- **Info** (`{colors.info}` — `#337ab7`): a desaturated mid-blue used in informational chips.
- **Link** (`{colors.link}` — `#0000ee`): the unstyled-anchor default kept for fallback inline text links — production links inherit `{colors.ink}` and rely on underline/weight rather than colour.

## Typography

### Font Family

The entire system is set in **NouvelR**, Renault's proprietary display
family, used across navigation, headlines, body, captions, and button
labels. The family carries a slightly geometric, semi-condensed personality
with tall x-heights and squared apexes that pair naturally with the diamond
logomark.

When NouvelR cannot be licensed, suitable open-source substitutes include
**Inter Tight**, **Manrope**, or **HK Grotesk Semi Condensed** — all share
the geometric-with-warmth feel and adapt cleanly to weights 400 / 600 / 700.
Tighten `lineHeight` on display sizes to ~0.95 to match the original; do not
relax it.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 56px | 700 | 0.95 | 0 | Hero headlines, campaign titles ("E-TECH ELEKTRİKLİ", "REVOLUTION"). |
| `{typography.display-lg}` | 40px | 700 | 0.95 | 0 | Secondary section titles. |
| `{typography.display-md}` | 32px | 700 | 0.95 | 0 | Page-level H1 on sub-pages and configurator panels. |
| `{typography.heading-lg}` | 24px | 700 | 0.95 | 0 | Section headers, card titles. |
| `{typography.heading-md}` | 20px | 700 | 0.95 | 0 | Sub-section headers, prominent labels. |
| `{typography.heading-sm}` | 18px | 700 | 1.0 | 0 | Tile titles, list group headers. |
| `{typography.subtitle}` | 19.2px | 600 | 1.3 | 0 | Lead paragraphs, hero subtitles. |
| `{typography.body-lg}` | 18px | 400 | 1.5 | 0 | Long-form body. |
| `{typography.body-md}` | 16px | 400 | 1.4 | 0 | Default body and form fields. |
| `{typography.body-sm}` | 14px | 400 | 1.57 | 0 | Captions, metadata. |
| `{typography.button-lg}` | 16px | 700 | 1.0 | 0 | Large CTAs in hero bands. |
| `{typography.button-md}` | 14.4px | 700 | 1.0 | 0.144px | Default button label across the system. |
| `{typography.button-sm}` | 13px | 600 | 1.2 | 0.13px | Sub-nav pills, small in-card actions. |
| `{typography.caption}` | 12px | 400 | 1.4 | 0 | Footer disclosure, regulatory text. |
| `{typography.overline}` | 10px | 700 | 1.45 | 0 | Short uppercase labels above titles. |

### Principles
- Display sizes always weight 700, always at `lineHeight: 0.95`. The tightness is what makes the brand feel confident rather than corporate.
- Body copy stays at weight 400 — never 500. The contrast between body and display is part of the system.
- Button labels carry a tiny positive letter-spacing (`0.144px` on `{typography.button-md}`) — almost imperceptible, but it adds the small bit of mechanical precision the brand wants on CTAs.
- No italics, no script, no decorative ligatures.

### Note on Font Substitutes

NouvelR is licensed; substitutes (Inter Tight / Manrope / HK Grotesk Semi
Condensed) preserve the geometric character but typically render with
slightly looser line heights at display sizes — clamp display
`lineHeight` to 0.95 explicitly to match the source.

## Layout

### Spacing System
- **Base unit**: 4px, with the working scale built on multiples of 4 and 8.
- **Tokens**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 20px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.xxxl}` 40px · `{spacing.section}` 80px.
- Section padding (full-bleed band → next band): `{spacing.section}` (80px) on desktop, collapsing to `{spacing.xxxl}` (40px) on mobile.
- Promo-tile internal padding: `{spacing.xxl}` (32px) all sides on desktop.
- Configurator row vertical padding: `{spacing.xl}` (24px) top/bottom with hairline divider between rows.

### Grid & Container
- **Max content width** ≈ 1440px. Beyond that, content remains centred and the dark/light bands extend full-bleed.
- **Promo grid** on the homepage: a 2-column tile grid on desktop, dropping to 1-up on mobile. Each tile is square-cornered (`{rounded.none}`) with the photography or solid colour as the background.
- **Vehicle range grids**: 3 to 4 cars per row at desktop, collapsing 2-up at tablet and 1-up at small mobile.
- **Configurator** uses a fixed left visualisation pane (~60% width) with a right-hand scrolling option list (~40% width) on desktop.

### Whitespace Philosophy
- Whitespace is structural, not decorative. Sections are separated by colour-blocking (white → black) rather than soft padding ramps.
- Inside cards and configurator rows, padding is generous but never airy — the brand is mass-market, so density is acceptable.
- Hairline `{colors.hairline}` dividers on white surfaces create the sense of catalogue precision; on dark surfaces, `{colors.divider-dark}` carries the same role.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | No shadow, no border | Default page surface, full-bleed bands. |
| 1 — outline | 1px solid `{colors.hairline-strong}` where the outline is the component's boundary; 1px `{colors.hairline}` only as a decorative row rule | Promo tiles on light, vehicle cards, configurator panels. |
| 2 — colour-blocked elevation | Surface colour shift (e.g. `{colors.canvas}` card sitting inside a `{colors.surface-soft}` band) | Configurator detail cards, related-content rows. |
| 3 — dark inversion | Card swaps to `{colors.surface-dark}` against a `{colors.canvas}` band | "Ticari araç" hero promo tiles, lifestyle storytelling cards. |

The layers are deliberately faint: `{colors.canvas}` against
`{colors.surface-soft}` measures 1.07:1 and `{colors.surface-dark}` against
`{colors.surface-deep}` 1.11:1. Neither separation is a boundary — it is a tonal
hint, and any layer that must read as a distinct container takes an outline in
`{colors.hairline-strong}` (21.00:1 on `{colors.canvas}`) or inverts polarity
(level 3). Elevation in this system is **one mechanism — colour blocking plus
outline**; shadow is not part of the catalogue vocabulary.

Drop shadows are extracted from the system but rarely visible on the marketing
surfaces. When they appear, they are very subtle (~10% opacity, 2–4px blur)
and used on floating elements like the configurator's sticky summary bar.

### Decorative Depth
- The R5 hero band uses an atmospheric mesh-gradient backdrop — purple-to-pink-to-yellow glow behind the car silhouette — that acts as the only true atmospheric depth in the system. Everywhere else, depth is structural (colour-blocking + outlines), not atmospheric.
- E-TECH electric powertrain pages use a luminous magenta-to-violet gradient behind cutaway diagrams, reserved for the electric sub-brand.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Tiles, vehicle cards, dividers, banner bands, full-bleed images. |
| `{rounded.xs}` | 2px | Default buttons (primary yellow, secondary black, outline). |
| `{rounded.sm}` | 3px | Tab panels, small chips. |
| `{rounded.md}` | 4px | Form labels, inline tags. |
| `{rounded.pill}` | 46px | Sub-nav pills, "yeni" / "NEW" badges, decorative carousel chips. |
| `{rounded.full}` | 9999px | Configurator colour swatches, avatar dots. |

### Photography Geometry
- Vehicle photography is **always square-cornered** (`{rounded.none}`). No rounded vehicle hero shots, no soft-edged car cards.
- Aspect ratios cluster around **16:9** (hero bands), **1:1** (square promo tiles), and **4:3** (vehicle range cards). Lifestyle imagery sometimes runs **2:1 wide** for full-bleed bands.
- Avatars and small profile cues — when present — use `{rounded.full}` circles to contrast with the otherwise square geometry.

## Components

Each entry's `States:` line lists the states that control supports. Default,
and the pressed value of `button-primary-pressed`, are extracted. The remaining
state treatments are **prescribed** from the brand's own tokens — the captured
marketing pages are static, so hover, focus-visible, disabled, loading,
selected and error renderings were not observable (see Known Gaps).

### Buttons

**`button-primary`** — yellow CTA
- Background `{colors.primary}`, label `{colors.on-primary}`, type `{typography.button-md}`, padding `14px 24px`, `rounded: {rounded.xs}`.
- The single most important action on a page (e.g. "Hemen randevu al", "Hesapla", "Konfigüratörü başlat").
- Pressed state lives in `button-primary-pressed` (background `{colors.primary-deep}`).
- States: default · hover (`{colors.primary-deep}` fill) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (`{colors.primary-deep}` plus `scale(0.98)`) · disabled (`{colors.stone}` fill, `{colors.mute}` label, no ring) · loading (label holds, 2px `{colors.ink}` indeterminate bar along the lower edge) · error is owned by the adjacent field, never by this button.

**`button-secondary-dark`** — solid black CTA
- Background `{colors.surface-dark}`, label `{colors.on-dark}`, type `{typography.button-md}`, `rounded: {rounded.xs}`.
- Equal-weight secondary action paired with `{component.button-primary}`, or the primary action when used on a yellow tile background.
- States: default · hover (`{colors.surface-deep}` fill) · focus-visible (2px `{colors.focus}` ring, 2px offset, drawn on `{colors.canvas}`) · active/pressed (`{colors.surface-deep}` plus `scale(0.98)`) · disabled (`{colors.stone}` fill, `{colors.mute}` label) · loading (2px `{colors.primary}` indeterminate bar along the lower edge) · no selected or error state; it is an action, not a control.

**`button-outline-dark`** — outlined CTA on light
- Background `{colors.canvas}`, label `{colors.ink}`, 1px solid `{colors.hairline-strong}`, type `{typography.button-md}`, `rounded: {rounded.xs}`.
- Tertiary action; appears alongside primary/secondary for "Detayları gör", "Modeller", etc.
- States: default · hover (border thickens to 2px `{colors.ink}`, fill stays `{colors.canvas}`) · focus-visible (2px `{colors.focus}` ring at 2px offset, outside the border) · active/pressed (`{colors.surface-soft}` fill plus `scale(0.98)`) · disabled (border `{colors.stone}`, label `{colors.ash}`) · loading and selected are both absent on this variant — two interactive states only.

**`button-outline-light`** — outlined CTA on dark
- Background `{colors.surface-dark}`, label `{colors.on-dark}`, 1px solid `{colors.on-dark}`, type `{typography.button-md}`, `rounded: {rounded.xs}`.
- The dark-canvas counterpart to `{component.button-outline-dark}`.
- States: default · hover (border thickens to 2px `{colors.on-dark}`) · focus-visible (2px `{colors.focus-on-dark}` ring at 2px offset, drawn on `{colors.surface-dark}`) · active/pressed (`{colors.surface-deep}` fill plus `scale(0.98)`) · disabled (border and label `{colors.on-dark-mute}`) · no loading or selected state.

**`button-pill`** — sub-nav chip
- Background `{colors.canvas}`, label `{colors.ink}`, 1px solid `{colors.hairline-strong}`, type `{typography.button-sm}`, `rounded: {rounded.pill}`, height 36px.
- The only place the system uses a pill — for top-level filter chips ("Servis & randevu", "Sahiplik dönemi geçişi", "Kampanyalar") and configurator tab switches.
- States: default · hover (`{colors.surface-soft}` fill) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (`{colors.surface-soft}` fill plus `scale(0.98)`) · selected (fill inverts to `{colors.surface-dark}` with `{colors.on-dark}` label, `aria-current` set) · disabled (border `{colors.stone}`, label `{colors.ash}`) · no loading state.

**`button-icon-square`** — small icon button
- Background `{colors.canvas}`, 1px solid `{colors.hairline-strong}`, `rounded: {rounded.xs}`, 40×40px square.
- Carousel arrows, share, language switcher.
- States: default · hover (`{colors.surface-soft}` fill) · focus-visible (2px `{colors.focus}` ring, 2px offset; `{colors.focus-on-dark}` when the button sits on a dark band) · active/pressed (`scale(0.96)`) · disabled (icon `{colors.stone}`, border `{colors.hairline}`, used at the ends of a carousel) · no loading, selected or error state.

### Cards & Containers

**`promo-tile-light`** — white promo tile
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.heading-lg}`, padding `{spacing.xxl}`, `rounded: {rounded.none}`.
- Used in the homepage 2-up grid for "Hybrid araç modelleri", "binek araç satış kampanyaları" tiles.
- States: default · hover (photography scales to 1.03 inside a fixed, non-animated frame; the tile's own box never changes size) · focus-visible (2px `{colors.focus}` ring, 2px offset, around the whole tile when it is a single link) · active/pressed (`scale(0.995)`) · a tile is a link: no disabled, loading, selected or error state.

**`promo-tile-dark`** — black promo tile
- Background `{colors.surface-dark}`, text `{colors.on-dark}`, type `{typography.heading-lg}`, padding `{spacing.xxl}`, `rounded: {rounded.none}`.
- Lifestyle / commercial-vehicle storytelling tiles ("ticari araç satış kampanyaları").
- States: default · hover (photography scales to 1.03 within its frame) · focus-visible (2px `{colors.focus-on-dark}` ring at 2px offset) · active/pressed (`scale(0.995)`) · link-only: no disabled, loading, selected or error state.

**`promo-tile-yellow`** — accent promo tile
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.heading-lg}`, padding `{spacing.xxl}`, `rounded: {rounded.none}`.
- The single "PARLAK SARI" / "Sunlight Yellow" attention tile that anchors a campaign band. Reserved — usually one per page maximum.
- States: default · hover (fill deepens to `{colors.primary-deep}`) · focus-visible (2px `{colors.focus}` ring at 2px offset — black on yellow, measured 17.37:1) · active/pressed (`{colors.primary-deep}` plus `scale(0.995)`) · link-only: no disabled, loading, selected or error state.

**`vehicle-card`** — car listing card
- Background `{colors.canvas}`, full-bleed product photography on top, text below, `rounded: {rounded.none}`, no outer border.
- Includes vehicle name (`{typography.heading-md}`), variant subtitle (`{typography.body-sm}`), and a single trailing arrow icon.
- States: default · hover (photo scales to 1.03 in its frame, arrow translates 4px right) · focus-visible (2px `{colors.focus}` ring at 2px offset around the card) · active/pressed (`scale(0.995)`) · loading (skeleton: `{colors.surface-soft}` blocks at the photo and the two text lines, opacity pulse only) · selected (in compare mode, 2px `{colors.hairline-strong}` border plus a `{colors.primary}` check) · no disabled or error state.

**`hero-banner`** — full-bleed hero
- Background `{colors.surface-dark}` with full-bleed photo or atmospheric gradient, content stacked left, type `{typography.display-xl}` for the title.
- "SCENIC E-TECH ELEKTRİKLİ" hero on the homepage.
- States: a presentation band with two states only — default and loading (the atmospheric gradient and photo fade in over `{motion.duration-emphasis}`; `{colors.surface-dark}` holds the band until then). Hover, focus-visible, active/pressed, disabled, selected and error belong to the CTAs inside it, not to the band.

### Inputs & Forms

**`text-input`** — default input
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, 1px bottom border `{colors.hairline-strong}`, `rounded: {rounded.none}`, padding `{spacing.sm} {spacing.md}`, height 48px.
- Inputs intentionally minimal — borderless on top and sides, single hairline at the bottom — keeping the catalogue feel.
- States: default · hover (bottom border thickens to 2px `{colors.ink}`) · focus-visible (bottom border 2px `{colors.ink}` plus a 2px `{colors.focus}` ring at 2px offset around the field box — the thicker border alone is a 1-attribute change and does not satisfy WCAG 2.2) · disabled (`{colors.surface-soft}` fill, `{colors.ash}` text, bottom border `{colors.stone}`) · loading (field locks and an indeterminate 2px `{colors.primary}` bar replaces the bottom border while an async lookup, e.g. postcode-to-dealer, runs) · error (bottom border 2px `{colors.error}`, message below in `{typography.body-sm}` `{colors.error}` with a leading icon, since `{colors.error}` alone measures 4.04:1 on `{colors.canvas}`) · no selected state; selection lives on the select control.

### Configurator

**`configurator-row`** — option list row
- Background `{colors.canvas}`, separator hairline `{colors.hairline}` between rows, padding `{spacing.xl}` top/bottom, type `{typography.body-md}`.
- Right-side scrolling list on the configurator: "kasa tipi", "motor seçimi", "versiyon seçimi", "renk seçenekleri", etc.
- States: default · hover (`{colors.surface-soft}` fill across the full row) · focus-visible (2px `{colors.focus}` ring at 2px offset, inset so it is not clipped by the scroll container) · active/pressed (`{colors.surface-soft}` fill, no scale — the row is full-width) · selected (left edge gains a 4px `{colors.primary}` marker and the label steps to weight 700) · disabled (option unavailable for the chosen trim: label `{colors.ash}`, row not focusable, reason in `{typography.caption}`) · loading (price recalculating: the price cell shows a `{colors.surface-soft}` skeleton) · error (the row's inline price lookup failed: message in `{colors.error}`).

**`configurator-swatch`** — circular colour pick
- Background `{colors.surface-soft}` (or the actual car colour), `rounded: {rounded.full}`, 56×56px.
- Used for paint colour selection. Active state adds a 1px solid `{colors.hairline-strong}` ring.
- States: default · hover (swatch scales to 1.08) · focus-visible (2px `{colors.focus}` ring at 3px offset so the ring never touches the paint colour it surrounds — the swatch fill is a product colour with no measurable contrast, so the ring is judged against `{colors.canvas}` behind it at 21.00:1) · active/pressed (`scale(0.96)`) · selected (extracted: 1px solid `{colors.hairline-strong}` ring plus a 2px gap, and the paint name is announced in text — colour is never the only cue) · disabled (paint unavailable on this trim: 40% opacity plus a diagonal `{colors.stone}` slash) · no loading or error state.

### Navigation

**`nav-bar`** — top nav (desktop)
- Background `{colors.canvas}`, type `{typography.button-md}`, height 60px, hairline `{colors.hairline}` bottom border.
- Left: diamond logomark. Centre: top-level nav ("Modeller", "Hizmetler", "Renault Yaşamı", "MyRenault"). Right: language switcher + login icon.
- States (per nav item): default · hover (label steps `{colors.mute}` → `{colors.ink}`, 2px `{colors.ink}` underline grows from the centre) · focus-visible (2px `{colors.focus}` ring at 2px offset, inside the 60px bar) · active/pressed (`{colors.surface-soft}` fill on the item) · selected (current section: persistent 2px `{colors.ink}` underline, `aria-current="page"`) · disabled and loading do not apply to nav items; error does not apply.

**`nav-bar`** (mobile)
- Same height 60px, collapses centre nav into a hamburger icon. Logo stays left, login stays right.
- States (hamburger): default · hover (`{colors.surface-soft}` fill) · focus-visible (2px `{colors.focus}` ring at 2px offset) · active/pressed (`scale(0.96)`) · selected (drawer open: icon swaps to a close glyph, `aria-expanded="true"`) · no disabled, loading or error state.

**`sub-nav-pill`** — pill-style sub-nav
- Pill chips set in a horizontal scroll bar between hero and content body (e.g. "Servis & randevu", "Sahiplik dönemi geçişi", "Kampanyalar"), `{component.button-pill}` styling.
- States: inherits every state of `{component.button-pill}` — default, hover, focus-visible, active/pressed, selected, disabled — with no loading or error state of its own.

### Signature Components

**`badge-new`** — "yeni" badge
- Background `{colors.primary}`, label `{colors.on-primary}`, type `{typography.button-md}`, `rounded: {rounded.full}`, padding `6px 14px`.
- Anchored on the bottom-left of new vehicle cards.
- States: a non-interactive label with one state — default. No hover, focus-visible, active/pressed, disabled, loading, selected or error state, because it is never focusable and never a control.

**`footer`** — global footer
- Background `{colors.surface-dark}`, text `{colors.on-dark}`, type `{typography.body-sm}`, padding `64px 24px`.
- Three-column legal/quick-links/locale grid above a single-line copyright row separated by `{colors.divider-dark}`.
- States (per footer link): default · hover (`{colors.on-dark-mute}` → `{colors.on-dark}`, 1px underline) · focus-visible (2px `{colors.focus-on-dark}` ring at 2px offset on `{colors.surface-dark}`) · active/pressed (no scale — these are dense text links; the underline thickens to 2px) · no disabled, loading, selected or error state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** No timing function, duration or stagger below
was extracted from renault.com.tr; they are the shared **Cinematic** profile
values from the audit spec, chosen because the identity is automotive and
photography-first: full-bleed vehicle bands, sparse 700-weight NouvelR
headlines, and a slow reveal that lets the car land before the type does.

The brand reading that follows from that: motion is **weighted, never bouncy**.
No overshoot, no spring, no elastic easing anywhere — the same discipline that
rules out a secondary accent and a decorative italic rules out a springy
button. Travel is short and slow rather than long and fast, and only
`transform` and `opacity` ever animate. Colour-blocked band changes
(`{colors.canvas}` → `{colors.surface-dark}`) are scroll position, not
animation; bands never cross-fade into each other.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, pill, nav item) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, and the underline's `transform: scaleX()` | Fill and label colour swap instantly; no underline growth, no scale. |
| Hover (photography in a tile or vehicle card) | `{motion.duration-slow}` | `{motion.ease-standard}` | `transform: scale(1 → 1.03)` inside a fixed frame | Scale removed entirely; the photo holds at 1. |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` (0.96 on icon buttons, 0.995 on tiles) | Scale removed; the pressed fill (`{colors.primary-deep}`) applies with no transition. |
| Focus-visible (ring appears) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the ring only — never its width or offset | Ring appears at full opacity immediately. Never suppressed. |
| Page / route transition | out `{motion.duration-base}`, in `{motion.duration-slow}` | out `{motion.ease-exit}`, in `{motion.ease-enter}` | `opacity`, plus `transform: translateY(16px → 0)` on the incoming content block | Cross-fade at `{motion.duration-reduced}`; no travel. |
| Hero band first paint (signature) | `{motion.duration-emphasis}` | `{motion.ease-enter}` | photo `transform: scale(1.06 → 1)` with `opacity`; headline follows one `{motion.stagger-step}` later | Photo and headline appear together, opacity only, `{motion.duration-reduced}`; no scale, no stagger. Content is never gated on the animation. |
| Modal / drawer (open) | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(24px → 0)`; drawer uses `translateX(100% → 0)` | Opacity fade at `{motion.duration-reduced}`; the panel is placed with no travel. Scrim fades only. |
| Modal / drawer (close) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, reverse `transform` | Opacity fade at `{motion.duration-reduced}`; no travel. |
| Dropdown / language switcher (open) | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(-8px → 0)` | Opacity fade at `{motion.duration-reduced}`. |
| Dropdown (close) | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` only | Opacity fade at `{motion.duration-reduced}`. |
| Toast / inline confirmation (enter) | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px → 0)` | Opacity fade at `{motion.duration-reduced}`; no travel. Dismiss timing is unchanged. |
| Toast (exit) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform: translateY(0 → 8px)` | Opacity fade at `{motion.duration-reduced}`; no travel. |
| List enter (vehicle grid, configurator rows) | `{motion.duration-base}` per item, `{motion.stagger-step}` between items, capped at 6 items | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px → 0)` | All items fade in together at `{motion.duration-reduced}`; stagger and travel removed. |
| List exit (filter change) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` only | Items are removed with an opacity fade at `{motion.duration-reduced}`. |
| Loading (indeterminate bar) | `{motion.duration-emphasis}` loop, infinite while pending | `{motion.ease-standard}` | `transform: translateX()` of a 2px `{colors.primary}` bar — never `width` | Travel frozen; the bar holds static and pulses `opacity` 1 → 0.5 at `{motion.duration-reduced}`. |
| Loading (skeleton card) | `{motion.duration-emphasis}` loop, infinite while pending | `{motion.ease-standard}` | `opacity` pulse on `{colors.surface-soft}` blocks — no sweeping gradient | Opacity pulse held at `{motion.duration-reduced}`; no sweep. |

Rules this file holds itself to, beyond the table:

- `transform` and `opacity` only. Width, height, top, left and margin are never
  animated — a growing underline is `scaleX`, a loading bar is `translateX`,
  and a hovering photo scales inside a frame whose own box is fixed.
- Every exit is shorter than its matching entrance (modal 240ms out against
  400ms in; dropdown 120ms against 240ms; page 400ms against 600ms).
- Nothing on first paint delays content. The hero's 900ms reveal runs on an
  element that is already laid out and already legible.
- The only infinite animations are the two loaders above. The R5 and E-TECH
  atmospheric gradients are **static images, not ambience** — this brand has no
  looping decorative motion, and none should be added.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translateX/Y) and all scale — hover photo zoom,
     the hero's 1.06 → 1 reveal, press scale, drawer slide, toast rise,
     list stagger, and the loading bar's translateX.
     Kept: opacity fades, at {motion.duration-reduced} (150ms) and never
     longer, whatever this profile's own 240ms duration-fast says; the
     focus-visible ring, which appears instantly and is never suppressed;
     and every colour and border state change, applied with no transition.
     Frozen: the loaders keep an opacity pulse but no travel; there is no
     brand ambience to freeze. */
  *, *::before, *::after {
    animation-duration: 150ms !important;
    animation-delay: 0ms !important;
    transition-duration: 150ms !important;
    transition-property: opacity, background-color, border-color, color !important;
  }
}
```

## Accessibility

Every ratio below is computed from this file's own frontmatter hexes with the
WCAG 2.1 relative-luminance formula. Nothing here was measured on a rendered
page: overlap, clipping and real tap-target sizes are outside what this
document can verify, so the tap-target notes state declared token values only.

### Measured contrast — key pairs

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#000000` on `{colors.canvas}` `#ffffff` | 21.00:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-soft}` `#f7f7f7` | 19.60:1 | 4.5:1 | Pass |
| `{colors.body}` `#222222` on `{colors.canvas}` | 15.91:1 | 4.5:1 | Pass |
| `{colors.charcoal}` `#333333` on `{colors.canvas}` | 12.63:1 | 4.5:1 | Pass |
| `{colors.mute}` `#666666` on `{colors.canvas}` | 5.74:1 | 4.5:1 | Pass — this is the system's secondary/muted ink. |
| `{colors.mute}` on `{colors.surface-soft}` | 5.36:1 | 4.5:1 | Pass |
| `{colors.on-dark}` `#ffffff` on `{colors.surface-dark}` `#000000` | 21.00:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.surface-deep}` `#111111` | 18.88:1 | 4.5:1 | Pass |
| `{colors.on-dark-mute}` (composites to `#b8b8b8`) on `{colors.surface-dark}` | 10.59:1 | 4.5:1 | Pass |
| `{colors.on-primary}` `#000000` on `{colors.primary}` `#ffed00` | 17.37:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary-deep}` `#e6d200` | 13.58:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` `#000000` on `{colors.canvas}` | 21.00:1 | 3.0:1 | Pass — the file's real component boundary. |
| `{colors.link}` `#0000ee` on `{colors.canvas}` | 9.40:1 | 4.5:1 | Pass |
| `{colors.info}` `#337ab7` on `{colors.canvas}` | 4.56:1 | 4.5:1 | Pass, with no margin. |

### Measured contrast — real failures, disclosed

These are extracted values. They are frozen, not corrected: the document's job
is to describe the brand accurately, and a falsified hex would make it wrong.
Each line below is the honest statement that the real brand fails WCAG AA at
that point.

| Foreground / Background | Ratio | Required | Verdict and scope |
|---|---|---|---|
| `{colors.hairline}` `#f2f2f2` on `{colors.canvas}` `#ffffff` | 1.12:1 | 3.0:1 | **Fail.** Decoration only. This tone is a catalogue rhythm line between configurator rows and under the nav bar, not a component boundary. Where a boundary carries meaning — an input edge, a card outline, a focus ring — the file already owns `{colors.hairline-strong}` at 21.00:1, and that is the token to use. No new token was added for this; the palette already contains the passing tone. |
| `{colors.hairline}` on `{colors.surface-soft}` `#f7f7f7` | 1.04:1 | 3.0:1 | **Fail**, and effectively invisible. `{colors.hairline}` must not be used as a divider inside a `{colors.surface-soft}` band; `{colors.stone}` `#c4c4c4` does not rescue it either, at 1.63:1 on that band. Use `{colors.mute}` `#666666` (5.36:1) for a quiet but visible rule, or `{colors.hairline-strong}` where the boundary matters. |
| `{colors.error}` `#be6464` on `{colors.canvas}` | 4.04:1 | 4.5:1 | **Fail** as body-size text — the brand's muted red misses AA by a small margin. It clears 3.0:1, so it is defensible on text at 18px+ / 14px bold and on non-text boundaries such as the `{component.text-input}` error border. Inline error *messages* at `{typography.body-sm}` (14px / 400) do not clear AA with this hex. Never the only cue: pair with an icon and text. |
| `{colors.warning}` `#f0ad4e` on `{colors.canvas}` | 1.95:1 | 4.5:1 | **Fail**, and it also misses 3.0:1, so it is unusable as text or as a boundary on white at any size. Use it as a fill behind `{colors.ink}` text (`#000000` on `#f0ad4e` measures 10.79:1), which is how amber appears in the chips. |
| `{colors.success}` `#8dc572` on `{colors.canvas}` | 2.03:1 | 4.5:1 | **Fail**, and below 3.0:1 as well. Same rule: a fill carrying `{colors.ink}`, never green type on white. |
| `{colors.ash}` `#8a8a8a` on `{colors.canvas}` | 3.45:1 | 4.5:1 | **Fail** as text. Scoped to placeholder and disabled labels, which WCAG exempts for disabled controls — but a placeholder is not disabled text, so any placeholder carrying real instruction must use `{colors.mute}` at 5.74:1. |
| `{colors.stone}` `#c4c4c4` on `{colors.canvas}` | 1.74:1 | 4.5:1 | **Fail** as text, and intentionally so: this is the disabled-state foreground, which WCAG sets no requirement on. Do not use it for live text. |
| `{colors.divider-dark}` (composites to `#292929`) on `{colors.surface-dark}` | 1.44:1 | 3.0:1 | **Fail.** Decoration only — the footer's column rule. On dark surfaces, a boundary that carries meaning uses `{colors.on-dark}` or `{colors.on-dark-mute}`. |

### Focus ring

The file previously defined no focus ring; two are now declared, because the
system has two real polarities — a white browsing canvas and a black
storytelling canvas — and no single tone clears 3:1 on both while still
reading as Renault. **Neither is a new brand colour:** `{colors.focus}` reuses
`{colors.ink}` `#000000` and `{colors.focus-on-dark}` reuses `{colors.primary}`
`#ffed00`, the two values the brand already treats as structural.

Both rings are drawn **outside** the control, with a 2px offset (3px on
`{component.configurator-swatch}`), so each is judged against the surface
behind the control rather than the control's own fill — which is what WCAG 2.2
Focus Appearance asks for, and the only arithmetically possible answer when the
same ring must sit beside a `#ffed00` CTA and on a `#ffffff` page.

| Ring | Surface it is drawn on | Ratio | Required | Verdict |
|---|---|---|---|---|
| `{colors.focus}` `#000000` | `{colors.canvas}` `#ffffff` | 21.00:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.surface-soft}` `#f7f7f7` | 19.60:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.primary}` `#ffed00` tile | 17.37:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` `#ffed00` | `{colors.surface-dark}` `#000000` | 17.37:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` | `{colors.surface-deep}` `#111111` | 15.62:1 | 3.0:1 | Pass |

`{colors.focus-on-dark}` measures 1.21:1 on `{colors.canvas}` and
`{colors.focus}` measures 1.00:1 on `{colors.surface-dark}`: each ring covers
one polarity only, and the pair is a system. Use `{colors.focus}` on
`{colors.canvas}`, `{colors.surface-soft}`, `{colors.surface-card}` and yellow
tiles; use `{colors.focus-on-dark}` on `{colors.surface-dark}`,
`{colors.surface-deep}` and the footer. Over the R5 / E-TECH atmospheric
gradients, which have no single measurable colour, draw `{colors.focus}` with a
1px `{colors.on-dark}` outer edge so one of the two bands always separates from
the backdrop.

The ring is never the only focus cue on an input: `{component.text-input}`
pairs it with a bottom border that steps from 1px to 2px, so focus survives
forced-colours mode.

### Non-colour cues

- `{colors.primary}` is never the only carrier of meaning. A selected
  `{component.configurator-swatch}` also gains a ring and a text label; a
  selected `{component.sub-nav-pill}` also inverts its fill and sets
  `aria-current`.
- Error, warning and success all pair a colour with an icon and with text,
  which is required here rather than merely good practice, given the measured
  failures above.
- Links inside body copy inherit `{colors.ink}` and rely on underline and
  weight rather than colour, so the 9.40:1 `{colors.link}` fallback is not
  load-bearing.

### Tap targets (declared values, not rendered measurements)

- `{component.button-primary}` declares `height: 48px`, and
  `{component.text-input}` 48px — both clear the 44px minimum.
- `{component.button-icon-square}` declares 40px, which is **below the 44px
  minimum** this document should hold itself to. The Responsive Behavior
  section already says it should grow to 44px as a primary navigation control;
  it should grow to 44px everywhere.
- `{component.button-pill}` declares 36px, bumped to 40px on mobile per
  Responsive Behavior — still short of 44px. Treat 44px as the floor for both.
- `{component.configurator-swatch}` at 56px clears it comfortably.
- Whether any of these overlap, clip or shift on a real page cannot be
  determined from this document.

### Reduced motion

Every animation in Motion & Animation respects
`@media (prefers-reduced-motion: reduce)`, which removes all travel and scale,
holds opacity fades at `{motion.duration-reduced}` (150ms) and never longer,
and freezes the two loaders' travel while keeping their opacity pulse. The
focus ring is never suppressed by it.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` exclusively for primary CTAs, "yeni"/"NEW" badges, and at most one accent promo tile per band — `{component.promo-tile-yellow}` is intentionally rare.
- Pair `{colors.primary}` only with `{colors.on-primary}` text. Yellow + white is forbidden.
- Set everything in **NouvelR** — no secondary serif, no script, no decorative italic.
- Hold display headlines at `{typography.display-xl}` weight 700 with `lineHeight: 0.95` so they stack tightly on multi-line wraps.
- Use `{rounded.xs}` (2px) on every standard button — the near-flat corner is part of the brand.
- Switch full bands between `{colors.canvas}` and `{colors.surface-dark}` for storytelling rhythm. Avoid mid-greys as section backgrounds.
- Show vehicle photography full-bleed inside `{component.vehicle-card}` with copy stacked beneath, never overlaid.
- Use `{component.sub-nav-pill}` (`{rounded.pill}`) only for sub-nav and small filter rows — never for primary CTAs.

### Don't
- Don't introduce a secondary accent colour. Yellow is the only brand accent; semantic colours (`{colors.error}`, `{colors.success}`, `{colors.warning}`) are functional, not decorative.
- Don't round vehicle cards or promo tiles. Square-cornered photography is core to the brand expression.
- Don't soften body weights to 500 or 600 — the system relies on the 400 / 700 contrast.
- Don't apply `{colors.primary}` to body text or large surfaces beyond the single accent tile per band.
- Don't add atmospheric gradient washes outside the dedicated R5 / E-TECH hero contexts.
- Don't pair light grey text on white. Body text steps through `{colors.body}`, `{colors.charcoal}`, `{colors.mute}` — `{colors.ash}` and `{colors.stone}` are reserved for placeholders and disabled states.
- Don't add drop shadows to vehicle cards or promo tiles — the system is shadow-free at the catalogue level.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop XL | ≥ 1440px | Full max-width container, 3–4 column vehicle grid, 2-up promo tile grid. |
| Desktop | 1280–1439px | Same layout, container shrinks to viewport with `{spacing.xl}` side padding. |
| Tablet Large | 1024–1279px | Vehicle grid drops to 3-up, configurator left/right panes resize to 55/45. |
| Tablet | 768–1023px | Promo tile grid collapses to 2-up, sub-nav pills become horizontal scroll. |
| Mobile Large | 426–767px | Vehicle grid 2-up, configurator switches to stacked panes (visualisation on top, options below), nav collapses to hamburger. |
| Mobile | ≤ 425px | All grids 1-up, hero `{typography.display-xl}` clamps to ~40px, section padding `{spacing.section}` collapses to `{spacing.xxxl}`. |

### Touch Targets
- All buttons ship at minimum 44×44px on mobile; default `{component.button-primary}` is 48px tall, comfortably exceeding WCAG AAA.
- `{component.sub-nav-pill}` (36px) is bumped to 40px tall on mobile via increased vertical padding.
- `{component.button-icon-square}` (40px) sits at the WCAG AA minimum and remains tappable, but should grow to 44px when used as a primary navigation control.

### Collapsing Strategy
- Top-level nav collapses to hamburger at < 1024px; the logo and login icon stay anchored.
- 2-up promo grid collapses to 1-up at < 768px; tile padding shrinks from `{spacing.xxl}` to `{spacing.lg}`.
- Configurator switches from side-by-side to stacked at < 1024px, with the visualisation pinned to the top of the viewport on scroll.
- Display headlines clamp: `{typography.display-xl}` 56px → 40px → 32px across the breakpoint ladder.
- Sub-nav pills convert from a wrap row to a horizontal scroll-rail at < 768px.

### Image Behavior
- Vehicle photography is served at 1.5× and 2× DPR; below 768px, the system swaps to a portrait-oriented composition where art direction allows.
- Hero atmospheric gradients (R5, E-TECH) load lazily after primary content; they are not blocking.
- Lifestyle / commercial photography in `{component.promo-tile-dark}` keeps the same 16:9 framing across breakpoints, cropping inward rather than letterboxing.

## Iteration Guide

1. Focus on ONE component at a time. Most components share `{rounded.xs}`, `{colors.canvas}` / `{colors.surface-dark}`, and NouvelR — only the role-specific tokens (`{colors.primary}`, `{component.promo-tile-yellow}`) shift between variants.
2. Reference component names and tokens directly (`{colors.primary}`, `{component.button-primary-pressed}`, `{rounded.pill}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits; the orphaned-tokens warning will catch unused entries before they ship.
4. Add new variants as separate entries (`-pressed`, `-disabled`, `-outline`) — do not bury them in prose.
5. Default body type to `{typography.body-md}`; reach for `{typography.subtitle}` only on hero subtitles and lead paragraphs.
6. Keep `{colors.primary}` scarce — if more than one yellow element appears per viewport, ask whether one of them should drop to `{colors.surface-dark}` or `{colors.canvas}` instead.

## Known Gaps

- Active/pressed visual states are not consistently observable in static surfaces; `button-primary-pressed` documents the extracted darkened-yellow value, but no other component has a pressed variant promoted to the YAML.
- Drop-shadow values exist in the extracted tokens but are rarely surfaced visually; only the configurator's sticky summary bar uses them on the captured pages.
- The MyRenault application surfaces (logged-in product) are out of scope for this extraction — only the public marketing canvas is documented.
- Form-field focus styling is not extracted; the system likely relies on a thicker bottom border at `{colors.ink}`, but this is not visually confirmed on the captured pages. `{colors.focus}` and `{colors.focus-on-dark}` are therefore **prescribed**, not extracted — each reuses an existing palette value (`{colors.ink}`, `{colors.primary}`) rather than introducing a colour the brand does not use.
- The entire Motion & Animation section is **prescribed** from the audit spec's Cinematic profile. No duration, easing or stagger on this site was measured; the real site's timing functions are unknown.
- Every state treatment in Components except default and `button-primary-pressed` is **prescribed** from the brand's own tokens. The captured pages are static, so hover, focus-visible, disabled, loading, selected and error renderings could not be observed.
- No shadow tokens exist in the frontmatter. The prose records an approximate elevation (~10% opacity, 2–4px blur) on the configurator's sticky summary bar, but no exact offset, blur, spread or colour was captured, so no `shadow:` group was invented to hold them.
- Renault's real site may define a mid-grey band as a section background; none was captured, so the file documents only the white / black / yellow rhythm. If such a surface exists, the focus-ring pair would need re-checking against it.
