## A44 · nike

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 2 | 5 | 2 | 3 | 1 | 1 |
| after | 4 | 5 | 5 | 5 | 5 | 5 |

`tokens` stops at 4 on purpose. Of the three roles the harness reported missing, only
`focus` was genuinely absent from the palette. `surface` and `text-dim` were both already
present under brand names the role patterns did not match — `soft-cloud` and `mute` — so per
SPEC section 1 I reported them as a harness bug and **added no alias token for either**.
`text-dim` has since started resolving to `mute` on its own: audit.py commit `d9df67e`
("accept mute-\* dim tones") landed mid-review and added `^mute$` to the pattern list, which
is the fix this report proposes below. `surface` is still unresolved, still for the same
reason, and still without an invented token — see Shared issues.

The `focus` pair I did add is not an alias. It is a real role binding under the exception
SPEC commit `baf1859` added to section 1: the two rings reuse hexes the palette already
owns (`{colors.ink}` and `{colors.on-primary}`) but carry distinct jobs on distinct
surfaces, and a ring must be addressable as `focus*` to be specified or measured at all.
The Accessibility section states which existing tone each one reuses, so neither reads as a
new brand colour.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A Token contract | `colors.focus` | No focus ring token anywhere in the file. The only focus treatment documented was `search-pill-focused`; every other control — pill CTAs, filter chips, swatch dots, product cards, campaign tiles, nav links — had no keyboard indicator at all. Fixed. |
| P0 | B Colour | `{colors.hairline}` `#cacacb` on `{colors.canvas}` | 1.64:1, against the 3:1 WCAG 1.4.11 floor. Not merely a decorative divider: the file bound it as the *only* boundary of `filter-chip`, `badge-promo` and the light-colorway `swatch-dot` ring, i.e. three interactive affordances whose edge is invisible. Fixed by rescoping, not by changing the hex. |
| P0 | C/F Sections + motion | document | `## Motion & Animation` and `## Accessibility` both absent; no `motion:` group; no `prefers-reduced-motion` rule anywhere in the file. Fixed. |
| P1 | B Colour | `{colors.stone}` `#9e9ea0` on `{colors.canvas}` | 2.67:1. The Colors section gives it two jobs — inverse text on dark surfaces (7.06:1 on `{colors.ink}`, passes) and "lowest-emphasis utility text", which on the white canvas fails 4.5:1 *and* fails the 3:1 large-text allowance. The harness never saw it: `stone` matches no `text-dim` or `text` pattern. Disclosed and rescoped in prose. |
| P1 | B Colour | `{colors.hairline-soft}` `#e5e5e5` on `{colors.canvas}` | 1.26:1, undisclosed. Genuinely decorative (inset seam under sticky bars), so the value stands; now declared with its ratio. |
| P1 | B Colour | `{colors.success-bright}` `#1eaa52` on `{colors.canvas}` | 3.03:1 as text, below 4.5:1. The palette documents it as inverse success for dark surfaces, where it is 6.23:1 on `{colors.ink}` and passes — but the file declares no dark surface token, so the only ground the harness can measure it against is the white canvas. Disclosed with both numbers. |
| P1 | H States | every component | hover, focus-visible, disabled, loading and error named nowhere in the file; the Components preamble declared hover out of scope "per system policy". Fixed with a Component States table that marks extracted states **(E)** and the rest prescribed. `badge-promo` and `badge-sale-text` are stated as genuinely single-state. |
| P1 | A Token contract | `surface`, `text-dim` roles | Unresolved by the harness although the palette plainly contains both (`soft-cloud`, `mute`). Reported as a harness bug, not papered over. `text-dim` was fixed upstream mid-review by audit.py `d9df67e`; `surface` still stands. See Shared issues. |
| P1 | B/G Colour | no dark theme | The file names two inverse-on-dark tones (`stone`, `success-bright`) but declares no dark canvas or dark surface token for them to sit on. Their only measurable dark ground is `{colors.ink}` via component bindings. Added to Known Gaps. |
| P2 | E Shapes | `{rounded.full}` vs `{rounded.lg}` | Frontmatter binds `{rounded.full}` (9999px) on every pill component; the prose says those same pills are `{rounded.lg}` (30px), and Key Characteristics mislabels `{rounded.full}` as "30px". **Not fixed** — I cannot tell from the file which value was extracted, and for a 48px-high pill both render identically, so a guess would just move the error. Needs the capture to resolve. |
| P2 | F Motion | `button-primary-active` | The extracted pressed state records `scale(0.5)` with `opacity: 0.5`. A 50% collapse reads far more like a captured mid-transition frame than a resting pressed value. Kept verbatim because it is the file's one extracted motion fact; flagged here and in Known Gaps. |
| P2 | C Elevation | `{colors.canvas}` / `{colors.soft-cloud}` | The two layers measure 1.09:1 against each other, so they are not distinguishable as layers by luminance — only by being large adjacent fields. There is no third raised layer. This is faithful to a system whose stated position is "no elevation", and elevation *is* expressed one consistent way (a 3-level ladder: flat, 1px hairline, 1px inset line), so nothing was changed. |
| P2 | D Typography | `{typography.utility-xs}` | 9px, bound to the footer fine-print row. Contrast passes at 4.94:1; the size does not survive any legibility floor. Extracted, so kept; noted in Accessibility as not reusable for anything actionable. |
| P2 | D Typography | `{spacing.section}` | Used as `button-primary`'s 48px height, so a spacing-ladder token is doing duty as a component dimension. Pre-existing and referenced consistently; left alone to keep the diff reviewable. |

