---
version: alpha
name: Wise-Inspired-design-analysis
description: An inspired interpretation of Wise's design language — a global money-transfer brand whose surface combines an unusually heavy near-black display sans (weight 900 at 64–126 px) with a vivid lime-green brand accent, sage-tinted surface neutrals, and rounded white cards on a pale green-tinted canvas; the whole system reads more like a Scandinavian fintech magazine than a bank.

colors:
  primary: "#9fe870"
  on-primary: "#0e0f0c"
  primary-active: "#cdffad"
  primary-neutral: "#c5edab"
  primary-pale: "#e2f6d5"
  ink: "#0e0f0c"
  ink-deep: "#163300"
  body: "#454745"
  mute: "#868685"
  canvas: "#ffffff"
  canvas-soft: "#e8ebe6"
  positive: "#2ead4b"
  positive-deep: "#054d28"
  warning: "#ffd11a"
  warning-deep: "#b86700"
  warning-content: "#4a3b1c"
  negative: "#d03238"
  negative-deep: "#a72027"
  negative-darkest: "#a7000d"
  negative-bg: "#320707"
  accent-orange: "#ffc091"
  accent-cyan: "#38c8ff"
  focus: "#163300"
  focus-on-dark: "#9fe870"

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

typography:
  display-mega:
    fontFamily: Wise Sans, Inter, system-ui, -apple-system, sans-serif
    fontSize: 126px
    fontWeight: 900
    lineHeight: 107.1px
  display-xxl:
    fontFamily: Wise Sans, Inter, system-ui, sans-serif
    fontSize: 96px
    fontWeight: 900
    lineHeight: 81.6px
  display-xl:
    fontFamily: Wise Sans, Inter, system-ui, sans-serif
    fontSize: 64px
    fontWeight: 900
    lineHeight: 54.4px
  display-lg:
    fontFamily: Wise Sans, Inter, system-ui, sans-serif
    fontSize: 47px
    fontWeight: 400
    lineHeight: 70.5px
    letterSpacing: -0.108px
  display-md:
    fontFamily: Wise Sans, Inter, system-ui, sans-serif
    fontSize: 40px
    fontWeight: 900
    lineHeight: 34px
  display-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 600
    lineHeight: 38.4px
    letterSpacing: -0.96px
  display-xs:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 31.2px
    letterSpacing: -0.48px
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 30px
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-md-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 20px
  caption:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px

rounded:
  none: 0px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    padding: "{spacing.md} {spacing.xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.xl}"
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.xl}"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  card-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  card-feature-sage:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  card-feature-green:
    backgroundColor: "{colors.primary-pale}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  card-feature-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  hero-band:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-mega}"
    padding: "{spacing.3xl} {spacing.xl}"
  hero-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    typography: "{typography.display-mega}"
    padding: "{spacing.3xl} {spacing.xl}"
  content-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.3xl} {spacing.xl}"
  currency-converter-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  badge-positive:
    backgroundColor: "{colors.primary-pale}"
    textColor: "{colors.positive-deep}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  badge-negative:
    backgroundColor: "{colors.negative-bg}"
    textColor: "{colors.canvas-soft}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.mute}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    item-divider: "{colors.mute}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.mute}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Wise — the global money-transfer brand — wears its identity in a single signature pairing: a vivid lime-green `{colors.primary}` (`#9fe870`) used as the CTA pill and brand accent, set against a pale sage-tinted canvas `{colors.canvas-soft}` (`#e8ebe6`) that runs across the hero band, and a near-black ink `{colors.ink}` (`#0e0f0c`) with a hint of warmth from the brand's underlying olive cast. The brand reads more like a calm Scandinavian magazine than a bank — generous whitespace, large rounded cards, and an unusually heavy display sans set at weight 900 carrying every hero headline.

Display typography is the second decisive voice. The proprietary `Wise Sans` family carries hero displays at weight 900 in scales from 64 px up to 126 px on the largest hero. The brand pairs Wise Sans 900 with Inter at weight 600 for sub-displays — the contrast between the chunky proprietary face and Inter's neutrality creates a particular hierarchy: Wise Sans for the brand moment, Inter for everything else.

