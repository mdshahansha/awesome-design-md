---
version: alpha
name: TheVerge-design-analysis
description: The Verge's 2024 redesign — an almost-black #131313 editorial canvas, Manuka display headlines up to 107px, and acid-mint #3cffd0 plus ultraviolet #5200ff used as hazard tape rather than brand wash. Depth is carried by 1px hairlines and saturated full-bleed colour-block story tiles, never by shadow. Every colour, type, spacing, radius, shadow and component value below is read from this file's own prose; the motion group is prescribed, not measured.

colors:
  canvas: "#131313"
  surface-slate: "#2d2d2d"
  surface-hazard-white: "#ffffff"
  text: "#ffffff"
  text-dim: "#949494"
  text-on-slate: "#e9e9e9"
  text-inverted: "#131313"
  black: "#000000"
  accent: "#3cffd0"
  on-accent: "#000000"
  ultraviolet: "#5200ff"
  ultraviolet-rule: "#3d00bf"
  link-hover: "#3860be"
  focus: "#1eaedb"
  focus-on-light: "#0500ff"
  border-white: "#ffffff"
  border-mint: "#309875"
  border-image: "#313131"
  border-hover-ring: "#c2c2c2"
  pressed-gray: "#8c8c8c"
  hover-fill: "rgba(255, 255, 255, 0.2)"
  pressed-fill: "rgba(140, 140, 140, 0.87)"
  overlay-black: "rgba(0, 0, 0, 0.33)"

typography:
  display-hero:
    fontFamily: "Manuka, Impact, Helvetica, sans-serif"
    fontSize: 107px
    fontWeight: 900
    lineHeight: 0.80
    letterSpacing: 1.07px
  display-secondary:
    fontFamily: "Manuka, Impact, Helvetica, sans-serif"
    fontSize: 90px
    fontWeight: 900
    lineHeight: 0.80
  display-tertiary:
    fontFamily: "Manuka, Impact, Helvetica, sans-serif"
    fontSize: 60px
    fontWeight: 900
    lineHeight: 0.80
  headline-large:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.00
  heading-wide:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: 0.32px
  heading-medium:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.00
  heading-small:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.00
  label-light-caps:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 300
    lineHeight: 1.20
    letterSpacing: 1.9px
    textTransform: capitalize
  label-caps-xl:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: 1.8px
    textTransform: uppercase
  body-bold:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.00
  body-relaxed:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.60
  label-inline:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0.15px
  body-compact:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.60
  eyebrow-caps:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 1.8px
    textTransform: uppercase
  tag-label:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0.72px
    textTransform: uppercase
  caption-micro:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 1.1px
    textTransform: uppercase
  meta-nano:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 1.5px
    textTransform: uppercase
  mono-button:
    fontFamily: "PolySans Mono, Courier New, Courier, monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 2.00
    letterSpacing: 1.5px
    textTransform: uppercase
  mono-timestamp:
    fontFamily: "PolySans Mono, Courier New, Courier, monospace"
    fontSize: 11px
    fontWeight: 500-600
    lineHeight: 1.20
    letterSpacing: 1.1-1.8px
    textTransform: uppercase
  serif-body:
    fontFamily: "FK Roman Standard, Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.16px
  serif-caption:
    fontFamily: "FK Roman Standard, Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.20

spacing:
  space-1: 1px
  space-2: 2px
  space-4: 4px
  space-5: 5px
  space-6: 6px
  space-8: 8px
  space-9: 9px
  space-10: 10px
  space-12: 12px
  space-14: 14px
  space-15: 15px
  space-16: 16px
  space-20: 20px
  space-24: 24px
  space-25: 25px
  space-32: 32px
  space-40: 40px
  space-48: 48px
  space-64: 64px

rounded:
  tag: 2px
  image: 3px
  nested: 4px
  tile: 20px
  feature: 24px
  promo: 30px
  pill: 40px
  circle: 50%

shadow:
  reset: "rgba(0, 0, 0, 0) 0px 0px 0px 0px inset"
  atmospheric-ring: "rgba(0, 0, 0, 0.33) 0px 0px 0px 1px"
  hover-ring: "0px 0px 0px 1px #c2c2c2"
  pressed-ring: "0px 0px 0px 1px #8c8c8c"
  active-underline: "0px -1px 0px 0px inset #3cffd0"

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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.feature}"
    padding: "{spacing.space-10} {spacing.space-24}"
  button-primary-hover:
    backgroundColor: "{colors.hover-fill}"
    textColor: "{colors.on-accent}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.feature}"
  button-primary-focus:
    backgroundColor: "{colors.focus}"
    textColor: "{colors.text}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.feature}"
    borderColor: "{colors.focus-on-light}"
  button-primary-pressed:
    backgroundColor: "{colors.pressed-fill}"
    textColor: "{colors.on-accent}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.feature}"
  button-secondary:
    backgroundColor: "{colors.surface-slate}"
    textColor: "{colors.text-on-slate}"
    typography: "{typography.body-bold}"
    rounded: "{rounded.feature}"
    padding: "{spacing.space-10} {spacing.space-24}"
  button-tertiary-outlined:
    backgroundColor: transparent
    textColor: "{colors.accent}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.pill}"
    borderColor: "{colors.accent}"
    padding: "{spacing.space-10} {spacing.space-20}"
  button-outlined-ultraviolet:
    backgroundColor: transparent
    textColor: "{colors.ultraviolet}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.promo}"
    borderColor: "{colors.ultraviolet}"
  pill-tag:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption-micro}"
    rounded: "{rounded.tile}"
    padding: "{spacing.space-4} {spacing.space-10}"
  storystream-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text}"
    typography: "{typography.heading-medium}"
    rounded: "{rounded.tile}"
    borderColor: "{colors.border-white}"
    padding: "{spacing.space-24}"
  storystream-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-dim}"
    typography: "{typography.mono-timestamp}"
    borderColor: "{colors.ultraviolet-rule}"
  feature-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text}"
    typography: "{typography.display-tertiary}"
    rounded: "{rounded.feature}"
    borderColor: "{colors.border-white}"
    padding: "{spacing.space-32}"
  card-mint-tile:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text-inverted}"
    typography: "{typography.heading-medium}"
    rounded: "{rounded.tile}"
    borderColor: "{colors.border-mint}"
    padding: "{spacing.space-24}"
  card-ultraviolet-tile:
    backgroundColor: "{colors.ultraviolet}"
    textColor: "{colors.text}"
    typography: "{typography.heading-wide}"
    rounded: "{rounded.feature}"
    padding: "{spacing.space-24}"
  card-spotlight-tile:
    backgroundColor: "{colors.surface-hazard-white}"
    textColor: "{colors.text-inverted}"
    typography: "{typography.heading-medium}"
    rounded: "{rounded.tile}"
    padding: "{spacing.space-24}"
  input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text}"
    typography: "{typography.label-inline}"
    rounded: "{rounded.tag}"
    borderColor: "{colors.border-white}"
  input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text}"
    typography: "{typography.label-inline}"
    rounded: "{rounded.tag}"
    borderColor: "{colors.ultraviolet}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text}"
    typography: "{typography.mono-button}"
    padding: "{spacing.space-24}"
  image-frame:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.image}"
    borderColor: "{colors.border-image}"
---

# Design System Inspired by The Verge

## Overview

The Verge's 2024 redesign feels like somebody wired a Condé Nast magazine to a chiptune soundboard. The canvas is almost-black (`#131313`), the headlines are built from a brutally heavy display face (Manuka) that runs up to 107px, and the whole page is peppered with acid-mint `#3cffd0` and ultraviolet `#5200ff` that behave less like brand colors and more like hazard tape. Story tiles are not quiet gray cards — they're saturated, full-bleed color blocks (yellow, pink, orange, blue, purple) that feel like pasted-up rave flyers arranged into a timeline. The mood is "developer console meets club night meets tech tabloid": serious enough to cover a congressional hearing, loud enough to review a synthesizer.

What makes this system unmistakable is the **StoryStream** timeline: a vertical feed where every post is a rounded rectangle — often 20–40px radius — filled edge-to-edge with color, framed by a thin border, and marked by a mono-uppercase timestamp on its left rail. Stories don't float on a grid; they stack on a dashed vertical rule like commits in a git log. Above that, a massive **"The Verge" wordmark** dominates the masthead in Manuka at hero scale, letting the reader know before any headline loads that this is editorial territory, not a template.

