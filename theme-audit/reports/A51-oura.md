## A51 · oura

Scores before -> after (1-5), from the harness:

| Dimension | Before | After |
|---|---|---|
| tokens | 3 | 4 |
| refs | 5 | 5 |
| contrast | 2 | 5 |
| sections | 1 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

`tokens` stops at 4 on purpose: the one role the harness still reports missing is `text-dim`, and this file already owns that role under two other names. Per SPEC section 1 that is a harness bug to report, not a token to invent — see Shared issues.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Zero durations, zero easings. The main gap. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Six real contrast failures were undisclosed, including the brand's own hairline at 1.22:1. |
| P0 | A Token contract | `colors.focus` | No focus ring token at all, and the file documents three surface polarities (cream/white, cool silver, ink/stone), so one ring cannot cover them. |
| P0 | B Colour | `colors.hairline` #e1dcd3 | 1.22:1 on `canvas`, 1.37:1 on `surface`, against 3.0:1. It is bound as `borderColor` on `feature-card`, `button-icon-circular`, `ex-cart-drawer` dividers and `ex-data-table-cell` row rules — i.e. it was the only boundary of interactive controls. |
| P0 | C/H States | every component | `hover`, `focus-visible`, `pressed`, `disabled`, `loading` named nowhere in the file. The Components blockquote waived them rather than declaring them. |
| P1 | Sections | `### Responsive Strategy` | Carried as a Layout subsection, not the required top-level `## Responsive Behavior`. |
| P1 | Sections | `## Known Gaps` | Absent, while the file contains several genuinely unextracted things (shadow values, dark theme, section rhythm). |
| P1 | B Colour | `colors.ash` #838280 | 3.42:1 on cream, 3.84:1 on white, against 4.5:1. Documented as "muted grey for meta text" and bound to `person-card` role text at `{typography.caption}` 13px, where the 18px+ defence does not apply. Real AA failure. |
| P1 | B Colour | `colors.mute` #a8a5a0 | 2.19:1 on cream. Fails at every size on the light worlds. Passes only where the file actually uses it most, the dark footer (7.15:1). |
| P1 | B Colour | `colors.error` #e33a22 | 3.82:1 on cream against 4.5:1 for text. Defensible as the extracted focused-field *border* (3:1), not as message text. |
| P1 | B Colour | `colors.silver` #cccac7 | 1.46:1 on cream. It is the extracted *selected*-state border of `pill-tab`, so the selected tab is not perceivable; the harness misses this because `silver` matches no `border` pattern. |
| P1 | E Focus ring | — | Nothing stated the ring's width, offset, or which surface it is measured against. |
| P2 | C Elevation | Elevation & Depth | Four levels described qualitatively ("very soft, low-opacity drop shadow") with no `rgba(...)` value and no `shadow:` group. Expressed one consistent way (shadow for levels 1-3, colour-world shift or hairline for level 0), so not mixed at random — but unquantified. |
| P2 | D Typography | `typography.lead` | Weight 100 at 24px is the lightest reading-size text in the file; every role does carry size, weight and line height, and body on `canvas`/`surface` measures 15.32:1 / 17.20:1, so readability itself is fine. |
| P2 | E Ladders | `rounded`, `spacing` | Both ladders are internally consistent; no value sits outside its scale. `spacing` stops at 32px while the prose describes section-scale "silences" with no token for them. |
| P2 | A Refs | — | Zero dangling `{group.token}` references before and after. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-strong: "#8a8171"` | Parallel accessible boundary (3.43:1 cream / 3.85:1 white) for controls whose only edge is a 1px rule. The extracted `hairline` is unchanged and still documented. |
| frontmatter `colors:` | — -> `error-strong: "#bf2a14"` | 5.26:1 on cream, so validation *text* has a passing tone; the extracted `error` keeps its real border job. |
| frontmatter `colors:` | — -> `focus: "#1f5ab4"`, `focus-on-dark: "#f7f1e8"` | Two rings, as SPEC section 1 requires of a file with both light and dark signature surfaces. Deepened action blue for the cream/white/silver worlds; brand paper cream for the stone and ink worlds. |
| frontmatter | — -> `motion:` group | The Cinematic block from SPEC section 5, verbatim, no deviation. |
| `## Colors` → Surface | `hairline` entry -> same entry + measured 1.22:1 / 1.37:1 and "decoration only" scope, plus a new `hairline-strong` entry | SPEC section 2: scope the frozen tone to decoration, label the parallel token prescribed. |
| `## Colors` → Semantic | `error` entry -> same + border-vs-text ratios, plus `error-strong` | Same reason. |
| `## Colors` | — -> new `### Focus` subsection | States both rings, their measured ratios per surface, the 2px/2px offset, and why the ring is deliberately not `{colors.primary}`. |
| `## Components` | blockquote waiving states -> blockquote + `### Interaction States` table | Every component entry now names its states and marks each one extracted or prescribed. `stat-badge`/`eyebrow-label`/`hero`/`announcement-bar` are declared one-state; plain cards are declared genuinely two-state. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the visual identity and was not measured from the live site. 12-row table of interaction × duration × easing × property × reduced-motion, plus rules and the `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | — -> `## Accessibility` | Measured contrast table, an explicit "where the real brand fails AA" list with every ratio, per-surface focus-ring coverage, tap-target requirement labelled prescribed, reduced-motion statement. |
| `### Responsive Strategy` (inside Layout) | moved verbatim -> `## Responsive Behavior` after Do's and Don'ts, `####` children promoted to `###` | SPEC section 3: move, never duplicate. Content is byte-identical apart from heading depth. |
| end of file | — -> `## Known Gaps` | Nine items: prescribed motion, no shadow values, prescribed states, prescribed rings, prescribed strong tones, no dark theme, the `text-dim` naming gap, untokenised section rhythm, and what a document cannot measure. |
| `### Don't` | 6 bullets -> 10 | Four motion/a11y prohibitions: no layout-property animation, no content-delaying entrance, no bare `hairline` as a control boundary, never suppress the ring. |

