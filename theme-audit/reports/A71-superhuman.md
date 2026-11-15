## A71 · superhuman

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 3 -> 5 · sections 2 -> 5 · motion 1 -> 5 · states 1 -> 5

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F motion | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule. Zero durations or easings anywhere. |
| P0 | G accessibility | whole file | No `## Accessibility` section, so every contrast failure below was undisclosed. |
| P0 | A tokens | `colors` | No `focus` role: the file defined no focus ring on either polarity, and it documents both a white body and indigo/teal signature surfaces. |
| P0 | B contrast | `{colors.hairline}` #e8e4dd | 1.27:1 on `{colors.canvas}` and 1.21:1 on `{colors.canvas-soft}`. It is the only boundary of `text-input`, `card-pricing` and `card-feature-light` — the real brand fails WCAG 1.4.11 at the sole boundary of a text field. Extracted and frozen, so disclosed rather than changed. |
| P1 | B contrast | `{colors.ink-faint}` #9a9794 | 2.91:1 on white, below 4.5:1, while the Colors section describes it as "Tertiary / disabled text" — defensible for disabled, not for tertiary running copy. |
| P1 | B contrast | `{colors.on-dark-faint}` #5a5772 | 2.45:1 on `{colors.primary}`, below 4.5:1 for "Tertiary text on dark". Not measured by the harness (no pattern matches the key). |
| P1 | B contrast | `{colors.hairline-dark}` #3f3a52 | 1.56:1 on `{colors.primary}`, the surface the token is explicitly documented for. Dark-ground dividers fail 3:1. Not measured by the harness. |
| P1 | C elevation | `canvas-soft` vs `canvas` | 1.05:1. The alternating band system is invisible by luminance; separation comes only from position and padding, which the file never states. |
| P1 | C elevation | Elevation & Depth | Elevation is expressed two ways at once — box-shadow levels 1–2 and a 1px hairline on cards — with no rule for which applies where. Recorded in Known Gaps; the extracted evidence does not settle it. |
| P1 | H states | all 17 components | Only `pressed` documented (as a separate component). hover, focus-visible, active, disabled, loading, selected and error named nowhere. |
| P1 | Sections | document order | Missing Motion & Animation, Accessibility and Known Gaps entirely. |
| P1 | A tokens (harness) | `text-dim` role | Harness resolves `text-dim` to `on-dark-mute` (a dark-ground ink) while the file's light-canvas muted inks are `ink-mute` / `ink-faint`. Role satisfied wrongly; see Shared issues. No alias added. |
| P1 | A tokens (harness) | `surface` role | Harness resolves `surface` to `surface-violet-soft`, the hero pill fill and atmospheric wash. The real raised surface is `canvas-soft`. This manufactures the `hairline on surface-violet-soft` pair. See Shared issues. |
| P2 | A/E shapes | `rounded` | Ladder 4/6/8/12/16 is internally consistent; `full` 9999px is scoped to hero CTA and pill tabs only, which the Shapes table states. No value sits outside its scale. No fix needed. |
| P2 | D typography | `body-strong` 18.72px / 700 | The only non-integer size and the only 700 weight in a 460/540/600 system; it is also the only role whose px value looks browser-derived rather than designed. Left as extracted. |
| P2 | B semantics | `colors` | No error/success/warning tone exists and the Don'ts forbid adding one, so the prescribed error state can only use `{colors.primary}` — shape and copy carry validation, with no colour signal. Recorded. |
| P2 | A tokens | `shadow` | Prose states `rgba(0,0,0,0.08)` / `rgba(0,0,0,0.12)` with no `shadow:` group, so no `{shadow.*}` reference is possible. Left alone (no prose reference currently dangles); recorded in Known Gaps. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| `colors:` frontmatter | — -> `focus: "#1b1938"`, `focus-on-dark: "#c9b4fa"` | Fills the `focus` role with two hexes the palette already owns (`primary`, `surface-violet-soft`). Two rings because the file documents both light and dark signature surfaces; no single tone clears 3:1 on #ffffff and #0e3030 at once. |
| frontmatter, after `spacing:` | — -> `motion:` group | SPEC section 4/5 **Crisp** block, verbatim. |
| `## Components`, intro | — -> one paragraph | States that only `pressed` is extracted and that the State rows are prescribed; states the ring geometry once instead of repeating it. |
| `## Components`, 14 entries | — -> a `States:` line per entry | Names default, hover, focus-visible, active/pressed, disabled, loading, selected, error. Static entries (`card-feature-light`, `link-on-light`, `footer-light`, `card-feature-row`) say plainly which states they genuinely do not have. |
| `text-input` | border described as `1px {colors.hairline}` -> same, plus measured 1.27:1, a plain statement that the brand fails AA at the input boundary, and a pointer to `{colors.hairline-dark}` (10.83:1) where a boundary must be perceivable | SPEC section 2 steps 1 and 4. The palette already owns a passing tone, so nothing was added; the frontmatter binding is untouched and re-binding sits under Needs approval. |
| `card-feature-light`, `card-pricing` | border line -> same, plus "extracted; 1.27:1 … decoration rather than a perceivable boundary" | Scopes the frozen tone to decoration in prose without re-pointing it. |
| `button-secondary-outline` | border line -> same, plus 10.83:1 note | Flags the one boundary tone that passes on white. |
| New `## Motion & Animation`, after Components | — -> prescribed-first-line disclaimer, token recap, 12-row interaction table, Motion Rules, `@media (prefers-reduced-motion: reduce)` block | SPEC sections 3, 4, 6. transform/opacity only; exits shorter than entrances; hero ambience declared as ambience. |
| New `## Accessibility`, after Motion | — -> 13-row pass table, 8 disclosed failures with measured ratios, focus-ring geometry and per-surface ratios, tap targets labelled as unverified, reduced motion | SPEC section 2 disclosure and brief dimension G. |
| New `## Known Gaps`, at end after Iteration Guide | — -> 9 items | Required section; records everything prescribed and everything unrenderable. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #292827 / canvas #ffffff | 14.72:1 | 4.5 | Pass |
| ink / canvas-soft #fafaf8 | 14.08:1 | 4.5 | Pass |
| ink / surface-violet-soft #c9b4fa | 7.98:1 | 4.5 | Pass |
| ink-mute #73706d / canvas | 4.92:1 | 4.5 | Pass |
| ink-mute / canvas-soft | 4.71:1 | 4.5 | Pass |
| ink-faint #9a9794 / canvas | 2.91:1 | 4.5 | **Fail** (disclosed) |
| on-primary #ffffff / primary #1b1938 | 16.9:1 | 4.5 | Pass |
| on-primary / surface-teal-deep #0e3030 | 14.15:1 | 4.5 | Pass |
| on-primary / surface-teal-mid #155555 | 8.53:1 | 4.5 | Pass |
| on-dark-mute #bcbac9 / primary | 8.86:1 | 4.5 | Pass |
| on-dark-faint #5a5772 / primary | 2.45:1 | 4.5 | **Fail** (disclosed) |
| primary / surface-violet-soft (hero pill label) | 9.17:1 | 4.5 | Pass |
| hairline #e8e4dd / canvas | 1.27:1 | 3.0 | **Fail** (disclosed, frozen) |
| hairline / canvas-soft | 1.21:1 | 3.0 | **Fail** (disclosed, frozen) |
| hairline / surface-violet-soft | 1.45:1 | 3.0 | **Fail** (disclosed; manufactured pair, see Shared issues) |
| hairline-dark #3f3a52 / canvas | 10.83:1 | 3.0 | Pass |
| hairline-dark / canvas-soft | 10.37:1 | 3.0 | Pass |
| hairline-dark / surface-violet-soft | 5.88:1 | 3.0 | Pass |
| hairline-dark / primary | 1.56:1 | 3.0 | **Fail** (disclosed, frozen) |
| canvas-soft / canvas (layer separation) | 1.05:1 | 3.0 | **Fail** (disclosed; layers not distinguishable) |
| surface-teal-mid / surface-teal-deep | 1.66:1 | 3.0 | **Fail** (disclosed; decorative) |
| focus #1b1938 / canvas | 16.9:1 | 3.0 | Pass |
| focus / canvas-soft | 16.17:1 | 3.0 | Pass |
| focus / surface-violet-soft | 9.17:1 | 3.0 | Pass |
| focus-on-dark #c9b4fa / primary | 9.17:1 | 3.0 | Pass |
| focus-on-dark / surface-teal-deep | 7.68:1 | 3.0 | Pass |
| focus-on-dark / surface-teal-mid | 4.63:1 | 3.0 | Pass |

