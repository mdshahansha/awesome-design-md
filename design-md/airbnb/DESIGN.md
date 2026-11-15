---
version: alpha
name: Airbnb-design-analysis
description: A warm, generous consumer marketplace anchored on a clean white canvas and Airbnb Rausch (#ff385c), the single brand voltage that carries every primary CTA, search-button orb, and rating dot. Type runs Airbnb Cereal VF at modest weights — display sits at 22–28px in weight 500/600 rather than the heavy 700+ that fintech and enterprise systems use; the brand trusts photography and generous whitespace over typographic muscle. Three product entries (Homes, Experiences, Services) sit in the top nav with hand-illustrated 32-icon glyphs and "NEW" badges, signaling a marketplace expansion rather than a feature dump. Pill-shaped search bars (`{rounded.full}`), softly rounded property cards (`{rounded.lg}` ~14px), and 32px button radii read as friendly and human — there is no hard corner anywhere except the body grid.

colors:
  primary: "#ff385c"
  primary-active: "#e00b41"
  primary-disabled: "#ffd1da"
  primary-error-text: "#c13515"
  primary-error-text-hover: "#b32505"
  luxe: "#460479"
  plus: "#92174d"
  ink: "#222222"
  body: "#3f3f3f"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  border-strong: "#c1c1c1"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  focus: "#222222"
  focus-inner: "#ffffff"
  legal-link: "#428bff"
  star-rating: "#222222"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Airbnb Cereal VF', Circular, -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  display-lg:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: -0.44px
  display-md:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 21px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  display-sm:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.18px
  title-md:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  rating-display:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  body-md:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0
  micro-label:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 8px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.32px
    textTransform: uppercase
  button-md:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Airbnb Cereal VF', Circular, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 14px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px

motion:
  duration-instant: 80ms
  duration-fast: 120ms
  duration-base: 200ms
  duration-slow: 320ms
  duration-emphasis: 480ms
  ease-standard: cubic-bezier(0.2, 0, 0, 1)
  ease-enter: cubic-bezier(0.17, 0.89, 0.32, 1.28)
  ease-exit: cubic-bezier(0.3, 0, 1, 1)
  stagger-step: 60ms

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-rausch:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  search-orb:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 48px
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  product-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  product-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 14px 24px
    height: 64px
  search-field-segment:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 8px 24px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  property-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  property-card-photo:
    rounded: "{rounded.md}"
  experience-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
  city-link-block:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  rating-display-card:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.rating-display}"
  guest-favorite-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  new-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.full}"
    padding: 2px 6px
  amenity-row:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 12px 0
  reviews-card:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  host-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 24px
  reservation-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  date-picker-day:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
  date-picker-day-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 12px
    height: 56px
  footer-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: 48px 80px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  legal-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
---

## Overview

