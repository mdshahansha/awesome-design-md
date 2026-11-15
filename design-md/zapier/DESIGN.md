---
version: alpha
name: Zapier-Inspired-design-analysis
description: An inspired interpretation of Zapier's design language — a workflow-automation platform whose surface combines warm-cream neutrals (`#fffefb` canvas, `#f8f4f0` soft cream) with deep coffee ink (`#201515`) and a single saturated orange CTA accent (`#ff4f00`); typography pairs the proprietary Degular Display family at hero scale with Inter for sub-displays and body, giving the brand a confident-warm rather than cool-tech voice.

colors:
  primary: "#ff4f00"
  on-primary: "#fffefb"
  ink: "#201515"
  ink-soft: "#2f2a26"
  ink-mid: "#36342e"
  body: "#605d52"
  body-mid: "#939084"
  mute: "#c5c0b1"
  canvas: "#fffefb"
  canvas-soft: "#f8f4f0"
  focus: "#ff4f00"

typography:
  display-xl:
    fontFamily: Degular Display, Inter, system-ui, -apple-system, sans-serif
    fontSize: 56px
    fontWeight: 500
    lineHeight: 56px
  display-lg:
    fontFamily: Degular Display, Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 500
    lineHeight: 48px
  display-md:
    fontFamily: Degular Display, Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 500
    lineHeight: 36px
    letterSpacing: 1px
  display-sub-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 500
    lineHeight: 49.92px
  display-sub-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 400
    lineHeight: 40px
  display-sub-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 30px
    letterSpacing: -0.6px
  display-xs:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 700
    lineHeight: 25px
    letterSpacing: -0.5px
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 30px
    letterSpacing: -0.2px
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 27px
  body-md-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 27px
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-sm-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
  caption:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 21px
  eyebrow-uppercase:
    fontFamily: Degular Display, Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 14px
    letterSpacing: 1px
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 27px
  button-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 14.4px
    letterSpacing: 0.144px

rounded:
  none: 0px
  sm: 6px
  md: 12px
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
  4xl: 64px

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
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.xl}"
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.xl}"
  button-text:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  card-content:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  card-feature-cream:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  card-feature-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  pricing-card-featured:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.4xl} {spacing.xl}"
  hero-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.4xl} {spacing.xl}"
  content-band-cream:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.4xl} {spacing.xl}"
  content-band-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.4xl} {spacing.xl}"
  eyebrow-uppercase:
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow-uppercase}"
  badge-pill:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
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
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
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
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Zapier is the original "connect your apps" workflow automation platform — and the marketing surface today reads as confidently-mature. The brand pairs a warm-cream canvas `{colors.canvas}` (`#fffefb`) with a deep coffee-ink `{colors.ink}` (`#201515`) and a single saturated orange `{colors.primary}` (`#ff4f00`) CTA. The warmth in the neutrals — slightly cream rather than pure white — is the brand's defining temperature signal.

Type carries the second voice. The proprietary `Degular Display` family carries hero displays at weight 500. The brand uses `Inter` for everything else — sub-displays, body, button, eyebrow. The two-face pairing reads as "the brand has its own typeface for the loud moments and uses the workhorse for the rest" — modest and unflashy.

Cards are universally `{rounded.md}` 12 px. Buttons share the same 12 px radius — not pills, not square. The brand sits between the friendly-rounded and the technical-square camps with a deliberate middle position.

**Key Characteristics:**
- A single primary CTA color `{colors.primary}` (`#ff4f00`) — saturated orange. The brand's conversion signature.
- Warm-cream canvas `{colors.canvas}` (`#fffefb`) — not pure white. The temperature IS the brand voice.
- Deep coffee ink `{colors.ink}` (`#201515`) — not pure black. Warmth carries through to text.
- Proprietary Degular Display for hero-scale, Inter for everything else. Two-face system.
- `{rounded.md}` 12 px for buttons and cards — the brand's middle-radius signature.
- A muted cream / coffee neutral ladder — `{colors.canvas-soft}` (`#f8f4f0`), `{colors.mute}` (`#c5c0b1`), `{colors.body-mid}` (`#939084`), `{colors.body}` (`#605d52`) — every neutral carries warmth, none are cool grey.

## Colors

