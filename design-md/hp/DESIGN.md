---
version: alpha
name: HP-design-analysis
description: An inspired interpretation of HP's design language — a white-paper enterprise-consumer system anchored by HP Electric Blue (`#024ad8`) as the lone signal CTA, near-black ink (`#1a1a1a`) for headlines, geometric Forma-DJR sans throughout, and angular blue-chevron decorations that nod to the HP wordmark's slashes. Cards round at 8–16px, photos sit in soft 16px frames, and dark navy slabs anchor the customer-story and "how can we help" closing bands.

colors:
  primary: "#024ad8"
  primary-bright: "#296ef9"
  primary-deep: "#0e3191"
  primary-soft: "#c9e0fc"
  on-primary: "#ffffff"
  ink: "#1a1a1a"
  ink-deep: "#000000"
  ink-soft: "#292929"
  on-ink: "#ffffff"
  canvas: "#ffffff"
  paper: "#ffffff"
  surface: "#ffffff"
  cloud: "#f7f7f7"
  fog: "#e8e8e8"
  steel: "#c2c2c2"
  graphite: "#636363"
  charcoal: "#3d3d3d"
  text-dim: "#3d3d3d"
  hairline: "#e8e8e8"
  hairline-strong: "#c2c2c2"
  hairline-control: "#767676"
  focus: "#0e3191"
  focus-inset: "#ffffff"
  focus-on-dark: "#c9e0fc"
  link: "#024ad8"
  link-pressed: "#0e3191"
  bloom-coral: "#ff5050"
  bloom-rose: "#f9d4d2"
  bloom-deep: "#b3262b"
  bloom-wine: "#5a1313"
  storm-mist: "#8ebdce"
  storm-sea: "#7fadbe"
  storm-deep: "#356373"
  error: "#b3262b"

typography:
  display-xxl:
    fontFamily: Forma DJR Micro
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  display-xl:
    fontFamily: Forma DJR Micro
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  display-lg:
    fontFamily: Forma DJR Micro
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  display-md:
    fontFamily: Forma DJR Micro
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  display-sm:
    fontFamily: Forma DJR Micro
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.17
    letterSpacing: 0
  display-xs:
    fontFamily: Forma DJR Micro
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  body-lg:
    fontFamily: Forma DJR Micro
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: Forma DJR Micro
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  body-emphasis:
    fontFamily: Forma DJR Micro
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-md:
    fontFamily: Forma DJR Micro
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: Forma DJR Micro
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: Forma DJR Micro
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  link-md:
    fontFamily: Forma DJR Micro
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: Forma DJR Micro
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.7px
    textTransform: uppercase
  button-sm:
    fontFamily: Forma DJR Micro
    fontSize: 12.6px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.126px
  price-md:
    fontFamily: Forma DJR Micro
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.17
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 3px
  md: 4px
  lg: 8px
  xl: 16px
  pill: 9999px
  full: 9999px

shadow:
  soft-lift: "0 2px 8px rgba(26, 26, 26, 0.08)"
  floating: "0 8px 24px rgba(26, 26, 26, 0.12)"

motion:
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 500ms
  ease-standard: cubic-bezier(0.4, 0, 0.2, 1)
  ease-enter: cubic-bezier(0.2, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 40ms
  duration-reduced: 150ms

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  xxl: 32px
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.on-primary}"
  button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-outline-ink:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-text-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.link-md}"
    padding: 4px 0
  badge-pill-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 6px 12px
  badge-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 6px 12px
  badge-sale-coral:
    backgroundColor: "{colors.bloom-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
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
  text-input-search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 40px
  card-product:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-product-feature:
    backgroundColor: "{colors.cloud}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px
  card-pricing-tier:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-pricing-tier-featured:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-customer-story:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 16px
  card-article-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 16px
  card-category-icon:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-emphasis}"
    rounded: "{rounded.lg}"
    padding: 16px
  promo-strip-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 48px
  hero-promo-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px
  utility-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-md}"
    height: 36px
    padding: 0 24px
  nav-bar-top:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    height: 64px
    padding: 0 32px
  nav-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 8px 16px
  category-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-emphasis}"
    rounded: "{rounded.pill}"
    padding: 8px 20px
  category-tab-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  faq-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-emphasis}"
    rounded: "{rounded.lg}"
    padding: 20px 24px
  chevron-decoration:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  help-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    padding: 64px 32px
  footer-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    padding: 64px 32px
---

## Overview

HP reads like a long-running consumer-electronics catalog crossed with an enterprise-software product page. The whole system sits on **pure white** (`{colors.canvas}` — `#ffffff`) with thin gray panels (`{colors.cloud}` / `{colors.fog}`) for alternating section bands. There is one chromatic action color — **HP Electric Blue** (`{colors.primary}` — `#024ad8`) — and one ink color (`{colors.ink}` — `#1a1a1a`); together they do ninety percent of the work. Type is a single family across every surface: **Forma DJR Micro**, HP's bespoke geometric grotesque, set at weight 500 for headlines and 400 for body — clean, neutral, slightly mechanical.

The signature gesture is **angular blue chevrons** — sharp 0-radius slashes derived from the HP wordmark's pair of parallel slashes — that anchor the homepage hero, the laptop-page hero, and the printer pricing page. They appear on the left and right edges of the primary banner card, layered behind product photography. Outside those decorative slashes, every other surface is rectilinear with **soft 8–16px corners** on cards and a 4px corner on buttons.

The system breaks into three voice modes: a **white commercial body** for product browsing (cards, category icons, pricing tiers); a **dark navy slab** (`{colors.ink}` near-black) for testimonial bands, the closing "How can we help?" footer-prelude, and the page footer; and a **light fog band** (`{colors.cloud}` / `{colors.fog}`) for utility sections like comparison strips and FAQ accordions. The blue accent appears only on filled CTAs, link text, the chevron decorations, and the active price-stamp on a featured tier — never as a section background.

