---
version: alpha
name: Clay-design-analysis
description: A vibrant claymation-meets-data interface for Clay.com (GTM data-orchestration platform). Anchors on white canvas with dark-navy primary CTAs, custom rounded display type, and saturated single-color feature cards — hot pink, deep teal, lavender, peach, ochre — that punctuate long-scroll explainer pages. Brand voltage comes from 3D-rendered claymation illustrations (mountains, characters, mascots) used as full-bleed hero artifacts and the bright multi-color card surfaces showing product UI fragments.

colors:
  primary: "#0a0a0a"
  primary-active: "#1f1f1f"
  primary-disabled: "#e5e5e5"
  ink: "#0a0a0a"
  body: "#3a3a3a"
  body-strong: "#1a1a1a"
  muted: "#6a6a6a"
  muted-soft: "#9a9a9a"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  hairline-strong: "#7a736a"
  canvas: "#fffaf0"
  surface-soft: "#faf5e8"
  surface-card: "#f5f0e0"
  surface-strong: "#ebe6d6"
  surface-dark: "#0a1a1a"
  surface-dark-elevated: "#1a2a2a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-soft: "#a0a0a0"
  brand-pink: "#ff4d8b"
  brand-teal: "#1a3a3a"
  brand-lavender: "#b8a4ed"
  brand-peach: "#ffb084"
  brand-ochre: "#e8b94a"
  brand-mint: "#a4d4c5"
  brand-coral: "#ff6b5a"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  focus: "#c2185b"
  focus-inset: "#fffaf0"

typography:
  display-xl:
    fontFamily: "Plain Black, Inter, sans-serif"
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: -2.5px
  display-lg:
    fontFamily: "Plain Black, Inter, sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -2px
  display-md:
    fontFamily: "Plain Black, Inter, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1px
  display-sm:
    fontFamily: "Plain Black, Inter, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  title-lg:
    fontFamily: "Inter, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.5px
  button:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  pill: 9999px
  full: 9999px

motion:
  duration-instant: 70ms
  duration-fast: 120ms
  duration-base: 200ms
  duration-slow: 320ms
  duration-emphasis: 480ms
  ease-standard: cubic-bezier(0.2, 0, 0, 1)
  ease-enter: cubic-bezier(0.34, 1.56, 0.64, 1)
  ease-exit: cubic-bezier(0.3, 0, 1, 1)
  stagger-step: 60ms
  press-scale: 0.97
  hover-lift: -2px

shadow:
  hover-lift: "0 6px 16px rgba(10, 26, 26, 0.10)"
  focus-glow: "0 0 0 4px rgba(194, 24, 91, 0.22)"

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
    height: 44px
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
    height: 44px
  button-on-color:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 44px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
  text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
  feature-card-pink:
    backgroundColor: "{colors.brand-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  feature-card-teal:
    backgroundColor: "{colors.brand-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  feature-card-lavender:
    backgroundColor: "{colors.brand-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  feature-card-peach:
    backgroundColor: "{colors.brand-peach}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  feature-card-ochre:
    backgroundColor: "{colors.brand-ochre}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  feature-card-cream:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  product-mockup-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  pricing-tier-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-card-featured:
    backgroundColor: "{colors.brand-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 44px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.error}"
    rounded: "{rounded.md}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  category-tab-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.pill}"
  badge-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  expert-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  cta-band-illustrated:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.xl}"
    padding: 80px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 80px
---

## Overview

