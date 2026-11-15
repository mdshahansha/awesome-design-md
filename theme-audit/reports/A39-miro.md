## A39 · miro

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 1 | 3 | 3 | 1 |
| After | 5 | 5 | 5 | 5 | 5 | 5 |

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A. Token contract | `colors.focus` | No focus role at all. Nothing in the file named a ring colour, so no keyboard affordance was specified for any of the ~45 interactive component entries. |
| P0 | H. States | `## Components` preamble | The file asserted a "no-hover policy" and documented no hover state anywhere. No such policy exists in this repo — `grep` over README.md and CONTRIBUTING.md finds nothing. It was a local invention that suppressed five of the eight SPEC §7 states. |
| P0 | F. Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. The only timing in the file was a Known Gaps line guessing "150–200ms ease", which is both unprescribed and off-profile. |
| P0 | B. Colour | `hairline-strong` on `canvas` | 1.64:1 against the 3:1 non-text minimum, and this is the *only* edge of `text-input`, `button-secondary` and `filter-dropdown`. A text field whose boundary is invisible is unusable, not merely imperfect. |
| P1 | G. Accessibility | whole file | No `## Accessibility` section. Nine palette-level and three component-level contrast failures were present and entirely undisclosed. |
| P1 | B. Colour | `badge-success` | `{colors.on-primary}` on `{colors.success-accent}` measures 2.7:1 on a 13px/600 label. A real failure in a semantic status component, where misreading has consequences. |
| P1 | B. Colour | `muted` | 2.37:1 on canvas, 2.23:1 on surface, and the Colors prose offered it for "input placeholders" — placeholders are read, so this was a documented instruction to fail AA. |
| P1 | B. Colour | `badge-tag-purple` | 4.33:1, a near miss on 4.5:1. Not large text (13px/600), so the 3:1 allowance does not apply. |
| P2 | B. Colour | `success-accent` as text | 2.7:1 on canvas. Fine as a fill, listed without qualification as a "Confirmation/success indicator". |
| P2 | E. Borders / radius | focus ring geometry | Nothing stated ring width, offset or corner behaviour, so a ring added later would sit outside the radius ladder. |
| P2 | A. Token contract | `blue-450`, `brand-coral`, `brand-teal`, `stone`, `ink-deep`, `surface-soft`, `brand-orange-light`, `brand-red`, `brand-red-dark` | Nine palette tokens are documented in prose but bound to no component. Left alone: they are extracted facts about the palette, and the SPEC's rule against pattern-filling aliases is a rule against *adding* such tokens, not a licence to prune extracted ones. |
| P2 | C. Elevation | `## Elevation & Depth` | Levels 0–4 are consistently expressed (level 0 = border, 1–4 = shadow, one `rgba(5,0,56,·)` family throughout) — no mixing. Canvas→surface is 1.06:1 and surface→surface-soft is 1.03:1, so the layers are not independently distinguishable; they rely on their borders. Left as extracted, disclosed in Accessibility via the hairline rows. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#4262ff"` | Closes the missing role. Not a new colour: this is Miro's own action blue, already documented as the `text-input-focused` border. One mid-luminance ring covers every surface in the file, so no `focus-on-dark` companion was invented. |
| frontmatter `colors:` | — -> `hairline-control: "#8a8d9c"` | SPEC §2 parallel accessible token. 3.3:1 on canvas, 3.1:1 on surface. The three extracted hairlines stay untouched and are scoped to decoration in the prose. Labelled prescribed. |
| frontmatter | — -> `motion:` group | Playful profile block from SPEC §5, verbatim, no deviation. |
| `## Colors` | — -> `hairline-control` entry + new `### Focus` subsection | Both new tokens get a documented job and a stated measured ratio; no dangling references. |
| `## Shapes` | — -> `### Focus Ring Geometry` | 2px ring, 2px outer offset, radius inherited from the control's own token, so the ring stays inside the existing radius ladder. |
| `## Components` preamble | "Per the no-hover policy, hover states are NOT documented" -> explicit note that default/pressed/disabled are extracted and the other five are prescribed | The claimed policy does not exist. Removing it is the root fix for the states score. |
| `## Components` | — -> `### State Coverage` table | 19 rows × 8 states. Non-interactive badges and static cells say outright that they genuinely have one state, as SPEC §7 requires, rather than being padded. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and not measured. Fourteen-row interaction table, motion rules, and a `@media (prefers-reduced-motion: reduce)` block naming what is removed, kept and frozen. |
| after Motion | — -> `## Accessibility` | 15 passing pairs, 12 disclosed failures with measured ratios, 12-surface focus-ring table, tap targets from documented box sizes, reduced-motion pointer. |
| `## Do's and Don'ts` | +3 Do, +3 Don't | Focus ring, control border, entrance-overshoot signature; the transform/opacity restriction and the two tones that must not be used as text. |
| `## Known Gaps` | "Animation/transition timings not extracted; recommend 150–200ms ease" -> explicit prescribed-not-measured note, plus entries for `hairline-control` and the prescribed states | The old line presented a guess as a recommendation with no provenance label. |

