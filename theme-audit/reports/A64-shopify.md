## A64 · shopify

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 3 | 4 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 2 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

`tokens` is capped at 4 deliberately. The missing role is `text-dim`, and the
brand plainly owns that role under other names (`shade-40` / `-50` / `-60`,
`link-cool-1..3`, `link-mint`, each described in `## Colors` as secondary or
tertiary ink). Adding a `text-dim` alias would satisfy a regex and nothing else,
which SPEC section 1 forbids, so the point is left on the table and the
mismatch is raised below as a harness issue.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Nothing in the file said how anything moves. Fixed. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Five measurable contrast failures, including the resting outline of `text-input`, were undisclosed. Fixed by disclosure; the hexes are untouched. |
| P0 | A Token contract | `colors.focus` | No focus ring of any kind, on either polarity. Fixed: `focus` `#ffffff` for dark surfaces, `focus-on-light` `#000000` for light, both reusing tones the palette already owns. |
| P0 | H States | every component | Only `pressed` was documented anywhere, via one component name. Seven of the eight states were absent. Fixed: a `States:` line on every component entry. |
| P1 | B Colour | `hairline-light` `#e4e4e7` | 1.27:1 on `canvas-light`, 1.22:1 on `canvas-cream`, against a 3:1 boundary minimum. Extracted and frozen, so disclosed rather than changed. It is the resting border of `text-input` and every table rule, so the real brand ships text inputs with no perceivable outline. |
| P1 | B Colour | `hairline-dark` `#1e2c31` | 1.46:1 on `canvas-night`, 1.38:1 on `canvas-night-elevated`. Extracted, disclosed, unchanged. The dark track has no perceivable card boundary. |
| P1 | B Colour | `shade-40` `#a1a1aa` | `## Colors` calls it "tertiary text on light", where it measures 2.56:1 — below AA for body and below 3:1 even as large text. The harness never saw this pair, because `shade-40` matches no `text-dim` pattern. Disclosed, with `shade-50` (4.83:1) and `shade-60` (7.73:1) named as the light-track replacements. |
| P1 | A Token contract | `text-dim` role | Genuinely present in the brand, absent as a name. Left unfilled, recorded in `## Known Gaps` with the evidence, and raised under Shared issues. |
| P1 | A Token contract | `shadow:` group | The Elevation table states four real `rgba(...)` stacks with no token to reference, which SPEC section 1 names as exactly the condition that requires a `shadow:` group. Added `shadow.level-0` … `level-4` and referenced them from the table and from `card-feature-cinematic`. |
| P1 | C Elevation | `canvas-night` / `canvas-night-elevated` | The two dark layers measure 1.06:1 — the fill step is invisible. Separation is carried entirely by `{shadow.level-1}` / `{shadow.level-2}`. Elevation is at least expressed consistently (shadow per track, not shadow-and-border at random), but a dark card has no boundary at all if shadows are suppressed. Documented in a new "Layer Separation (measured)" subsection. |
| P1 | C Elevation | `canvas-cream` / `canvas-light` | 1.04:1. The cream canvas is a warmth choice, not a layer; the light track's depth is `{shadow.level-3}` plus the (failing) hairline. Documented. |
| P2 | B Colour | `hairline-dark` vs `surface-elevated-dark` | Same hex, `#1e2c31`, under two names. The nominal pair measures 1.0:1. They are never drawn against each other, so this is a token-naming collision rather than a rendered defect, but one of the two should be renamed or re-valued. Disclosed as manufactured. |
| P2 | B Colour | `shade-50` on `aloe-10` | 4.15:1 — just under AA. Not claimed by the prose, but a featured pricing card is the obvious place someone would reach for the ladder's mid tone. Noted in `## Accessibility`. |
| P2 | D Typography | all 15 roles | Every role carries family, size, weight, line height and letter-spacing. Body is readable on every surface it is actually drawn on (21.0:1 light, 21.0:1 dark). No change needed. |
| P2 | E Shapes | `rounded.xs` 4px / `rounded.sm` 5px | One step recorded twice, 1px apart. Kept as extracted, noted in Known Gaps. |
| P2 | E Shapes | `rounded.xs` bindings | Bound as the radius of `nav-bar-light`, `nav-bar-dark`, `footer-dark`, `footer-light` and `link-on-dark`, none of which is a rounded element. Reads as a default dropped where no radius applies. Noted, not changed — the bindings are extracted. |
| P2 | E Layout | spacing ladder | `## Layout` cites ~48px section padding and 128–192px of vertical air; the ladder jumps 32px → 64px and stops. Left as prose; adding steps would invent extraction. Noted in Known Gaps. |
| P2 | G Accessibility | `link-on-dark` | No underline at rest, colour identical to body ink — a WCAG 1.4.1 risk for an inline link inside body copy. Noted with a scoped recommendation. |
| P2 | I Identity | whole file | Cinematic is the right profile; see Identity verdict. No change. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | (no ring) -> `focus: "#ffffff"`, `focus-on-light: "#000000"`, with a comment naming the tones they reuse | SPEC section 1: the focus role is the one exception, and a ring must be addressable as `focus*`. Both hexes are already in the palette, so this is a role binding, not a new brand colour. Two rings because the file documents both light and dark signature surfaces. |
| frontmatter, new `shadow:` group | (none) -> `level-0` … `level-4` carrying the four extracted stacks verbatim | SPEC section 1: required where the file documents real shadow values in prose. It did, with nothing to reference. |
| frontmatter, new `motion:` group | (none) -> the Cinematic block from SPEC section 4, verbatim, with a comment marking it prescribed | Brief F; no deviation from the profile's values. |
| `## Elevation & Depth` table | 3 columns -> 4, each row gaining its `{shadow.level-N}` token | So the stacks are referenceable rather than copied by hand. |
| `## Elevation & Depth`, new subsection | (none) -> "Layer Separation (measured)" with the 1.06:1, 1.46:1 and 1.04:1 fill steps | Dimension C: the layers are *not* distinguishable by fill, and a reader should know the shadow is load-bearing. |
| `## Components`, 14 entries | no states -> a `States:` line per entry, naming default, hover, focus-visible, active/pressed, disabled, loading, selected, error where each applies | Dimension H. `pill-tag-mint`, `pill-tag-shade` and `card-pistachio-band` say plainly that they have one state, since they are labels and bands, not controls. |
| `## Components` → `text-input` | (no note) -> a line stating the resting border measures 1.27:1 | The failure belongs where a reader meets the component, not only in the Accessibility section. |
| new `## Motion & Animation`, after `## Components` | (none) -> prescribed-not-measured first line, five principles, an 11-row interaction table, a `@media (prefers-reduced-motion: reduce)` block | Brief F. Eleven rows: the ten required plus the hero reveal, which is the Cinematic signature and the one piece of brand ambience, stated as such. |
| new `## Accessibility`, after `## Motion & Animation` | (none) -> 16 passing pairs, 6 disclosed failures, the two-ring coverage table, tap targets, reduced motion, 1.4.1 notes | Brief G. |
| new `## Known Gaps`, at end after `## Iteration Guide` | (none) -> `text-dim` evidence, prescribed-vs-extracted split, untokenised prose values, scale irregularities, what a document cannot measure | SPEC section 3 requires it last; the legacy `## Iteration Guide` is kept verbatim ahead of it. |

