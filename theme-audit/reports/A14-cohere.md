## A14 · cohere

Scores before -> after (1-5), from the harness: tokens 5 -> 5 · refs 5 -> 5 · contrast 2 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

Harness command: `python3 -I theme-audit/audit.py --site cohere --json`. All three contrast failures remain in the file as extracted facts and now count as disclosed, which is the intended outcome per SPEC section 2.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` token group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Nothing in the file said anything about timing. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Three measurable contrast failures were present and undisclosed. |
| P0 | H States | all 14 component entries | Not one state named anywhere in the Components section — no default, hover, focus-visible, active/pressed, disabled, loading, selected or error. |
| P0 | B Colour | `hairline` `#d9d9dd` | 1.41:1 on `canvas`, against 3.0:1 for a boundary. The Elevation table listed it as the border for forms and footer inputs, i.e. as the only boundary of text controls. |
| P1 | B Colour | `muted` `#93939f` | 3.04:1 on `canvas` and 2.71:1 on `card-border`, against 4.5:1. Prose assigned it to footer links, dates and metadata — body-size secondary text. |
| P1 | A Token contract | `focus-blue` `#4c6ee6` | Named as "keyboard focus and ring color" but measures 2.76:1 on `deep-green`, the brand's signature product band. One ring could not serve both polarities; the file defined no second ring and no ring geometry. |
| P1 | C Elevation | `canvas` / `card-border` / `soft-stone` | Light layers are 1.12:1 and 1.18:1 apart — not distinguishable by fill. The file relied on them as containment without saying so, and the only stated boundary failed 3:1. |
| P1 | B Colour | `coral` `#ff7759` | 2.61:1 on white. `blog-filter-chip` used a coral outline as a control boundary. |
| P2 | B Colour | `border-light` `#e5e7eb` | 1.24:1 on canvas; decorative only, was not scoped as such. |
| P2 | E Ladders | `spacing.xs` 6px | Sits off the documented 8px base. Extracted, so kept; now called out. |
| P2 | E Ladders | `rounded.lg` 22px / `xl` 30px / `pill` 32px | Three near-neighbours in one ladder. All three are extracted and the prose justifies 22px as the signature media radius; kept, noted. |
| P2 | C Elevation | Elevation table | Expressed consistently as border + surface change, never shadow — correct, but no `shadow:` group is needed and the file did not say so. |
| P2 | D Typography | all roles | Every role already carried size, weight and line height; body at 16px/1.5 in `ink` is 16.10:1 on canvas and 13.64:1 on `soft-stone`. No defect. |
| P2 | G Accessibility | `announcement-bar` close control | Bar is 36px tall, below a 44px tap target. Rendered size is not verifiable from a document, so recorded as a specification. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | added `hairline-strong: "#75758a"` | Parallel accessible boundary (4.50:1 on canvas) for borders that are a control's only edge. `hairline` stays frozen and is scoped to decoration. |
| frontmatter `colors` | added `focus-on-dark: "#ffad9b"` | `focus-blue` falls to 2.76:1 on `deep-green`. Taken from the brand's own Soft Coral rather than a generic white outline. |
| frontmatter | added `motion:` group, Crisp block verbatim | SPEC section 4; used literally so files sharing the profile stay comparable. |
| Colors > Text & Rules | `Muted Slate` / `Hairline` / `Border Light` entries rewritten | Each now carries its measured ratio and is scoped to decoration or large labels, with `body-muted` named as the accessible substitute. |
| Colors > Text & Rules | added `Hairline Strong` entry | Documents the new token and labels it prescribed. |
| Colors > Semantic | `Focus Blue` rewritten, `Focus On Dark` added | Names which surfaces each ring is drawn on, as SPEC section 1 requires for a file with both polarities. |
| Elevation & Depth | added two paragraphs; `Bordered` row rewritten | States that elevation is border + surface only (no `shadow:` group), gives the 1.12:1 / 1.18:1 layer ratios, and splits decorative rules from control boundaries. |
| after `## Components` | new `## Motion & Animation` section | First line states the system is prescribed to match the brand's identity and was not measured from the live site. Ten-interaction table plus a `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | new `## Accessibility` section | Measured contrast table, plain statement of the real AA failures, per-surface focus-ring ratios, tap targets, reduced motion, colour-not-alone. |
| Components, all 14 entries | added a `- **States:**` line each | States named per component, with the genuinely two-state and non-interactive ones saying so (`announcement-bar`, `trust-logo-strip`, `dark-feature-band`, `hero-photo-card`). |
| Known Gaps | added five bullets | Motion, states and the two new tokens labelled prescribed; the off-ladder spacing and radius values called out; the non-computable claims fenced off. |

