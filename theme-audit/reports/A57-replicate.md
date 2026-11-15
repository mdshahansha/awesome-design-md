## A57 · replicate

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

Harness command: `python3 -I theme-audit/audit.py --site replicate --json`.
Profile: **Crisp**, as rostered. Kept — see Identity verdict.

Harness claims checked against the file itself:
- "Missing colour roles: focus, text-dim" — **half stale**. `focus` was genuinely
  missing by the harness's own patterns. `text-dim` was already satisfied: the
  run resolved `text-dim -> mute` before my edits. The brief's pre-measured list
  is out of date relative to the current `audit.py`.
- "Missing sections: Motion & Animation, Accessibility" — confirmed.
- "States never named anywhere: hover, focus-visible, disabled, loading,
  selected, error" — confirmed; only `active` and `pressed` were present, from
  the `button-primary-pressed` line.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A/G Focus | `{colors.ring-focus}` | The shipped ring `rgba(59,130,246,0.5)` clears 3:1 on **none** of the six surfaces this file defines: 1.80:1 on `{colors.canvas}`, 1.85:1 on `{colors.surface-card}`, 1.76:1 on `{colors.surface-bone}`, 2.07:1 on `{colors.surface-dark}`, 2.10:1 on `{colors.surface-deep}`, 1.26:1 over the orange `{component.hero-band}`. Keyboard focus is effectively unindicated across the whole system. |
| P0 | A Token contract | `colors:` | No key matching the `focus*` pattern, so neither the file nor the harness could speak about a ring at all. |
| P0 | C/F Sections | document | `## Motion & Animation` absent. No duration, easing or stagger anywhere in the file (`durations_found: []`, `easings_found: 0`). |
| P0 | G Sections | document | `## Accessibility` absent, so four real AA failures sat undisclosed. |
| P0 | F Motion | frontmatter | No `motion:` group; all three minimum keys missing. |
| P0 | H States | 19 component entries | `hover`, `focus-visible`, `disabled`, `loading`, `selected`, `error` documented nowhere. Every control was default-only, including `{component.text-input}`, which has no documented error state at all. |
| P0 | B Colour | `{colors.hairline}` | Composites to 1.27:1 on `{colors.canvas}` and 1.26:1 on `{colors.surface-bone}` while being the *only* boundary of `{component.text-input}`, `{component.button-icon}` and `{component.badge-tag}` — a WCAG 1.4.11 failure, previously unstated. |
| P1 | B Colour | `{component.button-primary}` | `#ffffff` on `#ea2804` = 4.37:1 against 4.5:1. Brand identity hex; left alone, now disclosed. See Needs approval. |
| P1 | B Colour | `{component.badge-status}` | `#fcfcfc` on `#2b9a66` = 3.46:1 against 4.5:1. Set in `{typography.caption}` 12px/400, so the large-text 3:1 allowance does not apply. See Needs approval. |
| P1 | B Colour | `{colors.link}` | `#ea2804` as inline link text on `{colors.canvas}` = 4.09:1. The file told implementers to pull links into the brand orange and never mentioned that this fails AA, nor required an underline. |
| P1 | B Colour | `{colors.divider-dark}` | Composites to 1.93:1 on `{colors.surface-dark}` and 1.66:1 on `{colors.surface-deep}`. Footer and code-band structure rests on it. |
| P1 | A Token contract | `shadow:` | Elevation level 4 wrote a literal `0 8px 24px rgba(32,32,32,0.08)` in prose with no token. SPEC §1 requires a `shadow:` group exactly where a file documents a real shadow value. |
| P1 | B Colour | `{colors.ash}`, `{colors.stone}` | 3.10:1 and 1.79:1 on `{colors.canvas}`. Neither had a stated usage scope, so nothing stopped `ash` being used as body copy. |
| P1 | C Elevation | cream layers | `{colors.canvas}` to `{colors.surface-bone}` = 1.06:1 and to `{colors.surface-card}` = 1.07:1. Combined with "Don't add drop shadows on cream surfaces", some card boundaries had no measurable edge at all. `{colors.surface-dark}` to `{colors.surface-deep}` = 1.29:1. Never stated. |
| P1 | G Accessibility | tap targets | `{component.button-icon}` 36px desktop, `{component.sub-nav-pill}` 36px, `{component.contributor-avatar}` 40px — all under 44px, while Responsive Behavior claimed the system "comfortably clear[s] WCAG AAA". That claim was true only of the 44px buttons. |
| P2 | D Typography | `{typography.heading-lg}` | `lineHeight: 0.83` at 38.4px sits outside the file's own ladder (every other role is 1.0 or 1.2–1.56) and will clip descenders in most substitute families. Extracted, so not changed; flagged. |
| P2 | E Shapes | `{rounded.sm}` 6px | Bound by no component; it exists only as "mid-radius callouts" in prose. An unused rung between `{rounded.xs}` 4px and `{rounded.md}` 10px. Left in place — removing an extracted value is worse than an idle rung. |
| P2 | I Known Gaps | Known Gaps | Did not record that interaction states were unextracted, so a reader could not tell documented-and-absent from never-looked-at. |

