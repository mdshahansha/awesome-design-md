---
version: alpha
name: OpenCode-design-analysis
description: |
  A terminal-native marketing system rendered entirely in Berkeley Mono — every word on the page, from the hero headline down to the footer fine print, is monospaced. The page itself reads like a manpage or a static-site README: warm cream canvas (`#fdfcfc`), nearly-black ink (`#201d1d`), 4px-radius rectangles for the few interactive elements, and bracketed `[+]`/`[-]` ASCII markers used as bullets. The brand's only "visual moment" is a single dark hero card that mocks up the OpenCode TUI itself — black background, monospaced terminal output, ASCII pipe characters, and a wordmark rendered as block-pixel ASCII. Every section sits as a hairline-bordered text block on the cream canvas with no shadows, no gradients, no decorative imagery, and no non-monospaced character anywhere in the system.

colors:
  primary: "#201d1d"
  on-primary: "#fdfcfc"
  ink: "#201d1d"
  ink-deep: "#0f0000"
  charcoal: "#302c2c"
  body: "#424245"
  mute: "#646262"
  stone: "#6e6e73"
  ash: "#9a9898"
  canvas: "#fdfcfc"
  surface-soft: "#f8f7f7"
  surface-card: "#f1eeee"
  surface-dark: "#201d1d"
  surface-dark-elevated: "#302c2c"
  hairline: "rgba(15,0,0,0.12)"
  hairline-strong: "#646262"
  on-dark: "#fdfcfc"
  on-dark-mute: "#9a9898"
  focus: "#201d1d"
  focus-on-dark: "#fdfcfc"
  accent: "#007aff"
  accent-hover: "#0056b3"
  accent-active: "#004085"
  warning: "#ff9f0a"
  warning-hover: "#cc7f08"
  warning-active: "#995f06"
  danger: "#ff3b30"
  danger-hover: "#d70015"
  danger-active: "#a50011"
  success: "#30d158"

typography:
  display-xl:
    fontFamily: Berkeley Mono
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  heading-md:
    fontFamily: Berkeley Mono
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: Berkeley Mono
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-strong:
    fontFamily: Berkeley Mono
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  body-tight:
    fontFamily: Berkeley Mono
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  link-md:
    fontFamily: Berkeley Mono
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: Berkeley Mono
    fontSize: 16px
    fontWeight: 500
    lineHeight: 2
    letterSpacing: 0
  caption-md:
    fontFamily: Berkeley Mono
    fontSize: 14px
    fontWeight: 400
    lineHeight: 2
    letterSpacing: 0

rounded:
  none: 0px
  sm: 4px
  full: 9999px

spacing:
  xxs: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
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
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 4px 20px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 4px 20px
  button-tab:
    backgroundColor: "transparent"
    textColor: "{colors.mute}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  button-tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-disabled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ash}"
    rounded: "{rounded.sm}"
  badge-news:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  textarea:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px
  install-snippet:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  hero-tui-mockup:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 64px 32px
  tui-prompt-row:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  list-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 0px
  faq-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 0px
  testimonial-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 16px 20px
  chart-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.none}"
    padding: 16px
  primary-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
    height: 56px
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.none}"
    padding: 32px 0px
  link-inline:
    textColor: "{colors.ink}"
    typography: "{typography.link-md}"
  badge-section-label:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.heading-md}"
    rounded: "{rounded.none}"
---

## Overview

OpenCode's marketing site is rendered entirely in Berkeley Mono — every word on the page, from the 38px hero headline down to the 14px footer fine print, sits in the same monospaced face. The visual identity comes from that single typographic decision: the page reads like a manpage or a static-site README, complete with bracketed `[+]` / `[-]` / `[x]` ASCII markers used in place of icons or bullets, and a wordmark rendered as block-pixel ASCII art at the top of the nav. There is no sans-serif anywhere, no display face, no italics, no decorative ornament — the system is one font and one weight away from being a 1990s `whatis` page rendered at modern resolutions.

The chrome is austere: warm cream canvas (`{colors.canvas}` — `#fdfcfc` with a faint blush), nearly-black ink (`{colors.ink}` — `#201d1d`), and a 4-tier neutral gray ladder for body, metadata, and disabled text. Cards don't exist as raised surfaces — sections are just hairline-bordered text blocks (`{colors.hairline}` 1px) sitting directly on the canvas with `{spacing.section}` (96px) air between them. The single "visual" moment in the entire system is a full-bleed dark hero card (`{colors.surface-dark}` — true near-black) that mocks up the OpenCode TUI itself: a terminal frame with `tab` / `ctrl-p` keybinding hints, a "Build" command line, and the OpenCode wordmark rendered as a pixel-block ASCII title.

The semantic palette is unusual for a brand-marketing site: it ships the full Apple Human Interface Guidelines accent ramp — `{colors.accent}` (Apple Blue `#007aff`), `{colors.danger}` (`#ff3b30`), `{colors.warning}` (`#ff9f0a`), `{colors.success}` (`#30d158`) plus their hover/active deepenings — even though the marketing surfaces themselves only use these colors in the dark hero TUI mockup as syntax-highlight stand-ins. The wider palette belongs to the in-product TUI; the marketing pages mostly stay in monochrome.

