## A80 · webflow

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 5

Harness command: `python3 -I theme-audit/audit.py --site webflow --json`. Note that `audit.py` changed under this run (commit `981bd47`, saturation-based surface election); the before-scores are from the pre-change run and the after-scores from the post-change run. The contrast score is unaffected either way, because both elections are disclosed.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Nothing in the file said motion was prescribed. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section; six measured contrast failures and a failing component binding were entirely undisclosed. |
| P0 | A · Token contract | `colors.focus` | No focus ring token, and no prose anywhere about focus visibility, on a file that documents both white and near-black signature surfaces. |
| P0 | H · States | Components | Only `active` was documented (one `ex-app-shell-row` line). Seven of eight states absent: hover, focus-visible, pressed, disabled, loading, selected, error. |
| P0 | B · Colour | `category-card-orange` | White on `{colors.accent-orange}` `#ff6b00` = 2.86:1, below even the 3:1 large-text threshold its own 32 px type earns. **Genuine brand failure, not a binding error** — see below. |
| P1 | B · Colour | `{colors.hairline}` | 1.43:1 on canvas while bound as the *only* boundary of `text-input` and `button-secondary`. A real WCAG 1.4.11 failure in the live brand, previously unstated. |
| P1 | B · Colour | `{colors.mute}`, `{colors.mute-soft}` | 3.5:1 and 2.3:1 on canvas, both below 4.5:1 for body text. `mute-soft` is the documented placeholder tone and fails at every size. |
| P1 | C · Elevation | Elevation & Depth | Five literal `rgba(...)` shadow stacks in prose with no `shadow:` group, so `{shadow.*}` is unusable. Elevation is otherwise consistent (hairline at Level 1, shadow at 2-4) — border and shadow are not mixed at random. |
| P1 | Section contract | `### Responsive Strategy` | Carried as a Layout subsection, not a top-level `## Responsive Behavior`. Moved verbatim, children promoted one level. |
| P1 | Section contract | Known Gaps | Absent. The file made no distinction between extracted and inferred content. |
| P1 | A · Harness | `surface` role | Role satisfied **wrongly**: the file owns no raised neutral token, so the harness elects a container binding — `{colors.accent-green}` before `981bd47`, `{colors.primary}`/`{colors.ink}` after — and measures light-mode greys against a ground the brand never pairs them with. Shared issue; disclosed locally as manufactured. |
| P2 | E · Borders / radius | Shapes | Radius ladder was internally consistent, but no border-width or ring geometry was stated anywhere. Added as a Border & Ring Ladder subsection. |
| P2 | B · Colour | `{colors.accent-orange}`, `-green`, `-yellow` | 2.86:1, 1.95:1, 1.86:1 as text on canvas. Fill-only tones; the file never said so. |
| P2 | B · Colour | `{colors.accent-red}` | 4.32:1 on canvas — marginally under 4.5:1 for the documented error/validation role. |
| P2 | D · Typography | all roles | Every role already carried size, weight and line height, and body-md at `{colors.body}` measures 12.08:1 on canvas. No change needed. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#080808"`, `focus-on-dark: "#ffffff"` | Required role, absent. Both reuse hexes the palette already owns (`ink`/`primary` and `on-primary`); the file documents white *and* near-black signature surfaces, so one ring cannot serve both (SPEC §1). |
| frontmatter | — -> `motion:` group | Calm profile block from SPEC §4, verbatim, no deviation. |
| Colors › Surface | hairline described as "input borders, card chrome, divider lines" -> scoped to decorative separation, with its 1.43:1 stated; `{colors.mute}` named as the accessible boundary tone | SPEC §2 step 1: the palette already owns a passing tone (3.5:1), so re-scope and add nothing. Frozen `borderColor` bindings untouched. |
| Colors › Focus | — -> new subsection | Documents which existing tones the two rings reuse, so neither reads as a new brand colour. |
| Shapes | — -> `### Border & Ring Ladder` | States the single 1 px stroke weight and the 2 px ring at 2 px outside offset, with ring radius following the control's own radius token. |
| Components › `text-input` | — -> two bullets naming the 1.43:1 boundary and the 2.3:1 placeholder | The failure belongs where someone building the input will read it. |
| Components › `category-card-orange` | — -> paragraph stating the 2.86:1 failure and why it is extracted, not a slip | SPEC §2 step 4. |
| Components | — -> `### Component States` (per-component table + state-treatment table) | Dimension H. Labelled prescribed. All treatments paint-only except modal/dropdown/toast/list travel, per SPEC §6. |
| after Components | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Ten-plus interaction rows, reduced-motion column, `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | — -> `## Accessibility` | Passing pairs, disclosed failures, ring coverage per surface, tap targets (flagged unverifiable), reduced motion. |
| Layout › `### Responsive Strategy` -> `## Responsive Behavior` | moved, heading renamed to the contract name, body byte-identical, `####` children promoted to `###` | SPEC §3 as clarified by `bdf658b`: move, never duplicate; "verbatim" governs the body, not the heading. The computed-not-measured tap-target caveat went to Known Gaps rather than into the moved body. |
| end of file | — -> `## Known Gaps` | Separates extracted from prescribed: no raised surface tone, motion, states, focus ring, shadow tokens, no dark theme, font substitutes, breakpoints/tap targets, and what a document cannot verify. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via the harness's own `contrast()`.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#080808` / `canvas` `#ffffff` | 20.03:1 | 4.5 | Pass |
| `ink-strong` `#222222` / `canvas` | 15.91:1 | 4.5 | Pass |
| `body` `#363636` / `canvas` | 12.08:1 | 4.5 | Pass |
| `body-mid` `#5a5a5a` / `canvas` | 6.9:1 | 4.5 | Pass |
| `mute` `#898989` / `canvas` | 3.5:1 | 4.5 | **Fail** (passes 3.0 as boundary / 24 px+ text) |
| `mute-soft` `#ababab` / `canvas` | 2.3:1 | 4.5 | **Fail** at every size |
| `hairline` `#d8d8d8` / `canvas` | 1.43:1 | 3.0 | **Fail** |
| `on-primary` / `primary` `#080808` | 20.03:1 | 4.5 | Pass |
| `on-primary` / `accent-purple` `#7a3dff` | 5.33:1 | 3.0 (32 px) | Pass |
| `on-primary` / `accent-pink` `#ed52cb` | 3.15:1 | 3.0 (32 px) | Pass |
| `on-primary` / `accent-blue` `#3b89ff` | 3.38:1 | 3.0 (32 px) | Pass |
| `on-primary` / `accent-orange` `#ff6b00` | 2.86:1 | 3.0 (32 px) | **Fail** |
| `primary` / `accent-green` `#00d722` | 10.25:1 | 3.0 (32 px) | Pass |
| `accent-blue-info` `#146ef5` / `canvas` | 4.59:1 | 4.5 | Pass |
| `accent-blue-deep` `#006acc` / `canvas` | 5.34:1 | 4.5 | Pass |
| `accent-red` `#ee1d36` / `canvas` | 4.32:1 | 4.5 | **Marginal fail** |
| `accent-orange` / `canvas` (as text) | 2.86:1 | 4.5 | **Fail** — fill tone only |
| `accent-green` / `canvas` (as text) | 1.95:1 | 4.5 | **Fail** — fill tone only |
| `accent-yellow` `#ffae13` / `canvas` (as text) | 1.86:1 | 4.5 | **Fail** — fill tone only |
| `focus` `#080808` / `canvas` | 20.03:1 | 3.0 | Pass |
| `focus` / `accent-purple` · `-pink` · `-blue` · `-orange` · `-green` | 3.76 · 6.36 · 5.92 · 7.01 · 10.25 | 3.0 | Pass |
| `focus-on-dark` `#ffffff` / `primary` `#080808` | 20.03:1 | 3.0 | Pass |
| Manufactured (surface elected as `primary`/`ink`): `ink-strong` / `ink` | 1.26:1 | 4.5 | Fail — not rendered |
| Manufactured: `body` / `ink` | 1.66:1 | 4.5 | Fail — not rendered |
| Manufactured (surface elected as `accent-green`): `mute-soft` · `hairline` · `mute` / `accent-green` | 1.17 · 1.37 · 1.79 | 4.5 / 3.0 / 4.5 | Fail — not rendered |

