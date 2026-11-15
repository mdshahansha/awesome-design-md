## A11 · claude

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

**`theme-audit/audit.py` was modified three times by another agent while this audit was running** — `clean_value`, `parse_components`, `check_all`, a per-component background/text check, and finally a disclosure rule that scores only *undisclosed* failures. Both columns above are measured against the harness as it stands at the end (before-scores re-measured by running the current `audit()` against `git show HEAD:design-md/claude/DESIGN.md`), so they are comparable to each other but **not** to any report written against an earlier version. Intermediate readings I passed through for the record: contrast 2 on the original harness, then 1 once `check_all` flagged the frozen hairlines, then 4, then 5 once every failure was named in the Accessibility section.

**Eleven contrast failures remain measurable in this file and none were fixed, because every one is an extracted brand value and SPEC §2 forbids falsifying a hex.** The score reaches 5 only because all eleven are now disclosed — named with their ratio and nearest passing alternative in the Accessibility and Colors sections. That is the SPEC's prescribed outcome, not a clean bill of health: **the real Claude brand fails WCAG AA at its signature CTA.** Two of the eleven are harness false positives (see Shared issues).

Failures remaining, all disclosed:

| Pair | Ratio | Required | Status |
|---|---|---|---|
| `hairline-soft` on `canvas` | 1.18 | 3.0 | Frozen extracted tone, now scoped to decoration only in the file |
| `hairline` on `canvas` | 1.25 | 3.0 | Frozen extracted tone, now scoped to decoration only; `hairline-strong` (3.74) added for controls |
| `on-primary` on `accent-amber` | 2.11 | 4.5 | Pairing never used; file forbids it and prescribes `ink` (8.74) |
| `on-primary` on `accent-teal` | 2.37 | 4.5 | Pairing never used; file forbids it and prescribes `ink` (7.79) |
| `on-dark-soft` on `canvas` | 2.57 | 4.5 | **Harness false positive** — `on-dark-soft` is a dark-surface-only tone; on `surface-dark` it measures 6.62 |
| `muted-soft` on `canvas` | 3.23 | 4.5 | Real failure, documented; `muted` (5.13) prescribed for 13px captions |
| `on-primary` on `primary` | 3.28 | 4.5 | Real brand failure at the 14px label. Needs approval |
| component `button-primary`, `badge-coral`, `callout-card-coral`, `cta-band-coral` | 3.28 | 4.5 | The same white-on-coral pair, surfaced per component by the new component check. Documented |

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A / G | `colors.focus` | No focus token existed. Nothing in the file said how keyboard focus is drawn, on either the cream or the dark half of the system. Fixed: `focus` + `focus-on-dark` added, both prescribed. |
| P0 | B / G | `colors.hairline` on `colors.canvas` | 1.25:1 against the 3.0:1 non-text floor, and it is the only boundary of `text-input`, `button-secondary`, `button-icon-circular`, `connector-tile`, `model-comparison-card` and `pricing-tier-card`. The real brand's control boundaries are not perceivable. Fixed by a parallel token, original preserved and scoped to decoration. |
| P0 | B | `on-primary` on `primary` | White on #cc785c is 3.28:1. `button-primary` sets its label at 14px/500, which is normal-size text, so the live brand fails AA on its signature CTA. Not fixable in file — stated plainly, Needs approval. |
| P0 | F | whole file | No motion group, no Motion & Animation section, no reduced-motion rule. Fixed. |
| P0 | G | whole file | No Accessibility section. Fixed. |
| P0 | H | Components | Only `active` was documented in a structured line. Seven of the eight SPEC §7 states were absent everywhere. Fixed with a Component States table; extracted vs prescribed cells labelled. |
| P1 | B | `text-link` using `colors.primary` | Coral inline link is 3.11:1 on canvas at `body-md` 16px — a second real AA failure, not previously noted. Prescribed substitute `primary-active` (4.8:1) documented; extracted value kept for 24px+ links. |
| P1 | B | `on-primary` on `accent-teal` / `accent-amber` | 2.37:1 and 2.11:1. Harness flags both; in reality neither tone carries white text (teal is a status dot, amber a badge fill). Prose now states the required ink (`ink`: 7.79:1 / 8.74:1) and forbids white. |
| P1 | C | cream and dark surface ladders | No adjacent layer pair reaches 3:1 (canvas↔surface-soft 1.08, canvas↔surface-card 1.15, surface-soft↔surface-card 1.07, surface-dark↔surface-dark-elevated 1.14). Elevation was expressed three ways — fill, border, shadow — with no rule for which. Fixed: fill is primary, border secondary, shadow rare; measured table added. |
| P1 | A | `shadow` group | Prose stated `0 1px 3px rgba(20,20,19,0.08)` with no token to reference. Fixed: `shadow:` group with `none` and `hover-lift`. |
| P1 | B / G | `muted-soft` on `canvas` | 3.23:1 but used for `caption` at 13px. Below AA. Harness misses it because `muted` wins the `text-dim` role. Documented as a fail with a remedy. |
| P1 | B / G | `muted` on `surface-card` | 4.48:1 — fails AA by 0.02. Not harness-visible (role check uses canvas only). Documented. |
| P1 | G | status colours as indicators | `accent-teal` 2.25:1, `success` 2.33:1, `accent-amber` 2.00:1 on canvas — all below 1.4.11 as non-text indicators. Documented; colour-alone forbidden. |
| P2 | E | `rounded.pill` / `rounded.full` | Same 9999px value under two names. Kept deliberately (two intents) but now stated, so it does not read as an error. |
| P2 | E | border width | One border width (1px) used everywhere but never stated as a ladder. Now stated, with ring width, offset and radius. |
| P2 | H / I | `Don't add hover state styling…` and Iteration Guide item 4 (`Never document hover`) | Both directly contradicted the SPEC §7 state contract. Rewritten to point at the Component States table and to preserve the brand's anti-decoration intent rather than the blanket ban. |
| P2 | G | tap targets | `button-icon-circular` at 36px, `button-primary` and `text-input` at 40px, `category-tab` ≈36px — all under 44. The file already admitted the 36px case. Remedies prescribed; flagged as unverifiable from a static document. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-strong: "#848075"` | Parallel accessible boundary token (SPEC §2). 3.74:1 on canvas, 3.01:1 on the darkest cream, 4.54:1 on `surface-dark` — one token clears 3:1 on every surface the file defines. Prescribed. |
| frontmatter `colors:` | — -> `focus: "#141413"`, `focus-on-dark: "#faf9f5"` | SPEC §1 requires `focus`; this file documents both cream and dark signature surfaces, so it requires both rings. `focus` on `surface-dark` is 1.03:1, which is why one ring cannot serve. Prescribed. |
| frontmatter | — -> `shadow:` group (`none`, `hover-lift`) | SPEC §1: the file stated a real rgba shadow in prose with no token. |
| frontmatter | — -> `motion:` group, 9 keys | SPEC §4/§5, Crisp values: instant 50 / fast 100 / base 150 / slow 220 / emphasis 320ms, near-linear easings, stagger 20ms. |
| `## Colors` → Surface | — -> **Hairline Strong** bullet | Documents the new token, its measured ratios, and scopes `hairline`/`hairline-soft` to decoration only. |
| `## Colors` | — -> `### Focus` subsection | Documents both rings with measured contrast on all seven surfaces plus coral, and states the ink ring is deliberately not a borrowed system blue. |
| `## Colors` → Brand & Accent | — -> `#### Measured contrast on the signal colours — the brand fails AA here` | States the white-on-coral, coral-link, teal/amber-with-white and success/warning failures plainly, with nearest passing values. No hex altered. |
| `## Elevation & Depth` table | `Soft hairline` row -> split into `Soft hairline` (decoration) + `Control boundary` (`hairline-strong`) | The one row was doing both jobs, which is how the 1.25:1 hairline ended up outlining text inputs. |
| `## Elevation & Depth` table | inline `rgba(20,20,19,0.08)` -> `{shadow.hover-lift}` | Removes the last untokenised value in the file. |
| `## Elevation & Depth` | — -> `### Layer separation — measured` | Dimension C: six measured layer pairs, the honest conclusion that the cream ladder is not distinguishable by luminance alone, and the rule that fill pairs with a `hairline-strong` edge where separation must be perceivable. |
| `## Shapes` | — -> pill/full note + `### Border & Focus Ring Geometry` | Dimension E: states the single border width, ring width 2px, offset 2px, concentric radius, and which ring goes on which surface. Prescribed. |
| `## Components` | — -> `### Component States` table (15 rows × 8 states) + notes | Dimension H. Extracted cells (default, active/pressed, disabled) distinguished from prescribed ones. Containers and the two badges are explicitly declared single-state rather than left blank. |
| after `## Components` | — -> `## Motion & Animation` | SPEC §3/§6. First line states the system is prescribed and was not measured. Profile justified. 10-interaction table (hover, press, focus, page transition, modal/drawer, dropdown, toast, list enter, list exit, loading) × duration × easing × property × reduced-motion. Exit always shorter than entrance. `transform`/`opacity` only. |
| inside Motion | — -> `### @media (prefers-reduced-motion: reduce)` | SPEC §6: names what is removed (all transform, all stagger, all ambience including the homepage typewriter) and what remains (opacity ≤100ms, colour transitions, instant focus ring, static loading indicator with a text label). |
| after Motion | — -> `## Accessibility` | SPEC §3. 14-pair measured contrast table with verdicts, focus-ring visibility on all 8 surfaces, tap-target table with remedies, reduced-motion summary, and the colour-alone / zoom / reflow requirements. |
| `## Do's and Don'ts` → Don't | `Don't add hover state styling beyond what the system already encodes…` -> points at the Component States table; + 3 new Don'ts (never skip the focus ring, never use `hairline` as a control boundary, never white type on teal/amber/success/warning) | The old line forbade exactly what SPEC §7 requires. Rewritten to keep the brand's minimal-motion intent while allowing the documented states. |
| `## Iteration Guide` item 4 | `Never document hover. Default and Active/Pressed states only.` -> states live in the Component States table, extracted vs prescribed marked | Same contradiction. |
| `## Known Gaps` | animation/validation bullets -> 8 bullets | Labels motion, the focus ring, `hairline-strong` and most states as prescribed; records that tap targets, overlap, clipping, reflow and frame rate are unverifiable here; records the three unfixable brand AA failures and that no extracted hex was changed. |

