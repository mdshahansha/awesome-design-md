---
version: alpha
name: Vercel-Inspired-design-analysis
description: An inspired interpretation of Vercel's design language — a developer-platform brand whose surface is a stark black-and-ink duet on near-white canvas, broken at hero scale by a multi-color mesh gradient (cyan / blue / magenta / amber) that acts as the entire decorative system, paired with a custom geometric sans for headlines and a monospaced caption face for technical labels.

colors:
  primary: "#171717"
  on-primary: "#ffffff"
  ink: "#171717"
  body: "#4d4d4d"
  mute: "#888888"
  hairline: "#ebebeb"
  hairline-strong: "#a1a1a1"
  canvas: "#ffffff"
  canvas-soft: "#fafafa"
  canvas-soft-2: "#f5f5f5"
  link: "#0070f3"
  link-deep: "#0761d1"
  link-bg-soft: "#d3e5ff"
  success: "#0070f3"
  error: "#ee0000"
  error-soft: "#f7d4d6"
  error-deep: "#c50000"
  warning: "#f5a623"
  warning-soft: "#ffefcf"
  warning-deep: "#ab570a"
  violet: "#7928ca"
  violet-soft: "#d8ccf1"
  violet-deep: "#4c2889"
  cyan: "#50e3c2"
  cyan-soft: "#aaffec"
  cyan-deep: "#29bc9b"
  highlight-pink: "#ff0080"
  highlight-magenta: "#eb367f"
  gradient-develop-start: "#007cf0"
  gradient-develop-end: "#00dfd8"
  gradient-preview-start: "#7928ca"
  gradient-preview-end: "#ff0080"
  gradient-ship-start: "#ff4d4d"
  gradient-ship-end: "#f9cb28"
  selection-bg: "#171717"
  selection-fg: "#f2f2f2"
  focus: "#0070f3"

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

shadow:
  level-0: "none"
  level-1: "0 0 0 1px #00000014 inset"
  level-2: "0px 1px 1px #00000005, 0px 2px 2px #0000000a, 0 0 0 1px #00000014 inset"
  level-3: "0px 2px 2px #0000000a, 0px 8px 8px -8px #0000000a, 0 0 0 1px #00000014 inset"
  level-4: "0px 2px 2px #0000000a, 0px 8px 16px -4px #0000000a, 0 0 0 1px #00000014 inset"
  level-5: "0px 1px 1px #00000005, 0px 8px 16px -4px #0000000a, 0px 24px 32px -8px #0000000f, 0 0 0 1px #00000014 inset"

typography:
  display-xl:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 48px
    fontWeight: 600
    lineHeight: 48px
    letterSpacing: -2.4px
  display-lg:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 32px
    fontWeight: 600
    lineHeight: 40px
    letterSpacing: -1.28px
  display-md:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: -0.96px
  display-sm:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: -0.6px
  body-lg:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
    letterSpacing: 0px
  body-md:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-md-strong:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
  body-sm:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: -0.28px
  body-sm-strong:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: -0.28px
  caption:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  caption-mono:
    fontFamily: Geist Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  code:
    fontFamily: Geist Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
  button-md:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
  button-lg:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill-sm: 64px
  pill: 100px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 40px
  3xl: 48px
  4xl: 64px
  5xl: 96px
  6xl: 128px
  section: 192px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 64px
    padding: "{spacing.sm} {spacing.lg}"
  nav-link:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  nav-cta-signup:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.xs}"
    height: 28px
  nav-cta-login:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.xs}"
    height: 28px
  nav-cta-ask-ai:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.xs}"
    height: 28px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.pill}"
    padding: "0px {spacing.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.pill}"
    padding: "0px {spacing.sm}"
  button-primary-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "0px {spacing.xs}"
  button-secondary-sm:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "0px {spacing.xs}"
  tab-ghost:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill-sm}"
    padding: "0px {spacing.md}"
  icon-button-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
  card-marketing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  card-marketing-large:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  card-soft:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  template-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  code-editor-mockup:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  form-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.sm}"
    height: 40px
  form-input-sm:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.sm}"
    height: 32px
  form-input-lg:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.sm}"
    height: 48px
  badge-secondary:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "0px {spacing.xs}"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  pricing-card-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  logo-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.4xl} {spacing.lg}"
  feature-mesh-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.5xl} {spacing.lg}"
  showcase-band-light:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.5xl} {spacing.lg}"
  showcase-band-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.5xl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.4xl} {spacing.lg}"
  link-inline:
    textColor: "{colors.link}"
    typography: "{typography.body-md}"
  banner-marketing:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default tier card. Mirrors pricing-card chrome on canvas-soft surface with a hairline border."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-pricing-tier-featured:
    description: "Featured tier — polarity-flipped to ink primary with white text and white CTA."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-product-selector:
    description: "What's Included summary card — repurposed for the brand's GPU / inference / Pro feature tiers."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  ex-cart-drawer:
    description: "Subscription summary — line items per add-on (NOT a literal e-commerce cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row. Active state uses brand primary as a left-edge indicator bar."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  ex-data-table-cell:
    description: "Mirrors the brand's table chrome. Header uses caption-mono uppercase mono; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption-mono}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.xs} {spacing.sm}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Mirrors card-marketing-large chrome with form-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as card-marketing-large with Level 5 modal shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame. Generous padding on canvas-soft."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — flat-cornered card-marketing chrome with Level 4 shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"

---


## Overview

Vercel is a developer-platform brand — the page is a deployment dashboard's marketing surface, written for engineers who already know the syntax. It earns that posture with one of the cleanest stark systems on the web: near-white `{colors.canvas-soft}` body background, ink-near-black `{colors.ink}` text, a 200-step gray scale that gives every divider, border, and disabled state its own deliberate step. The only place the brand introduces colour at marketing scale is the multi-stop mesh gradient (`{colors.gradient-develop-start}` → `{colors.gradient-preview-end}` → `{colors.gradient-ship-start}` → cyan / magenta / amber) that floats in atmospheric backdrops, never miniaturised to a swatch. That gradient is the entire decoration system.

Type is the second decisive voice. The brand's own custom geometric sans (Geist) carries display, body, button — everything narrative — at weight 600 for display, 500 for buttons, 400 for body. A matching monospaced face (Geist Mono) carries technical labels: terminal mockups, code blocks, sometimes filename captions. Headlines are sentence-case with aggressive negative letter-spacing (`-2.4px` at 48 px hero) — the brand never letter-spaces positively, never goes uppercase outside of mono labels.

Surfaces use a four-step ladder: `{colors.canvas}` (pure white for cards), `{colors.canvas-soft}` 98% (the page body), `{colors.canvas-soft-2}` 95% (occasional inset region), `{colors.primary}` (the deep ink-near-black used as the polarity-flipped band when a section needs the dark mode treatment). Shadows are exceptionally subtle — every elevated card carries a stacked shadow built from `0px 1px 1px #00000005` + `0px 2px 2px #0000000a` + an inset border. Cards never float on heavy drop-shadow; they sit on the page held by hairline + soft glow.

