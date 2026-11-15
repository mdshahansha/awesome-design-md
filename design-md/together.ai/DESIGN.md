---
version: alpha
name: Together-AI-Inspired-design-analysis
description: An inspired interpretation of Together AI's design language — an AI infrastructure platform whose surface alternates between near-black hero bands (with a three-color orange-magenta-periwinkle gradient as the single piece of brand chrome) and bright white research / pricing / docs bands, knit together by a custom display sans and an uppercase mono eyebrow face.

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  ink: "#000000"
  body: "#959494"
  hairline: "#ebebeb"
  hairline-on-dark: "#26263a"
  canvas: "#ffffff"
  canvas-dark: "#010120"
  surface-dark-soft: "#313641"
  on-dark: "#ffffff"
  focus: "#000000"
  focus-on-dark: "#ffffff"
  accent-orange: "#fc4c02"
  accent-magenta: "#ef2cc1"
  accent-periwinkle: "#bdbbff"
  accent-mint: "#c8f6f9"

typography:
  display-xxl:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 64px
    fontWeight: 500
    lineHeight: 70.4px
    letterSpacing: -1.92px
  display-xl:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 40px
    fontWeight: 500
    lineHeight: 48px
    letterSpacing: -0.8px
  display-lg:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 28px
    fontWeight: 500
    lineHeight: 32.2px
    letterSpacing: -0.42px
  display-md:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 22px
    fontWeight: 500
    lineHeight: 25.3px
    letterSpacing: -0.22px
  body-lg:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 23.4px
    letterSpacing: -0.18px
  body-lg-strong:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 18px
    fontWeight: 500
    lineHeight: 23.4px
    letterSpacing: -0.18px
  body-md:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 20.8px
    letterSpacing: -0.16px
  body-md-strong:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 20.8px
    letterSpacing: -0.16px
  caption:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 19.6px
  caption-strong:
    fontFamily: The Future, Inter, Helvetica Neue, Arial, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 19.6px
  mono-caps-button:
    fontFamily: PP Neue Montreal Mono, ui-monospace, SF Mono, Menlo, monospace
    fontSize: 16px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.08px
  mono-caps-eyebrow:
    fontFamily: PP Neue Montreal Mono, ui-monospace, SF Mono, Menlo, monospace
    fontSize: 11px
    fontWeight: 500
    lineHeight: 11px
    letterSpacing: 0.55px
  mono-caps-label:
    fontFamily: PP Neue Montreal Mono, ui-monospace, SF Mono, Menlo, monospace
    fontSize: 11px
    fontWeight: 500
    lineHeight: 15.4px
    letterSpacing: 0.055px
  mono-caption:
    fontFamily: PP Neue Montreal Mono, ui-monospace, SF Mono, Menlo, monospace
    fontSize: 10px
    fontWeight: 400
    lineHeight: 14px
    letterSpacing: 0.05px

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

rounded:
  none: 0px
  xs: 3.25px
  sm: 4px
  md: 8px
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
  4xl: 44px
  5xl: 48px
  6xl: 55.2px
  section: 80px

components:
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} {spacing.3xl}"
  nav-link:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.2xl}"
  button-secondary-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.2xl}"
  button-secondary-white:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.2xl}"
  button-ghost-on-dark:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "rgba(0, 0, 0, 0.08)"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.xs}"
  button-icon-circular:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "rgba(0, 0, 0, 0.08)"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  badge-neutral:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "rgba(0, 0, 0, 0.08)"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-subtle-on-dark:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  hero-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.section} {spacing.3xl}"
  research-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.3xl}"
  feature-tab-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.2xl}"
  pricing-sub-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  stats-card-tinted:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  research-card:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    borderColor: "rgba(255, 255, 255, 0.12)"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  article-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  code-editor-mockup:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.mono-caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  data-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "rgba(0, 0, 0, 0.08)"
    typography: "{typography.body-md}"
    padding: "{spacing.md} {spacing.lg}"
  data-table-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.mono-caps-eyebrow}"
    padding: "{spacing.md} {spacing.lg}"
  toggle-pill-group:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.3xl}"
  footer-wordmark-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.display-xxl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Mirrors article-card chrome on canvas-soft surface with a hairline border."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "rgba(0, 0, 0, 0.08)"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  ex-pricing-tier-featured:
    description: "Featured tier — polarity-flipped to canvas-dark with white text."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  ex-product-selector:
    description: "What's Included summary card — repurposed for the brand's GPU / inference packaging tiers."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  ex-cart-drawer:
    description: "Subscription summary — line items per add-on (NOT a literal e-commerce cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row. Active state uses brand primary as a left-edge indicator bar."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Mirrors the brand's pricing-page table. Header uses mono-caps-eyebrow uppercase; body uses body-md."
    headerBackground: "{colors.hairline}"
    headerTypography: "{typography.mono-caps-eyebrow}"
    bodyTypography: "{typography.body-md}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Mirrors article-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as article-card; relies on tinted scrim instead of card shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame. Generous padding on canvas-soft surface."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.5xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — flat-cornered article-card chrome with a soft brand-tinted drop shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-md}"

---


## Overview

Together AI is an AI cloud-infrastructure platform — model inference, GPU clusters, fine-tuning, all the plumbing that makes "the AI native cloud" deliverable to a developer team — and the brand's web surface signals exactly that posture: a near-black hero on top, a long ribbon of white technical content in the middle, and a single recurring piece of brand chrome — a three-color orange-magenta-periwinkle gradient ribbon — that does the entire job of "we are not just another grey enterprise SaaS." There is no other illustration system. The gradient is the brand.

Type is the second decisive voice. Two faces carry every page: a custom geometric display sans (extracted as `The Future`) for headlines and body, set at weight 500 with tight, slightly-negative letter-spacing so 64-pixel hero type feels poured rather than typed; and an uppercase monospace eyebrow (`PP Neue Montreal Mono`) that labels every section, every button, and every cell header. Headlines are sentence-case; everything technical is uppercase mono. That contrast is the brand's tonal joke — the platform is serious enough to use a monospace label, modern enough to not put the headline in it.

Surfaces alternate aggressively: a `{colors.canvas-dark}` (`#010120`) band for hero / research / "Grounded in cutting-edge research" — followed by `{colors.canvas}` (white) for product, pricing, and testimonials, with `{colors.hairline}` reserved for table-header rows and toggle backgrounds. Pastel `{colors.accent-mint}` tinted stat tiles break up the white middle. Cards are universally lightly rounded (`{rounded.sm}` 4 px) with hairline borders — never floating with shadows.

