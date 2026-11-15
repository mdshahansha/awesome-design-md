---
version: alpha
name: Replicate-design-analysis
description: |
  Replicate's marketing surfaces pair the warm-cream developer-tools aesthetic
  of an indie ML playground with a confident hot-orange brand accent and a
  signature display typeface (rb-freigeist-neue) sized aggressively large at
  72px+. The system reads as "AI lab notebook crossed with print magazine":
  cream and bone surfaces, dark ink type, monospace code wells, irregular
  hand-drawn-feeling diagrams, and a rich orange used scarcely on the most
  consequential CTA. Photography of contributors and example outputs is
  square-ish with mid-radius corners; everything else is borderless or hairline.

colors:
  primary: "#ea2804"
  primary-deep: "#c01f00"
  on-primary: "#ffffff"
  ink: "#202020"
  body: "#3a3a3a"
  charcoal: "#575757"
  mute: "#646464"
  ash: "#8d8d8d"
  stone: "#bbbbbb"
  on-dark: "#fcfcfc"
  on-dark-mute: "rgba(252,252,252,0.72)"
  canvas: "#f9f7f3"
  surface-bone: "#f3f0e8"
  surface-card: "#ffffff"
  surface-dark: "#202020"
  surface-deep: "#000000"
  hairline: "rgba(32,32,32,0.12)"
  hairline-strong: "#202020"
  divider-dark: "rgba(255,255,255,0.2)"
  hero-warm: "#ea2804"
  hero-glow: "#ff6a3d"
  hero-pink: "#f4a8a0"
  badge-success: "#2b9a66"
  link: "#ea2804"
  ring-focus: "rgba(59,130,246,0.5)"
  focus: "#202020"
  focus-on-dark: "#fcfcfc"
  github-dark: "#24292e"

typography:
  display-xxl:
    fontFamily: rb-freigeist-neue
    fontSize: 128px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -3px
  display-xl:
    fontFamily: rb-freigeist-neue
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1.8px
  display-lg:
    fontFamily: rb-freigeist-neue
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  display-md:
    fontFamily: rb-freigeist-neue
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  heading-lg:
    fontFamily: basier-square
    fontSize: 38.4px
    fontWeight: 600
    lineHeight: 0.83
    letterSpacing: -0.5px
  heading-md:
    fontFamily: basier-square
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.35px
  heading-sm:
    fontFamily: basier-square
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: -0.3px
  subtitle:
    fontFamily: rb-freigeist-neue
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: 0
  body-lg:
    fontFamily: basier-square
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: basier-square
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: basier-square
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: basier-square
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0
  button-sm:
    fontFamily: basier-square
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0
  caption:
    fontFamily: basier-square
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-tight:
    fontFamily: basier-square
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: -0.35px
  code-md:
    fontFamily: jetbrains-mono
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  code-sm:
    fontFamily: jetbrains-mono
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
  lg: 16px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  xxxl: 48px
  section: 96px
  band: 160px

shadow:
  soft-drop: "0 8px 24px rgba(32,32,32,0.08)"

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
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-outline:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  button-icon:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  hero-band:
    backgroundColor: "{colors.hero-warm}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: 96px 32px
  model-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 16px
  collection-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-md}"
    rounded: "{rounded.md}"
    padding: 24px
  pricing-tier:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-featured:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  code-block:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code-md}"
    rounded: "{rounded.md}"
    padding: 24px
  code-tab:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark-mute}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  badge-status:
    backgroundColor: "{colors.badge-success}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 60px
  sub-nav-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  contributor-avatar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 40px
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 64px 32px
---

## Overview

Replicate is a developer-tools platform with the soul of an art zine. The
public marketing surfaces sit on a warm cream canvas (`{colors.canvas}` —
`#f9f7f3`) rather than the white-or-near-black default of typical AI
infrastructure sites, and that single decision colours everything else:
photography reads as editorial, code wells read as printed pull-quotes, and
the brand orange (`{colors.primary}` — `#ea2804`) feels like a stamp rather
than a notification.

The typography is the load-bearing decoration. **rb-freigeist-neue** — a
heavy, slightly condensed grotesque — appears at sizes up to 128px in hero
bands, with a tight `lineHeight: 1.0` and negative letter-spacing that lets
multi-line headlines pack into geometric blocks. The companion family,
**basier-square**, takes care of body, button labels, and metadata in the
14–18px range. **JetBrains Mono** carries every code well, command, and
example. Three families, three jobs, no overlap.

Page rhythm cycles between a default cream canvas, a bold full-bleed orange
hero band, and a `{colors.surface-dark}` (`#202020`) section that hosts the
code stories — the "how it works" walkthrough. Curves are intentional and
soft: every interactive surface (buttons, inputs, tags, avatars) uses
`{rounded.full}`, while content cards and code wells step up to `{rounded.md}`
or `{rounded.lg}`. There are no sharp corners on Replicate; the system reads
as friendly precision.

**Key Characteristics:**
- A warm cream canvas (`{colors.canvas}` — `#f9f7f3`) replaces the typical white background, paired with `{colors.surface-bone}` for inset cards.
- Hot orange (`{colors.primary}` — `#ea2804`) is reserved for the primary CTA, the hero band, and inline link colour. Never decorative.
- Display headlines run massive — `{typography.display-xxl}` at 128px in hero bands and `{typography.display-xl}` at 72px on section openers — with tight `lineHeight: 1.0` and negative letter-spacing.
- Three-family typography stack: `rb-freigeist-neue` for display, `basier-square` for UI/body, `jetbrains-mono` for code.
- Every interactive element is fully rounded (`{rounded.full}` 9999px) — buttons, inputs, badges, avatars — while content cards step to `{rounded.md}` 10px.
- Dark code wells (`{colors.surface-dark}` background) sit inside the cream canvas as full-bleed reading surfaces, mimicking print pull-quotes.
- Section rhythm: cream → orange hero → cream → dark code-story band → cream → black footer.

## Colors

