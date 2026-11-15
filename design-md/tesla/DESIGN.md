---
version: alpha
name: Tesla-design-analysis
description: Radical subtraction — a white canvas (#FFFFFF) carrying full-viewport cinematic car photography, with a single Electric Blue (#3E6AE1) reserved for primary CTAs and three dark greys for text hierarchy. No shadows, no gradients, no patterns, 4px radius on every control. Every colour, type and component token below is read from this file's own prose; the motion group is prescribed, not measured, except the two extracted transition values marked as such.

colors:
  canvas: "#FFFFFF"
  surface-ash: "#F4F4F4"
  surface-carbon: "#171A20"
  surface-frost: rgba(255, 255, 255, 0.75)
  overlay-modal: rgba(128, 128, 128, 0.65)
  ink: "#171A20"
  ink-on-image: "#FFFFFF"
  body: "#393C41"
  text-dim: "#5C5E62"
  muted-placeholder: "#8E8E8E"
  border: "#EEEEEE"
  border-strong: "#D0D1D2"
  accent: "#3E6AE1"
  on-accent: "#FFFFFF"
  focus: "#3E6AE1"

typography:
  hero-title:
    fontFamily: "Universal Sans Display, -apple-system, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: normal
  promo-text:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 0.91
    letterSpacing: normal
  product-name:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: normal
  category-label:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    letterSpacing: normal
  nav-item:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: normal
  button-label:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: normal
  body:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: normal
  sub-link:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: normal

spacing:
  fine: 4px
  base: 8px
  md: 16px
  lg: 21.44px

rounded:
  none: 0px
  button: 4px
  card: 12px
  dot: 50%

shadow:
  none: rgba(0, 0, 0, 0)
  focus-inset: rgba(0, 0, 0, 0) 0px 0px 0px 2px inset
  hover-hint: rgba(0, 0, 0, 0.05)

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
  duration-extracted-state: 330ms
  ease-extracted-state: cubic-bezier(0.5, 0, 0, 0.75)

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-label}"
    rounded: "{rounded.button}"
    padding: 4px
    minHeight: 40px
    width: 200px
    borderColor: transparent
    borderWidth: 3px
    boxShadow: "{shadow.focus-inset}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-label}"
    rounded: "{rounded.button}"
    padding: 4px
    minHeight: 40px
    width: 200px
    borderColor: transparent
    borderWidth: 3px
  button-nav:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    rounded: "{rounded.button}"
    padding: 4px 16px
    minHeight: 32px
  link-text:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-dim}"
    typography: "{typography.sub-link}"
    rounded: "{rounded.none}"
  nav-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    rounded: "{rounded.none}"
  card-vehicle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.product-name}"
    rounded: "{rounded.none}"
  card-category:
    backgroundColor: transparent
    backgroundImage: full-bleed photography — no measurable colour
    textColor: "{colors.ink-on-image}"
    typography: "{typography.category-label}"
    rounded: "{rounded.card}"
  section-ash:
    backgroundColor: "{colors.surface-ash}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
  hero-title-overlay:
    backgroundColor: transparent
    backgroundImage: full-bleed photography — no measurable colour
    textColor: "{colors.ink-on-image}"
    typography: "{typography.hero-title}"
    rounded: "{rounded.none}"
  hero-promo:
    backgroundColor: transparent
    backgroundImage: full-bleed photography — no measurable colour
    textColor: "{colors.accent}"
    typography: "{typography.promo-text}"
    rounded: "{rounded.none}"
  overlay-text-panel:
    backgroundColor: "{colors.surface-carbon}"
    textColor: "{colors.ink-on-image}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
  carousel-arrow:
    backgroundColor: "{colors.surface-frost}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    size: 44px
  carousel-dot:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.dot}"
  chat-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
  input-chat:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
---

# Design System Inspired by Tesla

## Overview

Tesla's website is an exercise in radical subtraction — a digital showroom where the product is everything and the interface is almost nothing. The page opens with a full-viewport hero that fills the entire screen with cinematic car photography: three vehicles arranged on polished concrete against a hazy cityscape sky, with a single model name floating above in translucent white type. There are no decorative borders, no gradients, no patterns, no shadows. The UI exists only to provide just enough navigational structure to get out of the way. Every pixel that isn't product imagery is white space, and that restraint is the design system's most powerful statement.

The color philosophy is almost ascetic: a single blue (`{colors.accent}` — `#3E6AE1`) for primary calls to action, three shades of dark gray for text hierarchy, and white for everything else. The entire emotional weight is carried by photography — sprawling landscape shots, studio-lit vehicle profiles, and atmospheric environmental compositions that stretch edge-to-edge across each viewport-height section. The UI chrome dissolves into the imagery. The navigation bar floats above the hero with no visible background, border, or shadow — the TESLA wordmark and five navigation labels simply exist in the space, trusting the content beneath them to provide sufficient contrast.

Typography recently transitioned from Gotham to Universal Sans — a custom family split into "Display" for headlines and "Text" for body/UI elements — unifying the website, mobile app, and in-car software into a single typographic voice. The Display variant renders hero titles at 40px weight 500, while the Text variant handles everything from navigation (14px/500) to body copy (14px/400). The font carries a geometric precision with slightly humanist terminals that feels engineered rather than designed — exactly matching Tesla's brand identity of technology that doesn't need to announce itself. There are no text shadows, no text gradients, no decorative type treatments. Every letterform earns its place through clarity alone.

**Key Characteristics:**
- Full-viewport hero sections (100vh) dominated by cinematic car photography with minimal overlay UI
- Near-zero UI decoration: no shadows, no gradients, no borders, no patterns anywhere on the page
- Single accent color — Electric Blue (`{colors.accent}`) — used exclusively for primary CTA buttons
- Universal Sans font family (Display + Text) unifying web, app, and in-car interfaces
- Photography-first presentation where product imagery carries all emotional weight
- Frosted-glass navigation concept with transparent/white nav (`{colors.surface-frost}`) that floats over hero content
- 0.33s cubic-bezier transitions as the universal timing for all interactive state changes — the one motion value this file genuinely extracted, carried as `{motion.duration-extracted-state}`
- Carousel-driven hero with dot indicators and edge arrow navigation for multiple vehicle showcases
- "Ask a Question" persistent chatbot bar anchored to the viewport bottom

