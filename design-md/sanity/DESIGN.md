---
version: alpha
name: Sanity-Inspired-design-analysis
description: "A developer-content platform rendered as a nocturnal command center: a near-black canvas (#0b0b0b) carrying a purely achromatic grey ramp, waldenburgNormal display type with extreme negative tracking (-4.48px at 112px), IBM Plex Mono for technical labels, and three vivid punctuation colours — coral-red CTA (#f36458), electric blue (#0052ef) as the universal hover signal, and a wide-gamut neon green. Depth is colorimetric, never shadowed; primary buttons are full pills, everything else is a 3-12px rounded rectangle."

colors:
  canvas: "#0b0b0b"
  canvas-void: "#000000"
  surface: "#212121"
  surface-raised: "#353535"
  surface-inverse: "#ffffff"
  surface-inverse-soft: "#ededed"
  ink: "#ffffff"
  ink-muted: "#b9b9b9"
  ink-tertiary: "#797979"
  ink-on-light: "#212121"
  ink-on-light-deep: "#0b0b0b"
  primary: "#f36458"
  on-primary: "#ffffff"
  accent-blue: "#0052ef"
  accent-blue-light: "#55beff"
  accent-blue-pale: "#afe3ff"
  accent-green: "#19d600"
  accent-green-p3: "color(display-p3 .270588 1 0)"
  accent-magenta-p3: "color(display-p3 .960784 0 1)"
  error: "#dd0000"
  success-gpc: "#37cd84"
  border-dark: "#0b0b0b"
  border-subtle: "#212121"
  border-strong: "#353535"
  border-inverse: "#ffffff"
  border-control: "#797979"
  border-accent-orange-p3: "color(display-p3 1 0.3333 0)"
  focus: "#55beff"
  focus-on-light: "#0052ef"
  input-focus-bg: "#072227"

typography:
  display-hero:
    fontFamily: waldenburgNormal
    fontSize: 112px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -4.48px
  hero-secondary:
    fontFamily: waldenburgNormal
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -2.88px
  section-heading:
    fontFamily: waldenburgNormal
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -1.68px
  heading-lg:
    fontFamily: waldenburgNormal
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: -1.14px
  heading-md:
    fontFamily: waldenburgNormal
    fontSize: 32px
    fontWeight: 425
    lineHeight: 1.24
    letterSpacing: -0.32px
  heading-sm:
    fontFamily: waldenburgNormal
    fontSize: 24px
    fontWeight: 425
    lineHeight: 1.24
    letterSpacing: -0.24px
  subheading:
    fontFamily: waldenburgNormal
    fontSize: 20px
    fontWeight: 425
    lineHeight: 1.13
    letterSpacing: -0.2px
  body-lg:
    fontFamily: waldenburgNormal
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.18px
  body:
    fontFamily: waldenburgNormal
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: normal
  body-sm:
    fontFamily: waldenburgNormal
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.15px
  caption:
    fontFamily: waldenburgNormal
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.13px
  caption-sm:
    fontFamily: waldenburgNormal
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.12px
  micro-label:
    fontFamily: waldenburgNormal
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: normal
  code-body:
    fontFamily: IBM Plex Mono
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: normal
  code-caption:
    fontFamily: IBM Plex Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: normal
  code-micro:
    fontFamily: IBM Plex Mono
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: normal

spacing:
  space-1: 1px
  space-2: 2px
  space-3: 4px
  space-4: 6px
  space-5: 8px
  space-6: 12px
  space-7: 16px
  space-8: 24px
  space-9: 32px
  space-10: 48px
  space-11: 64px
  space-12: 96px

rounded:
  xs: 3px
  sm: 5px
  md: 6px
  lg: 12px
  pill: 99999px

shadow:
  flat: none
  ring-subtle: "0 0 0 1px #212121"
  ring-focus-extracted: "0 0 0 2px var(--color-blue-500)"
  ring-focus: "0 0 0 2px #55beff"
  overlay: "backdrop-filter blur over semi-transparent #0b0b0b — blur radius and alpha are not stated in the source file"

motion:
  duration-instant: 60ms
  duration-fast: 100ms
  duration-base: 150ms
  duration-slow: 220ms
  duration-emphasis: 300ms
  ease-standard: cubic-bezier(0.2, 0, 0.2, 1)
  ease-enter: cubic-bezier(0, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 20ms
  duration-reduced: 100ms

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 12px
  button-outlined:
    backgroundColor: "{colors.surface-inverse}"
    textColor: "{colors.ink-on-light-deep}"
    typography: "{typography.body}"
    borderColor: "{colors.border-dark}"
    rounded: "{rounded.pill}"
    padding: 8px
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.sm}"
    padding: 0px 12px
  button-label-uppercase:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.sm}"
    padding: 0px 12px
  card-dark:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    borderColor: "{colors.border-strong}"
    rounded: "{rounded.md}"
    padding: 24px
  card-feature:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.lg}"
    padding: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  text-input-focused:
    backgroundColor: "{colors.input-focus-bg}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    ringColor: "{colors.focus}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 0px 12px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    borderColor: "{colors.border-subtle}"
    padding: 8px 32px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    padding: 64px 32px
  badge-neutral-subtle:
    backgroundColor: "{colors.surface-inverse}"
    textColor: "{colors.ink-on-light-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-neutral-filled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 8px
---

# Design System Inspired by Sanity

## Overview


Sanity's website is a developer-content platform rendered as a nocturnal command center -- dark, precise, and deeply structured. The entire experience sits on a near-black canvas (`#0b0b0b`) that reads less like a "dark mode toggle" and more like the natural state of a tool built for people who live in terminals. Where most CMS marketing pages reach for friendly pastels and soft illustration, Sanity leans into the gravity of its own product: structured content deserves a structured stage.

The signature typographic voice is waldenburgNormal -- a distinctive, slightly geometric sans-serif with tight negative letter-spacing (-0.32px to -4.48px at display sizes) that gives headlines a compressed, engineered quality. At 112px hero scale with -4.48px tracking, the type feels almost machined -- like precision-cut steel letterforms. This is paired with IBM Plex Mono for code and technical labels, creating a dual-register voice: editorial authority meets developer credibility.

What makes Sanity distinctive is the interplay between its monochromatic dark palette and vivid, saturated accent punctuation. The neutral scale runs from pure black through a tightly controlled gray ramp (`#0b0b0b` -> `#212121` -> `#353535` -> `#797979` -> `#b9b9b9` -> `#ededed` -> `#ffffff`) with no warm or cool bias -- just pure, achromatic precision. Against this disciplined backdrop, a neon green accent (display-p3 green) and electric blue (`#0052ef`) land with the impact of signal lights in a dark control room. The orange-red CTA (`#f36458`) provides the only warm touch in an otherwise cool system.

**Key Characteristics:**
- Near-black canvas (`#0b0b0b`) as the default, natural environment -- not a dark "mode" but the primary identity
- waldenburgNormal with extreme negative tracking at display sizes, creating a precision-engineered typographic voice
- Pure achromatic gray scale -- no warm or cool undertones, pure neutral discipline
- Vivid accent punctuation: neon green, electric blue (`#0052ef`), and coral-red (`#f36458`) against the dark field
- Pill-shaped primary buttons (99999px radius) contrasting with subtle rounded rectangles (3-6px) for secondary actions
- IBM Plex Mono as the technical counterweight to the editorial display face
- Full-bleed dark sections with content contained in measured max-width containers
- Hover states that shift to electric blue (`#0052ef`) across all interactive elements -- a consistent "activation" signal

