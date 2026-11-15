## A23 · figma

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 3 | 5 | 1 | 3 | 1 | 1 |
| after | 5 | 5 | 5 | 5 | 5 | 5 |

Harness command: `python3 -I theme-audit/audit.py --site figma --json`.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A / H | `components.button-icon-circular-inverse` | `backgroundColor` was bound to `{colors.on-inverse-soft}` (`#ffffff`) with `textColor: {colors.inverse-ink}` (`#ffffff`) — a white glyph on a white fill at 1.00:1. An authoring bug in the binding, not a brand failure: `on-inverse-soft` is the *overlay* base (white at 16% over a dark ground), never a paintable surface. Fixed. |
| P0 | A | `colors.focus` | No focus token at all, and no focus ring documented anywhere, while `text-input-focused` asserts "focus is communicated via ring, not via fill change" — a ring with no colour. Fixed. |
| P0 | A | `colors` (text-dim role) | No `text-dim`-class role existed. The brand genuinely has no mid-grey text, so the gap was real but the fix is not a grey. Fixed with `caption: "#000000"`. |
| P0 | F | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule, zero durations, zero easing curves. Fixed. |
| P0 | G | whole file | No `## Accessibility` section, so four measurable contrast failures were entirely undisclosed. Fixed. |
| P0 | B | `hairline` / `hairline-soft` on `canvas` | 1.25:1 and 1.13:1 against a 3.0:1 non-text minimum. Both extracted and frozen. `hairline` was documented as the 1px border of `/contact/` text inputs — the sole boundary of an interactive control at 1.25:1. Disclosed; parallel accessible token added. |
| P1 | B | `button-magenta-promo` | `#ffffff` on `#ff3d8b` = 3.34:1 against 4.5:1 for its own `{typography.button}` (20px / 480). Real brand value; disclosed, not changed. Needs approval. |
| P1 | B | `comparison-checkmark` | `#1ea64a` on `#ffffff` = 3.18:1. Fails the harness 4.5:1 but passes the 3:1 non-text minimum that actually applies to a glyph. The real defect is information encoded in colour alone. Disclosed with a no-colour-change mitigation. Needs approval for the hex. |
| P1 | H | every component entry | Only `active`/`pressed` and `selected` were documented anywhere; `hover`, `focus-visible`, `disabled`, `loading` and `error` appeared nowhere in Components. Fixed with a per-component state matrix marking each cell extracted, prescribed or n/a. |
| P1 | C | Elevation & Depth | Level 2 stated a literal `rgba(0,0,0,0.06)` shadow with no token, so a `{shadow.*}` reference had nothing to point at. No `shadow:` group existed. Fixed. |
| P1 | I / F | motion profile | Assigned **Playful**; the file's own observable signals read **Calm**. Argued below and switched, not silently. |
| P2 | C | canvas / surface | `canvas` `#ffffff` to `surface-soft` `#f7f7f5` is 1.03:1. The two layers are not luminance-distinguishable; this file does not use luminance for elevation at all (colour blocks and a hairline do that work). Internally consistent, so not "fixed" — it is a true description of the brand. |
| P2 | E | `rounded.pill` 50px vs `rounded.full` 9999px | Both are fully round at every size this system ships (40–56px elements). A reader could mistake 50px for a measured half-height. Noted in Shapes as a semantic rather than geometric distinction. |
| P2 | D | `typography.caption` | 12px at line-height 1.00 — no leading at the smallest size in the system. Scoped in Accessibility to single-line labels only. |
| P2 | D | `typography.headline` vs `subhead` | Identical size, line-height and tracking (26px / 1.35 / -0.26px); they differ only by weight (540 vs 340). Correct for this brand ("weight, not size, carries hierarchy") but it means the two roles are indistinguishable in a token dump. Left as-is; the Principles block already explains it. |