## Colors

### Primary
- **Electric Blue** (`{colors.accent}` — `#3E6AE1`): Primary CTA button background — a confident, mid-saturation blue (rgb 62, 106, 225) that stands alone as the only chromatic color in the entire interface. Used exclusively for "Order Now" and other primary action buttons
- **Pure White** (`{colors.canvas}` — `#FFFFFF`): Dominant background color for all surfaces, panels, navigation, and secondary button fills — the canvas that lets photography breathe. The same value is bound separately as `{colors.on-accent}` for the label drawn on the blue CTA and as `{colors.ink-on-image}` for type drawn over photography, because those are different jobs on different grounds

### Secondary & Accent
- **Promo Blue** (`{colors.accent}` — `#3E6AE1`): Blue also serves for promotional text ("0% APR Available") displayed over hero imagery in the same hue as the CTA — creating a visual link between incentive messaging and action. It is the same token, not a second one; the palette genuinely contains one chromatic value
- No secondary accent colors exist. Tesla deliberately avoids color variety to maintain extreme visual discipline

### Surface & Background
- **White Canvas** (`{colors.canvas}` — `#FFFFFF`): Page background, navigation panel, dropdown menus, and all surface containers
- **Light Ash** (`{colors.surface-ash}` — `#F4F4F4`): Subtle alternate surface for section differentiation — barely perceptible shift from pure white (rgb 244, 244, 244). Measured against the canvas it is 1.10:1, which is the intended effect and also means it can never carry a boundary on its own
- **Carbon Dark** (`{colors.surface-carbon}` — `#171A20`): Dark surface color for hero text overlays and potential dark-mode contexts (rgb 23, 26, 32) — a warm near-black with a blue undertone. It is the same value as `{colors.ink}`; the file uses one carbon tone both as ink on light grounds and as ground under light ink
- **Frosted Glass** (`{colors.surface-frost}` — `rgba(255, 255, 255, 0.75)`): Semi-transparent white for navigation backdrop-filter effects on scroll. Composited over the canvas it resolves to `#FFFFFF`; over photography its rendered colour is unmeasurable from a document
- **Modal Overlay** (`{colors.overlay-modal}` — `rgba(128, 128, 128, 0.65)`): The scrim behind modal overlays and region/cookie popups. Composited over the canvas it resolves to `#ACACAC`

### Neutrals & Text
- **Carbon Dark** (`{colors.ink}` — `#171A20`): Primary heading and navigation text — the darkest text value (rgb 23, 26, 32), used for model names, nav labels, and hero titles on light backgrounds
- **Graphite** (`{colors.body}` — `#393C41`): Body text and secondary content (rgb 57, 60, 65) — the default paragraph color, slightly warmer than pure gray
- **Pewter** (`{colors.text-dim}` — `#5C5E62`): Tertiary text for sub-links, secondary navigation links like "Learn" and "Order" (rgb 92, 94, 98). The strongest muted tone the palette owns, and therefore the tone to reach for wherever a muted element must still be perceivable
- **Silver Fog** (`{colors.muted-placeholder}` — `#8E8E8E`): Placeholder text in input fields and disabled states (rgb 142, 142, 142). As placeholder text this is a **real AA failure of the live site** — 3.28:1 on the canvas — see Accessibility
- **Cloud Gray** (`{colors.border}` — `#EEEEEE`): Light borders and divider lines (rgb 238, 238, 238)
- **Pale Silver** (`{colors.border-strong}` — `#D0D1D2`): Subtle UI borders and delineation (rgb 208, 209, 210)

### Semantic & Accent
- Tesla's marketing site avoids semantic color coding (no green/red/yellow status indicators). Error, success, and warning states follow standard browser defaults in form contexts
- The blue CTA (`{colors.accent}`) serves as the sole interactive color signal

### Borders
Both extracted boundary tones are **decoration only**, and the file's own Don'ts agree: "Add borders to cards or containers" is forbidden, because separation is spacing. `{colors.border}` measures 1.16:1 and `{colors.border-strong}` 1.53:1 against the canvas — far below the 3:1 a perceivable boundary needs. Neither is re-pointed, and no third hairline is invented. Where a boundary is the *only* thing defining a control — the chat bar's input field — the palette already owns a tone that clears 3:1: use `{colors.text-dim}` (6.50:1 on the canvas). Re-binding the extracted hairlines is a brand-owner decision and sits under Needs approval in the audit report, not in this file.

### Focus
- **Focus ring** (`{colors.focus}` — `#3E6AE1`): **Prescribed, not extracted.** The live site reserves space for a focus treatment — the primary CTA carries a 3px transparent border and an invisible inset shadow (`{shadow.focus-inset}`) that "animates to visible on focus" — but states no ring colour. This ring reuses the brand's own Electric Blue; no new brand colour is introduced. One ring serves every surface this file defines rather than a light/dark pair, because the blue clears 3:1 on all three: canvas 4.82:1, `{colors.surface-ash}` 4.39:1, `{colors.surface-carbon}` 3.61:1. Over full-bleed photography and over `{colors.overlay-modal}`, neither of which has a reliable measurable colour, the ring is two-tone — see Accessibility

### Gradient System
- No gradients are used anywhere in the interface
- Depth is achieved entirely through photography, whitespace, and the binary contrast between full-bleed imagery and clean white surfaces
- The navigation achieves layering through opacity (frosted glass effect) rather than gradient or shadow

## Typography

