## A56 · renault

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

Harness command: `python3 -I theme-audit/audit.py --site renault --json`.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A / G | focus role | No focus ring token, no focus prose, no Accessibility section. Every control in the file was unfocusable in documentation terms. Fixed: `focus: "#000000"` (reuses `{colors.ink}`) and `focus-on-dark: "#ffed00"` (reuses `{colors.primary}`), with per-surface ratios stated. |
| P0 | F | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule, zero durations or easings anywhere. Fixed with the Cinematic block verbatim plus a 16-row interaction table and a `@media (prefers-reduced-motion: reduce)` rule. |
| P0 | G | Accessibility | Section absent, so five real contrast failures were undisclosed. Fixed: `## Accessibility` added between Components and Do's and Don'ts, with every measured pair. |
| P0 | B | `{colors.hairline}` `#f2f2f2` | 1.12:1 on `{colors.canvas}`, 1.04:1 on `{colors.surface-soft}` against 3.0:1 required, and the Elevation table listed it as an interchangeable alternative to `{colors.hairline-strong}` for component outlines — i.e. the document authorised a 1.12:1 component boundary. Value frozen; scoped to decoration in prose; Elevation row rewritten so the boundary job belongs to `{colors.hairline-strong}` (21.00:1). **No parallel token added** — the palette already owns the passing tone. |
| P1 | H | 19 component entries | Only `active` and `pressed` were documented anywhere in Components; hover, focus-visible, disabled, loading, selected and error were named nowhere in the file. Fixed: a `States:` line on every entry, with genuinely-two-state components (`badge-new`, `hero-banner`) saying so. |
| P1 | B | `{colors.warning}` `#f0ad4e`, `{colors.success}` `#8dc572` | 1.95:1 and 2.03:1 on `{colors.canvas}` — below even 3.0:1, so unusable as text or boundary at any size. Frozen and disclosed; scoped in prose to fills carrying `{colors.ink}` (10.79:1 and 10.36:1). |
| P1 | B | `{colors.error}` `#be6464` | 4.04:1 on `{colors.canvas}`; the file's own prose puts it on "inline form errors", which are `{typography.body-sm}` 14px/400 — those messages fail AA. Frozen and disclosed with the 18px+/14px-bold usage note. Under Needs approval. |
| P1 | C | Elevation & Depth | Layer separations were never stated and are near-invisible: `canvas`/`surface-soft` 1.07:1, `surface-dark`/`surface-deep` 1.11:1. Added both ratios and a sentence fixing elevation to one mechanism (colour block + outline), since the prose otherwise drifted between outline, colour block and shadow. |
| P2 | B | `{colors.ash}` `#8a8a8a` (3.45:1), `{colors.stone}` `#c4c4c4` (1.74:1), `{colors.divider-dark}` (1.44:1 composited) | Not flagged by the harness (role `text-dim` resolves to the passing `{colors.mute}`), but all three fail as text or boundary. Disclosed with scope: `stone` is disabled-only (WCAG-exempt), `ash` must not carry instruction, `divider-dark` is decorative. |
| P2 | C | Elevation prose | States a shadow (~10% opacity, 2–4px blur) with no exact offset/blur/spread/colour and no `{shadow.*}` reference. No `shadow:` group added — inventing exact values would falsify an extraction. Recorded in Known Gaps. |
| P2 | E | `{rounded.sm}` 3px / `{rounded.md}` 4px | A 0/2/3/4px ladder is three near-identical steps; `sm` and `md` carry no component binding in the frontmatter. Left as extracted — collapsing them would discard an extracted fact — but noted here as the one soft spot in the radius scale. |
| P2 | D | `{typography.subtitle}` 19.2px, `{typography.button-md}` 14.4px | Off-ladder sizes (19.2 = 1.2rem, 14.4 = 0.9rem) sitting between 18 and 20, and 13 and 16. Extracted, so kept verbatim. Every role does carry size, weight and line height; body on every surface this file defines passes 4.5:1 (`{colors.body}` 15.91:1, `{colors.mute}` 5.74:1 on canvas, 5.36:1 on `surface-soft`). |
| P2 | A | harness / brief | The brief lists `text-dim` as a missing role; the harness resolves it to `{colors.mute}` and reports only `focus` missing. The brief's pre-measurement is stale, not the file. No alias token was added. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | (none) -> `focus: "#000000"`, `focus-on-dark: "#ffed00"` | Satisfies the focus role with two values the palette already owns; two rings because the file has two real canvas polarities and no single Renault tone clears 3:1 on both. |
| frontmatter | (no `motion:` group) -> Cinematic block, all ten keys verbatim from SPEC §4 | Required group; profile per roster. No value deviates. |
| `## Colors` → Hairline bullet | "the soft 1px divider between rows" -> same, plus "**Decorative only** — 1.12:1 / 1.04:1 … never the sole boundary of a control" | Scopes a frozen failing tone instead of changing it. |
| `## Colors` → Divider Dark bullet | unchanged text + "Decorative only, at 1.44:1 once composited" | Same reason, dark polarity. |
| `## Colors` | (no focus subsection) -> `### Focus` with both rings, labelled prescribed | States which existing tone each ring reuses, per SPEC §1. |
| `## Elevation & Depth` level-1 row | "1px solid `{colors.hairline-strong}` or `{colors.hairline}`" -> boundary = `hairline-strong`, `hairline` = decorative row rule only | The "or" authorised a 1.12:1 component boundary. |
| `## Elevation & Depth` | (no layer ratios) -> paragraph stating 1.07:1 and 1.11:1 and fixing elevation to one mechanism | Dimension C: layers measured and the mechanism made consistent. |
| `## Components` intro | (none) -> paragraph marking default and `button-primary-pressed` as extracted and all other states as prescribed | Keeps the state rows from reading as extracted facts. |
| `## Components`, 19 entries | no states -> a `States:` line per entry naming default, hover, focus-visible, active/pressed, disabled, loading, selected, error, or saying plainly which do not exist | SPEC §7. |
| after `## Components` | (nothing) -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. 16 rows covering hover (two kinds), press, focus, page transition, hero reveal, modal/drawer open and close, dropdown open and close, toast enter and exit, list enter and exit, and two loaders; `transform`/`opacity` only; every exit shorter than its entrance; `@media (prefers-reduced-motion: reduce)` block naming what is removed, kept and frozen. |
| after Motion | (nothing) -> `## Accessibility` | 14 passing pairs, 8 disclosed failures, the focus-ring table per surface, non-colour cues, declared tap targets, reduced motion. |
| `## Known Gaps` | 4 items -> 9 | Adds prescribed-motion, prescribed-states, prescribed-focus, absent shadow tokens, and the uncaptured-mid-grey risk to the ring pair. |

