## A27 · ibm

Scores before -> after (1-5), from the harness: tokens 2 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

Harness after: `ibm 5 5 5 5 5 5 (disclosed:6)`, zero undisclosed contrast failures, zero dangling refs, zero layout-animating properties.

Note on the run: `theme-audit/audit.py` was amended during this review (commit `e360abd`, "judge the focus-ring system, not each ring in isolation" — a working-tree change, not yet committed at the time of my first run). My first after-run reported 7 disclosed failures including `focus on primary` at 1.0:1; the amended harness recognises the composite `focus-inset` band and no longer raises that pair, so the count is 6. Both runs score 5/5/5/5/5/5. The 1.0:1 fact is still stated in the file's Accessibility section, since it is true and a reader needs it.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Nothing in the file said how anything moves. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Four real contrast failures were present and undisclosed. |
| P0 | A Tokens | `colors.focus` | No focus token, although the Elevation table already specified the ring ("2px `{colors.primary}` outline + 1px `{colors.hairline-strong}` underline") and the Colors section already listed "focus rings" as a use of IBM Blue. The ring was described but not tokenised, so nothing could reference it. |
| P0 | A Tokens | `colors.surface`, `colors.text-dim` | Roles unsatisfied. The file's `surface-1` and `ink-muted` do the jobs, but neither name matches the SPEC role patterns, so the raised-surface and secondary-text roles resolved to nothing. |
| P0 | H States | every component | 18 component entries, not one naming its states. `focus-visible`, `active`, `disabled` and `loading` appeared nowhere in the file. The gap was worst on `text-input`, which has three frontmatter variants and documented none of their triggers. |
| P1 | B Colour | `colors.hairline` #e0e0e0 | 1.32:1 on canvas, 1.2:1 on `surface`. The file used it as the 1px boundary of cards, inputs and logo tiles — i.e. as the only boundary of interactive controls — with no note that it fails the 3:1 non-text minimum. Extracted Carbon value, so frozen. |
| P1 | B Colour | `colors.ink-subtle` #8c8c8c | 3.36:1 on canvas, 3.06:1 on `surface`, against 4.5:1. Documented for "disabled, helper text, captions" — the first is exempt, the other two are a plain AA failure at 12-14px. |
| P1 | B Colour | `colors.semantic-success`, `colors.semantic-warning` | 3.35:1 and 1.68:1 on canvas. Real Carbon green-50 and yellow-30, used as fills, but the file gave no usage scope, so they read as text colours. |
| P1 | B Colour | `colors.focus` on `colors.primary` | 1.0:1 — the ring and the primary-button fill are the same #0f62fe. A ring on IBM's own primary CTA is invisible without a separating band. This is the one case where the brand's single-accent rule actively breaks focus visibility. |
| P2 | A Tokens | focus on the inverted footer | `{colors.focus}` #0f62fe on `{colors.inverse-canvas}` #161616 measures 3.62:1, so it does clear 3:1 — but at the floor, and Carbon publishes `$focus-inverse` white for exactly this surface. The file documents a charcoal footer, so it now defines `focus-on-dark` (18.1:1) rather than running the blue ring at its limit. |
| P2 | E Ladders | `rounded.md` 6px, `rounded.lg` 8px | Both documented as "(Used rarely; documented for completeness)" and the file's own Don'ts say even 4px breaks the Carbon look. Dead rungs, but they are honestly labelled, so left alone. |
| P2 | E Ladders | `rounded.pill` / `rounded.full` | Two keys, same 9999px value, no distinction drawn in prose. Left alone: removing one risks a dangling ref in another consumer. |
| P2 | D Typography | `typography.button` / `eyebrow` | Byte-identical (14px/400/1.29/0.16px). Defensible as two semantic names, but nothing in the file says why both exist. |
| P2 | C Elevation | Elevation table | Levels 0-2 are consistent (no shadow anywhere; depth is hairline + surface change only), which is correct for Carbon. But the canvas->surface-1 step is 1.1:1 and surface-1->surface-2 is 1.2:1: the layers are *technically* distinguishable and nothing more. Not fixable without falsifying Carbon's greys; recorded here. |
| P2 | D Typography | weight 300 | Every display role runs weight 300, which is the brand signature, but the file never warned against taking 300 down to body sizes where light strokes thin out. Added as an Accessibility note. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `text-secondary: "#525252"` | Satisfies the `text-dim` role. Same value as `ink-muted`; `$text-secondary` is Carbon's own name for it, so this is an alias, not a new colour. |
| frontmatter `colors:` | — -> `surface: "#f4f4f4"` | Satisfies the `surface` role. Same value as `surface-1`, which Carbon calls `layer-01`. Alias, not a new colour. |
| frontmatter `colors:` | — -> `focus: "#0f62fe"`, `focus-inset: "#ffffff"`, `focus-on-dark: "#ffffff"` | Tokenises the ring the file already described. Carbon's published `$focus` / `$focus-inset` / `$focus-inverse`. Two polarities because the file documents a charcoal footer, per SPEC section 1. |
| frontmatter | — -> `motion:` group, Calm block verbatim from SPEC section 5 | No deviations from the profile block. |
| `## Colors` → Surface | hairline bullet rewritten | Scopes `hairline` to decoration and names `hairline-strong` as the control boundary, with both measured ratios. |
| `## Colors` → Text | ink-subtle bullet rewritten | Scopes it to disabled and decorative use; points readable helper text at `ink-muted` at 7.81:1. States the AA failure in place. |
| `## Colors` | — -> `### Focus` subsection | Documents the three focus tokens with measured ratios per surface. First line says these are Carbon's published values, recorded in this file's own prose, not invented. |
| `## Colors` → Semantic | success / warning bullets rewritten | Scopes both to fills and icons, with measured ratios and the `{colors.ink}`-on-yellow pairing at 10.75:1. |
| `## Elevation & Depth` level 3 | `2px {colors.primary} outline + 1px {colors.hairline-strong} underline` -> `2px {colors.focus} outline + 1px {colors.focus-inset} inner band; focused inputs keep the {colors.hairline-strong} underline` | Points at the focus tokens, and adds the inner band the blue-on-blue case needs. |
| `## Components`, 17 entries | — -> one `States:` line per entry | SPEC section 7. Components with genuinely few states say so: `hero-card` is default-only, `product-card` is three plus focus, `utility-bar` links are three. |
| `## Components` → feature-card | `Stroked with 1px {colors.hairline}` -> hairline-strong where the tile is a link target | A link tile's only boundary cannot be a 1.32:1 rule. |
| after `## Components` | — -> `## Motion & Animation` | Calm profile. First line states the system is prescribed and was not measured from the live site. Eleven-row inventory, rules, and a `prefers-reduced-motion` block naming what is removed and what remains. |
| after Motion | — -> `## Accessibility` | Measured passes, seven disclosed real failures with ratios, focus ring per surface, tap targets (labelled prescribed), reduced motion. |
| `## Do's and Don'ts` | — -> 3 Don'ts | No layout-property animation; no `ink-subtle` for read text; no bare focus ring on the blue fill. |
| `## Known Gaps` | — -> 4 bullets | Motion is prescribed; focus values are Carbon-published but their per-page application is unverified; `button-danger` hover/pressed hexes were not extracted; nothing here was rendered, so no tap-target or overlap claim is measured. |

