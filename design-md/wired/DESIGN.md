---
version: alpha
name: Wired-Inspired-design-analysis
description: An inspired interpretation of Wired's design language — a flagship technology-magazine brand whose surface is a strict editorial duet of stark black wordmark on white canvas, anchored by a tall narrow custom display serif for hero headlines, a humanist serif body face for long-form reading, and a clean sans face for metadata; layout reads like a printed magazine ported to the web with very little marketing chrome.

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  ink: "#000000"
  ink-soft: "#1a1a1a"
  body: "#757575"
  hairline: "#e0e0e0"
  canvas: "#ffffff"
  canvas-soft: "#f5f5f5"
  link: "#057dbc"
  focus: "#057dbc"

typography:
  display-hero:
    fontFamily: WiredDisplay, "Times New Roman", Georgia, serif
    fontSize: 64px
    fontWeight: 400
    lineHeight: 59.52px
    letterSpacing: -0.5px
  display-lg:
    fontFamily: WiredDisplay, "Times New Roman", Georgia, serif
    fontSize: 48px
    fontWeight: 400
    lineHeight: 50.4px
    letterSpacing: -0.4px
  display-md:
    fontFamily: WiredDisplay, "Times New Roman", Georgia, serif
    fontSize: 32px
    fontWeight: 400
    lineHeight: 35.2px
    letterSpacing: -0.3px
  display-sm:
    fontFamily: WiredDisplay, "Times New Roman", Georgia, serif
    fontSize: 26px
    fontWeight: 400
    lineHeight: 28.08px
  display-xs:
    fontFamily: Apercu, "Helvetica Neue", Helvetica, Arial, sans-serif
    fontSize: 20px
    fontWeight: 700
    lineHeight: 24px
    letterSpacing: -0.28px
  body-serif-lg:
    fontFamily: BreveText, Georgia, "Times New Roman", serif
    fontSize: 19px
    fontWeight: 400
    lineHeight: 27.93px
    letterSpacing: 0.108px
  body-serif-md:
    fontFamily: BreveText, Georgia, "Times New Roman", serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: 0.09px
  body-md:
    fontFamily: Apercu, "Helvetica Neue", Helvetica, Arial, sans-serif
    fontSize: 17px
    fontWeight: 400
    lineHeight: 20px
  body-md-strong:
    fontFamily: Apercu, "Helvetica Neue", Helvetica, Arial, sans-serif
    fontSize: 17px
    fontWeight: 700
    lineHeight: 22px
    letterSpacing: -0.144px
  body-sm:
    fontFamily: Apercu, "Helvetica Neue", Helvetica, Arial, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 18px
    letterSpacing: 0.4px
  body-sm-strong:
    fontFamily: Apercu, "Helvetica Neue", Helvetica, Arial, sans-serif
    fontSize: 14px
    fontWeight: 700
    lineHeight: 18px
    letterSpacing: 0.4px
  byline:
    fontFamily: BreveText, Georgia, "Times New Roman", serif
    fontSize: 12.73px
    fontWeight: 700
    lineHeight: 28px
    letterSpacing: 0.108px
  caption:
    fontFamily: Apercu, "Helvetica Neue", Helvetica, Arial, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  button-md:
    fontFamily: Apercu, "Helvetica Neue", Helvetica, Arial, sans-serif
    fontSize: 16px
    fontWeight: 700
    lineHeight: 20px
    letterSpacing: 0.3px

