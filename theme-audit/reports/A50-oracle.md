## A50 · oracle

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

**4·5·1·1·1·1 -> 4·5·3·5·5·5**

Both runs are against `audit.py` md5 `1082e48a8a676d378a9c2f4c0a7dcf4a` (HEAD `1effc06`). The harness was patched three times while this review ran, which matters for the numbers: the brief's pre-measured summary came from an earlier revision that reported 2 contrast failures and `surface` unresolved, where the current revision reports 10 and resolves `surface`. The before-scores above were re-measured by running the current harness against the pristine file from `git show HEAD`, so before and after are comparable.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group and no `## Motion & Animation` section. Nothing in the file said whether motion was extracted or prescribed. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section. Three extracted boundary tones fail the 3:1 threshold and all three were undisclosed. |
| P0 | A · Token contract | `{colors.focus}` | The file claimed the ring is "declared once and applied identically on light and dark surfaces". It measures **1.81:1** on `{colors.band-forest}`, so the one deep-colour band on the site had no perceptible focus ring. The claim was false, not merely incomplete. |
| P0 | Section contract | whole file | No `## Known Gaps`. Prescribed and unverified material had nowhere to be declared, so inference and extraction read identically. |
| P1 | Section contract | `### Responsive Strategy` | Carried as a Layout subsection, not the required top-level `## Responsive Behavior`. |
| P1 | H · States | Components | Not one component named its state set. `hover`, `focus-visible`, `loading` and `error` appeared nowhere in the file at all. |
| P1 | A · Token contract | `text-dim` | Role unfilled, and **not fillable from this brand**. Oracle has one ink per polarity; captions and fine print are all `{colors.ink}`. Documented rather than invented — see Needs approval. |
| P1 | C · Elevation / B | `{components.button-secondary-inverse}` | Declared a white border and white label but no `backgroundColor`, so the harness measured both against the white canvas at 1.0:1. The prose said "dark band" but no component declared the ground, which SPEC §1 requires. |
| P1 | B · Colour | `{colors.field-border}` | 1.55:1 on `{colors.canvas}`. This is the border of the masthead search field — the site's only text input has no boundary a low-vision user can find. Was undisclosed. |
| P1 | B · Colour | `{colors.hairline}`, `{colors.divider}` | Measured only against the canvas. On cards they are worse: hairline falls to 1.14:1 on `{colors.canvas-warm}`, divider to 1.08:1. Eight pairings were unmeasured. |
| P2 | B · Colour | `{colors.error}` vs `{colors.brand-mark}` | 4.65:1 and 4.82:1 on canvas, and visually adjacent reds. Both pass; setting them side by side would make a validation message read as branding. Noted in the file. |
| P2 | G · Accessibility | `{components.link-inline}` | Colour-only affordance, no underline, which fails WCAG 1.4.1 for links inside running copy. Unresolvable without contradicting an explicit Don't. Documented, not overridden. |
| P2 | E · Borders / radius | `{rounded.xl}` 15px | Sits off a conventional ladder where 16px is expected. The file already called it deliberate; kept and moved into Known Gaps as unverified. |
| P2 | B · Colour | `{components.button-tertiary}` | Specified as "an 8% wash of `{colors.ink}`" — a composite with no token, so its contrast cannot be checked. Recorded as unverified. |
| P2 | D · Typography / tap target | `{components.button-primary}` | 37px tall, under 44×44. The file already said so; relabelled as arithmetic from declared padding, since nothing here renders. |

15 findings: **4 P0, 6 P1, 5 P2.**

