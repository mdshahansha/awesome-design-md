---
version: alpha
name: Oracle Analysis
description: An analysis of Oracle's design language — an enterprise system built on a warm neutral ladder rather than a colour palette. Six numbered greys carry almost every surface, a single dark charcoal carries every action, and the famous red is held back for the wordmark alone. Two display registers coexist, being a very light sans on the corporate index and a Georgia serif across the product pages, and the only chromatic moments are a thin gold rule under a headline and the occasional full-width band of teal or forest green.

colors:
  primary: "#312d2a"
  primary-pressed: "#47423e"
  on-primary: "#ffffff"
  brand-mark: "#c74634"
  ink: "#161513"
  ink-deep: "#211e1c"
  canvas: "#ffffff"
  canvas-soft: "#fbf9f8"
  canvas-tint: "#f5f4f2"
  canvas-warm: "#f1efed"
  hairline: "#e4e1dd"
  divider: "#e9e7e4"
  field-border: "#d4cfca"
  hairline-strong: "#857f79"
  link: "#006b8f"
  accent-gold: "#f0cc71"
  accent-gold-soft: "#f7e0a1"
  band-teal: "#d6e5e5"
  band-forest: "#33553c"
  focus: "#227e9e"
  focus-on-dark: "#9ad5e8"
  error: "#d63b25"
  disabled-ink: "#aea8a2"

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
  display-serif-xl:
    fontFamily: Georgia
    fontSize: 56px
    fontWeight: 400
    lineHeight: 67.2px
    letterSpacing: 0
  display-serif-lg:
    fontFamily: Georgia
    fontSize: 40px
    fontWeight: 400
    lineHeight: 48px
    letterSpacing: 0
  display-serif-md:
    fontFamily: Georgia
    fontSize: 36px
    fontWeight: 400
    lineHeight: 43.2px
    letterSpacing: 0
  display-sans-lg:
    fontFamily: Oracle Sans
    fontSize: 40px
    fontWeight: 300
    lineHeight: 52px
    letterSpacing: 0
  display-sans-md:
    fontFamily: Oracle Sans
    fontSize: 32px
    fontWeight: 300
    lineHeight: 44px
    letterSpacing: 0
  heading-xl:
    fontFamily: Oracle Sans
    fontSize: 28px
    fontWeight: 800
    lineHeight: 33.6px
    letterSpacing: 0
  heading-lg:
    fontFamily: Oracle Sans
    fontSize: 24px
    fontWeight: 800
    lineHeight: 28.8px
    letterSpacing: 0
  heading-md:
    fontFamily: Oracle Sans
    fontSize: 20px
    fontWeight: 800
    lineHeight: 24px
    letterSpacing: 0
  heading-sm:
    fontFamily: Oracle Sans
    fontSize: 18px
    fontWeight: 800
    lineHeight: 21.6px
    letterSpacing: 0
  heading-card:
    fontFamily: Oracle Sans
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: 0
  lead:
    fontFamily: Oracle Sans
    fontSize: 24px
    fontWeight: 400
    lineHeight: 33.6px
    letterSpacing: 0
  body:
    fontFamily: Oracle Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 22.4px
    letterSpacing: 0
  body-loose:
    fontFamily: Oracle Sans
    fontSize: 16px
    fontWeight: 350
    lineHeight: 24px
    letterSpacing: 0
  body-strong:
    fontFamily: Oracle Sans
    fontSize: 16px
    fontWeight: 700
    lineHeight: 22.4px
    letterSpacing: 0
  label:
    fontFamily: Oracle Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 16.8px
    letterSpacing: 0
  label-strong:
    fontFamily: Oracle Sans
    fontSize: 14px
    fontWeight: 600
    lineHeight: 20px
    letterSpacing: 0
  caption:
    fontFamily: Oracle Sans
    fontSize: 12px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 15px
  full: 9999px

spacing:
  xs: 10px
  sm: 12px
  md: 16px
  lg: 18px
  xl: 20px
  xxl: 24px
  xxxl: 32px
  section: 48px
  gutter: 72px

components:
  masthead:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    height: 85px
  logo-wordmark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.brand-mark}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    borderColor: "{colors.field-border}"
    rounded: "{rounded.sm}"
    padding: 12px 18px
  product-subnav:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    height: 64px
  product-subnav-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    height: 64px
  subnav-active-bar:
    backgroundColor: "{colors.accent-gold-soft}"
    rounded: "{rounded.none}"
    height: 5px
    width: 67px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-primary-disabled:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.disabled-ink}"
    typography: "{typography.label}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-secondary:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-tertiary:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-primary-inverse:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-secondary-inverse:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    borderColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  hero-band:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-serif-md}"
    rounded: "{rounded.none}"
    padding: 48px
  hero-eyebrow-rule:
    backgroundColor: "{colors.accent-gold}"
    rounded: "{rounded.none}"
    width: 40px
    height: 4px
  section-band-white:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 48px
  section-band-soft:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 48px
  section-band-tint:
    backgroundColor: "{colors.canvas-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 48px
  section-band-warm:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 48px
  section-band-teal:
    backgroundColor: "{colors.band-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 48px
  section-band-forest:
    backgroundColor: "{colors.band-forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 48px
  content-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-loose}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxxl}"
  stat-panel:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-loose}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  product-card-warm:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  nav-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-strong}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  media-frame:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
  play-button-circular:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    size: 40px
  channel-column:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-lg}"
    borderColor: "{colors.divider}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl}"
  link-inline:
    textColor: "{colors.link}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    height: 105px
  footer-link:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"

  # ─── Examples (illustrative) — kit-mirror demonstration surfaces ───
  ex-pricing-tier:
    description: "Default pricing tier card. Product-card chrome with a hairline border, since the system separates same-rung surfaces with a rule rather than a shadow."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  ex-pricing-tier-featured:
    description: "Featured tier — polarity-flipped to the action charcoal with white text, the same inversion the dark bands perform."
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  ex-product-selector:
    description: "What's-included summary card, one rung up the neutral ladder. Rows borrow the navigation-tile chrome."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  ex-cart-drawer:
    description: "Subscription summary. Line items are separated by the same warm rule the contact page uses between columns."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
    item-divider: "{colors.divider}"
  ex-app-shell-row:
    description: "Sidebar nav row at the product-card radius. Active state is marked by the action charcoal, the system's only emphasis fill."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  ex-data-table-cell:
    description: "Data-table header and body chrome. The header sits one rung up the ladder and rows are divided by a hairline."
    headerBackground: "{colors.canvas-tint}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body}"
    cellPadding: "{spacing.sm} {spacing.md}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in card. Product-card chrome with the masthead search field's input treatment inside."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  ex-modal-card:
    description: "Modal dialog surface — product-card chrome with a hairline border and no shadow, because the system has none."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  ex-empty-state-card:
    description: "Empty-state frame one rung up the ladder, padded to the section rhythm."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.section}"
    captionTypography: "{typography.body}"
  ex-toast:
    description: "Toast notification — the product-card radius on a white surface, bounded by a hairline instead of an elevation."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.xl}"
    typography: "{typography.body}"

---


## Overview

Oracle's web system is unusual for an enterprise brand in that it barely uses colour at all. The page ground is a six-step ladder of warm neutrals that runs from pure white through three off-whites to a warm near-black, and that ladder does almost all the structural work. Sections are distinguished from one another not by cards or rules or shadows but by which rung of the ladder they sit on, stacked full-bleed and square-cornered so the page reads as a series of tonal shifts rather than a stack of containers.

