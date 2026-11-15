## A76 · vercel

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 1 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

Contrast moved 1 -> 5 by **disclosure, not by changing a hex**. All seven
failures are extracted and frozen; all seven are now named in `## Accessibility`
with their measured ratios, so the harness counts 7 disclosed / 0 undisclosed.
No brand hex was altered.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule. Zero durations and zero easing curves anywhere in the file. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section. Seven contrast failures undisclosed, including the brand's only boundary tone. |
| P0 | B/G · Colour | `{colors.hairline}` `#ebebeb` | 1.19:1 on `{colors.canvas}`, 1.14:1 on `{colors.canvas-soft}` against 3.0:1 — and it is bound as `borderColor` on `form-input`, `form-input-sm`, `form-input-lg`, `nav-cta-ask-ai`, `icon-button-circular` and `ex-pricing-tier`. The real brand's card edge and input edge fail WCAG 1.4.11. |
| P0 | C · Elevation | surface ladder | `{colors.canvas}` -> `{colors.canvas-soft}` is **1.04:1**; `{colors.canvas}` -> `{colors.canvas-soft-2}` is **1.09:1**. The four-step ladder is not perceptible as fill, so the (failing) hairline is the *only* thing separating a card from the page. Compounding failure, not two independent ones. |
| P0 | A · Tokens | `focus` role | Absent. No ring of any kind in the captured surfaces. |
| P1 | B · Colour | `{colors.warning}` `#f5a623` | 2.03:1 on canvas — fails AA as text and does not even reach the 3:1 large-text bar. The palette already owns `{colors.warning-deep}` at 5.12:1. |
| P1 | B · Colour | `{colors.mute}` `#888888` | 3.54:1 / 3.40:1 against 4.5:1 as text. Prose called it "fine print, low-key labels" — i.e. read-this text at a failing ratio. |
| P1 | B · Colour | `{colors.hairline-strong}` `#a1a1a1` | 2.58:1 / 2.48:1 against 3.0:1. Prose offered it as the "slightly-stronger divider", which reads as the accessible alternative to `hairline`. It is not one. |
| P1 | H · States | all ~40 component entries | Only `hover` and `active` documented anywhere. `focus-visible`, `pressed`, `disabled`, `loading`, `selected`, `error` named nowhere in the file. |
| P1 | Sections | Responsive Behavior | Present only as `### Responsive Strategy` inside `## Layout` — no top-level section. |
| P1 | Sections | Known Gaps | Absent. Every prescribed value was therefore undisclosed as prescribed. |
| P1 | G · Tap targets | `nav-cta-*` | The file claimed nav buttons "inflate touch area through `{spacing.xs}` padding on mobile to meet the 44 × 44 px floor". The declared padding is `0px {spacing.xs}` — **horizontal only**. 28 px height + 0 vertical padding = 28 px. The file's own numbers contradicted its own claim. |
| P2 | A · Tokens | `shadow:` group | Elevation & Depth documents six real stacked-shadow values in prose with no token to reference — the exact condition SPEC section 1 says requires a `shadow:` group. |
| P2 | E · Shapes | `{rounded.xs}` | Shapes table described 4 px as "the `nav-cta-signup` 6-px-radius button (mapped to `xs/sm`)". The component binds `{rounded.sm}` 6 px. The row described a binding that does not exist. |
| P2 | I · Identity | Do's and Don'ts | Direct self-contradiction: a Do says the 100 px pill and the 6 px nav radius "coexist deliberately"; a Don't forbade pairing them "on the same screen". The real page does exactly that (pill hero + 6 px nav). |
| P2 | I · Identity | Don'ts | "the four-pair gradient palette" — the file documents three pairs (develop / preview / ship). |
| P2 | — | Examples note | Stale generator boilerplate: refers to `TO_FILL` markers to "resolve in the LLM judgment pass"; no `TO_FILL` marker exists in the file. Left verbatim (auto-generated upstream), recorded in Known Gaps. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | *(no focus role)* -> `focus: "#0070f3"` | The one permitted role binding per SPEC section 1. Reuses the existing `{colors.link}` / `{colors.success}` hex unchanged — no new brand colour, and not an alias: it carries a distinct job on a distinct surface. Measured 4.55 / 4.36 / 4.18 / 3.94:1 against the four grounds the file defines. |
| frontmatter | *(no `motion:`)* -> **Crisp** block verbatim from SPEC section 5 | Ten keys, no deviations. Nothing extracted to displace it: `durations_found` and `easings_found` were both empty before the edit. |
| frontmatter | *(no `shadow:`)* -> `shadow:` with `level-0`..`level-5` | Transcribes the six Elevation & Depth values already in the prose, so `{shadow.level-N}` resolves. Values quoted so the parser does not read ` #00000005` as a trailing comment. |
| Colors · Surface · Hairline | Use note only -> + frozen-and-fails disclosure, scoped to decoration, interactive boundaries re-scoped to `{colors.mute}` | SPEC section 2 step 1: the palette already owns a passing tone (`{colors.mute}` at 3.54 / 3.40:1), so re-scope the prose and **add nothing**. No `hairline-accessible` token was invented. |
| Colors · Surface · Hairline Strong | "slightly-stronger divider" -> + 2.58 / 2.48:1 disclosed, explicitly *not* a boundary fix, with its passing 6.94:1 on the dark band | Stops it reading as the accessible alternative it is not. |
| Colors · Text · Mute | "fine print, low-key labels" -> + 3.54 / 3.40:1 disclosed; demoted to placeholder glyphs, read-this text goes to `{colors.body}` (8.45:1) | Frozen tone, honest scope. |
| Colors · Text | *(new bullet)* `Focus` | States which existing tone the ring reuses, as SPEC section 1 requires. |
| Colors · Semantic · Warning | "Caution / pending status indicator" -> "**Fill and icon only**", 2.03:1 disclosed, text goes to `{colors.warning-deep}` (5.12:1) | Step 1 again: the passing tone already exists in the palette. |
| `## Components` | *(new)* `### Interaction States` table, 20 rows covering every named component and `ex-*` surface | All eight state words now documented in structured rows. `badge-secondary` ("two states only") and the static bands ("default") say so plainly rather than claiming states they lack. |
| after `## Components` | *(new)* `## Motion & Animation` | First line states the system is prescribed and was not measured. 11-row interaction table, Crisp tokens only, `transform`/`opacity` for travel, paint-only for hover and press, `@media (prefers-reduced-motion: reduce)` block naming what is removed and what remains. |
| after Motion | *(new)* `## Accessibility` | 21-row measured contrast table (all 7 failures disclosed with ratios), focus-ring coverage table for all four grounds with the 2 px / 2 px-offset geometry, tap targets from documented heights, reduced motion, non-colour signals. |
| `## Layout` -> top level | `### Responsive Strategy` **moved** verbatim to `## Responsive Behavior` after Do's and Don'ts; its four `####` children promoted to `###` | SPEC section 3: move, never duplicate. The Layout subsection is gone, not copied. |
| Responsive Behavior · Touch Targets | 44 px claim corrected to: 28 px, horizontal padding only, clears 2.5.8 AA, 16 px short of 2.5.5 AAA, fix labelled a prescription | The claim was arithmetically false on the file's own token values. |
| end of file | *(new)* `## Known Gaps` | Separates prescribed (motion, ring geometry, hit area, boundary re-scoping, hover/press treatments) from absent-from-capture (dark mode, the 100–1000 ladder, gradient geometry) from not-computable. |
| Shapes table, `{rounded.xs}` row | "the `nav-cta-signup` 6-px-radius button (mapped to `xs/sm`)" -> "No component in this file binds it; `nav-cta-signup` binds `{rounded.sm}` 6 px, not this." | Removed a false binding claim. |
| Don'ts | "on the same screen" -> "*inside one button cluster*", with the page-level coexistence stated | Resolved the contradiction in favour of what the brand actually does. |
| Don'ts | "four-pair gradient palette" -> "three-pair gradient palette (develop / preview / ship)" | Matches the three pairs the file documents. |

