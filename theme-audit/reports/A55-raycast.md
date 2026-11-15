## A55 · raycast

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Zero durations and zero easings in the file. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Six boundary-contrast failures sat entirely undisclosed, including the one that matters most: the only focus affordance in the system is a 1.56:1 border. |
| P0 | A Token contract | `colors.focus` | No focus role. Confirmed missing. Nothing in the file was addressable as a ring. |
| P0 | B Colour | `colors.hairline` / `-soft` / `-strong` | All three hairlines fail 3:1 on both canvas and surface: 1.33 / 1.29, 1.17 / 1.19, 1.52 / 1.56. `{colors.hairline-strong}` is the entire focus indicator on `{component.text-input-focused}`, so focus is effectively invisible. Extracted and frozen; not corrected in place. |
| P1 | H States | Components | Five of eight states never documented: hover, focus-visible, loading, selected, error. The file's "no hover states documented per system policy" note described the capture limit as a policy, which left the matrix looking deliberate rather than incomplete. |
| P1 | B Colour | `colors.stone` #434345 | Documented as "least-emphasis caption text" but measures 2.03:1 on canvas against a 4.5:1 requirement. Unusable for any caption meant to be read. Not flagged by the harness (not a role representative). |
| P1 | C Elevation | surface ladder | The four-step ladder spans only 1.07:1 end to end (1.03 / 1.03 / 1.01 between adjacent steps). Not a WCAG failure, but the file presented the ladder as the system's whole depth mechanism without saying it is barely perceptible, and the hairline that actually does the separating is at 1.33:1. |
| P2 | B Colour | `colors.ash` #6a6b6c | 3.75:1 on canvas. Defensible for its documented disabled-text use (WCAG exempts disabled), but the file never said so. |
| P2 | B Colour | `colors.hero-stripe-end` #a1131a | 2.50:1 on canvas. Pure decoration with no text or meaning, so 3:1 does not apply — recorded for completeness. |
| P2 | C Elevation | Elevation & Depth | Elevation *is* expressed one consistent way (background colour plus hairline, never shadow), and the absence of a `shadow:` group is correct since no shadow value is documented — but neither fact was stated. |
| P2 | D Typography | typography group | Clean: all 15 roles carry family, size, weight, line height and letter spacing, and body-md at 16px/1.6 measures 12.6:1 to 18.2:1 on every surface the file defines. No change needed. |
| P2 | E Shapes | `rounded` ladder | Clean: 0 / 4 / 6 / 8 / 10 / 16 / 9999, no value outside its own scale, and every component's `rounded` binding resolves to a rung. No change needed. |
| P2 | — Harness/brief | brief line 12 | The brief lists `text-dim` as a missing role. The current harness resolves `text-dim` -> `mute` (#9c9c9d, 7.30:1 on canvas), and the palette plainly owns the role. The brief is stale, not the harness; no token was invented. See Shared issues. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#ffffff"` | Role binding onto a hex the palette already owns (`primary` / `on-dark`). A chromatic ring would break the file's own "no saturated accent on chrome" rule and gain nothing: white measures 17.6:1 to 20.0:1 on every surface here. Not an alias — it carries a distinct job on a distinct surface. |
| frontmatter `colors:` | — -> `hairline-accessible: "#646869"` | Parallel accessible token per SPEC §2. The frozen hairlines keep every binding they were extracted with; this one exists for implementers who need a control edge that reads. Chosen as the lowest value in the brand's cool-grey family clearing 3:1 on all five surfaces the file defines, including `button-fg` (3.12:1). |
| frontmatter | — -> `motion:` group | Crisp profile block, verbatim from SPEC §4. |
| Colors / Surface | hairline bullets -> same bullets plus measured ratios, "extracted and frozen", "decorative only" scoping | Scopes the frozen tones in prose instead of changing their hexes. Adds the two new tokens with their measured ratios and their prescribed labels. |
| Elevation & Depth | closing paragraph -> plus one paragraph of measured ladder steps | The ladder's 1.01–1.07:1 steps are the real reason a Raycast card reads flat; the file claimed depth without quantifying it. |
| Components | "No hover states documented per system policy" -> "No hover states were **extracted** per the original capture policy", pointing at the new table | The gap was a capture limit, not a design decision. Saying so is the honest framing. |
| Components | — -> `### Component States` table | Every component entry now names its states, each marked extracted or prescribed, with "n/a" where a component genuinely has none. Non-interactive display elements (`keycap`, `badge-*`, `app-icon-tile*`) and containers are grouped and declared single-state. |
| after Components | — -> `## Motion & Animation` | First line states the system is prescribed and was not measured from the live site. Ten-row inventory, all ten motion tokens referenced, transform/opacity only, exits shorter than entrances, plus the `@media (prefers-reduced-motion: reduce)` rule. |
| after Motion | — -> `## Accessibility` | 18 text ratios, 19 boundary/ring ratios, a plain statement of the four real brand failures, the focus-ring treatment and offset, tap targets marked as documented-not-measured, reduced motion. |
| Do's and Don'ts | 8 Dos / 7 Don'ts -> 11 Dos / 12 Don'ts | Four new rules for the ring, the accessible hairline and Crisp motion; five new prohibitions covering hairline-as-focus, layout-property animation, chromatic rings and `stone` as caption text. |
| Known Gaps | 6 items -> 10 items | Prescribed motion, prescribed ring, prescribed hairline, hover-not-extracted, and tap targets documented rather than measured. |

Section order after the edits is Overview · Colors · Typography · Layout · Elevation & Depth · Shapes · Components · **Motion & Animation** · **Accessibility** · Do's and Don'ts · Responsive Behavior · Iteration Guide · Known Gaps — the SPEC §3 order. Responsive Behavior was already top-level; nothing was moved or reflowed.

### Contrast checks

All computed from this file's token values with WCAG 2.1 relative luminance; translucent tokens composited over the stated background first. None estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #f4f4f6 on `canvas` #07080a | 18.24:1 | 4.5:1 | Pass |
| `ink` on `surface` #0d0d0d | 17.69:1 | 4.5:1 | Pass |
| `ink` on `surface-elevated` #101111 | 17.22:1 | 4.5:1 | Pass |
| `ink` on `surface-card` #121212 | 17.05:1 | 4.5:1 | Pass |
| `body` #cdcdcd on `canvas` | 12.60:1 | 4.5:1 | Pass |
| `body` on `surface` | 12.23:1 | 4.5:1 | Pass |
| `charcoal` #d3d3d4 on `canvas` | 13.39:1 | 4.5:1 | Pass |
| `mute` (text-dim) #9c9c9d on `canvas` | 7.30:1 | 4.5:1 | Pass |
| `mute` on `surface-elevated` | 6.90:1 | 4.5:1 | Pass |
| `on-dark` #ffffff on `canvas` | 20.04:1 | 4.5:1 | Pass |
| `on-dark-mute` composited on `canvas` (-> #bababa) | 10.32:1 | 4.5:1 | Pass |
| `on-primary` #000000 on `primary` #ffffff | 21.00:1 | 4.5:1 | Pass |
| `on-primary` on `primary-pressed` #e8e8e8 | 17.14:1 | 4.5:1 | Pass |
| `accent-blue` #57c1ff on `canvas` | 10.00:1 | 4.5:1 | Pass |
| `accent-red` #ff6161 on `canvas` | 6.81:1 | 4.5:1 | Pass |
| `accent-green` #59d499 on `canvas` | 10.78:1 | 4.5:1 | Pass |
| `accent-yellow` #ffc533 on `canvas` | 12.68:1 | 4.5:1 | Pass |
| `accent-blue` on `accent-blue-soft` over canvas (-> #13242f) | 7.93:1 | 4.5:1 | Pass |
| `ash` #6a6b6c on `canvas` | 3.75:1 | 4.5:1 | **Fail** (disabled-text use only; WCAG exempt there) |
| `stone` #434345 on `canvas` | 2.03:1 | 4.5:1 | **Fail** (documented as caption text — not exempt) |
| `hairline` #242728 on `canvas` | 1.33:1 | 3.0:1 | **Fail** (frozen) |
| `hairline` on `surface` | 1.29:1 | 3.0:1 | **Fail** (frozen) |
| `hairline-soft` composited on `canvas` (-> #1b1c1e) | 1.17:1 | 3.0:1 | **Fail** (frozen) |
| `hairline-soft` composited on `surface` (-> #202020) | 1.19:1 | 3.0:1 | **Fail** (frozen) |
| `hairline-strong` composited on `canvas` (-> #2f3031) | 1.52:1 | 3.0:1 | **Fail** (frozen) |
| `hairline-strong` composited on `surface` (-> #343434) | 1.56:1 | 3.0:1 | **Fail** (frozen; this is the whole focus indicator) |
| `hairline-accessible` #646869 on `canvas` | 3.55:1 | 3.0:1 | Pass |
| `hairline-accessible` on `surface` | 3.45:1 | 3.0:1 | Pass |
| `hairline-accessible` on `surface-elevated` | 3.36:1 | 3.0:1 | Pass |
| `hairline-accessible` on `surface-card` | 3.32:1 | 3.0:1 | Pass |
| `hairline-accessible` on `button-fg` #18191a | 3.12:1 | 3.0:1 | Pass |
| `focus` #ffffff on `canvas` | 20.04:1 | 3.0:1 | Pass |
| `focus` on `surface` | 19.44:1 | 3.0:1 | Pass |
| `focus` on `surface-elevated` | 18.91:1 | 3.0:1 | Pass |
| `focus` on `surface-card` | 18.73:1 | 3.0:1 | Pass |
| `focus` on `button-fg` | 17.61:1 | 3.0:1 | Pass |
| `focus` on `hero-stripe-start` #ff5757 | 3.11:1 | 3.0:1 | Pass (lightest point of the hero gradient) |
| `focus` on `hero-stripe-end` #a1131a | 8.00:1 | 3.0:1 | Pass |
| `hero-stripe-end` on `canvas` | 2.50:1 | 3.0:1 | **Fail** — decoration, no text, 3:1 does not apply |

Surface-ladder adjacency, for the elevation finding: canvas→surface 1.03:1, surface→surface-elevated 1.03:1, surface-elevated→surface-card 1.01:1, canvas→surface-card 1.07:1, canvas→button-fg 1.14:1.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity`; surface-ladder fills swap untransitioned | Unchanged |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `transform: scale(0.98)` + `opacity` | Scale removed; opacity at `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on the ring; never travels | Unchanged |
| Page / route transition | 150ms in `{motion.duration-base}`, 100ms out `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` only | Unchanged |
| Modal / drawer (mobile nav) | 220ms in `{motion.duration-slow}`, 150ms out `{motion.duration-base}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateX` + scrim `opacity` | Travel removed; cross-fade at 100ms |
| Dropdown / menu | 100ms in `{motion.duration-fast}`, 60ms out `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(-4px)` | Travel removed; opacity only |
| Toast | 150ms in `{motion.duration-base}`, 100ms out `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px)` | Travel removed; opacity only |
| List enter | 100ms `{motion.duration-fast}` per item, `{motion.stagger-step}` 20ms offset | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px)` | Stagger and travel removed; one fade at 100ms |
| List exit | 60ms `{motion.duration-instant}`, no stagger | `{motion.ease-exit}` | `opacity` only | Unchanged |
| Loading | spinner 600ms = 2 × `{motion.duration-emphasis}` per revolution, infinite; skeleton pulse `{motion.duration-emphasis}` 300ms | `{motion.ease-standard}` | spinner `transform: rotate`; skeleton `opacity` 0.4↔1.0 | Rotation stops, static glyph; pulse freezes at full opacity; progress announced in text |

Rule compliance: transform and opacity only, every exit shorter than its entrance, nothing on first paint, one infinite animation (the loader) and no brand ambience — the hero stripe is a static gradient. One stated deviation: the spinner runs at 2 × `duration-emphasis` because a 60–300ms revolution strobes. `duration-reduced` is 100ms, under the 150ms ceiling.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `design-md/raycast/DESIGN.md` line 4 (frontmatter key) | The summary key is `属于:` — a Chinese word ("belongs to") where every other file presumably carries an English key such as `summary:`. The harness never reads it, so it costs nothing today, but it is a corrupted key name in a document meant to be machine-read. Not touched, because renaming a frontmatter key is a schema change across 84 files, not a raycast fix. | Agree one key name repo-wide (`summary:`) and rename in a single mechanical pass, after confirming nothing downstream reads `属于`. |
| `theme-audit/briefs/A55-raycast.md` line 12 | "Missing colour roles: focus, **text-dim**" is wrong for the current harness, which resolves `text-dim` -> `mute`. Per the settled rule I did not add an alias to satisfy the pattern; the role was already satisfied. Briefs appear to have been generated against an earlier harness. | Regenerate the briefs from the current `audit.py`, or add the harness version to the brief header so a stale pre-measurement is visible as stale. |
| `theme-audit/audit.py` (contrast sweep) | `stone` #434345 at 2.03:1 as documented caption text is the file's second-worst real failure and the harness does not surface it: only the role *representative* of `text-dim` (`mute`) is checked against 4.5:1, so the other text tones in the palette are never measured as text. The equivalent sweep does happen for boundary tones ("all tones"). | Extend the text sweep the way the boundary sweep already works — measure every non-`disabled`-named tone documented under a text heading against 4.5:1, not just the role representative. |
| `theme-audit/audit.py` (role representative) | Adding `hairline-accessible` moved the `border` role representative from `hairline-strong` to the new token. Correct per SPEC §1 (every tone is still measured and all six failures are still reported, now as disclosed), but the reported representative silently changed as a side effect of adding a token. Worth a note in the JSON. | Emit `roles_resolved` with the full candidate list per role, not only the winner, so a representative change is visible in a diff of two runs. |

### Needs approval

1. **Re-binding `{component.text-input-focused}` to the focus ring.** Its extracted binding — border brightening to `{colors.hairline-strong}`, 1.56:1 composited on `{colors.surface}` — is left exactly as captured, because it is a fact about the real product. But as the system's only focus affordance it is a WCAG 2.4.7 / 2.4.11 failure. Proposal: re-point the focused input at a 2px `{colors.focus}` #ffffff ring with a 2px `{colors.surface}` offset (19.44:1). Nearest passing value if a border is preferred over a ring: `{colors.hairline-accessible}` #646869 at 3.45:1 on surface. Needs a brand owner, because it changes what the document says Raycast does.
2. **`{colors.hairline}` #242728 as a control boundary.** 1.33:1 on canvas, 1.29:1 on surface, against a 3:1 non-text minimum. Nearest passing value in the same cool-grey family: **#646869** (3.55:1 / 3.45:1) — i.e. `{colors.hairline-accessible}`. Usage note that makes the real value defensible: `{colors.hairline}` is acceptable wherever the edge is decorative — card separation, dividers, the nav and footer rules — because the content inside the card is independently perceivable. It is not acceptable as the sole boundary of a text input, search field or install pill, where the edge *is* the control. The file now says exactly this; a brand owner needs to confirm the split.
3. **`{colors.stone}` #434345 as caption text.** 2.03:1 on canvas against 4.5:1. Nearest passing value at the same hue: **#8b8b8d** (approximately 5.9:1 on canvas). Usage note that would make the real value defensible: restrict `{colors.stone}` to disabled icon fills only, which WCAG exempts, and move "least-emphasis caption text" to `{colors.mute}` (7.30:1), which the file already owns. Note that even the 18px/3:1 large-text concession does not rescue 2.03:1, so unlike most muted-grey cases there is no size at which the extracted value passes. The alternative is to state that Raycast's lowest caption tier fails AA and leave it.
4. **`{colors.ash}` #6a6b6c at 3.75:1.** No change proposed. It is documented as disabled-state text, which carries no WCAG contrast requirement, and the file now says so. Flagged only so the decision is explicit rather than silent: if `{colors.ash}` is ever used for enabled text, it fails.
5. **The focus ring itself is a brand decision.** `{colors.focus}` reuses white rather than introducing a new hex, and an offset-outside ring is a visible change to Raycast's chrome. If the brand would rather keep the inset-border idiom, option 1's `{colors.hairline-accessible}` border is the fallback that still clears 3:1.

### Identity verdict

Still unmistakably Raycast. The additions are all in the brand's own vocabulary and none of them introduce a colour the palette did not already own: the ring is the same white that is already the system's single interactive signal, which is the one choice that respects both "white IS the brand action" and "never saturated accent on chrome" at the same time. The one genuinely new hex, `{colors.hairline-accessible}` #646869, sits in the existing cool-grey family beside `{colors.ash}` and is labelled prescribed rather than presented as extracted.

The Crisp assignment is right and I kept it. Rule 2 of SPEC §5 fires squarely: Raycast is a developer-tool and launcher identity, and uniquely among the collection its marketing chrome *is* its product chrome — a keyboard-driven command palette. The motion section is written around that rather than around generic token names: surface-ladder fill changes swap with no transition at all, press is 60ms, there is no entrance choreography, and the only infinite animation is the install spinner, because the system has no ambience to animate. A reader who removed the brand name would still place this file: ss03 Inter, keycap glyphs, the one-band stripe rule, the four-step near-black ladder, white pills.

The honest cost of the audit is that the file is now considerably more candid about itself. Its headline accessibility fact — that a Raycast text field's focus state is a 1.56:1 border and effectively invisible — was previously absent, and it is more useful to anyone building on the document than any of the ratios that pass.
