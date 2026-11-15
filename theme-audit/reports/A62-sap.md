## A62 · sap

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 3 | 5 | 3 | 1 | 1 | 1 |
| after | 4 | 5 | 5 | 5 | 5 | 5 |

`tokens` stops at 4 deliberately: the `text-dim` role is reported unsatisfied by a regex miss, not by a missing tone, and no alias was added to buy the point. See Shared issues.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule. Nothing in the file spoke about time at all. Fixed. |
| P0 | G Accessibility | whole file | No `## Accessibility` section; no contrast ratio stated anywhere; no focus indicator defined for any surface, including the two dark hero grounds. Fixed. |
| P0 | A Token contract | `colors.focus` | Absent. A keyboard user had no documented indicator on a palette that spans #ffffff to #022879. Fixed with two rings, both reusing existing tones. |
| P1 | C Section contract | `## Responsive Behavior` | Existed only as `### Responsive Strategy` inside Layout. Moved verbatim to a top-level section after Do's and Don'ts, child headings promoted `####` → `###`. Not duplicated. |
| P1 | C Section contract | `## Known Gaps` | Absent, so six real absences (no shadow value, no gradient stops, no status palette, no extracted states, no extracted motion, no rendered verification) were undocumented. Fixed. |
| P1 | H States | all components | Only `active` and `selected` were countable; the file opened the Components section with "No hover states documented." Added a prescribed, clearly labelled state matrix covering all eight state words, with genuinely-one-state surfaces named as such. |
| P1 | A/C Harness | `surface` role | Resolves only through a component binding, to `chrome`… it does **not**. It resolves to `primary-deep`, via `hero-band`. See the note below — this is a harness bug, and it manufactured both contrast failures. |
| P2 | B Colour | `{colors.primary}` on `{colors.sky}` / on `{colors.ink}` | 3.22:1 and 3.29:1 — above the 3:1 non-text floor, below 4.5:1. Both grounds correctly bind a different ink, but nothing in the file said "do not set blue type here". Now stated in Accessibility. |
| P2 | E Ladders | `spacing` | 2 · 3 · 8 · 9 · 10 · 12 · 15 · 16 · 20 · 24 · 32 · 40 · 48 · 56 · 72 is not an 8px ladder, despite the Layout section calling 8px the base unit. Left as extracted — these are measured paddings, and smoothing them would falsify the capture. Noted here only. |
| P2 | D Typography | all roles | Every one of the twelve roles carries family, size, weight, line height and letter spacing. No gap. Body at 18px/27px in `{colors.ink-body}` reads 12.57:1 on canvas and 11.57–11.62:1 on all four bands. No finding. |
| P2 | E Radius | `rounded` | 0 · 4 · 8 · 12 is a clean ladder and every value is used by a documented component. Elevation is expressed one way throughout — flat band, never shadow-and-border mixed. No finding. |

#### The `surface` role, checked

Asked to confirm: the `surface` role here resolves **only** through a component binding, and it binds to **`primary-deep`, not `chrome`**. The harness's `CONTAINERISH` regex matches `hero-band` on the substring "band", and `hero-band` is the first such component in document order, so `surface = primary-deep` (#0040b0).

That is **not** this file's card or panel surface. `primary-deep` is the flat 450px hero band on interior pages and the label colour of an outline button — a hero fill. This system's card and panel surface is `{colors.canvas}` #ffffff: the Overview states that content panes, cards and most sections sit on it unchanged, and eighteen of the twenty-six brand-native components bind `{colors.canvas}` as their background. Its genuinely *raised* neutral surfaces are `{colors.chrome}` #f5f6f7 (nav bar, `band-neutral`) and `{colors.band}` #eaecee (footer). Either of those would be a defensible representative; `primary-deep` is not.