### Font Family
- **Display**: `Universal Sans Display`, -apple-system, Arial, sans-serif — used for hero titles and large model names. A geometric sans-serif with precisely engineered proportions, recently replacing Gotham to unify Tesla's digital ecosystem (website, mobile app, vehicle interface)
- **Text/UI**: `Universal Sans Text`, -apple-system, Arial, sans-serif — used for navigation, body copy, buttons, and all UI text. Optimized for legibility at smaller sizes with slightly wider proportions than the Display variant
- **No OpenType features** detected — typography is completely unembellished
- **No italic variants** observed on the marketing site

### Hierarchy

| Role | Token | Size | Weight | Line Height | Letter Spacing | Notes |
|------|-------|------|--------|-------------|----------------|-------|
| Hero Title | `{typography.hero-title}` | 40px (2.50rem) | 500 | 48px (1.20) | normal | Universal Sans Display, white on dark hero imagery |
| Product Name | `{typography.product-name}` | 17px (1.06rem) | 500 | 20px (1.18) | normal | Universal Sans Text, model names in nav panel and cards |
| Nav Item | `{typography.nav-item}` | 14px (0.88rem) | 500 | 16.8px (1.20) | normal | Universal Sans Text, primary navigation labels |
| Body Text | `{typography.body}` | 14px (0.88rem) | 400 | 20px (1.43) | normal | Universal Sans Text, paragraph and descriptive content |
| Button Label | `{typography.button-label}` | 14px (0.88rem) | 500 | 16.8px (1.20) | normal | Universal Sans Text, CTA button text |
| Sub-link | `{typography.sub-link}` | 14px (0.88rem) | 400 | 20px (1.43) | normal | Tertiary links (Learn, Order, Experience) |
| Promo Text | `{typography.promo-text}` | 22px (1.38rem) | 400 | 20px (0.91) | normal | White promotional text on hero ("0% APR Available") |
| Category Label | `{typography.category-label}` | 16px (est.) | 500 | — | normal | White text labels on category cards ("Sport Sedan"). No line height recorded — see Known Gaps |

Every role here is at or below 22px at weight 400–500, so the 4.5:1 normal-text threshold applies to all of them; nothing in this file qualifies for the 3:1 large-text allowance. Body copy at 14px/400 in `{colors.body}` measures 11.07:1 on the canvas and 10.07:1 on `{colors.surface-ash}` — comfortably readable on both of this file's light surfaces.

### Principles
- **"Normal" letter-spacing everywhere**: Unlike most modern tech brands that use negative tracking for headlines, Tesla uses default letter-spacing at every level. This reflects a philosophy that the typeface should speak for itself without manipulation
- **Weight restraint**: Only two weights appear — 500 (medium) for headings/UI and 400 (regular) for body. No bold (700), no light (300). The system avoids typographic drama
- **Unified font sizing**: Most UI text clusters at 14px with only hero titles (40px) and promo text (22px) breaking away. This extreme uniformity creates a sense of engineered consistency
- **Display vs Text split**: The two-variant system (Display for hero, Text for UI) creates subtle optical correction without visible stylistic difference — they appear as the same typeface at different sizes
- **No text transforms**: No uppercase text appears in the main navigation or CTAs — the lowercase approach reinforces Tesla's understated confidence

## Layout

### Spacing System
- **Base unit**: 8px (`{spacing.base}`)
- **Common values**: 8px (`{spacing.base}`, 0.5rem), 16px (`{spacing.md}`, 1rem), 21.44px (`{spacing.lg}`, 1.34rem)
- **Button padding**: 4px (`{spacing.fine}`, minimal outer) with content centering via flexbox, `{spacing.fine}` `{spacing.md}` for nav items
- **Section padding**: Full-viewport sections with content centered vertically
- **Card gap**: approximately `{spacing.md}` between category cards

### Grid & Container
- **Max width**: approximately 1383px (full viewport width used for most content)
- **Hero**: Full-bleed, edge-to-edge, 100vh sections
- **Navigation panel**: 3-column grid for vehicle cards with right-aligned text sidebar (~70/30 split)
- **Category cards**: 2-up horizontal layout (large left card + smaller right card)

### Whitespace Philosophy
Tesla uses whitespace as a luxury signal. The generous vertical spacing between sections (each section is a full viewport height) means you can only see one "message" at a time — one car, one model name, one CTA pair. This creates a gallery-like browsing experience where each scroll is a deliberate transition, not a continuous feed. White space is not empty — it's the frame that elevates each vehicle to the status of art piece.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Level 0 (Flat) | No shadow, no border (`{shadow.none}`) | Default state for all elements — cards, panels, buttons at rest |
| Level 1 (Frost) | `{colors.surface-frost}` backdrop | Navigation bar on scroll — frosted glass transparency |
| Level 2 (Overlay) | `{colors.overlay-modal}` | Modal overlays and region/cookie popups |
| Level 3 (Subtle) | `{shadow.hover-hint}` | Minimal shadow hints on rare hover states |

Elevation here is expressed one way — by alpha, not by mixing shadow and border at random. Levels 1 and 2 are opacity over a ground; Level 0 is the absence of both. Level 3 is the single exception, and it contradicts this file's own Don'ts ("Add shadows to any element"); it is recorded because the source records it, and should be read as a vestige rather than a rung on the ladder.

The light surface layers themselves are deliberately near-invisible: `{colors.canvas}` to `{colors.surface-ash}` is 1.10:1. A reader looking for a card edge will not find one, by design — which is why spacing and photography, not luminance steps, do the separating. `{colors.surface-carbon}` against the canvas is 17.43:1, so the one real layer jump in the system is light-to-dark, not raised-neutral.

### Shadow Philosophy
Tesla's approach to elevation is essentially "none." The site avoids box-shadows entirely in its primary interface. Depth is communicated through three alternative strategies:
1. **Z-index layering**: The sticky navigation sits above hero content through positioning, not shadow
2. **Opacity-based transparency**: The frosted glass nav and overlay modals use background-color opacity rather than shadow to indicate layering
3. **Photography-as-depth**: The full-bleed images create their own visual depth through perspective, lighting, and composition — making UI shadows redundant