### Brand & Accent
- **Replicate Orange** (`{colors.primary}` — `#ea2804`): the brand accent. Reserved for the primary CTA, hero band background, and inline link colour. Treat as a stamp — one orange element per viewport at most.
- **Orange Pressed** (`{colors.primary-deep}` — `#c01f00`): the active/pressed state of `{colors.primary}` — used on `{component.button-primary-pressed}`.
- **Hero Glow** (`{colors.hero-glow}` — `#ff6a3d`): the lighter orange that appears in the radial atmospheric mesh behind the hero copy.
- **Hero Pink** (`{colors.hero-pink}` — `#f4a8a0`): a warm pink wash that softens the bottom edge of the hero band before it transitions to cream.
- **On-Primary** (`{colors.on-primary}` — `#ffffff`): label colour on top of `{colors.primary}` surfaces.

### Surface
- **Canvas** (`{colors.canvas}` — `#f9f7f3`): the default page background. Warm cream, never pure white.
- **Surface Bone** (`{colors.surface-bone}` — `#f3f0e8`): a half-step deeper cream used for inset card groups and feature bands.
- **Surface Card** (`{colors.surface-card}` — `#ffffff`): pure white for individual model cards, search inputs, and pricing tiers — the only place white appears.
- **Surface Dark** (`{colors.surface-dark}` — `#202020`): code wells, featured pricing tier, and the "how it works" walkthrough band.
- **Surface Deep** (`{colors.surface-deep}` — `#000000`): footer canvas and the inset code-tab strip inside `{component.code-block}`.
- **Hairline** (`{colors.hairline}` — `rgba(32,32,32,0.12)`): low-contrast 1px dividers on cream surfaces. Composites to `#dfddda` on `{colors.canvas}` (1.27:1) and `#dad7d0` on `{colors.surface-bone}` (1.26:1), so it is **decoration only** — a mood rule between content blocks. Where a boundary is the only thing defining a control (the `{component.text-input}` edge, the `{component.button-icon}` edge, the `{component.badge-tag}` edge), use `{colors.hairline-strong}` instead, which the palette already owns and which clears 3:1 on every cream surface. The real site draws the faint hairline on those controls, and that fails WCAG 1.4.11; see Accessibility.
- **Hairline Strong** (`{colors.hairline-strong}` — `#202020`): button outlines, focused inputs, structural separators, and the accessible boundary for any control whose edge carries meaning.

### Text
- **Ink** (`{colors.ink}` — `#202020`): primary text colour. Notably warmer than `#000000`, matching the cream canvas.
- **Body** (`{colors.body}` — `#3a3a3a`): long-form body copy where ink would feel too heavy at 18px+ line lengths.
- **Charcoal** (`{colors.charcoal}` — `#575757`): captions, metadata, secondary nav.
- **Mute** (`{colors.mute}` — `#646464`): supporting text and inactive labels.
- **Ash** (`{colors.ash}` — `#8d8d8d`): tertiary text, placeholder copy.
- **Stone** (`{colors.stone}` — `#bbbbbb`): disabled foreground, neutral icon outlines.
- **On-Dark** (`{colors.on-dark}` — `#fcfcfc`): primary text on `{colors.surface-dark}` and `{colors.surface-deep}`.
- **On-Dark Mute** (`{colors.on-dark-mute}` — `rgba(252,252,252,0.72)`): secondary text in dark regions; preserves the off-white feel without pure white pop.