The consequence is not cosmetic: every contrast failure the harness reported for this site is a pair measured against the hero band — `hairline on primary-deep` 1.32:1 and `ink on primary-deep` 2.36:1 — and the site renders neither. Both are disclosed in the file anyway, with the explanation.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| `colors:` (after `hairline`) | — -> `focus: "#0057d2"`, `focus-on-dark: "#ffffff"` | The file had no addressable focus ring. Both values are tones the palette already owns (`primary`, `on-primary`); one ring cannot serve both a white canvas and a #022879 hero, so the file gets the two-polarity pair SPEC §1 prescribes. |
| frontmatter, between `spacing:` and `components:` | — -> `motion:` group | The **Calm** profile block from SPEC §5, carried verbatim, no deviation. |
| `## Components`, opening blockquote | "No hover states documented. Every component below documents its default state only." -> "No interaction states were extracted from the live site… The state matrix at the end of this section is **prescribed**." | Keeps the extracted fact while pointing at the new matrix, so a reader cannot mistake prescription for capture. |
| end of `## Components` | — -> `### Interaction States (prescribed)`, 18-row matrix | Brief H. Every row is built from tokens already in the file; nothing new was introduced. `product-tab-active` is named as a one-state variant, and fifteen type roles and grounds are named as single-state by design. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the visual identity and was not measured. 14-row interaction × duration × easing × property × reduced-motion table covering hover, press, focus, page transition, modal/drawer, dropdown, toast, list enter, list exit, loading, plus a hero reveal. `transform` and `opacity` only; every exit shorter than its entrance; `@media (prefers-reduced-motion: reduce)` block names what is removed and what remains. |
| after Motion | — -> `## Accessibility` | 17-pair measured contrast table, a disclosed-failures table for the two hero-band pairs, per-surface focus-ring ratios with the 2px offset stated, declared tap-target heights flagged as declared rather than measured, and the reduced-motion summary. |
| `## Layout` -> after `## Do's and Don'ts` | `### Responsive Strategy` (with `#### Breakpoints` …) -> `## Responsive Behavior` (with `### Breakpoints` …) | SPEC §3 requires it top-level and in that position. Moved verbatim, children promoted one level, not duplicated. |
| end of file | — -> `## Known Gaps` | Eight entries, including the `text-dim` naming question, the absent status palette and the un-tokenised gradients. |

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`, from this file's own hexes.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #000000 / canvas #ffffff | 21.0:1 | 4.5:1 | Pass |
| ink-lead #3c3c3c / canvas | 11.03:1 | 4.5:1 | Pass |
| ink-body #223548 / canvas | 12.57:1 | 4.5:1 | Pass |
| ink-list #354a5f / canvas | 9.15:1 | 4.5:1 | Pass |
| ink-meta #475e75 / canvas | 6.72:1 | 4.5:1 | Pass |
| ink-nav #545454 / canvas | 7.57:1 | 4.5:1 | Pass |
| ink-nav / chrome #f5f6f7 | 7.0:1 | 4.5:1 | Pass |
| ink-nav / band #eaecee | 6.39:1 | 4.5:1 | Pass |
| ink-body / chrome | 11.62:1 | 4.5:1 | Pass |
| ink-body / band-blue #ebf8ff | 11.61:1 | 4.5:1 | Pass |
| ink-body / band-lavender #f7f4ff | 11.57:1 | 4.5:1 | Pass |
| ink / sky #6bc0ff | 10.61:1 | 4.5:1 | Pass |
| on-primary #ffffff / primary #0057d2 | 6.38:1 | 4.5:1 | Pass |
| on-primary / primary-deep #0040b0 | 8.9:1 | 4.5:1 | Pass |
| on-primary / navy #022879 | 13.27:1 | 4.5:1 | Pass |
| on-primary / ink | 21.0:1 | 4.5:1 | Pass |
| primary / canvas | 6.38:1 | 4.5:1 | Pass |
| primary-deep / canvas | 8.9:1 | 4.5:1 | Pass |
| hairline #475e75 / canvas | 6.72:1 | 3.0:1 | Pass |
| hairline / chrome | 6.21:1 | 3.0:1 | Pass |
| ink-meta / band | 5.67:1 | 4.5:1 | Pass |
| focus #0057d2 / canvas | 6.38:1 | 3.0:1 | Pass |
| focus / chrome | 5.89:1 | 3.0:1 | Pass |
| focus / band | 5.38:1 | 3.0:1 | Pass |
| focus / band-blue | 5.89:1 | 3.0:1 | Pass |
| focus / band-lavender | 5.87:1 | 3.0:1 | Pass |
| focus / sky | 3.22:1 | 3.0:1 | Pass |
| focus / ink | 3.29:1 | 3.0:1 | Pass |
| focus-on-dark #ffffff / primary-deep | 8.9:1 | 3.0:1 | Pass |
| focus-on-dark / navy | 13.27:1 | 3.0:1 | Pass |
| focus-on-dark / primary (ring outside a blue control) | 6.38:1 | 3.0:1 | Pass |
| primary / sky (as type) | 3.22:1 | 4.5:1 | Fail — not a bound pair; `sky-panel` binds ink. Now forbidden in prose. |
| primary / ink (as type) | 3.29:1 | 4.5:1 | Fail — not a bound pair; `ex-pricing-tier-featured` binds on-primary. Now forbidden in prose. |
| hairline / primary-deep | 1.32:1 | 3.0:1 | Fail — harness-derived pair, not rendered. Disclosed. |
| ink / primary-deep | 2.36:1 | 4.5:1 | Fail — harness-derived pair, not rendered. Disclosed. |

Elevation layers (brief C): canvas→chrome 1.08:1, canvas→band 1.18:1, chrome→band 1.09:1. The neutral layers are **not** distinguishable by luminance alone — which is correct for this system and is the point of it. Separation comes from full-bleed extent and the white interval between zones, not from a step in value; nothing is bordered and nothing is elevated, so there is no boundary for a 3:1 threshold to apply to. Elevation is expressed one consistent way (flat band, then solid colour band, then gradient), with shadow appearing only inside depicted interfaces.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover — button, link, list item, nav link | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity` of a primary tint overlay | Fade kept at `{motion.duration-reduced}` |
| Press — button, tab | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` step; no scale | Opacity step at `{motion.duration-reduced}` |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the focus ring | Appears at `{motion.duration-reduced}`, no scale |
| Page / route transition | `{motion.duration-base}` 250ms | `{motion.ease-standard}` | `opacity` of the content pane; chrome never animates | Cross-fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `translateY(8px → 0)` | Travel removed, fade at `{motion.duration-reduced}` |
| Modal / drawer exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `translateY(0 → 8px)` | Travel removed, fade at `{motion.duration-reduced}` |
| Dropdown enter | `{motion.duration-fast}` | `{motion.ease-enter}` | `opacity` + `translateY(4px → 0)` | Travel removed, fade at `{motion.duration-reduced}` |
| Dropdown exit | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-reduced}` |
| Toast enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity` + `translateY(12px → 0)` | Travel removed, fade at `{motion.duration-reduced}` |
| Toast exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `translateY(0 → 12px)` | Travel removed, fade at `{motion.duration-reduced}` |
| List enter | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `{motion.stagger-step}` 40ms per item | Stagger dropped, one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity`, no stagger | Fade at `{motion.duration-reduced}` |
| Loading | `{motion.duration-slow}` 400ms, looped | `{motion.ease-standard}` | `opacity` pulse on a band placeholder; indeterminate bar uses `translateX` | Loop and travel removed; static fill, `aria-busy` |
| Hero reveal | `{motion.duration-emphasis}` 500ms | `{motion.ease-enter}` | `opacity`, started after first paint | Removed; type renders at full opacity |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 28-31, `REQUIRED_COLOR_ROLES["text-dim"]` | SAP plainly owns a muted tier — four tones, documented as lead, list, caption and chrome ink, with `ink-meta` described in the file as "the quietest legible tier" — but no pattern matches `ink-meta`, `ink-list`, `ink-lead` or `ink-nav`. The role is reported missing and the site loses a token point. No alias was added; the palette's naming is already explicit about what each tier does, and a token existing only to match a regex would be worse than a 4. | Extend the pattern list with `r"^ink-(meta|note|caption|nav|list|lead)$"`. `^caption$` is already there, so capturing the same role under an `ink-` prefix is consistent with existing intent. |
| `theme-audit/audit.py` line 217-230, `CONTAINERISH` surface fallback | The regex matches `hero-band` on "band" and takes the first match in document order, so this file's `surface` resolves to `primary-deep` — a 450px hero fill — rather than to `chrome` or `band`, which are its actual raised panel surfaces, or `canvas`, which is its card ground. Both contrast failures reported for this site are pairs against that hero fill and neither renders on the real site. | Two options, either sufficient: (a) exclude `hero|display|title` from `CONTAINERISH`, since a hero band is a page region, not a raised surface; (b) where several containerish bindings exist, prefer the one with the lowest contrast against the canvas — a raised neutral layer is near its floor, a hero fill is far from it. (b) generalises better across the collection. |
| `theme-audit/audit.py` line 532, `threshold_for` | Reads only `fontSize`/`fontWeight`, so `{typography.lead}` at 28px/400 correctly gets 3:1, but a 19px/700 role would be judged at 4.5:1 when WCAG's large-text rule (18.66px + bold) applies. Not triggered by this file; both of its ≥18.66px bold roles clear 4.5:1 anyway. | Already handled in the code; noting only that the px threshold is applied before the weight check, which reads correctly. No change needed for this site. |

