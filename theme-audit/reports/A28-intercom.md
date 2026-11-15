## A28 · intercom

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

- **Before:** tokens 2 · refs 5 · contrast 1 · sections 3 · motion 1 · states 1
- **After:** tokens 5 · refs 5 · contrast 5 · sections 5 · motion 5 · states 5

Harness line after edits: `intercom 5 5 5 5 5 5 (disclosed:10)`. The diff is 148 insertions, 0 deletions — nothing existing was reflowed.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A tokens | `colors.focus` | No focus ring token anywhere in the file, and no focus treatment described in prose. A keyboard user has nothing to see. |
| P0 | F motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Zero durations and zero easing curves in the file. |
| P0 | G accessibility | whole file | No `## Accessibility` section. Six contrast failures, all undisclosed, including the brand's primary AI CTA. |
| P0 | B colour | `button-fin` | `{colors.on-primary}` white on `{colors.fin-orange}` #ff5600 measures **3.19:1** against 4.5:1 for its 15px / weight 500 label. This is the brand's flagship Fin CTA and the failure was silent. |
| P0 | E borders | `text-input` | The input's only affordance is its 1px edge, and the file left that edge at `{colors.hairline}` (1.57:1 on white). A control boundary that cannot be seen. |
| P1 | A tokens | `colors.surface` | `surface-1` / `surface-2` match no `surface` role pattern, so the `surface` role resolved to nothing and **every** `text on surface` and `border on surface` check was silently skipped — four real failures were hidden by the gap, not absent. |
| P1 | A tokens | `colors.text-dim` | All four text tones are named `ink-*`, which satisfies the `text` role; the `text-dim` role resolved to nothing. The file had no canonical secondary-text token, so prose pointed at `ink-subtle` (3.78:1) and `ink-muted` (5.44:1) interchangeably. |
| P1 | B colour | `{colors.ink-subtle}` | 3.78:1 on canvas / 4.25:1 on white, used at `{typography.body-sm}` 14px in the footer and at `{typography.caption}` 12px. Fails AA at both sizes. |
| P1 | B colour | `{colors.ink-tertiary}` | 2.36:1 on canvas / 2.65:1 on white. Clears no threshold at any size; the file describes it as "footnotes" as well as "disabled". |
| P1 | B colour | `{colors.hairline}` / `{colors.hairline-soft}` | 1.39:1 and 1.1:1 on canvas. Both are extracted and frozen; the file offered no accessible parallel for the cases where a boundary must actually be seen. |
| P1 | B colour | `{colors.semantic-success}` | #0bdf50 at 1.6:1 on canvas, and the same hex is also `{colors.report-green}`. The file called it "Positive states" without ever saying it is a chart fill that must never carry text. |
| P1 | H states | 16 of 18 component entries | Only `pressed` and `selected` were documented anywhere. `hover`, `focus-visible`, `active`, `disabled`, `loading` and `error` appeared in no component entry. |
| P1 | C elevation | Elevation ladder | Level 2 is "`{colors.surface-1}` + 1px `{colors.hairline}`", i.e. a border, while levels 1 and 3 are surface swaps — border and surface mixed in one ladder. Defensible as documented (the file says "Intercom resists drop shadows"), but level 2's border is the 1.57:1 hairline, so level 2 is visually identical to level 1. Flagged, not changed: the ladder is an extracted observation. |
| P2 | A tokens | `rounded.pill` / `rounded.full` | Two tokens, one value (9999px). Harmless, kept — they carry distinct intent (tab toggles vs avatars) and both are referenced in prose. |
| P2 | D typography | `{typography.caption}` | 12px at weight 400 is the footer's size, and the footer's colour was `{colors.ink-muted}`; the pairing is legible (5.44:1) but the file also pointed `ink-subtle` at "footer columns". Resolved in the footer state line. |
| P2 | I identity | frontmatter | Four `ink-*` tones with overlapping stated jobs ("tertiary type", "quaternary type", "disabled, footnotes") and no contrast guidance. Addressed by scoping them in Accessibility rather than renaming. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `surface: "#ffffff"` | Satisfies the required `surface` role; an exact alias of the extracted `surface-1`, so no value is invented. Unlocked four `on surface` contrast checks the harness had been skipping. |
| frontmatter `colors:` | — -> `text-dim: "#626260"` | Satisfies the required `text-dim` role; an exact alias of the extracted `ink-muted`, the only secondary tone that passes AA (5.44:1 canvas, 4.96:1 on `surface-2`). |
| frontmatter `colors:` | — -> `hairline-strong: "#857f75"` | **Prescribed**, not extracted. Parallel accessible boundary per SPEC §2: 3.53:1 on canvas, 3.97:1 on white. Scoped in prose to control edges only; the frozen hairlines keep decoration. |
| frontmatter `colors:` | — -> `focus: "#0007cb"` | The required focus role. Reuses Intercom's own `brand-blue` rather than inventing a ring colour. 9.87:1 canvas, 11.09:1 white, 9.01:1 `surface-2`, 3.48:1 on the Fin Orange fill — clears 3:1 on every light surface the file defines. |
| frontmatter `colors:` | — -> `focus-on-dark: "#65b5ff"` | The file documents dark signature surfaces (charcoal CTA, charcoal featured tier, black quote strip) where #0007cb sits at 1.7:1. Reuses the extracted `report-blue` hex. 8.64:1 on charcoal, 9.61:1 on black, 5.96:1 on `inverse-surface-1`. |
| frontmatter, before `spacing:` | — -> `motion:` group | The **Playful** block from SPEC §5, verbatim, all ten keys. |
| `## Components`, preamble | — -> one line | States the interaction states below are prescribed, naming the three variants (`button-primary-pressed`, `text-input-focused`, `pricing-tab-selected`) that were genuinely documented. Keeps prescribed and extracted separable. |
| `## Components`, 18 entries | — -> a `States:` line per entry | Covers default, hover, focus-visible, active/pressed, disabled, loading, selected, error. Presentational entries say so explicitly rather than padding: `feature-card` "two only", `product-mockup-card` "default and loading only", `startup-discount-card` and `cta-banner` "default only, states belong to the buttons they contain". |
| `## Components` -> `text-input` | `{colors.hairline}` edge -> `{colors.hairline-strong}` edge, with both ratios stated | The input's border is its only affordance, so it takes the accessible parallel token. The decorative hairline is unchanged everywhere else. |
| `## Components` -> `footer` | link colour pinned to `{colors.text-dim}`, **not** `{colors.ink-subtle}`, ratios stated | The file previously assigned `ink-subtle` (3.78:1) to footer columns at 12px. |
| new `## Motion & Animation`, after `## Components` | — -> full section | First line states the system is prescribed and was not measured from the live site. Ten-row interaction table, choreography notes, `@media (prefers-reduced-motion: reduce)` block. `transform` and `opacity` only; every exit shorter than its entrance. |
| new `## Accessibility`, after Motion | — -> full section | Measured contrast table (16 rows, 10 failures disclosed with their ratios), per-surface focus ring table, tap targets labelled as unverified, reduced-motion summary, and three honest residual gaps. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via a stdlib-only `python3` snippet; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #111111 / `canvas` #f5f1ec | 16.79:1 | 4.5:1 | Pass |
| `ink` / `surface` #ffffff | 18.88:1 | 4.5:1 | Pass |
| `ink` / `surface-2` #ebe7e1 | 15.33:1 | 4.5:1 | Pass |
| `text-dim` #626260 / `canvas` | 5.44:1 | 4.5:1 | Pass |
| `text-dim` / `surface` | 6.11:1 | 4.5:1 | Pass |
| `text-dim` / `surface-2` | 4.96:1 | 4.5:1 | Pass |
| `on-primary` #ffffff / `primary` #111111 | 18.88:1 | 4.5:1 | Pass |
| `inverse-ink` #ffffff / `inverse-canvas` #000000 | 21.0:1 | 4.5:1 | Pass |
| `semantic-error` #c41c1c / `canvas` | 5.29:1 | 4.5:1 | Pass |
| `hairline-strong` #857f75 / `canvas` | 3.53:1 | 3.0:1 | Pass (prescribed) |
| `hairline-strong` / `surface` | 3.97:1 | 3.0:1 | Pass (prescribed) |
| `hairline-strong` / `surface-2` | 3.22:1 | 3.0:1 | Pass (prescribed) |
| `focus` #0007cb / `canvas` | 9.87:1 | 3.0:1 | Pass |
| `focus` / `surface` | 11.09:1 | 3.0:1 | Pass |
| `focus` / `surface-2` | 9.01:1 | 3.0:1 | Pass |
| `focus` / `fin-orange` #ff5600 | 3.48:1 | 3.0:1 | Pass |
| `focus` / `ink` charcoal | 1.70:1 | 3.0:1 | Fail — which is why `focus-on-dark` exists |
| `focus-on-dark` #65b5ff / `ink` | 8.64:1 | 3.0:1 | Pass |
| `focus-on-dark` / `inverse-canvas` | 9.61:1 | 3.0:1 | Pass |
| `focus-on-dark` / `inverse-surface-1` #313130 | 5.96:1 | 3.0:1 | Pass |
| `ink-subtle` #7b7b78 / `canvas` | 3.78:1 | 4.5:1 | **Fail — frozen, disclosed** |
| `ink-subtle` / `surface` | 4.25:1 | 4.5:1 | **Fail — frozen, disclosed** |
| `ink-tertiary` #9c9fa5 / `canvas` | 2.36:1 | 4.5:1 | **Fail — frozen, disclosed** |
| `ink-tertiary` / `surface` | 2.65:1 | 4.5:1 | **Fail — frozen, disclosed** |
| `hairline` #d3cec6 / `canvas` | 1.39:1 | 3.0:1 | **Fail — frozen, disclosed** |
| `hairline` / `surface` | 1.57:1 | 3.0:1 | **Fail — frozen, disclosed** |
| `hairline-soft` #ebe7e1 / `canvas` | 1.10:1 | 3.0:1 | **Fail — frozen, disclosed** |
| `hairline-soft` / `surface` | 1.23:1 | 3.0:1 | **Fail — frozen, disclosed** |
| `semantic-success` #0bdf50 / `canvas` | 1.60:1 | 4.5:1 | **Fail — frozen, disclosed (chart fill)** |
| `button-fin`: `on-primary` / `fin-orange` | 3.19:1 | 4.5:1 | **Fail — frozen, disclosed** |

