---
version: alpha
name: HashiCorp-design-analysis
description: "An enterprise-infrastructure marketing canvas built around a near-black ground (#000000) and a system of per-product accent colors — Terraform purple, Vault yellow, Consul pink, Waypoint cyan, Vagrant blue — that act as identity tokens rather than decorative palette. Display type is hashicorpSans set in 600/700 with tight 1.17–1.21 line-heights; body type runs the same family at 500 weight with relaxed 1.50–1.71 line-heights. Cards live as charcoal surfaces with 1px translucent gray borders; product showcase cards lift into per-product chromatic gradients. The system reads as confident, technical, and intentionally multi-product — every section quietly signals which HashiCorp tool it represents."

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  accent-blue: "#2b89ff"
  ink: "#ffffff"
  ink-muted: "#b2b6bd"
  ink-subtle: "#656a76"
  canvas: "#000000"
  surface-1: "#15181e"
  surface-2: "#1f232b"
  surface-3: "#3b3d45"
  surface-card: "#15181e"
  hairline: "#3b3d45"
  hairline-soft: "#252830"
  hairline-strong: "#8a8f99"
  text-dim: "#b2b6bd"
  focus: "#2b89ff"
  focus-inset: "#000000"
  inverse-canvas: "#ffffff"
  inverse-ink: "#000000"
  product-terraform: "#7b42bc"
  product-terraform-bright: "#911ced"
  product-vault: "#ffcf25"
  product-consul: "#e62b1e"
  product-waypoint: "#14c6cb"
  product-waypoint-deep: "#12b6bb"
  product-vagrant: "#1868f2"
  product-nomad: "#00ca8e"
  product-boundary: "#f24c53"
  amber-100: "#fbeabf"
  amber-200: "#bb5a00"
  blue-7: "#101a59"
  semantic-success: "#00ca8e"
  semantic-warning: "#ffcf25"
  semantic-error: "#e62b1e"
  semantic-visited: "#a737ff"

typography:
  display-xl:
    fontFamily: hashicorpSans
    fontSize: 80px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: -2.5px
  display-lg:
    fontFamily: hashicorpSans
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -1.6px
  display-md:
    fontFamily: hashicorpSans
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.19
    letterSpacing: -1.0px
  headline:
    fontFamily: hashicorpSans
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.21
    letterSpacing: -0.6px
  card-title:
    fontFamily: hashicorpSans
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.4px
  subhead:
    fontFamily: hashicorpSans
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  body-lg:
    fontFamily: hashicorpSans
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.69
    letterSpacing: 0
  body:
    fontFamily: hashicorpSans
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: hashicorpSans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.71
    letterSpacing: 0
  caption:
    fontFamily: hashicorpSans
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  button:
    fontFamily: hashicorpSans
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  eyebrow:
    fontFamily: hashicorpSans
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.6px

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
  pill: 9999px
  full: 9999px

spacing:
  hair: 1px
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

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
    backgroundColor: "{colors.inverse-canvas}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  button-primary-pressed:
    backgroundColor: "{colors.inverse-canvas}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  button-product-terraform:
    backgroundColor: "{colors.product-terraform}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  button-product-vault:
    backgroundColor: "{colors.product-vault}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  button-product-waypoint:
    backgroundColor: "{colors.product-waypoint}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
  product-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  product-card-terraform:
    backgroundColor: "{colors.product-terraform}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  product-card-vault:
    backgroundColor: "{colors.product-vault}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  product-card-waypoint:
    backgroundColor: "{colors.product-waypoint}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  feature-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  pricing-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-card-featured:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 32px
  resource-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 16px
  text-input:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px 14px
  text-input-focused:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px 14px
  product-pill:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 64px
  comparison-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  cta-banner:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.subhead}"
    rounded: "{rounded.xxl}"
    padding: 48px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 32px
---

## Overview

HashiCorp's marketing canvas is a near-black ground that serves a multi-product portfolio without ever feeling generic. The dominant surface is `{colors.canvas}` (pure black) layered with `{colors.surface-1}` charcoal cards and 1px translucent gray hairlines. The chrome is monochrome — white pill-rounded buttons (`{components.button-primary}`), white type, gray secondary type — but the system is held together by a **palette of per-product accent colors** that signal which HashiCorp tool a given section belongs to: Terraform purple, Vault yellow, Consul red, Waypoint cyan, Vagrant blue, Nomad green, Boundary coral.

Display type is **hashicorpSans** at weights 600/700 with tight line-heights (1.17–1.21); body type is the same family at 500 weight with deliberately relaxed line-heights (1.50–1.71) — the contrast feels editorial, not enterprise-templated. CTAs use small `{rounded.md}` 8px corners rather than pills, which keeps the system reading as developer-facing rather than consumer-y.

The signature device is the **product-card** family — each HashiCorp product gets its own colored card variant on the home and infrastructure pages, lifting Terraform into a violet ground, Vault into yellow, Waypoint into cyan. These aren't decorative gradients — they're identity surfaces. A reader scrolling the page can tell which product a section is about from the corner of their eye.

