## A07 · bmw-m

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 3 | 3 | 1 | 1 |
| After | 5 | 5 | 4 | 5 | 5 | 5 |

Contrast stays at 4: the one remaining failure is `muted` on `surface-card`, an extracted
brand hex that SPEC section 2 forbids changing. It is recorded under Needs approval.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Nothing in the file described timing at all. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. No contrast measured anywhere in the document. |
| P0 | A Tokens | `colors.focus` | No focus token and no focus ring documented. `{component.text-input}` said only "focus state thickens the border to white" — a border change is not a ring and was unmeasured. |
| P0 | B Colour | `colors.hairline` | #3c3c3c measures 1.9:1 on `{colors.canvas}` and 1.58:1 on `{colors.surface-card}`, under the 3.0:1 boundary minimum, while the prose assigned it to card outlines and the `text-input` edge. Confirmed; the harness figure of 1.9:1 reproduces. |
| P1 | B Colour | `colors.muted` | #7e7e7e measures 4.29:1 on `{colors.surface-card}` and 3.73:1 on `{colors.surface-elevated}`, under 4.5:1, yet the prose assigns it to footer links, breadcrumbs and captions with no size qualifier. Confirmed. |
| P1 | H States | every component | Only hover and active appeared in structured Components lines. focus-visible, pressed, disabled, loading, selected and error were absent file-wide. Confirmed. |
| P1 | H States | Iteration Guide item 5 | Said "Never document hover states. Default and Active/Pressed only." — a standing instruction against the state coverage SPEC section 7 requires. |
| P1 | C Elevation | surface ladder | Layers are 1.08:1 / 1.21:1 / 1.15:1 apart. The file presented "Card surface" and "Soft hairline" as alternative elevation treatments with no rule for which applies, so a control could end up bounded by a 1.21:1 tint and nothing else. |
| P2 | B Colour | `colors.m-blue-light`, `colors.electric-blue` | 3.54:1 and 2.92:1 on canvas — fine as stripe and fill, failures as text, and the file never said so. Not harness-flagged (neither matches the signal-colour pattern). |
| P2 | B Colour | `colors.warning`, `colors.success` | White ink on them is 1.85:1 and 3.33:1. The file documented the tones with no ink rule. |
| P2 | A Tokens | `colors.bmw-blue` / `colors.m-blue-dark` | Duplicate hex #1c69d4 under two names; `{colors.hairline-strong}` duplicates `{colors.surface-elevated}` #262626. Both are already explained in the prose, so left as documentation of a real brand overlap, not deduplicated. |
| P2 | D Typography | all roles | Every role carries family, size, weight, line height and tracking. Body (#bbbbbb at 16px/300) is 10.94:1 on canvas and 9.07:1 on card — readable. No defect. |
| P2 | E Shapes | radius ladder | 0 / 2 / 4 / 6 / 9999 is internally consistent, with the binary "0 or circle" rule stated. The new focus ring was given geometry on that scale (square by default, `{rounded.full}` on icon buttons). No defect. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-control: "#767676"` | Parallel accessible boundary token per SPEC section 2; 4.62:1 on canvas, 3.12:1 on the lightest surface. The extracted `hairline` is untouched and scoped to decoration. |
| frontmatter `colors:` | — -> `focus: "#2b7de9"` | Fills the missing `focus` role. `{colors.m-blue-dark}` #1c69d4 lifted in luminance: the heritage hex is 2.90:1 on `surface-elevated` and 2.71:1 on `carbon-gray`, so it cannot serve. Labelled prescribed. |
| frontmatter | — -> `motion:` group, 9 keys | Cinematic profile values per SPEC sections 4–5: base 400ms, slow 600ms, stagger 80ms, long-decelerate curves. |
| Colors → Hairlines | added `hairline-control` entry and a measured paragraph | States the 1.9:1 failure plainly and scopes `hairline` to decoration. |
| Colors → Text → Muted | added measured figures and a usage rule | States the AA failure, gives the surfaces where it passes and the 18px+ large-text route. |
| Colors | — -> new `### Focus` subsection | Documents the ring, its measured contrast on all six surfaces, geometry, and that the tricolor is never a focus ring. |
| Elevation & Depth | added "Measured layer separation" | Records the 1.08–1.39:1 ladder and fixes one elevation expression per element type: bands flat, cards tint-only, controls border-only. Also notes why there is no `shadow:` group. |
| Components → `text-input` | "1px hairline border. Focus state thickens the border to white." -> `hairline-control` edge, focus-visible ring, error border | The input's only edge needed a visible tone, and the state wording was vague. |
| Components | — -> `### Component States` table | 14 rows covering the full ladder, with two-state and single-state components stated as such. Marked prescribed. |
| after Components | — -> `## Motion & Animation` | Required section. First line states it is prescribed and unmeasured. Carries the profile argument, the 11-row inventory, the rules, and the reduced-motion block. |
| after Motion | — -> `## Accessibility` | Required section: 18-row contrast table, focus-ring visibility per surface, tap targets (flagged as unverifiable), reduced motion, and the document's own limits. |
| Iteration Guide item 5 | "Never document hover states…" -> document the full ladder | Removed the standing instruction that contradicted SPEC section 7. |
| Don'ts | added 4 entries | Hairline not as a control edge; stripe not as a focus ring; no layout-property animation; do not speed Cinematic timing up. |
| Known Gaps | animation line rewritten, 2 entries added | Marks motion, focus, `hairline-control` and the state ladder as prescribed rather than extracted. |

### Contrast checks

All computed with WCAG 2.1 relative luminance in python3; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #ffffff / `canvas` #000000 | 21.0:1 | 4.5 | Pass |
| `ink` #ffffff / `surface-card` #1a1a1a | 17.4:1 | 4.5 | Pass |
| `ink` #ffffff / `surface-elevated` #262626 | 15.13:1 | 4.5 | Pass |
| `body` #bbbbbb / `canvas` | 10.94:1 | 4.5 | Pass |
| `body` #bbbbbb / `surface-card` | 9.07:1 | 4.5 | Pass |
| `body-strong` #e6e6e6 / `surface-card` | 13.94:1 | 4.5 | Pass |
| `muted` #7e7e7e / `canvas` | 5.17:1 | 4.5 | Pass |
| `muted` #7e7e7e / `surface-soft` #0d0d0d | 4.79:1 | 4.5 | Pass |
| `muted` #7e7e7e / `surface-card` | 4.29:1 | 4.5 | **Fail** |
| `muted` #7e7e7e / `surface-elevated` | 3.73:1 | 4.5 | **Fail** |
| `muted` #7e7e7e / `carbon-gray` #2b2b2b | 3.49:1 | 4.5 | **Fail** |
| `on-primary` #000000 / `primary` #ffffff | 21.0:1 | 4.5 | Pass |
| `hairline` #3c3c3c / `canvas` | 1.9:1 | 3.0 | **Fail** (scoped to decoration) |
| `hairline` #3c3c3c / `surface-card` | 1.58:1 | 3.0 | **Fail** (scoped to decoration) |
| `hairline-strong` #262626 / `canvas` | 1.39:1 | 3.0 | **Fail** (scoped to decoration) |
| `hairline-control` #767676 / `canvas` | 4.62:1 | 3.0 | Pass |
| `hairline-control` #767676 / `surface-card` | 3.83:1 | 3.0 | Pass |
| `hairline-control` #767676 / `surface-elevated` | 3.33:1 | 3.0 | Pass |
| `hairline-control` #767676 / `carbon-gray` | 3.12:1 | 3.0 | Pass |
| `focus` #2b7de9 / `canvas` | 5.21:1 | 3.0 | Pass |
| `focus` #2b7de9 / `surface-soft` | 4.82:1 | 3.0 | Pass |
| `focus` #2b7de9 / `surface-card` | 4.32:1 | 3.0 | Pass |
| `focus` #2b7de9 / `surface-elevated` | 3.76:1 | 3.0 | Pass |
| `focus` #2b7de9 / `carbon-gray` | 3.51:1 | 3.0 | Pass |
| `focus` #2b7de9 / #ffffff | 4.03:1 | 3.0 | Pass |
| `m-blue-dark` #1c69d4 / `surface-elevated` (rejected ring) | 2.90:1 | 3.0 | Fail — why the ring is lifted |
| `m-red` #e22718 / `canvas` | 4.54:1 | 4.5 | Pass |
| `m-blue-light` #0066b1 / `canvas` | 3.54:1 | 4.5 | **Fail as text** (stripe only) |
| `electric-blue` #0653b6 / `canvas` | 2.92:1 | 4.5 | **Fail as text** (fill only) |
| `success` #0fa336 / `canvas` | 6.31:1 | 4.5 | Pass |
| `warning` #f4b400 / `canvas` | 11.38:1 | 4.5 | Pass |
| #ffffff / `warning` #f4b400 | 1.85:1 | 4.5 | **Fail** — chips take black ink |
| #ffffff / `success` #0fa336 | 3.33:1 | 4.5 | **Fail** — chips take black ink |
| Layers: `canvas` / `surface-soft` | 1.08:1 | — | tint only, never a boundary |
| Layers: `canvas` / `surface-card` | 1.21:1 | — | tint only, never a boundary |
| Layers: `surface-card` / `surface-elevated` | 1.15:1 | — | tint only, never a boundary |
| Layers: `canvas` / `surface-elevated` | 1.39:1 | — | tint only, never a boundary |

### Motion inventory

Profile: **Cinematic**. All values prescribed, none measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, links, tabs) | 240ms | `ease-standard` | opacity, translateX 4px (chevron) | opacity only at 120ms, travel removed |
| Hover (photo cards) | 600ms | `ease-standard` | scale 1 → 1.04 in fixed crop | scale removed; static border brighten |
| Press | 120ms | `ease-exit` | opacity 1 → 0.85 | unchanged |
| Focus ring | 120ms | `ease-standard` | opacity | unchanged; size never animates |
| Page / route transition | 600ms in, 240ms out | `ease-enter` / `ease-exit` | opacity, scale 1.02 → 1 | 120ms cross-fade, no scale |
| Modal / drawer (mobile nav sheet) | 400ms in, 240ms out | `ease-enter` / `ease-exit` | opacity, translateY / translateX | opacity only at 120ms, appears in place |
| Dropdown | 240ms in, 120ms out | `ease-enter` / `ease-exit` | opacity, translateY −8px → 0 | opacity only at 120ms |
| Toast | 400ms in, 240ms out | `ease-enter` / `ease-exit` | opacity, translateY 12px → 0 | opacity only at 120ms |
| List enter | 400ms per item, 80ms stagger, 5 max | `ease-enter` | opacity, translateY 16px → 0 | single 120ms fade, no stagger |
| List exit | 240ms, no stagger | `ease-exit` | opacity, scale 1 → 0.98 | opacity only at 120ms |
| Loading | 900ms cycle, infinite while pending | `ease-standard` | opacity 1 → 0.4 → 1 | frozen at 0.4, status text carries state |