Elevation consistency (dimension C) is otherwise sound: levels 0–3 use no shadow
and level 4 is the only shadow in the system, so the language is colour-blocking
throughout rather than shadow and border mixed at random. Typography (D) was
already complete — all 17 roles carry family, size, weight, line height and
letter spacing, and body type passes on every surface the file defines
(`{colors.ink}` on `{colors.surface-card}` 16.29:1). Spacing and radius ladders
(E) are internally consistent; the only value outside its own scale is the 38.4px
type size and the 0.83 line height noted above. Reference integrity (A) was
already at zero dangling refs and still is.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| `colors:` | — -> `focus: "#202020"` | Binds the focus role. Reuses the tone the palette already owns as `{colors.ink}` / `{colors.hairline-strong}`; not a new brand colour, per SPEC §1's focus exception. 15.23:1 on `{colors.canvas}`. |
| `colors:` | — -> `focus-on-dark: "#fcfcfc"` | This file documents both cream and near-black signature surfaces plus an orange hero band, so one ring cannot serve them. Reuses `{colors.on-dark}`. 15.88:1 / 20.47:1 on the dark surfaces. |
| `colors:` | `ring-focus` kept verbatim | Extracted fact, frozen. Retained and measured rather than deleted or re-valued. |
| frontmatter | — -> `shadow:` group with `soft-drop` | SPEC §1: a shadow group is required where the file documents real shadow values. Value taken verbatim from the Elevation table, nothing invented. |
| frontmatter | — -> `motion:` group | The **Crisp** block from SPEC §5, copied verbatim, no deviations. |
| `## Colors` → Surface | `hairline` one-line description -> description + measured 1.27:1 / 1.26:1 + scoped to decoration, pointing boundary work at `{colors.hairline-strong}` | Frozen tone scoped in prose rather than altered; the file already owns a passing boundary tone, so no parallel token was added. |
| `## Colors` → Semantic | one `Focus Ring` bullet -> three bullets (extracted ring with its failing ratios, plus the two role bindings and what tone each reuses) | States which existing tone each ring reuses, as SPEC §1 requires. |
| `## Elevation & Depth` | level-4 literal hex-shadow -> `{shadow.soft-drop}`; added a paragraph with the measured layer separations (1.06:1, 1.07:1, 15.23:1, 1.29:1) | Makes the shadow addressable and states plainly that the cream layers separate by warmth, not brightness. |
| `## Components` | 19 entries, default-only -> every entry carries a `States —` line | Dimension H. Default, `button-primary-pressed` and the `{component.code-tab}` active treatment are labelled extracted; everything else is labelled prescribed. Entries that genuinely have one or two states say so: `{component.badge-status}`, `{component.code-block}`, `{component.hero-band}`, `{component.pricing-tier-featured}`, `{component.collection-tile}`. |
| `## Components` → `{component.text-input}` | "Focus state adds a `{colors.ring-focus}` 3px ring" -> same, plus the note that it clears 3:1 on no surface, plus a full state list including `error` | The input was the only form control in the file and had no error state. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. Table covers hover, press, focus, page transition, modal/drawer, dropdown, toast, list enter, list exit, loading. Transform and opacity only; every exit shorter than its entrance. |
| `## Motion & Animation` | — -> `@media (prefers-reduced-motion: reduce)` block | Names what is removed (all travel, all scale, the stagger cascade, spinner rotation, skeleton pulse) and what remains (opacity fades at `{motion.duration-reduced}` = 100ms, instant colour changes, the untransitioned ring). |
| after Motion | — -> `## Accessibility` | Measured contrast for the key pairs, the four failures with ratios, ring visibility per surface, tap targets, reduced motion, non-colour cues. |
| `## Do's and Don'ts` | — -> 2 Do's, 3 Don'ts | Ring selection by ground; Crisp timing; no entrance choreography; no reliance on `{colors.hairline}` as a control edge; no animating layout properties. |
| `## Known Gaps` | 4 entries -> 11 | Records that motion and most states are prescribed, that the two rings are role bindings reusing owned tones, that the hairline re-binding is deliberately left as extracted, and that tap targets are quoted not measured. |