**Key Characteristics:**
- Pure white canvas (`{colors.canvas}`) with deep ink (`{colors.ink}`) running every body surface; light fog bands (`{colors.cloud}`, `{colors.fog}`) alternate for section rhythm
- HP Electric Blue (`{colors.primary}`) is the lone CTA fill and link color; it appears at most twice per viewport
- Bespoke Forma DJR Micro across every surface — display, body, button, caption — at weights 400 / 500 / 600 / 700
- Cards round at `{rounded.xl}` (16px) for product/pricing tiles; buttons sit at `{rounded.md}` (4px) with capitalize labels
- Geometric blue chevrons (`{colors.primary}` rectangles cut at 45°) frame hero photography and reinforce the wordmark
- Dark-navy slabs (`{colors.ink}`) close every page rhythm — testimonial bands, "how can we help?" prelude, and the footer
- Section rhythm: utility-strip → top nav → white body → cloud-band → ink slab → cloud-band → ink footer

## Colors

> **No Interaction sub-section.** Hover colors are silently filtered. Allowed sub-sections: Brand & Accent, Surface, Text, Semantic.

### Brand & Accent
- **HP Electric Blue** (`{colors.primary}` — `#024ad8`): the system's lone signal — primary CTA fill, link color, chevron-decoration fill, active sub-nav indicator. Reserved.
- **Bright Blue** (`{colors.primary-bright}` — `#296ef9`): a slightly lighter variant used inside dark slabs (testimonial-card buttons, dark-band CTA links) where the deeper blue would muddy.
- **Deep Navy** (`{colors.primary-deep}` — `#0e3191`): pressed state for the primary CTA and the visited-link color.
- **Soft Blue** (`{colors.primary-soft}` — `#c9e0fc`): pale-blue surface used inside customer-story cards and selection chips.
- **Focus Ring** (`{colors.focus}` — `#0e3191`, prescribed — no ring was extracted from the live site): a 2px ring drawn on every focusable element on a light surface. It reuses the deep navy of the pressed CTA rather than Electric Blue so the ring never disappears into a blue CTA fill. Measures 11.25:1 on `{colors.canvas}`.
- **Focus Inset** (`{colors.focus-inset}` — `#ffffff`, prescribed): the mandatory 2px white offset drawn *between* the element and `{colors.focus}`. It is what makes the ring legible on a `{colors.primary}` fill, where the ring alone sits at 1.59:1. Band-to-band separation is 11.25:1.
- **Focus on Dark** (`{colors.focus-on-dark}` — `#c9e0fc`, prescribed): the ring used inside the `{colors.ink}` slabs — testimonial bands, the "How can we help?" prelude, the footer. Measures 12.89:1 on `{colors.ink}`.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): the universal page background. White, full opacity.
- **Paper** (`{colors.paper}` — `#ffffff`): card surfaces — same white as canvas, with hairline borders or shadows providing the lift.
- **Surface** (`{colors.surface}` — `#ffffff`): the role alias for `{colors.paper}`, named so the card/panel surface is addressable by role. It is deliberately the same hex as `{colors.canvas}`: a white card on a white page measures 1.00:1, so the separation is carried entirely by `{shadow.soft-lift}` and the hairline, never by tone.
- **Cloud** (`{colors.cloud}` — `#f7f7f7`): the lightest gray section band, used for alternating-row backgrounds and product-feature card groups.
- **Fog** (`{colors.fog}` — `#e8e8e8`): a slightly darker gray surface band, used for FAQ outer panels and the "Trending laptops" header strip.
- **Steel** (`{colors.steel}` — `#c2c2c2`): hairline border used on outlined elements with stronger emphasis (active filter, input default border). Same value as `{colors.hairline-strong}`.
- **Control Boundary** (`{colors.hairline-control}` — `#767676`, prescribed — not extracted): the boundary tone for anything a user types into or operates, where the frozen `{colors.hairline}` (1.23:1) and `{colors.hairline-strong}` (1.78:1) are both below the 3:1 non-text minimum. Measures 4.54:1 on `{colors.canvas}`, 4.24:1 on `{colors.cloud}`, 3.71:1 on `{colors.fog}`. `{colors.hairline}` and `{colors.hairline-strong}` stay scoped to decoration — table rules, section dividers, card edges — where no boundary carries meaning.
- **Bloom Coral / Bloom Rose** (`{colors.bloom-coral}` / `{colors.bloom-rose}` — `#ff5050`, `#f9d4d2`): the "Get 25% off" sale-tag chip + soft pink lifestyle accent on the sale hero.
- **Storm Mist / Sea / Deep** (`{colors.storm-mist}`, `{colors.storm-sea}`, `{colors.storm-deep}` — `#8ebdce`, `#7fadbe`, `#356373`): the teal-storm tones reserved for the printer-plan illustration backdrop and supporting infographic accents.

### Text
- **Ink** (`{colors.ink}` — `#1a1a1a`): the universal text color on white surfaces — headlines, body, button labels, navigation.
- **Ink Deep** (`{colors.ink-deep}` — `#000000`): pure black used for the wordmark and 1px hairline strokes around badge outlines.
- **Ink Soft** (`{colors.ink-soft}` — `#292929`): an alternate near-black used inside dark-navy slabs as a subtle textural shift.
- **On Ink** (`{colors.on-ink}` — `#ffffff`): pure white used for headline and body text on every dark-navy slab.
- **Charcoal** (`{colors.charcoal}` — `#3d3d3d`): muted body color on white surfaces — secondary descriptions, fine-print disclaimers.
- **Text Dim** (`{colors.text-dim}` — `#3d3d3d`): the role alias for `{colors.charcoal}`, so secondary ink is addressable by role. 10.86:1 on `{colors.canvas}`.
- **Graphite** (`{colors.graphite}` — `#636363`): smaller-print color, used for legal lines and timestamp metadata.

### Semantic
- **Bloom Deep** (`{colors.bloom-deep}` — `#b3262b`) + **Bloom Wine** (`{colors.bloom-wine}` — `#5a1313`): error and discount-emphasis colors. The deep brick reads as "sale" or "destructive" depending on placement.
- **Storm Deep** (`{colors.storm-deep}` — `#356373`): used as a neutral status accent (e.g., printer-plan tier "Versatile" tier color).

## Typography

### Font Family

