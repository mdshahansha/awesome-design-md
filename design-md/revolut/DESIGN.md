---
version: alpha
name: Revolut-design-analysis
description: |
  Revolut's marketing surfaces pair a stark black canvas with the brand's
  cobalt-violet (`#494fdf`) and a wide accent palette of deep, fully-saturated
  product colours — teal, light-blue, deep pink, light-green, warning orange.
  The system reads as fintech-meets-product-brochure: oversized 80px–136px
  Aeonik Pro display headlines, generous whitespace, photography-led hero
  bands, and full-width product mockups (cards, phones, terminals) shown as
  hero objects inside near-black sections. Most surfaces are either black or
  off-white; pill-shaped buttons and rounded-12/20px content cards carry the
  consumer-financial-app feel without crossing into playful territory.

colors:
  primary: "#494fdf"
  primary-bright: "#4f55f1"
  primary-deep: "#3a40c4"
  on-primary: "#ffffff"
  ink: "#191c1f"
  body: "#1f2226"
  charcoal: "#3a3d40"
  mute: "#505a63"
  ash: "#5c5e60"
  stone: "#8d969e"
  faint: "#c9c9cd"
  on-dark: "#ffffff"
  on-dark-mute: "rgba(255,255,255,0.72)"
  canvas-light: "#ffffff"
  canvas-dark: "#000000"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-deep: "#0a0a0a"
  surface-elevated: "#16181a"
  hairline-light: "#e2e2e7"
  hairline-dark: "rgba(255,255,255,0.12)"
  hairline-strong: "#191c1f"
  divider-soft: "rgba(255,255,255,0.06)"
  accent-teal: "#00a87e"
  accent-blue-link: "#376cd5"
  accent-light-blue: "#007bc2"
  accent-light-green: "#428619"
  accent-green-text: "#006400"
  accent-yellow: "#b09000"
  accent-warning: "#ec7e00"
  accent-pink: "#e61e49"
  accent-danger: "#e23b4a"
  accent-deep-red: "#8b0000"
  accent-brown: "#936d62"
  link: "#376cd5"
  focus: "#494fdf"
  focus-on-dark: "#ffffff"

typography:
  display-xxl:
    fontFamily: Aeonik Pro
    fontSize: 136px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: -2.72px
  display-xl:
    fontFamily: Aeonik Pro
    fontSize: 80px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: -0.8px
  display-lg:
    fontFamily: Aeonik Pro
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.21
    letterSpacing: -0.48px
  display-md:
    fontFamily: Aeonik Pro
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.4px
  heading-lg:
    fontFamily: Aeonik Pro
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.19
    letterSpacing: -0.32px
  heading-md:
    fontFamily: Aeonik Pro
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  heading-sm:
    fontFamily: Aeonik Pro
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: -0.09px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.24px
  body-md-bold:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.16px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
  button-lg:
    fontFamily: Aeonik Pro
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
  button-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.24px
  button-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
  caption:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
  link-emph:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.24px

rounded:
  none: 0px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 28px
  full: 9999px

spacing:
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 14px
  lg: 16px
  xl: 24px
  xxl: 32px
  xxxl: 48px
  block: 80px
  section: 88px
  band: 120px

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
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.canvas-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-pressed:
    backgroundColor: "{colors.faint}"
    textColor: "{colors.canvas-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-soft:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-outline-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-outline-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-pill-sm:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 14px 16px
    height: 56px
  hero-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xxl}"
    rounded: "{rounded.none}"
    padding: 88px 24px
  hero-band-photo:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: 0
  feature-card-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  feature-card-dark:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  plan-card:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  plan-card-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  product-mockup:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xl}"
    padding: 48px
  download-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 56px
  badge-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-feature:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 64px
  sub-nav-pill:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark-mute}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 80px 24px
---

## Overview

Revolut's marketing canvas operates in a high-contrast two-mode system: a
**near-black storytelling canvas** (`{colors.canvas-dark}` — `#000000`)
that hosts hero bands, product mockups, and the planning section, alternating
with **white catalogue bands** (`{colors.canvas-light}` — `#ffffff`) that
host comparison tables, FAQ rows, and download tiles. The two modes switch
in full-bleed bands rather than soft transitions; sections slam against each
other to create the magazine-spread rhythm the brand is known for.

