---
version: alpha
name: Spotify-design-analysis
description: Content-first darkness — a near-black charcoal ladder (#121212 to #272727) where the UI recedes so album art can glow, Spotify Green (#1ed760) as the single functional signal, SpotifyMixUI type kept compact at 10-24px, and a pill-and-circle geometry (500px, 9999px, 50%) carried by notably heavy shadows. Every colour, type and component value below is read from this file's own prose; the motion group is prescribed, not measured.

colors:
  canvas: "#121212"
  surface: "#181818"
  surface-interactive: "#1f1f1f"
  surface-card: "#252525"
  surface-card-alt: "#272727"
  text: "#ffffff"
  text-emphasis: "#fdfdfd"
  muted: "#b3b3b3"
  muted-bright: "#cbcbcb"
  border: "#4d4d4d"
  border-outline: "#7c7c7c"
  border-focus: "#000000"
  divider: "#b3b3b3"
  accent: "#1ed760"
  accent-border: "#1db954"
  on-accent: "#000000"
  focus: "#1ed760"
  negative: "#f3727f"
  warning: "#ffa42b"
  announcement: "#539df5"
  button-light: "#eeeeee"
  on-light: "#181818"

typography:
  section-title:
    fontFamily: "SpotifyMixUITitle, CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, Helvetica Neue, helvetica, arial, Hiragino Sans, Hiragino Kaku Gothic ProN, Meiryo, MS Gothic"
    fontSize: 24px
    fontWeight: 700
    lineHeight: normal
    letterSpacing: normal
  feature-heading:
    fontFamily: "SpotifyMixUI, CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, Helvetica Neue, helvetica, arial, Hiragino Sans, Hiragino Kaku Gothic ProN, Meiryo, MS Gothic"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: normal
  body-bold:
    fontFamily: "SpotifyMixUI"
    fontSize: 16px
    fontWeight: 700
    lineHeight: normal
    letterSpacing: normal
  body:
    fontFamily: "SpotifyMixUI"
    fontSize: 16px
    fontWeight: 400
    lineHeight: normal
    letterSpacing: normal
  button-uppercase:
    fontFamily: "SpotifyMixUI"
    fontSize: 14px
    fontWeight: 600-700
    lineHeight: 1.00
    letterSpacing: 1.4px-2px
    textTransform: uppercase
  button:
    fontFamily: "SpotifyMixUI"
    fontSize: 14px
    fontWeight: 700
    lineHeight: normal
    letterSpacing: 0.14px
  nav-link-bold:
    fontFamily: "SpotifyMixUI"
    fontSize: 14px
    fontWeight: 700
    lineHeight: normal
    letterSpacing: normal
  nav-link:
    fontFamily: "SpotifyMixUI"
    fontSize: 14px
    fontWeight: 400
    lineHeight: normal
    letterSpacing: normal
  caption-bold:
    fontFamily: "SpotifyMixUI"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.50-1.54
    letterSpacing: normal
  caption:
    fontFamily: "SpotifyMixUI"
    fontSize: 14px
    fontWeight: 400
    lineHeight: normal
    letterSpacing: normal
  small-bold:
    fontFamily: "SpotifyMixUI"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: normal
  small:
    fontFamily: "SpotifyMixUI"
    fontSize: 12px
    fontWeight: 400
    lineHeight: normal
    letterSpacing: normal
  badge:
    fontFamily: "SpotifyMixUI"
    fontSize: 10.5px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: normal
    textTransform: capitalize
  micro:
    fontFamily: "SpotifyMixUI"
    fontSize: 10px
    fontWeight: 400
    lineHeight: normal
    letterSpacing: normal

spacing:
  hair: 1px
  micro: 2px
  micro-alt: 3px
  fine: 4px
  fine-alt: 5px
  xs: 6px
  sm: 8px
  sm-alt: 10px
  md: 12px
  md-alt: 14px
  md-wide: 15px
  lg: 16px
  xl: 20px

rounded:
  minimal: 2px
  subtle: 4px
  standard: 6px
  comfortable: 8px
  medium: 10px
  medium-max: 20px
  large: 100px
  pill: 500px
  full-pill: 9999px
  circle: 50%

shadow:
  heavy: rgba(0,0,0,0.5) 0px 8px 24px
  medium: rgba(0,0,0,0.3) 0px 8px 8px
  inset-border: rgb(18,18,18) 0px 1px 0px, rgb(124,124,124) 0px 0px 0px 1px inset

motion:
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 500ms
  ease-standard: cubic-bezier(0.4, 0, 0.2, 1)
  ease-enter: cubic-bezier(0.2, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 40ms
  duration-reduced: 150ms

components:
  button-dark-pill:
    backgroundColor: "{colors.surface-interactive}"
    textColor: "{colors.text}"
    typography: "{typography.button}"
    rounded: "{rounded.full-pill}"
    padding: 8px 16px
  button-dark-pill-muted:
    backgroundColor: "{colors.surface-interactive}"
    textColor: "{colors.muted}"
    typography: "{typography.button}"
    rounded: "{rounded.full-pill}"
    padding: 8px 16px
  button-dark-large-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 0px 43px
  button-light-pill:
    backgroundColor: "{colors.button-light}"
    textColor: "{colors.on-light}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
  button-outlined-pill:
    backgroundColor: transparent
    textColor: "{colors.text}"
    typography: "{typography.button}"
    rounded: "{rounded.full-pill}"
    borderColor: "{colors.border-outline}"
    padding: 4px 16px 4px 36px
  button-circular-play:
    backgroundColor: "{colors.surface-interactive}"
    textColor: "{colors.text}"
    rounded: "{rounded.circle}"
    padding: 12px
  button-circular-play-green:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.circle}"
    padding: 12px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-bold}"
    rounded: "{rounded.comfortable}"
  card-alt:
    backgroundColor: "{colors.surface-interactive}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.standard}"
  card-elevated:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.comfortable}"
  card-elevated-alt:
    backgroundColor: "{colors.surface-card-alt}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.comfortable}"
  input-search:
    backgroundColor: "{colors.surface-interactive}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 12px 96px 12px 48px
  input-search-focus:
    backgroundColor: "{colors.surface-interactive}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    borderColor: "{colors.border-focus}"
  nav-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text}"
    typography: "{typography.nav-link-bold}"
  nav-item-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  divider-rule:
    backgroundColor: "{colors.divider}"
    height: 1px
