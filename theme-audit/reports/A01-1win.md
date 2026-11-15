## A01 · 1win

Scores before → after (1-5), from the harness:

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 4 | 5 | 3 | 1 | 1 | 2 |
| after | **5** | **5** | **3** | **5** | **5** | **5** |

Contrast stays at 3 deliberately: both remaining failures are extracted values, and
SPEC §2 forbids falsifying a hex to pass. Both are now stated plainly in the file.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No motion information of any kind — no `motion:` group, no section, no reduced-motion rule. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section; the two AA failures below were undocumented, so the file read as if the palette were safe. |
| P0 | B · Colour | `on-primary` on `primary` | White on #00b24b is **2.81:1** (needs 4.5). The brand's highest-visibility control fails AA and the file never said so. |
| P0 | B · Colour | `on-primary` on `secondary` | White on #0075ff is **4.21:1** (needs 4.5). Not caught by the harness (it only checks the `accent` role) but a real failure. |
| P1 | A · Token contract | `colors` | No `focus` role. Repo-wide gap; a focus ring was undefined on a surface where every control sits on near-black. |
| P1 | E · Borders | `hairline` on `canvas` | **1.37:1** — the documented hairline cannot carry a control boundary, yet `text-input`, `pill-outline` and `ex-data-table-cell` all relied on it as their only edge. |
| P1 | H · States | all components | Only default + active/pressed existed. `focus-visible`, `loading` and `error` appeared nowhere in the file. |
| P1 | C · Sections | Responsive Behavior | Content existed but was nested as `### Responsive Strategy` inside Layout, so the required top-level section was absent. |
| P1 | C · Sections | Known Gaps | Absent. The file's inferences (notably the `ex-*` block and the hairline's "translucent" description) were unlabelled. |
| P2 | D · Typography | `faint` on `canvas` | **2.54:1**. Documented for "placeholder text and disabled labels" — fine for disabled, not for live placeholders. Now scoped. |
| P2 | G · Accessibility | `button-primary` | 14px/1.4 type + 8px padding ≈ 36px high, under the 44px target the Responsive section itself asks for. Flagged as a spec, not a measurement. |
| P2 | C · Elevation | `rgba(0,0,0,0.4)` | Expressed consistently (one tonal ladder + one floating shadow) but the shadow is prose-only with no token; no `shadow:` group exists in the contract. Logged as a shared issue. |
| P2 | A · Token contract | `colors.black` | Carries the only accessible accent-label pairing (7.47:1 on green) but matches no role pattern, so the harness cannot see it. Shared issue. |

Dimension C otherwise passes: canvas → surface is 1.39:1, a real but narrow step, and
elevation is expressed one way throughout (tonal ladder, shadow reserved for floating).
Dimension D passes: all six type roles carry size, weight and line height, and body ink
is 16.42:1 / 11.77:1 on the two surfaces. Dimension E's radius ladder (4/6/8/10/12/16/999)
and spacing ladder (2/4/8/12/16/20/24/32) have no outliers.

### Changes made

