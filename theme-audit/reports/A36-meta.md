## A36 · meta

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

**Before:** 3 · 5 · 1 · 3 · 3 · 2
**After:** 4 · 5 · 5 · 5 · 5 · 5

`tokens` stops at 4 because `text-dim` is still reported missing. That is a harness pattern gap, not a missing token — see Shared issues. Per SPEC section 1 I did not add an alias to satisfy the regex.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A (token contract) | `colors.focus` | No focus ring token anywhere in the file; no component documented a focus appearance. Fixed. |
| P0 | B/H (binding) | `hero-band-marketing` | `backgroundColor: {colors.canvas}` with `textColor: {colors.canvas}` — white on white, 1.0:1. A **binding error**, not a brand failure (reasoning below). Fixed. |
| P0 | F (motion) | frontmatter + body | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Known Gaps instead carried a bare guess ("150–250ms ease-out") presented as a recommendation. Fixed. |
| P0 | G (accessibility) | body | No `## Accessibility` section. Nine contrast failures were undisclosed, including two that are real text failures at the captured size. Fixed. |
| P0 | H (states) | `## Components` | The file opened with "Per the no-hover policy, hover states are NOT documented for any component below." That is a capture gap written as a design policy — Meta's commerce surfaces plainly have hover affordances. It suppressed hover, focus-visible and loading across 20+ components. Fixed with a prescribed, labelled state matrix. |
| P1 | B (contrast) | `badge-attention` | `{colors.canvas}` on `{colors.attention}` = 2.01:1 on a 12px `{typography.caption-bold}` label. The worst text pair in the system and a real failure. Disclosed; fix needs approval (see below). |
| P1 | B (contrast) | `badge-success` / `colors.success` | 3.28:1 as both a badge label ground and as body text ("In stock", "Free returns") at `{typography.body-sm}` 14px. Real failure. Disclosed; fix needs approval. |
| P1 | B/E (contrast) | `colors.hairline` | 1.54:1 on canvas, 1.40:1 on surface-soft, against the 3:1 non-text minimum — and it is the *only* boundary of `text-input` and of inactive `button-pill-tab`. Frozen extracted value, so a parallel `hairline-strong` was added per SPEC section 2 and the original scoped to decoration. |
| P1 | C (elevation) | `## Elevation & Depth` | Elevation is expressed three ways at once: a border at level 0, an `rgba(0,0,0,0.2) 1px 1px 0 0` offset rule at level 1, and a real soft shadow at level 2. The level-1 value is a hard 1px offset, not a shadow — it reads as a border drawn in the shadow slot. Left as extracted; flagged here only, since correcting it would falsify an extracted value and the level ladder is coherent as a *use* ladder. |
| P1 | C (layering) | `canvas` vs `surface-soft` | The two surface layers separate at only **1.10:1**. The layers are effectively indistinguishable; the system relies on borders and rounding, not luminance, to tell a card from the page. That is consistent with the file's own "runs predominantly flat" claim, so it is a documented characteristic rather than a defect — but a card on canvas is invisible without its hairline, and that hairline fails 3:1. Noted in the report rather than changed. |
| P2 | B (undeclared pair) | `card-feature-photo` | Prose says "copy is overlaid bottom-left in white" but the component declares no `textColor`, so the pair is invisible to the harness. I did **not** declare it: its ground is a photograph with no measurable colour, and declaring white-on-canvas there would manufacture the same false 1.0:1 I just removed from the hero. Recorded in Known Gaps instead. |
| P2 | E (radius ladder) | `rounded.circle` | Declared as `9999px` in the frontmatter but documented as `50%` in the Shapes table. Both produce a circle on a square box; they are not the same value. Left alone (extracted), flagged here. |
| P2 | D (typography) | `typography.heading-md` | Weight 300 at 28px is the file's signature editorial subhead. It is legible on both surfaces this file defines (`{colors.ink}` at 16.71:1 / 15.13:1), so no action — recorded because a 300 weight is the one type role worth re-checking on a rendered page, which this audit cannot do. |
| P2 | F (motion) | `## Known Gaps` | The old motion bullet contradicted the assigned profile (150–250ms versus a 400ms base). Superseded and labelled. |