The voice is **single-family**: Forma DJR Micro (HP's bespoke geometric grotesque, fallback Arial) across every surface — display, body, button, caption. Forma DJR Micro is a wide, slightly rounded grotesque designed at small optical sizes to stay legible at UI-chrome scale. HP runs it at weight 400 for body, 500 for display headlines, 600/700 for emphasis and button labels.

The 16/14/12-px caption tier carries the catalog metadata — model numbers, spec rows, fine print — at weight 400 with a 1.4–1.5 line-height. Button labels lift to weight 600/700 with positive 0.5–1.1px letter-spacing and uppercase transform — the only place the system tracks letters.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 72px | 500 | 1.0 | 0 | Hero headline (homepage, laptop hub) |
| `{typography.display-xl}` | 56px | 500 | 1.0 | 0 | Section headlines on landing pages |
| `{typography.display-lg}` | 44px | 500 | 1.0 | 0 | Sub-section headlines on shop pages |
| `{typography.display-md}` | 32px | 500 | 1.0 | 0 | Promo strip headlines, FAQ section headers |
| `{typography.display-sm}` | 24px | 500 | 1.17 | 0 | Card titles, pricing-tier names |
| `{typography.display-xs}` | 20px | 500 | 1.0 | 0 | Inline list headers, accordion labels |
| `{typography.body-lg}` | 18px | 400 | 1.33 | 0 | Lead paragraphs |
| `{typography.body-md}` | 16px | 400 | 1.38 | 0 | Default body |
| `{typography.body-emphasis}` | 16px | 500 | 1.38 | 0 | Bolded run-in copy |
| `{typography.caption-md}` | 14px | 400 | 1.5 | 0 | Specs, metadata, captions |
| `{typography.caption-bold}` | 14px | 700 | 1.3 | 0 | Sale tags, in-card highlights |
| `{typography.caption-sm}` | 12px | 400 | 1.33 | 0 | Footnotes, legal lines |
| `{typography.link-md}` | 16px | 500 | 1.38 | 0 | Inline link emphasis |
| `{typography.button-md}` | 14px | 600 | 1.4 | 0.7px | Primary/secondary button labels (uppercase) |
| `{typography.button-sm}` | 12.6px | 700 | 1.0 | 0.126px | Compact button labels in tight cells |
| `{typography.price-md}` | 24px | 500 | 1.17 | 0 | Tier and product price stamps |

### Principles

The typographic decision worth flagging: HP runs **weight 500 for every display size**, including the largest 72px hero headline. Most editorial systems jump to 600/700 at hero scale; HP doesn't. The result feels open and approachable rather than commanding — appropriate for a brand that sells across consumer, SMB, and enterprise audiences in the same catalog.

Forma DJR Micro's rounded-grotesque shapes do most of the warmth. There's no italic in the system except inside legal disclaimers; emphasis is carried by weight (500 → body-emphasis, 700 → caption-bold) instead.

### Note on Font Substitutes

Forma DJR Micro is proprietary (Commercial Type / Mark Caneso). Closest open-source substitutes:
- **Inter** at weights 400 / 500 / 600 / 700 — slightly narrower than Forma DJR Micro; bump font-size by ~3% to compensate
- **Manrope** at weights 400 / 500 / 600 / 700 — closer in proportion, gentler curves; use directly with no metric adjustment
- **Roboto** at weights 400 / 500 / 700 — flatter character; use as last-resort fallback

When swapping, set body line-height to 1.4 and display line-height to 1.0 explicitly — the Forma DJR Micro line-height numbers are tight, and most substitutes default looser.

## Layout

### Spacing System

- **Base unit**: 8px. Smaller half-step at 4px. The scale is gentle — most card padding lands at 16px or 24px; section gap at 80px.
- **Tokens (front matter)**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 20px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.section}` 80px
- **Section padding**: `{spacing.section}` (80px) vertical between major bands on desktop; collapses to ~48px on mobile.
- **Card internal padding**: `{spacing.xl}` (24px) for product cards; `{spacing.xxl}` (32px) for promo strips and feature cards; `{spacing.md}` (16px) for compact article tiles.
- **Gutter**: `{spacing.xl}` (24px) between grid columns at desktop; `{spacing.md}` (16px) on tablet/mobile.

The 80px section gap is the universal rhythm constant — it appears between every major homepage band, between the hero and the comparison table on the printer-plan page, and between feature rows on the laptop-shop page.

### Grid & Container

- **Desktop max-width**: 1366px content container with full-bleed-on-canvas section backgrounds.
- **Hero**: a single full-width photo card (homepage and laptop-hub hero) with the headline overlay positioned upper-left or upper-right.
- **Product family grid**: 4 columns at >1200px, 3 at 1024–1199px, 2 at 768–1023px, 1 below 768px.
- **Pricing tiers**: 4 columns at >1024px, 2x2 grid at 768–1023px, single-column accordion below 768px.
- **Footer**: 5-column link grid at >1024px, collapsing to 2-column then accordion on mobile.

### Whitespace Philosophy

Whitespace is **commercial-clean** — generous around hero photography, tight around catalog spec rows. Product cards leave breathing room above and below the photo (≥32px) so the laptop or printer reads as a hero shot rather than a thumbnail. The fine-print disclaimer regions (legal, footnote rows) tighten line-height to 1.3 and shrink type to 11–12px so the bulk of fine print stays compact.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow. | Section bands (white, cloud, fog), full-bleed photo heroes |
| 1 — Hairline | 1px solid `{colors.hairline}` (`#e8e8e8`) border, no shadow. Controls use `{colors.hairline-control}` instead. | Outlined buttons, comparison-table cells, FAQ accordion outers |
| 2 — Soft Lift | `{shadow.soft-lift}` — `0 2px 8px rgba(26, 26, 26, 0.08)`. | Product cards, pricing-tier columns, customer-story tiles |
| 3 — Floating Modal | `{shadow.floating}` — `0 8px 24px rgba(26, 26, 26, 0.12)`. | Add-to-cart drawer, mobile-nav sheet, image zoom modal |

Elevation is expressed one way only: **shadow for lift, hairline for enclosure, never both on the same element.** A card that carries `{shadow.soft-lift}` carries no border; a comparison-table cell carries a hairline and no shadow.

The system is mostly flat — depth is communicated by **color contrast** (cloud-band vs. white card on the same band) rather than shadow elevation. The honest measurement: `{colors.canvas}` to `{colors.surface}` is 1.00:1, canvas to `{colors.cloud}` is 1.07:1, canvas to `{colors.fog}` is 1.23:1, cloud to fog is 1.14:1. None of those layer separations is visible as tone alone, so `{shadow.soft-lift}` is load-bearing rather than ornamental, and a build that drops the shadow loses the card entirely. The Soft Lift level is the workhorse for the catalog — every product tile and pricing column gets it; nothing else does. Modal-floating is rare and reserved for transient overlays.