| Location in file | Before → After | Why |
|---|---|---|
| frontmatter `colors:` | — → `focus: "#4da3ff"` | Required role, absent repo-wide. A lifted step of the brand blue, 7.01:1 on canvas. |
| frontmatter `colors:` | — → `hairline-strong: "#77797d"` | Gives the file a boundary value that actually meets 3:1 without touching the extracted `hairline`. |
| frontmatter, after `spacing:` | — → `motion:` group, 9 keys, Calm profile | SPEC §4/§5. Preceded by a comment stating it is prescribed. |
| Colors › Brand & Accent | `on-primary` bullet → + measured 2.81:1 / 4.21:1 and the two defensible routes | The failure belongs next to the colour, not only in an appendix. |
| Colors › Surface | `hairline` bullet → + 1.37:1 and "decorative edge only"; new `hairline-strong` bullet | Stops the hairline being used as a control boundary. |
| Colors › Text | `faint` bullet → + 2.54:1, scoped to disabled; `black` bullet → + 7.47:1 | Honest limits; surfaces the accessible accent pairing. |
| Colors › **Focus** (new) | — → `focus` spec with the mandatory canvas offset | Ring-on-green is 1.07:1, so the offset is load-bearing and had to be specified. |
| Layout › `### Responsive Strategy` | promoted to `## Responsive Behavior`, children demoted one level | Required section; promotion rather than duplication keeps the diff small. |
| Components › intro note | "No hover states documented." → extraction limit + pointer to the prescribed matrix | The old note would have read as contradicting the new matrix. |
| Components › **Component States** (new) | — → 10-component × 8-state matrix | SPEC §7. `pill-badge` and `footer` are marked genuinely single-state. |
| **## Motion & Animation** (new, after Components) | — → prescribed-first-line, token table, 13-row interaction table, rules, reduced-motion rule | SPEC §4/§6. Transform + opacity only; every exit shorter than its entrance. |
| **## Accessibility** (new) | — → 16-row measured contrast table, per-surface focus-ring table, tap targets, motion, not-verified list | SPEC §3, dimension G. |
| Don'ts | + 3 entries (white-on-green, hairline-as-boundary, motion properties) | Makes the new constraints actionable at the point people read rules. |
| **## Iteration Guide** (new) | — → 4 entries | Optional per SPEC; the two-step ladder and the "change tokens not rows" rule needed saying. |
| **## Known Gaps** (new) | — → 8 entries | Required section. Labels everything prescribed or unverifiable. |

No existing extracted value was altered. No hex was changed.

### Contrast checks

All computed with WCAG 2.1 relative luminance from this file's hexes.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #f0f2f5 / `canvas` #141415 | 16.42:1 | 4.5 | Pass |
| `ink` #f0f2f5 / `surface` #2e3035 | 11.77:1 | 4.5 | Pass |
| `muted` #9aa1b1 / `canvas` #141415 | 7.11:1 | 4.5 | Pass |
| `muted` #9aa1b1 / `surface` #2e3035 | 5.10:1 | 4.5 | Pass |
| `faint` #53575f / `canvas` #141415 | 2.54:1 | 4.5 | **Fail** (scoped to disabled) |
| `faint` #53575f / `surface` #2e3035 | 1.82:1 | 4.5 | **Fail** (scoped to disabled) |
| `on-primary` #ffffff / `primary` #00b24b | 2.81:1 | 4.5 | **Fail** — brand, unchanged |
| `on-primary` #ffffff / `secondary` #0075ff | 4.21:1 | 4.5 | **Fail** — brand, unchanged |
| `black` #000000 / `primary` #00b24b | 7.47:1 | 4.5 | Pass |
| `black` #000000 / `secondary` #0075ff | 4.99:1 | 4.5 | Pass |
| `hairline` #2d2f33 / `canvas` #141415 | 1.37:1 | 3.0 | **Fail** — extracted, unchanged |
| `hairline` #2d2f33 / `surface` #2e3035 | 1.02:1 | 3.0 | **Fail** — extracted, unchanged |
| `hairline-strong` #77797d / `canvas` #141415 | 4.22:1 | 3.0 | Pass |
| `hairline-strong` #77797d / `surface` #2e3035 | 3.03:1 | 3.0 | Pass |
| `focus` #4da3ff / `canvas` #141415 | 7.01:1 | 3.0 | Pass |
| `focus` #4da3ff / `surface` #2e3035 | 5.03:1 | 3.0 | Pass |
| `focus` #4da3ff / `primary` #00b24b | 1.07:1 | 3.0 | **Fail** — hence the mandatory canvas offset |
| `focus` #4da3ff / `secondary` #0075ff | 1.60:1 | 3.0 | **Fail** — hence the mandatory canvas offset |
| `primary` #00b24b / `canvas` #141415 | 6.55:1 | 3.0 | Pass |
| `secondary` #0075ff / `canvas` #141415 | 4.37:1 | 3.0 | Pass |
| `surface` #2e3035 / `canvas` #141415 | 1.39:1 | — | layer step, narrow but real |

### Motion inventory