**Not changed, deliberately:** every `components:` binding. `{colors.hairline}`
remains the declared `borderColor` on all six components that extracted it.
SPEC section 2 step 3 — those are facts about the real site, and silently
re-pointing them would make the document describe a product that does not exist.
The prose now says to draw interactive boundaries in `{colors.mute}`; the
binding question is under Needs approval below.

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`, standard library only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#171717` / `canvas` `#ffffff` | 17.93:1 | 4.5 | Pass |
| `ink` / `canvas-soft` `#fafafa` | 17.18:1 | 4.5 | Pass |
| `ink` / `canvas-soft-2` `#f5f5f5` | 16.44:1 | 4.5 | Pass |
| `on-primary` `#ffffff` / `primary` `#171717` | 17.93:1 | 4.5 | Pass |
| `selection-fg` `#f2f2f2` / `selection-bg` `#171717` | 16.01:1 | 4.5 | Pass |
| `body` `#4d4d4d` / `canvas` | 8.45:1 | 4.5 | Pass |
| `body` / `canvas-soft` | 8.10:1 | 4.5 | Pass |
| **`mute` `#888888` / `canvas`** | **3.54:1** | 4.5 | **Fail — frozen, disclosed** |
| **`mute` / `canvas-soft`** | **3.40:1** | 4.5 | **Fail — frozen, disclosed** |
| **`hairline` `#ebebeb` / `canvas`** | **1.19:1** | 3.0 | **Fail — frozen, disclosed (bound boundary)** |
| **`hairline` / `canvas-soft`** | **1.14:1** | 3.0 | **Fail — frozen, disclosed** |
| **`hairline-strong` `#a1a1a1` / `canvas`** | **2.58:1** | 3.0 | **Fail — frozen, disclosed** |
| **`hairline-strong` / `canvas-soft`** | **2.48:1** | 3.0 | **Fail — frozen, disclosed** |
| **`warning` `#f5a623` / `canvas`** | **2.03:1** | 4.5 | **Fail — frozen, disclosed (fill only)** |
| `hairline` / `primary` | 15.04:1 | 3.0 | Pass (dark band only) |
| `hairline-strong` / `primary` | 6.94:1 | 3.0 | Pass |
| `warning-deep` `#ab570a` / `canvas` | 5.12:1 | 4.5 | Pass — the warning text tone |
| `link` `#0070f3` / `canvas` | 4.55:1 | 4.5 | Pass by 0.05 |
| `link` / `canvas-soft` | 4.36:1 | 4.5 | Fail — disclosed; use `link-deep` 5.53:1 on tinted grounds |
| `link` / `canvas-soft-2` | 4.18:1 | 4.5 | Fail — disclosed; `link-deep` 5.29:1 |
| `error` `#ee0000` / `canvas` | 4.53:1 | 4.5 | Pass by 0.03 |
| `error-deep` `#c50000` / `canvas-soft` | 5.96:1 | 4.5 | Pass |
| `highlight-pink` `#ff0080` / `canvas` | 3.77:1 | 4.5 | Gradient stop only — never text |
| `cyan` `#50e3c2` / `canvas` | 1.60:1 | 4.5 | Gradient stop only; 11.19:1 on `primary` |
| **focus** `#0070f3` / `canvas` | 4.55:1 | 3.0 | Pass |
| **focus** / `canvas-soft` | 4.36:1 | 3.0 | Pass |
| **focus** / `canvas-soft-2` | 4.18:1 | 3.0 | Pass |
| **focus** / `primary` (dark band, `code-editor-mockup`, `pricing-card-featured`) | 3.94:1 | 3.0 | Pass |
| *layer separation* `canvas` / `canvas-soft` | 1.04:1 | — | Imperceptible |
| *layer separation* `canvas` / `canvas-soft-2` | 1.09:1 | — | Imperceptible |
| *layer separation* `canvas-soft` / `canvas-soft-2` | 1.04:1 | — | Imperceptible |
| *layer separation* `canvas` / `primary` | 17.93:1 | — | The only real depth cue in the brand |