Not touched, deliberately: every typography value, every spacing and radius
value, every brand hex, and the existing `components:` bindings — including the
three that bind the failing `{colors.hairline}`. Nothing was reflowed.

### Contrast checks

All computed with WCAG 2.1 relative luminance via `python3` standard library;
`rgba()` values composited over the stated ground first.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #202020 / `canvas` #f9f7f3 | 15.23:1 | 4.5:1 | Pass |
| `ink` / `surface-bone` #f3f0e8 | 14.31:1 | 4.5:1 | Pass |
| `ink` / `surface-card` #ffffff | 16.29:1 | 4.5:1 | Pass |
| `body` #3a3a3a / `canvas` | 10.63:1 | 4.5:1 | Pass |
| `charcoal` #575757 / `canvas` | 6.75:1 | 4.5:1 | Pass |
| `mute` #646464 / `canvas` (text-dim representative) | 5.53:1 | 4.5:1 | Pass |
| `mute` / `surface-bone` | 5.20:1 | 4.5:1 | Pass |
| `ash` #8d8d8d / `canvas` | 3.10:1 | 4.5:1 | **Fail** — placeholder/tertiary only; scoped in file |
| `stone` #bbbbbb / `canvas` | 1.79:1 | n/a | Exempt (disabled foreground) |
| `on-dark` #fcfcfc / `surface-dark` #202020 | 15.88:1 | 4.5:1 | Pass |
| `on-dark` / `surface-deep` #000000 | 20.47:1 | 4.5:1 | Pass |
| `on-dark-mute` -> #bebebe / `surface-dark` | 8.77:1 | 4.5:1 | Pass |
| `on-dark-mute` -> #b5b5b5 / `surface-deep` | 10.24:1 | 4.5:1 | Pass |
| `on-primary` #ffffff / `primary` #ea2804 | 4.37:1 | 4.5:1 | **Fail** — brand hex, disclosed |
| `on-primary` / `primary-deep` #c01f00 | 6.11:1 | 4.5:1 | Pass |
| `primary-deep` / `canvas` | 5.71:1 | 4.5:1 | Pass |
| `link` #ea2804 / `canvas` | 4.09:1 | 4.5:1 | **Fail** — brand hex, disclosed |
| `on-dark` / `badge-success` #2b9a66 | 3.46:1 | 4.5:1 | **Fail** — 12px caption, disclosed |
| `badge-success` / `canvas` (as text) | 3.32:1 | 4.5:1 | Fail — never used as text; fill only |
| `ink` / `badge-success` | 4.59:1 | 4.5:1 | Pass — the zero-hex-change fix for the badge |
| `on-dark` / `github-dark` #24292e | 14.30:1 | 4.5:1 | Pass |
| `hairline-strong` #202020 / `canvas` (border role) | 15.23:1 | 3.0:1 | Pass |
| `hairline` -> #dfddda / `canvas` | 1.27:1 | 3.0:1 | **Fail** — extracted, scoped to decoration, disclosed |
| `hairline` -> #dad7d0 / `surface-bone` | 1.26:1 | 3.0:1 | **Fail** — same, disclosed |
| `hairline` -> #e4e4e4 / `surface-card` | 1.27:1 | 3.0:1 | **Fail** — same, disclosed |
| `divider-dark` -> #4d4d4d / `surface-dark` | 1.93:1 | 3.0:1 | **Fail** — decoration, disclosed |
| `divider-dark` -> #333333 / `surface-deep` | 1.66:1 | 3.0:1 | **Fail** — decoration, disclosed |
| `focus` #202020 / `canvas` | 15.23:1 | 3.0:1 | Pass |
| `focus` / `surface-bone` | 14.31:1 | 3.0:1 | Pass |
| `focus` / `surface-card` | 16.29:1 | 3.0:1 | Pass |
| `focus` / `hero-warm` #ea2804 | 3.73:1 | 3.0:1 | Pass |
| `focus-on-dark` #fcfcfc / `surface-dark` | 15.88:1 | 3.0:1 | Pass |
| `focus-on-dark` / `surface-deep` | 20.47:1 | 3.0:1 | Pass |
| `focus-on-dark` / `hero-warm` | 4.26:1 | 3.0:1 | Pass |
| `ring-focus` -> #9abcf4 / `canvas` | 1.80:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `ring-focus` -> #97b9ef / `surface-bone` | 1.76:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `ring-focus` -> #9dc0fa / `surface-card` | 1.85:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `ring-focus` -> #2e518b / `surface-dark` | 2.07:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `ring-focus` -> #1e417b / `surface-deep` | 2.10:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `ring-focus` -> #92557d / `hero-warm` | 1.26:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `ink` / `hero-glow` #ff6a3d | 5.73:1 | 4.5:1 | Pass |
| `ink` / `hero-pink` #f4a8a0 | 8.50:1 | 4.5:1 | Pass |
| `on-dark` / `hero-glow` | 2.77:1 | 4.5:1 | Fail — gradient mid-stop; type sits on the `primary` core, not here |

