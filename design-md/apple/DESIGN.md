---
version: alpha
name: Apple-design-analysis
description: A photography-first interface that turns marketing into a museum gallery. Edge-to-edge product tiles alternate light and dark canvases, framed by SF Pro Display headlines with negative letter-spacing and a single Action Blue (#0066cc) interactive color. UI chrome recedes so the product can speak — no decorative gradients, no shadows on chrome, only the one signature drop-shadow under product imagery resting on a surface.

colors:
  primary: "#0066cc"
  primary-focus: "#0071e3"
  primary-on-dark: "#2997ff"
  ink: "#1d1d1f"
  body: "#1d1d1f"
  body-on-dark: "#ffffff"
  body-muted: "#cccccc"
  ink-muted-80: "#333333"
  ink-muted-48: "#7a7a7a"
  divider-soft: "#f0f0f0"
  hairline: "#e0e0e0"
  hairline-strong: "#86868b"
  muted-strong: "#6e6e73"
  canvas: "#ffffff"
  canvas-parchment: "#f5f5f7"
  surface-card: "#ffffff"
  surface-pearl: "#fafafc"
  surface-tile-1: "#272729"
  surface-tile-2: "#2a2a2c"
  surface-tile-3: "#252527"
  surface-black: "#000000"
  surface-chip-translucent: "#d2d2d7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  focus: "#0071e3"
  focus-on-dark: "#2997ff"
  focus-ink: "#1d1d1f"

typography:
  hero-display:
    fontFamily: "SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.07
    letterSpacing: -0.28px
  display-lg:
    fontFamily: "SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0
  display-md:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.47
    letterSpacing: -0.374px
  lead:
    fontFamily: "SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: 0.196px
  lead-airy:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  tagline:
    fontFamily: "SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: 21px
    fontWeight: 600
    lineHeight: 1.19
    letterSpacing: 0.231px
  body-strong:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.24
    letterSpacing: -0.374px
  body:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: -0.374px
  dense-link:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 2.41
    letterSpacing: 0
  caption:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: -0.224px
  caption-strong:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.224px
  button-large:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: 0
  button-utility:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: -0.224px
  fine-print:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.12px
  micro-legal:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.08px
  nav-link:
    fontFamily: "SF Pro Text, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.12px

rounded:
  none: 0px
  xs: 5px
  sm: 8px
  md: 11px
  lg: 18px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 17px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px

shadow:
  none: none
  hairline-ring: rgba(0, 0, 0, 0.08) 0 0 0 1px
  soft-ring: rgba(0, 0, 0, 0.04) 0 0 0 3px
  product: rgba(0, 0, 0, 0.22) 3px 5px 30px 0

motion:
  duration-instant: 120ms
  duration-fast: 240ms
  duration-base: 400ms
  duration-slow: 600ms
  duration-emphasis: 900ms
  ease-standard: cubic-bezier(0.28, 0, 0.12, 1)
  ease-enter: cubic-bezier(0.16, 1, 0.3, 1)
  ease-exit: cubic-bezier(0.4, 0, 0.9, 1)
  stagger-step: 80ms

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 11px 22px
  button-primary-focus:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-primary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-secondary-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 11px 22px
  button-dark-utility:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-utility}"
    rounded: "{rounded.sm}"
    padding: 8px 15px
  button-pearl-capsule:
    backgroundColor: "{colors.surface-pearl}"
    textColor: "{colors.ink-muted-80}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-store-hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-large}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  button-icon-circular:
    backgroundColor: "{colors.surface-chip-translucent}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 44px
  text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body}"
  text-link-on-dark:
    backgroundColor: transparent
    textColor: "{colors.primary-on-dark}"
    typography: "{typography.body}"
  global-nav:
    backgroundColor: "{colors.surface-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 44px
  sub-nav-frosted:
    backgroundColor: "{colors.canvas-parchment}"
    textColor: "{colors.ink}"
    typography: "{typography.tagline}"
    height: 52px
  product-tile-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.none}"
    padding: 80px
  product-tile-parchment:
    backgroundColor: "{colors.canvas-parchment}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.none}"
    padding: 80px
  product-tile-dark:
    backgroundColor: "{colors.surface-tile-1}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.none}"
    padding: 80px
  product-tile-dark-2:
    backgroundColor: "{colors.surface-tile-2}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  product-tile-dark-3:
    backgroundColor: "{colors.surface-tile-3}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  store-utility-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.lg}"
    padding: 24px
  configurator-option-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 12px 16px
  configurator-option-chip-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    height: 44px
  floating-sticky-bar:
    backgroundColor: "{colors.canvas-parchment}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    height: 64px
    padding: 12px 32px
  environment-quote-card:
    backgroundColor: "{colors.surface-tile-1}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.none}"
    padding: 80px
  footer:
    backgroundColor: "{colors.canvas-parchment}"
    textColor: "{colors.ink-muted-80}"
    typography: "{typography.fine-print}"
    padding: 64px
---

## Overview

Apple's web presence is a masterclass in **reverent product photography framed by near-invisible UI**. Every page is a stack of edge-to-edge product "tiles" — alternating light and dark canvases, each centered on a hero headline, a one-line tagline, two tiny blue pill CTAs, and an impossibly crisp product render. Nothing competes with the product. Typography is confident but quiet; color is either pure white, an off-white parchment, or a near-black tile; interactive elements are a single, quiet blue.

Density is unusually low even by contemporary SaaS standards. Each tile occupies roughly one viewport, and there is no decorative chrome — no borders, no gradients, no decorative frames, no shadows on headlines. Elevation appears only when a product image rests on a surface (a single soft `rgba(0, 0, 0, 0.22) 3px 5px 30px` drop for visual weight). The result is a catalog that feels more like a museum gallery: the wall disappears and the artifact takes over.

Store and shop surfaces retain the same chassis but switch modes. The product configurator (iPhone 17 Pro, accessories grid) introduces a tight grid of white utility cards at `{rounded.lg}` (18px) radius with a thin border, paired with a persistent thin sub-nav strip. The environment page leans darker and more editorial. Across all five surfaces the typographic system, spacing rhythm, and the single blue accent are consistent — this is one design language expressed at different volumes.