### Decorative Depth
- No gradients, glows, or atmospheric effects on UI elements
- The hero imagery itself provides all visual richness — sunset skies, reflected light on car surfaces, ground shadows from studio lighting
- The carousel arrow buttons use a semi-transparent white background to float above the hero imagery without disrupting it

## Shapes

### Border Radius Scale
| Value | Token | Context |
|-------|-------|---------|
| 0px | `{rounded.none}` | Most elements — sharp edges are the default |
| 4px | `{rounded.button}` | Buttons (primary, secondary, nav items) — barely perceptible rounding |
| ~12px | `{rounded.card}` | Category cards — noticeable but restrained rounding on larger surfaces |
| 50% | `{rounded.dot}` | Carousel dot indicators — perfect circles |

The ladder is 0 → 4 → 12 → 50%, with nothing sitting off its own scale. The 3px border width on the CTA buttons is a reserved-space device for the focus animation, not a step in a boundary scale: no other element in the file carries a border width, so there is no border ladder for it to be consistent with.

## Components

### Buttons
All buttons use barely-rounded rectangles (`{rounded.button}` — 4px border-radius) — creating a sharp, technical aesthetic that mirrors the precision of the vehicles.

**Primary CTA** (`{components.button-primary}`) — The main action button:
- Default: bg `{colors.accent}` (Electric Blue), text `{colors.on-accent}`, typography `{typography.button-label}`, padding `{spacing.fine}` with inner content centering, borderRadius `{rounded.button}`, minHeight 40px, width 200px
- Border: 3px solid transparent (reserves space for focus/active border animation)
- Box Shadow: `{shadow.focus-inset}` — `rgba(0,0,0,0) 0px 0px 0px 2px inset`, invisible at rest, animates to visible on focus
- Transition: `border-color 0.33s, background-color 0.33s, color 0.33s, box-shadow 0.25s` — extracted; see Motion & Animation
- States recorded: default; hover (subtle darkening of the blue background); focus-visible (prescribed mapping of the extracted focus style — the reserved border and inset shadow become visible, drawn in `{colors.focus}`); active (the reserved 3px border animates in)
- States not documented in the source: pressed as distinct from active, loading, selected, error
- Used for: "Order Now" calls to action

**Secondary CTA** (`{components.button-secondary}`) — The alternative action button:
- Default: bg `{colors.canvas}`, text `{colors.body}` (Graphite), same dimensions and border pattern as primary
- Transition: identical timing to primary (`{motion.duration-extracted-state}`)
- States recorded: default; hover (the same colour-only treatment as primary); focus-visible (prescribed, as primary); active
- States not documented in the source: pressed as distinct from active, loading, selected, error
- Used for: "View Inventory" alongside primary CTA

**Nav Button** (`{components.button-nav}`) — Top navigation items:
- Default: bg transparent, text `{colors.ink}` (Carbon Dark), typography `{typography.nav-item}`, borderRadius `{rounded.button}`, padding `{spacing.fine}` `{spacing.md}`, minHeight 32px
- Transition: `color 0.33s, background-color 0.33s`
- States recorded: default; hover; active/expanded (subtle background highlight while its dropdown panel is open); focus-visible (prescribed, drawn in `{colors.focus}`)
- States not documented in the source: pressed as distinct from active, disabled, loading, selected, error
- Used for: "Vehicles", "Energy", "Charging", "Discover", "Shop"

**Text Link** (`{components.link-text}`) — In-content actions:
- Default: text `{colors.text-dim}` (Pewter), typography `{typography.sub-link}`, no background, no border
- Hover: underline decoration with box-shadow transition
- Transition: `box-shadow 0.33s cubic-bezier(0.5, 0, 0, 0.75), color 0.33s` — the one easing curve this file extracted, carried as `{motion.ease-extracted-state}`
- States recorded: default; hover (underline); focus-visible (prescribed, drawn in `{colors.focus}`)
- States not documented in the source: active, pressed, disabled, loading, selected, error
- Used for: "Learn", "Order", "Experience", "New", "Pre-Owned" links in dropdown panel

### Cards & Containers

**Vehicle Card** (`{components.card-vehicle}`, navigation panel):
- Background: transparent (inherits panel white — `{colors.canvas}`)
- Border: none
- Shadow: `{shadow.none}`
- Content: vehicle image (transparent PNG) + model name in `{typography.product-name}` centered below + two text links
- Layout: 3-column grid within the dropdown panel
- States: **default only, genuinely.** The source states there is no hover animation on the card itself; interaction happens entirely through the text links beneath it, which carry their own states

**Category Card** (`{components.card-category}`, homepage lower section):
- Background: full-bleed landscape photography
- Border radius: `{rounded.card}` (approximately 12px, subtly rounded)
- Overflow: hidden (clips image to rounded corners)
- Text: white label (`{colors.ink-on-image}`, `{typography.category-label}`) in top-left corner ("Sport Sedan", "Midsize SUV")
- Size: large format, approximately 2:1 aspect ratio
- No shadow, no border, no overlay gradient — text relies on image darkness for contrast
- States recorded: default; focus-visible (prescribed — the two-tone ring described in Accessibility, since the card sits on photography)
- States not documented in the source: hover, active, pressed, disabled, loading, selected, error