Nothing else was reflowed. No extracted hex, type value, spacing value or radius was altered.

### Contrast checks

All computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---:|---:|---|
| `ink #212121` / `canvas #ffffff` | 16.10:1 | 4.5 | Pass |
| `ink` / `card-border #f2f2f2` | 14.38:1 | 4.5 | Pass |
| `ink` / `soft-stone #eeece7` | 13.64:1 | 4.5 | Pass |
| `ink` / `pale-green #edfce9` | 15.11:1 | 4.5 | Pass |
| `ink` / `pale-blue #f1f5ff` | 14.76:1 | 4.5 | Pass |
| `body-muted #616161` / `canvas` | 6.19:1 | 4.5 | Pass |
| `body-muted` / `card-border` | 5.53:1 | 4.5 | Pass |
| `muted #93939f` / `canvas` | 3.04:1 | 4.5 | **Fail (disclosed)** |
| `muted` / `card-border` | 2.71:1 | 4.5 | **Fail (disclosed)** |
| `muted` / `soft-stone` | 2.57:1 | 4.5 | **Fail (disclosed)** |
| `slate #75758a` / `canvas` | 4.50:1 | 4.5 | Pass |
| `hairline #d9d9dd` / `canvas` | 1.41:1 | 3.0 | **Fail (disclosed)** |
| `hairline-strong #75758a` / `canvas` | 4.50:1 | 3.0 | Pass |
| `hairline-strong` / `soft-stone` | 3.81:1 | 3.0 | Pass |
| `border-light #e5e7eb` / `canvas` | 1.24:1 | 3.0 | Fail — decorative only |
| `card-border` / `canvas` (layer separation) | 1.12:1 | n/a | Not distinguishable by fill |
| `soft-stone` / `canvas` (layer separation) | 1.18:1 | n/a | Not distinguishable by fill |
| `on-primary #ffffff` / `primary #17171c` | 17.86:1 | 4.5 | Pass |
| `on-dark #ffffff` / `deep-green #003c33` | 12.40:1 | 4.5 | Pass |
| `on-dark` / `dark-navy #071829` | 17.92:1 | 4.5 | Pass |
| `on-dark` / `cohere-black #000000` | 21.00:1 | 4.5 | Pass |
| `action-blue #1863dc` / `canvas` | 5.44:1 | 4.5 | Pass |
| `coral #ff7759` / `canvas` | 2.61:1 | 3.0 | Fail — fill/outline, never text |
| `ink` / `coral` (selected chip) | 6.16:1 | 4.5 | Pass |
| `coral-soft #ffad9b` / `canvas` | 1.79:1 | 3.0 | Fail — used on dark surfaces only |
| `error #b30000` / `canvas` | 7.20:1 | 4.5 | Pass |
| `focus-blue #4c6ee6` / `canvas` | 4.49:1 | 3.0 | Pass |
| `focus-blue` / `card-border` | 4.01:1 | 3.0 | Pass |
| `focus-blue` / `pale-green` | 4.21:1 | 3.0 | Pass |
| `focus-blue` / `pale-blue` | 4.11:1 | 3.0 | Pass |
| `focus-blue` / `soft-stone` | 3.80:1 | 3.0 | Pass |
| `focus-blue` / `deep-green` | 2.76:1 | 3.0 | **Fail — the reason focus-on-dark exists** |
| `focus-on-dark #ffad9b` / `deep-green` | 6.91:1 | 3.0 | Pass |
| `focus-on-dark` / `primary` | 9.95:1 | 3.0 | Pass |
| `focus-on-dark` / `dark-navy` | 9.99:1 | 3.0 | Pass |
| `focus-on-dark` / `cohere-black` | 11.70:1 | 3.0 | Pass |
| `form-focus #9b60aa` / `canvas` | 4.52:1 | 3.0 | Pass |

