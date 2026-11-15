## A32 · linear.app

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

`2 · 5 · 1 · 3 · 1 · 1`  ->  `5 · 5 · 5 · 5 · 5 · 5`

Harness command, run before and after:
`python3 -I theme-audit/audit.py --site linear.app --json`

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A Token contract | `colors.focus` | No focus token at all. The file's prose promised a ring ("focus rings" is named three times in the Overview and Colors sections) and pointed it at `{colors.primary-focus}`, which is not a `focus`-role key and measures **1.01:1 against `{colors.primary}`** — the lavender CTA is the one control a ring most needs to mark, and the shipped ring is invisible on it. At the documented 50% opacity it is weaker still on every dark surface. |
| P0 | A Token contract | `colors.surface` | `surface` role unresolved. The file defines `surface-1`…`surface-4`, none of which matches the role pattern, so no `text on surface` or `border on surface` check ran at all — nine real contrast facts were being skipped, not passed. |
| P0 | A Token contract | `colors.text-dim` | `text-dim` role unresolved. All three secondary tones are named `ink-*`, so the harness judged every one of them as primary body text at 4.5:1 and the file had no declared secondary tone. |
| P0 | B Colour | `hairline`, `hairline-strong`, `hairline-tertiary` | All three boundary tones fail 1.4.11 on both the canvas and the default surface: 1.36 / 1.24, 1.69 / 1.54, 1.96 / 1.79 — the strongest is a third short of 3.0:1. `hairline-strong` was explicitly documented as "input focus rings", a job it cannot do. Undisclosed before this audit. |
| P0 | B Colour | `button-primary-hover` | White label on `#828fff` measures **2.87:1**: the primary CTA passes at rest (4.70:1) and **fails AA the moment it is hovered**. `{typography.button}` is 14px/500, so the large-text exemption does not apply. Not disclosed anywhere in the file. |
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule, zero durations, zero easing curves. The file was mute on motion. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Five real AA/AAA failures were present and none was stated. |
| P1 | B Colour | `ink-tertiary` | 3.62:1 on canvas, 3.30:1 on surface-1, down to 3.02:1 on surface-4 — below AA for body text. The file's own usage note reads "disabled, footnotes": the disabled half is WCAG-exempt, the footnote half is a live failure at 12px. |
| P1 | B Colour | `primary` as link ink | 4.44:1 on canvas — short of 4.5:1 by 0.06 for body-size link text. Not harness-checked (the accent is only measured against `on-accent`), so it would have gone unrecorded. |
| P1 | C Elevation | surface ladder | The four-step ladder is not a contrast ladder: canvas→surface-1 1.10:1, surface-1→2 1.04:1, surface-2→3 1.04:1, surface-3→4 **1.01:1**, canvas→surface-4 only 1.20:1. The file presented four levels as carrying hierarchy "without shadow"; in fact the hairline carries it, and `pricing-card-featured` / `pricing-tab-selected` relied on a 1.04:1 and 1.14:1 fill step as a state signal. |
| P1 | H States | every component | 21 component tokens, three state words documented (`hover`, `pressed`, `selected`). `focus-visible`, `active`, `disabled`, `loading`, `error` appeared nowhere in the Components section. |
| P1 | A Token contract | focus on the inverse band | The file documents a pure-white `inverse-canvas` band with a `button-inverse` on it. A single ring cannot serve both that band and a #010102 canvas, and nothing addressed it. |
| P2 | E Borders / radius | border widths | The radius ladder is clean (4·6·8·12·16·24·pill) with no value off-scale, but border width was never stated as a scale, so "1px" was repeated nine times with no rule governing when a heavier stroke would be allowed. |
| P2 | D Typography | type roles | Clean — all 13 roles carry family, size, weight, line height and letter-spacing, and body at 16px/1.50 in `{colors.ink}` reads at 17.90:1 on surface-1. No finding beyond the `{colors.ink-tertiary}` note above. |
| P2 | C Elevation | expression | Elevation is expressed one consistent way (background step + 1px hairline) and the brand ships no shadow — but no `shadow:` group and no statement that shadow is deliberately absent. |
| P2 | I Identity | — | `semantic-overlay` #000000 is measured by the harness as text on canvas (1.01:1) although it is a scrim fill. A usage note was the only thing missing. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `text-dim: "#d0d6e0"` | Resolves the `text-dim` role with the file's real secondary tone (alias of `{colors.ink-muted}`, identical hex). Clears 4.5:1 on canvas (14.28:1) and all four surfaces. No new colour introduced. |
| frontmatter `colors:` | — -> `surface: "#0f1011"` | Resolves the `surface` role (alias of `{colors.surface-1}`, identical hex), which switched on nine `on surface` contrast checks that had been silently skipped. |
| frontmatter `colors:` | — -> `hairline-control: "#6a6e78"` | Prescribed parallel accessible boundary per SPEC §2, since all three extracted hairlines fail 3:1. 4.09:1 on canvas, 3.73/3.58/3.45/3.41:1 on surfaces 1–4. Chosen inside Linear's own grey ramp, between `ink-tertiary` #62666d and `ink-subtle` #8a8f98, so it reads as the brand. |
| frontmatter `colors:` | — -> `focus: "#dfe3fb"` | Prescribed ring. The brand lavender pulled to near-paper luminance so one ring clears 3:1 on the canvas, all four surfaces **and** the lavender CTA fill (3.70:1) — which `primary-focus` cannot (1.01:1). |
| frontmatter `colors:` | — -> `focus-on-light: "#5e6ad2"` | Second ring for the white `inverse-canvas` band, where `{colors.focus}` sits at 1.27:1. Uses the brand lavender itself: 4.70:1 on white. SPEC §1's light/dark ring pair, inverted for a dark-default file. |
| frontmatter | — -> `motion:` group | The **Crisp** profile block from SPEC §5, verbatim, unmodified. |
| `## Colors` → Surface | — -> `**Surface**` entry | Documents the role alias and tells authors to keep using the ladder tokens. |
| `## Colors` → Surface | — -> `**Hairline Control**` entry | Labels the token prescribed, scopes the three real hairlines to decoration, and states plainly that all three fail 3:1 on every surface. |
| `## Colors` → Text | — -> `**Text Dim**` entry | Documents the alias and points at the size restriction on `ink-subtle` / `ink-tertiary`. |
| `## Colors` | — -> new `### Focus` subsection | Three entries: both prescribed rings, plus `primary-focus` kept as the extracted fact with its 1.01:1 failure stated and the reason the prescribed pair exists. |
| `## Elevation & Depth` table | level 4 `2px {colors.primary-focus}` at 50% opacity -> `2px {colors.focus}` + 2px `{colors.canvas}` offset, plus a new `4-inverse` row using `{colors.focus-on-light}` | The shipped ring is unmeasurable at 50% opacity and fails on the accent. Extracted value is preserved in `## Colors`, not deleted. |
| `## Elevation & Depth` | — -> "The ladder is tonal, not contrast-bearing" paragraph | Records the five measured inter-level ratios (1.01:1 to 1.20:1) and states that the hairline, not the fill step, draws the edge. Also states that elevation is expressed one way only and that there is no `shadow:` group because the file documents no shadow. |
| `## Shapes` | — -> `### Border Widths` | One width (1px), the 2px ring as an `outline` so it costs no layout, no 3px/4px step, and the rule that emphasis comes from tone not width. Closes the only ladder that had no stated scale. |
| `## Components` — every prose entry | state words `hover`, `pressed`, `selected` only -> every entry carries a `States —` line | SPEC §7. Genuinely static or two-state components say so explicitly: `testimonial-card`, `cta-banner` and `status-badge` are default-only; `feature-card`, `product-screenshot-card` and `customer-logo-tile` have two. `error` on `text-input` is marked **unspecified** rather than filled with an invented red. |
| `## Components` → `button-secondary`, `text-input` | 1px `{colors.hairline}` -> 1px `{colors.hairline-control}` | These are the control cases where the border is the only boundary; the decorative hairline cannot carry them. |
| `## Components` → `pricing-tab`, `pricing-card-featured` | — -> note that the fill step alone is not a perceivable state | 1.14:1 and 1.04:1 respectively; selection must also change text tone or add a border/badge. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. Token list, 13-row inventory covering hover, press, focus, page transition, modal/drawer enter+exit, dropdown enter+exit, toast enter+exit, list enter, list exit and loading; rules; and a `@media (prefers-reduced-motion: reduce)` block. |
| after `## Motion & Animation` | — -> `## Accessibility` | Four tables: 13 passing key pairs, 12 disclosed failures with usage notes, focus-ring visibility on all seven surfaces, tap-target spec. Plus reduced-motion and an explicit list of what is not verifiable from a document. |
| `## Do's and Don'ts` | — -> 3 Do's, 4 Don'ts | Motion timing, the two rings, the control boundary; and the prohibitions on hairline-as-control-boundary, single-step state, entrance choreography/ambience, and animating layout properties. |
| `## Known Gaps` | — -> 7 entries | Labels the whole motion section prescribed; labels the three new rings/boundary prescribed; declares the two aliases introduce no new colour; records the 40px-vs-44px tap-target shortfall; records that tap size, overlap, clipping, frame rate and layout shift are not verifiable here; records that surface-3 and surface-4 are 1.01:1 apart and the four-step ladder is effectively two or three steps. |