The display typography is **Aeonik Pro at weight 500**, used at sizes from
20px to 136px. The flagship hero ("Banking & Beyond", "Join the 70+ million
using Revolut") sits at 80–136px with `lineHeight: 1.0` and tight negative
letter-spacing. Body type is **Inter** at weight 400 — open-source,
no-nonsense, paired with positive tracking (`0.24px`) on UI labels for
slightly more mechanical precision.

The brand accent is `{colors.primary}` (`#494fdf`) — a saturated cobalt
violet — but it appears scarcely on marketing surfaces. The actual primary
CTA on the hero is the **white pill on black** ("Choose your subscription"),
and the cobalt violet is reserved for featured plan cards, secondary CTAs in
white sections, and the brand glyph itself. A wide secondary palette of deep
teal, light-blue, deep-pink, light-green, warning orange, and yellow appears
inside product mockups and feature illustrations — never as button surfaces.

**Key Characteristics:**
- Two-mode canvas system — `{colors.canvas-dark}` (true black) for storytelling, `{colors.canvas-light}` (white) for browsing — switched in full-bleed bands.
- Display typography is **Aeonik Pro 500** at sizes 20–136px with tight `lineHeight: 1.0` and large negative letter-spacing on display sizes.
- The actual primary CTA is `{component.button-primary}` — a **white pill with black text**, sitting on the dark canvas as the brightest pixel. Cobalt-violet `{colors.primary}` is reserved for featured plan cards and secondary CTAs.
- Eight saturated accent colours live inside product mockups and illustrations only, never as button surfaces — teal, light-blue, deep-pink, light-green, warning orange, yellow, brown, danger red.
- All buttons are pill-shaped (`{rounded.full}`); content cards use `{rounded.lg}` (20px); inputs and small chips use `{rounded.md}` (12px).
- Photography is product-led — phone mockups, card mockups, terminal mockups — shown full-bleed inside dark sections with no caption overlay.

## Colors

### Brand & Accent
- **Cobalt Violet** (`{colors.primary}` — `#494fdf`): the brand accent. Reserved for featured plan cards (`{component.plan-card-featured}`), the brand wordmark icon, and secondary CTAs in white-canvas regions.
- **Cobalt Bright** (`{colors.primary-bright}` — `#4f55f1`): a one-step-up bright variant used in inline link colour and accent-photo headers.
- **Cobalt Deep** (`{colors.primary-deep}` — `#3a40c4`): the active/pressed state of cobalt elements.
- **On-Primary** (`{colors.on-primary}` — `#ffffff`): label colour on top of `{colors.primary}` surfaces.

### Surface
- **Canvas Light** (`{colors.canvas-light}` — `#ffffff`): the white catalogue mode for FAQ, download tiles, comparison tables.
- **Canvas Dark** (`{colors.canvas-dark}` — `#000000`): the storytelling canvas — true black, never near-black.
- **Surface Soft** (`{colors.surface-soft}` — `#f4f4f4`): a subtle off-white used on download tiles, soft buttons, and inset card groups inside white bands.
- **Surface Card** (`{colors.surface-card}` — `#ffffff`): pure white card surface, used for feature cards in white-canvas regions.
- **Surface Deep** (`{colors.surface-deep}` — `#0a0a0a`): a one-step-up dark surface for inset cards inside black-canvas regions.
- **Surface Elevated** (`{colors.surface-elevated}` — `#16181a`): the planning-section card background — slightly luminous, lifts plan cards off the black canvas.
- **Hairline Light** (`{colors.hairline-light}` — `#e2e2e7`): 1px dividers inside white bands.
- **Hairline Dark** (`{colors.hairline-dark}` — `rgba(255,255,255,0.12)`): the corresponding low-contrast divider in dark regions.
- **Hairline Strong** (`{colors.hairline-strong}` — `#191c1f`): structural full-strength dividers and the outline of light cards.

### Text
- **Ink** (`{colors.ink}` — `#191c1f`): primary text colour. Notably warmer than pure black, paired with the white canvas for body legibility.
- **Body** (`{colors.body}` — `#1f2226`): long-form body where `{colors.ink}` would feel slightly too sharp.
- **Charcoal** (`{colors.charcoal}` — `#3a3d40`): captions, secondary nav.
- **Mute** (`{colors.mute}` — `#505a63`): supporting text.
- **Ash** (`{colors.ash}` — `#5c5e60`): tertiary text, footer copy.
- **Stone** (`{colors.stone}` — `#8d969e`): metadata, subtle captions.
- **Faint** (`{colors.faint}` — `#c9c9cd`): disabled foreground, hairline replacements.
- **On-Dark** (`{colors.on-dark}` — `#ffffff`): primary text on `{colors.canvas-dark}`.
- **On-Dark Mute** (`{colors.on-dark-mute}` — `rgba(255,255,255,0.72)`): secondary text in dark regions.

### Focus

The two-mode canvas needs two rings; one value cannot clear 3:1 on both white
and true black. Both reuse tones the palette already owns — neither is a new
brand colour.

- **Focus Ring** (`{colors.focus}` — `#494fdf`): the ring for light-canvas surfaces. The same hex as `{colors.primary}`, so focus reads as the brand stamp. Measures 6.06:1 on `{colors.canvas-light}` and 5.51:1 on `{colors.surface-soft}`.
- **Focus Ring On Dark** (`{colors.focus-on-dark}` — `#ffffff`): the ring for dark-canvas surfaces and for the cobalt featured card. The same hex as `{colors.on-dark}`. Measures 21.00:1 on `{colors.canvas-dark}`, 19.80:1 on `{colors.surface-deep}`, 17.80:1 on `{colors.surface-elevated}` and 6.06:1 on `{colors.primary}`.

Both rings are drawn **outside** the control: 2px ring, 2px offset, so the ring
is judged against the surface behind the control rather than the control fill.
That is what keeps a ring legible around the white `{component.button-primary}`
pill sitting on black.

### Semantic
- **Accent Teal** (`{colors.accent-teal}` — `#00a87e`): used in product mockup illustrations.
- **Accent Light Blue** (`{colors.accent-light-blue}` — `#007bc2`): inline link colour in dark photo headers.
- **Accent Blue Link** (`{colors.accent-blue-link}` — `#376cd5`): default inline link colour on white surfaces.
- **Accent Light Green** (`{colors.accent-light-green}` — `#428619`): success / positive product callouts.
- **Accent Green Text** (`{colors.accent-green-text}` — `#006400`): inline success text.
- **Accent Yellow** (`{colors.accent-yellow}` — `#b09000`): caution / pending state in product mockups.
- **Accent Warning** (`{colors.accent-warning}` — `#ec7e00`): full-saturation orange used in warning illustrations.
- **Accent Pink** (`{colors.accent-pink}` — `#e61e49`): deep pink — used inside product photography and category iconography.
- **Accent Danger** (`{colors.accent-danger}` — `#e23b4a`): destructive / error state.
- **Accent Deep Red** (`{colors.accent-deep-red}` — `#8b0000`): inline error text.
- **Accent Brown** (`{colors.accent-brown}` — `#936d62`): a single warm-neutral used in metals tier card chrome.
- **Link** (`{colors.link}` — `#376cd5`): default inline link colour. Same as `{colors.accent-blue-link}`.

## Typography

### Font Family

Revolut ships a two-family stack:

- **Aeonik Pro** — proprietary humanist sans-serif used for all display sizes (20px+) at weight 500. Carries the brand's editorial confidence; tightens dramatically with negative letter-spacing at large sizes.
- **Inter** — open-source workhorse for body, button labels, captions, and metadata. Always at weight 400 or 600, with positive tracking (`0.16–0.24px`) on UI labels.

When Aeonik Pro cannot be licensed, **Inter Display**, **General Sans**, or **Söhne** are credible substitutes — all share the warm geometric character. Apply -1% letter-spacing on display sizes to match the original tightness.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 136px | 500 | 1.0 | -2.72px | The flagship hero ("Banking & Beyond"). One per page. |
| `{typography.display-xl}` | 80px | 500 | 1.0 | -0.8px | Section openers ("Join the 70+ million using Revolut"). |
| `{typography.display-lg}` | 48px | 500 | 1.21 | -0.48px | Sub-section titles. |
| `{typography.display-md}` | 40px | 500 | 1.2 | -0.4px | Feature card titles. |
| `{typography.heading-lg}` | 32px | 500 | 1.19 | -0.32px | Plan card titles. |
| `{typography.heading-md}` | 24px | 500 | 1.33 | 0 | Section sub-titles. |
| `{typography.heading-sm}` | 20px | 500 | 1.4 | 0 | List headers, prominent labels. |
| `{typography.body-lg}` | 18px | 400 | 1.56 | -0.09px | Marketing prose. |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0.24px | Default body. |
| `{typography.body-md-bold}` | 16px | 600 | 1.5 | 0.16px | Emphatic body. |
| `{typography.body-sm}` | 14px | 400 | 1.43 | 0 | Captions, metadata. |
| `{typography.button-lg}` | 20px | 500 | 1.4 | 0 | Hero CTAs (Aeonik Pro). |
| `{typography.button-md}` | 16px | 600 | 1.5 | 0.24px | Default button label. |
| `{typography.button-sm}` | 14px | 600 | 1.43 | 0 | Pill chips, sub-nav. |
| `{typography.caption}` | 13px | 400 | 1.4 | 0 | Footer disclosure, regulatory text. |
| `{typography.link-emph}` | 16px | 700 | 1.5 | 0.24px | Emphatic inline link in dark mode. |

### Principles
- Display sizes always run at weight 500 with `lineHeight: 1.0` (or 1.19–1.21 below 48px). The negative letter-spacing scales with size — bigger types tighten more.
- Body Inter sits at weight 400 with positive tracking (`0.24px`) — the small spacing nudge makes UI labels feel slightly mechanical, fitting fintech precision.
- Hero CTAs use the Aeonik Pro `{typography.button-lg}` variant; everything below the hero uses the Inter `{typography.button-md}`.
- Inline links inside dark photo regions step up to weight 700 (`{typography.link-emph}`) so they hold contrast against the canvas without using the cobalt accent.

### Note on Font Substitutes

When Aeonik Pro is unavailable, clamp display `lineHeight` to 1.0 explicitly and apply -1% letter-spacing on display sizes. Inter Display, General Sans, or Söhne will read closest to the original. Inter is open-source and should be used directly.

## Layout

### Spacing System
- **Base unit**: 4px, with the working scale on multiples of 4 / 8 / 16.
- **Tokens**: `{spacing.xxs}` 4px · `{spacing.xs}` 6px · `{spacing.sm}` 8px · `{spacing.md}` 14px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.xxxl}` 48px · `{spacing.block}` 80px · `{spacing.section}` 88px · `{spacing.band}` 120px.
- Section padding: `{spacing.section}` (88px) vertical between bands; `{spacing.band}` (120px) on the hero band and the closing planning section.
- Card internal padding: `{spacing.xxl}` (32px) on `{component.feature-card-light}`, `{component.plan-card}`, `{component.feature-card-dark}`.

### Grid & Container
- **Max content width** ≈ 1200px on body sections; hero bands run full-bleed.
- **Plan grid**: 4-up plan cards on the home page, stacking 2-up at tablet and 1-up at small mobile.
- **Feature grid**: 3-up at desktop, 2-up at tablet, 1-up at mobile.
- **Product mockup bands**: a single full-width hero photo of a phone or card mockup, no surrounding chrome — the asset itself is the section.

### Whitespace Philosophy
- Whitespace is generous and editorial — sections breathe at 88–120px so display headlines have room to register at 80–136px without feeling cramped.
- Inside cards, padding stays at 32px so feature copy and plan tiers have a consistent rhythm.
- Hairline `{colors.hairline-light}` dividers replace shadow on white surfaces; `{colors.hairline-dark}` carries the corresponding role in dark regions.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | No shadow, no border | Default canvas bands (light or dark), full-bleed hero. |
| 1 — surface card | `{colors.surface-card}` (white) on `{colors.surface-soft}` band | Feature cards inside light bands. |
| 2 — surface elevated dark | `{colors.surface-elevated}` (`#16181a`) on `{colors.canvas-dark}` | Plan cards inside the planning section. |
| 3 — featured surface | `{colors.primary}` on `{colors.canvas-dark}` | Featured plan card (cobalt violet inversion). |
| 4 — product mockup | Full-bleed photo asset | Hero phone / card / terminal mockup bands. |

