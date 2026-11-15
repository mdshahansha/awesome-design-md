---
version: alpha
name: Ollama-design-analysis
description: |
  An almost defiantly minimal documentation-first system that treats the home page like a Markdown README — paper-white canvas, 36px center-aligned heading, a single black pill CTA, an inline terminal install snippet, and a hand-drawn llama mascot as the only ornamental element. No gradient, no hero photography, no marketing pyrotechnics. The chrome is a tiny utility palette of pure black, pure white, and three neutral grays; every interactive element is fully rounded into a pill (`{rounded.full}`); typography is SF Pro Rounded for headings paired with system sans for body and ui-monospace for code. Pricing tiers, FAQs, and "your data stays yours" guarantees all sit on the same flat canvas inside thin-border cards — the system is the documentation, and the documentation is the system.

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  ink: "#000000"
  ink-deep: "#090909"
  charcoal: "#525252"
  body: "#737373"
  mute: "#a3a3a3"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  hairline: "#e5e5e5"
  hairline-strong: "#d4d4d4"
  hairline-control: "#8f8f8f"
  on-dark: "#ffffff"
  on-dark-mute: "rgba(255,255,255,0.7)"
  surface-dark: "#171717"
  focus-ring: "rgba(59,130,246,0.5)"
  focus-ring-strong: "#3b82f6"
  link: "#000000"
  link-mute: "#737373"
  terminal-red: "#ff5f56"
  terminal-yellow: "#ffbd2e"
  terminal-green: "#27c93f"

typography:
  display-xl:
    fontFamily: SF Pro Rounded
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.11
    letterSpacing: 0
  display-lg:
    fontFamily: SF Pro Rounded
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  heading-lg:
    fontFamily: SF Pro Rounded
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  heading-md:
    fontFamily: ui-sans-serif
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  heading-sm:
    fontFamily: ui-sans-serif
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: ui-sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-strong:
    fontFamily: ui-sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: ui-sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  body-sm-strong:
    fontFamily: ui-sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  caption-sm:
    fontFamily: ui-sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  code-md:
    fontFamily: ui-monospace
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  code-sm:
    fontFamily: ui-monospace
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: ui-sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0

rounded:
  none: 0px
  sm: 6px
  md: 8px
  lg: 12px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 88px

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
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.mute}"
    rounded: "{rounded.full}"
  search-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  search-pill-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  install-snippet:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.code-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  command-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.full}"
    padding: 6px 12px
  terminal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.lg}"
    padding: 16px
  terminal-traffic-lights:
    rounded: "{rounded.full}"
    size: 12px
  pricing-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  feature-bullet:
    textColor: "{colors.charcoal}"
    typography: "{typography.body-sm}"
  faq-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 16px 0px
  link-inline:
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
  link-mute:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  primary-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.none}"
    height: 56px
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.none}"
    padding: 32px 24px
  cta-strip-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-lg}"
    rounded: "{rounded.lg}"
    padding: 24px 32px
---

## Overview

Ollama's site is the most aggressively under-designed marketing surface in the AI tooling space, and that is the entire point. The home page reads like a Markdown README rendered with care: a 36px center-aligned heading sits above an inline `curl` install snippet inside a soft-gray pill, a single black "Download" CTA, and a hand-drawn llama mascot as the only ornament. Everything else — automate-your-work block, "Start local. Scale cloud." pricing pair, "Your data stays yours" guarantee strip, FAQ wall on `/pricing` — sits on the same paper-white canvas (`{colors.canvas}`) with quiet `{colors.body}` neutrals carrying the prose. The system is the documentation, and the documentation is the system.

The design philosophy is geometric: every interactive element collapses to `{rounded.full}` (9999px) — buttons, search pills, install-snippet pills, text inputs, and the terminal-traffic-light dots. There are no decorative drop shadows, no gradients, no hero illustrations beyond the llama. Cards (the rare ones, on `/pricing`) use a soft `{rounded.lg}` (12px) and a 1px hairline. The single inverted moment in the entire system is the dark "Max" pricing tier — `{colors.surface-dark}` with white text — which acts as the only attention-grabbing surface in an otherwise studiously flat layout.

Typography pairs SF Pro Rounded (display headings, weight 500–600) with the operating system's default sans (`ui-sans-serif`) for body and `ui-monospace` for code. The roundness of the heading face is the only "personality" the chrome carries — it gently echoes the `{rounded.full}` button geometry without being decorative about it.

**Key Characteristics:**
- Paper-white `{colors.canvas}` end-to-end with no surface alternation — the whole page is one continuous sheet
- Center-aligned hero with `{typography.display-xl}` SF Pro Rounded headline, no eyebrow, no subhead beyond a small "Power OpenClaw with Ollama" line under the llama
- Pill geometry everywhere: every button and pill input is `{rounded.full}`; cards use `{rounded.lg}`; nothing is sharp-cornered except section dividers
- Single-color CTA system: pure black `{colors.primary}` pills carry every action; "Get Pro" / "Get Max" inside pricing cards are the only variations
- Inline `curl` install snippet rendered as a pill with `{typography.code-md}` — the most signature element, sitting directly under the hero headline
- Terminal-mockup card with macOS traffic-light dots and inline `ollama launch openclaw` example — the home page's only "product preview"
- Inverted dark `{component.pricing-card-dark}` for the highest-tier "Max" plan, breaking the flat-white rhythm exactly once per page

## Colors

> **Source pages:** `/` (home) and `/pricing`. The chrome palette is identical across both — only content changes.