### Inputs & Forms
- Background: transparent over `{colors.canvas}`
- Text color: `{colors.ink}` (Carbon Dark)
- Placeholder color: `{colors.muted-placeholder}` (Silver Fog) — 3.28:1 on the canvas, a real AA failure, disclosed in Accessibility
- Border: minimal, inherits from browser defaults
- Font: `{typography.body}`
- The "Ask a Question" chatbot input bar (`{components.input-chat}`, inside `{components.chat-bar}`) sits at the viewport bottom with a clean white background and subtle border. Where that hairline is the field's only boundary, draw it in `{colors.text-dim}`; neither extracted hairline tone can be seen
- States recorded: default; disabled (the source binds Silver Fog to both placeholder and disabled text); error (the source states explicitly that error, success and warning follow the browser's default form styling — the site defines no semantic colour of its own)
- States not documented in the source: hover, active, pressed, loading, selected, and focus-visible as an extracted style

### Navigation
- **Desktop**: Centered horizontal nav with TESLA wordmark (spaced uppercase letters) on the left, five category buttons center-aligned, and three icon buttons (help, globe/language, account) on the right
- **Background**: White `{colors.canvas}` (transitions from transparent over dark hero to opaque white on scroll via class toggle `tds-site-header--white-background`)
- **Dropdown panel** (`{components.nav-panel}`): Full-width white panel with 3-column vehicle grid + right sidebar text links, no shadow, no border — appears seamlessly below the nav
- **Sticky behavior**: `sticky-without-slide` class — stays at top without slide-in animation
- **Mobile**: Hamburger collapse pattern
- **No visible separator** between nav and content — the nav blends with the hero
- States recorded: default; hover on each nav item; active/expanded while a panel is open; focus-visible (prescribed)
- States not documented in the source: pressed, disabled, loading, selected, error

### Image Treatment
- **Hero** (`{components.hero-title-overlay}`): Full-viewport (100vh) sections with cinematic photography — edge-to-edge, no padding, no margin
- **Vehicle images**: Transparent PNG renders on white background in dropdown panel, studio-quality 3/4 angle shots
- **Category cards**: Landscape photography with approximately 2:1 ratio, rounded corners (`{rounded.card}`)
- **Carousel**: Auto-advancing with dot indicators (`{components.carousel-dot}`, 3 dots) and left/right arrow navigation on edges (`{components.carousel-arrow}`, `{colors.surface-frost}` fill)
- **Lazy loading**: Below-fold sections use lazy loading, rendering as blank white until scrolled into view
- States recorded: default; loading (the extracted lazy-load behaviour — a below-fold section renders as blank white canvas until it scrolls into view, with no skeleton, no spinner and no placeholder image)
- States not documented in the source, for the carousel dots in particular: the treatment that marks the current slide, so `selected` is left unfilled here rather than guessed

### Persistent Chat Bar
- Anchored to viewport bottom, visible across all sections (`{components.chat-bar}`)
- White background (`{colors.canvas}`) with subtle border
- Contains: chat icon + "Ask a Question" label + placeholder text ("What's Dog Mode?") + send icon + "Schedule a Drive Today" secondary CTA
- Schedule CTA has a teal/blue icon accent — no hex is recorded for it, so no token was created; see Known Gaps
- States recorded: default; hover on the send icon and the secondary CTA; focus-visible (prescribed)
- States not documented in the source: active, pressed, disabled, loading, selected, error

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** The duration ladder, the easing curves and all choreography below are the shared **Cinematic** profile from `theme-audit/SPEC.md` section 5, carried verbatim in the `motion:` frontmatter group so that every Cinematic file in this collection behaves as a sibling.

**One documented deviation, and it is an extracted one.** Unlike most files in this collection, Tesla's source does record real transition values: `0.33s` on `border-color`, `background-color` and `color`, `0.25s` on `box-shadow`, and one easing curve, `cubic-bezier(0.5, 0, 0, 0.75)`, on the text-link box-shadow. Those two facts are carried beside the profile block as `{motion.duration-extracted-state}` (330ms) and `{motion.ease-extracted-state}`, and the row they govern — hover, the one interaction the extracted CSS plainly covers — uses the extracted value rather than the profile's `{motion.duration-fast}` (240ms). Everything the source is silent about uses the profile verbatim. An extracted fact outranks a prescribed one.

Cinematic is the right profile here on the assignment rule's first clause: automotive identity, full-viewport cinematic photography, sparse type and a deliberately slow, gallery-like reveal. The white canvas does not change the answer; SPEC says as much.

A second brand rule shapes the table: this file's own Don'ts forbid scale and translate on hover ("Tesla's interactions are color-only"). Hover and press therefore carry no transform at all. Page transitions, modals, dropdowns, toasts and lists keep the profile's travel, since the source's rule is about interaction feedback rather than about reveals. Only `transform` and `opacity` are animated; the extracted colour and box-shadow transitions are recorded as the brand's own behaviour and stay confined to the interaction rows.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-extracted-state}` (extracted) | `{motion.ease-standard}` | `opacity`, plus the extracted `background-color` / `border-color` / `color` crossfade — no transform (brand rule) | Same crossfade, capped at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` only — no scale pop (brand rule) | Unchanged; already at or below `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring and of the extracted inset `{shadow.focus-inset}` | Ring appears instantly and is never suppressed |
| Page / route transition | `{motion.duration-emphasis}` | `{motion.ease-enter}` | `opacity` 0→1, `transform: translateY(24px)`→0 | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(32px)`→0 | Travel removed; the `{colors.overlay-modal}` scrim fades at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-base}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown (nav panel) enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| List enter (vehicle grid, category cards) | `{motion.duration-base}`, staggered by `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px)`→0 | Stagger and travel removed; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading (a lazy-loaded section arriving) | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` 0→1 on the section once its image has decoded | Fade at `{motion.duration-reduced}`; the section may simply appear with no transition |
| Hero carousel auto-advance — **stated here as deliberate brand ambience**, since the source records an auto-advancing hero | `{motion.duration-emphasis}` crossfade on a slow interval | `{motion.ease-enter}` | `opacity` between slides, `transform: scale(1)`→`scale(1.03)` on the active slide | Ambience frozen: auto-advance stops at `scale(1)` and the carousel becomes manual, driven only by its dots and arrows |