Every exit is shorter than its entrance; transform and opacity only; the loader is the
only infinite animation and the file states there is no brand ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| theme-audit/audit.py, line ~137 (`check("focus", bg, 3.0, ...)` loop over `canvas`, `surface`, `accent`) | The focus ring is checked against the `accent` role, but `accent` resolves by name, not by use. In this file `accent` resolves to `primary` = #ffffff, which is a text colour, not a surface a ring is ever drawn on. The check therefore forces the ring into a narrow luminance window (0.10–0.30) for a surface that does not exist, and in this file ruled out the real heritage blue. | Only run the focus-on-accent check when the accent token is actually used as a component `backgroundColor` in the `components:` block; otherwise skip it. |
| theme-audit/audit.py, line ~128 (`roles["text-dim"]` via `find_role`) | `text-dim` is resolved by `find_role` (first pattern wins) while `border` and `focus` use `find_role_strongest`. So a file that adds a compliant parallel secondary-text token per SPEC section 2 still scores the failure of the frozen one, and the SPEC-sanctioned remedy cannot change the score. | Either apply `find_role_strongest` to `text-dim` as well, or report frozen-tone failures in a separate `frozen_contrast_failures` list that does not reduce the contrast score once the file documents the failure and names a compliant alternative. |
| theme-audit/audit.py, line ~160 (signal-colour loop) | Signal colours are matched on the name prefixes `primary|accent|secondary|brand|cta`. This file's real signal colours are `m-red`, `m-blue-light`, `m-blue-dark` and `electric-blue`, none of which match, so the three text-contrast failures among them were invisible to the harness and had to be found by hand. SPEC section 2 claims every signal colour is checked. | Treat any colour used as a component `backgroundColor`, or named in the file's own prose as an accent, as a signal colour, rather than relying on name prefixes. |
| theme-audit/SPEC.md, lines 45–52 | The `focus` role is required of all 84 files, and section 2 requires 3:1 "against every surface it can appear over", but neither states what to do about full-bleed photography, which has no measurable colour. On a photography-led brand this is the common case. | Add a line: where a focus ring can land on imagery, specify a two-tone ring (brand colour plus a contrasting outer edge) and state that the pair, not a ratio, is the requirement. |

