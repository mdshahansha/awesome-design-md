## A78 · voltagent

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 3 | 1 | 1 | 1 |
| After | 5 | 5 | 5 | 5 | 5 | 5 |

Harness invocation: `python3 -I theme-audit/audit.py --site voltagent --json`, run from the repo root before and after the edits. Every ratio in this report was computed with a WCAG 2.1 relative-luminance snippet in `python3 -I`; none is estimated.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F — Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. No duration, easing or transition recorded anywhere. Confirmed: `durations_found: []`, `easings_found: 0`. |
| P0 | C/B — Colour, elevation | `{colors.hairline}` `#3d3a39` | The brand's universal 1 px edge measures **1.69:1** on `{colors.canvas}` `#101010` and **1.54:1** on `{colors.canvas-soft}` `#1a1a1a`, against the 3.0:1 SC 1.4.11 needs. Harness figures confirmed exactly. Since the same hairline is the only boundary of `text-input`, the real site fails AA at the point where a user has to find a form field. |
| P0 | C — Background and elevation | `{colors.canvas}` vs `{colors.canvas-soft}` | The two layers measure **1.09:1** against each other, so they are not distinguishable as layers at all. Worse, `card-feature` paints `{colors.canvas}` on a `{colors.canvas}` band — a 1.00:1 step — so the brand's whole marketing elevation system rests on a 1.69:1 line. Not reported by the harness; this pair is not in its check list. |
| P0 | G — Accessibility | whole file | No `## Accessibility` section, so three measurable failures were undisclosed. |
| P1 | A — Token contract | `focus` | No focus role. The Colors section already asserted that `{colors.primary-soft}` is used for "tooltip / focus indicators", so the role was satisfiable from the prose and was simply never bound. |
| P1 | A — Token contract | `focus` on a light fill | `ex-pricing-tier-featured` paints a light `#f2f2f2` fill. The green ring collapses to **1.67:1** there; `{colors.primary}` reaches 1.65:1 and `{colors.primary-deep}` only 2.27:1, so no green in the palette can serve that ground. One ring was not enough. |
| P1 | A — Token contract | `shadow:` group | The prose documents two real shadow values (`0 0 15px rgba(92, 88, 85, 0.2)` and the modal stack) and the Examples block references "elevated shadow" and "medium shadow", with no token to point at. SPEC section 1 requires a `shadow:` group exactly here. |
| P1 | H — States | every component | One state word documented in `## Components` (`active`, from `ex-app-shell-row`). hover, focus-visible, pressed, disabled, loading, selected and error were named nowhere. |
| P1 | Sections | `Responsive Behavior` | Present only as the Layout subsection `### Responsive Strategy` with `####` children, not as a top-level section. |
| P1 | Sections | `Known Gaps` | Missing. Several real limits (no semantic palette, no token for the dashed divider, unexplained mono weight 549) were therefore undocumented. |
| P2 | E — Radius ladder | `{rounded.xs}` | The Shapes table assigned 4 px to "code inline chips", but `code-inline-chip` binds `{rounded.sm}` 6 px. A documented value contradicting its own component. |
| P2 | C — Elevation consistency | Levels 0-3 | Elevation is expressed two ways — border for 0-1, shadow for 2-3 — while Don'ts forbids shadows on cards. Not actually random (the split is marketing vs in-product), but nothing in the file said so, so it read as mixed. |
| P2 | B — Colour | `{colors.rounded.full}` / `{colors.rounded.pill}` | Both 9999px. Duplicate values, but with distinct documented uses (status tags vs circular icon containers), so left as extracted. No change. |
| P2 | D — Typography | all roles | Checked: every one of the 16 roles carries fontSize, fontWeight and lineHeight. Body 16px/26px in `{colors.body}` on `{colors.canvas}` is 10.13:1. No finding — recorded because the brief asks. |