The `link` rows at 4.36 and 4.18:1 are not in the harness's seven — the harness
checks semantic tones against the canvas only. They are real failures on the
file's own tinted grounds, found by hand and disclosed in the Accessibility
section with the `link-deep` remedy.

**One ring, not two.** The file documents light *and* dark signature surfaces,
which normally forces a `focus` / `focus-on-dark` pair. It does not here:
`#0070f3` is mid-luminance enough to clear 3:1 on all four grounds, including
`{colors.primary}` at 3.94:1. SPEC section 1 explicitly prefers the single
mid-luminance ring where it works, so a second ring would have been noise. The
2 px offset is load-bearing: it puts the ring on the *surface behind* the
control, which is the only reading under which a single value can serve a white
canvas and an ink band — requiring it to clear the black `button-primary` fill
too is arithmetically impossible.

### Motion inventory

Prescribed, Crisp profile, stated as prescribed in the section's first line.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `background-color`, `border-color`, `color` — paint only | Unchanged; no travel or scale exists to remove |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` 1 -> 0.85 on the fill | Unchanged; already under 100ms and opacity-only |
| Focus-visible ring | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on the ring layer (`box-shadow` outside `{shadow.level-1}`) | Ring appears with no fade; never suppressed or delayed |
| Page / route transition | in 150ms `{motion.duration-base}`, out 100ms `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(4px)`, content column only | `opacity` only at `{motion.duration-reduced}` 100ms, no translate |
| Modal / drawer | in 150ms, out 100ms | `{motion.ease-enter}` / `{motion.ease-exit}` | modal `opacity` + `translateY(8px)`; drawer `opacity` + `translateX(100%)`; backdrop `opacity` | `opacity` only at 100ms; panel appears in final position |
| Dropdown / menu | in 100ms, out 60ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(-2px)` | `opacity` only, no translate |
| Toast | in 150ms, out 100ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px)` | `opacity` only at 100ms, no travel |
| List / grid enter | 100ms per item, `{motion.stagger-step}` 20ms apart, capped at 8 | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px)` | `opacity` only, stagger 0, all at once |
| List / grid exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity`, no stagger | Unchanged |
| Loading (skeleton) | `{motion.duration-emphasis}` 300ms per half-cycle, infinite | `{motion.ease-standard}` | `opacity` 0.4 <-> 1 on `{colors.canvas-soft-2}` | Frozen at static 0.6 opacity |
| Loading (spinner) | 600ms per revolution, infinite | linear | `transform: rotate()` | Replaced by a static mono status label |