### Brand & Accent
- **Pure Black** (`{colors.primary}` — `#000000`): the brand. Every primary CTA, every black pill, every link in the nav, and every solid icon. There is no other "brand color."
- **Ink Deep** (`{colors.ink-deep}` — `#090909`): pressed-state black for the primary pill — a single notch below pure.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): the page itself. Nearly every surface in the system.
- **Soft Surface** (`{colors.surface-soft}` — `#fafafa`): install-snippet pill background, search pill, secondary chip backgrounds, alternating row fill where one is needed.
- **Surface Dark** (`{colors.surface-dark}` — `#171717`): the dark "Max" pricing card and dark CTA strips. The single inverted surface in the system.
- **Hairline** (`{colors.hairline}` — `#e5e5e5`): 1px card border, divider line above footer, divider between FAQ rows.
- **Hairline Strong** (`{colors.hairline-strong}` — `#d4d4d4`): rare slightly stronger divider where extra separation is needed (e.g., between unrelated FAQ groups).
- **Hairline Control** (`{colors.hairline-control}` — `#8f8f8f`): **prescribed, not extracted.** Both extracted hairlines are decorative-weight only — `{colors.hairline}` measures 1.26:1 and `{colors.hairline-strong}` 1.48:1 against `{colors.canvas}`, far below the 3:1 a non-text boundary needs. Where a hairline is the *only* thing defining a control — the `{component.text-input}` edge, the `{component.button-secondary}` outline, the `{component.search-pill}` rim once it leaves its soft fill — use this tone instead: 3.23:1 on `{colors.canvas}` and 3.10:1 on `{colors.surface-soft}`. The extracted hairlines stay as documented for card edges, FAQ dividers and the footer rule, where the boundary is decoration rather than the affordance. See `## Accessibility`.

### Text
- **Ink** (`{colors.ink}` — `#000000`): all headlines, primary nav links, button text on light surfaces, prices on pricing cards.
- **Charcoal** (`{colors.charcoal}` — `#525252`): list-item text and disabled-state secondary copy.
- **Body** (`{colors.body}` — `#737373`): default body color for paragraph copy, FAQ answers, footer link text — the system's most-used text color after pure black.
- **Mute** (`{colors.mute}` — `#a3a3a3`): caption text, command-line "comment" gray inside terminal mockups, lowest-emphasis utility text.
- **On Dark** (`{colors.on-dark}` — `#ffffff`): primary text on `{colors.surface-dark}`.
- **On Dark Mute** (`{colors.on-dark-mute}` — `rgba(255,255,255,0.7)`): secondary copy inside the dark "Max" pricing card.

### Semantic
The system has effectively no error/success/warning palette in its public marketing surfaces — there are no validation states, no destructive flows, no banners. The only "semantic" colors are the macOS terminal traffic lights inside the terminal mockup:

- **Terminal Red** (`{colors.terminal-red}` — `#ff5f56`): close-window dot.
- **Terminal Yellow** (`{colors.terminal-yellow}` — `#ffbd2e`): minimize dot.
- **Terminal Green** (`{colors.terminal-green}` — `#27c93f`): zoom dot.

These appear only inside `{component.terminal-card}` and have no other use.

### Focus
- **Focus Ring** (`{colors.focus-ring}` — `rgba(59,130,246,0.5)`): the extracted value — the translucent blue browser-default ring the live site leaves in place around interactive elements. The only blue in the system. At 50% alpha it composites to `#9dc0fa` over `{colors.canvas}`, which measures 1.85:1 — it is not a usable focus indicator anywhere on this brand's light surfaces.
- **Focus Ring Strong** (`{colors.focus-ring-strong}` — `#3b82f6`): **prescribed, not extracted.** The same blue with the alpha removed, which is the whole fix: the hue was never the problem, the transparency was. One ring serves the entire system because this file has three surface polarities (paper-white, `#fafafa` soft fill, and the inverted `{colors.surface-dark}` / `{colors.ink-deep}` grounds), and a mid-luminance blue clears 3:1 against all of them — 3.68:1 on `{colors.canvas}`, 3.52:1 on `{colors.surface-soft}`, 4.87:1 on `{colors.surface-dark}`, 5.41:1 on `{colors.ink-deep}`. No light/dark pair is needed. Drawn as a 2px ring **outside** the control with a 2px offset in the underlying surface colour, so it is judged against the surface behind it (WCAG 2.2 Focus Appearance) rather than against the black pill it surrounds — a ring required to clear both `{colors.canvas}` and a pure-black `{colors.primary}` fill has no solution. On the one dark surface, the same ring is drawn with a `{colors.surface-dark}` offset.

## Typography

### Font Family
- **SF Pro Rounded** (display headings) — Apple's rounded geometric sans, used at weights 500 and 600 for headlines from `{typography.display-xl}` (36px) down to `{typography.heading-lg}` (24px). Falls back to `system-ui` → `-apple-system`.
- **ui-sans-serif** (body, links, buttons, captions) — the operating system's default sans-serif. Carries every non-display text role at 12–20px. Falls back through `system-ui` and platform emoji families.
- **ui-monospace** (code, install snippet, command tags) — the OS default monospace. Used inside the terminal mockup, the inline `curl` install pill, and any inline `<code>` formatting. Falls back to SFMono-Regular → Menlo → Monaco → Consolas.

The pairing of SF Pro Rounded display + system sans body + system mono code is intentionally "stock Apple" — the design decision is to not have a typography decision. Branded display faces would compete with the system's documentation feel.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 36px | 500 | 1.11 | 0 | Hero headline ("The easiest way to build with open models") |
| `{typography.display-lg}` | 30px | 500 | 1.2 | 0 | Major section headlines ("Pricing", "Frequently asked questions") |
| `{typography.heading-lg}` | 24px | 600 | 1.33 | 0 | Section subheading inside body ("Automate your work", "Start local. Scale cloud.") |
| `{typography.heading-md}` | 20px | 500 | 1.4 | 0 | Pricing tier name ("Free", "Pro", "Max"), card title |
| `{typography.heading-sm}` | 18px | 500 | 1.56 | 0 | FAQ question label, in-card subtitle |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default body, FAQ answers, paragraph copy |
| `{typography.body-strong}` | 16px | 500 | 1.5 | 0 | Inline emphasis, primary-nav link |
| `{typography.body-sm}` | 14px | 400 | 1.43 | 0 | Feature bullet ("Access larger models on data-center-grade hardware"), footer link |
| `{typography.body-sm-strong}` | 14px | 500 | 1.43 | 0 | Button label, pricing-card eyebrow ("Solve harder tasks, faster") |
| `{typography.caption-sm}` | 12px | 400 | 1.33 | 0 | Footer copyright row, smallest meta text |
| `{typography.code-md}` | 16px | 400 | 1.5 | 0 | Install-snippet `curl` line, in-terminal command |
| `{typography.code-sm}` | 14px | 400 | 1.43 | 0 | Terminal output line, inline `<code>` chips |
| `{typography.button-md}` | 14px | 500 | 1 | 0 | Every button label across the system |

