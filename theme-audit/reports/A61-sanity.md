## A61 · sanity

Scores before -> after (1-5), from the harness: tokens 1 -> 5 · refs 1 -> 5 · contrast 1 -> 5 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 5

The before-scores for **refs** and **contrast** are not real passes and were not real
failures either: the file had no frontmatter, so the harness floors both at 1 because
nothing was measurable. After conversion, 34 colour tokens, 18 typography entries, 12
spacing steps, 5 radii, 5 shadow values, the Crisp motion block and 16 components are
measurable, and the contrast 5 is earned by **disclosure** of 9 real failures, not by their
absence.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | J / A | whole file | No frontmatter token block at all. Every hex, type value, spacing step and radius lived only in prose, so none of the eight required colour roles resolved and no `{group.token}` reference existed to check. |
| P0 | J / section contract | all headings | Numbered legacy headings (`## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide`). All 12 required sections reported missing purely on naming. |
| P0 | F | motion | No motion group, no Motion & Animation section, no reduced-motion rule, no duration or easing anywhere in the file. |
| P0 | A / G | focus ring | The file names a ring (`#0052ef`, "Focus Ring Blue") but it measures 3.24:1 on the canvas, **2.65:1 on `#212121`** and **2.02:1 on `#353535`** — it fails 1.4.11 on the two surfaces inputs and cards actually sit on, and 2.06:1 on the inverted white band. One ring cannot serve both polarities of this file. |
| P0 | B | `button-primary` | White on Sanity Red `#f36458` is **3.10:1** — the single most-clicked element in the system fails AA at 16px/400. Unmeasured and unmentioned before this audit. |
| P0 | C / E | borders | All four extracted borders fail 1.4.11 badly: `#0b0b0b` 1.00:1 on canvas, `#212121` 1.22:1 on canvas and **1.00:1 on its own `#212121` card**, `#353535` 1.60:1 on canvas. `#212121` is the *only* boundary of `text-input`, `search-input`, `button-ghost` and the nav rule. |
| P0 | G | accessibility | No Accessibility section and no contrast ratio anywhere in the file, despite a Don't that instructs the reader to "check the gray-on-gray contrast ratio". |
| P1 | H | all components | Only `hover` and `focus` appeared anywhere. `focus-visible`, `active/pressed`, `disabled`, `loading`, `selected`, `error` were absent for every one of the 16 components. |
| P1 | B | `error` `#dd0000` | 3.82:1 on the canvas, 3.12:1 on `#212121` — validation text in the brand's error red fails AA, with no usage note. |
| P1 | B | `ink-tertiary` `#797979` | 4.52:1 on the canvas but **3.70:1 on `#212121`** and 2.82:1 on `#353535`. The file assigns it to metadata and placeholders, which appear inside cards. |
| P1 | B | `accent-blue` `#0052ef` | Documented as the universal hover colour for links and text, but 3.24:1 on the canvas and 2.02:1 on `#353535`. It is usable only as a fill behind white (6.08:1). |
| P1 | B | fills vs white | White on `#19d600` is 1.97:1 and on `#55beff` 2.06:1. The file gives no ink guidance for its own vivid fills. |
| P1 | C | elevation | Depth is declared colorimetric, yet the Shadow System table mixes a ring shadow, a focus shadow and a backdrop blur with border-based containment, and the ladder's real steps (1.22:1, 1.31:1, 1.60:1) were never stated — so "elevation change" was being offered as a state signal that is barely perceivable. |
| P1 | A | shadow tokens | Prose states `0 0 0 2px var(--color-blue-500)` while naming only `--color-blue-700` `#0052ef`. The extracted focus shadow is unmeasurable; the overlay states neither blur radius nor alpha. |
| P1 | D / J | typography, spacing, radius | Several source values are ranges, not values: caption weight 400-500 and line height 1.30-1.50, micro label 500-600 and 1.00-1.50, code micro 10-12px, `space-12` 96-120px, `radius-sm` 4-5px. A token must carry one value. |
| P2 | D | max width | "~1440px (inferred from breakpoints)" — an inference in the source, kept as one. |
| P2 | A | p3 colours | `display-p3` magenta and the orange accent border have no sRGB fallback stated, so neither is measurable and neither can carry a hex token. |
| P2 | H | `card-dark` hover | Extracted as "subtle border color shift or elevation change" — neither the property nor the target value is stated. |
| P2 | G | tap target | The file states a 44px minimum, but `button-primary` at 16px/1.50 plus 8px padding computes to ~40px, and `button-ghost` / `search-input` are documented with 0px vertical padding. |
| P2 | section contract | Iteration Guide | The legacy `### Iteration Guide` lives inside `## 9. Agent Prompt Guide`. It is kept verbatim there rather than promoted, so the optional section stays undetected — which costs nothing per SPEC section 3. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Top of file | no frontmatter -> full YAML block: `colors` (34 keys), `typography` (18), `spacing` (12), `rounded` (5), `shadow` (5), `motion` (10), `components` (16) | SPEC section 1. Every value was lifted from this file's own prose; nothing invented. |
| All section headings | `## 1. Visual Theme & Atmosphere` … `## 8. Responsive Behavior` -> `## Overview`, `## Colors`, `## Typography`, `## Layout`, `## Elevation & Depth`, `## Shapes`, `## Components`, `## Motion & Animation`, `## Accessibility`, `## Do's and Don'ts`, `## Responsive Behavior`, `## Known Gaps` | SPEC section 3 order and naming. Prose moved verbatim; `### Border Radius Scale` moved out of Layout into the new Shapes section unchanged. |
| `## 9. Agent Prompt Guide` | numbered, in place -> `## Agent Prompt Guide`, verbatim, after Known Gaps | SPEC section 3: a legacy section with no slot is kept, not folded or deleted. Its `### Iteration Guide` child is untouched. |
| `## Colors` | hex bullets only -> same bullets plus `### Focus` and `### Token Map` | Gives every extracted hex an addressable token and states which tones are prescribed. |
| `colors.focus` | none -> `#55beff` (prescribed; the palette's own Light Blue) | No ring existed that works on dark. 9.56:1 on canvas, 7.82:1 on `#212121`, 5.96:1 on `#353535`, 10.20:1 on `#000000`, 8.05:1 on `#072227`. No new brand colour. |
| `colors.focus-on-light` | none -> `#0052ef` (extracted) | The shipped ring, kept and scoped to the inverted bands: 6.08:1 on `#ffffff`, 5.19:1 on `#ededed`. Two rings because the file documents both polarities. |
| `colors.border-control` | none -> `#797979` (prescribed; the palette's own Medium Gray) | Parallel accessible boundary per SPEC section 2. The four extracted borders keep their `components:` bindings exactly as extracted and are scoped to decoration in prose. |
| `## Components` | styling only -> styling verbatim plus `### State Coverage` table | Eight states per component, extracted and prescribed labelled separately. |
| `## Motion & Animation` | absent -> new section after Components: prescription disclaimer as its first line, Crisp token block verbatim, 14-row inventory, rules, `@media (prefers-reduced-motion: reduce)` block | SPEC sections 4-6. `transform` and `opacity` only; every exit shorter than its entrance. |
| `## Accessibility` | absent -> new section: 17 passing pairs, 13 disclosed failures, ring coverage per surface, tap target, reduced motion | SPEC section 2 disclosure and dimension G. |
| `## Do's and Don'ts` | 8 + 8 bullets -> 12 + 13 | Added focus, control-boundary, ink-on-fill and motion rules; existing bullets untouched. |
| `## Known Gaps` | absent -> new section, 13 entries | Everything the conversion could not recover, plus every prescribed value. |

### Contrast checks

All computed with WCAG 2.1 relative luminance, python3 standard library only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #ffffff / `canvas` #0b0b0b | 19.68 | 4.5 | Pass |
| `ink` #ffffff / `surface` #212121 | 16.10 | 4.5 | Pass |
| `ink` #ffffff / `surface-raised` #353535 | 12.27 | 4.5 | Pass |
| `ink` #ffffff / `input-focus-bg` #072227 | 16.57 | 4.5 | Pass |
| `ink-muted` #b9b9b9 / `canvas` #0b0b0b | 10.03 | 4.5 | Pass |
| `ink-muted` #b9b9b9 / `surface` #212121 | 8.21 | 4.5 | Pass |
| `ink-muted` #b9b9b9 / `surface-raised` #353535 | 6.25 | 4.5 | Pass |
| `ink-tertiary` #797979 / `canvas` #0b0b0b | 4.52 | 4.5 | Pass by 0.02 |
| `ink-tertiary` #797979 / `surface` #212121 | 3.70 | 4.5 | **Fail** (disclosed) |
| `ink-tertiary` #797979 / `surface-raised` #353535 | 2.82 | 4.5 | **Fail** (disclosed) |
| `ink-on-light-deep` #0b0b0b / `surface-inverse` #ffffff | 19.68 | 4.5 | Pass |
| `ink-on-light-deep` #0b0b0b / `surface-inverse-soft` #ededed | 16.81 | 4.5 | Pass |
| `ink-on-light` #212121 / `surface-inverse` #ffffff | 16.10 | 4.5 | Pass |
| `ink-on-light` #212121 / `surface-inverse-soft` #ededed | 13.75 | 4.5 | Pass |
| `on-primary` #ffffff / `primary` #f36458 | 3.10 | 4.5 | **Fail** (disclosed; `button-primary` as shipped) |
| `ink-on-light-deep` #0b0b0b / `primary` #f36458 | 6.35 | 4.5 | Pass — the fix that changes no brand hex |
| `ink` #ffffff / `accent-blue` #0052ef (hover fill) | 6.08 | 4.5 | Pass |
| `accent-blue` #0052ef / `canvas` #0b0b0b (as ink) | 3.24 | 4.5 | **Fail** (disclosed) |
| `accent-blue` #0052ef / `surface` #212121 (as ink) | 2.65 | 4.5 | **Fail** (disclosed) |
| `accent-blue` #0052ef / `surface-raised` #353535 (as ink) | 2.02 | 4.5 | **Fail** (disclosed) |
| `primary` #f36458 / `canvas` #0b0b0b (as ink) | 6.35 | 4.5 | Pass |
| `accent-green` #19d600 / `canvas` #0b0b0b | 9.99 | 4.5 | Pass |
| `success-gpc` #37cd84 / `canvas` #0b0b0b | 9.59 | 4.5 | Pass |
| `error` #dd0000 / `canvas` #0b0b0b | 3.82 | 4.5 | **Fail** (disclosed) |
| `error` #dd0000 / `surface` #212121 | 3.12 | 4.5 | **Fail** (disclosed) |
| `ink` #ffffff / `accent-green` #19d600 | 1.97 | 4.5 | **Fail** (disclosed; use dark ink, 9.99) |
| `ink` #ffffff / `accent-blue-light` #55beff | 2.06 | 4.5 | **Fail** (disclosed; use dark ink, 9.56) |
| `border-dark` #0b0b0b / `canvas` #0b0b0b | 1.00 | 3.0 | **Fail** (disclosed) |
| `border-dark` #0b0b0b / `surface` #212121 | 1.22 | 3.0 | **Fail** (disclosed) |
| `border-subtle` #212121 / `canvas` #0b0b0b | 1.22 | 3.0 | **Fail** (disclosed) |
| `border-subtle` #212121 / `surface` #212121 | 1.00 | 3.0 | **Fail** (disclosed) |
| `border-strong` #353535 / `canvas` #0b0b0b | 1.60 | 3.0 | **Fail** (disclosed) |
| `border-strong` #353535 / `surface` #212121 | 1.31 | 3.0 | **Fail** (disclosed) |
| `border-inverse` #ffffff / `canvas` #0b0b0b | 19.68 | 3.0 | Pass |
| `border-control` #797979 / `canvas` #0b0b0b | 4.52 | 3.0 | Pass (prescribed) |
| `border-control` #797979 / `surface` #212121 | 3.70 | 3.0 | Pass (prescribed) |
| `border-control` #797979 / `surface-raised` #353535 | 2.82 | 3.0 | **Fail** — raised controls take `ink-muted` #b9b9b9 (6.25) |
| `focus` #55beff / `canvas` #0b0b0b | 9.56 | 3.0 | Pass |
| `focus` #55beff / `canvas-void` #000000 | 10.20 | 3.0 | Pass |
| `focus` #55beff / `surface` #212121 | 7.82 | 3.0 | Pass |
| `focus` #55beff / `surface-raised` #353535 | 5.96 | 3.0 | Pass |
| `focus` #55beff / `input-focus-bg` #072227 | 8.05 | 3.0 | Pass |
| `focus` #55beff / `surface-inverse` #ffffff | 2.06 | 3.0 | **Fail** — never used there |
| `focus` #55beff / `surface-inverse-soft` #ededed | 1.76 | 3.0 | **Fail** — never used there |
| `focus` #55beff / `primary` #f36458 (the pill fill) | 1.50 | 3.0 | **Fail** — the ring is drawn outside the pill with a 2px offset, so it is judged on the ground behind |
| `focus-on-light` #0052ef / `surface-inverse` #ffffff | 6.08 | 3.0 | Pass |
| `focus-on-light` #0052ef / `surface-inverse-soft` #ededed | 5.19 | 3.0 | Pass |
| `focus-on-light` #0052ef / `canvas` #0b0b0b | 3.24 | 3.0 | Pass — but 2.65 on `surface`, 2.02 on `surface-raised` |
| `canvas` #0b0b0b / `surface` #212121 (ladder step) | 1.22 | — | Weak; never the sole state signal |
| `surface` #212121 / `surface-raised` #353535 (ladder step) | 1.31 | — | Weak; never the sole state signal |
| `canvas` #0b0b0b / `surface-raised` #353535 (ladder step) | 1.60 | — | Weak |

Harness after: 9 disclosed contrast failures, 0 undisclosed, 0 dangling references.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` + discrete fill change to `#0052ef` | Unchanged |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `transform: scale(0.99)` | Scale removed; colour change remains |
| Focus-visible | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | `opacity` on the ring only | No transition |
| Page / route | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | `opacity` 0 -> 1 | Fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` + `translateY(6px -> 0)` | Travel removed |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity` + `transform` reversed | Fade only |
| Dropdown enter | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | `opacity` + `scale(0.98 -> 1)` | Scale removed |
| Dropdown exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` | Unchanged |
| Toast enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` + `translateY(8px -> 0)` | Travel removed |
| Toast exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity` + `translateY(0 -> 4px)` | Fade only |
| List enter | 100ms per item, 20ms stagger, 6 items max | `{motion.ease-enter}` | `opacity` + `translateY(4px -> 0)` | Stagger and travel removed |
| List exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` | Unchanged |
| Loading | spinner 600ms/rotation infinite; media fade `{motion.duration-base}` | linear; `{motion.ease-enter}` | `transform: rotate()`; `opacity` | Spinner replaced by static or pulsing indicator |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py:449` | SPEC section 2 requires `on-accent` on `accent` at 4.5:1, but no `check()` call measures that pair. This file's `on-primary` #ffffff on `primary` #f36458 at **3.10:1** is invisible to the harness; it surfaced only through the `components:` binding of `button-primary`. A file that documents the pair as tokens but binds no component would hide the failure entirely. | Add `check("on-accent", "accent", 4.5, "label on accent")` beside the other `check()` calls, and a `check_all("on-accent", "accent", 4.5, ...)` for files with several accent inks. |
| `theme-audit/audit.py:649-651` | The `NOT_DOCUMENTED` filter drops an entire structured line containing `n/a`. A state table that writes `n/a` to mean "this state genuinely does not exist" — exactly what SPEC section 7 asks a two-state component to say — loses every state named in that row. I had to reword 30 cells to the word "none" to keep honest rows countable. | Treat the marker as a whole-cell value: split table rows on `|` and drop only cells that are entirely `n/a` / `unknown` / `not documented`, rather than discarding the line. |
| `theme-audit/audit.py` (sections) | `Iteration Guide` is matched only as `## Iteration Guide`. In the ten legacy files it is a `###` child of `## 9. Agent Prompt Guide`, which SPEC section 3 says to keep verbatim — so a correct conversion still reports the optional section missing. No score effect, but the reported "optional_sections_missing" is misleading. | Either match the heading at any depth, or note in SPEC that legacy files keep it nested. |

### Needs approval

Each item below changes an extracted fact or a shipped binding, so none was applied.

1. **`button-primary` label.** `#ffffff` on `#f36458` is 3.10:1. Two routes, both needing a brand-owner decision: (a) re-bind the label to `{colors.ink-on-light-deep}` `#0b0b0b`, which measures **6.35:1** and changes no brand hex; or (b) keep the white label and darken the coral to **`#e62111`** (4.57:1 with white), which does change an identity colour. Usage note that makes the real pair defensible: white on `#f36458` clears only the 3:1 large-text floor, so it is acceptable at 24px+ — and this system forbids the 700 weight that would allow 18.66px.
2. **Re-binding the input and ghost-button boundary.** `text-input`, `search-input`, `button-ghost` and the nav rule are extracted as 1px `#212121`, measured at 1.22:1 on the canvas. The bindings are left exactly as extracted. Approval requested to re-point control boundaries to `{colors.border-control}` `#797979` (4.52:1 on canvas, 3.70:1 on surface) in the `components:` block.
3. **`error` `#dd0000` as validation text.** 3.82:1 on the canvas, 3.12:1 on `#212121`. Nearest passing value for body-size text on the canvas: **`#f40000`** (4.54:1). Usage note for the real value: acceptable as a 1px boundary or icon fill on the canvas only, always paired with an `{colors.ink}` message.
4. **`accent-blue` `#0052ef` as link ink on dark.** 3.24:1 on canvas, 2.65:1 on `#212121`, 2.02:1 on `#353535`. Nearest passing value: **`#2670ff`** (4.54:1 on the canvas). Usage note for the real value: fill-only — white on the blue fill is 6.08:1, which is how Sanity uses it; hovered *link text* on dark needs the lighter blue or an underline plus `{colors.ink}`.
5. **`ink-tertiary` `#797979` inside cards.** 3.70:1 on `#212121`, 2.82:1 on `#353535`. Nearest passing values: **`#888888`** (4.54:1 on `#212121`) and **`#9d9d9d`** (4.52:1 on `#353535`). Usage note for the real value: canvas-only, or 24px+ where 3:1 applies — but it fails even that on `#353535`.
6. **`shadow.ring-focus-extracted`.** The source states `0 0 0 2px var(--color-blue-500)` and never gives `--color-blue-500` a hex. The token is recorded unmeasurable; approval requested either to supply the hex or to retire the shadow in favour of `{shadow.ring-focus}`.

### Identity verdict

Still unmistakably Sanity. The identity markers all survive the conversion: the near-black
`#0b0b0b` canvas described as the natural state rather than a dark mode, the pure achromatic
ramp with no warm or cool bias, waldenburgNormal at 112px with -4.48px tracking, IBM Plex
Mono as the uppercase technical counterweight, the coral-red pill as the only warm element,
the universal hover shift to electric blue, the radius ladder that jumps from 12px straight
to 99999px, and colorimetric rather than shadowed depth. The four added tokens are two
focus rings and one control boundary drawn from hexes the palette already owned, plus the
inverted-section names; no new hue enters the system and no alias exists to satisfy a regex.

**Crisp is the right profile** and is confirmed, not merely accepted. SPEC section 5 rule 2
fires on evidence in the file's own words: a developer-content platform for "people who live
in terminals", a monospace register for system metadata, a "precision-engineered" type voice,
and depth that is flat by policy. The one argument for Cinematic — full-bleed feature cards
with large imagery — is outweighed by the absence of any luxury, automotive, hardware or
gaming identity, and by a system whose stated signature is an instantaneous blue activation
on every interactive element. A 400ms hover would read as a different brand.