rounded:
  none: 0px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 48px

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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  story-card-large:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg}"
  story-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xs}"
    padding: "{spacing.md}"
  story-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md-strong}"
    padding: "{spacing.lg} 0"
  category-eyebrow:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
  byline-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.byline}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-hero}"
    padding: "{spacing.4xl} {spacing.xl}"
  masthead-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    padding: "{spacing.md} {spacing.xl}"
  hairline-divider:
    borderColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.4xl} {spacing.xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Wired is the flagship technology-magazine brand under Condé Nast — and the web surface refuses to dress itself as a SaaS marketing site. The page is unmistakably an editorial product: a white canvas, a strict black wordmark in the brand's proprietary `WiredDisplay` (a tall, narrow, high-contrast serif used at 64 px), and stacked story cards that read as a printed magazine grid ported to the screen. There is no atmospheric gradient, no decorative chrome, no chromatic accent — the brand's only colour beyond the black-and-white duet is the small `{colors.link}` (`#057dbc`) used for inline body links inside long-form articles.

Type carries the entire identity. Three families ladder the system: `WiredDisplay` (the proprietary high-contrast serif) for hero / section headlines; `BreveText` (a humanist serif) for long-form body and bylines; and `Apercu` (a humanist sans) for metadata, captions, eyebrow tags, and buttons. The pairing is editorial-grade: serifs for narrative, sans for navigation and structural labels.

Buttons are square. The brand uses `{rounded.none}` 0 px corners across the entire UI — newsletter sign-ups, login forms, "Read more" CTAs all render as sharp rectangles. The only circular shape is the `button-icon-circular` used for social-share affordances. There are no soft drop-shadows; the brand uses hairline borders for elevation when needed.

**Key Characteristics:**
- A strict black-and-white duet with no chromatic accent except the inline link blue `{colors.link}`. The brand reads as a printed magazine.
- Three-face typographic system — `WiredDisplay` serif for display, `BreveText` serif for body, `Apercu` sans for metadata and buttons.
- Square buttons (`{rounded.none}`) — the brand never softens corners on interactive elements.
- A magazine-style story grid: large feature card at top, two-up secondary, then a vertical stack of bylined story rows separated by `{colors.hairline}` 1 px dividers.
- The brand's only signature decorative move is the **masthead band** — a thin black strip with the wordmark centred, no other decoration.
- A near-black `{colors.ink}` (`#000000`) footer band, no graphics, just text columns and the wordmark repeating.

## Colors

### Brand & Accent
- **Ink Black** (`{colors.primary}` — `#000000`): The brand's only "accent." Used for wordmark, headlines, CTAs, footer fill. Pure black, never softened.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): The default page background.
- **Canvas Soft** (`{colors.canvas-soft}` — `#f5f5f5`): Rare tint used for the comment-section background and search-result row hover states (not in the main page rhythm).
- **Hairline** (`{colors.hairline}` — `#e0e0e0`): 1 px dividers between story rows. The brand's only "line." **Decorative only** — at 1.32:1 on `{colors.canvas}` and 1.21:1 on `{colors.canvas-soft}` it is below the 3:1 a boundary needs, so where a rule is the only boundary of a control or a card use `{colors.ink}` or `{colors.body}` instead. See Accessibility.

### Text
- **Ink** (`{colors.ink}` — `#000000`): Every headline, every body paragraph in BreveText.
- **Ink Soft** (`{colors.ink-soft}` — `#1a1a1a`): A near-black variant used for caption-strong / footer link emphasis.
- **Body** (`{colors.body}` — `#757575`): Secondary metadata — bylines, timestamps, supporting body lines.

### Semantic
The brand operates with one inline link colour and no separate error / success / warning palette in its marketing surface. Validation cues on form pages use the ink black + body grey hierarchy.

- **Link** (`{colors.link}` — `#057dbc`): The inline body-link blue. Used only inside long-form article body copy, never on UI buttons or navigation.
- **Focus** (`{colors.focus}` — `#057dbc`): The focus ring. Not a new brand colour — it reuses the link blue, the one chromatic tone the brand owns, and is the only palette value that clears 3:1 on white, on `{colors.canvas-soft}` and on the black footer band. Prescribed, not extracted; see Accessibility.

## Typography

### Font Family
Three families ladder the system:
1. **WiredDisplay** — the proprietary tall-narrow high-contrast serif used exclusively for display headlines (64 px hero, scaling down to 26 px sub-display). The brand's most-recognisable typographic signature.
2. **BreveText** — the proprietary humanist serif used for long-form body, bylines, and editorial captions. Used at 16 – 19 px line-height 1.45 – 1.50 for comfortable reading density.
3. **Apercu** — a humanist sans used for nav, button labels, category eyebrows, metadata, and captions. Weights 400 / 700.

Inter is loaded as a fourth fallback face for embedded utility surfaces (the comment section, account pages) but does not appear on the main marketing / article surface.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-hero}` | 64px | 400 | 59.5px | -0.5px | Cover-story headline. |
| `{typography.display-lg}` | 48px | 400 | 50.4px | -0.4px | Major section / feature headlines. |
| `{typography.display-md}` | 32px | 400 | 35.2px | -0.3px | Story-card large variant. |
| `{typography.display-sm}` | 26px | 400 | 28px | 0 | Sub-display headings inside long-form articles. |
| `{typography.display-xs}` | 20px | 700 | 24px | -0.28px | Sans (Apercu) display micro-headings for category callouts. |
| `{typography.body-serif-lg}` | 19px | 400 | 27.93px | 0.108px | Lead paragraph of an article (BreveText). |
| `{typography.body-serif-md}` | 16px | 400 | 24px | 0.09px | Default article body (BreveText). |
| `{typography.body-md}` | 17px | 400 | 20px | 0 | Sans body (Apercu) for nav / metadata. |
| `{typography.body-md-strong}` | 17px | 700 | 22px | -0.144px | Bold sans body. |
| `{typography.body-sm}` | 14px | 400 | 18px | 0.4px | Secondary sans body. |
| `{typography.body-sm-strong}` | 14px | 700 | 18px | 0.4px | Bold caption / nav-link. |
| `{typography.byline}` | 12.73px | 700 | 28px | 0.108px | Article byline (BreveText). |
| `{typography.caption}` | 12px | 400 | 16px | 0 | Fine print, image captions. |
| `{typography.button-md}` | 16px | 700 | 20px | 0.3px | Button label. |

### Principles
- **Serif for narrative, sans for structure.** The serif faces never carry button labels or nav text; the sans face never carries article body.
- **Display weight 400** — the proprietary WiredDisplay reads as elegant by virtue of its thin-tall-narrow design at default weight, not via weight 700+.
- **Bylines use BreveText weight 700 with relaxed line-height 2.2.** The vertical breathing is part of the editorial signature.

### Note on Font Substitutes
The three proprietary faces have no exact substitutes. Best open-source approximations:
- **WiredDisplay** — *Playfair Display* weight 400 at large display sizes captures the high-contrast didone feel, though wider than the brand's tall-narrow proportions.
- **BreveText** — *Lora* or *Source Serif Pro* at 16 – 19 px.
- **Apercu** — *Inter* or *Manrope* weights 400 / 700.

## Layout

### Spacing System
- **Base unit**: 4 px.
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 20 px · `{spacing.2xl}` 24 px · `{spacing.3xl}` 32 px · `{spacing.4xl}` 48 px.
- **Section padding**: hero / story grid use `{spacing.4xl}` 48 px top/bottom on desktop.
- **Story row padding**: `{spacing.lg}` 16 px vertical between bylined story rows.

### Grid & Container
- Marketing content uses a wide container (~1400 px max).
- Cover-story grid: 1 large hero + 2-up secondary stories + vertical stack.
- Story-row stack: full-width single column with hairline dividers.

Responsive rules moved verbatim to the top-level `## Responsive Behavior`
section, per the section contract.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default — almost every surface lives at this level. |
| Level 1 — Hairline | 1 px solid `{colors.hairline}` border. | Story-row dividers, input borders. |
| Level 2 — Heavy Black Border | 2 px solid `{colors.ink}` border. | Subscribe CTA on certain campaign moments. |

