## A09 · bugatti

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 4 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

Harness findings confirmed independently before editing: `focus` was the only missing colour role; `hairline-strong` (#3a3a3a) on `canvas` (#000000) measures 1.85:1 against a 3.0:1 requirement; `Motion & Animation` and `Accessibility` were both absent; none of the eight states appeared in the Components section. All four confirmed.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A / G | `colors.focus` | No focus token and no focus indicator documented anywhere. The only focus prose in the file was "Focus thickens the bottom border to white" on `text-input` — a white-on-black change with no ring, and nothing at all for the other 15 components. On a #000000 canvas a browser-default outline is effectively invisible: a WCAG 2.4.7 failure. |
| P0 | B / E | `colors.hairline-strong` | 1.85:1 on canvas, and it was the *sole* boundary of `text-input`. A sighted low-vision user cannot see where the field is. `colors.hairline` is worse at 1.39:1. Extracted, so frozen — fixed by a parallel prescribed token, not by changing the hex. |
| P0 | F | whole file | No motion tokens, no motion section, no reduced-motion rule. Zero durations and zero easing curves in the file. |
| P0 | H | all 16 components | No component named a single state. Compounded by Iteration Guide item 5, which actively instructed authors *not* to document hover — a rule that contradicts SPEC §7 and was the root cause of the states score of 1. |
| P1 | C | `surface-soft` / `surface-card` / `surface-elevated` | The elevation ladder is not perceptually distinguishable: surface-soft 1.08:1 against canvas, surface-card 1.14:1, surface-elevated 1.27:1, and surface-card against surface-soft is 1.05:1. The file's own prose admits this ("no contrast jump"), but it means a "card" is identifiable only by its hairline — which fails 3:1. Extracted brand values, so recorded and scoped rather than altered. Elevation *is* expressed one consistent way (no shadow anywhere, border or photography only), so dimension C passes on consistency and fails on perceptibility. |
| P1 | B / G | `colors.muted-soft` | #666666 at 3.66:1 on canvas, used at 14px for legal and copyright lines. Fails 4.5:1. Extracted; under Needs approval. |
| P1 | G | `components.button-icon` | Specified at exactly 40 × 40px, below the 44px AAA target the file itself claims to meet for `button-primary`. Flagged from its documented size only — no tap-target claim is computable from a document. |
| P2 | A | `shadow` group | Not required here: the file documents *no* shadow value in prose ("no shadows, no glassmorphism, no gradients") and makes no `{shadow.*}` reference. Confirmed rather than added. |
| P2 | E | `rounded` ladder | `pill` and `full` are both 9999px — a duplicate rather than a ladder violation, and the prose explains the split (pill for buttons, full for circular icons). Left alone; the binary 0px/9999px scale has no value sitting outside it. |
| P2 | D | typography | All 12 roles carry family, size, weight, line height and letter-spacing. `body-md` at 16px/1.5 in #cccccc measures 13.08:1 on canvas and 11.47:1 on surface-card — readable on every surface the file defines. No change needed. |
| P2 | G | no light mode | `prefers-color-scheme` is not honoured and cannot be, by brand decision. Stated plainly in Accessibility rather than hidden. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `border-control: "#6b6b6b"` | Parallel accessible boundary token per SPEC §2. 3.94:1 on canvas, and ≥3:1 on all four surfaces this file defines (3.65 / 3.46 / 3.09). The two extracted hairlines stay in the file, untouched, scoped to decoration. |
| frontmatter `colors:` | — -> `focus: "#5b7fa6"` | Closes the missing role. `colors.link` (#c3d9f3) deepened so one ring clears 3:1 on every surface *and* against white (4.17:1) — a white ring would vanish on `colors.primary` and over blown-out photography. Keeps the ring inside the single chromatic note the brand already permits. |
| frontmatter | — -> `motion:` group, 9 keys | Cinematic profile per SPEC §4/§5: base 400ms, slow 600ms, emphasis 900ms, stagger 80ms, long-decelerate `cubic-bezier(0.16, 1, 0.3, 1)`. |
| `## Colors` | — -> Border Control and Focus entries | Both labelled prescribed, with every measured ratio stated and the AA failure of the real hairlines said plainly. |
| `## Components`, 16 entries | — -> one `- States:` line each | SPEC §7. Four components say plainly that they have one or two states (`wordmark-display`, `spec-cell`, `caption-overlay`, and the static form of `category-tag`) rather than inventing states to fill the list. |
| `## Components` -> `text-input` | `1px hairline-strong bottom border` -> `1px` `{colors.border-control}` underline, with a paragraph naming the substitution | The underline is the control's only boundary, so it must clear 3:1. The failing extracted tone is named and kept in the document. |
| `## Components` -> `text-input` | `Focus thickens the bottom border to white.` -> full state list, focus-visible = 2px white underline **plus** a 2px `{colors.focus}` ring | A white-to-white thickening is not a reliable indicator. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. Carries a token table, a 14-row interaction inventory, the motion rules, and the reduced-motion rule. |
| after Motion | — -> `## Accessibility` | 17-row measured contrast table, three named real-brand AA failures, focus-ring ratios on all five backgrounds it can land on, documented tap targets with the 40px icon button flagged, reduced-motion, plus tracking/colour-channel/no-light-mode notes. |
| `## Iteration Guide` item 5 | `Never document hover. Default and Active/Pressed states only.` -> document every real state, say so when there is only one, keep hover to opacity and underline weight | This line was the root cause of the states failure and contradicted SPEC §7. Rewritten to preserve the brand intent (no fill or colour flips on hover) while allowing the states to be documented. |
| `## Known Gaps` | one line on animation -> five lines | The whole motion section, both new tokens, the ring-over-photography limit, the tap-target limit, and the prescribed component states are now each labelled as prescribed or uncomputable. |

Not touched: every extracted hex, the typography block, the spacing and radius ladders, Layout, Elevation & Depth, Shapes, Do's and Don'ts, and Responsive Behavior. No prose was reflowed.

### Contrast checks

All computed with WCAG 2.1 relative luminance via a `python3 -I` stdlib snippet; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #ffffff / `canvas` #000000 | 21.0:1 | 4.5:1 | Pass |
| `ink` / `surface-soft` #0d0d0d | 19.44:1 | 4.5:1 | Pass |
| `ink` / `surface-card` #141414 | 18.42:1 | 4.5:1 | Pass |
| `ink` / `surface-elevated` #1f1f1f | 16.48:1 | 4.5:1 | Pass |
| `body` #cccccc / `canvas` | 13.08:1 | 4.5:1 | Pass |
| `body` / `surface-card` | 11.47:1 | 4.5:1 | Pass |
| `body-strong` #e6e6e6 / `canvas` | 16.83:1 | 4.5:1 | Pass |
| `muted` #999999 / `canvas` | 7.37:1 | 4.5:1 | Pass |
| `muted` / `surface-soft` | 6.82:1 | 4.5:1 | Pass |
| `muted` / `surface-card` | 6.47:1 | 4.5:1 | Pass |
| `muted-soft` #666666 / `canvas` | 3.66:1 | 4.5:1 | **Fail** (extracted — Needs approval) |
| `link` #c3d9f3 / `canvas` | 14.54:1 | 4.5:1 | Pass |
| `warning` #d4a017 / `canvas` | 8.84:1 | 4.5:1 | Pass |
| `success` #5fa657 / `canvas` | 7.08:1 | 4.5:1 | Pass |
| `on-primary` #000000 / `primary` #ffffff | 21.0:1 | 4.5:1 | Pass |
| `hairline` #262626 / `canvas` | 1.39:1 | 3.0:1 | **Fail** (extracted — scoped to decoration) |
| `hairline-strong` #3a3a3a / `canvas` | 1.85:1 | 3.0:1 | **Fail** (extracted — scoped to decoration) |
| `hairline-strong` / `surface-card` | 1.62:1 | 3.0:1 | **Fail** (extracted — scoped to decoration) |
| `border-control` #6b6b6b / `canvas` | 3.94:1 | 3.0:1 | Pass (prescribed) |
| `border-control` / `surface-soft` | 3.65:1 | 3.0:1 | Pass (prescribed) |
| `border-control` / `surface-card` | 3.46:1 | 3.0:1 | Pass (prescribed) |
| `border-control` / `surface-elevated` | 3.09:1 | 3.0:1 | Pass (prescribed) |
| `focus` #5b7fa6 / `canvas` | 5.03:1 | 3.0:1 | Pass (prescribed) |
| `focus` / `surface-soft` | 4.66:1 | 3.0:1 | Pass (prescribed) |
| `focus` / `surface-card` | 4.41:1 | 3.0:1 | Pass (prescribed) |
| `focus` / `surface-elevated` | 3.95:1 | 3.0:1 | Pass (prescribed) |
| `focus` / `primary` #ffffff | 4.17:1 | 3.0:1 | Pass (prescribed) |
| Elevation: `surface-soft` / `canvas` | 1.08:1 | — | Layers not perceptually distinct |
| Elevation: `surface-card` / `canvas` | 1.14:1 | — | Layers not perceptually distinct |
| Elevation: `surface-elevated` / `canvas` | 1.27:1 | — | Layers not perceptually distinct |
| Elevation: `surface-card` / `surface-soft` | 1.05:1 | — | Layers not perceptually distinct |
| Elevation: `surface-elevated` / `surface-card` | 1.12:1 | — | Layers not perceptually distinct |

### Motion inventory

Prescribed, not measured. Cinematic profile.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity` (+ `translateX(4px)` on the career-row chevron only) | Opacity at 120ms; travel removed |
| Press / active | `{motion.duration-instant}` 120ms | `{motion.ease-exit}` | `opacity` | Unchanged — already opacity-only, under 150ms |
| Focus-visible ring | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` | Instant, no fade; never animated away |
| Page / route transition | `{motion.duration-emphasis}` 900ms in, `{motion.duration-slow}` 600ms out | `{motion.ease-exit}` out, `{motion.ease-enter}` in | `opacity`; incoming hero `scale(1.04 → 1)` | 150ms cross-fade only; no scale, no stagger |
| Modal / drawer open | `{motion.duration-slow}` 600ms | `{motion.ease-enter}` | `opacity`; `translateY(16px → 0)` / `translateX(100% → 0)` | 150ms fade; panel appears in place |
| Modal / drawer close | `{motion.duration-fast}` 240ms | `{motion.ease-exit}` | `opacity`, `transform` | 150ms fade |
| Dropdown open | `{motion.duration-base}` 400ms | `{motion.ease-enter}` | `opacity`; `translateY(-8px → 0)`; items staggered 80ms | 150ms fade; no travel, no stagger |
| Dropdown close | `{motion.duration-fast}` 240ms | `{motion.ease-exit}` | `opacity`, `transform` | 150ms fade |
| Toast in | `{motion.duration-base}` 400ms | `{motion.ease-enter}` | `opacity`; `translateY(12px → 0)` | 150ms fade; no travel; dwell unchanged |
| Toast out | `{motion.duration-fast}` 240ms | `{motion.ease-exit}` | `opacity`, `transform` | 150ms fade |
| List enter | 400ms per item, `{motion.stagger-step}` 80ms between | `{motion.ease-enter}` | `opacity`; `translateY(12px → 0)` | All fade together at 150ms; no travel, no stagger |
| List exit | `{motion.duration-fast}` 240ms, no stagger | `{motion.ease-exit}` | `opacity` | 150ms fade |
| Loading | 1400ms loop | `{motion.ease-standard}` | `opacity` 1 → 0.3 on three monospace dots, offset 80ms | Loop frozen; static "LOADING" label in `{colors.muted}` |
| Hero / model photo reveal | `{motion.duration-emphasis}` 900ms | `{motion.ease-enter}` | `opacity` 0 → 1; `scale(1.04 → 1)` | 150ms fade, no scale; headline never waits on the image either way |

Every exit is shorter than its entrance. Only `transform` and `opacity` are animated. The sole infinite animation is the loader; the file states explicitly that Bugatti has no ambient motion vocabulary — no shimmer, pulse or parallax.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, line ~165 (`for bg in ("canvas", "surface", "accent")`) | The focus ring is checked against the `accent` role, which for a monochrome brand resolves to `primary` = `#ffffff`. That makes any ring at ≥3:1 on a black canvas and ≥3:1 on white the only legal answer — a mid-tone in luminance 0.10–0.30 — so a brand whose real ring is white is forced to invent a chromatic one. It is a defensible check (a ring can land on an accent-filled button), but for brands whose accent *is* white or black it silently narrows the solution space to a band the brand may not own. | Skip the `focus` vs `accent` check when the accent token is also the file's `text` or `canvas` value, or allow a second `focus-on-accent` token for that case, as SPEC already allows `focus-on-dark` for light/dark files. |
| `theme-audit/SPEC.md`, §1, the `focus-on-dark` paragraph | Scoped to files with "both light and dark signature surfaces". It has no rule for a file whose accent is white: here the ring must survive both #000000 and #ffffff, which is the same two-surface problem the paragraph describes, but the paragraph's trigger does not fire. | Broaden the trigger: define a second ring whenever any surface *or accent* the ring can appear over differs from the canvas by more than ~0.3 relative luminance. |
| `theme-audit/SPEC.md`, §2 | No threshold is set for canvas↔surface↔raised separation, yet SPEC §C-equivalent in the briefs asks whether layers are "actually distinguishable". Bugatti's layers sit at 1.05–1.27:1 and the harness scores contrast 5/5. | State a minimum (1.2:1 is the common floor for a surface step) or state explicitly that layer separation is a judgement call, so 84 reviewers do not each pick their own number. |
| `design-md/bugatti/DESIGN.md` Iteration Guide (fixed here, but likely repo-wide) | The instruction "Never document hover. Default and Active/Pressed states only." reads as boilerplate that may appear in other site files, where it would produce the same states score of 1. | Worth a repo-wide grep by whoever owns more than one file; I could not check other files' content under the one-file rule. |

### Needs approval

1. **`colors.muted-soft` #666666 — 3.66:1 on `canvas`, required 4.5:1.** Extracted brand tone, used at 14px for legal and copyright lines. Nearest passing value for 16px body: **#757575** (4.56:1). Usage note that would make the real value defensible: *this tone is for 18px+ regular or 14px bold text only, where the 3:1 large-text threshold applies* — but the file documents it at 14px regular, so as used it fails. Not changed; the hex is an extracted fact.
2. **`colors.hairline` #262626 (1.39:1) and `colors.hairline-strong` #3a3a3a (1.85:1) — required 3.0:1.** Both left in place and scoped to decoration per SPEC §2. Approval needed only for the judgement that the prescribed `border-control` #6b6b6b is the right nearest passing value; the brand's real boundary tone fails and the file now says so.
3. **`colors.focus` #5b7fa6 is an invention.** Nothing in the analyzed set showed a focus indicator. The value is derived from `colors.link`, the one chromatic token the brand permits. If Bugatti's real ring is white, the honest token would be `#ffffff` — which passes 21:1 on canvas but 1:1 against `colors.primary` and disappears over blown-out photography. Approving #5b7fa6 means accepting a prescribed chromatic addition to a brand that documents "no accent color".
4. **`components.button-icon` at 40 × 40px.** Below the 44px AAA target the file claims elsewhere. Fix needs either a size change (an extracted-value change) or a transparent 44px hit area (a prescribed addition). Flagged, not changed.

### Identity verdict

Still unmistakably Bugatti. Nothing was added that could have come from another file in the collection: the motion section argues from this brand's *absences* — no accent to flash, no fill to invert, no shadow to lift, no bold weight to snap to — and concludes that opacity and a ≤1.04 photo scale are the only channels left, with an explicit ban on overshoot, on type scaling, and on any ambient motion. The state lists are written in the brand's own vocabulary (opacity steps, underline weight, amber-not-red validation, "no shimmer — Bugatti has no shimmer vocabulary") and four components are allowed to say they have one or two states rather than being padded out.

The two additions that do drift are named as drift: `focus` #5b7fa6 adds a chromatic ring to a brand whose first sentence is "there is no accent color", and `border-control` #6b6b6b adds a visible boundary to a system built on invisible hairlines. Both are labelled prescribed in the frontmatter prose, the Accessibility section and Known Gaps, so a reader can strip them and still have the real brand. That is the smallest honest footprint I could find.

**Cinematic is the correct profile** and I did not switch it. SPEC §5 rule 1 fires exactly: dark canvas (#000000, the darkest in the collection) plus a luxury-automotive identity. The file's own signals agree — 120px section rhythm, full-bleed photography as the only depth element, weight 400 throughout, "slow-reading prose" as a stated editorial philosophy. Crisp at 150ms would read as cheap against that rhythm; Playful's overshoot would be a brand violation the file's Don'ts already forbid in spirit.
