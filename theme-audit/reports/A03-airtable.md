# A03 · airtable

Scores before → after (1-5), from the harness:

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 4 | 5 | 4 | 3 | 1 | 2 |
| after | **5** | **5** | **4** | **5** | **5** | **5** |

Contrast stays at 4 deliberately. The one failure is `hairline` #dddddd on `canvas` #ffffff at 1.36:1 against a 3.0:1 minimum. It is Airtable's real border tone, so per SPEC §2 it is not changed; it is recorded under Needs approval and stated plainly in the file.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F | whole file | No motion information of any kind: no `motion:` token group, no `## Motion & Animation` section, no reduced-motion rule. Harness motion score 1. |
| P0 | G | whole file | No `## Accessibility` section. No contrast figure appeared anywhere in the file; every colour claim was qualitative. |
| P0 | A | `colors` | No `focus` role. The file described "an outer 2px blue ring" in Elevation and `info-border` on focused inputs, but the ring had no token and no hex, so focus visibility could not be checked on any surface. |
| P1 | B/G | `colors.hairline` | #dddddd is 1.36:1 on white. It is the sole boundary of `button-secondary` and `text-input`, so those controls fail WCAG 1.4.11. The file previously made no mention of this. |
| P1 | H | `components` (all 27 entries) | The "no-hover policy" blockquote was being used to avoid documenting *state coverage*, not just hover colours. `focus-visible`, `loading` and `selected` appeared nowhere in the file, although the file itself describes a focused input, a selected pricing tier and an active filter-rail item. |
| P1 | G | `button-icon-circular` | 40 × 40px, below the 44 × 44 minimum. The file acknowledged this but dismissed it ("the centered icon and dot-radius compensate visually"), which is not a thing contrast or hit-testing does. |
| P1 | I | profile assignment | Roster assigned **Playful**. The file's own evidence says Calm. Switched — see Identity verdict. |
| P2 | B | `colors.on-primary` on `colors.signature-mustard` | 2.25:1. The demo-grid surfaces are documented as a group with white type implied by the coral/forest precedent; mustard cannot carry white type. Now stated. |
| P2 | B | `colors.success-border`, `colors.border-strong` | 2.41:1 and 2.93:1 on canvas. Both below 3:1, both acceptable in their actual use (accent stroke beside a label; disabled control). Recorded, not changed. |
| P2 | E | `components.footer` | `padding: 64px` was a literal sitting outside the spacing ladder (which jumps 48 → 96). Fixed by naming it. |
| P2 | E | `rounded.pill` / `rounded.full` | Both 9999px. Two names for one value — defensible as intent signalling, but a CSS generator will emit a duplicate. Now flagged in Known Gaps. |
| P2 | D | `typography.body-md` | 14px / 1.25 is 17.5px of leading for the default running-text role. Tight for the long editorial paragraphs this system is built around. Noted in Accessibility, value unchanged (it is extracted). |
| P2 | G | `colors.link` | No underline by default; link blue to body ink is 2.02:1, so colour alone does not distinguish a link. Underline on hover/focus is load-bearing. Now stated. |
| P2 | A | `colors.ink` vs `colors.primary` | Same hex (#181d26) under two names, as is `surface-dark`. The file already explains this as one role at three layers — kept, it is genuinely informative here. |

### Changes made

| Location in file | Before → After | Why |
|---|---|---|
| frontmatter `colors` | — → `focus: "#1b61c9"`, `focus-on-dark: "#ffffff"` | SPEC §1 requires a `focus` role. Reuses the documented Airtable link blue rather than inventing a hue; 5.83:1 on canvas. White covers the signature surfaces where blue measures 1.17:1 on coral. |
| frontmatter `spacing` | — → `xxxl: 64px` | Names a value already present as a literal, so the ladder has no gap at 64px. |
| frontmatter | — → `motion:` group, 9 keys, Calm values | SPEC §4/§5. Base 250ms, symmetric `cubic-bezier(0.4, 0, 0.2, 1)`, 40ms stagger. |
| `components.footer` | `padding: 64px` → `padding: "{spacing.xxxl}"` | Removes the off-ladder literal. |
| Colors → Surface, Hairline bullet | added the measured 1.36:1 and why the hex is not being changed | SPEC §2: a real brand failure is useful information, not something to hide. |
| Colors → Semantic | added **Focus** and **Focus On Dark** bullets with per-surface ratios | Documents the new tokens where a reader looks for them. |
| Elevation & Depth, "Button focus" row | "Outer 2px blue ring at higher alpha" → `{colors.focus}` ring with a 2px canvas offset, `{colors.focus-on-dark}` on signature surfaces | The ring was described but untokenised. |
| Components, opening blockquote | "No hover states documented. Per the global no-hover policy…" → hover *styling* is not extracted, state *coverage* is | The old wording justified a gap SPEC §7 does not permit. |
| Components | — → `### State Matrix`, 8-column table covering every component entry | SPEC §7. Components with genuinely one state are listed as such rather than omitted. |
| after Components | — → `## Motion & Animation` | SPEC §3/§6. First line states the system is prescribed and unmeasured. Interaction table covers all ten required interactions; motion rules; `@media (prefers-reduced-motion: reduce)` block with what is removed and what remains. |
| after Motion | — → `## Accessibility` | SPEC §3. 26 measured pairs, per-surface focus ring table, tap targets, reduced motion, type/link notes. |
| Don'ts | replaced the "don't add hover styling" bullet with one on hover colour vs hover timing; added a "no press scale-pop" bullet | The old bullet now contradicts the Motion section; the new one keeps the no-hover-hex rule while allowing prescribed timing. The scale-pop bullet records the Playful→Calm decision where a reader will act on it. |
| Iteration Guide item 5 | "Never document hover." → document the state set, keep hover colours unextracted | Same reconciliation. |
| Responsive → Touch Targets | icon button "compensates visually" → "a real failure, see Accessibility" | The original claim was not true and not checkable from a document. |
| Known Gaps | replaced "Animation and transition timings are not in scope" with the prescribed-motion caveat; added entries for the focus tokens, `{spacing.xxxl}`, the pill/full duplicate, and hover colour values | Every value added in this pass that is not extracted is labelled here. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`, not estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #181d26 / `canvas` #ffffff | 16.90 | 4.5 | pass |
| `ink` / `surface-soft` #f8fafc | 16.15 | 4.5 | pass |
| `ink` / `surface-strong` #e0e2e6 | 13.03 | 4.5 | pass |
| `body` #333840 / `canvas` | 11.79 | 4.5 | pass |
| `muted` #41454d / `canvas` | 9.62 | 4.5 | pass |
| `on-primary` #ffffff / `primary` #181d26 | 16.90 | 4.5 | pass |
| `on-primary` / `primary-active` #0d1218 | 18.80 | 4.5 | pass |
| `on-primary` / `signature-coral` #aa2d00 | 6.81 | 4.5 | pass |
| `on-primary` / `signature-forest` #0a2e0e | 14.89 | 4.5 | pass |
| `on-dark` / `surface-dark-elevated` #1d1f25 | 16.47 | 4.5 | pass |
| `ink` / `signature-cream` #f5e9d4 | 14.07 | 4.5 | pass |
| `ink` / `signature-peach` #fcab79 | 9.05 | 4.5 | pass |
| `ink` / `signature-mint` #a8d8c4 | 10.69 | 4.5 | pass |
| `ink` / `signature-yellow` #f4d35e | 11.53 | 4.5 | pass |
| `ink` / `signature-mustard` #d9a441 | 7.51 | 4.5 | pass |
| `link` #1b61c9 / `canvas` | 5.83 | 4.5 | pass |
| `link-active` #1a3866 / `canvas` | 11.66 | 4.5 | pass |
| `info` #254fad / `canvas` | 7.50 | 4.5 | pass |
| `success` #006400 / `canvas` | 7.44 | 4.5 | pass |
| `pricing-ink` #1d1f25 / `canvas` | 16.47 | 4.5 | pass |
| `focus` #1b61c9 / `canvas` | 5.83 | 3.0 | pass |
| `focus` / `surface-soft` | 5.58 | 3.0 | pass |
| `focus` / `surface-strong` | 4.50 | 3.0 | pass |
| `focus` / `signature-cream` | 4.86 | 3.0 | pass |
| `focus` / `signature-peach` | 3.12 | 3.0 | pass |
| `focus` / `signature-mint` | 3.69 | 3.0 | pass |
| `focus` / `signature-yellow` | 3.98 | 3.0 | pass |
| `focus` / `signature-mustard` | 2.59 | 3.0 | **fail** — ring switches to `ink` (7.51) |
| `focus` / `signature-coral` | 1.17 | 3.0 | **fail** — ring switches to `focus-on-dark` |
| `focus-on-dark` #ffffff / `surface-dark` | 16.90 | 3.0 | pass |
| `focus-on-dark` / `signature-forest` | 14.89 | 3.0 | pass |
| `focus-on-dark` / `signature-coral` | 6.81 | 3.0 | pass |
| `hairline` #dddddd / `canvas` | **1.36** | 3.0 | **fail** |
| `border-strong` #9297a0 / `canvas` | **2.93** | 3.0 | **fail (narrow)** |
| `info-border` #458fff / `canvas` | 3.17 | 3.0 | pass |
| `success-border` #39bf45 / `canvas` | **2.41** | 3.0 | **fail** |
| `on-primary` #ffffff / `signature-mustard` | **2.25** | 4.5 | **fail** |
| `link` / `body` (link distinguishability) | 2.02 | 3.0 | **fail** — underline required |

Elevation layers: `canvas`→`surface-soft` 1.05, `surface-soft`→`surface-strong` 1.24, `canvas`→`surface-strong` 1.30. All three light layers are near-indistinguishable by luminance alone, which is correct for this brand — the file's stated elevation philosophy is "color-block first, shadow second" and real separation comes from the signature cards (`canvas`→`surface-dark` 16.90, →`signature-coral` 6.81, →`signature-forest` 14.89), not from the grey ladder. Worth knowing that `surface-soft` as a "raised" layer carries no visible edge on its own; the `pricing-tier-card-featured` tone shift is a very quiet signal.

### Motion inventory

Profile: **Calm**. Every value prescribed, none measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `duration-fast` 150ms | `ease-standard` | opacity | unchanged |
| Press | `duration-instant` 80ms | `ease-standard` | opacity, no scale | unchanged |
| Focus ring | `duration-instant` 80ms | `ease-standard` | opacity | no transition at all |
| Page / route | 250ms in, 150ms out | `ease-enter` / `ease-exit` | opacity + translateY 8px | cross-fade, travel removed |
| Modal / drawer | 250ms in, 150ms out | `ease-enter` / `ease-exit` | opacity + translateY 16px (sheet: translateX 100%) | cross-fade, travel removed |
| Dropdown | 150ms in, 80ms out | `ease-enter` / `ease-exit` | opacity + translateY 4px | fade, travel removed |
| Toast | 250ms in, 150ms out | `ease-enter` / `ease-exit` | opacity + translateY 8px | fade, travel removed |
| List enter | 250ms per item, 40ms stagger | `ease-enter` | opacity + translateY 8px | group fades once at 150ms, stagger removed |
| List exit | 150ms, no stagger | `ease-exit` | opacity + translateY −4px | fade, travel removed |
| Loading | 600ms/rotation, infinite while pending | linear (spinner) / `ease-standard` (skeleton) | transform rotate, opacity | both stop; static labelled indicator |
| Signature card enter | `duration-slow` 400ms, no stagger | `ease-enter` | opacity only | unchanged (already opacity-only) at 150ms |

Only `transform` and `opacity`; every exit shorter than its entrance; loaders are the only infinite animation and there is no brand ambience loop.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 29 | `border` role patterns put `^hairline$` first, so a file that defines both `hairline` (decorative) and `border-strong` (control boundary) is always scored on the decorative one. Airtable's `border-strong` is 2.93:1 — still a fail, but the check is measuring the wrong token's job. | Either check *all* border-ish keys and report the best, or split the role into `divider` (no minimum) and `border` (3:1), since WCAG 1.4.11 applies to control boundaries, not to decorative rules. |
| `theme-audit/audit.py` line 154 | `states_missing` is a substring search over the whole file, so a file scores 5/5 on states by mentioning the word "loading" once anywhere — including in a Known Gaps line saying loading is *not* documented. The metric is not measuring state coverage. | Scope the search to the `## Components` section, or count components whose entry names ≥1 state. |
| `theme-audit/audit.py` line 138 | `focus` contrast is only checked against `canvas`. A single blue focus ring passes on white and is invisible on this file's coral and dark signature cards (1.17:1). | Also check `focus` against every `surface*` and signature key present, or require a `focus-on-dark` companion wherever a surface is darker than 50% luminance. |
| `theme-audit/audit.py` line 150 | The layout-animation regex only fires when a forbidden property is within 60 non-period characters *after* "animat". `transition: width 200ms` with no nearby "animat" is invisible to it. | Add a second pattern over `transition(-property)?:` declarations. |
| `theme-audit/SPEC.md` §3 | `Iteration Guide` is listed "optional" but `audit.py` includes it in `SECTIONS`, so its absence costs a sections point. | Either drop it from `SECTIONS` or mark it required in the spec. |
| `theme-audit/SPEC.md` §5 | Rule 3 ("saturated multi-colour … consumer identity → Playful") reads off the *count* of named colours, not their saturation or their role. Airtable has eight signature colours, most of them dark and desaturated, used as static card backgrounds — and the rule still lands on Playful. | Qualify rule 3: saturated multi-colour used on *interactive* elements, and exclude palettes whose brand colours are below ~40% saturation or sit above 50% in luminance distance from the canvas. |

### Needs approval

1. **`colors.hairline` #dddddd — 1.36:1 on white, needs 3.0:1.** Not changed. Nearest passing value is **#949494 (3.03:1)**; a comfortable one is **#888888 (3.54:1)**. Usage note that would make the real value defensible: *#dddddd is a decorative divider tone for table rules and section separators, where no control boundary is being communicated.* That note holds for `pricing-comparison-row` dividers and sub-nav rails. It does **not** hold for `button-secondary` or `text-input`, where the hairline is the only edge the control has — so a split is the honest fix: keep #dddddd as `divider`, introduce a ≥3:1 tone for control boundaries. Airtable's real site fails AA for non-text contrast on those two controls and I have said so in the file rather than papering over it.
2. **`colors.border-strong` #9297a0 — 2.93:1, needs 3.0:1.** Not changed, 0.07 short. Nearest passing is **#8f949d (3.05:1)**, visually identical. Usage note that makes the real value defensible: *it appears only on disabled controls, and WCAG 1.4.11 exempts inactive components.* I think that note is sufficient and no change is needed, but it is a judgement call.
3. **`colors.success-border` #39bf45 — 2.41:1.** Not changed. Nearest passing is **#2a8f33 (4.14:1)** but that loses the bright-green read entirely. Usage note: *a 1px accent stroke on a badge that always carries a text label in `colors.success` (7.44:1), never the sole carrier of state.*
4. **White type on `colors.signature-mustard` — 2.25:1.** Not a change request; the file now says ink-on-mustard (7.51:1) only. Flagging because the demo-grid surfaces are documented as one group and the coral/forest precedent implies white type, so the group needs the exception spelled out — which it now does.
5. **`components.button-icon-circular` 40 × 40px.** Left at the extracted value. The fix is a 44px invisible hit area, which changes no visual token; the file recommends it. Approve if you want the declared `size` raised to 44px instead, but that would be changing an extracted value.
6. **Profile switch Playful → Calm.** Roster rule change needed, see below.

### Identity verdict

**Switched: Playful → Calm.** The roster should be corrected.

Evidence from the file, not from outside it:

- Its own `description` field reads "A sober, editorial workflow-software interface". Playful is not a sober profile.
- The canvas is `#ffffff` and the Overview forbids any atmosphere on it: "no gradient, no mesh, no background flourish", "Trust whitespace as the hero atmosphere", "whitespace as the dominant atmospheric tool". Playful's signature is springy reveals; this hero is explicitly specified to do nothing.
- Type voice: display weight **400**, with an explicit Don't against bolding it. The only 600 in the system is the cookie banner. Playful type is not weight-400 Haas Grotesk at 40px.
- The colours that trip the roster's rule 3 are not saturated in use. `signature-coral` #aa2d00 is an oxide red at 6.81:1 against white type; `signature-forest` #0a2e0e is a near-black green at 14.89:1. Those are dark editorial blocks, not candy. The genuinely bright values (peach, mint, yellow, mustard) are **static card backgrounds behind product screenshots** — the file says each demo card "frames a product UI fragment". No interactive element in the system uses a saturated colour; the primary CTA is near-black.
- Elevation is "color-block first, shadow second", with "no soft-glow / atmospheric-shadow / heavy-elevation language anywhere". Playful overshoot needs somewhere to overshoot into.
- The system's pacing device is already specified and it is spatial, not temporal: `spacing.section` 96px between every band. A brand that paces with whitespace does not also pace with bouncy entrances.

So rule 3 misfired on colour *count*. Rule 4 (everything else → Calm) is the right landing. Calm's "short opacity-led fades, little travel" is exactly what a long-scroll print-magazine layout wants, and it is the only profile that lets the signature cards arrive as whole blocks rather than as choreographed contents.

**Does it still read as Airtable?** Yes, and more specifically than before. The additions are written against this file's own vocabulary: the Motion section argues from the coral/forest/dark card rhythm and the 96px band constant, the focus ring reuses the documented link blue instead of a generic ring colour, the per-surface ring table exists *because* this brand has eight signature surfaces, and the State Matrix names the selected pricing tier and the filter-rail count badge that only this file has. The one thing that would read as borrowed is the reduced-motion CSS block, which is close to boilerplate — but SPEC §6 asks every file to state the same thing, so the convergence is the spec's, not drift. The pricing sub-system (Inter Display 475, pill radius) is untouched and still the file's sharpest identity signal.
