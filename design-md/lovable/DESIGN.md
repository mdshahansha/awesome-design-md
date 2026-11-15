---
version: alpha
name: Lovable-design-analysis
description: Warmth through restraint. A parchment-cream canvas (#f7f4ed) replaces the cold white of most developer-tool sites, near-black charcoal ink (#1c1c1c) carries all type, and every grey in the system is that same charcoal at a stated opacity rather than a separate hex. The custom Camera Plain Variable typeface runs tight and editorial at display sizes (-0.9px to -1.5px tracking, weight 600) and relaxes to weight 400 everywhere else. Depth is deliberately shallow: warm #eceae4 hairlines contain cards instead of drop shadows, and the one signature shadow is a multi-layer inset on dark buttons that reads as pressed-into-paper rather than floating above it. There is no saturated accent colour by design.

colors:
  canvas: "#f7f4ed"
  surface-cream: "#f7f4ed"
  primary: "#1c1c1c"
  on-primary: "#fcfbf8"
  ink: "#1c1c1c"
  muted: "#5f5f5d"
  hairline: "#eceae4"
  hairline-strong: "#8a8884"
  focus: "#3b82f6"
  ink-83: "rgba(28,28,28,0.83)"
  ink-82: "rgba(28,28,28,0.82)"
  ink-40: "rgba(28,28,28,0.4)"
  ink-04: "rgba(28,28,28,0.04)"
  ink-03: "rgba(28,28,28,0.03)"
  ring-brand: "rgba(59,130,246,0.5)"

typography:
  display-hero:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 60px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.5px
  display-alt:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 60px
    fontWeight: 480
    lineHeight: 1.00
    letterSpacing: normal
  section-heading:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: -1.2px
  sub-heading:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -0.9px
  card-title:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: normal
  body-large:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: normal
  body:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: normal
  button:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: normal
  button-small:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: normal
  link:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: normal
  link-small:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: normal
  caption:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: normal

rounded:
  micro: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px

spacing:
  xs: 8px
  sm: 10px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  xxxl: 40px
  section-xs: 56px
  section-sm: 80px
  section-md: 96px
  section-lg: 128px
  section-xl: 176px
  section-xxl: 192px
  section-xxxl: 208px

shadow:
  none: none
  button-inset: "rgba(255,255,255,0.2) 0px 0.5px 0px 0px inset, rgba(0,0,0,0.2) 0px 0px 0px 0.5px inset, rgba(0,0,0,0.05) 0px 1px 2px 0px"
  focus-soft: "rgba(0,0,0,0.1) 0px 4px 12px"

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
  button-primary-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    shadow: "{shadow.button-inset}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    border: 1px solid {colors.ink-40}
  button-cream:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-pill-icon:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    shadow: "{shadow.button-inset}"
  card:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.lg}"
    border: 1px solid {colors.hairline}
    shadow: "{shadow.none}"
  card-featured:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    border: 1px solid {colors.hairline}
  card-compact:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.hairline}
  image-card:
    backgroundColor: "{colors.surface-cream}"
    rounded: "{rounded.lg}"
    border: 1px solid {colors.hairline}
  text-input:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    placeholderColor: "{colors.muted}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.link}"
  nav-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    shadow: "{shadow.button-inset}"
  menu-toggle:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    textDecoration: underline
  ai-chat-input:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body-large}"
    rounded: "{rounded.lg}"
    border: 1px solid {colors.hairline}
  suggestion-pill:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.button-small}"
    rounded: "{rounded.pill}"
    border: 1px solid {colors.hairline}
  template-card:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.lg}"
    border: 1px solid {colors.hairline}
  stats-metric:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.section-heading}"
  stats-label:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.link-small}"
    rounded: "{rounded.xl}"
    border: 1px solid {colors.hairline}
---

# Design System Inspired by Lovable

## Overview

Lovable's website radiates warmth through restraint. The entire page sits on a creamy, parchment-toned background (`#f7f4ed`) that immediately separates it from the cold-white conventions of most developer tool sites. This isn't minimalism for minimalism's sake — it's a deliberate choice to feel approachable, almost analog, like a well-crafted notebook. The near-black text (`#1c1c1c`) against this warm cream creates a contrast ratio that's easy on the eyes while maintaining sharp readability.

The custom Camera Plain Variable typeface is the system's secret weapon. Unlike geometric sans-serifs that signal "tech company," Camera Plain has a humanist warmth — slightly rounded terminals, organic curves, and a comfortable reading rhythm. At display sizes (48px–60px), weight 600 with aggressive negative letter-spacing (-0.9px to -1.5px) compresses headlines into confident, editorial statements. The font uses `ui-sans-serif, system-ui` as fallbacks, acknowledging that the custom typeface carries the brand personality.

What makes Lovable's visual system distinctive is its opacity-driven depth model. Rather than using a traditional gray scale, the system modulates `#1c1c1c` at varying opacities (0.03, 0.04, 0.4, 0.82–0.83) to create a unified tonal range. Every shade of gray on the page is technically the same hue — just more or less transparent. This creates a visual coherence that's nearly impossible to achieve with arbitrary hex values. The border system follows suit: `1px solid #eceae4` for light divisions and `1px solid rgba(28, 28, 28, 0.4)` for stronger interactive boundaries.

