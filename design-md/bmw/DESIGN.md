---
version: alpha
name: BMW-design-analysis
description: BMW's corporate site — distinct from BMW M's motorsport-bombastic variant, this is a measured and settled corporate-automotive interface. On a light (cream-tinted white) canvas, BMW corporate blue (#1c69d4) carries every primary CTA; dark navy hero bands frame model photography. BMW Type Next Latin sets the entire hierarchy on two weights — heavy 700 display and Light 300 body. Configuration and reservation flows ride a card-based 4-up grid, where each card holds a model render, a name, and a "Learn More" link.

colors:
  primary: "#1c69d4"
  primary-active: "#0653b6"
  primary-disabled: "#d6d6d6"
  ink: "#262626"
  body: "#3c3c3c"
  body-strong: "#1a1a1a"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#e6e6e6"
  hairline-strong: "#cccccc"
  hairline-control: "#8a8a8a"
  focus: "#0a1929"
  focus-on-dark: "#ffffff"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#fafafa"
  surface-strong: "#ebebeb"
  surface-dark: "#1a2129"
  surface-dark-elevated: "#262e38"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-soft: "#bbbbbb"
  m-blue-light: "#0066b1"
  m-blue-dark: "#1c69d4"
  m-red: "#e22718"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#dc2626"

typography:
  display-xl:
    fontFamily: "'BMW Type Next Latin', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: 0
  display-lg:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  display-md:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  display-sm:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  label-uppercase:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  button:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'BMW Type Next Latin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  pill: 9999px
  full: 9999px

motion:
  duration-instant: 120ms
  duration-fast: 200ms
  duration-base: 400ms
  duration-slow: 600ms
  duration-emphasis: 900ms
  ease-standard: cubic-bezier(0.16, 1, 0.3, 1)
  ease-enter: cubic-bezier(0.05, 0.7, 0.1, 1)
  ease-exit: cubic-bezier(0.3, 0, 1, 1)
  stagger-step: 80ms

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px

components:
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 13px 31px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
  text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
  hero-band-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 80px
  hero-photo-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 80px
  model-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: 24px
  model-card-photo:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
  feature-photo-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: 24px
  spec-cell:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    padding: 24px
  inventory-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 16px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 8px 14px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  configurator-option-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 16px 24px
  configurator-option-tile-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 15px 23px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px 16px
    height: 48px
  cookie-consent-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 24px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
  m-stripe-divider:
    backgroundColor: transparent
    rounded: "{rounded.none}"
  cta-band-photo:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-md}"
    padding: 80px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 64px
---

## Overview

BMW's corporate site carries a far more **measured, corporate-automotive** interface than its motorsport-bombastic cousin BMW M. The atmosphere is light: `{colors.canvas}` (#ffffff) is the base surface, `{colors.surface-card}` (#fafafa) carries the soft-grey card plates, and dark navy `{colors.surface-dark}` (#1a2129) appears only inside hero bands — one per page, framing the lead model render.

Type runs BMW's licensed **BMW Type Next Latin** at two weights: heavy 700 (display + button + nav) and Light 300 (body + secondary copy). That contrast — heavy display next to thin paragraph — is the editorial signature, channeling the brand's "European-engineered" voice. Weight 500 is deliberately absent; weight 400 only appears on caption and nav-link in neutral utility contexts.