### Brand & Accent
- **Zapier Orange** (`{colors.primary}` — `#ff4f00`): The single brand accent. Every primary CTA pill, every conversion target. The saturated orange IS the brand.

### Surface
- **Canvas** (`{colors.canvas}` — `#fffefb`): Warm off-white page background.
- **Canvas Soft** (`{colors.canvas-soft}` — `#f8f4f0`): Cream-tinted soft surface for cards / inset regions.

### Text
- **Ink** (`{colors.ink}` — `#201515`): Deep coffee — every heading and primary text.
- **Ink Soft** (`{colors.ink-soft}` — `#2f2a26`): Near-black with brown warmth.
- **Ink Mid** (`{colors.ink-mid}` — `#36342e`): Mid-emphasis text.
- **Body** (`{colors.body}` — `#605d52`): Default body text color.
- **Body Mid** (`{colors.body-mid}` — `#939084`): Secondary body / metadata.
- **Mute** (`{colors.mute}` — `#c5c0b1`): Decorative only. At 1.8:1 on `{colors.canvas}` and 1.66:1 on `{colors.canvas-soft}` this tone fails AA for text and fails the 3:1 non-text threshold for any boundary that must be seen. It is the brand's extracted lightest neutral and is kept as extracted; use it for ornament, never for fine print, captions or a divider that carries meaning. Boundaries that must be seen use `{colors.ink}` (17.65:1 on canvas), which is what the brand already draws for pricing-card chrome and outline buttons.

### Focus
- **Focus Ring** (`{colors.focus}` — `#ff4f00`): The ring reuses the brand's existing orange `{colors.primary}`; it is the same hex, not a new brand colour. One ring serves both polarities because it clears 3:1 on every surface this file defines — see **Accessibility**.

### Semantic
The brand doesn't surface a separate semantic palette on its marketing pages. Status / validation cues borrow from the ink + orange hierarchy.

## Typography

### Font Family
Two faces ladder the system:
1. **Degular Display** — proprietary geometric display sans used for hero headlines at weight 500. The brand's typographic signature.
2. **Inter** — used for sub-displays, body, links, buttons, and eyebrows. Weights 400 / 500 / 600 / 700 are present.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 56px | 500 | 56px | 0 | Hero headline (Degular Display). |
| `{typography.display-lg}` | 48px | 500 | 48px | 0 | Sub-hero displays (Degular Display). |
| `{typography.display-md}` | 32px | 500 | 36px | 1px | Section displays (Degular Display, positive tracking). |
| `{typography.display-sub-lg}` | 48px | 500 | 49.92px | 0 | Inter-rendered sub-display. |
| `{typography.display-sub-md}` | 32px | 400 | 40px | 0 | Inter sub-display. |
| `{typography.display-sub-sm}` | 24px | 600 | 30px | -0.6px | Card titles (Inter, semibold). |
| `{typography.display-xs}` | 20px | 700 | 25px | -0.5px | Inline display micro-headings. |
| `{typography.body-lg}` | 20px | 400 | 30px | -0.2px | Lead paragraphs. |
| `{typography.body-md}` | 18px | 400 | 27px | 0 | Default body. |
| `{typography.body-md-strong}` | 18px | 600 | 27px | 0 | Bolded inline body. |
| `{typography.body-sm}` | 16px | 400 | 24px | 0 | Secondary body. |
| `{typography.body-sm-strong}` | 16px | 600 | 24px | 0 | Bold caption. |
| `{typography.caption}` | 14px | 400 | 21px | 0 | Fine print. |
| `{typography.eyebrow-uppercase}` | 14px | 500 | 14px | 1px | UPPERCASE eyebrow (Degular Display, positive tracking). |
| `{typography.button-md}` | 18px | 600 | 27px | 0 | Primary button label. |
| `{typography.button-sm}` | 14.4px | 700 | 14.4px | 0.144px | Small button label. |

### Principles
- **Degular Display 500 for hero, Inter for everything else.** Strict role separation.
- **Positive tracking on the Degular eyebrow** — `1 px` at 14 px is the brand's signature label style.
- **Sentence-case headlines.** The brand never uppercases display sizes.

### Note on Font Substitutes
Degular Display is proprietary. Open-source substitutes:
- **Display** — *Inter* weight 500 at hero scale comes closest. *Mona Sans* weight 500 is a softer alternative.
- **Sub-display + body** — *Inter* is the brand's actual second face.

