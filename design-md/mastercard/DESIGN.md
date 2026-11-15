---
version: alpha
name: Mastercard-design-analysis
description: A warm editorial-magazine payments identity built on putty-cream paper rather than white. The canvas is Canvas Cream (#F3F0EE) and the single ink is a warm near-black (#141413) that doubles as the primary CTA fill and the footer surface; the brand's red and yellow (#EB001B / #F79E1B) appear only inside the logo mark and never as UI colour. Signal Orange (#CF4500) is reserved for consent and compliance actions, and its lighter sibling (#F37338) only draws the hand-traced orbital arcs between circular service portraits. Type is MarkForMC throughout at an unusual 450 body weight with -2% display tracking. Shape is the loudest gesture: 20px button pills, 40px stadium media frames, perfect circles for portraits and full 999px pills for navigation, with the conventional 8-12px middle ground deliberately absent.

colors:
  brand-red: "#EB001B"
  brand-yellow: "#F79E1B"
  ink: "#141413"
  ink-charcoal: "#262627"
  ink-muted: "#696969"
  ink-granite: "#555555"
  ink-graphite: "#565656"
  ink-whisper: "#D1CDC7"
  canvas-cream: "#F3F0EE"
  surface-lifted: "#FCFBFA"
  surface-white: "#FFFFFF"
  surface-bone: "#F4F4F4"
  surface-ink-footer: "#141413"
  on-ink: "#FFFFFF"
  accent-signal: "#CF4500"
  accent-signal-light: "#F37338"
  accent-clay: "#9A3A0A"
  on-accent: "#FFFFFF"
  link-blue: "#3860BE"
  watermark-ghost: "#E8E2DA"
  media-black: "#000000"
  media-slate: "#2B2B2B"
  border-ink: "#141413"
  hairline-ink-50: "rgba(20, 20, 19, 0.5)"
  border-on-ink: "rgba(255, 255, 255, 0.4)"
  focus: "#141413"
  focus-on-ink: "#F3F0EE"

typography:
  display-hero:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 64px
    letterSpacing: -1.28px
  display-section:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 44px
    letterSpacing: -0.72px
  title-card:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 28.8px
    letterSpacing: -0.48px
  subhead:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 18.2px
    letterSpacing: normal
  eyebrow:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 14px
    letterSpacing: 0.56px
    textTransform: uppercase
  body:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 450
    lineHeight: 22.4px
    letterSpacing: normal
  nav-link:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: -0.48px
  button-primary-label:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    letterSpacing: -0.32px
  button-secondary-label:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 450
    lineHeight: 20.8px
  button-consent-label:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    letterSpacing: 0.13px
  footer-link:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 450
    lineHeight: 20px
    letterSpacing: normal
  footer-column-header:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 14px
    letterSpacing: 0.56px
    textTransform: uppercase
  ghost-watermark:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 500
    letterSpacing: -2%

spacing:
  base: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  xxl: 64px
  section: 96px
  section-lg: 128px

rounded:
  xs: 3px
  sm: 6px
  md: 20px
  lg: 24px
  xl: 40px
  circle: 50%
  full: 999px

shadow:
  none: none
  level-1: "rgba(0, 0, 0, 0.04) 0px 4px 24px 0px"
  level-2: "rgba(0, 0, 0, 0.08) 0px 24px 48px 0px"
  level-3: "rgba(0, 0, 0, 0.25) 0px 70px 110px 0px"

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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas-cream}"
    typography: "{typography.button-primary-label}"
    rounded: "{rounded.md}"
    padding: 6px 24px
    border: 1.5px solid {colors.border-ink}
  button-primary-disabled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-muted}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    typography: "{typography.button-secondary-label}"
    rounded: "{rounded.md}"
    padding: 6px 24px
    border: 1.5px solid {colors.border-ink}
  button-consent:
    backgroundColor: "{colors.accent-signal}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-consent-label}"
    rounded: "{rounded.lg}"
    padding: 1px 30px
  button-consent-secondary:
    textColor: "{colors.accent-clay}"
    typography: "{typography.button-secondary-label}"
  satellite-cta:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
    height: 56px
  icon-button-circle:
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
    height: 40px
    border: 1px solid {colors.border-ink}
  hero-media-frame:
    backgroundColor: "{colors.media-black}"
    rounded: "{rounded.xl}"
    shadow: "{shadow.none}"
  portrait-card:
    rounded: "{rounded.circle}"
  carousel-pill-card:
    rounded: "{rounded.full}"
    shadow: "{shadow.level-2}"
  chip-category:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  ghost-watermark-text:
    textColor: "{colors.watermark-ghost}"
    typography: "{typography.ghost-watermark}"
  eyebrow-label:
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow}"
  nav-pill:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.full}"
    padding: 16px 40px
    shadow: "{shadow.level-1}"
  search-input-expanded:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    border: 1px solid {colors.hairline-ink-50}
  link-inline:
    textColor: "{colors.link-blue}"
    typography: "{typography.body}"
  footer:
    backgroundColor: "{colors.surface-ink-footer}"
    textColor: "{colors.on-ink}"
    padding: 100px 48px 148px
  footer-link-row:
    backgroundColor: "{colors.surface-ink-footer}"
    textColor: "{colors.on-ink}"
    typography: "{typography.footer-link}"
  country-selector:
    backgroundColor: "{colors.surface-ink-footer}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.full}"
    border: 1px solid {colors.border-on-ink}
---

# Design System Inspired by Mastercard

## Overview

Mastercard's experience reads like a warm, editorial magazine built from soft stone and signal orange. The canvas is a muted putty-cream (`#F3F0EE`) — not white, not gray, but a color that feels like the paper of a premium annual report. On top of that canvas, everything that matters is shaped like a stadium, a pill, or a perfect circle. The dominant visual gesture is the **oversized radius**: heroes carry 40-point corners, cards go fully pill-shaped, service images are cropped into circular orbits, and buttons either complete the pill or fit snugly at 20 points. There are almost no sharp corners anywhere on the page.

