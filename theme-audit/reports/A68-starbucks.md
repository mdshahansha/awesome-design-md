## A68 · starbucks

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 1 | 5 |
| refs | 1 | 5 |
| contrast | 1 | 5 |
| sections | 1 | 5 |
| motion | 3 | 5 |
| states | 1 | 2 |

Before: `1 · 1 · 1 · 1 · 3 · 1`. After: `5 · 5 · 5 · 5 · 5 · 2`.

This was one of the ten legacy files: no frontmatter token block, numbered headings
(`## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide`). The before-scores of 1
on refs and contrast are the no-frontmatter floor, not a measurement — nothing in the file
was machine-checkable. States stays at 2 deliberately: hover, disabled and loading are
absent from the source and were left unfilled rather than invented.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | J, A | whole file | No frontmatter token block at all. Every colour, type, spacing, radius, shadow and component value existed only as prose, so none of it was addressable or measurable. Converted: 26 colours, 12 typography roles, 15 spacing steps, 6 radii, 6 shadows, 36 components, all built from values already written in the file. |
| P0 | J, section contract | headings | Numbered legacy headings; `Shapes`, `Motion & Animation` and `Accessibility` absent entirely; `Known Gaps` buried as a `###` inside `## 9. Agent Prompt Guide`. All twelve required sections now present, in the SPEC order. |
| P0 | F | whole file | No motion system. The file carried four extracted fragments (`all 0.2s ease`, `300ms` expander, `cubic-bezier(0.32, 2.32, 0.61, 0.27)` checked-input, `opacity 0.3s ease-in` image fade) and two unexplained var names, with no tokens, no table and no reduced-motion rule. |
| P0 | A, G | focus | No focus ring anywhere in the file, for any control, and the brand has two signature polarities, so one ring cannot serve. Two prescribed rings added, both reusing extracted tones. |
| P0 | B, E | `border-input` #d6dbde | At **1.40:1 on white** and 1.23:1 on cream, the sole visible edge of the floating-label field, the Add-in/Milk select and the stepper buttons. A real AA failure of the live brand, previously undisclosed. |
| P0 | G | whole file | No accessibility statement of any kind: no measured ratio, no tap-target note, no reduced-motion note, and therefore no disclosure of any of the failures above. |
| P1 | A, B | `#d6dbde`, `#e7e7e7` | Both boundary tones appeared **only inside component specs**; the colour list omitted them, so the file's own palette section never admitted it had borders. Tokenised and measured. |
| P1 | A, B | `rgb(0, 130, 72)` | A second filled-CTA green, stated only inside the cookie-consent component spec and never listed in the palette. At 4.90:1 with white it is the tightest filled-button pair in the system — one step from failing. Tokenised as `{colors.green-consent}`. |
| P1 | B | `warning` #fbbc05 | 1.50:1 on the canvas, 1.71:1 on white. Declared as "Warning state" with no note that it cannot carry text on any surface this file defines. |
| P1 | B | `gold` #cba258 | 2.08:1 on the canvas and 2.20:1 on its own `surface-gold-wash` partnership band. Legible only on the two dark grounds (5.25:1 on House Green). The file described Gold-tier "callouts" without saying which ground they sit on. |
| P1 | H | every component | hover, disabled and loading documented nowhere, for any component; focus named once (the Add-in select's border shift); selected named once (the size ring); error only as a tint token. Coverage is now marked per state, not filled. |
| P1 | C | canvas / surface / ceramic | The elevation ladder is carried **entirely by shadow**: white card against cream canvas is 1.14:1, ceramic against canvas 1.04:1, the Account dropdown against the white nav 1.05:1 — and the source's own words for the dropdown are "no border — just background surface shift". The file never stated that removing a shadow removes the layer. Measured and stated in Accessibility. |
| P1 | D | `{typography.rewards-serif}`, `{typography.careers-script}` | Both secondary typefaces are named with no size, weight or line height anywhere in the file. The ten primary roles all carry size, weight and line height. |
| P1 | D | letter-spacing | The file states tracking two ways and never reconciles them: `-0.16px` in the hierarchy table and `-0.01em` in the token list. At 16px these are not the same value. Both recorded on the entries they belong to; flagged in Known Gaps. |
| P1 | I, J | PDP cluster | The size selector and the breadcrumb are described twice, inconsistently: the component spec puts them on a light ground (Starbucks Green / Text Black Soft), the agent prompt puts them in white on the House Green band. The ground is genuinely unresolved; the component spec's reading is tokenised and the conflict recorded. |
| P1 | D, J | PDP cluster | "Proxima Nova" is named in five PDP component specs although the typography section states SoDoSans is universal and never mentions it. Almost certainly a fallback caught mid-font-load; no `proxima` token was created. |
| P1 | A | `shadow:` | Six real shadow values were documented in prose with no token to reference, including the `--svcShadowFilter` SVG drop-shadow pair. `shadow:` group added, as SPEC section 1 requires for a file with real shadow values. |
| P2 | C | SVC / gift cards | Elevation is otherwise expressed one consistent way — stacked 2–3 low-alpha box-shadows — but the Starbucks-Card visuals use SVG `drop-shadow()` filters instead. Extracted, kept, and labelled as the one deviation. |
| P2 | E | `{rounded.svc}` | `3.3333%/5.298%` sits outside the 4 / 12 / 50px / 50% ladder. The source already labels it "Specialty"; it describes an illustrated card mockup, not a UI container. Left as extracted, with the ladder's consistency now stated in Shapes. |
| P2 | H | Rewards tiers | A "colored gradient/color header ring" per tier with no hex for any of Bronze, Gold or "Silver-ish" — the third tier is not even named. No tier tokens exist. |
| P2 | B | gift-card tile | Radius and shadow are hedged in the source itself ("`~12px`, slightly tighter"; "lighter than default card"). Recorded as the card radius and no shadow token rather than inventing a second value. |
| P2 | G | tap targets | The file computes ~32px for the default pill from `7px 16px` padding and says mobile padding "may be visually expanded to meet the minimum" without saying to what. Kept as the document's own arithmetic and explicitly **not** presented as a measurement — SPEC's honest-limits rule forbids a tap-target claim from a document. |
| P2 | section contract | Iteration Guide | Remains a `###` inside the preserved Agent Prompt Guide rather than a top-level section. Optional per SPEC section 3, so it costs nothing and the legacy block stays verbatim. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| top of file | no frontmatter -> `colors` (26), `typography` (12), `spacing` (15), `rounded` (6), `shadow` (6), `motion` (10), `components` (36) | SPEC section 1. Every value is one already written in the prose; nothing invented. |
| `colors:` | — -> `canvas` #f2f0eb, `surface` #ffffff, `text` rgba(0,0,0,0.87), `text-dim` rgba(0,0,0,0.58), `border-input` #d6dbde, `accent` #00754A, `on-accent` #ffffff | The eight required roles, each bound to the tone the prose already gives that job. No alias was added for any of them. |
| `colors.focus` / `colors.focus-on-dark` | — -> `#00754A` / `#ffffff` | No file in the repo defines a ring. Two are needed because the file documents both cream/white and House Green/Black signature grounds: `{colors.focus}` reaches only 2.16:1 on House Green. Both reuse extracted tones — Green Accent is the one focus response the source documents, white is already the ink on every dark ground. Gold was rejected because the brand's own Don'ts forbid Gold as a general-purpose accent. |
| `colors.green-consent` | — -> `#008248` | Extracted from the consent component's `rgb(0, 130, 72)`; it is a second filled-CTA green and had to be measurable as one. |
| `colors.border-input`, `colors.border-hairline` | — -> `#d6dbde`, `#e7e7e7` | Both existed only inside component specs. |
| `## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide` | numbered -> `## Overview`, `## Colors`, `## Typography`, `## Layout`, `## Elevation & Depth`, `## Shapes`, `## Components`, `## Do's and Don'ts`, `## Responsive Behavior` | SPEC section 3 heading set and order. |
| `### Border Radius Scale` (inside Layout) | Layout subsection -> `## Shapes` with the table moved verbatim, heading promoted | Shapes was absent; the radius ladder is its content and already existed. |
| `## Shapes` | — -> two added paragraphs on radius-ladder and border-width consistency | Dimension E. Both ladders are built from values already in the file (4/12/50px/50%; 1px/1.5px/2px). |
| `## Colors` | 22 colour bullets -> same bullets with a `{colors.*}` reference added before each hex | Makes the palette addressable; no prose reworded. |
| `## Colors` | — -> `### Borders` and `### Focus` subsections | Documents the two hairlines, scopes them to decoration, names the two extracted tones that carry a perceivable boundary instead, and states both rings as prescribed. |
| `## Components` | — -> `### Interaction States` | Marks all eight contract states: five extracted or prescribed, three recorded as absent. |
| after `## Components` | — -> `## Motion & Animation` | SPEC sections 4–6. First line states the system is prescribed and unmeasured; Playful block verbatim; 14-row interaction table; `prefers-reduced-motion` block. |
| after Motion | — -> `## Accessibility` | 31 measured pairs, a layer-separation table, a manufactured-pairs table, ring coverage on all ten surfaces, tap target, reduced motion. |
| `### Known Gaps` | `###` inside the Agent Prompt Guide -> top-level `## Known Gaps` with the conversion record and 14 new gap entries; the original six bullets kept verbatim under `### Gaps stated in the original document` | Required section; the extracted gaps are facts and were not rewritten. |
| `## 9. Agent Prompt Guide` | — -> kept verbatim as `## Agent Prompt Guide` after Known Gaps | SPEC section 3: a legacy section with no slot in the contract is preserved, not folded away. |
| `## Do's and Don'ts` | — -> 3 Do and 3 Don't lines on boundaries, focus and motion | The new rules need to be enforceable in the same place as the rest. |
| `components.button-outlined-on-dark`, `components.button-dark-outlined` | `backgroundColor: transparent` -> the ground each is actually drawn on (`green-house`, `surface`) | A transparent fill states no ground, so the harness measured a white outline against the cream page it never appears on. SPEC section 1 asks for the declared pair where the prose names the ground. |

### Contrast checks

All computed with WCAG 2.1 relative luminance; translucent inks composited over the ground
they are drawn on first.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `text` rgba(0,0,0,0.87) → #1f1f1f / `canvas` #f2f0eb | 14.47:1 | 4.5:1 | Pass |
| `text` → #212121 / `surface` #ffffff | 16.10:1 | 4.5:1 | Pass |
| `text` → #202020 / `surface-cool` #f9f9f9 | 15.48:1 | 4.5:1 | Pass |
| `text` → #1f1f1e / `surface-ceramic` #edebe9 | 13.87:1 | 4.5:1 | Pass |
| `text` → #20201f / `surface-gold-wash` #faf6ee | 15.13:1 | 4.5:1 | Pass |
| `text-dim` rgba(0,0,0,0.58) → #666563 / `canvas` | 5.11:1 | 4.5:1 | Pass |
| `text-dim` → #6b6b6b / `surface` | 5.33:1 | 4.5:1 | Pass |
| `text-dim` → #646362 / `surface-ceramic` | 5.04:1 | 4.5:1 | Pass (narrowest in the text system) |
| `text-white` #ffffff / `green-house` #1E3932 | 12.45:1 | 4.5:1 | Pass |
| `text-white-soft` → #bcc4c2 / `green-house` | 7.00:1 | 4.5:1 | Pass |
| `text-white` / `black` #000000 | 21.00:1 | 4.5:1 | Pass |
| `on-accent` #ffffff / `accent` #00754A | 5.76:1 | 4.5:1 | Pass |
| `text-white` / `green-consent` #008248 | 4.90:1 | 4.5:1 | Pass (tightest filled pair) |
| `green-starbucks` #006241 / `canvas` | 6.53:1 | 4.5:1 | Pass |
| `green-starbucks` / `surface` | 7.44:1 | 4.5:1 | Pass |
| `accent` #00754A / `canvas` | 5.06:1 | 4.5:1 | Pass |
| `accent` / `surface` | 5.76:1 | 4.5:1 | Pass |
| `accent` / `surface-ceramic` | 4.85:1 | 4.5:1 | Pass |
| `rewards-green` #33433d / `canvas` | 9.17:1 | 4.5:1 | Pass |
| `rewards-green` / `surface-gold-wash` | 9.69:1 | 4.5:1 | Pass |
| `error` #c82014 / `canvas` | 5.02:1 | 4.5:1 | Pass |
| `error` / `surface` | 5.72:1 | 4.5:1 | Pass |
| `gold` #cba258 / `green-house` | 5.25:1 | 4.5:1 | Pass |
| `gold` #cba258 / `canvas` | 2.08:1 | 4.5:1 | **Fail — real brand failure, disclosed** |
| `gold` / `surface-gold-wash` | 2.20:1 | 4.5:1 | **Fail — real brand failure, disclosed** |
| `gold-light` #dfc49d / `canvas` | 1.47:1 | 4.5:1 | Fail by name only — documented as a wash, never an ink |
| `warning` #fbbc05 / `canvas` | 1.50:1 | 4.5:1 | **Fail — real brand failure, disclosed** |
| `warning` / `surface` | 1.71:1 | 4.5:1 | **Fail — real brand failure, disclosed** |
| `border-input` #d6dbde / `surface` | 1.40:1 | 3:1 | **Fail — frozen extracted boundary, disclosed** |
| `border-input` / `canvas` | 1.23:1 | 3:1 | **Fail — frozen, disclosed** |
| `border-input` / `surface-ceramic` | 1.17:1 | 3:1 | **Fail — frozen, disclosed** |
| `border-hairline` #e7e7e7 / `surface` | 1.24:1 | 3:1 | **Fail — frozen, disclosed** |
| `border-hairline` / `canvas` | 1.09:1 | 3:1 | **Fail — frozen, disclosed** |
| `border-hairline` / `surface-ceramic` | 1.04:1 | 3:1 | **Fail — frozen, disclosed** |
| `accent` as a boundary / `surface` | 5.76:1 | 3:1 | Pass — the perceivable boundary the palette already owns |
| `text` → #212121 as a boundary / `surface` | 16.10:1 | 3:1 | Pass — the Sign-in button's extracted stroke |
| `focus` #00754A ring / `canvas` | 5.06:1 | 3:1 | Pass |
| `focus` / `surface` | 5.76:1 | 3:1 | Pass |
| `focus` / `surface-cool` | 5.47:1 | 3:1 | Pass |
| `focus` / `surface-ceramic` | 4.85:1 | 3:1 | Pass |
| `focus` / `surface-gold-wash` | 5.35:1 | 3:1 | Pass |
| `focus` / `green-light` #d4e9e2 | 4.54:1 | 3:1 | Pass |
| `focus` / `green-house` | 2.16:1 | 3:1 | Fail — the reason a second ring exists |
| `focus-on-dark` #ffffff / `green-house` | 12.45:1 | 3:1 | Pass |
| `focus-on-dark` / `black` | 21.00:1 | 3:1 | Pass |
| `focus-on-dark` / `green-uplift` #2b5148 | 8.85:1 | 3:1 | Pass |
| layer: `surface` / `canvas` | 1.14:1 | — | Not a WCAG pair; the white card exists only because `{shadow.card}` does |
| layer: `surface-ceramic` / `canvas` | 1.04:1 | — | Zone separator, read as temperature not edge |
| layer: `surface-cool` / `surface` | 1.05:1 | — | The Account dropdown's only separation, with "no border" by the source's own description |
| layer: `green-house` / `canvas` | 10.93:1 | — | The one strong layer step in the system |

### Motion inventory

Prescribed **Playful** profile, stated as prescribed in the section's first line. Two
extracted timings are kept in preference to the profile value, with the reason given in the
file. `transform` and `opacity` only.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (prescribed; none documented) | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `opacity`, `transform: scale(1.02)` on cards | Travel and scale removed; opacity at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-base}` 200ms | `{motion.ease-standard}` | `transform: scale(0.95)` — extracted; Frap also fades its ambient shadow | Scale removed; shadow fade at `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` of the ring | Instant, never suppressed |
| Page / route transition | `{motion.duration-slow}` 320ms | `{motion.ease-enter}` | `opacity`, `translateY(16px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `translateX(-100%)`→0 (drawer), `scale(0.97)`→1 (modal) | Travel and scale removed; scrim fades |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown enter / exit | `{motion.duration-fast}` / `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(-8px)`→0 | Travel removed; fade |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(12px)`→0 | Travel removed; fade |
| List enter (gift-card grid, menu tiles, Rewards panels) | `{motion.duration-base}`, stagger `{motion.stagger-step}` 60ms | `{motion.ease-enter}` | `opacity`, `translateY(12px)`→0 | Stagger and travel removed; one fade |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade |
| Expander / accordion (FAQ) | 300ms — **extracted**, kept | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` — extracted | `opacity` plus `transform: scaleY()`; must not animate `height` | Opens with no transition; content fades at `{motion.duration-reduced}` |
| Floating-label rise | `{motion.duration-fast}` | `cubic-bezier(0.32, 2.32, 0.61, 0.27)` — **extracted** overshoot | `translateY(-12px) translateY(-50%)`, `opacity` | Travel removed; label snaps |
| Image load | 300ms — **extracted** | `ease-in` — extracted | `opacity` 0→1 | Kept, capped at `{motion.duration-reduced}` |
| Loading | 1200ms, infinite | linear | `opacity` pulse on a `{colors.surface-ceramic}` placeholder | Frozen; static placeholder remains |

Profile verdict: **Playful is correct and the file's own extracted values argue for it** —
`transform: scale(0.95)` on every pill (the profile's "small scale pops on press", named by
the document as "the signature micro-interaction"); `cubic-bezier(0.32, 2.32, 0.61, 0.27)`
on the checked input, a literal overshoot curve; and `all 0.2s ease`, which is already
`{motion.duration-base}` to the millisecond. Saturated green sits on the interactive
elements (CTAs, Frap, selected-size ring) rather than behind them, and the type voice runs
to a handwritten script for cup names. No switch argued.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 297–317 | The surface role is resolved to the surface-pattern tone **nearest the canvas**, which here picks `surface-ceramic` (#edebe9) — a page-section wash the prose describes as a zone separator — over `surface` (#ffffff), the card tone that `{components.card}`, `{components.modal}` and every input actually bind. Six hairline ratios are then measured against a ground those components never render on. | Prefer a tone that a container component declares as `backgroundColor` over a bare name match, as the existing `if not roles.get("surface")` fallback at line 236 already does; only fall back to nearest-the-canvas when no component binds any surface-pattern tone. Disclosed as manufactured in the file's Accessibility section. |
| `theme-audit/audit.py` lines ~390–412 (`bound_borders`) | A `borderColor` equal to its own `backgroundColor` is reported as a 1.00:1 boundary failure. This brand states `1px solid #00754A` on a `#00754A` fill, `1px solid #000000` on black and `1px solid #ffffff` on white — the borders exist to equalise filled and outlined pill box dimensions and are deliberately invisible. Three artefact failures. | Skip the pair when the resolved border hex equals the component's own declared ground hex. Disclosed as manufactured in the file meanwhile. |
| `theme-audit/audit.py` line ~669 (`structured`) | The structured-line filter accepts any line matching `\*\*[^*]+\*\*\s*[:—-]`, which matches a bold phrase mid-paragraph. An explanatory sentence that merely mentions a state word therefore counts as documentation of that state: my first draft scored `hover` from the sentence "a fabricated hover tint would be a worse outcome than a gap". | Anchor the pattern to the start of the line (`^\s*\*\*`), so only a bold label leading a line counts. |
| `theme-audit/audit.py` | The file was edited by other agents three times while this review ran (`dd934af`, `b805d65`, `f8b785f`), and the surface role resolved differently before and after. Not a defect, but after-scores in these reports are only comparable at a fixed harness revision. | Record the harness commit alongside each report's after-scores. |

### Needs approval

1. **Re-binding the form field's boundary.** `{colors.border-input}` #d6dbde is extracted and
   frozen, and it is the only visible edge of every text input, select and stepper at 1.40:1
   on white. Per SPEC section 2 step 3 the extracted bindings are left exactly as they are
   and the question is raised here. Nearest passing value in the same cool-grey family:
   **#929597** (3.01:1 on white) or **#878a8c** (3.05:1 on the cream canvas). The alternative,
   which adds nothing to the palette, is to re-point the field to `{colors.accent}` (5.76:1)
   or `{colors.text}` (16.10:1) — both already extracted as control strokes elsewhere in this
   same file. A brand owner has to choose; I did not.
2. **`{colors.border-hairline}` #e7e7e7 on the nutrition table**, 1.24:1 on white. Defensible
   as decorative separation in a table that also separates by position and alignment, which
   is how I have scoped it. If it is ever the sole separator, the nearest passing value is
   **#949494** (3.03:1 on white).
3. **`{colors.warning}` #fbbc05 as a text colour.** Usage note that makes the real value
   defensible: yellow is a chip, icon or band fill with `{colors.text}` drawn on it, never a
   label colour. If a yellow *label* is required, **#8a6703** reaches 4.58:1 on the canvas,
   and **#ad8203** reaches 3.09:1, which is enough at 18.66px/700 or 24px+.
4. **`{colors.gold}` #cba258 as a text colour on light grounds**, 2.08:1 on canvas and 2.20:1
   on its own partnership wash. It passes on House Green (5.25:1), which is where the Rewards
   Cost Pill actually sits. For Gold-tier callouts on a light ground, **#846939** reaches
   4.54:1 on the canvas and **#a68548** reaches 3.04:1 for 18.66px/700+ headings. Keeping the
   real gold and restricting it to dark grounds is the option I would take, but it narrows
   where Rewards ceremony can appear and so is a brand decision.
5. **The expander's animated property.** The source gives the accordion a `300ms`
   `cubic-bezier(0.25, 0.46, 0.45, 0.94)` transition but never says what it animates; a real
   FAQ accordion almost certainly animates `height`, which SPEC section 6 forbids outright. I
   have specified `transform: scaleY()` plus `opacity` and said it must not animate `height`.
   If the live site does animate height, the file now documents a correction rather than the
   brand, and someone should decide which the document is for.
6. **The self-coloured 1px borders on the filled pills.** Extracted facts
   (`1px solid #00754A` on a `#00754A` fill, and the same pattern in black and white) that
   produce three 1.00:1 artefact failures in the harness. I kept them declared and disclosed
   them as manufactured. Dropping the `borderColor` line from those three components would
   silence the artefact at the cost of an extracted fact.

### Identity verdict

Still unmistakably Starbucks, and in one respect more so than before. The things that make
this file specific all survived in place: the four-tier green system with each tier bound to
its own surface role, Gold fenced off for Rewards ceremony, the warm-cream canvas held
against pure white, the 50px pill on every button without exception, the `scale(0.95)` press,
the 56px Frap with its stacked shadow, the three-typeface discipline, the gift cards as
photographed physical objects, and the espresso-dark bookend of House Green bands around a
bright body. The 264-line Components section is untouched prose. The whole Agent Prompt
Guide is preserved verbatim, including its ten worked prompts.

What the conversion added reads as this brand rather than as the audit: the focus rings reuse
Green Accent and white instead of introducing a chromatic ring; Gold was explicitly rejected
as a ring because the brand's own Don'ts forbid it; and the motion profile is argued from
three values the file already contained, not asserted. The one genuine drift risk was the
`Interaction States` subsection, which is the most generic-looking block in the file — it is
kept short, and three of its eight rows say the state does not exist here rather than filling
in a plausible hover tint.

The sharpest new fact about the brand is one the original file obscured: Starbucks' text
system is excellent on every surface it defines, and its weakness is entirely in the
boundaries. Three of its layers sit within 1.14:1 of each other and the two hairlines that
should separate them are invisible, so the whole elevation ladder rests on whisper-soft
shadows that the file's own Do's tell you to keep soft.