Layer separation (not a WCAG threshold; reported for dimension C):
`canvas`/`surface-bone` 1.06:1 · `canvas`/`surface-card` 1.07:1 ·
`surface-bone`/`surface-card` 1.14:1 · `canvas`/`surface-dark` 15.23:1 ·
`surface-dark`/`surface-deep` 1.29:1.

### Motion inventory

Prescribed from the **Crisp** profile; nothing extracted.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity`, plus colour change | Colour applies at once; no opacity ramp |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `transform: scale(0.98)`; 0.94 on `{component.button-icon}` | Scale removed; `{colors.primary-deep}` fill carries the feedback |
| Focus-visible ring | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on the ring | No transition; ring is full-size the moment it exists |
| Page / route transition | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity` on the content region | Cross-fade at 100ms, no travel |
| Modal / drawer | enter 150ms / exit 100ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px -> 0)` | Travel removed; opacity only at 100ms |
| Dropdown | enter 100ms / exit 60ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(4px -> 0)` | Travel removed; opacity only at 100ms |
| Toast | enter 100ms / exit 60ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(6px -> 0)` | Travel removed; opacity only at 100ms; dismiss timer unchanged |
| List enter | 100ms per item, `{motion.stagger-step}` 20ms between, capped at 8 | `{motion.ease-enter}` | `opacity` 0 -> 1 | Stagger and fade removed; grid present on first paint |
| List exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` 1 -> 0 | Removed without a fade |
| Loading | 800ms/rotation, infinite while pending | linear | `transform: rotate()`; skeleton `opacity` 0.6 -> 1 -> 0.6 | Spinner becomes a static glyph; skeleton holds one flat `{colors.surface-bone}` fill |