The second gesture is **orbit and trajectory**. Circular image masks don't sit still — they're connected by thin, hand-drawn-feeling orange arcs that span entire viewport widths, implying a constellation of services rather than a list. Each circle has a small attached "satellite" — a white micro-CTA holding an arrow icon — docked onto its perimeter like a moon. This is the most distinctive thing about Mastercard's current design language: the circles feel like they're in motion even though the page is still.

Typography is rendered entirely in **MarkForMC**, Mastercard's proprietary geometric sans. Headlines are set at a medium weight (500) with tight negative letter-spacing (-2%), giving them confidence without shouting. Body copy runs at the same family in a slightly lighter weight (450) — a weight you rarely see on the web, chosen because it reads softer than regular 400 without feeling thin. The whole system — warm cream surfaces, pill shapes, circular portraits, traced-orange orbits, black CTAs — feels simultaneously institutional (a 60-year-old payments network) and editorial (a modern brand magazine), which is exactly the tension Mastercard wants to hold.

**Key Characteristics:**
- Warm cream canvas (`#F3F0EE`) replaces traditional white — every surface is tinted, never sterile
- Extreme border-radius as design language: 40px, 99px, 1000px dominate; anything square is a cookie-banner third-party
- Circular image portraits with attached white satellite-CTAs and traced-orange orbital paths
- Ghost "watermark" headlines (cream-on-cream text at heading scale) layered behind circle portraits
- Black primary CTAs with 20px radius in the body — the cookie-banner orange is kept to consent flows
- Floating pill-shaped navigation that docks below the viewport top with rounded shoulders
- Eyebrow labels with a tiny accent dot + uppercase bold tracking — used as the section-category signal
- Dark warm-black footer (`#141413`) with four-column link layout and large conversational headline

## Colors

### Primary
- **Mastercard Red** (`#EB001B`): The left circle of the Mastercard mark — used only in the brand logo, never as a UI color.
- **Mastercard Yellow** (`#F79E1B`): The right circle of the Mastercard mark — used only in the brand logo, never as a UI color.
- **Ink Black** (`#141413`): The warm near-black used for primary CTAs, headline text on cream, and the footer surface. Slightly warm (the `13` blue value pulls toward the cream) so it never feels jet-black on the warm canvas.

### Secondary & Accent
- **Signal Orange** (`#CF4500`): The burnt/rust CTA orange used on consent actions and eyebrow dots. Deeper than the brand yellow, brighter than ink — it's the page's single aggressive color and must be used sparingly.
- **Light Signal Orange** (`#F37338`): A lighter carroty orange used for carousel active indicators and decorative orbital arcs. Always acts as an attention cue, never as body color.
- **Clay Brown** (`#9A3A0A`): The deep rust used for secondary link-style buttons (e.g., cookie details). Sits between ink and signal orange.

### Surface & Background
- **Canvas Cream** (`#F3F0EE`): The page canvas. Warm, putty-toned, the default body background. All editorial sections sit on this.
- **Lifted Cream** (`#FCFBFA`): One step lighter than canvas — used for nested "raised" sections that want to feel like paper laid on paper.
- **White** (`#FFFFFF`): Reserved for the floating navigation pill, modal cards, secondary button fills, and small satellite-CTA circles attached to image portraits.
- **Soft Bone** (`#F4F4F4`): A cool-gray alternative surface used inside a handful of component subregions.

### Neutrals & Text
- **Ink Black** (`#141413`): Primary headline and body text color.
- **Charcoal** (`#262627`): A slightly softer black used for some text alternates.
- **Slate Gray** (`#696969`): Muted secondary text — eyebrow label alternative, disabled states, "Privacy Choices" bottom-row text.
- **Granite** (`#555555`) and **Graphite** (`#565656`): Deeper gray for inline body accents and link alternates.
- **Dust Taupe** (`#D1CDC7`): Very muted cream-gray used for disabled or "whisper" text (e.g., placeholder-like empty state labels). Low contrast on cream; use only for subdued content.

### Semantic & Accent
- **Link Blue** (`#3860BE`): A deep, slightly dusty blue used for inline links and informational callouts. Saturated enough to read as a link without being neon.
- **Priceless Red + Yellow**: The full-color Mastercard logo mark is the only place the brand's red and yellow appear together; they lock the identity to the page without acting as a UI palette.

### Gradient System
Mastercard uses no programmatic gradients in the core UI. The visual impression of "gradient" comes from two places:
- **Circular image portraits** where a warm-orange photo subject (a card, a sunflower, a beverage) fades to the cream canvas at its edge
- **Deep card shadows** on elevated content (`rgba(0,0,0,0.08) 0px 24px 48px`) that create a soft halo beneath pill-shaped media

## Typography

### Font Family
- **Primary**: `MarkForMC` — Mastercard's proprietary geometric sans. Every headline, body paragraph, button, nav link, and footer link on the page.
- **Secondary**: `MarkOffcForMC` — an "Official" cut used in a minority of contexts (legal text, some forms).
- **Fallback stack**: `SofiaSans, Arial, sans-serif` — Sofia Sans is a reasonable open-source stand-in; Arial is the final web-safe fallback.

### Hierarchy

