## A52 · pinterest

Scores before -> after (1-5), from the harness:

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 5 | 5 | 1 | 3 | 1 | 1 |
| after | 5 | 5 | 5 | 5 | 5 | 5 |

Contrast moved from 1 to 5 by closing one real failure (no focus ring covered `surface-dark`) and disclosing five frozen extracted failures with their measured ratios. The five hexes were not altered.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A / E | focus ring on `{colors.surface-dark}` | `focus-outer` `#435ee5` measures 2.87:1 on `#262622`, the ground of `{component.hero-cta-strip}`. No ring in the file cleared 3:1 there. The file's composite ring (2px white `focus-inner` gap + coloured outer band) separates its own bands at 5.29:1, which is a WCAG 2.2 Focus Appearance pass *for band separation* but does not make the ring perceivable against a dark surface. Fixed by adding the polarity counterpart `focus-on-dark`. |
| P0 | F | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. |
| P0 | G | whole file | No `## Accessibility` section; five extracted contrast failures undisclosed. |
| P1 | H | Components | Only default / active / pressed / disabled documented. hover, focus-visible, loading, selected and error named nowhere in a structured line. |
| P1 | B | `{colors.hairline}`, `{colors.hairline-soft}` | 1.4:1 / 1.36:1 and 1.26:1 / 1.22:1 against canvas and `surface-soft`. Both are real extracted dividers. Scoped to decoration in prose; **no parallel token added**, because the palette already owns `{colors.ash}` at 3.17:1 doing the control-boundary work (SPEC §1: use the passing tone you have, add nothing). |
| P1 | B | `{colors.success-pale}` | 1.24:1 on canvas. The harness scores it as a text tone; the file uses it only as a pill fill, with `{colors.success-deep}` ink on it at 9.97:1. Disclosed with both ratios. |
| P2 | B | `{colors.ash}` on `{colors.surface-card}` | 2.92:1 — below 3:1 as a boundary on the cream card surface, though it passes on canvas (3.17:1). Noted in Accessibility as a usage restriction; the file does not currently bind that pair. |
| P2 | B | `{colors.on-primary}` on `{colors.primary}` | 4.78:1 — passes 4.5:1 with almost no headroom. Flagged so nobody tints either value. |
| P2 | C | `canvas` / `surface-soft` / `surface-card` | 1.04:1, 1.08:1 and 1.05:1 between layers — the three chrome surfaces are not distinguishable by contrast. This is correct for the brand (a deliberately invisible cream wash) and elevation is expressed one consistent way: flat by default, hairline border at level 1, scrim + ambient shadow at level 2 only. No shadow/border mixing. Left as is. |
| P2 | A | harness / brief | The brief listed `text-dim` as a missing role and `focus-outer on primary` at 1.11:1 as a failure. Neither reproduces: the harness resolves `text-dim` to `ink-soft`, and accent fills are excluded from ring coverage per SPEC §1. Stale brief text, not a file defect; no alias token invented. |
| P2 | D | typography | Every one of the 14 roles carries family, size, weight, line height and letter spacing. Body at 16px/1.4 in `{colors.body}` measures 12.7:1 on canvas and `{colors.ink}` 19.4:1 on `surface-card`. No action. |
| P2 | E | ladders | spacing 4/6/8/12/16/24/32/64, radius 0/8/16/32/pill — no value sits outside its scale. `rounded.sm` (8px) is documented as near-unused rather than deleted; it is extracted. No action. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus-on-dark: "#617bff"` | The light-default file needs a dark-polarity ring (SPEC §1). 4.18:1 on `#262622`. Reuses the brand's own pressed-blue hex rather than inventing one; the role is prescribed, the hex is extracted. |
| frontmatter | — -> `motion:` group, Playful block verbatim | SPEC §4/§5. |
| Colors › Semantic | — -> **Focus On Dark** entry | States the 2.87:1 failure of `focus-outer` on `surface-dark` and why a second ring exists. |
| Colors › Surface | hairline entries -> same + "decorative only" + a control-boundary note pointing at `{colors.ash}` | Scopes the frozen tones away from boundary duty without adding a token. |
| Components | — -> `### Interaction States` matrix | All eight states per component, each marked Extracted or Prescribed. Structural surfaces (`primary-nav`, `footer-section`, `hero-cta-strip`) are stated as genuinely one state. |
| after Components | — -> `## Motion & Animation` | First line states the system is prescribed, not measured. 13-row table, transform/opacity only, exits shorter than entrances, `@media (prefers-reduced-motion: reduce)` contract. |
| after Motion | — -> `## Accessibility` | Measured pairs, the five frozen failures with ratios, per-surface ring table with the 2px outside offset, tap targets marked unverified, reduced motion. |
| Known Gaps | +5 bullets | Motion prescribed; hover/loading/error prescribed; `focus-on-dark` a prescribed role; tap targets unverified. |

