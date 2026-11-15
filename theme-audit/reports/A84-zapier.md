## A84 · zapier

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 2 -> 5 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 5

All contrast failures are now disclosed rather than fixed: three counted by the harness (`mute on canvas`, `on-primary on primary`, `button-primary`) plus three it does not currently see (see Shared issues).

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Nothing to reference. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section, so every contrast failure below was undisclosed. |
| P0 | B · Colour | `on-primary` on `primary` | Warm white `#fffefb` on Zapier orange `#ff4f00` is 3.27:1, below the 4.5:1 normal-size text needs. `{typography.button-md}` is 18px/600 — below WCAG's 18.66px/700 large-text cut-off, so the 3:1 allowance does not apply. Brand identity hexes; not changed. Logged under Needs approval. |
| P0 | B · Colour | `body-mid` `#939084` | Documented as "secondary body / metadata" — normal-size text — at 3.17:1 on canvas and 2.92:1 on canvas-soft. Fails AA on both, and fails even the 3:1 large-text threshold on canvas-soft. The harness never measured it (see Shared issues). |
| P0 | B · Colour | `mute` `#c5c0b1` | 1.8:1 on canvas, 1.66:1 on canvas-soft. Documented as text ("fine print, low-emphasis captions") and bound as a boundary in three `ex-*` entries. Extracted and frozen; re-scoped to decoration in prose per SPEC §2 step 1, since `{colors.ink}` already does the boundary work at 17.65:1. No parallel token added. |
| P0 | A · Tokens | `focus` | No focus role existed. Bound to `#ff4f00`, the hex the palette already owns — a real role binding, not an alias. |
| P0 | H · States | every component | Only `active` was documented, and only inside an `ex-*` description. No hover, focus-visible, pressed, disabled, loading, selected or error anywhere. |
| P1 | C · Sections | `Responsive Behavior` | Existed only as `### Responsive Strategy` inside Layout. Moved verbatim to a top-level `##` after Do's and Don'ts, children promoted one level. Not duplicated. |
| P1 | C · Sections | `Known Gaps` | Missing entirely; the file made no statement about what it does not know. |
| P1 | E · Focus ring | two polarities | The file defines dark signature surfaces (`card-feature-dark`, `hero-band-dark`, `pricing-card-featured`, `footer` on `{colors.ink}`) as well as cream ones. One mid-luminance ring clears 3:1 on all three grounds (3.27 / 3.01 / 5.40), so a `focus-on-dark` counterpart would add a token without adding coverage. Offset stated, because on `button-primary` the ring's colour equals the fill it surrounds. |
| P1 | C · Elevation | `ex-modal-card`, `ex-toast` | Both descriptions claim a shadow ("elevated shadow", "medium shadow") with no `shadow:` group and no token behind either. Auto-derived generator text, not brand fact. Recorded in Known Gaps; the descriptions are left as generated. |
| P2 | D · Typography | all roles | Every role carries size, weight and line height; body on both cream surfaces passes. No change needed. |
| P2 | E · Ladders | `rounded`, `spacing` | `rounded.pill` and `rounded.full` are both 9999px — a duplicate, but a documented one (pills vs circular icon containers). Spacing is a clean 4px-based ladder apart from `xxs` 2px, which the file states as its own half-step. No value sits outside its scale. |
| P2 | C · Elevation | Level 0–2 | Elevation is expressed one consistent way — flat, hairline, cream-fill — with no shadow/border mixing. Canvas to canvas-soft is only 1.09:1, so Level 2 is a very quiet step; it is the brand's real choice, not a defect, and the hairline level carries anything that must read as separated. |
| P2 | A · Refs | prose | Zero dangling `{group.token}` references before and after. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | (no focus role) -> `focus: "#ff4f00"` | SPEC §1: the ring must be addressable as `focus*`. Reuses the hex the palette already owns, so it is a role binding, not an alias. |
| frontmatter, after `spacing:` | (no motion group) -> `motion:` with the **Playful** block verbatim from SPEC §4 | Required group; profile per roster. No value deviates. |
| `## Colors` → Mute bullet | "Lowest-priority text — fine print, low-emphasis captions." -> decoration-only scope, both failing ratios stated, boundary work pointed at `{colors.ink}` | SPEC §2 step 1 and step 4: the palette already owns a passing boundary tone, so nothing new was added and the failure is stated plainly. |
| `## Colors` → new `### Focus` | (new) -> states that the ring reuses `{colors.primary}` and is the same hex | SPEC §1: say which existing tone the ring reuses so nobody reads it as a new brand colour. |
| `## Components` → new `### Interaction States` | (new) -> one row per component naming its states; static containers and bands say they have one or two states | SPEC §7. State *set* labelled prescribed; hover/pressed hexes left uninvented. |
| after `## Components` | (new) -> `## Motion & Animation`, first line stating the system is prescribed and not measured | SPEC §3 order, §6 coverage: ten interactions × duration × easing × property × reduced-motion, plus the four motion rules and a `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | (new) -> `## Accessibility` | SPEC §3: measured contrast for every key pair, the four real failures stated plainly, ring visibility per surface with geometry and offset, tap-target arithmetic, reduced motion. |
| `## Layout` | `### Responsive Strategy` + three `####` children -> removed from Layout | Moved, not duplicated. |
| after Do's and Don'ts | (new) -> `## Responsive Behavior` with the three children promoted to `###`, content verbatim | SPEC §3: top-level section, moved verbatim. |
| `## Do's and Don'ts` → Don't | (new) -> two entries: no normal-size text in `body-mid` or `mute`; never drop the ring's 2px offset | The two failures a downstream consumer is most likely to walk into. |
| end of file | (new) -> `## Known Gaps` | Eight entries: prescribed motion, no shadow tokens, uninvented hover hexes, no semantic palette, no dark theme, tap targets computed not rendered, proprietary display face, prescribed ring. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#201515` / `canvas` `#fffefb` | 17.65:1 | 4.5:1 | Pass |
| `ink` / `canvas-soft` `#f8f4f0` | 16.27:1 | 4.5:1 | Pass |
| `ink-soft` `#2f2a26` / `canvas` | 14.07:1 | 4.5:1 | Pass |
| `ink-mid` `#36342e` / `canvas` | 12.34:1 | 4.5:1 | Pass |
| `body` `#605d52` / `canvas` | 6.54:1 | 4.5:1 | Pass |
| `body` / `canvas-soft` | 6.03:1 | 4.5:1 | Pass |
| `on-primary` `#fffefb` / `ink` | 17.65:1 | 4.5:1 | Pass |
| `canvas-soft` / `ink` (footer text) | 16.27:1 | 4.5:1 | Pass |
| `ink` as border / `canvas` | 17.65:1 | 3.0:1 | Pass |
| `ink` as border / `canvas-soft` | 16.27:1 | 3.0:1 | Pass |
| `focus` `#ff4f00` / `canvas` | 3.27:1 | 3.0:1 | Pass |
| `focus` / `canvas-soft` | 3.01:1 | 3.0:1 | Pass, 0.01 of margin |
| `focus` / `ink` | 5.40:1 | 3.0:1 | Pass |
| `on-primary` / `primary` `#ff4f00` | 3.27:1 | 4.5:1 | **Fail** — disclosed |
| `button-primary` label / its own fill | 3.27:1 | 4.5:1 | **Fail** — disclosed |
| `body-mid` `#939084` / `canvas` | 3.17:1 | 4.5:1 | **Fail** — disclosed |
| `body-mid` / `canvas-soft` | 2.92:1 | 4.5:1 | **Fail** — disclosed |
| `mute` `#c5c0b1` / `canvas` | 1.80:1 | 4.5:1 | **Fail** — disclosed |
| `mute` / `canvas-soft` | 1.66:1 | 4.5:1 text, 3.0:1 boundary | **Fail** — disclosed |
| `ink` / `primary` (alternative CTA label) | 5.40:1 | 4.5:1 | Pass — the defensible fix |
| `canvas` / `canvas-soft` (elevation step) | 1.09:1 | n/a | Layer step is real but very quiet |
| `ink` / `primary` fill (dark text on orange) | 5.40:1 | 3.0:1 | Pass |

