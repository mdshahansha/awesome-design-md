## A17 · cursor

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

All eight harness-reported defects were reproduced independently before any edit: `focus` was absent from `colors:`, the three hairline/canvas pairs and the four muted/canvas-and-card pairs measured exactly the ratios stated in the brief, both new sections were missing, and only `active` appeared in a structured Components line. The harness additionally flagged two component-level failures the brief did not list: `button-primary` (white on Cursor Orange, 3.52:1) and `timeline-pill-done` (white on gold, 3.16:1).

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no Motion & Animation section, no reduced-motion rule. Nothing to build timing from. |
| P0 | G Accessibility | whole file | No Accessibility section. Nine real contrast failures, including the brand's signature CTA, were undisclosed. |
| P0 | A Tokens | `colors.focus` | No focus ring token or geometry anywhere in the file. Keyboard operation was undocumented. |
| P0 | B Colour | `button-primary` | White `{colors.on-primary}` on `{colors.primary}` #f54e00 = 3.52:1 against 4.5:1. The brand's primary CTA fails AA for its own 14px/500 label, and the file's own rule against bold weights closes the AA-Large escape. Extracted value, not corrected. |
| P0 | B Colour | `timeline-pill-done` | White on `{colors.timeline-done}` #c08532 = 3.16:1 against 4.5:1, at 11px. No large-text exemption applies. `{colors.ink}` on the same gold is 4.86:1. |
| P1 | B Colour | `{colors.muted}` | 3.84:1 on canvas / 4.12:1 on card, documented as "Sub-titles" with no size floor — i.e. as body-size secondary text, which fails AA. |
| P1 | E Borders | all three hairlines | Strongest hairline is 1.48:1 on canvas. `text-input` and `button-secondary` had a hairline as their only boundary, so the sole indicator of a control sat at 1.18–1.48:1. |
| P1 | H States | every component | 25 component entries, one documented state (`button-primary-active`). Hover, focus-visible, disabled, loading, selected and error were named nowhere. |
| P1 | C Elevation | `surface-card` on `canvas` | White-on-cream is 1.07:1. The file said cards "float above the canvas via 1px hairlines and the slight white-on-cream contrast" — the surface shift is not perceptible on its own, so the hairline is load-bearing, not optional. Elevation is otherwise consistently expressed (hairline, never shadow), so no `shadow:` group is warranted. |
| P2 | D Typography | all roles | Complete — every one of the 14 roles carries family, size, weight, line height and letter spacing. Body at 16px/1.5 in `{colors.ink}` reads at 14.33:1 on canvas. No defect. |
| P2 | E Radius | `rounded` ladder | `none`/`xs`/`sm`/`md`/`lg`/`xl` plus `pill` and `full` sharing 9999px. The duplicate is a harmless semantic alias and `xl` is marked rare; no value sits outside its scale. No change made. |
| P2 | G Accessibility | `{colors.semantic-success}` | #1f8a65 is 4.01:1 on canvas — fails AA for body text. Not harness-flagged (not a required role pair); disclosed anyway. |
| P2 | Responsive | Touch Targets | Claimed 40px is "at WCAG AA, padded for AAA". Misstates the threshold; 44 × 44px is the floor. Corrected to a padding requirement. |
| P2 | Iteration Guide | item 5 | "Hover state never documented" became stale once states were prescribed. Rewritten to point at the new table and keep the prescribed label. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| `colors:` frontmatter | — -> `focus: "#26251e"`, `focus-on-dark: "#f7f7f4"` | Missing required role. Ink ring clears 3:1 on every light surface the file defines, the orange CTA included; cream ring serves the two ink-surfaced components. |
| `colors:` frontmatter | — -> `hairline-control: "#8f8c82"` | Parallel accessible boundary (3.13:1 on canvas) for controls whose hairline is their only edge. The three real hairlines stay frozen and are scoped to decoration in the prose. |
| `colors:` frontmatter | — -> `muted-accessible: "#6e6b62"` | Parallel accessible secondary tone (4.96:1 canvas / 5.33:1 card). Real `{colors.muted}` stays, scoped to 18.66px+. |
| frontmatter after `spacing:` | — -> `motion:` group | SPEC section 4 Crisp block, used verbatim. |
| Colors § Hairlines | — -> `hairline-control` entry | States the 1.48:1 measurement, labels the new token prescribed, splits decoration from control boundary. |
| Colors § Text | — -> `muted-accessible` entry | States 3.84:1 / 4.12:1 plainly and gives the size floor that makes the real tone defensible. |
| Colors | — -> new `### Focus` subsection | Documents both rings with measured ratios and the reason the ring is ink rather than orange (orange ring on orange CTA = 1.34:1). |
| Shapes | — -> `### Focus Ring` | 2px ring, 2px offset, inherits the control's own radius so no new value enters the radius ladder. |
| Components | — -> `### States` table, 26 rows | Every component entry now names its states; genuinely single-state components say so. Prescribed status stated in the lead-in. |
| after Components | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. 14-row interaction table, rules, reduced-motion block. |
| after Motion | — -> `## Accessibility` | Measured passes, measured failures with ratios, per-surface focus ratios, tap-target floor, reduced-motion pointer. |
| Responsive § Touch Targets | "40px — at WCAG AA, padded for AAA" -> 44px floor, 4px touch padding required | The old claim was wrong about the threshold. |
| Iteration Guide item 5 | "Hover state never documented." -> points to the States table, keeps the prescribed label | Stale after the states work. |
| Known Gaps | 1 animation line -> 4 lines | Records that motion, both focus tokens and the two accessible parallels are prescribed, and that tap targets are unverifiable here. |