Exit is shorter than its entrance on every row. Only the two loaders are
infinite, which SPEC section 6 permits; the brand has no ambience, and the file
says the mesh gradient must stay static. Harness `layout_animation_mentions` is
empty after the edit.

Hover and press are deliberately **paint-only**. SPEC section 6 permits this
explicitly ("a paint-only change ... is permitted and needs no apology"), and on
a near-monochrome developer brand with three 1–2 px shadow offsets, inventing a
scale pop to satisfy a literal reading of "transform and opacity only" would
contradict the identity. Both use the same duration tokens as every other state
change.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line ~22, `REQUIRED_COLOR_ROLES["canvas"]` | Pattern order puts `^canvas$` before `^canvas-`, so the token *literally named* `canvas` always takes the page-floor role. This file's prose says the opposite: `{colors.canvas-soft}` `#fafafa` is "the default page background — almost every section sits on this tone", and `{colors.canvas}` `#ffffff` is "the pure-white card / dialog / modal surface". The harness therefore resolves `canvas=canvas` (the card) and `surface=canvas-soft` (the page) — **the two roles are swapped relative to the document.** Low impact here only because the two tones are 1.04:1 apart, so every ratio shifts by under 4% and no failure is hidden or manufactured. On a file with a stronger page tint it would measure against a ground the site never renders. | Prefer a `canvas-*` token that a `components:` entry binds as the `backgroundColor` of a band/page/section component over the bare `canvas` key, mirroring the existing `roles_from_bindings` logic for `surface` and `border`. Fallback to pattern order only when no binding settles it. |
| `theme-audit/audit.py` line ~508, the SEMANTIC check | Semantic tones are measured as text against the canvas only, never against the file's other light grounds. `{colors.link}` passes on `#ffffff` at 4.55:1 and fails on both `{colors.canvas-soft}` (4.36:1) and `{colors.canvas-soft-2}` (4.18:1) — a real failure on the tone the file calls its default page background, invisible to the harness. | Run the SEMANTIC loop over every same-theme ground in `surface_keys`, as `check_all` already does for `border` and `text-dim`, rather than against `roles["canvas"]` alone. |
| `theme-audit/audit.py` line ~41, `REQUIRED_COLOR_ROLES["focus"]` | Pattern `^[a-z]+-focus$` would let a token like `card-focus` take the role, but `^[a-z]+-ring$` and `^focus-` mean a composite ring's *inner* band can also claim it; combined with `find_role_strongest` against the canvas, the reported representative can be the band rather than the ring. Not triggered by this file (single `focus` key), reported for the other eighty-three. | Exclude the `(inner|inset|halo)` tokens from role representation the same way the `focus_tokens` / `focus_bands` split already does for coverage. |
| `theme-audit/SPEC.md` section 1, shadow paragraph | "A `shadow:` group is required only where the file documents real shadow values in its prose" is a hard requirement that `audit.py` never checks and no score reflects, so compliance is invisible and agents will diverge on it. This file documented six real stacked-shadow values with no token group. | Either add a `shadow` check to the token score, or mark the sentence as advisory in SPEC so the 84 reviews do not split on it. |