Ten failures, all disclosed in `## Accessibility` with their measured ratios. No brand identity hex was altered.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `opacity`, `transform: translateY(-1px)` | Travel removed; opacity only at 130ms |
| Press / active | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.97)` | Scale removed; fill swap instant |
| Focus-visible ring | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` on the `{colors.focus}` ring | No transition at all — never delayed |
| Page / route transition | 200ms in · 130ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(8px)` | Travel removed; cross-fade at 130ms |
| Modal / drawer | 320ms in · 200ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: scale(0.98→1)`; drawer `translateX` | Scale and slide removed; fade at 130ms |
| Dropdown | 130ms in · 70ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-4px) scale(0.99)` | Travel and scale removed; fade at 130ms |
| Toast | 200ms in · 130ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(12px)` | Travel removed; fade at 130ms |
| List enter | 200ms, stagger `{motion.stagger-step}` 60ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Stagger and travel removed; one fade at 130ms |
| List exit | 130ms, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Scale removed; fade at 130ms |
| Loading | 900ms spin / 1200ms shimmer, infinite | `linear` | `transform: rotate()`; `opacity` | Rotation becomes an opacity pulse at 130ms; shimmer frozen at mid tone |

Every exit is shorter than its entrance. Only `transform` and `opacity` animate — the harness reports no layout-property animation. The sole infinite animations are the spinner and skeleton; Intercom has no brand ambience loop, and the file says so.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 22, `REQUIRED_COLOR_ROLES["surface"]` | The `surface` pattern list matches `^surface$` and `^surface-(card\|soft\|raised\|elevated\|cream\|dark\|light\|alt\|muted\|subtle\|panel\|deep\|strong\|mid)` but **not numbered surfaces**. `surface-1` / `surface-2` is a common convention and failed the role outright. Worse, the miss is silent *and* load-bearing: with no `surface` representative, `check("text","surface")`, `check("text-dim","surface")`, `check_all("text","surface")`, `check_all("text-dim","surface")` and `check_all("border","surface")` all short-circuit, so a file is rewarded for the omission with four fewer recorded failures. | Add `r"^surface-\d+$"` (and `r"^surface$"` already present) to the `surface` pattern list. Any file using `surface-1` repo-wide is affected the same way. |
| `theme-audit/audit.py` line 25, `REQUIRED_COLOR_ROLES["text"]` | `r"^ink-"` is in the **text** pattern list, so `ink-muted`, `ink-subtle` and `ink-tertiary` all register as primary-text candidates and none can ever satisfy `text-dim`. An `ink-*`-named palette is structurally unable to pass the `text-dim` role without an alias token. | Move `r"^ink-(muted\|subtle\|soft\|secondary\|tertiary\|dim)$"` into the `text-dim` pattern list, ahead of the `text` list's `r"^ink-"`. |
| `theme-audit/audit.py` lines 283–296, focus-ring check | `surface_keys` is `^(canvas\|background\|bg\|base\|surface\|card\|panel)`, which excludes `inverse-canvas` and `inverse-surface-1`. And because `dual_theme` requires a `light`/`dark` substring in a surface key, a file whose dark surfaces are named `inverse-*` reports `dual_theme = False`, so `focus-on-dark` finds no targets and is never measured at all. A ring could be declared for dark surfaces and checked against nothing. | Add `r"^inverse-"` to `surface_keys`, and treat an `inverse-*` surface key as a dark-theme surface in `theme_of` / `dual_theme`. I verified my own `focus-on-dark` by hand (8.64 / 9.61 / 5.96) precisely because the harness does not. |
| `theme-audit/SPEC.md` §2 table | The table requires `text-dim on canvas` but never `text on surface` or `border on surface`, while `audit.py` checks both. The spec's stated contract is narrower than the measured one. | Add `text on surface`, `text-dim on surface` and `border on surface` rows to the §2 table so the document matches the harness. |
| `design-md/intercom/DESIGN.md` → repo-wide | `{colors.semantic-success}` and `{colors.report-green}` are the same hex #0bdf50 with two different stated jobs ("Positive states" vs "Analytics chart lime/green"). A semantic success token that is really a chart fill is a trap. Not a shared-file issue, but worth a CONTRIBUTING note. | Add a CONTRIBUTING rule: a `semantic-*` token must be checked as text and may not alias a chart colour. Not edited — `CONTRIBUTING.md` is read-only for me. |