Calm profile. Every value references the `motion:` token block. Prescribed, not measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity`; `scale(1.02)` on `game-tile` only | Scale removed, opacity kept at 150ms |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `transform: scale(0.98)` | Removed; pressed is colour only |
| Focus-visible | `{motion.duration-instant}` 80ms | `{motion.ease-enter}` | `opacity` | Unchanged |
| Page / route transition | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` | Cross-fade at 150ms, no travel |
| Modal | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scale(0.97→1)`, scrim `opacity` | Scale dropped, fades at 150ms |
| Drawer / mobile betslip | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateY(100%→0)` | Travel dropped, fade at 150ms |
| Dropdown | 150ms in / 80ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(-4px→0)` | Travel dropped, fade only |
| Toast | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px→0)` | Travel dropped, fade only, same dwell |
| List enter | 250ms, stagger `{motion.stagger-step}` 40ms | `{motion.ease-enter}` | `opacity` + `translateY(6px→0)` | Stagger and travel dropped, one 150ms fade |
| List exit | 150ms, no stagger | `{motion.ease-exit}` | `opacity` | Unchanged |
| Loading — tile skeleton | 1200ms infinite | `{motion.ease-standard}` | `opacity` pulse on the `{colors.surface}` placeholder | Frozen mid-opacity, static placeholder |
| Loading — button spinner | 800ms infinite | linear | `transform: rotate()` | Frozen, static indicator + `aria-busy` |
| Reward moment (scoped exception) | `{motion.duration-emphasis}` 600ms | `{motion.ease-enter}` + overshoot to `scale(1.04)` | `opacity` + `transform` | Overshoot removed, value fades at 150ms |