**Key Characteristics:**
- A single black-ink primary CTA `{colors.primary}` carries every conversion target, paired with white-on-white `button-secondary` for the secondary action. The brand uses 100 px pill shape for marketing CTAs and a tight 6 px square shape for in-app nav buttons.
- A multi-stop mesh gradient (cyan-blue-magenta-amber) is the only decorative chrome — used at hero scale and inside feature-band atmospheric backdrops. It is the brand.
- Every section eyebrow and small label uses the monospace face `{typography.caption-mono}` or `{typography.code}`; everything else is in the geometric sans.
- Subtle stacked-shadow elevation — three offsets layered with 4-12 % black opacity — never a single heavy drop-shadow.
- A complete 100–1000 gray + blue + red + amber + green + teal + purple + pink colour scale exists as a system token set, but the marketing surface uses only the `100`, `1000`, and `700`-level tones; the rest stay in the design-system tokens for in-product surfaces.
- An "Active CPU" pricing rhythm: `pricing-card` lays out 3-up on the pricing page with `pricing-card-featured` (Pro tier) polarity-flipped to `{colors.primary}` against white-card siblings.

## Colors

### Brand & Accent
- **Ink** (`{colors.primary}` — `#171717`): The single primary CTA color. Black-near-pure ink that carries every Sign Up pill, every footer CTA, the dark-band polarity-flip. Used as text color throughout the page on light surfaces. (Resolved from `--ds-gray-1000`.)
- **Cyan** (`{colors.cyan}` — `#50e3c2`): A signature mint-cyan used in the brand gradient and inside Geist-system spotlight tokens. Visible inside the hero gradient stops.
- **Highlight Pink** (`{colors.highlight-pink}` — `#ff0080`): The brand's highlight magenta, used as the high-saturation stop in the preview-gradient pair.
- **Violet** (`{colors.violet}` — `#7928ca`): The deep purple used as the start of the preview-gradient and inside developer-console highlights.
- **Link Blue** (`{colors.link}` — `#0070f3`): The brand's primary link color and the legacy `--geist-success` semantic.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): The pure-white card / dialog / modal surface.
- **Canvas Soft** (`{colors.canvas-soft}` — `#fafafa`): The default page background — 98 % white. Almost every section sits on this tone.
- **Canvas Soft 2** (`{colors.canvas-soft-2}` — `#f5f5f5`): A slightly deeper inset surface for "code editor inner background", template-card hover states, and dropdown menus.
- **Hairline** (`{colors.hairline}` — `#ebebeb`): 1 px dividers — table rows, card borders, input borders. **Extracted and frozen, and it fails WCAG 1.4.11 as a boundary**: 1.19:1 on `{colors.canvas}` and 1.14:1 on `{colors.canvas-soft}`, against the 3.0:1 a non-text boundary needs. Scope it to decoration — row rules and card edges that only group content visually. Where a hairline is the *only* boundary of an interactive control (`form-input`, `nav-cta-ask-ai`, `icon-button-circular`), draw the boundary in `{colors.mute}` (3.54:1 / 3.40:1 — the palette already owns a passing tone, so nothing new is invented) and keep `{colors.hairline}` for the decorative rules.
- **Hairline Strong** (`{colors.hairline-strong}` — `#a1a1a1`): The 500-level gray, used as the slightly-stronger divider on light bands and as the deemphasised text color. Also extracted and frozen, and also short of 3.0:1 on light grounds (2.58:1 / 2.48:1) — it is not a substitute for `{colors.mute}` where a boundary must be seen. It does clear 3:1 on the dark band (6.94:1 on `{colors.primary}`).

### Text
- **Ink** (`{colors.ink}` — `#171717`): Every heading and body paragraph on light surfaces.
- **Body** (`{colors.body}` — `#4d4d4d`): Secondary text — sub-headings, body captions, nav-link inactive text, footer column body.
- **Mute** (`{colors.mute}` — `#888888`): Lowest-priority text — placeholder text, fine print, low-key labels. **Extracted and frozen, and it fails AA as body text**: 3.54:1 on `{colors.canvas}`, 3.40:1 on `{colors.canvas-soft}`, against 4.5:1. It clears the 3:1 bar for non-text, so it is the correct tone for a *boundary* that must be seen; as text, demote to `{colors.body}` (8.45:1) for anything a reader has to read, and keep `{colors.mute}` for placeholder glyphs inside a focused field.
- **On Primary** (`{colors.on-primary}` — `#ffffff`): All text on `{colors.primary}` surfaces (17.93:1).
- **Focus** (`{colors.focus}` — `#0070f3`): The focus ring. **Prescribed as a role binding, not a new brand colour** — it reuses the existing `{colors.link}` / `{colors.success}` hex unchanged, because a developer platform's ring should read as the same blue its links do. One mid-luminance ring serves all four grounds this file defines; see Accessibility for the measured ratios and the mandatory offset.

### Semantic
- **Success / Link** (`{colors.success}` — `#0070f3`): The brand's legacy success indicator doubles as the primary link color. Visible underline-on-hover for inline body links.
- **Link Deep** (`{colors.link-deep}` — `#0761d1`): The pressed / visited tone for inline links.
- **Link Bg Soft** (`{colors.link-bg-soft}` — `#d3e5ff`): Soft pastel blue fill for "what's new" pill banners and informational badges.
- **Error** (`{colors.error}` — `#ee0000`): Validation red for destructive actions and form errors.
- **Error Soft** (`{colors.error-soft}` — `#f7d4d6`): Soft pastel red for destructive-state backgrounds.
- **Error Deep** (`{colors.error-deep}` — `#c50000`): Pressed / deep destructive state.
- **Warning** (`{colors.warning}` — `#f5a623`): Caution / pending status indicator. **Fill and icon only.** Extracted and frozen, and at 2.03:1 on `{colors.canvas}` it fails AA by a wide margin as text — it is an amber at near-paper luminance. Set warning *text* in `{colors.warning-deep}` (5.12:1), which the palette already owns; `{colors.warning}` stays the status dot, the pending bar and the band fill. On the dark band it is fine (8.85:1 on `{colors.primary}`).
- **Warning Soft** (`{colors.warning-soft}` — `#ffefcf`) / **Warning Deep** (`{colors.warning-deep}` — `#ab570a`): Background + pressed variants. `{colors.warning-deep}` is also the warning text tone on light grounds, per the note above.

### Brand Gradient
The brand's signature decoration is a three-pair gradient stack:
- **Develop** (`{colors.gradient-develop-start}` `#007cf0` → `{colors.gradient-develop-end}` `#00dfd8`) — the blue-to-teal pair used to mark the "deploy" / "develop" rhythm.
- **Preview** (`{colors.gradient-preview-start}` `#7928ca` → `{colors.gradient-preview-end}` `#ff0080`) — the violet-to-pink pair used for "preview" surfaces.
- **Ship** (`{colors.gradient-ship-start}` `#ff4d4d` → `{colors.gradient-ship-end}` `#f9cb28`) — the coral-to-amber pair used for "ship" surfaces.

