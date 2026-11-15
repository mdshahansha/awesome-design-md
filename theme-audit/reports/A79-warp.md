## A79 · warp

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 4 | 5 |
| refs | 5 | 5 |
| contrast | 3 | 5 |
| sections | 1 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F. Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Nothing in the source records any duration or easing curve, so the vacuum was total. Fixed with the Crisp profile block verbatim, labelled prescribed in the section's first line. |
| P0 | G. Accessibility | whole file | No `## Accessibility` section. The brand's hairline failure (1.33:1 / 1.11:1) was therefore entirely undisclosed, which is the worst outcome for a document whose job is to tell the truth about the brand. Fixed. |
| P0 | A. Token contract | `colors.focus` | No focus role, so neither the file nor the harness could speak about a focus ring at all. Bound `focus: "#f7f5f0"` — the brand's own paper (`{colors.primary}` / `{colors.ink}`), a hex the palette already owns, with a mandatory 2 px `{colors.canvas}` offset. 13.74:1 on canvas, 11.44:1 on canvas-soft. |
| P0 | B. Colour | `{colors.hairline}` | 1.11:1 on `{colors.canvas-soft}` and 1.33:1 on `{colors.canvas}` — the extracted hairline is not a conformant boundary anywhere in this system, and `text-input` uses it as its only boundary. Extracted and frozen, so disclosed plainly and re-scoped to decoration in prose; `{colors.mute}` (already in the palette, 5.19:1 / 6.23:1) named as the tone for boundaries that are load-bearing. Bindings untouched; re-binding under Needs approval. |
| P1 | H. States | every component | Only `active` was documented anywhere (and that only in the auto-derived `ex-app-shell-row` description). Fifteen component entries now name their states; six of them genuinely have one or two states and say so. |
| P1 | C. Section contract | `## Responsive Behavior` | Existed only as `### Responsive Strategy` inside Layout. Moved verbatim to a top-level section between Do's and Don'ts and Known Gaps, child headings promoted `####` → `###`. The heading itself was renamed to the contract's name; content is byte-identical. |
| P1 | C. Section contract | `## Known Gaps` | Absent. Added, carrying nine real gaps including the prescribed-motion disclosure. |
| P1 | C. Background and elevation | canvas vs canvas-soft | The two surfaces sit 1.20:1 apart, so surface contrast alone does not separate a card from the page — and the hairline that is meant to compensate is at 1.11:1 against the card fill. The file never said this. Now stated in Accessibility. Elevation itself is consistently expressed (surface step + hairline, no shadow), so no mixed-mechanism finding. |
| P1 | B. Colour | `text-input` error state | The brand surfaces no error, warning or success hue, so an error state cannot be signalled by colour. Specified as a mono `!` glyph plus `{colors.body-strong}` helper text, and recorded in Known Gaps. |
| P2 | E. Shapes | `{rounded.full}` | Referenced by `button-icon-circular` in both frontmatter and prose, but absent from the Shapes radius table, which listed only `{rounded.pill}` at the same 9999px. Row added, duplication noted. |
| P2 | D. Typography | — | No finding. Every one of the 14 roles carries family, size, weight and line height; body at 16/24 measures 13.74:1 on canvas and 11.44:1 on canvas-soft. |
| P2 | I. Identity | `ex-modal-card`, `ex-toast` | Auto-derived descriptions claim "elevated shadow" and "medium shadow" for a brand that Elevation & Depth says uses no shadow, and there is no `shadow:` group to reference. Left verbatim (generated text, and no dangling ref results), contradiction recorded in Known Gaps with the brand-correct alternative. |
| P2 | I. Identity | `ex-pricing-tier-featured` | Describes light-mode polarity behaviour this single-polarity token set does not define. Recorded in Known Gaps. |
| P2 | E. Spacing | `{spacing.md}` | 10 px sits off the stated 4 px base, as does the 6 px button padding mentioned in Layout. Extracted as such; left alone, recorded in Known Gaps. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | (no focus role) -> `focus: "#f7f5f0"` | A ring has to be addressable as `focus*` for the file and the harness to speak about it. The hex is `{colors.primary}`/`{colors.ink}`, already owned by the palette, so this is a role binding on a distinct job and surface, not an alias. |
| frontmatter | (no `motion:` group) -> Crisp block, all ten keys verbatim from SPEC section 5 | Required group; nothing extracted to displace it. |
| `## Colors` → Hairline bullet | plain "1 px solid divider" -> same plus measured 1.33:1 / 1.11:1, the statement that the real brand fails AA here, and the decoration/boundary split with `{colors.mute}` named | SPEC section 2 step 1: the palette already owns a passing tone, so re-scope the prose and add nothing. Step 4: say plainly that the brand fails. |
| `## Colors` | (no focus subsection) -> `### Focus` documenting which existing tone the ring reuses and its measured ratios | SPEC section 1 requires the Accessibility section to say which tone the ring reuses so nobody mistakes it for a new brand colour; stated in both places. |
| `## Shapes` radius table | `pill` row only -> `pill` scoped to status pills + new `full` row | `{rounded.full}` was referenced but undocumented. |
| `## Components`, 15 entries | no states -> `- States:` line per entry | SPEC section 7. Six entries (card-mockup, partner-logo-tile, testimonial-card, hero-band, content-band, non-interactive card-content) genuinely have one state and now say so rather than inventing a hover. |
| `## Components` → `text-input` | -> states line plus an accessibility note on the 1.11:1 border | The one control whose only boundary is the failing hairline; the reader needs to know at the component, not just in the Accessibility section. |
| after `## Components` | (nothing) -> `## Motion & Animation` | New required section, placed between Components and Do's and Don'ts per the contract's order. First line states it is prescribed and unmeasured. |
| after Motion | (nothing) -> `## Accessibility` | New required section: 13 measured pairs, focus-ring visibility on both surfaces, tap targets, reduced motion. |
| `## Layout` → `### Responsive Strategy` | moved out -> top-level `## Responsive Behavior`, children `####` → `###` | SPEC section 3: move verbatim, never duplicate, promote child headings one level. |
| end of file | (nothing) -> `## Known Gaps` | New required section. |

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3 -I`; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#f7f5f0` / `canvas` `#2b2622` | 13.74:1 | 4.5:1 | Pass |
| `ink` / `canvas-soft` `#383330` | 11.44:1 | 4.5:1 | Pass |
| `body-strong` `#dad2c1` / `canvas` | 9.96:1 | 4.5:1 | Pass |
| `body` `#c9c0ad` / `canvas` | 8.29:1 | 4.5:1 | Pass |
| `body` / `canvas-soft` | 6.90:1 | 4.5:1 | Pass |
| `mute` `#aea69c` / `canvas` (text-dim role) | 6.23:1 | 4.5:1 | Pass |
| `mute` / `canvas-soft` | 5.19:1 | 4.5:1 | Pass |
| `on-primary` `#2b2622` / `primary` `#f7f5f0` (on-accent on accent) | 13.74:1 | 4.5:1 | Pass |
| `primary` / `canvas` (the only signal colour — brand has no second CTA tone) | 13.74:1 | 3.0:1 | Pass |
| `focus` `#f7f5f0` / `canvas` | 13.74:1 | 3.0:1 | Pass |
| `focus` / `canvas-soft` | 11.44:1 | 3.0:1 | Pass |
| `focus` / `primary` fill (why the offset is mandatory, not the judged pair) | 1.00:1 | n/a — ring is drawn outside the control at 2 px offset and judged against the surface behind it | n/a |
| `hairline` `#3f3a36` / `canvas` | 1.33:1 | 3.0:1 | **Fail — frozen, disclosed** |
| `hairline` / `canvas-soft` | 1.11:1 | 3.0:1 | **Fail — frozen, disclosed** |
| `canvas-soft` / `canvas` (layer step, informational) | 1.20:1 | — | — |
| `mute` / `hairline` (sanity check for the alternative boundary tone) | 4.67:1 | — | — |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `background-color`, `border-color`, `color` — paint only | Unchanged; paint, not motion |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `background-color` — paint only, no scale | Unchanged |
| Focus | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Ring appears instantly, no transition |
| Page / route | 150ms in / 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` only | `opacity` at `{motion.duration-reduced}` 100ms |
| Modal / drawer | 150ms in / 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(4px → 0)` | Travel removed, `opacity` at 100ms |
| Dropdown | 100ms in / 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(2px → 0)` | Travel removed, `opacity` at 100ms |
| Toast | 150ms in / 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(6px → 0)` | Travel removed, `opacity` at 100ms |
| List enter | 100ms per item, `{motion.stagger-step}` 20ms | `{motion.ease-enter}` | `opacity` + `transform: translateY(4px → 0)` | Travel and stagger removed, all fade together at 100ms |
| List exit | `{motion.duration-instant}` 60ms, no stagger | `{motion.ease-exit}` | `opacity` + `transform: translateY(0 → 2px)` | Travel removed, `opacity` at 100ms |
| Loading | `{motion.duration-emphasis}` 300ms cycle, infinite | linear / `steps()` | `opacity` of a DM Mono block caret `▌` — the only infinite animation, declared as loader and brand ambience | Blink frozen at opacity 1, `aria-busy` carries it |

