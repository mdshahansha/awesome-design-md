## A40 · mistral.ai

Scores before -> after (1-5), from the harness:

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 3 | 5 |
| states | 1 | 5 |

Contrast moved from 1 to 5 by disclosure, not by altering a hex. All 14 failures
the harness found are still failures; each is now named in `## Accessibility`
with its measured ratio, which is the outcome SPEC section 2 asks for. No brand
identity colour was changed.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Known Gaps carried a loose "recommend 150–200ms ease" line instead. |
| P0 | G Accessibility | whole file | No `## Accessibility` section, so six real AA failures in the extracted palette were undocumented. |
| P0 | A Token contract | `colors` | No focus role of any kind. Nothing in the file said how focus is drawn, on a brand with three surface polarities (white/cream, near-black, saturated orange). |
| P0 | H States | `## Components` | A blockquote declared a "no-hover policy" and that hover states are "NOT documented" — directly contrary to SPEC section 7. 40 component entries named no states at all; five of the eight state words appeared nowhere. |
| P0 | B/E Borders | `text-input`, `text-area`, `button-secondary` | The only boundary of each control was `{colors.hairline-strong}`, 1.69:1 on `{colors.canvas}` — under half the 3:1 non-text minimum. A field with no other boundary was effectively invisible. |
| P1 | B Colour | `muted` | `{colors.muted}` (2.38:1 on canvas, 2.28:1 on surface) was listed as "Disabled, placeholders" but nothing scoped it, and the harness reads it as the file's secondary-text role. |
| P1 | C Elevation | `## Elevation & Depth` | Four real `rgba(...)` elevation values were written in prose with no token to reference, so nothing could cite them. SPEC section 1 requires a `shadow:` group in exactly this case. |
| P1 | B Colour | brand orange | Six component pairs sit at 3.34:1 (`#fa520f` with `#ffffff`, both directions) with no disclosure and no accessible alternative named anywhere in the file. |
| P1 | H States | contact form | No error or validation state existed for any field, on a file whose source pages include a contact form. |
| P2 | C Elevation | `card-feature-product` | Border and shadow both express the same elevation step. Kept — the extracted page does this — but now called out as the single exception rather than left as drift. |
| P2 | D Typography | all roles | Checked: every one of the 20 type roles carries fontFamily, fontSize, fontWeight and lineHeight. Body `{typography.body-md}` at 16px/1.55 in `{colors.ink}` reaches 16.48:1 on canvas and 15.51:1 on cream. No finding. |
| P2 | E Ladders | `rounded`, `spacing` | Checked: radius 4/6/8/12/16/20/9999 and spacing 4/8/12/16/20/24/32/40/48/64/96/120 are both monotonic with no value off-scale. No finding. |
| P2 | — | `card-feature` prose | Stray backtick (`` `1px solid `{colors.hairline-soft}` ``) broke the token reference visually. Fixed. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| `colors:` | — -> `focus: "#8f2600"`, `focus-on-dark: "#fff8e0"` | The missing role. `#8f2600` is the deep red end of the brand's own sunset gradient; `focus-on-dark` reuses the brand cream rather than inventing a second hue. |
| frontmatter | — -> `shadow:` group (`flat`, `subtle`, `card`, `mockup`, `modal`) | The prose already stated these rgba values; they now have tokens to reference. |
| frontmatter | — -> `motion:` group, **Crisp** block from SPEC section 5, verbatim | SPEC section 4. |
| `card-feature-product` | `shadow: "rgba(0,0,0,0.04) 0px 4px 12px"` -> `shadow: "{shadow.card}"` | Bind the literal to the new ladder. |
| `text-input`, `text-area`, `button-secondary` | `border: 1px solid {colors.hairline-strong}` -> `{colors.stone}` | A control's only boundary must clear 3:1. `{colors.stone}` is an existing extracted tone at 3.45:1 on canvas, so no hex was invented and the original value is recorded in the prose. |
| `components:` | — -> `text-input-error`, `field-error-message` | Gives the form an error state. Uses `{colors.primary-deep}` (5.03:1 on canvas) because the brand defines no error colour. |
| `## Colors` | — -> `### Focus` subsection | Documents both rings, their measured ratios on all eleven grounds, the 2px/2px-offset geometry and the two-tone ring over photography. |
| `## Colors` | hairline and `muted` entries | Each now carries its measured ratio and an explicit scope (decorative / placeholder-and-disabled only). |
| `## Elevation & Depth` | table -> table with a Token column, plus a level-0-control row | Elevation now reads one way: border at level 0, `{shadow.*}` above it. |
| `## Components` | "no-hover policy" blockquote -> a states contract blockquote | SPEC section 7 requires states; the blockquote now also marks hover/focus-visible/loading/selected/error as prescribed, not extracted. |
| `## Components` | 40 entries -> each gains a `- States:` line | SPEC section 7. Genuinely static entries (badges, bands, footer region) say so. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Token table, 12-row interaction inventory, brand-specific rules, reduced-motion CSS. |
| after that | — -> `## Accessibility` | Text, non-text, signal-colour and focus tables with measured ratios; tap targets; reduced motion; remaining gaps. |
| `## Do's and Don'ts` | +5 Do, +4 Don't | Focus ring, control boundary, ink-on-orange, Crisp durations; and the don'ts for animating the hero, animating layout properties, and using `muted` for readable text. |
| `## Iteration Guide` | +2 steps | Motion through tokens only; every new component gets states and a focus treatment. |
| `## Known Gaps` | loose timing line -> 6 explicit entries | Separates what is prescribed (motion, focus ring, hover/loading/selected/error, modal and dropdown shadow levels) from what is extracted. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via `python3`, not estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #1f1f1f / `canvas` #ffffff | 16.48:1 | 4.5 | Pass |
| `ink` / `surface` #fafafa | 15.79:1 | 4.5 | Pass |
| `ink` / `cream` #fff8e0 | 15.51:1 | 4.5 | Pass |
| `charcoal` #2c2c2c / `canvas` | 13.97:1 | 4.5 | Pass |
| `ink-tint` #3d3d3d / `canvas` | 10.86:1 | 4.5 | Pass |
| `slate` #4a4a4a / `canvas` | 8.86:1 | 4.5 | Pass |
| `steel` #6a6a6a / `canvas` | 5.41:1 | 4.5 | Pass |
| `steel` / `surface` | 5.18:1 | 4.5 | Pass |
| `stone` #8a8a8a / `canvas` | 3.45:1 | 4.5 body | Fail as body text — scoped to 24px+ labels and control boundaries |
| `muted` #a8a8a8 / `canvas` | 2.38:1 | 4.5 | **Fail** — frozen; placeholder and disabled only |
| `muted` / `surface` | 2.28:1 | 4.5 | **Fail** — frozen; same scope |
| `on-dark` #ffffff / `surface-code` #1c1c1e | 17.01:1 | 4.5 | Pass |
| `on-dark-muted` #a8a8a8 / `surface-code` | 7.16:1 | 4.5 | Pass |
| `hairline-soft` #ededed / `surface` | 1.12:1 | 3.0 | **Fail** — frozen; decorative |
| `hairline-soft` / `canvas` | 1.17:1 | 3.0 | **Fail** — frozen; decorative |
| `hairline` #e5e5e5 / `surface` | 1.21:1 | 3.0 | **Fail** — frozen; decorative |
| `hairline` / `canvas` | 1.26:1 | 3.0 | **Fail** — frozen; decorative |
| `hairline-strong` #c7c7c7 / `surface` | 1.62:1 | 3.0 | **Fail** — frozen; card and panel edges |
| `hairline-strong` / `canvas` | 1.69:1 | 3.0 | **Fail** — frozen; card and panel edges |
| `stone` / `canvas` (as control boundary) | 3.45:1 | 3.0 | Pass |
| `stone` / `surface` (as control boundary) | 3.31:1 | 3.0 | Pass |
| `on-primary` #ffffff / `primary` #fa520f (`button-primary`, `badge-orange`, `sunset-stripe-band`) | 3.34:1 | 4.5 | **Fail** — frozen brand orange |
| `primary` / `canvas` (`button-link`, `footer-link`, `segmented-tab-active`) | 3.34:1 | 4.5 | **Fail** — frozen brand orange |
| `ink` / `primary` | 4.93:1 | 4.5 | Pass — the accessible label on the orange |
| `ink` / `sunshine-700` #ffa110 | 8.13:1 | 4.5 | Pass — the hero band's own pairing |
| `primary-deep` #cc3a05 / `canvas` | 5.03:1 | 4.5 | Pass — the accessible substitute for orange text |
| `focus` #8f2600 / `canvas` | 8.59:1 | 3.0 | Pass |
| `focus` / `surface` | 8.23:1 | 3.0 | Pass |
| `focus` / `surface-cream` #fff8e0 | 8.08:1 | 3.0 | Pass |
| `focus` / `surface-cream-soft` #fffaeb | 8.23:1 | 3.0 | Pass |
| `focus` / `cream-deeper` #fff0c2 | 7.56:1 | 3.0 | Pass |
| `focus` / `beige-deep` #e6d5a8 | 5.91:1 | 3.0 | Pass |
| `focus` / `yellow-saturated` #ffd900 | 6.21:1 | 3.0 | Pass |
| `focus` / `sunshine-700` | 4.24:1 | 3.0 | Pass |
| `focus` / `primary` | 2.57:1 | 3.0 | Fail — which is why `focus-on-dark` exists |
| `focus-on-dark` #fff8e0 / `primary` | 3.15:1 | 3.0 | Pass |
| `focus-on-dark` / `ink` | 15.51:1 | 3.0 | Pass |
| `focus-on-dark` / `surface-code` | 16.01:1 | 3.0 | Pass |
| `primary-deep` / `canvas` (`field-error-message`) | 5.03:1 | 4.5 | Pass |

Why two rings and not one, arithmetically: 3:1 against `canvas` caps a ring's
relative luminance at 0.300; 3:1 against `surface-code` (L 0.0117) demands at
least 0.135; but `primary` (L 0.2639) admits only a ring below 0.055 or above
0.892. No single value satisfies all three, so the file defines `focus` for
light and warm grounds and `focus-on-dark` for dark and saturated ones, with a
two-tone combination over the gradient bands and the hero photography.

### Motion inventory

Prescribed, not extracted. Crisp profile, values verbatim from SPEC section 5.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `background-color`, `opacity` | unchanged — no travel to remove |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` only, no scale | unchanged |
| Focus ring appears | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on the ring | ring appears with no fade |
| Page / route transition | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | `opacity` | `opacity` at `{motion.duration-reduced}` |
| Modal / drawer enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | `opacity` + `transform: translateY(8px → 0)` | `opacity` only, 100ms |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity` + `transform` | `opacity` only, 100ms |
| Dropdown / nav menu | enter 100ms, exit 60ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(-4px → 0)` | `opacity` only, 100ms |
| Toast | enter 150ms, exit 100ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px → 0)` | `opacity` only, 100ms |
| List / grid enter | 100ms per item, `{motion.stagger-step}` 20ms between | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px → 0)` | `opacity` only, no stagger, 100ms |
| List / grid exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` | `opacity` at 100ms |
| FAQ accordion disclosure | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity` + `transform` on panel content; `height` is **not** animated | `opacity` only, 100ms |
| Loading | 800ms, infinite | linear | `transform: rotate` | rotation stops; static progress label |

Exit is shorter than its matching entrance in every row. Only `transform` and
`opacity` are animated. The loading spinner is the one infinite animation; the
hero photography and the sunset stripe are explicitly static, which is the right
answer for a Crisp brand and also removes any ambience to freeze.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py:28-31` (`REQUIRED_COLOR_ROLES["text-dim"]`) | **Harness bug, per the no-alias rule.** This palette's secondary and tertiary ink are `slate` (#4a4a4a, 8.86:1) and `steel` (#6a6a6a, 5.41:1); both pass AA comfortably. Neither matches any `text-dim` pattern, so the role resolves to `muted` — the file's placeholder/disabled tone — and the harness then reports two secondary-text failures the document never commits. I did **not** add a `text-dim` alias; the role is plainly present under another name. | Add `^slate$`, `^steel$`, `^stone$`, `^grey-\d`, `^gray-\d` to the `text-dim` pattern list, and let `find_role_strongest` pick among them as it already does for `border`. |
| `theme-audit/audit.py:383` | `"disabled" in name` exempts a component by *name* only. A token scoped to disabled text in prose (`muted` here) still gets measured as live secondary text. | Also skip a token the Colors section marks disabled-or-placeholder-only, or accept the existing disclosure route (which is what this file now uses). |
| `theme-audit/audit.py:317-320` (`surface_keys`) | The regex misses real grounds a ring can land on when they are not named `surface`/`canvas`/`band`: `yellow-saturated`, `beige-deep` and `cream-deeper` are all surfaces in this file but none is checked for ring coverage. My ring clears 3:1 on all of them, but the harness would not have caught it if it did not. | Also treat a key bound as a `backgroundColor` in `components:` as a surface. |
| `theme-audit/audit.py:439` | `has_motion_section` is a plain `"## Motion & Animation" in text` substring test, so it would pass on a mention inside a sentence. | Anchor it, as `sections_present` already does with `^## `. |