Every failure above is now named with its measured ratio in `## Accessibility`; the harness reports 0 undisclosed and 7 disclosed.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, nav-link) | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `background-color`, `border-color` | Unchanged — paint-only |
| Hover (card lift) | `{motion.duration-base}` 250ms | `{motion.ease-standard}` | `box-shadow`, `opacity` | Shadow change only, instant |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `background-color` | Unchanged |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears instantly |
| Page / route transition | 250ms out / 150ms in | `{motion.ease-exit}` / `{motion.ease-enter}` | `opacity` | Cross-fade at `{motion.duration-reduced}` |
| Modal / drawer open | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Fade only, 150ms, no translate |
| Modal / drawer close | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, `transform` | Fade only, 150ms |
| Dropdown open / close | 150ms / 80ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(4px)` | Fade only, 150ms |
| Toast enter / exit | 250ms / 150ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(12px)` | Fade only, 150ms |
| List / card-grid enter | `{motion.duration-base}`, `{motion.stagger-step}` 40ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Fade together, 150ms, stagger 0 |
| List / card-grid exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | Fade at 150ms |
| Loading | 1200ms loop | linear | `transform: rotate`, `opacity` | Static mono caption, loop removed |
| Scroll reveal (secondary bands) | `{motion.duration-emphasis}` 500ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px)` | Renders at final position |

Every exit is shorter than its entrance. The loader is the only infinite animation; the brand carries no ambience. The hero does not animate on first paint.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines ~290-337 (surface election) | The `surface` role is satisfied **wrongly** for any file with no raised neutral token. webflow owns none — light-mode cards are `{colors.canvas}` with a 1 px boundary — so the harness elects a container binding: `{colors.accent-green}` (a 32 px-display category-card fill) before `981bd47`, and `{colors.primary}`/`{colors.ink}` (the polarity-flipped dark card) after. Both then measure light-mode greys against grounds the brand never pairs them with, producing five failures that cannot render, while hiding the real card ground (white). | Where every distinct bound container ground differs from the canvas in *polarity* rather than elevation, treat the file as having no raised surface: set `surface = canvas` (the brand's real card ground) and skip the `*_on_surface` checks, as the existing `else` branch at line ~331 already intends. Equivalently, exclude a bound ground whose polarity differs from the canvas from `distinct_bound`, the way `NOT_A_SURFACE` already excludes hero fills. |
| `theme-audit/audit.py` (`parse_frontmatter`) | `motion:` values are unquoted scalars containing commas and parentheses (`cubic-bezier(0.4, 0, 0.2, 1)`), which parse fine here but only because the parser is line-based. Worth a note in SPEC §4 that the block is to be pasted unquoted. | Documentation only; no code change proposed. |
| `theme-audit/audit.py` (`layout_animation_mentions`) | The `NEGATED` list misses "nothing", so the correct prose "Nothing animates `width`, `height`…" is flagged as a violation while "Never animate …" passes. I reworded my own file to "Never animate"; other agents will hit this. | Add `nothing|none of` to the `NEGATED` alternation. |
| `theme-audit/audit.py` (surface election, again) | The election is not stable across harness revisions, so a file's disclosed-failure list can silently go stale: my first disclosure pass covered the `accent-green` pairs and was invalidated by `981bd47` electing `ink`. I disclose both sets. | Freeze the elected `surface` per site in `roster.json`, or report the election in the table output so agents can see it change. |

### Needs approval

1. **`category-card-orange` — white on `#ff6b00` at 2.86:1.** Verdict: **genuine brand failure, not a binding error.** The evidence: `category-card-green` in the same five-card set deliberately flips its label to `{colors.primary}` ink and the prose says why ("uses ink text for legibility against the lighter green"), so the file's author considered the ink-flip and applied it to exactly one card. White-on-orange is therefore an asserted extracted pairing, not a copy-paste default. It is also the only one of the five that misses: purple 5.33, pink 3.15, blue 3.38, green (ink) 10.25. Left as extracted. Nearest passing value: `{colors.primary}` `#080808` ink text at **7.01:1**, which would make the orange card match the green card's own rule. Usage note that would make the real value defensible: none available — the card's type is already 32 px / weight 500, so the relaxed 3:1 large-text threshold is the one in force and it still misses by 0.14. Darkening the fill to `#e85f00` reaches 3.0:1 with white, but that changes a brand hex and is not proposed.
2. **Re-pointing `text-input.borderColor` and `button-secondary.borderColor`** from `{colors.hairline}` (1.43:1) to `{colors.mute}` (3.5:1). The prose now scopes hairline to decoration and names `mute` as the build-time boundary, but the extracted `components:` bindings are untouched per SPEC §2 step 3. A brand owner must decide whether the shipped product is to change.
3. **`{colors.accent-red}` at 4.32:1** for validation text. Nearest passing value `#e01830` (4.52:1). Usage note: defensible as-is for a 1 px boundary and for 18.66 px+ bold labels; the inline error message itself should be set in `{colors.body}`, which is what the file now prescribes.
4. **`{colors.mute-soft}` as placeholder text at 2.3:1.** No passing value exists in this role without abandoning the tone; nearest passing grey is `#767676` (4.54:1). Documented as a real failure instead.
5. **No `shadow:` group added.** The five elevation levels are multi-offset `rgba(...)` recipes, not single values, so tokenising them is a structural decision about the token format rather than an audit fix.