Rule compliance: transform and opacity only; every exit shorter than its
entrance; nothing animates on first paint; the only infinite animations are the
loader and the skeleton pulse, both frozen under reduced motion; the hero mesh is
a static gradient and is explicitly **not** animated ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 37 | `"focus": [r"^focus$", r"^focus-ring$", r"^focus-", r"^ring$"]` does not match `ring-focus`, which is the name this file (and plausibly others) actually uses. The harness reported the focus role missing while the palette plainly contained a ring. This is the harness-bug case SPEC §1 describes, not a missing token — reporting it here rather than treating the regex as the authority. | Add `r"^ring[-_]focus$"` and `r"^ring[-_]"` to the pattern list. Worth a repo-wide re-run: any file naming its ring `ring-*` is being scored as role-missing. |
| `theme-audit/audit.py` line 37 (same list) | Separately: in this file the fix would not have made the role *pass* anything, because `ring-focus` is an `rgba()` at 0.5 alpha that clears 3:1 on no surface. So the regex bug and the real defect coincided here — which is exactly why the regex should be fixed, so the next file's genuine ring is not mistaken for a missing one. | As above. |
| `theme-audit/audit.py` ~line 465 (`CONTAINER` regex) | `tier` and `block` are absent, so `pricing-tier-featured` and `code-block` do not contribute their grounds to the focus-coverage surface list. Harmless in this file (both grounds are already `surface-*` keys) but it would hide a dark ground in a file that only names it on the component. | Add `tier|block` to the `CONTAINER` alternation. |
| `theme-audit/audit.py` | SPEC §1 requires a `shadow:` group wherever prose states a real shadow value, but nothing in `audit.py` checks for it, so the requirement is invisible to the score. I added the group because SPEC asks for it, not because the harness did. | Add a check: if the body matches a shadow literal (`\d+px\s+\d+px[^;\n]*rgba`) and no `shadow:` group exists, report it. |
| `theme-audit/briefs/A57-replicate.md` line 12 | Pre-measured list says `text-dim` is missing. The current `audit.py` resolves `text-dim -> mute`. The briefs were generated against an older harness. | Regenerate the briefs from the current `audit.py`, or state in the brief which harness revision produced the numbers. |
| `design-md/replicate/DESIGN.md` → Responsive Behavior (my own file, left as-is) | "comfortably clearing WCAG AAA" is true of the 44px buttons only, not of `button-icon` 36px, `sub-nav-pill` 36px or `contributor-avatar` 40px. I corrected this in `## Accessibility` rather than rewriting the Responsive Behavior claim, to keep the diff reviewable and because tap-target size is not measurable from a document. Flagging the wording as a remaining inconsistency inside my own file. | Soften the Responsive Behavior line to "clearing the 44px AAA target on the primary button row". |

### Needs approval

Every item here is a change to an extracted brand value or an extracted binding.
None was applied.

1. **`{colors.primary}` `#ea2804` with `{colors.on-primary}` `#ffffff` — 4.37:1,
   needs 4.5:1.** Nearest passing value: **`#e52704`** (4.54:1), a 2% luminance
   step that is visually indistinguishable but is still a falsified brand hex.
   *Preferred alternative, no hex change:* the 3:1 threshold applies at 24px+,
   or 18.66px+ at weight 700. The CTA label is `{typography.button-md}`
   16px/600, so AA genuinely applies and the brand genuinely fails it by 0.13.
   The defensible usage note is therefore: "white on Replicate orange is
   compliant only where the label is set at `{typography.heading-md}` 24px or
   larger; at the documented 16px button size it is a known 4.37:1 failure."
   Third option: keep `#ea2804` as the fill and set the label in
   `{colors.ink}` — but that abandons the white-on-orange CTA, which is the
   brand's single loudest gesture.
2. **`{colors.badge-success}` `#2b9a66` with `{colors.on-dark}` `#fcfcfc` —
   3.46:1 at 12px, needs 4.5:1.** Nearest passing green: **`#258458`**
   (4.53:1). *Better option, no hex change:* set the badge label to
   `{colors.ink}` `#202020`, which measures **4.59:1** on the extracted green
   and passes without touching a brand value. Needs approval only because it
   changes the pill from white-on-green to ink-on-green.
