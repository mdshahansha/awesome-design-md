## A29 · jobright

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 1 | 1 | 1 | 1 |
| After | 5 | 5 | 5 | 5 | 5 | 5 |

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A/B | `ex-pricing-tier-featured` | `textColor: {colors.on-primary}` (#000000) over `backgroundColor: {colors.ink}` (#000000) — black on black, 1.00:1. A **binding error**, not a brand fact: `on-primary` is defined in this file as the black label used on the mint accent fill, so it is not a valid ink for a dark surface. The entry's own description asks for "dark fill + light text". |
| P0 | A | Frontmatter `colors` | No `focus` role. No focus ring colour, width, offset or measured ratio existed anywhere in the file. |
| P0 | F | Whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Zero durations and zero easings in the file. |
| P0 | G | Whole file | No `## Accessibility` section, so five measured contrast failures were undisclosed. |
| P1 | B | `score-ring` | `{colors.primary}` #00f0a0 numeral on `{colors.canvas}` #ffffff = 1.50:1, against 3.0:1 for 32px large text. A **genuine brand failure**, not a binding error: canvas is a real paintable surface here, mint is genuinely the brand's accent, and the file's own prose says "mint value". Disclosed rather than repainted; a prescribed `{colors.primary-deep}` parallel added for mint-as-text. |
| P1 | B | `{colors.muted}` | #86909c = 3.24:1 on canvas and 2.94:1 on `{colors.surface-soft}`, used for 14px `{component.footer}` links. Fails AA for body text; fails even 3:1 on the grey panel. Extracted and frozen. |
| P1 | B/E | `{colors.hairline}` | #e5e7eb = 1.24:1 on canvas, 1.12:1 on surface-soft, 1.18:1 on canvas-mint, while being the only boundary of `{component.text-input}` and `{component.job-search-bar}`. Extracted and frozen. |
| P1 | C | Elevation & Depth | Elevation is expressed two ways at once — border at levels 0–1, a shadow at level 2 — and the level-1 `rgba(0,0,0,0.5)` inset has no token to reference. No blur/offset/spread captured, so a `shadow:` group cannot be built without inventing values. Logged in Known Gaps. |
| P1 | H | Every component entry | No component named any state. Harness saw only "active", and that from an `activeIndicator` property name. |
| P1 | E | Shapes table | Row read `` `{rounded.lg}` | 28px `` — wrong token for that value (`{rounded.lg}` is 24px, `{rounded.xl}` is 28px), and the same mistake appeared twice in prose describing the primary black pill, which the frontmatter builds from `{rounded.xl}`. |
| P1 | A | `{component.text-input}` | Frontmatter says `rounded: {rounded.none}` (0px); the Shapes table and Components prose both say `{rounded.sm}` (12px). Unresolvable from the document; logged in Known Gaps rather than silently reconciled. |
| P2 | A | `ex-data-table-cell` | Prose said "Header uses mono-caps eyebrow typography" while the token is `{typography.caption}` (Inter 13px/500). No mono family exists in this file. |
| P2 | C | Canvas/surface layers | `{colors.canvas}` #ffffff vs `{colors.surface-soft}` #f2f4f5 = 1.10:1 and vs `{colors.canvas-mint}` #ecffe0 = 1.05:1. The layers are barely separable on their own; the system relies on full-bleed band *extent* and card radius, not luminance steps, which is a real property of this brand rather than a defect. Stated in the file. |
| P2 | B | `{colors.primary}` on `{colors.canvas-mint}` | 1.43:1. Not flagged by the harness, but worth stating: mint type on the mint band is invisible. Added as a Don't-style note in the Accessibility disclosure table. |
| P2 | G | Responsive Behavior | The pre-existing "comfortable ≥44px tap height" claim is not measurable from a document. Kept verbatim on the move, but labelled as prescribed in Accessibility and Known Gaps. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Frontmatter `colors` | 9 tokens -> 13: added `focus: #008f66`, `muted-strong: #616a75`, `hairline-strong: #7a8290`, `primary-deep: #00664a`, under a comment marking them prescribed | Fills the missing `focus` role and gives the three frozen failures parallel accessible tokens (SPEC §2) without touching a brand hex |
| Frontmatter | no `motion:` group -> Playful block from SPEC §5, verbatim | Required token group; profile values copied exactly so sibling Playful files stay comparable |
| Frontmatter `ex-pricing-tier-featured` | `textColor: {colors.on-primary}` -> `{colors.on-dark}` | Binding error fixed: 1.00:1 -> 21.00:1. `on-primary` is the mint accent's label, `on-dark` is the ink for black surfaces |
| `## Colors` | added `### Prescribed Accessible Parallels (not extracted)`; `{colors.hairline}` bullet now scopes it to decoration | Labels the four new tokens as prescribed and states each measured ratio |
| `## Shapes` table | `{rounded.lg}` | 28px -> `{rounded.xl}` | 28px | Token sat outside its own scale; 28px is `{rounded.xl}` |
| Overview key characteristic + Do's bullet | black pills `{rounded.lg}` -> `{rounded.xl}` | Matched prose to the frontmatter the components actually use |
| `## Components`, `button-primary` | rounded `{rounded.lg}` -> `{rounded.xl}` | Same |
| `## Components`, all 19 brand entries + all 10 `ex-*` entries | no states -> a `States —` line each | SPEC §7. Static bands, `stat-item`, `score-ring`, `testimonial-card`, `video-card` and `ex-empty-state-card` state plainly that they have one, two or three real states instead of padding the list |
| `## Components`, `score-ring` | added the measured 1.50:1 failure and the `{colors.primary-deep}` remedy inline | The failure belongs where someone building the component will read it |
| `## Components`, `text-input` / `job-search-bar` / `footer` | added the measured ratio and the `-strong` token to use | Same reason |
| `## Components`, `ex-data-table-cell` | "mono-caps eyebrow typography" -> `{typography.caption}` eyebrow typography | No mono family exists in this file |
| New `## Motion & Animation` after `## Components` | absent -> first line states the system is prescribed, not measured; 11-row interaction table; rules; `@media (prefers-reduced-motion: reduce)` block | SPEC §3, §4, §6 |
| New `## Accessibility` | absent -> measured-pass table, disclosed-failure table, focus ring ratios on all four surfaces, tap target, reduced motion | SPEC §3; disclosure is what stops a frozen failure counting (SPEC §2) |
| `## Layout` -> new top-level `## Responsive Behavior` | `### Responsive Strategy` **moved** verbatim out of Layout, not duplicated; its four `####` children re-levelled to `###` under the promoted parent | SPEC §3 requires it as a top-level section |
| New `## Known Gaps` | absent -> 9 entries | SPEC §3, plus every prescribed/unverifiable claim in the file now has a home |

### Contrast checks

All computed with WCAG 2.1 relative luminance, python3 stdlib only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #000000 / `canvas` #ffffff | 21.00:1 | 4.5:1 | Pass |
| `ink` / `surface-soft` #f2f4f5 | 19.03:1 | 4.5:1 | Pass |
| `ink` / `canvas-mint` #ecffe0 | 19.95:1 | 4.5:1 | Pass |
| `on-dark` #ffffff / `ink` | 21.00:1 | 4.5:1 | Pass |
| `on-primary` #000000 / `primary` #00f0a0 | 13.97:1 | 4.5:1 | Pass |
| `muted` #86909c / `canvas` | 3.24:1 | 4.5:1 | **Fail** — disclosed, frozen |
| `muted` / `surface-soft` | 2.94:1 | 4.5:1 | **Fail** — disclosed, frozen |
| `muted` / `canvas-mint` | 3.08:1 | 4.5:1 | **Fail** — disclosed, frozen |
| `hairline` #e5e7eb / `canvas` | 1.24:1 | 3.0:1 | **Fail** — disclosed, frozen |
| `hairline` / `surface-soft` | 1.12:1 | 3.0:1 | **Fail** — disclosed, frozen |
| `hairline` / `canvas-mint` | 1.18:1 | 3.0:1 | **Fail** — disclosed, frozen |
| `primary` #00f0a0 / `canvas` (score-ring numeral) | 1.50:1 | 3.0:1 | **Fail** — disclosed, genuine brand failure |
| `primary` / `canvas-mint` | 1.43:1 | 3.0:1 | **Fail** — disclosed |
| `primary` / `ink` | 13.97:1 | 3.0:1 | Pass |
| `ex-pricing-tier-featured` text / fill, before | 1.00:1 | 4.5:1 | **Fail** — binding error, fixed |
| `ex-pricing-tier-featured` text / fill, after | 21.00:1 | 4.5:1 | Pass |
| `focus` #008f66 / `canvas` | 4.10:1 | 3.0:1 | Pass |
| `focus` / `canvas-mint` | 3.90:1 | 3.0:1 | Pass |
| `focus` / `surface-soft` | 3.72:1 | 3.0:1 | Pass |
| `focus` / `ink` | 5.12:1 | 3.0:1 | Pass |
| `focus` / `primary` (mint pill fill) | 2.73:1 | 3.0:1 | **Fail** — handled by the mandatory 2px offset, which puts the ring on the band behind the pill; disclosed |
| `muted-strong` #616a75 / `canvas` | 5.49:1 | 4.5:1 | Pass (prescribed) |
| `muted-strong` / `surface-soft` | 5.18:1 | 4.5:1 | Pass (prescribed) |
| `muted-strong` / `canvas-mint` | 5.43:1 | 4.5:1 | Pass (prescribed) |
| `hairline-strong` #7a8290 / `canvas` | 3.62:1 | 3.0:1 | Pass (prescribed) |
| `hairline-strong` / `surface-soft` | 3.51:1 | 3.0:1 | Pass (prescribed) |
| `hairline-strong` / `canvas-mint` | 3.68:1 | 3.0:1 | Pass (prescribed) |
| `primary-deep` #00664a / `canvas` | 7.00:1 | 4.5:1 | Pass (prescribed) |
| `canvas` / `surface-soft` (layer separation) | 1.10:1 | — | Layers not separable by luminance alone |
| `canvas` / `canvas-mint` (layer separation) | 1.05:1 | — | Same; band extent and radius carry the separation |

### Motion inventory

Profile: **Playful**, token block copied verbatim from SPEC §5. Prescribed, not measured — stated in the section's first line.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `transform: scale(1.02)` / `translateY(-2px)`, `opacity` | No transform; colour/opacity instant |
| Press / active | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.97)` | Scale removed; instant |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the 2px `{colors.focus}` ring | Appears instantly, never suppressed |
| Page / route transition | `{motion.duration-base}` 200ms | `ease-enter` in, `ease-exit` out | `opacity` + `translateY(8px)` | Opacity only, `{motion.duration-reduced}` |
| Modal / drawer | 200ms in, 130ms out | `ease-enter` / `ease-exit` | `opacity` + `scale(0.98→1)` / `translateX` | Opacity only, 130ms; appears in place |
| Dropdown | 130ms in, 70ms out | `ease-enter` / `ease-exit` | `opacity` + `scale(0.98→1)` | Opacity only, 130ms |
| Toast | 200ms in, 130ms out | `ease-enter` / `ease-exit` | `opacity` + `translateY(12px)`, slight overshoot | Opacity only, no travel or overshoot |
| List enter | 200ms per item, `{motion.stagger-step}` 60ms between | `ease-enter` | `opacity` + `translateY(12px)` | Stagger dropped; all fade together at 130ms |
| List exit | 130ms | `ease-exit` | `opacity` + `scale(0.98)` | Opacity only, 130ms |
| Loading | `{motion.duration-emphasis}` 450ms count-up; spinner loops | `{motion.ease-standard}` | `rotate()` on spinner, `opacity` on skeletons | Static mint arc plus text status; final number shown at once |
| Job ticker marquee (brand ambience) | continuous, ~40s cycle | linear | `transform: translateX()` | Frozen, static band |

No `width`, `height`, `top`, `left` or `margin` is animated; the FAQ accordion and the nav underline are explicitly specified on `transform`/`opacity` so neither reaches for height or width. Every exit is shorter than its entrance. Only two infinite animations exist — the loader and the marquee — and the marquee is declared as deliberate brand ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, line ~366 (`disclosed()`) | Disclosure matches on the foreground token name or hex appearing on a line that also states the ratio. Nothing ties the line to the *background*, so one sentence mentioning `muted` and `3.24:1` discloses both the `muted on canvas` pair and the separate `footer` component failure. Harmless here (same pair), but it would let a file disclose a pair on white and be credited for a different failure of the same token on another surface. | Also require the background hex or its token name on the matching line, where the failure record carries one. |
| `theme-audit/audit.py`, line ~346 | `if fg and not bg and roles.get("canvas")` assumes any component with no `backgroundColor` is drawn on the canvas. For this brand most `ex-*` surfaces actually sit on `{colors.canvas-mint}` bands, which would be the stricter test. | Allow a component to declare its parent surface (e.g. an `on:` property), falling back to canvas. |
| `theme-audit/SPEC.md` §1 | "Where a file documents both light and dark signature surfaces, one ring cannot serve both" reads as mandatory, then the following paragraph permits a single mid-luminance ring for three-polarity brands. A reader hits the hard rule first and defines a `focus-on-dark` it does not need. | Lead with the measurement test — "the ring must reach 3:1 against every surface it can appear over" — and present the pair and the single mid-luminance ring as two ways of satisfying it. |
| `theme-audit/SPEC.md` §3 | The Responsive Behavior row says to move a Layout subsection "verbatim" without saying whether its child heading levels should be promoted with it. I promoted `####` to `###` so the section is not a level deep under its own `##`. | Add "promoting its child headings one level" to that row. |
| `design-md/jobright/DESIGN.md` prose, `## Elevation & Depth` | Level 1 states `rgba(0,0,0,0.5) 0px 0px 0px 0.5px inset` with no token, and level 2 a "whisper-soft drop shadow" with no values at all. Repo-wide pattern per SPEC §1. Not inventable from this document, so no `shadow:` group was added. | Capture real shadow values from the live sites, then add `shadow:` groups and reference them. |