Not changed, deliberately: no brand hex was altered, `timeline-pill-done`'s white label was left as documented, and no section not listed above was reflowed.

### Contrast checks

All computed with WCAG 2.1 relative luminance in a stdlib-only python3 snippet; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #26251e / `canvas` #f7f7f4 | 14.33:1 | 4.5 | Pass |
| `ink` #26251e / `surface-card` #ffffff | 15.38:1 | 4.5 | Pass |
| `body` #5a5852 / `canvas` #f7f7f4 | 6.63:1 | 4.5 | Pass |
| `body` #5a5852 / `canvas-soft` #fafaf7 | 6.80:1 | 4.5 | Pass |
| `muted-accessible` #6e6b62 / `canvas` | 4.96:1 | 4.5 | Pass |
| `muted-accessible` #6e6b62 / `surface-card` | 5.33:1 | 4.5 | Pass |
| `canvas` #f7f7f4 / `ink` #26251e | 14.33:1 | 4.5 | Pass |
| `ink` / `timeline-thinking` #dfa88f | 7.42:1 | 4.5 | Pass |
| `ink` / `timeline-grep` #9fc9a2 | 8.31:1 | 4.5 | Pass |
| `ink` / `timeline-read` #9fbbe0 | 7.80:1 | 4.5 | Pass |
| `ink` / `timeline-edit` #c0a8dd | 7.24:1 | 4.5 | Pass |
| `ink` / `timeline-done` #c08532 | 4.86:1 | 4.5 | Pass |
| `semantic-error` #cf2d56 / `canvas` | 4.70:1 | 4.5 | Pass |
| `focus` #26251e / `canvas` | 14.33:1 | 3.0 | Pass |
| `focus` #26251e / `canvas-soft` | 14.70:1 | 3.0 | Pass |
| `focus` #26251e / `surface-card` | 15.38:1 | 3.0 | Pass |
| `focus` #26251e / `surface-strong` #e6e5e0 | 12.19:1 | 3.0 | Pass |
| `focus` #26251e / `primary` #f54e00 | 4.37:1 | 3.0 | Pass |
| `focus-on-dark` #f7f7f4 / `ink` #26251e | 14.33:1 | 3.0 | Pass |
| `hairline-control` #8f8c82 / `canvas` | 3.13:1 | 3.0 | Pass |
| `on-primary` #ffffff / `primary` #f54e00 (`button-primary`) | 3.52:1 | 4.5 | **Fail** — frozen brand value, disclosed |
| `on-primary` #ffffff / `timeline-done` #c08532 | 3.16:1 | 4.5 | **Fail** — disclosed |
| `semantic-success` #1f8a65 / `canvas` | 4.01:1 | 4.5 | **Fail** — disclosed, 18.66px+ only |
| `muted` #807d72 / `canvas` | 3.84:1 | 4.5 | **Fail** — frozen, disclosed |
| `muted` #807d72 / `surface-card` | 4.12:1 | 4.5 | **Fail** — frozen, disclosed |
| `muted-soft` #a09c92 / `canvas` | 2.55:1 | 4.5 | **Fail** — disabled-text tone, disclosed |
| `muted-soft` #a09c92 / `surface-card` | 2.74:1 | 4.5 | **Fail** — disabled-text tone, disclosed |
| `hairline-strong` #cfcdc4 / `canvas` | 1.48:1 | 3.0 | **Fail** — frozen, scoped to decoration |
| `hairline` #e6e5e0 / `canvas` | 1.18:1 | 3.0 | **Fail** — frozen, scoped to decoration |
| `hairline-soft` #efeee8 / `canvas` | 1.08:1 | 3.0 | **Fail** — frozen, scoped to decoration |
| `surface-card` #ffffff / `canvas` #f7f7f4 | 1.07:1 | — | Layer separation, not a text pair; disclosed as imperceptible |
| `canvas-soft` #fafaf7 / `canvas` #f7f7f4 | 1.03:1 | — | Layer separation; imperceptible without the pane's own hairline |
| `primary-active` #d04200 / `primary` #f54e00 | 1.34:1 | — | Why the focus ring is ink, not orange |