Clay.com is the most playful B2B SaaS interface in the GTM-data category. The base atmosphere is **cream-tinted white canvas** (`{colors.canvas}` — #fffaf0) holding dark-navy ink type and **3D-rendered claymation illustrations** (mountains, mascot characters, peach/ochre/lavender landscapes) as the dominant brand voltage. Where most data-platform brands play it cool with grids and gradients, Clay leans hard into hand-crafted-looking 3D illustrations and saturated single-color feature cards.

Type voice runs **Plain Black** (or substituted with Inter weight 500-600) — a custom rounded display face used at very large sizes (72px hero) with negative letter-spacing. Body type uses Inter at standard weights. The display weight stays at 500, never bolder — the rounded character of the typeface gives it warmth without needing weight.

Component voltage comes from **saturated single-color feature cards** in a 6-color palette: hot pink, deep teal, lavender, peach, ochre, and cream-card. Each card shows product UI fragments at small scale — Claygent agent runs, sequencer flows, CRM enrichment outputs. The colored card IS the primary visual element on every long-scroll page.

**Key Characteristics:**
- Cream-tinted white canvas (`{colors.canvas}` — #fffaf0). The warmth differentiates Clay from cool-gray competitor sites.
- Dark navy/black primary CTAs (`{colors.primary}` — #0a0a0a). Buttons rounded `{rounded.md}` (12px) — friendly modern but not pill.
- 6-color saturated feature card palette: `{colors.brand-pink}`, `{colors.brand-teal}`, `{colors.brand-lavender}`, `{colors.brand-peach}`, `{colors.brand-ochre}`, `{colors.surface-card}` (cream).
- 3D claymation illustrations (mountains, characters, abstract shapes) as full-bleed hero artifacts — the brand's most-recognized visual element.
- Custom rounded Plain Black display typeface at 500 weight with -1 to -2.5px letter-spacing on display sizes.
- Border radius is generous: `{rounded.md}` (12px) for buttons + inputs, `{rounded.lg}` (16px) for content cards, `{rounded.xl}` (24px) for feature cards. The bigger radius matches the rounded display type's character.
- Product UI fragments embedded inside colored cards at small scale — agent run logs, sequencer flows, enrichment results.
- Section rhythm `{spacing.section}` (96px) between major bands.
- Footer is cream-tinted (`{colors.surface-soft}`) — Clay does NOT use a dark footer. Even the closing band stays warm-light.

## Colors

### Brand & Accent
- **Primary** (`{colors.primary}` — #0a0a0a): All primary CTAs, h1/h2 ink type. Near-black with slight warmth.
- **Brand Pink** (`{colors.brand-pink}` — #ff4d8b): Hot-pink feature card surface. Sequencer / outbound feature pages.
- **Brand Teal** (`{colors.brand-teal}` — #1a3a3a): Deep teal-green feature card. Often the featured pricing tier.
- **Brand Lavender** (`{colors.brand-lavender}` — #b8a4ed): Soft lavender feature card.
- **Brand Peach** (`{colors.brand-peach}` — #ffb084): Warm peach feature card.
- **Brand Ochre** (`{colors.brand-ochre}` — #e8b94a): Mustard / ochre feature card and illustration accents.
- **Brand Mint** (`{colors.brand-mint}` — #a4d4c5): Mint accent on illustrations and small badges.
- **Brand Coral** (`{colors.brand-coral}` — #ff6b5a): Coral accent for highlights.

### Surface
- **Canvas** (`{colors.canvas}` — #fffaf0): The default page floor. Cream-tinted white.
- **Surface Soft** (`{colors.surface-soft}` — #faf5e8): Footer and CTA-band background.
- **Surface Card** (`{colors.surface-card}` — #f5f0e0): Cream feature cards, testimonial cards.
- **Surface Strong** (`{colors.surface-strong}` — #ebe6d6): Stronger cream for emphasized bands.
- **Surface Dark** (`{colors.surface-dark}` — #0a1a1a): Dark teal-tinted near-black for occasional dark cards (rare).
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — #1a2a2a): Elevated dark cards.
- **Hairline** (`{colors.hairline}` — #e5e5e5): The extracted 1px border tone. Measured at **1.21:1 against `{colors.canvas}`**, so it is a decorative rule only — card edges, dividers, table rules. Clay's real site uses it as the boundary of text inputs too, and at 1.21:1 that boundary genuinely fails WCAG 1.4.11 (3:1 for non-text UI components).
- **Hairline Soft** (`{colors.hairline-soft}` — #f0f0f0): Even fainter rule for internal card dividers. Decoration only.
- **Hairline Strong** (`{colors.hairline-strong}` — #7a736a) — **prescribed, not extracted.** A warm grey tuned to the cream palette, added so a control boundary can actually be seen: **4.50:1 on `{colors.canvas}`**, 4.30:1 on `{colors.surface-soft}`, 4.10:1 on `{colors.surface-card}`, 3.75:1 on `{colors.surface-strong}`. Use it for the boundary of anything interactive — `{component.text-input}`, `{component.button-secondary}`, `{component.pricing-tier-card}` — and keep `{colors.hairline}` for decoration.

### Focus
Both focus tokens are **prescribed, not extracted** — Clay's live site was not measured for a focus ring, and no file in this collection defined one.

- **Focus** (`{colors.focus}` — #c2185b): The outer ring. A deepened hot pink, hue-matched to `{colors.brand-pink}`, so the indicator reads as Clay and not as a browser default. Measured: **5.65:1 on `{colors.canvas}`**, 5.40:1 on `{colors.surface-soft}`, 5.15:1 on `{colors.surface-card}`, 4.70:1 on `{colors.surface-strong}`, 3.37:1 on `{colors.primary}` (the near-black CTA), 3.30:1 on `{colors.brand-peach}`, 3.21:1 on `{colors.brand-ochre}`, 3.58:1 on `{colors.brand-mint}`.
- **Focus Inset** (`{colors.focus-inset}` — #fffaf0): The inner cream halo, drawn 2px inside the outer ring. It carries the indicator where the outer ring runs out of contrast: **11.80:1 on `{colors.brand-teal}`**, 17.17:1 on `{colors.surface-dark}`, 19.03:1 on `{colors.primary}`, 3.02:1 on `{colors.brand-pink}`.

The ring is therefore a composite: 2px `{colors.focus-inset}` then 2px `{colors.focus}`, with 5.65:1 between the two bands, so the indicator is a visible shape on every surface this file defines. Two cards are still short of 3:1 against *either* band on its own — see Accessibility.

### Text
- **Ink** (`{colors.ink}` — #0a0a0a): Headlines and primary text.
- **Body Strong** (`{colors.body-strong}` — #1a1a1a): Emphasized body, lead paragraphs.
- **Body** (`{colors.body}` — #3a3a3a): Default running-text.
- **Muted** (`{colors.muted}` — #6a6a6a): Sub-headings, breadcrumbs, footer body.
- **Muted Soft** (`{colors.muted-soft}` — #9a9a9a): Captions, fine-print. **Measured 2.70:1 on `{colors.canvas}` — this fails AA for text at any size.** It is the extracted value, so it stays, but it is a decorative tone: use it for non-essential fine print only, and move anything a reader must actually read to `{colors.muted}` (5.20:1 on canvas, 4.97:1 on `{colors.surface-soft}`).
- **On Primary / On Dark** (`{colors.on-primary}` — #ffffff): Text on primary buttons + dark feature cards (teal). Measured 19.80:1 on `{colors.primary}` and 12.28:1 on `{colors.brand-teal}` — both comfortable.

**White text on the hot-pink card fails AA, and that is the real brand.** `{colors.on-primary}` on `{colors.brand-pink}` measures **3.14:1**, below the 4.5:1 WCAG AA needs for body copy. It clears 3:1, so it is defensible only for large text — 24px/400 or 18.66px/700 and above, i.e. `{typography.title-lg}` or larger. Do not set `{typography.body-md}` or `{typography.caption}` in white on the pink card; use `{colors.ink}` there (6.30:1).

On the lighter saturated cards white is never the answer and the system already knows it: `{colors.ink}` is the documented ink on lavender (9.02:1), peach (11.12:1), ochre (10.81:1), mint (12.07:1) and coral (7.07:1). The audit harness pairs `{colors.on-primary}` against every `brand-*` token, which reports six failures; five of those pairings are combinations this file does not use.

### Semantic
- **Success** (`{colors.success}` — #22c55e): Success states.
- **Warning** (`{colors.warning}` — #f59e0b): Warning callouts.
- **Error** (`{colors.error}` — #ef4444): Validation errors.

## Typography

### Font Family
The system runs **Plain Black** (a custom rounded display face) for headlines and **Inter** for body, navigation, and UI. Plain Black at weight 500 with negative letter-spacing handles every display headline; Inter handles the rest. The fallback stack walks `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` for both.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 72px | 500 | 1.0 | -2.5px | Homepage h1 ("Go to market with unique data") — Plain Black |
| `{typography.display-lg}` | 56px | 500 | 1.05 | -2px | Section heads — Plain Black |
| `{typography.display-md}` | 40px | 500 | 1.1 | -1px | Sub-section heads, product names |
| `{typography.display-sm}` | 32px | 500 | 1.15 | -0.5px | CTA-band heads, feature card titles |
| `{typography.title-lg}` | 24px | 600 | 1.3 | -0.3px | Pricing plan names, larger feature titles |
| `{typography.title-md}` | 18px | 600 | 1.4 | 0 | Card titles, intro paragraphs |
| `{typography.title-sm}` | 16px | 600 | 1.4 | 0 | Small card titles, list labels |
| `{typography.body-md}` | 16px | 400 | 1.55 | 0 | Default running-text |
| `{typography.body-sm}` | 14px | 400 | 1.55 | 0 | Footer body, fine-print |
| `{typography.caption}` | 13px | 500 | 1.4 | 0 | Badge labels, captions |
| `{typography.caption-uppercase}` | 12px | 600 | 1.4 | 1.5px | Section labels, "FEATURED" badges |
| `{typography.button}` | 14px | 600 | 1.0 | 0 | Standard button labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Top-nav menu items |

### Principles
Plain Black at weight 500 + negative letter-spacing IS the brand voice. Going to weight 700 reads as bombastic; the rounded character of the typeface adds warmth that bolder weight would flatten.

The body-vs-display split is functional: Plain Black for Plain Black moments (headlines), Inter for everything else (running text, UI, buttons). Mixing them is a system violation.

### Note on Font Substitutes
If Plain Black is unavailable, **Inter** at weight 500 with -0.05em letter-spacing is a usable approximation. **Söhne Breit** at weight Buch is an alternative if licensed. **Recoleta** at weight 500 carries similar rounded-display warmth.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- **Section padding:** `{spacing.section}` (96px) between major editorial bands.
- **Card internal padding:** `{spacing.xl}` (32px) for feature cards and pricing tiers; `{spacing.lg}` (24px) for testimonial and product mockup cards.

### Grid & Container
- **Max content width:** ~1280px centered.
- **Editorial body:** Single 12-column grid; hero often uses 7/5 split (h1 left, illustration right).
- **Feature card grids:** 3-up at desktop, 2-up at tablet, 1-up at mobile.
- **Pricing grid:** 3-4 up at desktop, 1-up at mobile.

### Whitespace Philosophy
Clay uses generous whitespace around big rounded display headlines and saturated feature cards. The cream canvas + colored cards + 3D illustrations create a playful warmth that competing data-platform sites lack.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body sections, top nav, hero |
| Decorative rule | 1px `{colors.hairline}` border | Dividers, non-interactive card edges |
| Control boundary | 1px `{colors.hairline-strong}` border | Inputs, secondary buttons, pricing tiers — anything interactive |
| Saturated card | Brand pink/teal/lavender/peach/ochre fill — no shadow | Feature cards |
| Cream card | `{colors.surface-card}` background — no shadow | Testimonial, secondary cards |
| Hover lift | `{shadow.hover-lift}` plus `translateY({motion.hover-lift})` | Hover-elevated cards (rare) |

**Elevation is expressed by fill, not by shadow.** Depth comes from the saturated colour step between cream canvas and bright feature cards; a border is a boundary, not a level. The one shadow in the system is the hover lift, and `{shadow.hover-lift}` is **prescribed** — the prose previously said "faint shadow at low alpha" with no value to reference.

The cream layers are deliberately a near-flat stack, and they are not distinguishable by luminance alone: `{colors.canvas}` → `{colors.surface-soft}` is **1.046:1**, `{colors.surface-soft}` → `{colors.surface-card}` is **1.047:1**, `{colors.surface-card}` → `{colors.surface-strong}` is **1.095:1**, and `{colors.canvas}` → `{colors.surface-strong}` is only **1.20:1**. That is a real property of the warm palette, not a defect to fix: layers read by radius, padding and position, so any card that must be seen as a separate object carries `{rounded.lg}` or larger plus a `{colors.hairline-strong}` boundary. Do not rely on the cream step alone to separate a surface from the page.

### Decorative Depth
- **3D claymation illustrations** — mountains, characters, mascots rendered in a hand-crafted 3D style. The brand's most-recognized depth element. Not a token — these are illustrated assets.
- **Mascot characters** appear as inline figures in feature cards and CTAs.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 6px | Small badges, dropdown items |
| `{rounded.sm}` | 8px | Small buttons, hairline-border accent |
| `{rounded.md}` | 12px | Standard CTA buttons, text inputs |
| `{rounded.lg}` | 16px | Content cards, testimonial cards, pricing tiers |
| `{rounded.xl}` | 24px | Feature cards (the saturated brand-color cards) |
| `{rounded.pill}` | 9999px | Category tabs, badge pills |
| `{rounded.full}` | 9999px / 50% | Avatars, icon buttons |

The ladder is 6 → 8 → 12 → 16 → 24 → pill: a clean +2/+4/+4/+8 progression with no value sitting off-scale. `{rounded.pill}` and `{rounded.full}` are the same 9999px and differ only in intent (pill = horizontal capsule, full = circle).

### Border & Ring Widths
A deliberately short ladder; nothing else exists.

| Use | Width | Colour |
|---|---|---|
| Decorative rule, divider | 1px | `{colors.hairline}` |
| Control boundary | 1px | `{colors.hairline-strong}` |
| Focused input boundary | 2px | `{colors.ink}` |
| Focus ring, inner halo | 2px | `{colors.focus-inset}` |
| Focus ring, outer band | 2px | `{colors.focus}` |

The focus ring follows the radius of the element it surrounds plus the 2px offset, so a `{rounded.md}` button gets a 14px ring and a `{rounded.xl}` feature card gets a 26px ring. **Prescribed, not extracted.**

## Components

### Top Navigation

**`top-nav`** — Cream nav bar pinned to top. 64px tall, `{colors.canvas}` background. Carries the Clay logo + wordmark at left, primary horizontal menu (Product, Solutions, Resources, Pricing, Customers) center, right-side cluster with "Sign in" + "Try free" `{component.button-primary}`. Menu items in `{typography.nav-link}` (Inter 14px / 500).

### Buttons

**`button-primary`** — Background `{colors.primary}` (near-black), text `{colors.on-primary}` (white), type `{typography.button}` (Inter 14px / 600), padding 12px × 20px, height 44px, rounded `{rounded.md}` (12px).

**`button-secondary`** — Cream button with a visible outline. Background `{colors.canvas}`, text `{colors.ink}`, 1px `{colors.hairline-strong}` border (4.50:1 on canvas). It is an interactive boundary, so it does not use `{colors.hairline}`.

**`button-on-color`** — White button used over saturated brand-color feature cards. Same shape as primary but inverted (white background, ink text).

**`button-text-link`** — Inline text button, no background. Used for "Sign in" and inline link CTAs.

**`text-link`** — Inline body links in `{colors.ink}` with underline.

### Cards & Containers

**`hero-band`** — Cream-canvas hero with 7-5 grid: h1 + sub-headline + button row on the left, 3D claymation illustration on the right. Vertical padding `{spacing.section}` (96px).

**`hero-illustration-card`** — Right-side artifact holding 3D claymation illustration (mountains, mascot character, abstract shapes). Background `{colors.surface-soft}`, rounded `{rounded.xl}` (24px). The illustration IS the artifact.

**`feature-card-pink`** / **`feature-card-teal`** / **`feature-card-lavender`** / **`feature-card-peach`** / **`feature-card-ochre`** — Saturated single-color feature cards. Background varies per variant; rounded `{rounded.xl}` (24px); padding `{spacing.xl}` (32px). Each card carries an h3 in `{typography.title-md}`, a body description, and a product UI fragment or mascot illustration. Text color flips to `{colors.on-dark}` (white) on the teal card (12.28:1) and `{colors.ink}` (dark) on lavender/peach/ochre cards (9.02:1, 11.12:1, 10.81:1). The **pink card is the exception**: white on `{colors.brand-pink}` measures 3.14:1, so white is allowed there only at `{typography.title-lg}` (24px) and above; the card's body copy and `{typography.caption}` labels use `{colors.ink}` (6.30:1).

**`feature-card-cream`** — Lower-key feature card variant on `{colors.surface-card}`. Used for less-emphasized features that don't warrant a saturated color.

**`product-mockup-card`** — Card showing actual Clay product UI (Claygent agent runs, sequencer flows, CRM enrichment tables). Background `{colors.canvas}` with hairline border, rounded `{rounded.lg}`, padding `{spacing.lg}` (24px).

**`testimonial-card`** — Customer quote cards. Background `{colors.surface-card}` (cream), rounded `{rounded.lg}`, padding `{spacing.lg}` (24px). Top row has avatar + name + role; below sits the testimonial in `{typography.body-md}`.

**`pricing-tier-card`** — Standard tier card. Background `{colors.canvas}` with a 1px `{colors.hairline-strong}` boundary (the card is selectable, so the edge must be visible), rounded `{rounded.lg}`, padding `{spacing.xl}` (32px).

**`pricing-tier-card-featured`** — The featured tier flips to `{colors.brand-teal}` (deep teal-green). The teal surface IS the featured signal.

**`expert-card`** — Used on /experts page. Background `{colors.canvas}` with hairline, rounded `{rounded.lg}`, padding `{spacing.lg}`. Carries an avatar at top, expert name, specialization, and a "Book session" link.

### Inputs & Forms

**`text-input`** — Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, rounded `{rounded.md}` (12px), padding 12px × 16px, height 44px. 1px `{colors.hairline-strong}` border (4.50:1 on canvas) — the extracted `{colors.hairline}` at 1.21:1 is not a usable control boundary.

**`text-input-focused`** — Border thickens to `{colors.ink}` for emphasis and the composite focus ring is drawn outside it: 2px `{colors.focus-inset}` then 2px `{colors.focus}`, offset 2px.

**`text-input-error`** — Boundary flips to `{colors.error}` (#ef4444, 3.62:1 on `{colors.canvas}`, clearing the 3:1 UI-component threshold). The message line below sits in `{colors.error}` at `{typography.body-sm}` — and at 3.62:1 that is **below the 4.5:1 AA needs for 14px text**, so the message is never colour-alone: it carries an icon, and the error wording is read out via `aria-invalid` plus a described-by association. For the message ink itself use `{colors.body}` (10.93:1) and keep `{colors.error}` for the icon and boundary.

### Tabs / Badges

**`category-tab`** + **`category-tab-active`** — Pill-shaped tabs in sub-nav. Inactive: transparent + muted text. Active: cream-card background + ink text. Padding 8px × 16px.

**`badge-pill`** — Small cream-fill pill labels in `{typography.caption}` (13px / 500), rounded `{rounded.pill}`.

### CTA / Footer

**`cta-band-illustrated`** — Pre-footer "Turn your growth ideas into reality today" band. Background `{colors.surface-soft}`, rounded `{rounded.xl}`, padding 80px. Carries an h2 in `{typography.display-md}`, a sub-line, and a `{component.button-primary}` — usually paired with a 3D illustration of a mascot or scene.

**`footer`** — Cream-tinted footer (NOT dark navy unlike most SaaS sites). Background `{colors.surface-soft}`, text `{colors.body}`. 4-column link list. Vertical padding 80px. Often features a horizon-style 3D mountain illustration at the very bottom — Clay's signature footer mountain.

### Component States

Only `default`, `active` and `disabled` were extracted from the live site (as the `-active` and `-disabled` frontmatter variants). Everything else in this table is **prescribed** — a consistent state model for the components the file already documents. A component with genuinely two states says so in its row.

| Component | States | Treatment |
|---|---|---|
| `button-primary` | default · hover · focus-visible · pressed · disabled · loading | hover: `{colors.primary-active}` fill plus `translateY({motion.hover-lift})`; focus-visible: composite ring, `{colors.focus-inset}` then `{colors.focus}`; pressed: `scale({motion.press-scale})`; disabled: `{colors.primary-disabled}` fill with `{colors.muted}` label (4.29:1) and no pointer events; loading: label swaps for a spinner, box size held so the button does not resize |
| `button-secondary` | default · hover · focus-visible · pressed · disabled · loading | hover: fill steps to `{colors.surface-card}`, boundary stays `{colors.hairline-strong}`; focus-visible: composite ring; pressed: `scale({motion.press-scale})`; disabled: `{colors.muted-soft}` label with a `{colors.hairline}` boundary; loading: inline spinner |
| `button-on-color` | default · hover · focus-visible · pressed · disabled | On saturated cards the ring's inner `{colors.focus-inset}` band is the load-bearing edge. hover: `{colors.surface-card}` fill; pressed: `scale({motion.press-scale})` |
| `button-text-link` / `text-link` | default · hover · focus-visible · pressed | Three-state plus default by design: hover thickens the underline, focus-visible draws the composite ring, pressed drops opacity to 0.7. No disabled state — a dead link is removed, not greyed |
| `top-nav` link | default · hover · focus-visible · selected | selected marks the current section with a 2px `{colors.focus}` underline (5.65:1 on `{colors.canvas}`), never colour alone |
| `category-tab` | default · hover · focus-visible · selected · disabled | selected is `{component.category-tab-active}` — `{colors.surface-card}` fill plus `{colors.ink}` label, so the change is fill and weight, not just colour; disabled drops the label to `{colors.muted-soft}` |
| `text-input` | default · hover · focus-visible · disabled · error · loading | hover warms the boundary only; focus-visible is `{component.text-input-focused}`; error is `{component.text-input-error}`; loading shows an async-validation spinner at the trailing edge; disabled fills `{colors.surface-strong}` |
| `feature-card-*` (pink, teal, lavender, peach, ochre, cream) | default · hover · focus-visible — only when the whole card is a link | Static cards have exactly one state and say so. As a link: hover lifts by `{motion.hover-lift}`, focus-visible draws the composite ring outside the `{rounded.xl}` edge |
| `pricing-tier-card` | default · hover · focus-visible · selected | selected is `{component.pricing-tier-card-featured}` — `{colors.brand-teal}` fill plus a `{typography.caption-uppercase}` "FEATURED" badge, so selection is not conveyed by colour alone |
| `product-mockup-card` / `testimonial-card` / `hero-illustration-card` | default only | Genuinely single-state: presentational containers with no interactive affordance |
| `expert-card` | default · hover · focus-visible · loading | loading is the skeleton shown while the /experts list fetches: `{colors.surface-strong}` blocks, opacity pulse only |
| `badge-pill` | default only | Genuinely single-state: a label, never a control |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted from Clay.com; every value is an inference from the identity the rest of this file documents, and should be treated as a starting proposal, not an observed fact.

**Profile: Playful.** Clay qualifies on rule 3 of the profile ladder — saturated multi-colour identity where the colour sits on interactive elements, not just behind screenshots: `{component.feature-card-pink}` through `{component.feature-card-ochre}` are clickable surfaces, `{component.pricing-tier-card-featured}` signals selection with a `{colors.brand-teal}` fill, and `{component.category-tab-active}` changes fill on selection. The type voice is informal (rounded Plain Black display at weight 500, never bolder) and the brand's defining asset is 3D claymation illustration. Clay is not Calm: nothing in the file reads "sober" or "editorial", and gradients are not forbidden. Base duration is 200ms, entrances overshoot, and the signature gesture is the small press-squash — clay deforms under a thumb and springs back, which is the one motion idea the whole identity hands you for free.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, link, card) | `{motion.duration-fast}` (120ms) | `{motion.ease-standard}` | `transform: translateY({motion.hover-lift})`, `opacity` | Travel removed; the fill and underline changes remain and apply instantly |
| Press | `{motion.duration-instant}` (70ms) down, `{motion.duration-fast}` (120ms) release | `{motion.ease-standard}` down, `{motion.ease-enter}` release | `transform: scale({motion.press-scale})` | Scale removed entirely; the pressed fill still applies, with no transition |
| Focus (focus-visible ring) | `{motion.duration-instant}` (70ms) | `{motion.ease-standard}` | `opacity` only — the ring never scales or travels in | Ring appears instantly at full opacity. Never suppressed |
| Page / route transition | `{motion.duration-base}` (200ms) out, `{motion.duration-slow}` (320ms) in | `{motion.ease-exit}` out, `{motion.ease-enter}` in | `opacity`, `transform: translateY(8px)` | Opacity crossfade at `{motion.duration-fast}` (120ms); no translate |
| Modal / drawer | `{motion.duration-slow}` (320ms) in, `{motion.duration-base}` (200ms) out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: scale(0.96 → 1)` for a modal, `translateX(100% → 0)` for a drawer | Opacity fade at 120ms, no scale, no slide. Backdrop fades, never blurs in |
| Dropdown / nav menu | `{motion.duration-fast}` (120ms) in, `{motion.duration-instant}` (70ms) out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: scale(0.98 → 1)` from the trigger edge | Opacity only at 120ms, no scale |
| Toast | `{motion.duration-base}` (200ms) in, `{motion.duration-fast}` (120ms) out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: translateY(12px → 0)` | Opacity at 120ms; no travel. Auto-dismiss timing is unchanged |
| List enter (feature-card grid, expert grid, pricing tiers) | `{motion.duration-base}` (200ms) per item, `{motion.stagger-step}` (60ms) apart, capped at 6 items | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px) scale(0.98)` | Stagger and travel removed; the whole group fades at 120ms as one, or appears outright if already in view |
| List exit | `{motion.duration-fast}` (120ms), no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Opacity at 120ms, no scale |
| Loading (spinner, skeleton) | 900ms spinner rotation, 1600ms skeleton pulse — both infinite by necessity | linear rotation, `{motion.ease-standard}` pulse | `transform: rotate()` for the spinner, `opacity` for the skeleton | Spinner rotation stops and becomes a static indicator with text; skeleton pulse freezes at mid-opacity. Both still announce busy state |

Rules this system holds to:

- **`transform` and `opacity` only.** Never `width`, `height`, `top`, `left` or `margin` — a lifting feature card translates, it does not grow its box.
- **Exits are shorter than their entrances** in every row above.
- **Nothing animates on first paint in a way that delays content.** The hero `{typography.display-xl}` headline and its copy are painted, not revealed; list-enter choreography applies only to items entering an already-painted viewport.
- **No infinite animation except loaders and one piece of brand ambience.** The 3D claymation illustrations may carry a slow, declared ambient drift — this is deliberate brand ambience, stated as such, and it freezes under reduced motion.
- **The press-squash is the brand's signature.** `scale({motion.press-scale})` on every control, released with the overshoot of `{motion.ease-enter}`. It is small on purpose; Clay is friendly, not bouncy-cartoon.

### `@media (prefers-reduced-motion: reduce)`

**Removed:** all travel (`translateX`, `translateY`), all scale (including the press-squash and the modal scale-in), all stagger (`{motion.stagger-step}` becomes 0), the spinner's rotation, and the claymation ambient drift, which freezes on its first frame.

**Kept:** every opacity fade, clamped to 120ms or less — at or under the 150ms ceiling the spec sets. Focus rings still appear, instantly and at full opacity. All colour and fill changes still happen, applied with no transition. Skeletons still show as static `{colors.surface-strong}` blocks. Auto-dismiss timings, busy announcements and every non-motion affordance are untouched. Reduced motion removes decoration; it never removes information.

## Accessibility

Every ratio below was computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. Contrast and token values are measurable from the document; **tap-target size, overlap, clipping and frame rate are not** — those need a rendered page, and nothing here claims them as measured.

### Text contrast

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 19.03:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-soft}` | 18.19:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-card}` | 17.37:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas}` | 10.93:1 | 4.5:1 | Pass |
| `{colors.muted}` on `{colors.canvas}` | 5.20:1 | 4.5:1 | Pass |
| `{colors.muted}` on `{colors.surface-card}` | 4.75:1 | 4.5:1 | Pass |
| `{colors.muted}` on `{colors.surface-strong}` | 4.33:1 | 4.5:1 | **Fail** — use `{colors.body}` on the strong cream band |
| `{colors.muted-soft}` on `{colors.canvas}` | 2.70:1 | 4.5:1 | **Fail** — decorative fine print only |
| `{colors.on-primary}` on `{colors.primary}` | 19.80:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.brand-teal}` | 12.28:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.surface-dark}` | 17.86:1 | 4.5:1 | Pass |
| `{colors.on-dark-soft}` on `{colors.surface-dark}` | 6.83:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.brand-pink}` | 3.14:1 | 4.5:1 | **Fail** — large text only (`{typography.title-lg}` and above) |
| `{colors.ink}` on `{colors.brand-pink}` | 6.30:1 | 4.5:1 | Pass — the correct ink for body copy on the pink card |
| `{colors.ink}` on `{colors.brand-lavender}` | 9.02:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.brand-peach}` | 11.12:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.brand-ochre}` | 10.81:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.brand-mint}` | 12.07:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.brand-coral}` | 7.07:1 | 4.5:1 | Pass |
| `{colors.error}` on `{colors.canvas}` | 3.62:1 | 4.5:1 | **Fail** as text — boundary and icon only |
| `{colors.success}` on `{colors.canvas}` | 2.19:1 | 4.5:1 | **Fail** as text — fill and icon only |
| `{colors.warning}` on `{colors.canvas}` | 2.06:1 | 4.5:1 | **Fail** as text — fill and icon only |

**Where the real brand fails AA, plainly:**

- **`{component.feature-card-pink}` fails.** Its declared pairing is `{colors.on-primary}` (#ffffff) on `{colors.brand-pink}` (#ff4d8b) at **3.14:1**, below the 4.5:1 AA needs for body text. It clears 3:1, so white is defensible on that card only at `{typography.title-lg}` (24px) and above; the card's body copy and `{typography.caption}` labels use `{colors.ink}` at 6.30:1. The hex is the real brand and is not altered here.
- **`{colors.muted-soft}` (2.70:1) and `{colors.on-dark-soft}` on cream (2.51:1) fail at every size.** Both are frozen extracted tones. `{colors.on-dark-soft}` is only ever drawn on `{colors.surface-dark}` (6.83:1) and `{colors.surface-dark-elevated}` (5.70:1), where it passes; on cream it is never used.
- **`{colors.success}`, `{colors.warning}` and `{colors.error}` fail as ink on cream** (2.19:1, 2.06:1, 3.62:1). They are fills, icons and boundaries, not text colours.
- **`{colors.hairline}` (1.21:1) and `{colors.hairline-soft}` (1.10:1) fail the 3:1 WCAG 1.4.11 threshold** for a non-text UI boundary, which is why text inputs built from the extracted palette alone have an invisible edge. `{colors.hairline-strong}` exists for that job.

These are properties of the brand as it exists, not defects introduced here, and no extracted hex was changed to make a ratio pass.

### Non-text contrast

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.hairline}` on `{colors.canvas}` | 1.21:1 | 3.0:1 | **Fail** — frozen extracted tone, scoped to decoration |
| `{colors.hairline-soft}` on `{colors.canvas}` | 1.10:1 | 3.0:1 | **Fail** — frozen extracted tone, internal card dividers only. Never a control boundary |
| `{colors.hairline-strong}` on `{colors.canvas}` | 4.50:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.surface-soft}` | 4.30:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.surface-card}` | 4.10:1 | 3.0:1 | Pass |
| `{colors.hairline-strong}` on `{colors.surface-strong}` | 3.75:1 | 3.0:1 | Pass |
| `{colors.error}` on `{colors.canvas}` (input boundary) | 3.62:1 | 3.0:1 | Pass |

### Focus ring visibility, surface by surface

The ring is a composite: 2px `{colors.focus-inset}` inside, 2px `{colors.focus}` outside, 5.65:1 between the two bands. Both tokens are **prescribed**. Every surface this file defines:

| Surface | Outer `{colors.focus}` | Inner `{colors.focus-inset}` | Verdict |
|---|---|---|---|
| `{colors.canvas}` | 5.65:1 | 1.00:1 | Pass on the outer band |
| `{colors.surface-soft}` | 5.40:1 | 1.05:1 | Pass on the outer band |
| `{colors.surface-card}` | 5.15:1 | 1.10:1 | Pass on the outer band |
| `{colors.surface-strong}` | 4.70:1 | 1.20:1 | Pass on the outer band |
| `{colors.primary}` (near-black CTA) | 3.37:1 | 19.03:1 | Pass on both |
| `{colors.surface-dark}` | 3.04:1 | 17.17:1 | Pass on both |
| `{colors.surface-dark-elevated}` | — | 14.33:1 | Pass on the inner band |
| `{colors.brand-teal}` | 2.09:1 | 11.80:1 | Pass on the inner band |
| `{colors.brand-peach}` | 3.30:1 | 1.71:1 | Pass on the outer band |
| `{colors.brand-ochre}` | 3.21:1 | 1.76:1 | Pass on the outer band |
| `{colors.brand-mint}` | 3.58:1 | 1.58:1 | Pass on the outer band |
| `{colors.brand-pink}` | 1.87:1 | 3.02:1 | Pass on the inner band |
| `{colors.brand-lavender}` | 2.68:1 | 2.11:1 | **Neither band reaches 3:1** |
| `{colors.brand-coral}` | 2.10:1 | 2.69:1 | **Neither band reaches 3:1** |

On `{colors.brand-lavender}` and `{colors.brand-coral}` the composite ring is still perceivable as a shape, because the two bands contrast 5.65:1 with each other — the construction WCAG 2.2 Focus Appearance allows. But neither band alone clears 3:1 against those two card fills, so **a focusable control placed directly on a lavender or coral fill is not compliant**. The system's answer is that `{component.button-on-color}` is a cream button: the ring is then drawn against `{colors.canvas}` (5.65:1), not against the card. Do not place a bare focusable element on the lavender or coral fill. Nearest passing fills are recorded in the audit report, not applied here, because they would falsify the brand hexes.

### Minimum tap target

`{component.button-primary}`, `{component.button-secondary}`, `{component.button-on-color}` and `{component.text-input}` are all declared at 44px height, which satisfies WCAG 2.5.5 Target Size (Enhanced). `{component.category-tab}` at 8px × 16px padding on `{typography.nav-link}` (14px / 1.4) computes to roughly 36px tall and **does not reach 44px** — pad it to 44px or extend the hit area beyond the painted pill. `{component.badge-pill}` is a label, not a target. **None of this is rendered-and-measured** — it is arithmetic on the declared padding and type metrics, and real tap-target size can only be confirmed on a running page.

### Reduced motion

Every motion row above declares its reduced-motion behaviour, and the `@media (prefers-reduced-motion: reduce)` rule is stated in full under Motion & Animation. Under reduce: all travel, scale and stagger are removed, the spinner stops rotating, the claymation ambience freezes, opacity fades are clamped to 120ms, and focus rings still appear instantly. No information is conveyed by motion alone anywhere in this system.

### Not conveyed by colour alone

`{component.pricing-tier-card-featured}` pairs its `{colors.brand-teal}` fill with a `{typography.caption-uppercase}` "FEATURED" badge. `{component.category-tab-active}` pairs its fill change with the `{colors.ink}` label step. `{component.text-input-error}` pairs its `{colors.error}` boundary with an icon and an accessible description. The six brand-colour feature cards are editorial variety, not meaning — the card colour never encodes a value a reader has to decode.

## Do's and Don'ts

### Do
- Anchor every page on the cream canvas (`{colors.canvas}` — #fffaf0). The warm tint differentiates Clay from cool-gray data sites.
- Use 3D claymation illustrations as hero artifacts. Hand-crafted 3D characters and mountains ARE the brand.
- Cycle saturated feature cards across the page — pink → teal → lavender → peach → ochre → cream. Repeating the same color twice in a row reads as off-rhythm.
- Use Plain Black at weight 500 with negative letter-spacing on every display headline.
- Show product UI fragments inside saturated feature cards. The brand voltage is product-driven, not abstract.
- Use cream footer (NOT dark). Clay deliberately closes pages with warm cream rather than the standard dark-footer SaaS template.
- Anchor every band with `{spacing.section}` (96px) vertical rhythm.

### Don't
- Don't use cool grays for canvas. The cream tint is non-negotiable.
- Don't use a 7th brand-color card. The 6-color palette is saturated enough.
- Don't bold display weight beyond 500. Plain Black at 700 reads as bombastic.
- Don't repeat the same brand-color card twice in a row.
- Don't replace claymation illustrations with flat vector art. The hand-crafted 3D character IS the brand voice.
- Don't use a dark footer. The cream footer is part of the system's warm-throughout pacing.
- Don't add hover state styling beyond what the Component States table encodes — a `translateY({motion.hover-lift})` lift and a fill step, nothing more.
- Don't suppress the focus ring. `{colors.focus}` plus `{colors.focus-inset}` is the only focus indicator in the system, and it survives `prefers-reduced-motion`.
- Don't set white body copy on `{colors.brand-pink}` — 3.14:1. Use `{colors.ink}` (6.30:1), and keep white for `{typography.title-lg}` and above.
- Don't use `{colors.hairline}` as the boundary of anything interactive. At 1.21:1 on the canvas it is invisible; `{colors.hairline-strong}` exists for that job.
- Don't animate `width`, `height`, `top`, `left` or `margin`. Lift and squash with `transform`; fade with `opacity`.
- Don't put a bare focusable control directly on the lavender or coral card fill — neither focus band reaches 3:1 there. Use `{component.button-on-color}`.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav; hero h1 72→36px; hero-illustration-card stacks below; feature grids 1-up; pricing 1-up |
| Tablet | 768–1024px | Top nav tightens; feature cards 2-up; pricing 2-up |
| Desktop | 1024–1440px | Full top-nav; 3-up feature cards; 3-up pricing tiers |
| Wide | > 1440px | Same as desktop with more breathing room; max content 1280px |

### Touch Targets
- `{component.button-primary}` at minimum 44 × 44px (matches WCAG AAA).
- `{component.text-input}` height is 44px.

### Collapsing Strategy
- Top nav collapses to hamburger at < 768px.
- Hero 7-5 grid → single-column on mobile.
- Feature card grids reduce columns rather than scaling.
- Saturated feature cards retain their colored fill at every breakpoint.
- Pricing tier cards collapse 4 → 2 → 1.

## Iteration Guide

1. Focus on ONE component at a time. Reference its YAML key (`{component.feature-card-pink}`, `{component.pricing-tier-card-featured}`).
2. Pick the right brand-color card for the feature: pink for outbound/sequencer, teal for enterprise/featured, lavender for AI-agent products, peach for general SaaS warmth, ochre for community / experts.
3. Variants of an existing component (`-active`, `-disabled`) live as separate entries.
4. Use `{token.refs}` everywhere — never inline hex.
5. Document states in the Component States table, not inline per component — one place, one model. New components join that table or state plainly that they are single-state.
6. Display headlines stay Plain Black 500 with negative letter-spacing. Body stays Inter 400.
7. The cream-throughout palette is a system contract — don't add a dark footer.

## Known Gaps

- Plain Black is licensed to Clay and not available as a public web font; Inter weight 500 with negative letter-spacing is the closest substitute.
- 3D claymation illustrations are commissioned assets, not system tokens — they're rendered per-page.
- The mascot characters (named characters that recur across the site) are illustrated assets; their exact lineage and naming are not formalized in tokens.
- **The entire Motion & Animation section is prescribed, not extracted.** No duration, easing curve or stagger was measured from Clay.com; the Playful profile's values were fitted to the identity the rest of this file documents. Real scroll parallax on the 3D illustrations and real feature-card entrance timing remain unmeasured.
- **The focus ring is prescribed.** `{colors.focus}` and `{colors.focus-inset}` were not extracted — Clay's live focus treatment was never captured, and nothing in this collection defined one. The hue is derived from `{colors.brand-pink}`; the luminance was chosen to clear 3:1 on the cream surfaces and on `{colors.primary}`.
- **`{colors.hairline-strong}` is prescribed.** It is a parallel accessible token added alongside the extracted `{colors.hairline}`, which stays frozen at 1.21:1.
- `{shadow.hover-lift}` and `{shadow.focus-glow}` are prescribed. The prose documented "a faint shadow at low alpha" with no value, so there was nothing to extract.
- `{component.text-input-error}` is prescribed. Form validation beyond `{component.text-input-focused}` was not extracted, and the error treatment here is an inference from `{colors.error}`.
- Tap-target sizes in the Accessibility section are arithmetic on declared padding and type metrics, not rendered measurements. Overlap, clipping, horizontal overflow and frame rate cannot be assessed from a document.
- The actual Clay product surface (in-app data tables, formula editor, agent builder) shares some tokens with the marketing site but adds many product-specific components that are out of scope.
