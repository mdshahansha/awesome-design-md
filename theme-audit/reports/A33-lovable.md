## A33 · lovable

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

- **Before:** 1 · 5 · 5 · 1 · 1 · 1
- **After:** 5 · 5 · 5 · 5 · 5 · 5

The two "before" fives are artefacts of an empty file, not quality: with no frontmatter there were no references to dangle and no hexes to measure. The real starting state was a legacy numbered-heading document with zero tokens.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | J / format | whole file | No frontmatter token block at all; numbered heading variant (`## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide`). Nothing machine-readable, no `{group.token}` reference layer. |
| P0 | A / token contract | all eight colour roles | `canvas`, `surface`, `text`, `text-dim`, `border`, `accent`, `on-accent`, `focus` all absent. Every value existed in prose; none was a token. |
| P0 | B / colour | `hairline` #eceae4 | 1.10:1 against the cream canvas — fails WCAG 1.4.11 by a wide margin, and it is the *only* boundary on `text-input` and `ai-chat-input`, whose fill is the same #f7f4ed as the page. Frozen brand value. |
| P0 | B / colour, E | `ring-brand` rgba(59,130,246,0.5) | 1.78:1 on cream. The brand's only focus indicator, paired with a 12px rgba(0,0,0,0.1) shadow, and the file's own Don'ts forbid "sharp focus outlines". Keyboard focus is effectively invisible. |
| P0 | F / motion | — | No motion section, no motion tokens, no `prefers-reduced-motion` rule anywhere. |
| P0 | G / accessibility | — | No Accessibility section. The Overview asserts the cream/charcoal pair "creates a contrast ratio that's easy on the eyes" without measuring it. |
| P1 | B / colour | `ink-40` rgba(28,28,28,0.4) | Composites to #9f9e99 over cream = 2.44:1, fails 3:1. This is the *stronger* of the two real border tones and carries the entire visual identity of the ghost button. |
| P1 | H / states | all components | Not one of the eight states was documented. The file names `Active: opacity 0.8` and `Focus: shadow` in prose but never hover, focus-visible, disabled, loading, selected or error. |
| P1 | C / section contract | Shapes | No `## Shapes` section; the radius ladder was buried as a Layout subsection. |
| P1 | C / section contract | Known Gaps | Absent. Nine substantive omissions (no disabled tone, no semantic palette, no control dimensions, no gradient stops) were simply unmentioned. |
| P1 | G / tap targets | all buttons | 8px vertical padding + 16px/1.5 line box ≈ 40px declared height, below the 44 × 44 minimum. The Responsive section asserts "adequate spacing" and that a 9999px radius "creates large tap-friendly targets" — neither is a measurement, and radius has no bearing on hit area. |
| P2 | C / elevation | Depth table | Elevation is expressed three ways at once — border (L1), inset shadow (L2), drop shadow (L3), ring (L4). This is *documented* as deliberate and reads consistently, so it is polish, not a defect: the levels are mutually exclusive per component, not mixed at random. Left as-is. |
| P2 | D / typography | `display-hero` | line-height 1.00–1.10 with -1.5px tracking is correct at 60px, but the Responsive section scales the same role to 36px on mobile where that leading crowds. No mobile line-height is stated. |
| P2 | D / typography | `display-alt` weight 480 | A variable-font axis value with no fallback behaviour stated; `ui-sans-serif` will round it to 500. |
| P2 | A / refs | `shadow` group | The prose stated three real shadow values with no token to reference. Group added; names assigned during conversion, values verbatim. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Top of file | no frontmatter -> full YAML block: `colors` (16), `typography` (12 roles), `rounded` (6), `spacing` (14), `shadow` (3), `motion` (10), `components` (19) | Dimension J. Every value built from a hex, type row or component description already in the prose. Two exceptions, both labelled prescribed: `focus` and `hairline-strong`. |
| All nine headings | `## 1. Visual Theme & Atmosphere` -> `## Overview`; `## 2. Color Palette & Roles` -> `## Colors`; `## 3. Typography Rules` -> `## Typography`; `## 4. Component Stylings` -> `## Components`; `## 5. Layout Principles` -> `## Layout`; `## 6. Depth & Elevation` -> `## Elevation & Depth`; `## 7./8.` -> unnumbered; `## 9. Agent Prompt Guide` -> `## Iteration Guide` | SPEC section 3 heading set. Body prose untouched. |
| Section order | Components was 4th -> now 7th, so `## Motion & Animation` follows it | Brief F: motion must sit after Components. Blocks moved whole, not rewritten. |
| Layout -> Shapes | `### Border Radius Scale` moved out of Layout into a new `## Shapes`, with `{rounded.*}` references added to each rung | Required section was missing; the ladder was its natural content. |
| `## Shapes` | — -> `### Borders` and `### Focus Ring` subsections | Dimension E: one width (1px), two real tones with fixed jobs, plus the prescribed third; ring geometry (2px / 2px offset) stated. |
| `## Colors` | — -> `### Token Map` table + an "On the absence of an accent" note | Maps every prose colour to its token, and records that `accent` is filled by the charcoal CTA because this brand forbids a chromatic accent. |
| `colors.focus` | brand ships `rgba(59,130,246,0.5)` (1.78:1) -> token added as `#3b82f6` at full opacity (3.35:1 cream / 4.63:1 dark button) | SPEC section 1: no file in the repo defines a focus ring. Same brand hue, full opacity. One mid-luminance ring clears 3:1 on both of this file's surface polarities, so no `focus-on-dark` pair is needed. |
| `colors.hairline-strong` | — -> `#8a8884` (3.22:1), prescribed | SPEC section 2 parallel accessible token. `#1c1c1c` at 50% over cream — one stop between the brand's documented 0.4 and 0.82 — so it stays inside Lovable's own opacity model rather than introducing a hue. |
| `## Components` | — -> `### Component States` table, 11 rows × 8 states | Dimension H. Hover/press built from the file's own `{colors.ink-04}` "subtle hover backgrounds" and `opacity 0.8` active convention; disabled, loading and error are prescribed and labelled as such. The final row states plainly that the static surfaces have one state and no more. |
| after `## Components` | — -> `## Motion & Animation`, Playful block verbatim from SPEC section 5 | Dimension F. First line states the system is prescribed and unmeasured. |
| — | -> `## Accessibility` | Dimension G. 18 measured pairs, per-surface ring table, tap targets, reduced motion. |
| — | -> `## Known Gaps`, 13 entries | Everything the prose does not state, so nothing had to be invented. |

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`. Where the brand states a colour as an opacity over cream, the composited hex was computed first and the composite measured.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #1c1c1c / `canvas` #f7f4ed | 15.51:1 | 4.5:1 | pass |
| `ink` / `surface-cream` #f7f4ed | 15.51:1 | 4.5:1 | pass |
| `ink` / `hairline` #eceae4 as fill | 14.17:1 | 4.5:1 | pass |
| `muted` #5f5f5d / `canvas` | 5.83:1 | 4.5:1 | pass |
| `muted` / `hairline` as fill | 5.32:1 | 4.5:1 | pass |
| `on-primary` #fcfbf8 / `primary` #1c1c1c | 16.47:1 | 4.5:1 | pass |
| `ink-83` -> #414140 / `canvas` | 9.30:1 | 4.5:1 | pass |
| `ink-82` -> #434342 / `canvas` | 9.02:1 | 4.5:1 | pass |
| `focus` #3b82f6 / `canvas` | 3.35:1 | 3.0:1 | pass |
| `focus` / `primary` #1c1c1c | 4.63:1 | 3.0:1 | pass |
| `focus` / `hairline` #eceae4 as fill | 3.06:1 | 3.0:1 | pass |
| `hairline-strong` #8a8884 / `canvas` | 3.22:1 | 3.0:1 | pass (prescribed) |
| `hairline-strong` / `primary` | 4.82:1 | 3.0:1 | pass (prescribed) |
| `hairline` #eceae4 / `canvas` | **1.10:1** | 3.0:1 | **fail — frozen brand value, disclosed** |
| `ink-40` -> #9f9e99 / `canvas` | **2.44:1** | 3.0:1 | **fail — frozen brand value, disclosed** |
| `ring-brand` -> #99bbf2 / `canvas` | **1.78:1** | 3.0:1 | **fail — frozen brand value, disclosed** |
| `ring-brand` -> #2c4f89 / `primary` | **2.10:1** | 3.0:1 | **fail — frozen brand value, disclosed** |
| `ink-04` -> #eeebe5 / `canvas` | 1.08:1 | n/a | decorative tint, no requirement |
| `ink-03` -> #f0eee7 / `canvas` | 1.06:1 | n/a | decorative tint, no requirement |

The harness reports one disclosed failure (`hairline on surface-cream`) and zero undisclosed. It cannot see the `ink-40` and `ring-brand` failures because those values are `rgba(...)`, not hex, so they are measured by hand above and stated in the file's Accessibility section regardless. No brand hex was altered.

### Motion inventory

Profile: **Playful**, block taken verbatim from SPEC section 5. Prescribed, not measured — stated as the first line of the section.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `opacity` of the `{colors.ink-04}` tint / border layer | Unchanged — already opacity-only at ≤130ms |
| Press | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` 1→0.8 (brand's own active state) + `transform: scale(0.98)` | Scale removed; opacity drop remains, instant |
| Focus | 0ms, no transition | none | ring not animated | Unchanged — must never lag the keyboard |
| Page / route transition | in 200ms, out 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(8px→0)` | Travel removed; cross-fade at `{motion.duration-reduced}` |
| Modal / drawer (mobile sheet) | in `{motion.duration-slow}` 320ms, out 200ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(16px→0)` / `translateX(100%→0)` | All travel removed; cross-fade at 130ms; backdrop still fades |
| Dropdown | in 130ms, out 70ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(4px→0) scale(0.98→1)` | Travel and scale removed; fade at 130ms |
| Toast | in 200ms, out 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(8px→0)` | Travel removed; fade at 130ms; auto-dismiss unchanged |
| List enter (template gallery, feature cards, suggestion pills) | 200ms per item, `{motion.stagger-step}` 60ms between | `{motion.ease-enter}` | `opacity`, `translateY(8px→0)` | Stagger and travel removed; group fades once at 130ms |
| List exit (gallery filtering) | 130ms, no stagger | `{motion.ease-exit}` | `opacity`, `translateY(-4px)` | Travel removed; fade at 130ms |
| Loading (button spinner, `{colors.ink-03}` skeletons) | `{motion.duration-emphasis}` 450ms per rotation, infinite while pending; sweep 320ms | linear / `{motion.ease-standard}` | `transform: rotate()`, `opacity` | Rotation and sweep stop; static labelled indicator remains |

`transform` and `opacity` only; `width`, `height`, `top`, `left`, `margin` excluded by rule. Every exit is shorter than its entrance. The hero gradient wash is explicitly static — the one place an ambient loop would be tempting, and the file calls it "barely visible", so a drift would make the quietest element the busiest.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, lines 152–156 (`colors` filter) and 183–197 (`check_all`) | The colour dict keeps only `#rgb`/`#rrggbb`/`#rrggbbaa` values, so any token stated as `rgba(...)` is invisible to every contrast check. In this file that silently hides two genuine failures — `ink-40` at 2.44:1 and `ring-brand` at 1.78:1 — and a brand whose whole palette is opacity-derived (which is exactly what Lovable's own Overview describes) could score a clean 5 while having no measurable boundary anywhere. | Composite `rgba(r,g,b,a)` over the resolved `canvas` token before measuring, and record the composited hex in the result so the agent's report and the harness agree. Failing that, flag `rgba(...)` colour values as `unmeasured_colors` in the JSON so they cannot pass unexamined. |
| `theme-audit/audit.py`, line 360 (`disclosed`) | A failure is disclosed if *any* Accessibility line containing the token's name states a matching ratio. With `hairline` and `hairline-strong` both present, the substring match makes the two names interchangeable, so a file could disclose the wrong one's ratio and still clear the check. | Match the token name on a word boundary (`\b<name>\b`) rather than as a bare substring. |
| `theme-audit/SPEC.md`, section 3, line 121 | The section contract gives a required set but no required *order*, while brief F mandates that `## Motion & Animation` follow `## Components`. For the ten legacy files, whose original order differs from the SPEC table's, this leaves the correct placement of every other section undefined. | State in SPEC section 3 that the table's row order is the required document order. |

### Needs approval

Three frozen brand values fail their threshold. None has been changed; all three are stated plainly in the file's Accessibility section with their measured ratio.

1. **`hairline` #eceae4 on `canvas` #f7f4ed — 1.10:1, needs 3.0:1 (WCAG 1.4.11).**
   - Nearest passing value: **#8a8884** (3.22:1), which is `#1c1c1c` at 50% over cream and is already in the file as the prescribed `hairline-strong`.
   - Usage note that makes the real value defensible: #eceae4 is acceptable wherever the boundary is decorative and the content is identifiable without it — card containment, image outlines, dividers, the footer container. It is **not** defensible on `text-input`, `ai-chat-input` or `suggestion-pill`, where the fill is the same #f7f4ed as the page and the hairline is the sole indication that a control exists. Those three need `hairline-strong`.
   - Recommendation: keep #eceae4 as the documented brand value, scope it to decoration in prose (done), and apply `hairline-strong` to control boundaries only. Approval needed because it changes how two documented components render.

2. **`ink-40` rgba(28,28,28,0.4) -> #9f9e99 on cream — 2.44:1, needs 3.0:1.**
   - Nearest passing value: the same charcoal at **0.5 opacity** -> #8a8884, 3.22:1. A one-stop change within the brand's own opacity ladder, which is the least invasive fix available for an opacity-derived palette.
   - Usage note: 2.44:1 is defensible where the border is accompanied by a text label at 4.5:1 or better and is not the only affordance — which describes `button-ghost`, whose label is `ink` at 15.51:1. It is not defensible on an icon-only control, where the border *is* the control.
   - Recommendation: raise interactive borders to 0.5 and leave passive ones alone. Approval needed because the file's Don'ts explicitly fix the two-tone border system.

3. **`ring-brand` rgba(59,130,246,0.5) — 1.78:1 on cream, 2.10:1 on the dark button, needs 3.0:1.**
   - Nearest passing value: **#3b82f6** at full opacity — 3.35:1 and 4.63:1. Same hue, same Tailwind blue, no new colour.
   - Usage note: there is no usage at which 1.78:1 is defensible for a focus indicator. WCAG 2.4.11/1.4.11 admit no size or context exemption for the sole keyboard-focus signal, and the brand pairs it with a 12px rgba(0,0,0,0.1) shadow that is not measurable either.
   - Recommendation: this one should be fixed in the product, not merely documented. **This is the only item here I would call a defect rather than a trade-off.** Approval needed because the file's own Don'ts say "don't use sharp focus outlines" — the prescribed ring deliberately contradicts a documented brand rule, and keeps `{shadow.focus-soft}` alongside it so the warm glow survives.

Also for approval, lower stakes:

4. **Tap targets.** Declared button height is ~40px against a 44 × 44 minimum. The proposed fix is an invisible 44px hit area around the 40px visual box, which leaves the brand's compact 8px/16px padding untouched. Not applied — it is an implementation note, and per SPEC's honest-limits clause no rendered size can be verified from a document.

### Identity verdict

**The file still reads as Lovable, and the two places it could have drifted were the two I had to think hardest about.**

The first was the accent role. The token contract wants an `accent`, and Lovable's Don'ts say "don't introduce saturated accent colors — the palette is intentionally warm-neutral". Inventing a chromatic accent to fill the slot would have been the single fastest way to turn this into a generic file. `accent` is filled by `primary` #1c1c1c, the charcoal CTA, because that is genuinely where this brand puts its signal, and the Colors section now says so in a short note rather than leaving a reader to wonder why the accent is black.

The second was the focus ring, where a required addition contradicts a documented brand rule ("don't use sharp focus outlines"). The resolution keeps `{shadow.focus-soft}` — the brand's real warm diffused glow — and adds the measurable ring alongside it rather than in place of it. The Accessibility section says explicitly that the soft shadow stays and only stops being the *only* signal.

On the profile: **Playful is correct, and I nearly argued otherwise.** The usual Playful tell — saturated colour on interactive elements — is absent by brand rule, and a careless reading of SPEC's assignment rule 3 ("saturated multi-colour or illustration-led") would send this to Calm. But the rule's own test is "whether saturated colour appears on interactive elements **and** whether the type voice is light and informal", and the second half is decisive here. The file describes its own typeface as having "humanist warmth", "slightly rounded terminals" and "organic curves"; it uses the full pill extensively on action and toggle buttons; the hero carries a multi-colour gradient wash; and the documented press feedback is `opacity 0.8` applied, in the file's words, "for responsive tactile feedback". That is a friendly system. Unlike a genuinely editorial file, nothing here says "sober", the display weight is 600 rather than 400, and gradients are used rather than forbidden. What the restraint changes is amplitude, not timing: `ease-enter` keeps its overshoot, but travel is capped at 8px and press scale stops at 0.98, because a depth model whose whole point is "pressed into the paper rather than hovering above it" cannot have elements leaping off the page. That qualification is stated in the motion section itself, not hidden here.

The prose is the original author's throughout. I renamed headings, moved two blocks, and added token references; I did not rewrite a paragraph. The opacity-derived palette — the thing that actually makes this file distinctive — survives conversion intact as `ink-83` through `ink-03`, stated as `rgba(...)` rather than flattened to invented hexes.
