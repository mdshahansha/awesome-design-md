## A16 · composio

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A | `colors.focus` | No focus token at all. The brand's own `{colors.primary}` (#0007cd) measures 1.75:1 on `{colors.canvas}`, so it cannot serve as an indicator — a ring had to be derived. |
| P0 | F | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Known Gaps declared animation "out of scope". |
| P0 | G | whole file | No `## Accessibility` section; five measurable contrast failures undisclosed. |
| P0 | B | `hairline-strong` | `button-outline` was specified as a 1px `hairline-strong` edge — the control's only boundary, at 1.52:1 on canvas. Unusable as a control boundary. |
| P1 | H | all 21 component entries | No entry named a state. Only `button-primary-active` implied press; hover, focus-visible, disabled, loading, selected, error appeared nowhere. |
| P1 | B | `muted-soft` | Documented as "Disabled text" but nothing scoped it away from live text; 3.34:1 on canvas / 3.09:1 on surface-card. |
| P1 | E | borders / focus | No border-width or focus-ring ladder anywhere; widths existed only as the prose phrase "1px". |
| P1 | C | elevation ladder | Elevation is consistently brightness-only (good — no shadow/border mixing), but the four steps measure 1.08-1.12:1 and the file claimed depth without stating that no single step is independently perceivable. |
| P2 | B | `muted` on `surface-card-elevated` | 4.49:1 — 0.01 short of AA on the secondary-button and terminal-pane surface. Not caught by the harness, which checks `surface-card` only. |
| P2 | B | `accent-violet` | 3.35:1 on canvas. Fine as illustration-only, but that restriction was asserted without the ratio. |
| P2 | D | typography | All 14 roles already carry family, size, weight, line height and letter spacing; body at 16px/1.5 in `{colors.body}` is 8.06:1 on canvas. No defect found. |
| P2 | G | Responsive -> Touch Targets | Claimed 40px CTAs were "at WCAG AA, padded for AAA" with no figure; AAA is 44x44, so 40px is 4px short. |
| P2 | A | `shadow:` group | Not added: the file documents no real shadow value and explicitly forbids shadow tiers, so SPEC section 1's shadow condition does not apply. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#6b7bff"` | SPEC section 1 requires a focus role; Composio Blue lifted until it clears 3:1 on every surface here. Prescribed, labelled as such. |
| frontmatter `colors:` | — -> `hairline-control: "#757575"` | Parallel accessible boundary token per SPEC section 2; the three extracted hairlines stay frozen and are scoped to decoration. |
| frontmatter | — -> `motion:` group | Crisp profile block, verbatim from SPEC section 4. |
| frontmatter `components:` | `button-outline`, `text-input`, `search-input` -> added `borderColor` / `focusRingColor` | The control boundary and ring now resolve to tokens instead of prose. |
| Colors -> Hairlines | 3 bullets -> 4 bullets + decorative-only preamble | Names the AA failure in place and introduces the accessible parallel. |
| Colors -> Focus (new) | — -> focus-ring entry | States the prescribed ring, its offset, and why `{colors.primary}` cannot be it. |
| Colors -> Text | `muted` / `muted-soft` bullets | Added measured ratios; scoped `muted-soft` to disabled/decorative. |
| Elevation & Depth | — -> "How far apart the layers actually sit" table | States the real 1.08-1.12:1 steps and the 1px-edge mitigation for small raised elements. |
| Shapes | — -> "Border & Focus Ring Widths" table | One two-step width ladder; the ring inherits its host radius, so no value sits outside its scale. |
| Components -> `button-outline` | 1px hairline-strong -> 1px `{colors.hairline-control}` | A control's only boundary cannot be a 1.52:1 tone. |
| Components -> `text-input`, `search-input` | — -> border, focus ring, error border | Form states were absent. |
| Components -> Interaction States (new) | — -> table, one row per component entry | SPEC section 7. Prescribed; static bands say "default only". |
| after `## Components` | — -> `## Motion & Animation` | SPEC sections 3 and 6; first line states it is prescribed, not measured. |
| after Motion | — -> `## Accessibility` | SPEC section 3; discloses all five frozen failures with measured ratios. |
| Do's and Don'ts | +3 Do's, +3 Don'ts | Focus ring, boundary token, Crisp motion ceiling, and the three new traps. |
| Responsive -> Touch Targets | "at WCAG AA, padded for AAA" -> explicit 24x24 / 44x44 figures | The old claim was unsupported. |
| Iteration Guide item 5 | "Hover state never documented." -> points at the prescribed states table | Stale after the states work. |
| Known Gaps | "Animation timings out of scope." -> 4 prescription disclosures + non-computable list | Nothing added to the file may read as extracted. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #ffffff / `canvas` #0f0f0f | 19.17:1 | 4.5:1 | Pass |
| `ink` #ffffff / `surface-card` #181818 | 17.76:1 | 4.5:1 | Pass |
| `body` #a8a8a8 / `canvas` #0f0f0f | 8.06:1 | 4.5:1 | Pass |
| `body` #a8a8a8 / `surface-card` #181818 | 7.47:1 | 4.5:1 | Pass |
| `on-primary` #ffffff / `primary` #0007cd | 10.98:1 | 4.5:1 | Pass |
| `muted` #888888 / `canvas` #0f0f0f | 5.41:1 | 4.5:1 | Pass |
| `muted` #888888 / `surface-card` #181818 | 5.01:1 | 4.5:1 | Pass |
| `muted` #888888 / `surface-card-elevated` #222222 | 4.49:1 | 4.5:1 | Fail — 0.01 short; disclosed, use `body` there |
| `muted-soft` #666666 / `canvas` #0f0f0f | 3.34:1 | 4.5:1 | Fail — frozen; disclosed, disabled/decorative only |
| `muted-soft` #666666 / `surface-card` #181818 | 3.09:1 | 4.5:1 | Fail — frozen; disclosed |
| `hairline-soft` #1a1a1a / `canvas` #0f0f0f | 1.10:1 | 3.0:1 | Fail — frozen; disclosed, decorative only |
| `hairline` #222222 / `canvas` #0f0f0f | 1.20:1 | 3.0:1 | Fail — frozen; disclosed, decorative only |
| `hairline-strong` #333333 / `canvas` #0f0f0f | 1.52:1 | 3.0:1 | Fail — frozen; disclosed, decorative only |
| `hairline-control` #757575 / `canvas` #0f0f0f | 4.16:1 | 3.0:1 | Pass (prescribed) |
| `hairline-control` #757575 / `surface-card` #181818 | 3.85:1 | 3.0:1 | Pass |
| `hairline-control` #757575 / `surface-card-elevated` #222222 | 3.45:1 | 3.0:1 | Pass |
| `hairline-control` #757575 / `surface-strong` #2a2a2a | 3.12:1 | 3.0:1 | Pass |
| `focus` #6b7bff / `canvas` #0f0f0f | 5.39:1 | 3.0:1 | Pass (prescribed) |
| `focus` #6b7bff / `canvas-deep` #000000 | 5.90:1 | 3.0:1 | Pass |
| `focus` #6b7bff / `surface-card` #181818 | 4.99:1 | 3.0:1 | Pass |
| `focus` #6b7bff / `surface-card-elevated` #222222 | 4.47:1 | 3.0:1 | Pass |
| `focus` #6b7bff / `surface-strong` #2a2a2a | 4.03:1 | 3.0:1 | Pass |
| `focus` #6b7bff / `primary` #0007cd | 3.09:1 | 3.0:1 | Pass |
| `focus` #6b7bff / `primary-active` #0005a3 | 3.81:1 | 3.0:1 | Pass |
| `primary` #0007cd / `canvas` #0f0f0f | 1.75:1 | 3.0:1 | Fail — why the brand hex cannot be the ring |
| `accent-violet` #7b3aed / `canvas` #0f0f0f | 3.35:1 | 4.5:1 | Fail — illustration-only; disclosed |
| `accent-cyan` #00d4ff / `canvas` #0f0f0f | 10.83:1 | 4.5:1 | Pass |
| `semantic-error` #ff4d4d / `canvas` #0f0f0f | 5.86:1 | 4.5:1 | Pass |
| `semantic-success` #33d17a / `canvas` #0f0f0f | 9.62:1 | 4.5:1 | Pass |
| Elevation step `surface-card` / `canvas` | 1.08:1 | — | Layer not independently perceivable; disclosed |
| Elevation step `surface-card-elevated` / `surface-card` | 1.12:1 | — | Same |
| Elevation step `surface-strong` / `surface-card-elevated` | 1.11:1 | — | Same |
| Elevation step `canvas` / `canvas-deep` | 1.10:1 | — | Same |

