---
version: alpha
name: Starbucks-design-analysis
description: A warm, confident retail flagship. The canvas is a neutral-warm cream (#f2f0eb) with a ceramic off-white sibling (#edebe9); white cards sit on it at 12px radius under whisper-soft stacked shadows, and a four-tier green system (Starbucks #006241 for headings, Green Accent #00754A for CTAs, House Green #1E3932 for deep bands and footers, Green Uplift #2b5148 for decoration) carries the brand. Gold (#cba258) is reserved for Rewards-status ceremony. Every button is a 50px full pill that presses with transform scale(0.95); the 56px circular Frap order button is the signature elevation element. SoDoSans carries nearly every surface at -0.16px tracking, with a Rewards serif and a Careers script in two tightly scoped contexts. Every colour, type, spacing, radius, shadow and component value below is read from this file's own prose; the motion group and the focus rings are prescribed, not measured.

colors:
  canvas: "#f2f0eb"
  surface: "#ffffff"
  surface-cool: "#f9f9f9"
  surface-ceramic: "#edebe9"
  surface-gold-wash: "#faf6ee"
  accent: "#00754A"
  on-accent: "#ffffff"
  green-starbucks: "#006241"
  green-house: "#1E3932"
  green-uplift: "#2b5148"
  green-light: "#d4e9e2"
  green-consent: "#008248"
  gold: "#cba258"
  gold-light: "#dfc49d"
  black: "#000000"
  text: "rgba(0, 0, 0, 0.87)"
  text-dim: "rgba(0, 0, 0, 0.58)"
  text-white: "rgba(255, 255, 255, 1)"
  text-white-soft: "rgba(255, 255, 255, 0.70)"
  rewards-green: "#33433d"
  error: "#c82014"
  warning: "#fbbc05"
  tint-valid: "hsl(160 32% 87% / 33%)"
  tint-invalid: "hsl(4 82% 43% / 5%)"
  border-input: "#d6dbde"
  border-hairline: "#e7e7e7"
  focus: "#00754A"
  focus-on-dark: "#ffffff"

typography:
  display:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 400-600
    lineHeight: 1.2
    letterSpacing: -0.16px
  jumbo:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 58px
    fontWeight: 400-600
    lineHeight: 1.2
    letterSpacing: -0.16px
  hero-large:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 45px
    fontWeight: 400-600
    lineHeight: 1.2-1.5
    letterSpacing: -0.16px
  h1:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 36px
    letterSpacing: -0.16px
  h2:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 36px
    letterSpacing: -0.16px
  body-large:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 400-600
    lineHeight: 33.25px
    letterSpacing: -0.16px
  body:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: -0.01em
  small:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400-600
    lineHeight: 1.5
    letterSpacing: -0.01em
  micro:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.01em
  button-label:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14-16px
    fontWeight: 400-600
    lineHeight: 1.2
    letterSpacing: -0.01em
  rewards-serif:
    fontFamily: "Lander Tall, Iowan Old Style, Georgia, serif"
  careers-script:
    fontFamily: "Kalam, Comic Sans MS, cursive"

spacing:
  space-1: 0.4rem
  space-2: 0.8rem
  space-3: 1.6rem
  space-4: 2.4rem
  space-5: 3.2rem
  space-6: 4rem
  space-7: 4.8rem
  space-8: 5.6rem
  space-9: 6.4rem
  gutter: 1.6rem
  gutter-md: 2.4rem
  gutter-lg: 4.0rem
  field-padding: 12px
  modal-padding: 2.4rem
  modal-top-padding: 8.8rem

rounded:
  input: 4px
  card: 12px
  tab-top: "12px 12px 0 0"
  pill: 50px
  circle: 50%
  svc: "3.3333%/5.298%"

shadow:
  card: "0 0 0.5px rgba(0,0,0,0.14), 0 1px 1px rgba(0,0,0,0.24)"
  nav: "0 1px 3px rgba(0,0,0,0.1), 0 2px 2px rgba(0,0,0,0.06), 0 0 2px rgba(0,0,0,0.07)"
  frap-base: "0 0 6px rgba(0,0,0,0.24)"
  frap-ambient: "0 8px 12px rgba(0,0,0,0.14)"
  frap-ambient-pressed: "0 8px 12px rgba(0,0,0,0)"
  svc: "drop-shadow(0 4px 1px rgba(0,0,0,0.11)) drop-shadow(0 0 2px rgba(0,0,0,0.24))"

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
  button-primary-filled:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    borderColor: "{colors.accent}"
    typography: "{typography.button-label}"
    rounded: "{rounded.pill}"
    padding: "7px 16px"
  button-primary-outlined:
    backgroundColor: transparent
    textColor: "{colors.accent}"
    borderColor: "{colors.accent}"
    typography: "{typography.button-label}"
    rounded: "{rounded.pill}"
    padding: "7px 16px"
  button-black-filled:
    backgroundColor: "{colors.black}"
    textColor: "{colors.text-white}"
    borderColor: "{colors.black}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: "7px 16px"
  button-dark-outlined:
    backgroundColor: "{colors.surface}"   # transparent fill; drawn on the white nav
    textColor: "{colors.text}"
    borderColor: "{colors.text}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: "7px 16px"
  button-inverted-on-green:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.accent}"
    borderColor: "{colors.surface}"
    typography: "{typography.button-label}"
    rounded: "{rounded.pill}"
  button-outlined-on-dark:
    backgroundColor: "{colors.green-house}"   # transparent fill; the ground it is drawn on
    textColor: "{colors.text-white}"
    borderColor: "{colors.text-white}"
    typography: "{typography.button-label}"
    rounded: "{rounded.pill}"
  button-consent-agree:
    backgroundColor: "{colors.green-consent}"
    textColor: "{colors.text-white}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: "7px 16px"
  frap-floating-order:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.circle}"
    shadow: "{shadow.frap-base}"
  feedback-tab:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text-white}"
    typography: "{typography.small}"
    rounded: "{rounded.tab-top}"
    padding: "8px 16px"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.card}"
    shadow: "{shadow.card}"
    padding: "{spacing.space-3}"
  card-gift-tile:
    backgroundColor: none
    rounded: "{rounded.card}"
  card-rewards-status:
    backgroundColor: "{colors.green-house}"
    textColor: "{colors.text-white}"
    typography: "{typography.h1}"
    rounded: "{rounded.card}"
  card-partnership:
    backgroundColor: "{colors.surface-gold-wash}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.card}"
    shadow: "{shadow.card}"
  dropdown-account:
    backgroundColor: "{colors.surface-cool}"
    textColor: "{colors.text}"
    typography: "{typography.h2}"
  modal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.card}"
    padding: "{spacing.modal-padding}"
  input-floating-label:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    borderColor: "{colors.border-input}"
    typography: "{typography.body}"
    rounded: "{rounded.input}"
    padding: "{spacing.field-padding}"
  select-addin:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    borderColor: "{colors.border-input}"
    typography: "{typography.body}"
    rounded: "{rounded.input}"
  stepper-numeric:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    borderColor: "{colors.border-input}"
    typography: "{typography.body}"
    rounded: "{rounded.circle}"
  nav-global:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.small}"
    shadow: "{shadow.nav}"
  cta-strip-join:
    backgroundColor: "{colors.black}"
    textColor: "{colors.text-white}"
    typography: "{typography.small}"
  feature-band:
    backgroundColor: "{colors.green-house}"
    textColor: "{colors.text-white}"
    typography: "{typography.h2}"
  feature-band-body:
    backgroundColor: "{colors.green-house}"
    textColor: "{colors.text-white-soft}"
    typography: "{typography.body-large}"
  size-option-selector:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.green-starbucks}"
    typography: "{typography.body}"
    rounded: "{rounded.card}"
    padding: "16px 24px"
  size-option-caption:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-dim}"
    typography: "{typography.micro}"
  customize-button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.accent}"
    borderColor: "{colors.accent}"
    typography: "{typography.button-label}"
    rounded: "{rounded.pill}"
    padding: "14px 40px"
  add-to-order-button:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-label}"
    rounded: "{rounded.pill}"
    padding: "14px 32px"
  rewards-cost-pill:
    backgroundColor: "{colors.green-house}"
    textColor: "{colors.gold}"
    borderColor: "{colors.gold}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: "4px 12px"
  product-description-band:
    backgroundColor: "{colors.green-house}"
    textColor: "{colors.text-white}"
    typography: "{typography.body}"
  store-availability-selector:
    backgroundColor: "{colors.green-house}"
    textColor: "{colors.text-white}"
    typography: "{typography.small}"
    rounded: "{rounded.input}"
  nutrition-table:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    borderColor: "{colors.border-hairline}"
    typography: "{typography.small}"
  nutrition-footnote:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-dim}"
    typography: "{typography.micro}"
  breadcrumb-pdp:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-dim}"
    typography: "{typography.small}"
  back-chevron-link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.accent}"
    typography: "{typography.small}"
  expander:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
  footer:
    backgroundColor: "{colors.green-house}"
    textColor: "{colors.text-white-soft}"
    typography: "{typography.body}"
---

# Design System Inspired by Starbucks

## Overview