Cards are universally pill-rounded — `{rounded.xl}` 24 px is the brand's signature card radius. Buttons take the same 24 px pill-rectangle shape. The brand never uses sharp corners on UI elements; the visual softness is part of the friendly fintech voice.

**Key Characteristics:**
- A single lime-green CTA accent `{colors.primary}` (`#9fe870`) — the brand's universal primary action color. No second accent.
- Two-face display typography — Wise Sans (proprietary, weight 900, hero scale) + Inter (weight 600, sub-display scale). The contrast is the brand's typographic story.
- `{rounded.xl}` 24 px is the canonical card and button radius. Generous, friendly.
- Sage-tinted canvas `{colors.canvas-soft}` (`#e8ebe6`) is the brand's hero surface; white `{colors.canvas}` is reserved for cards within the sage band.
- A full semantic palette: positive green family, warning yellow family, negative red family — each documented with content / hover / active variants for in-product use.
- Currency-converter card on the hero — the brand's signature interactive component, hosting from/to amount inputs.

## Colors

### Brand & Accent
- **Wise Green** (`{colors.primary}` — `#9fe870`): The brand's universal CTA color. Every primary button, every "Send money" pill, the brand's logo accent.
- **Wise Green Hover** (`{colors.primary-active}` — `#cdffad`): The lighter green for active state.
- **Wise Green Neutral** (`{colors.primary-neutral}` — `#c5edab`): A mid-saturation green used as a neutral active fill.
- **Wise Green Pale** (`{colors.primary-pale}` — `#e2f6d5`): The lightest green for soft surface tints / badge backgrounds.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): Pure white for card interiors.
- **Canvas Soft** (`{colors.canvas-soft}` — `#e8ebe6`): The sage-tinted page background. Defining mood of the brand.

### Text
- **Ink** (`{colors.ink}` — `#0e0f0c`): Near-black with a hint of olive warmth — the brand's default text and headings color.
- **Ink Deep** (`{colors.ink-deep}` — `#163300`): A deep forest-green ink used on positive-state surfaces.
- **Body** (`{colors.body}` — `#454745`): Secondary body text.
- **Mute** (`{colors.mute}` — `#868685`): Lowest-priority text — captions, placeholder, fine print.

### Semantic
- **Positive** (`{colors.positive}` — `#2ead4b`): Success indicator.
- **Positive Deep** (`{colors.positive-deep}` — `#054d28`): Pressed positive state.
- **Warning** (`{colors.warning}` — `#ffd11a`): Caution indicator.
- **Warning Deep** (`{colors.warning-deep}` — `#b86700`): Pressed warning.
- **Warning Content** (`{colors.warning-content}` — `#4a3b1c`): Text on warning surfaces.
- **Negative** (`{colors.negative}` — `#d03238`): Destructive / error red.
- **Negative Deep** (`{colors.negative-deep}` — `#a72027`): Pressed destructive.
- **Negative Darkest** (`{colors.negative-darkest}` — `#a7000d`): Highest-emphasis destructive text.
- **Negative Bg** (`{colors.negative-bg}` — `#320707`): Dark maroon for destructive callout backgrounds.

### Brand Accent — Tertiary
- **Accent Orange** (`{colors.accent-orange}` — `#ffc091`): Bright peach used inside illustrative content / pricing cards.
- **Accent Cyan** (`{colors.accent-cyan}` — `#38c8ff`): Bright sky-blue used as a tertiary illustration accent.

## Typography