| Role | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|--------|-------------|----------------|-------|
| H1 (hero) | 64px | 500 | 64px | -1.28px (-2%) | Set to `1:1` line-height for very tight vertical rhythm on multi-line hero |
| H2 (section) | 36px | 500 | 44px | -0.72px (-2%) | Used in ghost-watermark headline treatments and section titles |
| H3 (card title) | 24px | 500 | 28.8px (1.2) | -0.48px (-2%) | Titles inside service/solution cards |
| H4 (subhead) | 14px | 700 | 18.2px (1.3) | normal | Rarely used in marketing surfaces |
| Eyebrow (H5) | 14px | 700 | 14px | 0.56px (+4%) | Uppercase, paired with a tiny accent dot (e.g., "• SERVICES") |
| Body paragraph | 16px | 450 | 22.4px (1.4) | normal | The half-step 450 weight is MarkForMC's signature — softer than 500, firmer than 400 |
| Nav link / Button label | 16px | 500 | 16px | -0.48px (-3%) | Tight, compact, no text-transform |
| Footer link | 14px | 450 | ~20px | normal | Lighter weight on dark footer for airier density |
| Footer column header | 12–14px | 700 | 14px | 0.56px (+4%) | Uppercase, muted gray, short tracking |

### Principles
- **Weight 450 is load-bearing**. Most brands use 400/500/700; Mastercard uses 450 for body copy, which creates an unusually soft reading tone. Replacing it with 400 flattens the identity.
- **Tight negative tracking on headlines** (-2%) gives display text its editorial density — the words lock together rather than breathe.
- **Uppercase tracking only on the eyebrow scale** (14px / 700 / +4% tracking). Don't use uppercase anywhere else; no shouty section titles.
- **One-font system**. Resist the urge to add a second typeface for contrast. The contrast comes from scale, weight, and letter-spacing, not from a serif or display accent.
- **Line-height ratio drops with size**. H1 is 1:1, H3 is 1.2, body is 1.4. Tight display, comfortable reading.

### Note on Font Substitutes
MarkForMC is proprietary and licensed. When rebuilding a matching aesthetic without access to the original:
- **Sofia Sans** (Google Fonts) is the closest open-source match — it's already in Mastercard's declared fallback stack.
- **Inter** at weights 450/500/700 works as a generic stand-in; expect slightly taller x-height and looser letter shapes.
- **Neue Haas Grotesk** or **Geist** can approximate the geometric feel for commercial projects.
- Whichever substitute is used, preserve the **-2% letter-spacing on headlines** and the **450 body weight** (use `font-weight: 450` with variable fonts, or substitute `font-weight: 400` and tighten the letter-spacing by ~-0.5% to compensate).

## Components

### Component States

Default and active/pressed are extracted from the live page. Every other column
is **prescribed** to suit this identity — Mastercard's marketing surfaces expose
no hover, loading or error styling that could be captured, so those cells are a
recommendation, not an observation. A dash means the component genuinely does
not have that state.

| Component | Default | Hover | Focus-visible | Active / pressed | Disabled | Loading | Selected | Error |
|---|---|---|---|---|---|---|---|---|
| `{components.button-primary}` | Ink pill, cream label | ink lightens toward `{colors.ink-charcoal}` | 2px `{colors.focus}` ring, 2px offset | subtle inward-shrink or 2px offset (extracted) | `{colors.ink-muted}` label on ink, no pointer | label swaps for a 16px spinner, width held | — | — |
| `{components.button-secondary}` | White pill, ink outline | fill shifts to `{colors.surface-bone}` | 2px `{colors.focus}` ring, 2px offset | subtle compression (extracted) | outline drops to `{colors.hairline-ink-50}` | spinner replaces label | — | — |
| `{components.button-consent}` | Signal Orange pill, white label | orange deepens toward `{colors.accent-clay}` | 2px `{colors.focus}` ring, 2px offset | 0.98 scale | not offered | spinner replaces label | — | inline message in `{colors.accent-clay}` below the pill |
| `{components.satellite-cta}` | White circle, ink arrow | arrow travels 2px along its own axis | 2px `{colors.focus}` ring, 2px offset | 0.96 scale | — | — | — | — |
| `{components.icon-button-circle}` | Transparent or white circle, ink outline | outline thickens to 1.5px | 2px `{colors.focus}` ring (`{colors.focus-on-ink}` over media) | 0.96 scale | outline at `{colors.hairline-ink-50}` | spinner in place of the icon | carousel dot fills with `{colors.accent-signal-light}` | — |
| `{components.nav-pill}` | White floating pill | link gains a faint `{colors.surface-bone}` pill surround | 2px `{colors.focus}` ring, 2px offset | link compresses 1px | — | — | current section link holds the pill surround | — |
| `{components.search-input-expanded}` | White field, 50% ink hairline | hairline goes solid `{colors.border-ink}` | 2px `{colors.focus}` ring, 2px offset | caret active | field greys to `{colors.surface-bone}` | spinner at the trailing edge | — | hairline and helper text in `{colors.accent-clay}` |
| `{components.country-selector}` | Ink pill, 40% white hairline | hairline rises to 70% white | 2px `{colors.focus-on-ink}` ring, 2px offset | chevron rotates 180 degrees | — | — | chosen locale shown in the closed pill | — |
| `{components.portrait-card}` | Circular photo, orbit arc | photo scales to 1.02 inside its mask | ring is carried by the satellite CTA | 0.99 scale | — | cream-tinted blur-up placeholder (extracted) | — | — |
| `{components.carousel-pill-card}` | Pill-cropped photography | — | 2px `{colors.focus}` ring, 2px offset | 0.99 scale on drag | — | cream-tinted blur-up placeholder (extracted) | active slide marked by an `{colors.accent-signal-light}` dot | — |
| `{components.chip-category}` | White pill, ink label | — | — | — | — | — | — | — |
| `{components.ghost-watermark-text}` | Cream-on-cream display text, decorative only | — | — | — | — | — | — | — |
| `{components.link-inline}` | `{colors.link-blue}`, no underline | underline appears | 2px `{colors.focus}` ring, 2px offset | colour deepens | `{colors.ink-muted}`, no pointer | — | — | — |
| `{components.footer-link-row}` | White label on ink | underline appears | 2px `{colors.focus-on-ink}` ring, 2px offset | 1px downward nudge | — | — | — | — |

