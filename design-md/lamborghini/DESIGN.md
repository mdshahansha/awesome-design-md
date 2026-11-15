---
version: alpha
name: Lamborghini-design-analysis
description: A cathedral of darkness — true black (#000000) surfaces holding white LamboType display headlines in extreme uppercase, with Lamborghini Gold (#FFC000) as the sole chromatic signal, reserved for primary CTAs. Zero border-radius everywhere except toggle switches. Depth is built by lightening the black rather than by shadow, and full-viewport video carries all emotional weight. Every token below is read from this file's own prose; the motion group is prescribed, not measured.

colors:
  canvas: "#000000"
  surface-card: "#202020"
  surface-deep: "#181818"
  surface-light: "#F8F8F8"
  surface-light-alt: "#E6E6E6"
  overlay-strong: rgba(0,0,0,0.7)
  overlay-mid: rgba(0,0,0,0.5)
  overlay-soft: rgba(0,0,0,0.25)
  ink: "#FFFFFF"
  ink-dark: "#313131"
  body-soft: "#F5F5F5"
  muted: "#7D7D7D"
  text-secondary: "#666666"
  body-muted: "#555555"
  on-light: "#494949"
  steel: "#969696"
  accent: "#FFC000"
  accent-hover: "#917300"
  accent-text: "#FFCE3E"
  on-accent: "#000000"
  info: "#29ABE2"
  link-hover: "#3860BE"
  action-teal: "#1EAEDB"
  border: "#202020"
  border-strong: "#7D7D7D"
  border-switch: "#DDDDDD"
  border-ghost: rgba(255,255,255,0.5)
  focus: "#3866D8"

typography:
  display-hero:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 120px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: normal
  display-2:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 1.13
    letterSpacing: normal
  section-title:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 54px
    fontWeight: 400
    lineHeight: 1.19
    letterSpacing: normal
  sub-section:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: normal
  feature-heading:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 27px
    fontWeight: 400
    lineHeight: 1.37
    letterSpacing: normal
  card-title:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    letterSpacing: normal
  body-large:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: normal
  body:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal
  button-large:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal
  button-standard:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 14.4px
    fontWeight: 300
    lineHeight: 1
    letterSpacing: 0.2px
  button-small:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.2px
  caption:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: -0.42px
  nav-label:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    letterSpacing: normal
  label:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.83
    letterSpacing: 0.96px
  micro:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.225px

spacing:
  micro: 2px
  fine: 4px
  hair: 5px
  xs: 8px
  sm: 10px
  sm-alt: 12px
  md: 15px
  md-alt: 16px
  lg: 20px
  xl: 24px
  xxl: 32px
  3xl: 40px
  section: 48px
  section-lg: 56px

rounded:
  none: 0px
  hairline: 1px
  badge: 2px
  switch: 20px

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
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-large}"
    rounded: "{rounded.none}"
    padding: 24px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-standard}"
    rounded: "{rounded.none}"
    padding: 16px
    borderColor: "{colors.border-ghost}"
  button-white-filled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-large}"
    rounded: "{rounded.none}"
    padding: 24px
  button-black-filled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-large}"
    rounded: "{rounded.none}"
    padding: 24px
  button-gray:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-small}"
    rounded: "{rounded.none}"
    padding: 16px
  badge:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.badge}"
    padding: 8px
  card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.feature-heading}"
    rounded: "{rounded.none}"
    padding: 24px
  card-news:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 24px
  card-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.on-light}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 24px
  top-nav:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    rounded: "{rounded.none}"
  hero-video:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-hero}"
    rounded: "{rounded.none}"
    padding: 40px
  pause-button-hex:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    size: 48px
  progress-bar:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 1px
  section-divider:
    backgroundColor: "{colors.border}"
    rounded: "{rounded.none}"
    height: 1px
  switch:
    backgroundColor: transparent
    rounded: "{rounded.switch}"
    borderColor: "{colors.border-switch}"
  modal-overlay:
    backgroundColor: "{colors.overlay-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
  cookie-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    borderColor: "{colors.border-strong}"
    padding: 24px
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.body-soft}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 56px
---

# Design System Inspired by Lamborghini

## Overview

Lamborghini's website is a cathedral of darkness — a digital stage where jet-black surfaces stretch infinitely and every element emerges from the void like a machine under a spotlight. The page is almost entirely black. Not dark gray, not near-black — true, uncompromising black (`{colors.canvas}` — #000000) that saturates the viewport and refuses to yield. Into this abyss, white type (`{colors.ink}`) and Lamborghini Gold (`{colors.accent}`) are deployed with surgical precision, creating a visual language that feels like walking through a nighttime motorsport event where every surface absorbs light except the things that matter.

The hero is a full-viewport video — dark, cinematic, immersive — showing event footage or vehicle reveals with the Lamborghini bull logo floating ethereally above. The navigation is minimal: a centered bull logo, a "MENU" hamburger on the left, and search/bookmark icons on the right, all rendered in white against the black canvas. There are no borders, no visible nav containers, no background color on the header — just white marks floating in darkness. The overall mood is nocturnal luxury: exclusive, theatrical, and deliberately intimidating. Each section transition is a scroll through darkness into the next revelation.

Typography is the voice of this darkness. LamboType — a custom Neo-Grotesk typeface created by Character Type and design agency Strichpunkt — is used for everything from 120px uppercase display headlines to 10px micro labels. Its distinctive 12° angled terminals are inspired by the aerodynamic lines of Lamborghini's super sports cars, and its proportions range from Normal to Ultracompressed width. Headlines SHOUT in uppercase at enormous scales with tight line-heights (0.92 at 120px), creating dense blocks of text that feel stamped from steel. The typeface carries hexagonal geometric DNA — constructed from hexagons, three-armed stars, and circles — that echoes throughout the interface in the hexagonal pause button and UI icons. Built on Bootstrap grid with 68 Element Plus/UI components, the technical infrastructure is substantial beneath the theatrical surface.