**Key Characteristics:**
- 100% Berkeley Mono typography across every text role — no sans-serif fallback anywhere in the chrome
- Warm cream `{colors.canvas}` (#fdfcfc) as the only body background — no surface alternation across sections
- Single dark surface (`{colors.surface-dark}` — #201d1d) reserved exclusively for the hero TUI mockup
- 4px radius (`{rounded.sm}`) on every interactive element; sections themselves are sharp rectangles bordered in 1px hairline
- ASCII bracket markers (`[+]`, `[-]`, `[x]`) used as bullet glyphs in feature lists and FAQ rows
- Block-pixel ASCII wordmark in the primary nav and inside the hero TUI — the brand identity is its own ASCII art
- 96px `{spacing.section}` rhythm between every section, with no decorative dividers; only thin 1px `{colors.hairline}` rules separate content blocks

## Colors

> **Source pages:** `/` (home), `/zen`, `/enterprise`. The chrome palette is identical across all three.

### Brand & Accent
- **Ink** (`{colors.primary}` / `{colors.ink}` — `#201d1d`): the brand's only "color." Headlines, body text, primary CTA fill, nav links, and every solid icon. Treats nearly-black as the brand color rather than pure black to keep type readable on the warm cream canvas.
- **Ink Deep** (`{colors.ink-deep}` — `#0f0000`): pressed-state for the primary CTA. Carries a faint red undertone matching the canvas's warm cast.
- **Cream** (`{colors.canvas}` — `#fdfcfc`): the brand's signature warm white. Used for every page body, every card surface, the on-primary text color, and the ASCII wordmark fill on dark.

### Surface
- **Canvas Cream** (`{colors.canvas}` — `#fdfcfc`): every page body, every card.
- **Soft Surface** (`{colors.surface-soft}` — `#f8f7f7`): text-input default background, testimonial row fill, alternating row tint.
- **Surface Card** (`{colors.surface-card}` — `#f1eeee`): install-snippet pill, disabled button fill, slightly-elevated section row.
- **Surface Dark** (`{colors.surface-dark}` — `#201d1d`): the hero TUI mockup background and the dark CTA pill on the home page. Identical to `{colors.ink}` — the brand uses one near-black for both text and dark surfaces.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — `#302c2c`): the prompt-row inside the hero TUI mockup, one notch lighter than the dark surface itself.
- **Hairline** (`{colors.hairline}` — `rgba(15,0,0,0.12)`): 1px section divider. The translucent warm tint matches the cream canvas's undertone.
- **Hairline Strong** (`{colors.hairline-strong}` — `#646262`): tab strip's bottom rule and stronger inline divider.

### Text
- **Ink** (`{colors.ink}` — `#201d1d`): headlines, body text, primary nav links, button text on light surfaces.
- **Charcoal** (`{colors.charcoal}` — `#302c2c`): subtly softer body where pure ink is too heavy.
- **Body** (`{colors.body}` — `#424245`): default paragraph text and FAQ answers.
- **Mute** (`{colors.mute}` — `#646262`): tab labels (default state), metadata, footer link text, in-list secondary annotations.
- **Stone** (`{colors.stone}` — `#6e6e73`): least-emphasis utility text, breadcrumb separators.
- **Ash** (`{colors.ash}` — `#9a9898`): disabled text and secondary annotation in dark TUI mockup, also TUI mockup secondary color.

Note on naming: `{colors.mute}`, `{colors.stone}` and `{colors.ash}` are this system's secondary/muted text ladder. The brand names them as tones, not as a `text-dim` role; nothing in the palette is called `muted` or `text-dim`.

### Focus

**Prescribed, not extracted.** The captured surfaces document a focused text input as a border swap (`{colors.ink}` 1px, no halo) and nothing else; no focus ring was observed on buttons, tabs, or links. The ring below is specified to match the brand's rule that it has no accent colour on marketing chrome — Apple Blue belongs to the in-product TUI, so a blue ring would contradict the identity. Per the monochrome case, the ring is the brand's own ink on light grounds and the brand's own cream on the dark TUI surface, each with a mandatory 2px offset of the opposite polarity so the ring never touches the control fill.

- **Focus** (`{colors.focus}` — `#201d1d`, identical to `{colors.ink}`): the default ring, drawn as a 2px solid outline with a 2px offset in `{colors.canvas}`, on `{colors.canvas}`, `{colors.surface-soft}` and `{colors.surface-card}`. Measured against the ground it is drawn on: 16.34:1 on `{colors.canvas}`, 15.65:1 on `{colors.surface-soft}`, 14.51:1 on `{colors.surface-card}`.
- **Focus on Dark** (`{colors.focus-on-dark}` — `#fdfcfc`, identical to `{colors.canvas}`): the counterpart ring for the dark TUI surfaces, 2px solid with a 2px offset in `{colors.surface-dark}`. Measured: 16.34:1 on `{colors.surface-dark}`, 13.47:1 on `{colors.surface-dark-elevated}`, 20.1:1 on `{colors.ink-deep}` (the pressed primary CTA fill).
- The ring is drawn **outside** its control with the stated 2px offset, so it is judged against the surface behind the control rather than the control's own fill — which is what WCAG 2.2 Focus Appearance asks for.

### Semantic
The full Apple Human Interface Guidelines semantic ramp ships with the system. On marketing pages these colors appear primarily inside the hero TUI mockup as syntax-highlight stand-ins; in the in-product TUI they carry their conventional meaning.

- **Accent** (`{colors.accent}` — `#007aff`): primary informational signal, in-product link color, TUI command highlight.
- **Accent Hover** (`{colors.accent-hover}` — `#0056b3`): pressed informational link.
- **Accent Active** (`{colors.accent-active}` — `#004085`): deeply-pressed informational state.
- **Danger** (`{colors.danger}` — `#ff3b30`): destructive confirmation, error state.
- **Danger Hover** (`{colors.danger-hover}` — `#d70015`): pressed destructive.
- **Danger Active** (`{colors.danger-active}` — `#a50011`): deeply-pressed destructive.
- **Warning** (`{colors.warning}` — `#ff9f0a`): caution callouts.
- **Warning Hover** (`{colors.warning-hover}` — `#cc7f08`): pressed caution.
- **Warning Active** (`{colors.warning-active}` — `#995f06`): deeply-pressed caution.
- **Success** (`{colors.success}` — `#30d158`): positive confirmation, in-TUI success indicator.

## Typography

### Font Family
**Berkeley Mono** is the proprietary monospaced face used across every text role in the system. It carries weights 400 (regular), 500 (medium), and 700 (bold) and falls back through a long monospace stack — IBM Plex Mono → ui-monospace → SFMono-Regular → Menlo → Monaco → Consolas → Liberation Mono → Courier New.

The single-font decision is the brand. There is no display face, no body sans, no italic alternative, and no fallback to a proportional font anywhere — even the legal copyright row uses Berkeley Mono at 14px. This is the most aggressive typographic restraint of any site in the marketing-tools category: OpenCode's identity is "the marketing page is a man page."

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 38px | 700 | 1.5 | 0 | Hero headline ("The open source AI coding agent") |
| `{typography.heading-md}` | 16px | 700 | 1.5 | 0 | Section label ("What is OpenCode?", "FAQ", "Built for privacy first") |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Body copy, paragraph text, list-row text, install-snippet code |
| `{typography.body-strong}` | 16px | 500 | 1.5 | 0 | Inline emphasis, primary nav link, tab-label active |
| `{typography.body-tight}` | 16px | 500 | 1 | 0 | Compact label rendered without breathing room |
| `{typography.link-md}` | 16px | 400 | 1.5 | 0 | Inline anchor link in body prose |
| `{typography.button-md}` | 16px | 500 | 2 | 0 | Every button label across the system |
| `{typography.caption-md}` | 14px | 400 | 2 | 0 | Footer link text, badge label, copyright row, chart caption |

### Principles
The hierarchy is built almost entirely from size and weight contrast on a single face. The display headline (38px / 700) and the heading-md label (16px / 700) share a weight; the difference is just size. Body and link share size, weight, and line-height — only context distinguishes them. Buttons get a deliberately tall line-height (2.0) so labels feel calmly spaced inside the 4px-radius rectangle.

### Note on Font Substitutes
Berkeley Mono is a paid commercial font. Open-source substitutes that approximate its metrics within ~3% at body sizes:
- **JetBrains Mono** — closest match for stroke contrast and x-height; pair at weights 400 / 500 / 700.
- **IBM Plex Mono** — official secondary fallback in the documented font stack; slightly more open counters but matches line-height behavior.
- **Geist Mono** — modern alternative with similar geometric construction.

When substituting, line-height behavior is preserved by keeping `lineHeight: 1.5` for body and `lineHeight: 2` for buttons — adjusting weight is rarely needed.

## Layout

### Spacing System
- **Base unit:** 8px (with finer 1/2/4px steps available for tight inline gaps).
- **Tokens (front matter):** `{spacing.xxs}` (1px) · `{spacing.xs}` (4px) · `{spacing.sm}` (8px) · `{spacing.md}` (12px) · `{spacing.lg}` (16px) · `{spacing.xl}` (24px) · `{spacing.xxl}` (32px) · `{spacing.section}` (96px).
- **Universal section rhythm:** every page in the set uses `{spacing.section}` (96px) as the vertical gap between major content blocks. This is the largest spacing token in the system and is the dominant layout cue across the home, `/zen`, and `/enterprise` pages.
- **Section internal padding:** content rows inside a section sit at `{spacing.lg}` (16px) vertical with no horizontal padding — text starts flush at the section's left edge.

### Grid & Container
- **Max width:** ~960px content column for body sections; the dark hero TUI mockup is full-bleed within an outer ~1100px content frame.
- **Two-column split:** `/enterprise` pairs a left text block (~360px wide) with a right-aligned form column (~480px wide). The home page is single-column reading.
- **Footer:** 5-up horizontal link row (GitHub / Docs / Changelog / Discord / X) at desktop, collapsing to 2-up at tablet and 1-up at mobile.

### Whitespace Philosophy
Whitespace is structural and generous. Sections sit 96px apart with no decorative dividers between them — the `{colors.hairline}` 1px rule is the only signal of separation. Inside a section, content is left-flush against the column edge with no internal indentation; bullets use ASCII bracket prefixes (`[+]` / `[-]`) instead of indent-based layout. The result is a page that feels like a printed code listing rather than a styled marketing layout.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Default for body sections, list rows, hero text block, footer |
| 1 — Hairline rule | 1px solid `{colors.hairline}` (translucent warm tint) | **Decorative only** — section dividers between 96px-separated blocks, where the whitespace carries the separation. At 1.31:1 on both `{colors.canvas}` and `{colors.surface-soft}` this tone is below the 3:1 non-text minimum, so it must not be the sole boundary of a control |
| 2 — Hairline strong | 1px solid `{colors.hairline-strong}` | Tab strip bottom rule, in-list emphasized divider, and the accessible boundary wherever a rule has to be *seen* rather than felt — control edges, input borders, selection underlines (5.92:1 on `{colors.canvas}`) |
| 3 — Inverted dark | `{colors.surface-dark}` fill | Hero TUI mockup, dark CTA pill — the system's only "elevated" surface uses color, not shadow |

There are no drop shadows in the system. Nothing lifts, nothing floats. The only way an element registers as "above" another is the dark surface used in the hero mockup.

Elevation is therefore expressed exactly one way — a 1px rule, or a fill swap — and never by mixing shadow with border. There is no `shadow:` token group because the system documents no shadow values; the frontmatter carries none rather than inventing one. The `{colors.focus}` ring is an outline, not an elevation level: it sits outside the layer ladder above and is never used to imply depth.

### Decorative Depth
Depth comes from typography density and the single dark TUI mockup, not from CSS effects:
- **ASCII block-pixel wordmark** — the OpenCode brand name rendered as a 5-row block of monospaced character cells, used in the primary nav and as the centerpiece of the hero TUI mockup.
- **Hero TUI mockup** — full-bleed `{colors.surface-dark}` rectangle containing a faux terminal interface: ASCII wordmark, a `tui-prompt-row` showing a Build command line, and `tab switch agent` / `ctrl-p commands` keybinding hints in `{colors.ash}` at the bottom edge.
- **Chart tiles** — three thin-line ASCII charts inside the home page's "open source AI coding agent" stat block, with abstract dotted/sparse-line plots in `{colors.body}` against the cream canvas. Captions sit beneath in `{typography.caption-md}` (`Fig 1. 150K GitHub Stars`, `Fig 2. 850 Contributors`, `Fig 3. 6.5M Monthly Devs`).

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Sections, hero TUI mockup, primary nav, footer, list rows — every container that isn't a button |
| `{rounded.sm}` | 4px | Every interactive element — primary CTA, secondary CTA, text inputs, install snippet, badges, prompt rows |
| `{rounded.full}` | 9999px | Avatar circles in testimonials |

The radius vocabulary is two values: 4px for interactive elements and 0px for everything else. Avatar circles in testimonial rows are the only fully-rounded element in the system.

### Border Width Scale

| Width | Use |
|---|---|
| 1px | Every hairline, divider, section rule, input border, nav and footer rule — `{colors.hairline}` or `{colors.hairline-strong}` |
| 2px | Selection and focus only — the active tab's bottom underline, and the `{colors.focus}` ring with its 2px offset |

Two widths, and the wider one carries meaning rather than weight: 2px appears only where the system is reporting state. No 3px, no 4px, no fractional strokes.

### Photography Geometry
There is no photography. Visual elements are limited to:
- **ASCII block-pixel wordmark** in the nav and hero TUI mockup.
- **Inline ASCII charts** inside the stat-block section — abstract sparse-line and dotted plots without specific data points.
- **Avatar dots** (~32px) inside testimonial rows on `/zen` — flat colored circles in `{rounded.full}`.
- **In-product icons** (kbd, A+, ⊕, ↻, K, Z) rendered as small monospaced character glyphs, not bitmaps or SVG.

## Components

> **Extracted vs prescribed states.** The capture recorded Default, Active/Pressed and Disabled only — hover was never captured, and no focus ring was observed outside the text input's border swap. Every entry below therefore carries a `States:` line that marks which states are extracted and which are **prescribed** here (focus-visible, hover, loading, selected, error). Prescribed states follow the brand's own vocabulary: an ink/cream colour swap, never a shadow, a glow, or a size change. Timings come from `## Motion & Animation`.

### Buttons

**`button-primary`** — the universal OpenCode CTA
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button-md}`, padding `4px 20px`, height ~36px, rounded `{rounded.sm}` (4px).
- Used for "Download" (top nav), "Get started with Zen", "Send" (enterprise contact form), "Subscribe" (newsletter footer), "Read docs →".
- Pressed state lives in `button-primary-active` — background drops to `{colors.ink-deep}`.
- **States:** default (extracted) · active/pressed (extracted, `button-primary-active`) · disabled (extracted, `button-disabled`) · hover (prescribed — fill to `{colors.charcoal}`) · focus-visible (prescribed — 2px `{colors.focus}` ring at 2px offset) · loading (prescribed — label holds its box, a `[/]` → `[-]` → `[\]` → `[|]` ASCII spinner glyph replaces the leading character, opacity only) · error (prescribed — form submit failure leaves the button at default and renders the message in `{colors.danger}` beside it; the button itself has no error skin). Not selected: this control is never a selection target.

**`button-secondary`** — outlined alternative
- Background `{colors.canvas}`, text `{colors.ink}`, 1px solid `{colors.hairline-strong}` border, type `{typography.button-md}`, padding `4px 20px`, rounded `{rounded.sm}`.
- Lower-emphasis CTA — appears beside the primary fill where two actions are paired.
- **States:** default (extracted) · hover (prescribed — border to `{colors.ink}`, fill unchanged) · focus-visible (prescribed — 2px `{colors.focus}` ring at 2px offset) · active/pressed (prescribed — fill to `{colors.surface-card}`) · disabled (prescribed — border and text to `{colors.ash}`) · loading and error as `button-primary`. Not selected.

**`button-tab`** + **`button-tab-active`** — install-tab strip
- Default: transparent background, text `{colors.mute}`, type `{typography.button-md}`, padding `8px 16px`, rounded `{rounded.none}`.
- Active: same surface, text `{colors.ink}`, with a 2px `{colors.ash}` bottom underline indicating selection.
- Used in the install-method tab strip on the home page (`curl` / `npm` / `bun` / `brew` / `yay`).
- **States:** default (extracted) · selected (extracted — `button-tab-active`: text to `{colors.ink}` plus the 2px bottom underline) · hover (prescribed — text to `{colors.ink}`, no underline) · focus-visible (prescribed — 2px `{colors.focus}` ring at 2px offset, inset so it does not clip the strip rule) · active/pressed (prescribed — same as selected, applied immediately on pointer-down). No disabled, loading or error state: the strip is a client-side switch between five static snippets, so a tab is never unavailable and never waiting.
- **Selection contrast:** the extracted underline colour `{colors.ash}` measures 2.8:1 on `{colors.canvas}` and misses the 3:1 non-text minimum. `{colors.hairline-strong}` (5.92:1) is the accessible substitute and needs no new token; see `## Accessibility`.