### Needs approval

Three frozen brand values fail AA and are disclosed in the file rather than altered. Each needs a product decision before anyone builds on this document.

1. **`{colors.muted}` #86909c as secondary text.** Measures 3.24:1 on `{colors.canvas}` and 2.94:1 on `{colors.surface-soft}`; the brand uses it for 14px footer links and captions. Nearest passing value: **#616a75** (5.49:1 on canvas), added as the prescribed `{colors.muted-strong}`. Usage note that would make the real value defensible: *`{colors.muted}` is for 18px+ regular or 14px bold labels only, where 3:1 applies, and never on `{colors.surface-soft}`, where it fails even that.* Approve either the swap for body-size text or the restriction.
2. **`{colors.hairline}` #e5e7eb as a control boundary.** 1.24:1 on canvas, 1.12:1 on surface-soft. Nearest passing value: **#7a8290** (3.62:1 on canvas), added as the prescribed `{colors.hairline-strong}`. Usage note: *`{colors.hairline}` is a decorative divider between content rows; the only boundary of an interactive control takes `{colors.hairline-strong}`.* Approve the two-token split.
3. **`{colors.primary}` #00f0a0 as text on light surfaces.** 1.50:1 on `{colors.canvas}` (the `{component.score-ring}` numeral) and 1.43:1 on `{colors.canvas-mint}`; the Colors section also gives mint to inline links. Nearest passing value: **#00664a** (7.00:1), added as the prescribed `{colors.primary-deep}`. Usage note: *mint is a fill, a stroke and a mark on black — never type on white or mint.* Approve `{colors.primary-deep}` for mint-coloured text, and confirm whether the live score numeral really is mint or whether that was an extraction of the ring arc.

