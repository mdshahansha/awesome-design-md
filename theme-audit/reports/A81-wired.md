## A81 · wired

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 2 -> 5 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 5

All six harness figures confirmed independently: the pre-edit run reported
`roles_missing: ["focus"]`, three undisclosed contrast failures, four missing
sections, no `motion:` group and one documented state (`active`, from the
`ex-app-shell-row` description). Every ratio below was computed with a python3
snippet using WCAG 2.1 relative luminance, not estimated.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. The brand's entire interaction timing was undocumented. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Three contrast failures, including one on real body metadata, were undisclosed. |
| P0 | A Token contract | `colors` | No `focus` role. Nothing in the file said how a keyboard user sees where they are on a pure black-on-white surface. |
| P0 | H States | `## Components` | Only one state documented across 25 component entries. Hover, focus-visible, pressed, disabled, loading, selected and error were named nowhere. |
| P1 | Section contract | document order | `Responsive Behavior` existed only as `### Responsive Strategy` inside Layout; `Known Gaps` was absent entirely. |
| P1 | B Colour | `{colors.body}` on `{colors.canvas-soft}` | 4.23:1, below 4.5:1. Grey metadata on the tinted surface fails AA for normal text. Extracted, so disclosed with a size qualifier rather than changed. |
| P1 | B Colour | `{colors.hairline}` on both grounds | 1.32:1 and 1.21:1, below 3:1. Extracted and frozen. Real failure where a hairline is a card's only boundary. |
| P1 | B Colour | `{colors.link}` on `{colors.canvas-soft}` | 4.13:1, below 4.5:1. The harness never measured this token at all (see Shared issues); found by hand. |
| P2 | B Colour | `{colors.link}` on `{colors.canvas}` | 4.5006:1. Passes AA by 0.0006. A one-step darkening of the canvas behind an inline link breaks it; noted as a floor in the file. |
| P2 | G Accessibility | `button-icon-circular` | Computes to 36 px tall from `{spacing.sm}` 8+8 plus a 20 px glyph box — below a 44 px tap target, while the pre-existing Touch Targets text claims "WCAG AAA at all widths" for `button-primary` only. Arithmetic, not a rendered measurement. |
| P2 | C Elevation | `ex-modal-card`, `ex-toast` | Auto-derived descriptions promise an "elevated shadow" and a "medium shadow". The brand documents no shadow value, has no `shadow:` group, and its own Don't forbids drop-shadows. Boilerplate contradicting the brand; recorded in Known Gaps, text left as extracted. |
| P2 | D Typography | all roles | Every typography role carries fontSize, fontWeight and lineHeight. No gap. `{typography.byline}` at 12.73 px is an odd value, likely computed rather than authored; noted in Known Gaps. |
| P2 | E Ladders | `rounded`, `spacing` | Both ladders are internally consistent; `rounded` has exactly two rungs (0 and 9999), which is the brand's point, not a gap. No value sits outside its scale. |

