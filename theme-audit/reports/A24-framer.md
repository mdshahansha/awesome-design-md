## A24 · framer

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 2 | 5 |
| refs | 5 | 5 |
| contrast | 2 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

All six harness findings from the brief were reproduced before editing: missing `focus`, `surface`, `text-dim`; `hairline-soft` on canvas 1.14:1; `hairline` on canvas 1.32:1; missing Motion & Animation and Accessibility; and hover / focus-visible / disabled / loading / error named nowhere. One finding the brief did not list also appeared in `--json`: a component-level failure on `gradient-spotlight-card-orange`.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, G | whole file | No `focus` role and no focus ring anywhere. The only focus signal documented was the extracted `rgba(0,153,255,0.15)` 0 0 0 1px glow on inputs, which is a decorative halo far below 3:1 — on a #090909 canvas there was effectively no keyboard affordance in the system. |
| P0 | B | `gradient-spotlight-card-orange` | `{colors.ink}` #ffffff on `{colors.gradient-orange}` #ff7a3d measures 2.59:1 — below even the 3:1 large-text floor, undisclosed. Checked for a binding error first: the card binds `{colors.ink}` exactly as its violet, magenta and coral siblings do, the prose says the variants are "otherwise identical", and the file's own Don't forbids a third text tone, so the binding is faithful. This is a real brand failure at a frozen extracted anchor, not a mis-bound token. Hex unchanged; see Needs approval. |
| P0 | B, E | `text-input`, comparison table | `{colors.hairline}` at 1.32:1 was the only boundary of a text input and the only rule in a wide comparison table. A frozen value cannot be edited, so the fix is a parallel accessible token, not a changed hex. |
| P0 | F | whole file | No `motion:` group, no Motion & Animation section, no reduced-motion rule — the gap this audit exists for. |
| P0 | G | whole file | No Accessibility section, so every contrast failure in the file was undisclosed. |
| P1 | A | `colors.surface-1`, `colors.surface-2`, `colors.ink-muted` | The `surface` and `text-dim` roles were unresolvable. A numeric ladder (`surface-1/-2`) matches none of the role patterns, and `ink-muted` matches the `text` role's `^ink-` pattern but nothing in `text-dim`. Real tokens existed for both roles; only the names blocked them. |
| P1 | H | every component entry | hover, focus-visible, disabled, loading and error were named nowhere in the file. Buttons documented a pressed variant and the tabs a selected one; everything else was default-only with no statement that it was deliberate. |
| P1 | A | Elevation & Depth | The prose documented three real shadow values (`rgba(255,255,255,0.10)` top edge, `rgba(0,0,0,0.25)` drop, `rgba(0,153,255,0.15)` ring) with no `shadow:` group, so none of them was referenceable — the exact case SPEC section 1 calls out. |
| P1 | C | surface ladder | The three layers are 1.08:1 apart (canvas→surface and surface→surface-raised; 1.17:1 canvas→surface-raised). The file leaned on that ladder as the sole signal for "featured" and "selected" ("selected = lift, not color") without stating that the lift is near-subliminal and can vanish on a dimmed panel. |
| P1 | B | `gradient-spotlight-card`, `-magenta`, coral | White on violet 5.30:1, magenta 3.43:1, coral 3.08:1 — large-text-only on three of four grounds, previously undocumented. `{typography.subhead}` 24px/400 qualifies; `{typography.body}`, `{typography.caption}` and `{typography.micro}` do not, and nothing in the file said so. |
| P1 | A, G | gradient cards | Even a correct brand-blue ring collapses on the gradient tiles (1.16:1 on orange, 1.77:1 on violet), and `button-translucent` is documented as sitting on exactly those grounds — one ring could not serve both polarities. |
| P2 | E | Elevation & Depth | Elevation was expressed three ways (surface lift, light-edge + drop shadow, chromatic ring) with no rule saying which governs; the file listed "four shadow signatures" and then used a lift for the featured card. Consistent in practice, unstated. |
| P2 | D | `typography.display-xxl` | `fontFamily: GT Walsheim Framer Medium` where every other display tier says `GT Walsheim Medium`. Left as extracted — it looks like a real two-name font situation on the live site, and inventing a single name would falsify it. Logged, not changed. |
| P2 | E | `spacing` | The prose claims a 5px base unit, but `xxs` 4px, `xs` 8px and `sm` 12px are 4-multiples while `md` 15px, `lg` 20px and `xl` 30px are 5-multiples. Two interleaved ladders sharing one scale. Extracted values, so left in place; the claim in the prose is the part that is loose. |
| P2 | A | `colors.inverse-ink`, `motion.duration-slow` | Orphaned tokens: `inverse-ink` was defined and never referenced; the Calm block's `duration-slow` had no use once the motion table was written. Both now carry a stated use rather than being deleted. |
| P2 | G | Known Gaps | The section did not distinguish extracted facts from prescribed ones, and said nothing about forced-colors mode or about what a document cannot verify. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | `surface-1` -> `surface`; `surface-2` -> `surface-raised`; `ink-muted` -> `text-muted` (36 reference sites updated mechanically, prose labels "Surface 1/2", "Ink Muted" with them) | Resolves the `surface` and `text-dim` roles with the tokens that already existed. No hex changed; the ladder keeps its meaning and the Elevation prose still reads canvas → surface → surface-raised. |
| frontmatter `colors` | + `hairline-strong: "#6b6b6b"` | Parallel accessible boundary per SPEC section 2. 3.74:1 on canvas, 3.46:1 on surface, 3.20:1 on surface-raised — passes on every dark layer, so it works as an input edge and a table rule. Labelled prescribed. |
| frontmatter `colors` | + `focus: "#0099ff"` | The brand's own signal blue, so the ring is not an invention: 6.64:1 canvas, 6.14:1 surface, 5.68:1 surface-raised, 3.00:1 on `inverse-canvas` white. One ring covers every monochrome surface the file defines, including the white pill and the light template thumbnails. |
| frontmatter `colors` | + `focus-on-gradient: "#000000"` | SPEC's second-ring case. The blue is 1.16:1 on orange; black clears 3:1 on all four gradient grounds (3.97 / 6.12 / 8.10 / 6.82), and `button-translucent` is documented as living on those cards. |
| frontmatter | + `shadow:` group (`light-edge`, `float`, `focus-glow`) | The prose already documented these three real values; now they are tokens, and the Elevation table references them instead of inlining rgba. |
| frontmatter | + `motion:` group — the Calm block from SPEC section 5, verbatim | Required group; profile confirmed, not changed. |
| after `## Components` | + `## Motion & Animation` | First line states the system is prescribed to match the visual identity and was not measured from the live site. Table of 11 interactions × duration × easing × property × reduced-motion, rules (exit shorter than entrance, nothing animates on first paint, spinner the only infinite loop), and a `@media (prefers-reduced-motion: reduce)` block naming what is removed, what is kept at `{motion.duration-reduced}` and what is frozen. `transform` and `opacity` only. |
| after Motion | + `## Accessibility` | 18-row measured contrast table, a plain-language "where this brand fails AA" block, a per-surface focus-ring table for all eight surfaces, tap-target spec marked as specified-not-measured, and reduced motion. Every failure named with its ratio, which is what stops them counting against the file. |
| `## Components` intro | + one paragraph | States that state coverage is prescribed, since the source material is static captures. |
| 14 component entries | + a `States:` line each | default / hover / focus-visible / active-pressed / disabled / loading / selected / error as each component actually needs them, built from existing tokens. `pricing-card` + `-featured` say plainly they have two states and are containers, not controls; `product-mockup-tile` says default only. The input's error state uses `{colors.gradient-coral}` and is marked prescribed, matching the existing Known Gap about error styling. |
| `## Colors` | Hairline entries rewritten; + Hairline Strong, + Inverse Ink, + a `### Focus` subsection; + a paragraph under Brand Gradient | Scopes the two frozen hairlines to decoration with their measured ratios, documents the prescribed additions with ratios, and states the white-on-gradient numbers at the point of use. |
| `## Elevation & Depth` | rgba literals -> `{shadow.*}`; + a rule paragraph; + measured layer separation | One governing rule (surface lift; shadow only for things that genuinely float; the glow is a marker, not a step) and the honest 1.08:1 figure with the instruction never to let the ladder be the only signal. |
| `## Known Gaps` | + 5 entries | Motion prescribed, states prescribed, the three prescribed colour tokens, forced-colors undocumented, and what a document cannot verify at all. |