Not changed: every extracted hex, every extracted component border, and every typography value. No identity colour was altered to make a ratio pass.

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`, not estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink `#1c1c1e` / canvas `#ffffff` | 17.01:1 | 4.5:1 | Pass |
| ink / surface `#f7f8fa` | 16.01:1 | 4.5:1 | Pass |
| on-primary `#ffffff` / primary `#1c1c1e` | 17.01:1 | 4.5:1 | Pass |
| ink-deep `#050038` / canvas | 19.75:1 | 4.5:1 | Pass |
| charcoal `#2c2c34` / canvas | 13.84:1 | 4.5:1 | Pass |
| slate `#555a6a` / canvas | 6.87:1 | 4.5:1 | Pass |
| steel `#6b6f7e` / canvas | 5.0:1 | 4.5:1 | Pass |
| steel / surface | 4.71:1 | 4.5:1 | Pass |
| stone `#8e91a0` / canvas | 3.13:1 | 4.5:1 | Fail — exempt: `stone` is bound to no component, so the harness never asserts it as text |
| muted `#a5a8b5` / canvas | 2.37:1 | 4.5:1 | **Fail — disclosed** |
| muted / surface | 2.23:1 | 4.5:1 | **Fail — disclosed** |
| on-dark-muted `#a5a8b5` / footer-bg `#1c1c1e` | 7.19:1 | 4.5:1 | Pass |
| yellow-dark `#746019` / surface-yellow `#fff8e0` | 5.76:1 | 4.5:1 | Pass |
| coral-dark `#600000` / coral-light `#ffc6c6` | 9.45:1 | 4.5:1 | Pass |
| moss-dark `#187574` / teal-light `#c3faf5` | 4.77:1 | 4.5:1 | Pass |
| primary / brand-yellow `#ffd02f` | 11.6:1 | 4.5:1 | Pass |
| primary / coral-light | 11.46:1 | 4.5:1 | Pass |
| primary / teal-light | 14.84:1 | 4.5:1 | Pass |
| primary / rose-light `#fde0f0` | 13.85:1 | 4.5:1 | Pass |
| brand-blue `#4262ff` / canvas | 4.75:1 | 4.5:1 | Pass |
| brand-blue / surface-pricing-featured `#f5f3ff` (`badge-tag-purple`) | 4.33:1 | 4.5:1 | **Fail — disclosed** |
| on-primary / success-accent `#00b473` (`badge-success`) | 2.7:1 | 4.5:1 | **Fail — disclosed** |
| success-accent / canvas | 2.7:1 | 4.5:1 | **Fail — disclosed** |
| hairline-soft `#eef0f3` / canvas | 1.14:1 | 3.0:1 | **Fail — disclosed** |
| hairline-soft / surface | 1.07:1 | 3.0:1 | **Fail — disclosed** |
| hairline `#e0e2e8` / canvas | 1.3:1 | 3.0:1 | **Fail — disclosed** |
| hairline / surface | 1.22:1 | 3.0:1 | **Fail — disclosed** |
| hairline-strong `#c7cad5` / canvas | 1.64:1 | 3.0:1 | **Fail — disclosed** |
| hairline-strong / surface | 1.54:1 | 3.0:1 | **Fail — disclosed** |
| `footer-link` ink `#a5a8b5` / canvas | 2.37:1 | 4.5:1 | **Fail — disclosed**; 7.19:1 on the footer it is actually drawn on |
| hairline-control `#8a8d9c` / canvas *(prescribed)* | 3.3:1 | 3.0:1 | Pass |
| hairline-control / surface *(prescribed)* | 3.1:1 | 3.0:1 | Pass |
| hairline-control / surface-soft `#fafbfc` *(prescribed)* | 3.18:1 | 3.0:1 | Pass |
| **focus** `#4262ff` / canvas | 4.75:1 | 3.0:1 | Pass |
| focus / surface | 4.47:1 | 3.0:1 | Pass |
| focus / surface-soft | 4.58:1 | 3.0:1 | Pass |
| focus / surface-yellow `#fff8e0` | 4.47:1 | 3.0:1 | Pass |
| focus / surface-pricing-featured | 4.33:1 | 3.0:1 | Pass |
| focus / primary + footer-bg `#1c1c1e` | 3.58:1 | 3.0:1 | Pass |
| focus / brand-yellow | 3.24:1 | 3.0:1 | Pass |
| focus / coral-light | 3.2:1 | 3.0:1 | Pass |
| focus / teal-light | 4.14:1 | 3.0:1 | Pass |
| focus / rose-light + brand-pink | 3.87:1 | 3.0:1 | Pass |
| focus / brand-rose `#ffd8f4` | 3.7:1 | 3.0:1 | Pass |
| focus / brand-orange-light `#ffe6cd` | 3.95:1 | 3.0:1 | Pass |
| focus / yellow-light `#fff4c4` | 4.29:1 | 3.0:1 | Pass |
| focus / brand-red `#fbd4d4` | 3.5:1 | 3.0:1 | Pass |
| focus / brand-red-dark `#e3c5c5` | 2.95:1 | 3.0:1 | Fail, 0.05 short — `brand-red-dark` is an error *border*, never a surface a control sits on; stated as such in the file |
| focus / primary, as *fill* behind a white label | — | — | Not required: the ring is drawn outside the control at a 2px offset, so WCAG 2.2 Focus Appearance measures it against the surface behind, not the control fill |