### Principles
The typography is built for legibility at small sizes on a flat-white canvas. SF Pro Rounded's softened terminals on the heading face do almost all of the brand expression; everything below 20px collapses into the operating system's default sans, which renders identically to the way docs.ollama.com and the Ollama CLI's own help text would appear in a terminal. There is almost no letter-spacing variation, no display-only weights, no italic, and the heading-to-body ratio compresses tightly (36 → 30 → 24 → 20 → 16) so the page reads as a single readable column rather than a marketing pyramid.

### Note on Font Substitutes
SF Pro Rounded is Apple-licensed and ships only on macOS/iOS. On other systems it falls back to `system-ui` (Segoe UI / Roboto / DejaVu Sans depending on platform) — Ollama explicitly accepts that the heading face will look slightly different on Windows/Linux. The closest open-source substitute is **Nunito** (rounded geometric sans, weights 500/600). For the body face, **Inter** is a near-perfect match for `system-ui` rendered metrics. For code, **JetBrains Mono** or **Fira Code** are the canonical open-source substitutes for `ui-monospace`.

## Layout

### Spacing System
- **Base unit:** 8px (with finer 2/4/6px steps available for tight inline gaps)
- **Tokens (front matter):** `{spacing.xxs}` (2px) · `{spacing.xs}` (4px) · `{spacing.sm}` (8px) · `{spacing.md}` (12px) · `{spacing.lg}` (16px) · `{spacing.xl}` (24px) · `{spacing.xxl}` (32px) · `{spacing.section}` (88px)
- **Universal section rhythm:** every page uses `{spacing.section}` (88px) as the vertical gap between major content blocks (hero → automate → start local/scale cloud → your data stays yours → get-started footer call). This is the single largest spacing token in the system and it is used liberally.
- **Card internal padding:** pricing cards sit at `{spacing.xxl}` (32px) all around; FAQ rows use `{spacing.lg}` (16px) vertical with no horizontal padding.

### Grid & Container
- **Max width:** ~720px content column on the home page (the whole page is laid out as a single narrow reading column with optional 2-column splits inside specific sections).
- **Pricing grid:** 3-up cards at desktop with a max content width of ~960px; collapses to 1-up below 768px.
- **Automate-your-work split:** desktop 50/50 left-text/right-terminal-mockup; mobile stacks vertical with the terminal below the text.
- **FAQ:** single-column stacked rows, full-width within the 720px content column.
- **Footer:** single-row of small body-sm links, center-aligned at desktop, wrapping to two rows on narrow screens.

### Whitespace Philosophy
Whitespace is the entire layout. Sections are separated by 88px of plain white air, never by decorative dividers, never by colored bands. Inside a section, content sits in a tight reading column with no decorative columns, callout boxes, or lifted cards. The site treats the page as a long-form Markdown document, and the air between sections is the equivalent of a blank line in Markdown source.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Hero, automate-your-work, your-data-stays-yours, footer — the dominant treatment across the page |
| 1 — Hairline border | 1px solid `{colors.hairline}` | Pricing cards, FAQ row dividers, terminal mockup card |
| 2 — Inverted dark | `{colors.surface-dark}` fill | Dark "Max" pricing card and dark CTA strip — the system's only "elevated" surfaces use color, not shadow |

The system has no drop-shadow elevation at all. Nothing lifts, nothing floats, nothing layers. The only depth cue beyond hairline borders is the single dark surface used on the highest-tier pricing card to draw attention to it.

### Decorative Depth
The site has effectively zero decorative depth in the traditional sense. The "depth" comes entirely from two recurring devices:
- **The hand-drawn llama mascot** — appearing once at the top of the hero, once at the top of each pricing card, and once next to the lock icon in the "Your data stays yours" section. It is the only illustration in the system.
- **A single line-drawn lock icon** — used in the data-privacy section. Stroke-only, no fill, drawn in `{colors.ink}`.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Nav, footer, FAQ row dividers — flat structural lines |
| `{rounded.sm}` | 6px | Inline code chips, command tags |
| `{rounded.md}` | 8px | Rare medium-radius surfaces (e.g., dropdown panels) |
| `{rounded.lg}` | 12px | Pricing cards, terminal mockup card |
| `{rounded.full}` | 9999px | Every button, every pill input, install-snippet pill, search pill, traffic-light dots |

The dominant shape vocabulary is just two values: pills (`{rounded.full}`) for everything interactive and 12px (`{rounded.lg}`) for the few cards in the system. There are no medium-radius "soft cards" — surfaces are either pills or rectangles with corners large enough to read as deliberately soft.

### Photography Geometry
There is no photography. The only image-like elements are:
- **The llama mascot** — a hand-drawn line illustration, ~80–120px on the hero, ~32–48px when it appears as a pricing-card eyebrow icon.
- **The lock icon** — single stroke line drawing in the privacy section.
- **macOS traffic-light dots** — three filled circles at 12px (`{rounded.full}`) inside the terminal mockup card.

## Components