The brand uses no drop-shadows. Surface contrast and hairline borders carry all visual hierarchy.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Every interactive shape — buttons, inputs, cards. The brand's signature square geometry. |
| `{rounded.full}` | 9999px | Circular icon containers only (social-share, account avatar). |

### Photography Geometry
- Cover stories: 16:9 hero, edge-to-edge.
- Secondary story cards: 4:3 thumbnails.
- Article body images: native aspect, full column width.
- Bylines / avatars: circular `{rounded.full}` 28 px crops.

## Components

### Buttons

**`button-primary`** — the square black CTA.
- Background `{colors.primary}`, text `{colors.on-primary}`, label `{typography.button-md}` (Apercu 16 px / 700 / 0.3 px tracking), padding `{spacing.md} {spacing.xl}`, shape `{rounded.none}` 0 px.

**`button-outline`** — the white outline CTA.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, same typography / padding / shape.

**`button-icon-circular`** — the circular share-icon button.
- Background `{colors.canvas}`, ink icon, shape `{rounded.full}`.

### Cards & Containers

**`story-card-large`** — the cover-story card with `{typography.display-md}` headline.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg}`. No border — the card lives on the canvas with the photo doing the work.

**`story-card`** — the secondary story card.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md}`. Photo at top, sans display heading + body lead below.

