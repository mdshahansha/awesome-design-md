## A37 · minimax

Scores before -> after (1-5), from the harness:

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 3 | 5 |
| states | 1 | 5 |

Before: 15 undisclosed contrast failures, 0 disclosed. After: 0 undisclosed, 10
disclosed. The remaining ten are extracted brand values, frozen on purpose and
named with their measured ratios in the file's Accessibility section.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A. Token contract | `colors:` | No `focus` role. No focus treatment of any kind was documented for a platform whose whole product is keyboard-driven developer surfaces. |
| P0 | F. Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. The only timing in the file was a loose "recommend 150–200ms" line in Known Gaps. |
| P0 | G. Accessibility | whole file | No `## Accessibility` section, so fifteen measurable contrast failures were undisclosed. |
| P0 | H. States | `## Components` | The file opened with "Per the no-hover policy, hover states are NOT documented." SPEC section 7 requires every component entry to name its states; a blanket refusal to document four of the eight is a P0 against that contract, not a policy. hover, focus-visible, loading and selected appeared nowhere. |
| P1 | B. Colour | `muted` `#a8aab2` | 2.32:1 on canvas, 2.18:1 on surface. The tone is correct for the black footer (8.54:1) and wrong everywhere else, and the file used it for "de-emphasized labels" generally. |
| P1 | B. Colour | `hairline` `#e5e7eb`, `hairline-soft` `#eaecf0` | 1.24:1 and 1.18:1 on canvas. Frozen extracted values, but `text-input` and `search-pill` used `hairline` as the control's *only* boundary — SPEC section 2's exact example. |
| P1 | B. Colour | `badge-success` | `success-text` on `success-bg` is 2.95:1 at 13px. A real brand AA failure that the file did not mention. |
| P1 | B. Colour | `product-card-*` taglines | 14px white at 80% opacity on coral (full-opacity white is already only 3.18:1). The weakest text in the system and undocumented. |
| P1 | A. Token contract | `components.footer-link` | Declared `backgroundColor: transparent` while the prose places it inside the black footer, so the pair measured as `muted` on white (2.32:1) — a failure the brand does not actually ship. |
| P1 | C. Elevation | `card-feature` | The only component relying on a bare `{colors.surface}` fill with no border or shadow, across a 1.06:1 tonal step. Undocumented as a weakness. |
| P1 | A. Token contract | `shadow:` | Elevation & Depth stated five real `rgba(...)` elevations with no token group to reference, exactly the gap SPEC section 1 calls out. |
| P2 | A. Token contract | `components.product-card-*` | No `typography:` key, so the harness applied 4.5:1 to cards whose prose says the wordmark is 40–56px. The threshold was wrong, not the colour. |
| P2 | E. Ladders | `button-primary` padding `11px 24px` | 11px sits off the 4px spacing ladder. Extracted (it yields the 38–40px pill height with a 14px/1.4 label), so left alone and noted. |
| P2 | E. Ladders | `{rounded.xxl}` (20px) | Defined in the radius scale, bound by no component. Now in Known Gaps. |
| P2 | D. Typography | `docs-prose-block` | Prose says "line-height 1.6" while its bound `{typography.body-md}` is 1.50. Left as written — it is an extracted observation about that one surface — but the two numbers disagree. |
| P2 | B. Colour | `stone` `#8e8e93` | 3.26:1 on canvas. Passes for 24px+ only, and the file describes it as "muted captions and tab inactive labels" — captions are 13px. Noted in the report rather than re-scoped, since the harness does not class `stone` as text-dim and the usage is ambiguous. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| `colors:` | added `focus: "#1456f0"`, `focus-on-dark: "#ffffff"` | Satisfies the missing role with the brand's own blue plus a white ring for its black and saturated surfaces. Both prescribed and labelled as such. |
| `colors:` | added `hairline-strong: "#767a85"`, `muted-strong: "#6f717a"`, `success-text-strong: "#0f7a50"` | SPEC section 2 parallel accessible tokens. The frozen originals stay and are scoped to decoration in the prose. |
| frontmatter | added `shadow:` group with the five elevations the prose already stated | A documented `rgba(...)` with no token was unreferenceable. |
| frontmatter | added `motion:` group, Crisp block verbatim from SPEC section 5 | Missing group; values copied without deviation so the file stays comparable with its Crisp siblings. |
| `components.button-primary-*` | added `-hover`, `-focus-visible`, `-loading` | Three of the four missing states, labelled prescribed. |
| `components.text-input` | border `{colors.hairline}` -> `{colors.hairline-strong}`; added `outline` + `outlineOffset` to `-focused`; added `text-input-disabled` | The border is the field's only boundary at 1.24:1. |
| `components.search-pill` | border `{colors.hairline}` -> `{colors.hairline-strong}` | Same reason. |
| `components.product-card-*` | added `typography:` (`display-lg` for coral and photo, `heading-lg` for magenta, blue, purple) | Binds the size the prose already states, so the 3:1 large-text threshold applies instead of 4.5:1. No hex changed. |
| `components.footer-link` | `backgroundColor: transparent` -> `{colors.footer-bg}` | SPEC section 1: declare the pair the prose asserts. Measures 8.54:1, which is what the brand ships. |
| `components` | added `badge-success-accessible` | Prescribed parallel for the 2.95:1 badge; original kept. |
| `## Colors` | added Hairline Strong, Muted Strong, Success Text Strong entries and a new `### Focus` subsection | Documents the five new tokens with their measured ratios and marks each prescribed. |
| `## Elevation & Depth` | shadow values now reference `{shadow.*}`; added a one-way-per-layer line and a "Layer separation, measured" subsection | Elevation is now expressed consistently (border at level 0, shadow at 1–4) and the 1.06:1 canvas/surface step is stated. |
| `## Components` | replaced the "no-hover policy" note; added a `### State coverage` table | Every component family now names all eight states or says the state does not apply, with extracted and prescribed marked separately. |
| `## Components` | `button-primary`, `text-input`, `search-pill`, `badge-success` entries extended | Each names its new states and the substitution made. |
| after `## Components` | new `## Motion & Animation` | Missing section. First line states the system is prescribed and unmeasured. |
| after that | new `## Accessibility` | Missing section. Carries the passing pairs, the disclosed failures, per-surface ring ratios, tap targets and reduced motion. |
| `## Do's and Don'ts` | four new Don'ts | Coral/magenta text sizes, hairline scope, layout-property animation, entrance ceiling. |
| `## Iteration Guide` | two new steps | Motion and focus-ring guidance. |
| `## Known Gaps` | replaced the "150–200ms" line; added five entries | Motion, four prescribed states, the focus ring, the three prescribed tokens and the unbound 20px radius are all now declared as inference rather than extraction. |