**Key Characteristics:**
- Black-canvas marketing system: `{colors.canvas}` is the surface for hero, body, pricing, comparison tables, and footer alike.
- **Per-product color identity**: Terraform `{colors.product-terraform}`, Vault `{colors.product-vault}`, Waypoint `{colors.product-waypoint}`, Vagrant `{colors.product-vagrant}`, Consul `{colors.product-consul}`, Nomad `{colors.product-nomad}`, Boundary `{colors.product-boundary}` — each with its own button + card variant.
- Display headlines run hashicorpSans 600/700 with line-height 1.17–1.21 (tight); body runs the same family at 500 with 1.50–1.71 (relaxed) — the proportional gap is the brand's voice.
- CTA shape is `{rounded.md}` 8px — not a pill — keeping the system reading as developer-tool rather than consumer-app.
- Charcoal surface lift (canvas → surface-1 → surface-2) instead of shadow-driven elevation.
- 1px translucent gray hairlines (`rgba(178,182,189,0.1)`) define cards and dividers — the borders are felt more than seen.
- Eyebrow typography (12–13px, 600 weight, 0.6px positive tracking, uppercase) marks every section as a category label.

## Colors

> Source pages: hashicorp.com/en (home), /en/infrastructure-cloud, /en/products/terraform, /en/pricing, /en/resources?contentType=PDF.

### Brand & Accent
- **Black** ({colors.primary}): The system primary surface. Canvas, footer, comparison tables, hero — all black.
- **White** ({colors.on-primary}): Inverse text on black; canvas of `button-primary`.
- **Accent Blue** ({colors.accent-blue}): Hyperlinks across the marketing surface.
- **Visited Purple** ({colors.semantic-visited}): Visited-link state.

