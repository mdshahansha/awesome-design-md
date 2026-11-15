## A66 · spacex

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 2 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

Both harness runs: `python3 -I theme-audit/audit.py --site spacex --json`.

**Note on the before-scores.** `theme-audit/audit.py` was updated mid-review (commits `dd934af`, `b805d65`). My first run, against the earlier script, read `tokens 4 · refs 5 · contrast 3 · sections 2 · motion 1 · states 1`. Both columns above are re-measured against the **current** script, by restoring the pre-edit file from commit `3883984` and re-running, so they are comparable. The change moved `contrast` from 3 to 1 because the new `dual_theme` polarity detection and the reordered `text-dim` patterns surfaced three more pairs; it also changed the `surface` role from `canvas-light` to `canvas-night-soft`, which is **correct for this brand** — `canvas-night-soft` is the real raised dark surface, while `canvas-light` is the shop site's own canvas at the other polarity.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, G | `focus` role | No focus ring of any kind. Four surfaces (`canvas-night`, `canvas-night-soft`, `canvas-light`, `canvas-cool`) plus full-bleed photography, and no keyboard indicator on any of them. Fixed. |
| P0 | B, E | `text-input` boundary | `hairline-on-light` `#e0e0e8` on `canvas-light` `#ffffff` = 1.31:1. On the input this 1px edge is the control's *only* boundary, so WCAG 1.4.11 applies and is not met. Extracted and frozen; prose re-scoped, re-binding under Needs approval. |
| P0 | B, C | `hairline-on-dark` | `#3a3a3f` on `canvas-night` `#000000` = 1.86:1, below 3:1 — the dark-side boundary tone cannot be seen. The harness never reports it (Shared issues #2), so it was an entirely silent failure. Disclosed and re-scoped. |
| P1 | F | frontmatter + document | No `motion:` group and no `## Motion & Animation` section. Fixed with the Cinematic block verbatim from SPEC section 4. |
| P1 | G | document | No `## Accessibility` section, so every contrast failure above was undisclosed. Fixed. |
| P1 | — | document | No `## Known Gaps`, so prescribed values had nowhere to be declared. Fixed. |
| P1 | H | all 10 components | Zero of the eight states documented anywhere. Fixed; hover is the only state with extracted evidence, the rest are labelled prescribed. |
| P1 | C | `canvas-night-soft` | `#0a0a0a` separates from `#000000` at 1.06:1. The file calls it "a subtle separation"; at 1.06:1 it is no separation at all, and its paired hairline (1.86:1) does not rescue it. Recorded in Known Gaps as the brand's own limitation, not corrected. |
| P1 | B | `link-blue-fallback` | `#0000ee` on `canvas-night` = 2.23:1. Documented as a non-brand browser default but never flagged as a failure; the harness checks no `^link` pattern. Disclosed. |
| P1 | B, G | `ink`, `ink-mute` | Four harness-reported failures (1.0:1, 1.06:1, 3.06:1, 2.89:1) are **manufactured**: the shop site's light-surface inks measured on the two dark grounds, which the product never pairs. Not corrected in the palette — the pairings do not exist — but disclosed in the file as manufactured, and the root cause filed under Shared issues. |
| P2 | A | prose refs | `{button-ghost-on-dark}`, `{text-input}`, `{link-on-dark}` are written without a group, so they resolve only by luck and are invisible to the reference checker. Not fixed — the style is used consistently across the file and the Iteration Guide teaches it; changing it is a whole-file reflow. |
| P2 | B, D | `on-primary-mute` | `#f0f0fa` sits 1.13:1 from `on-primary` `#ffffff`. As a secondary-ink tier it is imperceptible; the file already admits it is "barely distinguishable". Noted in Accessibility. |
| P2 | D | `body-lg` / `body-md` | Both 16px / 400 / 0.32px, differing only in line-height (1.7 vs 1.5). A two-token tier that is really one size with two leadings. Left as extracted. |
| P2 | D | `button-cap`, `caption` | `fontSize: 13.008px` is a computed-style artifact carried into a spec. Harmless but it is not a designed value. Left as extracted. |
| P2 | E | `spacing.lg` | 18px is the only value in the 4/8/12/16/24/32/48 ladder that is not a multiple of 4. It is load-bearing (the pill's vertical padding, and the source of the 49px tap height), so left alone. |

Ladders checked and found internally consistent: `rounded` 4/8/16/32/9999 is a clean doubling with a separate `full`; elevation is expressed one way only (photography), never shadow-and-border mixed — the file explicitly forbids shadows, blurs, glows and gradients. Every typography role carries fontFamily, fontSize, fontWeight and lineHeight.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#ffffff"`, `focus-on-light: "#000000"` | Two polarities need two rings (SPEC section 1). Both are hexes the palette already owns (`on-primary`'s white, `ink`'s black), so these are real role bindings on distinct surfaces, not aliases, and the brand's no-accent rule survives. |
| frontmatter | — -> `motion:` group | Cinematic profile block from SPEC section 4, verbatim, no deviation. |
| Colors › Surface | hairline bullets -> same bullets + measured ratio + decoration scoping | 1.86:1 and 1.31:1 stated in place; boundaries that must be seen are pointed at `on-primary` (21:1 on dark) and `ink-mute` (6.86:1 on light), both already in the palette, so nothing was added (SPEC section 2 step 1). |
| Colors › Link | `link-blue-fallback` bullet -> + 2.23:1 and a never-render rule | A documented colour with an undocumented failure. |
| Colors › **new** Focus Ring | — -> subsection | States which existing tone each ring reuses, the 2px/2px geometry, the two-tone treatment over photography, and every measured ratio. |
| Components (intro) | — -> one paragraph | Marks hover as the only extracted state and the rest as prescribed, before the tables assert them. |
| Components, all 10 entries | — -> a `**States:**` line each | `card-photo-band` and `footer-dark` say default-only; both links say three states only; `nav-bar-overlay` says disabled is not used. |
| Components › `text-input` | "1px `{colors.hairline-on-light}` border" -> extracted value kept and measured, with `{colors.ink-mute}` specified for the edge that must be seen | The one place the frozen hairline does load-bearing contrast work. |
| **new** `## Motion & Animation` (after Components) | — -> section | First line states the system is prescribed and was not measured from the live site. 10-row interaction table, rules, and the reduced-motion block. |
| **new** `## Accessibility` (after Motion) | — -> section | 12 passing pairs, 4 declared failures with ratios, per-surface ring visibility, tap target, reduced motion. |
| **new** `## Known Gaps` (after Iteration Guide) | — -> section | Separates prescribed-not-extracted, genuinely-absent-from-the-brand, not-computable-from-a-document, and unverified. |

Section order now matches SPEC section 3 exactly: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Motion & Animation, Accessibility, Do's and Don'ts, Responsive Behavior, Iteration Guide, Known Gaps. `Responsive Behavior` was already top-level, so nothing moved.

### Contrast checks

All computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `on-primary` #ffffff / `canvas-night` #000000 | 21.0:1 | 4.5:1 | Pass |
| `on-primary` / `canvas-night-soft` #0a0a0a | 19.8:1 | 4.5:1 | Pass |
| `on-primary-mute` #f0f0fa / `canvas-night` | 18.55:1 | 4.5:1 | Pass |
| `on-primary-mute` / `canvas-night-soft` | 17.49:1 | 4.5:1 | Pass |
| `ink` #000000 / `canvas-light` #ffffff | 21.0:1 | 4.5:1 | Pass |
| `ink` / `canvas-cool` #f0f0fa | 18.55:1 | 4.5:1 | Pass |
| `ink-mute` #5a5a5f / `canvas-light` | 6.86:1 | 4.5:1 | Pass |
| `ink-mute` / `canvas-cool` | 6.06:1 | 4.5:1 | Pass |
| `on-primary` / `primary` #000000 (on-accent on accent) | 21.0:1 | 4.5:1 | Pass |
| `focus` #ffffff / `canvas-night` | 21.0:1 | 3.0:1 | Pass |
| `focus` / `canvas-night-soft` | 19.8:1 | 3.0:1 | Pass |
| `focus-on-light` #000000 / `canvas-light` | 21.0:1 | 3.0:1 | Pass |
| `focus-on-light` / `canvas-cool` | 18.55:1 | 3.0:1 | Pass |
| `focus` against `focus-on-light` (composite ring bands) | 21.0:1 | 3.0:1 | Pass |
| `hairline-on-light` #e0e0e8 / `canvas-light` | 1.31:1 | 3.0:1 | **Fail** — real, extracted, disclosed |
| `hairline-on-light` / `canvas-cool` | 1.16:1 | 3.0:1 | **Fail** — real, extracted, disclosed |
| `hairline-on-dark` #3a3a3f / `canvas-night` | 1.86:1 | 3.0:1 | **Fail** — real, extracted, disclosed; harness-invisible |
| `hairline-on-dark` / `canvas-night-soft` | 1.75:1 | 3.0:1 | **Fail** — real, extracted, disclosed |
| `link-blue-fallback` #0000ee / `canvas-night` | 2.23:1 | 4.5:1 | **Fail** — unstyled fallback only, disclosed |
| `link-blue-fallback` / `canvas-light` | 9.4:1 | 4.5:1 | Pass |
| `ink` #000000 / `canvas-night` #000000 | 1.0:1 | 4.5:1 | **Fail, manufactured** — the site never draws the shop ink on the marketing canvas; disclosed because the harness reports it |
| `ink` #000000 / `canvas-night-soft` #0a0a0a | 1.06:1 | 4.5:1 | **Fail, manufactured** — same cause |
| `ink-mute` #5a5a5f / `canvas-night` #000000 | 3.06:1 | 4.5:1 | **Fail, manufactured** — a light-surface secondary ink measured on the black canvas |
| `ink-mute` #5a5a5f / `canvas-night-soft` #0a0a0a | 2.89:1 | 4.5:1 | **Fail, manufactured** — same cause |
| `canvas-night-soft` / `canvas-night` (layer separation) | 1.06:1 | 3.0:1 | **Fail** — nominal elevation, recorded in Known Gaps |
| `canvas-cool` / `canvas-light` (layer separation) | 1.13:1 | 3.0:1 | Fail as a boundary; it is a tint, not an elevation step |
| `on-primary-mute` / `on-primary` (ink tier separation) | 1.13:1 | — | No threshold applies; noted as imperceptible |

### Motion inventory

Profile: **Cinematic**. Prescribed, not extracted — stated as the first line of the section in the file.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (ghost CTA, nav item, link) | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity`, chevron `translateX` | Travel removed; opacity only at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` | Unchanged — already opacity-only, under 150ms |
| Focus (ring appear) | `{motion.duration-instant}` 120ms | `{motion.ease-enter}` | `opacity` | Unchanged; ring never fades on blur, exempt from all reduction |
| Page / route transition | `{motion.duration-emphasis}` 900ms | `{motion.ease-enter}` | `opacity`, hero `scale(1.04 -> 1)` | Scale removed; cross-fade at `{motion.duration-reduced}` |
| Modal / drawer (shop cart) | in 400ms / out 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(24px -> 0)` | Travel removed; opacity at `{motion.duration-reduced}` |
| Dropdown (nav menu, size picker) | in 240ms / out 120ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(-8px -> 0)` | Travel removed; opacity at `{motion.duration-reduced}` |
| Toast | in 400ms / out 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(16px -> 0)` | Travel removed; opacity at `{motion.duration-reduced}` |
| List enter (shop grid, footer columns) | 400ms per item, `{motion.stagger-step}` 80ms apart | `{motion.ease-enter}` | `opacity`, `translateY(16px -> 0)` | Stagger and travel removed; all items fade together at `{motion.duration-reduced}` |
| List exit (filter change) | `{motion.duration-fast}` 240ms, no stagger | `{motion.ease-exit}` | `opacity` | Duration drops to `{motion.duration-reduced}` |
| Loading (indeterminate sweep) | 1200ms loop | linear | `translateX` on a 1px bar | Loop frozen; static 1px bar remains |

Rules honoured: `transform` and `opacity` only; every exit shorter than its entrance; nothing animates on first paint in a way that delays content; the only infinite animations are the loader and the autoplaying rocket-launch video, which is declared as deliberate brand ambience and freezes under reduced motion. `layout_animation_mentions` is empty after the edit.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 234, with the role-strengthening tuple at line ~291 after `dd934af` | The `text` role is resolved by `find_role`, whose first pattern is `^ink$`. In this dual-polarity file that picks `ink` (#000000, the shop site's light-surface ink) and then measures it on `canvas-night` (#000000), producing a 1.0:1 "body text" failure for a pairing the product never renders. Dark-canvas body text is `on-primary` at 21:1. | Add `"text"` to the `for role in ("border", "focus", "text-dim")` tuple so `text` goes through `find_role_strongest` against the resolved canvas, as the other three already do. That picks `on-primary` here. Every tone in the role is still measured separately by `check_all`, so the fix hides nothing. This is the narrower of the two fixes; the `theme_of()` row below is the root cause and would resolve this one too. |
| `theme-audit/audit.py` `theme_of()` (lines ~330-346 after `dd934af`) | The theme marker alphabet is still the literal strings `dark` and `light`, even though `dual_theme` now measures polarity. This file's dark grounds are `canvas-night` and `canvas-night-soft`, so `theme_of()` returns `None` for both, while `theme_of("hairline-on-dark")` returns `"dark"` and `theme_of("ink")` / `theme_of("ink-mute")` return `None`. Two consequences, in opposite directions: (a) the genuine 1.86:1 `hairline-on-dark` / `canvas-night` boundary failure is skipped by `same_theme()` and never recorded by `alt_grounds`, so it is invisible to the harness; (b) the light-polarity inks `ink` and `ink-mute` are treated as default-theme and measured on both dark grounds, manufacturing four failures (1.0:1, 1.06:1, 3.06:1, 2.89:1) for pairings the product never renders. This is the "satisfies a role wrongly, then measures against a ground the site never renders" case in SPEC section 1. The same blind spot hits any file naming a polarity `night`, `midnight`, `void`, `day` or `noon`. | Give `theme_of()` the same treatment `dual_theme` just received: where a token's name carries no marker, derive its polarity from measured luminance — grounds by their own luminance, inks by which ground they clear — instead of from the two literal strings. A smaller fix is to extend the alphabet (`night|midnight|void|black` -> dark, `day|noon|paper|white` -> light), which repairs (a) here but leaves (b), since `ink` and `ink-mute` carry no marker at all. |
| `theme-audit/briefs/A66-spacex.md` line 11 (generated by `theme-audit/make_briefs.py`) | The pre-measured list says "Missing colour roles: focus, text-dim." `text-dim` is not missing — it resolves to `on-primary-mute` (#f0f0fa, 18.55:1 on the canvas) and the harness reports only `focus`. Verified by running the harness before any edit. The brief is stale relative to the script. | Regenerate the briefs from the current `audit.py`, or have `make_briefs.py` read `roles_missing` directly rather than from a cached run. |
| `design-md/spacex/DESIGN.md` frontmatter `description` (line 4) | Two prose defects carried in from extraction: the brand is spelled "Spasex" throughout, and "UI chrome is intentionally minimal a single ghost outlined pill button" is missing its connector (`minimal — a single...`). | Not touched: the spelling is consistent across the whole file and the repo, so it looks deliberate rather than a typo, and a global rename is outside this file's remit. Flagging rather than guessing. |

### Needs approval

1. **Re-binding the extracted light hairline.** `hairline-on-light` #e0e0e8 is 1.31:1 on `canvas-light` and 1.16:1 on `canvas-cool`. Per SPEC section 2 step 3 I left the extracted value and its prose record intact and added nothing to the palette; the prose now scopes it to decoration and specifies the palette's own `ink-mute` #5a5a5f (6.86:1 / 6.06:1) for the `text-input` edge. A brand owner has to decide whether the shipped product changes.
   - Nearest passing value if the brand insists on a pale cool hairline: **#8c8c99** (3.32:1 on white, but still only 2.93:1 on `canvas-cool`) or **#767680** (4.49:1 / 3.97:1, passes on both). The lightest neutral that clears 3:1 on white at all is **#949494**.
   - Usage note that makes #e0e0e8 defensible where it stays: on `card-shop-product` the hairline is decorative separation between same-coloured cards and carries no information a user needs to identify or operate a control, so 1.4.11 does not apply. That argument is true of the card and false of the input, which is why only the input's edge was re-specified.
2. **Re-scoping the extracted dark hairline.** `hairline-on-dark` #3a3a3f is 1.86:1 on `canvas-night`. I scoped it to decoration and pointed load-bearing dark boundaries at `on-primary` (21:1), which is what the ghost CTA already does — so nothing was added. If the brand wants a true grey hairline instead, the nearest passing neutral on #000000 is **#5a5a5a** (3.04:1); the palette's own `ink-mute` #5a5a5f reaches 3.06:1 on `canvas-night` but only 2.89:1 on `canvas-night-soft`, so it would pass on one dark ground and fail on the other.
3. **Both focus rings are prescribed.** The source pages define no focus style. `focus` #ffffff and `focus-on-light` #000000 reuse existing palette hexes and introduce no hue, but the 2px ring / 2px outside offset and the two-tone treatment over photography are my specification and need sign-off. The offset matters: a ring drawn outside the control is judged against the surface behind it, which is what WCAG 2.2 Focus Appearance asks, and it is the only way to get 3:1 over an arbitrary photograph.
4. **Error styling without a red.** The brand forbids accent colour, so I expressed the error state through border weight, position and caption copy rather than a semantic hue. If the brand will accept one functional red for error states, that is a palette decision above this file.

### Identity verdict

Still unmistakably this brand. Nothing chromatic was added: the palette grew by two keys and both are hexes it already contained (#ffffff, #000000), so the "no accent colour, black and white and the photography" rule is intact — which was the main risk, since a focus ring is the usual place a monochrome brand acquires an accidental blue. The motion section argues from the brand's own material (full-bleed photography that settles, type arriving 80ms behind its imagery, a looping rocket-launch video declared as ambience) rather than from a generic interaction list, and the error state is deliberately typographic because the brand has no red to signal with. The one place the file now reads more like a system document than a brand document is the per-component States lines, which is unavoidable if states are to be documented at all; they are kept short and reference brand tokens only.

**Cinematic is correct and I did not switch it.** SPEC section 5 assignment rule 1 fires on the first clause: an aerospace identity, "whatever the canvas polarity", and the stated tell — full-bleed photography, sparse type, slow reveal — is this file's entire thesis. The pure-black canvas makes it the least ambiguous Cinematic case in the set; no argument for Crisp or Calm survives rule 1.
