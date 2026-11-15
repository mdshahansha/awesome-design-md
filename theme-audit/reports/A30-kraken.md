## A30 · kraken

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

- **Before:** 1 · 5 · 5 · 1 · 1 · 1
- **After:** 5 · 5 · 5 · 5 · 5 · 5

**Harness changed mid-review.** After my first clean run (all 5s), another agent committed a change to `theme-audit/audit.py` that composites `rgba()` colour tokens over the canvas and measures them. That re-scored this file to contrast 4 with one new undisclosed failure — `success-subtle` composited to #d9efe6, measured as a *semantic tone used as text* at 1.2:1, although it is only ever a badge fill. I disclosed all four opacity fills with their measured composite ratios and a statement of what they are and are not used for. Final run is 5 · 5 · 5 · 5 · 5 · 5 with 4 disclosed failures. Anyone comparing reports across this run should know the harness is not identical between agents.

The before-contrast 5 and before-refs 5 are artefacts of an empty file: with no frontmatter there were no tokens to measure and no references to resolve. After conversion the file carries 15 hex colours, 5 real contrast failures — all three distinct ones disclosed in the Accessibility section with their measured ratios — and 0 dangling references.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, J | whole file | No frontmatter token block at all. Every one of the 8 required colour roles was missing; `{group.token}` references were impossible. Legacy numbered-heading format. |
| P0 | C (section contract) | headings | All 12 required sections missing by name: the numbered variant (`## 1. Visual Theme & Atmosphere` …) matched none of them. `Motion & Animation`, `Accessibility`, `Shapes` and `Known Gaps` had no content at all, not just the wrong name. |
| P0 | F | motion | No motion tokens, no motion section, no reduced-motion rule, no durations or easings anywhere in the file. |
| P0 | G | accessibility | No Accessibility section. Kraken's secondary text tone (#9497a9, 2.89:1) and divider hairline (#dedee5, 1.34:1) both fail AA and the file said nothing about either. |
| P0 | A | focus ring | No focus ring defined, and the brand's single-hue purple palette means the obvious choice does not work: `#5b1ecf` on the `#7132f5` button measures 1.37:1. |
| P1 | H | all 7 components | No state named anywhere. Not one of hover, focus-visible, active, pressed, disabled, loading, selected, error appeared in the file. |
| P1 | B | `#9497a9` | Documented as "Secondary text" with no warning. It fails 1.4.3 at 2.89:1 and does not even clear the 3:1 large-text threshold, so there is no size at which it is compliant. Extracted value, left unchanged, now disclosed. |
| P1 | B | `#dedee5` | Documented as "Divider borders" at 1.34:1 against white — fails 1.4.11. Scoped to decoration in the file; no parallel accessible token was needed because the only documented control boundary is the `#5741d8` outlined-button border at 6.66:1. |
| P1 | B | `#149e61` | "Green accent for positive/success states" with no usage note. As text it is 3.45:1 and fails; the file only ever uses it as a 16% fill, with `#026b3f` (6.61:1) carrying the text. Now stated. |
| P1 | D | `Micro` role | 7px / 500 / line-height 1.00. Below any practical reading floor, with no usage note. Now scoped to ornamental labels duplicated at 12px+. |
| P1 | E | spacing ladder | The stated list (1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 15, 16, 20, 24, 25px) is a measured inventory, not a scale: 13, 15 and 25 sit off any 4px rhythm. Carried verbatim with that stated plainly, rather than smoothed into a fake ladder. |
| P2 | D | `Micro` role | The source table recorded `uppercase` in its **Letter Spacing** column — a text transform in a tracking field. Carried as `textTransform`; the real letter-spacing is now a Known Gap. |
| P2 | D | 4 type roles | `Button` (weight 500–600), `Caption` (400–700, line-height 1.43–1.71) and `Small` (400–500) were extracted as ranges, not values. Ranges preserved verbatim; picking an end would have been invention. |
| P2 | C | elevation | Two shadow levels at 3–4% alpha and nothing else. Expressed one consistent way (shadow), but the file previously never said that borders are a variant/divider device rather than an elevation device. Now stated. |
| P2 | C | surface layering | `canvas` and `surface` are both `#ffffff` — the only surface the prose states. The canvas/surface/raised comparison dimension C asks for cannot be made here, and that is now in Known Gaps rather than papered over with an invented second grey. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Top of file | no frontmatter -> full YAML block: `colors` (15 hexes + 4 rgba), `typography` (10 roles), `spacing` (15), `rounded` (8), `shadow` (2), `motion` (10), `components` (7) | Dimension J. Every value read out of the file's own prose; nothing added from outside it. |
| `colors` roles | — -> `canvas`, `surface`, `ink`, `text-secondary`, `border-subtle`, `primary`, `on-primary`, `focus` | All 8 required roles now resolve. `tokens` 1 -> 5. |
| `colors.focus` / `colors.focus-inner` | — -> `#101114` ring + `#ffffff` 2px offset | Dimension A. A purple ring fails on the purple button (1.37:1). SPEC section 1's offset pattern applies: brand ink plus an opposite-polarity offset. Measured 18.88:1 on canvas and surface, 3.13:1 on the `#7132f5` fill, band separation 18.88:1. Labelled prescribed. |
| `shadow` group | rgba values in prose with no token -> `shadow.subtle`, `shadow.micro` | SPEC section 1: a `shadow:` group is required where the file states real shadow values. It stated two. |
| All 9 numbered headings | `## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide` -> `## Overview`, `## Colors`, `## Typography`, `## Components`, `## Layout`, `## Elevation & Depth`, `## Do's and Don'ts`, `## Responsive Behavior`, `## Agent Prompt Guide` | Dimension J / SPEC section 3. Prose kept verbatim where it was not being fixed; token references added in place of bare hexes. |
| New `## Shapes` | radius list was one line inside `## 5. Layout Principles` -> its own section with an 8-row token table and use column | Required section. The radius line was **moved**, not duplicated. |
| New `## Motion & Animation`, placed after `## Components` | absent -> Calm block verbatim from SPEC section 5, prescribed-not-measured disclaimer as the first line, 10-row interaction table, motion rules, `prefers-reduced-motion` block | Dimension F. `motion` 1 -> 5. |
| New `## Accessibility` | absent -> 15-row measured contrast table, a "Where Kraken's real values fail AA" subsection, focus-ring visibility per surface, type size, reduced motion, and an explicit list of what a document cannot verify | Dimension G. Disclosure moves the 3 real failures out of `contrast_unresolved`. |
| New `## Known Gaps` | absent -> 5 grouped subsections | Dimension J: everything the prose did not state, listed instead of invented. |
| `## Components` | 7 prose blocks, no states -> same 7 blocks with contrast ratios, plus a state matrix covering all 8 states | Dimension H. `states` 1 -> 5. Every unknown value reads "not extracted"; the two badges are declared single-state. |
| `## Layout` | bare `### Spacing: 1px, 2px…` heading -> token list plus a paragraph naming the off-scale values | Dimension E, and the old form was a heading used as content. |
| `## Do's and Don'ts` | 5 entries -> 8, adding the three contrast prohibitions and the layout-property rule | The file now owns its own failures at the point of use. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #101114 on `canvas` #ffffff | 18.88:1 | 4.5:1 | Pass |
| `ink` #101114 on `surface` #ffffff | 18.88:1 | 4.5:1 | Pass |
| `on-primary` #ffffff on `primary` #7132f5 | 6.04:1 | 4.5:1 | Pass |
| `purple-dark` #5741d8 on `canvas` | 6.66:1 | 4.5:1 | Pass |
| `purple-deep` #5b1ecf on `canvas` | 8.3:1 | 4.5:1 | Pass |
| `badge-ink` #484b5e on `canvas` | 8.59:1 | 4.5:1 | Pass |
| `success-text` #026b3f on `canvas` | 6.61:1 | 4.5:1 | Pass |
| `success-text` on composited `success-subtle` #d9efe6 | 5.49:1 | 4.5:1 | Pass |
| `primary` on composited `purple-subtle` #ebe5fe | 4.94:1 | 4.5:1 | Pass |
| `badge-ink` on composited `neutral-subtle` #ededf0 | 7.36:1 | 4.5:1 | Pass |
| `ink` on composited `gray-subtle` #f6f7f8 | 17.6:1 | 4.5:1 | Pass |
| `focus` #101114 on `canvas` | 18.88:1 | 3.0:1 | Pass |
| `focus` #101114 on `primary` #7132f5 | 3.13:1 | 3.0:1 | Pass |
| `focus-inner` #ffffff against `focus` #101114 | 18.88:1 | 3.0:1 | Pass |
| `purple-dark` border on `canvas` | 6.66:1 | 3.0:1 | Pass |
| **`text-secondary` #9497a9 on `canvas`** | **2.89:1** | 4.5:1 | **Fail — extracted, disclosed** |
| **`text-secondary` #9497a9 on `surface`** | **2.89:1** | 4.5:1 | **Fail — extracted, disclosed** |
| **`border-subtle` #dedee5 on `canvas`** | **1.34:1** | 3.0:1 | **Fail — extracted, disclosed** |
| **`border-subtle` #dedee5 on `surface`** | **1.34:1** | 3.0:1 | **Fail — extracted, disclosed** |
| **`success` #149e61 on `canvas`, as text** | **3.45:1** | 4.5:1 | **Fail — extracted, disclosed (used as a 16% fill)** |
| `neutral-cool` #686b82 at 24% composited (#dbdbe1) on `canvas` | 1.38:1 | 3.0:1 | Fail — extracted, disclosed; decorative border only |
| `neutral-cool` #686b82 at full opacity on `canvas` | 5.23:1 | 4.5:1 | Pass (not tokenised as text; prose calls it a neutral/border tone) |
| `purple-deep` #5b1ecf on `primary` #7132f5 | 1.37:1 | 3.0:1 | Fail — this is why the focus ring is ink, not purple |
| **`success-subtle` composited #d9efe6 on `canvas`** | **1.2:1** | 4.5:1 | **Fail as text — extracted, disclosed; it is a badge fill, `success-text` carries the ink at 5.49:1** |
| `purple-subtle` composited #ebe5fe on `canvas` | 1.22:1 | 4.5:1 | Fail as text — disclosed; button fill, `primary` carries the ink at 4.94:1 |
| `neutral-subtle` composited #ededf0 on `canvas` | 1.17:1 | 4.5:1 | Fail as text — disclosed; badge fill, `badge-ink` carries the ink at 7.36:1 |
| `gray-subtle` composited #f6f7f8 on `canvas` | 1.07:1 | 4.5:1 | Fail as text — disclosed; button fill, `ink` carries the text at 17.6:1 |

