## A35 · mercury

Scores before -> after (1-5), from the harness: tokens 3 -> 4 · refs 5 -> 5 · contrast 1 -> 5 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 5

`tokens` stops at 4 because the `border` role stays unresolved. That is deliberate: see Shared issues.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, G | `colors.focus` | No focus ring token anywhere in the file; focus-visible was undocumented on every control. Added `focus: "#5266eb"` (prescribed), measured against all six surfaces. |
| P0 | B | `toggle-switch` | Declared pair was wrong, not merely low: `textColor: {colors.ink-secondary}` over `backgroundColor: {colors.primary}` = 1.61:1. The prose says the label sits *beside* the indigo track on the light canvas. The component asserted a pair the brand never renders. |
| P0 | B | `nav-link`, `button-icon-round`, `stat-block`, `logo-strip` | Night-world components declared `textColor` and no ground, so the harness measured `{colors.on-dark}` on `{colors.canvas}` at 1.14:1 — four failures that cannot render. Ground now declared. |
| P0 | B | `button-glass-dark`, `button-tint-dark` | `backgroundColor` was a raw `rgba()`, which no tool here composites, so both fell back to the light canvas at 1.14:1. Replaced with the composited hex plus a `fillSource` recording the source `rgba()` and its ground. |
| P0 | F | whole file | No `motion:` group, no Motion & Animation section, no reduced-motion rule. Added, with the Calm block verbatim. |
| P0 | G | whole file | No Accessibility section: no contrast stated, no focus-ring claim, no reduced-motion statement. Added. |
| P1 | C | `canvas` / `surface` / `surface-tint` / `night` / `night-raised` | Layer separation is 1.03:1, 1.03:1 and 1.08:1; a card on the light canvas is 1.14:1. Elevation is tonal and effectively imperceptible as a boundary. Extracted, so disclosed rather than changed. |
| P1 | B, E | `{colors.fog}` | 1.70:1 on `{colors.canvas}` while doing real boundary work (1px accordion rules, `ex-pricing-tier` `borderColor`, `ex-data-table-cell` `rowBorder`). Frozen extracted value; scoped to decoration in the file and the failure stated plainly. No parallel token invented — `{colors.slate}` (4.75:1 on canvas) already serves the strong case. |
| P1 | H | every component | Components carried default only. Each entry now names its state ladder, labelled prescribed; genuinely static entries say "default only" and why. |
| P1 | A3 | section contract | `Responsive Behavior` existed only as `### Responsive Strategy` inside Layout. Moved verbatim, children promoted one level, nothing duplicated. |
| P1 | A3 | section contract | No `Known Gaps` section at all. Added, listing everything prescribed or uncaptured. |
| P2 | C | Elevation & Depth | Level 1 is "≈2–9% ink" with no `shadow:` group and no numbers; no `{shadow.*}` reference exists, so nothing dangles, but the value is unusable as written. Recorded in Known Gaps rather than invented. |
| P2 | B | `button-tint-light`, `button-outline-light`, `button-small` | Raw `rgba()` fills still fall back to the canvas floor. Their labels are `{colors.ink}` and clear 4.5:1 on both the composite (12.70:1, 12.77:1) and the canvas (14.42:1), so no measurement is wrong — noted in Known Gaps, left alone to keep the diff small. |
| P2 | B | `{colors.on-primary}` on `{colors.primary}` | 4.71:1 — passes AA body text with 0.21 of margin. Any darkening of the label or lightening of the indigo breaks it. Stated in Accessibility. |
| P2 | D | typography | Every one of the 11 roles has family, size, weight, line height and tracking. No gap. Body at 360 weight on `{colors.canvas}` measures 14.42:1, so the unusually light weights are not a contrast problem at the documented sizes. |
| P2 | E | `rounded` | Ladder is 0 / 4 / 8 / 12 / 16 / 32 / 40 / 9999. `xl: 32px` and `pill: 40px` are both capsule radii at the brand's 40px control height, which looks like a duplicate — but the file uses them distinctly (32px on `button-primary` and the input's left edge, 40px on secondary and nav pills), so it is a real brand distinction, not a stray value. No change. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | (no focus token) -> `focus: "#5266eb"` with a comment marking it prescribed | SPEC section 1 requires a focus ring; Mercury Indigo is the only palette value clearing 3:1 on all six surfaces, so one ring replaces a light/dark pair |
| frontmatter | (no `motion:` group) -> Calm block, verbatim from SPEC section 5 | SPEC section 4 |
| `components.nav-link` | no ground -> `backgroundColor: "{colors.night}"` | It is drawn in the night nav bar; the harness was measuring it on the light canvas |
| `components.button-glass-dark` | `backgroundColor: "rgba(175, 178, 206, 0.2)"` -> `"#353644"` + `fillSource: "rgba(175, 178, 206, 0.2) over {colors.night}"` | Same 20% wash, now measurable; the source value is preserved, not discarded |
| `components.button-tint-dark` | `backgroundColor: "rgba(156, 180, 232, 0.2)"` -> `"#323649"` + `fillSource` | As above |
| `components.button-icon-round` | no ground -> `backgroundColor: "{colors.night-raised}"` | Prose: play/pause and "+" on spotlight cards |
| `components.toggle-switch` | `backgroundColor: "{colors.primary}"` -> `backgroundColor: "{colors.canvas}"`, `trackColor: "{colors.primary}"` | The label is never drawn on the indigo; the track fill keeps its own key |
| `components.stat-block`, `components.logo-strip` | no ground -> `backgroundColor: "{colors.night}"` | Both are homepage night-canvas elements |
| `## Colors` | -> added `### Boundaries` and `### Focus` | States which tokens carry boundaries, scopes fog to decoration, and records the ring's six measured ratios and its 2px offset |
| `## Components` lead note | "Only Default states are documented." -> note that colour/type/geometry are extracted while the States lines are prescribed | SPEC: do not present inferred behaviour as extracted |
| `## Components`, every entry | -> added a `- States:` line | SPEC section 7 |
| after `## Components` | -> new `## Motion & Animation` | 13-row interaction table, `{motion.*}` references only, transform/opacity only, exits shorter than entrances, both infinite animations declared, `@media (prefers-reduced-motion: reduce)` block |
| after Motion | -> new `## Accessibility` | 16 measured pairs, the fog failure stated plainly, focus ring per surface, layer separation, reduced motion, tap-target intent marked unverifiable |
| `## Layout` | `### Responsive Strategy` (+ four `####`) removed -> re-emitted verbatim as `## Responsive Behavior` (+ four `###`) after Do's and Don'ts | SPEC section 3: move, never duplicate |
| `## Do's and Don'ts` | -> two Don'ts added (no layout-property animation; fog is never a sole boundary) | Keeps the new motion and contrast rules where a reader will meet them |
| end of file | -> new `## Known Gaps` | Everything prescribed or uncaptured, including the absent shadow values |

