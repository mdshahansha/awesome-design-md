## A19 · dji

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

- **before:** 3 · 5 · 1 · 1 · 1 · 1
- **after:** 5 · 5 · 5 · 5 · 5 · 5

All six harness findings in the brief were reproduced before editing: `focus` and `text-dim` missing; `hairline` #f0f0f0 on #ffffff at 1.14:1 and `divider` #e8e8e8 on #ffffff at 1.23:1 against a 3.0:1 boundary minimum; Motion & Animation, Accessibility, Responsive Behavior and Known Gaps absent; hover, focus-visible, pressed and loading named nowhere. Two further contrast failures the brief did not list were also present (`button-store-cart` 4.41:1, `option-badge` 2.38:1).

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A tokens | `colors.focus` | No focus token at all, and no focus treatment anywhere in the file. A white-canvas site with a blue pill, a black media tile and a charcoal footer cannot be served by one ring. |
| P0 | F motion | whole file | No `motion:` group, no Motion & Animation section, no reduced-motion rule. Nothing in the file said how anything moves. |
| P0 | G accessibility | whole file | No Accessibility section. Thirteen real AA failures in the extracted palette were undisclosed, including every interactive boundary. |
| P0 | B colour | `control-border` #cccccc (1.61:1), `input-border` #d4d7d9 (1.45:1), `card-border` #d9d9d9 (1.41:1), `dashed-border` #dddddd (1.36:1) | The quantity stepper, checkbox, store email field and option card are interactive and their only boundary is below 2:1. More serious than the two lines the brief flagged, which are decorative rules. |
| P0 | B colour | `button-store-cart` — `store-blue` on `store-blue-tint`, 4.41:1 | Add to Cart is a primary commerce action failing 4.5:1 at 16px/400. Extracted, so frozen; was undisclosed. |
| P0 | B colour | `option-badge` — white on `badge-orange` #fa8c16, 2.38:1 | 12px/600 label at under half the required ratio. Extracted, frozen, was undisclosed. |
| P1 | B colour | `hairline` 1.14:1, `divider` 1.23:1 on canvas | Confirmed. Both are genuinely decorative (the tab's ink underline and the FAQ chevron carry the real signal), so they are scoped to decoration and disclosed rather than changed. |
| P1 | B colour | `steel` #9fa3a6 2.54:1, `ink-tertiary` #8c8c8c 3.36:1, `link-blue` #1890ff 3.24:1, `error` #f5222d 4.08:1 on canvas | Four more AA failures on 12–16px text that the harness does not check, because its role patterns do not reach these key names. `steel` is comparison-table captions; `link-blue` is every "Learn More ›". |
| P1 | H states | all 40 component entries | Only resting state documented; the file's own blockquote admitted it for hover and said nothing about focus, pressed, disabled or loading. |
| P1 | C sections | Responsive Behavior | The content existed, but nested as `### Responsive Strategy` under Layout, so the required top-level section was absent. |
| P1 | C elevation | Elevation & Depth | Elevation was described but layer separation was never quantified: `canvas` → `canvas-soft` → `panel` → `fog` are 1.03:1–1.09:1 apart and are not reliably distinguishable. |
| P2 | A tokens | `shadow:` group | Prose stated a real value ("0 8px 16px at 10% black") with no token to reference. SPEC section 1 asks for a `shadow:` group in exactly this case. |
| P2 | D typography | `typography.nav` | lineHeight 1.0 at 14px. Legal, and plausible for a single-line nav label, but it is the only role in a 21-role scale with no leading at all. Left as extracted. |
| P2 | E shapes | `rounded` ladder | `xl` 60px, `xxl` 64px, `pill` 100px and `full` 9999px all render as the same pill at these component heights (32–48px), so four tokens encode one visual outcome. Extracted and genuinely referenced by different components, so left alone and not reflowed. |
| P2 | G accessibility | tap targets | Nine components sit at 32px or 40px against a 44px minimum. Not rendered-verified, so recorded as box heights with a prescribed remedy. |
| P2 | A tokens | `text-dim` role | The harness's `text` role pattern `^ink-` swallows `ink-secondary` and `ink-tertiary`, so no `text-dim` can ever resolve for a file using DJI's ink-step naming. Harness issue; see Shared issues. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#00142b"` | Focus ring. DJI Blue driven to its darkest step, so the ring reads as brand, not browser default. 18.50:1 on canvas, and still 3.77:1 drawn **on top of** the `primary` blue pill — no mid-blue ring can do that. Labelled prescribed. |
| frontmatter `colors:` | — -> `focus-on-dark: "#ffffff"` | `focus` measures 1.13:1 on `media-black` and 1.24:1 on `footer`. SPEC section 1 requires a second ring where a file documents both polarities. 21.00:1 and 14.94:1. |
| frontmatter `colors:` | — -> `text-secondary: "#595959"` | Satisfies the `text-dim` role without renaming DJI's own ink-step vocabulary. Same extracted value as `ink-secondary`, stated as an alias in the prose. 7.00:1 on canvas. |
| frontmatter `colors:` | — -> `hairline-strong: "#767676"` | SPEC section 2's parallel accessible token. The six extracted line tones stay frozen and are scoped to decoration; this one is prescribed for the four interactive boundaries. 4.54:1 on canvas. |
| frontmatter | — -> `shadow:` group (`floating`, `none`) | SPEC section 1. The prose already stated the real shadow value with nothing to reference. |
| frontmatter | — -> `motion:` group | Cinematic profile block, verbatim from SPEC section 4, no deviations. |
| Colors → Lines bullet | listed six line tones -> same list plus "all six sit below 2:1 on canvas, decoration only, never the sole signal that something is a control" | Scopes the frozen tones to decoration, per SPEC section 2, without touching a hex. |
| Colors → new `### Focus` | — -> both ring tokens with measured ratios and the two-tone rule over photography | Photography has no measurable colour, so SPEC section 1's two-tone ring applies to the hero and the media tiles. |
| Colors → Ink Secondary bullet | unchanged value -> notes the `text-secondary` alias | Keeps the alias honest: same extracted value, generic role name. |
| Elevation & Depth | "No shadow" / "Soft shadow, 0 8px 16px at 10% black" -> `{shadow.none}` / `{shadow.floating}` + a paragraph quantifying layer separation | Dimension C: one consistent expression per level (flat / outlined / ringed / shadowed, never mixed), plus the honest fact that the three pale layers are not distinguishable. |
| Components → opening note | "No hover states documented." -> "Only resting states were extracted" + a prescribed-states warning | The old line was true but read as a dead end. |
| Components → new `### Interaction States` | — -> 16-row table across all eight states | Dimension H. Static components are grouped in one row that says plainly they have one state. Whole table labelled prescribed. |
| after Components | — -> `## Motion & Animation` | Placed immediately after Components as the brief requires. First line states it is prescribed and unmeasured. 12-row inventory covering hover, press, focus, page transition, modal/drawer, dropdown, toast, list enter, list exit, loading, plus the hero carousel, which is this brand's signature motion. `transform` and `opacity` only; exit always shorter than entrance. |
| Motion → `### Reduced Motion` | — -> `@media (prefers-reduced-motion: reduce)` block | Names what is removed (all travel, scale, stagger, autoplay, Ken Burns ambience, spinner rotation, skeleton pulse) and what remains (opacity fades at `{motion.duration-reduced}` 150ms, and the focus ring, which is never removed). |
| after Motion | — -> `## Accessibility` | Dimension G. 14 passing key pairs, every real failure disclosed with its measured ratio, a per-surface focus-ring table, tap targets, reduced motion, and an explicit "not verified here" list. |
| Layout → `### Responsive Strategy` | full subsection -> one-line pointer; content promoted verbatim to `## Responsive Behavior` | Required top-level section. Moved rather than duplicated, and not reworded. |
| Do's and Don'ts | -> 4 Do and 5 Don't lines added | Motion timing, no-hue-change on state, the focus rule, the boundary rule, the layer rule, and the no-layout-animation rule. |
| end of file | — -> `## Known Gaps` | Nine entries. Separates prescribed from extracted explicitly: motion, states, focus ring, `hairline-strong`, tap targets, dark mode, shadow coverage, logotype names, and the list of things a Markdown file cannot establish. |

No hex that documents the real brand was changed. The four new colour tokens are additions, each labelled prescribed in its frontmatter comment and in the prose.

### Contrast checks

All computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #262626 / `canvas` #ffffff | 15.13:1 | 4.5:1 | pass |
| `ink` / `canvas-soft` #f7f9fa | 14.33:1 | 4.5:1 | pass |
| `ink` / `panel` #f6f8f9 | 14.21:1 | 4.5:1 | pass |
| `ink` / `fog` #f5f5f5 | 13.88:1 | 4.5:1 | pass |
| `ink` / `card-border` #d9d9d9 (harness `surface`) | 10.72:1 | 4.5:1 | pass |
| `text-secondary` = `ink-secondary` #595959 / `canvas` | 7.00:1 | 4.5:1 | pass |
| `ink-secondary` / `card-border` #d9d9d9 | 4.96:1 | 4.5:1 | pass |
| `store-ink` #333333 / `canvas` | 12.63:1 | 4.5:1 | pass |
| `nav-ink` #303233 / `canvas` | 12.89:1 | 4.5:1 | pass |
| `graphite` #3b3e40 / `canvas` | 10.77:1 | 4.5:1 | pass |
| `graphite` / `panel` #f6f8f9 | 10.11:1 | 4.5:1 | pass |
| `slate` #6c7073 / `canvas` | 5.00:1 | 4.5:1 | pass |
| `footer-link` #b3b3b3 / `footer` #272727 | 7.12:1 | 4.5:1 | pass |
| `on-primary` #ffffff / `primary` #0070d5 | 4.91:1 | 4.5:1 | pass |
| `on-primary` / `store-blue` #0060ef | 5.36:1 | 4.5:1 | pass |
| `on-primary` / `footer-pill` #383838 | 11.73:1 | 4.5:1 | pass |
| `tier-orange` #be4e04 / `canvas` | 4.91:1 | 4.5:1 | pass |
| `hairline-strong` #767676 / `canvas` (prescribed) | 4.54:1 | 3.0:1 | pass |
| `focus` #00142b / `canvas` (prescribed) | 18.50:1 | 3.0:1 | pass |
| `focus` / `canvas-soft` #f7f9fa | 17.52:1 | 3.0:1 | pass |
| `focus` / `fog` #f5f5f5 | 16.97:1 | 3.0:1 | pass |
| `focus` / `store-blue-tint` #deeafd | 15.24:1 | 3.0:1 | pass |
| `focus` / `card-border` #d9d9d9 | 13.11:1 | 3.0:1 | pass |
| `focus` / `primary` #0070d5 | 3.77:1 | 3.0:1 | pass |
| `focus` / `store-blue` #0060ef | 3.45:1 | 3.0:1 | pass |
| `focus-on-dark` #ffffff / `footer` #272727 | 14.94:1 | 3.0:1 | pass |
| `focus-on-dark` / `media-black` #000000 | 21.00:1 | 3.0:1 | pass |
| `focus` / `media-black` #000000 | 1.13:1 | 3.0:1 | **fail — which is why `focus-on-dark` exists; `focus` is forbidden on this surface** |
| `focus` / `footer` #272727 | 1.24:1 | 3.0:1 | **fail — same, forbidden on this surface** |
| `hairline` #f0f0f0 / `canvas` | 1.14:1 | 3.0:1 | **fail — extracted, frozen, disclosed** |
| `divider` #e8e8e8 / `canvas` | 1.23:1 | 3.0:1 | **fail — extracted, frozen, disclosed** |
| `dashed-border` #dddddd / `canvas` | 1.36:1 | 3.0:1 | **fail — extracted, frozen, disclosed** |
| `card-border` #d9d9d9 / `canvas` | 1.41:1 | 3.0:1 | **fail — extracted, frozen, disclosed** |
| `input-border` #d4d7d9 / `canvas` | 1.45:1 | 3.0:1 | **fail — extracted, frozen, disclosed** |
| `control-border` #cccccc / `canvas` | 1.61:1 | 3.0:1 | **fail — extracted, frozen, disclosed** |
| `store-blue` #0060ef / `store-blue-tint` #deeafd (`button-store-cart`, 16px/400) | 4.41:1 | 4.5:1 | **fail — extracted, frozen, disclosed** |
| `on-primary` #ffffff / `badge-orange` #fa8c16 (`option-badge`, 12px/600) | 2.38:1 | 4.5:1 | **fail — extracted, frozen, disclosed** |
| `steel` #9fa3a6 / `canvas` (14px spec captions) | 2.54:1 | 4.5:1 | **fail — extracted, frozen, disclosed** |
| `ink-tertiary` #8c8c8c / `canvas` (14px eyebrows) | 3.36:1 | 4.5:1 | **fail — extracted, frozen, disclosed** |
| `ink-tertiary` / `fog` #f5f5f5 | 3.08:1 | 4.5:1 | **fail — extracted, frozen, disclosed** |
| `link-blue` #1890ff / `canvas` (16px links) | 3.24:1 | 4.5:1 | **fail — extracted, frozen, disclosed** |
| `link-blue` / `fog` #f5f5f5 | 2.98:1 | 4.5:1 | **fail — extracted, frozen, disclosed** |
| `error` #f5222d / `canvas` (12px "Out of Stock") | 4.08:1 | 4.5:1 | **fail — extracted, frozen, disclosed** |
| Layer steps: `canvas`→`canvas-soft` 1.06:1, `canvas`→`panel` 1.07:1, `canvas`→`fog` 1.09:1, `canvas-soft`→`fog` 1.03:1 | — | no WCAG minimum | **not distinguishable — stated as such in Elevation & Depth** |

Every failure above is now named with its measured ratio in `## Accessibility`, so `contrast_unresolved` is empty.

### Motion inventory

Cinematic profile, used verbatim. Prescribed, not extracted.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover — pills, links, option cards | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity`; `scale(1.01)` on option cards | opacity only at 150ms; scale removed |
| Hover — product tile render | `{motion.duration-slow}` 600ms | `{motion.ease-standard}` | `scale(1.02)` on the render only; type never moves | no scale; tile static |
| Press — any pill, card, toggle | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `scale(0.98)`, 0.96 on circle buttons and stepper cells | no scale; press reads from the hover opacity |
| Focus-visible | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` on the ring | unchanged — already under the 150ms ceiling, and the ring never animates its size |
| Page / route transition | 400ms in, 240ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(12px)` on the first block | cross-fade at 150ms, no travel |
| Hero carousel slide | `{motion.duration-emphasis}` 900ms | `{motion.ease-enter}` | `opacity` cross-fade + `scale(1.04 → 1.0)` Ken Burns; title arrives 160ms late | cross-fade at 150ms, no scale, no stagger; autoplay stops |
| Modal / drawer | 400ms in, 240ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | scrim `opacity`; `translateX(100%)` drawer, `scale(0.98 → 1.0)` modal | fade only at 150ms; no slide, no scale |
| Dropdown | 240ms in, 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(-6px → 0)` | opacity only at 150ms |
| Toast | 400ms in, 240ms out, 5s dwell | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px → 0)` | opacity only at 150ms; dwell unchanged |
| List enter | 400ms per item, 80ms stagger, capped at 6 | `{motion.ease-enter}` | `opacity` + `translateY(16px → 0)` | all items fade together at 150ms; no stagger, no travel |
| List exit | 240ms, no stagger | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | opacity only at 150ms |
| Loading | 900ms linear spinner loop; skeleton pulse over 900ms | linear / `{motion.ease-standard}` | `rotate()` spinner; `opacity` skeleton | static glyph + text status; one flat `{colors.fog}` box, no pulse |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 31 (`REQUIRED_COLOR_ROLES["text"]`) | The pattern `^ink-` sits in the **text** role, so `ink-secondary` and `ink-tertiary` are consumed as primary text and `text-dim` resolves to nothing. Every file using an ink-step naming scheme loses a token point for a role it actually defines. I worked around it with a `text-secondary` alias, which is a token this file does not strictly need. | Move `^ink-` from the `text` list to the `text-dim` list; `^ink$` already covers primary ink. |
| `theme-audit/audit.py` line 35 (`REQUIRED_COLOR_ROLES["surface"]`) | `^card-` appears in the **surface** role, so this file's `card-border` #d9d9d9 — a 1px line — is used as the representative surface for `text on surface`, `text-dim on surface` and `focus on surface`. The checks happen to pass here, but they are measuring text against a border colour, and `panel` #f6f8f9 (a real surface) is never reached because it is later in the pattern order. | Narrow to `^card-(bg|background|surface|fill)` or drop `^card-`, and move `^panel$` ahead of the card patterns. |
| `theme-audit/audit.py` `check_all` (lines ~196–210) | `check_all` only iterates tokens whose names match a role pattern, so genuine text failures under brand-specific names are invisible: `steel` (2.54:1), `link-blue` (3.24:1) and `error` (4.08:1) were never flagged, while two decorative hairlines were. The harness is systematically stricter on decoration than on text. | Check every colour token the `components:` block uses as a `textColor`, regardless of its name — the component pass already dereferences these, so the data is already there. |
| `theme-audit/audit.py` score for `tokens` (line ~309) | `focus` and `focus-on-dark` collapse into one role, so a file that correctly ships two rings scores the same as one shipping a single ring that fails on half its surfaces. | Where a file defines a dark surface more than 7:1 from canvas, require the `focus-on-dark` variant and score it separately. |
| `README.md` | The collection's token-contract description predates `motion` and `shadow` and lists neither, so a contributor copying README's shape produces a file that fails SPEC sections 1 and 4 immediately. | Add `motion` and `shadow` to README's required-group list, with a pointer to `theme-audit/SPEC.md` sections 1 and 4. |
| `CONTRIBUTING.md` | No rule separating extracted values from prescribed ones — now the single most important distinction in these files, since motion, interaction states and focus rings are all prescribed. | Require that any value not read off the live site carries an inline `PRESCRIBED` marker and a matching Known Gaps entry. |

### Needs approval

Each item is a real extracted brand value that fails AA. Nothing was changed; the failure is disclosed in the file instead.

1. **`option-badge` — white on `badge-orange` #fa8c16, 2.38:1 (needs 4.5:1 at 12px/600).** The worst failure in the file. Nearest passing options: keep the orange and set the label in `{colors.ink}` #262626, measuring **6.36:1**, which preserves the badge colour exactly; or, if the label must stay white, darken the fill to **#9a5100** (5.91:1), which is no longer DJI's orange. Recommend the ink label. Usage note that would make the real value defensible: none — there is no text size at which 2.38:1 passes.
2. **`button-store-cart` — `store-blue` #0060ef on `store-blue-tint` #deeafd, 4.41:1 (needs 4.5:1).** Fails by 0.09. Nearest passing value: **#0056d6** for the label only, 5.24:1 on the tint. The alternative usage note — confine the pair to 18.66px/700 or larger, where 3:1 applies — would be false here, since the extracted type is 16px/400. Recommend approving #0056d6 as a label-only prescribed variant, leaving `{colors.store-blue}` untouched for the Buy Now fill, the selection ring and the care tag.
3. **`steel` #9fa3a6 on canvas, 2.54:1 (needs 4.5:1).** Comparison-table spec captions at 14px/400. Nearest passing value: **#767676** (4.54:1), i.e. the new `{colors.hairline-strong}` tone. No defensible usage note exists: even the large-text 3:1 threshold is not met.
4. **`ink-tertiary` #8c8c8c on canvas, 3.36:1 (needs 4.5:1).** 14px tile eyebrows. Nearest passing value: **#767676** (4.54:1). Usage note that would make the real value defensible: restrict `{colors.ink-tertiary}` to 24px+, or 18.66px+ at weight 700, where 3:1 applies — it clears that at 3.36:1. The eyebrows are 14px today, so the note requires a type change, not just a note.
5. **`link-blue` #1890ff on canvas, 3.24:1 (needs 4.5:1), and 2.98:1 on `fog`.** Every "Learn More ›" and "Buy Now ›" text link at 16px. Nearest passing value already in the palette: **`{colors.primary}` #0070d5** at 4.91:1, which would collapse three blues to two — arguably an improvement, but it changes the brand's link colour, so it needs a decision rather than an edit.
6. **`error` #f5222d on canvas, 4.08:1 (needs 4.5:1).** 12px "Out of Stock". Nearest passing value: **#e01020** (4.92:1). Low risk, since the text itself carries the meaning, but colour is currently the only other signal.
7. **The four interactive boundaries — `card-border` 1.41:1, `dashed-border` 1.36:1, `input-border` 1.45:1, `control-border` 1.61:1 (all need 3.0:1).** I prescribed `{colors.hairline-strong}` #767676 (4.54:1) for these four in the prose but did **not** change the four extracted tokens or the component entries that reference them. Swapping `option-card`, `quantity-stepper`, the checkbox and the store email field onto `hairline-strong` would visibly change DJI's chrome, so it needs approval.
8. **`focus` #00142b, `focus-on-dark` #ffffff and `hairline-strong` #767676 are all invented.** DJI ships no documented focus ring and no 3:1 boundary. These are prescriptions consistent with the brand, not observations, and are labelled as such in the frontmatter, the Colors section and Known Gaps.

### Identity verdict

Still unmistakably DJI, and the Cinematic assignment is right.

The profile holds on SPEC section 5's first rule without needing an argument: hardware-flagship drones and cameras, a full-height hero carousel of a single product, square gutter-separated studio renders, sparse tightly-tracked Open Sans, and colour withheld from everything except the action pill. The white canvas is exactly the case SPEC calls out — a white-canvas premium brand is still cinematic; the tell is the full-bleed photography and the slow reveal, not a dark background. The motion is built around that: the hero image takes the 900ms `duration-emphasis` with a slow Ken Burns drift, the slide title arrives 160ms after the photograph has begun to settle, and the product render — not the type — is the thing that scales on hover. Under Crisp the carousel would snap and the showroom would read as a dashboard.

What keeps the file from drifting into a token dump: the new material names DJI's own components throughout rather than generic ones (`purchase-bar`, `option-card`, `media-toggle`, `tier-eyebrow`, `care-tag`, `button-hero-ghost`), and the two hardest decisions are both brand-driven. The focus ring is DJI Blue driven dark rather than a generic blue, chosen specifically so it survives being drawn on top of a DJI Blue pill. The no-hue-change rule on hover and press exists because this brand has exactly one action colour per surface, which is the file's own strongest stated principle.

One piece of pre-existing drift I neither introduced nor removed: the ten `ex-*` example entries in the frontmatter and the matching Examples subsection carry descriptions borrowed from another file in the collection — "fashion / DTC variant selector", "DTC / fashion brand actual cart chrome", and `ex-data-table-cell` claiming "mono-caps eyebrow typography" and "body-sm" when this file defines neither a mono face nor a `body-sm` role. DJI sells drones; nothing on the site is fashion DTC. They are illustrative kit surfaces rather than extracted DJI components, and rewriting them sat outside what the brief asked me to fix, so I left them. They are the only part of the file that would suit any site.