Section order after the edit: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Motion & Animation, Accessibility, Do's and Don'ts, Responsive Behavior, Iteration Guide, Known Gaps — matching SPEC §3. Responsive Behavior was already top-level, so nothing was moved. No section was reflowed.

### Contrast checks

All computed with WCAG 2.1 relative luminance via a stdlib `python3 -I` snippet; `rgba()` tones composited over their stated ground first.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #000000 / `canvas` #ffffff | 21.00:1 | 4.5 | Pass |
| `ink` / `surface-soft` #f7f7f7 | 19.60:1 | 4.5 | Pass |
| `body` #222222 / `canvas` | 15.91:1 | 4.5 | Pass |
| `charcoal` #333333 / `canvas` | 12.63:1 | 4.5 | Pass |
| `mute` #666666 / `canvas` (text-dim role) | 5.74:1 | 4.5 | Pass |
| `mute` / `surface-soft` | 5.36:1 | 4.5 | Pass |
| `ash` #8a8a8a / `canvas` | 3.45:1 | 4.5 | Fail — disclosed, scoped to placeholder/disabled |
| `stone` #c4c4c4 / `canvas` | 1.74:1 | 4.5 | Fail — disclosed, disabled-only (WCAG-exempt) |
| `on-dark` #ffffff / `surface-dark` #000000 | 21.00:1 | 4.5 | Pass |
| `on-dark` / `surface-deep` #111111 | 18.88:1 | 4.5 | Pass |
| `on-dark-mute` → #b8b8b8 / `surface-dark` | 10.59:1 | 4.5 | Pass |
| `on-primary` #000000 / `primary` #ffed00 | 17.37:1 | 4.5 | Pass |
| `on-primary` / `primary-deep` #e6d200 | 13.58:1 | 4.5 | Pass |
| `hairline-strong` #000000 / `canvas` (border role) | 21.00:1 | 3.0 | Pass |
| `hairline` #f2f2f2 / `canvas` | 1.12:1 | 3.0 | Fail — frozen, disclosed, scoped to decoration |
| `hairline` / `surface-soft` | 1.04:1 | 3.0 | Fail — frozen, disclosed |
| `divider-dark` → #292929 / `surface-dark` | 1.44:1 | 3.0 | Fail — frozen, disclosed, decoration |
| `error` #be6464 / `canvas` | 4.04:1 | 4.5 | Fail — frozen, disclosed; clears 3.0 for 18px+/14px-bold and borders |
| `warning` #f0ad4e / `canvas` | 1.95:1 | 4.5 | Fail — frozen, disclosed; fill-only tone |
| `success` #8dc572 / `canvas` | 2.03:1 | 4.5 | Fail — frozen, disclosed; fill-only tone |
| `info` #337ab7 / `canvas` | 4.56:1 | 4.5 | Pass (no margin) |
| `link` #0000ee / `canvas` | 9.40:1 | 4.5 | Pass |
| `ink` / `warning` #f0ad4e (fill usage) | 10.79:1 | 4.5 | Pass |
| `ink` / `success` #8dc572 (fill usage) | 10.36:1 | 4.5 | Pass |
| `focus` #000000 / `canvas` | 21.00:1 | 3.0 | Pass |
| `focus` / `surface-soft` | 19.60:1 | 3.0 | Pass |
| `focus` / `primary` #ffed00 tile | 17.37:1 | 3.0 | Pass |
| `focus-on-dark` #ffed00 / `surface-dark` | 17.37:1 | 3.0 | Pass |
| `focus-on-dark` / `surface-deep` | 15.62:1 | 3.0 | Pass |
| `focus-on-dark` / `canvas` (never drawn there) | 1.21:1 | n/a | Out of scope by design — stated in the file; the two rings are one system, each covering one polarity |
| `canvas` / `surface-soft` (layer separation) | 1.07:1 | n/a | Tonal hint, not a boundary — stated in Elevation |
| `surface-dark` / `surface-deep` (layer separation) | 1.11:1 | n/a | Tonal hint, not a boundary — stated in Elevation |

