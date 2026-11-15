---
version: alpha
name: 1win Analysis
description: An analysis of 1win's design language — a near-black crypto casino and sportsbook built on Inter at heavy weights, where a vivid green action color and an electric blue secondary carry every CTA across dense, full-bleed game-tile rails, promo cards, and live betting panels on a flat dark-grey surface ladder.

colors:
  primary: "#00b24b"
  secondary: "#0075ff"
  on-primary: "#ffffff"
  canvas: "#141415"
  surface: "#2e3035"
  hairline: "#2d2f33"
  hairline-strong: "#77797d"
  ink: "#f0f2f5"
  muted: "#9aa1b1"
  faint: "#53575f"
  black: "#000000"
  focus: "#4da3ff"

typography:
  display:
    fontFamily: Inter
    fontSize: 33px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: 0
  heading:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0
  title:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  ui:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 10px
  xl: 12px
  card: 16px
  full: 999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  xxl: 24px
  xxxl: 32px

# Prescribed to match 1win's visual identity (Calm profile) — not measured from the live site.
motion:
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 600ms
  ease-standard: cubic-bezier(0.4, 0, 0.6, 1)
  ease-enter: cubic-bezier(0, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 40ms

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: "8px 12px"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: "8px 12px"
  button-tertiary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: "8px 12px"
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: "0px 8px"
  pill-badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "0px 4px"
  pill-outline:
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    rounded: "{rounded.full}"
    padding: "0px 8px"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "8px 16px"
  sidebar-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    padding: "8px"
  game-tile:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
  hero-banner:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "24px"
  promo-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "16px"
  feature-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "16px"
  feature-card-elevated:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "16px"
  bet-odds-button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.md}"
    padding: "8px 12px"
  betslip-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "16px"
  text-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "8px 12px"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    padding: "24px"

  # ─── Examples (illustrative) — kit-mirror surfaces ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.surface}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body}"
    cellPadding: "{spacing.sm} {spacing.md}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "{spacing.xxl}"
    captionTypography: "{typography.body}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body}"

---


## Overview

