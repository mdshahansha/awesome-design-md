## A20 · elevenlabs

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A. Token contract | `colors.focus` | No focus ring token anywhere in the file. Nothing told a builder how to indicate keyboard focus, on either the off-white canvas or the near-black band. Confirmed. |
| P0 | F. Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule, zero durations and zero easings. Confirmed. |
| P0 | G. Accessibility | whole file | No `## Accessibility` section. Six contrast failures present and undisclosed. Confirmed. |
| P0 | B. Colour | `hairline-control` (absent) | `text-input` and `button-outline` both declared their boundary as 1px `{colors.hairline-strong}`, which measures 1.37:1 on the canvas and 1.49:1 on the white field. The only boundary of a text input was effectively invisible. Confirmed. |
| P0 | H. States | all 20 component entries | Only `active` was documented, and only because `button-primary-active` exists as a separate component. hover, focus-visible, pressed, disabled, loading, selected and error were named nowhere. Confirmed. |
| P1 | B. Colour | `colors.muted` | 4.43:1 on `{colors.canvas}` — misses AA by 0.07. Prose called it "Sub-titles" with no size qualifier. Confirmed. |
| P1 | B. Colour | `colors.muted-soft` | 2.31:1 on canvas, 2.52:1 on white. Prose called it "Disabled text", which is exempt, but nothing said it must not be used for live text. Confirmed. |
| P1 | B. Colour | `colors.semantic-success` | 3.02:1 on canvas — not flagged by the harness, found by hand. Fails AA for text under 24px. |
| P1 | B. Colour | `colors.semantic-error` | 4.43:1 on canvas (4.83:1 on white) — marginal fail, found by hand. |
| P1 | C. Elevation | Elevation & Depth table | The soft drop was a bare `rgba(...)` with no token, so it could not be referenced. Added a `shadow:` group per SPEC section 1. |
| P1 | C. Elevation | layer luminance | canvas→surface-card 1.09:1, canvas→canvas-soft 1.04:1, canvas→surface-strong 1.05:1, surface-dark→surface-dark-elevated 1.13:1. The layers are **not** distinguishable by fill. The file never said so, which made the 1px border look optional. |
| P2 | E. Ladders | `rounded.pill` / `rounded.full` | Two keys with the identical value 9999px. Left alone: different intent (CTA geometry vs circular avatar), both referenced. Not a defect. |
| P2 | A. Token contract | `rounded.none` | Documented as "Reserved" and referenced only inside a Don't. Harmless; left alone. |
| P2 | Stale prose | Iteration Guide item 5 | Said "Hover state never documented." Made false by this edit; corrected. |
| P2 | Stale prose | Known Gaps | Said animation timings were "out of scope"; they now exist and must be labelled prescribed. Corrected. |
| P2 | G. Accessibility | Responsive → Touch Targets | Claimed "at WCAG AA, padded for AAA" for a 40px pill. WCAG has no AAA tap-target criterion at that figure, and tap-target size is not computable from a document. Rewritten as a declared-value claim with the limit stated. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `muted-strong: "#757068"` | Prescribed parallel accessible tone for `{colors.muted}`, which misses AA at 4.43:1. 4.51:1 on canvas. The extracted `muted` is untouched. |
| frontmatter `colors:` | — -> `hairline-control: "#8a8580"` | Prescribed parallel accessible boundary, 3.35:1 on canvas / 3.65:1 on white. All three extracted hairlines are under 1.5:1 and cannot bound a control. |
| frontmatter `colors:` | — -> `focus: "#78716c"` | The missing role. One mid-luminance warm stone, chosen so a single token clears 3:1 on all six surfaces this file defines rather than needing a `focus-on-dark` pair. |
| frontmatter | — -> `shadow:` group (`none`, `card-hover`) | The file stated a real `rgba(...)` elevation with no token to reference — exactly the case SPEC section 1 calls out. |
| frontmatter | — -> `motion:` group | Cinematic profile block, verbatim from SPEC section 4 including `duration-reduced: 150ms`, so this file stays comparable with its siblings. |
| Colors → Text | `muted`: "Sub-titles." -> plus measured 4.43:1 and an 18px+ scope | A frozen near-miss has to be stated, not silently carried. |
| Colors → Text | `muted-soft`: "Disabled text." -> plus 2.31:1, scoped to disabled text and to dark bands (7.83:1) | The one legitimate use is the dark band; that had to be written down. |
| Colors → Text | — -> `muted-strong` entry | Documents the prescribed stand-in and labels it prescribed. |
| Colors → Hairlines | — -> `hairline-control` entry; extracted hairlines scoped to decoration | SPEC section 2's parallel-token pattern. |
| Colors | — -> new `### Focus` subsection | States why the ring is neutral rather than chromatic for a brand whose first rule is that it has no accent, with the measured ratio on every surface. |
| Elevation & Depth | prose -> plus "expressed one way" paragraph and the four measured layer ratios | Dimension C. Elevation is border-always, shadow-as-hover-increment; nothing mixes. |
| Elevation & Depth table | bare `0 4px 16px rgba(...)` -> `{shadow.card-hover}`; new "Control border" row | Makes the shadow referenceable and puts the accessible boundary in the elevation ladder. |
| Components | — -> `### Interaction States` table, 20 rows | Dimension H. Every entry names its states; `button-primary-active`, `testimonial-card`, `voice-icon-circular`, `hero-band`, `cta-band`, `footer` and `badge-pill` say plainly that they have one or two. |
| Components → `text-input` | 1px `{colors.hairline-strong}` -> 1px `{colors.hairline-control}`, focus adds the ring outside the 2px ink border | A 2px border alone is a border change, not a focus indicator. |
| Components → `button-outline` | 1px `{colors.hairline-strong}` -> 1px `{colors.hairline-control}` | Same reason. Prose also called it an "ink border" while pointing at a grey token — fixed. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. Token table, 12-row interaction table, rules, reduced-motion block. |
| after Motion | — -> `## Accessibility` | 17-row measured contrast table, per-surface focus-ring table, tap targets, reduced motion, and an explicit statement of what a document cannot measure. |
| Do's and Don'ts | — -> 2 Do's, 3 Don'ts | Boundary token, slow entrances, no brand-coloured ring, transform/opacity only, no `muted-soft` as live text. |
| Iteration Guide item 5 | "Hover state never documented." -> points at the state table | Was made false by this edit. |
| Responsive → Touch Targets | AAA claim -> declared-value figures plus "not measured here" | The old claim was both wrong and not computable from a document. |
| Known Gaps | 1 animation line -> 3 lines | Labels motion, the three new tokens and the semantic hexes as prescribed or unverified. |