The three pairs collapse into a single multi-color mesh gradient when used as the hero atmospheric backdrop. Treat the gradient as one unified object — do not crop down to a single colour, do not reorder the stops, and do not miniaturise. Used at hero scale only.

## Typography

### Font Family
Two custom faces carry the entire system:

1. **A custom geometric sans** (extracted as `Geist`) for every display, body, button, link, and label. Weights 400 / 500 / 600 are the working set; the face never appears in 700 or heavier. Display sizes are tracked aggressively negative (`-2.4 px` at 48 px hero, `-1.28 px` at 32 px section); body stays at neutral or slightly-negative tracking.
2. **A custom monospaced face** (extracted as `Geist Mono`) for terminal mockups, code blocks, and small mono-caption labels — anything that wants to signal "technical." Weight 400 only at 12 – 13 px. Tracking neutral.

A condensed display sans (`Space Grotesk`) is loaded as a third face for occasional editorial moments but does not render as the primary face anywhere in the captured surfaces.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 48px | 600 | 48px | -2.4px | Hero headline ("Build and deploy on the AI Cloud."). |
| `{typography.display-lg}` | 32px | 600 | 40px | -1.28px | Section headlines ("Your frontend, delivered.", "A compute model for all workloads."). |
| `{typography.display-md}` | 24px | 600 | 32px | -0.96px | Card-cluster headlines, pricing-tier names. |
| `{typography.display-sm}` | 20px | 600 | 28px | -0.6px | Inline display micro-headings. |
| `{typography.body-lg}` | 18px | 400 | 28px | 0 | Lead paragraphs under section headlines. |
| `{typography.body-md}` | 16px | 400 | 24px | 0 | Default body paragraph. |
| `{typography.body-md-strong}` | 16px | 500 | 24px | 0 | Bolded inline body. |
| `{typography.body-sm}` | 14px | 400 | 20px | -0.28px | Secondary body, nav-link text, button-md labels. |
| `{typography.body-sm-strong}` | 14px | 500 | 20px | -0.28px | Nav CTA labels, table-row emphasis. |
| `{typography.caption}` | 12px | 400 | 16px | 0 | Footer secondary lines, badge labels. |
| `{typography.caption-mono}` | 12px | 400 | 16px | 0 | Section eyebrows and label captions that want a technical voice. |
| `{typography.code}` | 13px | 400 | 20px | 0 | Inline code, terminal mockups, command snippets. |
| `{typography.button-md}` | 14px | 500 | 20px | 0 | Small / nav-scale button labels. |
| `{typography.button-lg}` | 16px | 500 | 24px | 0 | Marketing-scale pill button labels. |

### Principles
- **Negative tracking is part of the voice.** Display sizes use aggressive `-2.4` to `-0.6` px tracking. Reverting to default tracking breaks the brand.
- **Sentence-case headlines, period-terminated.** Headlines like "Build and deploy on the AI Cloud." end with a deliberate period — that punctuation is part of the brand's voice.
- **Mono for the technical layer only.** Section eyebrows, code blocks, terminal mockups. Body paragraphs never set in mono.
- **Weight 600 is the display ceiling.** The geometric sans never appears at 700 / 800. The brand reads as a calmer system because of this.

### Note on Font Substitutes
The two primary faces are proprietary (custom-cut for the brand). Open-source substitutes:
- **Geometric sans** — *Inter* (400 / 500 / 600) is the closest stylistic match; `font-feature-settings: "ss01", "ss02"` enables the geometric alternates. *Satoshi* is a passable second choice.
- **Monospace** — *JetBrains Mono* (400) at 12 – 13 px matches the technical voice. *IBM Plex Mono* is the second-best option.

## Layout

### Spacing System
- **Base unit**: 4 px. The brand's `--geist-space` token is exactly 4 px and every captured value is a multiple of 4.
- **Tokens**: `{spacing.xxs}` 4 px · `{spacing.xs}` 8 px · `{spacing.sm}` 12 px · `{spacing.md}` 16 px · `{spacing.lg}` 24 px · `{spacing.xl}` 32 px · `{spacing.2xl}` 40 px · `{spacing.3xl}` 48 px · `{spacing.4xl}` 64 px · `{spacing.5xl}` 96 px · `{spacing.6xl}` 128 px · `{spacing.section}` 192 px.
- **Section padding**: marketing bands use `{spacing.4xl}` to `{spacing.5xl}` top/bottom. Hero bands stretch to `{spacing.section}` to give the mesh gradient room to breathe.
- **Card interior padding**: marketing cards sit at `{spacing.lg}` to `{spacing.xl}`; template-grid cards stay tighter at `{spacing.md}` because they sit in a denser grid.
- **Inline gap**: button rows, nav rows, and chip rows use `{spacing.sm}` to `{spacing.md}` between siblings. The brand's `--geist-gap` is exactly 24 px.

### Grid & Container
- **Max width**: ~1400 px (`--ds-page-width`); the legacy `--geist-page-width` is 1200 px and still appears on some marketing surfaces. Content centres with horizontal gutters of `{spacing.lg}` 24 px on desktop, `{spacing.md}` 16 px on mobile.
- **Column patterns**:
  - Three-feature row: 3-up at desktop, 1-up at mobile (rows like "Web Apps / Composable Commerce / Multi-tenant Platforms").
  - Tab pill row: 5-up centred row of `tab-ghost` pills.
  - Template-grid cluster: 5-up at desktop, scaling to 1-up at mobile.
  - Pricing tier grid: 3-up at desktop with the middle tier polarity-flipped.
  - Logo strip: ~5 logos wide, single row.

### Whitespace Philosophy
The mesh gradient does most of the heavy decorative lifting; whitespace separates the bands. Section spacing is generous — `{spacing.4xl}` to `{spacing.5xl}` between bands lets the gradient breathe. Inside a card, the headline/paragraph stack is tight (`{spacing.xs}` 8 px gap), then a wider gap before the CTA cluster. The page reads as engineered — large gaps + tight interior, never the other way around.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Full-bleed hero bands and the polarity-flipped dark sections. |
| Level 1 — Inset Hairline | `0 0 0 1px #00000014` inset 1 px border. | Default card chrome — the brand's universal "you can see this card" cue. |
| Level 2 — Subtle Drop | `0px 1px 1px #00000005, 0px 2px 2px #0000000a` plus inset hairline. | Slightly elevated cards (template-grid, marketing-card). |
| Level 3 — Soft Stack | `0px 2px 2px #0000000a, 0px 8px 8px -8px #0000000a` plus inset hairline. | The "medium" elevation — feature-grid cards. |
| Level 4 — Float Stack | `0px 2px 2px #0000000a, 0px 8px 16px -4px #0000000a` plus inset hairline. | "Large" elevation — pricing cards, callout panels. |
| Level 5 — Modal | `0px 1px 1px #00000005, 0px 8px 16px -4px #0000000a, 0px 24px 32px -8px #0000000f` plus inset hairline. | Modal / dialog surfaces and dropdown menus. |

The brand uses STACKED shadows — multiple small offsets layered to fake natural light — never a single 8-px-blur generic drop. Inset hairline rings are always added so the card edge stays crisp.