Starbucks' design system is a **warm, confident retail flagship** wearing the green of their storefront apron across every surface. The canvas alternates between a neutral-warm cream (`#f2f0eb`) and a ceramic off-white (`#edebe9`) — colors that reference actual store materials: the paper napkins, the café walls, the wood finishes — while the signature **Starbucks Green** (`#006241`) anchors the brand moment on hero bands, CTAs, and the Rewards experience. The greens come in four calibrated shades (Starbucks, Accent, House, Uplift) each mapped to a specific surface role, and gold (`#cba258`) appears only around Rewards-status ceremony — not as a general accent.

Typography carries most of the brand voice. The proprietary **SoDoSans** typeface (custom to Starbucks) sits across nearly every surface with a tight `-0.16px` letter-spacing — it reads confident and friendly rather than fashion-magazine severe. What's unusual: the Rewards page switches to a warm serif (`"Lander Tall", "Iowan Old Style", Georgia`) for specific headline moments, subtly echoing the nostalgic feel of a coffeehouse chalkboard. And the Careers pages use a handwritten script (`"Kalam", "Comic Sans MS", cursive`) for personal cup-name touches. Three typefaces, three contexts — the system is disciplined about when each appears.

The surfaces breathe through rounded geometry. Every button is a 50px full-pill. Cards take a 12px rounded-rectangle. The "Frap" floating CTA — a 56px circular order button in Green Accent (`#00754A`) — is the product's signature depth move: it floats bottom-right with a layered shadow stack (`0 0 6px rgba(0,0,0,0.24)` base + `0 8px 12px rgba(0,0,0,0.14)` ambient) and compresses via `scale(0.95)` on press. Elevations are otherwise restrained — card shadows stay at a whispered `0.14/0.24` alpha, global nav gets a quiet three-layer shadow stack. The whole system feels like clean café signage: legible, warm, and never shouting.

**Key Characteristics:**
- Four-tier green brand system (Starbucks / Accent / House / Uplift) each mapped to a distinct surface role — not a single "brand green"
- Gold reserved for Rewards-status moments only; never a general-purpose accent
- Warm-neutral canvas (`#f2f0eb` / `#edebe9`) instead of cold white — references café materials
- Custom proprietary typeface (SoDoSans) with tight `-0.16px` letter-spacing as the universal voice
- Context-specific type switches: serif (Lander Tall) for Rewards, script (Kalam) for Careers cup-names
- Full-pill buttons (`50px` radius) universal, `scale(0.95)` active press the signature micro-interaction
- Floating "Frap" circular CTA (`56px`, Green Accent fill, layered shadow stack) — the product's signature elevation element
- Gift-card surfaces designed as **photographed physical product** — every card is a distinct illustrated photograph rather than a generated graphic
- 12px card radius + whisper-soft shadows keep content cards flat-plus-hint-of-lift
- Rem-based spacing scale anchored at 1.6rem (~16px) = `--space-3`, stepping to 6.4rem (~64px)

**Color-block page rhythm:** Cream hero → White content sections → Dark-green (`#1E3932`) feature band with white text → Cream utility zone → Dark-green (`#1E3932`) footer with gold / white text — an espresso-dark bookend around the bright body.

## Colors

**Source pages analyzed:** homepage, rewards, gift cards, product detail (Pink Energy Drink), product nutrition (Cold Brew).

### Primary

- **Starbucks Green** (`{colors.green-starbucks}` — `#006241`): The historic brand green. Used on h1 headings, primary section headers on the Rewards page, and as the main brand signal wherever a single dominant color is needed.
- **Green Accent** (`{colors.accent}` — `#00754A`): A slightly brighter, more luminous green. The primary filled-CTA color ("Explore our afternoon menu", "See the spring menu") and the fill of the floating Frap circular button.
- **House Green** (`{colors.green-house}` — `#1E3932`): The deep near-black brand green. Footer surface, feature-band backgrounds, reward-status dark surfaces, and the headline "Free coffee is just the beginning" hero band on Rewards.
- **Green Uplift** (`{colors.green-uplift}` — `#2b5148`): A secondary mid-dark green used sparingly on decorative accents and dark-gradient moments.
- **Green Light** (`{colors.green-light}` — `#d4e9e2`): A pale mint wash used for form-valid-state tints and light green utility surfaces.

### Secondary & Accent

- **Gold** (`{colors.gold}` — `#cba258`): Reserved almost exclusively for Rewards-status ceremony — Gold-tier callouts, partnership badges (SkyMiles, Bonvoy), and premium-feeling accents. Never a general-purpose brand color.
- **Gold Light** (`{colors.gold-light}` — `#dfc49d`): Softer gold for background washes on gold-tier sections.
- **Gold Lightest** (`{colors.surface-gold-wash}` — `#faf6ee`): Cream-gold page-surface wash used under partnership sections on the Rewards page — ties the gold accent back into the warm neutral system.
- **Consent Green** (`{colors.green-consent}` — `#008248`): Stated in the source only inside the cookie-consent component spec, as `rgb(0, 130, 72)`. Slightly brighter than Green Accent and reserved for the consent-banner Agree action; tokenised here because it is a second filled-CTA green and has to be measured as one.

### Surface & Background

- **White** (`{colors.surface}` — `#ffffff`): Primary card and modal surface. Also card fill on gift-card tiles.
- **Neutral Cool** (`{colors.surface-cool}` — `#f9f9f9`): Subtle cool-gray surface used on dropdown menus ("Account" dropdown), form-card wraps, and quiet utility containers.
- **Neutral Warm** (`{colors.canvas}` — `#f2f0eb`): The warm cream **primary page canvas** for Rewards utility zones and hero bands.
- **Ceramic** (`{colors.surface-ceramic}` — `#edebe9`): A slightly warmer/darker cream for zone separators, soft page-section washes, and Rewards partnership band.
- **Black** (`{colors.black}` — `#000000`): Deep ink reserved for the dark top-of-page CTA strip ("Join now") and high-contrast top-nav sign-in buttons.

### Neutrals & Text

- **Text Black** (`{colors.text}` — `rgba(0, 0, 0, 0.87)`): Primary heading and body text color on light surfaces. Not pure black — an 87%-opacity black that reads warmer.
- **Text Black Soft** (`{colors.text-dim}` — `rgba(0, 0, 0, 0.58)`): Secondary/metadata text on light surfaces.
- **Text White** (`{colors.text-white}` — `rgba(255, 255, 255, 1)`): Primary heading/body text on dark green surfaces.
- **Text White Soft** (`{colors.text-white-soft}` — `rgba(255, 255, 255, 0.70)`): Secondary text on dark-green surfaces — footer link descriptions, caption text.
- **Rewards Green** (`{colors.rewards-green}` — `#33433d`): A dedicated muted slate-green used only on Rewards-page text blocks — a slightly "dustier" reading color than Text Black that signals "reward surface" without using full Starbucks Green.

### Semantic & Accent

- **Red** (`{colors.error}` — `#c82014`): Error and destructive state (form invalid, destructive actions).
- **Yellow** (`{colors.warning}` — `#fbbc05`): Warning state, legacy brand touch.
- **Green Light tint** (`{colors.tint-valid}` — `#d4e9e2` at 33% opacity = `hsl(160 32% 87% / 33%)`): Form valid-field tint background.
- **Red Tint** (`{colors.tint-invalid}` — `hsl(4 82% 43% / 5%)`): Invalid-field tint on forms.

### Black / White Alpha Ladders

Two parallel translucent scales for overlay and secondary-text use:
- `rgba(0,0,0,0.06)` through `rgba(0,0,0,0.90)` in 10% steps — for dark overlays on light surfaces
- `rgba(255,255,255,0.10)` through `rgba(255,255,255,0.90)` in 10% steps — for light overlays on dark surfaces

### Gradient System

No structural gradient tokens observed. Surface hierarchy is solid-color-block throughout — the system relies on its five-tier cream/green surface palette rather than gradients.

### Borders

Two boundary tones appear in the component prose and are tokenised here; neither is named in the original colour list.

- **Input Border** (`{colors.border-input}` — `#d6dbde`): The 1px boundary of the Add-in / Milk select, the numeric stepper buttons and the floating-label field. At 1.40:1 on `{colors.surface}` and 1.23:1 on `{colors.canvas}` it is **below the 3:1 boundary threshold** — see Accessibility.
- **Table Hairline** (`{colors.border-hairline}` — `#e7e7e7`): The 1px rule below each nutrition label/value row. At 1.24:1 on `{colors.surface}` it is **decorative separation only**, not a perceivable boundary.

Both values are extracted and frozen. **No parallel accessible boundary token is added**, because the palette already owns tones that do the job: the system's own outlined controls are drawn in `{colors.accent}` (`1px solid #00754A` on the Primary Outlined and Customize buttons, 5.76:1 on white) and in `{colors.text}` (`1px solid rgba(0,0,0,0.87)` on the Sign-in button, 16.10:1 on white). Any boundary that must actually be perceived — the edge of a text input, the outline of a focusable card — is drawn in one of those two extracted tones. The two hairlines above stay scoped to decoration, and the components that bind them keep their extracted bindings. Re-pointing the form field to a perceivable boundary is a brand-owner decision, recorded under Needs approval in the audit report.

### Focus