Nothing outside `design-md/framer/DESIGN.md` was touched. No hex of the brand's identity palette was altered, no section was reflowed, and no extracted value was edited — the only renames are token keys, applied consistently.

### Contrast checks

All computed with WCAG 2.1 relative luminance in a stdlib-only python3 snippet; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #ffffff / `canvas` #090909 | 19.91:1 | 4.5:1 | Pass |
| `ink` / `surface` #141414 | 18.42:1 | 4.5:1 | Pass |
| `ink` / `surface-raised` #1c1c1c | 17.04:1 | 4.5:1 | Pass |
| `text-muted` #999999 / `canvas` | 6.99:1 | 4.5:1 | Pass |
| `text-muted` / `surface` | 6.47:1 | 4.5:1 | Pass |
| `text-muted` / `surface-raised` | 5.98:1 | 4.5:1 | Pass |
| `on-primary` #000000 / `primary` #ffffff | 21.0:1 | 4.5:1 | Pass |
| `inverse-ink` / `inverse-canvas` | 21.0:1 | 4.5:1 | Pass |
| `accent-blue` #0099ff / `canvas` | 6.64:1 | 4.5:1 | Pass |
| `accent-blue` / `surface` | 6.14:1 | 4.5:1 | Pass |
| `semantic-success` #22c55e / `canvas` | 8.74:1 | 4.5:1 (glyph) | Pass |
| `focus` #0099ff / `canvas` | 6.64:1 | 3.0:1 | Pass |
| `focus` / `surface` | 6.14:1 | 3.0:1 | Pass |
| `focus` / `surface-raised` | 5.68:1 | 3.0:1 | Pass |
| `focus` / `inverse-canvas` #ffffff | 3.00:1 | 3.0:1 | Pass, exactly at threshold |
| `focus` / `gradient-violet` | 1.77:1 | 3.0:1 | Fail — ring never drawn there, disclosed |
| `focus` / `gradient-orange` | 1.16:1 | 3.0:1 | Fail — ring never drawn there, disclosed |
| `focus-on-gradient` #000000 / `gradient-violet` #6a4cf5 | 3.97:1 | 3.0:1 | Pass |
| `focus-on-gradient` / `gradient-magenta` #d44df0 | 6.12:1 | 3.0:1 | Pass |
| `focus-on-gradient` / `gradient-orange` #ff7a3d | 8.10:1 | 3.0:1 | Pass |
| `focus-on-gradient` / `gradient-coral` #ff5577 | 6.82:1 | 3.0:1 | Pass |
| `focus-on-gradient` / `canvas` | 1.05:1 | 3.0:1 | Fail — gradient-only ring, disclosed |
| `focus-on-gradient` / `surface` | 1.14:1 | 3.0:1 | Fail — gradient-only ring, disclosed |
| `focus-on-gradient` / `surface-raised` | 1.23:1 | 3.0:1 | Fail — gradient-only ring, disclosed |
| `hairline-strong` #6b6b6b / `canvas` | 3.74:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface` | 3.46:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface-raised` | 3.20:1 | 3.0:1 | Pass |
| `hairline` #262626 / `canvas` | 1.32:1 | 3.0:1 | **Fail — extracted, frozen, disclosed** |
| `hairline` / `surface` | 1.22:1 | 3.0:1 | **Fail — extracted, frozen, disclosed** |
| `hairline-soft` #1a1a1a / `canvas` | 1.14:1 | 3.0:1 | **Fail — extracted, frozen, disclosed** |
| `hairline-soft` / `surface` | 1.06:1 | 3.0:1 | **Fail — extracted, frozen, disclosed** |
| `ink` / `gradient-violet` | 5.30:1 | 3.0:1 large | Pass large, fail 4.5:1 body |
| `ink` / `gradient-magenta` | 3.43:1 | 3.0:1 large | Pass large only |
| `ink` / `gradient-coral` | 3.08:1 | 3.0:1 large | Pass large only, no margin |
| `ink` / `gradient-orange` (`gradient-spotlight-card-orange`) | 2.59:1 | 3.0:1 large | **Fail at every size — extracted, frozen, disclosed** |
| `on-primary` / `gradient-orange` (proposed alternative) | 8.10:1 | 4.5:1 | Pass |
| `ink` / #e05f20 (proposed darker ground) | 3.60:1 | 3.0:1 large | Pass large only |
| layer separation `surface` / `canvas` | 1.08:1 | n/a | Disclosed as near-subliminal |
| layer separation `surface-raised` / `surface` | 1.08:1 | n/a | Disclosed as near-subliminal |