Typography otherwise clean: every one of the 13 roles carries fontSize, fontWeight and
lineHeight, and body text passes on both of this file's own light surfaces (`{colors.ink}`
18.88:1 on canvas, 17.32:1 on soft-cloud). Zero dangling `{group.token}` references before
or after. Spacing and radius ladders are internally monotonic with no stray value.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#111111"`, `focus-on-dark: "#ffffff"` | The only genuinely missing role. Nike has no accent colour, so per SPEC section 1 the ring is the brand's own ink and its own paper with a mandatory opposite-polarity offset, not an invented hue. Two rings because the file documents both white grounds and solid-`{colors.ink}` campaign tiles; one ring cannot serve both (ink on ink is 1:1). |
| frontmatter | — -> `motion:` group | Cinematic block from SPEC section 5, verbatim, all ten keys. |
| Colors › Surface | hairline bullets -> same hexes, scoped to "decorative dividers only" with their ratios stated; new "Control boundary" bullet pointing at `{colors.mute}` | The frozen hexes are untouched. Per the settled rule, the palette already owns a passing tone that can do the boundary work (`{colors.mute}`, 4.94:1 / 4.53:1), so no parallel `hairline-strong` was invented. |
| Colors › Focus (new `###`) | — -> both rings with measured ratios, offsets, and the two-tone variant for full-bleed photography | Focus ring is prescribed; labelled as such. Ring is drawn outside the control with a stated 2px offset so it is judged against the surface behind it, which is the only way a system whose primary CTA is solid `#111111` gets a visible indicator. |
| Components › preamble | "No hover states documented per system policy" -> extracted-versus-prescribed note | The old line declared a whole class of states out of scope. The replacement keeps the honest fact (hover values were not captured) without using it as an excuse to document nothing. |
| Components › `filter-chip`, `badge-promo`, `swatch-dot` | 1px `{colors.hairline}` -> 1px `{colors.mute}`, each with the reason inline | These three edges are the control. See Needs approval — this changes an extracted treatment. |
| Components › Component States (new `###`) | — -> 14-row table | Dimension H. Every component names its states; extracted ones marked **(E)**; two components stated as genuinely single-state. |
| new `## Motion & Animation` after Components | — -> prescribed-not-measured first line, a chrome/editorial split, a 12-row interaction table, and the `prefers-reduced-motion` block | Dimension F. Covers all ten required interactions plus the campaign hero reveal. `transform` and `opacity` only; every exit shorter than its entrance; loaders are the only loop. |
| new `## Accessibility` after that | — -> measured key pairs, declared failures, per-surface focus ring table, tap targets, reduced motion | Dimension G. Every failure stated with its ratio rather than hidden. |
| Known Gaps | +5 bullets | Motion prescribed; focus ring prescribed; hover/disabled/loading/error prescribed; no dark theme declared; tap targets and layout unverifiable without a rendered page. |

