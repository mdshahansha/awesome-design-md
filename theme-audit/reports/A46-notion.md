## A46 · notion

Scores before -> after (1-5), from the harness: tokens 4 -> 5 · refs 5 -> 5 · contrast 1 -> 5 · sections 3 -> 5 · motion 3 -> 5 · states 1 -> 5

Harness command: `python3 -I theme-audit/audit.py --site notion --json`. After: 0 unresolved contrast failures, 14 disclosed, 0 dangling refs, 0 missing roles, 0 missing sections.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A | `colors.focus` | No focus indicator token of any kind. Nothing in the file said how keyboard focus is shown on any of its 14 distinct surfaces (canvas, surface, surface-soft, nine `card-tint-*` panels, the navy hero band, black fills). |
| P0 | B | `colors.muted` (#bbb8b1) | 1.98:1 on `canvas`, 1.82:1 on `surface`, yet documented as the token for **placeholders** — i.e. real text. Undisclosed. This is the weakest ink in the palette and, per the orchestrator, the worst secondary-text value in the 84-file collection. |
| P0 | B | `hairline`, `hairline-soft`, `hairline-strong` | No boundary tone in the palette reaches 3:1 on either light ground (1.28 / 1.21 / 1.74 on canvas; 1.18 / 1.11 / 1.59 on surface). `hairline-strong` at 1.74:1 is the *only* boundary of `text-input`, so the brand's text fields fail WCAG 1.4.11 outright. Undisclosed. |
| P0 | F | frontmatter, `## Motion & Animation` | No `motion:` group and no motion section. The only motion statement in the file was a Known Gaps line, "recommend 150–200ms ease". |
| P0 | G | `## Accessibility` | Section absent, so all 14 real contrast failures were undisclosed. |
| P0 | H / I | `## Components` preamble | `> Per the no-hover policy, hover states are NOT documented.` No such policy exists in README.md or CONTRIBUTING.md (`grep -rn -i "no-hover\|no hover\|hover polic"` returns nothing in either). It is boilerplate shared by seven files; in a document whose stated job is to tell the truth about a brand, an invented policy is the most serious kind of error, because it suppressed real content. |
| P1 | H | every component | 5 of 8 states never documented: hover, focus-visible, loading, selected, error. Only `pressed`, `disabled` and `active` appeared, via the extracted `button-primary-pressed`, `button-primary-disabled`, `text-input-focused`, `pill-tab-active`, `segmented-tab-active`. |
| P1 | A / C | `shadow:` group | The Elevation table and `workspace-mockup-card` document four real `rgba(...)` shadow values in prose with no token to reference. Per SPEC section 1 a `shadow:` group is required exactly here. |
| P1 | B | `badge-pink`, `badge-orange`, `badge-tag-green` | White on `brand-pink` 2.66:1, white on `brand-orange` 3.77:1, `brand-green` on `card-tint-mint` 2.50:1 — all 13px/600 labels, all requiring 4.5:1, all undisclosed. |
| P1 | B | `semantic-success`, `semantic-warning` | Listed as plain semantic tones with no usage limit, but 2.93:1 and 3.77:1 on canvas as text. |
| P1 | B | `search-pill` | `steel` on `surface` 4.17:1 at 16px — the search field's placeholder ink misses AA by 0.33. |
| P1 | C | `## Elevation & Depth` | Elevation expressed two ways with no rule: level 0 is border-only, levels 1–4 shadow-only, and `workspace-mockup-card` carries both at once with no explanation. |
| P2 | D | `## Typography` hierarchy table | `caption`, `micro` and `micro-uppercase` defined in frontmatter but missing from the table, so three type roles had no documented use. |
| P2 | B | `colors.stone` (#a4a097) | 2.61:1 on canvas, described only as "Muted labels" — no indication it cannot carry text. |
| P2 | E | `rounded.xl` / `xxl` / `xxxl` | 16/20/24px exist in the ladder with vague uses ("larger feature panels", "featured product showcases", "larger feature cards") and no component in the file uses any of them. Left alone: they are extracted values, and removing them would discard a fact. Noted for whoever next captures the site. |
| P2 | G | tap targets | The file states 40–44px buttons and ~32px desktop pill tabs. Below the 44x44px of WCAG 2.5.5 (AAA), though above 2.5.8 (AA). Not measurable from a document, so recorded as the file's own claim. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | (no focus token) -> `focus: "#3a2a99"`, `focus-on-dark: "#d6b6f6"` | Satisfies the one missing role with two tokens that have a real job. The file documents both light default surfaces and a navy signature band, so per SPEC section 1 one ring cannot serve both. Both values reuse hexes the brand already owns (`primary-deep`, `brand-purple-300`), so no colour is invented. |
| frontmatter | (none) -> `shadow:` group with `subtle`, `card`, `mockup`, `modal` | The prose already documented these four rgba values; they now have tokens to reference. |
| frontmatter | (none) -> `motion:` group, Crisp block verbatim from SPEC section 5 | Required group; values unaltered so this file stays comparable with its Crisp siblings. |
| `## Colors` → Surface | hairline entries unannotated -> each carries its measured ratio and is scoped to decoration; `hairline-strong` entry states that `{colors.steel}` is drawn where a control edge must be perceivable | SPEC section 2: frozen tones stay, the passing tone the palette already owns does the work. No new token added. |
| `## Colors` → Text | `muted`: "Disabled, placeholders" -> scoped to disabled text only, with both ratios, and secondary text redirected to `{colors.slate}` (6.80:1) and tertiary to `{colors.steel}` (4.54:1); `stone` annotated | The failure is disclosed, not patched, and the file now points at tones that pass. |
| `## Colors` → Semantic | three bare one-liners -> each carries its ratio and its usage limit | `semantic-success` is a fill tone, `semantic-warning` is 24px+ text only. |
| `## Colors` | (none) -> `### Focus` subsection | States that the ring is prescribed, lists its ratio on every surface, and states the 2px ring / 2px offset geometry and that the ring is measured against the surface behind the control. |
| `## Elevation & Depth` | bare rgba values -> `{shadow.*}` references alongside the literal values, plus a paragraph stating the one-way-per-level rule and the single documented exception | Makes the mixed border/shadow expression explicit instead of accidental. |
| `## Typography` | table missing three tokens -> rows added for `caption`, `micro`, `micro-uppercase` | Every defined type role now has size, weight, line height and a use. |
| `## Components` preamble | `> Per the no-hover policy, hover states are NOT documented.` -> a note listing which state variants were extracted and stating that hover, focus-visible, loading, selected and error are prescribed | **The no-hover policy claim is withdrawn.** It has no source in README.md or CONTRIBUTING.md and is boilerplate that propagated to seven files. The honest fact is that a static capture cannot show hover. |
| `## Components` | (none) -> `### Interaction States` table, 17 rows | Names every state per component family, marks prescribed rows *P*, and says plainly where a component genuinely has one state (pastel tint cards, badges, static containers). |
| after `## Components` | (none) -> `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. 14-row interaction table, emphasis/ambience note, and a `@media (prefers-reduced-motion: reduce)` block. transform and opacity only; every exit shorter than its entrance. |
| after Motion | (none) -> `## Accessibility` | Passing pairs, the 14 real failures with measured ratios, focus-ring ratio per surface, tap targets flagged as the file's own claim rather than a measurement, reduced motion. |
| `## Do's and Don'ts` | 5 don'ts -> 9 | Added don'ts for `muted` text, hairline-only control boundaries, green-as-text, and animating layout properties. |
| `## Known Gaps` | 4 items -> 8 | Records that motion, the focus ring and five of the eight states are prescribed, that the no-hover claim was withdrawn and why, and that tap-target figures are declared values, not measurements. |

Sections were inserted between `## Components` and `## Do's and Don'ts`, which is the SPEC section 3 order. `## Responsive Behavior` was already a top-level section and was not touched. No extracted hex, type value, spacing or radius was changed.

### Contrast checks

All computed with WCAG 2.1 relative luminance via a `python3 -I` snippet; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #1a1a1a / `canvas` #ffffff | 17.40:1 | 4.5:1 | Pass |
| `ink` / `surface` #f6f5f4 | 15.98:1 | 4.5:1 | Pass |
| `charcoal` #37352f / `canvas` | 12.26:1 | 4.5:1 | Pass |
| `slate` #5d5b54 / `canvas` | 6.80:1 | 4.5:1 | Pass |
| `slate` / `surface` | 6.24:1 | 4.5:1 | Pass |
| `steel` #787671 / `canvas` | 4.54:1 | 4.5:1 | Pass |
| `steel` / `surface` | 4.17:1 | 4.5:1 | **Fail** (disclosed; `search-pill`) |
| `stone` #a4a097 / `canvas` | 2.61:1 | 4.5:1 | **Fail** (decorative/disabled only) |
| `muted` #bbb8b1 / `canvas` | 1.98:1 | 4.5:1 | **Fail** (disclosed) |
| `muted` / `surface` | 1.82:1 | 4.5:1 | **Fail** (disclosed) |
| `hairline-soft` #ede9e4 / `surface` | 1.11:1 | 3.0:1 | **Fail** (disclosed) |
| `hairline` #e5e3df / `surface` | 1.18:1 | 3.0:1 | **Fail** (disclosed) |
| `hairline-soft` / `canvas` | 1.21:1 | 3.0:1 | **Fail** (disclosed) |
| `hairline` / `canvas` | 1.28:1 | 3.0:1 | **Fail** (disclosed) |
| `hairline-strong` #c8c4be / `surface` | 1.59:1 | 3.0:1 | **Fail** (disclosed) |
| `hairline-strong` / `canvas` | 1.74:1 | 3.0:1 | **Fail** (disclosed) |
| `on-primary` #ffffff / `primary` #5645d4 | 6.57:1 | 4.5:1 | Pass |
| `link-blue` #0075de / `canvas` | 4.57:1 | 4.5:1 | Pass |
| `link-blue` / `surface` | 4.19:1 | 4.5:1 | Fail — see Needs approval |
| `semantic-error` #e03131 / `canvas` | 4.51:1 | 4.5:1 | Pass (no margin) |
| `semantic-success` #1aae39 / `canvas` | 2.93:1 | 4.5:1 | **Fail** (disclosed; fill tone) |
| `semantic-warning` #dd5b00 / `canvas` | 3.77:1 | 4.5:1 | **Fail** (disclosed; 24px+ only) |
| `badge-pink`: #ffffff / `brand-pink` #ff64c8 | 2.66:1 | 4.5:1 | **Fail** (disclosed) |
| `badge-orange`: #ffffff / `brand-orange` #dd5b00 | 3.77:1 | 4.5:1 | **Fail** (disclosed) |
| `badge-tag-green`: `brand-green` #1aae39 / `card-tint-mint` #d9f3e1 | 2.50:1 | 4.5:1 | **Fail** (disclosed) |
| `badge-tag-purple`: `brand-purple-800` / `card-tint-lavender` | 11.06:1 | 4.5:1 | Pass |
| `badge-tag-orange`: `brand-orange-deep` / `card-tint-peach` | 7.70:1 | 4.5:1 | Pass |
| `charcoal` / `card-tint-lavender` (weakest tint) | 9.54:1 | 4.5:1 | Pass |
| `charcoal` / `card-tint-yellow` (strongest tint) | 11.38:1 | 4.5:1 | Pass |
| `on-dark` #ffffff / `brand-navy` #0a1530 | 18.06:1 | 4.5:1 | Pass |
| `on-dark-muted` #a4a097 / `brand-navy` | 6.93:1 | 4.5:1 | Pass |
| `focus` #3a2a99 / `canvas` | 10.65:1 | 3.0:1 | Pass |
| `focus` / `surface` | 9.78:1 | 3.0:1 | Pass |
| `focus` / `surface-soft` #fafaf9 | 10.20:1 | 3.0:1 | Pass |
| `focus` / `card-tint-lavender` (worst tint) | 8.29:1 | 3.0:1 | Pass |
| `focus` / `brand-navy` | 1.70:1 | 3.0:1 | Fail — which is why `focus-on-dark` exists |
| `focus-on-dark` #d6b6f6 / `brand-navy` | 10.22:1 | 3.0:1 | Pass |
| `focus-on-dark` / `brand-navy-deep` #070f24 | 10.77:1 | 3.0:1 | Pass |
| `focus-on-dark` / `brand-navy-mid` #1a2a52 | 7.94:1 | 3.0:1 | Pass |
| `focus-on-dark` / `ink-deep` #000000 | 11.88:1 | 3.0:1 | Pass |
| `focus` / `primary` fill #5645d4 (ring vs control fill) | 1.62:1 | n/a | Stated in the file; the 2px offset carries the separation |

Layer separation (dimension C): `surface` on `canvas` 1.09:1, `surface-soft` on `canvas` 1.04:1, `card-tint-gray` on `canvas` 1.16:1. The three light layers are **not** distinguishable by luminance alone — they are Notion's real warm-white ladder and they depend on borders or shadows to read as layers, which is exactly why the 1.28:1 hairline matters. Recorded in the file's Elevation rule and Accessibility section; not altered, since all three are extracted.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | opacity, `translateY(-1px)` on cards | travel removed, opacity only at 100ms |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `scale(0.98)` | no scale; colour applies immediately |
| Focus (ring appear) | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | opacity on the ring | ring appears instantly |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | opacity | opacity only at 100ms |
| Modal / drawer enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | opacity, `translateY(8px)` → 0 | no travel, opacity only at 100ms |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | opacity, `translateY(4px)` | opacity only at 100ms |
| Dropdown enter | `{motion.duration-fast}` 100ms | `{motion.ease-enter}` | opacity, `translateY(4px)` → 0 | opacity only at 100ms |
| Dropdown exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | opacity | opacity only at 100ms |
| Toast enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | opacity, `translateY(8px)` → 0 | opacity only at 100ms |
| Toast exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | opacity | opacity only at 100ms |
| List enter | `{motion.duration-base}` 150ms + `{motion.stagger-step}` 20ms | `{motion.ease-enter}` | opacity, `translateY(6px)` → 0 | stagger and travel removed; all fade together at 100ms |
| List exit | `{motion.duration-fast}` 100ms, no stagger | `{motion.ease-exit}` | opacity | opacity only at 100ms |
| Loading | 800ms linear loop (spinner); `{motion.duration-slow}` 220ms skeleton pulse | linear / `{motion.ease-standard}` | `rotate()`, opacity | spinner becomes a static indicator; pulse frozen |
| Accordion expand | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | opacity, `scaleY()`, chevron `rotate(180deg)` | opacity only at 100ms; rotation removed |
| Hero mockup settle (emphasis) | `{motion.duration-emphasis}` 300ms | `{motion.ease-enter}` | opacity, `translateY(12px)` | removed entirely |

Every exit is shorter than its matching entrance. No infinite animation except the loader, which is stated as such. No layout property is animated — the harness confirms `layout_animation_mentions: []`.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `design-md/airbnb/DESIGN.md`, `design-md/ferrari/DESIGN.md`, `design-md/meta/DESIGN.md`, `design-md/mintlify/DESIGN.md`, `design-md/miro/DESIGN.md`, `design-md/x.ai/DESIGN.md` | The same unsourced line, `> Per the no-hover policy, hover states are NOT documented.`, sits in all six (plus notion, now fixed). The policy has no source: `grep -rn -i "no-hover\|no hover\|hover polic" README.md CONTRIBUTING.md` returns nothing. A document that cites a non-existent rule to justify an omission is wrong twice over. | Each file's owning agent replaces it with a factual note — hover is not observable in a static capture — and documents hover as prescribed. Out of my scope; one file only. |
| `theme-audit/SPEC.md` section 3 | The section table is declared to be the required document order, but the harness explicitly does not enforce it, so order drift is invisible to scoring across 84 files. | Add an `order_violations` field: compare the index order of `sections_present` against `REQUIRED_SECTIONS` and report inversions. Report-only at first, so no existing file's score moves. |
| `theme-audit/audit.py` lines ~346-360 (`focus_tokens` / `surface_keys`) | `ACCENTISH` matches `^brand`, so `brand-navy` is skipped as a ring target even though `hero-band-dark` declares it as a `backgroundColor` with white text — it is a genuine surface a ring lands on, not a signal fill. In this file the coverage check therefore never tested the navy hero band; `focus-on-dark` was added because I measured it by hand (1.70:1 for the light ring), not because the harness asked. Any file whose dark signature surface is named `brand-*` has the same blind spot. | Narrow `ACCENTISH` so `^brand` only skips a token that is not also used as a component `backgroundColor` with a declared `textColor`; a ground carrying declared text is a surface regardless of its name. |
| `theme-audit/audit.py` line ~457 (`acc_lines`) | Disclosure requires the Accessibility section to restate each ratio within ±0.06, so a file is rewarded for transcribing numbers the harness itself computed. A file could disclose a *wrong* pairing with a right-looking number. | Have the harness emit the failure list it expects to see disclosed, and match on the pair rather than on the digits alone. |

Not a harness bug, checked explicitly per the settled rule: `roles_missing` reported only `focus` before my edit, and the palette genuinely contained no focus tone under another name, so adding one was not an alias-for-regex. I added **no** token to satisfy a pattern. For `border`, `hairline-strong` already held the role name and the palette's only tone that can do perceivable boundary work (`steel`, 4.54:1) is referenced in the prose rather than duplicated as a new `border-*` alias — and all three hairline tones are still reported and still disclosed individually, exactly as the spec says they should be.

### Needs approval

Every item below is a real extracted brand value that fails WCAG AA. None was changed; each is disclosed in the file's Accessibility section with its measured ratio.

1. **`muted` #bbb8b1 as placeholder text** — 1.98:1 on canvas, 1.82:1 on surface. Nearest passing value at the same warm-grey hue: **#73706a** (4.94:1 canvas, 4.53:1 surface). In-palette alternative needing no new token: `slate` #5d5b54 (6.80 / 6.24) or `steel` #787671 (4.54 / 4.17 — canvas only). Usage note that would make the real value defensible: *`muted` is disabled-state ink only, where WCAG sets no contrast requirement.* I have written exactly that scope into the file, so #bbb8b1 is defensible as it stands **provided** nothing live draws placeholder text in it. Whether Notion actually does is not knowable from this document; the capture says "placeholders", which if accurate is a genuine product-level AA failure.
2. **`hairline-strong` #c8c4be as the `text-input` border** — 1.74:1 on canvas, 1.59:1 on surface, against the 3:1 of WCAG 1.4.11. Nearest passing warm grey: **#918c85** (3.34:1 canvas, 3.06:1 surface). Usage note: non-text contrast has no large-text exemption, so there is no size at which 1.74:1 becomes defensible for a control boundary — the only defensible framing is that the field is identified by its fill and label as well as its edge.
3. **`hairline` #e5e3df as the universal card border** — 1.28:1 on canvas. Nearest passing value **#918c85** (3.34:1), which would visibly coarsen Notion's whole warm-white card system. Usage note: decorative divider between layers that are themselves only 1.09:1 apart; it conveys no state and no boundary of an interactive control.
4. **`badge-pink` white on #ff64c8** — 2.66:1 at 13px/600. Nearest passing: **#c4267f** (5.34:1), a noticeably deeper magenta. Usage note: none is available — at 13px there is no large-text exemption. Defensible only if the badge text is decorative and duplicated elsewhere, or if the badge is redrawn with `brand-pink-deep` #a02e6d (6.76:1 against white) as the fill.
5. **`badge-orange` white on #dd5b00** — 3.77:1 at 13px/600. Nearest passing: **#c24e00** (4.79:1), a small and visually close shift. Usage note: 3:1 would apply at 24px+, or 18.66px+ at weight 700; the badge is 13px, so it does not qualify.
6. **`badge-tag-green` #1aae39 on #d9f3e1** — 2.50:1 at 13px/600. Nearest passing: **#157a28** on the same mint (4.64:1). Usage note: same as above; no size exemption applies at 13px.
7. **`semantic-success` #1aae39 as text on canvas** — 2.93:1. Nearest passing: **#157a28** (5.46:1). Usage note: defensible as a fill, icon or chart tone, which is how I scoped it; not as text at any size, since even the 3:1 large-text threshold is missed.
8. **`semantic-warning` #dd5b00 as text on canvas** — 3.77:1. Nearest passing: **#c24e00** (4.79:1). Usage note: *passes at 24px+, or 18.66px+ at weight 700* — this one is genuinely defensible with a size restriction, which is now written into the Colors section.
9. **`search-pill` placeholder `steel` on `surface`** — 4.17:1 at 16px, missing AA by 0.33. Nearest passing: **#73706a** (4.53:1 on surface). Usage note: `steel` passes on `canvas` (4.54:1); the failure is specific to the tinted field. Either darken the ink on tinted grounds or set the field on `canvas`.
10. **`link-blue` #0075de on `surface`** — 4.19:1. Not flagged by the harness, because no component declares that pairing, but the prose describes `link-blue` as the inline link colour and `surface` as a section background, so the pairing will occur. Nearest passing: **#0070d4** (4.52:1 on surface). Usage note: `link-blue` passes on `canvas` (4.57:1) only; it has no margin anywhere. I did not bind the pair in `components:` because the file never asserts it as a component — flagging it rather than inventing the pairing.
11. **Tap targets** — 40px buttons and ~32px desktop pill tabs, both from the file's own Responsive Behavior text. Below WCAG 2.5.5 (AAA, 44x44), above 2.5.8 (AA, 24x24). Unverifiable from a document; recorded as the file's claim. Needs a rendered page to settle.

### Identity verdict

Still unmistakably Notion, and the additions lean on the brand rather than on a generic scale. The focus ring is the brand's own deep purple and its dark counterpart is the brand's own light purple, so the indicator reads as Notion rather than as a default blue ring borrowed from another file in the collection. The states table is phrased in this file's vocabulary — the yellow-bold assistant banner, the pastel tint cards named as genuinely static, the `pill-tab` versus `segmented-tab` distinction, the "rectangles, not pills" geometry. The Accessibility section is specific to this palette's actual weakness, which is a warm-white layer ladder only 1.04–1.16:1 apart held together by hairlines that cannot be seen.

**Crisp is the right profile and I kept it.** The evidence is in the file: it documents a workspace tool whose own Known Gaps line recommends 150–200ms, and Crisp's `duration-base` is 150ms — the roster assignment and the file's only extracted motion statement agree, which is rare in this collection. Rule 2 of the assignment order is a near-miss rather than a hit (Notion is a workspace tool, not a terminal or IDE, though the file itself mentions a Developer Platform promo), so the honest reading is that Crisp survives on rule 4's terminal answer plus this corroborating evidence. I considered Playful and rejected it on SPEC section 5's own test: the nine pastel tints are static card backgrounds behind product screenshots, not saturated colour on interactive elements, the single saturated interactive tone is one purple CTA, and the file describes its own geometry as "sober-editorial". Calm would not be wrong, but at 250ms it would make a kanban board feel slower than the product it documents.

The one identity risk I introduced is length: the Interaction States and Accessibility tables are the two biggest blocks in the file and are the parts most likely to read as audit scaffolding in any of the 84. I kept them in this file's own component names and ratios rather than in generic role names, which is the only defence available.