### Motion inventory

Calm profile, prescribed and labelled as such in the file. `transform` and `opacity` only.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (pill, card, nav link) | `duration-fast` 150ms | `ease-standard` | `opacity`; `scale(1.01)` on cards | Opacity only at 150ms; scale dropped |
| Press (pill, icon button) | `duration-instant` 80ms | `ease-standard` | `scale(0.97)` | No transform; fill opacity step at 150ms |
| Focus-visible ring | `duration-instant` 80ms | `ease-standard` | `opacity` on the `focus` ring | Appears instantly, no fade at all |
| Page / route transition | `duration-base` 250ms | `ease-standard` | `opacity`; `translateY(8px)` on the first band | Opacity only at 150ms; no travel |
| Modal / drawer | 250ms in, 150ms out | `ease-enter` / `ease-exit` | `opacity`; `scale(0.98)→1`; backdrop `opacity` | Opacity only at 150ms; no scale |
| Dropdown / nav menu | 150ms in, 80ms out | `ease-enter` / `ease-exit` | `opacity`; `translateY(-4px)→0` | Opacity only at 150ms; no travel |
| Toast | 250ms in, 150ms out | `ease-enter` / `ease-exit` | `opacity`; `translateY(12px)→0` | Opacity only at 150ms; no travel |
| List enter (gallery, template grid) | 250ms, `stagger-step` 40ms | `ease-enter` | `opacity`; `translateY(12px)→0` | Stagger removed, all items fade together at 150ms |
| List exit (filtered-out tiles) | `duration-fast` 150ms | `ease-exit` | `opacity`; `scale(0.98)` | Opacity only at 150ms; no scale |
| Loading (spinner, tile skeleton) | 800ms/rotation, infinite | linear | `rotate()`; skeleton `opacity` 0.4↔0.7 | Spinner frozen at one frame; skeleton static at 0.5 |
| Display-type reveal (hero band) | `duration-emphasis` 500ms | `ease-enter` | `opacity`; `translateY(16px)→0` | Opacity only at 150ms; no travel |