### Decorative Depth

The system's most distinctive depth gesture is the **HP blue chevron pair** — two angular `{colors.primary}` slashes (no radius, no shadow) that sit on the left and right of the homepage hero card and the laptop-shop hero. They're not decorative noise; they're a literal echo of the HP wordmark's two parallel slashes, scaled up to architectural size. Treat them as a brand artifact, not a generic geometric flourish.

Photography on the homepage and laptop-shop pages frames product imagery inside `{rounded.xl}` (16px) containers with a soft 1px hairline. Lifestyle photography (testimonials, "How HP works for X") sits full-bleed inside dark-navy slabs without rounding.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Hero chevron decorations, full-bleed photo heroes, marquee strips |
| `{rounded.xs}` | 2px | Secondary chip backgrounds, sale-tag pills |
| `{rounded.sm}` | 3px | Default secondary CTA radius (small touch zones) |
| `{rounded.md}` | 4px | Primary buttons, secondary buttons, text inputs |
| `{rounded.lg}` | 8px | Badge pills, category-icon cards, FAQ row containers |
| `{rounded.xl}` | 16px | Product cards, pricing tiers, customer-story tiles, photo frames |
| `{rounded.pill}` | 9999px | Category sub-nav tabs, search-pill input, filter chips |

The system maintains a clear two-tier philosophy: **buttons stay sharp** (4px, almost rectilinear) while **cards and photo frames stay soft** (16px). This split is the visual signature — sharp interactive elements against softer container surfaces.

### Photography Geometry

Hero photography sits in `{rounded.xl}` (16px) frames with no border. Product family thumbnails inside the laptop-grid are 1:1 (square) on a `{colors.canvas}` background, padded so the laptop is shown at ~70% of the frame. Customer-story photography uses 16:9 inside the same `{rounded.xl}` frame. There are no full-bleed circular avatars; testimonial avatars are 4px-rounded squares.

## Components

> **Extracted versus prescribed.** The per-component specs below are extracted: default and active/pressed only, the two states the live pages expose as static CSS. The `### Interaction States` table at the end of this section is **prescribed** — no hover, focus, loading, selected or error state was measured from the live site. Variants live as separate front-matter entries.

### Buttons

**`button-primary`** — the lone HP Electric Blue CTA
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button-md}` (uppercase, 0.7px tracking), padding `{spacing.sm} {spacing.xl}` (12 × 24), height 44px, rounded `{rounded.md}`
- Pressed state `button-primary-pressed` — background `{colors.primary-deep}`, same text
- Disabled state `button-primary-disabled` — background `{colors.steel}`, white text
- Used for: "Buy now", "Shop now", "Get a printer", primary form submit

**`button-ink`** — black filled CTA
- Background `{colors.ink}`, text `{colors.on-primary}`, padding `{spacing.sm} {spacing.xl}`, height 44px, rounded `{rounded.md}`, type `{typography.button-md}`
- Used for: "Buy now" on dark photo overlays, secondary primary actions where the blue would clash with imagery

**`button-outline`** — blue-text outlined CTA
- Background `{colors.canvas}`, text `{colors.primary}`, 1px `{colors.primary}` border, padding `{spacing.sm} {spacing.xl}`, height 44px, rounded `{rounded.md}`
- Used for: "Compare", "Customize", "Learn more" — secondary actions on white surfaces

**`button-outline-ink`** — black-text outlined CTA
- Background `{colors.canvas}`, text `{colors.ink}`, 1px `{colors.ink}` border, padding `{spacing.sm} {spacing.xl}`, height 44px, rounded `{rounded.md}`
- Used for: "View" buttons inside product family card grids — neutral against the blue primary

**`button-text-link`** — inline blue link with underline
- Background `{colors.canvas}`, text `{colors.primary}`, type `{typography.link-md}`, padding `{spacing.xxs} 0`
- Used for: "See details", "Read more" inside cards and disclaimer rows

### Cards & Containers

**`card-product`** — the workhorse product tile
- Background `{colors.canvas}`, rounded `{rounded.xl}` (16px), padding `{spacing.xl}` (24px), Soft Lift shadow
- Layout: hero photo (1:1 ratio) on top, title in `{typography.display-xs}`, spec rows in `{typography.caption-md}`, price in `{typography.price-md}`, CTA pinned to bottom
- Used for: laptop catalog cards, desktop catalog cards

**`card-product-feature`** — full-row feature card with photo + copy
- Background `{colors.cloud}`, rounded `{rounded.xl}`, padding `{spacing.xxl}` (32px)
- Layout: photo on the left (50% width), copy on the right with section eyebrow + title + body + CTA pair
- Used for: "Trending laptops" feature rows, "Shop these must haves"

**`card-pricing-tier`** + **`card-pricing-tier-featured`**
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xl}`, Soft Lift shadow
- Tier name in `{typography.display-sm}`, monthly price in `{typography.display-md}` with `{typography.caption-md}` cadence, page count caption, full feature list, primary CTA
- Featured tier carries `{colors.primary}` text accent on the price-stamp + a `{colors.primary}` thin top border instead of a colored card background — never inverted to dark

**`card-customer-story`** — the three-up testimonial tile
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.md}` (16px), Soft Lift shadow
- 16:9 photo at top in `{rounded.xl}` frame, quote excerpt in `{typography.body-md}`, attribution row at the bottom
- Used in the "See what our customers say" homepage section

**`card-article-tile`** — the four-up "Latest from HP" tile
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.md}`, Soft Lift shadow
- 16:9 thumbnail at top, date eyebrow in `{typography.caption-sm}`, title in `{typography.body-emphasis}`, "Read more" link

**`card-category-icon`** — the small icon-and-label card in the homepage "Our Products" row
- Background `{colors.canvas}`, rounded `{rounded.lg}` (8px), padding `{spacing.md}`
- 48px icon at top, label in `{typography.body-emphasis}` below
- Used for: Laptops, Desktops, Printers, Computer Tools, Accessories, Enterprise Solutions

**`hero-promo-card`** — the homepage hero card with chevron decorations
- Background `{colors.canvas}`, rounded `{rounded.xl}`, padding `{spacing.xxl}` (32px)
- Photography occupies left half; copy block (eyebrow + headline + price stamp + CTA pair) occupies right half
- Flanked by `chevron-decoration` blue slashes outside the card's bounding box on left and right edges

