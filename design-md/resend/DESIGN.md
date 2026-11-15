---
version: alpha
name: Resend-design-analysis
description: |
  Resend's marketing surfaces sit on a near-pure black canvas with off-white
  text and a single signature color — the deep editorial-serif Domaine
  Display headline mark — that gives an otherwise utilitarian developer-tool
  brand its print-magazine confidence. The system pairs Domaine Display
  (oversized 76px–96px serif, ss01/ss04/ss11 features on) with ABC Favorit
  for body and Inter for UI. Surfaces rely on subtle 6–9% opacity gradient
  glows, hairline 1px borders made from translucent white, and a strict
  rounded-12px container vocabulary. There is no decorative chrome — just
  type, code, and atmospheric depth.

colors:
  primary: "#fcfdff"
  primary-on: "#000000"
  ink: "#fcfdff"
  body: "rgba(252,253,255,0.86)"
  charcoal: "rgba(252,253,255,0.7)"
  mute: "#a1a4a5"
  ash: "#888e90"
  stone: "#464a4d"
  on-light: "#000000"
  on-light-mute: "rgba(0,0,51,0.7)"
  canvas: "#000000"
  surface-card: "#0a0a0c"
  surface-elevated: "#101012"
  surface-deep: "#06060a"
  hairline: "rgba(255,255,255,0.06)"
  hairline-strong: "rgba(255,255,255,0.14)"
  hairline-control: "rgba(255,255,255,0.36)"
  divider-soft: "rgba(255,255,255,0.04)"
  accent-orange: "#ff801f"
  accent-orange-glow: "rgba(255,89,0,0.22)"
  accent-yellow: "#ffc53d"
  accent-blue: "#3b9eff"
  accent-blue-glow: "rgba(0,117,255,0.34)"
  accent-green: "#11ff99"
  accent-green-glow: "rgba(34,255,153,0.18)"
  accent-red: "#ff2047"
  accent-red-glow: "rgba(255,32,71,0.34)"
  link: "#3b9eff"
  surface-light: "#f1f7fe"
  focus: "#3b9eff"
  focus-on-light: "#0075ff"

typography:
  display-xxl:
    fontFamily: Domaine Display
    fontSize: 96px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.96px
    fontFeature: "ss01, ss04, ss11"
  display-xl:
    fontFamily: Domaine Display
    fontSize: 76.8px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.768px
    fontFeature: "ss01, ss04, ss11"
  display-lg:
    fontFamily: ABC Favorit
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -2.8px
    fontFeature: "ss01, ss04, ss11"
  heading-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: -0.4px
  heading-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  subtitle:
    fontFamily: ABC Favorit
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    fontFeature: "ss01, ss04, ss11"
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontFamily: ABC Favorit
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.8px
    fontFeature: "ss01, ss04, ss11"
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
  button-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
  button-sm:
    fontFamily: ABC Favorit
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.35px
    fontFeature: "ss01, ss03, ss04"
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
  caption-emph:
    fontFamily: Helvetica
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
  code-md:
    fontFamily: Geist Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
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
  band: 128px

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
    textColor: "{colors.primary-on}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 36px
  button-primary-pressed:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.primary-on}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
  button-ghost:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 36px
  button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 7px 15px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    height: 40px
  hero-stripe:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xxl}"
    rounded: "{rounded.none}"
    padding: 96px 32px
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  feature-card-bordered:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-featured:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  code-window:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.body}"
    typography: "{typography.code-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  code-tab:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.charcoal}"
    typography: "{typography.code-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  email-mockup:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 0
  email-mockup-light:
    backgroundColor: "#ffffff"
    textColor: "{colors.on-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 0
  badge-pill:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  status-dot:
    backgroundColor: "{colors.accent-green}"
    rounded: "{rounded.full}"
    size: 8px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 64px
  sub-nav-pill:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  contributor-avatar:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    size: 32px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.charcoal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 64px 32px
---

## Overview

Resend looks like a developer tool with the typography of an editorial.
Every page opens on `{colors.canvas}` (`#000000`), and the loudest element on
the canvas is not a button or a brand stamp — it's a 96px Domaine Display
serif headline ("Email for developers", "Email reimagined") with the
`ss01 / ss04 / ss11` stylistic alternates engaged. That single typographic
decision sets the brand tone: confident, considered, slightly literary, and
priced on quality rather than novelty.

The supporting cast is technical. Body copy switches to **ABC Favorit** for
marketing prose and **Inter** for UI labels, while code blocks render in
**Geist Mono** inside `{component.code-window}` shells with hairline traffic-
light dots. Surface depth is built almost entirely from translucent white —
6% borders, 14% strong borders, 4% dividers — over a deep `{colors.surface-deep}`
layer that sits just below the canvas black. There are no gradients painted
across full bands, just **soft atmospheric glows** (orange, blue, green, red,
yellow) anchored at the top of select sections, all at low opacity.

Page rhythm cycles in a single dark register: hero stripe → atmospheric
section → code window section → email mockup section → pricing or feature
grid → black footer. The brand never warms to a light surface; even
secondary email mockups are rendered as compact white cards inside the dark
canvas, framed like print insets in a black-bordered magazine page.

**Key Characteristics:**
- Pure black canvas (`{colors.canvas}` — `#000000`) on every public page; off-white text (`{colors.ink}` — `#fcfdff`) carries the full read.
- A serif-led type system: **Domaine Display** at 76–96px for hero headlines, **ABC Favorit** for marketing body, **Inter** for UI, **Geist Mono** for code.
- Six accent glow colours used only as low-opacity atmospheric washes (`{colors.accent-orange}`, `{colors.accent-blue}`, `{colors.accent-green}`, `{colors.accent-red}`, `{colors.accent-yellow}`) — never as buttons or solid surfaces.
- Strict container vocabulary: `{rounded.lg}` (12px) for feature cards, code wells, and email mockups; `{rounded.md}` (8px) for buttons; `{rounded.full}` for pills and avatars.
- Translucent white borders (`{colors.hairline}` 6% / `{colors.hairline-strong}` 14%) replace shadows entirely — the system has no traditional drop-shadow elevation language.
- `{component.button-primary}` is a small white rectangle with black text — counterintuitive contrast that becomes the page's brightest pixel and works as a single visual anchor.

