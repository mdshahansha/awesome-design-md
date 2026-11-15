## A31 · lamborghini

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 1 | 5 |
| refs | 5 | 5 |
| contrast | 5 | 5 |
| sections | 1 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

Before: no frontmatter at all, so `refs` and `contrast` scored 5 vacuously — there was nothing to resolve and nothing to measure. After: 0 dangling refs, 0 undisclosed contrast failures, 10 disclosed failures, 0 missing sections, 0 missing states, `motion:` group complete and a `prefers-reduced-motion` rule present. Both runs are `python3 -I theme-audit/audit.py --site lamborghini --json`.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, J | whole file | No frontmatter token block. All 8 required colour roles missing; every value lived only in prose, so nothing was referenceable or measurable. |
| P0 | A, G | focus ring | No `focus` token. The only focus style documented was the ghost button's `outline 2px solid #000000` — a black ring on a black canvas, i.e. no visible focus indicator anywhere in the system. |
| P0 | B, H | Black Filled button | Extracted spec is bg `#000000` with text `#202020` — 1.29:1. Unusable as recorded; internally contradictory with its stated use on light sections. |
| P0 | B, D | Shadow `#313131` | The source describes it as "text on dark surfaces where white is too strong". 1.61:1 on canvas, 1.25:1 on charcoal — not legible as text at any size. |
| P0 | C, G, J | sections | All 12 required sections missing by name (numbered variant). No Accessibility section, no Known Gaps, no Shapes. |
| P0 | F | motion | No motion tokens, no Motion & Animation section, no reduced-motion rule, no duration or easing value anywhere in the file. |
| P1 | B, H | ghost button hover | Documented hover is white label on Teal Action `#1EAEDB` — 2.58:1. |
| P1 | B | Badge/Tag | White on Steel `#969696` at 10px — 2.96:1. |
| P1 | B | news card | The file's own example prompt specifies `#7D7D7D` body text at 16px on `#202020` — 3.96:1. |
| P1 | B | Link Blue `#3860BE` | The universal link hover colour on a black page — 3.58:1 as text. |
| P1 | B, E | section hairline `#202020` | 1.29:1 on canvas and 1.00:1 on the charcoal card it divides. No accessible boundary token existed and the hairline was not scoped to decoration. |
| P1 | B, D | Slate `#666666`, Iron `#555555` | Both described as secondary/body text tones; both fail AA on canvas and on charcoal. |
| P1 | H | every component | Not one state was named anywhere in the file — 8 of 8 state words absent. |
| P1 | C | elevation ladder | `#000000` → `#181818` → `#202020` separate by 1.18:1, 1.29:1 and 1.09:1. The file called them "elevated sections" without stating that the step is imperceptible on its own. |
| P1 | D | `card-title`, nav label | Card Title had no line height ("—"); the "MENU" label (14px/400) existed only in Navigation prose and in no type role. |
| P1 | E | radius ladder | The radius scale sat as a Layout subsection with no Shapes section, and the 20px switch outlier was unscoped. |
| P2 | E | spacing ladder | Stated base unit is 8px, but the scale carries a parallel 5/10/15/20 run. Real, but unremarked. |
| P2 | J | card border | `border: 0px 1px solid #202020` is a malformed shorthand; the intended value is unverifiable. |
| P2 | I | Agent Prompt Guide | Recommended `#7D7D7D` as body text and `#FFFFFF at 50%` as the generic border, both of which its own values make indefensible on charcoal. |
| P2 | J | headings | Numbered heading variant (`## 1. Visual Theme & Atmosphere`) throughout. |