**Key Characteristics:**
- True black (`{colors.canvas}`) dominant surfaces with white and gold as the only relief colors
- LamboType custom Neo-Grotesk font with 12° angled terminals inspired by aerodynamic car lines
- Lamborghini Gold (`{colors.accent}`) as the sole accent color — used exclusively for primary CTA buttons
- All-uppercase display typography at extreme scales (120px, 80px, 54px) with tight line-heights
- Full-viewport video heroes with cinematic event/vehicle content
- Zero border-radius on buttons — sharp, angular, uncompromising rectangles
- Hexagonal motifs in UI elements (pause button, icon system) echoing brand geometry
- Bootstrap grid system + Element Plus/UI 68 components underneath
- Transparent ghost buttons with white borders at 50% opacity (`{colors.border-ghost}`) as the secondary CTA pattern

## Colors

### Primary
- **Lamborghini Gold** (`{colors.accent}` — `#FFC000`): The signature accent color — a warm, saturated amber-gold (rgb 255, 192, 0) used exclusively for primary action buttons ("Discover More", "Tickets", "Start Configuration"). The only chromatic color in the entire interface, it ignites against the black canvas like a headlight cutting through night
- **Pure White** (`{colors.ink}` — `#FFFFFF`): Primary text color on dark surfaces, logo rendering, nav elements, and light-mode button fills — the voice that speaks from the darkness

### Secondary & Accent
- **Dark Gold** (`{colors.accent-hover}` — `#917300`): Hover/pressed state for gold buttons — a deep amber (rgb 145, 115, 0) that darkens the gold to signal interaction
- **Gold Text** (`{colors.accent-text}` — `#FFCE3E`): Slightly lighter gold variant (rgb 255, 206, 62) used for inline text accents and highlighted labels
- **Cyan Pulse** (`{colors.info}` — `#29ABE2`): Electric blue-cyan (rgb 41, 171, 226) appearing as an informational accent and interactive element highlight
- **Link Blue** (`{colors.link-hover}` — `#3860BE`): Medium blue (rgb 56, 96, 190) used universally for link hover states across all text colors. On the black canvas this is a **real AA failure for link text** — see Accessibility

### Surface & Background
- **Absolute Black** (`{colors.canvas}` — `#000000`): The dominant surface color — used for page background, hero sections, header, footer, and most containers
- **Charcoal** (`{colors.surface-card}` — `#202020`): Elevated dark surface (rgb 32, 32, 32) — the primary "dark gray" for cards, panels, and text containers sitting above the black canvas
- **Dark Iron** (`{colors.surface-deep}` — `#181818`): Subtle surface variant (rgb 24, 24, 24) — barely distinguishable from black, used for footer and deep sections
- **Overlay Black** (`{colors.overlay-strong}` — `rgba(0,0,0,0.7)`): Semi-transparent overlay for modals and video dimming
- **Near White** (`{colors.surface-light}` — `#F8F8F8`): Rare light surface (rgb 248, 248, 248) for content blocks in white-mode sections
- **Mist** (`{colors.surface-light-alt}` — `#E6E6E6`): Light gray surface for secondary light-mode containers

### Neutrals & Text
- **Pure White** (`{colors.ink}` — `#FFFFFF`): Primary text on dark backgrounds — headlines, body, nav labels
- **Smoke** (`{colors.body-soft}` — `#F5F5F5`): Secondary text on dark surfaces — slightly softer than pure white
- **Graphite** (`{colors.on-light}` — `#494949`): Dark gray text on light surfaces (rgb 73, 73, 73) — only ever drawn on `{colors.surface-light}` / `{colors.surface-light-alt}`
- **Ash** (`{colors.muted}` — `#7D7D7D`): Mid-range gray for muted text, timestamps, and metadata (rgb 125, 125, 125). Clears AA on the black canvas, **fails on charcoal**
- **Steel** (`{colors.steel}` — `#969696`): Lighter gray used for disabled text, subtle labels, and the gray neutral button/badge fill (rgb 150, 150, 150)
- **Slate** (`{colors.text-secondary}` — `#666666`): Alternative mid-gray for secondary content — **fails AA on both dark surfaces**
- **Iron** (`{colors.body-muted}` — `#555555`): Dark mid-gray for body text variants — **fails AA on both dark surfaces**
- **Shadow** (`{colors.ink-dark}` — `#313131`): Very dark gray described on the live site as text on dark surfaces where white is too strong. It is **not legible as text** on either dark surface; treat it as a decorative or disabled-only tone

### Semantic & Accent
- **Cyan Pulse** (`{colors.info}` — `#29ABE2`): Used for informational highlights and interactive feedback
- **Link Blue** (`{colors.link-hover}` — `#3860BE`): Universal hover state for all hyperlinks
- **Teal Action** (`{colors.action-teal}` — `#1EAEDB`): Button hover background for transparent/ghost variants (rgb 30, 174, 219)

### Borders
- **Section hairline** (`{colors.border}` — `#202020`): The extracted 1px bottom border used for section dividers. Against the canvas it is **decoration only** — never the sole boundary of a control
- **Cookie-banner border** (`{colors.border-strong}` — `#7D7D7D`): The strongest boundary the live site defines — the parallel accessible token, used wherever a boundary must be perceivable
- **Switch border** (`{colors.border-switch}` — `#DDDDDD`): 1px border on toggle switches
- **Ghost border** (`{colors.border-ghost}` — `rgba(255,255,255,0.5)`): 1px white at 50% opacity on secondary CTAs

### Focus
- **Focus ring** (`{colors.focus}` — `#3866D8`): **Prescribed, not extracted.** The live site documents only a black outline on the ghost button, which is invisible on a black canvas. This ring is Link Blue (`#3860BE`) lifted in luminance until it clears 3:1 against all four surface polarities this file defines *and* the gold accent fill. One mid-luminance ring is used rather than a light/dark pair because this file carries three surface polarities plus a near-white light mode; the measured ratios are in Accessibility.

