## A69 · stripe

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

- Before: 4 · 5 · 1 · 2 · 1 · 1
- After: 5 · 5 · 5 · 5 · 5 · 5

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Nothing in the file said anything about timing. |
| P0 | G Accessibility | whole file | No `## Accessibility` section, so four frozen contrast failures were undisclosed and the file told nobody that the brand's own hairlines are not perceivable boundaries. |
| P0 | A Tokens | `colors` | No `focus*` role. The file specified a focus behaviour in prose (`text-input-focused`: border swaps to `{colors.primary}`) with no addressable ring token and no measured ratio. |
| P0 | B Colour | `{colors.hairline-input}` on `{colors.canvas}` | 1.82:1 against the 3:1 non-text minimum. This is the sole boundary of `text-input`, so the real brand's form fields fail WCAG 1.4.11. Frozen value; handled by re-scoping prose to `{colors.ink-mute}` (4.75:1), already in the palette. |
| P0 | B Colour | `{colors.hairline}` on `{colors.canvas}` / `{colors.canvas-soft}` | 1.23:1 and 1.17:1. Card and table boundaries across the whole marketing system are below 3:1. Frozen; now scoped to decoration in prose. |
| P1 | B Colour | `pill-tag-soft` | `{colors.primary-deep}` on `{colors.primary-bg-subdued-hover}` is 4.23:1, under 4.5:1, and the type is 10px `{typography.micro-cap}` — the smallest role in the file, so no large-text exemption applies. Real AA failure, now stated. |
| P1 | H States | every component | Only `hover` and `pressed` were documented. `focus-visible`, `active`, `disabled`, `loading`, `selected`, `error` appeared nowhere. |
| P1 | C Elevation | Elevation & Depth | Level 3 is "gradient mesh backdrop" while Levels 1–2 are box-shadows, so the ladder mixes two mechanisms. Kept — it is a true statement about this brand — but recorded in Known Gaps so it is not mistaken for a consistent scale. |
| P1 | A Tokens | no `shadow:` group | The prose states literal `rgba(0,55,112,0.08)` recipes with no token to reference, which SPEC section 1 flags as exactly the case a `shadow:` group exists for. Not added: adding one would mean inventing names for three recipes and re-pointing extracted prose, a bigger diff than this audit's scope. Recorded in Known Gaps. |
| P1 | B Colour | `{colors.ink-mute}` on `{colors.canvas-cream}` | 3.95:1 — the caption ink is unusable for body copy on the cream band. Unmeasured by the harness (see Shared issues); now disclosed with `{colors.ink-secondary}` at 9.77:1 as the fix. |
| P2 | B Colour | `link-on-light` | `{colors.primary}` against `{colors.ink}` is 2.51:1, so an un-underlined inline link is distinguished from body text by hue alone, short of the 3:1 WCAG 1.4.1 wants. Underline-on-hover is now required in the file. |
| P2 | B Colour | `{colors.ink-mute}` on `{colors.canvas-soft}` | 4.49:1 — fails AA by 0.01. Noted with an 18px+ usage note rather than treated as a defect. |
| P2 | A Tokens | `{colors.ink-mute-2}` | `#61718a` is 0.2:1 from `{colors.ink-mute}` `#64748d`. Two tokens, one perceptible colour. Kept as extracted, recorded in Known Gaps. |
| P2 | D Typography | all roles | Every role carries size, weight, line height and letter spacing — no gap. Body at 15px/1.4 weight 300 reads at 14.73:1 on the soft band, so it is readable on this file's own surfaces. No change. |
| P2 | E Shapes | radius ladder | 4 / 6 / 8 / 12 / 16 / 9999px is internally consistent; nothing sits outside its scale. Focus ring geometry (2px ring, 2px offset) was the only missing rung and is now specified. |
| P2 | A Tokens | `components` | `{colors.canvas-soft}`, the brand's real secondary surface, was never bound to any component, so it was invisible to the harness. Added `section-band-soft`, which the Overview and Colors prose already described in words. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | — -> `focus: "#665efd"` | The `focus` role was missing. `#665efd` is the hex `{colors.primary-soft}` already owns — a real role binding on a real job, not an alias — and it is the one indigo that clears 3:1 on all four surfaces this file defines (4.58 / 4.34 / 3.81 / 3.36). One ring, so no second polarity token. |
| frontmatter | — -> `motion:` group | SPEC section 4/5 **Crisp** block, verbatim, no deviation. |
| frontmatter `components` | — -> `section-band-soft` (bg `{colors.canvas-soft}`, text `{colors.ink}`) | Documents the feature band the prose already described, and makes the brand's real secondary surface measurable. Side effect: the `surface` role now resolves to `canvas-soft` instead of the one-off cream band, so the boundary pairs the harness reports are ones the site actually renders. |
| frontmatter `components` | `card-feature-light`, `card-pricing` -> + `borderColor: "{colors.hairline}"`; `text-input` -> + `borderColor: "{colors.hairline-input}"`; `text-input-focused` -> + `borderColor: "{colors.primary}"`, `focusRing: "{colors.focus}"` | The borders were stated in prose but never declared, so per SPEC section 1 they were unmeasurable. Declaring them added no new failing pair — each duplicates a pair already failing on the canvas. Values are the extracted ones; nothing was re-pointed. |
| Colors › Surface | hairline entries plain -> labelled frozen and decorative, with their measured ratios and the `{colors.ink-mute}` substitute for load-bearing boundaries; new `{colors.focus}` entry | SPEC section 2 steps 1, 3 and 4: the palette already owns a passing tone, so re-scope prose and add nothing. |
| Components › all entries | — -> a `States:` line per component | Dimension H. Components that genuinely have one state (`card-cream-band`, `card-dashboard-mockup`, `section-band-soft`) say so explicitly rather than claiming the full set. |
| Components › `text-input` | — -> note that the extracted boundary is 1.82:1 and fails 1.4.11 | SPEC section 2 step 4: say plainly where the brand fails. |
| Components › `pill-tag-soft` | — -> note that the extracted pair is 4.23:1 at 10px, with `{colors.primary-press}` at 6.18:1 as the nearest passing ink | Same. |
| Components › `card-cream-band` | — -> note that the band carries no border (1.2:1 against white is a colour change, not an edge) | Pre-empts drawing a hairline on cream, which measures 1.03:1. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Ten-row interaction table, token list, rules, `prefers-reduced-motion` block. `transform` and `opacity` only. |
| after that | — -> `## Accessibility` | 20-row measured-contrast table, focus ring measured on each surface with its offset, tap-target spec marked as specification, reduced-motion pointer, non-colour-redundancy rule. |
| after `## Iteration Guide` | — -> `## Known Gaps` | Prescribed motion, missing semantic palette, duplicate mute ink, missing shadow tokens and mixed elevation mechanisms, under-specified dark track, unverifiable tap targets, unmeasurable gradient mesh. |