Dimension C, checked and clean: `canvas` #ffffff to `canvas-soft` #f5f5f5 is
1.09:1, so the two layers are not distinguishable by luminance alone — but the
file never asks them to be. Elevation is expressed one consistent way (flat,
1 px hairline, 2 px ink border) with no shadow anywhere, so there is no
shadow/border mixing to fix.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | (no focus token) -> `focus: "#057dbc"` | Required role, and the ring needs a name before the file can speak about it. Reuses the existing `{colors.link}` hex: a real role binding at a tone the palette already owns, not an alias for a regex. |
| frontmatter | (no group) -> `motion:` with the Calm profile block verbatim | SPEC section 4/5. No value deviates, so this file stays comparable with its profile siblings. |
| `## Colors` → Surface | hairline bullet -> same bullet plus its two measured ratios and a scope to decoration | SPEC section 2 step 4: say plainly where the real brand fails, at the point of use. |
| `## Colors` → Semantic | (nothing) -> `Focus` bullet | Documents which existing tone the ring reuses, so nobody reads it as a new brand colour. |
| `## Layout` | `### Responsive Strategy` + four `####` children -> pointer line | Moved, not duplicated, per the section contract. |
| `## Components` | (nothing) -> `### Component States` table, 11 rows x 8 states | SPEC section 7. Paint-only changes throughout, because that is what this brand does. |
| after `## Components` | (nothing) -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. 13-row interaction table plus a `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | (nothing) -> `## Accessibility` | Measured contrast for 10 pairs, ring coverage on 4 surfaces, tap-target arithmetic, reduced-motion summary. |
| after Do's and Don'ts | (nothing) -> `## Responsive Behavior` | The Layout subsection body byte-identical, heading renamed from Responsive Strategy to the contract name and child headings promoted `####` -> `###`, per the SPEC amendment in bdf658b ("verbatim governs the content, not the heading"). |
| `## Don't` | 5 bullets -> 6 | Added the no-scale-pop/no-slide rule the motion section now relies on. |
| end of file | (nothing) -> `## Known Gaps` | Eight entries, separating prescribed from extracted. |

No brand hex was changed. No existing `components:` binding was re-pointed. No
prose outside the lines above was reflowed.

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #000000 / canvas #ffffff | 21.00:1 | 4.5:1 | Pass |
| ink #000000 / canvas-soft #f5f5f5 | 19.26:1 | 4.5:1 | Pass |
| ink-soft #1a1a1a / canvas #ffffff | 17.40:1 | 4.5:1 | Pass |
| ink-soft #1a1a1a / canvas-soft #f5f5f5 | 15.96:1 | 4.5:1 | Pass |
| on-primary #ffffff / primary #000000 | 21.00:1 | 4.5:1 | Pass |
| body #757575 / canvas #ffffff | 4.61:1 | 4.5:1 | Pass |
| body #757575 / canvas-soft #f5f5f5 | 4.23:1 | 4.5:1 | **Fail** (disclosed) |
| hairline #e0e0e0 / canvas #ffffff | 1.32:1 | 3.0:1 | **Fail** (disclosed) |
| hairline #e0e0e0 / canvas-soft #f5f5f5 | 1.21:1 | 3.0:1 | **Fail** (disclosed) |
| hairline #e0e0e0 / primary #000000 | 15.91:1 | 3.0:1 | Pass (footer rules) |
| link #057dbc / canvas #ffffff | 4.50:1 (4.5006) | 4.5:1 | Pass, marginal |
| link #057dbc / canvas-soft #f5f5f5 | 4.13:1 | 4.5:1 | **Fail** (disclosed; scoped out of use) |
| focus #057dbc / canvas #ffffff | 4.50:1 | 3.0:1 | Pass |
| focus #057dbc / canvas-soft #f5f5f5 | 4.13:1 | 3.0:1 | Pass |
| focus #057dbc / primary #000000 (footer) | 4.67:1 | 3.0:1 | Pass |
| focus #057dbc / hairline #e0e0e0 | 3.41:1 | 3.0:1 | Pass |

One ring covers every surface the file defines, including the black footer
band, so no `focus-on-dark` counterpart was added. The ring is drawn 2 px
outside the control at a 2 px offset, so it is judged against the surface
behind the control and not against the pure-black CTA fill — which no single
ring could clear alongside white.

