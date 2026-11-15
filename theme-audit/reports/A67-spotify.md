## A67 · spotify

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 1 | 5 |
| refs | 1 | 5 |
| contrast | 1 | 5 |
| sections | 1 | 5 |
| motion | 1 | 5 |
| states | 1 | 1 |

The before-row is 1 across the board because this was one of the ten legacy files: no frontmatter token block, numbered headings. The refs and contrast 1s are floors, not findings — with no frontmatter there was nothing to resolve and nothing to measure, so neither score described the file. The states 1 survives the conversion, and that is a real result: see Findings H and Known Gaps.

### Findings

19 findings: **5 P0, 8 P1, 6 P2.**

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | J / A | whole file | No frontmatter token block at all. 0 of 8 colour roles resolved, 0 of 12 required sections recognised, every `{group.token}` reference impossible. The file was entirely unmeasurable. |
| P0 | B / G | `input-search` focus | The source's one extracted focus treatment is "border becomes `#000000`, outline `1px solid`" on a `#1f1f1f` field: **1.27:1**. A sighted keyboard user gets no visible focus indicator on Spotify's primary search control. Real brand failure, disclosed, frozen. |
| P0 | F | motion | No `motion:` group and no `## Motion & Animation` section. The source contains no duration, easing curve, transition or choreography of any kind. |
| P0 | G | accessibility | No `## Accessibility` section. No ratio had ever been computed against this file's own 22 hexes. |
| P0 | J | headings | All twelve required sections absent under the numbered variant (`## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide`). |
| P1 | A | `focus` role | No focus token, and no focus treatment documented for any control except the search input (which fails). |
| P1 | B / E | `border` `#4d4d4d` | The source names Border Gray "button borders on dark" and it clears 3:1 on **no surface in the file**: 2.22:1 on canvas, 2.10:1 on surface, 1.95:1 on the exact `#1f1f1f` fill the dark pills use, 1.77:1 on `#272727`. Frozen; re-scoped to decoration in prose. |
| P1 | H | every component | Five of eight states undocumented for every component. Press, disabled, loading and selected appear nowhere in the file for any control; `error` exists only as `--text-negative`, never bound. Nothing to extract and nothing invented. |
| P1 | C | elevation ladder | Elevation is expressed two incompatible ways: levels 0–1 are background steps with no shadow, levels 2–3 are shadows with no stated background. The two halves never pair. |
| P1 | C | charcoal layers | Adjacent layers are 1.03:1 to 1.25:1 apart (`canvas`/`surface` 1.06:1; `surface-card`/`surface-card-alt` 1.03:1). Not WCAG pairs, but not reliable layer boundaries either — a card's edge depends entirely on shadow, radius and album art. |
| P1 | A | `shadow:` group | Three real shadow values in prose (`rgba(0,0,0,0.5) 0px 8px 24px`, `rgba(0,0,0,0.3) 0px 8px 8px`, the inset border combo) with no token to reference them by. Added. |
| P1 | I | motion profile | Rostered **Cinematic**; the file's own evidence gives **Calm**. Switched, argued in the file and below. Not switched silently. |
| P1 | G | tap targets | No height, width or icon-box dimension for any control anywhere in the file. The 44×44px minimum can be neither confirmed nor failed; stated as such rather than claimed either way. |
| P2 | E | spacing ladder | Four component paddings sit outside the 1px–20px scale: 36px and 43px (asymmetric pill insets), 48px and 96px (search input, icon-aware). Recorded as stated, not snapped. |
| P2 | E | radius ladder | 100px, 500px and 9999px are three spellings of one "full pill" intent, and `10px–20px` is a range with no canonical value. Kept as stated; explained in Shapes. |
| P2 | D | typography | `lineHeight: normal` for nine of fourteen roles and `letterSpacing: normal` for eleven. Those are the source's own words, carried through unresolved rather than computed. |
| P2 | A | `#b3b3b3` | One hex, two names in the prose with two distinct jobs ("Separator: divider lines"; "Silver: secondary text, muted labels, inactive nav"). Kept as two tokens, neither added to satisfy a pattern. |
| P2 | B | white on green | `#ffffff` on `#1ed760` is 1.92:1 and the source documents green as a control *background* without ever saying the label must be black. The Agent Prompt Guide does say `#000000` icon; now stated as a rule in Colors and in the Don'ts. |
| P2 | J | Iteration Guide | The file's Iteration Guide is a `###` subsection inside the legacy Agent Prompt Guide. Left verbatim where it is rather than promoted, since the Agent Prompt Guide is kept verbatim by SPEC section 3 and Iteration Guide is optional. The harness therefore still reports it missing; see Shared issues. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Top of file | no frontmatter -> full YAML block: `colors` (22), `typography` (14), `spacing` (13), `rounded` (10), `shadow` (3), `motion` (10), `components` (16) | SPEC section 1. Every value read from the prose; nothing invented. |
| `colors:` | — -> `canvas`, `surface`, `surface-interactive`, `surface-card`, `surface-card-alt`, `text`, `text-emphasis`, `muted`, `muted-bright`, `border`, `border-outline`, `border-focus`, `divider`, `accent`, `accent-border`, `on-accent`, `focus`, `negative`, `warning`, `announcement`, `button-light`, `on-light` | All 8 required roles resolve. Every hex is one the prose already states. |
| `colors.focus` | — -> `#1ed760` | SPEC section 1's focus exception: a real role binding reusing a tone the palette already owns and already assigns to "active states". No new brand colour, no alias. |
| `colors.border-focus` | — -> `#000000` | Records the source's one *extracted* focus treatment as a token so its failure is measurable rather than invisible. Bound to `input-search-focus` exactly as the prose asserts, and left there. |
| `colors.button-light` / `on-light` | "Light Surface `#eeeeee`" / "Text `#181818`" in prose -> declared pair on `button-light-pill` | SPEC section 1: only a declared `backgroundColor`/`textColor` pair is measurable. Named `button-light`, not `surface-light`, because the prose calls it a *button* fill — it is a control fill the ring surrounds, not a ground the ring is drawn on. |
| `## 1. Visual Theme & Atmosphere` … `## 8. Responsive Behavior` | numbered -> unnumbered SPEC names, reordered to the section-contract order | SPEC section 3. |
| `## 5. Layout Principles` > "Border Radius Scale" | subsection of Layout -> `## Shapes`, promoted one level, verbatim | Shapes is a required top-level section and the radius scale was its only content in the source. Moved, not duplicated. |
| `## 9. Agent Prompt Guide` | numbered, before nothing -> unnumbered, verbatim, after `## Known Gaps` | SPEC section 3: a legacy section with no slot is kept verbatim after Known Gaps. Its nested `### Iteration Guide` moved with it unchanged. |
| after `## Components` | — -> `## Motion & Animation`, first line stating the system is prescribed and unmeasured, 11-row interaction table, `prefers-reduced-motion` block | SPEC sections 4 and 6. |
| `motion:` | — -> the **Calm** block verbatim from SPEC section 5 | Profile argued below. No value deviates from the shared block. |
| after Motion | — -> `## Accessibility` with 57 measured pairs in four tables, focus-ring coverage per surface, tap-target statement, reduced-motion statement, three plainly-stated real failures | SPEC section 2 and brief dimension G. |
| `## Components` | prose only -> `{components.*}` refs plus per-entry state lines | SPEC section 7. Three states are extracted (card hover, nav active, input focus); focus-visible elsewhere is labelled prescribed; the other five are marked not documented. |
| Colors > Surface & Border | "Border Gray: Button borders on dark" -> same, plus "**decorative only.** At 2.22:1 on the canvas it does not reach the 3:1 boundary threshold" | SPEC section 2 step 1: re-scope the frozen tone in prose, point the boundary job at `border-outline`, which the palette already owns. Add nothing. |
| Elevation & Depth | table only -> table plus a paragraph quantifying the 1.03:1–1.25:1 layer steps and naming the two-ladder split | Brief dimension C. |
| Do's / Don'ts | 7 + 7 -> 9 + 11 | Added the boundary rule, the focus-ring rule, white-on-green, `border-focus`, the layer-step warning and the layout-property prohibition. Existing lines untouched. |
| Responsive Behavior | breakpoints + collapsing -> plus "Touch Targets: not stated" | Honest answer to dimension G rather than silence. |
| end of file | — -> `## Known Gaps`, 15 entries | Everything the prose does not contain. |