All ratios computed with WCAG 2.1 relative luminance in a python3 stdlib snippet; `rgba()` fills were composited over `#ffffff` first. None estimated.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity` | Unchanged — already opacity-only at 150ms |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity`, no scale | Unchanged |
| Focus | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` of the ring | Zero duration — must not lag the keyboard |
| Page / route transition | in 250ms, out 150ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(8px→0)` | Travel removed; cross-fade at `{motion.duration-reduced}` |
| Modal / drawer | in 250ms, out 150ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(16px→0)` / `translateX(100%→0)` | Travel removed; cross-fade at 150ms, backdrop still fades |
| Dropdown | in 150ms, out 80ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(4px→0)` | Travel removed; fade at 150ms |
| Toast | in 250ms, out 150ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(8px→0)` | Travel removed; fade at 150ms, auto-dismiss unchanged |
| List enter | 250ms per item, `{motion.stagger-step}` 40ms between | `{motion.ease-enter}` | `opacity`, `translateY(8px→0)` | Stagger and travel removed; group fades once at 150ms |
| List exit | 150ms, no stagger | `{motion.ease-exit}` | `opacity`, `translateY(-4px)` | Travel removed; fade at 150ms |
| Loading | `{motion.duration-emphasis}` 500ms per rotation, infinite while pending | linear / `{motion.ease-standard}` | `transform: rotate()`, `opacity` | Rotation and sweep stop; static labelled indicator remains |

Values are the Calm block from SPEC section 5, verbatim, with no deviation. Every exit is shorter than its entrance. Only `transform` and `opacity` are transitioned. The loader is the only infinite animation; there is no brand ambience. One brand-specific rule was added beyond the profile: a displayed balance, price or percentage never moves or scales — on an exchange, a number that bounces reads as a number still changing.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, `find_role_strongest` call site (line ~181, the `for role in ("border", "focus", "text-dim")` loop) | The representative token for `border`, `focus` and `text-dim` is chosen as the **highest-contrast** match. A file that owns both a failing hairline and a passing strong border therefore reports the passing one from `check()`, and the failure surfaces only via `check_all`. It happens to be caught here, but a role with a single pattern match and no `check_all` counterpart would hide it. | Keep `find_role_strongest` for reporting the representative, but run the threshold `check()` against the *weakest* match as well, or drop `check()` for these three roles since `check_all` already covers every tone. |
| `theme-audit/audit.py`, `focus_tokens` (line ~245) | A ring named `focus-on-dark` is skipped entirely when the palette has no dark surface token (`if not targets: continue`). A file can therefore satisfy the `focus` role with a ring that is never measured against anything. | Treat a theme-scoped ring with no matching surface as an unresolved finding rather than a silent skip, so the file is forced to either tokenise the dark surface or drop the ring. |
| `theme-audit/audit.py`, the new rgba-compositing block (added mid-run by another agent, ~line 155) | The composite is fed into the `SEMANTIC` check, which measures tokens as *text on the canvas*. An opacity fill named `success-subtle` is therefore reported as a 1.2:1 text failure although it is a background by definition. Every file in the repo with a `*-subtle` opacity ladder will now carry a synthetic failure it can only answer with prose. | Exclude keys whose name marks them as a fill (`-subtle`, `-bg`, `-fill`, `-wash`) from the semantic-as-text check, or measure a composited fill only as a background for the ink the components block puts on it. |
| `theme-audit/audit.py`, `disclosed()` (line ~330) | Disclosure matches on the foreground token name appearing anywhere on a line that also states the ratio. `success` is a substring of `success-text`, so a line about the passing token could accidentally disclose the failing one if it happened to state a matching ratio. | Require a word boundary around the token name, or match on the hex only. |
| `SPEC.md`, section 3 (line 121–128) | The ten legacy files are told to convert their headings, but the spec never says what to do with a legacy section that has no slot in the contract — this file's `## 9. Agent Prompt Guide`. I kept it as an unnumbered extra section; another agent may delete it or fold it into `Iteration Guide`, and the ten conversions will diverge. | Add one line: legacy sections outside the contract are kept verbatim under an unnumbered heading, placed after `Responsive Behavior`. |