## Colors


### Primary Brand
- **Sanity Black** (`#0b0b0b`): The primary canvas and dominant surface color. Not pure black but close enough to feel absolute. The foundation of the entire visual identity.
- **Pure Black** (`#000000`): Used for maximum-contrast moments, deep overlays, and certain border accents.
- **Sanity Red** (`#f36458`): The primary CTA and brand accent -- a warm coral-red that serves as the main call-to-action color. Used for "Get Started" buttons and primary conversion points.

### Accent & Interactive
- **Electric Blue** (`#0052ef`): The universal hover/active state color across the entire system. Buttons, links, and interactive elements all shift to this blue on hover. Also used as `--color-blue-700` for focus rings and active states.
- **Light Blue** (`#55beff` / `#afe3ff`): Secondary blue variants used for accent backgrounds, badges, and dimmed blue surfaces.
- **Neon Green** (`color(display-p3 .270588 1 0)`): A vivid, wide-gamut green used as `--color-fg-accent-green` for success states and premium feature highlights. Falls back to `#19d600` in sRGB.
- **Accent Magenta** (`color(display-p3 .960784 0 1)`): A vivid wide-gamut magenta for specialized accent moments.

### Surface & Background
- **Near Black** (`#0b0b0b`): Default page background and primary surface.
- **Dark Gray** (`#212121`): Elevated surface color for cards, secondary containers, input backgrounds, and subtle layering above the base canvas.
- **Medium Dark** (`#353535`): Tertiary surface and border color for creating depth between dark layers.
- **Pure White** (`#ffffff`): Used for inverted sections, light-on-dark text, and specific button surfaces.
- **Light Gray** (`#ededed`): Light surface for inverted/light sections and subtle background tints.

### Neutrals & Text
- **White** (`#ffffff`): Primary text color on dark surfaces, maximum legibility.
- **Silver** (`#b9b9b9`): Secondary text, body copy on dark surfaces, muted descriptions, and placeholder text.
- **Medium Gray** (`#797979`): Tertiary text, metadata, timestamps, and de-emphasized content.
- **Charcoal** (`#212121`): Text on light/inverted surfaces.
- **Near Black Text** (`#0b0b0b`): Primary text on white/light button surfaces.

### Semantic
- **Error Red** (`#dd0000`): Destructive actions, validation errors, and critical warnings -- a pure, high-saturation red.
- **GPC Green** (`#37cd84`): Privacy/compliance indicator green.
- **Focus Ring Blue** (`#0052ef`): Focus ring color for accessibility, matching the interactive blue.

### Border System
- **Dark Border** (`#0b0b0b`): Primary border on dark containers -- barely visible, maintaining minimal containment.
- **Subtle Border** (`#212121`): Standard border for inputs, textareas, and card edges on dark surfaces.
- **Medium Border** (`#353535`): More visible borders for emphasized containment and dividers.
- **Light Border** (`#ffffff`): Border on inverted/light elements or buttons needing contrast separation.
- **Orange Border** (`color(display-p3 1 0.3333 0)`): Special accent border for highlighted/featured elements.

### Focus

- **Focus Ring, dark surfaces** ({colors.focus}): **Prescribed, not extracted.** `#55beff` — the brand's own Light Blue, reused as the ring on every dark ground. No new colour enters the palette. Drawn as a 2px outline with a 2px `{colors.canvas}` offset, so the ring sits on the surface behind the control rather than on the control's own fill. It clears 3:1 on `{colors.canvas}`, `{colors.canvas-void}`, `{colors.surface}`, `{colors.surface-raised}` and `{colors.input-focus-bg}` — see **Accessibility**.
- **Focus Ring, light surfaces** ({colors.focus-on-light}): `#0052ef` — the ring Sanity actually ships (`--color-blue-700`), kept as an extracted fact and used where it works: the inverted white and `#ededed` bands. This file documents both a near-black canvas and pure-white inverted sections, so one ring cannot serve both polarities.
- The extracted `#0052ef` ring is correct on the canvas itself (3.24:1) but drops to 2.65:1 on `{colors.surface}` and 2.02:1 on `{colors.surface-raised}`, which is why `{colors.focus}` exists for dark grounds. Both ratios are recorded in **Accessibility**.
- **Control Boundary** ({colors.border-control}): **Prescribed, not extracted.** `#797979` — the palette's own Medium Gray, promoted to carry any boundary that is the *only* thing defining an interactive control: text-input and textarea edges, checkbox and radio outlines, segmented-control dividers. All four extracted borders fail the 3:1 non-text threshold on every surface in this file, so they are scoped to decoration. No new hue is introduced.

### Token Map

Every hex above, as the token the rest of this document references.

| Token | Value | Role |
|---|---|---|
| `{colors.canvas}` | `#0b0b0b` | page floor — Sanity Black |
| `{colors.canvas-void}` | `#000000` | maximum-contrast moments, deep overlays |
| `{colors.surface}` | `#212121` | elevated cards, containers, input chrome |
| `{colors.surface-raised}` | `#353535` | tertiary surface, one step above `{colors.surface}` |
| `{colors.surface-inverse}` | `#ffffff` | inverted sections, light button surfaces |
| `{colors.surface-inverse-soft}` | `#ededed` | light surface for inverted sections, subtle tints |
| `{colors.ink}` | `#ffffff` | primary text and headlines on dark |
| `{colors.ink-muted}` | `#b9b9b9` | secondary text, body copy, placeholders — Silver |
| `{colors.ink-tertiary}` | `#797979` | metadata, timestamps, de-emphasised content |
| `{colors.ink-on-light}` | `#212121` | text on light / inverted surfaces — Charcoal |
| `{colors.ink-on-light-deep}` | `#0b0b0b` | text on white and light button surfaces |
| `{colors.primary}` | `#f36458` | the CTA accent — Sanity Red |
| `{colors.on-primary}` | `#ffffff` | the label Sanity draws on the CTA (fails AA — see **Accessibility**) |
| `{colors.accent-blue}` | `#0052ef` | the universal hover / active signal (`--color-fg-accent-blue`) |
| `{colors.accent-blue-light}` | `#55beff` | accent backgrounds, badges |
| `{colors.accent-blue-pale}` | `#afe3ff` | dimmed blue surfaces |
| `{colors.accent-green}` | `#19d600` | sRGB fallback of the neon green |
| `{colors.accent-green-p3}` | `color(display-p3 .270588 1 0)` | wide-gamut neon green (`--color-fg-accent-green`) |
| `{colors.accent-magenta-p3}` | `color(display-p3 .960784 0 1)` | wide-gamut magenta — no sRGB fallback is stated in the source |
| `{colors.error}` | `#dd0000` | destructive actions, validation errors |
| `{colors.success-gpc}` | `#37cd84` | privacy / compliance indicator green |
| `{colors.border-dark}` | `#0b0b0b` | barely-visible border on dark containers |
| `{colors.border-subtle}` | `#212121` | standard border for inputs, textareas, card edges |
| `{colors.border-strong}` | `#353535` | emphasised containment, dividers |
| `{colors.border-inverse}` | `#ffffff` | border on inverted / light elements |
| `{colors.border-control}` | `#797979` | **prescribed** accessible boundary for controls |
| `{colors.border-accent-orange-p3}` | `color(display-p3 1 0.3333 0)` | featured-element accent border — no sRGB fallback is stated |
| `{colors.focus}` | `#55beff` | **prescribed** focus ring, dark grounds |
| `{colors.focus-on-light}` | `#0052ef` | focus ring, inverted light grounds (extracted) |
| `{colors.input-focus-bg}` | `#072227` | deep-cyan input background while focused |