---

# Design System Inspired by Spotify

## Overview

Spotify's web interface is a dark, immersive music player that wraps listeners in a near-black cocoon (`#121212`, `#181818`, `#1f1f1f`) where album art and content become the primary source of color. The design philosophy is "content-first darkness" — the UI recedes into shadow so that music, podcasts, and playlists can glow. Every surface is a shade of charcoal, creating a theater-like environment where the only true color comes from the iconic Spotify Green (`#1ed760`) and the album artwork itself.

The typography uses SpotifyMixUI and SpotifyMixUITitle — proprietary fonts from the CircularSp family (Circular by Lineto, customized for Spotify) with an extensive fallback stack that includes Arabic, Hebrew, Cyrillic, Greek, Devanagari, and CJK fonts, reflecting Spotify's global reach. The type system is compact and functional: 700 (bold) for emphasis and navigation, 600 (semibold) for secondary emphasis, and 400 (regular) for body. Buttons use uppercase with positive letter-spacing (1.4px–2px) for a systematic, label-like quality.

What distinguishes Spotify is its pill-and-circle geometry. Primary buttons use 500px–9999px radius (full pill), circular play buttons use 50% radius, and search inputs are 500px pills. Combined with heavy shadows (`rgba(0,0,0,0.5) 0px 8px 24px`) on elevated elements and a unique inset border-shadow combo (`rgb(18,18,18) 0px 1px 0px, rgb(124,124,124) 0px 0px 0px 1px inset`), the result is an interface that feels like a premium audio device — tactile, rounded, and built for touch.

**Key Characteristics:**
- Near-black immersive dark theme (`#121212`–`#1f1f1f`) — UI disappears behind content
- Spotify Green (`#1ed760`) as singular brand accent — never decorative, always functional
- SpotifyMixUI/CircularSp font family with global script support
- Pill buttons (500px–9999px) and circular controls (50%) — rounded, touch-optimized
- Uppercase button labels with wide letter-spacing (1.4px–2px)
- Heavy shadows on elevated elements (`rgba(0,0,0,0.5) 0px 8px 24px`)
- Semantic colors: negative red (`#f3727f`), warning orange (`#ffa42b`), announcement blue (`#539df5`)
- Album art as the primary color source — the UI is achromatic by design

## Colors

### Primary Brand
- **Spotify Green** (`{colors.accent}` — `#1ed760`): Primary brand accent — play buttons, active states, CTAs
- **Near Black** (`{colors.canvas}` — `#121212`): Deepest background surface
- **Dark Surface** (`{colors.surface}` — `#181818`): Cards, containers, elevated surfaces
- **Mid Dark** (`{colors.surface-interactive}` — `#1f1f1f`): Button backgrounds, interactive surfaces

### Text
- **White** (`{colors.text}` — `#ffffff`): `--text-base`, primary text
- **Silver** (`{colors.muted}` — `#b3b3b3`): Secondary text, muted labels, inactive nav
- **Near White** (`{colors.muted-bright}` — `#cbcbcb`): Slightly brighter secondary text
- **Light** (`{colors.text-emphasis}` — `#fdfdfd`): Near-pure white for maximum emphasis

### Semantic
- **Negative Red** (`{colors.negative}` — `#f3727f`): `--text-negative`, error states
- **Warning Orange** (`{colors.warning}` — `#ffa42b`): `--text-warning`, warning states
- **Announcement Blue** (`{colors.announcement}` — `#539df5`): `--text-announcement`, info states

### Surface & Border
- **Dark Card** (`{colors.surface-card}` — `#252525`): Elevated card surface
- **Mid Card** (`{colors.surface-card-alt}` — `#272727`): Alternate card surface
- **Border Gray** (`{colors.border}` — `#4d4d4d`): Button borders on dark — **decorative only.** At 2.22:1 on the canvas it does not reach the 3:1 boundary threshold; see Accessibility
- **Light Border** (`{colors.border-outline}` — `#7c7c7c`): Outlined button borders, muted links — the strongest boundary the palette owns short of the separator, and the one to use where a component edge must actually be seen
- **Separator** (`{colors.divider}` — `#b3b3b3`): Divider lines
- **Light Surface** (`{colors.button-light}` — `#eeeeee`): Light-mode buttons (rare), with `{colors.on-light}` (`#181818`) as its label ink
- **Spotify Green Border** (`{colors.accent-border}` — `#1db954`): Green accent border variant

### Accent Contrast
- **Black on Green** (`{colors.on-accent}` — `#000000`): the icon or label drawn on Spotify Green, as the source's own circular-play prompt specifies. White on green is **not** a usable pair (1.92:1).

### Focus
- **Focus Ring** (`{colors.focus}` — `#1ed760`): **Prescribed by this audit, not extracted.** It reuses Spotify Green, a tone the palette already owns and already assigns to "active states", so no new colour enters a palette whose first rule is that it is achromatic apart from the green. Drawn 2px wide with a 2px offset outside the control, so it is judged against the surface behind it. Measured ratios for every surface in this file are in Accessibility.
- **Extracted input focus border** (`{colors.border-focus}` — `#000000`): the source's one real focus treatment — "border becomes `#000000`, outline `1px solid`" on the search input. It is **frozen as extracted** and it fails: black on `#1f1f1f` is 1.27:1. Disclosed in Accessibility and raised under Needs approval in the audit report.

### Shadows
- **Heavy** (`{shadow.heavy}` — `rgba(0,0,0,0.5) 0px 8px 24px`): Dialogs, menus, elevated panels
- **Medium** (`{shadow.medium}` — `rgba(0,0,0,0.3) 0px 8px 8px`): Cards, dropdowns
- **Inset Border** (`{shadow.inset-border}` — `rgb(18,18,18) 0px 1px 0px, rgb(124,124,124) 0px 0px 0px 1px inset`): Input border-shadow combo