### Needs approval

1. **`button-fin` fails AA at 3.19:1** — `{colors.on-primary}` white on `{colors.fin-orange}` #ff5600. This is Intercom's flagship Fin AI CTA and the hex is extracted; I did not change it.
   - *Nearest passing value:* #cc4500 reaches 4.54:1 with white, but it is visibly a different, muddier orange and would falsify the brand.
   - *Usage note that makes the real value defensible:* the pair clears 3:1, so it is compliant as **large text** — `{typography.headline}` 28px, or 18.66px+ at weight 700. At the component's actual `{typography.button}` 15px / weight 500 it is non-compliant. The honest alternatives are (a) raise the Fin CTA label to large-text size, or (b) use `{colors.ink}` #111111 on the orange fill, which measures 5.26:1 and keeps the Fin Orange identity intact while inverting only the label. **(b) is my recommendation and needs a brand decision, so I did not apply it.**
2. **`hairline-strong: "#857f75"` is a prescribed token, not an extracted one.** It is labelled as prescribed in the file. It introduces a warm grey Intercom does not publish. Approve or substitute a real Intercom boundary hex if one exists on a page I could not inspect.
3. **`focus: "#0007cb"` and `focus-on-dark: "#65b5ff"` reuse extracted brand hexes for a role the brand does not document.** The hexes are real (`brand-blue`, `report-blue`); their use as focus rings is prescribed. `brand-blue` is described in the file as "used on a small set of marketing illustrations", so promoting it to a system focus role is a judgement call that deserves sign-off.
4. **`{colors.ink-subtle}` at 14px and 12px.** The file assigns it to footer columns and helper text, where it measures 3.78:1 — a real AA failure at those sizes. I pinned the footer to `{colors.text-dim}` in the component entry, which changes a documented colour assignment. If the live footer genuinely ships `ink-subtle`, revert my pin and keep the disclosure only.
5. **`surface` and `text-dim` are alias tokens** duplicating `surface-1` and `ink-muted` exactly. They exist to satisfy role patterns the harness cannot otherwise match on this naming scheme (see Shared issues). If the harness patterns are fixed, both aliases should be deleted rather than left as redundant keys.