The system has **no traditional drop-shadow language**. Surfaces register depth via colour-blocking (light → dark band switches) and surface-luminance shifts (`{colors.canvas-dark}` → `{colors.surface-elevated}`). Photography mockups carry their own depth from the asset itself.

### Decorative Depth
- **Product mockup hero bands** — the home page features a phone mockup full-bleed against `{colors.canvas-dark}`, with the device's own glow providing the only atmospheric depth. No additional gradients, no shadows.
- **Featured plan card** — the cobalt-violet `{component.plan-card-featured}` sits inside the otherwise dark planning grid as a single saturated colour block, marking the recommended tier visually.
- **Card metals tier** — the brand uses `{colors.accent-brown}` and a deep gradient on metals card mockups to signal premium without resorting to gold-on-black metallic effects.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Hero bands, full-bleed sections, footer. |
| `{rounded.sm}` | 8px | Inline tags, small chips. |
| `{rounded.md}` | 12px | Form inputs, download tiles. |
| `{rounded.lg}` | 20px | Feature cards, plan cards. |
| `{rounded.xl}` | 28px | Product mockup containers. |
| `{rounded.full}` | 9999px | Buttons, pills, badges, tabs. |

### Photography Geometry
- Phone mockups: 9:19.5 (vertical) with `{rounded.xl}` corners on the device chrome.
- Card mockups: 1.586:1 (credit-card aspect) with `{rounded.lg}` corners.
- Terminal/POS mockups: 4:3 with `{rounded.xl}` corners and substantial padding around the device.
- Lifestyle photography (rare): 16:9 with `{rounded.lg}` corners.

