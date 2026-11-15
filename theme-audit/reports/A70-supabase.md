## A70 · supabase

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 1 | 2 | 1 | 1 |
| After | 5 | 5 | 5 | 5 | 5 | 5 |

Motion profile: **Crisp**, as rostered. Confirmed, not switched — see Identity verdict.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule, zero durations and zero easing curves anywhere in the file. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Seven contrast failures undisclosed, including five that mean no hairline in the brand reaches 3:1 on white. |
| P0 | A Token contract | `colors.focus` | No focus role at all, so the file documented no focus indicator for any of its four surfaces. |
| P0 | H States | all 16 components | Only `hover` and `pressed` documented anywhere. `focus-visible`, `active`, `disabled`, `loading`, `selected`, `error` named nowhere, so the file specified no keyboard affordance and no async or failure behaviour. |
| P1 | A / Sections | whole file | No `## Known Gaps`, so every prescribed-vs-extracted boundary was unmarked. |
| P1 | B Colour | `colors.hairline`, `hairline-strong`, `hairline-cool`, `hairline-cool-2`, `hairline-cool-3` | All five boundary tones fail 3:1 on `canvas` (1.15–1.69:1). Extracted and frozen, so not altered — but the file claimed a 1px `{colors.hairline}` border as `text-input`'s only boundary at 1.33:1, where the boundary is an affordance rather than decoration. |
| P1 | B Colour | `colors.ink-mute-2` `#9a9a9a` | 2.81:1 on `canvas` — below AA for body and below 3:1 even for large text, yet documented as "tertiary text" with no surface restriction. Passes on the dark track (6.06:1). |
| P1 | C Elevation | `## Elevation & Depth` | Four real `rgba()` shadow values with no `shadow:` group to reference, and no rule on whether hairline and shadow may coexist on one element — SPEC section 1 requires the group where the prose documents real shadow values. |
| P1 | A Token contract | `surface` role | The brand names no raised neutral: light cards are white-on-white separated by a hairline, and `canvas-soft` is a section band. No token invented; recorded in Known Gaps per SPEC section 1. |
| P2 | E Focus ring | `## Shapes` | No focus-ring geometry in the radius/stroke ladder; added with an explicit 2px offset so the ring is judged against the surface behind the control. |
| P2 | C Elevation | `canvas-night` / `canvas-night-soft` | The two dark tones separate by 1.05:1, so nested dark chrome is invisible without a border. Extracted; recorded, not changed. |
| P2 | I Identity | `## Components` | Several entries ended at a background and a radius, with no interaction surface described at all. |
| — | Harness | `audit.py` `surface` inference | `surface` resolves to `canvas-night`, manufacturing two failures the brand never draws. Reported under Shared issues, not fixed. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#707070"` | The one hex in this palette clearing 3:1 on all four surfaces it defines (4.95 / 4.74 / 3.44 / 3.29:1). Same hex the palette already owns as `ink-mute`, so it is a role binding, not an alias or a new brand colour. One mid-luminance ring instead of a light/dark pair, per SPEC section 1. |
| frontmatter | — -> `shadow:` group (`none`, `small`, `medium`, `large`) | SPEC section 1: the prose documented four real `rgba()` elevation values with no token to reference. Values copied verbatim from the existing Elevation table. |
| frontmatter | — -> `motion:` group | Crisp profile block from SPEC section 5, verbatim, no deviation. |
| `## Colors` | — -> `### Focus` subsection | States the ring is prescribed, which existing tone it reuses, its measured ratio on each surface, and why emerald is not the ring (2.00:1 on white). |
| `## Elevation & Depth` table | raw `box-shadow:` values -> `{shadow.*}` refs with the literal value retained beside each | Elevation expressed one way. Values unchanged. |
| `## Elevation & Depth` | — -> `### One Elevation Language` | Dimension C: hairline **or** shadow, never both on one element. |
| `## Shapes` | — -> `### Focus Ring Geometry` | 2px ring, 2px offset, drawn outside the control; radius follows the control's own, so no value sits outside the existing ladder. |
| `## Components`, all 16 entries | 2 states documented -> all 8 named per entry | Dimension H. Genuinely static entries (`pill-tag-green`, the composited mockups, `card-feature-dark`) say so explicitly rather than inventing states. |
| `## Components` → `text-input` | 1px `{colors.hairline}` as the only boundary -> extracted 1.33:1 stated plainly; 1px `{colors.ink-mute}` (4.95:1) prescribed for the boundary | SPEC section 2 step 1: the palette already owns a passing tone, so nothing was added. The frozen tone keeps its extracted role on card and table chrome (step 3); re-binding the rest is under Needs approval. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and was not measured. 12-row interaction table, Crisp values only, transform/opacity (plus paint-only colour) and a `prefers-reduced-motion` block. |
| after Motion | — -> `## Accessibility` | 14 measured pairs, the five hairline failures stated plainly, the two manufactured pairs labelled as manufactured, per-surface ring ratios, tap targets flagged as unverifiable, reduced motion. |
| `## Do's and Don'ts` | +2 Do, +4 Don't | Focus ring, elevation language, the layout-property prohibition, no mockup entrance choreography, and no light-track ink on the dark track. |
| `## Iteration Guide` | +1 step | Take motion values from `{motion.*}` rather than typing durations. |
| end of file | — -> `## Known Gaps` | 9 entries: motion prescribed, ring prescribed, no semantic colour family, no `surface` token, hairlines below 3:1, thin dark-track separation, Circular proprietary, tap targets documented not measured, mockup pointer behaviour unobserved. |