> **Extraction note.** The captured surfaces yielded Default, Active/Pressed and Disabled only; hover was never documented, by system policy. The state matrix below fills the rest in as **prescribed** behaviour — derived from this file's own tokens, not measured from the live site — and says plainly where a state genuinely does not exist on this brand.

### State matrix

Extracted states are marked (E); prescribed states are marked (P); `n/a` means the component genuinely has no such state on these surfaces.

| Component | default | hover | focus-visible | active/pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | (E) `{colors.primary}` fill | (P) fill to `{colors.ink-deep}`, no travel | (P) 2px `{colors.focus-ring-strong}` ring, 2px `{colors.canvas}` offset | (E) `{component.button-primary-active}` | (E) `{component.button-disabled}` | (P) label swaps to a spinner, pill width held | n/a — not a toggle | n/a — no validation on this surface |
| `button-secondary` | (E) `{colors.canvas}` fill, 1px `{colors.hairline-control}` | (P) border to `{colors.ink}` | (P) same ring as `button-primary` | (P) fill to `{colors.surface-soft}` | (E) `{component.button-disabled}` | (P) spinner in place of label | n/a | n/a |
| `button-pill-on-dark` | (E) `{colors.canvas}` pill on `{colors.surface-dark}` | (P) fill to `{colors.surface-soft}` | (P) ring with a `{colors.surface-dark}` offset | (P) fill to `{colors.hairline}` | (P) `{colors.hairline-strong}` fill, `{colors.charcoal}` label | (P) spinner in place of label | n/a | n/a |
| `search-pill` | (E) `{colors.surface-soft}` fill | (P) fill to `{colors.canvas}` + 1px `{colors.hairline-control}` | (E→P) `{component.search-pill-focused}` plus `{colors.focus-ring-strong}` ring | n/a — a field, not a button | (P) `{colors.surface-soft}` fill, `{colors.mute}` placeholder | (P) results row shows a `{colors.mute}` skeleton; the pill itself does not animate | (P) a chosen model chip carries `{colors.ink}` text on `{colors.surface-soft}` | n/a — search cannot fail validation |
| `text-input` | (E) `{colors.canvas}`, 1px `{colors.hairline}` (decorative weight — use `{colors.hairline-control}`) | (P) border to `{colors.hairline-strong}` | (E→P) `{component.text-input-focused}`: 1px `{colors.ink}` border + `{colors.focus-ring-strong}` ring | n/a — a field, not a button | (P) `{colors.surface-soft}` fill, `{colors.mute}` text | (P) submit control carries the spinner, never the field | n/a | **undocumented** — the captured pages have no validation state at all; see `## Known Gaps` |
| `install-snippet` | (E) `{colors.surface-soft}` pill | (P) copy icon moves from `{colors.mute}` to `{colors.ink}` | (P) ring on the copy control only | (P) copy icon at `{colors.charcoal}` | n/a | (P) copy icon swaps to a `✓` at `{colors.ink}` for `{motion.duration-slow}`, opacity only | n/a | n/a |
| `faq-row` | (E) always expanded | n/a | (P) ring on the inline link only | n/a | n/a | n/a | n/a | n/a — this component genuinely has one state; it never collapses |
| `link-inline` / `link-mute` | (E) underlined | (P) underline thickens, colour held | (P) ring around the text box, 2px offset | (P) `{colors.charcoal}` | n/a | n/a | n/a | n/a |
| `primary-nav` | (E) `{colors.canvas}` bar | (P) link to `{colors.body}` | (P) ring per link | (P) link to `{colors.ink}` | n/a | n/a | (P) current-page link at `{typography.body-sm-strong}` `{colors.ink}` | n/a |
| `terminal-card` / `pricing-card` / `cta-strip-dark` | (E) static | n/a — not interactive | n/a | n/a | n/a | n/a | n/a | n/a — these three are presentational surfaces with a single state |

### Buttons

**`button-primary`** — the universal Ollama CTA
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button-md}`, padding `8px 20px`, height `36px`, rounded `{rounded.full}`.
- Used for "Download" (top nav), "Sign in" (top nav, paired with Download), "Create account", "Get Pro", "Get Max" — every primary action in the system.
- Pressed state lives in `button-primary-active` — background drops to `{colors.ink-deep}`.

**`button-secondary`** — outline alternative on light canvas
- Background `{colors.canvas}`, text `{colors.ink}`, 1px solid `{colors.hairline-strong}` as extracted (1.48:1 — substitute `{colors.hairline-control}`, since this outline is the whole button), type `{typography.button-md}`, padding `8px 20px`, height `36px`, rounded `{rounded.full}`.
- Used as a secondary affordance — e.g., the "Sign in" pill in the top nav when paired with the black "Download" pill, "See more apps →" arrow link in compact form.

**`button-pill-on-dark`** — white pill on dark surface
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.button-md}`, rounded `{rounded.full}`.
- Sits inside the dark "Max" pricing card as the "Get Max" CTA — inverts the standard primary so the dark card itself becomes the visual anchor and the white pill reads as the CTA.

**`button-disabled`**
- Background `{colors.surface-soft}`, text `{colors.mute}`, rounded `{rounded.full}` — flat soft gray.

### Inputs & Forms

**`search-pill`** + **`search-pill-focused`**
- Default: background `{colors.surface-soft}`, text `{colors.ink}`, type `{typography.body-sm}`, padding `8px 16px`, height `36px`, rounded `{rounded.full}`. Anchored in the center of the primary nav with a small magnifier icon prefix and "Search models" placeholder.
- Focused: background flips to `{colors.canvas}` and the browser-default `{colors.focus-ring}` translucent blue ring appears. That extracted ring measures 1.85:1 over the canvas; draw `{colors.focus-ring-strong}` at 2px with a 2px offset instead.