`{components.chip-category}` and `{components.ghost-watermark-text}` are static —
a chip is a label, and the watermark is a decorative background layer. Both
genuinely have one state each.

### Buttons

**Primary — Ink Pill**
- Background: Ink Black (`#141413`)
- Text: Canvas Cream (`#F3F0EE`) — not pure white
- Border: 1.5px solid Ink Black (same as bg, creates crisp edge)
- Radius: 20px
- Padding: 6px 24px
- Font: MarkForMC 16px / weight 500 / letter-spacing -0.32px
- Default: as above; solid warm-black pill on cream canvas
- Active / pressed: subtle inward-shrink or 2px offset (not a hover variant)
- Use for: all marketing CTAs in the page body ("Learn more", "Explore", "Discover")

**Secondary — Outlined Pill**
- Background: White (`#FFFFFF`)
- Text: Ink Black (`#141413`)
- Border: 1.5px solid Ink Black
- Radius: 20px
- Padding: 6px 24px
- Font: MarkForMC 16px / weight 450 / line-height 20.8px
- Default: white-on-cream pill with crisp ink outline
- Active / pressed: subtle compression
- Use for: secondary actions paired with a primary, or standalone utility CTAs

**Consent / Signal — Orange Pill**
- Background: Signal Orange (`#CF4500`)
- Text: White (`#FFFFFF`)
- Border: 0
- Radius: 24px
- Padding: 1px 30px (very tight vertical, wide horizontal)
- Font: MarkForMC 13px / weight 400 / letter-spacing 0.13px
- Default: as above; bright rust pill with white text
- Use for: cookie consent, privacy preference, and other legally-distinct confirmations. **Do not** use this orange for marketing CTAs — it reads as a compliance color.

**Satellite — Circular Micro-CTA**
- Background: White (`#FFFFFF`)
- Icon: Ink Black arrow (`→`) at ~20px
- Border: none
- Radius: 50% (perfect circle)
- Size: ~50–60px diameter
- Shadow: none or very subtle (the portrait's shadow carries the elevation)
- Default: docks onto the bottom-right edge of a circular portrait, protruding partway outside the portrait's circle
- Use for: the primary entry point into service/solution cards; always paired with a circular portrait

**Icon-Only Circle Button (carousel, play/pause)**
- Background: transparent or white
- Icon: 10–20px centered
- Border: 1px solid Ink Black (when on cream) or none (when over media)
- Radius: 50%
- Size: 40px diameter minimum for carousel controls; 80px for hero video play
- Use for: carousel pagination/play-pause, hero video play, search toggle

### Cards & Containers

**Hero Media Frame (Stadium)**
- Background: Dark video or full-bleed imagery (typically black `#000000` or `#2B2B2B` behind video)
- Radius: 40px all corners (creates a stadium shape on wide viewports)
- Width: ~full viewport minus ~48px gutter on each side
- Height: ~60–70% of viewport
- Shadow: none (sits directly on canvas)
- Corners: the extreme 40px radius on a media element is the most iconic Mastercard gesture — do not round less

**Service / Solution Portrait Card**
- Shape: Perfect circle (radius 50%) or ellipse (radius 999px / 1000px)
- Diameter: 260–340px desktop; ~220px mobile
- Image crop: square source, cropped to circle
- Attached element: White satellite circular CTA (see above) docked bottom-right, ~40% outside the portrait
- Eyebrow below: accent dot + uppercase label (e.g., "• SERVICES", "• SOLUTIONS")
- Title below: H3 (24px / weight 500 / -2% tracking), 1–2 lines max
- Decorative orbit: thin ~1px Light Signal Orange curved line spanning from this card outward to the next, implying connection

**Pill Carousel Card**
- Radius: 1000px (full pill) or 40px corners (rounded stadium)
- Width: ~40–60% of viewport
- Height: ~380–420px (portrait-pill orientation)
- Content: full-bleed photography with small overlaid chip labels
- Chip inside: White pill (~ 999px radius), Ink Black text, padding 8px 20px, used for category tags like "Story"
- Large inline CTA inside: Ink Pill button, oversized (padding 16px 40px, radius 40px)

**Ghost Watermark Text Block**
- Font: MarkForMC 72–128px / weight 500 / tight -2% tracking
- Color: Canvas Cream slightly darkened (`#E8E2DA` or similar — cream-on-cream)
- Position: layered behind portrait circles, bleeding off the viewport edge
- Purpose: sets section theme without competing with foreground copy

### Inputs & Forms
Minimal form surface on the marketing page. The search input in the nav header is:
- Initial state: a 48px circular button with a magnifier icon
- Expanded state: horizontal input field, border `1px solid` Ink Black at ~50% opacity, radius 999px, padding 12px 24px, white background

**Country/language selector (footer)**
- Background: Ink Black (same as footer)
- Text: White
- Border: 1px solid `rgba(255,255,255,0.4)`
- Radius: 999px (full pill)
- Icon: downward chevron on the right

### Navigation

**Floating Nav Pill (desktop)**
- Container: white-to-translucent-white pill floating below the very top of the viewport with a ~24px top margin
- Radius: 999px / 1000px (full pill)
- Padding: ~16px 40px internal
- Shadow: very soft (`rgba(0, 0, 0, 0.04) 0px 4px 24px 0px`) — just enough to lift it off the cream canvas
- Content: Mastercard logo left, primary link group center ("For you", "For business", "For the world", "For innovators", "News and trends"), search icon right
- Link spacing: ~48–56px gap between primary links
- Link style: Ink Black, weight 500, 16px, no underline, no pill surround until active

**Mobile Nav**
- The same pill shape but collapsed to: logo + hamburger menu button + search icon only
- Menu opens into a full-screen overlay with the primary links stacked vertically

### Image Treatment

- **Aspect ratios used**: 1:1 (all service portraits — cropped to circle), ~3:4 or ~4:5 (carousel pill cards), 16:9 or wider (hero video frame)
- **Full-bleed vs padded**: Hero is viewport-wide with gutters; service portraits are always centered in their column with generous whitespace around; footer imagery is rare
- **Masking**: Aggressive circular masking is the defining treatment — square source images are cropped to perfect circles of matching diameter. Never use rectangular service imagery.
- **Lazy loading**: Standard `loading="lazy"` with a soft blur-up transition from a cream-tinted placeholder, preserving the warm palette during load

### Decorative Orbital Lines

A signature motif: thin (~1–1.5px) single-weight curved lines in Light Signal Orange (`#F37338`) tracing arcs between circular portraits. These lines:
- Imply connection between service cards without literal arrows
- Span widths from ~200px up to full-viewport arcs
- Feel hand-drawn (subtle irregularity) rather than perfect CSS curves
- Appear only in sections with circular portrait content — never on pill sections, never in the footer

### Footer

- Background: Ink Black (`#141413`)
- Text: White
- Padding: 48px horizontal 100px / bottom 148px (very tall bottom space)
- Structure: large conversational H2 ("We're always here when you need us") left-aligned, then a 4-column link grid below
- Column headers: uppercase, muted, weight 700, letter-spacing +4%
- Link rows: white, weight 450, 14px; entries prefixed with a small icon (support bubble, card, map pin, question mark) for the "NEED HELP?" column
- External link marker: a small upper-right arrow (`↗`) after link text
- Bottom row (below a 1px white-at-opacity divider): copyright + privacy small-print + country-language pill dropdown + four social icons (LinkedIn, Facebook, X, YouTube)

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** Nobody timed Mastercard's real transitions;
what follows is the **Calm** profile, chosen because the file's own description
is editorial, the display weight is 500 rather than a heavy 700+, gradients are
absent from the core UI, and whitespace is used to slow the reader down. Travel
is small and opacity leads, so the constellation of circles keeps its stillness.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, link, nav) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `transform: translateY(-1px)` | travel removed; opacity only at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | no scale; no substitute |
| Focus ring appears | `{motion.duration-instant}` | `{motion.ease-enter}` | `opacity` | unchanged — the ring must never be delayed or faded out |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` | opacity only at `{motion.duration-reduced}` |
| Modal or drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px)` | travel removed; opacity only at `{motion.duration-reduced}` |
| Modal or drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform: translateY(8px)` | travel removed; opacity only at `{motion.duration-reduced}` |
| Dropdown (country selector, nav menu) | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(-4px)` | travel removed; opacity only at `{motion.duration-reduced}` |
| Toast | in `{motion.duration-base}`, out `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px)` | travel removed; opacity only at `{motion.duration-reduced}` |
| List enter (service portraits, footer columns) | `{motion.duration-base}`, staggered `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | stagger and travel removed; one opacity fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | opacity only at `{motion.duration-reduced}` |
| Loading (spinner, blur-up placeholder) | 1200ms loop | linear | `transform: rotate()`, `opacity` | spinner frozen; a static cream-tinted placeholder remains |

Rules this table obeys:

- Animate `transform` and `opacity` only — never `width`, `height`, `top`,
  `left` or `margin`. The "inward-shrink" on a pressed pill is a `scale`, not a
  size change.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content; the hero media
  frame is painted, not revealed.
- The spinner is the only infinite animation. The orbital arcs are drawn once
  and then still — they are decorative geometry, not brand ambience, so there is
  no looping motion anywhere else in the system.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate, all scale, the list stagger, the spinner's rotation. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (150ms), and the
     focus ring, which is never animated away. */
  *, *::before, *::after {
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important;
    transition-property: opacity !important;
  }
}
```