Nothing outside `design-md/minimax/DESIGN.md` and this report was touched. No brand
identity hex was altered.

### Contrast checks

All computed with the WCAG 2.1 relative-luminance formula via a `python3 -I`
snippet; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #0a0a0a / `canvas` #ffffff | 19.80:1 | 4.5 | Pass |
| `ink` / `surface` #f7f8fa | 18.63:1 | 4.5 | Pass |
| `charcoal` #222222 / `canvas` | 15.91:1 | 4.5 | Pass |
| `slate` #45515e / `canvas` | 8.10:1 | 4.5 | Pass |
| `steel` #5f5f5f / `canvas` | 6.39:1 | 4.5 | Pass |
| `steel` / `surface` | 6.01:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary` #0a0a0a | 19.80:1 | 4.5 | Pass |
| `muted` #a8aab2 / `footer-bg` #0a0a0a | 8.54:1 | 4.5 | Pass |
| `brand-blue-deep` #1d4ed8 / `brand-blue-200` #bfdbfe | 4.72:1 | 4.5 | Pass |
| `stone` #8e8e93 / `canvas` | 3.26:1 | 4.5 | Fail (passes at 24px+) |
| `muted` / `canvas` | 2.32:1 | 4.5 | Fail — disclosed |
| `muted` / `surface` | 2.18:1 | 4.5 | Fail — disclosed |
| `hairline` #e5e7eb / `canvas` | 1.24:1 | 3.0 | Fail — disclosed, scoped to decoration |
| `hairline-soft` #eaecf0 / `canvas` | 1.18:1 | 3.0 | Fail — disclosed, scoped to decoration |
| `hairline` / `surface` | 1.17:1 | 3.0 | Fail — disclosed |
| `hairline-soft` / `surface` | 1.11:1 | 3.0 | Fail — disclosed |
| `success-text` #1ba673 / `canvas` | 3.11:1 | 4.5 | Fail — disclosed (it is a badge label, not body ink) |
| `success-text` / `success-bg` #e8ffea (`badge-success`) | 2.95:1 | 4.5 | Fail — disclosed |
| `on-dark` #ffffff / `brand-coral` #ff5530 (`badge-new`, `promo-cta-card`) | 3.18:1 | 4.5 | Fail — disclosed |
| `on-dark` / `brand-magenta` #ea5ec1 | 3.06:1 | 3.0 large text | Pass at 40px+, fails at body sizes |
| `on-dark` / `brand-purple` #a855f7 | 3.96:1 | 3.0 large text | Pass at 40px+ |
| `hairline-strong` #767a85 / `canvas` | 4.29:1 | 3.0 | Pass (prescribed) |
| `hairline-strong` / `surface` | 4.04:1 | 3.0 | Pass (prescribed) |
| `hairline-strong` / `surface-soft` #f2f3f5 | 3.87:1 | 3.0 | Pass (prescribed) |
| `muted-strong` #6f717a / `canvas` | 4.86:1 | 4.5 | Pass (prescribed) |
| `muted-strong` / `surface` | 4.58:1 | 4.5 | Pass (prescribed) |
| `success-text-strong` #0f7a50 / `success-bg` | 5.08:1 | 4.5 | Pass (prescribed) |
| `success-text-strong` / `canvas` | 5.36:1 | 4.5 | Pass (prescribed) |
| `focus` #1456f0 / `canvas` | 5.80:1 | 3.0 | Pass |
| `focus` / `surface` | 5.46:1 | 3.0 | Pass |
| `focus` / `surface-soft` | 5.23:1 | 3.0 | Pass |
| `focus-on-dark` #ffffff / `footer-bg` and `primary` | 19.80:1 | 3.0 | Pass |
| `focus-on-dark` / `brand-blue` #1456f0 | 5.80:1 | 3.0 | Pass |
| `focus-on-dark` / `brand-purple` | 3.96:1 | 3.0 | Pass |
| `focus-on-dark` / `brand-coral` | 3.18:1 | 3.0 | Pass |
| `focus-on-dark` / `brand-magenta` | 3.06:1 | 3.0 | Pass (narrowest ring margin in the file) |
| `focus-on-dark` / `ink-strong` #000000 (two-tone band separation over photography) | 21.00:1 | 3.0 | Pass |
| Layer step: `canvas` / `surface` | 1.06:1 | — | Stated in Elevation |
| Layer step: `canvas` / `surface-soft` | 1.11:1 | — | Stated in Elevation |
| Layer step: `surface` / `surface-soft` | 1.04:1 | — | Stated in Elevation |

Two rings rather than one, because MiniMax documents both a white marketing canvas
and black/saturated signature surfaces — SPEC section 1's dual-polarity case. Both
are drawn outside the control at a 2px offset with a 2px stroke, so each is judged
against the surface behind the control, which is also the only reading under which
a single value could clear 3:1 on both a white canvas and a coral card.

### Motion inventory

Profile: **Crisp**, as rostered. Prescribed, not extracted — stated in the
section's first line in the file.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `background-color`, `opacity` | Unchanged; no travel to remove |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `transform: scale(0.99)` | Scale removed; fill step alone marks the press |
| Focus | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on the ring | Ring appears instantly, never animated |
| Page / route transition | `{motion.duration-base}` 150ms in, `{motion.duration-fast}` 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-reduced}` 100ms |
| Modal / drawer | `{motion.duration-slow}` 220ms in, `{motion.duration-base}` 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateX/Y`, `opacity` | Travel removed; fade at 100ms |
| Dropdown | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: scale(0.98 → 1)` | Scale removed; fade at 100ms |
| Toast | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px → 0)` | Travel removed; fade at 100ms |
| List enter | `{motion.duration-base}`, `{motion.stagger-step}` 20ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px → 0)` | Stagger and travel removed; one fade at 100ms |
| List exit | `{motion.duration-fast}` 100ms, no stagger | `{motion.ease-exit}` | `opacity`, `transform: translateY(0 → 4px)` | Travel removed; fade at 100ms |
| Loading | 800ms spinner, 1200ms skeleton sweep, infinite while pending | linear / `{motion.ease-standard}` | `transform: rotate`, `opacity` | Both frozen; static glyph and flat fill remain |