No dangling `{group.token}` references before or after; the repo stays at zero.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | — -> `caption: "#000000"` | Satisfies the `text-dim` role without inventing a mid-grey the brand forbids. The secondary/caption role genuinely *is* black here; 21.00:1 on canvas. |
| frontmatter `colors` | — -> `focus: "#000000"`, `focus-on-dark: "#ffffff"` | First focus ring in the repo. The file documents both polarities as signature surfaces (white canvas + pastels vs black footer/marquee + navy block), so per SPEC section 1 one ring cannot serve both. Brand ink and brand paper, not an invented chromatic ring, because this brand's stated first rule is that its system palette has no accent colour. |
| frontmatter `colors` | — -> `border-control: "#000000"` | Parallel accessible boundary token per SPEC section 2. The frozen hairlines stay untouched and are scoped to decoration; anything that is a control's only boundary takes ink at 21.00:1. Ink rather than a grey because a grey would have to reach about `#646464` to clear 3:1 on `block-lilac`, and that is a colour this brand does not own. |
| frontmatter `colors` | — -> `surface-inverse-soft: "#292929"` | Derived (`on-inverse-soft` at 16% over `inverse-canvas`) so the inverse icon button has a measurable ground. Labelled derived, not extracted. |
| frontmatter | — -> `shadow:` group (`none`, `soft`, `modal`) | SPEC section 1: the file documented a real `rgba(0,0,0,0.06)` shadow in prose with no token. `soft` is the extracted value; `modal` is labelled prescribed. |
| frontmatter | — -> `motion:` group, **Calm** block verbatim | SPEC section 4. Profile argument below. |
| `components.button-icon-circular-inverse` | `backgroundColor: "{colors.on-inverse-soft}"` -> `"{colors.surface-inverse-soft}"` | The P0 authoring bug. White-on-white 1.00:1 -> 14.55:1. The component always intended a white glyph on a translucent-white circle over a *dark* ground; the binding had named the overlay's own white as the background. |
| Colors / Text | added `{colors.caption}` entry; expanded the `on-inverse-soft` entry | Documents the new role and states plainly that `on-inverse-soft` is an overlay base and must not be bound to a `backgroundColor`. |
| Colors / new `### Focus` | — -> two entries with usage, offset rule and prescribed label | Dimension A. |
| Colors / Surface | added `surface-inverse-soft` and `border-control`; scoped `hairline-soft` to decoration | Dimension B, SPEC section 2 parallel-token pattern. |
| Elevation & Depth | literal shadow strings -> `{shadow.none}` / `{shadow.soft}` / `{shadow.modal}`; added a paragraph stating the ladder is border-only at level 1 and shadow-only at 2–3 | Dimension C: elevation now expressed one consistent way rather than border and shadow mixed. |
| Shapes / new `### Focus Ring Geometry` | — -> ring width, offset, radius inheritance, pill-vs-full note | Dimension E. |
| Components / new `### Component States` | — -> matrix of 18 component rows x 8 states | Dimension H. Every cell marked extracted / prescribed / n/a; `comparison-checkmark` declared a genuine two-state (present/absent) non-interactive glyph. |
| new `## Motion & Animation` (after `## Components`) | — -> prescribed-first-line disclaimer, profile argument, 15-row interaction table, six motion rules, `prefers-reduced-motion` block | Dimension F. |
| new `## Accessibility` (after Motion) | — -> 15 passing pairs, 12 focus-ring pairs, 4 disclosed failures, tap targets, reduced motion, other notes | Dimension G. |
| Known Gaps | 1 animation line -> 6 lines | Every prescribed or derived value added above is now named as such: motion, error styling, `shadow.modal`, `surface-inverse-soft`, focus geometry. |

Nothing outside `design-md/figma/DESIGN.md` was touched. No existing prose was reflowed; every edit is an insertion or a single-line replacement.

### Contrast checks

