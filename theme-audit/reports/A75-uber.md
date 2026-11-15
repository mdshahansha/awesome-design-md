## A75 · uber

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 5

One caveat on the contrast 5, stated up front because the number flatters the file: two of the three real failures (`mute` on the light grounds) are disclosed in `## Accessibility` with their measured ratios, which is what SPEC section 2 asks for — but they also stopped being *emitted* by the harness after I declared `link-mute-soft`'s ground, because the new `bound_polarity` inference then read `mute` as a dark-theme token. See Shared issues. The brand still fails AA at those points and the file says so plainly.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule. Nothing in the file said how a pill press, a drawer or a loader behaves. |
| P0 | A/G | `colors` | No focus role of any kind: a keyboard user had no indicator on any of the five surfaces this file defines, and the file could not even name one. |
| P0 | B | `link-on-dark` | Measured 1.00:1 — the component declared `textColor: on-dark` with no `backgroundColor`, so the harness substituted the page floor and measured white on white. The prose says "the white link inside dark bands"; the binding never said it. |
| P0 | B/G | `mute` `#afafaf` | Fails AA on every light ground the brand owns (2.19:1 canvas, 1.91:1 canvas-soft, 1.98:1 canvas-softer) and fails the 3:1 large-text allowance too, with no disclosure anywhere in the file. |
| P0 | G | sections | No `## Accessibility` section, so every failure above was undisclosed by construction. |
| P1 | B | `surface-pressed` `#e2e2e2` | Bound as a boundary tone in three illustrative entries (`ex-pricing-tier.borderColor`, `ex-cart-drawer.item-divider`, `ex-data-table-cell.rowBorder`) at 1.13:1 on its own ground — an invisible border. |
| P1 | B | `link-mute-soft` | Measured 2.19:1 for the same missing-ground reason; the prose says this link is used "on dark surfaces", where the same tone is 9.57:1. |
| P1 | A/C | `shadow` | The Elevation table documents three real `rgba(...)` values with no tokens to reference, which SPEC section 1 requires wherever prose states real shadow values. |
| P1 | Section contract | `## Responsive Behavior` | Present only as a Layout subsection titled "Responsive Strategy", not as a top-level peer. |
| P1 | Section contract | `## Known Gaps` | Absent: the file's unknowns (no disabled tone, no semantic palette, no extracted motion) were nowhere recorded. |
| P1 | H | Components | Only `active` appeared in a structured Components line. `hover`, `focus-visible`, `pressed`, `disabled`, `loading`, `selected`, `error` were named nowhere, although the palette already carried the extracted hover and pressed fills. |
| P1 | H | `colors` | No disabled tone exists in the palette, so disabled states had no expressible treatment. |
| P1 | H | `colors` | No error/success/warning tone — a genuine brand absence (the file states it), but it leaves error states with no colour channel. |
| P2 | Responsive | Touch Targets | "Both meet WCAG AAA at all breakpoints" is a rendering claim this audit cannot make; the figures are arithmetic from padding + line-height. |
| P2 | I | `ex-*` block | Descriptions are generic kit text ("re-purposed for SaaS / B2B verticals", "mono-caps eyebrow typography" — this file has no mono face). Reads as borrowed from the shared example kit. Left verbatim: not extracted content, and rewriting it is outside a reviewable diff. |
| P2 | E | `rounded` | `pill` 999px and `full` 9999px are the same rung by the file's own admission; the ladder carries a redundant value. Left as extracted. |
| P2 | D/Layout | `spacing` prose | Layout claims "a few 6-px sub-multiples (10, 14) inside button padding", but 10 and 14 are not tokens and `xs` 6px is the only off-4 value. The prose describes padding the token block does not contain. |
| P2 | D | `body-sm-strong`, `body-md-strong` | Line heights of 16px at 14px and 20px at 16px (1.14 / 1.25) sit below their non-strong siblings' 1.43 / 1.50. Plausible for single-line chip and button labels, but the file does not say they are single-line-only. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | *(no focus role)* -> `focus: "#000000"`, `focus-on-dark: "#ffffff"` | Two surface polarities (white canvas family, ink bands) cannot share one ring. Both hexes are already the brand's ink and paper, so this is a role binding, not a new colour and not an alias. |
| frontmatter | *(none)* -> `shadow:` group with `level-1/2/3` carrying the three extracted `rgba(...)` values verbatim | SPEC section 1: a file documenting real shadow values needs tokens for them. No new shadow invented. |
| frontmatter | *(none)* -> `motion:` group, Playful block from SPEC section 5, verbatim | Assigned profile; every value unchanged. |
| `components.link-on-dark` | no `backgroundColor` -> `backgroundColor: "{colors.ink}"` | Declares the ground the prose already asserts ("the white link inside dark bands"). 1.00:1 -> 21.0:1. |
| `components.link-mute-soft` | no `backgroundColor` -> `backgroundColor: "{colors.ink}"` | Same: the prose says "on dark surfaces". 2.19:1 -> 9.57:1. |
| `components.card-elevated`, `request-form-card`, `button-floating` | no shadow prop -> `shadow: "{shadow.level-1}" / "{shadow.level-2}" / "{shadow.level-3}"` | The prose already assigned each component its level; now it resolves to a token. |
| `components.ex-pricing-tier.borderColor`, `ex-cart-drawer.item-divider`, `ex-data-table-cell.rowBorder` | `{colors.surface-pressed}` -> `{colors.hairline-mid}` | SPEC section 2 step 1: the palette already owns a passing boundary tone (7.59:1 on canvas-soft), so re-scope rather than add. These three are auto-derived demonstration surfaces, not extracted site facts; **no extracted binding was re-pointed**, and `surface-pressed` keeps its pressed-fill job. |
| Colors -> Surface Pressed bullet | — -> states it is a fill tone, not a boundary tone, with both measured ratios | Scopes the frozen tone to decoration, per step 3. |
| Colors -> Mute bullet | — -> states the three measured failures, that 3:1 does not rescue it, and which tones to use instead | Step 4: say plainly that the real brand fails AA here. |
| Colors -> new `### Focus` subsection | — -> both rings, their geometry (2px ring, 2px opposite-polarity offset, two-tone over photography) and every measured ratio | Monochrome brand: SPEC section 1 says use the brand's own ink/paper with a mandatory offset rather than invent a chromatic ring. |
| Elevation table | bare `rgba(...)` -> `{shadow.level-N}` + the same literal value | Referenceable without losing the extracted string. |
| Components | — -> `### Component States` table, one row per component, naming states and their extracted-vs-prescribed status | SPEC section 7. Containers that genuinely have one or two states say so (`card-content`: default only; `nav-bar`: default + loading). |
| after Components | — -> `## Motion & Animation` | First line states the system is prescribed to match the visual identity and was not measured from the live site. 10-interaction table, the four motion rules, and the `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | — -> `## Accessibility` | Measured contrast for the key pairs, a separate table of the real AA failures, ring visibility per surface, tap targets (labelled as computed), reduced motion, and the colour-only-hover / no-semantic-palette notes. |
| Layout -> after Do's and Don'ts | `### Responsive Strategy` (Layout subsection) -> `## Responsive Behavior`, content verbatim, `####` children promoted to `###` | Section contract: moved, not duplicated. |
| end of file | — -> `## Known Gaps` | Records the prescribed-motion seam, the absent disabled and semantic tones, the mute failure, the three re-pointed illustrative bindings, the computed (not rendered) tap targets, and the borrowed `ex-*` prose. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#000000` / `canvas` `#ffffff` | 21.00:1 | 4.5 | Pass |
| `ink` / `canvas-soft` `#efefef` | 18.26:1 | 4.5 | Pass |
| `ink` / `canvas-softer` `#f3f3f3` | 18.93:1 | 4.5 | Pass |
| `ink` / `surface-pressed` `#e2e2e2` | 16.21:1 | 4.5 | Pass |
| `on-primary` `#ffffff` / `primary` `#000000` | 21.00:1 | 4.5 | Pass |
| `on-dark` `#ffffff` / `black-elevated` `#282828` | 14.74:1 | 4.5 | Pass |
| `body` `#5e5e5e` / `canvas` | 6.48:1 | 4.5 | Pass |
| `body` / `canvas-soft` | 5.64:1 | 4.5 | Pass |
| `hairline-mid` `#4b4b4b` / `canvas` | 8.72:1 | 3.0 | Pass |
| `hairline-mid` / `canvas-soft` | 7.59:1 | 3.0 | Pass |
| `link` `#0000ee` / `canvas` | 9.40:1 | 4.5 | Pass |
| `link` / `ink` | 2.23:1 | 4.5 | Fail — never used there; dark bands use `link-on-dark`. Noted in Accessibility. |
| `mute` `#afafaf` / `canvas` | 2.19:1 | 4.5 | **Fail** (extracted, disclosed) |
| `mute` / `canvas-soft` | 1.91:1 | 4.5 | **Fail** (extracted, disclosed) |
| `mute` / `canvas-softer` | 1.98:1 | 4.5 | **Fail** (extracted, disclosed) |
| `mute` / `ink` | 9.57:1 | 4.5 | Pass — the one ground where the brand uses it |
| `surface-pressed` / `canvas-soft` | 1.13:1 | 3.0 (as boundary) | **Fail as a boundary** — re-scoped to pressed fill, disclosed |
| `surface-pressed` / `canvas` | 1.30:1 | 3.0 (as boundary) | **Fail as a boundary** — same |
| `focus` `#000000` / `canvas` | 21.00:1 | 3.0 | Pass |
| `focus` / `canvas-soft` | 18.26:1 | 3.0 | Pass |
| `focus` / `canvas-softer` | 18.93:1 | 3.0 | Pass |
| `focus` / `surface-pressed` | 16.21:1 | 3.0 | Pass |
| `focus-on-dark` `#ffffff` / `ink` `#000000` | 21.00:1 | 3.0 | Pass |
| `focus-on-dark` / `black-elevated` | 14.74:1 | 3.0 | Pass |
| Candidate `mute` replacements: `#767676` / `canvas` | 4.54:1 | 4.5 | Pass (nearest passing) |
| `#6d6d6d` / `canvas-soft` | 4.50:1 | 4.5 | Pass (nearest passing) |
| `#949494` / `canvas` | 3.03:1 | 3.0 | Pass at 24px+ / 18.66px-bold only |

