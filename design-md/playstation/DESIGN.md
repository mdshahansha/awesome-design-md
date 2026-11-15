---
version: alpha
name: PlayStation-design-analysis
description: |
  A three-surface marketing system organized around alternating black, white, and PlayStation Blue chapters that scroll past the viewer like a console launch trailer. Each section has a single editorial purpose — hero photography, console product render, PS Plus tier callout, news strip — and each owns one of three full-bleed canvas modes. The chrome is unusually quiet for a gaming brand: bright PlayStation Blue (`#0070d1`) carries every primary CTA as a fully-rounded pill, the proprietary SST face renders display copy at a signature weight 300 (light) for an airy, premium feel, and a crisp 8px-radius secondary card system carries product info on either canvas mode. The system never decorates — no gradient backgrounds on chrome, no atmospheric mesh, no drop shadows beyond a faint section-divide. Imagery does all the heavy lifting: console glamour shots, game key art, and PS Plus tier illustrations occupy 60-90% of every section, with copy compressed into a small editorial slot.

colors:
  primary: "#0070d1"
  primary-pressed: "#0064b7"
  primary-active: "#004d8d"
  on-primary: "#ffffff"
  link-light: "#0064b7"
  link-dark: "#53b1ff"
  commerce: "#d53b00"
  commerce-pressed: "#aa2f00"
  commerce-link-base: "#d63d00"
  on-commerce: "#ffffff"
  ink: "#000000"
  ink-deep: "#121314"
  ink-elevated: "#181818"
  charcoal: "#1f2024"
  body-light: "rgba(0,0,0,0.6)"
  mute-light: "#6b6b6b"
  ash-light: "#cccccc"
  body-dark: "rgba(255,255,255,0.7)"
  mute-dark: "rgba(229,229,229,0.55)"
  ash-dark: "rgba(229,229,229,0.2)"
  canvas-light: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#f5f7fa"
  surface-filter: "rgba(245,247,250,0.3)"
  canvas-dark: "#000000"
  surface-dark-elevated: "#121314"
  surface-dark-card: "#181818"
  hairline-light: "#f3f3f3"
  hairline-dark: "rgba(229,229,229,0.2)"
  focus: "#0070d1"
  focus-on-dark: "#ffffff"
  on-dark: "#ffffff"
  on-dark-mute: "#cccccc"
  warning: "#c81b3a"
  ps-plus-gold-start: "#ffce21"
  ps-plus-gold-mid: "#f5a623"
  ps-plus-gold-end: "#ee8e00"
  marathon-yellow: "#deff20"

typography:
  display-xl:
    fontFamily: PlayStation SST
    fontSize: 54px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.1px
  display-lg:
    fontFamily: PlayStation SST
    fontSize: 44px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  display-md:
    fontFamily: PlayStation SST
    fontSize: 35px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  heading-xl:
    fontFamily: PlayStation SST
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  heading-lg:
    fontFamily: PlayStation SST
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  heading-md:
    fontFamily: PlayStation SST
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  body-md:
    fontFamily: PlayStation SST
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  body-strong:
    fontFamily: PlayStation SST
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.4px
  body-sm:
    fontFamily: PlayStation SST
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-md:
    fontFamily: PlayStation SST
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: PlayStation SST
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  link-md:
    fontFamily: PlayStation SST
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-lg:
    fontFamily: PlayStation SST
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.45px
  button-md:
    fontFamily: PlayStation SST
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.324px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
  button-commerce:
    backgroundColor: "{colors.commerce}"
    textColor: "{colors.on-commerce}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-commerce-pressed:
    backgroundColor: "{colors.commerce-pressed}"
    textColor: "{colors.on-commerce}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
  button-secondary-light:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ash-light}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focused:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  filter-pill:
    backgroundColor: "{colors.surface-filter}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  filter-pill-active:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  product-card-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  game-tile:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  feature-card:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 32px
  hero-band-blue:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.none}"
    padding: 96px 48px
  hero-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: 96px 48px
  hero-band-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: 96px 48px
  ps-plus-banner:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-xl}"
    rounded: "{rounded.md}"
    padding: 48px 32px
  carousel-paddle:
    backgroundColor: "rgba(255,255,255,0.16)"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    size: 48px
  pagination-dot:
    backgroundColor: "{colors.ash-dark}"
    rounded: "{rounded.full}"
    size: 8px
  pagination-dot-active:
    backgroundColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    size: 8px
  badge-info:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  primary-nav:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
    height: 48px
  sub-nav:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.none}"
    height: 40px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.none}"
    padding: 48px 32px
  support-search-bar:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 56px
  support-row:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 16px 0px
  link-inline:
    textColor: "{colors.link-light}"
    typography: "{typography.link-md}"
---

## Overview

PlayStation's marketing system reads like a console launch trailer scrolling past the viewer in chapters. Each section is a full-bleed band — pure black `{colors.canvas-dark}`, true white `{colors.canvas-light}`, or PlayStation Blue `{colors.primary}` — and each chapter owns one editorial moment: hero console photography, a games-coming-soon strip, the PlayStation Plus tier banner, the "30 Years of PlayStation" anniversary band, the news strip from the PlayStation Blog. There is no decorative chrome between chapters; the section background change IS the divider. Sections stack at `{spacing.section}` (96px) rhythm with the next band's color taking over the page edge-to-edge.

The system has two distinct surface modes that alternate down the page: a **dark canvas mode** for editorial product moments (hero, "ON PLAYSTATION" band, marathon game pages) and a **light canvas mode** for utility surfaces (PS5 games listing, support pages, news index). Both modes use the same chrome vocabulary — fully-rounded `{rounded.full}` pill buttons, 8px-radius `{rounded.md}` cards, the proprietary PlayStation SST face — only the surface and on-surface colors change. The third surface mode is the **PlayStation Blue band** (`{colors.primary}` — `#0070d1`) reserved for the highest-priority moments: the Marathon launch CTA strip, the footer, and any "Action Required" banner.

The typography is the system's most distinctive choice. PlayStation SST renders display headlines at **weight 300** (light) — unusual for a gaming brand that could easily reach for bold geometric display faces. The light weight gives the chrome an airy, almost editorial quality that lets the imagery speak; copy is information rather than decoration. Heading sizes drop in tight increments (54 → 44 → 35 → 28 → 22 → 18) and body settles at 18px with 1.5 line-height for comfortable long-form reading on support and games pages.