### Contrast checks

All computed with WCAG 2.1 relative luminance via a `python3` snippet; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #28253b / `canvas` #fbfcfd | 14.42:1 | 4.5 | Pass |
| `ink` / `surface` #ffffff | 14.81:1 | 4.5 | Pass |
| `ink` / `surface-tint` #fbfbff | 14.35:1 | 4.5 | Pass |
| `ink` / `lavender` #edecfb | 12.69:1 | 4.5 | Pass |
| `ink-secondary` #554e7b / `canvas` | 7.40:1 | 4.5 | Pass |
| `ink-secondary` / `surface` | 7.60:1 | 4.5 | Pass |
| `ink-secondary` / `lavender` | 6.51:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary` #5266eb | 4.71:1 | 4.5 | Pass (0.21 margin) |
| `on-dark` #ededf3 / `night` #171721 | 15.25:1 | 4.5 | Pass |
| `on-dark` / `night-raised` #1e1e2a | 14.13:1 | 4.5 | Pass |
| `on-dark` / glass fill #353644 | 10.22:1 | 4.5 | Pass |
| `on-dark` / tint fill #323649 | 10.24:1 | 4.5 | Pass |
| `ink` / tint-light fill #eaedfb | 12.70:1 | 4.5 | Pass |
| `ink` / outline-light fill #edeef2 | 12.77:1 | 4.5 | Pass |
| `fog` #c3c3cc / `night` | 10.16:1 | 4.5 | Pass |
| `fog` / `night-raised` | 9.42:1 | 4.5 | Pass |
| `slate` #70707d / `canvas` | 4.75:1 | 4.5 | Pass |
| `slate` / `night` (1px divider) | 3.64:1 | 3.0 | Pass |
| `primary` / `lavender` (plan suffix, 28px) | 4.04:1 | 3.0 | Pass as large text |
| **`fog` / `canvas` (1px accordion rule)** | **1.70:1** | 3.0 | **Fail — extracted, frozen, disclosed** |
| `toggle-switch` label as previously declared: `ink-secondary` / `primary` | 1.61:1 | 4.5 | Fail — pair never rendered; declaration corrected |
| `focus` #5266eb / `canvas` | 4.59:1 | 3.0 | Pass |
| `focus` / `surface` | 4.71:1 | 3.0 | Pass |
| `focus` / `surface-tint` | 4.56:1 | 3.0 | Pass |
| `focus` / `lavender` | 4.04:1 | 3.0 | Pass |
| `focus` / `night` | 3.78:1 | 3.0 | Pass |
| `focus` / `night-raised` | 3.50:1 | 3.0 | Pass |
| Layer: `canvas` / `surface` | 1.03:1 | — | Not separable |
| Layer: `surface` / `surface-tint` | 1.03:1 | — | Not separable |
| Layer: `night` / `night-raised` | 1.08:1 | — | Not separable |
| Layer: `lavender` / `canvas` | 1.14:1 | — | Not separable |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity` of fill wash | Opacity at `{motion.duration-reduced}`, no travel |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` to 0.92 | Opacity only, 150ms |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | No transition; ring never suppressed |
| Page / route transition | `{motion.duration-base}` 250ms | `{motion.ease-standard}` | `opacity` | Cross-fade at 150ms, no translate |
| Modal or drawer | `{motion.duration-base}` in / `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY` 8px in, 4px out | Fade only, 150ms |
| Dropdown | `{motion.duration-fast}` in / `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY` 4px | Fade only, 150ms |
| Toast | `{motion.duration-base}` in / `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY` 8px | Fade only, 150ms |
| List enter | `{motion.duration-base}`, `{motion.stagger-step}` 40ms apart | `{motion.ease-enter}` | `opacity` + `translateY` 8px | Fade, no stagger, no travel, 150ms |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | Fade at 150ms |
| Accordion chevron | `{motion.duration-fast}` | `{motion.ease-standard}` | `transform: rotate(180deg)` | No rotation; expanded content carries the state |
| Loading | 1200ms infinite | linear | `transform: rotate()` | Static label or stepped opacity pulse at 150ms |
| Hero ambience (declared ambience) | `{motion.duration-emphasis}` 500ms and slower, infinite | `{motion.ease-standard}` | `opacity` + `transform` | Frozen on frame one |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 32 (`REQUIRED_COLOR_ROLES["border"]`) | The `border` patterns are name-based (`hairline`, `border`, `divider`, `rule`, `stroke`, `outline`, `line`). Mercury's boundary tokens are `fog` and `slate`, both documented in the file's own prose as 1px rules and dividers, and both bound to `borderColor` / `rowBorder` / `item-divider` in `components:`. The role is present under another name, so per SPEC section 1 this is a harness bug and I did not add an alias token to satisfy the regex. Cost: `tokens` capped at 4. | Resolve `border` from component usage, not only from the token name: any colour token referenced by a `borderColor`, `rowBorder`, `item-divider` or similar boundary key satisfies the role. That also sends `check_all("border", ...)` at the tone the file really uses as a boundary — which would have caught `fog` at 1.70:1 on the canvas without a human reading the prose. |
| `theme-audit/audit.py` line ~380 | A component with a `textColor` and no `backgroundColor` is assumed to sit on the canvas. In a dual-world file that manufactures failures: four Mercury night components measured 1.14:1 against a light canvas they never touch. | Where the component's `textColor` is theme-scoped (`on-dark`, `on-light`), pick the ground of the matching polarity instead of the default canvas, or skip the check and report it as unmeasurable. The existing `same_theme()` guard already encodes this idea for role pairs but is not applied to the component fallback. |
| `theme-audit/audit.py` lines 156-180 | `rgba()` compositing is applied only to the `colors:` group, never to an inline `rgba()` in a component's `backgroundColor`, which then derefs to `None` and falls back to the canvas. Mercury has five such fills. | Run the same compositing on inline component values. Composite over the component's own ground where one is declared, not over the canvas. |
| `theme-audit/audit.py` line ~320 (`surface_keys`) | Focus coverage only considers tokens whose names match `canvas|background|base|surface|card|panel|tile|band`. Mercury's two dark surfaces are `night` and `night-raised`, so neither was tested for ring coverage; a ring could pass the harness while being invisible on the homepage. I measured both by hand (3.78:1, 3.50:1). | Add surfaces by usage as well as by name: any colour token bound to a component `backgroundColor` is a surface a ring can appear over. |
| `theme-audit/briefs/A35-mercury.md` line 11 | Lists `text-dim` among the missing colour roles. The harness resolves `text-dim` to `ink-secondary`, and did so before any edit of mine. The brief's pre-measured list is out of step with `audit.py`. | Regenerate the briefs from a current `audit.py --json` run, or have `make_briefs.py` read the harness output rather than a stored snapshot. |

### Needs approval

1. **`{colors.fog}` #c3c3cc on `{colors.canvas}` at 1.70:1** (needs 3:1 as a non-text boundary). Extracted and not altered. Nearest passing value: **#8a8a93** (3.01:1) or, staying inside the palette, `{colors.slate}` #70707d at 4.75:1. Usage note that makes the real value defensible: fog is decorative only — it separates accordion rows that are already distinguished by their own text, and it is never the sole boundary of a control nor the only carrier of an error state. Approval needed only if the collection wants a prescribed `hairline-strong` token added; I did not add one, because `{colors.slate}` already does that job in this file and a new token would exist mainly to satisfy the `border` regex.
2. **Tonal elevation at 1.03:1 to 1.14:1** between canvas, surface, surface-tint, lavender and the two night layers. This is Mercury's identity — "depth is almost entirely tonal" — and no step reaches 3:1. Nearest passing value would mean repigmenting the brand's surfaces, so nothing was changed; the limitation is stated in Accessibility and Known Gaps. Approval needed if the collection would rather prescribe a `{colors.slate}` hairline on cards by default.
3. **`{colors.focus}` = #5266eb is prescribed, not extracted.** It reuses Mercury Indigo and clears 3:1 on all six surfaces, so it needs no light/dark pair. If the collection prefers rings to be visually distinct from the action colour, the alternative is #3b4bd1 (6.57:1 on canvas) — but that drops to 2.64:1 on `{colors.night}` and would then require a second `focus-on-dark` token.
4. **`{colors.on-primary}` on `{colors.primary}` at 4.71:1** passes with 0.21 of margin. No change requested; flagged because any future tweak to either value breaks AA.

### Identity verdict

Still unmistakably Mercury. The two surface worlds, the single saturated indigo pill against translucent capsules, the 360–480 weight range and the night nav bracketing light pages all survive untouched; the new motion is opacity-led with 8px of travel at most, which is the same restraint the type and colour already show, and the focus ring is the brand's own indigo rather than a borrowed system blue. Nothing reads as imported from another file in the collection.

**Calm is the right profile.** Rule 1 does not fire (fintech, no full-bleed product photography driving the layout), rule 2 does not fire (marketing site, not a developer tool — the signed-in product is not documented here), and rule 3 does not fire: the palette is 14 tokens but desaturated, saturated colour appears on exactly one interactive element, and the type voice is "quiet, precise", display weight 480, no gradients in the chrome. Rule 4 is the terminal answer, and the file's own words — "calm and confident", "gallery-like pace", "everything around it whispering" — are a direct description of the Calm signature. No switch argued; the roster stands.