There is no "light mode" on the homepage — the dark canvas is the product, and the only time the palette inverts is when a single story tile takes a mint or yellow fill. The depth is almost entirely flat: **hairline 1px borders** (`#ffffff`, `#3cffd0`, or `#5200ff`) do the work that shadows would do on a Material-flavored site. Every container is either `#131313` with a 1px outline, a fully saturated accent block, or a slate-gray `#2d2d2d` secondary surface.

**Key Characteristics:**
- Near-black editorial canvas (`#131313`) as the default surface — no light mode on the homepage
- Acid-mint `#3cffd0` + ultraviolet `#5200ff` as hazard-tape accents, never quiet background wash
- Massive Manuka display headlines up to 107px — the single loudest type move in mainstream tech media
- Rounded pill-card everything: 20/24/30/40px corner radii, never square
- Fully saturated color-block story tiles (mint, purple, yellow, pink, orange, electric blue) on a dark page
- Timeline "StoryStream" feed with mono uppercase timestamps rather than a traditional magazine grid
- Flat depth — 1px borders in white, mint, purple do the work that shadows would do elsewhere

## Colors

### Primary (Brand Hazards)
- **Jelly Mint** (`{colors.accent}` — `#3cffd0`): The Verge's signature acid-mint accent. Used as CTA button fill, link underlines, active tab borders, and high-attention story-tile backgrounds. Treat it as the visual equivalent of neon safety paint — applied sparingly to the most important element on screen.
- **Verge Ultraviolet** (`{colors.ultraviolet}` — `#5200ff`): The complementary brand hazard. Used for secondary color-block tiles, promotional spans, and the occasional outlined button. Often applied at 0.9 alpha to soften its cathode intensity.

### Secondary & Accent
- **Console Mint Border** (`{colors.border-mint}` — `#309875`): A darker variant of the jelly mint used on card outlines and button borders where pure mint would over-saturate.
- **Deep Link Blue** (`{colors.link-hover}` — `#3860be`): The link *hover* color — the one moment blue appears on the site. It replaces mint/white/black on hover across every link style. At **3.17:1** on the canvas it misses AA for body-size links — a real failure of the live site, disclosed in Accessibility.
- **Focus Cyan** (`{colors.focus}` — `#1eaedb`): Reserved for button focus rings. Never shown outside a keyboard-focus state. **Extracted, not prescribed** — see Focus below.
- **Purple Rule** (`{colors.ultraviolet-rule}` — `#3d00bf`): A darker ultraviolet variant used as the vertical border on StoryStream `<li>` items. At 1.73:1 on the canvas it is a decorative spine, not a perceivable boundary.

### Surface & Background
- **Canvas Black** (`{colors.canvas}` — `#131313`): The default dark surface for the entire homepage. Almost-but-not-quite pure black — has just enough warmth to feel like a printed newsprint negative rather than an OLED void.
- **Surface Slate** (`{colors.surface-slate}` — `#2d2d2d`): Secondary card background, used when a story tile doesn't need to be a saturated color block.
- **Image Frame** (`{colors.border-image}` — `#313131`): The 1px border that wraps inline imagery. At 1.43:1 on the canvas this is **decoration only** and never the sole boundary of a control — see Accessibility.
- **Hazard White** (`{colors.text}` / `{colors.border-white}` / `{colors.surface-hazard-white}` — `#ffffff`): Used as story-tile fill, button border, and primary text. When white appears as a large block, it's an editorial decision — a "spotlight" on that tile. The one hex carries three jobs, so it is bound under three names: as ink, as hairline, and as the spotlight tile ground that `{components.card-spotlight-tile}` declares.
- **Absolute Black** (`{colors.on-accent}` / `{colors.black}` — `#000000`): Reserved for text on the mint/yellow/white tiles — the only place it appears.

### Neutrals & Text
- **Primary Text** (`{colors.text}` — `#ffffff`): Headlines and display text on the canvas.
- **Secondary Text** (`{colors.text-dim}` — `#949494`): Bylines, timestamps, photo credits. The mid-gray that anchors the metadata layer. Clears AA on the canvas (6.13:1) and on slate (4.54:1), **fails on a white spotlight tile** (3.03:1).
- **Muted Text** (`{colors.text-on-slate}` — `#e9e9e9`): Button text on dark slate buttons. Slightly off-white to reduce screen glare.
- **Inverted Text** (`{colors.text-inverted}` — `#131313`): Used only on accent tiles (mint, yellow, white) to keep contrast legible.

### Semantic & Accent
- **Focus Ring** (`{colors.focus}` — `#1eaedb`): Keyboard focus only.
- **Overlay Black** (`{colors.overlay-black}` — `rgba(0, 0, 0, 0.33)`): Subtle 1px ring used as the quiet shadow alternative on stacked cards. Over the canvas it renders as `#0d0d0d` (1.05:1) — atmosphere, not a boundary.
- **Dim Gray** (`{colors.pressed-gray}` — `#8c8c8c`): Active/pressed button background — the "pressed down" state.
- **Hover Fill** (`{colors.hover-fill}` — `rgba(255, 255, 255, 0.2)`) and **Pressed Fill** (`{colors.pressed-fill}` — `rgba(140, 140, 140, 0.87)`): the translucent button grounds the hover and active states swap in. Over the canvas they render as `#424242` and `#7c7c7c`.
- **Hover Ring** (`{colors.border-hover-ring}` — `#c2c2c2`): the 1px ring shadow the hover state adds.

### Borders

The Verge documents four boundary tones and two of them are frozen below the 3:1 threshold: `{colors.border-image}` (1.43:1 on the canvas) and `{colors.ultraviolet-rule}` (1.73:1). That is the real site — the hazard-tape identity puts its contrast budget into fills, not hairlines. **No parallel accessible boundary token is added**, because the palette already owns tones that do the job: `{colors.border-white}` (18.58:1 on the canvas, 13.77:1 on slate) is the hairline the system actually uses for cards and inputs, and `{colors.border-mint}` clears 3:1 on both dark grounds (5.20:1 / 3.85:1). Any boundary that must be perceivable — the edge of a text input, a focusable tile — is drawn in white or Console Mint. The image frame and the purple rail stay scoped to decoration, with their extracted `components:` bindings left exactly as found.

### Focus

- **Focus ring** (`{colors.focus}` — `#1eaedb`): **extracted, not prescribed.** Unusually for this collection, The Verge already documents a focus treatment: Focus Cyan, reserved for keyboard focus and never shown otherwise. It is kept as the ring for the file's dark grounds, where it measures 7.20:1 on `{colors.canvas}` and 5.33:1 on `{colors.surface-slate}`.
- **Focus ring, light grounds** (`{colors.focus-on-light}` — `#0500ff`): this file documents light signature surfaces as well as dark — the mint and white spotlight tiles — and one ring cannot serve both: Focus Cyan sits at 2.02:1 on a mint tile. The counterpart ring reuses `#0500ff`, the hex the file's own primary-button focus state already draws as a 1px border, so no new colour enters the palette. It measures 6.70:1 on mint and 8.57:1 on a white tile.
- The ultraviolet tile is the one ground **no** ring in this palette covers: Focus Cyan reaches 2.90:1 there and `#0500ff` only 1.14:1. On an ultraviolet fill the ring is two-tone — `{colors.focus}` with a mandatory 1px outer edge in `{colors.text}` (7.49:1 on ultraviolet). See Accessibility.

### Gradient System
The Verge uses **zero decorative gradients**. The only gradient-like treatment is the transition from a saturated accent story tile (mint/purple/yellow) back to the `#131313` canvas between rows. Color is applied in solid blocks, not as washes. This is a deliberate choice — the site's hazard-tape visual identity would dissolve if anything faded.

## Typography