Exit is always shorter than its matching entrance. Nothing animates on first paint in a way that delays content: the hero image paints first, and the model name and CTA pair fade in after it, never gating it. There is no infinite animation other than the carousel ambience named above.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: every translate and scale, the hero carousel's auto-advance and
     its slow scale ambience, and the list stagger. */
  /* Kept: opacity fades only, capped at {motion.duration-reduced} (150ms),
     the extracted colour crossfades on hover (also capped), and the focus
     ring, which appears instantly and is never removed. */
  *, *::before, *::after {
    transition-property: opacity, color, background-color, border-color;
    transition-duration: 150ms; /* {motion.duration-reduced} */
    animation: none;
  }
}
```

## Accessibility

Every ratio below is computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. **The extracted brand values are frozen: the failures listed here are real failures of the live Tesla interface, disclosed rather than corrected.**

### Measured contrast — key pairs

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `ink` #171A20 on `canvas` #FFFFFF | 17.43:1 | 4.5:1 | Pass |
| `ink` #171A20 on `surface-ash` #F4F4F4 | 15.84:1 | 4.5:1 | Pass |
| `body` #393C41 on `canvas` | 11.07:1 | 4.5:1 | Pass |
| `body` #393C41 on `surface-ash` | 10.07:1 | 4.5:1 | Pass |
| `text-dim` #5C5E62 on `canvas` | 6.50:1 | 4.5:1 | Pass |
| `text-dim` #5C5E62 on `surface-ash` | 5.91:1 | 4.5:1 | Pass |
| `muted-placeholder` #8E8E8E on `canvas` | 3.28:1 | 4.5:1 | **Fail — real brand failure.** Silver Fog is the live site's placeholder colour. It is defensible as *disabled* text, where WCAG sets no requirement; as placeholder text it misses AA. The nearest passing grey on white is #767676 (4.54:1), and `{colors.text-dim}` already clears it |
| `muted-placeholder` #8E8E8E on `surface-ash` | 2.98:1 | 4.5:1 | **Fail — real brand failure.** Worse on the ash surface than on the canvas |
| `on-accent` #FFFFFF on `accent` #3E6AE1 | 4.82:1 | 4.5:1 | Pass — the Electric Blue CTA with a white label clears AA, with little margin |
| `accent` #3E6AE1 on `canvas` | 4.82:1 | 4.5:1 as text, 3:1 non-text | Pass — so the promo line ("0% APR Available") is legible wherever it sits over a light part of the hero image |
| `border` #EEEEEE on `canvas` | 1.16:1 | 3:1 | **Fail — frozen decorative hairline.** Cloud Gray divides stacked content; it is never the sole boundary of a control |
| `border` #EEEEEE on `surface-ash` | 1.05:1 | 3:1 | **Fail — invisible by construction.** Cloud Gray on Light Ash is two near-identical whites |
| `border-strong` #D0D1D2 on `canvas` | 1.53:1 | 3:1 | **Fail — frozen decorative hairline.** Pale Silver is the strongest boundary tone the live site defines, and it still does not reach 3:1 |
| `border-strong` #D0D1D2 on `surface-ash` | 1.39:1 | 3:1 | **Fail — real brand failure** |
| `ink-on-image` #FFFFFF on `surface-carbon` #171A20 | 17.43:1 | 4.5:1 | Pass |
| `canvas` #FFFFFF against `surface-ash` #F4F4F4 | 1.10:1 | — | Layer separation, not a text pair. The two light surfaces are not distinguishable from each other; that is the documented intent |

Tesla's palette has **no boundary tone that can carry a perceivable edge.** That is the single most useful accessibility fact about this design system: any control whose only definition is a hairline — a text input, a segmented control, a bordered select — cannot be built from the extracted palette and must borrow `{colors.text-dim}` (6.50:1 on the canvas, 5.91:1 on ash) instead.

### Component pairs

| Component | Measured | Required | Verdict |
|---|---|---|---|
| `button-primary` — #FFFFFF on #3E6AE1 at 14px/500 | 4.82:1 | 4.5:1 | Pass |
| `button-secondary` — #393C41 on #FFFFFF at 14px/500 | 11.07:1 | 4.5:1 | Pass |
| `button-nav` — #171A20 over the canvas at 14px/500 | 17.43:1 | 4.5:1 | Pass |
| `link-text` — #5C5E62 on #FFFFFF at 14px/400 | 6.50:1 | 4.5:1 | Pass |
| `card-vehicle` — #171A20 on #FFFFFF at 17px/500 | 17.43:1 | 4.5:1 | Pass |
| `section-ash` — #393C41 on #F4F4F4 at 14px/400 | 10.07:1 | 4.5:1 | Pass |
| `overlay-text-panel` — #FFFFFF on #171A20 at 14px/400 | 17.43:1 | 4.5:1 | Pass |
| `chat-bar` / `input-chat` — #171A20 on #FFFFFF at 14px/400 | 17.43:1 | 4.5:1 | Pass |
| `input-chat` placeholder — #8E8E8E on #FFFFFF at 14px/400 | 3.28:1 | 4.5:1 | **Fail**, as above |
| `card-category`, `hero-title-overlay`, `hero-promo` — white or blue type over full-bleed photography | not measurable | 4.5:1 | **Unverifiable from a document.** The source itself says the category-card label "relies on image darkness for contrast" and specifies no scrim and no overlay gradient. Any image whose top-left corner is light breaks the label, and nothing in the system prevents that |

### Focus ring visibility on every surface this file defines

`{colors.focus}` (#3E6AE1) is drawn as a 2px ring with a 2px offset, outside the control, so it is judged against the surface behind the control rather than against the control's own fill. Prescribed, not extracted. It reuses the brand's existing Electric Blue rather than introducing a colour.

| Surface it is drawn on | Measured | Required | Verdict |
|---|---|---|---|
| `canvas` #FFFFFF | 4.82:1 | 3:1 | Pass |
| `surface-ash` #F4F4F4 | 4.39:1 | 3:1 | Pass |
| `surface-carbon` #171A20 | 3.61:1 | 3:1 | Pass |
| `surface-frost` composited over the canvas (#FFFFFF) | 4.82:1 | 3:1 | Pass |
| `overlay-modal` composited over the canvas (#ACACAC) | 2.12:1 | 3:1 | **Fail at mid grey.** Over the modal scrim — and over full-bleed photography, which has no measurable colour — the ring is two-tone: 2px `{colors.focus}` with a 1px outer edge in `{colors.ink-on-image}` (#FFFFFF). The two bands separate at 4.82:1, so the pair reads on any ground |

One ring serves the whole file rather than a light/dark pair: the blue clears 3:1 on all three real surfaces, and SPEC prefers the simpler answer where it works. A white-canvas brand whose only chromatic value is this blue has nothing else to build a ring from.

### Minimum tap target
The source records primary CTAs at 200px × 40px, nav buttons at a 32px minimum height with `{spacing.fine}` `{spacing.md}` padding, and carousel arrows at roughly 44px square. Two of those are **below the 44×44px minimum as documented**: the 40px CTA height and the 32px nav button. The source's own claim that 200×40px is "well above 44×44px" is wrong on the vertical axis. This is a document, not a rendered page, so nothing here was measured as rendered — these are the source's own figures.

### Reduced motion
`@media (prefers-reduced-motion: reduce)` removes every translate and scale, stops the hero carousel's auto-advance and its slow scale ambience, and drops the list stagger. Opacity fades and the extracted colour crossfades remain, capped at `{motion.duration-reduced}` (150ms) — below the extracted 330ms and below the Cinematic profile's own `{motion.duration-fast}`. The focus ring is never animated away.

## Do's and Don'ts

### Do
- Let photography dominate every screen — the product IS the design
- Use Electric Blue (`{colors.accent}`) exclusively for primary CTAs — never for decorative purposes
- Maintain viewport-height sections for major content blocks — one message per screen
- Keep typography at weight 400-500 only — no bold, no light, no extremes
- Use `{rounded.button}` border-radius for all interactive elements — precision over playfulness
- Trust whitespace as a luxury signal — never fill available space just because it's empty
- Keep all interaction-state transitions at `{motion.duration-extracted-state}` (0.33s) — consistency in motion is as important as consistency in color
- Use transparent PNG vehicle imagery on white backgrounds for product showcases
- Center CTAs horizontally below model names — the vertical rhythm is model → subtitle → buttons
- Maintain the Display/Text font split — Display for hero-scale text only, Text for everything else
- Reach for `{colors.text-dim}` whenever a muted element has to stay perceivable — it is the only muted tone in the palette that clears AA

### Don't
- Add shadows to any element — elevation through shadow contradicts the flat, gallery aesthetic
- Use more than one chromatic color besides the blue CTA — the palette is intentionally monochrome-plus-one
- Apply gradients, patterns, or decorative backgrounds to surfaces — white and photography are the only backgrounds
- Use text larger than 40px on the web — the typography is deliberately restrained even at hero scale
- Add borders to cards or containers — separation is achieved through spacing, not lines
- Use uppercase text transforms — Tesla's confidence is expressed through lowercase calm
- Introduce rounded-pill buttons or large border-radii — the `{rounded.button}` radius is deliberate and precise
- Override the Universal Sans family with other typefaces — cross-platform consistency is a core brand value
- Add hover animations with scale/translate transforms — Tesla's interactions are color-only (background and border transitions)
- Clutter the viewport with multiple CTAs — every screen should have at most two action buttons
- Rely on `{colors.border}` or `{colors.border-strong}` as the only boundary of a control — neither reaches 3:1 on any surface in this file
- Place white or blue type over photography without checking the image behind it — the system provides no scrim and no overlay gradient

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single-column layout, hamburger nav replaces horizontal labels, hero text scales to ~28px, CTA buttons stack vertically, category cards become full-width |
| Tablet | 768-1024px | 2-column nav panel, hero maintains full-viewport height, CTAs remain side-by-side, reduced horizontal padding |
| Desktop | 1024-1440px | Full horizontal nav, 3-column vehicle grid in dropdown, hero at 40px, side-by-side CTAs at 200px/160px width |
| Large Desktop | >1440px | Content remains centered, hero photography scales to fill wider viewports, max-width container for nav panel content |

### Touch Targets
- Primary CTA buttons: 200px × 40px — 40px is **below** the 44×44px WCAG target size; see Accessibility
- Nav buttons: minimum 32px height with `{spacing.fine}` `{spacing.md}` padding — also below 44px
- Carousel arrows: ~44px square white semi-transparent buttons at viewport edges
- Text links ("Learn", "Order"): 14px text with adequate line-height spacing for touch

### Collapsing Strategy
- **Navigation**: Horizontal category buttons (Vehicles, Energy, Charging, Discover, Shop) collapse to a hamburger/drawer menu on mobile
- **Hero CTA pair**: Side-by-side buttons on desktop stack vertically on mobile
- **Category cards**: 2-up horizontal layout collapses to single-column full-width on mobile
- **Vehicle grid**: 3-column grid in desktop nav panel becomes 2-column on tablet, single-column on mobile
- **Spacing**: Section vertical padding remains generous (viewport-height sections) but horizontal padding reduces

### Image Behavior
- Hero images are fully responsive and fill the entire viewport at every breakpoint
- Vehicle carousel images use `object-fit: cover` to maintain cinematic composition across widths
- Transparent PNG vehicle images in the nav panel scale proportionally within their grid cells
- Category card images maintain their landscape ratio and clip via `overflow: hidden` with border-radius

## Known Gaps

Everything here is absent from, or unverifiable in, the source document. Nothing in this file was invented to fill one of these holes.

**Lost in the legacy-format conversion.** This file carried no frontmatter token block and used numbered headings (`## 1. Visual Theme & Atmosphere` and so on); every token above was built only from hexes, type values and component descriptions already present in its prose.
- **Token names.** The source named colours only in prose ("Carbon Dark", "Pewter", "Silver Fog"), so every token key above is a new name mapped onto an extracted hex. Whatever names Tesla itself uses are unknown.
- **One hex, two jobs.** `{colors.ink}` and `{colors.surface-carbon}` are the same value, #171A20, because the source describes Carbon Dark as both the primary text colour and a dark surface. Whether the real design system treats that as one token or two is unknown. The same applies to #FFFFFF, split here into `{colors.canvas}`, `{colors.on-accent}` and `{colors.ink-on-image}` by job.
- **Component property coverage.** Most component descriptions gave a background and a text colour but no gap, border width, icon size or hover value; those keys are absent rather than guessed. "Hover: subtle darkening of blue background" records no hover hex, so there is no `accent-hover` token.
- **State coverage.** The source documents hover for several components, active for two, a focus *mechanism* with no colour, disabled only as a text tone, loading only as lazy-load behaviour, and error only as "browser defaults". `pressed` and `selected` appear nowhere — including for the carousel dots, where a current-slide treatment must exist on the real site and is simply not described. Both are left unfilled, and the lost point is accepted.
- **No shadow geometry.** The `shadow:` group carries only the three alpha values the prose states — `rgba(0,0,0,0)`, the 2px inset at zero alpha, and `rgba(0,0,0,0.05)`. No offset, blur or spread is recorded for the 0.05 hint, so it is a colour rather than a usable shadow.