### Contrast checks

All 57 pairs are in the file's Accessibility section. Reproduced here: every failure, plus the worst case for each passing token across the five charcoal grounds.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `text` #ffffff / `canvas` #121212 | 18.73:1 | 4.5:1 | Pass |
| `text` #ffffff / `surface-card-alt` #272727 (worst) | 14.94:1 | 4.5:1 | Pass |
| `text-emphasis` #fdfdfd / `surface-card-alt` (worst) | 14.69:1 | 4.5:1 | Pass |
| `muted-bright` #cbcbcb / `surface-card-alt` (worst) | 9.21:1 | 4.5:1 | Pass |
| `muted` #b3b3b3 / `surface-card-alt` (worst) | 7.12:1 | 4.5:1 | Pass |
| `on-light` #181818 / `button-light` #eeeeee | 15.30:1 | 4.5:1 | Pass |
| `on-accent` #000000 / `accent` #1ed760 | 10.94:1 | 4.5:1 | Pass |
| `on-accent` #000000 / `accent-border` #1db954 | 8.12:1 | 4.5:1 | Pass |
| `accent` #1ed760 as text / `surface-card-alt` (worst) | 7.79:1 | 4.5:1 | Pass |
| `accent-border` #1db954 as text / `surface-card-alt` (worst) | 5.78:1 | 4.5:1 | Pass |
| `warning` #ffa42b / `surface-card-alt` (worst) | 7.54:1 | 4.5:1 | Pass |
| `negative` #f3727f / `surface-card-alt` (worst) | 5.35:1 | 4.5:1 | Pass |
| `announcement` #539df5 / `surface-card-alt` (worst) | 5.34:1 | 4.5:1 | Pass |
| `divider` #b3b3b3 / `canvas` | 8.93:1 | 3:1 | Pass |
| `border-outline` #7c7c7c / `canvas` | 4.49:1 | 3:1 | Pass |
| `border-outline` #7c7c7c / `surface-interactive` #1f1f1f | 3.95:1 | 3:1 | Pass |
| `border-outline` #7c7c7c / `surface-card-alt` (worst) | 3.58:1 | 3:1 | Pass |
| `focus` #1ed760 / `canvas` | 9.76:1 | 3:1 | Pass |
| `focus` #1ed760 / `surface-card-alt` (worst ground) | 7.79:1 | 3:1 | Pass |
| `text` #ffffff / `accent` #1ed760 | 1.92:1 | 4.5:1 | **Fail** — never use it; green controls carry a black icon |
| `border` #4d4d4d / `canvas` #121212 | 2.22:1 | 3:1 | **Fail** — frozen, decorative |
| `border` #4d4d4d / `surface` #181818 | 2.10:1 | 3:1 | **Fail** — frozen, decorative |
| `border` #4d4d4d / `surface-interactive` #1f1f1f | 1.95:1 | 3:1 | **Fail** — frozen, decorative |
| `border` #4d4d4d / `surface-card-alt` #272727 | 1.77:1 | 3:1 | **Fail** — frozen, decorative |
| `border-focus` #000000 / `surface-interactive` #1f1f1f | 1.27:1 | 3:1 | **Fail** — extracted focus border, the serious one |
| `border-focus` #000000 / `surface-card-alt` #272727 | 1.41:1 | 3:1 | **Fail** — extracted |
| `border-focus` #000000 / `surface` #181818 | 1.18:1 | 3:1 | **Fail** — extracted |
| `border-focus` #000000 / `canvas` #121212 | 1.12:1 | 3:1 | **Fail** — extracted |
| `focus` #1ed760 / `button-light` #eeeeee | 1.65:1 | 3:1 | **Fail, and not required** — `button-light` is a control fill, not a ground the ring is drawn on. The ring sits outside the pill on the dark canvas behind it, at 9.76:1. Stated in the file. |
| `canvas` / `surface` | 1.06:1 | — | Layer separation, not a WCAG pair |
| `surface-card` / `surface-card-alt` | 1.03:1 | — | Layer separation, not a WCAG pair |