- **Focus ring, light surfaces** (`{colors.focus}` — `#00754A`): **Prescribed, not extracted** — the source documents no focus treatment for any control except the Add-in / Milk select, whose border shifts to Green Accent. The ring reuses that same extracted tone rather than introducing a new colour, so nothing enters the palette that the brand does not already own. Drawn 2px wide with a 2px offset **outside** the control, so it is judged against the surface behind it.
- **Focus ring, dark surfaces** (`{colors.focus-on-dark}` — `#ffffff`): **Prescribed, not extracted.** The file documents two dark signature grounds — House Green feature bands, footers and Rewards panels, and the Black join strip — and one ring cannot serve both polarities: `{colors.focus}` reaches only 2.16:1 on `{colors.green-house}`. White is already the ink on every dark ground here, so the counterpart ring reuses it. Measured ratios for both rings, on every surface this file defines, are in Accessibility.

## Typography

### Font Family

- **Primary:** `SoDoSans, "Helvetica Neue", Helvetica, Arial, sans-serif` — Starbucks' proprietary corporate typeface, used across nearly every surface
- **Loading Fallback:** `"Helvetica Neue", Helvetica, Arial, sans-serif` — what users see before SoDoSans loads
- **Rewards Serif:** `"Lander Tall", "Iowan Old Style", Georgia, serif` — used on specific Rewards-page headline moments for a warm editorial feel
- **Careers Script:** `"Kalam", "Comic Sans MS", cursive` — used exclusively for Careers-page "cup name" decorative touches, referencing the hand-written names on Starbucks cups

No OpenType stylistic sets explicitly activated at `:root`.

### Hierarchy

| Role | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|--------|-------------|----------------|-------|
| Display (text-10) | 5.0rem / 80px | 400–600 | 1.2 | -0.16px | Largest Rewards/hero display |
| Jumbo (text-9) | 3.6rem / 58px | 400–600 | 1.2 | -0.16px | Secondary hero headings |
| Hero Large (text-8) | 2.8rem / 45px | 400–600 | 1.2–1.5 | -0.16px | Landing section headlines |
| H1 | 24px | 600 | 36px | -0.16px | Starbucks-Green primary heading |
| H2 | 24px | 400 | 36px | -0.16px | Regular-weight section title in Text Black |
| Body Large | 19px | 400–600 | 33.25px (~1.75) | -0.16px | Hero intro copy, feature-band body |
| Body (text-3) | 1.6rem / 16px | 400 | 1.5 (24px) | -0.01em | Default body copy |
| Small (text-2) | 1.4rem / ~14px | 400–600 | 1.5 | -0.01em | Button label, metadata, form labels |
| Micro (text-1) | 1.3rem / ~13px | 400 | 1.5 | -0.01em | Active float-label state, caption micro-copy |
| Button Label | 14–16px | 400–600 | 1.2 | -0.01em | All pill-button labels |

**Letter-spacing tokens:**
- `letterSpacingNormal`: `-0.01em` (default — tight, characteristic)
- `letterSpacingLoose`: `0.1em` (emphasized caps)
- `letterSpacingLooser`: `0.15em` (uppercase-style labels, extreme emphasis)

**Line-height tokens:**
- `lineHeightNormal`: `1.5` (body)
- `lineHeightCompact`: `1.2` (display/buttons)

### Principles

- **Tight negative tracking (`-0.01em`)** is applied almost universally — the entire product reads slightly compressed, which gives SoDoSans its confident presence without feeling squeezed.
- **Weight shifts carry hierarchy, not size shifts.** H1 and H2 share the same 24px/36px size; only weight (600 vs 400) and color (Starbucks-Green vs Text Black) separate them.
- **Size tokens use rem, anchored to `1rem = 10px`** on this site (via a `font-size: 62.5%` root trick). So `1.6rem` = 16px, `2.4rem` = 24px, etc. The scale is semantic (textSize-1 through textSize-10), not arbitrary pixel values.
- **Context-specific typeface swaps** — serif on Rewards, script on Careers — are deliberate and localized. Never mix them with the primary sans within the same surface.
- **Body text never goes pure black** — it sits at `rgba(0,0,0,0.87)` to match the warm-neutral canvas temperature.

### Note on Font Substitutes

SoDoSans is proprietary to Starbucks (licensed from House Industries, not publicly available). Reasonable open-source substitutes:
- **Inter** (Google Fonts) — similar humanist geometric proportions, wide weight range
- **Manrope** — slightly rounder, similar confident feel
- **Nunito Sans** — warmer, good for a "café" brand substitute

If substituting, verify the tight `-0.01em` / `-0.16px` tracking still reads well; some open-source fonts need `-0.005em` instead.

Lander Tall (the Rewards serif) is custom — open-source substitutes: **Iowan Old Style** (already in fallback), **Lora**, or **Source Serif Pro**. Kalam (Careers script) is available on Google Fonts directly.

## Layout

### Spacing System

Rem-based semantic scale (anchored `1rem = 10px`):

| Token | Rem | Pixels | Typical Use |
|-------|-----|--------|-------------|
| `--space-1` | `0.4rem` | 4px | Tightest inline padding |
| `--space-2` | `0.8rem` | 8px | Small gap, button vertical padding |
| `--space-3` | `1.6rem` | 16px | Default — card padding, outer gutter xs |
| `--space-4` | `2.4rem` | 24px | Section inner spacing, outer gutter md |
| `--space-5` | `3.2rem` | 32px | Major between-section spacing |
| `--space-6` | `4rem` | 40px | Large gaps, outer gutter lg, header crate |
| `--space-7` | `4.8rem` | 48px | Section-to-section spacing |
| `--space-8` | `5.6rem` | 56px | Very large breathing — Frap height |
| `--space-9` | `6.4rem` | 64px | Widest section padding |

**Gutter tokens:**
- `--outerGutter: 1.6rem` (16px, default / mobile)
- `--outerGutterMedium: 2.4rem` (24px, tablet)
- `--outerGutterLarge: 4.0rem` (40px, desktop)

**Universal rhythm constant:** `1.6rem` (16px) appears across every page as the default outer gutter, card padding baseline, and text size 3 body — the system's most frequent spacing unit.

### Grid & Container

- Column width scale: `--columnWidthSmall: 343px` / `Medium: 500px` / `Large: 720px` / `XLarge: 1440px`
- Gift-card grid uses a 3-5-up responsive grid of `~343px` tiles
- Rewards status section: 3-up dark-green panels at `lg+` breakpoints
- Hero: asymmetric split 40% (image) / 60% (content) via `--headerCrateProportion` / `--contentCrateProportion`

### Whitespace Philosophy

Whitespace carries the feeling of "plenty of space in the café." Section padding leans generous (40–64px). Content blocks are separated by whitespace rather than dividers. The cream canvas (`#f2f0eb`) is itself a visual breath between white cards and green feature bands.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Card | `0 0 0.5px rgba(0,0,0,0.14), 0 1px 1px rgba(0,0,0,0.24)` | Default content cards — a whisper-soft dual-shadow |
| Global Nav | `0 1px 3px rgba(0,0,0,0.1), 0 2px 2px rgba(0,0,0,0.06), 0 0 2px rgba(0,0,0,0.07)` | Triple-layer soft lift on the fixed top bar |
| Frap Base | `0 0 6px rgba(0,0,0,0.24)` | Base halo around the floating circular CTA |
| Frap Ambient | `0 8px 12px rgba(0,0,0,0.14)` | Stacked directional ambient — floats the Frap forward |
| Gift Card | Light drop shadow around illustrated photograph | Physical-card feel for gift tiles |
| Starbucks Card (SVC) | `drop-shadow(0 4px 1px rgba(0,0,0,0.11)) drop-shadow(0 0 2px rgba(0,0,0,0.24))` | Stacked SVG drop shadows for Starbucks Card visuals |

**Shadow philosophy:** Whisper-soft, layered over solid — the system never reaches for a single heavy drop shadow. Instead, it stacks 2–3 low-alpha shadows with different offsets to simulate real-world ambient + direct lighting. The Frap button is the most elevated element on any page.

### Decorative Depth

- **No gradient system** — surfaces are solid color-block
- **Color-block banding** carries perceived depth (dark-green bands read as "recessed feature zones" between cream/white body sections)
- **SVG filter shadows** on Starbucks-Card visuals add a slight 3D physicality without a box-shadow

## Shapes

### Border Radius Scale

| Value | Use |
|-------|-----|
| `12px` | Cards, modals, menu-item tiles (`--cardBorderRadius`) |
| `12px 12px 0 0` | Full-width feedback tab (top-rounded only) |
| `50px` | All buttons — full-pill radius (`--buttonBorderRadius`) |
| `50%` | Circular icons, Frap floating button, avatar thumbnails |
| Specialty | `3.3333%/5.298%` elliptical for Starbucks-Visa-Card mockups (`{rounded.svc}`, `--svcRoundedCorners`) |

**Ladder consistency.** Four steps, each with one job and no value sitting between them: `{rounded.input}` (4px) for rectangular form controls, `{rounded.card}` (12px) for every container, `{rounded.pill}` (50px) for every button without exception, and `{rounded.circle}` (50%) for the Frap and icon buttons. `{rounded.tab-top}` is the card radius applied to two corners, not a fifth value. The elliptical `{rounded.svc}` is labelled Specialty in the source for a reason: it describes an illustrated card mockup, not a UI container, and it is the one value outside the ladder.

