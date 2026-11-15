## A72 · tesla

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 1 | 5 |
| refs | 1 | 5 |
| contrast | 1 | 5 |
| sections | 1 | 5 |
| motion | 1 | 5 |
| states | 1 | 3 |

Every harness claim in the brief was confirmed before editing: no frontmatter at all, all twelve required sections absent under the numbered-heading variant, all eight colour roles unresolved, all eight states unseen. `refs` and `contrast` scored 1 by construction — with no frontmatter there was nothing to resolve or measure, so those two ones were floors, not findings.

`states` stays at 3 on purpose. `pressed` and `selected` are recorded nowhere in the source, including for the carousel dots, where the real site must mark a current slide and the document does not say how. Both are left unfilled and named in Known Gaps rather than invented for the column.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | J — format | whole file | Legacy format: no frontmatter token block, numbered headings (`## 1. Visual Theme & Atmosphere` …). Nothing was machine-readable; every colour, type value and component sat in prose only |
| P0 | A — token contract | all 8 colour roles | No `colors`, `typography`, `spacing`, `rounded`, `components` or `motion` group existed |
| P0 | F — motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. The file's only motion facts (0.33s / 0.25s, one cubic-bezier) were buried in component prose |
| P0 | G — accessibility | whole file | No `## Accessibility` section; no ratio stated anywhere in a file that ships a 3.28:1 placeholder tone |
| P0 | A — focus | focus ring | No focus colour defined. The primary CTA reserves a 3px transparent border and a zero-alpha 2px inset shadow that "animates to visible on focus" — a focus mechanism with no colour |
| P1 | B — colour | Silver Fog `#8E8E8E` | 3.28:1 on the canvas, 2.98:1 on Light Ash. Bound by the source to **placeholder** text as well as disabled text, so it is a real AA failure, not an exempt disabled tone. Frozen and disclosed |
| P1 | B/E — borders | Cloud Gray `#EEEEEE`, Pale Silver `#D0D1D2` | 1.16:1 and 1.53:1 on the canvas; 1.05:1 and 1.39:1 on Light Ash. The palette owns **no** tone that can carry a perceivable boundary. Re-scoped to decoration; `{colors.text-dim}` (6.50:1) named for any boundary that must be seen. Nothing invented |
| P1 | H — states | every component | The source named hover for a few components and active for two. Each entry now states what it documents and, on a separate line, what it does not |
| P1 | G — tap target | primary CTA, nav button | The source asserts 200×40px is "well above 44×44px WCAG". It is below it on the vertical axis, as is the 32px nav button. Corrected in both Accessibility and Responsive Behavior; not measurable as rendered, so stated as the source's own figures |
| P2 | C — elevation | Level 0–3 ladder | Expressed consistently by alpha, **except** Level 3 `rgba(0,0,0,0.05)`, which contradicts the file's own Don't ("Add shadows to any element"). Kept as extracted, labelled a vestige |
| P2 | C — elevation | canvas vs Light Ash | 1.10:1 — the two light surfaces are not distinguishable. Documented as the intent, with the note that spacing and photography, not luminance, do the separating |
| P2 | D — typography | Category Label | No line height recorded and the 16px size is marked "(est.)" in the source. Token omits `lineHeight`; the estimate is flagged |
| P2 | D — typography | Promo Text | 22px against a 20px line height (0.91) — a sub-1.0 line height. Carried as extracted, flagged as a likely measurement artefact |
| P2 | A — tokens | "teal/blue icon accent" | The chat bar's Schedule CTA icon has no hex, and a teal would be a second chromatic value in a one-accent system. No token created; recorded in Known Gaps |
| P2 | E — radius | 0 / 4 / 12 / 50% | Internally consistent, nothing off-scale. The 3px CTA border is a reserved-space device, not a border ladder — stated, since there is no other border width in the file |
| P2 | I — identity | file voice | Prose kept verbatim wherever it was not being fixed; tokens inserted into existing sentences. The one-blue, no-shadow, photography-first voice survives |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Top of file | no frontmatter -> `colors` (15), `typography` (8), `spacing` (4), `rounded` (4), `shadow` (3), `motion` (12), `components` (17) | Legacy conversion (dimension J). Every value read from the file's own prose |
| Headings | `## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide` -> unnumbered SPEC set in contract order | Section contract. Order: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Motion & Animation → Accessibility → Do's and Don'ts → Responsive Behavior → Known Gaps |
| `## 5. Layout Principles` → `### Border Radius Scale` | moved verbatim -> new `## Shapes` | Shapes is required and the radius table was its only content; moved, not duplicated |
| `## 9. Agent Prompt Guide` | numbered section -> unnumbered `## Agent Prompt Guide` kept verbatim **after** Known Gaps | No slot in the contract; content is extracted, so deleting or folding it would be a regression. Its `### Iteration Guide` subsection stays inside it |
| Colors section | bare hexes -> `{colors.*}` refs beside the same hexes and the same names | Reference integrity; prose otherwise untouched |
| Colors → new `### Borders` | (absent) -> both hairlines scoped to decoration, with measured ratios and `{colors.text-dim}` named for real boundaries | Frozen tones doing a contrast job: SPEC step 1 — the palette already owns a passing tone, so nothing was added |
| Colors → new `### Focus` | (absent) -> `focus: #3E6AE1`, prescribed, reusing the brand's own Electric Blue | The one role SPEC allows to be bound. One ring, not a pair: 4.82 / 4.39 / 3.61:1 across all three surfaces |
| `## Components` | prose with no state coverage -> each entry lists states recorded and, on a separate line, states not documented | Dimension H, honestly: the "not documented" lines are excluded from the harness's own state haystack by design |
| New `## Motion & Animation` after Components | (absent) -> Cinematic block verbatim + 11-row interaction table + reduced-motion CSS | Dimension F |
| `motion:` group | — -> Cinematic profile verbatim, **plus** `duration-extracted-state: 330ms` and `ease-extracted-state: cubic-bezier(0.5, 0, 0, 0.75)` | The ten profile values are untouched. The two extras are the only real motion facts the source records; an extracted fact outranks a prescribed one, and the deviation is stated in the section |
| New `## Accessibility` | (absent) -> 16 key pairs, 10 component pairs, 5-surface focus-ring table, tap targets, reduced motion | Dimension G |
| `## Do's and Don'ts` | 10 + 10 -> 11 + 12, existing items untouched except token refs | Added the two facts a builder needs: reach for `text-dim` when a muted element must be seen; never let either hairline be a control's only boundary |
| Touch Targets | "well above 44×44px WCAG requirement" -> states 40px and 32px are below 44px | The source's own arithmetic was wrong |
| New `## Known Gaps` | (absent) -> conversion losses + 11 genuinely missing values | Nothing was invented to fill a hole |
| `components:` photography entries | `backgroundColor: <photography>` -> `backgroundColor: transparent` + `backgroundImage: full-bleed photography — no measurable colour` | A non-hex background fell through to the canvas and manufactured two white-on-white failures. The image is a background *image*; the element's background-color is genuinely transparent |

