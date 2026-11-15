## A65 · slack

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 2 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

`audit.py` was updated mid-review (commit `dd934af`, dim-tone ordering and surface preference), which changed two role resolutions for this file. Both columns above are measured with the **current** harness: the before column by running it against `HEAD:design-md/slack/DESIGN.md` in a scratch tree, the after column against the edited file. Under the older harness the pre-edit contrast score read 3 rather than 1, because `text-dim` then resolved to the wrong token and fewer grounds were measured.

Totals: 3 P0 · 7 P1 · 3 P2.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A. Token contract | `colors.focus` | No focus role of any kind. The file documents a light system *and* aubergine signature surfaces, so keyboard users had no indicator on either polarity. Level 4 of Elevation & Depth named "button focus" for a 1px **inset** aubergine ring, which cannot be judged against the surface behind the control and is not a conforming indicator. |
| P0 | B. Colour | `colors.hairline` on `text-input` | `#e6e6e6` on `#ffffff` = **1.25:1** against a 3:1 requirement, and the hairline is the field's *only* edge. A real, undisclosed AA failure on the one interactive control the file documents. Extracted, so frozen. |
| P0 | B. Colour | `colors.primary-tint` on `colors.primary` | `#592466` on `#4a154b` = **1.25:1** for a token the prose calls a "border accent on aubergine-on-aubergine surfaces". The harness never saw it (see Shared issues), so it was failing silently. |
| P1 | F. Motion | frontmatter + sections | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule, zero durations and zero easing curves in the whole file. |
| P1 | G. Accessibility | sections | No `## Accessibility` section, so every contrast failure in the file was undisclosed by construction. |
| P1 | Section contract | sections | No `## Known Gaps`, so the prescribed-vs-extracted boundary was nowhere stated. |
| P1 | H. States | all 16 component entries | Only `hover` and `pressed` appeared anywhere structured. `focus-visible`, `active`, `disabled`, `loading`, `selected` and `error` were absent from every entry, including `text-input`, which needs `error` to be usable at all. |
| P1 | A. Token contract | `colors.hairline-strong` | `#000000` sits in the token block with **no prose binding, no source page and no mention anywhere in the document**, yet it takes the `border` role from the real extracted hairline. Pure black is an implausible hairline for this brand; origin unverified. |
| P1 | C. Elevation | `## Elevation & Depth` | Four `rgba(...)`/`rgb(...)` shadow values written in prose with no `shadow:` group to reference, which SPEC section 1 requires exactly where a file documents real shadow values. Depth is also expressed two ways at once — three box-shadows plus an inset ring, against a Decorative Depth note saying the brand's real depth language is the gradient and uses no literal lift. |
| P1 | C. Elevation | level 4 use note | "button focus" as a use for an inset ring conflicts with the focus system now defined; left in place as extracted but explicitly rejected in prose. |
| P2 | B. Colour | `colors.on-aubergine-mute` on light grounds | 1.71:1 on `canvas` and 1.54:1 on `canvas-lavender` — **manufactured** pairs. The token names its own ground: it is drawn only on aubergine (8.19:1 there) and the file never places it on a light surface. The real light-ground muted ink is `ink-mute` at 5.49:1, which passes, and the current harness now resolves `text-dim` to it correctly; these two ratios survive only because `check_all` sweeps every `^on-[a-z]+-mute` token across the light grounds. Disclosed as manufactured. |
| P2 | Identity | pastel-mesh gradient | The mesh stops are inline, hedged hexes (`#fff0e6`-ish peach, `#e9d8ff` lavender) and the dusty green has no value at all. Nothing binds them, so no contrast claim is possible for the hero headline that sits over them. Recorded in Known Gaps; not invented. |
| P2 | Identity | brand name | The `name` field and the Overview had the brand misspelled with zero occurrences of the real name (corrected before this review). Rechecked the whole body: all three remaining occurrences now read "Slack", and no other brand reference is mangled. "Salesforce Avant Garde" / "Salesforce Sans" are spelled correctly and are plausible for a Salesforce-owned brand, but unverifiable from the document — noted in Known Gaps rather than altered. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#1264a3"`, `focus-on-dark: "#d9bdde"` | Two polarities, no single tone clears 3:1 on both. Both hexes are ones the palette already owns (`link-blue`, `on-aubergine-mute`), so these are role bindings, not new brand colours or regex aliases. |
| frontmatter | — -> `motion:` group, Playful block verbatim | SPEC section 4; profile per roster. |
| frontmatter | — -> `shadow:` group with the four extracted elevation values | SPEC section 1 requires it where prose documents real shadows; values copied verbatim, nothing invented. |
| `## Colors` → Hairline | plain description -> same plus "1.25:1 on canvas, treat as decoration" | SPEC section 2 step 1/3: scope the frozen tone to decoration, do not re-point it. |
| `## Colors` → new Hairline Strong entry | undocumented token -> documented as the accessible boundary tone, 21:1, origin unverified | The palette already owned a passing tone, so step 1 applied and nothing new was added. |
| `## Colors` → Aubergine Tint | plain description -> same plus measured 1.25:1 and a re-scope to decoration | Frozen boundary tone failing its stated job. |
| `## Colors` → new `### Focus` subsection | — -> both rings with measured ratios and which surface each serves | SPEC section 1 asks the file to say which existing tone a ring reuses. |
| `## Elevation & Depth` table | raw shadow values -> same values referenced as `{shadow.elev-*}`, level 4's "button focus" reading rejected in place | Makes depth addressable; stops an inset ring being read as the focus indicator. |
| `## Components`, all 16 entries | 2 states -> every entry names its states, with genuinely-non-interactive entries (`card-stat`, `pill-cap-shade`) saying so | SPEC section 7. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and not measured. 11-row table covering hover, press, focus, page transition, modal/drawer enter and exit, dropdown, toast, list enter, list exit, loading; `transform`/`opacity` only; exit shorter than entrance everywhere; `@media (prefers-reduced-motion: reduce)` block naming what is removed and what remains at 130ms. |
| after Motion | — -> `## Accessibility` | 13 passing pairs, the three failures with measured ratios, per-surface ring coverage, tap-target arithmetic, reduced-motion. |
| end of file | — -> `## Known Gaps` | Nine entries separating prescribed from extracted. |
| `## Motion & Animation` prose | — -> note that the mesh gradient does not animate | The Overview says the gradients "pulse"; that is optical, and no ambient motion is documented. Stated so nobody implements an infinite animation from a figure of speech. |