Dimension I (identity) and A (reference integrity) had no findings before the edits: `dangling_refs` was already empty and stayed empty.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#2fd6a1"` | Binds the ring to a hex the palette already owns, and specifically to the tone the Colors section already says is the focus indicator. A real role binding under SPEC section 1, not an alias; a comment in the frontmatter says so. |
| frontmatter `colors:` | — -> `focus-on-light: "#101010"` | The one light fill this file declares needs an opposite-polarity ring. Reuses the brand's own `{colors.on-primary}` near-black at 17.00:1; no new chromatic value invented. |
| frontmatter | — -> `shadow:` group (`none`, `glow`, `modal`) | The prose already stated these rgba values. Now referenceable; Elevation & Depth and two `ex-*` entries point at them. |
| frontmatter | — -> `motion:` group | The **Crisp** profile block from SPEC section 5, verbatim, no deviation. |
| frontmatter `components:` | `ex-modal-card`, `ex-toast`, `ex-auth-form-card` gain `textColor: "{colors.ink}"`; the first two gain `shadow:` | Each description already asserts it re-uses feature-card chrome and a shadow; declaring the pair makes the ink measurable instead of invisible to the harness. All three pass (17.00:1 / 15.55:1). |
| `## Colors` → Surface | `{colors.hairline}` described only as "the brand's universal edge colour" -> plus its two measured failing ratios and an explicit scoping to decoration; `{colors.hairline-soft}` re-scoped as the palette's accessible boundary tone with its two passing ratios | SPEC section 2 step 1: the palette already owns a passing tone, so re-scope the prose and add nothing. Step 4: say plainly that the real brand fails AA here. |
| `## Elevation & Depth` | raw rgba strings -> `{shadow.glow}` / `{shadow.modal}` / `{shadow.none}`; new paragraph naming the border-vs-shadow seam and the 1.00:1 card step | Makes the two-way expression deliberate and documented instead of apparently random. |
| `## Shapes` | `{rounded.xs}` "code inline chips" -> "icon chips", with a parenthetical pointing at `{rounded.sm}` | Removes the contradiction with `code-inline-chip`. |
| `## Components` | — -> `### Interaction States`, an 11-row × 8-state table, placed after Signature Components and before Examples | SPEC section 7. Two entries declare a smaller real surface: `code-inline-chip` is two states (it is static inline typography), `green-divider-band` is one. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Token table, 15-row inventory covering all ten required interactions, the four motion rules, and a `@media (prefers-reduced-motion: reduce)` block saying what is removed and what remains. |
| after Motion | — -> `## Accessibility` | 12 passing text pairs, 3 disclosed failures with ratios, the focus-ring table with geometry and offset, tap targets computed from tokens, reduced motion. |
| `## Layout` | `### Responsive Strategy` + four `####` children -> **moved** to top-level `## Responsive Behavior` with `###` children, verbatim text, placed after Do's and Don'ts | SPEC section 3: move, never duplicate, promoting child headings one level. A one-line pointer is left in Layout. |
| end of file | — -> `## Known Gaps` | Eight real limits, including the fact that the entire motion section is prescribed. |
| `## Do's and Don'ts` | +2 Do's, +2 Don'ts | The hairline-soft boundary rule, the focus ring, the transform/opacity rule and the no-scale-pop rule, so the new sections are enforced where a reader looks for rules. |

Nothing outside those locations was reflowed. No existing sentence was deleted; no extracted hex was altered.

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#f2f2f2` / `canvas` `#101010` | 17.00:1 | 4.5 | Pass |
| `ink` / `canvas-soft` `#1a1a1a` | 15.55:1 | 4.5 | Pass |
| `ink-strong` `#ffffff` / `canvas` | 19.03:1 | 4.5 | Pass |
| `body` `#bdbdbd` / `canvas` | 10.13:1 | 4.5 | Pass |
| `body` / `canvas-soft` | 9.26:1 | 4.5 | Pass |
| `mute` `#8b949e` / `canvas` | 6.19:1 | 4.5 | Pass |
| `mute` / `canvas-soft` | 5.66:1 | 4.5 | Pass |
| `canvas-text-soft` `#f5f6f7` / `canvas-soft` | 16.08:1 | 4.5 | Pass |
| `on-primary` `#101010` / `primary` `#00d992` | 10.28:1 | 4.5 | Pass |
| `on-primary` / `primary-soft` `#2fd6a1` | 10.20:1 | 4.5 | Pass |
| `on-primary` / `primary-deep` `#10b981` | 7.50:1 | 4.5 | Pass |
| `on-primary` / `ex-pricing-tier-featured` fill `#f2f2f2` | 17.00:1 | 4.5 | Pass |
| `primary` / `canvas` | 10.28:1 | 3.0 | Pass |
| `primary` / `canvas-soft` | 9.40:1 | 3.0 | Pass |
| `primary-soft` / `canvas` | 10.20:1 | 3.0 | Pass |
| `primary-soft` / `canvas-soft` | 9.33:1 | 3.0 | Pass |
| `primary-deep` / `canvas` | 7.50:1 | 3.0 | Pass |
| `primary-deep` / `canvas-soft` | 6.86:1 | 3.0 | Pass |
| `hairline-soft` `#b8b3b0` / `canvas` | 9.16:1 | 3.0 | Pass |
| `hairline-soft` / `canvas-soft` | 8.38:1 | 3.0 | Pass |
| `focus` `#2fd6a1` / `canvas` | 10.20:1 | 3.0 | Pass |
| `focus` / `canvas-soft` | 9.33:1 | 3.0 | Pass |
| `focus-on-light` `#101010` / `#f2f2f2` | 17.00:1 | 3.0 | Pass |
| **`hairline` `#3d3a39` / `canvas` `#101010`** | **1.69:1** | 3.0 | **Fail — disclosed** |
| **`hairline` / `canvas-soft` `#1a1a1a`** | **1.54:1** | 3.0 | **Fail — disclosed** |
| **`canvas-soft` / `canvas`** | **1.09:1** | 3.0 | **Fail — disclosed** (layer separation; not a pair the harness checks) |
| `focus` `#2fd6a1` / `#f2f2f2` light fill | 1.67:1 | 3.0 | Fail — the reason `focus-on-light` exists |
| `primary` `#00d992` / `#f2f2f2` | 1.65:1 | 3.0 | Fail — rejected as a light-ground ring |
| `primary-deep` `#10b981` / `#f2f2f2` | 2.27:1 | 3.0 | Fail — rejected as a light-ground ring |