### Font Family
- **Manuka** (Klim Type Foundry) — fallback: Impact, Helvetica. The signature display face for The Verge wordmark and feature headlines. A heavy-weight (900) industrial sans-serif with a condensed, almost-athletic stance. Runs at 60–107px on the homepage, never smaller.
- **PolySans** (PanGram Pangram / Nikolas Wrobel) — fallback: Helvetica, Arial. The UI and secondary headline workhorse. Covers weights 300 / 500 / 700 across the system — everything from kicker captions to body decks.
- **PolySans Mono** — fallback: Courier New, Courier. The monospaced sibling, used exclusively for ALL-CAPS labels: kickers, timestamps, category tags, button labels. This mono-uppercase usage is the second-most-identifiable Verge detail after Manuka.
- **FK Roman Standard** (Florian Karsten) — fallback: Georgia. A serif used sparingly for specific body/caption treatments (article excerpts, certain review pulls). Adds a "print-magazine" counterpoint to the PolySans stack.
- **Roboto** — fallback: `-apple-system`, `system-ui`. Utility UI font for widgets and legacy modules.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|---|---|---|---|---|---|---|
| Hero Wordmark / Display | Manuka | 107px / 6.69rem | 900 | 0.80 | 1.07px | The top-of-page "The Verge" logo and feature headlines |
| Secondary Display | Manuka | 90px / 5.63rem | 900 | 0.80 | — | Section-level feature headlines |
| Tertiary Display | Manuka | 60px / 3.75rem | 900 | 0.80 | — | Inline feature callouts |
| Large Headline | PolySans | 34px / 2.13rem | 700 | 1.00 | — | Section and module headlines |
| Heading Wide | PolySans | 32px / 2.00rem | 400 | 1.10 | 0.32px | Sub-heroes, promotional units |
| Heading Medium | PolySans | 24px / 1.50rem | 700 | 1.00 | — | Story tile headlines in the main feed |
| Heading Small | PolySans | 20px / 1.25rem | 700 | 1.00 | — | Compact tile headlines |
| Light Capitalized Label | PolySans | 19px / 1.19rem | 300 | 1.20 | 1.9px | Thin-weight capitalized eyebrows — a distinctive Verge move |
| All-Caps Label XL | PolySans | 18px / 1.13rem | 400 | 1.10 | 1.8px | UPPERCASE section kickers |
| Bold Body | PolySans | 16px / 1.00rem | 700 | 1.00 | — | Emphasis within decks |
| Body Relaxed | PolySans | 16px / 1.00rem | 500 | 1.60 | — | Long-form reading body |
| Inline Label | PolySans | 15px / 0.94rem | 400 | 1.20 | 0.15px | UI labels and secondary headlines |
| Body Compact | PolySans | 13px / 0.81rem | 400 | 1.60 | — | Secondary captions and decks |
| Eyebrow All-Caps | PolySans | 12px / 0.75rem | 400 | 1.30 | 1.8px | UPPERCASE kicker above tile headlines |
| Tag Label | PolySans | 12px / 0.75rem | 400 | 1.20 | 0.72px | UPPERCASE category tag |
| Caption Micro | PolySans | 11px / 0.69rem | 400 | 1.20 | 1.1px | UPPERCASE bylines |
| Meta Nano | PolySans | 10px / 0.63rem | 500 | 1.40 | 1.5px | UPPERCASE timestamp microtext |
| Mono Button Label | PolySans Mono | 12px / 0.75rem | 600 | 2.00 | 1.5px | UPPERCASE button text, very open leading |
| Mono Timestamp | PolySans Mono | 11px / 0.69rem | 500/600 | 1.20 | 1.1–1.8px | UPPERCASE StoryStream timestamps |
| Serif Body | FK Roman Standard | 16px / 1.00rem | 400 | 1.30 | -0.16px | Review decks, print-voice excerpts |
| Serif Caption | FK Roman Standard | 20px / 1.25rem | 400 | 1.20 | — | Magazine-style pull quotes |

Each row above is carried in the `typography:` frontmatter group, in table order:
`{typography.display-hero}`, `{typography.display-secondary}`, `{typography.display-tertiary}`,
`{typography.headline-large}`, `{typography.heading-wide}`, `{typography.heading-medium}`,
`{typography.heading-small}`, `{typography.label-light-caps}`, `{typography.label-caps-xl}`,
`{typography.body-bold}`, `{typography.body-relaxed}`, `{typography.label-inline}`,
`{typography.body-compact}`, `{typography.eyebrow-caps}`, `{typography.tag-label}`,
`{typography.caption-micro}`, `{typography.meta-nano}`, `{typography.mono-button}`,
`{typography.mono-timestamp}`, `{typography.serif-body}`, `{typography.serif-caption}`.
Every role carries a size, a weight and a line height. Letter-spacing is absent for seven roles
because the source states none for them, and `{typography.mono-timestamp}` keeps its
extracted ranges (weight 500–600, tracking 1.1–1.8px) rather than resolving to one value.

### Principles
- **Manuka is always the hero, never the UI.** If you see Manuka below 60px you're looking at a bug. It exists to *shout the brand*, not to label a button.
- **PolySans is the workhorse, PolySans Mono is its uniformed sibling.** Mono is used exclusively for UPPERCASE labels, timestamps, tags, and certain buttons. Lowercase mono doesn't exist in this system.
- **Thin-weight (300) capitalized headlines** are a signature Verge move. The 19–20px weight-300 with 1.9px tracking creates a "fashion magazine whisper" that contrasts with the 107px Manuka shout above it. This whisper-vs-shout contrast is the typographic fingerprint.
- **Letter-spacing has two registers**: positive (0.72–1.9px) for ALL-CAPS mono and sans labels, negative (`-0.16px`) for the rare serif appearances, barely-positive (0.32px, 1.07px) for massive display. Plain 0 letter-spacing is rare.
- **FK Roman Standard is the editorial exception**, not the rule. Reserve it for long-form print-voice moments — reviews, critic pulls, masthead essays. Never use it in UI.
- **Line heights are tight** (0.80–1.30) for every display and label, relaxed (1.60–2.00) only for reading body and mono button labels. The leading jump is intentional — it gives the page a "telegraph ticker" rhythm.

### Note on Font Substitutes
The 0.80 line-height on Manuka display (107px, 90px, 60px) assumes the **proprietary Manuka face from Klim Type Foundry**, which has aggressively tight vertical metrics designed for athletic stance at large sizes. If you substitute with wide-metric open-source condensed displays like **Anton**, **Oswald**, **Bebas Neue**, or **Archivo Black**, loosen display line-heights by approximately **+0.10 to +0.15** to prevent ascender/descender collisions (e.g., 0.80 → 0.95). PolySans substitutes (Space Grotesk, DM Sans, Hanken Grotesk) work at the token values without adjustment — their metrics are close enough. PolySans Mono substitutes (Space Mono, JetBrains Mono) and FK Roman substitutes (Newsreader, Literata) also work without adjustment.

## Layout

### Spacing System
- **Base unit**: 8px.
- **Scale**: 1, 2, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 20, 24, 25px.
- **Section padding**: 32–64px vertical between major feed sections. StoryStream items themselves are tighter — 12–16px gaps.
- **Card padding**: 20–32px interior. Feature cards expand to 40–48px.
- **Inline spacing**: kickers sit ~6–10px above headlines; headlines sit ~10–14px above decks; timestamps sit ~6–8px below decks.
- **Micro-scale**: The 2/4/5/6/9/10px values are used inside buttons, pills, and tight label clusters, not in the editorial grid.
- **Tokens**: the extracted scale is carried verbatim as `{spacing.space-1}` … `{spacing.space-25}`, plus the stated section and card values `{spacing.space-32}` (section padding, tightened card interior), `{spacing.space-40}` and `{spacing.space-48}` (feature-card interior, desktop container padding) and `{spacing.space-64}` (section padding at full desktop). Note that the declared 8px base unit does not actually generate this ladder — 1, 5, 9, 10, 14, 15 and 25px are not multiples of 8 — so the "base unit" is a description of the editorial rhythm, not a grid the micro values obey. Recorded in Known Gaps rather than corrected.

### Grid & Container
- **Max width**: ~1280–1300px (dembrandt detected breakpoints at 1200/1280/1300).
- **Column patterns**: a 12-column underlying grid that resolves into 3-column hero + 1-column StoryStream rail + feature panels. The homepage feels freeform because color-block tiles frequently span 2–3 columns on a whim.
- **Container padding**: 24px mobile / 48px desktop on the outer edges.
- **Gutters**: 16–24px between columns, tighter (8–12px) inside StoryStream items.

