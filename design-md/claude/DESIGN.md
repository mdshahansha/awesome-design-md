---
version: alpha
name: Claude-design-analysis
description: A warm-canvas editorial interface for Anthropic's Claude product. The system anchors on a tinted cream canvas with serif display headlines, warm coral CTAs, and dark navy product surfaces (code editor mockups, model showcase cards). Brand voltage comes from the cream/coral pairing — deliberately warm and humanist where most AI brands use cool blue + slate. Type voice runs a slab-serif display ("Copernicus" / Tiempos Headline) for h1/h2 and a humanist sans for body. The signature Anthropic black-radial-spike mark anchors the wordmark.

colors:
  primary: "#cc785c"
  primary-active: "#a9583e"
  primary-disabled: "#e6dfd8"
  ink: "#141413"
  body: "#3d3d3a"
  body-strong: "#252523"
  muted: "#6c6a64"
  muted-soft: "#8e8b82"
  hairline: "#e6dfd8"
  hairline-soft: "#ebe6df"
  hairline-strong: "#848075"
  focus: "#141413"
  focus-on-dark: "#faf9f5"
  canvas: "#faf9f5"
  surface-soft: "#f5f0e8"
  surface-card: "#efe9de"
  surface-cream-strong: "#e8e0d2"
  surface-dark: "#181715"
  surface-dark-elevated: "#252320"
  surface-dark-soft: "#1f1e1b"
  on-primary: "#ffffff"
  on-dark: "#faf9f5"
  on-dark-soft: "#a09d96"
  accent-teal: "#5db8a6"
  accent-amber: "#e8a55a"
  success: "#5db872"
  warning: "#d4a017"
  error: "#c64545"

typography:
  display-xl:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.5px
  code:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  button:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px
  full: 9999px

shadow:
  none: "none"
  hover-lift: "0 1px 3px rgba(20, 20, 19, 0.08)"

motion:
  duration-instant: 50ms
  duration-fast: 100ms
  duration-base: 150ms
  duration-slow: 220ms
  duration-emphasis: 320ms
  ease-standard: cubic-bezier(0.2, 0, 0.2, 1)
  ease-enter: cubic-bezier(0, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 20ms

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 40px
  button-secondary-on-dark:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 36px
  text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 96px
  hero-illustration-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  product-mockup-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  code-window-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: 24px
  model-comparison-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-card-featured:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  callout-card-coral:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  connector-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    height: 40px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  cookie-consent-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 24px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 8px 14px
    rounded: "{rounded.md}"
  category-tab-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
  badge-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-coral:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  cta-band-coral:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.lg}"
    padding: 64px
  cta-band-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.lg}"
    padding: 64px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark-soft}"
    typography: "{typography.body-sm}"
    padding: 64px
---

## Overview