Rejected single-ring alternative: `blue-pressed` `#2a41b6` reaches 8.3:1 on canvas but only 2.05:1 on `{colors.primary}`, so it cannot serve the dark footer, the dark CTA banner or the enterprise pricing card. `brand-blue` is the only value in the palette that clears 3:1 on both polarities.

Canvas / surface / raised separation, as a background-layer check: canvas→surface 1.06:1, canvas→surface-soft 1.03:1, surface→surface-soft 1.03:1, canvas→surface-pricing-featured 1.04:1. The layers are not distinguishable on their own luminance; every one of them is identified by its border or its radius instead. Disclosed through the hairline rows, not corrected — these are extracted hexes.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 130ms | `{motion.ease-standard}` | `opacity`, `transform: scale(1.02)` on cards | Colour only; scale removed, fade at 130ms |
| Press | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `transform: scale(0.96)` | Scale pop removed; fill applies with no travel |
| Focus | `{motion.duration-instant}` 70ms | `{motion.ease-standard}` | `opacity` on the 2px `{colors.focus}` ring | Ring appears instantly at full opacity |
| Page / route transition | `{motion.duration-base}` 200ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(8px)` | Fade only at 130ms; travel removed |
| Modal / drawer enter | `{motion.duration-base}` 200ms | `{motion.ease-enter}` | `opacity`, `transform: scale(0.97 → 1)` | Fade at 130ms; no scale, no overshoot |
| Modal / drawer exit | `{motion.duration-fast}` 130ms | `{motion.ease-exit}` | `opacity`, `transform: scale(1 → 0.98)` | Fade at 130ms; no scale |
| Dropdown enter | `{motion.duration-fast}` 130ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(-4px → 0)` | Fade at 130ms; no travel |
| Dropdown exit | `{motion.duration-instant}` 70ms | `{motion.ease-exit}` | `opacity` | Fade at 130ms |
| Toast enter | `{motion.duration-base}` 200ms | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px → 0)` | Fade at 130ms; no travel |
| Toast exit | `{motion.duration-fast}` 130ms | `{motion.ease-exit}` | `opacity`, `transform: translateY(0 → 6px)` | Fade at 130ms; no travel |
| List enter | `{motion.duration-base}` 200ms, `{motion.stagger-step}` 60ms between | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px → 0)` | Stagger to zero; all items fade together at 130ms |
| List exit | `{motion.duration-fast}` 130ms, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Fade at 130ms; no scale |
| Loading | `{motion.duration-emphasis}` 450ms loop | `linear` spinner / `{motion.ease-standard}` pulse | `transform: rotate()`, `opacity` | Spinner frozen; static `{colors.hairline-soft}` block replaces the pulse |
| Hero mockup ambience (stated as deliberate brand atmosphere) | `{motion.duration-emphasis}` 450ms loop | `{motion.ease-standard}` | `transform: translate()`, `opacity` | Frozen at rest frame |