## Colors

### Brand & Accent
- **Primary White** (`{colors.primary}` — `#fcfdff`): the brand's de facto accent. Reserved for `{component.button-primary}` (white pill on black canvas), Domaine display headlines, and the active text colour. White is the loudest possible colour on this canvas — that's the signature.
- **Primary On** (`{colors.primary-on}` — `#000000`): label colour on top of `{colors.primary}` surfaces. Black text on white pill is the brand's CTA pattern.
- **Surface Light** (`{colors.surface-light}` — `#f1f7fe`): a subtle blue-tinted off-white used as the active/pressed state of `{component.button-primary}`.

### Surface
- **Canvas** (`{colors.canvas}` — `#000000`): the default page background. True black, never near-black.
- **Surface Card** (`{colors.surface-card}` — `#0a0a0c`): the standard inset card surface, just lighter than canvas to register a step up in elevation.
- **Surface Elevated** (`{colors.surface-elevated}` — `#101012`): a second elevation step used on featured pricing tiers and ghost button surfaces.
- **Surface Deep** (`{colors.surface-deep}` — `#06060a`): code window background — slightly cooler and darker than the canvas itself, suggesting depth via temperature.
- **Hairline** (`{colors.hairline}` — `rgba(255,255,255,0.06)`): the soft 1px translucent-white divider used between rows and around feature cards.
- **Hairline Strong** (`{colors.hairline-strong}` — `rgba(255,255,255,0.14)`): the structural 1px border on cards, code wells, and form inputs.
- **Hairline Control** (`{colors.hairline-control}` — `rgba(255,255,255,0.36)`): **prescribed, not extracted.** A parallel accessible boundary for controls whose only edge is a border — `{component.text-input}`, `{component.button-outline}`, `{component.button-ghost}`. The extracted `{colors.hairline-strong}` reaches only 1.42:1 on `{colors.surface-card}`, so it is scoped to decorative card and row edges; use `{colors.hairline-control}` (3.25:1 on `{colors.surface-card}`, 3.14:1 on `{colors.canvas}`) wherever the boundary carries meaning. The existing `components:` bindings are left exactly as extracted; re-pointing them is a brand-owner decision.
- **Divider Soft** (`{colors.divider-soft}` — `rgba(255,255,255,0.04)`): low-contrast dividers between footer columns.

### Focus

- **Focus** (`{colors.focus}` — `#3b9eff`): the focus ring on every dark surface. **Prescribed, not extracted** — the real site relies on the browser default. It reuses the existing `{colors.accent-blue}` / `{colors.link}` hex rather than introducing a new brand colour, so the ring reads as the one interactive colour the system already owns. Measured 7.52:1 on `{colors.canvas}`, 7.08:1 on `{colors.surface-card}`, 6.81:1 on `{colors.surface-elevated}`, 7.24:1 on `{colors.surface-deep}`.
- **Focus On Light** (`{colors.focus-on-light}` — `#0075ff`): the counterpart ring for the white email-card insets and `{colors.surface-light}`, where `{colors.focus}` collapses to 2.59:1. It is the opaque base of `{colors.accent-blue-glow}` (`rgba(0,117,255,0.34)`), so again no new hex enters the palette. Measured 3.90:1 on `{colors.surface-light}` and 4.21:1 on `#ffffff`.
- Both rings are drawn **outside** the control: 2px ring, 2px offset, so the ratio that matters is against the surface behind the control rather than the control's own fill. That is what WCAG 2.2 Focus Appearance measures.

### Text
- **Ink** (`{colors.ink}` — `#fcfdff`): primary text colour on the dark canvas. Faintly blue-cool to feel like printed paper rather than pure white pop.
- **Body** (`{colors.body}` — `rgba(252,253,255,0.86)`): long-form body text where pure ink would feel too sharp.
- **Charcoal** (`{colors.charcoal}` — `rgba(252,253,255,0.7)`): captions, secondary nav labels.
- **Mute** (`{colors.mute}` — `#a1a4a5`): supporting text and inactive labels.
- **Ash** (`{colors.ash}` — `#888e90`): tertiary text, footer copy.
- **Stone** (`{colors.stone}` — `#464a4d`): disabled foreground.
- **On-Light** (`{colors.on-light}` — `#000000`): label colour inside the rare email-mockup white cards.
- **On-Light Mute** (`{colors.on-light-mute}` — `rgba(0,0,51,0.7)`): secondary text inside email mockups.

### Semantic
- **Accent Orange** (`{colors.accent-orange}` — `#ff801f`) + glow (`{colors.accent-orange-glow}` — `rgba(255,89,0,0.22)`): atmospheric warm wash anchored to "Email reimagined" / customer story sections. Solid orange never appears as a button or surface — only the glow.
- **Accent Yellow** (`{colors.accent-yellow}` — `#ffc53d`): used in inline highlight strokes and "first-class developer experience" key callouts.
- **Accent Blue** (`{colors.accent-blue}` — `#3b9eff`) + glow (`{colors.accent-blue-glow}` — `rgba(0,117,255,0.34)`): inline link colour and the cool atmospheric wash on the "Integrate this weekend" section.
- **Accent Green** (`{colors.accent-green}` — `#11ff99`) + glow (`{colors.accent-green-glow}` — `rgba(34,255,153,0.18)`): success status dots and the "delivery confirmed" feature glow.
- **Accent Red** (`{colors.accent-red}` — `#ff2047`) + glow (`{colors.accent-red-glow}` — `rgba(255,32,71,0.34)`): inline error red and the "reach humans, not spam folders" attention wash.
- **Link** (`{colors.link}` — `#3b9eff`): inline link colour — same as accent blue.