All three disclosed failures are extracted values and were left unchanged in the frontmatter and in their `components:` bindings. After disclosure the harness reports `contrast_unresolved: []` and `contrast_disclosed: 2`.

### Motion inventory

Prescribed, not extracted. Crisp profile, SPEC section 5, verbatim.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `background-color`, `color`, `border-color` — paint only | Unchanged; nothing travels, so nothing to remove |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `background-color`, `border-color` | Unchanged |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the ring | Appears immediately, no fade |
| Page / route transition | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` only | Cross-fade at `{motion.duration-reduced}` |
| Modal / drawer open | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px)` (`translateX` for drawer) | Transform dropped; fade at `{motion.duration-reduced}` |
| Modal / drawer close | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | same pair reversed | Transform dropped; fade at `{motion.duration-reduced}` |
| Dropdown open | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(-4px)` | Transform dropped; fade at `{motion.duration-reduced}` |
| Dropdown close | `{motion.duration-instant}` | `{motion.ease-exit}` | same pair reversed | Fade at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `transform: translateY(12px)` | Transform dropped; fade at `{motion.duration-reduced}` |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | same pair reversed | Fade at `{motion.duration-reduced}` |
| List / card-grid enter | `{motion.duration-base}` per item, `{motion.stagger-step}` 20ms between, capped at 6 | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px)` | Stagger and transform dropped; one fade at `{motion.duration-reduced}` |
| List / card-grid exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity` + `transform: translateY(4px)` | Transform dropped; fade at `{motion.duration-reduced}` |
| Loading — spinner | 700ms/rev, infinite (permitted loader) | `linear` | `transform: rotate()` | Frozen; static glyph plus status text |
| Loading — skeleton | `{motion.duration-emphasis}` 300ms, infinite alternate | `{motion.ease-standard}` | `opacity` 0.4 ↔ 1 | Frozen at `opacity: 0.7` |

Every exit is shorter than its entrance. No layout-driving property is animated (`layout_animation_mentions: []` after the edit). The only infinite animations are the two loaders; the brand has no ambience and the file now says it should not acquire any.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, the contrast pair list (SPEC section 2 table, `theme-audit/SPEC.md` lines 120-130) | No pair measures **surface against canvas**, so a brand whose card fill is 1.09:1 from its page floor — or, as here, a `card-feature` painted at exactly the canvas colour, 1.00:1 — scores a clean 5 on layer separation that does not exist. This is the single most consequential thing wrong with voltagent and the harness is blind to it. | Add `surface` on `canvas` at 3.0:1 to the checked pairs, flagged as advisory rather than a hard failure where the file documents a hairline as the separator; then flag the case where the separator itself is also sub-threshold, which is the actual defect. |
| `theme-audit/audit.py` `find_role_strongest`, lines 160-166 | Not a bug, but worth recording since several agents are likely to file it as one: `border` resolves to `hairline-soft`, not to `hairline`, which the prose calls "the brand's universal edge colour". The strongest-variant pick is deliberate and documented, and both tones are still measured separately — the two `hairline` failures are reported in full. No fix needed. | None. Leaving this note so the next reader does not "fix" it. |
| `theme-audit/audit.py` disclosure matcher, lines 669-688 | Disclosure requires the failing pair's ratio on a line that also names the foreground token or hex. A disclosure phrased only as a narrative paragraph ("the hairline sits well below threshold") does not count, which is correct, but a disclosure split across a table row and its explanatory sentence can also miss. | Document the required shape in SPEC section 2 — "name the token or hex and its measured ratio on one line" — so agents do not have to read the matcher to score the point. |
| `design-md/voltagent/DESIGN.md` Examples block, and `scripts/derive-examples-block.mjs` | The auto-derived `ex-pricing-tier-featured` paints a light `#f2f2f2` fill into a brand whose Don'ts explicitly forbid a light-mode counterpart. That single generated entry is the only reason this dark-only brand needs a second focus ring. Out of scope to remove (the generator owns it, and the brief forbids editing it). | Have the generator respect a dark-only flag, or emit the featured tier as a 2 px `{colors.primary}` edge on the dark fill — which is what the real brand does for "featured" status, per Decorative Depth. |