## Typography

### Font Families
- **Title**: `SpotifyMixUITitle`, fallbacks: `CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, Helvetica Neue, helvetica, arial, Hiragino Sans, Hiragino Kaku Gothic ProN, Meiryo, MS Gothic`
- **UI / Body**: `SpotifyMixUI`, same fallback stack

### Hierarchy

| Role | Token | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|-------|------|------|--------|-------------|----------------|-------|
| Section Title | `{typography.section-title}` | SpotifyMixUITitle | 24px (1.50rem) | 700 | normal | normal | Bold title weight |
| Feature Heading | `{typography.feature-heading}` | SpotifyMixUI | 18px (1.13rem) | 600 | 1.30 (tight) | normal | Semibold section heads |
| Body Bold | `{typography.body-bold}` | SpotifyMixUI | 16px (1.00rem) | 700 | normal | normal | Emphasized text |
| Body | `{typography.body}` | SpotifyMixUI | 16px (1.00rem) | 400 | normal | normal | Standard body |
| Button Uppercase | `{typography.button-uppercase}` | SpotifyMixUI | 14px (0.88rem) | 600–700 | 1.00 (tight) | 1.4px–2px | `text-transform: uppercase` |
| Button | `{typography.button}` | SpotifyMixUI | 14px (0.88rem) | 700 | normal | 0.14px | Standard button |
| Nav Link Bold | `{typography.nav-link-bold}` | SpotifyMixUI | 14px (0.88rem) | 700 | normal | normal | Navigation |
| Nav Link | `{typography.nav-link}` | SpotifyMixUI | 14px (0.88rem) | 400 | normal | normal | Inactive nav |
| Caption Bold | `{typography.caption-bold}` | SpotifyMixUI | 14px (0.88rem) | 700 | 1.50–1.54 | normal | Bold metadata |
| Caption | `{typography.caption}` | SpotifyMixUI | 14px (0.88rem) | 400 | normal | normal | Metadata |
| Small Bold | `{typography.small-bold}` | SpotifyMixUI | 12px (0.75rem) | 700 | 1.50 | normal | Tags, counts |
| Small | `{typography.small}` | SpotifyMixUI | 12px (0.75rem) | 400 | normal | normal | Fine print |
| Badge | `{typography.badge}` | SpotifyMixUI | 10.5px (0.66rem) | 600 | 1.33 | normal | `text-transform: capitalize` |
| Micro | `{typography.micro}` | SpotifyMixUI | 10px (0.63rem) | 400 | normal | normal | Smallest text |

### Principles
- **Bold/regular binary**: Most text is either 700 (bold) or 400 (regular), with 600 used sparingly. This creates a clear visual hierarchy through weight contrast rather than size variation.
- **Uppercase buttons as system**: Button labels use uppercase + wide letter-spacing (1.4px–2px), creating a systematic "label" voice distinct from content text.
- **Compact sizing**: The range is 10px–24px — narrower than most systems. Spotify's type is compact and functional, designed for scanning playlists, not reading articles.
- **Global script support**: The extensive fallback stack (Arabic, Hebrew, Cyrillic, Greek, Devanagari, CJK) reflects Spotify's 180+ market reach.
- **Line height is mostly unresolved**: the source records `normal` for nine of the fourteen roles rather than a number. Those are carried through as `normal`, not replaced with a guess; see Known Gaps.

## Layout

### Spacing System
- Base unit: 8px (`{spacing.sm}`)
- Scale: 1px, 2px, 3px, 4px, 5px, 6px, 8px, 10px, 12px, 14px, 15px, 16px, 20px — `{spacing.hair}` through `{spacing.xl}`
- Four component paddings sit outside this ladder (36px, 43px, 48px, 96px), all of them icon- or label-aware insets on pills; recorded in Known Gaps rather than snapped to the scale

### Grid & Container
- Sidebar (fixed) + main content area
- Grid-based album/playlist cards
- Full-width now-playing bar at bottom
- Responsive content area fills remaining space

### Whitespace Philosophy
- **Dark compression**: Spotify packs content densely — playlist grids, track lists, and navigation are all tightly spaced. The dark background provides visual rest between elements without needing large gaps.
- **Content density over breathing room**: This is an app, not a marketing site. Every pixel serves the listening experience.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Base (Level 0) | `{colors.canvas}` (`#121212`) background | Deepest layer, page background |
| Surface (Level 1) | `{colors.surface}` (`#181818`) or `{colors.surface-interactive}` (`#1f1f1f`) | Cards, sidebar, containers |
| Elevated (Level 2) | `{shadow.medium}` (`rgba(0,0,0,0.3) 0px 8px 8px`) | Dropdown menus, hover cards |
| Dialog (Level 3) | `{shadow.heavy}` (`rgba(0,0,0,0.5) 0px 8px 24px`) | Modals, overlays, menus |
| Inset (Border) | `{shadow.inset-border}` (`rgb(18,18,18) 0px 1px 0px, rgb(124,124,124) 0px 0px 0px 1px inset`) | Input borders |

**Shadow Philosophy**: Spotify uses notably heavy shadows for a dark-themed app. The 0.5 opacity shadow at 24px blur creates a dramatic "floating in darkness" effect for dialogs and menus, while the 0.3 opacity at 8px blur provides a more subtle card lift. The unique inset border-shadow combination on inputs creates a recessed, tactile quality.

**Elevation is expressed two ways, and the two halves never meet.** Levels 0 and 1 are background steps with no shadow; levels 2 and 3 are shadows with no stated background. The background steps are also very small: `{colors.surface}` sits 1.06:1 from `{colors.canvas}`, `{colors.surface-card}` 1.22:1, and `{colors.surface-card}` and `{colors.surface-card-alt}` are 1.03:1 apart. None of those is a WCAG pair, but none of them is a reliable layer boundary either, so a card's edge on this interface is carried by shadow, radius and album art rather than by the step in charcoal. That is the brand's stated intent ("depth through shade variation") and also its weakest point; recorded in Known Gaps.