**Key Characteristics:**
- A single black `{colors.primary}` CTA pill carries every conversion target across pricing, footer, sign-in. The mint `{colors.accent-mint}` and white pill variants are reserved for hero contexts only.
- A three-color brand gradient (`{colors.accent-orange}` → `{colors.accent-magenta}` → `{colors.accent-periwinkle}`) is the entire decorative system — used as the hero ribbon graphic and never reduced to a swatch elsewhere.
- All-caps mono eyebrows and button labels in `{typography.mono-caps-eyebrow}` / `{typography.mono-caps-button}` everywhere — section titles, model row headers, "ON-DEMAND" labels in pricing tables.
- Lightly rounded card chrome at `{rounded.sm}` 4 px; one off `{rounded.xs}` 3.25 px appears inside pricing-tab pills as a tighter system; `{rounded.full}` only for the floating chat-launcher orb.
- Dual surface mode — alternating `{colors.canvas-dark}` and `{colors.canvas}` bands; no in-between greys. The single soft surface `{colors.hairline}` exists only to mark table-header rows.
- A massive `together.ai` wordmark banner at the very bottom of every page, set in `{typography.display-xxl}` and tinted nearly-into-the-canvas (`{colors.hairline}`), as a "we are here" sign-off that doubles as a footer separator.

## Colors

### Brand & Accent
- **Ink Black** (`{colors.primary}` — `#000000`): The single primary CTA color. Black pill carries "Sign in", "Contact sales", "Get started now", every footer CTA.
- **Brand Orange** (`{colors.accent-orange}` — `#fc4c02`): One leg of the three-color brand gradient. Appears in the hero ribbon graphic; never used as a UI fill on its own.
- **Brand Magenta** (`{colors.accent-magenta}` — `#ef2cc1`): The second leg of the gradient.
- **Brand Periwinkle** (`{colors.accent-periwinkle}` — `#bdbbff`): The third leg of the gradient; also used as a soft fill for some stat tiles.
- **Brand Mint** (`{colors.accent-mint}` — `#c8f6f9`): A pastel cyan that lives outside the gradient — used for hero secondary-CTA pills and `stats-card-tinted` tiles.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): The default product / pricing / docs background.
- **Hairline / Canvas Soft** (`{colors.hairline}` — `#ebebeb`): The brand's single soft surface tone and its 1 px divider, one and the same value — data-table header rows, toggle-pill rails, dividers between table rows, card and badge chrome. Pre-blended from the brand's translucent-black 8 % rule (`rgba(0, 0, 0, 0.08)` over `{colors.canvas}` composites to exactly `#ebebeb`), which is why the components block still carries the literal. As a boundary it measures **1.19:1** against `{colors.canvas}` — below the 3:1 WCAG 1.4.11 threshold. It is frozen and decorative; see Accessibility.
- **Canvas Dark** (`{colors.canvas-dark}` — `#010120`): The brand's dark hero surface; appears on `hero-band-dark` and `research-band-dark`.
- **Hairline on Dark** (`{colors.hairline-on-dark}` — `#26263a`): 1 px dividers and badge borders on `{colors.canvas-dark}` surfaces; pre-blended from the brand's translucent-white-on-dark hairline. Measures 1.38:1 against `{colors.canvas-dark}` — the dark-band mirror of the same frozen failure.
- **Surface Dark Soft** (`{colors.surface-dark-soft}` — `#313641`): A slightly lighter dark fill used inside dark-band cards and ghost buttons.

### Text
- **Ink** (`{colors.ink}` — `#000000`): Every heading and body paragraph on light surfaces.
- **Body** (`{colors.body}` — `#959494`): Secondary / muted text — captions, table cell secondary values, table-header labels, footer link text. Pre-blended from the brand's translucent-black 42 % body color. This is the brand's **only** muted ink: it is the `text-dim` role under a brand-specific name, not a missing role. It measures **3.03:1** on `{colors.canvas}`, below the 4.5:1 AA body-text threshold — frozen, disclosed in Accessibility.
- **On Dark** (`{colors.on-dark}` — `#ffffff`): All text on `{colors.canvas-dark}` surfaces.

### Focus
- **Focus Ring** (`{colors.focus}` — `#000000`): The focus indicator on light grounds. It reuses the brand's own ink (`{colors.primary}` / `{colors.ink}`) rather than introducing a new colour — Together AI's signal colour *is* its ink, and the three-stop gradient is explicitly never reduced to a single swatch, so a chromatic ring would break the brand's own rule. 21:1 on `{colors.canvas}`.
- **Focus Ring on Dark** (`{colors.focus-on-dark}` — `#ffffff`): The same indicator on `{colors.canvas-dark}` and `{colors.surface-dark-soft}` grounds, reusing `{colors.on-dark}`. 20.46:1 and 12.11:1.
- Both rings are 2 px and drawn **outside** the control with a 2 px offset in the ground colour, so a black ring never merges into the black `button-primary` fill and is measured against the surface behind the control (WCAG 2.2 Focus Appearance). Prescribed, not extracted.

### Semantic
The brand does not maintain a separate error / success palette in its public surface; validation cues use the primary black or the brand gradient depending on context. No explicit error red, success green, or warning yellow is documented here — adopting framework defaults is appropriate.

### Brand Gradient
The brand's signature decoration is a three-stop gradient drawn from `{colors.accent-orange}` → `{colors.accent-magenta}` → `{colors.accent-periwinkle}`, applied as the only piece of decorative chrome (the hero ribbon graphic). Treat the gradient as one unified object — do not crop it down to a single colour, do not reorder the stops, and do not add a fourth stop. Used at large scale; never miniaturised to icon size.

## Typography

### Font Family
Two families carry the entire system:

1. **A custom geometric display sans** (extracted as `The Future`) for every headline, lead paragraph, body, button label that is not uppercase, and inline link. Weights 400 and 500 are the working pair; the face never appears in bold (700) or heavier. Tight negative letter-spacing (`-1.92 px` at 64 px display, `-0.16 px` at 16 px body) gives the face its slightly-condensed, poured-on-the-page feel.
2. **An uppercase mono caption face** (extracted as `PP Neue Montreal Mono`) for every eyebrow, button label, table-header cell, and pricing-table tab. Weight 500 at 11–16 px; always uppercase; positive letter-spacing (`0.05 – 0.55 px`). The mono carries the brand's technical voice — every label that says "PRICING", "INFERENCE", "MODEL", "GPU", "GA-DEC '25" is set in this face.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 64px | 500 | 70.4px | -1.92px | Hero headline ("Build what's next on the AI Native Cloud"). |
| `{typography.display-xl}` | 40px | 500 | 48px | -0.8px | Section headlines ("The Together AI Platform", "Start building on Together AI"). |
| `{typography.display-lg}` | 28px | 500 | 32.2px | -0.42px | Sub-section headlines and stat-tile big numbers. |
| `{typography.display-md}` | 22px | 500 | 25.3px | -0.22px | Card titles, research-card headings. |
| `{typography.body-lg}` | 18px | 400 | 23.4px | -0.18px | Lead paragraphs under section headlines. |
| `{typography.body-lg-strong}` | 18px | 500 | 23.4px | -0.18px | Emphasis runs inside lead paragraphs. |
| `{typography.body-md}` | 16px | 400 | 20.8px | -0.16px | Default body paragraph. |
| `{typography.body-md-strong}` | 16px | 500 | 20.8px | -0.16px | Bolded inline body. |
| `{typography.caption}` | 14px | 400 | 19.6px | 0 | Fine print, footer secondary text. |
| `{typography.caption-strong}` | 14px | 500 | 19.6px | 0 | Bolded captions. |
| `{typography.mono-caps-button}` | 16px | 500 | 16px | 0.08px | Primary button labels — uppercase, mono. |
| `{typography.mono-caps-eyebrow}` | 11px | 500 | 11px | 0.55px | Section eyebrows, table-header cell labels. |
| `{typography.mono-caps-label}` | 11px | 500 | 15.4px | 0.055px | Inline tag labels inside text contexts. |
| `{typography.mono-caption}` | 10px | 400 | 14px | 0.05px | Mono fine print (inside code editor mockup). |

### Principles
- **Two-face contrast is the voice.** Display sans for narrative; uppercase mono for technical labels. Never let the mono carry a paragraph; never let the display sans carry a button label.
- **Negative letter-spacing only on the display sans.** The mono face uses small positive tracking; reversing this is wrong.
- **Headlines stay sentence-case.** Every uppercase moment belongs to the mono face. Mixing all-caps display would muddy the contrast.

### Note on Font Substitutes
The two primary faces are proprietary. Open-source substitutes:
- **Display sans** — *Inter* (400 / 500) with `font-feature-settings: "ss01"` enabled comes closest; tighten letter-spacing by ~0.6 % at display sizes to land on the brand's compressed feel. *Geist* is the second-best option but reads slightly wider.
- **Uppercase mono eyebrow** — *JetBrains Mono* or *Geist Mono* (weight 500) at 11 px with `text-transform: uppercase` matches the brand's voice once tracking is bumped to `0.04em`.

## Layout

### Spacing System
- **Base unit**: 4 px. Almost every captured value is a multiple of 4, with two exceptions (7.2 px, 55.2 px) that are gap-multiplier derivatives, not layout decisions.
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 20 px · `{spacing.2xl}` 24 px · `{spacing.3xl}` 32 px · `{spacing.4xl}` 44 px · `{spacing.5xl}` 48 px · `{spacing.6xl}` 55.2 px · `{spacing.section}` 80 px.
- **Section padding**: marketing bands use `{spacing.section}` 80 px top/bottom on desktop. The hero and the "research" dark band keep the 80 px rhythm; pricing tables tighten to `{spacing.5xl}` to keep dense data legible.
- **Card interior padding**: research cards and testimonial cards sit at `{spacing.2xl}` 24 px interior; the stat-card tiles use `{spacing.3xl}` 32 px to give the big number breathing room.
- **Inline gap**: button + nav rows use `{spacing.md}` 12 px between siblings; chip groups use `{spacing.sm}` 8 px.

### Grid & Container
- **Max width**: ~1280 px desktop container; nothing rendered above that. Content centres with horizontal gutters of `{spacing.3xl}` 32 px on desktop, `{spacing.lg}` 16 px on mobile.
- **Column patterns**:
  - Research / testimonial grids: 3-up at desktop, 1-up at mobile.
  - Stats tile grid: 3-up at desktop, 1-up at mobile.
  - Article-card grid: 2-up at desktop, 1-up at mobile.
  - Pricing data table: full-width, model rows stack on mobile.
  - Hero: 50 / 50 split (headline left, ribbon graphic right) at desktop; stacked at mobile with graphic above.

### Whitespace Philosophy
Surface contrast does most of the separation. A dark band ends → 80 px of breathing room → next light band begins. Inside a band, headline and lead paragraph hug close (`{spacing.lg}` 16 px between them), then a wider gap before the supporting visual or CTA cluster. Inside pricing data tables, the brand keeps rows tight (`{spacing.md}` 12 px vertical) — the table reads more like a sheet than a marketing component.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Most cards on light surfaces lean on hairline borders, not shadow. |
| Level 1 — Hairline | 1 px solid `{colors.hairline}` on `{colors.canvas}` cards. | Testimonial cards, article cards, data-table rows. |
| Level 2 — Hairline on Dark | 1 px solid `{colors.hairline-on-dark}` on `{colors.canvas-dark}` cards. | Research-band cards, on-dark badges. |
| Level 3 — Soft Drop | `rgba(1, 1, 32, 0.1) 0px 4px 10px 0px` — a barely-perceptible shadow tinted with the brand's dark-navy. | Floating elements (the chat-launcher orb, sticky-bottom nav row when one appears). |

### Decorative Depth
- **Gradient ribbon as depth**: the hero's three-stop gradient ribbon is the page's only true atmospheric effect. It loops through layered translucent shapes that imply depth without leaving the brand palette.
- **Code editor mockup as section-depth break**: a dark code-editor surface inside the otherwise-white product band acts as a one-step lift, mirroring the hero's polarity flip.
- **Wordmark banner as terminal depth**: the giant `together.ai` letters at the bottom are technically inside `{colors.canvas}` but tinted toward `{colors.hairline}` so they read as a faint stencil, giving the page a final "you have arrived" sign-off.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Hero / research full-bleed bands; the footer wordmark banner. |
| `{rounded.xs}` | 3.25px | The pricing page's slightly tighter sub-tab and outline button. |
| `{rounded.sm}` | 4px | The brand's canonical radius — buttons, badges, cards, data-table rows, stat tiles. |
| `{rounded.md}` | 8px | Feature-tab pills inside the "Full-stack cloud" section, larger pricing-tab containers. |
| `{rounded.full}` | 9999px | The floating chat-launcher orb (`button-icon-circular`). The only fully-pill shape in the system. |