### Font Family
Two faces ladder the system:
1. **Wise Sans** — proprietary geometric sans with an unusually heavy weight 900 used for all hero displays. The face is the brand's typographic signature. Always at weight 900, never lighter on the marketing surface.
2. **Inter** — used for sub-displays (weight 600), all body, and form labels. Loaded with `font-feature-settings: "calt"` for contextual alternates.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-mega}` | 126px | 900 | 107.1px | 0 | Hero stencil at maximum scale. |
| `{typography.display-xxl}` | 96px | 900 | 81.6px | 0 | Sub-hero scale. |
| `{typography.display-xl}` | 64px | 900 | 54.4px | 0 | Standard hero headline. |
| `{typography.display-lg}` | 47px | 400 | 70.5px | -0.108px | Lighter sub-display. |
| `{typography.display-md}` | 40px | 900 | 34px | 0 | Section / card headlines. |
| `{typography.display-sm}` | 32px | 600 | 38.4px | -0.96px | Inter-rendered section headings. |
| `{typography.display-xs}` | 24px | 600 | 31.2px | -0.48px | Sub-section displays. |
| `{typography.body-lg}` | 20px | 400 | 30px | 0 | Lead paragraphs. |
| `{typography.body-md}` | 16px | 400 | 24px | 0 | Default body. |
| `{typography.body-md-strong}` | 16px | 600 | 24px | 0 | Bold inline body. |
| `{typography.body-sm}` | 14px | 400 | 20px | 0 | Secondary body. |
| `{typography.body-sm-strong}` | 14px | 600 | 20px | 0 | Bold caption / nav-link. |
| `{typography.caption}` | 12px | 400 | 16px | 0 | Fine print. |
| `{typography.button-md}` | 16px | 600 | 24px | 0 | Button label. |

### Principles
- **Weight 900 for hero, weight 600 for everything else.** The brand's display ceiling is full-black weight; everything below is semibold.
- **Wise Sans for the brand voice, Inter for utility.** Strict role separation.

### Note on Font Substitutes
Wise Sans is proprietary. Open-source substitutes:
- **Display** — *Inter* at weight 900 or *Manrope* at weight 800 / 900 captures the geometric heaviness. *Geist* weight 800 is a passable second choice.
- **Sub-display + body** — *Inter* is the brand's actual second face.

## Layout

### Spacing System
- **Base unit**: 4 px.
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 24 px · `{spacing.2xl}` 32 px · `{spacing.3xl}` 48 px.
- **Section padding**: bands use `{spacing.3xl}` 48 px top/bottom on desktop.
- **Card interior**: cards at `{spacing.xl}` 24 px.

### Grid & Container
- Marketing container centres at ~1200 px.
- Hero: split layout (headline left, currency-converter card right) at desktop; stacked at mobile.
- Feature grids: 2-up / 3-up at desktop.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default. |
| Level 1 — Hairline on Dark | 1 px solid `{colors.ink}` border. | Tertiary outline buttons, form inputs. |
| Level 2 — Soft Card | Implicit Level 0 white card sitting on sage canvas — the surface contrast IS the elevation. | Cards on the sage hero band. |

The brand uses surface contrast (`{colors.canvas-soft}` background vs `{colors.canvas}` cards) as the primary elevation cue.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed bands. |
| `{rounded.sm}` | 8px | Inline pills, small badges. |
| `{rounded.md}` | 12px | Form inputs, smaller chrome. |
| `{rounded.lg}` | 16px | Mid-size cards. |
| `{rounded.xl}` | 24px | The brand's canonical button + card radius. |
| `{rounded.pill}` | 9999px | Status pills and full-radius accents. |
| `{rounded.full}` | 9999px | Circular icon containers. |

## Components

### Buttons

**`button-primary`** — the lime-green CTA pill.
- Background `{colors.primary}`, text `{colors.on-primary}`, label `{typography.button-md}`, padding `{spacing.md} {spacing.xl}`, shape `{rounded.xl}` 24 px.
- States: **default** `{colors.primary}` · **hover** fill lifts to `{colors.primary-active}` · **focus-visible** 2 px `{colors.focus}` ring, 2 px offset outside the pill · **pressed** fill drops to `{colors.primary-neutral}` · **disabled** `{colors.primary-pale}` fill with `{colors.mute}` label, no pointer events · **loading** label swapped for an in-place spinner, width held so no layout shift. Fill changes are paint-only (`background-color`) at `{motion.duration-fast}`.

**`button-secondary`** — the sage-tinted secondary.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, same typography / padding / shape.
- States: **default**, **hover** (fill to `{colors.primary-pale}`), **focus-visible** (`{colors.focus}` ring, 2 px offset), **pressed** (fill to `{colors.primary-neutral}`), **disabled** (`{colors.mute}` label), **loading** (in-place spinner).

**`button-tertiary`** — the white outline tertiary.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, same typography / padding / shape.
- States: **default**, **hover** (fill to `{colors.canvas-soft}`, border held), **focus-visible** (`{colors.focus}` ring, 2 px offset outside the `{colors.ink}` border), **pressed** (fill to `{colors.primary-pale}`), **disabled** (border and label to `{colors.mute}`), **loading** (in-place spinner).

**`button-icon-circular`** — the circular icon button.
- Background `{colors.canvas}`, ink icon, shape `{rounded.full}`.
- States: **default**, **hover** (fill to `{colors.canvas-soft}`), **focus-visible** (`{colors.focus}` ring, 2 px offset), **pressed** (fill to `{colors.primary-neutral}`), **disabled** (icon to `{colors.mute}`). No loading state — the control is never a submit target.

### Cards & Containers

**`card-content`** — the default white card.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.xl}`. No border, sits on sage canvas.
- States: **default** and, where the whole card is a link, **hover** (`translateY(-2px)` at `{motion.duration-base}`) and **focus-visible** (`{colors.focus}` ring, 2 px offset). Static content cards have **default** only.

