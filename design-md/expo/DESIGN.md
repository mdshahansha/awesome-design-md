---
version: alpha
name: Expo-design-analysis
description: A React Native developer-platform whose marketing site reads like a quietly-confident infrastructure brand. The base canvas is pure white with a soft sky-blue gradient atmospheric wash behind the hero; near-black ink (`#171717`) carries body and display alike. The single brand voltage is **pure black** (`#000000`) for primary CTAs — minimal and editorial-feeling, paired with a small blue text-link accent (`#0d74ce`) reserved for inline body links. Type pairs Inter at modest weights (display 600, body 400) with JetBrains Mono on every code surface. The brand's strongest visual signature is the **device-mockup hero** — a centered MacBook + iPhone composite showing real Expo dev surfaces — over the gradient sky wash.

colors:
  primary: "#000000"
  primary-active: "#1a1a1a"
  text-link: "#0d74ce"
  text-link-secondary: "#476cff"
  ink: "#171717"
  body: "#60646c"
  body-strong: "#171717"
  muted: "#999999"
  muted-soft: "#cccccc"
  muted-strong: "#6b6f76"
  hairline: "#f0f0f3"
  hairline-soft: "#f5f5f7"
  hairline-strong: "#dcdee0"
  border-control: "#86888f"
  canvas: "#ffffff"
  canvas-soft: "#fafafa"
  surface-card: "#ffffff"
  surface-strong: "#f0f0f3"
  surface-dark: "#171717"
  surface-dark-elevated: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-soft: "#b0b4ba"
  gradient-sky-light: "#cfe7ff"
  gradient-sky-mid: "#a8c8e8"
  accent-warning: "#ab6400"
  accent-preview: "#8145b5"
  accent-link-bright: "#47c2ff"
  semantic-error: "#eb8e90"
  semantic-error-text: "#b3261e"
  semantic-success: "#16a34a"
  focus: "#0d74ce"
  focus-on-dark: "#47c2ff"

typography:
  display-mega:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -1.92px
  display-xl:
    fontFamily: "'Inter', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -1.44px
  display-lg:
    fontFamily: "'Inter', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1.08px
  display-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.84px
  display-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.88px
    textTransform: uppercase
  code:
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  base: 16px
  md: 20px
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
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 10px 18px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 9px 17px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.text-link}"
    typography: "{typography.button}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-mega}"
    padding: 96px
  device-mockup-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 0
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  feature-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  workflow-step-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 20px
  workflow-step-icon:
    backgroundColor: "{colors.surface-strong}"
    rounded: "{rounded.md}"
    size: 32px
  code-block:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: 20px
  ide-mockup-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: 0
  pricing-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-featured:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 44px
  badge-pill:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  ecosystem-tile:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    size: 64px
  cta-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 96px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  footer-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 64px 48px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
---

## Overview

Expo's marketing site reads like a quietly-confident React-Native developer platform. The base canvas is **pure white** (`{colors.canvas}` — #ffffff) with a soft **sky-blue gradient atmospheric wash** behind the hero band. Near-black ink `{colors.ink}` (#171717) carries body and display alike. The single brand voltage is **pure black** (`{colors.primary}` — #000000) for primary CTAs — minimal and editorial-feeling. A small blue text-link accent (`{colors.text-link}` — #0d74ce) is reserved for inline body links, never as a CTA.

Type runs **Inter** as the single sans family at modest weights (display 600, body 400). JetBrains Mono carries every code surface. No custom typeface — the brand trusts Inter's editorial neutrality.

The brand's strongest visual signature is the **device-mockup hero** — a centered MacBook + iPhone composite showing real Expo dev surfaces (Expo Studio, EAS Build dashboard, the Expo Go simulator) — over a sky-blue gradient atmospheric wash. The composite is the page's chrome instead of an illustration.