### The `hero-band-marketing` verdict: binding error

**Mine is the figma pattern — a binding error — not framer's genuine brand failure.** Four pieces of evidence from this file alone:

1. The component's own prose (Signature Components) says the ground is *"Edge-to-edge product photography on a dark or photographic background."* Not canvas. The declaration contradicted the paragraph describing it.
2. The Overview's key characteristics say *"Photographic feature cards with no card chrome … the product imagery IS the surface treatment."* Canvas in this file is explicitly **not** the paintable surface of a photographic component.
3. The sibling `card-feature-photo` carries the same `backgroundColor: {colors.canvas}` with the prose gloss *"(visible only at the corners)"* — proving canvas is used in this file as a placeholder behind photography, not as a painted ground.
4. Every component in this file that genuinely paints white type on a ground binds `{colors.ink-deep}`, not canvas: `card-promo-strip`, `promo-banner`, `button-pill-tab-active`. The hero is the only white-on-white declaration in 35 components, and it is the only one whose ground is a photograph.

So, exactly as in figma's case, the background was bound to something that is not a paintable surface. framer's case was the opposite: the ink was bound the same way its siblings bound theirs, and the ground was a real frozen palette anchor. Here the siblings bind a *different* ground, and the declared one does not exist as paint.

Fix: `backgroundColor` rebound to `{colors.ink-deep}` — measured 18.78:1 with the existing white type. I did **not** invent a scrim alpha. The file's Elevation & Depth section documents that dark hero photography carries a translucent darkening overlay, but the only alphas it states (`rgba(255,255,255,0.1)`, `rgba(10,19,23,0.12)`) are far too light to support white type, so quoting one as the hero scrim would have been a fabricated extracted fact. Instead the component now declares the file's own darkest documented ground and states the implementer requirement: the photograph must be darkened to at least that luminance within the type's footprint. The unmeasurable residue is recorded in Known Gaps.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-strong: "#868b92"` | Parallel accessible boundary token per SPEC section 2. The two extracted hairlines are frozen but are the only boundary of `text-input` and inactive `button-pill-tab`. Clears 3:1 on both grounds (3.43:1 / 3.11:1). Labelled prescribed in the Colors section. |
| frontmatter `colors:` | — -> `focus: "#0064e0"` | Required role, absent from all 84 files. The brand's own cobalt, so the ring is brand-true rather than a generic blue. One ring clears 3:1 on all three of this system's surface polarities (5.39 / 4.88 / 3.49), so no `focus-on-dark` is needed. |
| frontmatter | — -> `motion:` group | Cinematic block from SPEC, verbatim, no deviation. |
| frontmatter `components.hero-band-marketing` | `backgroundColor: "{colors.canvas}"` -> `"{colors.ink-deep}"` | Binding error. Reasoning above. 1.0:1 -> 18.78:1. |
| `## Colors` → Surface | — -> **Hairline Strong** bullet | Scopes the extracted hairlines to decoration, labels the new token as prescribed, points at the measured failures. |
| `## Colors` | — -> `### Focus` subsection | States the ring value, the 2px outside offset, that one ring serves all polarities, and the two-tone variant over photography. Labelled prescribed. |
| `## Components` opening | "no-hover policy" blockquote -> capture-gap note + `### State Matrix` | The policy claim was a capture gap. The matrix covers all eight states across 14 component groups, marks prescribed states as prescribed, and says plainly that badges and static content blocks have one state each. |
| `## Components` → `hero-band-marketing` | — -> ground/scrim paragraph | Documents why the declared ground is `ink-deep` and what implementers must guarantee. |
| after `## Components` | — -> `## Motion & Animation` | First line states it is prescribed and unmeasured. 10-row interaction table, motion rules, reduced-motion CSS block. |
| after that | — -> `## Accessibility` | Measured key pairs, a plain statement of where the real brand fails AA, per-surface focus-ring ratios, specified tap targets (labelled as specifications, not measurements), reduced motion. |
| `## Known Gaps` | 1 motion bullet -> 4 bullets | Replaces a guess presented as a recommendation; adds the uncaptured states, the unmeasurable photographic grounds, and the prescribed ring. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #1c1e21 / `canvas` #ffffff | 16.71:1 | 4.5:1 | Pass |
| `ink-deep` #0a1317 / `canvas` #ffffff | 18.78:1 | 4.5:1 | Pass |
| `ink` #1c1e21 / `surface-soft` #f1f4f7 | 15.13:1 | 4.5:1 | Pass |
| `ink-deep` #0a1317 / `surface-soft` #f1f4f7 | 17.01:1 | 4.5:1 | Pass |
| `charcoal` #444950 / `canvas` | 9.07:1 | 4.5:1 | Pass |
| `slate` #4b4c4f / `canvas` | 8.59:1 | 4.5:1 | Pass |
| `steel` #5d6c7b / `canvas` | 5.39:1 | 4.5:1 | Pass |
| `steel` #5d6c7b / `surface-soft` | 4.88:1 | 4.5:1 | Pass |
| `stone` #8595a4 / `canvas` | 3.07:1 | 4.5:1 | Fail — scoped to disabled/decorative only, no WCAG requirement |
| `on-primary` #ffffff / `primary` #0064e0 | 5.39:1 | 4.5:1 | Pass |
| `on-ink-button` #ffffff / `ink-button` #000000 | 21.0:1 | 4.5:1 | Pass |
| `canvas` #ffffff / `ink-deep` #0a1317 (promo strip, hero band) | 18.78:1 | 4.5:1 | Pass |
| `hairline-strong` #868b92 / `canvas` | 3.43:1 | 3.0:1 | Pass (prescribed) |
| `hairline-strong` #868b92 / `surface-soft` | 3.11:1 | 3.0:1 | Pass (prescribed) |
| `hairline` #ced0d4 / `canvas` | 1.54:1 | 3.0:1 | **Fail — real, disclosed** |
| `hairline` #ced0d4 / `surface-soft` | 1.40:1 | 3.0:1 | **Fail — real, disclosed** |
| `hairline-soft` #dee3e9 / `canvas` | 1.29:1 | 3.0:1 | **Fail — decorative, disclosed** |
| `hairline-soft` #dee3e9 / `surface-soft` | 1.17:1 | 3.0:1 | **Fail — decorative, disclosed** |
| `warning` #f7b928 / `canvas` | 1.76:1 | 4.5:1 | Fail as text — fill only, disclosed |
| `warning-bg` #ffe200 / `canvas` | 1.30:1 | 4.5:1 | Fail as text — fill only, disclosed |
| `success-bg` #24e400 / `canvas` | 1.73:1 | 4.5:1 | Fail as text — fill only, disclosed |
| `success` #31a24c / `canvas` | 3.28:1 | 4.5:1 | **Fail — used as 14px text, disclosed** |
| `badge-success`: #ffffff / #31a24c | 3.28:1 | 4.5:1 | **Fail — real, disclosed** |
| `badge-attention`: #ffffff / #f2a918 | 2.01:1 | 4.5:1 | **Fail — real, disclosed** |
| `badge-promo-yellow`: `ink-deep` / `warning` | 10.66:1 | 4.5:1 | Pass |
| `badge-critical`: #ffffff / `critical` #e41e3f | 4.61:1 | 4.5:1 | Pass |
| `critical-strong` #f0284a / `canvas` | 4.11:1 | 4.5:1 | Fail — error *border* only, 1.4.11 applies at 3:1, so Pass in role |
| `focus` #0064e0 / `canvas` #ffffff | 5.39:1 | 3.0:1 | Pass |
| `focus` #0064e0 / `surface-soft` #f1f4f7 | 4.88:1 | 3.0:1 | Pass |
| `focus` #0064e0 / `ink-deep` #0a1317 | 3.49:1 | 3.0:1 | Pass |
| `canvas` / `surface-soft` (layer separation) | 1.10:1 | — | Layers are not luminance-distinguishable; see findings |
| `hero-band-marketing` after rebinding | 18.78:1 | 3.0:1 | Pass (was 1.0:1) |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity`, `transform: scale(1.02)` on card imagery only | Scale removed, opacity only at 150ms |
| Press | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `transform: scale(0.98)`, `opacity` | Scale removed, fill change untransitioned |
| Focus | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` on the ring | Instant, never suppressed |
| Page / route transition | enter 600ms / exit 400ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px)` | Travel removed, cross-fade at 150ms |
| Modal / drawer | enter 400ms / exit 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateX(100%)` or `scale(0.96)` | Travel and scale removed, opacity only at 150ms |
| Dropdown | enter 240ms / exit 120ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px)` | Travel removed, opacity only at 150ms |
| Toast | enter 400ms / exit 240ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(12px)` | Travel removed, opacity only at 150ms |
| List enter | 400ms per item, 80ms stagger, capped at 6 | `{motion.ease-enter}` | `opacity`, `transform: translateY(12px)` | Stagger and travel removed, all fade together at 150ms |
| List exit | 240ms, no stagger | `{motion.ease-exit}` | `opacity`, `transform: scale(0.98)` | Scale removed, opacity only at 150ms |
| Loading | 900ms loop, infinite | `{motion.ease-standard}` | `opacity` pulse on skeleton; `transform: rotate()` on spinner | Both frozen; static `{colors.surface-soft}` block |
| Hero photography settle (brand signature) | 900ms, once | `{motion.ease-enter}` | `transform: scale(1.02 -> 1.00)`, type arrives +80ms | Settle removed entirely; hero renders at rest |