**`card-feature-sage`** — the sage-tinted feature card.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.xl}`.
- States: **default** only when static; **hover** and **focus-visible** as `card-content` when linked.

**`card-feature-green`** — the soft-green feature card.
- Background `{colors.primary-pale}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.xl}`.
- States: **default** only when static; **hover** and **focus-visible** as `card-content` when linked.

**`card-feature-dark`** — the polarity-flipped dark card with green text.
- Background `{colors.ink}`, text `{colors.primary}` (Wise green!), padding `{spacing.xl}`, shape `{rounded.xl}`. Used for promotional moments.
- States: **default**; **hover** and **focus-visible** when linked — the ring on this surface is `{colors.focus-on-dark}`, not `{colors.focus}`.

**`currency-converter-card`** — the brand's signature interactive widget.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, padding `{spacing.xl}`, shape `{rounded.xl}`. Hosts from/to amount inputs + currency selectors.
- States: **default** · **loading** while a mid-market rate is fetched (rate line replaced by a skeleton; inputs stay interactive) · **error** when the rate fetch or an amount fails validation — message in `{colors.negative-darkest}` under the field, card border to `{colors.negative}`. **hover**, **focus-visible** and **disabled** belong to the inputs and the selector inside it, not to the card frame.

### Inputs & Forms

**`text-input`** — the canonical text input.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, body in `{typography.body-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.md}`.
- States: **default** · **hover** border held, fill to `{colors.canvas-soft}` · **focus-visible** 2 px `{colors.focus}` ring at 2 px offset outside the `{colors.ink}` border · **disabled** fill `{colors.canvas-soft}`, border and text `{colors.mute}` · **error** border `{colors.negative}` with helper text in `{colors.negative-darkest}` · **selected** applies to the currency row inside the selector, fill `{colors.primary-pale}`. No pressed or loading state on the field itself.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.xl}`.
- States: two only — **default** (flat on the canvas) and scrolled (a 1 px `{colors.canvas-soft}` bottom hairline appears). The bar itself takes no hover, pressed, disabled, loading, selected or error state; those live on `nav-link`.

**`nav-link`** — link items inside nav.
- Text `{colors.ink}`, set in `{typography.body-sm-strong}`.
- States: **default** · **hover** text to `{colors.ink-deep}`, 1 px underline · **focus-visible** `{colors.focus}` ring at 2 px offset · **selected** current section keeps the underline permanently and sets the label to `{colors.ink-deep}` · **disabled** `{colors.mute}`. No pressed, loading or error state.

