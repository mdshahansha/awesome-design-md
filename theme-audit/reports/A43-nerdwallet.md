## A43 · nerdwallet

Scores before -> after (1-5), from the harness: tokens 3 -> 4 · refs 5 -> 5 · contrast 1 -> 5 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 5

`tokens` stops at 4 because the `surface` role still does not resolve. That is deliberate — see Shared issues. No alias token was added to satisfy the pattern.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Nothing in the file said anything about timing. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section. Four frozen tones and four component pairs fail AA and the file disclosed none of them. |
| P0 | A · Token contract | `colors` | No `focus` role. Keyboard focus was entirely undocumented, and one ring cannot serve both the white canvas and the `{colors.primary}` hero band. |
| P0 | B · Colour | `editorial-badge`, `breadcrumb` | Both are described in prose as sitting on the green band, but neither declared a `backgroundColor`, so the harness measured them against the canvas — white-on-white at 1.0:1 and lime-on-white at 1.1:1. The pairs the file actually uses were invisible to measurement. |
| P0 | B · Colour | `{colors.hairline-strong}` | 1.41:1 on canvas, and it is the extracted border of `{button-outline}` — a control whose border is its only affordance. The real brand's outlined button has no perceivable boundary. |
| P1 | H · States | every component entry | The file documented Default and Active only, and said so in one line. Seven of eight states were absent across 30 entries. |
| P1 | C · Section contract | `## Responsive Behavior` | Present only as `### Responsive Strategy` inside Layout, so it read one level below its peers. |
| P1 | C · Section contract | `## Known Gaps` | Absent. A file whose motion, states and focus ring are all prescribed needs it most. |
| P1 | B · Colour | `{colors.hairline}` 1.19:1, `{colors.faint}` 2.1:1, `{colors.info}` 3.0:1 | Three frozen tones below their thresholds with no usage scope written anywhere. |
| P1 | B · Colour | `{marquee-ribbon}` | `{colors.primary}` on `{colors.lime-ribbon}` at 3.36:1 with a 14px bold label. A genuine AA failure on the loudest element in the system. |
| P2 | B · Colour | `{award-ribbon-pill}` 4.45:1, `{badge-compare}` 4.41:1, `{editorial-badge}` 4.41:1 | Three near-misses on 12px and 11px labels, where no large-text exemption applies. |
| P2 | C · Elevation | levels 3 and 4 | Elevation is expressed four different ways — flat, hairline rule, hairline-strong border, then two raw shadow stacks in `rgba()` and `oklab()` with no tokens. Consistent in intent, mixed in expression, and untokenised so `{shadow.*}` cannot be referenced. Left as written; noted in Known Gaps. |
| P2 | D · Typography | all roles | Every role carries size, weight and line height. No gap. Body at weight 300 reads at 10.41:1 on `{colors.canvas}` and 9.72:1 on `{colors.canvas-soft}`, so it is readable on this file's own surfaces. |
| P2 | E · Ladders | `{rounded}`, `{spacing}` | Both ladders are internally consistent; `{spacing.lg}` 20px is the only value off the 8px base, and the file already says the base is 8px with 4px as the half step. No value sits outside its own scale. `{button-outline}`'s `8px 16px` padding is called out in the file as a deliberate break. No change. |
| P2 | D · Typography | Chronicle Display, weights 600/900 | Named in prose with no tokens and no usage. Moved to Known Gaps rather than invented. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | — -> `boundary-strong: "#8e9094"` | SPEC §2: a frozen tone doing a job that needs contrast gets a parallel accessible token rather than being edited. 3.2:1 on canvas. |
| frontmatter `colors` | — -> `focus: "#003d28"` | SPEC §1 requires a focus role. A spruce one step deeper than `{colors.forest}`, so it stays inside the green family. 12.37:1 on canvas. |
| frontmatter `colors` | — -> `focus-on-dark: "#f2ffd6"` | `{colors.focus}` sits at 2.2:1 on `{colors.primary}`. The file documents a saturated green hero band, so SPEC §1's two-ring case applies. 4.64:1 on `{colors.primary}`. |
| frontmatter | — -> `motion:` group, Calm block verbatim | SPEC §4/§5. Values copied literally from the Calm block; nothing tuned. |
| `components.breadcrumb` | no `backgroundColor` -> `"{colors.primary}"` | SPEC §1: declare the ground the prose already states. Turns a bogus 1.0:1 into a real 4.86:1. |
| `components.editorial-badge` | no `backgroundColor` -> `"{colors.primary}"` | Same. Turns a bogus 1.1:1 into the real 4.41:1, which then fails honestly and is disclosed. |
| `## Components` preamble | "documents Default and, where extracted, Active states only" -> same fact, plus an explicit label that every States line below is prescribed, and the file's focus-ring convention | The states had to be added; pretending they were extracted would be a fabricated fact. |
| 30 component entries | — -> a `**States**` line each | SPEC §7. Static surfaces say so explicitly ("static surface — Default only") rather than listing states they do not have. |
| `### Responsive Strategy` (inside Layout) | -> `## Responsive Behavior`, moved verbatim, `####` children promoted to `###` | SPEC §3: move, never duplicate. Body text unchanged. |
| after `## Components` | — -> `## Motion & Animation` | SPEC §3/§6. First line states the system is prescribed and unmeasured. 12-row table, rules, reduced-motion block. |
| after Motion | — -> `## Accessibility` | SPEC §3. 15 passing pairs, nine stated failures, both rings with per-surface ratios, tap targets, reduced motion. |
| `### Surface` in Colors | — -> `### Prescribed (not extracted)` with the three new tokens; `{colors.hairline-strong}` bullet gained its decoration scope | Keeps the prescribed values visibly separate from extracted brand values. |
| `### Don't` | — -> four rules: hairline-strong as a control boundary, focus on green, animated layout properties | The new tokens and the motion rules need enforcement in the same voice as the rest. |
| end of file | — -> `## Known Gaps` | SPEC §3, and the honest home for everything prescribed here. |

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`, never estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #000000 / `canvas` #ffffff | 21.0:1 | 4.5 | Pass |
| `ink` / `canvas-soft` #f7f7f7 | 19.6:1 | 4.5 | Pass |
| `ink` / `mint-50` #effcf8 | 19.95:1 | 4.5 | Pass |
| `ink` / `mint-100` #e3faf2 | 19.22:1 | 4.5 | Pass |
| `body` #3d4045 / `canvas` | 10.41:1 | 4.5 | Pass |
| `body` / `canvas-soft` | 9.72:1 | 4.5 | Pass |
| `muted` #64666a / `canvas` | 5.75:1 | 4.5 | Pass |
| `muted` / `canvas-soft` | 5.37:1 | 4.5 | Pass |
| `faint` #b1b3b5 / `canvas` | 2.1:1 | 4.5 | **Fail** (frozen, disclosed) |
| `on-primary` #ffffff / `primary` #008254 | 4.86:1 | 4.5 | Pass (0.36 headroom) |
| `on-primary` / `primary-deep` #006642 | 7.05:1 | 4.5 | Pass |
| `on-primary` / `forest` #00482f | 10.67:1 | 4.5 | Pass |
| `primary` / `canvas` | 4.86:1 | 4.5 | Pass |
| `primary` / `mint-50` | 4.62:1 | 4.5 | Pass |
| `primary` / `mint-100` (`award-ribbon-pill`) | 4.45:1 | 4.5 | **Fail** (frozen, disclosed) |
| `primary` / `lime-panel` #e8fdac (`badge-compare`) | 4.41:1 | 4.5 | **Fail** (frozen, disclosed) |
| `primary` / `lime-ribbon` #a8ea4c (`marquee-ribbon`) | 3.36:1 | 4.5 | **Fail** (frozen, disclosed) |
| `lime-panel` / `primary` (`editorial-badge`) | 4.41:1 | 4.5 | **Fail** (frozen, disclosed) |
| `on-primary` / `primary` (`breadcrumb`, after declaring the ground) | 4.86:1 | 4.5 | Pass |
| `link` #005fb9 / `canvas` | 6.29:1 | 4.5 | Pass |
| `error` #de2828 / `canvas` | 4.73:1 | 4.5 | Pass |
| `info` #4b99e6 / `canvas` | 3.0:1 | 4.5 | **Fail** (frozen, disclosed) |
| `hairline` #ebebec / `canvas` | 1.19:1 | 3.0 | **Fail** (frozen, disclosed) |
| `hairline-strong` #d8d9da / `canvas` | 1.41:1 | 3.0 | **Fail** (frozen, disclosed) |
| `boundary-strong` #8e9094 / `canvas` | 3.2:1 | 3.0 | Pass (prescribed) |
| `logo-lime` #8dc63f / `canvas` | 2.04:1 | 3.0 | **Fail** (frozen, disclosed; never text) |
| `lime-hero` #9ae600 / `canvas` | 1.53:1 | 3.0 | **Fail** (frozen, disclosed; never on white) |
| `lime-hero` / `forest` | 6.96:1 | 4.5 | Pass (its real ground) |
| `focus` #003d28 / `canvas` | 12.37:1 | 3.0 | Pass |
| `focus` / `canvas-soft` | 11.54:1 | 3.0 | Pass |
| `focus` / `mint-50` | 11.75:1 | 3.0 | Pass |
| `focus` / `mint-100` | 11.32:1 | 3.0 | Pass |
| `focus` / `mint-200` #b7ecda | 9.44:1 | 3.0 | Pass |
| `focus` / `hairline` | 10.38:1 | 3.0 | Pass |
| `focus` / `lime-panel` | 11.23:1 | 3.0 | Pass |
| `focus` / `lime-accent` #ddfa88 | 10.66:1 | 3.0 | Pass |
| `focus` / `lime-ribbon` | 8.56:1 | 3.0 | Pass |
| `focus` / `logo-lime` | 6.05:1 | 3.0 | Pass |
| `focus` / `primary` | 2.2:1 | 3.0 | **Fail** — why `focus-on-dark` exists |
| `focus-on-dark` #f2ffd6 / `primary` | 4.64:1 | 3.0 | Pass |
| `focus-on-dark` / `primary-deep` | 6.73:1 | 3.0 | Pass |
| `focus-on-dark` / `forest` | 10.19:1 | 3.0 | Pass |

Elevation layers, checked for dimension C: `canvas` #ffffff to `canvas-soft` #f7f7f7 is 1.07:1 and `canvas` to `mint-50` #effcf8 is 1.05:1. The layers are **not** distinguishable by luminance — they separate by hue and by area, not by step. That is the documented intent ("almost shadowless… hairlines and pale mint washes rather than elevation") rather than a defect, but it means a greyscale or low-vision rendering collapses the whole mint ladder into the canvas. Stated in the file's Accessibility and Known Gaps sections.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `background-color`, `border-color`, `opacity` | Colour change instant, no fade |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` to 0.92 | Colour only, no dip |
| Focus-visible ring | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` on the ring | Instant at full opacity |
| Page / route transition | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` only | Cross-fade at `{motion.duration-reduced}` |
| Modal | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scale(0.98 → 1)` | Opacity only, no scale |
| Drawer | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `translateX` + `opacity` | Opacity only, appears in place |
| Dropdown | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(-4px → 0)` | Opacity only |
| Toast | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px → 0)` | Opacity only, no travel |
| List enter | `{motion.duration-base}`, `{motion.stagger-step}` 40ms between | `{motion.ease-enter}` | `opacity` + `translateY(6px → 0)` | Together, no stagger, no travel |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` only | Instant removal |
| Loading | `{motion.duration-emphasis}` 500ms loop | `{motion.ease-standard}` | `opacity` pulse; spinner `rotate` | Static block, spinner replaced by a text label |
| `{marquee-ribbon}` ambience | 40s loop, declared ambience | linear | `translateX` | Frozen mid-band |