No hex was altered. No token was renamed. No extracted `components:` binding was re-pointed.

### Contrast checks

All computed with WCAG 2.1 relative luminance via a `python3` snippet, not estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#171717` on `canvas` `#ffffff` | 17.93:1 | 4.5 | Pass |
| `ink` on `canvas-soft` `#fafafa` | 17.18:1 | 4.5 | Pass |
| `ink-secondary` `#212121` on `canvas` | 16.10:1 | 4.5 | Pass |
| `ink-mute` `#707070` on `canvas` | 4.95:1 | 4.5 | Pass |
| `ink-mute` on `canvas-soft` | 4.74:1 | 4.5 | Pass |
| `ink-mute-2` `#9a9a9a` on `canvas` | 2.81:1 | 4.5 | **Fail** — disclosed, light-track use withdrawn in prose |
| `ink-mute-2` on `canvas-night` `#1c1c1c` | 6.06:1 | 4.5 | Pass |
| `ink-faint` `#b2b2b2` on `canvas` | 2.12:1 | — | Exempt (placeholder / disabled) |
| `on-dark` `#ffffff` on `canvas-night` | 17.04:1 | 4.5 | Pass |
| `on-dark` on `canvas-night-soft` `#202020` | 16.29:1 | 4.5 | Pass |
| `on-primary` `#171717` on `primary` `#3ecf8e` | 8.98:1 | 4.5 | Pass |
| `on-primary` on `primary-deep` `#24b47e` | 6.75:1 | 4.5 | Pass |
| `focus` `#707070` on `canvas` | 4.95:1 | 3.0 | Pass |
| `focus` on `canvas-soft` | 4.74:1 | 3.0 | Pass |
| `focus` on `canvas-night` | 3.44:1 | 3.0 | Pass |
| `focus` on `canvas-night-soft` | 3.29:1 | 3.0 | Pass |
| `hairline` `#dfdfdf` on `canvas` | 1.33:1 | 3.0 | **Fail** — extracted, frozen, disclosed |
| `hairline-strong` `#c7c7c7` on `canvas` | 1.69:1 | 3.0 | **Fail** — extracted, frozen, disclosed |
| `hairline-cool-3` `#d4d4d4` on `canvas` | 1.48:1 | 3.0 | **Fail** — extracted, frozen, disclosed |
| `hairline-cool` `#ededed` on `canvas` | 1.17:1 | 3.0 | **Fail** — extracted, frozen, disclosed |
| `hairline-cool-2` `#efefef` on `canvas` | 1.15:1 | 3.0 | **Fail** — extracted, frozen, disclosed |
| `ink` on `canvas-night` | 1.05:1 | 4.5 | **Fail, manufactured** — the file never draws this pair |
| `ink-secondary` on `canvas-night` | 1.06:1 | 4.5 | **Fail, manufactured** — same |
| `canvas` / `canvas-soft` (layer separation) | 1.04:1 | — | Layering rests on hairlines and `{shadow.*}`, not tone |
| `canvas-night` / `canvas-night-soft` | 1.05:1 | — | Nested dark chrome needs a border; extracted |
| `primary` `#3ecf8e` on `canvas` (why it is not the ring) | 2.00:1 | 3.0 | Fail — emerald rejected as focus colour |
| `focus` on `primary` (control fill, not a ground) | 2.48:1 | — | Not required: the ring is offset outside the control |