The brand action color, **BMW corporate blue** (`{colors.primary}` — #1c69d4), works alone across every primary CTA — buttons are **rectangular, 0px corner**, with white type. The site rotates a blue-button + dark-navy-hero combination across page rhythm. The M tricolor stripe (`{colors.m-blue-light}` → `{colors.m-blue-dark}` → `{colors.m-red}`) only appears in motorsport contexts and as M-model badges/dividers — never in the corporate site's main language.

The configuration and reservation flows add a dealer-side inventory UI on top of the same system — filter chips, model cards, price tables — but typography and color stay identical; only density goes up.

**Key Characteristics:**
- Light `{colors.canvas}` is the base surface; dark navy `{colors.surface-dark}` appears only inside hero bands — page rhythm relies on contrast.
- BMW corporate blue (`{colors.primary}` — #1c69d4) acts as the single primary action color.
- BMW Type Next Latin: weight 700 display against weight 300 body is the signature.
- Buttons are **rectangular, 0px radius** — corporate dialect, distinct from M's sportier radii.
- Model cards run as 4-up or 5-up grids with no hairline border or only minimal border — just white plate + photo + title.
- Photography (model renders) sits in environment, no shadow — depth comes entirely from color-block contrast.
- M tricolor stripe appears only in M-model contexts — not part of the corporate language.
- Section rhythm holds at `{spacing.section}` (80px) for every major band.

## Colors

### Brand & Accent
- **BMW Blue (Primary)** (`{colors.primary}` — #1c69d4): The single brand action color. All primary CTAs, "Learn More" link prefixes (blue text), nav-link active state. Press shifts to `{colors.primary-active}` (#0653b6).
- **M Blue Light** (`{colors.m-blue-light}` — #0066b1) + **M Blue Dark** (`{colors.m-blue-dark}` — #1c69d4) + **M Red** (`{colors.m-red}` — #e22718): The M tricolor stripe — appears on the corporate site only on M-model pages and the "M" badge. Never as CTA colors.

### Surface
- **Canvas** (`{colors.canvas}` — #ffffff): The default page surface.
- **Surface Soft** (`{colors.surface-soft}` — #f7f7f7): Soft grey for the footer and sub-navigation bands.
- **Surface Card** (`{colors.surface-card}` — #fafafa): The light plate behind a model card's photo block.
- **Surface Strong** (`{colors.surface-strong}` — #ebebeb): A slightly heavier grey used as a section divider.
- **Surface Dark** (`{colors.surface-dark}` — #1a2129): Dark navy for hero bands and large dark CTAs. Not pure black — carries a warm undertone.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — #262e38): One step lighter, used for nested cards on top of the dark hero.

### Hairlines
- **Hairline** (`{colors.hairline}` — #e6e6e6): The 1px divider — table separator, configurator card outline. **Decoration only.** At 1.25:1 on `{colors.canvas}` it is not a perceivable boundary; never let it be the sole outline of an interactive control.
- **Hairline Strong** (`{colors.hairline-strong}` — #cccccc): The extracted "more visible" 1px outline — secondary buttons, emphasized table border. Measures **1.61:1 on `{colors.canvas}`**, below the 3:1 WCAG 1.4.11 non-text-contrast threshold. **The real BMW corporate site fails AA on control boundaries at this point.** The value is left unchanged because it is an extracted fact.
- **Hairline Control** (`{colors.hairline-control}` — #8a8a8a): **Prescribed, not extracted.** A parallel accessible boundary at **3.45:1 on `{colors.canvas}`**, for any border that is the only boundary of an interactive control — `{component.text-input}`, `{component.button-secondary}`, `{component.filter-chip}`. Use `{colors.hairline-strong}` where the border is decorative and a label or fill already carries the affordance. It holds at 3.22:1 on `{colors.surface-soft}` and 3.31:1 on `{colors.surface-card}`, but drops to **2.90:1 on `{colors.surface-strong}`** — do not place a bordered control on the #ebebeb divider band.

### Focus
- **Focus** (`{colors.focus}` — #0a1929): **Prescribed, not extracted** — no file in this repo documented a focus ring. A 2px deep-navy ring drawn from the `{colors.surface-dark}` family, offset 2px from the control so its backdrop is always the light surface beneath, never the control fill. Measures **17.74:1 on `{colors.canvas}`**, 16.56:1 on `{colors.surface-soft}`, 14.88:1 on `{colors.surface-strong}`, and 3.40:1 directly over `{colors.primary}`. A blue ring was rejected: `{colors.primary-active}` on `{colors.primary}` measures 1.38:1, so BMW blue cannot ring its own button.
- **Focus On Dark** (`{colors.focus-on-dark}` — #ffffff): **Prescribed.** The ring on dark bands, where `{colors.focus}` collapses to 1.09:1. Measures 16.24:1 on `{colors.surface-dark}` and 13.72:1 on `{colors.surface-dark-elevated}`.

### Text
- **Ink** (`{colors.ink}` — #262626): All display and primary text. Not pure black — soft against photography.
- **Body** (`{colors.body}` — #3c3c3c): Default running text.
- **Body Strong** (`{colors.body-strong}` — #1a1a1a): Emphasized paragraphs and lead text.
- **Muted** (`{colors.muted}` — #6b6b6b): Footer links, breadcrumbs, captions.
- **Muted Soft** (`{colors.muted-soft}` — #9a9a9a): Disabled text, fine-print legal.
- **On Primary** (`{colors.on-primary}` — #ffffff): White text on a blue button.
- **On Dark** (`{colors.on-dark}` — #ffffff): White text on a dark hero band.
- **On Dark Soft** (`{colors.on-dark-soft}` — #bbbbbb): A slightly muted white for secondary text on dark bands.

### Semantic
- **Success** (`{colors.success}` — #22c55e): Confirmation messages and "available" indicators. **2.28:1 on `{colors.canvas}` — fails AA as text.** Fill, icon and bar role only; the message text beside it must be `{colors.body}`.
- **Warning** (`{colors.warning}` — #f59e0b): Warning callouts. **2.15:1 on `{colors.canvas}` — fails AA as text.** Same restriction as success.
- **Error** (`{colors.error}` — #dc2626): Validation errors. 4.83:1 on `{colors.canvas}` — passes AA for body text. Note it drops to 4.51:1 on `{colors.surface-soft}`, barely at threshold.
- **Muted Soft** (`{colors.muted-soft}` — #9a9a9a) measures **2.81:1 on `{colors.canvas}` and fails AA at any size.** It is extracted and unchanged; see Accessibility.

## Typography

### Font Family
The system runs **BMW Type Next Latin** in two cuts: regular (display + UI labels) and **BMW Type Next Latin Light** (body + secondary copy). Fallback stack: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.

The display/body split is functional:
- BMW Type Next Latin (700) → display headlines, button labels, nav links
- BMW Type Next Latin Light (300) → paragraphs, descriptive copy
- BMW Type Next Latin (400) → caption, neutral nav-link contexts

This three-way split mirrors BMW M's — corporate and the M sub-brand share the same typographic DNA; only the weight/size ratios differ.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 64px | 700 | 1.05 | 0 | Hero h1 ("iX3", model name) |
| `{typography.display-lg}` | 48px | 700 | 1.1 | 0 | Section heads |
| `{typography.display-md}` | 32px | 700 | 1.15 | 0 | Sub-section heads |
| `{typography.display-sm}` | 24px | 700 | 1.25 | 0 | CTA-band headlines |
| `{typography.title-lg}` | 20px | 700 | 1.3 | 0 | Card group titles |
| `{typography.title-md}` | 18px | 700 | 1.4 | 0 | Model card title, intro paragraphs |
| `{typography.title-sm}` | 16px | 700 | 1.4 | 0 | Inventory card title, list label |
| `{typography.body-md}` | 16px | 300 (Light) | 1.55 | 0 | Default body — BMW Type Next Latin Light |
| `{typography.body-sm}` | 14px | 300 (Light) | 1.55 | 0 | Footer body, fine-print |
| `{typography.caption}` | 12px | 400 | 1.4 | 0.5px | Photo captions, meta |
| `{typography.label-uppercase}` | 13px | 700 | 1.3 | 1.5px | "LEARN MORE" inline links, category tabs |
| `{typography.button}` | 14px | 700 | 1.0 | 0.5px | Standard CTA button label |
| `{typography.nav-link}` | 14px | 400 | 1.4 | 0.3px | Top-nav menu items |

### Principles
- The **700/300 contrast** is the editorial signature. Weight 500 is absent from the system.
- **No negative letter-spacing** — BMW Type Next Latin works on a wide body, so tracking stays at default. Apple/Cal.com-style tightening reads off-brand here.
- **UPPERCASE inline links** — "LEARN MORE"-style CTAs run uppercase with 1.5px tracking. The "machined precision" voice.
- **Weight 400 lives in a narrow lane** — only caption and nav-link, both neutral utility roles.

### Note on Font Substitutes
BMW Type Next Latin is a licensed BMW typeface. Open-source alternatives:
- **Inter** (variable) — close match at weight 700/300. Leave letter-spacing at 0.0em.
- **Saira Condensed** — for a slightly more compressed BMW Type feel.

## Layout

### Spacing System
- **Base unit:** 8px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- **Section padding:** `{spacing.section}` (80px) for every major editorial band.
- **Card internal padding:** `{spacing.lg}` (24px) for model and feature cards.

### Grid & Container
- **Max content width:** ~1440px center-aligned.
- **Editorial body:** A single 12-column grid.
- **Model card grids:** 4-up or 5-up at desktop, 2-up at tablet, 1-up on mobile.
- **Configurator inventory grids:** 3-up filter row + 4-up vehicle cards, dense layout.

### Whitespace Philosophy
BMW's whitespace strategy is tighter than BMW M's motorsport-aerated grenadier — the corporate side is more utility-driven. Section rhythm is 80px (not M's 96px). Card padding is 24px (not M's 32px). The page is denser, more dealership-functional.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body, top nav, footer, hero bands |
| Soft hairline | 1px `{colors.hairline}` border | Configurator option tile, table divider |
| Card surface | `{colors.surface-card}` background — no shadow | Model card photo plate |
| Photographic | Edge-to-edge photography | Hero band, model renders |

The system never uses a drop shadow. Depth comes entirely from (a) color-block contrast (light canvas vs dark hero) and (b) photographic subject + lighting.

### Decorative Depth
- **`m-stripe-divider`** — a 4px-tall horizontal tricolor stripe (`{colors.m-blue-light}` → `{colors.m-blue-dark}` → `{colors.m-red}`). Only in M-model contexts, motorsport badges, or as an M-related section divider. Not part of the main corporate flow.
- **Photographic depth** — full-bleed vehicle photography (lighting + subject) does the work chrome would otherwise do.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Every button, card, input, configurator chip — the dominant radius |
| `{rounded.xs}` | 2px | Very small badges, very rare |
| `{rounded.sm}` | 4px | Small inline button (rare) |
| `{rounded.md}` | 8px | Mobile-only collapse cards (rare) |
| `{rounded.lg}` | 12px | Very rare — modal/dialog corners |
| `{rounded.pill}` | 9999px | Filter chips in some contexts (rare) |
| `{rounded.full}` | 9999px / 50% | Avatar, circular icon button |

The radius hierarchy is binary: **rectangular for everything, circular only for icon buttons.** A clear departure from the soft-cornered SaaS dialect of Apple or Cal.com — closer to BMW corporate-automotive's "engineered precision" voice.

### Photography Geometry
- Hero photography is full-bleed at 16:9 or 21:9 cinematic ratio.
- Model card photos sit at 16:10, edge-to-edge with `{rounded.none}` corners.
- Configurator vehicle renders sit on a white studio background, full silhouette visible.

## Components

### Top Navigation

**`top-nav`** — A white sticky nav bar pinned to the top of the page. 64px tall, `{colors.canvas}` background. Left: BMW circular badge logo; center: primary horizontal menu (Models, Next Generation, Pre-Owned, Dealers, Test Drive); right: cart icon, language picker, profile. Menu items render in `{typography.nav-link}` (14px / 400 / 0.3px tracking).

### Buttons

**`button-primary`** — The signature primary CTA. Background `{colors.primary}` (BMW Blue #1c69d4), text `{colors.on-primary}`, type `{typography.button}` (BMW Type Next Latin 14px / 700 / 0.5px tracking), padding 14px × 32px, height 48px, rounded `{rounded.none}` (0px — rectangular). Press state: `button-primary-active` shifts to `{colors.primary-active}`.

**`button-secondary`** — A white button with a hairline outline. Background `{colors.canvas}`, text `{colors.ink}`, same padding + height + radius. The extracted border is 1px `{colors.hairline-strong}` (1.61:1 — fails WCAG 1.4.11); use 1px `{colors.hairline-control}` (3.45:1) where the outline is the only thing making the button a button.

**`button-secondary-on-dark`** — Used over a dark hero band. Background transparent, text `{colors.on-dark}`, 1px `{colors.on-dark}` border, same rectangular shape.

**`button-text-link`** — An inline UPPERCASE letter-spaced link. No background, text `{colors.ink}`, type `{typography.label-uppercase}` (13px / 700 / 1.5px tracking). Reads as "LEARN MORE", terminated by a `›` chevron.

**`text-link`** — An inline link inside body copy. `{colors.ink}` text, no underline by default; underlines per context.

### Cards & Containers

**`hero-band-dark`** — Full-width dark navy hero. Background `{colors.surface-dark}`, text `{colors.on-dark}`, vertical padding `{spacing.section}` (80px). Centered: model name in `{typography.display-xl}` (64px / 700) + sub-headline + vehicle render (right-aligned or below). A single `{component.button-primary}` (blue) or `{component.button-secondary-on-dark}`.

**`hero-photo-band`** — A light-canvas model showcase band. Background `{colors.canvas}`, text `{colors.ink}`. The vehicle render takes the wide area; right or below, a headline + two link CTAs + sub-tagline.

**`model-card`** — Used in 4-up or 5-up model card grids on the homepage ("BMW iX3", "BMW iX", "BMW 5 Series"). Background `{colors.canvas}`, rounded `{rounded.none}`, padding `{spacing.lg}` (24px). Contents: model render at the top (`{component.model-card-photo}` on `{colors.surface-card}`), model name in `{typography.title-md}` (18px / 700) below, a one-line tagline in `{typography.body-sm}` (14px / 300), and a `{component.button-text-link}` ("LEARN MORE ›").

**`model-card-photo`** — The card's photo plate. Background `{colors.surface-card}` (#fafafa — soft grey), rounded `{rounded.none}`, vehicle render in full silhouette. Zero padding — the photo runs edge-to-edge.

**`feature-photo-card`** — A feature/lifestyle card. Background `{colors.canvas}`, padding `{spacing.lg}`. 16:9 photo at the top, `{typography.title-md}` headline + body excerpt below.

**`spec-cell`** — A technical spec cell (model detail page). Transparent background, separated by hairline dividers. Value on top (`{typography.display-sm}` 24px / 700), label below (`{typography.label-uppercase}`).

### Inventory & Configurator

**`inventory-card`** — One card per vehicle on the dealer inventory page. Background `{colors.canvas}`, padding `{spacing.md}` (16px), rounded `{rounded.none}`. Vehicle photo on top, model + variant name + price + "View" link below.

**`filter-chip`** + **`filter-chip-active`** — Inventory filter chips (model, year, price range). Inactive: background `{colors.canvas}`, 1px border — `{colors.hairline-strong}` as extracted, `{colors.hairline-control}` where the chip's outline is its only boundary — text `{colors.ink}`, type `{typography.caption}`. Active: background `{colors.ink}`, text `{colors.on-dark}`. Padding 8px × 14px, radius `{rounded.none}`.

**`configurator-option-tile`** + **`configurator-option-tile-selected`** — Configurator selection cell (color, wheels, upholstery). Inactive: background `{colors.canvas}`, 1px hairline. Selected: 2px `{colors.primary}` border. Padding 16px × 24px, radius `{rounded.none}`.

### Inputs & Forms

**`text-input`** — Standard text input. Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, rounded `{rounded.none}` (0px), padding 14px × 16px, height 48px, 1px border. The extracted border is `{colors.hairline}` (1.25:1), which is not a perceivable boundary for the only outline of a form field; use 1px `{colors.hairline-control}` (3.45:1) instead. On focus the border thickens to ink and a 2px `{colors.focus}` ring sits 2px outside it.

**`cookie-consent-card`** — Cookie banner. Background `{colors.canvas}`, 1px hairline, padding `{spacing.lg}` (24px), `{typography.body-sm}` (14px / 300 — Light even in legal copy).

### Tabs / Tags

**`category-tab`** + **`category-tab-active`** — Category sub-nav. Inactive: transparent + `{colors.muted}` UPPERCASE label. Active: transparent + `{colors.ink}` UPPERCASE label + 2px ink underline. 12px vertical padding, no horizontal radius.

### Brand Signature

**`m-stripe-divider`** — A 4px-tall horizontal tricolor stripe (`{colors.m-blue-light}` → `{colors.m-blue-dark}` → `{colors.m-red}`). Only in M-model contexts, motorsport badges, or as an M-related section divider. Absent from the corporate main flow; on M-model detail pages and the M Performance badge it plays an inline divider role.

### CTA / Footer

**`cta-band-photo`** — A pre-footer "Discover the New iX3"-style band. Background `{colors.surface-dark}` with a full-bleed vehicle photo. Centered headline in `{typography.display-md}` (32px / 700) + a single `{component.button-secondary-on-dark}`. 80px padding.

**`footer`** — The closing soft-grey footer. Background `{colors.surface-soft}` (#f7f7f7 — not pure white — soft grey), text `{colors.body}`. A 4-column link list: Models / Services / Dealers / About. Vertical padding 64px. Below, a copyright line in `{typography.body-sm}` with `{colors.muted}`.

### Component States

Default, active/pressed, selected and disabled are extracted from the live site (they exist as separate `components:` entries or as documented border/fill shifts). **Hover, focus-visible, loading and error are prescribed** — the corporate site was captured statically and these were never observed; see Known Gaps.

| Component | States |
|---|---|
| `top-nav` | default · hover (link ink darkens to `{colors.body-strong}`) · focus-visible (2px `{colors.focus}` ring) · active/pressed · selected (current section, 2px ink underline). No disabled, loading or error state. |
| `button-primary` | default · hover (fill holds `{colors.primary}`, 4% ink overlay) · focus-visible (2px `{colors.focus}` ring, 2px offset on `{colors.canvas}`) · pressed → `button-primary-active` `{colors.primary-active}` · disabled → `button-primary-disabled` `{colors.primary-disabled}` with `{colors.muted}` label · loading (label swaps to a 1.2s indeterminate bar, button width frozen). No error state. |
| `button-secondary` | default · hover (border to `{colors.ink}`) · focus-visible (2px `{colors.focus}` ring) · pressed (fill `{colors.surface-strong}`) · disabled (border `{colors.hairline-strong}`, label `{colors.muted-soft}`) · loading. No error state. |
| `button-secondary-on-dark` | default · hover (border to `{colors.on-dark}` at full opacity) · focus-visible (2px `{colors.focus-on-dark}` ring) · pressed · disabled (`{colors.on-dark-soft}` border and label). No loading or error state. |
| `button-text-link` / `text-link` | default · hover (underline appears) · focus-visible (2px `{colors.focus}` ring around the text box) · active/pressed. Three states plus focus; no disabled, loading, selected or error state. |
| `model-card` / `feature-photo-card` / `inventory-card` | default · hover (photo scales 1.03, `{component.button-text-link}` underline appears) · focus-visible (ring on the whole card, the card being one link target) · active/pressed · loading (skeleton plate on `{colors.surface-card}`). No disabled, selected or error state. |
| `filter-chip` | default · hover (border `{colors.ink}`) · focus-visible · active/pressed · selected → `filter-chip-active` (`{colors.ink}` fill) · disabled (no inventory matches: label `{colors.muted-soft}`, border `{colors.hairline-strong}`) · loading (chip count placeholder). No error state. |
| `configurator-option-tile` | default · hover (border `{colors.ink}`) · focus-visible · active/pressed · selected → `configurator-option-tile-selected` (2px `{colors.primary}` border) · disabled (option not available on trim) · loading (render swap in progress). No error state. |
| `text-input` | default · hover (border `{colors.ink}`) · focus-visible (border ink + 2px `{colors.focus}` ring) · active/pressed · disabled (`{colors.surface-soft}` fill, `{colors.muted-soft}` text) · error (1px `{colors.error}` border plus a `{typography.body-sm}` message in `{colors.body}` — never colour-only) · loading (async validation spinner in the trailing slot). No selected state. |
| `category-tab` | default · hover (label to `{colors.ink}`) · focus-visible · active/pressed · selected → `category-tab-active` (ink label + 2px ink underline) · disabled. No loading or error state. |
| `cookie-consent-card` | A static container: default only, plus focus-visible on its own buttons. No hover, pressed, disabled, loading, selected or error state of its own. |
| `hero-band-dark` / `hero-photo-band` / `cta-band-photo` / `footer` / `spec-cell` / `m-stripe-divider` / `model-card-photo` | Static, non-interactive: **default only.** States belong to the controls nested inside them. |

## Motion & Animation

**This motion system is prescribed to match BMW's visual identity and was not measured from the live site.** No timing function, duration or easing curve below was extracted; nothing here should be cited as an observed BMW value. The profile assigned is **Cinematic** — slow, deliberate, premium — which fits an automotive flagship whose page rhythm is built on full-bleed vehicle photography and dark hero bands, even though BMW's own canvas is light rather than dark.

The Cinematic reading of BMW corporate is deliberately the *restrained* one, matching the file's "measured and settled" corporate voice rather than BMW M's motorsport cut: travel distances stay short (16–24px), scale changes stay under 1.04, and the premium feel comes from the long decelerate of `{motion.ease-standard}` rather than from large movement.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, chip, tab, link) | `{motion.duration-fast}` 200ms | `{motion.ease-standard}` | `opacity`, `transform` (no travel; overlay opacity only) | Colour/border change applies instantly; no transition |
| Hover (card photo) | `{motion.duration-base}` 400ms | `{motion.ease-standard}` | `transform: scale(1 → 1.03)` | Scale removed entirely; photo stays at 1.0 |
| Press | `{motion.duration-instant}` 120ms | `{motion.ease-exit}` | `opacity` (fill shift to `{colors.primary-active}`), `transform: scale(0.99)` | Scale removed; fill shift instant |
| Focus (ring appear) | `{motion.duration-instant}` 120ms | `{motion.ease-enter}` | `opacity` on the `{colors.focus}` ring | Ring appears instantly at full opacity — never suppressed |
| Page / route transition | `{motion.duration-slow}` 600ms in, `{motion.duration-base}` 400ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` 0→1, `transform: translateY(24px → 0)` on the content column | Travel removed; cross-fade only, capped at 150ms |
| Modal / drawer (mobile nav sheet) | `{motion.duration-base}` 400ms in, `{motion.duration-fast}` 200ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `transform: translateX(100% → 0)`, scrim `opacity` | Slide removed; scrim and panel fade at 150ms |
| Dropdown (language picker, nav mega-menu) | `{motion.duration-fast}` 200ms in, `{motion.duration-instant}` 120ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: translateY(-8px → 0)` | Travel removed; 120ms opacity fade |
| Toast (configurator confirmation) | `{motion.duration-base}` 400ms in, `{motion.duration-fast}` 200ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: translateY(16px → 0)` | Travel removed; 150ms fade, hold time unchanged |
| List enter (model-card grid, inventory results) | `{motion.duration-slow}` 600ms per item, `{motion.stagger-step}` 80ms apart | `{motion.ease-enter}` | `opacity`, `transform: translateY(24px → 0)` | Stagger and travel removed; the whole grid fades in once at 150ms |
| List exit (filtered-out inventory cards) | `{motion.duration-base}` 400ms, no stagger | `{motion.ease-exit}` | `opacity` 1→0, `transform: scale(0.98)` | Scale removed; 150ms fade |
| Loading (indeterminate bar, configurator render swap) | 1200ms loop | `{motion.ease-standard}` | `transform: translateX` on a 2px `{colors.primary}` bar | Loop frozen; a static `{colors.primary}` bar plus the text "Loading" remains |
| Emphasis — hero vehicle settle on first paint | `{motion.duration-emphasis}` 900ms | `{motion.ease-standard}` | `transform: scale(1.04 → 1)` on the hero photograph, `opacity` on the headline arriving one `{motion.stagger-step}` later | Removed entirely; hero renders at its final position |

### Rules

- Never animate `width`, `height`, `top`, `left` or `margin`: `transform` and `opacity` only. The 0px-radius rectangles in this system have no shape transitions to make.
- Every exit is shorter than its matching entrance (600/400 page, 400/200 drawer and toast, 200/120 dropdown).
- Nothing animates on first paint in a way that delays content: the hero emphasis runs on an already-painted photograph, and type is readable before it settles.
- The only infinite animation is the loading bar. There is **no brand ambience loop** — BMW corporate's depth comes from photography and colour-block contrast, not from motion.
- The M tricolor stripe never animates. It is a static 4px rule in every state and breakpoint.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale — hero settle, card photo scale,
     page-transition travel, drawer slide, dropdown and toast travel,
     list-enter stagger, press scale. */
  /* Removed: the list-enter stagger ({motion.stagger-step}) in full;
     grids appear as one. */
  /* Frozen: the loading bar loop — a static bar plus a text label remains. */
  /* Kept: opacity fades, clamped to 150ms or less. */
  /* Kept at full strength: the {colors.focus} and {colors.focus-on-dark}
     focus rings, which appear instantly and are never animated away. */
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important;
    transition-property: opacity, color, background-color, border-color !important;
    scroll-behavior: auto !important;
  }
}
```

## Accessibility

Every ratio below was computed from this file's own hexes with the WCAG 2.1 relative-luminance formula. Claims that need a rendered page — overlap, clipping, real tap-target size, frame rate — are not made here.

### Measured contrast

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` #262626 / `{colors.canvas}` #ffffff | 15.13:1 | 4.5 | Pass |
| `{colors.ink}` / `{colors.surface-soft}` #f7f7f7 | 14.13:1 | 4.5 | Pass |
| `{colors.ink}` / `{colors.surface-card}` #fafafa | 14.50:1 | 4.5 | Pass |
| `{colors.body}` #3c3c3c / `{colors.canvas}` | 11.03:1 | 4.5 | Pass |
| `{colors.muted}` #6b6b6b / `{colors.canvas}` | 5.33:1 | 4.5 | Pass |
| `{colors.muted}` / `{colors.surface-soft}` | 4.97:1 | 4.5 | Pass — the footer's own pairing |
| `{colors.muted-soft}` #9a9a9a / `{colors.canvas}` | 2.81:1 | 4.5 | **Fail** |
| `{colors.on-primary}` #ffffff / `{colors.primary}` #1c69d4 | 5.22:1 | 4.5 | Pass |
| `{colors.on-primary}` / `{colors.primary-active}` #0653b6 | 7.19:1 | 4.5 | Pass |
| `{colors.on-dark}` #ffffff / `{colors.surface-dark}` #1a2129 | 16.24:1 | 4.5 | Pass |
| `{colors.on-dark-soft}` #bbbbbb / `{colors.surface-dark}` | 8.46:1 | 4.5 | Pass |
| `{colors.on-dark-soft}` / `{colors.surface-dark-elevated}` #262e38 | 7.15:1 | 4.5 | Pass |
| `{colors.hairline}` #e6e6e6 / `{colors.canvas}` | 1.25:1 | 3.0 | **Fail** — scoped to decoration |
| `{colors.hairline-strong}` #cccccc / `{colors.canvas}` | 1.61:1 | 3.0 | **Fail** — extracted, left unchanged |
| `{colors.hairline-control}` #8a8a8a / `{colors.canvas}` | 3.45:1 | 3.0 | Pass — prescribed replacement |
| `{colors.focus}` #0a1929 / `{colors.canvas}` | 17.74:1 | 3.0 | Pass |
| `{colors.focus}` / `{colors.primary}` | 3.40:1 | 3.0 | Pass |
| `{colors.focus-on-dark}` #ffffff / `{colors.surface-dark}` | 16.24:1 | 3.0 | Pass |
| `{colors.m-blue-light}` #0066b1 / `{colors.canvas}` | 5.94:1 | 4.5 | Pass |
| `{colors.m-red}` #e22718 / `{colors.canvas}` | 4.63:1 | 4.5 | Pass |
| `{colors.error}` #dc2626 / `{colors.canvas}` | 4.83:1 | 4.5 | Pass |
| `{colors.success}` #22c55e / `{colors.canvas}` | 2.28:1 | 4.5 | **Fail** — non-text use only |
| `{colors.warning}` #f59e0b / `{colors.canvas}` | 2.15:1 | 4.5 | **Fail** — non-text use only |

**Real failures, stated plainly.** BMW corporate's extracted hairlines (#e6e6e6 at 1.25:1, #cccccc at 1.61:1) do not meet WCAG 1.4.11 for a component boundary, so the real site's secondary buttons, filter chips and text inputs have no perceivable outline. `{colors.muted-soft}` (#9a9a9a, 2.81:1) fails AA for text at every size, including the fine-print legal copy it is used for; the nearest passing value on `{colors.canvas}` is #767676 (4.54:1), and #949494 (3.03:1) is the floor for 18px+ or 14px-bold text under the AA large-text rule. `{colors.success}` and `{colors.warning}` fail as text and are usable only as fills, icons and bars with a `{colors.body}` label beside them. None of these hexes has been altered; they are extracted facts about the brand.

### Focus ring visibility, surface by surface

| Surface | Ring token | Ratio |
|---|---|---|
| `{colors.canvas}` #ffffff | `{colors.focus}` | 17.74:1 |
| `{colors.surface-soft}` #f7f7f7 | `{colors.focus}` | 16.56:1 |
| `{colors.surface-card}` #fafafa | `{colors.focus}` | 16.99:1 |
| `{colors.surface-strong}` #ebebeb | `{colors.focus}` | 14.88:1 |
| `{colors.primary}` #1c69d4 (ring crossing a blue fill) | `{colors.focus}` | 3.40:1 |
| `{colors.surface-dark}` #1a2129 | `{colors.focus-on-dark}` | 16.24:1 |
| `{colors.surface-dark-elevated}` #262e38 | `{colors.focus-on-dark}` | 13.72:1 |

The ring is drawn 2px **outside** the control so its backdrop is the surface, not the fill: `{colors.focus}` over `{colors.primary-active}` would be only 2.47:1, which is why the offset is part of the token's definition rather than a suggestion. On any dark band — `{component.hero-band-dark}`, `{component.cta-band-photo}` — switch to `{colors.focus-on-dark}`; `{colors.focus}` collapses to 1.09:1 there.

### Other

- **Minimum tap target:** the system's documented control heights are 48px (`{component.button-primary}`, `{component.button-secondary}`, `{component.text-input}`), clearing the 44 × 44px target. `{component.filter-chip}` at 8px vertical padding on 12px `{typography.caption}` computes to roughly 33px tall, **below 44px** — it needs 14px vertical padding or an expanded hit area. Actual rendered size is not verifiable from this document.
- **Colour is never the only signal:** `{component.text-input}` error state pairs the `{colors.error}` border with a text message; `{component.filter-chip-active}` and `{component.category-tab-active}` pair their fill or label change with a shape change (fill inversion, 2px underline).
- **Reduced motion:** honoured in full — see the `@media (prefers-reduced-motion: reduce)` block above. Travel and scale are removed, opacity fades clamp to 150ms, the loading loop freezes, and focus rings are untouched.
- **Type size floor:** `{typography.caption}` at 12px and `{typography.body-sm}` at 14px/300 are the smallest roles. A 300 weight at 14px on `{colors.muted-soft}` is the worst legibility case in the system and should not be used for anything a user must read.

## Do's and Don'ts

### Do
- Sit every page on `{colors.canvas}` (pure white); reserve `{colors.surface-dark}` for hero bands only.
- Pair primary CTAs with `{colors.primary}` (BMW Blue) + `{colors.on-primary}` white text + `{rounded.none}` 0px corners — the corporate signature.
- Set display headlines in BMW Type Next Latin 700 and body in Light 300. The contrast is non-negotiable.
- Use UPPERCASE letter-spaced links like "LEARN MORE" as inline CTAs.
- Place the model card photo on `{colors.surface-card}` with the title beneath — the standard BMW corporate pattern.
- Hold section rhythm at `{spacing.section}` (80px) — tighter than BMW M's 96px.
- Reserve the M tricolor stripe for M-model contexts and motorsport dividers.
- Draw focus with `{colors.focus}` on light surfaces and `{colors.focus-on-dark}` on hero bands, always 2px outside the control.
- Keep motion slow and short: `{motion.duration-base}` with `{motion.ease-standard}`, under 24px of travel. Premium reads as deliberate, not as large.

### Don't
- Don't add a brand color other than blue — BMW Blue is the only primary action color.
- Don't use pill or rounded buttons — `{rounded.none}` (0px) rectangular IS the brand button.
- Don't drop display weight to 500 — the system uses 700 / 400 / 300; 500 is absent.
- Don't bold body type — Light 300 is the BMW corporate editorial voice.
- Don't add drop shadows to cards — depth comes from photo + color-block contrast.
- Don't repeat the same surface mode across two consecutive bands — light → dark hero → light → light feature → dark CTA → light footer rotation is required.
- Don't use the M tricolor stripe as a CTA fill — divider/accent role only.
- Don't mix languages in a single page — UI language must stay consistent.
- Don't let `{colors.hairline}` or `{colors.hairline-strong}` be the only boundary of an interactive control — use `{colors.hairline-control}`.
- Don't suppress the focus ring under `prefers-reduced-motion`, and don't animate `width`, `height`, `top`, `left` or `margin` anywhere in this system.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav; hero h1 64→40px; model card grid 1-up; configurator filter chips 2-up; footer 4 col → 1 col |
| Tablet | 768–1024px | Top nav narrows, secondary menu hides under "More"; model card 2-up; inventory 2-up |
| Desktop | 1024–1440px | Full top-nav; 4-up or 5-up model card grid; inventory 3-up; full configurator UI |
| Wide | > 1440px | Same as desktop, content fixed at 1440px; gutters absorb the rest |

### Touch Targets
- `{component.button-primary}` minimum 48 × 48px — above WCAG AAA (44 × 44).
- `{component.text-input}` height 48px.
- Category tabs run with 12px vertical padding, giving an effective tap area > 44px.

### Collapsing Strategy
- The top nav collapses to a hamburger below 768px; the menu opens as a full-screen sheet.
- The hero band's internal layout drops to a single column.
- Model card grid 4-up/5-up → 2-up → 1-up.
- The configurator filter chip row scrolls horizontally on mobile.
- The M tricolor stripe stays at 4px height across every breakpoint.

### Image Behavior
- Model renders scale at every breakpoint while preserving native aspect ratios.
- Hero photography may shift to a more vertical crop on mobile (art direction).
- Inventory vehicle photos may move from 16:9 to 4:3 on mobile.

## Iteration Guide

1. Focus on a single component. Reference its YAML key directly (`{component.model-card}`, `{component.button-primary}`).
2. New components default to `{rounded.none}` (0px). Use `{rounded.full}` only for circular icon buttons.
3. Variants (`-active`, `-disabled`, `-selected`) live as separate entries inside the `components:` block.
4. `{token.refs}` everywhere — never inline hex.
5. Only Default, Active/Pressed, Selected and Disabled were extracted. Hover, focus-visible, loading and error are prescribed in the Component States table — treat them as the system's intent, not as observed BMW behaviour.
6. Display headlines stay BMW Type Next Latin 700; body stays Light 300; the trio is fixed.
7. Keep UI strings in a single language — match the locale of the page.

## Known Gaps

- BMW Type Next Latin is licensed to BMW and not published as a public web font; Inter at weights 700/300 is documented as the substitute.
- Animation and transition timings (configurator colour swap, model card hover-reveal) were never measured from the live site. The Motion & Animation section is a **prescribed Cinematic profile**, not an extracted one.
- Form validation states beyond `{component.text-input}` focus were not extracted — the error and loading states in the Component States table are prescribed and would need a dedicated form page to confirm.
- `{colors.focus}`, `{colors.focus-on-dark}` and `{colors.hairline-control}` are prescribed tokens. No focus ring was observed on the captured pages, and no accessible control boundary exists in the extracted palette.
- Tap-target size, overlap and clipping cannot be verified from a static document. The `{component.filter-chip}` height is a computed estimate from its padding and type size, not a measurement.
- The dealer inventory sub-domain shares typography and color with the main corporate site; only UI density rises (filters, tables, prices).
- A cookie consent overlay can occlude part of the hero — the lead hero band content may not be fully captured.
- The M tricolor stripe appears infrequently on this corporate site; full motorsport context lives on the BMW M site.