Every exit is shorter than its entrance (150→100, 100→60). Nothing animates on first paint. Only `transform` and `opacity` animate; no `width`, `height`, `top`, `left` or `margin` anywhere. Paint-only hover and press are deliberate: the brand has no shadow, no gradient and no chromatic accent, so paint *is* its state feedback, and a scale pop on a 3 px radius would contradict the file's own Don'ts.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` (role resolution) | `text-dim` resolves to `mute` `#aea69c`, which is correct, but `body` `#c9c0ad` and `body-strong` `#dad2c1` — the two tones that actually carry most secondary copy on this site — are never measured as text pairs at all. Only the role's representative token is checked. Both pass here (8.29:1, 9.96:1), so nothing is hidden in this file, but a brand with a failing mid-emphasis ink would slip through. | Measure every non-`disabled` colour token whose name matches a text-ish pattern against `canvas` and `surface`, the way signal colours are already all checked rather than just the representative accent. |
| `theme-audit/audit.py` (states check) | The one state the harness found before my edits was `active`, and its only source was the auto-generated `ex-app-shell-row` description string ("Active state uses brand primary as the indicator") in the frontmatter-mirrored Examples prose. SPEC's stated correction says a state counts only where Components documents it in a table row or list item, and a generated one-line description is neither — it is a label for a surface, not a state declaration. This inflated warp's before-score by one state. | Exclude the auto-derived `ex-*` description paragraphs from the states scan, or require the state word to appear in a line beginning `- States:` / a table cell, so generated boilerplate cannot score. |
| `theme-audit/audit.py` (contrast roles) | The two reported hairline failures are labelled `boundary on surface, all tones` and `bound boundary` — two different wordings for what is arithmetically the same token against two grounds. Harmless but it reads like two distinct checks. | Use one role label with the ground named, e.g. `boundary on canvas` / `boundary on surface`. |
| `theme-audit/SPEC.md` section 3 | The contract names the section `Responsive Behavior`, but files carry it as `Responsive Strategy`; "move it verbatim" does not say whether the heading text itself may change. I renamed the heading and kept the body byte-identical, since the harness matches on the contract's name. | State explicitly that the heading is renamed to the contract's name and only the body moves verbatim. |