## Components

Only `default` and `pressed` were extracted from the live marketing pages. The
other states below are **prescribed** for implementers and are labelled as such
in each entry; they are not observed facts about the real site.

### Buttons

**`button-primary`** — white CTA on dark
- Background `{colors.canvas-light}`, label `{colors.canvas-dark}`, type `{typography.button-md}`, padding `14px 28px`, `rounded: {rounded.full}`, height 48px.
- The brand's primary CTA, used on every dark hero band ("Choose your subscription", "Get started").
- Pressed state lives in `button-primary-pressed` (background `{colors.faint}`).
- States: `default` (extracted), `active/pressed` (extracted — `{component.button-primary-pressed}`); prescribed: `hover` (opacity 0.88 on the white fill), `focus-visible` (2px `{colors.focus-on-dark}` ring, 2px offset — the pill sits on dark canvas), `disabled` (fill `{colors.faint}`, label `{colors.stone}`), `loading` (label swapped for an indeterminate indicator, control width held).

**`button-dark`** — dark CTA on light
- Background `{colors.canvas-dark}`, label `{colors.on-dark}`, type `{typography.button-md}`, `rounded: {rounded.full}`.
- The reverse-canvas equivalent of `{component.button-primary}` — used inside white catalogue bands.
- States: `default` (extracted); prescribed: `hover` (opacity 0.88), `focus-visible` (2px `{colors.focus}` ring, 2px offset — the control sits on `{colors.canvas-light}`), `active/pressed` (fill `{colors.body}`), `disabled` (fill `{colors.faint}`, label `{colors.stone}`), `loading` (indeterminate indicator in `{colors.on-dark}`).

**`button-soft`** — soft surface CTA
- Background `{colors.surface-soft}`, label `{colors.ink}`, type `{typography.button-md}`, `rounded: {rounded.full}`.
- Tertiary action in white-canvas regions ("Learn more", "View FAQs").
- States: `default` (extracted); prescribed: `hover` (fill steps to `{colors.faint}`), `focus-visible` (2px `{colors.focus}` ring, 2px offset), `active/pressed` (fill `{colors.faint}`, label `{colors.body}`), `disabled` (label `{colors.stone}`). No `loading` — tertiary actions are navigational.

**`button-outline-light`** — outlined CTA on light
- Background `{colors.canvas-light}`, label `{colors.ink}`, 1px solid `{colors.hairline-strong}`, type `{typography.button-md}`, `rounded: {rounded.full}`.
- Secondary action when paired with `{component.button-dark}`.
- States: `default` (extracted); prescribed: `hover` (border steps to `{colors.ink}`, fill `{colors.surface-soft}`), `focus-visible` (2px `{colors.focus}` ring, 2px offset), `active/pressed` (fill `{colors.surface-soft}`), `disabled` (border and label `{colors.faint}`).

**`button-outline-dark`** — outlined CTA on dark
- Background `{colors.canvas-dark}`, label `{colors.on-dark}`, 1px solid `{colors.on-dark}`, type `{typography.button-md}`, `rounded: {rounded.full}`, padding `13px 27px`, height 48px.
- Dark-canvas counterpart of `{component.button-outline-light}`; used inside dark hero bands as a tertiary action when paired with `{component.button-primary}`.
- States: `default` (extracted); prescribed: `hover` (border opacity to 100%, fill `{colors.surface-elevated}`), `focus-visible` (2px `{colors.focus-on-dark}` ring, 2px offset), `active/pressed` (fill `{colors.surface-deep}`), `disabled` (border and label at `{colors.on-dark-mute}`).

**`button-pill-sm`** — small pill chip
- Background `{colors.surface-soft}`, label `{colors.ink}`, type `{typography.button-sm}`, `rounded: {rounded.full}`, padding `8px 16px`, height 36px.
- Sub-nav chips, filter pills.
- States: `default` (extracted); prescribed: `hover` (fill `{colors.faint}`), `focus-visible` (2px `{colors.focus}` ring, 2px offset), `active/pressed` (fill `{colors.faint}`), `selected` (fill `{colors.canvas-dark}`, label `{colors.on-dark}` — the filter pill is the one chip with a selected state), `disabled` (label `{colors.stone}`).

### Cards & Containers

**`hero-band-dark`** — full-bleed dark hero
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, type `{typography.display-xxl}` for the title, padding `{spacing.section}` (88px) vertical, `rounded: {rounded.none}`.
- Used only on the home page hero band.
- States: `default` only. A full-bleed band is not an interactive control, so it has no hover, focus, pressed, disabled, loading, selected or error state.

**`hero-band-photo`** — photo-led hero
- Background `{colors.canvas-dark}` with full-bleed product photography, text `{colors.on-dark}`, type `{typography.display-xl}`, `rounded: {rounded.none}`.
- Used on product pages — phone or card mockup as the full-band canvas.
- States: `default` only, as for `{component.hero-band-dark}`. Any interactivity belongs to the buttons inside the band, not the band.

**`feature-card-light`** — feature card on white
- Background `{colors.surface-card}`, text `{colors.ink}`, 1px solid `{colors.hairline-light}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}` (32px).
- Used in white catalogue bands for feature comparisons.
- States: `default` (extracted); prescribed, where the card is a link: `hover` (border steps from `{colors.hairline-light}` to `{colors.hairline-strong}`; no shadow, no lift), `focus-visible` (2px `{colors.focus}` ring, 2px offset), `active/pressed` (fill `{colors.surface-soft}`). A non-linked card is `default` only.