## Layout

### Spacing System
- **Base unit**: 4 px.
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 24 px · `{spacing.2xl}` 32 px · `{spacing.3xl}` 48 px · `{spacing.4xl}` 64 px.
- **Section padding**: bands use `{spacing.4xl}` 64 px top/bottom.
- **Card interior**: cards at `{spacing.xl}` 24 px.

### Grid & Container
- Marketing container ~1280 px wide; centred with gutters.
- Hero: split at desktop (headline left, illustration right); stacked at mobile.
- Pricing tier grid: 3 / 4-up at desktop.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default for hero. |
| Level 1 — Hairline | 1 px solid `{colors.ink}` border. | Pricing-tier card chrome, outline buttons. |
| Level 2 — Soft Card | `{colors.canvas-soft}` cream fill against `{colors.canvas}` page. | Default content cards — surface contrast carries elevation. |

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed bands. |
| `{rounded.sm}` | 6px | Inline pills, form inputs. |
| `{rounded.md}` | 12px | The brand's canonical button + card radius. |
| `{rounded.pill}` | 9999px | Status pills, badges. |
| `{rounded.full}` | 9999px | Circular icon containers. |

## Components

### Buttons

**`button-primary`** — the orange CTA.
- Background `{colors.primary}`, text `{colors.on-primary}` (warm white), label `{typography.button-md}`, padding `{spacing.md} {spacing.xl}`, shape `{rounded.md}` 12 px.

**`button-secondary`** — the dark coffee-ink CTA.
- Background `{colors.ink}`, text `{colors.on-primary}`, same typography / padding / shape.

**`button-tertiary`** — the outline CTA.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, same typography / padding / shape.

**`button-text`** — text-only CTA used inside cards / nav.
- Background `{colors.canvas}`, text `{colors.ink}`, body in `{typography.button-sm}`, padding `{spacing.sm} {spacing.lg}`, shape `{rounded.md}`.

### Cards & Containers

**`card-content`** — the default cream content card.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.md}`.

**`card-feature-cream`** — the cream feature card.
- Same chrome as `card-content`. Hosts headline + body + illustration.

**`card-feature-dark`** — the polarity-flipped dark coffee card.
- Background `{colors.ink}`, text `{colors.on-primary}`, padding `{spacing.xl}`, shape `{rounded.md}`.

**`pricing-card`** — the default pricing tier card.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, padding `{spacing.xl}`, shape `{rounded.md}`.

**`pricing-card-featured`** — the polarity-flipped featured pricing tier.
- Background `{colors.ink}`, text `{colors.on-primary}`, same shape / padding.

### Inputs & Forms

**`text-input`** — the canonical text input.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, body in `{typography.body-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.sm}` 6 px.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.xl}`.

**`nav-link`** — link items inside nav.
- Text `{colors.ink}`, set in `{typography.body-sm}`.

**`footer`** — the dark coffee footer.
- Background `{colors.ink}`, text `{colors.canvas-soft}`, padding `{spacing.3xl} {spacing.xl}`. Body in `{typography.body-sm}`.

### Signature Components

**`hero-band`** — the cream hero band.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.4xl} {spacing.xl}`. Headline in `{typography.display-xl}` (Degular Display 56 px / 500).

**`hero-band-dark`** — the polarity-flipped dark coffee hero.
- Background `{colors.ink}`, text `{colors.on-primary}`, same scale.

**`content-band-cream`** — the cream content band that follows hero.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.4xl} {spacing.xl}`. Section headline in `{typography.display-lg}`.

**`content-band-light`** — the white content band.
- Background `{colors.canvas}`, text `{colors.ink}`, same padding / scale.

**`eyebrow-uppercase`** — the small UPPERCASE Degular eyebrow above section headlines.
- Text `{colors.ink}`, set in `{typography.eyebrow-uppercase}` (14 px / 500 / `1 px` tracking).

**`badge-pill`** — the inline pill for metadata / tag.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, body in `{typography.body-sm}`, padding `{spacing.xs} {spacing.md}`, shape `{rounded.pill}`.

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

### Interaction States