Counts: 6 P0, 10 P1, 4 P2.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| top of file | no frontmatter -> full YAML block: 30 `colors`, 16 `typography`, 14 `spacing`, 4 `rounded`, 10 `motion`, 20 `components` | Dimension J. Every value is read from the file's own prose; nothing invented except the prescribed `focus` and `motion` values, both labelled as such. |
| `colors.focus` | absent -> `#3866D8`, prescribed | No file in the repo defines a ring. Link Blue `#3860BE` lifted in luminance until it clears 3:1 against all five surfaces *and* the gold accent fill. 4.06:1 against the canvas. |
| `colors.border-strong` | absent as a token -> `#7D7D7D`, the cookie-banner border already in the prose | Parallel accessible boundary beside the frozen 1.29:1 hairline, per SPEC section 2. Extracted, not invented. |
| `colors` naming | prose names only -> `canvas`, `surface-card`, `surface-deep`, `surface-light`, `ink`, `muted`, `on-accent`, `on-light` … | Satisfies the 8 required roles while keeping every brand name in the Colors prose. |
| headings | `## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide` -> unnumbered SPEC set | Section contract. Overview, Colors, Typography, Components, Layout, Elevation & Depth, Do's and Don'ts, Responsive Behavior and Iteration Guide are renamed in place, not rewritten. |
| `## Shapes` | absent -> new section | The Border Radius Scale table was **moved** verbatim out of Layout, with the hexagon/rectangle/1px-line motifs added from the file's own prose. |
| `## Motion & Animation` | absent -> new section, placed immediately after `## Components` | Dimension F. Cinematic block from SPEC section 5 verbatim, 12-row interaction table, `prefers-reduced-motion` CSS rule. First line states the system is prescribed and unmeasured. |
| `## Accessibility` | absent -> new section | 25 key pairs, 11 component pairs, focus-ring ratios on all 6 surfaces, tap targets, reduced motion. Every failure named with its measured ratio. |
| `## Known Gaps` | absent -> new section | 15 entries: what the conversion lost, plus every value genuinely missing from the source. |
| Components section | bare CSS-ish bullets -> each entry names default, hover, focus-visible, active/pressed, and says plainly where disabled / loading / selected / error do not exist | Dimension H. Progress bar and badge are explicitly two-state and one-state. |
| Elevation & Depth | "Level 1 (Surface) … elevated sections" -> same table plus a measured "Layer separation" paragraph | Dimension C. The layers are 1.09–1.29:1 apart; the file now says they are not distinguishable alone and that the boundary is carried by content or `border-strong`. |
| Do's and Don'ts | 20 rules -> 22 | Added: step body copy to `body-soft` on charcoal; draw focus rings in `{colors.focus}`; never animate `width`/`height`/`top`/`left`/`margin`; never use `ink-dark`/`body-muted`/`text-secondary` as body text on dark. |
| Agent Prompt Guide | body text "#7D7D7D", news-card prompt "#7D7D7D at 16px" -> `body-soft` with the failing ratio stated inline | The guide was teaching the one combination the measurements rule out. |
| Typography table | 14 rows -> 15 rows with a token column | Added `nav-label` (14px/400, from Navigation prose). Range and weight-pair handling stated under the table rather than resolved by guesswork. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #FFFFFF / `canvas` #000000 | 21.00:1 | 4.5:1 | Pass |
| `ink` #FFFFFF / `surface-card` #202020 | 16.29:1 | 4.5:1 | Pass |
| `body-soft` #F5F5F5 / `canvas` | 19.26:1 | 4.5:1 | Pass |
| `body-soft` #F5F5F5 / `surface-card` | 14.94:1 | 4.5:1 | Pass |
| `muted` #7D7D7D / `canvas` | 5.10:1 | 4.5:1 | Pass |
| `muted` #7D7D7D / `surface-card` | 3.96:1 | 4.5:1 | **Fail** (disclosed) |
| `text-secondary` #666666 / `canvas` | 3.66:1 | 4.5:1 | **Fail** (disclosed) |
| `text-secondary` #666666 / `surface-card` | 2.84:1 | 4.5:1 | **Fail** (disclosed) |
| `body-muted` #555555 / `canvas` | 2.82:1 | 4.5:1 | **Fail** (disclosed) |
| `body-muted` #555555 / `surface-card` | 2.19:1 | 4.5:1 | **Fail** (disclosed) |
| `ink-dark` #313131 / `canvas` | 1.61:1 | 4.5:1 | **Fail** (disclosed; not harness-counted, see Shared issues) |
| `ink-dark` #313131 / `surface-card` | 1.25:1 | 4.5:1 | **Fail** (disclosed; not harness-counted) |
| `on-accent` #000000 / `accent` #FFC000 | 12.79:1 | 4.5:1 | Pass |
| `on-accent` #000000 / `accent-hover` #917300 | 4.66:1 | 4.5:1 | Pass (thin margin) |
| `accent` #FFC000 / `canvas` | 12.79:1 | 3:1 | Pass |
| `accent-text` #FFCE3E / `canvas` | 14.15:1 | 4.5:1 | Pass |
| `info` #29ABE2 / `canvas` | 8.02:1 | 4.5:1 | Pass |
| `link-hover` #3860BE / `canvas` | 3.58:1 | 4.5:1 | **Fail** (disclosed) |
| `border` #202020 / `canvas` | 1.29:1 | 3:1 | **Fail** (disclosed, scoped to decoration) |
| `border` #202020 / `surface-card` | 1.00:1 | 3:1 | **Fail** (disclosed) |
| `border-strong` #7D7D7D / `canvas` | 5.10:1 | 3:1 | Pass |
| `border-switch` #DDDDDD / `canvas` | 15.46:1 | 3:1 | Pass |
| `on-light` #494949 / `surface-light` #F8F8F8 | 8.48:1 | 4.5:1 | Pass |
| `on-light` #494949 / `surface-light-alt` #E6E6E6 | 7.21:1 | 4.5:1 | Pass |
| `steel` #969696 / `canvas` (disabled label) | 7.10:1 | exempt | Exempt |
| `focus` #3866D8 / `canvas` | 4.06:1 | 3:1 | Pass |
| `focus` #3866D8 / `surface-card` | 3.15:1 | 3:1 | Pass |
| `focus` #3866D8 / `surface-deep` #181818 | 3.43:1 | 3:1 | Pass |
| `focus` #3866D8 / `surface-light` #F8F8F8 | 4.87:1 | 3:1 | Pass |
| `focus` #3866D8 / `surface-light-alt` #E6E6E6 | 4.14:1 | 3:1 | Pass |
| `focus` #3866D8 / `accent` #FFC000 | 3.15:1 | 3:1 | Pass |
| `button-accent` #000000 / #FFC000 | 12.79:1 | 4.5:1 | Pass |
| `button-ghost` #FFFFFF / canvas | 21.00:1 | 4.5:1 | Pass |
| ghost hover #FFFFFF / `action-teal` #1EAEDB | 2.58:1 | 4.5:1 | **Fail** (disclosed) |
| `button-white-filled` #202020 / #FFFFFF | 16.29:1 | 4.5:1 | Pass |
| `button-black-filled` #202020 / #000000 | 1.29:1 | 4.5:1 | **Fail** (disclosed) |
| `button-gray` #202020 / #969696 | 5.51:1 | 4.5:1 | Pass |
| `badge` #FFFFFF / #969696 at 10px | 2.96:1 | 4.5:1 | **Fail** (disclosed) |
| `card-news` #7D7D7D / #202020 at 16px | 3.96:1 | 4.5:1 | **Fail** (disclosed) |
| `footer` #F5F5F5 / #181818 | 16.29:1 | 4.5:1 | Pass |
| `surface-deep` / `canvas` (layer step) | 1.18:1 | — | Not distinguishable |
| `surface-card` / `canvas` (layer step) | 1.29:1 | — | Not distinguishable |
| `surface-card` / `surface-deep` (layer step) | 1.09:1 | — | Not distinguishable |

