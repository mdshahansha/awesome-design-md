## A08 · bmw

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 4 | 3 | 1 | 1 |
| After | 5 | 5 | 5 | 5 | 5 | 5 |

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Known Gaps explicitly declared animation "out of scope". |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Nothing in the file stated a measured ratio, so the brand's real AA failures were invisible to anyone building on it. |
| P0 | A Token contract | `colors.focus` | No focus token at all. Nothing in the file described focus behaviour except one clause on `text-input` ("the border thickens to ink") — a border thickening is not a focus indicator and has no stated contrast. |
| P0 | B/E Colour, borders | `colors.hairline-strong` | #cccccc on #ffffff = 1.61:1, against 3.0:1 for a component boundary. The file assigned it to `button-secondary` and `filter-chip` outlines, where it is the control's only boundary. Extracted, so frozen. |
| P0 | B Colour | `colors.hairline` | #e6e6e6 on #ffffff = 1.25:1, and the file assigned it to `text-input` — the single boundary of a form field. Worse than the value the harness flagged, and unflagged because the harness judges the strongest variant. |
| P1 | H States | all 23 component entries | Only `active` and `selected` were documented. The Iteration Guide actively instructed against hover ("Hover state is never documented"), so disabled, loading, error and focus-visible had no home anywhere. |
| P1 | B Colour | `colors.muted-soft` | #9a9a9a on #ffffff = 2.81:1 — fails AA at every size, and the file assigns it to "fine-print legal" copy at 14px/300, the worst legibility case in the system. Unflagged by the harness because `muted` wins the `text-dim` role. |
| P1 | B Colour | `colors.success`, `colors.warning` | 2.28:1 and 2.15:1 on canvas. The file described both as carrying "messages" and "callouts", i.e. text roles they cannot serve. |
| P2 | C Elevation | Elevation & Depth | Consistent — one mechanism (no shadow at all; colour-block and photographic depth only), correctly stated, and no `shadow:` group is needed because no rgba elevation is documented in the prose. No fix required. The layers themselves are near-indistinguishable (canvas/surface-card 1.04:1, canvas/surface-soft 1.07:1, canvas/surface-strong 1.19:1, surface-dark/surface-dark-elevated 1.18:1), which is a real property of the brand, not an error. |
| P2 | D Typography | all 14 roles | Every role carries family, size, weight, line height and letter spacing. Body on every surface this file defines passes 4.5:1 comfortably (`ink` 14.13–15.13:1, `body` 11.03:1). No fix required. |
| P2 | E Shapes | `rounded.pill` / `rounded.full` | Both are 9999px — a duplicate rung in the ladder, with `full` additionally documented as "9999px / 50%" in the prose table, a value that is not in the frontmatter. Left as-is: it is a documentation wart, not a wrong value, and resolving it would mean deleting an extracted token. |
| P2 | A Refs | prose | Zero dangling refs before and after. Every `{motion.*}`, `{colors.focus*}` and `{colors.hairline-control}` reference I added resolves. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | (absent) -> `hairline-control: "#8a8a8a"` | Parallel accessible boundary at 3.45:1 on canvas, per SPEC §2. The frozen #cccccc stays and is scoped to decoration. Labelled prescribed in the prose. |
| frontmatter `colors:` | (absent) -> `focus: "#0a1929"` | Fills the missing role. A deep navy from the `surface-dark` family: 17.74:1 on canvas, 3.40:1 even when crossing the blue button fill. A blue ring was rejected — `primary-active` on `primary` is 1.38:1, so BMW blue cannot ring its own button. |
| frontmatter `colors:` | (absent) -> `focus-on-dark: "#ffffff"` | The file documents dark signature surfaces (`hero-band-dark`, `cta-band-photo`), where `focus` collapses to 1.09:1. SPEC §1 requires the second ring in exactly this case. 16.24:1 on `surface-dark`. |
| frontmatter, new `motion:` group | (absent) -> 9 keys, Cinematic values | SPEC §4/§5. Base 400ms, slow 600ms, emphasis 900ms, stagger 80ms, long-decelerate `cubic-bezier(0.16, 1, 0.3, 1)`. |
| `## Colors` → Hairlines | 2 bullets -> 3 bullets, each with its measured ratio | States plainly that the real BMW site fails WCAG 1.4.11 on control boundaries, scopes `hairline` and `hairline-strong` to decoration, introduces `hairline-control`. |
| `## Colors` → new "Focus" subsection | (absent) -> 2 bullets | Documents both rings, their measured ratios on every surface, the 2px outside offset, and why a blue ring was rejected. |
| `## Colors` → Semantic | 3 bullets -> 4 bullets | Records the success/warning AA failures and restricts them to non-text roles; adds the `muted-soft` failure. |
| `button-secondary`, `filter-chip`, `text-input` prose | sole border was `hairline-strong` / `hairline` -> extracted value kept, `hairline-control` named for the load-bearing case | The boundary fix has to land where the boundary is actually drawn, not only in the token list. `text-input` also gains the focus ring. |
| `## Components` → new "### Component States" | (absent) -> table, 12 rows covering all 23 entries | SPEC §7. Extracted states (default, active/pressed, selected, disabled) separated from prescribed ones (hover, focus-visible, loading, error). Seven static entries are grouped as "default only"; `cookie-consent-card` and `text-link` say in words that they genuinely have few states. |
| new `## Motion & Animation` (after `## Components`) | (absent) -> first line states it is prescribed and unmeasured; 12-row interaction table; Rules; reduced-motion CSS | SPEC §3/§5/§6. Covers hover, press, focus, page transition, modal/drawer, dropdown, toast, list enter, list exit, loading, plus one brand emphasis row. `transform`/`opacity` only; every exit shorter than its entrance; the loader is the only infinite animation and there is no ambience loop. |
| new `## Accessibility` | (absent) -> 23-row contrast table, per-surface focus table, plain-language failure paragraph, tap target / colour-signal / reduced-motion / type-floor notes | SPEC §3. Tap-target language is explicitly marked as computed from padding, not measured, per SPEC's non-computable list. |
| `## Iteration Guide` item 5 | "Hover state is never documented. Only Default and Active/Pressed states." -> extracted vs prescribed split | The old line instructed future contributors to leave the gap this audit exists to close, and it now contradicts the States table. |
| `## Known Gaps` | animation "out of scope" -> motion/focus/boundary tokens labelled prescribed; tap-target unverifiability added | Honesty requirement: nothing added here is an extracted fact. |
| `## Do's and Don'ts` | +2 Do's, +2 Don'ts | Focus-ring usage, motion restraint, the hairline rule, and the no-layout-animation rule. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #262626 / canvas #ffffff | 15.13:1 | 4.5 | Pass |
| ink / surface-soft #f7f7f7 | 14.13:1 | 4.5 | Pass |
| ink / surface-card #fafafa | 14.50:1 | 4.5 | Pass |
| ink / surface-strong #ebebeb | 12.69:1 | 4.5 | Pass |
| body #3c3c3c / canvas | 11.03:1 | 4.5 | Pass |
| body-strong #1a1a1a / canvas | 17.40:1 | 4.5 | Pass |
| muted #6b6b6b / canvas | 5.33:1 | 4.5 | Pass |
| muted / surface-soft | 4.97:1 | 4.5 | Pass |
| muted-soft #9a9a9a / canvas | 2.81:1 | 4.5 | **Fail** (extracted, frozen) |
| on-primary #ffffff / primary #1c69d4 | 5.22:1 | 4.5 | Pass |
| on-primary / primary-active #0653b6 | 7.19:1 | 4.5 | Pass |
| on-dark #ffffff / surface-dark #1a2129 | 16.24:1 | 4.5 | Pass |
| on-dark / surface-dark-elevated #262e38 | 13.72:1 | 4.5 | Pass |
| on-dark-soft #bbbbbb / surface-dark | 8.46:1 | 4.5 | Pass |
| on-dark-soft / surface-dark-elevated | 7.15:1 | 4.5 | Pass |
| hairline #e6e6e6 / canvas | 1.25:1 | 3.0 | **Fail** (extracted, scoped to decoration) |
| hairline-strong #cccccc / canvas | 1.61:1 | 3.0 | **Fail** (extracted, scoped to decoration) |
| hairline-control #8a8a8a / canvas | 3.45:1 | 3.0 | Pass (prescribed) |
| hairline-control / surface-soft | 3.22:1 | 3.0 | Pass |
| hairline-control / surface-card | 3.31:1 | 3.0 | Pass |
| hairline-control / surface-strong | 2.90:1 | 3.0 | **Fail** — prose forbids bordered controls on the #ebebeb band |
| focus #0a1929 / canvas | 17.74:1 | 3.0 | Pass |
| focus / surface-soft | 16.56:1 | 3.0 | Pass |
| focus / surface-card | 16.99:1 | 3.0 | Pass |
| focus / surface-strong | 14.88:1 | 3.0 | Pass |
| focus / primary #1c69d4 | 3.40:1 | 3.0 | Pass |
| focus / primary-active #0653b6 | 2.47:1 | 3.0 | **Fail** — reason the ring is specified 2px outside the control |
| focus / surface-dark | 1.09:1 | 3.0 | **Fail** — reason `focus-on-dark` exists |
| focus-on-dark #ffffff / surface-dark | 16.24:1 | 3.0 | Pass |
| focus-on-dark / surface-dark-elevated | 13.72:1 | 3.0 | Pass |
| primary #1c69d4 / canvas | 5.22:1 | 4.5 | Pass |
| primary / surface-soft | 4.88:1 | 4.5 | Pass |
| primary / surface-card | 5.00:1 | 4.5 | Pass |
| m-blue-light #0066b1 / canvas | 5.94:1 | 4.5 | Pass |
| m-red #e22718 / canvas | 4.63:1 | 4.5 | Pass |
| error #dc2626 / canvas | 4.83:1 | 4.5 | Pass |
| error / surface-soft | 4.51:1 | 4.5 | Pass (at threshold) |
| success #22c55e / canvas | 2.28:1 | 4.5 | **Fail** (extracted; non-text use only) |
| warning #f59e0b / canvas | 2.15:1 | 4.5 | **Fail** (extracted; non-text use only) |
| muted / primary-disabled #d6d6d6 | 3.67:1 | — | Exempt (disabled) |
| canvas / surface-soft (layer separation) | 1.07:1 | — | Informational |
| canvas / surface-card | 1.04:1 | — | Informational |
| canvas / surface-strong | 1.19:1 | — | Informational |
| surface-dark / surface-dark-elevated | 1.18:1 | — | Informational |