### Motion inventory

Crisp profile, prescribed. `transform` and `opacity` only; every exit shorter than its entrance.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity`; `scale(1.01)` on pill CTAs only | Opacity only at `{motion.duration-reduced}`; no scale |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `transform: scale(0.98)` | No transform; opacity step at `{motion.duration-reduced}` |
| Focus-visible ring | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on ring layer | Ring still appears, at `{motion.duration-reduced}` |
| Page / route transition | 100ms in / 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` only, no travel | Cross-fade at `{motion.duration-reduced}` |
| Modal / drawer | `{motion.duration-base}` 150ms in / `{motion.duration-fast}` 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)`, scrim opacity | Opacity only; no translate |
| Dropdown | 100ms in / 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(4px)` | Opacity only at `{motion.duration-reduced}` |
| Toast | 100ms in / 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(6px)` | Opacity only; auto-dismiss timing unchanged |
| List enter | 100ms per item, `{motion.stagger-step}` 20ms between | `{motion.ease-enter}` | `opacity` only — no stagger travel | Stagger dropped; one list-wide fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-reduced}`, no stagger |
| Loading | `{motion.duration-emphasis}` 300ms loop | `{motion.ease-standard}` | `opacity` pulse; `rotate()` on spinner | Rotation frozen, skeletons static, progress announced in text |

`{motion.duration-slow}` (220ms) is defined by the profile but unused: nothing in a Crisp enterprise tool interface earns it, and inventing a 220ms interaction to consume the token would have been worse than leaving it available.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 188 (`theme_of`) | A token name containing `light` is classed as the light *theme*, so `border-light` (`#e5e7eb`, 1.24:1 on canvas) is never checked against the default canvas and its failure is invisible to the harness. Names like `hairline-light` fail the same way across the repo. | Treat `light` as a theme marker only in `on-light` and a trailing `-theme`/`-mode` form, or require the opposing `dark` token to exist before splitting a file into themes. Observed, not guessed: `border-light` is absent from this site's failure list while `hairline` at 1.41:1 is present. |
| `theme-audit/audit.py` lines 326-336 (`layout_animation_mentions`) | The negation window is the 80 characters *before* `animat`, so the canonical, correct sentence "Only `transform` and `opacity` animate — never `width`, `height`, `top`, `left` or `margin`" is flagged as a violation. I had to reword to "...are animated. `width` ... are never animated." to clear it. Every agent writing that rule will hit this. | Scan the clause *after* the `animat` match for a negation as well as the clause before, or treat a backticked layout word following `never`/`not` as a prohibition. |
| `theme-audit/audit.py` line 357 (`states_documented`) | States are matched as independent substrings, so the single string `active/pressed` satisfies two checks while a file writing only "pressed" never credits "active". | Match `active|pressed` as one state, which is how SPEC section 7 words it. |
| `theme-audit/SPEC.md` lines 26-35 | Requires a `shadow:` group only "where the file documents real shadow values in its prose", but the required-groups sentence lists it inline, which reads as mandatory. Cohere documents no shadow at all. | Split the sentence: required groups are `colors`, `typography`, `spacing`, `rounded`, `components`, `motion`; `shadow` is conditional. |

### Needs approval

