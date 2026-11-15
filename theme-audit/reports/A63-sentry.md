## A63 · sentry

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 2 | 5 | 5 | 2 | 1 | 1 |
| after | 3 | 5 | 5 | 5 | 5 | 5 |

`tokens` is capped at 3 on purpose: the two roles the harness still reports missing (`canvas`, `text-dim`) are both plainly present in the palette under another name, which SPEC section 1 says is a harness bug to report, not a token to invent. No alias was added to lift the score.

The before-run's `contrast: 5` was an artefact, not a clean bill of health: because no key matched the `canvas` role, every canvas-anchored check was skipped and six real failures went unmeasured. They are measured and disclosed below.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F motion | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule. Zero durations, zero easings. |
| P0 | G accessibility | whole file | No `## Accessibility` section. Six extracted tones fail their WCAG threshold and none was disclosed. |
| P0 | A/E focus ring | `ring-focus` | The only ring in the file is a pale blue at **1.85:1** on `{colors.surface-canvas-light}` and **1.62:1** on `{colors.surface-press-light}`. A dual-polarity file had one ring, usable on one polarity, and the token name (`ring-focus`) was not addressable as the focus role. |
| P0 | B colour | `hairline-cool` | **1.54:1** on the light canvas, and on the real site it is the *only* boundary of `text-input` — a genuine WCAG 1.4.11 failure for form fields. Undisclosed. |
| P1 | B colour | `hairline-cloud` | **1.24:1** on the light canvas; border of `card-pricing` and the pricing-table divider. Undisclosed. |
| P1 | B colour | `hairline-violet` | **1.37:1** on `{colors.surface-canvas-dark}`, **1.49:1** on `{colors.surface-night}`; boundary of every dark card. Undisclosed. |
| P1 | B colour | `on-dark-faint` | **1.53:1** on the dark canvas — the fill of `button-ghost-on-dark`, which therefore has no perceivable edge. |
| P1 | B colour | `accent-pink` | **2.42:1** on the light canvas and documented as a chart-point colour; below the 3:1 of 1.4.11 for non-text graphics. |
| P1 | H states | all components | Only `pressed` and `disabled` were documented anywhere. Six of the eight states were absent, and the Components header said so without routing the gap anywhere. |
| P1 | A sections | whole file | `## Known Gaps` missing entirely — a required section, and the file had plenty to record. |
| P1 | G accessibility | Responsive Behavior | Touch-target arithmetic was wrong: "12px vertical padding × 16px font + line-height = ~44px" actually yields **40px** (12 + 12 + 14px × 1.14 ≈ 40), so the stated 44×44px AAA claim did not hold. |
| P1 | A tokens | `shadow` group | The Elevation table documents five real shadow values in prose with no `shadow:` group to reference, which SPEC section 1 requires in exactly this case. |
| P2 | C elevation | Elevation & Depth | Shadow and border were used as elevation with no rule saying which applies where — dark cards use a hairline, light cards a shadow, level 3 a canvas-coloured vignette. Consistent in practice, undocumented. |
| P2 | D typography | `pill-neutral-dark` | Prose said "`{typography.caption}` 12px"; the token is 14px. |
| P2 | A tokens | `on-dark-muted`, `on-dark-faint`, `ring-focus` | Prose states an `rgba(...)` for each; the token block carries a flat hex that does not composite exactly to the stated alpha over either canvas. Which form is the extraction cannot be settled from the file. |
| P2 | E ladders | `spacing` | Layout states mobile section padding as "32px–48px"; 48px sits outside the spacing ladder with no token. |
| P2 | I identity | — | None. The file reads strongly as itself; see Identity verdict. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | `ring-focus: "#9dc1f5"` -> `focus: "#9dc1f5"` | Renamed, hex untouched, so the ring is addressable as the `focus` role. SPEC section 1 calls this a real role binding, not an alias. The old name matched no focus pattern. |
| frontmatter `colors:` | — -> `focus-on-light: "#422082"` | The pale blue is 1.85:1 on the light canvas. SPEC section 1 requires a second ring where a file documents both polarities. Reuses the brand's existing Deep Violet; 11.93:1 on white. |
| frontmatter | — -> `motion:` group, Crisp block verbatim from SPEC section 5 | Required group; no deviation from the profile's values. |
| frontmatter | — -> `shadow:` group, five tokens | The prose documents real shadow values, which SPEC section 1 makes the trigger for this group. Values copied verbatim from the Elevation table. |
| Colors › Semantic | one focus-ring bullet -> two, by polarity | States which ground each ring is drawn on, the offset, and that neither introduces a new brand colour. |
| Colors › Text | `on-dark-muted` bullet | Named it as the system's `text-dim` role with its measured ratios, and recorded that the light canvas has no muted ink. |
| Colors › Surface | three hairline bullets + new paragraph | Scoped all three frozen hairlines to decoration with their measured ratios, and pointed implementers at `{colors.accent-violet-mid}` (5.33:1 light / 3.23:1 dark) for boundaries that must be seen. Added no new border token, since the palette already owns a passing tone. |
| Elevation & Depth | raw shadow strings -> `{shadow.*}` references with the literal kept in parentheses; new "How elevation is expressed" paragraph | Makes elevation referenceable and states the one consistent rule: shadow on light, hairline-plus-fill on dark. |
| Components header | "No hover states documented." -> extraction scope note | Separates what was extracted from what is prescribed, so the prescribed states cannot be mistaken for observed facts. |
| Components | — -> `### State matrix` | Covers all eight states for every component, each marked extracted / prescribed / genuinely absent. Records `pill-neutral-dark` and `chip-lime-keyword` as genuinely single-state. |
| Components › `text-input` | focus bullet | References `{shadow.input-focus-inset}` and states that an inset shadow is not a sufficient focus indicator; pairs it with the prescribed ring. |
| Components › `pill-neutral-dark` | "caption 12px" -> "caption 14px" | Matched the prose to the token. |
| after Components | — -> `## Motion & Animation` | First line states the system is prescribed and not measured. Crisp tokens, 13-row interaction table covering all ten required interactions, transform/opacity only, every exit shorter than its entrance, reduced-motion CSS block. |
| after Motion | — -> `## Accessibility` | Measured contrast for 18 key pairs, a plain statement of the six real failures, per-surface ring visibility, tap-target correction, reduced-motion pointer. |
| Responsive › Touch Targets | wrong arithmetic -> corrected, with `min-height: 44px` required explicitly | The claimed 44px did not follow from the padding. |
| end of file | — -> `## Known Gaps` | Nine gaps, including the absent light-canvas muted ink, the absent semantic palette, and everything unverifiable without a render. |