### Semantic
- **Success** (`{colors.badge-success}` — `#2b9a66`): inline success badges and "running" status pills on model cards.
- **Link** (`{colors.link}` — `#ea2804`): inline link colour — same as primary orange, intentionally pulling links into the brand accent.
- **Focus Ring, extracted** (`{colors.ring-focus}` — `rgba(59,130,246,0.5)`): the ring the live site ships. A half-opacity generic blue; it composites to `#9abcf4` on `{colors.canvas}` (1.80:1) and `#2e518b` on `{colors.surface-dark}` (2.07:1), so it clears 3:1 on **no** surface this file defines. Kept as the extracted fact, not as the recommendation.
- **Focus Ring, light surfaces** (`{colors.focus}` — `#202020`): the ring to draw on `{colors.canvas}`, `{colors.surface-bone}` and `{colors.surface-card}`. Not a new brand colour — it is the same ink as `{colors.ink}` and `{colors.hairline-strong}`, reused for the ring job, which keeps the "no second accent" rule intact.
- **Focus Ring, dark surfaces** (`{colors.focus-on-dark}` — `#fcfcfc`): the ring on `{colors.surface-dark}`, `{colors.surface-deep}` and the orange `{component.hero-band}` — the same off-white as `{colors.on-dark}`. Two rings are needed because this file documents both cream and near-black signature surfaces, and no single tone clears 3:1 on both.
- **GitHub Dark** (`{colors.github-dark}` — `#24292e`): the GitHub-branded button surface (kept off-brand-on-purpose to match GitHub's own tokens).

## Typography

### Font Family

Replicate ships a deliberate three-family stack:

- **rb-freigeist-neue** — proprietary heavy grotesque used for all display sizes (30px+). Carries the editorial-magazine personality through tight `lineHeight: 1.0` and negative letter-spacing.
- **basier-square** — proprietary humanist sans-serif used for body, button labels, captions, and metadata.
- **jetbrains-mono** — open-source monospace used in every code well and inline command.

When proprietary families cannot be licensed, **Bricolage Grotesque** or **Migra** are credible substitutes for rb-freigeist-neue, and **Geist** or **Inter** can stand in for basier-square. JetBrains Mono is open-source and should always be used directly.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 128px | 700 | 1.0 | -3px | The single hero "Run AI" / "Imagine what you can build" headline. One per page. |
| `{typography.display-xl}` | 72px | 700 | 1.0 | -1.8px | Section openers ("How it works", "Scale on Replicate"). |
| `{typography.display-lg}` | 48px | 700 | 1.0 | -1px | Sub-section titles, pricing tier names. |
| `{typography.display-md}` | 30px | 600 | 1.2 | -0.5px | Feature card titles. |
| `{typography.heading-lg}` | 38.4px | 600 | 0.83 | -0.5px | Tightly-stacked basier-square headlines, used in pricing and enterprise hero. |
| `{typography.heading-md}` | 24px | 600 | 1.33 | -0.35px | Card titles, model detail headers. |
| `{typography.heading-sm}` | 20px | 600 | 1.4 | -0.3px | List section headers. |
| `{typography.subtitle}` | 18px | 600 | 1.56 | 0 | Lead paragraphs in display sections. |
| `{typography.body-lg}` | 18px | 400 | 1.56 | 0 | Marketing prose. |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default body. |
| `{typography.body-sm}` | 14px | 400 | 1.43 | 0 | Captions, metadata. |
| `{typography.button-md}` | 16px | 600 | 1.0 | 0 | Default button label. |
| `{typography.button-sm}` | 14px | 600 | 1.0 | 0 | Compact button label, sub-nav pills. |
| `{typography.caption}` | 12px | 400 | 1.33 | 0 | Footer disclosure, copyright. |
| `{typography.caption-tight}` | 14px | 600 | 1.43 | -0.35px | Emphatic small caption used in pricing tier rows. |
| `{typography.code-md}` | 14px | 400 | 1.43 | 0 | Code blocks and inline code. |
| `{typography.code-sm}` | 11px | 400 | 1.5 | 0 | Code-tab labels and small inline tokens. |

### Principles
- Display sizes hold `lineHeight: 1.0` (or 0.83 on `{typography.heading-lg}`) so multi-line stacks read as single typographic blocks.
- Negative letter-spacing scales with size — bigger types tighten more (-3px at 128px down to -0.3px at 20px). Body type stays at 0.
- Body weight sits at 400 across `{typography.body-lg}` and `{typography.body-md}` — never bumped to 500 for emphasis. Emphasis comes from family change (basier-square → rb-freigeist-neue) rather than weight.
- Code is never set in basier-square, even at small sizes — JetBrains Mono carries every literal command, every model slug, every API call.

### Note on Font Substitutes

When the proprietary families are unavailable, clamp display `lineHeight` to 1.0 explicitly and apply a -3% letter-spacing on display-xxl / display-xl to match the original tightness. Substitutes typically render with looser tracking by default.

## Layout

### Spacing System
- **Base unit**: 4px, with the working scale on multiples of 4 / 8 / 16.
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.xxxl}` 48px · `{spacing.section}` 96px · `{spacing.band}` 160px.
- Section padding: `{spacing.section}` (96px) vertical between full-width bands; `{spacing.band}` (160px) when a band needs extra editorial breathing room (the hero, the closing "Imagine what you can build" stripe).
- Card internal padding: `{spacing.lg}` (16px) on `{component.model-card}`, `{spacing.xxl}` (32px) on `{component.pricing-tier}`.

### Grid & Container
- **Max content width** ≈ 1280px on body sections, 1440px on hero bands which run full-bleed.
- **Model grid** on collections: 4 columns at desktop, 3 at tablet large, 2 at tablet, 1 at mobile.
- **Pricing**: 3-tier grid centred at desktop, stacking vertically below 1024px; the centre tier flips to `{component.pricing-tier-featured}` (dark inversion) as the recommended option.
- **Code-story sections**: a 2-up split — narrative copy left, code well right — collapsing to stacked at < 1024px.

### Whitespace Philosophy
- Whitespace on cream is generous and editorial — sections breathe at 96px and key bands open at 160px so the typography can scale up without feeling cramped.
- Inside cards, the system tightens to 16–32px so model thumbnails, statuses, and metadata sit in a compact list-of-cards rhythm.
- Hairline `{colors.hairline}` dividers replace shadow on cream surfaces; on dark surfaces, `{colors.divider-dark}` carries the equivalent role.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | No shadow, no border | Default cream canvas, full-bleed bands. |
| 1 — outline | 1px solid `{colors.hairline}` or `{colors.hairline-strong}` | Model cards, pricing tiers, collection tiles. |
| 2 — bone inset | Surface colour shift to `{colors.surface-bone}` inside a `{colors.canvas}` band | Feature group containers, "How it works" walkthrough. |
| 3 — dark inversion | Card swaps to `{colors.surface-dark}` against cream | Code wells, featured pricing tier, "Scale on Replicate" hero card. |
| 4 — soft drop | `{shadow.soft-drop}` — `0 8px 24px rgba(32,32,32,0.08)` | Hover-anchored model thumbnails. Applied on `{component.model-card}` hover, thumbnail only. |

Drop shadows exist in the extracted tokens but are restrained — used sparingly to lift photography thumbnails one step off the cream canvas. The dominant elevation language is colour-blocking.

Elevation is expressed one way per level, not as a mix: levels 0–3 never carry a shadow, and level 4 is the only shadow in the system. That consistency comes at a cost worth stating — the cream layers are extremely close in luminance. `{colors.canvas}` to `{colors.surface-bone}` measures **1.06:1** and `{colors.canvas}` to `{colors.surface-card}` **1.07:1**, so the layer boundary is legible only as a *warmth* shift, not a brightness one. Anywhere the boundary has to carry structure rather than mood, add a `{colors.hairline-strong}` edge (level 1) instead of relying on the fill shift. The dark inversion at level 3 has no such problem (`{colors.canvas}` to `{colors.surface-dark}` is **15.23:1**), while `{colors.surface-dark}` to `{colors.surface-deep}` is **1.29:1** — the code-tab strip inside `{component.code-block}` reads as a seam, not a step.

### Decorative Depth
- **Hero atmospheric mesh** — the orange-to-pink gradient backing the home hero is a layered radial mesh: `{colors.primary}` core → `{colors.hero-glow}` mid-stop → `{colors.hero-pink}` outer wash. Reserved for the home hero band only.
- **Code-story dark band** — the "How it works" section uses `{colors.surface-dark}` full-bleed with a single hairline `{colors.divider-dark}` separating narrative copy and code well.
- **Contributor mosaic** — the home page features a horizontally-scrolling band of circular avatars (`{component.contributor-avatar}`) over a textured cream canvas; this is the only place avatars appear at the brand level.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Hero bands, full-bleed sections, footer. |
| `{rounded.xs}` | 4px | Code tabs, inline tags inside code wells. |
| `{rounded.sm}` | 6px | Mid-radius callouts, small inset chips. |
| `{rounded.md}` | 10px | Model cards, collection tiles, code wells. |
| `{rounded.lg}` | 16px | Pricing tiers, larger feature cards. |
| `{rounded.full}` | 9999px | Buttons, inputs, badges, avatars, pills. |

### Photography Geometry
- Model thumbnails: square (1:1) with `{rounded.md}` corners, full-bleed image to the card edge.
- Hero example outputs: 4:3 or 16:9 with `{rounded.md}` corners.
- Contributor avatars: circular (`{rounded.full}`), 40px on home, 32px in card metadata.
- The hero band uses a stylised black-ink illustration (the "tinkerer at the workbench") as its photography stand-in — kept inside the orange band rather than overlaid on cream.

## Components

### Buttons

**`button-primary`** — orange CTA
- Background `{colors.primary}`, label `{colors.on-primary}`, type `{typography.button-md}`, padding `12px 24px`, `rounded: {rounded.full}`, height 44px.
- The single most important action on a page (e.g. "Sign in with GitHub", "Try a model").
- Pressed state lives in `button-primary-pressed` (background `{colors.primary-deep}`).
- States — default, hover, focus-visible, active/pressed, disabled, loading. Default and active/pressed are extracted; the rest are prescribed by this audit. Hover: opacity 0.92 on the fill, `{motion.duration-fast}`. Focus-visible: 2px `{colors.focus}` ring at 2px offset on cream, `{colors.focus-on-dark}` inside the `{component.hero-band}`. Active/pressed: `{colors.primary-deep}` via `{component.button-primary-pressed}`, scale 0.98. Disabled: fill `{colors.stone}`, label `{colors.surface-card}`, pointer-events off. Loading: label swaps to a spinner in `{colors.on-primary}`, fill unchanged, width frozen so the row does not reflow.

**`button-dark`** — dark CTA
- Background `{colors.surface-dark}`, label `{colors.on-dark}`, type `{typography.button-md}`, `rounded: {rounded.full}`.
- Equal-weight secondary action paired with `{component.button-primary}`, or the primary action on cream when orange would be too loud.
- States — default, hover, focus-visible, active/pressed, disabled, loading. Prescribed, except default. Hover: fill lifts toward `{colors.charcoal}` at opacity 0.92. Focus-visible: `{colors.focus}` ring, 2px offset, drawn on the cream ground behind the pill. Active/pressed: scale 0.98. Disabled: fill `{colors.stone}`, label `{colors.surface-card}`. Loading: spinner in `{colors.on-dark}`.

**`button-outline`** — outlined CTA
- Background `{colors.surface-card}`, label `{colors.ink}`, 1px solid `{colors.hairline-strong}`, type `{typography.button-md}`, `rounded: {rounded.full}`.
- Tertiary action; appears alongside primary/dark for "View docs", "Read more".
- States — default, hover, focus-visible, active/pressed, disabled. Prescribed, except default. Hover: fill shifts to `{colors.surface-bone}`, border stays `{colors.hairline-strong}`. Focus-visible: `{colors.focus}` ring at 2px offset, outside the existing 1px border so the two never merge. Active/pressed: scale 0.98. Disabled: border and label drop to `{colors.stone}`. No loading state — this button never submits.

**`button-ghost`** — inline button
- Background `{colors.canvas}`, label `{colors.ink}`, no border, type `{typography.button-md}`, `rounded: {rounded.full}`, padding `8px 16px`.
- Sub-actions inside cards and inline with body copy.
- States — default, hover, focus-visible, active/pressed, disabled. Prescribed, except default. Hover: fill `{colors.surface-bone}`. Focus-visible: `{colors.focus}` ring, 2px offset. Active/pressed: scale 0.98. Disabled: label `{colors.stone}`.

**`button-icon`** — icon button
- Background `{colors.surface-card}`, label `{colors.ink}`, 1px solid `{colors.hairline}`, `rounded: {rounded.full}`, 36×36px circular.
- Carousel arrows, copy-to-clipboard, GitHub link icon.
- States — default, hover, focus-visible, active/pressed, disabled, selected. Prescribed, except default. Hover: border steps from `{colors.hairline}` to `{colors.hairline-strong}`. Focus-visible: `{colors.focus}` ring, 2px offset. Active/pressed: scale 0.94 — the one place a slightly deeper press reads, since the target is only 36px. Disabled: border and glyph `{colors.stone}` (carousel arrow at the end of the rail). Selected: used only for the copy-to-clipboard confirm, glyph swaps to `{colors.badge-success}` for `{motion.duration-slow}`.

### Cards & Containers

**`model-card`** — model listing card
- Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.body-md}`, `rounded: {rounded.md}`, padding `{spacing.lg}` (16px).
- Square thumbnail on top, model owner + name beneath in `{typography.body-sm}`, single-line description in `{colors.charcoal}`, status pill `{component.badge-status}` bottom-left.
- States — default, hover, focus-visible, loading. Default is extracted; the rest are prescribed. Hover: `{shadow.soft-drop}` on the thumbnail only, at `{motion.duration-fast}`. Focus-visible: `{colors.focus}` ring at 2px offset around the whole card, since the card is one link. Loading: a skeleton in `{colors.surface-bone}` with an opacity pulse, no shimmer sweep. The card has no pressed, disabled, selected or error state — it is a link, not a control.