Section order now matches SPEC section 3 exactly. No existing prose was reflowed
and no extracted hex, type value, radius, spacing step or `components:` binding
was altered.

### Contrast checks

All computed with WCAG 2.1 relative luminance via a `python3` stdlib snippet; no
value here is estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `on-primary` `#ffffff` / `canvas-night` `#000000` | 21.0:1 | 4.5:1 | Pass |
| `on-primary` / `canvas-night-elevated` `#0a0a0a` | 19.8:1 | 4.5:1 | Pass |
| `on-primary` / `surface-elevated-dark` `#1e2c31` | 14.39:1 | 4.5:1 | Pass |
| `on-primary` / `shade-70` `#3f3f46` (pressed pill) | 10.44:1 | 4.5:1 | Pass |
| `ink` `#000000` / `canvas-light` `#ffffff` | 21.0:1 | 4.5:1 | Pass |
| `ink` / `canvas-cream` `#fbfbf5` | 20.22:1 | 4.5:1 | Pass |
| `ink` / `aloe-10` `#c1fbd4` | 18.02:1 | 4.5:1 | Pass |
| `ink` / `pistachio-10` `#d4f9e0` | 18.43:1 | 4.5:1 | Pass |
| `ink` / `shade-30` `#d4d4d8` | 14.21:1 | 4.5:1 | Pass |
| `link-cool-1` `#9dabad` / `canvas-night` | 8.86:1 | 4.5:1 | Pass |
| `link-cool-2` `#9797a2` / `canvas-night` | 7.26:1 | 4.5:1 | Pass |
| `link-cool-3` `#bdbdca` / `canvas-night` | 11.3:1 | 4.5:1 | Pass |
| `link-mint` `#99b3ad` / `canvas-night` | 9.41:1 | 4.5:1 | Pass |
| `shade-40` `#a1a1aa` / `canvas-night` | 8.19:1 | 4.5:1 | Pass |
| `shade-50` `#71717a` / `canvas-light` | 4.83:1 | 4.5:1 | Pass |
| `shade-50` / `canvas-cream` | 4.65:1 | 4.5:1 | Pass |
| `shade-60` `#52525b` / `canvas-light` | 7.73:1 | 4.5:1 | Pass |
| `shade-70` / `canvas-light` | 10.44:1 | 4.5:1 | Pass |
| `focus` `#ffffff` / `canvas-night` | 21.0:1 | 3.0:1 | Pass |
| `focus` / `canvas-night-elevated` | 19.8:1 | 3.0:1 | Pass |
| `focus` / `surface-elevated-dark` | 14.39:1 | 3.0:1 | Pass |
| `focus-on-light` `#000000` / `canvas-light` | 21.0:1 | 3.0:1 | Pass |
| `focus-on-light` / `canvas-cream` | 20.22:1 | 3.0:1 | Pass |
| `focus-on-light` / `aloe-10` | 18.02:1 | 3.0:1 | Pass |
| `focus-on-light` / `pistachio-10` | 18.43:1 | 3.0:1 | Pass |
| `focus-on-light` / `shade-30` | 14.21:1 | 3.0:1 | Pass |
| `focus` / `focus-on-light` (two-tone ring over photography) | 21.0:1 | 3.0:1 | Pass |
| **`hairline-light` `#e4e4e7` / `canvas-light` `#ffffff`** | **1.27:1** | 3.0:1 | **Fail** — extracted, disclosed |
| **`hairline-light` / `canvas-cream` `#fbfbf5`** | **1.22:1** | 3.0:1 | **Fail** — extracted, disclosed |
| **`hairline-dark` `#1e2c31` / `canvas-night` `#000000`** | **1.46:1** | 3.0:1 | **Fail** — extracted, disclosed |
| **`hairline-dark` / `canvas-night-elevated` `#0a0a0a`** | **1.38:1** | 3.0:1 | **Fail** — extracted, disclosed (the fill of `card-feature-cinematic`; became a harness-reported pair when `surface` re-resolved mid-review) |
| **`shade-40` `#a1a1aa` / `canvas-light`** | **2.56:1** | 4.5:1 | **Fail** — extracted, disclosed |
| **`shade-50` / `aloe-10`** | **4.15:1** | 4.5:1 | **Fail** — extracted, disclosed |
| `hairline-dark` / `surface-elevated-dark` | 1.0:1 | 3.0:1 | Fail — **manufactured**: same hex under two names, never drawn against each other |
| `ink` `#000000` / `canvas-night` `#000000` | 1.0:1 | 4.5:1 | Fail — **manufactured**: `ink` is light-track ink; dark surfaces take `on-primary` at 21.0:1 |
| `ink` / `surface-elevated-dark` `#1e2c31` | 1.46:1 | 4.5:1 | Fail — **manufactured**: same reason; the real pair is `on-primary` at 14.39:1 |
| Layer step: `canvas-night-elevated` / `canvas-night` | 1.06:1 | — | fill step effectively invisible |
| Layer step: `surface-elevated-dark` / `canvas-night` | 1.46:1 | — | very shallow |
| Layer step: `canvas-cream` / `canvas-light` | 1.04:1 | — | warmth, not a layer |