Section order now matches SPEC section 3 exactly: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Motion & Animation, Accessibility, Do's and Don'ts, Responsive Behavior, Iteration Guide, Known Gaps. Nothing outside the two owned paths was touched, and no existing prose was reflowed.

### Contrast checks

All computed with WCAG 2.1 relative luminance via `python3 -I`; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #1d1d1d / `canvas` #ffffff | 16.86:1 | 4.5 | Pass |
| `ink` / `canvas-cream` #f4ede4 | 14.51:1 | 4.5 | Pass |
| `ink` / `canvas-lavender` #f9f0ff | 15.20:1 | 4.5 | Pass |
| `ink-mute` #696969 / `canvas` | 5.49:1 | 4.5 | Pass |
| `ink-mute` / `canvas-cream` | 4.73:1 | 4.5 | Pass |
| `ink-mute` / `canvas-lavender` | 4.95:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary` #4a154b | 14.00:1 | 4.5 | Pass |
| `on-primary` / `primary-press` #611f69 | 11.00:1 | 4.5 | Pass |
| `on-primary` / `primary-deep` #481a54 | 13.54:1 | 4.5 | Pass |
| `on-primary` / `primary-tint` #592466 | 11.24:1 | 4.5 | Pass |
| `on-aubergine-mute` #d9bdde / `surface-aubergine` #4a154b | 8.19:1 | 4.5 | Pass |
| `link-blue` #1264a3 / `canvas` | 6.22:1 | 4.5 | Pass |
| `link-blue` / `canvas-cream` | 5.35:1 | 4.5 | Pass |
| `link-hover` #3860be / `canvas` | 5.86:1 | 4.5 | Pass |
| `semantic-error` #cc4117 / `canvas` | 4.84:1 | 4.5 | Pass |
| `semantic-success` #007a5a / `canvas` | 5.34:1 | 4.5 | Pass |
| `primary` / `canvas` (outline button label) | 14.00:1 | 4.5 | Pass |
| `hairline-strong` #000000 / `canvas` | 21.00:1 | 3.0 | Pass |
| `focus` #1264a3 / `canvas` | 6.22:1 | 3.0 | Pass |
| `focus` / `canvas-cream` | 5.35:1 | 3.0 | Pass |
| `focus` / `canvas-lavender` | 5.61:1 | 3.0 | Pass |
| `focus` / `surface-aubergine` | 2.25:1 | 3.0 | **Fail — ring scoped away from aubergine** |
| `focus-on-dark` #d9bdde / `surface-aubergine` | 8.19:1 | 3.0 | Pass |
| `focus-on-dark` / `primary-press` | 6.44:1 | 3.0 | Pass |
| `hairline` #e6e6e6 / `canvas` | 1.25:1 | 3.0 | **Fail — extracted, disclosed** |
| `hairline` / `canvas-cream` | 1.07:1 | 3.0 | **Fail — extracted, disclosed** |
| `primary-tint` / `primary` | 1.25:1 | 3.0 | **Fail — extracted, disclosed** |
| `hairline` / `canvas-lavender` | 1.13:1 | 3.0 | **Fail — extracted, disclosed** |
| `on-aubergine-mute` / `canvas` | 1.71:1 | 4.5 | **Fail — manufactured pair, disclosed as such** |
| `on-aubergine-mute` / `canvas-lavender` | 1.54:1 | 4.5 | **Fail — manufactured pair, disclosed as such** |

Harness after the edits: `contrast_unresolved: []`, `contrast_disclosed: 4`, `component_contrast_failures: []`, `dangling_refs: []`.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `opacity`, `transform: scale(1.02)` | Colour change only; no scale |
| Press | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.97)` | No scale; `primary-press` fill alone signals it |
| Focus | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` | Ring appears with no transition |
| Page / route transition | `{motion.duration-base}` 200ms | `{motion.ease-standard}` | `opacity` | Fade at 130ms; no travel |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `translateY(12px) → 0` | Fade at 130ms; no travel or overshoot |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `translateY(8px)` | Fade at 130ms |
| Dropdown | 130ms enter / 70ms exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `scale(0.98) → 1` | Fade at 130ms; no scale |
| Toast | 200ms enter / 130ms exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(16px) → 0` | Fade at 130ms; appears in place |
| List enter | `{motion.duration-base}`, stagger `{motion.stagger-step}` 60ms | `{motion.ease-enter}` | `opacity`, `translateY(16px) → 0` | All items fade together at 130ms; stagger removed |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `scale(0.98)` | Fade at 130ms; no scale |
| Loading | 900ms loop, infinite | linear / `{motion.ease-standard}` | `transform: rotate()`; `opacity` 0.6 → 1 | Rotation stops, static indicator; skeleton holds a flat fill |

