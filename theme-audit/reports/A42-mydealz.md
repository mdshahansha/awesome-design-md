## A42 · mydealz

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

- **Before:** 4 · 5 · 1 · 1 · 1 · 1
- **After:** 5 · 5 · 5 · 5 · 5 · 5

Both runs are on the harness build present at 16:37 (`audit.py` mtime 16:36, commit `317c766`). My first run used an earlier build and additionally reported `warning-surface on canvas` at 1.01:1 as a "semantic tone as text" failure; the newer build exempts fill tones whose name contains `surface`, which is the correct call. Eight undisclosed contrast failures under the old build, seven under the new.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Nothing to reference. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section. Five frozen-value AA failures and three component failures were entirely undisclosed. |
| P0 | A · Tokens | `colors` | No `focus` role. Nothing in the file said what a focus ring looks like, on a site whose every control is a 540px pill. |
| P0 | B · Colour | `button-primary` | White label on `#30a83c` measures 3.09:1 at 14px/700, against 4.5:1. The site's most-used control is below AA and the file did not say so. |
| P0 | B · Colour | `button-outline-green` | The same green as a label on white, 3.09:1 against 4.5:1 — while the file already documents `green-strong` (5.18:1) as the answer for green text on light surfaces. |
| P0 | B · Colour | `muted` | 2.16:1 on canvas / 2.36:1 on surface, documented as "the quietest captions and placeholder text" — i.e. prescribed for a job it cannot do. |
| P0 | H · States | `## Components` | Only `active` was documented anywhere structured, and that in an illustrative `ex-*` entry. Seven of eight states absent, including every state of the signature `temperature-control`. |
| P1 | C · Colour | `hairline` | 1.2:1 on canvas / 1.31:1 on surface, against 3:1, while being named as the border of `text-input`, `search-pill` and `country-selector` — controls whose edge is their only definition. |
| P1 | B · Colour | `price-lockup` | Green price on canvas is 2.83:1, missing even the 3:1 large-text threshold its 24px/700 type earns. On `surface`, where prices actually sit, the same pair reaches 3.09:1 and passes. |
| P1 | Section contract | Responsive | Carried as `### Responsive Strategy` inside Layout, not as a top-level section. |
| P1 | Section contract | Known Gaps | Absent, so the prescribed-versus-extracted line was nowhere stated. |
| P1 | A · Tokens | `shadow` | Elevation levels 2 and 3 state real `rgba(...)` values in prose with no token to reference them by. |
| P1 | E · Shapes | focus ring | No ring geometry anywhere: no width, no offset, no per-control radius. |
| P2 | B · Colour | `warm` | Rising-orange is 3.1:1 on surface and 2.84:1 on canvas — fine for a large numeral, not for the 14px/700 `{typography.ui}` the badges use. Undisclosed. |
| P2 | D · Typography | `micro` | 10px/700 is below any practical reading floor; the file gives it no minimum-use note. Recorded, not changed — it is an extracted value. |
| P2 | Prose/token drift | `text-input` | Prose says "navy-translucent border" while the frontmatter entry declared no border at all. Now both say `{colors.hairline-strong}`. |
| P2 | C · Elevation | levels 0-3 | Mixing border and shadow is *not* random here — border at rest, shadow on lift — but the rule was only implied. Left as prose, now reinforced by the hover row in the motion table. |