**Key Characteristics:**
- Photography-first presentation; UI recedes so the product can speak.
- Alternating full-bleed tile sections: white/parchment ↔ near-black, with the color change itself acting as the section divider.
- Single blue accent (`{colors.primary}` — #0066cc) carries every interactive element. No second brand color exists.
- Two button grammars: tiny blue pill CTAs (`{rounded.pill}`) and compact utility rects (`{rounded.sm}`).
- SF Pro Display + SF Pro Text — negative letter-spacing at display sizes for the signature "Apple tight" headline feel.
- Whisper-soft elevation used only when a product image needs to breathe — exactly one drop-shadow in the entire system.
- Tight two-row nav: slim `{component.global-nav}` + product-specific `{component.sub-nav-frosted}` with persistent right-aligned primary CTA.
- Section rhythm across multiple pages: light hero → dark product tile → light utility tile → dark tile → parchment footer — a predictable pulse.

## Colors

> **Source pages analyzed:** homepage, environment, store, iPhone 17 Pro buy page, accessories index. The color system is identical across all five surfaces; only the surface-mode mix differs.

### Brand & Accent
- **Action Blue** (`{colors.primary}` — #0066cc): The single brand-level interactive color. All text links, all blue pill CTAs ("Learn more", "Buy"), and the focus ring root. This is Apple's quiet but universal "click me" signal. Press state shifts to a slightly darker variant via the active scale transform rather than a hex change.
- **Focus Blue** (`{colors.primary-focus}` — #0071e3): A marginally brighter sibling of Action Blue, reserved for the keyboard focus ring on buttons (`outline: 2px solid`).
- **Sky Link Blue** (`{colors.primary-on-dark}` — #2997ff): A brighter blue used on dark surfaces for in-copy links and inline callouts, where Action Blue would disappear against the tile background. **It is a text colour, never a fill.** As text it passes: 4.94:1 on `{colors.surface-tile-1}`, 6.96:1 on `{colors.surface-black}`. As a *filled* surface it does not: `{colors.on-primary}` white on it measures only **3.02:1**, below the 4.5:1 AA floor for text on a signal colour. So never build a Sky-Blue pill button. If one is ever needed, set its label in `{colors.focus-ink}` (#1d1d1f), which measures 5.58:1 on it.

### Surface
- **Pure White** (`{colors.canvas}` — #ffffff): The dominant canvas. Content, utility cards, store tiles, configurator grids.
- **Card White** (`{colors.surface-card}` — #ffffff): The raised-surface alias for the store/accessories utility card and the configurator chip. It is the *same* white as `{colors.canvas}` — measured 1.00:1 against it, and 1.09:1 against `{colors.canvas-parchment}`. Apple's light-mode elevation is not luminance-based; the card is separated from the page only by its 1px hairline. The token exists so a build can address the raised layer without re-pointing at the page floor.
- **Parchment** (`{colors.canvas-parchment}` — #f5f5f7): The signature Apple off-white. Used for alternating light tiles, footer region, and the default page canvas in store utility sections. Just different enough from white to create rhythm.
- **Pearl Button** (`{colors.surface-pearl}` — #fafafc): A near-white used as the fill for secondary "ghost" buttons — lighter than the parchment canvas so the button still reads as a button against `{colors.canvas-parchment}`.
- **Near-Black Tile 1** (`{colors.surface-tile-1}` — #272729): The primary dark-tile surface on the homepage product grid.
- **Near-Black Tile 2** (`{colors.surface-tile-2}` — #2a2a2c): A micro-step lighter — used where a dark tile sits directly above or below Tile 1 to create the faintest separation.
- **Near-Black Tile 3** (`{colors.surface-tile-3}` — #252527): A micro-step darker — used at the bottom of the stack and in embedded video/player frames.
- **Pure Black** (`{colors.surface-black}` — #000000): Reserved for true void — video player backgrounds, edge-to-edge photographic overlays, the global nav bar background.
- **Translucent Chip Gray** (`{colors.surface-chip-translucent}` — #d2d2d7): The base hex of the translucent gray chip used over photography for circular control buttons. In production, applied at ~64% alpha as `rgba(210, 210, 215, 0.64)`.

### Text
- **Near-Black Ink** (`{colors.ink}` — #1d1d1f): The voice of every headline, every body paragraph, and the dark utility button's fill. Chosen instead of pure black to keep the page feeling photographic rather than printed.
- **Body** (`{colors.body}` — #1d1d1f): Same hex as ink — Apple uses one near-black tone for all text on light surfaces.
- **Body On Dark** (`{colors.body-on-dark}` — #ffffff): All text on dark tiles and on the global nav bar.
- **Body Muted** (`{colors.body-muted}` — #cccccc): Secondary copy **on dark tiles only**, where pure white would be too loud. It measures 9.28:1 on `{colors.surface-tile-1}` and 13.08:1 on `{colors.surface-black}` — comfortably AA. On a light canvas it measures **1.61:1 and is unusable**; never place it on `{colors.canvas}`, `{colors.canvas-parchment}` or `{colors.surface-card}`.
- **Muted Strong** (`{colors.muted-strong}` — #6e6e73) — *prescribed, not extracted*: The light-surface counterpart to Body Muted, added because the extracted system has no AA-passing secondary ink for light tiles. Measures 5.07:1 on `{colors.canvas}` and 4.66:1 on `{colors.canvas-parchment}`. Use for captions, price deltas and spec subcopy on light surfaces at any size.
- **Ink Muted 80** (`{colors.ink-muted-80}` — #333333): Body text on the white Pearl Button surface — slightly softer than pure black.
- **Ink Muted 48** (`{colors.ink-muted-48}` — #7a7a7a): Disabled button text and legal fine-print. Measures 4.29:1 on `{colors.canvas}` and 3.94:1 on `{colors.canvas-parchment}` — **below the 4.5:1 AA floor** at the 12px `{typography.fine-print}` and 10px `{typography.micro-legal}` sizes it is actually used at. Legitimate only in its disabled-text role, where WCAG sets no requirement. For live legal copy, use `{colors.muted-strong}`.

### Hairlines & Borders
- **Divider Soft** (`{colors.divider-soft}` — #f0f0f0): The "border" tone on secondary buttons — functions as a ring shadow rather than a hard line. In production, often applied as `rgba(0, 0, 0, 0.04)`.
- **Hairline** (`{colors.hairline}` — #e0e0e0): The extracted 1px hairline on store utility cards and configurator chips. Measures **1.32:1 on `{colors.canvas}` and 1.21:1 on `{colors.canvas-parchment}` — far below the 3.0:1 a component boundary needs.** This is the real brand value and it is kept as-is; scope it to decoration only (card edges that carry no interactive meaning). Apple genuinely fails AA here: on `{component.store-utility-card}` and `{component.configurator-option-chip}` the hairline is the *only* boundary, and at 1.32:1 a low-vision user cannot see where the control begins.
- **Hairline Strong** (`{colors.hairline-strong}` — #86868b) — *prescribed, not extracted*: The parallel accessible boundary. Measures 3.62:1 on `{colors.canvas}` and 3.33:1 on `{colors.canvas-parchment}`. Use wherever the border is the only edge of an interactive control — `{component.configurator-option-chip}`, `{component.search-input}`, `{component.store-utility-card}` when the whole card is clickable. Keep `{colors.hairline}` for decorative rules only.

### Focus

No focus colour existed in the extracted system; the three tokens below are *prescribed*. The ring is always `2px solid` with `2px` offset, drawn **outside** the control so it lands on the page surface rather than on the control fill.

- **Focus Blue** (`{colors.focus}` — #0071e3): The ring on light surfaces. Measures 4.70:1 on `{colors.canvas}`, 4.31:1 on `{colors.canvas-parchment}`, 4.51:1 on `{colors.surface-pearl}` — all above the 3.0:1 non-text floor. Shares its hex with `{colors.primary-focus}`, which keeps the signal single-blue.
- **Focus Sky** (`{colors.focus-on-dark}` — #2997ff): The ring on dark tiles. 4.94:1 on `{colors.surface-tile-1}`, 4.75:1 on `{colors.surface-tile-2}`, 5.07:1 on `{colors.surface-tile-3}`, 6.96:1 on `{colors.surface-black}`.
- **Focus Ink** (`{colors.focus-ink}` — #1d1d1f): The ring where a blue ring would sit *on* blue or over photography — an accent-filled `{component.button-primary}` whose offset ring overlaps the fill, and `{component.button-icon-circular}` floating over an image. 3.02:1 on `{colors.primary}`, 3.58:1 on `{colors.primary-focus}`, 11.17:1 on `{colors.surface-chip-translucent}`, 16.83:1 on `{colors.canvas}`. A blue ring fails this job outright: `{colors.focus}` on `{colors.primary}` measures 1.19:1.

### Brand Gradient
**No decorative gradients.** Atmospheric depth on product photography (the iPhone 17 Pro camera plate, the Apple Watch bands, AirPods reflections) is inherent to the imagery, not a CSS gradient overlay. The environment page's hero uses photographic atmosphere (mountain vista at dawn) but no gradient tokens are defined. Apple is the rare luxury-brand site with zero gradient-based design tokens.

## Typography

### Font Family
- **Display**: `SF Pro Display, system-ui, -apple-system, sans-serif` — Apple's proprietary display face, optimized for sizes ≥ 19px. Defines the voice of every headline.
- **Body / UI**: `SF Pro Text, system-ui, -apple-system, sans-serif` — the text-optimized variant used for body copy, captions, buttons, and links below 20px.
- **OpenType features**: `font-variant-numeric: numerator` is enabled on numeric links (pricing tables, spec sheets). Display sizes rely on tight tracking rather than contextual ligatures.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 56px | 600 | 1.07 | -0.28px | Hero headline; the signature "Apple tight" tracking |
| `{typography.display-lg}` | 40px | 600 | 1.10 | 0 | Tile headlines atop every product tile |
| `{typography.display-md}` | 34px | 600 | 1.47 | -0.374px | Section heads (SF Pro Text at display proportions) |
| `{typography.lead}` | 28px | 400 | 1.14 | 0.196px | Product tile subcopy |
| `{typography.lead-airy}` | 24px | 300 | 1.5 | 0 | Environment-page lead paragraphs (the rare weight 300) |
| `{typography.tagline}` | 21px | 600 | 1.19 | 0.231px | Sub-tile tagline; sub-nav category name |
| `{typography.body-strong}` | 17px | 600 | 1.24 | -0.374px | Inline strong emphasis |
| `{typography.body}` | 17px | 400 | 1.47 | -0.374px | Default paragraph |
| `{typography.dense-link}` | 17px | 400 | 2.41 | 0 | Footer / store utility link lists (relaxed leading) |
| `{typography.caption}` | 14px | 400 | 1.43 | -0.224px | Secondary captions, button text |
| `{typography.caption-strong}` | 14px | 600 | 1.29 | -0.224px | Emphasized captions |
| `{typography.button-large}` | 18px | 300 | 1.0 | 0 | Store hero CTAs (the rare weight 300) |
| `{typography.button-utility}` | 14px | 400 | 1.29 | -0.224px | Utility/nav button labels |
| `{typography.fine-print}` | 12px | 400 | 1.0 | -0.12px | Fine-print, footer body |
| `{typography.micro-legal}` | 10px | 400 | 1.3 | -0.08px | Micro legal disclaimers |
| `{typography.nav-link}` | 12px | 400 | 1.0 | -0.12px | Global nav menu items |

### Principles

- **Negative letter-spacing at display sizes — but not uniformly.** The tighten (`-0.08 → -0.374px`) runs through `{typography.hero-display}`, `{typography.display-md}`, `{typography.body}`, `{typography.body-strong}`, `{typography.caption}`, `{typography.fine-print}`, `{typography.micro-legal}` and `{typography.nav-link}`. Three roles deliberately break it: `{typography.display-lg}` sits at 0, and `{typography.lead}` (+0.196px) and `{typography.tagline}` (+0.231px) run *positive* — the subcopy opens up while the headline above it closes in. Do not "correct" those three to negative; the contrast between tight headline and open tagline is the cadence.
- **Body copy at 17px, not 16px.** Apple breaks the SaaS convention and runs paragraph text at 17px. The extra pixel gives the page an unmistakable "reading, not scanning" pace.
- **Weight 300 is real and rare.** Used deliberately on a handful of large-size reads (`{typography.button-large}` at 18px/300 and `{typography.lead-airy}` at 24px/300). It's not an accident — it's a light-atmosphere cue reserved for moments where the content should feel airy.
- **Weight 600, not 700, for headlines.** Apple's headlines sit at weight 600, `{typography.tagline}` included. **No role in this file uses 700**; the weight ladder actually defined is 300 / 400 / 600.
- **Line-height is context-specific.** Display sizes use 1.07–1.19 (tight). Body uses 1.47. Utility link stacks in the footer/store use an unusually relaxed 2.41 (`{typography.dense-link}`). The 2.41 is not a bug — it's how the footer's dense link columns breathe.
- **Weight 500 is deliberately absent.** The ladder is 300 / 400 / 600. Mid-weight readings always use 600.

### Note on Font Substitutes
SF Pro is Apple's proprietary system font. When building off-system:

- Use `system-ui, -apple-system, BlinkMacSystemFont` as the first stack entry — on macOS/iOS/Safari this resolves to the real SF Pro.
- For non-Apple platforms, **Inter** (Google Fonts, variable) is the closest open-source equivalent. Inter at weight 600 with `font-feature-settings: "ss03"` approximates SF Pro's rounded "a" character.
- Nudge `letter-spacing` down by `-0.01em` on display sizes to re-create the Apple tight feel; Inter's default tracking runs slightly wider than SF Pro.
- For body text, tighten line-height by `0.03` (from 1.47 → 1.44) when substituting Inter — Inter's taller x-height needs less leading.

## Layout

### Spacing System
- **Base unit:** 8px. Sub-base values (2, 4, 5, 6, 7) are used for tight typographic adjustments; structural layout snaps to 8/12/16/20/24.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 17px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- **Section vertical padding:** `{spacing.section}` (80px) inside a product tile; tiles stack edge-to-edge with 0 gap (the color change provides the break).
- **Card padding:** `{spacing.lg}` (24px) inside utility grid cards.
- **Button padding:** 8–11px vertical, 15–22px horizontal.
- **Universal rhythm constants:** the 17px body line-height multiplier (~25px line) and 21px tagline size show up on every analyzed page.

### Grid & Container
- **Max content width:** ~980px on text-heavy sections (environment), ~1440px on product grids (store, accessories), full-bleed for product tiles (homepage).
- **Column patterns:** 3 to 5 column utility card grid on store/accessories; 2-column side-by-side tiles on homepage occasional sections; single-column centered stack on product tile heroes.
- **Gutters:** 20–24px between cards in a utility grid.

### Whitespace Philosophy
Apple's whitespace is the product's pedestal. Every tile begins with at least 64px of air above its headline and 48–64px below. Product renders are never crowded; the nearest content to a product image is at least 40px away. The footer is the only area that breaks this — there, Apple goes deliberately dense to make the full information architecture visible at a glance.

## Elevation & Depth

| Level | Token | Treatment | Use |
|---|---|---|---|
| Flat | `{shadow.none}` | No shadow, no border | Full-bleed tiles, global nav, footer, body sections |
| Soft hairline | `{shadow.hairline-ring}` | 1px `rgba(0, 0, 0, 0.08)` border | Utility cards, sub-nav frosted-glass separator |
| Soft ring | `{shadow.soft-ring}` | 3px `rgba(0, 0, 0, 0.04)` ring | `{component.button-pearl-capsule}` — reads as a halo, not a line |
| Backdrop blur | — | `backdrop-filter: blur(N)` on Parchment 80% | Sub-nav and the iPhone buy floating sticky bar |
| Product shadow | `{shadow.product}` | `rgba(0, 0, 0, 0.22) 3px 5px 30px 0` | Product renders resting on a surface (the only true "shadow" in the system) |

**Shadow philosophy.** Apple uses **exactly one** drop-shadow, and it is applied to photographic product imagery — never to cards, never to buttons, never to text. Elevation in the UI comes from (a) surface-color change (light tile ↔ dark tile) and (b) backdrop-blur on sticky bars. The single shadow is about giving the product weight, not about UI hierarchy.

**Elevation is expressed one way per mode, and the light mode's way is weak.** Measured layer separation:

| Layer pair | Ratio | Reading |
|---|---|---|
| `{colors.canvas}` → `{colors.surface-card}` | 1.00:1 | identical white; the 1px border is the *only* separation |
| `{colors.canvas}` → `{colors.canvas-parchment}` | 1.09:1 | the section-rhythm step, not an elevation step |
| `{colors.canvas-parchment}` → `{colors.surface-pearl}` | 1.04:1 | the ghost button barely lifts off the parchment |
| `{colors.surface-tile-1}` → `{colors.surface-tile-2}` | 1.04:1 | deliberate micro-step; invisible by design |
| `{colors.surface-tile-1}` → `{colors.surface-tile-3}` | 1.03:1 | deliberate micro-step |
| `{colors.surface-black}` → `{colors.surface-tile-1}` | 1.41:1 | the only layer pair a sighted user reads as a step |

On light surfaces, therefore, **luminance carries no elevation at all** — the border does the whole job, and at `{colors.hairline}` 1.32:1 that border is itself below the 3.0:1 boundary floor. Use `{colors.hairline-strong}` (3.62:1) wherever the boundary must be perceivable. The system is consistent — one border grammar on light, one surface-swap grammar on dark, never shadow mixed with border — but its light-mode consistency is achieved at an inaccessible contrast level.

### Decorative Depth
- **Atmospheric imagery** on the environment page (photographic vista) supplies mood; no CSS gradient involved.
- **Edge-to-edge tile alternation** creates rhythm without borders or shadows — the color change itself is the divider.
- **Backdrop-filter blur** on `{component.sub-nav-frosted}` and `{component.floating-sticky-bar}` creates a "floating over content" effect that's functional, not decorative.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed product tiles (no corner rounding) |
| `{rounded.xs}` | 5px | Inline links when styled as subtle chips (rare) |
| `{rounded.sm}` | 8px | Dark utility buttons (Sign In, Bag), inline card imagery |
| `{rounded.md}` | 11px | White Pearl Button capsules |
| `{rounded.lg}` | 18px | Store utility cards, accessories grid cards |
| `{rounded.pill}` | 9999px | Primary blue pill CTAs, sub-nav buy button, configurator option chips, search input — the signature Apple pill |
| `{rounded.full}` | 9999px / 50% | Circular control chips floating over photography |

### Photography Geometry
- **Hero imagery**: full-bleed, 21:9 or taller on the homepage; 16:9 on environment and shop pages. Product renders are photographic-realistic, often shot on a tinted surface that becomes the tile background.
- **Product renders**: PNG/WebP with transparency; rest on a surface tile and pick up the system shadow.
- **Accessory grid**: square 1:1 crops at `{rounded.lg}` (18px) radius, light neutral backgrounds, product centered with 20–40px internal padding.
- **No rounded imagery in hero tiles** — images are full-bleed rectangular. Rounding (`{rounded.sm}`, `{rounded.lg}`) appears only on inline card imagery.
- Lazy-loading via responsive `srcset` and `sizes` across all breakpoints; CDN-optimized WebP.

## Components

### Top Navigation

**`global-nav`** — Persistent, ultra-thin black nav bar pinned to the top of every page. Background `{colors.surface-black}`, height 44px, text `{colors.on-dark}` in `{typography.nav-link}` (12px / 400 / -0.12px tracking). Links are quiet, spaced ~20px apart, running edge-to-edge across the top. Right-aligned cluster: Search, Bag icons — always visible. On mobile, collapses to hamburger at ~834px and the Apple logo centers.

**`sub-nav-frosted`** — Surface-specific nav that sticks below the global nav. Background `{colors.canvas-parchment}` at 80% opacity with backdrop-filter blur, creating a frosted-glass effect. Height 52px. Content on left: product category name ("iPhone", "Store", "Accessories") in `{typography.tagline}` (21px / 600). Content right: inline nav links in `{typography.button-utility}` (14px), ending in a persistent `{component.button-primary}` ("Buy") or a utility link.

### Buttons

**`button-primary`** — The signature Apple action. Background `{colors.primary}` (Action Blue #0066cc), text `{colors.on-primary}` in `{typography.body}` (SF Pro Text 17px / 400), rounded `{rounded.pill}` (full pill — capsule-shaped), padding 11px × 22px. The full-pill radius IS the brand action signal.
- Active state: `{component.button-primary-active}` — `transform: scale(0.95)` (the system-wide micro-interaction).
- Focus state: `{component.button-primary-focus}` — 2px solid `{colors.primary-focus}` outline.

**`button-secondary-pill`** — Used as the second CTA when two blue pills appear together ("Learn more" / "Buy"). Background transparent, text `{colors.primary}`, 1px solid `{colors.primary}` border, rounded `{rounded.pill}`, padding 11px × 22px. Reads as a "ghost pill."

**`button-dark-utility`** — Global nav actions (Sign In, Bag, language selector). Background `{colors.ink}` (#1d1d1f), text `{colors.on-dark}` in `{typography.button-utility}` (14px / 400 / -0.224px tracking), rounded `{rounded.sm}` (8px), padding 8px × 15px. Active state shrinks via `transform: scale(0.95)`.

**`button-pearl-capsule`** — Product-card secondary button. Background `{colors.surface-pearl}` (#fafafc), text `{colors.ink-muted-80}` in `{typography.caption}` (14px), 3px solid `{colors.divider-soft}` border (functions as a soft ring rather than a visible line), rounded `{rounded.md}` (11px), padding 8px × 14px.

**`button-store-hero`** — A larger primary CTA used on store hero surfaces. Same Action Blue + Paper White as `{component.button-primary}`, but with `{typography.button-large}` (18px / 300 — note the rare weight 300) and slightly more padding (14px × 28px). Used sparingly on the store landing.

**`button-icon-circular`** — Floats over photography. 44 × 44px, background `{colors.surface-chip-translucent}` at ~64% alpha, icon in `{colors.ink}`, rounded `{rounded.full}`. Used for carousel controls, close buttons, and in-image controls (product image thumbnails on the iPhone buy page).

**`text-link`** — Inline body links in `{colors.primary}` (Action Blue). Underlined or non-underlined per context.

**`text-link-on-dark`** — Inline body links on dark tiles in `{colors.primary-on-dark}` (Sky Link Blue #2997ff) — Action Blue would disappear against `{colors.surface-tile-1}`.

### Cards & Containers

**`product-tile-light`** — Full-bleed light tile. Background `{colors.canvas}` (white), text `{colors.ink}`, rounded `{rounded.none}` (0 — tiles touch edges), vertical padding `{spacing.section}` (80px). Centered stack: product name in `{typography.display-lg}` (40px / 600) → one-line tagline in `{typography.lead}` (28px / 400) → two `{component.button-primary}` CTAs ("Learn more" / "Buy") → product render resting on the surface with the system shadow.

**`product-tile-parchment`** — Same as `{component.product-tile-light}` but on `{colors.canvas-parchment}` (#f5f5f7). Used to break two consecutive white tiles.

**`product-tile-dark`** — Full-bleed dark tile. Background `{colors.surface-tile-1}` (#272729), text `{colors.on-dark}`, rounded `{rounded.none}`, vertical padding `{spacing.section}` (80px). Same content stack as the light tile but with `{component.text-link-on-dark}` for inline copy and `{component.button-primary}` (Action Blue still works on the dark surface). Used on the homepage product grid as the alternating dark band.

**`product-tile-dark-2`** — Variant on `{colors.surface-tile-2}` (#2a2a2c). Used where a dark tile sits directly above or below `{component.product-tile-dark}` to create the faintest separation through micro-step lightness change.

**`product-tile-dark-3`** — Variant on `{colors.surface-tile-3}` (#252527). Used at the bottom of the stack and in embedded video/player frames.

**`store-utility-card`** — Used in store grid and accessories grid. Background `{colors.canvas}` (white), 1px solid `{colors.hairline}` border, rounded `{rounded.lg}` (18px), padding `{spacing.lg}` (24px). Top: product image (1:1 crop with `{rounded.sm}` (8px) inner image radius). Below: product name in `{typography.body-strong}` (17px / 600), price in `{typography.body}` (17px / 400), and a `{component.text-link}` ("Buy" or "Learn more"). No shadow by default; product render itself carries the system product-shadow.

**`configurator-option-chip`** — Pill-shaped tappable cell used in the iPhone 17 Pro buy page. Background `{colors.canvas}`, text `{colors.ink}` in `{typography.caption}`, rounded `{rounded.pill}`, padding 12px × 16px. Contains a small product thumbnail + label + price delta. Arranged in a grid of 4–5 options per row.

**`configurator-option-chip-selected`** — Selected state. Border upgrades to 2px solid `{colors.primary-focus}`. Same shape, same content.

**`environment-quote-card`** — A photographic-canvas hero specific to the environment page. Dark photographic backdrop (mountain vista at dawn) with `{colors.surface-tile-1}` as the fallback color, centered white-text headline in `{typography.display-lg}` (40px), small green "Apple 2030" pictographic logo above the headline, single `{component.button-primary}` below. Padding `{spacing.section}` (80px).

**`floating-sticky-bar`** — Floats at the bottom of the viewport on the iPhone 17 Pro buy page during scroll. Background `{colors.canvas-parchment}` at 80% opacity with `backdrop-filter: blur(N)`, height 64px, padding 12px × 32px. Left: running price total in `{typography.body}`. Right: `{component.button-primary}` ("Add to Bag").

### Inputs & Forms

**`search-input`** — The accessories search input. Background `{colors.canvas}`, text `{colors.ink}` in `{typography.body}` (17px), 1px solid `rgba(0, 0, 0, 0.08)` border, rounded `{rounded.pill}` (full pill — search is also pill-shaped, matching the CTA grammar), padding 12px × 20px, height 44px. Leading icon: search glyph at 14px, muted tint.

Error and validation states were not surfaced in the analyzed pages.

### Footer

**`footer`** — Background `{colors.canvas-parchment}` (#f5f5f7), text `{colors.ink-muted-80}`. Link columns in `{typography.dense-link}` (17px / 400 / 2.41 line-height — the relaxed leading is what makes the dense columns scannable). Column headings in `{typography.caption-strong}` (14px / 600). Legal row at the very bottom in `{typography.fine-print}` (12px / 400) with `{colors.ink-muted-48}` text. Vertical padding 64px.

### Interaction States

Only **default**, **active / pressed**, **focus** and **selected** were observable on the analyzed pages — Apple's marketing surfaces expose no disabled, loading or error UI outside the checkout flow. The rows below mark each state `extracted` or `prescribed`; prescribed states follow the Action-Blue-and-scale grammar the extracted states establish, and nothing else.

| Component | default | hover | focus-visible | active / pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `{component.button-primary}` | `{colors.primary}` fill, `{colors.on-primary}` label *(extracted)* | fill lightens to `{colors.primary-focus}`, no travel *(prescribed)* | 2px `{colors.focus}` ring at 2px offset; `{colors.focus-ink}` where the ring overlaps the fill *(prescribed)* | `transform: scale(0.95)` *(extracted)* | `{colors.ink-muted-48}` label on `{colors.surface-pearl}`, no ring, `aria-disabled` *(prescribed)* | label swaps for a 16px spinner, width locked so nothing reflows *(prescribed)* | n/a — not a selectable control | n/a — errors surface on the form, not the button |
| `{component.button-secondary-pill}` | transparent fill, 1px `{colors.primary}` border *(extracted)* | border thickens to 2px, no colour change *(prescribed)* | 2px `{colors.focus}` ring at 2px offset *(prescribed)* | `transform: scale(0.95)` *(prescribed, mirrors primary)* | border and label to `{colors.ink-muted-48}` *(prescribed)* | spinner in `{colors.primary}` *(prescribed)* | n/a | n/a |
| `{component.button-dark-utility}` | `{colors.ink}` fill, `{colors.on-dark}` label *(extracted)* | fill to `{colors.surface-tile-2}` *(prescribed)* | 2px `{colors.focus-on-dark}` ring *(prescribed)* | `transform: scale(0.95)` *(extracted)* | 48% label opacity *(prescribed)* | not applicable — nav actions navigate, they do not submit | n/a | n/a |
| `{component.button-pearl-capsule}` | `{colors.surface-pearl}` fill, `{shadow.soft-ring}` *(extracted)* | ring darkens to `{colors.hairline}` *(prescribed)* | 2px `{colors.focus}` ring *(prescribed)* | `transform: scale(0.95)` *(prescribed)* | label to `{colors.ink-muted-48}` *(prescribed)* | spinner replaces label *(prescribed)* | n/a | n/a |
| `{component.button-store-hero}` | as `{component.button-primary}` at `{typography.button-large}` *(extracted)* | as `{component.button-primary}` *(prescribed)* | as `{component.button-primary}` *(prescribed)* | `transform: scale(0.95)` *(prescribed)* | as `{component.button-primary}` *(prescribed)* | as `{component.button-primary}` *(prescribed)* | n/a | n/a |
| `{component.button-icon-circular}` | translucent chip, `{colors.ink}` glyph *(extracted)* | chip alpha 0.64 → 0.80 *(prescribed)* | 2px `{colors.focus-ink}` ring — blue is unreadable over photography *(prescribed)* | `transform: scale(0.95)` *(prescribed)* | alpha 0.32, glyph to `{colors.ink-muted-48}` *(prescribed)* | n/a — carousel controls never load | n/a | n/a |
| `{component.text-link}` / `{component.text-link-on-dark}` | `{colors.primary}` / `{colors.primary-on-dark}` *(extracted)* | underline appears; colour unchanged *(prescribed)* | 2px `{colors.focus}` / `{colors.focus-on-dark}` ring *(prescribed)* | no scale — text must not jump *(prescribed)* | `{colors.ink-muted-48}`, underline removed *(prescribed)* | n/a | n/a | n/a |
| `{component.configurator-option-chip}` | `{colors.canvas}` fill, 1px `{colors.hairline-strong}` border *(extracted; border upgraded for AA)* | border to `{colors.primary}` *(prescribed)* | 2px `{colors.focus}` ring at 2px offset *(prescribed)* | `transform: scale(0.98)` — gentler than a button, the chip is large *(prescribed)* | 40% opacity, `aria-disabled`, struck-through price *(prescribed; "sold out" is a real configurator condition)* | skeleton chip at `{colors.canvas-parchment}` while price deltas resolve *(prescribed)* | `{component.configurator-option-chip-selected}` — 2px `{colors.primary-focus}` border *(extracted)* | 2px `{colors.hairline-strong}` border plus an inline message in `{colors.muted-strong}`; no red exists in this palette *(prescribed)* |
| `{component.search-input}` | `{colors.canvas}` fill, 1px `{colors.hairline-strong}` border *(extracted; border upgraded for AA)* | border to `{colors.hairline-strong}` at 1.5px *(prescribed)* | 2px `{colors.focus}` ring at 2px offset, border unchanged *(prescribed)* | n/a — inputs are not pressed | border and placeholder to `{colors.hairline}`, `aria-disabled` *(prescribed)* | trailing 14px spinner replaces the clear glyph *(prescribed)* | n/a | message below the field in `{colors.muted-strong}` + 2px `{colors.hairline-strong}` border, `aria-invalid="true"` *(prescribed — the brand ships no error colour)* |
| `{component.store-utility-card}` | `{colors.surface-card}` fill, 1px `{colors.hairline}` *(extracted)* | whole-card hover lifts nothing; the inner `{component.text-link}` underlines *(prescribed)* | 2px `{colors.focus}` ring on the card when the whole card is the link *(prescribed)* | `transform: scale(0.99)` when the card itself is the target *(prescribed)* | 40% opacity for out-of-stock *(prescribed)* | skeleton block at `{colors.canvas-parchment}` *(prescribed)* | n/a | n/a |
| `{component.global-nav}` / `{component.sub-nav-frosted}` | as specified above *(extracted)* | nav link opacity 0.8 → 1.0 *(prescribed)* | 2px `{colors.focus-on-dark}` ring on global nav, `{colors.focus}` on sub-nav *(prescribed)* | n/a | n/a | n/a | current-section link at full opacity, others at 0.8 *(prescribed)* | n/a |
| `{component.product-tile-light}` / `-parchment` / `-dark` / `-2` / `-3`, `{component.environment-quote-card}` | **genuinely two states only: default and in-view.** They are layout surfaces, not controls — no hover, no focus, no pressed, no disabled, no loading, no selected, no error. Their only behaviour is the in-view reveal in Motion & Animation. | | | | | | | |
| `{component.floating-sticky-bar}` | pinned, `{colors.canvas-parchment}` at 80% + blur *(extracted)* | n/a — the bar is a container | focus passes to the contained `{component.button-primary}` | n/a | n/a | price total shows a 2-character skeleton while recalculating *(prescribed)* | n/a | n/a |
| `{component.footer}` | as specified above *(extracted)* | link underlines *(prescribed)* | 2px `{colors.focus}` ring *(prescribed)* | n/a | n/a | n/a | n/a | n/a |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or stagger below was extracted from apple.com; the only motion fact the analyzed pages actually yielded is the `transform: scale(0.95)` press, which is documented above and reused here unchanged. Everything else is an inference from the **Cinematic** profile — the right profile for this file, because the identity is hardware-luxury, the canvas alternates into near-black tiles, and the whole layout exists to let full-bleed product photography hold the screen. The one place Cinematic is wrong is press feedback: a 400ms press feels broken, so press alone drops to `{motion.duration-instant}`. Slow motion is for *arrival*, never for *acknowledgement*.

Only `transform` and `opacity` are animated. Never animate `width`, `height`, `top`, `left` or `margin` — those trigger layout, and a product tile that reflows mid-scroll destroys the gallery illusion.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, chip, link) | `{motion.duration-fast}` (240ms) | `{motion.ease-standard}` | `opacity`, and `border-color`/`background-color` as a non-animated swap | Colour swap applies instantly; no fade |
| Press / active | `{motion.duration-instant}` (120ms) | `{motion.ease-exit}` | `transform: scale(0.95)` | Removed entirely — scale is travel. No visual press; rely on focus ring and result |
| Focus-visible | `{motion.duration-instant}` (120ms) | `{motion.ease-standard}` | `opacity` on the ring only; the ring's geometry never animates | Ring appears instantly at full opacity |
| Page / route transition | `{motion.duration-slow}` (600ms) in, `{motion.duration-base}` (400ms) out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` 0→1, `transform: translateY(24px)`→0 | `opacity` only, 120ms, no travel |
| Modal / drawer (bag, nav tray) | `{motion.duration-base}` (400ms) in, `{motion.duration-fast}` (240ms) out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` on the scrim, `transform: translateY(100%)`→0 on the sheet | `opacity` only, 120ms; the sheet is present or absent, never sliding |
| Dropdown (sub-nav tray, locale picker) | `{motion.duration-fast}` (240ms) in, `{motion.duration-instant}` (120ms) out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: translateY(-8px)`→0 | `opacity` only, 120ms |
| Toast ("Added to Bag") | `{motion.duration-base}` (400ms) in, `{motion.duration-fast}` (240ms) out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity`, `transform: translateY(16px)`→0 | `opacity` only, 120ms. Dismiss timer extends to 8s, since a fade gives less warning than a slide |
| List enter (store / accessories grid, configurator chips) | `{motion.duration-slow}` (600ms) per item, `{motion.stagger-step}` (80ms) between items, capped at 8 items | `{motion.ease-enter}` | `opacity` 0→1, `transform: translateY(32px) scale(0.98)`→none | All items at full opacity immediately; no stagger, no travel |
| List exit (filter change, search clear) | `{motion.duration-fast}` (240ms), no stagger | `{motion.ease-exit}` | `opacity` 1→0 | Removed instantly |
| Loading (spinner, skeleton) | 1000ms linear loop (spinner); 1600ms skeleton shimmer | `linear` | `transform: rotate()` on the spinner, `opacity` 0.4↔1.0 on the skeleton | Spinner frozen; skeleton holds a static `{colors.canvas-parchment}` block. A text status replaces both for screen readers either way |
| **Signature:** full-bleed product reveal on scroll-into-view | `{motion.duration-emphasis}` (900ms) for the image, type entering at `{motion.duration-slow}` (600ms) one `{motion.stagger-step}` later | `{motion.ease-enter}` | `transform: scale(1.04)`→`scale(1)` on the image, `opacity` + `translateY(24px)`→0 on headline then tagline then CTAs | Removed. Tile renders at its final state on first paint |

**Rules this file holds itself to.** Every exit is shorter than its matching entrance. Nothing animates on first paint in a way that delays content: the above-fold hero renders at its final state and only below-fold tiles reveal on scroll-into-view. There is no infinite animation anywhere except the loaders in the table above — this brand has no ambient motion, which is consistent with its "no decorative gradients, no decorative chrome" posture, and ambience must not be introduced.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and all scale. No translateY, no scale(0.95) press,
     no scale(1.04) product reveal, no stagger. */
  /* Kept: opacity fades, capped at {motion.duration-instant} (120ms). */
  /* Frozen: the spinner's rotate() and the skeleton shimmer hold a static frame;
     an aria-live text status carries the loading state instead. */
  *, *::before, *::after {
    animation-duration: 120ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 120ms !important;
    transition-property: opacity !important;
  }
}
```

## Accessibility

### Measured contrast

Every ratio below is computed from this file's own hexes with WCAG 2.1 relative luminance. Failures are stated, not softened.

| Foreground / Background | Ratio | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` / `{colors.canvas}` | 16.83:1 | 4.5 | pass |
| `{colors.ink}` / `{colors.canvas-parchment}` | 15.46:1 | 4.5 | pass |
| `{colors.ink}` / `{colors.surface-card}` | 16.83:1 | 4.5 | pass |
| `{colors.on-dark}` / `{colors.surface-tile-1}` | 14.91:1 | 4.5 | pass |
| `{colors.on-dark}` / `{colors.surface-black}` | 21.00:1 | 4.5 | pass |
| `{colors.body-muted}` / `{colors.surface-tile-1}` | 9.28:1 | 4.5 | pass (its only legitimate surface) |
| `{colors.body-muted}` / `{colors.canvas}` | **1.61:1** | 4.5 | **fail — forbidden combination, see Colors** |
| `{colors.muted-strong}` / `{colors.canvas}` | 5.07:1 | 4.5 | pass *(prescribed token)* |
| `{colors.ink-muted-48}` / `{colors.canvas}` | **4.29:1** | 4.5 | **fail** — real brand value; AA-legal only in its disabled-text role |
| `{colors.on-primary}` / `{colors.primary}` | 5.57:1 | 4.5 | pass |
| `{colors.on-primary}` / `{colors.primary-focus}` | 4.70:1 | 4.5 | pass |
| `{colors.on-primary}` / `{colors.primary-on-dark}` | **3.02:1** | 4.5 | **fail** — real brand value; see Colors. Never use Sky Link Blue as a fill |
| `{colors.primary}` / `{colors.canvas}` | 5.57:1 | 4.5 | pass (links are text) |
| `{colors.primary-on-dark}` / `{colors.surface-tile-1}` | 4.94:1 | 4.5 | pass |
| `{colors.hairline}` / `{colors.canvas}` | **1.32:1** | 3.0 | **fail** — real brand value; decoration only |
| `{colors.divider-soft}` / `{colors.canvas}` | **1.14:1** | 3.0 | **fail** — real brand value; a halo, never a boundary |
| `{colors.hairline-strong}` / `{colors.canvas}` | 3.62:1 | 3.0 | pass *(prescribed token)* |

**Plainly: Apple fails AA at three measured points in this system** — the hairline that is the only boundary of the store card, configurator chip and search input (1.32:1); the 12px and 10px legal copy set in `{colors.ink-muted-48}` (4.29:1); and white on Sky Link Blue if anyone ever builds it as a fill (3.02:1). The first two are shipping conditions, not hypotheticals. The prescribed `{colors.hairline-strong}` and `{colors.muted-strong}` are the minimum changes that fix them without touching a brand identity hex.

### Focus ring visibility, per surface this file defines

The ring is `2px solid` with `2px` offset, drawn outside the control.

| Surface | Ring token | Ratio | Required |
|---|---|---|---|
| `{colors.canvas}` | `{colors.focus}` | 4.70:1 | 3.0 |
| `{colors.canvas-parchment}` | `{colors.focus}` | 4.31:1 | 3.0 |
| `{colors.surface-card}` | `{colors.focus}` | 4.70:1 | 3.0 |
| `{colors.surface-pearl}` | `{colors.focus}` | 4.51:1 | 3.0 |
| `{colors.surface-tile-1}` | `{colors.focus-on-dark}` | 4.94:1 | 3.0 |
| `{colors.surface-tile-2}` | `{colors.focus-on-dark}` | 4.75:1 | 3.0 |
| `{colors.surface-tile-3}` | `{colors.focus-on-dark}` | 5.07:1 | 3.0 |
| `{colors.surface-black}` | `{colors.focus-on-dark}` | 6.96:1 | 3.0 |
| `{colors.primary}` fill (ring overlaps an Action Blue pill) | `{colors.focus-ink}` | 3.02:1 | 3.0 |
| `{colors.primary-focus}` fill | `{colors.focus-ink}` | 3.58:1 | 3.0 |
| `{colors.surface-chip-translucent}` over photography | `{colors.focus-ink}` | 11.17:1 | 3.0 |

One ring cannot serve this file, because it documents a white canvas, near-black signature tiles and an accent-filled pill all at once: `{colors.focus}` measures **1.19:1 against `{colors.primary}`**, so a blue ring disappears on a blue pill, and `{colors.focus-on-dark}` measures only 3.02:1 on `{colors.canvas}` — a bare pass that reads washed out on white. Hence three rings. The `{colors.focus-ink}` row on `{colors.primary}` is the tightest pass in the file at 3.02:1; that is a floor, not a margin, and if the pill's fill is ever darkened the ring must be re-measured.

### Minimum tap target

44 × 44px, matching the extracted `{component.button-icon-circular}` and the 44px `{component.global-nav}` height. One documented exception fails it: global nav utility links sit at roughly 32 × 80px on desktop. The height is below 44px, so the hamburger tray at ≤ 833px is the only accessible path to those actions on touch. Actual rendered target size cannot be verified from this document — it is a layout fact, not a token.

### Reduced motion

See the `@media (prefers-reduced-motion: reduce)` rule in Motion & Animation. All travel and all scale are removed, opacity fades are capped at `{motion.duration-instant}` (120ms), and loader animation freezes behind an `aria-live` text status. Because the signature product reveal is pure travel and scale, a reduced-motion visitor sees every tile at its final state on first paint and loses nothing but the choreography.

### Not verifiable from this document

Keyboard tab order, screen-reader announcement, actual rendered tap-target size, focus-ring clipping at tile edges, reflow at 320px and text-spacing overrides all need a rendered page. No claim is made about them.

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
| `{colors.hairline}` (`#e0e0e0`) on `{colors.canvas-parchment}` (`#f5f5f7`) | 1.21:1 | 3.0:1 | Fail — boundary on surface, all tones |
| `{colors.body-muted}` (`#cccccc`) on `{colors.canvas-parchment}` (`#f5f5f7`) | 1.47:1 | 4.5:1 | Fail — secondary text on surface, all tones |
| `{colors.ink-muted-48}` (`#7a7a7a`) on `{colors.canvas-parchment}` (`#f5f5f7`) | 3.94:1 | 4.5:1 | Fail — secondary text on surface, all tones |

## Do's and Don'ts

### Do
- Use `{colors.primary}` (Action Blue #0066cc) for every interactive element — links, pill CTAs, focus signals — and nothing else. The single accent is non-negotiable.
- Set headlines in `{typography.hero-display}` or `{typography.display-lg}` with negative letter-spacing (`-0.28 → -0.374px`) to get the signature "Apple tight" cadence.
- Run body copy at `{typography.body}` (17px / 400 / 1.47 / -0.374px) — not 16px. The extra pixel defines the brand's reading pace.
- Alternate `{component.product-tile-light}` (or parchment) and `{component.product-tile-dark}` for full-bleed section rhythm. The color change IS the divider.
- Reserve `{rounded.pill}` for the primary blue CTA and any other element that should read as an "action" (configurator chips, search input, sticky bar CTA).
- Apply the single product-shadow (`rgba(0, 0, 0, 0.22) 3px 5px 30px`) only to product renders resting on a surface — never on cards, buttons, or text.
- Use `transform: scale(0.95)` as the active/press state on every button — it's the system-wide micro-interaction.
- Keep the global nav `{colors.surface-black}` (true black) — it's the only place pure black appears on most pages.

### Don't
- Don't introduce a second accent color; every "click me" signal is `{colors.primary}` (Action Blue).
- Don't add shadows to cards, buttons, or text — shadow is reserved for product imagery.
- Don't use gradients as decorative backgrounds; atmosphere comes from photography.
- Don't set body copy at weight 500 — Apple's ladder is 300 / 400 / 600, with 500 deliberately absent. Body is always 400; strong inline is 600; display is 600.
- Don't round full-bleed tiles — tiles are rectangular and edge-to-edge; the color change is the divider.
- Don't tighten line-height below 1.47 for body copy — the editorial leading is part of the brand.
- Don't mix radii grammars — use `{rounded.sm}` for compact utility, `{rounded.lg}` for utility cards, `{rounded.pill}` for pills, and nothing in between (except the rare `{rounded.md}` Pearl Button).
- Don't use `{colors.primary-on-dark}` (Sky Link Blue) on light surfaces — it's the dark-tile-only variant. Action Blue is for light surfaces.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Small phone | ≤ 419px | Single-column tiles; sub-nav collapses to category name + primary CTA only; hero typography drops to 28px |
| Phone | 420–640px | Single-column stack; product renders scale to 80% of tile width; hero h1 drops to 34px |
| Large phone | 641–735px | Tiles transition to tighter padding (48px vertical vs 80px); fine-print wraps |
| Tablet portrait | 736–833px | Global nav collapses to hamburger; sub-nav hides category chips, keeps primary CTA |
| Tablet landscape | 834–1023px | Global nav returns fully expanded; 3-column utility grids become 2-column |
| Small desktop | 1024–1068px | Product tiles use 2/3 width with margin gutters; hero h1 stays at 40px |
| Desktop | 1069–1440px | Full layout; 4–5 column store grids; 1440px content max |
| Wide desktop | ≥ 1441px | Content locks at 1440px, margins absorb extra width |

The structural breakpoints that matter for agents: 1440px (content lock), 1068px (small-desktop), 833px (tablet landscape switch), 734px (tablet portrait), 640px (phone), 480px (small phone).

### Touch Targets
- Minimum 44 × 44px. `{component.button-primary}` lands at ~44 × 100px (with the full-pill radius making the visible hit area more generous than the label suggests).
- `{component.button-icon-circular}` is exactly 44 × 44px.
- Global nav utility links are smaller (~32 × 80px) — they deliberately sit at a tighter target because they're precision desktop actions, and the mobile hamburger replaces them at ≤ 833px.

### Collapsing Strategy
- **Global nav**: full horizontal link row on desktop → collapses to Apple logo + hamburger + bag icon at 834px and below.
- **Sub-nav**: category name + inline links + primary CTA → category name + primary CTA only at mobile; inline links move into a hamburger tray.
- **Product tiles**: stack from 2-column to 1-column at 834px; vertical padding tightens from 80px → 48px at small-phone.
- **Utility grids** (store, accessories): 5-col → 4-col (1440px) → 3-col (1068px) → 2-col (834px) → 1-col (640px).
- **Hero typography**: `{typography.hero-display}` (56px) → `{typography.display-lg}` (40px) at 1068px → 34px at 640px → 28px at 419px.

### Image Behavior
- All product imagery uses responsive `srcset` with breakpoint-matched crops.
- Hero photography may switch art direction at mobile (e.g., the environment page's vista crops to a taller aspect ratio on mobile, framing the subject differently).
- Product renders maintain their 1:1 or 4:3 aspect ratios across breakpoints; only scale changes.
- Lazy-loading is default; the above-fold hero loads eagerly.

## Iteration Guide

1. Focus on ONE component at a time. Reference its YAML key directly (`{component.product-tile-dark}`, `{component.search-input}`).
2. Variants of an existing component (`-active`, `-focus`, `-2`, `-3`) live as separate entries in `components:`.
3. Use `{token.refs}` everywhere — never inline hex.
4. Default and Active/Pressed are the states the analyzed pages actually yielded. Hover, focus-visible, disabled, loading and error exist in the Interaction States matrix as *prescribed* additions — keep that label when you extend them, and keep hover restrained: a colour swap or an underline, never travel.
4a. Every component's row in Interaction States must stay complete. A component that genuinely has two states says so in the row rather than leaving cells blank.
5. Display headlines stay SF Pro Display 600 with negative letter-spacing. Body stays SF Pro Text 400 at 17px. The boundary is unbreakable.
6. The single drop-shadow (`rgba(0, 0, 0, 0.22) 3px 5px 30px`) is reserved for product photography only.
7. When in doubt about emphasis: alternate surface (light → dark tile) before adding chrome.

## Known Gaps

- **Every motion value in this file is prescribed, not extracted.** No duration, easing curve or stagger was measured from apple.com; the Cinematic profile was applied to a brand whose only observed motion fact is the `transform: scale(0.95)` press. Anyone with access to the live site should re-measure and replace the `motion:` group wholesale.
- **The three `focus*` tokens are prescribed.** The analyzed pages yielded `{colors.primary-focus}` as "the focus ring root" but no ring geometry, offset or dark-surface variant. `{colors.focus}` reuses that hex; `{colors.focus-on-dark}` and `{colors.focus-ink}` are inferences.
- **`{colors.hairline-strong}` and `{colors.muted-strong}` are prescribed accessible parallels**, not Apple values. The extracted `{colors.hairline}` (1.32:1) and `{colors.body-muted}` (1.61:1 on light) are kept untouched and scoped; the real brand fails AA at both points and that failure is recorded rather than patched over.
- `{colors.surface-card}` is an alias of `{colors.canvas}`, added so the raised layer is addressable. It encodes no new extracted fact — Apple's card really is the same white as the page.
- Form validation and error states were not surfaced on the analyzed pages; only the neutral search input is documented. The error treatments in Interaction States are prescribed, and notably **this palette contains no error colour at all** — no red, no amber. A production build will need one, and it will be the first token that breaks the single-accent rule.
- The homepage's embedded video/player frame uses `{colors.surface-black}`; interior player controls are not documented (they're a platform widget, not a web-design token).
- Some component imagery is dynamic (rotating product hero) and its specific copy varies per surface — component specs name the structure, not the rotating content.
- Dark-mode counterparts for store and accessories utility cards were not surfaced on the analyzed pages; the system documented is the daytime/light-dominant variant Apple ships by default.
- Atmospheric photography (environment page mountain vista) is a content asset, not a design token; the documented `{component.environment-quote-card}` describes the structural surface only.
- The exact backdrop-filter blur radius on `{component.sub-nav-frosted}` and `{component.floating-sticky-bar}` is platform-dependent; production CSS uses `saturate(180%) blur(20px)` as a typical baseline but the value isn't formalized as a token.