### Needs approval

Six pairs fail AA and are left at their real values, because changing a brand
hex would make the document wrong. Each needs a product decision, not an edit.

1. **`#ffffff` on `#fa520f` — 3.34:1, needs 4.5:1.** Affects `button-primary`,
   `badge-orange` and any copy on `sunset-stripe-band`.
   - Nearest passing value, keeping the orange: swap the label to
     `{colors.ink}` #1f1f1f, which measures **4.93:1** on the same orange. No
     brand colour changes. This is the recommended route.
   - Keeping a white label instead requires darkening the fill to about
     **#c24000** (4.52:1 with #ffffff), which is no longer Mistral orange.
   - Usage note that would make the real value defensible: at
     `{typography.button-md}` (14px/500) the 4.5:1 threshold applies, so there
     is no size at which 3.34:1 is compliant. A 24px+ bold label would only need
     3:1, but no button in this system uses one.
2. **`#fa520f` on `#ffffff` — 3.34:1, needs 4.5:1.** Affects `button-link`,
   `footer-link` and `segmented-tab-active`.
   - Nearest passing value: `{colors.primary-deep}` #cc3a05, already in the
     palette, at **5.03:1**. Reserve #fa520f for fills and the stripe, and use
     #cc3a05 for orange *text*. Recommended.
   - Usage note for keeping #fa520f: it would be defensible only on 24px+ text
     (3:1 threshold), which rules out links at 14px and tab labels at 14px.
