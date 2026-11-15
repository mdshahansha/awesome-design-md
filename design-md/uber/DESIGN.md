---
version: alpha
name: Uber-Inspired-design-analysis
description: An inspired interpretation of Uber's design language — a transportation-and-delivery super-app brand whose web surface is a black-and-white duet, framed by a custom geometric display sans, accented by a single signature pill shape (radius 999px) on every interactive element, and decorated only by editorial 4:3 illustrations of riders, drivers, and city objects.

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  ink: "#000000"
  body: "#5e5e5e"
  mute: "#afafaf"
  hairline-mid: "#4b4b4b"
  canvas: "#ffffff"
  canvas-soft: "#efefef"
  canvas-softer: "#f3f3f3"
  surface-pressed: "#e2e2e2"
  link: "#0000ee"
  on-dark: "#ffffff"
  black-elevated: "#282828"
  focus: "#000000"
  focus-on-dark: "#ffffff"

shadow:
  level-1: "rgba(0, 0, 0, 0.12) 0px 4px 16px 0px"
  level-2: "rgba(0, 0, 0, 0.16) 0px 4px 16px 0px"
  level-3: "rgba(0, 0, 0, 0.16) 0px 2px 8px 0px"

typography:
  display-xxl:
    fontFamily: UberMove, UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 52px
    fontWeight: 700
    lineHeight: 64px
  display-xl:
    fontFamily: UberMove, UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 36px
    fontWeight: 700
    lineHeight: 44px
  display-lg:
    fontFamily: UberMove, UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
  display-md:
    fontFamily: UberMove, UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 24px
    fontWeight: 700
    lineHeight: 32px
  display-sm:
    fontFamily: UberMove, UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 20px
    fontWeight: 700
    lineHeight: 28px
  body-lg:
    fontFamily: UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 18px
    fontWeight: 500
    lineHeight: 24px
  body-md:
    fontFamily: UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-md-strong:
    fontFamily: UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 20px
  body-sm:
    fontFamily: UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 16px
  caption:
    fontFamily: UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 20px
  button-large:
    fontFamily: UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 18px
    fontWeight: 500
    lineHeight: 24px
  button-md:
    fontFamily: UberMoveText, system-ui, Helvetica Neue, Arial, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 20px

rounded:
  none: 0px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 999px
  pill-tab: 36px
  full: 9999px

spacing:
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px

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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    padding: "{spacing.lg} {spacing.3xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.md}"
  button-subtle:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.lg}"
  button-floating:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md}"
    shadow: "{shadow.level-3}"
  button-large-rounded:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-large}"
    rounded: "{rounded.xl}"
    padding: "{spacing.lg} {spacing.xl}"
  button-tab-translucent:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.pill-tab}"
  text-input:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  text-input-on-soft:
    backgroundColor: "{colors.canvas-softer}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  card-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  card-elevated:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
    shadow: "{shadow.level-1}"
  card-soft-tinted:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  promo-card-illustrated:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  promo-card-on-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  request-form-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.lg}"
    shadow: "{shadow.level-2}"
  request-form-input-row:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  category-button:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.lg}"
  faq-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    padding: "{spacing.lg} 0"
  app-download-pill:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.xl}"
  hero-band-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  hero-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  showcase-image-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xxl}"
    rounded: "{rounded.xl}"
    padding: "{spacing.3xl}"
  link-blue:
    textColor: "{colors.link}"
    typography: "{typography.body-md}"
  link-on-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
  link-mute:
    textColor: "{colors.hairline-mid}"
    typography: "{typography.body-md}"
  link-mute-soft:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.mute}"
    typography: "{typography.body-md}"
  icon-button-circular:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.3xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default tier card. Mirrors card-content chrome with canvas-soft surface and a hairline-mid boundary."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-mid}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  ex-pricing-tier-featured:
    description: "Featured tier — polarity-flipped to ink with white text."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  ex-product-selector:
    description: "Plan picker — re-purposed for the brand's Ride / Eats / Reserve tier picker. Uses category-button pills inside the frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.2xl}"
  ex-cart-drawer:
    description: "Subscription summary — line items per add-on (NOT a literal e-commerce cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
    item-divider: "{colors.hairline-mid}"
  ex-app-shell-row:
    description: "Sidebar nav row. Active state uses brand primary as a left-edge indicator bar."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses body-sm-strong 500 weight; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.body-sm-strong}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline-mid}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Mirrors card-content chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as card-content with Level 2 drop shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame. Generous padding on canvas-soft surface."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — flat-cornered card-content chrome with Level 2 drop shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Uber is a transportation-and-delivery super-app — ride, eats, freight, the whole urban logistics layer — and the brand's web surface signals that scale through restraint: no third colour, no accent palette, no illustration that fights the headline. The page is structurally a black-and-white duet, where black `{colors.primary}` is the conversion anchor (every CTA pill, every nav login button, the footer fill) and `{colors.canvas}` white carries everything else. The only consistent decoration is a body of editorial 4:3 illustrations — riders, drivers, parking lots, cars-on-highway — that ground the marketing without leaking accent colour into the system.

Type is the second decisive voice. Two custom faces carry every page: `UberMove` at weight 700 for headlines (32 – 52 px display sizes with tight 1.22 – 1.25 line-height, never letter-spaced), and `UberMoveText` at weights 400 / 500 for body, button, and link. The pairing reads as engineering-grade — no italic, no decorative weight, no tracking flourish. Headlines are sentence-case; eyebrows are uppercase only when used as the section eyebrow ("WHY BECOME"); buttons are sentence-case.