Nothing was reflowed. No extracted hex was altered, added or removed — the two new non-focus tokens duplicate values already in the file under Carbon's own names.

### Contrast checks

All computed with WCAG 2.1 relative luminance via `python3 -I`, never estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #161616 / canvas #ffffff | 18.1:1 | 4.5:1 | Pass |
| ink / surface #f4f4f4 | 16.45:1 | 4.5:1 | Pass |
| ink / surface-2 #e0e0e0 | 13.71:1 | 4.5:1 | Pass |
| ink-muted = text-secondary #525252 / canvas | 7.81:1 | 4.5:1 | Pass |
| ink-muted / surface | 7.1:1 | 4.5:1 | Pass |
| ink-muted / surface-2 | 5.92:1 | 4.5:1 | Pass |
| ink-subtle #8c8c8c / canvas | 3.36:1 | 4.5:1 | **Fail — disclosed** |
| ink-subtle / surface | 3.06:1 | 4.5:1 | **Fail — disclosed** |
| on-primary #ffffff / primary #0f62fe | 5.0:1 | 4.5:1 | Pass |
| on-primary / blue-hover #0050e6 | 6.38:1 | 4.5:1 | Pass |
| on-primary / blue-60 #0043ce | 7.79:1 | 4.5:1 | Pass |
| on-primary / blue-80 #002d9c | 11.32:1 | 4.5:1 | Pass |
| on-primary / semantic-error #da1e28 | 5.0:1 | 4.5:1 | Pass |
| hairline #e0e0e0 / canvas | 1.32:1 | 3.0:1 | **Fail — disclosed** |
| hairline / surface | 1.2:1 | 3.0:1 | **Fail — disclosed** |
| hairline-strong #161616 / canvas | 18.1:1 | 3.0:1 | Pass |
| focus #0f62fe / canvas | 5.0:1 | 3.0:1 | Pass |
| focus / surface | 4.55:1 | 3.0:1 | Pass |
| focus / surface-2 | 3.79:1 | 3.0:1 | Pass |
| focus / primary #0f62fe | 1.0:1 | 3.0:1 | Fail bare — disclosed; composite ring required, and accepted as such by the amended harness |
| focus-inset #ffffff / focus #0f62fe | 5.0:1 | 3.0:1 | Pass (band separation) |
| focus-on-dark #ffffff / inverse-canvas #161616 | 18.1:1 | 3.0:1 | Pass |
| focus-on-dark / inverse-surface-1 #262626 | 15.13:1 | 3.0:1 | Pass |
| focus #0f62fe / inverse-canvas #161616 | 3.62:1 | 3.0:1 | Pass, but at the floor — focus-on-dark is used there instead |
| inverse-ink #ffffff / inverse-canvas | 18.1:1 | 4.5:1 | Pass |
| inverse-ink-muted #c6c6c6 / inverse-canvas | 10.59:1 | 4.5:1 | Pass |
| inverse-ink-muted / inverse-surface-1 | 8.86:1 | 4.5:1 | Pass |
| semantic-error #da1e28 / canvas | 5.0:1 | 4.5:1 | Pass |
| semantic-info #0f62fe / canvas | 5.0:1 | 4.5:1 | Pass |
| semantic-success #24a148 / canvas | 3.35:1 | 4.5:1 | **Fail — disclosed, fill-only** |
| semantic-warning #f1c21b / canvas | 1.68:1 | 4.5:1 | **Fail — disclosed, fill-only** |
| ink #161616 / semantic-warning #f1c21b | 10.75:1 | 4.5:1 | Pass — the pairing warning is actually used in |
| canvas / surface (elevation step) | 1.1:1 | — | Layers barely separate; extracted, unchanged |
| surface / surface-2 (elevation step) | 1.2:1 | — | Same |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | opacity, background-color | Unchanged — colour change is not travel |
| Press / active | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | background-color | Unchanged; no scale pop |
| Focus-visible ring | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | opacity | Ring appears instantly at full opacity |
| Page / route transition | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | opacity | Opacity only at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | opacity, translateY 8px -> 0 | Travel removed; fade at 150ms |
| Modal / drawer exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | opacity, transform | Travel removed; fade at 150ms |
| Dropdown / nav flyout | 150ms enter / 80ms exit | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity, translateY -4px -> 0 | Travel removed; opacity only |
| Toast / inline notification | 250ms enter / 150ms exit | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity, translateX 12px -> 0 | Travel removed; fade at 150ms |
| List / card grid enter | 250ms, stagger `{motion.stagger-step}` 40ms | `{motion.ease-enter}` | opacity, translateY 8px -> 0 | Stagger and travel removed; grid fades as one block at 150ms |
| List / card grid exit | 150ms, no stagger | `{motion.ease-exit}` | opacity | Opacity only at 150ms |
| Loading (spinner, skeleton) | 1400ms loop / `{motion.duration-slow}` 400ms loop | linear | rotate, opacity | Spinner freezes to a static ring; skeleton holds a flat band; status announced in text |