### Motion inventory

Crisp profile, prescribed. `duration-instant` 60ms · `duration-fast` 100ms · `duration-base` 150ms · `duration-slow` 220ms · `duration-emphasis` 300ms · `stagger-step` 20ms · `duration-reduced` 100ms.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`, background cross-fade | Unchanged — no travel to remove |
| Press | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed; colour only |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on ring | Ring appears untransitioned |
| Page / route transition | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` | `opacity` at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + translateY(4px -> 0) | Travel removed; fade at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown open | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` + scaleY(0.98 -> 1) | Scale removed; fade at `{motion.duration-reduced}` |
| Dropdown close | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + translateY(8px -> 0) | Travel removed; fade at `{motion.duration-reduced}` |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| List enter | `{motion.duration-fast}` per item, `{motion.stagger-step}` apart, capped at 8 | `{motion.ease-enter}` | `opacity` + translateY(4px -> 0) | Stagger and travel removed; one list fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-instant}`, no stagger | `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-reduced}` |
| Loading | 800ms, infinite | linear | `transform: rotate()`; `opacity` pulse on skeletons | Spinner freezes; skeletons hold a static fill |
| Spotlight-glow reveal | `{motion.duration-emphasis}`, then static | `{motion.ease-enter}` | `opacity` | Full opacity, no transition |