Typography (D) otherwise passes: every one of the nine roles carries family, size, weight, line height and letter spacing, and body at 16px/500/1.5 in `ink` reads at 19.21:1 on canvas and 21:1 on surface. The radius and spacing ladders (E) are internally consistent; `rounded.full: 540px` and `rounded.circle: 9999px` are both "fully round" but they are extracted and the file explains the split by use.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| `colors:` | added `focus: "#197e25"` | Required role, absent. Takes the brand's own deep green so the ring is brand-derived, not invented; role-named because it is a 2px offset ring, never a fill. |
| `colors:` | added `hairline-strong: "#8a8d91"` | Parallel accessible boundary per SPEC §2. 3.05:1 on canvas, 3.33:1 on surface. Labelled prescribed. The extracted `hairline` is untouched and rescoped to decoration. |
| frontmatter | added `shadow: {soft, deep}` | The two `rgba(...)` values already written in Elevation & Depth, now referenceable. Extracted, not invented. |
| frontmatter | added `motion:` with the **Playful** block verbatim from SPEC §5 | Required group. No value deviates. |
| `text-input`, `email-input`, `search-pill`, `country-selector` | `borderColor` -> `{colors.hairline-strong}`, added `focusRing: {colors.focus}` | These four are controls whose boundary is their only definition. Cards, nav and footer keep the extracted `hairline`, where the canvas gutter does the separating. |
| Colors · Surface | `hairline` entry rewritten; `hairline-strong` and `focus` entries added | States the 1.2:1 / 1.31:1 measurement and scopes the real tone to decoration rather than leaving it as an unqualified border. |
| Colors · Text | `muted` entry rewritten | Was prescribed for captions at 2.16:1. Now scoped to redundant ink (struck price, placeholder in a labelled field), with `{colors.body}` named as the readable alternative. |
| Elevation & Depth table | levels 2-3 now cite `{shadow.soft}` / `{shadow.deep}` alongside their literal values | Removes the token-less value SPEC §1 calls out. Literals kept so nothing extracted is lost. |
| Shapes | new `### Focus Ring` subsection | Width, offset, per-control radius, and why the ring is drawn outside the control. Marked prescribed. |
| Components | new `### State Coverage` table, 17 rows covering every entry | States were the weakest dimension. Entries that genuinely have one state say so (`price-lockup`, the five status badges, `timestamp-pill`). |
| after Components | new `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. Principles, 10-row interaction table, reduced-motion block. |
| after Motion | new `## Accessibility` | 13 passing pairs measured, 7 failures disclosed with ratios, focus-ring visibility per surface, tap-target prescription, reduced-motion summary. |
| Layout | `### Responsive Strategy` and its four `####` children **moved out** | Promoted one level to `## Responsive Behavior`, placed after Do's and Don'ts. Content verbatim; not duplicated. |
| end of file | new `## Known Gaps`, 10 entries | Separates prescribed from extracted: motion, focus ring, `hairline-strong`, tap targets, state styling, dark mode, button heights. |
| Do's and Don'ts | 3 Don'ts appended | Keeps the new rules where a reader of this file actually looks. |

Nothing else was reflowed. The description, Overview, type scale, spacing, grid, Shapes ladder and every existing component entry are byte-identical.

### Contrast checks

All computed with WCAG 2.1 relative luminance, `python3` standard library.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #000000 on `canvas` #f3f5f7 | 19.21:1 | 4.5:1 | Pass |
| `ink` on `surface` #ffffff | 21.0:1 | 4.5:1 | Pass |
| `body` #6b6d70 on `canvas` | 4.75:1 | 4.5:1 | Pass |
| `body` on `surface` | 5.19:1 | 4.5:1 | Pass |
| `muted` #a7a9ac on `canvas` | 2.16:1 | 4.5:1 | **Fail** — frozen, disclosed, rescoped |
| `muted` on `surface` | 2.36:1 | 4.5:1 | **Fail** — frozen, disclosed, rescoped |
| `hairline` #dfe1e4 on `canvas` | 1.2:1 | 3.0:1 | **Fail** — frozen, disclosed, decoration-only |
| `hairline` on `surface` | 1.31:1 | 3.0:1 | **Fail** — frozen, disclosed, decoration-only |
| `hairline-strong` #8a8d91 on `canvas` | 3.05:1 | 3.0:1 | Pass (prescribed) |
| `hairline-strong` on `surface` | 3.33:1 | 3.0:1 | Pass (prescribed) |
| `on-primary` #ffffff on `primary` #30a83c | 3.09:1 | 4.5:1 | **Fail** — brand identity, disclosed |
| `primary` on `surface` (`button-outline-green` label) | 3.09:1 | 4.5:1 | **Fail** — brand identity, disclosed |
| `primary` on `canvas` (`price-lockup`, 24px/700) | 2.83:1 | 3.0:1 | **Fail** — brand identity, disclosed |
| `primary` on `surface` (`price-lockup` in a card, 24px/700) | 3.09:1 | 3.0:1 | Pass |
| `green-strong` #197e25 on `surface` | 5.18:1 | 4.5:1 | Pass |
| `green-strong` on `canvas` | 4.74:1 | 4.5:1 | Pass |
| `green-strong` on `discount-surface` #defde4 | 4.76:1 | 4.5:1 | Pass |
| `warning-text` #9f5c0c on `warning-surface` #faf9ca | 4.85:1 | 4.5:1 | Pass |
| `warning-surface` on `canvas` (pill edge, not text) | 1.01:1 | n/a as text | Edgeless — noted, border prescribed when isolated |
| `hot` #ce1736 on `surface` | 5.53:1 | 4.5:1 | Pass |
| `hot` on `canvas` | 5.06:1 | 4.5:1 | Pass |
| `cold` #034eb1 on `surface` | 7.7:1 | 4.5:1 | Pass |
| `cold` on `canvas` | 7.04:1 | 4.5:1 | Pass |
| `premium` #7457dd on `surface` | 5.06:1 | 4.5:1 | Pass |
| `premium` on `canvas` | 4.63:1 | 4.5:1 | Pass |
| `warm` #fb6001 on `surface` | 3.1:1 | 4.5:1 | **Fail** at label size — disclosed with a size note |
| `warm` on `canvas` | 2.84:1 | 4.5:1 | **Fail** — disclosed |
| `focus` #197e25 on `canvas` | 4.74:1 | 3.0:1 | Pass |
| `focus` on `surface` | 5.18:1 | 3.0:1 | Pass |
| `focus` on `ink` #000000 (`ex-pricing-tier-featured` fill) | 4.05:1 | 3.0:1 | Pass |