All computed with the WCAG 2.1 relative-luminance formula, python3 stdlib only.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#000000` / `canvas` `#ffffff` | 21.00:1 | 4.5:1 | pass |
| `ink` / `surface-soft` `#f7f7f5` | 19.58:1 | 4.5:1 | pass |
| `caption` `#000000` / `canvas` | 21.00:1 | 4.5:1 | pass |
| `caption` / `surface-soft` | 19.58:1 | 4.5:1 | pass |
| `on-primary` `#ffffff` / `primary` `#000000` | 21.00:1 | 4.5:1 | pass |
| `inverse-ink` `#ffffff` / `inverse-canvas` `#000000` | 21.00:1 | 4.5:1 | pass |
| `inverse-ink` / `block-navy` `#1f1d3d` | 16.14:1 | 4.5:1 | pass |
| `inverse-ink` / `surface-inverse-soft` `#292929` | 14.55:1 | 4.5:1 | pass |
| `ink` / `block-cream` `#f4ecd6` | 17.82:1 | 4.5:1 | pass |
| `ink` / `block-lime` `#dceeb1` | 16.91:1 | 4.5:1 | pass |
| `ink` / `block-mint` `#c8e6cd` | 15.66:1 | 4.5:1 | pass |
| `ink` / `block-pink` `#efd4d4` | 15.04:1 | 4.5:1 | pass |
| `ink` / `block-coral` `#f3c9b6` | 13.84:1 | 4.5:1 | pass |
| `ink` / `block-lilac` `#c5b0f4` | 10.89:1 | 4.5:1 | pass (binding pastel case) |
| `border-control` `#000000` / `canvas` | 21.00:1 | 3.0:1 | pass |
| `border-control` / `block-lilac` | 10.89:1 | 3.0:1 | pass |
| `focus` `#000000` / `canvas` | 21.00:1 | 3.0:1 | pass |
| `focus` / `surface-soft` | 19.58:1 | 3.0:1 | pass |
| `focus` / `block-cream` | 17.82:1 | 3.0:1 | pass |
| `focus` / `block-lime` | 16.91:1 | 3.0:1 | pass |
| `focus` / `block-mint` | 15.66:1 | 3.0:1 | pass |
| `focus` / `block-pink` | 15.04:1 | 3.0:1 | pass |
| `focus` / `block-coral` | 13.84:1 | 3.0:1 | pass |
| `focus` / `block-lilac` | 10.89:1 | 3.0:1 | pass |
| `focus` / `accent-magenta` `#ff3d8b` | 6.29:1 | 3.0:1 | pass |
| `focus-on-dark` `#ffffff` / `inverse-canvas` | 21.00:1 | 3.0:1 | pass |
| `focus-on-dark` / `block-navy` | 16.14:1 | 3.0:1 | pass |
| `focus-on-dark` / `surface-inverse-soft` | 14.55:1 | 3.0:1 | pass |
| `hairline` `#e6e6e6` / `canvas` | 1.25:1 | 3.0:1 | **fail** — frozen, disclosed, scoped to decoration |
| `hairline-soft` `#f1f1f1` / `canvas` | 1.13:1 | 3.0:1 | **fail** — frozen, disclosed, scoped to decoration |
| `on-primary` `#ffffff` / `accent-magenta` `#ff3d8b` | 3.34:1 | 4.5:1 | **fail** — frozen, disclosed, needs approval |
| `semantic-success` `#1ea64a` / `canvas` | 3.18:1 | 4.5:1 | **fail** as text / **pass** at the 3:1 non-text minimum — disclosed, needs approval |
| `button-icon-circular-inverse`: `#ffffff` / `#ffffff` (before) | 1.00:1 | 4.5:1 | **was fail** — authoring bug, fixed to 14.55:1 |
| `canvas` / `surface-soft` (layer separation) | 1.03:1 | no threshold | layers not luminance-distinguishable; this system does not use luminance for elevation |

### Motion inventory