**`button-disabled`**
- Background `{colors.surface-card}`, text `{colors.ash}`, rounded `{rounded.sm}`.
- **States:** one state by definition. WCAG sets no contrast requirement on disabled controls; the 2.49:1 of `{colors.ash}` on `{colors.surface-card}` is therefore recorded, not corrected.

### Badges & Chips

**`badge-news`** — small dark chip in the news/announcement strip
- Background `{colors.surface-dark}`, text `{colors.on-dark}`, type `{typography.caption-md}`, padding `2px 8px`, rounded `{rounded.sm}`.
- Sits inline with body copy as a "News" / "Beta" / "Live now" tag on the home page above the hero headline.
- **States:** default only — a static label, not interactive. Where the whole news strip is a link, the surrounding row carries hover and focus-visible, not the badge.

**`badge-section-label`** — bracketed section header
- Background transparent, text `{colors.ink}`, type `{typography.heading-md}`, rounded `{rounded.none}`.
- Renders as a bare `**Heading**` line above a 1px `{colors.hairline}` rule with no chip background — but the way the text reads ("[+]", "[x]", `What is OpenCode?`) makes it function as a label component.
- **States:** default only — static text. No hover, focus-visible, pressed, disabled, loading, selected or error state exists for it.

### Inputs & Forms