All ratios computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`; none estimated. Harness after-run: 0 undisclosed failures, 10 disclosed.

### Motion inventory

Prescribed, not extracted. Cinematic profile, SPEC section 5, verbatim.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity`, `background-color` (no transform — brand rule) | Same crossfade, capped at 150ms |
| Press / active | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` only (no scale pop — brand rule) | Unchanged, already under 150ms |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Instant, never suppressed |
| Page / route transition | `{motion.duration-emphasis}` 900ms | `{motion.ease-enter}` | `opacity`, `translateY(24px)`→0 | Travel removed, fade at 150ms |
| Modal / drawer enter | `{motion.duration-slow}` 600ms | `{motion.ease-enter}` | `opacity`, `translateY(32px)`→0 | Travel removed, fade at 150ms |
| Modal / drawer exit | `{motion.duration-base}` 400ms | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed, fade at 150ms |
| Dropdown enter / exit | 400ms / 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(-8px)`→0 | Travel removed, fade at 150ms |
| Toast enter / exit | 400ms / 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(16px)`→0 | Travel removed, fade at 150ms |
| List enter | 400ms, stagger `{motion.stagger-step}` 80ms | `{motion.ease-enter}` | `opacity`, `translateY(16px)`→0 | Stagger and travel removed, one fade at 150ms |
| List exit | 240ms, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed, fade at 150ms |
| Loading | 1600ms infinite | linear | `scaleX()` on the progress bar, `opacity` pulse on the hex pause button | Frozen; static determinate bar remains |
| Hero reveal + continuous slow scale (declared brand ambience) | 900ms reveal | `{motion.ease-enter}` | `opacity`, `scale(1)`→`scale(1.04)` | Ambience frozen at `scale(1)`, video paused on its poster frame |

Exit is shorter than its matching entrance in every row. Only `transform` and `opacity` animate; the harness reports no layout-property animation. One deviation is stated in the file: hover and press carry no transform, because the brand's own Don'ts forbid scale and translate on hover.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, line ~200 (`theme_of`) | A token named `ink-dark` is read as belonging to a *dark theme* and is therefore never compared against the dark canvas, so its 1.61:1 failure is silently skipped. The suffix means "a dark ink", not "the dark theme's ink". Same trap for any `*-dark` ink. | Treat a trailing `-dark`/`-light` as a theme marker only on keys that also match a surface pattern, or require the explicit `on-dark`/`on-light` form for inks, which already has its own branch. |
| `theme-audit/audit.py`, line ~160 / 283 (`find_role`, focus targets) | Naming a light surface `surface-light` removes it from the focus-ring target list via `theme_of`, so a ring can score 5 without ever being measured against the file's light surfaces. Here it happens to pass (4.87:1 and 4.14:1), measured by hand. | Always measure every `focus*` token against every surface key, and use theme scoping only to suppress *ink on surface* pairs. |
| `theme-audit/audit.py`, line ~448 (`sections` score) | A file with zero frontmatter and the numbered heading variant scores 5 on both `refs` and `contrast`, because there are no refs to dangle and no colours to measure. The ten legacy files therefore looked better on two dimensions than converted files do. | Floor `refs` and `contrast` at 1 when `has_frontmatter` is false. |
| `theme-audit/SPEC.md`, section 3 | The section contract has no entry for `Agent Prompt Guide`, which exists in this file and others. It is neither required nor listed as optional, so it reads as an orphan. | Add it to the table as optional, beside `Iteration Guide`. |

### Needs approval

Four extracted values fail AA and were **not** changed. Each is disclosed in the file's Accessibility section with its measured ratio.

1. **`button-black-filled`: text `#202020` on `#000000` — 1.29:1.** Nearest passing value: `#FFFFFF` (21.00:1), or keep the charcoal label and change the fill to `#FFFFFF` (16.29:1), which is what the "Inverted CTA on light sections" usage note implies was meant. Usage note that would make the recorded value defensible: none — there is no size at which 1.29:1 is defensible. This looks like a source transcription error rather than a brand fact.
2. **Ghost button hover: `#FFFFFF` on Teal Action `#1EAEDB` — 2.58:1.** Nearest passing value with the brand's own palette: `{colors.on-accent}` `#000000` on the same teal, 8.13:1. Keeping the white label would need the teal darkened to about `#0E6D8A`, which changes a brand hex. Defensible usage note if the white label stays: the ghost label is 14.4px/300, so no large-text exemption applies — it would need to be 18.66px/700 or larger *and* the ratio would still only need 3:1, which 2.58:1 misses.
3. **`badge`: `#FFFFFF` on Steel `#969696` at 10px — 2.96:1.** Nearest passing value: `#202020` label on the same steel, 5.51:1 (already proven on `button-gray`). Usage note: at 10px there is no large-text exemption, so 4.5:1 applies; the badge is non-interactive metadata, not a control.
4. **Ash `#7D7D7D` as body text on Charcoal `#202020` — 3.96:1 (and the `card-news` component built from it).** Nearest passing value: Smoke `#F5F5F5`, 14.94:1 — the file's own secondary-text tone. Usage note that would make Ash defensible where it must stay: 24px+ or 18.66px+/700, where the 3:1 threshold applies; Ash also passes AA on the pure-black canvas (5.10:1), so restricting it to the canvas is the smaller change. Related, same root: Slate `#666666` (3.66:1 / 2.84:1), Iron `#555555` (2.82:1 / 2.19:1) and Shadow `#313131` (1.61:1 / 1.25:1) are all described as text tones and all fail; they are scoped to decoration in the file, which is a documentation decision an owner should confirm.