All five pairs the harness flags are disclosed with their measured ratios, so `contrast_unresolved` is empty. Nothing was changed to make a ratio pass; no identity hex was touched.

### Motion inventory

Prescribed, not measured — the source contains no motion value. **Calm** profile block, carried verbatim.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity` of the card's lightening overlay | Same crossfade, capped at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.97)` plus `opacity` | Scale removed; opacity only, at `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Instant, never suppressed |
| Page / route transition | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)`→0, content pane only | Travel removed; fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(16px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-base}` | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Dropdown enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-6px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(12px)`→0 | Travel removed; fade at `{motion.duration-reduced}` |
| List enter (playlist grid) | `{motion.duration-base}`, stagger `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)`→0 | Stagger and travel removed; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at `{motion.duration-reduced}` |
| Loading | 1200ms, infinite | linear | `opacity` pulse on an album-art placeholder | Frozen; static placeholder remains |

Exit is shorter than its entrance everywhere. Only `transform` and `opacity` animate. No brand ambience is prescribed — the loader is the only infinite animation, and the equalizer motion of a real player is not in this document, so none was invented.

**Profile argument: Cinematic -> Calm.** Applying SPEC section 5's rule in order. Rule 1 asks for a luxury, automotive, hardware-flagship, gaming-console or aerospace identity; a music-streaming app is none of those, and rule 1's own stated tell — "full-bleed photography, sparse type and a slow reveal" — is absent from this document in all three parts. The type is compact and functional at 10px–24px with an explicit Don't against relaxed line-heights; the file's own words are "this is an app, not a marketing site. Every pixel serves the listening experience" and "content density over breathing room"; and nothing anywhere in it describes a reveal. Rule 2 does not fire (consumer media app, not a terminal, IDE, infra or developer tool). Rule 3 does not fire (the palette is explicitly achromatic with one functional green; the type voice is systematic, not informal). Rule 4 is the terminal answer: **Calm**, whose signature of short opacity-led fades with little travel is precisely what the file's one documented hover ("slight background lightening") asks for. At a Cinematic 400ms base a play button reads as broken. The word "premium" in the Overview is what put spotify in `make_roster.py`'s hand-curated Cinematic set, but it is used there of tactility — "feels like a premium audio device — tactile, rounded, and built for touch" — not of pace.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/roster.md` line 74 | Row A67 still records `Cinematic` for `spotify`; this file now carries Calm, argued above. Cross-file comparability depends on the roster matching what the files do. | Change the profile cell to `Calm`. |
| `theme-audit/make_roster.py` line 37 | `spotify` is hand-listed in the `CINEMATIC` set. Regenerating the roster would silently revert it, the way `airtable` and `cal` needed `CALM_OVERRIDE` entries. | Remove `"spotify"` from `CINEMATIC`, or add it to `CALM_OVERRIDE` beside `airtable` and `cal` with the same style of comment. |
| `theme-audit/audit.py` line 305 (`find_role_strongest`, defined line 160) | `find_role_strongest` makes `divider` (#b3b3b3, 8.93:1) the representative for `border`, so `roles_resolved` and the `border on canvas` table check both report a pass while the token the prose actually names "button borders on dark" fails on every ground in the file. `check_all` does catch it, so nothing is hidden — but the summary line reads as a clean pass on a file whose named border tone clears 3:1 nowhere. | Report both: the representative token and the worst-contrast tone in the role, e.g. `roles_resolved["border"] = {"representative": "divider", "worst": "border"}`. |
| `theme-audit/audit.py` line 232 | `optional_sections_missing` reports `Iteration Guide` missing for every legacy file that carries one as a `###` inside the verbatim Agent Prompt Guide, which SPEC section 3 requires be kept as-is. It costs no score, but it is a false negative in nine files. | Match `^###? Iteration Guide\s*$` for the optional set only. |
| `theme-audit/audit.py` lines 550-588 | The focus-ring coverage check builds `surface_keys` from token *names* plus `CONTAINER`-named component bindings. A light control fill named `button-light` is correctly excluded; the same hex named `surface-light` would be charged as a ground the ring must clear, even though SPEC section 1 says a ring is judged against the surfaces it is drawn *on*, not the fill it surrounds. The right answer here came from a naming choice, not from logic. | Decide ring grounds solely from component bindings whose component name matches `CONTAINER`, and drop the name-based `surface_keys` regex. |