## Typography


### Font Family
- **Display / Headline**: `waldenburgNormal`, fallback: `waldenburgNormal Fallback, ui-sans-serif, system-ui`
- **Body / UI**: `waldenburgNormal`, fallback: `waldenburgNormal Fallback, ui-sans-serif, system-ui`
- **Code / Technical**: `IBM Plex Mono`, fallback: `ibmPlexMono Fallback, ui-monospace`
- **Fallback / CJK**: `Helvetica`, fallback: `Arial, Hiragino Sans GB, STXihei, Microsoft YaHei, WenQuanYi Micro Hei`

*Note: waldenburgNormal is a custom typeface. For external implementations, use Inter or Space Grotesk as the sans substitute (geometric, slightly condensed feel). IBM Plex Mono is available on Google Fonts.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero | waldenburgNormal | 112px (7rem) | 400 | 1.00 (tight) | -4.48px | Maximum impact, compressed tracking |
| Hero Secondary | waldenburgNormal | 72px (4.5rem) | 400 | 1.05 (tight) | -2.88px | Large section headers |
| Section Heading | waldenburgNormal | 48px (3rem) | 400 | 1.08 (tight) | -1.68px | Primary section anchors |
| Heading Large | waldenburgNormal | 38px (2.38rem) | 400 | 1.10 (tight) | -1.14px | Feature section titles |
| Heading Medium | waldenburgNormal | 32px (2rem) | 425 | 1.24 (tight) | -0.32px | Card titles, subsection headers |
| Heading Small | waldenburgNormal | 24px (1.5rem) | 425 | 1.24 (tight) | -0.24px | Smaller feature headings |
| Subheading | waldenburgNormal | 20px (1.25rem) | 425 | 1.13 (tight) | -0.2px | Sub-section markers |
| Body Large | waldenburgNormal | 18px (1.13rem) | 400 | 1.50 | -0.18px | Intro paragraphs, descriptions |
| Body | waldenburgNormal | 16px (1rem) | 400 | 1.50 | normal | Standard body text |
| Body Small | waldenburgNormal | 15px (0.94rem) | 400 | 1.50 | -0.15px | Compact body text |
| Caption | waldenburgNormal | 13px (0.81rem) | 400-500 | 1.30-1.50 | -0.13px | Metadata, descriptions, tags |
| Small Caption | waldenburgNormal | 12px (0.75rem) | 400 | 1.50 | -0.12px | Footnotes, timestamps |
| Micro / Label | waldenburgNormal | 11px (0.69rem) | 500-600 | 1.00-1.50 | normal | Uppercase labels, tiny badges |
| Code Body | IBM Plex Mono | 15px (0.94rem) | 400 | 1.50 | normal | Code blocks, technical content |
| Code Caption | IBM Plex Mono | 13px (0.81rem) | 400-500 | 1.30-1.50 | normal | Inline code, small technical labels |
| Code Micro | IBM Plex Mono | 10-12px | 400 | 1.30-1.50 | normal | Tiny code labels, uppercase tags |

### Principles
- **Extreme negative tracking at scale**: Display headings at 72px+ use aggressive negative letter-spacing (-2.88px to -4.48px), creating a tight, engineered quality that distinguishes Sanity from looser editorial typography.
- **Single font, multiple registers**: waldenburgNormal handles both editorial display and functional UI text. The weight range is narrow (400-425 for most, 500-600 only for tiny labels), keeping the voice consistent.
- **OpenType feature control**: Typography uses deliberate feature settings including `"cv01", "cv11", "cv12", "cv13", "ss07"` for display sizes and `"calt" 0` for body text, fine-tuning character alternates for different contexts.
- **Tight headings, relaxed body**: Headings use 1.00-1.24 line-height (extremely tight), while body text breathes at 1.50. This contrast creates clear visual hierarchy.
- **Uppercase for technical labels**: IBM Plex Mono captions and small labels frequently use `text-transform: uppercase` with tight line-heights, creating a "system readout" aesthetic for technical metadata.

## Layout


### Spacing System
Base unit: **8px**

| Token | Value | Usage |
|-------|-------|-------|
| space-1 | 1px | Hairline gaps, border-like spacing |
| space-2 | 2px | Minimal internal padding |
| space-3 | 4px | Tight component internal spacing |
| space-4 | 6px | Small element gaps |
| space-5 | 8px | Base unit -- button padding, input padding, badge padding |
| space-6 | 12px | Standard component gap, button horizontal padding |
| space-7 | 16px | Section internal padding, card spacing |
| space-8 | 24px | Large component padding, card internal spacing |
| space-9 | 32px | Section padding, container gutters |
| space-10 | 48px | Large section vertical spacing |
| space-11 | 64px | Major section breaks |
| space-12 | 96-120px | Hero vertical padding, maximum section spacing |

### Grid & Container
- Max content width: ~1440px (inferred from breakpoints)
- Page gutter: 32px on desktop, 16px on mobile
- Content sections use full-bleed backgrounds with centered, max-width content
- Multi-column layouts: 2-3 columns on desktop, single column on mobile
- Card grids: CSS Grid with consistent gaps (16-24px)

### Whitespace Philosophy
Sanity uses aggressive vertical spacing between sections (64-120px) to create breathing room on the dark canvas. Within sections, spacing is tighter (16-32px), creating dense information clusters separated by generous voids. This rhythm gives the page a "slides" quality -- each section feels like its own focused frame.

## Elevation & Depth


### Shadow System

| Level | Value | Usage |
|-------|-------|-------|
| Level 0 (Flat) | none | Default state for most elements -- dark surfaces create depth through color alone |
| Level 1 (Subtle) | 0px 0px 0px 1px `#212121` | Border-like shadow for minimal containment without visible borders |
| Level 2 (Focus) | 0 0 0 2px `var(--color-blue-500)` | Focus ring for inputs and interactive elements |
| Level 3 (Overlay) | Backdrop blur + semi-transparent dark | Navigation overlay, modal backgrounds |

### Depth Philosophy
Sanity's depth system is almost entirely **colorimetric** rather than shadow-based. Elevation is communicated through surface color shifts: `#0b0b0b` (ground) -> `#212121` (elevated) -> `#353535` (prominent) -> `#ffffff` (inverted/highest). This approach is native to dark interfaces where traditional drop shadows would be invisible. The few shadows that exist are ring-based (0px 0px 0px Npx) or blur-based (backdrop-filter) rather than offset shadows, maintaining the flat, precision-engineered aesthetic.

Border-based containment (1px solid `#212121` or `#353535`) serves as the primary spatial separator, with the border darkness calibrated to be visible but not dominant. The system avoids "floating card" aesthetics -- everything feels mounted to the surface rather than hovering above it.