### Decorative Depth
- **Mesh gradient as atmospheric depth**: the hero's multi-stop gradient is the brand's only "atmospheric" effect — applied as a flat 2-D backdrop rather than a 3-D illustration.
- **Polarity-flipped dark band as section-depth**: switching the surface from `{colors.canvas-soft}` to `{colors.primary}` (the deep ink) is the brand's chief depth cue between bands.
- **Inset-shadow + drop-shadow combo**: the cards' combination of an inset 1 px ring and a multi-stop drop produces a "card sits on the page" effect without ever feeling material-heavy.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed hero / footer bands. |
| `{rounded.xs}` | 4px | The tightest step — inline code chips and the focus-ring corner on 6-px controls. No component in this file binds it; `nav-cta-signup` binds `{rounded.sm}` 6 px, not this. |
| `{rounded.sm}` | 6px | The brand's `--geist-radius` token — base UI radius for in-app buttons, form inputs, dropdown menus. |
| `{rounded.md}` | 8px | The brand's `--geist-marketing-radius` token — feature cards, template cards. |
| `{rounded.lg}` | 12px | Slightly larger card chrome (pricing-card variants). |
| `{rounded.xl}` | 16px | Largest card chrome — when a card hosts a hero image cap. |
| `{rounded.pill-sm}` | 64px | Tab-ghost pills inside the "AI Apps / Web Apps / Ecommerce / Marketing / Platforms" row. |
| `{rounded.pill}` | 100px | The marketing CTA pill — `button-primary`, `button-secondary`, "Start Deploying" pill. |
| `{rounded.full}` | 9999px | Icon-button circular containers, nav-link ghost pills. |

### Photography Geometry
- **Mesh gradient**: full-bleed 2-D atmospheric backdrop, never cropped to a frame; treated as the page's wallpaper.
- **Customer logos**: monochrome SVG, consistent 24 px height in a flex row.
- **Code editor mockup**: 16:10 dark rectangle, `{rounded.md}` corners.
- **Template thumbnails**: 16:9 landscape inside `{rounded.md}` chrome.
- **Showcase imagery**: 2:1 or 16:9 inside `{rounded.lg}` to `{rounded.xl}` chrome with a stacked shadow.

## Components

### Buttons

**`button-primary`** — the canonical 100-px-radius black pill, marketing scale.
- Background `{colors.primary}`, text `{colors.on-primary}`, label set in `{typography.button-lg}`, padding `0px {spacing.sm}` 12 px, shape `{rounded.pill}` 100 px. Renders ~48 px tall when paired with the marketing flex layout.

**`button-secondary`** — the white pill paired with the black primary inside marketing bands.
- Background `{colors.canvas}`, text `{colors.ink}`, same typography + padding as `button-primary`, shape `{rounded.pill}`.

**`button-primary-sm`** — the smaller-scale primary pill used inside nav and pricing-card CTAs.
- Background `{colors.primary}`, text `{colors.on-primary}`, label set in `{typography.button-md}` (14 px / 500), shape `{rounded.pill}`.

**`button-secondary-sm`** — the smaller-scale white pill paired with `button-primary-sm`.
- Background `{colors.canvas}`, text `{colors.ink}`, same typography + shape as `button-primary-sm`.

**`tab-ghost`** — the centred-row tab pill ("AI Apps / Web Apps / Ecommerce / Marketing / Platforms").
- Background `{colors.canvas}`, text `{colors.ink}`, label set in `{typography.body-sm}`, padding `0px {spacing.md}`, shape `{rounded.pill-sm}` 64 px.

**`icon-button-circular`** — the circular icon container (often a "?" or arrow inside).
- Background `{colors.canvas}`, dark icon, 1 px solid hairline border, shape `{rounded.full}`.

**Nav CTAs:**

**`nav-cta-signup`** — the small black "Sign Up" button in the nav row.
- Background `{colors.primary}`, text `{colors.on-primary}`, label `{typography.body-sm-strong}`, padding `0px {spacing.xs}`, height 28 px, shape `{rounded.sm}` 6 px (the brand's `--geist-radius`).

**`nav-cta-login`** — the white "Log In" button in the nav.
- Background `{colors.canvas}`, text `{colors.ink}`, same typography / height / shape as `nav-cta-signup`.

**`nav-cta-ask-ai`** — the small "Ask AI" button with a faint border.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` border (extracted as `0px solid rgb(235, 235, 235)`), same typography / height / shape.

### Cards & Containers

**`card-marketing`** — the canonical marketing feature card (3-up section cards).
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg}` 24 px, shape `{rounded.md}` 8 px (the `--geist-marketing-radius`). Carries Level 3 soft-stack shadow.

**`card-marketing-large`** — the larger marketing card used for "compute model" / "AI Gateway" callouts.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.xl}`, shape `{rounded.lg}` 12 px. Carries Level 4 float-stack shadow.

**`card-soft`** — the soft-tinted card used inside cluster groups (lighter than canvas-soft).
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.lg}`, shape `{rounded.md}`.

**`template-card`** — the deploy-template card in the "Deploy your first app" grid.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.md}` 16 px, shape `{rounded.md}` 8 px. Hosts a 16:9 thumbnail at the top.

**`code-editor-mockup`** — the dark code-preview surface inside marketing bands.
- Background `{colors.primary}`, text `{colors.on-primary}`, body in `{typography.code}` (13 px / Geist Mono), padding `{spacing.lg}` 24 px, shape `{rounded.md}` 8 px.

**`pricing-card`** — the default pricing-tier card.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.xl}` 32 px, shape `{rounded.lg}` 12 px. Inside: tier name in `{typography.display-md}`, price in `{typography.display-xl}`, feature list in `{typography.body-md}` rows, CTA at the bottom.

**`pricing-card-featured`** — the polarity-flipped "Pro" tier card.
- Background `{colors.primary}`, text `{colors.on-primary}`, same shape + padding as `pricing-card`. CTA inverts to `button-secondary-sm` (white pill on black card).

### Inputs & Forms