Airbnb is the canonical example of a generous, photography-led consumer marketplace. The base canvas is **pure white** (`{colors.canvas}` — #ffffff) with deep near-black ink (`{colors.ink}` — #222222) for headlines and body, and a single voltage of **Rausch** (`{colors.primary}` — #ff385c) carrying every primary CTA, the search-button orb, the heart save state, and inline brand links. There is no secondary brand color in mainline marketing — the **Luxe purple** (`{colors.luxe}` — #460479) and **Plus magenta** (`{colors.plus}` — #92174d) tokens are sub-brand accents that only appear inside Airbnb Luxe / Plus contexts.

Type runs **Airbnb Cereal VF** (a custom variable font Airbnb licenses), with **Circular** as the historic in-house fallback and a system stack underneath. Cereal sits at modest weights — display headlines render at 22–28px in weight 500–600, not the heavy 700+ weights that financial or enterprise systems lean on. The hero h1 ("Inspiration for future getaways") on the homepage is just 28px / 700, which would feel small on a typical SaaS page; here it works because the layout leans on photography (city collage, property cards) for visual weight rather than typographic muscle.

The shape language is **soft**. Buttons are 8px radius (`{rounded.sm}`), property cards are ~14px (`{rounded.md}`), the search bar is fully pill-shaped (`{rounded.full}`), wishlist hearts and search orbs are circles (`{rounded.full}`), and category strip rounded corners run at 32px (`{rounded.xl}`). There is essentially no hard corner anywhere except the body grid itself — every interactive element is rounded.

**Key Characteristics:**
- Single accent color: `{colors.primary}` (#ff385c — "Rausch") carries every primary CTA, the search orb, the heart save state, and the brand wordmark. Used scarcely — most pages are 90% white + ink with one or two Rausch moments.
- Custom variable type: `Airbnb Cereal VF`. Display weights sit at 500–700, body at 400. Modest weight is intentional — the system trusts photography for visual heft.
- Three-product top nav: Homes, Experiences, Services — each with a hand-illustrated 32px icon and "NEW" badges (`{component.new-tag}`) on the two newer products. Active tab uses an underline rule (`{component.product-tab-active}`).
- Pill-shaped global search bar: white surface, fully rounded (`{rounded.full}`), divided by 1px hairlines into Where / When / Who segments, terminated by a circular Rausch search orb (`{component.search-orb}`).
- Property cards are photo-first: aspect-ratio rectangles with `{rounded.md}` corner clipping, swipeable image carousel, "Guest favorite" floating badge top-left, heart icon top-right, then 4–5 lines of meta beneath.
- Editorial dropdowns (footer, language picker) are clean text columns over the white canvas — no card surface, no shadow.
- The design system caps elevation at one shadow tier (`box-shadow: rgba(0,0,0,0.02) 0 0 0 1px, rgba(0,0,0,0.04) 0 2px 6px, rgba(0,0,0,0.1) 0 4px 8px`) — used on hover-floated cards and search/account dropdowns.
- 8px base spacing system, with major sections at `{spacing.section}` (64px) — generous but not airy enough to feel editorial-magazine; the marketplace density wants more cards per scroll.

## Colors

### Brand & Accent
- **Rausch** (`{colors.primary}` — #ff385c): The single brand color. Used for primary CTA backgrounds (Reserve, Continue), the search orb, the heart save state on property cards, and inline brand links. The most recognizable color in consumer travel.
- **Rausch Active** (`{colors.primary-active}` — #e00b41): The press / pointer-down variant — slightly more saturated. Used on `{component.button-primary-active}`.
- **Rausch Disabled** (`{colors.primary-disabled}` — #ffd1da): A pale tint used on disabled CTAs.
- **Luxe Purple** (`{colors.luxe}` — #460479): Sub-brand accent for Airbnb Luxe. Only appears inside Luxe-branded surfaces — never in mainline marketing.
- **Plus Magenta** (`{colors.plus}` — #92174d): Sub-brand accent for Airbnb Plus. Same scoping as Luxe — sub-product only.

### Surface
- **Canvas** (`{colors.canvas}` — #ffffff): The default page floor for every public page. Airbnb does not have a dark mode on the public web.
- **Surface Soft** (`{colors.surface-soft}` — #f7f7f7): The lightest fill — used on disabled fields, sub-nav hover backgrounds, and the inline search filter band.
- **Surface Strong** (`{colors.surface-strong}` — #f2f2f2): Slightly heavier fill — circular icon-button surface (e.g., the breadcrumb back-arrow and listing toolbar buttons).

### Hairlines & Borders
- **Hairline** (`{colors.hairline}` — #dddddd): The default 1px border tone — search bar dividers, table separators, footer column splitters, card 1px borders.
- **Hairline Soft** (`{colors.hairline-soft}` — #ebebeb): A lighter divider used on long-scrolling editorial body separators.
- **Border Strong** (`{colors.border-strong}` — #c1c1c1): A heavier stroke used on disabled outline buttons and form input outlines after focus.

### Text
- **Ink** (`{colors.ink}` — #222222): The dominant text color on light surfaces. Display headlines, body paragraphs, primary nav links, and most inline link text. Never pure black.
- **Body** (`{colors.body}` — #3f3f3f): A secondary running-text color used inside long-form review and amenity copy where ink would feel too heavy.
- **Muted** (`{colors.muted}` — #6a6a6a): Sub-titles inside city link blocks ("Cottage rentals", "Villa rentals"), inactive product-tab labels, footer category sub-labels, "View all" links.
- **Muted Soft** (`{colors.muted-soft}` — #929292): Disabled link text. Used very sparingly.
- **Star Rating** (`{colors.star-rating}` — #222222): The same ink token — Airbnb's star icon and "4.81" rating numbers all render in ink rather than a yellow/gold color, which is a deliberate brand choice (yellow stars feel cheap in travel context).
- **On Primary** (`{colors.on-primary}` — #ffffff): White text on Rausch CTAs.

### Semantic
- **Error** (`{colors.primary-error-text}` — #c13515): Inline error text for form validation. Distinct from Rausch — slightly darker, more saturated red.
- **Error Hover** (`{colors.primary-error-text-hover}` — #b32505): Darkens on link hover.
- **Legal Link Blue** (`{colors.legal-link}` — #428bff): Inline links inside legal copy (Privacy, Terms). Only used inside the legal sub-band.

### Focus
- **Focus** (`{colors.focus}` — #222222): The focus ring tone. It is the same ink the system already uses for the focused `{component.text-input}` outline, which thickens to 2px ink on focus — so the ring is ink rather than a blue or Rausch glow, consistent with a palette that keeps Rausch for CTAs only. Measures **15.91:1** against `{colors.canvas}` (#ffffff) and **14.85:1** against `{colors.surface-soft}`, far above the 3:1 non-text minimum.
- **Focus Inner** (`{colors.focus-inner}` — #ffffff): A 1px white inner ring drawn inside the ink ring, so the ring survives on ink-filled elements (`{component.date-picker-day-selected}`) and over photography in `{component.property-card}`. White against ink measures 15.91:1.

### Scrim
- **Scrim** (`{colors.scrim}` — #000000 at 50% opacity): The global modal backdrop tone — date picker, login dialog, language picker. Stored as the base hex; opacity is applied at render time.

### Measured contrast, including the failures
Computed with WCAG 2.1 relative luminance from the hexes in this file:

| Pair | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 15.91:1 | 4.5 | pass |
| `{colors.ink}` on `{colors.surface-soft}` | 14.85:1 | 4.5 | pass |
| `{colors.body}` on `{colors.canvas}` | 10.53:1 | 4.5 | pass |
| `{colors.muted}` on `{colors.canvas}` | 5.41:1 | 4.5 | pass |
| `{colors.focus}` on `{colors.canvas}` | 15.91:1 | 3.0 | pass |
| `{colors.on-primary}` on `{colors.primary}` | **3.52:1** | 4.5 | **fail** |
| `{colors.hairline}` on `{colors.canvas}` | **1.36:1** | 3.0 | **fail** |

Two real failures, stated plainly rather than patched:

- **White on Rausch is 3.52:1.** Every primary CTA in the system (`{component.button-primary}`, `{component.button-pill-rausch}`, `{component.search-orb}`) is below the 4.5:1 body-text minimum. It clears 3:1, so it is defensible only for large text — 24px regular or 18.66px bold and above — and for the non-text icon in the search orb. `{component.button-primary}` labels are `{typography.button-md}` at 16px / 500, which is *not* large text, so that button fails AA as built. The nearest passing value is a token already in this palette: `{colors.primary-active}` (#e00b41) measures 4.89:1 with white. The hex is not changed here — #ff385c is Airbnb Rausch, and falsifying it would make the document wrong.
- **Hairlines are invisible to a low-vision user.** `{colors.hairline}` (#dddddd) is 1.36:1 on white, `{colors.hairline-soft}` (#ebebeb) is 1.19:1, and even `{colors.border-strong}` (#c1c1c1) only reaches 1.80:1. No border token in this system meets the 3:1 non-text minimum; roughly #959595 would be needed. Airbnb's hairline language genuinely does not pass, and anything built on these tokens must not rely on a border alone to convey structure or state.
- **Secondary reds and blues:** `{colors.primary-error-text}` (#c13515) passes at 5.54:1. `{colors.legal-link}` (#428bff) is 3.30:1 on white and fails for the 13–14px legal copy it is used on. `{colors.muted-soft}` (#929292) is 3.11:1 and is only used for disabled text, which WCAG exempts.

## Typography

### Font Family
The system runs **Airbnb Cereal VF** for everything — display, body, navigation, captions, microcopy. Fallbacks walk `Circular, -apple-system, system-ui, Roboto, "Helvetica Neue", sans-serif`. **Circular** is the historic in-house typeface still kept as the first non-variable fallback; system stacks back it up.

There is no separate display family. The variable font carries the entire scale.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.rating-display}` | 64px | 700 | 1.1 | -1px | Listing detail rating display ("4.81") |
| `{typography.display-xl}` | 28px | 700 | 1.43 | 0 | Homepage h1 ("Inspiration for future getaways") |
| `{typography.display-lg}` | 22px | 500 | 1.18 | -0.44px | Listing detail h1 ("Close to Fethiye Aliyah Bali Beach…") |
| `{typography.display-md}` | 21px | 700 | 1.43 | 0 | Section heads inside listing detail ("What this place offers") |
| `{typography.display-sm}` | 20px | 600 | 1.20 | -0.18px | Sub-section titles ("Things to know") |
| `{typography.title-md}` | 16px | 600 | 1.25 | 0 | City link block titles ("Wilmington", "Athens") |
| `{typography.title-sm}` | 16px | 500 | 1.25 | 0 | Footer column heads ("Support", "Hosting", "Airbnb") |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default running-text inside listing copy |
| `{typography.body-sm}` | 14px | 400 | 1.43 | 0 | Card meta lines, dates, prices, distance text |
| `{typography.caption}` | 14px | 500 | 1.29 | 0 | Search field segment labels ("Where", "When", "Who") |
| `{typography.caption-sm}` | 13px | 400 | 1.23 | 0 | Footer legal line ("© 2026 Airbnb, Inc.") |
| `{typography.badge}` | 11px | 600 | 1.18 | 0 | "Guest favorite" floating badge text |
| `{typography.micro-label}` | 12px | 700 | 1.33 | 0 | Card amenity micro-labels ("Inline 6") |
| `{typography.uppercase-tag}` | 8px | 700 | 1.25 | 0.32px (uppercase) | "NEW" badge on product nav tabs |
| `{typography.button-md}` | 16px | 500 | 1.25 | 0 | Primary CTA button labels |
| `{typography.button-sm}` | 14px | 500 | 1.29 | 0 | Pill button labels (category strip) |
| `{typography.link}` | 14px | 400 | 1.43 | 0 | Inline body links |
| `{typography.nav-link}` | 16px | 600 | 1.25 | 0 | Top product-nav labels (Homes, Experiences, Services) |

### Principles
Display weights stay modest. The homepage h1 at 28px / 700 is deliberately small — it tucks under the search bar so photography and the city-link grid carry visual hierarchy. The listing-detail h1 at 22px / 500 is even quieter; the listing photo banner does the work above it.

The single typographically loud moment in the entire system is the **rating display** (`{typography.rating-display}` — 64px / 700) on listing pages. That is the only place the system trusts type alone to carry hierarchy — rating numbers are a peak trust signal, so they get the loudest treatment.

### Note on Font Substitutes
If Airbnb Cereal VF and Circular are unavailable, **Inter** is the closest open-source substitute. Adjust display headlines down by ~2% in line-height to match Cereal's slightly tighter cap height; otherwise the proportions transfer cleanly.

## Layout

### Spacing System
- **Base unit:** 4px (with 2px micro-step).
- **Tokens:** `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.base}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 64px.
- **Section padding (vertical):** `{spacing.section}` (64px) for major page bands; tighter than typical SaaS marketing (80–96px) because marketplace pages need higher card density per scroll.
- **Card internal padding:** `{spacing.lg}` (24px) for `{component.host-card}` and `{component.reservation-card}`; `{spacing.base}` (16px) for property-card meta block; `{spacing.sm}` (8px) for caption / date-row gutters.
- **Gutters:** `{spacing.base}` (16px) between cards in the homepage city grid; `{spacing.lg}` (24px) inside footer column gutters; `{spacing.xs}` (4px) on dense category-strip dividers.

### Grid & Container
- **Max content width:** ~1280px centered on the homepage and editorial pages. Listing detail pages cap closer to 1080px to keep the photo banner and reservation rail readable.
- **City link grid (homepage footer):** 6-column grid at desktop with each cell housing a city name in `{typography.title-md}` and a category sub-label in `{typography.body-sm}` muted.
- **Listing detail:** 2-column with photo / amenity body on the left (~64% width) and a sticky reservation card (`{component.reservation-card}`) on the right (~32%).
- **Footer:** 3-column link list (Support / Hosting / Airbnb) at desktop, collapsing to 1-column on mobile.

### Whitespace Philosophy
The system gives editorial bands 64px of vertical breathing room but compresses card grids — property and city-link cards sit just 16px apart. The contrast is intentional: the page reads as "open hero, dense marketplace below," reinforcing the marketplace nature without overwhelming the visitor at the fold.

## Elevation & Depth

The system has essentially **one shadow tier** plus the flat baseline.

- **Flat (no shadow):** Body, hero, footer, all editorial bands — 95% of surfaces.
- **Card hover float:** `box-shadow: rgba(0, 0, 0, 0.02) 0 0 0 1px, rgba(0, 0, 0, 0.04) 0 2px 6px 0, rgba(0, 0, 0, 0.1) 0 4px 8px 0` — applied to property cards on pointer hover, the search bar at rest, and the dropdown menus (account menu, language picker, date picker). This is the single shadow definition in the entire system.
- **Modal scrim:** `{colors.scrim}` rendered at 50% opacity — the global modal backdrop. Used on date pickers, login dialogs, language picker.

There are no progressive elevation tiers — the system either has the one shadow or none. Depth comes from photography, the white-on-white surface separation, and rounded-corner clipping rather than from layered shadows.

Because there is exactly one shadow definition, elevation is expressed one consistent way throughout: a surface either carries that triple-layer shadow or it is flat. Nothing in this file raises a surface by tinting it, by adding a second shadow, or by stacking z-layers with different shadow strengths. The three surfaces that carry it — `{component.search-bar-pill}` at rest, hovered `{component.property-card}`, and the dropdown / `{component.reservation-card}` group — are therefore all on the same visual plane.

## Shapes

### Radius Ladder
| Token | Value | Used on |
|---|---|---|
| `{rounded.none}` | 0px | The body grid, `{component.product-tab-active}` and `{component.category-tab-active}` underline rules |
| `{rounded.xs}` | 4px | Smallest chip and carousel-dot geometry |
| `{rounded.sm}` | 8px | `{component.button-primary}`, `{component.button-secondary}`, `{component.text-input}` |
| `{rounded.md}` | 14px | `{component.property-card}`, `{component.property-card-photo}`, `{component.experience-card}`, `{component.host-card}`, `{component.reservation-card}` |
| `{rounded.lg}` | 20px | Larger panel corners |
| `{rounded.xl}` | 32px | Category-strip corner treatment |
| `{rounded.full}` | 9999px | `{component.search-bar-pill}`, `{component.search-orb}`, `{component.button-pill-rausch}`, `{component.icon-button-circle}`, `{component.icon-button-outline}`, `{component.guest-favorite-badge}`, `{component.new-tag}`, `{component.date-picker-day}` |

The ladder steps 0 · 4 · 8 · 14 · 20 · 32 · full. It is not a doubling scale and not linear — 14px exists specifically because property-card photo clipping needed a value between 8 and 20, and no entry in this file sits outside the ladder.

### Shape Rules
- **Rounder as it gets more interactive.** Static plates are the least rounded; a tapped thing is a pill or a circle. The two most-tapped elements, `{component.search-bar-pill}` and `{component.search-orb}`, are the roundest objects on the page.
- **Circles carry identity, not just affordance.** The Rausch orb, the wishlist heart, the icon buttons and the date-picker day cells are all full circles — the circle is a brand shape here, which is why `{rounded.full}` appears on nine component entries.
- **One hard corner only.** The page grid and the 2px active-tab underline rule are the only square geometry; everything else is rounded, per the Overview.
- **Clipping, not framing.** Photography is cut to `{rounded.md}` with no border and no inner shadow. The rounded corner is the frame.
- **Stroke weights:** 1px for every hairline border, 2px for the ink underline on `{component.product-tab-active}` and for the focused `{component.text-input}` outline. There is no third stroke weight.

## Components

### Buttons

**`button-primary`** — Rausch fill, white text, 8px radius, 14×24px padding, 48px height, weight 500. The most common CTA across the system: "Reserve", "Continue", "Search", account-flow primaries.

**`button-primary-active`** — The press state. Background flips to `{colors.primary-active}`. No transform, no shadow change.

**`button-primary-disabled`** — Pale Rausch tint at #ffd1da with white text. Cursor not-allowed.

**`button-secondary`** — White fill with ink text and a 1px ink outline. 8px radius. Used for "Save", "Cancel", and inverse CTAs over Rausch surfaces.

**`button-tertiary-text`** — Plain ink text, no surface, no border. Underlined on hover. Used for "Show more" type links and modal close labels.

**`button-pill-rausch`** — A pill-shaped Rausch CTA used on featured cells (e.g., "Become a host" sub-CTA) — 9999px radius, 10×20px padding, 14px label.

### Search Surface

**`search-bar-pill`** — The signature global search bar. White fill, 9999px radius, 64px height, 1px hairline 1px-shadow border. Internally divided by vertical hairline rules into `{component.search-field-segment}` cells (Where / When / Who). Each segment holds an uppercase caption label above a placeholder line in `{typography.caption}`.

**`search-orb`** — The circular Rausch orb terminating the right edge of the search bar. 48×48px, fully rounded, white magnifying-glass icon centered. The hottest single color moment on the homepage.

### Top Navigation

**`top-nav`** — White surface, 80px height, 1px bottom hairline. The Airbnb wordmark sits flush left, the three product tabs (Homes / Experiences / Services) sit in the dead center, and account utilities (host link, language globe, account menu) sit flush right.

**`product-tab-active`** — Ink label in `{typography.nav-link}`, 32px hand-illustrated icon, 2px ink underline rule beneath the icon-label pair.

**`product-tab-inactive`** — Muted label, illustrated icon, no underline. Becomes active on click.

**`new-tag`** — A tiny rounded-pill badge (`{rounded.full}`) anchored top-right of an icon, carrying the uppercase "NEW" label in `{typography.uppercase-tag}` (8px / 700 with 0.32px tracking, uppercase). Used on Experiences and Services to signal recency.

### Listing Cards

**`property-card`** — A photo-first card. 1:1 aspect-ratio image with `{rounded.md}` corner clipping, image carousel dots overlay, "Guest favorite" floating badge top-left (`{component.guest-favorite-badge}`), and a heart icon top-right (`{component.icon-button-circle}` in default outlined state, Rausch-filled when saved). Beneath the image: 4–5 lines of meta — title (`{typography.title-md}`), distance / dates (`{typography.body-sm}` muted), and price ("$X night") right-aligned.

**`property-card-photo`** — The photo plate itself, separated as a token because some surfaces (wishlist, search results) reuse just the photo without the meta block.

**`experience-card`** — A taller-aspect card (4:5) for experience listings. Same `{rounded.md}` clipping, floating "NEW" badge top-left, heart top-right, and a single-line title beneath.

**`guest-favorite-badge`** — White rounded pill (`{rounded.full}`) at 11px / 600 weight. Sits over the photo with the system's only shadow tier applied for elevation.

### Listing Detail

**`rating-display-card`** — The signature listing-detail moment. A 64px / 700 rating number ("4.81") flanked left and right by tiny laurel-wreath SVG ornaments. Beneath the rating: "Guest favorite" tagline and a row of ink stat columns. The largest typographic weight in the whole system.

**`amenity-row`** — A 1-column list of amenity icons + ink labels in `{typography.body-md}`. 12px row padding, no border between rows; section is closed by a 1px hairline divider above and below.

**`reviews-card`** — A 2-column grid of review excerpts. Each column holds an author row (avatar, name, date) above a 3-line excerpt with "Show more" tertiary link.

**`host-card`** — A white card with `{rounded.md}` rounding and 24px padding holding a host avatar, name, "Superhost" badge, response-rate stat, and a "Contact host" `{component.button-secondary}`.

**`reservation-card`** — The sticky right-rail card on listing detail pages. White surface, `{rounded.md}` rounding, 1px hairline border, 1px shadow tier elevation, 24px padding. Contains: nightly price (`{typography.display-md}` ink), date-range selector, guest-count stepper, "Reserve" primary CTA full-width, and a fee breakdown stack beneath in `{typography.body-sm}`.

### Date Picker

**`date-picker-day`** — A 40×40px circular cell carrying the day number in `{typography.body-sm}`. Default state is transparent fill, ink text.

**`date-picker-day-selected`** — Ink fill, white text, full circle (`{rounded.full}`). Range states between two selected days carry a `{colors.surface-soft}` lozenge background that connects them.

### Forms

**`text-input`** — White surface, 1px hairline outline, `{rounded.sm}` 8px radius, 56px height, 14×12px padding. Stacked label above (in `{typography.caption}` muted), placeholder text in `{typography.body-md}` muted. On focus, the border thickens to 2px ink and the border color flips to `{colors.ink}` — no glow, no ring.

### Footer

**`footer-light`** — White surface (matches the page canvas — Airbnb has no contrast footer), 48×80px padding. Three columns of link blocks (Support / Hosting / Airbnb), separated by generous 24px gutters. Each column heads with a `{typography.title-sm}` ink label and stacks `{component.footer-link}` rows in `{typography.body-sm}` ink.

**`legal-band`** — A bottom strip beneath the footer columns carrying the copyright line, language picker (globe icon + "English (US)" link), currency picker, and social icons (Facebook, X, Instagram). All text in muted `{colors.muted}` at `{typography.caption-sm}`.

### States per Component

Hover colour values are not documented (see Known Gaps); this table names which states each entry *has*, using the tokens already defined above. Every interactive entry takes the focus ring described under Colors → Focus.

| Component | States |
|---|---|
| `{component.button-primary}` | default, hover (elevation only), focus-visible, pressed (`{component.button-primary-active}`), disabled (`{component.button-primary-disabled}`), loading (label swaps to an in-button spinner, width held) |
| `{component.button-secondary}` | default, hover, focus-visible, pressed, disabled (outline drops to `{colors.border-strong}`) |
| `{component.button-tertiary-text}` | default, hover (underline), focus-visible, pressed, disabled |
| `{component.button-pill-rausch}` | default, hover, focus-visible, pressed |
| `{component.search-orb}` | default, hover, focus-visible, pressed, loading (spinner replaces the glass icon while results resolve) |
| `{component.search-bar-pill}` | default (collapsed), focus-visible, expanded/selected (one `{component.search-field-segment}` active), error (invalid date range, text in `{colors.primary-error-text}`) |
| `{component.search-field-segment}` | default, hover, focus-visible, selected, error |
| `{component.product-tab-active}` / `{component.product-tab-inactive}` | two states only: selected and unselected, plus focus-visible on the link |
| `{component.category-tab-active}` | selected, unselected, hover, focus-visible |
| `{component.property-card}` | default, hover (the signature elevation lift), focus-visible (ring on the whole card), pressed, selected (saved — heart fills Rausch), loading (skeleton plate at `{colors.surface-soft}`) |
| `{component.property-card-photo}` | default, loading (skeleton), carousel-advancing |
| `{component.experience-card}` | same set as `{component.property-card}` |
| `{component.icon-button-circle}` (wishlist heart) | default, hover, focus-visible, pressed, selected (Rausch fill), loading (save in flight), disabled |
| `{component.icon-button-outline}` | default, hover, focus-visible, pressed, disabled |
| `{component.date-picker-day}` | default, hover, focus-visible, pressed, selected (`{component.date-picker-day-selected}`), in-range, disabled (unavailable night, `{colors.muted-soft}`) |
| `{component.text-input}` | default, hover, focus-visible (2px `{colors.focus}` outline), filled, disabled (`{colors.surface-soft}` fill), error (`{colors.primary-error-text}` helper text) |
| `{component.reservation-card}` | default, focus-visible within, loading (price recalculating), error (date conflict) |
| `{component.host-card}` | default and focus-visible on its contained controls — the card itself is static |
| `{component.reviews-card}` | default, loading (excerpt skeletons), expanded via the "Show more" tertiary link |
| `{component.guest-favorite-badge}`, `{component.new-tag}`, `{component.rating-display-card}`, `{component.amenity-row}`, `{component.legal-band}` | single state — these are display-only and have no interaction |
| `{component.footer-link}` | default, hover (underline), focus-visible, pressed |
| `{component.top-nav}`, `{component.category-strip}`, `{component.footer-light}` | containers; states live on the controls inside them |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or curve below was extracted from Airbnb; they are derived from the **Playful** profile in `theme-audit/SPEC.md` §5, chosen because this is a saturated, illustration-led consumer identity (hand-drawn 32px product glyphs, a single hot Rausch accent, pill and circle geometry throughout). Treat every value as a recommendation for building in this style, not as documentation of Airbnb's real code.

All values come from the `motion:` token block: `{motion.duration-instant}` 80ms · `{motion.duration-fast}` 120ms · `{motion.duration-base}` 200ms · `{motion.duration-slow}` 320ms · `{motion.duration-emphasis}` 480ms · `{motion.ease-standard}` · `{motion.ease-enter}` (overshoot, the Playful signature) · `{motion.ease-exit}` · `{motion.stagger-step}` 60ms.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Card hover (`{component.property-card}`) — the signature interaction | `{motion.duration-base}` | `{motion.ease-standard}` | `transform: scale(1.02)` plus the single shadow tier fading in via `opacity` on a pseudo-element | No scale. The shadow still fades in over `{motion.duration-fast}`, so hover remains perceivable |
| Button / link hover | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` on the fill overlay | Unchanged — already opacity-only |
| Press (`{component.button-primary}`, `{component.search-orb}`, wishlist heart) | `{motion.duration-instant}` down, `{motion.duration-fast}` release | `{motion.ease-enter}` on release for a small pop | `transform: scale(0.96)` down, overshoot to `scale(1.0)` on release; heart save pops to `scale(1.15)` then settles | No scale. The Rausch fill change is instant |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring; the ring's own geometry does not move | Ring appears with no transition |
| Page / route transition | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` 0→1 with `transform: translateY(8px)` on the content block only; photography never shifts | Cross-fade at 120ms, no travel |
| Modal / drawer (date picker, login) | `{motion.duration-slow}` enter, `{motion.duration-base}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | Scrim `opacity` 0→0.5; panel `transform: scale(0.96)→1` on desktop, `translateY(100%)→0` sheet on mobile | Scrim and panel fade only, 150ms, no scale and no slide |
| Dropdown (account menu, language picker) | `{motion.duration-fast}` enter, `{motion.duration-instant}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` plus `transform: scale(0.98)→1` from the trigger corner | Opacity only, 120ms |
| Toast | `{motion.duration-base}` enter, `{motion.duration-fast}` exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateY(12px)→0` with `opacity` | Fade only, 150ms, and the auto-dismiss timer is extended |
| List enter (search-results grid, category strip) | `{motion.duration-base}` per item, `{motion.stagger-step}` 60ms apart, capped at 8 items | `{motion.ease-enter}` | `opacity` 0→1 with `transform: translateY(12px)` | No stagger and no travel; the whole grid fades in once at 150ms |
| List exit (filter change, removed wishlist item) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` 1→0 with `transform: scale(0.98)`; remaining items reposition without a transition | Instant removal |
| Loading | `{motion.duration-emphasis}` 480ms loop | `{motion.ease-standard}`, linear for the spinner | Skeleton plate `opacity` pulse 1→0.6 on `{colors.surface-soft}`; `{component.search-orb}` spinner rotates by `transform` | Skeleton pulse frozen at its mid value; spinner reduced to a static indicator with text status |

### Motion Rules
- Only `transform` and `opacity` are used as transition targets. Layout-triggering properties (`width`, `height`, `top`, `left`, `margin`) are never transitioned — a card lift is a `scale`, not a size change, and the mobile sheet is a `translateY`, not a height change.
- Every exit is shorter than its matching entrance (modal 320→200ms, dropdown 120→80ms, toast 200→120ms, list 200→120ms).
- Nothing runs on first paint. Photography and above-the-fold copy render immediately; the list-enter stagger applies only to grids fetched after the first paint, such as a filter or search result change.
- The only looping motion is the loading state. There is no brand ambience loop in this system.
- Overshoot is the Playful signature and is confined to press release, the wishlist-heart pop, and panel entrances. It is never applied to an exit, where it would read as indecision.

### `@media (prefers-reduced-motion: reduce)`
**Removed:** all `scale` (card hover lift, press pop, heart pop, modal and dropdown scale), all travel (`translateY` on page transitions, toasts, list enter, the mobile sheet), the `{motion.stagger-step}` sequencing, and the skeleton pulse loop.
**Kept:** every `opacity` fade, clamped to 150ms or less; the focus ring, which appears with no transition; the Rausch fill and selected-state colour changes, which are instant; and a static loading indicator with a text status in place of the spinner. No state becomes unperceivable — anything that was communicated by movement is also communicated by the shadow tier, a colour change, or text.

## Accessibility

### Measured Contrast
Full table under Colors → "Measured contrast, including the failures". The summary:

| Pair | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 15.91:1 | 4.5 | pass |
| `{colors.ink}` on `{colors.surface-soft}` | 14.85:1 | 4.5 | pass |
| `{colors.muted}` on `{colors.canvas}` | 5.41:1 | 4.5 | pass |
| `{colors.muted}` on `{colors.surface-soft}` | 5.05:1 | 4.5 | pass |
| `{colors.body}` on `{colors.canvas}` | 10.53:1 | 4.5 | pass |
| `{colors.on-dark}` on `{colors.ink}` (selected day cell) | 15.91:1 | 4.5 | pass |
| `{colors.focus}` on `{colors.canvas}` | 15.91:1 | 3.0 | pass |
| `{colors.on-primary}` on `{colors.primary}` | 3.52:1 | 4.5 | **fail** |
| `{colors.hairline}` on `{colors.canvas}` | 1.36:1 | 3.0 | **fail** |
| `{colors.legal-link}` on `{colors.canvas}` | 3.30:1 | 4.5 | **fail** (13–14px legal copy) |
| `{colors.ink}` on `{colors.primary-disabled}` | 11.66:1 | — | pass, if a disabled CTA is re-inked |

Two of these are brand-level failures, not documentation errors: white on Rausch, and the hairline family. Neither hex is altered here. A disabled CTA (`{component.button-primary-disabled}`) is worse again — white on #ffd1da measures **1.37:1** — which is why disabled label text should be `{colors.ink}` (11.66:1) rather than `{colors.on-primary}`, and why disabled state must never be conveyed by colour alone.

### Focus Ring Visibility
`{colors.focus}` (#222222), 2px, offset 2px, with a 1px `{colors.focus-inner}` inner ring. On every surface this file defines:

| Surface | Ring contrast | Note |
|---|---|---|
| `{colors.canvas}` #ffffff | 15.91:1 | pass |
| `{colors.surface-soft}` #f7f7f7 | 14.85:1 | pass |
| `{colors.surface-strong}` #f2f2f2 | 14.21:1 | pass |
| `{colors.primary}` #ff385c (CTA) | 4.52:1 | pass |
| `{colors.ink}` fill (`{component.date-picker-day-selected}`) | 1.00:1 | ink-on-ink is invisible — the white inner ring carries it here, at 15.91:1 |
| Over photography (`{component.property-card-photo}`) | not computable | a hex-to-hex ratio cannot be computed against an image; the white inner ring is what guarantees the ring stays visible on a light photo |

The ring is drawn on `:focus-visible` only, so mouse users never see it. The existing 2px-ink input focus treatment described under `{component.text-input}` is the same ring, applied as a border rather than an outline.

### Minimum Tap Target
Per the Touch Targets list under Responsive Behavior: `{component.button-primary}`, `{component.button-secondary}` and `{component.search-orb}` are 48×48px; `{component.date-picker-day}` is 40×40px; `{component.icon-button-circle}` (the wishlist heart) is 32×32px, which is below the 44×44px AA target-size guidance and is the smallest interactive element in the system. The documented 12px padding around it is a spacing claim, not a measured hit area — whether the real hit target reaches 44px cannot be verified from this document. No tap-target size here is measured from a rendered page.

### Reduced Motion
See Motion & Animation → `@media (prefers-reduced-motion: reduce)`. All travel, scale and stagger are removed; opacity fades stay at 150ms or less; the loading pulse freezes. Because the motion system is prescribed rather than extracted, this is the recommended behaviour for a build in this style, not a record of Airbnb's own.

### Known Accessibility Limits of This Audit
Keyboard order, screen-reader labelling, visible overflow, the real hit areas and the behaviour of the image carousel cannot be evaluated from a document. They are untested here.

## Do's and Don'ts

### Do
- **Do keep Rausch scarce.** One or two `{colors.primary}` moments per page — the CTA and the search orb. The system reads as 90% white and ink; that ratio is the brand.
- **Do set Rausch CTA labels large or re-colour them.** White on #ff385c is 3.52:1, which only clears 3:1 for large text. If the label must stay 16px (`{typography.button-md}`), use `{colors.primary-active}` (#e00b41, 4.89:1) as the fill.
- **Do let photography carry hierarchy.** Display type stays at 22–28px in weight 500–700 because the image does the work. Raising headline weight to fix a weak page is the wrong lever.
- **Do round every interactive element.** `{rounded.sm}` for buttons and inputs, `{rounded.md}` for cards and photos, `{rounded.full}` for anything tapped or circular.
- **Do pair every hairline with something else.** No border token reaches 3:1 on white, so structure must also come from spacing, a `{colors.surface-soft}` fill, or the single shadow tier.
- **Do keep the one shadow tier.** Hovered cards, the search bar and the dropdown group share it; that is the system's only elevation.
- **Do use `{colors.ink}` for the focus ring,** with the `{colors.focus-inner}` white inner ring, so focus survives on ink fills and over photos.
- **Do hold the stagger cap.** List enter staggers at `{motion.stagger-step}` across at most 8 items; beyond that the grid fades in as a block.

### Don't
- **Don't introduce a second accent.** `{colors.luxe}` and `{colors.plus}` are sub-brand only, and `{colors.legal-link}` belongs to the legal band. A new brand colour breaks the single-voltage rule.
- **Don't darken Rausch to pass contrast and still call it Rausch.** #ff385c is the brand hex; change the type size or use the documented `{colors.primary-active}` instead, and say which you did.
- **Don't add elevation tiers.** A second or third shadow turns a photography-led page into a card-stack UI.
- **Don't use a yellow or gold star.** `{colors.star-rating}` is ink (#222222) by deliberate choice.
- **Don't carry white text on `{colors.primary-disabled}`.** It measures 1.37:1. Use ink, plus a non-colour disabled cue.
- **Don't ship a hard corner.** Only the body grid and the 2px active-tab underline are square.
- **Don't invent a dark mode.** This file documents no dark canvas; the public web has none.
- **Don't transition layout properties.** A card lift is `transform: scale`, not a size change; the mobile sheet is `translateY`, not a height change.
- **Don't put overshoot on an exit.** `{motion.ease-enter}` is for entrances and press release only.
- **Don't let motion delay the fold.** Nothing animates on first paint; the stagger belongs to content fetched afterwards.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to logo + hamburger; product tabs hide behind a sheet; search bar collapses to a single tappable pill; property cards stack 1-up; city grid 1-column; listing detail collapses reservation card to a sticky bottom bar. |
| Tablet | 744–1128px | Top nav keeps product tabs but search bar narrows; property cards 2-up; city grid 2–3 column; reservation card stays sticky right-rail at narrower width. |
| Desktop | 1128–1440px | Full top nav with three product tabs centered; search bar at full pill width with all 3 segments visible; property cards 4-up; city grid 6-column; listing detail 2-column with reservation rail. |
| Wide | > 1440px | Content width caps at 1440px on listing/search pages and ~1280px on editorial; gutters absorb the rest. |

### Touch Targets
- Primary CTAs at minimum 48×48px (above WCAG AAA).
- Search orb is 48×48px circular — the most-tapped element on the page.
- Heart save button is 32×32px circular — borderline for AAA but compensated by a generous 12px padding inside the photo card.
- Date-picker day cells are 40×40px circular.

### Collapsing Strategy
- Top product tabs collapse into a hamburger sheet below 744px.
- Search bar's 3 segments collapse into a single-tap entry that opens a full-screen search overlay on mobile.
- Property and city-link grids drop column counts cleanly at each breakpoint — never reflow rows; always reduce columns.
- Reservation card on listing detail switches from sticky right-rail to a sticky bottom bar on mobile, carrying just the "Reserve" CTA + nightly price summary.

## Iteration Guide

Order to work in when building on this file:

1. **Start from white and ink.** `{colors.canvas}` and `{colors.ink}` carry the page; place content and spacing before any colour decision.
2. **Spend Rausch once.** Pick the single primary action per view and give it `{colors.primary}`. If a second Rausch element appears, one of them is not primary.
3. **Set the radius from the ladder, not by eye.** `{rounded.sm}` controls, `{rounded.md}` cards and photos, `{rounded.full}` anything tapped or circular.
4. **Keep display type modest.** `{typography.display-xl}` tops out at 28px. If the page feels weak, the image is wrong, not the type.
5. **Pick the shadow or go flat.** One tier, no in-between.
6. **Add the focus ring before the hover state.** `{colors.focus}` plus `{colors.focus-inner}`; hover is decoration, focus is access.
7. **Apply motion last,** from the `motion:` tokens, and keep the card-hover scale small — `{motion.duration-base}` at `scale(1.02)`. Re-read the reduced-motion rule before shipping.
8. **Re-measure the pairs you changed.** Any new fill needs its own contrast number recorded, not estimated.

## Known Gaps

- **Hover state colors:** intentionally not documented per the global no-hover policy — Airbnb's actual `:hover` styling for property cards is a subtle elevation lift, but precise extraction is unreliable.
- **Loading states / skeleton screens:** not visible on the extracted surfaces.
- **Map view styling:** the search-results map uses Mapbox-tinted tiles with custom Rausch markers; not captured here.
- **Form input error states:** error text color (`{colors.primary-error-text}`) is documented, but the full input outline + helper-text combination on validation failure was not visible in the captured surfaces.
- **Sub-brand palettes:** Luxe (`{colors.luxe}`) and Plus (`{colors.plus}`) are documented as tokens, but their full sub-system (typography overrides, surface treatment) lives on separate sub-domains and is not captured here.