**Border widths** form their own three-step ladder, all extracted: `1px` for every default boundary and outlined pill, `1.5px` for the Customize button (a secondary-primary action that needs slightly more weight), and `2px` for the selected size-option ring. Nothing in the file uses a 3px or heavier stroke.

## Components

### Buttons

**1. Primary Filled — "Explore our afternoon menu / Sign up for free"**
- Background: `#00754A` (Green Accent)
- Text: `#ffffff`
- Border: `1px solid #00754A`
- Radius: `50px` (full pill)
- Padding: `7px 16px`
- Font: SoDoSans, 16px, weight 600, letter-spacing `-0.01em`
- Active state: `transform: scale(0.95)` via `--buttonActiveScale`
- Transition: `all 0.2s ease`

**2. Primary Outlined — "Give them a try / Start an order"**
- Background: transparent
- Text: `#00754A` (Green Accent)
- Border: `1px solid #00754A`
- Same radius/padding/active/transition as Primary Filled

**3. Black Filled — "Join now"**
- Background: `#000000`
- Text: `#ffffff`
- Border: `1px solid #000000`
- Radius: `50px`, Padding: `7px 16px`
- Font: 14px, weight 600
- Used on the top-of-page join strip and similar conversion moments

**4. Dark Outlined — "Sign in"**
- Background: transparent
- Text: `rgba(0, 0, 0, 0.87)` (Text Black)
- Border: `1px solid rgba(0, 0, 0, 0.87)`
- Radius: `50px`, Padding: `7px 16px`
- Font: 14px, weight 600

**5. Green-on-Green Inverted — "See the spring menu"**
- Background: `#ffffff`
- Text: `#00754A`
- Border: `1px solid #ffffff`
- Used when the surface behind the button is the dark green House Green band — white button with green text instead of a filled green pill on green bg

**6. Outlined on Dark — "Learn more / Order now"**
- Background: transparent
- Text: `#ffffff`
- Border: `1px solid #ffffff`
- Used on dark-green feature bands for secondary action paired with a white filled CTA

**7. Consent Agree (dark-green variant)**
- Background: `rgb(0, 130, 72)` (a specific variant green used in the cookie-consent module)
- Text: `#ffffff`
- No border, `50px` radius, `7px 16px` padding, 14px / weight 400
- Slightly brighter than Green Accent — reserved for the consent-banner Agree action

**8. Frap — Floating Circular Order Button**
- Background: `#00754A` (Green Accent)
- Icon: `#ffffff`
- Size: `5.6rem / 56px` (standard), `4rem / 40px` (mini variant)
- Radius: `50%` (full circle)
- Fixed bottom-right, `-0.8rem` touch offset for extra tap comfort
- Shadow stack: base `0 0 6px rgba(0,0,0,0.24)` + ambient `0 8px 12px rgba(0,0,0,0.14)`
- Active state: ambient shadow fades to `0 8px 12px rgba(0,0,0,0)`
- This is the product's signature elevation element — it floats over every scrolled surface

**9. Full-width Feedback Tab — "Provide feedback"**
- Background: `#00754A`
- Text: `#ffffff`
- Radius: `12px 12px 0px 0px` (top-rounded only)
- Padding: `8px 16px`
- Font: 14px, weight 400
- Positioned fixed bottom-right-inside, attached to the viewport edge

### Cards & Containers

**Content Card (default)**
- Background: `#ffffff` (`--cardBackgroundColor`)
- Radius: `12px` (`--cardBorderRadius`)
- Shadow: `0px 0px .5px 0px rgba(0,0,0,0.14), 0px 1px 1px 0px rgba(0,0,0,0.24)` (`--cardBoxShadow`)
- Used for: feature cards, menu-item tiles, reward-status panels