### Surface
- **Canvas** ({colors.canvas}): Default page background.
- **Surface 1** ({colors.surface-1}): Charcoal one step above canvas — feature cards, pricing cards, resource tiles.
- **Surface 2** ({colors.surface-2}): Two steps above — featured pricing card, secondary buttons, hovered product chrome.
- **Surface 3** ({colors.surface-3}): Three steps above — small chips, badges, sub-nav backgrounds.
- **Surface Card** ({colors.surface-card}): Role alias for `{colors.surface-1}` — the same extracted charcoal (#15181e), named so the card/panel role is addressable by role rather than by ladder position. Not a new value.
- **Hairline** ({colors.hairline}): 1px borders on cards and dividers. **Decorative only** — at 1.94:1 on `{colors.canvas}` it is below the 3:1 WCAG 1.4.11 boundary minimum, so it may not be the sole indicator of a control's edge.
- **Hairline Soft** ({colors.hairline-soft}): Subtler dividers — comparison-table rows. **Decorative only**, 1.42:1 on `{colors.canvas}`.
- **Hairline Strong** ({colors.hairline-strong}): **Prescribed, not extracted.** A parallel accessible boundary token for edges that must be seen — text-input borders, focusable card outlines, any boundary that carries meaning. 6.47:1 on `{colors.canvas}` and 5.48:1 on `{colors.surface-card}`. HashiCorp's real hairlines do not clear 3:1; this token exists so an implementation does not have to falsify them.
- **Inverse Canvas** ({colors.inverse-canvas}): Pure white — used as the surface of `button-primary` only.

### Text
- **Ink** ({colors.ink}): All headline and emphasized body type — pure white.
- **Ink Muted** ({colors.ink-muted}): Secondary type at #b2b6bd — meta info, footer columns.
- **Ink Subtle** ({colors.ink-subtle}): Tertiary type at #656a76 — form helper text, timestamps, footnotes. Measures 3.88:1 on `{colors.canvas}` and 3.28:1 on `{colors.surface-card}` — **below AA for normal text**. Restrict it to 18.66px+/700 or 24px+ type, or substitute `{colors.text-dim}`.
- **Text Dim** ({colors.text-dim}): Role alias for `{colors.ink-muted}` — the same extracted #b2b6bd, named for the secondary-text role. 10.32:1 on `{colors.canvas}`, 8.74:1 on `{colors.surface-card}`. This is the accessible secondary ink; `{colors.ink-subtle}` is not.

### Focus

- **Focus** ({colors.focus}): The focus ring, reusing the brand's own link blue #2b89ff. **Prescribed** — HashiCorp's live ring was not measured. 6.12:1 on `{colors.canvas}`, 5.19:1 on `{colors.surface-1}`, 4.59:1 on `{colors.surface-2}`, 3.16:1 on `{colors.surface-3}`, 3.43:1 on `{colors.inverse-canvas}` (the white `button-primary`).
- **Focus Inset** ({colors.focus-inset}): The ring's 1px inner edge, black. Separates from the blue outer band at 6.12:1. It exists because no single ring clears 3:1 against both the black canvas and the chromatic product grounds: blue sits at 1.03:1 on Boundary coral and 1.63:1 on Waypoint cyan. On a `product-card-*` ground the black inner band is the carrier (3.35:1 on Terraform purple through 14.2:1 on Vault yellow); on the dark canvas the blue outer band is.

### Per-Product Identity (signature)
HashiCorp's marketing isn't held together by a single accent color — it's held together by a system of product-specific accents, each used to mark which tool a section represents.

- **Terraform Purple** ({colors.product-terraform}): Terraform sections, terraform CTAs, the violet 3D cube on the home hero.
- **Terraform Bright** ({colors.product-terraform-bright}): Saturated highlight — link emphasis on Terraform pages.
- **Vault Yellow** ({colors.product-vault}): Vault sections and CTAs.
- **Consul Red** ({colors.product-consul}): Consul sections.
- **Waypoint Cyan** ({colors.product-waypoint}): Waypoint sections, deep variant `{colors.product-waypoint-deep}` for hover/active.
- **Vagrant Blue** ({colors.product-vagrant}): Vagrant sections.
- **Nomad Green** ({colors.product-nomad}): Nomad sections.
- **Boundary Coral** ({colors.product-boundary}): Boundary sections.

### Semantic
- **Success** ({colors.semantic-success}): Positive states (also reused as Nomad green).
- **Warning** ({colors.semantic-warning}): Warning states (also Vault yellow).
- **Error** ({colors.semantic-error}): Error states (also Consul red).
- **Amber 100** ({colors.amber-100}): Soft warm highlight — extracted but used sparingly.
- **Amber 200** ({colors.amber-200}): Saturated amber for caution badges.
- **Blue 7** ({colors.blue-7}): Deep navy used in unified-core gradients.

## Typography

### Font Family

- **hashicorpSans** — HashiCorp's proprietary marketing typeface. Geometric, clean, slightly humanist. Fallback stack `__hashicorpSans_Fallback_96f0ca` (system font), then `-apple-system, BlinkMacSystemFont, Segoe UI, helvetica, arial`.

The same family carries display, body, button, and caption — no separate display + body pairing. Hierarchy is carried by weight (500 body / 600 emphasis / 700 display) and by a deliberate line-height contrast (tight on display, relaxed on body).

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 80px | 700 | 1.17 | -2.5px | Largest hero headline |
| `{typography.display-lg}` | 56px | 700 | 1.18 | -1.6px | Section opener headlines |
| `{typography.display-md}` | 40px | 600 | 1.19 | -1.0px | Sub-section headlines |
| `{typography.headline}` | 28px | 600 | 1.21 | -0.6px | Pricing tier titles, CTA banner heading |
| `{typography.card-title}` | 22px | 600 | 1.18 | -0.4px | Feature card title |
| `{typography.subhead}` | 20px | 600 | 1.35 | -0.2px | Long-form intro paragraphs |
| `{typography.body-lg}` | 18px | 500 | 1.69 | 0 | Hero subhead, lead body |
| `{typography.body}` | 16px | 500 | 1.50 | 0 | Default body |
| `{typography.body-sm}` | 14px | 500 | 1.71 | 0 | Card body, footer columns |
| `{typography.caption}` | 13px | 500 | 1.38 | 0.2px | Meta, comparison cell labels |
| `{typography.button}` | 14px | 600 | 1.29 | 0 | Pill / square CTA buttons |
| `{typography.eyebrow}` | 12px | 600 | 1.23 | 0.6px | Uppercase section eyebrows |

### Principles

- **Tight on display, relaxed on body.** Display sits at line-height 1.17–1.21; body lifts to 1.50–1.71. The size + line-height contrast carries hierarchy.
- **Weight hierarchy is small.** 500 body / 600 emphasis / 700 display. No light / black extremes — the brand reads as engineered.
- **Eyebrow positive-tracked uppercase 12px is the section header.** Every meaningful section has one above the headline.
- **No mono.** Despite being a developer-tools brand, the marketing surface uses no monospace face — code voice is reserved for in-product surfaces.

### Note on Font Substitutes

If implementing without hashicorpSans, suitable open-source substitutes include **Inter** (closest geometric character set), **Geist Sans**, or **IBM Plex Sans**. Inter at weights 500 / 600 / 700 closely approximates hashicorpSans's proportions; expect to manually adjust line-heights down by ~0.02 to match.

## Layout

### Spacing System

- **Base unit**: 8px (the primary increments are 4 / 8 / 12 / 16 / 24 / 32 / 48).
- **Tokens (front matter)**: `{spacing.hair}` 1px · `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- Card interior padding: `{spacing.lg}` 24px on product cards; `{spacing.xl}` 32px on pricing cards; `{spacing.xxl}` 48px on CTA banners.
- Button padding: 10px vertical · 18px horizontal on `{components.button-primary}`.
- Universal rhythm constant: `{spacing.section}` (96px) vertical gap between major sections.

### Grid & Container

- Max content width sits around 1280px with side gutters scaling from `{spacing.xxl}` on desktop down to `{spacing.lg}` on mobile.
- Product card grids are 3-up on desktop, 2-up at tablet, 1-up on mobile.
- Pricing tier grid is 3-up across desktop; comparison table beneath uses fixed-width left column.
- Resource directory (PDF library) uses 4-up dense thumbnail grid.

### Whitespace Philosophy

The dark canvas IS the whitespace. Sections separate by surface lift (canvas → surface-1) rather than by gaps in white. Within a section, generous `{spacing.xl}` 32px gaps separate cards; `{spacing.lg}` 24px separates rows.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Canvas-mounted display type, hero, footer |
| 1 (charcoal lift) | `{colors.surface-1}` background + 1px `rgba(178,182,189,0.1)` border | Default cards, resource tiles, pricing cards |
| 2 (surface-2 lift) | `{colors.surface-2}` background + 1px `{colors.hairline}` border | Featured pricing card, hovered cards, sub-nav |
| 3 (product chromatic) | Per-product accent color background — Terraform purple, Vault yellow, Waypoint cyan | Product showcase cards |

The product chromatic level isn't a "modal lift" — it's an identity device. A Terraform card sits at the same z-plane as a feature-card; the difference is meaning, not depth.

### Decorative Depth

- **3D product visuals** — isometric purple cubes (Terraform), translucent yellow safes (Vault), and similar product-tinted illustrations sit in the right column of hero sections.
- **1px translucent gray hairlines** are the dominant edge — borders are visible without competing.
- **No drop shadows on dark.** Cards lift via surface change, never shadow.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Small chips / badges |
| `{rounded.sm}` | 6px | Inline tag |
| `{rounded.md}` | 8px | All CTA buttons, form inputs, list items |
| `{rounded.lg}` | 12px | Feature cards, product cards, pricing cards |
| `{rounded.xl}` | 16px | Large illustrative tiles |
| `{rounded.xxl}` | 24px | CTA banner panels |
| `{rounded.pill}` | 9999px | Eyebrow-style product pills (small chips) |
| `{rounded.full}` | 9999px | Avatar circles (rare on marketing) |

### Photography & Illustration Geometry

- Product 3D illustrations use full-bleed within their container — no rounded inner mask.
- Logo chips in the customer marquee sit on `{rounded.sm}` 6px tiles with 1px hairline.
- Resource thumbnails use `{rounded.lg}` 12px corners.

## Components

### Buttons

**`button-primary`** — White rounded-rect CTA. Used as primary CTA on all pages.
- Background `{colors.inverse-canvas}`, text `{colors.inverse-ink}`, type `{typography.button}`, padding 10px 18px, rounded `{rounded.md}`.
- Pressed state lives in `button-primary-pressed`.

**`button-secondary`** — Charcoal rounded-rect. Secondary CTA, "Read docs" / "Talk to sales".
- Background `{colors.surface-2}`, text `{colors.ink}`, type `{typography.button}`, rounded `{rounded.md}`, padding 10px 18px.

**`button-tertiary`** — Bare ghost button on canvas with text-only treatment.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.button}`, rounded `{rounded.md}`, padding 10px 18px.

**`button-product-terraform`** — Terraform-tinted CTA on Terraform pages.
- Background `{colors.product-terraform}`, text `{colors.ink}`, type `{typography.button}`, rounded `{rounded.md}`, padding 10px 18px.

**`button-product-vault`** — Vault-yellow CTA.
- Background `{colors.product-vault}`, text `{colors.inverse-ink}` (yellow needs dark text), type `{typography.button}`, rounded `{rounded.md}`, padding 10px 18px.

**`button-product-waypoint`** — Waypoint-cyan CTA.
- Background `{colors.product-waypoint}`, text `{colors.inverse-ink}`, type `{typography.button}`, rounded `{rounded.md}`, padding 10px 18px.

(Vagrant blue, Nomad green, Consul red, Boundary coral follow the same pattern with their respective `{colors.product-*}` token.)

### Cards & Containers

**`product-card`** — Default product showcase card — surface-1 charcoal.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 24px.

**`product-card-terraform`** — Product card with Terraform purple ground (used as identity surface, not modal elevation).
- Background `{colors.product-terraform}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 24px.

**`product-card-vault`** — Vault-yellow ground.
- Background `{colors.product-vault}`, text `{colors.inverse-ink}`, otherwise identical structure.

**`product-card-waypoint`** — Waypoint-cyan ground.
- Background `{colors.product-waypoint}`, text `{colors.inverse-ink}`, otherwise identical structure.

(Other product variants follow the same shape with their respective product token.)

**`feature-card`** — Generic feature highlight on surface-1.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 24px.

**`pricing-card`** — Pricing tier on `/en/pricing`.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 32px.

**`pricing-card-featured`** — Recommended tier (visually emphasized via surface lift).
- Background `{colors.surface-2}`, otherwise identical structure.

**`resource-card`** — PDF / whitepaper / guide tile in the resources directory.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body-sm}`, rounded `{rounded.lg}`, padding 16px.

### Inputs & Forms

**`text-input`** + **`text-input-focused`** — Form fields on pricing seat-count and contact forms.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.md}`, padding 10px 14px.
- Focused state retains the same surface; the focus ring is a 2px `{colors.focus}` outline with a 1px `{colors.focus-inset}` inner edge, offset 2px. The resting border uses `{colors.hairline-strong}`, not `{colors.hairline}` — an input's edge is a control boundary and must clear 3:1.

### Pills & Chips

**`product-pill`** — Small product-name chip used above hero headlines and on resource cards to label which product a piece of content belongs to.
- Background `{colors.surface-1}`, text `{colors.ink-muted}`, type `{typography.caption}`, rounded `{rounded.pill}`, padding 4px 10px.

### Comparison Table

**`comparison-row`** — Single row inside the pricing comparison table.
- Background `{colors.canvas}`, text `{colors.ink-muted}`, type `{typography.body-sm}`. Row separator is `{colors.hairline-soft}`.

### CTA Banner

**`cta-banner`** — Large rounded panel used at the bottom of long-form pages with a closing CTA.
- Background `{colors.surface-1}`, text `{colors.ink}`, type `{typography.subhead}`, rounded `{rounded.xxl}`, padding 48px.

### Navigation

**`top-nav`** — Sticky black bar with HashiCorp logomark left, primary nav links centered, and a `button-primary` ("Sign up") + `button-secondary` ("Sign in") pair right.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-sm}`, height 64px.
- Mobile: collapses primary links into a hamburger; the primary CTA remains visible.

