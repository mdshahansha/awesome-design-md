## A49 · opencode.ai

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 3 → 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

`3 → 4` on tokens is not a typo: `theme-audit/audit.py` changed under this review (commit `686d9e8`), which added `^mute$` to the `text-dim` patterns. Before that commit the role read as missing and the before-score was 3; re-measuring the untouched file against the current harness gives 4, with only `focus` missing. Both are recorded so the after-score is comparable. The `text-dim` role was **never** satisfied by adding an alias token — the palette already owned `mute` under a brand name, which is the harness-bug case in SPEC section 1, and it has since been fixed upstream. See "Shared issues".

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Zero durations, zero easings. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section. Six real contrast failures were undisclosed, including the one that matters (the only boundary of every form control). |
| P0 | A · Token contract | `colors.focus` | No focus ring token anywhere. The only captured focus appearance is `text-input-focused`'s border swap, which is a colour change indistinguishable from a hover tint and gives keyboard users no indicator on buttons, tabs, links or the TUI. |
| P0 | B · Colour | `hairline` on `surface-soft` | The extracted `rgba(15,0,0,0.12)` composites to 1.31:1 on the input's own fill. `text-input` and `textarea` have no other boundary, so the brand as built ships a 1.31:1 control edge where 3:1 is required. |
| P1 | H · States | every component entry | Only default / active / pressed / disabled documented; hover, focus-visible, loading, selected and error named nowhere. The file attributed this to "system policy", which was really an extraction gap. |
| P1 | B · Colour | `success`, `warning`, `warning-hover`, `danger` on `canvas` | The whole Apple HIG ramp the file ships fails AA at body size on cream: 1.97, 2.01, 3.10, 3.46. `success` and `warning` fail 3:1 as well, so they are not defensible at any text size there. Undisclosed before this pass. |
| P1 | B · Colour | `ash` as the active-tab underline | 2.8:1 on `canvas`, below the 3:1 non-text minimum of 1.4.11, and it is the install strip's *only* selection signal. Not flagged by the harness (`ash` matches no role pattern). |
| P1 | A · Token contract | `focus` on dark surfaces | One ring cannot serve this file: the brand uses one near-black (`#201d1d`) as both its ink and its dark surface, so an ink ring is 1.0:1 on `surface-dark`. A second ring was required, not optional. |
| P2 | B · Colour | `accent` on `canvas` | Apple Blue at 3.92:1 fails 4.5:1 as body text, and 4.17:1 on `surface-dark` where the TUI actually uses it. Not exercised as marketing text (links are ink), so a usage note rather than a defect. |
| P2 | E · Borders | border widths | 1px hairlines and a 2px tab underline were used with no stated ladder; the 2px value sat outside any documented scale. |
| P2 | C · Elevation | `## Elevation & Depth` | Elevation was already expressed one consistent way (rule or fill, never shadow), but the file did not say so, and did not say why it carries no `shadow:` group. |
| P2 | D · Typography | all roles | Clean: every one of the eight roles already carried fontFamily, size, weight, lineHeight and letterSpacing. Body ink measures 16.34 / 15.65 / 14.51:1 on canvas / surface-soft / surface-card. No finding. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#201d1d"`, `focus-on-dark: "#fdfcfc"` | Satisfies the `focus` role with a real job. SPEC section 1's monochrome case: a brand whose accent *is* its ink gets a ring in its own ink and paper, not an invented chromatic one. Two rings because the file documents both polarities. |
| frontmatter | — -> `motion:` group, Crisp block verbatim | SPEC section 4/5. Values are the Crisp block exactly as printed; nothing deviates. |
| `## Colors` | — -> `### Focus` subsection | Documents both rings, their 2px width, their mandatory 2px offset of opposite polarity, and the measured ratio on every ground each is drawn on. First line labels it prescribed. |
| `## Colors` | — -> naming note after the Text ladder | States that `mute` / `stone` / `ash` are this system's secondary-text role under brand names, so the harness's `text-dim` miss is legible from the file itself. |
| `## Elevation & Depth` row 1 | `1px solid {colors.hairline}` -> same, scoped **decorative only**, with the 1.31:1 figure | SPEC section 2: scope the frozen tone to decoration rather than "fixing" an extracted value. |
| `## Elevation & Depth` row 2 | `hairline-strong` -> same, plus "the accessible boundary wherever a rule has to be seen" | The passing tone the file already owns does the control-boundary job, so no `hairline-accessible` token was added. |
| `## Elevation & Depth` | — -> closing paragraph | States that elevation is expressed exactly one way, that there is deliberately no `shadow:` group, and that the focus ring is an outline outside the ladder. |
| `## Shapes` | — -> `### Border Width Scale` | Puts the 2px tab underline and the 2px ring inside a stated two-step ladder where the wider value carries meaning, not weight. |
| `## Components` intro | "No hover states documented per system policy" -> extracted-vs-prescribed note | The old line read as a design decision; it was an extraction gap. |
| `## Components`, all 19 entries | — -> a `- **States:**` line each | SPEC section 7. Each state is marked extracted or prescribed; genuinely single-state components (`badge-news`, `badge-section-label`, `hero-tui-mockup`, `tui-prompt-row`, `testimonial-row`, `button-disabled`) say so and say why. |
| `## Components` / `button-tab` | — -> selection-contrast note | Records the 2.8:1 underline failure and names `hairline-strong` as the substitute. |
| `## Components` / `text-input`, `textarea` | — -> boundary-contrast note | Records the 1.31:1 edge and names the existing passing token. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's identity and was not measured from the live site. Ten-row interaction table, rules, and the `@media (prefers-reduced-motion: reduce)` block. Every value references `{motion.*}`. |
| after that | — -> `## Accessibility` | Measured contrast for every key pair, the real failures stated plainly, focus-ring visibility per surface, tap targets labelled as documented-not-measured, reduced motion, and non-colour state signalling. |
| `## Do's and Don'ts` | +3 Do's, +4 Don'ts | Motion, focus and boundary rules in the brand's own voice. |
| `## Known Gaps` | "Hover states not documented by system policy" -> four honest entries | Hover not captured; motion prescribed; focus ring prescribed; loading/selected/error prescribed. |