The single shape signature is the pill. Every interactive element rounds to `{rounded.pill}` 999 px — primary CTA, secondary CTA, subtle gray pill, white floating pill, category chip, app-download badge. Cards and surfaces round to `{rounded.xl}` 16 px; the larger "Go Get 2026" annual-showcase card uses the same 16 px shape, just at scale. The tab-toggle on the hero ride-request form uses an off-shape `{rounded.pill-tab}` 36 px — barely-pill, deliberately tighter than the canonical 999 px pill.

**Key Characteristics:**
- A two-colour CTA hierarchy: black `{colors.primary}` pill for primary conversion targets; white `{colors.canvas}` pill (sometimes with a soft drop shadow) for secondary; subtle gray `{colors.canvas-soft}` pill for tertiary or chip variants.
- The pill is the single signature shape — `{rounded.pill}` 999 px on every interactive element except the tab-toggle (`{rounded.pill-tab}` 36 px) and the larger product cards (`{rounded.xl}` 16 px).
- Every headline is sentence-case in `{typography.display-xl}` / `{typography.display-xxl}` weight 700; no all-caps display.
- Editorial 4:3 illustrations of riders / drivers / cars are the only consistent decorative system; no gradients, no atmospheric backdrops, no shadows that aren't card-elevation hints.
- A signature alternating-band rhythm: white feature card → black promo card (with white text and white CTA) → white feature card → black footer. The black bands are NOT hero-only; they appear mid-page as promo callouts.
- A signature ride-request form card on the hero: pickup pin input + destination input + date/time chip + black "See prices" pill, all stacked inside a `{rounded.xl}` shadowed card.

## Colors

### Brand & Accent
- **Ink Black** (`{colors.primary}` — `#000000`): The brand's only conversion colour. Every primary CTA pill, the footer fill, every dark promo band, every nav login button. The system has no secondary accent.
- **Surface Pressed** (`{colors.surface-pressed}` — `#e2e2e2`): The pressed-state fill for white pills — a soft grey that's used only in active / pressed states. It is a **fill tone, not a boundary tone**: at 1.13:1 against `{colors.canvas-soft}` and 1.30:1 against `{colors.canvas}` it is invisible as a hairline, so any boundary that must be seen uses `{colors.hairline-mid}` (7.59:1 on `{colors.canvas-soft}`) instead.
- **Black Elevated** (`{colors.black-elevated}` — `#282828`): A near-black used on hover for the translucent white tab-toggle pill. Documented as a system colour because it appears on a recurring brand control.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): The default page background.
- **Canvas Soft** (`{colors.canvas-soft}` — `#efefef`): The soft gray fill for category chips, form-input rows inside the ride-request card, and subtle pill buttons.
- **Canvas Softer** (`{colors.canvas-softer}` — `#f3f3f3`): A slightly lighter gray used as a nested-input fill on white surfaces.

### Text
- **Ink** (`{colors.ink}` — `#000000`): Every heading and body paragraph on light surfaces.
- **Body** (`{colors.body}` — `#5e5e5e`): Secondary text — captions, sub-headings, supporting copy.
- **Hairline Mid** (`{colors.hairline-mid}` — `#4b4b4b`): A mid-gray used for muted link text inside footer columns and breadcrumb-style nav.
- **Mute** (`{colors.mute}` — `#afafaf`): The lightest text role — placeholder text, fine print, low-priority metadata. **This extracted tone fails WCAG AA on every light surface the brand owns** — 2.19:1 on `{colors.canvas}`, 1.91:1 on `{colors.canvas-soft}`, 1.98:1 on `{colors.canvas-softer}` — and it fails the 3:1 large-text allowance too, so no type size rescues it. It passes only on ink (9.57:1 on `{colors.ink}`), which is the one place `link-mute-soft` uses it. For light-surface secondary text use `{colors.body}` (6.48:1 on canvas) or `{colors.hairline-mid}` (8.72:1).
- **On Dark** (`{colors.on-dark}` — `#ffffff`): All text on `{colors.ink}` surfaces (footer, dark promo bands).

### Focus
- **Focus** (`{colors.focus}` — `#000000`): The focus ring on every light surface. It is **the brand's own ink, not a new colour** — this is a monochrome system whose first rule is "no third colour", so a chromatic ring would falsify it. Drawn as a 2 px ring with a 2 px `{colors.canvas}` offset outside the control, which is what makes it readable against a black CTA pill it surrounds. Measured 21.0:1 on `{colors.canvas}`, 18.26:1 on `{colors.canvas-soft}`, 18.93:1 on `{colors.canvas-softer}`, 16.21:1 on `{colors.surface-pressed}`.
- **Focus On Dark** (`{colors.focus-on-dark}` — `#ffffff`): The counterpart ring for the brand's black bands, footer and dark promo cards, where the ink ring would vanish. Same 2 px ring, offset 2 px in `{colors.ink}`. Measured 21.0:1 on `{colors.ink}` / `{colors.primary}`, 14.74:1 on `{colors.black-elevated}`. Over full-bleed hero photography, which has no measurable colour, use the two-tone form: 2 px `{colors.focus-on-dark}` with a 1 px `{colors.focus}` outer edge.
- Both rings reuse hexes the palette already owns; neither adds a brand colour.

### Semantic
The brand does not maintain a separate error / success / warning palette in its public marketing surface. Validation cues come from the primary black or from the brand's editorial illustrations. The `#0000ee` link colour is the system's only chromatic — it's the browser-default link blue, appearing in body-copy inline links inside legal / footer text.