### Contrast checks

All computed with WCAG 2.1 relative luminance, `python3` standard library only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #0c0a09 / `canvas` #f5f5f5 | 18.12:1 | 4.5:1 | Pass |
| `ink` #0c0a09 / `surface-card` #ffffff | 19.76:1 | 4.5:1 | Pass |
| `ink` #0c0a09 / `canvas-soft` #fafafa | 18.93:1 | 4.5:1 | Pass |
| `ink` #0c0a09 / `surface-strong` #f0efed | 17.19:1 | 4.5:1 | Pass |
| `body` #4e4e4e / `canvas` #f5f5f5 | 7.63:1 | 4.5:1 | Pass |
| `body` #4e4e4e / `surface-card` #ffffff | 8.32:1 | 4.5:1 | Pass |
| `muted` #777169 / `canvas` #f5f5f5 | 4.43:1 | 4.5:1 | **Fail** (frozen, disclosed) |
| `muted` #777169 / `canvas-soft` #fafafa | 4.62:1 | 4.5:1 | Pass |
| `muted` #777169 / `surface-card` #ffffff | 4.83:1 | 4.5:1 | Pass |
| `muted-soft` #a8a29e / `canvas` #f5f5f5 | 2.31:1 | 4.5:1 | **Fail** (frozen, disclosed) |
| `muted-soft` #a8a29e / `surface-card` #ffffff | 2.52:1 | 4.5:1 | **Fail** (frozen, disclosed) |
| `muted-strong` #757068 / `canvas` #f5f5f5 | 4.51:1 | 4.5:1 | Pass (prescribed) |
| `muted-strong` #757068 / `surface-card` #ffffff | 4.91:1 | 4.5:1 | Pass (prescribed) |
| `muted-strong` #757068 / `surface-strong` #f0efed | 4.28:1 | 4.5:1 | Fail — on badge plates use `{colors.ink}` |
| `hairline-soft` #f0efed / `canvas` #f5f5f5 | 1.05:1 | 3.0:1 | **Fail** (frozen, disclosed, decoration only) |
| `hairline` #e7e5e4 / `canvas` #f5f5f5 | 1.15:1 | 3.0:1 | **Fail** (frozen, disclosed, decoration only) |
| `hairline-strong` #d6d3d1 / `canvas` #f5f5f5 | 1.37:1 | 3.0:1 | **Fail** (frozen, disclosed, decoration only) |
| `hairline-strong` #d6d3d1 / `surface-card` #ffffff | 1.49:1 | 3.0:1 | **Fail** (frozen, disclosed) |
| `hairline-control` #8a8580 / `canvas` #f5f5f5 | 3.35:1 | 3.0:1 | Pass (prescribed) |
| `hairline-control` #8a8580 / `surface-card` #ffffff | 3.65:1 | 3.0:1 | Pass (prescribed) |
| `hairline-control` #8a8580 / `surface-strong` #f0efed | 3.18:1 | 3.0:1 | Pass (prescribed) |
| `on-primary` #ffffff / `primary` #292524 | 15.17:1 | 4.5:1 | Pass |
| `on-primary` #ffffff / `primary-active` #0c0a09 | 19.76:1 | 4.5:1 | Pass |
| `on-dark` #ffffff / `surface-dark` #0c0a09 | 19.76:1 | 4.5:1 | Pass |
| `on-dark-soft` #a8a29e / `surface-dark` #0c0a09 | 7.83:1 | 4.5:1 | Pass |
| `on-dark-soft` #a8a29e / `surface-dark-elevated` #1c1917 | 6.93:1 | 4.5:1 | Pass |
| `semantic-error` #dc2626 / `canvas` #f5f5f5 | 4.43:1 | 4.5:1 | **Fail** (marginal, disclosed) |
| `semantic-error` #dc2626 / `surface-card` #ffffff | 4.83:1 | 4.5:1 | Pass |
| `semantic-success` #16a34a / `canvas` #f5f5f5 | 3.02:1 | 4.5:1 | **Fail** (disclosed; icon / 24px+ only) |
| `semantic-success` #16a34a / `surface-card` #ffffff | 3.30:1 | 4.5:1 | **Fail** (disclosed; icon / 24px+ only) |
| `focus` #78716c / `canvas` #f5f5f5 | 4.40:1 | 3.0:1 | Pass |
| `focus` #78716c / `canvas-soft` #fafafa | 4.60:1 | 3.0:1 | Pass |
| `focus` #78716c / `surface-card` #ffffff | 4.80:1 | 3.0:1 | Pass |
| `focus` #78716c / `surface-strong` #f0efed | 4.17:1 | 3.0:1 | Pass |
| `focus` #78716c / `surface-dark` #0c0a09 | 4.12:1 | 3.0:1 | Pass |
| `focus` #78716c / `surface-dark-elevated` #1c1917 | 3.65:1 | 3.0:1 | Pass |
| `focus` #78716c / `gradient-mint` #a7e5d3 | 3.38:1 | 3.0:1 | Pass |
| `focus` #78716c / `gradient-peach` #f4c5a8 | 3.06:1 | 3.0:1 | Pass |
| `focus` #78716c / `gradient-sky` #a8c8e8 | 2.76:1 | 3.0:1 | **Fail** — two-tone ring required |
| `focus` #78716c / `gradient-rose` #e8b8c4 | 2.76:1 | 3.0:1 | **Fail** — two-tone ring required |
| `focus` #78716c / `gradient-lavender` #c8b8e0 | 2.60:1 | 3.0:1 | **Fail** — two-tone ring required |
| `ink` #0c0a09 / `gradient-lavender` #c8b8e0 (two-tone outer edge) | 10.71:1 | 3.0:1 | Pass |
| Layer separation: `canvas` / `surface-card` | 1.09:1 | — | Not distinguishable by fill |
| Layer separation: `canvas` / `canvas-soft` | 1.04:1 | — | Not distinguishable by fill |
| Layer separation: `canvas` / `surface-strong` | 1.05:1 | — | Not distinguishable by fill |
| Layer separation: `surface-dark` / `surface-dark-elevated` | 1.13:1 | — | Not distinguishable by fill |