Which states each entry above supports. The state *set* is prescribed, not extracted: the source records only the default appearance of each component, plus the `{colors.primary}` active indicator on `ex-app-shell-row`. Exact hover and pressed hexes were not extracted — see **Known Gaps**. Where a state is listed, it is paint-only (`background-color`, `color`, `border-color`) unless the row says otherwise; a paint-only change is the whole state on a near-monochrome warm palette, and the ring is `{colors.focus}`.

| Component | States |
|---|---|
| `button-primary` | default · hover (fill darkens) · focus-visible (`{colors.focus}` ring) · pressed (scale 0.98) · disabled · loading |
| `button-secondary` | default · hover (fill lightens toward `{colors.ink-mid}`) · focus-visible · pressed (scale 0.98) · disabled · loading |
| `button-tertiary` | default · hover (fill to `{colors.canvas-soft}`) · focus-visible · pressed (scale 0.98) · disabled |
| `button-text` | default · hover (text to `{colors.primary}`) · focus-visible · pressed · disabled |
| `text-input` | default · hover (border to `{colors.ink}` at full weight) · focus-visible (`{colors.focus}` ring, 2 px, 2 px offset) · disabled · error (border and message in `{colors.primary}`, the only signal colour the brand owns) |
| `card-content` | default and hover only — a static content surface, no pressed, selected or error state. |
| `card-feature-cream` | default and hover only — static content surface. |
| `card-feature-dark` | default and hover only — static content surface. |
| `pricing-card` | default · hover (border weight unchanged, fill to `{colors.canvas-soft}`) · focus-visible · selected (promotes to `pricing-card-featured` chrome) |
| `pricing-card-featured` | default · hover · focus-visible · selected (its resting state in the tier grid) |
| `nav-bar` | default only — a container, not an interactive target. |
| `nav-link` | default · hover (text to `{colors.primary}`) · focus-visible · pressed · selected (current page) |
| `footer` | default only — a container. |
| `hero-band` / `hero-band-dark` | default only — bands, not interactive targets. |
| `content-band-cream` / `content-band-light` | default only — bands. |
| `eyebrow-uppercase` | default only — a label. |
| `badge-pill` | default · selected (fill to `{colors.ink}`, text to `{colors.on-primary}`) · disabled. No hover: badges are not targets unless used as a filter chip. |
| `ex-pricing-tier` / `ex-pricing-tier-featured` | default · hover · focus-visible · selected |
| `ex-product-selector` | default · hover · focus-visible · selected |
| `ex-cart-drawer` | default · loading (summary rows skeleton) · error (totals unavailable) |
| `ex-app-shell-row` | default · hover · focus-visible · pressed · selected (`{colors.primary}` indicator) · disabled |
| `ex-data-table-cell` | default · hover (row) · selected (row) · loading (skeleton rows) |
| `ex-auth-form-card` | default · loading (submit in flight) · error (field-level and form-level) |
| `ex-modal-card` | default · loading · error |
| `ex-empty-state-card` | default · loading (before first fetch resolves) |
| `ex-toast` | default · error (variant) · hover (pauses auto-dismiss) |


## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or stagger below is an extracted fact: the source for this file records colour, type, spacing, radius and component chrome only. Treat every value as a starting point that fits the brand, not as documentation of what zapier.com actually does.