**`collection-tile`** — collection-of-models tile
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.heading-md}`, `rounded: {rounded.md}`, padding `{spacing.xl}` (24px).
- Cream-on-cream tile inside a `{colors.surface-bone}` band, used for browsing model categories.
- States — default, hover, focus-visible. Two beyond default, both prescribed; this tile is a plain navigation link with no pressed, disabled, loading, selected or error state. Hover: fill shifts from `{colors.canvas}` to `{colors.surface-card}`. Focus-visible: `{colors.focus}` ring at 2px offset — measured against `{colors.surface-bone}`, the band behind the tile, not against the tile fill.

**`pricing-tier`** — pricing tier card
- Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}` (32px).
- 3-up grid; tier name in `{typography.display-lg}` ("Free", "Pro", "Enterprise"), price in `{typography.display-md}`.
- States — default, selected. The container itself is static; "selected" is the recommended-tier inversion, which is a separate entry rather than a style flag — see `{component.pricing-tier-featured}`. Hover, focus-visible, pressed, disabled, loading and error live on the `{component.button-primary}` inside the tier, not on the tier.

**`pricing-tier-featured`** — featured pricing tier
- Background `{colors.surface-dark}`, text `{colors.on-dark}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}`.
- Centre tier flipped to dark inversion to mark "recommended".
- States — default only; it *is* the selected variant of `{component.pricing-tier}`. Its inner CTA is a `{component.button-primary}` and carries that entry's hover, focus-visible, pressed, disabled and loading states, with the ring swapping to `{colors.focus-on-dark}` because the ground here is `{colors.surface-dark}`.