Every exit is shorter than its entrance. Only `transform` and `opacity` are animated. Entrance travel is capped at 8px — a deep green full-bleed plane and a dense rate table both read badly in motion, which is the one place this file reasons about its own motion rather than copying the profile.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py:22-24` | `REQUIRED_COLOR_ROLES["surface"]` patterns are all anchored to `^surface`, `^card`, `^panel`, `^tile`, `^elevated`, so a brand-named panel surface never resolves. This file's panel surfaces are `mint-50` (bound as `components.section-panel-mint.backgroundColor`), `mint-100` (bound as `components.media-frame-mint.backgroundColor`) and `canvas-soft`. The palette is not missing the role; the patterns miss its naming. | Resolve `surface` from the components block, not the colour-key spelling: take the `backgroundColor` of any component whose own name contains `card`, `panel`, `tile`, `sheet`, `surface` or `well`, and fall back to the first non-`canvas` light fill. Failing that, at minimum unanchor these patterns the way `surface_keys` at line 339 already is. |
| `theme-audit/audit.py:22-24 and :339` | The same script resolves surfaces two different ways in one run: the role check at line 22 is anchored, while the focus-coverage check at line 339 uses an unanchored `re.search(r"(canvas\|background\|base\|surface\|card\|panel\|tile\|band)")`. A file can therefore have surfaces for focus-coverage purposes and no `surface` role at all. | Share one resolver between both call sites. |
| `theme-audit/audit.py:311-316` | The semantic-tone loop is dead code: `if FILL_MARKER.search(key): continue` is followed by the `fails.append(...)` block at the same indentation, so the append is unreachable, and the `ratio` it references is never assigned in that scope. Any semantic tone that is *not* a fill tone is silently skipped. (`info on canvas` did surface in the pre-edit run, so the live behaviour and the code as written disagree — worth a second pair of eyes.) | De-indent the `fails.append(...)` block out of the `if`, and compute `ratio = round(contrast(colors[key], colors[canvas_key]), 2)` before it. |
| `theme-audit/SPEC.md:50` | "`focus` — currently absent from all 84 files" will be stale as soon as these 84 reports land. | Reword to describe the requirement rather than the current repo state. |

### Needs approval

Every item below is a frozen extracted value that fails its threshold. None was changed. Each is disclosed in the file's Accessibility section with its measured ratio.

1. **`{colors.hairline-strong}` #d8d9da as a control boundary — 1.41:1 on canvas, needs 3.0.** It is the extracted border of `{button-outline}` and `{product-card}`. Nearest passing value: **#8e9094 at 3.2:1**, added as the prescribed parallel token `{colors.boundary-strong}` without touching the original. Usage note that makes the real value defensible: `{colors.hairline-strong}` is a card and panel rule only; it may never be the sole boundary of an interactive control. **Approval needed to apply `{colors.boundary-strong}` to `{button-outline}`'s `borderColor` in the frontmatter** — I left the extracted value in place, so the component spec still documents an inaccessible border.
2. **`{colors.hairline}` #ebebec — 1.19:1, needs 3.0.** Nearest passing: #8e9094 at 3.2:1. Usage note: decorative row rule only, never a boundary that carries meaning.
3. **`{colors.faint}` #b1b3b5 — 2.1:1, needs 4.5.** Nearest passing: **#75777b at 4.49:1**. Usage note: de-emphasised metadata that is duplicated elsewhere on the page; never the only carrier of a fact.
4. **`{colors.info}` #4b99e6 — 3.0:1, needs 4.5.** Nearest passing: **#2b79c4 at 4.53:1**. Usage note: defensible as a fill or icon mark, or as text at 18.66px bold / 24px regular and above, where the 3:1 threshold applies.
5. **`{marquee-ribbon}`: `{colors.primary}` on `{colors.lime-ribbon}` — 3.36:1, needs 4.5.** Its label is 14px bold, below the large-text threshold. Nearest passing inside the existing palette: **`{colors.forest}` #00482f at 7.39:1**. Usage note that would defend the real value: none at 14px — this fails AA outright. It would only be defensible if the slogan type were raised to 18.66px bold, where 3:1 applies.
6. **`{editorial-badge}`: `{colors.lime-panel}` on `{colors.primary}` — 4.41:1, needs 4.5.** 11px `{typography.micro}`. Nearest passing: **#f2ffd6 at 4.64:1**, which is the same value I used for `{colors.focus-on-dark}`.
7. **`{award-ribbon-pill}`: `{colors.primary}` on `{colors.mint-100}` — 4.45:1, needs 4.5**, and **`{badge-compare}`: `{colors.primary}` on `{colors.lime-panel}` — 4.41:1.** Both labels are 12px bold `{typography.eyebrow}`, which is not WCAG large text. Nearest passing for both: **`{colors.primary-deep}` #006642 at 6.45:1 and 6.4:1** respectively. Usage note: no exemption applies at 12px; raising either label to 18.66px bold would bring 3:1 into play and both would pass.
8. **`{colors.on-primary}` on `{colors.primary}` at 4.86:1** passes with 0.36 of headroom. Flagged, not failed: any future lightening of the spruce green by one step breaks the primary button.
9. **The three prescribed tokens themselves** — `{colors.focus}` #003d28, `{colors.focus-on-dark}` #f2ffd6, `{colors.boundary-strong}` #8e9094 — are invented values in a document whose purpose is to record real ones. They are labelled prescribed in Colors, Accessibility and Known Gaps, but a brand reviewer should confirm them.

### Identity verdict

The file still reads as NerdWallet. The test I applied: strip the prescribed additions and the original document is unchanged except for two declared `backgroundColor` lines; read the additions on their own and they are still specific to this brand rather than portable.

Three choices carry that. The focus ring is `#003d28`, one spruce step below `{colors.forest}` — the file's own Don'ts forbid introducing a warm accent and say the palette runs green through mint with blue as the only outside hue, so a conventional blue ring would have broken a rule the document states about itself. The dark-surface ring is a pale lime, because the file already explains that the lime tier exists precisely so emphasis can survive on a green ground ("green-on-green would vanish") — the ring reuses the brand's own answer to that problem rather than inventing a second one. And the motion section's only reasoned deviation is the 8px travel cap, justified from this file's content: a full-bleed saturated plane plus dense financial tables.

