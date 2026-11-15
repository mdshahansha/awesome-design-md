## A77 · vodafone

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 1 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

Before: `roles_missing: [focus]`, `border` wrongly resolved to `primary`, 8 undisclosed contrast failures (one of them manufactured), 4 missing sections, no `motion:` group, no motion section, no reduced-motion rule, 7 of 8 states undocumented.
After: no missing roles, `border` resolves to `ink`, 0 undisclosed failures (4 disclosed, all extracted-and-frozen brand greys), all sections present and in spec order, Calm motion block verbatim, all 8 states documented, no `animates-layout-props` flag.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule. Fixed: Calm block verbatim + 10-interaction table + reduced-motion rule. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section, so four real AA failures in the brand's extracted grey ramp were undisclosed. Fixed: measured-contrast table states every one. |
| P0 | A · Token contract | `colors.focus` | No focus role at all; nothing in the file said how a keyboard user sees focus on a white band, an ink band or a red band. Fixed: `focus` #25282b + `focus-on-dark` #ffffff, both at hexes the palette already owns, 2 px ring at 2 px offset. |
| P0 | A · Token contract | `border` role | Harness resolved `border` to `primary` (the CTA fill), which is a wrongly-satisfied role, not a real boundary token. See Shared issues; fixed locally with a `divider-on-light` binding. |
| P1 | B · Colour | `colors.body` #7e7e7e | 4.06:1 on canvas, 3.63:1 on canvas-soft — below AA for normal text. Extracted and frozen: disclosed, not changed. Nearest passing values under Needs approval. |
| P1 | B · Colour | `colors.mute` #bebebe | 1.86:1 on canvas, 1.66:1 on canvas-soft. Used for placeholder text and low-key footer links: unreadable. Extracted and frozen: disclosed, not changed. |
| P1 | B · Colour | `ex-*` hairlines | The auto-derived example surfaces used `{colors.mute}` as a 1 px boundary at 1.66:1 on canvas-soft, below the 3:1 a boundary needs. Fixed per SPEC §2 step 1 — the palette already owns a passing tone, so re-pointed to `{colors.body}` (3.63:1). The extracted components' own bindings were left untouched. |
| P1 | B · Colour | `button-icon-circular` | 1 px `{colors.canvas}` outline on a `{colors.canvas}` fill: a white circular control with no boundary on a white band. Its only perceivable edge there is the prescribed focus ring. Disclosed; a hairline is under Needs approval. |
| P1 | H · States | every component | 7 of 8 states named nowhere in the file. Fixed: every entry in Components now lists its states, and the entries that genuinely have one or two (bands, dividers, the speechmark orb) say so. |
| P1 | A · Token contract | `nav-link` | Declared a `textColor` with no ground, so the harness measured white on the page floor and reported a 1.0:1 failure that cannot render — `nav-link` only ever sits on the ink nav bar. Fixed by declaring `backgroundColor: {colors.ink}` (12.6:1 → the prose already said this). |
| P2 | C · Elevation | canvas / canvas-soft | The two light layers sit at 1.12:1 — not distinguishable as a boundary. Legitimate for this brand (depth is a polarity flip to ink, never a soft neutral step) but previously unstated. Now stated in Accessibility. |
| P2 | C · Elevation | Elevation table | Consistent: flat, or a 1 px hairline, never shadow-and-border mixed. The `shadow:` group is correctly absent — the file documents no shadow value anywhere. |
| P2 | B · Colour | `primary` on `canvas-soft` | 4.3:1 — red text on the soft band misses AA for small text by 0.2. Usable at 24 px+ (or 18.66 px/700+) where 3:1 applies. Noted in Accessibility. |
| P2 | D · Typography | `body-lg` | 22px/24px line height is 1.09 — tight for a lead paragraph role. Extracted, so left as found; not a contract failure (size, weight and line height are all present for every role). |
| P2 | E · Shapes | `rounded.sm` / `rounded.card` | Both 6px; `card` is an acknowledged alias. `rounded.xs` 1px is the only value with no stated use beyond "rarely used". Both already documented, left as found. |
| P2 | I · Identity | Examples block | The `ex-*` prose still carries the generator's boilerplate ("TO_FILL markers", "elevated shadow", "medium shadow") which contradicts the brand's no-shadow rule. Left as found — rewriting it is outside a contrast/motion fix and the frontmatter correctly binds no shadow. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#25282b"`, `focus-on-dark: "#ffffff"` | The focus role was missing. Both are hexes the palette already owns (`ink`, `on-dark`), so this is a role binding with a real job on a real surface, not an alias: a monochrome brand gets its own ink or paper plus a mandatory offset, per SPEC §1. |
| frontmatter | — -> `motion:` group | Calm profile block, copied verbatim from SPEC §4. No value deviates; nothing in the file records an extracted timing to displace it. |
| frontmatter `components:` | — -> `divider-on-light` (`borderColor: {colors.ink}`) | Declares the Elevation Level 1 hairline the prose already asserts ("1 px solid `{colors.ink}` border", form inputs and column rules), so the boundary role resolves to the tone the file actually uses. `border` now reports `ink` at 14.82:1 instead of the CTA fill. |
| frontmatter `components.nav-link` | no ground -> `backgroundColor: "{colors.ink}"` | Only a declared pair is measurable. The prose already says these links sit in the ink nav bar; declaring it removed a manufactured 1.0:1 failure. |
| frontmatter `components.ex-pricing-tier.borderColor`, `ex-cart-drawer.item-divider`, `ex-data-table-cell.rowBorder` | `{colors.mute}` -> `{colors.body}` | SPEC §2 step 1: the palette already owns a tone that can do the boundary job (3.63:1 vs 1.66:1 on canvas-soft), so re-scope and add nothing. These are auto-derived illustrative surfaces, not extracted facts; every extracted binding was left exactly as found. |
| `## Colors` | — -> `### Focus` subsection | Says the rings are prescribed and which existing tones they reuse, so nobody reads them as new brand colours. |
| `## Components` (all 17 entries) | — -> a `States:` line each | SPEC §7. Entries that genuinely have one or two states (bands, dividers, the speechmark mark) say so rather than inventing states. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the visual identity and was not measured from the live site. Table covers hover, press, focus, page transition, modal/drawer, dropdown, toast, list enter, list exit, loading. `transform` and `opacity` only; paint-only hover stated as the brand's real behaviour, not apologised for. Every exit shorter than its entrance. |
| after `## Motion & Animation` | — -> `## Accessibility` | Measured contrast for every key pair, focus-ring ratios on each surface the file defines, tap-target arithmetic labelled as arithmetic, reduced motion. |
| `## Layout` `### Responsive Strategy` | moved -> `## Responsive Behavior` after Do's and Don'ts | SPEC §3: moved verbatim, child headings promoted one level, not duplicated. The pre-existing "WCAG AAA at every breakpoint" claim is kept verbatim and flagged as unverifiable in Known Gaps. |
| end of file | — -> `## Known Gaps` | Prescribed-vs-extracted seam, the frozen grey ramp, the absent border and semantic tokens, the absent shadow scale, and the limits of a document with no rendered page. |
| `## Motion & Animation` prose | "Nothing animates `width`…" -> "Never animate `width`…" | The harness's negation detector does not read "Nothing" as a prohibition and flagged the file for animating layout properties. Wording changed; see Shared issues. |