### Identity verdict

**Still reads as Intercom.** The document's spine is untouched: cream #f5f1ec canvas, charcoal as the *system primary* with Fin Orange quarantined to the Fin AI CTA, Saans at weight 500 with aggressive negative tracking, white tiles with modest 12/16px corners, product screenshots as the protagonist, and an explicit refusal of drop shadows. My 148 lines are all additive and all anchored to those facts rather than to generic tokens — the focus ring is Intercom's own `brand-blue`, the dark ring is its own `report-blue`, the `button-fin` hover steps to the brand's own `report-orange`, and the motion notes argue from this brand's restraint ("the press pop is the one playful gesture", "product mockup cards never animate on first paint", "no brand ambience loop"). The one genuinely foreign value is `hairline-strong` #857f75, flagged as prescribed and listed under Needs approval.

**On the Playful assignment — kept, but it is the weakest call in this audit.** The case against it is real. SPEC §5 rule 3 tests "whether saturated colour appears on interactive elements **and** whether the type voice is light and informal". Intercom passes the first half — Fin Orange genuinely sits on a button — and fails the second: the file's own description says "editorial", "careful, product-led publication", "ornament is rare", the eyebrow is sentence case with no tracking, and the Do's and Don'ts forbid pill-rounded CTAs, second display families and gradients. The report palette, the only multi-colour evidence, is explicitly scoped by the file to "INSIDE product UI mockups… not marketing surface colors" — exactly the case §5 warns not to read as playful. That points at **Calm**.

The reason I did not switch: §5's Calm escape clause is also a conjunction — "whose own description says 'sober' or 'editorial', whose display weight is **400**, and which forbids gradients". Intercom's display weight is 500, not 400, so that clause does not fire either. With the Playful test half-satisfied and the Calm override not satisfied, the rostered assignment stands, and SPEC §4's cross-file comparability ("the same interaction is comparable across every file that shares a profile") breaks if I move a borderline file on my own read. I applied the Playful block verbatim and then damped it in prose instead: travel held to ≤8px, overshoot confined to `{motion.ease-enter}`, scale-pop confined to the two CTA components, and no bounce on cards or hero type. The result is Playful timings on a Calm choreography — which is, I think, the honest description of this brand. **If the orchestrator is normalising borderline cases, intercom is a candidate to move to Calm**; the only edit needed is swapping the ten `motion:` values and the five durations quoted in the Motion table.