### Whitespace Philosophy
The Verge treats whitespace like a club DJ treats silence — as a dramatic reset between loud moments. The canvas is so dark and the accents are so saturated that even 32px of empty `#131313` between two tiles acts as a palette cleanser. The page is not airy like Apple or Stripe; it's **paced**, with loud hazard-color blocks interrupting stretches of near-black. Whitespace carries the rhythm, not the elegance.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | No border, no shadow | Default `#131313` canvas text |
| 1 | `rgba(0,0,0,0) 0px 0px 0px 0px inset` (placeholder) | Reset state for interactive elements |
| 2 | `1px solid #ffffff` or `#313131` hairline | Image frames and quiet card outlines |
| 3 | `1px solid #3cffd0` hairline | Active button outlines, focused story tiles |
| 4 | `1px solid #5200ff` hairline | Promotional/alternate state outlines |
| 5 | `rgba(0, 0, 0, 0.33) 0px 0px 0px 1px` | The single "atmospheric" ring — applied to layered cards |
| 6 | `0px -1px 0px 0px inset` (mint/black/white) | Active tab underline — a signature Verge move |
| 7 | Saturated accent fill (`#3cffd0`, `#5200ff`, white, yellow, pink) | Story-tile elevation via color, not shadow |

The Verge's depth philosophy is **color-as-elevation**. When something needs to stand out, it doesn't get a shadow — it gets a mint fill or a 1px hazard-color border. There are 14 shadow entries in the extracted tokens, but all of them are either inset underlines (0px -1px inset) or near-transparent 1px rings — none of them are traditional elevation shadows. The `#131313` canvas stays perfectly flat throughout, and hierarchy is carried by color saturation.

**Elevation is expressed one consistent way**: by changing the ground, not by mixing shadow and border at random. Levels 2–4 are the same device — a 1px hairline — in three colours, and level 7 is a fill. The only true shadow entries are `{shadow.reset}` (a zero-value placeholder), `{shadow.atmospheric-ring}`, `{shadow.hover-ring}`, `{shadow.pressed-ring}` and `{shadow.active-underline}`; none of them displaces light, and the first is not an elevation at all.

**Measured layer separation.** The step from `{colors.canvas}` to `{colors.surface-slate}` is **1.35:1** — a slate card on the page floor is barely a layer at all, which is why the system reaches for a hairline or a saturated fill instead. `{colors.surface-hazard-white}` against the canvas is 18.58:1, so a spotlight tile is the only layer the eye reads as raised without help. The atmospheric ring composites to `#0d0d0d` over the canvas (1.05:1) and is effectively invisible; treat it as texture, not depth.

### Decorative Depth
- **1px inset underline** on active tabs/nav links (mint, black, or white depending on context) — `{shadow.active-underline}`
- **Subtle `rgba(0, 0, 0, 0.33)` 1px ring** on stacked cards — the only effect that faintly resembles a shadow — `{shadow.atmospheric-ring}`
- **No gradients, no glows, no atmospheric blurs** anywhere. The hazard-tape aesthetic would break if anything faded softly.

## Shapes

### Border Radius Scale
- **2px** — inputs, small badges (feels like a typewriter tag)
- **3px** — inline images (just enough to soften against the canvas)
- **4px** — nested card images and small button variants
- **20px** — standard pill cards and color-block tiles
- **24px** — feature tile radius and primary button pill
- **30px** — large promotional buttons
- **40px** — outlined CTA pills (the loudest pill in the system)
- **50%** — avatar circles, icon buttons, and certain round badges

Eight discrete radius values — a **lot** for a single site. This is deliberate: the rhythm between 2px typewriter tags, 20px pill cards, and 40px outlined buttons creates a "nested scale" feel where every component announces its hierarchy through its corners.

The ladder is carried as `{rounded.tag}` 2px, `{rounded.image}` 3px, `{rounded.nested}` 4px, `{rounded.tile}` 20px, `{rounded.feature}` 24px, `{rounded.promo}` 30px, `{rounded.pill}` 40px and `{rounded.circle}` 50%. It is internally consistent but **bimodal**: a tight 2/3/4px cluster for form controls and nested imagery, then a 20/24/30/40px pill cluster for everything the reader touches, with nothing between 4px and 20px. No value sits outside its own cluster, and the gap is the system's own statement rather than a missing rung — the source calls square corners a break in the voice.

## Components

The Verge is unusually rich in extracted interaction state for this collection: hover, active/pressed, focus and the nav's selected treatment are all recorded with real values, and inputs carry an extracted error tone. Two states are genuinely **absent from the source** — `disabled` and `loading` — and are marked as not documented on each entry rather than invented. See Known Gaps.

### Buttons

**Primary — Jelly Mint Pill** (`{components.button-primary}`)
- Background: `#3cffd0` (Jelly Mint)
- Text: `#000000` (Absolute Black), PolySans 16px / 700 or PolySans Mono 12px / 600 UPPERCASE
- Border: none (pure fill)
- Border radius: `24px` — fully rounded pill
- Padding: `10px 24px`
- Outline: `none` at rest
- Hover: background shifts to `rgba(255, 255, 255, 0.2)` (translucent white), text stays black, adds a 1px `#c2c2c2` ring shadow
- Active: background `rgba(140, 140, 140, 0.87)`, opacity `0.5`, ring shadow `#8c8c8c`
- Focus: background `#1eaedb`, white text, 1px solid `#0500ff` border, translucent white focus ring
- Transition: ~180ms ease on background and shadow
- **States** (`{components.button-primary}`): default, hover (`{components.button-primary-hover}`), focus-visible (`{components.button-primary-focus}`), active / pressed (`{components.button-primary-pressed}`). Selected does not apply to a CTA
- Disabled and loading: not documented in the source for this or any other component
- **Hover** contrast warning: black on `{colors.hover-fill}` over the canvas renders `#000000` on `#424242` — **2.09:1**, a real AA failure of the live hover state. See Accessibility
- **Focus-visible** contrast warning: white on `{colors.focus}` is **2.58:1** — the extracted focus state fails AA for its own label. See Accessibility
- **Pressed**: `#000000` on the composited `#7c7c7c` fill is 5.03:1 and passes, but the extracted `opacity: 0.5` on top of it is applied to the whole control, so the rendered label is lighter than measured

**Secondary — Dark Slate Pill** (`{components.button-secondary}`)
- Background: `#2d2d2d` (Surface Slate)
- Text: `#e9e9e9` (Muted Text), PolySans 16px / 400
- Border: none
- Border radius: `24px`
- Padding: `10px 24px`
- Outline: `rgb(233, 233, 233) none 0px`
- Hover: same translucent white invert as primary — `rgba(255, 255, 255, 0.2)` bg, black text, 1px `#c2c2c2` ring
- Focus: same cyan focus treatment as primary
- **States**: default, hover, focus-visible, active / pressed — all inherited from the primary pill
- Disabled and loading: not documented in the source

**Tertiary — Outlined Mint** (`{components.button-tertiary-outlined}`)
- Background: transparent
- Text: `#3cffd0`, PolySans Mono 12px / 600 UPPERCASE, 1.5px tracking
- Border: `1px solid #3cffd0`
- Border radius: `40px` — larger pill for secondary outline style
- Padding: ~`10px 20px`
- Hover: inverts to mint fill, black text
- Transition: 150ms ease
- **States**: default, hover, focus-visible (`{colors.focus}` ring at a 2px offset, drawn outside the control), active / pressed
- Disabled and loading: not documented in the source
- The 1px `{colors.accent}` outline is the control's only boundary and measures 14.52:1 on the canvas — this is the system's one fully accessible hairline

**Outlined Ultraviolet (Promotional)** (`{components.button-outlined-ultraviolet}`)
- Background: transparent
- Text: `#5200ff` or `#ffffff`
- Border: `1px solid #5200ff`
- Border radius: `30px`
- Used for "Subscribe" or "Join the Stream" style promotional callouts
- **States**: default, hover, focus-visible, active / pressed
- Disabled and loading: not documented in the source
- The 1px `{colors.ultraviolet}` outline is **2.48:1 on the canvas** — below the 3:1 boundary minimum, so this control's edge is a brand gesture, not a perceivable boundary. Pair it with `{colors.border-white}` or a mint outline where the edge must be seen

**Pill Tag (Non-interactive)** (`{components.pill-tag}`)
- Background: saturated accent (`#3cffd0`, `#5200ff`, yellow, etc.)
- Text: black or white depending on background luminance
- Border radius: `20px` (tighter radius than buttons — this is the *text pill*)
- Font: PolySans Mono 11px / 600 UPPERCASE, 1.8px tracking
- Padding: ~`4px 10px`
- **States**: default only — this is a non-interactive label, as its own heading says. No interaction state applies to it at all