**Key Characteristics:**
- Warm parchment background (`#f7f4ed`) — not white, not beige, a deliberate cream that feels hand-selected
- Camera Plain Variable typeface with humanist warmth and editorial letter-spacing at display sizes
- Opacity-driven color system: all grays derived from `#1c1c1c` at varying transparency levels
- Inset shadow technique on buttons: `rgba(255,255,255,0.2) 0px 0.5px 0px 0px inset, rgba(0,0,0,0.2) 0px 0px 0px 0.5px inset`
- Warm neutral border palette: `#eceae4` for subtle, `rgba(28,28,28,0.4)` for interactive elements
- Full-pill radius (`9999px`) used extensively for action buttons and icon containers
- Focus state uses `rgba(0,0,0,0.1) 0px 4px 12px` shadow for soft, warm emphasis
- shadcn/ui + Radix UI component primitives with Tailwind CSS utility styling

## Colors

### Primary
- **Cream** (`#f7f4ed`): Page background, card surfaces, button surfaces. The foundation — warm, paper-like, human.
- **Charcoal** (`#1c1c1c`): Primary text, headings, dark button backgrounds. Not pure black — organic warmth.
- **Off-White** (`#fcfbf8`): Button text on dark backgrounds, subtle highlight. Barely distinguishable from pure white.

### Neutral Scale (Opacity-Based)
- **Charcoal 100%** (`#1c1c1c`): Primary text, headings, dark surfaces.
- **Charcoal 83%** (`rgba(28,28,28,0.83)`): Strong secondary text.
- **Charcoal 82%** (`rgba(28,28,28,0.82)`): Body copy.
- **Muted Gray** (`#5f5f5d`): Secondary text, descriptions, captions.
- **Charcoal 40%** (`rgba(28,28,28,0.4)`): Interactive borders, button outlines.
- **Charcoal 4%** (`rgba(28,28,28,0.04)`): Subtle hover backgrounds, micro-tints.
- **Charcoal 3%** (`rgba(28,28,28,0.03)`): Barely-visible overlays, background depth.

### Surface & Border
- **Light Cream** (`#eceae4`): Card borders, dividers, image outlines. The warm divider line.
- **Cream Surface** (`#f7f4ed`): Card backgrounds, section fills — same as page background for seamless integration.

### Interactive
- **Ring Blue** (`#3b82f6` at 50% opacity): `--tw-ring-color`, Tailwind focus ring.
- **Focus Shadow** (`rgba(0,0,0,0.1) 0px 4px 12px`): Focus and active state shadow — soft, warm, diffused.

### Inset Shadows
- **Button Inset** (`rgba(255,255,255,0.2) 0px 0.5px 0px 0px inset, rgba(0,0,0,0.2) 0px 0px 0px 0.5px inset, rgba(0,0,0,0.05) 0px 1px 2px 0px`): The signature multi-layer inset shadow on dark buttons.

### Token Map

The frontmatter names what the prose above describes. Nothing here is a new colour; every hex is one already written in this file.

| Token | Value | Role |
|---|---|---|
| `{colors.canvas}` | `#f7f4ed` | Page floor — the cream |
| `{colors.surface-cream}` | `#f7f4ed` | Card, panel and button surface — deliberately identical to the canvas |
| `{colors.ink}` | `#1c1c1c` | Primary text and headings |
| `{colors.primary}` | `#1c1c1c` | The brand's signal: the dark CTA. Lovable's "accent" is its ink |
| `{colors.on-primary}` | `#fcfbf8` | Off-white button text on the dark CTA |
| `{colors.muted}` | `#5f5f5d` | Secondary text, descriptions, captions, placeholders |
| `{colors.hairline}` | `#eceae4` | Passive containment — card borders, dividers, image outlines |
| `{colors.ink-40}` | `rgba(28,28,28,0.4)` | Interactive boundaries, ghost-button outlines |
| `{colors.ink-83}` / `{colors.ink-82}` | `rgba(28,28,28,0.83)` / `rgba(28,28,28,0.82)` | Strong secondary text, body copy |
| `{colors.ink-04}` / `{colors.ink-03}` | `rgba(28,28,28,0.04)` / `rgba(28,28,28,0.03)` | Hover tints, micro-overlays, skeletons |
| `{colors.ring-brand}` | `rgba(59,130,246,0.5)` | The Tailwind ring the brand actually ships |
| `{colors.focus}` | `#3b82f6` | **Prescribed.** The same blue at full opacity, so the ring is measurable |
| `{colors.hairline-strong}` | `#8a8884` | **Prescribed.** `#1c1c1c` at 50% over cream — the accessible boundary |

The last two are the only values in this group that Lovable does not ship as written. Both are labelled prescribed wherever they appear, and the Accessibility section states exactly why each exists and what the real brand value measures.

**On the absence of an accent.** Lovable has no accent colour and the Don'ts forbid adding one. The `accent` role in the token contract is therefore filled by `{colors.primary}` — the charcoal CTA — because that is genuinely where the brand puts its signal. A chromatic accent invented for this slot would be the single fastest way to make this file stop reading as Lovable.

## Typography