## Typography

### Font Family

Resend ships a four-family stack:

- **Domaine Display** — proprietary editorial serif used exclusively for hero headlines at 76px+, with `ss01 / ss04 / ss11` stylistic sets engaged for a slightly tighter, more print-magazine look.
- **ABC Favorit** — proprietary humanist sans-serif used for marketing body copy, hero subtitles, and pill labels. Carries `ss01 / ss03 / ss04` features for tabular figures and alternate glyphs.
- **Inter** — open-source sans-serif used for UI: button labels, captions, card body text, nav links.
- **Geist Mono** — open-source monospace used in code wells.

When proprietary families cannot be licensed, **Söhne** or **Tiempos Headline** stand in for Domaine Display, and **Geist** or **Inter Tight** can replace ABC Favorit. Inter and Geist Mono are open-source and should be used directly.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 96px | 400 | 1.0 | -0.96px | Home hero ("Email for developers"). One per page. |
| `{typography.display-xl}` | 76.8px | 400 | 1.0 | -0.768px | Section openers ("Email reimagined", "Available today"). |
| `{typography.display-lg}` | 56px | 400 | 1.2 | -2.8px | ABC Favorit display sub-titles. |
| `{typography.heading-md}` | 24px | 500 | 1.5 | -0.4px | Card titles, section sub-titles. |
| `{typography.heading-sm}` | 20px | 500 | 1.3 | -0.3px | List headers. |
| `{typography.subtitle}` | 20px | 400 | 1.3 | 0 | Hero subtitles. |
| `{typography.body-lg}` | 18px | 400 | 1.5 | 0 | Marketing prose. |
| `{typography.body-md}` | 16px | 400 | 1.5 | -0.8px | ABC Favorit body. |
| `{typography.body-sm}` | 14px | 400 | 1.43 | 0 | Captions, metadata. |
| `{typography.button-md}` | 14px | 500 | 1.43 | 0 | Default button label. |
| `{typography.button-sm}` | 14px | 500 | 1.43 | 0.35px | Pill labels, inline links. |
| `{typography.caption}` | 12px | 400 | 1.5 | 0 | Footer disclosure, copyright. |
| `{typography.caption-emph}` | 14px | 600 | 1.0 | 0 | Emphatic small caption — Helvetica fallback. |
| `{typography.code-md}` | 13px | 400 | 1.6 | 0 | Code blocks, inline code. |

### Principles
- Display sizes always run at `lineHeight: 1.0` with negative letter-spacing — the Domaine Display headlines pack into solid typographic blocks rather than open prose lines.
- Body weight stays at 400 across `{typography.body-lg}` and `{typography.body-md}`. The serif/sans family change carries hierarchy, not weight bumps.
- ABC Favorit always runs with `ss01 / ss04 / ss11` engaged; Inter never carries OpenType features. Code in Geist Mono never carries ligatures.
- Inline links use `{typography.button-sm}` with positive letter-spacing (`0.35px`) and ABC Favorit — the small spacing nudge gives interactive prose its precision.

### Note on Font Substitutes

When Domaine Display is unavailable, clamp `lineHeight` to 1.0 explicitly and apply `font-feature-settings: "ss01", "liga"` on the substitute serif to mimic the alternate glyphs. Söhne or Tiempos Headline will read closest. ABC Favorit substitutes (Geist, Inter Tight) typically default to looser tracking — apply -0.5% letter-spacing on body sizes to compensate.

## Layout

### Spacing System
- **Base unit**: 4px, with the working scale on multiples of 4 / 8 / 16.
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.xxxl}` 48px · `{spacing.section}` 96px · `{spacing.band}` 128px.
- Section padding: `{spacing.section}` (96px) vertical between bands; `{spacing.band}` (128px) on the hero stripe and closing footer transition.
- Card internal padding: `{spacing.xxl}` (32px) on `{component.feature-card}`, `{component.pricing-tier}`, and `{component.code-window}`.

### Grid & Container
- **Max content width** ≈ 1200px on body sections.
- **Feature grid**: 3 columns at desktop, 2 at tablet, 1 at mobile.
- **Pricing**: 3-tier grid centred at desktop; centre tier promotes to `{component.pricing-tier-featured}` (one-step-elevated surface).
- **Code-story splits**: a 2-up split — narrative copy left, `{component.code-window}` right — collapsing to stacked at < 1024px.
- **Email mockup band**: a single white card (640px max width) centred in the dark canvas with generous vertical padding to read like a print magazine inset.

### Whitespace Philosophy
- Whitespace is editorial and generous — full-bleed sections breathe at 96–128px so Domaine Display headlines have room to register at scale.
- Inside cards, padding stays at 32px so feature copy and code wells have a consistent rhythm with the outer grid.
- Hairline `{colors.hairline}` and `{colors.hairline-strong}` carry the role drop shadows would in a brighter system; the dark canvas suppresses traditional shadow depth entirely.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | No shadow, no border | Default canvas, full-bleed bands. |
| 1 — surface card | `{colors.surface-card}` (`#0a0a0c`) + 1px `{colors.hairline-strong}` | Feature cards, pricing tiers, form inputs. |
| 2 — elevated | `{colors.surface-elevated}` (`#101012`) + 1px `{colors.hairline-strong}` | Featured pricing tier, ghost button. |
| 3 — code well | `{colors.surface-deep}` (`#06060a`) + 1px `{colors.hairline-strong}` | Code window, terminal shells. |
| 4 — atmospheric glow | Low-opacity radial gradient (`{colors.accent-*-glow}`) anchored at section top | Section openers ("Integrate this weekend", "Email reimagined"). |