Section order now matches SPEC §3 exactly; `Responsive Behavior` was already top-level and was not touched. Nothing outside these points was reflowed.

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #000000 / `canvas` #ffffff | 21.0:1 | 4.5 | pass |
| `ink` / `surface-soft` #fbfbf9 | 20.27:1 | 4.5 | pass |
| `ink` / `surface-card` #f6f6f3 | 19.4:1 | 4.5 | pass |
| `ink-soft` #211922 / `canvas` | 17.12:1 | 4.5 | pass |
| `body` #33332e / `canvas` | 12.7:1 | 4.5 | pass |
| `mute` #62625b / `canvas` | 6.14:1 | 4.5 | pass |
| `mute` / `surface-card` | 5.68:1 | 4.5 | pass |
| `on-primary` #ffffff / `primary` #e60023 | 4.78:1 | 4.5 | pass (no headroom) |
| `on-dark` #ffffff / `surface-dark` #262622 | 15.19:1 | 4.5 | pass |
| `error` #9e0a0a / `canvas` | 8.39:1 | 4.5 | pass |
| `error-deep` #cc001f / `canvas` | 5.85:1 | 4.5 | pass |
| `success-deep` #103c25 / `canvas` | 12.39:1 | 4.5 | pass |
| `accent-purple` #7e238b / `canvas` | 8.4:1 | 4.5 | pass |
| `accent-purple-deep` #6845ab / `canvas` | 6.94:1 | 4.5 | pass |
| `ash` #91918c / `canvas` | 3.17:1 | 3.0 boundary | pass as boundary, fail as text |
| `ash` / `surface-card` | 2.92:1 | 3.0 | fail — restricted in prose |
| `stone` #c8c8c1 / `canvas` | 1.68:1 | 3.0 | fail — utility/disabled only, WCAG-exempt where disabled |
| `hairline` #dadad3 / `canvas` | 1.4:1 | 3.0 | fail — disclosed, decorative |
| `hairline` / `surface-soft` | 1.36:1 | 3.0 | fail — disclosed |
| `hairline-soft` #e5e5e0 / `canvas` | 1.26:1 | 3.0 | fail — disclosed |
| `hairline-soft` / `surface-soft` | 1.22:1 | 3.0 | fail — disclosed |
| `success-pale` #c7f0da / `canvas` | 1.24:1 | 4.5 as text | fail as text; it is a fill. `success-deep` on it: 9.97:1 pass |
| `focus-outer` #435ee5 / `canvas` | 5.29:1 | 3.0 | pass |
| `focus-outer` / `surface-soft` | 5.1:1 | 3.0 | pass |
| `focus-outer` / `surface-card` | 4.88:1 | 3.0 | pass |
| `focus-outer` / `surface-dark` | 2.87:1 | 3.0 | **fail — the gap this audit fixed** |
| `focus-outer` / `primary` #e60023 | 1.11:1 | n/a | the control fill, not a ground; ring sits outside at a 2px offset |
| `focus-on-dark` #617bff / `surface-dark` | 4.18:1 | 3.0 | pass |
| `focus-on-dark` / `ink` #000000 (active chip fill) | 5.79:1 | 3.0 | pass |
| `focus-inner` #ffffff / `focus-outer` | 5.29:1 | 3.0 band separation | pass |
| `focus-inner` / `focus-on-dark` | 3.63:1 | 3.0 band separation | pass |
| layer separation `canvas` / `surface-soft` | 1.04:1 | — | by design |
| layer separation `canvas` / `surface-card` | 1.08:1 | — | by design |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `ease-standard` | `scale(1.02)` + `opacity` | no scale; fill/opacity only at 130ms |
| Press | `{motion.duration-instant}` 70ms | `ease-standard` | `scale(0.96)` | no scale; pressed fill applied instantly |
| Focus | `{motion.duration-instant}` 70ms | `ease-standard` | ring `opacity` | ring appears instantly |
| Page / route | `{motion.duration-base}` 200ms | `ease-enter` | `opacity` + `translateY(8px)` | opacity only, 130ms |
| Modal / drawer enter | `{motion.duration-base}` 200ms | `ease-enter` | `opacity` + `scale(0.96→1)`, scrim to 0.5 | opacity only, 130ms |
| Modal / drawer exit | `{motion.duration-fast}` 130ms | `ease-exit` | `opacity` + `scale(1→0.98)` | opacity only, 130ms |
| Dropdown enter | `{motion.duration-fast}` 130ms | `ease-enter` | `opacity` + `scale(0.98→1)` | opacity only, 130ms |
| Dropdown exit | `{motion.duration-instant}` 70ms | `ease-exit` | `opacity` | unchanged |
| Toast enter | `{motion.duration-base}` 200ms | `ease-enter` | `opacity` + `translateY(12px)` | opacity only, 130ms |
| Toast exit | `{motion.duration-fast}` 130ms | `ease-exit` | `opacity` + `translateY(8px)` | opacity only, 130ms |
| List / pin-grid enter | `{motion.duration-slow}` 320ms, `stagger-step` 60ms | `ease-enter` | `opacity` + `translateY(12px)` | opacity only, 130ms, stagger 0 |
| List / pin-grid exit | `{motion.duration-fast}` 130ms | `ease-exit` | `opacity` + `scale(0.98)` | opacity only, 130ms |
| Loading | `{motion.duration-emphasis}` 450ms loop | `ease-standard` | skeleton `opacity` 0.6↔1; spinner `rotate` | loop frozen, static 0.6 block, static label |

