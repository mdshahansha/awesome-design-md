## A10 · cal

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

`4 · 5 · 3 · 3 · 1 · 1` -> `5 · 5 · 4 · 5 · 5 · 5`

Contrast stops at 4 by design: the one remaining harness failure is the real brand's own blue, which is frozen as an extracted fact (see Needs approval).

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A, G | `colors.focus` | No focus token and no focus treatment anywhere in the file. Every control was keyboard-invisible, and the Iteration Guide actively instructed authors not to document states beyond default and pressed. |
| P0 | F | Motion | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Zero durations, zero easings in the file. |
| P0 | G | Accessibility | No `## Accessibility` section. Four real AA failures in the palette were undocumented. |
| P0 | B | `colors.hairline` on `canvas` | 1.24:1 against the 3.0:1 needed for a component boundary, and it was the *only* edge of `text-input`, `button-secondary` and `button-icon-circular`. Confirmed. |
| P0 | H | Components | Only `hover` and `active` were documented, and `active` only incidentally. `focus-visible`, `pressed`, `disabled`, `loading`, `selected`, `error` appeared nowhere in structured Components lines. Confirmed. |
| P1 | B | `colors.brand-accent` #3b82f6 | 3.68:1 both as link text on canvas and as a white-text fill. Real brand fails AA. Confirmed. |
| P1 | B | `colors.muted-soft` #898989 | 3.50:1 on canvas, 3.21:1 on surface-card — fails 4.5:1 body text. Was documented as the caption and fine-print tone with no caveat. |
| P1 | B | `colors.error` / `success` / `warning` | 3.76 / 2.54 / 2.15:1 on canvas. All three were described as text-carrying states ("validation errors") while being fill-only tones. |
| P1 | C | Elevation & Depth | Elevation was expressed three ways at once — tint, hairline border, and a shadow stated as a raw `rgba(...)` string with no token. Several components claimed "hairline border, subtle drop shadow" simultaneously. |
| P1 | C | Surface layers | canvas→surface-soft 1.05:1, canvas→surface-card 1.09:1, surface-soft→surface-card 1.03:1, surface-dark→surface-dark-elevated 1.09:1. The layers are not distinguishable by tint alone; the file presented them as a working elevation ladder. |
| P1 | G | Responsive Behavior → Touch Targets | Two false claims: 40 × 40 stated as a sufficient "minimum", and 36 × 36 excused because "the centered icon and full-circle silhouette compensate". A third claim (`category-tab` "meets 44px+") is not computable from a document at all. |
| P1 | I | Motion profile | Roster assigns **Playful**; the file's own evidence says **Calm**. Argued and switched openly — see Identity verdict. |
| P2 | B | `colors.ink` on `colors.badge-violet` | 4.46:1, short of 4.5:1 by 0.04, with 13px `caption` labels specified on it. |
| P2 | B | `colors.muted` on `colors.surface-card` | 4.43:1 — passes on canvas (4.83:1), fails inside the gray feature cards where it is actually used. |
| P2 | E | `rounded.pill` / `rounded.full` | Two tokens, one value (9999px). Not a defect, but the ladder reads as seven steps when it is six. `rounded.xs` (4px) has no documented use. |
| P2 | A | Typography | All 13 roles carry size, weight and line height — dimension D passes with nothing to fix. Recorded for completeness. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-strong: "#868d97"` | Prescribed accessible parallel to the frozen 1.24:1 hairline; 3.35:1 on canvas. Satisfies the `border` role on its strongest variant. |
| frontmatter `colors:` | — -> `focus: "#2563eb"`, `focus-on-dark: "#60a5fa"` | The missing role. Two rings because the file documents a dark footer and a dark featured tier; one blue cannot clear 3:1 on both #ffffff and #101010. |
| frontmatter `colors:` | — -> `brand-accent-strong: "#1d4ed8"` | Accessible sibling for the brand blue wherever it carries text weight. 6.70:1. |
| frontmatter `colors:` | — -> `success-text`, `warning-text`, `error-text` | The three extracted semantic hexes are fills, not text tones. Parallel tones at 5.48 / 7.09 / 6.47:1. |
| frontmatter | — -> `shadow:` group (`none`, `small`, `medium`, `focus-ring`) | The Elevation prose already stated two real `rgba(...)` values with no token to reference. |
| frontmatter | — -> `motion:` group, 9 keys, **Calm** profile | SPEC §4/§5. Base 250ms, symmetric `cubic-bezier(0.4, 0, 0.2, 1)`, 40ms stagger. |
| Colors → Brand & Accent | accent described as "used sparely" -> plus measured 3.68:1 and a plain statement that the real brand fails AA | Honest failure beats a silent one. |
| Colors → Surface | hairline-soft/hairline unqualified -> each labelled decorative with its measured ratio; `hairline-strong` scoped to control edges | Scopes the frozen tone, adds the accessible one. |
| Colors → Text | muted / muted-soft unqualified -> measured, with the 18px+ usage note on muted-soft and a step-up rule for muted inside gray cards | Makes the real values defensible instead of removing them. |
| Colors → new **Focus** subsection | — -> both rings, every measured ratio, geometry | Dimension A/E/G. |
| Colors → Semantic | three fills described as text states -> measured, scoped to fills, with text parallels | |
| Elevation & Depth | 5 mixed-mechanism rows, raw rgba in prose -> 5 numbered levels, one mechanism each, all shadows tokenised; plus the measured layer ratios and an explicit "tint alone does not separate layers" rule | Dimension C. |
| Shapes | — -> pill/full collapse note, `rounded.xs` note, **Focus Ring Geometry** subsection | Dimension E; keeps the ring inside the existing radius ladder. |
| Components → `button-secondary`, `button-icon-circular`, `text-input` | `{colors.hairline}` edge -> `{colors.hairline-strong}`, with the extracted value named | These three are the controls whose only boundary is the border. |
| Components → `text-input-focused` | "border thickens" -> border + `{shadow.focus-ring}` | Focus was a tonal shift only. |
| Components → `text-link` | "(not documented per the no-hover policy)" -> hover documented; blue links routed to `brand-accent-strong` | |
| Components → new **Component States** matrix | — -> 16-row × 8-state table, prescribed cells marked **(p)**, genuinely-two-state components stated as such | Dimension H. All 8 state words now appear in structured Components lines. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and was not measured. Includes the Calm-vs-Playful argument, a 10-row inventory, the five motion rules, and the reduced-motion CSS block. |
| after Motion | — -> `## Accessibility` | Measured contrast table, per-surface focus-ring table, tap-target honesty, keyboard/semantics, reduced motion. |
| Do's and Don'ts | hover Don't -> corrected, plus three new Don'ts (never drop the ring; never use the four failing tones as text/control edges; no scale pops) | |
| Iteration Guide rule 4 | "Never document hover. Default and Active/Pressed states only." -> document every supported state, including "no visual change" | This one line was the root cause of the states gap and directly contradicted the new section. |
| Responsive → Touch Targets | three unverifiable/false claims -> stated token heights with the 44 × 44 shortfall named; the pill claim withdrawn | SPEC: tap-target size is not computable from a document. |
| Known Gaps | 1 motion line -> 7 lines labelling every prescribed addition | Nothing new is passed off as extracted. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #111111 / canvas #ffffff | 18.88:1 | 4.5 | Pass |
| ink / surface-soft #f8f9fa | 17.91:1 | 4.5 | Pass |
| ink / surface-card #f5f5f5 | 17.32:1 | 4.5 | Pass |
| ink / surface-strong #e5e7eb | 15.25:1 | 4.5 | Pass |
| body #374151 / canvas | 10.31:1 | 4.5 | Pass |
| body / surface-card | 9.45:1 | 4.5 | Pass |
| muted #6b7280 / canvas | 4.83:1 | 4.5 | Pass |
| muted / surface-soft | 4.59:1 | 4.5 | Pass |
| muted / surface-card | 4.43:1 | 4.5 | **Fail** |
| muted-soft #898989 / canvas | 3.50:1 | 4.5 | **Fail** |
| muted-soft / surface-card | 3.21:1 | 4.5 | **Fail** |
| on-primary #ffffff / primary #111111 | 18.88:1 | 4.5 | Pass |
| on-primary / primary-active #242424 | 15.52:1 | 4.5 | Pass |
| on-primary / brand-accent #3b82f6 | 3.68:1 | 4.5 | **Fail** |
| on-primary / brand-accent-strong #1d4ed8 | 6.70:1 | 4.5 | Pass (prescribed) |
| on-dark #ffffff / surface-dark #101010 | 19.03:1 | 4.5 | Pass |
| on-dark-soft #a1a1aa / surface-dark | 7.42:1 | 4.5 | Pass |
| on-dark-soft / surface-dark-elevated #1a1a1a | 6.79:1 | 4.5 | Pass |
| brand-accent / canvas | 3.68:1 | 4.5 | **Fail** |
| brand-accent / surface-card | 3.37:1 | 4.5 | **Fail** |
| hairline #e5e7eb / canvas | 1.24:1 | 3.0 | **Fail** |
| hairline-soft #f3f4f6 / canvas | 1.10:1 | 3.0 | **Fail** (decorative, scoped) |
| hairline-strong #868d97 / canvas | 3.35:1 | 3.0 | Pass (prescribed) |
| hairline-strong / surface-card | 3.07:1 | 3.0 | Pass (prescribed) |
| success #10b981 / canvas | 2.54:1 | 4.5 | **Fail** (fill only) |
| warning #f59e0b / canvas | 2.15:1 | 4.5 | **Fail** (fill only) |
| error #ef4444 / canvas | 3.76:1 | 4.5 | **Fail** (fill only) |
| success-text #047857 / canvas | 5.48:1 | 4.5 | Pass (prescribed) |
| warning-text #92400e / canvas | 7.09:1 | 4.5 | Pass (prescribed) |
| error-text #b91c1c / canvas | 6.47:1 | 4.5 | Pass (prescribed) |
| ink / badge-orange #fb923c | 8.34:1 | 4.5 | Pass |
| ink / badge-pink #ec4899 | 5.35:1 | 4.5 | Pass |
| ink / badge-emerald #34d399 | 9.82:1 | 4.5 | Pass |
| ink / badge-violet #8b5cf6 | 4.46:1 | 4.5 | **Fail** |
| focus #2563eb / canvas | 5.17:1 | 3.0 | Pass |
| focus / surface-soft | 4.90:1 | 3.0 | Pass |
| focus / surface-card | 4.74:1 | 3.0 | Pass |
| focus / surface-strong | 4.17:1 | 3.0 | Pass |
| focus / primary #111111 (black CTA) | 3.65:1 | 3.0 | Pass |
| focus / surface-dark #101010 | 3.68:1 | 3.0 | Pass (but focus-on-dark used instead) |
| focus-on-dark #60a5fa / surface-dark | 7.48:1 | 3.0 | Pass |
| focus-on-dark / surface-dark-elevated | 6.85:1 | 3.0 | Pass |
| focus-on-dark / canvas | 2.54:1 | 3.0 | **Fail** — dark surfaces only, stated in the file |
| canvas / surface-soft (layer separation) | 1.05:1 | — | not distinguishable |
| canvas / surface-card (layer separation) | 1.09:1 | — | not distinguishable |
| surface-soft / surface-card (layer separation) | 1.03:1 | — | not distinguishable |
| surface-dark / surface-dark-elevated (layer separation) | 1.09:1 | — | not distinguishable |

