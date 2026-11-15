---
version: alpha
name: Cal.com-design-analysis
description: A clean, calendar-software-first interface anchored on white canvas with black primary CTAs and custom Cal Sans display typography. The system reads as friendly modern SaaS — generous whitespace, soft-rounded cards (~12px), product UI fragments shown directly inside cards, and a dark navy footer that visually closes long-scroll pages. Brand voltage comes from the Cal Sans display headline (a custom geometric face) and from product UI artifacts shown in-card rather than from accent colors.

colors:
  primary: "#111111"
  primary-active: "#242424"
  primary-disabled: "#e5e7eb"
  ink: "#111111"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#898989"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  hairline-strong: "#868d97"
  canvas: "#ffffff"
  surface-soft: "#f8f9fa"
  surface-card: "#f5f5f5"
  surface-strong: "#e5e7eb"
  surface-dark: "#101010"
  surface-dark-elevated: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-soft: "#a1a1aa"
  brand-accent: "#3b82f6"
  brand-accent-strong: "#1d4ed8"
  focus: "#2563eb"
  focus-on-dark: "#60a5fa"
  success: "#10b981"
  success-text: "#047857"
  warning: "#f59e0b"
  warning-text: "#92400e"
  error: "#ef4444"
  error-text: "#b91c1c"
  badge-orange: "#fb923c"
  badge-pink: "#ec4899"
  badge-violet: "#8b5cf6"
  badge-emerald: "#34d399"

typography:
  display-xl:
    fontFamily: "Cal Sans, Inter, sans-serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -2px
  display-lg:
    fontFamily: "Cal Sans, Inter, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-md:
    fontFamily: "Cal Sans, Inter, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1px
  display-sm:
    fontFamily: "Cal Sans, Inter, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  title-lg:
    fontFamily: "Inter, sans-serif"
    fontSize: 22px
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
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  code:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
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
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
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
  section: 96px

shadow:
  none: none
  small: 0 1px 2px rgba(0, 0, 0, 0.05)
  medium: 0 4px 12px rgba(0, 0, 0, 0.08)
  focus-ring: 0 0 0 2px #ffffff, 0 0 0 4px #2563eb

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
    padding: 12px 20px
    height: 40px
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
    height: 40px
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 36px
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
  nav-pill-group:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.pill}"
    padding: 6px
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 96px
  hero-app-mockup-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  feature-icon-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: 24px
  product-mockup-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
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
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    height: 40px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 8px 14px
    rounded: "{rounded.md}"
  category-tab-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
  avatar-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 36px
  badge-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  rating-stars:
    backgroundColor: transparent
    textColor: "{colors.badge-orange}"
    typography: "{typography.caption}"
  cta-band-light:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.lg}"
    padding: 48px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark-soft}"
    typography: "{typography.body-sm}"
    padding: 64px
---

## Overview

Cal.com's marketing surface is a clean, friendly modern-SaaS interface — white canvas (`{colors.canvas}` — #ffffff) with black primary CTAs (`{colors.primary}` — #111111), custom **Cal Sans** display typography, and `{colors.surface-card}` (#f5f5f5) light-gray cards holding product UI fragments. The system reads as confidently engineered without trying to impress — every band has clear hierarchy, generous whitespace, and a single primary action.