## Shapes

### Border Radius Scale
- Minimal (`{rounded.minimal}` — 2px): Badges, explicit tags
- Subtle (`{rounded.subtle}` — 4px): Inputs, small elements
- Standard (`{rounded.standard}` — 6px): Album art containers, cards
- Comfortable (`{rounded.comfortable}` — 8px): Sections, dialogs
- Medium (`{rounded.medium}`–`{rounded.medium-max}` — 10px–20px): Panels, overlay elements
- Large (`{rounded.large}` — 100px): Large pill buttons
- Pill (`{rounded.pill}` — 500px): Primary buttons, search input
- Full Pill (`{rounded.full-pill}` — 9999px): Navigation pills, search
- Circle (`{rounded.circle}` — 50%): Play buttons, avatars, icons

### Geometric Motif
The ladder is not a geometric progression and is not meant to be. 2px–10px is a fine-grained container scale, and 100px, 500px and 9999px are three spellings of one "full pill" intent at different component widths — the pill-and-circle geometry that, with the 50% circles, carries most of the brand's recognition. Both ends of the `10px–20px` range and all three pill spellings are recorded as the source states them rather than collapsed to a single canonical value.

## Components

**Interaction states are the thinnest part of this document.** The source records exactly three: the card hover ("slight background lightening"), the navigation active weight and colour, and the search input's focus border. Everything else — press, disabled, loading, selected, error — appears nowhere in the file for any component, and no control is given a value to extract for them. Those are marked as not documented rather than guessed at; see Known Gaps. The focus-visible treatment on buttons, cards and navigation is prescribed by this audit and labelled as such throughout.

### Buttons

**Dark Pill** (`{components.button-dark-pill}` / `{components.button-dark-pill-muted}`)
- Background: `{colors.surface-interactive}` (`#1f1f1f`)
- Text: `{colors.text}` (`#ffffff`) or `{colors.muted}` (`#b3b3b3`)
- Padding: 8px 16px
- Radius: `{rounded.full-pill}` (9999px, full pill)
- Use: Navigation pills, secondary actions
- **Focus-visible** (prescribed): 2px `{colors.focus}` ring at a 2px offset, drawn outside the pill
- Hover, pressed, disabled, loading, selected and error: not documented in the source

**Dark Large Pill** (`{components.button-dark-large-pill}`)
- Background: `{colors.surface}` (`#181818`)
- Text: `{colors.text}` (`#ffffff`)
- Padding: 0px 43px
- Radius: `{rounded.pill}` (500px)
- Use: Primary app navigation buttons
- **Focus-visible** (prescribed): 2px `{colors.focus}` ring at a 2px offset
- Hover, pressed, disabled, loading, selected and error: not documented in the source

**Light Pill** (`{components.button-light-pill}`)
- Background: `{colors.button-light}` (`#eeeeee`)
- Text: `{colors.on-light}` (`#181818`)
- Radius: `{rounded.pill}` (500px)
- Use: Light-mode CTAs (cookie consent, marketing)
- **Focus-visible** (prescribed): the ring is drawn outside the pill, on the dark ground behind it, so it is measured against `{colors.canvas}` and not against the `#eeeeee` fill — which the green ring does **not** clear (1.65:1)
- Hover, pressed, disabled, loading, selected and error: not documented in the source

**Outlined Pill** (`{components.button-outlined-pill}`)
- Background: transparent
- Text: `{colors.text}` (`#ffffff`)
- Border: `1px solid {colors.border-outline}` (`#7c7c7c`)
- Padding: 4px 16px 4px 36px (asymmetric for icon)
- Radius: `{rounded.full-pill}` (9999px)
- Use: Follow buttons, secondary actions
- **Focus-visible** (prescribed): 2px `{colors.focus}` ring at a 2px offset, outside the existing 1px outline
- Hover, pressed, disabled, loading, selected and error: not documented in the source

**Circular Play** (`{components.button-circular-play}` / `{components.button-circular-play-green}`)
- Background: `{colors.surface-interactive}` (`#1f1f1f`), or `{colors.accent}` (`#1ed760`) for the green primary variant
- Icon: `{colors.text}` (`#ffffff`) on the dark variant, `{colors.on-accent}` (`#000000`) on the green one
- Padding: 12px
- Radius: `{rounded.circle}` (50%, circle)
- Use: Play/pause controls
- **Focus-visible** (prescribed): 2px `{colors.focus}` ring at a 2px offset; on the green variant the ring sits on the surface behind the control, never on the green fill itself
- Hover, pressed, disabled, loading, selected and error: not documented in the source — the most conspicuous absence in the file, since this is the one control a music player cannot be without a loading and a selected state for

### Cards & Containers
- `{components.card}` — Background `{colors.surface}` (`#181818`); `{components.card-alt}` — `{colors.surface-interactive}` (`#1f1f1f`)
- `{components.card-elevated}` / `{components.card-elevated-alt}` — `{colors.surface-card}` (`#252525`) and `{colors.surface-card-alt}` (`#272727`), the two elevated card tones
- Radius: `{rounded.standard}`–`{rounded.comfortable}` (6px–8px)
- No visible borders on most cards
- **Hover**: slight background lightening — the one card interaction the source records. Its target tone is not quantified; see Known Gaps
- Shadow: `{shadow.medium}` (`rgba(0,0,0,0.3) 0px 8px 8px`) on elevated
- **Focus-visible** (prescribed): where a card is wholly a link, the 2px `{colors.focus}` ring is drawn on the card edge at a 2px offset
- Pressed, disabled, loading, selected and error: not documented in the source

### Inputs
- `{components.input-search}` — Search input: `{colors.surface-interactive}` (`#1f1f1f`) background, `{colors.text}` (`#ffffff`) text
- Radius: `{rounded.pill}` (500px, pill)
- Padding: 12px 96px 12px 48px (icon-aware)
- Boundary: `{shadow.inset-border}` — the inset border-shadow combo, not a border token
- **Focus-visible** (extracted, `{components.input-search-focus}`): border becomes `{colors.border-focus}` (`#000000`), outline `1px solid`. This is the real Spotify treatment and it cannot be seen — 1.27:1 against the input's own `#1f1f1f` fill. The binding is frozen as extracted; the prescribed 2px `{colors.focus}` ring is what this audit recommends drawing instead, and the re-binding question is raised under Needs approval in the audit report
- Hover, pressed, disabled, loading, selected and error: not documented in the source. `{colors.negative}` (`#f3727f`) exists as `--text-negative` for error text, but the source never binds it to a control, so no error state is claimed here