The famous Oracle red appears exactly once per page, in the masthead wordmark, and nowhere else. Every action on the site is carried by `{colors.primary}`, a warm dark charcoal, in a small 4px-radius button that never grows louder than its label. The restraint is deliberate and total: there is no coloured CTA, no accent-tinted card, no gradient. When colour does arrive it arrives at full-band scale, a whole section width of `{colors.band-teal}` or `{colors.band-forest}`, and then the page returns to neutral.

What gives the system its character is the type. Two display registers run side by side. The corporate index sets its headings in Oracle Sans at weight 300, very large and very light, while the product pages set theirs in Georgia, a bookish transitional serif that is genuinely surprising on a database landing page. Beneath both, Oracle Sans handles everything else across a wide weight range, dropping to 350 for running copy and jumping all the way to 800 for section headings, so the contrast between a paragraph and the heading above it is enormous without either changing size very much. A single gold rule, 40 by 4 pixels, sits under the hero headline. It is the only decorative mark in the system, and against this much neutral it does a lot of work.

**Key Characteristics:**
- A six-rung warm neutral ladder — `{colors.canvas}` → `{colors.canvas-soft}` → `{colors.canvas-tint}` → `{colors.canvas-warm}` → `{colors.hairline}` → `{colors.ink-deep}` — carrying nearly every surface
- `{colors.brand-mark}` reserved for the wordmark and used nowhere else in the interface
- Every action in one warm charcoal `{colors.primary}` at `{rounded.xs}`, with no coloured CTA anywhere
- Two display registers, being Oracle Sans at weight 300 on the corporate index and Georgia serif across the product pages
- An extreme body-to-heading weight jump, from 350/400 running copy straight to 800 section headings
- Full-bleed square-cornered bands with no shadows — depth comes from tonal steps alone
- A 40 × 4px `{colors.accent-gold}` rule under the hero headline as the system's only ornament
- Chromatic colour deployed only at whole-band scale, never on a control

## Colors