## Shapes

### Border Radius Scale
| Token | Value | Usage |
|-------|-------|-------|
| radius-xs | 3px | Inputs, textareas, subtle rounding |
| radius-sm | 4-5px | Secondary buttons, small cards, tags |
| radius-md | 6px | Standard cards, containers |
| radius-lg | 12px | Large cards, feature containers, forms |
| radius-pill | 99999px | Primary buttons, badges, nav pills |

## Components


### Buttons

**Primary CTA (Pill)**
- Background: Sanity Red (`#f36458`)
- Text: White (`#ffffff`)
- Padding: 8px 16px
- Border Radius: 99999px (full pill)
- Border: none
- Hover: Electric Blue (`#0052ef`) background, white text
- Font: 16px waldenburgNormal, weight 400

**Secondary (Dark Pill)**
- Background: Near Black (`#0b0b0b`)
- Text: Silver (`#b9b9b9`)
- Padding: 8px 12px
- Border Radius: 99999px (full pill)
- Border: none
- Hover: Electric Blue (`#0052ef`) background, white text

**Outlined (Light Pill)**
- Background: White (`#ffffff`)
- Text: Near Black (`#0b0b0b`)
- Padding: 8px
- Border Radius: 99999px (full pill)
- Border: 1px solid `#0b0b0b`
- Hover: Electric Blue (`#0052ef`) background, white text

**Ghost / Subtle**
- Background: Dark Gray (`#212121`)
- Text: Silver (`#b9b9b9`)
- Padding: 0px 12px
- Border Radius: 5px
- Border: 1px solid `#212121`
- Hover: Electric Blue (`#0052ef`) background, white text

**Uppercase Label Button**
- Font: 11px waldenburgNormal, weight 600, uppercase
- Background: transparent or `#212121`
- Text: Silver (`#b9b9b9`)
- Letter-spacing: normal
- Used for tab-like navigation and filter controls

### Cards

**Dark Content Card**
- Background: `#212121`
- Border: 1px solid `#353535` or `#212121`
- Border Radius: 6px
- Padding: 24px
- Text: White (`#ffffff`) for titles, Silver (`#b9b9b9`) for body
- Hover: subtle border color shift or elevation change

**Feature Card (Full-bleed)**
- Background: `#0b0b0b` or full-bleed image/gradient
- Border: none or 1px solid `#212121`
- Border Radius: 12px
- Padding: 32-48px
- Contains large imagery with overlaid text

### Inputs

**Text Input / Textarea**
- Background: Near Black (`#0b0b0b`)
- Text: Silver (`#b9b9b9`)
- Border: 1px solid `#212121`
- Padding: 8px 12px
- Border Radius: 3px
- Focus: outline with `var(--focus-ring-color)` (blue), 2px solid
- Focus background: shifts to deep cyan (`#072227`)

**Search Input**
- Background: `#0b0b0b`
- Text: Silver (`#b9b9b9`)
- Padding: 0px 12px
- Border Radius: 3px
- Placeholder: Medium Gray (`#797979`)

### Navigation

**Top Navigation**
- Background: Near Black (`#0b0b0b`) with backdrop blur
- Height: auto, compact padding
- Logo: left-aligned, Sanity wordmark
- Links: waldenburgNormal 16px, Silver (`#b9b9b9`)
- Link Hover: Electric Blue via `--color-fg-accent-blue`
- CTA Button: Sanity Red pill button right-aligned
- Separator: 1px border-bottom `#212121`

**Footer**
- Background: Near Black (`#0b0b0b`)
- Multi-column link layout
- Links: Silver (`#b9b9b9`), hover to blue
- Section headers: White (`#ffffff`), 13px uppercase IBM Plex Mono

### Badges / Pills

**Neutral Subtle**
- Background: White (`#ffffff`)
- Text: Near Black (`#0b0b0b`)
- Padding: 8px
- Font: 13px
- Border Radius: 99999px

**Neutral Filled**
- Background: Near Black (`#0b0b0b`)
- Text: White (`#ffffff`)
- Padding: 8px
- Font: 13px
- Border Radius: 99999px

### State Coverage

The fills, borders, radii and hover colours above are extracted. Everything in the
**focus-visible**, **disabled**, **loading**, **selected** and **error** columns is
**prescribed** — the source pages show only resting and hover styling — and is built
from tokens this file already defines rather than from new values.

