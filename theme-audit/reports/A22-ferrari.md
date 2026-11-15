## A22 · ferrari

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

All four harness-measured contrast failures were confirmed by hand and are unchanged in value — they moved from `contrast_unresolved` to `contrast_disclosed`. No brand hex was altered.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A (token contract) | `colors.focus` | No focus role at all. The prose already named #fff200 as "the global focus-ring color" but no token carried it, so nothing could reference a ring. |
| P0 | F (motion) | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion`. Known Gaps declared animation "out of scope". |
| P0 | G (accessibility) | whole file | No `## Accessibility` section, so four real AA failures were undisclosed. |
| P0 | B (colour) | `{colors.muted}` #666666 | 3.09:1 on canvas, 2.30:1 on surface-card. Documented as "sub-titles, captions on dark" — unusable as text at any size this file defines. |
| P0 | H (states) | all 20 component entries | Only `active` named anywhere. hover, focus-visible, pressed, disabled, loading, selected, error absent; the Iteration Guide said "Hover state never documented". |
| P1 | B | `{colors.hairline}` #303030 | 1.35:1 on canvas, and `text-input-on-dark` makes it the control's only boundary. |
| P1 | B | `{colors.muted-soft}` #8f8f8f | 4.08:1 on surface-card, yet typed as "disabled link text" — the naming implies an exemption it does not have. |
| P1 | A (shadow group) | Elevation & Depth | Prose documented a real `0 4px 8px rgba(0,0,0,0.1)` shadow with no `shadow:` group, so a `{shadow.small}` reference had nothing to resolve to. |
| P1 | C (elevation) | canvas -> canvas-elevated | 1.35:1 step. The layers are barely distinguishable, and the file mixed brightness-step, hairline and one shadow tier without saying which is primary. |
| P1 | B | `{colors.hairline-on-light}` / `-soft` | 1.51:1 and 1.19:1 on white. The harness skips them (theme-scoped), but they fail the 3:1 boundary threshold in reality. |
| P2 | B | `{colors.body}` #969696 on surface-card | 4.46:1 — misses AA by 0.04. The harness does not flag it (`body` is outside the `text-dim` patterns); disclosed anyway. |
| P2 | B | `{colors.semantic-success}` #03904a | 4.31:1 on canvas. Defensible only at 18px+/700. |
| P2 | B | `{colors.primary}` #da291c | 3.65:1 on canvas. Fine for the 80px/700 `race-position-cell`, not for body text. |
| P2 | E (radius) | `rounded` ladder | 0/2/4/6/8/12/9999 is internally consistent; no value sits off-scale. The file uses only `none`, `sm` and `full` in components, so `xs`/`md`/`lg`/`xl` are declared-but-unused rather than wrong. No fix. |
| P2 | D (typography) | all 13 roles | Every role has size, weight and line height. Body 14px/400/1.5 reads at 17.76:1 on canvas and 13.20:1 on cards. No fix needed. |
| P2 | H | `badge-pill` tap area | 4px × 12px padding on 11px type is under 44px when used as a filter chip. Noted in Accessibility as specified-not-verified. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#fff200"`, `focus-on-light: "#181818"` | Satisfies the missing `focus` role. Yellow is the file's own extracted ring colour; ink serves the white bands, which yellow cannot (1.17:1). |
| frontmatter `colors:` | — -> `muted-strong: "#a8a8a8"`, `hairline-strong: "#949494"`, `hairline-strong-on-light: "#767676"` | Parallel accessible tokens per SPEC §2. Frozen originals untouched and rescoped to decoration. |
| frontmatter | — -> `shadow:` group with `small: "0 4px 8px rgba(0,0,0,0.1)"` | The known dangling-`{shadow.small}` cause. Value taken verbatim from the file's own Elevation table. |
| frontmatter | — -> `motion:` group, Cinematic block verbatim | SPEC §4. Used literally, including `duration-reduced: 150ms`, so profile siblings stay comparable. |
| `## Colors` | — -> `### Focus Ring` subsection | Documents both rings with measured ratios, the two-tone ring over photography, and labels the geometry prescribed. |
| `## Colors` | — -> `### Accessible Parallel Tones` | States each `-strong` token's job and ratios, and marks them prescribed. |
| `## Colors` hairline + muted bullets | plain descriptions -> "Decoration only" / "Fails AA as text", with ratios and the substitute token | Scopes the frozen values rather than hiding or changing them. |
| `## Elevation & Depth` | inline `0 4px 8px rgba(0,0,0,0.1)` -> `{shadow.small}`; added the measured 1.35:1 / 13.20:1 steps and a statement that brightness-step is the single primary mechanism | Dimension C: one consistent expression of elevation, with the weak step admitted. |
| `## Elevation & Depth` table | added a `Control boundary` row | Separates the decorative hairline from the edge that must be seen. |
| `## Components` `text-input-on-dark` / `-on-light` | border `{colors.hairline}` -> keeps the extracted value, adds the `hairline-strong` substitution for the control edge | The one place the 1.35:1 hairline does load-bearing work. |
| `## Components` | — -> `### Interaction States` table, 14 rows × 8 states | Dimension H. Extracted vs prescribed stated in the lead paragraph. Bands and spec cells declared one- or two-state explicitly. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Token table, 15-row inventory, rules, and the reduced-motion rule. |
| after Motion | — -> `## Accessibility` | 22-row measured contrast table, per-surface ring table, tap targets, reduced motion, colour-alone cues. |
| `## Do's and Don'ts` | +3 Do's, +4 Don'ts | Motion timing, ring-per-band, `muted-strong` substitution; prohibitions on layout-property animation, yellow on white, hairline-as-edge, stagger past 8 items. |
| `## Iteration Guide` item 5 | "Hover state never documented." -> points at the new states table and distinguishes extracted hex from unobserved behaviour | The old line contradicted the new section. |
| `## Known Gaps` | one animation line -> five lines | Separates extracted from prescribed for motion, states, ring geometry, `-strong` tones and tap targets. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #ffffff / canvas #181818 | 17.76:1 | 4.5:1 | Pass |
| ink #ffffff / surface-card #303030 | 13.20:1 | 4.5:1 | Pass |
| body-on-light #181818 / canvas-light #ffffff | 17.76:1 | 4.5:1 | Pass |
| on-primary #ffffff / primary #da291c | 4.87:1 | 4.5:1 | Pass |
| body #969696 / canvas #181818 | 6.00:1 | 4.5:1 | Pass |
| body #969696 / surface-card #303030 | 4.46:1 | 4.5:1 | Fail (by 0.04, disclosed) |
| muted #666666 / canvas #181818 | 3.09:1 | 4.5:1 | Fail (frozen, disclosed) |
| muted #666666 / surface-card #303030 | 2.30:1 | 4.5:1 | Fail (frozen, disclosed) |
| muted-soft #8f8f8f / canvas #181818 | 5.49:1 | 4.5:1 | Pass |
| muted-soft #8f8f8f / surface-card #303030 | 4.08:1 | 4.5:1 | Fail (frozen, disclosed) |
| hairline #303030 / canvas #181818 | 1.35:1 | 3.0:1 | Fail (frozen, disclosed) |
| hairline-on-light #d2d2d2 / canvas-light #ffffff | 1.51:1 | 3.0:1 | Fail (frozen, disclosed) |
| hairline-soft #ebebeb / canvas-light #ffffff | 1.19:1 | 3.0:1 | Fail (frozen, disclosed) |
| hairline-soft #ebebeb / canvas #181818 | 14.89:1 | 3.0:1 | Pass (the harness's representative border token) |
| primary #da291c / canvas #181818 | 3.65:1 | 4.5:1 | Fail as body text; Pass at 3:1 for 80px/700 |
| semantic-success #03904a / canvas #181818 | 4.31:1 | 4.5:1 | Fail; Pass at 3:1 for 18px+/700 |
| semantic-warning #f13a2c / canvas #181818 | 4.55:1 | 4.5:1 | Pass |
| semantic-info #4c98b9 / canvas #181818 | 5.50:1 | 4.5:1 | Pass |
| focus #fff200 / canvas #181818 | 15.18:1 | 3.0:1 | Pass |
| focus #fff200 / surface-card #303030 | 11.28:1 | 3.0:1 | Pass |
| focus #fff200 / primary #da291c | 4.16:1 | 3.0:1 | Pass |
| focus #fff200 / canvas-light #ffffff | 1.17:1 | 3.0:1 | Fail — never drawn there; `focus-on-light` serves light bands |
| focus-on-light #181818 / canvas-light #ffffff | 17.76:1 | 3.0:1 | Pass |
| focus-on-light #181818 / surface-soft-light #f7f7f7 | 16.57:1 | 3.0:1 | Pass |
| focus-on-light #181818 / surface-strong-light #ebebeb | 14.89:1 | 3.0:1 | Pass |
| focus-on-light #181818 / primary #da291c | 3.65:1 | 3.0:1 | Pass |
| muted-strong #a8a8a8 / canvas #181818 | 7.47:1 | 4.5:1 | Pass (prescribed) |
| muted-strong #a8a8a8 / surface-card #303030 | 5.55:1 | 4.5:1 | Pass (prescribed) |
| hairline-strong #949494 / canvas #181818 | 5.85:1 | 3.0:1 | Pass (prescribed) |
| hairline-strong #949494 / surface-card #303030 | 4.35:1 | 3.0:1 | Pass (prescribed) |
| hairline-strong-on-light #767676 / canvas-light #ffffff | 4.54:1 | 3.0:1 | Pass (prescribed) |
| hairline-strong-on-light #767676 / surface-strong-light #ebebeb | 3.81:1 | 3.0:1 | Pass (prescribed) |
| canvas #181818 / canvas-elevated #303030 (elevation step) | 1.35:1 | — | Weak step, disclosed |
| canvas-elevated #303030 / canvas-light #ffffff (elevation step) | 13.20:1 | — | Strong step |