The three manufactured pairs are disclosed in `## Accessibility` as
manufactured, with the pair that actually renders named alongside each. They are
disclosed rather than argued away because the harness will keep generating them
until the role-resolution issues below are fixed, and a reader of the file
deserves to know which of the five is a product defect and which is an artefact.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, nav item, card) | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity`; `transform: scale(1.01)` on cards only | No scale; opacity only at `{motion.duration-reduced}` 150ms |
| Press / active | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `transform: scale(0.98)` | No scale; fill/opacity step only at 150ms |
| Focus-visible ring | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` (ring fades in at a fixed 2px offset) | Ring appears at full opacity immediately; offset never animates |
| Page / route transition | enter `{motion.duration-slow}` 600ms, exit `{motion.duration-base}` 400ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`; `transform: translateY(24px)` | Cross-fade only at 150ms, no travel |
| Modal / drawer | enter `{motion.duration-base}` 400ms, exit `{motion.duration-fast}` 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`; `transform: scale(0.98)` (modal) or `translateY(100%)` (drawer) | Opacity only at 150ms; drawer appears in place |
| Dropdown / nav menu | enter `{motion.duration-fast}` 240ms, exit `{motion.duration-instant}` 120ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`; `transform: translateY(-4px)` | Opacity only at 150ms |
| Toast | enter `{motion.duration-base}` 400ms, exit `{motion.duration-fast}` 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`; `transform: translateY(16px)` | Opacity only at 150ms |
| List enter | `{motion.duration-base}` 400ms per item, `{motion.stagger-step}` 80ms between | `{motion.ease-enter}` | `opacity`; `transform: translateY(16px)` | All items fade together at 150ms; stagger 0ms |
| List exit | `{motion.duration-fast}` 240ms, no stagger | `{motion.ease-exit}` | `opacity`; `transform: translateY(-8px)` | Opacity only at 150ms |
| Loading | `{motion.duration-emphasis}` 900ms, looping | `{motion.ease-standard}` | `transform: rotate()` (spinner); `opacity` 1→0.4→1 (skeleton) | Loop frozen; static indicator with `aria-busy` |
| Hero reveal (brand ambience, once on enter) | `{motion.duration-emphasis}` 900ms | `{motion.ease-enter}` | `transform: scale(1.04 → 1.0)` on the photo; headline `opacity` + `translateY(24px)` delayed `{motion.stagger-step}` ×2 | Frozen; photo painted at scale 1.0, headline fades at 150ms |