**`feature-card-dark`** — feature card on dark
- Background `{colors.surface-elevated}`, text `{colors.on-dark}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}`.
- Used inside dark storytelling sections.
- States: `default` (extracted); prescribed, where the card is a link: `hover` (fill steps `{colors.surface-elevated}` → `{colors.surface-deep}` inverted, i.e. one luminance step up), `focus-visible` (2px `{colors.focus-on-dark}` ring, 2px offset). A non-linked card is `default` only.

**`plan-card`** — subscription plan card
- Background `{colors.surface-elevated}`, text `{colors.on-dark}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}` (32px).
- Plan name in `{typography.heading-lg}` ("Standard", "Plus", "Premium", "Metal", "Ultra").
- States: `default` (extracted); prescribed: `hover` (one luminance step up on the surface), `focus-visible` (2px `{colors.focus-on-dark}` ring, 2px offset), `selected` (the chosen tier; rendered as `{component.plan-card-featured}`), `loading` (price row replaced by a placeholder block while tier pricing resolves per market).

**`plan-card-featured`** — featured plan card
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}`.
- Cobalt-violet inversion of `{component.plan-card}` — used on the recommended tier.
- States: `default` (extracted) and `selected` — this card *is* the selected/recommended presentation of `{component.plan-card}`. Prescribed: `focus-visible` (2px `{colors.focus-on-dark}` ring, 2px offset — `{colors.focus}` would vanish at 1.00:1 on the cobalt fill).

**`product-mockup`** — full-bleed product asset
- Background `{colors.canvas-dark}`, the asset itself fills the band, `rounded: {rounded.xl}` on the device chrome.
- Phone, card, and terminal mockups — no caption overlay, no surrounding chrome.
- States: `default` only. It is a photographic asset, not a control.

**`download-tile`** — app store download tile
- Background `{colors.surface-soft}`, text `{colors.ink}`, type `{typography.body-sm}`, `rounded: {rounded.md}`, padding `12px 20px`, height 56px.
- App Store + Google Play download buttons, side-by-side.
- States: `default` (extracted); prescribed: `hover` (fill `{colors.faint}`), `focus-visible` (2px `{colors.focus}` ring, 2px offset), `active/pressed` (fill `{colors.faint}`, label `{colors.body}`).

### Inputs & Forms

**`text-input`** — default input
- Background `{colors.canvas-light}`, text `{colors.ink}`, type `{typography.body-md}`, 1px solid `{colors.hairline-light}`, `rounded: {rounded.md}`, padding `14px 16px`, height 56px.
- Generous height for fintech accessibility — the documented height comfortably exceeds the 44px WCAG 2.5.5 target. Not verified on a rendered page; see Known Gaps.
- The extracted 1px `{colors.hairline-light}` boundary measures 1.29:1 on `{colors.canvas-light}` — below the 3:1 that a control boundary needs. It is kept as extracted because it is a fact about the real site; `{colors.hairline-strong}` (17.11:1) is the accessible boundary an implementer should draw instead. Re-pointing the extracted binding is a brand-owner decision.
- States: `default` (extracted); prescribed: `hover` (boundary steps to `{colors.hairline-strong}`), `focus-visible` (2px `{colors.focus}` ring, 2px offset, boundary `{colors.hairline-strong}`), `disabled` (fill `{colors.surface-soft}`, text `{colors.stone}`), `error` (boundary and message text `{colors.accent-deep-red}` — `10.01:1` on `{colors.canvas-light}`, not `{colors.accent-danger}` at `4.24:1`). No `loading`, no `selected`.

### Navigation

**`nav-bar`** — top nav (desktop)
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, type `{typography.button-md}`, height 64px.
- Left: wordmark logo. Centre: top-level nav ("Personal", "Business", "Company"). Right: language switcher + "Log in" + `{component.button-primary}`.
- States, per nav item: `default` (extracted); prescribed: `hover` (label to `{colors.on-dark}` at full opacity from `{colors.on-dark-mute}`), `focus-visible` (2px `{colors.focus-on-dark}` ring, 2px offset), `active/pressed` (label `{colors.on-dark-mute}`), `selected` (current section — label `{colors.on-dark}` with a 2px underline in `{colors.on-dark}`). The bar itself has one state.

**`nav-bar`** (mobile)
- Same height 64px, collapses centre nav into a hamburger icon. Logo stays left, sign-in CTA stays right.
- States: the hamburger carries `default`, `hover`, `focus-visible` (2px `{colors.focus-on-dark}` ring), `active/pressed` and `selected` (menu open). Prescribed except `default`.

**`sub-nav-pill`** — sub-nav chip
- Pill chips set in a horizontal row inside dark sections (e.g. "Personal", "Business", "Premium"), `{component.sub-nav-pill}` styling.
- States: `default` (extracted); prescribed: `hover` (fill one luminance step up), `focus-visible` (2px `{colors.focus-on-dark}` ring, 2px offset), `active/pressed` (fill `{colors.surface-deep}`), `selected` (fill `{colors.canvas-light}`, label `{colors.canvas-dark}` — the active section chip).

### Signature Components

**`badge-tag`** — neutral tag
- Background `{colors.surface-soft}`, text `{colors.ink}`, type `{typography.caption}`, `rounded: {rounded.full}`, padding `4px 12px`.
- Inline tags inside feature cards.
- States: `default` only — a tag is a label, not a control.

**`badge-feature`** — feature highlight badge
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.caption}`, `rounded: {rounded.full}`, padding `4px 12px`.
- "New", "Most popular" badges anchored on plan cards.
- States: `default` only — a badge is a label, not a control.

**`footer`** — global footer
- Background `{colors.canvas-dark}`, text `{colors.on-dark-mute}`, type `{typography.body-sm}`, `rounded: {rounded.none}`, padding `80px 24px`.
- Multi-column quick-links grid above a copyright + regulatory disclosure block separated by `{colors.divider-soft}`.
- States, per footer link: `default` (extracted); prescribed: `hover` (label `{colors.on-dark-mute}` → `{colors.on-dark}`), `focus-visible` (2px `{colors.focus-on-dark}` ring, 2px offset), `active/pressed` (label `{colors.on-dark-mute}`). The footer container has one state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** No timing function, duration or easing curve
below was extracted from Revolut's pages; they follow the audit's **Cinematic**
profile, chosen because the brand's surfaces are photography-led full-bleed
bands with 80–136px display type and sparse content — type that should arrive
late and settle, not snap.