**`text-input`** + **`text-input-focused`**
- Default: background `{colors.canvas}`, 1px solid `{colors.hairline}` as extracted — but this hairline is the field's only boundary, so substitute `{colors.hairline-control}` where the input must be findable; type `{typography.body-md}`, padding `8px 16px`, height `40px`, rounded `{rounded.full}`.
- Focused: 1px ink border + browser-default focus ring; prescribe `{colors.focus-ring-strong}` at 2px/2px offset in its place.

**`install-snippet`** — the signature install pill
- Background `{colors.surface-soft}`, text `{colors.ink}` rendered in `{typography.code-md}`, padding `12px 20px`, height `48px`, rounded `{rounded.full}`.
- Contains the literal `curl -fsSL https://ollama.com/install.sh | sh` install command with a small copy-icon at the right edge. Sits directly below the hero headline as the page's most prominent "CTA."

**`command-tag`** — small inline command chip
- Background `{colors.surface-soft}`, text `{colors.ink}` in `{typography.code-sm}`, padding `6px 12px`, rounded `{rounded.full}`.
- Used inside the "Automate your work" section for the `ollama launch openclaw` example chip and similar inline-command demos.

### Cards & Containers

**`terminal-card`** — the home page's only "product preview"
- Container: background `{colors.canvas}`, 1px solid `{colors.hairline}`, padding `{spacing.lg}` (16px), rounded `{rounded.lg}`.
- Header: three `{component.terminal-traffic-lights}` dots (red/yellow/green at 12px) anchored to the top-left of the card.
- Body: terminal output rendered in `{typography.code-sm}` with comments in `{colors.mute}` and active commands in `{colors.ink}`.

**`terminal-traffic-lights`**
- Three 12px filled circles at `{rounded.full}`: `{colors.terminal-red}`, `{colors.terminal-yellow}`, `{colors.terminal-green}`. Sits as a row of three with `{spacing.xs}` gaps between dots inside the terminal card header.

**`pricing-card`** — Free / Pro tiers
- Container: background `{colors.canvas}`, 1px solid `{colors.hairline}`, padding `{spacing.xxl}` (32px), rounded `{rounded.lg}`.
- Layout: small llama mascot icon (~32px) at top, tier name in `{typography.heading-md}`, one-line tier description, large price in `{typography.display-lg}` (`$0` / `$20`), single `{component.button-primary}` CTA, divider, `{typography.body-sm-strong}` "Everything in Free, plus:" header, list of `{component.feature-bullet}` rows.

**`pricing-card-dark`** — Max tier (inverted)
- Identical layout to `pricing-card` but with `{colors.surface-dark}` background, `{colors.on-dark}` text, `{colors.on-dark-mute}` secondary text, and `{component.button-pill-on-dark}` CTA. The inversion is the system's single "look here" cue.

**`feature-bullet`** — pricing card list item
- Inline `✓` checkmark at `{colors.ink}` followed by `{typography.body-sm}` text in `{colors.charcoal}`. No background, no border, just stacked rows with `{spacing.sm}` between them.

**`faq-row`** — `/pricing` FAQ entry
- Container: background `{colors.canvas}`, padding `16px 0`, 1px bottom border `{colors.hairline}`.
- Question: `{typography.heading-sm}` (18px / 500) in `{colors.ink}`.
- Answer: `{typography.body-md}` (16px / 400) in `{colors.body}`, sitting directly below the question with `{spacing.xs}` gap. Always expanded — no accordion collapse.

**`cta-strip-dark`** — rare dark CTA band
- Background `{colors.surface-dark}`, text `{colors.on-dark}` in `{typography.heading-lg}`, padding `24px 32px`, rounded `{rounded.lg}`. Used sparingly between sections.

### Inline

**`link-inline`** — body-prose anchor link
- `{colors.ink}` text with underline. Default decoration is `text-decoration: underline`.

**`link-mute`** — secondary anchor in long-form prose
- `{colors.body}` text with underline appearing on default — used in FAQ answers ("see [hello@ollama.com](mailto:)") and footer.

### Navigation

**`primary-nav`**
- Background `{colors.canvas}`, text `{colors.ink}`, height 56px, type `{typography.body-sm-strong}`, rounded `{rounded.none}`.
- Layout (desktop): llama icon (left) followed by "Models · Docs · Pricing" text links, centered `{component.search-pill}`, and a right cluster of "Sign in" + black `{component.button-primary}` "Download".

**Top Nav (Mobile)**
- Llama icon at left, hamburger drawer trigger at right. Search pill expands to full-width when triggered. The drawer lists "Models · Docs · Pricing · Sign in · Download" stacked vertically with `{spacing.lg}` row gaps.

### Footer

**`footer-section`**
- Background `{colors.canvas}`, 1px top border `{colors.hairline}`, padding `32px 24px`, type `{typography.caption-sm}` `{colors.body}`.
- Single horizontal row of small links: "Download · Blog · Docs · GitHub · Discord · X · Contact · Privacy · Terms" + a "© 2026 Ollama" copyright at the right edge. Wraps to two rows on narrow screens.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or transition was extracted from ollama.com; every value below comes from the **Crisp** profile in `theme-audit/SPEC.md`, chosen because this is a developer-tool identity whose whole voice is a terminal and a README. Nothing here should be read as an observed fact about the site.