### Motion inventory

Cinematic profile, used verbatim. Prescribed, not extracted.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (button, card) | 240ms (`duration-fast`) | `ease-standard` | `opacity`, `box-shadow` to `{shadow.card-hover}` | Shadow at 150ms; no transform |
| Press | 120ms (`duration-instant`) | `ease-standard` | `transform: scale(0.99)`, `opacity` | Scale removed; fill change only |
| Focus ring appears | 120ms | `ease-enter` | `opacity` on the ring | No transition; ring appears at full opacity |
| Page / route transition | out 240ms, in 400ms | `ease-exit` / `ease-enter` | `opacity`, `translateY(12px)` | Travel removed; cross-fade at 150ms |
| Modal / drawer | in 400ms, out 240ms | `ease-enter` / `ease-exit` | `opacity`, `translateY(16px)` (drawer `translateX`) | Travel removed; opacity at 150ms |
| Dropdown | in 240ms, out 120ms | `ease-enter` / `ease-exit` | `opacity`, `translateY(-6px)` | Travel removed; opacity at 150ms |
| Toast | in 400ms, out 240ms | `ease-enter` / `ease-exit` | `opacity`, `translateY(12px)` | Travel removed; opacity at 150ms |
| List enter | 400ms per item, 80ms stagger | `ease-enter` | `opacity`, `translateY(8px)` | Stagger and travel removed; one fade at 150ms |
| List exit | 240ms, no stagger | `ease-exit` | `opacity`, `scale(0.99)` | Scale removed; opacity at 150ms |
| Loading | 900ms loop (`duration-emphasis`) | linear | `transform: rotate` / `opacity` pulse | Frozen; static 40%-opacity skeleton |
| Hero type settle (signature) | 600ms, 80ms per line | `ease-enter` | `opacity`, `translateY(16px)` | Travel and stagger removed; type present on first paint |
| Gradient orb drift (declared brand ambience) | 24s loop | `ease-standard` | `translate3d`, `scale(1.0 → 1.04)`, `opacity` | Frozen at frame 1 |

