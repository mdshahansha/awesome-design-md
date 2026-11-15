## A54 · posthog

Scores before -> after (1-5), from the harness: tokens 5 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

Contrast moved on disclosure, not on any changed hex: ten role failures and one component failure were undisclosed before; seven remain as failures and all seven are now named with their measured ratios in `## Accessibility`, and the four focus-coverage failures were resolved by binding a real ring.

Note on the brief's pre-measurement: it lists `focus` and `text-dim` as missing colour roles. The harness does not — `focus-ring` already satisfied `focus` by pattern and `mute` satisfied `text-dim`. The real defect was behind that: the only ring the file owned was the composited browser default, which covers no surface in the system. Logged under Shared issues as a stale brief, not as a harness bug.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | frontmatter + document body | No `motion:` group and no `## Motion & Animation` section. `duration-base`, `duration-fast` and `ease-standard` all absent; zero durations and zero easing curves anywhere in the file. |
| P0 | G · Accessibility | document body | No `## Accessibility` section, so seven real contrast failures — four boundary, two secondary-ink, one component — sat undisclosed in a document whose job is to state them. |
| P0 | A · Token contract | `focus-ring` | The only focus token was `rgba(59,130,246,0.5)`, the browser default. Composited it is `#94b8f0`: 1.75:1 on `{colors.canvas}`, **1.62:1 on `{colors.surface-soft}`**, 2.02:1 on `{colors.surface-card}`, 1.97:1 on `{colors.surface-doc}`. No surface in the system had a covering ring, against a 3:1 WCAG 2.2 Focus Appearance minimum. |
| P1 | H · States | all component entries | Five of eight states never named: hover, focus-visible, loading, selected, error. The file declared "No hover states documented per system policy", which conflates a gap in the captured set with a brand rule. |
| P1 | B · Colour | `link-inline` | `{colors.link-teal}` `#1078a3` on `{colors.canvas}` is 4.29:1 against 4.5:1 — the extracted doc-article link colour fails AA at the 15–16px it carries. |
| P1 | B · Colour | `mute` | 4.49:1 on `{colors.canvas}` (short by 0.01) and 4.16:1 on `{colors.surface-soft}`. The brand's metadata and footer ink misses AA. |
| P1 | E · Borders | `hairline`, `hairline-soft` | 1.58:1 and 1.17:1 on canvas, 1.46:1 and 1.08:1 on `surface-soft`. Frozen extracted values, but `{component.text-input}` and `{component.search-input}` have the 1px hairline as their *only* affordance, so a decorative tone was doing a control's work. |
| P2 | C · Elevation | canvas / surface-soft / surface-card / surface-doc | The four light grounds are 1.03:1–1.16:1 apart, so the layer system is carried almost entirely by a 1px rule that is itself at 1.58:1. Extracted and unchanged; recorded in Accessibility and here. |
| P2 | E · Spacing ladder | `feature-tile` | Prose read "padding `{spacing.lg}` (20px)" while `{spacing.lg}` is 16px and the component block declares 20px. 20px recurs (banners, code block) with no token. |
| P2 | E · Radius ladder | `{rounded.lg}` | The radius table attributed the active tab's `6px 6px 0 0` to the 8px step; 6px is `{rounded.md}`. |
| P2 | D · Typography | — | No defect: all 20 roles carry family, size, weight, line height and letter spacing, and body ink clears 6.68:1 on the weakest surface. |
| P2 | I · Identity | — | No defect; see Identity verdict. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#2c84e0"` | SPEC §1's focus exception: a real role binding on a hex the palette already owns (`accent-blue`, which the captured pages draw as the focused-input boundary). One mid-luminance ring clears 3:1 on all five surfaces the system defines, so no light/dark pair is needed. `focus-ring` is left in place, unaltered. |
| frontmatter, between `spacing:` and `components:` | — -> `motion:` group | The **Crisp** block from SPEC §5, verbatim, no deviation. |
| after `## Components`, before `## Do's and Don'ts` | — -> `## Motion & Animation` | First line states the system is prescribed and was not measured from the live site. Ten-row interaction table, transform/opacity only, exits shorter than entrances, plus the `prefers-reduced-motion` block. |
| after that | — -> `## Accessibility` | Measured pairs with ratios, the seven real failures stated plainly, per-surface focus-ring ratios with the 2px offset, tap-target metrics, reduced motion, and what a document cannot measure. |
| end of `## Components` | — -> `### States` matrix | Ten rows covering all eight states, each entry marked extracted or prescribed; the three one- or two-state components say so explicitly. |
| `## Components` lead blockquote | "No hover states documented per system policy." -> "Hover and focus treatments were not captured." | The gap is in the captured set, not in the brand's policy; the claim as written was an invented fact. |
| `## Colors` → Surface | `hairline` / `hairline-soft` bullets -> same, plus "**Decorative only**" with the measured ratio and a pointer to the accessible boundary | Scopes the frozen tones to decoration without touching their hexes or their `components:` bindings. |
| `## Colors` → Semantic | Focus Ring bullet -> `focus` bullet + an honest Focus Ring bullet | States which existing tone the ring reuses (SPEC §1) and records the browser default's real ratios. |
| `## Shapes` radius table | `{rounded.lg}` row attributed `6px 6px 0 0` to the 8px step -> row corrected to name `{rounded.md}` | Ladder consistency; no value invented or changed. |
| `## Components` → `feature-tile` | "padding `{spacing.lg}` (20px)" -> "padding `20px` — … the one padding in the system with no token" | The prose contradicted both the token and the component block. |
| `## Known Gaps` | "Hover states not documented by system policy" -> three entries | States gap, motion-is-prescribed, and the keyboard/screen-reader/tap-target limits of a document audit. |