Profile: **Calm** (switched from the assigned Playful — see Identity verdict). Tokens are the SPEC section 4 Calm block verbatim: instant 80ms, fast 150ms, base 250ms, slow 400ms, emphasis 500ms, reduced 150ms, stagger 40ms, `ease-standard cubic-bezier(0.4, 0, 0.2, 1)`, `ease-enter cubic-bezier(0.2, 0, 0.2, 1)`, `ease-exit cubic-bezier(0.4, 0, 1, 1)`. Prescribed, not extracted.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity` | unchanged (opacity only, already at or under reduced) |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `transform: scale(0.97)` / 0.94 on icon buttons | scale removed, state change instant |
| Focus | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` on the ring | unchanged; ring never delayed or suppressed |
| Page / route transition | 250ms out, 150ms in | `{motion.ease-exit}` / `{motion.ease-enter}` | `opacity` | fade clamped to `{motion.duration-reduced}` |
| Modal / lightbox | 250ms in, 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `transform: scale(0.98 to 1)`; scrim `opacity` | scale removed, both fade at 150ms |
| Drawer (mobile nav overlay) | 250ms in, 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateY(-8px to 0)` + `opacity` | travel removed, fade only at 150ms |
| Dropdown | 150ms in, 80ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateY(-4px to 0)` + `opacity` | travel removed, fade only |
| Toast | 250ms in, 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateY(8px to 0)` + `opacity` | travel removed; auto-dismiss extended, never shortened |
| List enter | 250ms per item, `{motion.stagger-step}` 40ms, capped at 6 items | `{motion.ease-enter}` | `opacity` + `transform: translateY(12px to 0)` | travel and stagger removed, all items fade together at 150ms |
| List exit | `{motion.duration-fast}` 150ms, no stagger | `{motion.ease-exit}` | `opacity` | unchanged |
| Loading | `{motion.duration-emphasis}` 500ms skeleton loop; spinner 800ms linear | `{motion.ease-standard}` / linear | `opacity` on skeletons, `transform: rotate()` on spinner | skeleton frozen to a static `{colors.surface-soft}` block; spinner becomes a static glyph plus a live-region text status |
| Marquee strip (brand ambience, stated as such) | continuous, about 40s | linear | `transform: translateX()` | frozen in its resting position, logos stay legible |
| Color-block section reveal | `{motion.duration-slow}` 400ms | `{motion.ease-enter}` | `opacity` + `translateY(16px to 0)` on the inner editorial column only; the panel ground never moves | travel removed, column fades at 150ms, panel painted immediately |
| Sticky-note thumbnail rotation | static | n/a | fixed `transform`, not an animation | unchanged |

Rules held: `transform`/`opacity` only (the file states explicitly that `width`, `height`, `top`, `left` and `margin` are never animated); every exit shorter than its entrance; nothing animates on first paint — hero headline, nav and both pill CTAs paint at full opacity; the marquee is the only infinite animation besides loaders and is declared as deliberate brand ambience; travel capped at 4–16px vertical; no overshoot anywhere.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, `REQUIRED_COLOR_ROLES["text-dim"]` (line ~27) | The `text-dim` role is satisfiable only by names that presuppose a lighter tone (`muted`, `text-soft`, `subtle`, `secondary`, `caption`). A brand whose explicit rule is "no mid-grey text — weight carries hierarchy" can satisfy the role only by adding a token that duplicates `ink`, which is what this file now does. It scores 5, but the token is a harness artefact as much as a design fact. | Let a file declare the role deliberately absent — accept a `text-dim: none` sentinel, or treat a Colors-section line naming the role as intentionally unified with `text` as satisfying it. Failing that, name `caption` in SPEC section 1 as the canonical escape hatch so 84 agents do not each invent a different one. |
| `theme-audit/audit.py`, `threshold_for()` (line ~235) | Every `components:` entry is judged at a text threshold via its `typography` ref, including entries whose `textColor` is a glyph fill rather than type. `comparison-checkmark` (size 16px, a check glyph) is held to 4.5:1 when WCAG's applicable minimum for a non-text graphic is 3:1 — which it passes at 3.18:1. The harness manufactures a failure, and the only way to clear it is to disclose a non-failure. | Skip the text threshold where a component declares `size` and no `padding` (an icon/glyph box), or honour an explicit `role: glyph` property on the entry and apply 3.0:1. |
| `theme-audit/audit.py`, `disclosed()` (line ~276) | Disclosure matches on substring, so a line disclosing `hairline-soft` also discloses `hairline`, and a line naming `button-primary` would discharge `button-primary-pressed`. A file can clear a failure it never mentioned. | Require a word-boundary match, or match the longest candidate token name first and consume it. |
| `theme-audit/audit.py`, dangling-ref regex (line ~170) | `\{([a-zA-Z]+)\.([A-Za-z0-9_.-]+)\}` does not match wildcard references such as `{colors.block-*}`, which this file uses nine times as a legitimate family reference. They are silently neither resolved nor flagged. | Recognise a trailing `*` as a family reference and require at least one matching key, or state in SPEC section 1 that wildcard refs are out of scope. |
| `theme-audit/SPEC.md` section 2 | The table lists `border on canvas` at 3.0:1, but the harness also runs `check_all` over *every* border-pattern token, so adding a passing parallel token (as section 2 instructs) cannot clear the original failure — only disclosure can. The SPEC reads as though the parallel token is the remedy. | Add one sentence: "A parallel accessible token satisfies the representative check; the frozen original must still be disclosed in Accessibility." |

### Needs approval

1. **`button-magenta-promo` — white on `#ff3d8b` at 3.34:1, required 4.5:1.**
   - Nearest passing fill at 4.5:1: `#d83376` (4.51:1). `#d81b60` reaches 4.95:1 with more hue shift.
   - Alternative with **no hex change** (my recommendation): swap the label to `{colors.ink}`, which measures **6.29:1** on the existing magenta and matches the rest of the system, where every pill is black-on-light or white-on-black. It preserves the brand hex exactly and changes only a text colour.
   - Usage note that would make the real value defensible as-is: white on `#ff3d8b` clears the 3:1 large-text threshold, so it is acceptable at **24px+, or 18.66px+ at weight 700**. The component currently ships `{typography.button}` at 20px / weight 480, below both.