### Motion inventory

Cinematic profile, used verbatim. Prescribed, not measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity`; `scale(1.03)` on card photography only | No scale; opacity at 150ms |
| Press | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `scale(0.99)` + `opacity` | No scale; fill change, no transition |
| Focus ring | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` on the ring | Instant, full opacity |
| Page / route transition | `{motion.duration-slow}` 600ms out, `{motion.duration-emphasis}` 900ms incoming hero | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(16px)`; hero `scale(1.04 -> 1.0)` | No travel or scale; cross-fade 150ms |
| Modal / drawer enter | `{motion.duration-base}` 400ms | `{motion.ease-enter}` | `opacity` + `translateY(24px)` / `translateX(100% -> 0)` | Opacity only, 150ms |
| Modal / drawer exit | `{motion.duration-fast}` 240ms | `{motion.ease-exit}` | same, reversed | Opacity only, 150ms |
| Dropdown open | `{motion.duration-base}` 400ms | `{motion.ease-enter}` | `opacity` + `translateY(-8px -> 0)` | Opacity only, 150ms |
| Dropdown close | `{motion.duration-fast}` 240ms | `{motion.ease-exit}` | same, reversed | Opacity only, 150ms |
| Toast enter | `{motion.duration-base}` 400ms | `{motion.ease-enter}` | `opacity` + `translateY(16px -> 0)` | Opacity only, 150ms |
| Toast exit | `{motion.duration-fast}` 240ms | `{motion.ease-exit}` | same, reversed | Opacity only, 150ms |
| List enter | `{motion.duration-base}` 400ms per item, `{motion.stagger-step}` 80ms between items, capped at 8 | `{motion.ease-enter}` | `opacity` + `translateY(24px -> 0)` | No travel, no stagger; one fade at 150ms |
| List exit | `{motion.duration-fast}` 240ms, no stagger | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | Opacity only, 150ms |
| Loading | 1400ms loop | `{motion.ease-standard}` | `opacity` 0.4 to 1.0 | Loop removed; static 0.6 opacity + text status |
| Brand ambience — hero push-in | 12000ms, one pass, no loop | `{motion.ease-standard}` | `scale(1.0 -> 1.04)` | Removed; holds at 1.0 |

Exit is shorter than its entrance in every pair. `transform` and `opacity` only; the harness reports `layout_animation_mentions: []`.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, `same_theme()` (~line 200) via `theme_of()` (~line 186) | A token named `focus-on-dark` is theme-tagged `dark`, while `canvas` and `surface-card` are theme `default`, so `check("focus", …)` is skipped entirely. A file following SPEC §1's literal advice ("defines `focus` **and** `focus-on-dark`") gets its ring never measured and still scores tokens 5. I avoided this by naming the pair `focus` / `focus-on-light`, which is a naming workaround, not a fix. | Treat an untagged dark canvas as theme `dark` for the focus check, or exempt the `focus` role from `same_theme()` and check every `focus-*` token against every surface it could plausibly sit on. |
| `theme-audit/audit.py`, `REQUIRED_COLOR_ROLES["text-dim"]` (~line 26) | `body` is matched by the `text` role (`^body$`, line 24) but by no `text-dim` pattern, so `body: #969696` at 4.46:1 on `#303030` is invisible to `check_all`. Any "default running-text" token named `body` escapes the secondary-text sweep. | Either add `^body$` to the `text-dim` candidates, or run `check_all("text", "surface", 4.5, …)` so every ink tone is swept the way the dim tones are. |
| `theme-audit/audit.py`, `check_all("border", …)` (line 234) | Boundary tokens are swept against the representative `canvas` only. `hairline-on-light` #d2d2d2 at 1.51:1 and `hairline-soft` #ebebeb at 1.19:1 on this file's own `canvas-light` white band are never checked, because `canvas-light` is not the representative canvas. | Sweep boundary tokens against every `canvas-*` and `surface-*` key whose theme tag matches, not just the representative canvas. |
| `theme-audit/audit.py`, `disclosed()` (~line 293) | Matching is a bare substring of the foreground token name, so a line disclosing `muted-soft` also satisfies the separate `muted` failures. One row can clear three failures. | Require a word-boundary match on the token name, and require the row to also mention the background token. |
| `theme-audit/SPEC.md` §1, focus-ring paragraphs | §1 gives three prescriptions for a file with a dark canvas plus white bands plus a chromatic accent — the `focus`/`focus-on-dark` pair, the "one mid-luminance ring" option, and the two-tone photography ring — with no stated precedence, so two agents auditing similar files will land differently. | State precedence: prefer the single mid-luminance ring where one exists; fall back to the pair when the brand's own extracted ring colour cannot serve both polarities (this file's case). |

