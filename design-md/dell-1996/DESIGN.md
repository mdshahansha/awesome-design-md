---
version: alpha
name: Dell 1996 Inspired
description: An inspired interpretation of Dell.com's 1996 design language — a catalog-era enterprise web design built around a literal black page frame, vivid flat color-block "ribbon cards" tinted in sage, salmon, periwinkle, sky, peach and lime, chunky Helvetica-Black display titles, Times Roman body copy, and an entire visual vocabulary of pre-Photoshop hand-cut GIF stickers (NEW! bursts, award seals, beveled product photos).

colors:
  primary: "#e91d2a"
  on-primary: "#ffffff"
  canvas: "#ffffff"
  surface: "#ffffff"
  ink: "#000000"
  frame-ink: "#000000"
  yellow-sticker: "#fcc20f"
  purple-stripe: "#6a26a4"
  link: "#0000ee"
  hairline: "#000000"          # extracted: every 1px rule on the page is frame-ink black
  text-muted: "#666666"        # PRESCRIBED, not extracted — see Accessibility
  focus: "#000000"             # PRESCRIBED — 2px black ring for light surfaces
  focus-on-dark: "#ffffff"     # PRESCRIBED — white ring on the black frame/banner/button-primary

  # Ribbon-card tint family (one per product line)
  tint-olive: "#8e8a25"
  tint-sage: "#b3bd95"
  tint-salmon: "#d77a7a"
  tint-peach: "#e6915d"
  tint-lime: "#c0d4a7"
  tint-sky: "#9ab6c8"
  tint-steel: "#a5b8c0"
  tint-periwinkle: "#8c9ae0"

typography:
  display:
    fontFamily: Arial Black
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: 0
  heading-1:
    fontFamily: Arial Black
    fontSize: 24px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: 0
  heading-2:
    fontFamily: Helvetica
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  heading-3:
    fontFamily: Helvetica
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  body:
    fontFamily: Times New Roman
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-sm:
    fontFamily: Times New Roman
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: Times New Roman
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button:
    fontFamily: Helvetica
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  link:
    fontFamily: Times New Roman
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  ui-label:
    fontFamily: Helvetica
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0

rounded:
  none: 0px
  full: 9999px

shadow:
  none: none
  bevel: "2px 2px 0 #000000"
  bevel-inset: "inset 1px 1px 0 #ffffff, inset -1px -1px 0 #000000"

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

focus-ring:
  width: 2px
  style: solid
  offset: 1px
  color: "{colors.focus}"
  color-on-dark: "{colors.focus-on-dark}"

spacing:
  xxs: 2px
  xs: 4px
  s: 6px
  sm: 8px
  m: 10px
  md: 12px
  lg: 16px
  xl: 20px
  xxl: 24px
  section-sm: 32px
  section: 40px
  section-lg: 48px