**`footer`** — the dark footer band.
- Background `{colors.ink}`, text `{colors.canvas-soft}`, padding `{spacing.3xl} {spacing.xl}`. Body in `{typography.body-sm}`.
- States: **default** only for the band. Links inside it take **hover** (text to `{colors.primary}`) and **focus-visible** (`{colors.focus-on-dark}` ring — `{colors.focus}` is unusable on this surface).

### Signature Components

**`hero-band`** — the sage-canvas hero band.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.xl}`. Headline in `{typography.display-mega}` (Wise Sans weight 900).

**`hero-band-dark`** — the polarity-flipped dark hero.
- Background `{colors.ink}`, text `{colors.primary}` (Wise green headline on near-black!), same padding / scale.

**`content-band`** — the white content band that follows hero.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.xl}`. Section headline in `{typography.display-md}`.
- States: **default** only. `hero-band`, `hero-band-dark` and `content-band` are layout bands, not controls; their interactive states belong to the buttons and cards they contain.

**`badge-positive`** — the positive status pill.
- Background `{colors.primary-pale}`, text `{colors.positive-deep}`, body in `{typography.body-sm-strong}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.pill}`.
- States: **default** only. The badge is a status output, never a control, so it has no hover, focus-visible, pressed, disabled, loading or selected state.

**`badge-negative`** — the negative status pill.
- Background `{colors.negative-bg}`, text `{colors.canvas-soft}` — the brand's near-white sage, the same token the dark `footer` uses for text on ink — body in `{typography.body-sm-strong}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.pill}`. The auto-derived block had bound this label to `{colors.on-primary}`, which is the near-black ink and measured 1.07:1 on the maroon ground.
- States: **default** only, as `badge-positive`.

### Examples (illustrative)

> Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`). Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently. `TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.
- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).
- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`
- The light text on the `{colors.ink}` fill is `{colors.primary}`, matching `card-feature-dark`; the auto-derived block had bound it to `{colors.on-primary}`, which is the same hex as the fill. Any focus ring inside this tier is `{colors.focus-on-dark}`.

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).
- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.
- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`
- States: **default** · **hover** fill `{colors.canvas-soft}` · **focus-visible** `{colors.focus}` ring at 2 px offset · **selected** 3 px `{colors.primary}` leading indicator plus `{colors.primary-pale}` fill · **disabled** label `{colors.mute}`.

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`
- States: **default** · **loading** on submit (the submit button carries the spinner; fields go `disabled`) · **error** form-level message in `{colors.negative-darkest}` above the first field. The card frame takes no hover, focus-visible, pressed or selected state.

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.
- Properties: `backgroundColor`, `rounded`, `padding`
- States: **default** only; it is a surface, not a control. On open, focus moves to the first focusable child and the `{colors.focus}` ring is visible there immediately.

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`


## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No durations, easing curves or choreography were extracted from Wise; nothing below is an observed fact. The values are the **Calm** profile from `theme-audit/SPEC.md` section 5, used verbatim so that every Calm file in this collection behaves as a sibling. The profile fits what the file *does* record: a single accent, no gradients, weight-900 type held still at hero scale, and surface contrast rather than shadow as the elevation cue — a composed, editorial system, not a springy one.

Tokens live in the `motion:` frontmatter group: `{motion.duration-instant}` 80 ms, `{motion.duration-fast}` 150 ms, `{motion.duration-base}` 250 ms, `{motion.duration-slow}` 400 ms, `{motion.duration-emphasis}` 500 ms, `{motion.ease-standard}`, `{motion.ease-enter}`, `{motion.ease-exit}`, `{motion.stagger-step}` 40 ms, `{motion.duration-reduced}` 150 ms.