### Navigation
- `{components.nav-sidebar}` — Dark sidebar on `{colors.canvas}` with `{typography.nav-link-bold}` (SpotifyMixUI 14px weight 700) for the current item, `{typography.nav-link}` (weight 400) otherwise
- `{components.nav-item-inactive}` — `{colors.muted}` (`#b3b3b3`) for inactive items
- **Active**: weight 700 and `{colors.text}` (`#ffffff`) — the second interaction state the source records
- Circular icon buttons (`{rounded.circle}`)
- Spotify logo top-left in green
- **Focus-visible** (prescribed): 2px `{colors.focus}` ring at a 2px offset
- Hover, pressed, disabled, loading, selected and error: not documented in the source for navigation; the card rule is the only hover the file states anywhere

### Dividers
- `{components.divider-rule}` — 1px rule in `{colors.divider}` (`#b3b3b3`)
- **Default state only** — a non-interactive rule, which is the whole of its state set

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No duration, easing curve, transition or choreography below was extracted from Spotify's interface; the source file contains no motion value of any kind. The values are a shared profile block from `theme-audit/SPEC.md` section 5, carried verbatim in the `motion:` frontmatter group so every file on the same profile behaves as a sibling.

**Profile: Calm, not the rostered Cinematic.** This is a deliberate, argued switch, not a drift — see `theme-audit/reports/A67-spotify.md` and Known Gaps. Applying SPEC section 5's assignment rule in order: Spotify is not a luxury, automotive, hardware-flagship, gaming-console or aerospace identity, so rule 1 does not fire, and rule 1's own stated tell — "full-bleed photography, sparse type and a slow reveal" — is absent from this document in all three parts. The type here is compact and functional at 10px–24px, the file's own words are "this is an app, not a marketing site. Every pixel serves the listening experience" and "content density over breathing room", and nothing in it describes a reveal of any kind. Rule 2 (terminal, IDE, infra, developer tool) does not fire: this is a consumer media app. Rule 3 does not fire: the palette is explicitly achromatic with one functional green, and the type voice is systematic rather than informal. Rule 4 is therefore the terminal answer — **Calm**, whose signature of short opacity-led fades with little travel is exactly what "slight background lightening" on a card hover asks for. At a Cinematic 400ms base a play button would feel broken.