**Gift Card Tile**
- Background: illustrated photography fills the card (no solid bg)
- Radius: similar to cards (`~12px`, slightly tighter on corners)
- Shadow: lighter than default card — these are treated like physical cards laid on the canvas
- Labeled by category above the card grid (Spring, Thank You, Birthday, Celebration, Mother's Day, Appreciation, Encouragement, Milestones, Anytime)

**Rewards Status Cards (Rewards page signature)**
- Three-column grid: Bronze / Gold / Silver-ish — each a dark-green (`#1E3932`) panel with:
  - Colored gradient/color header ring
  - Numbered "Level" badge
  - Status title in large SoDoSans weight 600
  - Stars / benefits list in white/translucent-white text
  - Bottom "As you earn more stars…" progression caption

**Partnership Card (Rewards)**
- Background: `#faf6ee` (Gold Lightest) warm-cream surface
- Content: partner logos ("SkyMiles", "Bonvoy") centered, with descriptive text below
- Radius and shadow follow default card spec

**Dropdown Menu (Account dropdown, top-nav)**
- Background: `#f9f9f9` (Neutral Cool)
- Menu items at `24px / weight 400` in Text Black
- No border — just background surface shift against white nav

**Modal**
- Padding: `2.4rem` (`--modalPadding`)
- Top padding: `8.8rem` (`--modalTopPadding`) — leaves room for close button / header
- Combined vertical padding: `11.2rem`
- Radius inherits from card spec (`12px`)

### Inputs & Forms

**Floating Label Input**
- Label floats above the input border when focused/filled
- Desktop label font size: `1.9rem` default, animates to `1.4rem` when active
- Mobile label font size: `1.6rem` default, animates to `1.3rem` active
- Label horizontal offset: `12px` from left
- Active label translate: up to `-12px` with `-50%` Y translation
- Field padding: `12px`
- Form horizontal padding: `1.6rem`
- Validation: valid-field gets `rgba(green-light, 0.33)` tint; invalid-field gets `rgba(red, 0.05)` tint
- Transition: `0.3s option-label-marker-expansion cubic-bezier(0.32, 2.32, 0.61, 0.27)` on checked-input

**Option Icon (checkbox/radio)**
- Padding: `3px` inner
- Uses the checked-input cubic-bezier animation above (a slightly "springy" 2.32 overshoot curve)

### Navigation

**Global Nav (top bar)**
- Fixed position with progressive heights: `64px` xs → `72px` mobile → `83px` tablet → `99px` desktop
- Shadow stack: `0 1px 3px rgba(0,0,0,0.1), 0 2px 2px rgba(0,0,0,0.06), 0 0 2px rgba(0,0,0,0.07)` — three-layer soft lift
- Left: Starbucks wordmark logo, offsetting by `99px` (md) / `131px` (lg) from left edge
- Primary links inline in SoDoSans weight 400–600: Menu · Rewards · Gift Cards
- Right: Find a store link + Sign in (outlined) + Join now (black filled)

**Sub-nav (second bar, e.g., Rewards internal)**
- Height: `53px` (global subnav) / `48px` (internal subnav)
- Typically horizontal tab group beneath the global nav

**Mobile Nav**
- Collapses to a hamburger drawer below tablet breakpoint
- Frap floating button persists at bottom-right regardless of nav state

### Image Treatment

- **Hero photography**: Product photos (beverages in clear glass with colored backgrounds — coral, sage, warm amber) occupy ~40vw of a split-hero layout; text occupies the other 60vw (`--headerCrateProportion: 40vw` / `--contentCrateProportion: 60vw`)
- **Gift card illustrations**: Each card is a distinct illustrated photograph (painted-feel, hand-drawn-looking, warm color palette). Never generic generated graphics.
- **Rewards ceremony imagery**: Photographs of Starbucks Rewards App screens held in-hand, angled compositions — product-in-context photography.
- **Menu thumbnails**: Square or 4:3 product photography with clean white/cream backdrops, slight soft drop-shadow around the glass.
- **Image fade-in**: `opacity 0.3s ease-in` transition on image load (`--imageFadeTransition`).

### Feature Band (dark-green hero strip)

Full-width `#1E3932` (House Green) band with:
- Left: white headline + subhead + CTA row
- Right: product photography or illustration
- Split ratio ~40/60 or 50/50 depending on section
- White text throughout with `rgba(255,255,255,0.70)` for secondary copy
- CTAs follow Green-on-Green Inverted (white filled) + Outlined on Dark (white outline) pairing

### Expander / Accordion

- Duration: `300ms` (`--expanderDuration`)
- Timing curve: `cubic-bezier(0.25, 0.46, 0.45, 0.94)` — a measured ease-out
- Used for FAQ sections on Rewards and gift page

### Cookie Consent Module

Dark-green modal card at top of page with "Agree" (green-filled) and "Manage preferences" (outlined) buttons. Appears on first visit; dismissible.

### Product Detail Components (PDP signature cluster)

A repeating component cluster used on menu product pages (e.g., `/menu/product/40498/iced` for a drink detail, `/menu/product/.../nutrition` for nutrition facts). These extend the component inventory without changing tokens.

**Size Options Selector**
- Horizontal row of 4 cup-icon buttons (Tall / Grande / Venti / Trenta)
- Each item: cup silhouette icon on top, size name below (16/700 in Starbucks-Green), fluid-ounce caption (13/400 in Text Black Soft)
- Active state: a green circular ring outline (`2px solid #00754A`) around the selected cup icon
- Inactive: no ring, same typography
- Full-width row, equal spacing
- Radius of container: `12px` or flat; individual icons are `50%` circular
- Padding: `16px 24px` internal

**Add-in / Milk Select (outlined rectangle)**
- Background: `#ffffff`
- Border: `1px solid #d6dbde` (Input Border)
- Radius: `4px`
- Full-width in its column
- Floating label above top border: "Add-ins" / "Milk" / "Add-ins" — 13/700 in Text Black, uppercase, `0.325px` letter-spacing
- Value displayed centered (e.g., "Ice", "Coconut", "Strawberry Fruit Inclusions scoop"): 16/400 Text Black
- Chevron-down icon right side in Text Black Soft
- Focus: border shifts to Green Accent (`#00754A`)

**Numeric Stepper**
- Embedded inside an Add-in row when a quantity is required (e.g., Strawberry Fruit Inclusions scoop)
- `−` minus button + count number + `+` plus button, all inline right of the label
- Buttons: circular `32×32px` with `1px solid #d6dbde` border, neutral gray icon
- Count number: 16/700 Text Black centered

**Customize Button**
- Background: `#ffffff`
- Text: `#00754A` (Green Accent)
- Border: `1.5px solid #00754A`
- Radius: `50px` (full pill)
- Padding: `14px 40px` (generously larger than default pills — this is a secondary primary action)
- Label: "Customize" with a gold sparkle ✨ icon inset left
- Used for: entering the drink-customization flow after size/milk selection

**Add to Order Button (PDP)**
- Background: `#00754A` (Green Accent)
- Text: `#ffffff`
- Radius: `50px`
- Padding: `14px 32px`
- Pinned top-right of product card and/or aligned right within the store-availability band
- Same scale(0.95) active behavior as other primary CTAs

**Rewards Cost Pill — "200★ item"**
- Background: transparent
- Border: `1px solid #cba258` (Gold)
- Text: `#cba258` (Gold)
- Radius: `50px` (full pill)
- Padding: `4px 12px`
- Content: "200★ item" where `★` is a small filled star glyph — indicates the Rewards Stars required to redeem this item
- Font: Proxima Nova 13/700 with `0.5px` letter-spacing
- Used only on products that are Rewards-redeemable

**Product Description Band**
- Full-width dark-green band (`#1E3932` House Green)
- Contains top-to-bottom:
  1. Rewards Cost Pill (gold) if applicable
  2. Product description body copy in white (16/400/1.5)
  3. Nutritional summary inline ("140 calories, 25g sugar, 2.5g fat") with info-icon tooltip — 14/700 white
  4. "Full nutrition & ingredients list" outlined-white-on-green pill button
- Padding: `32px` vertical
- Appears beneath the primary product header band

**Ingredients / Nutrition Table**
- Two-column layout on the Nutrition page
- Left column: "Ingredients" header + list or "Not available for this item" placeholder text block with an explanatory paragraph in Text Black Soft 14/400
- Right column: "Nutrition" header + label/value rows
- Each row: nutrient label (Proxima Nova 14/400) on the left, value (e.g., "140 calories", "25g", "205 mg**") on the right, separated by a `1px solid #e7e7e7` hairline below
- Footnote for caffeine/asterisk markers in 13/400 Text Black Soft at the bottom
- Reusable pattern for nutrition facts regulation-compliant tables

**Store Availability Selector**
- Appears on dark-green feature band above the size-options row
- Full-width rounded rectangle with transparent-white interior
- Text: "For item availability, choose a store" in white, 14/400
- Right side: chevron-down affordance + shopping-bag SVG icon in white outline
- Radius: `4px`
- Height: ~48px

**PDP Breadcrumb**
- "Menu / Refreshers / Pink Energy Drink" trail above the product title
- Separator: `/` slash character in Text Black Soft
- Current page is unlinked, prior pages are underlined green-accent links
- Font: 14/400 Proxima Nova
- Appears on all PDP pages

**Back Chevron Link (PDP nutrition / detail sub-pages)**
- "← Back" text link above section headings on the nutrition page
- Text in Green Accent (`#00754A`) 14/700 Proxima Nova
- Left chevron `<` in the same green
- Alternative to full breadcrumb on deep sub-pages

### Interaction States

State coverage is documented at the system level because the source documents it that way: the press behaviour is declared once, as universal, and then referenced per component. Where a state is absent from the source it is marked as absent rather than invented: this file documents a real brand, and a fabricated rollover tint would be a worse outcome than a gap.

- **default** — fully specified for every entry above: fill, text colour, border, radius, padding and type.
- **focus-visible** — one extracted behaviour: the Add-in / Milk select's `1px solid #d6dbde` border shifts to Green Accent (`#00754A`) on focus, and the floating label rises when a field is focused or filled. Everything else is **prescribed by this audit**: a 2px `{colors.focus}` ring at 2px offset outside the control on light surfaces, `{colors.focus-on-dark}` on House Green and Black grounds.
- **active / pressed** — extracted and universal: `transform: scale(0.95)` via `--buttonActiveScale` on every pill button, with a `200ms` transition. The Frap floating button additionally collapses its ambient shadow from `{shadow.frap-ambient}` to `{shadow.frap-ambient-pressed}` while held.
- **selected** — extracted on exactly one component: the Size Options Selector wraps the chosen cup icon in a `2px solid #00754A` circular ring; unselected items carry no ring and identical typography.
- **error** — extracted at the token level: an invalid form field takes a `{colors.tint-invalid}` wash, and `{colors.error}` (`#c82014`) is the documented error and destructive tone. Border weight, icon placement and message styling are absent from the source — see Known Gaps.
- **hover** — not documented anywhere in the source, for any component. See Known Gaps.
- **disabled** — not documented, and no disabled tone exists in the palette. See Known Gaps.
- **loading** — not documented for any control. The only load-time behaviour in the source is the `opacity 0.3s ease-in` image fade-in. See Known Gaps.

The Cookie Consent module and the Feedback Tab are genuinely two-state components: present or dismissed, with the Agree and Manage-preferences pills inheriting the universal press behaviour and nothing else.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** Nothing in the choreography below was timed against starbucks.com. The token values are the shared **Playful** profile from `theme-audit/SPEC.md` section 5, carried verbatim in the `motion:` frontmatter group so that every Playful file in this collection behaves as a sibling.

Playful is the right profile here, and unusually for this audit the file's own extracted values corroborate it rather than merely permitting it. Three signals, all already in the source: every pill button presses with `transform: scale(0.95)` — the profile's "small scale pops on press" signature, named by the document itself as "the signature micro-interaction"; the checked-input animation is `cubic-bezier(0.32, 2.32, 0.61, 0.27)`, an overshoot curve with a control point well past 1, which is the profile's "overshoot on enter" bias in literal extracted form; and the universal button transition is `all 0.2s ease`, which is already `{motion.duration-base}` to the millisecond. The saturated green sits on the interactive elements rather than behind them — CTAs, the Frap, the selected-size ring — and the type voice runs to a handwritten Kalam script for cup names. Only `transform` and `opacity` are animated: never `width`, `height`, `top`, `left` or `margin`.

Two extracted timings are kept in preference to the profile value, with the reason stated: the expander/accordion stays at its measured `300ms` with `cubic-bezier(0.25, 0.46, 0.45, 0.94)`, and image load keeps its measured `opacity 0.3s ease-in`. Both are facts about the real site and sit within a step of the profile's own ladder.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (prescribed — no hover is documented in the source) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` of the pill fill, `transform: scale(1.02)` on cards | Travel and scale removed; opacity only, at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-base}` | `{motion.ease-standard}` | `transform: scale(0.95)` — the extracted signature; the Frap also fades its ambient shadow | Scale removed; the shadow fade remains at `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` / `{colors.focus-on-dark}` ring | Ring appears instantly and is never suppressed |
| Page / route transition | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity` 0→1, `transform: translateY(16px)`→0 on the content crate | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Modal / drawer enter (incl. the mobile nav drawer) | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateX(-100%)`→0 for the drawer, `scale(0.97)`→1 for the modal | Travel and scale removed; scrim fades at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown enter / exit (Account menu) | `{motion.duration-fast}` / `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(12px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| List enter (gift-card grid, menu tiles, Rewards panels) | `{motion.duration-base}`, staggered by `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px)`→0 | Stagger and travel removed; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Expander / accordion (FAQ) — extracted `300ms` kept | 300ms | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | `opacity` plus `transform: scaleY()` on the panel; it must not animate `height` | Travel removed; the panel opens with no transition and its content fades at `{motion.duration-reduced}` |
| Floating-label rise | `{motion.duration-fast}` | `cubic-bezier(0.32, 2.32, 0.61, 0.27)` — extracted overshoot | `transform: translateY(-12px) translateY(-50%)`, `opacity`; the label's extracted font-size change from `1.9rem` to `1.4rem` is a paint change applied without transition | Travel removed; the label snaps to its small position, which is never animated |
| Image load | 300ms | `ease-in` | `opacity` 0→1 — extracted (`--imageFadeTransition`) | Fade kept, capped at `{motion.duration-reduced}` |
| Loading | 1200ms, infinite | linear | `opacity` pulse on a card-shaped placeholder at `{colors.surface-ceramic}` | Loader frozen; a static placeholder remains |

Exit is always shorter than its matching entrance. Nothing animates on first paint in a way that delays content: the hero image fade is an `opacity` transition on an already-laid-out element, and the Frap is present on first paint rather than flying in. There is no infinite animation anywhere except the loading placeholder; this brand carries no ambient motion, and none is prescribed.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: the scale(0.95) press pop, every translate, the floating-label
     overshoot, the gift-card grid stagger, the hover card lift, and the
     loading placeholder pulse. */
  /* Kept: opacity fades only, capped at {motion.duration-reduced} (130ms),
     plus the focus ring, which appears instantly and is never animated away. */
  *, *::before, *::after {
    transition-property: opacity;
    transition-duration: 130ms; /* {motion.duration-reduced} */
    animation: none;
  }
}
```