**Calm is the correct profile and I did not switch it.** Checking the SPEC §5 rules in order: rule 1 does not fire — no luxury, automotive, hardware, console or aerospace identity, and no full-bleed photography with sparse type; editorial photography here is boxed inside `{media-frame-mint}` and explicitly "never full-bleed". Rule 2 does not fire — this is a consumer comparison site, not a developer tool. Rule 3 is the only close call, and it fails on role: the palette lists nine saturated greens and limes, but the file's own test-case language settles it. The limes are static fills — `{expert-tip-panel}`, `{award-ribbon-pill}`, `{badge-compare}` — and `{marquee-ribbon}` is a non-interactive decorative band. Saturated colour on interactive elements is one green, `{colors.primary}`, used soberly. The type voice is weight-300 body against weight-700 headings with uppercase reserved to two roles, and the Don'ts forbid rounding the buttons on the grounds that `{rounded.xs}` is "a deliberate choice against the softness of the illustration style" — a document arguing against its own playfulness. Rule 4 is the terminal answer: Calm.

The one thing I would change if the roster were open: the file's own description calls the system "trustworthy and utilitarian", and the near-square `{rounded.xs}` controls plus the shadowless, ruled layout sit close to the Crisp boundary. What holds it in Calm is the editorial half — the gradient hero band, the serif secondary face, the weight-300 long-form body, and the mint washes used as breathing room. Those are composed-editorial signals, not tool-like ones. Calm stands.