All ratios computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`, not estimated.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `background-color`, `color`, `border-color` (paint only) | Unchanged; paint-only, capped 130ms |
| Press / active | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed; paint change alone |
| Focus | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` on the ring | Unchanged |
| Page / route | enter 200ms `{motion.duration-base}`, exit 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | Travel removed; fade at 130ms |
| Modal / drawer | enter 200ms, exit 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scale(0.98→1)`; drawer `translateX` | Scale and slide removed; backdrop fades |
| Dropdown | enter 130ms, exit 70ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(-4px→0)` | Travel removed; fade at 130ms |
| Toast | enter 200ms, exit 130ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(12px→0)` | Travel removed; fade at 130ms |
| List enter | 200ms per item, `{motion.stagger-step}` 60ms between | `{motion.ease-enter}` | `opacity` + `translateY(8px)` | Stagger and travel removed; all fade together |
| List exit | 130ms, no stagger | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | Scale removed |
| Loading | `{motion.duration-emphasis}` 450ms loop | `{motion.ease-standard}` | `opacity` pulse; spinner `rotate()` | Loop frozen; static indicator, state still announced in text |

Every exit is shorter than its entrance. Only `transform` and `opacity` animate; the one infinite animation is the loader. Nothing animates on first paint.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 372 `theme_of()` / line 402 `same_theme()` | **A surface token used once as a textColor is reclassified as a foreign theme, silencing every check against it.** `canvas-soft` is this file's card surface, but `footer` paints it as text on `{colors.ink}`, so `bound_polarity["canvas-soft"] == {"dark"}` and `theme_of("canvas-soft")` returns `"dark"` while the canvas is light. `same_theme` then fails for every default-theme ink, and **all five surface checks are skipped**: `check("text","surface")`, `check("text-dim","surface")`, `check_all("text","surface")`, `check_all("text-dim","surface")`, `check_all("border","surface")`, plus the bound-boundary check on `ex-pricing-tier`. The brief for this site (written against an earlier revision) lists `mute on canvas-soft` at 1.66:1 twice — as secondary text and as a bound boundary. Both are real; the current harness reports neither. Any file whose footer or dark card inverts a light surface tone as text has the same hole. | Derive polarity for a token only from the roles it is *not* otherwise bound to: skip a token that any component declares as a `backgroundColor` (or that a canvas/surface role resolves to) when building `bound_polarity`. A tone that paints grounds is a ground, whatever one footer uses it for. |
| `theme-audit/audit.py` line 29 `REQUIRED_COLOR_ROLES["text-dim"]` | **`body-mid` matches no `text-dim` pattern**, so a token the file documents as "Secondary body / metadata" is never measured. It fails AA at 3.17:1 and 2.92:1. The existing `^body-(soft\|muted\|secondary)$` alternation covers three naming conventions and misses `-mid`, which this palette uses for both its ink and its body ladder (`ink-mid`, `body-mid`); `ink-mid` is caught only because `^ink-...mid` is listed. | Add `mid` to the `body-` alternation: `^body-(soft\|muted\|secondary\|mid)$`. |
| `theme-audit/audit.py` line 468, bound-boundary prop list | Only `borderColor`, `border` and `outlineColor` count as boundary bindings, so `{colors.mute}` as `item-divider` (`ex-cart-drawer`) and `rowBorder` (`ex-data-table-cell`) is invisible at 1.66:1. Divider props are exactly where a too-light hairline hides. | Match the property *name* instead of an allow-list: any component property whose name contains `border`, `divider`, `rule`, `stroke`, `outline` or `hairline` and resolves to a colour token is a boundary binding. |
| `theme-audit/audit.py` line 463 bound-boundary vs line 594 ring coverage | The two checks contradict each other. SPEC §1 says a ring is judged against the surfaces it is drawn *on*, not the control fill it surrounds — but declaring `outlineColor: "{colors.focus}"` on `button-primary`, which is the honest way to document the ring binding, makes `bound_borders` measure the ring against the orange fill at 1.00:1 and manufacture a failure. So documenting the ring correctly is penalised, and I left the binding out of the frontmatter for that reason alone. | Exclude `outlineColor` from `bound_borders` when the token is also a `focus*` token or appears in `focus_tokens`; the ring-coverage check already judges it against the right grounds. |
| `theme-audit/briefs/A84-zapier.md` line 3 | The brief's "Theme intent" line is truncated mid-sentence: "An inspired interpretation of Zapier's design language — a". Same truncation in `roster.md` line 91. Cosmetic, but it is the only statement of intent an agent is handed. | Carry the full `description` from frontmatter, or stop at a word boundary with an ellipsis. |
| `theme-audit/briefs/A84-zapier.md` lines 11-14 | The brief's measured facts were generated against an earlier `audit.py`: it lists `border` as a missing role (the current harness resolves it from bindings) and lists two `mute on canvas-soft` failures the current harness no longer emits, while omitting the `on-primary`/`primary` 3.27:1 failure that it does emit. Agents told to "confirm each of these yourself" will find the list disagrees with the tool in both directions. | Regenerate briefs from the same harness revision that agents run, and stamp the revision in the brief. |

### Needs approval

1. **`button-primary` label contrast, 3.27:1 against 4.5:1 required.** `{colors.on-primary}` `#fffefb` on `{colors.primary}` `#ff4f00`. Both hexes are extracted brand identity and were not changed. Two defensible resolutions, each a brand decision:
   - *Usage note:* restrict warm-white labels on orange to `{typography.display-xs}` 20px/700 or larger, where the 3:1 large-text threshold applies and 3.27:1 passes. `{typography.button-md}` 18px/600 is below WCAG's 18.66px/700 cut-off, so it does not qualify today.
   - *Nearest passing value:* ink the label in `{colors.ink}` `#201515`, which measures 5.40:1 on the same orange and changes no brand hex. This is the only change that makes the default CTA pass AA.
