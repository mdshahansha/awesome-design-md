## A59 · revolut

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 3 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Harness motion score 1. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section. No measured contrast stated anywhere, so every failure below was undisclosed. |
| P0 | A · Token contract | `colors` | No `focus` role. The file documents two signature polarities (`canvas-light` `#ffffff`, `canvas-dark` `#000000`) plus a cobalt featured-card surface, so one ring cannot serve it — two were required. |
| P0 | B · Colour | `hairline-light` `#e2e2e7` | 1.29:1 on `canvas-light`, 1.17:1 on `surface-soft`, against 3.0:1. It is the real 1px boundary of `text-input` and `feature-card-light`, so the brand fails WCAG non-text contrast on its own form control. Extracted, therefore frozen. |
| P0 | H · States | 21 component entries | Only `pressed` was documented anywhere. hover, focus-visible, active, disabled, loading, selected and error were absent from the Components section entirely. |
| P1 | B · Colour | `accent-warning` `#ec7e00` | 2.78:1 on `canvas-light` — fails the 4.5:1 text threshold *and* the 3:1 graphical threshold on white. The only listed accent that fails both. |
| P1 | B · Colour | `primary` `#494fdf` | 3.47:1 as text on `canvas-dark`. The file's Don'ts forbid cobalt prose but never state the ratio. |
| P1 | B · Colour | `link` / `accent-blue-link` `#376cd5` | 4.92:1 on white (passes) but 4.27:1 on `canvas-dark` (fails). The file names this token as the default inline link without distinguishing polarity. |
| P1 | B · Colour | `accent-danger` `#e23b4a` | 4.24:1 on white. Documented as the destructive/error state; narrowly fails AA for error text. |
| P1 | B · Colour | `stone` `#8d969e` | exactly 3.00:1 on white, documented for "metadata, subtle captions" — i.e. small text. Fails AA. |
| P1 | B · Colour | `accent-teal` 3.04:1, `accent-yellow` 3.07:1 | Fail 4.5:1 as text on white; clear 3:1 as illustration fills, which is the documented use. Needed stating, not fixing. Nearest passing as text: `#008766` (4.51:1) and `#8e7400` (4.52:1). |
| P1 | C · Elevation | surface ladder | `canvas-light`→`surface-soft` 1.10:1, `canvas-dark`→`surface-elevated` 1.18:1, `canvas-dark`→`surface-deep` 1.06:1. The layers are not perceptually distinguishable as boundaries; the file presents them as an elevation ladder without saying so. Elevation itself *is* expressed one consistent way (colour-blocking, no shadow, no `shadow:` group needed) — that part is clean. |
| P2 | D · Typography | all roles | Every role carries family, size, weight and line height; `body-sm`, `button-sm`, `caption`, `button-lg` carry no `letterSpacing`, which reads as 0 and is consistent with the stated principles. No fix needed. Body `body-md` on `surface-soft` measures 15.56:1 — readable on every surface the file defines. |
| P2 | E · Ladders | `spacing` | `xs: 6px` and `md: 14px` sit off the stated "multiples of 4 / 8 / 16" base. Left as extracted — padding values in `components:` (`14px 28px`, `13px 27px`) confirm 14px is real, so the prose claim is the loose part, not the token. Recorded here only. |
| P2 | A · Brief accuracy | `text-dim` | The brief lists `text-dim` as a missing role; the harness resolves it to `mute` `#505a63` (7.04:1 on white). No token added. See Shared issues. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#494fdf"`, `focus-on-dark: "#ffffff"` | Fills the one role SPEC treats as a real binding rather than an alias. Both reuse hexes the palette already owns (`primary`, `on-dark`); no new brand colour invented. Two rings because the file documents both polarities and a cobalt surface. |
| frontmatter | — -> `motion:` group | The **Cinematic** block from SPEC section 5, verbatim, no deviation. |
| `## Colors` | — -> new `### Focus` subsection | States which existing tones the rings reuse, their measured ratios, and the 2px ring / 2px offset drawn outside the control. |
| `## Components` intro | — -> one paragraph | Says plainly that only `default` and `pressed` were extracted and the rest is prescribed, so the added state lines cannot be mistaken for extracted facts. |
| `## Components`, 21 entries | — -> a `States:` line per entry | Covers default, hover, focus-visible, active/pressed, disabled, loading, selected, error where real. `hero-band-dark`, `hero-band-photo`, `product-mockup`, `badge-tag`, `badge-feature` are declared single-state with the reason (bands and labels are not controls). |
| `## Components` → `text-input` | — -> two added bullets | Scopes the frozen 1.29:1 `hairline-light` boundary to decoration, names `hairline-strong` (17.11:1) as the accessible boundary, and says the extracted binding is left as-is. Also corrects the error ink to `accent-deep-red` (10.01:1) rather than `accent-danger` (4.24:1). |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Ten-row interaction table, brand-ambience note, `prefers-reduced-motion` block. All values are `{motion.*}` references; only `transform` and `opacity` animate; every exit is shorter than its entrance. |
| after Motion | — -> `## Accessibility` | Passing table, a failures table naming every real failure with its ratio, surface-separation note, per-surface ring table, tap targets read from documented heights only, reduced motion. |
| `## Known Gaps` | 4 items -> 9 items | Labels prescribed motion, prescribed states and prescribed rings as prescribed; records the un-re-pointed `hairline-light` bindings; records that tap targets cannot be verified from a document. |