Every exit is shorter than its entrance; only the loader is infinite; nothing animates on first paint ahead of content.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, the `find_role` call for the `surface` role (line ~169) | The `surface` role resolves to a single representative key, so text is only ever checked against `surface-card`. This file's `muted` on `surface-card-elevated` fails at 4.49:1 and the harness cannot see it. | Add a `check_all("text-dim", ...)` pass over every `surface`-matching key, as already done for `border` and `text-dim` against canvas. |
| `theme-audit/audit.py`, `score["contrast"]` (line ~390) | A file that defines no boundary token at all scores 5 for contrast, while one that honestly defines three weak hairlines scores 1 until it writes disclosures. The incentive runs the wrong way for files with poor token coverage. | Floor the contrast score on `roles_missing`, or score coverage and disclosure separately. |
| `theme-audit/SPEC.md` section 1 | The spec mandates a `focus` role but gives no guidance for a dark-canvas brand whose accent is itself too dark to be a ring (#0007cd at 1.75:1). The monochrome and three-polarity cases are covered; this one is not. | Add a clause: where the accent fails 3:1 against the canvas, lift the accent's own hue to the nearest value clearing 3:1 on every defined surface and label it prescribed. |
| `theme-audit/audit.py`, `acc_lines` (line ~299) | Disclosure requires a ratio token on the same line as the colour name, so a correctly disclosed failure written across two lines scores as hidden. | Widen the disclosure window to the enclosing list item or table row. |

### Needs approval

1. **`focus: "#6b7bff"`** — prescribed, not extracted. It is `{colors.primary}` (#0007cd) lifted in luminance until it clears 3:1 on every surface the file defines, including the blue CTA (3.09:1). The real brand hex measures 1.75:1 on `{colors.canvas}` and cannot be a focus indicator. The nearest passing value closer to brand was #3d4bff (3.33:1 on canvas), rejected because it drops to 2.49:1 over `{colors.surface-strong}` dropdowns. Usage note that would make #3d4bff defensible: rings drawn only on `{colors.canvas}` and `{colors.canvas-deep}`.
2. **`hairline-control: "#757575"`** — prescribed accessible parallel to the three frozen hairlines (1.10 / 1.20 / 1.52:1 on canvas). Chosen as the lightest grey still reading as a hairline that clears 3:1 on all four defined surfaces (4.16 / 3.85 / 3.45 / 3.12:1). The nearest passing value against canvas alone is #606060 (3.05:1), which fails on `{colors.surface-strong}` at 2.33:1.
3. **`muted` #888888 on `surface-card-elevated` at 4.49:1** — no hex change proposed. Nearest passing value: #8a8a8a (4.61:1). Usage note that makes the real value defensible: `{colors.muted}` is for 18px+ labels on elevated surfaces, where 3:1 applies; below that use `{colors.body}` (6.69:1). Documented as a failure rather than corrected.
4. **`muted-soft` #666666 kept frozen.** Nearest passing value for body text: #949494 (6.32:1 canvas / 5.85:1 surface-card). Usage note that makes #666666 defensible: disabled text (WCAG-exempt) and 24px+ decorative labels, where 3:1 applies — it clears at 3.34:1 on canvas and only just at 3.09:1 on `surface-card`.
5. **`accent-violet` #7b3aed at 3.35:1 on canvas** — illustration-only, carries no text and no boundary. No change proposed.
6. **The whole Interaction States table and the whole motion system are prescribed.** If the owner holds captures of real hover or dropdown behaviour, these should be replaced with extracted values.

### Identity verdict

Still unmistakably Composio. The file's distinguishing facts are untouched: the single deep-electric-blue voltage, the 2x2 terminal-mockup grid as hero anchor, brightness-step-not-shadow elevation, abcDiatype at weight 500 with JetBrains Mono on every code surface, 8px CTAs rather than pills, and the 96px section rhythm. The two new colour tokens are derived from the brand's own palette — the ring is Composio Blue lifted, the boundary is a step on the existing neutral ramp — rather than imported from a generic scale, and both are named as prescribed. The new Elevation sub-table and Accessibility section are specific to this file's near-black ladder; neither would transplant to another site.

**The assigned Crisp profile is correct and was used unchanged.** Composio is a developer-tool identity for AI-agent tool integration, so SPEC section 5 rule 2 applies directly, and the file's own observable signals agree: terminal mockups as the central brand device, monospace code surfaces throughout, compact 8px developer-ergonomic radii, no drop-shadow tiers, and an explicit prohibition on a secondary brand colour. Nothing here argues for Cinematic (no full-bleed photography, no sparse-type slow reveal), Playful (cyan and violet are illustration-only against a near-black canvas) or Calm (the voice is tool-like, not editorial). One deviation was considered and rejected: the spotlight glow is the one place the brand reads atmospheric and could have justified a reveal longer than `duration-emphasis` 300ms, but lengthening it would break comparability with sibling Crisp files for no real gain, so the glow uses the profile's own value and is stated as a one-shot reveal, not ambience.