Also for approval, because they are additions rather than extractions: **`colors.focus` `#3866D8`** (prescribed; Link Blue lifted in luminance, 4.06:1 on canvas, 3.15:1 on gold) and the whole **`motion:` group** (prescribed Cinematic profile, nothing measured from the live site).

### Identity verdict

Still unmistakably Lamborghini. The file reads as it did — darkness as whitespace, true black over near-black, gold reserved for the single primary CTA, LamboType shouting in uppercase from 120px to 10px, zero radius everywhere except the one 20px switch, hexagonal motifs, and video carrying the emotion while the UI stays infrastructure. The three Overview paragraphs, the Do's and Don'ts and the example prompts are the original prose; tokens were threaded through them rather than over them.

Cinematic is the right profile and I kept it: luxury automotive, full-viewport video heroes, sparse uppercase type, slow reveals — clause 1 of the assignment rule, no argument needed. The one place the profile and the brand conflict is hover: Cinematic's signature is travel and settle, but this file's own Don'ts forbid scale or translate on hover and demand colour-only interaction. I kept the brand rule and documented the deviation in the file, rather than importing a generic hover lift that would have made the system feel like a borrowed one. The additions that are genuinely not from the brand — the focus ring and all motion values — are labelled prescribed at the point of use, so a reader can tell brand fact from audit prescription.