**`story-row`** — the bylined story list row.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` bottom border, body in `{typography.body-md-strong}`, padding `{spacing.lg}` 0.

### Inputs & Forms

**`text-input`** — the standard text input.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.ink}` border, body in `{typography.body-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.none}`.

### Navigation

**`nav-bar`** — the top nav, light by default.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.xl}`. Layout: hamburger left, masthead centre, Subscribe right.

**`nav-link`** — link items inside nav.
- Text `{colors.ink}`, set in `{typography.body-sm-strong}` (Apercu 14 / 700).

**`footer`** — the black footer band.
- Background `{colors.primary}`, text `{colors.on-primary}`, padding `{spacing.4xl} {spacing.xl}`. Body in `{typography.body-sm}` (Apercu 14 / 400). Footer column eyebrows in `{typography.body-sm-strong}`.

### Signature Components

**`hero-band`** — the white hero band hosting the cover-story.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.4xl} {spacing.xl}`. Cover headline in `{typography.display-hero}` (WiredDisplay 64 px).

**`masthead-band`** — the thin top band with the wordmark.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md} {spacing.xl}`. The wordmark sits centred; flanked by section nav.

**`category-eyebrow`** — the small uppercase category label above story headlines.
- Text `{colors.ink}`, set in `{typography.body-sm-strong}` (Apercu 14 / 700 — though some campaigns use ALL CAPS via CSS).

**`byline-row`** — the article byline strip.
- Background `{colors.canvas}`, text `{colors.body}`, body in `{typography.byline}` (BreveText 12.73 / 700 / line-height 2.2). Includes an author avatar + name + date.

**`hairline-divider`** — the 1 px line between story rows.
- 1 px solid `{colors.hairline}`.

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

State changes on this brand are paint-only — ink, rule and underline swap, nothing
travels and nothing scales. That is the editorial identity, not an omission: a
square black CTA that pops on press would read as a SaaS button. Every row below
uses `{motion.duration-fast}` with `{motion.ease-standard}` unless the Motion &
Animation table says otherwise. The focus ring is `{colors.focus}` in every row
that lists focus-visible: a 2 px ring with a 2 px offset, drawn outside the control.

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.primary}` fill, `{colors.on-primary}` label | fill lifts to `{colors.ink-soft}` | 2 px `{colors.focus}` ring, 2 px offset | label drops to 70% opacity | 40% opacity, no pointer | label replaced by a 3-dot ink pulse, width held | — (not a toggle) | — (form-level, see `text-input`) |
| `button-outline` | 1 px `{colors.ink}` border on `{colors.canvas}` | border thickens to 2 px `{colors.ink}` (Level 2 elevation) | 2 px `{colors.focus}` ring, 2 px offset | fill inverts to `{colors.ink}`, label `{colors.on-primary}` | border and label at 40% opacity | 3-dot ink pulse in place of the label | — (not a toggle) | — |
| `button-icon-circular` | ink glyph on `{colors.canvas}` | glyph to `{colors.ink}`, 1 px `{colors.body}` ring appears | 2 px `{colors.focus}` ring, 2 px offset | glyph at 70% opacity | 40% opacity | glyph swaps to the ink pulse | pressed share state holds the inverted fill | — |
| `text-input` | 1 px `{colors.ink}` border, `{colors.ink}` value | border holds; placeholder to `{colors.ink-soft}` | 2 px `{colors.focus}` ring, 2 px offset, border unchanged | caret only | border and label to `{colors.body}`, surface `{colors.canvas-soft}` | submit button carries the loading state, the field does not | — | 2 px `{colors.ink}` border plus an `{typography.body-sm-strong}` message below; the brand has no error red, so weight and rule carry the signal |
| `nav-link` | `{colors.ink}`, no rule | 1 px `{colors.ink}` underline appears | 2 px `{colors.focus}` ring, 2 px offset | underline holds, label at 70% opacity | 40% opacity | — | current section keeps a persistent 1 px `{colors.ink}` underline | — |
| `story-card-large`, `story-card` | headline `{colors.ink}`, photo at rest | headline gains a 1 px `{colors.ink}` underline; photo opacity to 0.92 | 2 px `{colors.focus}` ring around the whole card, 2 px offset | headline at 70% opacity | — (a card is never disabled) | skeleton: `{colors.canvas-soft}` blocks at the photo and headline boxes, opacity pulse only | — | — |
| `story-row` | `{colors.ink}` title above a `{colors.hairline}` rule | title underlines; row surface to `{colors.canvas-soft}` | 2 px `{colors.focus}` ring, 2 px offset | title at 70% opacity | — | skeleton bars as above | — | — |
| `hairline-divider`, `masthead-band`, `hero-band`, `byline-row`, `category-eyebrow`, `footer` | as specified above | — | — | — | — | — | — | — |
| `ex-app-shell-row` | `{colors.canvas}`, ink label | surface to `{colors.canvas-soft}` | 2 px `{colors.focus}` ring, 2 px offset | label at 70% opacity | 40% opacity | — | 2 px `{colors.primary}` left `activeIndicator`, label `{typography.body-md-strong}` | — |
| `ex-pricing-tier`, `ex-auth-form-card`, `ex-modal-card`, `ex-empty-state-card` | as specified above | — | focus is carried by the controls inside, not the card | — | — | card body swaps to skeleton blocks | `ex-pricing-tier-featured` is the selected variant: `{colors.ink}` fill, `{colors.on-primary}` text | inline message in `{typography.body-sm-strong}` above the submit control |
| `ex-toast` | `{colors.canvas}` surface, 1 px `{colors.ink}` rule | — (non-interactive except its dismiss control) | dismiss control takes the `{colors.focus}` ring | — | — | — | — | the error toast carries a 2 px `{colors.ink}` left rule, not a red fill |

