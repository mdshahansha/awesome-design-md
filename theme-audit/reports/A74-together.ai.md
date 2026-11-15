## A74 · together.ai

Scores before -> after (1-5), from the harness: tokens 3 -> 4 · refs 5 -> 5 · contrast 2 -> 4 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 5

Harness command: `python3 -I theme-audit/audit.py --site together.ai --json`. Every ratio below was computed with a WCAG 2.1 relative-luminance snippet (`python3 -I`, stdlib only); none is estimated.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Nothing in the file said anything about timing. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section. The brand fails AA in three separate places and the document disclosed none of them. |
| P0 | A/B · Tokens, colour | `colors.hairline` | Frontmatter carried `hairline: "#959494"` — a byte-for-byte duplicate of `{colors.body}` — while the prose stated `#ebebeb` twice and every component border is the literal `rgba(0, 0, 0, 0.08)`, which composites over `#ffffff` to exactly `#ebebeb`. The `border` role was therefore being measured at 3.03:1 against a hex the site never draws as a hairline; the real boundary is 1.19:1. Two distinct facts were collapsed onto one key. |
| P0 | A/E · Focus | whole file | No `focus` role, no ring of any kind, no statement of focus behaviour on either surface polarity — and the file documents both a white canvas and a near-black hero band. |
| P1 | H · States | all 24 components | Zero states documented. The harness found only `active`, incidentally, in an `ex-app-shell-row` description. Nothing named hover, focus-visible, pressed, disabled, loading, selected or error. |
| P1 | C · Sections | `## Responsive Behavior` | Existed only as `### Responsive Strategy` inside Layout, with `####` children — a depth below every peer section. |
| P1 | C · Sections | `## Known Gaps` | Absent. Nothing recorded which values were extracted and which were inferred. |
| P1 | A · Tokens | `#26263a` | The Colors prose named a distinct "Hairline on Dark" tone at `#26263a` but bound it to `{colors.surface-dark-soft}`, whose value is `#313641`. The reference resolved, so the harness saw nothing, but the document asserted a tone it had no token for. |
| P1 | B · Colour | `nav-link` | Declared `textColor: {colors.on-dark}` with no ground, so the harness composited it over the canvas and reported white on white at 1.0:1. The prose states plainly that the link row sits inside `nav-bar` on `{colors.canvas-dark}`: a manufactured failure caused by a missing binding. |
| P1 | B · Colour | Colors prose | Self-contradictory bullets: `{colors.body}` documented as `#999999` (frontmatter: `#959494`), two separate bullets both titled "Hairline", and a third labelled "Hairline / Canvas Soft" for the same key. |
| P1 | H · Components | `badge-neutral` | Prose said the fill is `{colors.hairline}`; the components block says `{colors.canvas}`. One of the two had to be wrong. |
| P2 | C · Elevation | Elevation Level 2 | Pointed the on-dark hairline at `{colors.surface-dark-soft}` (a card fill), not at a boundary token. Elevation is otherwise expressed consistently — hairline-and-polarity, with exactly one documented shadow reserved for the floating orb — so the ladder itself is sound. |
| P2 | E · Shapes/spacing | `rounded.xs` 3.25px, `spacing.6xl` 55.2px | Both sit off the 4 px ladder. Extracted, so kept; now recorded in Known Gaps rather than left looking like errors. |
| P2 | A · Tokens | `ex-*` block | The auto-derived examples still carry "`TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass" although no marker remains. Harmless, but it reads as unfinished machinery inside a brand document. |
| P2 | D · Typography | `caption`, `caption-strong` | Alone among the roles they omit `letterSpacing` where the Hierarchy table states `0`. Every role does carry size, weight and line height, so the contract holds; this is a cosmetic asymmetry and was left alone. |