The system has **no traditional drop shadow language**. Every surface either gets a translucent-white hairline border or sits inside an atmospheric glow. The dark canvas absorbs shadow naturally; surfaces register depth via temperature and luminance shifts rather than blur.

### Decorative Depth
- **Atmospheric section glows** — six accent colours each with a paired glow token (orange, yellow, blue, green, red, plus a deep slate for "everything in your context"). Each section opens with a single radial wash anchored at the top edge of the section, falling off to canvas black within ~600px vertical distance. Never two glows in the same section.
- **Email card insets** — the "Beyond experience" mockup band lifts a single white email card off the black canvas, giving it the only true light-on-dark contrast in the system. The card uses no shadow; the contrast itself is the elevation.
- **Code window traffic lights** — `{component.code-window}` shells include a row of three coloured dots (red `{colors.accent-red}`, yellow `{colors.accent-yellow}`, green `{colors.accent-green}`) at the top — the only place all three semantic colours appear together as solid surfaces.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Hero stripe, full-bleed bands, footer. |
| `{rounded.xs}` | 4px | Inline tags inside code wells. |
| `{rounded.sm}` | 6px | Code tabs, mid-size chips. |
| `{rounded.md}` | 8px | Buttons, form inputs. |
| `{rounded.lg}` | 12px | Feature cards, pricing tiers, code wells, email mockups. |
| `{rounded.xl}` | 16px | Larger feature panels. |
| `{rounded.full}` | 9999px | Pills, status dots, contributor avatars. |

### Photography Geometry
- The system uses almost no photography. Visual interest comes from typography + atmospheric glows + code wells + the white email-card insets.
- When portraits appear (testimonial avatars), they are circular (`{rounded.full}`) at 32px, sitting inline with body copy.
- Email mockup cards run at 4:5 portrait aspect with `{rounded.lg}` corners.

## Components

### Buttons

**`button-primary`** — white CTA
- Background `{colors.primary}`, label `{colors.primary-on}`, type `{typography.button-md}`, padding `8px 16px`, `rounded: {rounded.md}`, height 36px.
- The brightest pixel on the canvas. Used for "Get started", "Sign up", "Try Resend".
- Pressed state lives in `button-primary-pressed` (background `{colors.surface-light}`).
- **States** — default · hover (background lifts to `{colors.surface-light}`) · focus-visible (2px `{colors.focus}` ring, 2px offset, border unchanged) · active/pressed (`button-primary-pressed`) · disabled (`{colors.stone}` label on `{colors.surface-elevated}`, no ring) · loading (label swaps for an in-place spinner, width held so the button does not reflow). No selected or error state: the primary CTA is never a toggle.

**`button-ghost`** — translucent CTA
- Background `{colors.surface-elevated}`, label `{colors.ink}`, 1px `{colors.hairline-strong}`, type `{typography.button-md}`, `rounded: {rounded.md}`, height 36px.
- Equal-weight secondary action paired with `{component.button-primary}`.
- **States** — default · hover (surface steps from `{colors.surface-elevated}` toward `{colors.surface-card}` luminance, border to `{colors.hairline-control}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (surface returns to `{colors.surface-card}`) · disabled (`{colors.stone}` label, border drops to `{colors.hairline}`) · loading (inline spinner replaces the label). No selected or error state.

**`button-outline`** — outlined CTA
- Background `{colors.canvas}`, label `{colors.ink}`, 1px `{colors.hairline-strong}`, type `{typography.button-md}`, `rounded: {rounded.md}`, height 36px.
- Tertiary action; appears on its own next to inline links.
- **States** — default · hover (border to `{colors.hairline-control}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · active/pressed (fill to `{colors.surface-card}`) · disabled (`{colors.stone}` label, border `{colors.hairline}`). No loading, selected or error state.

### Cards & Containers

**`hero-stripe`** — full-bleed hero
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.display-xxl}` for the headline, padding `96px 32px`, `rounded: {rounded.none}`.
- Used only on the home page hero band; carries the 96px Domaine Display headline and a single `{component.button-primary}` CTA. No photography, no atmospheric glow inside the hero itself — the glow appears on the section that follows.
- **States** — default only. A full-bleed band is not interactive, so it has no hover, focus-visible, pressed, disabled, loading, selected or error state; its CTA carries all of those.

**`feature-card`** — feature highlight card
- Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}` (32px).
- Used in the home grid: "Despite emails using React", "So beyond editing", etc. No outline by default — relies on canvas black contrast.
- **States** — default · hover (surface to `{colors.surface-elevated}`, 1.04:1 against `{colors.surface-card}`, so a border step to `{colors.hairline-control}` carries the change rather than the fill) · focus-visible (whole card takes a 2px `{colors.focus}` ring at 2px offset when it wraps a link). Genuinely three states: a static feature card has no pressed, disabled, loading, selected or error state.

**`feature-card-bordered`** — outlined feature card
- Background `{colors.surface-card}`, text `{colors.ink}`, 1px `{colors.hairline-strong}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}`.
- Used when feature cards sit close together and need explicit separation.
- **States** — default · hover (border to `{colors.hairline-control}`) · focus-visible (2px `{colors.focus}` ring, 2px offset, when the card is a link). No pressed, disabled, loading, selected or error state.

