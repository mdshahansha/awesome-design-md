---
version: alpha
name: Jobright Analysis
description: An analysis of Jobright's design language — an AI job-hunting platform built on an energetic spring-mint green against black and white, with pale-mint section bands carrying the page rhythm. Bold condensed Titillium Web display headings pair with a clean Inter UI, and the CTA system runs on high-contrast pill buttons — black pills for primary actions, a mint-green pill for the signature accent. Rounded product-mockup cards, a scrolling black job ticker, and generous whitespace give it a friendly, high-energy startup feel.

colors:
  primary: "#00f0a0"
  on-primary: "#000000"
  ink: "#000000"
  on-dark: "#ffffff"
  canvas: "#ffffff"
  canvas-mint: "#ecffe0"
  muted: "#86909c"
  hairline: "#e5e7eb"
  surface-soft: "#f2f4f5"
  # ── Prescribed accessible parallels (not extracted from the live site) ──
  focus: "#008f66"
  muted-strong: "#616a75"
  hairline-strong: "#7a8290"
  primary-deep: "#00664a"

typography:
  display:
    fontFamily: Titillium Web
    fontSize: 80px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  heading-1:
    fontFamily: Titillium Web
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-2:
    fontFamily: Titillium Web
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  heading-3:
    fontFamily: Titillium Web
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  heading-4:
    fontFamily: Titillium Web
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  button:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 28px
  pill-nav: 18px
  pill: 36px
  card: 40px
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
  duration-instant: 70ms
  duration-fast: 130ms
  duration-base: 200ms
  duration-slow: 320ms
  duration-emphasis: 450ms
  ease-standard: cubic-bezier(0.3, 0, 0.2, 1)
  ease-enter: cubic-bezier(0.17, 0.89, 0.32, 1.28)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 60ms
  duration-reduced: 130ms

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md}"
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    padding: "{spacing.sm} {spacing.section}"
  button-primary-sm:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.pill-nav}"
    padding: "{spacing.xxs} {spacing.md}"
  button-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.xxl}"
  button-dark-square:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  hero:
    backgroundColor: "{colors.canvas-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.display}"
    padding: "{spacing.section}"
  video-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.md}"
  stat-item:
    backgroundColor: "{colors.canvas-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-3}"
  job-ticker:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md}"
  feature-band:
    backgroundColor: "{colors.canvas-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-2}"
    padding: "{spacing.section}"
  feature-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  score-ring:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.heading-4}"
    rounded: "{rounded.full}"
    size: 64px
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  testimonial-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-4}"
    padding: "{spacing.section}"
  faq-item:
    backgroundColor: "{colors.canvas-mint}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  cta-band:
    backgroundColor: "{colors.canvas-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-2}"
    padding: "{spacing.section}"
  job-search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses caption eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.sm} {spacing.md}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"

---


## Overview