### Photography Geometry
- **Hero ribbon**: SVG gradient, free-form; no aspect-ratio constraint.
- **Customer logos**: vector, rendered grayscale at consistent height (~24 px) in a wrapping flex row.
- **Testimonial portraits**: 1:1 square crop with hard-edge corners — no avatar pill.
- **Article thumbnails**: 16:9 with `{rounded.sm}` 4 px top-corner radius on the image only; card chrome stays square.

## Components

### Buttons

**`button-primary`** — the black pill that carries every primary CTA.
- Background `{colors.primary}`, text `{colors.on-primary}`, label set in `{typography.mono-caps-button}` (uppercase mono, 16 px / 500 / 0.08 px tracking), shape `{rounded.sm}` 4 px, padding `{spacing.xs} {spacing.2xl}`. No shadow.
- States: default · hover (fill lightens to `{colors.surface-dark-soft}`) · focus-visible (2 px `{colors.focus}` ring, 2 px `{colors.canvas}` offset) · pressed (fill `{colors.surface-dark-soft}`, no scale) · disabled (fill `{colors.hairline}`, label `{colors.body}`) · loading (label swaps for a mono-caps "…" marker; width held) · error (not applicable — the button never carries validation state). Paint-only: the brand is near-monochrome and a scale pop would contradict it.

**`button-secondary-mint`** — the hero secondary CTA pill.
- Background `{colors.accent-mint}`, text `{colors.ink}`, same typography and shape as `button-primary`. Only appears in hero contexts.
- States: default · hover (fill deepens ~6 % toward `{colors.accent-periwinkle}`) · focus-visible (`{colors.focus}` ring, offset in the surrounding band colour) · pressed (opacity 0.9) · disabled (fill `{colors.hairline}`, label `{colors.body}`). No loading, selected or error state.

**`button-secondary-white`** — the white pill paired with `button-secondary-mint` inside the hero.
- Background `{colors.canvas}`, text `{colors.ink}`, same typography and shape. Always sits adjacent to the mint or primary button.
- States: default · hover (fill `{colors.hairline}`) · focus-visible (`{colors.focus-on-dark}` ring — it sits on the dark hero band) · pressed (opacity 0.9) · disabled (label `{colors.body}`). No loading, selected or error state.

**`button-ghost-on-dark`** — the translucent button used on dark hero / research surfaces.
- Background `{colors.surface-dark-soft}`, text `{colors.on-dark}`, shape `{rounded.sm}` 4 px. Used for "Read more" / "Watch the announcement" affordances on dark bands.
- States: default · hover (fill lightens ~8 %) · focus-visible (2 px `{colors.focus-on-dark}` ring, 2 px `{colors.canvas-dark}` offset) · pressed (opacity 0.9) · disabled (label drops to `{colors.body}`) · loading (mono-caps "…" marker). No selected or error state.

**`button-outline`** — the white-on-white outline button used inside pricing pages and feature toggles.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` border, shape `{rounded.xs}` 3.25 px. The extracted border is `rgba(0, 0, 0, 0.08)` → `#ebebeb`, **1.19:1** on `{colors.canvas}`: it is the control's only boundary and it fails WCAG 1.4.11. Where this button must be independently discoverable, draw the boundary in `{colors.body}` (`#959494`, 3.03:1) instead; see Accessibility.
- States: default · hover (fill `{colors.hairline}`) · focus-visible (`{colors.focus}` ring) · pressed (fill `{colors.hairline}`, border `{colors.body}`) · disabled (label and border `{colors.body}`) · selected (fill `{colors.primary}`, label `{colors.on-primary}` — used inside toggle rows). No loading or error state.

**`button-icon-circular`** — the floating chat-launcher orb in the bottom-right of every page.
- Background `{colors.primary}`, white icon, shape `{rounded.full}`. The only fully-pill shape in the system.
- States: default · hover (fill lightens to `{colors.surface-dark-soft}`) · focus-visible (2 px `{colors.focus}` ring, 2 px offset in whichever band it floats over) · pressed (opacity 0.9) · loading (indeterminate ring, see Motion & Animation). No disabled, selected or error state — the launcher is always available.

### Cards & Containers

**`research-card`** — the 4-up grid card on the dark "Grounded in cutting-edge research" band.
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, 1 px solid `{colors.hairline-on-dark}` border, padding `{spacing.2xl}`, shape `{rounded.sm}` 4 px. Inside: mono eyebrow tag + display headline + body paragraph.
- States: default · hover (border lifts to `{colors.surface-dark-soft}`) · focus-visible (`{colors.focus-on-dark}` ring, card is a link target) · pressed (opacity 0.9) · loading (skeleton block in `{colors.surface-dark-soft}`). No disabled, selected or error state — it is a static content card.

**`testimonial-card`** — the 3-up "AI natives build on Together AI" card.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.2xl}`, shape `{rounded.sm}` 4 px. Inside: 1:1 portrait crop + display-md name + body quote + mono caption stat row.
- States: default and loading (skeleton blocks in `{colors.hairline}`) only. Genuinely a two-state component: it is not interactive, carries no link, and so has no hover, focus-visible, pressed, disabled, selected or error state.

**`article-card`** — the 2-up "What's new at Together AI" article card.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.2xl}`, shape `{rounded.sm}` 4 px. Inside: 16:9 image at top + mono eyebrow tag + display-md title + body summary + mono caption byline.
- States: default · hover (title underlines; card border darkens to `{colors.body}`) · focus-visible (`{colors.focus}` ring around the whole card, 2 px offset) · pressed (opacity 0.9) · loading (skeleton). No disabled, selected or error state.

**`code-editor-mockup`** — the dark code-preview surface inside the product band.
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, body in `{typography.mono-caption}`, padding `{spacing.2xl}`, shape `{rounded.sm}` 4 px. Window chrome stays minimal — no traffic-light dots, no title bar.
- States: default · loading (typing reveal, see Motion & Animation) · selected (the tab row above it marks the active language) · error (a mono-caps line in `{colors.accent-orange}` when a sample fails to load). No hover, focus-visible, pressed or disabled state — it is a display surface.