Only `transform` and `opacity` are animated — never `width`, `height`, `top`, `left` or `margin`.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` of the card's lightening overlay — the extracted "slight background lightening", expressed as an overlay fade rather than an animated background colour | Same crossfade, capped at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.97)` on pills and circular controls, plus `opacity` | Scale removed; `opacity` only, at `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Ring appears instantly and is never suppressed |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` 0→1 and `transform: translateY(8px)`→0 on the content pane only; the sidebar and now-playing bar never transition | Travel removed; opacity fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px)`→0, with `{shadow.heavy}` already in place | Travel removed; scrim and panel fade at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-base}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-6px)`→0, with `{shadow.medium}` | Travel removed; fade at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(12px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| List enter (playlist / album grid) | `{motion.duration-base}`, staggered by `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)`→0 | Stagger and travel removed; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading | 1200ms, infinite | linear | `opacity` pulse on an album-art placeholder filled with `{colors.surface-interactive}` — never a layout-affecting skeleton | Loader frozen; a static placeholder remains |

Exit is always shorter than its matching entrance. Nothing animates on first paint in a way that delays content: the grid's stagger runs on tiles that have already painted and never gates the first row. **No brand ambience is prescribed.** The only infinite animation is the loader; the equalizer and scrubber motion of a real player is not documented in this file, so none is invented here.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: every translate, the press scale, the playlist-grid stagger,
     and the album-art placeholder pulse. */
  /* Kept: opacity fades only, capped at {motion.duration-reduced} (150ms),
     plus the focus ring, which appears instantly and is never removed. */
  *, *::before, *::after {
    transition-property: opacity;
    transition-duration: 150ms; /* {motion.duration-reduced} */
    animation: none;
  }
}
```

## Accessibility

Every ratio below is computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter. **The extracted brand values are frozen: the failures listed here are real failures of the real Spotify interface, disclosed rather than corrected.** The good news first — Spotify's ink ladder is genuinely strong. Every text tone, including all three semantic tones, clears AA on all five charcoal grounds with margin. Both failures are boundaries: the grey the source calls "button borders on dark", and the black border the source gives the focused search input.

### Measured contrast — text on every surface this file defines

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `text` #ffffff on `canvas` #121212 | 18.73:1 | 4.5:1 | Pass |
| `text` #ffffff on `surface` #181818 | 17.76:1 | 4.5:1 | Pass |
| `text` #ffffff on `surface-interactive` #1f1f1f | 16.48:1 | 4.5:1 | Pass |
| `text` #ffffff on `surface-card` #252525 | 15.33:1 | 4.5:1 | Pass |
| `text` #ffffff on `surface-card-alt` #272727 | 14.94:1 | 4.5:1 | Pass |
| `text-emphasis` #fdfdfd on `canvas` | 18.42:1 | 4.5:1 | Pass |
| `text-emphasis` #fdfdfd on `surface-card-alt` | 14.69:1 | 4.5:1 | Pass |
| `muted` #b3b3b3 on `canvas` | 8.93:1 | 4.5:1 | Pass |
| `muted` #b3b3b3 on `surface` | 8.47:1 | 4.5:1 | Pass |
| `muted` #b3b3b3 on `surface-interactive` | 7.86:1 | 4.5:1 | Pass |
| `muted` #b3b3b3 on `surface-card` | 7.31:1 | 4.5:1 | Pass |
| `muted` #b3b3b3 on `surface-card-alt` | 7.12:1 | 4.5:1 | Pass — the worst case for Silver across all five grounds |
| `muted-bright` #cbcbcb on `canvas` | 11.55:1 | 4.5:1 | Pass |
| `muted-bright` #cbcbcb on `surface-card-alt` | 9.21:1 | 4.5:1 | Pass |
| `on-light` #181818 on `button-light` #eeeeee | 15.30:1 | 4.5:1 | Pass — the light pill's own pair |

### Measured contrast — accent and semantic tones

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `on-accent` #000000 on `accent` #1ed760 | 10.94:1 | 4.5:1 | Pass — black on green, as the source's own play-button prompt specifies |
| `on-accent` #000000 on `accent-border` #1db954 | 8.12:1 | 4.5:1 | Pass |
| `text` #ffffff on `accent` #1ed760 | 1.92:1 | 4.5:1 | **Fail — never use this pair.** White on Spotify Green is unusable. The source's Don'ts already forbid green as a background for anything but functional controls, and those controls carry a black icon |
| `accent` #1ed760 as text on `canvas` | 9.76:1 | 4.5:1 | Pass |
| `accent` #1ed760 as text on `surface-card-alt` | 7.79:1 | 4.5:1 | Pass |
| `accent-border` #1db954 as text on `canvas` | 7.24:1 | 4.5:1 | Pass |
| `accent-border` #1db954 as text on `surface-card-alt` | 5.78:1 | 4.5:1 | Pass |
| `negative` #f3727f on `canvas` | 6.71:1 | 4.5:1 | Pass |
| `negative` #f3727f on `surface-card-alt` | 5.35:1 | 4.5:1 | Pass |
| `warning` #ffa42b on `canvas` | 9.45:1 | 4.5:1 | Pass |
| `warning` #ffa42b on `surface-card-alt` | 7.54:1 | 4.5:1 | Pass |
| `announcement` #539df5 on `canvas` | 6.70:1 | 4.5:1 | Pass |
| `announcement` #539df5 on `surface-card-alt` | 5.34:1 | 4.5:1 | Pass |

All three semantic tones are declared as text colours in the source (`--text-negative`, `--text-warning`, `--text-announcement`) and never as fills, so 4.5:1 is the right threshold for each, and each clears it on every ground in the file.

### Measured contrast — boundaries

| Pair | Measured | Required | Verdict |
|---|---|---|---|
| `divider` #b3b3b3 on `canvas` #121212 | 8.93:1 | 3:1 | Pass — the Separator tone, the strongest boundary the palette owns |
| `divider` #b3b3b3 on `surface` #181818 | 8.47:1 | 3:1 | Pass |
| `border-outline` #7c7c7c on `canvas` #121212 | 4.49:1 | 3:1 | Pass |
| `border-outline` #7c7c7c on `surface` #181818 | 4.25:1 | 3:1 | Pass |
| `border-outline` #7c7c7c on `surface-interactive` #1f1f1f | 3.95:1 | 3:1 | Pass — the Outlined Pill's own pair |
| `border-outline` #7c7c7c on `surface-card-alt` #272727 | 3.58:1 | 3:1 | Pass — its worst case across all five grounds |
| `border` #4d4d4d on `canvas` #121212 | 2.22:1 | 3:1 | **Fail — frozen decorative hairline.** Border Gray is the source's "button borders on dark" and it reaches the boundary threshold on no surface in this file. Never the sole boundary of a control; use `{colors.border-outline}` where an edge must be seen |
| `border` #4d4d4d on `surface` #181818 | 2.10:1 | 3:1 | **Fail — frozen decorative hairline** |
| `border` #4d4d4d on `surface-interactive` #1f1f1f | 1.95:1 | 3:1 | **Fail — frozen decorative hairline**, on the exact fill the dark pills use |
| `border` #4d4d4d on `surface-card-alt` #272727 | 1.77:1 | 3:1 | **Fail — frozen decorative hairline** |
| `border-focus` #000000 on `surface-interactive` #1f1f1f | 1.27:1 | 3:1 | **Fail — real brand failure, and the serious one.** This is the search input's extracted focus treatment: the border turns black on a `#1f1f1f` field. A sighted keyboard user gets no visible focus indicator at all |
| `border-focus` #000000 on `canvas` #121212 | 1.12:1 | 3:1 | **Fail — real brand failure** |
| `border-focus` #000000 on `surface` #181818 | 1.18:1 | 3:1 | **Fail — real brand failure** |
| `border-focus` #000000 on `surface-card-alt` #272727 | 1.41:1 | 3:1 | **Fail — real brand failure** |

The `{colors.border-focus}` binding on `{components.input-search-focus}` is left exactly as extracted. Re-pointing it at the prescribed ring would make this document describe a product that does not exist; the question of changing the real site is raised under Needs approval in the audit report.

### Component pairs

| Component | Measured | Required | Verdict |
|---|---|---|---|
| `button-dark-pill` — #ffffff on #1f1f1f at 14px/700 | 16.48:1 | 4.5:1 | Pass |
| `button-dark-pill-muted` — #b3b3b3 on #1f1f1f at 14px/700 | 7.86:1 | 4.5:1 | Pass |
| `button-dark-large-pill` — #ffffff on #181818 at 14px/700 | 17.76:1 | 4.5:1 | Pass |
| `button-light-pill` — #181818 on #eeeeee at 14px/700 | 15.30:1 | 4.5:1 | Pass |
| `button-outlined-pill` — #ffffff on a transparent fill | — | — | Ground not stated by the source, so nothing to measure; its 1px #7c7c7c outline is measured above |
| `button-circular-play` — #ffffff on #1f1f1f | 16.48:1 | 4.5:1 | Pass |
| `button-circular-play-green` — #000000 on #1ed760 | 10.94:1 | 4.5:1 | Pass |
| `card` — #ffffff on #181818 at 16px/700 | 17.76:1 | 4.5:1 | Pass |
| `card-alt` — #b3b3b3 on #1f1f1f at 14px/400 | 7.86:1 | 4.5:1 | Pass |
| `card-elevated` — #ffffff on #252525 at 16px/400 | 15.33:1 | 4.5:1 | Pass |
| `card-elevated-alt` — #ffffff on #272727 at 16px/400 | 14.94:1 | 4.5:1 | Pass |
| `input-search` — #ffffff on #1f1f1f at 16px/400 | 16.48:1 | 4.5:1 | Pass |
| `input-search-focus` — its #000000 focus border on #1f1f1f | 1.27:1 | 3:1 | **Fail**, as disclosed above |
| `nav-sidebar` — #ffffff on #121212 at 14px/700 | 18.73:1 | 4.5:1 | Pass |
| `nav-item-inactive` — #b3b3b3 on #121212 at 14px/400 | 8.93:1 | 4.5:1 | Pass |
| `divider-rule` — a 1px #b3b3b3 rule on #121212 | 8.93:1 | 3:1 | Pass |