### Footer

**`footer`** — Dense link grid on `{colors.canvas}` with the wordmark at left and 5–6 columns of caption-sized links.
- Background `{colors.canvas}`, text `{colors.ink-muted}`, type `{typography.caption}`, padding 64px 32px.

### States

Only `button-primary-pressed` and `text-input-focused` were observable as separate
extracted entries; the rest of this table is **prescribed** from the system's own
surface-lift logic — no state was measured off the live site beyond those two.

| Component | Default | Hover | Focus-visible | Active / pressed | Disabled | Loading | Selected | Error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.inverse-canvas}` ground | ground drops to `{colors.text-dim}` | 2px `{colors.focus}` ring + 1px `{colors.focus-inset}` inner edge, 2px offset | `button-primary-pressed`, opacity 0.85 | 40% opacity, `cursor: not-allowed`, no ring | label swaps for an indeterminate bar in `{colors.inverse-ink}` | n/a — not a toggle | n/a — errors surface on the form, not the button |
| `button-secondary` | `{colors.surface-2}` ground | lifts to `{colors.surface-3}` | same ring | ground returns to `{colors.surface-2}`, opacity 0.9 | 40% opacity, no ring | indeterminate bar in `{colors.ink}` | n/a | n/a |
| `button-tertiary` | bare on `{colors.canvas}` | ground fades up to `{colors.surface-1}` | same ring | opacity 0.9 | 40% opacity | inherits `button-secondary` loading | n/a | n/a |
| `button-product-*` | product ground | deep variant (e.g. `{colors.product-waypoint-deep}`) | same ring; on a chromatic ground the `{colors.focus-inset}` band carries visibility | opacity 0.9 | 40% opacity | indeterminate bar in the entry's own text color | n/a | n/a |
| `text-input` | `{colors.hairline-strong}` 1px border | border to `{colors.text-dim}` | `text-input-focused` — 2px `{colors.focus}` ring, 1px `{colors.focus-inset}` inner edge | n/a — no pressed state on a field | 40% opacity, border to `{colors.hairline}` | trailing spinner, field stays editable | n/a | border and helper text to `{colors.semantic-error}`, message in `{typography.caption}` |
| `product-card` / `product-card-*` | surface or product ground | border to `{colors.hairline-strong}`, no travel | ring on the card, not on the inner link | opacity 0.95 | not used — marketing cards are never disabled | skeleton block in `{colors.surface-2}` | 2px `{colors.focus}` left edge when it is the active tab panel | n/a |
| `feature-card` / `resource-card` | `{colors.surface-1}` | lifts to `{colors.surface-2}` | same card ring | opacity 0.95 | not used | skeleton block in `{colors.surface-2}` | n/a | n/a |
| `pricing-card` | `{colors.surface-1}` | border to `{colors.hairline-strong}` | same card ring | n/a | n/a | n/a | `pricing-card-featured` is the selected tier | n/a |
| `product-pill` | `{colors.surface-1}` | ground to `{colors.surface-2}` | same ring | n/a | n/a | n/a | ground to the section's `{colors.product-*}` token | n/a |
| `top-nav` link | `{colors.ink}` | underline in `{colors.focus}` | same ring | opacity 0.9 | n/a | n/a | current section marked with a 2px `{colors.focus}` underline | n/a |
| `comparison-row` | `{colors.canvas}` | row ground to `{colors.surface-1}` | n/a — rows are not focusable | n/a | n/a | n/a | n/a | n/a |
| `cta-banner`, `footer` | static | no hover | n/a — containers, not controls | n/a | n/a | n/a | n/a | n/a |

`cta-banner` and `footer` genuinely have two states each: present and absent.
Their contained links take the link states above.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** No timing function, duration or easing curve
below was extracted from hashicorp.com; they are the audit's **Crisp** profile,
assigned because HashiCorp is an infrastructure and developer-tool identity
(SPEC section 5, rule 2). Nothing here should be read as a recorded fact about
the real site.

Crisp fits the brand for the same reason the 8px CTA corner does: the system
reads as a tool, not a consumer app. State changes should land immediately,
with no entrance choreography and no bounce. The per-product chromatic cards
are identity surfaces, not stage sets — they appear, they do not perform.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, nav link) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `transform` (no travel on cards) | Colour and opacity change applies instantly; no transform |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`, `transform: scale(0.99)` | Opacity only, `{motion.duration-reduced}`; scale removed |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears with no transition — it must never lag the key press |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` only | Cross-fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px → 0)` | Opacity fade at `{motion.duration-reduced}`; translate removed |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Opacity fade at `{motion.duration-reduced}` |
| Dropdown / nav mega-menu | `{motion.duration-fast}` enter, `{motion.duration-instant}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px → 0)` | Opacity only, `{motion.duration-reduced}` |
| Toast | `{motion.duration-base}` enter, `{motion.duration-fast}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px → 0)` | Opacity only, `{motion.duration-reduced}`; auto-dismiss timer unchanged |
| List enter (product-card, resource grid) | `{motion.duration-base}` per item, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity`, `transform: translateY(6px → 0)` | All items fade together at `{motion.duration-reduced}`; stagger and travel removed |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Opacity only, `{motion.duration-reduced}`, no stagger |
| Loading (button bar, card skeleton) | `{motion.duration-emphasis}` loop | `{motion.ease-standard}` | `opacity`, `transform: translateX` on the sweep | Loop frozen; a static skeleton block and `aria-busy` carry the state |

Rules this file holds itself to:

- Animate `transform` and `opacity` only. Never animate `width`, `height`,
  `top`, `left` or `margin` — no layout-triggering property is in the table above.
- Every exit is shorter than its matching entrance (`{motion.duration-fast}`
  against `{motion.duration-base}`).
- Nothing animates on first paint. The hero headline and its 3D product visual
  are painted, not revealed; `{motion.duration-emphasis}` exists for the
  loading sweep, not for an entrance.
- The only infinite animation is the loading sweep. HashiCorp's marketing
  surface has no brand ambience loop, so none is specified.
- Hover on a `product-card-*` changes border and opacity only. The chromatic
  ground never shifts hue on hover — a product colour that moves stops reading
  as that product's identity.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale, the 20ms list stagger,
     and the infinite loading sweep (frozen to a static skeleton). */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (100ms),
     and the focus ring, which is never animated away. */
  *, *::before, *::after {
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;
    transition-property: opacity !important;
  }
}
```