Every value references a `{motion.*}` token. Only `transform` and `opacity`
animate; `width`, `height`, `top`, `left` and `margin` never do.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, pills, cards) | `{motion.duration-fast}` (240ms) | `{motion.ease-standard}` | `opacity` on the fill; `transform: none` | Same opacity change at `{motion.duration-reduced}` (150ms). No change otherwise. |
| Press / active | `{motion.duration-instant}` (120ms) | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed entirely; the extracted `{component.button-primary-pressed}` colour change is the only feedback. |
| Focus (`focus-visible` ring) | `{motion.duration-instant}` (120ms) | `{motion.ease-standard}` | `opacity` on the 2px ring | Ring appears instantly at full opacity. Never suppressed. |
| Page / route transition | `{motion.duration-slow}` (600ms) enter, `{motion.duration-fast}` (240ms) exit | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` 0→1 with `transform: translateY(16px)` → `none` | Travel removed; opacity cross-fade at `{motion.duration-reduced}`. |
| Hero band reveal (display type settling) | `{motion.duration-emphasis}` (900ms), lines staggered by `{motion.stagger-step}` (80ms) | `{motion.ease-enter}` | `opacity` with `transform: translateY(24px)` → `none` | Travel and stagger removed; a single opacity fade at `{motion.duration-reduced}`. Content is never withheld — the band paints at final layout and the fade runs over it. |
| Modal / drawer | `{motion.duration-base}` (400ms) enter, `{motion.duration-fast}` (240ms) exit | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` on the scrim; `transform: translateY(100%)` → `none` on a drawer, `scale(0.98)` → `1` on a modal | Travel and scale removed; scrim and panel fade at `{motion.duration-reduced}`. |
| Dropdown (language switcher, nav menu) | `{motion.duration-fast}` (240ms) enter, `{motion.duration-instant}` (120ms) exit | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` with `transform: translateY(-8px)` → `none` | Travel removed; opacity only at `{motion.duration-reduced}`. |
| Toast | `{motion.duration-base}` (400ms) enter, `{motion.duration-fast}` (240ms) exit | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` with `transform: translateY(16px)` → `none` | Travel removed; opacity only at `{motion.duration-reduced}`. Dismiss timing is unchanged. |
| List enter (plan grid, feature grid) | `{motion.duration-slow}` (600ms) per item, staggered by `{motion.stagger-step}` (80ms) | `{motion.ease-enter}` | `opacity` with `transform: translateY(20px)` → `none` | Travel and stagger removed; all items fade together at `{motion.duration-reduced}`. |
| List exit (filtered-out items) | `{motion.duration-fast}` (240ms), no stagger | `{motion.ease-exit}` | `opacity` 1→0 with `transform: scale(0.98)` | Scale removed; opacity only at `{motion.duration-reduced}`. |
| Loading (indeterminate) | `{motion.duration-emphasis}` (900ms) per cycle, infinite | linear for rotation, `{motion.ease-standard}` for a pulse | `transform: rotate()` on a spinner, or `opacity` on a placeholder block | Rotation frozen; an `opacity` pulse at `{motion.duration-reduced}` or a static indicator with a text label. |

Exit is always shorter than its matching entrance. Nothing in the list above
delays first paint: entrance animations run over content that is already laid
out at its final position.

### Brand ambience