**`pricing-tier`** — pricing tier card
- Background `{colors.surface-card}`, text `{colors.ink}`, 1px `{colors.hairline-strong}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}` (32px).
- Tier name in `{typography.heading-md}` + price in `{typography.display-lg}` (ABC Favorit, 56px).
- **States** — default · hover (border to `{colors.hairline-control}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · selected (promotes to `{component.pricing-tier-featured}`). No pressed, disabled, loading or error state; the tier's CTA owns those.

**`pricing-tier-featured`** — recommended tier
- Background `{colors.surface-elevated}`, text `{colors.ink}`, 1px `{colors.hairline-strong}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}`.
- Centre tier elevated by surface luminance, not by colour.
- **States** — default (this *is* the selected variant of `{component.pricing-tier}`) · hover (border to `{colors.hairline-control}`) · focus-visible (2px `{colors.focus}` ring, 2px offset). No pressed, disabled, loading or error state.

**`code-window`** — code well
- Background `{colors.surface-deep}`, text `{colors.body}`, type `{typography.code-md}`, 1px `{colors.hairline-strong}`, `rounded: {rounded.lg}`, padding `{spacing.xl}` (24px).
- Includes a 3-dot traffic-light row at top using `{colors.accent-red}` / `{colors.accent-yellow}` / `{colors.accent-green}` for chrome, plus a tab strip below it.
- **States** — default · hover (copy-to-clipboard affordance fades in at `{motion.duration-fast}`) · focus-visible (2px `{colors.focus}` ring, 2px offset, on the copy control and on the scroll container) · selected (handled by `{component.code-tab}`) · loading (skeleton rows at `{colors.hairline-strong}` while a snippet streams). No pressed, disabled or error state.

**`code-tab`** — code language tab
- Background `{colors.surface-card}`, text `{colors.charcoal}`, type `{typography.code-md}`, `rounded: {rounded.sm}`, padding `6px 12px`.
- Active tab bumps text to `{colors.ink}` and adds a subtle `{colors.hairline-strong}` underline.
- **States** — default (`{colors.charcoal}` label) · hover (label to `{colors.ink}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · selected (label `{colors.ink}` plus underline; `aria-selected`) · active/pressed (same treatment as selected, applied on pointer-down). No disabled, loading or error state.

**`email-mockup`** — email-card inset
- Background `{colors.surface-card}` (or the rare `#ffffff` when rendered as a light-island inset), text `{colors.ink}` (or `{colors.on-light}` for white insets), type `{typography.body-md}`, `rounded: {rounded.lg}`, padding 0.
- Used in the "Beyond experience" band to demonstrate rendered email output.
- The light-island variant is declared as `email-mockup-light` (`#ffffff` ground, `{colors.on-light}` ink, 21.0:1) so the pair is measurable rather than implied by prose.
- **States** — default only: it is a rendered artefact, not a control, so it carries no hover, focus-visible, pressed, disabled, loading, selected or error state.

### Inputs & Forms

**`text-input`** — default input
- Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.body-sm}`, 1px `{colors.hairline-strong}`, `rounded: {rounded.md}`, padding `10px 14px`, height 40px.
- Sign-up and waitlist email fields. As extracted, the focus state thickens the border to `{colors.ink}` and the site adds no ring of its own.
- **States** — default (border `{colors.hairline-strong}` as extracted; `{colors.hairline-control}` prescribed, since the border is this control's only edge) · hover (border to `{colors.hairline-control}`) · focus-visible (border to `{colors.ink}` as extracted, plus a prescribed 2px `{colors.focus}` ring at 2px offset) · active/pressed (same as focus-visible; the field has no distinct press) · disabled (`{colors.stone}` placeholder, border `{colors.hairline}`) · loading (border holds, submit button carries the spinner) · error (border and helper text to `{colors.accent-red}`, 5.55:1 on `{colors.canvas}`). No selected state.

### Navigation

**`nav-bar`** — top nav (desktop)
- Background `{colors.canvas}`, text `{colors.body}`, type `{typography.button-sm}`, height 64px, single hairline `{colors.hairline}` bottom border.
- Left: wordmark logo. Centre: top-level nav ("Features", "Pricing", "Docs", "Customers"). Right: "Sign in" link + `{component.button-primary}`.
- **States** — nav links: default (`{colors.body}`) · hover (`{colors.ink}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · selected (current route holds `{colors.ink}` and sets `aria-current`). No pressed, disabled, loading or error state.

**`nav-bar`** (mobile)
- Same height 64px, collapses centre nav into a hamburger icon. Logo stays left, sign-in CTA stays right.

**`sub-nav-pill`** — pill-style sub-nav
- Pill chips set in a horizontal row above content (e.g. on the customers index), `{component.sub-nav-pill}` styling.
- **States** — default · hover (label to `{colors.ink}`) · focus-visible (2px `{colors.focus}` ring, 2px offset) · selected (fill holds `{colors.surface-elevated}`, label `{colors.ink}`, border `{colors.hairline-control}`) · active/pressed (same as selected on pointer-down). No disabled, loading or error state.

### Signature Components

**`badge-pill`** — neutral pill
- Background `{colors.surface-elevated}`, text `{colors.body}`, type `{typography.caption}`, `rounded: {rounded.full}`, padding `4px 10px`.
- Inline tags ("New", "Beta", "v3.0") inside hero copy and customer story headers.
- **States** — default only when static. Where a badge links out it adds hover (label to `{colors.ink}`) and focus-visible (2px `{colors.focus}` ring, 2px offset); never pressed, disabled, loading, selected or error.