Harness after the edit: 0 undisclosed failures, 5 disclosed.

### Motion inventory

Cinematic profile, all values from SPEC §4 verbatim. Prescribed, not measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, pill, nav item) | 240ms `duration-fast` | `ease-standard` | `opacity`, underline `scaleX` | Colour swaps instantly; no growth, no scale |
| Hover (photography) | 600ms `duration-slow` | `ease-standard` | `transform: scale(1→1.03)` in a fixed frame | Scale removed |
| Press / active | 120ms `duration-instant` | `ease-standard` | `transform: scale(0.98)` (0.96 icons, 0.995 tiles) | Scale removed; pressed fill applies untransitioned |
| Focus-visible | 120ms `duration-instant` | `ease-standard` | ring `opacity` only | Appears instantly; never suppressed |
| Page / route transition | 400ms out / 600ms in | `ease-exit` / `ease-enter` | `opacity`, `translateY(16px→0)` | Cross-fade at 150ms; no travel |
| Hero band reveal (signature) | 900ms `duration-emphasis`, type +80ms | `ease-enter` | photo `scale(1.06→1)` + `opacity` | Opacity only at 150ms; no scale, no stagger; content never gated |
| Modal / drawer open | 400ms `duration-base` | `ease-enter` | `opacity`, `translateY(24px→0)` / `translateX(100%→0)` | Fade at 150ms; placed with no travel |
| Modal / drawer close | 240ms `duration-fast` | `ease-exit` | `opacity`, reverse transform | Fade at 150ms |
| Dropdown open | 240ms `duration-fast` | `ease-enter` | `opacity`, `translateY(-8px→0)` | Fade at 150ms |
| Dropdown close | 120ms `duration-instant` | `ease-exit` | `opacity` | Fade at 150ms |
| Toast enter | 400ms `duration-base` | `ease-enter` | `opacity`, `translateY(16px→0)` | Fade at 150ms; dismiss timing unchanged |
| Toast exit | 240ms `duration-fast` | `ease-exit` | `opacity`, `translateY(0→8px)` | Fade at 150ms |
| List enter | 400ms per item, 80ms `stagger-step`, capped at 6 | `ease-enter` | `opacity`, `translateY(12px→0)` | All together at 150ms; stagger and travel removed |
| List exit | 240ms, no stagger | `ease-exit` | `opacity` | Fade at 150ms |
| Loading (indeterminate bar) | 900ms loop, infinite while pending | `ease-standard` | `translateX` of a 2px `primary` bar — never `width` | Travel frozen; static bar pulses opacity at 150ms |
| Loading (skeleton) | 900ms loop, infinite while pending | `ease-standard` | `opacity` pulse on `surface-soft` blocks | Pulse held at 150ms; no sweep |