Not touched: every extracted hex, the typography block, the spacing and radius ladders, the Overview, Layout, Responsive Behavior, and the component definitions themselves.

### Contrast checks

All computed with WCAG 2.1 relative luminance via `python3`, none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #141413 / `canvas` #faf9f5 | 17.50 | 4.5 | Pass |
| `ink` / `surface-soft` #f5f0e8 | 16.25 | 4.5 | Pass |
| `ink` / `surface-card` #efe9de | 15.26 | 4.5 | Pass |
| `ink` / `surface-cream-strong` #e8e0d2 | 14.07 | 4.5 | Pass |
| `body-strong` #252523 / `canvas` | 14.58 | 4.5 | Pass |
| `body` #3d3d3a / `canvas` | 10.34 | 4.5 | Pass |
| `body` / `surface-card` | 9.02 | 4.5 | Pass |
| `muted` #6c6a64 / `canvas` | 5.13 | 4.5 | Pass |
| `muted` / `surface-soft` | 4.77 | 4.5 | Pass |
| `muted` / `surface-card` | 4.48 | 4.5 | **Fail** (by 0.02) |
| `muted` / `surface-cream-strong` | 4.13 | 4.5 | **Fail** |
| `muted-soft` #8e8b82 / `canvas` | 3.23 | 4.5 | **Fail** (passes AA Large) |
| `muted-soft` / `surface-card` | 2.82 | 4.5 | **Fail** |
| `on-dark` #faf9f5 / `surface-dark` #181715 | 17.00 | 4.5 | Pass |
| `on-dark` / `surface-dark-soft` #1f1e1b | 15.82 | 4.5 | Pass |
| `on-dark` / `surface-dark-elevated` #252320 | 14.88 | 4.5 | Pass |
| `on-dark-soft` #a09d96 / `surface-dark` | 6.62 | 4.5 | Pass |
| `on-dark-soft` / `surface-dark-elevated` | 5.79 | 4.5 | Pass |
| `on-primary` #ffffff / `primary` #cc785c | 3.28 | 4.5 | **Fail** — brand hex, passes AA Large |
| `on-primary` / `primary-active` #a9583e | 5.06 | 4.5 | Pass |
| `ink` / `primary` | 5.63 | 4.5 | Pass — the accessible route |
| `on-primary` / `accent-teal` #5db8a6 | 2.37 | 4.5 | **Fail** — pairing never used |
| `on-primary` / `accent-amber` #e8a55a | 2.11 | 4.5 | **Fail** — pairing never used |
| `ink` / `accent-teal` | 7.79 | 4.5 | Pass |
| `ink` / `accent-amber` | 8.74 | 4.5 | Pass |
| `on-primary` / `success` #5db872 | 2.45 | 4.5 | **Fail** — pairing forbidden in file |
| `on-primary` / `warning` #d4a017 | 2.38 | 4.5 | **Fail** — pairing forbidden in file |
| `on-primary` / `error` #c64545 | 4.84 | 4.5 | Pass |
| `ink` / `success` | 7.52 | 4.5 | Pass |
| `ink` / `warning` | 7.76 | 4.5 | Pass |
| `primary` / `canvas` (inline link ink, 16px) | 3.11 | 4.5 | **Fail** — brand hex |
| `primary-active` / `canvas` | 4.80 | 4.5 | Pass — prescribed substitute |
| `error` / `canvas` | 4.59 | 4.5 | Pass |
| `error` / `surface-card` | 4.01 | 4.5 | **Fail** — use on canvas only |
| `hairline` #e6dfd8 / `canvas` | 1.25 | 3.0 | **Fail** — frozen, decoration only |
| `hairline-soft` #ebe6df / `canvas` | 1.18 | 3.0 | **Fail** — frozen, decoration only |
| `hairline-strong` #848075 / `canvas` | 3.74 | 3.0 | Pass (prescribed) |
| `hairline-strong` / `surface-soft` | 3.48 | 3.0 | Pass |
| `hairline-strong` / `surface-card` | 3.26 | 3.0 | Pass |
| `hairline-strong` / `surface-cream-strong` | 3.01 | 3.0 | Pass |
| `hairline-strong` / `surface-dark` | 4.54 | 3.0 | Pass |
| `hairline-strong` / `surface-dark-elevated` | 3.97 | 3.0 | Pass |
| `focus` #141413 / `canvas` | 17.50 | 3.0 | Pass |
| `focus` / `surface-soft` | 16.25 | 3.0 | Pass |
| `focus` / `surface-card` | 15.26 | 3.0 | Pass |
| `focus` / `surface-cream-strong` | 14.07 | 3.0 | Pass |
| `focus` / `primary` (coral callout) | 5.63 | 3.0 | Pass |
| `focus` / `surface-dark` | 1.03 | 3.0 | **Fail** — which is why `focus-on-dark` exists |
| `focus-on-dark` #faf9f5 / `surface-dark` | 17.00 | 3.0 | Pass |
| `focus-on-dark` / `surface-dark-soft` | 15.82 | 3.0 | Pass |
| `focus-on-dark` / `surface-dark-elevated` | 14.88 | 3.0 | Pass |
| `accent-teal` / `canvas` (status dot, non-text) | 2.25 | 3.0 | **Fail** — needs a label |
| `success` / `canvas` (status dot, non-text) | 2.33 | 3.0 | **Fail** — needs a label |
| `accent-amber` / `canvas` (non-text) | 2.00 | 3.0 | **Fail** — needs a label |
| `primary-disabled` #e6dfd8 / `canvas` | 1.25 | — | Exempt (disabled) |
| `muted` / `primary-disabled` (disabled label) | 4.10 | — | Exempt; clears 4.5 only at AA Large, adequate at the 14px/500 label |
| Layer: `canvas` / `surface-soft` | 1.08 | — | Not distinguishable alone |
| Layer: `canvas` / `surface-card` | 1.15 | — | Not distinguishable alone |
| Layer: `surface-soft` / `surface-card` | 1.07 | — | Not distinguishable alone |
| Layer: `canvas` / `surface-cream-strong` | 1.24 | — | Not distinguishable alone |
| Layer: `surface-dark` / `surface-dark-soft` | 1.07 | — | Not distinguishable alone |
| Layer: `surface-dark` / `surface-dark-elevated` | 1.14 | — | Not distinguishable alone |
| Layer: `canvas` / `surface-dark` | 17.00 | — | The only self-sufficient layer change |