### Needs approval

1. **Re-bind the interactive boundaries from `{colors.hairline}` to `{colors.mute}`.**
   Six `components:` entries declare `borderColor: "{colors.hairline}"` —
   `form-input`, `form-input-sm`, `form-input-lg`, `nav-cta-ask-ai`,
   `icon-button-circular`, `ex-pricing-tier`. At 1.19:1 on `{colors.canvas}` that
   border is not a visible boundary, so every text input and the bordered nav
   button fails WCAG 1.4.11 as shipped. The bindings are left exactly as
   extracted and the prose now instructs `{colors.mute}` (3.54:1 / 3.40:1, a tone
   the palette already owns). A brand owner has to decide whether the real
   product changes or the document keeps recording the failure. Nothing new needs
   inventing either way.
   *Usage note that would make the frozen value defensible:* `{colors.hairline}`
   is sound where the boundary is decorative and redundant — a table row rule
   between rows that are already separated by whitespace, or a card edge where the
   card also carries `{shadow.level-2}`. It is not defensible as the sole
   boundary of a control.

2. **`{colors.mute}` `#888888` as text.** 3.54:1 / 3.40:1 against 4.5:1.
   Nearest passing values: `#767676` clears white (4.54:1) but still fails
   `{colors.canvas-soft}` (4.35:1); `#6f6f6f` clears both (5.02:1 / 4.81:1) and is
   the value to approve if one is wanted. *Usage note that makes `#888888`
   defensible as-is:* restrict it to placeholder glyphs inside a field the user is
   about to type into, and to non-text boundary work where only 3:1 applies —
   both of which it passes. Any label a reader must actually read goes to
   `{colors.body}` (8.45:1), which the file now says.

3. **`{colors.hairline-strong}` `#a1a1a1` as a boundary.** 2.58:1 / 2.48:1
   against 3.0:1 — short by 0.42 and 0.52. Nearest passing value that clears both
   light grounds: `#919191` (3.15:1 / 3.02:1); `#8f8f8f` (3.23:1 / 3.10:1) gives
   more margin. *Usage note:* defensible unchanged as a *divider on the dark band*
   (6.94:1 on `{colors.primary}`) and as deemphasised large text, but not as the
   accessible alternative to `{colors.hairline}` on light grounds, which is how
   the original prose read.