1. **`muted` `#93939f` fails AA for body text.** 3.04:1 on `canvas`, 2.71:1 on `card-border`, 2.57:1 on `soft-stone`, against 4.5:1. The hex is extracted and was not changed. Nearest passing value on white: `#767682` (4.50:1), which stays in the same cool-grey family. Usage note that would make the real value defensible: *this tone is for 18px+ regular or 14px+ bold labels on `canvas` only, where the 3:1 large-text threshold applies* — and even that does not hold on `card-border` or `soft-stone`, where it misses 3:1 too. Decision needed: adopt `#767682` as a `muted-strong` token, or accept the brand failure as documented and route all body-size secondary text to `body-muted` (`#616161`, 6.19:1), which is what the file now does.
2. **`hairline` `#d9d9dd` fails the 3:1 boundary threshold** at 1.41:1 on `canvas`. Extracted, not changed. I added `hairline-strong` `#75758a` (4.50:1) alongside it and scoped `hairline` to decoration. Needs sign-off that reusing the extracted Slate value for the new boundary token is acceptable, rather than introducing a hex not present in the brand.
3. **`focus-on-dark` `#ffad9b` is prescribed for this file.** No focus ring was observed on Cohere's live pages, so both ring colours and the geometry (2px ring, 2px offset, two-tone over photography) are specifications. The value is the brand's own Soft Coral, chosen over white so the ring is not mistaken for body text on the dark bands. Needs sign-off on a coral ring for a brand whose CTA system is deliberately monochrome.
4. **`coral` `#ff7759` at 2.61:1 on white** means a 1px coral chip outline is not a sufficient boundary. The documented chip pairs it with a pale fill and a text label and inverts on selection, which I recorded, but a stricter reading would require `blog-filter-chip` to carry a `hairline-strong` outline in its inactive state. Not changed, because it would alter a documented visual.
5. **`announcement-bar` is 36px tall**, so its close control cannot meet a 44px tap target without an invisible extended hit area. I specified the extension. It is a prescription, not a measurement.

### Identity verdict

The file still reads as Cohere. The additions are anchored to its own vocabulary rather than a generic token set: the new boundary token reuses the brand's extracted Slate; the dark-surface focus ring is the brand's Soft Coral, not white; and the motion table's defining choices — opacity-only page transitions so the hero declaration is never delayed, an opacity-only list enter with no stagger travel for the research and blog lists, a 60ms press — are arguments about *this* system's austerity, not boilerplate. The state lines name real Cohere components (`agent-console-card` loading skeletons, `blog-filter-chip` coral inversion, `research-table` row skeletons) and four entries correctly say they have one or two states rather than padding the list.

**The assigned Crisp profile is right, and I used it unchanged.** Working SPEC section 5's rules in order: rule 1 does not fire — there is photography, but it is contained in rounded cards with visible corners, which the file explicitly contrasts with full-bleed imagery, and this is not a luxury, automotive, hardware, gaming or aerospace identity. Rule 2 fires: this is infra and developer-tool identity — an "enterprise AI command center", a Playground, agent-console mockups with status chips and prompt fields, a `CohereMono` label role, and a research-publication table. The near-tie is with Calm, and the file does hand Calm two signals: it calls itself "sober" with "editorial restraint", and every display weight is 400. But rule 2 precedes rule 4, and the Crisp tells are stronger here — the file's own stated principle is that there is no decorative chrome in the normal interface, which is the same claim as "state change reads as instant; no entrance choreography". Playful is out despite coral and five pale washes: the saturated colour appears on taxonomy chips and photography rather than on the CTA system, the type voice is measured, and the file forbids gradients as UI fill, which rule 3 names explicitly as a not-Playful tell.

One place where the result is thinner than I would like: the 300ms `duration-emphasis` loader is the only animation a user would consciously notice, and Cohere's real pages lazy-load content blocks late (its own Known Gaps say so), so a real implementation will show more skeleton time than this table implies. That is a limit of the profile, not drift.