| Component | Default | Hover | Focus-visible | Active / pressed | Disabled | Loading | Selected | Error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.primary}` fill, `{colors.on-primary}` label, `{rounded.pill}` | `{colors.accent-blue}` fill, `{colors.ink}` label (`button-primary-hover`) — extracted | 2px `{colors.focus}` ring, 2px `{colors.canvas}` offset | fill holds `{colors.accent-blue}`, no travel | `{colors.surface}` fill, `{colors.ink-tertiary}` label, no hover | label holds its width, `{colors.on-primary}` spinner in the icon slot | none — the CTA is not a toggle | none — the button carries no error state |
| `button-secondary` | `{colors.canvas}` fill, `{colors.ink-muted}` label | `{colors.accent-blue}` fill, `{colors.ink}` label — extracted | 2px `{colors.focus}` ring, 2px `{colors.canvas}` offset | fill holds `{colors.accent-blue}` | `{colors.ink-tertiary}` label | spinner in `{colors.ink-muted}` | none | none |
| `button-outlined` | `{colors.surface-inverse}` fill, `{colors.ink-on-light-deep}` label, 1px `{colors.border-dark}` | `{colors.accent-blue}` fill, `{colors.ink}` label — extracted | 2px `{colors.focus-on-light}` ring, 2px `{colors.surface-inverse}` offset — the light-ground ring, not `{colors.focus}` | fill holds `{colors.accent-blue}` | `{colors.surface-inverse-soft}` fill, `{colors.ink-tertiary}` label | spinner in `{colors.ink-on-light-deep}` | none | none |
| `button-ghost` | `{colors.surface}` fill, `{colors.ink-muted}` label, 1px `{colors.border-subtle}`, `{rounded.sm}` | `{colors.accent-blue}` fill, `{colors.ink}` label — extracted | 2px `{colors.focus}` ring, 2px `{colors.canvas}` offset | fill holds `{colors.accent-blue}` | `{colors.ink-tertiary}` label, border `{colors.border-subtle}` | spinner in `{colors.ink-muted}` | none | none |
| `button-label-uppercase` | `{colors.surface}` or transparent, `{colors.ink-muted}` at `{typography.micro-label}` | text to `{colors.ink}` | 2px `{colors.focus}` ring at `{rounded.sm}` | same as selected | `{colors.ink-tertiary}` text | none | active tab: `{colors.ink}` text plus a `{colors.primary}` 2px underline — the `{colors.surface}` fill alone is 1.22:1 against the canvas and cannot carry selection | none |
| `card-dark` | `{colors.surface}` fill, `{colors.ink}` title, `{colors.ink-muted}` body, 1px `{colors.border-strong}` | border shifts to `{colors.border-control}` or surface steps to `{colors.surface-raised}` — extracted as "subtle border colour shift or elevation change" | ring lives on the card's own CTA, not on the card | no pressed state | none | image and content slots hold their aspect ratio and fade in; no skeleton shimmer is documented | none | none |
| `card-feature` | `{colors.canvas}` or full-bleed image, `{rounded.lg}`, optional 1px `{colors.border-subtle}` | no hover is extracted for this card | ring lives on the overlaid CTA | no pressed state | none | media slot fades in at `{motion.duration-base}` | none | none |
| `text-input` / `text-input-focused` | `{colors.canvas}` fill, `{colors.ink-muted}` text, 1px `{colors.border-subtle}`, `{rounded.xs}` | boundary to `{colors.border-control}` | `text-input-focused`: 2px `{colors.focus}` outline, background shifts to `{colors.input-focus-bg}` — the background shift is extracted, the ring colour is prescribed in place of the unmeasurable `var(--color-blue-500)` | same as focus-visible; a text field has no separate pressed state | `{colors.surface}` fill, `{colors.ink-tertiary}` text and boundary | field goes read-only with a trailing `{colors.ink-muted}` spinner | none | 1px `{colors.error}` boundary plus an `{colors.error}` message at `{typography.caption}` — never colour alone |
| `search-input` | `{colors.canvas}` fill, `{colors.ink-muted}` text, `{colors.ink-tertiary}` placeholder | boundary to `{colors.border-control}` | 2px `{colors.focus}` outline | same as focus-visible | `{colors.ink-tertiary}` text | trailing spinner while results resolve | none | none |
| `top-nav` | `{colors.canvas}` with backdrop blur, 1px `{colors.border-subtle}` bottom rule, `{colors.ink-muted}` links | links to `{colors.accent-blue}` — extracted | 2px `{colors.focus}` ring per link | no travel | none | none | current section: `{colors.ink}` against its `{colors.ink-muted}` siblings, never an underline alone | none |
| `footer` | `{colors.canvas}`, `{colors.ink-muted}` links, `{colors.ink}` section headers at `{typography.code-caption}` uppercase | links to `{colors.accent-blue}` — extracted | 2px `{colors.focus}` ring per link | no change | none | none | none | none |
| `badge-neutral-subtle` / `badge-neutral-filled` | white-on-black and black-on-white pills at `{typography.caption}`, `{rounded.pill}` | none — these are output, not controls | none | none | none | none | none | none |

`badge-neutral-subtle` and `badge-neutral-filled` genuinely have **one** state each: they
are labels, not controls. `card-feature` and `card-dark` have default plus hover only
unless the whole tile is a link, in which case it borrows `button-ghost`'s focus ring.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or stagger below was extracted from sanity.io. They are the shared **Crisp** profile values, assigned because Sanity's identity is a developer tool — a structured-content platform whose own prose calls the canvas a command centre, whose type is machined and whose depth is colorimetric. Crisp means a state change reads as already done, with no entrance choreography. Treat everything here as a specification to build to, not as a record of what Sanity ships.

### Tokens

`{motion.duration-instant}` 60ms · `{motion.duration-fast}` 100ms · `{motion.duration-base}` 150ms · `{motion.duration-slow}` 220ms · `{motion.duration-emphasis}` 300ms · `{motion.ease-standard}` · `{motion.ease-enter}` · `{motion.ease-exit}` · `{motion.stagger-step}` 20ms · `{motion.duration-reduced}` 100ms.

### Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, nav link, footer link) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`, plus the fill cross-fade to `{colors.accent-blue}` as a discrete colour change — no `transform` | Unchanged; already colour and opacity only, and under 150ms |
| Press / active | `{motion.duration-instant}` | `{motion.ease-exit}` | `transform: scale(0.99)` on pills only | Scale removed; the `{colors.accent-blue}` fill change remains, instant |
| Focus-visible ring | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` on the 2px `{colors.focus}` outline — the ring's geometry and offset never animate | Ring appears with no transition |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` 0 → 1 on the incoming view; no travel, and no cross-fade of the outgoing view | `opacity` fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px) → 0`; the scrim is the `{shadow.overlay}` backdrop blur over `{colors.canvas}`, fading `opacity` 0 → 1 | Travel removed; panel and scrim fade at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + the same `transform` reversed — shorter than its entrance | `opacity` fade at `{motion.duration-reduced}` |
| Dropdown / nav menu enter | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` + `transform: scale(0.98) → 1`, origin at the trigger edge | Scale removed; `opacity` only at `{motion.duration-reduced}` |
| Dropdown / nav menu exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` only | Unchanged |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px) → 0` | Travel removed; `opacity` at `{motion.duration-reduced}` |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: translateY(0 → 4px)` | `opacity` only at `{motion.duration-reduced}` |
| List enter (card grids, feature rows, search results) | `{motion.duration-fast}` per item, `{motion.stagger-step}` 20ms between items, 6 items maximum before the rest appear together | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px) → 0` | Stagger and travel removed; the whole list fades together at `{motion.duration-reduced}` |
| List exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity`; no stagger, no travel | Unchanged |
| Loading (button spinner, media slot) | spinner: 600ms per rotation, infinite — a loader, the one permitted infinite animation; media fade-in: `{motion.duration-base}` | spinner: linear; fade: `{motion.ease-enter}` | spinner `transform: rotate()`; slot `opacity` 0 → 1 | Spinner is replaced by a static `{typography.code-micro}` label or a three-dot glyph whose `opacity` pulses at `{motion.duration-reduced}`; the slot fade stays at `{motion.duration-reduced}` |

### Rules

- Animate `transform` and `opacity` only. Never `width`, `height`, `top`, `left` or `margin` — a near-black canvas shows reflow as a visible jolt, and the focus ring is an `outline` precisely so it costs no layout.
- Every exit is shorter than its matching entrance: modal 100ms out against 150ms in, dropdown 60ms out against 100ms in, toast 100ms out against 150ms in, list 60ms out against 100ms in.
- Nothing animates on first paint in a way that delays content. The 112px `{typography.display-hero}` line renders at its final position and opacity; the list stagger applies only to content entering after first paint.
- No infinite animation except the loading spinner above. This system has **no brand ambience**: no drifting gradient, no breathing glow on the neon green, no never-ending logo marquee.
- Travel stays between 4px and 8px. Crisp means the state change is the message, not the journey.
- Hover is the one place Sanity's own identity is loud: every interactive element shifts to `{colors.accent-blue}`. Keep that change instantaneous — a slow cross-fade to blue would read as a different brand.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: every translate and every scale, on all interactions above.
     Removed: the list stagger — lists appear as one block.
     Removed: the rotating spinner, replaced by a static or pulsing indicator.
     Frozen:  all ambience — this system defines none, and none may be added.
     Kept:    opacity fades only, clamped to 100ms ({motion.duration-reduced}).
     Kept:    every colour change, including the hover shift to #0052ef, instant.
     Kept:    the focus ring, which appears with no transition. */
  *, *::before, *::after {
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;
    transition-property: opacity, background-color, border-color, color !important;
  }
}
```

Nothing in this system is conveyed by motion alone: every animated state also changes a colour, a surface or a ring, so a reader with motion suppressed loses no information.

## Accessibility

Every ratio below was computed from this file's own hexes with the WCAG 2.1 relative-luminance formula. Nothing here was measured on a rendered page: overlap, clipping, frame rate, layout shift and real tap-target size are **not** verifiable from a document, so no claim is made about them.

### Key text pairs