Type voice splits cleanly into two roles: **Cal Sans** (the brand's custom geometric display face — used for h1, h2, h3, and hero headlines) and **Inter** (used for everything else — body, buttons, nav, captions). Cal Sans uses weight 600 with negative letter-spacing (-0.5px to -2px depending on size) — it feels modern, slightly condensed, distinctly Cal.com.

Component voltage comes from **product UI fragments shown directly inside cards** — calendar widgets, scheduling forms, automation diagrams, integration tiles. Cal.com doesn't paint marketing illustrations of the product; it shows the actual product chrome at small scale embedded in the marketing flow.

The footer flips to `{colors.surface-dark}` (#101010) — a deep near-black that visually closes every long-scroll page. The footer is the only dark surface in the system; everything above stays white-with-light-gray-cards.

**Key Characteristics:**
- White canvas with black primary CTA (`{colors.primary}` — #111111). Buttons are `{rounded.md}` (8px) with confident weight-600 labels. Standard friendly-SaaS button.
- Custom `Cal Sans` display typeface for headlines (substituted with Inter weight 600 here). Negative letter-spacing on display sizes — geometric, precise, slightly condensed.
- Light-gray card surfaces (`{colors.surface-card}` — #f5f5f5) for feature cards, testimonials, and pricing tiers (non-featured). The featured pricing tier flips to `{colors.surface-dark}` (the only dark card on light pages).
- Product UI fragments embedded directly in cards — Cal.com shows real schedule pickers, calendar widgets, integration grids inside its marketing cards. Brand voltage from real product chrome at small scale.
- Nav-pill-group (`{component.nav-pill-group}`) — a small pill-radius wrapper around grouped nav segments (e.g., the sub-nav switcher between product views). The pill wrapper is one of the system's signature interactive components.
- Avatars are circular (`{rounded.full}`), 36px diameter, used in testimonial rows and team-listing surfaces.
- Footer is dark navy (`{colors.surface-dark}` — #101010) with light text (`{colors.on-dark-soft}` — #a1a1aa). The dark footer closes every page even though the body above is white.
- Spacing rhythm is `{spacing.section}` (96px) between major bands — tight enough to feel modern-SaaS but generous enough to breathe.
- Border radius is hierarchical: `{rounded.md}` (8px) for buttons + inputs, `{rounded.lg}` (12px) for content cards, `{rounded.xl}` (16px) for the hero app-mockup container, `{rounded.pill}` for nav-pill-group + badges, `{rounded.full}` for avatars + icon buttons.

## Colors

### Brand & Accent
- **Primary** (`{colors.primary}` — #111111): The dominant action color. All primary CTAs, h1/h2 display type. Press state shifts to `{colors.primary-active}` (#242424).
- **Brand Accent** (`{colors.brand-accent}` — #3b82f6): Used sparely on inline links and on a small badge / "Customer story" highlight. Cal.com is a near-monochrome brand — the blue appears rarely. **This extracted blue fails WCAG AA as text:** it measures 3.68:1 on `{colors.canvas}` and 3.37:1 on `{colors.surface-card}`, against the 4.5:1 body-text threshold, and white on it measures the same 3.68:1. The real brand fails AA at this point; the hex is not adjusted here because it is an extracted fact.
- **Brand Accent Strong** (`{colors.brand-accent-strong}` — #1d4ed8) — **prescribed, not extracted.** The accessible parallel to the brand blue for any case where blue carries text weight: blue link text at body size (6.70:1 on `{colors.canvas}`), or white text on a blue fill (6.70:1). Scope `{colors.brand-accent}` itself to decoration — badge fills, illustration strokes, 24px+ display numerals — where the 3:1 large-text threshold applies.
- **Badge Pastels** — A small pastel set for category badges and avatar fills: `{colors.badge-orange}` (#fb923c), `{colors.badge-pink}` (#ec4899), `{colors.badge-violet}` (#8b5cf6), `{colors.badge-emerald}` (#34d399). These appear on tag pills and small accent moments inside product UI fragments — never on hero CTAs. With `{colors.ink}` on top they measure: orange 8.34:1, pink 5.35:1, emerald 9.82:1 — and violet 4.46:1, which misses 4.5:1 by a hair. Badge labels on `{colors.badge-violet}` sit at `{typography.caption}` (13px / 500), below the large-text exemption, so violet badges carry an icon or a 16px+ label rather than 13px text.

### Surface
- **Canvas** (`{colors.canvas}` — #ffffff): The default page floor.
- **Surface Soft** (`{colors.surface-soft}` — #f8f9fa): Nav-pill-group background, very-soft section dividers.
- **Surface Card** (`{colors.surface-card}` — #f5f5f5): Feature cards, testimonial cards, badge pills, default avatar fills.
- **Surface Strong** (`{colors.surface-strong}` — #e5e7eb): Hairline border alternative; disabled button background.
- **Surface Dark** (`{colors.surface-dark}` — #101010): The footer background — the only dark surface on every page. Also used for the featured pricing tier card.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — #1a1a1a): Used for nested cards inside the dark footer or featured pricing card.
- **Hairline** (`{colors.hairline}` — #e5e7eb): The 1px border tone on light surfaces. Used on input borders, table dividers, content card outlines (sometimes).
- **Hairline Soft** (`{colors.hairline-soft}` — #f3f4f6): A barely-visible divider used between sections that share the white canvas. 1.10:1 on `{colors.canvas}` — decorative only.
- **Hairline Strong** (`{colors.hairline-strong}` — #868d97) — **prescribed, not extracted.** Cal.com's real hairline is `{colors.hairline}` at 1.24:1 on `{colors.canvas}`, far below the 3:1 a visible component boundary needs; the real brand fails that threshold. Where the border is the *only* thing defining a control — `{component.text-input}`, `{component.button-secondary}`, `{component.button-icon-circular}` — use `{colors.hairline-strong}` (3.35:1 on `{colors.canvas}`, 3.07:1 on `{colors.surface-card}`). Keep `{colors.hairline}` for decorative rules: table dividers, card outlines, section separators.

### Text
- **Ink** (`{colors.ink}` — #111111): All headlines and primary text.
- **Body** (`{colors.body}` — #374151): Default running-text color.
- **Muted** (`{colors.muted}` — #6b7280): Secondary text — sub-headings, breadcrumbs, footer body. 4.83:1 on `{colors.canvas}` — passes AA. On `{colors.surface-card}` it measures 4.43:1, marginally under 4.5:1, so secondary text inside a gray feature card should step up to `{colors.body}` (9.45:1 there).
- **Muted Soft** (`{colors.muted-soft}` — #898989): Tertiary text — captions, fine-print, copyright lines. 3.50:1 on `{colors.canvas}`, 3.21:1 on `{colors.surface-card}` — **fails AA for body text.** The real brand fails here. It clears the 3:1 large-text threshold, so scope it to 18px+ / 14px-bold-and-above fine print only; anything smaller uses `{colors.muted}`.
- **On Primary / On Dark** (`{colors.on-primary}` / `{colors.on-dark}` — #ffffff): Text on primary buttons and dark footer.
- **On Dark Soft** (`{colors.on-dark-soft}` — #a1a1aa): Footer body text — slightly muted white for the link rows.

### Focus
- **Focus** (`{colors.focus}` — #2563eb) — **prescribed, not extracted.** No focus ring was captured from the live site; this one is chosen as the accessible sibling of Cal.com's own sparse blue rather than a new hue, so the ring reads as part of the brand rather than as a browser default. Measured: 5.17:1 on `{colors.canvas}`, 4.74:1 on `{colors.surface-card}`, 4.90:1 on `{colors.surface-soft}`, 4.17:1 on `{colors.surface-strong}`, 3.65:1 on `{colors.primary}` (the black CTA). Every surface clears the 3:1 ring threshold.
- **Focus On Dark** (`{colors.focus-on-dark}` — #60a5fa) — **prescribed.** `{colors.focus}` reaches only 3.68:1 on `{colors.surface-dark}`; this lighter blue measures 7.48:1 there and 6.85:1 on `{colors.surface-dark-elevated}`, so the ring stays obvious inside the dark footer and the featured pricing tier. It is **not** for light surfaces (2.54:1 on `{colors.canvas}`).
- The ring is drawn as `{shadow.focus-ring}` — a 2px canvas-coloured spacer then a 4px blue ring — so it stays visible against both the control fill and the surface behind it.

### Semantic
- **Success** (`{colors.success}` — #10b981): Confirmation states, success badges in product UI. 2.54:1 on `{colors.canvas}` — a fill tone, never text.
- **Warning** (`{colors.warning}` — #f59e0b): Warning callouts. 2.15:1 on `{colors.canvas}` — a fill tone, never text.
- **Error** (`{colors.error}` — #ef4444): Validation errors. 3.76:1 on `{colors.canvas}` — below the 4.5:1 body-text threshold, so it is a fill and icon tone, not an error-message tone.
- **Semantic text tones** (`{colors.success-text}` — #047857, 5.48:1 · `{colors.warning-text}` — #92400e, 7.09:1 · `{colors.error-text}` — #b91c1c, 6.47:1, all on `{colors.canvas}`) — **prescribed, not extracted.** The three extracted semantic hexes are saturated fills lifted from product-UI badges; none passes AA as running text. Use these parallel tones for validation copy and keep the originals for the badge fills and icons they were observed on.

## Typography

### Font Family
The system runs **Cal Sans** for display + brand wordmark and **Inter** for everything else. Cal Sans is Cal.com's custom geometric display typeface — slightly condensed, weight 600, negative letter-spacing. Inter handles body, buttons, navigation, captions, and tabular code blocks. The fallback stack walks `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` for both families.

The split is functional:
- Cal Sans (display, 600 weight, -0.5 to -2px tracking) — h1, h2, h3
- Inter (body + UI, 400-600 weight, 0 letter-spacing) — paragraphs, labels, buttons, nav

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 64px | 600 | 1.05 | -2px | Homepage h1 ("The better way to schedule your meetings") — Cal Sans |
| `{typography.display-lg}` | 48px | 600 | 1.1 | -1.5px | Section heads ("Your all-purpose scheduling app") — Cal Sans |
| `{typography.display-md}` | 36px | 600 | 1.15 | -1px | Sub-section heads, card titles — Cal Sans |
| `{typography.display-sm}` | 28px | 600 | 1.2 | -0.5px | CTA-band heads, pricing tier prices — Cal Sans |
| `{typography.title-lg}` | 22px | 600 | 1.3 | -0.3px | Pricing plan names — Inter |
| `{typography.title-md}` | 18px | 600 | 1.4 | 0 | Feature card titles, intro paragraphs |
| `{typography.title-sm}` | 16px | 600 | 1.4 | 0 | Small card titles, list labels |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default running-text |
| `{typography.body-sm}` | 14px | 400 | 1.5 | 0 | Footer body, fine-print |
| `{typography.caption}` | 13px | 500 | 1.4 | 0 | Badge labels, captions |
| `{typography.code}` | 14px | 400 | 1.5 | 0 | Code snippets, API examples — JetBrains Mono |
| `{typography.button}` | 14px | 600 | 1.0 | 0 | Standard button labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Top-nav menu items |

### Principles
Cal Sans is the brand voice — every display headline uses it. Inter handles the supporting type. The boundary is strict: never put body copy in Cal Sans, never put a display headline in Inter. Cal Sans without negative letter-spacing reads as off-brand — the -0.5 to -2px tracking is part of the voice.

Display weight stays at 600 across all sizes — never 700, never 500. The middle weight is what makes Cal Sans feel modern and confident without becoming bombastic.

### Note on Font Substitutes
If Cal Sans is unavailable, **Inter** at weight 600 with -0.04em letter-spacing is a usable approximation. The geometric character of Cal Sans differs from Inter's humanist forms, but the substitution preserves the weight + tracking signature. **Manrope** at weight 700 is another close alternative.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- **Section padding:** `{spacing.section}` (96px) — the universal vertical rhythm between editorial bands.
- **Card internal padding:** `{spacing.xl}` (32px) for feature cards and pricing tier cards; `{spacing.lg}` (24px) for testimonial and product-mockup cards.
- **Gutters:** `{spacing.lg}` (24px) between cards in 3-up grids; `{spacing.md}` (16px) inside footer columns.

### Grid & Container
- **Max content width:** ~1200px centered on marketing pages.
- **Editorial body:** Single 12-column grid; hero band often uses 7/5 split (h1 left, app mockup card right).
- **Feature card grids:** 3-up at desktop, 2-up at tablet, 1-up at mobile.
- **Pricing grid:** 4-up at desktop, 2-up at tablet, 1-up at mobile.
- **Footer:** 4-column link list at desktop, wrapping to 2-up at tablet, 1-up at mobile.

### Whitespace Philosophy
Cal.com uses generous but not excessive whitespace — section padding sits at 96px (modern-SaaS standard), and card internal padding stays at 32px. The rhythm is calibrated for fast scanning: every band has a single h1 + h2 + supporting cards, never densely packed lists. The result reads as confident-not-shouting.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | `{shadow.none}`, no border | Body sections, top nav, hero bands |
| 1 — Tinted | `{colors.surface-card}` or `{colors.surface-soft}` background, `{shadow.none}` | Feature cards, testimonial cards, nav-pill-group wrapper |
| 2 — Resting | `{shadow.small}` (`0 1px 2px rgba(0,0,0,0.05)`) | Pricing tier cards, the active pill inside `{component.nav-pill-group}` |
| 3 — Raised | `{shadow.medium}` (`0 4px 12px rgba(0,0,0,0.08)`) | `{component.hero-app-mockup-card}`, dropdowns, modals, toasts |
| Inverted | `{colors.surface-dark}` background, `{shadow.none}` | The featured pricing tier and the footer — colour contrast does the elevation work |

**One mechanism per level.** A given component gets *either* a tint, *or* a shadow, *or* an inversion — never a shadow stacked on a tinted card, and never a hairline used as a substitute for a shadow. Borders in this system are boundaries, not elevation: `{colors.hairline}` is a decorative rule and `{colors.hairline-strong}` is a control edge. Where the earlier draft said a card carries "1px hairline border, subtle drop shadow", read that as level 3 with a control edge, not as two elevation signals.

The elevation philosophy is **soft and modern** — small drop shadows on elevated cards, colour-block contrast for emphasis. No heavy shadows, no neumorphism, no glassmorphism. The four light layers are deliberately close in value — `{colors.canvas}` to `{colors.surface-soft}` is 1.05:1, to `{colors.surface-card}` 1.09:1, and `{colors.surface-soft}` to `{colors.surface-card}` 1.03:1 — so **tint alone does not reliably separate two stacked layers.** Any surface that must read as a distinct layer at a glance uses `{shadow.small}` or `{shadow.medium}`, or steps to `{colors.surface-strong}` (1.24:1). The same holds in the dark: `{colors.surface-dark}` to `{colors.surface-dark-elevated}` is 1.09:1.

### Decorative Depth
- Calendar widgets and product UI fragments embedded inside marketing cards carry their own internal shadows from the product UI itself — these are not system tokens, they're product chrome shown as content.
- Avatar circles in testimonial sections sometimes carry pastel fill colors (`{colors.badge-orange}`, `{colors.badge-pink}`, etc.) — adds a small chromatic flourish without breaking the monochrome brand voice.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Almost no use — reserved for badge accents |
| `{rounded.sm}` | 6px | Small inline buttons, dropdown items |
| `{rounded.md}` | 8px | Standard CTA buttons, text inputs, category tabs |
| `{rounded.lg}` | 12px | Content cards (feature cards, testimonial cards, pricing tier cards) |
| `{rounded.xl}` | 16px | Hero app-mockup card (a slightly larger radius for the marquee component) |
| `{rounded.pill}` | 9999px | Nav-pill-group, badge pills |
| `{rounded.full}` | 9999px / 50% | Avatars, icon buttons |

`{rounded.pill}` and `{rounded.full}` hold the same 9999px value — they are two names for one step, kept apart because they describe different intents (a wrapped segment group versus a circle). Treat the ladder as six steps, not seven. `{rounded.xs}` (4px) has no documented use in the system; it stays in the scale for product-UI fragments that bring their own 4px corners.

### Focus Ring Geometry — prescribed
- Offset 2px, width 2px, drawn outside the control's own edge via `{shadow.focus-ring}`. On dark surfaces the same geometry swaps `{colors.focus}` for `{colors.focus-on-dark}` and the spacer colour for `{colors.surface-dark}`.
- The ring follows the control's own radius: `{rounded.md}` on buttons, inputs and tabs; `{rounded.full}` on `{component.avatar-circle}` and `{component.button-icon-circular}`; `{rounded.lg}` on focusable cards. No value sits outside the radius ladder.

### Photography Geometry
Avatar photos use `{rounded.full}` (perfect circles) at 36px or 40px. Product UI fragments inside marketing cards retain their native chrome (which often has its own internal radii — e.g., calendar grid cells, button rows). Hero illustration zones use 16:9 or 4:3 ratios with `{rounded.xl}` corners.

## Components

### Top Navigation

**`top-nav`** — White nav bar pinned to the top of every page. 64px tall, `{colors.canvas}` background. Carries the Cal.com wordmark + logo at left (the lowercase "Cal.com" with the brand circle), primary horizontal menu (Product, Solutions, Resources, Pricing, Enterprise) center, right-side cluster with "Sign in" text-link, "Sign up free" `{component.button-primary}`, and a sometimes-visible language selector. Menu items in `{typography.nav-link}` (Inter 14px / 500).

**`nav-pill-group`** — A small pill-radius wrapper around 2-3 sub-nav segments (e.g., the product-mode switcher between "Personal" / "Teams" / "Enterprise"). Background `{colors.surface-soft}` with internal padding 6px, rounded `{rounded.pill}`. Active segment renders as a white-canvas pill with a subtle drop shadow inside the wrapper. The pill-in-pill treatment is one of Cal.com's signature interactive components.

### Buttons

**`button-primary`** — The signature primary CTA. Background `{colors.primary}` (#111111), text `{colors.on-primary}`, type `{typography.button}` (Inter 14px / 600), padding 12px × 20px, height 40px, rounded `{rounded.md}` (8px). Active state `button-primary-active` shifts to `{colors.primary-active}` (#242424).

**`button-secondary`** — White button with hairline outline. Background `{colors.canvas}`, text `{colors.ink}`, 1px `{colors.hairline-strong}` border (the outline is the button's only boundary), same padding + height + radius as primary.

**`button-icon-circular`** — 36 × 36px circular icon button. Background `{colors.canvas}`, `{colors.hairline-strong}` border, ink-color icon. Used for share, "view more", carousel arrows.

**`button-text-link`** — Inline text button, no background. Used for "Sign in" in the top nav and inline CTA links inside cards.

**`text-link`** — Inline body links in `{colors.ink}` (the brand keeps inline links monochrome). Underlined on hover. Where a link is rendered in blue instead, it uses `{colors.brand-accent-strong}`, not `{colors.brand-accent}`, which fails AA at body size.

### Cards & Containers

**`hero-band`** — White-canvas hero with a 7-5 grid: h1 + sub-headline + button row on the left, `{component.hero-app-mockup-card}` on the right. Vertical padding `{spacing.section}` (96px).

**`hero-app-mockup-card`** — A larger product-UI mockup card showing the actual Cal.com booking widget with calendar grid, time slots, and a primary "Confirm" button inside. Background `{colors.canvas}`, 1px hairline border, rounded `{rounded.xl}` (16px), subtle drop shadow. Used as the hero's right-side artifact.

**`feature-card`** — Used in 3-up feature grids ("With us, appointment scheduling is easy"). Background `{colors.surface-card}` (#f5f5f5), rounded `{rounded.lg}` (12px), internal padding `{spacing.xl}` (32px). Carries a small icon at top, an `{typography.title-md}` headline, and a body description in `{typography.body-md}`.

**`feature-icon-card`** — A simpler card variant used in 4-up feature grids on lower-density bands. Background `{colors.canvas}` with hairline border, rounded `{rounded.lg}`, padding `{spacing.lg}` (24px). Carries a small icon, `{typography.title-sm}` title, short description.

**`product-mockup-card`** — A card showing actual Cal.com product UI fragments (workflow editor, calendar grid, integration grid, automation flow). Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.lg}` (24px). The product UI inside has its own internal chrome — these cards display the product, they don't decorate around it.

**`testimonial-card`** — Used in customer-quote grids. Background `{colors.surface-card}`, rounded `{rounded.lg}`, padding `{spacing.lg}` (24px). Top row carries a `{component.avatar-circle}` + name + role; below sits the testimonial quote in `{typography.body-md}`.

**`pricing-tier-card`** — Standard tier card. Background `{colors.canvas}`, rounded `{rounded.lg}`, padding `{spacing.xl}` (32px). Carries the plan name in `{typography.title-lg}`, price in `{typography.display-sm}`, feature checklist in `{typography.body-md}`, and a `{component.button-primary}` at the bottom.

**`pricing-tier-card-featured`** — The featured tier (typically "Teams"). Background flips to `{colors.surface-dark}` (#101010), text inverts to `{colors.on-dark}`. The dark surface IS the featured-tier signal — no accent border, no badge, no scale shift.

### Inputs & Forms

**`text-input`** — Standard text input. Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, rounded `{rounded.md}` (8px), padding 10px × 14px, height 40px. 1px border: the extracted value is `{colors.hairline}`, but since that border is the input's only boundary, use `{colors.hairline-strong}` — see Colors.

**`text-input-focused`** — Focus state. Border shifts to `{colors.ink}` for emphasis, plus the prescribed `{shadow.focus-ring}` in `{colors.focus}` so keyboard focus is visible and not only a tonal shift.

### Tags / Badges

**`badge-pill`** — Small pill label used for category tags ("Product", "Article", "New") and pastel-fill avatar substitutes. Background `{colors.surface-card}` or one of the badge pastels (`{colors.badge-orange}`, `{colors.badge-pink}`, etc.), text `{colors.ink}`, type `{typography.caption}` (13px / 500), rounded `{rounded.pill}`, padding 4px × 12px.

**`avatar-circle`** — 36px diameter, rounded `{rounded.full}`. Either holds a photo or a pastel fill with initials in `{typography.caption}`.

**`rating-stars`** — Inline star rating in `{colors.badge-orange}` (#fb923c). Used near testimonial avatars to display a 5-star satisfaction score.

### Tab / Filter

**`category-tab`** + **`category-tab-active`** — Used inside the nav-pill-group. Inactive: transparent background, `{colors.muted}` text. Active: `{colors.canvas}` background, `{colors.ink}` text, subtle drop shadow inside the pill-group wrapper. Padding 8px × 14px, rounded `{rounded.md}`.

### CTA / Footer

**`cta-band-light`** — A pre-footer "Smarter, simpler scheduling" CTA card. Background `{colors.surface-card}`, rounded `{rounded.lg}`, padding `{spacing.xxl}` (48px). Carries an h2 in `{typography.display-sm}`, a sub-line, and a `{component.button-primary}` centered.

**`footer`** — Dark navy footer that closes every page. Background `{colors.surface-dark}` (#101010), text `{colors.on-dark-soft}`. 4-column link list at desktop covering Product / Solutions / Company / Resources. Vertical padding 64px. The Cal.com wordmark sits at the top-left in `{colors.on-dark}`. The footer is the only dark surface on every page — the deliberate inversion visually closes the page.

### Component States

Cal.com's own restraint at the action layer is real and is kept: the brand darkens its primary button on press and otherwise changes very little. But "the system doesn't style hover" is not the same as "the component has no hover state", and a component that can take keyboard focus must show it. The matrix below names, for every component, the states it supports. Where the extracted design genuinely has no visual change for a state, the cell says so; where a state is prescribed rather than observed, it is marked **(p)**.

| Component | Default | Hover | Focus-visible | Active / pressed | Disabled | Loading | Selected | Error |
|---|---|---|---|---|---|---|---|---|
| `{component.button-primary}` | `{colors.primary}` fill | no visual change (brand policy) | `{shadow.focus-ring}` **(p)** | `{component.button-primary-active}` — `{colors.primary-active}` | `{component.button-primary-disabled}` — `{colors.primary-disabled}` fill, `{colors.muted}` label | label swaps for a spinner, width held **(p)** | n/a — not a toggle | n/a — error lives on the field |
| `{component.button-secondary}` | `{colors.canvas}` fill, `{colors.hairline-strong}` edge | no visual change (brand policy) | `{shadow.focus-ring}` **(p)** | edge steps to `{colors.ink}` **(p)** | edge `{colors.hairline}`, label `{colors.muted}` **(p)** | spinner in place of label **(p)** | n/a | n/a |
| `{component.button-icon-circular}` | 36px circle, `{colors.hairline-strong}` edge | no visual change (brand policy) | `{shadow.focus-ring}` at `{rounded.full}` **(p)** | icon `{colors.primary-active}` **(p)** | icon `{colors.muted}` **(p)** | spinner replaces icon **(p)** | n/a | n/a |
| `{component.button-text-link}` / `{component.text-link}` | `{colors.ink}`, no underline | underline appears | `{shadow.focus-ring}` **(p)** | `{colors.primary-active}` **(p)** | `{colors.muted}`, no underline **(p)** | n/a | n/a | n/a |
| `{component.text-input}` | `{colors.canvas}` fill, `{colors.hairline-strong}` edge | no visual change | `{component.text-input-focused}` — edge `{colors.ink}` plus `{shadow.focus-ring}` **(p)** | n/a — an input is not pressed | edge `{colors.hairline}`, text `{colors.muted}`, fill `{colors.surface-soft}` **(p)** | trailing spinner, field stays editable **(p)** | n/a | edge `{colors.error}`, message in `{colors.error-text}` at `{typography.body-sm}` **(p)** |
| `{component.category-tab}` | transparent, `{colors.muted}` label | no visual change | `{shadow.focus-ring}` **(p)** | label `{colors.ink}` **(p)** | label `{colors.muted-soft}`, not focusable **(p)** | n/a | `{component.category-tab-active}` — `{colors.canvas}` pill, `{colors.ink}` label, `{shadow.small}`; carries `aria-selected` **(p)** | n/a |
| `{component.nav-pill-group}` | `{colors.surface-soft}` wrapper | wrapper unchanged | ring is drawn on the focused child tab, never on the wrapper **(p)** | n/a | whole group dimmed to 0.5 opacity **(p)** | n/a | exactly one child is selected at all times | n/a |
| `{component.top-nav}` | `{colors.canvas}` bar, 64px | menu items underline | `{shadow.focus-ring}` on each item **(p)** | n/a | n/a | n/a | current-section item renders in `{colors.ink}` rather than `{colors.muted}` **(p)** | n/a |
| `{component.feature-card}` / `{component.feature-icon-card}` | tinted or hairline card, `{shadow.none}` | **two states only** — static content, no hover, no focus unless the whole card is a link | if linked: `{shadow.focus-ring}` at `{rounded.lg}` **(p)** | n/a | n/a | skeleton block at `{colors.surface-card}`, no shimmer **(p)** | n/a | n/a |
| `{component.product-mockup-card}` / `{component.hero-app-mockup-card}` | `{shadow.medium}`, `{rounded.xl}` or `{rounded.lg}` | no lift — the card is a frame, not a control | n/a — the product UI inside owns its own focus | n/a | n/a | image placeholder at `{colors.surface-soft}` **(p)** | n/a | n/a |
| `{component.testimonial-card}` | `{colors.surface-card}`, `{shadow.none}` | **two states only** — default and loading; the card is not interactive | n/a | n/a | n/a | skeleton rows at `{colors.surface-strong}` **(p)** | n/a | n/a |
| `{component.pricing-tier-card}` / `{component.pricing-tier-card-featured}` | `{shadow.small}` / inverted dark | no visual change | ring on the contained `{component.button-primary}` only **(p)** | n/a | tier marked unavailable: 0.5 opacity, button disabled **(p)** | price area skeleton while billing period switches **(p)** | featured tier is the selected tier — signalled by `{colors.surface-dark}`, nothing else | n/a |
| `{component.badge-pill}` / `{component.rating-stars}` | pill or stars | **single state** — purely decorative labels, never interactive | n/a | n/a | n/a | n/a | n/a | n/a |
| `{component.avatar-circle}` | photo or pastel fill | no visual change | if linked to a profile: `{shadow.focus-ring}` at `{rounded.full}` **(p)** | n/a | n/a | `{colors.surface-card}` fill with no initials **(p)** | n/a | fill `{colors.surface-strong}` with initials when the image 404s **(p)** |
| `{component.cta-band-light}` | `{colors.surface-card}` band | band unchanged | ring on the contained button only **(p)** | n/a | n/a | n/a | n/a | n/a |
| `{component.footer}` | `{colors.surface-dark}` | link brightens to `{colors.on-dark}` | `{colors.focus-on-dark}` ring **(p)** | n/a | n/a | n/a | n/a | newsletter field, when present, uses the `{component.text-input}` error treatment on `{colors.surface-dark-elevated}` **(p)** |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted from cal.com; each value is inferred from the documented visual voice — white canvas, near-monochrome action layer, weight-600 geometric display type, and a stated policy of minimal state change. Treat the table as a proposal consistent with the brand, not as observed fact.

**Profile: Calm** (`roster.md` assigns Playful; see the note below for why this file uses Calm instead). Base duration `{motion.duration-base}` (250ms), symmetric easing `{motion.ease-standard}`, stagger `{motion.stagger-step}` (40ms). Short opacity-led fades, very little travel.

### Why Calm and not Playful

The assignment rule in the audit spec reaches Playful only on a *saturated multi-colour or illustration-led consumer identity*, judged on saturation **and role**. Cal.com fails both halves of that test on this file's own evidence: the action layer is explicitly monochrome (`{colors.primary}` is #111111, and the Don'ts section forbids accent colour on primary CTAs); the badge pastels appear only on avatar fills and tag pills, never on an interactive element; the single brand blue is described as appearing "rarely"; and the type voice is a weight-600 geometric face with negative tracking, described in this file as "confidently engineered without trying to impress" and "confident-not-shouting" — not light or informal. The identity is not dark-luxury (rule 1) and the documented surface is a marketing site rather than a terminal or IDE (rule 2), so rule 4 applies and the profile is **Calm**. Scale pops and springy overshoot would read as borrowed from a consumer app, which this file's own Don'ts warn against ("larger radii read as consumer-app, not professional booking software"). Playful is recorded in the roster; this file documents Calm and says so rather than switching silently.

### Motion Inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (links, nav items, footer links) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` (and the link underline's `transform: scaleX()`, drawn from the inline edge) | Underline appears instantly, no scale; opacity change kept at `{motion.duration-fast}` |
| Press (`{component.button-primary}`, tabs, icon buttons) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` only — the fill swap to `{colors.primary-active}` is immediate, with no scale pop | Unchanged; already at 80ms with no travel |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears with no transition — focus must never lag the key press |
| Page / route transition | `{motion.duration-base}` out `{motion.duration-fast}` | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, plus `transform: translateY(8px)` on enter | Cross-fade only, 150ms, no translate |
| Modal / drawer | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(12px)` (drawer: `translateX`); scrim fades `opacity` alone | Opacity fade at `{motion.duration-fast}`, no translate; scrim unchanged |
| Dropdown / select menu | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(4px)` | Opacity only, `{motion.duration-fast}` |
| Toast | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(16px)` | Opacity only, `{motion.duration-fast}`; dismiss timer lengthened, never removed |
| List enter (feature grids, calendar slot lists, integration tiles) | `{motion.duration-base}` per item, `{motion.stagger-step}` between items, 6 items maximum then the rest appear together | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px)` | All items fade together in `{motion.duration-fast}`, no stagger, no translate |
| List exit (filtered-out cards, removed slots) | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: scale(0.98)` | Opacity only, `{motion.duration-fast}` |
| Loading (button spinner, skeleton blocks) | 800ms, infinite | linear (spinner) / `{motion.ease-standard}` (skeleton pulse) | `transform: rotate()` on the spinner; `opacity` 0.6→1 on skeletons | Spinner frozen and replaced by a static "Loading…" label; skeleton pulse frozen at its mid opacity |

### Motion Rules

- Only `transform` and `opacity` animate. Never `width`, `height`, `top`, `left` or `margin` — a dropdown that appears to grow does so by scaling a fixed-size layer, not by animating its height.
- Every exit is shorter than its matching entrance (modal 250ms in / 150ms out; dropdown 150ms in / 80ms out; toast 250ms in / 150ms out).
- Nothing animates on first paint in a way that delays content. Hero copy and the hero mockup card render at full opacity; list stagger runs only on lists that change *after* load (filtering, slot fetches), never on the initial server-rendered grid.
- The loading spinner and the skeleton pulse are the only infinite animations in the system. There is no brand ambience — no drifting gradient, no looping hero video, no perpetual calendar demo. Cal.com's page is still when the user is still.
- `{motion.duration-slow}` and `{motion.duration-emphasis}` exist for completeness and are unused in this system. A Calm profile on a scheduling tool has nothing that should take 400ms or longer; if a future surface needs one, it is a deliberate exception and should be documented as such.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. Every translateY/translateX/scale/rotate
     transition collapses to no transform at all — elements appear in their final
     position. The list stagger is removed; items appear together. */
  *, *::before, *::after {
    transition-property: opacity;
    transition-duration: 150ms;      /* {motion.duration-fast} ceiling */
    animation: none;                 /* freezes the skeleton pulse mid-cycle */
  }
  /* Kept: opacity fades at 150ms or less, so state changes stay legible. */
  /* Kept: the focus ring, which has no transition in either mode. */
  /* Replaced, not removed: the loader. The spinner's rotate() is frozen and a
     static "Loading…" label carries the meaning instead, so progress is still
     communicated. */
}
```

What is **removed**: translate, scale and rotate on every interaction above; the `{motion.stagger-step}` cascade on list enter; the spinner's rotation; the skeleton pulse.
What is **kept**: all opacity fades, capped at `{motion.duration-fast}` (150ms); the instant focus ring; every colour and border state change, which is immediate in both modes; and a textual loading indicator in place of the frozen spinner.

## Accessibility

### Measured contrast

All ratios below were computed with WCAG 2.1 relative luminance from this file's own frontmatter hexes.

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 18.88:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.surface-card}` | 17.32:1 | 4.5 | Pass |
| `{colors.ink}` on `{colors.surface-soft}` | 17.91:1 | 4.5 | Pass |
| `{colors.body}` on `{colors.canvas}` | 10.31:1 | 4.5 | Pass |
| `{colors.muted}` on `{colors.canvas}` | 4.83:1 | 4.5 | Pass |
| `{colors.muted}` on `{colors.surface-card}` | 4.43:1 | 4.5 | **Fail** — use `{colors.body}` inside gray cards |
| `{colors.muted-soft}` on `{colors.canvas}` | 3.50:1 | 4.5 | **Fail** — real brand fails AA; 18px+ only |
| `{colors.on-primary}` on `{colors.primary}` | 18.88:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.primary-active}` | 15.52:1 | 4.5 | Pass |
| `{colors.on-primary}` on `{colors.brand-accent}` | 3.68:1 | 4.5 | **Fail** — real brand fails AA; use `{colors.brand-accent-strong}` (6.70:1) |
| `{colors.brand-accent}` on `{colors.canvas}` | 3.68:1 | 4.5 | **Fail** — same; link text uses `{colors.brand-accent-strong}` |
| `{colors.on-dark}` on `{colors.surface-dark}` | 19.03:1 | 4.5 | Pass |
| `{colors.on-dark-soft}` on `{colors.surface-dark}` | 7.42:1 | 4.5 | Pass |
| `{colors.hairline}` on `{colors.canvas}` | 1.24:1 | 3.0 | **Fail** — decorative only; real brand fails for control edges |
| `{colors.hairline-strong}` on `{colors.canvas}` | 3.35:1 | 3.0 | Pass (prescribed) |
| `{colors.error}` on `{colors.canvas}` | 3.76:1 | 4.5 | **Fail** — fill tone; error copy uses `{colors.error-text}` (6.47:1) |
| `{colors.ink}` on `{colors.badge-violet}` | 4.46:1 | 4.5 | **Fail** by 0.04 — no 13px labels on violet |

**Stated plainly:** Cal.com's real palette fails AA in four places — the hairline as a control boundary, the brand blue as text or as a white-text fill, the tertiary grey at body size, and the three saturated semantic fills as text. None of those hexes is altered here, because they are extracted facts. Each has a prescribed accessible sibling named above.

### Focus ring visibility, per surface this file defines

| Surface | Ring token | Ratio | Verdict |
|---|---|---|---|
| `{colors.canvas}` #ffffff | `{colors.focus}` | 5.17:1 | Pass |
| `{colors.surface-soft}` #f8f9fa | `{colors.focus}` | 4.90:1 | Pass |
| `{colors.surface-card}` #f5f5f5 | `{colors.focus}` | 4.74:1 | Pass |
| `{colors.surface-strong}` #e5e7eb | `{colors.focus}` | 4.17:1 | Pass |
| `{colors.primary}` #111111 (the black CTA fill) | `{colors.focus}` | 3.65:1 | Pass |
| `{colors.surface-dark}` #101010 (footer, featured tier) | `{colors.focus-on-dark}` | 7.48:1 | Pass |
| `{colors.surface-dark-elevated}` #1a1a1a | `{colors.focus-on-dark}` | 6.85:1 | Pass |

`{colors.focus}` is drawn on every light surface and on the black primary button; `{colors.focus-on-dark}` is drawn on the two dark surfaces only. The 2px white spacer in `{shadow.focus-ring}` is what keeps the light ring legible on the black CTA — on dark surfaces that spacer becomes `{colors.surface-dark}`.

### Minimum tap target

Not verifiable from this document — tap-target size needs a rendered page, and nothing here was measured in a browser. What the token values *state* is:
- `{component.button-primary}` and `{component.text-input}` are 40px tall. 40 < 44, so both need 4px of vertical padding around them in layout, or an enlarged hit area, to reach the WCAG 2.5.5 44 × 44 target. The earlier claim that 40 × 40 is a sufficient "minimum" is wrong and is corrected here.
- `{component.button-icon-circular}` is 36 × 36 — 8px short on both axes. A circular silhouette does not compensate for an undersized target; this needs an invisible 44 × 44 hit area.
- `{component.category-tab}` has no stated height, only 8 × 14 padding. Its effective target cannot be computed from this file. The earlier claim that it "meets 44px+ with the surrounding pill" is unverifiable and is withdrawn to Known Gaps.

### Keyboard and semantics

- Every interactive component in the states matrix above has a focus-visible row. The ring is never suppressed — `outline: none` without a replacement ring is a defect, not a style choice.
- `{component.nav-pill-group}` is a tablist: arrow keys move between `{component.category-tab}` children, exactly one carries `aria-selected`, and focus never lands on the wrapper.
- Colour is never the only carrier of state. The featured pricing tier is signalled by `{colors.surface-dark}` alone in the extracted design; a text label ("Most popular") is prescribed so the signal survives for a colour-blind or high-contrast reader. Validation shows an icon and message, not only a red edge.
- Disabled controls keep their text legible where practical, but `{colors.primary-disabled}` with a `{colors.muted}` label is exempt from contrast requirements under WCAG and is not reported as a failure.

### Reduced motion

Honoured as specified in the Motion & Animation section: all travel and scale removed, opacity fades capped at 150ms, loaders frozen and replaced by a static label. There is no brand ambience to freeze.

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
| `{colors.hairline-soft}` (`#f3f4f6`) on `{colors.surface-card}` (`#f5f5f5`) | 1.01:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.hairline-soft}` (`#f3f4f6`) on `{colors.canvas}` (`#ffffff`) | 1.10:1 | 3.0:1 | Fail — boundary, all tones |
| `{colors.hairline}` (`#e5e7eb`) on `{colors.surface-card}` (`#f5f5f5`) | 1.14:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.warning}` (`#f59e0b`) on `{colors.surface-card}` (`#f5f5f5`) | 1.97:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.warning}` (`#f59e0b`) on `{colors.canvas}` (`#ffffff`) | 2.15:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.success}` (`#10b981`) on `{colors.surface-card}` (`#f5f5f5`) | 2.33:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.success}` (`#10b981`) on `{colors.canvas}` (`#ffffff`) | 2.54:1 | 4.5:1 | Fail — semantic tone as text |
| `{colors.muted-soft}` (`#898989`) on `{colors.surface-card}` (`#f5f5f5`) | 3.21:1 | 4.5:1 | Fail — secondary text on surface, all tones |
| `{colors.error}` (`#ef4444`) on `{colors.surface-card}` (`#f5f5f5`) | 3.45:1 | 4.5:1 | Fail — semantic tone as text |

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (#111111) for primary CTAs and h1/h2 type. Cal.com's button is near-black, not blue.
- Use Cal Sans for every display headline. Pair with Inter body. Never blur the boundary.
- Apply negative letter-spacing on display sizes (-0.5 to -2px). Cal Sans without it reads as off-brand.
- Use `{component.feature-card}` (light gray) and `{component.product-mockup-card}` (white with chrome) deliberately — the gray cards signal "abstract feature claim", white cards signal "look at the actual product".
- Embed real product UI fragments inside marketing cards. Don't paint marketing illustrations of the product when you can show the product itself.
- Keep avatar circles at 36px, perfect circles, sometimes with pastel fills. Avatars are the only place where badge pastels appear.
- Use `{component.nav-pill-group}` for grouped sub-nav segments. The pill-in-pill treatment is signature.
- End every page with the dark footer. The light-to-dark transition is part of the editorial rhythm.

### Don't
- Don't use accent colors (`{colors.brand-accent}`, badge pastels) on primary CTAs. The system is monochrome at the action layer.
- Don't bold display weight beyond 600. Cal Sans at 700 reads as bombastic.
- Don't use rounded radius beyond `{rounded.xl}` (16px) on cards. Larger radii read as consumer-app, not professional booking software.
- Don't put dark surface cards anywhere except the footer and the featured pricing tier. The dark surface is a deliberate, scarce signal.
- Don't repeat the same surface mode in two consecutive bands. Cal.com's pacing alternates white → light-gray → white → product-mockup-card → white → dark-footer.
- Don't add hover state styling beyond what the system already encodes — primary darkens on press, links underline; nothing else changes on hover.
- Don't read that restraint as permission to drop the focus ring. `{colors.focus}` is mandatory on every focusable control, and `outline: none` without a replacement ring is a defect.
- Don't use `{colors.hairline}` as the only edge of a control, or `{colors.brand-accent}` / `{colors.muted-soft}` / `{colors.error}` as body text. Each fails AA; each has a prescribed sibling.
- Don't add scale pops or springy overshoot. This system is Calm, not Playful — see Motion & Animation.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav; hero h1 64→32px; hero-app-mockup-card stacks below content; feature grids 1-up; pricing 1-up; footer 4 cols → 1 |
| Tablet | 768–1024px | Top nav stays horizontal but tightens; nav-pill-group wraps; feature cards 2-up; pricing 2-up |
| Desktop | 1024–1440px | Full top-nav with all menu items; 3-up feature cards; 4-up pricing tiers |
| Wide | > 1440px | Same as desktop with more outer breathing room; max content width caps at 1200px |

### Touch Targets
Stated token sizes only — no target was measured in a browser, so none of these is a verified tap area. See the Accessibility section.
- `{component.button-primary}` is 40px tall, 8px short of WCAG 2.5.5's 44 × 44. Needs surrounding padding or an enlarged hit area on touch.
- `{component.button-icon-circular}` is exactly 36 × 36 — under 44 × 44 on both axes. A circular silhouette does not compensate; give it an invisible 44 × 44 hit area.
- `{component.text-input}` height is 40px — same 4px shortfall as the primary button.
- `{component.category-tab}` inside `{component.nav-pill-group}` has 8 × 14 padding and no stated height, so its effective tap area cannot be computed from this document.

### Collapsing Strategy
- Top nav collapses to hamburger at < 768px; menu opens as a full-screen sheet.
- Hero band's 7-5 grid collapses to single-column on mobile — h1 + sub-head + buttons first, then the app-mockup card below.
- Feature grids reduce columns rather than scaling cards down.
- Pricing tier cards collapse 4 → 2 → 1; featured-tier dark surface stays visually distinct at every breakpoint.
- Nav-pill-group wraps to multi-row on tablet if the segments don't fit horizontally.
- Avatar + testimonial card layouts stay grid-aligned at every breakpoint.

### Image Behavior
- Product UI fragments inside cards retain native aspect ratios; the cards themselves resize.
- Avatar photos crop to circles at every breakpoint.
- Hero app-mockup card scales proportionally on mobile — the calendar grid stays legible.

## Iteration Guide

1. Focus on ONE component at a time. Reference its YAML key directly (`{component.feature-card}`, `{component.pricing-tier-card-featured}`).
2. Variants of an existing component (`-active`, `-disabled`, `-focused`) live as separate entries in `components:`.
3. Use `{token.refs}` everywhere — never inline hex.
4. Document every state a component supports, including hover and focus-visible, even where the honest answer is "no visual change". Cal.com's restraint is a design decision worth recording, not a reason to leave the row blank. See the Component States matrix.
5. Display headlines stay Cal Sans 600 with negative letter-spacing. Body stays Inter 400. The trinity does not blur.
6. The dark footer is the only dark surface on most pages. Don't add other dark cards casually.
7. When in doubt about emphasis: bigger Cal Sans before bolder Cal Sans.

## Known Gaps

- The dembrandt frequency analyzer captured `Buttons: 0 variants` — Cal.com renders most CTAs as styled `<a>` link elements rather than `<button>` tags, which dembrandt's button selector doesn't capture. Button styles are documented from screenshot ground-truth + standard Cal Sans / Inter baselines.
- Cal Sans is licensed to Cal.com and not available as a public web font; substitutes are documented in the typography section.
- The badge pastel set (orange / pink / violet / emerald) is documented from observed avatar fill colors; exact hex values may shift seasonally.
- **Every value in Motion & Animation is prescribed, not extracted.** No real Cal.com duration, easing curve or stagger was measured — the calendar slot picker, schedule confirmation and integration-grid reveals were never timed. The profile (Calm) is argued from this file's own visual evidence, and the roster assigns Playful; the disagreement is documented in that section rather than resolved silently.
- **The focus ring is prescribed.** `{colors.focus}`, `{colors.focus-on-dark}` and `{shadow.focus-ring}` were not captured from the live site; no focus treatment was extracted at all. The hues are chosen as accessible siblings of the brand's existing blue.
- `{colors.hairline-strong}`, `{colors.brand-accent-strong}`, `{colors.success-text}`, `{colors.warning-text}` and `{colors.error-text}` are prescribed accessible parallels, not brand colours. The extracted tones they sit beside are unchanged.
- The `{shadow.small}` and `{shadow.medium}` values are read from rgba strings already written in this file's Elevation prose; they were not re-measured, and `{shadow.focus-ring}` is prescribed.
- Tap-target sizes are stated token heights, not measured hit areas. Nothing in this document was rendered, so no claim here about actual tap area, overlap or overflow is verified. The previous claim that `{component.category-tab}` "meets 44px+ with the surrounding pill" is withdrawn as unverifiable.
- Form validation states beyond `{component.text-input-focused}` are not extracted — the error, loading and disabled rows in the Component States matrix are marked prescribed and would need a sign-up or booking flow to confirm.
- Loading and skeleton treatments are prescribed throughout; no loading state was observed on the marketing surface.
- The actual booking widget surface (cal.com/{username}) is the product, not a marketing surface; its spec is out of scope.
- Avatar photos in testimonial sections sometimes carry pastel circular fills with initials instead of photographs; both treatments coexist on the same page.