Every ratio above was computed with a `python3` WCAG 2.1 relative-luminance snippet; none is estimated.

### Motion inventory

Profile: **Cinematic**. Prescribed, not measured — stated as the first line of the file's Motion & Animation section.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, chip, tab, link) | `{motion.duration-fast}` 200ms | `{motion.ease-standard}` | `opacity` (overlay), no travel | Instant colour/border change, no transition |
| Hover (card photo) | `{motion.duration-base}` 400ms | `{motion.ease-standard}` | `transform: scale(1 → 1.03)` | Scale removed; photo stays at 1.0 |
| Press | `{motion.duration-instant}` 120ms | `{motion.ease-exit}` | `opacity`, `transform: scale(0.99)` | Scale removed; fill shift instant |
| Focus (ring appear) | `{motion.duration-instant}` 120ms | `{motion.ease-enter}` | `opacity` on the ring | Ring appears instantly, never suppressed |
| Page / route transition | 600ms in / 400ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(24px → 0)` | Travel removed; cross-fade ≤150ms |
| Modal / drawer (mobile nav sheet) | 400ms in / 200ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateX(100% → 0)`, scrim `opacity` | Slide removed; fade at 150ms |
| Dropdown (language picker, mega-menu) | 200ms in / 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px → 0)` | Travel removed; 120ms fade |
| Toast (configurator confirmation) | 400ms in / 200ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px → 0)` | Travel removed; 150ms fade, hold unchanged |
| List enter (model-card grid, inventory) | `{motion.duration-slow}` 600ms, `{motion.stagger-step}` 80ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(24px → 0)` | Stagger and travel removed; one grid fade at 150ms |
| List exit (filtered-out cards) | `{motion.duration-base}` 400ms | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Scale removed; 150ms fade |
| Loading (indeterminate bar, render swap) | 1200ms loop | `{motion.ease-standard}` | `transform: translateX` on a 2px primary bar | Loop frozen; static bar plus "Loading" text |
| Emphasis — hero vehicle settle | `{motion.duration-emphasis}` 900ms | `{motion.ease-standard}` | `transform: scale(1.04 → 1)`, headline `opacity` one stagger later | Removed; hero renders at final position |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line ~189 (`NEGATED` / `lead` window) | The negation check reads `line[m.start()-80 : m.start()+10]`, i.e. the text *before* the verb. A correct prohibition written verb-first — "Animate `transform` and `opacity` only — never `width`, `height`…" — is flagged as a violation, while "never animate width" passes. I reworded my own line to verb-last to get a clean run, which means the harness is shaping prose rather than measuring it. | Take the negation window from the whole clause, not just the lead: `lead = line[max(0, m.start()-80) : m.end()+40]`, or search the full line when the match starts within the first ~20 characters. |
| `theme-audit/audit.py` line ~148 (`check` calls) | Only the *representative* token per role is contrast-checked, so a file's second-worst offender is invisible. Here `text-dim` resolves to `muted` (5.33:1, passes) and `muted-soft` (2.81:1, fails AA at every size, used for legal copy) is never reported. Likewise `border` resolves to the *strongest* hairline, hiding `hairline` at 1.25:1 — the worse value, and the one assigned to `text-input`. | Check every key matching a role pattern, not just the representative, and report the worst as the role's score while listing the rest. For `border` this is the inverse of `find_role_strongest`: the strongest is the right token to *judge coverage* on, but the weakest is the right one to *warn* about. |
| `theme-audit/audit.py` line ~155 (`signals` regex) | Signal colours are matched on `^(primary|accent|secondary|brand|cta)`, so `success`, `warning` and `error` are never contrast-checked despite being text-carrying semantic colours in most files. BMW's `success` (2.28:1) and `warning` (2.15:1) pass the harness untouched. | Add `success|warning|error|danger|info|positive|negative` to the signal pattern, checked against the file's own body ink on canvas rather than `on-accent`. |
| `theme-audit/SPEC.md` §4 | The motion token block is given as one literal YAML sample with Crisp-ish values (`duration-base: 250ms`, `cubic-bezier(0.2, 0, 0, 1)`), then §5 says "values are per profile, not identical across files" — but §5's table only fixes base duration, easing *bias* and stagger. `duration-instant`, `duration-slow`, `duration-emphasis`, `ease-enter` and `ease-exit` have no per-profile values anywhere, so 84 agents will each invent a different ladder and the files will not be comparable. | Add a per-profile values table to §5 giving all nine keys for each of Crisp / Calm / Playful / Cinematic, and mark §4's block as the schema only. |
| `theme-audit/SPEC.md` §5 assignment rule 1 | Rule 1 reads "Dark canvas **+** luxury/automotive/hardware identity → Cinematic". BMW corporate is unambiguously luxury automotive but its canvas is `#ffffff`; taken literally the conjunction fails and BMW falls through to rule 4, Calm. The roster assigns Cinematic, so the rule as written contradicts its own output. | Make the conjunction a disjunction with a tie-break, e.g. "Luxury/automotive/hardware identity, **or** a dark canvas → Cinematic", or add "a light-canvas brand whose page rhythm is built on full-bleed product photography still counts". |
| `design-md/bmw/DESIGN.md` vs `design-md/bmw-m/DESIGN.md` | Not an issue to fix, but worth recording for the roster: these two files are the same brand family and cross-reference each other's numbers ("tighter than BMW M's 96px", "M's 32px card padding"). If A07/whoever owns `bmw-m` changes those values, this file's comparisons go stale. Neither agent can edit the other's file. | A reconciliation pass over the bmw / bmw-m pair after both audits land. |