## Layout

### Spacing System
- **Base unit**: 8px (confirmed by dembrandt extraction and computed styles)
- **Scale**: 8 / 16 / 24 / 32 / 48 / 64 / 96 / 128 (powers of 8)
- **Section vertical padding**: ~96–128px between major sections on desktop; ~48–64px on mobile
- **Card internal padding**: 32–40px on desktop, ~24px on mobile
- **Nav top margin**: ~24px from viewport top (the pill floats, doesn't touch)

### Grid & Container
- **Max content width**: ~1200–1280px centered, with ~48–100px horizontal gutter
- **Column pattern**: 12-column implied, but practical layouts use 2-up asymmetric (large headline left, supporting text right), 1-up full-bleed (hero, video), or staggered single-portrait placement (service cards sit in varying grid positions creating the "constellation" feel)
- **Footer grid**: 4 equal columns on desktop, collapses to single column accordion on mobile

### Whitespace Philosophy
Mastercard treats whitespace as structure, not absence. A typical service section has:
- A ghost headline occupying the top ~40% of the section (mostly empty cream)
- A single circular portrait positioned ~60% down, asymmetric to left or right
- ~300–500px of blank canvas between the portrait and the next section
This deliberate emptiness tells the eye "slow down, read one thing at a time" — the opposite of dense dashboard UIs.


## Shapes

| Radius | Use |
|--------|-----|
| 3–6px | Tiny decorative elements, cookie banner micro-chips |
| 20px | Primary and secondary body CTAs (the signature button radius) |
| 24px | Consent/orange pill buttons, modal inner chips |
| 40px | Hero media frames, large section container corners, H2 pill labels |
| 50% | Circular portraits, icon-only buttons, satellite CTAs |
| 99px / 999px / 1000px | Full pill shapes — navigation, carousel cards, footer country selector, primary inline chips |

The scale is unusual: most systems use 4/8/12/16. Mastercard skips those and commits to **either small (≤6), medium-large (20–40), or full-pill (99+)**. The middle ground of 8–12 is absent, which is why the UI feels either "precise and utility" or "soft and editorial" with no in-between.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| 0 | No shadow | The default — 95% of surfaces sit directly on cream canvas |
| 1 | `rgba(0, 0, 0, 0.04) 0px 4px 24px 0px` | Floating nav pill — barely-there lift |
| 2 | `rgba(0, 0, 0, 0.08) 0px 24px 48px 0px` | Hero media frames, elevated cards — a soft large-radius halo rather than a hard drop |
| 3 | `rgba(0, 0, 0, 0.25) 0px 70px 110px 0px` | Rare; dramatic elevation on a feature tile |

### Shadow Philosophy
Mastercard uses shadows as **atmospheric cushioning**, not directional light. The Level 2 shadow has a 48px spread and only 8% opacity — it barely exists as dark pixels but creates a "the card is breathing above the canvas" feel. There are almost no hard-edged, tight shadows anywhere in the system. Border lines are preferred over shadows for functional delineation (form inputs, footer divider).

Shadow is doing all of the work here, because the surface tones carry almost no
luminance separation: `surface-lifted` sits at 1.10:1 against `canvas-cream`,
`surface-white` at 1.13:1 and `surface-bone` at 1.03:1. None of those layers is
distinguishable from the canvas by colour alone, which is deliberate — the three
cream tones exist to warm a surface, not to rank it. Depth therefore has exactly
two legitimate expressions in this system, and they are not interchangeable:
`{shadow.level-1}` to `{shadow.level-3}` for floating or elevated content, and a
1px rule (`{colors.hairline-ink-50}` on cream, `{colors.border-on-ink}` on the
ink footer) for functional delineation. Do not substitute a slightly different
cream for either one; at ~1.1:1 it will not read as a layer.

### Decorative Depth
- **Orbital arcs** (Light Signal Orange, ~1px): trace connective paths across sections
- **Ghost watermark headlines**: cream-on-cream text gives sections an almost-pressed-paper quality
- **Circle-image fade**: warm-toned photography at the edge of circular portraits dissolves into the canvas, implying soft atmospheric depth

## Accessibility

Every ratio below is computed with WCAG 2.1 relative luminance from the hexes in
this file's own `colors:` block. Extracted brand values are frozen: where one
fails, it is named here rather than quietly corrected.

### Measured contrast

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `ink` on `canvas-cream` | 16.25:1 | 4.5:1 | pass |
| `ink` on `surface-lifted` | 17.84:1 | 4.5:1 | pass |
| `ink` on `surface-white` | 18.43:1 | 4.5:1 | pass |
| `ink` on `surface-bone` | 16.76:1 | 4.5:1 | pass |
| `ink-charcoal` on `canvas-cream` | 13.33:1 | 4.5:1 | pass |
| `ink-muted` on `canvas-cream` | 4.84:1 | 4.5:1 | pass |
| `ink-granite` on `canvas-cream` | 6.57:1 | 4.5:1 | pass |
| `ink-graphite` on `canvas-cream` | 6.47:1 | 4.5:1 | pass |
| `link-blue` on `canvas-cream` | 5.16:1 | 4.5:1 | pass |
| `accent-clay` on `canvas-cream` | 6.20:1 | 4.5:1 | pass |
| `on-accent` on `accent-signal` | 4.66:1 | 4.5:1 | pass |
| `on-ink` on `surface-ink-footer` | 18.43:1 | 4.5:1 | pass |
| `border-ink` on `canvas-cream` | 16.25:1 | 3.0:1 | pass |
| `hairline-ink-50` composited on `canvas-cream` | 3.37:1 | 3.0:1 | pass |
| `focus` on `canvas-cream` | 16.25:1 | 3.0:1 | pass |
| `focus` on `surface-white` | 18.43:1 | 3.0:1 | pass |
| `focus` on `surface-bone` | 16.76:1 | 3.0:1 | pass |
| `focus-on-ink` on `surface-ink-footer` | 16.25:1 | 3.0:1 | pass |
| `accent-signal` as text on `canvas-cream` | 4.11:1 | 4.5:1 | **fail** — fill-only colour, see below |
| `accent-signal-light` as text on `canvas-cream` | 2.53:1 | 4.5:1 | **fail** — decorative only, see below |
| `ink-whisper` as text on `canvas-cream` | 1.40:1 | 4.5:1 | **fail** — real brand failure, see below |
| `ghost-watermark-text` (`watermark-ghost` on `canvas-cream`) | 1.13:1 | 3.0:1 | **fail** — deliberate, see below |
| `brand-red` on `canvas-cream` | 4.07:1 | 4.5:1 | **fail** — logo mark only, never text |
| `brand-yellow` on `canvas-cream` | 1.88:1 | 4.5:1 | **fail** — logo mark only, never text |
| `border-on-ink` composited on `canvas-cream` | 1.05:1 | 3.0:1 | **fail** — harness artifact, see below |
| `border-on-ink` composited on `surface-lifted` | 1.04:1 | 3.0:1 | **fail** — harness artifact, see below |
| `ink-muted` on `surface-ink-footer` | 3.36:1 | 4.5:1 | **fail** — do not place muted grey on the ink footer |

### Where this brand genuinely fails AA

- **Ghost watermark headlines fail by design.** `watermark-ghost` (`#E8E2DA`) on
  `canvas-cream` is 1.13:1. Cream-on-cream is the point of the treatment, so the
  honest answer is not to darken it but to treat it as decoration: the watermark
  must never carry information that is not also present in real foreground copy,
  and it must be `aria-hidden`. Anyone who needs the section theme reads it from
  the eyebrow label and the H2.
- **Dust Taupe is not a text colour.** `ink-whisper` (`#D1CDC7`) measures 1.40:1
  on the canvas. The file describes it as "whisper" and placeholder-like text;
  at that ratio it is invisible to a large share of readers. Use
  `ink-muted` (4.84:1) for any placeholder or empty-state label that has to be
  read, and keep `ink-whisper` for hairline-weight decoration.
- **Signal Orange cannot be body text.** `accent-signal` (`#CF4500`) is 4.11:1
  on the canvas. It passes as a *fill* behind white text (4.66:1), which is the
  only way the file uses it, but it must not be set as text or as an icon that
  conveys meaning on cream.
- **The orbital arc colour is decorative and nothing else.**
  `accent-signal-light` (`#F37338`) is 2.53:1 on the canvas — below even the
  3:1 non-text threshold. The arcs carry no information, so this is acceptable,
  but the same colour must not be reused for a carousel dot that is the *only*
  indicator of position. Pair the dot with a size or shape change as well.
- **The logo mark is exempt.** `brand-red` and `brand-yellow` fail as text and
  are never used as text; WCAG 1.4.3 does not apply to a logotype.

### Focus ring

No file in this collection defined a focus ring, so one is prescribed here.
It is drawn **outside** the control, so it is judged against the surface behind
it rather than the control fill, which is what WCAG 2.2 Focus Appearance asks
for.

- `focus` = `{colors.focus}` (`#141413`, the brand ink), 2px wide, 2px offset.
  Used on `canvas-cream` (16.25:1), `surface-lifted` (17.84:1), `surface-white`
  (18.43:1) and `surface-bone` (16.76:1).
- `focus-on-ink` = `{colors.focus-on-ink}` (`#F3F0EE`, the canvas cream), 2px
  wide, 2px offset. Used on `surface-ink-footer` (16.25:1) — the ink ring would
  sit at 1:1 there, which is why a second token exists rather than one
  compromise value.
- Over hero video and full-bleed photography, which has no measurable colour,
  the ring is two-tone: 2px `focus-on-ink` with a 1px `focus` outer edge, so one
  band always separates from the imagery.
- The ring is the brand's own ink and paper rather than a new chromatic colour,
  because Signal Orange is reserved for consent and compliance signalling and a
  focus ring in that colour would dilute the legal signal this file is explicit
  about protecting.

### Tap targets

The file states that every interactive element exceeds 44x44px — satellite CTAs
at 50-60px, nav pill controls at ~48px, mobile hamburger and search at 48x48px.
That is a claim copied from the source document, not a measurement: tap-target
size cannot be verified from a document, so treat it as the design intent to
hold rather than as a confirmed fact.

### Reduced motion

`@media (prefers-reduced-motion: reduce)` removes all translate and scale,
removes the list stagger, freezes the loading spinner, and keeps opacity fades
capped at `{motion.duration-reduced}` (150ms). The focus ring is never animated
away under any preference.

## Do's and Don'ts

### Do
- Use Canvas Cream (`#F3F0EE`) as the default body background — never pure white
- Mask service/feature imagery as perfect circles, not rectangles or rounded rectangles
- Attach a white satellite CTA to the bottom-right of each circular portrait
- Set headlines in MarkForMC weight 500 with -2% letter-spacing
- Use weight 450 (not 400) for body paragraphs
- Keep primary CTAs as Ink Black pills (20px radius) with cream text
- Use Signal Orange only on consent, legal, or compliance actions
- Float the nav as a rounded white pill below the viewport top, not flush at y=0
- Build page rhythm from three surface tones: canvas cream → lifted cream → ink footer
- Use thin Light Signal Orange arcs between service cards to imply connection

### Don't
- Don't use pure white as a page background — it breaks the warm editorial tone
- Don't round image frames at 8–16px — Mastercard either uses full-pill, 40px, or full-circle. In-between radii look generic
- Don't use Signal Orange for marketing CTAs — it reads as cookie-consent orange and dilutes the legal color signal
- Don't mix typefaces — no serif accent, no script, no secondary display font
- Don't crowd the nav with more than six top-level links — the pill is meant to feel airy
- Don't drop hard shadows — all elevation should use 48px+ spread and ≤10% opacity
- Don't use uppercase for anything larger than the 14px eyebrow label
- Don't omit the tiny accent dot before eyebrow labels — it's the identity
- Don't place circular portraits on a grid — their magic comes from asymmetric placement

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | ≤ 767px | Nav pill shows logo + menu + search only; primary links hide behind hamburger; service portraits stack single-column centered; hero headline drops from 64px to ~40px; footer columns collapse into a vertical accordion |
| Tablet | 768–1023px | Nav pill shows 2–3 primary links truncated; service portraits arrange 2-up; hero headline ~48px |
| Desktop | ≥ 1024px | Full nav with 5 primary links centered; service portraits asymmetrically placed with decorative orbital lines; hero headline 64px |
| Wide | ≥ 1440px | Content max-width caps at ~1280px; gutters grow symmetrically; orbital lines extend further |

### Touch Targets
All interactive elements comfortably exceed 44×44px. The satellite CTA (circle + arrow) is ~50–60px. The nav pill buttons are ~48px tall. Mobile hamburger and search are 48×48px. No link or button drops below 40px in any breakpoint.

### Collapsing Strategy
- **Nav**: full pill → compact pill with hamburger. Pill shape is preserved across breakpoints — always rounded, always floating.
- **Service grid**: asymmetric constellation → 2-up → 1-up stack. Orbital arcs are removed on mobile (they only work with asymmetric placement).
- **Spacing**: section vertical padding compresses from 128px to 48px on mobile.
- **Content**: two-column hero (headline left / supporting text right) becomes stacked (headline on top, supporting text below).
- **Footer**: 4 columns → 1 column accordion with chevron toggles per section.

### Image Behavior
Circular portraits scale proportionally (maintaining the perfect circle at every size). Hero video frames maintain their 40px radius at every breakpoint, but the frame itself shrinks with the viewport. Lazy loading is standard with a cream-tinted blur-up placeholder, preserving the palette during load.

## Iteration Guide
When refining existing screens generated with this design system:
1. Focus on ONE component at a time — don't redesign multiple surfaces in parallel
2. Reference specific color names AND hex codes from this document
3. Use natural language ("warm putty cream", "stadium pill", "circular portrait with satellite CTA") alongside technical values
4. Describe the desired "feel" (editorial, soft, institutional) alongside specific measurements
5. When in doubt, reach for one of three radii: 20px (buttons), 40px (hero/stadium), or 999px (pill/nav)
6. Default backgrounds to Canvas Cream (`#F3F0EE`), not white — this single change shifts the entire mood toward Mastercard


## Known Gaps
- The live page uses MarkForMC, a proprietary licensed typeface. Sofia Sans is the closest open-source substitute and is listed in Mastercard's own fallback stack.
- Tablet breakpoint specifics (768–1023px) were inferred from desktop and mobile captures; intermediate layouts may vary per section.
- The exact "whisper" cream tone used for ghost-watermark headlines behind circular portraits reads between `#E8E2DA` and `#D1CDC7` in captures; the precise value varies per section.
- Third-party consent orange (`#CF4500`) is Mastercard's documented consent signal and should not be confused with any marketing CTA color.
- The Mastercard logo mark (red `#EB001B` + yellow `#F79E1B`) is a brand asset, not a UI palette entry.
- No frontmatter token block existed before this revision. Every token now in
  `colors:`, `typography:`, `spacing:`, `rounded:` and `shadow:` was read out of
  this file's own prose; nothing was measured afresh and nothing was invented.
- Line height is not stated anywhere in the source for the primary button label,
  the consent button label, or the ghost-watermark display role. Those three
  `typography:` entries carry size, weight and tracking but no `lineHeight`.
- The source gives the tiny decorative radius as a "3-6px" range and the pill
  radius as "99px / 999px / 1000px". `{rounded.xs}` and `{rounded.sm}` take the
  two ends of the first range and `{rounded.full}` takes 999px; the exact value
  per element is unknown.
- The footer column headers are described only as "uppercase, muted, weight
  700". No hex is given for that grey, so no `footer-column-header` entry
  exists in `components:` and no contrast pair could be declared for it. Note that
  `ink-muted` on the ink footer is 3.36:1, so the obvious guess would fail.
- The source gives the footer column-header size as a "12-14px" range;
  `{typography.footer-column-header}` takes 14px, the value the Do's and Don'ts
  and the Agent Prompt Guide both repeat.
- Chip labels, the "Story" category tag and the oversized inline carousel CTA
  have stated padding and radius but no stated type size, so no typography role
  was created for them.
- The whole Motion & Animation section is prescribed, not extracted. No timing
  function, duration or easing curve in this file was measured from the live
  site.
- Hover, focus-visible, loading, selected and error styling is prescribed for
  every component. The source documents only default and active/pressed, and
  only for the two body buttons.
- `{colors.border-on-ink}` is stated in the source as `rgba(255,255,255,0.4)`
  and is only ever drawn on the ink footer, where it measures 3.83:1. It has no
  opaque equivalent in the source.
- The source disagrees with itself on the footer divider's opacity: the Footer
  description gives `rgba(255,255,255,0.4)` for the country-selector border
  while the Agent Prompt Guide asks for a "1px white-at-30%-opacity horizontal
  divider". `{colors.border-on-ink}` takes the 40% figure, since that is the one
  attached to a named component. Whether the divider and the selector border are
  the same value is unresolved.
- The three cream surfaces are separated by 1.03:1 to 1.13:1, so elevation in
  this system is legible only through shadow or a rule, never through surface
  tone. That is recorded as the intent in Elevation & Depth rather than as a
  defect, but it does mean a layer ladder cannot be built from these tokens.

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: "Ink Black (`#141413`) — the warm near-black used for primary pill buttons and footer"
- Background: "Canvas Cream (`#F3F0EE`) — warm putty body canvas, never pure white"
- Lifted surface: "Lifted Cream (`#FCFBFA`) — one step lighter than canvas for nested sections"
- Heading text: "Ink Black (`#141413`)"
- Body text: "Ink Black (`#141413`) at weight 450"
- Muted text: "Slate Gray (`#696969`)"
- Signal / Consent: "Signal Orange (`#CF4500`) — reserve for cookie consent and legal actions"
- Accent arc: "Light Signal Orange (`#F37338`) — orbital decorative lines only"
- Border / Outline: "Ink Black at 1.5px for pill buttons; 1px at low opacity elsewhere"
- Footer: "Ink Black (`#141413`) with White text"

### Example Component Prompts
- "Create a circular portrait card 300px in diameter, with a square photograph cropped to a perfect circle. Attach a 56px white satellite button with a dark arrow icon at the bottom-right, so it protrudes ~40% outside the portrait. Below the portrait, add an eyebrow label with a Light Signal Orange dot and uppercase 'SERVICES' text in MarkForMC weight 700 at 14px. Below the eyebrow, set a 24px / weight 500 title in Ink Black."
- "Design a primary CTA button: Ink Black (`#141413`) background, Canvas Cream (`#F3F0EE`) text, 20px border-radius, 6px vertical and 24px horizontal padding, MarkForMC font at 16px weight 500 with -2% letter-spacing."
- "Build a floating navigation pill: white background with `rgba(0, 0, 0, 0.04) 0px 4px 24px 0px` shadow, 999px border-radius, ~16px vertical and 40px horizontal internal padding. Position it 24px below the viewport top, centered, with the Mastercard logo at the left, five primary links centered with 48px gap, and a circular 48px search button at the right."
- "Create a hero media frame: 40px border-radius on all corners, full viewport width minus 48px gutters, ~60% viewport height, dark background for video content. Place it directly on the cream canvas with no shadow."
- "Design a footer: Ink Black (`#141413`) background, white text, 4-column link grid with uppercase muted column headers at 14px weight 700 +4% tracking. Include a large conversational H2 above the grid, a 1px white-at-30%-opacity horizontal divider below, and a bottom row with copyright, legal small-print links, a pill-shaped country selector, and four social icons."