### Interaction table

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav-link) | `{motion.duration-fast}` | `{motion.ease-standard}` | `background-color`, `color` — paint only, no travel | Unchanged; the colour swap carries the whole state on a near-monochrome brand |
| Press (button) | `{motion.duration-instant}` | `{motion.ease-standard}` | `background-color` to the pressed fill, plus `transform: scale(0.98)` | Scale removed; colour swap kept at `{motion.duration-instant}` |
| Focus (focus-visible ring) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the ring, drawn at full width from the first frame | Ring appears instantly, no fade |
| Page / route transition | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` 0→1 with `transform: translateY(8px)` → 0 | Travel removed; `opacity` only at `{motion.duration-reduced}` |
| Modal or drawer | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` plus `transform: translateY(12px)` (modal) or `translateX(100%)` (drawer); scrim `opacity` alone | Travel removed; scrim and panel fade at `{motion.duration-reduced}` |
| Dropdown / currency selector | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` plus `transform: translateY(-4px)` → 0 | Travel removed; `opacity` only at `{motion.duration-reduced}` |
| Toast | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` plus `transform: translateY(12px)` | Travel removed; `opacity` only at `{motion.duration-reduced}` |
| List enter (feature grid, currency rows) | `{motion.duration-base}` per item, `{motion.stagger-step}` 40 ms apart, capped at 6 items | `{motion.ease-enter}` | `opacity` plus `transform: translateY(8px)` | Stagger and travel removed; the whole list fades once at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` plus `transform: translateY(-4px)` | Travel removed; `opacity` only at `{motion.duration-reduced}` |
| Loading (rate fetch, button spinner) | 800 ms per rotation, infinite while pending | linear | `transform: rotate()` on the spinner; skeleton blocks pulse `opacity` 0.4↔1 at `{motion.duration-emphasis}` | Rotation and pulse frozen; a static `{colors.mute}` skeleton block with `aria-busy="true"` stands in |

### Rules this file follows

- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin` — layout-triggering properties are barred. Paint-only changes (`background-color`, `color`, `border-color`) are the brand's real hover and press states and use the same duration tokens.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content: the hero headline and the currency-converter card render immediately and are excluded from the list-enter stagger.
- The spinner and the skeleton pulse are the only infinite animations, and only while a request is pending. The brand has no ambient motion.
- Stagger is capped at 6 items so a long currency list never waits 400 ms for its last row.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale — page transitions, modal and drawer
     travel, dropdown and toast slide, list stagger, button press scale.    */
  /* Removed: the loader rotation and the skeleton opacity pulse, which are
     replaced by a static {colors.mute} block marked aria-busy.             */
  /* Kept:    opacity fades, clamped to {motion.duration-reduced} 150ms, and
     every paint-only hover / press / focus colour change at its own token. */
  *, *::before, *::after {
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important;
    scroll-behavior: auto !important;
  }
}
```

Nothing is made unusable by the rule: every state that signals something — hover, press, focus, error, selected, loading — is legible from colour, ring or static skeleton with all travel removed.

## Accessibility

### Measured contrast

Ratios computed with WCAG 2.1 relative luminance from this file's own hexes. The failures below are real properties of the brand palette, not oversights, and no identity hex was changed to clear a threshold.

**Passing — the pairs the brand leans on:**

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 19.23:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` | 15.98:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.primary-pale}` | 16.82:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 13.05:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas}` | 9.37:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas-soft}` | 7.79:1 | 4.5:1 | Pass |
| `{colors.primary}` on `{colors.ink}` | 13.05:1 | 4.5:1 | Pass (dark cards, dark hero, footer links) |
| `{colors.canvas-soft}` on `{colors.ink}` | 15.98:1 | 4.5:1 | Pass (footer body) |
| `{colors.canvas-soft}` on `{colors.negative-bg}` | 14.93:1 | 4.5:1 | Pass (`badge-negative`) |
| `{colors.positive-deep}` on `{colors.primary-pale}` | 8.76:1 | 4.5:1 | Pass (`badge-positive`) |
| `{colors.warning-content}` on `{colors.warning}` | 7.44:1 | 4.5:1 | Pass |
| `{colors.negative}` on `{colors.canvas}` | 5.01:1 | 4.5:1 | Pass |
| `{colors.negative-darkest}` on `{colors.canvas}` | 7.93:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.primary}` | 13.05:1 | 3.0:1 | Pass (the `{colors.ink}` hairline on tertiary buttons and inputs is 19.23:1 on `{colors.canvas}`) |