No extracted hex was altered, renamed or removed. Every change is either a new prescribed token (labelled as such in the file), a role alias with an identical hex, or prose.

### Contrast checks

All computed with the WCAG 2.1 relative-luminance formula, python3 stdlib only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #f7f8f8 / `canvas` #010102 | 19.61:1 | 4.5 | Pass |
| `ink` #f7f8f8 / `surface-1` #0f1011 | 17.90:1 | 4.5 | Pass |
| `ink` #f7f8f8 / `surface-2` #141516 | 17.18:1 | 4.5 | Pass |
| `ink` #f7f8f8 / `surface-3` #18191a | 16.55:1 | 4.5 | Pass |
| `ink` #f7f8f8 / `surface-4` #191a1b | 16.38:1 | 4.5 | Pass |
| `text-dim` = `ink-muted` #d0d6e0 / `canvas` | 14.28:1 | 4.5 | Pass |
| `text-dim` = `ink-muted` #d0d6e0 / `surface-1` | 13.04:1 | 4.5 | Pass |
| `text-dim` = `ink-muted` #d0d6e0 / `surface-4` | 11.93:1 | 4.5 | Pass |
| `ink-subtle` #8a8f98 / `canvas` | 6.42:1 | 4.5 | Pass |
| `ink-subtle` #8a8f98 / `surface-1` | 5.86:1 | 4.5 | Pass |
| `ink-subtle` #8a8f98 / `surface-4` | 5.36:1 | 4.5 | Pass |
| `ink-tertiary` #62666d / `canvas` | 3.62:1 | 4.5 | **Fail** (disclosed) |
| `ink-tertiary` #62666d / `surface-1` | 3.30:1 | 4.5 | **Fail** (disclosed) |
| `ink-tertiary` #62666d / `surface-2` | 3.17:1 | 4.5 | **Fail** (disclosed) |
| `ink-tertiary` #62666d / `surface-3` | 3.05:1 | 4.5 | **Fail** (disclosed) |
| `ink-tertiary` #62666d / `surface-4` | 3.02:1 | 4.5 | **Fail** (disclosed) |
| `on-primary` #ffffff / `primary` #5e6ad2 | 4.70:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary-focus` #5e69d1 | 4.75:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary-hover` #828fff | 2.87:1 | 4.5 | **Fail** (disclosed) |
| `inverse-ink` #000000 / `inverse-canvas` #ffffff | 21.00:1 | 4.5 | Pass |
| `semantic-success` #27a644 / `canvas` | 6.58:1 | 4.5 | Pass |
| `brand-secure` #7a7fad / `canvas` | 5.43:1 | 4.5 | Pass |
| `brand-secure` #7a7fad / `surface-1` | 4.96:1 | 4.5 | Pass |
| `primary` #5e6ad2 as link ink / `canvas` | 4.44:1 | 4.5 | **Fail by 0.06** (disclosed) |
| `semantic-overlay` #000000 / `canvas` | 1.01:1 | 4.5 | **Fail** — scrim fill, not text; disclosed with usage note |
| `hairline` #23252a / `canvas` | 1.36:1 | 3.0 | **Fail** (disclosed) |
| `hairline` #23252a / `surface-1` | 1.24:1 | 3.0 | **Fail** (disclosed) |
| `hairline-strong` #34343a / `canvas` | 1.69:1 | 3.0 | **Fail** (disclosed) |
| `hairline-strong` #34343a / `surface-1` | 1.54:1 | 3.0 | **Fail** (disclosed) |
| `hairline-tertiary` #3e3e44 / `canvas` | 1.96:1 | 3.0 | **Fail** (disclosed) |
| `hairline-tertiary` #3e3e44 / `surface-1` | 1.79:1 | 3.0 | **Fail** (disclosed) |
| `hairline-control` #6a6e78 / `canvas` | 4.09:1 | 3.0 | Pass (prescribed) |
| `hairline-control` #6a6e78 / `surface-1` | 3.73:1 | 3.0 | Pass (prescribed) |
| `hairline-control` #6a6e78 / `surface-2` | 3.58:1 | 3.0 | Pass (prescribed) |
| `hairline-control` #6a6e78 / `surface-3` | 3.45:1 | 3.0 | Pass (prescribed) |
| `hairline-control` #6a6e78 / `surface-4` | 3.41:1 | 3.0 | Pass (prescribed) |
| `focus` #dfe3fb / `canvas` #010102 | 16.41:1 | 3.0 | Pass (prescribed) |
| `focus` #dfe3fb / `surface-1` | 14.98:1 | 3.0 | Pass (prescribed) |
| `focus` #dfe3fb / `surface-2` | 14.38:1 | 3.0 | Pass (prescribed) |
| `focus` #dfe3fb / `surface-3` | 13.85:1 | 3.0 | Pass (prescribed) |
| `focus` #dfe3fb / `surface-4` | 13.71:1 | 3.0 | Pass (prescribed) |
| `focus` #dfe3fb / `primary` #5e6ad2 (CTA fill) | 3.70:1 | 3.0 | Pass (prescribed) |
| `focus` #dfe3fb / `inverse-canvas` #ffffff | 1.27:1 | 3.0 | **Fail** — ring forbidden on the white band; disclosed |
| `focus-on-light` #5e6ad2 / `inverse-canvas` #ffffff | 4.70:1 | 3.0 | Pass (prescribed) |
| `focus-on-light` #5e6ad2 / `inverse-surface-1` #f5f6f6 | 4.34:1 | 3.0 | Pass (prescribed) |
| `focus-on-light` #5e6ad2 / `inverse-surface-2` #f6f7f7 | 4.38:1 | 3.0 | Pass (prescribed) |
| `primary-focus` #5e69d1 / `primary` #5e6ad2 (shipped ring on the CTA) | 1.01:1 | 3.0 | **Fail** (disclosed) |
| `primary-focus` #5e69d1 / `canvas` | 4.39:1 | 3.0 | Pass |
| `primary-focus` #5e69d1 / `surface-1` | 4.01:1 | 3.0 | Pass |