**`promo-strip-dark`** — the inline dark navy promo block
- Background `{colors.ink}`, text `{colors.on-ink}`, rounded `{rounded.xl}`, padding `{spacing.xxl} 48px`
- Used for: "When did work start getting in the way of work?" mid-page promo, the SMB testimonial slab

### Inputs & Forms

**`text-input`** + **`text-input-focused`**
- Background `{colors.canvas}`, text `{colors.ink}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, height 44px
- Extracted: 1px `{colors.steel}` border in default; gains 1px `{colors.ink}` border on focus (no halo)
- Prescribed correction: the default border moves to 1px `{colors.hairline-control}` (4.54:1), because `{colors.steel}` at 1.78:1 is the input's only boundary and fails the 3:1 non-text minimum. Focus adds the 2px `{colors.focus}` ring plus the `{colors.focus-inset}` offset, keeping the extracted ink border underneath

**`text-input-search`** — pill search in the top nav
- Background `{colors.canvas}`, rounded `{rounded.md}`, padding `{spacing.sm} {spacing.md}`, height 40px, 1px `{colors.steel}` border, magnifying-glass icon at right

**`badge-pill-ink`** — filled tag pill
- Background `{colors.ink}`, text `{colors.on-primary}`, rounded `{rounded.lg}`, padding 6px 12px, type `{typography.body-md}`
- Used inline next to product titles to mark "New" or featured indicators

**`badge-pill-outline`** — outlined tag pill
- Background `{colors.canvas}`, text `{colors.ink}`, 1px `{colors.ink}` border, rounded `{rounded.lg}`, padding 6px 12px

**`badge-sale-coral`** — the sale price-stamp
- Background `{colors.bloom-coral}`, text `{colors.on-primary}`, rounded `{rounded.sm}`, padding `{spacing.xxs} {spacing.xs}`, type `{typography.caption-bold}`
- Used for: "Save $200", "25% off" overlay tags on hero promo cards

### Navigation

**`utility-strip`** — the top-of-page utility bar
- Background `{colors.ink}`, text `{colors.on-primary}`, height 36px, padding 0 {spacing.xl}, type `{typography.caption-md}`
- Holds: country/locale picker, "For Business / For Home" toggle, "Sign in" link, cart link

**`nav-bar-top`** — desktop top nav (sits below utility strip)
- Background `{colors.canvas}`, height 64px, padding 0 32px
- Layout: HP wordmark logo flush left → middle category list (Laptops / Desktops / Printers / Accessories / Solutions / Support) → right slot with Search field, Sign-in link, Cart icon
- 1px `{colors.hairline}` bottom border separates nav from page

**`nav-link`**
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, padding `{spacing.xs} {spacing.md}`
- Active page draws a 2px `{colors.primary}` underline below the text baseline

**Top Nav (Mobile)**
- Same height, hamburger icon replaces the middle category list, Search and Cart stay visible
- Drawer expands as a full-canvas sheet with `{typography.body-lg}` link list and a sticky Sign-in CTA at bottom

**`category-tab`** + **`category-tab-active`** — the pill sub-nav
- Default: background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-emphasis}`, rounded `{rounded.pill}`, padding `{spacing.xs} {spacing.lg}`
- Active: background `{colors.ink}`, text `{colors.on-primary}`, same rounding
- Used on the laptop-shop page for "All / Trending / On Sale" filtering, and on the homepage "How can we help?" closing band

### Signature Components

**`chevron-decoration`** — the geometric blue slash motif
- Background `{colors.primary}`, rounded `{rounded.none}`, no shadow
- Renders as a sharp parallelogram cut at ~60° angle, sized to the height of the hero card it flanks
- Reserved for hero bands and full-page banners — never decorative noise inside cards

**`faq-row`** — the accordion row on the printer-plan FAQ
- Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.lg} {spacing.xl}`, type `{typography.body-emphasis}`
- 1px `{colors.hairline}` divider between rows; chevron-down icon on the right collapsed, chevron-up when expanded
- Body answer renders inside the same row container in `{typography.body-md}` after expansion

**`help-band-dark`** — the closing "How can we help?" prelude band
- Background `{colors.ink}`, text `{colors.on-primary}`, padding 64px {spacing.xl}
- Layout: large lifestyle photograph as the band background (low-opacity) with chip-style category tabs centered: Browse Topics / Live Chat / Contact / Diagnose / Order Status

**`footer-dark`**
- Background `{colors.ink}`, text `{colors.on-primary}`, type `{typography.body-md}`, padding 64px {spacing.xl}
- 5-column link grid (Company / Shop / Support / Resources / Connect) with `{typography.body-emphasis}` headers and `{typography.caption-md}` link rows
- Bottom strip carries social icons, language picker, and legal lines in `{typography.caption-sm}` muted to `{colors.steel}`

### Interaction States

**Prescribed, not extracted.** Only default and active/pressed were readable from the live pages; everything else below is specified to match HP's one-accent, flat, hairline-led system. Hover never introduces a new hue — it shifts to `{colors.primary-deep}`, drops to `{colors.cloud}`, or thickens the existing boundary.

| Component | Default | Hover | Focus-visible | Active / pressed | Disabled | Loading | Selected | Error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.primary}` fill | fill → `{colors.primary-deep}` | 2px `{colors.focus}` ring + `{colors.focus-inset}` offset | `button-primary-pressed` fill, 0.98 scale | `button-primary-disabled` (`{colors.steel}` fill) | label swaps for a 16px spinner, width frozen | n/a — not a toggle | n/a — form-level |
| `button-ink` | `{colors.ink}` fill | fill → `{colors.ink-soft}` | 2px `{colors.focus}` ring + offset; `{colors.focus-on-dark}` when over a dark slab | 0.98 scale, no colour change | `{colors.steel}` fill, `{colors.canvas}` label | spinner as above | n/a | n/a |
| `button-outline` / `button-outline-ink` | 1px border, `{colors.canvas}` fill | fill → `{colors.cloud}`, border unchanged | 2px `{colors.focus}` ring + offset | fill → `{colors.fog}` | border and label → `{colors.steel}` | spinner replaces label | n/a | n/a |
| `button-text-link` | `{colors.primary}`, underline | `{colors.primary-deep}`, underline thickens to 2px | 2px `{colors.focus}` ring, 2px offset | `{colors.link-pressed}` | `{colors.steel}`, no underline | n/a | n/a | n/a |
| `text-input` / `text-input-search` | 1px `{colors.hairline-control}` | border → `{colors.ink}` | `text-input-focused` + 2px `{colors.focus}` ring | n/a — not pressable | `{colors.cloud}` fill, `{colors.steel}` border and text | trailing 16px spinner inside the field | n/a | 1px `{colors.error}` border + `{typography.caption-md}` message in `{colors.error}` below |
| `category-tab` | `{colors.canvas}` pill, `{colors.ink}` label | fill → `{colors.cloud}` | 2px `{colors.focus}` ring, 2px offset outside the pill | 0.98 scale | label → `{colors.steel}`, no fill | n/a | `category-tab-active` — `{colors.ink}` fill, `{colors.on-primary}` label | n/a |
| `faq-row` | collapsed, `{colors.hairline}` divider | row fill → `{colors.cloud}` | 2px `{colors.focus}` ring on the whole row | chevron rotates 180° | n/a | n/a | expanded row keeps `{colors.cloud}` fill while open | n/a |
| `card-product` / `card-article-tile` / `card-customer-story` | `{shadow.soft-lift}` | shadow → `{shadow.floating}`, title → `{colors.primary}`, no card travel | 2px `{colors.focus}` ring on the card bounds | 0.99 scale | whole card at 0.4 opacity, pointer-events off | skeleton blocks in `{colors.fog}`, no shimmer travel | `{colors.primary}` 2px top border, as on `card-pricing-tier-featured` | out-of-stock line in `{colors.error}`, `{typography.caption-md}` |
| `nav-link` | `{colors.ink}` | 2px `{colors.primary}` underline fades in | 2px `{colors.focus}` ring | underline at full opacity | `{colors.steel}` | n/a | active page keeps the 2px `{colors.primary}` underline | n/a |
| `badge-pill-ink` / `badge-pill-outline` / `badge-sale-coral` | static | none — **genuinely two-state** (present / absent); badges are not interactive | none | none | none | none | none | none |
| `chevron-decoration` | static | none — **genuinely one state**; decoration only, never focusable | none | none | none | none | none | none |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or transition was extracted from HP's pages; every value below is the shared **Calm** profile applied to HP's own surfaces. Calm is the right fit: one chromatic accent, display weight 500 at every size, a flat shadow ladder, no gradients and an explicit rule against opacity tricks — a composed, editorial catalog rather than a springy consumer toy or a cinematic hardware reveal.