**`stats-card-tinted`** — the pastel-tinted stat tile (mint, peach, periwinkle) on the white middle band.
- Background `{colors.accent-mint}` (or sibling accent tints), text `{colors.ink}`, big number in `{typography.display-xl}` + label in `{typography.mono-caps-eyebrow}`, padding `{spacing.3xl}`, shape `{rounded.sm}` 4 px. Ink on mint measures 18.01:1; ink on periwinkle 11.72:1.
- States: default and loading (number replaced by a `{colors.canvas}` skeleton bar) only — a genuinely two-state display tile, with no hover, focus-visible, pressed, disabled, selected or error state.

### Inputs & Forms

**`text-input`** — the form input on the startup-accelerator application form.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` border, body set in `{typography.body-md}`, shape `{rounded.sm}` 4 px. That extracted border (`rgba(0, 0, 0, 0.08)` → `#ebebeb`) is the field's only boundary and measures **1.19:1** on `{colors.canvas}` — a real WCAG 1.4.11 failure in the live brand. The palette already owns a passing tone: draw the resting boundary in `{colors.body}` (`#959494`, **3.03:1**) and keep `{colors.hairline}` for decorative dividers.
- States: default · hover (border `{colors.body}`) · focus-visible (2 px `{colors.focus}` ring, 2 px `{colors.canvas}` offset, border `{colors.ink}`) · pressed/active (same as focus) · disabled (fill `{colors.hairline}`, text `{colors.body}`) · loading (field locked, mono-caps "…" in the trailing slot) · error (border and mono-caps helper text in `{colors.accent-orange}`, 3.4:1 on `{colors.canvas}` — boundary-legal, paired with a text message, never colour alone) · selected (text selection only). Shape, size and position never change between states.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas-dark}` on the hero band, switches to `{colors.canvas}` once the user scrolls past the hero. Text `{colors.on-dark}` on dark, `{colors.ink}` on white. Layout: logo left, link row centre, "Contact sales" + "Sign in" right.
- States: default · selected (the current section's link carries a 1 px underline) · loading (none — the nav is static chrome). Hover, focus-visible, pressed and disabled live on `nav-link`, not on the bar.

**`nav-link`** — the centred link row inside `nav-bar`.
- Text `{colors.on-dark}` (or `{colors.ink}` after scroll), set in `{typography.body-md}` 400 weight. Links separate with `{spacing.2xl}` 24 px between siblings. The link is declared against its own ground (`{colors.canvas-dark}`) in the components block, which is where it is drawn — 20.46:1.
- States: default · hover (opacity 0.7) · focus-visible (2 px `{colors.focus-on-dark}` ring on the dark bar, `{colors.focus}` after the scroll flip) · pressed (opacity 0.6) · disabled (not used) · selected (1 px underline in the current text colour). No loading or error state.

**`footer`** — the bottom 4-column nav.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.section} {spacing.3xl}`. Eyebrow labels in `{typography.mono-caps-eyebrow}`; link rows in `{typography.body-md}`.
- States: links carry default · hover (underline) · focus-visible (`{colors.focus}` ring) · pressed (opacity 0.7). The footer container itself is a two-state surface (default, loading) with no disabled, selected or error state.

### Signature Components

**`hero-band-dark`** — the dark navy hero that opens every product / marketing page.
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, padding `{spacing.section} {spacing.3xl}`. Headline in `{typography.display-xxl}` (sentence case, never all-caps). Eyebrow in `{typography.mono-caps-eyebrow}`. Two-column layout: headline + CTA cluster on left, gradient ribbon SVG on right. White on `{colors.canvas-dark}` is 20.46:1.
- States: default only; the band is a layout surface. Its contents carry their own states, and any focus ring drawn inside it uses `{colors.focus-on-dark}`.

**`research-band-dark`** — the dark navy band that hosts the "Grounded in cutting-edge research" 4-up card grid.
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, padding `{spacing.section} {spacing.3xl}`. Section headline in `{typography.display-xl}` followed by the `research-card` grid.
- States: default only, for the same reason as `hero-band-dark`.

**`feature-tab-pill`** — the tab pill row inside the "Full-stack cloud" section.
- Background `{colors.canvas}`, text `{colors.ink}`, label in `{typography.body-md-strong}`, padding `{spacing.md} {spacing.2xl}`, shape `{rounded.md}` 8 px. Tab group sits on `{colors.hairline}` rail.
- States: default (inactive pill is the rail colour) · hover (fill `{colors.canvas}` at 60 % travel-free opacity) · focus-visible (`{colors.focus}` ring, 2 px offset) · pressed (opacity 0.9) · selected (fill `{colors.canvas}`, label `{colors.ink}`, the indicator slides — see Motion & Animation) · disabled (label `{colors.body}`) · loading (panel below shows a skeleton). No error state.

**`pricing-sub-tab`** — the secondary tab row inside the pricing-page model table (TEXT / VISION / IMAGE / AUDIO / VIDEO).
- Background `{colors.canvas}`, text `{colors.ink}`, label in `{typography.body-md}`, padding `{spacing.sm} {spacing.lg}`, shape `{rounded.xs}` 3.25 px.
- States: default · hover (fill `{colors.hairline}`) · focus-visible (`{colors.focus}` ring) · pressed (opacity 0.9) · selected (fill `{colors.primary}`, label `{colors.on-primary}`, 21:1) · disabled (label `{colors.body}`) · loading (table below shows skeleton rows). No error state.