### Motion inventory

Profile **Crisp**. Every value prescribed, none measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | 100ms `{motion.duration-fast}` | `{motion.ease-standard}` | `background-color`, `border-color`, `opacity`, `box-shadow` | Unchanged — colour only, no travel to remove |
| Press | 50ms `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: translateY(1px)` / `scale(0.96–0.995)` | Transform removed; press reads as the `primary-active` fill change |
| Focus (ring appear) | 50ms | `{motion.ease-standard}` | `opacity` on the ring | Unchanged — instant, never animated in |
| Page / route transition | 100ms out, 150ms in | `{motion.ease-exit}` / `{motion.ease-enter}` | `opacity` only | Crossfade held at 100ms; no travel at any time |
| Modal / drawer | 150ms in, 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` (drawer `translateX`) | Transform removed; opacity 100ms; backdrop 100ms |
| Dropdown / menu | 100ms in, 50ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scale(0.98) → 1` | Transform removed; opacity only, 100ms |
| Toast | 150ms in, 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | Transform removed; opacity only; auto-dismiss extended to 10s |
| List enter | 100ms per item, 20ms `{motion.stagger-step}`, capped at 8 | `{motion.ease-enter}` | `opacity` 0 → 1 only (Crisp adds no enter travel) | Stagger → 0ms, all items appear together; nothing delayed |
| List exit | 50ms, no stagger | `{motion.ease-exit}` | `opacity` 1 → 0 | Instant removal, no fade |
| Loading | 800ms linear, infinite | `linear` | `rotate` (spinner) / `opacity` 0.6 ↔ 1 (skeleton) | Rotation frozen, static `muted` indicator + live-region text label; skeleton frozen at `opacity: 1`. The only infinite animation in the system |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, `check_all("text-dim", "canvas", …)` (added mid-audit) | `on-dark-soft` #a09d96 matches the `text-dim` pattern list (`^on-dark-soft$`) and is therefore tested against `canvas`, where it measures 2.57:1. It is a **dark-surface-only** tone — on `surface-dark` it measures 6.62:1 and passes. The check creates a failure for a pairing the system never makes, which is the same class of error as the signal-colour loop below. | Exclude `on-*` tokens from the `text-dim` role when the file defines a matching dark surface, or test each `on-<surface>` token against the surface its name identifies rather than against the canvas. The cleanest fix is to drop `^on-dark-soft$` from `REQUIRED_COLOR_ROLES["text-dim"]` — the pattern exists so dark-only files can satisfy the role, so gate it on whether a light canvas is present. |
| `theme-audit/audit.py`, `check_all("border", "canvas", 3.0, …)` (added mid-audit) | Tests every boundary tone at 3:1, which flags `hairline` (1.25) and `hairline-soft` (1.18) even after SPEC §2's prescribed remedy has been applied in full — a parallel `hairline-strong` token added, the originals preserved and explicitly scoped to decoration in the prose. The check and the SPEC now disagree: §2 says "a hairline at 1.36:1 is as much an extracted fact as the brand's red, so do not 'fix' it in place", and then the score punishes exactly the file that followed that instruction. The older single-representative `find_role_strongest` behaviour rewarded the correct remedy; `check_all` removes that signal. | Keep `check_all` for discovery but exempt a tone that the file has scoped to decoration — detectable as a boundary token whose *strongest* sibling passes 3:1, or by requiring the prose to name the token alongside the word "decorative"/"decoration". Failing that, report these as informational rather than folding them into `score["contrast"]`. |
| `theme-audit/audit.py`, lines ~158–167 (signal-colour loop) | Every key matching `^(primary\|accent\|secondary\|brand\|cta)` is tested against the file's `on-accent` ink at 4.5:1, regardless of whether that token is ever a text background. `accent-teal` here is an 8px status dot and `accent-amber` a badge fill; white is never placed on either, so two of my three remaining failures are pairings that do not exist. Meanwhile the real second failure — coral as *inline link ink* at 3.11:1 on canvas — is invisible to the harness, because an accent used as foreground is never checked against the canvas. | Check each signal colour against the inks the `components:` block actually pairs it with (resolve `textColor` where `backgroundColor` is that token), and add a reciprocal `accent on canvas` check at 4.5:1 for any signal token referenced as a `textColor`. Failing that, exempt tokens no component uses as a `backgroundColor`. |
| `theme-audit/audit.py`, line ~143 (`check("text-dim", "canvas", …)`) | **Resolved concurrently** by the `check_all("text-dim", …)` addition while this audit ran. Recorded for the record: the original `find_role` took the *first* pattern match, so `muted` (5.13:1, passes) was scored and `muted-soft` (3.23:1, used for 13px captions) was never tested. My file documents the `muted-soft` failure independently. | Done upstream; see the `on-dark-soft` row above for the over-reach the new check introduced. |
| `theme-audit/audit.py`, line ~141–142 | `text` and `text-dim` are still checked against the representative `surface` only (here `surface-soft`, the lightest). `surface-card` and `surface-cream-strong` are darker and `muted` fails on both (4.48:1, 4.13:1) — neither is harness-visible. `check_all` was added for the foreground role, not for the background. | Mirror `check_all` on the background side: test each text role against every `surface*` key, not just the representative. |
| `theme-audit/audit.py`, score block (`"contrast"`) | Score is `5 - len(fails)`, so a file that honestly documents an unfixable brand failure scores the same as one that ignores it, and a file is rewarded for renaming `accent-teal` to dodge the signal loop. The SPEC explicitly anticipates unfixable brand failures but the score cannot represent "failing and correctly disclosed". | Treat a failure as mitigated when the file names the pair and its ratio in its Accessibility or Colors section, and weight by severity (a 1.25:1 boundary is not the same finding as a 4.48:1 near-miss). |
| `theme-audit/audit.py` (the file itself) | The harness changed under the audit: `clean_value`, `parse_components`, `check_all` and the component-pair check all landed while this review was in progress, altering my own before-scores. Eighty-four reports written against a moving measuring stick are not comparable, which is the stated purpose of the SPEC. | Freeze `audit.py` for the duration of the review round and re-run all 84 at the end against one pinned version, recording its commit SHA in each report. I did not edit the harness; my brief forbids it. |
| `theme-audit/SPEC.md`, §3 section table | The section order is given but not required, and the briefs place `Motion & Animation` after `Components` while the table lists it there too — yet the harness only tests for presence. Files that put Accessibility before Components would score identically. | Either state that order is not checked, or add an order check. Minor. |
| `README.md` | Does not mention `focus`, `motion` or `shadow` as frontmatter groups, so a new contributor building a file from the README alone will reproduce exactly the gaps this audit exists to close. | Add `focus` to the colour-role list and `motion:` / `shadow:` to the frontmatter template, with the SPEC §4 default block. |