### Needs approval

Three extracted Kraken values fail WCAG and were **not** changed. Each is recorded with its nearest passing value and the usage note that would make the real value defensible.

1. **`text-secondary` #9497a9 — 2.89:1 on #ffffff, needs 4.5:1.**
   - Nearest passing for body text: **#737684** (4.51:1).
   - Nearest passing for the 3:1 large-text threshold: **#9194a6** (3.00:1) — a change of 3 steps in each channel.
   - Defensible usage note, if the hex is frozen: *none exists.* This is the important finding. At 2.89:1 the tone does not clear 3:1, so there is no size, weight or role at which it becomes compliant — unlike a typical muted grey that survives as an 18px+ label. Either the hex changes or the tone is decorative.
2. **`border-subtle` #dedee5 — 1.34:1 on #ffffff, needs 3.0:1.**
   - Nearest passing: **#939397** (3.06:1).
   - Defensible usage note: decorative dividers and section rules only, never the sole boundary of a control. This note is already true of the file as written — the one documented control boundary is the `#5741d8` outlined-button border at 6.66:1 — so no parallel accessible token was added. If inputs or selectable rows are ever documented for Kraken, a prescribed `border-strong` will be needed at that point.
3. **`success` #149e61 — 3.45:1 on #ffffff as text, needs 4.5:1.**
   - Nearest passing: **#118652** (4.61:1).
   - Defensible usage note: fill-only, at 16% opacity, with `success-text` #026b3f (6.61:1 on canvas, 5.49:1 on the composited fill) carrying every label. At 18.66px/700 or 24px it clears the 3:1 large-text threshold. This note is true of the file as written.