One ring clears 3:1 on all three grounds this file defines, so `focus` is defined and `focus-on-dark` is not — the SPEC's "one mid-luminance ring" case rather than the light/dark pair. The ring is drawn 2px outside the control with a 2px offset, so it is measured against the surface behind the control, not the control's fill; a green ring measured against the green `button-primary` fill would be 1.68:1 and arithmetically unfixable without abandoning the brand colour.

### Motion inventory

Prescribed, **Playful** profile, verbatim token values. Nothing measured from the live site.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `opacity`; `translateY(-1px)` on `deal-card` | Travel removed; opacity/colour only at 130ms |
| Press | `{motion.duration-instant}` 70ms | `{motion.ease-standard}`, release via `{motion.ease-enter}` | `scale(0.97)`; vote arrow releases to `scale(1.06)` and settles | Scale removed; state change instant |
| Focus | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` on the ring | Ring appears instantly, never animated away |
| Page / route | `{motion.duration-base}` 200ms | `{motion.ease-standard}` | `opacity` on the feed column | Cross-fade at 130ms, no transform |
| Modal / drawer | 200ms in, 130ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(16px)` in, `translateY(8px)` out | Opacity only at 130ms; sheet appears in place |
| Dropdown | 130ms in, 70ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scale(0.98 -> 1)` from the top edge | Opacity only at 130ms |
| Toast | 200ms in, 130ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(12px)` | Opacity only at 130ms; auto-dismiss unchanged |
| List enter | 200ms, stagger `{motion.stagger-step}` 60ms, capped at 5 | `{motion.ease-enter}` | `opacity` + `translateY(8px)` | Stagger and travel removed; batch fades together at 130ms |
| List exit | 130ms | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | Opacity only at 130ms |
| Loading | `{motion.duration-emphasis}` 450ms loop | `{motion.ease-standard}`, alternating | `opacity` 0.6 ↔ 1 on skeleton; `rotate()` on spinner | Frozen to a static frame; `aria-busy` remains |

Every exit is shorter than its entrance. Only `transform` and `opacity` animate. The sole infinite animations are the skeleton pulse and the vote spinner; there is no brand ambience to freeze, because the palette is flat and the frog mascot is a static illustration.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` (~line 241, `check_all("border", ...)`) | The `border` role resolves to whichever key matches the pattern first. Adding the accessible `hairline-strong` made the harness report `"border": "hairline-strong"`, so the *representative* border is now the prescribed tone while the extracted `hairline` is only caught by `check_all`. The headline role resolution now names the token the brand does not use. | Resolve the representative role to the first-declared matching key, or report all matching keys for a role rather than one. |
| `theme-audit/audit.py` (~line 462, states haystack) | `states_documented` is a substring test, so `active` is satisfied by the word "Active" inside an `ex-app-shell-row` *description* — an illustrative kit-mirror surface, not a brand component. The states dimension can be partly satisfied by prose about non-brand examples. | Exclude `ex-*` entries from the states haystack, or require the state word on a line that also names a non-`ex-` component. |
| `theme-audit/audit.py` (~line 496, motion score) | Scoring is binary on section presence + the three minimum keys + a `prefers-reduced-motion` match anywhere in the file. A file can score 5 with a motion section whose durations contradict its own `motion:` block, and `has_reduced_motion` is satisfied by the string appearing in a Known Gaps line saying reduced motion is undocumented. | Require the reduced-motion match to fall inside the Motion & Animation section, and check that durations in the prose are token references or members of the declared block. |
| `theme-audit/audit.py` (~line 393, `disclosed()`) | Disclosure matches on the foreground's name appearing anywhere on a line that states the right ratio. `muted` is a substring of `button-muted`, `hairline` of `hairline-strong`, so a line about one token can discharge another's failure by accident. | Match the token in backticks or as a word boundary, and require the pair's background to be named on the same line. |
| `theme-audit/SPEC.md` §1 vs §2 | §1 forbids adding a token to satisfy a pattern; §2 requires adding a parallel accessible token next to a failing frozen one. `hairline-strong` is the second, but it also changes which key satisfies the `border` role, so a legitimate §2 token looks like a §1 violation in the output. | State in §1 that a parallel accessible token added under §2 is not a pattern-satisfying alias, and fix the role resolution above so adding one does not move the role. |
| `theme-audit/audit.py` (noted, already correct) | The `warning-surface on canvas` "semantic tone as text" failure present in the pre-16:36 build is gone in `317c766`: `FILL_MARKER` now exempts names containing `surface`. Correct behaviour — recording it only because my before-scores straddle the two builds. | None. |

No change proposed to `README.md` or `CONTRIBUTING.md`; nothing in this audit traced to either.

### Needs approval

Three brand-identity hexes fail AA. None was changed; each is disclosed in the file with its measured ratio.

1. **`button-primary` — white on `primary` #30a83c, 3.09:1 vs 4.5:1.** Nearest passing value: **`#197e25`** (`green-strong`, already in the palette) at 5.18:1, visually a deeper version of the same green. Usage note that would make the real value defensible: the 14px/700 label would need to rise to 18.66px/700 or 24px for the 3:1 large-text threshold to apply, which conflicts with the pill's `0px 14px` padding and the feed's density. Recommendation: darken the fill to `green-strong` for the CTA only, leaving `primary` as the price and link colour. Needs brand approval — this is the most visible green on the site.
2. **`button-outline-green` — `primary` label on white, 3.09:1 vs 4.5:1.** Nearest passing value: **`#197e25`** at 5.18:1. The file *already* documents `green-strong` as "a darker green for green text on light surfaces … where the fill green would be too light", so this is the brand contradicting its own stated rule. Lowest-risk fix in the set.
3. **`price-lockup` — `primary` on `canvas`, 2.83:1 vs the 3:1 large-text threshold.** Nearest passing value: **`#197e25`** at 4.74:1. Usage note that makes the real value defensible: at 24px/700 the requirement is 3:1, and inside a card on `surface` the same pair reaches 3.09:1 and passes — so the price is compliant where it is actually rendered and fails only if a price is set directly on the page floor. Recommendation: keep `primary` for prices and forbid the price lockup on bare `canvas`.