Nothing else was reflowed. No extracted hex was altered.

### Contrast checks

All computed with the WCAG 2.1 relative-luminance formula, python3 stdlib only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #1c1b1a / canvas #f7f1e8 | 15.32:1 | 4.5:1 | Pass |
| ink / surface #ffffff | 17.20:1 | 4.5:1 | Pass |
| ink / surface-grey #ececec | 14.56:1 | 4.5:1 | Pass |
| stone #4a4741 / canvas | 8.24:1 | 4.5:1 | Pass |
| stone / surface | 9.26:1 | 4.5:1 | Pass |
| on-primary #ffffff / primary #2a72de | 4.61:1 | 4.5:1 | Pass |
| on-stone #ffffff / stone | 9.26:1 | 4.5:1 | Pass |
| on-dark #ffffff / ink-band-soft #19191c | 17.54:1 | 4.5:1 | Pass |
| canvas / ink-band #000000 (cream card on black) | 18.70:1 | 4.5:1 | Pass |
| mute #a8a5a0 / ink-band-soft (footer secondary) | 7.15:1 | 4.5:1 | Pass |
| **ash #838280 / canvas** | **3.42:1** | 4.5:1 | **Fail** (disclosed) |
| **ash / surface** | **3.84:1** | 4.5:1 | **Fail** (disclosed) |
| **mute / canvas** | **2.19:1** | 4.5:1 | **Fail** (disclosed) |
| **hairline #e1dcd3 / canvas** | **1.22:1** | 3.0:1 | **Fail** (disclosed) |
| **hairline / surface** | **1.37:1** | 3.0:1 | **Fail** (disclosed) |
| **error #e33a22 / canvas, as text** | **3.82:1** | 4.5:1 | **Fail** (disclosed) |
| error / canvas, as border | 3.82:1 | 3.0:1 | Pass |
| **silver #cccac7 / canvas** (pill-tab selected border) | **1.46:1** | 3.0:1 | **Fail** (disclosed) |
| hairline-strong #8a8171 / canvas | 3.43:1 | 3.0:1 | Pass |
| hairline-strong / surface | 3.85:1 | 3.0:1 | Pass |
| hairline-strong / surface-grey | 3.26:1 | 3.0:1 | Pass |
| error-strong #bf2a14 / canvas | 5.26:1 | 4.5:1 | Pass |
| error-strong / surface | 5.90:1 | 4.5:1 | Pass |
| focus #1f5ab4 / canvas | 5.88:1 | 3.0:1 | Pass |
| focus / surface | 6.60:1 | 3.0:1 | Pass |
| focus / surface-grey | 5.59:1 | 3.0:1 | Pass |
| focus / silver #cccac7 | 4.04:1 | 3.0:1 | Pass |
| focus-on-dark #f7f1e8 / stone | 8.24:1 | 3.0:1 | Pass |
| focus-on-dark / ink #1c1b1a | 15.32:1 | 3.0:1 | Pass |
| focus-on-dark / ink-band-soft | 15.62:1 | 3.0:1 | Pass |
| focus-on-dark / ink-band | 18.70:1 | 3.0:1 | Pass |

