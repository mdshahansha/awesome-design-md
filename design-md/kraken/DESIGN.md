---
version: alpha
name: Kraken-design-analysis
description: A clean, trustworthy crypto-exchange interface on a white canvas, commanded by Kraken Purple. Display headings run the proprietary Kraken-Brand face at 700 with negative tracking; Kraken-Product (IBM Plex Sans fallback) is the UI workhorse. Buttons sit at a 12px radius — rounded but never pill. Shadows are whisper-level; a single green carries positive and success states.

colors:
  primary: "#7132f5"
  purple-dark: "#5741d8"
  purple-deep: "#5b1ecf"
  purple-subtle: "rgba(133,91,251,0.16)"
  on-primary: "#ffffff"
  canvas: "#ffffff"
  surface: "#ffffff"
  ink: "#101114"
  text-secondary: "#9497a9"
  neutral-cool: "#686b82"
  neutral-subtle: "rgba(104,107,130,0.12)"
  gray-subtle: "rgba(148,151,169,0.08)"
  badge-ink: "#484b5e"
  border-subtle: "#dedee5"
  success: "#149e61"
  success-subtle: "rgba(20,158,97,0.16)"
  success-text: "#026b3f"
  focus: "#101114"
  focus-inner: "#ffffff"

typography:
  display-hero:
    fontFamily: "Kraken-Brand, IBM Plex Sans, Helvetica, Arial"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: -1px
  section-heading:
    fontFamily: "Kraken-Brand, IBM Plex Sans, Helvetica, Arial"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: -0.5px
  sub-heading:
    fontFamily: "Kraken-Brand, IBM Plex Sans, Helvetica, Arial"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.5px
  feature-title:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: normal
  body:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: normal
  body-medium:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: normal
  button:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial"
    fontSize: 16px
    fontWeight: 500-600
    lineHeight: 1.38
    letterSpacing: normal
  caption:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial"
    fontSize: 14px
    fontWeight: 400-700
    lineHeight: 1.43-1.71
    letterSpacing: normal
  small:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial"
    fontSize: 12px
    fontWeight: 400-500
    lineHeight: 1.33
    letterSpacing: normal
  micro:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial"
    fontSize: 7px
    fontWeight: 500
    lineHeight: 1.00
    textTransform: uppercase

spacing:
  s1: 1px
  s2: 2px
  s3: 3px
  s4: 4px
  s5: 5px
  s6: 6px
  s8: 8px
  s10: 10px
  s12: 12px
  s13: 13px
  s15: 15px
  s16: 16px
  s20: 20px
  s24: 24px
  s25: 25px

rounded:
  xs: 3px
  sm: 6px
  md: 8px
  lg: 10px
  xl: 12px
  xxl: 16px
  pill: 9999px
  circle: 50%

shadow:
  subtle: "rgba(0,0,0,0.03) 0px 4px 24px"
  micro: "rgba(16,24,40,0.04) 0px 1px 4px"

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
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    padding: 13px 16px
  button-outlined:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.purple-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    border: 1px solid {colors.purple-dark}
  button-subtle:
    backgroundColor: "{colors.purple-subtle}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    padding: 8px
  button-white:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    shadow: "{shadow.subtle}"
  button-secondary-gray:
    backgroundColor: "{colors.gray-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
  badge-success:
    backgroundColor: "{colors.success-subtle}"
    textColor: "{colors.success-text}"
    typography: "{typography.small}"
    rounded: "{rounded.sm}"
  badge-neutral:
    backgroundColor: "{colors.neutral-subtle}"
    textColor: "{colors.badge-ink}"
    typography: "{typography.small}"
    rounded: "{rounded.md}"
---

# Design System Inspired by Kraken

