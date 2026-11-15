## A21 · expo

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 1 | 3 | 1 | 1 |
| After | 5 | 5 | 5 | 5 | 5 | 5 |

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A Token contract | `colors.focus` | No focus colour anywhere in the file; no component documented a focus treatment, so keyboard users had no specified indicator on any of the six surfaces this file defines. |
| P0 | F Motion | frontmatter + sections | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Known Gaps declared animation "out of scope". |
| P0 | G Accessibility | sections | No `## Accessibility` section; every contrast failure below was undisclosed. |
| P0 | B Colour | `semantic-error` #eb8e90 | 2.39:1 on white. Documented as the colour for "Validation errors" — error text in it is unreadable at any size. The harness never checks semantic tokens, so this was invisible to scoring. |
| P1 | B Colour | hairline ladder | All three extracted hairlines fail the 3:1 boundary threshold (1.09, 1.14, 1.35:1). `hairline-strong` is prose-specified as the only outline of `text-input`, `feature-card`, `pricing-tier-card` — i.e. the sole boundary of a control. |
| P1 | B Colour | `muted` #999999 | 2.85:1 on canvas and on surface-card, used for "Sub-titles" — body-size secondary text below AA. |
| P1 | B Colour | `muted-soft` #cccccc | 1.61:1, named as disabled text but not name-exempt, and nothing in the file forbade live copy in it. |
| P1 | B Colour | `text-link-secondary` #476cff | 4.32:1 — marginal AA fail on the legal footer link, undisclosed. |
| P1 | B Colour | `accent-link-bright` #47c2ff | 2.01:1 on canvas. The file did not state it is a dark-surface-only tone. |
| P1 | B Colour | `semantic-success` #16a34a | 3.30:1 — fine for icons, fails for body copy; no size scoping stated. |
| P1 | H States | all 22 components | Only `active` was documented (as the captured `button-primary-active` fill). Hover, focus-visible, pressed, disabled, loading, selected and error were named nowhere in a component entry. |
| P1 | A Token contract | dark surfaces | The file documents both a white canvas and a #171717 signature surface (code blocks, dark feature cards, featured pricing). One ring cannot serve both: brand blue is 3.76:1 on #171717 and bright cyan is 2.01:1 on white — SPEC section 1 requires a `focus` / `focus-on-dark` pair here. |
| P2 | C Elevation | Elevation & Depth table | Elevation is expressed two ways at once — hairline border *and* a single soft drop shadow — and the shadow `rgba(0,0,0,0.04)` has no token, so nothing can reference it. Not fixed: the mixed treatment is what the real site does, and a `shadow:` group would be a token the prose does not otherwise reference. Flagged only. |
| P2 | E Ladders | `rounded.pill` / `rounded.full` | Two keys, one value (9999px). The ladder has a duplicate rung. Left alone — both are referenced in prose with distinct uses. |
| P2 | D Typography | all roles | Every role carries size, weight and line height; body (16px/400/1.5, #60646c at 5.94:1) is readable on both white surfaces. No defect found. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `muted-strong: "#6b6f76"` | Parallel accessible secondary-text token (5.05:1); extracted `muted` stays frozen. SPEC section 2. |
| frontmatter `colors:` | — -> `border-control: "#86888f"` | Parallel accessible boundary (3.54:1 on white, 3.11:1 on #f0f0f3) for controls whose only definition is their outline. The three real hairlines stay frozen, scoped to decoration. |
| frontmatter `colors:` | — -> `semantic-error-text: "#b3261e"` | Accessible error ink (6.54:1); extracted #eb8e90 re-scoped to borders and tints. |
| frontmatter `colors:` | — -> `focus: "#0d74ce"`, `focus-on-dark: "#47c2ff"` | Fills the missing `focus` role. Both reuse colours the brand already owns. Pair required because the file has two surface polarities. |
| frontmatter | — -> `motion:` group, Crisp block verbatim | SPEC section 4. Copied literally, including `duration-reduced: 100ms`, so sibling Crisp files stay comparable. |
| Colors › Hairlines | three bullets -> same three relabelled decorative, plus `border-control` and a lead-in stating none reaches 3:1 | Disclosure plus a usable alternative. |
| Colors › Text | `muted` / `muted-soft` bullets -> same, with measured ratios and size scoping; `muted-strong` added | Disclosure at the point of use. |
| Colors › Semantic | success/error bullets -> same, with ratios and scoping; `semantic-error-text` added | Error colour was the worst real failure in the file. |
| Colors › Focus | — -> new sub-section documenting both rings with measured ratios | A new role needs prose, not just a token. |
| Components › `text-input` | `1px {colors.hairline-strong}` border, "Focus thickens border to 2px ink" -> `{colors.border-control}` border, 2px `{colors.focus}` ring with canvas offset, error state named | A 1.35:1 outline cannot be a control's only boundary; the old focus note gave a thickness but no visible indicator colour. |
| Components | — -> `### Interaction States` table, 22 rows | Every component names its states; the eleven genuinely static ones say "default only" rather than being padded. First line marks all but `button-primary-active` as prescribed. |
| after Components | — -> `## Motion & Animation` | Required section. First line states the system is prescribed and unmeasured. Table covers hover, press, focus, page transition, modal/drawer open and close, dropdown, toast, list enter, list exit, loading, plus the hero mockup entrance. `transform`/`opacity` only; every exit shorter than its entrance. Closes with the reduced-motion rule and a CSS block. |
| after Motion | — -> `## Accessibility` | Required section: passing pairs, disclosed failures, focus-ring ratio per surface, tap targets (declared not measured), reduced motion. |
| Iteration Guide item 5 | "Hover state never documented." -> states/motion sourcing rule | Stale once the states table landed. |
| Known Gaps | "Animation timings … out of scope." -> four lines naming what is prescribed vs extracted | The audit replaced the gap with a prescription; saying so is the honest record. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via the harness's own `contrast()`;
no ratio here is estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #171717 / canvas #ffffff | 17.93:1 | 4.5 | Pass |
| ink #171717 / surface-card #ffffff | 17.93:1 | 4.5 | Pass |
| body #60646c / canvas | 5.94:1 | 4.5 | Pass |
| body #60646c / canvas-soft #fafafa | 5.69:1 | 4.5 | Pass |
| on-primary #ffffff / primary #000000 | 21.00:1 | 4.5 | Pass |
| on-dark #ffffff / surface-dark #171717 | 17.93:1 | 4.5 | Pass |
| on-dark-soft #b0b4ba / surface-dark | 8.61:1 | 4.5 | Pass |
| text-link #0d74ce / canvas | 4.77:1 | 4.5 | Pass |
| accent-warning #ab6400 / canvas | 4.61:1 | 4.5 | Pass |
| accent-preview #8145b5 / canvas | 6.08:1 | 4.5 | Pass |
| muted-strong #6b6f76 / canvas (prescribed) | 5.05:1 | 4.5 | Pass |
| muted-strong #6b6f76 / surface-strong #f0f0f3 | 4.44:1 | 4.5 | Fail — noted in file; ink used instead |
| border-control #86888f / canvas (prescribed) | 3.54:1 | 3.0 | Pass |
| border-control #86888f / surface-strong #f0f0f3 | 3.11:1 | 3.0 | Pass |
| semantic-error-text #b3261e / canvas (prescribed) | 6.54:1 | 4.5 | Pass |
| focus #0d74ce / canvas | 4.77:1 | 3.0 | Pass |
| focus #0d74ce / canvas-soft #fafafa | 4.57:1 | 3.0 | Pass |
| focus #0d74ce / surface-strong #f0f0f3 | 4.19:1 | 3.0 | Pass |
| focus #0d74ce / gradient-sky-light #cfe7ff | 3.75:1 | 3.0 | Pass |
| focus #0d74ce / gradient-sky-mid #a8c8e8 | 2.74:1 | 3.0 | Fail — mandatory 2px canvas offset carries the edge (offset vs #a8c8e8 = 3.75:1) |
| focus #0d74ce / surface-dark #171717 | 3.76:1 | 3.0 | Passes, but focus-on-dark is specified instead |
| focus-on-dark #47c2ff / surface-dark #171717 | 8.90:1 | 3.0 | Pass |
| focus-on-dark #47c2ff / surface-dark-elevated #1a1a1a | 8.64:1 | 3.0 | Pass |
| hairline-soft #f5f5f7 / canvas | 1.09:1 | 3.0 | Fail — extracted, disclosed, scoped to decoration |
| hairline #f0f0f3 / canvas | 1.14:1 | 3.0 | Fail — extracted, disclosed, scoped to decoration |
| hairline-strong #dcdee0 / canvas | 1.35:1 | 3.0 | Fail — extracted, disclosed |
| muted #999999 / canvas | 2.85:1 | 4.5 | Fail — extracted, disclosed; clears 3:1 so defensible at 24px+ only |
| muted #999999 / surface-card | 2.85:1 | 4.5 | Fail — extracted, disclosed |
| muted-soft #cccccc / canvas | 1.61:1 | 4.5 | Fail — extracted, disclosed; disabled text only |
| muted-soft #cccccc / surface-card | 1.61:1 | 4.5 | Fail — extracted, disclosed |
| semantic-error #eb8e90 / canvas | 2.39:1 | 4.5 | Fail — extracted, disclosed; re-scoped to tints |
| semantic-success #16a34a / canvas | 3.30:1 | 4.5 | Fail — extracted, disclosed; icons and 24px+ only |
| text-link-secondary #476cff / canvas | 4.32:1 | 4.5 | Fail — extracted, disclosed |
| accent-link-bright #47c2ff / canvas | 2.01:1 | 4.5 | Fail — extracted, disclosed; dark-surface tone only |

### Motion inventory

Profile: Crisp, values literal from SPEC section 4. Prescribed, not measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card, tile) | 100ms `{motion.duration-fast}` | `{motion.ease-standard}` | opacity, translateY(-1px) | Travel removed; opacity at 100ms |
| Press | 60ms `{motion.duration-instant}` | `{motion.ease-standard}` | scale(0.98) | Scale removed; instant |
| Focus ring appears | 60ms `{motion.duration-instant}` | `{motion.ease-standard}` | opacity | Unchanged |
| Page / route transition | 150ms in `{motion.duration-base}`, 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity | Cross-fade at 100ms |
| Modal / drawer open | 150ms `{motion.duration-base}` | `{motion.ease-enter}` | opacity, translateY(8px) to 0 | Travel removed; fade at 100ms |
| Modal / drawer close | 100ms `{motion.duration-fast}` | `{motion.ease-exit}` | opacity, transform | Travel removed; fade at 100ms |
| Dropdown / nav menu | 100ms in, 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity, scaleY(0.98) to 1 | Scale removed; opacity at 100ms |
| Toast | 150ms in, 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity, translateY(8px) | Travel removed; opacity at 100ms |
| List enter | 150ms, 20ms `{motion.stagger-step}` per item | `{motion.ease-enter}` | opacity, translateY(6px) | Stagger and travel removed; fade together at 100ms |
| List exit | 100ms, no stagger | `{motion.ease-exit}` | opacity, translateY(4px) | Travel removed; opacity at 100ms |
| Loading (spinner, EAS build status) | 800ms linear loop | linear | rotate | Rotation frozen; static indicator plus text label |
| Hero device-mockup entrance | 300ms `{motion.duration-emphasis}` | `{motion.ease-enter}` | opacity, translateY(12px) | Travel removed; opacity at 100ms. Runs after first paint |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, the `check(...)` call block (lines 227-234) | SPEC section 2 requires `on-accent` on `accent` at 4.5:1, but no `check("on-accent", "accent", ...)` call exists. The pair is never measured for any of the 84 files. | Add `check("on-accent", "accent", 4.5, "text on accent")` beside the other `check` calls. Expo passes it at 21:1, so this costs nothing here but may be hiding failures elsewhere. |
| `theme-audit/audit.py`, same block (lines 224-234) | SPEC section 2 says "Every signal colour is checked, not just the representative accent", but `check_all` is only invoked for `text-dim` and `border`. Semantic and accent tones are never measured — Expo's `semantic-error` at 2.39:1 and `accent-link-bright` at 2.01:1 drew zero deductions. | Add `check_all("accent", "canvas", 4.5, ...)` and extend the role patterns to cover `^semantic-`, or add a `signal` pseudo-role for `semantic-*` / `accent-*` tones used as text. |
| `theme-audit/audit.py`, `find_role_strongest` (line 150) | Adding a parallel accessible token silently promotes it to the representative for its role, so the representative-pair check stops failing even though the weak extracted tone is still what the prose uses everywhere. Only `check_all` keeps the file honest. | Keep the representative at `find_role` (first-match) order and use `find_role_strongest` for reporting only, or report both. |
| `theme-audit/SPEC.md`, section headings 4 and 5 | The per-profile literal YAML blocks sit under "## 4. Motion tokens", while the brief and SPEC prose point at "section 5" for profile values; section 5 is the profile table. Off-by-one between the brief's wording and the spec's numbering. | Move the per-profile blocks under section 5, or renumber so the token blocks and the profile table share one section. |

### Needs approval

Nothing below changes an extracted hex; these are the recorded failures of the
real brand, each with the nearest passing value and the usage note that would
make the real value defensible.

1. **`muted` #999999 — 2.85:1 on white, needs 4.5:1.** Nearest passing value #6b6f76 (5.05:1), added alongside as `muted-strong`. Defensible as-is only at 24px+ (or 18.66px bold), where the threshold drops to 3:1 and #999999 clears it. The file uses it for "Sub-titles", which are not reliably that large. Decision needed: scope `muted` to 24px+ upstream, or replace it with `muted-strong` at small sizes.
2. **`muted-soft` #cccccc — 1.61:1.** Documented as disabled text, for which WCAG sets no requirement, so defensible provided it never carries live copy. Decision needed: rename it `text-disabled` upstream so its one legal use is enforced by its name (and it becomes name-exempt in the harness). I did not rename it — renaming an extracted token breaks the prose contract.
3. **Hairline ladder #f5f5f7 / #f0f0f3 / #dcdee0 — 1.09 / 1.14 / 1.35:1, needs 3:1.** Nearest passing value #86888f (3.54:1), added as `border-control`. The real hairlines are defensible only as decoration between content rows. Decision needed: Expo's real `text-input`, `feature-card` and `pricing-tier-card` outlines use #dcdee0 and are therefore invisible to low-vision users. Changing them is a brand decision.
4. **`semantic-error` #eb8e90 — 2.39:1, needs 4.5:1.** Nearest passing value #b3261e (6.54:1), added as `semantic-error-text`. There is no text size at which #eb8e90 is defensible; only as a border or background tint. Decision needed: this is a live accessibility defect in Expo's own validation messaging.
5. **`text-link-secondary` #476cff — 4.32:1, needs 4.5:1.** Nearest passing value #3f61e8 (4.78:1). Defensible at 24px+ under the 3:1 rule, but it is used for legal-footer links, which are small. 0.18 short.
6. **`semantic-success` #16a34a — 3.30:1, needs 4.5:1.** Nearest passing value #157f3c (4.52:1). Defensible for icons and 24px+ text as-is.
7. **`accent-link-bright` #47c2ff — 2.01:1 on white.** Defensible only on `surface-dark`, where it reaches 8.90:1. Decision needed: confirm it never appears on a light docs surface.
8. **Focus ring on the hero gradient.** `focus` #0d74ce reaches only 2.74:1 against `gradient-sky-mid` #a8c8e8. I specified a mandatory 2px canvas offset, giving a 3.75:1 outer edge. That requirement is prescribed, not extracted, and it makes the offset non-optional wherever the ring can land on the hero wash.
9. **Tap targets.** `button-primary` and `button-secondary` are declared at 40px, below WCAG 2.5.5's 44px. Recorded, not changed — and declared, not measured, since nothing was rendered.

### Identity verdict

Still unmistakably Expo. The additions are deliberately parasitic on what the
brand already owns: the light focus ring is the file's own text-link blue
#0d74ce, the dark ring is its own docs cyan #47c2ff, and no new chromatic family
was introduced — which matters for a brand whose first rule is that black is the
only CTA fill. The prescribed greys (`muted-strong`, `border-control`) sit on the
same cool-neutral axis as the extracted `body` #60646c rather than arriving from
a generic ramp.

The Crisp profile is right, and not marginally. SPEC section 5 rule 2
(developer-tool identity) fires on a monochrome CTA, JetBrains Mono on every
code surface, a `code-block` and an `ide-mockup-card` component, and a hero that
shows EAS dashboards instead of choreography. The temptation was Cinematic —
there is a large device composite and a gradient sky wash — but rule 1 wants a
luxury or hardware identity with sparse type and a slow reveal, and Expo's hero
is dense product UI with a 64px headline and an immediate CTA. The one place I
let the profile breathe is the mockup entrance at `duration-emphasis` (300ms),
which is still the Crisp token, not a deviation.

The drift risk is the states table: 22 rows of prescribed hover-and-press
behaviour is the most generic material in the file. I kept it honest by marking
every static component "default only" — eleven of twenty-two — rather than
inventing a six-state ladder for a testimonial card, and by routing every state
through this file's own tokens.