### Motion inventory

Prescribed, Playful profile, verbatim from SPEC section 5. Nothing was extracted from the live site, which the section's first line states.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `background-color` / `border-color` / `box-shadow` — paint only; on this near-monochrome brand the fill change *is* the hover | Fill change kept at `{motion.duration-reduced}`; no shadow lift |
| Press | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.98)` + fill to `{colors.surface-pressed}` | Scale removed; fill change only |
| Focus | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` on the 2px ring | Ring appears instantly; never suppressed |
| Page / route transition | enter 200ms `{motion.duration-base}` · exit 130ms `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | Travel removed; cross-fade at `{motion.duration-reduced}` |
| Modal / drawer | enter 200ms · exit 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scale(0.98)→1` (drawer `translateY(16px)`) | Opacity only at `{motion.duration-reduced}` |
| Dropdown | enter 130ms · exit 70ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scale(0.98)`, origin at trigger edge | Opacity only at `{motion.duration-reduced}` |
| Toast | enter 200ms · exit 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(12px)` | Travel removed; fade at `{motion.duration-reduced}` |
| List enter | 200ms per item, `{motion.stagger-step}` 60ms apart, capped at 6 | `{motion.ease-enter}` | `opacity` + `translateY(8px)` | Stagger and travel removed; items fade together at `{motion.duration-reduced}` |
| List exit | 130ms, no stagger | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | Scale removed; fade at `{motion.duration-reduced}` |
| Loading | spinner 900ms/revolution, infinite · skeleton `{motion.duration-emphasis}` 450ms/pass, infinite | `linear` · `{motion.ease-standard}` | `transform: rotate()` · `transform: translateX()` on a masked gradient | Both loops frozen; static indicator, label fades at `{motion.duration-reduced}` |