Elevation separation, measured for dimension C:

| Pair | Ratio |
|---|---|
| `canvas` #010102 / `surface-1` #0f1011 | 1.10:1 |
| `surface-1` / `surface-2` | 1.04:1 |
| `surface-2` / `surface-3` | 1.04:1 |
| `surface-3` / `surface-4` | 1.01:1 |
| `canvas` / `surface-2` | 1.14:1 |
| `canvas` / `surface-4` | 1.20:1 |

The layers are **not** reliably distinguishable from one another. Nothing in the file is wrong — these are Linear's own CSS variables — but the document previously claimed the ladder "carries hierarchy without shadow", which the numbers do not support. The hairline border does the work. This is now stated in the file.

### Motion inventory

Prescribed, **Crisp** profile, not measured from linear.app.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity`, discrete `background-color` cross-fade; no `transform` | Unchanged — already opacity/colour only and under 150ms |
| Press / active | 60ms | `{motion.ease-exit}` | `transform: scale(0.99)` | Scale removed; background change remains, instant |
| Focus-visible ring | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | `opacity` on the ring; geometry never animates | Ring appears with no transition |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | `opacity` 0→1 on the incoming view, no travel | Opacity fade at `{motion.duration-reduced}` 100ms |
| Modal / drawer enter | 150ms | `{motion.ease-enter}` | `opacity` + `translateY(6px)→0`; scrim `opacity` 0→0.6 | Travel removed; both fade at 100ms |
| Modal / drawer exit | 100ms | `{motion.ease-exit}` | `opacity` + `transform` reversed | Opacity fade at 100ms |
| Dropdown / sub-nav enter | 100ms | `{motion.ease-enter}` | `opacity` + `scale(0.98)→1` from the trigger edge | Scale removed; opacity only at 100ms |
| Dropdown / sub-nav exit | 60ms | `{motion.ease-exit}` | `opacity` only | Unchanged |
| Toast enter | 150ms | `{motion.ease-enter}` | `opacity` + `translateY(8px)→0` | Travel removed; opacity at 100ms |
| Toast exit | 100ms | `{motion.ease-exit}` | `opacity` + `translateY(0→4px)` | Opacity only at 100ms |
| List enter | 100ms per item, `{motion.stagger-step}` 20ms apart, 6 items max | `{motion.ease-enter}` | `opacity` + `translateY(4px)→0` | Stagger and travel removed; list fades as one block at 100ms |
| List exit | 60ms | `{motion.ease-exit}` | `opacity`; no stagger, no travel | Unchanged |
| Loading | spinner 600ms/rotation infinite (loader exemption); screenshot fade 150ms | linear; `{motion.ease-enter}` | spinner `transform: rotate()`; slot `opacity` 0→1 | Spinner replaced by a static or opacity-pulsing indicator at 100ms; slot fade at 100ms |

Rule compliance: `transform` and `opacity` only; every exit shorter than its entrance (150/100 modal, 100/60 dropdown, 150/100 toast, 100/60 list); nothing animates on first paint; the spinner is the only infinite animation and Linear is declared to have no brand ambience on this canvas; reduced motion clamps to 100ms, under the 150ms ceiling. Harness `layout_animation_mentions` is empty.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 288, `surface_keys` regex `^(canvas\|background\|bg\|base\|surface\|card\|panel)` | A focus ring is never measured against an inverse/alternate band whose key is prefixed rather than suffixed. `inverse-canvas: "#ffffff"` is a real full-bleed surface in this file and `{colors.focus}` sits on it at **1.27:1**, but the harness reports no failure because the key starts with `inverse-`. This is a genuine undetected hole, not a false positive: I found it only by hand. | Add `inverse` and `invert` to the prefix alternation, or match the surface words anywhere in the key (`(^|[-_])(canvas\|surface\|card\|panel\|bg\|base)`). Same hole applies to `dual_theme` detection on line 189, which also anchors at `^`, so a file whose second theme is named `inverse-*` is treated as single-theme. |
| `theme-audit/audit.py` lines 26-28, `text-dim` role patterns | No `ink-*` pattern, although `^ink-` *is* listed under the `text` role on line 25. Any file naming its secondary tones `ink-muted` / `ink-subtle` therefore has them judged at 4.5:1 as primary body text and still scores `text-dim` as missing. Likely affects every `ink-`-naming file in the collection. | Add `r"^ink-(muted\|subtle\|soft\|secondary\|tertiary)$"` to the `text-dim` pattern list, and make the `text` role's `^ink-` pattern narrower so a tone is not counted in both roles. |
| `theme-audit/audit.py` line 364, `disclosed()` | Substring matching on the token name means a disclosure line for `hairline-strong` can satisfy a `hairline` failure whenever the two ratios happen to fall within 0.06 of each other. It did not bite here (1.36/1.24 vs 1.69/1.54), but it is a latent false pass for any file with a prefix-nested token family. | Require a word-boundary match on the token name: `re.search(rf"(?<![\w-]){re.escape(fg_name)}(?![\w-])", line)`. |
| `theme-audit/audit.py` lines 257-272, `SEMANTIC` | `semantic-overlay`, a modal scrim fill, is measured as text on the canvas and produces a mandatory 1.01:1 "failure" that can only ever be answered with prose. Scrims, dividers and fills are structurally not text. | Exempt keys matching `(overlay\|scrim\|veil\|backdrop)` as the `disabled` exemption already does, or move them to a separate advisory list that does not feed `contrast_unresolved`. |
| `theme-audit/SPEC.md` §1 | The light/dark focus-ring convention is written one-way-round only: "defines `focus` **and** `focus-on-dark`". For a dark-default file like this one the sensible pair is `focus` + `focus-on-light`, which is also the naming the harness's own `theme_of()` already understands. | Reword as "defines `focus` for its default polarity and `focus-on-light` / `focus-on-dark` for the other", so dark-default files are not pushed toward a misleading name. |

### Needs approval

1. **`button-primary-hover`: white label on `#828fff` at 2.87:1.** Both hexes are extracted. Nearest passing value for the hover background, keeping white text at 4.5:1, is roughly **#646ec4 (4.60:1)** — barely a step lighter than the resting `#5e6ad2`, which guts the point of a lighten-on-hover state. The alternative is to swap the label to `{colors.inverse-ink}` #000000, which measures 7.32:1 on `#828fff` but is not what Linear ships. Usage note that would make the real value defensible: the pair satisfies 1.4.3 only at 18.66px+/700 or 24px+, and `{typography.button}` is 14px/500 — so there is no size at which the shipped combination is defensible for a button label. Disclosed in the file; flagged here because fixing it requires changing an extracted hex.
2. **`primary` #5e6ad2 as link ink on the canvas: 4.44:1, short by 0.06.** Nearest passing value is **#5f6bd4 (4.51:1)**. Not applied — this is the brand's identity colour. Usage note in the file: `{colors.ink}` with a lavender underline for inline links at `{typography.body}` and below; lavender ink reserved for 24px+ emphasis, where 3:1 applies and it passes comfortably.
3. **`ink-tertiary` #62666d below AA on every surface (3.62:1 down to 3.02:1).** Nearest value passing 4.5:1 on all four surfaces and the canvas is about **#7c828a** (5.38:1 on canvas, 4.91:1 on surface-1, 4.50:1 on surface-4). Not applied. Usage note in the file: 18.66px+/700 or 24px+ only, or genuinely disabled text. The file's own "footnotes" usage is a real AA failure and is now stated as one.
4. **The three hairlines (1.24:1 – 1.96:1 against 3.0:1).** Nearest passing value against the worst case (`surface-4`) is about **#6a6e78**, which is exactly the prescribed `{colors.hairline-control}` I added *alongside* them. The extracted tones are untouched and rescoped to decoration. Approval needed only if the repo would rather replace the extracted hairlines than carry a parallel token.
5. **`primary-focus` #5e69d1 as the ring on the lavender CTA: 1.01:1.** No nearby value fixes this — any ring close enough to the brand lavender to read as lavender is invisible on a lavender fill. Resolved by prescribing `{colors.focus}` #dfe3fb rather than by moving the extracted hex.
6. **Prescribed tokens awaiting sign-off**, all labelled prescribed in the file and in Known Gaps: `focus` #dfe3fb, `focus-on-light` #5e6ad2, `hairline-control` #6a6e78.
7. **`{colors.surface}` and `{colors.text-dim}` are duplicate-hex role aliases.** They add two keys with no new colour. If the repo prefers renaming `surface-1` → `surface` and `ink-muted` → `text-dim` across prose instead, that is a larger diff in this file and a convention decision for all 84, so I took the additive route.
8. **"CTAs hold ≥40px tap height"** in Responsive Behavior is 4px under WCAG 2.5.5. Left as written because it reflects the pages; recorded in Known Gaps. Changing it to 44px would be a prescription dressed as an extraction.