The one continuous motion the brand would support is the slow scale of a
full-bleed product mockup inside a dark band — a `transform: scale(1 → 1.04)`
over `{motion.duration-emphasis}` on scroll, tied to scroll position rather
than looping. **This is deliberate brand ambience and is stated as such.** It
is the only place scale is allowed above 1.0, and it is frozen entirely under
reduced motion.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel (translate), all scale, all stagger, and the
     full-bleed mockup ambience, which freezes at scale(1). */
  /* Kept: opacity fades only, clamped to {motion.duration-reduced} (150ms),
     and the focus ring, which always appears instantly at full opacity. */
  *,
  *::before,
  *::after {
    transition-duration: 150ms !important;   /* {motion.duration-reduced} */
    animation-duration: 150ms !important;    /* {motion.duration-reduced} */
    transition-property: opacity !important;
    animation-iteration-count: 1 !important;
    transform: none !important;
  }
}
```

`{motion.duration-reduced}` is 150ms, below this profile's own
`{motion.duration-fast}` of 240ms — the reduced ceiling is 150ms whatever the
profile.

## Accessibility

Every ratio below was computed with WCAG 2.1 relative luminance from the hexes
in this file's own frontmatter. Composited tokens (`{colors.on-dark-mute}`,
`{colors.hairline-dark}`, `{colors.divider-soft}`) carry alpha and are not
measurable on their own; their effective values depend on the band behind them.

### Measured contrast — passing

| Pair | Ratio | Required |
|---|---|---|
| `{colors.ink}` on `{colors.canvas-light}` | 17.11:1 | 4.5:1 |
| `{colors.ink}` on `{colors.surface-soft}` | 15.56:1 | 4.5:1 |
| `{colors.body}` on `{colors.canvas-light}` | 15.97:1 | 4.5:1 |
| `{colors.mute}` on `{colors.canvas-light}` | 7.04:1 | 4.5:1 |
| `{colors.ash}` on `{colors.canvas-light}` | 6.51:1 | 4.5:1 |
| `{colors.on-dark}` on `{colors.canvas-dark}` | 21.00:1 | 4.5:1 |
| `{colors.on-dark}` on `{colors.surface-elevated}` | 17.80:1 | 4.5:1 |
| `{colors.on-primary}` on `{colors.primary}` | 6.06:1 | 4.5:1 |
| `{colors.hairline-strong}` on `{colors.canvas-light}` | 17.11:1 | 3.0:1 |
| `{colors.focus}` on `{colors.canvas-light}` | 6.06:1 | 3.0:1 |
| `{colors.focus-on-dark}` on `{colors.canvas-dark}` | 21.00:1 | 3.0:1 |

### Measured contrast — real failures, stated plainly

These are extracted brand values. They are **not** adjusted here; a falsified
hex would make this document describe a product that does not exist.

| Pair | Ratio | Required | Note |
|---|---|---|---|
| `{colors.hairline-light}` on `{colors.canvas-light}` | 1.29:1 | 3.0:1 | The real divider inside white bands, and the real 1px boundary of `{component.text-input}` and `{component.feature-card-light}`. **The brand fails WCAG 2.1 non-text contrast here.** `{colors.hairline-strong}` (17.11:1) already exists in the palette and is the boundary to draw where a boundary carries meaning; `{colors.hairline-light}` is defensible only as decoration between rows that are already separated by whitespace. |
| `{colors.hairline-light}` on `{colors.surface-soft}` | 1.17:1 | 3.0:1 | Same divider on the off-white band. Same conclusion, slightly worse. |
| `{colors.stone}` on `{colors.canvas-light}` | 3.00:1 | 4.5:1 | Metadata and subtle captions. Fails AA for body text; defensible only at 18.66px+ regular or 14px+ bold, where 3:1 applies. |
| `{colors.accent-teal}` on `{colors.canvas-light}` | 3.04:1 | 4.5:1 | Illustration fill only, per Do's and Don'ts. Fails as text on white; clears the 3:1 graphical threshold. |
| `{colors.accent-yellow}` on `{colors.canvas-light}` | 3.07:1 | 4.5:1 | Caution fill inside product mockups. Fails as text on white; clears 3:1 graphical. |
| `{colors.accent-warning}` on `{colors.canvas-light}` | 2.78:1 | 4.5:1 | Full-saturation orange. Fails **both** the 4.5:1 text threshold and the 3:1 graphical threshold on white. Use it on `{colors.canvas-dark}` (7.55:1) or pair it with `{colors.ink}` type. |
| `{colors.accent-danger}` on `{colors.canvas-light}` | 4.24:1 | 4.5:1 | Narrowly fails for error text on white. `{colors.accent-deep-red}` (10.01:1) is the inline-error ink and is what `{component.text-input}` error state uses. |
| `{colors.link}` / `{colors.accent-blue-link}` on `{colors.canvas-dark}` | 4.27:1 | 4.5:1 | Passes on white (4.92:1), fails on the black storytelling canvas. The file's own answer is `{colors.accent-light-blue}` (4.61:1 on black) plus `{typography.link-emph}` at weight 700. |
| `{colors.primary}` on `{colors.canvas-dark}` | 3.47:1 | 4.5:1 | Cobalt violet as *text* on black fails AA. It passes as a surface — `{component.plan-card-featured}` is a cobalt fill carrying white type at 6.06:1 — which is how the brand actually uses it. Never set cobalt type on black. |
| `{colors.faint}` on `{colors.canvas-light}` | 1.65:1 | — | Documented as disabled foreground. WCAG sets no contrast requirement on disabled controls, so this is recorded rather than failed. |

### Surface separation

The elevation ladder carries almost no luminance difference:
`{colors.canvas-light}` to `{colors.surface-soft}` is 1.10:1,
`{colors.canvas-dark}` to `{colors.surface-elevated}` is 1.18:1, and
`{colors.canvas-dark}` to `{colors.surface-deep}` is 1.06:1. These steps are
atmosphere, not boundaries. Where a card edge has to be perceivable — a
selectable plan, a form container — the boundary must come from
`{colors.hairline-strong}` on light or a `{colors.on-dark}` hairline on dark,
not from the surface step alone.

### Focus ring visibility, per surface

The ring is 2px with a 2px offset, drawn outside the control, so it is measured
against the surface behind the control.

| Surface | Ring | Ratio |
|---|---|---|
| `{colors.canvas-light}` | `{colors.focus}` | 6.06:1 |
| `{colors.surface-soft}` / `{colors.surface-card}` | `{colors.focus}` | 5.51:1 / 6.06:1 |
| `{colors.canvas-dark}` | `{colors.focus-on-dark}` | 21.00:1 |
| `{colors.surface-deep}` | `{colors.focus-on-dark}` | 19.80:1 |
| `{colors.surface-elevated}` | `{colors.focus-on-dark}` | 17.80:1 |
| `{colors.primary}` (featured plan card) | `{colors.focus-on-dark}` | 6.06:1 |
| Full-bleed product photography | `{colors.focus-on-dark}` with a 1px `{colors.canvas-dark}` outer edge | Not measurable — photography has no single colour, so the ring is two-tone by rule. |

`{colors.focus}` reuses the existing `{colors.primary}` hex and
`{colors.focus-on-dark}` reuses the existing `{colors.on-dark}` hex. Neither is
a new brand colour. A single ring cannot serve both polarities: `{colors.focus}`
measures 1.00:1 on `{colors.primary}` and 3.47:1 on `{colors.canvas-dark}`,
which is why the dark counterpart exists.

### Tap targets

From the heights documented in this file, not from a rendered page: every
button ships at 48px, `{component.text-input}` at 56px, `{component.nav-bar}`
at 64px. These clear the 44px of WCAG 2.5.5 AAA.
`{component.button-pill-sm}` and `{component.badge-tag}` are documented at 36px
and at `4px 12px` padding respectively — the pill is noted as padded to 44px on
mobile; the badge is a label, not a target. Rendered target size cannot be
verified from a document, so this is a reading of the documented values only.

### Reduced motion

Honoured as set out in Motion & Animation: all travel, scale, stagger and brand
ambience are removed, opacity fades are clamped to `{motion.duration-reduced}`
(150ms), and the focus ring is never suppressed.

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
| `{colors.link}` (`#376cd5`) on `{colors.surface-soft}` (`#f4f4f4`) | 4.47:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Switch full bands between `{colors.canvas-dark}` (storytelling) and `{colors.canvas-light}` (catalogue). The two-mode rhythm is core.
- Use `{component.button-primary}` (white pill on dark) as the primary CTA on every dark hero band. It's the brand's loudest action.
- Reserve `{colors.primary}` for the featured plan card and the brand wordmark — the cobalt should feel like a deliberate stamp, not a colour theme.
- Set hero headlines in **Aeonik Pro 500** at 80–136px with `lineHeight: 1.0` and large negative letter-spacing.
- Use **Inter** for body, button labels, captions — never substitute Aeonik Pro for body type.
- Apply `{rounded.full}` to every button and pill; `{rounded.lg}` (20px) to feature and plan cards; `{rounded.md}` (12px) to inputs.
- Show product mockups full-bleed inside dark sections — the asset IS the section.
- Use the wide accent palette (`{colors.accent-teal}`, `{colors.accent-pink}`, `{colors.accent-light-green}`, etc.) inside product illustrations and iconography only.