**Key Characteristics:**
- Three-canvas chapter system: `{colors.canvas-dark}` (black), `{colors.canvas-light}` (white), `{colors.primary}` (PlayStation Blue) alternating down the page
- PlayStation Blue (`{colors.primary}` — `#0070d1`) is the universal primary CTA — fully-rounded pill at `{rounded.full}` (9999px)
- Commerce orange (`{colors.commerce}` — `#d53b00`) is the secondary CTA reserved for "Buy now" / "Pre-order" / store actions
- PlayStation SST display tier renders at **weight 300** with -0.1px to +0.4px tracking — the brand's signature airy editorial voice
- 8px-radius (`{rounded.md}`) for product cards and feature panels; 4px-radius (`{rounded.sm}`) for inputs; pills (`{rounded.full}`) for every CTA
- Game tiles, console renders, and PS Plus tier illustrations occupy 60-90% of each section — imagery does the storytelling
- Color-block page rhythm (one observed band sequence): dark hero → light console showcase → dark "Great PS4 & PS5 games" rail → light "Discover PlayStation Plus" tier band → light "30 years of PlayStation" callout → dark "ON PLAYSTATION" band → light news strip → blue footer

## Colors

> **Source pages:** `/en-tr/` (home), `/en-tr/ps5/games/` (PS5 games listing), `/en-tr/games/marathon/` (single game page), `/tr-tr/support/account/` (support center). The chrome palette is identical across all four pages; the support page uses the light-canvas mode exclusively while marketing pages alternate.

### Brand & Accent
- **PlayStation Blue** (`{colors.primary}` — `#0070d1`): the brand's universal primary. Every primary CTA pill, the active filter chip, the footer surface, badge fills, and inline link color on dark surfaces.
- **PlayStation Blue Pressed** (`{colors.primary-pressed}` — `#0064b7`): pressed state for the primary pill — also doubles as the inline link color on light surfaces.
- **PlayStation Blue Active** (`{colors.primary-active}` — `#004d8d`): deeply-pressed state for the primary button.
- **Commerce Orange** (`{colors.commerce}` — `#d53b00`): the secondary CTA reserved for store/buy/pre-order actions. The only warm color in the system.
- **Commerce Orange Pressed** (`{colors.commerce-pressed}` — `#aa2f00`): pressed state for commerce buttons.
- **Marathon Yellow** (`{colors.marathon-yellow}` — `#deff20`): a single high-saturation game-page accent extracted from Marathon's product palette — used only inside the dedicated `/marathon/` game page chrome and not part of the system's general accent vocabulary.

### Surface
- **Canvas Dark** (`{colors.canvas-dark}` — `#000000`): pure black hero band, primary nav background, footer base. The dominant surface for editorial product moments.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — `#121314`): inset dark panels, PS Plus tier banner background, "ON PLAYSTATION" gradient end.
- **Surface Dark Card** (`{colors.surface-dark-card}` — `#181818`): game tile fill, dark product card background.
- **Canvas Light** (`{colors.canvas-light}` — `#ffffff`): true white console-showcase band, support page body, news strip background.
- **Soft Surface** (`{colors.surface-soft}` — `#f3f3f3`): hairline-soft band fill on light pages, divider rule on light surfaces.
- **Surface Card** (`{colors.surface-card}` — `#f5f7fa`): cool-blue-tinted product card and tier-card background on light canvas.
- **Surface Filter** (`{colors.surface-filter}` — `rgba(245,247,250,0.3)`): translucent fill for filter-pill default state on light canvas.
- **Hairline Light** (`{colors.hairline-light}` — `#f3f3f3`): 1px divider rule on light pages. **Decorative only.** It measures 1.11:1 on `{colors.canvas-light}` and 1.00:1 on `{colors.surface-soft}` — it is the extracted brand value and is kept as-is, but it must never be the only boundary of an interactive control. Use `{colors.mute-light}` for those (see below).
- **Hairline Dark** (`{colors.hairline-dark}` — `rgba(229,229,229,0.2)`): translucent 1px divider on dark canvas. Composites to `#2e2e2e` over `{colors.canvas-dark}` at 1.55:1 — decorative only, same restriction as the light hairline.
- **Control boundary** — **prescribed, not extracted.** Where a boundary carries meaning rather than decoration (`{component.text-input}`, `{component.button-secondary-light}`), draw it in `{colors.mute-light}` (`#6b6b6b`), which measures 5.33:1 on `{colors.canvas-light}`, 4.80:1 on `{colors.surface-soft}` and 4.97:1 on `{colors.surface-card}`. The palette already owned a tone that clears 3:1, so no new boundary token was added. The 1px `{colors.ash-light}` border the live inputs actually use measures 1.61:1 and fails WCAG 1.4.11.

### Focus
Both tokens below are **prescribed, not extracted** — the captured pages expose no focus-ring value, and `{component.text-input-focused}` signals focus with a 2px border-weight change only, which is not a focus indicator for any other control.

- **Focus** (`{colors.focus}` — `#0070d1`, PlayStation Blue): the default ring, drawn as a 2px solid ring with a 2px offset **outside** the control, so it is measured against the surface behind it. 4.95:1 on `{colors.canvas-light}`, 4.47:1 on `{colors.surface-soft}`, 4.62:1 on `{colors.surface-card}`, 3.58:1 on `{colors.surface-dark-card}`.
- **Focus on Dark** (`{colors.focus-on-dark}` — `#ffffff`): the counterpart ring for the two surfaces the blue ring cannot clear — the PlayStation Blue band itself (`{colors.primary}`, where blue-on-blue is 1.00:1) and any control whose own fill is blue or commerce orange. 21.00:1 on `{colors.canvas-dark}` and 4.95:1 on `{colors.primary}`.

### Text
- **Ink** (`{colors.ink}` — `#000000`): primary text on `{colors.canvas-light}`. Headlines, button text, support body.
- **Ink Deep** (`{colors.ink-deep}` — `#121314`): warmer near-black for in-card titles on dark surfaces and deep-shadow gradients.
- **Ink Elevated** (`{colors.ink-elevated}` — `#181818`): the lightest of the dark-canvas inks, used for elevated card backgrounds.
- **Body Light** (`{colors.body-light}` — `rgba(0,0,0,0.6)`): translucent body text on light canvas — the system's default paragraph color.
- **Mute Light** (`{colors.mute-light}` — `#6b6b6b`): metadata text and footer link captions on light canvas.
- **Ash Light** (`{colors.ash-light}` — `#cccccc`): disabled-state text and lowest-emphasis utility on light surfaces.
- **On Dark** (`{colors.on-dark}` — `#ffffff`): primary text on `{colors.canvas-dark}` — headlines, button text on dark hero bands.
- **Body Dark** (`{colors.body-dark}` — `rgba(255,255,255,0.7)`): translucent body text on dark canvas.
- **On Dark Mute** (`{colors.on-dark-mute}` — `#cccccc`): secondary text and disabled state on dark surfaces.
- **Mute Dark** (`{colors.mute-dark}` — `rgba(229,229,229,0.55)`): captions and metadata on dark canvas.

