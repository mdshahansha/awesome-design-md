---
version: alpha
name: Nintendo.com (2001) Analysis
description: An analysis of Nintendo.com's 2001 design language — a brushed-periwinkle "console chrome" interface where every panel is a beveled metal plate, navigation glows amber over a halftone-dotted carbon bar, and bold outlined display type sits on circuit-board hero fields. A Y2K hardware aesthetic that treats the web page like the faceplate of a game system.

colors:
  primary: "#e60012"          # Nintendo Red — racetrack logo, alert
  signal: "#f68d1f"           # Signal Orange — forward cues, submit, "Play It On"
  amber: "#ecab37"            # Amber — utility buttons, info-box tabs, badges
  nav-gold: "#e48600"         # Nav Gold — top-nav menu links
  canvas: "#7a8aba"           # Periwinkle metallic — primary interface body
  canvas-soft: "#9fbee7"      # Pale Sky — secondary-nav strip, light inset panels
  sky: "#9fbee7"              # Pale Sky alias
  lavender: "#acace7"         # Pale Lavender — home hero field
  ice: "#c0d5e6"              # Pale Ice — news hero field
  periwinkle: "#8ba1d4"       # Light Periwinkle — raised mid panels
  chrome-indigo: "#3d4f97"    # Chrome Indigo — beveled borders, tab edges
  muted-indigo: "#60619c"     # Muted Indigo — inactive tabs, secondary chrome
  platinum: "#dedede"         # Platinum Gray — list-row / inset content surface
  surface: "#ffffff"          # White — content cards, list-row highlight
  carbon: "#21242e"           # Carbon Navy — nav bar, dark buttons, footer, ink
  hairline: "#5a5f8c"         # blended bevel divider
  ink: "#21242e"              # primary text on light
  ink-soft: "#3d4f97"         # secondary text / chrome labels
  on-primary: "#ffffff"       # text on dark/red/orange chrome
  focus: "#13275e"            # Bevel Indigo — focus ring on periwinkle/white chrome (prescribed)
  focus-on-dark: "#ecab37"    # Amber ring for controls on the carbon command layer (reuses the extracted amber)
  systems-teal: "#206479"     # Systems hero circuit-board cyan
  games-red: "#a7282b"        # Games F-1 racing hero
  error: "#e60012"            # validation / destructive (shares brand red)

typography:
  nav-link:
    fontFamily: Arial
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
  ui-label:
    fontFamily: Arial
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px
  display:
    fontFamily: Arial Black
    fontSize: 44px
    fontWeight: 900
    lineHeight: 1
    letterSpacing: 0
  hero-tagline:
    fontFamily: Arial
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body:
    fontFamily: Arial
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: Arial
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  micro:
    fontFamily: Arial
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 48px

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
    backgroundColor: "{colors.carbon}"
    textColor: "{colors.nav-gold}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    height: 28px
  subnav-strip:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs}"
  logo-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.display}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs}"
  button-primary:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.carbon}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
  button-primary-pressed:
    backgroundColor: "{colors.nav-gold}"
    textColor: "{colors.carbon}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
  button-submit:
    backgroundColor: "{colors.signal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.carbon}"
    textColor: "{colors.on-primary}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
  button-icon-arrow:
    backgroundColor: "{colors.signal}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    size: 22px
  button-arrow-chip:
    backgroundColor: "{colors.signal}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"
    size: 18px
  search-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"
    height: 20px
  text-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"
    height: 20px
  select-dropdown:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"
    height: 24px
  field-label:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs}"
  form-panel:
    backgroundColor: "{colors.platinum}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  dotted-divider:
    borderColor: "{colors.muted-indigo}"
    borderStyle: dotted
    rounded: "{rounded.none}"
    height: 1px
  hero-panel:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.surface}"
    typography: "{typography.display}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  section-label-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  news-row:
    backgroundColor: "{colors.platinum}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.link}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  featured-tile:
    backgroundColor: "{colors.carbon}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs}"
  poll-panel:
    backgroundColor: "{colors.periwinkle}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  radio-option:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.full}"
    size: 12px
  info-box:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
  promo-card:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.display}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
  system-tile:
    backgroundColor: "{colors.periwinkle}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  link-row-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  calendar-widget:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  left-rail-tab:
    backgroundColor: "{colors.carbon}"
    textColor: "{colors.canvas-soft}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs}"
  footer-bar:
    backgroundColor: "{colors.carbon}"
    textColor: "{colors.canvas-soft}"
    typography: "{typography.micro}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  esrb-badge:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.carbon}"
    typography: "{typography.micro}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs}"
  esrb-rating-square:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.carbon}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.xs}"
    size: 20px
  mascot-bubble:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.carbon}"
    typography: "{typography.micro}"
    rounded: "{rounded.lg}"
    padding: "{spacing.sm}"

  # ─── Examples (illustrative) — kit-mirror demonstration surfaces ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.ui-label}"
    bodyTypography: "{typography.body}"
    cellPadding: "{spacing.xs} {spacing.sm}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.lg}"
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

Nintendo.com circa 2001 is the web rendered as **console hardware**. Where most sites of the era reached for either grunge texture or corporate gradients, this interface builds itself out of **brushed-periwinkle metal plates** — every region is a discrete beveled panel, edge-lit with a brighter highlight on top and a `{colors.chrome-indigo}` shadow line beneath, as if stamped from the same injection-molded plastic as a Game Boy. The whole page reads as one machine faceplate: a body of `{colors.canvas}` periwinkle chrome carrying inset modules, with the corners of the largest panels physically **chamfered** (cut at 45°) rather than rounded, reinforcing the manufactured-object feeling.

The system runs on a tight three-voice contrast. The structural voice is the cool periwinkle-to-indigo chrome (`{colors.canvas}`, `{colors.periwinkle}`, `{colors.chrome-indigo}`). The authority voice is `{colors.carbon}` carbon-navy — the top navigation bar, the right-rail action buttons, and the footer, all near-black slabs printed with a faint **halftone dot-matrix texture** that evokes a speaker grille. The energy voice is warm and reserved for one job only: telling you where to go. `{colors.nav-gold}` lights the primary menu words, `{colors.amber}` fills the utility chips and badges, and `{colors.signal}` orange marks every "forward" cue — the round arrow buttons, the chevron chips beside each headline, the Submit button. Warmth in this system always means *action*; the cool chrome never carries it.