Only the two loaders are infinite. The R5 / E-TECH atmospheric gradients are documented as static images, explicitly not ambience, so there is no ambience to freeze.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/briefs/A56-renault.md` line 12 | Lists `text-dim` as a missing colour role. The harness resolves `text-dim` to `{colors.mute}` (5.74:1 on canvas) and reports only `focus` missing, so the brief's pre-measurement is one harness revision stale. Acting on it would have meant inventing an alias token, which SPEC §1 forbids. | Regenerate the briefs from the current `audit.py` output, or add the harness revision to each brief header so a stale pre-measurement is visible as stale. |
| `theme-audit/audit.py` lines 254-263 | Ref resolution accepts `{component.x}` by pluralising the group name (`grp + "s"`), so this file's 7 `{component.*}` references resolve while the frontmatter group is `components:`. The repo is therefore inconsistent across files with no harness signal. | Keep accepting both, but emit a `ref_style` field naming the non-canonical form so a later pass can normalise the repo to `{components.x}` without a scoring change. |
| `theme-audit/audit.py` line 603 | The layout-animation `NEGATED` list includes bare `no` and `not`, so a sentence like "loading bar animates translateX, not width" clears the check. The intent is right but a file could also evade it by phrasing a genuine `width` animation with any nearby negation. | Require the negation to govern the animated property (same clause, before the property token) rather than appearing anywhere in the clause. |
| `theme-audit/audit.py` lines 556-575 | Disclosure matches on the foreground token name appearing anywhere on a line that states the ratio. A single Accessibility row mentioning two tones can disclose a pair it never measured. | Require the row to state both tones (or both hexes) of the pair it discloses. |

### Needs approval

1. **`{colors.error}` `#be6464` on `{colors.canvas}` — 4.04:1, needs 4.5:1.** The file's own prose puts this tone on inline form error messages, which are set in `{typography.body-sm}` (14px / 400), so those messages fail AA by a small margin. Nearest passing value: **`#b15d5d` (4.57:1)**, a barely perceptible darkening of the same hue. Usage note that makes the real value defensible if the hex is kept: restrict `#be6464` to text at 18px+ or 14px bold (3.0:1 applies) and to the non-text error border on `{component.text-input}`, and set inline messages in `{colors.body}` with a `{colors.error}` icon and border carrying the signal. The hex was **not** changed.
2. **`{colors.warning}` `#f0ad4e` (1.95:1) and `{colors.success}` `#8dc572` (2.03:1) on `{colors.canvas}`.** Both miss 3.0:1 as well, so no text size rescues them. Nearest passing values: `#976d31` (4.62:1) and `#5c804a` (4.52:1) — both are visibly different colours, which is why they are a brand-owner decision rather than a fix. Interim scope now written into the file: use each only as a fill behind `{colors.ink}` (10.79:1 and 10.36:1). Hexes **not** changed.
3. **Re-binding the frozen `{colors.hairline}` in `components:`.** `configurator-row` and `nav-bar` still declare `{colors.hairline}` exactly as extracted (1.12:1 on canvas). Those bindings are facts about the real site and were left untouched; the prose now scopes the tone to decoration. If a brand owner wants the implemented product to differ, the change is `configurator-row` separator and `nav-bar` bottom border → `{colors.stone}` or `{colors.hairline-strong}`. Needs an owner's yes, because it would make the document describe something other than the live site.
4. **Two focus rings, both prescribed.** `{colors.focus}` = `#000000` and `{colors.focus-on-dark}` = `#ffed00` reuse existing palette values and introduce no new colour, but Renault has published no focus treatment that was captured here. A brand owner should confirm the 2px / 2px-offset geometry and the yellow-on-black choice (yellow is otherwise reserved for primary CTAs, so a focus ring in yellow slightly widens that reservation).
5. **Tap targets below 44px.** `{component.button-icon-square}` declares 40px and `{component.button-pill}` 36px (40px on mobile). Both are extracted values. Raising them to 44px is a product change, not a documentation fix, so the file states the shortfall rather than rewriting the heights.

### Identity verdict

Still unmistakably Renault. The yellow is still the only accent and still scarce; corners are still 2px or square; NouvelR is still the only family; the white → black → yellow band rhythm still drives the document. The two additions that could have genericised it did not: the focus rings are the brand's own ink and its own Sunlight Yellow rather than the default blue every other design system reaches for, and the motion section is argued from this brand's evidence — weighted, no overshoot, no spring, no elastic — which is the same discipline that already forbade a secondary accent and a decorative italic. The one place the file now reads more like a system than a brand is the per-component `States:` lines, which are necessarily prescribed and so carry less Renault-specific texture than the extracted prose around them; they are marked as prescribed for exactly that reason.

**Cinematic is the right profile.** Assignment rule 1 fires on identity alone — automotive — and the file's own content corroborates it rather than merely permitting it: full-bleed vehicle photography as the primary content type, `lineHeight: 0.95` display type at weight 700, "photography-first automotive" in the description, an atmospheric mesh-gradient hero band, and square-cornered imagery with copy stacked beneath rather than overlaid. The white default canvas is not a counter-argument; SPEC §5 rule 1 says so explicitly. The only tension is that the brand is self-described mass-market dealership rather than luxury, which might argue for Calm's shorter 250ms base. I keep Cinematic: rule 1 is keyed on automotive identity, not on price position, and cross-file comparability with the other automotive files (bmw, ferrari, tesla, lamborghini) matters more than a half-step of tempo. No switch was made.