Every exit is shorter than its entrance. `transform` and `opacity` only. The only infinite animations are the two loaders; this system declares no ambience loop.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, `REQUIRED_COLOR_ROLES["text-dim"]`, lines 28-31 | The patterns are `^text-dim$`, `^muted`, `^ink-(muted\|subtle\|soft\|tertiary\|secondary\|light)`, `^text-(secondary\|muted\|soft\|tertiary)$`, `^body-(soft\|muted\|secondary)$`, `^subtle$`, `^secondary$`, `^on-dark-soft$`, `^caption$`. This palette carries a full four-step dim ladder under brand names — `charcoal` (#444950, "tertiary body text"), `slate` (#4b4c4f, "supporting microcopy"), `steel` (#5d6c7b, "quieter caption text"), `stone` (#8595a4, "de-emphasized labels") — none of which match. The role is plainly satisfied; only the regex disagrees. Per SPEC section 1 I did not add an alias, so this file scores `tokens: 4` for a token it has four of. | Either widen the pattern set to a documented synonym list that includes the common metal/stone greys (`^(charcoal\|slate\|steel\|stone\|graphite\|smoke\|ash\|gray\|grey)`), or — better, since synonym lists never end — resolve the role from the Colors prose: a colour bullet whose text contains "secondary", "tertiary", "muted", "caption", "quieter" or "de-emphasized" satisfies `text-dim`. The same gap will hit every file that names its greys after materials rather than after roles. |
| `theme-audit/audit.py`, semantic-tone loop, `FILL_MARKER` at line 308 | `FILL_MARKER` skips any token whose name contains `bg`, so `warning-bg` and `success-bg` are exempted as fills. That is correct for those two, but the same substring will exempt a genuine text token in any file that uses `bg` as a prefix or inside another word. Note also that this check's behaviour changed mid-audit: my first harness run reported `warning-bg` and `success-bg` as failures and my second did not, with no change on my side. | Anchor the marker to a token-name segment (`(^|[-_])(bg\|fill\|tint\|wash\|band)([-_]\|$)`) rather than a bare substring. Separately: pin or version the harness for the duration of a batch, so before/after scores in 84 reports are comparable. |
| `theme-audit/audit.py`, focus coverage, `surface_keys` at line 320 | `surface_keys` excludes any key starting with `ink`, so `ink-deep` — which is the painted ground of `card-promo-strip`, `promo-banner`, `button-pill-tab-active` and now `hero-band-marketing` — is not checked as a surface a ring can land on. A file could ship a ring that is invisible on its own dark promo surfaces and still score 5. I verified that surface by hand (3.49:1, passes). | Derive the surface set from the `components:` block's declared `backgroundColor` values rather than from token names. Those are the grounds that actually exist. |

### Needs approval

1. **`badge-attention` label — real AA failure.** `{colors.canvas}` #ffffff on `{colors.attention}` #f2a918 measures **2.01:1** against 4.5:1 for its 12px `{typography.caption-bold}` label. Nearest passing value: keep the extracted amber fill and flip the label to `{colors.ink-deep}` #0a1317, which measures **9.36:1**. I did not apply it — the white label is the extracted value, and flipping it changes a documented fact rather than a token definition. Usage note that would make the real value defensible: none. At 12px no threshold forgives 2.01:1; this is simply a failure in the live brand.
2. **`badge-success` label and `colors.success` as text — real AA failure.** #ffffff on #31a24c and #31a24c on #ffffff both measure **3.28:1** against 4.5:1. Nearest passing value for the fill is roughly #2a8c42 (not applied — brand green). Usage note that would make the real value defensible: 3:1 applies to large text only, i.e. 18.66px+ bold or 24px+ regular. The badge label is 12px and the "In stock" body usage is `{typography.body-sm}` 14px, so **neither qualifies** and the note does not rescue it. Recommended resolution: `{colors.ink-deep}` on `{colors.success}` measures 5.73:1 and passes; or restrict `{colors.success}` text to 24px+.
3. **`colors.hairline` as a control boundary — real 1.4.11 failure.** 1.54:1 on canvas, 1.40:1 on surface-soft against 3:1, as the sole boundary of `text-input` and inactive `button-pill-tab`. I added the prescribed `hairline-strong` #868b92 (3.43:1 / 3.11:1) and scoped the extracted tone to decoration, but I did **not** rebind `text-input`'s border, because that border is an extracted value. Approval needed to rebind `text-input.border` and `button-pill-tab.border` to `{colors.hairline-strong}`, which would make the document prescriptive at those two points rather than descriptive.
4. **`colors.focus` duplicates `colors.primary`.** Both are #0064e0. This is deliberate — the ring is the brand's cobalt signal, and it is the only value in the palette that clears 3:1 on all three surface polarities (white 5.39, soft grey 4.88, ink-deep 3.49). `primary-deep` #0457cb would read as more ring-like but drops below 3:1 on `ink-deep`. Flagging it in case the collection prefers rings to be visually distinct from CTAs; if so, the honest consequence is a second token (`focus-on-dark`) and a pair of rings rather than one.
5. **`rounded.circle` disagrees with itself** — `9999px` in the frontmatter, `50%` in the Shapes table. Both render a circle on the square boxes this file uses them on, so nothing is visibly wrong, but one of the two is an inaccurate transcription. Approval needed to pick one, since I cannot tell from the file which was extracted.

### Identity verdict

The file still reads as Meta, and more so than before. Nothing I added is generic: the focus ring is Meta's own cobalt rather than a borrowed blue; `hairline-strong` is a darkened sibling of Meta's own hairline rather than a stock grey; the state matrix names this system's real components (`button-buy-cta` versus `button-primary`, `color-sku-picker-row`, `faq-accordion-item`) and keeps the brand's two-tier CTA logic visible by moving the cobalt pill's hover toward `primary-deep` and the black pill's toward `charcoal`, exactly as the extracted pressed states already did.

The **Cinematic** profile is correct for this file and I kept it. Assignment rule 1 fires on the identity alone — Quest VR and Ray-Ban Meta glasses are hardware-flagship commerce — and the file's own evidence is the Cinematic tell rather than the dark-canvas stereotype SPEC warns against: product photography given 50–70% of viewport height, a single 64px `hero-display` line over it, photography-as-depth in place of shadow, and an explicit "don't apply heavy shadows to marketing cards" rule. The white canvas does not argue against it, and SPEC says so outright. The one place Cinematic needed care is the configurator: a 400ms base is wrong for an information-dense purchase rail where a shopper is comparing storage tiers, so the press and dropdown interactions sit at 120ms and 240ms — within the profile's own token set, not a deviation from it.

The two places the file still reads thinner than the brand are both honest gaps rather than drift: dark-mode tokens genuinely were not published on these commerce surfaces, and the photographic grounds of `hero-band-marketing` and `card-feature-photo` cannot be measured from a document. Both are in Known Gaps where they belong.