Rule compliance: `transform` and `opacity` only, in every row. Every exit is
shorter than its matching entrance (600/400 page, 400/240 modal, 240/120
dropdown, 400/240 toast, 400/240 list). Nothing animates on first paint in a way
that delays content — the hero is painted at its final position before it
settles. The only loops are the loader and the hero ambience, and the ambience is
labelled as such. `{motion.duration-reduced}` is 150ms, below the profile's own
`duration-fast` of 240ms, which is the reason the token exists.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, `REQUIRED_COLOR_ROLES["text-dim"]`, lines 29-34 | The role is reported missing although the brand plainly owns it under a numeric-ladder and link-family naming convention: `shade-40` ("tertiary text on light, secondary text on dark"), `shade-50` ("secondary text on light"), `shade-60`, and `link-cool-1..3` / `link-mint` ("muted footer / tertiary link colors"). Per SPEC section 1 this is a harness bug, not a token to invent. | Do **not** simply add `^shade-\d+$` to the pattern list: `find_role_strongest` would then pick the lightest shade, and `check_all("text-dim", "canvas", 4.5, …)` would measure every shade against the *dark* canvas, manufacturing failures for `shade-60` and `shade-70`, which are light-track inks (`shade-70` on `canvas-night` is about 2.2:1). The role needs the same binding-derived resolution that `border` already gets at lines 265-273: resolve `text-dim` from a tone the `## Colors` prose labels secondary/tertiary/muted ink, or from a `components:` `textColor` on a non-primary role, and scope it to the ground it is described as sitting on. A regex over names cannot see the polarity. |
| `theme-audit/audit.py`, `theme_of()`, lines 340-356 | An unmarked `ink` is treated as belonging to the file's default theme, and `canvas-night`'s `dark` marker is nulled because it matches `canvas_polarity`. Both land in "default", so the harness measures a light-track ink on a dark-track floor and reports `ink on canvas-night` at 1.0:1 and `ink on surface-elevated-dark` at 1.46:1 — pairs this brand never renders. | Let `components:` bindings override the name heuristic for the `text` role, the way they already do for `border` and `surface`. Here `ink` is bound as `textColor` on `button-outline-on-light`, `button-aloe-pill`, `text-input`, `card-pricing`, `card-pricing-featured`, `card-pistachio-band`, `pill-tag-mint`, `pill-tag-shade`, `nav-bar-light` and `footer-light` — ten light grounds and not one dark ground. That is decisive evidence that `ink` is light-theme, and it is already parsed. |
| `theme-audit/audit.py`, surface preference — **fixed upstream mid-review, no action needed** | At the start of this review the `surface` role resolved to `surface-elevated-dark`, which this file's own prose describes as "used on a small subset of dark cards", so every `… on surface` pair was measured against a ground the site barely renders. `dd934af` ("surface preference") added the nearest-the-canvas selection over name-matched and `canvas-`prefixed candidates at lines 278-289, and `surface` now resolves to `canvas-night-elevated`, which is correct for this file. | None. Recorded because it changed the numbers mid-review: it replaced the `ink on surface-elevated-dark` pair with `hairline-dark on canvas-night-elevated` at 1.38:1, which is disclosed in `## Accessibility` alongside the rest. Both are listed in the Contrast checks table. |
| `theme-audit/audit.py`, `disclosed()`, lines 618-632 | Disclosure is matched by substring on the foreground token name, so a short name is a substring of longer ones — `ink` matches any line containing `link-cool-1`, `hairline` matches `hairline-light` and `hairline-dark` alike. A file can satisfy a disclosure it never wrote. | Match the foreground on a word boundary, and require the background token or hex on the same line as well as the foreground, so a disclosure is tied to its own pair rather than to any line that mentions a prefix. |