Crisp fits Ollama for reasons the file itself already states: the page is a documentation surface with no hero choreography, no gradients and no photography, and its signature element is a `curl` command. A state change should read as instant, the way a key press in a terminal does. Durations sit at `{motion.duration-base}` (150ms) and below for everything a person touches, and no entrance is choreographed.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, nav link, copy icon) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` only; colour tokens swap discretely, and no geometry is animated | Unchanged — the fade is already at or under `{motion.duration-reduced}` |
| Press (`{component.button-primary}` → `{component.button-primary-active}`) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`; the fill step to `{colors.ink-deep}` is discrete. No scale — pills do not squash in this system | Discrete fill step only, no fade |
| Focus (`{colors.focus-ring-strong}` ring appears) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring | Ring appears with no transition — a focus indicator never waits |
| Page / route transition (`/` ↔ `/pricing`) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` on the content column; no slide, no travel | Opacity only at `{motion.duration-reduced}` |
| Modal / drawer (mobile nav drawer) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `transform: translateX()` plus `opacity` on the scrim | Travel removed; scrim and panel fade at `{motion.duration-reduced}` |
| Dropdown (search results, account menu) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` plus `transform: translateY(-2px → 0)` — 2px, which is `{spacing.xxs}`, not a reveal | Travel removed; opacity only at `{motion.duration-reduced}` |
| Toast ("Copied", "Download started") | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` plus `transform: translateY(4px → 0)` | Travel removed; opacity only at `{motion.duration-reduced}` |
| List enter (pricing cards, FAQ rows, search results) | `{motion.duration-fast}` per item, `{motion.stagger-step}` (20ms) between items | `{motion.ease-enter}` | `opacity`; stagger caps at 5 items so a FAQ wall never crawls in | Stagger and travel removed; the list renders at full opacity immediately |
| List exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity`, no stagger | Items are removed with no transition |
| Loading (copy-confirm, submit spinner, search skeleton) | Spinner: 800ms linear loop. Confirm tick: `{motion.duration-slow}` | `{motion.ease-standard}` for the tick; linear for the spinner | `transform: rotate()` on the spinner, `opacity` on the tick and on the `{colors.mute}` skeleton | Spinner is replaced by a static `{typography.body-sm}` "Loading…" label in `{colors.body}`; no rotation, no pulse |

### Rules

- Only `transform` and `opacity` are animated. Never `width`, `height`, `top`, `left` or `margin` — the install-snippet pill reflows its `curl` text at narrow widths and must not animate that reflow.
- Every exit is shorter than its matching entrance (drawer 150 → 100ms, dropdown 100 → 60ms, toast 150 → 100ms).
- Nothing animates on first paint. The hero headline, the install snippet and the llama render immediately; this is a documentation page and the content is the product.
- The only infinite animation in the system is the loading spinner. There is no brand ambience — this system has no gradients to drift and no imagery to pan, and adding any would contradict `## Do's and Don'ts`.
- Durations deviate from the Crisp block nowhere. The one bare value is the 800ms spinner loop, which is a loop period rather than a transition duration and so has no token in the profile.

### `@media (prefers-reduced-motion: reduce)`

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. The drawer, dropdown and toast
     arrive in place; no translate, no rotate except where noted below. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (100ms). */
  /* Removed: the {motion.stagger-step} list cascade — lists render at once. */
  /* Replaced: the loading spinner's rotate() becomes a static text label. */
  /* Unchanged: the {colors.focus-ring-strong} focus ring, which is a
     visibility affordance and is never suppressed. */
}
```

What remains under reduce: opacity fades at `{motion.duration-reduced}` (100ms), discrete colour steps, and the focus ring. What is removed: every `translate`, the dropdown's 2px lift, the toast's 4px rise, the drawer's slide, the list stagger, and the spinner's rotation.

## Accessibility

Every ratio below was computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. `{colors.focus-ring}` and `{colors.on-dark-mute}` are alpha values, so each is composited over the ground it is actually drawn on before measuring.

### Measured contrast — key pairs

| Pair | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#000000` on `{colors.canvas}` | 21.0:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-soft}` | 20.12:1 | 4.5:1 | Pass |
| `{colors.charcoal}` `#525252` on `{colors.canvas}` | 7.81:1 | 4.5:1 | Pass |
| `{colors.body}` `#737373` on `{colors.canvas}` | 4.74:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.surface-soft}` | 4.54:1 | 4.5:1 | Pass — by 0.04, so `{colors.surface-soft}` is the darkest ground this ink may sit on |
| `{colors.mute}` `#a3a3a3` on `{colors.canvas}` | 2.52:1 | 4.5:1 | **Fail — real brand failure, see below** |
| `{colors.on-primary}` on `{colors.primary}` | 21.0:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.surface-dark}` | 17.93:1 | 4.5:1 | Pass |
| `{colors.on-dark-mute}` (composites to `#b3b3b3`) on `{colors.surface-dark}` | 8.55:1 | 4.5:1 | Pass |
| `{colors.hairline}` `#e5e5e5` on `{colors.canvas}` | 1.26:1 | 3.0:1 | **Fail — extracted and frozen** |
| `{colors.hairline}` on `{colors.surface-soft}` | 1.21:1 | 3.0:1 | **Fail — extracted and frozen** |
| `{colors.hairline-strong}` `#d4d4d4` on `{colors.canvas}` | 1.48:1 | 3.0:1 | **Fail — extracted and frozen** |
| `{colors.hairline-strong}` on `{colors.surface-soft}` | 1.42:1 | 3.0:1 | **Fail — extracted and frozen** |
| `{colors.hairline-control}` `#8f8f8f` on `{colors.canvas}` | 3.23:1 | 3.0:1 | Pass — prescribed |
| `{colors.hairline-control}` on `{colors.surface-soft}` | 3.10:1 | 3.0:1 | Pass — prescribed |

### Where the real brand fails AA

Three extracted tones do not meet their threshold, and none of them has been altered here:

- **Both hairlines fail the 3:1 non-text threshold by a wide margin** — `{colors.hairline}` at 1.26:1 and `{colors.hairline-strong}` at 1.48:1 on `{colors.canvas}`, 1.21:1 and 1.42:1 on `{colors.surface-soft}`. On a card edge or an FAQ divider that is defensible: the boundary is decoration and the content inside it is what carries meaning. It is **not** defensible on `{component.text-input}`, `{component.button-secondary}` or a focused `{component.search-pill}`, where the hairline is the only thing that says a control is there. Prescribed `{colors.hairline-control}` (3.23:1) exists for exactly those cases; the extracted tones keep their decorative job.
- **`{colors.mute}` `#a3a3a3` fails body-text contrast at 2.52:1 on `{colors.canvas}`.** The file documents it for caption text, terminal comments and lowest-emphasis utility text. At 2.52:1 it does not reach 4.5:1 at any size, and it does not reach the 3:1 large-text allowance either, so there is no size at which it is compliant as text. Use `{colors.body}` (4.74:1) for any caption a reader must actually read, and keep `{colors.mute}` for the simulated comment lines inside `{component.terminal-card}`, which are decorative screenshot content rather than page copy.
- **The extracted focus ring is not a focus indicator.** `{colors.focus-ring}` at 50% alpha composites to `#9dc0fa` over `{colors.canvas}` and measures 1.85:1, and 1.77:1 over `{colors.surface-soft}`. Over `{colors.surface-dark}` the same alpha composites to `#294c86` at 2.11:1, so it fails on the dark card too. Leaving the browser default in place is the most common accessibility defect on a site this minimal, and it is a genuine failure of the live design.

### Focus ring visibility, per surface this file defines

`{colors.focus-ring-strong}` `#3b82f6` is prescribed, drawn at 2px with a 2px offset in the underlying surface colour, so what it is measured against is the surface behind the control rather than the control's own fill.

| Surface the ring is drawn on | Ratio against `{colors.focus-ring-strong}` | Verdict |
|---|---|---|
| `{colors.canvas}` `#ffffff` | 3.68:1 | Pass |
| `{colors.surface-card}` `#ffffff` | 3.68:1 | Pass |
| `{colors.surface-soft}` `#fafafa` | 3.52:1 | Pass |
| `{colors.surface-dark}` `#171717` | 4.87:1 | Pass |
| `{colors.ink-deep}` `#090909` | 5.41:1 | Pass |

One ring covers all five because this file has three surface polarities rather than a clean light/dark pair, and a mid-luminance blue clears 3:1 against every one of them. A `focus-on-dark` counterpart would be redundant here and is deliberately not defined.

The ring is never drawn *on* `{colors.primary}`: a pure-black pill and a paper-white canvas cannot both be cleared by one ring value, which is why the 2px offset is mandatory rather than stylistic. Inside `{component.pricing-card-dark}`, the offset is `{colors.surface-dark}`.

### Tap targets

Not measurable from a document — these are the **documented** heights, not rendered measurements, and nothing here has been verified on a running page:

- `{component.button-primary}`, `{component.button-secondary}`, `{component.search-pill}`: 36px documented height. Meets WCAG 2.2 AA 2.5.8 (24×24 CSS px). Falls short of AAA 2.5.5 (44×44) on the vertical axis — horizontal padding does not fix a height.
- `{component.text-input}`: 40px documented height. Same verdict.
- `{component.install-snippet}`: 48px documented height, and its copy icon is the only control inside it; the icon's own hit area is not documented anywhere in the captured surfaces.
- Footer links at `{typography.caption-sm}` (12px) with ~8px vertical padding give a documented row of roughly 32px. That clears 24×24 but is the tightest target in the system.

### Reduced motion

See `## Motion & Animation`. Under `prefers-reduced-motion: reduce`, all travel, scale and rotation are removed, opacity fades are capped at `{motion.duration-reduced}` (100ms), the list stagger is dropped, the loading spinner becomes a static text label, and the focus ring is never suppressed. This system has no brand ambience to freeze.

### Other notes

- Colour is never the sole carrier of meaning: the system has no success/warning/error palette at all, and the three `{colors.terminal-red}` / `{colors.terminal-yellow}` / `{colors.terminal-green}` dots are a macOS window-chrome likeness inside a screenshot, not status indicators.
- `{component.button-disabled}` pairs `{colors.mute}` on `{colors.surface-soft}` at 2.42:1. WCAG sets no contrast requirement on disabled controls, so this is recorded rather than flagged.
- Keyboard order, screen-reader labelling, heading structure and `alt` text for the llama mascot are not documented in the captured surfaces. See `## Known Gaps`.

## Do's and Don'ts

### Do
- Treat the page like a Markdown document: single reading column, plenty of `{spacing.section}` air between sections, no decorative dividers.
- Use `{component.button-primary}` (black pill) for every primary action. There is no green, no blue, no brand-tinted CTA.
- Default to `{rounded.full}` for any interactive element. Cards get `{rounded.lg}` (12px) and that is the only exception.
- Use `{typography.display-xl}` SF Pro Rounded for the hero headline and `{typography.body-md}` system sans for everything else. Avoid intermediate display sizes.
- Reserve `{component.pricing-card-dark}` (the inverted dark surface) for exactly one "look here" moment per page — never use it twice.
- Render install commands and CLI examples inside `{component.install-snippet}` or `{component.terminal-card}` with `{typography.code-md}` / `{typography.code-sm}`. Code is a first-class component.
- Keep the llama mascot the only illustration in the system. It is the brand.
- Keep motion at `{motion.duration-base}` (150ms) or under for anything a person touches, and animate `transform` and `opacity` only. A state change here should read as instant, like a terminal.
- Draw `{colors.focus-ring-strong}` at 2px with a 2px offset for every keyboard focus state, on light and dark surfaces alike.
- Use `{colors.hairline-control}` wherever a 1px rule is the *only* boundary of a control. Keep `{colors.hairline}` for card edges and dividers.