Elevation layers, for dimension C: canvas/surface 1.12:1, surface-grey/canvas 1.05:1, silver/surface 1.64:1. The three light layers are **not** distinguishable by luminance alone — this file's elevation is carried by radius, shadow and the surface-world shift, not by a step in tone, which is consistent with the Overview's own description and is now stated in Accessibility and Known Gaps.

### Motion inventory

Prescribed Cinematic profile. No value was extracted from the live site.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, card, nav link) | 240ms `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`, `transform: translateY(-2px)` | travel removed; opacity only at 150ms |
| Press / active | 120ms `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | scale removed; instant state change |
| Focus-visible ring | 120ms | `{motion.ease-standard}` | ring `opacity` | no transition; ring never suppressed |
| Page / route transition | 600ms `{motion.duration-slow}` | `{motion.ease-enter}` | `opacity`, `translateY(16px)` | travel removed; cross-fade at 150ms |
| Modal / drawer enter | 400ms `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `translateY(24px)` / `translateX` | travel removed; opacity at 150ms |
| Modal / drawer exit | 240ms | `{motion.ease-exit}` | `opacity`, `translateY(12px)` | travel removed; opacity at 150ms |
| Dropdown | 240ms enter / 120ms exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(-4px)` | travel removed; opacity at 150ms |
| Toast | 400ms enter / 240ms exit | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(16px)` | travel removed; opacity at 150ms |
| List / grid enter | 400ms per item, 80ms `{motion.stagger-step}` | `{motion.ease-enter}` | `opacity`, `translateY(24px)` | travel and stagger removed; all items fade together at 150ms |
| List / grid exit | 240ms | `{motion.ease-exit}` | `opacity`, `translateY(-8px)` | travel removed; opacity at 150ms |
| Loading (spinner, skeleton) | 900ms `{motion.duration-emphasis}` loop | `{motion.ease-standard}` | `transform: rotate()`, `opacity` 0.4↔1 | rotation removed; single opacity pulse at 150ms, or static skeleton |
| Hero / product ambience (slow image scale, radial glow) | 900ms+ loop, stated as ambience | `{motion.ease-standard}` | `transform: scale()`, `opacity` | frozen at end state |

Every exit is shorter than its entrance. Only `transform` and `opacity` animate. The only loops are the loader and the one named brand ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 28-31 (`REQUIRED_COLOR_ROLES["text-dim"]`) | The `text-dim` role reports missing for oura, but this file plainly owns it twice under other names: `ash` #838280 ("muted grey for meta text, titles-under-names, and utility captions") and `mute` #a8a5a0 ("warm grey for the quietest captions and for secondary text on dark bands"), both declared in `## Colors` → Text. `mute` just misses the existing `^muted$` pattern by one character. Per SPEC section 1 this is a harness bug, so **no alias was added**. | Add `r"^ash$"`, `r"^mute$"` and `r"^mute-"` to the `text-dim` pattern list. Note the consequence, which is correct and desirable: `check_all("text-dim", ...)` would then surface ash at 3.42:1 / 3.84:1 and mute at 2.19:1 as measured failures. Both are already disclosed with those exact ratios in this file's Accessibility section, so the fix would read as disclosed, not as a new deduction. |
| `theme-audit/audit.py` line 32 (`REQUIRED_COLOR_ROLES["border"]`) + line 207-216 (binding fallback) | `silver` #cccac7 is the extracted *selected*-state border of `pill-tab` and measures 1.46:1 on canvas — a real boundary failure the harness never reports. The binding fallback at line 207 only runs `if not roles.get("border")`, so once a name-matched `border` token exists, every other token declared as a `borderColor` is invisible to `check_all("border", ...)`. | Run the component-binding sweep unconditionally and union its results into the tones `check_all("border", ...)` iterates, instead of using it only as a fallback when no name matches. |
| `theme-audit/audit.py` line 534-537 (`score["tokens"]`) | A file that correctly declines to invent an alias is scored identically to one that simply lacks the role. There is no way for the harness to distinguish "role genuinely absent" from "role present under a name the regex misses". | Minor: when a role resolves from a component binding or is claimed in the report, surface it as `roles_from_bindings` (which already exists for `border`) and exclude it from `roles_missing` rather than deducting. |

