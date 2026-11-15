## A41 · mongodb

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 3 -> 5 · motion 3 -> 5 · states 1 -> 5

Undisclosed contrast failures went 12 -> 0 (10 now disclosed, 2 were doc defects and were fixed).

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A Tokens | `colors` | No `focus` role at all. The file documents a white page floor *and* deep-teal hero/footer/code surfaces, so one ring cannot serve both — SPEC §1 requires `focus` plus `focus-on-dark` here. |
| P0 | A/B Colour | `components.button-secondary-on-dark` | Declared `backgroundColor: transparent`, so the only measurable pair the file asserted was white-on-white, 1.0:1. The component is only ever drawn on the deep-teal band; the document asserted a pair that cannot render. |
| P0 | A/B Colour | `components.footer-link` | Same defect: `transparent` ground made `{colors.on-dark-muted}` measure 2.13:1 against the white canvas, when it is drawn on the dark footer at 8.06:1. |
| P0 | B Colour | `badge-orange` | White on `{colors.accent-orange}` = 2.86:1 at 13px against 4.5:1. The worst pair in the file, undisclosed. Extracted, so left as observed and now stated. |
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Known Gaps carried a bare "recommend 150–200ms ease" instead. |
| P0 | G A11y | whole file | No `## Accessibility` section; twelve measured failures undisclosed. |
| P1 | B/E Borders | `text-input`, `search-pill` | `{colors.hairline-strong}` at 1.63:1 on canvas is the *only* boundary of a text input. A real defect, not just a decorative tone. |
| P1 | H States | `## Components` | A "no-hover policy" blockquote was being used to suppress state *coverage*, not just hover hexes. `hover`, `focus-visible`, `loading`, `selected` and `error` appeared nowhere, although the file itself describes a focused input, a selected (featured) pricing tier and an active tab. |
| P1 | B Colour | `button-primary-pressed` | Ink on `{colors.primary-pressed}` = 3.93:1, below 4.5:1. Pressed state only, but undisclosed. |
| P1 | B Colour | `hairline`, `hairline-soft`, `hairline-strong`, `muted` | Eight extracted light tones between 1.11:1 and 2.13:1, all undisclosed. |
| P2 | C Elevation | `## Elevation & Depth` | Layer ratios are 1.04–1.08:1; the ladder was documented without saying that luminance alone does not separate the layers and the hairlines carrying the job fail 3:1. Mechanism itself was already consistent (level 0 border, 1–4 shadow). |
| P2 | B Colour | `stone` | 3.46:1 on canvas. The harness never measures it (see Shared issues), so it was invisible; valid for 18px+ labels only. |
| P2 | D Typography | `### Hierarchy` | `caption`, `micro`, `body-md-medium`, `heading-3`/`heading-4` variants exist in frontmatter; the Hierarchy table omits `caption`, `micro` and `body-md-medium`. Every role does carry size, weight and line height, so this is table coverage, not a token gap. Not fixed — outside the diff I was asked for. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| `colors` | added `focus: "#00684a"`, `focus-on-dark: "#00ed64"` | Dimension A. Reuses the brand's own dark green (the hue the file already uses for the focused input border and the active underline tab) and the bright green for dark bands. Not a regex alias: the role was genuinely absent. |
| `colors` | added `hairline-control: "#6b7a88"` (prescribed) | SPEC §2 parallel-accessible-token rule. 4.41:1 on canvas, 4.24:1 on surface; the three extracted hairlines stay as decoration. |
| frontmatter | added `motion:` group, Crisp block verbatim from SPEC §5 | Dimension F. |
| `components.button-secondary-on-dark` | `transparent` -> `{colors.brand-teal-deep}` | Declares the ground the prose already states. Removes an unrenderable 1.0:1 assertion; real pair is 17.2:1. |
| `components.footer-link` | `transparent` -> `{colors.brand-teal-deep}` | Same. Real pair 8.06:1. |
| `components.text-input-focused` | border `{colors.brand-green-dark}` -> `{colors.focus}` | Same hex; routes the focus treatment through the focus role. |
| `components` | added `focus-ring`, `focus-ring-on-dark` | 2px ring, 2px outer offset, pill radius. |
| `## Colors` | added `### Focus` plus a `hairline-control` bullet | States each ring's measured contrast and labels both as prescribed. |
| `## Elevation & Depth` | added layer-separation paragraph | Dimension C: 1.04–1.08:1 stated, mechanism confirmed as non-mixed. |
| `## Components` blockquote | "hover states are NOT documented" -> hover *hex values* are not extracted, state *coverage* is documented | The old wording justified a gap SPEC §7 does not permit. |
| `## Components` | added a 16-row State Matrix + `focus-ring` entries | Dimension H. Marks badges and the layout/band surfaces as genuinely single-state. |
| `## Components` | notes added to `button-primary`, `badge-orange`, `button-secondary-on-dark`, `footer-link`, `text-input` | States each real failure where a reader will act on it. |
| after `## Components` | new `## Motion & Animation` | Dimension F. First line says the system is prescribed, not measured. |
| after that | new `## Accessibility` | Dimension G. |
| `## Known Gaps` | replaced the "recommend 150–200ms" line; added focus-ring and `hairline-control` as prescribed | The old line was an unsourced timing guess. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` / `canvas` | 17.2:1 | 4.5:1 | Pass |
| `ink` / `surface` | 16.56:1 | 4.5:1 | Pass |
| `on-dark` / `brand-teal-deep` | 17.2:1 | 4.5:1 | Pass |
| `on-dark-muted` / `brand-teal-deep` | 8.06:1 | 4.5:1 | Pass |
| `on-primary` / `brand-green` | 10.89:1 | 4.5:1 | Pass |
| `slate` / `canvas` | 8.51:1 | 4.5:1 | Pass |
| `steel` / `canvas` | 5.41:1 | 4.5:1 | Pass |
| `brand-green-dark` / `canvas` | 6.82:1 | 4.5:1 | Pass |
| `on-dark` / `accent-purple` | 5.48:1 | 4.5:1 | Pass |
| `semantic-warning-text` / `semantic-warning-bg` | 4.29:1 | 4.5:1 | Fail (marginal, disclosed) |
| `stone` / `canvas` | 3.46:1 | 4.5:1 | Fail — 18px+ only (disclosed) |
| `button-primary-pressed` ink / `primary-pressed` | 3.93:1 | 4.5:1 | Fail (disclosed) |
| `badge-orange` white / `accent-orange` | 2.86:1 | 4.5:1 | Fail (disclosed) |
| `muted` / `canvas` | 2.13:1 | 4.5:1 | Fail (disclosed) |
| `muted` / `surface` | 2.05:1 | 4.5:1 | Fail (disclosed) |
| `hairline-strong` / `canvas` | 1.63:1 | 3.0:1 | Fail (disclosed) |
| `hairline-strong` / `surface` | 1.57:1 | 3.0:1 | Fail (disclosed) |
| `hairline` / `canvas` | 1.27:1 | 3.0:1 | Fail (disclosed) |
| `hairline` / `surface` | 1.22:1 | 3.0:1 | Fail (disclosed) |
| `hairline-soft` / `canvas` | 1.15:1 | 3.0:1 | Fail (disclosed) |
| `hairline-soft` / `surface` | 1.11:1 | 3.0:1 | Fail (disclosed) |
| `hairline-control` / `canvas` (prescribed) | 4.41:1 | 3.0:1 | Pass |
| `hairline-control` / `surface` (prescribed) | 4.24:1 | 3.0:1 | Pass |
| `focus` / `canvas` | 6.82:1 | 3.0:1 | Pass |
| `focus` / `surface` | 6.56:1 | 3.0:1 | Pass |
| `focus` / `surface-soft` | 6.33:1 | 3.0:1 | Pass |
| `focus` / `surface-feature` | 6.31:1 | 3.0:1 | Pass |
| `focus-on-dark` / `brand-teal-deep` (= `canvas-dark`) | 10.89:1 | 3.0:1 | Pass |
| `focus-on-dark` / `brand-teal` | 7.47:1 | 3.0:1 | Pass |
| `focus-on-dark` / `brand-teal-mid` | 4.32:1 | 3.0:1 | Pass |
| `focus` / `brand-teal-deep` (why a second ring is needed) | 2.52:1 | 3.0:1 | Fail — hence `focus-on-dark` |
| `canvas` / `surface` (layer separation) | 1.04:1 | n/a | Layers not separable by luminance |
| `canvas` / `surface-feature` (layer separation) | 1.08:1 | n/a | Same |
| `hairline-dark` / `brand-teal-deep` | 1.21:1 | 3.0:1 | Fail — reads as a tint; disclosed in the component note |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity` | Colour/opacity at `{motion.duration-reduced}`, no lift |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` | Instant, no scale |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Instant, never suppressed |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | `opacity` | Crossfade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Fade only, no travel |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Fade only |
| Dropdown | `{motion.duration-fast}` / `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px)` | Fade only |
| Toast | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px)` | Fade only |
| List enter | `{motion.duration-base}` + `{motion.stagger-step}` 20ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(6px)` | Fade together, stagger dropped |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | Fade then remove |
| Loading | 900ms loop | linear | `transform: rotate`, `opacity` | Loop frozen, static indicator + label remain |

Exit is shorter than its matching entrance in every row. Only the loader loops; the hero gradient is static, so there is no ambience to freeze.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `README.md` / `CONTRIBUTING.md` (string absent from both) | The "no-hover policy" is cited verbatim in ~10 site files, this one included, and is sourced nowhere in the repo. It suppressed state coverage that SPEC §7 requires. Also reported by A03 and A18. | State in CONTRIBUTING.md that hover *hex extraction* is out of scope for static captures while state *coverage* is mandatory, then sweep the remaining files. |
| `theme-audit/audit.py:197-200` (`find_role_strongest` call for `border`) | The representative `border` token is chosen as the highest-contrast match against the canvas, with no `same_theme` filter. For this file that picks `hairline-dark` (#1c2d38, explicitly "border on dark surfaces") as the light-mode border role, so `check("border","canvas")` passes on a token that never appears on the white canvas. `check_all` happens to catch the real hairlines, so no failure was hidden here — but the resolved role is wrong. | Filter candidates through `same_theme(key, canvas_key)` before picking the strongest. |
| `theme-audit/audit.py:28-32` (`text-dim` patterns) | MongoDB's secondary-text ladder is named `slate` / `steel` / `stone` / `charcoal`. None matches a `text-dim` pattern, so `check_all("text-dim", ...)` never measures them and `stone` at 3.46:1 was invisible. Per the SPEC rule I did **not** add an alias token to make the pattern fire; the palette plainly has the role under its own names. | Either widen the `text-dim` pattern list, or measure every achromatic colour token against the canvas regardless of name and let the file's prose scope it. |
| `theme-audit/audit.py:326-341` (focus coverage loop) | The loop measures every ring against every surface with no `same_theme` filter. Correct for this file (coverage is best-ring-per-surface, and both polarities are covered), but a file with light-only and dark-only rings could be charged for a cross-theme pair. | Low priority; note it before another agent is asked to explain a cross-theme ring failure. |

### Needs approval

1. **`badge-orange`: white on `{colors.accent-orange}` #fa6e39 = 2.86:1** (required 4.5:1; 13px `caption-bold`). Both hexes are extracted and unchanged. No usage note rescues this one — even at 18px+ the 3:1 threshold is missed. Nearest passing options, each needing brand sign-off: keep the orange and swap the label to `{colors.on-primary}` #001e2b (**6.03:1**, no new hue, recommended), or darken the tag fill to #c2410c with white retained (5.18:1, changes a brand accent).
2. **`button-primary-pressed`: ink on `{colors.primary-pressed}` #008c34 = 3.93:1** (required 4.5:1). Defensible usage note: the pressed state is transient and the resting state is 10.89:1, so no information is only available while pressed. Nearest passing with ink retained: #009b3d (4.72:1); with the existing `{colors.brand-green-deep}` #00b545 it is 6.3:1.
3. **`stone` #7c8c9a on canvas = 3.46:1.** Usage note that makes it defensible: 18px+ labels only, where 3:1 applies. Needs confirmation that no 13–16px caption uses it.
4. **`hairline-strong` as the `text-input` boundary = 1.63:1.** I added the prescribed `{colors.hairline-control}` #6b7a88 (4.41:1) alongside and scoped the extracted hairlines to decoration, rather than changing the input's documented border. Approval needed to make `hairline-control` the documented input border.
5. **Both focus tokens and the 2px/2px ring geometry are prescribed**, as is `hairline-control`. MongoDB's real `:focus-visible` treatment was not captured; the values reuse brand hues already in the palette.

### Identity verdict

Still unmistakably MongoDB. The two rings are the brand's own greens rather than a generic blue, the State Matrix is written in the file's own vocabulary (green pill deepens, ink-fill pill tab, green underline tab, mint featured tier), and the press rule explicitly forbids a scale pop because the pill is a brand signature. Nothing was borrowed from another file in the collection; the only new hex is `hairline-control`, a desaturated slate that sits inside the existing grey ladder between `steel` and `stone`.

**Crisp is the right profile** and I kept it. Rule 2 fires on evidence in the file itself: a database product, terminal-aesthetic code mockup cards as the hero's centrepiece, `Source Code Pro` in the type stack, and documentation surfaces. Rule 1 does not fire (no full-bleed photography, no slow reveal). Rule 3 does not fire: the file has many hexes, but the saturated purple/orange/pink/blue appear only as static course-category tags, never on interactive elements, and the display weight is 500 — the SPEC's own test for "not playful".
