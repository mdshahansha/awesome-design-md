---
version: alpha
name: Binance-design-analysis
description: A confident financial-platform interface anchored on a deep near-black canvas, where Binance's iconic yellow (#FCD535) carries every primary CTA, brand accent, and value-claim moment. Type runs Binance's custom BinanceNova / BinancePlex stack at modest weights — the system trusts size and yellow voltage over bold weight. Marketing and product surfaces default to the dark theme; transactional surfaces (buy crypto, deposit, exchange) flip to a light theme that shares the same yellow CTAs and gray-blue hairlines. Trading green (up) and red (down) accents thread through both modes for price-direction signals.

colors:
  primary: "#fcd535"
  primary-active: "#f0b90b"
  primary-disabled: "#3a3a1f"
  ink: "#181a20"
  body: "#eaecef"
  body-on-light: "#181a20"
  muted: "#707a8a"
  muted-strong: "#929aa5"
  hairline-on-light: "#eaecef"
  hairline-on-dark: "#2b3139"
  border-strong: "#cdd1d6"
  canvas-light: "#ffffff"
  canvas-dark: "#0b0e11"
  surface-card-dark: "#1e2329"
  surface-elevated-dark: "#2b3139"
  surface-soft-light: "#fafafa"
  surface-strong-light: "#f5f5f5"
  on-primary: "#181a20"
  on-dark: "#ffffff"
  trading-up: "#0ecb81"
  trading-down: "#f6465d"
  accent-turquoise: "#2dbdb6"
  info: "#3b82f6"
  info-ring: "#3b82f6"
  focus: "#1f6feb"
  focus-on-dark: "#3b82f6"
  muted-readable: "#5e6673"
  border-control: "#848e9c"

typography:
  hero-display:
    fontFamily: "BinanceNova, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  number-display:
    fontFamily: "BinancePlex, BinanceNova, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  number-md:
    fontFamily: "BinancePlex, BinanceNova, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  number-sm:
    fontFamily: "BinancePlex, BinanceNova, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px

shadow:
  focus-ring: "0 0 0 2px {colors.focus}"
  focus-ring-on-dark: "0 0 0 2px {colors.focus-on-dark}"
  card-over-image: "0 2px 8px rgba(11, 14, 17, 0.24)"

motion:
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 600ms
  ease-standard: cubic-bezier(0.4, 0, 0.2, 1)
  ease-enter: cubic-bezier(0, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 40ms

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-primary-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 32px
  button-secondary-on-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
  button-secondary-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button}"
  button-trading-up:
    backgroundColor: "{colors.trading-up}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
  button-trading-down:
    backgroundColor: "{colors.trading-down}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
  button-subscribe:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 6px 16px
    height: 28px
  text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  top-nav-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  hero-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.hero-display}"
    padding: 80px
  stat-callout-card:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.number-display}"
  trust-badge:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: 16px 20px
  markets-table-card:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 24px
  markets-row:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.number-md}"
    padding: 12px 0
  price-up-cell:
    backgroundColor: transparent
    textColor: "{colors.trading-up}"
    typography: "{typography.number-md}"
  price-down-cell:
    backgroundColor: transparent
    textColor: "{colors.trading-down}"
    typography: "{typography.number-md}"
  search-input-on-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 10px 16px
    height: 40px
  text-input-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 40px
  funds-safu-band:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.primary}"
    typography: "{typography.display-lg}"
    padding: 80px
  feature-photo-card:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xl}"
  qr-promo-card:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  faq-row:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 20px 0
  cta-band-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.xl}"
    padding: 48px
  arena-hero-gradient:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.primary}"
    typography: "{typography.display-lg}"
    padding: 80px
  cookie-consent-card:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 16px
  buy-crypto-amount-card:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.number-display}"
    rounded: "{rounded.lg}"
    padding: 24px
  steps-card:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: 24px
  price-chart-card:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  conversion-cell:
    backgroundColor: transparent
    textColor: "{colors.body-on-light}"
    typography: "{typography.body-md}"
  trader-row:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    padding: 12px 0
  footer-light:
    backgroundColor: "{colors.surface-soft-light}"
    textColor: "{colors.body-on-light}"
    typography: "{typography.body-md}"
    padding: 64px
---

## Overview