## Typography

### Font Family
Two custom faces carry the entire system:

1. **A custom geometric display sans** (extracted as `UberMove`) for every headline. Weight 700 only; no italic; no tracking variation. Sizes range from `display-sm` 20 px up to `display-xxl` 52 px on the hero. Line-heights tighten to 1.22 – 1.25 at display sizes for a poured-on-the-page look.
2. **A custom text sans** (extracted as `UberMoveText`) for body, button, link, and small headings. Weights 400 and 500 are the working pair. Used at 12 – 18 px; 24 px maximum for ride-request form labels. Tracking is always neutral.

The two faces share a family DNA but never overlap roles — the display face never carries a body paragraph; the text face never carries a hero headline.

### Hierarchy

| Token | Size | Weight | Line Height | Use |
|---|---|---|---|---|
| `{typography.display-xxl}` | 52px | 700 | 64px | Hero headline ("Go anywhere with Uber", "Drive when you want"). |
| `{typography.display-xl}` | 36px | 700 | 44px | Page section headlines ("Plan for later", "Safety, simplified"). |
| `{typography.display-lg}` | 32px | 700 | 40px | Promo-card headlines. |
| `{typography.display-md}` | 24px | 700 | 32px | Card titles, illustrated-promo headlines. |
| `{typography.display-sm}` | 20px | 700 | 28px | Sub-card headings. |
| `{typography.body-lg}` | 18px | 500 | 24px | Lead paragraphs and larger body. |
| `{typography.body-md}` | 16px | 400 | 24px | Default paragraph body. |
| `{typography.body-md-strong}` | 16px | 500 | 20px | Bolded inline body and most button labels. |
| `{typography.body-sm}` | 14px | 400 | 20px | Captions, secondary metadata. |
| `{typography.body-sm-strong}` | 14px | 500 | 16px | Bold caption / chip labels. |
| `{typography.caption}` | 12px | 400 | 20px | Fine print, footer secondary lines. |
| `{typography.button-large}` | 18px | 500 | 24px | Large rounded buttons inside the ride-request form. |
| `{typography.button-md}` | 16px | 500 | 20px | Default button label. |

### Principles
- **Sentence-case is the voice.** No all-caps headlines. Eyebrow tags ("WHY BECOME") are the rare exception.
- **Weight 700 is for headlines; weight 500 is for buttons and emphasis.** Don't promote button labels to 700.
- **No tracking flourish.** The display face is never letter-spaced, positive or negative.
- **Two faces, two roles.** UberMove for display; UberMoveText for everything else. Never cross the streams.

### Note on Font Substitutes
The two faces are proprietary. Open-source substitutes:
- **Display sans** — *Inter* weight 700 with `font-feature-settings: "ss01"` enabled comes closest. *Geist* weight 700 is the second-best option.
- **Text sans** — *Inter* weights 400 / 500 match the geometric width and x-height. *Plus Jakarta Sans* is a softer alternative if the brand wants a less neutral feel.

## Layout

### Spacing System
- **Base unit**: 4 px. Most captured values are multiples of 4 with a few 6-px sub-multiples (10, 14) inside button padding.
- **Tokens**: `{spacing.xxs}` 4 px · `{spacing.xs}` 6 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 20 px · `{spacing.2xl}` 24 px · `{spacing.3xl}` 32 px.
- **Section padding**: marketing bands sit at `{spacing.3xl}` 32 px top/bottom on tighter pages and `{spacing.3xl} {spacing.3xl}` for hero bands; promo cards inset at `{spacing.2xl}` 24 px.
- **Card interior padding**: content cards sit at `{spacing.2xl}` 24 px; the ride-request form uses `{spacing.lg}` 16 px to keep the form compact.
- **Inline gap**: button rows, category chip rows, app-store pill rows use `{spacing.md}` 12 px between siblings.

### Grid & Container
- **Max width**: ~1200 px container; centred with horizontal gutters of `{spacing.3xl}` 32 px on desktop, `{spacing.lg}` 16 px on mobile.
- **Column patterns**:
  - Promo-card rows: 2-up at desktop (image left + content right, alternating sides), 1-up at mobile.
  - Category chips: horizontal flex with wrap.
  - FAQ rows: full-width single-column.
  - App-download pills: 2-up at desktop (Rider + Driver), 1-up at mobile.

### Whitespace Philosophy
Card-to-card spacing carries the rhythm — between two stacked promo cards there's roughly a full `{spacing.3xl}` 32 px gutter; inside a card the headline / paragraph / CTA stack is tight (`{spacing.sm}` 8 px between siblings). The black promo bands and the footer have no internal hairlines — content sits on flat ink with white text.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default — most cards and surfaces lean on hairline-of-canvas contrast. |
| Level 1 — Subtle Drop | `{shadow.level-1}` — `rgba(0, 0, 0, 0.12) 0px 4px 16px 0px` | Card-elevated frames around promo cards on light bands. |
| Level 2 — Card Drop | `{shadow.level-2}` — `rgba(0, 0, 0, 0.16) 0px 4px 16px 0px` | The ride-request form card on the hero; large content cards with embedded forms. |
| Level 3 — Pill Float | `{shadow.level-3}` — `rgba(0, 0, 0, 0.16) 0px 2px 8px 0px` | The floating white pill button (the one that floats over hero photography). |