Section order now matches SPEC section 3 exactly: … Components, Motion & Animation,
Accessibility, Do's and Don'ts, Responsive Behavior, Iteration Guide, Known Gaps.
`Responsive Behavior` was already a top-level `##`, so nothing was moved.

### Contrast checks

All computed with WCAG 2.1 relative luminance via python3 stdlib; none estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#111111` / `canvas` `#ffffff` | 18.88:1 | 4.5:1 | pass |
| `ink` / `soft-cloud` `#f5f5f5` | 17.32:1 | 4.5:1 | pass |
| `on-primary` `#ffffff` / `ink` | 18.88:1 | 4.5:1 | pass |
| `charcoal` `#39393b` / `canvas` | 11.52:1 | 4.5:1 | pass |
| `ash` `#4b4b4d` / `canvas` | 8.70:1 | 4.5:1 | pass |
| `mute` `#707072` / `canvas` | 4.94:1 | 4.5:1 | pass |
| `mute` / `soft-cloud` | 4.53:1 | 4.5:1 | pass (0.03 margin) |
| `stone` `#9e9ea0` / `canvas` | 2.67:1 | 4.5:1 | **fail** — disclosed |
| `stone` / `ink` | 7.06:1 | 4.5:1 | pass (its inverse job) |
| `hairline` `#cacacb` / `canvas` | 1.64:1 | 3.0:1 | **fail** — disclosed |
| `hairline-soft` `#e5e5e5` / `canvas` | 1.26:1 | 3.0:1 | **fail** — disclosed |
| `sale` `#d30005` / `canvas` | 5.57:1 | 4.5:1 | pass |
| `sale-deep` `#780700` / `canvas` | 11.48:1 | 4.5:1 | pass |
| `success` `#007d48` / `canvas` | 5.21:1 | 4.5:1 | pass |
| `success-bright` `#1eaa52` / `canvas` | 3.03:1 | 4.5:1 | **fail** — disclosed |
| `success-bright` / `ink` | 6.23:1 | 4.5:1 | pass (its inverse job) |
| `info` `#1151ff` / `canvas` | 5.76:1 | 4.5:1 | pass |
| `info-deep` `#0034e3` / `canvas` | 8.08:1 | 4.5:1 | pass |
| `accent-pink` `#ed1aa0` / `canvas` | 4.00:1 | 4.5:1 | fail as text — forbidden as text by the file; disclosed |
| `accent-teal` `#0a7281` / `canvas` | 5.62:1 | 4.5:1 | pass |
| `focus` `#111111` / `canvas` | 18.88:1 | 3.0:1 | pass |
| `focus` / `soft-cloud` | 17.32:1 | 3.0:1 | pass |
| `focus-on-dark` `#ffffff` / `ink` | 18.88:1 | 3.0:1 | pass |
| `canvas` / `soft-cloud` (layer separation) | 1.09:1 | n/a | layers not separable by luminance |

Component bindings: 0 failures across all 23 `components:` entries, before and after.
The remaining soft accent tones (`accent-pink-soft`, `accent-purple-soft`,
`accent-purple-pale`, `accent-pink-deep`) are fills and swatch colours never bound to a
label, so per SPEC section 1 there is no declared pair to measure and none was guessed.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover — chrome (pill, chip, nav/footer link) | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` | retained at `{motion.duration-reduced}`; no travel to remove |
| Hover — editorial (campaign tile, benefit card, card image) | `{motion.duration-slow}` 600ms | `{motion.ease-standard}` | `transform: scale(1.03)` | scale removed; static |
| Press / active | `{motion.duration-instant}` | `{motion.ease-exit}` | `transform: scale()` + `opacity` (extracted collapse) | scale removed; opacity step only |
| Focus ring appear | `{motion.duration-instant}` | `{motion.ease-enter}` | `opacity` | retained unchanged — never slowed |
| Page / route transition | 400ms out / 600ms in | `{motion.ease-exit}` / `{motion.ease-enter}` | `opacity` + `translateY(16px)` | translate removed; cross-fade |
| Modal / drawer | 400ms in / 240ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `translateX` + scrim `opacity` | slide removed; both fade |
| Dropdown | 240ms in / 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scaleY()` | scale removed; opacity only |
| Toast | 240ms in / 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | translate removed; dwell unchanged |
| List enter | 400ms per item, `{motion.stagger-step}` 80ms between | `{motion.ease-enter}` | `opacity` + `translateY(12px)` | stagger and translate removed; one fade |
| List exit | 240ms, no stagger | `{motion.ease-exit}` | `opacity` | retained at `{motion.duration-reduced}` |
| Loading (skeleton, 3-dot loader) | 1200ms loop | `{motion.ease-standard}` | `opacity` 1 → 0.4 → 1 | frozen at static 0.7 opacity |
| Campaign hero reveal | 900ms image, 600ms headline at 160ms delay | `{motion.ease-enter}` | `scale(1.04)` → `1`, `opacity` + `translateY(24px)` | all travel removed; fade together |