Section order now matches SPEC section 3 exactly: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Motion & Animation, Accessibility, Do's and Don'ts, Responsive Behavior, Iteration Guide, Known Gaps.

### Contrast checks

All ratios computed with WCAG 2.1 relative luminance in a `python3 -I` snippet, standard library only; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #1f1633 / `surface-canvas-light` #ffffff | 17.20:1 | 4.5:1 | Pass |
| `on-primary` #ffffff / `surface-canvas-dark` #1f1633 | 17.20:1 | 4.5:1 | Pass |
| `on-primary` / `surface-night` #150f23 | 18.68:1 | 4.5:1 | Pass |
| `on-primary` / `primary` #150f23 (on-accent on accent) | 18.68:1 | 4.5:1 | Pass |
| `on-primary` / `accent-violet-deep` #422082 | 11.93:1 | 4.5:1 | Pass |
| `on-primary` / `accent-violet-mid` #79628c | 5.33:1 | 4.5:1 | Pass |
| `on-dark-muted` #bdb8c0 / `surface-canvas-dark` | 8.83:1 | 4.5:1 | Pass |
| `on-dark-muted` / `surface-night` | 9.59:1 | 4.5:1 | Pass |
| `ink-deep` / `accent-lime` #c2ef4e (88px/700 chip) | 12.90:1 | 3:1 | Pass |
| `ink-press` #1a1a1a / `surface-press-stronger` #efefef | 15.14:1 | 4.5:1 | Pass |
| `ink-press` / `surface-press-light` #f0f0f0 | 15.27:1 | 4.5:1 | Pass |
| `accent-violet` #6a5fc1 / `surface-canvas-light` (inline link) | 5.22:1 | 4.5:1 | Pass |
| `accent-violet-mid` / `surface-canvas-light` (accessible boundary) | 5.33:1 | 3:1 | Pass |
| `accent-violet-mid` / `surface-canvas-dark` (accessible boundary) | 3.23:1 | 3:1 | Pass |
| `focus` #9dc1f5 / `surface-canvas-dark` | 9.32:1 | 3:1 | Pass |
| `focus` / `surface-night` | 10.12:1 | 3:1 | Pass |
| `focus` / `accent-violet-deep` | 6.46:1 | 3:1 | Pass |
| `focus-on-light` #422082 / `surface-canvas-light` | 11.93:1 | 3:1 | Pass |
| `focus-on-light` / `surface-press-light` | 10.47:1 | 3:1 | Pass |
| `focus-on-light` / `surface-press-stronger` | 10.37:1 | 3:1 | Pass |
| `focus` / `surface-canvas-light` | 1.85:1 | 3:1 | **Fail** — why the light polarity needs its own ring; disclosed |
| `focus` / `surface-press-light` | 1.62:1 | 3:1 | **Fail** — same; disclosed |
| `hairline-cool` #cfcfdb / `surface-canvas-light` | 1.54:1 | 3:1 | **Fail** — extracted, frozen, disclosed |
| `hairline-cloud` #e5e7eb / `surface-canvas-light` | 1.24:1 | 3:1 | **Fail** — extracted, frozen, disclosed |
| `hairline-violet` #362d59 / `surface-canvas-dark` | 1.37:1 | 3:1 | **Fail** — extracted, frozen, disclosed |
| `hairline-violet` / `surface-night` | 1.49:1 | 3:1 | **Fail** — extracted, frozen, disclosed |
| `on-dark-faint` #3f3849 / `surface-canvas-dark` | 1.53:1 | 3:1 | **Fail** as a boundary; it is a fill, so 1.4.11 does not apply to it — disclosed with that note |
| `accent-pink` #fa7faa / `surface-canvas-light` | 2.42:1 | 3:1 (non-text) | **Fail** — decoration and chart points only; disclosed |
| `accent-lime` / `surface-canvas-light` | 1.33:1 | 3:1 (non-text) | **Fail** — chip fill only, never type; disclosed |
| `accent-pink` / `surface-canvas-dark` | 7.11:1 | 3:1 | Pass (its primary home) |
| `accent-lime` / `surface-canvas-dark` | 12.90:1 | 3:1 | Pass (its primary home) |