Dimension D, for the record: body text is readable on every surface the file actually renders — `{colors.ink}` on `{colors.canvas}` 21:1, on `{colors.hairline}` 17.62:1, `{colors.on-dark}` on `{colors.canvas-dark}` 20.46:1 and on `{colors.surface-dark-soft}` 12.11:1. The readability problem is confined to the one muted ink.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | `hairline: "#959494"` -> `hairline: "#ebebeb"` | The prose states `#ebebeb` twice and `rgba(0, 0, 0, 0.08)` over `#ffffff` composites to exactly `#ebebeb` (255 × 0.92 = 234.6). `#959494` was a copy of `{colors.body}`, which is itself the 42 % black pre-blend. Declaring the value the file already asserts, not inventing one. |
| frontmatter `colors` | — -> `hairline-on-dark: "#26263a"` | A binding the prose already asserted and had no token for. |
| frontmatter `colors` | — -> `focus: "#000000"`, `focus-on-dark: "#ffffff"` | Both hexes the palette already owns (`{colors.ink}` / `{colors.on-dark}`). Together AI's signal colour *is* its ink and the file forbids reducing the gradient to one swatch, so SPEC section 1's monochrome case applies: brand ink and paper with a mandatory 2 px offset of the opposite polarity, drawn outside the control. Two rings, because the file documents both polarities. |
| frontmatter | — -> `motion:` group | The **Crisp** profile's block from SPEC section 5, verbatim, no deviation. |
| frontmatter `components.nav-link` | — -> `backgroundColor: "{colors.canvas-dark}"` | Declares the ground the prose already states, so the pair measures where it renders (20.46:1) instead of as white-on-white. |
| `## Colors` → Surface / Text | Merged the duplicate "Hairline" bullets; `#999999` -> `#959494`; "Hairline on Dark" repointed to `{colors.hairline-on-dark}` | Removed the internal contradictions and put each tone's measured ratio beside it. |
| `## Colors` | — -> `### Focus` | States which existing tones the rings reuse, the offset, and the measured ratio on every surface, so nobody mistakes either for a new brand colour. |
| `## Components` (all 24 entries) | — -> a `States:` line per entry | Each entry now names its states; the genuinely two-state surfaces (`testimonial-card`, `stats-card-tinted`, `badge-subtle-on-dark`, `footer-wordmark-banner`, the two dark bands) say so explicitly. Hover and press are paint-only, which SPEC section 6 permits and which is the honest hover state for a near-monochrome brand. |
| `## Components` → `text-input`, `button-outline` | — -> the 1.19:1 boundary named, with `{colors.body}` (3.03:1) recommended for control boundaries | SPEC section 2, step 1: the palette already owns a passing tone, so nothing was added. The frozen `rgba(0, 0, 0, 0.08)` bindings are untouched. |
| `## Components` → `badge-neutral` | Prose fill `{colors.hairline}` -> `{colors.canvas}` | Aligned to the components block, which is the contract. Flagged under Needs approval. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. 13-row interaction table (hover, press, focus, page transition, modal/drawer, dropdown, toast, list enter, list exit, loading, plus ribbon ambience, tab indicator, nav polarity flip), `transform`/`opacity` only for movement, paint-only for recolour, every exit shorter than its entrance, and a `@media (prefers-reduced-motion: reduce)` block stating what is removed and what remains. |
| after Motion | — -> `## Accessibility` | 16-row measured contrast table, the three real AA failures named plainly with ratios and nearest passing values, focus-ring visibility on all six surfaces the file defines, the tap-target target labelled as prescribed and unverifiable, colour-never-alone, and reduced motion. |
| Layout `### Responsive Strategy` | Moved verbatim to top-level `## Responsive Behavior` after Do's and Don'ts; `####` children promoted to `###` | SPEC section 3: move, never duplicate. Not one word of the content changed. |
| end of file | — -> `## Known Gaps` | Records the unfilled `text-dim` role and its evidence, the hairline reconciliation, that all motion and both rings are prescribed, the absent semantic palette, the two off-ladder values, and that nothing in the file is rendered. |
| `## Elevation & Depth` Level 2 | `{colors.surface-dark-soft}` -> `{colors.hairline-on-dark}` | A boundary token for a boundary row. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#000000` / `canvas` `#ffffff` | 21:1 | 4.5:1 | Pass |
| `ink` `#000000` / `hairline` `#ebebeb` | 17.62:1 | 4.5:1 | Pass |
| `ink` `#000000` / `accent-mint` `#c8f6f9` | 18.01:1 | 4.5:1 | Pass |
| `ink` `#000000` / `accent-periwinkle` `#bdbbff` | 11.72:1 | 4.5:1 | Pass |
| `on-dark` `#ffffff` / `canvas-dark` `#010120` | 20.46:1 | 4.5:1 | Pass |
| `on-dark` `#ffffff` / `surface-dark-soft` `#313641` | 12.11:1 | 4.5:1 | Pass |
| `on-primary` `#ffffff` / `primary` `#000000` | 21:1 | 4.5:1 | Pass |
| `body` `#959494` / `canvas` `#ffffff` | 3.03:1 | 4.5:1 | **Fail — extracted, frozen, disclosed** |
| `body` `#959494` / `hairline` `#ebebeb` (`data-table-header`) | 2.54:1 | 4.5:1 | **Fail — extracted, frozen, disclosed** |
| `hairline` `#ebebeb` / `canvas` `#ffffff` | 1.19:1 | 3:1 | **Fail — extracted, frozen, disclosed** |
| `hairline-on-dark` `#26263a` / `canvas-dark` `#010120` | 1.38:1 | 3:1 | **Fail — extracted, frozen, disclosed** |
| `accent-orange` `#fc4c02` / `canvas` `#ffffff` | 3.4:1 | 3:1 non-text | Pass as boundary/icon; fails as text — scoped accordingly |
| `accent-magenta` `#ef2cc1` / `canvas` `#ffffff` | 3.62:1 | 3:1 non-text | Gradient leg only, never a text colour |
| `accent-periwinkle` `#bdbbff` / `canvas` `#ffffff` | 1.79:1 | — | Fill only |
| `accent-mint` `#c8f6f9` / `canvas` `#ffffff` | 1.17:1 | — | Fill only |
| `focus` `#000000` / `canvas` `#ffffff` | 21:1 | 3:1 | Pass |
| `focus` `#000000` / `hairline` `#ebebeb` | 17.62:1 | 3:1 | Pass |
| `focus` `#000000` / `accent-mint` `#c8f6f9` | 18.01:1 | 3:1 | Pass |
| `focus` `#000000` / `accent-periwinkle` `#bdbbff` | 11.72:1 | 3:1 | Pass |
| `focus-on-dark` `#ffffff` / `canvas-dark` `#010120` | 20.46:1 | 3:1 | Pass |
| `focus-on-dark` `#ffffff` / `surface-dark-soft` `#313641` | 12.11:1 | 3:1 | Pass |
| `body` `#959494` / `surface-dark-soft` `#313641` | 4.0:1 | 4.5:1 | Fail — pairing not used by the brand; documented as forbidden |
| `ink` `#000000` / `ink` `#000000` ("body text on surface") | 1.0:1 | 4.5:1 | **Manufactured by the harness — cannot render. See Shared issues.** |

