## A38 · mintlify

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| Before | 4 | 5 | 1 | 3 | 3 | 2 |
| After | 5 | 5 | 5 | 5 | 5 | 5 |

Before: `roles:focus; contrast-undisclosed:11; no-motion-section`.
After: `(disclosed:11)` — zero undisclosed failures, zero dangling refs, zero layout-property animations.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, G | `colors.focus` | No focus token anywhere in the file. The brand's only activation signal was `text-input-focused`'s `2px solid {colors.brand-green}` border at **1.92:1** on `{colors.canvas}` — a WCAG 1.4.11 failure, and the only focus affordance for every button, tab, nav item and link in the system. |
| P0 | F | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. The only timing in the file was an unsourced "recommend 150–200ms ease" line in Known Gaps. |
| P0 | G | whole file | No `## Accessibility` section. Eleven real contrast failures were present and none was disclosed. |
| P0 | B, E | `colors.hairline` on `colors.canvas` | 1.26:1, below 3.0:1, and it is the *only* visible boundary of `text-input`, `search-pill`, `button-secondary` and `button-icon-circular`. Extracted and frozen, so a parallel accessible token was required. |
| P0 | H | `## Components` | The file opened with "Per the no-hover policy, hover states are NOT documented" — a documentation convention, not a brand property, that left every interactive component with no hover and no focus-visible state. `hover`, `focus-visible` and `loading` appeared nowhere in the file. No README.md or CONTRIBUTING.md source for that policy exists; it was local to this file. |
| P1 | B | `on-dark` on `testimonial-orange` | 3.28:1 on both `testimonial-card-feature` and `founder-quote-card`, below 4.5:1. The 28px quote clears the 3:1 large-text threshold; the `{typography.body-sm}` / `{typography.body-sm-medium}` attribution beneath it does not. Extracted — disclosed, not changed. |
| P1 | B | `on-dark` on `hero-sky-from` | 2.48:1. Fails 4.5:1 and fails the 3:1 large-text threshold too, even at 72px `{typography.hero-display}`. The worst real failure in the file. |
| P1 | B | `on-dark` on `brand-error` (`badge-required`) | 3.99:1 at 11px/600 `{typography.micro-uppercase}`, so 4.5:1 applies. |
| P1 | B | `muted` on `canvas` / `surface` | 2.37:1 and 2.22:1. Was documented as "de-emphasized labels **and** disabled text" — the disabled half is WCAG-exempt, the labels half is not. Scoped to disabled and decoration only. |
| P1 | B | `hairline-soft` on `canvas` / `surface` | 1.17:1 and 1.09:1. Decorative dividers, so a usage scope rather than a replacement, but it was unstated. |
| P1 | C | `## Elevation & Depth` | Five elevation levels documented as raw `rgba(...)` strings with no `shadow:` group, so nothing could reference them; `pricing-card-featured` and `hero-product-mockup` repeated the literal strings in `components:`. SPEC section 1 requires a `shadow:` group where the prose documents real shadow values. |
| P1 | C | `hero-product-mockup` | The only component mixing a border and a shadow as competing boundaries, with no reason stated. Deliberate (screenshot frame on a gradient) but undocumented, which is what SPEC section C calls out. |
| P2 | C | canvas / surface / surface-soft | Layer separation is real but very thin: `surface` on `canvas` 1.07:1, `surface-soft` on `canvas` 1.04:1, `surface` on `surface-soft` 1.03:1. Defensible for a near-white documentation brand and no threshold applies to decorative layering, so left as extracted and noted here rather than altered. |
| P2 | D | typography | Complete — all 20 roles carry size, weight and line height. Body on this file's own surfaces: `{typography.body-md}` in `{colors.ink}` is 19.80:1 on canvas and 18.48:1 on surface. No finding. |
| P2 | E | `rounded` / `spacing` | Both ladders are internally consistent with no value outside its own scale: radius 4/6/8/12/16/24/full, spacing 4/8/12/16/20/24/32/40/48/64/96/120. `{rounded.xl}` (16px) and `{rounded.xxl}` (24px) are declared but used by no component entry — unused, not inconsistent. |
| P2 | A | `colors.brand-cursor` | `#888888`, byte-identical to `colors.stone`. A pre-existing duplicate pair; left alone, since renaming an extracted token is outside this audit's remit. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#005440"` | Prescribed focus ring for light grounds. Deep mint, same hue family as `{colors.brand-green}`, so the ring stays brand-true. 8.97:1 on `{colors.canvas}`, 3.61:1 on `{colors.hero-sky-from}`. |
| frontmatter `colors:` | — -> `focus-on-dark: "#00d4a4"` | The file documents both light and dark signature surfaces, so per SPEC section 1 one ring cannot serve both. Value is the brand mint itself: 10.33:1 on `{colors.canvas-dark}`, 8.87:1 on `{colors.surface-code}`. |
| frontmatter `colors:` | — -> `hairline-strong: "#888888"` | Parallel accessible boundary per SPEC section 2, for borders that are a control's only edge. Reuses the brand's own `{colors.stone}` grey — the lightest extracted grey clearing 3:1 on both light surfaces (3.54:1 / 3.31:1) — rather than inventing a hex. The frozen `hairline` and `hairline-soft` are untouched. |
| frontmatter | — -> `shadow:` group (`none`, `subtle`, `card`, `mockup`, `brand-glow`) | SPEC section 1: the prose documented five real elevation values with no token to reference. |
| frontmatter | — -> `motion:` group, Crisp block verbatim | SPEC section 4/5. Copied exactly from the Crisp block, no deviation. |
| frontmatter `components:` | — -> `focus-ring`, `focus-ring-on-dark` | Makes the ring referenceable, with its 2px outside offset declared so it is judged against the surface behind it (WCAG 2.2 Focus Appearance). |
| `components:` `pricing-card-featured`, `hero-product-mockup` | literal `rgba(...)` -> `{shadow.brand-glow}`, `{shadow.mockup}` | One source of truth for elevation. |
| `## Colors` → Surface | — -> `Hairline Strong` bullet | States the token is prescribed and scopes the frozen hairlines to decoration. |
| `## Colors` | — -> new `### Focus` subsection | Documents both rings, their grounds, and why the brand's green could not be used. |
| `## Colors` → Text, Muted bullet | "De-emphasized labels and disabled text" -> disabled and decorative only, with the 2.37:1 measurement and `{colors.steel}` / `{colors.slate}` named as the readable alternatives | The old wording sanctioned a 2.37:1 label. |
| `## Elevation & Depth` table | raw `rgba(...)` -> `{shadow.*}` token + the literal value retained | Reference integrity without losing the extracted fact. |
| `## Elevation & Depth` | — -> paragraph on the one-way-per-level rule and the level-3 exception | Dimension C: elevation is now expressed consistently, with the single border+shadow mix justified. |
| `## Components` | "Per the no-hover policy, hover states are NOT documented." -> withdrawal note | The policy was a convention with no source in the repo and it blocked SPEC section 7. |
| `## Components` | — -> `### Component States` table, one row per component entry | Names states for all 35 entries, including the single-state ones that genuinely have one. Added as a table rather than 35 inline bullets to keep the diff additive and avoid reflowing entries that needed no other change. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. Carries the 10-row interaction table, the rules, and the `prefers-reduced-motion` block. |
| after Motion | — -> `## Accessibility` | Passing pairs, the 11 disclosed failures with measured ratios, focus-ring visibility per surface, tap targets, reduced motion, and an explicit not-verifiable-here list. |
| `## Do's and Don'ts` | — -> 3 Do's, 4 Don'ts | Motion, focus ring and boundary-token guidance. |
| `## Known Gaps` | "recommend 150–200ms ease" -> prescribed-motion note | The old line invented a timing and presented it as advice; replaced with a labelled statement that the whole motion system is prescribed. Two further gaps added for the prescribed focus/boundary tokens and for unobservable keyboard and screen-reader behaviour. |