**`form-input`** — the canonical text input.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` border, body in `{typography.body-sm}` (14 px), padding `0px {spacing.sm}`, height 40 px (the brand's `--geist-form-height`), shape `{rounded.sm}` 6 px.

**`form-input-sm`** — small-height variant (32 px tall) for tight forms.
- Same as `form-input` but height 32 px (the `--geist-form-small-height`).

**`form-input-lg`** — large-height variant (48 px tall) for hero CTAs.
- Same as `form-input` but height 48 px (the `--geist-form-large-height`); body in `{typography.body-md}` 16 px.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas}`, text `{colors.ink}`, height 64 px (the brand's `--header-height`), padding `{spacing.sm} {spacing.lg}`. Layout: logo left, link row centre, "Ask AI / Log In / Sign Up" cluster right.

**`nav-link`** — the centred link row inside `nav-bar`.
- Text `{colors.body}`, set in `{typography.body-sm}`, padding `{spacing.xs} {spacing.sm}`, shape `{rounded.full}` (ghost pill — visible only on hover or active, but the radius is documented).

**`footer`** — the bottom 4-column nav.
- Background `{colors.canvas}`, text `{colors.body}`, padding `{spacing.4xl} {spacing.lg}`. Eyebrow column labels in `{typography.caption-mono}` (uppercase mono effect); link rows in `{typography.body-sm}`.

### Signature Components

**`hero-band`** — the white hero with the mesh gradient backdrop.
- Background `{colors.canvas}` (or `{colors.canvas-soft}` on some surfaces), text `{colors.ink}`, padding `{spacing.4xl} {spacing.lg}`. Inside: a small mono badge above the headline, the headline in `{typography.display-xl}` (sentence-case, period-terminated), a body lead in `{typography.body-lg}`, then a CTA row with `button-primary` + `button-secondary`. The mesh gradient sits behind, scaled to occupy roughly the top half of the band.

**`feature-mesh-band`** — the secondary section that hosts a mesh-gradient atmospheric backdrop with feature copy on top.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.5xl} {spacing.lg}`. Section headline in `{typography.display-lg}`; supporting body in `{typography.body-md}`.

**`showcase-band-light`** — a soft-canvas section ("Deploy your first app in seconds").
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.5xl} {spacing.lg}`.

**`showcase-band-dark`** — the polarity-flipped dark band ("A compute model for all workloads").
- Background `{colors.primary}`, text `{colors.on-primary}`, padding `{spacing.5xl} {spacing.lg}`. Section headline in `{typography.display-lg}` (white on black). Often contains a `code-editor-mockup` flush with the band.

**`logo-strip`** — the customer-logo wrapping row near the top of the page.
- Background `{colors.canvas}`, text `{colors.body}`, padding `{spacing.lg} {spacing.xl}`. Logos rendered as monochrome SVGs at consistent height.

**`badge-secondary`** — the small inline metadata pill ("New", "Beta", "Live").
- Background `{colors.canvas-soft}`, text `{colors.body}`, body in `{typography.caption}`, padding `0px {spacing.xs}`, shape `{rounded.full}`.

**`banner-marketing`** — the "Introducing X" announcement pill at the top of pages.
- Background `{colors.canvas-soft}`, text `{colors.body}`, body in `{typography.body-sm}`, padding `{spacing.xs} {spacing.sm}`, shape `{rounded.full}`.

**`link-inline`** — body-copy inline links.
- Text `{colors.link}` (`#0070f3`), body in `{typography.body-md}`, underlined.

### Examples (illustrative)

> Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`). Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently. `TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.
- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).
- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).
- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.
- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`


### Interaction States

Every component above is listed here with the states it supports. A surface that
is genuinely static says so rather than claiming states it does not have.
Hover and pressed are **paint-only** on this brand — a background-color, a
border-color or a text-colour step, never a scale pop or a lift. That is the
house style, not an omission: a tool-like identity signals state by changing
colour at speed, and a bounce would read as someone else's brand.

| Component | States | State treatment |
|---|---|---|
| `button-primary`, `button-primary-sm` | default, hover, focus-visible, active/pressed, disabled, loading | Hover lifts the ink fill one step toward `{colors.body}`; pressed settles to opacity 0.85 on the fill; focus-visible draws the `{colors.focus}` ring at 2 px with a 2 px offset; disabled drops the fill to `{colors.hairline}` with `{colors.mute}` label; loading swaps the label for a mono ellipsis while the control holds its footprint. |
| `button-secondary`, `button-secondary-sm` | default, hover, focus-visible, active/pressed, disabled, loading | Hover tints the fill to `{colors.canvas-soft}`; boundary steps from `{colors.hairline}` to `{colors.mute}`; otherwise as `button-primary`. |
| `nav-cta-signup`, `nav-cta-login` | default, hover, focus-visible, active/pressed, disabled | Same ladder at nav scale; the 6 px radius keeps the ring corner at `{rounded.xs}` + offset. |
| `nav-cta-ask-ai` | default, hover, focus-visible, active/pressed, disabled | Interactive boundary draws in `{colors.mute}`, not `{colors.hairline}` — see Accessibility. |
| `tab-ghost` | default, hover, focus-visible, active/pressed, selected | Selected is the live filter: fill `{colors.canvas-soft-2}`, label `{colors.ink}`, and the only persistent state in the row. |
| `icon-button-circular` | default, hover, focus-visible, active/pressed, disabled | Boundary in `{colors.mute}`; icon `{colors.ink}`, dropping to `{colors.mute}` when disabled. |
| `nav-link` | default, hover, focus-visible, selected | Hover reveals the `{rounded.full}` ghost pill in `{colors.canvas-soft}`; selected is the current route, label `{colors.ink}` instead of `{colors.body}`. |
| `link-inline` | default, hover, focus-visible, active/pressed | Underline is always on; hover deepens to `{colors.link-deep}`; pressed holds `{colors.link-deep}`. |
| `form-input`, `form-input-sm`, `form-input-lg` | default, hover, focus-visible, disabled, error | Boundary `{colors.mute}` at rest, `{colors.focus}` at 2 px when focused, `{colors.error}` with a `{colors.error-soft}` tint on error; disabled fills `{colors.canvas-soft}` and keeps the placeholder in `{colors.mute}`. |
| `card-marketing`, `card-marketing-large`, `card-soft` | default, hover, focus-visible, active/pressed | Interactive only where the whole card is a link: hover steps elevation from `{shadow.level-2}` to `{shadow.level-3}`, focus-visible rings the card, pressed returns to `{shadow.level-2}`. As a plain container the card has a default state and nothing else. |
| `template-card` | default, hover, focus-visible, active/pressed, loading | Loading is the thumbnail skeleton — a flat `{colors.canvas-soft-2}` block at the 16:9 frame. |
| `pricing-card`, `pricing-card-featured` | default, hover, focus-visible, selected | Selected is the chosen tier, marked by the polarity flip to `{colors.primary}` rather than by a border. |
| `badge-secondary` | default, error | Two states only: the neutral `{colors.canvas-soft}` pill, and an error variant on `{colors.error-soft}` with `{colors.error-deep}` text. It is a label, not a control. |
| `banner-marketing` | default, hover, focus-visible, active/pressed | A link dressed as a pill; hover deepens the fill one step to `{colors.canvas-soft-2}`. |
| `ex-app-shell-row` | default, hover, focus-visible, active/pressed, selected | Selected paints the left-edge indicator in `{colors.primary}` and the label in `{colors.ink}`. |
| `ex-data-table-cell` | default, hover, selected, loading | Row hover tints to `{colors.canvas-soft}`; selected adds a `{colors.link-bg-soft}` row fill; loading shows skeleton bars in `{colors.canvas-soft-2}`. |
| `ex-toast` | default, error, focus-visible | The dismiss control takes focus-visible; the error variant swaps the leading icon to `{colors.error}` and the text to `{colors.error-deep}`. |
| `ex-auth-form-card`, `ex-modal-card`, `ex-cart-drawer`, `ex-product-selector`, `ex-pricing-tier`, `ex-pricing-tier-featured` | default, loading, error | Container surfaces: the states belong to the controls inside them. Loading is a skeleton stack; error is an inline `{colors.error-deep}` message above the primary action. |
| `ex-empty-state-card` | default | One state. It is an illustration frame with a caption. |
| `hero-band`, `feature-mesh-band`, `showcase-band-light`, `showcase-band-dark`, `logo-strip`, `footer`, `code-editor-mockup`, `nav-bar` | default | Static layout surfaces. They carry no interactive states of their own; every state in them belongs to a control listed above. |

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was
not measured from the live site.** No duration, easing curve or transition
property was extracted; nothing in the captured surfaces records a timing
function. Every value below comes from the **Crisp** profile in
`theme-audit/SPEC.md` section 5, assigned because this is an infrastructure and
developer-tool identity: the state change should read as already finished, and
there is no entrance choreography anywhere in the brand. Treat the whole section
as a reasoned default, not a fact about the product, and replace it wholesale if
the real timings are ever captured.

Crisp fits this file on its own evidence: the decorative system is a single
static mesh gradient rather than a reveal, the display ceiling is weight 600,
elevation is three 1–2 px offsets instead of a lift, and the page's own voice is
a deployment dashboard. A slower profile would make a tool feel like a brochure.

### Timing tokens

`{motion.duration-instant}` 60 ms · `{motion.duration-fast}` 100 ms ·
`{motion.duration-base}` 150 ms · `{motion.duration-slow}` 220 ms ·
`{motion.duration-emphasis}` 300 ms · `{motion.stagger-step}` 20 ms ·
`{motion.duration-reduced}` 100 ms.
Easings: `{motion.ease-standard}` for state changes, `{motion.ease-enter}` for
things arriving, `{motion.ease-exit}` for things leaving.

### Interaction inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, nav links, cards, rows) | `{motion.duration-fast}` 100 ms | `{motion.ease-standard}` | `background-color`, `border-color`, `color` — paint only, no travel and no scale | Unchanged. There is no travel or scale to remove, so the colour step runs at the same 100 ms. |
| Press / active | `{motion.duration-instant}` 60 ms | `{motion.ease-exit}` | `opacity` on the fill (1 → 0.85) | Unchanged — opacity only, already inside `{motion.duration-reduced}`. |
| Focus-visible ring | `{motion.duration-instant}` 60 ms | `{motion.ease-standard}` | `opacity` on the ring layer; the ring itself is a `box-shadow` painted outside `{shadow.level-1}`'s inset hairline | Ring appears with no fade. It must never be delayed or suppressed. |
| Page / route transition | in `{motion.duration-base}` 150 ms, out `{motion.duration-fast}` 100 ms | in `{motion.ease-enter}`, out `{motion.ease-exit}` | `opacity` + `transform: translateY(4px)` on the content column only; the nav never moves | `opacity` only, `{motion.duration-reduced}` 100 ms, no translate. |
| Modal / drawer | in `{motion.duration-base}` 150 ms, out `{motion.duration-fast}` 100 ms | in `{motion.ease-enter}`, out `{motion.ease-exit}` | Modal: `opacity` + `transform: translateY(8px)`. Drawer: `opacity` + `transform: translateX(100%)`. Backdrop: `opacity` 0 → 1 | `opacity` only at `{motion.duration-reduced}` 100 ms; the panel appears in its final position. |
| Dropdown / menu | in `{motion.duration-fast}` 100 ms, out `{motion.duration-instant}` 60 ms | in `{motion.ease-enter}`, out `{motion.ease-exit}` | `opacity` + `transform: translateY(-2px)` | `opacity` only, no translate. |
| Toast | in `{motion.duration-base}` 150 ms, out `{motion.duration-fast}` 100 ms | in `{motion.ease-enter}`, out `{motion.ease-exit}` | `opacity` + `transform: translateY(8px)` | `opacity` only at `{motion.duration-reduced}` 100 ms; no travel. |
| List / grid enter | `{motion.duration-fast}` 100 ms per item, `{motion.stagger-step}` 20 ms apart, capped at 8 items | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px)` | `opacity` only, stagger 0, all items at once. |
| List / grid exit | `{motion.duration-instant}` 60 ms | `{motion.ease-exit}` | `opacity` only, no stagger | Unchanged — already opacity-only and under 100 ms. |
| Loading (skeleton) | `{motion.duration-emphasis}` 300 ms per half-cycle, infinite | `{motion.ease-standard}` | `opacity` 0.4 ↔ 1 on `{colors.canvas-soft-2}` blocks | Frozen. The skeleton holds a static 0.6 opacity; no pulse. |
| Loading (spinner) | 600 ms per revolution, linear, infinite | linear | `transform: rotate()` | Replaced by a static mono status label; no rotation. |