| Foreground | Background | Ratio | Required | Verdict |
|---|---|---|---|---|
| `{colors.ink}` `#ffffff` | `{colors.canvas}` `#0b0b0b` | 19.68:1 | 4.5:1 | Pass |
| `{colors.ink}` `#ffffff` | `{colors.surface}` `#212121` | 16.10:1 | 4.5:1 | Pass |
| `{colors.ink}` `#ffffff` | `{colors.surface-raised}` `#353535` | 12.27:1 | 4.5:1 | Pass |
| `{colors.ink}` `#ffffff` | `{colors.input-focus-bg}` `#072227` | 16.57:1 | 4.5:1 | Pass |
| `{colors.ink-muted}` `#b9b9b9` | `{colors.canvas}` `#0b0b0b` | 10.03:1 | 4.5:1 | Pass |
| `{colors.ink-muted}` `#b9b9b9` | `{colors.surface}` `#212121` | 8.21:1 | 4.5:1 | Pass |
| `{colors.ink-muted}` `#b9b9b9` | `{colors.surface-raised}` `#353535` | 6.25:1 | 4.5:1 | Pass |
| `{colors.ink-muted}` `#b9b9b9` | `{colors.input-focus-bg}` `#072227` | 8.45:1 | 4.5:1 | Pass |
| `{colors.ink-tertiary}` `#797979` | `{colors.canvas}` `#0b0b0b` | 4.52:1 | 4.5:1 | Pass, by 0.02 |
| `{colors.ink-on-light-deep}` `#0b0b0b` | `{colors.surface-inverse}` `#ffffff` | 19.68:1 | 4.5:1 | Pass |
| `{colors.ink-on-light-deep}` `#0b0b0b` | `{colors.surface-inverse-soft}` `#ededed` | 16.81:1 | 4.5:1 | Pass |
| `{colors.ink-on-light}` `#212121` | `{colors.surface-inverse}` `#ffffff` | 16.10:1 | 4.5:1 | Pass |
| `{colors.ink-on-light}` `#212121` | `{colors.surface-inverse-soft}` `#ededed` | 13.75:1 | 4.5:1 | Pass |
| `{colors.ink}` `#ffffff` on the hover fill | `{colors.accent-blue}` `#0052ef` | 6.08:1 | 4.5:1 | Pass — `button-primary-hover` is more legible than the resting CTA |
| `{colors.primary}` `#f36458` as ink | `{colors.canvas}` `#0b0b0b` | 6.35:1 | 4.5:1 | Pass — the coral is safe as *text* on the canvas; it is as a *fill* that it fails |
| `{colors.accent-green}` `#19d600` as ink | `{colors.canvas}` `#0b0b0b` | 9.99:1 | 4.5:1 | Pass |
| `{colors.success-gpc}` `#37cd84` as ink | `{colors.canvas}` `#0b0b0b` | 9.59:1 | 4.5:1 | Pass |

### Where the real brand fails

These are extracted Sanity values. They are frozen — the hexes are facts about the brand and are not adjusted to make a ratio pass. Each failure is named with its measured ratio and the usage note that makes the value defensible. The nearest passing alternatives are listed under **Needs approval** in the audit report, not applied here.

| Foreground | Background | Measured | Required | Note |
|---|---|---|---|---|
| `{colors.on-primary}` `#ffffff` | `{colors.primary}` `#f36458` | 3.10:1 | 4.5:1 | **The primary CTA fails AA.** White on Sanity Red at `{typography.body}` 16px/400 is 1.4 short. It clears only the 3:1 large-text floor, so it is defensible at 24px+, or 18.66px+ at weight 700 — and this system forbids 700 weights. `{colors.ink-on-light-deep}` `#0b0b0b` on the same coral measures 6.35:1 and is the fix that changes no brand hex. |
| `button-primary` (`{colors.primary}` fill, `{colors.on-primary}` label) | — | 3.10:1 | 4.5:1 | The same failure as shipped in the component: the single most-clicked element in the system is the one that fails. Recorded rather than silently re-bound. |
| `{colors.accent-blue}` `#0052ef` as link or label ink | `{colors.canvas}` `#0b0b0b` | 3.24:1 | 4.5:1 | The universal hover colour is **not** usable as text on the dark canvas, and it is worse on a lift: 2.65:1 on `{colors.surface}`, 2.02:1 on `{colors.surface-raised}`. Use it as a *fill* behind `{colors.ink}` (6.08:1), which is what Sanity does, and never as hovered link ink on dark. |
| `{colors.error}` `#dd0000` as ink | `{colors.canvas}` `#0b0b0b` | 3.82:1 | 4.5:1 | Validation text in this red fails AA on the canvas, and 3.12:1 on `{colors.surface}`. Defensible as a 1px boundary or an icon fill, where 3:1 applies on the canvas only; pair every error state with a `{colors.ink}` message rather than relying on the red. |
| `{colors.ink-tertiary}` `#797979` | `{colors.surface}` `#212121` | 3.70:1 | 4.5:1 | Metadata and timestamps in Medium Gray pass on the canvas (4.52:1) and fail on every card. Restrict to 24px+ on `{colors.surface}`, or step up to `{colors.ink-muted}` inside cards. Worse again on `{colors.surface-raised}`: 2.82:1, below even the large-text floor. |
| `{colors.border-dark}` `#0b0b0b` | `{colors.canvas}` `#0b0b0b` | 1.00:1 | 3.0:1 | The file's own description — "barely visible, maintaining minimal containment" — is literally true: on the canvas this border is invisible. Decorative only. |
| `{colors.border-dark}` `#0b0b0b` | `{colors.surface}` `#212121` | 1.22:1 | 3.0:1 | Same token, drawn on a card. Decorative only. |
| `{colors.border-subtle}` `#212121` | `{colors.canvas}` `#0b0b0b` | 1.22:1 | 3.0:1 | **This is the extracted boundary of `text-input`, `search-input`, `button-ghost` and the nav rule** — the only thing defining those controls, at a quarter of the required contrast. Scoped to decoration; use `{colors.border-control}` `#797979` (4.52:1) for any control edge. |
| `{colors.border-subtle}` `#212121` | `{colors.surface}` `#212121` | 1.00:1 | 3.0:1 | Same token on a card of the same value — the `card-dark` fallback border is invisible against its own fill. |
| `{colors.border-strong}` `#353535` | `{colors.canvas}` `#0b0b0b` | 1.60:1 | 3.0:1 | The strongest border Sanity ships, still half the threshold. Decorative: card edges, dividers, table rules. |
| `{colors.border-strong}` `#353535` | `{colors.surface}` `#212121` | 1.31:1 | 3.0:1 | Same, as used on `card-dark`. The card is legible because of its fill step, not its border. |
| `{colors.ink}` `#ffffff` | `{colors.accent-green}` `#19d600` | 1.97:1 | 4.5:1 | Not a defect in the file, but a trap: the neon green is a wide-gamut *fill*. Any label on it must be `{colors.ink-on-light-deep}` `#0b0b0b` (9.99:1), never white. |
| `{colors.ink}` `#ffffff` | `{colors.accent-blue-light}` `#55beff` | 2.06:1 | 4.5:1 | Same trap for the light blue badge fill: use `{colors.ink-on-light-deep}` (9.56:1). `{colors.accent-blue-pale}` `#afe3ff` is lighter still and takes the same dark ink (14.30:1). |