Every exit is shorter than its entrance. Nothing animates on first paint in a way that
delays content — the hero reveal is intersection-triggered and the headline is painted and
readable before its transform resolves. The two loaders are the only infinite animations
and there is no brand ambience loop. `{motion.duration-reduced}` is 150ms, deliberately
below this profile's own 240ms `duration-fast`, which is exactly the case SPEC section 6
says the token exists for. Harness confirms `layout_animation_mentions: []`.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py:22` | The `surface` role patterns match only literal naming (`surface*`, `card*`, `panel*`, `tile*`, `elevated`). Nike's panel surface is `soft-cloud` `#f5f5f5` — bound as `backgroundColor` on `product-card-image`, `utility-bar`, `search-pill`, `button-secondary` and `button-icon-circular`, and called "a single soft surface gray" in the file's own description. **The palette genuinely has a card/panel surface; it is the naming that defeats the pattern.** Decisive evidence that this is a bug and not a gap: the same script, at line 362, *already* treats `soft-cloud` as a surface — its focus-coverage check appends any token a component declares as `backgroundColor`, so audit.py holds two different notions of "surface" and the role check uses the weaker one. | Apply to the `surface` role the component-binding fallback that already exists for `border` at lines 208–213: if no pattern matches, take a non-accentish `backgroundColor` that is bound by a component and is not the canvas. That resolves `surface=soft-cloud` here with better evidence than any regex, and would then also exercise the four `check_all(..., "surface", ...)` calls that are currently skipped on this file. |
| `theme-audit/audit.py:28` | **Fixed upstream during this review — recorded for the record.** The `text-dim` patterns included `^muted$` but not `^mute$`, so Nike's secondary ink `mute` `#707072` (documented as "product category subtitles, footer link text, secondary metadata", bound as `footer.textColor`) left the role unresolved. Commit `d9df67e` added `^mute$` and `^mute-`; `text-dim` now resolves to `mute` at 4.94:1 and the role is satisfied with no token added to this file. | Done. No further action. |
| `theme-audit/audit.py:28` | Related false negative in the other direction: `stone` `#9e9ea0` is a real low-emphasis text tone at 2.67:1 on the canvas and matches no `text` or `text-dim` pattern, so the harness never measures it. I found it by hand and disclosed it. | Same binding-based fallback would help, but the general fix is to measure every colour the prose or a component binds as an ink, not only pattern-matched ones. Out of scope for a pattern tweak; recorded so it is not lost. |
| `theme-audit/audit.py:~245` (`theme_of`) | `dual_theme` requires a colour key containing both a surface word and `light`/`dark`. Nike documents inverse-on-dark tones (`stone`, `success-bright`) but names no dark surface token, so `dual_theme` is false and both are measured against the white canvas — a ground the file says they are never drawn on. The resulting `success-bright` failure is real-as-measured but misattributed. | Treat a token the prose or a component binds onto a dark `backgroundColor` as theme-scoped, or let a file declare its inverse ground explicitly. I disclosed the pair with both ratios rather than wait for this. |

### Needs approval