The five band / divider components in the ninth row are presentational: they have
one state each and genuinely no interactive states at all.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** No duration, easing curve or stagger below was
extracted from Wired; the file records none. The values are the SPEC **Calm**
profile verbatim, which suits a composed editorial surface: short opacity-led
fades, almost no travel, no overshoot. Every value is referenced as a
`{motion.*}` token so the numbers live in one place.

Animate `transform` and `opacity` only; never `width`, `height`, `top`, `left`
or `margin`. On a brand with no shadow, no radius and no chromatic accent, most
state changes are paint-only — `color`, `border-color`, `background-color` —
which is permitted and needs no substitute travel. Exit durations are shorter
than their matching entrances.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (link, nav-link, story headline, card) | `{motion.duration-fast}` | `{motion.ease-standard}` | `color`, `border-color`, `opacity` (photo to 0.92) | Unchanged — paint-only, no travel to remove |
| Press (button-primary, button-outline, icon button) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` to 0.7, `background-color` on the outline invert | Unchanged at `{motion.duration-reduced}` |
| Focus (ring appear) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Ring appears instantly, no fade |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` 0 → 1 on the article column; no slide | Cross-fade at `{motion.duration-reduced}` |
| Modal or drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` 0 → 1, `transform: translateY(8px)` → 0 | `opacity` only at `{motion.duration-reduced}`, translate removed |
| Modal or drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` 1 → 0, no travel | `opacity` only at `{motion.duration-reduced}` |
| Dropdown / section menu | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px)` → 0 | `opacity` only at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` 0 → 1, `transform: translateY(8px)` → 0 | `opacity` only at `{motion.duration-reduced}`, translate removed |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` 1 → 0 | `opacity` only at `{motion.duration-reduced}` |
| List enter (story grid, story rows) | `{motion.duration-base}` per item, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity` 0 → 1 only — the magazine grid fades in place, it does not fly in | Stagger dropped, single `opacity` fade at `{motion.duration-reduced}` |
| List exit (filter / search re-query) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | `opacity` only at `{motion.duration-reduced}` |
| Loading (skeleton, button pulse) | `{motion.duration-emphasis}` per cycle, infinite | `{motion.ease-standard}` | `opacity` 1 → 0.5 → 1 on `{colors.canvas-soft}` blocks | Animation frozen; a static `{colors.canvas-soft}` block is shown instead |
| Hero / cover image on first paint | none | none | none — the cover renders at rest | Unchanged |