Elevation verdict (dimension C): the three layers are 1.07:1 and 1.03:1 apart. They are not distinguishable by surface alone — the hairline is the real boundary. Elevation is nonetheless expressed one consistent way throughout (hairline, never shadow), so nothing was restructured; the limitation is now stated in Accessibility.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `ease-standard` | opacity; translateY(-1px) on cards | Opacity only at 100ms, lift removed |
| Press | `{motion.duration-instant}` 60ms | `ease-standard` | opacity, scale(0.98) | Scale removed, colour change instant |
| Focus ring appear | `{motion.duration-instant}` 60ms | `ease-standard` | opacity | Unchanged |
| Page / route transition | `{motion.duration-base}` 150ms | `ease-enter` | opacity, translateY(4px) | Cross-fade at 100ms, travel removed |
| Modal / drawer enter | `{motion.duration-base}` 150ms | `ease-enter` | opacity, translateY(8px) / translateX | Fade at 100ms, travel removed |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `ease-exit` | opacity, transform | Fade at 100ms, travel removed |
| Dropdown open | `{motion.duration-fast}` 100ms | `ease-enter` | opacity, translateY(-4px) | Fade at 100ms, travel removed |
| Dropdown close | `{motion.duration-instant}` 60ms | `ease-exit` | opacity | Fade at 60ms |
| Toast enter | `{motion.duration-base}` 150ms | `ease-enter` | opacity, translateY(8px) | Fade at 100ms, travel removed |
| Toast exit | `{motion.duration-fast}` 100ms | `ease-exit` | opacity, transform | Fade at 100ms, travel removed |
| List enter | `{motion.duration-base}` 150ms, stagger 20ms | `ease-enter` | opacity, translateY(4px) | All items fade together at 100ms |
| List exit | `{motion.duration-fast}` 100ms, no stagger | `ease-exit` | opacity | Fade at 100ms |
| Loading | `{motion.duration-emphasis}` 300ms loop | linear / `ease-standard` | rotate(); skeleton opacity | Loop frozen, static indicator plus label |
| AI-timeline stage advance | `{motion.duration-base}` 150ms, stagger 20ms | `ease-standard` | opacity both sides | Cross-fade at 100ms; stage text still changes |