**`code-block`** — code well
- Background `{colors.surface-dark}`, text `{colors.on-dark}`, type `{typography.code-md}`, `rounded: {rounded.md}`, padding `{spacing.xl}` (24px).
- Tab strip on top using `{component.code-tab}` for switching between languages (Python, Node.js, cURL, HTTP).
- States — default only. The well is a reading surface; every interactive state belongs to `{component.code-tab}` and the copy `{component.button-icon}` sitting in its corner.

**`code-tab`** — code tab chip
- Background `{colors.surface-deep}`, text `{colors.on-dark-mute}`, type `{typography.code-sm}`, `rounded: {rounded.xs}`, padding `6px 12px`.
- Active tab swaps text colour to `{colors.on-dark}` and adds a 2px bottom underline in `{colors.primary}`.
- States — default, hover, focus-visible, selected. Default and selected are extracted (the active-tab treatment above); hover and focus-visible are prescribed. Hover: label lifts from `{colors.on-dark-mute}` to `{colors.on-dark}`. Focus-visible: 2px `{colors.focus-on-dark}` ring at 2px offset, drawn on `{colors.surface-deep}`. No pressed, disabled, loading or error state.

**`hero-band`** — full-bleed hero
- Background `{colors.hero-warm}` with the atmospheric mesh detailed in Elevation, text `{colors.on-dark}`, type `{typography.display-xxl}` for the title.
- Used only on the home page; secondary pages open with cream + `{typography.display-xl}`.
- States — default only. It is a layout band, not a control; any focus-visible ring belongs to the `{component.button-primary}` inside it and switches to `{colors.focus-on-dark}` against the orange.

### Inputs & Forms

**`text-input`** — default input
- Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.body-md}`, 1px solid `{colors.hairline}`, `rounded: {rounded.full}`, padding `12px 20px`, height 44px.
- Pill-shaped search and email fields. Focus state as extracted adds a `{colors.ring-focus}` 3px ring — which clears 3:1 on none of this file's surfaces (see Accessibility).
- States — default, hover, focus-visible, disabled, loading, error. Default is extracted; the rest are prescribed. Hover: border steps from `{colors.hairline}` to `{colors.hairline-strong}`. Focus-visible: 2px `{colors.focus}` ring at 2px offset, replacing the extracted blue; the border itself goes `{colors.hairline-strong}`. Disabled: fill `{colors.surface-bone}`, placeholder `{colors.stone}`. Loading: the trailing `{component.button-icon}` slot carries the spinner while a search resolves; the field stays editable. Error: border `{colors.primary}` plus a `{typography.body-sm}` message beneath in `{colors.primary-deep}` — orange is the only signal tone this brand owns, so the error state reuses it and is always paired with text, never colour alone.

### Navigation

**`nav-bar`** — top nav (desktop)
- Background `{colors.canvas}`, type `{typography.button-sm}`, height 60px, single hairline `{colors.hairline}` bottom border.
- Left: wordmark logo. Centre: top-level nav ("Explore", "Pricing", "Docs", "Blog"). Right: GitHub icon + "Sign in" link + `{component.button-primary}`.
- States — default; its links carry hover, focus-visible and selected. Prescribed, except default. Link hover: label `{colors.ink}` from `{colors.charcoal}`. Link focus-visible: `{colors.focus}` ring, 2px offset, on `{colors.canvas}`. Selected (current section): label `{colors.ink}` with a 2px `{colors.primary}` underline. The bar has no pressed, disabled, loading or error state.

**`nav-bar`** (mobile)
- Same height 60px, collapses centre nav into a hamburger icon. Logo stays left, sign-in CTA stays right.

**`sub-nav-pill`** — sub-nav chip
- Pill chips set in a horizontal row above content (e.g. "All", "Featured", "Image generation", "Audio"), `{component.sub-nav-pill}` styling.
- States — default, hover, focus-visible, selected. Prescribed, except default. Hover: fill `{colors.surface-bone}`. Focus-visible: `{colors.focus}` ring, 2px offset. Selected: fill flips to `{colors.surface-dark}` with the label in `{colors.on-dark}` — the same dark-inversion move the pricing grid uses, so "chosen" reads one way across the system. No pressed, disabled, loading or error state.

### Signature Components

**`badge-status`** — model status badge
- Background `{colors.badge-success}`, label `{colors.on-dark}`, type `{typography.caption}`, `rounded: {rounded.full}`, padding `4px 10px`.
- Anchored on the bottom-left of model cards to indicate "running" or "deployed".
- States — default only, and that is genuine: the badge is a status readout, not a control. It has no hover, focus-visible, pressed, disabled, selected or error variant. Where a model is failing, the card shows an error badge built from `{colors.primary-deep}` label on `{colors.canvas}` (5.71:1) with the word "failed" — colour never carries the status alone.

**`badge-tag`** — neutral tag
- Background `{colors.canvas}`, label `{colors.ink}`, 1px solid `{colors.hairline}`, type `{typography.caption}`, `rounded: {rounded.full}`, padding `4px 10px`.
- Capability tags ("text-to-image", "video", "audio") on model cards.
- States — default, hover, focus-visible, selected where the tag is a filter link. Prescribed, except default. Hover: border steps to `{colors.hairline-strong}`. Focus-visible: `{colors.focus}` ring, 2px offset. Selected: fill `{colors.surface-dark}`, label `{colors.on-dark}`. A tag rendered as pure metadata has default only and no pressed, disabled, loading or error state.

**`contributor-avatar`** — community contributor
- Background `{colors.surface-card}` placeholder behind 1:1 photography, `rounded: {rounded.full}`, 40×40px (32px in metadata contexts).
- Used in the home-page contributor mosaic.
- States — default, hover, focus-visible, loading. Prescribed, except default. Hover: opacity 1.0 from a resting 0.9, plus the contributor name in a `{typography.caption}` tooltip. Focus-visible: `{colors.focus}` ring, 2px offset. Loading: `{colors.surface-bone}` circle, no pulse — thirty avatars pulsing at once is noise. No pressed, disabled, selected or error state.

**`footer`** — global footer
- Background `{colors.surface-deep}`, text `{colors.on-dark}`, type `{typography.body-sm}`, `rounded: {rounded.none}`, padding `64px 32px`.
- Multi-column quick-links grid above a copyright row separated by `{colors.divider-dark}`.
- States — default; its links carry hover and focus-visible. Prescribed, except default. Link hover: label `{colors.on-dark}` from `{colors.on-dark-mute}` with an underline. Link focus-visible: 2px `{colors.focus-on-dark}` ring at 2px offset, drawn on `{colors.surface-deep}`. No pressed, disabled, loading, selected or error state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** No timing function, duration or stagger below
was extracted from Replicate; every value comes from the **Crisp** profile in
`theme-audit/SPEC.md`, chosen because this is a developer-tools and ML-infra
identity — a place where a model either ran or did not, and where state change
should read as instant rather than choreographed. The one brand-specific reading
is restraint: a product whose own rule is "one orange element per viewport" does
not get entrance animation on its content either.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, cards, pills, tags) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` (and `background-color` as a colour change, not a transform) | Colour change applies at once; no opacity ramp. |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` — `scale(0.94)` on `{component.button-icon}` | Scale removed entirely; the pressed fill (`{colors.primary-deep}`) carries the feedback. |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring only | Ring appears with no transition. Never animate the ring's offset — it must be at full size the moment it exists. |
| Page / route transition | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` on the content region only | Cross-fade at `{motion.duration-reduced}`; no travel. The cream canvas never fades, so no flash between routes. |
| Modal / drawer (mobile nav sheet) | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` + `transform: translateY(8px -> 0)` | Travel removed; opacity only at `{motion.duration-reduced}`. Scrim fades at the same duration. |
| Dropdown (language switcher, account menu) | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` + `transform: translateY(4px -> 0)` | Travel removed; opacity only at `{motion.duration-reduced}`. |
| Toast (copy confirmation, "model queued") | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity` + `transform: translateY(6px -> 0)` | Travel removed; opacity only at `{motion.duration-reduced}`. Dismiss timer unchanged. |
| List enter (model grid, collection tiles, contributor mosaic) | `{motion.duration-fast}` per item, `{motion.stagger-step}` between items, capped at 8 items | `{motion.ease-enter}` | `opacity` 0 -> 1 | Stagger and fade both removed; the grid is present on first paint. |
| List exit (filtered-out cards) | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` 1 -> 0 | Items are removed without a fade. |
| Loading (button spinner, card skeleton) | 800ms per rotation, infinite while pending | linear | `transform: rotate()` on the spinner; `opacity` 0.6 -> 1 -> 0.6 on the skeleton | Spinner is replaced by a static glyph; the skeleton holds one flat `{colors.surface-bone}` fill with no pulse. |