### Contrast checks

All computed with WCAG 2.1 relative luminance in `python3`, standard library only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #0a0a0a / `canvas` #ffffff | 19.80:1 | 4.5:1 | Pass |
| `ink` / `surface` #f7f7f7 | 18.48:1 | 4.5:1 | Pass |
| `charcoal` #1c1c1e / `surface` | 15.88:1 | 4.5:1 | Pass |
| `slate` #3a3a3c / `canvas` | 11.35:1 | 4.5:1 | Pass |
| `steel` #5a5a5c / `canvas` | 6.88:1 | 4.5:1 | Pass |
| `steel` / `surface` | 6.42:1 | 4.5:1 | Pass |
| `stone` #888888 / `canvas` | 3.54:1 | 4.5:1 | Fail as body text; passes 3:1 for 24px+ — captions only, noted |
| `on-primary` #ffffff / `primary` #0a0a0a | 19.80:1 | 4.5:1 | Pass |
| `primary` / `brand-green` #00d4a4 | 10.33:1 | 4.5:1 | Pass |
| `on-dark` #ffffff / `surface-code` #1c1c1e | 17.01:1 | 4.5:1 | Pass |
| `on-dark-muted` #b3b3b3 / `surface-code` | 8.11:1 | 4.5:1 | Pass |
| `on-dark` / `hero-dark-from` #1a3d4a | 11.60:1 | 4.5:1 | Pass |
| `on-dark` / `hero-dark-to` #2d5a4f | 7.82:1 | 4.5:1 | Pass |
| `ink` / `hero-sky-from` #87a8c8 | 7.98:1 | 4.5:1 | Pass |
| `brand-tag` #3772cf / `canvas` | 4.70:1 | 4.5:1 | Pass |
| `hairline-strong` #888888 / `canvas` | 3.54:1 | 3.0:1 | Pass |
| `hairline-strong` / `surface` | 3.31:1 | 3.0:1 | Pass |
| `focus` #005440 / `canvas` | 8.97:1 | 3.0:1 | Pass |
| `focus` / `surface` | 8.37:1 | 3.0:1 | Pass |
| `focus` / `surface-soft` #fafafa | 8.59:1 | 3.0:1 | Pass |
| `focus` / `hero-sky-from` | 3.61:1 | 3.0:1 | Pass |
| `focus` / `hero-sky-to` #f5e9d8 | 7.48:1 | 3.0:1 | Pass |
| `focus-on-dark` #00d4a4 / `canvas-dark` #0a0a0a | 10.33:1 | 3.0:1 | Pass |
| `focus-on-dark` / `surface-code` | 8.87:1 | 3.0:1 | Pass |
| `focus-on-dark` / `hero-dark-from` | 6.05:1 | 3.0:1 | Pass |
| `focus-on-dark` / `hero-dark-to` | 4.08:1 | 3.0:1 | Pass |
| `hairline` #e5e5e5 / `canvas` | 1.26:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `hairline` / `surface` | 1.18:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `hairline-soft` #ededed / `canvas` | 1.17:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `hairline-soft` / `surface` | 1.09:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `muted` #a8a8aa / `canvas` | 2.37:1 | 4.5:1 | **Fail** — extracted, disclosed |
| `muted` / `surface` | 2.22:1 | 4.5:1 | **Fail** — extracted, disclosed |
| `on-dark` / `testimonial-orange` #f55a3c — `testimonial-card-feature` | 3.28:1 | 4.5:1 | **Fail** — extracted, disclosed |
| `on-dark` / `testimonial-orange` — `founder-quote-card` | 3.28:1 | 4.5:1 | **Fail** — extracted, disclosed |
| `on-dark` / `brand-error` #d45656 — `badge-required` | 3.99:1 | 4.5:1 | **Fail** — extracted, disclosed |
| `on-dark` / `hero-sky-from` — `hero-band-sky` | 2.48:1 | 4.5:1 | **Fail** — extracted, disclosed; fails 3:1 too |
| `on-dark-muted` / `canvas` — `copy-code-button` | 2.10:1 | 4.5:1 | **Fail as measured; harness artifact** — the control's real ground is `surface-code`, where the same pair is 8.11:1 |
| `brand-green` / `canvas` (brand's own focus border) | 1.92:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `focus` / `testimonial-orange` | 1.52:1 | 3.0:1 | Fail — no ring covers the orange ground; no interactive control sits there |
| `focus-on-dark` / `testimonial-orange` | 1.71:1 | 3.0:1 | Fail — same |
| `surface` / `canvas` (layer separation) | 1.07:1 | n/a | Decorative layering, no threshold |
| `surface-soft` / `canvas` | 1.04:1 | n/a | Decorative layering, no threshold |
| `hairline-dark` #1f1f1f / `canvas-dark` | 1.20:1 | n/a | Dark-surface divider, decorative; `surface-code` 1.03:1 |

### Motion inventory

Prescribed **Crisp** profile, verbatim from SPEC section 5. Not measured from the live site.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity`; `transform: translateY(-1px)` on link-wrapped cards only | Travel removed; opacity cross-fade at 100ms |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `transform: scale(0.98)`, `opacity` | Scale removed; colour/opacity at 100ms |
| Focus | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` only — the ring never scales or travels in | Unchanged; already opacity-only and under 150ms |
| Page / route transition | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | `opacity` on the prose column only | Opacity-only at 100ms, no cross-fade overlap |
| Modal / drawer | enter `{motion.duration-base}` 150ms, exit `{motion.duration-fast}` 100ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `transform: translateX` (drawer), `transform: scale(0.98)` + `opacity` (dialog), scrim `opacity` | Travel and scale removed; fade at 100ms |
| Dropdown | enter 100ms, exit `{motion.duration-instant}` 60ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(-4px)` | Travel removed; fade at 100ms |
| Toast | enter 100ms, exit 60ms | enter `{motion.ease-enter}`, exit `{motion.ease-exit}` | `opacity`, `transform: translateY(8px)` | Travel removed; fade at 100ms |
| List enter | 100ms per item, `{motion.stagger-step}` 20ms between, capped at 8 | `{motion.ease-enter}` | `opacity`, `transform: translateY(4px)` | Stagger and travel removed; one fade at 100ms |
| List exit | 60ms, no stagger | `{motion.ease-exit}` | `opacity` | Unchanged; already opacity-only and under 150ms |
| Loading | spinner 800ms infinite; skeleton shimmer 1200ms infinite | linear | spinner `transform: rotate()`; skeleton `opacity` 0.4→1 | Both frozen; static glyph and flat 0.7-opacity block, loading still announced |

Every exit is shorter than its entrance. Nothing animates on first paint. `transform` and `opacity` only. The only infinite animations are the two loaders; this brand has no ambient motion.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, lines 384–387 (`if fg and not bg and roles.get("canvas"): bg = colors[roles["canvas"]]`) | A component whose `backgroundColor` is the literal `transparent` is measured against the canvas. That is right for `button-ghost` on a white page and wrong for `copy-code-button`, which is declared with a `{colors.hairline-dark}` border and `{colors.on-dark-muted}` ink — i.e. unambiguously inside the dark `code-block-header`. The harness reports it at 2.10:1; its real ground gives 8.11:1. Forced into "Real Failures, Disclosed" with an explanation, which makes the file state a failure that does not exist on the page. | Honour an optional `on:` or `parent:` key in a `components:` entry naming the component whose `backgroundColor` is the real ground, and fall back to the canvas only when no such key is present. A cheaper heuristic: when a transparent-fill component's own `textColor` or `border` resolves to a token whose theme is dark while the canvas is light, skip the pair rather than inventing a ground. |
| `theme-audit/audit.py`, lines 32–33 and 310 | `border` role resolution returns the first pattern match in declaration order, which for this file is `hairline-dark` (#1f1f1f, a dark-surface divider). `check("border", "canvas", 3.0, ...)` is then skipped entirely by `same_theme`, so the representative-role border check never ran on a light-canvas file. The real light boundary `hairline` was caught only because `check_all` sweeps every match. Harmless here, but on a file without `check_all` coverage the primary border check would silently pass. | When resolving a role, prefer the first matching key whose `theme_of` agrees with the resolved canvas, falling back to declaration order only if none agrees. |
| `theme-audit/audit.py`, line 322 (`focus_bands` / `focus_tokens`) | `focus-on-dark` matches `^focus-` and so joins `focus_tokens`, which is correct, but any future `focus-light` / `focus-dark` pair is also measured for coverage of *every* surface key via the any-ring rule — so a file can pass coverage while a specific ring is drawn on a surface it fails. Not triggered here (both rings were checked by hand, per-surface, in the Accessibility section). | Optionally let a ring declare the surfaces it serves (`focus-on-dark: {value, on: [canvas-dark, surface-code]}`) and measure each ring only against its declared grounds. |
| `theme-audit/SPEC.md`, section 1 | The "never add an alias token purely to satisfy a pattern" rule and the "such a file defines `focus` **and** `focus-on-dark`" rule collide when the correct dark-ground ring is the brand accent itself. `focus-on-dark: "#00d4a4"` here is byte-identical to `brand-green`. I followed the explicit `focus-on-dark` requirement, since it binds a distinct role to a distinct surface rather than feeding a regex — the `focus` role was already satisfied by `focus` alone. Worth a sentence in SPEC either way. | Add: "a polarity-paired ring may repeat an existing hex where that hex is the right ring for that polarity; state the duplication in the Accessibility section." |

Not a shared issue: the "no-hover policy" line appears nowhere in `README.md` or `CONTRIBUTING.md`. It was local to this file and is withdrawn in it.

### Needs approval

Five extracted brand values fail AA and were disclosed rather than changed. Each needs a brand-side decision.

1. **`on-dark` #ffffff on `hero-sky-from` #87a8c8 — `hero-band-sky`, 2.48:1** (needs 4.5:1; fails the 3:1 large-text threshold too, even at 72px). The worst failure in the file: the homepage hero headline is not readable at the top of the gradient. Nearest passing values: keep white and deepen the sky stop to **#4a6f94** (5.26:1), or keep the extracted gradient and set the headline in `{colors.ink}` (**7.98:1** on the existing #87a8c8). Usage note that would make the real value defensible: none — there is no size at which 2.48:1 passes.
2. **`on-dark` on `testimonial-orange` #f55a3c — `testimonial-card-feature`, 3.28:1.** Nearest passing: `{colors.ink}` on the same orange is **6.04:1**, or the palette's own `{colors.testimonial-orange-deep}` #cc3a1f carries white at **5.01:1**. Usage note: the 28px `{typography.heading-3}` quote is large text, so 3:1 applies there and 3.28:1 passes — the failure is confined to the `{typography.body-sm-medium}` attribution line.
3. **`on-dark` on `testimonial-orange` — `founder-quote-card`, 3.28:1.** Same pair, but this card's copy is `{typography.body-sm}` throughout, so no large-text note rescues it. Nearest passing: `{colors.ink}` at 6.04:1.
4. **`on-dark` on `brand-error` #d45656 — `badge-required`, 3.99:1.** Nearest passing: **#b32424** (6.57:1) as a label-only error tone, keeping #d45656 for borders and fills. Usage note: none available — the label is 11px/600, so 4.5:1 applies.
5. **`brand-green` #00d4a4 on `canvas`, 1.92:1**, as `text-input-focused`'s 2px activation border. Needs 3:1 for non-text contrast. The prescribed `focus-ring` (#005440, 8.97:1) is layered outside it so the green can stay as the brand's input-active cue, but if the green border is to be the *only* indicator it must deepen to **#007f62** (4.99:1) or darker.

Also for approval, as prescribed rather than extracted: `focus` #005440, `focus-on-dark` #00d4a4, `hairline-strong` #888888, the `shadow:` token names, and the whole Crisp motion block.

### Identity verdict

Still unmistakably Mintlify, and the profile is right.

The file reads as the same brand it did before: the dual-mode structure survives intact — atmospheric sky and dark-teal hero bands on one side, a dense 3-column docs grid with Geist Mono type signatures on the other — and the mint accent is still rationed to CTAs, checkmarks, the featured-tier border and active indicators. Every added token is anchored in something the file already said: the light focus ring is the brand mint darkened down its own hue rather than a borrowed blue; the dark ring *is* the brand mint; `hairline-strong` reuses the brand's own #888888 grey rather than an invented value. Nothing in the motion section would fit another file in the collection unaltered — it names the scroll-spy TOC, the sidebar group expand, the Monthly/Annual toggle re-rendering three tier cards, the "Copied" toast on the code-block header, and it explicitly rules out ambient motion on the cloud and rocket illustrations because those are static imagery.

**Crisp is correct and I kept it.** SPEC section 5 rule 2 fires on the nose — Mintlify is developer-tool identity, and the file's own evidence is overwhelming: Geist Mono for code blocks, inline code and type signatures; `{typography.code-md}` / `code-sm` / `code-inline` as first-class roles; a dark `surface-code` wrapper; a twoslash annotation palette; "documentation-grade body" at 14–16px; and an explicit Do that keeps deeper surfaces "flat and dense". The counter-argument is real and worth naming: the Overview calls the heroes "cinematic", the homepage runs a full-bleed cloud illustration on a soft gradient with a 72px display headline at 1.05 leading and a deep 24px-offset drop shadow on the mockup — which is close to SPEC's Cinematic tell. It still fails rule 1: Cinematic requires a luxury, automotive, hardware, console or aerospace identity, and documentation infrastructure is none of those; rule 1 is a conjunction and the atmospheric backdrop alone does not carry it. The deciding evidence is that the heroes are *static* — illustration and gradient, with no reveal, no parallax and no scaling imagery documented anywhere in the file. A brand whose only slow register is a still image is not a brand with slow motion. The two-tier reading is handled inside the profile instead: `{motion.duration-emphasis}` (300ms) is reserved for the marketing-side mobile drawer at full travel, while every docs-side state change sits at 60–100ms, which is exactly the Crisp signature of a state change reading as instant with no entrance choreography.

The one place the file now risks genericness is the `### Component States` table, which is necessarily mechanical. It is kept brand-specific where it can be — scroll-spy TOC selection, `{colors.brand-green-deep}` as the accent-button hover, the single-state orange quote cards and the reason they need no ring — but it is the least Mintlify-flavoured prose in the document, and a future pass folding those rows back into each component entry would read better.