**`text-input`** + **`text-input-focused`**
- Default: background `{colors.surface-soft}`, text `{colors.ink}`, 1px solid `{colors.hairline}`, type `{typography.body-md}`, padding `8px 12px`, height ~40px, rounded `{rounded.sm}`.
- Focused: background flips to `{colors.canvas}`, border becomes 1px solid `{colors.ink}` (the canvas's flat focus signal — no halo, no glow).
- Used for every contact-form field on `/enterprise` (Full name, Role, Company, Company email, Phone number) and the newsletter email field at the home page footer.
- **States:** default (extracted) · focus-visible (extracted as the border swap in `text-input-focused`; **prescribed addition** — the 2px `{colors.focus}` ring at 2px offset, because the extracted border swap alone changes only colour and gives a keyboard user no indicator distinguishable from the hover tint) · hover (prescribed — border to `{colors.hairline-strong}`) · disabled (prescribed — fill `{colors.surface-card}`, text `{colors.ash}`) · error (prescribed — 1px border to `{colors.danger}`, message beneath in `{typography.caption-md}` `{colors.danger}` prefixed `[x]`, never colour alone) · loading (prescribed — read-only during submit, `[-]` glyph in the trailing cell). No selected state.
- **Boundary contrast:** the extracted 1px border is `{colors.hairline}`, which composites to 1.31:1 on its own `{colors.surface-soft}` fill. For an input whose only boundary is that rule this fails the 3:1 non-text minimum; `{colors.hairline-strong}` (5.67:1 on `{colors.surface-soft}`) is the accessible substitute and already exists in the palette. See `## Accessibility`.

**`textarea`**
- Background `{colors.surface-soft}`, text `{colors.ink}`, 1px solid `{colors.hairline}`, type `{typography.body-md}`, padding `12px`, rounded `{rounded.sm}`.
- "What problem are you trying to solve?" multi-line textarea on `/enterprise`.
- **States:** identical to `text-input` — default, hover, focus-visible, disabled, error, loading; no selected state. Same boundary-contrast caveat applies.

**`install-snippet`** — the home page's signature install code block
- Background `{colors.surface-card}` (`#f1eeee`), text `{colors.ink}` rendered in `{typography.body-md}` (already monospaced — Berkeley Mono), padding `12px 16px`, rounded `{rounded.sm}`.
- Contains the literal `curl -fsSL https://opencode.ai/install | bash` command with a small copy-icon at the right edge. Sits below the install-method tab strip.
- **States:** the block itself is static; its copy affordance carries default (extracted) · hover (prescribed — glyph to `{colors.ink}`) · focus-visible (prescribed — 2px `{colors.focus}` ring at 2px offset) · active/pressed (prescribed — glyph to `{colors.ink-deep}`) · loading (prescribed — glyph swaps to `[-]` for `{motion.duration-base}` while the clipboard write resolves) · selected (prescribed — the "copied" confirmation reads as `[x] copied` in `{colors.mute}`, held 1.5s, opacity only). No disabled or error state.

### Cards & Containers

**`hero-tui-mockup`** — the home page's signature TUI preview
- Container: full-bleed `{colors.surface-dark}` (~near-black), padding `64px 32px`, rounded `{rounded.none}`.
- Contents (top → bottom): ASCII block-pixel "OPENCODE" wordmark centered in `{colors.on-dark}`; a `{component.tui-prompt-row}` showing a "Build" command line with model selector text; an `tab switch agent  ctrl-p commands` keybinding hint row at the bottom in `{colors.ash}`.
- **States:** default only — a static mockup, not a live terminal. It is not focusable, has no hover affordance, and never enters a loading, selected or error state.

**`tui-prompt-row`** — the inset command line inside the TUI mockup
- Background `{colors.surface-dark-elevated}` (`#302c2c`), text `{colors.on-dark}` in `{typography.body-md}`, padding `8px 12px`, rounded `{rounded.sm}`.
- Renders an inline command (`Build  Claude Opus 4.5  OpenCode Zen`) with a leading vertical pipe and the model name styled as a bracketed token.
- **States:** default only, for the same reason as its container. The leading pipe is a static glyph, not a blinking caret — nothing in the mockup animates.

**`list-row`** — feature/benefit row with ASCII bracket bullet
- Background `{colors.canvas}`, text `{colors.body}` in `{typography.body-md}`, padding `8px 0`.
- Each row begins with a `[+]` / `[-]` / `[x]` ASCII marker followed by a bold label and a regular description: e.g., `[+] LSP enabled    Automatically loads the right LSPs for the IDE`. The bracket marker is part of the text content, not a separate icon.
- **States:** default only where the row is prose. Where a row wraps a link, the link carries hover and focus-visible per `link-inline`; the row has no pressed, disabled, loading, selected or error state.

**`faq-row`** — FAQ entry with bracket toggle
- Background `{colors.canvas}`, text `{colors.ink}` in `{typography.body-md}`, padding `12px 0`, with a 1px `{colors.hairline}` bottom rule.
- Each row leads with `+` / `−` ASCII markers indicating expand/collapse state. Always rendered as plain text rows — no chevron icons, no animated accordion chrome.
- **States:** default/collapsed (extracted) · selected/expanded (extracted — marker flips `+` → `−`) · hover (prescribed — question text to `{colors.charcoal}`) · focus-visible (prescribed — 2px `{colors.focus}` ring at 2px offset around the question row only) · active/pressed (prescribed — marker flips on pointer-down, no fill change). No disabled, loading or error state: the answers are in the document, so nothing is fetched.
- The marker, not colour, carries the expanded state, so the state survives greyscale and reduced-motion alike.

**`testimonial-row`** — `/zen` peer-quote row
- Background `{colors.surface-soft}`, text `{colors.body}` in `{typography.body-md}`, padding `16px 20px`, rounded `{rounded.sm}`.
- Layout: a 32px avatar circle (`{rounded.full}`) at left, name + role + company in `{typography.body-strong}` on the first line, quote in `{typography.body-md}` `{colors.body}` on the second line.
- **States:** default only — a static quote. Where the name links out, the anchor carries hover and focus-visible per `link-inline`; the row does not.

**`chart-tile`** — the stat-block sparse-line chart
- Background `{colors.canvas}`, text `{colors.body}` in `{typography.caption-md}`, rounded `{rounded.none}`, padding `16px`.
- Contains an inline SVG/CSS-drawn ASCII-style sparse-line plot (dotted, abstract — never specific data points) with a `Fig N. <stat label>` caption beneath in `{colors.mute}`.
- **States:** default (extracted) · loading (prescribed — the plot area holds its box and the caption reads `Fig N. [-] loading`, opacity only; the tile never collapses or reflows). No hover, focus-visible, pressed, disabled, selected or error state: the plots are decorative and have no data points to inspect.

### Navigation

**`primary-nav`**
- Background `{colors.canvas}`, text `{colors.ink}` in `{typography.body-strong}`, height ~56px, rounded `{rounded.none}`, with a 1px `{colors.hairline}` bottom rule.
- Layout (desktop): block-pixel ASCII OpenCode wordmark at left (~120×24px), nav links cluster center-right ("GitHub [150K] · Docs · Zen · Go · Enterprise"), `{component.button-primary}` "Download" CTA at the far right with a small download glyph.
- **States:** the bar itself is a static container. Each nav link carries default (extracted) · hover (prescribed — text to `{colors.ink}` from `{colors.mute}`, underline appears) · focus-visible (prescribed — 2px `{colors.focus}` ring at 2px offset) · active/pressed (prescribed — text to `{colors.ink-deep}`) · selected (prescribed — current page link stays `{colors.ink}` with a persistent 2px `{colors.hairline-strong}` underline, and carries `aria-current`, so selection is not colour-only). No disabled, loading or error state.

**Top Nav (Mobile)**
- ASCII wordmark stays at left, nav links collapse into a hamburger drawer at the right. The Download CTA remains visible at every breakpoint.
- **States:** the drawer trigger carries default · hover · focus-visible · selected (prescribed — the glyph flips `[+]` → `[x]` when the drawer is open). Drawer open/close timing is in `## Motion & Animation`.

### Footer

**`footer-section`**
- Background `{colors.canvas}`, text `{colors.body}` in `{typography.caption-md}`, padding `32px 0`, with a 1px `{colors.hairline}` top rule.
- Top row: 5-column horizontal link grid (GitHub [150K] · Docs · Changelog · Discord · X), each rendered as a centered cell separated by 1px `{colors.hairline}` vertical rules.
- Bottom row: `©2026 Anomaly` copyright at left, `Brand · Privacy · Terms · English ▼` utility cluster at right, all in `{typography.caption-md}` `{colors.mute}`.
- **States:** the container is static. Footer links carry default (extracted) · hover (prescribed — `{colors.mute}` → `{colors.ink}`, underline appears) · focus-visible (prescribed — 2px `{colors.focus}` ring at 2px offset) · active/pressed (prescribed — `{colors.ink-deep}`). The language selector additionally carries selected (prescribed — chosen locale marked `[x]` in the list, not by colour). The newsletter field inherits every state of `text-input`, including loading and error.

### Inline

**`link-inline`** — body-prose anchor link
- `{colors.ink}` text with underline. The brand's only link affordance — even links inside body paragraphs use ink color rather than `{colors.accent}` blue. Apple Blue is reserved for the in-product TUI.
- **States:** default (extracted — underlined ink) · hover (prescribed — underline thickens to 2px, colour held; no colour change, because the link is already ink on cream and the brand has no second link colour) · focus-visible (prescribed — 2px `{colors.focus}` ring at 2px offset) · active/pressed (prescribed — text to `{colors.ink-deep}`) · visited (prescribed — unchanged; the system draws no distinction). No disabled, loading, selected or error state.
- The underline is permanent, not hover-revealed, so links remain identifiable without colour — which matters in a monochrome system where ink is both link and body ink.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No animation, timing function or duration in this section was extracted from opencode.ai; the values are the shared **Crisp** profile, assigned because the brand is a terminal-native developer tool whose whole identity is a man page rendered in Berkeley Mono. Crisp is the right fit on the file's own evidence: the system has no shadows, no gradients, no photography and no entrance choreography, and its single visual moment is a static TUI mockup. A state change here should read as instant, the way a keystroke does in a terminal — anything slower would contradict the identity.

All values reference `{motion.duration-instant}` (60ms), `{motion.duration-fast}` (100ms), `{motion.duration-base}` (150ms), `{motion.duration-slow}` (220ms), `{motion.duration-emphasis}` (300ms), `{motion.ease-standard}`, `{motion.ease-enter}`, `{motion.ease-exit}`, `{motion.stagger-step}` (20ms) and `{motion.duration-reduced}` (100ms).

### Interaction Table

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, links, nav, tab labels) | `{motion.duration-instant}` | `{motion.ease-standard}` | `color`, `border-color`, `opacity` | Unchanged — colour-only, no travel to remove |
| Press / active | `{motion.duration-instant}` | `{motion.ease-exit}` | `background-color`, `opacity` | Unchanged — no scale to remove; OpenCode never pops on press |
| Focus-visible ring | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` on the ring | Ring appears at full opacity with no transition; it is never delayed |
| Page / route transition | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` only, 0 → 1 | Cross-fade at `{motion.duration-reduced}`; no travel existed to remove |
| Modal / mobile nav drawer | `{motion.duration-base}` enter, `{motion.duration-fast}` exit | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` and `transform: translateX()` | Travel removed; opacity fade only at `{motion.duration-reduced}` |
| Dropdown (language selector) | `{motion.duration-fast}` enter, `{motion.duration-instant}` exit | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` and `transform: translateY(-2px → 0)` | Travel removed; opacity fade only at `{motion.duration-reduced}` |
| Toast ("copied", form confirmation) | `{motion.duration-fast}` enter, `{motion.duration-instant}` exit | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` and `transform: translateY(4px → 0)` | Travel removed; opacity fade only at `{motion.duration-reduced}` |
| List enter (feature rows, footer link grid) | `{motion.duration-fast}` per item, `{motion.stagger-step}` between | `{motion.ease-enter}` | `opacity` only | Stagger removed; all items fade together at `{motion.duration-reduced}` |
| List exit (FAQ collapse, drawer close) | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` only | Items disappear with a `{motion.duration-reduced}` fade |
| Loading (copy glyph, form submit) | `{motion.duration-emphasis}` per full ASCII cycle, looping | steps — the glyph advances `[/]` `[-]` `[\]` `[|]` in discrete frames, no interpolation | glyph substitution and `opacity`; no `transform` | Loop frozen on `[-]`; the control still reports busy via `aria-busy`, so the state survives without animation |