Also for approval: the **focus ring is prescribed, not extracted** (`focus` #101114, `focus-inner` #ffffff). It is the brand's own ink rather than a brand purple, because every purple in the palette fails against the purple button fill (`#5b1ecf` on `#7132f5` = 1.37:1). A reviewer who wants a chromatic ring will have to accept either a ring that disappears on the primary CTA or a purple outside Kraken's stated scale, which the file's own Don'ts forbid.

### Identity verdict

The file still reads as Kraken, and more so than before. The conversion kept the original prose almost sentence for sentence — the atmosphere paragraph, the key-characteristics list, the colour role names ("Kraken Purple", "Silver Blue", "Border Gray"), the full type table including the 7px micro oddity, the two-line don'ts — and added token references around them rather than rewriting them. The things that are specifically Kraken survived the token block: a single commanding purple with three near-identical dark variants, one white that is both canvas and card, shadows at 3% alpha, a 12px button ceiling stated as a rule, and one green doing all of positive/success.

**Calm is the correct profile and I kept it.** The evidence is in the file's own words: "clean, trustworthy", a plain white canvas with no gradient or mesh, shadows the file itself calls "whisper-level", and a palette of one hue plus one semantic green. It is not a developer tool (no terminal or IDE language anywhere), not luxury or hardware (no photography, no reveal), and not illustration-led or saturated-multi-colour — a single purple at three luminances is the opposite of the Playful test. SPEC's assignment rules fall through to rule 4. The one brand-specific motion rule I added, that a displayed balance or price never moves or scales, is a Calm reading of a financial-exchange identity rather than a deviation from the profile's values, which are used verbatim.

The risk in this conversion was the opposite direction: a 15-token colour block, a generic 10-row motion table and a generic state matrix could have buried a short, opinionated file. The mitigation was to keep every measured ratio attached to the Kraken token that produces it, and to put the generic machinery (the motion table, the reduced-motion block) in sections that did not exist before rather than over the top of the original prose.

### Note for the nine remaining legacy conversions

This was the first. What the prose did and did not give up, and the pattern that followed from it, is in the reply to the orchestrator.