`duration-slow` 400ms is in the block verbatim and is stated in the file as held in reserve for a full-bleed gallery crossfade — no interaction in the table reaches for it.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, `REQUIRED_COLOR_ROLES["surface"]`, line 22 | The `surface` pattern list has no alternative for a numeric ladder, so a perfectly valid `surface-1` / `surface-2` pair resolves to no `surface` role. A numbered elevation ladder is a common convention and this file is unlikely to be the only one. | Add `r"^surface-\d+$"` to the `surface` pattern list. |
| `theme-audit/audit.py`, `REQUIRED_COLOR_ROLES["text-dim"]`, lines 27-29 | `ink-muted` matches `^ink-` under `text` but nothing under `text-dim`, so a file using the ink/ink-muted pair loses the `text-dim` role while its `text` role still resolves. | Add `r"^ink-(muted|soft|dim|secondary)$"` to the `text-dim` pattern list. |
| `theme-audit/audit.py`, focus checks around line 307 | Every token matching `^focus-` is checked against every monochrome surface, so a correctly specified second ring for non-monochrome grounds (SPEC section 1's own `focus-on-dark` case) always registers failures that must then be disclosed as deliberate non-use. The disclosure is honest but it is noise, and it pushes files toward defining one ring where SPEC asks for two. | Skip a `focus-*` variant against surfaces its own name excludes, or check each focus token only against the surfaces the Accessibility section pairs it with. |
| `theme-audit/SPEC.md`, section 1 | SPEC names the second ring `focus-on-dark` for a light-canvas file. A dark-canvas file whose non-monochrome surfaces are saturated gradient cards has no "dark" counterpart to name, so the convention does not extend. This file uses `focus-on-gradient`. | Say in SPEC that the second ring is named for the surface class it serves (`focus-on-dark`, `focus-on-gradient`, `focus-on-photo`), and that the Accessibility section must pair each ring with its surfaces. |

### Needs approval

1. **`gradient-spotlight-card-orange`: white on `#ff7a3d` is 2.59:1 and fails at every text size.** Verified as a brand failure, not a binding error — the card binds `{colors.ink}` exactly as the violet, magenta and coral variants do, and that is what the brand does. The hex is a frozen extracted anchor and was not changed. Two options, each needing a brand owner:
   - *Nearest passing value, same type colour:* darken the ground to `#e05f20`, which carries white at 3.60:1. Usage note that makes it defensible: white type on a gradient tile only at `{typography.subhead}` 24px/400 or larger, where 3:1 applies; never body, caption or micro.
   - *Keep the extracted hex, change the type:* set the card's text to `{colors.on-primary}` black, 8.10:1 on this ground and ≥3.97:1 on all four gradients. This conflicts with the file's own Don't ("the hierarchy is binary: `ink` or `text-muted`"), so it is a brand decision, not an edit I can make.
   Interim rule now written into the file: treat orange spotlight cards as image-grade decoration and keep no essential text on them.
2. **White on magenta (3.43:1) and coral (3.08:1) is large-text-only.** Acceptable as-is under AA large text at the 24px subhead the cards use, but coral has no margin — any drift darker in the real gradient drops it below 3:1. Documented; a decision to keep body copy off gradient tiles is implied and worth confirming.
3. **The two frozen hairlines, 1.32:1 and 1.14:1 on canvas, are real brand values that fail.** Kept and scoped to decoration, with `hairline-strong` (#6b6b6b, 3.74:1, prescribed) added alongside for boundaries that carry meaning. Approval needed on the prescribed grey: it is a value Framer does not use, and on a near-black canvas a 3.74:1 rule is visibly louder than the brand's own hairline.
4. **`focus` #0099ff clears the white surface at exactly 3.00:1.** No margin. If the white pill CTA or a light template thumbnail is ever tinted even slightly, the ring falls below threshold and needs a darker blue or a two-tone edge.
5. **Three prescribed colour tokens and an entire prescribed motion system** now sit in a file that otherwise documents extracted facts. Each is labelled in place and in Known Gaps, but the ratio of prescribed to extracted content in this file has gone up materially and a brand owner should see that.

### Identity verdict

Still unmistakably Framer. The things that make the file specific are untouched: the -5.5px tracking on a 110px display, the GT Walsheim / Inter-with-character-variants split, the white pill as the only CTA shape, the single blue reserved for links and selection, the four gradient spotlight cards as atmosphere rather than section grounds, and the 5px-ish spacing oddity. The three colour additions borrow from the brand rather than importing a palette — the focus ring *is* `#0099ff`, and the gradient ring is the black already in `on-primary`. The motion section is the one place the file now carries content no one extracted, which is why its first line says so and why Known Gaps repeats it.

**Calm is the right profile, and it was kept.** The assignment rule would push a developer-tool identity to Crisp, and Framer is a builder. But rule 2 describes terminal, IDE and infra identities, and what this file documents is the marketing canvas, not the product chrome: one assertive statement per black band, 1.30 line-heights, a display weight of 500, surface lift instead of chromatic state, and the file's own words — "poster", "editorial", "like cuts in a dark film". That is Calm's signature (opacity-led fades, little travel), not Crisp's instant state change. A Crisp reading would also fight the 500ms hero reveal that this kind of poster band needs. No argument for a switch; no silent change made.

One honest limit: everything in Motion & Animation, every state beyond pressed/selected/focused, and every tap-target figure is prescribed or specified, not observed. This file has no DOM and no screenshots of interaction, so overlap, clipping, real tap targets and frame rate remain unverifiable here.