### Needs approval

1. **`colors.muted-soft` #9a9a9a at 2.81:1 on canvas.** Extracted; not changed. The file assigns it to "disabled text, fine-print legal" at `{typography.body-sm}` (14px / weight 300). Nearest passing value for normal-size text is **#767676 (4.54:1)**; **#949494 (3.03:1)** is the floor if the usage is narrowed to 18px+ or 14px-bold, under the AA large-text 3:1 rule. Usage note that would make the real value defensible: *restrict #9a9a9a to disabled control labels only, where WCAG sets no requirement, and move all legal fine print to `{colors.muted}` (5.33:1).* Needs a brand decision because it is a real extracted tone.
2. **`colors.success` #22c55e (2.28:1) and `colors.warning` #f59e0b (2.15:1) on canvas.** Extracted; not changed. Nearest passing values, holding hue and darkening only, are **#178841 (4.53:1)** for success and **#a46a07 (4.52:1)** for warning. Usage note applied in the file instead: *fill, icon and bar roles only, with the message text in `{colors.body}`* — which keeps the real hexes defensible without a swap. Approve either the usage restriction or the darker pair.
3. **`colors.hairline` #e6e6e6 (1.25:1) and `colors.hairline-strong` #cccccc (1.61:1).** Extracted; not changed, per SPEC's frozen-value rule. I added `hairline-control` #8a8a8a (3.45:1) alongside and scoped the originals to decoration. This is a documented statement that **the real BMW corporate site fails WCAG 1.4.11 on control boundaries** — confirm that saying so in the file is wanted before it ships.
4. **Three prescribed colour tokens added to a frontmatter that otherwise holds only extracted hexes:** `focus` #0a1929, `focus-on-dark` #ffffff, `hairline-control` #8a8a8a. All three are labelled prescribed in the prose and in Known Gaps, but they do raise `color_count` from 25 to 28 and will read as BMW values to anyone who skims only the YAML. If that is unacceptable, the alternative is a separate `prescribed:` group — which the harness does not look for, so it would re-break the `focus` role.
5. **`hairline-control` on `surface-strong` is 2.90:1**, just under 3.0. I handled it in prose ("do not place a bordered control on the #ebebeb divider band") rather than by darkening the token, because darkening it further pulls the boundary away from the brand's light-grey hairline character. Darkening to #858585 (3.69:1 on canvas, 3.10:1 on #ebebeb) would close it if preferred.