### Decorative Depth
- **Black bands as polarity-flip depth**: the brand uses pure black `{colors.primary}` mid-page bands to break the white-on-white rhythm. The polarity shift IS the depth cue.
- **Editorial illustrations as in-card depth**: every promo card has a single 4:3 illustration as its left or right column. The illustration's visual weight is part of the card's elevation read.
- **Pill geometry as micro-depth**: `{rounded.pill}` 999 px applied at varying button heights creates a stack of nested pills that reads as visual hierarchy.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed hero bands, footer fill, raw image edges. |
| `{rounded.md}` | 8px | Form-input fields inside the ride-request card. |
| `{rounded.lg}` | 12px | Smaller secondary card chrome. |
| `{rounded.xl}` | 16px | Canonical card radius — promo cards, content cards, ride-request form card, annual-showcase card, large rounded buttons. |
| `{rounded.pill}` | 999px | The brand's signature interactive shape — every pill button, category chip, app-download pill, icon button. |
| `{rounded.pill-tab}` | 36px | The translucent-white tab-toggle pill on the hero (Ride / Drive). |
| `{rounded.full}` | 9999px | Identical effect to `{rounded.pill}` for circular icon containers. |

### Photography Geometry
- **Editorial illustrations**: 4:3 landscape inside promo cards; 16:9 for full-width showcase frames.
- **Driver / rider portraits**: 4:5 portrait crop; framed by `{rounded.xl}` 16 px card chrome.
- **Annual showcase image**: 2:3 portrait at desktop, scaling to 4:3 at mobile. The image fills the card; the headline overlays the bottom.
- **Logo bar**: monochrome SVG vectors at consistent ~24 px height.
- **Avatars** (where used): square or `{rounded.full}` circle, never `{rounded.lg}` rounded-square.

## Components

### Buttons

**`button-primary`** — the canonical black pill, the brand's conversion target.
- Background `{colors.primary}`, text `{colors.on-primary}`, label set in `{typography.button-md}`, padding `{spacing.md} {spacing.md}`, shape `{rounded.pill}` 999 px.

**`button-secondary`** — the white pill paired with the black primary.
- Background `{colors.canvas}`, text `{colors.ink}`, same label and padding as `button-primary`, shape `{rounded.pill}`.

**`button-subtle`** — the gray secondary pill used for tertiary actions inside cards (e.g., "Learn more" / "Use Reserve").
- Background `{colors.canvas-soft}` (`#efefef`), text `{colors.ink}`, label in `{typography.button-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.pill}`.

**`button-floating`** — the white pill with a subtle drop-shadow that floats over a dark or photographic surface.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md}`, shape `{rounded.pill}`. Carries a Level 3 pill-float shadow.

**`button-large-rounded`** — the bigger black call-to-action used inside the ride-request flow ("Yes, help me").
- Background `{colors.primary}`, text `{colors.on-primary}`, label in `{typography.button-large}`, padding `{spacing.lg} {spacing.xl}`, shape `{rounded.xl}` 16 px (not pill — the only black CTA that breaks the pill rule, used in the larger form context).

**`button-tab-translucent`** — the tab-toggle on the hero ride-request form (Ride / Drive).
- Background `{colors.canvas}`, text `{colors.ink}`, label in `{typography.body-md-strong}`, shape `{rounded.pill-tab}` 36 px (off-shape, deliberately tighter than the canonical 999 px pill).

### Cards & Containers

**`card-content`** — the canonical content card.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.2xl}`, shape `{rounded.xl}` 16 px. No shadow on the default state.

**`card-elevated`** — the content card with Level 1 subtle drop.
- Background `{colors.canvas}`, text `{colors.ink}`, same padding + shape as `card-content`. Shadow at Level 1.

**`card-soft-tinted`** — the gray-tinted card used as a sub-region inside the page (e.g., "Plan for later" callout).
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.2xl}`, shape `{rounded.xl}`.

**`promo-card-illustrated`** — the 2-column promo card with illustration on one side and copy on the other.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.2xl}`, shape `{rounded.xl}`. Headline in `{typography.display-md}` or larger.

**`promo-card-on-dark`** — the polarity-flipped promo card in black.
- Background `{colors.ink}`, text `{colors.on-dark}`, padding `{spacing.2xl}`, shape `{rounded.xl}`. Used for the "Drive with Uber" mid-page band.

**`request-form-card`** — the hero ride-request form chrome.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg}`, shape `{rounded.xl}`. Carries Level 2 card drop shadow.

**`request-form-input-row`** — the per-field row inside the request-form card.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.lg}`, shape `{rounded.md}` 8 px. Hosts an icon + label + value.

**`showcase-image-card`** — the giant "GO•GET 2026" annual showcase card.
- Background `{colors.ink}`, text `{colors.on-dark}` overlay, padding `{spacing.3xl}`, shape `{rounded.xl}`. Display-xxl headline overlays the bottom of the image.

### Inputs & Forms

**`text-input`** — the canonical text input.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, body in `{typography.body-md}`, padding `{spacing.lg}`, shape `{rounded.md}` 8 px.

**`text-input-on-soft`** — the nested input on a white card (slightly lighter fill).
- Background `{colors.canvas-softer}`, otherwise identical to `text-input`.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas}` on light pages, switches to `{colors.ink}` on the rare dark page (e.g., Uber Eats hero). Padding `{spacing.lg} {spacing.3xl}`.

**`nav-link`** — the link row inside `nav-bar`.
- Text `{colors.ink}`, set in `{typography.body-md-strong}` 500 weight.

**`footer`** — the deep-black footer band.
- Background `{colors.primary}` (the brand's only true black surface), text `{colors.on-dark}`, padding `{spacing.3xl} {spacing.3xl}`. Body in `{typography.body-sm}`; column eyebrows in `{typography.body-md-strong}`.

### Signature Components

**`hero-band-light`** — the white hero with the ride-request card.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.3xl}`. Headline in `{typography.display-xxl}` (52 px / 700) on the left; `request-form-card` on the right.