### Rules

- Only `transform` and `opacity` are animated. Never `width`, `height`, `top`,
  `left` or `margin` — a 128px `{typography.display-xxl}` headline reflowing
  mid-transition is the one failure mode this system cannot absorb.
- Every exit is shorter than its matching entrance (`{motion.duration-fast}`
  enter / `{motion.duration-instant}` exit on dropdowns and toasts;
  `{motion.duration-base}` / `{motion.duration-fast}` on the mobile sheet).
- Nothing animates on first paint in a way that delays content. The hero
  `{component.hero-band}` and its atmospheric mesh are painted, not revealed.
- The only infinite animations are the loading spinner and the skeleton pulse.
  The hero mesh is a static CSS gradient and is deliberately **not** animated
  ambience — see Responsive Behavior.
- The `{component.contributor-avatar}` mosaic scroll-rail is user-driven, not an
  auto-playing marquee. If a build adds auto-scroll it must be declared as brand
  ambience and frozen under reduced motion.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translateY on sheets, dropdowns, toasts),
     all scale (press feedback on every button), the list-enter stagger,
     the spinner rotation and the skeleton pulse. */
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-property: opacity !important;   /* no transform, ever */
    transition-duration: 100ms !important;      /* {motion.duration-reduced} */
  }
}
```

What remains: opacity fades, capped at `{motion.duration-reduced}` (100ms);
instant colour changes on hover; the focus ring, which never had a transition to
begin with. What is removed: every `translateY`, every `scale`, the
`{motion.stagger-step}` cascade, the spinner rotation and the skeleton pulse.
Pressed states stay legible because they are colour (`{colors.primary-deep}`),
not movement.

## Accessibility

Ratios below are computed with WCAG 2.1 relative luminance from this file's own
token values; `rgba()` tokens are composited over the stated ground first.

### Measured contrast — key pairs

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 15.23:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-bone}` | 14.31:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-card}` | 16.29:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas}` | 10.63:1 | 4.5:1 | Pass |
| `{colors.charcoal}` on `{colors.canvas}` | 6.75:1 | 4.5:1 | Pass |
| `{colors.mute}` on `{colors.canvas}` | 5.53:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.surface-dark}` | 15.88:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.surface-deep}` | 20.47:1 | 4.5:1 | Pass |
| `{colors.on-dark-mute}` (composites to `#bebebe`) on `{colors.surface-dark}` | 8.77:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 15.23:1 | 3:1 | Pass |
| `{colors.focus}` on `{colors.canvas}` | 15.23:1 | 3:1 | Pass |
| `{colors.primary-deep}` on `{colors.canvas}` | 5.71:1 | 4.5:1 | Pass |
| `{colors.github-dark}` under `{colors.on-dark}` | 14.30:1 | 4.5:1 | Pass |

### Measured failures — stated, not hidden

Four pairs in this document do not meet AA. Three of them are extracted brand
facts and are **not** altered here; the fourth is a utility tone now scoped to
decoration.

| Pair | Ratio | Required | Why it stands |
|---|---|---|---|
| `button-primary` — `{colors.on-primary}` `#ffffff` on `{colors.primary}` `#ea2804` | 4.37:1 | 4.5:1 | Replicate's primary CTA genuinely fails AA for normal-size text by a hair. `#ea2804` is the brand. Not changed. See Needs approval in the audit report. |
| `badge-status` — `{colors.on-dark}` `#fcfcfc` on `{colors.badge-success}` `#2b9a66` | 3.46:1 | 4.5:1 | The status pill is set in `{typography.caption}` at 12px, so the 3:1 large-text allowance does not apply. Extracted green, not changed. |
| `{colors.hairline}` composited to `#dfddda` on `{colors.canvas}` | 1.27:1 | 3:1 | Extracted hairline. Scoped to decoration in Colors; `{colors.hairline-strong}` is the boundary token for anything a control depends on. |
| `{colors.hairline}` composited to `#dad7d0` on `{colors.surface-bone}` | 1.26:1 | 3:1 | Same tone, inset band. Decoration only. |

