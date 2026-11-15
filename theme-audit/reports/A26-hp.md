## A26 · hp

Scores before -> after (1-5), from the harness: tokens 2 -> 5 · refs 5 -> 5 · contrast 2 -> 5 · sections 2 -> 5 · motion 1 -> 5 · states 1 -> 5

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule. Nothing in the file said what moves or how long it takes. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Five contrast failures were present and undisclosed. |
| P0 | A Tokens | `colors.focus` | No focus ring token anywhere. Keyboard focus was documented only as "gains 1px `{colors.ink}` border on focus (no halo)" on `text-input`, and nowhere else. |
| P0 | B Colour | `hairline` `#e8e8e8` on `canvas` `#ffffff` | 1.23:1 against a 3.0:1 non-text minimum, and it is the documented boundary of comparison-table cells and FAQ outers. Extracted and frozen, so disclosed rather than changed. |
| P0 | B Colour | `hairline-strong` / `steel` `#c2c2c2` on `canvas` | 1.78:1 against 3.0:1, and `steel` is the only boundary of `text-input` and `text-input-search`. |
| P1 | A Tokens | `colors.surface`, `colors.text-dim` | Roles unresolvable: the file had `paper` and `charcoal` doing the work under names no role pattern matches. |
| P1 | H States | `## Components` | Only default and active/pressed documented; hover, focus-visible, loading, selected and error named nowhere. The section opened by asserting hover states were "silently filtered", which left the gap permanent rather than explicit. |
| P1 | C Elevation | `## Elevation & Depth` | Shadow values written as raw `rgba(...)` with no `shadow:` group to reference, and the Hairline level mixed border and shadow language with no rule saying which wins. |
| P1 | B Colour | `badge-sale-coral` | `#ffffff` on `#ff5050` is 3.22:1 at 14px/700, below 4.5:1. Real brand hex, so recorded under Needs approval. |
| P1 | B Colour | `primary-bright` `#296ef9` on `ink` `#1a1a1a` | 3.89:1 — passes for large text, fails body copy, and the file prescribed it for "dark-band CTA links" without a size floor. |
| P2 | C Elevation | canvas / surface / cloud / fog | Layer separation is 1.00:1, 1.07:1 and 1.23:1. Not a defect — it is HP's real system — but the file never said the shadow is load-bearing. |
| P2 | E Shapes | `rounded.xs` 2px, `rounded.sm` 3px | One-unit step inside a ladder that otherwise doubles 4 → 8 → 16. Both carry distinct documented uses, so left alone and logged in Known Gaps. |
| P2 | I Identity | Overview vs `chevron-decoration` | Chevron cut is given as 45° in the Overview and ~60° in the component entry. Unmeasured either way; left as found and logged. |
| P2 | B Colour | `ink-soft` `#292929`, `ink-deep` `#000000` | 1.20:1 and 1.21:1 against `ink`. Described as a "subtle textural shift" that cannot render as one. |
| P2 | A Tokens | Iteration Guide item 6 | Says "two flame elements per viewport" — "flame" is vocabulary borrowed from another file in the collection; HP has no flame. Left unedited to keep the diff reviewable, flagged here. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `surface: "#ffffff"` | Resolves the `surface` role as an alias of `paper`; adds no new hex. |
| frontmatter `colors:` | — -> `text-dim: "#3d3d3d"` | Resolves the `text-dim` role as an alias of `charcoal`; 10.86:1 on canvas. |
| frontmatter `colors:` | — -> `hairline-control: "#767676"` | Parallel accessible boundary token for controls, per SPEC §2. 4.54:1 on canvas. Prescribed, labelled as such. |
| frontmatter `colors:` | — -> `focus: "#0e3191"`, `focus-inset: "#ffffff"`, `focus-on-dark: "#c9e0fc"` | The repo's first focus ring. Deep navy rather than Electric Blue so the ring never vanishes into a blue CTA; white inset band makes it legible on the accent fill; soft blue serves the `ink` slabs. |
| frontmatter | — -> `shadow:` group (`soft-lift`, `floating`) | The prose documented real rgba shadows with no token to reference. |
| frontmatter | — -> `motion:` group | Calm profile block from SPEC §5, verbatim. |
| `## Colors` → Brand & Accent | — -> three focus-token entries with measured ratios | Documents the new ring and why it is deep navy. |
| `## Colors` → Surface | — -> `surface` and `hairline-control` entries | States that surface equals canvas at 1.00:1 and scopes the frozen hairlines to decoration. |
| `## Colors` → Text | — -> `text-dim` entry | Names the alias. |
| `## Elevation & Depth` table | raw `rgba(...)` -> `{shadow.soft-lift}` / `{shadow.floating}` | Token references instead of loose values. |
| `## Elevation & Depth` prose | — -> "shadow for lift, hairline for enclosure, never both" + the four measured layer ratios | Makes elevation one consistent mechanism and states that the shadow is load-bearing. |
| `## Components` lead note | "No hover states documented." -> extracted-versus-prescribed note | The gap is now filled and labelled rather than asserted as permanent. |
| `## Components` → `text-input` | focus = 1px ink border -> adds the prescribed `hairline-control` default and the `focus` ring | The input's only boundary was at 1.78:1. |
| `## Components` | — -> `### Interaction States` table | Eleven components × eight states. Badges and `chevron-decoration` are marked genuinely two-state and one-state. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Eleven-row interaction table, transform/opacity only, exits shorter than entrances, `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | — -> `## Accessibility` | 22 measured pairs, a plain-language failure list, per-surface focus-ring table, tap targets (marked not verifiable from a document), reduced motion. |
| end of file | — -> `## Known Gaps` | Separates prescribed from genuinely unknown, and states what a document cannot measure. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#1a1a1a` / `canvas` `#ffffff` | 17.4:1 | 4.5:1 | Pass |
| `ink` / `surface` `#ffffff` | 17.4:1 | 4.5:1 | Pass |
| `ink` / `cloud` `#f7f7f7` | 16.25:1 | 4.5:1 | Pass |
| `ink` / `fog` `#e8e8e8` | 14.2:1 | 4.5:1 | Pass |
| `text-dim` / `charcoal` `#3d3d3d` / `canvas` | 10.86:1 | 4.5:1 | Pass |
| `graphite` `#636363` / `canvas` | 6.01:1 | 4.5:1 | Pass |
| `graphite` / `cloud` | 5.61:1 | 4.5:1 | Pass |
| `on-primary` `#ffffff` / `primary` `#024ad8` | 7.06:1 | 4.5:1 | Pass |
| `primary` as link text / `canvas` | 7.06:1 | 4.5:1 | Pass |
| `on-ink` `#ffffff` / `ink` | 17.4:1 | 4.5:1 | Pass |
| `primary-bright` `#296ef9` / `ink` | 3.89:1 | 4.5:1 | Fail (passes 3:1 large text) |
| `error` / `bloom-deep` `#b3262b` / `canvas` | 6.5:1 | 4.5:1 | Pass |
| `storm-deep` `#356373` / `canvas` | 6.6:1 | 4.5:1 | Pass |
| `hairline-control` `#767676` / `canvas` | 4.54:1 | 3.0:1 | Pass |
| `hairline-control` / `cloud` | 4.24:1 | 3.0:1 | Pass |
| `hairline-control` / `fog` | 3.71:1 | 3.0:1 | Pass |
| `hairline` `#e8e8e8` / `canvas` | 1.23:1 | 3.0:1 | Fail — disclosed, frozen |
| `hairline` / `surface` | 1.23:1 | 3.0:1 | Fail — disclosed, frozen |
| `hairline-strong` / `steel` `#c2c2c2` / `canvas` | 1.78:1 | 3.0:1 | Fail — disclosed, frozen |
| `hairline-strong` / `surface` | 1.78:1 | 3.0:1 | Fail — disclosed, frozen |
| `badge-sale-coral` `#ffffff` / `bloom-coral` `#ff5050` | 3.22:1 | 4.5:1 | Fail — disclosed, needs approval |
| `focus` `#0e3191` / `canvas` | 11.25:1 | 3.0:1 | Pass |
| `focus` / `cloud` | 10.5:1 | 3.0:1 | Pass |
| `focus` / `fog` | 9.18:1 | 3.0:1 | Pass |
| `focus` / `primary` `#024ad8` | 1.59:1 | 3.0:1 | Fail — disclosed; mitigated by the `focus-inset` band |
| `focus-inset` `#ffffff` / `focus` (band separation) | 11.25:1 | 3.0:1 | Pass |
| `focus-on-dark` `#c9e0fc` / `ink` `#1a1a1a` | 12.89:1 | 3.0:1 | Pass |
| `ink` / `bloom-coral` (the passing alternative) | 5.4:1 | 4.5:1 | Pass |
| `canvas` / `surface` (layer separation) | 1.00:1 | — | Not a WCAG pair; shadow-only separation |
| `canvas` / `cloud` (layer separation) | 1.07:1 | — | Shadow-only separation |
| `canvas` / `fog` (layer separation) | 1.23:1 | — | Shadow-only separation |