### Font Family
- **Primary**: `Camera Plain Variable`, with fallbacks: `ui-sans-serif, system-ui`
- **Weight range**: 400 (body/reading), 480 (special display), 600 (headings/emphasis)
- **Feature**: Variable font with continuous weight axis — allows fine-tuned intermediary weights like 480.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Camera Plain Variable | 60px (3.75rem) | 600 | 1.00–1.10 (tight) | -1.5px | Maximum impact, editorial |
| Display Alt | Camera Plain Variable | 60px (3.75rem) | 480 | 1.00 (tight) | normal | Lighter hero variant |
| Section Heading | Camera Plain Variable | 48px (3.00rem) | 600 | 1.00 (tight) | -1.2px | Feature section titles |
| Sub-heading | Camera Plain Variable | 36px (2.25rem) | 600 | 1.10 (tight) | -0.9px | Sub-sections |
| Card Title | Camera Plain Variable | 20px (1.25rem) | 400 | 1.25 (tight) | normal | Card headings |
| Body Large | Camera Plain Variable | 18px (1.13rem) | 400 | 1.38 | normal | Introductions |
| Body | Camera Plain Variable | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text |
| Button | Camera Plain Variable | 16px (1.00rem) | 400 | 1.50 | normal | Button labels |
| Button Small | Camera Plain Variable | 14px (0.88rem) | 400 | 1.50 | normal | Compact buttons |
| Link | Camera Plain Variable | 16px (1.00rem) | 400 | 1.50 | normal | Underline decoration |
| Link Small | Camera Plain Variable | 14px (0.88rem) | 400 | 1.50 | normal | Footer links |
| Caption | Camera Plain Variable | 14px (0.88rem) | 400 | 1.50 | normal | Metadata, small text |

### Principles
- **Warm humanist voice**: Camera Plain Variable gives Lovable its approachable personality. The slightly rounded terminals and organic curves contrast with the sharp geometric sans-serifs used by most developer tools.
- **Variable weight as design tool**: The font supports continuous weight values (e.g., 480), enabling nuanced hierarchy beyond standard weight stops. Weight 480 at 60px creates a display style that feels lighter than semibold but stronger than regular.
- **Compression at scale**: Headlines use negative letter-spacing (-0.9px to -1.5px) for editorial impact. Body text stays at normal tracking for comfortable reading.
- **Two weights, clear roles**: 400 (body/UI/links/buttons) and 600 (headings/emphasis). The narrow weight range creates hierarchy through size and spacing, not weight variation.

## Layout

### Spacing System
- Base unit: 8px
- Scale: 8px, 10px, 12px, 16px, 24px, 32px, 40px, 56px, 80px, 96px, 128px, 176px, 192px, 208px
- The scale expands generously at the top end — sections use 80px–208px vertical spacing for editorial breathing room

### Grid & Container
- Max content width: approximately 1200px (centered)
- Hero: centered single-column with massive vertical padding (96px+)
- Feature sections: 2–3 column grids
- Full-width footer with multi-column link layout
- Showcase sections with centered card grids

### Whitespace Philosophy
- **Editorial generosity**: Lovable's spacing is lavish at section boundaries (80px–208px). The warm cream background makes these expanses feel cozy rather than empty.
- **Content-driven rhythm**: Tight internal spacing within cards (12–24px) contrasts with wide section gaps, creating a reading rhythm that alternates between focused content and visual rest.
- **Section separation**: Footer uses `1px solid #eceae4` border and 16px radius container. Sections defined by generous spacing rather than border lines.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, cream background | Page surface, most content |
| Bordered (Level 1) | `1px solid #eceae4` | Cards, images, dividers |
| Inset (Level 2) | `rgba(255,255,255,0.2) 0px 0.5px 0px inset, rgba(0,0,0,0.2) 0px 0px 0px 0.5px inset, rgba(0,0,0,0.05) 0px 1px 2px` | Dark buttons, primary actions |
| Focus (Level 3) | `rgba(0,0,0,0.1) 0px 4px 12px` | Active/focus states |
| Ring (Accessibility) | `rgba(59,130,246,0.5)` 2px ring | Keyboard focus on inputs |

**Shadow Philosophy**: Lovable's depth system is intentionally shallow. Instead of floating cards with dramatic drop-shadows, the system relies on warm borders (`#eceae4`) against the cream surface to create gentle containment. The only notable shadow pattern is the inset shadow on dark buttons — a subtle multi-layer technique where a white highlight line sits at the top edge while a dark ring and soft drop handle the bottom. This creates a tactile, pressed-into-surface feeling rather than a hovering-above-surface feeling. The warm focus shadow (`rgba(0,0,0,0.1) 0px 4px 12px`) is deliberately diffused and large, creating a soft glow rather than a sharp outline.

### Decorative Depth
- Hero: soft, warm multi-color gradient wash (pinks, oranges, blues) behind hero — atmospheric, barely visible
- Footer: gradient background with warm tones transitioning to the bottom
- No harsh section dividers — spacing and background warmth handle transitions

## Shapes

### Border Radius Scale
- Micro (`{rounded.micro}`, 4px): Small buttons, interactive elements
- Standard (`{rounded.sm}`, 6px): Buttons, inputs, navigation menu
- Comfortable (`{rounded.md}`, 8px): Compact cards, divs
- Card (`{rounded.lg}`, 12px): Standard cards, image containers, templates
- Container (`{rounded.xl}`, 16px): Large containers, footer sections
- Full Pill (`{rounded.pill}`, 9999px): Action pills, icon buttons, toggles

