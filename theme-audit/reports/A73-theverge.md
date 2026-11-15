## A73 · theverge

Scores before -> after (1-5), from the harness: tokens 1 -> 5 · refs 1 -> 5 · contrast 1 -> 5 · sections 1 -> 5 · motion 3 -> 5 · states 1 -> 4

The states 4 is one point too generous and should be read as 3. The file genuinely documents six of eight states (hover, focus-visible, active, pressed, selected, error); `disabled` and `loading` are absent from the source and are marked absent rather than filled. The harness counts `loading` because the pre-existing Image Treatment line `- **Lazy loading**: \`loading="lazy"\` on everything below the first fold` sits inside `## Components` and matches the word. That line is extracted prose and was left verbatim; see Shared issues.

Before-scores were taken on the legacy file, which had no frontmatter — so refs and contrast were floored at 1 by design, not measured.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | J, A | whole file | No frontmatter token block at all; numbered legacy headings. Nothing was measurable: all eight colour roles unresolved, zero colours parsed. Converted — `colors`, `typography`, `spacing`, `rounded`, `shadow`, `components`, `motion` built only from values already in the prose |
| P0 | Section contract | whole file | All twelve required sections missing by name. Eight were renames of numbered headings; `Shapes`, `Motion & Animation`, `Accessibility` and `Known Gaps` did not exist |
| P0 | B, H | `button-primary-hover` | The extracted hover swaps the mint pill for `rgba(255,255,255,0.2)` over the near-black canvas and keeps black text: #000000 on a composited #424242 = **2.09:1**. The loudest control on the site is barely legible while hovered. Real brand failure, disclosed; fix is in Needs approval |
| P0 | B, H | `button-primary-focus` | The extracted focus state fills the button with Focus Cyan and sets white text: #ffffff on #1eaedb = **2.58:1**. The ring itself is fine (7.20:1 on canvas); the label on the cyan fill is not. Real brand failure, disclosed |
| P0 | F | motion | No `motion:` group, no Motion & Animation section, no reduced-motion rule. Only two bare durations existed in prose (150ms, ~180ms). Added the Crisp block verbatim plus a ten-interaction table and a `prefers-reduced-motion` rule |
| P1 | B | `link-hover` #3860be | The site's universal link-hover colour is **3.17:1** on the canvas and **2.35:1** on slate, applied to every link including 12–14px mono nav links. Fails AA below 18.66px/700. Disclosed; Needs approval |
| P1 | B, E | `border-image` #313131 | 1.43:1 on canvas, 1.06:1 on slate. Frozen decorative hairline, scoped to decoration in prose, bindings left as extracted |
| P1 | B, E | `ultraviolet-rule` #3d00bf | The StoryStream spine is 1.73:1 on the canvas. Frozen; the white alternative the source also lists is 18.58:1 |
| P1 | B | `ultraviolet` #5200ff as a 1px boundary | 2.48:1 on canvas. It is the only boundary of the promotional outlined button and the sole signal of the input error state — an error distinguishable by colour alone, below the boundary minimum. Disclosed, with the instruction to pair it with a text message |
| P1 | B | `border-mint` #309875 on a mint tile | 2.79:1. Two neighbours on the same mint ramp cannot separate. Frozen binding kept; `{colors.text-inverted}` (14.52:1) named as the accessible alternative |
| P1 | A, G | focus ring coverage | The extracted ring (#1eaedb) covers the dark grounds (7.20:1 / 5.33:1) but not the mint or white tile fills (2.02:1 / 2.58:1). Added `focus-on-light` #0500ff — the hex the primary button's own focus border already declares — at 6.70:1 and 8.57:1. No ring in the palette covers the full-opacity ultraviolet tile (best 2.90:1), so a mandatory two-tone ring with a 1px `{colors.text}` outer edge (7.49:1) is specified there |
| P1 | B | `text-dim` #949494 on a white spotlight tile | 3.03:1. A dark-canvas metadata tone used on the one light signature surface |
| P1 | H | every component | `disabled` and `loading` appear nowhere in the source: no disabled fill, ink or opacity, no skeleton, no spinner. Marked absent per component, not invented |
| P1 | J | tile palette | Four of the six story-tile colours (yellow, pink, orange, electric blue) are named repeatedly but have **no hex anywhere in the file**. No tokens were invented; four grounds and their ink pairs are therefore unmeasurable. Known Gaps |
| P1 | C | layer separation | `canvas` -> `surface-slate` is **1.35:1**: a slate card barely lifts off the page floor, which is why the system reaches for a hairline or a saturated fill. Stated with the measurement in Elevation & Depth |
| P2 | Layout | spacing | The declared 8px base unit does not generate its own scale — 1, 5, 9, 10, 14, 15 and 25px are not multiples of 8. Both statements are extracted, so both were kept and the contradiction recorded |
| P2 | E | radius ladder | Bimodal: a 2/3/4px form-control cluster and a 20/24/30/40px pill cluster with nothing between. No value sits outside its own cluster, and the gap is the source's own statement — noted, not changed |
| P2 | J | padding | Every container's padding is a range ("~24–32px", "32px+", "40–48px"). Bindings use the single stated value nearest each range; the ranges stay in prose |
| P2 | J | secondary button outline | `rgb(233, 233, 233) none 0px` is a computed-style artifact (zero width), not a design value. Not tokenised |
| P2 | J | mint tile border | Recorded two ways in the source: `0px 0px 1px solid #3cffd0` in Components, `#309875` in the Agent Prompt Guide. The second is bound; both are disclosed |
| P2 | D | typography | Letter-spacing is absent for seven roles and `mono-timestamp` states ranges (weight 500–600, tracking 1.1–1.8px). Kept as ranges; no canonical value picked |
| P2 | G | tap targets | The source's own note gives nav links at 28–32px against its 44px instruction. Not measurable from a document; recorded as the source's disclosure, not as an audit finding |
| P2 | F | extracted transition property | The one real transition in the system animates `color`, not `opacity`. Not a layout-triggering property, so kept as found and stated plainly; everything added animates `transform` and `opacity` only |

Counts: **P0 5 · P1 10 · P2 7**.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Top of file | no frontmatter -> full YAML block: 23 colours, 21 typography roles, 19 spacing steps, 8 radii, 5 shadows, the Crisp motion block, 19 components | Legacy conversion (dimension J). Every value is already written in the prose |
| Headings | `## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide` -> unnumbered contract names | SPEC section 3 |
| Section order | Components sat at 4, radius scale inside Layout -> `## Shapes` created from the moved Border Radius Scale, `## Components` moved after it, both verbatim | SPEC section 3 required order |
| `## Colors` | hexes only -> every tone bound to a token, plus new `### Borders` and `### Focus` subsections | Refs must resolve; the boundary and ring decisions need to be stated |
| `colors.focus` / `colors.focus-on-light` | ring colour existed in prose as "Focus Cyan", untokenised -> `focus: #1eaedb` (extracted) and `focus-on-light: #0500ff` (the primary button's own extracted focus border) | A ring must be addressable; one ring cannot serve both the dark grounds and the mint/white tiles |
| `## Elevation & Depth` | philosophy prose only -> plus measured layer separation (1.35:1, 18.58:1, 1.05:1) and a statement that elevation is one device in three colours | Dimension C |
| `## Shapes` | bare list -> plus token names and the bimodal-ladder note | Dimension E |
| `## Components` | no state coverage -> a state line per entry, with `disabled`/`loading` marked absent on their own bullets, and the four contrast failures named inline | Dimension H |
| `## Motion & Animation` | absent -> new section after Components: prescribed-not-measured first line, Crisp argued from the file's own 150ms/180ms and "no lift, no scale", ten-interaction table, reduced-motion CSS | Dimension F |
| `## Accessibility` | absent -> new section: 28 key pairs, 16 component pairs, ring visibility on all five surfaces, tap targets, reduced motion | Dimension G |
| `## Do's and Don'ts` | 10 + 10 -> plus 5 Don'ts covering the invisible hairlines, the hover-colour failure, layout-property animation and masthead entrance | The new measurements need an actionable rule |
| `## Known Gaps` | absent -> new section with eleven entries, including the four tile colours with no hex and the harness's `loading` false positive | SPEC section 3; nothing invented |
| `## Agent Prompt Guide` | `## 9.` -> kept verbatim after Known Gaps, including its `### Iteration Guide` | SPEC section 3: a legacy section with no slot is kept, not folded |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `text` #ffffff / `canvas` #131313 | 18.58:1 | 4.5:1 | Pass |
| `text` #ffffff / `surface-slate` #2d2d2d | 13.77:1 | 4.5:1 | Pass |
| `text` #ffffff / `ultraviolet` #5200ff | 7.49:1 | 4.5:1 | Pass |
| `text-dim` #949494 / `canvas` | 6.13:1 | 4.5:1 | Pass |
| `text-dim` #949494 / `surface-slate` | 4.54:1 | 4.5:1 | Pass (no margin) |
| `text-dim` #949494 / `surface-hazard-white` #ffffff | 3.03:1 | 4.5:1 | Fail (disclosed) |
| `text-on-slate` #e9e9e9 / `surface-slate` | 11.34:1 | 4.5:1 | Pass |
| `text-inverted` #131313 / `accent` #3cffd0 | 14.52:1 | 4.5:1 | Pass |
| `text-inverted` #131313 / `surface-hazard-white` | 18.58:1 | 4.5:1 | Pass |
| `on-accent` #000000 / `accent` | 16.41:1 | 4.5:1 | Pass |
| `accent` #3cffd0 as ink / `canvas` | 14.52:1 | 4.5:1 | Pass |
| `link-hover` #3860be / `canvas` | 3.17:1 | 4.5:1 | Fail (disclosed) |
| `link-hover` #3860be / `surface-slate` | 2.35:1 | 4.5:1 | Fail (disclosed) |
| `pressed-gray` #8c8c8c / `canvas` | 5.53:1 | 4.5:1 | Pass |
| `border-white` #ffffff / `canvas` | 18.58:1 | 3:1 | Pass |
| `border-white` #ffffff / `surface-slate` | 13.77:1 | 3:1 | Pass |
| `border-white` #ffffff / `surface-hazard-white` | 1.00:1 | 3:1 | Fail — a pair the source says never renders (spotlight tiles take no border); disclosed |
| `border-mint` #309875 / `canvas` | 5.20:1 | 3:1 | Pass |
| `border-mint` #309875 / `surface-slate` | 3.85:1 | 3:1 | Pass |
| `border-mint` #309875 / `accent` #3cffd0 | 2.79:1 | 3:1 | Fail (disclosed, frozen binding) |
| `border-hover-ring` #c2c2c2 / `canvas` | 10.43:1 | 3:1 | Pass |
| `border-image` #313131 / `canvas` | 1.43:1 | 3:1 | Fail (disclosed, frozen) |
| `border-image` #313131 / `surface-slate` | 1.06:1 | 3:1 | Fail (disclosed, frozen) |
| `border-image` #313131 / `surface-hazard-white` | 13.01:1 | 3:1 | Pass — the frozen tone is the accessible edge on a white tile |
| `ultraviolet` #5200ff / `canvas` | 2.48:1 | 3:1 | Fail (disclosed, frozen) |
| `ultraviolet` #5200ff / `surface-slate` | 1.84:1 | 3:1 | Fail (disclosed, frozen) |
| `ultraviolet-rule` #3d00bf / `canvas` | 1.73:1 | 3:1 | Fail (disclosed, frozen) |
| `overlay-black` rgba(0,0,0,0.33) over `canvas` -> #0d0d0d / `canvas` | 1.05:1 | — | Atmosphere, not a boundary |
| `focus` #1eaedb / `canvas` | 7.20:1 | 3:1 | Pass |
| `focus` #1eaedb / `surface-slate` | 5.33:1 | 3:1 | Pass |
| `focus` #1eaedb / `accent` #3cffd0 | 2.02:1 | 3:1 | Fail — `focus-on-light` serves this surface |
| `focus` #1eaedb / `surface-hazard-white` | 2.58:1 | 3:1 | Fail — `focus-on-light` serves this surface |
| `focus` #1eaedb / `ultraviolet` #5200ff | 2.90:1 | 3:1 | Fail — no ring covers it; two-tone ring mandated (disclosed) |
| `focus` #1eaedb / ultraviolet at 0.9 alpha -> #4c02e7 | 3.29:1 | 3:1 | Pass — the gap is real only at full opacity |
| `focus-on-light` #0500ff / `accent` | 6.70:1 | 3:1 | Pass |
| `focus-on-light` #0500ff / `surface-hazard-white` | 8.57:1 | 3:1 | Pass |
| `focus-on-light` #0500ff / `focus` #1eaedb (the extracted inner border) | 3.32:1 | 3:1 | Pass |
| `text` #ffffff / ultraviolet tile, as the ring's outer edge | 7.49:1 | 3:1 | Pass |
| `button-primary` #000000 / #3cffd0 at 12px/600 | 16.41:1 | 4.5:1 | Pass |
| `button-primary-hover` #000000 / composited #424242 | 2.09:1 | 4.5:1 | Fail (disclosed) |
| `button-primary-focus` #ffffff / #1eaedb | 2.58:1 | 4.5:1 | Fail (disclosed) |
| `button-primary-pressed` #000000 / composited #7c7c7c | 5.03:1 | 4.5:1 | Pass (before the extracted `opacity: 0.5`) |
| `button-secondary` #e9e9e9 / #2d2d2d at 16px/700 | 11.34:1 | 4.5:1 | Pass |
| `card-ultraviolet-tile` #ffffff / #5200ff at 32px | 7.49:1 | 3:1 large | Pass |
| `card-mint-tile` #131313 / #3cffd0 at 24px/700 | 14.52:1 | 3:1 large | Pass |
| `card-spotlight-tile` #131313 / #ffffff at 24px/700 | 18.58:1 | 3:1 large | Pass |
| `surface-slate` / `canvas` (layer separation) | 1.35:1 | — | Barely a layer |
| `surface-hazard-white` / `canvas` (layer separation) | 18.58:1 | — | The only self-evident layer |

### Motion inventory

Prescribed, not extracted. **Crisp** profile, carried verbatim from SPEC section 5.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (link, tile headline, nav) | `{motion.duration-base}` 150ms | `{motion.ease-standard}` | `color` to `{colors.link-hover}` as extracted, plus `opacity` on the fill swap — no lift, no scale | Kept, capped at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` to the extracted 0.5 over `{colors.pressed-fill}` | Unchanged; already below the cap |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Instant; never suppressed |
| Page / route transition | `{motion.duration-slow}` 220ms | `{motion.ease-enter}` | `opacity`, `translateY(8px)`->0 on the feed, never the masthead | Travel removed; fade at the cap |
| Modal / drawer enter (mobile nav) | `{motion.duration-base}` | `{motion.ease-enter}` | `opacity`, `translateX(-100%)`->0 | Travel removed; fade at the cap |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at the cap |
| Dropdown enter / exit | `{motion.duration-fast}` / `{motion.duration-instant}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(-4px)`->0 | Travel removed; fade at the cap |
| Toast enter / exit | `{motion.duration-base}` / `{motion.duration-fast}` | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(8px)`->0 | Travel removed; fade at the cap |
| List enter (StoryStream) | `{motion.duration-fast}`, stagger `{motion.stagger-step}` 20ms | `{motion.ease-enter}` | `opacity`, `translateY(6px)`->0 | Stagger and travel removed; one fade at the cap |
| List exit | `{motion.duration-instant}`, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; fade at the cap |
| Loading | 1000ms, infinite | linear | `opacity` pulse 1 -> 0.4 on a `{colors.surface-slate}` placeholder | Frozen; static placeholder remains |

Exit is always shorter than its entrance; no infinite animation except the loader; nothing animates on first paint; `transform` and `opacity` only, plus the one extracted `color` swap.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` — the states block in `audit()` (`structured` / `documents()`, the `NOT_DOCUMENTED` filter) | A structured line inside `## Components` that merely contains a state word counts as documentation of that state. This file's extracted `- **Lazy loading**: \`loading="lazy"\` on everything below the first fold` makes `loading` count as a documented state, inflating states from 3 to 4. Deleting the line to score honestly would destroy extracted content | Exclude `loading="` / `loading=lazy` / `lazy loading` from the `loading` match, or require the state word to sit in a state-ish context (start of the line, after `**`, or adjacent to `state`/`:hover`-style markers) |
| `theme-audit/audit.py` — `dual_theme` (~line 355) and `theme_of` (~line 383) | The measured-polarity clause plus the `white` naming marker make a single light tile a second "theme" in a dark-canvas file. Two consequences here: (1) `border-white` is reclassified light-theme, so its real extracted bindings on the dark canvas (18.58:1) are skipped entirely; (2) a manufactured pair is reported — `border-white on surface-hazard-white` at 1.00:1 — which the source explicitly says never renders ("Border: … or nothing (on saturated fill)"). I disclosed it rather than leave it unresolved, but it is a measurement against a ground the site never draws it on | Require the alt-theme ground to be bound as a component `backgroundColor` *with its own ink of the opposite polarity*, and do not let a colour-name marker (`white`, `black`, `cream`) re-theme a token whose bindings are all on default-polarity grounds |
| `theme-audit/briefs/A73-theverge.md`, line 26 | The brief asserts "No file in this repo defines a focus ring — add one that suits this brand". This file already defines one: **Focus Cyan `#1eaedb`**, "Reserved for button focus rings. Never shown outside a keyboard-focus state", plus a `#0500ff` focus border on the primary button. I kept both as extracted instead of prescribing a new colour; per SPEC section 1 a file that has a ring needs no second one unless a second polarity demands it, which here it does | Soften the brief's premise to "check first" (SPEC already says oracle has one), so no agent invents a ring over an extracted one |
| `theme-audit/audit.py` | The script changed on disk mid-review (35,850 -> 40,548 bytes, 17:10 -> 17:22), which changed theme detection and therefore which pairs are reported. My before-scores were produced by the earlier build | Freeze the harness for the duration of a review wave, or stamp its version into the JSON so before/after scores are comparable |

### Needs approval

Every item below is a **frozen extracted value**. Nothing was changed in place; each is disclosed in the file's Accessibility section with its measured ratio.

1. **`button-primary` hover label — #000000 on `rgba(255,255,255,0.2)` over the canvas, composited #424242 = 2.09:1.** Nearest passing value: invert the label to `{colors.text}` #ffffff, which measures **10.05:1** on the same fill. Usage note that would make the real value defensible: none — a 12px/600 mono button label has no large-text exemption, so this one needs the brand owner's decision rather than a note.
2. **`button-primary` focus label — #ffffff on `focus` #1eaedb = 2.58:1.** Nearest passing value: `{colors.on-accent}` #000000 on the same cyan fill = **8.13:1**, which also matches the brand's own rule that black ink belongs on light fills. The ring is unaffected and stays at 7.20:1 on the canvas.
3. **`link-hover` #3860be — 3.17:1 on canvas, 2.35:1 on slate**, applied to every link on the site. Two defensible routes: (a) a usage note restricting Deep Link Blue to 18.66px+/700 or 24px+ text, where the 3:1 large-text threshold applies — this covers tile headlines but **not** the 12–14px mono nav links the source applies it to; or (b) the nearest passing tone, **#5a7bc9 (4.52:1 on canvas)**, which still fails on slate at 3.35:1. A hover colour that works on both grounds does not exist in this hue at this saturation.
4. **Re-binding the two frozen hairlines.** `{colors.border-image}` #313131 (1.43:1) and `{colors.ultraviolet-rule}` #3d00bf (1.73:1) keep their extracted `components:` bindings. Nearest passing values, if the brand owner wants them re-pointed: **#626262 (3.05:1)** and **#7145d0 (3.07:1)**. Both change the look; neither was applied.
5. **`border-mint` #309875 on a mint tile = 2.79:1.** The palette's own passing alternative is `{colors.text-inverted}` #131313 at 14.52:1. The extracted binding is kept; swapping it is a brand decision.
6. **`ultraviolet` #5200ff as a 1px boundary = 2.48:1**, including as the sole signal of the input error state. Nearest passing value **#6e29ff (3.03:1)**; the usage note that makes the real value defensible is that the error must also carry a text message, which the file now states.
7. **The ultraviolet tile's focus ring.** No single tone in the palette clears 3:1 on a full-opacity #5200ff fill (best: `focus` at 2.90:1). The file now mandates a two-tone ring — `{colors.focus}` with a 1px `{colors.text}` outer edge at 7.49:1. Approving a new mid-luminance ring colour instead would be the alternative, and would add a colour to a palette whose own Don'ts forbid new accents.

### Identity verdict

Still unmistakably The Verge. The frontmatter reads as a hazard-tape system rather than a generic token dump: mint and ultraviolet are bound as `accent` and as tile fills rather than as a neutral "primary", the radius ladder keeps all eight of its idiosyncratic values including the 40px outlined pill, the Manuka 107px/900/0.80 display role and the PolySans Mono uppercase-only labels survive intact, and the three declared tile grounds (mint, ultraviolet, white spotlight) are the component block's most distinctive entries. The one risk I watched was the Accessibility section: 28 measured rows could bury the voice, so every failing row names the Verge-specific thing that fails — the hazard-tape hairline, the StoryStream spine, the universal link hover — rather than reciting token names.

**The Crisp profile is correct and I did not switch it.** The evidence is in the file, not in the category: the only two transition values it records are 150ms and ~180ms, within 30ms of Crisp's base; its hover is explicitly "no lift, no scale"; its images are "static — no zoom, no scale, no opacity shift"; and the single documented response to a pointer anywhere in the document is a colour swap. That is Crisp's signature exactly. Playful is the tempting alternative on the six-colour saturated tile palette and the mint-on-interactive buttons, but SPEC's rule 3 is a conjunction and the second half fails: the type voice is a 900-weight 107px industrial shout with mono-uppercase labels, not light and informal, and nothing in the file springs, pops or overshoots. Cinematic is excluded — no full-bleed photographic reveal, no slow scale, and type that arrives all at once. Calm would be wrong for a document that says "developer console meets club night".