## Accessibility

Every ratio below is computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. Translucent inks are composited over the ground they are actually drawn on before measurement, so `{colors.text}` is measured as the `#1f1f1f` it renders as on the cream canvas rather than as pure black. **The extracted brand values are frozen: the failures listed here are real failures of the live Starbucks interface, disclosed rather than corrected.** The headline finding is that the text system is healthy on every surface the brand defines, and that the weakness sits entirely in the boundary tones — both documented hairlines are invisible at the 3:1 threshold — plus two signal colours, Gold and Yellow, that cannot be read as text on a light ground.

### Measured contrast — key pairs

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `text` rgba(0,0,0,0.87) → #1f1f1f on `canvas` #f2f0eb | 14.47:1 | 4.5:1 | Pass |
| `text` → #212121 on `surface` #ffffff | 16.10:1 | 4.5:1 | Pass |
| `text` → #202020 on `surface-cool` #f9f9f9 | 15.48:1 | 4.5:1 | Pass |
| `text` → #1f1f1e on `surface-ceramic` #edebe9 | 13.87:1 | 4.5:1 | Pass |
| `text` → #20201f on `surface-gold-wash` #faf6ee | 15.13:1 | 4.5:1 | Pass |
| `text-dim` rgba(0,0,0,0.58) → #666563 on `canvas` | 5.11:1 | 4.5:1 | Pass |
| `text-dim` → #6b6b6b on `surface` | 5.33:1 | 4.5:1 | Pass |
| `text-dim` → #646362 on `surface-ceramic` | 5.04:1 | 4.5:1 | Pass — the narrowest margin in the text system |
| `text-white` #ffffff on `green-house` #1E3932 | 12.45:1 | 4.5:1 | Pass |
| `text-white-soft` rgba(255,255,255,0.70) → #bcc4c2 on `green-house` | 7.00:1 | 4.5:1 | Pass |
| `text-white` on `black` #000000 | 21.00:1 | 4.5:1 | Pass |
| `on-accent` #ffffff on `accent` #00754A | 5.76:1 | 4.5:1 | Pass — the primary CTA pair |
| `green-starbucks` #006241 as heading ink on `canvas` | 6.53:1 | 4.5:1 | Pass |
| `green-starbucks` on `surface` | 7.44:1 | 4.5:1 | Pass |
| `accent` #00754A as link/label ink on `canvas` | 5.06:1 | 4.5:1 | Pass |
| `accent` as link/label ink on `surface` | 5.76:1 | 4.5:1 | Pass |
| `accent` as ink on `surface-ceramic` | 4.85:1 | 4.5:1 | Pass |
| `text-white` on `green-consent` #008248 (consent-banner Agree pill) | 4.90:1 | 4.5:1 | Pass — the tightest filled-button pair in the system |
| `rewards-green` #33433d on `canvas` | 9.17:1 | 4.5:1 | Pass |
| `rewards-green` on `surface-gold-wash` | 9.69:1 | 4.5:1 | Pass |
| `error` #c82014 on `canvas` | 5.02:1 | 4.5:1 | Pass |
| `error` on `surface` | 5.72:1 | 4.5:1 | Pass |
| `warning` #fbbc05 on `canvas` | 1.50:1 | 4.5:1 | **Fail — real brand failure.** Yellow is a fill tone and a "legacy brand touch"; it is not readable as text on any surface this file defines (1.71:1 on white). Defensible only as a chip or icon fill with `{colors.text}` drawn on it; a yellow warning *label* must be re-drawn in `{colors.text}` |
| `gold` #cba258 on `green-house` | 5.25:1 | 4.5:1 | Pass — the ground the Rewards Cost Pill is actually drawn on |
| `gold` #cba258 as ink on `canvas` | 2.08:1 | 4.5:1 | **Fail — real brand failure.** Gold is legible only on the two dark grounds. On the cream canvas and on its own `surface-gold-wash` band (2.20:1) it is a decorative tone, never text |
| `gold-light` #dfc49d on `canvas` | 1.47:1 | 4.5:1 | **Fail by name only** — Gold Light is documented as a background wash, never as an ink, so 1.4.3 does not apply to it. Text drawn on it must be `{colors.text}` |
| `border-input` #d6dbde on `surface` #ffffff | 1.40:1 | 3:1 | **Fail — frozen extracted boundary.** This is the pair `{components.input-floating-label}`, `{components.select-addin}` and `{components.stepper-numeric}` actually bind: the sole visible edge of a text input, at well under half the required ratio |
| `border-input` #d6dbde on `canvas` #f2f0eb | 1.23:1 | 3:1 | **Fail — frozen extracted boundary**, worse on the cream page floor than on a white card |
| `border-hairline` #e7e7e7 on `surface` #ffffff | 1.24:1 | 3:1 | **Fail — frozen extracted boundary.** The nutrition-table row rule; acceptable as decorative separation in a table that also separates by position, not acceptable as a control boundary |
| `border-hairline` #e7e7e7 on `canvas` #f2f0eb | 1.09:1 | 3:1 | **Fail — frozen extracted boundary**, effectively invisible on cream |
| `accent` #00754A as a boundary on `surface` | 5.76:1 | 3:1 | Pass — the perceivable boundary the palette already owns, extracted from the Primary Outlined and Customize buttons |
| `text` → #212121 as a boundary on `surface` | 16.10:1 | 3:1 | Pass — the Sign-in button's extracted `1px solid rgba(0,0,0,0.87)` |

### Manufactured pairs, disclosed as manufactured

Three pairs below are artefacts of how the harness reads a `components:` entry, not findings about the brand. They are recorded here so that nobody reading the machine output mistakes them for defects, and the harness defect is filed in the audit report under Shared issues.

| Pair | Measured | Required | Why it is not a finding |
|---|---|---|---|
| `accent` border on `accent` fill — `{components.button-primary-filled}`, 1.00:1 | 1.00:1 | 3:1 | The source states `Border: 1px solid #00754A` on a `#00754A` fill: the border exists to equalise the outlined and filled pills' box dimensions, and is deliberately invisible. A border equal to its own fill is a self-pair, not a boundary |
| `black` border on `black` fill — `{components.button-black-filled}`, 1.00:1 | 1.00:1 | 3:1 | Same extracted pattern: `1px solid #000000` on `#000000` |
| `surface` border on `surface` fill — `{components.button-inverted-on-green}`, 1.00:1 | 1.00:1 | 3:1 | Same again: `1px solid #ffffff` on `#ffffff`. This pill's real boundary is the House Green band behind it, at 12.45:1 |