Elevation layers (dimension C), measured: `canvas` → `hairline` 1.19:1, `canvas` → `canvas-dark` 20.46:1, `canvas-dark` → `surface-dark-soft` 1.69:1. The light-side step is the brand's own near-invisible one; the layers that carry real separation are the polarity flip and the hairline, and elevation is expressed one way throughout — boundary plus polarity, with a single documented shadow reserved for the floating orb.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, nav links, table rows, cards) | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `background-color`, `color`, `border-color`, `opacity` — paint only | Unchanged; already travel-free |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity`, `background-color`; no scale | Unchanged |
| Focus-visible ring | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on the 2 px ring | Appears instantly, no fade |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | `opacity` on the content band | Opacity only at `{motion.duration-reduced}` |
| Modal / drawer | `{motion.duration-base}` in / `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px → 0)`; scrim `opacity` | Opacity only at `{motion.duration-reduced}`, no translate |
| Dropdown / menu | `{motion.duration-fast}` in / `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(4px → 0)` | Opacity only at `{motion.duration-reduced}`, no translate |
| Toast | `{motion.duration-fast}` in / `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: translateY(8px → 0)` | Opacity only at `{motion.duration-reduced}`, no translate |
| List enter | `{motion.duration-base}` per item, `{motion.stagger-step}` 20ms, capped at 8 | `{motion.ease-enter}` | `opacity` + `transform: translateY(6px → 0)` | No stagger, no translate; one fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity` 1 → 0, no stagger | Opacity only at `{motion.duration-reduced}` |
| Loading | `{motion.duration-slow}` 220ms skeleton loop; spinner 800ms/turn | `{motion.ease-standard}` / linear | `opacity` pulse; `transform: rotate()` | Static `{colors.hairline}` block; spinner replaced by a mono-caps "LOADING…" label |
| Gradient ribbon ambience (declared) | 20s loop | `{motion.ease-standard}` | `transform` only | Frozen on frame one |
| Tab / toggle indicator | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `transform: translateX()` | Indicator jumps; label colour fades at `{motion.duration-reduced}` |
| Nav polarity flip on scroll | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | `background-color` + `color` | Unchanged; paint-only |

No extracted timing exists for this brand, so nothing displaces a profile value. The only non-token timings are the 20 s ribbon ambience and the 800 ms spinner turn, both labelled prescribed.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 25-26 (`REQUIRED_COLOR_ROLES["text"]`) and 29-33 (`["text-dim"]`) | `^body$` sits in the **text** pattern list, and the `text-dim` list accepts only `^body-(soft\|muted\|secondary)$`. In a file that names its primary ink `ink` and its muted ink `body`, `text` resolves to `ink` and the muted tone is never offered to `text-dim`, which then reports as missing. The palette plainly contains the role. Five files in this audit are reported to show the same pattern. | Add `^body$` to the `text-dim` patterns, after the `text` role has taken its representative: where a file owns both an `^ink` token and `body`, resolve `text=ink` and `text-dim=body`. Cheaper alternative: resolve `text-dim` from the muted ink a component binds as `textColor` on the canvas, as the `border` role already does from `borderColor`. |
| `theme-audit/audit.py` lines 296-330 (surface resolution) | `surface` resolves to **`ink`** `#000000` for this file. The elected ground comes from `ex-pricing-tier-featured`, an auto-derived demonstration surface, and it is the same token the `text` role resolved to — so `check("text", "surface")` compares `ink` against `ink` and reports "body text on surface" failing at 1.0:1. The pair cannot render: no element in the file paints black ink on a black fill, and that component's own `textColor` is `{colors.on-primary}` (white on black, 21:1). It is this file's one remaining undisclosed failure and it is manufactured, which is why it is not disclosed in the document: disclosing it would assert a defect the brand does not have. The token it should have picked is `{colors.hairline}` `#ebebeb` — the file's only soft raised tone, 17.62:1 against ink — or `{colors.canvas}`, since this brand paints its light cards the page colour and separates them with a hairline. | Two guards: (a) never elect a ground identical to the resolved `text` token, and skip any pair whose foreground and background are the same key; (b) exclude `ex-*` auto-derived example components from role election, or prefer a bound ground whose component also declares a `textColor`, which gives the pair that actually renders. |
| `theme-audit/audit.py` lines ~426-430 (`theme_of`) | The dark-polarity marker alternation includes bare `ink`, so in a light-canvas file the token `ink` is classified as a dark-theme tone and `same_theme("ink", "canvas")` is false. The result is that `text` on `canvas` — the first row of SPEC section 2's table — is silently **never checked** in any file whose primary ink is called `ink`. Benign here (21:1) but it suppresses the most important check in the spec, and would hide a genuine failure elsewhere. | Remove bare `ink` from the marker alternation and match only compounds (`ink-dark`, `dark-ink`). A token named for ink is a text tone, not a theme. |
| `theme-audit/audit.py` focus coverage, lines ~595-616 | `surface_keys` admits any token a `CONTAINER`-named component binds as `backgroundColor`, including `{colors.accent-mint}` via `stats-card-tinted` — a static display tile with no interactive child. A ring is then required to clear 3:1 against a fill nothing is ever focused over. Both of this file's rings happen to clear it, so nothing was hidden here; the cost falls on brands whose tints are lighter. | Admit a bound fill as a ring ground only where the component (or a child it declares) carries an interactive state — otherwise a decorative tile sets the ring's budget. |