Every hairline tone in the brand is below 3:1 on white. That is the brand's own failure and is now stated in the file rather than fixed in place.

### Motion inventory

Prescribed, Crisp profile, not measured from the live site.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `background-color`, `color`, `opacity` | Unchanged — paint-only, no travel |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `background-color`; no scale | Unchanged |
| Focus-visible ring | `{motion.duration-instant}` 60ms | `{motion.ease-enter}` | `opacity` | Instant, never suppressed |
| Page / route transition | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity` | Fade at `{motion.duration-reduced}` 100ms |
| Modal / drawer enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` + `translateY(8px)` | Travel removed, fade 100ms |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity` | Fade 100ms |
| Dropdown enter | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | `opacity` + `translateY(4px)` | Travel removed, fade 100ms |
| Dropdown exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` | Fade 60ms |
| Toast | in 150ms / out 100ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | Travel removed, fade 100ms |
| List enter | 100ms, `{motion.stagger-step}` 20ms apart, capped at 6 | `{motion.ease-enter}` | `opacity` + `translateY(4px)` | Stagger and travel removed, fade together 100ms |
| List exit | `{motion.duration-instant}` 60ms, no stagger | `{motion.ease-exit}` | `opacity` | Fade 60ms |
| Loading | 800ms loop | `linear` | `transform: rotate()`, `opacity` 0.4↔1 | Loop frozen; static indicator plus text status |

Every exit is shorter than its entrance. The 800ms loader is the only infinite animation; there is no brand ambience, which follows from the file's own white-canvas commitment. `duration-slow` 220ms and `duration-emphasis` 300ms are carried in the token block for profile comparability but are unused by this file's interactions — a Crisp developer-tool identity has nothing that should take 300ms.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 234–261 | `surface` role inference resolves to `canvas-night` for this file, then measures the light-track inks against it: `ink on canvas-night` 1.05:1 and `ink-secondary on canvas-night` 1.06:1. Both are manufactured. The light cards (`card-feature-light`, `card-pricing`) are skipped by the `colors[m.group(1)] == canvas_hex` guard on line 251 because this brand's cards are white on white, separated by a hairline; the only remaining container fill is the deliberately inverted dark tier, so the role lands on the opposite polarity. Every component bound to `canvas-night` sets `textColor: {colors.on-dark}` at 17.04:1, so the pair the harness measures cannot render. | Require the inferred surface to share the canvas polarity — reject a candidate whose luminance sits on the other side of the 0.2 threshold from the canvas. Then prefer `canvas-soft` `#fafafa`, the file's nearest raised neutral, or, where every container fill equals the canvas hex, fall back to the canvas itself and report `surface=canvas` so the contrast checks measure a pair the file actually draws. The present behaviour is the "satisfies a role wrongly" case SPEC section 1 names: it hides the real card ground and measures against one the site never renders. |
| `theme-audit/audit.py` line 632 | `durations_found` picks up `001` from the `animation-duration: 0.001ms` in the reduced-motion block, which is a correct way to write that rule. Cosmetic — it only affects the reported list, not any score. | Match `\b(\d{2,4})ms\b` only where not preceded by `.`, or drop values below 10ms from the list. |
| `theme-audit/audit.py` lines 29–33 | `text-dim` patterns match `^ink-(muted|...)` but not `ink-mute`, so this file's `ink-mute` `#707070` and `ink-mute-2` `#9a9a9a` are never measured as secondary text. `ink-mute-2` at 2.81:1 on white is a real AA failure the harness does not see; it is disclosed in the file regardless. | Add `mute` beside `muted` in the alternation: `^ink-(muted?|subtle|soft|…)`. |

### Needs approval