Exit is shorter than its matching entrance on every row. The two infinite
animations are loaders, which SPEC section 6 permits; this brand has no ambient
motion, and none should be added — the mesh gradient is a **static** backdrop
and animating it would contradict the identity.

Never animate `width`, `height`, `top`, `left` or `margin`. Travel is always a
`transform`, and a card that grows on hover is wrong for this brand in any case.
Nothing animates on first paint: the hero headline, the mesh gradient and the
CTA row render in place.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and scale travel; the skeleton pulse; the spinner
     rotation; every stagger (stagger-step becomes 0). */
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 100ms !important;   /* {motion.duration-reduced} */
    transform: none !important;
  }
  /* Kept: opacity fades at {motion.duration-reduced} 100 ms, every paint-only
     hover and press step, and the focus-visible ring, which is never
     suppressed or delayed. */
  .skeleton { animation: none; opacity: 0.6; }
  .spinner  { animation: none; }
}
```

What is removed: every `translateY` / `translateX`, every scale, the list
stagger, the skeleton pulse and the spinner rotation. What remains: opacity
fades capped at `{motion.duration-reduced}` 100 ms, all paint-only state
changes, and the focus ring.

## Accessibility

Ratios below are computed with WCAG 2.1 relative luminance from this file's own
frontmatter hexes. Tap-target and layout claims are read off documented token
values; nothing here was measured from a rendered page, and this document has no
running UI to measure.

### The honest summary

This is a near-monochrome brand whose entire boundary system sits below the
WCAG non-text threshold. `{colors.hairline}` `#ebebeb` is the card border, the
input border and the table rule, and it measures **1.19:1** on `{colors.canvas}`
— it is a grouping cue, not a visible boundary. The four-step surface ladder
does not rescue it: `{colors.canvas}` to `{colors.canvas-soft}` is **1.04:1**
and `{colors.canvas}` to `{colors.canvas-soft-2}` is **1.09:1**, so a card is
not distinguishable from the page by fill either. **The real brand fails WCAG
1.4.11 at every card edge and every input edge.** Say that out loud when
building on this document; do not assume the hairline is doing work it cannot do.

### Measured contrast