One stated deviation from the Playful block: the loader's 900ms infinite loop, which the profile does not cover. Exit is shorter than its matching entrance in every row. No layout-triggering property is animated anywhere (`layout_animation_mentions: []`).

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 278-289 | **The `surface` role resolves wrongly for this file: `canvas-lavender`, a section band and secondary-button fill, instead of `surface-elev`, the raised card tone the file actually declares.** The preference block drops any candidate whose hex equals the canvas hex, and this brand legitimately renders white cards on a white page (`surface-elev` = `canvas` = `#ffffff`), so the file's real surface is excluded and the nearest tinted band wins. Everything then measured "on surface" is measured against a ground that carries no cards: `hairline on canvas-lavender` 1.13:1 and `on-aubergine-mute on canvas-lavender` 1.54:1 are both disclosed in the file as manufactured. It should pick `surface-elev` and report that the raised surface is tonally identical to the canvas — which is the real finding, and one the file states in prose. | Keep an explicit `surface*` token even when its hex equals the canvas: exclude canvas-equal candidates only when some other `surface*` token differs. A white-card-on-white-page system is common enough that dropping it silently mismeasures every boundary in the file. |
| `theme-audit/audit.py` line 35 (`check_all`, `^on-[a-z]+-mute`) | A token named `on-<ground>-mute` states the ground it is drawn on, yet `check_all("text-dim", "canvas"/"surface", 4.5)` sweeps it across the light grounds anyway, manufacturing two failures here (1.71:1 and 1.54:1) that no rendered page can produce. This is separate from the `text-dim` representative, which commit `dd934af` now resolves correctly to `ink-mute`. | Skip `on-<x>-*` tokens in the light-ground sweep when a colour key matching `^<x>` or `^surface-<x>` exists, and measure them against that ground instead — the same evidence-from-the-name rule the border-from-bindings block already applies. |
| `theme-audit/audit.py` lines ~417-443 | Boundary tokens are measured against `canvas`, `surface`, and the grounds of any theme the name markers detect — but `surface-aubergine` carries no light/dark marker, so the aubergine grounds are never used for the `border` check. `primary-tint` at 1.25:1 on `primary`, the one boundary the prose explicitly places on aubergine, was invisible. The focus-coverage block already does the right thing: it harvests grounds from component `backgroundColor` bindings. | Harvest border grounds the same way the focus block does — any colour a CONTAINER-ish component binds as `backgroundColor` is a ground a boundary can be drawn on. |
| `theme-audit/audit.py` | SPEC section 1 requires a `shadow:` group wherever prose documents real shadow values, and the harness never looks at `shadow` at all. 84 files can carry raw `rgba(...)` values with no token and score 5 on tokens. | Add a shadow-group check gated on an `rgba(`/`box-shadow` match inside `## Elevation & Depth`. |
| `theme-audit/briefs/A65-slack.md` lines 11-12 | "Missing colour roles: focus, text-dim" — `text-dim` was never missing: the file owns `ink-mute` at 5.49:1, and the current harness resolves it. Line 12's single contrast failure ("hairline on surface-elev … 1.25:1") is also stale: the current harness reports four, against different grounds. Trusting the brief would have meant inventing a muted token the file already owns. | Regenerate the briefs from the current `audit.py` before the next wave; the brief predates two role-resolution fixes. |