The surface ladder itself is the other honest weakness: `{colors.canvas}` → `{colors.surface}` is 1.22:1, `{colors.surface}` → `{colors.surface-raised}` is 1.31:1, `{colors.canvas}` → `{colors.surface-raised}` is 1.60:1. A level change is a legitimate depth cue but is **never** a sufficient signal of selection or state on its own — pair it with ink tone, a `{colors.border-control}` edge or a `{colors.primary}` marker.

### Focus ring visibility, surface by surface

`{colors.focus}` `#55beff`, a 2px outline with a 2px offset, measured against every ground it can be drawn on:

| Surface | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.canvas}` `#0b0b0b` | 9.56:1 | 3.0:1 | Pass |
| `{colors.canvas-void}` `#000000` | 10.20:1 | 3.0:1 | Pass |
| `{colors.surface}` `#212121` | 7.82:1 | 3.0:1 | Pass |
| `{colors.surface-raised}` `#353535` | 5.96:1 | 3.0:1 | Pass |
| `{colors.input-focus-bg}` `#072227` | 8.05:1 | 3.0:1 | Pass |
| `{colors.surface-inverse}` `#ffffff` | 2.06:1 | 3.0:1 | **Fail — never draw `{colors.focus}` on the inverted band** |
| `{colors.surface-inverse-soft}` `#ededed` | 1.76:1 | 3.0:1 | **Fail — use `{colors.focus-on-light}` instead** |

`{colors.focus-on-light}` `#0052ef` covers the inverted bands: 6.08:1 on `{colors.surface-inverse}` `#ffffff` and 5.19:1 on `{colors.surface-inverse-soft}` `#ededed`. It is the ring Sanity actually ships, and on dark grounds it measures 3.24:1 on the canvas but 2.65:1 on `{colors.surface}` and 2.02:1 on `{colors.surface-raised}` — which is why `{colors.focus}` exists for dark. Two rings are required because this file documents both a near-black canvas and pure-white inverted sections; no single value clears 3:1 on both.

Because both rings are drawn **outside** the control with a 2px offset, each is judged against the surface behind the control, as WCAG 2.2 Focus Appearance asks — not against the control's fill. That matters for `button-primary`: `{colors.focus}` against the coral fill is only 1.50:1, so the ring must never be drawn inside the pill's edge.

Resting control boundaries use `{colors.border-control}` `#797979`: 4.52:1 on `{colors.canvas}` and 3.70:1 on `{colors.surface}`, both above 3:1. On `{colors.surface-raised}` it falls to 2.82:1, so a control sitting on the raised surface takes `{colors.ink-muted}` `#b9b9b9` (6.25:1) as its edge instead.

### Minimum tap target

Specified in this file, not measured — a document cannot verify a rendered hit box.

- **Responsive Behavior** states a 44px minimum for all interactive elements on touch, which meets WCAG 2.5.5 AAA and clears the 2.5.8 AA floor of 24px.
- `button-primary` at `{typography.body}` 16px/1.50 plus 8px vertical padding computes to roughly 40px of visual height, so it needs an invisible expansion to reach the file's own 44px target on touch.
- `button-ghost` and `search-input` are documented with `0px` vertical padding and depend entirely on their line box; both must be expanded to 44px on touch.
- `badge-neutral-subtle` and `badge-neutral-filled` are labels, not controls, and are exempt.

### Reduced motion

Honoured in full — see the `@media (prefers-reduced-motion: reduce)` block in **Motion & Animation**. All travel and scale are removed, the list stagger is removed, the spinner stops rotating, and opacity fades are clamped to `{motion.duration-reduced}` 100ms. This system defines no ambient animation to freeze. No information is carried by motion alone.

### Other notes

- Contrast is the only automatically verifiable dimension here. Keyboard order, heading structure, landmark regions, alt text and screen-reader labelling cannot be checked from a token document and are untested.
- `{colors.accent-green-p3}`, `{colors.accent-magenta-p3}` and `{colors.border-accent-orange-p3}` are wide-gamut `display-p3` values. Only the green states an sRGB fallback (`{colors.accent-green}`); the other two cannot be measured and are listed in **Known Gaps**.
- The hover convention — every interactive element shifting to `{colors.accent-blue}` — is a colour-only state change. It is acceptable here because hover is never the sole carrier of meaning, but selection and error states in this file deliberately add ink, border or text so that they do not depend on colour alone.

## Do's and Don'ts


### Do
- Use the achromatic gray scale as the foundation -- maintain pure neutral discipline with no warm/cool tinting
- Apply Electric Blue (`#0052ef`) consistently as the universal hover/active state across all interactive elements
- Use extreme negative letter-spacing (-2px to -4.48px) on display headings 48px and above
- Keep primary CTAs as full-pill shapes (99999px radius) with the coral-red (`#f36458`)
- Use IBM Plex Mono uppercase for technical labels, tags, and system metadata
- Communicate depth through surface color (dark-to-light) rather than shadows
- Maintain generous vertical section spacing (64-120px) on the dark canvas
- Use `"cv01", "cv11", "cv12", "cv13", "ss07"` OpenType features for display typography

- Draw focus with `{colors.focus}` on dark grounds and `{colors.focus-on-light}` on the inverted light bands, always as a 2px outline with a 2px offset outside the control
- Give any control whose edge is its only boundary a `{colors.border-control}` border — the extracted borders are decoration
- Keep every state change between `{motion.duration-instant}` and `{motion.duration-base}`; Crisp means the change reads as already done
- Put `{colors.ink-on-light-deep}` on the neon green, the light blue and the pale blue fills — never white

### Don't
- Don't introduce warm or cool color tints to the neutral scale -- Sanity's grays are pure achromatic
- Don't use drop shadows for elevation -- dark interfaces demand colorimetric depth
- Don't apply border-radius between 13px and 99998px -- the system jumps from 12px (large card) directly to pill (99999px)
- Don't mix the coral-red CTA with the electric blue interactive color in the same element
- Don't use heavy font weights (700+) -- the system maxes out at 600 and only for 11px uppercase labels
- Don't place light text on light surfaces or dark text on dark surfaces without checking the gray-on-gray contrast ratio
- Don't use traditional offset box-shadows -- ring shadows (0 0 0 Npx) or border-based containment only
- Don't break the tight line-height on headings -- 1.00-1.24 is the range, never go to 1.5+ for display text
- Don't use `{colors.border-dark}`, `{colors.border-subtle}` or `{colors.border-strong}` as the only boundary of an input, checkbox or segmented control — all three measure below 1.6:1
- Don't use `{colors.accent-blue}` as text on any dark surface; it is a fill colour (3.24:1 on the canvas, 2.02:1 on `{colors.surface-raised}`)
- Don't rely on a single surface step to signal selection — adjacent levels sit between 1.22:1 and 1.60:1
- Don't add entrance choreography, parallax, scroll-driven reveals or ambient looping motion; this system has no ambience
- Don't animate `width`, `height`, `top`, `left` or `margin` — `transform` and `opacity` only

## Responsive Behavior


### Breakpoints

