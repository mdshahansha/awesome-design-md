## A13 · clickhouse

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 4 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

All three harness findings confirmed independently: `focus` was the only missing colour role; `hairline-strong` (#3a3a3a) on `canvas` (#0a0a0a) measures 1.74:1 against a 3.0:1 requirement; `Motion & Animation` and `Accessibility` were both absent; the Components section documented only `active`.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Nothing in the file said how any state change is timed. |
| P0 | A Tokens | `colors.focus` | No focus ring token anywhere. Nothing in the file told a builder what a keyboard-focused control looks like, and `text-input-focused` pointed at `{colors.primary}`, which measures 1.00:1 on the file's own yellow CTA bands. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. The file's two genuine AA failures (hairlines as boundaries, `muted-soft` as text) were undisclosed. |
| P0 | H States | Components | Seven of eight states undocumented. Worse, the file actively forbade documenting them: Iteration Guide item 4 read "Never document hover. Default and Active/Pressed states only," and the Don'ts banned hover styling. That is a direct contradiction of SPEC §7, not an omission. |
| P1 | B Colour | `colors.hairline-strong` | 1.74:1 on canvas, and 1.53:1 on `surface-card` — the surface it was actually described as underlining ("input underlines"). The extracted value cannot be the only boundary of a text input. |
| P1 | B Colour | `colors.hairline` | 1.38:1 on canvas, 1.21:1 on `surface-card`. Prose called it "1px borders on cards" with no note that it is invisible as a boundary. |
| P1 | B Colour | `colors.muted-soft` | 2.87:1 on canvas, used for "tertiary text — fine print." Fails AA for text at any size, and fails even the 3:1 large-text threshold. The harness never saw this: `text-dim` resolves to `muted` (5.58:1), so the weaker tone was hidden behind the stronger one. |
| P1 | C Elevation | surface ladder | `surface-soft`/`canvas` = 1.06:1, `surface-card`/`canvas` = 1.14:1, `surface-elevated`/`surface-card` = 1.12:1. The layers are effectively indistinguishable as fills, and the file claimed depth came from exactly that contrast. |
| P1 | C Elevation | Elevation table | Expressed two ways at once — "Soft hairline: 1px border" and "Surface card: background, no shadow" — with no rule for which applies when. |
| P1 | E Focus ring | Shapes | No ring geometry, no border-width ladder. Radius ladder itself was clean. |
| P2 | B Colour | `colors.muted` on `surface-elevated` | 4.38:1, just under 4.5. Legal at 18px+, a fail below it; previously unstated. |
| P2 | D Typography | all roles | Every role already carried family, size, weight, line height and letter spacing. Body on every defined surface clears 4.5:1 comfortably (10.84:1 on `surface-card`). No defect. |
| P2 | A Tokens | `colors.success` / `error` / `warning` | Duplicate the `accent-*` hexes exactly. Harmless aliasing, left alone; `error` is now referenced by `text-input-error`, which gives it a job. |
| P2 | E Shapes | `rounded.pill` / `rounded.full` | Same 9999px value under two names. Intentional (semantic split), now stated as such rather than left looking like a ladder defect. |
| P2 | G Accessibility | tap targets | 40px buttons, 40px inputs, 36px icon button — all below 44 × 44. The file already flagged the icon button; it did not flag the other three. Declared values only, not measured. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `border-control: "#6e6e6e"` | Parallel accessible boundary per SPEC §2. 3.88:1 on canvas, 3.04:1 on the tightest surface (`surface-elevated`). Extracted hairlines untouched. |
| frontmatter `colors:` | — -> `focus: "#7a7f10"` | The missing role. Brand yellow pushed into the one luminance band that clears 3:1 on both the black surface family and the yellow bands, so one ring serves the whole system. |
| frontmatter | — -> `motion:` group, 9 keys | Crisp profile per SPEC §4/§5: base 150ms, near-linear-out easing, 20ms stagger. |
| frontmatter `components:` | `text-input` -> adds `borderColor: {colors.border-control}` | The input needed a visible edge. |
| frontmatter `components:` | `text-input-focused` -> adds `borderColor: {colors.focus}` | Was described as yellow-on-dark only; yellow is invisible on a yellow band. |
| frontmatter `components:` | — -> `text-input-error`, `focus-ring` | Error state and ring geometry needed referenceable keys. |
| `## Colors` | — -> hairline scoping paragraph + `border-control` + `focus` entries | States the AA failure plainly, scopes the frozen tones to decoration, labels both new tokens as prescribed with every measured ratio. |
| `## Elevation & Depth` | — -> "Measured layer separation" paragraph | Records the three fill ratios and settles elevation on one expression: tone plus optional 1px hairline, never shadow. |
| `## Shapes` | — -> Border Widths table + Focus Ring Geometry | Ladder for 1px decorative / 1px control / 2px ring, and the ring's radius inheritance. |
| `## Components` | `text-input` / `text-input-focused` prose rewritten; `text-input-error` added | Explains why `hairline-strong` is not the input's edge (1.53:1 on its own fill). |
| `## Components` | — -> `### Component States` table, 14 components × 8 states | SPEC §7. Badges and stat callouts are marked default-only, because they genuinely are. Extracted vs prescribed stated in the lead-in. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Tokens table, 14-row interaction inventory, motion rules, `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | — -> `## Accessibility` | 19-row measured contrast table, 6-surface focus-ring table, declared tap targets, colour-is-never-the-only-signal, reduced motion. |
| `## Don'ts` | "Don't add hover state styling beyond what the system already encodes" -> three rules: no *movement* on hover/press, never suppress the ring, never use a hairline as a control boundary | The old line forbade exactly what SPEC §7 requires. Rewritten to forbid the thing that actually matters for Crisp: travel. |
| `## Iteration Guide` item 4 | "Never document hover. Default and Active/Pressed states only." -> "Document every state a component supports…" | Same contradiction. |
| `## Known Gaps` | animation line -> explicit "no motion value in this file was measured"; added prescribed-token gap, prescribed-state gap, declared-vs-measured tap-target gap | Keeps the prescribed/extracted boundary honest. |

No brand hex was changed. No existing extracted value was altered anywhere in the file.

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #ffffff / canvas #0a0a0a | 19.80 | 4.5 | Pass |
| ink / surface-soft #121212 | 18.73 | 4.5 | Pass |
| ink / surface-card #1a1a1a | 17.40 | 4.5 | Pass |
| ink / surface-elevated #242424 | 15.52 | 4.5 | Pass |
| body #cccccc / canvas | 12.33 | 4.5 | Pass |
| body / surface-card | 10.84 | 4.5 | Pass |
| body-strong #e6e6e6 / canvas | 15.86 | 4.5 | Pass |
| muted #888888 / canvas | 5.58 | 4.5 | Pass |
| muted / surface-soft | 5.28 | 4.5 | Pass |
| muted / surface-card | 4.91 | 4.5 | Pass |
| muted / surface-elevated | 4.38 | 4.5 | **Fail** |
| muted-soft #5a5a5a / canvas | 2.87 | 4.5 | **Fail** |
| on-primary #0a0a0a / primary #faff69 | 18.45 | 4.5 | Pass |
| on-primary / primary-active #e6eb52 | 15.43 | 4.5 | Pass |
| on-primary / accent-emerald #22c55e | 8.69 | 4.5 | Pass |
| on-primary / accent-rose #ef4444 | 5.26 | 4.5 | Pass |
| on-primary / accent-blue #3b82f6 | 5.38 | 4.5 | Pass |
| on-primary / warning #f59e0b | 9.22 | 4.5 | Pass |
| primary / canvas | 18.45 | 4.5 | Pass |
| primary / surface-card | 16.22 | 4.5 | Pass |
| hairline #2a2a2a / canvas | 1.38 | 3.0 | **Fail** — frozen, decoration only |
| hairline-strong #3a3a3a / canvas | 1.74 | 3.0 | **Fail** — frozen, decoration only |
| hairline-strong / surface-card | 1.53 | 3.0 | **Fail** — frozen, decoration only |
| border-control #6e6e6e / canvas | 3.88 | 3.0 | Pass (prescribed) |
| border-control / surface-soft | 3.67 | 3.0 | Pass (prescribed) |
| border-control / surface-card | 3.41 | 3.0 | Pass (prescribed) |
| border-control / surface-elevated | 3.04 | 3.0 | Pass (prescribed) |
| focus #7a7f10 / canvas | 4.59 | 3.0 | Pass (prescribed) |
| focus / surface-soft | 4.35 | 3.0 | Pass (prescribed) |
| focus / surface-card | 4.04 | 3.0 | Pass (prescribed) |
| focus / surface-elevated | 3.60 | 3.0 | Pass (prescribed) |
| focus / primary #faff69 | 4.02 | 3.0 | Pass (prescribed) |
| focus / primary-active #e6eb52 | 3.36 | 3.0 | Pass (prescribed) |
| surface-soft / canvas | 1.06 | — | layer separation, informational |
| surface-card / canvas | 1.14 | — | layer separation, informational |
| surface-elevated / surface-card | 1.12 | — | layer separation, informational |

Rejected ring candidates, measured not guessed: #faff69 → 18.45 on canvas but 1.00 on the yellow band. #ffffff → 19.80 on canvas, 1.07 on the band. #e6eb52 → 15.43 / 1.20. Only a mid-luminance value (relative luminance between 0.109 and 0.282) can clear 3:1 at both ends; #7a7f10 sits at 0.194 with margin on every surface.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | opacity, fill/colour crossfade | Unchanged — no travel exists to remove |
| Press | 60ms | `{motion.ease-standard}` | fill swap only; no transform scale | Unchanged |
| Focus (ring appears) | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | opacity 0→1 | Instant at full opacity |
| Page / route transition | 100ms | `{motion.ease-standard}` | opacity 0→1 on incoming main | None |
| Modal / drawer enter | `{motion.duration-slow}` 220ms | `{motion.ease-enter}` | opacity + translateY 8px→0 | opacity only, 150ms |
| Modal / drawer exit | 100ms | `{motion.ease-exit}` | opacity + transform reversed | opacity only, 100ms |
| Dropdown enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | opacity + translateY −4px→0 | opacity only, 150ms |
| Dropdown exit | 60ms | `{motion.ease-exit}` | opacity 1→0 | opacity only, 60ms |
| Toast enter | 150ms | `{motion.ease-enter}` | opacity + translateY 12px→0 | opacity only, 150ms |
| Toast exit | 100ms | `{motion.ease-exit}` | opacity + translateY 0→8px | opacity only, 100ms |
| List enter | 150ms, 20ms stagger, 6 items max | `{motion.ease-enter}` | opacity + translateY 6px→0 | No stagger, no travel; one 150ms fade |
| List exit | 100ms, no stagger | `{motion.ease-exit}` | opacity 1→0 | opacity only, 100ms |
| Loading | 800ms linear, infinite | linear | transform: rotate (spinner); opacity 0.4↔0.8 (skeleton) | Spinner frozen on one frame; skeleton static at 0.4; text status carries the state |

Every exit is shorter than its entrance. Only transform and opacity appear. The spinner is the only infinite animation; this brand has no ambient motion.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py:129-132` and `:163-164` | `find_role_strongest` picks the focus token with the *highest* contrast against the canvas, then `check("focus", "accent", 3.0, …)` tests that same token against the accent. On a brand whose accent is near-white in luminance (ClickHouse yellow at 0.947), the two checks pull in opposite directions, and a file that correctly scopes two rings — a bright one for dark surfaces, a dark one for the yellow bands — is reported as failing no matter which it defines. SPEC §1 explicitly allows that two-token split; the harness cannot model the scoping. | Resolve the focus role per background: for the `focus` on `<bg>` check, pick the matching focus-\* token with the highest contrast against *that* background, rather than resolving once against the canvas. |
| `theme-audit/audit.py:158-161` | Contrast is checked only against the single representative token per role, so a weaker same-role tone is invisible to the harness. Here `text-dim` resolved to `muted` (5.58:1) and `muted-soft` at 2.87:1 was never measured; `surface` resolved to `surface-soft` and `surface-elevated` was never used as a background. | For `text` and `text-dim`, check every matching token against every matching `surface` token, and report the worst pair rather than the representative one. |
| `theme-audit/audit.py:187` (`durations_found`) | The regex `\b(\d{2,4})ms\b` picks `001` out of `animation-duration: 0.001ms`, so a correct reduced-motion block reports a nonsense 1ms duration. Cosmetic — it does not affect the score once a full motion section exists. | Require a word or non-dot boundary before the digits: `(?<![.\d])(\d{2,4})ms\b`. |
| `theme-audit/SPEC.md` §1 | The two-ring rule is written only in the light-surface direction ("defines `focus` **and** `focus-on-dark`"). A dark-canvas brand with a near-white accent surface needs the mirror of that, and the spec offers no name for it. | Name the pair by surface rather than by polarity, e.g. `focus` plus `focus-alt`, with the Accessibility section stating which surface each is drawn on. |

### Needs approval

1. **`{colors.muted-soft}` #5a5a5a at 2.87:1 on canvas.** Extracted value, documented as "tertiary text — fine print." It fails AA for normal text (4.5:1) and also fails the 3:1 large-text threshold, so no usage note rescues it as written. Nearest passing value for 4.5:1 is **#7a7a7a (4.61:1)**; the nearest value that would make the current *large-text* framing defensible is **#606060 (3.15:1)**, with the usage note "18.66px+ / 24px bold only." Left unchanged — it is a real brand tone and changing it would falsify the document. Recorded here instead.
2. **`{colors.muted}` #888888 on `{colors.surface-elevated}` #242424 at 4.38:1.** Fails 4.5:1 by a hair. Defensible as-is with the usage note "on nested elevated cards, `{colors.muted}` is for 18px+ labels only, where 3:1 applies" — which is what the Accessibility section now says. Nearest passing value on that surface is **#8e8e8e (4.74:1)**. Not changed.
3. **The extracted hairlines, 1.38:1 and 1.74:1 on canvas.** Handled per SPEC §2 with a parallel prescribed token and the failure stated plainly in the file. Flagged here for the record: a reader who follows the brand literally and uses `{colors.hairline}` as an input border ships an invisible control boundary.
4. **Prescribed `{colors.focus}` #7a7f10 and `{colors.border-control}` #6e6e6e.** Neither was sampled from ClickHouse. Both are labelled prescribed in the file and in Known Gaps, but they are new hexes entering a brand document and should be signed off by whoever owns the brand.
5. **Declared tap targets below 44 × 44 everywhere** (40px buttons and inputs, 36px icon button, ~36px tabs). The fix recommended in the file — hold the painted box, extend the pointer target to 44px — is prescribed and changes no visual value, but it is a behavioural change to the brand's components.
6. **Two Iteration Guide / Don'ts rules were reversed**, not just extended: the file previously instructed readers never to document hover. If that instruction reflected a deliberate editorial policy rather than an artifact of static-screenshot extraction, the rewrite needs sign-off.

### Identity verdict

Still unmistakably ClickHouse. The identity in this file is carried by three things — the near-pure black canvas, electric yellow #faff69 doing every piece of signal work, and SQL code windows as the hero artifact — and none of them moved. The additions lean *into* that: the focus ring is the brand yellow driven down in luminance rather than a borrowed blue, the prescribed boundary is a neutral grey so it cannot compete with the yellow, the Elevation note defends the brand's deliberately flat 1.14:1 panel look instead of proposing shadows, and the states table is written in the file's own vocabulary (`stat-callout`, `code-window-card`, `cta-band-yellow`) rather than in generic component names. The Motion section explicitly forbids stat-counter count-up and typewriter effects — a decision that only makes sense for this brand, where the credibility number must be readable the instant the band paints.

**Crisp is the right profile and I kept it.** SPEC §5 rule 2 (terminal, IDE, infra or developer-tool identity) applies cleanly: JetBrains Mono code blocks, embedded query-console product fragments, SQL as the marketing payload, and a Don't that says "the code IS the marketing voltage." Rule 1 (dark canvas + luxury/automotive/hardware) is the only competing candidate and it does not apply — there is no imagery-led atmosphere here, no gradients, and the file's own Whitespace Philosophy says "engineering-grade rather than marketing-soft." Crisp's no-press-pop signature also happens to preserve the file's original instinct that hover and press should not be theatrical; the old "never document hover" rule was the wrong expression of a correct feeling, and the rewrite keeps the feeling.

The one real identity risk is bulk: the file grew by roughly 150 lines of tables, and tables read flatter than the prose voice the Overview and Colors sections have. Mitigated by keeping every new row anchored to a named ClickHouse component, but a future editor should resist adding more generic rows.