The profile is **Playful** — responsive and friendly, with overshoot on entrance and a small scale pop on press. The warrant is in the brand itself: a single saturated `{colors.primary}` orange carried on every interactive CTA, an illustration-led surface of zap and workflow SVGs with photography rare, a 12 px middle radius and pill badges. The warm-cream temperature keeps it friendly rather than loud, so travel distances stay small — the pop is 2% of scale, not a bounce.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, nav link) | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `background-color`, `color`, `border-color` — paint only, no travel | Unchanged. Paint-only state changes are not motion; they stay at `{motion.duration-reduced}` 130ms. |
| Press / active | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed. The press reads through its paint change alone. |
| Focus (ring appears) | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` on the `{colors.focus}` ring | Unchanged — already opacity-only at 70ms. |
| Page / route transition | enter `{motion.duration-base}` 200ms, exit `{motion.duration-fast}` 130ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` + `transform: translateY(8px)` | Travel removed. Opacity cross-fade at `{motion.duration-reduced}` 130ms. Nothing animates on first paint; the initial route renders at rest. |
| Modal / drawer | enter `{motion.duration-base}` 200ms, exit `{motion.duration-fast}` 130ms | enter `{motion.ease-enter}` (overshoot), exit `{motion.ease-exit}` | `opacity` + `transform: scale(0.98→1)`; drawer `transform: translateX(100%→0)` | Scale and translate removed. Opacity fade at `{motion.duration-reduced}` 130ms. Backdrop fades, never slides. |
| Dropdown / menu | enter `{motion.duration-fast}` 130ms, exit `{motion.duration-instant}` 70ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` + `transform: translateY(-4px→0)` | Travel removed. Opacity fade at `{motion.duration-reduced}` 130ms. |
| Toast | enter `{motion.duration-base}` 200ms, exit `{motion.duration-fast}` 130ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` + `transform: translateY(12px→0)` | Travel removed. Opacity fade at `{motion.duration-reduced}` 130ms. Auto-dismiss timing is unchanged. |
| List enter (tier grid, table rows, app cards) | `{motion.duration-base}` 200ms per item, `{motion.stagger-step}` 60ms between items | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px)` | Stagger and travel removed. All items fade together at `{motion.duration-reduced}` 130ms. |
| List exit | `{motion.duration-fast}` 130ms, no stagger | `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)` | Scale removed. Opacity fade at `{motion.duration-reduced}` 130ms. |
| Loading (skeleton, button spinner) | `{motion.duration-emphasis}` 450ms loop | `{motion.ease-standard}` | `opacity` pulse on skeleton blocks; `transform: rotate()` on the spinner | Loop frozen. Skeletons hold one static opacity and the spinner becomes a static indicator; the loading state is still announced in text. |

Rules this file follows:
- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin` — they trigger layout. Paint-only changes (`background-color`, `color`, `border-color`) are permitted and use the same duration token as any other state change.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content.
- No infinite animation except the loading indicators above. The brand ships no ambient motion.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate, scale and rotate; every stagger; the loader loop. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} 130ms, and all
     paint-only state changes (background-color, color, border-color). */
  *, *::before, *::after {
    animation-duration: 130ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 130ms !important;
    transform: none !important;
  }
}
```

Removed under reduce: the press scale pop, the modal and drawer scale and slide, every `translateY` on page transitions, dropdowns, toasts and list enter, the `{motion.stagger-step}` cascade, and the loader's loop. Kept: opacity fades at `{motion.duration-reduced}` 130ms, the focus ring (already opacity-only), and every paint-only hover and selected state.

## Accessibility

### Measured contrast

WCAG 2.1 relative luminance, computed from this file's own hexes.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#201515` on `{colors.canvas}` `#fffefb` | 17.65:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` `#f8f4f0` | 16.27:1 | 4.5:1 | Pass |
| `{colors.ink-soft}` `#2f2a26` on `{colors.canvas}` | 14.07:1 | 4.5:1 | Pass |
| `{colors.ink-mid}` `#36342e` on `{colors.canvas}` | 12.34:1 | 4.5:1 | Pass |
| `{colors.body}` `#605d52` on `{colors.canvas}` | 6.54:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas-soft}` | 6.03:1 | 4.5:1 | Pass |
| `{colors.on-primary}` `#fffefb` on `{colors.ink}` | 17.65:1 | 4.5:1 | Pass |
| `{colors.canvas-soft}` on `{colors.ink}` (footer text) | 16.27:1 | 4.5:1 | Pass |
| `{colors.ink}` border on `{colors.canvas}` | 17.65:1 | 3:1 | Pass |
| `{colors.focus}` `#ff4f00` on `{colors.canvas}` | 3.27:1 | 3:1 | Pass |
| `{colors.focus}` on `{colors.canvas-soft}` | 3.01:1 | 3:1 | Pass, with no margin |
| `{colors.focus}` on `{colors.ink}` | 5.40:1 | 3:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` `#ff4f00` | 3.27:1 | 4.5:1 | **Fail** |
| `button-primary` label on its orange fill | 3.27:1 | 4.5:1 | **Fail** |
| `{colors.body-mid}` `#939084` on `{colors.canvas}` | 3.17:1 | 4.5:1 | **Fail** |
| `{colors.body-mid}` on `{colors.canvas-soft}` | 2.92:1 | 4.5:1 | **Fail** |
| `{colors.mute}` `#c5c0b1` on `{colors.canvas}` | 1.8:1 | 4.5:1 | **Fail** |
| `{colors.mute}` on `{colors.canvas-soft}` | 1.66:1 | 4.5:1 and 3:1 as a boundary | **Fail** |