## Accessibility

Every ratio below was computed from this file's own frontmatter hexes with
WCAG 2.1 relative luminance. Tap-target, overlap and frame-rate claims cannot
be verified from a document, so the figures under "Touch Targets" in
Responsive Behavior are the design intent, not a measurement.

### Measured contrast — key pairs

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 21.0:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-card}` | 17.78:1 | 4.5:1 | Pass |
| `{colors.text-dim}` / `{colors.ink-muted}` on `{colors.canvas}` | 10.32:1 | 4.5:1 | Pass |
| `{colors.text-dim}` on `{colors.surface-card}` | 8.74:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 21.0:1 | 4.5:1 | Pass |
| `{colors.accent-blue}` on `{colors.canvas}` | 6.12:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 6.47:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.surface-card}` | 5.48:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.canvas}` | 6.12:1 | 3.0:1 | Pass |

### Where the real brand fails AA

These are extracted HashiCorp values. They are **not** corrected here, because a
falsified hex would make this document wrong. Each is scoped to decoration or to
large type instead, with an accessible parallel token named.

| Foreground / Background | Ratio | Required | Scope that makes it defensible |
|---|---|---|---|
| `hairline` on `{colors.canvas}` | 1.94:1 | 3.0:1 | Decorative divider only. Use `{colors.hairline-strong}` for any control boundary. |
| `hairline` on `{colors.surface-card}` | 1.64:1 | 3.0:1 | Same scope: card edge as texture, never as the sole edge of a control. |
| `hairline-soft` on `{colors.canvas}` | 1.42:1 | 3.0:1 | Comparison-table row rule. The table is also readable by cell alignment and text, so the rule is not load-bearing. |
| `hairline-soft` on `{colors.surface-card}` | 1.21:1 | 3.0:1 | Decorative inner divider only. |
| `ink-subtle` on `{colors.canvas}` | 3.88:1 | 4.5:1 | Clears 3:1, so it is usable at 24px+, or 18.66px+ at weight 700. At 13–16px it fails; use `{colors.text-dim}` there. |
| `ink-subtle` on `{colors.surface-card}` | 3.28:1 | 4.5:1 | Same: large text only, and it is close to the 3:1 floor on charcoal. |
| `{colors.product-boundary}` / `{colors.ink}` | 3.54:1 | 4.5:1 | White on Boundary coral is large-text-only (24px+). `{colors.inverse-ink}` on the same ground reaches 5.93:1 and is the safer pairing. |
| `{colors.product-consul}` / `{colors.ink}` | 4.44:1 | 4.5:1 | White on Consul red misses AA by 0.06. Use `{colors.inverse-ink}` (4.73:1) or reserve for 24px+ display type. |
| `{colors.product-terraform-bright}` on `{colors.canvas}` | 3.59:1 | 4.5:1 | Link-emphasis tint on Terraform pages — large text or non-text use only; body links use `{colors.accent-blue}` (6.12:1). |
| `{colors.blue-7}` on `{colors.canvas}` | 1.31:1 | — | Gradient stop, never text and never a boundary. No threshold applies. |

### Focus ring visibility, per surface this file defines

The ring is 2px `{colors.focus}` with a 1px `{colors.focus-inset}` inner edge
and a 2px offset. One band is always the carrier:

| Surface | `{colors.focus}` ratio | `{colors.focus-inset}` ratio | Carrier |
|---|---|---|---|
| `{colors.canvas}` #000000 | 6.12:1 | 1.0:1 | Blue outer band |
| `{colors.surface-1}` / `{colors.surface-card}` | 5.19:1 | 1.18:1 | Blue outer band |
| `{colors.surface-2}` | 4.59:1 | 1.33:1 | Blue outer band |
| `{colors.surface-3}` | 3.16:1 | 1.94:1 | Blue outer band, at the 3:1 floor |
| `{colors.inverse-canvas}` (white `button-primary`) | 3.43:1 | 21.0:1 | Either; the black inner edge dominates |
| `{colors.product-terraform}` | 1.83:1 | 3.35:1 | Black inner band |
| `{colors.product-vault}` | 2.32:1 | 14.2:1 | Black inner band |
| `{colors.product-waypoint}` | 1.63:1 | 9.97:1 | Black inner band |
| `{colors.product-vagrant}` | 1.42:1 | 4.3:1 | Black inner band |
| `{colors.product-boundary}` | 1.03:1 | 5.93:1 | Black inner band |

No single ring colour clears 3:1 against both the black canvas and the
chromatic product grounds, which is why the ring is two-tone rather than a
`focus` / `focus-on-dark` pair.

### Minimum tap target

- Design intent is 44x44px for every interactive element on touch viewports;
  `button-primary` and `button-secondary` are specified at ≥40px tall on
  desktop and should be padded to 44px below 768px.
- `product-pill` at 24px tall on desktop is below 44px. Where a pill is a link
  or filter rather than a label, it needs the touch-viewport 28px height plus
  invisible padding to reach 44px. **Unverifiable from this document** — it
  needs a rendered page.

### Reduced motion

`@media (prefers-reduced-motion: reduce)` removes all translate and scale, drops
the `{motion.stagger-step}` list stagger, and freezes the loading sweep to a
static skeleton with `aria-busy`. Opacity fades remain, capped at
`{motion.duration-reduced}` (100ms). The focus ring is never animated, so it is
unaffected.

### Other accessibility notes

- Per-product colour is the system's primary signal for "which tool is this
  section about". Colour alone is not an accessible signal, so every product
  section also carries its product name in the `product-pill`
  (`{typography.caption}`) and in the eyebrow (`{typography.eyebrow}`).
- `{colors.semantic-success}` (9.84:1), `{colors.semantic-warning}` (14.2:1)
  and `{colors.semantic-error}` (4.73:1) all clear AA as text on
  `{colors.canvas}`. `{colors.semantic-visited}` reaches 4.63:1.
- The brand is dark-only by design (see Don'ts). There is no light-mode token
  set to audit, so no light-mode ratio is claimed.

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
| best ring `{colors.focus}` (`#2b89ff`) against `{colors.product-waypoint}` (`#14c6cb`) | 1.63:1 | 3.0:1 | Fail — no focus ring this file declares reaches 3:1 on that surface |
| best ring `{colors.focus}` (`#2b89ff`) against `{colors.product-terraform}` (`#7b42bc`) | 1.83:1 | 3.0:1 | Fail — no focus ring this file declares reaches 3:1 on that surface |
| best ring `{colors.focus}` (`#2b89ff`) against `{colors.product-vault}` (`#ffcf25`) | 2.32:1 | 3.0:1 | Fail — no focus ring this file declares reaches 3:1 on that surface |
| `{colors.semantic-visited}` (`#a737ff`) on `{colors.surface-1}` (`#15181e`) | 3.92:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.semantic-error}` (`#e62b1e`) on `{colors.surface-1}` (`#15181e`) | 4.00:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do