Rule compliance: transform/opacity only; every exit shorter than its entrance;
no first-paint animation (rails render at full opacity, stagger applies only to
client-side list changes); the only infinite loops are the two loaders, and the
file states there is no ambience loop.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` L19-35 (`REQUIRED_COLOR_ROLES`) | No `on-canvas-max` / `on-accent-alt` role, so `colors.black` — the only hex that makes 1win's green CTA pass AA — is invisible to the audit. The harness reports the brand's failure but cannot see its remedy. | Add an optional role `on-accent-alt: [r"^black$", r"^on-accent-alt$", r"^on-primary-alt$"]` and, when present, report the better of the two accent-label ratios alongside the primary one. |
| `theme-audit/audit.py` L136 | `check("on-accent", "accent", ...)` only tests the single `accent` role, so white on `secondary` #0075ff (4.21:1 — a real AA failure on the "Log In" button) is never reported. Any brand with two accents hides one failure. | Also check `on-accent` against every `colors` key matching `^secondary$|^accent-2$|^brand-alt$` when such a key exists. |
| `theme-audit/SPEC.md` §1 | The token contract has no `shadow:` group, yet `rgba(0,0,0,0.4)` is a real elevation value in this file (and in the `feature-card-elevated` / `ex-modal-card` / `ex-toast` entries). It can only live as prose, so it cannot be referenced as `{…}` and cannot be checked. | Add an optional `shadow:` group (`shadow-floating`, `shadow-overlay`) to §1 and resolve `{shadow.*}` in the dangling-reference check. |
| `theme-audit/SPEC.md` §3 | `Iteration Guide` is marked optional, but `audit.py` L104 counts it in `sections_missing`, so a file that legitimately omits it loses a section point. Optional and scored cannot both be true. | Either drop `Iteration Guide` from `SECTIONS` in `audit.py`, or exclude it from the `sections` score: `max(1, 5 - len([s for s in missing if s != "Iteration Guide"]))`. |
| `theme-audit/SPEC.md` §6 | "Animate `transform` and `opacity` only. Never `width`, `height`, …" — a file that quotes this rule verbatim trips the `layout_animation_mentions` regex at `audit.py` L150 and is flagged for animating layout properties. The spec's own wording fails the spec's own check. | Require the negative form to be a separate sentence, or tighten the regex to require an affirmative verb (`transition[s]?\s|animates\s`) rather than any `animat\w*`. |
| `design-md/1win/DESIGN.md` (and, from a spot check, the whole `ex-*` family across the collection) | The ten `ex-*` component entries are identical boilerplate in every file, differing only in which brand tokens they reference. They are honestly labelled "not extracted brand components", but they inflate `components:` and are the one part of this file that reads as borrowed. Not fixed here because the fix is collection-wide. | Move the `ex-*` block to a shared `design-md/_kit/EXAMPLES.md` that files reference by name, so each site's `components:` holds only extracted components. |

### Needs approval

1. **`{colors.on-primary}` #ffffff on `{colors.primary}` #00b24b — 2.81:1, needs 4.5:1.**
   This is 1win's Registration button, the single most important control on the site.
   Hex left untouched (brand identity).
   - Nearest passing value, keeping white: green darkened to **#005021** (9.68:1) — a
     different, much heavier green that no longer reads as the brand.
   - Preferred remedy: keep #00b24b and set the label in `{colors.black}` → **7.47:1**.
   - Usage note that would make the real value defensible: *white on green is used only
     at `{typography.display}` / `{typography.heading}` (33px and 20px at weight 800),
     where the 3:1 large-text threshold applies.* Note this is **still not enough** —
     2.81:1 misses even 3:1. There is no reading under which white-on-#00b24b passes.
     State it as a known brand failure or switch the label colour.

2. **`{colors.on-primary}` #ffffff on `{colors.secondary}` #0075ff — 4.21:1, needs 4.5:1.**
   The "Log In" button and `pill-badge`. Hex untouched.
   - Preferred remedy: `{colors.black}` label → 4.99:1.
   - Usage note that makes the real value defensible: *white on blue is restricted to
     14px+ at weight 700/800 — the only weights this system uses — so the 3:1
     large-text threshold applies and 4.21:1 clears it comfortably.* Given that every
     role in this file is 600 or 800, this is a genuinely defensible note, and the
     cleanest resolution for the blue.

3. **`{colors.hairline}` #2d2f33 on `{colors.canvas}` #141415 — 1.37:1, needs 3.0:1.**
   An extracted decorative value, left untouched.
   - Nearest passing value: **#606266** (3.01:1) or the #77797d added here as
     `hairline-strong` (4.22:1 on canvas, 3.03:1 on surface).
   - Usage note that makes the real value defensible: *this is a decorative tonal
     seam between same-family darks, never the sole boundary of an interactive
     control; every focusable element carries `hairline-strong` or the focus ring.*
     That note is now in the file, so the real hex is defensible as shipped — but
     the harness will keep reporting it, correctly.

4. **`hairline-strong` #77797d is a prescribed value, not an extracted one.** It is
   labelled as such in the file. If 1win ships an accessible input edge, the measured
   hex should replace it.

5. **`focus` #4da3ff is prescribed.** Chosen as a lifted step of the brand blue so the
   ring stays identifiably 1win rather than a generic system blue. If a focus style is
   ever observed on the live site, it supersedes this.

### Identity verdict

Still 1win. The additions are expressed in this brand's own vocabulary rather than
in generic tokens: the focus ring is a lifted step of the same electric blue that
already carries "Log In" and live odds, not a borrowed system blue; the state matrix
is written around `bet-odds-button` suspension, betslip stake validation, rail tile
decode and the `sidebar-rail` green indicator, so it could not be lifted into another
file; and the motion section argues its profile from this file's own observation that
saturation lives in content, not chrome.

**Calm is the right base profile, with one scoped exception.** By SPEC §5's ordering,
rule 1 does not apply (dark canvas, but gaming, not luxury/automotive/hardware),
rule 2 does not apply, and rule 3 — "saturated multi-colour or illustration-led
consumer identity" — is the close call. It does not apply to the *system*: the file's
central argument is that the purples, reds and ambers are game artwork, and the chrome
is monochrome dark plus exactly two signals. Motion dresses the chrome, so rule 4,
Calm, is correct, and short opacity-led fades are what keep a wall of 40+ bright
thumbnails from reading as a slot machine. The exception is the reward moment — win
confirmations, wheel-of-fortune results — where a gambling product genuinely wants
Playful overshoot. That is handled as one explicitly scoped row at
`{motion.duration-emphasis}` rather than by changing the base profile, so nothing
else on the surface inherits it.

The one thing that still reads as borrowed is the `ex-*` example block, which is
identical boilerplate across the collection. It is honestly labelled and references
only brand-native primitives, and fixing it properly is a collection-wide change —
logged under Shared issues.