| Foreground / Background | Measured | Required | Verdict |
|---|---|---|---|
| `{colors.ink}` `#171717` on `{colors.canvas}` `#ffffff` | 17.93:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft}` `#fafafa` | 17.18:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.canvas-soft-2}` `#f5f5f5` | 16.44:1 | 4.5:1 | Pass |
| `{colors.on-primary}` `#ffffff` on `{colors.primary}` `#171717` | 17.93:1 | 4.5:1 | Pass |
| `{colors.body}` `#4d4d4d` on `{colors.canvas}` | 8.45:1 | 4.5:1 | Pass |
| `{colors.body}` on `{colors.canvas-soft}` | 8.10:1 | 4.5:1 | Pass |
| `{colors.mute}` `#888888` on `{colors.canvas}` | 3.54:1 | 4.5:1 | **Fail** — extracted and frozen. Passes the 3:1 non-text bar, so it is the correct *boundary* tone; as text it is placeholder-only. |
| `{colors.mute}` on `{colors.canvas-soft}` | 3.40:1 | 4.5:1 | **Fail** — same tone, same frozen value, measured on the page ground. |
| `{colors.hairline}` `#ebebeb` on `{colors.canvas}` | 1.19:1 | 3.0:1 | **Fail** — extracted and frozen. Decorative rules only; it is still bound as `borderColor` on `form-input`, `form-input-sm`, `form-input-lg`, `nav-cta-ask-ai`, `icon-button-circular` and `ex-pricing-tier`, exactly as extracted. Re-binding those is under Needs approval in the audit report. |
| `{colors.hairline}` on `{colors.canvas-soft}` | 1.14:1 | 3.0:1 | **Fail** — same, on the page ground. |
| `{colors.hairline-strong}` `#a1a1a1` on `{colors.canvas}` | 2.58:1 | 3.0:1 | **Fail** — extracted and frozen, and short of the bar by 0.42. Not a fix for the hairline. |
| `{colors.hairline-strong}` on `{colors.canvas-soft}` | 2.48:1 | 3.0:1 | **Fail** — same, on the page ground. |
| `{colors.hairline}` on `{colors.primary}` | 15.04:1 | 3.0:1 | Pass — the hairline only works as a boundary on the dark band. |
| `{colors.hairline-strong}` on `{colors.primary}` | 6.94:1 | 3.0:1 | Pass. |
| `{colors.warning}` `#f5a623` on `{colors.canvas}` | 2.03:1 | 4.5:1 | **Fail** — extracted and frozen, and it does not reach 3:1 even as large text. Fill and icon only; warning text uses `{colors.warning-deep}`. |
| `{colors.warning-deep}` `#ab570a` on `{colors.canvas}` | 5.12:1 | 4.5:1 | Pass — the warning text tone. |
| `{colors.link}` `#0070f3` on `{colors.canvas}` | 4.55:1 | 4.5:1 | Pass, with 0.05 to spare. Do not darken the canvas behind a link: on `{colors.canvas-soft}` it is 4.36:1 and on `{colors.canvas-soft-2}` 4.18:1, both below AA. Inline links on a tinted band use `{colors.link-deep}` (5.53:1 / 5.29:1). |
| `{colors.error}` `#ee0000` on `{colors.canvas}` | 4.53:1 | 4.5:1 | Pass by 0.03. On tinted grounds use `{colors.error-deep}` (5.96:1 / 5.71:1). |
| `{colors.highlight-pink}` `#ff0080` on `{colors.canvas}` | 3.77:1 | 4.5:1 | Gradient stop only — never set as text. Measured here so nobody promotes it to a label. |
| `{colors.cyan}` `#50e3c2` on `{colors.canvas}` | 1.60:1 | 4.5:1 | Gradient stop only. On `{colors.primary}` it is 11.19:1 and legible. |

### Focus ring

`{colors.focus}` `#0070f3` — the existing `{colors.link}` hex, bound to a new
role rather than added as a new brand colour. **One mid-luminance ring serves
every surface this file defines**, which is why there is no `focus-on-dark`
counterpart:

| Ring drawn on | Measured | Required | Verdict |
|---|---|---|---|
| `{colors.canvas}` `#ffffff` | 4.55:1 | 3.0:1 | Pass |
| `{colors.canvas-soft}` `#fafafa` | 4.36:1 | 3.0:1 | Pass |
| `{colors.canvas-soft-2}` `#f5f5f5` | 4.18:1 | 3.0:1 | Pass |
| `{colors.primary}` `#171717` (the polarity-flipped band, `code-editor-mockup`, `pricing-card-featured`) | 3.94:1 | 3.0:1 | Pass |

Geometry, which the ratios above depend on: **2 px solid `{colors.focus}`, 2 px
offset, drawn outside the control**, with the ring's corner radius set to the
control's radius plus 2 px. The offset matters twice over — it is what makes the
ring measurable against the *surface behind the control* rather than against the
control's own fill, which is what WCAG 2.2 Focus Appearance asks for, and it is
the only reason a single ring can serve both the white canvas and the ink band.
Requiring the ring to clear 3:1 against the black `button-primary` fill as well
would be arithmetically impossible. The ring is never suppressed, never replaced
by a colour change alone, and never animated away.

### Tap targets

Read from documented token heights; rendered size is not verifiable from this
document.

- `button-primary` / `button-secondary` render ~48 px tall in marketing bands —
  clears both 2.5.8 (AA, 24 × 24) and 2.5.5 (AAA, 44 × 44).
- `form-input` is 40 px and `form-input-lg` is 48 px; `form-input-sm` is 32 px.
- `nav-cta-signup`, `nav-cta-login` and `nav-cta-ask-ai` are **28 px tall with
  `0px {spacing.xs}` padding — horizontal padding only**. They clear 2.5.8 (AA)
  at 28 px but fall 16 px short of the 44 × 44 AAA floor, and nothing in the
  documented token set closes that gap. The honest fix is a 44 px hit area
  around the 28 px visual control on touch viewports; that is a prescription,
  not an extracted value.
- `badge-secondary` and `banner-marketing` are labels and links inside text
  flow, not standalone targets.

### Other

- **Reduced motion** is handled in Motion & Animation: all travel, scale,
  stagger and loader motion removed; opacity fades kept at
  `{motion.duration-reduced}` 100 ms; the focus ring always kept.
- **Selection colours** `{colors.selection-bg}` / `{colors.selection-fg}` give
  16.01:1 — the strongest pair in the file.
- **Colour is never the only signal.** Error states pair `{colors.error}` with
  text; `tab-ghost` selection pairs the fill change with a weight change; link
  underlines are always on, never hover-only.
- **The dark band** `showcase-band-dark` and `code-editor-mockup` invert cleanly:
  every ink on `{colors.primary}` clears AA except `{colors.body}` (2.12:1) and
  `{colors.violet}` (2.53:1), neither of which the file binds there.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (`#171717`) for primary CTAs across the page. Black ink IS the conversion target.
- Use `{rounded.pill}` 100 px for every marketing-scale CTA and `{rounded.sm}` 6 px for nav-scale buttons. The two pill scales coexist deliberately.
- Set every headline in `{typography.display-*}` weight 600, sentence-case, often period-terminated. Aggressive negative tracking is part of the voice.
- Use the brand mesh gradient as atmospheric decoration at hero scale only — never miniaturise it to an icon, never reduce to a single colour.
- Layer stacked shadows (multiple small offsets with inset hairline) rather than single heavy drops. The brand's elevation is calmer than Material.
- Cycle page surfaces in `{colors.canvas-soft}` → `{colors.canvas}` → `{colors.primary}` polarity-flipped bands; the dark band IS the depth cue.
- Set every code block and technical eyebrow in `{typography.code}` / `{typography.caption-mono}`. Mono is the voice of the platform.