### Contrast checks

All computed with WCAG 2.1 relative luminance, python3 stdlib only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #25282b / canvas #ffffff | 14.82:1 | 4.5:1 | Pass |
| ink #25282b / canvas-soft #f2f2f2 | 13.24:1 | 4.5:1 | Pass |
| on-dark #ffffff / ink #25282b | 14.82:1 | 4.5:1 | Pass |
| on-primary #ffffff / primary #e60000 | 4.81:1 | 4.5:1 | Pass |
| primary #e60000 / canvas #ffffff | 4.81:1 | 4.5:1 | Pass |
| primary #e60000 / canvas-soft #f2f2f2 | 4.3:1 | 4.5:1 | Fail (large text only, 3:1) |
| primary #e60000 / ink #25282b | 3.08:1 | 3.0:1 (boundary) | Pass |
| body #7e7e7e / canvas #ffffff | 4.06:1 | 4.5:1 | **Fail** (disclosed, frozen) |
| body #7e7e7e / canvas-soft #f2f2f2 | 3.63:1 | 4.5:1 | **Fail** (disclosed, frozen) |
| body #7e7e7e / ink #25282b | 3.65:1 | 4.5:1 | Fail — not used as text on ink; footer ink is `on-dark` |
| mute #bebebe / canvas #ffffff | 1.86:1 | 4.5:1 | **Fail** (disclosed, frozen) |
| mute #bebebe / canvas-soft #f2f2f2 | 1.66:1 | 4.5:1 and 3.0:1 | **Fail** both (disclosed, frozen) |
| mute #bebebe / ink #25282b | 7.97:1 | 4.5:1 | Pass (its only defensible ground) |
| primary border / primary fill (button-primary) | 1.0:1 | 3.0:1 | Fail by construction — box-model parity with the outline pills; real boundary is 4.81:1 on canvas |
| canvas outline / canvas fill (button-icon-circular) | 1.0:1 | 3.0:1 | **Fail** (disclosed; intended over photography) |
| focus #25282b / canvas #ffffff | 14.82:1 | 3.0:1 | Pass |
| focus #25282b / canvas-soft #f2f2f2 | 13.24:1 | 3.0:1 | Pass |
| focus #25282b / primary #e60000 | 3.08:1 | 3.0:1 | Pass |
| focus-on-dark #ffffff / ink #25282b | 14.82:1 | 3.0:1 | Pass |
| focus-on-dark #ffffff / primary #e60000 | 4.81:1 | 3.0:1 | Pass |
| ink (divider-on-light) / canvas #ffffff | 14.82:1 | 3.0:1 | Pass |
| body (ex-* hairline) / canvas-soft #f2f2f2 | 3.63:1 | 3.0:1 | Pass |
| canvas #ffffff / canvas-soft #f2f2f2 | 1.12:1 | — | Layers not distinguishable; by design (depth is a polarity flip) |