### Needs approval

1. **`{colors.hairline}` is bound as a boundary at 6.72:1 on canvas and passes — but it is the same hex as `{colors.ink-meta}`.** The file documents this ("The same value as `{colors.ink-meta}`, used as a border rather than as type"). This is an observation, not a failure: no re-binding is proposed and the extracted bindings for `button-outline`, `ex-pricing-tier`, `ex-cart-drawer` and `ex-data-table-cell` stay exactly as captured. Flagged only so a brand owner knows the boundary tone and the caption tone are one value, which forecloses ever darkening one without the other.
2. **Two rings, prescribed.** `{colors.focus}` = `{colors.primary}` #0057d2 and `{colors.focus-on-dark}` = `{colors.on-primary}` #ffffff, 2px at 2px offset. No new hex. Needs a brand owner's confirmation that reusing the one acting colour as the ring is acceptable, given the file's own rule that `{colors.primary}` is reserved for things that act — a focus ring arguably is one. If not, the nearest alternative that clears 3:1 on every light ground is `{colors.navy}` #022879 (canvas 13.27:1, sky 6.71:1), which costs the ring its association with action.
3. **No status palette.** `ex-auth-form-card`'s error state is marked structurally and by text because the brand owns no red. A real SAP error red almost certainly exists in Fiori but was not captured here, and inventing one would falsify the document. Needs an extraction pass or a brand owner's value.
4. **Prescribed state matrix.** Eighteen rows of interaction states, none extracted. The treatments are plausible and token-consistent, but they are proposals. A capture of the live site's hover, focus and loading behaviour would replace them.
5. **Blue type is now forbidden on `{colors.sky}` (3.22:1) and `{colors.ink}` (3.29:1).** Both clear the 3:1 non-text minimum, so the usage note that makes them defensible is: these values are legitimate for the focus ring and for non-text boundaries, and for text only at 24px+ or 18.66px+ bold, where 3:1 applies. No binding in the file uses blue type on either ground today. The nearest passing value for blue-as-text on `{colors.sky}` is `{colors.navy}` #022879 at 6.71:1.