**Disclosed failures — the brand genuinely does not reach AA at these points:**

- `{colors.mute}` `#868685` on `{colors.canvas}` `#ffffff` measures **3.64:1**, short of the 4.5:1 that secondary text needs. Captions, placeholders and fine print set in this grey fail AA as normal-size text. It is usable only at 18.66 px+ or 14 px+ bold, where 3:1 applies.
- `{colors.mute}` on `{colors.canvas-soft}` `#e8ebe6` measures **3.03:1** — the same tone on the sage band, weaker still.
- `{colors.mute}` on `{colors.primary-pale}` `#e2f6d5` measures **3.19:1** — fails as text on the green feature card.
- `{colors.positive}` `#2ead4b` on `{colors.canvas}` measures **2.92:1**, below 4.5:1. The tone is a fill and icon colour, not a text colour; where success wording is needed, use `{colors.positive-deep}` `#054d28`, which measures 10.01:1 on `{colors.canvas}`.
- `{colors.warning}` `#ffd11a` on `{colors.canvas}` measures **1.46:1**, far below 4.5:1. Yellow at this luminance cannot carry text on white at any size. It is a fill only; text on it is `{colors.warning-content}` at 7.44:1.
- `{colors.warning-deep}` `#b86700` on `{colors.canvas}` measures **4.22:1** — it misses 4.5:1 by a narrow margin, so it passes for 18.66 px+ or 14 px+ bold text and fails for normal body.
- `{colors.accent-orange}` `#ffc091` on `{colors.canvas}` measures **1.59:1** and `{colors.accent-cyan}` `#38c8ff` measures **1.93:1**. Both are illustration accents, scoped to decoration; neither may be used for text or for a boundary that conveys meaning.
- Layer separation: `{colors.canvas-soft}` against `{colors.canvas}` measures **1.2:1**, and `{colors.primary-pale}` against `{colors.canvas}` measures **1.14:1**. The brand's stated elevation cue — a white card on a sage band — is therefore well below the 3:1 a meaningful non-text boundary would need. It reads because of the 24 px radius and the card's size, not because of luminance, and it will not survive greyscale or low-vision viewing. Anywhere the card boundary carries meaning rather than mood, add the `{colors.ink}` hairline that Level 1 already defines.

### Focus ring

No ring was extracted from the live site; both rings below are prescribed, and each reuses a hex the palette already owns rather than introducing a new brand colour.

- `{colors.focus}` `#163300` is the brand's existing `{colors.ink-deep}` forest green, promoted to a named role. It is the ring for every light surface: **13.93:1** on `{colors.canvas}`, **11.58:1** on `{colors.canvas-soft}`, **12.19:1** on `{colors.primary-pale}`, and **9.45:1** on `{colors.primary}` — all far past the 3:1 WCAG 2.2 Focus Appearance threshold.
- `{colors.focus-on-dark}` `#9fe870` is the brand's own `{colors.primary}`, used as the ring on the dark polarity the file documents (`card-feature-dark`, `hero-band-dark`, `footer`, `ex-pricing-tier-featured`, and the `{colors.negative-bg}` badge ground): **13.05:1** on `{colors.ink}` and **12.19:1** on `{colors.negative-bg}`. `{colors.focus}` on `{colors.ink}` would measure only 1.38:1, which is why a second ring is required rather than optional.
- Geometry: 2 px solid ring at a 2 px offset **outside** the control, so it is judged against the surface behind the control and never against a saturated CTA fill. The offset is what makes a single light-surface ring arithmetically possible.
- The ring is applied on `:focus-visible` only, never suppressed with `outline: none`, and is drawn at full size from its first frame — only its `opacity` animates.

### Tap targets

Computed from this file's own tokens, not from a rendered page: `button-primary` at `{spacing.md}` 12 px vertical padding plus the `{typography.button-md}` 24 px line box resolves to 48 px, and `button-icon-circular` at `{spacing.sm}` 8 px padding around a 24 px icon resolves to 40 px. 48 px clears the 44 px minimum comfortably; the 40 px icon button does not, and needs either `{spacing.md}` padding or an expanded hit area. Both figures are arithmetic on tokens — actual rendered size is not verifiable from a document.