None of these changes the honest verdict on this file; they change which numbers
the harness prints about it. `audit.py` moved under me during the review
(`dd934af`, `b805d65`, and a later `40a1161` on another site), so the line
numbers above are against the working tree as of this report.

### Needs approval

1. **Re-point the extracted `hairline-light` where a boundary must be seen.**
   `hairline-light` `#e4e4e7` measures 1.27:1 on `canvas-light` and 1.22:1 on
   `canvas-cream`, against a 3:1 minimum. It is the resting outline of
   `text-input`, so the real product ships a text field with no perceivable
   border. The palette already owns a passing tone — `shade-50` `#71717a` at
   4.83:1 on `canvas-light` and 4.65:1 on `canvas-cream` — so SPEC section 2
   needs no new token here, only a decision. Nearest passing value if the brand
   would rather keep a light hairline: `#767676` (4.54:1 on `#ffffff`), or
   `#949494` (3.0:1 exactly) if 3:1 is the only target. **Usage note that would
   make the extracted value defensible as it stands:** `hairline-light` is
   decorative only — table zebra rules, card edges and dividers that carry no
   information a user must perceive — and any boundary that *is* the sole
   indicator of an interactive element's extent uses `shade-50`. I have written
   the disclosure and named `shade-50` as the replacement, but I have not
   re-pointed the prose or added a `borderColor` binding, because the extracted
   bindings are facts about the real site.