3. **Three hairline tones at 1.12–1.69:1, needing 3:1.** Left frozen and scoped
   to decoration. Approval needed only for the one place it mattered — control
   boundaries — where the file now uses `{colors.stone}` (3.45:1). If the brand
   insists on `{colors.hairline-strong}` on inputs, the nearest passing value is
   about **#949494** (3.03:1 on canvas, 2.91:1 on surface, so it still fails on
   `{colors.surface}`); #8a8a8a is the first value that clears both.
4. **`{colors.muted}` at 2.38:1.** No change requested: WCAG sets no contrast
   requirement on disabled text, and placeholders are never the only label in
   this system. Approval is only needed if `muted` is ever used for live
   secondary prose — in which case `{colors.steel}` (5.41:1) is the value.
5. **Prescribed focus tokens.** `focus` #8f2600 and `focus-on-dark` #fff8e0 are
   added by this audit; the brand ships no visible ring. Needs design sign-off
   that the deep sunset red reads as Mistral rather than as a generic alert red.
6. **Prescribed interaction states.** Hover, focus-visible, loading, selected
   and error treatments on 40 components are inferred from the palette, not
   observed. The specific choices (hover on `{colors.sunshine-800}`, error on
   `{colors.primary-deep}`) need confirming against whatever the product UI
   actually does.