**`status-dot`** — status indicator
- Background `{colors.accent-green}`, `rounded: {rounded.full}`, 8px square.
- Inline indicator next to "Status: Operational" in the footer or system status references.
- **States** — two only, and deliberately so: operational (`{colors.accent-green}`) and degraded (`{colors.accent-red}`, which is the component's error state). Not interactive, so no hover, focus-visible, pressed, disabled, loading or selected state. Colour alone must never carry the status — the adjacent text label does.

**`contributor-avatar`** — testimonial avatar
- Background `{colors.surface-card}` placeholder, `rounded: {rounded.full}`, 32×32px.
- Used inline with customer testimonials.
- **States** — default · loading (placeholder `{colors.surface-card}` disc before the image resolves) · hover and focus-visible (2px `{colors.focus}` ring, 2px offset) only where the avatar links to a customer story. No pressed, disabled, selected or error state.

**`footer`** — global footer
- Background `{colors.canvas}`, text `{colors.charcoal}`, type `{typography.body-sm}`, `rounded: {rounded.none}`, padding `64px 32px`.
- Multi-column quick-links grid above a single-line copyright row separated by `{colors.divider-soft}`.
- **States** — the band itself has default only; its links carry hover (`{colors.charcoal}` to `{colors.ink}`) and focus-visible (2px `{colors.focus}` ring, 2px offset). No pressed, disabled, loading, selected or error state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted from Resend's running pages; the values are the shared **Crisp** profile from `theme-audit/SPEC.md`, chosen because Resend is a developer-tool identity whose state changes should read as instant — a terminal, not a showreel. Treat every number here as a specification to build to, not as a fact about the brand.

### Principles
- State changes read as immediate. Nothing in this brand choreographs an entrance; type and code simply appear and settle in under 150ms.
- Animate `transform` and `opacity` only — never `width`, `height`, `top`, `left` or `margin`. Colour and border-colour steps are paint-only and are stepped with the same duration token; they are the one documented deviation from the transform/opacity rule, and they trigger no layout.
- Every exit is shorter than its matching entrance.
- Atmospheric glows (`{colors.accent-orange-glow}` and siblings) are **static gradients**. They are not brand ambience and must never breathe, pulse or drift.
- Nothing animates on first paint in a way that delays content: the hero headline and its `{component.button-primary}` paint at full opacity.

### Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav link, card) | `{motion.duration-fast}` (100ms) | `{motion.ease-standard}` | `opacity`; colour / border-colour step | Kept, clamped to `{motion.duration-reduced}` (100ms) — opacity only, no travel |
| Press / active | `{motion.duration-instant}` (60ms) | `{motion.ease-standard}` | `opacity` 1 → 0.92. No scale pop; Crisp has no overshoot | Kept as-is — already opacity-only and under 100ms |
| Focus (focus-visible ring) | 0ms — the `{colors.focus}` ring appears on the same frame | none | `opacity` 0 → 1 on the ring only | Identical. A focus ring never animates in or out |
| Page / route transition | enter `{motion.duration-base}` (150ms) · exit `{motion.duration-fast}` (100ms) | enter `{motion.ease-enter}` · exit `{motion.ease-exit}` | `opacity` + `transform: translateY(4px → 0)` | Travel removed; opacity cross-fade at `{motion.duration-reduced}` |
| Modal / drawer | enter `{motion.duration-base}` (150ms) · exit `{motion.duration-fast}` (100ms) | enter `{motion.ease-enter}` · exit `{motion.ease-exit}` | `opacity` + `transform: scale(0.98 → 1)` (modal) or `translateX(100% → 0)` (drawer); backdrop `opacity` 0 → 1 | Scale and translate removed; panel and backdrop fade at `{motion.duration-reduced}` |
| Dropdown / popover | enter `{motion.duration-fast}` (100ms) · exit `{motion.duration-instant}` (60ms) | enter `{motion.ease-enter}` · exit `{motion.ease-exit}` | `opacity` + `transform: translateY(-4px → 0)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| Toast | enter `{motion.duration-base}` (150ms) · exit `{motion.duration-fast}` (100ms) | enter `{motion.ease-enter}` · exit `{motion.ease-exit}` | `opacity` + `transform: translateY(8px → 0)` | Travel removed; opacity only at `{motion.duration-reduced}`; dismiss timer unchanged |
| List enter (feature grid, pricing tiers, code tabs) | `{motion.duration-fast}` (100ms) per item, `{motion.stagger-step}` (20ms) offset, capped at 6 items | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px → 0)` | Stagger and travel removed; the whole list fades once at `{motion.duration-reduced}` |
| List exit | `{motion.duration-instant}` (60ms), no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | Kept, clamped to `{motion.duration-reduced}` |
| Loading | spinner 800ms per rotation, linear, infinite; skeleton shimmer 1200ms, linear, infinite | linear — a loader has no entrance to shape, so it sits outside the duration ladder deliberately | spinner `transform: rotate()`; skeleton `opacity` oscillation over a `{colors.hairline-strong}` block | Spinner freezes to a static indeterminate bar; shimmer removed, leaving a flat `{colors.hairline-strong}` block. Progress is announced through `aria-busy` / `aria-live`, not through movement |

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. No translateY, no translateX, no
     scale() anywhere — page transitions, modals, drawers, dropdowns, toasts
     and list reveals all become pure cross-fades. List stagger is removed,
     so a list fades as one block rather than item by item. The loading
     spinner stops rotating and the skeleton shimmer stops oscillating. */

  /* Kept: opacity fades, clamped to {motion.duration-reduced} (100ms), and
     every colour / border-colour step, which involves no movement. Focus
     rings, which never animated, are unchanged. The static atmospheric
     glows are unaffected because they were never animated. */

  *, *::before, *::after {
    animation-duration: 100ms !important;   /* {motion.duration-reduced} */
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;  /* {motion.duration-reduced} */
    transition-property: opacity, color, background-color, border-color !important;
  }
}
```

## Accessibility

Every ratio below is computed from this file's own token values with WCAG 2.1 relative luminance; translucent tones are flattened over the ground they are drawn on. Nothing here was measured from a rendered page, so overlap, clipping, real tap-target size and screen-reader order are outside what this document can claim.

### Measured contrast — key pairs

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#fcfdff` on `{colors.canvas}` `#000000` | 20.63:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-card}` `#0a0a0c` | 19.44:1 | 4.5:1 | Pass |
| `{colors.body}` (flattened `#d9dadb`) on `{colors.canvas}` | 15.0:1 | 4.5:1 | Pass |
| `{colors.charcoal}` (flattened `#b0b1b2`) on `{colors.canvas}` | 9.78:1 | 4.5:1 | Pass |
| `{colors.mute}` `#a1a4a5` on `{colors.canvas}` | 8.37:1 | 4.5:1 | Pass |
| `{colors.mute}` on `{colors.surface-card}` | 7.88:1 | 4.5:1 | Pass |
| `{colors.ash}` `#888e90` on `{colors.canvas}` | 6.32:1 | 4.5:1 | Pass |
| `{colors.ash}` on `{colors.surface-elevated}` `#101012` | 5.72:1 | 4.5:1 | Pass |
| `{colors.primary-on}` `#000000` on `{colors.primary}` `#fcfdff` | 20.63:1 | 4.5:1 | Pass — the white CTA is the strongest pair in the system |
| `{colors.on-light}` `#000000` on the `#ffffff` email inset (`{component.email-mockup-light}`) | 21.0:1 | 4.5:1 | Pass |
| `{colors.on-light-mute}` (flattened `#4d4d70` on white) on `#ffffff` | 8.04:1 | 4.5:1 | Pass |
| `{colors.link}` / `{colors.accent-blue}` `#3b9eff` on `{colors.canvas}` | 7.52:1 | 4.5:1 | Pass |
| `{colors.accent-red}` `#ff2047` on `{colors.canvas}` | 5.55:1 | 4.5:1 | Pass — usable as inline error text |
| `{colors.accent-orange}` `#ff801f` on `{colors.canvas}` | 8.36:1 | 4.5:1 | Pass |
| `{colors.accent-green}` `#11ff99` on `{colors.canvas}` | 15.79:1 | 4.5:1 | Pass |
| `{colors.accent-yellow}` `#ffc53d` on `{colors.canvas}` | 13.31:1 | 4.5:1 | Pass |
| `{colors.hairline-control}` (flattened `#5c5c5c`) on `{colors.canvas}` | 3.14:1 | 3.0:1 | Pass — the prescribed control boundary |
| `{colors.hairline-control}` (flattened `#626263`) on `{colors.surface-card}` | 3.25:1 | 3.0:1 | Pass |