### Don't
- Don't use accent colours (`{colors.accent-teal}`, `{colors.accent-pink}`, etc.) as button surfaces. They live inside illustrations only.
- Don't use a near-black canvas. The brand is `#000000`, not `#0a0a0a`.
- Don't pair white text with cobalt violet inside body content — `{colors.primary}` is for the featured plan card surface, not large prose.
- Don't add drop shadows on cards. Elevation is canvas + surface-luminance shifts.
- Don't introduce a secondary brand colour. Cobalt violet is the only brand stamp.
- Don't loosen Aeonik Pro `lineHeight` past 1.0 on display sizes. Tight stacking is structural.
- Don't bump body Inter to weight 500. Use 400 (default) or 600 (emphatic) — never the in-between.
- Don't pair `{colors.canvas-dark}` with another dark surface beyond `{colors.surface-elevated}`. The surface ladder has only two dark steps.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop XL | ≥ 1440px | 4-up plan grid, full-bleed product mockup bands, max content 1200. |
| Desktop | 1280–1439px | Container shrinks; xl side padding. |
| Tablet Large | 1024–1279px | Plan grid 4-up; feature grid 3-up. |
| Tablet | 768–1023px | Plan grid 2-up; feature grid 2-up. |
| Mobile Large | 426–767px | Plan grid 1-up; feature grid 1-up; nav collapses to hamburger; hero `display-xxl` clamps to 64px. |
| Mobile | ≤ 425px | All grids 1-up; hero clamps to 48px; section padding `{spacing.section}` collapses to 64px. |

### Touch Targets
- All buttons ship at minimum 48px tall — comfortably exceeds WCAG AAA (44px). Default `{component.button-primary}` is 48px.
- `{component.text-input}` is 56px tall — fintech-grade accessibility.
- `{component.button-pill-sm}` (36px) is bumped to 44px on mobile via padding adjustment.

### Collapsing Strategy
- Top-level nav collapses to hamburger at < 1024px; the wordmark and `{component.button-primary}` stay anchored.
- Hero `{typography.display-xxl}` clamps: 136px → 80px → 64px → 48px across the breakpoint ladder.
- Plan grid steps from 4-up to 2-up at < 1024px to 1-up at < 768px.
- Product mockup bands maintain full-bleed at every breakpoint; the asset crops inward rather than letterboxing.
- Sub-nav pills convert from a wrap row to a horizontal scroll-rail at < 768px.

### Image Behavior
- Phone and card mockups are served at 1.5× and 2× DPR; below 768px the system swaps to a smaller hero crop.
- Product photography retains its own atmospheric lighting at every breakpoint — no responsive variant assets.

## Iteration Guide

1. Focus on ONE component at a time. Most surfaces share the `{colors.canvas-dark}` / `{colors.canvas-light}` pair with `{rounded.full}` for buttons and `{rounded.lg}` for cards.
2. Reference component names and tokens directly (`{colors.primary}`, `{component.plan-card-featured}`, `{rounded.lg}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits; orphaned-tokens warnings will catch unused entries.
4. Add new variants as separate entries (`-pressed`, `-featured`, `-disabled`) — do not bury them in prose.
5. Default body type to `{typography.body-md}` (Inter 400 with positive tracking); reach for `{typography.body-md-bold}` only on emphasis.
6. Keep `{colors.primary}` scarce — if more than one cobalt-violet element appears per viewport, ask whether one should drop to `{component.plan-card}` (`{colors.surface-elevated}`) instead.

## Known Gaps

- Pressed/active visual states are documented for `button-primary-pressed` only. Every other state named in Components is **prescribed**, not extracted: the live pages were not instrumented for hover, focus-visible, disabled, loading, selected or error, and nothing here should be read as an observed fact about the real site.
- The whole Motion & Animation section is prescribed, including the Cinematic durations and easings and the scroll-tied mockup ambience. Revolut's real timing functions were never measured.
- `{colors.focus}` and `{colors.focus-on-dark}` are prescribed role bindings onto hexes the palette already owns (`{colors.primary}` and `{colors.on-dark}`). Revolut's real focus treatment was not extracted; the brand may well use something else.
- The extracted `{colors.hairline-light}` is bound to `{component.text-input}` and `{component.feature-card-light}` in the prose at 1.29:1. Those bindings are left exactly as extracted. Whether to re-point them to `{colors.hairline-strong}` is a brand-owner decision and is not taken here.
- Tap-target and overflow behaviour cannot be verified from a document; the Accessibility section reads documented heights only, with no rendered page behind it.
- Logged-in app surfaces (transactions, transfers, account settings) are out of scope — only the public marketing canvas is documented.
- The wide accent palette (`{colors.accent-teal}` through `{colors.accent-brown}`) is captured from the extracted token set, but exact usage inside product illustrations varies per market and product line; document per-illustration rather than as system buttons.
- Mobile-app screenshot art direction (phone bezels, status bars) is product-photography territory and not standardised as design tokens.
