## A12 · clay

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 1 | 3 | 1 | 1 |
| After | 5 | 5 | 1 | 5 | 5 | 5 |

Contrast stays at 1 because the harness clamps at `max(1, 5 - failures)`: failures dropped 7 → 6, but six are the unfixable `on-primary` × `brand-*` pairings and cannot be cleared without falsifying brand hexes. The one fixable failure (`hairline` on `canvas`, 1.21:1) is resolved by a parallel accessible token.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, G | `colors.focus` | No focus token and no focus ring anywhere in the file. Nothing documented what a keyboard user sees. Fixed: composite `{colors.focus}` + `{colors.focus-inset}`, measured against all 14 surfaces the file defines. |
| P0 | B, E | `colors.hairline` | 1.21:1 on `{colors.canvas}`, yet the prose used it as the boundary of `{component.text-input}` and `{component.button-secondary}` — an interactive control with an effectively invisible edge. Fixed with a prescribed parallel token; the extracted value stays frozen and is scoped to decoration. |
| P0 | B, H | `feature-card-pink` | Prose instructed white text on `{colors.brand-pink}` for all copy. White on #ff4d8b is 3.14:1 — fails AA for body text. Fixed: white restricted to `{typography.title-lg}`+, `{colors.ink}` (6.30:1) for body and captions. |
| P0 | F | whole file | No `motion:` group, no Motion & Animation section, no reduced-motion rule. Iteration Guide item 5 actively said "Never document hover", and Don'ts forbade hover styling — the file was structurally hostile to interaction documentation. Fixed, and both contradictions rewritten. |
| P0 | G | whole file | No Accessibility section. Added, with measured ratios, per-surface focus visibility, tap-target arithmetic and reduced-motion. |
| P0 | H | Components | Only `active` was documented, and only incidentally via the `-active` frontmatter variants. Seven states never named. Fixed with a Component States table; four components are declared genuinely single-state. |
| P1 | B | `colors.muted-soft` | #9a9a9a at 2.70:1 on canvas is documented for "captions, fine-print" — it fails AA at every size. The harness never flags it because `text-dim` resolves to `muted` (first-pattern-wins). Stated plainly in the file and scoped to decorative fine print. |
| P1 | B | `colors.muted` | 4.33:1 on `{colors.surface-strong}` — passes on canvas (5.20:1) but fails on the strongest cream band. The harness checks `text-dim` against `surface`, which resolves to `surface-soft` (4.97:1), so the failure was invisible. Noted with a fallback to `{colors.body}`. |
| P1 | B | `success`, `warning`, `error` | 2.19:1, 2.06:1, 3.62:1 on canvas. All three were documented as text colours ("validation errors", "warning callouts"). Scoped to fills, icons and boundaries. |
| P1 | C | cream stack | `canvas` → `surface-soft` is 1.046:1, `surface-soft` → `surface-card` 1.047:1, `canvas` → `surface-strong` only 1.20:1. The four-layer cream stack is not distinguishable by luminance. Not a defect to fix (it is the warm palette's defining property) but it was undocumented; now stated, with radius + boundary as the separating mechanism. |
| P1 | C | Elevation table | Mixed border and shadow as if they were the same axis, and the "subtle drop shadow" row carried no value to reference. Fixed: elevation is fill, boundary is boundary, one prescribed `shadow:` group for the single hover lift. |
| P1 | G | `category-tab` | 8px vertical padding on 14px/1.4 type computes to ~36px tall, under the 44px the file claims for its other controls. Flagged as arithmetic, not a rendered measurement. |
| P2 | E | `rounded` | `pill` and `full` are both 9999px with no stated difference. Documented as intent-distinguished (capsule vs circle), ladder confirmed on-scale at 6/8/12/16/24. |
| P2 | A | `text-input-error` | Prose referenced only `{component.text-input-focused}`; no error entry existed at all. Added as prescribed, with a frontmatter key so the reference resolves. |
| P2 | D | typography | Every one of the 13 roles already carried size, weight, line height and letter-spacing — no gap. Body-on-surface readability verified: `{typography.body-md}` in `{colors.body}` is 9.98:1 on `{colors.surface-card}`. No change needed. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Frontmatter `colors:` | added `hairline-strong: "#7a736a"` | Parallel accessible boundary token; 4.50:1 on canvas vs the frozen hairline's 1.21:1 |
| Frontmatter `colors:` | added `focus: "#c2185b"`, `focus-inset: "#fffaf0"` | Required `focus` role was missing; hue derived from `{colors.brand-pink}` so the ring reads as Clay |
| Frontmatter | added `motion:` group (11 keys, Playful profile) | SPEC §4; base 200ms, overshoot enter, 60ms stagger, plus `press-scale` and `hover-lift` for the signature squash |
| Frontmatter | added `shadow:` group (`hover-lift`, `focus-glow`) | Elevation prose said "faint shadow at low alpha" with no token to reference |
| Frontmatter `components:` | added `text-input-error` | The file documented focus but no error state for inputs |
| Colors § Surface | hairline line expanded; added hairline-soft and hairline-strong entries | States the 1.21:1 failure plainly and scopes the frozen token to decoration |
| Colors § new Focus subsection | added | Per-surface measured ratios for both ring bands, labelled prescribed |
| Colors § Text | `muted-soft` line gained its 2.70:1 measurement and a scope | Real AA failure that the harness cannot see |
| Colors § Text | `on-primary` line gained the pink-card failure and the ink alternative | 3.14:1 is the real brand; large-text-only is the defensible usage note |
| Elevation & Depth | table rows re-cut (decorative rule vs control boundary vs hover lift); layer ratios added | Dimension C: one consistent elevation axis, and the cream layers measured |
| Shapes | added radius-ladder note and a Border & Ring Widths table | Dimension E: the width ladder was undocumented |
| Components § Buttons | `button-secondary` boundary → `{colors.hairline-strong}` | Interactive boundary needs 3:1 |
| Components § Cards | `feature-card-*` text rule rewritten with measured ratios | Removed the instruction to set white body copy at 3.14:1 |
| Components § Cards | `pricing-tier-card` boundary → `{colors.hairline-strong}` | Selectable card, visible edge required |
| Components § Inputs | `text-input` boundary → `{colors.hairline-strong}`; focused state spelled out; `text-input-error` added | Control boundary + the missing error state |
| Components | new `### Component States` table (12 rows) | Dimension H; all 8 state words now documented in structured lines |
| after Components | new `## Motion & Animation` | SPEC §3/§5/§6. First line declares the whole section prescribed |
| after Motion | new `## Accessibility` | SPEC §3 |
| Don'ts | hover line rewritten; 5 new don'ts | The old "don't add hover state styling" contradicted the new states model |
| Iteration Guide item 5 | "Never document hover" -> point at the Component States table | Directly contradicted SPEC §7 |
| Known Gaps | animation line replaced with 6 explicit prescribed-value entries | SPEC's honesty requirement: every inferred value is labelled |

### Contrast checks

All computed with `theme-audit/audit.py`'s WCAG 2.1 relative-luminance functions; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #0a0a0a / `canvas` #fffaf0 | 19.03:1 | 4.5:1 | Pass |
| `ink` / `surface-soft` #faf5e8 | 18.19:1 | 4.5:1 | Pass |
| `ink` / `surface-card` #f5f0e0 | 17.37:1 | 4.5:1 | Pass |
| `ink` / `surface-strong` #ebe6d6 | 15.86:1 | 4.5:1 | Pass |
| `body` #3a3a3a / `canvas` | 10.93:1 | 4.5:1 | Pass |
| `body` / `surface-card` | 9.98:1 | 4.5:1 | Pass |
| `muted` #6a6a6a / `canvas` | 5.20:1 | 4.5:1 | Pass |
| `muted` / `surface-soft` | 4.97:1 | 4.5:1 | Pass |
| `muted` / `surface-card` | 4.75:1 | 4.5:1 | Pass |
| `muted` / `surface-strong` | 4.33:1 | 4.5:1 | **Fail** |
| `muted-soft` #9a9a9a / `canvas` | 2.70:1 | 4.5:1 | **Fail** |
| `on-primary` #ffffff / `primary` #0a0a0a | 21.00:1 | 4.5:1 | Pass |
| `on-dark` / `brand-teal` #1a3a3a | 12.28:1 | 4.5:1 | Pass |
| `on-dark` / `surface-dark` #0a1a1a | 17.86:1 | 4.5:1 | Pass |
| `on-dark-soft` #a0a0a0 / `surface-dark` | 6.83:1 | 4.5:1 | Pass |
| `on-dark-soft` / `surface-dark-elevated` #1a2a2a | 5.70:1 | 4.5:1 | Pass |
| `on-primary` / `brand-pink` #ff4d8b | 3.14:1 | 4.5:1 | **Fail** (passes 3:1 large text) |
| `on-primary` / `brand-lavender` #b8a4ed | 2.19:1 | 4.5:1 | **Fail** (combination not used) |
| `on-primary` / `brand-peach` #ffb084 | 1.78:1 | 4.5:1 | **Fail** (combination not used) |
| `on-primary` / `brand-ochre` #e8b94a | 1.83:1 | 4.5:1 | **Fail** (combination not used) |
| `on-primary` / `brand-mint` #a4d4c5 | 1.64:1 | 4.5:1 | **Fail** (combination not used) |
| `on-primary` / `brand-coral` #ff6b5a | 2.80:1 | 4.5:1 | **Fail** (combination not used) |
| `ink` / `brand-pink` | 6.30:1 | 4.5:1 | Pass |
| `ink` / `brand-lavender` | 9.02:1 | 4.5:1 | Pass |
| `ink` / `brand-peach` | 11.12:1 | 4.5:1 | Pass |
| `ink` / `brand-ochre` | 10.81:1 | 4.5:1 | Pass |
| `ink` / `brand-mint` | 12.07:1 | 4.5:1 | Pass |
| `ink` / `brand-coral` | 7.07:1 | 4.5:1 | Pass |
| `error` #ef4444 / `canvas` (as text) | 3.62:1 | 4.5:1 | **Fail** |
| `error` / `canvas` (as UI boundary) | 3.62:1 | 3.0:1 | Pass |
| `success` #22c55e / `canvas` (as text) | 2.19:1 | 4.5:1 | **Fail** |
| `warning` #f59e0b / `canvas` (as text) | 2.06:1 | 4.5:1 | **Fail** |
| `hairline` #e5e5e5 / `canvas` | 1.21:1 | 3.0:1 | **Fail** (frozen, scoped to decoration) |
| `hairline-strong` #7a736a / `canvas` | 4.50:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface-soft` | 4.30:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface-card` | 4.10:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface-strong` | 3.75:1 | 3.0:1 | Pass |
| `focus` #c2185b / `canvas` | 5.65:1 | 3.0:1 | Pass |
| `focus` / `surface-soft` | 5.40:1 | 3.0:1 | Pass |
| `focus` / `surface-card` | 5.15:1 | 3.0:1 | Pass |
| `focus` / `surface-strong` | 4.70:1 | 3.0:1 | Pass |
| `focus` / `primary` (near-black CTA) | 3.37:1 | 3.0:1 | Pass |
| `focus` / `surface-dark` | 3.04:1 | 3.0:1 | Pass |
| `focus` / `brand-peach` | 3.30:1 | 3.0:1 | Pass |
| `focus` / `brand-ochre` | 3.21:1 | 3.0:1 | Pass |
| `focus` / `brand-mint` | 3.58:1 | 3.0:1 | Pass |
| `focus` / `brand-pink` | 1.87:1 | 3.0:1 | Fail — inner band carries it (3.02:1) |
| `focus` / `brand-teal` | 2.09:1 | 3.0:1 | Fail — inner band carries it (11.80:1) |
| `focus` / `brand-lavender` | 2.68:1 | 3.0:1 | **Fail — see Needs approval** |
| `focus` / `brand-coral` | 2.10:1 | 3.0:1 | **Fail — see Needs approval** |
| `focus-inset` #fffaf0 / `brand-lavender` | 2.11:1 | 3.0:1 | **Fail — see Needs approval** |
| `focus-inset` / `brand-coral` | 2.69:1 | 3.0:1 | **Fail — see Needs approval** |
| `focus-inset` / `focus` (band-to-band) | 5.65:1 | 3.0:1 | Pass |
| `focus-inset` / `primary` | 19.03:1 | 3.0:1 | Pass |
| `focus-inset` / `brand-teal` | 11.80:1 | 3.0:1 | Pass |
| `focus-inset` / `surface-dark` | 17.17:1 | 3.0:1 | Pass |
| `focus-inset` / `surface-dark-elevated` | 14.33:1 | 3.0:1 | Pass |
| `muted` / `primary-disabled` #e5e5e5 (disabled label) | 4.29:1 | exempt | Exempt (WCAG sets no threshold on disabled) |
| `canvas` / `surface-soft` (layer step) | 1.046:1 | n/a | Layers not separable by luminance |
| `surface-soft` / `surface-card` | 1.047:1 | n/a | Layers not separable by luminance |
| `surface-card` / `surface-strong` | 1.095:1 | n/a | Layers not separable by luminance |
| `canvas` / `surface-strong` | 1.200:1 | n/a | Layers not separable by luminance |

### Motion inventory

Profile: **Playful** (SPEC §5 rule 3). Base 200ms, overshoot on enter, 60ms stagger. Entire table prescribed; nothing measured from Clay.com.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 120ms | `{motion.ease-standard}` | `transform: translateY(-2px)`, `opacity` | Travel removed; fill and underline change applies instantly |
| Press | 70ms down / 120ms release | `{motion.ease-standard}` / `{motion.ease-enter}` | `transform: scale(0.97)` | Scale removed; pressed fill still applies, no transition |
| Focus | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` only | Ring appears instantly at full opacity; never suppressed |
| Page / route transition | 200ms out / 320ms in | `{motion.ease-exit}` / `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Opacity crossfade at 120ms, no translate |
| Modal / drawer | 320ms in / 200ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: scale(0.96→1)` or `translateX(100%→0)` | Opacity at 120ms, no scale, no slide; backdrop fades, never blurs |
| Dropdown | 120ms in / 70ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: scale(0.98→1)` | Opacity only at 120ms, no scale |
| Toast | 200ms in / 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(12px→0)` | Opacity at 120ms, no travel; auto-dismiss unchanged |
| List enter | 200ms per item, `{motion.stagger-step}` 60ms apart, capped at 6 | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px) scale(0.98)` | Stagger and travel removed; group fades at 120ms as one |
| List exit | 120ms, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Opacity at 120ms, no scale |
| Loading | 900ms spinner rotation, 1600ms skeleton pulse (infinite) | linear / `{motion.ease-standard}` | `transform: rotate()`, `opacity` | Rotation stops, becomes static indicator with text; pulse freezes mid-opacity; busy state still announced |

Every exit is shorter than its matching entrance. Only `transform` and `opacity` animate. Nothing animates on first paint. The one piece of ambience (claymation illustration drift) is declared as brand ambience and freezes under reduce.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 169–178 | The signal-colour loop pairs the single `on-accent` token against every token matching `^(primary\|accent\|secondary\|brand\|cta)`, regardless of whether the file documents that pairing. For clay this produces 6 failures of which 5 are combinations the file explicitly routes to `{colors.ink}` instead. The score then clamps to 1 and cannot move however the file is corrected. | Let a file declare its ink per signal colour — e.g. honour a `components:` entry's `textColor` when the signal token is used as a `backgroundColor` there — and fall back to the blanket `on-accent` pairing only when no component binds that colour. Failing that, split the score so a documented-and-measured failure costs less than an undocumented one. |
| `theme-audit/audit.py` lines 19–35, 125 | `find_role` is first-pattern-wins for `text-dim`, so `muted` (5.20:1) represents the role and `muted-soft` (2.70:1) is never checked — the opposite of the `find_role_strongest` treatment given to `border` and `focus`. Real failures hide behind a passing sibling. | Check every token matching a role's patterns, not only the representative one; keep the representative for reporting. |
| `theme-audit/audit.py` lines 160–161, 22 | `text-dim` on `surface` is checked only against the first matching surface (`surface-soft`, 4.97:1). `muted` on `surface-strong` is 4.33:1 and goes unreported. | Check text roles against every `surface*` token, or against the darkest one. |
| `theme-audit/audit.py` line 164 | `focus` is checked against `canvas`, `surface` and `accent`, which forces one token to clear 3:1 on both a cream canvas and a near-black CTA. SPEC §1 anticipates two rings (`focus` / `focus-on-dark`) but the strongest-vs-canvas selection then feeds the dark ring into the accent check, where it must fail. The two models are inconsistent. | When a file defines more than one `focus*` token, check the set collectively: each surface must be cleared by at least one ring, rather than by the single representative. |
| `theme-audit/SPEC.md` §1 | Names `focus-on-dark` as the second ring, but the harness's role patterns (`^focus-`) plus strongest-vs-canvas selection make that naming actively counterproductive — a dark-surface ring is light, so it is never selected, while a light-surface ring that happens to be darker gets checked against the accent. | State the composite/dual-ring contract explicitly, and say which token the harness will treat as representative. |

### Needs approval

Six contrast failures remain. None can be fixed without falsifying an extracted brand hex, so all are recorded here rather than applied.

1. **`on-primary` #ffffff on `brand-pink` #ff4d8b — 3.14:1, needs 4.5:1.** This is a real combination on the live site: white copy on the hot-pink feature card. Nearest passing value: **#d13f72** (4.50:1), an 18% luminance reduction that visibly dulls the brand's most recognisable card. Usage note that makes the real value defensible: *white on `{colors.brand-pink}` is permitted only at `{typography.title-lg}` (24px / 400) and above, where WCAG's 3:1 large-text threshold applies; body copy and captions on that card use `{colors.ink}` at 6.30:1.* The file now says this, and says plainly that the brand fails AA at that point. **Approval needed only if you want the hex changed.**

2–6. **`on-primary` on `brand-lavender` (2.19:1), `brand-peach` (1.78:1), `brand-ochre` (1.83:1), `brand-mint` (1.64:1), `brand-coral` (2.80:1).** These are harness pairings, not documented combinations — the file routes all five to `{colors.ink}` (9.02:1, 11.12:1, 10.81:1, 12.07:1, 7.07:1 respectively). Nearest passing values if you ever did need white on them: #7c6fa0, #9c6b51, #8f722e, #607c73, #c45245 — every one is a muddied, desaturated version of the brand colour and would destroy the claymation palette. Recommendation: **do not change these hexes.** The defect is in the check (see Shared issues), not in the brand.

7. **Focus ring on `brand-lavender` and `brand-coral`.** Neither band of the composite ring reaches 3:1 against those two fills (outer 2.68:1 / 2.10:1, inner 2.11:1 / 2.69:1), and no single luminance can clear 3:1 against both `{colors.primary}` (#0a0a0a) and `{colors.brand-lavender}` — the windows do not overlap. Nearest passing values: lighten lavender to **#c3aefb** (outer band reaches 3.01:1) or darken it to **#9988c5** (inner band 3.02:1); darken coral to **#f06555** (inner band 3.01:1, and visually near-identical to #ff6b5a). The file's current answer is a system rule instead of a hex change — `{component.button-on-color}` is a cream button, so its ring is drawn against the canvas, and the file forbids bare focusable elements on those two fills. **Approval needed if you prefer the #f06555 coral correction, which is cheap.**

8. **Prescribed values introduced, listed for the record:** `{colors.focus}` #c2185b, `{colors.focus-inset}` #fffaf0, `{colors.hairline-strong}` #7a736a, the whole `motion:` group, the `shadow:` group, and `{component.text-input-error}`. All are labelled prescribed in the file and in Known Gaps.

### Identity verdict

Still unmistakably Clay. The cream canvas, the six-colour saturated card cycle, Plain Black at 500 with negative letter-spacing, the cream-not-dark footer and the claymation illustrations are all untouched, and the additions lean on them rather than around them: the focus ring is a deepened `{colors.brand-pink}` rather than a system blue, the signature motion gesture is a 0.97 press-squash chosen because clay deforms and springs back, and `{colors.hairline-strong}` is a warm grey tuned to the cream palette rather than a neutral slate. Nothing reads as borrowed from another file in the collection.

The assigned **Playful** profile is correct, and worth defending because SPEC §5 rule 3 explicitly warns against judging on hex count. Clay passes the stricter test: the saturated colour is on interactive elements, not behind screenshots — `{component.feature-card-pink}` through `{component.feature-card-ochre}` are clickable surfaces, `{component.pricing-tier-card-featured}` signals selection with a `{colors.brand-teal}` fill, and `{component.category-tab-active}` changes fill on selection. The type voice is informal (rounded display face, weight capped at 500 because 700 "reads as bombastic"), gradients are not forbidden, and the file's own first line calls Clay "the most playful B2B SaaS interface in the GTM-data category". No argument for a different profile.

One genuine tension: the file's original Don'ts and Iteration Guide forbade documenting hover at all, which is a real editorial position (restraint) and not an oversight. Overriding it was necessary to meet SPEC §7, and both lines were rewritten rather than deleted so the restraint survives as a bound on *how much* hover does, not a ban on naming it.
