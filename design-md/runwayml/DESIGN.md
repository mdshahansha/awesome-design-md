---
version: alpha
name: Runway-design-analysis
description: A cinematic reel rendered as a website. The canvas is true black (#000000), full-bleed photography and video are the primary UI elements, and the interface itself retreats into near-invisibility — zero shadows, barely visible #27272a hairlines, cool blue-gray neutrals (#767d88, #7d848e) for every secondary voice. One typeface, abcNormal, carries everything from 48px film-title display to 11px weight-450 micro labels at line-height 1.0 with negative tracking. There is no accent colour by design: the only colour in the product comes from the imagery. Every colour, type, spacing and radius value below is read from this file's own prose; the motion group is prescribed, not measured.

colors:
  canvas: "#000000"
  canvas-deep: "#030303"
  surface-dark: "#1a1a1a"
  surface-light: "#fefefe"
  surface-light-cool: "#e9ecf2"
  ink: "#ffffff"
  on-light: "#404040"
  ink-secondary-alt: "#3f3f3f"
  text-secondary: "#767d88"
  text-tertiary: "#7d848e"
  text-soft: "#6b7280"
  muted: "#a7a7a7"
  muted-footer: "#999999"
  link-on-light: "#0c0c0c"
  border-dark: "#27272a"
  border-light-cool: "#c9ccd1"
  border-light-silver: "#d0d4d4"
  focus: "#767d88"

typography:
  display-hero:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -1.2px
  section-heading:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.00-1.10
    letterSpacing: -1px to 0px
  sub-heading:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -0.9px
  card-title:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: normal
  feature-title:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: normal
  body:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 16px
    fontWeight: 400-600
    lineHeight: 1.30-1.50
    letterSpacing: -0.16px to normal
  caption:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 14px
    fontWeight: 500-600
    lineHeight: 1.25-1.43
    letterSpacing: 0.35px
    textTransform: uppercase
  small:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.16px to -0.26px
  micro:
    fontFamily: "abcNormal, abcNormal Fallback, Inter, DM Sans, sans-serif"
    fontSize: 11px
    fontWeight: 450
    lineHeight: 1.30
    letterSpacing: normal
    textTransform: uppercase

spacing:
  hair: 4px
  micro: 6px
  xs: 8px
  sm: 12px
  md: 16px
  md-alt: 20px
  lg: 24px
  lg-alt: 28px
  xl: 32px
  section: 48px
  section-lg: 64px
  section-xl: 78px

rounded:
  sharp: 4px
  subtle: 6px
  comfortable: 8px
  generous: 16px

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
  button-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sharp}"
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sharp}"
    borderColor: "{colors.border-dark}"
  card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.comfortable}"
    borderColor: "{colors.border-dark}"
    padding: "{spacing.lg}"
  card-light:
    backgroundColor: "{colors.surface-light-cool}"
    textColor: "{colors.on-light}"
    typography: "{typography.card-title}"
    rounded: "{rounded.comfortable}"
    borderColor: "{colors.border-light-cool}"
    padding: "{spacing.lg}"
  alert-container:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.generous}"
    borderColor: "{colors.border-dark}"
    padding: "{spacing.md}"
  top-nav:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body}"
  hero-cinematic:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-hero}"
  article-card-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.comfortable}"
  article-card-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.on-light}"
    typography: "{typography.card-title}"
    rounded: "{rounded.comfortable}"
  section-label:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.caption}"
  trust-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    padding: "{spacing.section}"
  mission-statement:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.sub-heading}"
    padding: "{spacing.section-xl}"
  image-frame:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.comfortable}"
  link-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.link-on-light}"
    typography: "{typography.body}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-footer}"
    typography: "{typography.body}"
    padding: "{spacing.section}"
---

# Design System Inspired by Runway

## Overview

Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements. This is not a typical tech product page; it's a visual manifesto for AI-powered creativity. Every section feels like a frame from a film: dramatic lighting, sweeping landscapes, and intimate human moments captured in high-quality imagery that dominates the viewport.

The design language is built on a single typeface — abcNormal — a clean, geometric sans-serif that handles everything from 48px display headlines (`{typography.display-hero}`) to 11px uppercase labels (`{typography.micro}`). This single-font commitment creates an extreme typographic uniformity that lets the visual content speak louder than the text. Headlines use tight line-heights (1.0) with negative letter-spacing (-0.9px to -1.2px), creating compressed text blocks that feel like film titles rather than marketing copy.