### Semantic
- **Warning** (`{colors.warning}` — `#c81b3a`): validation errors and destructive confirmation copy.
- **Link Light** (`{colors.link-light}` — `#0064b7`): inline body-prose anchor link on light canvas — same hex as `{colors.primary-pressed}`.
- **Link Dark** (`{colors.link-dark}` — `#53b1ff`): inline body-prose anchor link on dark canvas — a brightened blue for dark-mode legibility.

### Brand Gradient
- **PlayStation Plus Gold Gradient** — a horizontal three-stop gold gradient `{colors.ps-plus-gold-start}` (`#ffce21`) → `{colors.ps-plus-gold-mid}` (`#f5a623`) → `{colors.ps-plus-gold-end}` (`#ee8e00`) that anchors the PS Plus banner on the home page. The only gradient in the system; reserved exclusively for PS Plus chrome.

## Typography

### Font Family
- **PlayStation SST** is the proprietary brand sans-serif used across every text role on the site. It carries weights 300 (light), 400 (regular), 500 (medium), 600 (semibold), and 700 (bold), and falls back through `sst` → `Arial` → `Helvetica`. The brand's distinctive choice is using **weight 300 (light) for display headlines** — unusual for a gaming brand and the source of the system's editorial, airy character.
- **SST** appears as a secondary cut for in-product surfaces, falling back to Helvetica → Arial.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 54px | 300 | 1.25 | -0.1px | Hero headline ("Discover all PS5 consoles and accessories") |
| `{typography.display-lg}` | 44px | 300 | 1.25 | 0.1px | Section headline ("Great PS4 & PS5 games out now or coming soon") |
| `{typography.display-md}` | 35px | 300 | 1.25 | 0 | Mid-section headline, game-page sub-hero |
| `{typography.heading-xl}` | 28px | 300 | 1.25 | 0.1px | "30 Years of PlayStation" callout, in-band sub-heading |
| `{typography.heading-lg}` | 22px | 300 | 1.25 | 0.1px | News card title, support category title |
| `{typography.heading-md}` | 18px | 600 | 1 | 0 | Card label, navigation menu heading, in-product strong title |
| `{typography.body-md}` | 18px | 400 | 1.5 | 0.1px | Body copy, paragraph text, support article body |
| `{typography.body-strong}` | 18px | 500 | 1.25 | 0.4px | Inline emphasis, primary nav link, button label (large) |
| `{typography.body-sm}` | 16px | 400 | 1.5 | 0 | Card description, secondary body |
| `{typography.caption-md}` | 14px | 400 | 1.5 | 0 | Footer link, metadata, sub-nav text |
| `{typography.caption-sm}` | 12px | 500 | 1.5 | 0 | Smallest utility text, badge label |
| `{typography.link-md}` | 18px | 400 | 1.5 | 0 | Inline body-prose anchor link |
| `{typography.button-lg}` | 18px | 700 | 1.25 | 0.45px | Primary CTA pill |
| `{typography.button-md}` | 14px | 700 | 1.25 | 0.324px | Compact pill, filter chip, secondary CTA |

### Principles
The hierarchy works on a 1.25-line-height ladder almost exclusively — even body sits at 1.5 instead of the typical 1.6 — which keeps long-form support pages tight and console showcases efficient. The weight contrast between display (300) and button (700) is dramatic: a single 18px chrome line might host a heavyweight CTA next to a feather-light 22px headline, giving the system its editorial gaming-magazine feel.

### Note on Font Substitutes
PlayStation SST is proprietary. The closest open-source substitutes:
- **Roboto Light (300)** for the display tier — its slightly looser letter-spacing matches SST's display optical fit.
- **Inter** at weights 400/500/600 for body and chrome — the closest geometric sans match for SST's body cut.
- **Source Sans Pro Light (300)** as an alternative for the display tier when Roboto reads too utilitarian.

When substituting, preserve the +0.1px to +0.45px tracking on display and button tiers — the spacing is part of what makes PlayStation SST feel premium at the light weight.

## Layout

### Spacing System
- **Base unit:** 8px (with finer 4/12px steps for tight inline gaps).
- **Tokens (front matter):** `{spacing.xxs}` (4px) · `{spacing.xs}` (8px) · `{spacing.sm}` (12px) · `{spacing.md}` (16px) · `{spacing.lg}` (24px) · `{spacing.xl}` (32px) · `{spacing.xxl}` (48px) · `{spacing.section}` (96px).
- **Universal section rhythm:** every page in the set uses `{spacing.section}` (96px) as the vertical gap between major content blocks. Card grids use `{spacing.lg}` (24px) gutters; in-card padding sits at `{spacing.lg}` to `{spacing.xl}` depending on density.
- **Hero band padding:** 96px vertical / 48px horizontal — the largest spacing in the system, reserved for full-bleed surface chapters.

### Grid & Container
- **Max width:** ~1280px content area for body text on desktop with 24px gutters that expand to ~48px at ultrawide. Hero bands and game-tile rails go full-bleed with no max-width constraint on imagery.
- **Game tile carousel:** 4-up at desktop with horizontal scroll on the same row, collapsing to 3-up at 1024px and 2-up at 768px. Each tile uses 16:9 cover art at `{rounded.md}`.
- **Console showcase grid:** desktop 5-column thumbnail strip below the main hero render, collapsing to 3-up + horizontal scroll at tablet.
- **Support page:** desktop 2-column 30/70 split (sidebar nav + article body), collapsing to single-column with the sidebar promoted to a top accordion at mobile.
- **News strip:** 3-up card grid at desktop, 2-up at tablet, 1-up at mobile.