**`hero-band-dark`** — the rare black hero (used on Uber Eats and Drive landing).
- Background `{colors.ink}`, text `{colors.on-dark}`, padding `{spacing.3xl} {spacing.3xl}`. Same display-xxl headline scale; CTA inverts to `button-secondary` white pill.

**`category-button`** — the horizontal-scroll category row ("Reserve / Rentals / Teens / Group rides").
- Background `{colors.canvas-soft}`, text `{colors.ink}`, label in `{typography.body-sm-strong}`, padding `{spacing.sm} {spacing.lg}`, shape `{rounded.pill}`. An icon precedes the label.

**`faq-row`** — the FAQ accordion item.
- Background `{colors.canvas}`, text `{colors.ink}`, question in `{typography.body-md-strong}`, padding `{spacing.lg}` 0. No card chrome — hairline dividers between rows.

**`app-download-pill`** — the "Download the Rider app" / "Download the Driver app" pill.
- Background `{colors.ink}`, text `{colors.on-dark}`, label in `{typography.body-md-strong}`, padding `{spacing.md} {spacing.xl}`, shape `{rounded.pill}`.

**`icon-button-circular`** — the round icon container used in the nav and inside the ride-request card.
- Background `{colors.canvas-soft}`, dark icon, shape `{rounded.full}`. No label.

### Links

**`link-blue`** — the system-default browser-blue link inside legal / footer fine print.
- Text `{colors.link}` (`#0000ee`), body in `{typography.body-md}`.

**`link-on-dark`** — the white link inside dark bands.
- Text `{colors.on-dark}`, body in `{typography.body-md}`.

**`link-mute`** — the muted gray link inside footer columns.
- Text `{colors.hairline-mid}`, body in `{typography.body-md}`.

**`link-mute-soft`** — the lightest gray link, used for low-priority secondary text on dark surfaces.
- Text `{colors.mute}`, body in `{typography.body-md}`.

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


### Component States

Every component's supported states. `focus-visible` always draws `{colors.focus}` on light
surfaces and `{colors.focus-on-dark}` on ink surfaces, 2 px with a 2 px offset. Hover and
pressed fills are extracted (`{colors.black-elevated}`, `{colors.surface-pressed}`); every
other state in this table is prescribed, not extracted.

| Component | States | Notes |
|---|---|---|
| `button-primary` | default · hover · focus-visible · pressed · disabled · loading | hover fills `{colors.black-elevated}`; pressed adds `scale(0.98)`; disabled drops fill + label to 38% opacity; loading swaps the label for a spinner at a frozen pill width. No selected, no error. |
| `button-secondary` | default · hover · focus-visible · pressed · disabled · loading | hover fills `{colors.canvas-soft}`; pressed fills `{colors.surface-pressed}`. |
| `button-subtle` | default · hover · focus-visible · pressed · disabled | hover fills `{colors.surface-pressed}`; pressed holds it with `scale(0.98)`. |
| `button-floating` | default · hover · focus-visible · pressed · disabled | shadow steps `{shadow.level-3}` → `{shadow.level-1}` on hover; focus ring uses the two-tone form over photography. |
| `button-large-rounded` | default · hover · focus-visible · pressed · disabled · loading | same ladder as `button-primary` at `{rounded.xl}`. |
| `button-tab-translucent` | default · hover · focus-visible · pressed · selected | selected is the active Ride / Drive tab: `{colors.ink}` fill, `{colors.on-dark}` label; hover on the unselected tab fills `{colors.black-elevated}`. |
| `category-button` | default · hover · focus-visible · pressed · selected · disabled | selected inverts to `{colors.ink}` fill with `{colors.on-dark}` label. |
| `text-input` | default · hover · focus-visible · disabled · error | focus draws the ring outside the field, keeping `{rounded.md}`; error adds a 2 px `{colors.ink}` boundary plus a `{typography.caption}` message — the brand owns no chromatic error tone (see Known Gaps). No hover fill change beyond `{colors.canvas-softer}`. |
| `text-input-on-soft` | default · hover · focus-visible · disabled · error | identical ladder to `text-input`. |
| `request-form-input-row` | default · hover · focus-visible · selected · error | selected is the row whose picker is open; hover fills `{colors.surface-pressed}`. |
| `request-form-card` | default · loading | two states only: static chrome, plus a loading state while prices resolve. No hover, no pressed — it is a container. |
| `card-content` · `card-soft-tinted` | default | one state only: a static container with no interactive affordance. |
| `card-elevated` | default · hover | hover steps `{shadow.level-1}` → `{shadow.level-2}` where the whole card is a link; otherwise default only. |
| `promo-card-illustrated` · `promo-card-on-dark` | default · hover · focus-visible | the card is a link target: hover lifts the shadow one level, focus-visible rings the whole card. |
| `showcase-image-card` | default · hover · focus-visible | hover scales the image `1.02`; the frame does not move. |
| `nav-bar` | default · loading | two states: resting, and a route-change loading bar. |
| `nav-link` | default · hover · focus-visible · selected | hover underlines in `{colors.ink}`; selected is the current section. |
| `faq-row` | default · hover · focus-visible · pressed · selected | selected is the expanded row; the chevron rotates, the panel fades. |
| `app-download-pill` | default · hover · focus-visible · pressed | hover fills `{colors.black-elevated}`. |
| `icon-button-circular` | default · hover · focus-visible · pressed · disabled · selected | selected used for the map-layer toggles only. |
| `link-blue` · `link-on-dark` · `link-mute` · `link-mute-soft` | default · hover · focus-visible | hover underlines; no colour change — the brand has no hover-link tone. |
| `footer` · `hero-band-light` · `hero-band-dark` | default | one state only: page furniture. |
| `ex-*` (illustrative) | default · hover · focus-visible · pressed · disabled · loading · selected · error | the demonstration surfaces inherit the ladder of the brand primitive each one mirrors; `ex-app-shell-row` and `ex-product-selector` carry selected, `ex-auth-form-card` carries error and loading. |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity; it was not measured from the live site.** No duration, easing curve or delay was extracted from Uber's web surface, so every value below comes from the **Playful** profile in `theme-audit/SPEC.md` section 5, used verbatim. The two things motion here *can* lean on are extracted: `{colors.black-elevated}` is the real hover fill of the hero tab pill, and `{colors.surface-pressed}` is the real pressed fill of a white pill. Where a state is a colour change, that colour is a fact and the timing is not.