### Needs approval

1. **`{colors.body}` `#959494` as secondary text — 3.03:1 on `{colors.canvas}`, required 4.5:1.** Extracted; not changed. Nearest passing value on white: **`#767676` (4.54:1)**. The usage note that would make the real value defensible: it clears the 3:1 large-text bar, so it is acceptable at **≥ 24 px, or ≥ 18.66 px bold**. Every current use is below that — 14 px captions, 11 px mono eyebrows, pricing-table cell values — so as drawn today the brand fails AA for secondary text.
2. **The same ink on `{colors.hairline}` `#ebebeb` — 2.54:1, required 4.5:1.** This is `data-table-header`, the row that labels the price columns, set at 11 px uppercase mono. No usage note rescues 2.54:1 at 11 px. Nearest passing value on that ground: **`#666666` (4.82:1)**; `#6a6a6a` is the break-even point. The alternative is to repaint the header labels in `{colors.ink}` (17.62:1), which would change the brand's look.
3. **Re-binding the frozen control boundaries.** `text-input` and `button-outline` keep their extracted `rgba(0, 0, 0, 0.08)` → `#ebebeb` border at 1.19:1, which is the control's only boundary. The document recommends `{colors.body}` `#959494` (3.03:1) for control boundaries and scopes `#ebebeb` to decoration in prose, but the component bindings are untouched. A brand owner should decide whether the real inputs get the stronger boundary.
4. **Which hairline hex is authoritative.** The token is now `#ebebeb`, on the strength of the prose plus the exact `rgba(0, 0, 0, 0.08)` composite. If the extraction that produced `#959494` was reading a real element, that element needs identifying — but as it stands `#959494` was indistinguishable from `{colors.body}` and documented two different jobs with one value.
5. **`badge-neutral` fill.** Prose said `{colors.hairline}`, the components block says `{colors.canvas}`. The prose was aligned to the block. If the live badge is actually the soft grey, the block is the thing to correct.
6. **Both focus rings are prescribed**, including the 2 px width and 2 px offset. If the live site has a real focus treatment, it should displace this.

