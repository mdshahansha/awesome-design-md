---
version: alpha
name: IBM-design-analysis
description: "An enterprise-marketing canvas faithful to Carbon Design System: white surfaces, charcoal type, IBM Blue (#0f62fe) as the single confident accent, and a deliberately flat-square aesthetic where corners stay at 0–4px. Type runs IBM Plex Sans at light weight 300 for display sizes (a brand signature) and 400/600 for body and emphasis. Cards live as thin-bordered tiles with no shadow; sections separate via subtle gray rows. The chrome is square, the typography is light, and the only color in the system is one assertive blue — the result reads as old-world enterprise gravitas reframed for the cloud era."

colors:
  primary: "#0f62fe"
  on-primary: "#ffffff"
  ink: "#161616"
  ink-muted: "#525252"
  ink-subtle: "#8c8c8c"
  text-secondary: "#525252"   # Carbon $text-secondary — same value as ink-muted, named for the secondary-text role
  canvas: "#ffffff"
  surface: "#f4f4f4"          # Carbon layer-01 — same value as surface-1, named for the raised-surface role
  surface-1: "#f4f4f4"
  surface-2: "#e0e0e0"
  inverse-canvas: "#161616"
  inverse-surface-1: "#262626"
  inverse-ink: "#ffffff"
  inverse-ink-muted: "#c6c6c6"
  hairline: "#e0e0e0"
  hairline-strong: "#161616"
  focus: "#0f62fe"            # Carbon $focus — the 2px ring already described in Elevation level 3
  focus-inset: "#ffffff"      # Carbon $focus-inset — 1px inner band so the ring separates from a blue fill
  focus-on-dark: "#ffffff"    # Carbon $focus-inverse — ring drawn on the charcoal footer
  blue-60: "#0043ce"
  blue-80: "#002d9c"
  blue-hover: "#0050e6"
  semantic-success: "#24a148"
  semantic-warning: "#f1c21b"
  semantic-error: "#da1e28"
  semantic-info: "#0f62fe"

typography:
  display-xl:
    fontFamily: IBM Plex Sans
    fontSize: 76px
    fontWeight: 300
    lineHeight: 1.17
    letterSpacing: -0.5px
  display-lg:
    fontFamily: IBM Plex Sans
    fontSize: 60px
    fontWeight: 300
    lineHeight: 1.17
    letterSpacing: -0.4px
  display-md:
    fontFamily: IBM Plex Sans
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.20
    letterSpacing: 0
  headline:
    fontFamily: IBM Plex Sans
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  card-title:
    fontFamily: IBM Plex Sans
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  subhead:
    fontFamily: IBM Plex Sans
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0
  body-lg:
    fontFamily: IBM Plex Sans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body:
    fontFamily: IBM Plex Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.16px
  body-sm:
    fontFamily: IBM Plex Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.16px
  body-emphasis:
    fontFamily: IBM Plex Sans
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.16px
  caption:
    fontFamily: IBM Plex Sans
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.32px
  button:
    fontFamily: IBM Plex Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.16px
  eyebrow:
    fontFamily: IBM Plex Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.16px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

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
    rounded: "{rounded.none}"
    padding: 12px 16px
  button-primary-pressed:
    backgroundColor: "{colors.blue-80}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  button-ghost:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  button-danger:
    backgroundColor: "{colors.semantic-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  feature-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 24px
  feature-card-elevated:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 24px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 32px
  hero-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.none}"
    padding: 48px
  cta-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.headline}"
    rounded: "{rounded.none}"
    padding: 48px
  text-input:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 11px 16px
  text-input-focused:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 11px 16px
  text-input-error:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 11px 16px
  newsletter-input:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 11px 16px
  product-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 16px 20px
  product-tab-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-emphasis}"
    rounded: "{rounded.none}"
    padding: 16px 20px
  resource-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 16px
  customer-logo-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 24px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 48px
  utility-bar:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    height: 32px
  footer:
    backgroundColor: "{colors.inverse-canvas}"
    textColor: "{colors.inverse-ink-muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 64px 32px
---

## Overview