Boundary work, resolved by SPEC section 2's ordered steps: step 1 applied. The
palette already owns passing tones for a real boundary — `{colors.ink}` at 21:1
(already bound as `text-input`'s border) and `{colors.body}` at 4.61:1 / 4.23:1,
both clearing 3:1 — so the prose was re-scoped to use them and **no parallel
`hairline-strong` token was added**. Step 3 honoured: every extracted
`{colors.hairline}` binding is untouched.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | color, border-color, opacity (photo 0.92) | Unchanged — paint-only |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | opacity to 0.7, background-color invert | Unchanged at `{motion.duration-reduced}` |
| Focus | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | opacity of the ring | Appears instantly, no fade |
| Page / route transition | `{motion.duration-base}` 250ms | `{motion.ease-standard}` | opacity 0 -> 1, no slide | Cross-fade at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | opacity, translateY(8px) -> 0 | opacity only, translate removed |
| Modal / drawer exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | opacity 1 -> 0 | opacity only at `{motion.duration-reduced}` |
| Dropdown | enter 150ms / exit 80ms | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity, translateY(4px) -> 0 | opacity only, translate removed |
| Toast enter | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | opacity, translateY(8px) -> 0 | opacity only, translate removed |
| Toast exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | opacity 1 -> 0 | opacity only at `{motion.duration-reduced}` |
| List enter | 250ms per item, `{motion.stagger-step}` 40ms between | `{motion.ease-enter}` | opacity 0 -> 1 only | Stagger dropped, single fade |
| List exit | `{motion.duration-fast}` 150ms, no stagger | `{motion.ease-exit}` | opacity 1 -> 0 | opacity only at `{motion.duration-reduced}` |
| Loading | `{motion.duration-emphasis}` 500ms per cycle, infinite | `{motion.ease-standard}` | opacity 1 -> 0.5 -> 1 on canvas-soft blocks | Frozen to a static block |
| Hero on first paint | none | none | none | Unchanged |

Every exit is shorter than its entrance. Only `transform` and `opacity` are
animated; the hover and press rows are paint-only, which SPEC section 6 permits
explicitly — on a brand with no shadow, no radius and no accent, the ink swap
*is* the hover state, and inventing a scale pop would contradict the file's own
Don'ts. One infinite animation (the skeleton pulse), stated as such; no
ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 541 (`SEMANTIC` tuple) | A `link*` tone is measured by nothing. It matches no entry in `REQUIRED_COLOR_ROLES` and no pattern in `SEMANTIC`, yet it is by definition ink drawn on a ground at body size. wired's `link` #057dbc passes on canvas by 0.0006 and **fails at 4.13:1 on canvas-soft**, and the harness reported neither. Any file with a link, anchor or hyperlink token has the same blind spot. | Add `r"^link"`, `r"^anchor"`, `r"^hyperlink"` to the `SEMANTIC` tuple, or better, to the `text` role's pattern list so `check_all("text", ...)` picks them up on both grounds. The `FILL_MARKER` guard already in the semantic loop stops `link-bg`-style fills from being charged. |
| `theme-audit/audit.py` line ~548 (`SEMANTIC` loop) | Semantic tones are measured only against `canvas`, never against `surface`, while text roles get both via `check_all`. A tone that passes on white and fails on a tint is invisible. | Run the same loop a second time against `roles["surface"]`. |
| `theme-audit/audit.py` line ~768 (`documents()`) | The states check counts the bare word `active`, so the auto-generated `ex-app-shell-row` description "Active state uses brand primary as the indicator" scored a state in any file carrying the examples block. Verified for wired against `HEAD:design-md/wired/DESIGN.md`: that generated line was the single source of `active`, so the baseline `states: 1` was really a 0. Commit bdf658b states the bold-run anchoring added for A68 "already excludes the generated `ex-*` description string"; it does not here — the line is itself a bold-run (`**`ex-app-shell-row`** — …`) and so is kept as structured. | Require the word on a row that also names a component, or exclude lines whose bold run matches `^ex-` from the haystack. |
| `design-md/wired/DESIGN.md` example generator (`scripts/derive-examples-block.mjs`, not mine to edit) | It emits "elevated shadow" and "medium shadow" into `ex-modal-card` and `ex-toast` for a brand whose Don'ts forbid drop-shadows, and emits a `TO_FILL` instruction line into shipped prose. | Have the generator read the file's Elevation & Depth levels instead of a fixed template, and strip the `TO_FILL` note when no marker remains. |

Not a harness bug, checked: `surface` resolving to `canvas-soft` is correct
here. It is bound as a real background by five `ex-*` components, so
`hairline on canvas-soft` and `body on canvas-soft` are pairs the file actually
asserts, not manufactured ones. The brand's dominant card surface is
`{colors.canvas}` itself — every `story-card` sits on white — which is why the
failures only appear on the rare tint.

### Needs approval

1. **Re-bind the `ex-*` card borders off `{colors.hairline}`.** `ex-pricing-tier`
   and `ex-data-table-cell` use `{colors.hairline}` #e0e0e0 as a card's or a
   row's only boundary, at 1.21:1 on `{colors.canvas-soft}` against a 3:1
   requirement. Nearest passing value from the existing palette:
   `{colors.body}` #757575, 4.23:1 on canvas-soft and 4.61:1 on canvas. Usage
   note that would make the real value defensible: the hairline is a
   typographic rule between story rows, where no boundary has to be *found*,
   and 1.4.11 does not apply to purely decorative lines — so the extracted
   value stands for `story-row` and `hairline-divider`, and only the card and
   table bindings need the stronger tone. Left exactly as extracted pending a
   brand decision, per SPEC section 2 step 3.
2. **`{colors.body}` #757575 on `{colors.canvas-soft}` #f5f5f5 at 4.23:1.**
   Nearest passing grey: #707070 (4.54:1 on canvas-soft, 4.95:1 on canvas).
   Usage note that makes the extracted value defensible: restrict this pair to
   18.66 px/700 or 24 px+, where 3:1 applies, and set smaller metadata on
   `{colors.canvas}` where #757575 passes at 4.61:1. Hex unchanged.
3. **`{colors.link}` #057dbc at 4.5006:1 on white.** Technically AA, with no
   margin. If the brand ever wants headroom, #0673ad gives 5.0:1; changing it
   is a brand-identity decision, so nothing was changed.
4. **`{colors.focus}` reuses `{colors.link}`.** Confirm the brand accepts its
   inline-link blue appearing as a 2 px keyboard focus ring on chrome, given
   the file's own Don't reserves that blue for article body links. The
   alternative that still clears 3:1 everywhere is `{colors.body}` #757575
   (4.61 / 4.23 / 4.56), a grey ring — correct for a monochrome brand but a
   weaker indicator. The blue was chosen for visibility.
5. **`button-icon-circular` at 36 px** needs `{spacing.md}` padding or an
   extended hit area to reach 44 px. Changing the extracted `{spacing.sm}`
   padding would alter a documented brand value, so it is flagged, not fixed.

### Identity verdict

Still unmistakably Wired, and the Calm profile is right — no switch argued.

Rule 4 of the assignment order is the terminal answer here, and the file
positively earns it rather than falling through: the description calls itself
editorial and magazine-like, every display weight is 400, there is no gradient,
no shadow, no radius and no chromatic accent beyond one inline link blue. Rule 1
does not fire (full-bleed cover photography exists, but the type is dense and
fast, not sparse and slow — a magazine front page, not a product reveal). Rule 2
does not fire; rule 3 cannot (a two-hex palette plus one link blue is the
opposite of saturated multi-colour). Calm's signature — short opacity-led fades,
little travel, symmetric ease — is exactly what a printed-page-ported-to-screen
surface should do.

The additions are written in this brand's vocabulary, not a token dump: states
are paint-only because the brand forbids softening and shadow; press is an
opacity drop rather than a scale pop; `button-outline`'s hover reuses the file's
own Level 2 two-pixel ink border rather than inventing a treatment; the loading
skeleton is `{colors.canvas-soft}`, the brand's one tint; the error state is
weight and rule because the palette genuinely has no red and none was invented.
The focus ring is the only chromatic tone the brand already owns. Nothing here
would transplant onto another file in the collection without reading wrong.