### Needs approval

1. **Re-binding the extracted hairline.** `text-input` and `card-pricing` document a `1px {colors.hairline}` border at **1.25:1** on white. The extracted bindings are left exactly as found, per SPEC section 2 step 3, and the prose now scopes the hairline to decoration. A brand owner must decide whether the real `text-input` border moves to `{colors.hairline-strong}` (`#000000`, 21:1). If pure black is too heavy, the nearest passing neutral that clears 3:1 on **all three** light grounds is **`#898989`** (3.50:1 on `#ffffff`, 3.01:1 on `#f4ede4`, 3.15:1 on `#f9f0ff`); `#949494` clears white at 3.03:1 but fails cream at 2.61:1. Usage note that would make the extracted value defensible: the 1.25:1 hairline is acceptable only as a decorative card seam where grouping is already carried by padding and grid, never as the sole boundary of a control.
2. **The origin of `{colors.hairline-strong}` `#000000`.** It has no prose binding, no attributed source page and no mention in the document, yet it holds the `border` role. Either confirm it as extracted, or replace it with a prescribed `#898989` and label it as such. I did not remove it (removing a possibly-extracted value is worse than documenting it) and I did not add a parallel token, because the palette already owned a passing tone.
3. **The aubergine seam.** `{colors.primary-tint}` `#592466` on `#4a154b` is **1.25:1** for a stated border accent. The file now scopes it to decoration and points real boundaries on aubergine at `{colors.on-aubergine-mute}` (8.19:1). If a tinted seam must be perceivable in the brand's own hue, the nearest passing value on that ground is **`#ac52c2`** (3.16:1) — a visible departure from the extracted tint, which is why it needs a brand decision rather than an edit.
4. **The focus system is a prescription.** Both rings reuse palette hexes, but ring existence, 2px width and 2px offset (1px on `text-input`) are proposals. The brand owner should confirm, in particular, that the blue ring is never drawn on aubergine (2.25:1) and that the level-4 inset aubergine ring is not intended as the focus indicator, which is how its original use note read.

### Identity verdict

The file still reads as this brand and not as a token dump. Everything that carries the identity is untouched: the aubergine monotheism, the 90px over-padded pills, the negative display tracking, the pastel-mesh backdrop with the product mockup floating above and never inside it, the blue-link exception, the closing aubergine band. The additions are anchored in the brand's own vocabulary rather than borrowed — the two rings are the brand's link blue and its muted mauve, the loading skeleton is a cream block, the dropdown opens from the trigger edge of a pill, and I explicitly refused to turn the Overview's "pulse" into an ambient animation.

**Profile: Playful, kept as rostered.** The evidence is genuinely split and worth recording. For Playful: saturated aubergine sits on every interactive element rather than behind screenshots, the file already documents a distinct press colour (so a press state is part of the brand, not an invention), the pill geometry is deliberately soft and over-padded, and the mesh palette is multi-hue. Against it: the prose reaches for "editorial density", "editorial warmth" and body copy that "reads quietly", which is Calm vocabulary, and the brand has exactly one accent plus one link colour, which is the opposite of multi-colour. The tiebreak is SPEC section 5's own test — saturated colour *on interactive elements* and an informal voice — which the pills satisfy and the mesh does not need to. Playful's 200ms base and 60ms stagger also sit closer to a messaging product than Cinematic's 400-600ms would, and nothing in the file suggests a developer-tool Crisp identity. A switch to Calm would be defensible on the type voice alone; it is not clearly correct, so the roster value stands rather than being changed silently.