2. **Re-pointing the `ex-*` `mute` boundary bindings.** `ex-pricing-tier.borderColor`, `ex-cart-drawer.item-divider` and `ex-data-table-cell.rowBorder` all resolve to `{colors.mute}` at 1.66:1 on their own cream ground, below the 3:1 a visible boundary needs. Per SPEC §2 step 3 the bindings are left exactly as generated and the prose scopes `mute` to decoration. Approval sought to re-point all three at `{colors.ink}` (16.27:1 on canvas-soft), which is the tone the Elevation ladder already names for hairlines.
3. **`{colors.body-mid}` `#939084` as metadata text**, 3.17:1 on canvas and 2.92:1 on canvas-soft. Nearest passing value already in the palette: `{colors.body}` `#605d52` at 6.54:1 / 6.03:1. Usage note that would make the real value defensible: `body-mid` for 24px+ (or 18.66px/700+) text on `{colors.canvas}` only — it still misses 3:1 on `{colors.canvas-soft}`, so there is no surface on which it is defensible at normal size.
4. **`{colors.focus}` as a prescribed ring.** The hex is a brand fact; its use as a focus ring is this audit's prescription, and the 2px offset is load-bearing (0.01 of margin on `canvas-soft`, and identical to the fill on `button-primary`). Worth a brand-owner sign-off that orange is the ring rather than, say, `{colors.ink}` with an offset — which would be 17.65:1 on cream but invisible on the dark coffee cards.