### Identity verdict

Still unmistakably Mistral, and the additions lean on the brand rather than
dilute it. Every value added comes from the sunset gradient or the existing
neutral ladder: the focus ring is the deep red end of the stripe, the dark-ground
ring is the brand cream, the error colour is `primary-deep`, and the control
boundary is the already-extracted `stone`. Nothing generic was introduced — there
is no new blue focus ring, no borrowed semantic red, no invented grey.

The prose keeps the things only this file says: the sunset stripe as the brand
recognizer, PP Editorial Old against Inter, the explicit refusal of pill buttons,
the 8px/12px radius pairing. The Motion section is where drift was most likely,
so it is written against those facts: the hero photography and the stripe are
declared **static**, which is an identity claim, not a default, and it is the
opposite of what a Cinematic reading of "atmospheric mountain-sunset hero" would
produce.

**Crisp is the right profile, and I kept it**, though it is the closest call in
this file. The case against: the Overview calls the brand
"almost cinematographic", the display face is a 400-weight near-serif at 84px,
and the hero is full-bleed photography — SPEC rule 1's tells for Cinematic.
The case for Crisp, which wins: rule 1 scopes Cinematic to luxury, automotive,
hardware-flagship, console or aerospace identity, and Mistral is none of those.
Its product surface is a developer tool — Le Studio, `code-block`,
`code-block-header`, JetBrains Mono, IDE mockups, a coding solutions page — which
is rule 2's explicit trigger. The photography is a marketing-page backdrop, not
the thing the user operates. A slow reveal on an orange CTA in a model playground
would be wrong. Rule 3 does not fire either: the saturated colour sits on CTAs
but the type voice is editorial and sober, not light and informal. So Crisp by
rule 2, with the slow-reveal temptation handled by naming the hero static.