Every exit is shorter than its entrance. Only `transform` and `opacity` are animated; the harness reports `layout_animation_mentions: []`. The three infinite animations are the spinner, the skeleton pulse and the hero ambience, and the ambience is labelled as such.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py:376–391` | **Resolved upstream, confirmed here.** The brief's pre-measured list for this site is stale: it was generated when the harness guessed text/background pairs by token name, which produced `on-primary on brand-orange-light` and `on-primary on brand-red-dark` for miro. Neither is a binding this file ever had. `grep` over the whole `components:` block shows `brand-orange-light`, `brand-red` and `brand-red-dark` appear **only** in the `colors:` block and the Colors prose — no component sets either as a `backgroundColor`, and `on-primary` is never placed on them. The current `parse_components` path measures declared pairs only and no longer emits them. No fix needed; flagged so the roster/brief regeneration is not read as a regression. |
| `theme-audit/audit.py:300–306` (`check` / semantic-tone loop) | `stone` `#8e91a0` is flagged nowhere even though the Colors prose offers it for "Captions, muted labels" at 3.13:1, while `muted` is flagged — the difference is only that `muted` happens to satisfy the `text-dim` role regex. A tone the prose assigns to text should be measured as text whether or not it won a role slot. | Extend the semantic-tone scan to any colour the Colors prose binds to a text role, or accept that prose-only text assignments are out of scope and say so in SPEC §2. |
| `theme-audit/audit.py:380–382` | Where a component declares a `textColor` and no `backgroundColor`, the harness substitutes the canvas. `footer-link` is explicitly a child of `footer-region` (`{colors.footer-bg}`), where its ink measures 7.19:1, but it is charged 2.37:1 against white. The failure is an artefact of the fallback, not of the design. | Honour a parent relationship, or add an optional `on:` key so a component can name the surface it is drawn on; until then the disclosure route is the only available answer, which is what this file now does. |
| `theme-audit/SPEC.md` §3 | The section table lists Motion & Animation and Accessibility between Components and Do's and Don'ts; the brief says only "after `## Components`". Order is unenforced by the harness. | State in SPEC §3 that the table's order is normative, so 84 files do not settle it 84 different ways. |

### Needs approval

Four real brand failures. Each is an extracted value, so none was changed in the file — all four are disclosed in `## Accessibility` with their measured ratio.