Every surface this file defines — canvas, canvas-soft, ink, primary — is covered by one of the two rings at 3:1 or better, measured against the surface the ring is drawn *on* (2 px offset outside the control), which is what WCAG 2.2 Focus Appearance asks for.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `background-color`, `color`, `border-color` (paint only) | Colour change kept at 150ms; no travel to remove |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` 1 → 0.9 | Opacity step kept at `{motion.duration-reduced}`; no scale used |
| Focus | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | ring `opacity` + `box-shadow` paint | Ring appears immediately, no fade |
| Page / route transition | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | `opacity` + `translateY(8px)` | `opacity` only at 150ms |
| Modal / drawer | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(12px)` (drawer `translateX`), scrim `opacity` | `opacity` only at 150ms, no travel |
| Dropdown | 150ms in / 80ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(-4px)` | `opacity` only at 150ms |
| Toast | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | `opacity` only at 150ms |
| List enter | 250ms, `{motion.stagger-step}` 40ms | `{motion.ease-enter}` | `opacity` + `translateY(12px)` | Stagger 0, travel removed, one 150ms fade |
| List exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | `opacity` | `opacity` at 150ms, no stagger |
| Loading | 1200ms linear loop (the one permitted infinite animation) | linear | `transform: rotate()`, skeleton `opacity` pulse | Loop frozen, static indicator, steady opacity |

`{motion.duration-slow}` 400ms and `{motion.duration-emphasis}` 500ms are carried in the token block per profile but are not bound to an interaction in this file; the brand's heaviest moment is the hero photo fade, which sits at `{motion.duration-base}`.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 266-274 (`if not roles.get("border")` fallback) | The border fallback takes the **first** component declaring a `borderColor` and breaks. For vodafone that is `button-primary`, whose border is `{colors.primary}` — the CTA fill, at 3.99:1… but reported as the brand's *boundary* role while the file's actual hairline (`{colors.ink}`, 14.82:1, named in Elevation & Depth and bound by `text-input`) was invisible. A wrongly-satisfied role, per SPEC §1. | Collect every bound `borderColor` instead of breaking on the first, then pick with `find_role_strongest` against the canvas — or skip a candidate whose hex equals its own component's `backgroundColor` (a self-coloured edge is not a boundary) before choosing. The second half of that is already done in the bound-boundary check at line 513 but not in the role fallback. |
| `theme-audit/audit.py` line 715 (`NEGATED`) | The prohibition detector matches `\bno\b` but not `nothing`/`neither`/`none`, so the sentence "Nothing animates `width`, `height`, `top`, `left` or `margin`" — a prohibition — flagged the file for `animates-layout-props`. A file is penalised for stating the rule correctly in English. | Extend the alternation to `no(thing|ne)?|neither|nor|without`. I reworded my own file rather than leave a false positive, but the pattern will keep catching correct prose in other files. |
| `theme-audit/audit.py` lines 652-671 (`disclosed`) | Disclosure requires the failing pair's ratio to appear on a line that also names the foreground token or hex, and silently ignores any stated number equal to the `required` threshold. A file that writes `4.5:1` as its *measured* value for a pair whose requirement is 4.5 can never disclose it. Edge case, but it is a silent one. | Parse the disclosure row's columns rather than the whole line, or require the measured value to be the first ratio on the line. |
| `theme-audit/audit.py` (states check) | `NOT_DOCUMENTED` matches `n/?a\b`, which also fires on prose containing `n/a` inside an otherwise valid state list, and the cell-dropping heuristic means a single disclaimer can delete evidence of neighbouring states in the same row. | Match `\bn/a\b` with a leading boundary. |

Nothing in `README.md` or `CONTRIBUTING.md` was implicated.

### Needs approval

1. **`{colors.body}` #7e7e7e as normal-size text.** 4.06:1 on `{colors.canvas}`, 3.63:1 on `{colors.canvas-soft}`; AA needs 4.5:1. Nearest passing value: **#767676** (4.54:1 on white) for the canvas, **#6e6e6e** (4.55:1 on #f2f2f2, 5.1:1 on white) if one value must serve both grounds. Usage note that makes the real hex defensible: *restrict `{colors.body}` to 24 px+, or 18.66 px at weight 700+, where the 3:1 threshold applies — it clears 3:1 on both light grounds.* Not applied: this is an extracted brand value.
2. **`{colors.mute}` #bebebe as text.** 1.86:1 / 1.66:1. There is no usage note that makes this defensible as text at any size; it fails even the 3:1 large-text threshold. Nearest passing value for placeholder text: **#767676**. Nearest value that would merely work as a *boundary*: **#959595** (3.0:1 on white) or **#8c8c8c** (3.0:1 on #f2f2f2). A brand owner has to choose between the extracted tone and a readable placeholder.
3. **Re-binding the frozen tones.** SPEC §2 step 3 requires the extracted `components:` bindings be left as extracted, so `{colors.mute}`'s remaining role as placeholder text and low-key footer links stands in the document. Whether to re-point it to a passing tone in the real product is a brand-owner decision.
4. **`button-icon-circular` needs a hairline on light bands.** Over hero photography the white circle reads; on `{colors.canvas}` it is a 1.0:1 edge. Proposal: a 1 px `{colors.body}` (3.63-4.06:1) hairline, or a mandatory scrim behind the control. Not applied — it changes an extracted component's chrome.
5. **`{colors.primary}` as small text on `{colors.canvas-soft}`.** 4.3:1, short of 4.5:1. Usage note: red type on the soft band at 24 px+ only. Nearest passing red would darken the brand hex, which is out of bounds.

### Identity verdict

Still unmistakably Vodafone. The file's three load-bearing facts — one red accent and no second colour, weight-800 uppercase display against weight-300 sub-displays, and the 60 px pill on every interactive shape — are untouched, and everything added is anchored to them: the focus rings reuse the brand's own ink and paper rather than importing a conventional blue, the hover language in Motion & Animation is a paint flip to `{colors.primary}` rather than a borrowed scale pop, and the loading row animates the speechmark orb because that mark is the brand's stated centre of gravity. The Accessibility section is the only place the document now admits the brand is imperfect, and it does so about the grey ramp, which is the honest finding.

**Profile: Calm, kept.** Worth arguing, because the file reads cinematic in places: full-bleed editorial photography, sparse heroic type, a campaign-poster posture. But SPEC §5 rule 1 is a conjunction over *identity* — luxury, automotive, hardware-flagship, console, aerospace — and a consumer telecom operator is none of those; the photography is documentary (real portraits, real cities, real cabling), not a slow product reveal, there is no gradient or atmospheric system to choreograph, and the brand's own secondary voice is a weight-300 sentence after the shout. Rules 2 and 3 do not fire either (single accent, no illustration, no developer-tool register), so rule 4 is the terminal answer and Calm's 250ms opacity-led fades with little travel are the right fit. Nothing was switched.