Sections sit in SPEC section 3 order: Motion & Animation and Accessibility between Components and Do's and Don'ts. `## Responsive Behavior` was already a top-level heading and was not touched. `## Iteration Guide` is optional and was left verbatim. No prose outside the listed locations was reflowed.

### Contrast checks

All computed with WCAG 2.1 relative luminance from this file's own hexes. `hairline` figures are `rgba(15,0,0,0.12)` composited over the ground it is actually drawn on.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` / `canvas` | 16.34:1 | 4.5:1 | Pass |
| `ink` / `surface-soft` | 15.65:1 | 4.5:1 | Pass |
| `ink` / `surface-card` | 14.51:1 | 4.5:1 | Pass |
| `charcoal` / `canvas` | 13.47:1 | 4.5:1 | Pass |
| `body` / `canvas` | 9.78:1 | 4.5:1 | Pass |
| `mute` / `canvas` | 5.92:1 | 4.5:1 | Pass |
| `stone` / `canvas` | 4.95:1 | 4.5:1 | Pass |
| `on-primary` / `primary` | 16.34:1 | 4.5:1 | Pass |
| `on-dark` / `surface-dark` | 16.34:1 | 4.5:1 | Pass |
| `on-dark-mute` / `surface-dark` | 5.83:1 | 4.5:1 | Pass |
| `on-dark-mute` / `surface-dark-elevated` | 4.81:1 | 4.5:1 | Pass |
| `hairline-strong` / `canvas` | 5.92:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface-soft` | 5.67:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface-card` | 5.25:1 | 3.0:1 | Pass |
| `focus` (#201d1d) / `canvas` | 16.34:1 | 3.0:1 | Pass |
| `focus` / `surface-soft` | 15.65:1 | 3.0:1 | Pass |
| `focus` / `surface-card` | 14.51:1 | 3.0:1 | Pass |
| `focus-on-dark` (#fdfcfc) / `surface-dark` | 16.34:1 | 3.0:1 | Pass |
| `focus-on-dark` / `surface-dark-elevated` | 13.47:1 | 3.0:1 | Pass |
| `focus-on-dark` / `ink-deep` | 20.1:1 | 3.0:1 | Pass |
| `danger-hover` / `canvas` | 5.26:1 | 4.5:1 | Pass |
| `danger-active` / `canvas` | 7.86:1 | 4.5:1 | Pass |
| `accent-hover` / `canvas` | 6.88:1 | 4.5:1 | Pass |
| `success` / `surface-dark` | 8.28:1 | 4.5:1 | Pass |
| `warning` / `surface-dark` | 8.14:1 | 4.5:1 | Pass |
| `danger` / `surface-dark` | 4.72:1 | 4.5:1 | Pass |
| **`hairline` (→#e0dede) / `canvas`** | **1.31:1** | 3.0:1 | **Fail — disclosed, decorative only** |
| **`hairline` (→#dcd9d9) / `surface-soft`** | **1.31:1** | 3.0:1 | **Fail — disclosed; sole boundary of every form control** |
| **`hairline` (→#d6d1d1) / `surface-card`** | **1.31:1** | 3.0:1 | **Fail — disclosed, decorative only** |
| **`ash` / `canvas`** (active-tab underline, non-text) | **2.8:1** | 3.0:1 | **Fail — disclosed** |
| **`accent` / `canvas`** | **3.92:1** | 4.5:1 | **Fail — disclosed; clears 3:1** |
| **`accent` / `surface-dark`** | **4.17:1** | 4.5:1 | **Fail — disclosed; clears 3:1** |
| **`success` / `canvas`** | **1.97:1** | 4.5:1 | **Fail — disclosed; fails 3:1 too** |
| **`warning` / `canvas`** | **2.01:1** | 4.5:1 | **Fail — disclosed; fails 3:1 too** |
| **`warning-hover` / `canvas`** | **3.10:1** | 4.5:1 | **Fail — disclosed; clears 3:1** |
| **`danger` / `canvas`** | **3.46:1** | 4.5:1 | **Fail — disclosed; clears 3:1** |
| `ash` / `surface-card` (`button-disabled`) | 2.49:1 | exempt | Recorded, not corrected |

Harness after: 6 failures, 0 undisclosed. The three additional failures above (`ash` underline, `accent` on both grounds) the harness does not detect — `ash` matches no role pattern and `accent` is not in its SEMANTIC list — and are disclosed anyway.

### Motion inventory

Profile: **Crisp**, Crisp token block used verbatim, no deviation.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `color`, `border-color`, `opacity` | Unchanged — colour-only, no travel to remove |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `background-color`, `opacity` | Unchanged — no scale to remove |
| Focus-visible ring | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | `opacity` on the ring | Appears at full opacity, never delayed |
| Page / route transition | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity` 0 → 1 | Cross-fade at `{motion.duration-reduced}` |
| Modal / mobile drawer | 150ms in, 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateX()` | Travel removed, fade only at 100ms |
| Dropdown | 100ms in, 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-2px → 0)` | Travel removed, fade only at 100ms |
| Toast | 100ms in, 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px → 0)` | Travel removed, fade only at 100ms |
| List enter | 100ms per item, `{motion.stagger-step}` 20ms between | `{motion.ease-enter}` | `opacity` only | Stagger removed, all items fade together at 100ms |
| List exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` only | 100ms fade |
| Loading | `{motion.duration-emphasis}` 300ms per cycle, looping | discrete steps, no interpolation | ASCII glyph substitution `[/]` `[-]` `[\]` `[\|]`, `opacity`; no `transform` | Loop frozen on `[-]`, state carried by `aria-busy` |

Rules satisfied: transform/opacity only; every exit shorter than its entrance; nothing animates on first paint; the only loop is the loading glyph and there is no brand ambience; reduced motion caps at `{motion.duration-reduced}` 100ms. `duration-slow` (220ms) is defined by the profile and deliberately unused — nothing in a terminal-native system earns 220ms.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 28 (`REQUIRED_COLOR_ROLES["text-dim"]`) — **fixed upstream during this review** | The `text-dim` patterns missed this palette's muted ladder: `mute`, `stone` and `ash` matched nothing, so the role reported missing although the file documents it explicitly ("metadata, footer link text", "least-emphasis utility text"). Per SPEC section 1 this was a harness bug, so no alias token was invented. Commit `686d9e8` added `^mute$` and `^mute-`, and the role now resolves to `mute` at 5.92:1. Recorded here because the fix landed mid-review and the before-score reflects the old behaviour. | Done upstream. Remaining suggestion: `stone` (4.95:1) and `ash` (2.8:1) still match no pattern. Adding them would not hide anything — `find_role_strongest` picks the strongest variant for the role name while `check_all` measures every tone, so `ash` would still be reported failing. |
| `theme-audit/audit.py` lines 156-193 (rgba compositing) | An `rgba()` token is composited **once** over the canvas, and that single composite is then measured against every other ground. Hence `hairline on surface-soft` is reported at 1.25:1 (canvas composite `#e0dede` against `#f8f7f7`) when the real composite over that fill is `#dcd9d9` at 1.31:1. The error is small here only because this file's surfaces are within one luminance step of each other; on a file with a dark surface it would invert the result. | Composite per comparison rather than once per token: keep the source `rgba` and alpha alongside the token, and have `check_all` / `check` composite over `colors[bg]` at measurement time. Affects every file in the repo with an rgba token used on more than one ground. |
| `theme-audit/audit.py` line 525 (`disclosed`) | The ±0.06 tolerance is applied with a bare float subtraction, so a stated 1.31 against a computed 1.25 evaluates to 0.06000000000000005 and fails the `<= 0.06` test. A correctly disclosed pair can read as undisclosed on a rounding boundary. | Compare with a small epsilon (`<= 0.0601`) or on integer hundredths: `abs(round(stated*100) - round(f["ratio"]*100)) <= 6`. |
| `theme-audit/audit.py` SEMANTIC list and role patterns | A brand's `accent` is never measured as text on the canvas, and a tone like `ash` that carries a real non-text job (a 2px selection underline) matches no role at all. Both failures here were found by hand, not by the harness. | Add `accent` and its hover/active variants to a 3:1 non-text check against the canvas, and consider measuring any token a component binds as a border or underline colour against its ground. |

No change was needed in `README.md` or `CONTRIBUTING.md`.

### Needs approval

Four brand hexes fail AA and were **not** altered. Each is the stock Apple Human Interface Guidelines tone, so changing one would falsify the document.

| Token | Real value | Measured on `canvas` | Nearest passing value | Usage note that makes the real value defensible |
|---|---|---|---|---|
| `success` | `#30d158` | 1.97:1 | `#1e8638` (4.53:1) for body text; `#25a846` (3.03:1) for large text / non-text | None at body size on cream — it fails 3:1 too. It is defensible **only** on `surface-dark`, where it measures 8.28:1, which is the only place the file documents it being used. Approve either the darkened value for any cream-canvas use, or an explicit prohibition on using it on cream. |
| `warning` | `#ff9f0a` | 2.01:1 | `#a76600` (4.51:1) for body text; `#d28000` (3.00:1) for large text / non-text | Same shape as `success`: 8.14:1 on `surface-dark`, nothing defensible on cream. |
| `warning-hover` | `#cc7f08` | 3.10:1 | `#a56706` (4.51:1) | Clears 3:1, so it is defensible at 18.66px bold / 24px regular and above, or as a non-text indicator. The system's largest non-hero role is 16px, so in practice this means non-text only. |
| `danger` | `#ff3b30` | 3.46:1 | `#ea0c00` (4.51:1) | Clears 3:1, so defensible as a non-text indicator — which is exactly the prescribed use: the 1px error border on `text-input`. The error **message** is prescribed in `danger-hover` (5.26:1), which passes at body size. Approve that split, or approve the darkened hex. |

Also for approval, lower stakes:

- `accent` `#007aff` at 3.92:1 on `canvas` and 4.17:1 on `surface-dark`. Nearest passing for body text is `#0070eb` (4.54:1). The file's own rule keeps Apple Blue out of marketing chrome, so the defensible note is "non-text syntax highlight and 18px+ only". Unchanged.
- `ash` `#9a9898` as the 2px active-tab underline, 2.8:1 against `canvas` where 3:1 is required. No new token was added: `hairline-strong` (5.92:1) already exists and does boundary work, and the `button-tab` entry now names it as the substitute. This needs a yes/no on substituting an existing token for an extracted one in the prescribed guidance, since the extracted value is still recorded.
- `hairline` `rgba(15,0,0,0.12)` at 1.31:1 on all three light grounds. Scoped to decoration; `hairline-strong` named for control boundaries. Same question, same answer — no new token.

### Identity verdict

Still unmistakably OpenCode. The additions were written in the brand's own vocabulary rather than in generic design-system prose: the prescribed loading state is an ASCII spinner glyph cycling `[/]` `[-]` `[\]` `[|]`, the FAQ expanded state is the extracted `+` → `−` marker flip, the copy confirmation reads `[x] copied`, the error prefix is `[x]`, and the focus ring is the brand's own ink and cream because the file's first rule is that marketing chrome has no accent colour. Travel distances were set at 2px and 4px specifically because larger values read as a monospaced grid breaking. Nothing was borrowed from another file in the collection.

The one place the diff pushes against the source is the hover state: this file previously said hover was undocumented "per system policy", and nineteen prescribed hover entries now exist. That is defensible because the gap was an extraction gap rather than a policy, and each entry is labelled prescribed — but a reader who believed the old line will notice the change, so it is called out in Known Gaps as well as in the Components intro.

**Profile: Crisp, confirmed, not switched.** SPEC section 5 rule 2 (terminal / IDE / infra / developer-tool identity) fires on the file's own evidence, and the evidence is unusually strong: every text role is Berkeley Mono, the only visual moment is a static TUI mockup, there is no photography, no gradient and no shadow anywhere, and the file's own voice is "the marketing page is a man page". Rule 1 cannot fire — there is no full-bleed photography and no slow reveal. Rule 3 cannot fire either, despite the file listing a full Apple HIG saturated ramp: those tones appear on no interactive element and the file explicitly forbids them on CTAs, which is precisely the saturation-and-role test SPEC section 5 describes. A terminal responds on the keystroke, so 150ms base with near-linear easing and a 20ms stagger is the only honest reading.