Durations and easings are referenced as tokens: `{motion.duration-instant}` 80ms, `{motion.duration-fast}` 150ms, `{motion.duration-base}` 250ms, `{motion.duration-slow}` 400ms, `{motion.duration-emphasis}` 500ms, `{motion.stagger-step}` 40ms, `{motion.duration-reduced}` 150ms.

Only `transform` and `opacity` are animated — never `width`, `height`, `top`, `left` or `margin`. The chevron decorations do not move; they are architecture, not animation.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav-link, card) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `box-shadow`; underline reveals via `transform: scaleX()` from the left | colour and shadow swap instantly, no scaleX travel |
| Press (button, tab, card) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | scale removed entirely; fill change only |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-enter}` | `opacity` on the `{colors.focus}` ring | ring appears at full opacity with no transition |
| Page / route transition | `{motion.duration-base}` out, `{motion.duration-fast}` in | `{motion.ease-standard}` | `opacity` only; no slide, no band travel | cross-fade at `{motion.duration-reduced}` |
| Modal / add-to-cart drawer | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px)` for the modal; `translateX(100%)` for the right-side drawer | opacity fade at `{motion.duration-reduced}`, no translate; scrim fades only |
| Dropdown (locale picker, nav mega-menu) | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(-4px)` | opacity only at `{motion.duration-reduced}` |
| Toast / cart confirmation | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px)` | opacity only at `{motion.duration-reduced}`; auto-dismiss timer unchanged |
| List enter (product grid, article tiles) | `{motion.duration-base}` per item, `{motion.stagger-step}` apart, capped at 8 items | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px)` | all items fade together at `{motion.duration-reduced}`, no stagger, no travel |
| List exit (filter change, remove from cart) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)` | opacity only at `{motion.duration-reduced}` |
| Loading (spinner, skeleton) | 900ms linear loop (spinner); skeletons cross-fade at `{motion.duration-slow}` | linear / `{motion.ease-standard}` | `transform: rotate()` on the spinner; `opacity` on skeleton blocks | spinner becomes a static 25%-arc glyph with a text label; skeletons hold at one opacity |
| Hero / band entrance on first paint | none | — | — | none — nothing animates on first paint; content is never delayed by a reveal |