### Focus ring visibility on every surface this file defines

`{colors.focus}` (`#1ed760`) is drawn as a 2px ring with a **2px offset, outside the control**, so it is judged against the surface behind it — which is what WCAG 2.2 Focus Appearance asks for. **Prescribed, not extracted.** It reuses Spotify Green, which the source already assigns to "active states", so no new colour enters the palette and no alias token was added.

| Surface it is drawn on | Measured | Required | Verdict |
|---|---|---|---|
| `canvas` #121212 | 9.76:1 | 3:1 | Pass |
| `surface` #181818 | 9.25:1 | 3:1 | Pass |
| `surface-interactive` #1f1f1f | 8.59:1 | 3:1 | Pass |
| `surface-card` #252525 | 7.99:1 | 3:1 | Pass |
| `surface-card-alt` #272727 | 7.79:1 | 3:1 | Pass — its worst case |

One ring serves this file and a second polarity is not needed. `{colors.button-light}` (`#eeeeee`) is a rare light **control fill**, not a surface the ring is drawn on: the green ring is 1.65:1 against it, which is exactly why the ring sits outside the pill, on the dark ground behind it, at 9.76:1. Over album artwork, which has no measurable colour, the ring is two-tone — 2px `{colors.focus}` with a 1px outer edge in `{colors.canvas}` over light artwork and in `{colors.text}` over dark artwork. A single-tone ring cannot be guaranteed on a surface that is whatever cover image the listener chose.

### Minimum tap target
Not measurable from this document. The source gives padding for four controls (8px 16px; 0px 43px; 4px 16px 4px 36px; 12px on the circular play button) and font sizes from 10px to 24px, but no height or width for any control and no icon box size. The 44×44px minimum can therefore be neither confirmed nor failed here: the circular play button at 12px padding would need a 20px icon to reach 44px, and the source does not say what the icon is. Recorded in Known Gaps.

### Reduced motion
`@media (prefers-reduced-motion: reduce)` removes every translate, the press scale, the playlist-grid stagger and the album-art placeholder pulse. Opacity fades remain, capped at `{motion.duration-reduced}` (150ms). The focus ring is never animated away.

### Real failures, stated plainly
1. **The focused search input has no visible focus indicator.** `#000000` on `#1f1f1f` is 1.27:1. This is the most consequential accessibility defect in the extracted system, and it is the only focus treatment the source records.
2. **Border Gray is not a boundary.** At 2.22:1 on the canvas and 1.95:1 on the pill fill it cannot carry a component edge, and the source's own Don'ts ("don't expose raw gray borders") suggest it was never meant to.
3. **The charcoal layers are not separable by colour** — 1.03:1 to 1.25:1 between adjacent levels. Depth here depends entirely on shadow, radius and album art, so a user who cannot resolve the shadow cannot resolve the card.

## Do's and Don'ts

### Do
- Use near-black backgrounds (`#121212`–`#1f1f1f`) — depth through shade variation
- Apply Spotify Green (`#1ed760`) only for play controls, active states, and primary CTAs
- Use pill shape (500px–9999px) for all buttons — circular (50%) for play controls
- Apply uppercase + wide letter-spacing (1.4px–2px) on button labels
- Keep typography compact (10px–24px range) — this is an app, not a magazine
- Use heavy shadows (`0.3–0.5 opacity`) for elevated elements on dark backgrounds
- Let album art provide color — the UI itself is achromatic
- Draw any boundary that must actually be seen in `{colors.border-outline}` (`#7c7c7c`) or `{colors.divider}` (`#b3b3b3`), and keep `{colors.border}` for decoration
- Draw the focus ring in `{colors.focus}` at a 2px offset outside the control, never inside it

### Don't
- Don't use Spotify Green decoratively or on backgrounds — it's functional only
- Don't use light backgrounds for primary surfaces — the dark immersion is core
- Don't skip the pill/circle geometry on buttons — square buttons break the identity
- Don't use thin/subtle shadows — on dark backgrounds, shadows need to be heavy to be visible
- Don't add additional brand colors — green + achromatic grays is the complete palette
- Don't use relaxed line-heights — Spotify's typography is compact and dense
- Don't expose raw gray borders — use shadow-based or inset borders instead
- Don't put white text on Spotify Green — 1.92:1, and the green controls carry a black icon
- Don't rely on `{colors.border-focus}` (`#000000`) as a focus indicator — it is 1.27:1 on the input it belongs to
- Don't rely on the charcoal step alone to separate a card from the page — 1.06:1 is not a visible edge
- Don't animate `width`, `height`, `top`, `left` or `margin` — `transform` and `opacity` only

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <425px | Compact mobile layout |
| Mobile | 425–576px | Standard mobile |
| Tablet | 576–768px | 2-column grid |
| Tablet Large | 768–896px | Expanded layout |
| Desktop Small | 896–1024px | Sidebar visible |
| Desktop | 1024–1280px | Full desktop layout |
| Large Desktop | >1280px | Expanded grid |

### Collapsing Strategy
- Sidebar: full → collapsed → hidden
- Album grid: 5 columns → 3 → 2 → 1
- Now-playing bar: maintained at all sizes
- Search: pill input maintained, width adjusts
- Navigation: sidebar → bottom bar on mobile