### Contrast checks

All computed with WCAG 2.1 relative luminance via `python3` from the hexes now in the file's frontmatter.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #171A20 / `canvas` #FFFFFF | 17.43:1 | 4.5:1 | Pass |
| `ink` #171A20 / `surface-ash` #F4F4F4 | 15.84:1 | 4.5:1 | Pass |
| `body` #393C41 / `canvas` | 11.07:1 | 4.5:1 | Pass |
| `body` #393C41 / `surface-ash` | 10.07:1 | 4.5:1 | Pass |
| `text-dim` #5C5E62 / `canvas` | 6.50:1 | 4.5:1 | Pass |
| `text-dim` #5C5E62 / `surface-ash` | 5.91:1 | 4.5:1 | Pass |
| `muted-placeholder` #8E8E8E / `canvas` | 3.28:1 | 4.5:1 | **Fail — real brand failure, disclosed** |
| `muted-placeholder` #8E8E8E / `surface-ash` | 2.98:1 | 4.5:1 | **Fail — real brand failure, disclosed** |
| `on-accent` #FFFFFF / `accent` #3E6AE1 | 4.82:1 | 4.5:1 | Pass (0.32 of margin) |
| `accent` #3E6AE1 / `canvas` | 4.82:1 | 4.5:1 text, 3:1 non-text | Pass |
| `accent` #3E6AE1 / `surface-ash` | 4.39:1 | 3:1 non-text | Pass as a ring/graphic; **fails 4.5:1 as text on Light Ash**, where the source does not place it |
| `border` #EEEEEE / `canvas` | 1.16:1 | 3:1 | **Fail — frozen decorative hairline, disclosed** |
| `border` #EEEEEE / `surface-ash` | 1.05:1 | 3:1 | **Fail — invisible by construction, disclosed** |
| `border-strong` #D0D1D2 / `canvas` | 1.53:1 | 3:1 | **Fail — frozen, disclosed** |
| `border-strong` #D0D1D2 / `surface-ash` | 1.39:1 | 3:1 | **Fail — frozen, disclosed** |
| `ink-on-image` #FFFFFF / `surface-carbon` #171A20 | 17.43:1 | 4.5:1 | Pass |
| `focus` #3E6AE1 / `canvas` | 4.82:1 | 3:1 | Pass |
| `focus` #3E6AE1 / `surface-ash` | 4.39:1 | 3:1 | Pass |
| `focus` #3E6AE1 / `surface-carbon` | 3.61:1 | 3:1 | Pass |
| `focus` #3E6AE1 / `surface-frost` composited (#FFFFFF) | 4.82:1 | 3:1 | Pass |
| `focus` #3E6AE1 / `overlay-modal` composited (#ACACAC) | 2.12:1 | 3:1 | **Fail at mid grey** — handled by the two-tone ring (white outer edge, 4.82:1 against the blue band) |
| `canvas` #FFFFFF / `surface-ash` #F4F4F4 (layer separation) | 1.10:1 | — | Layers not distinguishable; documented intent |
| `canvas` #FFFFFF / `surface-carbon` #171A20 (layer separation) | 17.43:1 | — | The only real layer jump in the system |
| Component `button-primary` #FFFFFF / #3E6AE1 @14px/500 | 4.82:1 | 4.5:1 | Pass |
| Component `button-secondary` #393C41 / #FFFFFF | 11.07:1 | 4.5:1 | Pass |
| Component `link-text` #5C5E62 / #FFFFFF | 6.50:1 | 4.5:1 | Pass |
| Component `section-ash` #393C41 / #F4F4F4 | 10.07:1 | 4.5:1 | Pass |
| Component `overlay-text-panel` #FFFFFF / #171A20 | 17.43:1 | 4.5:1 | Pass |
| Components `card-category`, `hero-title-overlay`, `hero-promo` over photography | not measurable | 4.5:1 | **Unverifiable from a document** — the source states the label "relies on image darkness" and specifies no scrim |