Nothing else was reflowed. `Responsive Behavior` was already a top-level section; `Iteration Guide` was kept in place.

### Contrast checks

All computed with WCAG 2.1 relative luminance from the file's own hexes, not estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#0d253d` / `canvas` `#ffffff` | 15.57:1 | 4.5:1 | Pass |
| `ink` / `canvas-soft` `#f6f9fc` | 14.73:1 | 4.5:1 | Pass |
| `ink` / `canvas-cream` `#f5e9d4` | 12.96:1 | 4.5:1 | Pass |
| `ink-secondary` `#273951` / `canvas` | 11.73:1 | 4.5:1 | Pass |
| `ink-secondary` / `canvas-soft` | 11.10:1 | 4.5:1 | Pass |
| `ink-mute` `#64748d` / `canvas` | 4.75:1 | 4.5:1 | Pass |
| `ink-mute` / `canvas-soft` | 4.49:1 | 4.5:1 | Fail (by 0.01) |
| `ink-mute` / `canvas-cream` | 3.95:1 | 4.5:1 | Fail |
| `ink-mute-2` `#61718a` / `canvas` | 4.96:1 | 4.5:1 | Pass |
| `ink-mute-2` / `canvas-soft` | 4.69:1 | 4.5:1 | Pass |
| `ink-mute-2` / `canvas-cream` | 4.13:1 | 4.5:1 | Fail |
| `on-primary` `#ffffff` / `primary` `#533afd` | 6.19:1 | 4.5:1 | Pass |
| `on-primary` / `brand-dark-900` `#1c1e54` | 15.41:1 | 4.5:1 | Pass |
| `primary` / `canvas` | 6.19:1 | 4.5:1 | Pass |
| `primary` / `canvas-cream` | 5.16:1 | 4.5:1 | Pass |
| `primary-deep` `#4434d4` / `primary-bg-subdued-hover` `#b9b9f9` (`pill-tag-soft`) | 4.23:1 | 4.5:1 | Fail |
| `primary-press` `#2e2b8c` / `primary-bg-subdued-hover` | 6.18:1 | 4.5:1 | Pass (proposed) |
| `hairline` `#e3e8ee` / `canvas` | 1.23:1 | 3.0:1 | Fail |
| `hairline` / `canvas-soft` | 1.17:1 | 3.0:1 | Fail |
| `hairline` / `canvas-cream` | 1.03:1 | 3.0:1 | Fail |
| `hairline-input` `#a8c3de` / `canvas` | 1.82:1 | 3.0:1 | Fail |
| `hairline-input` / `canvas-soft` | 1.72:1 | 3.0:1 | Fail |
| `hairline-input` / `canvas-cream` | 1.52:1 | 3.0:1 | Fail |
| `ink-mute` as boundary / `canvas` | 4.75:1 | 3.0:1 | Pass (the in-palette substitute) |
| `focus` `#665efd` / `canvas` | 4.58:1 | 3.0:1 | Pass |
| `focus` / `canvas-soft` | 4.34:1 | 3.0:1 | Pass |
| `focus` / `canvas-cream` | 3.81:1 | 3.0:1 | Pass |
| `focus` / `brand-dark-900` | 3.36:1 | 3.0:1 | Pass |
| `primary` / `ink` (link vs body text) | 2.51:1 | 3.0:1 | Fail — underline required |
| `canvas-soft` / `canvas` (layer separation) | 1.06:1 | — | Barely separable; the brand relies on section scale, not edge contrast |
| `canvas-cream` / `canvas` | 1.20:1 | — | A colour change, not a boundary |
| `brand-dark-900` / `canvas` | 15.41:1 | — | The dark track is unambiguously a separate layer |