IBM's marketing system is a faithful application of **Carbon Design System** — IBM's open-source enterprise design system. The dominant surface is `{colors.canvas}` pure white with `{colors.surface-1}` light gray for elevation, charcoal `{colors.ink}` (#161616) for text, and IBM Blue `{colors.primary}` (#0f62fe) as the single brand accent.

The defining choice is **flat geometry**: every CTA, every card, every input, every container uses square corners (`{rounded.none}` 0px) with thin 1px borders. There are no rounded pills, no soft shadows, no atmospheric gradients. The system is engineered, not stylized.

**IBM Plex Sans** carries the entire type hierarchy. Display sizes (76 / 60 / 42px) run at weight **300** — IBM's signature light display treatment that makes 76px feel calmer than competing brands' 700-weight display. Body type sits at weight 400 with `letter-spacing: 0.16px` (a Carbon precision detail) and line-height 1.50. The voice reads as careful, technical, and trustworthy.

The system reaches for color rarely — IBM Blue marks links, primary CTAs, and the rare full-bleed CTA banner. Charcoal carries every other surface that isn't white. The result is enterprise gravitas without the enterprise stiffness: rigorous, light-weighted, and intentionally restrained.

**Key Characteristics:**
- **Carbon Design System** — IBM's marketing chrome IS Carbon. Buttons are square, inputs are square-with-bottom-rule, corners stay at 0px.
- **Light-weight display type**: Plex Sans at weight 300 for 42–76px headlines is the brand's typographic signature.
- **One accent color**: `{colors.primary}` IBM Blue carries every link, primary CTA, and CTA banner. There is no second brand color.
- White canvas + light gray (`{colors.surface-1}`) + charcoal (`{colors.ink}`) cover 95% of surfaces.
- Footer inverts to charcoal (`{colors.inverse-canvas}` #161616) — the only dark surface above the page break.
- Card hierarchy is carried by 1px hairlines and surface change, never by drop shadow.
- `letter-spacing: 0.16px` on body is a Carbon precision detail — the small positive tracking is part of the brand voice.
- Page rhythm: utility bar → top nav → hero with light-weight headline → feature card grid → customer logo marquee → enterprise feature row → training section → newsletter / sign-in CTA → dark footer.

## Colors

> Source pages: ibm.com (home), /software/ai-productivity, /consulting, /products/cloud-pak-for-aiops, /products/bare-metal-servers, community.ibm.com.

### Brand & Accent
- **IBM Blue** ({colors.primary}): The single brand accent. Links, primary CTAs, CTA banner backgrounds, focus rings.
- **Blue 60** ({colors.blue-60}): Hovered link state.
- **Blue 80** ({colors.blue-80}): Pressed primary button.
- **Blue Hover** ({colors.blue-hover}): Hover state for primary buttons.

### Surface
- **Canvas** ({colors.canvas}): Default page background.
- **Surface** ({colors.surface}): The raised-surface role. Same value as `{colors.surface-1}`; Carbon names it `layer-01`.
- **Surface 1** ({colors.surface-1}): Light gray (#f4f4f4) — input fields, alternate-row stripes, subtle section bands.
- **Surface 2** ({colors.surface-2}): Slightly darker gray (#e0e0e0) — disabled fields, hairline-as-fill for separators.
- **Hairline** ({colors.hairline}): 1px **decorative** borders on cards, dividers and logo tiles. It measures 1.32:1 on {colors.canvas} and does not meet the 3:1 non-text threshold — where a 1px rule is the *only* boundary of an interactive control, use `{colors.hairline-strong}` instead. See Accessibility.
- **Hairline Strong** ({colors.hairline-strong}): 1px charcoal — the control boundary, and the underline on focused inputs (Carbon's signature focus treatment). 18.1:1 on {colors.canvas}.
- **Inverse Canvas** ({colors.inverse-canvas}): Charcoal #161616 — footer surface.
- **Inverse Surface 1** ({colors.inverse-surface-1}): One step lighter than inverse canvas — footer column dividers, hovered footer items.

### Text
- **Ink** ({colors.ink}): All headlines and emphasized body type — charcoal #161616.
- **Ink Muted** ({colors.ink-muted}): Secondary type at #525252 — meta, sub-headlines, footer body. Also exposed as `{colors.text-secondary}`, Carbon's own name for this role.
- **Ink Subtle** ({colors.ink-subtle}): Tertiary type at #8c8c8c — **disabled text and decorative labels only**. It measures 3.36:1 on {colors.canvas} and fails AA for body copy, so helper text and captions that must be read take `{colors.ink-muted}` (7.81:1). See Accessibility.
- **Inverse Ink** ({colors.inverse-ink}): White on charcoal — footer headings.
- **Inverse Ink Muted** ({colors.inverse-ink-muted}): Light gray on charcoal — footer body.

### Focus

Carbon publishes a real focus ring, and this file already described it in Elevation level 3; these tokens name it rather than invent it.

- **Focus** ({colors.focus}): IBM Blue, identical to {colors.primary}. Drawn as a 2px outline with a 1px offset. 5.0:1 on {colors.canvas}, 4.55:1 on {colors.surface}, 3.79:1 on {colors.surface-2}.
- **Focus Inset** ({colors.focus-inset}): 1px white inner band, drawn only where the ring lands on a blue or charcoal fill (primary and secondary buttons, the {components.cta-banner} CTA). The two bands separate at 5.0:1.
- **Focus On Dark** ({colors.focus-on-dark}): White ring for the inverted footer — 18.1:1 on {colors.inverse-canvas}, 15.13:1 on {colors.inverse-surface-1}.

### Semantic
- **Success Green** ({colors.semantic-success}): Carbon green-50 — success **fills and icons only**, 3.35:1 on {colors.canvas}. Success *text* takes {colors.ink}.
- **Warning Yellow** ({colors.semantic-warning}): Carbon yellow-30 — warning fills only, 1.68:1 on {colors.canvas}. Carbon pairs it with {colors.ink} type on top (10.75:1); never use it as a text colour.
- **Error Red** ({colors.semantic-error}): Carbon red-60 — error states; danger button background.
- **Info Blue** ({colors.semantic-info}): Identical to primary — informational badges.

## Typography

### Font Family

- **IBM Plex Sans** — IBM's open-source proprietary typeface (free for any use). Geometric, slightly humanist, designed specifically for enterprise UI. Fallback: `Helvetica Neue, Arial, sans-serif`.

The same family carries display, body, and caption — there is no display + body pairing. Hierarchy is carried by **size + weight** rather than by family change. Plex Sans is also free / open-source under the SIL Open Font License — making it the easiest custom face on this list to substitute for in implementation.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 76px | 300 | 1.17 | -0.5px | Largest hero headline |
| `{typography.display-lg}` | 60px | 300 | 1.17 | -0.4px | Section opener headlines |
| `{typography.display-md}` | 42px | 300 | 1.20 | 0 | Sub-section headlines, hero card title |
| `{typography.headline}` | 32px | 400 | 1.25 | 0 | Card collection heading, FAQ category |
| `{typography.card-title}` | 24px | 400 | 1.33 | 0 | Feature card title |
| `{typography.subhead}` | 20px | 400 | 1.40 | 0 | Lead body next to display headlines |
| `{typography.body-lg}` | 18px | 400 | 1.50 | 0 | Hero subhead, lead paragraphs |
| `{typography.body}` | 16px | 400 | 1.50 | 0.16px | Default body |
| `{typography.body-sm}` | 14px | 400 | 1.29 | 0.16px | Card body, footer columns |
| `{typography.body-emphasis}` | 14px | 600 | 1.29 | 0.16px | Selected tab label, emphasized body line |
| `{typography.caption}` | 12px | 400 | 1.33 | 0.32px | Captions, meta, utility bar |
| `{typography.button}` | 14px | 400 | 1.29 | 0.16px | All button labels |
| `{typography.eyebrow}` | 14px | 400 | 1.29 | 0.16px | Section eyebrows (Carbon avoids strong eyebrows; uses sentence case 14px) |

### Principles

- **Light-weight display is the brand voice.** Plex Sans at weight 300 for 76px headlines reads as quietly authoritative — switching to 700 would make it look like every other enterprise site.
- **Carbon's `letter-spacing: 0.16px`** on body sizes is a precision detail. Don't remove it.
- **No mono** on marketing surfaces (Plex Mono exists but lives in product surfaces only).
- **Eyebrow typography uses sentence case 14px** — Carbon resists the all-caps tracked eyebrow common to other enterprise brands.
- **Line-heights tighten on display, relax on body**: 1.17 at display-xl, 1.50 at body — proportional to size.

### Note on Font Substitutes

IBM Plex Sans is **free and open-source** (SIL OFL license) and available on Google Fonts. It is the recommended implementation. The Plex family also includes Plex Mono and Plex Serif if expanded typographic needs arise.

## Layout

### Spacing System

- **Base unit**: 4px (Carbon's signature 4-pixel grid).
- **Tokens (front matter)**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- Card interior padding: `{spacing.lg}` 24px on feature cards; `{spacing.xl}` 32px on product cards; `{spacing.xxl}` 48px on hero cards and CTA banners.
- Button padding: 12px vertical · 16px horizontal — Carbon spec.
- Form input padding: 11px vertical · 16px horizontal.

### Grid & Container

- Carbon's 16-column grid at desktop, scaling to 8 / 4 columns at tablet / mobile.
- Max content width sits around 1584px (Carbon's max-grid breakpoint).
- Card grids are 4-up at desktop, 2-up at tablet, 1-up at mobile.
- The customer logo marquee uses fixed-width tiles in a flex row, scrolling horizontally on smaller viewports.

### Whitespace Philosophy

Carbon uses precise alignment to a 4-pixel grid as its whitespace system. Sections separate via thin gray rows (`{colors.surface-1}`) rather than via large vertical gaps. Content is dense by design — IBM's customers expect to see a lot on a page, not a lot of air.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Default for body type, hero text, footer body |
| 1 (hairline) | 1px `{colors.hairline}` border on canvas | Feature cards, inputs, list items |
| 2 (surface lift) | `{colors.surface-1}` background on canvas | Alternate-row banners, hovered cards |
| 3 (focus ring) | 2px `{colors.focus}` outline + 1px `{colors.focus-inset}` inner band; focused inputs keep the 1px `{colors.hairline-strong}` underline | Focused input, focused button |

Carbon resists drop shadows on marketing — depth is carried by surface change and 1px hairlines. The exception is product / app surfaces (Carbon documents shadow tokens for elevated panels), but the marketing site barely uses them.

### Decorative Depth

- **Soft blue gradient backdrops** appear behind some hero illustrations — a faint blue-to-white wash that warms the canvas without competing with the headline.
- **No atmospheric depth.** No spotlight cards, no pastel section blocks, no gradient panels.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Default — every button, card, input, container |
| `{rounded.xs}` | 2px | Small badges (rare exception) |
| `{rounded.sm}` | 4px | Avatar circles squared, dropdown menus |
| `{rounded.md}` | 6px | (Used rarely; documented for completeness) |
| `{rounded.lg}` | 8px | (Used rarely; documented for completeness) |
| `{rounded.pill}` | 9999px | Status pills, badges in product UI (rare on marketing) |

The brand commits to flat 0px corners. The other tokens exist for product / mobile surfaces but rarely surface on marketing.

### Photography & Illustration Geometry

- IBM uses photography (people, hardware, sports cars) and abstract illustration (geometric mesh, dotted patterns) interchangeably.
- Image frames are flat — no rounded corners.
- Customer logo tiles sit on `{rounded.none}` 0px tiles with thin 1px borders.

## Components

### Buttons

**`button-primary`** — Blue solid CTA. The default primary across all pages.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}`, padding 12px 16px, rounded `{rounded.none}`.
- Pressed state lives in `button-primary-pressed` (background shifts to `{colors.blue-80}`).
- States: default · hover `{colors.blue-hover}` · focus-visible 2px `{colors.focus}` ring with a 1px `{colors.focus-inset}` inner band · active/pressed `{colors.blue-80}` · disabled `{colors.surface-2}` fill with `{colors.ink-subtle}` label · loading, label swaps for an inline Carbon spinner and the button keeps its width · error is not a button state here; the adjacent field carries it.

**`button-secondary`** — Charcoal solid button — Carbon's "secondary" treatment.
- Background `{colors.ink}`, text `{colors.inverse-ink}`, type `{typography.button}`, padding 12px 16px, rounded `{rounded.none}`.
- States: default · hover `{colors.inverse-surface-1}` · focus-visible 2px `{colors.focus}` ring with a 1px `{colors.focus-inset}` inner band (the charcoal fill needs the inner band) · active/pressed back to `{colors.ink}` · disabled `{colors.surface-2}` with `{colors.ink-subtle}` label · loading inline spinner · no selected or error state.

**`button-tertiary`** — White button with blue 1px border + blue text. Used for tertiary CTAs.
- Background `{colors.canvas}`, text `{colors.primary}`, type `{typography.button}`, rounded `{rounded.none}`, padding 12px 16px. (Border in implementation: 1px `{colors.primary}`.)
- States: default · hover `{colors.surface}` fill · focus-visible 2px `{colors.focus}` ring · active/pressed `{colors.surface-2}` fill · disabled 1px `{colors.surface-2}` border with `{colors.ink-subtle}` label · loading inline spinner · no selected or error state.

**`button-ghost`** — Plain text + chevron, no background until hover.
- Background `{colors.canvas}`, text `{colors.primary}`, type `{typography.button}`, rounded `{rounded.none}`, padding 12px 16px.
- States: default · hover `{colors.surface}` fill and the chevron shifts 4px right · focus-visible 2px `{colors.focus}` ring · active/pressed `{colors.surface-2}` fill · disabled `{colors.ink-subtle}` label · no loading, selected or error state.

**`button-danger`** — Carbon's destructive variant.
- Background `{colors.semantic-error}`, text `{colors.on-primary}`, type `{typography.button}`, rounded `{rounded.none}`, padding 12px 16px.
- States: default · hover darkens one Carbon step · focus-visible 2px `{colors.focus}` ring with a 1px `{colors.focus-inset}` inner band · active/pressed darkens two steps · disabled `{colors.surface-2}` with `{colors.ink-subtle}` label · loading inline spinner · no selected state.

### Cards & Containers

**`feature-card`** — Default feature highlight tile on the home and product pages.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.none}`, padding 24px. Stroked with 1px `{colors.hairline-strong}` where the whole tile is a link target, 1px `{colors.hairline}` where it is static.
- States: default · hover lifts to `{colors.surface}` · focus-visible 2px `{colors.focus}` ring on the whole tile · active/pressed `{colors.surface-2}` · selected is not a card state · disabled, loading (skeleton band on `{colors.surface}`) and error only apply to the data-backed variants in the Recommended carousel.

**`feature-card-elevated`** — Same shape on `{colors.surface-1}` ground — used for "Recommended" cards in the latest-content carousel.
- Background `{colors.surface-1}`, otherwise identical structure.
- States: identical to `feature-card`, except hover lifts to `{colors.canvas}` rather than down to `{colors.surface}`.

**`product-card`** — Larger product showcase tile.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.none}`, padding 32px.
- States: default · hover `{colors.surface}` · focus-visible 2px `{colors.focus}` ring · active/pressed `{colors.surface-2}`. Three states plus focus; no disabled, loading, selected or error.

**`hero-card`** — Hero composition card with light-weight title, body, and CTA.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.display-md}`, rounded `{rounded.none}`, padding 48px.
- States: default only — the hero card is static chrome; its CTA carries the interactive states. No hover, focus-visible, active, disabled, loading, selected or error state on the container itself.

**`cta-banner`** — Full-width blue CTA panel near the bottom of the page.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.headline}`, rounded `{rounded.none}`, padding 48px.
- States: default only on the panel. Its CTA is a `button-secondary` on the blue ground, and its focus-visible ring uses `{colors.focus-inset}` as the outer band because `{colors.focus}` is the same blue as the panel — see Accessibility.

**`resource-tile`** — Smaller article / case-study tile.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-sm}`, rounded `{rounded.none}`, padding 16px.
- States: default · hover `{colors.surface}` · focus-visible 2px `{colors.focus}` ring · active/pressed `{colors.surface-2}` · loading skeleton while the resource feed resolves. No disabled, selected or error.

**`customer-logo-tile`** — Single tile in the customer marquee on the home page (Ferrari, Pfizer, etc.).
- Background `{colors.canvas}`, text `{colors.ink-muted}`, type `{typography.caption}`, rounded `{rounded.none}`, padding 24px. 1px `{colors.hairline}` border — decorative, since the tile is not a control.
- States: default only where the marquee is static; where a tile links to a case study it adds hover `{colors.surface}` and focus-visible 2px `{colors.focus}`. No active, disabled, loading, selected or error state.

### Inputs & Forms

**`text-input`** + **`text-input-focused`** + **`text-input-error`** — Carbon's input chrome.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.none}`, padding 11px 16px.
- Focus state replaces the bottom 1px hairline with a 2px `{colors.primary}` underline (Carbon's signature focus treatment).
- Error state adds 2px `{colors.semantic-error}` bottom underline, plus an error message in `{colors.semantic-error}` at `{typography.body-sm}` (5.0:1 on `{colors.canvas}`).
- States: default (1px `{colors.hairline-strong}` bottom rule) · hover rule darkens to `{colors.ink}` · focus-visible 2px `{colors.focus}` outline on the field box plus the Carbon underline · active/pressed is the same as focus for a text field · disabled `{colors.surface-2}` fill with `{colors.ink-subtle}` text · loading, the field is read-only with a skeleton value · error as above · no selected state.

**`newsletter-input`** — The "Stay connected" newsletter capture on the home page.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.none}`, padding 11px 16px. Adjacent submit is `button-primary`.
- States: inherits every `text-input` state — default, hover, focus-visible, active, disabled, loading, error — and adds a success confirmation that replaces the field with `{colors.ink}` body copy. No selected state.

### Tabs

**`product-tab`** + **`product-tab-selected`** — The horizontal tab strip on product pages and the home "Recommended" carousel.
- Default: `{colors.canvas}` background, `{colors.ink-muted}` text, rounded `{rounded.none}`, padding 16px 20px. Bottom 1px hairline.
- Selected: `{colors.canvas}` background, `{colors.ink}` text, `{typography.body-emphasis}` weight, bottom 2px `{colors.primary}` underline. Same padding / rounding.
- States: default · hover `{colors.surface}` fill with `{colors.ink}` label · focus-visible 2px `{colors.focus}` ring inset 2px from the tab edge · active/pressed `{colors.surface-2}` · selected as above · disabled `{colors.ink-subtle}` label with no underline · loading, the panel below shows a skeleton while the tab's content resolves · no error state.

### Navigation

**`top-nav`** — Sticky white bar with the IBM logomark left, nav categories center, and search / sign-in icons right.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-sm}`, height 48px. 1px bottom hairline.
- States per nav item: default · hover `{colors.surface}` fill · focus-visible 2px `{colors.focus}` ring · active/pressed `{colors.surface-2}` · selected, the current section keeps a 2px `{colors.primary}` bottom rule · no disabled, loading or error state.

**`utility-bar`** — Slim gray ribbon above the top nav with location switch, contact, search shortcuts.
- Background `{colors.surface-1}`, text `{colors.ink-muted}`, type `{typography.caption}`, height 32px.
- States per link: default · hover underline · focus-visible 2px `{colors.focus}` ring. Three states; no active, disabled, loading, selected or error treatment.

### Footer

**`footer`** — Charcoal footer (`{colors.inverse-canvas}`) with the IBM wordmark left and 5–6 columns of caption-sized links. The only inverted surface above the page break.
- Background `{colors.inverse-canvas}`, text `{colors.inverse-ink-muted}`, type `{typography.body-sm}`, padding 64px 32px.
- States per footer link: default `{colors.inverse-ink-muted}` · hover `{colors.inverse-ink}` with underline · focus-visible 2px `{colors.focus-on-dark}` ring, the one place the inverted ring is used · active/pressed `{colors.inverse-surface-1}` fill. No disabled, loading, selected or error state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** Carbon publishes real motion tokens (`$duration-fast-02`, `$duration-moderate-01`, and the `productive` / `expressive` easing curves), and the durations below sit in the same range, but nobody timed ibm.com to produce this table. Treat every value here as a prescription, not an extraction.

Profile: **Calm** — composed and editorial. Short opacity-led fades, little travel. That is the right reading of a brand whose own description is "deliberately flat-square", whose display weight is 300, and which forbids gradients and shadows: the chrome should settle, not bounce. Carbon's own `productive` curve `cubic-bezier(0.2, 0, 0.38, 0.9)` is close in character to `{motion.ease-standard}`.

### Tokens

`{motion.duration-instant}` 80ms · `{motion.duration-fast}` 150ms · `{motion.duration-base}` 250ms · `{motion.duration-slow}` 400ms · `{motion.duration-emphasis}` 500ms · `{motion.ease-standard}` · `{motion.ease-enter}` · `{motion.ease-exit}` · `{motion.stagger-step}` 40ms · `{motion.duration-reduced}` 150ms.

### Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, nav item) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `background-color` | Unchanged — a colour change is not travel |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `background-color` | Unchanged. No scale pop; Carbon's square chrome does not squash |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears instantly at full opacity |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` | Opacity only at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px → 0)` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Dropdown / nav flyout | `{motion.duration-fast}` enter, `{motion.duration-instant}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-4px → 0)` | Travel removed; opacity only |
| Toast / inline notification | `{motion.duration-base}` enter, `{motion.duration-fast}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateX(12px → 0)` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| List / card grid enter | `{motion.duration-base}`, staggered `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px → 0)` | Stagger and travel removed; the grid fades in as one block at `{motion.duration-reduced}` |
| List / card grid exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` | Opacity only at `{motion.duration-reduced}` |
| Loading (Carbon spinner, skeleton band) | 1400ms loop (spinner), `{motion.duration-slow}` loop (skeleton shimmer) | linear | `transform: rotate`, `opacity` | Spinner freezes to a static indeterminate ring; skeleton holds a flat `{colors.surface}` band and the status is announced in text |

### Rules

- Animate `transform` and `opacity` only. Never `width`, `height`, `top`, `left` or `margin` — a square-cornered grid on a 4px baseline shows layout jitter immediately.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content. The hero headline is painted, not revealed; `{motion.duration-emphasis}` is reserved for the one deliberate reveal on a product page's feature row, triggered on scroll, never on load.
- The only infinite animations are the loading indicators above and the customer logo marquee, which is deliberate brand ambience and is stated as such here. Both pause on hover and on focus.
- Carbon's `expressive` register is not used on these pages; this is a productive-motion system throughout.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale travel, the list stagger, the
     logo-marquee ambience, and the skeleton shimmer. */
  *, *::before, *::after {
    transition-duration: 150ms;   /* {motion.duration-reduced} */
    animation-duration: 150ms;
    animation-iteration-count: 1;
    transform: none !important;
  }
  .logo-marquee { animation-play-state: paused; }
}
```

**Removed:** every `transform` — modal rise, dropdown slide, toast slide, card-grid rise — plus the `{motion.stagger-step}` cascade, the marquee scroll and the skeleton shimmer.
**Kept:** opacity fades, capped at `{motion.duration-reduced}` 150ms, and all colour transitions on hover, press and focus. The focus ring still appears instantly. No state change is dropped — only its travel.

## Accessibility

Ratios below are computed from this file's own frontmatter with WCAG 2.1 relative luminance. Everything else here is prescribed: this is a document, so tap-target size, overlap and reading order were not rendered or measured.

### Measured contrast — passes

| Pair | Ratio | Required |
|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 18.1:1 | 4.5:1 |
| `{colors.ink}` on `{colors.surface}` | 16.45:1 | 4.5:1 |
| `{colors.ink-muted}` / `{colors.text-secondary}` on `{colors.canvas}` | 7.81:1 | 4.5:1 |
| `{colors.ink-muted}` on `{colors.surface}` | 7.1:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.primary}` | 5.0:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.blue-hover}` | 6.38:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.blue-80}` | 11.32:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.semantic-error}` | 5.0:1 | 4.5:1 |
| `{colors.hairline-strong}` on `{colors.canvas}` | 18.1:1 | 3.0:1 |
| `{colors.inverse-ink}` on `{colors.inverse-canvas}` | 18.1:1 | 4.5:1 |
| `{colors.inverse-ink-muted}` on `{colors.inverse-canvas}` | 10.59:1 | 4.5:1 |
| `{colors.semantic-error}` on `{colors.canvas}` | 5.0:1 | 4.5:1 |

### Measured contrast — real failures, disclosed

These are extracted Carbon values. They are not corrected here, because changing a brand's real hex would make this document wrong. Each is scoped in the Colors section instead.

- `{colors.hairline}` #e0e0e0 on `{colors.canvas}` measures **1.32:1**, against the 3:1 non-text minimum. Carbon's own hairline fails this threshold. It is decoration here; the control boundary is `{colors.hairline-strong}`.
- `{colors.hairline}` on `{colors.surface}` measures **1.2:1** — worse still. A card on the grey band must be bounded by surface change, not by this rule.
- `{colors.ink-subtle}` #8c8c8c on `{colors.canvas}` measures **3.36:1**, against 4.5:1. The real brand fails AA here for any body or caption text. Scoped to disabled text (where WCAG sets no requirement) and decorative labels; readable helper text takes `{colors.ink-muted}`.
- `{colors.ink-subtle}` on `{colors.surface}` measures **3.06:1**. Same scope, and the reason disabled fields on `{colors.surface-2}` are the only place this pairing is allowed.
- `{colors.semantic-success}` #24a148 on `{colors.canvas}` measures **3.35:1**. Carbon green-50 is a fill and icon colour; as text it fails AA. Success *text* takes `{colors.ink}`.
- `{colors.semantic-warning}` #f1c21b on `{colors.canvas}` measures **1.68:1**. Carbon yellow-30 is a fill only, always carrying `{colors.ink}` type on top at 10.75:1.
- `{colors.focus}` on `{colors.primary}` measures **1.0:1** — the ring and the primary button fill are the same IBM Blue. The ring is never drawn bare on blue: a 1px `{colors.focus-inset}` band separates them at 5.0:1, which is how Carbon solves it. This is a composite-ring requirement, not a passing single-colour pair.

### Focus ring, per surface

| Surface this file defines | Ring token | Measured |
|---|---|---|
| `{colors.canvas}` #ffffff | `{colors.focus}` | 5.0:1 — pass |
| `{colors.surface}` / `{colors.surface-1}` #f4f4f4 | `{colors.focus}` | 4.55:1 — pass |
| `{colors.surface-2}` #e0e0e0 | `{colors.focus}` | 3.79:1 — pass |
| `{colors.primary}` #0f62fe fill | `{colors.focus}` + 1px `{colors.focus-inset}` | 1.0:1 bare; 5.0:1 band-to-ring — composite required |
| `{colors.ink}` / `{colors.inverse-canvas}` #161616 fill | `{colors.focus-on-dark}` | 18.1:1 — pass |
| `{colors.inverse-surface-1}` #262626 | `{colors.focus-on-dark}` | 15.13:1 — pass |

The ring is 2px, offset 1px, and never removed on mouse input — `:focus-visible` only, so it does not fire on click. Over the soft blue hero gradient, which has no single measurable colour, use the composite form: `{colors.focus}` with a 1px `{colors.focus-inset}` outer edge.

### Tap targets

Prescribed, not measured — there is no rendered page here. Carbon's 48px minimum, already recorded under Responsive Behavior, governs: buttons, inputs, tab rows and nav links hold 48px on touch viewports, and the 12px/16px button padding plus `{typography.button}` 14px/1.29 reaches 48px only once that touch minimum is applied. Utility-bar links at `{typography.caption}` 12px in a 32px ribbon are **below** 48px and the ribbon is hidden below 672px for that reason.

### Reduced motion

See Motion & Animation. All travel and stagger are removed, opacity fades cap at `{motion.duration-reduced}` 150ms, and the marquee ambience freezes.

### Other

- Weight 300 at `{typography.display-xl}` 76px is safe; weight 300 must never drop to `{typography.body}` 16px or below, where light strokes thin out for low-vision readers.
- `{colors.primary}` is the only link colour, and links in body copy carry an underline, so colour is not the sole signal.
- Error states pair the `{colors.semantic-error}` underline with text, never colour alone.

## Do's and Don'ts

### Do

- Use `{rounded.none}` 0px on every CTA, card, input, and container. The flat-square aesthetic is the brand.
- Pair Plex Sans weight 300 for display sizes (42px+) with weight 400 for body. Resist the urge to bold the headline.
- Reserve `{colors.primary}` IBM Blue for primary CTAs, links, focused-input underlines, and CTA banner. Do not use it as a card background or eyebrow color.
- Apply `letter-spacing: 0.16px` to body sizes. It's a Carbon precision detail and part of the typographic voice.
- Use surface change (`canvas` → `surface-1`) and 1px hairlines for card hierarchy. Skip drop shadows.
- Stick to sentence case for eyebrows and section labels — Carbon resists all-caps tracking.
- Invert to `{colors.inverse-canvas}` only at the footer; the rest of the page stays light.

### Don't

- Don't round corners on buttons, cards, or inputs. Even 4px rounded corners break the Carbon look.
- Don't bold display headlines. Plex Sans at weight 300 is the brand voice; weight 700 makes it look generic.
- Don't add atmospheric depth (gradient backdrops, drop shadows, atmospheric overlays) outside the documented soft-blue hero gradient.
- Don't introduce a second brand color. IBM Blue is the only chromatic accent; status semantics use the documented green / yellow / red.
- Don't replace IBM Plex Sans with Inter or Helvetica without preserving the `letter-spacing: 0.16px` and weight-300 display treatment.
- Don't animate `width`, `height`, `top`, `left` or `margin`. Carbon's 4px baseline shows layout jitter instantly — move `transform` and `opacity` only.
- Don't use `{colors.ink-subtle}` for text a reader has to read: it measures 3.36:1 on white and fails AA. Use `{colors.ink-muted}`.
- Don't draw `{colors.focus}` bare on a `{colors.primary}` fill — same blue, 1.0:1. Add the 1px `{colors.focus-inset}` band.
- Don't use pill-shaped buttons. Carbon uses square corners; pills read as a different brand.
- Don't write all-caps tracked eyebrows. Carbon's eyebrows are sentence case at 14px.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Max | 1584px | Carbon max grid; gutters expand |
| Desktop-XL | 1312px | Default desktop layout |
| Desktop | 1056px | Card grid 4-up maintained |
| Tablet | 672px | Card grid 4-up → 2-up; nav becomes hamburger |
| Mobile | 320px | Single-column; display-xl scales 76px → ~32px |

### Touch Targets

- Carbon spec: 48px minimum tap target. Buttons and inputs hold 48px on touch viewports.
- Top-nav links grow from 36px to 48px tap height on touch.
- Tab strip rows hold 48px tap height.

### Collapsing Strategy

- **Top nav**: links collapse to a hamburger overlay below 672px. Logomark and search icon stay on the bar.
- **Utility bar**: hides below 672px to reclaim vertical space.
- **Card grid**: 4-up → 2-up at 1056px → 1-up below 672px.
- **Display type**: `{typography.display-xl}` 76px scales toward 42px on mobile while preserving the weight-300 treatment.
- **Footer**: 6-column link grid → 3-column at tablet → 1-column at mobile.

### Image Behavior

- Customer logos in the marquee maintain aspect ratio and may collapse to 2-row scroll below 672px.
- Hero illustrations scale proportionally; below 672px they may stack above the headline rather than sit beside it.

## Iteration Guide

1. Focus on ONE component at a time and reference it by its `components:` token name.
2. Default body to `{typography.body}` at weight 400 with `letter-spacing: 0.16px`. Don't remove the tracking.
3. When introducing a new section, decide whether it sits on `{colors.canvas}` (default) or on `{colors.surface-1}` (alternate band). The two-surface rhythm is the rhythm.
4. Run `npx @google/design.md lint DESIGN.md` after edits.
5. Add new variants as separate component entries (`button-primary-pressed`, `text-input-error`, `text-input-focused`).
6. Treat IBM Blue as scarce: links, primary CTA, CTA banner, focus underline. Anything beyond that is drift.
7. Resist rounded corners. If a designer pushes for 4px rounding, the brand is shifting away from Carbon.

## Known Gaps

- IBM's product surfaces (cloud-pak, watson, datacap) have richer Carbon component usage (data tables, graph cells, breadcrumbs, contextual menus) that aren't present on the marketing pages inspected — those components live in Carbon's documentation rather than in the marketing extraction.
- Form-field error and validation styling is documented in Carbon docs; the inspected pages didn't render error states.
- Dark mode is documented in Carbon as Gray-100 theme but isn't exposed on these marketing pages — only the footer inverts. The full dark theme is a separate Carbon palette not extracted here.
- **Motion is prescribed, not extracted.** No timing function, duration or easing in this file was measured from ibm.com. Carbon publishes real motion tokens and this file's Calm profile sits in the same range, but the exact mapping of Carbon's `$duration-*` tokens to specific marketing interactions is unverified here.
- `{colors.focus}`, `{colors.focus-inset}` and `{colors.focus-on-dark}` carry Carbon's published focus values (`$focus`, `$focus-inset`, `$focus-inverse`); the 2px width, 1px offset and composite behaviour on blue fills are Carbon's documented treatment, matching what this file already described at Elevation level 3. The per-page application was not inspected on every surface.
- Hover, pressed and disabled hexes are documented only where this file already names a token. `button-danger` hover and pressed are described as Carbon steps rather than hexes, because no value for them was extracted.
- Tap-target sizes are quoted from Carbon spec. Nothing in this document was rendered, so no tap target, overlap or reading-order claim here is measured.
- The community.ibm.com sub-domain uses a different chrome (community-platform white-label) that approximates Carbon but isn't strict — the documented system applies to ibm.com proper.