2. **Re-point or re-scope the extracted `hairline-dark`.** 1.46:1 on
   `canvas-night`, 1.38:1 on `canvas-night-elevated`. Nearest passing value on
   black: `#5f5f5f` (3.0:1). Defensible as extracted only if dark-card chrome is
   accepted as decoration and the card's extent is communicated by
   `{shadow.level-2}`'s `rgba(255,255,255,0.08)` ring instead — which is what
   the Elevation table already describes, and which is probably the true
   intention. A brand owner should confirm that reading.
3. **Resolve the `hairline-dark` / `surface-elevated-dark` collision.** Both are
   `#1e2c31`. One of the two names should go, or one value should move. I have
   not guessed which.
4. **`shade-40` on the light track.** 2.56:1 on `canvas-light`, while
   `## Colors` describes it as tertiary text on light. Either the description is
   wrong (it is safe at 8.19:1 on the dark track) or the usage is. Nearest
   passing value for light-track body text: `#767676` (4.54:1). I have disclosed
   the failure and named `shade-50` / `shade-60` as the replacements without
   touching the extracted hex or its description.
5. **Focus-ring geometry.** The 2px stroke and 2px outer offset are prescribed,
   not extracted. The *colours* reuse `on-primary` and `ink`, so no new brand
   colour has been introduced, but the geometry needs a brand owner's sign-off.
6. **All motion values**, as prescribed from the Cinematic profile, and all
   hover / disabled / loading / selected / error treatments in `## Components`.
   Only `button-primary-pill-pressed` is extracted.

### Identity verdict

Still unmistakably this brand, and the Cinematic assignment is correct — I am
keeping it.

The file's own extracted content satisfies SPEC section 5 rule 1 on the
signature test rather than the sector test: full-bleed merchant photography that
escapes the container, 96px display type at weight 330, "one and only one action
per band", 128–192px of vertical air, and an explicit instruction that
photography does the work gradients and illustrations do elsewhere. That is
precisely "full-bleed imagery scales slowly; type arrives late and settles". The
near-black canvas supports it but is not the reason; a light-canvas brand with
the same signals would score the same. Rule 3 (Playful) is the only plausible
competitor, because of the aloe and pistachio greens — and it fails on role:
those tones are pastel section fills and one featured-tier card background, the
file explicitly forbids putting type on them, and the type voice is a 330-weight
editorial display cut, not a light informal one. Rule 2 does not fire. Rule 1
does.

The additions are shaped to the brand rather than dropped in from a template.
The two rings are monochrome because the brand's accent *is* its ink, which
SPEC section 1 anticipates for exactly this case, and the Accessibility section
says which existing tone each one reuses. The motion table's one profile-level
addition is the hero reveal, which is the thing this brand actually does. The
two-track polarity split survives everywhere: every state line, every ring
assignment and every reduced-motion note is written per track, and the greens
stay on the light track throughout. The one thing a reader would now notice that
they could not before is how little of this brand's layer separation comes from
colour — 1.06:1 between the two dark canvases — and that is a fact about the
brand, not drift toward a token dump.