Every exit is shorter than its entrance. `transform` and `opacity` only. Nothing
animates on first paint. The only infinite animations are the two loaders; no brand
ambience is claimed, because MiniMax ships none.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 386-387 (`if fg and not bg and roles.get("canvas")`) | A component declaring `backgroundColor: transparent` is measured against the canvas even where the prose places it on a known dark ground. `footer-link` produced a phantom 2.32:1 failure the brand does not ship. SPEC section 1 already prescribes the in-file remedy (declare the pair), so this is a usability wart rather than a scoring bug — but every file with a footer link will hit it. | Treat the literal value `transparent` as "ground unknown" and skip, or let a component name an `on:` key naming the ground it sits in. |
| `theme-audit/audit.py` line 375-379 (`threshold_for`) | A component with no `typography:` key silently gets 4.5:1. For the five `product-card-*` entries, whose prose states a 40–56px wordmark, that reported a colour failure where the real defect was a missing binding. | Report untyped components in a separate bucket ("threshold assumed") rather than as contrast failures, so agents fix the binding instead of arguing about the hex. |
| `theme-audit/SPEC.md` section 3 | `Iteration Guide` is documented as optional and the harness honours that, but the section contract table still lists it inside the same table as the required sections, which reads as a requirement on a first pass. | Split the optional row out of the table, or mark it in a separate list. |