Exit is shorter than its matching entrance in every paired row. Only `transform` and `opacity` animate. The only infinite animations are the loader and the declared orb ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, line 352 (`structured = ...`) | The states check counts only lines in `## Components` starting with a pipe, dash or asterisk, or matching a run-in bold name followed by a dash. A file documenting states in an indented sub-block or a `### States` paragraph scores 1 while being fully documented. It rewards one layout rather than the presence of the facts. | Also count lines inside a `###` subsection whose heading contains "state", and count a run-in bold state name anywhere in the section. |
| `theme-audit/audit.py`, lines 289–300 (`disclosed`) | Disclosure matches on substring, so a line disclosing `hairline-soft` also silently discloses `hairline`, and a line disclosing `muted-soft` discloses `muted`. A file can clear three failures by naming one. | Match the token name on a word boundary (treating `-` as part of the word), or require the exact hex. |
| `theme-audit/audit.py`, lines 241–248 (`for bg in ("canvas", "surface", "accent")`) | The focus ring is checked only against the canvas, the representative surface and the accent. SPEC section 1 requires 3:1 against **every** surface the ring can appear over. Here the ring passes the harness at 4.40:1 while measuring 2.60:1 over `gradient-lavender`. | Check `focus` against every token matching the `surface` and `canvas` patterns, and flag unmeasurable surfaces (gradients, photography) for a stated two-tone treatment. |
| `theme-audit/SPEC.md`, line 83 | `disabled`-named tokens are exempt, but a token doing disabled duty under another name (`muted-soft` here, prose-documented as "Disabled text") is not. The harness therefore reports a failure WCAG does not require. | Exempt a token whose prose entry scopes it to the disabled state, or require such tokens to be named `*-disabled`. |
| `theme-audit/roster.md`, line 27 | The description column is truncated mid-sentence: "A voice-AI brand whose marketing surfaces read like a". The same truncation is copied into the brief's "Theme intent" line, so the intent statement an agent is judged against is an incomplete sentence. | Store the full description, or truncate on a word boundary with an ellipsis. |

### Needs approval

Three failing pairs are extracted brand facts. None was changed in place; each is disclosed in the file with its measured ratio, and a prescribed parallel token carries the job that needs contrast. What follows needs a human decision.

1. **`colors.muted` #777169 on `colors.canvas` #f5f5f5 — 4.43:1, needs 4.5:1.**
   Nearest passing value: **#757068** (4.51:1), a two-step darkening, visually indistinguishable.
   Usage note that makes the real value defensible: `{colors.muted}` is for labels at 18px+ (or 14px+ at weight 700), where the WCAG large-text threshold of 3:1 applies and 4.43:1 clears it comfortably. Below that size, use `{colors.muted-strong}`.
   Decision wanted: keep #777169 with the size scope, or replace the extracted hex with #757068 everywhere. I kept the extracted value.