No identity hex was changed.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity` of an overlay layer | Fade at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` only; no scale pop (Crisp) | Instant swap, no transition |
| Focus ring | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` of the ring | Appears with no transition; never suppressed |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | `opacity` of the content band, no travel | `opacity` at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` + `translateY(8px → 0)` | `opacity` only, no travel |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity` + `translateY(0 → 4px)` | `opacity` only, no travel |
| Dropdown | enter 100ms / exit 60ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(4px → 0)` | `opacity` only, no travel |
| Toast enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` + `translateY(8px → 0)` | `opacity` only |
| Toast exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity` + `translateY(0 → 4px)` | `opacity` only |
| List enter | 100ms per item, `{motion.stagger-step}` 20ms between | `{motion.ease-enter}` | `opacity` + `translateY(4px → 0)` | `opacity` only, stagger 0, no travel |
| List exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` | `opacity` at `{motion.duration-reduced}`, no stagger |
| Loading (spinner) | `{motion.duration-emphasis}` 300ms per revolution, infinite | linear | `transform: rotate()` | Static indicator; label carries the state |
| Loading (skeleton) | `{motion.duration-slow}` 220ms per cycle, infinite | `{motion.ease-standard}` | `opacity` 1 → 0.5 → 1 | Frozen at one mid opacity |

Only `transform` and `opacity` animate. Every exit is shorter than its entrance. The two infinite animations are both loaders. The sticker mascots and starfield are documented as static, so the file claims no brand ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 20-21 (`REQUIRED_COLOR_ROLES["canvas"]`) | The `canvas` role reports missing although the palette plainly owns `surface-canvas-dark` and `surface-canvas-light`, named in the prose as "Dark Canvas" and "Light Canvas". No pattern reaches a canvas key behind a `surface-` prefix. This is the harness bug SPEC section 1 describes, so no token was invented. Knock-on: with no canvas resolved, `_canvas_hex()` falls back to `#ffffff`, `canvas_polarity` is `None`, and every canvas-anchored contrast check and the `find_role_strongest` pass for border/focus/text-dim are skipped — which is why this file scored `contrast: 5` with six real failures in it. | Add `r"^surface-canvas($|[-_])"` (and, for other files, `r"^surface[-_]page"`) to the `canvas` pattern list, ordered after the exact-name patterns so a file with a literal `canvas` key is unaffected. |
| `theme-audit/audit.py` line 28-31 (`REQUIRED_COLOR_ROLES["text-dim"]`) | `text-dim` reports missing although `on-dark-muted` is exactly that role and is described in the prose as "Secondary text, captions, and table cell values". The list already carries `^on-dark-soft$` as an exact string, which catches one file's spelling and misses the synonym. | Replace the literal `r"^on-dark-soft$"` with `r"^on-(dark|light)-(muted|soft|subtle|faint|secondary)$"`. A plain `^muted` prefix would not help here, since the tone's name leads with its ground. |
| `theme-audit/audit.py` line 37 (`REQUIRED_COLOR_ROLES["focus"]`) | `^focus($\|[-_])`, `^focus-ring$`, `^ring$` miss the common reversed spelling `ring-focus`, which this file used. Several files are likely to carry the same name. | Add `r"^ring[-_]"` to the pattern list. I renamed the token here under SPEC section 1's focus exception, but the pattern gap will recur. |
| `theme-audit/briefs/A63-sentry.md` line 11 | The brief lists `surface` among the missing colour roles; the harness resolves it to `surface-canvas-dark` both before and after my edits. The brief's role list disagrees with the harness it cites. | Regenerate the briefs from a current harness run, or have `make_briefs.py` stamp the run it was generated from. |
| `theme-audit/briefs/A63-sentry.md` line 3 | "Theme intent:" is truncated mid-sentence ("— a"), as is the roster row. The agent is given a fragment of its own site's description. | `make_roster.py` / `make_briefs.py`: stop truncating the description, or truncate on a word boundary with an ellipsis. |
| `design-md/sentry/DESIGN.md` Iteration Guide step 3 | Instructs the reader to run `npx @google/design.md lint DESIGN.md`, which introduces a network dependency and a tool this repo does not use; the audit here is `theme-audit/audit.py`. Left verbatim because it is pre-existing content outside the dimensions I was asked to fix. | Point step 3 at `python3 theme-audit/audit.py --site sentry` instead, repo-wide. |

