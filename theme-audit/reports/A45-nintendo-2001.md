## A45 · nintendo-2001

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

- before: 4 · 5 · 1 · 1 · 1 · 1
- after:  5 · 5 · 5 · 5 · 5 · 5

8 contrast failures remain measured; all 8 are now disclosed with their ratios in `## Accessibility`, and 0 are unresolved. No brand hex was changed.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A (tokens) | `colors.focus` | No focus ring anywhere in the file. The file documents two surface polarities (light periwinkle chrome and the `carbon` command layer), so one ring cannot serve both — `#13275e` sits at 1.09:1 on carbon. Two rings required. |
| P0 | F (motion) | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. |
| P0 | G | whole file | No `## Accessibility` section; eight real contrast failures undisclosed. |
| P0 | B | `button-submit`, `button-icon-arrow`, `button-arrow-chip` | White label/chevron on Signal Orange #f68d1f = 2.40:1, needs 4.5 (and fails 3.0 even read as a non-text glyph). Extracted, frozen. |
| P0 | B | `hero-panel` | White 44px/900 wordmark on `lavender` #acace7 = 2.14:1, needs 3.0. **Genuine failure, not a binding error** — lavender is a real painted field and the wordmark is really white on it. The carbon outline + hard drop shadow carried legibility in 2001 and earn no WCAG credit. Binding left alone. |
| P1 | A (binding) | `dotted-divider` | **Binding error.** The entry declared `backgroundColor: {colors.muted-indigo}` *and* `textColor: {colors.muted-indigo}`, scoring 1.00:1. A 1px dotted rule has no fill and no text; the token is its stroke. Rebound to `borderColor` + `borderStyle: dotted`. On its real ground (`form-panel` platinum) the stroke measures 4.23:1, above the 3:1 a boundary needs. No hex changed. |
| P1 | C (sections) | document order | `Responsive Behavior` existed only as `### Responsive Strategy` inside Layout; `Known Gaps` absent. |
| P1 | H (states) | every component | Only `active`/`pressed` documented. Six states never named: hover, focus-visible, disabled, loading, selected, error. |
| P1 | B | `ink-soft` / `muted-indigo` / `hairline` / `error` on `canvas` | 2.23:1, 1.67:1, 1.79:1, 1.41:1 — all extracted, all now disclosed with scoping prose. |
| P2 | D (typography) | `micro` 10px, `ui-label` 11px | Below a 12px floor and used for real content, not decoration. Recorded in Accessibility, not changed (extracted). |
| P2 | B | `ink` on `canvas` | Passes at 4.55:1 — by 0.05. Any opacity or antialiasing in practice drops it under AA. Recorded in Known Gaps. |
| P2 | A | `sky` / `canvas-soft`, `carbon` / `ink` | Two duplicate-hex pairs. Both names are load-bearing in the prose, so kept and documented in Known Gaps rather than de-duplicated. |
| P2 | C (elevation) | Elevation & Depth | Elevation is expressed one consistent way (bevel polarity, 4 levels, no shadow blur anywhere) and the Don'ts forbid soft shadow. No `shadow:` group is required and none was added — correct per SPEC section 1. |
| P2 | E | radius ladder | 0/2/4/6/10/9999 — monotonic, no value outside its scale. No change. |