### Identity verdict

Still BMW, and specifically BMW *corporate* rather than BMW M. The things that make the file identifiable are untouched: the 700/300 BMW Type Next Latin split, the single blue CTA, `{rounded.none}` on every control, the light-canvas → dark-navy-hero → light rotation, the explicit no-shadow rule, the M tricolor stripe quarantined to M contexts, and the 80px/24px rhythm the file itself frames as tighter than BMW M's 96px/32px.

The additions were written to that voice rather than to a generic template. The focus ring is drawn from the brand's own `surface-dark` navy family instead of a stock blue or the usual #005fcc, and the file explains that BMW blue was rejected because it cannot ring its own button — a conclusion that only applies to this brand. The motion section argues the *restrained* Cinematic reading: 16–24px of travel, scale under 1.04, premium carried by a long decelerate rather than by distance, with an explicit note that there is no ambience loop because BMW corporate's depth comes from photography and colour blocks. The hero-settle row is the one piece of real brand choreography.

**On the assigned profile:** Cinematic is right, and I kept it. SPEC §5 rule 1 technically does not fire — BMW's canvas is #ffffff, not dark — but the brand is flagship luxury automotive, the page rhythm is built on full-bleed vehicle photography and dark navy hero bands, and the file's own description says "measured and settled". Calm would be the literal rule-4 fallback and would be wrong: it would flatten the hero photography to an opacity fade and lose the one thing that makes an automotive site feel like one. The rule's wording is the defect, not the assignment; it is logged under Shared issues.

The one honest risk is volume. The file was ~545 lines and is now ~700, with the Accessibility contrast table being the largest single block. That table is measurement, not identity, and it reads as audit apparatus bolted onto a brand document. It earns its place because the brand's real AA failures were previously invisible, but if the collection later wants the identity-to-apparatus ratio protected, the per-pair tables are the first thing to move to a sibling file.