Nothing animates on first paint in a way that delays content: the hero band and
its headline render at rest, and the list-enter fade applies only to grids
fetched after the first paint. The skeleton pulse is the one infinite animation
in the system; there is no brand ambience.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale — modal, drawer, dropdown and toast
     entrances become pure cross-fades; list stagger is dropped so a grid
     appears in one step. The loader's infinite pulse is frozen to a static
     canvas-soft block. */
  /* Kept: opacity fades and every paint-only change (color, border-color,
     background-color), capped at {motion.duration-reduced} 150ms. The focus
     ring appears with no transition at all. */
}
```

## Accessibility

### Measured contrast

WCAG 2.1 relative luminance, computed from this file's own hexes. Three pairs
fail, and all three are extracted brand facts kept as-is.

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#000000` on `{colors.canvas}` `#ffffff` | 21.00:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` `#f5f5f5` | 19.26:1 | 4.5:1 | Pass |
| `{colors.ink-soft}` `#1a1a1a` on `{colors.canvas}` | 17.40:1 | 4.5:1 | Pass |
| `{colors.on-primary}` `#ffffff` on `{colors.primary}` `#000000` | 21.00:1 | 4.5:1 | Pass |
| `{colors.body}` `#757575` on `{colors.canvas}` | 4.61:1 | 4.5:1 | Pass |
| `{colors.body}` `#757575` on `{colors.canvas-soft}` `#f5f5f5` | 4.23:1 | 4.5:1 | **Fail — the real brand fails AA here.** Grey metadata set on the tinted surface is below AA for normal text. Use `{colors.body}` on `{colors.canvas-soft}` only at 18.66 px/700 or 24 px+, where 3:1 applies; below that size put metadata on `{colors.canvas}`, where it passes. |
| `{colors.hairline}` `#e0e0e0` on `{colors.canvas}` | 1.32:1 | 3.0:1 | **Fail — extracted and frozen.** Decorative rule only. |
| `{colors.hairline}` `#e0e0e0` on `{colors.canvas-soft}` `#f5f5f5` | 1.21:1 | 3.0:1 | **Fail — extracted and frozen.** Decorative rule only. |
| `{colors.link}` `#057dbc` on `{colors.canvas}` | 4.50:1 | 4.5:1 | Pass, by 0.0006 — treat as the floor and never darken the canvas behind an inline link. |
| `{colors.link}` `#057dbc` on `{colors.canvas-soft}` `#f5f5f5` | 4.13:1 | 4.5:1 | **Fail.** Inline links are specified for article body on `{colors.canvas}` only; do not carry them onto the tinted comment surface at body size. |

The `{colors.hairline}` failures are the honest shape of this brand: the 1 px
rule between story rows is a typographic device, not a boundary a reader has to
find. Where a hairline is the *only* boundary of a control or a card —
`text-input`, and the `ex-*` card surfaces — the palette already owns a passing
tone and no new token is needed: `{colors.ink}` (21:1, already bound on
`text-input`) or `{colors.body}` (4.61:1 on `{colors.canvas}`, 4.23:1 on
`{colors.canvas-soft}`, both clearing 3:1). The existing `{colors.hairline}`
bindings on `story-row`, `hairline-divider` and the `ex-*` cards are left exactly
as extracted; re-pointing the `ex-*` card borders to `{colors.body}` is a brand
decision and sits in the audit report under Needs approval.

### Focus ring

`{colors.focus}` is **not a new brand colour**: it reuses `{colors.link}`
`#057dbc`, the one chromatic tone the brand already owns, and it is the only
palette value that clears 3:1 on every surface this file defines. Drawn as a
2 px ring at a 2 px offset *outside* the control, so it is judged against the
surface behind the control rather than the control's own fill — which matters
here, because the brand's primary CTA fill is pure black.

| Ring on surface | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.focus}` on `{colors.canvas}` `#ffffff` | 4.50:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.canvas-soft}` `#f5f5f5` | 4.13:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.primary}` `#000000` (footer band) | 4.67:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.hairline}` `#e0e0e0` | 3.41:1 | 3.0:1 | Pass |

One ring serves both polarities, so this file needs no `focus-on-dark`
counterpart.

### Minimum tap target

`button-primary` and `button-outline` compute to 44 px tall from this file's own
tokens: `{spacing.md}` 12 px top + 12 px bottom + `{typography.button-md}`
20 px line-height. `button-icon-circular` computes to 36 px from `{spacing.sm}`
8 px + 8 px + a 20 px glyph box, which is **below the 44 px target** — it needs
`{spacing.md}` padding, or a 44 px hit area extended past the visible circle.
These are arithmetic from the token values, not measurements of a rendered page;
nothing here was rendered.