A second artefact concerns the surface role itself: the harness resolves `surface` to `{colors.surface-ceramic}` (#edebe9), the surface-pattern tone nearest the canvas. Ceramic is a page-section wash, not a raised surface; the brand's card tone is `{colors.surface}` (#ffffff), which `{components.card}`, `{components.modal}` and every input bind. The hairline ratios against ceramic above (1.17:1, 1.04:1) are therefore measured against a ground those components never render on, and the white-card figures are the ones to build against.

### Layer separation

Contrast is not a WCAG requirement between two backgrounds, but it is what decides whether the elevation ladder is visible at all. Starbucks' warm-neutral family is deliberately tight: the cream canvas, the ceramic wash and the white card are three steps on one ramp, and the shadows — not the fills — are what separate them.

| Layers | Measured | Note |
|---|---|---|
| `surface` #ffffff against `canvas` #f2f0eb | 1.14:1 | A white card on cream is distinguishable only with `{shadow.card}` present. Remove the shadow and the card disappears |
| `surface-ceramic` #edebe9 against `canvas` | 1.04:1 | Zone separators are near-imperceptible by design; they are read as a temperature shift, not an edge |
| `surface-cool` #f9f9f9 against `surface` | 1.05:1 | The Account dropdown against the white nav — the source's own words are "no border — just background surface shift", which at 1.05:1 is not a reliable boundary on its own |
| `surface-gold-wash` #faf6ee against `canvas` | 1.06:1 | The partnership band |
| `green-house` #1E3932 against `canvas` | 10.93:1 | The deliberate espresso-dark bookend — the one strong layer step in the system |
| `black` #000000 against `canvas` | 18.44:1 | The join strip |

### Focus ring visibility on every surface this file defines

**Prescribed, not extracted.** Both rings are drawn 2px wide with a 2px offset **outside** the control, so each is judged against the surface behind it rather than against the fill it surrounds. `{colors.focus}` reuses Green Accent, the one tone the source does document as a focus response (the Add-in select's border shift); `{colors.focus-on-dark}` reuses the white that is already the ink on every dark ground. Gold was rejected as a ring: the brand's own Don'ts forbid Gold as a general-purpose accent.

| Surface it is drawn on | Ring | Measured | Required | Verdict |
|---|---|---|---|---|
| `canvas` #f2f0eb | `{colors.focus}` | 5.06:1 | 3:1 | Pass |
| `surface` #ffffff | `{colors.focus}` | 5.76:1 | 3:1 | Pass |
| `surface-cool` #f9f9f9 | `{colors.focus}` | 5.47:1 | 3:1 | Pass |
| `surface-ceramic` #edebe9 | `{colors.focus}` | 4.85:1 | 3:1 | Pass |
| `surface-gold-wash` #faf6ee | `{colors.focus}` | 5.35:1 | 3:1 | Pass |
| `green-light` #d4e9e2 (valid-field tint) | `{colors.focus}` | 4.54:1 | 3:1 | Pass |
| `green-house` #1E3932 | `{colors.focus}` | 2.16:1 | 3:1 | **Fail — this is why a second ring exists** |
| `green-house` #1E3932 | `{colors.focus-on-dark}` | 12.45:1 | 3:1 | Pass |
| `black` #000000 | `{colors.focus-on-dark}` | 21.00:1 | 3:1 | Pass |
| `green-uplift` #2b5148 | `{colors.focus-on-dark}` | 8.85:1 | 3:1 | Pass |

The Frap floating button is the one control that can come to rest over anything, since it floats above whatever is scrolled beneath it — including gift-card photography and hero product shots, which have no measurable colour. Over imagery the ring is two-tone: 2px `{colors.focus-on-dark}` with a 1px outer edge in `{colors.green-house}`, so one band or the other always separates from the frame behind it.

### Minimum tap target

The source states that pill buttons at `7px 16px` padding "measure ~32px tall — below 44px", that the Frap is `56px`, and that the Frap extends its tap area a further 8px with `--frapTouchOffset`. Those are the document's own arithmetic, not a rendered measurement: **this is a document, not a running page, so no tap target was measured here.** What can be said is that the default pill, as documented, is specified below the 44×44px minimum for touch-only surfaces, and that the source already flags this and says padding "may be visually expanded" on mobile without stating to what. That hedge is recorded in Known Gaps.

### Reduced motion

`@media (prefers-reduced-motion: reduce)` removes the `scale(0.95)` press pop, every translate, the floating-label overshoot curve, the gift-card grid stagger and the loading placeholder pulse. Opacity fades remain, capped at `{motion.duration-reduced}` (130ms) — including the extracted image fade, which is shortened from its real `300ms`. The focus ring is never animated and never suppressed.

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
| `{colors.warning}` (`#fbbc05`) on `{colors.surface-gold-wash}` (`#faf6ee`) | 1.58:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Use Neutral Warm (`#f2f0eb`) or Ceramic (`#edebe9`) as page canvas instead of pure white — the warm cream is the signature
- Map the green tiers to their intended surface role — Starbucks Green for headings, Green Accent for CTAs, House Green for deep bands, Uplift for decorative
- Keep tracking tight at `-0.01em` / `-0.16px` on SoDoSans across the whole system
- Use 50px full-pill radius on every button without exception
- Apply `transform: scale(0.95)` as the universal button active state
- Reserve Gold for Rewards-status ceremony moments only
- Use SoDoSans for nearly everything; switch to Lander Tall serif only for Rewards editorial headlines; reserve Kalam script for Careers "cup name" moments
- Layer 2–3 low-alpha shadows instead of one heavier drop shadow for elevation
- Use the Frap circular CTA as the persistent floating order entry on every shopping surface
- Let the cream canvas breathe between content cards — use whitespace, not dividers
- Draw any boundary that must actually be perceived in `{colors.accent}` or `{colors.text}`, and keep `{colors.border-input}` and `{colors.border-hairline}` for decorative separation
- Draw focus with `{colors.focus}` on cream and white grounds and `{colors.focus-on-dark}` on House Green and Black, always 2px at 2px offset outside the control
- Animate `transform` and `opacity` only, and honour `prefers-reduced-motion` by dropping the `scale(0.95)` press pop while keeping the opacity fades

### Don't
- Don't use pure white as the page canvas — the warm cream temperature is load-bearing
- Don't pick "one brand green" — the four-green system is intentional; using only `#006241` everywhere flattens the brand
- Don't use Gold as a general-purpose accent — it's a Rewards signal only
- Don't square the corners on buttons — the 50px pill is universal
- Don't introduce gradient fills — the system is color-block throughout
- Don't weight-contrast h1 and h2 by size — the hierarchy comes from weight + color (600 Starbucks-Green vs 400 Text Black)
- Don't use pure black for body text — `rgba(0,0,0,0.87)` matches the warm canvas
- Don't skip the `scale(0.95)` active feedback on buttons — it's a signature micro-interaction
- Don't stack single heavy shadows; always layer 2–3 low-alpha ones
- Don't introduce serifs or scripts into the main shopping flow — they belong to Rewards and Careers contexts respectively
- Don't rely on `{colors.border-input}` as the only edge of a text input — at 1.40:1 on white it is not a perceivable boundary
- Don't set Gold or Yellow as text on any light surface — both are fill and ceremony tones, and neither is readable there
- Don't remove the focus ring, and don't let a reduced-motion preference suppress it

## Responsive Behavior

### Breakpoints

Inferred from component width tokens and progressive nav heights:

| Name | Width | Key Changes |
|------|-------|-------------|
| xs | < 480px | Global nav 64px; hamburger menu; single-column layouts; pill buttons full-width |
| Mobile | 480–767px | Global nav 72px; gift-card grid 2-up; card padding tightens |
| Tablet | 768–1023px | Global nav 83px; gift-card grid 3-up; hero split begins to appear |
| Desktop | 1024–1439px | Global nav 99px; gift-card grid 4-up; full asymmetric hero 40/60 |
| XLarge | 1440px+ | Content caps at `--columnWidthXLarge`; gift-card grid 5-up; extra cream margin |

### Touch Targets

- Pill buttons at `7px 16px` padding measure ~32px tall — below 44px WCAG AAA minimum for touch-only surfaces. On mobile, button padding may be visually expanded to meet the minimum.
- Frap floating circular button at `56px` is well above minimum.
- Frap uses `--frapTouchOffset: calc(-1 * .8rem)` to extend tap area 8px beyond visual edge.
- Form float-label inputs grow their label font size on mobile (1.6rem base vs 1.9rem desktop) — easier to tap and read at arm's-length.

### Collapsing Strategy

- **Global nav height scales progressively**: 64 → 72 → 83 → 99px across breakpoints, not a single value
- **Hero split collapses**: 40/60 asymmetric split → stacked (image top, content below) at mobile
- **Gift-card grid**: 5-up → 4-up → 3-up → 2-up → 1-up across breakpoints with adjusted card widths
- **Feature bands**: Stay full-width but text + imagery stack vertically on mobile
- **Outer gutter scales**: 16px → 24px → 40px as viewport grows
- **Rewards 3-column status panels**: Stack to single column on mobile

### Image Behavior

- Hero product photography crops tighter vertically on mobile; content becomes the visual anchor
- Gift-card illustrations preserve aspect ratio; card grid reflows
- `opacity 0.3s ease-in` fade-in transition on image load (prevents jarring pop-in)
- Rewards app-in-hand photography scales proportionally; never stretches

## Known Gaps

This file was one of the collection's ten legacy documents: it carried no frontmatter token block and used numbered headings (`## 1. Visual Theme & Atmosphere` and so on). The `colors`, `typography`, `spacing`, `rounded`, `shadow` and `components` groups above were built **only** from values already written in its prose, and the headings were renamed to the current set. Nothing was invented to fill a column. The legacy `## 9. Agent Prompt Guide` has no slot in the current section contract and is kept verbatim after this section rather than deleted. What the prose does not contain is listed here.

### Gaps in the extraction

- **Interaction states are almost entirely absent.** The source documents the press state (`scale(0.95)`, universal), one focus behaviour (the Add-in select's border shift), one selected state (the size-selector ring) and the error state at token level only. **Hover, disabled and loading appear nowhere in the file, for any component** — there is no hover tint, no disabled tone in the palette, and no skeleton or spinner. The Interaction States subsection therefore *marks* coverage rather than filling it, and the focus-visible ring is prescribed by this audit and labelled as such. Three of the eight contract states are left unfilled and the score is accepted as lost.
- **No focus treatment was extracted** beyond the one border shift. `{colors.focus}` and `{colors.focus-on-dark}` are prescribed; both reuse tones the palette already owns. The live site's focus appearance is unknown.
- **No motion values beyond four fragments.** The source states `all 0.2s ease` on buttons, `300ms` with `cubic-bezier(0.25, 0.46, 0.45, 0.94)` for the expander, `cubic-bezier(0.32, 2.32, 0.61, 0.27)` for the checked input, `opacity 0.3s ease-in` on image load, and names `--duration: 0.4s` and `--iconTransition: all ease-out 0.2s` without saying what they apply to. Everything else in Motion & Animation is the prescribed Playful profile.
- **Two boundary tones were only ever named inside component specs** (`#d6dbde`, `#e7e7e7`); the original colour list omitted them entirely. They are tokenised in Colors now, and both fail the 3:1 boundary threshold — see Accessibility.
- **The PDP size selector and breadcrumb are described twice, inconsistently.** The component spec puts the size name in Starbucks Green and the fluid-ounce caption in Text Black Soft, implying a light ground; the agent prompt for the same component puts both in white on the House Green band. `{components.size-option-selector}` records the component spec's reading, because that is the more detailed of the two. The real ground is unresolved.
- **"Proxima Nova" appears in five PDP component specs** (the Rewards Cost Pill, nutrition rows, breadcrumb, back link) although the typography section states SoDoSans is universal and never mentions Proxima Nova. This is almost certainly a fallback the extraction caught mid-font-load, so no `proxima` token was created; the PDP components reference the SoDoSans scale instead.
- **Gift-card tile radius and shadow are hedged in the source itself**: "similar to cards (`~12px`, slightly tighter on corners)" and "lighter than default card". The tilde and the comparative are the source's; `{components.card-gift-tile}` records the card radius and no shadow token rather than inventing a second value.
- **Rewards status card tier colours are not stated.** The source describes a "colored gradient/color header ring" per tier (Bronze / Gold / Silver-ish) with no hex for any of the three, and names the third tier "Silver-ish". No tier tokens exist.
- **Form error styling is incomplete.** The invalid-field tint is extracted; border weight, icon placement and message typography are not.
- **No tap-target dimensions beyond the pill's own arithmetic.** The source computes ~32px from `7px 16px` padding and says mobile padding "may be visually expanded to meet the minimum" without stating the expanded value, so the 44×44px minimum can be neither confirmed nor failed from this document.
- **Letter-spacing is stated two ways** — `-0.16px` in the hierarchy table and `-0.01em` in the token list — and the source uses both without reconciling them. Both are recorded on the typography entries they belong to; at 16px they are not the same value.
- **Weight ranges are kept as ranges** (`400–600`) because the source states them as ranges; no single canonical weight was picked for display, hero, body-large, small or button-label.
- **No sizes for the two secondary typefaces.** `{typography.rewards-serif}` and `{typography.careers-script}` carry a family and nothing else, because the source gives neither a size nor a weight for either.
- **Breakpoint values are the source's own inference**, not extracted media queries: it says so itself ("Inferred from component width tokens and progressive nav heights").
- **Careers and Starbucks-Card components are named but not specified** — the cup-name card, the search radio grid, and the SVC mockup behind `--svcRoundedCorners` / `--svcShadowFilter`. `{rounded.svc}` and `{shadow.svc}` carry the two values the source does state.

### Gaps stated in the original document

- SoDoSans is a proprietary typeface not available on Google Fonts — when implementing publicly, use Inter or Manrope as a substitute and document the swap
- Lander Tall (Rewards serif) is also custom — substitute with Iowan Old Style, Lora, or Source Serif Pro
- Specific per-component animation timings beyond the few documented (`--duration: 0.4s`, `--iconTransition: all ease-out 0.2s`, `--expanderDuration: 300ms`) are not captured for every interactive surface
- Form error-state full styling (red border weight, icon placement) visible on the tint token but not exhaustively extracted
- Careers-page specific components (cup-name card, search radio grid) are referenced in token names but not covered by this extraction
- Starbucks Visa Card / Starbucks-Card (SVC) detailed mockup specs are hinted at by `--svcRoundedCorners` and `--svcShadowFilter` tokens but not fully documented

## Agent Prompt Guide

### Quick Color Reference

- Primary CTA: "Green Accent (`#00754A`)"
- Primary CTA text: "White (`#ffffff`)"
- Brand heading: "Starbucks Green (`#006241`)"
- Feature band / footer: "House Green (`#1E3932`)"
- Page canvas: "Neutral Warm (`#f2f0eb`)"
- Card canvas: "White (`#ffffff`)"
- Heading text on light: "Text Black (`rgba(0,0,0,0.87)`)"
- Body text on light: "Text Black Soft (`rgba(0,0,0,0.58)`)"
- Body text on dark-green: "Text White Soft (`rgba(255,255,255,0.70)`)"
- Rewards accent: "Gold (`#cba258`)"
- Rewards text: "Rewards Green (`#33433d`)"
- Destructive: "Red (`#c82014`)"

### Example Component Prompts

1. "Create a primary Starbucks CTA pill button with Green Accent (`#00754A`) background, white text 'Explore our afternoon menu', SoDoSans font at 16px weight 600 with `-0.01em` letter-spacing, `50px` border-radius (full pill), `7px 16px` padding. Apply `transform: scale(0.95)` as the active state with a `0.2s ease` transition."

2. "Design a content card with White (`#ffffff`) background at `12px` border-radius, layered shadow `0 0 0.5px rgba(0,0,0,0.14), 0 1px 1px rgba(0,0,0,0.24)`. Pad contents `16–24px` (`--space-3` to `--space-4`). Place on a Neutral Warm (`#f2f0eb`) page canvas with `16px` gap to siblings."

3. "Build the Frap floating circular order button — `56px` diameter, Green Accent (`#00754A`) fill, white shopping-bag icon centered. Layered shadow: `0 0 6px rgba(0,0,0,0.24)` + `0 8px 12px rgba(0,0,0,0.14)`. Fixed position bottom-right with `-0.8rem` touch offset. Active state collapses the ambient shadow to `0 8px 12px rgba(0,0,0,0)` with `scale(0.95)`."

4. "Build a dark-green feature band — full-width section with House Green (`#1E3932`) background. Left column: white SoDoSans h2 at 24px weight 600, followed by a Text White Soft (`rgba(255,255,255,0.70)`) body paragraph and a CTA row with two buttons (White-filled with Green Accent text for primary, Outlined-on-Dark white border for secondary). Right column: product photography. Split ratio 40/60, stacked vertically below `768px`."

5. "Create a Rewards status card — House Green (`#1E3932`) panel with `12px` border-radius, colored gradient top stripe (Bronze/Silver/Gold tier). Title in SoDoSans 24px weight 600 in white. Benefits list as white bullets with `rgba(255,255,255,0.70)` secondary captions. Bottom progression text in Text White Soft. Stack 3 panels in a grid at `lg+`, single column on mobile."

6. "Design a gift-card tile — card radius matches `12px`, fills with an illustrated photograph (hand-drawn watercolor-painted feel) as the entire surface. Subtle drop shadow makes it feel like a physical card on the cream canvas. Group under a category label ('Spring', 'Thank You', 'Birthday') in SoDoSans 24px weight 400 above the grid."

7. "Create a Starbucks product-detail header — House Green (`#1E3932`) band with breadcrumb 'Menu / Refreshers / Pink Energy Drink' in 14/400 white above the product title in SoDoSans 32/700 uppercase white. Product photograph centered below title. Below photo: a 4-up size selector row — each cup-icon button shows a vertical cup silhouette, size name ('Tall' / 'Grande' / 'Venti' / 'Trenta') in 16/700 white, and fluid-ounce in 13/400 Text White Soft. Selected size wraps the cup icon in a `2px solid #00754A` circular ring."

8. "Build a Starbucks customize flow — under the size selector, 3 stacked outlined-rectangle input rows (white bg, `1px solid #d6dbde` border, `4px` radius). Each has a floating label ('Add-ins', 'Milk', 'Add-ins') above the top border in 13/700 Text Black uppercase. Value centered (e.g., 'Ice', 'Coconut'). Right side: chevron-down in Text Black Soft. For the scoop row, embed a numeric stepper (`−` `1` `+` with circular `32px` outlined buttons). Below all three fields: outlined green 'Customize' pill with gold sparkle icon, `50px` radius, `14px 40px` padding. Pair with a Green Accent filled 'Add to Order' pill in the same row."

9. "Design a Starbucks product description band — full-width House Green (`#1E3932`) below product header. Top: a gold-outlined '200★ item' Rewards Cost Pill (`50px` radius, `4px 12px` padding, gold `#cba258` border and text). Below: product description in white 16/400/1.5. Nutritional inline summary in white 14/700 ('140 calories, 25g sugar, 2.5g fat') with info-icon tooltip. Outlined-white-on-green pill button 'Full nutrition &amp; ingredients list'. 32px vertical padding."

10. "Create a Starbucks nutrition facts table — two-column layout inside a White card. Left column: 'Ingredients' header (24/400 Text Black), followed by ingredient list or 'Not available for this item' placeholder paragraph in 14/400 Text Black Soft. Right column: 'Nutrition' header, then label/value rows (nutrient name left, value right) separated by `1px solid #e7e7e7` hairlines. Typography: labels in 14/400 Text Black, values in 14/700 Text Black right-aligned. Footnote asterisk markers in 13/400 Text Black Soft at the bottom."

### Iteration Guide

When refining existing screens generated with this design system:
1. Focus on ONE component at a time
2. Reference specific color names and hex codes from this document
3. Use natural language descriptions ("warm cream canvas," "four-tier green system") alongside exact values
4. Preserve the 50px pill + `scale(0.95)` active state universally
5. Check that greens are mapped to their correct role (Green Accent for CTA, Starbucks Green for heading, House Green for band)
6. Don't introduce gradients — the system is color-block
7. Keep SoDoSans tracking at `-0.01em` / `-0.16px` across the board