Why Playful on a monochrome brand: the identity is illustration-led and consumer-facing (editorial riders / drivers / city objects are the only decorative system), and the pill is on every interactive element — so presses get a small scale pop and reveals a light overshoot. The brand's restraint is honoured by keeping travel short (8–12 px) and scale small (0.98–1.02), never by slowing the curve.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, link, card) | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `background-color` / `border-color` / `box-shadow` — paint only, no transform; this near-monochrome brand's hover *is* the fill change | Fill change kept, timed at `{motion.duration-reduced}`; no shadow lift |
| Press | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.98)` + `background-color` → `{colors.surface-pressed}` | Scale removed; fill change only |
| Focus (focus-visible) | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` on the 2 px ring | Ring appears with no fade — instant, never suppressed |
| Page / route transition | enter `{motion.duration-base}` 200ms · exit `{motion.duration-fast}` 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px)` | Travel removed; cross-fade at `{motion.duration-reduced}` |
| Modal / drawer | enter `{motion.duration-base}` 200ms · exit `{motion.duration-fast}` 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: scale(0.98) → 1` (drawer: `translateY(16px)`) | Opacity only at `{motion.duration-reduced}`; backdrop fade kept |
| Dropdown / menu | enter `{motion.duration-fast}` 130ms · exit `{motion.duration-instant}` 70ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)`, origin at the trigger edge | Opacity only at `{motion.duration-reduced}` |
| Toast | enter `{motion.duration-base}` 200ms · exit `{motion.duration-fast}` 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(12px)` | Travel removed; fade at `{motion.duration-reduced}` |
| List enter (category chips, FAQ rows, promo cards) | `{motion.duration-base}` 200ms per item, `{motion.stagger-step}` 60ms apart, capped at 6 items | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px)` | Stagger and travel removed; all items fade together at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` 130ms, no stagger | `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)` | Scale removed; fade at `{motion.duration-reduced}` |
| Loading | indeterminate spinner: 900ms per revolution, infinite · skeleton shimmer: `{motion.duration-emphasis}` 450ms per pass, infinite | `linear` (spinner) · `{motion.ease-standard}` (shimmer) | `transform: rotate()` · `transform: translateX()` on a masked gradient | Both loops frozen; replaced by a static indicator whose label fades in at `{motion.duration-reduced}` |

**Rules this file holds to**
- `transform` and `opacity` are the only animated geometry. Never `width`, `height`, `top`, `left` or `margin` — the ride-request card and the chip row must not reflow while they move. Paint-only changes (`background-color`, `border-color`, `box-shadow`) are state changes, not travel, and use the same tokens.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content: the hero headline and the ride-request card render at rest. Only content entering after an interaction animates.
- The spinner and the skeleton shimmer are the only infinite animations. The brand runs no ambient motion.
- The 900ms spinner revolution is the one value outside the profile scale, and deliberately so: a loader cycle is a rhythm, not a state change, and the profile's longest token (450ms) spins too fast to read.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translate), all scale, the stagger on list enter,
     the shadow lift on hover, the spinner rotation and the skeleton shimmer
     (both are frozen to a static indicator). */
  *, *::before, *::after {
    animation-duration: 130ms !important;   /* {motion.duration-reduced} */
    animation-iteration-count: 1 !important;
    transition-duration: 130ms !important;  /* {motion.duration-reduced} */
    transition-property: opacity, background-color, border-color, color !important;
    transform: none !important;
  }
  /* Kept: opacity fades at {motion.duration-reduced} (130ms, never above
     150ms), every paint-only state change, and the focus ring, which appears
     instantly and is never suppressed. */
}
```

## Accessibility

### Measured contrast

WCAG 2.1 relative luminance, computed from this file's own hexes.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#000000` on `{colors.canvas}` `#ffffff` | 21.0:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` `#efefef` | 18.26:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-softer}` `#f3f3f3` | 18.93:1 | 4.5:1 | Pass |
| `{colors.on-primary}` `#ffffff` on `{colors.primary}` `#000000` | 21.0:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.ink}` | 21.0:1 | 4.5:1 | Pass |
| `{colors.body}` `#5e5e5e` on `{colors.canvas}` | 6.48:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas-soft}` | 5.64:1 | 4.5:1 | Pass |
| `{colors.hairline-mid}` `#4b4b4b` on `{colors.canvas}` | 8.72:1 | 3.0:1 | Pass (boundary) |
| `{colors.hairline-mid}` on `{colors.canvas-soft}` | 7.59:1 | 3.0:1 | Pass (boundary) |
| `{colors.link}` `#0000ee` on `{colors.canvas}` | 9.4:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.black-elevated}` `#282828` | 14.74:1 | 4.5:1 | Pass |