### Whitespace Philosophy
Whitespace is structural and band-defined. The 96px `{spacing.section}` between chapters reads as silence between trailer cuts — there's no decorative wash, no gradient transition, no mid-section divider. Inside a section, content is left-aligned in a tight column with the imagery breathing in the right 60-70% of the band. Paragraph text is comfortable at 1.5 line-height but column widths stay narrow (~520px at desktop) to keep long-form copy readable.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Default for hero bands, footer, full-bleed sections — the dominant treatment |
| 1 — Hairline divider | 1px solid `{colors.hairline-light}` or `{colors.hairline-dark}` | Card borders, support row dividers, footer column rules |
| 2 — Soft active shadow | `0 4px 12px rgba(0,0,0,0.16)` | Active/pressed CTAs, lifted product card |
| 3 — Section gradient | Soft top-to-bottom darkening from `{colors.surface-dark-elevated}` to `{colors.canvas-dark}` | "ON PLAYSTATION" band — only place a gradient appears on chrome |

The system has effectively no resting shadow on cards; depth is built from surface-color contrast across band chapters. Cards lift only on press.

### Decorative Depth
Depth comes from the alternating-band rhythm and from the imagery itself:
- **Console product photography** — DualSense controller and PS5 console renders shot on neutral white with crisp edge lighting, full-bleed inside the light-canvas band.
- **Game key art** — full-bleed cinematic stills (Marathon, the latest blockbuster releases) inside dark-canvas bands with title lockup overlaid in the lower-left.
- **PS Plus tier banner** — a subtle horizontal gold gradient (`{colors.ps-plus-gold-start}` → `{colors.ps-plus-gold-end}`) sits as the only chrome gradient in the system, anchoring the "Discover PlayStation Plus" CTA.
- **"ON PLAYSTATION" gradient band** — top-to-bottom deepening from `{colors.surface-dark-elevated}` (`#121314`) to `{colors.canvas-dark}` (`#000000`) creates a cinematic dimming effect under the anniversary callout.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Hero bands, primary nav, footer, sub-nav, support article body — every full-bleed structural surface |
| `{rounded.sm}` | 4px | Text inputs, support search field utilities |
| `{rounded.md}` | 8px | Game tiles, product cards, feature cards, PS Plus banner |
| `{rounded.lg}` | 16px | Rare large container with extra-soft corners (e.g., dialog cards) |
| `{rounded.full}` | 9999px | Every CTA pill (primary / commerce / secondary), filter chips, pagination dots, carousel paddles |

The radius vocabulary works on a 4 / 8 / pill rhythm for chrome with structural surfaces staying flat at 0px.

### Photography Geometry
- **Hero console render:** large centered console + DualSense composition on white, ~70% width of the band, with copy slot to the left.
- **Game tiles:** 16:9 key art at `{rounded.md}` (8px), 4-up rail at desktop with horizontal carousel.
- **Marathon game page hero:** full-bleed cinematic 16:9 still with the "MARATHON" wordmark in the lower-left at light weight, brand yellow `{colors.marathon-yellow}` accent on a few small UI tags.
- **News card thumbnails:** 16:9 imagery at `{rounded.md}` with a small text block below.
- **Avatar / brand icons:** 32–40px circles for sub-nav social row.

## Components

> **Extracted states:** default and active/pressed (plus disabled for buttons). The live pages document no hover state, per system policy. The state matrix below fills the remaining states as **prescribed** values consistent with the system's own vocabulary — they were not observed on the captured pages.

### State matrix

Legend: ✓ extracted from the captured pages · ◻ prescribed · — genuinely not applicable.

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | ✓ | ◻ opacity 0.88, no travel | ◻ 2px `{colors.focus}` ring, 2px offset | ✓ `{colors.primary-pressed}`, then `{colors.primary-active}` | ✓ `{component.button-disabled}` | ◻ label swaps for a spinner, pill width frozen | — | — |
| `button-commerce` | ✓ | ◻ opacity 0.88 | ◻ 2px `{colors.focus-on-dark}` ring (the orange fill defeats the blue ring) | ✓ `{colors.commerce-pressed}` | ◻ `{component.button-disabled}` | ◻ spinner in place of the label | — | — |
| `button-secondary-light` | ✓ | ◻ border steps to `{colors.mute-light}` | ◻ 2px `{colors.focus}` ring | ✓ border steps to `{colors.ink}` | ◻ `{colors.ash-light}` text and border | — | — | — |
| `button-secondary-dark` | ✓ | ◻ border steps to `{colors.on-dark-mute}` | ◻ 2px `{colors.focus-on-dark}` ring | ✓ border steps to `{colors.on-dark}` | ◻ `{colors.mute-dark}` text and border | — | — | — |
| `text-input` | ✓ | ◻ border steps to `{colors.mute-light}` | ✓ 2px `{colors.primary}` border, plus a prescribed 2px `{colors.focus}` ring at 2px offset | — | ◻ `{colors.surface-soft}` fill, `{colors.ash-light}` text | — | — | ◻ 2px `{colors.warning}` border with a `{typography.caption-md}` message in `{colors.warning}` |
| `filter-pill` | ✓ | ◻ fill lifts toward `{colors.canvas-light}` | ◻ 2px `{colors.focus}` ring | ◻ fill at `{colors.surface-soft}` | — | — | ✓ `{component.filter-pill-active}` — opaque `{colors.canvas-light}` fill | — |
| `game-tile` | ✓ | ◻ scale 1.02 on the art only, copy static | ◻ 2px `{colors.focus-on-dark}` ring, 2px offset | ◻ scale 0.99 | — | ◻ `{colors.surface-dark-elevated}` placeholder block, no shimmer | ◻ 2px `{colors.focus-on-dark}` inner border | — |
| `product-card` / `product-card-dark` / `feature-card` | ✓ | ◻ no visual change; the card is not interactive unless it wraps a link | ◻ ring on the wrapped link, not the card | ✓ level-2 soft shadow (`0 4px 12px rgba(0,0,0,0.16)`) | — | ◻ skeleton block at `{colors.surface-soft}` / `{colors.surface-dark-card}` | — | — |
| `carousel-paddle` | ✓ | ◻ scrim rises to `rgba(255,255,255,0.28)` | ◻ 2px `{colors.focus-on-dark}` ring | ◻ scale 0.96 | ◻ opacity 0.4 at the end of the rail | — | — | — |
| `pagination-dot` | ✓ | ◻ fill lifts to `{colors.on-dark-mute}` | ◻ 2px `{colors.focus-on-dark}` ring | — | — | — | ✓ `{component.pagination-dot-active}` | — |
| `support-row` | ✓ | ◻ chevron travels 4px right, row ink unchanged | ◻ 2px `{colors.focus}` ring inset to the row box | ◻ ink drops to `{colors.body-light}` | — | — | — | — |
| `link-inline` | ✓ | ◻ underline appears, colour held | ◻ 2px `{colors.focus}` ring (light canvas) / `{colors.focus-on-dark}` (dark canvas) | ◻ colour drops to `{colors.primary-active}` | — | — | — | — |
| `badge-info` | ✓ | — | — | — | — | — | — | — |
| `primary-nav` / `sub-nav` | ✓ | ◻ item ink lifts to `{colors.on-dark}` from `{colors.body-dark}` | ◻ 2px `{colors.focus-on-dark}` ring | ◻ ink held, no travel | — | — | ◻ 2px `{colors.on-dark}` underline on the current section | — |