### Where the real brand fails AA, plainly

- **Warm white on Zapier orange is 3.27:1.** The brand's signature CTA — `{colors.on-primary}` `#fffefb` on `{colors.primary}` `#ff4f00` — does not reach the 4.5:1 that normal-size text needs. It clears the 3:1 large-text threshold, and `{typography.button-md}` is 18 px at weight 600, which is *below* the 18.66 px / 700 that WCAG counts as large text. So as specified, `button-primary` fails AA. Both hexes are extracted brand identity and are not changed here. The defensible fixes are: set the label at `{typography.display-xs}` 20 px / 700 or larger, where 3:1 applies; or ink the label in `{colors.ink}` (5.40:1 on the orange) and keep warm white only for display-scale CTAs. Both are decisions for the brand owner, not this audit.
- **`{colors.body-mid}` `#939084` is 3.17:1 on canvas and 2.92:1 on canvas-soft.** The file documents it as "secondary body / metadata", which is normal-size text: it fails AA at both. Use `{colors.body}` `#605d52` (6.54:1 / 6.03:1) for any metadata a reader must read, and keep `body-mid` for 24 px+ or 18.66 px/700+ text, where 3:1 applies — a threshold it still misses on `{colors.canvas-soft}`.
- **`{colors.mute}` `#c5c0b1` is 1.8:1 on canvas and 1.66:1 on canvas-soft.** It fails AA as text by a wide margin and fails the 3:1 non-text threshold as a boundary. It is extracted and kept as extracted, scoped to decoration. Nothing in the palette between `mute` and `{colors.body}` passes, and no parallel accessible neutral is invented here, because the brand already owns a boundary tone that passes: `{colors.ink}` at 17.65:1, which the Elevation ladder already uses for card chrome and outline buttons.
- The `ex-*` illustrative entries still bind `{colors.mute}` as `borderColor`, `item-divider` and `rowBorder`. Those bindings are left exactly as generated; re-pointing them at `{colors.ink}` is a brand-owner decision and is logged for approval rather than made here. Any divider that carries meaning should use `{colors.ink}`.

### Focus ring

- `{colors.focus}` is `#ff4f00` — the same hex as `{colors.primary}`, reused, not a new brand colour.
- **One ring serves both polarities.** This file documents light cream surfaces (`{colors.canvas}`, `{colors.canvas-soft}`) and dark coffee surfaces (`{colors.ink}` behind `card-feature-dark`, `hero-band-dark`, `pricing-card-featured`, `footer`). The orange is mid-luminance, so it clears 3:1 against all three: 3.27:1, 3.01:1 and 5.40:1. A light/dark ring pair would add a token without adding coverage.
- **Geometry and offset:** 2 px ring, 2 px offset, drawn *outside* the control, so it is judged against the surface behind the control rather than the control's own fill. This matters on `button-primary`, whose fill is the ring's own colour: against that orange fill the ring would be 1:1, and the 2 px offset of bare canvas is what separates them. On `{colors.canvas-soft}` the margin is 0.01 over threshold, so the offset is not optional — do not drop it to save space.
- The ring is visible on every surface this file defines. It never relies on colour alone: it is a ring, a shape change, and `text-input` pairs it with its error message in text.

### Minimum tap target

Computed from this file's tokens, not measured on a rendered page: `button-primary` is `{spacing.md}` 12 px padding top and bottom plus `{typography.button-md}`'s 27 px line box — 51 px tall, clearing both the 44 px of WCAG 2.5.5 and the 24 px of 2.5.8. `button-text` is `{spacing.sm}` 8 px plus a 14.4 px line box — 30.4 px, which clears 2.5.8 but **not** the 44 px of 2.5.5; give it 44 px of hit area where it stands alone rather than inline in a sentence. Actual rendered sizes are untested here — see **Known Gaps**.

### Reduced motion