### Don't
- Don't introduce a sixth accent colour. The brand operates with ink + gray + the three-pair gradient palette (develop / preview / ship); new accents flatten the voice.
- Don't render headlines in all-caps. Sentence-case + negative tracking is non-negotiable.
- Don't drop a single heavy drop-shadow on cards. The brand's elevation is built from stacked small offsets + inset hairline rings.
- Don't render the brand gradient at icon scale or in a single-colour reduced form. The gradient lives at hero scale only.
- Don't promote the geometric sans to weight 700. The brand's display ceiling is 600.
- Don't mix the marketing 100-px pill and the 6-px nav radius *inside one button cluster*. The two scales coexist on the same page by design — pill in the hero and the marketing bands, 6 px in the nav row — but a single row of sibling buttons picks one scale and stays there.
- Don't set body paragraphs in the mono face. The mono is for code + technical labels only.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 600px | Hero stacks; nav collapses to hamburger; 3-up feature grids drop to 1-up; tab pill row enables horizontal scroll. |
| Tablet | 600–959px | 3-up grids drop to 2-up; nav still horizontal. |
| Desktop | 960–1199px | Full 3-up grids; pricing 3-up. |
| Wide | 1200–1399px | Container caps at 1400 px content width. |
| Ultra-wide | ≥ 1400px | Content stays centred at 1400 px; bands stretch edge-to-edge in colour but content holds the max-width. |

### Touch Targets
The `button-primary` pill renders at ~32 px tall in nav and ~48 px tall in marketing contexts. Marketing CTAs meet 2.5.5 (AAA, 44 × 44) at all breakpoints. The nav controls do **not**: `nav-cta-signup`, `nav-cta-login` and `nav-cta-ask-ai` are documented at 28 px tall with `0px {spacing.xs}` padding, which is horizontal only — it adds nothing to the vertical hit area. They clear 2.5.8 (AA, 24 × 24) and fall 16 px short of the AAA floor. Closing that gap needs a 44 px hit area around the 28 px visual control on touch viewports; that is a prescription, not an extracted value. See Accessibility.

### Collapsing Strategy
- **Nav**: full link row + Ask AI / Log In / Sign Up pills at desktop. Collapses to logo + hamburger at mobile with the menu opening as a full-overlay.
- **Hero**: mesh gradient stays centred; headline + body stack vertically at all breakpoints (the brand doesn't use a split-hero pattern).
- **Three-feature row**: 3-up → 2-up → 1-up at the breakpoints above; cards keep their `{rounded.md}` 8 px shape across all viewports.
- **Pricing card grid**: 3-up at desktop, vertical stack at mobile with `pricing-card-featured` always sitting in the middle.
- **Template grid**: 5-up → 3-up → 2-up → 1-up. Each `template-card` keeps its 16:9 aspect on the image.

### Image Behavior
- **Mesh gradient**: rendered as inline SVG or canvas-painted gradient; scales fluidly with the hero container; never crops, never tiles.
- **Customer logos**: rendered as monochrome SVGs in the logo strip; consistent 24 px height.
- **Code editor mockup**: dark `{colors.primary}` rectangle with mono text rendered inside; treated as an image at the layout level.
- **Template thumbnails**: 16:9 landscape inside `{rounded.md}` card chrome; lazy-loaded; consistent grayscale palette in the placeholder state.

## Known Gaps

Everything in this list is either absent from the captured surfaces or
prescribed by the audit rather than extracted. Nothing here is a guess dressed
as a fact.

**Prescribed, not extracted**
- **The whole motion system.** No duration, easing curve or transition property
  was captured. The `motion:` group is the SPEC Crisp profile verbatim and the
  Motion & Animation section says so in its first line. If real timings are ever
  measured, they displace these values and the seam should be marked.
- **`{colors.focus}`.** The captured surfaces record no focus ring at all. The
  token reuses the existing `{colors.link}` hex `#0070f3`, so no new brand
  colour was invented, but the 2 px width, the 2 px offset and the radius rule
  are prescriptions. Vercel's real ring geometry is unknown.
- **The 44 px nav hit area.** The extracted nav control height is 28 px with
  horizontal padding only. The recommended 44 px touch hit area is a fix, not an
  observation.
- **Boundary re-scoping.** The decision to draw interactive boundaries in
  `{colors.mute}` rather than `{colors.hairline}` is this audit's prescription.
  The `components:` bindings still say `{colors.hairline}`, because that is what
  the real site renders; re-pointing them is a brand-owner decision and sits
  under Needs approval in `theme-audit/reports/A76-vercel.md`.
- **Hover and press treatments** in the Interaction States table. The brand's
  paint-only direction is inferred from its near-monochrome identity and its
  flat elevation, not recorded.

**Absent from the capture**
- **Dark mode.** `{colors.primary}` is a polarity-flipped *band* inside a light
  page, not a theme. There is no dark-mode canvas, no dark-mode hairline and no
  dark-mode gray ladder in this file, so no dark-theme contrast ladder can be
  stated. A real dark theme would need its own `canvas-dark` / `hairline-dark`
  tones and its own ring check.
- **The full 100–1000 scale.** The Overview says a complete gray / blue / red /
  amber / green / teal / purple / pink ladder exists in the design-system
  tokens. Only the tones listed in `colors:` were captured; the intermediate
  steps are not in this file and must not be interpolated.
- **No `green`/`teal` semantic token** despite the Overview naming those
  ladders; `{colors.success}` is the brand's blue, which is a real quirk of the
  system rather than an omission.
- **Gradient geometry.** Stop positions, angle and mesh node placement for the
  signature gradient are not recorded — only the six stop colours.
- **Shadow opacity source.** The `shadow:` group transcribes the Elevation &
  Depth table's 8-digit hexes as captured. Whether the real system expresses
  them as `rgba()` with named opacity tokens is unknown.
- **`{rounded.xs}` 4 px and `{rounded.xl}` 16 px** are in the ladder but no
  component in this file binds either one.
- **Legacy boilerplate.** The Examples note still refers to `TO_FILL` markers
  and `scripts/derive-examples-block.mjs`; no `TO_FILL` marker remains in the
  file. The sentence is kept rather than rewritten because the Examples block
  is auto-generated upstream.

**Not computable from a document**
Overlap, horizontal overflow, clipping, rendered tap-target size, frame rate and
layout shift need a running page. No claim about any of them appears above; the
tap-target figures are documented token heights, not measurements.

**Known contrast failures** are not gaps — they are disclosed with measured
ratios in Accessibility. The headline fact bears repeating: this brand's
boundary system (`{colors.hairline}` at 1.19:1) and its four-step surface
ladder (1.04:1 between steps) both sit below the WCAG non-text threshold, and
that is true of the real product, not of this document.