Jobright is the marketing site of an AI job-hunting platform, and its design radiates startup energy. The system is anchored by a single electric accent — a spring-mint green (`{colors.primary}` — #00f0a0) — set against crisp black (`{colors.ink}`) and white (`{colors.canvas}`). The signature move is a pale-mint section band (`{colors.canvas-mint}` — #ecffe0) that carries most of the page: heroes, feature blocks, FAQ, and the closing CTA all sit on this soft green wash, punctuated by full-black bands for the scrolling job ticker and a featured testimonial.

The type system pairs a bold, slightly condensed Titillium Web (`{typography.display}`) for big confident headlines with a clean Inter (`{typography.body-md}`) for UI and body copy. Headlines run large and heavy; body stays light and readable. The overall feel is friendly and high-energy rather than corporate — rounded product-mockup cards, emoji accents, and generous whitespace keep it approachable.

The CTA system is built on high-contrast pill buttons. Primary actions use a **black pill** (`{colors.ink}` fill, white label) at a large 28px radius; the brand's signature accent button is a **mint-green pill** (`{colors.primary}` fill, black label, thin black border) at a rounder 36px. Product features are demonstrated in white mockup cards with pronounced 40px asymmetric corners, floating over the mint bands. Elevation is light — a hairline or a whisper-soft shadow, never heavy blur.

**Key Characteristics:**
- A single electric accent: spring-mint `{colors.primary}` owns the logo, links, the signature green pill, and every highlight — used against black and white with conviction.
- Pale-mint section bands (`{colors.canvas-mint}`) carry the page rhythm, alternating with white and full-black bands.
- Dual pill-button system: black pills (`{rounded.xl}`) for primary CTAs, a mint-green pill (`{rounded.pill}`) for the signature accent action.
- Bold Titillium Web display type (`{typography.display}`) over a light, clean Inter body (`{typography.body-lg}`) — confident headlines, quiet copy.
- Rounded product-mockup cards with a distinctive 40px asymmetric corner (`{rounded.card}`), floating over the mint bands to demo AI features.
- Page rhythm: mint hero → mint stats → white job-hub → black scrolling ticker → alternating mint feature bands → white testimonials → black featured quote → mint FAQ → mint CTA → white footer.

## Colors

Source pages analyzed: the homepage, the job-referral page, the employers page, the about page, and the tnt page. The palette is consistent across all five — a tightly controlled mint / black / white system.

### Brand & Accent
- **Spring Mint** (`{colors.primary}` — #00f0a0): the brand's one electric accent. Colors the logo mark, links, the signature green pill button, score highlights, and inline emphasis.
- **On-Primary** (`{colors.on-primary}` — #000000): black label used on top of the mint-green button, where dark-on-mint reads with maximum punch.

### Surface
- **Canvas** (`{colors.canvas}` — #ffffff): default page and card background.
- **Mint Canvas** (`{colors.canvas-mint}` — #ecffe0): the pale spring-mint band that carries the hero, feature blocks, FAQ, and CTA sections — the system's dominant surface.
- **Soft Surface** (`{colors.surface-soft}` — #f2f4f5): light gray utility fill for inset panels and inputs.
- **Hairline** (`{colors.hairline}` — #e5e7eb): 1px card and divider borders. Measured at 1.24:1 on `{colors.canvas}`, so it is a **decorative** divider only — it is not strong enough to be the sole boundary of a control. Use `{colors.hairline-strong}` where the border is the only thing defining an interactive edge.

### Text
- **Ink** (`{colors.ink}` — #000000): headings, body text, and the fill of every black pill button and dark band.
- **Muted** (`{colors.muted}` — #86909c): secondary text, captions, and footer links.
- **On Dark** (`{colors.on-dark}` — #ffffff): text set on the black ticker and testimonial bands.

### Prescribed Accessible Parallels (not extracted)

The four tokens below were **not measured from the live site**. They are added so a
build on this document can meet WCAG 2.1 AA without altering an extracted brand
hex. The brand values above stay frozen and keep their documented roles.

- **Focus** (`{colors.focus}` — #008f66): the focus ring. Jobright has three surface
  polarities (white, pale mint, full black), so one mid-luminance deep-mint ring serves
  all of them rather than a light/dark pair: 4.10:1 on `{colors.canvas}`, 3.90:1 on
  `{colors.canvas-mint}`, 3.72:1 on `{colors.surface-soft}`, 5.12:1 on `{colors.ink}`.
  It is the same hue family as `{colors.primary}`, so the ring still reads as Jobright.
- **Muted Strong** (`{colors.muted-strong}` — #616a75): accessible replacement for
  `{colors.muted}` wherever muted grey carries real secondary text below 18px —
  footer links, captions, metadata. 5.49:1 on `{colors.canvas}`.
- **Hairline Strong** (`{colors.hairline-strong}` — #7a8290): control boundary where the
  border is the only edge — text inputs, select controls, the job-search bar. 3.62:1 on
  `{colors.canvas}`.
- **Primary Deep** (`{colors.primary-deep}` — #00664a): deep-mint replacement for
  `{colors.primary}` wherever mint is used as *text* on a light surface — inline links,
  the score numeral. 7.00:1 on `{colors.canvas}`. Mint stays the brand's accent for
  fills, strokes and marks on black.

## Typography

### Font Family
Two families do the work. **Titillium Web** — a bold, slightly condensed humanist sans — carries every display headline and section title, giving the page its confident, high-energy voice. **Inter** handles all body copy, UI labels, buttons, and captions, keeping dense content clean and legible. The contrast between heavy condensed headlines and light, airy body copy is the system's core typographic tension.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display}` | 80px | 700 | 1.05 | -1px | Largest hero / section headline (Titillium Web) |
| `{typography.heading-1}` | 60px | 700 | 1.1 | -0.5px | Primary section headings (Titillium Web) |
| `{typography.heading-2}` | 48px | 700 | 1.15 | 0 | Feature-band headings (Titillium Web) |
| `{typography.heading-3}` | 38px | 700 | 1.2 | 0 | Stat numbers, sub-headings (Titillium Web) |
| `{typography.heading-4}` | 32px | 600 | 1.25 | 0 | Card titles, quotes (Titillium Web) |
| `{typography.body-lg}` | 18px | 300 | 1.6 | 0 | Lead paragraphs (Inter light) |
| `{typography.body-md}` | 16px | 500 | 1.6 | 0 | Default body copy (Inter) |
| `{typography.body-sm}` | 14px | 500 | 1.5 | 0 | Dense body, ticker, footer (Inter) |
| `{typography.button}` | 16px | 600 | 1 | 0 | Button labels (Inter) |
| `{typography.nav-link}` | 14px | 600 | 1.4 | 0 | Top-nav links (Inter) |
| `{typography.caption}` | 13px | 500 | 1.4 | 0 | Fine print, metadata (Inter) |

### Principles
Headlines are big, heavy, and condensed for maximum confidence; body copy stays light (Inter 300) and roomy. The pairing lets marketing headlines shout while product detail stays quiet and scannable.

### Note on Font Substitutes
Both Titillium Web and Inter are open-source Google fonts — use them directly. If a fallback is needed, Titillium Web degrades to a condensed sans (e.g. "Arial Narrow", system-ui) and Inter to Helvetica/Arial with no metric adjustment.

## Layout

### Spacing System
- **Base unit**: 8px.
- **Tokens (front matter)**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- Feature cards sit at `{spacing.lg}`; full-width bands breathe at `{spacing.section}`; the large primary pill uses a wide `{spacing.sm} {spacing.section}` padding.

### Grid & Container
Content is centered in a ~1200px container (the dominant breakpoint in a wide 1600→575px ladder). Feature blocks run as two-column rows — copy + CTA on one side, a product-mockup card on the other — alternating sides down the page and collapsing to stacked single column on narrow screens. Testimonials run 3-up; the footer job-search bar runs as a single horizontal control row.

### Whitespace Philosophy
Whitespace is generous and band-driven. The page groups content by alternating full-width color bands — pale mint for marketing sections, white for neutral content, full black for the ticker and featured quote — with roomy vertical padding that keeps the high-energy type from feeling crowded.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | 1px `{colors.hairline}` border or none | Bands, list rows, inputs |
| 1 — Hairline | `rgba(0,0,0,0.5)` 0px 0px 0px 0.5px inset | Bordered chips and outlined controls |
| 2 — Soft float | whisper-soft drop shadow | Product-mockup cards floating over mint bands |

Elevation is deliberately light — the design relies on color-band contrast and rounded card shapes rather than heavy shadow. Depth comes from the mockup cards lifting off the mint bands and the full-black bands punctuating the page.

### Decorative Depth
There is no gradient system; depth is band-and-card based. Playful accents — emoji, a pink heart, hand-drawn illustration marks — add lightweight texture, and the scrolling black job ticker adds motion-based depth between static sections.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.sm}` | 12px | Square dark button, small chips, inputs |
| `{rounded.md}` | 16px | Cards, tab lists, video card |
| `{rounded.lg}` | 24px | Testimonial and content cards |
| `{rounded.xl}` | 28px | Primary black CTA pill (large) |
| `{rounded.pill-nav}` | 18px | Compact nav pill button |
| `{rounded.pill}` | 36px | Signature mint-green pill button |
| `{rounded.card}` | 40px | Product-mockup feature cards (asymmetric 0/40/40 corner) |
| `{rounded.full}` | 9999px | Avatars, score rings, footer search bar |

### Photography Geometry
Product mockups sit inside rounded white cards at 16–40px corners (`{rounded.md}` / `{rounded.card}`), often with one asymmetric sharp corner for a distinctive silhouette. Avatars and circular score rings are fully round (`{rounded.full}`). The hero video is a rounded card (`{rounded.md}`).

## Components

### Buttons

**`button-primary`** — the large black pill CTA ("Try For Free", "Find My Matches", "Start Autofilling")
- Background `{colors.ink}`, white label `{colors.on-dark}`, type `{typography.button}`, rounded `{rounded.xl}`, wide padding `{spacing.sm} {spacing.section}`.
- States — **default**: solid black fill. **hover**: `scale(1.02)` over `{motion.duration-fast}`. **focus-visible**: 2px `{colors.focus}` ring at 2px offset. **pressed** (active): `scale(0.97)` at `{motion.duration-instant}`. **disabled**: 40% opacity, pointer-events off, no ring. **loading**: label swapped for a mint spinner, width held, control stays focusable with `aria-busy`. **selected**: not applicable — this is an action, not a toggle. **error**: not applicable; form-level errors surface on the input, not the CTA.

**`button-primary-sm`** — the compact black nav pill ("Join Now")
- Background `{colors.ink}`, white label `{colors.on-dark}`, type `{typography.nav-link}`, rounded `{rounded.pill-nav}`, padding `{spacing.xxs} {spacing.md}`.
- States — same ladder as `{component.button-primary}`: **default**, **hover** (`scale(1.02)`), **focus-visible** (2px `{colors.focus}` ring, 2px offset), **pressed** (`scale(0.97)`), **disabled** (40% opacity), **loading** (mint spinner, `aria-busy`). **selected** and **error** are not applicable.

**`button-green`** — the signature mint-green pill ("Try For Free" on the closing CTA)
- Background `{colors.primary}`, black label `{colors.on-primary}`, 1px black border `{colors.ink}`, type `{typography.button}`, rounded `{rounded.pill}`, padding `{spacing.sm} {spacing.xxl}`.
- States — **default**: mint fill, black label (13.97:1). **hover**: `scale(1.02)`, border stays 1px `{colors.ink}`. **focus-visible**: 2px `{colors.focus}` ring drawn at 2px offset so it lands on the band behind the pill, never on the mint fill (the ring measures only 2.73:1 against `{colors.primary}` itself). **pressed** (active): `scale(0.97)`. **disabled**: 40% opacity. **loading**: black spinner on mint, `aria-busy`. **selected** and **error** are not applicable.

**`button-dark-square`** — a squarer black utility button
- Background `{colors.ink}`, white label `{colors.on-dark}`, type `{typography.button}`, rounded `{rounded.sm}`, padding `{spacing.sm} {spacing.md}`.
- States — **default**, **hover**, **focus-visible**, **pressed**, **disabled**, **loading** as `{component.button-primary}`; **selected** and **error** are not applicable.

### Cards & Containers

**`feature-card`** — the white product-mockup card demoing an AI feature
- Background `{colors.canvas}`, type `{typography.body-md}`, rounded `{rounded.card}` (40px, with one asymmetric sharp corner), padding `{spacing.lg}`, floating on a soft shadow over the mint band.
- States — **default** and **hover** (`translateY(-2px)` at `{motion.duration-base}`) for the whole card; where the card is a link it also carries **focus-visible** (2px `{colors.focus}` ring, 2px offset) and **pressed** (`scale(0.99)`). **loading**: skeleton blocks at `{colors.surface-soft}`, no shimmer travel. **disabled**, **selected** and **error** are not applicable — this is a static demo surface.

**`video-card`** — the rounded hero video frame
- Background `{colors.canvas}`, 1px `{colors.ink}` border, rounded `{rounded.md}`.
- States — genuinely three: **default** (poster frame), **hover** (play affordance at full opacity, `scale(1.03)` on the play mark), **focus-visible** (2px `{colors.focus}` ring, 2px offset). **loading**: poster held with a mint spinner. **pressed**, **disabled**, **selected** and **error** are not applicable.

**`testimonial-card`** — a user-love quote card
- Background `{colors.canvas}`, 1px `{colors.hairline}` border, rounded `{rounded.lg}`, padding `{spacing.lg}`, with an avatar, name, and quote.
- States — genuinely two: **default** and **hover** (`translateY(-2px)`). In a carousel it adds **selected** (the active slide, 1px `{colors.hairline-strong}` border plus a mint under-mark) and **focus-visible** on its arrows. **pressed**, **disabled**, **loading** and **error** are not applicable.

**`score-ring`** — the circular AI-match score indicator
- White surface `{colors.canvas}`, mint value `{colors.primary}` in `{typography.heading-4}`, rounded `{rounded.full}`, size 64px. **The real brand fails AA here**: mint #00f0a0 on white measures 1.50:1, far below the 3.0:1 that 32px large text requires. The mint is legible as the ring *stroke* against white, not as the numeral. Build the numeral in `{colors.primary-deep}` (7.00:1) or `{colors.ink}` (21.00:1) and keep `{colors.primary}` for the arc.
- States — genuinely two value states plus one transient: **default** (score rendered), **loading** (arc at `{colors.surface-soft}`, numeral suppressed, `aria-busy`), and **error** (arc at `{colors.hairline-strong}`, an em-dash in place of the score). **hover**, **focus-visible**, **pressed**, **disabled** and **selected** are not applicable — the ring is a read-only indicator.

### Inputs & Forms

**`text-input`** — search and form fields
- Background `{colors.canvas}`, 1px `{colors.hairline}` border, text `{colors.ink}`, type `{typography.body-md}`, rounded `{rounded.sm}`, padding `{spacing.sm} {spacing.md}`. The extracted `{colors.hairline}` border is the field's only boundary and measures 1.24:1 on `{colors.canvas}`; draw the resting border in `{colors.hairline-strong}` (3.62:1) so the control has a perceivable edge.
- States — **default** (1px `{colors.hairline-strong}`), **hover** (border `{colors.ink}`), **focus-visible** (2px `{colors.focus}` ring at 2px offset, border `{colors.ink}`), **disabled** (`{colors.surface-soft}` fill, 40% label opacity), **loading** (trailing mint spinner, field read-only), **error** (2px border and message in a dark red; this brand defines no error hue — see Known Gaps). **pressed** and **selected** are not applicable.

**`job-search-bar`** — the footer job-search control row
- White pill `{colors.canvas}`, 1px `{colors.hairline}` border, rounded `{rounded.full}`, padding `{spacing.xs} {spacing.md}`, holding Work Model / Location / Experience select controls and a submit. As with `{component.text-input}`, draw the resting edge in `{colors.hairline-strong}`.
- States — per select control: **default**, **hover** (label to `{colors.ink}`), **focus-visible** (2px `{colors.focus}` ring, 2px offset), **selected** (chosen option in `{colors.ink}` at weight 600 with a mint dot), **disabled** (40% opacity), **loading** (option list replaced by three skeleton rows), **error** (dark-red border on the submit row). **pressed** applies to the submit only (`scale(0.97)`).

### Navigation

**`nav-bar`** — top navigation (desktop)
- Background `{colors.canvas}`, links `{colors.ink}` in `{typography.nav-link}`, padding `{spacing.md}`. Logo left, link cluster center, "Sign In" plus a persistent black `{component.button-primary-sm}` "Join Now" pill right. Collapses to a hamburger under 768px.
- States — per link: **default** `{colors.ink}`, **hover** (mint `{colors.primary-deep}` label plus a 2px mint underline that grows from the centre), **focus-visible** (2px `{colors.focus}` ring, 2px offset), **selected** (current route, weight 600 with a persistent mint underline), **pressed** (`scale(0.98)`), **disabled** (40% opacity, used only on gated nav items). **loading** and **error** are not applicable.

**`footer`** — the site footer
- Background `{colors.canvas}`, muted `{colors.muted}` links in `{typography.body-sm}`, padding `{spacing.section}`. Multi-column link groups, logo, social icons, and the `{component.job-search-bar}` above it. At 14px the extracted `{colors.muted}` measures 3.24:1 on `{colors.canvas}` and fails AA for body text; set footer links in `{colors.muted-strong}` (5.49:1) and keep `{colors.muted}` for 18px+ labels only.
- States — **default** `{colors.muted-strong}`, **hover** (`{colors.ink}`, underline), **focus-visible** (2px `{colors.focus}` ring, 2px offset), **pressed** (no transform; underline holds). **disabled**, **loading**, **selected** and **error** are not applicable.

### Signature Components

**`hero`** — the pale-mint hero band
- Background `{colors.canvas-mint}`, black display headline `{typography.display}`, padding `{spacing.section}`, with a rounded `{component.video-card}` and a black `{component.button-primary}`.
- States — **default** only; the band is a layout surface. Its children carry the hover, focus-visible, pressed, disabled, loading, selected and error states listed under their own entries.

**`stat-item`** — a trust statistic (2,000,000 users, 80%, No.1 Choice)
- On the mint band `{colors.canvas-mint}`, big black number `{typography.heading-3}` over a caption, with a small line icon.
- States — one only: **default**. A trust statistic is static, non-interactive text; it has no hover, focus-visible, pressed, disabled, selected or error state, and counts up on first view only (see Motion & Animation).

**`job-ticker`** — the scrolling black job-listing marquee
- Full-width black band `{colors.ink}`, white text `{colors.on-dark}` in `{typography.body-sm}`, padding `{spacing.md}`, with continuously scrolling job titles and mint Jobright marks.
- States — **default** (marquee running; this is the file's one piece of deliberate brand ambience), **hover** (marquee pauses), **focus-visible** (2px `{colors.focus}` ring at 5.12:1 on the black band for each linked job title, which also pauses the marquee), **loading** (band at full black with no items rather than an empty rail). **pressed**, **disabled**, **selected** and **error** are not applicable. Under reduced motion the marquee is frozen — see Motion & Animation.

**`feature-band`** — an AI-feature section on the mint wash
- Background `{colors.canvas-mint}`, black headline `{typography.heading-2}`, padding `{spacing.section}`; copy + a black `{component.button-primary}` on one side, a `{component.feature-card}` mockup on the other.
- States — **default** only; a layout band with no interactive state of its own. Its CTA and mockup card own their hover, focus-visible, pressed, disabled, loading, selected and error behaviour.

**`testimonial-band-dark`** — the featured black testimonial band
- Background `{colors.ink}`, white quote `{colors.on-dark}` in `{typography.heading-4}`, padding `{spacing.section}`, with an author avatar and title.
- States — **default** only. Any link inside it takes **focus-visible** as a 2px `{colors.focus}` ring, which measures 5.12:1 against this black band.

**`faq-item`** — a question accordion row
- On the mint band `{colors.canvas-mint}`, 1px `{colors.hairline}` divider, question `{colors.ink}` in `{typography.body-md}`, padding `{spacing.md}`, with a plus/expand toggle.
- States — **default** (collapsed), **hover** (plus mark rotates 90°, row opacity to 1), **focus-visible** (2px `{colors.focus}` ring on the whole row, 2px offset), **pressed** (`scale(0.99)`), **selected** (expanded: plus becomes a minus, answer revealed, `aria-expanded="true"`). **disabled**, **loading** and **error** are not applicable.

**`cta-band`** — the closing "Let Jobright Take You to..." band
- Background `{colors.canvas-mint}`, black headline `{typography.heading-2}`, padding `{spacing.section}`, with a `{component.button-green}` and a hand-drawn illustration.
- States — **default** only; the mint pill inside it carries hover, focus-visible, pressed, disabled and loading.

### Examples (illustrative)

> Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`). Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently. `TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.
- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`
- States — **default**, **hover** (`translateY(-2px)`), **focus-visible** (2px `{colors.focus}` ring, 2px offset), **pressed** (`scale(0.99)`), **selected** (chosen plan: 2px `{colors.ink}` border plus a mint flag), **disabled** (unavailable plan at 40% opacity), **loading** (skeleton price row), **error** (dark-red helper line under the price when billing lookup fails).

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).
- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`
- Text is `{colors.on-dark}` (#ffffff, 21.00:1 on the black fill), **not** `{colors.on-primary}`: `on-primary` is scoped to labels sitting on the mint accent and is itself black, so binding it to a black fill would specify black-on-black.
- States — same ladder as `{component.ex-pricing-tier}`: **default**, **hover**, **focus-visible**, **pressed**, **selected**, **disabled**, **loading**, **error**, all drawn in the light-on-dark polarity.

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).
- Properties: `backgroundColor`, `rounded`, `padding`
- States — per option row: **default**, **hover**, **focus-visible**, **pressed**, **selected** (mint tick plus `{colors.ink}` label at weight 600), **disabled**, **loading** (skeleton rows), **error** (dark-red helper line).

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).
- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`
- States — **default**, **hover** and **pressed** on each line item's remove control, **focus-visible** on the drawer close button and every control inside it, **disabled** (locked add-on), **loading** (totals row as a skeleton), **error** (dark-red line when a price fails to resolve). **selected** is not applicable — items are present or absent, not selected.

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.
- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`
- States — **default**, **hover** (`{colors.surface-soft}` fill), **focus-visible** (2px `{colors.focus}` ring, 2px offset), **pressed** (`scale(0.99)`), **selected** (active route: 3px `{colors.primary}` indicator, label `{colors.ink}` at weight 600), **disabled** (40% opacity), **loading** (skeleton label), **error** (dark-red dot on the row when its section has a failure).

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses `{typography.caption}` eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`
- States — **default**, **hover** (row fill `{colors.surface-soft}`), **focus-visible** (2px `{colors.focus}` ring on the focused cell or row link), **pressed** on a sortable header, **selected** (checked row: `{colors.canvas-mint}` fill plus a mint left edge), **disabled** (non-sortable header, no hover), **loading** (three skeleton rows), **error** (dark-red cell text with an icon). Row borders use `{colors.hairline}` decoratively; the table's outer edge uses `{colors.hairline-strong}`.

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`
- States — inherited from `{component.text-input}` and `{component.button-primary}`: **default**, **hover**, **focus-visible**, **pressed**, **disabled**, **loading** (submit spinner, fields read-only), **error** (per-field dark-red border plus a form-level message). **selected** is not applicable.

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.
- Properties: `backgroundColor`, `rounded`, `padding`
- States — **default** (open), plus **focus-visible** on the close control and a trapped focus order inside the dialog; **loading** (body as skeleton while content resolves) and **error** (dark-red message block above the actions). **hover**, **pressed**, **disabled** and **selected** belong to the controls inside it, not the surface.

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`
- States — genuinely two: **default** (illustration plus caption) and **error** (same frame, failure copy and a retry `{component.button-primary}`). Its retry button carries hover, focus-visible, pressed, disabled and loading; the frame itself has no hover or selected state.

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`
- States — **default** (neutral), **error** (dark-red 2px left edge and icon), plus **hover** (dismiss timer pauses) and **focus-visible** on the dismiss control. **pressed**, **disabled**, **loading** and **selected** are not applicable.


## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** Nobody timed Jobright's real transitions; the values below are the shared **Playful** profile from `theme-audit/SPEC.md` section 5, applied to the surfaces this file documents. The one motion fact that *is* observable in the file is the continuously scrolling black job ticker (`{component.job-ticker}`), which is treated as deliberate brand ambience.

Playful fits this brand: saturated mint sits on interactive elements (the `{component.button-green}` pill, mint nav-link hovers, the mint score ring), the voice is informal, and the page carries emoji, a hand-drawn illustration and a marquee. Small scale pops on press and a springy enter read as Jobright; they would be wrong on a sober editorial system.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, cards, nav links) | `{motion.duration-fast}` | `{motion.ease-standard}` | `transform: scale(1.02)` / `translateY(-2px)`, `opacity` | No transform; colour/opacity change applied instantly |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.97)` | Scale removed; the state change is instant |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the 2px `{colors.focus}` ring | Ring appears instantly at full opacity — never suppressed |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(8px)` | Opacity fade only at `{motion.duration-reduced}`, no travel |
| Modal / drawer | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: scale(0.98→1)` (modal), `translateX` (drawer) | Opacity fade only at `{motion.duration-reduced}`; drawer appears in place |
| Dropdown / select menu | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: scale(0.98→1)` from the trigger edge | Opacity fade only at `{motion.duration-reduced}` |
| Toast (`{component.ex-toast}`) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` + `transform: translateY(12px)` with a slight overshoot | Opacity fade only at `{motion.duration-reduced}`, no travel or overshoot |
| List enter (job cards, testimonials, FAQ rows) | `{motion.duration-base}` per item, `{motion.stagger-step}` between | `{motion.ease-enter}` | `opacity` + `transform: translateY(12px)` | Stagger dropped; all items fade together at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)` | Opacity fade only at `{motion.duration-reduced}` |
| Loading (spinner, skeleton, stat count-up) | `{motion.duration-emphasis}` for the count-up; spinner loops continuously | `{motion.ease-standard}` | `transform: rotate()` on the spinner, `opacity` on skeletons | Spinner becomes a static mint arc with a text status; skeletons hold at a flat `{colors.surface-soft}`; the stat count-up shows its final number immediately |
| Job ticker marquee (brand ambience) | continuous, ~40s per cycle | linear | `transform: translateX()` | Frozen — the band renders static with its job titles in place |

### Rules

- **Only `transform` and `opacity` animate.** Never `width`, `height`, `top`, `left` or `margin` — the FAQ accordion reveals its answer with `opacity` and a `transform` on the inner wrapper, not by animating height, and the nav underline scales on `transform` rather than animating width.
- Every exit is shorter than its matching entrance (`{motion.duration-fast}` out against `{motion.duration-base}` in).
- Nothing animates on first paint in a way that delays content: hero copy and the primary pill render at full opacity, and the list-enter stagger applies only to content entering after the first view.
- The only infinite animations are the loading spinner and the `{component.job-ticker}` marquee, which is stated here as deliberate brand ambience. No other loop exists in this system.
- The overshoot in `{motion.ease-enter}` (`cubic-bezier(0.17, 0.89, 0.32, 1.28)`) is the Playful signature and is capped at a 2% scale or 12px travel, so a springy reveal never reads as a bounce.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. No translateY, translateX, scale or
     rotate on hover, press, page transition, modal, drawer, dropdown, toast,
     list enter or list exit. The list stagger is removed with it. */
  /* Frozen: the job-ticker marquee and the stat count-up, which render in
     their final state. The loading spinner stops and is replaced by a static
     mint arc plus a text status. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (130ms), and the
     focus-visible ring, which always appears instantly and is never removed. */
  *, *::before, *::after {
    transition-duration: 130ms !important;   /* {motion.duration-reduced} */
    animation-duration: 130ms !important;
    animation-iteration-count: 1 !important;
    transition-property: opacity, color, background-color, border-color !important;
  }
}
```

## Accessibility

Measured with WCAG 2.1 relative luminance over the hexes in this file's own frontmatter. Everything in the table is computed; the tap-target and focus-order notes below it are prescribed, since this document has no rendered page behind it.

### Measured contrast

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` #000000 on `{colors.canvas}` #ffffff | 21.00:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-mint}` #ecffe0 | 19.95:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-soft}` #f2f4f5 | 19.03:1 | 4.5:1 | Pass |
| `{colors.on-dark}` #ffffff on `{colors.ink}` | 21.00:1 | 4.5:1 | Pass |
| `{colors.on-primary}` #000000 on `{colors.primary}` #00f0a0 | 13.97:1 | 4.5:1 | Pass |
| `{colors.focus}` #008f66 on `{colors.canvas}` | 4.10:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.canvas-mint}` | 3.90:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.surface-soft}` | 3.72:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.ink}` | 5.12:1 | 3.0:1 | Pass |
| `{colors.muted-strong}` #616a75 on `{colors.canvas}` | 5.49:1 | 4.5:1 | Pass (prescribed) |
| `{colors.hairline-strong}` #7a8290 on `{colors.canvas}` | 3.62:1 | 3.0:1 | Pass (prescribed) |
| `{colors.primary-deep}` #00664a on `{colors.canvas}` | 7.00:1 | 4.5:1 | Pass (prescribed) |

### Disclosed failures — the real brand does not meet AA here

These are extracted values and are frozen. Each one is a genuine failure of the live brand, stated rather than corrected.

| Foreground / Background | Ratio | Required | Note |
|---|---|---|---|
| `{colors.hairline}` #e5e7eb on `{colors.canvas}` #ffffff | 1.24:1 | 3.0:1 | **Fails.** The brand's 1px divider is decorative. Where it is a control's only boundary — `{component.text-input}`, `{component.job-search-bar}` — use `{colors.hairline-strong}`. |
| `{colors.hairline}` #e5e7eb on `{colors.surface-soft}` #f2f4f5 | 1.12:1 | 3.0:1 | **Fails.** Same divider on the grey utility fill; effectively invisible. Same remedy. |
| `{colors.muted}` #86909c on `{colors.surface-soft}` #f2f4f5 | 2.94:1 | 4.5:1 | **Fails.** Muted grey on the grey inset panel fails even the 3:1 large-text threshold. Use `{colors.muted-strong}`. |
| `{colors.muted}` #86909c on `{colors.canvas}` #ffffff | 3.24:1 | 4.5:1 | **Fails** for text under 18px, which is how the brand uses it — `{component.footer}` links are 14px `{typography.body-sm}`. It clears 3:1, so it is defensible for 18px+ / 14px-bold labels only. Everything smaller takes `{colors.muted-strong}`. |
| `{component.score-ring}` numeral: `{colors.primary}` #00f0a0 on `{colors.canvas}` #ffffff | 1.50:1 | 3.0:1 | **Fails.** Mint on white is near-invisible as text at any size. This is a real brand failure, not a token binding mistake: the mint *is* the brand's accent and the ring stroke reads fine. The numeral should be `{colors.primary-deep}` or `{colors.ink}`. |
| `{colors.primary}` #00f0a0 on `{colors.canvas-mint}` #ecffe0 | 1.43:1 | 3.0:1 | **Fails.** Never set mint type or mint icons on the mint band; the accent only works against `{colors.ink}` (13.97:1) or as a fill. |

One correction, not a disclosure: `{component.ex-pricing-tier-featured}` previously bound `textColor` to `{colors.on-primary}` over an `{colors.ink}` fill — black on black, 1.00:1. `{colors.on-primary}` is scoped to labels on the mint accent, so that was a binding error, now `{colors.on-dark}` at 21.00:1.

### Focus ring

- One ring: 2px solid `{colors.focus}` #008f66 at a 2px offset, with the control's own radius.
- Ratios against every surface this file defines are in the table above: 4.10:1 on `{colors.canvas}`, 3.90:1 on `{colors.canvas-mint}`, 3.72:1 on `{colors.surface-soft}`, 5.12:1 on `{colors.ink}`. A single mid-luminance ring is used instead of a light/dark pair because the brand runs three surface polarities and one deep-mint tone clears 3:1 on all of them.
- The 2px offset is mandatory, not decorative: `{colors.focus}` #008f66 on `{colors.primary}` #00f0a0 measures 2.73:1, below the 3.0:1 a focus indicator needs, so the ring must sit on the band behind the mint `{component.button-green}` pill rather than on the accent fill itself. Drawn at its offset the ring lands on `{colors.canvas-mint}` (3.90:1) or `{colors.canvas}` (4.10:1) and passes.
- The ring is never suppressed, never animated out, and is the one thing reduced motion leaves fully intact.

### Tap targets and reduced motion

- **Minimum tap target: 44 × 44px** for every interactive element, including the compact `{component.button-primary-sm}` nav pill (whose `{spacing.xxs} {spacing.md}` padding alone does not reach it — pad the hit area), the FAQ toggle, the job-search selects and the toast dismiss. **Prescribed, not verified:** tap-target size cannot be measured from a document, only from a rendered page.
- Reduced motion: all travel and scale removed, opacity fades capped at `{motion.duration-reduced}` (130ms), the job-ticker marquee and stat count-up frozen in their final state. Full rule in Motion & Animation.
- Target size, overlap, reflow and focus-order claims beyond the above are out of scope here for the same reason — see Known Gaps.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` for the logo, links, the signature green pill, and highlights — the one electric accent that carries the brand.
- Carry section rhythm on the pale-mint band (`{colors.canvas-mint}`), alternating with white and full-black bands.
- Use black pills (`{rounded.xl}`) for primary CTAs and the mint-green pill (`{rounded.pill}`) for the one signature accent action.
- Pair heavy Titillium Web headlines (`{typography.display}`) with light Inter body (`{typography.body-lg}`) for confident-yet-quiet hierarchy.
- Float product-mockup cards (`{rounded.card}`) on soft shadows over the mint bands to demo AI features.
- Keep buttons pill-shaped and high-contrast — black-on-mint or white-on-black.

### Don't
- Don't introduce the product-UI tag/score palette (Ant-style pastels) as brand chrome — the marketing system is mint, black, and white only.
- Don't fill a primary CTA with `{colors.primary}` green as the default — the everyday primary is the black pill; green is the one accent pill.
- Don't set body copy in Titillium Web or headlines in Inter — the display/UI font roles are fixed.
- Don't put heavy shadows on cards — elevation is a hairline or a whisper-soft float.
- Don't cool or blue-shift the mint bands — the section wash is warm spring-mint `{colors.canvas-mint}`.
- Don't square off the pills or the mockup cards — the rounded pill + 40px card silhouette is core to the friendly feel.

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 576px | Single column; nav → hamburger; feature rows stack; pills go full-width |
| Tablet | 576–991px | Two-column feature rows collapse toward stacked; testimonials drop to 1–2 up |
| Laptop | 992–1199px | Multi-column grids intact; tightened gutters |
| Desktop | ≥ 1200px | Full layout; centered ~1200px column; full-bleed bands |

### Touch Targets
The primary (`{component.button-primary}`) and green (`{component.button-green}`) pills carry ample padding for a comfortable ≥44px tap height. Nav collapses to a hamburger under 768px while keeping the black "Join Now" pill visible.

### Collapsing Strategy
The top nav collapses to a hamburger under 768px, keeping the black CTA pill. Two-column feature rows stack image-below-copy; the 3-up testimonial grid reflows to 1–2 up; the footer job-search bar wraps its select controls. The full-width mint and black bands stay full-bleed at every width.

### Image Behavior
Product-mockup imagery sits inside rounded white cards (`{rounded.card}` / `{rounded.md}`), floating over the mint bands with a soft shadow. The hero leads with a rounded video card. Avatars and score rings are circular (`{rounded.full}`). Images lazy-load below the fold; the job ticker scrolls as a continuous marquee.

## Known Gaps

- **Motion is prescribed, not extracted.** No timing function, duration or spring in this file was measured from the live site; the whole `motion:` group and the Motion & Animation table are the shared Playful profile applied by judgement. The only observed motion facts are the continuous job-ticker marquee and the lazy-loading of below-fold imagery.
- **States are prescribed.** The live site was analysed as static pages, so every hover, focus-visible, pressed, disabled, loading, selected and error behaviour documented under Components is a reasoned proposal consistent with the brand's chrome, not a recorded observation. The one exception is the `{component.ex-app-shell-row}` active indicator, which the frontmatter already carried.
- **`{component.text-input}` radius conflicts between sources.** The frontmatter records `{rounded.none}` (0px) while the Shapes table and the Components prose both say `{rounded.sm}` (12px). Both are left as written rather than silently reconciled; the 0px extraction may have come from a reset stylesheet rather than the rendered control. Needs a second look at the live page.
- **No error or status hues exist in this palette.** The brand defines mint, black, white, a grey and two utility tones — there is no red, amber or blue. Error states above say "dark red" without a token because inventing a brand hex would be a falsification. A semantic status ramp needs to be added by whoever builds on this document, and stated as an addition.
- **No shadow tokens.** `## Elevation & Depth` states an `rgba(0,0,0,0.5)` inset hairline and a "whisper-soft drop shadow" in prose with no token to reference, and no blur, offset or spread was captured. The elevation ladder is therefore described two ways — border at level 0–1, shadow at level 2 — and cannot be expressed as one consistent scale until real shadow values are measured.
- **The radius ladder is a record, not a scale.** It runs 12 / 16 / 24 / 28 / 18 / 36 / 40, with `{rounded.pill-nav}` 18px sitting between `{rounded.md}` and `{rounded.lg}` and `{rounded.none}` unused in the Shapes table. The ladder is a record of what the site does rather than a designed scale; a rebuild should pick one.
- **The 40px asymmetric corner is undocumented in detail.** The prose says "asymmetric 0/40/40" for `{component.feature-card}` without stating which corner is squared or whether it mirrors when the feature row alternates sides.
- **Not computable from a document:** tap-target size, overlap, horizontal overflow, clipping, frame rate and layout shift. The ≥44px tap height in Responsive Behavior and the 44 × 44px minimum in Accessibility are design intent, not measurements.
- **Dark mode is undefined.** The file documents full-black *bands* inside a light page, not a dark theme. `{colors.focus}` was chosen to clear 3:1 on those black bands as well as the light surfaces, but no dark-mode surface, text or border set exists.