### Needs approval

Four extracted hexes fail their threshold and were **not** changed. Each is disclosed in the file with its measured ratio and a prescribed substitute. Approval is needed to either accept the stated usage note or adopt the nearest passing value.

| Token | Real value | Fails | Nearest passing value | Usage note that makes the real value defensible |
|---|---|---|---|---|
| `{colors.muted}` | #666666 | 3.09:1 on canvas (need 4.5), 2.30:1 on surface-card | `#a8a8a8` (7.47:1 / 5.55:1) — shipped as `{colors.muted-strong}` | None is defensible for text. Even the 3:1 large-text allowance fails on `surface-card`. The only honest note is "decorative or non-essential ornament, never copy". |
| `{colors.muted-soft}` | #8f8f8f | 4.08:1 on surface-card (need 4.5) | `#a8a8a8` (5.55:1) | Passes on `canvas` at 5.49:1. Defensible on cards only for 18px+/700 labels, where 3:1 applies, or as genuinely disabled text (WCAG-exempt), which is what the file's own description claims. |
| `{colors.hairline}` | #303030 | 1.35:1 on canvas (need 3.0) | `#949494` (5.85:1) — shipped as `{colors.hairline-strong}` | Defensible as pure decoration: a tonal seam between two dark bands where the boundary is not the only way to perceive the grouping. Not defensible as the edge of `text-input-on-dark`, which is where the captured markup puts it. |
| `{colors.hairline-on-light}` / `{colors.hairline-soft}` | #d2d2d2 / #ebebeb | 1.51:1 / 1.19:1 on `canvas-light` (need 3.0) | `#767676` (4.54:1) — shipped as `{colors.hairline-strong-on-light}` | Defensible as decorative rules between light editorial bands. Not defensible as a control boundary. |