Nothing else in the file was reflowed. The brand description, token values, typography scale, Do's and Don'ts and Responsive Behavior are untouched.

### Contrast checks

All computed with WCAG 2.1 relative luminance, `python3` standard library only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#191c1f` / `canvas-light` `#ffffff` | 17.11:1 | 4.5:1 | Pass |
| `ink` / `surface-soft` `#f4f4f4` | 15.56:1 | 4.5:1 | Pass |
| `body` `#1f2226` / `canvas-light` | 15.97:1 | 4.5:1 | Pass |
| `mute` `#505a63` (text-dim) / `canvas-light` | 7.04:1 | 4.5:1 | Pass |
| `mute` / `surface-soft` | 6.40:1 | 4.5:1 | Pass |
| `charcoal` `#3a3d40` / `canvas-light` | 10.93:1 | 4.5:1 | Pass |
| `ash` `#5c5e60` / `canvas-light` | 6.51:1 | 4.5:1 | Pass |
| `on-dark` `#ffffff` / `canvas-dark` `#000000` | 21.00:1 | 4.5:1 | Pass |
| `on-dark` / `surface-elevated` `#16181a` | 17.80:1 | 4.5:1 | Pass |
| `on-primary` `#ffffff` / `primary` `#494fdf` | 6.06:1 | 4.5:1 | Pass |
| `on-primary` / `primary-bright` `#4f55f1` | 5.38:1 | 4.5:1 | Pass |
| `on-primary` / `primary-deep` `#3a40c4` | 7.75:1 | 4.5:1 | Pass |
| `hairline-strong` `#191c1f` / `canvas-light` | 17.11:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface-soft` | 15.56:1 | 3.0:1 | Pass |
| `focus` `#494fdf` / `canvas-light` | 6.06:1 | 3.0:1 | Pass |
| `focus` / `surface-soft` | 5.51:1 | 3.0:1 | Pass |
| `focus-on-dark` `#ffffff` / `canvas-dark` | 21.00:1 | 3.0:1 | Pass |
| `focus-on-dark` / `surface-deep` `#0a0a0a` | 19.80:1 | 3.0:1 | Pass |
| `focus-on-dark` / `surface-elevated` | 17.80:1 | 3.0:1 | Pass |
| `focus-on-dark` / `primary` | 6.06:1 | 3.0:1 | Pass |
| `accent-blue-link` `#376cd5` / `canvas-light` | 4.92:1 | 4.5:1 | Pass |
| `accent-light-blue` `#007bc2` / `canvas-light` | 4.55:1 | 4.5:1 | Pass |
| `accent-light-blue` / `canvas-dark` | 4.61:1 | 4.5:1 | Pass |
| `accent-light-green` `#428619` / `canvas-light` | 4.51:1 | 4.5:1 | Pass |
| `accent-green-text` `#006400` / `canvas-light` | 7.44:1 | 4.5:1 | Pass |
| `accent-pink` `#e61e49` / `canvas-light` | 4.52:1 | 4.5:1 | Pass |
| `accent-deep-red` `#8b0000` / `canvas-light` | 10.01:1 | 4.5:1 | Pass |
| `accent-brown` `#936d62` / `canvas-light` | 4.56:1 | 4.5:1 | Pass |
| `accent-teal` `#00a87e` / `canvas-dark` | 6.90:1 | 4.5:1 | Pass |
| `accent-danger` `#e23b4a` / `canvas-dark` | 4.96:1 | 4.5:1 | Pass |
| `hairline-light` `#e2e2e7` / `canvas-light` | 1.29:1 | 3.0:1 | **Fail** — extracted, frozen, disclosed |
| `hairline-light` / `surface-soft` | 1.17:1 | 3.0:1 | **Fail** — extracted, frozen, disclosed |
| `stone` `#8d969e` / `canvas-light` | 3.00:1 | 4.5:1 | **Fail** — disclosed |
| `accent-teal` / `canvas-light` | 3.04:1 | 4.5:1 | **Fail** as text; passes 3:1 graphical |
| `accent-yellow` `#b09000` / `canvas-light` | 3.07:1 | 4.5:1 | **Fail** as text; passes 3:1 graphical |
| `accent-warning` `#ec7e00` / `canvas-light` | 2.78:1 | 4.5:1 | **Fail** both thresholds |
| `accent-danger` / `canvas-light` | 4.24:1 | 4.5:1 | **Fail** — disclosed |
| `link` `#376cd5` / `canvas-dark` | 4.27:1 | 4.5:1 | **Fail** — disclosed |
| `primary` / `canvas-dark` (as text) | 3.47:1 | 4.5:1 | **Fail** — disclosed; passes as a surface |
| `faint` `#c9c9cd` / `canvas-light` | 1.65:1 | — | Disabled foreground; no WCAG requirement |