Atmosphere comes from the **hero fields**, which break the periwinkle calm with full-bleed product photography over textured backdrops — a circuit-board cyan on Systems, a motion-blurred racetrack red on Games, a soft lavender wash on Home — each topped with chunky `{typography.display}` wordmarks rendered in white with a heavy outline and hard drop shadow, the visual signature of game-box cover type. A pixel-eared Mario leans in from the masthead with a "Welcome to Nintendo.com!" speech bubble, anchoring the entire machine to the brand's playful character voice.

**Key Characteristics:**
- Every UI region is a **beveled metal plate** in `{colors.canvas}` periwinkle, edge-lit on top and shadow-lined with `{colors.chrome-indigo}` below — the page is assembled, not laid out.
- **Chamfered (cut-corner) panel geometry** on the largest modules; most chrome is sharp-edged (`{rounded.none}`), with rounding reserved for the logo pill, radio dots, and circle-arrow badges (`{rounded.full}`).
- A **carbon-navy command layer** (`{colors.carbon}`) with halftone-dot texture carries the top nav, right-rail buttons, and footer.
- Warmth is rationed as **directional signal only**: `{colors.nav-gold}` for menu words, `{colors.amber}` for utility chips/badges, `{colors.signal}` for every forward/Submit cue.
- **Photographic hero fields** cycle a page-specific accent tint (`{colors.lavender}` home → `{colors.systems-teal}` systems → `{colors.games-red}` games) under outlined `{typography.display}` box-art wordmarks.
- A dense, **modular grid** — masthead, dual nav bars, hero, then a two-thirds content column of stacked list/feature panels beside a one-third right action rail — packed with minimal whitespace.
- **Character-led**: the Mario mascot speech-bubble masthead and ESRB badge frame the chrome with brand personality and regulatory trust marks.

## Colors

The palette is a **cool metallic chassis with rationed warm signal**. Read it as three layers: the periwinkle chrome that everything is built from, the carbon command slabs, and the warm wayfinding accents that are the only saturated color in the steady-state interface.