1. **`hairline-strong` `#c7cad5` as a control boundary — 1.64:1 on canvas, 1.54:1 on surface (needs 3:1).** This is the live border of `text-input`, `button-secondary` and `filter-dropdown`. Nearest passing value: `#8a8d9c` (3.3:1 / 3.1:1), added as the prescribed `{colors.hairline-control}` rather than substituted. Defensible usage note if the extracted value is kept: only where the control carries a second, independent boundary cue — a filled background, a persistent label, or an adjacent icon — since WCAG 1.4.11 exempts a boundary that is not required to identify the control. **`text-input` has no such second cue, so I do not think it is defensible there.**
2. **`muted` `#a5a8b5` as secondary text — 2.37:1 on canvas, 2.23:1 on surface (needs 4.5:1).** Nearest passing: `#6f727e` (4.79:1 / 4.51:1). Defensible usage note: restrict to genuinely decorative labels and to disabled text, which WCAG exempts. The Colors prose offers it for "input placeholders", which are read, so that one use is not defensible; `{colors.steel}` at 5.0:1 is the in-palette replacement.
3. **`badge-success` — white `#ffffff` on `#00b473` at 2.7:1 (needs 4.5:1).** Two routes, both in-palette or near it: swap the label to `{colors.primary}` on the same green, which measures 6.3:1 and changes no brand hex at all (**recommended**); or darken the fill to `#00804f` to keep white ink at 5.0:1, which does change an extracted hex. I did not apply either.
4. **`badge-tag-purple` — `{colors.brand-blue}` on `{colors.surface-pricing-featured}` at 4.33:1 (needs 4.5:1).** Nearest passing: `#3a59f5` (4.88:1), a 0.4% luminance move off the brand blue. Alternative defensible note: raise the chip label to 18.66px/700 so the 3:1 large-text threshold applies — but the chip is `{typography.caption-bold}` at 13px/600, and enlarging it would misdescribe the real component.

Also for approval, lower stakes: `{colors.focus}` reaches 2.95:1 against `{colors.brand-red-dark}` `#e3c5c5`, 0.05 short. I treated this as out of scope because `brand-red-dark` is documented as an error border and is bound to no component as a background, so no control is ever focused on top of it. If a reviewer wants full coverage regardless, the ring would have to darken past `#3a59f5`, which costs the brand-blue identity for a surface that does not exist.

### Identity verdict

**Still unmistakably Miro, and the Playful profile is correct — keep it.**

The additions are brand-specific rather than generic. The focus ring is not a new colour borrowed from a palette generator; it is Miro's own action blue, the value the file already documented as the focused-input border, which is why one ring serves both the white marketing canvas and the near-black footer without a `focus-on-dark` companion. The motion signature — `ease-enter` at `cubic-bezier(0.17, 0.89, 0.32, 1.28)`, overshooting and settling — is argued from the product itself: Miro is a direct-manipulation canvas where a dragged sticky note lands slightly past the cursor and settles, so the overshoot is a description of the product's physics, not a decorative flourish. The State Coverage table reuses the existing pastel and pill vocabulary (`pill-tab-active`, `button-primary-pressed`, the `brand-red` / `coral-dark` error pair) instead of importing a generic state ladder.

On the profile: Miro passes SPEC §5 rule 3 on both of its conjuncts, which is the test that usually fails for a brand with a large pastel palette. Saturated colour does land on interactive elements, not only on static cards behind screenshots — the canary-yellow pill, the blue CTA, the `{rounded.full}` pill applied to every button, tab and badge. And the type voice is informal: "See how teams get great done with Miro" is not editorial register, and Roobert PRO's rounded geometric character at weight 500 is friendly rather than sober. Nothing in the file says "sober" or "editorial", the display weight is 500 rather than 400, and gradients are not forbidden. Rule 1 does not fire (no luxury or hardware identity), rule 2 does not fire (collaboration product, not a developer tool), so rule 3 is the terminal answer. No switch argued.

The one honest risk to flag: this file is now substantially longer than it was, and the largest new block — the 19-row State Coverage table — is prescribed rather than extracted. It is labelled as such in three places (the Components preamble, the table's own note, and Known Gaps), but a reader skimming it could mistake prescription for measurement. That is the cost of closing the states gap in a document nobody rendered.