## Overview

Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color. The design operates on white backgrounds with Kraken Purple (`{colors.primary}` — #7132f5, `{colors.purple-dark}` — #5741d8, `{colors.purple-deep}` — #5b1ecf) creating a distinctive, professional crypto identity. The proprietary Kraken-Brand font handles display headings with bold (700) weight and negative tracking, while Kraken-Product (with IBM Plex Sans fallback) serves as the UI workhorse.

**Key Characteristics:**
- Kraken Purple (`{colors.primary}`) as primary brand with darker variants (`{colors.purple-dark}`, `{colors.purple-deep}`)
- Kraken-Brand (display) + Kraken-Product (UI) dual font system
- Near-black (`{colors.ink}`) text with cool blue-gray neutral scale
- 12px radius buttons — `{rounded.xl}`, rounded but not pill
- Subtle shadows (`{shadow.subtle}`) — whisper-level
- Green accent (`{colors.success}`) for positive/success states

This file was converted from the early numbered-heading format. Every hex, type value and component in the token block above was read out of this file's own prose; nothing was added from outside it. What the prose never stated — hover and press colours, inputs, navigation, cards, tap-target sizes — is listed in Known Gaps rather than guessed at.

## Colors

### Primary
- **Kraken Purple** (`{colors.primary}` — #7132f5): Primary CTA, brand accent, links. 6.04:1 on `{colors.canvas}`.
- **Purple Dark** (`{colors.purple-dark}` — #5741d8): Button borders, outlined variants. 6.66:1 on `{colors.canvas}`.
- **Purple Deep** (`{colors.purple-deep}` — #5b1ecf): Deepest purple. 8.3:1 on `{colors.canvas}`.
- **Purple Subtle** (`{colors.purple-subtle}` — rgba(133,91,251,0.16)): Purple at 16% — subtle button backgrounds. Composited over `{colors.canvas}` this resolves to #ebe5fe, and `{colors.primary}` on it measures 4.94:1.
- **Near Black** (`{colors.ink}` — #101114): Primary text. 18.88:1 on `{colors.canvas}`.

### Neutral
- **Cool Gray** (`{colors.neutral-cool}` — #686b82): Primary neutral, borders at 24% opacity. At 24% over `{colors.canvas}` that boundary resolves to #dbdbe1 — 1.38:1, decorative only.
- **Silver Blue** (`{colors.text-secondary}` — #9497a9): Secondary text, muted elements. **This is the real extracted value and it fails WCAG 1.4.3 for body text: 2.89:1 against `{colors.canvas}`, against a 4.5:1 minimum.** It is left unchanged because falsifying it would make this document wrong about Kraken. See Accessibility.
- **White** (`{colors.canvas}` / `{colors.surface}` — #ffffff): Primary surface. Kraken's canvas and its card surface are the same white; depth comes from `{shadow.subtle}`, not from a second surface tone.
- **Border Gray** (`{colors.border-subtle}` — #dedee5): Divider borders. **1.34:1 against `{colors.canvas}`, against a 3:1 non-text minimum.** Scoped to decoration: dividers and section rules only. It is never the sole boundary of a control in this file — `{component.button-outlined}` carries a 1px `{colors.purple-dark}` outline at 6.66:1 instead.
- **Badge Ink** (`{colors.badge-ink}` — #484b5e): Neutral badge text. 8.59:1 on `{colors.canvas}`.

### Semantic
- **Green** (`{colors.success}` — #149e61): Success/positive, used at 16% opacity (`{colors.success-subtle}`) for badge fills. As a fill it is outside 1.4.3; as text it measures 3.45:1 on `{colors.canvas}` and fails. Do not set it as body text.
- **Green Dark** (`{colors.success-text}` — #026b3f): Badge text. 6.61:1 on `{colors.canvas}`, 5.49:1 on the composited `{colors.success-subtle}` fill (#d9efe6).

### Focus
- **Focus** (`{colors.focus}` — #101114) with **Focus Inner** (`{colors.focus-inner}` — #ffffff): **Prescribed, not extracted — no file in this repo documented a focus ring.** Kraken's palette is a single purple hue on white, so a purple ring cannot work: `{colors.purple-deep}` on the `{colors.primary}` button measures 1.37:1. The ring therefore uses the brand's own ink with a mandatory 2px offset of the opposite polarity, per SPEC section 1. Measured: **18.88:1 against `{colors.canvas}`** and `{colors.surface}`, **3.13:1 against the `{colors.primary}` button fill**, and 15.44:1 against the composited `{colors.purple-subtle}` fill. The white inner band separates from the ring at 18.88:1.

## Typography

### Font Families
- **Display**: `Kraken-Brand`, fallbacks: `IBM Plex Sans, Helvetica, Arial`
- **UI / Body**: `Kraken-Product`, fallbacks: `Helvetica Neue, Helvetica, Arial`

### Hierarchy

Every role carries size, weight and line height. Where the original extraction recorded a **range** rather than a single value, the range is preserved verbatim in the token block — inventing a single number would be a claim this file cannot support.

| Role | Token | Font | Size | Weight | Line Height | Letter Spacing |
|------|-------|------|------|--------|-------------|----------------|
| Display Hero | `{typography.display-hero}` | Kraken-Brand | 48px | 700 | 1.17 | -1px |
| Section Heading | `{typography.section-heading}` | Kraken-Brand | 36px | 700 | 1.22 | -0.5px |
| Sub-heading | `{typography.sub-heading}` | Kraken-Brand | 28px | 700 | 1.29 | -0.5px |
| Feature Title | `{typography.feature-title}` | Kraken-Product | 22px | 600 | 1.20 | normal |
| Body | `{typography.body}` | Kraken-Product | 16px | 400 | 1.38 | normal |
| Body Medium | `{typography.body-medium}` | Kraken-Product | 16px | 500 | 1.38 | normal |
| Button | `{typography.button}` | Kraken-Product | 16px | 500–600 | 1.38 | normal |
| Caption | `{typography.caption}` | Kraken-Product | 14px | 400–700 | 1.43–1.71 | normal |
| Small | `{typography.small}` | Kraken-Product | 12px | 400–500 | 1.33 | normal |
| Micro | `{typography.micro}` | Kraken-Product | 7px | 500 | 1.00 | uppercase (see note) |

**Micro note.** The original table recorded `uppercase` in its Letter Spacing column. That is a text transform, not a tracking value, so it is carried as `textTransform: uppercase` and the actual letter-spacing of this role is unknown — see Known Gaps. At 7px, `{typography.micro}` is below any practical reading floor; restrict it to ornamental labels whose content is also available at `{typography.small}` or larger.

**Body readability.** `{typography.body}` (16px / 400) in `{colors.ink}` on `{colors.canvas}` and on `{colors.surface}` measures 18.88:1 — comfortably clear of AA. The same body size in `{colors.text-secondary}` measures 2.89:1 and is not usable for running text.

## Layout

### Spacing

The extracted ladder is `{spacing.s1}` 1px · `{spacing.s2}` 2px · `{spacing.s3}` 3px · `{spacing.s4}` 4px · `{spacing.s5}` 5px · `{spacing.s6}` 6px · `{spacing.s8}` 8px · `{spacing.s10}` 10px · `{spacing.s12}` 12px · `{spacing.s13}` 13px · `{spacing.s15}` 15px · `{spacing.s16}` 16px · `{spacing.s20}` 20px · `{spacing.s24}` 24px · `{spacing.s25}` 25px.

This is a measured inventory, not a designed scale, and the file should say so: 1px, 2px, 3px and 5px are hairline and optical-nudge values rather than layout steps, and 13px, 15px and 25px sit off any 4px rhythm — 13px survives because `{component.button-primary}` genuinely pads 13px × 16px. For new layout work use the 4-multiples (`{spacing.s4}`, `{spacing.s8}`, `{spacing.s12}`, `{spacing.s16}`, `{spacing.s20}`, `{spacing.s24}`) and treat the off-scale values as the specific one-off measurements they are.

Section-level vertical rhythm, container widths and grid column counts were never captured for this site. See Known Gaps.

## Elevation & Depth

Depth in this system is expressed **one way: shadow.** There is no raised surface tone — `{colors.surface}` and `{colors.canvas}` are the same white — and no elevation border. Borders in this file are a button-variant device (`{component.button-outlined}`) and a divider device (`{colors.border-subtle}`), never a stand-in for height.

| Level | Token | Treatment | Use |
|---|---|---|---|
| Flat | — | No shadow, no border | Page bands, body sections |
| Micro | `{shadow.micro}` | `rgba(16,24,40,0.04) 0px 1px 4px` | Smallest lifted elements |
| Subtle | `{shadow.subtle}` | `rgba(0,0,0,0.03) 0px 4px 24px` | `{component.button-white}`, whisper-level lift |
| Focus | `{colors.focus}` | 2px `{colors.focus}` ring with a 2px `{colors.focus-inner}` offset | Keyboard focus on any interactive element |

Both shadows sit at 3–4% alpha. The ladder has exactly two steps and no heavy or glow tier; anything that needs to read as "above the page" more strongly than `{shadow.subtle}` is outside this system.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 3px | Smallest extracted corner |
| `{rounded.sm}` | 6px | `{component.badge-success}` |
| `{rounded.md}` | 8px | `{component.badge-neutral}` |
| `{rounded.lg}` | 10px | `{component.button-white}` |
| `{rounded.xl}` | 12px | All other buttons — the signature button corner, and the maximum for a button |
| `{rounded.xxl}` | 16px | Largest extracted rectangular corner |
| `{rounded.pill}` | 9999px | Fully round elements — **never buttons** |
| `{rounded.circle}` | 50% | Circular elements, avatars |

The ladder is internally consistent: 3 · 6 · 8 · 10 · 12 · 16, then the two fully-round values. No value in the components block sits outside it. The one hard rule the brand states for itself is that `{rounded.pill}` never reaches a button — `{rounded.xl}` (12px) is the ceiling.

## Components

> **Hover and press *styling* is not extracted; state *coverage* is.** The original extraction captured no hover, pressed, disabled, loading, selected or error value for this site, so no such hex is claimed below. What each component supports is named in the state matrix, and every unknown value says so.

### State Matrix

A dash means the state does not exist for that component — not that it was skipped.

| Component | Default | Hover | Focus-visible | Active / Pressed | Disabled | Loading | Selected | Error |
|---|---|---|---|---|---|---|---|---|
| `button-primary` | yes | tone shift toward `{colors.purple-dark}`, exact value not extracted | 2px `{colors.focus}` ring + 2px `{colors.focus-inner}` offset | shift toward `{colors.purple-deep}`, exact value not extracted | not extracted — see Known Gaps | label swaps to an inline spinner, the button keeps its rest box | — | — |
| `button-outlined` | yes | tone shift only, value not extracted | 2px `{colors.focus}` ring + offset | value not extracted | not extracted | spinner replaces the label | — | — |
| `button-subtle` | yes | `{colors.purple-subtle}` deepens, value not extracted | 2px `{colors.focus}` ring + offset | value not extracted | not extracted | — | — | — |
| `button-white` | yes | `{shadow.subtle}` strengthens, value not extracted | 2px `{colors.focus}` ring + offset | value not extracted | not extracted | — | — | — |
| `button-secondary-gray` | yes | `{colors.gray-subtle}` deepens, value not extracted | 2px `{colors.focus}` ring + offset | value not extracted | not extracted | — | — | — |
| `badge-success` | yes | — | — | — | — | — | — | — |
| `badge-neutral` | yes | — | — | — | — | — | — | — |

`badge-success` and `badge-neutral` genuinely have **one** state each. They are non-interactive status fills, carry no affordance of their own, and are listed so the gap is explicit rather than assumed. No selected and no error component exists anywhere in this file's prose; both are recorded in Known Gaps instead of being invented here.

### Buttons

**`button-primary`** — Primary Purple. Background `{colors.primary}` (#7132f5), text `{colors.on-primary}` (#ffffff) at 6.04:1, type `{typography.button}`, padding `{spacing.s13}` × `{spacing.s16}` (13px 16px), radius `{rounded.xl}` (12px).

**`button-outlined`** — Purple Outlined. Background `{colors.canvas}`, text `{colors.purple-dark}` (#5741d8) at 6.66:1, border 1px solid `{colors.purple-dark}` at 6.66:1 non-text contrast, radius `{rounded.xl}` (12px).

**`button-subtle`** — Purple Subtle. Background `{colors.purple-subtle}` (purple at 16%), text `{colors.primary}`, padding `{spacing.s8}` (8px), radius `{rounded.xl}` (12px). Text on the composited fill measures 4.94:1.

**`button-white`** — White Button. Background `{colors.canvas}`, text `{colors.ink}` at 18.88:1, radius `{rounded.lg}` (10px), shadow `{shadow.subtle}`. The only button in the set that uses elevation instead of colour to separate itself from the page.

**`button-secondary-gray`** — Secondary Gray. Background `{colors.gray-subtle}` (rgba(148,151,169,0.08)), text `{colors.ink}` at 17.6:1 over the composited fill, radius `{rounded.xl}` (12px).

### Badges

- **`badge-success`** — `{colors.success-subtle}` fill, `{colors.success-text}` text at 5.49:1, radius `{rounded.sm}` (6px).
- **`badge-neutral`** — `{colors.neutral-subtle}` fill, `{colors.badge-ink}` text at 7.36:1, radius `{rounded.md}` (8px).

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity. It was not measured from the live site — no duration, easing curve or property below was extracted from Kraken's CSS or observed in a recording.** Treat it as the motion that *belongs* to this palette and type voice, and replace any value here with a measured one the moment one exists.

**Profile: Calm** (composed, editorial), and Calm is the right call for this file. The canvas is plain white with no gradient or mesh; the brand's own prose calls its shadows "whisper-level" at 3–4% alpha; the palette is a single purple hue plus one green, not a saturated multi-colour set; and the document's first sentence asks for "clean, trustworthy". A crypto exchange showing live balances has a further reason to avoid springy overshoot: a number that bounces reads as a number that is still changing. This is not a developer tool (no terminal or IDE language), not luxury or hardware (no full-bleed photography, no slow reveal), and not illustration-led, so SPEC's assignment rules fall through to Calm.

Calm values: base `{motion.duration-base}` (250ms), symmetric `{motion.ease-standard}`, stagger `{motion.stagger-step}` (40ms). Opacity leads; travel stays at 4–8px and never crosses the viewport.

### Interaction Table

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, links, badges) | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` of the tone layer | Unchanged — already opacity-only and at `{motion.duration-reduced}` |
| Press (`button-primary` toward `{colors.purple-deep}`) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the press layer; no scale | Unchanged — the colour swap reads the same either way |
| Focus ring appears | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Ring appears at zero duration — it must never lag the keyboard |
| Page / route transition | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` 0→1, `transform: translateY(8px→0)` | Travel removed; cross-fade only, at `{motion.duration-reduced}` |
| Modal / drawer | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px→0)` for the modal, `translateX(100%→0)` for the drawer | Travel removed; both cross-fade at `{motion.duration-reduced}`. Backdrop still fades |
| Dropdown | enter `{motion.duration-fast}`, exit `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px→0)` | Travel removed; fade at `{motion.duration-reduced}` |
| Toast | enter `{motion.duration-base}`, exit `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px→0)` | Travel removed; fade at `{motion.duration-reduced}`. Auto-dismiss timing unchanged |
| List enter (rows, cards, badge groups) | `{motion.duration-base}` per item, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px→0)` | Stagger and travel both removed; the group fades in once at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform: translateY(-4px)` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading (inline button spinner, skeleton rows) | `{motion.duration-emphasis}` per rotation, infinite while pending | linear for the spinner, `{motion.ease-standard}` for the skeleton sweep | `transform: rotate()` for the spinner, `opacity` for the skeleton | Rotation and sweep both stop; a static indicator with a text label remains. This is the only infinite animation in the system — Kraken has no brand ambience loop |

### Motion Rules

Only `transform` and `opacity` are ever transitioned. Layout-affecting properties are excluded by rule: `width`, `height`, `top`, `left` and `margin` are never transitioned, because each one forces layout.

- Every exit is shorter than its matching entrance (`{motion.duration-fast}` out against `{motion.duration-base}` in).
- Nothing moves on first paint in a way that delays content. Hero type and the primary CTA render at their final position.
- No infinite animation except the loading indicators named above.
- Travel never exceeds 16px, and only the drawer uses a full-width translate.
- A displayed balance, price or percentage never moves or scales. It may cross-fade its value at `{motion.duration-fast}`; nothing about a number in this system is communicated by movement.

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all translate and all scale, every stagger, the spinner
     rotation and the skeleton sweep. */
  /* Kept: opacity fades, capped at 150ms — {motion.duration-reduced}. */
  /* Kept at zero duration: the focus ring, which must track the keyboard. */
  *, *::before, *::after {
    transition-duration: 150ms !important;
    transition-property: opacity !important;
    animation: none !important;
    scroll-behavior: auto !important;
  }
}
```

What is removed: every `translateY` / `translateX` offset, every scale, the `{motion.stagger-step}` delay on list groups, the loading spinner's rotation and the skeleton sweep. What remains: opacity fades at `{motion.duration-reduced}` (150ms) or less, the focus ring at zero duration, and a static labelled loading indicator in place of the spinner. Nothing becomes unreachable or unreadable when motion is off — no state in this system is communicated by movement alone.

## Accessibility

### Measured Contrast

Computed with WCAG 2.1 relative luminance against the hexes in this file's frontmatter. Nothing here is estimated. Where a value is an `rgba()` fill it is composited over `{colors.canvas}` first, and the composite is named.

| Foreground / Background | Ratio | Required | Result |
|---|---|---|---|
| `{colors.ink}` on `{colors.canvas}` | 18.88:1 | 4.5:1 | pass |
| `{colors.ink}` on `{colors.surface}` | 18.88:1 | 4.5:1 | pass |
| `{colors.on-primary}` on `{colors.primary}` | 6.04:1 | 4.5:1 | pass |
| `{colors.purple-dark}` on `{colors.canvas}` | 6.66:1 | 4.5:1 | pass |
| `{colors.purple-deep}` on `{colors.canvas}` | 8.3:1 | 4.5:1 | pass |
| `{colors.badge-ink}` on `{colors.canvas}` | 8.59:1 | 4.5:1 | pass |
| `{colors.success-text}` on `{colors.canvas}` | 6.61:1 | 4.5:1 | pass |
| `{colors.success-text}` on composited `{colors.success-subtle}` (#d9efe6) | 5.49:1 | 4.5:1 | pass |
| `{colors.primary}` on composited `{colors.purple-subtle}` (#ebe5fe) | 4.94:1 | 4.5:1 | pass |
| `{colors.badge-ink}` on composited `{colors.neutral-subtle}` (#ededf0) | 7.36:1 | 4.5:1 | pass |
| `{colors.ink}` on composited `{colors.gray-subtle}` (#f6f7f8) | 17.6:1 | 4.5:1 | pass |
| `{colors.focus}` on `{colors.canvas}` | 18.88:1 | 3:1 | pass |
| `{colors.focus}` on `{colors.primary}` | 3.13:1 | 3:1 | pass |
| `{colors.focus-inner}` against `{colors.focus}` | 18.88:1 | 3:1 | pass |
| `{colors.purple-dark}` border on `{colors.canvas}` | 6.66:1 | 3:1 | pass |

### Where Kraken's real values fail AA

These are extracted brand facts, left unchanged. The document's job is to be right about Kraken, not to score well.

- **text-secondary (#9497a9) on `{colors.canvas}` measures 2.89:1** against a 4.5:1 minimum, and the same 2.89:1 on `{colors.surface}`. Kraken's real secondary-text tone **fails WCAG 1.4.3 at every size below large text**, and it does not clear 3:1 either, so there is no size at which it becomes compliant. Anyone building on this document should treat it as decorative or replace it.
- **border-subtle (#dedee5) on `{colors.canvas}` measures 1.34:1** against a 3:1 non-text minimum, and 1.34:1 on `{colors.surface}`. Kraken's divider hairline **fails WCAG 1.4.11.** It is scoped to decoration here and is not the only boundary of any control this file documents. The `{colors.neutral-cool}` border at 24% opacity composites to #dbdbe1 — 1.38:1 — and fails the same way.
- **The opacity fills are fills, not ink, and two of them fail as text.** Composited over `{colors.canvas}`, `success-subtle` resolves to #d9efe6 and measures **1.2:1** against the canvas; `purple-subtle` resolves to #ebe5fe at 1.22:1, `neutral-subtle` to #ededf0 at 1.17:1, and `gray-subtle` to #f6f7f8 at 1.07:1. None of them is ever a text colour or a boundary in this file — each is a button or badge **background**, and the ink that sits on it is measured in the table above (4.94:1, 5.49:1, 7.36:1 and 17.6:1 respectively). Setting any of these four as text or as the only border of a control would fail WCAG, by the ratios just given.
- **success (#149e61) on `{colors.canvas}` measures 3.45:1** against a 4.5:1 minimum. It is used as a 16%-opacity badge fill, where 1.4.3 does not apply, and `{colors.success-text}` carries the text. Used directly as text below large size it **fails AA**; at 18.66px/700 or 24px it clears the 3:1 large-text threshold.

### Focus Ring Visibility

This file defines one surface polarity: `{colors.canvas}` and `{colors.surface}` are both #ffffff, so one ring serves the whole document and no `focus-on-dark` is needed. The ring is 2px `{colors.focus}` with a 2px `{colors.focus-inner}` offset, measured above at 18.88:1 on both white surfaces and 3.13:1 on the `{colors.primary}` button fill — the one chromatic surface a ring can land on here. A purple ring was rejected: `{colors.purple-deep}` on `{colors.primary}` measures 1.37:1.

### Type Size

`{typography.micro}` is 7px. WCAG sets no minimum size, but 7px is below any practical reading floor and this file cannot verify what it is used for. Restrict it to ornamental labels whose content is duplicated at `{typography.small}` (12px) or larger.

### Reduced Motion

Honoured as specified in Motion & Animation: all travel and scale removed, opacity fades capped at `{motion.duration-reduced}` (150ms), focus ring at zero duration, loader rotation frozen in favour of a static labelled indicator.

### Not verifiable from this document

Minimum tap-target size cannot be confirmed here. `{component.button-primary}` pads 13px × 16px around `{typography.button}` (16px × 1.38 ≈ 22px line box), which computes to roughly 48px tall — but the control's declared height, hit-area insets and icon-button dimensions were never extracted, and this is a document with no rendered page. Treat 44×44px as the target to verify, not as a verified fact. Overlap, overflow, clipping, frame rate and layout shift are likewise outside what this file can establish.

## Do's and Don'ts

### Do
- Use Kraken Purple (`{colors.primary}` — #7132f5) for CTAs and links
- Apply `{rounded.xl}` (12px) radius on all buttons
- Use Kraken-Brand for headings, Kraken-Product for body
- Keep `{colors.ink}` for body copy; it is the only ink in this palette that clears AA
- Carry badge text in `{colors.success-text}` or `{colors.badge-ink}`, never in the fill colour

### Don't
- Don't use pill buttons — `{rounded.xl}` (12px) is the max radius for buttons
- Don't use other purples outside the defined scale
- Don't set body text in `{colors.text-secondary}` (2.89:1) or `{colors.success}` (3.45:1)
- Don't let `{colors.border-subtle}` be the only boundary of an interactive control — it measures 1.34:1
- Don't animate `width`, `height`, `top`, `left` or `margin`, and never move or scale a displayed balance or price

## Responsive Behavior

Breakpoints: 375px, 425px, 640px, 768px, 1024px, 1280px, 1536px.

Per-breakpoint behaviour — column counts, container widths, type scaling, nav collapse — was never captured for this site. See Known Gaps.

## Agent Prompt Guide

### Quick Color Reference
- Brand: Kraken Purple (`{colors.primary}` — #7132f5)
- Dark variant: `{colors.purple-dark}` (#5741d8)
- Text: Near Black (`{colors.ink}` — #101114)
- Secondary text: `{colors.text-secondary}` (#9497a9) — fails AA at 2.89:1; prefer `{colors.badge-ink}` (#484b5e, 8.59:1) where the text must be read
- Background: White (`{colors.canvas}` — #ffffff)

### Example Component Prompts
- "Create hero: white background. Kraken-Brand 48px weight 700, letter-spacing -1px. Purple CTA (#7132f5, 12px radius, 13px 16px padding)."

## Known Gaps

Everything below is absent from this file's prose. It was not invented during the conversion from the numbered format.

**Colour and state values**
- No hover, pressed, active, disabled, selected or error colour was extracted for any component. The state matrix names the coverage and marks each value as not extracted.
- No disabled tone exists in the palette at all — neither a disabled fill nor a disabled label colour.
- No link-visited, link-hover or link-active tone.
- No dark theme. Canvas and surface are both #ffffff in this document; whether the real site has a dark mode is unknown here.
- No second surface tone. `{colors.surface}` equals `{colors.canvas}`, so the canvas / surface / raised layering SPEC asks to compare cannot be compared: there is one layer plus `{shadow.subtle}`.
- The focus ring (`{colors.focus}`, `{colors.focus-inner}`) is **prescribed, not extracted.**

**Typography**
- `{typography.micro}`: actual letter-spacing unknown — the source table recorded `uppercase` in that column.
- Four roles were extracted as ranges rather than values: `{typography.button}` weight 500–600, `{typography.caption}` weight 400–700 and line height 1.43–1.71, `{typography.small}` weight 400–500. The ranges are preserved; which end applies where is unknown.
- No responsive type scaling, no fluid clamp, no mobile size overrides.

**Layout**
- No container max-width, no grid column count, no gutter value, no section vertical rhythm. The spacing list is an inventory of measured values, not a designed ladder.
- No per-breakpoint behaviour for any of the seven breakpoints.

**Components never documented**
- Navigation (top nav, mobile nav, footer), inputs and form controls, cards, tables and price rows, tabs, tooltips, modals, drawers, dropdowns, toasts, loaders, charts and tickers. The Motion section prescribes timings for several of these interaction *classes*, but no component entry exists for them and none was fabricated.
- No selected and no error component of any kind.

**Motion**
- Every value in Motion & Animation is prescribed from the Calm profile. Nothing was measured from Kraken.

**Not computable from a document**
- Tap-target sizes, overlap, horizontal overflow, clipping, frame rate and layout shift. These need a rendered page.