`badge-info` is genuinely a two-state element: it is a static label overlaid on a tile and has only default and the absent/present distinction. `hero-band-*` and `footer-section` are surfaces, not controls, and carry no states at all.

### Buttons

**`button-primary`** — the universal PlayStation CTA
- Background `{colors.primary}` (PlayStation Blue), text `{colors.on-primary}`, type `{typography.button-lg}`, padding `12px 28px`, height ~48px, rounded `{rounded.full}`.
- Used for "Add to bag", "Sign up", "Learn more", "Subscribe" — every primary action across both light and dark canvases.
- Pressed state lives in `button-primary-pressed` — background drops to `{colors.primary-pressed}` (`#0064b7`).

**`button-commerce`** — orange store CTA
- Background `{colors.commerce}` (`#d53b00`), text `{colors.on-commerce}`, type `{typography.button-lg}`, padding `12px 28px`, height ~48px, rounded `{rounded.full}`.
- Reserved for "Buy now", "Pre-order", "Add to cart" — store actions only. The only warm color in the system.
- Pressed state lives in `button-commerce-pressed` — background drops to `{colors.commerce-pressed}`.

**`button-secondary-light`** — outline variant on light canvas
- Background transparent, text `{colors.ink}`, 1px solid `{colors.ash-light}` border, type `{typography.button-lg}`, padding `12px 28px`, height ~48px, rounded `{rounded.full}`.
- Lower-emphasis CTA on white surfaces ("Learn more →", "Watch trailer").

**`button-secondary-dark`** — outline variant on dark canvas
- Background transparent, text `{colors.on-dark}`, 1px solid `{colors.hairline-dark}`, type `{typography.button-lg}`, padding `12px 28px`, height ~48px, rounded `{rounded.full}`.
- Same role as the light variant but inverted for use on `{colors.canvas-dark}` hero bands.

**`button-disabled`**
- Background `{colors.surface-soft}`, text `{colors.ash-light}`, rounded `{rounded.full}` — flat soft gray.

### Filter & Tab Chips

**`filter-pill`** + **`filter-pill-active`**
- Default: background `{colors.surface-filter}` (translucent), text `{colors.ink}`, type `{typography.button-md}`, padding `8px 16px`, rounded `{rounded.full}`.
- Active: background flips to `{colors.canvas-light}` (opaque white) — the chip "lifts" from the translucent default.
- Used in the PS5 games filter strip ("All", "Coming Soon", "PlayStation VR2", "Recently Released").

### Inputs & Forms

**`text-input`** + **`text-input-focused`**
- Default: background `{colors.canvas-light}`, text `{colors.ink}`, 1px solid `{colors.ash-light}`, type `{typography.body-md}`, padding `12px 16px`, height ~48px, rounded `{rounded.sm}` (4px).
- Focused: 2px solid `{colors.primary}` border, no halo (relies on the border weight increase as the focus signal).

**`support-search-bar`** — the support-page signature search field
- Background `{colors.canvas-light}`, text `{colors.ink}`, type `{typography.body-md}`, padding `12px 24px`, height ~56px, rounded `{rounded.full}`.
- Sits at the top of the support page hero with a magnifier icon at the left edge and "Search the support center" placeholder.

### Cards & Containers

**`product-card`** — light-canvas product/feature card
- Container: background `{colors.surface-card}` (`#f5f7fa` cool-blue-tinted), 1px solid `{colors.hairline-light}` (rare; usually borderless), padding `{spacing.lg}` (24px), rounded `{rounded.md}` (8px).
- Used for the "PlayStation Store" sale callout, news cards, and PS Plus tier comparison cards on light canvas.

**`product-card-dark`** — dark-canvas product card
- Container: background `{colors.surface-dark-card}` (`#181818`), padding `{spacing.lg}`, rounded `{rounded.md}`.
- Used for game-detail cards and dark-canvas feature panels.

**`game-tile`** — game/console thumbnail tile
- Container: background `{colors.surface-dark-elevated}`, padding 0, rounded `{rounded.md}`.
- Layout: 16:9 cover art at full bleed inside the radius, with title + platform tag overlaid at the bottom-left in `{typography.body-sm}`.
- Used in the "Great PS4 & PS5 games" rail and the PS5 games listing grid.

**`feature-card`** — light-canvas marketing card
- Container: background `{colors.canvas-light}`, padding `{spacing.xl}` (32px), rounded `{rounded.md}`.
- Used for the "PlayStation Store" hero card and similar feature panels with a small product icon, title, body, and CTA.

**`hero-band-blue`** — the PlayStation Blue full-bleed band
- Background `{colors.primary}`, text `{colors.on-primary}` in `{typography.display-md}`, padding `96px 48px`, rounded `{rounded.none}`.
- The Marathon launch CTA strip and the footer surface use this band. The band's defining purpose is "this is the action moment of the page."

**`hero-band-dark`** — full-bleed dark hero
- Background `{colors.canvas-dark}` (with optional gradient end at `{colors.surface-dark-elevated}`), text `{colors.on-dark}` in `{typography.display-xl}`, padding `96px 48px`, rounded `{rounded.none}`.
- The home-page hero, the game-detail page hero, and the "ON PLAYSTATION" anniversary band.

**`hero-band-light`** — full-bleed white hero
- Background `{colors.canvas-light}`, text `{colors.ink}` in `{typography.display-xl}`, padding `96px 48px`, rounded `{rounded.none}`.
- The console showcase band ("Discover all PS5 consoles and accessories") and the support page top.