Every exit is shorter than its entrance. Only `transform` and `opacity` are animated. Travel is capped at 8px.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` (~line 291, `acc_lines` / `disclosed`) | Disclosure matches any Accessibility line containing a ratio and the token's name as a substring. A line about `hairline-strong` also contains the substring `hairline`, so disclosing the strong tone silently discloses the plain one. Here every tone has its own row, so the result is correct, but the check is weaker than it looks. | Match on word boundaries: `rf"(?<![a-z0-9-]){re.escape(fg_name)}(?![a-z0-9-])"`. |
| `theme-audit/audit.py` (~line 241, focus checks over `canvas`/`surface`/`accent`) | The focus ring is required to clear 3:1 against one representative `surface` only. A ring can pass while sitting at 2.79:1 on another real surface in the same file — `surface-strong` #e6e5e0 here, which is `badge-pill`'s fill. Cursor Orange would have passed the harness as a focus ring on that basis. | Route the focus check through `check_all` over every `surface`- and `canvas`-matching token, as the `border` and `text-dim` roles already are. |
| `theme-audit/audit.py` (~line 361, `tokens` score) | `tokens` scores only on missing colour roles, so a file with no `shadow:` group whose prose states real shadow values still scores 5, contrary to SPEC section 1. | Add a shadow-group check gated on an `rgba(` / `box-shadow` match in the prose. Does not affect this file, which documents no shadows. |
| `theme-audit/SPEC.md` section 2 (contrast table, lines 72–80) | The table states flat minima, but the component check applies a size-aware threshold (`threshold_for`, 3:1 at 24px+ or 18.66px+/700). Table and implementation describe different rules, which matters here because the 3:1 carve-out is the only defence the orange CTA could have had. | State the large-text carve-out in the SPEC table, as the implementation already has it. |

### Needs approval

Two extracted brand values fail AA and cannot be fixed without falsifying the document. Both are disclosed in the file; neither hex was touched.

1. **`button-primary` — white #ffffff on Cursor Orange #f54e00, 3.52:1, needs 4.5:1.** This is the brand's signature CTA.
   - Nearest passing value, same hue: **#c23d00** at 4.51:1 with white. A noticeably darker, browner orange — it would cost the brand its voltage.
   - Alternative that keeps the real orange: an ink label instead of white. `{colors.ink}` #26251e on #f54e00 is 4.37:1 — still short of 4.5:1, so this does not rescue it either.
   - Usage note that would make the real value defensible: **the 3:1 AA-Large threshold applies only at 24px+, or 18.66px+ at weight 700.** The CTA label is 14px/500 and this brand's own rules forbid bold, so no size note makes #f54e00 + white defensible at the documented label size. Either the label grows to 24px, the fill darkens, or the brand accepts a documented AA failure on its primary action.
2. **`timeline-pill-done` — white #ffffff on gold #c08532, 3.16:1, needs 4.5:1** at 11px uppercase.
   - Nearest passing value, same hue: **#8a5e1f** at 4.54:1 with white.
   - Cheaper fix, no hex change: swap the label to `{colors.ink}`, which measures **4.86:1 on the real gold** and passes. The other four timeline pills already use ink labels, so this also makes the set internally consistent. Not applied, because the white label is a documented observation of the brand rather than a token error — it needs a decision.

Lower-priority, same category: `{colors.semantic-success}` #1f8a65 at 4.01:1 on canvas (nearest passing #1b795a at 4.52:1), and `{colors.muted}` #807d72 at 3.84:1 / 4.12:1 (handled in-file by the prescribed `{colors.muted-accessible}` parallel plus an 18.66px floor on the real tone).

### Identity verdict

Still unmistakably Cursor. The additions lean on what the file already was rather than importing a generic layer: the focus ring is the brand's own warm ink #26251e with a cream offset — chosen precisely *because* this brand has exactly one chromatic voltage and spends it on the CTA, so a coloured ring would both compete with and collide with that CTA (1.34:1 orange-on-orange). The accessible parallels are warm greys drawn from the same cream-and-ink axis, not neutral slate. The states table is written in this brand's vocabulary: ink inversion for a selected pricing tier, and the AI-timeline pills treated as a loading state because that is literally their meaning.

The **Crisp** assignment is correct and I kept it. SPEC section 5 rule 2 applies on its face — this is an IDE and developer-tool identity and roughly half the page is code surfaces in JetBrains Mono. The one argument for Calm is real and worth naming: the file's own description says "quietly-confident", display sits at weight 400 with a stated magazine-editorial voice, and there are no shadows and no gradients, which are the tells SPEC lists for Calm. But rule 2 precedes rules 3 and 4, and the editorial voice is a *typographic* register, not a motion register; a code editor's marketing site still has to make a state change read as already done. I resolved the tension inside Crisp rather than against it: Crisp durations verbatim, but travel capped at 8px, no entrance choreography, and opacity-led rather than movement-led transitions. That is a Crisp file with a Calm hand, and it stays comparable to its Crisp siblings because the token block is unmodified — zero deviations, so no reason-for-deviation statement was needed.