### Rules this system follows

- Only `transform` and `opacity` are animated. Never `width`, `height`, `top`, `left` or `margin` — the FAQ accordion reveals its answer without a height transition, and the mobile drawer slides by `translateX` rather than by changing its box.
- Every exit is shorter than its matching entrance: drawer 100ms out against 150ms in, dropdown and toast 60ms out against 100ms in.
- Nothing animates on first paint. The hero headline, the TUI mockup and the install snippet are painted at full opacity; the list-enter fade applies only to content revealed after interaction or scroll, and never gates reading.
- The only looping animation in the system is the ASCII loading glyph. There is no brand ambience, no blinking caret in the TUI mockup, and no infinite marquee.
- Travel distances are deliberately tiny — 2px for the dropdown, 4px for the toast. In a monospaced grid, anything larger reads as the layout breaking rather than as motion.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. The drawer, dropdown and toast
     no longer translate; the list-enter stagger is dropped so every
     item resolves at once. The ASCII loading glyph stops cycling and
     freezes on [-], with aria-busy carrying the state instead. */
  *, *::before, *::after {
    transition-duration: 100ms !important;  /* {motion.duration-reduced} */
    animation-duration: 100ms !important;
    animation-iteration-count: 1 !important;
    transition-property: opacity, color, background-color, border-color !important;
  }
}
```

**What remains:** opacity fades at `{motion.duration-reduced}` (100ms), and every colour and border-colour change — hover, press, focus, selection — at its normal timing, because none of them involves travel. **What is removed:** all `transform` (drawer slide, dropdown and toast lift), the `{motion.stagger-step}` sequencing on list enter, and the looping loading glyph. Nothing that communicates state is lost: hover, press, focus, selection and busy are all reported by colour, by an ASCII marker, or by an ARIA attribute, so none of them depends on motion.

## Accessibility

Every ratio below is computed from this file's own frontmatter hexes with WCAG 2.1 relative luminance. The `{colors.hairline}` figures are the composite of its `rgba(15,0,0,0.12)` over the ground it is actually drawn on, not over a notional white. Nothing here is measured from a rendered page: tap-target figures are the documented box sizes from `## Responsive Behavior`, not observed hit areas.