No single hex can satisfy the harness's focus checks here: clearing 3:1 against `#ffffff` caps the ring's relative luminance at 0.30, while clearing 3:1 against `#024ad8` requires at least 0.396. That is why the ring is specified as a composite with a mandatory `focus-inset` offset band, which is what WCAG 2.2 Focus Appearance measures.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity`, `box-shadow`, underline `transform: scaleX()` | instant swap, no scaleX travel |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `transform: scale(0.98)` | scale removed, fill change only |
| Focus ring appear | `{motion.duration-instant}` 80ms | `{motion.ease-enter}` | `opacity` | appears at full opacity, no transition |
| Page / route transition | 250ms out, 150ms in | `{motion.ease-standard}` | `opacity` only | cross-fade at `{motion.duration-reduced}` |
| Modal / drawer | enter 250ms, exit 150ms | `ease-enter` / `ease-exit` | `opacity` + `translateY(8px)`; drawer `translateX(100%)` | opacity only at 150ms, scrim fades |
| Dropdown | enter 150ms, exit 80ms | `ease-enter` / `ease-exit` | `opacity` + `translateY(-4px)` | opacity only at 150ms |
| Toast | enter 250ms, exit 150ms | `ease-enter` / `ease-exit` | `opacity` + `translateY(8px)` | opacity only at 150ms |
| List enter | 250ms per item, `{motion.stagger-step}` 40ms apart, capped at 8 | `{motion.ease-enter}` | `opacity` + `translateY(8px)` | all fade together at 150ms, no stagger |
| List exit | 150ms, no stagger | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | opacity only at 150ms |
| Loading | spinner 900ms linear loop; skeleton cross-fade `{motion.duration-slow}` 400ms | linear / `ease-standard` | `transform: rotate()`; skeleton `opacity` | static 25%-arc glyph plus text label; skeletons hold one opacity |
| First paint | none | — | — | none; nothing animates on load |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `design-md/hp/DESIGN.md` line 820 (Iteration Guide item 3) | Tells the reader to run `npx @google/design.md lint DESIGN.md`, a command this repo does not provide and which is not the harness that scores these files. Inside my owned file, but outside every dimension I was asked to fix, so left for a repo-wide decision rather than changed in one file. | Replace with `python3 theme-audit/audit.py --site hp` across all 84 files in one pass. |
| `theme-audit/audit.py` lines 283-291 | A focus ring is measured against the `accent` fill, but a composite ring's `focus-inset` band is only measured against the outer ring — so a correctly specified two-band ring on a saturated accent always books one failure that can be cleared only by disclosure. | When a file defines a `focus-*` inset/halo band that separates ≥3:1 from the ring, treat the ring-on-accent pair as satisfied by the composite instead of as a failure. |
| `theme-audit/audit.py` lines 212-218 | `check()` and `check_all()` use `f"{fg} on {bg}"` as the dedupe key, so a file whose `surface` is the same hex as its `canvas` books every boundary failure twice (`hairline on canvas` and `hairline on surface`, both 1.23:1) and loses two contrast points for one defect. | Dedupe on `(fg_hex, bg_hex, required)` rather than on the token-name pair. |

### Needs approval

1. **`badge-sale-coral` — white on `bloom-coral` `#ff5050` at 3.22:1, requires 4.5:1.** `#ff5050` is a real HP sale-tag colour and is not changed here.
   - Nearest passing value, keeping the coral: switch the chip label to `{colors.ink}` `#1a1a1a` on `#ff5050` → **5.4:1**. Costs nothing but the label colour.
   - Nearest passing value, keeping white text: darken the chip to `#c2403f` → 4.54:1. This falsifies a brand hex and is **not** recommended.
   - Usage note that would make the real value defensible: white on `#ff5050` clears the 3:1 large-text threshold, so the chip is defensible only if its label is set at 24px+, or 18.66px+ at weight 700. It currently uses `{typography.caption-bold}` at 14px/700, which does not qualify.