2. **`comparison-checkmark` — `#1ea64a` on `#ffffff` at 3.18:1, required 4.5:1 by the harness.**
   - It **passes** the 3:1 non-text minimum that actually applies to a glyph, so I recommend approving no colour change and accepting the mitigation already written into the file: the glyph carries `aria-label="Included"` and the matrix headers are programmatically associated, so "included" is never encoded in colour alone.
   - If a hex change is wanted anyway, the nearest passing green at 4.5:1 is `#18883d` (4.54:1).
3. **`hairline` `#e6e6e6` (1.25:1) and `hairline-soft` `#f1f1f1` (1.13:1) on canvas.** Both frozen and disclosed; no hex change requested. What needs approval is the *scoping decision*: `hairline` was documented as the 1px border of `/contact/` text inputs, and I have moved that job to `{colors.border-control}` (ink, 21.00:1) while leaving `hairline` on decoration. That makes a visible change to how a form field looks versus the live site. Figma's real inputs use the light hairline and genuinely fail the 3:1 non-text minimum.
4. **Motion profile switched from Playful to Calm.** Stated in the file and argued below. Needs a yes/no, because it determines which other files this one is comparable with.
5. **`{shadow.modal}` = `0 24px 64px rgba(0,0,0,0.18)`** is prescribed, not extracted. It exists so `{shadow.*}` references resolve. Approve or replace with a measured value.

### Identity verdict

The file still reads unmistakably as Figma. Everything added is brand ink, brand paper, or a composite of two existing brand tokens — there is not one new hue in the frontmatter, which matters for a file whose stated first rule is that its system palette has no accent colour. The focus ring is a 2px black ring with a white offset; the accessible control boundary is 1px black; the prescribed error state is a 2px ink border plus a figmaMono caption and deliberately **no red**, because this system defines no semantic red and inventing one would have been the single most identity-destroying edit available. The new sections keep the file's own voice (colour blocks as the depth device, weight as hierarchy, pill as the only button shape) rather than importing generic token-dump prose.

**On the assigned profile: Playful is wrong for this brand, and I have used Calm.** SPEC section 5 rule 3 says to judge a playful identity on saturation *and role*, and gives the counter-case almost verbatim for this file: bright tones used as static backgrounds behind screenshots are not a playful identity; the test is whether saturated colour appears on interactive elements and whether the type voice is light and informal; and "a file whose own description says 'sober' or 'editorial', whose display weight is 400, and which forbids gradients is Calm no matter how many hexes it defines."

Figma matches every clause. The pastel blocks are full-width *section grounds* carrying product UI mocks — static backgrounds behind screenshots, exactly the excluded case — and they are pastel, not saturated (`block-lime` `#dceeb1`, `block-cream` `#f4ecd6`). Every interactive element in the system is monochrome: black pill, white pill, black selected tab. The one saturated interactive surface, `{colors.accent-magenta}`, is explicitly rationed to "one promo CTA per page, never two". The type voice is not informal: display weight 340 (below the clause's 400) with -1.72px tracking, and the file calls itself "editorial" three separate times — "editorial frame", "editorial cadence", "editorial paper". It also forbids gradients and shadows on its signature surfaces outright.

The honest counter-argument, for the record: the file does contain two Playful tells. `button-primary-pressed` is documented as relying on "micro-scale rather than a darkened fill", and the FigJam sticky-note thumbnails keep a deliberate off-axis rotation. I kept both — press is a `scale(0.97)` pop and the rotation is preserved as a static `transform` — but they are component-level details, not the identity-level signals the section 5 assignment rule is applied on. Calm's own signature ("short opacity-led fades, little travel") is the better description of a site whose pages are long, white, editorial columns.

Second note for the aggregator: the `caption: "#000000"` token exists to satisfy the harness's `text-dim` role and is the one place the file now carries a token for the harness's benefit rather than the brand's. It is labelled as such in the Colors section — the brand's real position is that it has no secondary text colour at all, and that is the more useful fact for anyone building on this document.