**`data-table-row`** — the model row inside the pricing serverless-inference table.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` bottom border, padding `{spacing.md} {spacing.lg}`. Inside: model icon + model name (display sans) + input cost cell + output cost cell. The row rule is decorative at 1.19:1; the row is never the only affordance for its content.
- States: default · hover (row fill `{colors.hairline}`) · focus-visible (`{colors.focus}` ring on the row's link target) · pressed (opacity 0.9) · selected (left-edge 2 px `{colors.primary}` indicator) · loading (skeleton cells) · disabled (model unavailable: text `{colors.body}`, exempt from the 4.5:1 threshold per WCAG) · error (mono-caps "UNAVAILABLE" tag in `{colors.accent-orange}` plus text, never colour alone).

**`data-table-header`** — the table header row.
- Background `{colors.hairline}`, text `{colors.body}`, set in `{typography.mono-caps-eyebrow}` (uppercase mono), padding `{spacing.md} {spacing.lg}`. Muted ink on the soft band measures **2.54:1** — the file's worst text pair, and an extracted one; see Accessibility.
- States: default · hover (sortable column shows a caret) · focus-visible (`{colors.focus}` ring on the sort control) · pressed (opacity 0.9) · selected (active sort column's label switches to `{colors.ink}`, 17.62:1). No disabled, loading or error state.

**`toggle-pill-group`** — the "Standard Pricing / Wholesale Pricing" segmented control above the fine-tuning table.
- Background `{colors.hairline}` rail, individual pills `{colors.canvas}` (inactive) or `{colors.primary}` (active), label in `{typography.mono-caps-button}`, shape `{rounded.sm}` 4 px, rail padding `{spacing.xs}`.
- States: default · hover (inactive pill fill `{colors.canvas}`) · focus-visible (`{colors.focus}` ring around the focused pill, 2 px offset so it never merges with the active black fill) · pressed (opacity 0.9) · selected/active (fill `{colors.primary}`, label `{colors.on-primary}`) · disabled (label `{colors.body}`) · loading (the table it controls shows skeleton rows). No error state.

**`badge-neutral`** — the inline tag pill on light surfaces.
- Background `{colors.canvas}`, text `{colors.ink}`, body in `{typography.body-md}`, 1 px solid `{colors.hairline}` border, padding `{spacing.xxs} {spacing.sm}`, shape `{rounded.sm}` 4 px. (The components block is authoritative here: the fill is `{colors.canvas}`, not the hairline tone; ink on canvas is 21:1.)
- States: default only, plus selected where a badge doubles as a filter chip (fill `{colors.primary}`, label `{colors.on-primary}`). A static tag has no hover, focus-visible, pressed, disabled, loading or error state.

**`badge-subtle-on-dark`** — the inline tag pill on dark hero / research surfaces.
- Background `{colors.surface-dark-soft}`, text `{colors.on-dark}`, body in `{typography.body-md}`, padding `{spacing.xxs} {spacing.sm}`, shape `{rounded.sm}` 4 px. 12.11:1.
- States: default only — a static tag, with no hover, focus-visible, pressed, disabled, loading, selected or error state.

**`footer-wordmark-banner`** — the massive `together.ai` wordmark at the bottom of every page.
- Background `{colors.canvas}`, wordmark colour `{colors.hairline}` (faint stencil tint), set in `{typography.display-xxl}` scaled fluidly to the viewport width. Edge-to-edge, square corners. Acts as the final page sign-off.
- The wordmark is **decoration, not text**: at 1.19:1 it is deliberately almost invisible. It must be `aria-hidden` and the accessible site name must come from the footer's own markup, never from this banner.
- States: default only — one state, by design.

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


## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or keyframe was extracted from together.ai; the values below are the shared **Crisp** profile (SPEC section 5), chosen because this is developer-facing AI-cloud infrastructure — a console, a pricing table and a docs ribbon, where a state change should read as already done. Every value is referenced as a `{motion.*}` token so this file stays comparable with its Crisp siblings.

Two brand rules shape how the profile is applied:

- The brand is near-monochrome — a black CTA on white or near-black bands. Most state changes are therefore **paint-only** (`background-color`, `color`, `border-color`), driven at `{motion.duration-fast}`. That is the honest hover state for this brand; a scale pop would contradict a system whose only decoration is one gradient ribbon.
- The gradient ribbon is the single piece of brand chrome. It may drift as ambience, slowly and in `transform` only, and that ambience is declared as such below.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, nav links, table rows, cards) | `{motion.duration-fast}` | `{motion.ease-standard}` | `background-color`, `color`, `border-color`, `opacity` — paint only, no travel | Unchanged: paint-only change, already travel-free |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` (and `background-color`) — no scale, the CTA shape is fixed | Unchanged |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the 2 px ring; the ring's offset never animates | Ring appears instantly, no fade |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-standard}` | `opacity` on the content band only; no cross-fade of the dark/light polarity flip | Opacity only at `{motion.duration-reduced}` |
| Modal / drawer (mobile nav overlay, dialog) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px → 0)`; scrim `opacity` only | Opacity only at `{motion.duration-reduced}`, no translate |
| Dropdown / menu (nav submenu, model picker) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(4px → 0)`, origin at the trigger edge | Opacity only at `{motion.duration-reduced}`, no translate |
| Toast (`ex-toast`) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px → 0)` | Opacity only at `{motion.duration-reduced}`, no translate |
| List enter (research / article / testimonial grids, table rows) | `{motion.duration-base}` per item, `{motion.stagger-step}` 20 ms stagger, capped at 8 items | `{motion.ease-enter}` | `opacity` 0 → 1 + `transform: translateY(6px → 0)` | No stagger, no translate: the whole list fades once at `{motion.duration-reduced}` |
| List exit (filtered pricing rows) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` 1 → 0, no stagger — shorter than its entrance | Opacity only at `{motion.duration-reduced}` |
| Loading (skeletons, chat-launcher spinner, code-sample reveal) | `{motion.duration-slow}` loop for the skeleton sweep; indeterminate spinner at 800 ms per turn | `{motion.ease-standard}` (linear for the spinner) | `opacity` pulse on skeletons; `transform: rotate()` on the spinner — the only infinite animations in the system apart from the ribbon | Skeletons hold at a static `{colors.hairline}` block; the spinner is replaced by a mono-caps "LOADING…" label |
| Gradient ribbon ambience (hero only, declared ambience) | 20 s loop | `{motion.ease-standard}` | `transform` only — a slow drift of the layered translucent shapes, never a hue shift or a reorder of the three stops | Frozen on its first frame |
| Tab / toggle indicator (`feature-tab-pill`, `toggle-pill-group`) | `{motion.duration-fast}` | `{motion.ease-standard}` | `transform: translateX()` on the indicator; labels repaint, never re-layout | Indicator jumps; label colour fades at `{motion.duration-reduced}` |
| Nav polarity flip on scroll past the hero | `{motion.duration-base}` | `{motion.ease-standard}` | `background-color` + `color` only | Unchanged: paint-only |