### Cards & Containers

**StoryStream Tile** (`{components.storystream-tile}`)
- Background: either `#131313` + 1px white border, OR a saturated accent fill (mint, purple, yellow, pink, orange, white)
- Border radius: `20px` (standard) or `24px` (feature)
- Border: `1px solid #ffffff` (on dark) or `0px 0px 1px solid #3cffd0` (on mint) or nothing (on saturated fill)
- Padding: ~24–32px interior
- Hover: no lift, no scale — the headline text color transitions from white to `#3860be` (deep link blue)
- Transition: 150ms ease on color only
- **States**: default, hover, focus-visible — where the whole tile is a link, the ring is drawn on the tile edge: `{colors.focus}` on dark fills, `{colors.focus-on-light}` on mint or white fills
- Active / pressed, selected, disabled and loading: not documented in the source
- **Hover** contrast warning: the hovered headline is `{colors.link-hover}` on `{colors.canvas}` — **3.17:1**. That clears the 3:1 large-text threshold for a 24px tile headline, but the same hover colour on a body-size link fails AA. See Accessibility

**Feature Card (Top Story)** (`{components.feature-card}`)
- Background: `#131313` with 1px hairline border, OR full-bleed color accent
- Border radius: `24px`
- Padding: 32px+
- Image inside: clipped to match the outer radius (`3px` or `4px` inner radius when nested)
- Hover: text color shift only; the image remains static
- **States**: default, hover, focus-visible
- Active / pressed, selected, disabled and loading: not documented in the source

**StoryStream Rail (Timeline)** (`{components.storystream-rail}`)
- A vertical dashed or solid rule (1px `#3d00bf` or `#ffffff`) runs along the left edge of each item, marking the timeline spine
- Timestamps sit on the left rail in PolySans Mono 11px / 500 / UPPERCASE / 1.1px tracking
- Each entry is a pill-cornered rectangle separated from its neighbors by 12–16px vertical gap
- **States**: default only — the rail is a decorative spine. Its 1px `{colors.ultraviolet-rule}` rule is **1.73:1** on the canvas; the white alternative is 18.58:1 and is the one to use where the spine must read

### Inputs & Forms (`{components.input}`, `{components.input-error}`)
- **Default**: `#131313` background, 1px solid `#ffffff` or `#949494` border, `2px` border radius (tight, newspaper-form feel), PolySans 15px text in `#ffffff`, placeholder in `#949494`.
- **Focus**: border transitions to `#3cffd0` (jelly mint) with optional `1px solid #5200ff` inner ring on deep focus. No glow.
- **Error**: border turns `#5200ff` (ultraviolet — used as error/alert accent here, not the usual red).
- **Transition**: ~150ms ease on border-color.
- **States**: default, hover (border lifts to `{colors.border-white}` where the default border is `#949494`), focus-visible (the mint border transition above is the extracted focus treatment, reinforced by the `{colors.focus}` ring), error. Active / pressed and selected do not apply to a text field
- Disabled and loading: not documented in the source
- **Error** boundary warning: a `{colors.ultraviolet}` border is 2.48:1 on the canvas, so the error state is not distinguishable by boundary contrast alone — pair it with a text message. The `#949494` default border is 6.13:1 and the white one 18.58:1, both perceivable

### Navigation (`{components.top-nav}`)

- **Top nav**: thin `#131313` bar with the Verge wordmark (Manuka) left-aligned, a search icon and a few UPPERCASE mono category links (12–14px, PolySans Mono, 1.5–1.8px tracking), and a single mint-pill CTA (usually "Subscribe") pinned right.
- **Wordmark**: massive on first scroll — the homepage treats the "The Verge" logo as a hero element, not a 32px corner logo.
- **Hover**: every link transitions from `#ffffff` to `#3860be` (deep link blue). No underline — it's a color-only response.
- **Active section**: marked by a 1px mint underline (inset box-shadow `0px -1px 0px 0px inset #3cffd0`)
- **Mobile**: the wordmark shrinks, category nav collapses into a hamburger drawer. Inside the drawer, links are mono-uppercase and stack with 16–20px gaps.
- **States**: default, hover, selected (the "Active section" mint inset underline above — `{shadow.active-underline}`), focus-visible (`{colors.focus}` ring at a 2px offset on the `{colors.canvas}` bar, 7.20:1)
- Active / pressed, disabled and loading: not documented in the source
- **Hover** contrast warning: a nav link hovering to `{colors.link-hover}` is **3.17:1** on the canvas, and these links are 12–14px mono — below AA. See Accessibility

### Image Treatment (`{components.image-frame}`)

- **Aspect ratios**: 16:9 dominates for hero and feature images, 4:3 for mid-feed, 1:1 for thumbnails and author avatars.
- **Corners**: always rounded to match the parent card — `3px`, `4px`, or inherit `20px` / `24px` from the tile.
- **Frame**: 1px `#313131` or `#ffffff` hairline around photography, giving a "contained Polaroid" feel.
- **Full-bleed**: only within the color-block tiles, where the image runs to the padded edge of the accent fill.
- **Hover**: static — no zoom, no scale, no opacity shift. The headline below is the only interactive response.
- **Lazy loading**: `loading="lazy"` on everything below the first fold; eager on the masthead hero only.
- **States**: default only where the image is not itself a link; a linked image takes its card's hover and focus-visible treatment
- Loading: not documented for any component. The `loading="lazy"` attribute above is an image-fetch hint, not an interaction state
- **Frame** contrast warning: the `{colors.border-image}` hairline is 1.43:1 on the canvas and 1.06:1 on `{colors.surface-slate}` — decorative only, never a control boundary

### StoryStream Timeline Item (Distinctive) (`{components.card-mint-tile}`, `{components.card-ultraviolet-tile}`, `{components.card-spotlight-tile}`)

- Vertical rail line (1px `#3d00bf` or `#ffffff` on `#131313`)
- Mono timestamp on the left in PolySans Mono 11px / UPPERCASE
- Pill-cornered body card (20px radius) with kicker, headline, and optional deck
- Stacked vertically with 12–16px gap, the rail continuing between them
- Often interleaved with full-bleed accent tiles that "break" the timeline rhythm for emphasis
- **Saturated tile grounds**, declared so their inks are measurable: mint (`{components.card-mint-tile}` — `{colors.text-inverted}` on `{colors.accent}`, 14.52:1), ultraviolet (`{components.card-ultraviolet-tile}` — `{colors.text}` on `{colors.ultraviolet}`, 7.49:1) and the white "spotlight" tile (`{components.card-spotlight-tile}` — `{colors.text-inverted}` on `{colors.surface-hazard-white}`, 18.58:1). The yellow, pink, orange and electric-blue tiles the Overview names have **no hex anywhere in this file** and so carry no token — see Known Gaps
- **States**: default, hover, focus-visible — ring polarity follows the fill, per Colors → Focus
- Active / pressed, selected, disabled, loading and error: not documented in the source

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve or choreography below was extracted from theverge.com; the values are the shared **Crisp** profile from `theme-audit/SPEC.md` section 5, carried verbatim in the `motion:` frontmatter group so every Crisp file in this collection behaves as a sibling.

Crisp is the right profile here, and the file's own prose is the evidence rather than a judgement call. The two transition values The Verge *does* document are **150ms** (story tiles, outlined buttons, input border-colour) and **~180ms** (the primary pill's background and shadow) — within 30ms of Crisp's `{motion.duration-base}` of 150ms. Its hover is explicitly "no lift, no scale", its images are "static — no zoom, no scale, no opacity shift", and the only response to a pointer anywhere in the document is a colour swap. That is Crisp's signature: a state change that reads as instant, with no entrance choreography. The saturated six-colour tile palette would otherwise argue for Playful, but rule 3 is a conjunction and this file fails its second half — the type voice is a 900-weight 107px shout, not light and informal, and nothing in the document springs, pops or overshoots.