Exit is always shorter than its matching entrance. The spinner is the only infinite animation in the system; there is no brand ambience loop.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate, all scale, the list stagger, the spinner's
     rotation loop, and the nav underline's scaleX reveal.
     Kept: opacity cross-fades, capped at {motion.duration-reduced} (150ms).
     Frozen: skeleton blocks hold a single opacity; the spinner renders as a
     static arc with a visible "Loading…" label. */
  *, *::before, *::after {
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 150ms !important;
    transition-property: opacity, color, background-color, border-color, box-shadow !important;
  }
}
```

## Accessibility

### Measured contrast

Every ratio below is computed with WCAG 2.1 relative luminance from this file's own hexes.

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#1a1a1a` on `{colors.canvas}` `#ffffff` | 17.4:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.surface}` `#ffffff` | 17.4:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.cloud}` `#f7f7f7` | 16.25:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.fog}` `#e8e8e8` | 14.2:1 | 4.5:1 | pass |
| `{colors.text-dim}` / `{colors.charcoal}` `#3d3d3d` on `{colors.canvas}` | 10.86:1 | 4.5:1 | pass |
| `{colors.graphite}` `#636363` on `{colors.canvas}` | 6.01:1 | 4.5:1 | pass |
| `{colors.graphite}` on `{colors.cloud}` | 5.61:1 | 4.5:1 | pass |
| `{colors.on-primary}` `#ffffff` on `{colors.primary}` `#024ad8` | 7.06:1 | 4.5:1 | pass |
| `{colors.primary}` as link text on `{colors.canvas}` | 7.06:1 | 4.5:1 | pass |
| `{colors.on-ink}` `#ffffff` on `{colors.ink}` | 17.4:1 | 4.5:1 | pass |
| `{colors.primary-bright}` `#296ef9` on `{colors.ink}` | 3.89:1 | 4.5:1 | **fail** — see below |
| `{colors.error}` / `{colors.bloom-deep}` `#b3262b` on `{colors.canvas}` | 6.5:1 | 4.5:1 | pass |
| `{colors.storm-deep}` `#356373` on `{colors.canvas}` | 6.6:1 | 4.5:1 | pass |
| `{colors.hairline-control}` `#767676` on `{colors.canvas}` | 4.54:1 | 3.0:1 | pass |
| `{colors.hairline-control}` on `{colors.fog}` | 3.71:1 | 3.0:1 | pass |
| `{colors.hairline}` `#e8e8e8` on `{colors.canvas}` | 1.23:1 | 3.0:1 | **fail — disclosed** |
| `{colors.hairline}` on `{colors.surface}` `#ffffff` | 1.23:1 | 3.0:1 | **fail — disclosed** |
| `{colors.hairline-strong}` / `{colors.steel}` `#c2c2c2` on `{colors.canvas}` | 1.78:1 | 3.0:1 | **fail — disclosed** |
| `{colors.hairline-strong}` on `{colors.surface}` | 1.78:1 | 3.0:1 | **fail — disclosed** |
| `badge-sale-coral`: `#ffffff` on `{colors.bloom-coral}` `#ff5050` | 3.22:1 | 4.5:1 | **fail — disclosed** |
| `{colors.focus}` `#0e3191` on `{colors.canvas}` | 11.25:1 | 3.0:1 | pass |
| `{colors.focus}` on `{colors.primary}` `#024ad8` | 1.59:1 | 3.0:1 | **fail — disclosed**, mitigated by `{colors.focus-inset}` |

### Where the real brand fails AA, plainly

- **Both extracted hairlines fail the 3:1 non-text minimum.** `{colors.hairline}` at 1.23:1 and `{colors.hairline-strong}` at 1.78:1 are frozen extracted facts, not mistakes to patch. HP's real site draws input and comparison-table boundaries with tones a low-vision user cannot see against white. The parallel prescribed token `{colors.hairline-control}` (4.54:1) exists for every boundary that carries meaning; the originals are scoped to decoration.
- **`{colors.steel}` as disabled-button fill carries white text at 1.78:1.** WCAG sets no contrast requirement on disabled controls, so this is not a violation, but a disabled HP CTA is genuinely hard to read.
- **The coral sale chip fails.** White `{typography.caption-bold}` on `{colors.bloom-coral}` measures 3.22:1 against a 4.5:1 requirement. The hex is a real brand value and is not changed here. `{colors.ink}` on the same coral would measure 5.4:1.
- **`{colors.primary-bright}` on the dark slabs fails at body size.** 3.89:1 clears 3:1 for large text (24px+, or 18.66px+ at weight 700) but not 4.5:1 for body copy. Inside an `{colors.ink}` slab, use it for `{typography.display-sm}` and up, or `{colors.on-ink}` for body links.
- **No layer separation is tonal.** `{colors.canvas}` to `{colors.surface}` is 1.00:1 and canvas to `{colors.cloud}` is 1.07:1; a build that drops `{shadow.soft-lift}` leaves cards invisible.

### Focus ring visibility, surface by surface

| Surface | Ring | Measured |
|---|---|---|
| `{colors.canvas}` / `{colors.surface}` / `{colors.paper}` `#ffffff` | `{colors.focus}` | 11.25:1 |
| `{colors.cloud}` `#f7f7f7` | `{colors.focus}` | 10.5:1 |
| `{colors.fog}` `#e8e8e8` | `{colors.focus}` | 9.18:1 |
| `{colors.primary}` `#024ad8` CTA fill | `{colors.focus}` alone is 1.59:1 — **never used alone here.** The mandatory 2px `{colors.focus-inset}` `#ffffff` offset sits between fill and ring; band-to-band separation is 11.25:1, which is what WCAG 2.2 Focus Appearance measures | 11.25:1 band-to-band |
| `{colors.ink}` `#1a1a1a` slabs (testimonial, help band, footer) | `{colors.focus-on-dark}` `#c9e0fc` | 12.89:1 |
| Full-bleed hero photography | two-tone: 2px `{colors.focus}` with a 1px `{colors.focus-inset}` outer edge, so one band always separates from the image | not measurable — photography has no fixed colour |

The ring is 2px with a 2px offset, drawn on `:focus-visible` only, and is never removed without a replacement. `{rounded.pill}` elements get a pill-shaped ring; everything else inherits the element's own radius.

### Tap targets

Every interactive element is specified at 44×44px minimum: `button-primary`, `button-ink`, `button-outline` and `text-input` are 44px tall by token; `text-input-search` at 40px is the one exception and gains a 44px invisible hit box. `category-tab` pads to 12px 24px on touch. **Not verified here:** these are document values. Rendered tap-target size needs a real page, so no claim in this file is a measurement of the live site.

### Reduced motion

`@media (prefers-reduced-motion: reduce)` is honoured system-wide, as specified in `## Motion & Animation`: all translate and scale removed, the list stagger removed, the spinner's rotation loop frozen to a static arc with a text label, and opacity fades capped at `{motion.duration-reduced}` (150ms).

### Other

- Colour is never the only signal: the active `category-tab` inverts its fill *and* its label, the error state adds a `{typography.caption-md}` message beside the `{colors.error}` border, and links keep an underline.
- The file's own rule against dropping ink opacity for hierarchy is an accessibility win — hierarchy comes from `{colors.text-dim}` and `{colors.graphite}`, both of which pass AA.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` for the primary CTA, link color, and `chevron-decoration` motif — at most twice per viewport
- Set every headline in Forma DJR Micro at weight 500 with line-height 1.0 — resist the urge to bump weight at hero scale
- Use `{rounded.xl}` (16px) for cards and photo frames; `{rounded.md}` (4px) for buttons and inputs — keep the two-tier split sharp
- Pair white `{colors.canvas}` body bands with `{colors.cloud}` (`#f7f7f7`) alternating bands; let the gray do the breathing
- Close every page rhythm with a dark-navy `{colors.ink}` slab — the "How can we help?" prelude + footer
- Set button labels in uppercase with `{typography.button-md}` (0.7px tracking) — the only place the system tracks letters
- Use Soft Lift shadow exclusively for product cards and pricing tiers — leave section bands flat
- Frame product photography inside `{rounded.xl}` containers; never use full-bleed circular masks