### Reduced motion

Every entrance loses its travel and becomes an opacity fade capped at
`{motion.duration-reduced}` 150 ms, list stagger is dropped, and the skeleton
pulse freezes. See the `@media (prefers-reduced-motion: reduce)` rule above.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` black for the wordmark, every CTA, and the footer fill. The brand IS the strict black-on-white duet.
- Set hero headlines in `{typography.display-hero}` (WiredDisplay 64 px weight 400). The proprietary serif IS the brand's typographic signature.
- Use `{rounded.none}` 0 px on every button and form input. The brand reads as a printed magazine — square corners are non-negotiable.
- Pair WiredDisplay (serif display) with BreveText (serif body) and Apercu (sans labels). Three faces, three roles.
- Render story rows with `{colors.hairline}` 1 px dividers — the brand's only elevation cue.

### Don't
- Don't introduce a chromatic brand accent. The link blue is reserved for inline body links inside articles only.
- Don't round button corners. The brand never softens its rectangular geometry.
- Don't drop a soft drop-shadow on cards. Surface contrast and hairlines carry elevation.
- Don't substitute the proprietary serif faces with a generic sans for display. The serif voice is the brand.
- Don't promote display weight beyond 400. The brand's elegance is in the typeface design, not bold weight.
- Don't add a scale pop or a slide to a state change. Hover, press and selection are paint-only on this brand; travel belongs to modals, dropdowns and toasts, and nowhere else.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Cover hero 64→40 px; all grids 1-up; hamburger nav. |
| Tablet | 768–1023px | 2-up secondary story grid. |
| Desktop | ≥ 1024px | Full magazine grid. |

### Touch Targets
Button-primary renders ~44 px tall (12 vertical padding + 20 line). WCAG AAA at all widths.

### Collapsing Strategy
- Nav: full link row + Subscribe CTA at desktop. Hamburger at mobile.
- Magazine grid: hero stays full-width; 2-up secondary drops to 1-up at mobile.
- Story rows: stay single-column at all viewports.

### Image Behavior
- Cover images: full-bleed 16:9 hero / 4:3 secondary.
- Article body images: full-width inside the article column.
- Author avatars: small inline circular crops next to bylines.

## Known Gaps

- **All motion is prescribed, none extracted.** No duration, easing curve,
  stagger or reduced-motion rule in this file was measured from the live site;
  the source records none. The values are the SPEC Calm profile verbatim.
  Anything in Motion & Animation is a proposal, not a brand fact.
- **The component state matrix is prescribed.** Only one state was documented
  in the source material — the `ex-app-shell-row` active indicator. Every other
  cell in the Component States table is inferred from the brand's own rules
  (paint-only change, square geometry, no shadow, no chromatic accent) and
  needs confirmation against the live site.
- **`{colors.focus}` is prescribed.** No focus ring was extracted. The token
  reuses the existing `{colors.link}` `#057dbc` rather than introducing a
  colour, and the 2 px width and 2 px offset are proposals.
- **No error, success or warning tone exists in the palette.** This is a real
  absence, not a naming miss: the brand carries one ink per polarity plus a
  single inline link blue, and validation on the live forms is carried by
  weight and rule rather than colour. No semantic tone has been invented to
  fill the column.
- **No `shadow:` group.** Correct for this brand — Elevation & Depth documents
  no shadow value at all, only flat, hairline and 2 px ink border. The two
  `ex-*` descriptions that mention an "elevated shadow" and a "medium shadow"
  are auto-derived boilerplate from the example generator and contradict the
  brand's own Don't; they describe no value in this file and reference no token.
- **Nothing in this document was rendered.** Tap-target sizes, including the
  44 px figure under Touch Targets and the 36 px figure for
  `button-icon-circular`, are arithmetic from the token values. Overlap,
  overflow, clipping, frame rate and layout shift were not and cannot be
  checked from a document.
- **Line-height 2.2 on `{typography.byline}`** is stated in the Typography
  principles as an editorial signature; the token itself records 12.73 px /
  28 px, which is 2.2. Consistent, but the 12.73 px size is an odd extracted
  value and may be a computed rather than an authored one.