Binance reads like a financial trading platform that wants to feel both authoritative and energetic. The base atmosphere is **deep near-black canvas** (`{colors.canvas-dark}` — #0b0e11) holding white type and a single, ubiquitous accent: **Binance Yellow** (`{colors.primary}` — #FCD535). That yellow does almost all of the brand's heavy lifting — it carries every primary CTA, every value-claim headline ("FUNDS ARE SAFU"), every "Sign Up" pill, every featured tier indicator, and the wordmark itself. There is no secondary brand color. The system trusts the yellow voltage to do the brand work, and it carries it.

Type runs Binance's custom **BinanceNova** (display + body) and **BinancePlex** (numerical / financial display) stack. BinanceNova carries display headlines, section titles, and body copy. BinancePlex appears on price tickers, large stat numbers (transaction volumes, user counts, prize pools) — anywhere a number wants to feel "tabular and reliable." Both run at modest weights — display sizes use weight 600-700 (bolder than typical marketing because trading platforms need numbers to read at a glance), body stays at 400.

The product is **multi-theme**: marketing surfaces (homepage, smart-money, futures arena) default to dark, while transactional surfaces (buy crypto, deposit, withdraw) flip to a light theme. The same yellow CTAs and gray-blue hairlines (`{colors.hairline-on-light}` — #eaecef) thread through both — only canvas, surface, and text tones flip. Trading **green** (`{colors.trading-up}` — #0ecb81) and **red** (`{colors.trading-down}` — #f6465d) signal price direction in tables, charts, and price tickers across both modes.

**Key Characteristics:**
- Single accent color: `{colors.primary}` (#FCD535) does all brand voltage — primary CTAs, hero headlines, brand mark, badges. Used scarcely on dark for emphasis, ubiquitously on transactional dialogs.
- Custom type stack: `BinanceNova` (display + body) and `BinancePlex` (numbers, prices, financial data). Big stat numbers always render in BinancePlex for tabular consistency.
- Multi-theme: marketing pages default dark (`{colors.canvas-dark}`); transactional pages flip light (`{colors.canvas-light}`). Yellow CTAs and trading green/red are shared across both.
- Light footer on dark body: the homepage uses `{colors.surface-soft-light}` (#fafafa) for the footer even when the body above it is dark — a deliberate inversion that visually closes the page.
- Trading semantics: green up / red down (`{colors.trading-up}` / `{colors.trading-down}`) for price changes, applied as text color rather than badge background.
- Card surfaces: `{colors.surface-card-dark}` (#1e2329) for elevated cards on dark; `{colors.canvas-light}` for cards on light. No gradient surfaces, no atmospheric backdrops — flat color blocks throughout.
- Border radius is small to medium: `{rounded.md}` (6px) for primary buttons, `{rounded.lg}` (8px) for inputs and content cards, `{rounded.xl}` (12px) for elevated card containers, `{rounded.pill}` for prominent feature CTAs.
- Spacing follows a 4-multiple scale; major editorial bands sit at `{spacing.section}` (80px) — slightly tighter than typical marketing-only sites because product pages need denser layouts.

## Colors

### Brand & Accent
- **Binance Yellow** (`{colors.primary}` — #FCD535): The single brand color. Used for primary CTA backgrounds, the wordmark, brand-claim headlines ("FUNDS ARE SAFU"), trust badges ("No.1 Trading Volume"), large stat numbers in `{component.stat-callout-card}`, and inline links.
- **Binance Yellow Active** (`{colors.primary-active}` — #f0b90b): The press / hover-darker variant. Slightly more saturated yellow.
- **Binance Yellow Disabled** (`{colors.primary-disabled}` — #3a3a1f): A desaturated dark-yellow used on disabled CTAs over dark canvas.
- **Accent Turquoise** (`{colors.accent-turquoise}` — #2dbdb6): A small secondary accent used very sparingly on Smart Money's "Check Now" CTA over dark surfaces. Treat as a single-product accent, not a system color.

### Surface

The system has two canvas modes that map to product context:

**Dark mode (marketing default):**
- **Canvas Dark** (`{colors.canvas-dark}` — #0b0e11): The primary page floor. Near-black with a slight warm tint — never pure black.
- **Surface Card Dark** (`{colors.surface-card-dark}` — #1e2329): Cards, navigation dropdowns, secondary buttons over dark canvas, markets table.
- **Surface Elevated Dark** (`{colors.surface-elevated-dark}` — #2b3139): One step lighter, used for nested cards, hovered nav items, and chart background panels.

**Light mode (transactional):**
- **Canvas Light** (`{colors.canvas-light}` — #ffffff): The page floor on transactional pages (buy crypto, deposit forms, account dialogs).
- **Surface Soft Light** (`{colors.surface-soft-light}` — #fafafa): Footer surface and disabled states.
- **Surface Strong Light** (`{colors.surface-strong-light}` — #f5f5f5): Form input backgrounds in muted contexts.

### Hairlines & Borders
- **Hairline on Light** (`{colors.hairline-on-light}` — #eaecef): The 1px border tone on light surfaces. Dembrandt's frequency analysis confirms this as the highest-count token (1022 occurrences) — Binance uses hairlines liberally.
- **Hairline on Dark** (`{colors.hairline-on-dark}` — #2b3139): The 1px border tone on dark surfaces. Same hex as `{colors.surface-elevated-dark}` — borders feel like surface steps, not ink lines.
- **Border Strong** (`{colors.border-strong}` — #cdd1d6): A heavier border tone used on disabled secondary buttons.
- **Border Control** (`{colors.border-control}` — #848e9c) — **prescribed, not extracted.** The two extracted hairlines are decorative-strength only: `{colors.hairline-on-light}` measures 1.18:1 on `{colors.canvas-light}` and `{colors.hairline-on-dark}` measures 1.48:1 on `{colors.canvas-dark}`, both far below the 3:1 a component boundary needs. Binance's real hairlines fail AA as control boundaries. Use the extracted hairlines for table dividers, FAQ separators and card edges — decoration, where no contrast requirement applies — and `{colors.border-control}` wherever a 1px line is the *only* boundary of an interactive control (text inputs, selects, secondary-button outlines). It measures 3.32:1 on `{colors.canvas-light}`, 3.04:1 on `{colors.surface-strong-light}`, 4.77:1 on `{colors.surface-card-dark}` and 5.83:1 on `{colors.canvas-dark}`, so one token serves both themes.

### Text
- **Ink** (`{colors.ink}` — #181a20): The strongest text on light surfaces. Display headlines on transactional pages.
- **Body on Dark** (`{colors.body}` — #eaecef): Default running-text on dark canvas — deliberately not pure white, slightly cooler.
- **Body on Light** (`{colors.body-on-light}` — #181a20): Same as ink — light-mode body text reuses the ink token.
- **Muted** (`{colors.muted}` — #707a8a): Footer links, breadcrumbs, captions, table column headers. Works on both light and dark canvas.
- **Muted Strong** (`{colors.muted-strong}` — #929aa5): A second-tier muted for emphasized labels. On dark surfaces it is the *readable* muted: 6.81:1 on `{colors.canvas-dark}`, 5.56:1 on `{colors.surface-card-dark}`, 4.61:1 on `{colors.surface-elevated-dark}`. On `{colors.canvas-light}` it collapses to 2.84:1 — never use it on light.
- **Muted Readable** (`{colors.muted-readable}` — #5e6673) — **prescribed, not extracted.** `{colors.muted}` fails AA body contrast on every surface this file defines (4.34:1 on `{colors.canvas-light}`, 4.16:1 on `{colors.surface-soft-light}`, 4.46:1 on `{colors.canvas-dark}`, 3.65:1 on `{colors.surface-card-dark}`), and the file uses it for 12px captions and footer links. That is a real AA failure in the live brand, stated plainly. Where secondary text runs below 18.66px bold / 24px regular on a light surface, substitute `{colors.muted-readable}` (5.79:1 on `{colors.canvas-light}`, 5.32:1 on `{colors.surface-strong-light}`); on dark surfaces substitute `{colors.muted-strong}`. `{colors.muted}` stays valid for large labels, where the 3:1 threshold applies and it passes on all four surfaces.
- **On Primary** (`{colors.on-primary}` — #181a20): Black text on yellow primary CTAs.
- **On Dark** (`{colors.on-dark}` — #ffffff): Pure white for high-contrast headlines on dark canvas.

### Trading Semantics
- **Trading Up** (`{colors.trading-up}` — #0ecb81): Price-up green, used as text color in tables, charts, and inline ticker arrows. Never as a button background.
- **Trading Down** (`{colors.trading-down}` — #f6465d): Price-down red. Same usage rules as trading-up.

### Info / Focus
- **Info** (`{colors.info}` — #3b82f6): Inline info badges and the focus-ring base. The Tailwind `--tw-ring-color` token surfaced by dembrandt — used on input focus.
- **Focus** (`{colors.focus}` — #1f6feb) — **prescribed, not extracted.** A single ring cannot serve both a white transactional page and a yellow CTA, so the system picks the ring by the colour it is drawn *against*, not by theme. `{colors.focus}` is the deeper of the two: 4.63:1 on `{colors.canvas-light}`, 4.44:1 on `{colors.surface-soft-light}`, 4.25:1 on `{colors.surface-strong-light}`, and — the case that forces the darker value — 3.25:1 on `{colors.primary}`, so the ring around a yellow `{component.button-primary}` stays visible in *both* themes. It is a deepened sibling of the extracted `{colors.info-ring}` (#3b82f6), not a new hue; yellow is deliberately not used for focus, because a yellow ring on a yellow CTA is invisible and because `{colors.primary}` is reserved for action, not for system state.
- **Focus on Dark** (`{colors.focus-on-dark}` — #3b82f6) — **prescribed**, and the same hex as `{colors.info-ring}`. Drawn on dark panels, where the deeper ring loses out: 5.26:1 on `{colors.canvas-dark}`, 4.30:1 on `{colors.surface-card-dark}`, 3.57:1 on `{colors.surface-elevated-dark}` (`{colors.focus}` reaches only 2.83:1 on that last surface, which is why the pair exists).

## Typography

### Font Family
The system runs **BinanceNova** for display and body, and **BinancePlex** for numerical / financial data. Both are licensed Binance custom typefaces. The fallback stack walks `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.

The split is functional, not decorative:
- BinanceNova → editorial type (headlines, paragraphs, button labels, nav)
- BinancePlex → tabular numerical type (prices, volumes, percentages, stat counters, prize pools)

Mixing them is not optional — BinanceNova on a price ticker would lose the trading-platform character; BinancePlex on a paragraph would feel monospace-cold.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 64px | 700 | 1.1 | -1px | Homepage h1 ("316,258,026 USERS TRUST US") |
| `{typography.display-lg}` | 48px | 700 | 1.1 | -0.5px | Brand-claim headlines ("FUNDS ARE SAFU"), prize-pool hero ("Futures Masters Arena") |
| `{typography.display-md}` | 40px | 600 | 1.15 | -0.3px | Section heads on long-scroll pages |
| `{typography.display-sm}` | 32px | 600 | 1.2 | 0 | CTA band headlines ("Secure, Low-Fee Trading on Binance") |
| `{typography.title-lg}` | 24px | 600 | 1.3 | 0 | Sub-section titles |
| `{typography.title-md}` | 20px | 600 | 1.35 | 0 | QR-promo cards, feature card titles |
| `{typography.title-sm}` | 16px | 600 | 1.4 | 0 | Trust badges, FAQ rows, step labels |
| `{typography.number-display}` | 40px | 700 | 1.1 | -0.3px | Big stat numbers (15,000 BTC, $429,423,449) — BinancePlex |
| `{typography.number-md}` | 16px | 500 | 1.4 | 0 | Markets table prices, table cells — BinancePlex |
| `{typography.number-sm}` | 14px | 500 | 1.4 | 0 | Inline prices, %  changes — BinancePlex |
| `{typography.body-md}` | 14px | 400 | 1.5 | 0 | Default running-text — BinanceNova |
| `{typography.body-sm}` | 13px | 400 | 1.5 | 0 | Cookie consent text, footer body |
| `{typography.caption}` | 12px | 500 | 1.4 | 0 | Small meta labels |
| `{typography.button}` | 14px | 600 | 1 | 0 | Standard CTA button labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Top nav menu items |

### Principles
Display sizes use weight 700 — heavier than most marketing systems. This makes sense for a trading platform: numbers need to read at a glance, headlines need to compete with chart visualizations and dense data tables. The system will not soften display weight to 400 the way Airtable or Stripe does.

`{typography.number-display}` and the smaller number variants always use **BinancePlex**, even when surrounding body type uses BinanceNova. Prices, volumes, and stat counters render in BinancePlex regardless of context — it is the system's "trustworthy number" voice.

### Note on Font Substitutes
If BinanceNova and BinancePlex are unavailable, **Inter** is the closest open-source substitute for BinanceNova and **JetBrains Mono** or **IBM Plex Sans** is the closest substitute for BinancePlex (depending on whether tabular monospace fidelity matters more than humanist proportions). Adjust display headlines down by ~3% in line-height to match BinanceNova's tighter cap height.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- **Section padding (vertical):** `{spacing.section}` (80px) — slightly tighter than airy marketing sites (96px) because Binance pages mix marketing bands with dense product surfaces (markets tables, FAQ accordions).
- **Card internal padding:** `{spacing.lg}` (24px) for content cards and markets tables; `{spacing.xl}` (32px) for QR-promo cards and CTA bands; `{spacing.md}` (16px) for trust badges and table rows.
- **Gutters:** `{spacing.lg}` (24px) between cards in 3-up grids; `{spacing.md}` (16px) inside footer column gutters and dense FAQ lists.

### Grid & Container
- **Max content width:** ~1280px centered on marketing pages; ~1440px on product surfaces (markets, smart-money tables) where horizontal density matters.
- **Editorial body:** Single 12-column grid; product pages often use 8/4 split (main panel + side rail).
- **Markets table:** 5-column header (Pair / Last Price / 24h Change / 24h Volume / Action), with the first column carrying coin icon + symbol pair.
- **Footer:** 6-column link list at desktop, wrapping to 2-up at tablet and 1-up on mobile.

### Whitespace Philosophy
Binance is denser than typical marketing sites — long-scroll pages mix hero bands with markets tables, FAQ accordions, and feature grids without much breathing room between them. The system trusts contrast (yellow vs. dark canvas, green vs. red price cells) to do the visual separation work, not whitespace. Where whitespace appears, it's always uniform — `{spacing.section}` between every major band.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body sections, top nav, hero bands, footer |
| Soft hairline | 1px `{colors.hairline-on-dark}` or `{colors.hairline-on-light}` | Inputs, table dividers, FAQ row separators, secondary buttons |
| Card surface | `{colors.surface-card-dark}` background on dark canvas, `{colors.canvas-light}` on light context — no shadow | All elevated cards (markets-table-card, QR-promo-card, feature-photo-card, trust-badges) |
| Subtle drop shadow | `{shadow.card-over-image}` — **prescribed**: the screenshots show a faint shadow but no extractable rgba value | Used sparingly on the buy-crypto-amount-card on transactional pages |
| Focus ring | `{shadow.focus-ring}` on light surfaces and on yellow CTAs; `{shadow.focus-ring-on-dark}` on dark panels. Drawn at full alpha, not 50% — a 50%-alpha ring halves the measured contrast and would drop `{colors.focus}` on `{colors.primary}` below 3:1 | Input + button keyboard focus state |

The elevation philosophy is **flat surfaces with color-block separation**. Binance does not use heavy drop shadows or glassmorphism — depth comes from the step between `{colors.canvas-dark}` and `{colors.surface-card-dark}`. Measured, that step is small: canvas → card is 1.22:1 and card → `{colors.surface-elevated-dark}` is 1.21:1 (canvas → elevated, 1.48:1). It is a legible boundary on a calibrated screen and a near-invisible one in bright ambient light, so **a card must never rely on the surface step alone to communicate that it is interactive** — pair it with a hairline, a radius change, or a label. Elevation is expressed exactly one way, as a surface-tone step; the hairline is a boundary, not an elevation level, and `{shadow.card-over-image}` is the single documented exception, used only where a card sits over photography and no tone step is available.

### Decorative Depth
- **Yellow → dark vertical gradient backdrop** on the Futures Arena hero: `{colors.primary}` fading down to `{colors.canvas-dark}`. This is a single-page treatment used for product-launch / event hero surfaces, not a system-wide signature.
- **Coin-stack illustrations** flanking large stat blocks (3D rendered crypto coins, trophy icons). These are illustrations, not tokens — treat as content rather than design system surface.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | Almost no use — reserved for very small badges |
| `{rounded.sm}` | 4px | Small inline buttons (subscribe, trading-up / trading-down inline) |
| `{rounded.md}` | 6px | Standard CTA buttons, primary buttons, primary input fields |
| `{rounded.lg}` | 8px | Search input, content cards, trust badges, sub-cards |
| `{rounded.xl}` | 12px | Elevated card containers (markets-table-card, QR-promo-card, CTA bands) |
| `{rounded.pill}` | 9999px | Prominent feature CTAs ("Sign Up" pill on dark, futures-arena "Join Now") |
| `{rounded.full}` | 9999px / 50% | Coin icons, avatars |

Binance's radius hierarchy is tighter than typical marketing systems — most surfaces sit at 6-12px. The pill radius is a deliberate exception used to signal "this is a top-of-page action."

### Photography & Iconography
- Coin icons render as 24×24 or 32×32 rounded glyphs (often 50% radius on circular outline + the coin's brand color inside).
- 3D rendered coin stacks and trophy illustrations are full-color illustrations with a slight floor shadow — not flat icons.
- Photographic content (people-using-the-app section) crops to `{rounded.xl}` (12px) corners, full-bleed on mobile.

## Components

### Top Navigation

**`top-nav-dark`** — The marketing top nav on dark canvas. 64px tall, `{colors.canvas-dark}` background. Carries the yellow Binance wordmark at left, primary horizontal menu (Buy Crypto, Markets, Trade, Futures, Earn, Square, Smart Money, Campaigns), right-side cluster with language selector, light/dark toggle, "Log In" text link, "Sign Up" `{component.button-primary}`. The wordmark uses `{colors.primary}` for "BINANCE" type.

**`top-nav-light`** — The transactional top nav on light canvas (buy crypto, deposit pages). Same layout but `{colors.canvas-light}` background and `{colors.ink}` menu items.

### Buttons

**`button-primary`** — The signature primary CTA. Background `{colors.primary}`, text `{colors.on-primary}` (black on yellow — the system's iconic combination), type `{typography.button}`, padding 12px × 24px, height 40px, rounded `{rounded.md}` (6px). Press state: `button-primary-active` darkens to `{colors.primary-active}` (#f0b90b). Disabled state: `button-primary-disabled` desaturates to `{colors.primary-disabled}`.

**`button-primary-pill`** — A larger pill variant of the primary CTA used for top-of-page sign-up moments and product-launch heroes (Futures Arena "Join Now"). Same yellow + black combination, padding 14px × 32px, rounded `{rounded.pill}` (9999px). Use sparingly — the pill is a "this is THE action" signal.

**`button-secondary-on-dark`** — Used over `{colors.canvas-dark}` for less-emphasized actions. Background `{colors.surface-card-dark}`, text `{colors.on-dark}`, rounded `{rounded.md}`.

**`button-secondary-on-light`** — Light-canvas equivalent. Background `{colors.canvas-light}` with `{colors.hairline-on-light}` 1px border, text `{colors.ink}`.

**`button-tertiary-text`** — Inline text button with no background. Used for "Log In" in the top nav and inline "Read More" links.

**`button-trading-up`** — A solid green button used on price-up signals (Buy / Long actions). Background `{colors.trading-up}`, text `{colors.on-dark}`, rounded `{rounded.sm}` (4px), padding 8px × 20px. Smaller and tighter than `{component.button-primary}` because it appears in dense trading interfaces.

**`button-trading-down`** — Symmetric red variant for Sell / Short actions. Same shape, background `{colors.trading-down}`.

**`button-subscribe`** — Compact yellow CTA used in the Smart Money traders table to subscribe to a top trader. Smaller height (28px) and tighter padding than the primary CTA — fits inside dense table rows. Same yellow + black combination.

**`text-link`** — Inline body links in `{colors.primary}` (yellow on dark, also yellow on light). No underline by default. Type inherits `{typography.body-md}`.

### Cards & Containers

**`hero-band-dark`** — Full-width dark band carrying the homepage h1 + sub-headline + dual CTA pair. Background `{colors.canvas-dark}`, padding `{spacing.section}` (80px). The h1 ("316,258,026 USERS TRUST US") uses `{typography.hero-display}` at 64px / 700 — the system's largest type role.

**`stat-callout-card`** — Inline yellow stat numbers (15,000 BTC, 7,488,223, $429,423,449). Transparent background, text `{colors.primary}`, type `{typography.number-display}` in BinancePlex. Used as a flat layout block, not a card with surface — the yellow text alone carries the visual weight.

**`trust-badge`** — Small dark cards holding "No.1 Customer Service" / "No.1 Trading Volume" claims. Background `{colors.surface-card-dark}`, rounded `{rounded.lg}` (8px), padding 16px × 20px. Yellow numeric or word badge ("No.1") sits next to a short label.

**`markets-table-card`** — The right-side markets table on the homepage. Background `{colors.surface-card-dark}`, rounded `{rounded.xl}` (12px), padding `{spacing.lg}` (24px). Carries a tab row (Popular / New listing / Top gainers), then a 5-column row of coin pairs with last price, 24h change %, action button. Each row uses `{component.markets-row}`.

**`markets-row`** — A single row inside the markets table. Transparent background, 12px vertical padding, hairline divider between rows. Coin icon (32×32) + symbol on left; last price in `{typography.number-md}` (BinancePlex); 24h change cell colored by direction (`{component.price-up-cell}` or `{component.price-down-cell}`); right-aligned chevron icon for "view detail."

**`price-up-cell`** / **`price-down-cell`** — Colored text cells for price changes. Transparent background, text `{colors.trading-up}` or `{colors.trading-down}`, type `{typography.number-md}` in BinancePlex. Always paired with a small triangle arrow indicating direction.

**`feature-photo-card`** — The "Trade on the go" section's photo strip — 3 lifestyle photos showing people using the Binance app. Background `{colors.surface-card-dark}`, rounded `{rounded.xl}`. Photos crop edge-to-edge, no internal padding around the image.

**`qr-promo-card`** — The "Trade on the go. Anywhere, anytime." card with QR code. Background `{colors.surface-card-dark}`, rounded `{rounded.xl}`, padding `{spacing.xl}` (32px). Contains an h2 in `{typography.title-md}`, a body paragraph, app store badges (iOS / Android), and a centered QR code.

**`funds-safu-band`** — The yellow-headlined "FUNDS ARE SAFU" band. Background stays `{colors.canvas-dark}`, but the headline uses `{colors.primary}` at `{typography.display-lg}`. Below the headline, three large `{component.stat-callout-card}` numbers anchor the band: total BTC reserves, users helped, funds recovered.

**`faq-row`** — A single FAQ accordion row. Transparent background, padding 20px vertical, hairline divider between rows. Closed state: question in `{typography.title-sm}` + chevron icon at right. Open state: question + answer body in `{typography.body-md}`.

**`cta-band-dark`** — The "Secure, Low-Fee Trading on Binance" pre-footer CTA band. Background `{colors.surface-card-dark}` (one step elevated from canvas), rounded `{rounded.xl}`, padding `{spacing.xxl}` (48px). Carries an h2 in `{typography.display-sm}` and a `{component.button-primary}` aligned right.

### Light-Mode Transactional Components

**`buy-crypto-amount-card`** — The right-rail card on the Buy BTC page. Background `{colors.canvas-light}`, rounded `{rounded.lg}` (8px), padding `{spacing.lg}` (24px). Carries an editable amount input in `{typography.number-display}` (BinancePlex), a currency selector, and a yellow `{component.button-primary}` for "Continue" / "Confirm Order."

**`steps-card`** — The "How to Buy Crypto" 3-up cards (Enter Amount → Confirm Order → Receive Crypto). Background `{colors.canvas-light}`, rounded `{rounded.lg}`, padding `{spacing.lg}`. Each card has a small numbered icon, a `{typography.title-sm}` step name, and a body description.

**`price-chart-card`** — The "Bitcoin Markets" card carrying the BTC price chart. Background `{colors.canvas-light}`, rounded `{rounded.lg}`. Top row carries pair selector ($79,065.04, +0.45%); main area is a candlestick / line chart in `{colors.trading-up}` and `{colors.trading-down}`; bottom row carries timeframe selector (24H / 1W / 1M / 3M / 1Y / ALL).

**`conversion-cell`** — A single row in the BTC ↔ USD conversion table. Transparent background, text `{colors.body-on-light}`, type `{typography.body-md}`. Pair label on left (BTC, USDT, etc.); USD equivalent on right.

### Inputs & Forms

**`search-input-on-dark`** — The "Search currencies" input on the homepage hero. Background `{colors.surface-card-dark}`, text `{colors.on-dark}`, rounded `{rounded.lg}` (8px), padding 10px × 16px, height 40px. Carries a yellow `{component.button-primary-pill}` on the right side ("Sign Up").

**`text-input-on-light`** — Standard input on transactional pages. Background `{colors.canvas-light}`, 1px `{colors.hairline-on-light}` border, rounded `{rounded.md}` (6px), padding 10px × 16px, height 40px. Focus state inherits the focus-ring shadow.

**`cookie-consent-card`** — The cookie banner card visible on the homepage. Background `{colors.canvas-light}`, rounded `{rounded.lg}`, padding `{spacing.md}` (16px). Body text in `{typography.body-sm}` (13px / 400) with three stacked button options (Accept Cookies & Continue / Reject Additional Cookies / Manage Cookies).

### Smart Money Sub-System

**`trader-row`** — A single row in the top-traders table on /smart-money. Transparent background, padding 12px vertical, hairline divider between rows. Avatar + trader name + private/public badge on left; ROI %, AUM, mint date columns; yellow `{component.button-subscribe}` on right.

### Signature Components

**`arena-hero-gradient`** — The Futures Arena product-launch hero. A vertical gradient from `{colors.primary}` at top to `{colors.canvas-dark}` at bottom, with the prize-pool headline (4,000,000 USDT) in `{typography.display-lg}` centered. A `{component.button-primary-pill}` ("Join Now") sits below the headline. Used only on product-launch event surfaces — do not generalize to other heroes.

### Footer

**`footer-light`** — The light-gray footer that closes every page (including dark-canvas pages). Background `{colors.surface-soft-light}` (#fafafa), text `{colors.body-on-light}`. 6-column link list at desktop covering Community / About Us / Products / Business / Service / Learn columns. Vertical padding 64px. The deliberate light footer on a dark page is one of Binance's most distinctive layout choices — it visually closes the page with a "marketing reset" surface.

### States

Binance's extracted surfaces document only Default, Active/Pressed and Disabled (see `{component.button-primary-active}` and `{component.button-primary-disabled}`). Everything below marked **prescribed** is a system-consistent completion, not an extracted fact: hover, focus-visible, loading, selected and error were not observable in the analyzed static screenshots.

| Component | Default | Hover (prescribed) | Focus-visible (prescribed) | Active / pressed | Disabled | Loading (prescribed) | Selected (prescribed) | Error (prescribed) |
|---|---|---|---|---|---|---|---|---|
| `{component.button-primary}` | `{colors.primary}` + `{colors.on-primary}` | `{colors.primary-active}` fill | `{shadow.focus-ring}` (same ring in both themes — the fill is yellow in both) | `{colors.primary-active}` fill, no travel | `{colors.primary-disabled}` fill, `{colors.muted}` label, pointer-events off | label swaps to a centred spinner, width held so the button does not reflow | n/a | n/a |
| `{component.button-primary-pill}` | as above, `{rounded.pill}` | `{colors.primary-active}` fill | `{shadow.focus-ring}` | `{colors.primary-active}` fill | `{colors.primary-disabled}` fill | spinner, as above | n/a | n/a |
| `{component.button-secondary-on-dark}` | `{colors.surface-card-dark}` | lifts to `{colors.surface-elevated-dark}` | `{shadow.focus-ring-on-dark}` | stays at `{colors.surface-elevated-dark}` | `{colors.surface-card-dark}` with `{colors.muted}` label | spinner | n/a | n/a |
| `{component.button-secondary-on-light}` | `{colors.canvas-light}` + `{colors.border-control}` | fills `{colors.surface-strong-light}` | `{shadow.focus-ring}` | fills `{colors.surface-strong-light}` | `{colors.border-strong}` border, `{colors.muted}` label | spinner | n/a | n/a |
| `{component.button-trading-up}` / `{component.button-trading-down}` | `{colors.trading-up}` / `{colors.trading-down}` | 4% darker fill (no new token — do not shift hue, the colour *is* the meaning) | `{shadow.focus-ring-on-dark}` | same darker fill | `{colors.surface-elevated-dark}` fill, `{colors.muted-strong}` label | spinner | long/short side selected: the unselected side drops to the disabled treatment | order rejected: `{colors.trading-down}` helper text below, never a colour change on the button |
| `{component.button-subscribe}` | `{colors.primary}` | `{colors.primary-active}` | `{shadow.focus-ring-on-dark}` | `{colors.primary-active}` | `{colors.primary-disabled}` | spinner inside the 28px height | subscribed: flips to `{component.button-secondary-on-dark}` with a check glyph | n/a |
| `{component.text-link}` | `{colors.primary}` | underline appears; colour held | `{shadow.focus-ring-on-dark}` / `{shadow.focus-ring}` by surface | `{colors.primary-active}` | `{colors.muted}`, no underline | n/a | n/a | n/a |
| `{component.top-nav-dark}` item | `{colors.body}` | item row fills `{colors.surface-elevated-dark}` | `{shadow.focus-ring-on-dark}` | dropdown held open | — | — | current section: `{colors.primary}` 2px underline *and* a weight step, so colour is not the only signal | n/a |
| `{component.markets-row}` | transparent | fills `{colors.surface-elevated-dark}` | `{shadow.focus-ring-on-dark}` inset on the row | — | — | skeleton bars at `{colors.surface-elevated-dark}`, opacity-pulsed, no layout shift | tab-selected pair gets `{colors.primary}` left edge | price feed stale: row drops to `{colors.muted-strong}` with a stale badge |
| `{component.search-input-on-dark}` | `{colors.surface-card-dark}` | boundary strengthens to `{colors.border-control}` | `{shadow.focus-ring-on-dark}` | — | `{colors.muted}` placeholder, boundary removed | inline spinner replaces the search glyph | n/a | `{colors.trading-down}` 1px boundary + message below, plus an icon — never colour alone |
| `{component.text-input-on-light}` | `{colors.canvas-light}` + `{colors.border-control}` | boundary darkens one step | `{shadow.focus-ring}` | — | `{colors.surface-strong-light}` fill, `{colors.border-strong}` boundary | inline spinner at the right edge | n/a | `{colors.trading-down}` boundary + message + icon |
| `{component.faq-row}` | collapsed, `{colors.on-dark}` question | question lightens to `{colors.on-dark}`, chevron rotates | `{shadow.focus-ring-on-dark}` on the row | chevron rotated, answer open | — | n/a | open row is the selected state — chevron rotation carries it, not colour | n/a |
| `{component.trader-row}` | transparent | fills `{colors.surface-elevated-dark}` | `{shadow.focus-ring-on-dark}` | — | — | skeleton bars | subscribed trader keeps a `{colors.primary}` left edge | — |
| `{component.cookie-consent-card}` | `{colors.canvas-light}` | per-button only | `{shadow.focus-ring}` per button | per-button only | — | — | — | — |

**Genuinely two-state components.** `{component.hero-band-dark}`, `{component.cta-band-dark}`, `{component.funds-safu-band}`, `{component.arena-hero-gradient}`, `{component.stat-callout-card}`, `{component.trust-badge}`, `{component.qr-promo-card}`, `{component.feature-photo-card}`, `{component.steps-card}`, `{component.price-up-cell}`, `{component.price-down-cell}`, `{component.conversion-cell}` and `{component.footer-light}` are static containers and cells: they have a default state and, where they carry a live number, a value-changed state. No hover, focus, pressed, selected or error applies, because nothing in them is focusable. `{component.price-chart-card}` and `{component.buy-crypto-amount-card}` are containers whose *contents* carry states; the card itself has one.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity. It was not measured from the live site** — no timing function, duration or curve below was extracted from Binance. The analyzed set was static screenshots plus a token dump; there was no recording, no DevTools trace and no running page. Treat every value here as a system-consistent proposal, and replace it with a measured value the moment one exists.

**Profile: Calm** (250ms base, symmetric easing, 40ms stagger). Binance is a dark-canvas platform but not a luxury one, and not a developer tool, so the profile rules land on Calm. The tension is real and worth naming: dense trading surfaces want Crisp immediacy, and the Calm profile accommodates that at the fast end rather than by switching profile — price-direction feedback runs at `{motion.duration-instant}` (80ms), because a 250ms fade on a changing price is a lie about when the price changed. Everything editorial — bands, cards, modals, route changes — runs at `{motion.duration-base}`. The easings are biased symmetric (`{motion.ease-standard}` = cubic-bezier(0.4, 0, 0.2, 1)) rather than the near-linear-out of Crisp or the overshoot of Playful: no bounce, no spring, nothing that reads as playful on a page where people move money.

Only `transform` and `opacity` are animated. Never animate `width`, `height`, `top`, `left` or `margin` — a reflowing markets table during a price tick is both a jank source and a mis-click risk.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav item, markets row) | `{motion.duration-fast}` (150ms) | `{motion.ease-standard}` | `opacity` on the fill layer; background-colour cross-fade. No lift, no scale — Binance's flat surfaces do not rise | Instant state change, no transition |
| Press (all buttons) | `{motion.duration-instant}` (80ms) | `{motion.ease-exit}` | `opacity` to 0.88 on press, back on release. No scale: a scaling Buy button in a dense order panel moves the hit target | Instant, opacity only |
| Focus-visible ring | `{motion.duration-instant}` (80ms) | `{motion.ease-enter}` | `opacity` on `{shadow.focus-ring}` / `{shadow.focus-ring-on-dark}` | Ring appears instantly, never animated away — a keyboard user must never wait to see where they are |
| Page / route transition | `{motion.duration-base}` (250ms) | `{motion.ease-standard}` | `opacity` only, 0 → 1 on the incoming view. No slide: the dark→light theme flip between marketing and transactional surfaces would read as a flash if it also travelled | Cross-fade capped at 150ms; no travel |
| Modal / drawer enter | `{motion.duration-base}` (250ms) | `{motion.ease-enter}` | `opacity` 0 → 1 with `transform: translateY(8px) → 0`; scrim fades over the same duration | `opacity` only at 150ms, no travel |
| Modal / drawer exit | `{motion.duration-fast}` (150ms) | `{motion.ease-exit}` | reverse of enter | `opacity` only at 120ms |
| Dropdown (nav menu, pair selector, timeframe) enter | `{motion.duration-fast}` (150ms) | `{motion.ease-enter}` | `opacity` 0 → 1, `transform: translateY(4px) → 0` | `opacity` only at 120ms |
| Dropdown exit | `{motion.duration-instant}` (80ms) | `{motion.ease-exit}` | `opacity` 1 → 0 | `opacity` only at 80ms |
| Toast / order confirmation | enter `{motion.duration-base}`, hold 4s, exit `{motion.duration-fast}` | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(12px) → 0` | `opacity` only at 150ms, same 4s hold, no travel |
| List enter (markets rows, trader rows, FAQ answers) | `{motion.duration-fast}` (150ms) per item, `{motion.stagger-step}` (40ms) between items, capped at 8 items | `{motion.ease-enter}` | `opacity` 0 → 1; rows do not travel, so a long table does not appear to slide | All items fade together at 150ms; stagger dropped entirely |
| List exit | `{motion.duration-instant}` (80ms), no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | `opacity` only at 80ms |
| Loading (skeleton rows, button spinner) | 1200ms loop | `{motion.ease-standard}` | `opacity` pulse 0.4 → 0.8 on skeleton bars; `transform: rotate()` on the spinner. These are the only permitted infinite animations | Spinner freezes to a static glyph; skeleton bars hold a single static `opacity` of 0.6 |
| Price-change flash (`{component.price-up-cell}` / `{component.price-down-cell}`) | `{motion.duration-instant}` (80ms) in, `{motion.duration-slow}` (400ms) out | `{motion.ease-exit}` | `opacity` on a `{colors.trading-up}` / `{colors.trading-down}` tint layer behind the cell. The number itself never moves | Removed entirely. The arrow glyph and the cell colour already carry direction, so nothing is lost |

`{motion.duration-emphasis}` (600ms) is defined for completeness and has **no assigned use** in this system. The `{component.arena-hero-gradient}` product-launch hero is the only surface that could justify it; nothing on a trading or transactional surface should take 600ms.

### `@media (prefers-reduced-motion: reduce)`

**Removed:** all `transform` — every translate, scale and rotate, including the modal and toast rise, the dropdown drop, the chevron rotation on `{component.faq-row}` (the chevron still flips, it just flips instantly), and the spinner's rotation. All stagger. The price-change flash. The decorative gradient motion on `{component.arena-hero-gradient}`, which freezes to its static yellow→dark end state.

**Kept:** `opacity` cross-fades, capped at 150ms. The focus ring, which appears instantly in both modes. Every state change itself — hover, press, selection and error are all still fully visible, they just arrive without a transition. Skeleton loaders stay as static placeholders so a loading table is still distinguishable from an empty one.

**Never conditional on the query:** no content is gated behind an animation, so nothing is hidden from a reduced-motion user. Nothing animates on first paint; the hero headline, the markets table and every price render at their final state and then begin updating.

## Accessibility

Contrast below is measured with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. Everything about rendered geometry — real tap-target size, overlap, clipping, frame rate — is **not measured here**; there was no running page. Sizes quoted are the dimensions this document declares, not observed ones.

### Measured contrast, key pairs

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas-light}` | 17.39:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas-dark}` | 16.35:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.surface-card-dark}` | 13.36:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.surface-elevated-dark}` | 11.08:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 12.18:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary-active}` | 9.65:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.accent-turquoise}` | 7.51:1 | 4.5:1 | Pass |
| `{colors.muted}` on `{colors.canvas-light}` | 4.34:1 | 4.5:1 | **Fail** (passes the 3:1 large-text threshold) |
| `{colors.muted}` on `{colors.surface-soft-light}` | 4.16:1 | 4.5:1 | **Fail** |
| `{colors.muted}` on `{colors.canvas-dark}` | 4.46:1 | 4.5:1 | **Fail**, by 0.04 |
| `{colors.muted}` on `{colors.surface-card-dark}` | 3.65:1 | 4.5:1 | **Fail** |
| `{colors.muted-readable}` on `{colors.canvas-light}` | 5.79:1 | 4.5:1 | Pass (prescribed substitute) |
| `{colors.muted-strong}` on `{colors.surface-card-dark}` | 5.56:1 | 4.5:1 | Pass (dark-surface substitute) |
| `{colors.muted-strong}` on `{colors.canvas-light}` | 2.84:1 | 4.5:1 | **Fail** — light-surface use is forbidden above |
| `{colors.primary}` on `{colors.canvas-light}` | 1.43:1 | 4.5:1 | **Fail** — see below |
| `{colors.on-dark}` on `{colors.trading-up}` | 2.13:1 | 4.5:1 | **Fail** — see below |
| `{colors.on-dark}` on `{colors.trading-down}` | 3.53:1 | 4.5:1 | **Fail** — see below |
| `{colors.trading-up}` on `{colors.canvas-light}` | 2.13:1 | 4.5:1 | **Fail** — see below |
| `{colors.trading-down}` on `{colors.canvas-light}` | 3.53:1 | 4.5:1 | **Fail** |
| `{colors.trading-up}` on `{colors.canvas-dark}` | 9.10:1 | 4.5:1 | Pass |
| `{colors.trading-down}` on `{colors.canvas-dark}` | 5.49:1 | 4.5:1 | Pass |
| `{colors.hairline-on-light}` on `{colors.canvas-light}` | 1.18:1 | 3.0:1 (boundary) | **Fail** — decorative only |
| `{colors.hairline-on-dark}` on `{colors.canvas-dark}` | 1.48:1 | 3.0:1 (boundary) | **Fail** — decorative only |
| `{colors.border-strong}` on `{colors.canvas-light}` | 1.53:1 | 3.0:1 (boundary) | **Fail** — decorative only |
| `{colors.border-control}` on `{colors.canvas-light}` | 3.32:1 | 3.0:1 | Pass (prescribed substitute) |
| `{colors.border-control}` on `{colors.surface-card-dark}` | 4.77:1 | 3.0:1 | Pass |
| `{colors.muted-readable}` on `{colors.surface-card-dark}` | 2.73:1 | 4.5:1 | **Fail** — this token is light-surface only; on dark surfaces the substitute is `{colors.muted-strong}` |

**Where Binance genuinely fails AA, stated plainly.** Four real failures, none of which this document is willing to falsify by editing a brand hex:

1. **`{colors.muted}` (#707a8a) fails body contrast on every surface in the system.** It is the brand's workhorse secondary tone and it is used at 12px. The honest reading: Binance's secondary text is below AA everywhere, and worst (3.65:1) on the markets table card where traders read column headers.
2. **`{colors.primary}` (#FCD535) as text on `{colors.canvas-light}` is 1.43:1** — effectively invisible. `{component.text-link}` documents yellow links "also yellow on light", which cannot be used as running text on white. On light surfaces, link text must switch to `{colors.focus}` (4.63:1) or `{colors.ink}` with an underline; yellow on light is valid only as a *fill* behind `{colors.on-primary}`, never as ink.
3. **White on the trading colours fails.** `{component.button-trading-up}` and `{component.button-trading-down}` both declare `{colors.on-dark}` labels: 2.13:1 on green, 3.53:1 on red. These are the Buy/Sell and Long/Short buttons — the highest-consequence controls on the platform — and their labels are below AA. `{colors.on-primary}` (#181a20) would reach 8.18:1 and 4.93:1 on the same two fills, matching the yellow CTA's black-on-colour logic. This document does **not** make that swap, because the white label is an extracted fact and the change needs brand approval; it is filed for approval instead.
4. **`{colors.trading-up}` as text on `{colors.canvas-light}` is 2.13:1.** Green price-up text on `{component.price-chart-card}` (white background) is unreadable at AA. The dark theme is fine (9.10:1). A light-theme-only darker green is needed and is not in this file.

**Colour is never the only signal.** Price direction always carries a triangle arrow alongside the green/red (already documented on `{component.price-up-cell}`), the selected nav item carries an underline *and* a weight step, and input errors carry an icon and a message, not just a red boundary. This matters more here than on most sites: red/green deuteranopia is the single most common colour-vision deficiency and this brand encodes gain and loss in exactly that pair.

### Focus ring visibility, per surface this file defines

| Surface | Ring token | Ratio | Required |
|---|---|---|---|
| `{colors.canvas-light}` | `{colors.focus}` | 4.63:1 | 3.0:1 |
| `{colors.surface-soft-light}` | `{colors.focus}` | 4.44:1 | 3.0:1 |
| `{colors.surface-strong-light}` | `{colors.focus}` | 4.25:1 | 3.0:1 |
| `{colors.primary}` (yellow CTA, either theme) | `{colors.focus}` | 3.25:1 | 3.0:1 |
| `{colors.canvas-dark}` | `{colors.focus-on-dark}` | 5.26:1 | 3.0:1 |
| `{colors.surface-card-dark}` | `{colors.focus-on-dark}` | 4.30:1 | 3.0:1 |
| `{colors.surface-elevated-dark}` | `{colors.focus-on-dark}` | 3.57:1 | 3.0:1 |

Every surface in the system is covered. The ring is 2px at full alpha, drawn outside the control's own boundary so it is never clipped by `{rounded.md}` corners, and it is never removed without a replacement — `outline: none` with no ring is a system violation. Note that the extracted `{colors.info-ring}` at 50% alpha, as the Elevation table originally described it, does not reach 3:1 on `{colors.primary}`; that is why the ring is specified at full alpha.

### Declared control sizes

Not measured — these are the heights this document declares, and real tap targets depend on rendering.

- `{component.button-primary}` declares 40px height. WCAG 2.1 AA (2.5.8, Target Size Minimum) asks for 24px, which 40px clears; AAA (2.5.5) asks for 44px, which 40px does **not** clear on height alone. The earlier claim in Responsive Behavior that it "meets WCAG AAA's 44 × 44" was wrong and has been corrected.
- `{component.button-subscribe}` declares 28px height. Below AAA, above the AA 24px floor, and the file is right that it matches trading-platform convention — but it should carry 8px of hit-area padding beyond its visual bounds.
- `{component.search-input-on-dark}` and `{component.text-input-on-light}` declare 40px height. Same verdict as the primary button.
- Coin icons are declared 24 × 24 or 32 × 32; the file states the whole `{component.markets-row}` is tappable, which is the right pattern, but row height is not declared anywhere and cannot be verified here.

### Reduced motion

Fully specified above under `@media (prefers-reduced-motion: reduce)`. In short: all travel, scale, rotation and stagger are removed, opacity fades are capped at 150ms, loaders freeze to static placeholders, and no content is gated behind an animation.

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
| `{colors.body}` (`#eaecef`) on `{colors.canvas-light}` (`#ffffff`) | 1.18:1 | 4.5:1 | Fail — body text, all tones |
| `{colors.hairline-on-dark}` (`#2b3139`) on `{colors.surface-card-dark}` (`#1e2329`) | 1.21:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.info}` (`#3b82f6`) on `{colors.canvas-light}` (`#ffffff`) | 3.68:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (Binance Yellow) for primary actions, brand-claim headlines, and the wordmark. Never use it for secondary or decorative purposes — yellow's scarcity is what makes it powerful.
- Keep `{component.button-primary}` (yellow with black text) as the universal primary CTA across both dark and light modes. The same button appears identically on `{colors.canvas-dark}` and `{colors.canvas-light}`.
- Use `{component.button-trading-up}` (green) and `{component.button-trading-down}` (red) only for explicit Buy/Sell or Long/Short actions. Never use them for general "confirm" or "cancel" because they carry semantic price-direction meaning.
- Use BinancePlex for every number. Prices, volumes, percentages, stat counters — all BinancePlex. Mixing BinanceNova into a number ticker breaks the trading-platform character.
- Choose canvas mode by surface intent: dark for marketing / product showcase / trading dashboards; light for transactional dialogs (buy / deposit / withdraw / form submission).
- Anchor every editorial band with `{spacing.section}` (80px). Binance is denser than airy marketing sites — 80px is the right rhythm.

### Don't
- Don't introduce a second brand color. The system has exactly one accent (`{colors.primary}`) and any expansion dilutes the brand identity. The turquoise on Smart Money is a single-product experiment, not a system token.
- Don't use yellow for body text or large surface fills. It is for focal-point CTAs and headlines only. On `{colors.canvas-light}` this is not a taste rule but a contrast one: `{colors.primary}` measures 1.43:1 on white, so yellow ink on a light surface is unreadable at any size.
- Don't use `{colors.trading-up}` / `{colors.trading-down}` as background fills on cards. They are price-direction signals, expressed as text color or small badge fill — never as a card surface.
- Don't soften display weight. `{typography.hero-display}` and `{typography.display-lg}` are intentionally weight 700 — going to 400 reads as design-portfolio, not trading platform.
- Don't add atmospheric gradients to the canvas (mesh, aurora, glow effects). Binance trusts color-block contrast — adding atmospheric depth muddies the trading-platform feel.
- Don't add spring, bounce or overshoot easing. The system is on the **Calm** motion profile with symmetric easing (`{motion.ease-standard}`); a bouncing Buy button reads as a game, not an exchange. Equally, don't slow editorial motion past `{motion.duration-base}` — `{motion.duration-emphasis}` has no assigned use here.
- Don't animate `width`, `height`, `top`, `left` or `margin` anywhere, and never reflow a markets row during a price tick — the hit target moves under the pointer. `transform` and `opacity` only.
- Don't invert `{component.button-primary}`'s text color. Black on yellow is the system's signature — white text on yellow loses contrast and brand recognition.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Top nav collapses to hamburger; hero h1 drops from 64px to ~36px; markets table converts to a horizontally-scrollable card list; demo grids drop to 1-up; footer 6 columns wrap to 2 |
| Tablet | 768–1024px | Top nav stays horizontal but tightens, secondary menu items hide behind a "More" dropdown; markets table 2-up; pricing/feature grids 2-up |
| Desktop | 1024–1440px | Full top-nav with all primary menu items; 5-column markets table; trading dashboards in 8/4 split (chart + side rail) |
| Wide | > 1440px | Same as desktop with more outer breathing room; max content width caps at 1280-1440px depending on surface |

### Touch Targets
- Primary CTAs render at minimum 40px high (`{component.button-primary}` height). That clears WCAG 2.1 AA (2.5.8, 24px) but **not** AAA (2.5.5, 44 × 44) on height alone; surrounding spacing may close the gap, which cannot be verified from a static document. See Accessibility.
- Subscribe / inline action buttons are 28 × 28 — denser than ideal but matches industry trading platform norms.
- Coin icons in markets tables are 32 × 32px, with the entire row tappable for 44px+ effective target.

### Collapsing Strategy
- Top nav collapses to hamburger at < 768px; the menu opens as a full-screen sheet with the same yellow accent CTAs anchored to the bottom of the sheet.
- Markets table reflows to a horizontally-scrollable single card per coin pair on mobile.
- The hero stat numbers ("316M USERS") shrink proportionally rather than wrapping — Binance's biggest claim must always read as a single block.
- Trading dashboards switch from chart + side-rail to chart-only with a separate "Trade" tab on mobile.
- The light footer stays full-bleed at every breakpoint — it does not collapse to a separate dark variant.

### Image Behavior
- Coin icons stay at fixed 24/32px sizes regardless of breakpoint.
- Lifestyle photos in the "Trade on the go" section crop responsively — wider at desktop, taller (vertical) at mobile.
- 3D coin-stack illustrations are fixed-aspect-ratio assets that scale uniformly without cropping.

## Iteration Guide

1. Focus on ONE component at a time. Reference its YAML key directly (`{component.button-primary}`, `{component.markets-row}`).
2. When adding a new component, decide first whether it lives in dark mode (marketing / product) or light mode (transactional). The same component appears in both with surface tone flipped.
3. Variants of an existing component (`-active`, `-disabled`) live as separate entries in `components:` — never as nested state objects.
4. Use `{token.refs}` everywhere prose mentions a color, a radius, a typography role, or a spacing value.
5. Hover, focus-visible, loading, selected and error were not extractable from the analyzed screenshots, so the Components > States table marks them **prescribed**. Keep that label on any state you add, and do not promote a prescribed state to an extracted fact without a measurement. Default, Active/Pressed and Disabled are the only extracted states.
6. Numbers always use BinancePlex; copy always uses BinanceNova. Mixing them is a system violation.
7. Trading green / red are semantic price tokens — never repurpose them for "success" or "error" generic states.

## Known Gaps

- The dembrandt frequency analyzer captured `#eaecef` (light hairline, count 1022) as the highest-frequency token. The brand-defining `{colors.primary}` (#FCD535) appears far less frequently because it's used scarcely as accent — its system role had to be confirmed from screenshots.
- BinanceNova and BinancePlex weight-axis values are not formalized as variable-font tokens — only the static weights observed in screenshots are documented.
- Animation and transition timings were never measured. Every value in Motion & Animation — durations, easings, stagger, the price-change flash, the loader loop — is prescribed to fit the brand, not extracted. Chart redraw behaviour in particular (candlestick streaming, order-book tick animation) needs a recording of a live trading surface to document honestly.
- Form validation states beyond `{component.text-input-on-light}` defaults are not extracted — error / success input variants would need a sign-up or order-confirmation flow to confirm.
- The trading dashboard surfaces (Spot / Futures / Margin) were not in the analyzed URL set; their order book, candlestick chart configuration, and position-management cards are not documented here.
- The light/dark theme toggle behavior (whether transactional pages can be forced dark by user preference) is product behavior, not extracted from the marketing surfaces.