No role-pattern harness bug to report for this file: `focus` was genuinely absent
from the palette under any name, so adding it was the correct remedy rather than a
regex-pleasing alias. The five tokens added are a focus pair the brand lacked
entirely plus three SPEC section 2 parallel accessible tones, none of them an alias
for an existing value.

### Needs approval

1. **`badge-new` — white on `brand-coral` at 13px, 2.95–3.18:1.** Coral is the
   brand's signature signal colour and the "NEW" pill is one of its most
   recognisable marks, so the hex is unchanged. Nearest passing value for white
   text at 13px is `#c73410` (5.35:1), which is visibly a different, darker red.
   Defensible alternative that keeps the coral: set the label in `{colors.ink}`
   instead of white (6.22:1 on coral). Usage note that would make the real value
   defensible: the badge is decorative redundancy beside a model name that is
   already legible, so 1.4.3 arguably does not apply — but only if the badge never
   carries information available nowhere else.
2. **`badge-success` — `success-text` on `success-bg` at 13px, 2.95:1.** Shipped
   `badge-success-accessible` alongside it using the prescribed
   `{colors.success-text-strong}` #0f7a50 (5.08:1). Approval needed on whether the
   accessible variant becomes the default and the extracted pairing is demoted to a
   documentation-only record.
3. **`product-card-*` taglines — 14px white at 80% opacity on coral/magenta.**
   Below 3.18:1 and 3.06:1 respectively. No fix applied because the opacity is an
   extracted observation. Options: full opacity plus 18px/700 (reaches the 3:1
   large-text threshold), or move the tagline off the saturated fill.
4. **`stone` #8e8e93 at 3.26:1 on canvas, described as "muted captions".** Either
   re-scope the prose to 24px+ labels only, or substitute `{colors.muted-strong}`
   for captions. Left unchanged because the usage is genuinely ambiguous in the
   source and I would be guessing which of the two the brand means.
5. **`focus-on-dark` on `brand-magenta` at 3.06:1.** Clears the bar with 0.06 to
   spare. If magenta is ever darkened or the ring stroke drops below 2px, this is
   the first pair to fail.

### Identity verdict

Still MiniMax, and recognisably so. The duality the Overview claims — stark white
marketing canvas with black pills against album-cover product cards in coral,
magenta, blue and purple — survived intact; no brand hex moved. The two additions
that carry the most risk of genericising a file are the focus ring and the motion
block, and both were taken from the brand rather than from a default: the light-
surface ring is `{colors.brand-blue}` itself, not a generic system blue, and the
two-ring structure exists *because* this brand has black footers and saturated
cards, which is a MiniMax-specific fact. The ring radius inherits
`{rounded.full}` on pills and `{rounded.hero}` on product cards, so focus looks
like this system rather than like a browser default.

**Crisp is the right profile and I kept it.** The assignment rule fires on rule 2:
MiniMax is a developer platform whose documented surfaces are API docs, a 3-column
documentation grid, a models comparison table and a pricing console — the file's own
description calls it "AI infrastructure". The tempting counter-argument is rule 1 or
rule 3: the vibrant gradient product cards with dark portrait photography read
cinematic, and four saturated hues read playful. Both fail on role. The saturated
colour appears only as static card fills behind product wordmarks, never on an
interactive element — the file's own Do's forbid exactly that ("never for general
buttons or text") — and the type voice is a 600-weight geometric sans at -2px
tracking, which is technical rather than informal. The photography is product
imagery inside bounded cards, not the full-bleed slow reveal rule 1 describes. So
Crisp, with the one concession stated in the file: the product cards get a small
scale step on press, still under 220ms.

The one thing I would flag as drift risk for a future pass is the State coverage
table. It is the largest single block I added and it is mostly prescribed, so it
carries less brand information per line than anything else in the file. It is
labelled as prescribed throughout, and the extracted states are called out
individually, but a reader skimming it could mistake inference for observation.