### Measured contrast — passing

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 16.34:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-soft}` | 15.65:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.surface-card}` | 14.51:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas}` | 9.78:1 | 4.5:1 | Pass |
| `{colors.mute}` on `{colors.canvas}` | 5.92:1 | 4.5:1 | Pass |
| `{colors.stone}` on `{colors.canvas}` | 4.95:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 16.34:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.surface-dark}` | 16.34:1 | 4.5:1 | Pass |
| `{colors.on-dark-mute}` on `{colors.surface-dark}` | 5.83:1 | 4.5:1 | Pass |
| `{colors.on-dark-mute}` on `{colors.surface-dark-elevated}` | 4.81:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 5.92:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.canvas}` | 16.34:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.surface-soft}` | 15.65:1 | 3.0:1 | Pass |
| `{colors.focus}` on `{colors.surface-card}` | 14.51:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` on `{colors.surface-dark}` | 16.34:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` on `{colors.surface-dark-elevated}` | 13.47:1 | 3.0:1 | Pass |
| `{colors.focus-on-dark}` on `{colors.ink-deep}` | 20.1:1 | 3.0:1 | Pass |

### Measured contrast — real failures, stated plainly

These are extracted brand values. They are frozen, not corrected in place.

- **`{colors.hairline}` on `{colors.canvas}` — 1.31:1, needs 3.0:1. Fails.** The extracted hairline is `rgba(15,0,0,0.12)`, which composites to `#e0dede` on the cream canvas. As a decorative section divider between 96px-separated blocks this is defensible — the whitespace, not the rule, carries the separation. As the sole boundary of a control it is not.
- **`{colors.hairline}` on `{colors.surface-soft}` — 1.31:1, needs 3.0:1. Fails.** Composited over the input's own `#f8f7f7` fill the hairline resolves to `#dcd9d9`, and the ratio is the same 1.31:1 as on the canvas, because the two grounds are within one luminance step of each other. This is the case that matters: `text-input` and `textarea` have no other boundary, so the brand as built gives a 1.31:1 edge where 3:1 is required. `{colors.hairline-strong}` (5.67:1 on `{colors.surface-soft}`) is the accessible substitute, and it already exists in the palette — no new token is needed. The original is scoped to decoration in `## Elevation & Depth`. (For the record, the audit harness composites `{colors.hairline}` over the canvas before measuring it against this surface and so reports this pair as 1.25:1; the correctly composited figure is the 1.31:1 above. Both are failures, and the difference is in the harness, not the brand.)
- **`{colors.ash}` as the active-tab underline on `{colors.canvas}` — 2.8:1, needs 3.0:1. Fails.** The install-method tab strip indicates its selection with a 2px `{colors.ash}` rule, which is a non-text UI component under 1.4.11 and misses the threshold. It is also the only selection signal in the strip. `{colors.hairline-strong}` (5.92:1) is the substitute; the `button-tab` entry records both.
- **`{colors.accent}` on `{colors.canvas}` — 3.92:1, needs 4.5:1. Fails as body-size text.** Apple Blue is never used as marketing text in the captured surfaces — the brand's link colour is `{colors.ink}` — so this ratio is not exercised on the pages documented here. On `{colors.surface-dark}`, where the TUI mockup does use it, it measures 4.17:1 and still misses 4.5:1. Treat it as a 3:1-at-18px-and-above tone, or as a non-text syntax highlight, which is how the TUI uses it.
- **`{colors.success}` on `{colors.canvas}` — 1.97:1, needs 4.5:1. Fails.** This is Apple HIG green used unmodified. It fails 3:1 as well, so it is not defensible at any text size on cream.
- **`{colors.warning}` on `{colors.canvas}` — 2.01:1, needs 4.5:1. Fails.** Apple HIG orange, also below 3:1 on cream.
- **`{colors.warning-hover}` on `{colors.canvas}` — 3.10:1, needs 4.5:1. Fails as body text**, clears 3:1, so it is defensible only at 18.66px/bold or 24px and above, or as a non-text indicator.
- **`{colors.danger}` on `{colors.canvas}` — 3.46:1, needs 4.5:1. Fails as body text**, clears 3:1, so the same large-text-only note applies. `{colors.danger-hover}` (5.26:1) and `{colors.danger-active}` (7.86:1) both pass at body size, so prescribed error text in `text-input` should use `{colors.danger}` for the 1px border (non-text, 3:1 applies) and `{colors.danger-hover}` for the message copy.