- Reserve `{colors.canvas}` (black) and `{colors.surface-1}` (charcoal) as the system's two anchor surfaces. Every band of the page is one or the other.
- When introducing a section about a specific HashiCorp product, use that product's `{colors.product-*}` token consistently — for the section pill, the CTA button, and (where appropriate) the showcase card background.
- Use `{rounded.md}` 8px on CTA buttons; HashiCorp's brand reads as engineered, not consumer.
- Pair tight display line-heights (1.17–1.21) with relaxed body line-heights (1.50–1.71). The contrast IS the brand voice.
- Use the eyebrow typography (`{typography.eyebrow}`, uppercase, 0.6px tracking) above every meaningful section.
- Use surface lift (canvas → surface-1 → surface-2) to express hierarchy on dark.
- Reserve product-chromatic cards for product identity; keep generic feature cards on `{colors.surface-1}`.

### Don't

- Don't ship a light-mode marketing page. HashiCorp's marketing brand IS dark.
- Don't introduce mid-tone gray text outside the documented `ink` / `ink-muted` / `ink-subtle` set.
- Don't square off CTA corners — use `{rounded.md}` 8px, not 0px.
- Don't use a product accent color for a CTA on a page that isn't about that product. Terraform purple on the Vault page is a brand violation.
- Don't combine multiple product accents in the same viewport — the system says "this section is about THIS tool", and mixing accents breaks that signal.
- Don't add drop shadows on dark; surface lift carries elevation.
- Don't let a state change take longer than `{motion.duration-base}` (150ms). The system should feel like a tool responding, not a page performing.
- Don't animate `width`, `height`, `top`, `left` or `margin`; `transform` and `opacity` only.
- Don't use `{colors.hairline}` or `{colors.hairline-soft}` as the only edge of a control — both are below 3:1. Reach for `{colors.hairline-strong}`.
- Don't suppress the focus ring. Both of its bands are needed: blue on dark grounds, the black inner edge on product-chromatic grounds.
- Don't replace `hashicorpSans` with a display-only sans for headlines and a different family for body. The brand is held together by one family across the full hierarchy.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop-XL | 1440px | Default desktop layout |
| Desktop | 1280px | Pricing 3-up grid maintained |
| Tablet | 1024px | Product card grid 3-up → 2-up |
| Mobile-Lg | 768px | Pricing comparison becomes per-tier accordion; nav becomes hamburger |
| Mobile | 480px | Single-column everything; display-xl scales 80px → ~36px |