Only infinite animation is the loader. No brand ambience. Exit shorter than entrance in every pair.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/briefs/A52-pinterest.md` | Lists "Missing colour roles: text-dim" and "focus-outer on primary 1.11:1". Neither reproduces against the current `audit.py`: `text-dim` resolves to `ink-soft`, and `ACCENTISH` fills are excluded from ring coverage per SPEC §1. A reviewer following the brief literally would invent a `text-dim` alias and try to repaint a ring to pass on #e60023. | Regenerate the briefs from the current harness output, or stamp each brief with the `audit.py` revision it was generated from. |
| `theme-audit/audit.py` ~line 356 | `focus_tokens` is name-matched on `^focus($|[-_])`. A file whose ring duty is carried by a differently named tone reports "no ring covers X" even when a passing tone exists. Here the finding was genuine — Pinterest owns no ring for dark grounds — so nothing was worked around, but the check will produce false positives elsewhere. | Also accept a colour bound as `outlineColor` / `borderColor` on a `*-focused` component entry, mirroring the existing `borderColor` fallback used for the `border` role. |
| `theme-audit/audit.py` ~line 525 | The states check counts a state word appearing in any structured line inside `## Components`, so "hover — not captured" scores as documented. Honest files and gaming files score alike. | Require the state word in a cell/row that also carries a value or an explicit Extracted/Prescribed marker, or report extracted-vs-prescribed counts separately. |
| `theme-audit/audit.py` ~line 324 | `success-pale` is charged at 4.5:1 as "semantic tone as text" although the file only ever uses it as a fill. | Where a semantic tone appears as a component `backgroundColor`, measure the declared `textColor` on it instead of the tone on canvas. |

### Needs approval

1. **`{colors.focus-on-dark}` duplicates an existing hex.** `#617bff` is already in the palette as `{colors.accent-pressed-blue}`. I added it under a second name because SPEC §1 requires the polarity counterpart ring to be a named `focus` token and the harness only recognises rings by that name. It is not an alias-for-a-regex — it has a real job (the ring drawn on `{component.hero-cta-strip}` and on the inverted active chip) — but it is a duplicated value and a maintainer may prefer a single token referenced twice.
2. **`{colors.hairline}` 1.4:1 / 1.36:1 and `{colors.hairline-soft}` 1.26:1 / 1.22:1.** Left frozen and disclosed. Nearest passing boundary values on white are `#949494` (3.03:1) or `#919191` (3.15:1) — a visibly grey rule that would break the warm-cream chrome. Usage note that makes the real values defensible: these are decorative 1px dividers whose information is also carried by 64px section spacing, and no control relies on them; `{colors.ash}` (3.17:1) carries every perceivable boundary.
3. **`{colors.ash}` at 2.92:1 on `{colors.surface-card}`.** Usage note: boundary use is restricted to `{colors.canvas}` grounds. Nearest passing value on the cream card is `#8f8f8f` (3.23:1 on white, 3.0:1 on `#f6f6f3`) if a cream-surface boundary is ever needed.
4. **`{colors.on-primary}` on `{colors.primary}` at 4.78:1.** Passes, but with 0.28 of headroom. Do not approve any tint of either value.
5. **Prescribed hover / loading / error / saved-pin states.** The file's own policy line says hover is undocumented. I kept that line and added prescribed treatments marked P. If the policy is meant to forbid specifying hover at all, those rows should be removed and the states score accepted as lower.

### Identity verdict

Still Pinterest. The added material is anchored to things only this file has: the ring problem is the `create.pinterest.com` dark CTA strip, the prescribed hover is a 1.02 scale on *the pin image*, the list-enter row is the masonry grid with an 8px gutter, the loading skeleton is a `surface-card` block *at the pin's own aspect ratio*, and the selected state is the fully inverting filter chip. Nothing in the new sections would transplant to another file unchanged.

**Profile: Playful is correct — kept.** The roster assignment survives SPEC §5 rule 3 on both tests: saturated colour sits on interactive elements (red is reserved for CTAs, the active tab and the wordmark, and the inverting chip is interactive), and the type voice is informal — Pin Sans at 600 for a 70px display, pill geometry at every size, no serif anywhere. The counter-evidence is real and worth naming: the file forbids gradients and shadows, calls its chrome "quiet", and gets its depth from photography — which is Calm's signature. But Calm's tell per SPEC is a 400 display weight and a sober self-description, and this file has neither; the restraint here is about *chrome*, to let saturated imagery dominate, not about the interaction feel. A 200ms base with a small scale pop on press matches a product whose core gesture is tapping images. Cinematic is excluded: no full-bleed slow reveal, no sparse type, 8px gutters.