### Where the real brand fails AA

These are extracted values, kept as they are. The brand genuinely fails here, and that is the useful fact for anyone building on this document.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `mute` `#afafaf` on `canvas` `#ffffff` | 2.19:1 | 4.5:1 | **Fail** — placeholder and fine-print grey. Also fails the 3:1 large-text allowance, so no type size defends it. |
| `mute` `#afafaf` on `canvas-soft` `#efefef` | 1.91:1 | 4.5:1 | **Fail** — the same grey inside a form-input row, which is where it is most often read. |
| `mute` `#afafaf` on `canvas-softer` `#f3f3f3` | 1.98:1 | 4.5:1 | **Fail** — nested input fill. |
| `surface-pressed` `#e2e2e2` on `canvas-soft` `#efefef` | 1.13:1 | 3.0:1 | **Fail as a boundary** — it is a pressed *fill*, and legitimate as one; nothing in this file now binds it as a border. Boundaries use `{colors.hairline-mid}`. |
| `surface-pressed` `#e2e2e2` on `canvas` `#ffffff` | 1.30:1 | 3.0:1 | **Fail as a boundary**, same reason. |

`mute` passes only on ink: 9.57:1 on `{colors.ink}`, which is the single place `link-mute-soft` is drawn. Nearest passing replacements, if a brand owner ever approves one: `#767676` (4.54:1 on canvas), `#6d6d6d` (4.50:1 on canvas-soft), or `#949494` (3.03:1 on canvas) for 24 px+ / 18.66 px-bold labels only.

### Focus ring visibility, surface by surface

The ring is drawn **outside** the control with a 2 px offset, so it is judged against the surface behind the control, not against the control's own fill — which matters here, because a black CTA pill and a white canvas cannot both be cleared by one ring colour.

| Surface | Ring | Ratio | Required |
|---|---|---|---|
| `{colors.canvas}` `#ffffff` | `{colors.focus}` `#000000` | 21.0:1 | 3.0:1 |
| `{colors.canvas-soft}` `#efefef` | `{colors.focus}` | 18.26:1 | 3.0:1 |
| `{colors.canvas-softer}` `#f3f3f3` | `{colors.focus}` | 18.93:1 | 3.0:1 |
| `{colors.surface-pressed}` `#e2e2e2` | `{colors.focus}` | 16.21:1 | 3.0:1 |
| `{colors.ink}` / `{colors.primary}` `#000000` (footer, dark bands, dark promo cards) | `{colors.focus-on-dark}` `#ffffff` | 21.0:1 | 3.0:1 |
| `{colors.black-elevated}` `#282828` (hover state of the dark tab pill) | `{colors.focus-on-dark}` | 14.74:1 | 3.0:1 |
| Full-bleed hero photography (no measurable colour) | two-tone: `{colors.focus-on-dark}` 2 px with a 1 px `{colors.focus}` outer edge | not measurable | — |

Neither ring is a new brand colour: `{colors.focus}` is the brand's ink and `{colors.focus-on-dark}` is its paper. A monochrome system whose first rule is "no third colour" gets a monochrome ring with a mandatory opposite-polarity offset, not an invented blue.

### Tap targets

`button-primary` computes to ~44 px tall and `button-large-rounded` to ~56 px from the padding and line-height tokens in this file; category chips reach ≥ 44 px on touch viewports through extra vertical padding. These are **arithmetic from tokens, not browser measurements** — nothing in this audit renders a page, so treat them as the intended minimum (44 × 44 px) rather than a verified one.

### Reduced motion

Every animation in `## Motion & Animation` has a reduced-motion counterpart, and the `@media (prefers-reduced-motion: reduce)` block there is normative: all travel, all scale, the list stagger, the shadow lift, the spinner rotation and the skeleton shimmer are removed; opacity fades and paint-only state changes remain at `{motion.duration-reduced}` 130ms. The focus ring is never suppressed.

### Other accessibility notes

- The brand carries **no error / success / warning palette** (stated in Colors → Semantic). Error states therefore signal with a 2 px `{colors.ink}` boundary plus a `{typography.caption}` message, which is shape and text rather than colour — it satisfies 1.4.1 by not relying on colour, but it gives a screen-reader-free user no colour cue at all. Recorded in Known Gaps.
- `{colors.link}` `#0000ee` is the browser default blue, used only in legal / footer fine print. It passes 4.5:1 on canvas but sits at 2.23:1 on `{colors.ink}`, so it must never appear inside a dark band; dark bands use `link-on-dark`.
- Hover states that are pure fill changes (`{colors.black-elevated}`, `{colors.surface-pressed}`) are paired with an underline on links, so hover is never colour-only.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (`#000000`) for every primary CTA pill. One black pill per visible viewport is the brand's whole conversion story.
- Use `{rounded.pill}` 999 px on every interactive element (buttons, chips, app pills). The pill IS the brand's geometric signature.
- Render cards in `{rounded.xl}` 16 px — promo cards, content cards, the ride-request form card, the annual-showcase card all share this radius.
- Set every headline in `{typography.display-*}` weight 700 in sentence-case. The display face never carries body copy.
- Use polarity-flipped black promo bands mid-page to break up white-on-white rhythm. The polarity shift IS the depth cue.
- Anchor every promo card with a 4:3 editorial illustration; never use generic stock imagery.