1. **Re-binding the card, table and divider hairlines.** `{colors.hairline}` `#dfdfdf` 1.33:1, `hairline-cool` `#ededed` 1.17:1, `hairline-cool-2` `#efefef` 1.15:1, `hairline-cool-3` `#d4d4d4` 1.48:1 and `hairline-strong` `#c7c7c7` 1.69:1 are all below 3:1 on `canvas` `#ffffff`. Nearest passing value in the palette: `{colors.ink-mute}` `#707070` at 4.95:1. Nearest passing value outside it: `#949494` at 3.03:1, which would keep the hairlines reading as chrome rather than as rules. Usage note that makes the extracted values defensible: these tones are purely decorative separation — table rules, card edges, section bands — and WCAG 1.4.11 sets no contrast floor on decoration. Only `text-input`'s boundary is an affordance, and that one has been re-scoped in prose to `{colors.ink-mute}`. A brand owner decides whether the rest follow; no `components:` binding was changed here.
2. **`{colors.ink-mute-2}` `#9a9a9a` on the light track.** 2.81:1 on `canvas`, so it fails AA at every text size — it does not even reach the 3:1 that applies to 18px+ / 14px-bold large text. Nearest passing value for body: `#767676` at 4.54:1. Nearest for large text only: `#949494` at 3.03:1, with the usage note "18px+ or 14px bold only". The file now withdraws it from light-track text and keeps it for the dark track, where it measures 6.06:1 — confirm that withdrawal is acceptable, since it changes which grey a tertiary caption uses on white.
3. **Focus ring colour.** `{colors.focus}` `#707070` is prescribed and is grey, not emerald. The alternative — emerald `{colors.primary}` — measures 2.00:1 on white and cannot be used. If the brand would rather carry a chromatic ring on the light track only, the palette's `accent-violet` `#644fc1` reaches 6.12:1 on `canvas` but only 2.78:1 on `canvas-night`, so it would force a second polarity-named ring and break the single-ring simplicity. Confirm the grey.
4. **Prescribed error tone.** `text-input` and `code-block` error states fall back to `{colors.accent-tomato}` `#ff2201` (3.83:1 on `canvas`), an integration-logo accent promoted to a semantic role because this palette holds no error tone. The brand should supply a proper semantic ramp; the prescribed stand-in is labelled as such in both the Components entries and Known Gaps.
5. **Prescribed `nav-bar-light` selected underline.** A 2px `{colors.primary}` underline on the current route is the one new non-CTA use of emerald in the file. Emerald's extracted non-CTA uses are the wordmark accent and the dot indicator, so this is an extension of the brand's scarcity rule, not an observation of it.

### Identity verdict

The file still reads as this brand, and the edits mostly sharpened that rather than diluting it. Two tests: nothing was added that would suit a different file, and every addition was argued from something the file already said. The ring is grey because the brand's first rule is that emerald is the only chromatic event and emerald cannot carry a ring on white; the press state has no scale because the file's own Don't forbids pill shapes and prizes square-ish 6px technical buttons; the mockups get no entrance choreography because the file says the product screenshot is the brand's argument; `pill-tag-soft`'s selected state inverts to `canvas-night` rather than filling with green, which is exactly how the featured pricing tier distinguishes itself in the extracted content. The one risk of drift is the Accessibility table, which is arithmetic and would look similar in any file — but its conclusions are specific: no hairline in this brand reaches 3:1, and `on-primary` on `primary` at 8.98:1 is the near-black-on-emerald idiosyncrasy that the file already identified as deliberate.

**Crisp is the right profile and was not switched.** SPEC section 5 rule 2 fires directly: an open-source database platform whose dominant decorative element is a dashboard, SQL editor and log stream is an infra / developer-tool identity. The counter-arguments both fail. Cinematic (rule 1) needs full-bleed photography and a slow reveal; this file explicitly has "no full-bleed photography" and "minimal photography". Playful (rule 3) needs saturated colour on interactive elements and an informal type voice; the palette is near-monochrome, the display weight is 500 with negative tracking described as "engineered, not decorative", and the eight chromatic accents are confined to chart points and integration logos — the file's own Don't forbids them as system colours. A single emerald CTA is not a saturated identity.