Dimensions that came back clean: **D** (every typography role carries family, size, weight, line height and letter-spacing; `{typography.body}` at 16/400 measures 18.25:1 to 15.91:1 across all four neutral rungs), **E** (radius ladder 0·4·6·8·12·15·9999 with each step assigned to a distinct control family, and spacing 10 to 72 with no value off its own scale), **C** (elevation is expressed one way only — position on the neutral ladder, with a 1px rule for same-rung surfaces and explicitly no shadows; the ladder's adjacent steps are 1.04:1 to 1.05:1, which is the real finding and is now stated in Accessibility), and **A** reference integrity (zero dangling refs before and after).

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-strong: "#857f79"` | Parallel accessible boundary per SPEC §2. 3.96:1 on canvas, 3.05:1 on `{colors.band-teal}`; clears 3:1 on every ground in the file. The extracted tones are untouched and scoped to decoration. |
| frontmatter `colors:` | — -> `focus-on-dark: "#9ad5e8"` | SPEC §1's two-ring rule. `{colors.focus}` reaches only 1.81:1 on `{colors.band-forest}`; this counterpart reaches 5.21:1 there and 10.3:1 on `{colors.ink-deep}`. Same hue, flipped polarity, which is the system's own rule for dark grounds. |
| frontmatter | — -> `motion:` group | The **Calm** block from SPEC §5, verbatim, no deviation. |
| frontmatter `components:` | `button-secondary-inverse` gains `backgroundColor: "{colors.ink-deep}"` | SPEC §1: a stated ink-on-ground pair must be declared to be measurable. Resolves the 1.0:1 white-on-white artifact; the real pairing is 16.57:1. |
| `## Colors` → Surface | `{colors.hairline}` and `{colors.divider}` entries | Scoped to decoration with their measured ratios; `{colors.hairline-strong}` documented as prescribed and pointed at load-bearing rules. |
| `## Colors` → Semantic | Focus entry rewritten | Removed the false "identical on light and dark" claim; added measured ratios, the 2px/2px-offset geometry and why the offset is load-bearing. Added `{colors.focus-on-dark}`. |
| `## Colors` → Text | — -> explicit "no secondary or muted ink" bullet | States the `text-dim` absence as a brand fact and forbids promoting `{colors.disabled-ink}` (2.24:1) to body use. |
| `## Components` | — -> `### Interaction States` table | 14 components × 8 states. Marks the two extracted cells and labels the rest prescribed. Names the components that genuinely have one state. |
| `### Responsive Strategy` under Layout | moved -> `## Responsive Behavior` after Do's and Don'ts | SPEC §3: moved verbatim, `####` children promoted to `###`. Not duplicated — zero occurrences of the old heading remain. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. 10-interaction table plus a `prefers-reduced-motion` block. `transform`/`opacity` only; every exit shorter than its entrance. |
| after Motion | — -> `## Accessibility` | 27 measured pairs, per-surface ring coverage, tap targets, reduced motion. |
| end of file | — -> `## Known Gaps` | Four registers: prescribed, genuinely absent, not knowable from a document, unverified in extraction. |

200 insertions, 27 deletions. No section I was not fixing was reflowed.

### Contrast checks

Every value computed with WCAG 2.1 relative luminance via a stdlib snippet; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #161513 / `canvas` #ffffff | 18.25:1 | 4.5 | Pass |
| `ink` / `canvas-soft` #fbf9f8 | 17.39:1 | 4.5 | Pass |
| `ink` / `canvas-tint` #f5f4f2 | 16.6:1 | 4.5 | Pass |
| `ink` / `canvas-warm` #f1efed | 15.91:1 | 4.5 | Pass |
| `ink` / `band-teal` #d6e5e5 | 14.08:1 | 4.5 | Pass |
| `ink` / `accent-gold` #f0cc71 | 11.8:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary` #312d2a | 13.64:1 | 4.5 | Pass |
| `on-primary` / `primary-pressed` #47423e | 9.92:1 | 4.5 | Pass |
| `on-primary` / `ink-deep` #211e1c | 16.57:1 | 4.5 | Pass |
| `on-primary` / `band-forest` #33553c | 8.38:1 | 4.5 | Pass |
| `link` #006b8f / `canvas` | 6.0:1 | 4.5 | Pass |
| `link` / `band-teal` | 4.63:1 | 4.5 | Pass (tightest link pair) |
| `brand-mark` #c74634 / `canvas` | 4.82:1 | 4.5 | Pass |
| `error` #d63b25 / `canvas` | 4.65:1 | 4.5 | Pass |
| `focus` #227e9e / `canvas` | 4.62:1 | 3.0 | Pass |
| `focus` / `canvas-soft` | 4.4:1 | 3.0 | Pass |
| `focus` / `canvas-tint` | 4.2:1 | 3.0 | Pass |
| `focus` / `canvas-warm` | 4.03:1 | 3.0 | Pass |
| `focus` / `band-teal` | 3.56:1 | 3.0 | Pass |
| `focus` / `ink-deep` | 3.59:1 | 3.0 | Pass |
| `focus` / `band-forest` | **1.81:1** | 3.0 | **Fail** — reason `focus-on-dark` exists |
| `focus` / `accent-gold` | **2.99:1** | 3.0 | **Fail by 0.01** — gold is a 4px rule, never a ground; disclosed |
| `focus-on-dark` #9ad5e8 / `band-forest` | 5.21:1 | 3.0 | Pass |
| `focus-on-dark` / `ink-deep` | 10.3:1 | 3.0 | Pass |
| `focus-on-dark` / `primary` | 8.48:1 | 3.0 | Pass |
| `hairline-strong` #857f79 / `canvas` | 3.96:1 | 3.0 | Pass |
| `hairline-strong` / `canvas-warm` | 3.45:1 | 3.0 | Pass |
| `hairline-strong` / `band-teal` | 3.05:1 | 3.0 | Pass (tightest boundary pair) |
| `field-border` #d4cfca / `canvas` | **1.55:1** | 3.0 | **Fail** — extracted, disclosed |
| `field-border` / `canvas-warm` | **1.35:1** | 3.0 | **Fail** — extracted, disclosed |
| `hairline` #e4e1dd / `canvas` | **1.3:1** | 3.0 | **Fail** — extracted, disclosed |
| `hairline` / `canvas-soft` | **1.24:1** | 3.0 | **Fail** — extracted, disclosed |
| `hairline` / `canvas-tint` | **1.19:1** | 3.0 | **Fail** — extracted, disclosed |
| `hairline` / `canvas-warm` | **1.14:1** | 3.0 | **Fail** — extracted, disclosed |
| `divider` #e9e7e4 / `canvas` | **1.23:1** | 3.0 | **Fail** — extracted, disclosed |
| `divider` / `canvas-soft` | **1.18:1** | 3.0 | **Fail** — extracted, disclosed |
| `divider` / `canvas-tint` | **1.12:1** | 3.0 | **Fail** — extracted, disclosed |
| `divider` / `canvas-warm` | **1.08:1** | 3.0 | **Fail** — extracted, disclosed |
| `disabled-ink` #aea8a2 / `canvas-soft` | 2.24:1 | — | Exempt (disabled) |
| Ladder step `canvas` / `canvas-soft` | 1.05:1 | — | Not a threshold; the system's defining fact |
| Ladder step `canvas-tint` / `canvas-warm` | 1.04:1 | — | As above |

Nine real, extracted failures, all of them boundary tones, all now disclosed with their measured ratios. No brand hex was altered.

### Motion inventory

Calm profile, prescribed. First line of the file's Motion section says so.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity` of fill wash; no transform — nothing lifts, because nothing has a shadow to lift into | Instant, no transition |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` of pressed wash; no scale | Instant, no transition |
| Focus | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` of ring 0→1 | Instant at full opacity; never suppressed |
| Page transition | `{motion.duration-base}` 250ms | `{motion.ease-standard}` | `opacity` on the content column; band fills never animate | Fade at `{motion.duration-reduced}`; no travel |
| Modal / drawer | enter 250ms, exit 150ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px→0)`; scrim opacity only | Opacity only at 150ms; travel removed |
| Dropdown | enter 150ms, exit 80ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(4px→0)` | Opacity only at 150ms; no travel |
| Toast | enter 250ms, exit 150ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px→0)` | Opacity only at 150ms; no travel |
| List enter | 250ms per item, `{motion.stagger-step}` 40ms apart, capped at 8 items | `{motion.ease-enter}` | `opacity` + `translateY(8px→0)` | All fade together at 150ms; stagger and travel removed |
| List exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | `opacity` only, no stagger | Instant removal |
| Loading | `{motion.duration-emphasis}` 500ms loop | `{motion.ease-standard}` | `opacity` pulse 1.0↔0.55 on a `{colors.canvas-tint}` skeleton; in-button spinner rotates by `transform` | Both freeze; skeleton holds static |

Rules checked: `transform`/`opacity` only — the harness reports `layout_animation_mentions: []`. Every exit is shorter than its entrance. Nothing animates on first paint; the tonal ladder is painted and stable before anything moves. One infinite animation (the loader), no brand ambience, and that is stated. `duration-reduced` is 150ms, the cap.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 205-219 | The new `surface` binding fallback picks `subnav-active-bar` — a **67 × 5px gold selection indicator** — as oracle's representative card surface, because `CONTAINERISH` includes `bar` and the loop `break`s on the first match in frontmatter order, ahead of `hero-band`, `stat-panel`, `product-card-warm` and six `section-band-*` entries. It then manufactures the file's only two remaining undisclosed failures (`hairline on accent-gold-soft` 1.0:1, `on-primary on accent-gold-soft` 1.3:1), neither of which can render: a hairline is never drawn on the gold bar, and the white-bordered button is a dark-band variant. I did not disclose them, because documenting a pairing that cannot occur is the failure mode the `same_theme` comment at line 295 was written to prevent, and I did not add a `surface` alias, per SPEC §1. | Drop `bar|strip|rail|pill` from `CONTAINERISH` — those name indicators, not surfaces — or skip any component declaring a `height` under about 24px, or prefer the candidate that declares `padding`. With `bar` removed, oracle resolves to `canvas-warm` via `hero-band`, which is correct and whose boundary pairings I have already disclosed. |
| `theme-audit/audit.py` line ~470 (`acc_lines` / `disclosed`) | Disclosure matching harvests every `N:1` on a line, including the **Required** column of a Markdown table. A row reading `… \| 4.62:1 \| 3.0:1 \| Pass \|` auto-discloses any failure measuring 2.94 to 3.06 that shares the row's hex. That is how `no ring covers accent-gold` (2.99:1) first came back disclosed here before I had written a word about it. Any 3:1 threshold failure in any file can be silently cleared this way. | Match only the first `N:1` on the line, or parse the measured-ratio cell specifically, or exclude a figure that equals the row's own `required` value. |
| `theme-audit/SPEC.md` line 61 | The focus role is described as "**currently absent from all 84 files**", and the brief repeats the instruction to add one. `oracle` already defined `focus: "#227e9e"` before this review — an extracted value, and a correct one on light grounds at 4.62:1. An agent following the brief literally would have added a second redundant ring. | Amend the claim to "absent from nearly all files", and have the brief generator check the file's own frontmatter before issuing that instruction. |

### Needs approval

1. **`{colors.hairline-strong}` #857f79 — new prescribed token.** Not a brand value. Oracle's three real boundary tones measure 1.23:1, 1.3:1 and 1.55:1 on white and nothing between #d4cfca and #211e1c exists in the palette, so no extracted tone can carry a load-bearing rule. Nearest passing value for `{colors.field-border}` specifically is this same #857f79 at 3.96:1. The usage note that would make the real #d4cfca defensible: *it is acceptable only where the field also carries a persistent visible label and a non-border affordance such as a fill change, since WCAG 1.4.11 applies to a boundary only where the boundary is the sole indicator of the control.* That note does not rescue Oracle's masthead search field, which has neither.
2. **`{colors.focus-on-dark}` #9ad5e8 — new prescribed token.** Required by SPEC §1's two-ring rule. The alternative is a white ring, which would be indistinguishable from `{components.button-secondary-inverse}`'s own white border; this keeps the focus hue and flips polarity, which is the system's documented move for dark grounds.
3. **`{components.button-secondary-inverse}` now declares `backgroundColor: "{colors.ink-deep}"`.** This commits the component to a specific ground the prose only described as "a dark band". `{colors.ink-deep}` is the system's dark plane and the choice is defensible, but it is my inference, not an extracted binding.
4. **`text-dim` left unfilled.** I did not add one. Oracle genuinely has one ink per polarity, `{colors.disabled-ink}` is scoped and fails at 2.24:1, and inventing a muted brand grey would falsify the document. This costs one point of `tokens` permanently. If a prescribed tone is wanted instead, **#6b6660** measures 5.68:1 on canvas and 4.96:1 on `{colors.canvas-warm}`, passing AA on every surface in the file. Say the word and I will add it labelled prescribed.
5. **Interaction States are almost entirely prescribed.** Only `{colors.primary-pressed}` and `{components.subnav-active-bar}` are extracted. The wash percentages (8/12/16%), disabled opacities and the skeleton loader are my extension of the system's one-rung rule. No loading state was observed on the real site.

### Identity verdict

Still unmistakably Oracle, and in one respect more so than before.

The test I applied: would any of the added prose fit another file in the collection unchanged? No. The motion section argues from this file's own evidence — "motion moves a surface one rung, it does not introduce a new gesture", the 8px travel cap justified as "the motion equivalent of a 1.05:1 tonal step", hover explicitly refusing to lift "because this system has no shadow to lift into", and press explicitly refusing a scale pop as a Playful signature foreign to a `{rounded.xs}` charcoal button. Those sentences are unusable in a file that has shadows or a coloured CTA. The states table keeps every emphasis in `{colors.primary}` and every selection in the gold bar, so no new colour entered the system; the two tokens I added are a warm grey on the ladder's own hue and a polarity flip of a colour already present. Red is still on the wordmark alone.

The sharpest gain is that the file now says the true and slightly embarrassing thing about the brand: a system whose entire structural argument is tonal restraint has pushed that restraint past the point where its boundaries are perceptible, and its only text input has a border at 1.55:1. That is a more faithful portrait of Oracle than the pre-audit file, which asserted a focus ring worked "identically on light and dark" when on the forest band it was invisible at 1.81:1.

**Motion profile: Calm, confirmed, not switched.** It is worth recording that this was not automatic. SPEC §5 rule 2 sends "infra or developer-tool identity" to Crisp, and Oracle is a database and cloud-infrastructure company — on the company name alone, Crisp. But rule 2 asks for identity signals in the file, and this file documents the corporate and product marketing web: `{typography.display-serif-xl}` is a 56px Georgia headline with ball terminals, display weights are 300 and 400, Consolas is declared and "never appears in page chrome", gradients are forbidden, and the page is a stack of full-bleed editorial bands. There is no terminal, no IDE chrome, no monospace surface anywhere. Rule 1 does not fire (no full-bleed photography-led luxury reveal), rule 3 does not fire (chromatic colour never touches an interactive element, which is rule 3's own stated test). The documented identity is editorial, so rule 4 lands on Calm as its terminal answer rather than as a fallback. The 250ms base and symmetric ease are right for a page that reads as tonal shifts; a 150ms near-linear Crisp would make the gold rule and the band transitions feel clipped.