Layer separation (not a WCAG threshold, recorded for dimension C):
`canvas-light`/`surface-soft` 1.10:1 · `canvas-dark`/`surface-deep` 1.06:1 ·
`canvas-dark`/`surface-elevated` 1.18:1 · `surface-deep`/`surface-elevated` 1.11:1 ·
`canvas-dark`/`primary` 3.47:1.

Composited tokens `on-dark-mute` `rgba(255,255,255,0.72)`, `hairline-dark`
`rgba(255,255,255,0.12)` and `divider-soft` `rgba(255,255,255,0.06)` are not
measurable without a stated backdrop and were not estimated.

### Motion inventory

Prescribed, not extracted. Cinematic profile, SPEC section 5 block verbatim.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity` | Opacity only at 150ms |
| Press | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `transform: scale(0.98)` | Scale removed; colour change only |
| Focus | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` on ring | Instant, full opacity, never suppressed |
| Page / route transition | 600ms in / 240ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(16px)` | Travel removed; cross-fade at 150ms |
| Hero band reveal | `{motion.duration-emphasis}` 900ms, 80ms stagger | `{motion.ease-enter}` | `opacity` + `translateY(24px)` | Travel and stagger removed; one fade at 150ms |
| Modal / drawer | 400ms in / 240ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` scrim + `translateY(100%)` or `scale(0.98)` | Travel and scale removed; fade at 150ms |
| Dropdown | 240ms in / 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(-8px)` | Travel removed; fade at 150ms |
| Toast | 400ms in / 240ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(16px)` | Travel removed; fade at 150ms |
| List enter | 600ms per item, 80ms stagger | `{motion.ease-enter}` | `opacity` + `translateY(20px)` | Travel and stagger removed; all fade at 150ms |
| List exit | 240ms, no stagger | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | Scale removed; fade at 150ms |
| Loading (indeterminate) | 900ms cycle, infinite | linear rotate / `{motion.ease-standard}` pulse | `transform: rotate()` or `opacity` | Rotation frozen; 150ms pulse or static labelled indicator |
| Brand ambience (full-bleed mockup) | 900ms, scroll-tied, not looping | `{motion.ease-standard}` | `transform: scale(1 → 1.04)` | Frozen at `scale(1)` |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/briefs/A59-revolut.md` line 12 | The brief states "Missing colour roles: focus, text-dim". The harness resolves `text-dim` to `mute` `#505a63`, and did so before any edit. The brief's pre-measured list is wrong on this point. Per the settled rule I did not add an alias to satisfy the claim. | Regenerate the briefs' pre-measured role list from the same resolver the harness uses, so a brief cannot name a role the harness already resolves. If 84 briefs were generated from a stale run, the other 83 may carry the same drift. |
| `theme-audit/audit.py`, `durations_found` | The field collects bare integers (`80`, `150` here) that come from `stagger-step` and `duration-reduced`, mixing stagger and animation durations into one list. Harmless for scoring, misleading to read. | Report stagger separately from durations, or key the list by token name. |
| `theme-audit/SPEC.md` section 2 | The frozen-tone paragraph (lines ~128-139) contains a duplicated "Then" clause and reads as two merged drafts, which makes the parallel-token instruction ambiguous on first pass. | Collapse to one sentence sequence: add the parallel token, scope the original in prose, label the new one prescribed, state the AA failure, put re-binding under Needs approval. |