One honest exception: the single *extracted* transition in this system animates `color`, not `opacity`. Colour is not a layout-triggering property, so it is kept as found; everything the audit adds below animates `transform` and `opacity` only, and never `width`, `height`, `top`, `left` or `margin`.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (link, tile headline, nav) | `{motion.duration-base}` | `{motion.ease-standard}` | `color` to `{colors.link-hover}` as extracted, plus `opacity` on the button fill swap — no lift, no scale | Colour and opacity swap kept, capped at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` to the extracted `0.5` over the `{colors.pressed-fill}` ground — no scale pop | Unchanged; already below `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring only | Ring appears instantly and is never suppressed |
| Page / route transition | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity` 0→1, `transform: translateY(8px)`→0 on the feed, never on the masthead | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Modal / drawer enter (mobile nav) | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateX(-100%)`→0 | Travel removed; scrim and panel fade at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown enter / exit | `{motion.duration-fast}` / `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-4px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| List enter (StoryStream items) | `{motion.duration-fast}`, staggered by `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(6px)`→0 — the timeline fills in like a log, never like a carousel | Stagger and travel removed; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-instant}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading | 1000ms, infinite | linear | `opacity` pulse between 1 and 0.4 on a `{colors.surface-slate}` placeholder block — never a layout-affecting skeleton | Loader frozen; a static `{colors.surface-slate}` placeholder remains |

Exit is always shorter than its matching entrance. Nothing animates on first paint in a way that delays content: the Manuka masthead paints at full opacity with no reveal, which is also the brand's own instruction to let the wordmark land before any headline loads. There is no brand ambience and no infinite animation other than the loader above.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: every translate, the StoryStream stagger, and the
     loader's opacity pulse (which freezes to a static placeholder). */
  /* Kept: colour and opacity transitions only, capped at
     {motion.duration-reduced} (100ms), plus the focus ring, which
     appears instantly and is never removed. */
  *, *::before, *::after {
    transition-property: color, background-color, opacity;
    transition-duration: 100ms; /* {motion.duration-reduced} */
    animation: none;
  }
}
```

## Accessibility

Every ratio below is computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. **The extracted brand values are frozen: the failures listed here are real failures of the live Verge interface, disclosed rather than corrected.** The headline findings are that the two loudest *interaction* states on the site — the primary button's hover and its own extracted focus fill — fail AA for their own labels, and that the hazard-tape identity spends its contrast budget on fills, leaving two of its four hairlines invisible.

### Measured contrast — key pairs

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `text` #ffffff on `canvas` #131313 | 18.58:1 | 4.5:1 | Pass |
| `text` #ffffff on `surface-slate` #2d2d2d | 13.77:1 | 4.5:1 | Pass |
| `text` #ffffff on `ultraviolet` #5200ff | 7.49:1 | 4.5:1 | Pass |
| `text-dim` #949494 on `canvas` | 6.13:1 | 4.5:1 | Pass |
| `text-dim` #949494 on `surface-slate` | 4.54:1 | 4.5:1 | Pass — with almost no margin |
| `text-dim` #949494 on `surface-hazard-white` #ffffff | 3.03:1 | 4.5:1 | **Fail — real brand failure.** Secondary Text is a dark-canvas tone; on a white spotlight tile use `{colors.text-inverted}` |
| `text-on-slate` #e9e9e9 on `surface-slate` | 11.34:1 | 4.5:1 | Pass |
| `text-inverted` #131313 on `accent` #3cffd0 | 14.52:1 | 4.5:1 | Pass |
| `text-inverted` #131313 on `surface-hazard-white` | 18.58:1 | 4.5:1 | Pass |
| `on-accent` #000000 on `accent` | 16.41:1 | 4.5:1 | Pass |
| `accent` #3cffd0 as ink on `canvas` | 14.52:1 | 4.5:1 | Pass — the Don't about mint text under 16px is about chromatic vibration, not contrast |
| `link-hover` #3860be on `canvas` | 3.17:1 | 4.5:1 | **Fail — real brand failure.** Deep Link Blue is the hover colour for *every* link on the site, including 12–14px mono nav links. It clears 3:1 only, so it is defensible at 18.66px/700 or 24px+ and fails everywhere else. See Needs approval in the report |
| `link-hover` #3860be on `surface-slate` | 2.35:1 | 4.5:1 | **Fail — real brand failure.** The same hover on a slate card is below even the 3:1 large-text threshold |
| `pressed-gray` #8c8c8c on `canvas` | 5.53:1 | 4.5:1 | Pass — as a fill it needs no ratio; recorded because the source lists it among the neutrals |
| `border-white` #ffffff on `canvas` | 18.58:1 | 3:1 | Pass — the system's primary hairline |
| `border-white` #ffffff on `surface-slate` | 13.77:1 | 3:1 | Pass |
| `border-mint` #309875 on `canvas` | 5.20:1 | 3:1 | Pass |
| `border-mint` #309875 on `surface-slate` | 3.85:1 | 3:1 | Pass |
| `border-mint` #309875 on `accent` #3cffd0 | 2.79:1 | 3:1 | **Fail — frozen extracted binding.** Console Mint Border is the documented outline for mint tile variants, and two neighbours on the same mint ramp cannot separate. Decorative there; use `{colors.text-inverted}` where a mint tile's edge must read |
| `border-hover-ring` #c2c2c2 on `canvas` | 10.43:1 | 3:1 | Pass |
| `border-white` #ffffff on `surface-hazard-white` #ffffff | 1.00:1 | 3:1 | **Fail, and a pair the site never renders.** The source says a spotlight tile takes "nothing (on saturated fill)" for a border, so a white hairline is never drawn on a white tile. Recorded because the white hairline and the white tile are the same extracted hex: where a spotlight tile does need an edge, `{colors.border-image}` #313131 measures 13.01:1 on it and `{colors.text-inverted}` 18.58:1 |
| `border-image` #313131 on `canvas` | 1.43:1 | 3:1 | **Fail — frozen decorative hairline.** The "contained Polaroid" image frame; never the sole boundary of a control |
| `border-image` #313131 on `surface-slate` | 1.06:1 | 3:1 | **Fail — frozen decorative hairline**, effectively invisible on the slate card it sits in |
| `ultraviolet` #5200ff on `canvas` | 2.48:1 | 3:1 | **Fail — frozen extracted boundary.** The promotional outlined button and the input error border are both 1px ultraviolet; below 3:1 the edge is a brand gesture, so pair it with white or with a text message |
| `ultraviolet` #5200ff on `surface-slate` | 1.84:1 | 3:1 | **Fail — frozen extracted boundary** |
| `ultraviolet-rule` #3d00bf on `canvas` | 1.73:1 | 3:1 | **Fail — frozen decorative hairline.** The StoryStream spine; the white alternative at 18.58:1 is the accessible one |
| `overlay-black` rgba(0,0,0,0.33) over `canvas` → #0d0d0d | 1.05:1 | — | Atmosphere, not a boundary; the single shadow-like effect in the system |
| `surface-slate` #2d2d2d against `canvas` | 1.35:1 | — | Layer separation, not a WCAG pair: a slate card barely lifts off the page floor |
| `surface-hazard-white` #ffffff against `canvas` | 18.58:1 | — | Layer separation: the spotlight tile is the only self-evident layer |

### Component pairs