Exit is shorter than entrance in every pair. Only `transform` and `opacity` animate. The two infinite animations are the loaders and the customer-logo marquee, declared as deliberate ambience and frozen under reduced motion.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, line 23 (`REQUIRED_COLOR_ROLES["surface"]`) | The pattern list accepts `surface-cream`, `surface-mid`, `surface-deep` and so on, but not a numeric ladder. Carbon, Material and Primer all number their layers (`layer-01`, `surface-1`), so a file using the real vendor naming scores 0 on the surface role while a file inventing `surface-soft` scores 5. I worked around it with an alias token; three or four other sites likely have the same false negative. | Add `r"^surface-\d"` and `r"^layer-\d"` to the `surface` pattern list. |
| `theme-audit/audit.py`, line 26 (`REQUIRED_COLOR_ROLES["text-dim"]`) | Same shape of problem. `^ink-` is in the **text** list, so `ink-muted` and `ink-subtle` are both judged at 4.5:1 as primary text, while the `text-dim` role goes unfilled. The effect is double: a secondary-ink file loses the role *and* gains a manufactured primary-text failure for its legitimately dimmer tone. | Add `r"^ink-(muted|subtle|soft|secondary|tertiary)$"` to `text-dim`, and have the `text` patterns stop at `^ink$` plus `^ink-(primary|strong)$`. |
| `theme-audit/audit.py`, focus-ring loop | **Already fixed upstream during this review** (`e360abd`). The loop used to measure every `^focus` token against the accent fill with no notion that a composite ring is the standard answer when ring and fill share a hue, so a file could only clear it by disclosing a 1.0:1 "failure" that is not one in implementation. The amended harness judges the ring system. No action needed; recorded because my first after-run predates it. | — |
| `theme-audit/SPEC.md`, section 2 table | The table lists six pairs, but `audit.py` also checks `border` on `surface`, `text` on `surface` for all tones, and every semantic tone as text on the canvas. Agents sizing their Accessibility section from the SPEC table alone will under-disclose and lose contrast points for failures they were never told to look for. | List the all-tones and semantic checks in the section 2 table. |