Layer separation (dimension C) measured and left alone: `canvas`→`surface` 3.40:1, `canvas`→`platinum` 2.53:1, `canvas`→`periwinkle` 1.32:1, `canvas`→`canvas-soft` 1.78:1. The raised layers are *not* separable by luminance alone, which is the point of the system — separation is carried by the bevel edge line in `chrome-indigo`, not by fill value. Stated in the file's own Elevation section already; no token added.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#13275e"` (Bevel Indigo, prescribed) | Satisfies the missing `focus` role with a real job: 4.17:1 on canvas, 14.19:1 on surface, 5.51–10.55:1 on every other light surface. Chosen as a deeper step of the existing `chrome-indigo` ladder so the ring reads as this brand's bevel line, not a generic blue. |
| frontmatter `colors:` | — -> `focus-on-dark: "#ecab37"` | SPEC section 1 requires a polarity counterpart where a file documents a dark signature surface. `focus` is 1.09:1 on `carbon`, where the nav words, rail buttons and left-rail tabs live. Reuses the extracted amber hex deliberately — amber is already this system's utility-energy colour — so it is a ring with a job, not a regex alias. |
| frontmatter | — -> `motion:` group | Playful block from SPEC section 5, verbatim, no deviations. |
| frontmatter `components.dotted-divider` | `backgroundColor` + `textColor` -> `borderColor` + `borderStyle: dotted` | Binding error: a 1px rule has no paintable surface and no text. The 1.00:1 reading was an artefact of the binding, not a defect in the design. |
| `## Colors` | — -> `### Focus` subsection | Documents both rings, their measured ratios per surface, and the 2px-outside/1px-offset geometry SPEC asks to be stated. |
| `## Components` intro note | "No hover states are documented." -> explicit list of the six states never extracted, plus a pointer that the new ladder is prescribed | Honesty about what is extracted vs prescribed. |
| `## Components` -> `dotted-divider`, `hero-panel` | — -> stroke-vs-fill note; hero failure stated at 2.14:1 | Keeps the fix legible at the point of use. |
| `## Components` | — -> `### Interaction States` table | 11 rows × 8 states, in this file's own bevel/warm-signal vocabulary; marked prescribed, with the two genuinely single-state components named. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and not measured. Plus the era argument, the 14-row table and the reduced-motion rule. |
| after Motion | — -> `## Accessibility` | 18 passing pairs, 8 failures with ratios, per-surface ring table, tap-target note, reduced-motion pointer, hue-only-signal and small-type notes. |
| Layout | `### Responsive Strategy` (with `####` children) -> moved verbatim to top-level `## Responsive Behavior` with children promoted to `###` | SPEC section 3: move, never duplicate. Heading renamed to the contract's own name; content unchanged. |
| end of file | — -> `## Known Gaps` | Ten gaps, all of them things this document cannot know. |

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`, never estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #21242e on `canvas` #7a8aba | 4.55:1 | 4.5 | Pass (by 0.05) |
| `ink` on `surface` #ffffff | 15.48:1 | 4.5 | Pass |
| `ink` on `platinum` #dedede | 11.51:1 | 4.5 | Pass |
| `ink` on `periwinkle` #8ba1d4 | 6.01:1 | 4.5 | Pass |
| `ink` on `canvas-soft` #9fbee7 | 8.10:1 | 4.5 | Pass |
| `ink` on `lavender` #acace7 | 7.23:1 | 4.5 | Pass |
| `ink` on `ice` #c0d5e6 | 10.25:1 | 4.5 | Pass |
| `ink-soft` #3d4f97 on `surface` | 7.60:1 | 4.5 | Pass |
| `ink-soft` on `platinum` | 5.65:1 | 4.5 | Pass |
| `ink-soft` on `canvas` | 2.23:1 | 4.5 | **Fail** (disclosed) |
| `muted-indigo` #60619c on `canvas` | 1.67:1 | 4.5 | **Fail** (disclosed) |
| `muted-indigo` on `platinum` | 4.23:1 | 3.0 | Pass (the divider's real ground) |
| `hairline` #5a5f8c on `canvas` | 1.79:1 | 3.0 | **Fail** (disclosed) |
| `hairline` on `surface` | 6.09:1 | 3.0 | Pass |
| `hairline` on `platinum` | 4.52:1 | 3.0 | Pass |
| `error` #e60012 on `canvas` | 1.41:1 | 4.5 | **Fail** (disclosed) |
| `error` on `surface` | 4.80:1 | 4.5 | Pass |
| `on-primary` #ffffff on `signal` #f68d1f | 2.40:1 | 4.5 | **Fail** (disclosed ×3 components) |
| `carbon` on `signal` | 6.45:1 | 4.5 | Pass (the passing alternative) |
| `on-primary` on `amber` #ecab37 | 2.01:1 | 4.5 | Fail — not used; amber always carries `carbon` text |
| `carbon` on `amber` | 7.70:1 | 4.5 | Pass |
| `on-primary` on `lavender` (`hero-panel`) | 2.14:1 | 3.0 | **Fail** (disclosed) |
| `on-primary` on `systems-teal` #206479 | 6.64:1 | 3.0 | Pass |
| `on-primary` on `games-red` #a7282b | 7.04:1 | 3.0 | Pass |
| `on-primary` on `carbon` #21242e | 15.48:1 | 4.5 | Pass |
| `nav-gold` #e48600 on `carbon` | 5.68:1 | 4.5 | Pass |
| `canvas-soft` on `carbon` | 8.10:1 | 4.5 | Pass |
| `on-primary` on `primary` #e60012 | 4.80:1 | 4.5 | Pass |
| `chrome-indigo` on `canvas` | 2.23:1 | 3.0 | Fail — bevel seam, decorative; same hex as `ink-soft`, disclosed under that name |
| `focus` #13275e on `canvas` | 4.17:1 | 3.0 | Pass |
| `focus` on `surface` | 14.19:1 | 3.0 | Pass |
| `focus` on `platinum` | 10.55:1 | 3.0 | Pass |
| `focus` on `canvas-soft` | 7.43:1 | 3.0 | Pass |
| `focus` on `periwinkle` | 5.51:1 | 3.0 | Pass |
| `focus` on `lavender` | 6.63:1 | 3.0 | Pass |
| `focus` on `ice` | 9.40:1 | 3.0 | Pass |
| `focus` on `amber` | 7.06:1 | 3.0 | Pass |
| `focus` on `signal` | 5.91:1 | 3.0 | Pass |
| `focus` on `nav-gold` | 5.21:1 | 3.0 | Pass |
| `focus` on `carbon` | 1.09:1 | 3.0 | Fail — which is why the second ring exists |
| `focus-on-dark` #ecab37 on `carbon` | 7.70:1 | 3.0 | Pass |
| `focus` vs `focus-on-dark` (ring separation) | 7.06:1 | 3.0 | Pass |
| layer `canvas` -> `surface` | 3.40:1 | — | separable |
| layer `canvas` -> `platinum` | 2.53:1 | — | not separable by fill; bevel carries it |
| layer `canvas` -> `periwinkle` | 1.32:1 | — | not separable by fill; bevel carries it |
| layer `canvas` -> `canvas-soft` | 1.78:1 | — | not separable by fill; bevel carries it |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (chip, nav word, news row) | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` of the bevel highlight | colour/opacity only at `{motion.duration-reduced}`; no travel |
| Press (button, chip, radio) | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `transform: scale(0.97)` | scale removed; fill swaps instantly |
| Focus (ring appears) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the ring | ring appears instantly |
| Page / route transition | `{motion.duration-fast}` | `{motion.ease-exit}` out / `{motion.ease-standard}` in | `opacity` only | opacity settle at `{motion.duration-reduced}` |
| Modal / drawer open | `{motion.duration-base}` 200ms | `{motion.ease-enter}` | `opacity` + `transform: scale(0.96→1)` | opacity only at `{motion.duration-reduced}` |
| Modal / drawer close | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `transform: scale(1→0.98)` | opacity only at `{motion.duration-reduced}` |
| Dropdown open | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(-4px→0)` | opacity only at `{motion.duration-reduced}` |
| Dropdown close | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | unchanged, capped at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px→0)` | opacity only at `{motion.duration-reduced}` |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` | unchanged, capped at `{motion.duration-reduced}` |
| List enter (news rows, tiles) | `{motion.duration-base}`, stagger `{motion.stagger-step}` 60ms | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px→0)` | stagger and travel removed; one shared fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` | unchanged, capped at `{motion.duration-reduced}` |
| Loading (submit chip, skeleton row) | `{motion.duration-emphasis}` 450ms, looping | `{motion.ease-standard}` | `opacity` pulse | loop frozen; static "Loading…" label |
| Hero field (ambience) | none | none | none | none — the motion blur is baked into the photograph |

Every exit is shorter than its entrance. Nothing animates on first paint. The only infinite animation is the loader; there is no brand ambience to freeze.

**Era judgement, stated in the section itself.** In 2001 CSS transitions and keyframes did not exist, so the real page's whole motion vocabulary was the instant JavaScript image-swap rollover, the animated GIF, the full page reload between routes, and a motion blur pre-rendered into a JPEG. Nothing on that page moved under a timing function. So the Playful block is used as a **target**, judged against what the era's own design language implies, not as modern choreography imported wholesale: hover and press sit at the short end (70/130ms) because the era's state change was a single-frame swap; the press scale pop is the honest animation of a drawing that is already a depressible beveled plate; and the route transition gets no choreography at all beyond an opacity settle, because the era's route change was a white flash and a reload. No value deviates from the SPEC block, so this file still reads as a sibling of every other Playful file.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, lines 500–517 (`layout_animation_mentions`) | The negation scan is **per line**: `for line in text.split("\n")` with `line.rfind(".")`. A prohibition that wraps across two source lines is not seen, so the honest sentence "no rule in this file animates `width`, `height`…" was flagged as *animating* width. I reworded my own line to dodge it, but any file with a hard-wrapped prohibition will be falsely flagged. | Run the clause scan over the paragraph, not the line: join soft-wrapped lines (split on blank lines and on `\n` only where the next line starts a list item or heading) before the `NEGATED` lookback. |
| `theme-audit/audit.py`, lines 370–381 (`surface_keys`) | Any component `backgroundColor` that is not already a surface and does not match `ACCENTISH` is treated as a surface a focus ring must clear 3:1. `amber`, `signal` and `nav-gold` are pure signal fills here and reach `surface_keys` only because the brand names its accents by colour rather than by role. The comment above the block says signal fills are deliberately excluded, so this is the intended exclusion missing its cases. | Treat a token as a signal fill when it is referenced as a `backgroundColor` *and* carries light text (`on-*` / white) in a control-shaped component, rather than keyword-matching the token name. |
| `theme-audit/audit.py`, line 459 `disclosed()` | Disclosure matches on `fg_name in line`. A component named `button-icon-arrow` and one named `button-arrow-chip` can both be matched by a single line mentioning either, if their ratios coincide — which they do here (both 2.40:1). The pairs are genuinely distinct and both are documented separately in my file, so no harm here, but the check can credit an undocumented sibling. | Require the component's own name, bounded, in the matching line. |

Nothing in `README.md` or `CONTRIBUTING.md` needed changing.

### Needs approval

Three frozen extracted pairs cannot be fixed without falsifying a brand hex. Each is disclosed in the file; each needs a decision from whoever owns the brand, not from this audit.

1. **White on Signal Orange `#f68d1f` — 2.40:1, needs 4.5** (`button-submit`, `button-icon-arrow`, `button-arrow-chip`).
   - Nearest passing orange for a white label: `#ae6416` (4.53:1). For the 3:1 non-text threshold: `#da7d1b` (3.03:1).
   - Usage note that makes the real value defensible: keep `#f68d1f` and set the label in `{colors.carbon}` instead of white — the same orange measures **6.45:1** with carbon text, so the brand hex survives and the pair passes. For the round and chip arrow glyphs, a carbon chevron passes at 6.45:1 against the identical fill.