### Brand & Accent
- **Oracle Red** (`{colors.brand-mark}` — #c74634): the wordmark, and only the wordmark. It appears in the masthead at the top of every page and is not used for any button, link, border, band or highlight. Elsewhere on the page red shows up only inside photography and inside logos printed on product hardware.
- **Action Charcoal** (`{colors.primary}` — #312d2a): the fill behind every primary action on the site. Warm rather than neutral, and a clear step lighter than `{colors.ink}` so a filled button reads as an object rather than as a block of text.
- **Action Charcoal Pressed** (`{colors.primary-pressed}` — #47423e): the active state of that button.
- **On Primary** (`{colors.on-primary}` — #ffffff): the label on a filled action, and the text colour on every inverted surface.
- **Gold Rule** (`{colors.accent-gold}` — #f0cc71): a 40 × 4px bar sitting under the hero headline on every product page. The system's one piece of ornament.
- **Gold Tab** (`{colors.accent-gold-soft}` — #f7e0a1): a paler gold, 5px tall, marking the selected item in the dark product sub-navigation.

### Surface
The surface set is a numbered ladder, and its rungs are close enough together that a band change reads as a shift in light rather than as a new panel.

- **Canvas** (`{colors.canvas}` — #ffffff): the masthead, the footer, content cards, and the brightest section bands.
- **Canvas Soft** (`{colors.canvas-soft}` — #fbf9f8): the most common product-page section fill. One barely-perceptible step off white.
- **Canvas Tint** (`{colors.canvas-tint}` — #f5f4f2): the next step, used for supporting sections and the contact hero.
- **Canvas Warm** (`{colors.canvas-warm}` — #f1efed): the warmest and most-used tint, carrying the corporate index page almost end to end and every product hero band.
- **Hairline** (`{colors.hairline}` — #e4e1dd): the tile and disabled-control border, and the last neutral rung before the dark end. Extracted and frozen. At 1.3:1 on `{colors.canvas}` it is **decoration only** — a tonal seam between two surfaces on the same rung, not a boundary a user has to find. Anywhere the rule is the only thing defining a control, use `{colors.hairline-strong}` instead.
- **Divider** (`{colors.divider}` — #e9e7e4): the 2px vertical rule that separates the contact page's channel columns. Extracted and frozen, and at 1.23:1 on `{colors.canvas}` the palest boundary in the system. Decoration only, on the same terms as `{colors.hairline}`.
- **Field Border** (`{colors.field-border}` — #d4cfca): the 1px border around the masthead search field, one clear step darker than `{colors.hairline}` so an input reads as interactive against a card that merely reads as a container. At 1.55:1 on `{colors.canvas}` that step is visible but still well below the 3:1 a control boundary needs; see Accessibility.
- **Hairline Strong** (`{colors.hairline-strong}` — #857f79): **prescribed, not extracted.** The accessible counterpart to `{colors.hairline}`, carried at the warm hue of the ladder so it reads as the same family rather than as an imported grey. It measures 3.96:1 on `{colors.canvas}` and clears 3:1 on every neutral rung and on `{colors.band-teal}`, so it is the boundary to draw wherever a rule is load-bearing — the `{components.text-input}` edge, a `{components.ex-modal-card}` perimeter, a table row separator a reader has to track across. The real brand uses `{colors.hairline}` there and fails AA; this token exists so a rebuild does not have to.
- **Ink Deep** (`{colors.ink-deep}` — #211e1c): the dark end of the ladder, used as a full-width band behind the product sub-navigation.

### Text
- **Ink** (`{colors.ink}` — #161513): every heading and every line of body copy. A warm near-black, never pure black, which keeps the very light 300-weight display sizes from looking harsh.
- **Link** (`{colors.link}` — #006b8f): inline links in body copy and channel columns. A deep teal-blue, set without an underline, at the same size and weight as the text around it — the colour alone carries the affordance.
- On dark bands, text inverts to `{colors.on-primary}` and there is no intermediate tone; the system has one text colour per polarity.
- **There is no secondary or muted ink.** Captions, footer fine print and table headers are all set in `{colors.ink}` and differentiated by size and weight alone — which is consistent with a system that carries hierarchy on the 350-to-800 weight axis. `{colors.disabled-ink}` is **not** a muted text tone and must not be used as one: it measures 2.24:1 on `{colors.canvas-soft}` and is exempt from the contrast requirement only because it is scoped to disabled controls. See Known Gaps.

### Semantic
- **Focus** (`{colors.focus}` — #227e9e): the focus indicator on every light surface — the four neutral rungs and `{colors.band-teal}`. A deeper relative of `{colors.link}`, so the keyboard affordance and the pointer affordance read as the same hue. Measured 4.62:1 against `{colors.canvas}` and 4.03:1 against `{colors.canvas-warm}`, both above the 3:1 required. Drawn as a 2px ring **outside** the control with a 2px offset, so it is judged against the surface behind the control rather than against the control's own fill — which matters here because `{colors.primary}` is a dark fill no light ring could also clear.
- **Focus On Dark** (`{colors.focus-on-dark}` — #9ad5e8): **prescribed, not extracted.** The same focus hue flipped to its light polarity, for rings drawn on the system's dark grounds. One ring cannot serve both polarities here: `{colors.focus}` measures only 1.81:1 on `{colors.band-forest}`, far under 3:1, so the band that carries the site's one deep colour would have no visible ring at all. This counterpart measures 5.21:1 on `{colors.band-forest}`, 10.3:1 on `{colors.ink-deep}` and 8.48:1 on `{colors.primary}`. It follows the system's own rule for dark grounds — flip polarity, keep the colour — the same move `{components.button-primary-inverse}` makes.
- **Error** (`{colors.error}` — #d63b25): validation messaging and error field text. 4.65:1 on `{colors.canvas}`, so it passes AA for body copy, but it is close to the brand red and must never be set next to `{colors.brand-mark}`.
- **Disabled Ink** (`{colors.disabled-ink}` — #aea8a2): the label on a disabled control, paired with a `{colors.canvas-soft}` fill and a `{colors.hairline}` border.

### Band Colours
Chromatic colour enters the system only as a full section band, never as a control, a card or a border.
- **Band Teal** (`{colors.band-teal}` — #d6e5e5): a pale teal strip, roughly 120 to 160px tall, used to break a run of neutral sections.
- **Band Forest** (`{colors.band-forest}` — #33553c): a deep green band carrying white text and a multi-column link list, around 390px tall.

## Typography

### Font Family
Three families, with a clear division of labour.

**Oracle Sans** is the workhorse — a variable humanist sans with open apertures and a slightly squared construction. Its variable axis is exercised hard: the declared base weight is 350, running copy sits at 350 or 400, and section headings jump all the way to 800. It also supplies the corporate index's display sizes at weight 300.

**Georgia** is the display serif on the product pages. It carries h1, h2 and h3 at 36 to 56px in regular weight, with its bracketed serifs and ball terminals reading as distinctly bookish next to the sans beneath it. It is declared as an explicit stack led by Georgia, so it renders as Georgia on virtually every machine rather than falling back.

**Consolas** is declared for monospace and never appears in page chrome.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-serif-xl}` | 56px | 400 | 67.2px | 0 | Product hero headline, Georgia |
| `{typography.display-serif-lg}` | 40px | 400 | 48px | 0 | Major section headline, Georgia |
| `{typography.display-serif-md}` | 36px | 400 | 43.2px | 0 | Product page headline and section headline, Georgia |
| `{typography.display-sans-lg}` | 40px | 300 | 52px | 0 | Corporate index section headline, Oracle Sans Light |
| `{typography.display-sans-md}` | 32px | 300 | 44px | 0 | Corporate index page headline, Oracle Sans Light |
| `{typography.heading-xl}` | 28px | 800 | 33.6px | 0 | Product section heading |
| `{typography.heading-lg}` | 24px | 800 | 28.8px | 0 | Section and channel-column heading |
| `{typography.heading-md}` | 20px | 800 | 24px | 0 | Sub-section heading |
| `{typography.heading-sm}` | 18px | 800 | 21.6px | 0 | Card heading |
| `{typography.heading-card}` | 24px | 600 | 32px | 0 | Corporate index card heading |
| `{typography.lead}` | 24px | 400 | 33.6px | 0 | Standfirst paragraph under a hero |
| `{typography.body}` | 16px | 400 | 22.4px | 0 | Product page running copy and links |
| `{typography.body-loose}` | 16px | 350 | 24px | 0 | Corporate index running copy, at the declared base weight |
| `{typography.body-strong}` | 16px | 700 | 22.4px | 0 | Emphasised list item and inline lead-in |
| `{typography.label}` | 14px | 500 | 16.8px | 0 | Button label |
| `{typography.label-strong}` | 14px | 600 | 20px | 0 | Navigation tile label |
| `{typography.caption}` | 12px | 400 | 20px | 0 | Footer links and fine print |

### Principles
Letter-spacing is zero on every role without exception. There is no tracked-out eyebrow, no tightened display line, no small-caps label — the system leaves the typeface's own fitting alone at every size from 12px to 56px.

Line-height moves in two registers. Display and heading roles run at a tight 1.2 (67.2/56, 48/40, 28.8/24, 21.6/18 all resolve to exactly 1.2), while body roles open up to 1.4 (22.4/16) or 1.5 (24/16). The split is clean: anything that is a heading is set tight, anything that is read in sentences is set loose.

The weight range is the most distinctive thing about the system. Running copy sits at 350 or 400 and section headings sit at 800, with almost nothing in between, so hierarchy is carried by weight far more than by size. A 24px 800-weight heading over 16px 400-weight body is a much sharper break than the 1.5× size ratio alone would suggest. The 300-weight display sizes on the corporate index run in the opposite direction, being lighter than the body text they sit above.

### Note on Font Substitutes
**Oracle Sans** is a proprietary variable face. The closest open substitute is **Inter**, which shares the humanist skeleton and open apertures and offers a full variable weight axis including the 350 and 800 stops this system depends on; **Source Sans 3** is a warmer alternative but tops out lower and needs the 800 roles dropped to 700. **Georgia** ships with virtually every operating system and needs no substitution; if a webfont is required, **Gelasio** is metric-compatible with it. **Consolas** substitutes cleanly with **JetBrains Mono**. Keep the 1.2 heading line-height, the 1.4 body line-height, and zero tracking on any substitute.

## Layout

### Spacing System
- **Base unit**: 8px, though the working steps are finer at the small end and jump hard at the large end.
- **Tokens**: `{spacing.xs}` 10px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 18px · `{spacing.xl}` 20px · `{spacing.xxl}` 24px · `{spacing.xxxl}` 32px · `{spacing.section}` 48px · `{spacing.gutter}` 72px
- `{spacing.section}` is the universal rhythm constant. Every full-width section on every page is padded `48px 0`, which is what gives the band stack its regularity.
- `{spacing.xxxl}` is the grid gutter and the corporate index card interior; `{spacing.xxl}` is the product card interior.
- Button padding is a fixed `10px 16px` everywhere, and headings carry an 18px bottom margin.

### Grid & Container
- **Outer container**: 1744px maximum, with a 72px side gutter.
- **Context container**: 1600px maximum for content that sits inside a band.
- **Minimum container**: 272px, which is the floor the layout collapses toward on the narrowest phones.
- **Grid gap**: 32px between columns, used by the corporate index tile row, the channel columns and the product card grids.
- **Masthead**: 85px tall, full width, white. **Product sub-navigation**: 64px, full width, sticky. **Footer**: 105px, full width, white.
- Sections are full-bleed and square-cornered; the container only constrains the content inside them, never the band itself.

### Whitespace Philosophy
Space is used to make the tonal ladder legible. Because adjacent bands can differ by as little as four or five points of lightness, each one needs enough vertical room for the eye to register it as a separate region — hence the uniform 48px section padding and the willingness to give a 160px teal strip an entire band to itself. Inside a band the opposite applies: content is packed into a 1600px column with 32px gutters and relatively tight card padding, so the generous outer rhythm reads as structure rather than emptiness.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat fill on the neutral ladder | Every band, section, nav and footer — the default |
| 1 | One rung up or down the ladder | Cards on a tinted band, the dark sub-navigation strip |
| 2 | 1px `{colors.hairline}` border | Navigation tiles and disabled controls |

The system carries **no shadows at all**. Not on cards, not on the sticky sub-navigation, not on the masthead, not on modals. Depth is produced entirely by position on the neutral ladder: a white card on a `{colors.canvas-warm}` band reads as raised because it is lighter, and a `{colors.ink-deep}` sub-navigation reads as a distinct plane because it is far darker. Where two surfaces sit on the same rung, a 1px `{colors.hairline}` border does the separating instead.

There are no gradients in the page chrome. The only tonal transitions in the system are the feathered lower edge of a cut-out hero photograph and the angled diagonal that ends some hero bands, and both belong to the image, not to the surface.

### Decorative Depth
Hero bands carry very low-contrast pattern overlays — dense topographic contour lines on one product page, large open swirls on another — drawn a point or two off the band fill. They read as texture rather than as image, and they are the reason a large area of `{colors.canvas-warm}` does not feel empty. Some hero bands end on an angled diagonal rather than a horizontal edge, letting the following band cut up into them.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Every band, section, masthead, sub-navigation and footer |
| `{rounded.xs}` | 4px | Every button, and every anchor styled as a button |
| `{rounded.sm}` | 6px | The masthead search field and small column items |
| `{rounded.md}` | 8px | Product page cards and media frames |
| `{rounded.lg}` | 12px | Corporate index navigation tiles |
| `{rounded.xl}` | 15px | Corporate index content cards and their inner stat panels |
| `{rounded.full}` | 9999px | The circular video play control |

The scale is unusually fine-grained at the small end, with 4, 6 and 8 all in active use and each assigned to a different control family — buttons, fields, cards. The two large steps are template-specific rather than interchangeable: the corporate index uses 15px throughout while the product pages use 8px, so a card's radius tells you which template you are on. The 15px value is worth noting as a deliberate oddity, since 16px would be the conventional choice and the system consistently uses 15.

### Photography Geometry
Images inside product cards take `{rounded.md}`; images filling half a corporate index card take `{rounded.xl}`. Full-band photography is square-cornered. Aspect ratios are not fixed — video thumbnails run roughly 16:9, hero photography is a wide strip, and card imagery fills whatever the card gives it. The system never crops to a circle except for the play control.

## Components

> Every component below documents its Default state. Variants live as separate entries in the `components:` front matter.

### Interaction States

Oracle expresses state the same way it expresses elevation: by moving one rung, not by adding a new colour. Only the pressed charcoal `{colors.primary-pressed}` and the gold selection bar are extracted state values; the rest of this table is **prescribed** to the same rule, and is labelled as such in Known Gaps.

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.primary}` fill | fill lightens to `{colors.primary-pressed}` | 2px `{colors.focus}` ring, 2px offset | `{colors.primary-pressed}`, extracted | `{components.button-primary-disabled}` | label holds, inline spinner in `{colors.on-primary}`, pointer events off | n/a — not a toggle | n/a — error is shown on the field, not the button |
| `button-secondary` | 1px `{colors.ink}` border | border thickens to 2px, no fill change | 2px `{colors.focus}` ring, 2px offset | 8% `{colors.ink}` wash | border and label to `{colors.disabled-ink}` | inline spinner in `{colors.ink}` | n/a | n/a |
| `button-tertiary` | borderless, 8% `{colors.ink}` wash | wash deepens to 12% | 2px `{colors.focus}` ring, 2px offset | wash to 16% | label `{colors.disabled-ink}`, no wash | inline spinner in `{colors.ink}` | n/a | n/a |
| `button-primary-inverse` | `{colors.canvas}` fill on a dark band | fill to `{colors.canvas-warm}` | 2px `{colors.focus-on-dark}` ring, 2px offset | fill to `{colors.hairline}` | fill to 24% `{colors.on-primary}`, label 60% | inline spinner in `{colors.ink}` | n/a | n/a |
| `button-secondary-inverse` | 1px `{colors.on-primary}` border on `{colors.ink-deep}` | border to 2px | 2px `{colors.focus-on-dark}` ring, 2px offset | 12% `{colors.on-primary}` wash | border and label to 40% `{colors.on-primary}` | inline spinner in `{colors.on-primary}` | n/a | n/a |
| `text-input` | 1px `{colors.field-border}`; use `{colors.hairline-strong}` where the rule is the only boundary | border to `{colors.ink}` | 2px `{colors.focus}` ring, 2px offset, border held | same as focus-visible | fill `{colors.canvas-soft}`, border `{colors.hairline}`, text `{colors.disabled-ink}` | border held, inline spinner at the trailing edge | n/a | 1px `{colors.error}` border plus a `{colors.error}` message in `{typography.label}` below the field |
| `nav-tile` | 1px `{colors.hairline}` border on `{colors.canvas}` | fill to `{colors.canvas-soft}`, border to `{colors.hairline-strong}` | 2px `{colors.focus}` ring, 2px offset | fill to `{colors.canvas-tint}` | label `{colors.disabled-ink}` | skeleton block at `{colors.canvas-tint}` | n/a — tiles navigate, they do not latch | n/a |
| `product-subnav` item | `{colors.on-primary}` label on `{colors.ink-deep}` | label underline, 1px, `{colors.on-primary}` | 2px `{colors.focus-on-dark}` ring, 2px offset | underline held | label to 40% `{colors.on-primary}` | n/a | 5px `{colors.accent-gold-soft}` bar, `{components.subnav-active-bar}`, extracted | n/a |
| `product-subnav-light` item | `{colors.ink}` label on `{colors.canvas}` | label underline, 1px, `{colors.ink}` | 2px `{colors.focus}` ring, 2px offset | underline held | label to `{colors.disabled-ink}` | n/a | 5px `{colors.ink}` underline, the light-polarity equivalent of the gold bar | n/a |
| `link-inline` | `{colors.link}`, no underline | underline appears; the colour does not change | 2px `{colors.focus}` ring, 2px offset | underline held | `{colors.disabled-ink}`, no underline | n/a | n/a | n/a |
| `footer-link` | `{colors.ink}` in `{typography.caption}` | underline appears | 2px `{colors.focus}` ring, 2px offset | underline held | n/a | n/a | n/a | n/a |
| `play-button-circular` | `{colors.ink}` fill, 40px | fill to `{colors.primary}` | 2px `{colors.focus}` ring, 2px offset — or `{colors.focus-on-dark}` when the control sits over photography | fill to `{colors.primary-pressed}` | n/a | n/a | n/a | n/a |
| `ex-app-shell-row` | `{colors.canvas}` | fill to `{colors.canvas-soft}` | 2px `{colors.focus}` ring, 2px offset | fill to `{colors.canvas-tint}` | label `{colors.disabled-ink}` | skeleton block at `{colors.canvas-tint}` | 3px leading bar in `{colors.primary}` | n/a |
| `ex-pricing-tier` | 1px `{colors.hairline}` border | border to `{colors.hairline-strong}` | ring belongs to the CTA inside, not the card | n/a — the card is not itself a control | n/a | skeleton blocks at `{colors.canvas-tint}` | 2px `{colors.primary}` border | n/a |

Two components genuinely have one state each and nothing more: `{components.hero-eyebrow-rule}` and `{components.subnav-active-bar}` are static bars, not controls, and have no hover, focus or pressed behaviour at all. `{components.masthead}`, `{components.footer}`, `{components.media-frame}` and the six band variants are containers with a single default state; their children carry the interaction.

### Masthead & Navigation

**`masthead`**
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.none}`, 85px tall
- Full width and identical on every page. Carries a hamburger, the wordmark, a wide search field and three utility icons

**`logo-wordmark`**
- Text `{colors.brand-mark}`, type `{typography.heading-lg}`, rounded `{rounded.none}`
- The only appearance of red in the interface

**`text-input`**
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, 1px `{colors.field-border}` border, rounded `{rounded.sm}`, padding `12px 18px`
- The masthead search field. A leading icon is inset with 48px of left padding

**`product-subnav`**
- Background `{colors.ink-deep}`, text `{colors.on-primary}`, type `{typography.body}`, rounded `{rounded.none}`, 64px tall
- A sticky full-bleed strip below the masthead on a product page, holding the section links for that product

**`product-subnav-light`**
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.none}`, 64px tall
- The same strip in its light polarity, where the active item is marked by an ink underline instead of a gold bar

**`subnav-active-bar`**
- Background `{colors.accent-gold-soft}`, rounded `{rounded.none}`, 67 × 5px
- Marks the selected item in the dark sub-navigation

### Buttons

Every button in the system is `{rounded.xs}` with `10px 16px` padding and a `{typography.label}` label. Only the fill and border change between variants.

**`button-primary`**
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.label}`, rounded `{rounded.xs}`, padding `10px 16px`
- The primary action everywhere. Frequently markup'd as an anchor rather than a button element

**`button-primary-pressed`**
- Background `{colors.primary-pressed}`, otherwise identical

**`button-primary-disabled`**
- Background `{colors.canvas-soft}`, text `{colors.disabled-ink}`, 1px `{colors.hairline}` border, rounded `{rounded.xs}`, padding `10px 16px`

**`button-secondary`**
- Transparent fill, text `{colors.ink}`, 1px `{colors.ink}` border, rounded `{rounded.xs}`, padding `10px 16px`
- The outlined companion, always paired to the right of a primary

**`button-tertiary`**
- Text `{colors.ink}`, rounded `{rounded.xs}`, padding `10px 16px`
- A borderless tonal variant whose fill is an 8% wash of `{colors.ink}` over whatever surface it sits on, so it reads as a soft block rather than a defined edge

**`button-primary-inverse`**
- Background `{colors.canvas}`, text `{colors.ink}`, rounded `{rounded.xs}`, padding `10px 16px`
- The primary action on a dark band — the polarity flips rather than the colour changing

**`button-secondary-inverse`**
- Transparent fill, text `{colors.on-primary}`, 1px `{colors.on-primary}` border, rounded `{rounded.xs}`, padding `10px 16px`

### Bands & Sections

All six band variants are full-bleed, square-cornered and padded `48px 0`. They differ only in fill.

**`hero-band`**
- Background `{colors.canvas-warm}`, text `{colors.ink}`, type `{typography.display-serif-md}`, rounded `{rounded.none}`, padding `48px`
- Opens every product page. Carries a low-contrast pattern overlay and frequently ends on an angled diagonal

**`hero-eyebrow-rule`**
- Background `{colors.accent-gold}`, rounded `{rounded.none}`, 40 × 4px
- Sits directly under the hero headline. The system's only ornament

**`section-band-white`** · **`section-band-soft`** · **`section-band-tint`** · **`section-band-warm`**
- Backgrounds `{colors.canvas}`, `{colors.canvas-soft}`, `{colors.canvas-tint}` and `{colors.canvas-warm}` respectively
- All text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.none}`, padding `48px`
- The four neutral rungs. A page is built by alternating them; the shift between adjacent rungs is deliberately small

**`section-band-teal`**
- Background `{colors.band-teal}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.none}`, padding `48px`
- A short chromatic strip, around 120 to 160px tall, used to interrupt a long neutral run

**`section-band-forest`**
- Background `{colors.band-forest}`, text `{colors.on-primary}`, type `{typography.body}`, rounded `{rounded.none}`, padding `48px`
- The one deep colour band, carrying white text and a multi-column link list

### Cards & Media

**`content-card`**
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-loose}`, rounded `{rounded.xl}`, padding `{spacing.xxxl}`
- The corporate index workhorse. A wide card holding a headline, copy, a primary action and a half-width image

**`stat-panel`**
- Background `{colors.canvas-warm}`, text `{colors.ink}`, type `{typography.body-loose}`, rounded `{rounded.xl}`, padding `{spacing.xl}`
- A tinted block nested inside a content card, holding a short bulleted list of figures

**`product-card`** and **`product-card-warm`**
- Backgrounds `{colors.canvas}` and `{colors.canvas-warm}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.md}`, padding `{spacing.xxl}`
- The product page equivalent, at the smaller radius. The warm variant is used when the card sits on a white band

**`nav-tile`**
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.label-strong}`, 1px `{colors.hairline}` border, rounded `{rounded.lg}`, padding `{spacing.md}`
- The row of eight product entry tiles below the corporate index masthead, grouped under two light sans labels

**`media-frame`**
- Background `{colors.canvas}`, rounded `{rounded.md}`
- The frame around an embedded video or product screenshot

**`play-button-circular`**
- Background `{colors.ink}`, icon `{colors.on-primary}`, rounded `{rounded.full}`, 40px
- The only circular element in the system

### Content & Links

**`channel-column`**
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.heading-lg}`, 2px `{colors.divider}` rule, rounded `{rounded.none}`, padding `{spacing.xxl}`
- A three-up group on the contact page. Each column holds a thin outline icon, an 800-weight heading, a short paragraph and a `{components.link-inline}`, separated by full-height vertical rules

**`link-inline`**
- Text `{colors.link}`, type `{typography.body}`, rounded `{rounded.none}`
- Set with no underline and at the same size and weight as the surrounding copy

### Footer

**`footer`**
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.caption}`, rounded `{rounded.none}`, 105px tall
- A single horizontal row of fine-print links above a row of social icons. No rule, no fill change, no column structure

**`footer-link`**
- Text `{colors.ink}`, type `{typography.caption}`, rounded `{rounded.none}`
- Set in ink rather than `{colors.link}`, which is what keeps the footer quiet

### Examples (illustrative)

> These ten surfaces are kit-mirror demonstrations, not components found on the brand's own pages. Each is composed from the primitives above so downstream consumers re-skin the shapes this system actually uses — the square `{rounded.none}` band, the `{rounded.xs}` button, the `{rounded.md}` card, and a neutral ladder that separates surfaces by tone and a hairline rule instead of by shadow.

**`ex-pricing-tier`** — default tier card
- Background `{colors.canvas}`, text `{colors.ink}`, 1px `{colors.hairline}` border, rounded `{rounded.md}`, padding `{spacing.xxl}`
- CTA from `{components.button-secondary}`

**`ex-pricing-tier-featured`** — the highlighted tier
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.md}`, padding `{spacing.xxl}`
- Polarity-flipped to the action charcoal, the same inversion `{components.section-band-forest}` performs, with its CTA from `{components.button-primary-inverse}`

**`ex-product-selector`** — what's-included summary card
- Background `{colors.canvas-soft}`, text `{colors.ink}`, rounded `{rounded.md}`, padding `{spacing.xxl}`
- One rung up the ladder, with rows borrowing `{components.nav-tile}` chrome

**`ex-cart-drawer`** — subscription summary
- Background `{colors.canvas}`, text `{colors.ink}`, rounded `{rounded.md}`, padding `{spacing.xxl}`, line items separated by `{colors.divider}`
- The same warm rule `{components.channel-column}` uses between columns

**`ex-app-shell-row`** — sidebar nav row
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, active indicator `{colors.primary}`

**`ex-data-table-cell`** — table header and body chrome
- Header background `{colors.canvas-tint}` in `{typography.caption}`, body cells `{typography.body}`, cell padding `{spacing.sm} {spacing.md}`, row border `{colors.hairline}`

**`ex-auth-form-card`** — sign-in card
- Background `{colors.canvas}`, text `{colors.ink}`, 1px `{colors.hairline}` border, rounded `{rounded.md}`, padding `{spacing.xxl}`
- Inputs take the `{components.text-input}` treatment

**`ex-modal-card`** — modal dialog surface
- Background `{colors.canvas}`, text `{colors.ink}`, 1px `{colors.hairline}` border, rounded `{rounded.md}`, padding `{spacing.xxl}`
- No shadow, since the system has none — the modal is bounded by its rule alone

**`ex-empty-state-card`** — empty-state frame
- Background `{colors.canvas-soft}`, text `{colors.ink}`, rounded `{rounded.md}`, padding `{spacing.section}`, caption in `{typography.body}`

**`ex-toast`** — toast notification surface
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body}`, 1px `{colors.hairline}` border, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.xl}`

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity. It was not measured from the live site — no timing function, duration or curve below is an extracted fact.** It is derived from what the file does document: a page built from full-bleed tonal bands with no shadows, an editorial Georgia display register, a single 40 × 4px ornament, and chromatic colour held back to whole-band scale. A system that restrained will not pop, bounce or overshoot, so the **Calm** profile applies — composed, opacity-led, little travel.

The governing rule is the same one that governs colour here: motion moves a surface one rung, it does not introduce a new gesture. Nothing travels further than 8px, because an 8px slide is the motion equivalent of a 1.05:1 tonal step, and this system's whole argument is that a step that small is enough.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, tile, link) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` of the fill wash; no `transform` — the tile does not lift, because this system has no shadow to lift into | Fill and underline change instantly, with no transition |
| Press | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the pressed wash only. No `scale`: a scale pop is a Playful signature and would read as foreign on a `{rounded.xs}` charcoal button | Instant, with no transition |
| Focus (focus-visible ring) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the ring, 0 to 1 | Ring appears instantly at full opacity — never faded in, never suppressed |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` 0 to 1 on the content column. The band fills do not animate, so the tonal ladder is painted and stable before anything moves | Content fades in at `{motion.duration-reduced}`; no travel |
| Modal / drawer | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` plus `transform: translateY(8px)` to `0`. The scrim fades `opacity` only. Per `{components.ex-modal-card}` there is no shadow to animate | `opacity` only at `{motion.duration-reduced}`; the 8px travel is removed |
| Dropdown (masthead menu, subnav overflow) | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` plus `transform: translateY(4px)` to `0` | `opacity` only at `{motion.duration-reduced}`; no travel |
| Toast | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` plus `transform: translateY(8px)` to `0` on `{components.ex-toast}` | `opacity` only at `{motion.duration-reduced}`; no travel |
| List enter (card grid, tile row, channel columns) | `{motion.duration-base}` per item, `{motion.stagger-step}` apart, capped at 8 items so the last card is never more than 320ms behind the first | `{motion.ease-enter}` | `opacity` plus `transform: translateY(8px)` to `0` | All items fade together at `{motion.duration-reduced}`; stagger and travel both removed |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` only, no stagger — shorter than its entrance, as every exit here is | Instant removal |
| Loading | `{motion.duration-emphasis}` loop | `{motion.ease-standard}` | `opacity` pulse between 1.0 and 0.55 on a `{colors.canvas-tint}` skeleton block. This is the only infinite animation in the system; there is no brand ambience. A spinner inside a button rotates by `transform` at the same 500ms period | Pulse and rotation both freeze; the skeleton holds at a static `{colors.canvas-tint}` and the button shows a static label change instead |

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translateY travel, all scale, the list stagger, and the
     loading pulse and spinner rotation — skeleton and spinner freeze. */
  /* Retained: opacity fades, clamped to {motion.duration-reduced} (150ms),
     and the focus-visible ring, which appears instantly and is never
     suppressed under any setting. */
}
```

What is removed: every `transform` — the 8px modal, toast and list-enter travel, and the 4px dropdown travel — the `{motion.stagger-step}` cadence, and both infinite animations, which freeze rather than stop mid-cycle.

What remains: opacity fades, every one of them clamped to `{motion.duration-reduced}` and never longer, and the focus ring, which is an accessibility affordance rather than decoration. No state change is cancelled under reduced motion; only its travel is. There is no brand ambience in this system to freeze.

## Accessibility

### Measured Contrast

Every ratio below is computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` #161513 on `{colors.canvas}` #ffffff | 18.25:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-warm}` #f1efed | 15.91:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.band-teal}` #d6e5e5 | 14.08:1 | 4.5:1 | Pass |
| `{colors.on-primary}` #ffffff on `{colors.primary}` #312d2a | 13.64:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.band-forest}` #33553c | 8.38:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.ink-deep}` #211e1c | 16.57:1 | 4.5:1 | Pass |
| `{colors.link}` #006b8f on `{colors.canvas}` | 6.0:1 | 4.5:1 | Pass |
| `{colors.link}` on `{colors.band-teal}` | 4.63:1 | 4.5:1 | Pass — the tightest link pairing in the system |
| `{colors.brand-mark}` #c74634 on `{colors.canvas}` | 4.82:1 | 4.5:1 | Pass |
| `{colors.error}` #d63b25 on `{colors.canvas}` | 4.65:1 | 4.5:1 | Pass |
| `{colors.focus}` #227e9e on `{colors.canvas}` | 4.62:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` #857f79 on `{colors.canvas}` | 3.96:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.band-teal}` | 3.05:1 | 3.0:1 | Pass — the tightest boundary pairing |
| `{colors.field-border}` #d4cfca on `{colors.canvas}` | 1.55:1 | 3.0:1 | **Fail** |
| `{colors.field-border}` on `{colors.canvas-warm}` #f1efed | 1.35:1 | 3.0:1 | **Fail** |
| `{colors.hairline}` #e4e1dd on `{colors.canvas}` | 1.3:1 | 3.0:1 | **Fail** |
| `{colors.hairline}` on `{colors.canvas-soft}` #fbf9f8 | 1.24:1 | 3.0:1 | **Fail** |
| `{colors.hairline}` on `{colors.canvas-tint}` #f5f4f2 | 1.19:1 | 3.0:1 | **Fail** |
| `{colors.hairline}` on `{colors.canvas-warm}` | 1.14:1 | 3.0:1 | **Fail** |
| `{colors.divider}` #e9e7e4 on `{colors.canvas}` | 1.23:1 | 3.0:1 | **Fail** |
| `{colors.divider}` on `{colors.canvas-soft}` | 1.18:1 | 3.0:1 | **Fail** |
| `{colors.divider}` on `{colors.canvas-tint}` | 1.12:1 | 3.0:1 | **Fail** |
| `{colors.divider}` on `{colors.canvas-warm}` | 1.08:1 | 3.0:1 | **Fail** |
| `{colors.disabled-ink}` #aea8a2 on `{colors.canvas-soft}` | 2.24:1 | — | Exempt — WCAG sets no contrast requirement on disabled controls |
| `{colors.on-primary}` #ffffff, the `{components.button-secondary-inverse}` border, measured against `{colors.canvas}` | 1.0:1 | 3.0:1 | Not a rendering pair — see below |

The last row needs explaining rather than fixing. `{components.button-secondary-inverse}` is the outlined button **for dark bands only**: its 1px border is `{colors.on-primary}` white, and it is drawn on `{colors.ink-deep}`, which this file now declares as the component's own `backgroundColor`. Against that real ground the border measures 16.57:1. The 1.0:1 figure is white-on-white, which is what you get by measuring the border against the page canvas instead of against the surface the component actually sits on, and that combination cannot occur: the white-bordered variant on a white band would be invisible, which is precisely why `{components.button-secondary}` with its `{colors.ink}` border exists for light grounds. The pair is stated here with its measured ratio for completeness, not as a defect to repair.

**Oracle's real boundary tones fail WCAG AA, and that is the most useful fact in this document.** Three extracted neutrals do boundary work and none reaches 3:1 against the white canvas: `{colors.divider}` at 1.23:1, `{colors.hairline}` at 1.3:1, and `{colors.field-border}` at 1.55:1 — the last being the border of the masthead search field, which means the site's only text input has no perceptible edge for a low-vision user. The failure gets worse, not better, as a boundary moves up the ladder onto a card: `{colors.hairline}` falls from 1.3:1 on white to 1.14:1 on `{colors.canvas-warm}`, and `{colors.divider}` from 1.23:1 to 1.08:1, because the rule and the fill converge. Nothing in the extracted palette can carry that job: the next rung past #d4cfca is `{colors.ink-deep}` #211e1c at the far dark end, with nothing in between. That is why `{colors.hairline-strong}` is prescribed rather than selected from the ladder. The three extracted values are facts and are not altered here; they are scoped to decoration in the Colors section, and `{colors.hairline-strong}` is specified wherever a rule is load-bearing.

### Focus Ring Visibility

Two rings, because one cannot clear 3:1 on both polarities of this system.

| Surface this file defines | Ring drawn | Ratio |
|---|---|---|
| `{colors.canvas}` #ffffff | `{colors.focus}` | 4.62:1 |
| `{colors.canvas-soft}` #fbf9f8 | `{colors.focus}` | 4.4:1 |
| `{colors.canvas-tint}` #f5f4f2 | `{colors.focus}` | 4.2:1 |
| `{colors.canvas-warm}` #f1efed | `{colors.focus}` | 4.03:1 |
| `{colors.band-teal}` #d6e5e5 | `{colors.focus}` | 3.56:1 |
| `{colors.ink-deep}` #211e1c | `{colors.focus-on-dark}` | 10.3:1 |
| `{colors.band-forest}` #33553c | `{colors.focus-on-dark}` | 5.21:1 |
| `{colors.primary}` #312d2a used as a surface | `{colors.focus-on-dark}` | 8.48:1 |

The ring is 2px with a **2px offset, drawn outside the control**, so it is measured against the surface behind the control and not against the control's own fill. That offset is load-bearing rather than cosmetic: `{colors.primary}` is a dark charcoal button fill sitting on a white canvas, and no single ring colour clears 3:1 against both at once — a ring light enough for the charcoal is too light for the white. Drawing it outside, against the stated surface, is what WCAG 2.2 Focus Appearance asks for and is the only arithmetically possible answer here.

`{colors.focus}` on `{colors.band-forest}` measures **1.81:1** and must never be used there; that pairing is the reason the second ring exists.

Two tokens are deliberately absent from the table above. `{colors.accent-gold}` is a 40 × 4px rule and `{colors.accent-gold-soft}` a 67 × 5px selection bar: neither is a ground a control is ever placed on, so neither needs ring coverage. For the record, `{colors.focus}` measures **2.99:1** on `{colors.accent-gold}` — one hundredth under the threshold — and 3.55:1 on `{colors.accent-gold-soft}`. If a future rebuild ever promotes the gold to a real surface, the 2.99:1 figure means the light ring would have to be re-derived for it rather than reused. The earlier claim in this file that the ring is "applied identically on light and dark surfaces" was wrong in contrast terms and has been corrected.

### Minimum Tap Target

`{components.button-primary}` resolves to 37px tall from its 10px vertical padding and 16.8px `{typography.label}` line box, under the 44 × 44 minimum, and relies on surrounding margin. Raising vertical padding to 14px brings it to 45px without changing any other value in the system. `{components.text-input}` at roughly 46px, `{components.product-subnav}` at 64px and `{components.nav-tile}` all clear the minimum. **These figures are arithmetic from the declared padding and line heights, not measurements of a rendered page** — nothing in this audit renders, so no claim is made here about actual hit area, overlap, or spacing between adjacent targets.

### Reduced Motion

Every animation in Motion & Animation is `transform` or `opacity` only; no `width`, `height`, `top`, `left` or `margin` is animated anywhere. Under `@media (prefers-reduced-motion: reduce)` all travel and all scale are removed, opacity fades are clamped to `{motion.duration-reduced}` at 150ms, and the two infinite animations — the skeleton pulse and the in-button spinner — freeze. The focus ring is exempt from suppression and appears instantly.

### Other Notes

- Hierarchy here rests on a 350-to-800 weight jump rather than on colour, which is robust for low-vision and monochrome users. The 300-weight display sizes at 32 to 40px are the exception and should not be taken below 32px, where a 300 weight thins past legibility.
- `{components.link-inline}` carries its affordance by colour alone, with no underline. At 6.0:1 against the canvas it passes contrast, but colour-only link signalling fails WCAG 1.4.1 Use of Colour for links set inside running copy. The prescribed hover underline in Interaction States helps pointer users and nobody else; an underline on the default state would be the correct fix and would contradict the brand's stated rule. This is a genuine conflict, recorded in Known Gaps rather than resolved.
- The neutral ladder's own steps are 1.04:1 to 1.05:1 between adjacent rungs. Band boundaries are therefore invisible to many users, and the system compensates with the uniform 48px rhythm rather than with contrast. Band adjacency must never be the only carrier of meaning.

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
| best ring `{colors.focus}` (`#227e9e`) against `{colors.accent-gold}` (`#f0cc71`) | 2.99:1 | 3.0:1 | Fail — no focus ring this file declares reaches 3:1 on that surface |
| `{colors.error}` (`#d63b25`) on `{colors.canvas-soft}` (`#fbf9f8`) | 4.43:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Build page structure from the neutral ladder. Moving a section one rung is the system's way of saying "new region".
- Keep `{colors.brand-mark}` on the wordmark and nowhere else. Its scarcity is what gives it weight.
- Run every action through `{colors.primary}` at `{rounded.xs}` with `10px 16px` padding, whatever the context.
- Flip polarity rather than changing colour when an action lands on a dark band — use `{components.button-primary-inverse}`.
- Hold `{spacing.section}` at 48px on every full-width band; the uniform rhythm is what makes the small tonal steps legible.
- Let weight carry hierarchy. The 400-to-800 jump between body and heading is the system's main structural signal.
- Keep letter-spacing at zero on every role, at every size.
- Deploy chromatic colour only at whole-band scale, as `{components.section-band-teal}` or `{components.section-band-forest}`.

### Don't
- Don't add shadows. The system has none, and elevation is expressed by position on the neutral ladder.
- Don't use pure black. `{colors.ink}` is warm and deliberately a few points off it.
- Don't round a band, a section, a masthead or a footer — `{rounded.none}` on full-width chrome is the rule.
- Don't mix the two card radii. `{rounded.xl}` belongs to the corporate index and `{rounded.md}` to the product pages; using both on one page breaks the template read.
- Don't set a headline in Oracle Sans on a product page or in Georgia on the corporate index — the two registers do not cross templates.
- Don't underline `{components.link-inline}`; `{colors.link}` alone carries the affordance.
- Don't add a fourth or fifth tint between the ladder rungs. They are already close enough that another step would be invisible.
- Don't give `{components.hero-eyebrow-rule}` a second colour or a second instance per page; one 40 × 4px gold bar is the whole ornament budget.

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Small mobile | ≤ 450px | Single column throughout; masthead collapses to hamburger, wordmark and icons; tile row stacks |
| Mobile | 451–600px | The system's heaviest breakpoint — sub-navigation becomes a scrolling strip, card grids go 1-up, hero type drops to its floor |
| Tablet | 601–770px | The second heaviest — grids go 2-up, the search field collapses to an icon, channel columns stack and lose their dividers |
| Laptop | 771–974px | 2-up and 3-up grids, side gutters tighten from 72px toward the container minimum |
| Desktop | 975–1344px | Full multi-column grids, sub-navigation shows all items inline |
| Wide | 1345–1744px | Content reaches the 1600px context cap; bands continue full-bleed |
| Ultra-wide | ≥ 1744px | Outer container caps; surplus width is absorbed by the band fills on either side |

### Touch Targets
`{components.button-primary}` stands 37px tall at its 10px vertical padding and 14px label, which is under the 44×44 WCAG AAA minimum and relies on surrounding margin for comfortable tapping. `{components.text-input}` and `{components.product-subnav}` both clear it comfortably, at roughly 46px and 64px respectively, as does `{components.nav-tile}`. For rebuilds, raising the button's vertical padding to 14px brings it to 45px without changing any other value in the system.

### Collapsing Strategy
The masthead is the element that changes most: at desktop it carries a hamburger, the wordmark, a wide search field and three utility icons, and below tablet the search field collapses to an icon while the rest holds position. The product sub-navigation keeps its full-bleed band at every width and turns into a horizontally scrolling strip rather than wrapping, so the active `{components.subnav-active-bar}` stays visible. Card grids step 4-up to 3-up to 2-up to 1-up across the ladder. The channel columns on the contact page drop their `{colors.divider}` vertical rules when they stack, since a vertical rule between stacked blocks reads as a mistake. Section padding holds at `{spacing.section}` far longer than most systems would keep it, compressing only at the mobile breakpoints.

### Image Behavior
Photography is full-bleed inside its container and square-cornered when it fills a band, but takes `{rounded.md}` when it sits inside a product card and `{rounded.xl}` when it fills half of a corporate index content card. Video thumbnails carry a circular `{components.play-button-circular}` overlay. The contact hero uses a cut-out photographic strip with a soft feathered lower edge rather than a hard crop. Decorative pattern overlays — fine topographic contour lines, large open swirls — sit behind hero content at very low contrast and are treated as part of the band fill rather than as images.

## Known Gaps

### Prescribed, not extracted

- **The entire Motion & Animation section.** Every duration, easing curve, travel distance and stagger is prescribed from the **Calm** profile to match this brand's visual identity. Nobody measured Oracle's real timing functions. The profile assignment is itself a judgement, argued from the file's own evidence: full-bleed tonal bands, a Georgia editorial display register, display weights of 300 and 400, a single ornament, no gradients and no shadows. Oracle's business is database and cloud infrastructure, which would point at a Crisp, tool-like profile — but this file documents the corporate and product marketing web, where `{typography.display-serif-xl}` is a 56px Georgia headline and monospace "never appears in page chrome". The documented identity is editorial, so Calm stands.
- **`{colors.hairline-strong}` #857f79.** A prescribed accessible boundary. The real brand has no boundary tone that reaches 3:1; see Accessibility.
- **`{colors.focus-on-dark}` #9ad5e8.** A prescribed light-polarity counterpart to `{colors.focus}`, needed because `{colors.focus}` measures 1.81:1 on `{colors.band-forest}`. `{colors.focus}` #227e9e is itself extracted; its 2px width and 2px outward offset are prescribed, as the file records no measured ring geometry.
- **Interaction States.** Only two cells in that table are extracted: `{colors.primary-pressed}` as the pressed fill, and `{components.subnav-active-bar}` as the selected marker in the dark sub-navigation. Every hover wash percentage, focus geometry, disabled treatment, loading skeleton and error treatment is prescribed by extending the system's one-rung rule. In particular, no loading state of any kind was observed on the real site.

### Genuinely absent from the brand

- **There is no `text-dim` role, and none has been invented here.** The SPEC token contract requires a secondary or muted ink; Oracle's palette has none. Captions, footer fine print and table headers are all set in `{colors.ink}` and separated by size and weight, which is coherent for a system whose hierarchy rides the 350-to-800 weight axis. The only candidate tone, `{colors.disabled-ink}` #aea8a2, is scoped to disabled controls and measures 2.24:1 on `{colors.canvas-soft}`; promoting it to secondary text would both falsify the brand and ship an AA failure. The honest state of this document is that the role is unfilled. A rebuild that needs a muted ink should prescribe one at or above 4.5:1 on `{colors.canvas-warm}` — around #6b6660, which measures 4.96:1 there — and label it prescribed.
- **No shadow tokens, deliberately.** The system carries no shadows at all, so no `shadow:` group exists to reference. This is an extracted fact, not an omission.
- **Colour-only link affordance.** `{components.link-inline}` has no underline in its default state, which fails WCAG 1.4.1 for links inside running copy. Fixing it means contradicting an explicit brand rule, so it is documented rather than silently overridden. See Accessibility.

### Not knowable from a document

Nothing in this audit renders a page. There is no DOM, no screenshot and no dev server, so this file makes no claim about overlap, horizontal overflow, clipping, actual tap-target hit area, frame rate or layout shift. The tap-target figures in Accessibility are arithmetic from declared padding and line heights only.

### Unverified in the source extraction

- The six-rung ladder is described in the Overview as running through `{colors.hairline}` to `{colors.ink-deep}`, but `{colors.hairline}` is used as a border rather than as a section fill, so whether it is genuinely a surface rung or only a boundary tone is unresolved.
- `{components.button-tertiary}` is documented as "an 8% wash of `{colors.ink}` over whatever surface it sits on". The resulting composite is not a token and its contrast was therefore not measured; on `{colors.canvas}` the wash resolves to roughly #ebebea, which would put any boundary it implies far below 3:1.
- `{rounded.xl}` is 15px where 16px would be conventional. The file treats this as a deliberate oddity; whether it is intentional or an artefact of the extraction is not established.
- Oracle Sans is proprietary and its real variable axis range is not recorded here beyond the 300, 350, 400, 500, 600, 700 and 800 stops this file uses.