**Values genuinely missing from the source:**
- `{typography.category-label}` has no recorded line height (the source table shows "—"), and its 16px size is marked "(est.)" in the source itself, so it is an estimate carried forward, not a measurement.
- `{typography.promo-text}` records a 22px size against a 20px line height (0.91) — a line height below 1.0 at that size. It is carried as extracted and is most likely a measurement artefact.
- No focus ring colour is extracted. The 3px transparent border and the zero-alpha inset shadow prove a focus treatment exists; its colour appears nowhere in the source. `{colors.focus}` is prescribed from the brand's own blue.
- The "Schedule a Drive Today" CTA is described as having "a teal/blue icon accent". No hex is given, and a teal would be a second chromatic value in a system whose first rule is that it has only one. No token was created for it.
- The chat bar and the chat input are described as having a "subtle border" with no hex. The guidance to draw that boundary in `{colors.text-dim}` is prescribed, not extracted, and the extracted hairlines keep their own bindings.
- Inputs are said to inherit their border "from browser defaults", so no input border width, style or colour exists in this system at all.
- Error, success and warning are stated to follow "standard browser defaults", so the system defines no semantic palette. There are no `success`, `warning` or `error` colour tokens because there are no values to carry.
- The max width of ~1383px is an odd measurement with no stated container token, and the spacing value 21.44px is likewise a measured artefact rather than a step on the 8px scale. Both are carried as recorded; the real ladder behind them is unknown.
- Nav button hover is "subtle background highlight" with no value, and the Level 3 shadow hint `rgba(0,0,0,0.05)` is "minimal shadow hints on rare hover states" with no element named. Which component, if any, uses either is unknown.
- **The motion values are prescribed**, with two exceptions: the 0.33s / 0.25s transition durations and `cubic-bezier(0.5, 0, 0, 0.75)` are extracted from the source's own component CSS. Everything else — the rest of the ladder, the other curves, the stagger, every piece of choreography — was never measured on tesla.com and was assigned from brand category.
- **Not measurable from a document:** overlap, horizontal overflow, clipping, rendered tap-target size, frame rate and layout shift. The tap-target figures above are the source's own numbers rather than rendered measurements — and two of them fall below 44px as written.

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: "Electric Blue (#3E6AE1)"
- Background: "Pure White (#FFFFFF)"
- Heading text: "Carbon Dark (#171A20)"
- Body text: "Graphite (#393C41)"
- Tertiary text: "Pewter (#5C5E62)"
- Placeholder: "Silver Fog (#8E8E8E)"
- Alternate surface: "Light Ash (#F4F4F4)"
- Dark surface: "Carbon Dark (#171A20)"