### Reduced motion

Covered in full under Motion & Animation. In short: all travel and scale removed, opacity fades clamped to `{motion.duration-reduced}` 150 ms, loader rotation and skeleton pulse frozen in favour of a static block marked `aria-busy`.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` Wise green for every primary CTA. The lime-green pill IS the brand's conversion signature.
- Set hero headlines in `{typography.display-mega}` / `{typography.display-xl}` Wise Sans weight 900. Never lighter.
- Use `{rounded.xl}` 24 px for buttons and cards. The generous radius is the brand's friendliness signature.
- Cycle page surfaces in `{colors.canvas-soft}` sage canvas → `{colors.canvas}` white cards. Surface contrast carries elevation.
- Use the full semantic palette (positive / warning / negative) for in-product status — never repurpose Wise green as success indicator since it IS the brand CTA.

### Don't
- Don't introduce a second brand accent. Wise green is the sole identity colour.
- Don't render the hero in weight 700 or lighter. The brand's display weight is 900.
- Don't render CTAs as sharp rectangles. The 24 px pill geometry is non-negotiable.
- Don't pair the green CTA with a green background. The brand always sits Wise green on neutral surfaces (sage / white / ink).
- Don't replace Wise Sans with a generic geometric sans for hero typography — the proprietary face IS the brand's voice.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hero stacks; converter card full-width below headline; grids 1-up. |
| Tablet | 768–1023px | Grids 2-up. |
| Desktop | ≥ 1024px | Hero split; full grids. |

### Touch Targets
Buttons render ~48 px tall (12 vertical padding + 24 line). WCAG AAA at all widths.

### Image Behavior
Photography is sparse; the brand prefers illustrative SVGs and product mockups inside cards. Country flag thumbnails appear inside currency rows.

## Known Gaps

- **Motion is prescribed, not extracted.** Every duration, easing curve and choreography decision in Motion & Animation comes from the Calm profile in `theme-audit/SPEC.md`. No real Wise timing was observed. The 800 ms spinner rotation is a convention, not a measurement.
- **The focus ring is prescribed.** Wise's real ring was not observed. `{colors.focus}` and `{colors.focus-on-dark}` reuse `{colors.ink-deep}` and `{colors.primary}`; the 2 px width and 2 px offset are prescribed geometry.
- **No shadow tokens, deliberately.** The file documents no `rgba(...)` elevation value, so no `shadow:` group is defined. Two example entries nonetheless describe themselves as having an "elevated shadow" (`ex-modal-card`) and a "medium shadow" (`ex-toast`) — those are leftovers from the auto-derived kit mirror and reference values this brand does not document. Elevation here is surface contrast plus the Level 1 `{colors.ink}` hairline, nothing else.
- **The Touch Targets line above is a rendering claim this document cannot support.** It is kept verbatim as extracted, but "WCAG AAA at all widths" was never measured against a rendered page, and the arithmetic in Accessibility puts `button-icon-circular` at 40 px, under the 44 px minimum. Treat it as an intent, not a verified result.
- **Overlap, overflow, clipping, frame rate and layout shift are not assessed.** They need a running page; nothing in this document speaks to them.
- **`{colors.primary-neutral}`, `{colors.negative-deep}` and `{colors.positive}` have no component binding.** They are documented in Colors with a stated purpose but no entry in `components:` draws them, so their contrast is only checkable against assumed grounds.
- **Font stack is a substitute, not the real thing.** Wise Sans is proprietary; anyone building on this document renders Inter 900 or Manrope 800/900 instead, which changes the hero's optical weight.
- **Dark mode is not a documented theme.** The file has dark *surfaces* (`card-feature-dark`, `hero-band-dark`, `footer`) inside a light-canvas system, but no dark-canvas token set. The second focus ring exists for those surfaces, not for a dark theme.