### Needs approval

1. **Re-point `text-input.borderColor` from `{colors.hairline}` to `{colors.mute}`.** The extracted border measures 1.11:1 against the input's own `{colors.canvas-soft}` fill, and on `text-input` that line is the control's only boundary. `{colors.mute}` `#aea69c` is already in the palette and measures 5.19:1 on `canvas-soft` / 6.23:1 on `canvas`. I did **not** change the binding: it is an extracted fact about the real site and silently re-pointing it would make the document describe a product that does not exist. A brand owner should decide. The same question applies, less urgently, to `ex-data-table-cell.rowBorder`.
2. **Nearest passing value if the brand would rather keep one hairline token than split the job.** `{colors.hairline}` `#3f3a36` would need to reach roughly `#6f6862` to clear 3:1 against `{colors.canvas-soft}` `#383330` — a visibly heavier line that would change the brand's flatness. Not recommended, and not applied; recorded only so the number exists. The usage note that makes the real `#3f3a36` defensible: it is decoration, never the sole boundary of an interactive control or the sole separator between two pieces of content, and it is only ever drawn where a fill step or spacing already separates the layers.
3. **The error state has no hue.** `text-input`'s error is specified as a mono `!` glyph plus `{colors.body-strong}` helper text, because the brand surfaces no red. If the brand wants a semantic palette on the marketing surface, that is a new brand decision and three or four new tokens, not an audit fix.
4. **Focus ring geometry.** 2 px ring, 2 px `{colors.canvas}` offset, drawn outside the control. The token hex is the brand's own; the geometry is prescribed. The offset is not optional — against `button-primary`'s off-white fill the ring is at 1.00:1, so the dark gap is what makes it visible.

### Identity verdict

Still unmistakably Warp. The brand's four load-bearing facts are intact and untouched: the warm near-charcoal canvas at `#2b2622`, the single off-white "primary" that doubles as ink and CTA fill with no chromatic accent anywhere, the 3–4 px radii, and Inter 400 at 64 px with `-1.6px` tracking. Not one hex changed.

The additions read as this brand rather than as a token dump because each was argued from the brand's own constraints. The focus ring is the brand's paper, not a borrowed blue, because the file's first Don't is "don't introduce a chromatic brand accent" — a coral or azure ring would have broken the document it was meant to complete. Hover and press are paint-only with no scale, because the brand forbids generous shapes and heavy weights and has no shadow system to lift against; a scale pop would have been the generic answer. The loading indicator is a blinking DM Mono caret, which is the one place where the terminal identity makes the motion system brand-specific rather than profile-generic.

**Crisp is the right profile and I kept it.** Assignment rule 2 fires cleanly and unambiguously: Warp is a terminal and development environment, the identity is tool-like, and the file itself describes a page that "reads more like a developer's reading-mode editor than a marketing surface." Nothing in the file argues for Cinematic (no full-bleed photography, no slow reveal, no sparse-type luxury posture — the decoration is terminal screenshots and monochrome logo SVGs), for Playful (zero saturation, no illustration system, no colour on interactive elements), or for Calm (the brand is quiet but it is quiet in the way a tool is quiet, not in the way an editorial page is; its own voice is "state change reads as instant"). The 150ms base and 20ms stagger match what this product would actually feel like.

The one honest blemish in identity terms is not of my making: the ten auto-derived `ex-*` example surfaces carry generated descriptions referring to shadows and a light mode that this brand does not have. They read as borrowed from the collection's shared scaffold rather than from Warp. I left them verbatim — they are generated text, they produce no dangling references, and deleting them would lose content — and recorded the contradiction in Known Gaps with the brand-correct alternative stated.