### Motion inventory

Profile: **Calm** (roster assigns Playful — argued below). All values prescribed, none measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity`; underline `transform: scaleX()` | Underline instant, no scale; fade kept at 150ms |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity`; fill swap immediate, no scale pop | Unchanged — already no travel |
| Focus ring appear | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `opacity` | No transition at all; focus never lags the key |
| Page / route transition | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` | Cross-fade 150ms, no translate |
| Modal / drawer | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(12px)` (drawer `translateX`); scrim opacity only | Fade 150ms, no translate |
| Dropdown | 150ms in / 80ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(4px)` | Opacity only, 150ms |
| Toast | 250ms in / 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(16px)` | Opacity only; dismiss timer lengthened, never removed |
| List enter | 250ms per item, `{motion.stagger-step}` 40ms, 6 items max | `{motion.ease-enter}` | `opacity` + `translateY(8px)` | All together, 150ms, no stagger, no translate |
| List exit | 150ms | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | Opacity only, 150ms |
| Loading | 800ms, infinite | linear (spinner) / `{motion.ease-standard}` (skeleton) | `rotate()`; skeleton `opacity` 0.6→1 | Spinner frozen, replaced by a static "Loading…" label; pulse frozen mid-opacity |

`transform` and `opacity` only; every exit shorter than its entrance; nothing animates on first paint; the two loaders are the only infinite animations and there is no brand ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/roster.md` line 17 | Assigns `cal` the **Playful** profile. Cal.com's action layer is monochrome (#111111 CTAs), the Don'ts forbid accent colour on CTAs, the pastels appear only on avatar fills, and the type voice is weight-600 geometric. SPEC §5 rule 3 requires saturation *and role*; neither holds. Rules 1 and 2 do not apply, so rule 4 → Calm. | Change the profile column for A10 from `Playful` to `Calm`. |
| `theme-audit/audit.py` lines 169-178 | Signal-colour check pairs the file's single `on-accent` ink against every token matching `^(primary\|accent\|secondary\|brand\|cta)`, including tokens the brand never fills with text. `brand-accent` here is a link and badge tone; white is never placed on it, so the file is charged a permanent failure for a pair that does not exist in the design. | Either exempt tokens whose prose scopes them to decoration, or let a file declare a paired ink per signal token (e.g. `brand-accent` ← `ink`), rather than assuming one global `on-accent`. |
| `theme-audit/audit.py` line 31 | `accent` role pattern puts `^primary$` first, so for a monochrome brand the "signal colour" resolves to near-black #111111 and the real brand accent is never the one checked as the accent role. Correct for this file as it happens, but it means `focus on accent` is measured against the CTA fill rather than the brand hue. | Low priority: document that `accent` means "the dominant action colour", not "the brand's chromatic hue". No code change needed if so. |
| `theme-audit/SPEC.md` §2 | The frozen-value rule and the "do not change an identity hex" rule both apply to `brand-accent`, and the harness scores a permanent -1 for honouring them. A file that does everything the spec asks cannot reach contrast 5. | State explicitly that a scoped-and-documented frozen failure caps contrast at 4, so reviewers do not chase an unreachable 5. |

### Needs approval

1. **`colors.brand-accent` #3b82f6 — white text on it, 3.68:1 (required 4.5:1).** Not changed; it is the extracted brand hue. Nearest passing value: **#1d4ed8** (6.70:1 with white), added alongside as `brand-accent-strong`. Usage note that makes the real value defensible: #3b82f6 clears the 3:1 large-text threshold, so it is defensible for 18px+/14px-bold display text and for badge fills and icon strokes — never for 16px body links or white-on-blue button labels. This is the one remaining harness contrast failure and the reason the score is 4 rather than 5.
2. **`colors.brand-accent` as link text on canvas, 3.68:1.** Same token, same decision. Usage note: blue inline links at `{typography.body-md}` (16px / 400) must use `brand-accent-strong`.
3. **`colors.hairline` #e5e7eb on canvas, 1.24:1 (required 3.0:1).** Not changed. Nearest passing value: **#868d97** (3.35:1), added as `hairline-strong`. Usage note: #e5e7eb is defensible as a decorative rule — table dividers, section separators, card outlines that sit beside a tint — but not as the sole boundary of an input or button.
4. **`colors.muted-soft` #898989 on canvas, 3.50:1.** Not changed. Nearest passing value: **#757575** (4.61:1). Usage note: defensible at 18px+ or 14px bold, where 3:1 applies; copyright and fine-print lines below that size must use `colors.muted`.
5. **`colors.error` / `success` / `warning` as text, 3.76 / 2.54 / 2.15:1.** Not changed. Parallel text tones added (#b91c1c, #047857, #92400e). Usage note: the extracted trio are badge fills and icon tones observed inside product-UI fragments, where ink sits on top of them, not on the canvas.
6. **`colors.ink` on `colors.badge-violet` #8b5cf6, 4.46:1.** Fails by 0.04. Not changed. Nearest passing violet with ink on it would be lighter than the observed hex; instead the file forbids 13px labels on violet badges. Alternative if a violet label is required: white on **#6d28d9** (7.10:1).
7. **Motion profile switched from Playful to Calm**, per the brief's instruction to argue rather than switch silently. The file documents Calm and carries the argument in its own Motion section. `roster.md` still says Playful and I may not edit it.
8. **One Iteration Guide rule rewritten** ("Never document hover" → document every supported state). It was the direct cause of the states gap and contradicted the new required sections, but it was a deliberate authorial rule, so it is flagged rather than quietly dropped.

### Identity verdict

Still unmistakably Cal.com. Nothing was removed and no extracted hex was altered; every addition is either a measured ratio of a value already in the file, or a prescribed parallel that is named as prescribed and scoped beside the real tone it protects. The near-monochrome action layer, the Cal Sans / Inter split with its negative tracking, the pill-in-pill nav, the product-UI-fragments-as-content thesis, and the single dark footer all read exactly as before.

The two places where the file could have drifted were handled deliberately. The focus ring is the brand's own sparse blue, darkened until it passes, rather than a system-default outline — so the one new chromatic element in an otherwise monochrome system still belongs to Cal.com. And the motion system is Calm, not Playful: scale pops and springy overshoot would have been the real drift, contradicting this file's own warning that larger radii "read as consumer-app, not professional booking software". A Calm profile — 250ms, symmetric easing, opacity-led, almost no travel, no ambience, still page when the user is still — is the motion equivalent of "confident-not-shouting", which is the file's own phrase for the brand.

The Component States matrix is the one section that reads more like a generic design system than the rest of the document. That is unavoidable: a state matrix has a fixed shape. It is kept Cal-specific by recording "no visual change (brand policy)" where the brand genuinely does nothing on hover, by marking every prescribed cell, and by naming the three components that honestly have one or two states rather than inventing eight for them.