### Identity verdict

Still unmistakably SAP, and the additions lean on the file's own logic rather than importing a house style. The focus ring reuses the one acting colour; the dark-polarity ring reuses the one on-accent white; the motion table refuses scale on press and keeps the two-storey chrome static through route changes, because this document's own thesis is that the page is the content pane of an application frame and the frame does not move. The reduced-motion rule has almost nothing to strip, which is itself a fair description of the brand. The state matrix names fifteen grounds and type roles as genuinely single-state instead of inventing hovers for them, and the error treatment is structural because the palette has no red — an invented red would have been the single fastest way to make this file read like any other enterprise token dump.

**Profile: Calm is correct, but it is a near miss with Crisp and worth stating why.** SAP is enterprise software, and SPEC §5 rule 2 routes "terminal, IDE, infra or developer-tool identity" to Crisp. What this file documents, though, is not the Fiori application shell — it is the public web surface: three marketing templates, a 57px/700 display headline, a 450px hero band, full-bleed navy gradient, composited product illustrations with dotted connector lines. Rule 2 is a conjunction and this fails it: no terminal, no IDE, no developer audience. Rule 1 fails (no luxury or hardware-flagship identity), rule 3 fails hard (one acting colour, zero saturated interactive surfaces, no illustration-led informality, and the file's own description calls the chrome "deliberately quiet"). Rule 4 is therefore the terminal answer: **Calm**, as rostered. No switch, silent or otherwise.
