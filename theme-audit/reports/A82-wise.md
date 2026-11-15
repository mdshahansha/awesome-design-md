## A82 · wise

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 4 | 5 | 1 | 1 | 1 | 1 |
| after | 5 | 5 | 5 | 5 | 5 | 5 |

Every figure the brief supplied was reproduced from the file's own hexes with
`python3` and WCAG 2.1 relative luminance; none was estimated. Two items in the
brief no longer appear in the current harness output — see Shared issues.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, F | frontmatter | No `motion:` group at all; no motion section, no reduced-motion rule. The whole dimension was absent. |
| P0 | A, G | frontmatter / Accessibility | No `focus` role and no focus ring anywhere in the file, on either polarity. The file documents three dark grounds (`card-feature-dark`, `hero-band-dark`, `footer`) plus a maroon badge ground, so one ring could not have served it. |
| P0 | B, H | `badge-negative` | `textColor` bound to `{colors.on-primary}` `#0e0f0c` on `{colors.negative-bg}` `#320707` — 1.07:1. **Binding error, not a brand failure:** the prose for the same component says "text white". The auto-derived block guessed the label by token name. |
| P0 | B, H | `ex-pricing-tier-featured` | `textColor` bound to `{colors.on-primary}` on a `{colors.ink}` fill — the identical hex, 1.00:1. **Binding error:** the entry's own description says "dark fill + light text". Same auto-derived cause. |
| P1 | C, G | `ex-cart-drawer.item-divider`, `ex-data-table-cell.rowBorder` | Both bound to `{colors.canvas-soft}`, which measures 1.2:1 against the `{colors.canvas}` card it divides. An invisible divider between line items and table rows. Escapes the harness because it is not declared as `borderColor` (Shared issues #2). |
| P1 | C | Elevation & Depth | The brand's stated elevation cue — white card on sage band — measures 1.2:1, and `{colors.primary-pale}` on canvas 1.14:1. Well under the 3:1 a meaningful non-text boundary needs. Real, undisclosed, and now stated. |
| P1 | B | `{colors.mute}` | 3.64:1 on canvas, 3.03:1 on `{colors.canvas-soft}`, 3.19:1 on `{colors.primary-pale}`. Documented as "captions, placeholder, fine print" — exactly the normal-size text use that fails. Frozen extracted value; disclosed with a size caveat. |
| P1 | B | `{colors.warning}`, `{colors.positive}`, `{colors.warning-deep}` | 1.46:1, 2.92:1 and 4.22:1 on canvas. Frozen; disclosed with fill-only / large-text scoping. |
| P1 | B | `{colors.accent-orange}`, `{colors.accent-cyan}` | 1.59:1 and 1.93:1 on canvas. Not flagged by the harness (not semantic-named), but they are real tones with no usage ceiling stated. Now scoped to decoration explicitly. |
| P1 | H | every component | Only `active` was documented anywhere structured. hover, focus-visible, pressed, disabled, loading, selected and error were named nowhere in the file. |
| P1 | Sections | document | Motion & Animation, Accessibility, Responsive Behavior and Known Gaps all absent. Responsive content existed only as `### Responsive Strategy` inside Layout. |
| P2 | A, G | `ex-modal-card`, `ex-toast` | Both describe themselves as having an "elevated shadow" / "medium shadow" while the file defines no shadow value and no `shadow:` group. Dangling prose, not a dangling token reference. Recorded in Known Gaps rather than invented. |
| P2 | G | Responsive Behavior → Touch Targets | "WCAG AAA at all widths" is a rendering claim no document can support, and the token arithmetic puts `button-icon-circular` at 40 px, under 44 px. Kept verbatim per SPEC section 3 and flagged in Known Gaps. |
| P2 | A | `{colors.primary-neutral}`, `{colors.negative-deep}`, `{colors.positive}` | Documented with a purpose but bound by no component, so their grounds are assumed rather than declared. Recorded in Known Gaps. |
| P2 | D, E | typography / radius | Every type role carries size, weight and line height. `{typography.display-lg}` is the one oddity — weight 400 at 47 px with a 70.5 px line height, 1.5×, against 0.85× for its weight-900 neighbours — but it is labelled "lighter sub-display", so it is a deliberate seam, not a stray value. Radius ladder 0/8/12/16/24/9999 is clean; `pill` and `full` are the same value under two names, which the file justifies by use. No value sits outside its scale. |

**Border role — the flagged "possibly wrongly-satisfied" role: not a harness bug.**
`border` resolves to `ink` from a real binding, and the prose asserts it: Level 1
elevation is "1 px solid `{colors.ink}` border" on tertiary outline buttons and
form inputs, and `button-tertiary`, `text-input` and `currency-converter-card`
all declare `borderColor: {colors.ink}`. It measures 19.23:1 on canvas against a
3:1 requirement. This brand genuinely has no hairline grey — its boundary is its
ink — so nothing was invented and nothing is misnamed. What the single role name
*does* hide is the weaker divider tone, and that is a harness blind spot rather
than a resolution error (Shared issues #2). No alias token was added.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#163300"` | The ring for every light surface. `#163300` is the hex the palette already owns as `{colors.ink-deep}`; per SPEC section 1 this is a real role binding, not an alias. 13.93:1 on canvas. |
| frontmatter `colors:` | — -> `focus-on-dark: "#9fe870"` | The file documents four dark grounds. `{colors.focus}` measures 1.38:1 on `{colors.ink}`, so one ring cannot serve both polarities. `#9fe870` is the brand's own `{colors.primary}`; 13.05:1 on ink. |
| frontmatter | — -> `motion:` group | SPEC section 5 **Calm** block, verbatim, no deviations. |
| `badge-negative.textColor` | `{colors.on-primary}` -> `{colors.canvas-soft}` | Fixes the 1.07:1 binding error. `{colors.canvas-soft}` is the brand's established near-white text-on-dark token (the `footer` uses it on the same ink), and measures 14.93:1 on `{colors.negative-bg}`. Pure `{colors.canvas}` white would measure 17.96:1 and is arguably what the prose means — see Needs approval, and Shared issues #1 for why binding it was not viable. |
| `ex-pricing-tier-featured.textColor` | `{colors.on-primary}` -> `{colors.primary}` | Fixes the 1.00:1 binding error. Matches `card-feature-dark`, the brand's own dark-surface pattern: Wise green on ink, 13.05:1. |
| `ex-cart-drawer.item-divider` | `{colors.canvas-soft}` -> `{colors.mute}` | SPEC section 2 step 1: the palette already owns a tone that clears the 3:1 boundary threshold, so re-scope rather than add. 3.64:1 on canvas against the 1.2:1 it replaced. Permitted here because this block is explicitly auto-derived and marked for resolution in the judgement pass, not extracted. |
| `ex-data-table-cell.rowBorder` | `{colors.canvas-soft}` -> `{colors.mute}` | Same, on a table row rule. |
| Layout | `### Responsive Strategy` block removed | Moved, not duplicated, per SPEC section 3. |
| after Do's and Don'ts | — -> `## Responsive Behavior` | Same content verbatim, child headings promoted `####` -> `###`. |
| after Components | — -> `## Motion & Animation` | First line states the system is prescribed and was not measured. Full 10-row interaction table, the five profile rules, and a `@media (prefers-reduced-motion: reduce)` block. |
| after Motion & Animation | — -> `## Accessibility` | 14 passing pairs, 8 disclosed failures with measured ratios, both focus rings with their per-surface ratios and stated 2 px offset, token-derived tap targets, reduced-motion summary. |
| end of document | — -> `## Known Gaps` | 8 entries: motion prescribed, ring prescribed, no shadow tokens behind two shadow claims, the unsupportable AAA tap-target claim, non-computables, unbound tones, substitute font stack, no dark theme. |
| Components, 16 entries | — -> `- States:` line each | hover, focus-visible, pressed, disabled, loading, selected, error. Badges, bands and `nav-bar` say plainly that they have one or two states and why. |
| `badge-negative`, `ex-pricing-tier-featured` prose | — -> note on the corrected label token | So the fix is visible to a reader, not only in the frontmatter. |

No brand identity hex was altered, no token was added to satisfy a regex, and no
section the audit was not fixing was reflowed.

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #0e0f0c / `canvas` #ffffff | 19.23:1 | 4.5:1 | Pass |
| `ink` / `canvas-soft` #e8ebe6 | 15.98:1 | 4.5:1 | Pass |
| `ink` / `primary-pale` #e2f6d5 | 16.82:1 | 4.5:1 | Pass |
| `on-primary` #0e0f0c / `primary` #9fe870 | 13.05:1 | 4.5:1 | Pass |
| `body` #454745 / `canvas` | 9.37:1 | 4.5:1 | Pass |
| `body` / `canvas-soft` | 7.79:1 | 4.5:1 | Pass |
| `body` / `primary-pale` | 8.20:1 | 4.5:1 | Pass |
| `primary` / `ink` | 13.05:1 | 4.5:1 | Pass |
| `canvas-soft` / `ink` | 15.98:1 | 4.5:1 | Pass |
| `canvas-soft` / `negative-bg` #320707 | 14.93:1 | 4.5:1 | Pass (after fix; was `on-primary` at 1.07:1) |
| `primary` / `ink` (`ex-pricing-tier-featured`) | 13.05:1 | 4.5:1 | Pass (after fix; was 1.00:1) |
| `positive-deep` #054d28 / `primary-pale` | 8.76:1 | 4.5:1 | Pass |
| `positive-deep` / `canvas` | 10.01:1 | 4.5:1 | Pass |
| `warning-content` #4a3b1c / `warning` #ffd11a | 7.44:1 | 4.5:1 | Pass |
| `negative` #d03238 / `canvas` | 5.01:1 | 4.5:1 | Pass |
| `negative-deep` #a72027 / `canvas` | 7.29:1 | 4.5:1 | Pass |
| `negative-darkest` #a7000d / `canvas` | 7.93:1 | 4.5:1 | Pass |
| `ink` border / `canvas` | 19.23:1 | 3.0:1 | Pass |
| `ink` border / `primary` | 13.05:1 | 3.0:1 | Pass |
| `mute` #868685 / `canvas` | 3.64:1 | 4.5:1 | **Fail** — disclosed, frozen |
| `mute` / `primary-pale` | 3.19:1 | 4.5:1 | **Fail** — disclosed, frozen |
| `mute` / `canvas-soft` | 3.03:1 | 4.5:1 | **Fail** — disclosed, frozen |
| `positive` #2ead4b / `canvas` | 2.92:1 | 4.5:1 | **Fail** — disclosed, fill-only |
| `warning-deep` #b86700 / `canvas` | 4.22:1 | 4.5:1 | **Fail** — disclosed, large-text only |
| `warning` #ffd11a / `canvas` | 1.46:1 | 4.5:1 | **Fail** — disclosed, fill-only |
| `accent-orange` #ffc091 / `canvas` | 1.59:1 | 4.5:1 | **Fail** — disclosed, decoration only |
| `accent-cyan` #38c8ff / `canvas` | 1.93:1 | 4.5:1 | **Fail** — disclosed, decoration only |
| `mute` divider / `canvas` | 3.64:1 | 3.0:1 | Pass (after fix; `canvas-soft` was 1.2:1) |
| `mute` divider / `canvas-soft` | 3.03:1 | 3.0:1 | Pass (after fix) |
| **Layers** `canvas-soft` / `canvas` | 1.20:1 | 3.0:1 if meaningful | **Fail** — disclosed; the brand's elevation cue is below threshold |
| **Layers** `primary-pale` / `canvas` | 1.14:1 | 3.0:1 if meaningful | **Fail** — disclosed |
| `focus` #163300 / `canvas` | 13.93:1 | 3.0:1 | Pass |
| `focus` / `canvas-soft` | 11.58:1 | 3.0:1 | Pass |
| `focus` / `primary-pale` | 12.19:1 | 3.0:1 | Pass |
| `focus` / `primary` | 9.45:1 | 3.0:1 | Pass |
| `focus` / `ink` | 1.38:1 | 3.0:1 | **Fail** — which is why the second ring exists |
| `focus-on-dark` #9fe870 / `ink` | 13.05:1 | 3.0:1 | Pass |
| `focus-on-dark` / `negative-bg` | 12.19:1 | 3.0:1 | Pass |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `background-color`, `color` — paint only | Unchanged; the colour swap is the whole state |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `background-color` + `transform: scale(0.98)` | Scale removed, colour kept at 80ms |
| Focus | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | ring `opacity`, drawn full-width from frame 1 | Instant, no fade |
| Page / route | 250ms in, 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | Travel removed, `opacity` at `{motion.duration-reduced}` |
| Modal / drawer | 250ms in, 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(12px)` or `translateX(100%)`; scrim `opacity` | Travel removed, both fade at 150ms |
| Dropdown / currency selector | 150ms in, 80ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(-4px)` | Travel removed, `opacity` at 150ms |
| Toast | 250ms in, 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(12px)` | Travel removed, `opacity` at 150ms |
| List enter | 250ms/item, `{motion.stagger-step}` 40ms, capped at 6 | `{motion.ease-enter}` | `opacity` + `translateY(8px)` | Stagger and travel removed, one fade at 150ms |
| List exit | 150ms, no stagger | `{motion.ease-exit}` | `opacity` + `translateY(-4px)` | Travel removed, `opacity` at 150ms |
| Loading | 800ms/rotation infinite; skeleton pulse at `{motion.duration-emphasis}` 500ms | linear / — | `transform: rotate()`; skeleton `opacity` 0.4↔1 | Both frozen; static `{colors.mute}` block with `aria-busy="true"` |

Every exit is shorter than its entrance. Only `transform` and `opacity` are
animated; paint-only changes are used where the brand's real state change is a
colour swap, as SPEC section 6 permits. The spinner and skeleton pulse are the
only infinite animations and only while a request is pending; the brand has no
ambience. No profile value was deviated from, and no extracted timing existed
to displace one.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 400–421 (`bound_polarity` / `theme_of`) | **This one silently zeroes the contrast dimension.** A token bound as a `textColor` on a dark ground in a light-canvas file is inferred to belong to a dark *theme*, and `same_theme` then skips every check that uses it. Binding `{colors.canvas}` as `badge-negative`'s label — the honest reading of that component's prose — flipped `canvas` to theme "dark" and silenced *all four* real failures plus every other canvas-grounded check, reporting `contrast_failures: []` and scoring a **false 5**. I confirmed this by running the harness in that state. It is already true today for `{colors.canvas-soft}` (bound as footer text on ink) and `{colors.primary}` (bound as `card-feature-dark` text), which is why `text on surface` and `text-dim on surface` are never measured in this file and why the brief's `mute on primary-pale` 3.19:1 no longer appears. I worked around it only by choosing a different (still correct) token, which is not a fix. Suggested fix: infer a theme from a textColor binding only when the token is **not** also bound as a `backgroundColor` or used on grounds of the file's own canvas polarity, and require a dual-theme *canvas* set, not merely a dark surface in a light file — the comment at line 370 already states this intent. A single dark card must not make the page's white a dark-theme colour. |
| `theme-audit/audit.py` line 481 | The bound-boundary scan reads only `("borderColor", "border", "outlineColor")`. Divider tones declared under any other property name are never measured, so `{colors.canvas-soft}` at 1.2:1 served as this file's table-row rule and drawer item divider invisibly to the audit. | Extend the tuple with `divider`, `dividerColor`, `item-divider`, `rowBorder`, `separator`, `ruleColor`. |
| `theme-audit/briefs/A82-wise.md` (and presumably all 84) | The brief lists `border` as a missing colour role and `mute on primary-pale` 3.19:1 as a measured failure. Neither appears in the current harness output: `border` resolves from bindings, and the `primary-pale` pair is suppressed by issue #1. The briefs were generated against an older `audit.py`. | Regenerate briefs from the current harness, or stamp each brief with the `audit.py` revision it was generated from so agents can tell drift from error. |
| `scripts/derive-examples-block.mjs` (referenced by the file; outside my scope) | It derives `textColor` by token name, which produced `{colors.on-primary}` on an `{colors.ink}` fill (1.00:1) and on `{colors.negative-bg}` (1.07:1) — two of the three worst ratios in this file came from the generator, not the brand. It also emits "elevated shadow" / "medium shadow" descriptions for files that define no shadow token. | Derive `textColor` from the measured polarity of the chosen `backgroundColor`, not from the token's name; and emit a shadow description only where the file defines a `shadow:` group. |
| `theme-audit/SPEC.md` section 3 | The contract requires a top-level `## Responsive Behavior`, but a file carrying the content as `### Responsive Strategy` has no instruction on whether to rename the heading when moving it "verbatim". I renamed it, since the harness matches on the contract name. | State that the heading text is normalised to the contract name while the body moves verbatim. |

### Needs approval

1. **`badge-negative` label token.** The prose says "text white"; the frontmatter said `{colors.on-primary}` (near-black, 1.07:1). I bound it to `{colors.canvas-soft}` `#e8ebe6`, the brand's own near-white text-on-dark token, at 14.93:1. If the real badge label is pure `#ffffff` (17.96:1), the binding should be `{colors.canvas}` — but that binding triggers Shared issues #1 and silences the whole contrast dimension, so it needs the harness fix first. A brand owner should confirm which white it is.
2. **`{colors.mute}` `#868685` at 3.64:1 on white.** Nearest passing value: **`#757575`** (4.61:1). Usage note that makes the real value defensible: *`{colors.mute}` is for labels at 18.66 px+, or 14 px+ at weight 600, where the 3:1 large-text threshold applies; captions at `{typography.caption}` 12 px and placeholder text must use `{colors.body}` `#454745` (9.37:1).* Today the file assigns it exactly the opposite job.
3. **`{colors.warning-deep}` `#b86700` at 4.22:1.** Nearest passing: **`#b06200`** (4.57:1) — a change invisible to the eye. Usage note if the hex is frozen: *large text only (18.66 px+ / 14 px bold+), 3:1 applies.*
4. **`{colors.positive}` `#2ead4b` at 2.92:1.** Nearest passing: **`#24883b`** (4.51:1). Usage note: *fill and icon only; success wording uses `{colors.positive-deep}` `#054d28` at 10.01:1.*
5. **`{colors.warning}` `#ffd11a` at 1.46:1.** Nearest passing on white would be **`#8c720e`** (4.64:1), which is no longer the brand's yellow — do not apply it. Usage note: *fill only, never text, at any size; labels on it are `{colors.warning-content}` at 7.44:1.*
6. **Layer separation at 1.2:1.** Whether the white-card-on-sage boundary is decorative (current reading, disclosed) or load-bearing. If load-bearing, it needs the Level 1 `{colors.ink}` hairline, which changes the brand's look. Owner's call.
7. **Re-binding the `{colors.canvas-soft}` divider.** I re-scoped the two auto-derived divider bindings to `{colors.mute}`. Those entries are generated and explicitly marked for resolution, so I treated them as fair game — but if any of them reflects a real observed Wise rule, SPEC section 2 step 3 says the extracted binding stands and only the prose should be re-scoped. Confirm.
8. **`button-icon-circular` at 40 px.** Token arithmetic puts it under the 44 px minimum. Fixing it means `{spacing.md}` padding or an expanded hit area; either is a brand-visible change. Flagged, not made.

### Identity verdict

The file still reads as Wise, and more so than before. Everything added is drawn
from tokens the file already owned: the focus ring is the existing
`{colors.ink-deep}` forest green on light surfaces and the brand's own lime
`{colors.primary}` on dark ones, so no new brand colour entered the palette; the
corrected dark-surface label is Wise green on ink, which is the pattern
`card-feature-dark` and `hero-band-dark` already establish; the states table
uses `{colors.primary-active}` and `{colors.primary-neutral}` for hover and
press, which the Colors section had already described as the lighter and
mid-saturation greens for active state but which no component had used. The
hover and press rows are paint-only because on a brand whose single accent sits
on neutral grounds, the colour swap *is* the state — inventing a scale pop would
have contradicted the Don'ts list.

**Calm is the right profile; it stays.** Rule 1 does not fire (money transfer,
not luxury or hardware). Rule 2 does not fire. Rule 3 is a conjunction and
fails on both halves: the palette is single-accent by explicit rule ("Don't
introduce a second brand accent. Wise green is the sole identity colour"), the
saturated tones that exist are illustration accents inside card artwork rather
than colour on interactive elements, and the type voice is a weight-900
geometric display held still at 126 px with negative letter-spacing — editorial,
not light and informal. The file's own Overview says the brand "reads more like
a calm Scandinavian magazine than a bank", and its elevation is surface
contrast rather than shadow. That is SPEC section 5's Calm signature almost
word for word: short opacity-led fades, little travel. Rule 4 is the terminal
answer and it is correct here.

The one drift risk is the auto-derived `ex-*` block, which is generic by
construction and contributed both 1:1 contrast failures. I corrected its two
broken bindings and left its structure alone, since it is shared scaffolding
across the collection rather than this file's own voice.