### Needs approval

1. **Re-binding the `text-input` boundary.** `text-input` and `feature-card-light` are documented with a 1px `{colors.hairline-light}` `#e2e2e7` border, measuring 1.29:1 on `#ffffff` against the 3.0:1 a control boundary needs. The binding is left exactly as extracted. Nearest passing value already in the palette: `{colors.hairline-strong}` `#191c1f` at 17.11:1; a softer passing option outside the palette is `#949498` at 3.02:1 (the lightest neutral on this hue that clears 3:1 on white). Usage note that makes the real value defensible: `hairline-light` is decoration between rows already separated by 32px+ whitespace, never the sole boundary of an interactive control. A brand owner should decide whether the real site's input border is re-pointed.
2. **`accent-warning` `#ec7e00` on white.** 2.78:1 — fails the graphical 3:1 threshold as well as the text threshold, so it is not defensible on white at any size. Nearest passing value for 3:1 graphical on white: `#e37900` (3.00:1); for 4.5:1 text: `#b56000` (4.53:1). Alternatively restrict it to `{colors.canvas-dark}`, where it measures 7.55:1. This needs a brand decision because the orange is an identity colour in the product illustrations.
3. **`accent-danger` `#e23b4a` as error text on white.** 4.24:1. Nearest passing value `#da3947` (4.51:1), or keep the hex and restrict it to 18.66px+/14px bold, or use the existing `{colors.accent-deep-red}` `#8b0000` (10.01:1) for inline error text — which is what I wrote into the `text-input` error state.
4. **`stone` `#8d969e` for metadata.** 3.00:1. Defensible only at 18.66px+ regular or 14px+ bold; the file documents it for "metadata, subtle captions", which are 13-14px regular. Nearest passing value `#70777e` (4.54:1).
5. **`link` `#376cd5` on the dark canvas.** 4.27:1. Nearest passing value `#3970dc` (4.53:1 on black); or scope the token to white surfaces only and use the existing `{colors.accent-light-blue}` `#007bc2` (4.61:1) on dark, which is what the file's own prose already implies.
6. **`primary` `#494fdf` as text on black.** 3.47:1. No approval is needed to keep it, because the file already forbids cobalt prose; recorded only so the number is on the table. The nearest passing lightening is `#585fff` (4.50:1 on black), which would break the "don't introduce a secondary brand colour" rule, so the correct answer is the existing restriction, not a new hex.
7. **The two focus rings.** Both are prescribed bindings onto existing hexes, not extracted facts. If Revolut's real focus treatment is known, it should replace them.

### Identity verdict

The file still reads as Revolut. The two-mode band rhythm, the white-pill-on-black primary CTA, the scarce cobalt stamp, Aeonik Pro 500 at 136px with `lineHeight: 1.0`, and the illustration-only accent palette are all untouched; nothing was genericised and no value was imported from another file in the collection. The additions lean on the file's own vocabulary — the rings reuse `primary` and `on-dark`, the accessible boundary is the palette's own `hairline-strong`, the error ink is the palette's own `accent-deep-red`, and the motion section's signature interaction is the brand's own full-bleed mockup band rather than a generic card lift.

**Cinematic is the right profile and I kept it.** The assignment rule's rule 1 fires on signals, not on sector: full-bleed photography (the file's own words: "the asset IS the section"), sparse type at 80-136px, and a slow reveal. Revolut is fintech, not luxury, but the marketing canvas it documents behaves exactly like a hardware-flagship page — true-black storytelling bands hosting a single phone or metal-card mockup as the whole section, with one display headline and one pill. The counter-argument for Playful is weak on SPEC's own test: the palette lists eight saturated accents, but the file forbids them on interactive elements ("never as button surfaces"), the display weight is 500 not a light informal voice, and the description itself says the system carries the consumer-financial feel "without crossing into playful territory". Crisp is wrong because the brand's whole depth language is atmospheric rather than tool-like. Calm would be the fallback if rule 1 did not fire, but it does: a 150ms state change would make a 136px headline over full-bleed photography feel cheap.