**`ps-plus-banner`** — PlayStation Plus tier callout
- Background `{colors.surface-dark-elevated}` with the `{colors.ps-plus-gold-start}` → `{colors.ps-plus-gold-end}` gold gradient as a horizontal accent bar across the top, text `{colors.on-dark}` in `{typography.heading-xl}`, padding `48px 32px`, rounded `{rounded.md}`.
- The "Discover PlayStation Plus" full-width banner on the home page.

**`carousel-paddle`** — circular carousel control
- Background `rgba(255,255,255,0.16)`, icon `{colors.on-dark}`, rounded `{rounded.full}`, size 48px.
- Anchored to the left/right edge of the game tile carousel.

**`pagination-dot`** + **`pagination-dot-active`**
- 8px circle at `{rounded.full}`. Default fill `{colors.ash-dark}`; active fill `{colors.on-dark}`.
- Carousel position indicator below the game tile rail.

### Inline

**`badge-info`** — small info tag
- Background `{colors.primary}`, text `{colors.on-primary}` in `{typography.caption-sm}`, padding `4px 10px`, rounded `{rounded.full}`.
- "New", "Pre-order", "Coming Soon" labels overlaid on game tiles.

**`link-inline`** — body-prose anchor link
- `{colors.link-light}` text on light canvas / `{colors.link-dark}` on dark canvas, no underline by default. Inline body links inside support article paragraphs.

### Navigation

**`primary-nav`**
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, height ~48px, type `{typography.body-strong}`, rounded `{rounded.none}`.
- Layout (desktop): PlayStation P-logo at far-left, centered nav row ("Games · PS5 · PS4 · PS VR2 · Subscriptions · Hardware · Mobile · News · Shop · Support"), right cluster (search-glyph + locale + cart icon + user-avatar circle).

**`sub-nav`** — secondary nav strip
- Background `{colors.canvas-dark}`, text `{colors.on-dark}` in `{typography.caption-md}`, height ~40px, rounded `{rounded.none}`.
- Sits directly below the primary nav on PS5 games / single game / PS Plus pages with section-specific anchor links.

**Top Nav (Mobile)**
- Hamburger menu icon at left, P-logo at center, search + cart icons at right. Primary nav collapses into a full-screen dark drawer that slides from the left.

### Footer

**`footer-section`**
- Background `{colors.primary}` (PlayStation Blue), text `{colors.on-primary}` in `{typography.caption-md}`, padding `{spacing.xxl}` (48px) vertical.
- Layout: large PlayStation wordmark at top-left, multi-column link grid (locale selector, store links, account, support, social), bottom row with terms / privacy fine-print in `{typography.caption-sm}`.
- The footer's blue surface is the system's "we're done — return to the brand" anchor.

### Support-page-specific

**`support-row`** — support article-list row
- Background `{colors.canvas-light}`, text `{colors.ink}` in `{typography.body-md}`, padding `16px 0`, with a 1px `{colors.hairline-light}` bottom rule.
- Used for FAQ / category-listing rows on the support page with a small chevron-right icon at the right edge.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or easing curve below was extracted from PlayStation's pages; the values are the shared **Cinematic** profile, assigned because this is a gaming-console identity whose pages are built from full-bleed console photography and key art with sparse weight-300 type — the slow-reveal signature the profile describes. Every value resolves to a `{motion.*}` token so that files sharing the profile stay comparable.

Only `transform` and `opacity` are animated. Never `width`, `height`, `top`, `left` or `margin` — band chapters are full-bleed, so a layout-triggering transition would reflow the whole page.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, tile, paddle) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`; `transform: scale()` on `{component.game-tile}` art only | Opacity only at `{motion.duration-reduced}`; scale removed |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)`, `opacity` | Scale removed; opacity at `{motion.duration-reduced}` |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the 2px `{colors.focus}` / `{colors.focus-on-dark}` ring | Ring appears instantly, no fade — focus must never be delayed |
| Page / route transition (band chapter) | `{motion.duration-emphasis}` in, `{motion.duration-slow}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`; `transform: translateY(16px)` on the copy slot, `transform: scale(1.04 → 1)` on the hero image | Opacity cross-fade only at `{motion.duration-reduced}`; no travel, no scale |
| Modal / drawer (mobile nav drawer) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `transform: translateX(-100% → 0)`, scrim `opacity` | Drawer and scrim fade at `{motion.duration-reduced}`; no slide |
| Dropdown (locale picker, mobile sub-nav select) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: translateY(-4px → 0)` | Opacity only at `{motion.duration-reduced}` |
| Toast / "Action Required" banner | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: translateY(8px → 0)` | Opacity only at `{motion.duration-reduced}` |
| List enter (game-tile rail, news strip) | `{motion.duration-slow}` per item, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity`, `transform: translateY(24px → 0)` | All stagger and travel removed; the full set fades in once at `{motion.duration-reduced}` |
| List exit (filter change on the PS5 games grid) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Opacity only at `{motion.duration-reduced}` |
| Loading (tile skeleton, search spinner) | `{motion.duration-emphasis}` loop | `{motion.ease-standard}` | `opacity` pulse 0.4 → 1 on the skeleton block; `transform: rotate()` on the spinner | Loop frozen; skeleton holds a static `{colors.surface-soft}` / `{colors.surface-dark-card}` fill and the spinner is replaced by static text |

Exit is shorter than its matching entrance in every row. Nothing animates on first paint in a way that delays content: the hero band's copy and image are painted, then settle; the reveal never gates the text. The only looping animation in the system is the loader. The one piece of deliberate brand ambience — the slow `transform: scale(1.04 → 1)` settle on a full-bleed hero image as its chapter enters the viewport — is stated as ambience here and is frozen under reduced motion.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translate), all scale, the hero-image settle,
     every stagger, and the loader loop (which freezes on a static fill). */
  /* Kept: opacity fades only, clamped to {motion.duration-reduced} = 150ms,
     whatever the Cinematic profile's own durations say. The focus ring
     still appears instantly. */
  *, *::before, *::after {
    transition-duration: 150ms !important;   /* {motion.duration-reduced} */
    transition-property: opacity !important;
    animation-duration: 150ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

## Accessibility

All ratios below are computed with WCAG 2.1 relative luminance from this file's own token values. Translucent tokens are composited over the surface they are drawn on, and that ground is named.

### Measured contrast — key pairs

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas-light}` | 21.00:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.surface-soft}` | 18.93:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.surface-card}` | 19.57:1 | 4.5:1 | pass |
| `{colors.body-light}` (composited `#666666` on white) on `{colors.canvas-light}` | 5.74:1 | 4.5:1 | pass |
| `{colors.mute-light}` on `{colors.canvas-light}` | 5.33:1 | 4.5:1 | pass |
| `{colors.mute-light}` on `{colors.surface-soft}` | 4.80:1 | 4.5:1 | pass |
| `{colors.on-dark}` on `{colors.canvas-dark}` | 21.00:1 | 4.5:1 | pass |
| `{colors.on-dark-mute}` on `{colors.canvas-dark}` | 13.08:1 | 4.5:1 | pass |
| `{colors.mute-dark}` (composited `#7e7e7e` on black) on `{colors.canvas-dark}` | 5.17:1 | 4.5:1 | pass |
| `{colors.on-primary}` on `{colors.primary}` | 4.95:1 | 4.5:1 | pass |
| `{colors.on-commerce}` on `{colors.commerce}` | 4.71:1 | 4.5:1 | pass |
| `{colors.link-light}` on `{colors.canvas-light}` | 5.99:1 | 4.5:1 | pass |
| `{colors.link-dark}` on `{colors.canvas-dark}` | 9.10:1 | 4.5:1 | pass |
| `{colors.warning}` on `{colors.canvas-light}` | 5.72:1 | 4.5:1 | pass |
| `{colors.focus}` on `{colors.canvas-light}` | 4.95:1 | 3.0:1 | pass |
| `{colors.focus-on-dark}` on `{colors.canvas-dark}` | 21.00:1 | 3.0:1 | pass |