### Rules
- `transform` and `opacity` only for anything that moves; paint properties for anything that merely recolours. Never `width`, `height`, `top`, `left` or `margin`.
- Every exit is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content: the hero headline and its CTA cluster render immediately, and only the ribbon's ambience and below-the-fold list entrances animate.
- The only infinite animations are the loaders and the declared hero ribbon ambience.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and scale — translateY on modals, dropdowns, toasts and
     list items; translateX on tab indicators; the ribbon's drift; the skeleton
     sweep and the spinner's rotation. */
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-property: opacity, background-color, color, border-color !important;
    transition-duration: 100ms !important;   /* {motion.duration-reduced} */
    transform: none !important;
  }
}
```

**Removed:** every translate and scale, the 20 ms list stagger, the skeleton sweep, the spinner rotation, and the hero ribbon's ambient drift (frozen on frame one). **Kept:** opacity fades and all paint-only state changes — hover, press, focus, selected, the nav polarity flip — at `{motion.duration-reduced}` (100 ms), never longer than 150 ms. Focus rings and the loading label remain fully visible, because removing motion must never remove feedback.

## Accessibility

Measured with WCAG 2.1 relative luminance from this file's own token values. Everything in the table below is computed; nothing here is a claim about a rendered page.

### Measured contrast — key pairs

| Pair | Values | Ratio | Required | Verdict |
|---|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | `#000000` / `#ffffff` | 21:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.canvas-dark}` | `#ffffff` / `#010120` | 20.46:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.surface-dark-soft}` | `#ffffff` / `#313641` | 12.11:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | `#ffffff` / `#000000` | 21:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.accent-mint}` | `#000000` / `#c8f6f9` | 18.01:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.accent-periwinkle}` | `#000000` / `#bdbbff` | 11.72:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.hairline}` | `#000000` / `#ebebeb` | 17.62:1 | 4.5:1 | Pass |
| **`{colors.body}` on `{colors.canvas}`** | `#959494` / `#ffffff` | **3.03:1** | 4.5:1 | **Fail — frozen, disclosed** |
| **`{colors.body}` on `{colors.hairline}`** (`data-table-header`) | `#959494` / `#ebebeb` | **2.54:1** | 4.5:1 | **Fail — frozen, disclosed** |
| **`{colors.hairline}` on `{colors.canvas}`** | `#ebebeb` / `#ffffff` | **1.19:1** | 3:1 | **Fail — frozen, disclosed** |
| **`{colors.hairline-on-dark}` on `{colors.canvas-dark}`** | `#26263a` / `#010120` | **1.38:1** | 3:1 | **Fail — frozen, disclosed** |
| `{colors.body}` on `{colors.surface-dark-soft}` | `#959494` / `#313641` | 4.0:1 | 4.5:1 | Fail — do not use; this pairing is not part of the brand |
| `{colors.accent-orange}` on `{colors.canvas}` | `#fc4c02` / `#ffffff` | 3.4:1 | 4.5:1 text / 3:1 non-text | Boundary and icon use only, never body text |
| `{colors.accent-magenta}` on `{colors.canvas}` | `#ef2cc1` / `#ffffff` | 3.62:1 | 4.5:1 text / 3:1 non-text | Gradient leg only; never a text colour |
| `{colors.accent-periwinkle}` on `{colors.canvas}` | `#bdbbff` / `#ffffff` | 1.79:1 | — | Fill only, never a foreground |
| `{colors.accent-mint}` on `{colors.canvas}` | `#c8f6f9` / `#ffffff` | 1.17:1 | — | Fill only, never a foreground |

**The real brand fails AA in three places, and this document does not hide it.**

1. **Secondary text.** `{colors.body}` `#959494` is the brand's only muted ink and it measures 3.03:1 on white — below the 4.5:1 AA threshold for body text, and below 3:1 for large text only in the sense that it *does* clear the 3:1 large-text bar. It is therefore defensible for ≥ 18.66 px bold or ≥ 24 px text and for the 11 px uppercase mono eyebrow **only if that eyebrow is treated as decoration with the information repeated in an accessible label** — which is not how the pricing table uses it. Nearest passing value on white: `#767676` (4.54:1). Changing it is a brand decision, not an audit decision.
2. **Table-header labels.** The same ink on the soft `#ebebeb` band is 2.54:1. This is the worst text pair in the file and it is load-bearing: it labels the price columns.
3. **Hairlines.** `#ebebeb` on white is 1.19:1 and `#26263a` on the navy band is 1.38:1, both far below the 3:1 WCAG 1.4.11 threshold for component boundaries. Decorative dividers at that ratio are acceptable; the same tone as the *only* boundary of `text-input` and `button-outline` is not. The palette already owns a passing tone, so no new colour is needed: draw control boundaries in `{colors.body}` (`#959494`, 3.03:1) and keep `{colors.hairline}` for dividers and card chrome. The extracted `rgba(0, 0, 0, 0.08)` bindings in the components block are left exactly as extracted — re-binding them is a brand owner's call.

### Focus ring visibility on every surface this file defines

The brand's signal colour *is* its ink, so the ring is the brand's own ink and paper with a mandatory 2 px offset in the opposite polarity, drawn outside the control. It is measured against the surface behind the control, not the control's fill.

| Ring | Drawn on | Ratio | Required |
|---|---|---|---|
| `{colors.focus}` `#000000` | `{colors.canvas}` `#ffffff` | 21:1 | 3:1 |
| `{colors.focus}` `#000000` | `{colors.hairline}` `#ebebeb` (table-header band, toggle rail) | 17.62:1 | 3:1 |
| `{colors.focus}` `#000000` | `{colors.accent-mint}` `#c8f6f9` (stat tiles, mint CTA) | 18.01:1 | 3:1 |
| `{colors.focus}` `#000000` | `{colors.accent-periwinkle}` `#bdbbff` | 11.72:1 | 3:1 |
| `{colors.focus-on-dark}` `#ffffff` | `{colors.canvas-dark}` `#010120` | 20.46:1 | 3:1 |
| `{colors.focus-on-dark}` `#ffffff` | `{colors.surface-dark-soft}` `#313641` | 12.11:1 | 3:1 |

Neither ring is extracted; both reuse a hex the palette already owns (`{colors.ink}` and `{colors.on-dark}`) rather than introducing a fifth colour, and neither touches the gradient, which the brand forbids reducing to a single swatch. The 2 px offset is what keeps a black ring legible around the black `button-primary` and a white ring legible around the white hero pill.

### Minimum tap target
The intended minimum is 44 × 44 px for every interactive control, including the mono-caps pill (whose resting box is about 32 px tall and is padded out on touch viewports) and the circular chat launcher. **This is a prescribed target, not a measurement:** a document has no rendered page, so no tap target in this file has been verified. Treat it as the spec to build to and re-measure in a browser.

### Colour is never the only channel
The brand documents no error, success or warning palette. Validation therefore uses `{colors.accent-orange}` **plus** a mono-caps text label and an icon — never colour alone. Disabled controls use `{colors.body}`, which WCAG exempts from contrast requirements.