### Identity verdict

Still unmistakably Webflow. The additions lean on what the file already asserts rather than importing a generic layer: the focus ring is the brand's own `#080808` ink (and its white counterpart for the two polarity-flipped surfaces), not a borrowed blue; the accessible boundary is `{colors.mute}`, a tone the palette already owned, so no token was invented; hover and press are paint-only, because a near-monochrome brand with a 600 weight ceiling and no pill geometry does not pop or bounce; and the state table explicitly forbids accent fills on `selected`, which preserves the file's own central rule that the five chromatic accents are surface fills and never actions.

**Profile: Calm is correct — no switch.** Rule 1 does not fire (a visual development platform is not luxury, automotive, hardware, console or aerospace; the category cards are flat colour fills with no photography at all, which the file says outright). Rule 2 does not fire: Webflow is a design tool, not a terminal, IDE or infra product, and its identity is a white marketing canvas with 80 px display type, not a mono surface. Rule 3 is the one to argue, and it fails on *role*: the palette lists five saturated hexes, but the file's own prose says three times over that they appear as full-card surface fills and never as button backgrounds — every interactive element is near-black or white-on-hairline. The type voice is restrained by rule (weight ceiling 600, negative tracking, "confident but not shouting"), which is the editorial register, not an informal one. Rule 4 is therefore the terminal answer: **Calm**.