### Gradient System
- No explicit gradients in the color palette — the dark-to-light progression is achieved through surface layering: `#000000` → `#181818` → `#202020` → `#494949` → `#7D7D7D`
- Video heroes use natural atmospheric gradients from the content itself
- Top-of-page gradient: subtle dark-to-darker fade at the edges of full-bleed imagery

## Typography

### Font Family
- **Display & UI**: `LamboType`, Roboto, Helvetica Neue, Arial — custom Neo-Grotesk typeface by Character Type for Lamborghini's 2024 brand refresh. Available in widths from Normal to Ultracompressed and weights from Light (300) to Black. Features 12° angled terminals inspired by aerodynamic car geometry, hexagonal construction logic, and support for 200+ languages including Latin, Cyrillic, and Greek
- **Fallback/UI**: `Open Sans` — used for some button/form contexts as system fallback
- **No italic variants** observed on the marketing site — the brand voice is always upright

### Hierarchy

| Role | Token | Size | Weight | Line Height | Letter Spacing | Notes |
|------|-------|------|--------|-------------|----------------|-------|
| Hero Display | `{typography.display-hero}` | 120px (7.50rem) | 400 | 0.92 | normal | LamboType, uppercase, maximum impact |
| Display 2 | `{typography.display-2}` | 80px (5.00rem) | 400 | 1.13 | normal | LamboType, uppercase, major section titles |
| Section Title | `{typography.section-title}` | 54px (3.38rem) | 400 | 1.19 | normal | LamboType, uppercase |
| Sub-section | `{typography.sub-section}` | 40px (2.50rem) | 400 | 1.15 | normal | LamboType, uppercase |
| Feature Heading | `{typography.feature-heading}` | 27px (1.69rem) | 400 | 1.37 | normal | LamboType, uppercase |
| Card Title | `{typography.card-title}` | 24px (1.50rem) | 400 | — (unrecorded) | normal | LamboType — line height absent from the source, see Known Gaps |
| Body Large | `{typography.body-large}` | 18px (1.13rem) | 400 | 1.56 | normal | LamboType, mixed case and uppercase variants |
| Body / UI | `{typography.body}` | 16px (1.00rem) | 400/700 | 1.50 | normal/0.16px | LamboType, primary body text |
| Button Large | `{typography.button-large}` | 16px (1.00rem) | 400 | 1.50 | normal | Gold CTA buttons |
| Button Standard | `{typography.button-standard}` | 14.4px (0.90rem) | 300/700 | 1.00 | 0.14–0.2px | LamboType, uppercase, ghost buttons |
| Button Small | `{typography.button-small}` | 13px (0.81rem) | 300/500 | 1.20 | 0.13–0.2px | LamboType, compact button variant |
| Caption | `{typography.caption}` | 14px (0.88rem) | 600/700 | 1.14–1.50 | -0.42px | LamboType, uppercase, negative tracking |
| Nav Label | `{typography.nav-label}` | 14px (0.88rem) | 400 | — (unrecorded) | normal | The "MENU" label beside the hamburger |
| Label | `{typography.label}` | 12px (0.75rem) | 400/500 | 1.83 | 0.96px | LamboType, uppercase badges and micro labels |
| Micro | `{typography.micro}` | 10px (0.63rem) | 400 | 1.00–2.00 | 0.225px | LamboType, uppercase, smallest text |

Where the source records a range, the token carries the lower bound (caption 1.14, micro 1.00) and the range stays in this table. Where the source records a weight pair, the token carries the first value.

### Principles
- **ALL-CAPS is the default voice**: Display and feature headings are universally uppercase. This creates a shouting, commanding tone that matches the brand's aggression
- **Extreme scale range**: From 120px heroes to 10px micro labels — a 12:1 ratio that creates dramatic visual hierarchy
- **Tight line-heights at scale**: Display sizes use 0.92-1.19 line-height, creating dense, compressed blocks of type that feel stamped rather than typeset
- **Weight 400 dominates**: Unlike many design systems that use bold for emphasis, Lamborghini's regular weight carries the headlines — the typeface itself is so distinctive it doesn't need weight variation
- **Negative tracking on captions**: -0.42px letter-spacing on 14px captions creates a compressed, technical aesthetic
- **Positive tracking on micro text**: +0.225px at 10px ensures legibility at the smallest sizes
- **Single typeface discipline**: LamboType handles everything — the 12° angled terminals and hexagonal geometry provide visual coherence across all sizes
- **Body text on this file's own surfaces**: on `{colors.canvas}`, body copy is `{colors.ink}` or `{colors.body-soft}`, both far above AA. `{colors.muted}` clears AA on the canvas but **not** on `{colors.surface-card}`, so body copy on a charcoal card must step up to `{colors.body-soft}`. On `{colors.surface-light}`, body copy is `{colors.on-light}`

## Components

All buttons use **zero border-radius** (`{rounded.none}`) — sharp, angular rectangles that echo the aggressive lines of Lamborghini vehicles.

### Buttons