Elevation note for dimension C: `canvas` `#ffffff` and `canvas-soft` `#f6f9fc` differ by 1.06:1, and cards on the soft band return to pure white, so the card-on-band relationship is carried almost entirely by a hairline that measures 1.17:1. The layers are, in the strict sense, not distinguishable by luminance; the brand separates them with 64–96px of section padding and the mesh instead. That is a real property of the brand, now stated in the file rather than implied.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity`, `transform` (shadow swap on cards) | Colour/shadow instant, no transform |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed, fill change only |
| Focus | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on the ring | Ring instant at full opacity |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` | `opacity` at `{motion.duration-reduced}` 100ms |
| Modal / drawer | 150ms in, 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | Opacity only, 100ms, no travel |
| Dropdown | 100ms in, 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(4px)` | Opacity only, 100ms, no travel |
| Toast | 100ms in, 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | Opacity only, 100ms, no travel |
| List enter | 150ms, stagger `{motion.stagger-step}` 20ms | `{motion.ease-enter}` | `opacity` + `translateY(6px)` | Stagger dropped, one fade at 100ms |
| List exit | 100ms | `{motion.ease-exit}` | `opacity` + `translateY(4px)` | Opacity only, 100ms, no travel |
| Loading | 900ms, infinite | linear | `transform: translateX` on a bar, `opacity` on skeletons | Loop frozen, static skeleton plus text status |

Every exit is shorter than its entrance. The loading indicator is the only infinite animation. The gradient mesh is a static image, so there is no brand ambience to freeze.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, line 31 (`text-dim` patterns) | The pattern `^ink-(muted\|subtle\|soft\|tertiary\|…)` does not match `ink-mute` or `ink-mute-2`, which are this file's actual caption and helper inks. Their real failures — 3.95:1 and 4.13:1 on `canvas-cream`, 4.49:1 on `canvas-soft` — were never measured, and `check_all("text-dim", …)` saw only `ink-secondary`, which passes everywhere. The harness reported a clean secondary-text result for a file whose caption ink fails on two of its three surfaces. | Add `^ink-mute` (and `^mute$`) to the `text-dim` pattern list, or relax `^ink-(muted…)` to `^ink-mut`. I disclosed the pairs in the file by hand instead. |
| `theme-audit/audit.py`, lines 234–260 (surface fallback) | Before my edit the `surface` role resolved to `canvas-cream`, a single warm interlude band, because it was the nearest-to-canvas token any container component bound — the real secondary surface `canvas-soft` was never bound, so it was invisible. Every "on surface" pair was then measured against a ground the site renders once, and the brief's two cream-band findings (1.03:1, 1.52:1) are manufactured in that sense: the file never draws a hairline on cream. This is the "satisfies a role wrongly" case in SPEC section 1. It should have picked `canvas-soft`. | The fallback already prefers the token nearest the canvas; the gap is that it only considers tokens bound in `components:`. Consider also allowing a `canvas-`/`surface-`-named token that the canvas pattern did not claim as a surface candidate, ranked the same way. I fixed it for this file by binding `canvas-soft` to a real component, which is the honest fix, but 83 other files may have the same blind spot. |
| `theme-audit/audit.py`, line 614 area (`durations_found`) | `re.findall(r"\b(\d{2,4})ms\b", text)` is fine, but `durations_found` for this file now reports `01` and `400` — `01` from `animation-duration: 0.01ms` in the reduced-motion block and `400` from the typographic prose "Bumping display weight above 300 — at 400 …". Cosmetic: the field is reported, not scored. | Match `(\d+(?:\.\d+)?)ms` and drop values under 10ms from the report. |

### Needs approval

1. **Re-point `text-input`'s boundary.** The extracted `borderColor: {colors.hairline-input}` `#a8c3de` measures 1.82:1 on `{colors.canvas}` and is the field's only affordance, so the real product fails WCAG 1.4.11. The frontmatter binding is left exactly as extracted. Nearest passing value already in the palette: `{colors.ink-mute}` `#64748d` at 4.75:1. Usage note that would make the real value defensible: none — 1.4.11's 3:1 applies to a control boundary at any size, with no small-text exemption, so `#a8c3de` is defensible only if the field carries a second non-colour affordance (a filled `{colors.canvas-soft}` ground, or a persistent label plus a 2px underline). A brand owner has to choose between re-pointing the token and adding that second affordance.
2. **Re-point `card-feature-light` / `card-pricing` boundaries.** `{colors.hairline}` `#e3e8ee` at 1.23:1 on white. Defensible as purely decorative, which is how the file now describes it, **provided** card extent is never meaningful — but pricing cards are compared side by side and one is selectable, where extent is meaningful. Nearest passing value in the palette: `{colors.ink-mute}` at 4.75:1, which would visibly change the brand's light touch. Alternative that preserves the look: keep the hairline and carry extent with the Level 1 shadow plus the 32px padding.
3. **`pill-tag-soft` ink.** `{colors.primary-deep}` on `{colors.primary-bg-subdued-hover}` is 4.23:1 at 10px. Nearest passing value: `{colors.primary-press}` `#2e2b8c` at 6.18:1. Usage note that would make `#4434d4` defensible: none at 10px — AA's 3:1 large-text threshold starts at 18px, or 14px bold, and `{typography.micro-cap}` is 10px at weight 400. Either darken the ink or raise the eyebrow to 14px bold.
4. **`{colors.ink-mute}` and `{colors.ink-mute-2}` on `{colors.canvas-cream}`.** 3.95:1 and 4.13:1. Nearest passing in-palette value: `{colors.ink-secondary}` `#273951` at 9.77:1. Defensible usage note for the real values: 18px+ or 14px-bold only — but `{typography.caption}` is 13px and `{typography.micro}` is 11px, so in practice helper text must not appear on the cream band at all without the swap.
5. **The prescribed `error` tone.** `{colors.ruby}` `#ea2261` is documented as a gradient and chart accent, never a state colour. I used it for `text-input`'s error state and labelled it prescribed. If the dashboard product UI has a real error red, it should replace this.