No hex was altered, no `components:` binding was re-pointed, and no alias token was added.

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`; `focus-ring` composited over each ground before measurement.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#23251d` / `canvas` `#eeefe9` | 13.41:1 | 4.5:1 | Pass |
| `ink` / `surface-card` `#ffffff` | 15.51:1 | 4.5:1 | Pass |
| `ink` / `surface-soft` `#e5e7e0` | 12.44:1 | 4.5:1 | Pass |
| `ink` / `surface-doc` `#fcfcfa` | 15.10:1 | 4.5:1 | Pass |
| `body` `#4d4f46` / `canvas` | 7.20:1 | 4.5:1 | Pass |
| `charcoal` `#33342d` / `canvas` | 10.87:1 | 4.5:1 | Pass |
| `on-primary` `#23251d` / `primary` `#f7a501` | 7.64:1 | 4.5:1 | Pass |
| `on-primary` / `primary-pressed` `#dd9001` | 5.96:1 | 4.5:1 | Pass |
| `on-dark` `#ffffff` / `surface-dark` `#23251d` | 15.51:1 | 4.5:1 | Pass |
| `link-blue` `#1d4ed8` / `canvas` | 5.79:1 | 4.5:1 | Pass |
| `link-blue` / `accent-blue-soft` `#dceaf6` (badge-promo) | 5.47:1 | 4.5:1 | Pass |
| `ink` / `accent-blue-soft` | 12.66:1 | 4.5:1 | Pass |
| `ink` / `accent-green-soft` `#d9eddf` | 12.65:1 | 4.5:1 | Pass |
| `ink` / `accent-red-soft` `#f7d6d3` | 11.46:1 | 4.5:1 | Pass |
| `ink` / `accent-purple-soft` `#e7d8ee` | 11.42:1 | 4.5:1 | Pass |
| `mute` `#6c6e63` / `canvas` | 4.49:1 | 4.5:1 | **Fail** (disclosed) |
| `mute` / `surface-soft` | 4.16:1 | 4.5:1 | **Fail** (disclosed) |
| `link-teal` `#1078a3` / `canvas` (`link-inline`) | 4.29:1 | 4.5:1 | **Fail** (disclosed) |
| `hairline` `#bfc1b7` / `canvas` | 1.58:1 | 3.0:1 | **Fail** (disclosed, scoped to decoration) |
| `hairline` / `surface-soft` | 1.46:1 | 3.0:1 | **Fail** (disclosed) |
| `hairline-soft` `#dcdfd2` / `canvas` | 1.17:1 | 3.0:1 | **Fail** (disclosed) |
| `hairline-soft` / `surface-soft` | 1.08:1 | 3.0:1 | **Fail** (disclosed) |
| `focus-ring` composited `#94b8f0` / `canvas` | 1.75:1 | 3.0:1 | **Fail** — extracted browser default, recorded |
| `focus-ring` composited / `surface-soft` | 1.62:1 | 3.0:1 | **Fail** — the surface the harness flagged |
| `focus-ring` composited / `surface-card` | 2.02:1 | 3.0:1 | **Fail** — extracted, recorded |
| `focus-ring` composited / `surface-doc` | 1.97:1 | 3.0:1 | **Fail** — extracted, recorded |
| `focus` `#2c84e0` / `canvas` | 3.31:1 | 3.0:1 | Pass |
| `focus` / `surface-soft` | 3.07:1 | 3.0:1 | Pass |
| `focus` / `surface-card` | 3.83:1 | 3.0:1 | Pass |
| `focus` / `surface-doc` | 3.73:1 | 3.0:1 | Pass |
| `focus` / `surface-dark` | 4.05:1 | 3.0:1 | Pass |
| `focus` / `primary` fill `#f7a501` | 1.89:1 | n/a | Not required — ring is drawn outside the control at 2px offset and judged against the surface behind it |
| `mute` as control boundary / `canvas` · `surface-soft` · `surface-card` · `surface-doc` | 4.49 · 4.16 · 5.19 · 5.05 | 3.0:1 | Pass — existing tone, no new token |
| `ash` `#9b9c92` / `canvas` | 2.40:1 | exempt | Disabled-state ink |
| `stone` `#b6b7af` / `canvas` | 1.75:1 | exempt | Lowest-emphasis caption / disabled icon; noted as unusable for information-bearing copy |
| layer separation: `canvas`/`surface-soft` · `canvas`/`surface-card` · `surface-card`/`surface-doc` | 1.08 · 1.16 · 1.03 | n/a | Layers are near-indistinguishable; the system leans on its 1px rule |