### Real failures, stated plainly

PlayStation's extracted utility greys do not meet WCAG. These are the brand's real values and are not altered here:

- **`{colors.hairline-light}` (`#f3f3f3`) on `{colors.canvas-light}` measures 1.11:1**, against the 3.0:1 that WCAG 1.4.11 asks of a meaningful boundary. The real brand fails here. It is scoped to decorative dividers in the Colors section, and `{colors.mute-light}` (5.33:1) is prescribed for any boundary that carries meaning.
- **`{colors.hairline-light}` on `{colors.surface-soft}` measures 1.00:1** — the two tokens are the same hex, so a card at `{colors.surface-soft}` with a hairline border has no visible edge at all. Same scoping applies.
- **`{colors.hairline-dark}` composites to `#2e2e2e` over `{colors.canvas-dark}` and measures 1.55:1.** Decorative only, same restriction.
- **`{colors.ash-light}` (`#cccccc`) on `{colors.canvas-light}` measures 1.61:1.** The live `{component.text-input}` and `{component.button-secondary-light}` use this as their 1px border, so the real input boundary fails 1.4.11. Prescribed replacement: `{colors.mute-light}`.
- **`{component.carousel-paddle}` is reported at 1.0:1.** That number measures the white icon against `{colors.canvas-light}`, which is not where the paddle is drawn: its `rgba(255,255,255,0.16)` scrim sits over dark key art, compositing to `#292929` over `{colors.canvas-dark}`, where the `{colors.on-dark}` icon measures **14.55:1**. Over `{colors.surface-dark-card}` the scrim composites to `#3d3d3d` and the icon measures 10.86:1. The paddle passes in situ; the 1.0:1 figure is an artefact of compositing a translucent fill against the default canvas.
- **`{colors.ash-dark}` composites to `#2e2e2e` over `{colors.canvas-dark}` and measures 1.55:1.** It is the default `{component.pagination-dot}` fill — a non-text indicator whose active counterpart is `{colors.on-dark}` at 21.00:1, so position is still conveyed, but the inactive dots are below 3:1.

### Focus ring visibility, per surface

The ring is 2px solid with a 2px offset **outside** the control, so it is measured against the surface behind the control rather than the control's own fill.

| Surface | Ring | Ratio |
|---|---|---|
| `{colors.canvas-light}` | `{colors.focus}` | 4.95:1 |
| `{colors.surface-soft}` | `{colors.focus}` | 4.47:1 |
| `{colors.surface-card}` | `{colors.focus}` | 4.62:1 |
| `{colors.surface-filter}` (composited `#fbfcfd`) | `{colors.focus}` | 4.82:1 |
| `{colors.canvas-dark}` | `{colors.focus-on-dark}` | 21.00:1 |
| `{colors.surface-dark-elevated}` | `{colors.focus-on-dark}` | 18.60:1 |
| `{colors.surface-dark-card}` | `{colors.focus-on-dark}` | 17.76:1 |
| `{colors.primary}` band (footer, Marathon CTA strip) | `{colors.focus-on-dark}` | 4.95:1 |
| `{colors.commerce}` fill | `{colors.focus-on-dark}` | 4.71:1 |

Blue-on-blue is 1.00:1, which is why the blue band and any blue or orange fill take `{colors.focus-on-dark}` instead. Over full-bleed key art, which has no measurable colour, draw `{colors.focus-on-dark}` with a 1px `{colors.ink}` outer edge so the ring survives a light frame.

### Tap targets

Stated from the heights this file documents, not from a rendered page: `{component.button-primary}` and `{component.button-commerce}` at 48px, `{component.text-input}` at 48px, `{component.support-search-bar}` at 56px, `{component.carousel-paddle}` at 48×48. `{component.filter-pill}` is the one at risk — its `8px 16px` padding on `{typography.button-md}` (14px) yields roughly 36px, below the 44px minimum, and it needs added inline padding to reach it. `{component.pagination-dot}` is an 8px dot and needs a 44px transparent hit area. Neither can be confirmed without a rendered page.

### Reduced motion

Every motion value in this file is prescribed, and under `@media (prefers-reduced-motion: reduce)` all travel, scale, stagger and the hero-image settle are removed; opacity fades remain, clamped to `{motion.duration-reduced}` (150ms); the loader loop freezes to a static fill. The focus ring is exempt from any fade and appears instantly.

### Known accessibility gaps

- No `aria` or keyboard-order evidence was captured; nothing here claims a tested keyboard path.
- `{component.text-input-focused}` signals focus with border weight alone on the live site. A weight change is not a 3:1 indicator on its own, which is why the prescribed ring is added alongside it.
- Overlap, clipping, reflow and real tap-target size need a rendered page and are not measured anywhere in this document.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (PlayStation Blue) for primary CTAs and the footer surface only. The blue band is precious — at most one full-bleed blue band per page.
- Reserve `{colors.commerce}` (orange) for store/buy/pre-order CTAs only. It is never used on marketing chrome or hero pills.
- Use PlayStation SST at weight 300 for display headings (54 / 44 / 35 / 28 / 22). The light weight is the brand voice.
- Stack content sections at `{spacing.section}` (96px) rhythm with the next band's surface color taking over the page edge-to-edge — no decorative dividers between bands.
- Use `{rounded.full}` (9999px) on every CTA pill and `{rounded.md}` (8px) on every product card. The two-radius vocabulary is the entire shape system aside from inputs.
- Pair full-bleed game key art and console renders inside dark or light bands; let imagery occupy 60-90% of the band's vertical height.
- Use `{component.ps-plus-banner}` with the gold gradient exclusively for the PlayStation Plus tier callout — never decorate other components with the gold.