### Needs approval

1. **Re-binding `text-input`'s border.** The extracted boundary is `{colors.hairline-cool}` #cfcfdb at **1.54:1** on white, and on the real site it is the field's only boundary — a WCAG 1.4.11 failure. The `components:` binding is left exactly as extracted, per SPEC section 2. Nearest passing value the palette already owns: `{colors.accent-violet-mid}` #79628c at **5.33:1**; nearest value that keeps the cool-grey character is roughly **#8e8ea0** (3.05:1). Usage note that would make the real value defensible: *none for this element* — a control boundary has no large-element exemption. The hairline is defensible only as a non-meaningful divider.
2. **Re-binding `card-pricing`'s border.** `{colors.hairline-cloud}` #e5e7eb at **1.24:1**. Defensible as extracted *if* the card's boundary is decorative and the card is not itself the interactive target; if the whole tier card is clickable, it needs `{colors.accent-violet-mid}`. Needs a brand-owner answer on whether the pricing card is a link.
3. **Re-binding the dark-card hairline.** `{colors.hairline-violet}` #362d59 at **1.37:1** / **1.49:1**. Nearest passing value in the violet family: #79628c (3.23:1 on `surface-canvas-dark`). Same question — decorative chrome or control boundary.
4. **`accent-pink` as a chart-point colour.** #fa7faa is **2.42:1** on the light canvas, below the 3:1 of 1.4.11 for meaningful non-text graphics. Defensible usage note: pink as *decoration only* (sticker outlines, which carry no information) — which is what the Don'ts already say. If chart points genuinely encode data on the light canvas, the series needs a darker tone or a non-colour channel (shape, label). Nearest passing pink: roughly **#d13f70** (4.56:1).
5. **`button-ghost-on-dark` has no perceivable edge.** Fill `{colors.on-dark-faint}` at **1.53:1** on the dark canvas, with no border token. Adding a `{colors.accent-violet-mid}` 1px boundary (3.23:1) would fix it but changes the extracted appearance of a signature control.
6. **The second focus ring.** `focus-on-light` carries the same hex as `{colors.accent-violet-deep}`. SPEC section 1 sanctions a focus role bound to a hex the palette already owns, and a dual-polarity file is required to define two rings, so I treated it as a role binding rather than an alias. If the project would rather have one ring token with a documented per-polarity rule, that is a one-line change.
7. **Renaming `ring-focus` to `focus`.** The hex is unchanged and the single prose reference was updated. If extracted token *names* are meant to be as frozen as extracted values, this should be reverted and the harness pattern fixed instead (see Shared issues).

### Identity verdict

Still unmistakably itself. The additions are anchored in the file's own vocabulary rather than in generic tokens: the focus rings reuse the brand's extracted pale blue and its Deep Violet instead of a borrowed system blue; the accessible boundary is the existing Mid Violet, so no new hue entered the palette; the selected-state treatments reach for the lime 2px bar, which is the brand's own highlight device; and the state matrix is written in the file's component names, not in abstract roles.

The Crisp assignment is **correct** and I kept it. Assignment rule 2 fires on the identity — an observability and error-monitoring developer tool, with a Monaco code tier, install snippets, dense reference tables, and a type system whose stated principle is that "the product reads like a log". Rule 3 is the only real competitor, since the file is illustration-led with saturated lime and pink. It does not fire: the saturated colour appears on stickers, chips and chart points, never on an interactive element — the Don'ts explicitly forbid lime as a button background and pink on buttons — and the single CTA is a near-black violet. Rule 3 asks for saturation *and role*, and the role is absent. Rule 2 also precedes rule 3 in the ordering, so even on a generous reading of the illustration the answer is Crisp.

The one tension worth recording: Crisp forbids the scale pop that this brand's sticker-and-squiggle personality might invite. I resolved it by keeping all motion crisp and letting the illustration layer carry the personality statically, which is also what the Elevation section already says depth is for. The brand's playfulness lives in its drawing, not in its timing.