**Why `surface-soft` had no ring, and how it was resolved.** `surface-soft` `#e5e7e0` is the lightest-but-one ground in a system whose four light surfaces span 1.03:1, and the file's only ring was a 50%-alpha blue that composites to `#94b8f0` — luminance 0.469, almost identical to the surface itself. Nothing could be disclosed into a pass there without leaving the file with no usable focus indicator at all, and SPEC §1's focus exception exists for precisely this: a ring must be addressable as `focus*`. Covering all five surfaces requires a ring luminance between 0.144 and 0.300 (3:1 against `#ffffff` caps it; 3:1 against `#23251d` floors it), so a light/dark ring pair is both unnecessary and worse than one mid-luminance tone. `accent-blue` `#2c84e0` (luminance 0.224) is inside that window, is already in the palette, and is already drawn as the focused-input boundary in the captured pages — so `focus` binds to that hex rather than to anything invented. The browser default's four failing ratios are stated in `## Accessibility` regardless; the new ring does not retract them.

### Motion inventory

Prescribed, Crisp profile. Not measured from the live site.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity`; colour/background as a discrete token swap | Swap applies instantly, no transition |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `transform: scale(0.98)` | No scale; fill swaps instantly |
| Focus | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` of the 2px ring | Ring appears instantly at full opacity |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` on the article column only | Fade at `{motion.duration-reduced}` 100ms |
| Modal / drawer (mobile nav) | 150ms in / 100ms out | `ease-enter` / `ease-exit` | `transform: translateX` + scrim `opacity` | No travel; cross-fade at 100ms |
| Dropdown (sub-nav select, sidebar accordion) | `{motion.duration-fast}` 100ms | `ease-enter` / `ease-exit` | `opacity` + `translateY(-4px → 0)` | Opacity only, 100ms |
| Toast (copy-to-clipboard) | 100ms in / 60ms out | `ease-enter` / `ease-exit` | `opacity` + `translateY(6px → 0)` | Opacity only, 100ms; dwell unchanged |
| List enter | 150ms per item, `{motion.stagger-step}` 20ms apart, capped at 6 | `{motion.ease-enter}` | `opacity` + `translateY(4px → 0)` | No stagger, no travel; one fade at 100ms |
| List exit | 100ms, no stagger | `{motion.ease-exit}` | `opacity` | Opacity at 100ms |
| Loading | spinner 600ms/revolution; skeleton pulse `{motion.duration-slow}` 220ms | linear / `ease-standard` | spinner `transform: rotate()`; skeleton `opacity` | Spinner stops rotating, becomes a 1.5s opacity pulse; skeleton capped at 100ms |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/briefs/A54-posthog.md` | The pre-measurement block lists "Missing colour roles: focus, text-dim", which the harness does not report for this file — `focus-ring` satisfies `focus` by pattern and `mute` satisfies `text-dim`. The brief also omits the four focus-coverage failures, which were the actual P0. The briefs appear to predate the current `audit.py`. | Regenerate the briefs from the current harness output, or stamp each brief with the `audit.py` revision that produced it so a reviewer knows when the block is stale. |
| `theme-audit/audit.py` (states block, ~line 630) | A structured line is counted when a state word appears anywhere in it, so "this component has neither selected nor error state" scores both words. Honest documentation of a two-state component and a false claim of eight states are indistinguishable to the check. | Count a state only when the line asserts it — e.g. ignore a state word that falls after a negation (`no`, `neither`, `without`) within the same cell — and score a declared one- or two-state component as complete instead. |
| `theme-audit/audit.py` (ring coverage, ~line 484) | A surface is covered when *any* ring clears 3:1, so a file keeping a frozen failing ring alongside a passing one reports clean. Correct per SPEC, but it means the live site's real focus failure is invisible in the JSON once a ring is added; only the prose carries it. | Emit covered-by-a-prescribed-ring surfaces as an informational field (not a score deduction) so the frozen ring's ratios stay in the machine-readable output. |