### Brand & Accent
- **Nintendo Red** (`{colors.primary}` — #e60012): The racetrack logo wordmark and the brand's anchor hue. Used sparingly as pure brand identity and doubled as the validation/alert color. Never a surface fill outside the logo plate.
- **Signal Orange** (`{colors.signal}` — #f68d1f): The "go forward" color. Fills every round arrow button, every chevron chip beside a headline, the Submit button, and the "Play It On" platform badges. If something advances you, it is orange.
- **Amber** (`{colors.amber}` — #ecab37): Utility energy. Fills the Code Bank / Game Finder / Go chips, the info-box header tabs, the sweepstakes stars, and the ESRB Privacy-Certified badge. Distinguished from Signal Orange by being more golden and reserved for *tools and marks* rather than *forward motion*.
- **Nav Gold** (`{colors.nav-gold}` — #e48600): The deeper orange-gold reserved exclusively for the primary navigation words (Games, Systems, News, Nsider, Downloads) glowing on the carbon bar.

### Surface
- **Periwinkle Metallic** (`{colors.canvas}` — #7a8aba): The primary interface body — the brushed-metal chrome that every module is inset into.
- **Light Periwinkle** (`{colors.periwinkle}` — #8ba1d4): Raised mid panels (poll panel, system tiles) — one step brighter than canvas for elevation.
- **Pale Sky** (`{colors.sky}` / `{colors.canvas-soft}` — #9fbee7): The secondary-nav strip and light inset panel fills.
- **Pale Lavender** (`{colors.lavender}` — #acace7): The home hero field and side promo cards.
- **Pale Ice** (`{colors.ice}` — #c0d5e6): The News hero panel field.
- **Chrome Indigo** (`{colors.chrome-indigo}` — #3d4f97): The beveled border / shadow line under every plate, and the leading angled edge of nav tabs.
- **Muted Indigo** (`{colors.muted-indigo}` — #60619c): Inactive tabs and recessed chrome.
- **Platinum Gray** (`{colors.platinum}` — #dedede): The list-row and inset content surface — news headlines and archive rows sit on this cool platinum.
- **White** (`{colors.surface}` — #ffffff): Content cards, form fields, the logo pill, and list-row highlight.

### Text
- **Carbon Navy** (`{colors.ink}` — #21242e): Primary text on light chrome, and the fill of the dark command layer (nav bar, rail buttons, footer).
- **Chrome Indigo** (`{colors.ink-soft}` — #3d4f97): Secondary text and small-caps chrome labels.
- **White** (`{colors.on-primary}` — #ffffff): Text on carbon, red, and orange chrome.

### Focus
No focus ring was extracted — the 2001 original relied on the browser's own
default dotted outline. Both rings below are **prescribed**, and one ring cannot
serve this file because it documents two surface polarities: the light periwinkle
chrome and the `{colors.carbon}` command layer.
- **Bevel Indigo** (`{colors.focus}` — #13275e): the ring for controls on every light surface — a deeper step of the same indigo ladder as `{colors.chrome-indigo}`, so it reads as the bevel line drawn one shade harder. Measures **4.17:1 on `{colors.canvas}`**, 14.19:1 on `{colors.surface}`, 10.55:1 on `{colors.platinum}`, 7.43:1 on `{colors.canvas-soft}`, 6.63:1 on `{colors.lavender}`, 5.51:1 on `{colors.periwinkle}`.
- **Amber on dark** (`{colors.focus-on-dark}` — #ecab37): the ring for controls on the `{colors.carbon}` slabs (nav words, right-rail buttons, left-rail tabs, footer links), where Bevel Indigo would sit at 1.09:1. It reuses the extracted amber hex on purpose — amber is already this system's utility-energy colour — and measures **7.7:1 on `{colors.carbon}`**.
- Both are drawn as a 2px ring **outside** the control with a 1px offset, so the ratio that matters is against the surface behind the control, not against the control's own fill. The two rings separate from each other at 7.06:1.

### Semantic
- **Error / Alert** (`{colors.error}` — #e60012): Validation and destructive states reuse the brand red.
- **Systems Teal** (`{colors.systems-teal}` — #206479): Page-accent tint — the Systems hero's circuit-board cyan field.
- **Games Red** (`{colors.games-red}` — #a7282b): Page-accent tint — the Games hero's motion-blurred racetrack field.

## Typography

### Font Family
The era's web-safe reality is **Arial / Helvetica** throughout — there are no webfonts. The system gets its character not from typeface choice but from *treatment*: tight uppercase tracking on every chrome label, and a heavy outlined-and-shadowed display style for hero wordmarks that mimics console box-art logotype. Body copy is plain small Arial; links are the same family at bold weight in `{colors.ink-soft}`.

The micro-labels (vertical left-rail tabs, footer fine print) render with the soft pixelation characteristic of small bitmap-rendered Arial of the period — for a faithful reproduction, pair Arial with a pixel face such as **Silkscreen** or **VT323** at the 10–11px label sizes.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display}` | 44px | 900 | 1 | 0 | Hero box-art wordmarks (white, heavy outline + hard drop shadow) |
| `{typography.hero-tagline}` | 15px | 700 | 1.3 | 0 | Hero supporting line ("Gorgeous graphics, great sound…") |
| `{typography.nav-link}` | 13px | 700 | 1 | 0.5px | Primary nav menu words, uppercase |
| `{typography.ui-label}` | 11px | 700 | 1.1 | 0.5px | Section header labels, panel titles, button text — uppercase |
| `{typography.link}` | 12px | 700 | 1.4 | 0 | News headline links, "Read More" |
| `{typography.body}` | 12px | 400 | 1.4 | 0 | Descriptions, poll text, info-box copy |
| `{typography.micro}` | 10px | 400 | 1.3 | 0 | Footer copyright, calendar cells, fine print |

### Principles
- **Uppercase + tracking is the chrome voice.** Every structural label — nav words, panel headers ("Official News", "Featured Sites", "Player's Poll"), button text — is uppercase Arial Bold with a half-pixel of tracking. It reads like silkscreened legends on a controller.
- **Display type is outlined, never flat.** Hero wordmarks always carry a thick contrasting outline and a hard offset shadow so they pop off the photographic field — the box-art convention.
- **Body stays small and quiet.** At 12px, descriptive copy never competes with the chrome; the hierarchy is carried entirely by the labels and the photography.

### Note on Font Substitutes
Arial is freely available system-wide and needs no substitute. To recreate the period bitmap rendering of micro-labels, layer a pixel font (**Silkscreen**, **VT323**, or **Press Start 2P** for the chunkiest legends) at 10–11px and disable anti-aliasing. The display wordmarks are bespoke logotypes; the closest open substitute is **Archivo Black** (italicized) or **Arial Black** with a CSS text-stroke outline and `text-shadow` offset.

## Layout

### Spacing System
- **Base unit**: 8px (`{spacing.sm}`) — the gutter rhythm between list rows and grid cells.
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.section}` 48px
- Panels carry **12px interior padding** (`{spacing.md}`); larger content modules use **16px** (`{spacing.lg}`). Inter-module gaps run 16–24px. The layout is deliberately dense — whitespace is a structural seam between plates, not a luxury.

### Grid & Container
- **Fixed-width canvas** ~780–830px wide (a desktop-era fixed table layout, centered). No fluid scaling — the interface is sized to a single target window like an application.
- **Masthead row**: Mario mascot + speech bubble (left) and search module (right) float above the chrome.
- **Dual nav bars**: a carbon primary bar (logo + 5 section words + Code Bank / Game Finder utility chips) stacked over a periwinkle secondary strip (Parents, Customer Service, Corporate, Global, Privacy, Store, Contact).
- **Body**: a full-width hero panel, then a **two-column split** — a ~two-thirds content column of stacked panels (Official News list, Featured Sites 2×2 grid, etc.) beside a ~one-third **right action rail** (Login / Subscribe / Newsletter / Help buttons, an info box, a side promo card).
- **Left rail**: a thin vertical strip of rotated tabs (Top Ten, Top Rentals, Player's Choice, ESRB Ratings) clipped to the chrome edge.

### Whitespace Philosophy
Empty space is **engineered seam**, not breathing room. Modules butt against each other separated by thin `{colors.chrome-indigo}` bevel lines and a few pixels of canvas, so the eye reads grouped plates. The density is intentional: it makes the page feel like a packed control panel where everything is one click away.

## Elevation & Depth

Depth in this system is **physical bevel simulation**, not soft shadow. There is no blurred drop-shadow vocabulary; instead every plate is given the illusion of being a raised piece of molded plastic.

| Level | Treatment | Use |
|---|---|---|
| 0 — Inset | Recessed into canvas; darker `{colors.chrome-indigo}` top edge, lighter bottom edge | List rows, form fields, the canvas body itself |
| 1 — Plate | Flush panel; lighter top highlight, `{colors.chrome-indigo}` shadow line beneath | Content panels, system tiles, info box |
| 2 — Raised chip | Beveled button with bright top edge + hard bottom shadow | Utility chips, Go/Submit buttons, nav tabs |
| 3 — Command slab | `{colors.carbon}` near-black with halftone texture, sits "above" the chrome | Top nav bar, right-rail buttons, footer |

### Decorative Depth
Depth is also carried by **texture and photography**: the halftone dot-matrix on carbon slabs reads as a recessed speaker grille; hero fields use motion-blur, circuit-board patterns, and product renders with their own cast shadows to create literal pictorial depth; chamfered corners on the outer chrome suggest a machined faceplate edge. The left-rail rotated tabs appear to tuck *behind* the main chrome, a small but effective layered cue.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | The default — nav bar, footer, most chrome plates (sharp / chamfered, not rounded) |
| `{rounded.xs}` | 2px | Utility buttons, form fields, badges |
| `{rounded.sm}` | 4px | Small panels, featured tiles, list rows |
| `{rounded.md}` | 6px | Content panels, hero panel |
| `{rounded.lg}` | 10px | Outer section panels, mascot bubble |
| `{rounded.full}` | 9999px | Logo racetrack pill, radio dots, circle-arrow badges |

The signature is **sharpness with rationed roundness**. The chrome is hard-edged and frequently *chamfered* (corners cut at 45° rather than curved) — this is the manufactured-faceplate look. Roundness appears only where it signals a physical control: the fully-pill logo, the round radio buttons, and the round Signal-Orange arrow badges. A modern reproduction should resist the urge to soften every corner; the tension between sharp plates and the few pill elements is the whole character.

### Photography Geometry
Hero photography fills beveled rectangles at roughly 4:1 (banner) and 16:9 proportions, full-bleed within the panel. Featured-site and game thumbnails are near-4:3 fixed tiles (~95×60px) framed by a 1–2px `{colors.chrome-indigo}` edge with `{rounded.sm}` corners. The mascot is a transparent cutout overlapping the masthead, breaking the rectangular grid for personality.

## Components

> Each spec below covers Default and, where extracted, Pressed/Active. Variants live as separate `components:` entries. **No hover, focus, disabled, loading, selected or error state was extracted from the 2001 site** — the only state change the original encoded was the depressed-bevel swap on a utility chip. The ladder in *Interaction States* below is therefore **prescribed** for a modern reproduction, not extracted.

### Navigation

**`nav-bar`** — Primary top navigation
- `{colors.carbon}` slab with a faint halftone-dot texture, ~28px tall, carrying the `{components.logo-pill}` at left, the five `{colors.nav-gold}` section words in `{typography.nav-link}` uppercase, and the amber Code Bank / Game Finder utility chips at right. Sharp corners (`{rounded.none}`), `{spacing.sm}` padding.

**`subnav-strip`** — Secondary navigation
- A `{colors.canvas-soft}` pale-sky strip directly beneath the nav bar, carrying utility links (Parents, Customer Service, Corporate, Global, Privacy, Store, Contact) in `{typography.ui-label}` `{colors.ink}`, separated by thin dividers. Sharp, `{spacing.xs}` padding.

**`left-rail-tab`** — Rotated section tabs
- A thin vertical strip of `{colors.carbon}` tabs (Top Ten, Top Rentals, Player's Choice, ESRB Ratings) with vertically-rotated `{typography.ui-label}` text in `{colors.canvas-soft}`, clipped to the left chrome edge. Sharp corners, `{spacing.xs}` padding.

### Brand & Masthead

**`logo-pill`** — Nintendo racetrack logo
- The wordmark in `{colors.primary}` red set inside a white `{rounded.full}` racetrack pill, outlined. Sits at the left of the nav bar. `{spacing.xs}` padding.

**`mascot-bubble`** — Mario welcome speech bubble
- A white `{rounded.lg}` rounded-rectangle speech bubble with a tail, carrying "Welcome to Nintendo.com!" in `{typography.micro}` `{colors.carbon}`, paired with the Mario cutout in the masthead. `{spacing.sm}` padding.

### Buttons

**`button-primary`** — Amber utility / Go chip
- `{colors.amber}` fill, `{colors.carbon}` text in `{typography.ui-label}`, `{rounded.xs}` corners, `{spacing.md}` padding, with a beveled top highlight. The everyday tool button (Code Bank, Game Finder, Go).
- Pressed state in **`button-primary-pressed`** — fill deepens to `{colors.nav-gold}`.

**`button-submit`** — Forward / Submit
- `{colors.signal}` orange fill, `{colors.on-primary}` white text in `{typography.ui-label}`, `{rounded.xs}`, `{spacing.lg}` padding. The "commit" action (poll Submit, Go on archives).

**`button-secondary`** — Right-rail action button
- `{colors.carbon}` near-black slab, `{colors.on-primary}` white text in `{typography.ui-label}`, sharp `{rounded.none}` corners, `{spacing.md}` padding, with a small leading icon. Used for Login / Subscribe / Newsletter / Help in the right rail.

**`button-icon-arrow`** — Round forward arrow
- A 22px `{colors.signal}` orange `{rounded.full}` disc with a white chevron — the primary "go" affordance on hero panels and section links.

**`button-arrow-chip`** — Headline chevron chip
- An 18px `{colors.signal}` orange `{rounded.xs}` chip with a white forward chevron, sitting at the right end of each `{components.news-row}` to advance to the article.

### Inputs & Forms

**`search-field`** — Masthead search input
- White `{colors.surface}` field, `{colors.ink}` text in `{typography.body}`, `{rounded.xs}` corners, 1px `{colors.hairline}` border, ~20px tall, paired with an "All" category dropdown and an amber Go chip.

**`text-input`** — Generic text field
- Same chassis as `search-field`: white fill, `{colors.ink}` text, `{rounded.xs}`, `{colors.hairline}` 1px border, `{spacing.xs}` padding. Used in the Login form (Username / Password / E-mail), news-archive keyword, and date fields.

**`select-dropdown`** — Native select ("Click to choose")
- A white `{colors.surface}` field with `{colors.ink}` text in `{typography.body}`, `{rounded.xs}` corners, and a hard 1px `{colors.carbon}` border (sharper than the inputs) closing on a beveled native dropdown-chevron button at the right edge. ~24px tall, `{spacing.xs}` padding. Used for the Register form's Month / Year pickers.

**`field-label`** — Inline form label
- A bold `{colors.ink}` label in `{typography.link}` (Arial Bold 12px) sitting left of its input (Username, Password, E-mail, Month, Year). `{rounded.none}`, `{spacing.xxs}` padding.

**`radio-option`** — Poll radio button
- A 12px white `{rounded.full}` radio dot with a `{colors.hairline}` ring, paired with `{typography.body}` option text. Used in the Player's Poll.

**`form-panel`** — Form container (Login / Register)
- A `{colors.platinum}` light-gray `{rounded.md}` panel holding a form, capped by a `{components.section-label-bar}` header (≡ LOG IN / ≡ REGISTER). `{spacing.lg}` interior. The Login page pairs two side by side.

**`dotted-divider`** — Dotted hairline rule
- A 1px dotted `{colors.muted-indigo}` separator rule used between form sub-sections (the "Note:" line, "Forgot Your Password?"). A recurring Y2K-chrome detail — dotted rather than solid. The token is the rule's **stroke**, declared as `borderColor`: this component has no fill and no text of its own, and it is drawn inside `{components.form-panel}`, where muted indigo on `{colors.platinum}` measures 4.23:1 — above the 3:1 a boundary needs.
- States: default only. A static rule genuinely has one state.

### Cards & Panels

**`hero-panel`** — Photographic hero plate
- A `{rounded.md}` beveled rectangle filled with full-bleed product photography over a page-tinted field (`{colors.lavender}` / `{colors.systems-teal}` / `{colors.games-red}`), topped with an outlined `{typography.display}` wordmark and a `{components.button-icon-arrow}` call-to-action. `{spacing.lg}` interior.
- **This pairing fails AA and the failure is real, not a binding artefact.** `{colors.lavender}` is a genuine painted field, and the white `{typography.display}` wordmark is genuinely drawn on it: white on #acace7 measures **2.14:1**, under the 3:1 that 44px/900 large text needs. The wordmark's carbon outline and hard offset shadow are what made it legible in 2001, and WCAG gives no credit for either. On the other two hero tints the same white type passes — 6.64:1 on `{colors.systems-teal}` and 7.04:1 on `{colors.games-red}` — so the lavender Home field is the single failing case. See Accessibility.
- States: default, hover, focus-visible (on its `{components.button-icon-arrow}`), loading (photographic field absent). No pressed, disabled, selected or error state — the panel is not itself a control.

**`section-label-bar`** — Panel header
- A `{colors.canvas}` header strip with a small grid/list glyph and an uppercase `{typography.ui-label}` title ("Official News", "Featured Sites", "Player's Poll"). Sharp corners, `{spacing.sm}` padding. Caps every content module.

**`news-row`** — Headline list row
- A `{colors.platinum}` `{rounded.sm}` row with a small category icon, a `{typography.link}` headline in `{colors.ink-soft}`, and a trailing `{components.button-arrow-chip}`. `{spacing.sm}` padding. Stacked into the Official News / Other Headlines lists.

**`featured-tile`** — Featured-site thumbnail
- A `{colors.carbon}`-framed `{rounded.sm}` tile (~95×60px) holding a screenshot thumbnail with a `{typography.micro}` URL caption (e.g. www.pokemon.com). Tight `{spacing.xxs}` padding, arranged in a 2×2 grid.

**`poll-panel`** — Player's Poll module
- A `{colors.periwinkle}` raised `{rounded.md}` panel posing a question, listing `{components.radio-option}` choices, and closing with a `{components.button-submit}`. `{spacing.md}` interior.

**`info-box`** — "What Is" explainer card
- A white `{colors.surface}` `{rounded.sm}` card with an amber header tab ("What Is — Game Finder") and `{typography.body}` explanatory copy. `{spacing.md}` padding. Sits in the right rail.

**`promo-card`** — Side product promo
- A `{colors.lavender}` `{rounded.sm}` card carrying an outlined product wordmark (e.g. Game Boy Advance) over a small product render, in the right rail. `{spacing.md}` padding.

**`system-tile`** — Hardware grid tile (Systems page)
- A `{colors.periwinkle}` `{rounded.sm}` tile holding a console render over a circuit-board backdrop with an outlined system name (Nintendo 64, Super Nintendo, Game Boy). `{spacing.sm}` padding, arranged in a 2×3 grid.

**`link-row-card`** — Utility link card (Systems page)
- A white `{rounded.sm}` card with an amber label tab (Technical Help, Store Locator, Online Store), a character icon, and a one-line `{typography.body}` description. `{spacing.sm}` padding.

**`calendar-widget`** — Month calendar (News page)
- A white `{rounded.sm}` grid calendar in `{typography.micro}`, with a `{colors.carbon}` caption header (e.g. "June 01"), highlighted event dates, and a month-select dropdown. `{spacing.sm}` padding.

### Badges & Footer

**`esrb-badge`** — ESRB Privacy-Certified mark
- A small `{colors.amber}` `{rounded.xs}` badge reading "ESRB — Privacy Certified" in `{typography.micro}` `{colors.carbon}`, pinned in the footer.

**`esrb-rating-square`** — Game content-rating square
- A 20px white `{rounded.xs}` square stamping the content-rating letter (E, T) in `{typography.ui-label}` `{colors.carbon}`, on each game card.

**`footer-bar`** — Page footer
- A `{colors.carbon}` chamfered slab with the "©1997–2001 Nintendo…" copyright in `{typography.micro}` `{colors.canvas-soft}`, the ESRB badge, and a privacy link. Sharp corners, `{spacing.lg}` padding.

### Examples (illustrative)

> Kit-mirror demonstration surfaces. Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently.

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

> **Prescribed, not extracted.** The 2001 original documents one state change:
> the beveled utility chip deepening to `{colors.nav-gold}` when depressed
> (`{components.button-primary-pressed}`). Everything else below is the state
> ladder a faithful modern reproduction needs, expressed in this file's own
> chrome vocabulary — bevel polarity, warm signal, and the two prescribed focus
> rings — rather than borrowed from a modern card system.

| Component | default | hover | focus-visible | active / pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.amber}` fill, top bevel highlight | fill lightens one step, bevel unchanged | 2px `{colors.focus}` ring, 1px offset | fill deepens to `{colors.nav-gold}`, bevel inverts to inset | fill desaturates to `{colors.platinum}`, `{colors.muted-indigo}` text, bevel flat | caption swaps to "…" ellipsis in `{typography.ui-label}`, chip non-interactive | n/a | n/a |
| `button-submit` | `{colors.signal}` fill, white label | fill lightens one step | 2px `{colors.focus}` ring | bevel inverts to inset | `{colors.platinum}` fill, `{colors.muted-indigo}` label | label replaced by a 3-dot progress glyph; chip stays sized | n/a | ring in `{colors.error}` when the form it submits failed validation |
| `button-secondary` | `{colors.carbon}` slab, white label | halftone texture brightens | 2px `{colors.focus-on-dark}` ring (it sits on carbon) | inset bevel | 50% opacity slab, `{colors.muted-indigo}` label | 3-dot glyph replaces the leading icon | n/a | n/a |
| `button-icon-arrow` / `button-arrow-chip` | `{colors.signal}` disc/chip, white chevron | disc lightens one step | 2px `{colors.focus}` ring | inset bevel | `{colors.platinum}` disc | n/a | n/a | n/a |
| `nav-bar` link | `{colors.nav-gold}` word on carbon | word brightens to `{colors.amber}` | 2px `{colors.focus-on-dark}` ring | word flattens to `{colors.canvas-soft}` | n/a | n/a | current section's word is underlined (selected) | n/a |
| `left-rail-tab` | `{colors.carbon}` tab, `{colors.canvas-soft}` rotated label | label brightens to white | 2px `{colors.focus-on-dark}` ring | tab tucks 1px further behind the chrome | n/a | n/a | selected tab's label is `{colors.amber}` | n/a |
| `text-input` / `search-field` | white fill, 1px `{colors.hairline}` border | border darkens to `{colors.chrome-indigo}` | 2px `{colors.focus}` ring, border unchanged | n/a (focus is the pressed equivalent) | `{colors.platinum}` fill, `{colors.muted-indigo}` text | n/a | n/a | 1px border swaps to `{colors.error}` with the message in `{typography.micro}` beneath |
| `select-dropdown` | white fill, 1px `{colors.carbon}` border | chevron button brightens | 2px `{colors.focus}` ring | chevron button shows inset bevel | `{colors.platinum}` fill | n/a | chosen option carries a `{colors.chrome-indigo}` check mark (selected) | border in `{colors.error}` |
| `radio-option` | 12px white dot, `{colors.hairline}` ring | ring darkens to `{colors.chrome-indigo}` | 2px `{colors.focus}` ring outside the dot | dot compresses | `{colors.platinum}` dot | n/a | selected shows a `{colors.primary}` centre fill | option row label turns `{colors.error}` when the poll was submitted empty |
| `news-row` | `{colors.platinum}` row, `{colors.ink-soft}` headline | row lifts to `{colors.surface}` (the documented list-row highlight) | 2px `{colors.focus}` ring on the whole row | row shows inset bevel | n/a | skeleton row keeps the platinum fill with no headline text | n/a | n/a |
| `info-box`, `poll-panel`, `promo-card`, `system-tile`, `link-row-card`, `calendar-widget`, `featured-tile`, `form-panel`, `section-label-bar`, `subnav-strip`, `footer-bar`, `logo-pill`, `mascot-bubble`, `esrb-badge`, `esrb-rating-square`, `hero-panel` | static surfaces | — | ring belongs to the control inside, not the plate | — | — | panels may show a skeleton fill; badges do not | `system-tile` and `featured-tile` take the selected ring when used as a chooser | — |

Components with genuinely two states: `button-primary` and `button-primary-pressed` are the only extracted pair. `dotted-divider`, `footer-bar`, `section-label-bar` and both ESRB marks have **one** state — they are decoration or legend, never controls.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** It could not have been: in 2001 CSS
transitions and keyframe animations did not exist, so the real page's entire
motion vocabulary was the instantaneous JavaScript image-swap rollover, the
animated GIF, the full page reload between routes, and — in the heroes — a
pre-rendered motion blur baked into a JPEG. Nothing on the 2001 Nintendo.com
moved under a timing function. The table below is a **target** for a modern
reproduction of this identity, not a reconstruction of a lost behaviour, and it
is deliberately read against what the era's own design language implies rather
than against modern choreography:

- The era's state change was **binary** — one image replaced by another in a
  single frame. So the short end of the Playful scale carries the ordinary
  interactions: hover and press at `{motion.duration-instant}` and
  `{motion.duration-fast}`, close enough to the original swap that the chrome
  still feels like hardware rather than like a web page easing.
- The one thing the 2001 page genuinely implies in motion is the **beveled
  physical control**. Every chip and button is drawn as a depressible plate with
  a top highlight and a bottom shadow line; a small scale pop on press, which is
  exactly the Playful signature, is the honest animation of that drawing. This
  is why the overshoot easing is used on *enter* only and never on a hero.
- Page transitions get **no choreography at all**, because the era's route
  change was a white flash and a fresh reload. Reproducing that as a slow
  cross-fade would be a modern import; a `{motion.duration-fast}` opacity
  settle is as far as this file goes.

Per SPEC section 6, only `transform` and `opacity` animate here.
No rule in this file animates `width`, `height`, `top`, `left` or `margin` — the fixed-canvas chrome never changes its own box.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (chip, nav word, news row) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the bevel highlight layer | colour/opacity change only, `{motion.duration-reduced}`; no travel |
| Press (button, chip, radio) | `{motion.duration-fast}` | `{motion.ease-standard}` | `transform: scale(0.97)` | scale removed; the pressed fill swaps instantly |
| Focus (ring appears) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the ring | ring appears instantly, no fade |
| Page / route transition | `{motion.duration-fast}` | `{motion.ease-exit}` out, `{motion.ease-standard}` in | `opacity` only | opacity settle at `{motion.duration-reduced}`; no travel |
| Modal / drawer open | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: scale(0.96 → 1)` | opacity only at `{motion.duration-reduced}`; no scale |
| Modal / drawer close | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: scale(1 → 0.98)` | opacity only at `{motion.duration-reduced}` |
| Dropdown open (`select-dropdown`, nav disclosure) | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(-4px → 0)` | opacity only at `{motion.duration-reduced}` |
| Dropdown close | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | unchanged (already opacity only), capped at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px → 0)` | opacity only at `{motion.duration-reduced}`; no travel |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | unchanged, capped at `{motion.duration-reduced}` |
| List enter (news rows, featured tiles, system tiles) | `{motion.duration-base}`, staggered `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px → 0)` | stagger and travel removed; one shared opacity fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` | unchanged, capped at `{motion.duration-reduced}` |
| Loading (submit chip, skeleton row) | `{motion.duration-emphasis}`, looping | `{motion.ease-standard}` | `opacity` pulse on the 3-dot glyph / skeleton fill | loop frozen; a static "Loading…" label in `{typography.ui-label}` replaces the pulse |
| Hero field (brand ambience) | — | — | — | — |

Exit is shorter than its matching entrance in every row. Nothing animates on
first paint: the hero plate and its wordmark are painted, not revealed, which is
also the era-true behaviour. **There is no ambient loop in this system** — the
heroes' motion blur is baked into the photograph, so the only infinite animation
anywhere is the loader.

### `@media (prefers-reduced-motion: reduce)`

- **Removed:** every `transform` — the press scale, the modal and toast scale,
  the dropdown and list travel, and the `{motion.stagger-step}` sequencing
  (lists appear together).
- **Removed:** the looping loader pulse, replaced by a static "Loading…" label.
- **Kept:** opacity fades only, every one clamped to `{motion.duration-reduced}`
  (130ms) and never above 150ms.
- **Kept unchanged:** the instant fills and bevel swaps, which were never
  animated — the reduced-motion rendering of this file is very close to what the
  2001 page actually did.

## Accessibility

Contrast below is measured with WCAG 2.1 relative luminance from this file's own
hexes. The extracted brand values are frozen; where a real pair fails, it is
named here rather than corrected.

### Measured contrast — key pairs

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` #21242e on `{colors.canvas}` #7a8aba | 4.55:1 | 4.5 | Pass (by 0.05 — see Known Gaps) |
| `{colors.ink}` on `{colors.surface}` #ffffff | 15.48:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.platinum}` #dedede | 11.51:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.periwinkle}` #8ba1d4 | 6.01:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.lavender}` #acace7 | 7.23:1 | 4.5 | Pass |
| `{colors.ink-soft}` on `{colors.surface}` | 7.6:1 | 4.5 | Pass |
| `{colors.ink-soft}` on `{colors.platinum}` | 5.65:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.carbon}` | 15.48:1 | 4.5 | Pass |
| `{colors.nav-gold}` on `{colors.carbon}` | 5.68:1 | 4.5 | Pass |
| `{colors.canvas-soft}` on `{colors.carbon}` (footer, rail tabs) | 8.1:1 | 4.5 | Pass |
| `{colors.carbon}` on `{colors.amber}` | 7.7:1 | 4.5 | Pass |
| `{colors.carbon}` on `{colors.signal}` | 6.45:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.primary}` #e60012 | 4.8:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.systems-teal}` | 6.64:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.games-red}` | 7.04:1 | 4.5 | Pass |
| `{colors.hairline}` on `{colors.surface}` (input border) | 6.09:1 | 3.0 | Pass |
| `{colors.hairline}` on `{colors.platinum}` | 4.52:1 | 3.0 | Pass |
| `{colors.muted-indigo}` on `{colors.platinum}` (`dotted-divider`'s real ground) | 4.23:1 | 3.0 | Pass |

### Real failures, stated plainly

The 2001 interface puts cool indigo ink and cool indigo hairlines on a
mid-luminance periwinkle body. That combination cannot reach AA, and these hexes
are extracted facts, so they are reported, not repaired:

| Foreground / Background | Ratio | Required | Note |
|---|---|---|---|
| `ink-soft` #3d4f97 on `canvas` #7a8aba | **2.23:1** | 4.5 | Chrome Indigo as secondary text directly on the periwinkle body fails AA. In the real layout this ink appears on `{colors.platinum}` (5.65:1) and `{colors.surface}` (7.6:1), where it passes; on bare canvas it does not. |
| `muted-indigo` #60619c on `canvas` #7a8aba | **1.67:1** | 4.5 | Muted Indigo is recessed/inactive chrome, not a text tone. As text on canvas it fails badly; it is scoped in this file to the `dotted-divider` stroke and inactive tab fills. |
| `hairline` #5a5f8c on `canvas` #7a8aba | **1.79:1** | 3.0 | The blended bevel divider fails the 3:1 boundary minimum against the periwinkle body. It is decoration there — the seam between plates, legible only as a tonal shift. Where the hairline does real boundary work, it is on white or platinum (6.09:1 and 4.52:1), which pass; so no parallel accessible border token is added, because the palette already owns a passing tone for that job. |
| `error` #e60012 on `canvas` #7a8aba | **1.41:1** | 4.5 | Nintendo Red as *text* on the periwinkle body fails AA. The brand red is a fill and a logo colour, not an ink; validation messages must be set on `{colors.surface}` (4.8:1) or in `{colors.ink}` with a red border. |
| `button-submit` white on `{colors.signal}` #f68d1f | **2.4:1** | 4.5 | Signal Orange with a white label is the brand's commit button and fails AA. `{colors.carbon}` on the same orange measures 6.45:1 and would pass, but the white label is the extracted fact. |
| `button-icon-arrow` white chevron on `{colors.signal}` | **2.4:1** | 4.5 (3.0 as a non-text glyph) | Fails either threshold. The round orange "go" disc is the signature forward affordance; its white chevron is genuinely low-contrast. |
| `button-arrow-chip` white chevron on `{colors.signal}` | **2.4:1** | 4.5 (3.0 as a non-text glyph) | Same pair as above, in the 18px headline chip. |
| `hero-panel` white `{typography.display}` on `{colors.lavender}` #acace7 | **2.14:1** | 3.0 (44px/900 large text) | A genuine failure, not a binding error: lavender is a real painted field and the wordmark is really white on it. The carbon outline and hard drop shadow carried legibility in 2001 and earn no WCAG credit. The other two hero tints pass (6.64:1 and 7.04:1). |

### Focus ring visibility, per surface

Both rings are prescribed; neither existed in 2001. Each is drawn **2px outside
the control with a 1px offset**, so it is judged against the surface behind the
control.

| Surface | Ring drawn | Ratio | Required |
|---|---|---|---|
| `{colors.canvas}` #7a8aba | `{colors.focus}` | 4.17:1 | 3.0 |
| `{colors.canvas-soft}` #9fbee7 | `{colors.focus}` | 7.43:1 | 3.0 |
| `{colors.surface}` #ffffff | `{colors.focus}` | 14.19:1 | 3.0 |
| `{colors.platinum}` #dedede | `{colors.focus}` | 10.55:1 | 3.0 |
| `{colors.periwinkle}` #8ba1d4 | `{colors.focus}` | 5.51:1 | 3.0 |
| `{colors.lavender}` #acace7 | `{colors.focus}` | 6.63:1 | 3.0 |
| `{colors.ice}` #c0d5e6 | `{colors.focus}` | 9.4:1 | 3.0 |
| `{colors.amber}` #ecab37 chip fill behind a ring | `{colors.focus}` | 7.06:1 | 3.0 |
| `{colors.signal}` #f68d1f | `{colors.focus}` | 5.91:1 | 3.0 |
| `{colors.nav-gold}` #e48600 | `{colors.focus}` | 5.21:1 | 3.0 |
| `{colors.carbon}` #21242e command layer | `{colors.focus-on-dark}` | 7.7:1 | 3.0 |

`{colors.focus}` on `{colors.carbon}` measures only 1.09:1, which is exactly why
the second ring exists; `{colors.focus-on-dark}` on the light chrome measures
1.05–2.01:1 and must never be used there. The two rings separate from each other
at 7.06:1, so a composite ring is unnecessary. Over a full-bleed hero
photograph, which has no measurable colour, draw `{colors.focus}` with a 1px
`{colors.on-primary}` outer edge.

### Minimum tap target

The original is mouse-only and its controls are 18–28px tall
(`{components.button-primary}` ~22px, `{components.button-icon-arrow}` 22px,
`{components.button-arrow-chip}` 18px, `{components.radio-option}` 12px,
`{components.nav-bar}` 28px) — every one below the 44×44px minimum. A modern
reproduction must grow the hit area with transparent padding rather than the
painted chip, so the dense chrome proportions survive. **No tap target was
measured on a rendered page**; these are the declared sizes in this file's own
`components:` block.

### Reduced motion

Covered in full under *Motion & Animation*: all travel and scale removed, all
stagger removed, the loader loop frozen, opacity fades kept at
`{motion.duration-reduced}` (130ms).

### Other accessibility facts

- Colour alone carries wayfinding in this system: warm = act, cool = chrome.
  Arrow glyphs and uppercase labels back it up, so meaning does not depend on
  hue alone — but `{colors.signal}` and `{colors.amber}` are distinguished from
  each other **only** by hue, which no one with a warm-hue deficiency will see.
- The `{typography.micro}` role is 10px and `{typography.ui-label}` is 11px.
  Both are below the 12px floor most guidance asks for, and both are used for
  real content (footer, calendar cells, button labels), not decoration.
- `{typography.body}` at 12px/1.4 on `{colors.platinum}` and `{colors.surface}`
  is the file's own reading surface and measures 11.51:1 and 15.48:1.

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
| `{colors.error}` (`#e60012`) on `{colors.platinum}` (`#dedede`) | 3.57:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Build every region as a **beveled plate**: a `{colors.canvas}` body with a brighter top edge and a `{colors.chrome-indigo}` shadow line beneath. The "assembled machine" feel depends on it.
- Reserve warm color for **wayfinding only** — `{colors.nav-gold}` for nav words, `{colors.amber}` for utility/badges, `{colors.signal}` for forward/Submit. Cool chrome never carries action color.
- Keep structural labels **uppercase Arial Bold with 0.5px tracking** (`{typography.ui-label}`) — it is the silkscreen-legend voice of the whole system.
- Render hero wordmarks as **outlined + drop-shadowed `{typography.display}`** over full-bleed photographic fields tinted per page.
- Use `{colors.carbon}` with halftone texture for the **command layer** (nav, right rail, footer) to separate "system controls" from "content."
- Let panels **butt together** with thin bevel seams; density is the intended texture.
- Default corners to **sharp/chamfered** (`{rounded.none}`); spend roundness only on the logo pill, radio dots, and circle-arrow badges.

### Don't
- Don't soften every corner — turning the sharp chrome into a uniformly rounded card system erases the manufactured-faceplate identity.
- Don't introduce a **soft blurred drop-shadow** elevation language; depth here is hard bevels and pictorial photography, not Material elevation.
- Don't let `{colors.signal}` and `{colors.amber}` bleed into decorative use — warm color must always mean "act here."
- Don't add accent colors outside the page-tint heroes (`{colors.systems-teal}`, `{colors.games-red}`); the steady-state chrome is strictly cool periwinkle + carbon.
- Don't widen body copy or whitespace into an airy modern layout; the packed, fixed-canvas density is the brand.
- Don't flatten the dual-nav structure (gold primary words over the pale secondary strip) into one bar — the layered command hierarchy is signature.
- Don't render hero or system wordmarks as flat text; without the outline + shadow they lose the box-art reference entirely.

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Desktop (only) | ~780–830px fixed | The native, sole target — a fixed-width application-style layout |
| Narrow window | < 780px | Horizontal scroll (no reflow); the table layout does not collapse |

This is a **pre-responsive, fixed-canvas** design. It was authored for a single desktop window size and does not reflow. A faithful *modern* re-implementation would preserve the fixed chrome metaphor on desktop and, below ~720px, stack the right action rail beneath the content column and collapse the dual nav bars into a single carbon bar with a disclosure toggle.

### Touch Targets
Not a consideration in the original (mouse-only era); buttons and chips are 18–28px tall. A modern port must enlarge the `{components.button-primary}`, `{components.button-icon-arrow}`, and `{components.radio-option}` hit areas to a 44×44px minimum.

### Collapsing Strategy
On a modern narrow viewport: dual nav bars → single carbon bar + menu disclosure; two-column body → single stacked column with the right rail moving below content; the left rotated-tab strip → a horizontal scroll chip row or removed; fixed hero → fluid full-bleed hero retaining the outlined wordmark.

### Image Behavior
Hero fields are **full-bleed photographic plates** clipped to the panel's beveled rectangle; featured-site and game tiles are fixed-pixel thumbnails (~95×60px) in a tight grid. No lazy loading (era predates it). Product renders sit on textured backdrops rather than transparent cutouts.

## Known Gaps

- **No motion was extracted.** The entire *Motion & Animation* section is
  prescribed. CSS transitions and keyframes did not exist in 2001, so the real
  page's only motion was instant image-swap rollovers, animated GIFs and full
  page reloads. Treat every duration and easing in this file as a target for a
  modern reproduction, never as a recovered value.
- **No focus ring was extracted.** `{colors.focus}` #13275e and
  `{colors.focus-on-dark}` are both prescribed. The original relied on the
  browser's default dotted outline, which it never styled.
- **No state ladder was extracted** beyond the depressed-bevel chip
  (`{components.button-primary-pressed}`). The *Interaction States* table is
  prescribed, as its own note says. Whether the 2001 site used JavaScript
  rollover swaps on the nav words is not recoverable from this document.
- **`{colors.ink}` on `{colors.canvas}` passes at 4.55:1 — by 0.05.** Any
  rendering that lightens the ink, applies opacity, or antialiases 12px body
  copy on the periwinkle body will drop it below AA in practice. Body copy
  belongs on `{colors.platinum}` or `{colors.surface}`, which is what the
  original does.
- **`{colors.sky}` and `{colors.canvas-soft}` are the same hex** (#9fbee7), kept
  as a documented alias pair from the extraction. Not de-duplicated here, since
  both names appear in the prose.
- **`{colors.carbon}` and `{colors.ink}` are the same hex** (#21242e) with two
  jobs — command-layer fill and primary ink. Intentional, and both names are
  load-bearing in the prose.
- **No shadow group.** Correct for this file: elevation is bevel simulation and
  the prose states no `rgba(...)` blur values, so there is nothing for a
  `shadow:` token to carry.
- **Not measurable from a document:** tap-target size on a rendered page,
  horizontal overflow at the ~780px fixed width, clipping of the rotated
  left-rail tabs, the halftone texture's actual dot pitch, and the real
  letter-spacing of the display wordmarks (they are bespoke logotypes, not set
  type).
- **Hero photography has no measurable colour.** The three page tints are
  documented, but the photographs sitting on them are not, so no contrast
  statement about type over the imagery is possible.
- **Chamfer geometry is described, not specified.** The prose says the largest
  panels are cut at 45°, but no chamfer size token exists; the `rounded:` ladder
  cannot express it.