### Identity verdict

Still unmistakably this brand, and in two places more so than before. The additions are all brand-specific rather than generic: the **Crisp** profile is right on the roster's own terms — financial infrastructure and developer tooling, where a 150ms base and no entrance choreography match a product whose argument is "look at the actual product," and where the document's own voice ("short, decisive, transactional") would be contradicted by a 400ms reveal. I considered Cinematic on the strength of the gradient mesh, and rejected it: the mesh is a static backdrop, not a slow full-bleed reveal, and nothing in the file describes imagery that scales or type that arrives late. Playful fails on role — the saturated tones (ruby, magenta, lemon) appear inside the mesh and as chart dots, explicitly never on interactive elements, which is exactly the case SPEC section 5 rule 3 says is not a playful identity. No switch.

The new Accessibility section is where the identity sharpens: a brand whose entire boundary vocabulary measures between 1.03:1 and 1.82:1, and whose single CTA colour is the only signal it has, is a specific and recognisable position, not a generic one. The one-ring decision follows from the palette (an indigo already sitting at a mid luminance that clears white through deep navy) rather than from a template. The risk I watched for was the motion table reading as the same table in 84 files; it is mitigated only partly — the durations are deliberately shared for comparability — so the brand-specific content sits in the notes around it (static mesh, no ambience, the transactional snap warning). The one drift I accepted is the `section-band-soft` component, which is the most generic entry in the file; it earns its place by making the brand's real secondary surface measurable.