### Needs approval

1. **Re-point the input boundary.** `{component.text-input}` and `{component.search-input}` are documented with a 1px `{colors.hairline}` boundary at 1.58:1 on cream — for a field whose boundary is its only affordance. The `components:` bindings are left exactly as extracted, and the Accessibility section prescribes `{colors.mute}` `#6c6e63` (4.49:1 / 4.16:1 / 5.19:1 / 5.05:1 across the four light grounds) for implementers. Changing the token block itself is a brand-owner decision: it would make the document describe a boundary the live site does not draw.
2. **`link-inline` at 4.29:1.** Nearest passing value `#10749e` (4.52:1 on canvas). Defensible as extracted only for 18.66px/700 or 24px+ text, which is not where it is used; the alternative is to route body-prose anchors to `{colors.link-blue}` `#1d4ed8`, already passing at 5.79:1. Not changed — `#1078a3` is an extracted brand hex.
3. **`mute` at 4.49:1 / 4.16:1.** Nearest passing value `#67685e` (4.88:1 on canvas, 4.53:1 on `surface-soft`). Defensible as extracted at 18.66px/700+ where 3:1 applies; it is currently used at 13–14px for metadata and footer links. Not changed.
4. **`stone` `#b6b7af` at 1.75:1 on canvas.** Documented as "least-emphasis caption text". At that ratio it cannot carry text of any size. Either confirm it is icon-and-decoration only, or accept a darker caption tone. Not changed.
5. **The prescribed ring colour.** `focus: #2c84e0` reuses `accent-blue`. If PostHog would rather its ring were the brand yellow, no yellow in the palette clears 3:1 on white (`primary` is 2.03:1), so that would require a new hex — which this audit will not invent.
6. **The whole Motion & Animation section and the prescribed half of the States matrix** are the audit's prescriptions, not observations, and are open to being overruled wholesale.

### Identity verdict

Still unmistakably PostHog. Every value added is either a literal from SPEC's Crisp block or a hex the palette already owned; nothing chromatic was introduced. The motion section argues from the brand's own evidence — flat bordered cards, static SVG hedgehogs, a docs-led chrome with no parallax and no hero reveal — to a system in which motion barely does anything, which is the honest reading of a developer-tools identity on a cream canvas.

Crisp is the right profile, and it is worth saying why the obvious objection fails. The file's own description opens with "a playful developer-tools system", and hand-drawn hedgehogs in lab coats are about as illustration-led as a brand gets, which points at Playful under SPEC §5 rule 3. But that rule is a conjunction judged on saturation *and role*: PostHog's saturated colour is one yellow CTA pill, the four callout pastels are static doc annotations rather than interactive elements, the type voice is IBM Plex at 400/600/700 with uppercase eyebrows, and the file explicitly forbids gradients, shadows and a second saturated CTA. The identity is docs, code blocks and flat cards — rule 2's developer-tool tell — with the illustration sitting in the margins as decoration. Overshoot easing on a 6px-radius bordered card would read as borrowed from another file in the collection. Roster assignment stands; no switch argued.

The one place the document now reads thinner than the brand is the States matrix, where five of eight states are this audit's prescription rather than PostHog's own behaviour. That is marked on every row, and the Known Gaps entry says plainly which three states the captured pages actually support.