**Key Characteristics:**
- Pure white canvas with sky-blue gradient atmospheric backdrop in hero only.
- Single primary CTA: pure black pill at `{rounded.md}` (8px) — compact developer-tool dialect.
- Text-link blue (`{colors.text-link}`) for inline links only — never on a CTA.
- Inter as the single sans family — no custom display typeface.
- JetBrains Mono on every code surface.
- Device-mockup hero with real Expo product surfaces is the brand chrome.
- Hairline + soft drop depth; no atmospheric brand decoration outside the hero.
- 96px section rhythm.

## Colors

### Brand & Accent
- **Black** (`{colors.primary}` — #000000): Primary CTA fill. Used scarcely.
- **Black Active** (`{colors.primary-active}` — #1a1a1a): Press state.
- **Text Link Blue** (`{colors.text-link}` — #0d74ce): Inline body links inside long-form copy. Scoped narrowly — never on CTAs.
- **Legal Link Blue** (`{colors.text-link-secondary}` — #476cff): Inline links inside legal copy footer.
- **Bright Cyan** (`{colors.accent-link-bright}` — #47c2ff): Used very sparingly inside docs widget links.

### Surface
- **Canvas** (`{colors.canvas}` — #ffffff): Pure white page floor.
- **Canvas Soft** (`{colors.canvas-soft}` — #fafafa): Subtle alternating band.
- **Surface Card** (`{colors.surface-card}` — #ffffff): Pure white card.
- **Surface Strong** (`{colors.surface-strong}` — #f0f0f3): Badges, ecosystem tiles, secondary buttons.
- **Surface Dark** (`{colors.surface-dark}` — #171717): Dark feature cards, code blocks, IDE mockups, featured pricing.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — #1a1a1a): One step lighter inside dark cards.

### Atmospheric Backdrop
- **Sky Light** (`{colors.gradient-sky-light}` — #cfe7ff) + **Sky Mid** (`{colors.gradient-sky-mid}` — #a8c8e8): The soft sky-blue gradient wash behind the homepage hero only. Not a brand action color.

### Hairlines
All three extracted hairlines are **decorative only** — none reaches the 3:1 a
component boundary needs against the white canvas (measured in Accessibility
below). Where a boundary carries meaning — a form control, a focusable card edge
— use `{colors.border-control}`, which is **prescribed, not extracted**.

- **Hairline** (`{colors.hairline}` — #f0f0f3): Decorative 1px divider between content rows.
- **Hairline Soft** (`{colors.hairline-soft}` — #f5f5f7): Decorative lighter divider.
- **Hairline Strong** (`{colors.hairline-strong}` — #dcdee0): Decorative panel outline.
- **Border Control** (`{colors.border-control}` — #86888f, *prescribed*): The accessible boundary for text inputs, selects and any outline that is the only thing defining a control. 3.54:1 on `{colors.canvas}`.

### Text
- **Ink** (`{colors.ink}` — #171717): Display, body emphasis.
- **Body** (`{colors.body}` — #60646c): Default running-text — slightly cool gray.
- **Body Strong** (`{colors.body-strong}` — #171717): Same as ink.
- **Muted** (`{colors.muted}` — #999999): Sub-titles. Extracted; fails AA for body-size text (2.85:1 on white) — decorative or 24px+ only.
- **Muted Soft** (`{colors.muted-soft}` — #cccccc): Disabled text only. WCAG sets no contrast requirement on disabled controls; never use it for live text.
- **Muted Strong** (`{colors.muted-strong}` — #6b6f76, *prescribed*): The accessible secondary-text tone. Use wherever `{colors.muted}` would carry readable copy at under 24px. 5.05:1 on `{colors.canvas}`.
- **On Primary** (`{colors.on-primary}` — #ffffff): White text on black CTA.
- **On Dark** (`{colors.on-dark}` — #ffffff): White text on dark cards.
- **On Dark Soft** (`{colors.on-dark-soft}` — #b0b4ba): Muted off-white on dark.

### Semantic
- **Warning** (`{colors.accent-warning}` — #ab6400): Warning text inside docs callouts.
- **Preview** (`{colors.accent-preview}` — #8145b5): "Preview" tag color.
- **Success** (`{colors.semantic-success}` — #16a34a): Confirmation. 3.30:1 on white — icon and 24px+ text only, not body copy.
- **Error** (`{colors.semantic-error}` — #eb8e90): Extracted error tone. 2.39:1 on white — it fails AA at any text size; treat it as a tint for borders and backgrounds.
- **Error Text** (`{colors.semantic-error-text}` — #b3261e, *prescribed*): The accessible error-message ink. 6.54:1 on `{colors.canvas}`.

### Focus
- **Focus** (`{colors.focus}` — #0d74ce, *prescribed*): The focus ring on every light surface. It reuses the brand's own text-link blue rather than introducing a colour Expo does not own. 4.77:1 on `{colors.canvas}`.
- **Focus On Dark** (`{colors.focus-on-dark}` — #47c2ff, *prescribed*): The ring on `{colors.surface-dark}` code blocks, dark feature cards and the featured pricing tier. 8.90:1 on #171717. One ring cannot serve both polarities here — brand blue sits at only 3.76:1 on #171717, and bright cyan collapses to 2.01:1 on white.

## Typography

### Font Family
**Inter** is the single sans family across every text role. **JetBrains Mono** carries every code surface. Fallback: `-apple-system, system-ui, sans-serif`.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-mega}` | 64px | 600 | 1.05 | -1.92px | Homepage hero h1 |
| `{typography.display-xl}` | 48px | 600 | 1.1 | -1.44px | Subsidiary heroes |
| `{typography.display-lg}` | 36px | 600 | 1.15 | -1.08px | Section heads |
| `{typography.display-md}` | 28px | 600 | 1.2 | -0.84px | Sub-section heads |
| `{typography.display-sm}` | 22px | 600 | 1.25 | -0.5px | Card group titles |
| `{typography.title-md}` | 18px | 600 | 1.4 | 0 | Component titles |
| `{typography.title-sm}` | 16px | 600 | 1.4 | 0 | List labels |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default body |
| `{typography.body-sm}` | 14px | 400 | 1.5 | 0 | Footer body |
| `{typography.caption}` | 13px | 400 | 1.4 | 0 | Photo captions |
| `{typography.caption-uppercase}` | 11px | 600 | 1.4 | 0.88px | Section labels, badges |
| `{typography.code}` | 13px | 400 | 1.5 | 0 | Code blocks — JetBrains Mono |
| `{typography.button}` | 14px | 500 | 1.0 | 0 | CTA labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Top-nav menu |

### Principles
- **Display weight stays at 600** — confident but not bombastic. Inter at 600 reads cleaner than 700.
- **Negative letter-spacing on display** — -0.5px to -1.92px tracking.
- **JetBrains Mono on every code surface.**

### Note on Font Substitutes
Inter and JetBrains Mono are both freely available — the system uses them directly.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.base}` 16px · `{spacing.md}` 20px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- **Section padding:** 96px.

### Grid & Container
- Max content width: ~1200px.
- Editorial body: 12-column grid.
- Feature card grids: 2-up at desktop for hero splits, 3-up for benefit grids.
- Ecosystem tile grid: 8-up at desktop.
- Footer: 5-column at desktop.

### Whitespace Philosophy
Generous editorial pacing. The white canvas does not compete with the hero's gradient sky wash; cards inside dense workflow sections sit close (16-24px gap).

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `{colors.canvas}` (#ffffff) | Body bands, footer |
| Card | `{colors.surface-card}` (#ffffff) | Content cards |
| Hairline border | 1px `{colors.hairline}` | Card outlines |
| Soft drop | `0 4px 12px rgba(0, 0, 0, 0.04)` | Hovered cards (single shadow tier) |
| Atmospheric gradient | Sky-blue radial wash | Hero backdrop only |
| Dark inversion | `{colors.surface-dark}` (#171717) | Dark feature cards, code blocks, featured pricing |

### Decorative Depth
- **Sky-blue gradient backdrop** in the hero only — atmospheric depth without claiming to be a brand color.
- **Device mockup composite** as page chrome — MacBook + iPhone showing real Expo dev surfaces.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Reserved |
| `{rounded.xs}` | 4px | Inline tags |
| `{rounded.sm}` | 6px | Compact rows |
| `{rounded.md}` | 8px | CTA buttons, form inputs, ecosystem tiles |
| `{rounded.lg}` | 12px | Feature cards, code blocks, pricing tiers |
| `{rounded.xl}` | 16px | Device mockup cards |
| `{rounded.xxl}` | 24px | Larger atmospheric cards (rare) |
| `{rounded.pill}` | 9999px | Badges only |
| `{rounded.full}` | 9999px | Avatar plates (rare) |

Compact developer-ergonomic radii — 8px CTAs, 12px cards. Pill geometry is reserved for badges, never CTAs.

## Components

### Top Navigation

**`top-nav`** — Background `{colors.canvas}`, text `{colors.ink}`, height 64px. Layout: Expo wordmark left, primary horizontal menu (Tools / Workflows / EAS / Pricing / Docs / Showcase), Sign In + Get started CTA right.

### Buttons

**`button-primary`** — Pure black pill. Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}` (14px / 500), padding 10px × 18px, height 40px, rounded `{rounded.md}` (8px).

**`button-primary-active`** — Press state. Background `{colors.primary-active}`.

**`button-secondary`** — White card with 1px hairline-strong border. Background `{colors.surface-card}`, text `{colors.ink}`, 1px `{colors.hairline-strong}` border.

**`button-tertiary-text`** — Inline blue text link. Background transparent, text `{colors.text-link}`.

### Hero & Device Mockup

**`hero-band`** — Background `{colors.canvas}` with a soft sky-blue gradient wash behind the centered headline. Display headline in `{typography.display-mega}` (64px / 600 / -1.92px), subhead in `{typography.body-md}`, single primary CTA, then below — the device mockup composite.

**`device-mockup-card`** — A layered MacBook + iPhone composite showing real Expo dev surfaces. Background `{colors.surface-card}`, rounded `{rounded.xl}`. The MacBook holds the EAS dashboard or Expo Studio screenshot; the iPhone overlay shows the running app in Expo Go. This is the page chrome.

### Cards

**`feature-card`** — Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.title-md}`, rounded `{rounded.lg}`, padding 24px, 1px `{colors.hairline-strong}` border.

**`feature-card-dark`** — Dark variant. Background `{colors.surface-dark}`, text `{colors.on-dark}`. Same shape, dark inversion.

**`workflow-step-card`** — Step in the "Get your app on every device" workflow row. Background `{colors.surface-card}`, text `{colors.body}`, rounded `{rounded.lg}`, padding 20px. Layout: 32px square `{component.workflow-step-icon}` + step number + label + body.

**`workflow-step-icon`** — Square plate. Background `{colors.surface-strong}`, rounded `{rounded.md}`, 32px size.

**`testimonial-card`** — Quote card. Background `{colors.surface-card}`, text `{colors.body}`, rounded `{rounded.lg}`, padding 24px.

### Code & IDE

**`code-block`** — Inline code block. Background `{colors.surface-dark}`, text `{colors.on-dark}` in `{typography.code}` (JetBrains Mono 13px), rounded `{rounded.lg}`, padding 20px. White text on dark.

**`ide-mockup-card`** — Stylized IDE mockup. Background `{colors.surface-dark}`, rounded `{rounded.lg}`. Multi-pane editor + terminal preview.

### Pricing

**`pricing-tier-card`** — Standard pricing tier. Background `{colors.surface-card}`, rounded `{rounded.lg}`, padding 32px, 1px `{colors.hairline-strong}` border.

**`pricing-tier-featured`** — Featured tier. Background `{colors.surface-dark}`, text `{colors.on-dark}`. Same shape, dark inversion.

### Ecosystem

**`ecosystem-tile`** — Square logo plate for ecosystem partner logos (TypeScript, React, Sentry, etc.). Background `{colors.surface-card}`, rounded `{rounded.md}`, 64px size, 1px `{colors.hairline}` border.

### Forms & Tags

**`text-input`** — Background `{colors.surface-card}`, text `{colors.ink}`, rounded `{rounded.md}` (8px), padding 12px × 16px, height 44px, 1px `{colors.border-control}` border (the extracted `{colors.hairline-strong}` outline measures 1.35:1 and cannot be the only thing defining a control). Focus-visible adds a 2px `{colors.focus}` ring with a 2px `{colors.canvas}` offset; error state swaps the border to `{colors.semantic-error-text}` with the message in the same ink.

**`badge-pill`** — Small uppercase pill. Background `{colors.surface-strong}`, text `{colors.ink}`, type `{typography.caption-uppercase}`, rounded `{rounded.pill}`, padding 4px × 10px.

### CTA / Footer

**`cta-band`** — Pre-footer band. Background `{colors.canvas}`, centered display headline in `{typography.display-lg}`, single black pill CTA. 96px padding.

**`footer-light`** — Closing white footer. Background `{colors.canvas}`, text `{colors.body}`. 5-column link list. 64×48px padding.

**`footer-link`** — Background transparent, text `{colors.body}`, type `{typography.body-sm}`.

### Interaction States

Only `button-primary-active` was captured on the live site; every other state
below is **prescribed** to match the brand's own dialect (opacity and tone
shifts, no colour invention). A component that genuinely has two states says so.

| Component | States | Notes |
|---|---|---|
| `top-nav` | default, hover, focus-visible, selected | Hover darkens link to `{colors.ink}`; selected marks the current section; the bar itself does not press. |
| `button-primary` | default, hover, active (pressed), focus-visible, disabled, loading | Hover → `{colors.primary-active}`; pressed → same fill at 0.98 scale; disabled → `{colors.muted-soft}` fill with `{colors.canvas}` label; loading → label holds width, inline spinner. |
| `button-primary-active` | pressed only | The captured press state of `button-primary`, not a component of its own. |
| `button-secondary` | default, hover, active (pressed), focus-visible, disabled, loading | Hover fills `{colors.surface-strong}`; border stays `{colors.border-control}`. |
| `button-tertiary-text` | default, hover, active (pressed), focus-visible, disabled | Hover underlines; colour stays `{colors.text-link}`. |
| `hero-band` | default only | Static band — two states would be an invention. |
| `device-mockup-card` | default only | Page chrome, not interactive. |
| `feature-card` | default, hover, focus-visible, selected | Hover raises the soft drop shadow; selected outlines in `{colors.focus}`. |
| `feature-card-dark` | default, hover, focus-visible, selected | Same, with `{colors.focus-on-dark}` for the ring and outline. |
| `workflow-step-card` | default, hover, selected | Selected marks the active step in the workflow row. |
| `workflow-step-icon` | default, selected | Plate fills `{colors.ink}` when its step is selected; no hover of its own. |
| `code-block` | default, hover, focus-visible, loading | Hover reveals the copy button; focus-visible rings it in `{colors.focus-on-dark}`; loading covers streamed output. |
| `ide-mockup-card` | default only | Static mockup. |
| `pricing-tier-card` | default, hover, focus-visible, selected | Selected is the tier the user is on. |
| `pricing-tier-featured` | default, hover, focus-visible, selected | Dark inversion of the above. |
| `text-input` | default, hover, focus-visible, disabled, error, loading | Error → `{colors.semantic-error-text}` border and message; disabled → `{colors.muted-soft}` text on `{colors.surface-strong}`; loading → inline validation spinner. |
| `badge-pill` | default only | A label, never interactive. |
| `ecosystem-tile` | default, hover, focus-visible | Hover lifts the tile; most tiles are links. |
| `cta-band` | default only | Static band; the CTA inside it carries the states. |
| `testimonial-card` | default only | Static quote. |
| `footer-light` | default only | Static region. |
| `footer-link` | default, hover, focus-visible | Hover darkens to `{colors.ink}`. |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** Nobody timed Expo's real transitions; what
follows is the **Crisp** profile from `theme-audit/SPEC.md`, chosen because this
is a developer-tool identity — a monochrome CTA, JetBrains Mono on every code
surface, and a hero that shows product dashboards rather than choreography. The
one place the brand would earn travel is the device-mockup composite, and even
there a tool brand should let the screenshots arrive, not perform.

Rules this section obeys: **`transform` and `opacity` only** — never `width`,
`height`, `top`, `left` or `margin`. Every exit is shorter than its entrance.
Nothing animates on first paint in a way that delays content. The only infinite
animation is the loading spinner.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, tile) | `{motion.duration-fast}` (100ms) | `{motion.ease-standard}` | `opacity`, `transform: translateY(-1px)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| Press | `{motion.duration-instant}` (60ms) | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed; state change is instant |
| Focus ring appears | `{motion.duration-instant}` (60ms) | `{motion.ease-standard}` | `opacity` | Unchanged — already opacity-only and under 150ms |
| Page / route transition | `{motion.duration-base}` (150ms) | `{motion.ease-enter}` in, `{motion.ease-exit}` out at `{motion.duration-fast}` | `opacity` | Cross-fade at `{motion.duration-reduced}`; no travel |
| Modal / drawer open | `{motion.duration-base}` (150ms) | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px) → 0` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Modal / drawer close | `{motion.duration-fast}` (100ms) | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Dropdown / nav menu | `{motion.duration-fast}` (100ms) in, `{motion.duration-instant}` (60ms) out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: scaleY(0.98) → 1` | Scale removed; opacity only at `{motion.duration-reduced}` |
| Toast | `{motion.duration-base}` (150ms) in, `{motion.duration-fast}` (100ms) out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| List enter (feature grid, ecosystem tiles) | `{motion.duration-base}` (150ms), `{motion.stagger-step}` (20ms) per item | `{motion.ease-enter}` | `opacity`, `transform: translateY(6px)` | Stagger and travel removed; all items fade together at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` (100ms), no stagger | `{motion.ease-exit}` | `opacity`, `transform: translateY(4px)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| Loading (spinner, EAS build status) | 800ms linear loop | linear | `transform: rotate` | Rotation frozen; replaced by a static indicator with a text label |
| Hero device-mockup entrance | `{motion.duration-emphasis}` (300ms) | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px)` | Travel removed; opacity only at `{motion.duration-reduced}`. Runs after first paint; the headline never waits on it |

### `@media (prefers-reduced-motion: reduce)`

**Removed:** every `translate`, every `scale`, the `{motion.stagger-step}` on
list entrances, and the device-mockup entrance travel. The spinner's rotation is
frozen and replaced with a static indicator plus its text label.

**Kept:** opacity fades, capped at `{motion.duration-reduced}` (100ms) —
never more than 150ms, whatever the profile. Focus rings, hover tone changes and
every colour transition remain, because none of them moves anything.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 100ms !important;   /* {motion.duration-reduced} */
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;  /* {motion.duration-reduced} */
    transition-property: opacity, color, background-color, border-color !important;
  }
}
```

## Accessibility

Ratios below are WCAG 2.1 relative luminance, computed from this file's own
hexes. Extracted brand values are **not** altered to pass; where the real brand
fails, it is named here.

### Measured contrast — passing

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` #171717 on `{colors.canvas}` #ffffff | 17.93:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.surface-card}` #ffffff | 17.93:1 | 4.5 | Pass |
| `{colors.body}` #60646c on `{colors.canvas}` | 5.94:1 | 4.5 | Pass |
| `{colors.on-primary}` #ffffff on `{colors.primary}` #000000 | 21.00:1 | 4.5 | Pass |
| `{colors.on-dark}` #ffffff on `{colors.surface-dark}` #171717 | 17.93:1 | 4.5 | Pass |
| `{colors.on-dark-soft}` #b0b4ba on `{colors.surface-dark}` | 8.61:1 | 4.5 | Pass |
| `{colors.text-link}` #0d74ce on `{colors.canvas}` | 4.77:1 | 4.5 | Pass |
| `{colors.muted-strong}` #6b6f76 on `{colors.canvas}` | 5.05:1 | 4.5 | Pass (prescribed) |
| `{colors.border-control}` #86888f on `{colors.canvas}` | 3.54:1 | 3.0 | Pass (prescribed) |
| `{colors.semantic-error-text}` #b3261e on `{colors.canvas}` | 6.54:1 | 4.5 | Pass (prescribed) |
| `{colors.accent-warning}` #ab6400 on `{colors.canvas}` | 4.61:1 | 4.5 | Pass |
| `{colors.accent-preview}` #8145b5 on `{colors.canvas}` | 6.08:1 | 4.5 | Pass |

### Measured contrast — real brand failures, disclosed

These are extracted values. They are frozen, not corrected.

| Pair | Ratio | Required | Honest reading |
|---|---|---|---|
| `{colors.hairline-soft}` #f5f5f7 on `{colors.canvas}` #ffffff | 1.09:1 | 3.0 | Fails. Decorative divider only — never the sole boundary of a control. |
| `{colors.hairline}` #f0f0f3 on `{colors.canvas}` | 1.14:1 | 3.0 | Fails. Decorative only. Use `{colors.border-control}` where a boundary must be seen. |
| `{colors.hairline-strong}` #dcdee0 on `{colors.canvas}` | 1.35:1 | 3.0 | Fails. Expo's strongest real hairline still does not reach 3:1; the card and input outlines drawn with it are invisible to low-vision users. |
| `{colors.muted}` #999999 on `{colors.canvas}` | 2.85:1 | 4.5 | Fails for body text. Defensible only at 24px+ (or 18.66px bold), where 3:1 applies — and it clears that. Below that size use `{colors.muted-strong}`. |
| `{colors.muted}` #999999 on `{colors.surface-card}` #ffffff | 2.85:1 | 4.5 | Same failure; the card surface is also pure white, so there is no safer surface for it. |
| `{colors.muted-soft}` #cccccc on `{colors.canvas}` | 1.61:1 | 4.5 | Fails. Disabled text only — WCAG sets no requirement on disabled controls. Never live copy. |
| `{colors.muted-soft}` #cccccc on `{colors.surface-card}` | 1.61:1 | 4.5 | Same, same reason. |
| `{colors.semantic-error}` #eb8e90 on `{colors.canvas}` | 2.39:1 | 4.5 | Fails at every text size. Use it as a border or background tint; error copy is `{colors.semantic-error-text}`. |
| `{colors.semantic-success}` #16a34a on `{colors.canvas}` | 3.30:1 | 4.5 | Fails for body text; clears 3:1, so icon and 24px+ text only. |
| `{colors.text-link-secondary}` #476cff on `{colors.canvas}` | 4.32:1 | 4.5 | Marginal fail — the legal-footer link blue is 0.18 short of AA. |
| `{colors.accent-link-bright}` #47c2ff on `{colors.canvas}` | 2.01:1 | 4.5 | Fails on light. It is a dark-surface tone only: 8.90:1 on `{colors.surface-dark}`. |

Plainly: **the hairline ladder fails AA as a boundary across the board, and the
muted text ramp fails AA below 24px.** That is a property of the real brand, not
of this document.

### Focus ring visibility, per surface this file defines

`{colors.focus}` (#0d74ce) is a 2px ring with a 2px `{colors.canvas}` offset.
`{colors.focus-on-dark}` (#47c2ff) is the same geometry with a `{colors.surface-dark}` offset.

| Surface | Ring | Ratio | Verdict |
|---|---|---|---|
| `{colors.canvas}` #ffffff | `{colors.focus}` | 4.77:1 | Pass |
| `{colors.canvas-soft}` #fafafa | `{colors.focus}` | 4.57:1 | Pass |
| `{colors.surface-card}` #ffffff | `{colors.focus}` | 4.77:1 | Pass |
| `{colors.surface-strong}` #f0f0f3 | `{colors.focus}` | 4.19:1 | Pass |
| `{colors.surface-dark}` #171717 | `{colors.focus-on-dark}` | 8.90:1 | Pass |
| `{colors.surface-dark-elevated}` #1a1a1a | `{colors.focus-on-dark}` | 8.64:1 | Pass |
| `{colors.gradient-sky-light}` #cfe7ff | `{colors.focus}` | 3.75:1 | Pass |
| `{colors.gradient-sky-mid}` #a8c8e8 | `{colors.focus}` | 2.74:1 | **Fail** — the darkest end of the hero gradient. The mandatory 2px white offset supplies the boundary there, giving the ring a 3.75:1 outer edge against #a8c8e8; without the offset the ring is not visible on the hero wash. |

Over the device-mockup composite, which is photography and has no measurable
colour, use the two-tone ring: `{colors.focus}` with a 1px `{colors.canvas}`
outer edge.

Secondary note: `{colors.muted-strong}` measures 4.44:1 on `{colors.surface-strong}`
(#f0f0f3), just under AA. Small copy on badges and icon plates uses `{colors.ink}`.

### Minimum tap target

Not computable from a document — there is no rendered page here, so these are
declared sizes, not measured ones. `button-primary` and `button-secondary` are
40px tall, below the 44px WCAG 2.5.5 AAA target; `text-input` is 44px and clears
it. Nav links and footer links carry no declared height and are an unknown.

### Reduced motion

Honoured as specified in Motion & Animation: all travel and scale removed,
opacity fades capped at `{motion.duration-reduced}` (100ms), the loading
rotation frozen. There is no brand ambience animation to freeze.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (black) for primary CTAs.
- Use `{colors.text-link}` (blue) for inline body links only — never on CTAs or buttons.
- Set every CTA at `{rounded.md}` (8px) — developer dialect.
- Use Inter at weight 600 for display, 400 for body.
- Render every code surface in JetBrains Mono.
- Pair the hero with the device-mockup composite — it's the page chrome.

### Don't
- Don't introduce a saturated brand action color. Black is the only CTA fill.
- Don't use blue (`{colors.text-link}`) on a CTA. Inline links only.
- Don't drop display below weight 600 or above 700.
- Don't use full pills on CTAs — pills are for badges only.
- Don't replicate the sky-blue gradient backdrop outside the hero.
- Don't extract a CTA color from a third-party widget (cookie consent, OneTrust). The brand's CTA is what appears on actual page CTAs.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 640px | Hero h1 64→32px; device mockup → single iPhone screen; feature grid 1-up; nav hamburger. |
| Tablet | 640–1024px | Hero h1 48px; device mockup compresses; feature grid 2-up. |
| Desktop | 1024–1280px | Full hero h1 64px; full MacBook + iPhone composite; feature grid 3-up. |
| Wide | > 1280px | Content caps at 1200px. |

### Touch Targets
- Primary CTA at 40px height — at WCAG AA, padded for AAA.
- Search input 44px — at AAA.

### Collapsing Strategy
- Top nav switches to hamburger below 768px.
- Device mockup MacBook + iPhone collapses to a single iPhone preview on mobile.
- Feature grid: 3-up → 2-up → 1-up.
- Ecosystem tile grid: 8-up → 4-up → 3-up → 2-up.

## Iteration Guide

1. Focus on a single component at a time.
2. CTAs default to `{rounded.md}` (8px). Cards use `{rounded.lg}` (12px).
3. Variants live as separate entries.
4. Use `{token.refs}` everywhere — never inline hex.
5. States live in the Components states table; motion values come from `{motion.*}` — never a hardcoded ms.
6. Inter 600 for display, Inter 400 for body. JetBrains Mono on code.
7. Black stays the only CTA color; text-link blue stays inline-only.

## Known Gaps

- Inter and JetBrains Mono are freely available — no licensing concerns.
- No motion was measured from the live site. Every value in Motion & Animation is the prescribed **Crisp** profile, including the device-mockup entrance; real Expo timings remain unknown.
- Focus ring, `{colors.border-control}`, `{colors.muted-strong}` and `{colors.semantic-error-text}` are prescribed, not extracted. No focus treatment was captured on the live surfaces.
- Every component state except `button-primary-active` is prescribed.
- Tap-target sizes are declared, not measured; no page was rendered.
- In-app surfaces (EAS dashboard interactive, Expo Go simulator) only partially captured via marketing mockups.
- Form validation states beyond focus not visible on captured surfaces.