### Needs approval

1. **`{colors.muted}` #7e7e7e on `{colors.surface-card}` #1a1a1a — 4.29:1, needs 4.5:1.**
   Nearest passing value on that surface: **#828282** (4.53:1), or **#8c8c8c** (5.18:1 on
   `surface-card`, 4.50:1 on `surface-elevated`) to clear both card layers. The hex was not
   changed: it is an extracted brand
   tone and SPEC section 2 freezes it.
   Usage note that makes the real value defensible: restrict `{colors.muted}` to
   `{colors.canvas}` and `{colors.surface-soft}`, where it measures 5.17:1 and 4.79:1, or to
   text at 18px+ (or 14px bold) on card surfaces, where the 3:1 large-text threshold applies
   and 4.29:1 clears it. Footer links and breadcrumbs sit on `{colors.canvas}` on the real
   site, so the common case already passes; captions printed on `{component.feature-photo-card}`
   are the exposure. Both routes are now written into the file.
2. **`{colors.m-blue-light}` #0066b1 (3.54:1) and `{colors.electric-blue}` #0653b6 (2.92:1)
   on `{colors.canvas}` fail as text.** Not changed; both are brand hexes. The file now states
   they are stripe and fill only and never type. Nearest passing text equivalents on black
   would be **#0075ca** (4.40:1, still short) → **#007eda** (5.00:1) and **#086ef1** (4.51:1),
   both the same hue lifted in lightness, if either is ever needed as a label.