1. **Control boundaries moved off an extracted hex.** `filter-chip`, `badge-promo` and the light-colorway `swatch-dot` ring were documented with a 1px `{colors.hairline}` `#cacacb` edge at 1.64:1. I changed those three to `{colors.mute}` `#707072` (4.94:1). The hairline hex itself is untouched and still documented with its real ratio, and no new token was created — `mute` was already in the palette. But this *is* a prescribed deviation from an extracted treatment on three components, so it wants a human eye. The alternative the SPEC also allows is a parallel `hairline-strong` token; I did not take it, because the settled rule says use a passing tone the palette already owns rather than add one.
2. **`{colors.hairline}` `#cacacb` — 1.64:1 on canvas, needs 3:1.** Nearest passing value `#949494` (3.03:1). Usage note that makes the real value defensible: as a purely decorative rule between rows whose labels carry the meaning, WCAG 1.4.11 does not apply, so the extracted value stands for dividers and only for dividers.
3. **`{colors.hairline-soft}` `#e5e5e5` — 1.26:1, needs 3:1.** Nearest passing `#949494` (3.03:1). Defensible as-is: it is a 1px inset seam under sticky bars, never an interactive boundary.
4. **`{colors.success-bright}` `#1eaa52` — 3.03:1 as text on canvas, needs 4.5:1.** Nearest passing `#157c3b` (5.28:1) or `#167f3d` (5.08:1). Defensible without any change if confined to its documented job — inverse text on `{colors.ink}`, 6.23:1 — or used as a fill carrying `{colors.ink}` text. It fails only in the use the file never claimed.
5. **`{colors.stone}` `#9e9ea0` — 2.67:1 on canvas.** Nearest passing `#767676` (4.54:1). No usage note rescues the canvas case: at 2.67:1 it fails even the 3:1 large-text allowance, so there is no minimum type size at which it becomes defensible on white. Defensible only in its other documented job, on `{colors.ink}` at 7.06:1.
6. **`{colors.accent-pink}` `#ed1aa0` — 4.00:1 on canvas.** Clears 3:1, so it is defensible for 24px+ text or 18.66px+ at weight 700, and for chip and swatch fills. The file already forbids the category accents as text, which is the stricter and correct rule; recorded so the number exists on the page.
7. **`{rounded.full}` vs `{rounded.lg}` on every pill.** Frontmatter and prose disagree (9999px vs 30px) and Key Characteristics labels `{rounded.full}` as "30px". I left all three alone rather than guess which was extracted. Someone with the capture should settle it.

### Identity verdict

Still unmistakably Nike, and the Cinematic assignment is right — but it needed an argument,
because the mechanical reading of SPEC section 5 does not reach it. Rule 1 lists luxury,
automotive, hardware-flagship, console and aerospace; Nike is none of those by category,
and on a literal pass the file would fall through rules 2 and 3 to **Calm**. The rule's own
tell decides it instead: "full-bleed photography, sparse type and a slow reveal, not a dark
background." That is this file's entire thesis. Full-bleed editorial photography carries
every hero, sport tile and member-benefit card; the type is one 96px uppercase Futura tier
and then nothing until 32px; the Elevation section twice reaches for the word "cinematic"
unprompted to describe its own depth model. The white canvas is explicitly not a
counter-argument. So: Cinematic, kept, argued rather than inherited.

The one place the profile had to bend is the retail chrome. The file's own description calls
the brand "athletic, kinetic, and absolute", and a 400ms base on a filter chip in a dense
three-up PLP would read as a broken page rather than a premium one. I resolved that inside
the profile instead of switching away from it: chrome runs at `duration-instant` and
`duration-fast`, editorial surfaces at `duration-base` through `duration-emphasis`, both
drawn from the same Cinematic block, with the reason stated in the file as SPEC section 4
requires. Nike therefore still feels like its Cinematic siblings on the surfaces where
cinema is the point, and still feels like a fast shop everywhere else.

Nothing added here reads as borrowed. The focus ring is ink and paper because Nike's first
rule is that it has no accent colour — adding a generic focus blue would have been the one
change that genuinely broke the identity, and SPEC section 1 explicitly forbids it for a
monochrome brand. The motion table's distinctive rows are the slow image scale behind a
fixed headline and the extracted press collapse, both specific to this system. The two
roles the harness still reports missing are reported as a harness bug precisely so this
file does not acquire a `surface-1` or a `text-dim` that no Nike document would ever carry.