Also for approval, lower stakes:

4. **`hairline-strong` #8a8d91 is a new prescribed colour**, not a brand tone. It is the only new chromatic value I introduced and it only appears on four control boundaries. If the brand would rather accept the AA failure than add a grey, remove the token and the file's disclosure still stands.
5. **`focus` #197e25 reuses `green-strong`'s hex under a new role name.** If a repo-wide convention prefers aliasing (`focus: "{colors.green-strong}"`), this should change everywhere at once rather than in one file.
6. **`warm` #fb6001 at 3.1:1 / 2.84:1.** Disclosed with a size restriction (24px+ numerals or icon-plus-text only) rather than changed, since it is a status colour on a small footprint. Nearest passing value for 14px label use would be around `#b84600`, which loses the orange's brightness and with it the point of the token.

### Identity verdict

Still mydealz. Everything that makes the file specific survived: the temperature control as the brand's defining component, cold-blue down / hot-red up, the green that owns every price and every action, mint discount pills, the 540px pill signature against 8px cards, Averta CY at exactly two weights, the rationed whitespace of an information product, and the frog mascot in Decorative Depth. The additions lean on those facts rather than around them — the State Coverage table's richest row is the `temperature-control` (eight states, including a rejected vote that reverts with a `{colors.hot}` flash), the press animation is specified around a vote feeling like it lands, and the focus ring is the brand's own deep green rather than a default blue.

**The assigned Playful profile is correct**, and I kept it. SPEC §5 rule 3 asks for saturated colour *on interactive elements* plus an informal type voice, and both hold here in a way they do not for most bright-palette files: the hot/cold arrows are controls, the green pills are controls, the saturated tones are not static card backgrounds behind screenshots. The voice is a cartoon frog and a crowd-voted "temperature", not an editorial one. Rule 1 does not fire (no luxury or hardware identity, no full-bleed photography — the file says outright there is no hero photography), and rule 2 does not fire (not a developer tool). The one argument for Calm is density: a feed of hundreds of cards cannot afford choreography. I answered that inside the profile rather than by switching it — Playful's 200ms base is already quick, the stagger is capped at five steps, and the overshoot curve is spent only on the vote, which is the one interaction that carries meaning. A file about a crowd-vote thermometer is not Calm.

The `ex-*` block is the one part that reads as borrowed. Those ten entries are a kit-mirror template shared across the collection — a pricing tier, a cart drawer, a data table — and none corresponds to anything on mydealz. The file labels them illustrative, so this is honest rather than wrong, but they are the only passage that would sit unchanged in any other file in the repo, and `ex-pricing-tier-featured`'s "dark fill … in dark mode" description promises a dark mode this file does not define. Flagged in Known Gaps; not removed, since the block is a repo-wide convention and out of a single file's scope.