The one place where identity is now *more* honest than before: the Agent Prompt Guide used to teach `#7D7D7D` body text on charcoal cards, which the brand's own palette cannot support. It now teaches Smoke on charcoal and states the failing ratio inline. That is a correction to the documentation, not a change to the brand.

### What the conversion could not recover

The legacy format cost this file its vocabulary and its state machine, and neither can be rebuilt from the prose. Every token key above is a name I invented to carry an extracted hex: the source said "Charcoal", "Dark Iron", "Smoke", "Ash", so whatever the brand's own token names are, they are gone, and a future reader cannot tell `surface-card` from what Lamborghini calls that colour. The same applies to component geometry — the prose gave a background and a text colour for most components and nothing else, so heights, gaps, border widths, icon sizes and the second half of every weight pair and letter-spacing range (400/700, 300/500, 0.14–0.2px, line-height 1.14–1.50) are absent rather than approximated; the token carries the first or lower value and Known Gaps records the rule that selects the other as unknown. Two type roles have no line height at all, one of them (`nav-label`) existing only because a Navigation bullet happened to mention "14px weight 400". Interaction state was never documented: hover for two buttons and a broken focus style for one is the whole of it, so disabled, loading, selected and error are recorded per component as "not documented on the live site" rather than filled in. And one extracted value is self-contradictory beyond repair — bg `#000000` with text `#202020` — which the conversion can only preserve and flag, since inventing the intended colour would be the same falsification as fixing a brand hex. Nothing was measured from the live site in the first place, so the motion system, the focus ring, and the claim that the black canvas is `#000000` rather than something imperceptibly off it are all as trustworthy as the original document and no more.