components:
  # ─── Brand-native components ───
  page-frame:
    backgroundColor: "{colors.frame-ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    padding: 8px

  top-banner:
    backgroundColor: "{colors.frame-ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.heading-2}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  section-eyebrow-olive:
    backgroundColor: "{colors.tint-olive}"
    textColor: "{colors.ink}"
    typography: "{typography.display}"
    rounded: "{rounded.none}"
    padding: 24px 16px

  section-eyebrow-salmon:
    backgroundColor: "{colors.tint-salmon}"
    textColor: "{colors.ink}"
    typography: "{typography.display}"
    rounded: "{rounded.none}"
    padding: 24px 16px

  ribbon-card-title:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.heading-3}"
    rounded: "{rounded.none}"
    padding: 6px 12px

  ribbon-card-body-sage:
    backgroundColor: "{colors.tint-sage}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  ribbon-card-body-salmon:
    backgroundColor: "{colors.tint-salmon}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  ribbon-card-body-peach:
    backgroundColor: "{colors.tint-peach}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  ribbon-card-body-lime:
    backgroundColor: "{colors.tint-lime}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  ribbon-card-body-sky:
    backgroundColor: "{colors.tint-sky}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  ribbon-card-body-steel:
    backgroundColor: "{colors.tint-steel}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  ribbon-card-body-periwinkle:
    backgroundColor: "{colors.tint-periwinkle}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  cta-block-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 16px

  phone-callout:
    backgroundColor: "{colors.frame-ink}"
    textColor: "{colors.primary}"
    typography: "{typography.heading-2}"
    rounded: "{rounded.none}"
    padding: 4px 8px

  buy-a-dell-sticker:
    backgroundColor: "{colors.yellow-sticker}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 4px 8px

  new-burst-sticker:
    backgroundColor: "{colors.yellow-sticker}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 4px 8px

  cert-seal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    size: 64px

  icon-label-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.none}"
    padding: 8px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 4px 6px

  button-primary:
    backgroundColor: "{colors.frame-ink}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 6px 16px

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 6px 16px

  button-text-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"

  footer-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
    typography: "{typography.body-sm}"
    padding: 16px

  # ─── Examples (illustrative, kit-mirror) — injected by derive-examples-block.mjs ───

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with the base white surface."
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.frame-ink}"
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
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    item-divider: "{colors.frame-ink}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.surface}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.s} {spacing.md}"
    rowBorder: "{colors.frame-ink}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card, elevated with a hard {shadow.bevel} offset, never a soft shadow."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    captionTypography: "{typography.body}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + hard {shadow.bevel} offset."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Dell's December 1996 home page is a perfectly preserved fossil of catalog-era enterprise web design — the moment when a Fortune-100 brand decided the web was *important enough* to invest in, but two years before CSS would be widely adopted and three years before "design system" was a phrase anyone used. Every visual choice on the page is a downstream consequence of that constraint: layout via HTML tables, type via the browser's built-in font stack (Arial Black / Helvetica / Times Roman), color via 8-bit-safe flat fills, and decoration via hand-cut GIF "stickers" (the NEW! burst, the round PC Magazine Readers' Choice seal, the beveled "BUY a DELL" yellow tab). The page is bordered — literally bordered, in a 1-cell-wide black HTML table — and inside that frame, every product line gets a "ribbon card": a white title bar with a sharp black underline, a tinted body block in one of eight catalog colors (sage, salmon, peach, lime, sky, steel, periwinkle, olive), and a beveled product photograph notched into the right edge of the card.

The brand voice carries through in two anchors: a vivid Dell-red CTA panel on the left of the homepage (cream-yellow Times Roman copy on a `{colors.primary}` fill, set inside the black frame) and a screaming red phone number — `1-800-213-DELL` — pinned to the top-right of every page, because in 1996 the website was a brochure that ended with a phone call. The footer is a row of four hand-drawn icon-labels (FIND / HOME / ONLINE STORE / SERVICE & SUPPORT) linked by a thin green horizontal rule, and a single classic-Mosaic-blue underlined "Copyright" link sitting above the legal small print in Times Roman.

**Key Characteristics:**
- Literal page frame: every page sits inside a `{colors.frame-ink}` (black) outer border ~8 px thick — the design treats the browser window as a printed picture frame
- Flat color-block "ribbon cards" tint each product family with a dedicated catalog color (`{colors.tint-sage}` Latitude, `{colors.tint-salmon}` OptiPlex GX, `{colors.tint-periwinkle}` PowerEdge, `{colors.tint-sky}` Dellware, etc.) — no gradients, no shadows, no opacity
- Chunky display typography in `{typography.display}` (Arial Black 36 / weight 900) for section title blocks; `{typography.heading-2}` (Helvetica Bold 16) for product row titles; `{typography.body}` Times Roman 14 for everything else
- Hand-cut GIF "stickers" overlay the layout: yellow "BUY a DELL" tab in the top right, angled "NEW!" bursts on new product rows, round red PC Magazine Readers' Choice seals
- `{colors.primary}` (Dell red) reserved for two things only: the homepage CTA panel and the top-right phone number — never decorative
- Footer icon-nav with classic-blue (`{colors.link}` #0000ee) anchor underlines — the unmistakable Netscape 3.x link colour

## Colors

### Brand & Accent
- **Dell Red** (`{colors.primary}` — #e91d2a): The brand's signature red. Reserved for the homepage CTA panel ("At Dell.com, we'll help you find the right system…"), the top-right phone number, and the PC Magazine Readers' Choice seal ring. Never used as a card body fill.
- **Dell Yellow** (`{colors.yellow-sticker}` — #fcc20f): Sticker yellow — the "BUY a DELL" tab in the top banner, and the angled "NEW!" bursts overlapping new product rows.
- **Dell Purple** (`{colors.purple-stripe}` — #6a26a4): The accent stripe behind the lowercase ".com" / "DELL" wordmark text — appears inside the "BUY a DELL" sticker chrome only.

### Surface
- **Frame Ink** (`{colors.frame-ink}` — #000000): Pure black. The page frame, the top banner background, button fills, and all 1 px ribbon-card hairlines.
- **Canvas** (`{colors.canvas}` — #ffffff): True white inside the frame. The page surface, the ribbon-card title-bar fill, and the icon-label nav backdrop.

### Text
- **Ink** (`{colors.ink}` — #000000): Body text, headings, link copy before visit. Pure black; no warm-near-black softening in 1996.
- **Link** (`{colors.link}` — #0000ee): Classic Mosaic / Netscape 3.x default link blue. Underlined inline anchors ("Copyright", "(Terms of Use)", inline "from Dell's award-winning service and support teams").

### Boundary, Muted & Focus
- **Hairline** (`{colors.hairline}` — #000000): Extracted. Every rule on the page — ribbon-card edge, table-cell divider, footer top border, input border — is the same pure black as the frame. There is no soft grey divider anywhere in the 1996 design, so `{colors.hairline}` and `{colors.frame-ink}` are the same value by design, not by omission. 21:1 on `{colors.canvas}`.
- **Muted text** (`{colors.text-muted}` — #666666): **PRESCRIBED, not extracted.** The 1996 page has no secondary ink: body, caption and legal small print are all pure `{colors.ink}` black, and hierarchy is carried by size and family instead of by tone. #666666 is supplied for modern reproductions that need a muted caption tone; it is a web-safe 8-bit-palette value, so it is at least period-plausible. Use it only for `{typography.caption}` legal print; never for body copy. 5.74:1 on `{colors.canvas}`.
- **Focus ring** (`{colors.focus}` — #000000 / `{colors.focus-on-dark}` — #ffffff): **PRESCRIBED, not extracted.** 1996 browsers drew their own dotted focus outline and the design never specified one. This brand has no chromatic UI accent to borrow — Dell red is reserved, the catalog tints are surfaces, and the link blue fails against both the red panel and the tints — so the ring follows the SPEC's monochrome rule: the brand's own ink, with a mandatory opposite-polarity ring on dark chrome. `{colors.focus}` measures 21:1 on `{colors.canvas}`, 4.67:1 on `{colors.primary}` and 5.81:1 on the lowest-contrast tint (`{colors.tint-olive}`). `{colors.focus-on-dark}` measures 21:1 on `{colors.frame-ink}`. Full table in Accessibility.

### Ribbon-Card Tint Family
Eight catalog colors, one per product line — these are the page's chromatic personality:
- **Olive** (`{colors.tint-olive}` — #8e8a25): "DIMENSION DESKTOPS" eyebrow block
- **Sage** (`{colors.tint-sage}` — #b3bd95): Latitude Notebooks ribbon body
- **Salmon** (`{colors.tint-salmon}` — #d77a7a): "OPTIPLEX DESKTOP SYSTEMS" eyebrow + GX Series body
- **Peach** (`{colors.tint-peach}` — #e6915d): Dimension card body + OptiPlex Gs body
- **Lime** (`{colors.tint-lime}` — #c0d4a7): OptiPlex G Series body
- **Sky** (`{colors.tint-sky}` — #9ab6c8): Dellware ribbon body
- **Steel** (`{colors.tint-steel}` — #a5b8c0): Dimension XPS Pro ribbon body
- **Periwinkle** (`{colors.tint-periwinkle}` — #8c9ae0): PowerEdge ribbon body

The tints are saturated but not vivid — they sit just below true neutral chroma, the signature of GIF-era web-safe-palette quantization.

## Typography

### Font Family

Three system-stack families, no webfonts (webfonts didn't exist yet):

- **Arial Black** (fallback: Helvetica, system-ui sans) — display headings only. The chunky stenciled section eyebrows ("DIMENSION DESKTOPS", "OPTIPLEX DESKTOP SYSTEMS") are Arial Black at weight 900, set in all-caps with normal tracking.
- **Helvetica** (fallback: Arial, system-ui sans) — product-row titles, button labels, the top banner's "BUILD YOUR OWN COMPUTER. ONLINE." headline. Always bold (700), always all-caps.
- **Times New Roman** (fallback: Times, serif) — body copy. Every paragraph, every caption, every inline anchor sits in default-rendered Times Roman. The serifs date the design instantly — body text on the modern web is almost never serif.

### Hierarchy

| Token | Size | Weight | Line Height | Use |
|---|---|---|---|---|
| `{typography.display}` | 36px | 900 | 1.0 | Section eyebrow titles ("DIMENSION DESKTOPS", "OPTIPLEX DESKTOP SYSTEMS") |
| `{typography.heading-1}` | 24px | 900 | 1.05 | Sub-page hero headlines |
| `{typography.heading-2}` | 16px | 700 | 1.2 | Top banner copy, product-line H1 ("Reliable PC's for High-Performance Computing.") |
| `{typography.heading-3}` | 14px | 700 | 1.2 | Ribbon-card title bar ("OPTIPLEX GX PRO", "DIMENSION XPS") |
| `{typography.body}` | 14px | 400 | 1.4 | Default paragraph copy, ribbon-card body, CTA-panel copy |
| `{typography.body-sm}` | 12px | 400 | 1.4 | "This site is best viewed with browser versions 3.0 and higher." |
| `{typography.caption}` | 11px | 400 | 1.35 | Footer copyright text |
| `{typography.button}` | 12px | 700 | 1.0 | Button labels, "NEW!" sticker, BUY-a-DELL sticker |
| `{typography.ui-label}` | 12px | 700 | 1.0 | Icon-label nav uppercase labels ("FIND", "HOME", "ONLINE STORE", "SERVICE & SUPPORT") |

### Principles
- Sans for UI, serif for body — the inverse of the modern convention, and a dead giveaway of mid-90s typography.
- Display weights are extreme (900 / Black) and never softer. The "Dimension" / "OptiPlex" eyebrow blocks lean on the heaviest weight the font ships.
- No letter-spacing tracking adjustments — pixel-fonts in 1996 didn't reward it. Everything is set at the browser's default kern.
- Line-height is tight on display (1.0) and conventional on body (1.4) — a holdover from print-magazine catalog layout.

### Note on Font Substitutes
All three families are operating-system defaults on every consumer OS shipped in 1996 (Windows 95: Arial / Times New Roman; Mac OS 7.5+: Helvetica / Times). The brand had no fallback strategy because no fallback was needed — the fonts were always present. Modern reproductions can stay on this exact stack (Arial Black / Helvetica / Times New Roman) for authenticity.

## Layout

### Spacing System

- **Base unit**: 4 px (with 2 / 6 / 10 intermediates). 1996 page layout was driven by HTML table cell padding (`cellpadding="4"` / `cellspacing="0"`) rather than a designed scale.
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.s}` 6px · `{spacing.sm}` 8px · `{spacing.m}` 10px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 20px · `{spacing.xxl}` 24px · `{spacing.section-sm}` 32px · `{spacing.section}` 40px · `{spacing.section-lg}` 48px.
- **Card interior padding**: `{spacing.md}` 12 px vertical / `{spacing.lg}` 16 px horizontal on ribbon-card bodies.
- **Section vertical rhythm**: `{spacing.section}` 40 px between product-ribbon stacks; `{spacing.section-sm}` 32 px between the eyebrow color block and its first ribbon-card.

### Grid & Container
- Fixed-width table layout pinned around 760 px wide — the de facto 1996 standard targeting 800×600 monitors with a small scrollbar gutter.
- Two-column outer structure: left rail (~28 %) carries the homepage icon-link grid + CTA red panel; right column (~72 %) carries the product ribbon stack.
- No grid system in the modern sense — every section is its own `<table>` declaration with hard-coded column widths.

### Whitespace Philosophy
Tight by modern standards. Catalog density wins over editorial breath — every pixel inside the black frame is doing work (illustration, color block, headline, body). The compensating decompression happens *inside* each ribbon card: white title bar + tinted body block + product photo notch creates internal breathing room without enlarging the overall page.

## Responsive Behavior

#### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Period default | 800 × 600 | Fixed 760 px layout, designed for the era's standard monitor |
| Modern desktop | 1280+ px | Layout sits centered with generous side gutters — emulates "magazine spread in the middle of the screen" |
| Tablet | 768 px | Black frame compresses to 4 px; ribbon-cards stack at full width inside |
| Mobile | < 480 px | Black frame to 2 px; two-column structure collapses to single column; left rail icon grid stacks above the right-column product stack |

#### Touch Targets
1996 had no notion of touch — the original designs assume mouse-only. Modern reproductions need to widen the icon-label nav targets to 44 × 44 px minimum at mobile (the 1996 icons sat at ~24 × 24 with 8 px label below, well under modern guidelines).

#### Collapsing Strategy
- At ≤ 768 px, the homepage's left-rail icon-link grid (Online Store / Service / Why Dell? / Government / Worldwide / Order Status / Company Info / U.S. Careers) collapses from a 2 × 4 grid to a single-column stack
- Ribbon-card right-edge product photo notch becomes a top-aligned full-width image at mobile
- The top banner's tagline ("BUILD YOUR OWN COMPUTER. ONLINE.") shrinks one type tier; the phone number wraps below the BUY-a-DELL sticker
- Footer icon-label nav stays 4-up at all widths — the icons are small enough to survive

#### Image Behavior
Product photos are bitmap GIFs with hand-applied bevel shadows — they were authored at fixed pixel widths (typically 80–120 px wide). The right-edge notch effect was achieved by table-cell negative spacing. Modern reproductions should keep the bevel shadow effect (it's signature) but use SVG drop-shadow or CSS `filter: drop-shadow(2px 2px 0 #000)` to recreate it crisply at high-DPI.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flush | `{shadow.none}` — no shadow, no border | Body text, copyright row, footer band background |
| 1 — Hairline | `1px solid {colors.hairline}` | Ribbon-card outer edge, table-cell dividers |
| 2 — Frame | `8px solid {colors.frame-ink}` | The page-frame border around the entire viewport |
| 3 — Bevel | `{shadow.bevel-inset}` (hard 1 px highlight + 1 px shadow) plus `{shadow.bevel}` offset | "BUY a DELL" yellow sticker, NEW! bursts, award seals, product photographs |

Elevation is expressed **one way only**: border weight. Levels 0–2 are a single ladder of black stroke widths (0 → 1 px → 8 px); level 3 is the same hard-edge idea baked into a GIF, offset by `{shadow.bevel}` (2 px, zero blur) rather than blurred. No level mixes a shadow with a border, and no level uses opacity.

`{colors.canvas}` and `{colors.surface}` are both #ffffff — 1.0:1, deliberately indistinguishable. In this design a "card" is not a lighter plane floating above the page; it is the same white paper with a black rule drawn around it. Any reproduction that tints the surface to separate the layers has left the brand.

There are **no soft shadows** in the 1996 design — every depth cue is either a hard 1 px border or a hand-painted bevel inside a GIF. Modern reproductions that need to feel period-accurate must resist the urge to add Material-style elevation or atmospheric drop shadows.

### Decorative Depth
Bevels and frames carry the entire depth vocabulary:
- The **page frame** is the strongest depth cue — it tells the viewer "this is a contained document, not a continuous canvas."
- **Bevels on stickers** (BUY a DELL, NEW!, PC Magazine Readers' Choice) push them forward off the page surface as if pinned on with thumbtacks.
- **Product photographs** carry their own hand-painted bevel + drop-shadow, baked into the GIF itself.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Universal default — buttons, cards, inputs, banners, page frame, ribbon-card bodies, eyebrow blocks |
| `{rounded.full}` | 9999px | Circular award seals (PC Magazine Readers' Choice), the round "h" sticker on the HOME icon |

The 1996 design has effectively **two** radius modes: square (everything) and round (decorative seal stickers). No 4 / 8 / 12 px subtle radius tier — that vocabulary belongs to the post-Bootstrap web.

### Photography Geometry
Product photos are rectangular GIFs with their own internal beveled "monitor" framing — they sit at native pixel dimensions, never scaled. Aspect ratios cluster around 4:3 (the era's standard CRT shape). Avatars don't exist on this site — staff photography was reserved for "About Dell" pages not captured in these snapshots.

## Components

> **State note.** The 1996 page had no interaction states to extract: HTML 3.2 offered `A:link / A:visited / A:active` and the browser's own button depress, nothing else. The matrix below is therefore **prescribed, not extracted** — it says which states each component needs in a modern reproduction, and which components genuinely have only one. Visuals stay inside the brand's vocabulary: black stroke weight, polarity flip, and the `{focus-ring.width}` `{colors.focus}` ring. No new hue is introduced for any state.

### State Matrix

Legend: ● supported · ○ not applicable · state visuals are listed under the table.

| Component | default | hover | focus-visible | pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `page-frame` | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| `top-banner` | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| `section-eyebrow-olive` / `-salmon` | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| `ribbon-card-title` | ● | ● | ● | ● | ○ | ○ | ● | ○ |
| `ribbon-card-body-<tint>` (all 7) | ● | ● | ● | ● | ○ | ○ | ● | ○ |
| `cta-block-red` | ● | ● | ● | ● | ○ | ○ | ○ | ○ |
| `phone-callout` | ● | ● | ● | ● | ○ | ○ | ○ | ○ |
| `buy-a-dell-sticker` | ● | ● | ● | ● | ○ | ○ | ○ | ○ |
| `new-burst-sticker` | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| `cert-seal` | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| `icon-label-nav` | ● | ● | ● | ● | ○ | ○ | ● | ○ |
| `text-input` | ● | ● | ● | ○ | ● | ○ | ○ | ● |
| `button-primary` | ● | ● | ● | ● | ● | ● | ○ | ○ |
| `button-secondary` | ● | ● | ● | ● | ● | ● | ○ | ○ |
| `button-text-link` | ● | ● | ● | ● | ● | ○ | ○ | ○ |
| `footer-band` | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| `ex-pricing-tier` / `-featured` | ● | ● | ● | ● | ○ | ○ | ● | ○ |
| `ex-product-selector` | ● | ● | ● | ● | ○ | ○ | ● | ○ |
| `ex-cart-drawer` | ● | ○ | ● | ○ | ○ | ● | ○ | ● |
| `ex-app-shell-row` | ● | ● | ● | ● | ● | ○ | ● | ○ |
| `ex-data-table-cell` | ● | ● | ● | ○ | ○ | ● | ● | ● |
| `ex-auth-form-card` | ● | ○ | ● | ○ | ○ | ● | ○ | ● |
| `ex-modal-card` | ● | ○ | ● | ○ | ○ | ○ | ○ | ○ |
| `ex-empty-state-card` | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| `ex-toast` | ● | ○ | ● | ○ | ○ | ○ | ○ | ● |

State visuals, used identically everywhere:

- **hover** — underline appears (anchors) or the 1 px `{colors.hairline}` border thickens to 2 px. No fill change, no lift, no hue.
- **focus-visible** — `{focus-ring.width}` (2 px) solid `{colors.focus}` ring at `{focus-ring.offset}` 1 px outside the element; on `{colors.frame-ink}` chrome (`top-banner`, `button-primary`, `phone-callout`, `page-frame`) the ring switches to `{colors.focus-on-dark}`.
- **pressed** — polarity flip: `button-primary` inverts to `{colors.canvas}` fill / `{colors.ink}` label; `button-secondary` inverts to black fill / white label. This is the era's own button-depress idiom, not a scale pop.
- **disabled** — label and border drop to `{colors.text-muted}`, fill stays `{colors.canvas}`, cursor `not-allowed`. Exempt from the 4.5:1 threshold per WCAG.
- **loading** — label replaced by a 3-glyph Times Roman ellipsis cycling at `{motion.duration-slow}`; the only moving thing on the page, and the nearest honest analogue to the era's animated-GIF "working" badge.
- **selected** — the active product family's `ribbon-card-title` gains a 2 px `{colors.hairline}` left edge; `ex-app-shell-row` uses `{colors.primary}` as a 3 px left indicator. No fill tint, since the fill already encodes the product line.
- **error** — 1 px border becomes 2 px `{colors.primary}`, with the message in `{typography.body-sm}` `{colors.primary}` beneath the field. Dell red is permitted here as a system signal; it does **not** count against the one-CTA-per-page rule.

### Frame & Banner

**`page-frame`** — the literal black border around the entire viewport.
- Background `{colors.frame-ink}`, padding `{spacing.sm}` 8 px on every side, no radius.
- The page sits *inside* this border. Treat it as a non-negotiable container chrome; collapsing it on mobile is acceptable (to ~4 px), but removing it entirely loses the brand.

**`top-banner`** — pure-black strip running across the top with white "BUILD YOUR OWN COMPUTER. ONLINE." headline + sub-tagline, the yellow "BUY a DELL" sticker pinned at right, and the red "1-800-213-DELL" phone number.
- Background `{colors.frame-ink}`, text `{colors.canvas}`, type `{typography.heading-2}`, padding 12 px vertical / 16 px horizontal, no radius.

### Section Eyebrow Blocks

**`section-eyebrow-olive`** — large tinted color block holding the chunky stenciled section title ("DIMENSION DESKTOPS"). Used at the top of the Dimension product page.
- Background `{colors.tint-olive}`, text `{colors.ink}`, type `{typography.display}` (Arial Black 36 / 900), padding 24 × 16, no radius.

**`section-eyebrow-salmon`** — same chrome with the OptiPlex line's salmon-pink fill ("OPTIPLEX DESKTOP SYSTEMS").
- Background `{colors.tint-salmon}`, otherwise identical to the olive variant.

### Ribbon Cards

The brand's signature component. Each product-row "card" is a stack of three pieces:
1. **`ribbon-card-title`** — white horizontal title bar with the product variant name in Helvetica Bold all-caps (e.g. "OPTIPLEX GX PRO", "DIMENSION XPS", "POWEREDGE SERVERS"). 1 px bottom border in `{colors.frame-ink}`.
   - Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.heading-3}`, padding 6 × 12, no radius.
2. **`ribbon-card-body-<tint>`** — color-block body in one of eight tints, holding the short marketing pitch in `{typography.body}` (Times Roman 14). Padding 12 × 16. The product photograph notches into the right edge with a transparent GIF cutout.
3. **Photo notch** — the GIF sits in the rightmost ~25 % of the row, hanging slightly above and below the body bar like a card pinned to a corkboard.

Each tint variant is its own component entry. Pick the one that matches the product family:

- **`ribbon-card-body-sage`** — `{colors.tint-sage}` fill, used for Latitude Notebooks rows
- **`ribbon-card-body-salmon`** — `{colors.tint-salmon}` fill, used for OptiPlex GX Series rows
- **`ribbon-card-body-peach`** — `{colors.tint-peach}` fill, used for Dimension rows and OptiPlex Gs
- **`ribbon-card-body-lime`** — `{colors.tint-lime}` fill, used for OptiPlex G Series rows
- **`ribbon-card-body-sky`** — `{colors.tint-sky}` fill, used for Dellware rows
- **`ribbon-card-body-steel`** — `{colors.tint-steel}` fill, used for Dimension XPS Pro rows
- **`ribbon-card-body-periwinkle`** — `{colors.tint-periwinkle}` fill, used for PowerEdge Server rows

All seven share identical chrome: 1 px solid `{colors.frame-ink}` border, `{spacing.md}` × `{spacing.lg}` (12 × 16) padding, `{rounded.none}` (sharp corners), `{typography.body}` Times Roman 14 inside. Only the fill color changes per product family.

### Call-to-Action

**`cta-block-red`** — the homepage's vivid Dell-red panel ("At Dell.com, we'll help you find the right system, configure it, price it, and order it…").
- Background `{colors.primary}`, text `{colors.on-primary}` (white), 1 px solid frame-ink border, type `{typography.body}` (Times Roman 14), padding 16 px, no radius.
- One per page maximum. The brand's most aggressive attention-grab — never use it for anything except a top-tier sales message.

**`phone-callout`** — top-right phone number ("1-800-213-DELL") rendered as red on the black banner.
- Background `{colors.frame-ink}`, text `{colors.primary}`, type `{typography.heading-2}` Helvetica Bold 16, padding 4 × 8, no radius. Pinned to the right of the top banner on every page.

### Stickers (GIF-style overlays)

**`buy-a-dell-sticker`** — yellow rectangular sticker with "BUY a DELL" in Helvetica Bold, the "a" set in a small purple stripe, the "DELL" wordmark in black. Pinned to the top-right of every page.
- Background `{colors.yellow-sticker}`, text `{colors.ink}`, 1 px black border, type `{typography.button}`, padding 4 × 8, no radius.

**`new-burst-sticker`** — angled yellow burst with "NEW!" in Helvetica Bold black, overlapping the right side of new product ribbon-cards. Slight rotation (~15°) gives it the pinned-on-with-tape feel.
- Background `{colors.yellow-sticker}`, text `{colors.ink}`, type `{typography.button}`, padding 4 × 8, no radius (rotation applied separately).

**`cert-seal`** — round red award seal: center reads "PC MAGAZINE", ringed by "SERVICE · RELIABILITY · READERS' CHOICE", with an inner white field and red bordered ring. Sits on the right rail of product pages.
- Background `{colors.primary}`, text `{colors.canvas}`, type `{typography.button}`, rounded `{rounded.full}`, 64 px size.

### Navigation

**`icon-label-nav`** — bottom-of-page navigation row: four hand-drawn icons (eyeglasses-FIND / house-HOME / yellow-sticker-ONLINE STORE / wrench-SERVICE & SUPPORT) connected by a thin green horizontal rule, each with an uppercase Helvetica label beneath.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.ui-label}`, padding 8 px around each icon-label pair, no radius.
- The connecting green rule is part of the GIF imagery, not a CSS border.

### Inputs & Buttons

**`text-input`** — bordered HTML input. White fill, 1 px solid black border, Times Roman 14 inside.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid frame-ink, type `{typography.body}`, padding 4 × 6, no radius.
- Used on the Search and "Configure & Buy" forms (not visible in these three captures but consistent with the era's HTML 3.2 form widgets).

**`button-primary`** — black filled button with white Helvetica Bold uppercase label.
- Background `{colors.frame-ink}`, text `{colors.on-primary}`, 1 px solid frame-ink, type `{typography.button}`, padding 6 × 16, no radius.

**`button-secondary`** — white filled outlined button. Same chrome with inverted colours.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid frame-ink, type `{typography.button}`, padding 6 × 16, no radius.

**`button-text-link`** — bare underlined anchor in classic-Mosaic blue.
- Text `{colors.link}` #0000ee, type `{typography.link}` Times Roman 14, underline on default. No padding, no radius.

### Footer

**`footer-band`** — the bottom of every page: icon-label nav row, classic-blue Copyright link, "(Terms of Use)" parenthetical, browser-compatibility small print, and the Microsoft BackOffice / Internet Explorer logo banners.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px top border in frame-ink, type `{typography.body-sm}`, padding 16 px.

### Examples (illustrative)

> Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`). Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently. `TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with the base white surface.
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

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** It cannot have been: the captured pages predate CSS transitions, `requestAnimationFrame` and every scripted easing curve on the modern web. In December 1996 the only moving pixels on Dell.com were animated GIFs and the browser's own repaint, and the only "transition" between two states was a full page load over a 28.8k modem. So nothing below is an extracted fact — it is an interpretation, written to the question *"if this catalog page had a motion vocabulary, what would be consistent with it?"* rather than *"what does a 2020s product do here?"*.

Judged against the era's design language, that answer is: **almost nothing should move.** The page's whole argument is that it is a printed object — a bordered picture frame, flat 8-bit colour blocks, hand-cut paper stickers pinned on top. Print does not ease. So the assigned **Calm** profile is applied here as a *ceiling rather than a target*:

- **Opacity only, wherever opacity will do.** Travel is capped at 2 px and scale is never used. Calm's "short opacity-led fades, little travel" is read literally: a card does not slide in, it simply becomes present.
- **Interaction feedback runs at `{motion.duration-instant}` (80ms), not `{motion.duration-base}`.** A 1996 button state change was a discrete repaint with no interpolation; 80ms is the shortest token the profile owns and reads as instant while still being a transition.
- **No entrance choreography on the ribbon-card stack beyond a single `{motion.stagger-step}` fade.** The catalog grid is meant to be read as one printed spread, not revealed row by row.
- **Nothing eases on first paint.** The frame, banner and ribbon stack render at full opacity; a brochure does not fade up.

Calm is also the right assignment under SPEC section 5's rules, and I kept it. Rule 1 does not apply — Dell in 1996 sold commodity beige boxes on price and a phone number, and the file contains no full-bleed photography, no sparse type and no slow reveal; a Cinematic reading would be a 2010s premium-hardware idea imposed on a catalog. Rule 2 does not apply: this is enterprise retail, not a developer tool — though it is the near miss, since Crisp's "state change reads as instant; no entrance choreography" describes 1996 exactly. That is why interaction feedback here sits at the profile's instant token: Calm's token block, read at its fastest end, lands on the same behaviour Crisp would have prescribed, while keeping this file comparable with every other Calm sibling. Rule 3 does not apply despite eight saturated tints, because the tints are static card fills behind product copy, never interactive elements, and the type voice (Arial Black / Times Roman) is anything but informal. So rule 4: **Calm**.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, anchors, ribbon-card rows) | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` on the underline/2 px border overlay | Unchanged — already 80ms, opacity only, no travel |
| Press / active (`button-primary`, `button-secondary`) | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` cross-fade of the polarity-flipped fill | Unchanged — polarity flip is not travel or scale |
| Focus-visible ring | `{motion.duration-instant}` 80ms | `{motion.ease-enter}` | `opacity` of the 2 px `{colors.focus}` ring | Ring appears at full opacity with no transition; visibility is never animated away |
| Page / route transition | `{motion.duration-fast}` 150ms in, `{motion.duration-instant}` 80ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` of the content area only — the `page-frame` and `top-banner` never move or fade | Cross-fade at `{motion.duration-reduced}` 150ms; no travel to remove |
| Modal / drawer | `{motion.duration-base}` 250ms in, `{motion.duration-fast}` 150ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(2px → 0)`; scrim `opacity` 0 → 0.6 | Travel dropped; `opacity` fade only at `{motion.duration-reduced}` 150ms |
| Dropdown / select menu | `{motion.duration-fast}` 150ms in, `{motion.duration-instant}` 80ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` only — the panel is a hard-bordered white rectangle that appears, as a 1996 menu did | Unchanged — already opacity only; fade clamped to `{motion.duration-reduced}` 150ms |
| Toast (`ex-toast`) | `{motion.duration-base}` 250ms in, `{motion.duration-fast}` 150ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(2px → 0)` | Travel dropped; `opacity` fade only at `{motion.duration-reduced}` 150ms |
| List enter (ribbon-card stack, table rows) | `{motion.duration-base}` 250ms, `{motion.stagger-step}` 40ms per row, capped at 6 rows | `{motion.ease-enter}` | `opacity` only, no travel | Stagger removed; the whole list fades as one block at `{motion.duration-reduced}` 150ms |
| List exit | `{motion.duration-fast}` 150ms, no stagger | `{motion.ease-exit}` | `opacity` only | Unchanged; clamped to `{motion.duration-reduced}` 150ms |
| Loading (`button-primary`, `ex-cart-drawer`, `ex-data-table-cell`) | `{motion.duration-slow}` 400ms per step, infinite | `{motion.ease-standard}` | `opacity` of three Times Roman ellipsis glyphs in sequence | Loop frozen; a static "Working…" label in `{typography.body-sm}` replaces it |

**Rules this file holds to.** Exit is always shorter than its matching entrance (250 → 150, 150 → 80). Never animate `width`, `height`, `top`, `left` or `margin`; `transform` and `opacity` only. Nothing animates on first paint in a way that delays content. The loading ellipsis is the only infinite loop, and it is a loader, not ambience — this brand has no ambient motion, and a reproduction that adds a drifting gradient or a looping sticker wiggle has invented something the era did not have. The `new-burst-sticker`'s ~15° rotation is a static transform, not an animation.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (the 2px translateY on modal, drawer and toast),
     all stagger (list enter collapses to one block), and the infinite
     loading ellipsis loop, which freezes to a static "Working…" label. */
  /* Kept: opacity fades, every one clamped to 150ms, and the focus ring,
     which appears instantly and is never faded out. */
  *, *::before, *::after {
    transition-duration: 150ms !important;   /* {motion.duration-reduced} */
    animation-duration: 150ms !important;    /* {motion.duration-reduced} */
    animation-iteration-count: 1 !important;
    transition-property: opacity !important;
  }
}
```

Nothing is lost at this setting: because the brand's motion vocabulary is opacity-led by construction, the reduced-motion rendering is the design, not a degraded fallback.

## Accessibility

### Measured contrast

Computed with WCAG 2.1 relative luminance. Extracted brand values are frozen — where one fails, it is named here rather than corrected.

| Pair | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` #000000 on `{colors.canvas}` #ffffff | 21.0:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface}` #ffffff | 21.0:1 | 4.5:1 | Pass |
| `{colors.text-muted}` #666666 on `{colors.canvas}` | 5.74:1 | 4.5:1 | Pass |
| `{colors.on-primary}` #ffffff on `{colors.primary}` #e91d2a | **4.49:1** | 4.5:1 | **Fail — see below** |
| `{colors.hairline}` #000000 on `{colors.canvas}` | 21.0:1 | 3.0:1 | Pass |
| `{colors.focus}` #000000 on `{colors.canvas}` | 21.0:1 | 3.0:1 | Pass |
| `{colors.link}` #0000ee on `{colors.canvas}` | 9.4:1 | 4.5:1 | Pass |
| `{colors.primary}` #e91d2a on `{colors.frame-ink}` #000000 (`phone-callout`) | 4.67:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.yellow-sticker}` #fcc20f | 12.86:1 | 4.5:1 | Pass |
| `{colors.purple-stripe}` #6a26a4 on `{colors.yellow-sticker}` | 5.3:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.tint-olive}` #8e8a25 | 5.81:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.tint-salmon}` #d77a7a | 6.95:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.tint-periwinkle}` #8c9ae0 | 7.81:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.tint-peach}` #e6915d | 8.57:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.tint-sky}` #9ab6c8 | 9.9:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.tint-steel}` #a5b8c0 | 10.22:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.tint-sage}` #b3bd95 | 10.63:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.tint-lime}` #c0d4a7 | 13.22:1 | 4.5:1 | Pass |

### Disclosed failure: white on Dell red

**`cta-block-red` — `{colors.on-primary}` #ffffff on `{colors.primary}` #e91d2a measures 4.49:1 against a 4.5:1 requirement, and fails.** The same pair fails on **`cert-seal`** at **4.49:1**. The real brand genuinely does not meet AA here, by one hundredth of a ratio point, and `{colors.primary}` is Dell's identity red — it is not changed in this document. Two defensible mitigations, neither of which touches the hex:

1. Set the `cta-block-red` copy at 18.66px/700 or 24px+, where the WCAG large-text threshold of 3:1 applies and 4.49:1 passes comfortably. The panel is a single short sales paragraph, so promoting it from `{typography.body}` 14px to `{typography.heading-2}` 16px is **not** enough; `{typography.heading-1}` 24px/900 would clear it.
2. Set the copy in `{colors.ink}` black on the red fill instead, which measures 4.67:1 and passes at any size — at the cost of the white-on-red look the 1996 panel actually had.

Until one is chosen, this is a known, disclosed AA failure, not an oversight. `cert-seal` is decorative award imagery with its text duplicated in the adjacent body copy, so its 4.49:1 is the lower-risk of the two.

### Focus ring visibility, per surface this file defines

`{colors.focus}` #000000 at `{focus-ring.width}` 2px with `{focus-ring.offset}` 1px, except on black chrome where `{colors.focus-on-dark}` #ffffff is used instead.

| Surface the ring is drawn over | Ring token | Ratio | Required | Result |
|---|---|---|---|---|
| `{colors.canvas}` / `{colors.surface}` #ffffff | `{colors.focus}` | 21.0:1 | 3.0:1 | Pass |
| `{colors.primary}` #e91d2a (`cta-block-red`, `cert-seal`) | `{colors.focus}` | 4.67:1 | 3.0:1 | Pass |
| `{colors.yellow-sticker}` #fcc20f (`buy-a-dell-sticker`) | `{colors.focus}` | 12.86:1 | 3.0:1 | Pass |
| `{colors.tint-olive}` #8e8a25 — the worst case of the eight tints | `{colors.focus}` | 5.81:1 | 3.0:1 | Pass |
| `{colors.tint-salmon}` #d77a7a | `{colors.focus}` | 6.95:1 | 3.0:1 | Pass |
| All six remaining tints | `{colors.focus}` | 7.81–13.22:1 | 3.0:1 | Pass |
| `{colors.frame-ink}` #000000 (`page-frame`, `top-banner`, `button-primary`, `phone-callout`) | `{colors.focus-on-dark}` | 21.0:1 | 3.0:1 | Pass |
| Product-photo GIFs (no measurable fill) | `{colors.focus}` + 1px `{colors.focus-on-dark}` outer edge | n/a | 3.0:1 | Two-tone ring, per SPEC §1 |

A single ring cannot serve this palette: `{colors.link}` #0000ee, the obvious brand-native choice, measures 9.4:1 on white but only **2.09:1 on `{colors.primary}`** and **2.60:1 on `{colors.tint-periwinkle}`**, so it is rejected. Black plus a white counterpart is both measurable and period-correct — 1996 browsers drew a black dotted outline, which is the ancestor of this ring.

### Tap targets

Not measurable from a document; this is a stated requirement, not an observation. 1996 assumed mouse-only input: the footer icon-label pairs sat at roughly 24 × 24px with an 8px label beneath, and `button-primary` at `{spacing.s}` 6px vertical padding on a `{typography.button}` 12px label computes to about 24px tall. Both are below the 44 × 44px minimum. Modern reproductions must pad `icon-label-nav` and every button to 44 × 44px minimum at all widths, without enlarging the glyph itself — the 24px icon stays 24px inside a 44px target, so the catalog density survives.

### Reduced motion

Honoured in full; see the `@media (prefers-reduced-motion: reduce)` block above. All travel and stagger are removed, every opacity fade is clamped to `{motion.duration-reduced}` 150ms, and the loading loop freezes to a static label. No information is conveyed by motion alone anywhere in this system.

### Other standing issues

- **Colour-only product coding.** The eight ribbon tints are the primary way product families are distinguished. Every card also carries its name in `{typography.heading-3}` in the title bar, so the coding is never colour-alone — keep that title bar in any reproduction that reorders or filters the cards.
- **Serif body at 14px.** `{typography.body}` Times New Roman 14px/1.4 is period-correct and passes contrast at 21:1, but a 14px serif is the least legible combination in this file. Modern reproductions should allow user text scaling to 200% without a fixed-width table clipping it — the original 760px fixed table does not survive that, which is a real conflict between fidelity and WCAG 1.4.4.
- **`{colors.text-muted}` is prescribed.** Using it for anything larger than `{typography.caption}` would introduce a tonal hierarchy the brand does not have.

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
| `{colors.text-muted}` (`#666666`) on `{colors.tint-steel}` (`#a5b8c0`) | 2.79:1 | 4.5:1 | Fail — secondary text on surface |

## Do's and Don'ts

### Do
- Keep the literal `{components.page-frame}` black border on every page — this is the brand's single most identifiable container chrome.
- Reserve `{colors.primary}` (Dell red) for the `{components.cta-block-red}` panel and the `{components.phone-callout}` only. Every other use dilutes the urgency signal.
- Use the eight ribbon-card tint colors (`{colors.tint-olive}` / sage / salmon / peach / lime / sky / steel / periwinkle) as a *family* — pick one per product line and stay with it across the line's marketing surfaces.
- Set every display headline in `{typography.display}` (Arial Black 36 / weight 900). The brand's typographic register depends on extreme weight against flat color.
- Keep body copy in `{typography.body}` Times Roman 14 — substituting a modern sans loses the catalog feel entirely.
- Render every CTA / button at `{rounded.none}` (0 px). Modern soft-radius buttons betray the era.
- Use hand-painted bevels / hard-edge GIF shadows on stickers and product photos. Never substitute a soft CSS shadow.

### Don't
- Don't introduce a chromatic accent outside the eight catalog tints + Dell red + Dell yellow + classic link blue. The palette is closed by design.
- Don't soften any corner. `{rounded.none}` is the universal modifier; only award seals get `{rounded.full}`.
- Don't replace Times Roman body with Arial / Helvetica / Inter / a webfont — the serif body is the era's signature.
- Don't add soft drop-shadows or atmospheric gradients. The brand has hard borders and flat fills; everything else reads as anachronism.
- Don't crop or "tuck" product photos with `border-radius` or `clip-path`. The notch into the ribbon-card right edge is the framing — the photo itself stays a hard rectangle.
- Don't pair two `{components.cta-block-red}` panels on the same page. The red fill is meant to be the singular attention pole.
- Don't strip the `{components.phone-callout}` from the top banner. In 1996 the website existed to drive phone-call orders; the phone number IS the navigation.
- Don't add entrance choreography, parallax, scroll reveals or ambient loops. The only infinite animation permitted is the `{motion.duration-slow}` loading ellipsis.
- Don't suppress the focus ring to protect the look. `{colors.focus}` / `{colors.focus-on-dark}` is prescribed, not extracted, but it is not optional.

## Known Gaps

Everything in this list is either unverifiable from the three captured pages or is an acknowledged interpretation. Nothing here should be read as an extracted fact.

**Prescribed, not extracted — the whole of it:**
- The entire `motion:` group, the `## Motion & Animation` table and the reduced-motion block. Dell.com in 1996 had no CSS transitions and no scripted easing; nobody measured a timing function on this site because there was none to measure. The Calm profile was assigned by SPEC §5 rule 4 and applied as a ceiling.
- `{colors.focus}` / `{colors.focus-on-dark}` and the whole `focus-ring:` group. The 1996 design specified no focus indicator; the browser drew its own dotted outline.
- `{colors.text-muted}` #666666. The real page has no secondary ink at all.
- The `shadow:` group. `{shadow.bevel}` and `{shadow.bevel-inset}` are a modern CSS transcription of bevels that were hand-painted into GIF pixels; the originals have no numeric value to extract.
- Every state in the State Matrix except default, and `button-text-link`'s underline. HTML 3.2 gave the page `A:link` / `A:visited` / `A:active` and the browser's native button depress; nothing else existed.

**Not knowable from a document:**
- Tap-target sizes, overlap, clipping, horizontal overflow, frame rate and layout shift all need a rendered page. The 24 × 24px icon figure and the ~24px button height in Accessibility are arithmetic from this file's own padding and type tokens, not measurements of a running UI.
- Whether the 760px fixed table survives 200% text zoom. Almost certainly it does not, but that is a rendering claim.

**Missing from the source captures:**
- `A:visited` link colour. The era's default was #551a8b, but it is not observed on these pages, so no `link-visited` token is defined.
- Form widget states beyond default. The Search and "Configure & Buy" forms are described in the prose but not visible in the three captures.
- Any dark-mode or alternate-polarity theme. The 1996 design has exactly one polarity: black frame, white paper. `{colors.focus-on-dark}` serves the black chrome, not a dark theme.
- "About Dell" staff photography, avatars and any page beyond the home page, the Dimension page and the OptiPlex page.
- The exact tint-to-product mapping for `{colors.tint-olive}` as a *body* fill. It is observed only as an eyebrow block; its use as a ribbon body is inferred from the pattern of the other seven.

**Unresolved by design:**
- `{colors.canvas}` and `{colors.surface}` are the same #ffffff, so the two layers measure 1.0:1. This is accurate to the brand and is not a defect to fix, but any tool that expects a distinguishable raised surface will have nothing to work with here.
- White on Dell red fails AA at 4.49:1. Disclosed in Accessibility, not corrected, and awaiting a decision between the two mitigations listed there.
- The `ex-*` block is auto-derived and its descriptions still reference "feature-card chrome", a component this file does not define. The references are prose, not `{}` tokens, so nothing dangles — but the wording came from a generator, not from this brand.