The honest summary: **the whole Apple HIG semantic ramp this brand ships fails AA on its own cream canvas at body size.** Three of those four tones read correctly on `{colors.surface-dark}` — success 8.28:1, warning 8.14:1, danger 4.72:1 — which is consistent with the file's own rule that the ramp belongs to the in-product TUI and not to marketing chrome. Taken as a dark-surface palette it is sound; taken as cream-canvas text it is not, and nothing in the captured surfaces uses it that way.

Disabled tones are exempt from contrast requirements and are recorded rather than corrected: `{colors.ash}` on `{colors.surface-card}` measures 2.49:1 in `button-disabled`.

### Focus ring visibility, surface by surface

The ring is **prescribed**, not extracted — see `## Colors`. It is 2px solid with a 2px offset, drawn outside the control so it is judged against the surface behind it.

| Surface this file defines | Ring drawn | Ratio |
|---|---|---|
| `{colors.canvas}` | `{colors.focus}` | 16.34:1 |
| `{colors.surface-soft}` | `{colors.focus}` | 15.65:1 |
| `{colors.surface-card}` | `{colors.focus}` | 14.51:1 |
| `{colors.surface-dark}` | `{colors.focus-on-dark}` | 16.34:1 |
| `{colors.surface-dark-elevated}` | `{colors.focus-on-dark}` | 13.47:1 |
| `{colors.ink-deep}` (pressed CTA fill) | `{colors.focus-on-dark}` | 20.1:1 |

One ring cannot serve both polarities here: `{colors.focus}` is 1.0:1 on `{colors.surface-dark}`, since the brand uses one near-black for both its ink and its dark surface. That is why the file defines a counterpart rather than a single ring.

### Tap targets

From this file's documented box sizes, not from a rendered page: `{component.button-primary}` is specified at 36px tall, `{component.text-input}` and `{component.textarea}` at 40px, and `{component.button-tab}` at 32–36px extended to a 44px cell by inline padding. Footer links reach roughly 44px from `{typography.caption-md}`'s 2.0 line-height plus 8px vertical padding. The 36px and 40px heights clear the 24×24px minimum of WCAG 2.2 Target Size (Minimum, AA) but sit below the 44×44px of Target Size (Enhanced, AAA). **These are documented values; actual rendered hit areas were not measured and cannot be verified from this document.**

### Reduced motion

`## Motion & Animation` states the full `@media (prefers-reduced-motion: reduce)` rule. In short: all travel and the list stagger are removed, opacity fades hold at `{motion.duration-reduced}` (100ms), the ASCII loading glyph freezes on `[-]`, and every state the system reports — hover, press, focus, selection, busy — remains legible from colour, an ASCII marker, or an ARIA attribute rather than from motion.

### Non-colour state signalling

The monospaced ASCII vocabulary is an accessibility asset, not only a style: `[+]` / `[-]` / `[x]` markers carry expand, collapse and error state as text, so FAQ expansion, form errors and the copy confirmation all survive greyscale, high-contrast mode and reduced motion. `link-inline` keeps a permanent underline rather than revealing one on hover, and the prescribed selected-nav state pairs its underline with `aria-current`.

## Do's and Don'ts