### Needs approval

1. **Re-binding the frozen hairline in `components:`.** Seven components bind `borderColor: "{colors.hairline}"` (`button-outline-on-dark`, `button-pill-tag`, `text-input`, `card-feature`, `card-feature-emphasized`, `code-mockup`, plus `ex-pricing-tier` / `ex-data-table-cell` / `ex-cart-drawer` as row and item dividers). Those bindings are extracted facts and are left exactly as they are. Three of them — `text-input`, `button-outline-on-dark`, `button-pill-tag` — are controls whose border is their only edge, so at 1.69:1 they fail SC 1.4.11 as the real site ships them. The Interaction States table draws them with `{colors.hairline-soft}`, but the frontmatter binding still says `{colors.hairline}`, and that seam needs a brand owner to close. Nearest passing value, already in the palette: `{colors.hairline-soft}` `#b8b3b0`, at 9.16:1 on canvas and 8.38:1 on canvas-soft. Usage note that would make the extracted value defensible instead: `#3d3a39` is acceptable only on boundaries that convey no information — card edges, row rules, the dashed section divider — since SC 1.4.11 exempts purely decorative boundaries. That exemption cannot cover a text input.
2. **Using `{colors.hairline-soft}` on dark at all.** It was extracted as a tint for "rare on-light secondary contexts". Promoting it to the on-dark accessible boundary is this audit's re-scoping, and the visual consequence is real: a `#b8b3b0` edge on `#101010` is a markedly brighter line than the brand draws today, which touches the "precise hairline rectangles" the Overview names as the brand's chrome. A brand owner may prefer to raise `{colors.hairline}` itself to roughly `#595552` (3.03:1 on canvas) and accept a changed extracted value, which this audit will not do unilaterally.
3. **The two-layer surface system.** `{colors.canvas}` and `{colors.canvas-soft}` are 1.09:1 apart. Nothing in SPEC forces a fix and nothing was changed, but a system in which code blocks and inputs are meant to "mark them visually distinct against the canvas" is not achieving that at 1.09:1. If a real separation is wanted, `#1a1a1a` would need to move to roughly `#2e2e2e` (1.49:1) or beyond — again an extracted value, so again an owner's call.
4. **`focus-on-light` in a dark-only brand.** Defensible under SPEC section 1 because the file declares a light fill, but if `ex-pricing-tier-featured` is corrected to the brand's real dark "featured" treatment (see Shared issues), `focus-on-light` becomes unnecessary and should be removed rather than left as a dormant light-theme hook.
5. **The `error` state has no colour.** The brand ships no red anywhere in the extracted material. The states table builds `error` from `{colors.ink-strong}` plus a caption message. A real semantic palette is a brand decision; this document should not invent one.

### Identity verdict

Still unmistakably Voltagent. The test I applied: strip the brand name from the file and see whether a reader could still identify it. They could — one electric-green accent and no second one, a near-black canvas with no light counterpart, hairline rectangles instead of shadows, Inter at weight 400 for a 60 px hero as a deliberate refusal to shout, SF Mono reserved for anything typeable at a terminal, and `{rounded.sm}` 6 px buttons that are pointedly not pills.

The additions lean into that rather than away from it. The focus ring is the brand's own green, not a generic system blue. The Interaction States table is explicitly paint-only, and the file now says why: on a near-monochrome dark brand whose own Don'ts forbid card shadows, the hover state *is* a border or fill shift, and bolting on a scale pop to look animated would contradict the document. SPEC section 6 permits exactly this, so no apology was needed and none was written. Two components declare a genuinely smaller state surface rather than padding the table.

**Crisp is the correct profile and I did not switch it.** SPEC assignment rule 2 fires on the file's own evidence: an AI agent engineering platform for developers, code-editor mockups as the hero, copy-to-clipboard on every snippet, numeric counters in monospace, and an Overview that calls the page "polished documentation that decided to also sell something." Rule 1 cannot fire — there is no photography at all, and the file says so. Rule 3 cannot fire — one accent, sentence-case Inter, gradients explicitly forbidden. Rule 2 is a clean hit, so rule 4 never gets a turn.

The one genuine drift risk is the `ex-*` Examples block, and it was already in the file before this audit: ten auto-derived surfaces mirroring a generic kit, one of which paints a light fill into a brand that forbids light mode. I could not remove it — the generator owns it and the brief limits me to this file — so it is flagged in Shared issues and in Known Gaps, which is where a borrowed-from-another-file section belongs.