### Where the real brand fails AA — disclosed, not fixed

These are extracted values and are left exactly as they are. Resend's translucent-white boundary system genuinely does not meet the 3:1 non-text contrast threshold of WCAG 1.4.11, and that is the honest fact about the brand:

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.hairline}` `rgba(255,255,255,0.06)` (flattened `#0f0f0f`) on `{colors.canvas}` | 1.1:1 | 3.0:1 | **Fail** — extracted and frozen. Decorative row and nav-bar edges only |
| `{colors.hairline}` (flattened `#19191b`) on `{colors.surface-card}` | 1.13:1 | 3.0:1 | **Fail** — extracted and frozen |
| `{colors.hairline-strong}` `rgba(255,255,255,0.14)` (flattened `#242424`) on `{colors.canvas}` | 1.35:1 | 3.0:1 | **Fail** — extracted and frozen, and this is the tone the real site uses as the *only* boundary of `{component.text-input}` |
| `{colors.hairline-strong}` (flattened `#2c2c2e`) on `{colors.surface-card}` | 1.42:1 | 3.0:1 | **Fail** — extracted and frozen |
| `{colors.divider-soft}` `rgba(255,255,255,0.04)` (flattened `#0a0a0a`) on `{colors.canvas}` | 1.06:1 | 3.0:1 | **Fail** — extracted. Footer column dividers; purely decorative, so 1.4.11 does not strictly apply |

The remedy is additive, not corrective: `{colors.hairline-control}` is defined above at 3.14:1 / 3.25:1 for any boundary that carries meaning. The extracted bindings in `components:` are left untouched, because they describe the product that actually ships. Re-pointing `{component.text-input}`, `{component.button-outline}` and `{component.button-ghost}` to `{colors.hairline-control}` is a brand-owner decision and is raised under Needs approval in the audit report.

`{colors.stone}` `#464a4d` reaches only 2.35:1 on `{colors.canvas}`. It is documented as the disabled foreground, and WCAG sets no contrast minimum on disabled controls, so it is exempt rather than failing — but it must never be used for live text.

### Focus ring visibility, per surface this file defines

Both rings are drawn outside the control at 2px width with a 2px offset, so each is judged against the surface *behind* the control, which is what WCAG 2.2 Focus Appearance measures. Neither ring is extracted; both reuse a hex the palette already owns.

| Ring | Surface | Ratio | Required | Verdict |
|---|---|---|---|---|
| `{colors.focus}` `#3b9eff` | `{colors.canvas}` `#000000` | 7.52:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.surface-card}` `#0a0a0c` | 7.08:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.surface-elevated}` `#101012` | 6.81:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.surface-deep}` `#06060a` | 7.24:1 | 3.0:1 | Pass |
| `{colors.focus}` | `{colors.surface-light}` `#f1f7fe` | 2.59:1 | 3.0:1 | Fail — which is why the second ring exists |
| `{colors.focus-on-light}` `#0075ff` | `{colors.surface-light}` `#f1f7fe` | 3.9:1 | 3.0:1 | Pass |
| `{colors.focus-on-light}` | `#ffffff` email inset | 4.21:1 | 3.0:1 | Pass |

Rule: use `{colors.focus}` on every dark surface; switch to `{colors.focus-on-light}` inside the white email-card insets and on `{colors.surface-light}`. The ring is never the only focus signal on `{component.text-input}`, which also steps its border to `{colors.ink}`.

### Tap targets

Not measurable from a document — these are the sizes the file specifies, not observed ones. `{component.button-primary}`, `{component.button-ghost}` and `{component.button-outline}` ship at 36px tall, below the 44×44px of WCAG 2.5.5 (AAA) and below 24×24px only when horizontal padding is stripped; `{component.sub-nav-pill}` at 36px and `{component.text-input}` at 40px sit in the same band. The Responsive Behavior section states that these scale to 44–48px on mobile via padding. Desktop at 36px meets WCAG 2.2 2.5.8 (24×24px, AA) and does not meet 2.5.5 (AAA); the file's existing claim that "WCAG AAA met on mobile" holds only for the mobile ladder.