Rules held: transform/opacity only (paint-only colour changes used where the brand's state *is* a colour change); every exit shorter than its entrance; nothing animates on first paint; the two loaders are the only infinite animations and there is no brand ambience. The 900ms spinner revolution is the single stated deviation from the profile scale, with its reason in the file.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` (`theme_of` / `bound_polarity`, ~line 372 onward, as of commit `981bd47` plus uncommitted edits) | A token bound to exactly one ground is assigned that ground's polarity as its *theme*. `mute` is bound only by `link-mute-soft`, whose ground I declared as ink, so `mute` became a dark-theme token and **all three of its light-surface failures stopped being emitted** — including `check("text-dim", "canvas")`, which is a SPEC section 2 required pair. A correct binding fix silently erased a real failure elsewhere. | Do not let a single binding re-theme a token that the prose places on the default-polarity grounds; or exempt the section 2 required pairs from the theme filter, since `text-dim on canvas` is asserted by the role table rather than by a binding. At minimum, report theme-suppressed pairs in a separate field so they are visible instead of absent. |
| `theme-audit/audit.py` (surface role, ~line 278-317) | The resolved `surface` for this file moved between two runs twenty minutes apart (`canvas-softer` -> `canvas-soft`) while `design-md/uber/DESIGN.md` was unchanged, because `audit.py` itself was edited mid-run. The brief's pre-measured figure (`mute on surface-pressed` 1.69:1) matches neither. | Harness changes during a run make before-scores non-comparable across agents; pin the harness for the duration of a run, or stamp each report with the `audit.py` commit it was measured against. This report's before-scores were measured at md5 `7e4d7d7f…` and its after-scores at `e7b57c98…`. |
| `theme-audit/audit.py` (component contrast, ~line 655) | A component that declares `textColor` and no `backgroundColor` is measured against the page floor. For `link-on-dark` that manufactured a 1.00:1 white-on-white failure the site never renders. The local fix (declaring the ground the prose asserts) only works where the prose asserts one. | Where a component's name or description states its ground (`*-on-dark`, `*-on-light`, "on dark surfaces"), resolve that ground instead of the canvas; otherwise skip the pair rather than substituting the page, as the code already does for unresolvable declared grounds. |
| `theme-audit/SPEC.md` section 5, rule 3 | "Saturated multi-colour **or** illustration-led consumer identity -> Playful" is then qualified by "judge this on saturation *and role*", which reads as a conjunction and would send a zero-saturation illustration-led brand to Calm. Uber is exactly that case. | Say explicitly whether the illustration-led branch stands on its own for a monochrome palette. One sentence would settle it for every illustration-led brand in the roster. |

### Needs approval

- **`mute` `#afafaf` on light grounds.** Extracted and unchanged. Nearest passing values: `#767676` (4.54:1 on canvas), `#6d6d6d` (4.50:1 on canvas-soft). The usage note that would make the real value defensible does not exist here — `mute` fails even the 3:1 large-text threshold (2.19:1), so there is no minimum type size at which `#afafaf` passes. If the brand wants to keep the hex, the only defensible scope is non-text decoration; for 24px+/18.66px-bold labels the nearest passing tone is `#949494` (3.03:1).
- **`surface-pressed` as a divider on the real site.** I re-pointed only the three auto-derived `ex-*` boundaries. If the live site really does draw dividers in `#e2e2e2` (1.13:1 / 1.30:1), the extracted bindings should stay and the prose should call those dividers decorative; a brand owner has to say which it is.
- **`hairline-mid` `#4b4b4b` as the boundary tone.** It passes comfortably (7.59:1 on canvas-soft) but is visually heavy for a hairline. If the brand wants a true hairline that still clears 3:1, `#8a8a8a` measures 3.00:1 on canvas-soft and 3.45:1 on canvas — but it would be a new, prescribed token, so I did not add it.
- **Disabled treatment.** Specified as 38% opacity on the live fill and label, because the palette contains no disabled tone and inventing a grey hex would falsify a monochrome brand. Needs a real token or confirmation of the opacity.
- **Error signalling with no semantic palette.** Specified as a 2px `{colors.ink}` boundary plus a `{typography.caption}` message. It avoids colour-only signalling, but it gives no colour cue at all. Either approve it or supply the brand's real error tone.
- **The 900ms spinner revolution**, the one value outside the Playful scale (the profile's longest token, 450ms, spins too fast to read as a loader).
- **Applying `{colors.black-elevated}` to the hover state of other ink pills.** Extracted for one control (the hero tab pill) only; extending it is prescribed consistency.

### Identity verdict

The file still reads as Uber, and more so than before: the two rings are the brand's own ink and paper rather than a borrowed blue, the hover and pressed fills in the states table are the extracted `#282828` and `#e2e2e2`, and the motion section argues from the pill and the editorial illustrations rather than from a generic token scale. Nothing I added would suit another file in the collection unchanged. The one piece of real drift is pre-existing and left verbatim: the `ex-*` block's descriptions come from the shared example kit and mention a "mono-caps eyebrow typography" this file does not define — recorded in Known Gaps.

**Playful: retained, with the tension stated.** The pull toward Calm is real — the palette is pure grayscale apart from a browser-default link blue in legal fine print, the Don'ts forbid a second accent, there are no gradients, and the Overview's own word is "restraint". Under a strict conjunctive reading of rule 3 (saturation *and* informal type voice) Uber fires neither and falls to rule 4, Calm. I kept Playful on the other branch of rule 3: this is an illustration-led consumer identity, and not incidentally so — the file calls the editorial 4:3 illustrations of riders, drivers and city objects "the only consistent decorative system", and the pill at 999px is on every interactive element, which is the geometry a scale pop is for. Rule 3's saturation test exists to stop bright *static card backgrounds* from reading as playful, which is not this file's situation; Uber has no saturated colour to misread. So the honest answer is that the brand is Playful in form and restrained in colour, and I expressed that by using the Playful block verbatim while keeping travel at 8-12px and scale at 0.98-1.02 — springy, never bouncy. If the roster owner prefers the conjunctive reading, Calm is the defensible alternative and only the duration/easing block would change; the interaction table's structure holds either way.