| Name | Width | Behavior |
|------|-------|----------|
| Desktop XL | >= 1640px | Full layout, maximum content width |
| Desktop | >= 1440px | Standard desktop layout |
| Desktop Compact | >= 1200px | Slightly condensed desktop |
| Laptop | >= 1100px | Reduced column widths |
| Tablet Landscape | >= 960px | 2-column layouts begin collapsing |
| Tablet | >= 768px | Transition zone, some elements stack |
| Mobile Large | >= 720px | Near-tablet layout |
| Mobile | >= 480px | Single-column, stacked layout |
| Mobile Small | >= 376px | Minimum supported width |

### Collapsing Strategy
- **Navigation**: Horizontal links collapse to hamburger menu below 768px
- **Hero typography**: Scales from 112px -> 72px -> 48px -> 38px across breakpoints, maintaining tight letter-spacing ratios
- **Grid layouts**: 3-column -> 2-column at ~960px, single-column below 768px
- **Card grids**: Horizontal scrolling on mobile instead of wrapping (preserving card aspect ratios)
- **Section spacing**: Vertical padding reduces by ~40% on mobile (120px -> 64px -> 48px)
- **Button sizing**: CTA pills maintain padding but reduce font size; ghost buttons stay fixed
- **Code blocks**: Horizontal scroll with preserved monospace formatting

### Mobile-Specific Adjustments
- Full-bleed sections extend edge-to-edge with 16px internal gutters
- Touch targets: minimum 44px for all interactive elements
- Heading letter-spacing relaxes slightly at mobile sizes (less aggressive negative tracking)
- Image containers switch from fixed aspect ratios to full-width with auto height

## Known Gaps

This file was converted from the early numbered format and carried no frontmatter token
block. Every token in the block above was built from a hex, type value, spacing step,
radius or component description already written in this document's own prose. Nothing was
invented to fill a column, so the gaps below are real gaps rather than omissions.

- **The whole Motion & Animation section is prescribed, not extracted.** No duration, easing curve or stagger was measured from sanity.io; the values are the shared **Crisp** profile and any of them may differ from what Sanity ships.
- `{colors.focus}` and `{colors.border-control}` are **prescribed**, not extracted. Both reuse hexes the palette already owns (`#55beff` Light Blue and `#797979` Medium Gray); no new brand colour was introduced. Sanity's own ring, `{colors.focus-on-light}` `#0052ef`, is kept as the extracted fact and is still used on the inverted light bands.
- `{colors.accent-magenta-p3}` and `{colors.border-accent-orange-p3}` are stated only as `display-p3` values. The source file gives no sRGB fallback for either, so neither can be measured for contrast and neither has a hex token.
- `{shadow.ring-focus-extracted}` is recorded as `0 0 0 2px var(--color-blue-500)`. The hex behind `--color-blue-500` is **not stated** anywhere in this file — the file names `--color-blue-700` as `#0052ef` instead — so the extracted focus shadow cannot be measured. `{shadow.ring-focus}` is the prescribed replacement.
- `{shadow.overlay}` is described only as "backdrop blur + semi-transparent dark". Neither the blur radius nor the alpha is stated, so the overlay cannot be specified exactly or measured.
- The `card-dark` hover is extracted as "subtle border colour shift or elevation change" — which of the two, and to which value, is not stated. The state table names a boundary step to `{colors.border-control}` or a fill step to `{colors.surface-raised}` as the prescribed reading.
- Max content width is given as "~1440px (inferred from breakpoints)" in the source and remains an inference, not an extracted value.
- `{spacing.space-12}` is written as "96-120px" in the source; the token carries 96px and the 96-120px range is kept in the Layout table. `{rounded.sm}` is written as "4-5px"; the token carries 5px, the value the ghost button actually uses.
- `{typography.caption}` is stated as weight 400-500 with line height 1.30-1.50, `{typography.micro-label}` as weight 500-600 with line height 1.00-1.50, and `{typography.code-micro}` as 10-12px. Each token carries one endpoint — the one the components use — and the full range stays in the Typography table.
- Focus-visible, disabled, loading, selected and error styling is **prescribed** throughout **Components**. The source pages document only resting and hover styling; no disabled, loading or validation state was observed, and in particular no form-error styling exists beyond the `{colors.error}` hex itself.
- waldenburgNormal is proprietary. Inter or Space Grotesk is the documented substitute, and letter-spacing values will need re-tuning against a substitute's own metrics.
- Light-mode is not a theme here. `{colors.surface-inverse}` and `{colors.surface-inverse-soft}` are inverted *sections* inside a dark system, not a second colour scheme, so there is no full light palette to audit.
- Tap-target size, overlap, clipping, frame rate and layout shift cannot be verified from a document. Nothing in **Accessibility** claims them as measured.

## Agent Prompt Guide


### Quick Color Reference
```
Background:      #0b0b0b (near-black canvas)
Surface:         #212121 (elevated cards/containers)
Border:          #353535 (visible) / #212121 (subtle)
Text Primary:    #ffffff (white on dark)
Text Secondary:  #b9b9b9 (silver on dark)
Text Tertiary:   #797979 (medium gray)
CTA:             #f36458 (coral-red)
Interactive:     #0052ef (electric blue, all hovers)
Success:         #19d600 (green, sRGB fallback)
Error:           #dd0000 (pure red)
Light Surface:   #ededed / #ffffff (inverted sections)
```

### Example Prompts

**Landing page section:**
"Create a feature section with a near-black (#0b0b0b) background. Use a 48px heading in Inter with -1.68px letter-spacing, white text. Below it, 16px body text in #b9b9b9 with 1.50 line-height. Include a coral-red (#f36458) pill button with white text and a secondary dark (#0b0b0b) pill button with #b9b9b9 text. Both buttons hover to #0052ef blue."

**Card grid:**
"Build a 3-column card grid on a #0b0b0b background. Each card has a #212121 surface, 1px solid #353535 border, 6px border-radius, and 24px padding. Card titles are 24px white with -0.24px letter-spacing. Body text is 13px #b9b9b9. Add a 13px IBM Plex Mono uppercase tag in #797979 at the top of each card."

**Form section:**
"Design a contact form on a #0b0b0b background. Inputs have #0b0b0b background, 1px solid #212121 border, 3px border-radius, 8px 12px padding, and #b9b9b9 placeholder text. Focus state shows a 2px blue (#0052ef) ring. Submit button is a full-width coral-red (#f36458) pill. Include a 13px #797979 helper text below each field."

**Navigation bar:**
"Create a sticky top navigation on #0b0b0b with backdrop blur. Left: brand text in 15px white. Center/right: nav links in 16px #b9b9b9 that hover to blue. Far right: a coral-red (#f36458) pill CTA button. Bottom border: 1px solid #212121."

### Iteration Guide
1. **Start dark**: Begin with `#0b0b0b` background, `#ffffff` primary text, `#b9b9b9` secondary text
2. **Add structure**: Use `#212121` surfaces and `#353535` borders for containment -- no shadows
3. **Apply typography**: Inter (or Space Grotesk) with tight letter-spacing on headings, 1.50 line-height on body
4. **Color punctuation**: Add `#f36458` for CTAs and `#0052ef` for all hover/interactive states
5. **Refine spacing**: 8px base unit, 24-32px within sections, 64-120px between sections
6. **Technical details**: Add IBM Plex Mono uppercase labels for tags and metadata
7. **Polish**: Ensure all interactive elements hover to `#0052ef`, all buttons are pills or subtle 5px radius, borders are hairline (1px)