### Touch Targets

- CTA buttons (`button-primary`, `button-secondary`) maintain ≥40px tap height across viewports.
- Product pills are 24px tall on desktop and grow to 28px on touch viewports.
- Form inputs hold ≥44px tap target on touch viewports.

### Collapsing Strategy

- **Nav**: horizontal nav with right-anchored CTAs collapses to a hamburger overlay below 768px. The primary CTA stays visible on the bar.
- **Product card grid**: 3-up → 2-up at 1024px → 1-up below 768px.
- **Pricing comparison table**: collapses into per-tier accordions below 768px to avoid horizontal scroll.
- **Display type**: `{typography.display-xl}` 80px scales toward `{typography.display-md}` 40px on mobile while preserving the negative-tracking percentage.

### Image Behavior

- 3D product illustrations (cubes, safes, etc.) maintain aspect ratio and never crop; below 768px they shrink rather than reflow.
- Customer logo marquee scales horizontally and may wrap to a second row at narrow widths.

## Iteration Guide

1. Focus on ONE component at a time and reference it by its `components:` token name.
2. When introducing a new section, decide first whether it's a generic feature (surface-1) or a product-identity section (product-* color).
3. Default body to `{typography.body}` at 500 weight; reach for `{typography.subhead}` only inside CTA banners and feature cards.
4. Run `npx @google/design.md lint DESIGN.md` after edits.
5. Add new product variants as separate component entries (`product-card-nomad`, `button-product-consul`, etc.).
6. Treat the per-product palette as identity tokens, not decoration. If you reach for a product color outside its product context, the brand is drifting.
7. Eyebrow type is mandatory above every section — skipping it makes sections read as floating.