4. **`{colors.warning}` `#f5a623` as text.** 2.03:1 — it fails AA and also fails
   the 3:1 large-text bar, so no minimum text size rescues it. Nearest passing
   value: `#8a5300` (6.33:1), but `{colors.warning-deep}` `#ab570a` (5.12:1) is
   already in the palette and is what the prose now specifies, so no new token is
   proposed. *Usage note that makes the frozen value defensible:* `#f5a623` as a
   status dot, a pending progress fill, or a band background with
   `{colors.warning-deep}` text on it — never as the text itself. Keep it for the
   dark band too, where it is 8.85:1 on `{colors.primary}`.

5. **The 44 px nav hit area.** `nav-cta-signup`, `nav-cta-login` and
   `nav-cta-ask-ai` are 28 px tall with `0px {spacing.xs}` (horizontal) padding.
   They clear 2.5.8 (AA, 24 × 24) and miss 2.5.5 (AAA, 44 × 44) by 16 px. Adding a
   44 px hit area around the 28 px visual control on touch viewports is a
   prescription, not an extracted value, and it changes the real product's touch
   behaviour — so it is flagged rather than written as fact. (Rendered size is not
   verifiable from a document; these are documented token heights.)

6. **The focus ring itself.** `{colors.focus}` reuses the existing
   `#0070f3` so no brand colour is invented, but the 2 px width, the 2 px offset
   and the "control radius + 2 px" corner rule are all prescribed — the captured
   surfaces record no ring at all. If Vercel's real ring geometry is known, it
   displaces these three values; the ratios in the Accessibility table hold for
   any geometry that keeps the offset, since the offset is what puts the ring on
   the surface behind the control.

### Identity verdict

**Crisp is correct. Keep the roster assignment.**

Assignment rule 2 fires cleanly and on the file's own evidence, not on the
brand's reputation: the Overview calls the page "a deployment dashboard's
marketing surface, written for engineers who already know the syntax"; the
monospace face carries every eyebrow, code block and terminal mockup; the
signature component is `code-editor-mockup`; the token names in the prose are
`--geist-radius`, `--geist-form-height`, `--ds-page-width`. This is an infra and
developer-tool identity by every observable signal.

The competing reading is Cinematic, and it fails. Rule 1 wants full-bleed
photography, sparse type and a slow reveal; this file has no photography at all
— the single decorative object is a **static** 2-D mesh gradient the file
explicitly forbids animating, cropping or miniaturising, and the type is dense
engineering prose at 16 px. Playful fails rule 3's role test outright: the
saturated colour appears only in that one backdrop gradient, never on an
interactive element, and the interactive palette is ink, white and three grays.
The brand's own stated restraint — weight 600 display ceiling, stacked 1–2 px
shadows "never a single heavy drop", no accent beyond ink — is the Crisp
signature: state change reads as instant, no entrance choreography.

Does it still read as Vercel after the edits? Yes, and the motion section is
where that is testable. Nothing was borrowed from another file in the
collection. Hover and press are paint-only because this brand's hover state
genuinely *is* a colour step; a 1.05 scale pop on the black pill would have been
the generic answer and would have read as someone else's product. Travel is
capped at 2–8 px, the loader is an opacity pulse on a `{colors.canvas-soft-2}`
block rather than a branded animation, and the gradient is stated as static in
three places. The file gained 6 tokens (1 colour, 10 motion keys as one group, 6
shadow keys) and 4 sections, and every added value either came from the SPEC
block verbatim, was computed from the existing palette, or transcribed prose
that was already in the file. The strongest single thing the audit added is not
a token at all — it is the Accessibility section saying plainly that a brand
famous for its clean edges has a card edge at 1.19:1 and a surface ladder at
1.04:1, which is exactly the fact anyone building on this document most needs
to know.