Honoured as specified in **Motion & Animation**: all travel, scale and stagger removed, opacity fades capped at `{motion.duration-reduced}` 130ms, loader loops frozen. No content depends on motion to be understood.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` Zapier orange for every primary CTA. The saturated orange IS the conversion signature.
- Keep canvas WARM — `{colors.canvas}` `#fffefb` cream, not pure white. The temperature is the brand voice.
- Set hero headlines in `{typography.display-xl}` Degular Display weight 500. Sentence-case, no uppercase.
- Pair Degular Display (hero, eyebrow) with Inter (everything else). Two faces, two roles.
- Use `{rounded.md}` 12 px for buttons + cards. The middle radius is the brand's signature.
- Pair orange CTA with ink-dark text on cream backgrounds — the three-token rhythm is the brand's whole conversion story.

### Don't
- Don't replace cream canvas with pure white. The warmth is the brand.
- Don't use pure black ink. The coffee-warmth in `#201515` carries through every text color.
- Don't render CTAs as pills. The brand's button is 12 px rounded rectangle.
- Don't introduce a second chromatic accent. Orange + cream + coffee is the entire palette.
- Don't substitute Degular Display with a cool geometric sans (e.g., generic Helvetica) — the brand's display face has warm proportions that the substitute doesn't capture.
- Don't set normal-size text in `{colors.body-mid}` or `{colors.mute}`. Both fail AA on both cream surfaces — see **Accessibility**.
- Don't drop the focus ring's 2 px offset. On `{colors.canvas-soft}` the ring passes by 0.01, and on `button-primary` the offset is the only thing separating the ring from the fill it surrounds.

## Responsive Behavior

Moved verbatim from the Layout section, where this file originally carried it as a subsection.

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hero stacks; grids 1-up; hamburger nav. |
| Tablet | 768–1023px | 2-up grids. |
| Desktop | ≥ 1024px | Full grids; hero split. |

### Touch Targets
Buttons render ~48 px tall (12 vertical padding + 27 line). WCAG AAA met.

### Image Behavior
The brand uses illustrative SVGs of zaps / workflows + product screenshots inside `{rounded.md}` framed cards. Photography is rare.

## Known Gaps

- **No motion value in this file is extracted.** The whole `motion:` group and the whole Motion & Animation section are the prescribed **Playful** profile from the audit spec. Nobody measured zapier.com's real durations, easing curves or stagger. If a real timing is ever extracted, it displaces the profile value and should be labelled extracted at that point.
- **No shadow values.** The Elevation ladder is flat / hairline / cream-fill only, so no `shadow:` group is defined — correctly, since the file documents no real shadow value. Two `ex-*` descriptions nonetheless mention an "elevated shadow" (`ex-modal-card`) and a "medium shadow" (`ex-toast`) with no token behind either. Those phrases come from the auto-derived examples generator, not from the brand; the modal and toast surfaces as specified here carry no shadow.
- **Hover and pressed hexes are not extracted.** The Interaction States table names which property each state changes and in which direction, but the exact hover fill for `button-primary` and `button-secondary` is unknown. No hex was invented for it.
- **No semantic palette.** The brand surfaces no success / warning / info colours on its marketing pages, so the error state borrows `{colors.primary}`. That is a documented borrow, not an extracted semantic token, and it means error and primary-action share one colour — a real limitation of the palette.
- **No dark theme.** The file has dark *surfaces* (`{colors.ink}` cards, bands and footer) but no dark canvas, so no second polarity of neutrals exists. The single focus ring is sized for that fact.
- **Tap targets are computed, never rendered.** This repo has no dev server, DOM or screenshot, so overlap, overflow, clipping, real tap-target size, frame rate and layout shift are all untested. The Responsive Behavior section's "~48 px" is the file's original figure; the token arithmetic in **Accessibility** gives 51 px (12 + 12 + 27). Both are arithmetic, neither is measured.
- **Degular Display is proprietary.** Weights beyond 500 are not documented, and the substitute ladder in Typography is a recommendation, not an extracted equivalence.
- **`{colors.focus}` is prescribed, not extracted.** No focus ring was observed on the live site; the role is bound to the brand's existing orange so the ring is addressable and measurable. Its hex is a brand fact; its *use as a ring* is this audit's prescription.