3. **Prescribed tokens, flagged for sign-off because they are inventions, not extractions:**
   `{colors.focus}` #2b7de9 and `{colors.hairline-control}` #767676. Both are derived from
   tokens already in the file and both are labelled prescribed in the prose and in Known Gaps.

### Identity verdict

The file still reads as BMW M, and the Cinematic assignment is correct — it is the clearest
case in the profile table: true-black canvas plus automotive-luxury identity, SPEC section 5
rule 1, no judgement needed. The useful finding is that Cinematic here cannot mean what it
usually means. This brand has no springs, no gradients, no colour transitions and an explicit
instruction that chrome backs off, so the whole motion budget had to go into two things the
file already named as its own: slow scale on full-bleed photography, and type arriving late
after the image settles. The inventory says so and the Don'ts protect it ("don't speed the
system up to feel sporty"), which is the opposite of what a generic Cinematic block would say
about a performance-car brand.

Two edits were kept deliberately narrow to protect identity. The focus ring is a lifted
`{colors.m-blue-dark}` rather than a neutral white or system blue, so the one new interactive
colour in the file is still a BMW blue — and the prose states twice that the M tricolor is a
mark, never a ring and never a sweep, which is the rule most likely to be broken by someone
implementing motion on this brand. The state table describes states in this system's own terms:
rectangles drop opacity instead of squashing, photo cards scale the image inside a fixed crop
while the card stays put, and `{component.text-link}` has no disabled state because an
unavailable link is removed rather than greyed.

Nothing reads as borrowed from another file in the collection. The one risk is volume: the new
Accessibility and Motion sections are the two longest in the document, which shifts the file's
centre of gravity away from photography and toward compliance tables. The Overview, Colors,
Typography and Shapes sections were left untouched, so the brand argument still comes first.