### Other requirements
- **Colour is never the sole carrier of meaning.** `{component.status-dot}` always sits beside a text label; `{colors.accent-red}` error states pair with helper text, not just a red border.
- **Reduced motion** is honoured in full — see the `@media (prefers-reduced-motion: reduce)` rule above. All travel and scale are removed, opacity fades are clamped to `{motion.duration-reduced}` (100ms), and the loading spinner and skeleton shimmer freeze.
- **Type size floor.** `{typography.caption}` at 12px is the smallest role and is used only for footer disclosure and copyright. Body copy never drops below `{typography.body-sm}` (14px).
- **Not assessable here:** keyboard order, visible focus on scroll containers, screen-reader labelling of the code-window traffic lights, and any claim about overflow, clipping or layout shift. Those need a rendered page.

## Do's and Don'ts

### Do
- Use `{colors.canvas}` (true black) as the default page background. Every public page lives here.
- Reserve `{component.button-primary}` (white pill) as the only solid bright surface. One per viewport at most.
- Set hero headlines in **Domaine Display** at 76–96px with `lineHeight: 1.0` and `ss01 / ss04 / ss11` features engaged.
- Use **ABC Favorit** for marketing body, **Inter** for UI labels, **Geist Mono** for code. Keep the lanes strict.
- Build elevation from translucent-white hairlines, not drop shadows.
- Use `{colors.accent-*-glow}` tokens as low-opacity radial atmospheric washes — never as solid surfaces.
- Set buttons and inputs to `{rounded.md}` (8px); cards and code wells to `{rounded.lg}` (12px); pills and avatars to `{rounded.full}`.
- Use the white email-mockup inset sparingly — it's the only deliberately-light surface and should feel like a print pull-quote.

### Don't
- Don't use a near-black canvas. The brand sits on `#000000`, not `#0a0a0a`.
- Don't apply solid colour to atmospheric accent tokens. `{colors.accent-orange}` is for inline highlights only — its glow form is for backdrops.
- Don't add drop shadows to feature cards or code wells. Translucent white borders carry depth on this canvas.
- Don't bump body weight to 600 for emphasis. Use family change (Inter → ABC Favorit → Domaine Display) instead.
- Don't render code outside `{component.code-window}` — even small inline code uses Geist Mono and a `{colors.surface-card}` background.
- Don't loosen Domaine Display `lineHeight` past 1.0. Tight stacking is structural to the brand.
- Don't introduce a secondary brand accent. White is the brand on black — accents are atmospheric only.
- Don't bring photography front-and-centre. The brand reads as type-and-code, not photography-led.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop XL | ≥ 1440px | Full max-width 1200 body, 3-up feature grid, side-by-side code-story splits. |
| Desktop | 1280–1439px | Container shrinks; xl side padding. |
| Tablet Large | 1024–1279px | Feature grid stays 3-up, code-story remains 2-up. |
| Tablet | 768–1023px | Feature grid 2-up, code-story stacks (narrative on top), pricing stacks vertically. |
| Mobile Large | 426–767px | Feature grid 1-up; nav collapses to hamburger; hero `{typography.display-xxl}` clamps to 56px. |
| Mobile | ≤ 425px | All grids 1-up, hero clamps to 44px, section padding `{spacing.section}` collapses to 64px. |

### Touch Targets
- All buttons ship at minimum 36px tall on desktop, scaling to 44px on mobile via padding adjustment. WCAG AAA met on mobile.
- `{component.text-input}` is 40px tall — comfortable but not large. Mobile scales to 48px via padding.
- `{component.sub-nav-pill}` stays at 36px on desktop, 40px on mobile.

### Collapsing Strategy
- Top-level nav collapses to hamburger at < 1024px; the wordmark and `{component.button-primary}` stay anchored.
- Hero `{typography.display-xxl}` clamps: 96px → 76px → 56px → 44px across the breakpoint ladder.
- Pricing 3-up stacks vertically at < 1024px with the featured tier remaining centre-stacked.
- Code-story splits switch from side-by-side to stacked at < 1024px, code well always second.
- Atmospheric glows scale with section width but maintain the same opacity — they fade naturally at small viewports.

### Image Behavior
- Email mockup cards reflow at 1:1 aspect on mobile to remain readable.
- Atmospheric glows are CSS gradients — no asset cost, no breakpoint variation.
- Customer testimonial avatars stay 32px circular regardless of breakpoint.

## Iteration Guide

1. Focus on ONE component at a time. Most surfaces share `{colors.surface-card}` or `{colors.surface-elevated}` with `{rounded.lg}` — only the role-specific tokens (`{colors.primary}`, `{component.code-window}`) shift between variants.
2. Reference component names and tokens directly (`{colors.primary}`, `{component.button-primary-pressed}`, `{rounded.lg}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits; orphaned-tokens warnings will catch unused entries.
4. Add new variants as separate entries (`-pressed`, `-featured`, `-disabled`) — do not bury them in prose.
5. Default body type to `{typography.body-md}`; reach for `{typography.subtitle}` only on hero subtitles.
6. Keep `{colors.primary}` (white) scarce — if more than one solid white surface appears per viewport, ask whether one should drop to `{component.button-ghost}` instead.

## Known Gaps

- Pressed/active visual states are documented only for `button-primary-pressed`; other components rely on the default focus-ring (browser default) for interactive feedback.
- Logged-in dashboard surfaces (API keys, sending logs, audience management) are out of scope; only the public marketing canvas is documented.
- Email-template editor surfaces (a key product feature) are not extracted — those live behind authentication.
- The atmospheric glow rendering uses CSS radial gradients; exact stops and angles vary per section and are not standardised as tokens — render per section-specific design judgment.