### Needs approval

Four real, extracted Carbon values fail WCAG and are disclosed rather than changed. Each needs a decision from whoever owns this document; none is actionable inside the file.

1. **`colors.hairline` #e0e0e0 at 1.32:1 on canvas, 1.2:1 on surface.** Nearest passing value for a 3:1 boundary is #949494 (3.03:1 on white); Carbon's own `$border-strong-01` #8d8d8d reaches only 3.32:1 on white and 3.02:1 on #f4f4f4, so even Carbon's strong border is marginal on the grey band. Usage note that makes #e0e0e0 defensible: it is decoration — a visual separator between two already-distinguished regions — and the 1.4.11 3:1 threshold applies to boundaries required to identify a control. Where a 1px rule *is* the only boundary of an input or a link tile, the file now routes to `hairline-strong`. Approval needed on whether IBM's real marketing cards, which use #e0e0e0 as their sole boundary, should be documented as non-conformant or re-specified.
2. **`colors.ink-subtle` #8c8c8c at 3.36:1 on canvas.** Nearest passing value is #767676 (4.54:1 on white); Carbon's `$text-helper` #6f6f6f reaches 5.02:1 and would pass. Usage note: 3:1 applies at 18.66px/700 or 24px/400, and `ink-subtle` is documented at `caption` 12px and `body-sm` 14px, so no size relief is available. The real brand fails AA for helper text. Approval needed on swapping helper and caption text to #6f6f6f, which is a genuine Carbon token and would pass, rather than leaving the documented failure.
3. **`colors.semantic-success` #24a148 at 3.35:1 and `colors.semantic-warning` #f1c21b at 1.68:1 on canvas.** Nearest passing green is Carbon's own `green-60` #198038 at 5.02:1. There is no passing text form of yellow-30 on white at any weight. Usage note: both are fills and icon colours; 1.4.3 does not apply to a fill, and 1.4.11 is met because the shapes carry `{colors.ink}` type and a 1px boundary. Approval needed on adding `green-60` as a prescribed success-text token — I did not add it, since it is a new hex and nothing in the file's own prose records it.
4. **`colors.focus` #0f62fe on `colors.primary` #0f62fe at 1.0:1.** There is exactly one passing single-colour answer, and it is already in the palette: `{colors.hairline-strong}` #161616 clears 3:1 against every surface this file defines — 18.1:1 on canvas, 16.45:1 on surface, 13.71:1 on surface-2 and 3.62:1 on the blue fill. I searched the full luminance range: the best achievable minimum across those four surfaces is 4.2:1, reached only at black, so no mid-tone and no lighter blue works. I did not adopt the charcoal ring, because Carbon publishes `$focus` as #0f62fe and this file's own prose already records IBM Blue as the focus colour; switching the ring to charcoal would be a design change, not an audit fix. I used Carbon's composite form instead (2px `{colors.focus}` ring, 1px `{colors.focus-inset}` white band, 5.0:1 between bands). Approval needed on the choice: composite blue ring as documented, or the charcoal single ring. The amended harness (`e360abd`) now accepts the composite form, so this is a design question rather than a scoring one.