What makes Runway distinctive is its complete commitment to visual content as design. Rather than illustrating features with icons or diagrams, Runway shows actual AI-generated and AI-enhanced imagery — cars driving through cinematic landscapes, artistic portraits, architectural renders. The interface itself retreats into near-invisibility: minimal borders (`{colors.border-dark}`), zero shadows, subtle cool-gray text (`{colors.text-secondary}`), and a dark palette (`{colors.canvas}`) that puts maximum focus on the photography.

**Key Characteristics:**
- Cinematic full-bleed photography and video as primary UI elements
- Single typeface system: abcNormal for everything from display to micro labels
- Dark-dominant palette with cool-toned neutrals (`{colors.text-secondary}` — #767d88, `{colors.text-tertiary}` — #7d848e)
- Zero shadows, minimal borders — the interface is intentionally invisible
- Tight display typography (line-height 1.0) with negative tracking (-0.9px to -1.2px)
- Uppercase labels with positive letter-spacing for navigational structure
- Weight 450 (unusual intermediate) for small uppercase text — precision craft
- Editorial magazine layout with mixed-size image grids
- **No accent colour at all**: the palette contains no signal hue, by design — see Known Gaps

## Colors

### Primary
- **Runway Black** (`{colors.canvas}` — `#000000`): The primary page background and maximum-emphasis text.
- **Deep Black** (`{colors.canvas-deep}` — `#030303`): A near-imperceptible variant for layered dark surfaces.
- **Dark Surface** (`{colors.surface-dark}` — `#1a1a1a`): Card backgrounds and elevated dark containers.
- **Pure White** (`{colors.ink}` — `#ffffff`): Primary text on dark surfaces and light-section backgrounds.

### Surface & Background
- **Near White** (`{colors.surface-light}` — `#fefefe`): The lightest surface — barely distinguishable from pure white.
- **Cool Cloud** (`{colors.surface-light-cool}` — `#e9ecf2`): Light section backgrounds with a cool blue-gray tint.
- **Border Dark** (`{colors.border-dark}` — `#27272a`): The single dark-mode border color — barely visible containment. At 1.41:1 on the canvas this is **decoration only** and never the sole boundary of a control — see Accessibility.

### Neutrals & Text
- **Charcoal** (`{colors.on-light}` — `#404040`): Primary body text on light surfaces and secondary text.
- **Near Charcoal** (`{colors.ink-secondary-alt}` — `#3f3f3f`): Described in the source as a "slightly lighter variant for dark-section secondary text". On either dark surface it is **not legible as text** (1.99:1 / 1.65:1) — see Accessibility.
- **Cool Slate** (`{colors.text-secondary}` — `#767d88`): Secondary body text — a distinctly blue-gray cool neutral. Clears AA on the canvas, **fails on the dark surface**.
- **Mid Slate** (`{colors.text-tertiary}` — `#7d848e`): Tertiary text, metadata descriptions.
- **Muted Gray** (`{colors.muted}` — `#a7a7a7`): De-emphasized content, timestamps.
- **Cool Silver** (`{colors.border-light-cool}` — `#c9ccd1`): Light borders and dividers.
- **Light Silver** (`{colors.border-light-silver}` — `#d0d4d4`): The lightest border/divider variant.
- **Tailwind Gray** (`{colors.text-soft}` — `#6b7280`): Standard Tailwind neutral for supplementary text. **Fails AA on both dark grounds**; defensible only on the light surfaces.
- **Dark Link** (`{colors.link-on-light}` — `#0c0c0c`): Darkest link text — nearly black, drawn on the light surfaces.
- **Footer Gray** (`{colors.muted-footer}` — `#999999`): Footer links and deeply muted content.

### Borders
Runway documents three boundary tones and all three are frozen below the 3:1 threshold — this is the deliberate "barely visible containment" the source describes. **No parallel accessible boundary token is added**, because the palette already owns a tone that does the job: `{colors.text-secondary}` (#767d88) clears 3:1 against every one of the six surfaces this file defines (3.51:1 at worst, on Cool Cloud). Any boundary that must be perceivable — the edge of a text input, a focusable card — is drawn in that tone. The three extracted hairlines stay scoped to decoration.

### Accent
**There is no accent colour.** Runway's palette contains no signal hue: the source states that "the interface itself is intentionally colorless", that "visual richness comes entirely from photographic content", and its own Don'ts forbid adding decorative colour. The `accent` and `on-accent` roles are therefore left **unfilled** rather than aliased onto the white ink — see Known Gaps. The brand's signal is white type on black, plus the imagery itself.

### Focus
- **Focus ring** (`{colors.focus}` — `#767d88`): **Prescribed, not extracted** — the source documents no focus treatment anywhere. The ring reuses an existing brand tone, Cool Slate, rather than introducing a new colour: a brand whose first rule is that it has no accent colour must not acquire a chromatic ring. One mid-luminance ring is used rather than a light/dark pair because this file carries three dark grounds and three light ones, and Cool Slate clears 3:1 against all six. Measured ratios are in Accessibility.

### Gradient System
- **None in the interface.** Visual richness comes entirely from photographic content — AI-generated and enhanced imagery provides all the color and gradient the design needs. The interface itself is intentionally colorless.

## Typography

### Font Family
- **Universal**: `abcNormal`, with fallback: `abcNormal Fallback`

*Note: abcNormal is a custom geometric sans-serif. For external implementations, Inter or DM Sans serve as close substitutes.*

### Hierarchy

| Role | Token | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|-------|------|------|--------|-------------|----------------|-------|
| Display / Hero | `{typography.display-hero}` | abcNormal | 48px (3rem) | 400 | 1.00 (tight) | -1.2px | Maximum size, film-title presence |
| Section Heading | `{typography.section-heading}` | abcNormal | 40px (2.5rem) | 400 | 1.00–1.10 | -1px to 0px | Feature section titles |
| Sub-heading | `{typography.sub-heading}` | abcNormal | 36px (2.25rem) | 400 | 1.00 (tight) | -0.9px | Secondary section markers |
| Card Title | `{typography.card-title}` | abcNormal | 24px (1.5rem) | 400 | 1.00 (tight) | normal | Article and card headings |
| Feature Title | `{typography.feature-title}` | abcNormal | 20px (1.25rem) | 400 | 1.00 (tight) | normal | Small headings |
| Body / Button | `{typography.body}` | abcNormal | 16px (1rem) | 400–600 | 1.30–1.50 | -0.16px to normal | Standard body, nav links |
| Caption / Label | `{typography.caption}` | abcNormal | 14px (0.88rem) | 500–600 | 1.25–1.43 | 0.35px (uppercase) | Metadata, section labels |
| Small | `{typography.small}` | abcNormal | 13px (0.81rem) | 400 | 1.30 (tight) | -0.16px to -0.26px | Compact descriptions |
| Micro / Tag | `{typography.micro}` | abcNormal | 11px (0.69rem) | 450 | 1.30 (tight) | normal | Uppercase tags, tiny labels |

### Principles
- **One typeface, complete expression**: abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching.
- **Tight everywhere**: Nearly every size uses line-height 1.0–1.30 — even body text is relatively compressed. This creates a dense, editorial feel.
- **Weight 450 — the precision detail**: Some small uppercase labels use weight 450, an uncommon intermediate between regular (400) and medium (500). This micro-craft signals typographic sophistication.
- **Negative tracking as default**: Even body text uses -0.16px to -0.26px letter-spacing, keeping everything slightly tighter than default.
- **Uppercase as structure**: Labels at 14px and 11px use `text-transform: uppercase` with positive letter-spacing (0.35px) to create navigational signposts that contrast with the tight lowercase text.

## Layout

### Spacing System
- Base unit: 8px
- Scale: `{spacing.hair}` 4px, `{spacing.micro}` 6px, `{spacing.xs}` 8px, `{spacing.sm}` 12px, `{spacing.md}` 16px, `{spacing.md-alt}` 20px, `{spacing.lg}` 24px, `{spacing.lg-alt}` 28px, `{spacing.xl}` 32px, `{spacing.section}` 48px, `{spacing.section-lg}` 64px, `{spacing.section-xl}` 78px
- Section vertical spacing: generous (48–78px)
- Component gaps: 16–24px

### Grid & Container
- Max container width: up to 1600px (cinema-wide)
- Hero: full-viewport, edge-to-edge
- Content sections: centered with generous margins
- Image grids: asymmetric, magazine-style mixed sizes
- Footer: full-width dark section

### Whitespace Philosophy
- **Cinema-grade breathing**: Large vertical gaps between sections create a scrolling experience that feels like watching scenes change.
- **Images replace whitespace**: Where other sites use empty space, Runway fills it with photography. The visual content IS the breathing room.
- **Editorial grid asymmetry**: The image grid uses intentionally varied sizes — large hero images paired with smaller supporting images, creating visual rhythm.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Everything — the dominant state |
| Bordered (Level 1) | `1px solid {colors.border-dark}` | Alert containers only |
| Dark Section (Level 2) | Dark bg (`{colors.canvas}` / `{colors.surface-dark}`) with light text | Hero, features, footer |
| Light Section (Level 3) | `{colors.surface-light}` / `{colors.surface-light-cool}` bg with dark text | Content sections, research |

**Shadow Philosophy**: Runway uses **zero shadows**. This is a film-production design decision — in cinema, depth comes from lighting, focus, and composition, not drop shadows. The interface mirrors this philosophy: depth is communicated through dark/light section alternation, photographic depth-of-field, and overlay transparency — never through CSS box-shadow. There is consequently **no `shadow:` token group** in this file, and nothing in the prose references one.

**Elevation is expressed one way only**: by changing the ground, not by mixing shadow and border at random. Level 1 is the single exception and is scoped to alert containers. The step from `{colors.canvas}` to `{colors.surface-dark}` measures **1.21:1** — a card on the page floor is, by design, almost indistinguishable from it; the image inside the card is what separates the two, not the surface.

## Shapes

### Border Radius Scale
- Sharp (`{rounded.sharp}` — 4px): Buttons, small interactive elements
- Subtle (`{rounded.subtle}` — 6px): Links, small containers
- Comfortable (`{rounded.comfortable}` — 8px): Standard containers, image cards
- Generous (`{rounded.generous}` — 16px): Alert-style containers, featured elements

The ladder is internally consistent — four values, each a step of its own, with no value sitting outside the scale. There is no pill or fully-round radius anywhere: Runway's geometry is subtly rounded, never circular.

## Components

Interaction states are the thinnest part of this document. The source records exactly one — the navigation hover — and the focus ring below is prescribed by the audit, not extracted. Every other state is marked as not documented rather than guessed at; see Known Gaps.

### Buttons
- `{components.button-link}` / `{components.button-dark}` — Text: weight 600 at 14px abcNormal (`{typography.caption}`)
- Background: likely transparent or dark, with minimal border (the source's own hedge — see Known Gaps)
- Radius: `{rounded.sharp}` (4px) for button-like links
- The button design is extremely restrained — no heavy fills or borders detected
- Interactive elements blend into the editorial flow
- **Hover**: text shifts to `{colors.ink}` or higher opacity, as documented for navigation
- **Focus-visible** (prescribed): 2px `{colors.focus}` ring at a 2px offset, drawn outside the control
- Pressed, disabled, loading, selected and error: not documented on the live site

### Cards & Containers
- `{components.card-dark}` — Background transparent or Dark Surface (`{colors.surface-dark}`)
- `{components.card-light}` — `{colors.surface-light-cool}` with `{colors.on-light}` text, for light research sections
- Border: `1px solid {colors.border-dark}` (dark mode) — barely visible containment
- Radius: `{rounded.sharp}`–`{rounded.comfortable}` (4–8px) for functional elements; `{rounded.generous}` (16px) for alert-style containers (`{components.alert-container}`)
- Shadow: zero — no shadows on any element
- Cards are primarily photographic — the image IS the card
- **Focus-visible** (prescribed): where a card is wholly a link, the 2px `{colors.focus}` ring is drawn on the card edge
- Hover, pressed, disabled, loading, selected and error: not documented on the live site

### Navigation
- `{components.top-nav}` — Minimal horizontal nav — transparent over hero content
- Logo: Runway wordmark in white/black
- Links: abcNormal at 16px (`{typography.body}`), weight 400–600
- **Hover**: text shifts to `{colors.ink}` or higher opacity — the one interaction state the source records
- **Focus-visible** (prescribed): 2px `{colors.focus}` ring at a 2px offset
- Extremely subtle — designed to not compete with visual content
- Pressed, disabled, loading, selected and error: not documented on the live site

### Image Treatment
- `{components.image-frame}` — Full-bleed cinematic photography and video dominate
- AI-generated content shown at large scale as primary visual elements
- Mixed-size image grids creating editorial magazine layouts
- Dark overlays on hero images for text readability
- Product screenshots with subtle rounded corners (`{rounded.comfortable}` — 8px)
- **Default state only** where the image is not itself a link; a linked image takes the hover and prescribed focus-visible treatment of its card

### Distinctive Components

**Cinematic Hero** (`{components.hero-cinematic}`)
- Full-viewport image or video with text overlay
- Headline in 48px abcNormal (`{typography.display-hero}`), `{colors.ink}` on dark imagery
- The image is always cinematic quality — film-grade composition
- **Default state only** — this is a static full-bleed frame with no interactive affordance of its own

**Research Article Cards** (`{components.article-card-dark}` / `{components.article-card-light}`)
- Photographic thumbnails with article titles
- Mixed-size grid layout (large feature + smaller supporting)
- Clean text overlay or below-image caption style
- Titles in `{colors.ink}` on dark grounds, `{colors.on-light}` on light grounds
- **Hover** and prescribed **focus-visible** as for Cards; pressed, disabled, loading, selected and error not documented

**Section Label** (`{components.section-label}`)
- 14px abcNormal weight 500, uppercase, letter-spacing 0.35px, in `{colors.text-secondary}`
- No border, no background
- **Default state only** — a non-interactive signpost

**Trust Bar** (`{components.trust-bar}`)
- Company logos (leading organizations across industries)
- Clean, monochrome treatment
- Horizontal layout with generous spacing (`{spacing.section}`)
- **Default state only** — the logos are not links on the live site as recorded

**Mission Statement** (`{components.mission-statement}`)
- "We are building AI to simulate the world through imagination, art and aesthetics"
- On a dark background (`{colors.canvas}`) with `{colors.ink}` text at `{typography.sub-heading}`
- The emotional close — artistic and philosophical
- **Default state only**

**Footer** (`{components.footer}`)
- Full-width dark section on `{colors.canvas}` with `{colors.muted-footer}` links at `{typography.body}`
- **Hover**: link lifts toward `{colors.ink}`, consistent with the navigation rule
- **Focus-visible** (prescribed): 2px `{colors.focus}` ring
- Pressed, disabled, loading, selected and error: not documented on the live site

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or choreography below was extracted from runwayml.com; the values are the shared **Cinematic** profile from `theme-audit/SPEC.md` section 5, carried verbatim in the `motion:` frontmatter group so every Cinematic file in this collection behaves as a sibling.

Cinematic is the right profile here, and it is reached on the assignment rule's own tell rather than on the dark canvas: full-bleed photography and video as the primary UI elements, sparse display type at line-height 1.0, and a scroll built so that "each section transition is a scroll through darkness into the next revelation". The file's own words are "cinematic reel". Only `transform` and `opacity` are animated — never `width`, `height`, `top`, `left` or `margin`.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` of text and image (the one documented hover is an opacity lift) | Same crossfade, capped at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` only — no scale pop, since the interface must stay invisible | Unchanged; already at `{motion.duration-reduced}` or below |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Ring appears instantly and is never suppressed |
| Page / route transition | `{motion.duration-emphasis}` | `{motion.ease-enter}` | `opacity` 0→1, `transform: translateY(24px)`→0 | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(32px)`→0 | Travel removed; scrim fades at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-base}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| List enter (image grid) | `{motion.duration-base}`, staggered by `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px)`→0 | Stagger and travel removed; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading | 1600ms, infinite | linear | `opacity` pulse on the image placeholder — never a layout-affecting skeleton | Loader frozen; a static placeholder remains |
| Hero reveal, then continuous slow scale — **stated here as deliberate brand ambience** | `{motion.duration-emphasis}` on reveal | `{motion.ease-enter}` | `opacity`, `transform: scale(1)`→`scale(1.04)` | Ambience frozen at `scale(1)`; video paused and its poster frame shown |

Exit is always shorter than its matching entrance. Nothing animates on first paint in a way that delays content: hero type fades in after the video's first frame has painted and never gates it.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: every translate, every scale, the hero's continuous scale
     ambience, the image-placeholder loader pulse, and the grid stagger. */
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

Every ratio below is computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. **The extracted brand values are frozen: the failures listed here are real failures of the live Runway interface, disclosed rather than corrected.** The headline finding is that Runway's cool-gray secondary scale was chosen against the black canvas and does not survive the move onto `{colors.surface-dark}`, and that all three of its documented hairlines are invisible by design.

### Measured contrast — key pairs

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `ink` #ffffff on `canvas` #000000 | 21.00:1 | 4.5:1 | Pass |
| `ink` #ffffff on `canvas-deep` #030303 | 20.62:1 | 4.5:1 | Pass |
| `ink` #ffffff on `surface-dark` #1a1a1a | 17.40:1 | 4.5:1 | Pass |
| `muted` #a7a7a7 on `canvas` | 8.73:1 | 4.5:1 | Pass |
| `muted` #a7a7a7 on `surface-dark` | 7.23:1 | 4.5:1 | Pass |
| `muted-footer` #999999 on `canvas` | 7.37:1 | 4.5:1 | Pass |
| `muted-footer` #999999 on `surface-dark` | 6.11:1 | 4.5:1 | Pass |
| `text-tertiary` #7d848e on `canvas` | 5.56:1 | 4.5:1 | Pass |
| `text-tertiary` #7d848e on `surface-dark` | 4.61:1 | 4.5:1 | Pass — with almost no margin |
| `text-secondary` #767d88 on `canvas` | 5.06:1 | 4.5:1 | Pass |
| `text-secondary` #767d88 on `surface-dark` | 4.19:1 | 4.5:1 | **Fail — real brand failure.** Cool Slate was chosen against the black canvas; on a #1a1a1a card it misses AA. Step up to `{colors.text-tertiary}` or `{colors.muted}` on cards |
| `text-soft` #6b7280 on `canvas` | 4.34:1 | 4.5:1 | **Fail — real brand failure.** Tailwind Gray misses AA on the canvas by a hair; defensible only at 18.66px+/700 or 24px+, where the 3:1 large-text threshold applies |
| `text-soft` #6b7280 on `surface-dark` | 3.60:1 | 4.5:1 | **Fail — real brand failure.** Not usable as body text on a dark card |
| `ink-secondary-alt` #3f3f3f on `canvas` | 1.99:1 | 4.5:1 | **Fail — real brand failure.** The source calls Near Charcoal "dark-section secondary text"; it is effectively invisible there. Treat it as a light-surface ink or as decoration only |
| `ink-secondary-alt` #3f3f3f on `surface-dark` | 1.65:1 | 4.5:1 | **Fail — real brand failure** |
| `on-light` #404040 on `surface-light` #fefefe | 10.28:1 | 4.5:1 | Pass |
| `on-light` #404040 on `surface-light-cool` #e9ecf2 | 8.76:1 | 4.5:1 | Pass |
| `link-on-light` #0c0c0c on `surface-light` | 19.40:1 | 4.5:1 | Pass |
| `link-on-light` #0c0c0c on `surface-light-cool` | 16.53:1 | 4.5:1 | Pass |
| `text-secondary` #767d88 as an ink on `surface-light` | 4.12:1 | 4.5:1 | **Fail — real brand failure.** The source's own example prompt puts Cool Slate section labels on light research sections |
| `text-secondary` #767d88 as an ink on `surface-light-cool` | 3.51:1 | 4.5:1 | **Fail — real brand failure.** On Cool Cloud, Cool Slate is a decorative tone, not a text tone |
| `border-dark` #27272a on `canvas` | 1.41:1 | 3:1 | **Fail — frozen decorative hairline.** "Barely visible containment" is the source's own phrase; never the sole boundary of a control |
| `border-dark` #27272a on `surface-dark` | 1.17:1 | 3:1 | **Fail — frozen decorative hairline**, effectively invisible on the card it contains |
| `border-light-cool` #c9ccd1 on `surface-light` | 1.60:1 | 3:1 | **Fail — frozen decorative hairline** |
| `border-light-cool` #c9ccd1 on `surface-light-cool` #e9ecf2 | 1.36:1 | 3:1 | **Fail — frozen decorative hairline.** This is the pair `{components.card-light}` actually binds: a Cool Silver hairline on a Cool Cloud card, two neighbours on the same cool-gray ramp |
| `border-light-silver` #d0d4d4 on `surface-light` | 1.48:1 | 3:1 | **Fail — frozen decorative hairline** |
| `text-secondary` #767d88 as a boundary on `canvas` | 5.06:1 | 3:1 | Pass — the perceivable boundary, reusing a tone the palette already owns rather than a new token |
| `text-secondary` #767d88 as a boundary on `surface-light-cool` | 3.51:1 | 3:1 | Pass — its worst case across all six surfaces |
| `surface-dark` #1a1a1a against `canvas` #000000 | 1.21:1 | — | Layer separation, not a WCAG pair: the card is near-indistinguishable from the page floor by design |
| `canvas-deep` #030303 against `canvas` #000000 | 1.02:1 | — | "Near-imperceptible" is the source's own description |

### Component pairs

| Component | Measured | Required | Verdict |
|---|---|---|---|
| `hero-cinematic` — #ffffff on #000000 | 21.00:1 | 4.5:1 | Pass |
| `card-dark` — #ffffff on #1a1a1a | 17.40:1 | 3:1 large (24px) | Pass |
| `card-light` — #404040 on #e9ecf2 | 8.76:1 | 3:1 large (24px) | Pass |
| `article-card-light` — #404040 on #fefefe | 10.28:1 | 3:1 large (24px) | Pass |
| `alert-container` — #ffffff on #1a1a1a | 17.40:1 | 4.5:1 | Pass |
| `button-dark` — #ffffff on #1a1a1a | 17.40:1 | 4.5:1 | Pass |
| `section-label` — #767d88 on #000000 at 14px | 5.06:1 | 4.5:1 | Pass on the canvas; **fails on either light surface** (4.12:1 / 3.51:1) |
| `trust-bar` — #ffffff on #000000 at 11px | 21.00:1 | 4.5:1 | Pass |
| `mission-statement` — #ffffff on #000000 | 21.00:1 | 3:1 large (36px) | Pass |
| `footer` — #999999 on #000000 | 7.37:1 | 4.5:1 | Pass |
| `link-light` — #0c0c0c on #fefefe | 19.40:1 | 4.5:1 | Pass |

### Focus ring visibility on every surface this file defines

`{colors.focus}` (#767d88) is drawn as a 2px ring with a 2px offset, outside the control, so it is judged against the surface behind it. **Prescribed, not extracted.** It reuses Cool Slate, an existing brand tone, so no new colour enters a palette whose first rule is that it has none.

| Surface it is drawn on | Measured | Required | Verdict |
|---|---|---|---|
| `canvas` #000000 | 5.06:1 | 3:1 | Pass |
| `canvas-deep` #030303 | 4.97:1 | 3:1 | Pass |
| `surface-dark` #1a1a1a | 4.19:1 | 3:1 | Pass |
| `surface-light` #fefefe | 4.12:1 | 3:1 | Pass |
| `ink` #ffffff as a light band | 4.15:1 | 3:1 | Pass |
| `surface-light-cool` #e9ecf2 | 3.51:1 | 3:1 | Pass |

Over full-bleed photography and video, which has no measurable colour, the ring is two-tone: 2px `{colors.focus}` with a 1px outer edge in `{colors.ink}` over dark imagery and in `{colors.canvas}` over light imagery. A single-tone ring cannot be guaranteed on a surface that is literally a film frame.

### Minimum tap target
The source records navigation links at 16px, article cards acting as large touch targets, and buttons at 14px weight 600 "with adequate padding" — it states no pixel height for any of them. Nothing here clears or fails the 44×44px minimum **as documented**, because the document does not say. This is a document, not a rendered page, so no tap target was measured; the gap is recorded in Known Gaps.

### Reduced motion
`@media (prefers-reduced-motion: reduce)` removes every translate and scale, freezes the hero's scale ambience, and drops the image-grid stagger and the placeholder pulse. Opacity fades remain, capped at `{motion.duration-reduced}` (150ms). The focus ring is never animated away.

## Do's and Don'ts

### Do
- Use full-bleed cinematic photography as the primary visual element
- Use abcNormal for all text — maintain the single-typeface commitment
- Keep display line-heights at 1.0 with negative letter-spacing for film-title density
- Use the cool-gray neutral palette (`{colors.text-secondary}`, `{colors.text-tertiary}`) for secondary text
- Maintain zero shadows — depth comes from photography and section backgrounds
- Use uppercase with letter-spacing for navigational labels (14px, 0.35px spacing)
- Apply small border-radius (`{rounded.sharp}`–`{rounded.comfortable}`) — the design is NOT pill-shaped
- Let visual content (photos, videos) dominate — the UI should be invisible
- Use weight 450 for micro labels — the precision matters
- Draw any boundary that must actually be seen in `{colors.text-secondary}`, and keep the three extracted hairlines for decoration

### Don't
- Don't add decorative colors to the interface — the only color comes from photography
- Don't use heavy borders or shadows — the interface must be nearly invisible
- Don't use pill-shaped radius — Runway's geometry is subtly rounded, not circular
- Don't use bold (700+) weight — 400–600 is the full range, with 450 as a precision tool
- Don't compete with the visual content — text overlays should be minimal and restrained
- Don't use gradient backgrounds in the interface — gradients exist only in photography
- Don't use more than one typeface — abcNormal handles everything
- Don't use body line-height above 1.50 — the tight, editorial feel is core
- Don't reduce image quality — cinematic photography IS the design
- Don't put `{colors.text-secondary}` body copy on `{colors.surface-dark}` or on either light surface — it misses AA on all three
- Don't animate `width`, `height`, `top`, `left` or `margin` — `transform` and `opacity` only

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, stacked images, reduced hero text |
| Tablet | 640–768px | 2-column image grids begin |
| Small Desktop | 768–1024px | Standard layout |
| Desktop | 1024–1280px | Full layout, expanded hero |
| Large Desktop | 1280–1600px | Maximum cinema-width container |

### Touch Targets
- Navigation links at comfortable 16px
- Article cards serve as large touch targets
- Buttons at 14px weight 600 with adequate padding

### Collapsing Strategy
- **Navigation**: Collapses to hamburger on mobile
- **Hero**: Full-bleed maintained, text scales down
- **Image grids**: Multi-column → 2-column → single column
- **Research articles**: Feature-size cards → stacked full-width
- **Trust logos**: Horizontal scroll or reduced grid

### Image Behavior
- Cinematic images scale proportionally
- Full-bleed hero maintained across all sizes
- Image grids reflow to fewer columns
- Video content maintains aspect ratio

## Known Gaps

This file was one of the collection's ten legacy documents: it carried no frontmatter token block and used numbered headings. The `colors`, `typography`, `spacing`, `rounded` and `components` groups above were built **only** from values already written in its prose. Nothing was invented to fill a column. What the prose does not contain is listed here.

- **No accent colour, and therefore no `on-accent`.** Both required roles are left unfilled. This is not a naming problem: the source states the interface is "intentionally colorless", that all colour comes from photography, and its Don'ts forbid adding decorative colour. Aliasing `accent` onto `{colors.ink}` would have satisfied the role pattern and falsified the brand, so the point is accepted as lost. Runway's signal is white type on black plus the imagery.
- **Interaction states are almost entirely absent.** The source documents exactly one — the navigation hover ("text shifts to white or higher opacity"). Pressed, disabled, loading, selected and error states appear nowhere in the file, for any component, and no error, success or warning tone exists in the palette to express them. The Components section above therefore *marks* state coverage rather than filling it. The focus-visible treatment is prescribed by this audit and labelled as such.
- **No focus treatment was extracted.** `{colors.focus}` is prescribed and reuses Cool Slate. The live site's focus appearance is unknown.
- **Button fill and border are hedged in the source itself**: "Background: likely transparent or dark, with minimal border" and "no heavy fills or borders detected". The word *likely* is the source's, and `{components.button-link}` / `{components.button-dark}` record both readings rather than picking one. Button padding and height are not stated anywhere.
- **No tap-target dimensions.** The source gives font sizes and "adequate padding" but no pixel height for any control, so the 44×44px minimum can be neither confirmed nor failed from this document.
- **No shadow values and no `shadow:` group.** This is a documented brand decision, not a gap in extraction: Runway uses zero shadows.
- **No motion values.** Nothing in the source describes a duration, easing curve, transition or scroll animation. The entire `motion:` group and Motion & Animation section are the prescribed Cinematic profile, as their first lines state.
- **Overlay opacity is unquantified.** "Dark overlays on hero images for text readability" and "overlay transparency" are described with no rgba value, so no overlay token exists.
- **Line-height and letter-spacing ranges are recorded as ranges** (`1.00-1.10`, `-1px to 0px`) because the source states them as ranges; no single canonical value was picked.
- **Two near-duplicate tones are kept as extracted** rather than merged: `{colors.canvas}` / `{colors.canvas-deep}` (1.02:1 apart) and `{colors.on-light}` / `{colors.ink-secondary-alt}` (#404040 / #3f3f3f). They are facts about the real site.
- **Polarity is unstated for several neutrals.** `{colors.text-soft}` (Tailwind Gray) and `{colors.muted}` (Muted Gray) are described without saying which ground they sit on; they are measured against both polarities in Accessibility and the failures disclosed there.

## Agent Prompt Guide

### Quick Color Reference
- Background Dark: "Runway Black (#000000)"
- Background Light: "Pure White (#ffffff)"
- Primary Text Dark: "Charcoal (#404040)"
- Secondary Text: "Cool Slate (#767d88)"
- Muted Text: "Muted Gray (#a7a7a7)"
- Light Border: "Cool Silver (#c9ccd1)"
- Dark Border: "Border Dark (#27272a)"
- Card Surface: "Dark Surface (#1a1a1a)"

### Example Component Prompts
- "Create a cinematic hero section: full-bleed dark background with a cinematic image overlay. Headline at 48px abcNormal weight 400, line-height 1.0, letter-spacing -1.2px in white. Minimal text below in Cool Slate (#767d88) at 16px."
- "Design a research article grid: one large card (50% width) with a cinematic image and 24px title, next to two smaller cards stacked. All images with 8px border-radius. Titles in white (dark bg) or Charcoal (#404040, light bg)."
- "Build a section label: 14px abcNormal weight 500, uppercase, letter-spacing 0.35px in Cool Slate (#767d88). No border, no background."
- "Create a trust bar: company logos in monochrome, horizontal layout with generous spacing. On dark background with white/gray logo treatments."
- "Design a mission statement section: Runway Black background, white text at 36px abcNormal, line-height 1.0, letter-spacing -0.9px. Centered, with generous vertical padding."

### Iteration Guide
1. Visual content first — always include cinematic photography
2. Use abcNormal for everything — specify size and weight, never change the font
3. Keep the interface invisible — no heavy borders, no shadows, no bright colors
4. Use the cool slate grays (#767d88, #7d848e) for secondary text — not warm grays
5. Uppercase labels need letter-spacing (0.35px) — never tight uppercase
6. Dark sections should be truly dark (#000000 or #1a1a1a) — no medium grays as surfaces