2. **`colors.muted-soft` #a8a29e — 2.31:1 on canvas, 2.52:1 on white.**
   Nearest passing value for live text: **#757068** (4.51:1 / 4.91:1) — a substantial change in appearance, not a nudge.
   Usage note that makes the real value defensible: this tone is **disabled** text (WCAG sets no contrast requirement on disabled controls) and muted text on the dark bands, where it measures 7.83:1 on `{colors.surface-dark}` and 6.93:1 on `{colors.surface-dark-elevated}`. It is defensible everywhere it is actually used; it fails only if someone uses it for live secondary text on a light surface, which the file now forbids.
   Decision wanted: confirm that forbidding the light-surface use is enough, rather than renaming the token `muted-disabled`.

3. **The three extracted hairlines — #f0efed (1.05:1), #e7e5e4 (1.15:1), #d6d3d1 (1.37:1) on the canvas, all needing 3:1.**
   Nearest passing value: **#8a8580** (3.35:1), added as the prescribed `{colors.hairline-control}` rather than altering any extracted hex.
   Usage note that makes the real values defensible: a hairline between two blocks of non-interactive content is decoration, and WCAG 1.4.11 does not apply to it. It becomes a failure the moment it is the only boundary of a control — which is exactly what the file previously specified for `text-input` and `button-outline`.
   Decision wanted: confirm the decoration/control split, and confirm that shipping ElevenLabs' real near-invisible dividers on non-interactive content is acceptable. **Plainly: the real brand fails WCAG 1.4.11 on every boundary it draws at 1.05–1.37:1.** That is a fact about ElevenLabs, not about this document.

4. **`colors.semantic-success` #16a34a — 3.02:1 on canvas, 3.30:1 on white.** Not flagged by the harness (it matches no required role) but it fails AA for text. Nearest passing value on white: a darker green around #15803d. It was read off a mockup at an unknown type size, so the file now scopes it to icons and 24px+ and logs the uncertainty in Known Gaps. Needs a product decision.

5. **`colors.focus` #78716c, `colors.hairline-control` #8a8580 and `colors.muted-strong` #757068 are inventions.** ElevenLabs documents no focus ring and no accessible boundary tone. All three are labelled prescribed in the file. They need brand sign-off, particularly the ring: a neutral warm stone was chosen deliberately, because giving a brand with no accent colour a coloured ring would invent brand voltage.

6. **Two-tone focus ring over the gradient orbs and over photography.** `{colors.focus}` falls to 2.60–2.76:1 over lavender, sky and rose. The file specifies a 1px `{colors.ink}` outer edge there (10.71:1 against lavender). This adds a visual element the brand has never shipped, and is the one place where accessibility and the brand's "pure atmosphere" rule for the orbs genuinely conflict.

### Identity verdict

**The file still reads as ElevenLabs, and the Cinematic assignment is correct.** I considered arguing for Calm and concluded against it.

The SPEC's assignment rule is ordered. ElevenLabs is not a luxury, automotive, hardware, console or aerospace brand, so rule 1 does not fire on sector. It is a voice-AI product, but its marketing surfaces are not a developer tool — no dark canvas, no monospace, no terminal voice — so rule 2 does not fire. The palette is not saturated and colour never touches an interactive element, which rule 3 explicitly excludes. That leaves rule 4, Calm, by elimination.

But rule 1's own text names the tell rather than the sector: "full-bleed photography, sparse type and a slow reveal, not a dark background". ElevenLabs has exactly that signature. Atmospheric gradient orbs drift full-bleed behind the copy and are forbidden from carrying content; display type sits at 64px and weight 300 with letter-spacing pulled to -1.92px; sections breathe at 96px. That is the Cinematic signature from SPEC section 5 — "full-bleed imagery scales slowly; type arrives late and settles" — almost line for line. A Calm profile's 250ms base and "short opacity-led fades, little travel" would make a 64px Waldenburg Light headline over a drifting pastel bloom feel clipped. So I used Cinematic as assigned; the roster is right, for a reason the assignment rule reaches through its tell rather than its sector list.

The one real risk of drift was the new focus ring: a chromatic ring would have broken the brand's first rule, that it has no accent colour. A neutral warm stone drawn from the same stone ramp as `{colors.muted}` and `{colors.muted-soft}` keeps it inside the brand. Everything else added — the state table, the measured accessibility numbers, the motion brief — is scaffolding around values that are still this brand's own, and both prescribed colour tokens are near neighbours of hexes already in the file rather than imports from a generic scale.