Claude.com is the warmest, most editorial interface in the AI-product category. The base atmosphere is a **tinted cream canvas** (`{colors.canvas}` — #faf9f5) — distinctly warm, deliberately not the cool gray-white that every other AI brand uses. Headlines run a **slab-serif display** ("Copernicus" / Tiempos Headline) at weight 400 with negative letter-spacing, paired with **StyreneB / Inter** body sans. The combination feels like a literary publication, not a SaaS marketing page.

Brand voltage comes from the **cream + coral pairing** — coral (`{colors.primary}` — #cc785c) is the signature Anthropic accent, used on every primary CTA, on the brand wordmark, and on full-bleed callout cards. The coral is warm, slightly muted, never cyan/blue — a deliberate counter-positioning against OpenAI's cool slate, Google's saturated blue, and Microsoft's corporate cyan.

The system has three surface modes that alternate page-by-page:
1. **Cream canvas** (`{colors.canvas}`) — default body floor
2. **Light cream cards** (`{colors.surface-card}`) — feature card backgrounds
3. **Dark navy product surfaces** (`{colors.surface-dark}`) — code editor mockups, model showcase cards, pre-footer CTAs, footer itself

The dark surfaces are where Claude shows its product chrome — code blocks, terminal output, model comparison tables, agentic-flow diagrams. The cream-to-dark contrast is the page's pacing rhythm.

**Key Characteristics:**
- Warm cream canvas (`{colors.canvas}` — #faf9f5) with dark warm-ink text (`{colors.ink}` — #141413). The brand's defining color choice.
- Coral primary CTA (`{colors.primary}` — #cc785c). Used scarcely on individual buttons, generously on full-bleed coral callout cards.
- Slab-serif display headlines via Copernicus / Tiempos Headline at weight 400 with negative letter-spacing. Pairs with humanist sans body for a literary editorial voice.
- Dark navy product mockup cards (`{colors.surface-dark}` — #181715) carrying code blocks, terminal panels, model comparison data — the brand shows the product chrome at scale rather than abstract marketing illustrations.
- Light cream feature cards (`{colors.surface-card}` — #efe9de) — slightly darker than canvas, used for content-driven feature explanations.
- Anthropic radial-spike mark — a small black asterisk-like glyph (4-spoke radial) — appears as the brand wordmark prefix and as a content marker.
- Border radius is hierarchical: `{rounded.md}` (8px) for buttons + inputs, `{rounded.lg}` (12px) for content + product cards, `{rounded.xl}` (16px) for the hero illustration container, `{rounded.pill}` for badges.
- Section rhythm `{spacing.section}` (96px) — modern-SaaS standard. Internal card padding stays generous at `{spacing.xl}` (32px).

## Colors

### Brand & Accent
- **Coral / Primary** (`{colors.primary}` — #cc785c): The signature Anthropic warm coral. Used on every primary CTA background, on full-bleed coral callout cards, on the brand wordmark accent. The most-recognized Anthropic color outside of the spike-mark logo.
- **Coral Active** (`{colors.primary-active}` — #a9583e): The press / hover-darker variant.
- **Coral Disabled** (`{colors.primary-disabled}` — #e6dfd8): A desaturated cream-tinted disabled state.
- **Accent Teal** (`{colors.accent-teal}` — #5db8a6): Used sparingly on secondary product surfaces (terminal status indicators, "active connection" dots in connectors page).
- **Accent Amber** (`{colors.accent-amber}` — #e8a55a): A small companion warm-tone used on category badges and inline highlights.

#### Measured contrast on the signal colours — the brand fails AA here
These are extracted brand hexes and are **not** adjusted to pass. Stated plainly, because it is the useful fact for anyone building on this document:

- `{colors.on-primary}` (#ffffff) on `{colors.primary}` (#cc785c) measures **3.28:1**. That is **below the 4.5:1 AA floor for normal-size text**, and `{component.button-primary}` sets its label at `{typography.button}` — 14px / 500, which is normal-size by WCAG. **White-on-coral at 14px is a real AA failure on the live brand.** It clears AA Large (3:1), so it is defensible only at 18.66px+ bold or 24px+ regular — which is what `{component.cta-band-coral}` and `{component.callout-card-coral}` actually do at `{typography.display-sm}` (28px). The two passing routes, both needing brand approval: set button labels in `{colors.ink}` on coral (**5.63:1**), or use `{colors.primary-active}` (#a9583e) as the button fill and keep white (**5.06:1**).
- `{colors.accent-teal}` (#5db8a6) and `{colors.accent-amber}` (#e8a55a) **never carry white text in this system** — teal is a 8–10px status dot, amber is a badge fill and an inline highlight. White on them measures **2.37:1** and **2.11:1** respectively and must never be used. Where either tone sits behind type, the ink is `{colors.ink}`: **7.79:1** on teal, **8.74:1** on amber. As non-text status indicators both clear the 3:1 of WCAG 1.4.11 against `{colors.canvas}` only when paired with a shape or label, never colour alone.
- `{colors.primary}` as *inline link* ink measures **3.11:1** on `{colors.canvas}`. `{component.text-link}` sets it at `{typography.body-md}` (16px), so the coral inline link is also a real AA failure. `{colors.primary-active}` (#a9583e) reaches **4.8:1** on canvas and is the prescribed accessible substitute for inline body links; the extracted coral stays correct for 24px+ display links. Underline the link in either case — colour is never the only cue.
- `{colors.warning}` (#d4a017) with white type measures **2.38:1**; use `{colors.ink}` on warning fills (**7.76:1**). `{colors.success}` (#5db872) with white measures **2.45:1**; `{colors.ink}` on success reaches **7.52:1**.

### Surface
- **Canvas** (`{colors.canvas}` — #faf9f5): The default page floor. Tinted cream — warm, deliberately not pure white.
- **Surface Soft** (`{colors.surface-soft}` — #f5f0e8): Section dividers, very-soft band backgrounds.
- **Surface Card** (`{colors.surface-card}` — #efe9de): Feature cards, content cards. One step darker than canvas.
- **Surface Cream Strong** (`{colors.surface-cream-strong}` — #e8e0d2): A strongest-cream variant used on selected category tabs and emphasized section bands.
- **Surface Dark** (`{colors.surface-dark}` — #181715): Code editor mockups, model showcase cards, footer. The dominant dark surface.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — #252320): Elevated cards inside dark bands (settings panels in mockups).
- **Surface Dark Soft** (`{colors.surface-dark-soft}` — #1f1e1b): Slightly lighter dark, used for code block backgrounds inside larger dark cards.
- **Hairline** (`{colors.hairline}` — #e6dfd8): The 1px border tone on cream surfaces. Same hex as `{colors.primary-disabled}` — borders feel like one elevation step rather than ink lines.
- **Hairline Soft** (`{colors.hairline-soft}` — #ebe6df): Barely-visible divider used inside the same band.
- **Hairline Strong** (`{colors.hairline-strong}` — #848075): **Prescribed, not extracted.** A warm grey boundary tone added by this audit for the places where the hairline is the *only* thing defining an interactive bound — the `{component.text-input}` outline above all. The extracted `{colors.hairline}` measures **1.25:1** on `{colors.canvas}`, far below the 3.0:1 WCAG 1.4.11 non-text-contrast floor, so the real claude.com text-input border is not a perceivable boundary for low-vision users. `{colors.hairline-strong}` measures 3.74:1 on `{colors.canvas}`, 3.48:1 on `{colors.surface-soft}`, 3.26:1 on `{colors.surface-card}`, 3.01:1 on `{colors.surface-cream-strong}` and 4.54:1 on `{colors.surface-dark}` — it clears 3:1 on every surface this file defines. Scope `{colors.hairline}` and `{colors.hairline-soft}` to **decoration only**: dividers, card edges, table rules, anything whose absence costs no information.

### Focus
Both focus tokens are **prescribed, not extracted** — claude.com's real focus treatment was not measured, and no file in this repo previously defined a focus ring at all.
- **Focus** (`{colors.focus}` — #141413): A 2px warm-ink focus ring for every control on a cream surface. Deliberately the same warm near-black as `{colors.ink}` and the Anthropic spike-mark rather than a borrowed system blue — a cool blue ring would break the warm-humanist palette the brand is built on. Measures 17.5:1 on `{colors.canvas}`, 16.25:1 on `{colors.surface-soft}`, 15.26:1 on `{colors.surface-card}`, 14.07:1 on `{colors.surface-cream-strong}`, and 5.63:1 on `{colors.primary}` — so the same ring also survives on a coral `{component.callout-card-coral}`.
- **Focus On Dark** (`{colors.focus-on-dark}` — #faf9f5): The cream ring used on the dark product surfaces, where the ink ring would vanish. Measures 17.0:1 on `{colors.surface-dark}`, 15.82:1 on `{colors.surface-dark-soft}` and 14.88:1 on `{colors.surface-dark-elevated}`. One ring cannot serve both halves of this system: `{colors.focus}` sits at 1.03:1 on `{colors.surface-dark}`.

The ring never replaces the coral emphasis border on `{component.text-input-focused}` — it sits outside it, offset 2px, so a focused input shows both the brand's coral edge and a boundary that actually passes 1.4.11.

### Text
- **Ink** (`{colors.ink}` — #141413): All headlines and primary text. Warm dark, slightly off-pure-black.
- **Body Strong** (`{colors.body-strong}` — #252523): Emphasized paragraphs, lead text.
- **Body** (`{colors.body}` — #3d3d3a): Default running-text color.
- **Muted** (`{colors.muted}` — #6c6a64): Sub-headings, breadcrumbs, footer-adjacent secondary text.
- **Muted Soft** (`{colors.muted-soft}` — #8e8b82): Captions, fine-print, copyright lines.
- **On Primary** (`{colors.on-primary}` — #ffffff): Text on coral buttons.
- **On Dark** (`{colors.on-dark}` — #faf9f5): Cream-tinted white used on dark surfaces (echoes the canvas tone).
- **On Dark Soft** (`{colors.on-dark-soft}` — #a09d96): Footer body text, secondary labels in dark mockups.

### Semantic
- **Success** (`{colors.success}` — #5db872): Green status dots, "available" indicators.
- **Warning** (`{colors.warning}` — #d4a017): Warning callouts (rare on marketing surfaces).
- **Error** (`{colors.error}` — #c64545): Validation errors.

## Typography

### Font Family
The system runs **Copernicus** (or **Tiempos Headline** as substitute) as the slab-serif display face for headlines, and **StyreneB** (or **Inter** as substitute) as the humanist sans for body, navigation, and UI labels. **JetBrains Mono** handles code blocks. The fallback stack walks `Tiempos Headline, Garamond, "Times New Roman", serif` for display and `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` for body.

The display/body split is editorial:
- Copernicus serif (weight 400, negative tracking) → h1, h2, h3, hero display
- StyreneB sans (weight 400-500) → body, navigation, buttons, captions, labels
- JetBrains Mono → all code blocks and terminal text

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 64px | 400 | 1.05 | -1.5px | Homepage h1 ("Meet your thinking partner") — Copernicus serif |
| `{typography.display-lg}` | 48px | 400 | 1.1 | -1px | Section heads — Copernicus |
| `{typography.display-md}` | 36px | 400 | 1.15 | -0.5px | Sub-section heads, model names — Copernicus |
| `{typography.display-sm}` | 28px | 400 | 1.2 | -0.3px | Pricing tier names, callout headlines — Copernicus |
| `{typography.title-lg}` | 22px | 500 | 1.3 | 0 | Pricing plan size labels — StyreneB |
| `{typography.title-md}` | 18px | 500 | 1.4 | 0 | Feature card titles, intro paragraphs |
| `{typography.title-sm}` | 16px | 500 | 1.4 | 0 | Connector tile titles, list labels |
| `{typography.body-md}` | 16px | 400 | 1.55 | 0 | Default running-text — StyreneB |
| `{typography.body-sm}` | 14px | 400 | 1.55 | 0 | Footer body, fine-print |
| `{typography.caption}` | 13px | 500 | 1.4 | 0 | Badge labels, captions |
| `{typography.caption-uppercase}` | 12px | 500 | 1.4 | 1.5px | Category tags, "NEW" badges |
| `{typography.code}` | 14px | 400 | 1.6 | 0 | Code blocks — JetBrains Mono |
| `{typography.button}` | 14px | 500 | 1.0 | 0 | Standard button labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Top-nav menu items |

### Principles
Display sizes use weight 400 (regular), never bold. Negative letter-spacing (-0.3 to -1.5px) is essential — Copernicus without it reads as off-brand. The serif character is what gives Anthropic its literary, considered voice; switching to a sans-serif display would make Claude feel like every other AI tool.

Body type stays at weight 400 for paragraphs, weight 500 for labels and emphasized phrases. The sans body is humanist (StyreneB) — never geometric. Inter is an acceptable substitute because of its similar humanist proportions; Helvetica or Arial would be too neutral and break the warm-editorial feel.

### Note on Font Substitutes
If Copernicus / Tiempos Headline is unavailable, **Cormorant Garamond** at weight 500 with -0.02em letter-spacing is the closest open-source approximation. **EB Garamond** is a fallback. For StyreneB, **Inter** is the closest match — both are humanist sans designed for screen reading. **Söhne** is another close alternative if licensed.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- **Section padding:** `{spacing.section}` (96px) — modern-SaaS rhythm.
- **Card internal padding:** `{spacing.xl}` (32px) for feature cards, pricing tier cards, model comparison cards; `{spacing.lg}` (24px) for code-window cards and connector tiles.
- **Callout / CTA bands:** `{spacing.xxl}` (48px) inside coral callout cards; 64px inside the larger dark CTA band.

### Grid & Container
- **Max content width:** ~1200px centered.
- **Editorial body:** Single 12-column grid; hero often uses 6/6 split (h1 left, illustration right).
- **Feature card grids:** 3-up at desktop, 2-up at tablet, 1-up at mobile.
- **Connector tile grids:** 4-up or 6-up at desktop, 2-up at tablet, 1-up at mobile.
- **Pricing grid:** 3-up at desktop (Free / Pro / Team / Enterprise often), 1-up at mobile.

### Whitespace Philosophy
The cream canvas + serif display + generous internal padding create an editorial pacing — Claude reads like a long-form magazine column rather than a marketing template. Whitespace between bands stays uniform at 96px; whitespace inside cards is generous (32px), letting type breathe.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body sections, top nav, hero bands |
| Soft hairline | 1px `{colors.hairline}` border | Dividers, card edges, sub-nav — decoration only |
| Control boundary | 1px `{colors.hairline-strong}` border | Inputs, icon buttons, secondary buttons — anywhere the border is the control's only bound (prescribed) |
| Cream card | `{colors.surface-card}` background — no shadow | Feature cards, content cards |
| Dark surface card | `{colors.surface-dark}` background — no shadow | Code editor mockups, model showcase cards |
| Subtle drop shadow | `{shadow.hover-lift}` — `0 1px 3px rgba(20, 20, 19, 0.08)` | Hover-elevated states, used rarely |

Every other level is `{shadow.none}`. The two shadow values the system owns are now tokens, so nothing in this file references a shadow that has no key.

### Layer separation — measured
Elevation here is expressed **one way: as a surface fill**, with a border as the secondary cue and shadow as a rare third. The fills are deliberately close in luminance, which is the editorial feel but is worth stating numerically:

| Layer pair | Ratio |
|---|---|
| `{colors.canvas}` ↔ `{colors.surface-soft}` | 1.08:1 |
| `{colors.canvas}` ↔ `{colors.surface-card}` | 1.15:1 |
| `{colors.surface-soft}` ↔ `{colors.surface-card}` | 1.07:1 |
| `{colors.canvas}` ↔ `{colors.surface-cream-strong}` | 1.24:1 |
| `{colors.surface-dark}` ↔ `{colors.surface-dark-soft}` | 1.07:1 |
| `{colors.surface-dark}` ↔ `{colors.surface-dark-elevated}` | 1.14:1 |

No adjacent pair reaches 3:1, so **the cream ladder is not distinguishable by luminance alone** — it reads only as a large adjacent block, and two of these fills sitting side by side at small scale are effectively one colour. Where a layer change must be perceivable (a selected `{component.category-tab}`, an elevated panel inside a dark mockup), pair the fill with a 1px `{colors.hairline-strong}` edge rather than relying on the fill. The cream→dark jump is the only layer change this system makes that is legible on its own: `{colors.canvas}` ↔ `{colors.surface-dark}` measures 17.0:1.

The elevation philosophy is **color-block first, shadow rare**. Most depth comes from the cream-vs-dark surface contrast. Shadows are minimal. The dark surface mockups have their own internal product chrome (code editor scrollbars, line numbers, syntax highlighting) which adds detail without needing external shadows.

### Decorative Depth
- The Anthropic spike-mark glyph (4-spoke radial asterisk) appears as a small black mark in the brand wordmark and inline as a content marker.
- Code editor mockups carry their own internal depth: syntax-highlighted text in muted blues / oranges / grays, line numbers in `{colors.muted-soft}`, status bars at the bottom in `{colors.surface-dark-elevated}`.
- Some hero illustrations use simple line-art with coral and dark-navy strokes on cream — minimal, hand-drawn-feeling, never photorealistic.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Reserved for badge accents and tiny dropdowns |
| `{rounded.sm}` | 6px | Small inline buttons, dropdown items |
| `{rounded.md}` | 8px | Standard CTA buttons, text inputs, category tabs |
| `{rounded.lg}` | 12px | Content cards (feature, pricing, code-window, model-comparison) |
| `{rounded.xl}` | 16px | Hero illustration container, the larger marquee components |
| `{rounded.pill}` | 9999px | Badge pills, "NEW" tags |
| `{rounded.full}` | 9999px / 50% | Avatar substitutes, icon buttons |

`{rounded.pill}` and `{rounded.full}` carry the same 9999px value and are kept as two names because they describe two intents (a stadium badge versus a circle); nothing else in the ladder duplicates, and no component uses a radius outside it.

### Border & Focus Ring Geometry
Prescribed by this audit — the live site's ring geometry was not measured.

| Property | Value |
|---|---|
| Border width, all boundaries | 1px (the system has exactly one border width) |
| Focus ring width | 2px |
| Focus ring offset | 2px, outside the control's own border |
| Focus ring radius | the control's own `{rounded.*}` value + 2px, so the ring stays concentric |
| Focus ring colour | `{colors.focus}` on cream and coral surfaces, `{colors.focus-on-dark}` on `{colors.surface-dark}` family surfaces |

The ring is never a background change and never an inset border — a cream-on-cream inset ring would be invisible on this canvas.

### Photography & Illustrations
Claude's hero rarely uses photography. Instead it uses:
- Simple line-art illustrations with coral + dark-navy strokes on the cream canvas
- Code editor mockups (the dominant "hero" treatment on developer-focused pages)
- Terminal output mockups with monospace text on dark
- Model comparison cards (Opus / Sonnet / Haiku) with abstract geometric thumbnails

When photography is used (rare — mostly testimonials), avatars crop to perfect circles at 40px diameter.

## Components

### Top Navigation

**`top-nav`** — Cream nav bar pinned to the top of every page. 64px tall, `{colors.canvas}` background. Carries the Anthropic spike-mark + "Claude" wordmark at left, primary horizontal menu (Product, Solutions, Use Cases, Pricing, Research, Company) center-left, right-side cluster with "Sign in" text-link, "Try Claude" `{component.button-primary}` (coral). Menu items in `{typography.nav-link}` (StyreneB 14px / 500).

### Buttons

**`button-primary`** — The signature coral CTA. Background `{colors.primary}` (#cc785c), text `{colors.on-primary}` (white), type `{typography.button}` (StyreneB 14px / 500), padding 12px × 20px, height 40px, rounded `{rounded.md}` (8px). Active state `button-primary-active` darkens to `{colors.primary-active}` (#a9583e).

**`button-secondary`** — Cream button with hairline outline. Background `{colors.canvas}`, text `{colors.ink}`, 1px hairline border, same padding + height + radius as primary.

**`button-secondary-on-dark`** — Used over `{colors.surface-dark}` cards. Background `{colors.surface-dark-elevated}` (#252320), text `{colors.on-dark}`. Stays dark — the system never inverts to a light secondary on dark surfaces.

**`button-text-link`** — Inline text button, no background. Used for "Sign in" in the top nav and inline CTA links.

**`button-icon-circular`** — 36px circular icon button. Background `{colors.canvas}`, hairline border, ink-color icon. Used for carousel arrows, share, "view more".

**`text-link`** — Inline body links in `{colors.primary}` (the coral). Underlined on press; the coral inline link is one of the system's most distinctive small details.

### Cards & Containers

**`hero-band`** — Cream-canvas hero with a 6-6 grid: h1 + sub-headline + button row on the left, hero illustration card or product mockup card on the right. Vertical padding `{spacing.section}` (96px).

**`hero-illustration-card`** — A larger card holding the hero's right-side artifact — sometimes a coral-stroke line illustration on cream background, sometimes a dark code editor mockup. Background `{colors.canvas}` or `{colors.surface-dark}` depending on context, rounded `{rounded.xl}` (16px).

**`feature-card`** — Used in 3-up feature grids. Background `{colors.surface-card}` (#efe9de — slightly darker cream), rounded `{rounded.lg}` (12px), internal padding `{spacing.xl}` (32px). Carries a small icon at top, an `{typography.title-md}` headline, and a body description in `{typography.body-md}`.

**`product-mockup-card-dark`** — Dark navy card showing actual Claude product chrome (chat interface, code editor, agent controls). Background `{colors.surface-dark}`, rounded `{rounded.lg}`, internal padding `{spacing.xl}` (32px). Carries text labels in `{colors.on-dark}` and product UI fragments below.

**`code-window-card`** — A specialized dark card showing a code editor with line numbers, syntax-highlighted code in `{typography.code}` (JetBrains Mono), and sometimes a "Run" button or terminal output panel below. Background `{colors.surface-dark}` with `{colors.surface-dark-soft}` for the inner code block, rounded `{rounded.lg}`, padding `{spacing.lg}` (24px). The signature visual element of Claude Code product pages.

**`model-comparison-card`** — Used on the homepage's "Which problem are you up against?" section comparing Opus / Sonnet / Haiku. Background `{colors.canvas}` with hairline border, rounded `{rounded.lg}`, internal padding `{spacing.xl}` (32px). Carries the model name, a short capability blurb, and a `{component.text-link}` to learn more.

**`pricing-tier-card`** — Standard tier card. Background `{colors.canvas}` with hairline border, rounded `{rounded.lg}`, padding `{spacing.xl}` (32px). Carries the plan name in `{typography.title-lg}` (StyreneB), price in `{typography.display-sm}` (Copernicus serif!), feature checklist in `{typography.body-md}`, and a `{component.button-primary}` at the bottom.

**`pricing-tier-card-featured`** — The featured tier (typically "Pro" or "Team"). Background flips to `{colors.surface-dark}`, text inverts to `{colors.on-dark}`. The dark surface IS the featured-tier signal.

**`callout-card-coral`** — A full-bleed coral card carrying a major call-to-action. Background `{colors.primary}` (#cc785c), text `{colors.on-primary}` (white), rounded `{rounded.lg}`, padding `{spacing.xxl}` (48px). The coral surface IS the voltage; the CTA inside uses an inverted button style (cream/canvas button on coral).

**`connector-tile`** — Used on the connectors page's integration grid. Background `{colors.canvas}` with hairline border, rounded `{rounded.lg}`, padding 20px. Each tile carries a logo at top, a `{typography.title-sm}` connector name, and a short description.

### Inputs & Forms

**`text-input`** — Standard text input. Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, rounded `{rounded.md}` (8px), padding 10px × 14px, height 40px. 1px hairline border in `{colors.hairline}`.

**`text-input-focused`** — Focus state. Border thickens or shifts to `{colors.primary}` (coral) for emphasis. Carries a 3px coral-at-15%-alpha outer ring.

**`cookie-consent-card`** — Bottom-right floating dark cookie banner. Background `{colors.surface-dark}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding `{spacing.lg}` (24px). One of the few places dark surface appears at small scale on cream pages.

### Tags / Badges

**`badge-pill`** — Small pill label used for category tags. Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.caption}` (13px / 500), rounded `{rounded.pill}`, padding 4px × 12px.

**`badge-coral`** — Coral-fill badge for "NEW", "BETA", featured highlights. Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.caption-uppercase}` (12px / 500 / 1.5px tracking), rounded `{rounded.pill}`, padding 4px × 12px.

### Tab / Filter

**`category-tab`** + **`category-tab-active`** — Used in sub-nav rows on solutions / connectors pages. Inactive: transparent background, `{colors.muted}` text. Active: `{colors.surface-card}` background, `{colors.ink}` text. Padding 8px × 14px, rounded `{rounded.md}`.

### CTA / Footer

**`cta-band-coral`** — A pre-footer "Try Claude" CTA card. Full-width coral fill, white type, rounded `{rounded.lg}`, padding 64px. Carries an h2 in `{typography.display-sm}` (still serif!), a sub-line, and a cream-button CTA.

**`cta-band-dark`** — Alternative pre-footer band on developer-focused pages. Background `{colors.surface-dark}`, text `{colors.on-dark}`, rounded `{rounded.lg}`, padding 64px. Often pairs with a code-window card.

**`footer`** — Dark navy footer that closes every page. Footer link states mirror `{component.button-text-link}`. Background `{colors.surface-dark}` (#181715), text `{colors.on-dark-soft}`. 4-column link list at desktop covering Product / Company / Resources / Legal. Vertical padding 64px. The Anthropic spike-mark + "Anthropic" wordmark sits at the top in `{colors.on-dark}`. The footer never inverts.

### Component States

The extracted document covered **default**, **active/pressed** and **disabled** only — `{component.button-primary-active}`, `{component.button-primary-disabled}` and `{component.text-input-focused}` are the only state variants claude.com's static surfaces revealed. Every other cell below is **prescribed by this audit**, not extracted. A component with genuinely two states says so in the Notes column.

| Component | default | hover | focus-visible | active / pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `{component.button-primary}` | `{colors.primary}` fill | fill → `{colors.primary-active}` | 2px `{colors.focus}` ring, 2px offset | fill `{colors.primary-active}`, `translateY(1px)` | `{colors.primary-disabled}` fill, `{colors.muted}` label (4.1:1 — passes AA at the 14px label size) | label opacity 0 → spinner in `{colors.on-primary}`, width held | n/a | n/a |
| `{component.button-secondary}` | `{colors.canvas}` fill, 1px `{colors.hairline-strong}` | border → `{colors.ink}` | 2px `{colors.focus}` ring | fill → `{colors.surface-card}` | border `{colors.hairline}`, label `{colors.muted-soft}` | spinner in `{colors.ink}` | n/a | n/a |
| `{component.button-secondary-on-dark}` | `{colors.surface-dark-elevated}` fill | fill → `#2f2c28` | 2px `{colors.focus-on-dark}` ring | fill → `{colors.surface-dark-soft}` | label `{colors.on-dark-soft}` | spinner in `{colors.on-dark}` | n/a | n/a |
| `{component.button-text-link}` | `{colors.ink}` label | underline appears | 2px `{colors.focus}` ring around the text box | label → `{colors.body}` | label `{colors.muted-soft}`, no underline | n/a | n/a | n/a |
| `{component.button-icon-circular}` | `{colors.canvas}` fill, 1px `{colors.hairline-strong}` | fill → `{colors.surface-card}` | 2px `{colors.focus}` ring | `scale(0.96)` | icon `{colors.muted-soft}` | n/a | n/a | n/a |
| `{component.text-link}` | `{colors.primary-active}` label + underline (see Colors — the extracted coral fails AA at 16px) | underline thickens 1px → 2px | 2px `{colors.focus}` ring | label → `{colors.ink}` | n/a | n/a | n/a | n/a |
| `{component.top-nav}` links | `{colors.ink}` in `{typography.nav-link}` | label → `{colors.body}` | 2px `{colors.focus}` ring | label → `{colors.ink}` | n/a | n/a | current section gets a 2px `{colors.primary}` underline | n/a |
| `{component.feature-card}` | `{colors.surface-card}` fill | `{shadow.hover-lift}`, no travel | 2px `{colors.focus}` ring when the whole card is a link | `scale(0.995)` | n/a | skeleton blocks in `{colors.surface-cream-strong}` | n/a | n/a |
| `{component.connector-tile}` | `{colors.canvas}` fill, 1px `{colors.hairline-strong}` | border → `{colors.muted}` | 2px `{colors.focus}` ring | `scale(0.99)` | tile at 40% opacity, "coming soon" label | skeleton blocks | 1px → 2px `{colors.primary}` border | n/a |
| `{component.model-comparison-card}` | `{colors.canvas}` fill, 1px `{colors.hairline-strong}` | `{shadow.hover-lift}` | 2px `{colors.focus}` ring | `scale(0.995)` | n/a | n/a | 2px `{colors.primary}` border | n/a |
| `{component.pricing-tier-card}` | `{colors.canvas}` fill, 1px `{colors.hairline-strong}` | `{shadow.hover-lift}` | ring on the contained `{component.button-primary}`, not the card | n/a | n/a | n/a | `{component.pricing-tier-card-featured}` — the dark fill *is* the selected signal | n/a |
| `{component.category-tab}` | transparent, `{colors.muted}` label | label → `{colors.ink}` | 2px `{colors.focus}` ring | label `{colors.ink}` | label `{colors.muted-soft}`, no pointer | n/a | `{component.category-tab-active}` — `{colors.surface-card}` fill + `{colors.ink}` label + 1px `{colors.hairline-strong}` edge, because the fill alone is only 1.15:1 from canvas | n/a |
| `{component.text-input}` | `{colors.canvas}` fill, 1px `{colors.hairline-strong}` | border → `{colors.muted}` | `{component.text-input-focused}`: 1px `{colors.primary}` border + 2px `{colors.focus}` ring at 2px offset | n/a | fill `{colors.surface-soft}`, border `{colors.hairline}`, text `{colors.muted-soft}` | trailing spinner inside the field, field stays editable | n/a | 1px `{colors.error}` border + message below in `{colors.error}` on `{colors.canvas}` (4.59:1) with an icon — never colour alone |
| `{component.badge-pill}`, `{component.badge-coral}` | static fill | — | — | — | — | — | — | — |
| `{component.cookie-consent-card}` | `{colors.surface-dark}` fill | — | ring on its contained buttons | — | — | — | — | — |

Notes on genuinely small state sets:
- `{component.badge-pill}` and `{component.badge-coral}` are **non-interactive labels: default only.** They have exactly one state.
- `{component.hero-band}`, `{component.hero-illustration-card}`, `{component.cta-band-coral}`, `{component.cta-band-dark}`, `{component.product-mockup-card-dark}` and `{component.code-window-card}` are **containers: default only.** Their states live on the controls they contain.
- `{component.footer}` is a container; its links take the `{component.button-text-link}` row with `{colors.on-dark}` / `{colors.focus-on-dark}` substituted.
- No component in this system has a true `loading` state on the marketing surface except the form controls and the skeletons noted above; the rest render server-side.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or choreography below was extracted from claude.com. The file's own Known Gaps already recorded that transition timings were out of scope; this section fills that gap with a declared profile rather than leaving it empty, and every value here is a design decision open to correction against the real product.

**Profile: Crisp** — immediate and tool-like. State change reads as instant; there is no entrance choreography. The justification is the product this document covers: the signature component is `{component.code-window-card}`, the dominant product chrome is a code editor and terminal, and the voice in Do's and Don'ts is already anti-decoration ("nothing else changes"). Editorial pacing in this brand is carried by 96px `{spacing.section}` rhythm and serif type, not by motion — so motion stays out of the way. Base duration `{motion.duration-base}` (150ms), near-linear easing, `{motion.stagger-step}` (20ms).

Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin` — the cream/dark band pacing depends on a stable layout, and those properties force layout on every frame.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, tile, card) | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `background-color`, `border-color`, `opacity`, `box-shadow` | Unchanged — colour-only change, no travel to remove |
| Press | `{motion.duration-instant}` 50ms | `{motion.ease-standard}` | `transform: translateY(1px)` / `scale(0.96–0.995)` | Travel and scale removed; press shows as the `{colors.primary-active}` fill change only |
| Focus (ring appear) | `{motion.duration-instant}` 50ms | `{motion.ease-standard}` | `opacity` on the ring | Unchanged — the ring appears instantly, never animated in |
| Page / route transition | `{motion.duration-fast}` 100ms out, `{motion.duration-base}` 150ms in | `{motion.ease-exit}` out, `{motion.ease-enter}` in | `opacity` only | Opacity crossfade held at 100ms; no travel at any time |
| Modal / drawer | `{motion.duration-base}` 150ms in, `{motion.duration-fast}` 100ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px)` (drawer: `translateX`) | `transform` removed; opacity fade at 100ms. Backdrop fades at 100ms |
| Dropdown / menu | `{motion.duration-fast}` 100ms in, `{motion.duration-instant}` 50ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: scale(0.98) → 1` from the trigger edge | `transform` removed; opacity only, 100ms |
| Toast | `{motion.duration-base}` 150ms in, `{motion.duration-fast}` 100ms out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px)` | `transform` removed; opacity only. Auto-dismiss timer extends to 10s, since a moving element is no longer drawing the eye |
| List enter (feature grid, connector grid) | `{motion.duration-fast}` 100ms per item, `{motion.stagger-step}` 20ms apart, capped at 8 items | `{motion.ease-enter}` | `opacity` 0 → 1 only — Crisp adds no travel on enter | Stagger dropped to 0ms; all items appear together at full opacity. Nothing is delayed |
| List exit (filter change on connectors) | `{motion.duration-instant}` 50ms, no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | Instant removal, no fade |
| Loading (spinner, skeleton) | 800ms linear, infinite | `linear` | `transform: rotate` (spinner) / `opacity` 0.6 ↔ 1 (skeleton pulse) | Spinner rotation frozen; replaced by a static `{colors.muted}` indicator with a live-region text label. Skeleton pulse frozen at `opacity: 1`. This is the only infinite animation in the system and exists solely to signal pending work |

Rules this profile holds to:
- Every exit is shorter than its matching entrance (modal 100 < 150, dropdown 50 < 100, toast 100 < 150, list 50 < 100).
- Nothing animates on first paint. Hero type, `{component.hero-band}` and all above-the-fold content render at final opacity; the list-enter stagger applies to content revealed by interaction or by scroll into view, never to the initial paint.
- `{component.code-window-card}` does **not** typewriter-animate its code. The extracted document notes a typewriter effect on the live homepage; under Crisp that is brand ambience at most, must be declared as such, must not be the only way the code becomes readable, and is frozen under reduced motion.
- No infinite animation except the loading indicators above.
- Durations never vary by viewport. A Crisp system does not slow down on mobile.

### `@media (prefers-reduced-motion: reduce)`

**Removed:** all `transform` — every `translateY`, `translateX`, `scale` and `rotate` in the table above, including the press scale, the modal and toast rise, the dropdown scale, and spinner rotation. All stagger (`{motion.stagger-step}` → 0ms). All ambience, including any homepage typewriter reveal, which freezes at its final state with the full text present.

**Kept:** opacity fades, capped at `{motion.duration-fast}` (100ms) — already under the 150ms ceiling, because Crisp's full-motion durations are short enough that nothing needs shortening. Colour transitions on hover, focus and press are kept: they carry state information and involve no motion. The focus ring still appears instantly. Loading still communicates, as a static indicator plus a text label rather than a spin.

Nothing is made unavailable or harder to reach under reduced motion; no interaction depends on an animation completing.

## Accessibility

Contrast figures here are computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. Everything about focus geometry, tap targets and reduced motion is **prescribed** — this document describes a static capture, so no rendered page was measured.

### Measured contrast — key pairs

| Foreground | Background | Ratio | Required | Verdict |
|---|---|---|---|---|
| `{colors.ink}` | `{colors.canvas}` | 17.5:1 | 4.5 | Pass |
| `{colors.ink}` | `{colors.surface-card}` | 15.26:1 | 4.5 | Pass |
| `{colors.body}` | `{colors.canvas}` | 10.34:1 | 4.5 | Pass |
| `{colors.muted}` | `{colors.canvas}` | 5.13:1 | 4.5 | Pass |
| `{colors.muted}` | `{colors.surface-card}` | 4.48:1 | 4.5 | **Fail by 0.02** — restrict `{colors.muted}` on cream cards to 18.66px+ bold / 24px+ regular, or step to `{colors.body}` (9.02:1) |
| `{colors.muted-soft}` | `{colors.canvas}` | 3.23:1 | 4.5 | **Fail** — fine-print tone. Clears AA Large only, so it is defensible for 24px+ text and for the copyright line it is used on only if that line is treated as non-essential. For `{typography.caption}` (13px) use `{colors.muted}` |
| `{colors.on-dark}` | `{colors.surface-dark}` | 17.0:1 | 4.5 | Pass |
| `{colors.on-dark-soft}` | `{colors.surface-dark}` | 6.62:1 | 4.5 | Pass |
| `{colors.on-dark-soft}` | `{colors.canvas}` | 2.57:1 | 4.5 | **Never use this pairing.** `{colors.on-dark-soft}` is a dark-surface-only ink; on cream, secondary text is `{colors.muted}` |
| `{colors.on-primary}` | `{colors.primary}` | 3.28:1 | 4.5 | **Fail** — real brand failure at the 14px button label. See Colors |
| `{colors.primary}` | `{colors.canvas}` | 3.11:1 | 4.5 | **Fail** as inline link ink at 16px. See Colors |
| `{colors.hairline}` | `{colors.canvas}` | 1.25:1 | 3.0 | **Fail** — decoration only from now on |
| `{colors.hairline-soft}` | `{colors.canvas}` | 1.18:1 | 3.0 | **Fail** — the weakest tone in the file. Decoration only: in-band dividers. Never a control boundary |
| `{colors.hairline-strong}` | `{colors.canvas}` | 3.74:1 | 3.0 | Pass (prescribed) |
| `{colors.focus}` | `{colors.canvas}` | 17.5:1 | 3.0 | Pass (prescribed) |
| `{colors.error}` | `{colors.canvas}` | 4.59:1 | 4.5 | Pass |

### Components that assert a failing pair

Four components in the frontmatter pair `{colors.on-primary}` (#ffffff) with `{colors.primary}` (#cc785c) — **3.28:1**, below the 4.5:1 AA floor for normal-size text. Named here rather than left for a reader to derive, because all four are extracted brand configurations and none of the hexes were altered:

| Component | Pair | Ratio | Verdict |
|---|---|---|---|
| `{component.button-primary}` | #ffffff on #cc785c | 3.28:1 | **Fail.** Label is `{typography.button}` 14px/500 — normal-size text, so 4.5:1 applies. The signature CTA of the brand fails AA. Passing routes: `{colors.ink}` label on coral (5.63:1) or a `{colors.primary-active}` fill with white (5.06:1) |
| `{component.badge-coral}` | #ffffff on #cc785c | 3.28:1 | **Fail.** `{typography.caption-uppercase}` 12px/500 — the worst case in the set, since the type is the smallest. Use `{colors.ink}` on the coral fill |
| `{component.callout-card-coral}` | #ffffff on #cc785c | 3.28:1 | Passes **AA Large** at its own `{typography.title-md}` heading only if that heading is set 18.66px+ bold or 24px+ regular; at the documented 18px/500 it **fails**. Body copy inside the card must not be white |
| `{component.cta-band-coral}` | #ffffff on #cc785c | 3.28:1 | **Passes AA Large** as documented — its type is `{typography.display-sm}` (28px), above the 24px regular threshold. Compliant as-is; any smaller type added to this band is not |

The same applies to `{colors.on-dark-soft}` inside `{component.footer}` (6.62:1 — passes) and to `{colors.muted}` inside `{component.button-primary-disabled}` (4.1:1 — exempt, WCAG sets no contrast requirement on disabled controls).

### Focus ring visibility on every surface this file defines

| Surface | Ring token | Ratio | Required |
|---|---|---|---|
| `{colors.canvas}` | `{colors.focus}` | 17.5:1 | 3.0 |
| `{colors.surface-soft}` | `{colors.focus}` | 16.25:1 | 3.0 |
| `{colors.surface-card}` | `{colors.focus}` | 15.26:1 | 3.0 |
| `{colors.surface-cream-strong}` | `{colors.focus}` | 14.07:1 | 3.0 |
| `{colors.primary}` (coral callout / CTA band) | `{colors.focus}` | 5.63:1 | 3.0 |
| `{colors.surface-dark}` | `{colors.focus-on-dark}` | 17.0:1 | 3.0 |
| `{colors.surface-dark-soft}` | `{colors.focus-on-dark}` | 15.82:1 | 3.0 |
| `{colors.surface-dark-elevated}` | `{colors.focus-on-dark}` | 14.88:1 | 3.0 |

Two rings are required because one cannot serve both halves of this system: `{colors.focus}` on `{colors.surface-dark}` measures 1.03:1 and would be invisible. The switch point is the surface, not the page: a `{component.cookie-consent-card}` floating over a cream page is a dark surface and takes `{colors.focus-on-dark}`.

Focus is never removed. `:focus-visible` is the hook, so pointer users do not see rings on click, but keyboard focus is always drawn — including on `{component.feature-card}` and `{component.connector-tile}` when the whole card is a link.

### Minimum tap target

Prescribed target: **44 × 44px** (WCAG 2.5.5 AAA / 2.5.8 AA minimum of 24×24 as the hard floor).

| Component | Documented size | Verdict |
|---|---|---|
| `{component.button-primary}` | 40px tall | Under 44. Add 4px of transparent vertical padding to reach a 44px hit area without changing the visible 40px pill |
| `{component.text-input}` | 40px tall | Same remedy |
| `{component.button-icon-circular}` | 36 × 36px | **Under 44** — the extracted file already admits this. Clears the 24×24 floor of 2.5.8; extend the hit area to 44 × 44 with transparent padding and keep the 36px visual circle |
| `{component.category-tab}` | 8px × 14px padding on 14px/1.4 type | ≈ 36px tall. Raise vertical padding to `{spacing.sm}` (12px) for a 44px row |
| `{component.connector-tile}` | whole 20px-padded card | Pass |

Spacing between adjacent targets must be at least `{spacing.xs}` (8px) so a 44px hit area never overlaps its neighbour. None of this is verifiable from a static document — it needs a rendered page.

### Reduced motion

See the `@media (prefers-reduced-motion: reduce)` block above. Summary: all travel, scale, rotation and stagger removed; opacity fades kept at `{motion.duration-fast}` (100ms); loading indicators become static plus a text label; no interaction depends on motion.

### Other prescribed requirements

- Colour is never the only carrier of meaning. `{colors.success}`, `{colors.warning}` and `{colors.error}` always pair with an icon or a text label — the teal "active connection" dot in particular is an 8–10px shape at 2.25:1 against `{colors.canvas}`, below the 3:1 of WCAG 1.4.11, and is meaningless alone. `{colors.success}` measures 2.33:1 and `{colors.accent-amber}` 2.0:1 on canvas — same conclusion.
- `{typography.body-md}` at 16px / 1.55 on every cream surface clears 4.5:1 in `{colors.ink}` and `{colors.body}`; the humanist sans at weight 400 is the readable default and no body copy drops below 14px.
- Display type at `{typography.display-xl}` (64px) with -1.5px tracking is the one place negative letter-spacing is aggressive; it stays above 0.12em total spacing, but tracking must not be tightened further at smaller sizes.
- Text must survive 200% zoom and a 1.5 line-height / 0.12em letter-spacing user override without clipping. Not verifiable here.
- `{component.code-window-card}` scrolls horizontally rather than wrapping. That is a documented choice; it means code blocks fail reflow (WCAG 1.4.10) on narrow viewports, which is permitted for content requiring two-dimensional layout, and the card must remain keyboard-scrollable.

## Do's and Don'ts

### Do
- Anchor every page on the cream canvas. Pure white reads as "any other AI tool"; the warm tint is the brand differentiator.
- Use Copernicus serif for every display headline. Pair with StyreneB sans body. Negative letter-spacing on display sizes is non-negotiable.
- Reserve `{colors.primary}` (coral) for primary CTAs and full-bleed `{component.callout-card-coral}` moments. Don't paint accent moments coral elsewhere.
- Use `{component.product-mockup-card-dark}` and `{component.code-window-card}` to show actual Claude product chrome. Don't paint marketing illustrations of code when you can show real code.
- Pair `{component.feature-card}` (cream) with `{component.product-mockup-card-dark}` (navy) in alternating bands. The cream-to-dark rhythm is the brand's pacing mechanism.
- Use the Anthropic spike-mark glyph as the brand wordmark prefix. Never invert the mark to white-on-dark within the wordmark itself.
- Apply `{spacing.section}` (96px) between major bands.

### Don't
- Don't use cool grays or pure white for canvas. Cream is the brand.
- Don't bold serif display weight. Copernicus at 700 reads as bombastic; the system stays at 400.
- Don't use cool blue or saturated cyan as a brand accent. The coral is the brand voltage.
- Don't put coral everywhere. The coral is scarce on individual elements and generous only on full-bleed coral callout cards.
- Don't use Inter for display headlines. The serif character is the brand voice.
- Don't repeat the same surface mode in two consecutive bands. The pacing alternates: cream → cream-card → dark-mockup → cream → coral-callout → dark-footer.
- Don't add hover state styling beyond the Component States table. The extracted system encoded press only; the hover, focus-visible, loading, selected and error cells added by this audit are prescribed and deliberately minimal — a colour or border shift, no travel. Anything richer than that table is off-brand.
- Don't skip the focus ring. It is the one addition to this system that is non-negotiable: every control takes `{colors.focus}` or `{colors.focus-on-dark}` on `:focus-visible`.
- Don't use `{colors.hairline}` as the only boundary of an interactive control. At 1.25:1 on canvas it is decoration; controls take `{colors.hairline-strong}`.
- Don't put white type on `{colors.accent-teal}`, `{colors.accent-amber}`, `{colors.success}` or `{colors.warning}`. Those pairs sit between 2.1:1 and 2.5:1. Use `{colors.ink}`.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav; hero h1 64→32px; hero-illustration-card stacks below content; feature grids 1-up; connector tiles 2-up; pricing 1-up; footer 4 cols → 1 |
| Tablet | 768–1024px | Top nav stays horizontal but tightens; feature cards 2-up; connector tiles 3-up; pricing 2-up |
| Desktop | 1024–1440px | Full top-nav with all menu items; 3-up feature cards; 4-up or 6-up connector tiles; 3-up pricing tiers |
| Wide | > 1440px | Same as desktop with more outer breathing room; max content width caps at 1200px |

### Touch Targets
- `{component.button-primary}` at minimum 40 × 40px.
- `{component.button-icon-circular}` at exactly 36 × 36 — slightly under WCAG 44 but visually centered.
- `{component.text-input}` height is 40px.
- Connector tile entire card area is tappable; effective tap area >> 44px.

### Collapsing Strategy
- Top nav collapses to hamburger at < 768px; menu opens as a full-screen cream sheet.
- Hero band's 6-6 grid collapses to single-column on mobile — h1 + sub-head + buttons first, then the illustration / mockup card below.
- Feature grids reduce columns rather than scaling cards down.
- Pricing tier cards collapse 4 → 2 → 1; featured-tier dark surface stays visually distinct at every breakpoint.
- Code-window cards retain code legibility at every breakpoint by allowing horizontal scroll within the card rather than wrapping code lines.

### Image Behavior
- Code blocks inside dark mockups stay at fixed font-size; horizontal scroll on mobile rather than wrapping.
- Hero illustrations scale proportionally; line-art strokes thin slightly on mobile.
- Avatar photos in testimonials crop to circles at every breakpoint.

## Iteration Guide

1. Focus on ONE component at a time. Reference its YAML key (`{component.feature-card}`, `{component.code-window-card}`).
2. Variants of an existing component (`-active`, `-disabled`, `-focused`) live as separate entries in `components:`.
3. Use `{token.refs}` everywhere — never inline hex.
4. States live in the Component States table. Default, Active/Pressed and Disabled are extracted; hover, focus-visible, loading, selected and error are prescribed by this audit — mark any change to them as prescribed until the live product is measured.
5. Display headlines stay Copernicus serif 400 with negative tracking. Body stays StyreneB / Inter 400. The split is unbreakable.
6. Cream + coral + dark navy is the trinity. Don't introduce a fourth surface tone (no purple cards, no green sections).
7. When in doubt about emphasis: bigger Copernicus serif before bolder weight.

## Known Gaps

- Copernicus and StyreneB are licensed Anthropic typefaces and not available as public web fonts. Substitutes (Tiempos Headline / Cormorant Garamond / EB Garamond for serif; Inter / Söhne for sans) are documented in the typography section.
- The Anthropic radial-spike-mark is a brand glyph rendered as inline SVG; it's not formalized as a system token here. Treat it as a logo asset.
- **Motion is prescribed, not extracted.** No timing on the live site was measured. The Motion & Animation section declares a Crisp profile chosen from this document's own observable signals (code-editor product chrome, anti-decoration voice) and says so in its first line. The real chat message reveal, the homepage code-block typewriter effect and the agentic-flow diagram animations remain unmeasured; the typewriter in particular is treated here as optional ambience, which may understate what the live page does.
- **The focus ring is prescribed.** `{colors.focus}` and `{colors.focus-on-dark}` are an addition by this audit, not an extracted brand value. claude.com's real focus treatment is unknown; it may well be a coral ring, which would need a different value on coral surfaces, since coral-on-coral is 1.0:1.
- **`{colors.hairline-strong}` is prescribed.** It is a parallel accessible boundary token, not a brand hex. The extracted `{colors.hairline}` is preserved unchanged at 1.25:1 and scoped to decoration.
- **Most component states are prescribed.** Only default, active/pressed and disabled were extractable. Hover, focus-visible, loading, selected and error in the Component States table are design decisions.
- Form validation states beyond `{component.text-input-focused}` are not extracted — the `error` column entries would need a sign-up or feedback flow to confirm.
- Tap-target sizes, overlap, clipping, reflow at 200% zoom and frame rate cannot be verified from a static document. The Accessibility section's target figures are the documented component dimensions plus a prescribed remedy, not measurements of a rendered page.
- The real brand fails WCAG AA at three points that cannot be fixed without changing a brand hex: white on coral at 14px (3.28:1), the coral inline link at 16px (3.11:1), and the hairline as a control boundary (1.25:1). All three are stated in Colors and Accessibility with their nearest passing values. None of the extracted hexes were altered.
- The actual Claude product surface (claude.ai chat interface) shares some tokens with the marketing site but adds many product-specific components (chat bubbles, message tools, file upload chips, conversation history sidebar) that are out of scope for this marketing-surface document.
- The "agent" / "computer use" demo cards on certain pages display animated Claude controlling a browser — the static screenshot doesn't fully capture the animation chrome.