## Known Gaps

- The exact product-color hex values come from the `--mds-color-*` CSS variable set extracted directly; they are HashiCorp's canonical brand spec.
- Shadow tokens are not extensively documented because the dark surface system uses surface lift instead of shadow elevation.
- Form-field error and validation styling is not visible on the inspected pages.
- Dark mode is the only marketing mode — light-mode adaptation is not documented.
- **Motion is prescribed, not extracted.** No duration, easing curve or stagger in Motion & Animation was measured from hashicorp.com; the whole block is the audit's Crisp profile.
- **The focus ring is prescribed.** `{colors.focus}` reuses the brand's own link blue and `{colors.focus-inset}` is black, but the ring's real geometry on hashicorp.com was not observed.
- `{colors.hairline-strong}` is prescribed. HashiCorp's real hairlines are `rgba(178,182,189,0.1)` over dark and do not clear 3:1 at any blend; the strong token is the audit's accessible substitute, not a brand value.
- `{colors.surface-card}` and `{colors.text-dim}` are role aliases of `{colors.surface-1}` and `{colors.ink-muted}`. They add no new hex.
- Component states beyond `button-primary-pressed` and `text-input-focused` are prescribed from the surface-lift ladder, not observed. Loading, selected and error treatments in particular were not visible on the inspected marketing pages.
- Tap-target sizes, overlap and frame rate cannot be verified from a document. Every figure under Touch Targets is intent.
- Product-card variants for Consul, Nomad, Vagrant, and Boundary follow the documented Terraform / Vault / Waypoint pattern but are referenced in prose only; if they need formal entries they can be added as `product-card-consul`, `product-card-nomad`, etc.