2. **White `{typography.display}` on `lavender` `#acace7` — 2.14:1, needs 3.0** (`hero-panel`, Home only).
   - Nearest passing lavender for white large text: `#9090c2` (3.02:1); for the full 4.5 threshold, `#73739a` (4.52:1).
   - Usage note: the 3:1 threshold applies because the wordmark is 44px/900. The defensible alternative that changes no hex is to treat the lavender Home field like the other two heroes — Systems teal passes at 6.64:1 and Games red at 7.04:1 — i.e. darken the *tint behind the photograph*, which is a composition choice, not an identity hex. The carbon outline and drop shadow are not a WCAG remedy and are not claimed as one.
3. **The cool-ink-on-periwinkle family: `ink-soft` 2.23:1, `muted-indigo` 1.67:1, `hairline` 1.79:1, `error` 1.41:1, all against `canvas` `#7a8aba`.**
   - Nearest passing values, if the periwinkle body is ever used as a text ground: `ink-soft` -> `#1b2343` (4.51:1), `muted-indigo` -> `#232339` (4.50:1), `hairline` -> `#3b3e5c` (3.04:1), `error` -> `#520006` (4.53:1).
   - Usage note: none of these is actually drawn on bare canvas in the extracted layout — `ink-soft` and `error` appear on `platinum` (5.65:1) and `surface` (7.60:1/4.80:1); `hairline` borders white and platinum controls (6.09:1, 4.52:1); `muted-indigo` is the `dotted-divider` stroke inside a platinum panel (4.23:1). The defensible position is a scoping rule — *the periwinkle body is a chassis, never a reading surface* — which the file now states. **No parallel accessible border token was added**, because the palette already owns a tone that passes where the hairline does real boundary work; inventing `hairline-strong` here would be a token with no job.