2. **`primary-bright` `#296ef9` on `ink` `#1a1a1a` at 3.89:1, requires 4.5:1.** Used for dark-band CTA links.
   - Usage note now written into the file: valid for `{typography.display-sm}` (24px) and larger only; body links inside `ink` slabs use `{colors.on-ink}`.
   - Nearest passing value if it must carry body copy: `#4e86fb` → 4.54:1 on `#1a1a1a`. Not applied, since it is a brand tone.
3. **`hairline-control` `#767676` is an invented value**, not an HP colour. It is labelled prescribed in both `## Colors` and `## Known Gaps`, but it is new vocabulary in a document about a real brand and deserves a sign-off.
4. **`focus` `#0e3191` reuses the pressed-CTA navy for a second job.** Defensible — it is HP's own blue and clears 3:1 on every light surface — but a brand team may prefer a dedicated ring hex.

### Identity verdict

Still HP. The additions are phrased in the file's own vocabulary — Electric Blue stays the lone accent and gains no rival, the new ring and boundary tones are drawn from the existing blue and grey families, and the motion table repeats HP's own structural facts (the chevrons do not move, the `ink` slabs close the page rhythm, hover shifts to `primary-deep` or `cloud` rather than introducing a hue). Nothing in the diff would suit a different brand unchanged.

**Calm is the right profile, and I kept it.** HP triggers none of the earlier rules: not luxury, automotive or hardware-flagship in presentation (the photography is catalog product-on-white, not full-bleed cinematic); not a developer tool; not illustration-led — the palette lists 34 hexes but saturated colour appears on exactly one interactive element, the blue CTA, with coral and the storm teals confined to static chips and illustration backdrops. Display weight 500 at 72px, line-height 1.0, a flat shadow ladder and an explicit rule against gradients and opacity hierarchy are the composed-editorial signals Calm is for.

The one thing worth watching: with all six required sections and the states table in place, the document is now roughly 40% prescribed content by length, and the character of the file depends on those additions staying in HP's voice. The `## Known Gaps` section exists mainly so a future reader can tell which half is HP and which half is this audit.