| Component | Measured | Required | Verdict |
|---|---|---|---|
| `button-primary` — #000000 on #3cffd0 at 12px/600 | 16.41:1 | 4.5:1 | Pass |
| `button-primary-hover` — #000000 on `hover-fill` composited to #424242 | 2.09:1 | 4.5:1 | **Fail — real brand failure.** The extracted hover swaps a mint pill for translucent white over the near-black canvas and keeps black text. The label is barely legible in the hovered state; the nearest passing fix is to invert the label to `{colors.text}` on the hovered fill, which measures 10.05:1 on #424242. See Needs approval |
| `button-primary-focus` — #ffffff on `focus` #1eaedb | 2.58:1 | 4.5:1 | **Fail — real brand failure.** The extracted focus state fills the button with Focus Cyan and sets white text. The ring itself is fine (7.20:1 on the canvas); it is the label on the cyan fill that fails. `{colors.on-accent}` on #1eaedb would measure 8.13:1 — see Needs approval |
| `button-primary-pressed` — #000000 on `pressed-fill` composited to #7c7c7c | 5.03:1 | 4.5:1 | Pass, before the extracted `opacity: 0.5` on the whole control is applied |
| `button-secondary` — #e9e9e9 on #2d2d2d at 16px/700 | 11.34:1 | 4.5:1 | Pass |
| `pill-tag` — #000000 on #3cffd0 at 11px | 16.41:1 | 4.5:1 | Pass |
| `storystream-tile` — #ffffff on #131313 at 24px/700 | 18.58:1 | 3:1 large | Pass |
| `storystream-rail` — #949494 on #131313 at 11px | 6.13:1 | 4.5:1 | Pass |
| `feature-card` — #ffffff on #131313 at 60px | 18.58:1 | 3:1 large | Pass |
| `card-mint-tile` — #131313 on #3cffd0 at 24px/700 | 14.52:1 | 3:1 large | Pass |
| `card-ultraviolet-tile` — #ffffff on #5200ff at 32px | 7.49:1 | 3:1 large | Pass |
| `card-spotlight-tile` — #131313 on #ffffff at 24px/700 | 18.58:1 | 3:1 large | Pass |
| `input` — #ffffff on #131313 at 15px | 18.58:1 | 4.5:1 | Pass; its #949494 placeholder is 6.13:1 |
| `input-error` — #ffffff on #131313 | 18.58:1 | 4.5:1 | Pass as text; the error *boundary* is the failure above |
| `top-nav` — #ffffff on #131313 at 12px | 18.58:1 | 4.5:1 | Pass at rest, fails on hover (3.17:1) |
| `image-frame` — no text pair; its #313131 hairline is the failure above | 1.43:1 | 3:1 | **Fail — frozen decorative hairline** |

### Focus ring visibility on every surface this file defines