### Example Component Prompts
- "Create a hero section with a full-viewport background image, centered 'Model Y' title in Universal Sans Display at 40px weight 500 in white, a subtitle line below, and two buttons side by side: a primary Electric Blue (#3E6AE1) 'Order Now' button and a secondary white 'View Inventory' button, both with 4px border-radius and 40px height"
- "Design a navigation bar with a spaced-letter wordmark on the left, five text buttons (14px, weight 500, Carbon Dark #171A20) centered, and three icon buttons on the right, all on a white background with no shadow or border"
- "Build a vehicle card grid with 3 columns, each card showing a transparent-background car image above a model name (17px, weight 500, Carbon Dark) and two text links (14px, weight 400, Pewter #5C5E62) labeled 'Learn' and 'Order', on a pure white surface with no borders or shadows"
- "Create a category card with full-bleed landscape photography, 12px border-radius, overflow hidden, and a white text label ('Sport Sedan') positioned in the top-left corner with no overlay gradient"
- "Design a persistent bottom bar with a chat input ('Ask a Question' placeholder), a send icon, and a secondary CTA ('Schedule a Drive Today') with a teal icon, anchored to the viewport bottom on a white background"

### Iteration Guide
When refining existing screens generated with this design system:
1. Focus on ONE component at a time — Tesla's system is so minimal that each element must be pixel-perfect
2. Reference specific color names and hex codes from this document — there are only 6-7 colors in the entire system
3. Use natural language descriptions, not CSS values — "barely rounded corners" not "border-radius: 4px"
4. Describe the desired "feel" alongside specific measurements — "gallery-like silence between sections" communicates the whitespace philosophy better than "margin-bottom: 100vh"
5. Always verify that photography is doing the emotional heavy-lifting — if the UI itself feels "designed," it's too much