Also for approval, lower stakes: the prescribed focus ring itself. **`{colors.focus}` #008f66**, 2px at 2px offset, one ring for all three surface polarities (4.10 / 3.90 / 3.72 / 5.12:1). The 2px offset is load-bearing — the ring is only 2.73:1 against the mint pill fill, so it must be drawn outside the control, not on it.

### Identity verdict

Still Jobright. The file's specifics survived: the mint/black/white three-polarity system, the pale-mint band rhythm, the dual pill ladder (black `{rounded.xl}` primary, mint `{rounded.pill}` signature), the 40px asymmetric mockup card, the scrolling black ticker and the Titillium-over-Inter tension are all untouched. The four new colour tokens are explicitly quarantined under a "prescribed, not extracted" heading, and three of the four are derived from the brand's own hues — the ring and `primary-deep` are deep-mint, `muted-strong` and `hairline-strong` are darker steps of the brand's existing blue-grey — so nothing generic was introduced into the palette proper.

**Playful is the right profile.** The assignment rule's test is saturated colour on interactive elements plus an informal type voice: Jobright puts #00f0a0 on a CTA pill, on nav-link hovers and on the score ring, carries emoji, a pink heart and hand-drawn illustration marks, runs a continuously scrolling marquee, and describes itself as "friendly, high-energy startup" rather than sober or editorial. Its display weight is 700 condensed, not 400. Crisp would be wrong — this is a marketing site, not a developer tool — and Calm would flatten the one genuine piece of brand motion the file records. The only concession to the brand's seriousness is the overshoot cap: `{motion.ease-enter}`'s springiness is held to 2% scale or 12px travel, so a job-search product never bounces.

The one place the document still reads as machine-made rather than brand-specific is the `### Examples (illustrative)` block, which arrived from `scripts/derive-examples-block.mjs` and announces its own `TO_FILL` markers. I resolved the two real defects in it — the black-on-black binding and the phantom "mono-caps" typography — and gave each entry brand-native states, but the block's framing is still auto-derived boilerplate. Out of scope for one file; worth a repo-wide pass.