### Don't
- Don't introduce a second brand accent colour (orange, blue, green). The brand's entire UI is black-and-white plus grayscale; new accents flatten the system.
- Don't render the primary CTA as a `{rounded.xl}` rectangle except inside the larger ride-request flow (where `button-large-rounded` is the documented exception).
- Don't use all-caps display headlines. Sentence-case is the voice; uppercase is restricted to rare eyebrow tags.
- Don't drop a soft drop-shadow on every card. The brand uses Level 0 flat as the default; shadow is reserved for the floating pill and the ride-request form.
- Don't reduce the brand to its illustration system alone. The pill geometry + black/white duet carries the brand even without illustrations.
- Don't tighten or loosen letter-spacing on the display face. The brand never letter-spaces; default tracking is part of the voice.
- Don't use `{rounded.full}` 9999 px for square cards — the pill 999 px and full 9999 px effects are identical for interactive elements, but cards stay at `{rounded.xl}` 16 px.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 600px | Nav collapses to hamburger; promo cards stack; ride-request form becomes full-width. |
| Mobile-Large | 600–767px | Same as Mobile; chip rows enable horizontal scroll. |
| Tablet | 768–1119px | 2-up promo grid at upper widths; nav stays horizontal until ≥ 1120 px. |
| Desktop | 1120–1135px | Full nav row visible; promo cards 2-up. |
| Desktop-Large | ≥ 1136px | Container caps at ~1200 px; bands stay edge-to-edge while content centres. |

### Touch Targets
The pill `button-primary` renders at ~44 px tall (10 px vertical padding + 24 px label line-height); the larger `button-large-rounded` at ~56 px. Both meet WCAG AAA at all breakpoints. Category chips inflate to ≥ 44 px tall through extra padding on touch viewports.

### Collapsing Strategy
- **Nav**: full link row + Help / Log in / Sign up pills at desktop. Collapses to logo + hamburger at mobile; menu overlays full-screen with the same link list stacked.
- **Ride-request form card**: at desktop, the form sits inside a max-490-px `{rounded.xl}` card with shadow. At mobile, full-width with edge-to-edge.
- **Promo cards**: at desktop, image-left + content-right (or alternating). At mobile, image always above content.
- **Annual showcase card**: scales from a 2:3 desktop frame to a 4:3 mobile frame; date text resizes proportionally.

### Image Behavior
- **Editorial illustrations**: 4:3 or 16:9 hard-edge rectangles; never cropped to a circle, never tilted. Aspect preserved.
- **Photography**: same — square or landscape; framed inside `{rounded.xl}` card chrome.
- **Maps in ride-request flow**: full-bleed inside a card; rounded corners follow the parent card.
- **Logo bar**: SVG vector, monochrome, consistent height.

## Known Gaps

- **No motion value is extracted.** Every duration, easing curve and stagger in `## Motion & Animation` comes from the Playful profile in `theme-audit/SPEC.md`, not from Uber's live site. The 900ms spinner revolution is a stated deviation from that profile.
- **No disabled tone exists in the palette.** Disabled states are specified as 38% opacity on the live fill and label, because inventing a grey hex would falsify a monochrome brand that documents none. A brand owner should confirm or replace that with a real token.
- **No semantic palette.** The brand publishes no error / success / warning / info colour, so error states carry shape and text only. Nothing in this file should be read as the brand's validation colour.
- **`{colors.mute}` fails AA everywhere it is used on a light surface** (2.19:1 / 1.91:1 / 1.98:1). The hex is extracted and unchanged; see Accessibility for nearest passing values, which need brand-owner approval.
- **Boundary re-scoping in the illustrative block.** `ex-pricing-tier` (borderColor), `ex-cart-drawer` (item-divider) and `ex-data-table-cell` (rowBorder) previously pointed at `{colors.surface-pressed}`, invisible at 1.13:1 on their own ground. They now point at `{colors.hairline-mid}`. Those three bindings are auto-derived demonstration surfaces, not extracted facts about the site; no extracted binding was re-pointed. Whether the real site draws a visible divider in those places is unverified.
- **Tap-target sizes are computed, not rendered.** The ~44 px and ~56 px figures in `## Responsive Behavior` and Accessibility are arithmetic from padding and line-height tokens. The claim that they "meet WCAG AAA at all breakpoints" is moved here as unverified: no page was rendered in this audit.
- **Shadow tokens are extracted values given names.** The three `rgba(...)` elevations were already written in the prose; `{shadow.level-1}` … `{shadow.level-3}` only make them referenceable. No new shadow was invented, and the brand's default remains Level 0 flat.
- **`{colors.black-elevated}` is documented as a hover fill for one control** (the hero tab pill). This file now applies it to the hover state of other ink pills, which is prescribed consistency, not an extracted fact.
- **Focus rings are prescribed.** No focus treatment was extracted from the site. The hexes are the brand's own ink and paper, and the 2 px ring / 2 px offset geometry is this document's prescription.
- **The `ex-*` block still carries its auto-derivation note** and generic descriptions ("re-purposed for SaaS / B2B"). It reads as borrowed from the shared example kit rather than from Uber. Left verbatim: rewriting it is outside this file's extracted content.