### Don't
- Don't introduce secondary saturated colors outside `{colors.primary}` family + the `bloom-coral` sale-tag and `storm` printer-plan accents
- Don't apply heavy material shadows — depth is via color contrast (cloud vs. white) and Soft Lift only
- Don't round buttons above `{rounded.md}` (4px); a soft 8px+ button reads as a different brand
- Don't run Forma DJR Micro below 12px — small caption at 11px is the floor
- Don't use the chevron decoration as inline noise; it is a hero-only architectural element tied to the wordmark
- Don't drop ink text opacity to create hierarchy — switch surface or shift to `{colors.charcoal}` / `{colors.graphite}` instead
- Don't replace the HP wordmark with a generic sans lockup; the wordmark is a custom mark with its own ratio

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 480px | Single-column stack; hamburger nav; section padding drops to ~48px; hero serif scales to ~36px |
| Mobile-Large | 480–767px | Same column count; hero scales to ~44px; pricing tiers stack vertically |
| Tablet | 768–1023px | 2-column product grid; pricing 2x2; nav still full text labels |
| Desktop | 1024–1279px | 3-column product grid; 4-column pricing; full nav |
| Desktop-Large | ≥ 1280px | 4-column product grid; 1366px content max-width with full-bleed bands |

### Touch Targets

Every interactive element clears 44×44px on mobile. `button-primary` at 44px height + 24px horizontal padding meets WCAG-AAA touch target. `category-tab` at 8px 20px padding bumps to 12px 24px on touch screens. Nav-link tap areas extend invisibly beyond the text run to the full 44px row height. Sticky cart/sign-in icons in the top nav use 44×44 invisible hit boxes around their visible 24×24 glyph.

### Collapsing Strategy

- **Utility strip**: stays visible on every breakpoint; dropdowns collapse into a single "Account" icon below 768px
- **Top nav**: middle category list collapses into a hamburger drawer below 1024px; the right-side Search + Sign-in + Cart stay visible
- **Hero**: stays single-column at every breakpoint; chevron decorations shrink to ~60% size on tablet and disappear entirely on mobile
- **Product family grid**: 4 → 3 → 2 → 1 column as breakpoints shrink; cards keep `{rounded.xl}` corners at every size
- **Pricing comparison table**: 4-column grid on desktop collapses to 2x2 on tablet, then stacks into individual accordion-style cards on mobile
- **Footer**: 5-column link grid → 2-column tablet → single-column accordion on mobile; HP wordmark stays flush left

### Image Behavior

Hero photography uses `{rounded.xl}` containers at every breakpoint. The chevron decorations vanish on mobile; the underlying photo card centers in the viewport. Lifestyle photography in the testimonial and "how-can-we-help" bands maintains 16:9 ratio with horizontal cropping rather than letterboxing on mobile. There are no art-direction crop swaps between desktop and mobile — the same image is used at every size.

## Iteration Guide

1. Focus on ONE component at a time; resist refactoring an entire section in one pass
2. Reference component names and tokens directly (`{colors.primary}`, `{typography.display-xxl}`, `{rounded.xl}`, `card-product`) — do not paraphrase to hex/px in prose
3. Run `npx @google/design.md lint DESIGN.md` after edits — `broken-ref`, `contrast-ratio`, and `orphaned-tokens` warnings flag issues automatically
4. Add new variants as separate component entries (`-pressed`, `-disabled`, `-focused`); never bury state inside prose
5. Default body to `{typography.body-md}`; reach for `{typography.body-emphasis}` for run-in bolds; keep display sizes for true heading roles
6. Keep `{colors.primary}` scarce — at most two flame elements per viewport (one CTA + one chevron decoration). Three flame items in one viewport is over-saturation
7. When introducing a new section band, choose from `{colors.canvas}` / `{colors.cloud}` / `{colors.fog}` / `{colors.ink}` — six pre-defined surface modes is the entire surface vocabulary

## Known Gaps

**Prescribed, not extracted.** These parts of the document are specified rather than measured, and a build should treat them as a reasonable default, not as HP's own decision:

- **The whole motion system.** No duration, easing, stagger or transition was taken from HP's live pages. `## Motion & Animation` applies the shared Calm profile.
- **Every state except default and active/pressed.** Hover, focus-visible, disabled on non-button components, loading, selected and error are prescribed in `### Interaction States`. The extracted front matter only ever carried `-pressed`, `-disabled` and `-focused` variants.
- **The focus ring.** `{colors.focus}`, `{colors.focus-inset}` and `{colors.focus-on-dark}` are all prescribed. HP's real ring was not captured; these are chosen from the brand's own blues and measured against this file's surfaces.
- **`{colors.hairline-control}`** `#767676` is prescribed, not an HP value. It exists because both extracted hairlines fail 3:1.
- **Role aliases.** `{colors.surface}` and `{colors.text-dim}` duplicate `{colors.paper}` and `{colors.charcoal}` so the required roles resolve. They add no new hex.

**Genuinely unknown:**

- The exact chevron geometry. The Overview calls the cut 45°, `chevron-decoration` says ~60°; neither was measured, and the two statements are left as they were found rather than silently reconciled.
- Whether `{colors.ink-soft}` `#292929` and `{colors.ink-deep}` `#000000` are distinct roles or extraction noise. At 1.20:1 and 1.21:1 against `{colors.ink}` neither reads as a tonal shift.
- `{rounded.xs}` 2px and `{rounded.sm}` 3px sit one unit apart in a ladder that otherwise doubles (4 → 8 → 16). Both appear in the Shapes table with distinct uses; the 3px step is likely a legacy value, but nothing in the file proves it.
- No dark theme. The `{colors.ink}` slabs are bands inside a light page, not a theme; there is no dark-mode canvas, and `{colors.focus-on-dark}` serves the slabs only.
- `{typography.button-sm}` at 12.6px with 0.126px tracking is an extracted computed value, not a designed one.
- **Not computable from a document:** overlap, horizontal overflow, clipping, rendered tap-target size, frame rate and layout shift. Nothing in this file is a claim about any of them.