### Needs approval

Four extracted values fail their threshold and were **not** changed. Each is recorded with the nearest passing value and the usage note that would make the real value defensible.

1. **`colors.hairline` #e1dcd3 — 1.22:1 on canvas, 1.37:1 on surface (needs 3.0:1).** Nearest passing on canvas: #8a8171 (3.43:1); the lightest warm tone that clears 3:1 on *white* as well is around #938a7a (3.41:1 on white, 3.04:1 on cream). Defensible usage note: the extracted hairline is a decorative seam between blocks of the same colour world only, never the sole boundary of a control or an input. Approval needed to keep the extracted tone bound as `borderColor` on `feature-card`, `button-icon-circular`, `ex-cart-drawer` and `ex-data-table-cell`, or to re-point those four bindings at `{colors.hairline-strong}` — I added the token and the prose rule but left the extracted bindings untouched, since changing them would rewrite an extracted fact.
2. **`colors.ash` #838280 — 3.42:1 on canvas, 3.84:1 on surface (needs 4.5:1).** Nearest passing: #6e6c69 (4.66:1 on cream, 5.23:1 on white). Defensible usage note: ash is for 18px+ regular or 14px+ bold text, where 3:1 applies. That note does **not** cover the file's own `person-card` role label at `{typography.caption}` 13px/400, so either that binding moves to 18px+, or ash moves to #6e6c69, or the brand's real AA failure stands as documented.
3. **`colors.mute` #a8a5a0 — 2.19:1 on canvas (needs 4.5:1).** Nearest passing on cream: #707072 (4.94:1). Defensible usage note: mute is a dark-ground tone only, where it measures 7.15:1 on `{colors.ink-band-soft}`; on the cream worlds it is decorative or a disabled tone (WCAG sets no requirement on disabled). Approval needed for that scoping.
4. **`colors.silver` #cccac7 as the `pill-tab` selected border — 1.46:1 on canvas (needs 3.0:1).** Nearest passing: #8a8171, i.e. `{colors.hairline-strong}` (3.43:1); staying inside the extracted cool-grey family would need roughly #8f8f8f (3.23:1). Defensible usage note: selection is additionally carried by `{typography.button}` weight, so the border is reinforcement rather than the sole indicator — which is now stated in the Interaction States table. The border itself remains below threshold.

Also for approval, though neither is an extracted value: the two prescribed focus rings (`#1f5ab4`, `#f7f1e8`) and the two prescribed strong tones (`#8a8171`, `#bf2a14`). The ring deliberately is not `{colors.primary}`, because the file's own Don't list reserves the action blue for the primary CTA and a stone ring would be indistinguishable from `button-outline-stone`'s own outline.

### Identity verdict

Still unmistakably Oura. The warm-paper default, the three surface worlds, the single-blue discipline, the thin Editorial New / AkkuratLL pairing and the earth-tone ramps are untouched; every added token is named and justified in the brand's own vocabulary (paper cream for the ring on ink, warm taupe for the strong hairline, a deepened action blue rather than a generic system blue), and the Motion section's signature row — imagery leading at 600ms with the headline arriving one 80ms step behind — is the brand's reveal, not a borrowed curve. Nothing in the diff reads as lifted from another file in the collection.

**Profile: Cinematic, confirmed, not switched.** SPEC section 5 rule 1 fires on the first pass: this is a hardware-flagship identity, and the file's own prose supplies the tells the rule asks for — "full-bleed lifestyle photography that carries most of the emotional weight", "the ring is photographed like jewellery", display type at weight 300 and lead at weight 100, and "long vertical silences between sections". Rule 1 explicitly says a white-canvas luxury brand is still Cinematic, which forecloses the one argument for moving this file to Calm. The honest tension is that Oura's *restraint* reads Calm — flat fills, hairline rules, no gradients, and the Overview calls the layouts "calm" outright — but rule 1 is checked before rule 4, the product hardware is the subject of the photography, and rule 4 is the terminal answer only when nothing above fires. So: Cinematic, with the proviso that this is a Cinematic at the quiet end of its profile, which is why the hover and press rows sit at `{motion.duration-instant}` / `{motion.duration-fast}` rather than reaching for the slow end on every interaction.