### Do
- Render every text role in Berkeley Mono. The single-font decision is the entire identity.
- Keep `{colors.canvas}` (`#fdfcfc`) as the only body background. Don't introduce gray section bands.
- Use ASCII bracket markers (`[+]`, `[-]`, `[x]`, `+`, `−`) as bullets, toggles, and section glyphs. They are the brand's only iconography.
- Anchor the dark `{component.hero-tui-mockup}` exactly once per landing page as the hero centerpiece. Never use the dark surface for body content.
- Reserve `{colors.accent}` (Apple Blue) and the rest of the semantic ramp for in-TUI states; marketing chrome stays monochrome.
- Use `{rounded.sm}` (4px) on every interactive element and `{rounded.none}` (0px) on every container.
- Stack content sections at `{spacing.section}` (96px) rhythm with only 1px `{colors.hairline}` rules between them.
- Keep state changes at `{motion.duration-instant}` or `{motion.duration-fast}`. A terminal responds on the keystroke; so should this page.
- Draw focus as the 2px `{colors.focus}` ring with a 2px offset on light grounds, and `{colors.focus-on-dark}` inside the TUI mockup.
- Use `{colors.hairline-strong}` wherever a rule is the only boundary of a control. `{colors.hairline}` is decoration.

### Don't
- Don't introduce a sans-serif body font, a display face, or an italic style. Berkeley Mono carries everything.
- Don't add drop shadows, gradients, or atmospheric backgrounds. The system is flat-on-cream.
- Don't replace the ASCII bracket markers with SVG icons. The brackets are the icons.
- Don't use the semantic accent ramp (`{colors.accent}`, `{colors.warning}`, `{colors.danger}`, `{colors.success}`) on marketing CTAs. They belong to the in-product TUI.
- Don't pad cards with 24px+ internal padding. List rows sit at 8px vertical; FAQ rows at 12px.
- Don't render the OpenCode wordmark as a vector logo. It is always block-pixel ASCII.
- Don't fill the hero TUI mockup with photography or illustration. It is text-only and always shows a faux terminal command line.
- Don't add entrance choreography, spring easing, scale pops or parallax. Crisp means the state is simply there; a 300ms reveal would make a man page feel like a product tour.
- Don't animate `width`, `height`, `top`, `left` or `margin` — reveal the FAQ answer and slide the mobile drawer with `transform` and `opacity` only.
- Don't give the focus ring a colour the brand does not own. Apple Blue stays in the TUI; the ring is ink on cream and cream on ink.
- Don't signal a state with colour alone. The ASCII markers (`[+]`, `[-]`, `[x]`) are what make selection, errors and busy states legible in greyscale and under reduced motion.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| desktop-large | 1280px+ | Default — 960px content column, 5-up footer link grid |
| desktop | 1024px | Same layout; nav remains horizontal |
| tablet | 850px | Footer collapses to 2-up grid; `/enterprise` two-column form stacks |
| tablet-narrow | 768px | Primary nav becomes hamburger drawer; Download CTA stays visible |
| mobile | 640px | Single-column everything; hero display drops 38px → ~28px; section padding tightens |

### Touch Targets
All interactive elements meet WCAG AA at the ~36–40px height range. `{component.button-primary}` sits at ~36px with 20px horizontal padding. `{component.text-input}` and `{component.textarea}` sit at ~40px. `{component.button-tab}` rows in the install-method strip sit at ~32–36px depending on label length but extend to a full 44px tappable cell via inline padding. Footer links use `{typography.caption-md}` (14px) but receive ~28px line-height (caption-md is 2.0) plus 8px vertical padding for a comfortable ~44px tappable row.

### Collapsing Strategy
- **Primary nav:** desktop horizontal cluster → tablet-narrow hamburger drawer at 768px. The dark "Download" CTA stays visible at all widths.
- **Hero TUI mockup:** maintains its full-bleed dark surface at every breakpoint; the ASCII wordmark scales proportionally and the keybinding-hint row may wrap to two lines on narrow screens.
- **Install snippet + tab strip:** desktop fixed-width pill → mobile full-width pill with horizontal scroll on the tab strip if labels overflow.
- **Footer:** 5-up horizontal link grid → 2-up at tablet → 1-up at mobile (each link becomes a full-width row).
- **`/enterprise` two-column layout:** desktop 50/50 → tablet stacks to single-column with the form below the text block.
- **Section padding:** `{spacing.section}` (96px) desktop → 64px tablet → 48px mobile.
- **Hero headline:** `{typography.display-xl}` (38px) at desktop, scaling to ~28px at mobile, line-height holding at 1.5.

### Image Behavior
There are no raster images in the system aside from the favicon and OG share image. Every visual element — wordmarks, charts, icons — is rendered as type or inline SVG and scales without aspect-ratio considerations.

## Iteration Guide

1. Focus on ONE component at a time. Pull its YAML entry and verify every property resolves.
2. Reference component names and tokens directly (`{colors.ink}`, `{component.hero-tui-mockup}`, `{rounded.sm}`) — do not paraphrase.
3. Run `npx @google/design.md lint DESIGN.md` after edits — `broken-ref`, `contrast-ratio`, and `orphaned-tokens` warnings flag issues automatically.
4. Add new variants as separate component entries (`-active`, `-disabled`) — do not bury them inside prose.
5. Default body to `{typography.body-md}`; reach for `{typography.body-strong}` for emphasis; reserve `{typography.display-xl}` strictly for the page-top hero headline.
6. Keep `{colors.surface-dark}` scarce — at most one full-bleed dark mockup per page. The dark surface is a narrative device, not a chrome treatment.
7. When introducing a new component, ask whether it can be expressed with the existing ASCII-bracket + 4px-radius + Berkeley-Mono vocabulary before adding new tokens. The system's strength is that it almost never needs new ones.

## Known Gaps

- **Mobile screenshots not captured** — responsive behavior synthesizes OpenCode's mobile pattern (hamburger drawer, single-column, footer accordion) from desktop evidence and the breakpoint stack.
- **Hover states not captured.** No hover appearance was recorded for any control. Every hover entry in `## Components` is prescribed from the brand's own colour vocabulary, not extracted.
- **Motion is prescribed, not measured.** Nobody timed opencode.ai. The `motion:` token group and the whole of `## Motion & Animation` are the shared **Crisp** profile, assigned from the brand's terminal/developer-tool identity. No duration or easing in this file was observed on the live site.
- **The focus ring is prescribed.** The only focus appearance captured anywhere is `text-input-focused`'s border swap. `{colors.focus}` and `{colors.focus-on-dark}` are specified here, measured against this file's own surfaces, and labelled as such in `## Colors`.
- **Loading, selected and error appearances are prescribed** for every control that plausibly has them. The captured surfaces show no spinner, no inline validation message and no selected styling beyond the install-tab underline.
- **In-product TUI screenshots** beyond the marketing hero mockup are not in the captured set; the actual `opencode` terminal interface (full keybindings, panels, status bar) is not documented here.
- **`/go` page** not extracted — the marketing page for the Go SDK likely shares the same chrome but introduces code-sample blocks not documented above.
- **Form validation state styling** (success / error inline messages) not present in the captured surfaces.