**Gold Accent CTA** (`{components.button-accent}`) — The primary action:
- Default: bg `{colors.accent}`, text `{colors.on-accent}`, padding `{spacing.xl}`, `{typography.button-large}`, radius `{rounded.none}`, no border
- Hover: bg `{colors.accent-hover}` (Dark Gold), darkens significantly — the black label still clears AA
- Active/pressed: bg `{colors.accent-hover}`, no transform (see Don'ts)
- Focus-visible: 2px `{colors.focus}` ring with a 2px offset onto `{colors.canvas}`
- Disabled, loading, selected and error: **no such state exists on the live site** — this is a marketing CTA with four states only
- Class: `btn-accent btn-large` · Used for: "Discover More", "Tickets", "Start Configuration"

**Transparent Ghost** (`{components.button-ghost}`) — The secondary action on dark backgrounds:
- Default: bg transparent, text `{colors.ink}`, border 1px solid `{colors.border-ghost}`, padding `{spacing.md-alt}`, opacity 0.5
- Hover: bg `{colors.action-teal}` (Teal Action), text white, opacity 0.7 — **a real AA failure**, see Accessibility
- Active/pressed: bg `{colors.action-teal}` at full opacity
- Focus-visible: the live site specifies bg `{colors.action-teal}`, border 1px solid `{colors.canvas}`, outline 2px solid `{colors.canvas}` — a black ring on a black page, invisible. Replace the outline with 2px `{colors.focus}`
- Disabled, loading, selected and error: not documented on the live site
- Used for: secondary CTAs on hero sections and dark panels

**White Filled** (`{components.button-white-filled}`) — Light-mode primary:
- Default: bg `{colors.ink}`, text `{colors.surface-card}`, no border
- Hover: opacity 0.7 · Active/pressed: opacity 0.9 · Focus-visible: 2px `{colors.focus}`
- Disabled, loading, selected and error: not documented
- Used for: CTAs on dark sections where gold isn't appropriate

**Black Filled** (`{components.button-black-filled}`) — Dark filled variant:
- Default: bg `{colors.canvas}`, text `{colors.surface-card}` — **unusable as recorded**, see Accessibility and Known Gaps
- Hover, active/pressed and focus-visible: same geometry as White Filled, ring in `{colors.focus}`
- Disabled, loading, selected and error: not documented
- Used for: Inverted CTA on light sections

**Gray Neutral** (`{components.button-gray}`) — Subtle action:
- Default: bg `{colors.steel}`, text `{colors.surface-card}`
- Hover: opacity 0.8 · Active/pressed: opacity 0.9 · Focus-visible: 2px `{colors.focus}`
- Disabled: `{colors.steel}` at 40% with an `{colors.ink-dark}` label · loading, selected and error: not documented
- Used for: secondary/tertiary actions, badge-like buttons

### Cards & Containers
- `{components.card}` — Background `{colors.surface-card}` (Charcoal) on black canvas, or `{colors.canvas}` on lighter sections; text `{colors.ink}`
- `{components.card-news}` — Charcoal card with `{colors.muted}` body copy at `{typography.body}`: **a real AA failure** at this size, see Accessibility
- `{components.card-light}` — `{colors.surface-light}` with `{colors.on-light}` text
- Border: 1px solid `{colors.border}` bottom borders for section dividers (`{components.section-divider}`)
- Border-radius: `{rounded.none}` (completely sharp corners)
- Shadow: minimal, uses overlay opacity for depth
- Content: full-bleed photography + overlaid text in white
- States: cards are **static containers with default and hover only** — hover lifts the image to opacity 1. A card that is wholly a link also takes focus-visible, drawn as the `{colors.focus}` ring on the card edge. No active/pressed, disabled, loading, selected or error state

### Inputs & Forms
- Minimal form presence on the marketing site
- `{components.switch}` — Switch elements: border-radius `{rounded.switch}` (20px, the only rounded element), border 1px solid `{colors.border-switch}`. States: default, hover, focus-visible (2px `{colors.focus}`), selected (knob travels, track fills `{colors.accent}`), disabled (40% opacity). No loading or error state
- `{components.cookie-banner}` — Cookie banner input style: white text on black with `{colors.border-strong}` borders. States: default, hover, focus-visible and pressed on its buttons; no loading, selected or error state, since no consent choice can be invalid

### Navigation
- `{components.top-nav}` — **Desktop**: Centered bull logo, "MENU" hamburger with icon on left, search icon + bookmarks icon on right
- **Background**: Transparent (inherits black page background)
- **Sticky**: Fixed to top, floats above content
- **No visible borders or shadows** — elements float in the darkness
- **"MENU" label**: `{colors.ink}` at `{typography.nav-label}` (14px weight 400), uppercase, accompanies hamburger icon
- **Hexagonal motifs**: Pause button on hero sections uses hexagonal outline shape
- States: default, hover (opacity to 1), focus-visible (2px `{colors.focus}`), active/pressed (opacity 0.6), selected (current section underlined in `{colors.ink}`). No disabled, loading or error state

### Image Treatment
- **Hero**: Full-viewport video sections (100vh) with cinematic event/vehicle footage (`{components.hero-video}`)
- **Event photography**: Full-bleed aerial shots of Lamborghini Arena events
- **Vehicle imagery**: High-contrast studio shots on dark backgrounds, full-width
- **Aspect ratios**: Predominantly 16:9 and wider for cinematic feel
- **Dark gradient overlays**: Subtle darkening at top/bottom edges of video to ensure text legibility

### Distinctive Components
- **Hexagonal Pause Button** (`{components.pause-button-hex}`): Video control uses a hexagonal outline (matching the brand's geometric DNA from the typeface), positioned bottom-right of hero sections. States: default, hover (stroke to full opacity), active/pressed, focus-visible (2px `{colors.focus}`), selected (playing versus paused icon swap), loading (stroke pulses while the video buffers). No disabled or error state
- **Progress Bar** (`{components.progress-bar}`): Thin white line at bottom of hero sections indicating video/slide progress. **Two states only** — loading (advancing) and complete. It is not interactive, so it has no hover, focus-visible, pressed, disabled, selected or error state
- **Badge/Tag** (`{components.badge}`): bg `{colors.steel}`, text `{colors.ink}`, padding `{spacing.xs}`, `{typography.micro}`, borderRadius `{rounded.badge}` — tiny metallic pills. **Default state only**, since badges are non-interactive. The white-on-steel label is **a real AA failure** at 10px, see Accessibility
- **Modal / overlay** (`{components.modal-overlay}`): `{colors.overlay-strong}` scrim with `{colors.ink}` content. States: default and focus-visible (focus trapped, ring in `{colors.focus}`); the scrim itself has no hover, pressed, disabled, loading, selected or error state
- **Footer** (`{components.footer}`): `{colors.surface-deep}` with `{colors.body-soft}` text. Footer links: default, hover (`{colors.link-hover}`), focus-visible, active/pressed; no disabled, loading, selected or error state

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or choreography below was extracted from lamborghini.com; the values are the shared **Cinematic** profile from `theme-audit/SPEC.md` section 5, carried verbatim in the `motion:` frontmatter group so every Cinematic file in this collection behaves as a sibling.

Cinematic is the right profile here on the assignment rule's first clause: luxury automotive identity, full-viewport video heroes, sparse uppercase type and a slow reveal. Only `transform` and `opacity` are animated — never `width`, `height`, `top`, `left` or `margin`.

**One documented deviation:** this file's own Don'ts forbid scale or translate on hover ("interactions should be color-only"). Hover and press therefore animate `opacity` and `background-color` with no transform, while page transitions, modals, dropdowns, toasts and lists keep the profile's travel.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `background-color` (no transform — brand rule) | Same crossfade, capped at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` only (no scale pop — brand rule) | Unchanged; already at or under `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Ring appears instantly and is never suppressed |
| Page / route transition | `{motion.duration-emphasis}` | `{motion.ease-enter}` | `opacity` 0→1, `transform: translateY(24px)`→0 | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(32px)`→0 | Travel removed; scrim fades at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-base}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| List enter | `{motion.duration-base}`, staggered by `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px)`→0 | Stagger and travel removed; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading | 1600ms, infinite | linear | `transform: scaleX()` on `{components.progress-bar}`, `opacity` pulse on the hex pause button | Loader frozen; a static determinate bar remains |
| Hero reveal, then continuous slow scale — **stated here as deliberate brand ambience** | `{motion.duration-emphasis}` on reveal | `{motion.ease-enter}` | `opacity`, `transform: scale(1)`→`scale(1.04)` | Ambience frozen at `scale(1)`; video paused and its poster frame shown |

Exit is always shorter than its matching entrance. Nothing animates on first paint in a way that delays content: hero type fades in after the video's first frame has painted and never gates it.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: every translate, every scale, the hero's continuous scale
     ambience, the progress-bar loader, and the list stagger. */
  /* Kept: opacity fades only, capped at {motion.duration-reduced} (150ms),
     plus the focus ring, which appears instantly and is never removed. */
  *, *::before, *::after {
    transition-property: opacity;
    transition-duration: 150ms; /* {motion.duration-reduced} */
    animation: none;
  }
}
```

## Accessibility

Every ratio below is computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. **The extracted brand values are frozen: the failures listed here are real failures of the live Lamborghini interface, disclosed rather than corrected.**

### Measured contrast — key pairs

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `ink` #FFFFFF on `canvas` #000000 | 21.00:1 | 4.5:1 | Pass |
| `ink` #FFFFFF on `surface-card` #202020 | 16.29:1 | 4.5:1 | Pass |
| `body-soft` #F5F5F5 on `canvas` | 19.26:1 | 4.5:1 | Pass |
| `body-soft` #F5F5F5 on `surface-card` | 14.94:1 | 4.5:1 | Pass |
| `muted` #7D7D7D on `canvas` | 5.10:1 | 4.5:1 | Pass |
| `muted` #7D7D7D on `surface-card` | 3.96:1 | 4.5:1 | **Fail — real brand failure.** Ash body copy on a charcoal card misses AA; step up to `{colors.body-soft}` |
| `text-secondary` #666666 on `canvas` | 3.66:1 | 4.5:1 | **Fail — real brand failure.** Slate is defensible only at 18.66px+/700 or 24px+, where the 3:1 large-text threshold applies |
| `text-secondary` #666666 on `surface-card` | 2.84:1 | 4.5:1 | **Fail — real brand failure.** Not usable as text on charcoal at any size |
| `body-muted` #555555 on `canvas` | 2.82:1 | 4.5:1 | **Fail — real brand failure.** Iron is a decorative tone on black, not a text tone |
| `body-muted` #555555 on `surface-card` | 2.19:1 | 4.5:1 | **Fail — real brand failure** |
| `ink-dark` #313131 on `canvas` | 1.61:1 | 4.5:1 | **Fail — real brand failure.** The source calls Shadow "text on dark surfaces"; it is effectively invisible there |
| `ink-dark` #313131 on `surface-card` | 1.25:1 | 4.5:1 | **Fail — real brand failure** |
| `on-accent` #000000 on `accent` #FFC000 | 12.79:1 | 4.5:1 | Pass |
| `on-accent` #000000 on `accent-hover` #917300 | 4.66:1 | 4.5:1 | Pass — the gold hover state holds, with little margin |
| `accent` #FFC000 on `canvas` | 12.79:1 | 3:1 non-text | Pass |
| `accent-text` #FFCE3E on `canvas` | 14.15:1 | 4.5:1 | Pass |
| `info` #29ABE2 on `canvas` | 8.02:1 | 4.5:1 | Pass |
| `link-hover` #3860BE on `canvas` | 3.58:1 | 4.5:1 | **Fail — real brand failure.** Link Blue is the documented hover colour for every link on a black page and does not reach AA as text |
| `border` #202020 on `canvas` | 1.29:1 | 3:1 | **Fail — frozen decorative hairline.** Section dividers only; never the sole boundary of a control |
| `border` #202020 on `surface-card` | 1.00:1 | 3:1 | **Fail — invisible by construction**: the hairline and the card are the same value. Any boundary that must be seen uses `{colors.border-strong}` |
| `border-strong` #7D7D7D on `canvas` | 5.10:1 | 3:1 | Pass — the parallel accessible boundary |
| `border-switch` #DDDDDD on `canvas` | 15.46:1 | 3:1 | Pass |
| `on-light` #494949 on `surface-light` #F8F8F8 | 8.48:1 | 4.5:1 | Pass |
| `on-light` #494949 on `surface-light-alt` #E6E6E6 | 7.21:1 | 4.5:1 | Pass |
| `steel` #969696 on `canvas` as a disabled label | 7.10:1 | exempt | WCAG sets no requirement on disabled text |

### Component pairs

| Component | Measured | Required | Verdict |
|---|---|---|---|
| `button-accent` — #000000 on #FFC000 | 12.79:1 | 4.5:1 | Pass |
| `button-ghost` — #FFFFFF over the canvas | 21.00:1 | 4.5:1 | Pass at rest; see hover |
| `button-ghost` hover — #FFFFFF on `action-teal` #1EAEDB | 2.58:1 | 4.5:1 | **Fail — real brand failure.** The documented teal hover with a white label is far below AA; `{colors.on-accent}` on the same teal measures 8.13:1 |
| `button-white-filled` — #202020 on #FFFFFF | 16.29:1 | 4.5:1 | Pass |
| `button-black-filled` — #202020 on #000000 | 1.29:1 | 4.5:1 | **Fail — unusable as recorded.** The extracted spec puts charcoal text on a black fill |
| `button-gray` — #202020 on #969696 | 5.51:1 | 4.5:1 | Pass |
| `badge` — #FFFFFF on #969696 at 10px | 2.96:1 | 4.5:1 | **Fail — real brand failure.** White on steel at 10px is well below AA |
| `card-news` — #7D7D7D on #202020 at 16px | 3.96:1 | 4.5:1 | **Fail — real brand failure.** This is exactly the combination the source's own example prompt specifies |
| `card` — #FFFFFF on #202020 | 16.29:1 | 3:1 large | Pass |
| `card-light` — #494949 on #F8F8F8 | 8.48:1 | 4.5:1 | Pass |
| `footer` — #F5F5F5 on #181818 | 16.29:1 | 4.5:1 | Pass |

### Focus ring visibility on every surface this file defines

`{colors.focus}` (#3866D8) is drawn as a 2px ring with a 2px offset. Prescribed, not extracted.

| Surface it is drawn on | Measured | Required | Verdict |
|---|---|---|---|
| `canvas` #000000 | 4.06:1 | 3:1 | Pass |
| `surface-card` #202020 | 3.15:1 | 3:1 | Pass |
| `surface-deep` #181818 | 3.43:1 | 3:1 | Pass |
| `surface-light` #F8F8F8 | 4.87:1 | 3:1 | Pass |
| `surface-light-alt` #E6E6E6 | 4.14:1 | 3:1 | Pass |
| `accent` #FFC000, the gold CTA fill | 3.15:1 | 3:1 | Pass |

Over full-bleed video and photography, which has no measurable colour, the ring is two-tone: 2px `{colors.focus}` with a 1px outer edge in `{colors.ink}`. The live site's own ghost-button focus style — a black outline on a black canvas — must never be used.

### Minimum tap target
The source records gold CTAs at 48px+ with `{spacing.xl}` padding, ghost buttons at 48px+ with `{spacing.md-alt}` padding, the hamburger at roughly 48px square and the hexagonal pause button at roughly 48px. All clear the 44×44px minimum **as documented**. This is a document, not a rendered page, so no tap target was measured here.

### Reduced motion
`@media (prefers-reduced-motion: reduce)` removes every translate and scale, freezes the hero's scale ambience and the progress-bar loader, and drops the list stagger. Opacity fades remain, capped at `{motion.duration-reduced}` (150ms). The focus ring is never animated away.

## Layout

### Spacing System
- **Base unit**: `{spacing.xs}` (8px)
- **Full scale**: `{spacing.micro}` 2px, `{spacing.fine}` 4px, `{spacing.hair}` 5px, `{spacing.xs}` 8px, `{spacing.sm}` 10px, `{spacing.sm-alt}` 12px, `{spacing.md}` 15px, `{spacing.md-alt}` 16px, `{spacing.lg}` 20px, `{spacing.xl}` 24px, `{spacing.xxl}` 32px, `{spacing.3xl}` 40px, `{spacing.section}` 48px, `{spacing.section-lg}` 56px
- **Button padding**: `{spacing.md-alt}` (ghost), `{spacing.xl}` (gold accent)
- **Section padding**: `{spacing.section}`–`{spacing.section-lg}` vertical, `{spacing.3xl}` horizontal
- **Small spacing**: `{spacing.micro}`–`{spacing.hair}` for fine adjustments (badge padding, border spacing)
- The ladder is the extracted one and is **not a clean multiple of the 8px base**: 5px, 10px, 15px and 20px form a parallel 5px run beside 8/16/24/32. Both runs are real; nothing here was regularised

### Grid & Container
- **Framework**: Bootstrap grid system (container + row + col)
- **Max width**: 1440px (largest breakpoint)
- **Columns**: Standard 12-column Bootstrap grid
- **Full-bleed**: Hero sections break out of grid to fill viewport edge-to-edge
- **Content areas**: Centered within 1200px max-width containers

### Whitespace Philosophy
Lamborghini uses darkness as whitespace. The generous black expanses between content blocks serve the same function as white space in a light design — creating breathing room that elevates each element to the status of exhibit. A model name floating in the middle of a black viewport has the same visual weight as a gallery piece on a white wall. The absence of color IS the design.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Level 0 (Abyss) | `{colors.canvas}` flat | Page background, deepest layer |
| Level 1 (Surface) | `{colors.surface-deep}` or `{colors.surface-card}` | Cards, content panels, elevated sections |
| Level 2 (Overlay) | `{colors.overlay-strong}` | Modal backdrops, video dimming |
| Level 3 (Fog) | `{colors.overlay-mid}` | Lighter overlays, hover states |
| Level 4 (Mist) | `{colors.overlay-soft}` | Subtle depth hints |

**Layer separation, measured.** The ladder is deliberately near-invisible: `{colors.surface-deep}` is 1.18:1 against the canvas, `{colors.surface-card}` is 1.29:1 against the canvas, and the two surfaces are 1.09:1 against each other. These layers are **not distinguishable on their own**. On this brand the boundary is carried by the content — full-bleed photography meeting black — or by `{colors.border-strong}`, never by the surface step alone. That is a real limitation of the extracted palette, not a documentation gap.

### Shadow Philosophy
Lamborghini achieves depth through surface color layering rather than shadows. On a black canvas, traditional drop shadows are invisible — instead, the system creates elevation by shifting from absolute black to progressively lighter dark grays: `#000000` → `#181818` → `#202020` → `#494949`. This "darkness gradient" approach means that elevated elements are literally lighter than their surroundings, inverting the traditional shadow model. **Elevation is expressed one way only — surface colour.** No component mixes a shadow with a border to signal the same thing, and there is no `shadow:` token group because the file documents no shadow value.

### Decorative Depth
- Full-bleed video provides atmospheric depth through cinematic lighting
- The hexagonal pause button floats with a thin white outline stroke
- Progress bars at hero section bottoms create a subtle horizon line
- No gradients, glows, or blur effects on UI elements — the photography provides all visual richness

## Shapes

### Border Radius Scale
| Token | Value | Context |
|-------|-------|---------|
| `{rounded.none}` | 0px | Default for everything — buttons, cards, containers, images |
| `{rounded.hairline}` | 1px | Subtle span elements |
| `{rounded.badge}` | 2px | Badges, close buttons, cookie elements — barely perceptible |
| `{rounded.switch}` | 20px | Toggle switches only — the sole rounded element |

The ladder is intentionally not geometric: 0 → 1 → 2 is a near-sharp cluster and 20px is a single deliberate outlier. `{rounded.switch}` is reserved for the toggle switch and nothing else may use it.

### Geometric Motifs
- **Hexagon**: the typeface's construction logic (hexagons, three-armed stars, circles) surfaces in the hexagonal pause button and the icon system
- **Rectangle**: every container, button and image is a sharp-cut rectangle
- **1px line**: the progress bar and the section divider are the only linear shapes

## Do's and Don'ts

### Do
- Use absolute black (`{colors.canvas}`) as the primary background — never dark gray as a substitute
- Apply Lamborghini Gold (`{colors.accent}`) exclusively for primary CTA buttons — never for decorative purposes
- Set all display headings in uppercase with LamboType — the brand voice is always SHOUTING
- Use zero border-radius on buttons and cards — sharp angles are non-negotiable
- Maintain tight line-heights (0.92–1.19) on display type to create dense, architectural text blocks
- Use the transparent ghost button (white border, 50% opacity) as the secondary CTA on dark backgrounds
- Let full-viewport video/photography carry emotional weight — UI is infrastructure, not decoration
- Reserve hexagonal geometry for UI icons and the video control button
- Use weight 400 (regular) for headlines — the typeface is distinctive enough without bold emphasis
- Keep the gray palette achromatic — all neutrals are pure gray without color tinting
- Step body copy up to `{colors.body-soft}` on `{colors.surface-card}`, where `{colors.muted}` falls below AA
- Draw every focus ring in `{colors.focus}` — never the black outline the live site specifies

### Don't
- Introduce additional accent colors beyond gold — the monochrome-plus-gold system is sacred
- Apply border-radius to buttons or cards — curved edges contradict the angular vehicle aesthetic
- Use LamboType in italic or decorative styles — the brand is always upright and direct
- Add gradients to buttons or surfaces — depth comes from surface layering, not blending
- Use light backgrounds as the primary canvas — darkness is the default state, light is the exception
- Mix lowercase into display headings — the uppercase convention communicates authority and power
- Add hover animations with scale or translate — interactions should be color-only (background/opacity shifts)
- Use Open Sans for display text — LamboType must handle all visible typography
- Create busy layouts with many small elements — Lamborghini's design is about singular, bold statements
- Apply shadows to elements — on a black canvas, shadows are meaningless; use surface color shifts instead
- Never animate `width`, `height`, `top`, `left` or `margin` — `transform` and `opacity` only
- Do not set `{colors.ink-dark}`, `{colors.body-muted}` or `{colors.text-secondary}` as body text on any dark surface

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <425px | Single column, reduced type scale, stacked buttons |
| Mobile | 425-576px | Single column, hamburger nav, hero text ~40px |
| Tablet Small | 576-768px | 2-column grid begins, padding adjusts |
| Tablet | 768-1024px | 2-column layout, expanded hero, vehicle cards side-by-side |
| Desktop | 1024-1280px | Full navigation, 3+ column grids, display text at 80px |
| Desktop Large | 1280-1440px | Full layout, hero at 120px display, max-width containers |
| Wide | >1440px | Content centered, margins expand, hero fills viewport |

### Touch Targets
- Gold CTA buttons: 48px+ minimum height with `{spacing.xl}` padding (exceeds WCAG 44×44px)
- Ghost buttons: 48px+ with `{spacing.md-alt}` padding
- Hamburger menu: large touch target (~48px square)
- Hexagonal pause button: approximately 48px diameter

### Collapsing Strategy
- **Navigation**: Always hamburger-based ("MENU" + icon) — no horizontal nav expansion on any breakpoint
- **Hero video**: Maintains full-viewport height across all breakpoints, adjusting object-fit
- **Display type**: Scales from 120px (desktop) → 80px (tablet) → 54px/40px (mobile)
- **Button layout**: Side-by-side on desktop, stacks vertically on mobile
- **Grid columns**: 3-column → 2-column → 1-column progression
- **Section spacing**: Reduces from `{spacing.section-lg}` → `{spacing.3xl}` → `{spacing.xl}` vertical padding

### Image Behavior
- Hero videos use `object-fit: cover` to maintain cinematic framing at all sizes
- Vehicle images scale within their containers with maintained aspect ratios
- Event photography crops to viewport width on narrow screens
- Background images darken at edges to maintain text contrast on all viewports

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: "Lamborghini Gold (#FFC000)" — `{colors.accent}`
- Background: "Absolute Black (#000000)" — `{colors.canvas}`
- Surface: "Charcoal (#202020)" — `{colors.surface-card}`
- Heading text: "Pure White (#FFFFFF)" — `{colors.ink}`
- Body text: "Smoke (#F5F5F5)" (`{colors.body-soft}`) on cards; "Ash (#7D7D7D)" (`{colors.muted}`) only on the pure-black canvas
- Link hover: "Link Blue (#3860BE)" — `{colors.link-hover}`, below AA as text, see Accessibility
- Accent: "Cyan Pulse (#29ABE2)" — `{colors.info}`
- Border: "Pure White at 50% opacity" — `{colors.border-ghost}`; perceivable boundaries use `{colors.border-strong}`
- Focus ring: "Lifted Link Blue (#3866D8)" — `{colors.focus}`, prescribed

### Example Component Prompts
- "Create a hero section with a full-viewport black background, the model name 'TEMERARIO' in LamboType at 120px uppercase weight 400 white text with 0.92 line-height, centered vertically, with a Lamborghini Gold (#FFC000) 'Discover More' button below — sharp corners, 0px radius, 24px padding, black text"
- "Design a transparent ghost button with 1px solid white border at 50% opacity, white text at 14.4px uppercase with 0.2px letter-spacing, padding 16px, on a black background — hover state changes to Teal Action (#1EAEDB) background with 70% opacity, and the focus ring is 2px #3866D8"
- "Build a navigation bar with zero visible background on absolute black, a centered bull logo, 'MENU' text label with hamburger icon on the left, and search + bookmark icons on the right — all in white, sticky position"
- "Create a news card grid on charcoal (#202020) background with white headlines at 27px uppercase, body text in #F5F5F5 at 16px (the site's own #7D7D7D reaches only 3.96:1 here), and a white underlined 'Read More' link that turns #3860BE on hover"
- "Design a section divider using a 1px solid bottom border in #202020 on a black canvas — the elevation difference is purely through surface color shift, not shadow"

### Iteration Guide
When refining existing screens generated with this design system:
1. Focus on ONE component at a time — Lamborghini's system is extreme and every element must feel aggressive
2. Reference specific color names and hex codes from this document — the palette has only about 5 active colors
3. Use natural language descriptions, not CSS values — "sharp-cut golden rectangle" not "border-radius: 0px; background: #FFC000"
4. Describe the desired "feel" alongside specific measurements — "floating in total darkness" communicates the black canvas better than "background: #000000"
5. Remember that UPPERCASE IS THE DEFAULT — if text isn't uppercase at display sizes, it probably should be

## Known Gaps

Everything here is absent from, or unverifiable in, the source document. Nothing in this file was invented to fill one of these holes.

**Lost in the legacy-format conversion.** This file carried no frontmatter token block and used numbered headings; the token block above was built only from hexes, type values and component descriptions already present in its prose.
- **Token names.** The source named colours only in prose ("Charcoal", "Dark Iron"), so every token key above is a new name mapped onto an extracted hex. Whatever names the brand itself uses are unknown.
- **Component property coverage.** Most component descriptions gave a background and a text colour but no height, gap, border width or icon size; those keys are absent rather than guessed.
- **State coverage.** The source documented hover for two buttons and focus for one. Every other state is marked "not documented" per component instead of being invented.
- **Font weight range.** LamboType is described as Light (300) through Black, but only 300/400/500/600/700 appear against specific roles. No role carries a Black weight.
- **Shadow group.** No shadow value appears anywhere in the source, so there is no `shadow:` group. The three overlay rgba values are the only alpha compositing recorded.

**Values genuinely missing from the source:**
- `{typography.card-title}` has no recorded line height (the source table shows "—"), so the token omits `lineHeight`.
- `{typography.nav-label}` has no recorded line height; it exists only in the Navigation prose ("white text at 14px weight 400"), not in the type table.
- `{typography.caption}` and `{typography.micro}` record line-height *ranges* (1.14–1.50 and 1.00–2.00). The tokens carry the lower bound; the condition that selects the upper bound is unknown.
- `{typography.body}`, `{typography.button-standard}` and `{typography.button-small}` record weight pairs (400/700, 300/700, 300/500) and letter-spacing ranges. The tokens carry the first value; the rule that switches between them is unknown.
- The source states `border: 0px 1px solid #202020` for cards — a malformed shorthand, read here as a 1px bottom border. The real value is unverified.
- **`button-black-filled` is internally contradictory**: the source gives bg `#000000` with text `#202020` (1.29:1). It is documented as extracted and flagged in Accessibility, not silently repaired.
- `{colors.border-ghost}` is recorded as "white at 50% opacity"; its composited result over video is unmeasurable from a document.
- The light-mode half of the system (`{colors.surface-light}`, `{colors.surface-light-alt}`, `{colors.on-light}`) is described as existing, but the source specifies no light-mode component — no light card beyond the inferred `{components.card-light}`, no light nav, no light ghost button.
- **All motion values are prescribed**, not extracted. The real site's durations, easing curves and scroll choreography were never measured; the Cinematic profile was assigned from brand category, not from observed timing.
- **Not measurable from a document:** overlap, horizontal overflow, clipping, rendered tap-target size, frame rate and layout shift. The 48px tap targets above are as documented, not as rendered.