Two further items, flagged but below the harness threshold:

- `{colors.body}` #969696 on `{colors.surface-card}` — 4.46:1, short of 4.5 by 0.04. Nearest passing: `#989898` (4.56:1). Defensible note: the token is specified as "default running-text on dark", where dark means `{colors.canvas}` (6.00:1); on cards it needs the `-strong` substitute.
- `{colors.semantic-success}` #03904a on canvas — 4.31:1. Nearest passing: `#049c50` (4.84:1). Defensible note: confirmation labels render at `{typography.title-md}` 18px/700 or larger, where 3:1 applies.

Also for approval: `{colors.focus-on-light}` #181818 is a **prescribed** token, not extracted. It reuses the brand's existing ink hex rather than inventing a chromatic ring, but it is still a token the real site does not define. The alternative — drawing the extracted #fff200 on white at 1.17:1 — is an invisible ring.

### Identity verdict

**Cinematic is the right profile, and the file still reads as Ferrari.**

The assignment is correct on SPEC §5's first rule twice over — luxury *and* automotive — and the file supplies the tell independently of its dark canvas: full-bleed hero photography as the page chrome, sparse type at display weight 500, 96–128px band padding, and an explicit prohibition on bolding display copy. I did not need the near-black background to reach Cinematic, which matters because this file also carries white editorial bands. No argument for a different profile.

The edits avoided a generic token dump in three specific ways. The focus ring is the brand's own documented Hypersail yellow, not a borrowed blue — and the one place it cannot go (white editorial bands) is handled with brand ink rather than an invented accent, so the file still carries exactly one chromatic signal, Rosso Corsa, plus the scoped sub-brand yellow. The motion section is anchored to brand-specific objects: the hero photograph's slow push-in, the livery band, the race-calendar row, the driver card, the 80px race-position numerals. The states table names the real components (`race-position-cell`, `preowned-listing-card`, `livery-band`) and says plainly where a surface has one state because it is a layout band — itself a Ferrari fact, since most of this site is bands and photographs rather than controls.

Nothing extracted was lost. Every frozen hex is intact and every added value is labelled prescribed. The added length is mostly the Accessibility table, which is measurement rather than voice.

One honest drift risk: the prescribed `-strong` greys (#a8a8a8, #949494, #767676) are the sort of values any audit would produce, and they do not come from Ferrari. They are confined to the parallel-token subsection and marked prescribed, so a reader can tell brand from remedy, but they are the least Ferrari-specific thing now in the file.