### Needs approval

1. **Re-bind the search input's focus border.** `{components.input-search-focus}` binds `borderColor: {colors.border-focus}` (`#000000`), measured at **1.27:1** against the input's own `#1f1f1f` fill. Left exactly as extracted per SPEC section 2 step 3. Proposed: a 2px `{colors.focus}` (`#1ed760`) ring at a 2px offset outside the control — **8.59:1** on `#1f1f1f`. Nearest passing value if the treatment must stay achromatic: the ring has to get *lighter*, not darker. `#696969` is the darkest achromatic tone that clears 3:1 on `#1f1f1f` (exactly 3.00:1), so anything below it fails and `#000000` cannot be made to work on any surface in this palette. There is no usage note that makes the real value defensible — WCAG sets no large-text exemption for a focus indicator. This is the one change I would make to the real product.
2. **Re-scope `{colors.border}` (`#4d4d4d`) to decoration permanently.** The prose calls it "button borders on dark" and it clears 3:1 on no surface in the file (2.22:1 / 2.10:1 / 1.95:1 / 1.81:1 / 1.77:1). I re-scoped it in prose and pointed the boundary job at `{colors.border-outline}` (`#7c7c7c`, 3.95:1 on the pill fill), which the palette already owns — so no token was added. Its `components:` bindings are untouched because it has none; a brand owner needs to confirm that Border Gray is decorative on the real site, which the source's own Don't ("don't expose raw gray borders") implies but does not state. Defensible as-is only where a control's boundary is carried by the fill step or the inset shadow rather than the stroke.
3. **Confirm the Calm profile** and the two roster changes under Shared issues.
4. **Quantify the card hover.** "Slight background lightening" names no target tone and no overlay opacity, so there is no hover token and the Motion table expresses it as an overlay `opacity` fade. `#1f1f1f`, `#252525` and `#272727` are all plausible targets and the source picks none; a brand owner can say which.

### Identity verdict

Still unmistakably Spotify. The reason is that almost nothing had to be added to the identity-bearing layers: the palette is 22 hexes all of which were already written in the prose, the five-step charcoal ladder from `#121212` to `#272727` survives intact with its near-invisible 1.03:1–1.25:1 steps documented rather than smoothed, and the three pill spellings (100px / 500px / 9999px) plus the 50% circles are kept as three separate rounded tokens instead of being collapsed into one tidy `pill: 9999px` that would have read as any other design system. Spotify Green appears exactly twice in the token block — as `accent` and as `focus` — and the focus binding is the brand's own functional green doing a functional job, not a borrowed blue ring. `on-accent: #000000` is extracted from the source's own play-button prompt, and the file now says out loud that white on that green is 1.92:1, which is a Spotify-specific fact no generic block would carry.

The two places the file could have drifted and did not: the motion section is labelled prescribed in its first line and its profile is argued from the file's own sentences rather than inherited, and the state matrix marks three extracted states and five absences rather than filling in a plausible-looking hover/press/disabled set that would have scored 5 and described no real product. The states score of 1 is the honest reading of a document that genuinely records three interaction states. Nothing here reads as borrowed from another file in the collection.