### Touch Targets
Not stated by the source. It records control padding but no control height at any breakpoint, so no tap target is confirmed or failed; see Known Gaps.

## Known Gaps

This file was one of the collection's ten legacy documents: it carried no frontmatter token block and used numbered headings (`## 1. Visual Theme & Atmosphere` and so on). The `colors`, `typography`, `spacing`, `rounded`, `shadow` and `components` groups above were built **only** from values already written in its prose. Nothing was invented to fill a column, and no alias token was added to satisfy a role pattern. What the prose does not contain is listed here.

- **No motion values at all.** The source describes no duration, easing curve, transition, scroll behaviour or choreography anywhere. The entire `motion:` group and the whole Motion & Animation section are prescribed, as their first lines state.
- **The motion profile was switched from Cinematic to Calm**, argued from the file's own evidence in the Motion & Animation section and in `theme-audit/reports/A67-spotify.md`. `theme-audit/roster.md` still records Cinematic; the roster is read-only to this agent, and the mismatch is flagged under Shared issues in that report so the roster can be brought into line.
- **Interaction states are almost entirely absent.** The source records three: the card hover ("slight background lightening"), the navigation active weight and colour, and the search input's focus border. **Press, disabled, loading and selected appear nowhere in the file, for any component**, and `error` appears only as a colour role (`--text-negative`) that is never bound to a control. The Components section above therefore *marks* state coverage rather than filling it, and the states score is accepted as lost rather than padded with invented behaviour. The most conspicuous absence is a loading and a selected state for the play control.
- **The card hover is unquantified.** "Slight background lightening" names no target tone and no overlay opacity, so there is no hover token. The three elevated charcoals (`#1f1f1f`, `#252525`, `#272727`) are plausible hover targets but the source does not say so, and none is bound as one.
- **The one extracted focus treatment fails.** `{colors.border-focus}` (`#000000`) is 1.27:1 on the input it belongs to. Its binding is left as extracted; every other focus treatment in this file is prescribed and labelled as such. The live site's focus appearance for every control other than the search input is unknown.
- **No tap-target dimensions.** Padding for four controls, font sizes for fourteen type roles, and no height, width or icon box anywhere, so the 44×44px minimum cannot be evaluated from this document.
- **Four paddings sit outside the spacing ladder**: 36px and 43px (asymmetric pill insets), 48px and 96px (the search input's icon-aware horizontal padding). They are recorded as the source states them rather than snapped to the 1px–20px scale, which they are plainly not part of.
- **Line height is `normal` for nine of fourteen type roles**, and letter-spacing is `normal` for eleven. Those are the source's own words, not a failed extraction, and they are carried through unresolved rather than replaced with a computed value. Two roles record ranges (`1.50–1.54`, `1.4px–2px`) and both ends are kept.
- **The radius ladder is three spellings of one intent.** 100px, 500px and 9999px all mean "full pill" at different component widths, and `10px–20px` is stated as a range with no canonical value. Nothing was collapsed or interpolated.
- **The charcoal layers are not separable by colour** (1.03:1 to 1.25:1 between adjacent levels) and the source states no non-colour affordance for a card edge beyond shadow and radius. Elevation is expressed as background steps for levels 0–1 and as shadows for levels 2–3, with no stated background for the elevated levels and no stated shadow for the base ones; the two halves of the ladder never meet.
- **No light-mode canvas.** `{colors.button-light}` (`#eeeeee`) is described as a control fill for "light-mode buttons (rare)" with no page surface behind it, so this file documents one polarity and therefore one focus ring. If a light surface exists on the real site, it is not in this document.
- **Several components have no colour values and are left out of `components:`** rather than given invented grounds: the now-playing bar (described only as "full-width at bottom"), the badge (a radius and a type role, no fill or ink), and the dropdown menu (a shadow level, no background).
- **No gradient values.** Real Spotify derives per-playlist gradients from album art; this document does not mention a gradient, so none is recorded.
- **No spacing value above 20px**, although the Layout section describes a sidebar, a grid and a bottom bar that imply larger gaps. The ladder is recorded exactly as stated.
- **`{colors.divider}` and `{colors.muted}` are the same hex** (`#b3b3b3`). They are kept as two tokens because the source names them separately with separate jobs — "Separator: divider lines" under Surface & Border, and "Silver: secondary text, muted labels, inactive nav" under Text. Neither exists to satisfy a pattern.

## Agent Prompt Guide

### Quick Color Reference
- Background: Near Black (`#121212`)
- Surface: Dark Card (`#181818`)
- Text: White (`#ffffff`)
- Secondary text: Silver (`#b3b3b3`)
- Accent: Spotify Green (`#1ed760`)
- Border: `#4d4d4d`
- Error: Negative Red (`#f3727f`)

### Example Component Prompts
- "Create a dark card: #181818 background, 8px radius. Title at 16px SpotifyMixUI weight 700, white text. Subtitle at 14px weight 400, #b3b3b3. Shadow rgba(0,0,0,0.3) 0px 8px 8px on hover."
- "Design a pill button: #1f1f1f background, white text, 9999px radius, 8px 16px padding. 14px SpotifyMixUI weight 700, uppercase, letter-spacing 1.4px."
- "Build a circular play button: Spotify Green (#1ed760) background, #000000 icon, 50% radius, 12px padding."
- "Create search input: #1f1f1f background, white text, 500px radius, 12px 48px padding. Inset border: rgb(124,124,124) 0px 0px 0px 1px inset."
- "Design navigation sidebar: #121212 background. Active items: 14px weight 700, white. Inactive: 14px weight 400, #b3b3b3."

### Iteration Guide
1. Start with #121212 — everything lives in near-black darkness
2. Spotify Green for functional highlights only (play, active, CTA)
3. Pill everything — 500px for large, 9999px for small, 50% for circular
4. Uppercase + wide tracking on buttons — the systematic label voice
5. Heavy shadows (0.3–0.5 opacity) for elevation — light shadows are invisible on dark
6. Album art provides all the color — the UI stays achromatic