### Reduced motion
`@media (prefers-reduced-motion: reduce)` removes all travel, scale, stagger and the hero ribbon's ambient drift, and keeps opacity and paint transitions at `{motion.duration-reduced}` (100 ms). Focus rings never fade or animate out of existence under reduced motion.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (`#000000`) for every primary CTA. One black pill per visible viewport — that consistency is the brand's whole conversion story.
- Set every section eyebrow and button label in `{typography.mono-caps-button}` / `{typography.mono-caps-eyebrow}` — uppercase mono, positive tracking.
- Pair the brand gradient (`{colors.accent-orange}` → `{colors.accent-magenta}` → `{colors.accent-periwinkle}`) at hero scale only. The gradient is the brand chrome; never shrink to icon size.
- Cycle page surfaces in the `{colors.canvas-dark}` → `{colors.canvas}` → `{colors.canvas-dark}` rhythm; the dark-light contrast carries elevation more than any shadow.
- Use `{rounded.sm}` 4 px as the canonical card / button radius across the system; reserve `{rounded.full}` for the single floating chat-launcher orb.
- Render the giant `together.ai` wordmark banner at the bottom of every long page in `{typography.display-xxl}`, tinted toward `{colors.hairline}` so it reads as a stencil — not as a heavy footer title.

### Don't
- Don't introduce a fifth accent colour. The three-stop gradient + mint pill is the entire decorative palette; new accents flatten the brand.
- Don't set body paragraphs in the mono face. The mono is for labels only; long-form mono reads as a console log, not as marketing copy.
- Don't centre-align body paragraphs under a left-aligned display headline. The brand keeps text-block alignment consistent within a copy stack.
- Don't drop a soft drop-shadow on light-surface cards. The brand uses hairlines and surface contrast for elevation; soft shadows belong only on the floating chat-launcher orb.
- Don't reduce the brand gradient to a single-colour fill, reorder its stops, or add a fourth stop. The gradient is a fixed object.
- Don't switch the primary button shape to a full pill `{rounded.full}`. The brand's CTA shape is a slightly-rounded rectangle, never a full pill.
- Don't set headlines in the all-caps mono. Every all-caps moment belongs to the mono face; every headline belongs to the display sans in sentence case.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 479px | Hero stacks; nav collapses to hamburger; all multi-col grids drop to 1-up. |
| Mobile-Large | 479–767px | Same as Mobile; some tables enable horizontal scroll. |
| Tablet | 768–991px | Article grid moves to 2-up; testimonial grid stays 3-up only if container > 900 px, otherwise 1-up. |
| Desktop | 992–1279px | Full 3-up research grid, 2-up article grid, hero 50/50 split. |
| Desktop-Large | ≥ 1280px | Container caps at 1280 px; bands stay edge-to-edge in colour while content centres. |

### Touch Targets
The mono-cap button label is set at 16 px; combined with `{spacing.xs}` 4 px top / bottom and a 24 px horizontal padding, the primary pill renders at roughly 32 px tall. On mobile viewports, button height is inflated to ≥ 44 px through extra vertical padding inside the touch row — meeting WCAG AAA. The circular icon button (`button-icon-circular`) renders at 44 × 44 px minimum at all viewports.

### Collapsing Strategy
- **Nav**: full link row + black "Sign in" pill + "Get started" pill at desktop. Collapses to logo + hamburger at mobile; the menu opens as a full-overlay drawer with the same link list stacked vertically.
- **Hero**: at desktop, headline left + gradient ribbon right (50 / 50). At mobile, headline stacks above a smaller-scale ribbon — never below.
- **Research band**: 4-up grid at desktop drops to 2-up at tablet, 1-up at mobile. Card chrome stays identical.
- **Pricing data table**: at desktop, full-width with all columns visible. At tablet, sub-tab row enables horizontal scroll. At mobile, cell rows stack model-name above price block.
- **Footer wordmark banner**: scales fluidly — the giant `together.ai` wordmark stays edge-to-edge regardless of viewport.

### Image Behavior
- **Hero ribbon graphic**: rendered as an SVG, scales fluidly with the hero container; never crops, never repositions.
- **Testimonial portraits**: square or 4:5 portrait, hard-cropped at top; consistent square framing across the grid.
- **Article thumbnails**: 16:9 landscape, fills card top with `{rounded.sm}` corners on the image only.
- **Logo bar**: customer logos rendered as grayscale SVGs in a wrapping flex row.

## Known Gaps

- **No `text-dim` role token, and that is correct for this brand.** Together AI keeps exactly one muted ink, `{colors.body}` `#959494`, used for captions, table-header labels, secondary cell values and footer links. It is the `text-dim` role in everything but name; the brand has no second, lighter secondary tone. No alias token was added to satisfy the role pattern, because an alias would document a tone the brand does not have. The audit harness reports `text-dim` as missing because its `text` role pattern claims `^body$` first — a naming collision, not an absent role (see the report's Shared issues).
- **The hairline value was contradictory and has been reconciled.** The frontmatter carried `hairline: "#959494"`, a duplicate of `{colors.body}`, while the prose twice stated `#ebebeb` and every component border is the literal `rgba(0, 0, 0, 0.08)`, which composites over `{colors.canvas}` to exactly `#ebebeb`. The token is now `#ebebeb`. If the extraction run that produced `#959494` was measuring a different element, the brand owner should say which.
- **`{colors.hairline-on-dark}` `#26263a` is a pre-blend, not a raw extraction.** It was named in the prose but had no token; the on-dark component borders are `rgba(255, 255, 255, 0.12)` literals, which composite to a slightly different value depending on the band beneath them.
- **Motion is entirely prescribed.** No duration, easing curve, stagger or keyframe in this file was measured from together.ai. The Crisp profile fills a vacuum; the 20 s ribbon ambience and the 800 ms spinner turn are the only non-token timings and both are prescribed too.
- **Both focus rings are prescribed.** The live site's focus treatment was not captured. The rings reuse existing brand hexes rather than inventing a colour, but the 2 px width and 2 px offset are this document's recommendation.
- **No semantic palette.** No error red, success green or warning amber is documented anywhere in the brand's public surface. The error states described in Components borrow `{colors.accent-orange}` and must be paired with text.
- **Nothing here is rendered.** Tap-target sizes, overflow, clipping, layout shift and frame rate cannot be checked from a document. Every such value in this file is a target to build to.
- **The `ex-*` examples are auto-derived**, not extracted surfaces. They mirror brand primitives so downstream kits stay consistent; they are not evidence about the live site.
- **Two off-ladder values survive by design:** `{rounded.xs}` 3.25 px and `{spacing.6xl}` 55.2 px are gap-multiplier derivatives of the 4 px base, not deliberate scale steps. They are kept because they were extracted.