### Needs approval

1. **White on coral fails AA at the button label size.** `on-primary` #ffffff on `primary` #cc785c = **3.28:1**; `button-primary` labels are `typography.button` 14px/500, so 4.5:1 applies. Both hexes are extracted brand values and neither was changed. Nearest passing options: (a) label in `ink` #141413 on coral → **5.63:1**; (b) fill in `primary-active` #a9583e keeping white → **5.06:1**. Usage note that would make the real value defensible as it stands: white on coral clears AA Large, so it is compliant at **18.66px+ bold or 24px+ regular** — which is what `cta-band-coral` and `callout-card-coral` already do at `display-sm` 28px. The failure is specific to small labels. Brand owner decision.
2. **Coral as inline link ink fails AA.** `primary` on `canvas` = **3.11:1** at `body-md` 16px. The file now prescribes `primary-active` (**4.80:1**) for inline body links and keeps the extracted coral for 24px+ display links, with underlines mandatory either way. This changes documented brand behaviour for small links and needs approval; if rejected, the file should say that coral links are an accepted AA failure.
3. **`hairline-strong` #848075 is an invented hex.** Prescribed, not extracted. It is the only new colour value in the file. Needs brand approval or replacement with Anthropic's real control-boundary tone, if one exists.
4. **`focus` #141413 and `focus-on-dark` #faf9f5 are invented.** claude.com's real focus treatment is unmeasured. If the brand uses a coral ring, `focus-on-coral` becomes a third required token, since coral on coral is 1.0:1.
5. **Two documented rules were rewritten**: the Don't `Don't add hover state styling beyond what the system already encodes` and Iteration Guide item 4 `Never document hover. Default and Active/Pressed states only.` Both contradicted SPEC §7 outright. I kept their intent (motion and hover stay minimal) but they no longer forbid documenting hover. Flagging because they read as deliberate authorial decisions, not oversights.
6. **Renaming `accent-teal` / `accent-amber` was considered and rejected.** Scoping them to `status-teal` / `highlight-amber` would clear two harness failures legitimately — neither is an accent that carries text — but SPEC §2 explicitly warns about brands "hiding one failure entirely" behind naming, so I left the names and documented the required ink instead. If the maintainers prefer the rename, it is a two-line change plus four prose references.
7. **The two frozen hairlines still score as failures.** `hairline` (1.25:1) and `hairline-soft` (1.18:1) on canvas. SPEC §2 freezes them and prescribes exactly the remedy I applied — a parallel accessible token, originals scoped to decoration. The harness's new all-tones boundary check flags them anyway. Either the SPEC's remedy or the check needs to give; I followed the SPEC. No hex changed.
8. **The homepage typewriter effect.** Known Gaps records a code-block typewriter on the live site. I treated it as optional brand ambience that freezes under reduced motion. Under Crisp it arguably should not exist at all. Unresolved without measuring the live page.

### Identity verdict

Still unmistakably Claude. The additions are scoped to the three things that were missing — a focus ring, a motion system and an accessibility ledger — and each is argued from this brand's own material rather than from a generic template: the ring is warm ink #141413 because it matches the spike-mark and would be broken by a borrowed system blue; the boundary token #848075 is a warm grey that sits in the same family as `muted` and `muted-soft`, not a neutral slate; the layer-separation table exists because *this* palette's cream ladder is deliberately close in luminance, which is a fact about Claude and no other file in the collection. Nothing was borrowed from another site's DESIGN.md.

**On the assigned profile: Crisp is correct, but the assignment rule reaches it by the wrong route.** SPEC §5 rule 2 ("terminal, IDE, infra or developer-tool identity") fits — `code-window-card` is named in the file as "the signature visual element of Claude Code product pages", the dominant product chrome is a code editor and a terminal, and `product-mockup-card-dark` exists to show real code rather than illustrations of it. But read on the file's own self-description this is a textbook rule-4 **Calm** candidate: it calls itself "warm-canvas editorial", runs display type at weight 400, forbids bold serif, forbids a fourth surface tone, and reads "like a long-form magazine column".

I kept Crisp, for one reason that is in the file rather than in the rule: the Don'ts already say *"primary darkens on press; nothing else changes"*, and the Iteration Guide says *"Never document hover"*. That is a brand telling you, in its own words, that it does not want motion — which is Crisp's 150ms/no-choreography signature, not Calm's 250ms opacity-led fades. Calm would have been a defensible second choice and would change little in practice (base 150 → 250ms, stagger 20 → 40ms, and a small amount of enter travel this brand does not want). The editorial quality of Claude is carried by 96px section rhythm and serif type, both static. Motion's job here is to get out of the way, and Crisp is the profile that does that.

The one risk to identity is volume: the Component States table and the Accessibility section together add more rows than the rest of the Components section holds. That is a consequence of a 15-component system needing 8 state columns, and the cells are written in this file's own vocabulary (coral, cream, spike-mark, `surface-dark` family) rather than in generic token names — but a future editor should resist letting the tables grow further at the prose's expense.