Also for approval, lower stakes: the two alias tokens (`surface`, `text-secondary`) duplicate `surface-1` and `ink-muted`. They exist to satisfy the SPEC role contract against a harness that does not read Carbon's numeric layer naming. If the harness patterns are fixed as proposed above, both aliases should be deleted.

### Identity verdict

Still unmistakably IBM, and the additions sharpened the identity rather than diluting it.

The brand's own rules did the work. The focus ring is IBM Blue because the file already said IBM Blue marks focus — I tokenised a value the document had written out in prose, not invented one. The ring is 2px square with a 1px offset, consistent with a system whose first rule is 0px corners. The composite inner band exists because a single-accent brand puts its ring on its own accent fill, which is a consequence of IBM's restraint, not a generic accessibility bolt-on. No second brand colour entered the palette.

On the Calm assignment: **correct, and I kept it.** Checked against SPEC section 5's ordered rule: not luxury or automotive (rule 1); not a terminal or IDE identity — ibm.com marketing is enterprise marketing, and Carbon's product surfaces are explicitly out of scope in this file's Known Gaps, so rule 2 does not fire; not saturated or illustration-led, since the file documents exactly one chromatic accent and forbids a second (rule 3). Falls to rule 4, Calm. The section 3 tie-breaker also points here independently: the file's own description is "deliberately flat-square", its display weight is 300, and it forbids gradients and shadows. Crisp was the only real alternative and it is wrong for a 76px weight-300 editorial hero — Crisp's signature is "no entrance choreography", and the file does document a soft blue hero gradient and a scroll-triggered feature row. Calm's 250ms base with symmetric easing fits a page that wants to settle.

One thing the motion section deliberately does not do: no scale on press. Playful's small pop would read as wrong on square corners, and Calm's "little travel" gave the right instruction. The `{motion.duration-emphasis}` 500ms rung is used once, on a scroll-triggered feature row, and nowhere on load.

The risk of drift is in the States lines, which are the most generic prose added. They are anchored by naming this file's own tokens in every state (`{colors.blue-80}` for pressed, `{colors.surface}` for hover, `{colors.focus-on-dark}` only at the footer) rather than describing states abstractly, and several entries say plainly that a component has three states or one. Nothing was borrowed from another file in the collection.