After the edits the harness reports zero undisclosed failures and zero component failures.

### Motion inventory

Cinematic profile, carried verbatim. `{motion.duration-extracted-state}` = 330ms and `{motion.ease-extracted-state}` = `cubic-bezier(0.5, 0, 0, 0.75)` are the file's only extracted motion facts.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-extracted-state}` (330ms, extracted) | `{motion.ease-standard}` | `opacity` + extracted `background-color` / `border-color` / `color`; no transform (brand rule) | Same crossfade, capped at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` only; no scale pop (brand rule) | Unchanged, already ≤ 150ms |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring and the extracted inset shadow | Instant; never suppressed |
| Page / route transition | `{motion.duration-emphasis}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(24px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(32px)`→0 | Travel removed; scrim fades at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-base}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown (nav panel) enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| List enter | `{motion.duration-base}`, stagger `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px)`→0 | Stagger and travel removed; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading (lazy-loaded section) | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` 0→1 once the image decodes | Fade at `{motion.duration-reduced}`, or none |
| Hero carousel auto-advance (**stated brand ambience**) | `{motion.duration-emphasis}` on a slow interval | `{motion.ease-enter}` | `opacity` between slides, `transform: scale(1)`→`scale(1.03)` | Frozen at `scale(1)`; carousel becomes manual |

Exit is shorter than its entrance in every pair. Only `transform` and `opacity` are animated for travel; the extracted colour and box-shadow transitions stay confined to the interaction rows. One infinite animation, named as ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py:302` | `colors[k] != colors[canvas_key]` compares hex **strings**, so a token whose composited value is `#ffffff` is not recognised as the canvas `#FFFFFF`. For tesla this makes the `surface` role resolve to `surface-frost` (the nav's `rgba(255,255,255,0.75)`, composited to white) instead of `surface-ash` `#F4F4F4`, the only real raised neutral in the file. Consequence here is mild — every "on surface-frost" pair is just the canvas pair again, and all are disclosed — but on a file with a tinted raised surface it would hide the real card tone, exactly the failure mode SPEC section 1 warns about | Normalise before comparing: `colors[k].lower() != colors[canvas_key].lower()`, expanding 3-digit hexes first. Same comparison at line 252 |
| `theme-audit/audit.py:530-549` | A component's `backgroundColor` that is not a token, a hex or `transparent` (a photograph, a video, a gradient) falls through to `bg = canvas`, manufacturing a white-on-white failure for white type over imagery. I worked around it in-file with `backgroundColor: transparent` + `backgroundImage:`, but the next photography-led file will hit it | Treat an unresolvable, non-empty `backgroundColor` as "ground not stated" and skip it, as `transparent` already is |
| `theme-audit/audit.py:467` | `achromatic()` is defined and never called — dead code inside the contrast block | Remove it, or wire it to whatever check it was written for |
| `theme-audit/audit.py:683` (`tokens` score) | A file with no frontmatter scores `max(1, 5 - 8) = 1` on tokens, the same as a file missing one role out of eight after a real attempt. Not wrong, but it compresses the legacy files into the floor | Optionally report `has_frontmatter` alongside the score, as the JSON already does, so the roster can distinguish "not converted" from "converted badly" |

### Needs approval

1. **Re-binding the extracted hairlines.** `{colors.border}` (#EEEEEE, 1.16:1) and `{colors.border-strong}` (#D0D1D2, 1.53:1) are the only boundary tones Tesla's site defines, and neither reaches 3:1 on any surface in this file. Per SPEC I left both bindings as extracted and scoped them to decoration, naming `{colors.text-dim}` (#5C5E62, 6.50:1 on the canvas) for any boundary that must be perceivable. **A brand owner must decide whether real controls — the chat input above all — may be drawn with a 6.50:1 Pewter hairline instead of an invisible one.** Nearest passing values if the grey must stay grey: #949494 (3.03:1 on #FFFFFF) and #8D8D8D (3.02:1 on #F4F4F4).
2. **Silver Fog as placeholder text.** #8E8E8E measures 3.28:1 on the canvas and 2.98:1 on Light Ash. It is defensible unchanged *only* for disabled text, which WCAG exempts. As a placeholder it fails AA at every size this file defines, since nothing here reaches 18.66px/700 or 24px, so the 3:1 large-text allowance never applies. Nearest passing value: #767676 (4.54:1 on #FFFFFF; #707070 for 4.50:1 on #F4F4F4). The brand hex is unchanged in the file.
3. **The prescribed focus ring.** `focus: #3E6AE1` reuses Electric Blue, which the file's own Don'ts reserve for primary CTAs ("never for decorative purposes"). A focus ring is not decoration, but it is a second use of the one chromatic token and a brand owner may want a different answer. The ring is drawn **outside** the control with a 2px offset, so it is judged against the surface behind it rather than against the CTA fill it surrounds; over the modal scrim (2.12:1) and over photography it needs its white outer edge.
4. **Two extra `motion:` keys.** `duration-extracted-state: 330ms` and `ease-extracted-state: cubic-bezier(0.5, 0, 0, 0.75)` sit beside the ten verbatim Cinematic values, and the hover row uses 330ms rather than the profile's 240ms. This is a deliberate, stated deviation because these two values are genuinely extracted from the source's component CSS, and SPEC asks that no inferred motion be presented as extracted — the converse seemed to follow. If cross-file comparability must win outright, drop both keys and the hover row reverts to `{motion.duration-fast}`.

### Identity verdict

Still unmistakably Tesla, and the conversion did not flatten it into a token dump. The things that make this file specific survived in prose and are now also true of the tokens: one chromatic value in the entire palette, with the promo blue documented as *the same token* rather than split into a second accent; three greys for text and nothing else; a radius ladder that tops out at 4px for every control; a `shadow:` group whose first entry is `rgba(0,0,0,0)`; and two surfaces 1.10:1 apart, which no generic system would ship. The most Tesla-specific fact in the new material is an absence — the palette contains no tone that can draw a visible edge — and that is a real finding about this brand, not a borrowed caveat.

Cinematic is the correct profile and I did not switch it. SPEC's first assignment clause fires on identity, not canvas polarity: automotive, full-bleed photography, sparse type, 100vh gallery sections, one message per screen. Tesla is the exact case the rule's "a white-canvas luxury brand is still cinematic" sentence was written for. The one tension — the file's own Don't against scale and translate on hover — is handled the way the Lamborghini conversion handled the same rule: hover and press lose all transform, reveals keep the profile's travel.

The honest caveat is motion generally. This file is unusual in recording two real transition values, and they are 330ms — slower than Cinematic's `duration-fast` and in the same register as its base, which is weak corroboration that the profile fits. Everything else about the timing is prescribed, and the file says so in its own first line.