Three further values are below AA and are called out because the file names
them, even though the harness exempts or skips them:

- `{colors.link}` / `{colors.primary}` `#ea2804` as inline link text on
  `{colors.canvas}` measures **4.09:1** against a 4.5:1 requirement. Orange
  links on cream fail AA. Underline them always, so colour is not the only
  cue, and prefer `{colors.primary-deep}` (**5.71:1**) for link text while
  keeping `#ea2804` for the CTA fill.
- `{colors.ash}` `#8d8d8d` on `{colors.canvas}` measures **3.10:1**. It is
  placeholder and tertiary text only — never body copy, never a label a task
  depends on.
- `{colors.stone}` `#bbbbbb` on `{colors.canvas}` measures **1.79:1**. Disabled
  foreground only, where WCAG sets no requirement.
- `{colors.divider-dark}` composites to `#4d4d4d` on `{colors.surface-dark}`
  (**1.93:1**) and `#333333` on `{colors.surface-deep}` (**1.66:1**). Decoration
  between footer rows; raising the alpha to 0.35 would clear 3:1 if a dark-surface
  divider ever has to carry structure.

### Focus ring

The extracted ring, `{colors.ring-focus}` `rgba(59,130,246,0.5)`, clears 3:1 on
**no** surface in this file: it composites to `#9abcf4` on `{colors.canvas}`
(**1.80:1**), `#9dc0fa` on `{colors.surface-card}` (**1.85:1**), `#2e518b` on
`{colors.surface-dark}` (**2.07:1**) and `#92557d` over the orange
`{component.hero-band}` (**1.26:1**). It is recorded as the extracted fact and
is not the recommendation.

Two rings replace it, both reusing tones this palette already owns rather than
introducing a colour — which matters for a brand whose stated rule is that
orange is the only accent:

- `{colors.focus}` `#202020` — the same ink as `{colors.ink}` and
  `{colors.hairline-strong}`. Drawn on the cream surfaces: `{colors.canvas}`
  **15.23:1**, `{colors.surface-bone}` **14.31:1**, `{colors.surface-card}`
  **16.29:1**. Against the orange `{component.hero-band}` it still reaches
  **3.73:1**.
- `{colors.focus-on-dark}` `#fcfcfc` — the same off-white as `{colors.on-dark}`.
  Drawn on the dark surfaces: `{colors.surface-dark}` **15.88:1**,
  `{colors.surface-deep}` **20.47:1**, and **4.26:1** over the hero orange.

Geometry: 2px ring at a 2px offset, drawn **outside** the control, so it is
judged against the surface behind the control rather than the control's own fill
— which is what WCAG 2.2 Focus Appearance measures and the only way a ring can
clear 3:1 next to a saturated `{colors.primary}` pill. Because every interactive
element is `{rounded.full}`, the ring follows the pill radius. Pick the ring by
the *ground*, not the control: a `{component.button-primary}` on cream takes
`{colors.focus}`; the same button inside `{component.pricing-tier-featured}` or
`{component.hero-band}` takes `{colors.focus-on-dark}`.

### Tap targets

Documented from the sizes this file already states; not measured on a rendered
page, so treat as the specification rather than a verified result.

- `{component.button-primary}`, `{component.button-dark}`,
  `{component.button-outline}` and `{component.text-input}` are 44px tall —
  clearing the 44x44px WCAG 2.5.5 AAA target.
- `{component.button-icon}` is 36px at desktop and is bumped to 44px on mobile
  via padding (Responsive Behavior). At desktop it meets 2.5.8 AA (24px) but not
  AAA.
- `{component.sub-nav-pill}` is 36px at desktop, 40px on mobile — AA, not AAA.
- `{component.contributor-avatar}` is 40px, below 44px. It links to a profile;
  the same link is reachable from the model card, so no task depends on hitting
  the avatar.

### Reduced motion

Every animation in Motion & Animation is honoured under
`@media (prefers-reduced-motion: reduce)`: all travel and all scale are removed,
opacity fades are capped at `{motion.duration-reduced}` (100ms), and the two
infinite animations — spinner rotation and skeleton pulse — are frozen. The
focus ring never had a transition, so it is unaffected.

### Non-colour cues

- The `{component.badge-status}` green and the error treatment both ship with a
  word ("running", "failed"); status is never colour alone.
- `{component.sub-nav-pill}` and `{component.badge-tag}` signal "selected" by
  flipping to the `{colors.surface-dark}` inversion, a luminance change rather
  than a hue change.
- Inline links carry a permanent underline, because `{colors.link}` on
  `{colors.canvas}` is 4.09:1 and cannot be the only signal.

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
| `{colors.link}` (`#ea2804`) on `{colors.canvas}` (`#f9f7f3`) | 4.09:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Use `{colors.canvas}` (cream) as the default page background. White (`{colors.surface-card}`) appears only on individual cards, inputs, and the hero illustration backdrop.
- Reserve `{colors.primary}` for the primary CTA, the home hero band, and inline links — three roles, nothing else.
- Set every interactive element to `{rounded.full}` — buttons, inputs, badges, avatars, pills.
- Step content cards up to `{rounded.md}` (10px) or `{rounded.lg}` (16px) — never sharp corners.
- Open hero bands with `{typography.display-xxl}` (128px) and `{typography.display-xl}` (72px) at `lineHeight: 1.0` with negative letter-spacing.
- Use `rb-freigeist-neue` for all display, `basier-square` for UI/body, `jetbrains-mono` for code. Keep the lanes strict.
- Render code in `{component.code-block}` with a `{colors.surface-dark}` background — code is print, not an inline grey box.
- Pair photography with `{rounded.md}` corners and full-bleed crop inside cards.
- Pick the focus ring by the ground it lands on: `{colors.focus}` on cream, `{colors.focus-on-dark}` on `{colors.surface-dark}`, `{colors.surface-deep}` and the orange hero band. 2px ring, 2px offset, outside the control.
- Keep state change immediate — `{motion.duration-fast}` on hover, `{motion.duration-instant}` on press. This is a tool, and a tool answers at once.