### Identity verdict

Still unmistakably Together AI, and in two places more so than before. The file's identity rests on four things — the black-pill CTA, the alternating navy/white band rhythm, the two-face split of geometric display sans against uppercase mono, and the one three-stop gradient that is the entire decorative system — and none of them was touched. The additions were argued from inside that identity rather than bolted on: the focus rings are the brand's own ink and paper, chosen *because* the brand's signal colour is its ink and because the file's own Don'ts forbid reducing the gradient to a single swatch, which rules out the obvious chromatic ring; the hover and press states are paint-only, because a scale pop would contradict a system whose only moving part is one ribbon; the error state borrows `{colors.accent-orange}` with mandatory text, since the brand genuinely has no semantic palette rather than one this audit could invent.

**Crisp is the right profile and is kept.** SPEC section 5's rule 2 fires squarely: this is infra and developer tooling — serverless inference, GPU clusters, a pricing table that "reads more like a sheet than a marketing component", a code-editor mockup in the product band, and a label voice of "ON-DEMAND" / "GA-DEC '25". There is no full-bleed photography and no slow reveal, so rule 1 does not apply; the three-colour gradient is saturated but appears on exactly one non-interactive hero graphic and never on a control, which is the distinction rule 3 asks for, and the type voice is sober at weight 500 sentence case. The one argument for Cinematic would be the 64 px hero and the gradient ribbon — but the ribbon is the only thing in the system that moves at all, which is why it is the single declared ambience in an otherwise 100-150 ms file.

The risk of drift is the `ex-*` example block, which is auto-derived boilerplate shared across the collection and reads as borrowed because it is; it was left verbatim and labelled in Known Gaps as machinery rather than evidence.