### Don't
- Don't introduce gradients, drop shadows, or atmospheric backgrounds. The canvas is pure `{colors.canvas}`.
- Don't add brand colors. The system is `{colors.primary}` (black) on `{colors.canvas}` (white) with `{colors.body}` (gray) text. That is it.
- Don't soften pills or sharpen cards — pills stay `{rounded.full}`, cards stay `{rounded.lg}`. Don't introduce `{rounded.md}` for buttons or `{rounded.full}` for cards.
- Don't lift cards with shadows. Use a 1px `{colors.hairline}` border or invert to `{colors.surface-dark}` — those are the only two card treatments.
- Don't replace `ui-sans-serif` with a branded display body face. The system relies on `system-ui` rendering to feel native.
- Don't fill long-form pages with marketing chrome. FAQ answers stay in `{colors.body}` body-md prose with no decorative containers.
- Don't choreograph entrances. No reveal on scroll, no staggered hero, and never animate `width`, `height`, `top`, `left` or `margin` — the install-snippet pill reflows at narrow widths and that reflow must not be animated.
- Don't ship the browser-default `{colors.focus-ring}` as the real focus indicator. At 1.85:1 over the canvas it is not visible enough to be one.
- Don't set body copy in `{colors.mute}`. At 2.52:1 it fails at every text size; use `{colors.body}`.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| desktop-large | 1280px+ | Default desktop — 720px content column, 3-up pricing grid |
| desktop | 1024px | Same layout; nav remains horizontal |
| tablet | 850px | Pricing collapses from 3-up to 2-up + 1; nav search pill compresses |
| tablet-narrow | 768px | Pricing collapses to 1-up stacked; primary nav becomes hamburger |
| mobile | 640px | Hero headline drops from `{typography.display-xl}` (36px) to ~28px; install-snippet wraps; section padding tightens |

### Touch Targets
All interactive elements sit in the 36–40px documented height range, which clears WCAG 2.2 AA 2.5.8 (24×24 CSS px) but **not** AAA 2.5.5 (44×44) — horizontal padding widens a target, it does not raise its height, and the earlier claim that it did was wrong. `{component.button-primary}` and `{component.button-secondary}` sit at 36px height with 20px horizontal padding, giving a documented area of roughly 36×80px. `{component.text-input}` sits at 40px. `{component.search-pill}` sits at 36px height with 16px padding. Footer links use `{typography.caption-sm}` (12px) but receive ~12px line-height + ~8px vertical padding for a tappable row of ~32–36px.

### Collapsing Strategy
- **Primary nav:** desktop horizontal → tablet-narrow hamburger drawer at 768px. The black "Download" CTA stays visible at all widths; it never collapses into the menu.
- **Search pill:** desktop fixed width ~360px → tablet compressed to ~240px → mobile collapses to icon-only with a full-width overlay on tap.
- **Pricing grid:** 3-up → 2+1 → 1-up stacked at 850, 768, and below. The dark "Max" card stays in its inverted treatment at every breakpoint.
- **Automate-your-work split:** desktop 50/50 → tablet stacks vertical with text above terminal mockup.
- **Hero headline:** `{typography.display-xl}` (36px) at desktop, scaling to ~28px at mobile with line-height holding at ~1.15.
- **Section spacing:** `{spacing.section}` (88px) desktop → 64px tablet → 48px mobile.
- **Install-snippet pill:** wraps `curl` text to a second line on narrow screens rather than truncating; the copy-icon stays anchored to the right edge.

### Image Behavior
The only image asset is the llama mascot (raster PNG at multiple resolutions: 16/32/48/64/180/192/512px). It is rendered at fixed pixel sizes on the hero and pricing cards rather than scaling responsively — the brand asset is treated like a logo, not a hero image.

## Iteration Guide

1. Focus on ONE component at a time. Pull its YAML entry from the front matter and verify every property resolves.
2. Reference component names and tokens directly (`{colors.primary}`, `{component.button-primary-active}`, `{rounded.full}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits — `broken-ref`, `contrast-ratio`, and `orphaned-tokens` warnings flag issues automatically.
4. Add new variants as separate component entries (`-active`, `-disabled`, `-focused`) — do not bury them inside prose.
5. Default body to `{typography.body-md}`; reach for `{typography.body-sm}` for footer/utility text; reserve `{typography.display-xl}` strictly for the page-top headline.
6. Keep `{colors.primary}` scarce per viewport — there should be at most one black pill per fold (counting nav, hero CTA, and pricing-card CTA together). The design's restraint is the design.
7. When introducing a new component, ask whether it can be expressed with the existing pill + flat-card + terminal-mockup vocabulary before adding new tokens. The system's strength is that it almost never needs new ones.

## Known Gaps

- **Mobile screenshots not captured** — responsive behavior synthesizes Ollama's known mobile pattern (hamburger drawer, 1-up pricing stack, install-snippet wrap) from desktop evidence and the extracted breakpoint stack.
- **Hover states not documented** by system policy. The `### State matrix` entries marked (P) are prescribed from this file's own tokens, not extracted; hover, loading and selected behaviour has never been observed on the live site.
- **All motion is prescribed.** No duration, easing or transition was extracted from ollama.com. The `## Motion & Animation` section applies the Crisp profile wholesale and says so in its first line.
- **`{colors.hairline-control}` and `{colors.focus-ring-strong}` are prescribed tokens**, added to carry jobs the extracted palette cannot do at 3:1. They are not Ollama values. `{colors.focus-ring-strong}` is the extracted ring's own blue with the alpha removed; `{colors.hairline-control}` is a neutral grey between `{colors.mute}` and `{colors.body}` and has no counterpart on the live site.
- **Validation and error states are entirely absent** from the captured surfaces — no form errors, no destructive confirmations, no banners. The state matrix records this as undocumented rather than inventing one.
- **Keyboard order, ARIA labelling, heading structure and mascot `alt` text** were not captured and are not described here.
- **Form field styling** beyond search and install-snippet is not present in the captured surfaces — there is no visible long-form form on the home or pricing pages.
- **Authenticated chrome** (account dropdown, billing settings, model dashboard) not in the captured pages.
- **Models / Docs pages** not in the captured set — those surfaces likely add a sidebar and a docs typography tier that this document does not describe.