### Don't
- Don't replace cream with pure white at the page level. The brand temperature comes from `{colors.canvas}`.
- Don't introduce a secondary brand colour. Orange is the only accent; semantic green and focus blue are functional, not decorative.
- Don't loosen display `lineHeight` past 1.0. Tight stacking is structural.
- Don't bump body weight to 500 for emphasis — change family (`basier-square` → `rb-freigeist-neue`) instead.
- Don't apply `{rounded.full}` to content cards. Pill-shaped cards break the rhythm.
- Don't put code in a light grey box. Code wells are always `{colors.surface-dark}` or `{colors.surface-deep}`.
- Don't use orange on body text or large surfaces — it loses its stamp quality immediately.
- Don't add drop shadows on cream surfaces. Elevation is colour-blocking; shadows are reserved for floating thumbnails.
- Don't choreograph entrances. `{motion.stagger-step}` is 20ms and caps at 8 items; a model grid that unfolds is a grid that arrives late.
- Don't rely on `{colors.hairline}` to define a control's edge — at 1.27:1 it is decoration. Use `{colors.hairline-strong}`.
- Don't animate `width`, `height`, `top`, `left` or `margin`. Transform and opacity only.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop XL | ≥ 1440px | Full max-width 1280 body, hero band runs full-bleed, 4-up model grid. |
| Desktop | 1280–1439px | Container shrinks; padding `{spacing.xl}` (24px) sides. |
| Tablet Large | 1024–1279px | Model grid 3-up, code-story splits remain 2-up. |
| Tablet | 768–1023px | Model grid 2-up, code-story stacks (narrative on top, code below), pricing stacks vertically. |
| Mobile Large | 426–767px | Model grid 1-up at 480px+, nav collapses to hamburger, hero `{typography.display-xxl}` clamps to 64px. |
| Mobile | ≤ 425px | All grids 1-up, hero clamps to 48px, section padding `{spacing.section}` collapses to 64px. |

### Touch Targets
- All buttons ship at minimum 44px tall on mobile; default `{component.button-primary}` is 44px tall — comfortably clearing WCAG AAA.
- `{component.button-icon}` (36px) is bumped to 44px on mobile via increased padding.
- `{component.sub-nav-pill}` stays at 36px on desktop and grows to 40px on mobile via vertical padding adjustment.

### Collapsing Strategy
- Top-level nav collapses to hamburger at < 1024px; the wordmark and `{component.button-primary}` stay anchored.
- Hero `{typography.display-xxl}` clamps: 128px → 96px → 64px → 48px across the breakpoint ladder.
- Pricing 3-up grid stacks vertically at < 1024px with the featured tier remaining centre-stacked.
- Code-story splits switch from side-by-side to stacked at < 1024px, code well always second.
- Sub-nav pills convert from a wrap row to a horizontal scroll-rail at < 768px.

### Image Behavior
- Model thumbnails serve at 1.5× and 2× DPR; below 768px the system swaps to a 600×600 export instead of 1200×1200.
- Hero atmospheric mesh is rendered as a CSS gradient — no asset cost, no breakpoint variation.
- Code-block contents wrap softly at < 1024px (no horizontal scroll); long lines break with a continuation marker.

## Iteration Guide

1. Focus on ONE component at a time. Most interactive elements share `{rounded.full}` and the `{colors.canvas}` / `{colors.surface-card}` pair — only the role-specific tokens (`{colors.primary}`, `{component.code-block}`) shift between variants.
2. Reference component names and tokens directly (`{colors.primary}`, `{component.button-primary-pressed}`, `{rounded.lg}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits; orphaned-tokens warnings will catch unused entries.
4. Add new variants as separate entries (`-pressed`, `-disabled`, `-featured`) — do not bury them in prose.
5. Default body type to `{typography.body-md}`; reach for `{typography.subtitle}` only on hero subtitles.
6. Keep `{colors.primary}` scarce — if more than one orange element appears per viewport, ask whether one should drop to `{colors.surface-dark}` instead.

## Known Gaps

- Active/pressed visual states are documented for `button-primary-pressed` only; other components rely on the focus-ring (`{colors.ring-focus}`) for interactive feedback, which is not extracted as a per-component variant.
- The model playground / try-this-model interactive surfaces (logged-in feature) are out of scope; only the public marketing canvas is documented.
- Dashboard / billing / API key management surfaces are not extracted — those live behind authentication.
- The home hero illustration ("the tinkerer at the workbench") is treated as decorative artwork, not a system component; replicating it requires bespoke illustration rather than tokens.
- **Motion is prescribed, not extracted.** Every duration, easing and stagger in Motion & Animation comes from the Crisp profile in `theme-audit/SPEC.md`. Replicate's real timing functions were never measured. Anyone with access to the live site should overwrite the `motion:` group with observed values.
- **Most interaction states are prescribed.** Only `default`, the `button-primary-pressed` fill, and the `{component.code-tab}` active treatment are extracted. Every hover, focus-visible, disabled, loading, selected and error behaviour in Components is this audit's recommendation, built from tones the palette already owns.
- `{colors.focus}` and `{colors.focus-on-dark}` are role bindings added by this audit, reusing `#202020` and `#fcfcfc`. They are not new brand colours. The ring Replicate actually ships, `{colors.ring-focus}`, is retained and measured in Accessibility, where it fails 3:1 on every surface this file defines.
- Re-pointing `{component.text-input}`, `{component.button-icon}` and `{component.badge-tag}` from `{colors.hairline}` to `{colors.hairline-strong}` would fix a real 1.27:1 boundary failure but would make the document describe a product that does not ship. The extracted bindings are left as they are; the swap is recommended in Colors and is a brand-owner decision.
- `{colors.badge-success}` `#2b9a66` is only measured here as a fill behind `{colors.on-dark}` (3.46:1). No extracted sample shows the green used as text, so no text pairing is documented.
- Tap-target sizes are quoted from the heights this file states, not measured on a rendered page; overlap, overflow and clipping were not testable from a document.