1win is a crypto casino and sportsbook that runs almost entirely on a near-black canvas (`{colors.canvas}` — #141415), a flat, slightly cool dark field that lets thousands of vibrant game thumbnails do the shouting. The chrome around the content is deliberately quiet: dark-grey surfaces (`{colors.surface}` — #2e3035), faint translucent hairlines, and off-white text (`{colors.ink}` — #f0f2f5). Against that restraint, two action colors carry the entire interactive layer — a vivid green (`{colors.primary}` — #00b24b) on the "Registration" CTA and every primary confirm, and an electric blue (`{colors.secondary}` — #0075ff) on "Log In", links, the "Show more" pill, active tabs, and bet highlights.

The layout is a high-density product surface, not a marketing page. A fixed left icon rail holds category navigation; the main column is a long stack of horizontally-scrolling rails — "Top games", "Slots", "Originals", game providers — each a row of full-bleed, brightly-illustrated `game-tile` thumbnails. Promotional bonuses ride in gradient-rich `hero-banner` cards at the top, and the sportsbook adds match rows with `bet-odds-button` chips and a right-hand `betslip-panel`. Typography is Inter set at heavy weights only (600 and 800) — even body copy is semibold — which gives the dense UI a punchy, app-like confidence rather than an editorial calm.

Color discipline is the key to reading this brand correctly: the loud purples, reds, ambers, and violets that fill the screen all live *inside* game artwork and bonus-card illustrations — they are content, not chrome. The system itself is monochrome dark plus exactly two signals: green for "go / win / register" and blue for "secondary / navigate / live". Everything structural is built from the dark surface ladder and those two accents.

**Key Characteristics:**
- Near-black `{colors.canvas}` foundation with a flat `{colors.surface}` card/tile ladder — depth comes from surface shifts and faint `{colors.hairline}` borders, not heavy shadow.
- Two-signal action system: green `{colors.primary}` for primary CTAs (Registration, confirm) and blue `{colors.secondary}` for secondary actions, links, and live/betting highlights.
- Inter at heavy weights only (600 / 800) — even `{typography.body}` is semibold, giving the dense UI an app-like punch.
- Content-forward game rails — full-bleed `game-tile` artwork supplies all the saturation; the surrounding frame stays monochrome dark.
- Pill language for badges and status (`{rounded.full}`), modest `{rounded.lg}`–`{rounded.xl}` on buttons, and `{rounded.card}` (16px) on tiles, promo cards, and panels.
- A left icon `sidebar-rail` + dense horizontally-scrolling rails define the shell, closer to a native app than a website.

## Colors

> Source pages analyzed: home, promotions, betting, vip-club.

### Brand & Accent
- **Action Green** (`{colors.primary}` — #00b24b): The primary action color — the "Registration" CTA, primary confirms, betslip place-bet, and section accent icons. The brand's "go / win" signal.
- **Electric Blue** (`{colors.secondary}` — #0075ff): The secondary action — "Log In", text links, the "Show more" pill, active tabs, badges, and live/betting highlights.
- **On Primary** (`{colors.on-primary}` — #ffffff): White text/icons on the green and blue fills. **This is how 1win really ships, and it fails AA:** white on `{colors.primary}` measures **2.81:1** and white on `{colors.secondary}` measures **4.21:1** — both below the 4.5:1 body-text minimum. Neither hex is altered here because both are brand identity. See Accessibility for the measured table and the two defensible routes (switch accent labels to `{colors.black}`, or restrict white-on-accent to 18px+/700 type where 3:1 applies).

### Surface
- **Canvas** (`{colors.canvas}` — #141415): The page background and the fill of the nav and `sidebar-rail` — a flat near-black.
- **Surface** (`{colors.surface}` — #2e3035): Cards, game tiles, promo cards, betslip panels, utility buttons, and input fields — the single elevated dark step.
- **Hairline** (`{colors.hairline}` — #2d2f33): The faint 1px divider/card border, a translucent cool-grey edge. Measured contrast against `{colors.canvas}` is **1.37:1**, so this is a decorative edge only — it does not meet the 3:1 non-text minimum and must not be the sole indicator of a control's boundary.
- **Hairline Strong** (`{colors.hairline-strong}` — #77797d): *Prescribed, not extracted.* The accessible boundary value for any edge that must be perceivable on its own — input outlines, `pill-outline`, `bet-odds-button`, table rules. 4.22:1 on `{colors.canvas}`, 3.03:1 on `{colors.surface}`.

### Text
- **Ink** (`{colors.ink}` — #f0f2f5): Primary text, the wordmark, and headings — a soft off-white.
- **Muted** (`{colors.muted}` — #9aa1b1): Secondary labels, inactive nav glyphs, footer text.
- **Faint** (`{colors.faint}` — #53575f): Tertiary/placeholder text and disabled labels. 2.54:1 on `{colors.canvas}` — below AA for body text. Acceptable for genuinely disabled controls (exempt from WCAG 1.4.3); for live placeholder text use `{colors.muted}` instead.
- **Black** (`{colors.black}` — #000000): Maximum-contrast text used on the brightest accent fills and light promo surfaces. 7.47:1 on `{colors.primary}` — the accessible pairing for green fills.

### Focus
- **Focus Ring** (`{colors.focus}` — #4da3ff): *Prescribed, not extracted.* A lifted step of the brand electric blue, chosen so the ring stays recognisably 1win-blue while clearing the two accent fills it may sit on. **7.01:1 against `{colors.canvas}`** and 5.03:1 against `{colors.surface}`. Drawn as a 2px ring with a 2px `{colors.canvas}` offset, so the perceived boundary is always ring-against-near-black (7.01:1) regardless of whether the focused control is filled green, blue, or grey — the ring alone against `{colors.primary}` is only 1.07:1, so the offset is mandatory, not decorative.

## Typography

### Font Family
The entire system is set in **Inter** (`Inter, sans-serif`), and only at heavy weights — **600 (semibold)** and **800 (extrabold)**. There is no regular-weight body text; even running copy is semibold, which is what gives the dense, data-heavy interface its punchy, native-app feel. Headlines and bonus figures use 800; everything functional uses 600.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display}` | 33px | 800 | 1.1 | 0 | Hero / page headlines (bonus figures, "Promotions") |
| `{typography.heading}` | 20px | 800 | 1.2 | 0 | Section + card titles |
| `{typography.title}` | 16px | 600 | 1.3 | 0 | Game titles, row headers, outlined pills |
| `{typography.body}` | 14px | 600 | 1.4 | 0 | Default body, button labels |
| `{typography.ui}` | 13px | 600 | 1.3 | 0 | Inline UI text, odds, metadata |
| `{typography.caption}` | 12px | 600 | 1.3 | 0 | Badges, chips, micro-labels |

### Principles
Hierarchy is built from size and the 600↔800 weight jump, never from a light/regular contrast. The heavy floor keeps small UI text legible against the dark, busy backdrop and matches the high-energy gambling context.

### Note on Font Substitutes
Inter is an open-source Google Font, so no substitution is needed. If a fallback is required, any grotesque with a strong semibold (e.g. Manrope, Geist) preserves the heavy-weight character; keep body at 600+ to retain the app-like density.

## Layout

### Spacing System
- **Base unit**: 8px.
- **Tokens (front matter)**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 20px · `{spacing.xxl}` 24px · `{spacing.xxxl}` 32px
- Controls run tight — `{spacing.sm}`×`{spacing.md}` (8×12px) is the recurring button padding; cards and panels use `{spacing.lg}`–`{spacing.xxl}` (16–24px) interiors.

### Grid & Container
The shell is a fixed left icon `sidebar-rail` plus a fluid content column. Discovery uses horizontally-scrolling rails (carousels) of `game-tile` thumbnails rather than wrapping grids; the promotions page uses a 2-up card grid, and the sportsbook uses full-width match rows with a docked right-hand `betslip-panel`.

### Whitespace Philosophy
Density is the point — tiles pack close together to maximize the number of games in view, and the dark canvas itself does the separating between rails. Vertical gaps between labeled rails are modest; the brightness step between a tile and the canvas, plus a faint `{colors.hairline}`, supplies most of the structure.

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Left rail collapses to a bottom/hamburger nav; rails shorten; betslip becomes a bottom sheet |
| Tablet | 768–1023px | Condensed rail; fewer tiles per rail; 2-up promo grid retained |
| Laptop | 1024–1439px | Full rail + multi-tile rails |
| Desktop | ≥ 1440px (up to 1920px) | Widest rails + persistent betslip panel |

### Touch Targets
Buttons carry `{spacing.sm}`×`{spacing.md}` padding and pills clear comfortable tap sizes; the green `button-primary` is the largest, highest-priority tap surface. Aim for 44×44px minimum on the dense rails.

### Collapsing Strategy
The left `sidebar-rail` collapses first (to a hamburger or bottom bar). Category tab strips and `bet-odds-button` rows become horizontally scrollable rather than wrapping. Game rails keep their carousel behavior at every width, simply showing fewer tiles. The `betslip-panel` docks to the right on desktop and becomes a bottom sheet on mobile.

### Image Behavior
Game thumbnails are full-bleed inside `{rounded.card}` corners (no internal padding) in portrait-leaning and square ratios; the artwork supplies all the color. Promo cards carry edge-to-edge photography behind an `{colors.ink}` title. Tiles lazy-load as rails scroll into view, with the `{colors.surface}` tile color as the placeholder.

## Elevation & Depth

Depth is mostly tonal — a flat two-step surface ladder rather than layered shadows.

| Level | Treatment | Use |
|---|---|---|
| 0 | `{colors.canvas}` flat | Page background, nav, sidebar rail |
| 1 | `{colors.surface}` + `{colors.hairline}` border | Cards, tiles, promo cards, betslip, buttons, inputs |
| Floating | `{colors.surface}` + soft `rgba(0,0,0,0.4)` shadow | Modals, dropdowns, the docked betslip lifted above content |

### Decorative Depth
The brand's visual richness comes from the game and promo artwork (radial-gradient bonus banners, illustrated tiles) layered on the flat dark canvas — not from UI shadows. Selected/active states use the green or blue accent as a glow-like emphasis rather than elevation.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Small chips, inner elements |
| `{rounded.sm}` | 6px | Compact cards, small media |
| `{rounded.md}` | 8px | Inputs, odds buttons, medium elements |
| `{rounded.lg}` | 10px | Primary / secondary / ghost buttons |
| `{rounded.xl}` | 12px | Utility buttons |
| `{rounded.card}` | 16px | Game tiles, promo cards, hero banners, panels |
| `{rounded.full}` | 999px | Pills, badges, avatars, circular controls |

### Photography Geometry
Game artwork is framed at `{rounded.card}` (16px) and runs full-bleed inside the tile. Promo cards use the same 16px frame with edge-to-edge imagery. Avatars, status badges, and provider chips use `{rounded.full}`. There is no exposed photography outside the gaming/promo content — the structural chrome stays geometric and flat.

## Components

> **Extraction limit:** no hover or focus state was captured from the live site — each extracted spec below covers Default and Active/Pressed only. Variants live as separate `components:` entries. The state matrix in *Component States* is **prescribed** from the extracted palette, not measured.

### Buttons

**`button-primary`** — the green "Registration" / primary-confirm CTA, the highest-visibility control.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.body}`, rounded `{rounded.lg}`, padding `{spacing.sm}` `{spacing.md}` (8×12px).

**`button-secondary`** — the blue "Log In" / secondary action and the "Show more" pill.
- Background `{colors.secondary}`, text `{colors.on-primary}`, type `{typography.body}`, rounded `{rounded.lg}`, padding 8×12px.

**`button-tertiary`** — the dark-grey utility button ("More events", "Read more").
- Background `{colors.surface}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.xl}`, padding 8×12px.

**`button-ghost`** — a low-emphasis grey control on dense rows.
- Background `{colors.surface}`, text `{colors.ink}`, type `{typography.body}`, rounded `{rounded.lg}`, padding `0` `{spacing.sm}` (0×8px).

### Navigation

**`top-nav`** — the sticky header carrying the 1win wordmark, search, balance, and the green Registration + blue Log In CTAs.
- Background `{colors.canvas}`, text `{colors.ink}`, padding 8×16px, with a `{colors.hairline}` base edge.

**`sidebar-rail`** — the fixed left icon rail (Casino, Sports, categories).
- Background `{colors.canvas}`, glyphs `{colors.muted}`, padding `{spacing.sm}`. Active item marked in `{colors.primary}`.

### Inputs & Forms

**`text-input`** — search and betslip amount fields.
- Background `{colors.surface}`, text `{colors.ink}`, placeholder `{colors.faint}`, border `{colors.hairline}`, type `{typography.body}`, rounded `{rounded.md}`, padding 8×12px.

**`bet-odds-button`** — the odds chip in sportsbook match rows.
- Background `{colors.surface}`, text `{colors.ink}`, type `{typography.ui}`, rounded `{rounded.md}`, padding 8×12px. Selected state highlights in `{colors.secondary}`.

### Pills & Badges

**`pill-badge`** — the solid blue status/count badge.
- Background `{colors.secondary}`, text `{colors.on-primary}`, type `{typography.caption}`, rounded `{rounded.full}`, padding `0` `{spacing.xs}` (0×4px).

**`pill-outline`** — the bordered filter/category pill.
- Text `{colors.ink}`, type `{typography.title}`, rounded `{rounded.full}`, padding 0×8px, with a `{colors.hairline}` border.

### Cards & Containers

**`game-tile`** — the core discovery unit: a full-bleed game thumbnail.
- Background `{colors.surface}` (placeholder), rounded `{rounded.card}`. Artwork fills edge-to-edge with no padding.

**`hero-banner`** — the top welcome-bonus / promo banner.
- Background `{colors.surface}` with edge-to-edge gradient imagery, headline `{colors.ink}` in `{typography.display}`, rounded `{rounded.card}`, padding `{spacing.xxl}`.

**`promo-card`** — a promotions-page card (full-bleed photo + title + chips).
- Background `{colors.surface}`, title `{colors.ink}`, rounded `{rounded.card}`, padding `{spacing.lg}`.

**`feature-card`** — generic dark content card.
- Background `{colors.surface}`, text `{colors.ink}`, border `{colors.hairline}`, rounded `{rounded.card}`, padding `{spacing.lg}`.

**`feature-card-elevated`** — a feature card lifted above the page (floating shadow), base for modal/toast surfaces.
- Background `{colors.surface}`, text `{colors.ink}`, rounded `{rounded.card}`, padding `{spacing.lg}`, soft `rgba(0,0,0,0.4)` shadow.

**`betslip-panel`** — the docked sportsbook betslip / wheel-of-fortune panel.
- Background `{colors.surface}`, text `{colors.ink}`, rounded `{rounded.card}`, padding `{spacing.lg}`. Confirm action uses `button-primary`.

**`footer`** — the page footer (support, information, categories columns).
- Background `{colors.canvas}`, text `{colors.muted}`, headings `{colors.ink}`, padding `{spacing.xxl}`.

### Component States

*Prescribed from the extracted palette — hover and focus were not observable on the live site. Hover and pressed are brightness/transform shifts only, so no new hex enters the palette.*

| Component | default | hover | focus-visible | active / pressed | disabled | loading | selected | error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | `{colors.primary}` fill | fill lightened ~6% | 2px `{colors.focus}` ring + 2px `{colors.canvas}` offset | `scale(0.98)` | fill at 40% opacity, label `{colors.faint}` | label swaps for an indeterminate spinner in `{colors.on-primary}`, control width held | n/a | n/a |
| `button-secondary` | `{colors.secondary}` fill | fill lightened ~6% | as above | `scale(0.98)` | fill at 40% opacity | spinner in `{colors.on-primary}` | n/a | n/a |
| `button-tertiary` / `button-ghost` | `{colors.surface}` fill | fill lightened ~8% | as above | `scale(0.98)` | label `{colors.faint}` | spinner in `{colors.muted}` | n/a | n/a |
| `text-input` | `{colors.hairline-strong}` 1px edge | edge → `{colors.muted}` | 2px `{colors.focus}` ring replaces the edge | n/a — no pressed state | fill `{colors.canvas}`, placeholder `{colors.faint}` | trailing spinner in `{colors.muted}` | n/a | **undefined** — no error red was extracted; see Known Gaps |
| `bet-odds-button` | `{colors.surface}` fill, `{colors.ink}` label | fill lightened ~8% | as above | `scale(0.98)` | label `{colors.faint}`, non-interactive (suspended market) | odds digits dim to `{colors.muted}` while re-pricing | `{colors.secondary}` fill, `{colors.on-primary}` label | n/a |
| `sidebar-rail` row (`ex-app-shell-row`) | glyph `{colors.muted}` | glyph → `{colors.ink}` | as above | glyph → `{colors.ink}` | glyph `{colors.faint}` | n/a | `{colors.primary}` indicator bar + `{colors.ink}` glyph | n/a |
| `game-tile` | `{colors.surface}` placeholder → artwork | `scale(1.02)` | as above, ring outside the `{rounded.card}` frame | `scale(0.99)` | n/a | `{colors.surface}` placeholder held until artwork decodes | n/a | n/a |
| `pill-outline` | `{colors.hairline-strong}` edge | edge → `{colors.muted}` | as above | n/a | label `{colors.faint}` | n/a | `{colors.secondary}` edge + label | n/a |
| `pill-badge` | `{colors.secondary}` fill | **two states only** — static indicator, no hover, no focus (not interactive) | — | — | — | — | — | — |
| `betslip-panel` | `{colors.surface}` | n/a (container) | focus is managed by its children | n/a | stake field disabled when the market suspends | panel-level spinner over the confirm row during bet placement | n/a | stake-validation message; colour **undefined** — see Known Gaps |

`pill-badge` and `footer` are genuinely non-interactive: default is their only state.

### Examples (illustrative)

> Kit-mirror demonstration surfaces. Each `ex-*` entry references 1win's brand-native primitives (`{colors.surface}`, `{colors.primary}`, `{rounded.card}`, the spacing scale) so downstream consumers re-skin the same 10 illustrative surfaces consistently. These are not extracted brand components.

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


## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or choreography below was observed on 1win; every value is derived from the **Calm** profile and tuned to the dense, near-black chrome this file documents. Treat it as a proposal, not an extraction.

Why Calm fits 1win: all of the saturation here lives *inside* game artwork and bonus illustrations, while the chrome is monochrome dark plus two signals. Motion follows the chrome, not the content — short opacity-led fades with minimal travel keep a wall of 40+ bright thumbnails from reading as a slot machine. The one place this profile is arguably wrong is the reward moment (win confirmations, wheel-of-fortune results), which wants Playful overshoot; that is handled as a scoped exception below rather than by changing the base profile.

### Tokens

| Token | Value |
|---|---|
| `{motion.duration-instant}` | 80ms |
| `{motion.duration-fast}` | 150ms |
| `{motion.duration-base}` | 250ms |
| `{motion.duration-slow}` | 400ms |
| `{motion.duration-emphasis}` | 600ms |
| `{motion.ease-standard}` | cubic-bezier(0.4, 0, 0.6, 1) — symmetric, the Calm bias |
| `{motion.ease-enter}` | cubic-bezier(0, 0, 0.2, 1) — decelerate in |
| `{motion.ease-exit}` | cubic-bezier(0.4, 0, 1, 1) — accelerate out |
| `{motion.stagger-step}` | 40ms |

### Interactions

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, `game-tile`, nav row) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`; `transform: scale(1.02)` on `game-tile` only | Scale removed; opacity shift kept at `{motion.duration-fast}` |
| Press (any control) | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | Removed entirely — pressed state is colour only |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-enter}` | `opacity` | Unchanged — already opacity-only and under 150ms |
| Page / route transition (Casino ⇄ Sports) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` only; no cross-fade travel | Cross-fade at `{motion.duration-fast}`, no travel |
| Modal (`ex-modal-card`) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: scale(0.97 → 1)`; scrim `opacity` | Scale dropped; scrim and dialog fade at `{motion.duration-fast}` |
| Drawer / mobile betslip sheet | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateY(100% → 0)` | Travel dropped; sheet fades in at `{motion.duration-fast}` |
| Dropdown (provider filter, account menu) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(-4px → 0)` | Travel dropped; fade only |
| Toast (`ex-toast`) | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px → 0)` | Travel dropped; fade only, same dwell time |
| List enter (rail tiles, match rows) | `{motion.duration-base}`, staggered `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity` 0 → 1, `transform: translateY(6px → 0)` | Stagger and travel dropped; the whole batch fades once at `{motion.duration-fast}` |
| List exit (filtered-out tiles, settled bets) | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | Unchanged |
| Loading — tile skeleton | 1200ms, infinite | `{motion.ease-standard}` | `opacity` pulse on the `{colors.surface}` placeholder | Loop frozen at its mid-opacity value; a static placeholder remains |
| Loading — button spinner | 800ms, infinite | linear | `transform: rotate()` | Rotation frozen; replaced by a static `{colors.muted}` indicator and `aria-busy` |
| **Exception — reward moment** (win confirm, wheel result) | `{motion.duration-emphasis}` | `{motion.ease-enter}` with overshoot to `scale(1.04)` then settle | `opacity` + `transform` | Overshoot and scale removed; the result value fades in at `{motion.duration-fast}` |

### Rules

- Only `transform` and `opacity` are ever put in a transition here. Layout-triggering properties are forbidden in every transition on this surface: `width`, `height`, `top`, `left`, `margin`.
- Every exit is shorter than its matching entrance (modal 150 vs 250, drawer 150 vs 250, dropdown 80 vs 150, list 150 vs 250).
- Nothing animates on first paint in a way that delays content. Game rails render at full opacity on load; the stagger applies only to subsequent client-side list changes (filter, "Show more", rail pagination).
- The only infinite loops are the two loaders above. There is **no brand ambience loop** on this surface — no drifting gradients, no pulsing CTAs; the bonus-banner gradients are static artwork.

### `@media (prefers-reduced-motion: reduce)`

**Removed:** all `transform` — every translate, every scale, the press compression, the reward overshoot, and the list stagger (`{motion.stagger-step}` → 0).

**Kept:** opacity fades, capped at `{motion.duration-fast}` (150ms), so state changes stay legible rather than snapping. Focus rings are unchanged. Both loaders freeze: the skeleton holds a static `{colors.surface}` placeholder and the spinner is replaced by a static indicator plus `aria-busy`, so loading is still announced without a moving element.

## Accessibility

Contrast computed with WCAG 2.1 relative luminance from this file's own hexes. Nothing here was verified in a browser — see Known Gaps.

### Measured contrast

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` / `{colors.canvas}` | 16.42:1 | 4.5 | Pass |
| `{colors.ink}` / `{colors.surface}` | 11.77:1 | 4.5 | Pass |
| `{colors.muted}` / `{colors.canvas}` | 7.11:1 | 4.5 | Pass |
| `{colors.muted}` / `{colors.surface}` | 5.10:1 | 4.5 | Pass |
| `{colors.faint}` / `{colors.canvas}` | 2.54:1 | 4.5 | **Fail** — disabled-only |
| `{colors.on-primary}` / `{colors.primary}` | 2.81:1 | 4.5 | **Fail** |
| `{colors.on-primary}` / `{colors.secondary}` | 4.21:1 | 4.5 | **Fail** |
| `{colors.black}` / `{colors.primary}` | 7.47:1 | 4.5 | Pass — the accessible alternative |
| `{colors.black}` / `{colors.secondary}` | 4.99:1 | 4.5 | Pass — the accessible alternative |
| `{colors.hairline}` / `{colors.canvas}` | 1.37:1 | 3.0 | **Fail** — decorative edge only |
| `{colors.hairline-strong}` / `{colors.canvas}` | 4.22:1 | 3.0 | Pass |
| `{colors.hairline-strong}` / `{colors.surface}` | 3.03:1 | 3.0 | Pass |
| `{colors.focus}` / `{colors.canvas}` | 7.01:1 | 3.0 | Pass |
| `{colors.focus}` / `{colors.surface}` | 5.03:1 | 3.0 | Pass |
| `{colors.primary}` / `{colors.canvas}` | 6.55:1 | 3.0 | Pass |
| `{colors.secondary}` / `{colors.canvas}` | 4.37:1 | 3.0 | Pass |

**The real brand fails AA on accent labels.** White on the green `{colors.primary}` is 2.81:1 and white on the blue `{colors.secondary}` is 4.21:1. Both hexes are brand identity and are left untouched. Two defensible routes: set accent-fill labels in `{colors.black}` (7.47:1 / 4.99:1), or keep white and restrict it to large text — 18px+ at weight 700, or 14px+ at the 800 weight this system already uses — where the 3:1 large-text threshold applies and 2.81:1 still misses on green but 4.21:1 clears on blue. Green with white at `{typography.body}` (14px/600) has no reading under which it passes.

### Focus ring visibility, surface by surface

| Surface | Ring treatment | Effective ratio |
|---|---|---|
| `{colors.canvas}` (nav, `sidebar-rail`, `footer`) | 2px `{colors.focus}`, no offset needed | 7.01:1 |
| `{colors.surface}` (cards, tiles, inputs, odds chips) | 2px `{colors.focus}` + 2px `{colors.canvas}` offset | 5.03:1 against the surface; 7.01:1 against the offset |
| `{colors.primary}` fill (`button-primary`) | 2px `{colors.focus}` + 2px `{colors.canvas}` offset — **offset mandatory**, ring-on-green is 1.07:1 | 6.55:1 (green/canvas) at the control edge, 7.01:1 at the ring |
| `{colors.secondary}` fill (`button-secondary`, `pill-badge`) | same, offset mandatory — ring-on-blue is 1.60:1 | 4.37:1 (blue/canvas) at the edge, 7.01:1 at the ring |
| Game artwork (`game-tile`, `hero-banner`) | ring drawn *outside* the `{rounded.card}` frame, over `{colors.canvas}` | 7.01:1 — never computed against artwork, which is unknowable |

The ring is never the only focus cue: focused controls also carry the hover brightness shift, so focus survives on any artwork.

### Tap targets

`button-primary` at `{typography.body}` (14px / line-height 1.4 ≈ 20px) plus `{spacing.sm}` vertical padding computes to roughly 36px — **below the 44px minimum**. The dense rails need extra hit area beyond the painted box: add a transparent inset so every interactive element clears 44×44px, and keep at least `{spacing.sm}` between adjacent `bet-odds-button` chips. `pill-badge` is non-interactive and exempt. These are target *specifications*; actual rendered sizes cannot be verified from a document.

### Motion

Reduced-motion handling is specified in full above. In short: no `transform` survives the query, opacity fades cap at `{motion.duration-fast}`, and both loaders freeze while remaining announced via `aria-busy`.

### Not verified here

Keyboard tab order, screen-reader labelling of the odds chips and the betslip, text resize to 200%, and any rendered geometry (overlap, overflow, real tap size) need a live page. None of it is claimed in this file.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (green) for primary actions — Registration, confirm, place-bet — and `{colors.secondary}` (blue) for secondary actions, links, and live/betting highlights.
- Build depth with the surface ladder (`{colors.canvas}` → `{colors.surface}`) plus a faint `{colors.hairline}` edge; avoid heavy shadows.
- Set every label in Inter 600+ (`{typography.body}` / `{typography.caption}`); use the 800 weight for headlines and bonus figures.
- Let game and promo artwork supply the color — keep the surrounding chrome monochrome dark.
- Use `{rounded.lg}`–`{rounded.xl}` on buttons, `{rounded.card}` (16px) on tiles/cards/panels, and `{rounded.full}` on pills and badges.
- Pair accent fills with `{colors.on-primary}` (white) text for legibility.

### Don't
- Don't promote game-tile or bonus-banner gradient colors (the purples, reds, violets, ambers) into the UI palette — they are content, not chrome.
- Don't add a third structural accent; the system is green + blue only.
- Don't use pure-regular weights — there is no Inter 400 here; body copy is semibold.
- Don't pad game tiles — artwork is full-bleed inside `{rounded.card}` corners.
- Don't rely on drop shadows for elevation; the surface brightness step is the elevation language.
- Don't set `{colors.on-primary}` on `{colors.primary}` at `{typography.body}` — 2.81:1. Use `{colors.black}` on green fills, or reserve white for the 800-weight display sizes.
- Don't use `{colors.hairline}` as a control's only boundary (1.37:1 on canvas) — use `{colors.hairline-strong}` where the edge carries meaning.
- Don't put travel or scale in a transition without a `prefers-reduced-motion` fallback, and don't transition anything other than `transform` and `opacity`.

## Iteration Guide

- **Adding a surface step.** The ladder is deliberately two-deep (`{colors.canvas}` → `{colors.surface}`, 1.39:1 apart). A third step has almost no luminance room before it collides with `{colors.surface}`; add elevation with the floating shadow from *Elevation & Depth* instead of a new hex.
- **Adding a semantic colour.** The one real hole is error/warning (see Known Gaps). Add it as a semantic token, not a third structural accent — the "green + blue only" rule in *Don't* is about chrome, not about validation feedback.
- **Retuning motion.** Change the tokens in the `motion:` group, not the per-interaction rows; every row references a token. If a future measurement of the live site contradicts these values, replace the token values and delete the "prescribed, not measured" caveat — it is only there because nothing was measured.
- **Re-skinning the `ex-*` surfaces.** They intentionally hold no new values. Keep them referencing brand primitives so the illustrative kit tracks any palette change automatically.

## Known Gaps

- **Motion is entirely prescribed.** No duration, easing or choreography was observed on 1win. The Calm profile was assigned from this file's own signals (monochrome chrome, two accents, content-supplied saturation), not from a recording.
- **Hover and focus were never captured.** The extracted component specs cover Default and Active/Pressed only; the whole *Component States* matrix is inference from the extracted palette.
- **No error / warning / success colour was extracted.** `{colors.primary}` doubles as the success signal, but validation errors — a rejected stake, a failed deposit, a suspended market — have no documented colour. Marked **undefined** in the state matrix rather than guessed at; a red would have to be measured or approved.
- **`{colors.hairline}` is described in the Colors section as "translucent", but it is recorded as an opaque hex.** If the real value is an `rgba()` over `{colors.canvas}`, its effective contrast differs from the 1.37:1 computed here.
- **Elevation shadow is a prose value, not a token.** `rgba(0,0,0,0.4)` appears in *Elevation & Depth* and in `feature-card-elevated` but has no frontmatter key, so it cannot be referenced as `{…}`. There is no `shadow:` group in the repo's token contract.
- **`{colors.black}` has no role pattern** in the audit's token contract, so the accessible accent-label pairing documented above is invisible to the harness.
- **Tap targets, overlap, overflow and frame rate are unverifiable** from a document. The 44px minimum is a specification, not a measurement.
- **Source pages were home, promotions, betting and vip-club only.** Account, deposit, cashier and live-casino surfaces were not analysed; the betslip spec in particular is partial.