All ratios computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`; none estimated.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | opacity, background-color | Unchanged (no travel) |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | opacity (no scale) | Unchanged |
| Focus ring appear | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | opacity | No transition |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | opacity | Fade at `{motion.duration-reduced}` 100ms |
| Modal / drawer enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | opacity + translateY 8px → 0 | Travel removed; opacity at 100ms |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | opacity + transform | Travel removed; opacity at 100ms |
| Dropdown | 100ms in / 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity + scaleY 0.98 → 1 | Scale removed; opacity at 100ms |
| Toast | 100ms in / 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity + translateY 6px → 0 | Travel removed; opacity at 100ms |
| List enter | 150ms, `{motion.stagger-step}` 20ms | `{motion.ease-enter}` | opacity + translateY 6px → 0 | Stagger and travel removed; one fade at 100ms |
| List exit | 100ms, no stagger | `{motion.ease-exit}` | opacity | Opacity at 100ms |
| Loading | 1.5s indeterminate loop | `{motion.ease-standard}` | opacity pulse 1 → 0.4 → 1 | Loop frozen; static placeholder at 0.6 |
| Hero atmospheric backdrop (declared ambience) | 20s loop | linear | opacity + scale 1 → 1.02 | Frozen at first frame |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 30-31 (`REQUIRED_COLOR_ROLES["text-dim"]`) | The `^ink-(muted\|subtle\|soft\|tertiary\|secondary\|light\|meta\|note\|caption\|nav\|list\|lead)` pattern does not cover `ink-mute` or `ink-faint`, so this file's light-ground muted inks are invisible to the role; `^on-[a-z]+-mute` then satisfies `text-dim` with `on-dark-mute`, a tone only ever drawn on the indigo. The role reports as satisfied by the wrong token, and `ink-mute` 4.92:1 / `ink-faint` 2.91:1 on white are never measured. Harness bug, per SPEC section 1 — no alias token was added. | Add `mute\|faint` to the `ink-` alternation (`^ink-(mute\|muted\|faint\|subtle\|…)`), and order the `on-[a-z]+-mute` pattern last so a default-theme muted ink wins over a theme-scoped one. |
| `theme-audit/audit.py` line 24-27 (`REQUIRED_COLOR_ROLES["surface"]`) and line 243-245 | The `NOT_A_SURFACE` filter (hero, masthead, display, banner…) runs only in the components-binding fallback, never on a direct pattern match. Here `^surface[-_]` matches `surface-violet-soft` — the hero pill fill and atmospheric wash — so `surface` resolves to a statement fill, hiding the real raised tone `canvas-soft` and manufacturing the `hairline on surface-violet-soft` 1.45:1 pair, which the site never renders. It should pick `canvas-soft` (nearest the canvas, bound as a card background by `card-feature-row`). | Apply the same `NOT_A_SURFACE` test to pattern matches, and when several keys match prefer the one nearest the canvas by contrast — the rule already used in the binding fallback. |
| `theme-audit/audit.py` line 304-310 (`dual_theme`) | `dual_theme` is false here because no key contains both a surface word and `light`/`dark`, yet the file plainly has two polarities (white body, indigo/teal bands). So `hairline-dark` is treated as default-theme and measured only against white (10.83:1, pass), while its documented ground `primary` (1.56:1) is never checked; `on-dark-faint` on `primary` (2.45:1) is likewise unmeasured. | Treat a file as dual-polarity when any `colors` key is bound as a `backgroundColor` whose luminance sits on the far side of 0.2 from the canvas, rather than relying on key names. |

### Needs approval

1. **Re-bind the input and card boundary from `{colors.hairline}` to `{colors.hairline-dark}`.** `{colors.hairline}` #e8e4dd is extracted and frozen at 1.27:1 on white; it is the only boundary of `text-input`, `card-pricing` and `card-feature-light`, so the brand fails WCAG 1.4.11 at a text field. `{colors.hairline-dark}` #3f3a52 is already in the palette and already used on white by `button-secondary-outline`, measuring 10.83:1 — no new token is needed. Nearest passing value if a lighter tone is preferred: **#a3a3a3** (3.03:1 on #ffffff), the lightest warm grey that clears 3:1. The prose now states the failure and points at the passing tone; the frontmatter binding is untouched pending this decision.
2. **Usage note for `{colors.ink-faint}` #9a9794 (2.91:1).** Defensible as written only if scoped to disabled controls (no WCAG minimum) or to 24px+ text where 3:1 applies. Nearest passing value for tertiary body copy at 14–16px: **#767472** (4.51:1 on #ffffff). Approval needed on whether tertiary copy is retired or the tone darkened.
3. **Usage note for `{colors.on-dark-faint}` #5a5772 (2.45:1 on `{colors.primary}`).** Nearest passing value on the indigo: **#8e8aa6** (4.52:1). Currently scoped in the file to disabled and decorative use only.
4. **Dark-ground divider.** `{colors.hairline-dark}` on `{colors.primary}` is 1.56:1. Nearest passing value: **#6d6885** (3.03:1 on #1b1938). The brand may prefer dividers on dark to stay invisible, which is a brand call.
5. **A semantic error tone.** The Don'ts forbid any accent beyond indigo / violet-soft / teal / warm greys, so the prescribed error state uses `{colors.primary}` and copy alone. Adding a red is a brand decision outside this audit.
6. **Both focus rings are prescribed.** `focus` reuses `{colors.primary}` and `focus-on-dark` reuses `{colors.surface-violet-soft}`; neither is a new brand colour, but the brand has never shipped a ring and should confirm the geometry (2px ring, 2px offset, drawn outside the control).

### Identity verdict

Still unmistakably this brand. The additions are expressed in the file's own vocabulary — the indigo/white/teal three-canvas rhythm, the hero pill versus body rounded-rectangle split, the sub-default 460/540/600 weights — and both focus rings reuse existing tones rather than introducing a fourth colour, which the Don'ts forbid. The motion table's 6–8px travel ceiling and "no scale on press" rule were chosen specifically against this file's editorial stillness; a Playful-style squash would have read as a different product.

**On the assigned profile: Crisp is right, but it is a genuine borderline.** The case against it is in the file's own words — "considered, slow-tempo" whitespace, 96–128px section air, half-bleed twilight portraiture, display weight 460, a description that reads "more like a high-end newsletter than a SaaS app" — every one of which is SPEC rule 4's Calm signature. The case for Crisp wins on what the brand sells: a keyboard-driven email client whose entire proposition is speed, which sits squarely in SPEC rule 2's "tool identity". A 250ms Calm base on a product marketed on milliseconds would contradict the pitch, and Crisp's "state change reads as instant; no entrance choreography" is exactly the editorial stillness the marketing pages hold. Kept as rostered; the tension is stated in the file's own Motion & Animation first paragraph so nobody reads the choice as unconsidered.