3. **Re-binding the three `{colors.hairline}` boundaries.**
   `{component.text-input}`, `{component.button-icon}` and
   `{component.badge-tag}` are drawn with a 1.27:1 edge on the live site. Per
   the settled rule the extracted bindings are left exactly as they are, and
   `{colors.hairline-strong}` is recommended in prose instead. Approving the
   re-binding would fix a real 1.4.11 failure; a gentler middle option is a
   prescribed `#8a8a8a` (3.23:1 / 3.03:1 / 3.45:1 on canvas / bone / card),
   which I did **not** add as a token because the palette already owns a passing
   boundary tone and SPEC §1 forbids adding one in that case.
4. **`{colors.link}` `#ea2804` on `{colors.canvas}` — 4.09:1.** Recommend
   `{colors.primary-deep}` `#c01f00` (**5.71:1**) for link *text*, keeping
   `#ea2804` for the CTA fill. Needs approval because it visibly changes the
   link colour. Interim mitigation already written into the file: links carry a
   permanent underline, so colour is never the only cue.
5. **Replacing the shipped focus ring.** `{colors.focus}` and
   `{colors.focus-on-dark}` reuse tones the palette owns and are measured in
   `## Accessibility`, but adopting them means the product stops drawing the
   blue `{colors.ring-focus}` it currently draws. That is a real visual change,
   even though the current ring is unusable at 1.26–2.10:1.
6. **`{colors.divider-dark}` alpha.** At `0.2` it measures 1.93:1 on
   `{colors.surface-dark}` and 1.66:1 on `{colors.surface-deep}`. Raising it to
   `0.35` would give 3.20:1 and 3.00:1. Only needed if a dark-surface divider is
   ever load-bearing rather than decorative; left at the extracted value.

### Identity verdict

**Still unmistakably Replicate, and the Crisp profile is right.**

The three signals that make this file specific — cream over white, one orange
used as a stamp, and 128px display type at `lineHeight: 1.0` — are untouched. No
hex, type value, spacing step or radius changed. The two tokens added to
`colors:` are the brand's own ink and its own off-white under a second name,
which is deliberate: a brand whose stated rule is "don't introduce a secondary
brand colour" would be contradicted by a chromatic focus ring, so the ring is
achromatic and the rule survives. The states I prescribed are built from tones
already in the palette (`{colors.surface-bone}` for hover, `{colors.stone}` for
disabled, `{colors.surface-dark}` for selected, `{colors.primary}` for error),
and the selected state reuses the dark-inversion gesture the pricing grid
already uses, so "chosen" reads one way across the system rather than arriving
as a borrowed convention.

On the profile: SPEC §5 rule 2 (developer-tool identity → Crisp) fires cleanly.
Replicate is ML infrastructure with monospace code wells, an API-tab strip and a
"how it works" walkthrough — a tool where a model either ran or did not. The one
argument for **Calm** is the file's own editorial self-description ("art zine",
"print magazine", full-bleed photography, generous 96/160px bands), and rule 1's
Cinematic tell is explicitly full-bleed photography with sparse type and slow
reveals, which the hero band half-matches. I kept Crisp: the editorial quality
here is *static* composition, not motion — the file documents no reveal, no
parallax, no scroll choreography, and its interaction surface is a model grid, a
search field and a code-tab switcher. Rule 2 is a conjunction on identity, and
the identity is a developer tool wearing a zine's clothes. Crisp timing also
makes the restraint legible: a 20ms stagger capped at 8 items is the motion
equivalent of "one orange element per viewport".

The place the SPEC left me guessing: §1 says never to add an alias purely to
satisfy a role pattern and to report an apparently unsatisfied role as a harness
bug, while also carving out focus as the one role you may bind explicitly — and
this file hit both at once, since `ring-focus` was a real ring the regex could
not see *and* a ring that fails 3:1 on every surface, so I did both (added the
binding, reported the regex).