Two rings, both drawn as a 2px ring at a 2px offset **outside** the control, so each is judged against the surface behind it. `{colors.focus}` (#1eaedb) is **extracted** — Focus Cyan is the site's own documented keyboard-focus colour. `{colors.focus-on-light}` (#0500ff) is the counterpart for this file's light signature surfaces and reuses the hex the primary button's focus border already declares, so no new colour enters the palette. The pair is needed because this file documents both dark grounds and mint/white tile fills, and one ring cannot clear 3:1 on both.

| Surface it is drawn on | Ring | Measured | Required | Verdict |
|---|---|---|---|---|
| `canvas` #131313 | `focus` #1eaedb | 7.20:1 | 3:1 | Pass |
| `surface-slate` #2d2d2d | `focus` #1eaedb | 5.33:1 | 3:1 | Pass |
| `accent` #3cffd0 tile | `focus-on-light` #0500ff | 6.70:1 | 3:1 | Pass |
| `surface-hazard-white` #ffffff tile | `focus-on-light` #0500ff | 8.57:1 | 3:1 | Pass |
| `ultraviolet` #5200ff tile | `focus` #1eaedb | 2.90:1 | 3:1 | **Fail — no single ring in this palette covers the ultraviolet tile.** `#0500ff` is worse there (1.14:1). On an ultraviolet fill the ring is therefore two-tone: 2px `{colors.focus}` with a **mandatory** 1px outer edge in `{colors.text}`, which measures 7.49:1 against the tile. At the 0.9 alpha the source says ultraviolet is often applied at, the fill composites to #4c02e7 over the canvas and the plain cyan ring reaches 3.29:1 — so the gap is real only at full opacity, and the white edge is specified for both cases |
| `focus` #1eaedb button fill (its own extracted 1px border `#0500ff`) | `focus-on-light` | 3.32:1 | 3:1 | Pass — the extracted inner border separates from the cyan fill |

Over full-bleed photography inside a colour-block tile, which has no measurable colour, the ring is the same two-tone construction: `{colors.focus}` with a 1px outer edge in `{colors.text}` on dark imagery and in `{colors.canvas}` on light imagery.

### Minimum tap target

The source states a figure for one control only: primary pill buttons at "~44px minimum height (10px vertical padding + 16px text + 2px border) — meets WCAG AA", circle icon buttons at "40–44px", and mono uppercase nav links at "~28–32px tall", with its own instruction to "pad to 44px on mobile" for derivative work. Those are the document's claims, not measurements: this is a document with no rendered page, so **no tap target was measured here** and the 28–32px nav link is recorded as the source's own disclosed shortfall rather than as an audit finding.

### Reduced motion

`@media (prefers-reduced-motion: reduce)` removes every translate, the StoryStream stagger and the loader's opacity pulse, which freezes to a static `{colors.surface-slate}` placeholder. Colour and opacity transitions remain, capped at `{motion.duration-reduced}` (100ms). The focus ring is never animated away.

## Do's and Don'ts

### Do
- **Do** use `#131313` as the canvas for every view. There is no light mode.
- **Do** use Jelly Mint (`#3cffd0`) and Verge Ultraviolet (`#5200ff`) as hazard accents — buttons, borders, active states, and saturated color-block tiles.
- **Do** use Manuka exclusively at 60px+ for hero headlines. Treat anything smaller as a bug.
- **Do** round everything: 20px for cards, 24px for feature cards, 30–40px for pill buttons.
- **Do** use PolySans Mono for UPPERCASE labels, timestamps, kickers, and button text. Lowercase mono doesn't exist here.
- **Do** apply 1.5–1.9px letter-spacing to every ALL-CAPS label — this is a Verge signature.
- **Do** use saturated color-block tiles (mint, purple, yellow, pink, orange, white) to elevate a story — never a drop shadow.
- **Do** use `#3860be` (deep link blue) as the hover color on every link, regardless of base color.
- **Do** apply the StoryStream timeline rail (1px dashed/solid `#3d00bf` or white) on feed views.
- **Do** use thin-weight (300) PolySans at 19–20px with 1.9px tracking for "fashion-whisper" capitalized eyebrows — the contrast with the 107px Manuka shout is the whole voice.

### Don't
- **Don't** use a light background. The dark canvas is the product.
- **Don't** add `box-shadow` for elevation. Use 1px borders or saturated accent fills instead.
- **Don't** use square corners. Every interactive and content container is rounded.
- **Don't** use Manuka for UI, buttons, or body copy. It's strictly display.
- **Don't** use lowercase mono. PolySans Mono is always UPPERCASE.
- **Don't** let mint and ultraviolet appear as background washes — they're hazard accents, not canvas tints.
- **Don't** use gradients anywhere. The system is solid color blocks only.
- **Don't** introduce new accent colors outside the declared mint / purple / yellow / pink / orange tile palette.
- **Don't** pair Manuka with FK Roman Standard in the same headline cluster — Manuka is the only display shout, serif pulls are reserved for body moments.
- **Don't** use `#3cffd0` text on a `#131313` background at under 16px — the contrast vibrates at small sizes.
- **Don't** rely on `#313131` or `#3d00bf` as the only edge of anything a reader has to find — they measure 1.43:1 and 1.73:1 on the canvas. Use `{colors.border-white}` or `{colors.border-mint}` for a boundary that must be seen.
- **Don't** put `{colors.link-hover}` on body-size text — at 3.17:1 on the canvas the hover colour fails AA below 18.66px/700.
- **Don't** animate `width`, `height`, `top`, `left` or `margin` — `transform`, `opacity` and the extracted `color` swap only.
- **Don't** add an entrance animation to the masthead or to a StoryStream item that delays the headline. The feed fills in like a log, not like a carousel.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Small Mobile | <400px | Single column, Manuka hero scales down to ~48–54px, StoryStream rail collapses to inline timestamps |
| Mobile | 400–549px | Single column, color-block tiles stack full-width, nav is a hamburger drawer |
| Large Mobile | 550–767px | Still single column but padding opens up, tile radii stay at 20px |
| Tablet | 768–1023px | 2-column StoryStream with feature card spanning, wordmark shrinks ~50% |
| Small Desktop | 1024–1179px | Full 3–4 column editorial grid, mint pill CTA restored to nav |
| Desktop | 1180–1299px | Max padding, Manuka wordmark at full hero scale |
| Large Desktop | ≥1300px | Container caps at ~1280–1300px, whitespace expands at the margins, no further scaling |

The dembrandt sweep detected 26 intermediate breakpoints (1300 → 1280 → 1200 → 1181 → 1180 → 1179 → 1024 → 1023 → 901 → 900 → 897 → 896 → 890 → 769 → 768 → 620 → 605 → 600 → 550 → 549 → 530 → 426 → 425 → 400 → 320). The Verge tunes its grid at virtually every major device boundary — an unusually aggressive responsive strategy.

### Touch Targets
- Primary pill buttons are ~44px minimum height (10px vertical padding + 16px text + 2px border) — meets WCAG AA.
- Mono uppercase nav links are smaller (~28–32px tall) — for derivative work, pad to 44px on mobile.
- Circle icon buttons are 40–44px circles, touch-friendly.

### Collapsing Strategy
- **Nav**: wordmark scales from hero (Manuka 60–107px) to ~24–32px on mobile. Category links collapse to a hamburger drawer below 900px.
- **Grid**: 4-col → 3-col → 2-col → 1-col. Feature cards that span 2 columns on desktop reflow to full-width single-column on mobile.
- **Spacing**: section padding tightens from 64px → 32px → 20px. Tile interior padding tightens from 32px → 20px.
- **Type**: Manuka hero scales from 107px to ~48–54px on mobile. PolySans headlines scale from 34px → 24px. Mono labels stay pinned at 11–12px (they don't shrink further or they become unreadable).
- **Color tiles**: accent story blocks never lose saturation on mobile — they just reflow to full width.

### Image Behavior
- Responsive raster via `srcset`, aspect ratios preserved.
- No art-direction swaps — same crop scales across all viewports.
- `loading="lazy"` on everything below the fold, `eager` on the masthead hero.
- Images inside color-block tiles inherit the tile's inner radius (4px or 20px nested).

## Known Gaps

This file was one of the collection's ten legacy documents: it carried no frontmatter token block and used numbered headings (`## 1. Visual Theme & Atmosphere` and so on). The `colors`, `typography`, `spacing`, `rounded`, `shadow` and `components` groups above were built **only** from values already written in its prose, and the headings were renamed and reordered to the current contract — the Border Radius Scale moved out of Layout into `## Shapes` and Components moved after it, both verbatim. Nothing was invented to fill a column. What the prose does not contain is listed here.

- **Four of the six story-tile colours have no hex.** The Overview, the Components section and the Do's all name mint, purple, yellow, pink, orange and electric blue as the colour-block palette, but only mint (`#3cffd0`), ultraviolet (`#5200ff`) and white (`#ffffff`) are ever written as a value. Yellow, pink, orange and electric blue therefore carry **no token at all** rather than a guessed hex, and the Don't that forbids "new accent colors outside the declared mint / purple / yellow / pink / orange tile palette" cannot be enforced from this document. Four unmeasurable grounds also mean four unmeasurable ink pairs.
- **`disabled` and `loading` states are absent for every component.** No disabled fill, no disabled ink, no skeleton, no spinner, and no opacity value for a disabled control appears anywhere in the file. The Components section *marks* this rather than filling it. The `loading="lazy"` attribute in Image Treatment is an image-fetch hint and is **not** a loading state; a word-matching audit will read it as one, which is a false positive.
- **No motion values beyond two bare transition durations.** The source records "~180ms ease" on the primary button and "150ms ease" on tiles, outlined buttons and input borders — no easing curve, no choreography, no stagger, no page or modal transition, and nothing about reduced motion. The whole `motion:` group and the Motion & Animation section are the prescribed Crisp profile, as their first lines state.
- **The declared 8px base unit does not generate the spacing ladder.** 1, 5, 9, 10, 14, 15 and 25px are not multiples of 8. Both statements are extracted, so both are kept; the base unit describes the editorial rhythm, not the micro-scale.
- **Padding is given as ranges, not values**, for every container: "~24–32px interior", "32px+", "40–48px", "12–16px gap". The `components:` bindings pick the single stated value nearest each description (`{spacing.space-24}`, `{spacing.space-32}`) and the ranges stay in prose.
- **Hover is undefined for several components.** Pill tags, the StoryStream rail and the timeline item have no documented hover; images are explicitly static. Those entries say so rather than inheriting the link rule.
- **The secondary button's outline is recorded as `rgb(233, 233, 233) none 0px`** — a zero-width outline in the extraction, which is a computed-style artifact rather than a design value. It is not tokenised.
- **Letter-spacing is absent for seven type roles** and the mono timestamp keeps its extracted ranges (weight 500–600, tracking 1.1–1.8px). No single canonical value was picked.
- **No tap-target dimensions beyond the three the source states**, and none of them measured: this is a document, not a rendered page.
- **The tile border on a mint fill is recorded two ways in the source** — `0px 0px 1px solid #3cffd0` in Components and "Console Mint Border (#309875) on mint variants" in the Agent Prompt Guide. `{components.card-mint-tile}` binds the Agent Prompt Guide's reading, and its 2.79:1 failure is disclosed rather than re-pointed.
- **`{colors.text}`, `{colors.border-white}` and `{colors.surface-hazard-white}` are the same hex** under three names. That is not an alias added to satisfy a role pattern: the source gives Hazard White three distinct jobs — ink, hairline and spotlight tile ground — and only a declared ground is measurable.

## Agent Prompt Guide

### Quick Color Reference
- **Primary CTA**: "Jelly Mint (`#3cffd0`)"
- **Background (Canvas)**: "Canvas Black (`#131313`)"
- **Accent (Secondary Hazard)**: "Verge Ultraviolet (`#5200ff`)"
- **Heading Text**: "Hazard White (`#ffffff`)"
- **Body Text**: "Hazard White (`#ffffff`)" (primary) or "Muted Text (`#e9e9e9`)"
- **Secondary Text / Metadata**: "Secondary Text (`#949494`)"
- **Card Border**: "Hazard White (`#ffffff`)" hairline on dark, "Console Mint Border (`#309875`)" on mint variants
- **Link Hover**: "Deep Link Blue (`#3860be`)"

### Example Component Prompts
1. *"Create a StoryStream timeline item on a `#131313` canvas: a 20px-radius rectangle with a 1px solid `#ffffff` border, a PolySans Mono 11px / 600 / UPPERCASE / 1.1px tracking timestamp on the left rail, a 12px PolySans UPPERCASE kicker in mint (`#3cffd0`), and a 24px / 700 PolySans headline in white below. No shadow, no lift — hover only shifts the headline color to `#3860be`."*
2. *"Design a primary subscribe button with a Jelly Mint (`#3cffd0`) fill, black text in PolySans Mono 12px / 600 / UPPERCASE / 1.5px tracking, 24px border radius, 10px × 24px padding. Hover state shifts to `rgba(255, 255, 255, 0.2)` background with a 1px `#c2c2c2` ring shadow, 180ms ease."*
3. *"Build a feature hero with a 107px Manuka 900 headline in white with 1.07px letter-spacing and 0.80 line-height, a thin-weight 300 PolySans 20px capitalized kicker above with 1.9px tracking, on a `#131313` canvas with 64px vertical padding."*
4. *"Create a color-block accent tile filled with Verge Ultraviolet (`#5200ff`) at 0.9 alpha, 24px border radius, white text, a PolySans Mono 11px UPPERCASE category label with 1.5px tracking at the top, and a 32px PolySans 400 capitalized headline with 0.32px tracking below."*
5. *"Design a dark slate secondary button with a `#2d2d2d` background, `#e9e9e9` PolySans 16px text, 24px radius pill shape, 10px × 24px padding. Hover matches the primary button — translucent white `rgba(255, 255, 255, 0.2)` bg with black text."*

### Iteration Guide
When refining existing screens generated with this design system:
1. **Audit the canvas.** If you see a light background anywhere on the homepage, flatten it to `#131313`. There is no light mode.
2. **Audit corners.** Every rectangle should land on 2/3/4/20/24/30/40px or 50%. Square corners break the voice.
3. **Audit shadows.** Strip every `box-shadow` that isn't a 1px inset underline or a 1px hazard-color border. The Verge uses color for elevation, not shadow.
4. **Audit type roles.** Manuka only ≥60px. PolySans Mono only UPPERCASE. PolySans 300 at 19–20px should have 1.9px tracking. FK Roman only for body/magazine moments, never UI.
5. **Audit accent usage.** Mint and ultraviolet should appear as hazard accents — buttons, 1px borders, active underlines, saturated tile fills. If they're appearing as background washes or gradient fades, correct to solid blocks.
6. **Audit labels.** Every kicker, timestamp, category tag, and button label should be ALL CAPS with 1.1–1.9px letter-spacing. Missing tracking = missing voice.
7. **Audit link hover.** Every link, regardless of its base color, should hover to `#3860be` deep link blue with no underline. Any other hover color is drift.