### Identity verdict

Still unmistakably Zapier, and the additions lean on brand facts rather than generic defaults. The focus ring is the brand's own orange rather than the system blue every token dump reaches for; the boundary question was answered with `{colors.ink}` — the tone the file's own Elevation ladder already names — instead of a manufactured neutral grey, which would have put a cool hairline into a palette whose first rule is that every neutral is warm; and the error state is documented as borrowing `{colors.primary}` precisely because the brand owns no second chromatic signal, with that limitation stated rather than papered over with an invented red. The Interaction States table names paint-only hover changes and leaves the unextracted hover hexes unfilled, so no colour was invented.

**Playful is the right profile, kept as rostered.** SPEC §5 rule 3 fires on both of its conjuncts: saturated colour appears on interactive elements, not just as static card grounds — `{colors.primary}` is on every CTA and is `ex-app-shell-row`'s active indicator — and the identity is illustration-led, with zap and workflow SVGs and photography explicitly rare. The Calm tell in the same rule does not fire: the file nowhere says "sober" or "editorial", its display weight is 500 not 400, and it forbids no gradients. The counter-argument is the file's own "confidently-mature" and "modest and unflashy", which is why the motion section keeps travel small — 8px translate, a 2% scale pop — rather than reaching for the springier end of the profile. Rule 2 was considered and rejected: Zapier is a workflow tool but not a terminal, IDE or infra identity, and nothing about a warm cream canvas with a Degular display face reads as developer-tool Crisp.

### Note for the orchestrator (A84 of 84)

Two things earlier agents would have wanted said, both already in Shared issues but worth surfacing: the `theme_of` polarity bug silently voids **every** `surface` contrast check in any file whose footer or dark card uses a light surface tone as text — so a clean contrast score in such a file means "not measured", not "passing" — and the briefs were generated against a different harness revision than the one agents are told to run, which means some agents were asked to confirm failures the tool no longer reports and to miss ones it does.