4. **Prescribed, not approved:** `focus: #13275e` and `focus-on-dark: #ecab37` are inventions of this audit, as is the entire state and motion ladder. They are labelled as prescribed throughout, but a brand owner should still sign off on the ring hue.

### Identity verdict

The file still reads unmistakably as Nintendo.com 2001. Every addition is phrased in the document's own vocabulary — the focus ring is "the bevel line drawn one shade harder" in the existing indigo ladder; the states table moves bevel polarity and warm signal rather than introducing a shadow or a tint scale; the motion section's central argument is the depressible beveled plate; and the reduced-motion rendering is, as the file now says, close to what the 2001 page actually did. Nothing in it would suit another site in the collection. The only genuinely generic block is the pre-existing `ex-*` "Examples (illustrative)" group, which is boilerplate shared across the repo and outside this brief's scope; it was left untouched.

**Profile: Playful, as rostered — and it needs an argument, because the ordered assignment rule looks like it should fire Cinematic first.** SPEC section 5 rule 1 names "gaming-console identity", and this is literally a games-console maker's site. But the rules are conjunctions, and rule 1's tell is "full-bleed photography, sparse type and a slow reveal". Only the first of those holds. This file's own prose describes a "dense, modular grid … packed with minimal whitespace", whitespace as "engineered seam, not breathing room", 44px/900 chunky outlined box-art wordmarks, and 10–12px body copy — the opposite of sparse type, and with no reveal of any kind to be slow. Rule 3's conjunction does hold on both halves: saturated colour appears **on interactive elements specifically** (`signal` orange arrow discs and chevron chips, `amber` utility chips, `nav-gold` menu words — the file's own rule is that warm colour means *act here*), and the type voice is informal and character-led (a Mario cutout with a "Welcome to Nintendo.com!" speech bubble in the masthead). That is the Playful test as SPEC states it, passed on saturation *and* role. Playful stands; the Playful block is used verbatim.