### Identity verdict

Still unmistakably Linear, and in a couple of places more so than before.

The things that make this file Linear are untouched: #010102 as the deepest canvas in the collection, a single chromatic accent used scarcely, the four-step charcoal ladder, display tracking at -3.0px, product screenshots as the protagonist, and the flat refusal of gradients, spotlight cards and a second accent. No extracted hex moved. The two role aliases carry the brand's own values. The three prescribed tokens were deliberately chosen *inside* Linear's existing ramps — `hairline-control` #6a6e78 sits between the brand's own #62666d and #8a8f98, and `focus` #dfe3fb is the brand lavender at paper luminance rather than a generic blue or white ring — so nothing reads as borrowed from another file.

**The Crisp profile is correct** and I did not consider switching. Assignment rule 2 applies directly: Linear is a developer tool — an issue tracker whose marketing is screenshots of keyboard-driven product chrome. The file's own voice supports it independently: "dense, technical", "the chrome is intentionally minimal", no gradients, no atmospheric colour, no spotlight cards. Crisp's signature — state change reads as instant, no entrance choreography — is the only profile that does not fight the document. Cinematic would have been actively wrong: there is no full-bleed photography and no slow reveal to justify 400–600ms. Playful is excluded by a single-accent palette with saturated colour appearing only on one CTA. Calm's 250ms base would make an issue-tracker brand feel laggy.

The one real identity risk I introduced is bulk: the new Motion & Animation and Accessibility sections are long, and the per-component `States —` lines add a line to each documented component block. I kept them brand-specific rather than generic — the reduced-motion block names the logo marquee, the motion rules state that Linear has *no* ambience, the state notes repeatedly point back to the 1.04:1 ladder problem that is particular to a near-black system, and the tap-target note cites this file's own 40px figure. None of it would transplant unchanged to another file in the collection.

The honest shift in the document's character is that it now admits the near-black canvas has a cost. Twelve disclosed failures, three of them affecting every boundary the brand draws, is the truthful reading of #010102 with #23252a hairlines. That makes the file less flattering and more useful, which is what SPEC §2 asks for.