The ladder is internally consistent: 4 → 6 → 8 → 12 → 16, then a single jump to the full pill. No value in the file sits outside it, and the pill is never applied to a rectangular button (see Don'ts).

### Borders
One width only: 1px. Two tones, with fixed jobs — `{colors.hairline}` (#eceae4) for passive containment and `{colors.ink-40}` (rgba(28,28,28,0.4)) for interactive boundaries. A third, `{colors.hairline-strong}`, is **prescribed, not extracted**, and exists only because neither real tone reaches WCAG 1.4.11; see Accessibility.

### Focus Ring
2px solid `{colors.focus}` (#3b82f6) with a 2px offset in the surface's own colour, paired with `{shadow.focus-soft}`. The brand itself ships `{colors.ring-brand}` — the same blue at 50% opacity — which measures 1.78:1 on cream and is unusable as the sole indicator. The ring token above is that blue at full opacity, which clears 3:1 on every surface this file defines. The accompanying soft shadow is the brand's real signature; the ring is the part that makes it legible.

## Components

### Buttons

**Primary Dark (Inset Shadow)**
- Background: `#1c1c1c`
- Text: `#fcfbf8`
- Padding: 8px 16px
- Radius: 6px
- Shadow: `rgba(0,0,0,0) 0px 0px 0px 0px, rgba(0,0,0,0) 0px 0px 0px 0px, rgba(255,255,255,0.2) 0px 0.5px 0px 0px inset, rgba(0,0,0,0.2) 0px 0px 0px 0.5px inset, rgba(0,0,0,0.05) 0px 1px 2px 0px`
- Active: opacity 0.8
- Focus: `rgba(0,0,0,0.1) 0px 4px 12px` shadow
- Use: Primary CTA ("Start Building", "Get Started")

**Ghost / Outline**
- Background: transparent
- Text: `#1c1c1c`
- Padding: 8px 16px
- Radius: 6px
- Border: `1px solid rgba(28,28,28,0.4)`
- Active: opacity 0.8
- Focus: `rgba(0,0,0,0.1) 0px 4px 12px` shadow
- Use: Secondary actions ("Log In", "Documentation")

**Cream Surface**
- Background: `#f7f4ed`
- Text: `#1c1c1c`
- Padding: 8px 16px
- Radius: 6px
- No border
- Active: opacity 0.8
- Use: Tertiary actions, toolbar buttons

**Pill / Icon Button**
- Background: `#f7f4ed`
- Text: `#1c1c1c`
- Radius: 9999px (full pill)
- Shadow: same inset pattern as primary dark
- Opacity: 0.5 (default), 0.8 (active)
- Use: Additional actions, plan mode toggle, voice recording

### Cards & Containers
- Background: `#f7f4ed` (matches page)
- Border: `1px solid #eceae4`
- Radius: 12px (standard), 16px (featured), 8px (compact)
- No box-shadow by default — borders define boundaries
- Image cards: `1px solid #eceae4` with 12px radius

### Inputs & Forms
- Background: `#f7f4ed`
- Text: `#1c1c1c`
- Border: `1px solid #eceae4`
- Radius: 6px
- Focus: ring blue (`rgba(59,130,246,0.5)`) outline
- Placeholder: `#5f5f5d`

### Navigation
- Clean horizontal nav on cream background, fixed
- Logo/wordmark left-aligned (128.75 x 22px)
- Links: Camera Plain 14–16px weight 400, `#1c1c1c` text
- CTA: dark button with inset shadow, 6px radius
- Mobile: hamburger menu with 6px radius button
- Subtle border or no border on scroll

### Links
- Color: `#1c1c1c`
- Decoration: underline (default)
- Hover: primary accent (via CSS variable `hsl(var(--primary))`)
- No color change on hover — decoration carries the interactive signal

### Image Treatment
- Showcase/portfolio images with `1px solid #eceae4` border
- Consistent 12px border radius on all image containers
- Soft gradient backgrounds behind hero content (warm multi-color wash)
- Gallery-style presentation for template/project showcases

### Distinctive Components

**AI Chat Input**
- Large prompt input area with soft borders
- Suggestion pills with `#eceae4` borders
- Voice recording / plan mode toggle buttons as pill shapes (9999px)
- Warm, inviting input area — not clinical

**Template Gallery**
- Card grid showing project templates
- Each card: image + title, `1px solid #eceae4` border, 12px radius
- Hover: subtle shadow or border darkening
- Category labels as text links

**Stats Bar**
- Large metrics: "0M+" pattern in 48px+ weight 600
- Descriptive text below in muted gray
- Horizontal layout with generous spacing

### Component States

Every entry in `components:` supports the states listed here and nothing beyond them. The brand's own state language is narrow and deliberate: opacity 0.8 on press, a soft diffused shadow on focus, and `{colors.ink-04}` for hover tints. There is no colour-shift vocabulary, because the system has no saturated accent to shift to.

| Component | default | hover | focus-visible | active / pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `{component.button-primary-dark}` | `{colors.primary}` bg, `{shadow.button-inset}` | `{shadow.button-inset}` plus a `{colors.ink-04}` overlay; no colour change | 2px `{colors.focus}` ring, 2px `{colors.canvas}` offset, plus `{shadow.focus-soft}` | opacity 0.8 | opacity 0.4, pointer-events none — prescribed, the file documents no disabled token | inline spinner replaces the label, width held so the button does not reflow | n/a — not a toggle | n/a — errors surface on the field, not the button |
| `{component.button-ghost}` | transparent bg, 1px `{colors.ink-40}` border | border steps to `{colors.hairline-strong}` | 2px `{colors.focus}` ring, 2px offset, plus `{shadow.focus-soft}` | opacity 0.8 | opacity 0.4 — prescribed | inline spinner, label hidden | n/a | n/a |
| `{component.button-cream}` | `{colors.surface-cream}` bg, no border | `{colors.ink-04}` tint | 2px `{colors.focus}` ring, 2px offset | opacity 0.8 | opacity 0.4 — prescribed | inline spinner | n/a | n/a |
| `{component.button-pill-icon}` | opacity 0.5, `{shadow.button-inset}` | opacity 1.0 | 2px `{colors.focus}` ring, 2px offset | opacity 0.8 | opacity 0.3 — prescribed | spinner inside the pill | opacity 1.0 with a 1px `{colors.ink-40}` border — this is the plan-mode / voice-recording toggle, so selected is a real state | n/a |
| `{component.text-input}` | 1px `{colors.hairline}` border, `{colors.muted}` placeholder | border steps to `{colors.hairline-strong}` | 2px `{colors.focus}` ring (the brand's `{colors.ring-brand}` at full opacity — see Accessibility) | n/a — an input has no pressed state | opacity 0.5, `{colors.ink-03}` fill — prescribed | `{component.button-primary-dark}` in the submit slot carries the spinner; the field itself only goes read-only | n/a | 1px `{colors.hairline-strong}` border plus a `{typography.caption}` message in `{colors.ink}` — prescribed, the file documents no error tone |
| `{component.card}`, `{component.card-featured}`, `{component.card-compact}` | 1px `{colors.hairline}` border, no shadow | border darkens toward `{colors.ink-40}` | 2px `{colors.focus}` ring when the whole card is the link target | n/a | n/a | `{colors.ink-03}` skeleton blocks in place of content | n/a | n/a |
| `{component.template-card}` | 1px `{colors.hairline}` border, 12px radius | subtle border darkening (the file's own words) or `{shadow.focus-soft}` | 2px `{colors.focus}` ring, 2px offset | opacity 0.8 | n/a | `{colors.ink-03}` skeleton on the image slot | n/a | n/a |
| `{component.suggestion-pill}` | 1px `{colors.hairline}` border | `{colors.ink-04}` tint | 2px `{colors.focus}` ring | opacity 0.8 | opacity 0.4 — prescribed | n/a | 1px `{colors.ink-40}` border once chosen | n/a |
| `{component.text-link}` | `{colors.ink}` with underline | underline persists; no colour change — the decoration carries the signal | 2px `{colors.focus}` ring, 2px offset | opacity 0.8 | opacity 0.4 — prescribed | n/a | n/a | n/a |
| `{component.top-nav}`, `{component.menu-toggle}` | cream, fixed, no border | `{colors.ink-04}` tint on the toggle | 2px `{colors.focus}` ring on each link and on the toggle | opacity 0.8 on the toggle | n/a | n/a | current-page link keeps the underline permanently — nav has exactly these states and no more | n/a |
| `{component.stats-metric}`, `{component.stats-label}`, `{component.footer}`, `{component.image-card}` | static | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

The last row is a genuine two-state-or-fewer group: these are presentational surfaces with no interaction, so they have a default state and nothing else. Saying so is the point — an invented hover on a stats figure would be noise.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity. It was not measured from the live site — no duration, easing curve or stagger value below was extracted from Lovable's CSS or observed in a recording.** Treat it as the motion that belongs to this cream canvas and this humanist typeface, and replace any value here with a measured one the moment one exists.

**Profile: Playful** (responsive, friendly). The assignment holds, with one qualification worth stating. Lovable has no saturated accent — the file explicitly forbids introducing one — so the usual Playful tell of bright colour on interactive elements is absent. The profile is earned elsewhere: the typeface is described in the file's own words as having "humanist warmth", "slightly rounded terminals" and "organic curves"; the hero carries a soft multi-colour gradient wash in pinks, oranges and blues; the full pill (`{rounded.pill}`) is used extensively on action and toggle buttons; and the brand's documented press feedback is `opacity 0.8` applied "for responsive tactile feedback". That is a friendly, immediate system, not an editorial one. The restraint shows up as amplitude rather than timing: `{motion.ease-enter}` keeps its overshoot, but travel stays at 4–8px and press scale stops at 0.98, because a system whose whole depth model is "pressed into the paper" cannot have things leaping off it.

Playful values: base `{motion.duration-base}` (200ms), overshoot on enter via `{motion.ease-enter}`, stagger `{motion.stagger-step}` (60ms).

### Interaction Table

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, cards, pills, links) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` of the `{colors.ink-04}` tint layer; `opacity` of the `{colors.hairline-strong}` border layer on cards | Unchanged — already opacity-only and at `{motion.duration-reduced}` or less |
| Press (`opacity 0.8`, the brand's own active state) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` 1 → 0.8, plus `transform: scale(0.98)` on `{component.button-primary-dark}` and `{component.button-pill-icon}` | Scale removed; the opacity drop remains, instant |
| Focus ring appears | 0ms — no transition | none | `opacity` of the `{colors.focus}` ring is not animated | Unchanged — the ring must never lag the keyboard |
| Page / route transition | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` 0 → 1, `transform: translateY(8px → 0)` | Travel removed; cross-fade only, capped at `{motion.duration-reduced}` |
| Modal / drawer (mobile hamburger sheet) | enter `{motion.duration-slow}`, exit `{motion.duration-base}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px → 0)` for a modal, `translateX(100% → 0)` for the sheet | All travel removed; both cross-fade at `{motion.duration-reduced}`. The backdrop still fades |
| Dropdown (nav menus, template category menus) | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px → 0) scale(0.98 → 1)` | Travel and scale removed; fade at `{motion.duration-reduced}` |
| Toast | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px → 0)` | Travel removed; fade at `{motion.duration-reduced}`. Auto-dismiss timing is unchanged |
| List enter (`{component.template-card}` gallery, feature cards, `{component.suggestion-pill}` row) | `{motion.duration-base}` per item, `{motion.stagger-step}` (60ms) between items | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px → 0)` | Stagger and travel both removed; the group fades in once at `{motion.duration-reduced}` |
| List exit (filtering the template gallery) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform: translateY(-4px)` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading (button spinner, `{colors.ink-03}` skeletons on cards and the AI chat input) | `{motion.duration-emphasis}` (450ms) per spinner rotation, infinite while pending; skeleton sweep `{motion.duration-slow}` | linear for the spinner, `{motion.ease-standard}` for the sweep | `transform: rotate()` for the spinner, `opacity` for the skeleton | Spinner rotation and skeleton sweep both stop; a static indicator with a text label remains |

Hero gradient note: the warm multi-colour wash behind the hero is **static**. It is the one place in the system where an ambient loop would be tempting, and the file describes it as "atmospheric, barely visible" — a drifting gradient would make the quietest element the busiest. If a future version animates it, it must be declared as brand ambience and frozen under reduced motion.

### Motion Rules

Only `transform` and `opacity` are ever transitioned. Layout-affecting properties are excluded by rule: `width`, `height`, `top`, `left` and `margin` are never transitioned, because each one forces layout and drops frames on the long editorial scroll this system is built for.

- Every exit is shorter than its matching entrance — `{motion.duration-base}` out against `{motion.duration-slow}` in for the drawer, `{motion.duration-fast}` out against `{motion.duration-base}` in everywhere else.
- Nothing moves on first paint in a way that delays content. The hero headline, the hero CTAs and `{component.top-nav}` render at their final position; only below-the-fold groups use an entrance.
- No infinite animation except the loading indicators named above. There is no brand ambience loop.
- Travel never exceeds 16px, and only the mobile nav sheet uses a full-width translate. Press scale never goes below 0.98 and enter scale never starts below 0.98 — the overshoot in `{motion.ease-enter}` supplies the bounce, so the amplitude does not have to.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: every translate, every scale, every {motion.stagger-step} delay,
     the spinner rotation and the skeleton sweep. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (130ms). */
  /* Kept at zero duration: the focus ring, which must track the keyboard. */
  *, *::before, *::after {
    transition-duration: 130ms !important;
    transition-property: opacity !important;
    animation: none !important;
    scroll-behavior: auto !important;
  }
}
```

What is removed: all `translateY` / `translateX` travel, the 0.98 press and dropdown scales, the `{motion.stagger-step}` delay on the template gallery and feature grids, the spinner rotation and the skeleton sweep. What remains: opacity fades at `{motion.duration-reduced}` (130ms) or less, the focus ring at zero duration, the brand's `opacity 0.8` press feedback, and a static labelled indicator in place of the spinner. Nothing becomes unreachable or unreadable when motion is off — no state in this system is communicated by movement alone.

## Accessibility

### Measured Contrast

Computed with WCAG 2.1 relative luminance against the hexes in this file's frontmatter. Nothing here is estimated. Where the brand states a colour as an opacity over cream, the composited hex is given and the composite is what was measured.

| Pair | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 15.51:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.surface-cream}` | 15.51:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.hairline}` (#eceae4 as a fill) | 14.17:1 | 4.5:1 | pass |
| `{colors.muted}` on `{colors.canvas}` | 5.83:1 | 4.5:1 | pass |
| `{colors.muted}` on `{colors.hairline}` | 5.32:1 | 4.5:1 | pass |
| `{colors.on-primary}` on `{colors.primary}` | 16.47:1 | 4.5:1 | pass |
| `{colors.ink-83}` → #414140 on `{colors.canvas}` | 9.30:1 | 4.5:1 | pass |
| `{colors.ink-82}` → #434342 on `{colors.canvas}` | 9.02:1 | 4.5:1 | pass |
| `{colors.focus}` on `{colors.canvas}` | 3.35:1 | 3.0:1 | pass |
| `{colors.focus}` on `{colors.primary}` (dark button) | 4.63:1 | 3.0:1 | pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 3.22:1 | 3.0:1 | pass — prescribed token, not a brand value |
| `{colors.hairline}` on `{colors.canvas}` | **1.10:1** | 3.0:1 | **fail** |
| `{colors.ink-40}` → #9f9e99 on `{colors.canvas}` | **2.44:1** | 3.0:1 | **fail** |
| `{colors.ring-brand}` → #99bbf2 on `{colors.canvas}` | **1.78:1** | 3.0:1 | **fail** |
| `{colors.ink-04}` → #eeebe5 on `{colors.canvas}` | 1.08:1 | n/a | decorative tint, no requirement |
| `{colors.ink-03}` → #f0eee7 on `{colors.canvas}` | 1.06:1 | n/a | decorative tint, no requirement |
| `{colors.on-primary}` on `{colors.canvas}` | 1.06:1 | n/a | never drawn in this combination — off-white is button ink only |

Three failures are real and they are Lovable's, not this document's:

- **`{colors.hairline}` (#eceae4) does not meet WCAG 1.4.11 non-text contrast.** At 1.10:1 against the cream canvas it is decoration, not a boundary. This matters most on `{component.text-input}` and `{component.ai-chat-input}`, where that hairline is the only thing identifying the control — the field background is the same `#f7f4ed` as the page. A low-vision user has no reliable edge to find.
- **`{colors.ink-40}` (rgba(28,28,28,0.4)) at 2.44:1 also misses 3:1**, and it is the stronger of the two real border tones — the one the file assigns to "interactive elements" and to the `{component.button-ghost}` outline. A secondary CTA whose entire visual identity is that border is therefore under-contrasted.
- **`{colors.ring-brand}` (#3b82f6 at 50%) at 1.78:1 cannot serve as a focus indicator.** The brand pairs it with `{shadow.focus-soft}`, and the file's own Don'ts say "don't use sharp focus outlines". A diffused 12px shadow at rgba(0,0,0,0.1) is not a measurable indicator either. This is the single most consequential accessibility gap in the system.

`{colors.hairline-strong}` (#8a8884) is the prescribed parallel token that closes the gap. It stays inside the brand's own model — charcoal `#1c1c1c` at 50% opacity over cream, one stop between the documented 0.4 and 0.82 — so it does not introduce a new hue. `{colors.hairline}` and `{colors.ink-40}` are scoped to decoration and to boundaries that are not the sole carrier of meaning. Neither real hex has been altered; candidate replacements are listed in the audit report under Needs approval.

### Focus Ring Visibility Per Surface

Every surface this file defines, against the one ring. Lovable has only two surface polarities — cream paper and charcoal button — and a single mid-luminance blue clears 3:1 on both, so there is no need for a `focus-on-dark` pair.

| Surface | Ring token | Ratio | Result |
|---|---|---|---|
| `{colors.canvas}` / `{colors.surface-cream}` (#f7f4ed) | `{colors.focus}` | 3.35:1 | pass |
| `{colors.primary}` (#1c1c1c, the dark button) | `{colors.focus}` | 4.63:1 | pass |
| `{colors.hairline}` (#eceae4, used as a fill) | `{colors.focus}` | 3.06:1 | pass |
| The hero gradient wash | `{colors.focus}` | not measurable | A gradient has no single colour. Over the wash, draw the ring two-tone: 2px `{colors.focus}` with a 1px outer edge in `{colors.on-primary}` |

The ring is 2px with a 2px offset in the surface's own colour, so it never sits flush against the control edge, and `{shadow.focus-soft}` is retained alongside it — the brand's soft warm glow stays, it just stops being the only signal. The 3.35:1 figure on cream is a pass with little headroom; it is the floor of this system, and any future surface lighter than #f7f4ed would break it.

### Tap Targets

- `{component.button-primary-dark}`, `{component.button-ghost}`, `{component.button-cream}`: 8px vertical padding plus a 16px/1.5 line box gives roughly 40px of height — **below the 44 × 44 minimum**, by the file's own declared values.
- `{component.menu-toggle}` and `{component.button-pill-icon}`: the file states no dimensions at all. The Responsive section asserts "adequate sizing" and that the pill radius "creates large tap-friendly targets"; neither is a measurement, and a 9999px radius has no bearing on hit area.
- The honest fix for the 40px buttons is an invisible 44px hit area around the visual box, which leaves the compact 8px/16px padding — a real brand characteristic — untouched.
- Per the audit spec, nothing here claims a *rendered* tap-target size. These are the declared values in this file's own frontmatter and prose, which is all a document can honestly be checked against.

### Reduced Motion

Covered in full under Motion & Animation. In short: all travel, all scale and every stagger are removed; opacity fades remain at `{motion.duration-reduced}` (130ms) or less; the focus ring is never animated; the spinner stops and a labelled static indicator takes its place; the hero gradient is static to begin with. No information in this system is carried by movement alone.

### Other

- Type never falls below 14px (`{typography.caption}`, `{typography.button-small}`, `{typography.link-small}`), and body copy sits at 16px / 1.5. That is a comfortable floor.
- `{typography.display-hero}` at line-height 1.00–1.10 with -1.5px tracking is tight by design. At 60px that is fine; the Responsive section scales the headline to 36px on mobile, where 1.10 leading and negative tracking start to crowd. Loosening to 1.15 below 40px is advisable and is not stated in the file.
- `{component.text-link}` carries a permanent underline and does not change colour on hover, so link identification never depends on colour — a genuine strength of this system.
- `{typography.display-alt}` at weight 480 is a variable-font axis value. If the variable font fails to load, the `ui-sans-serif` fallback will round it to 500, which is a visible shift the file does not acknowledge.

## Do's and Don'ts

### Do
- Use the warm cream background (`#f7f4ed`) as the page foundation — it's the brand's signature warmth
- Use Camera Plain Variable at display sizes with negative letter-spacing (-0.9px to -1.5px)
- Derive all grays from `#1c1c1c` at varying opacity levels for tonal unity
- Use the inset shadow technique on dark buttons for tactile depth
- Use `#eceae4` borders instead of shadows for card containment
- Keep the weight system narrow: 400 for body/UI, 600 for headings
- Use full-pill radius (9999px) only for action pills and icon buttons
- Apply opacity 0.8 on active states for responsive tactile feedback

### Don't
- Don't use pure white (`#ffffff`) as a page background — the cream is intentional
- Don't use heavy box-shadows for cards — borders are the containment mechanism
- Don't introduce saturated accent colors — the palette is intentionally warm-neutral
- Don't use weight 700 (bold) — 600 is the maximum weight in the system
- Don't apply 9999px radius on rectangular buttons — pills are for icon/action toggles
- Don't use sharp focus outlines — the system uses soft shadow-based focus indicators
- Don't mix border styles — `#eceae4` for passive, `rgba(28,28,28,0.4)` for interactive
- Don't increase letter-spacing on headings — Camera Plain is designed to run tight at scale

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <600px | Tight single column, reduced padding |
| Mobile | 600–640px | Standard mobile layout |
| Tablet Small | 640–700px | 2-column grids begin |
| Tablet | 700–768px | Card grids expand |
| Desktop Small | 768–1024px | Multi-column layouts |
| Desktop | 1024–1280px | Full feature layout |
| Large Desktop | 1280–1536px | Maximum content width, generous margins |

### Touch Targets
- Buttons: 8px 16px padding (comfortable touch)
- Navigation: adequate spacing between items
- Pill buttons: 9999px radius creates large tap-friendly targets
- Menu toggle: 6px radius button with adequate sizing

### Collapsing Strategy
- Hero: 60px → 48px → 36px headline scaling with proportional letter-spacing
- Navigation: horizontal links → hamburger menu at 768px
- Feature cards: 3-column → 2-column → single column stacked
- Template gallery: grid → stacked vertical cards
- Stats bar: horizontal → stacked vertical
- Footer: multi-column → stacked single column
- Section spacing: 128px+ → 64px on mobile

### Image Behavior
- Template screenshots maintain `1px solid #eceae4` border at all sizes
- 12px border radius preserved across breakpoints
- Gallery images responsive with consistent aspect ratios
- Hero gradient softens/simplifies on mobile

## Iteration Guide

### Quick Color Reference
- Primary CTA: Charcoal (`#1c1c1c`)
- Background: Cream (`#f7f4ed`)
- Heading text: Charcoal (`#1c1c1c`)
- Body text: Muted Gray (`#5f5f5d`)
- Border: `#eceae4` (passive), `rgba(28,28,28,0.4)` (interactive)
- Focus: `rgba(0,0,0,0.1) 0px 4px 12px`
- Button text on dark: `#fcfbf8`

### Example Component Prompts
- "Create a hero section on cream background (#f7f4ed). Headline at 60px Camera Plain Variable weight 600, line-height 1.10, letter-spacing -1.5px, color #1c1c1c. Subtitle at 18px weight 400, line-height 1.38, color #5f5f5d. Dark CTA button (#1c1c1c bg, #fcfbf8 text, 6px radius, 8px 16px padding, inset shadow) and ghost button (transparent bg, 1px solid rgba(28,28,28,0.4) border, 6px radius)."
- "Design a card on cream (#f7f4ed) background. Border: 1px solid #eceae4. Radius 12px. No box-shadow. Title at 20px Camera Plain Variable weight 400, line-height 1.25, color #1c1c1c. Body at 14px weight 400, color #5f5f5d."
- "Build a template gallery: grid of cards with 12px radius, 1px solid #eceae4 border, cream backgrounds. Each card: image with 12px top radius, title below. Hover: subtle border darkening."
- "Create navigation: sticky on cream (#f7f4ed). Camera Plain 16px weight 400 for links, #1c1c1c text. Dark CTA button right-aligned with inset shadow. Mobile: hamburger menu with 6px radius."
- "Design a stats section: large numbers at 48px Camera Plain weight 600, letter-spacing -1.2px, #1c1c1c. Labels below at 16px weight 400, #5f5f5d. Horizontal layout with 32px gap."

### Iteration Checklist
1. Always use cream (`#f7f4ed`) as the base — never pure white
2. Derive grays from `#1c1c1c` at opacity levels rather than using distinct hex values
3. Use `#eceae4` borders for containment, not shadows
4. Letter-spacing scales with size: -1.5px at 60px, -1.2px at 48px, -0.9px at 36px, normal at 16px
5. Two weights: 400 (everything except headings) and 600 (headings)
6. The inset shadow on dark buttons is the signature detail — don't skip it
7. Camera Plain Variable at weight 480 is for special display moments only

## Known Gaps

This file was converted from the early numbered format and had no frontmatter token block. Every token now in the frontmatter was built from a hex, type value or component description already written in the prose. The following are things the prose does not state, and nothing here has been invented to fill them.

**Not stated anywhere in the original file, and therefore absent or prescribed:**

- **No disabled tone.** No colour, opacity or treatment for a disabled control appears in the file. The `opacity 0.4` / `opacity 0.3` values in the Component States table are prescribed, derived from the brand's own `opacity 0.8` press convention.
- **No semantic palette.** No success, warning, error or info colour exists. The system has no saturated accent at all by design, so an error state has no tone to use; the Component States table resolves this with a `{colors.hairline-strong}` border and a `{colors.ink}` message, which is prescribed.
- **No hover tone for most components.** The file names `{colors.ink-04}` as "subtle hover backgrounds" and says template cards get "subtle shadow or border darkening", but specifies no value. The hover column is built from those two phrases and is otherwise prescribed.
- **No focus ring geometry.** The file gives the ring colour (Tailwind blue at 50%) and the focus shadow, but no width, offset or style. The 2px / 2px offset is prescribed.
- **No measured button or control dimensions.** Padding is given (8px 16px); height, min-width and icon-button size are not. Tap-target conclusions in Accessibility are derived from padding and line height only.
- **No type scale below 14px and no explicit mobile type sizes** beyond the headline ladder 60 → 48 → 36px.
- **No letter-spacing value for the 36px → smaller transition** other than "proportional".
- **No shadow token names in the original.** The `shadow:` group names were assigned during conversion; the values are verbatim from the prose.
- **Logo dimensions (128.75 × 22px)** are stated but no logo clear-space, minimum size or lockup rule is.
- **Dark mode is never mentioned.** The dark surface in this system is a button, not a theme. Whether Lovable has a dark theme is unknown from this document.
- **The hero gradient has no stated stops.** "Pinks, oranges, blues" is all the file gives; no hex, angle or stop position. It is referenced in prose only and has no token.
- **Motion is entirely prescribed.** See the first line of Motion & Animation. No timing in this file was measured.
- **Max content width is "approximately 1200px"** — the original hedges, and the hedge is preserved rather than hardened into a token.