### Don't
- Don't introduce drop shadows on resting cards. The system is flat-on-canvas; cards lift only on press.
- Don't replace `{colors.primary}` with another shade of blue. The brand blue is precise — `#0070d1` for default and `#0064b7` for pressed.
- Don't use `{colors.commerce}` (orange) on marketing/hero CTAs. It's reserved exclusively for store actions.
- Don't introduce a sans-serif body font, italic, or monospace style. PlayStation SST carries every text role.
- Don't soften pill geometry. CTAs are always `{rounded.full}` — no medium-radius buttons.
- Don't use the gold PS Plus gradient on anything that isn't the PS Plus banner. It is a tier-specific brand asset.
- Don't put a gradient on chrome. The only allowed gradient is the gold PS Plus accent and the soft top-to-bottom darkening of the "ON PLAYSTATION" band.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| ultrawide | 1920px+ | Hero band stays at content max-width 1280px; outer gutters grow to ~80px |
| desktop-large | 1440px | Default desktop — 4-up game tile carousel, full primary nav |
| desktop | 1280px | Same layout with narrower outer gutters |
| desktop-small | 1024px | Game tile rail collapses to 3-up; sub-nav remains horizontal |
| tablet | 768px | Game tiles → 2-up; primary nav becomes hamburger drawer |
| mobile | 480px | Single-column everything; hero `{typography.display-xl}` scales 54px → ~32px |
| mobile-narrow | 320px | Section padding tightens to 32px; hero further scales to ~28px |

### Touch Targets
All interactive elements meet WCAG AAA (≥ 44×44px). `{component.button-primary}` and `{component.button-commerce}` sit at 48px height with 28px horizontal padding (effective ~48×100px tappable). `{component.text-input}` sits at 48px. `{component.support-search-bar}` sits at 56px. `{component.filter-pill}` is ~36–40px height with 16px padding extending to 44px tappable via inline padding. `{component.carousel-paddle}` is exactly 48×48 circular.

### Collapsing Strategy
- **Primary nav:** desktop horizontal cluster → tablet hamburger drawer at 768px. The right-cluster icons (search, cart, account) stay visible at every breakpoint.
- **Sub-nav:** desktop horizontal anchor row → tablet horizontal scroll → mobile select dropdown.
- **Game tile carousel:** 4-up → 3-up → 2-up at 1024 and 768px; carousel paddles stay visible at every desktop breakpoint, hide on mobile in favor of touch-swipe.
- **Hero bands:** stay full-bleed at every breakpoint; only the internal content column reflows from 2-column (text-left + image-right) to single-column (text above image).
- **Console showcase:** desktop 5-up thumbnail strip → tablet 3-up + horizontal scroll → mobile 1-up with paddle.
- **Support page:** desktop 30/70 split (sidebar + body) → tablet sidebar promoted to top accordion → mobile fully collapsed accordion.
- **Section padding:** `{spacing.section}` (96px) desktop → 64px tablet → 48px mobile.
- **Hero headline:** `{typography.display-xl}` (54px) at desktop, scaling 44px / 32px / 28px down the breakpoint stack.

### Image Behavior
- Hero imagery (console renders, game key art) uses art-direction crops on mobile so the central subject stays centered when the band collapses to single-column.
- Game tile cover art preserves 16:9 ratio at every breakpoint; only the column count changes.
- Console showcase thumbnails maintain their natural aspect (~1:1 product render) across breakpoints.
- All non-critical imagery is lazy-loaded as the user scrolls into the next chapter.

## Iteration Guide

1. Focus on ONE component at a time. Pull its YAML entry and verify every property resolves.
2. Reference component names and tokens directly (`{colors.primary}`, `{component.button-primary-pressed}`, `{rounded.full}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits — `broken-ref`, `contrast-ratio`, and `orphaned-tokens` warnings flag issues automatically.
4. Add new variants as separate component entries (`-pressed`, `-disabled`) — do not bury them inside prose.
5. Default body to `{typography.body-md}` (18px / 400 / 1.5); reach for `{typography.display-xl}` strictly for the page-top hero headline; use `{typography.body-strong}` for primary nav links.
6. Keep `{colors.primary}` scarce per viewport — at most one full-bleed PlayStation Blue band per page.
7. When introducing a new component, ask whether it can be expressed with the existing pill + 8px-radius card + full-bleed-band vocabulary before adding new tokens. The system's strength is that it almost never needs new ones.

## Known Gaps

- **Mobile screenshots not captured** — responsive behavior synthesizes PlayStation's known mobile pattern (hamburger drawer, single-column band reflow, hero downscale) from desktop evidence and the breakpoint stack.
- **Hover states not documented** by system policy. The State matrix in Components marks every hover cell as prescribed (◻), not extracted.
- **Motion is prescribed, not measured.** No duration, easing curve or stagger in this file came from PlayStation's pages; the `{motion.duration-base}` ladder is the shared Cinematic profile.
- **Focus ring is prescribed.** `{colors.focus}` and `{colors.focus-on-dark}` are not extracted values — the captured pages expose only a 2px border-weight change on `{component.text-input-focused}`.
- **Control-boundary colour is prescribed.** The live inputs use `{colors.ash-light}` at 1.61:1; `{colors.mute-light}` is this document's prescribed replacement, not an observed value.
- **Sign-in / authentication chrome** (login modal, account dashboard, profile pages) not in the captured pages.
- **PlayStation Store** in-store browsing surfaces (PDP / cart / checkout) are not in the captured set — those use a more dense data-table layout that this document does not describe.
- **Game-page-specific theming** — the `/marathon/` page uses `{colors.marathon-yellow}` as a chapter accent. Other game pages may pull in their own per-title brand colors that vary outside the documented system.
- **Form validation states** (success / error inline messages) not present in the captured surfaces beyond the `{colors.warning}` color token.
