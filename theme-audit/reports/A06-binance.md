## A06 · binance

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 4 | 5 | 2 | 3 | 1 | 1 |
| after | **5** | 5 | 2 | **5** | **5** | **5** |

Contrast is unchanged at 2 by design. All three remaining failures are either a frozen extracted brand value or a cross-theme pairing artefact of the harness; fixing either would require falsifying a hex or renaming a brand token, both of which SPEC §2 forbids. Both are documented in the file and filed below.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | G / B | `{component.button-trading-up}`, `{component.button-trading-down}` | Both declare `{colors.on-dark}` (#ffffff) labels on their fills: 2.13:1 on #0ecb81 and 3.53:1 on #f6465d. These are the Buy/Sell and Long/Short buttons — the highest-consequence controls in the product — and their labels are below AA. Not changed (extracted fact); filed under Needs approval. |
| P0 | B | `{component.text-link}` | Documented as yellow "also yellow on light". `{colors.primary}` on `{colors.canvas-light}` is 1.43:1 — unreadable at any size. Scoped in the file: yellow on light is a fill behind `{colors.on-primary}`, never ink. |
| P0 | F | whole file | No motion tokens, no `## Motion & Animation`, no reduced-motion rule. The file's Known Gaps declared timings "not in scope", so the gap was documented but unaddressed. |
| P0 | A / E | whole repo, this file included | No `focus` role and no focus ring token. The Elevation table referenced a ring (`0 0 0 2px {colors.info-ring}` at 50% alpha) that no token backed, and at 50% alpha that ring does not reach 3:1 on `{colors.primary}`. |
| P1 | B | `{colors.muted}` (#707a8a) | Fails AA body contrast on **all four** surfaces the file defines: 4.34:1 on canvas-light, 4.16:1 on surface-soft-light, 4.46:1 on canvas-dark, 3.65:1 on surface-card-dark. The harness only caught two of the four. It is used for 12px captions and footer links. Real brand failure. |
| P1 | B | `{colors.trading-up}` as text on `{colors.canvas-light}` | 2.13:1. `{component.price-chart-card}` is a white card and charts price-up in this green. Dark theme is fine (9.10:1); the light theme has no passing green and this file has no token for one. |
| P1 | A / E | hairline family | `{colors.hairline-on-light}` 1.18:1, `{colors.hairline-on-dark}` 1.48:1, `{colors.border-strong}` 1.53:1 — all below the 3:1 a boundary needs, and `{component.text-input-on-light}` used a hairline as its only boundary. Frozen values, so a parallel token was added per SPEC §2. |
| P1 | H | Components section | Only `active` and `disabled` documented. `hover`, `focus-visible`, `pressed`, `loading`, `selected`, `error` appeared nowhere. Root cause was in the file itself: Iteration Guide rule 5 said "Never document hover." |
| P1 | G | Responsive Behavior > Touch Targets | Claimed 40 × 40px "meets WCAG AAA's 44 × 44". It does not — AAA 2.5.5 wants 44px. Overstated conformance claim. |
| P1 | C | Elevation & Depth | Prose claimed canvas → card is "a 12-step lightness jump that reads as a clear elevation boundary". Measured it is 1.22:1 (card → elevated 1.21:1). Legible on a calibrated screen, near-invisible in bright light. |
| P2 | C / A | Elevation & Depth | One row documented a real "subtle drop shadow" with no value and no token, so elevation mixed a tone step, a hairline and an undefined shadow. A `shadow:` group now carries all three, per SPEC §1. |
| P2 | B | harness artefact | `ink on surface-card-dark` = 1.10:1. `{colors.ink}` is light-mode text; `{colors.surface-card-dark}` is a dark-mode surface. They never co-occur — dark-mode body is `{colors.body}` at 13.36:1. Harness limitation, see Shared issues. |
| P2 | E | `rounded` | `pill: 9999px` and `full: 9999px` are duplicate values under two names. Extracted and semantically distinct in the prose (pill CTAs vs circular avatars); left alone. |
| P2 | D | `typography` | Every role carries size, weight and line height; no gaps. `{typography.button}` at lineHeight 1 is intentional for a fixed-height button. No action. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#1f6feb"`, `focus-on-dark: "#3b82f6"` | Fills the missing `focus` role. Two tokens because SPEC §1 requires it of a file with both light and dark signature surfaces, and because no single ring reaches 3:1 on both `{colors.surface-elevated-dark}` and `{colors.primary}`. |
| frontmatter `colors:` | — -> `muted-readable: "#5e6673"` | Parallel accessible token for `{colors.muted}`, per SPEC §2. The frozen value stays and is scoped to large text. |
| frontmatter `colors:` | — -> `border-control: "#848e9c"` | Parallel accessible boundary for the three decorative-strength hairlines. One token clears 3:1 on every surface in both themes. |
| frontmatter | — -> `shadow:` group (`focus-ring`, `focus-ring-on-dark`, `card-over-image`) | The prose documented a ring and a card shadow with no tokens; SPEC §1 asks for a `shadow:` group where it does. |
| frontmatter | — -> `motion:` group, nine keys, **Calm** profile | SPEC §4. 250ms base, 40ms stagger; easings biased symmetric per §5 Calm rather than the §4 sample's near-linear-out. |
| Colors > Hairlines & Borders | — -> `{colors.border-control}` entry with all four measured ratios, and the extracted hairlines explicitly scoped to decoration | States the real failure instead of hiding it. |
| Colors > Text | `muted-strong` one-liner -> ratios on all surfaces + light-surface use forbidden; new `{colors.muted-readable}` entry | #929aa5 is 2.84:1 on white; nothing in the file said not to use it there. |
| Colors > Info / Focus | — -> two focus entries with every measured ratio and the reason yellow is not the ring | Brief dimension A. |
| Elevation & Depth table | shadow with no value; ring at 50% alpha -> `{shadow.card-over-image}`; `{shadow.focus-ring}` / `{shadow.focus-ring-on-dark}` at full alpha | Resolves the untokenised shadow, and 50% alpha would drop the ring below 3:1 on yellow. |
| Elevation & Depth prose | "12-step lightness jump … clear elevation boundary" -> measured 1.22:1 / 1.21:1 / 1.48:1 + a rule that a card may not rely on the tone step alone | The claim was false as written. |
| Components > **new** `### States` | — -> 14-row component × 8-state table, every inferred state labelled **prescribed**, plus an explicit list of the 14 genuinely-static components | SPEC §7 and brief H, including "a component with genuinely two states says so". |
| **new** `## Motion & Animation` | — -> prescribed-not-measured first line, profile rationale, 12-row interaction table, unused-token note, `@media (prefers-reduced-motion: reduce)` subsection | SPEC §3, §6 and brief F. |
| **new** `## Accessibility` | — -> 26-row contrast table, four plainly-stated real failures, per-surface focus-ring table, declared control sizes with the AA/AAA distinction, reduced motion | SPEC §3 and brief G. |
| Do's and Don'ts > Don't | — -> two motion rules (no spring/overshoot; never animate layout properties); yellow-on-light rule now carries its 1.43:1 measurement | Keeps the motion system enforceable in the file's own voice. |
| Responsive > Touch Targets | "meets WCAG AAA's 44 × 44" -> clears AA 2.5.8 (24px), does not clear AAA 2.5.5 (44px) on height alone | The original was a false conformance claim. |
| Iteration Guide rule 5 | "Never document hover." -> prescribed states are allowed and must stay labelled; extracted states named | This line was the root cause of the states gap, and it is inside my owned file. |
| Known Gaps | "Animation and transition timings … are not in scope." -> every motion value is prescribed, not extracted; chart redraw needs a live recording | The gap moved rather than vanished. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via `theme-audit/audit.py`'s own `contrast()`.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #181a20 / canvas-light #ffffff | 17.39 | 4.5 | Pass |
| body #eaecef / canvas-dark #0b0e11 | 16.35 | 4.5 | Pass |
| body #eaecef / surface-card-dark #1e2329 | 13.36 | 4.5 | Pass |
| body #eaecef / surface-elevated-dark #2b3139 | 11.08 | 4.5 | Pass |
| ink #181a20 / surface-soft-light #fafafa | 16.66 | 4.5 | Pass |
| ink #181a20 / surface-strong-light #f5f5f5 | 15.95 | 4.5 | Pass |
| ink #181a20 / surface-card-dark #1e2329 | 1.10 | 4.5 | Fail — cross-theme pairing, never rendered |
| muted #707a8a / canvas-light #ffffff | 4.34 | 4.5 | Fail |
| muted #707a8a / surface-soft-light #fafafa | 4.16 | 4.5 | Fail |
| muted #707a8a / canvas-dark #0b0e11 | 4.46 | 4.5 | Fail |
| muted #707a8a / surface-card-dark #1e2329 | 3.65 | 4.5 | Fail |
| muted-readable #5e6673 / canvas-light #ffffff | 5.79 | 4.5 | Pass (prescribed) |
| muted-readable #5e6673 / surface-strong-light #f5f5f5 | 5.32 | 4.5 | Pass (prescribed) |
| muted-strong #929aa5 / canvas-dark #0b0e11 | 6.81 | 4.5 | Pass |
| muted-strong #929aa5 / surface-card-dark #1e2329 | 5.56 | 4.5 | Pass |
| muted-strong #929aa5 / surface-elevated-dark #2b3139 | 4.61 | 4.5 | Pass |
| muted-strong #929aa5 / canvas-light #ffffff | 2.84 | 4.5 | Fail — light use now forbidden in the file |
| on-primary #181a20 / primary #fcd535 | 12.18 | 4.5 | Pass |
| on-primary #181a20 / primary-active #f0b90b | 9.65 | 4.5 | Pass |
| on-primary #181a20 / accent-turquoise #2dbdb6 | 7.51 | 4.5 | Pass |
| primary #fcd535 / canvas-dark #0b0e11 | 13.55 | 4.5 | Pass |
| primary #fcd535 / surface-card-dark #1e2329 | 11.08 | 4.5 | Pass |
| primary #fcd535 / canvas-light #ffffff | 1.43 | 4.5 | Fail |
| on-dark #ffffff / trading-up #0ecb81 | 2.13 | 4.5 | Fail |
| on-dark #ffffff / trading-down #f6465d | 3.53 | 4.5 | Fail |
| on-primary #181a20 / trading-up #0ecb81 | 8.18 | 4.5 | Pass (proposed replacement) |
| on-primary #181a20 / trading-down #f6465d | 4.93 | 4.5 | Pass (proposed replacement) |
| trading-up #0ecb81 / canvas-dark #0b0e11 | 9.10 | 4.5 | Pass |
| trading-down #f6465d / canvas-dark #0b0e11 | 5.49 | 4.5 | Pass |
| trading-up #0ecb81 / canvas-light #ffffff | 2.13 | 4.5 | Fail |
| trading-down #f6465d / canvas-light #ffffff | 3.53 | 4.5 | Fail |
| hairline-on-light #eaecef / canvas-light #ffffff | 1.18 | 3.0 | Fail — decorative only |
| hairline-on-dark #2b3139 / canvas-dark #0b0e11 | 1.48 | 3.0 | Fail — decorative only |
| border-strong #cdd1d6 / canvas-light #ffffff | 1.53 | 3.0 | Fail — decorative only |
| border-control #848e9c / canvas-light #ffffff | 3.32 | 3.0 | Pass (prescribed) |
| border-control #848e9c / surface-strong-light #f5f5f5 | 3.04 | 3.0 | Pass (prescribed) |
| border-control #848e9c / surface-card-dark #1e2329 | 4.77 | 3.0 | Pass (prescribed) |
| border-control #848e9c / canvas-dark #0b0e11 | 5.83 | 3.0 | Pass (prescribed) |
| focus #1f6feb / canvas-light #ffffff | 4.63 | 3.0 | Pass |
| focus #1f6feb / surface-soft-light #fafafa | 4.44 | 3.0 | Pass |
| focus #1f6feb / surface-strong-light #f5f5f5 | 4.25 | 3.0 | Pass |
| focus #1f6feb / primary #fcd535 | 3.25 | 3.0 | Pass |
| focus #1f6feb / surface-elevated-dark #2b3139 | 2.83 | 3.0 | Fail — which is why focus-on-dark exists |
| focus-on-dark #3b82f6 / canvas-dark #0b0e11 | 5.26 | 3.0 | Pass |
| focus-on-dark #3b82f6 / surface-card-dark #1e2329 | 4.30 | 3.0 | Pass |
| focus-on-dark #3b82f6 / surface-elevated-dark #2b3139 | 3.57 | 3.0 | Pass |
| canvas-dark / surface-card-dark (elevation step) | 1.22 | — | Weak but legible |
| surface-card-dark / surface-elevated-dark (elevation step) | 1.21 | — | Weak but legible |
| canvas-light / surface-soft-light (elevation step) | 1.04 | — | Effectively flat |

### Motion inventory

Profile **Calm**. Every value prescribed, none measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | 150ms `{motion.duration-fast}` | `{motion.ease-standard}` | opacity on fill layer; no lift, no scale | instant, no transition |
| Press | 80ms `{motion.duration-instant}` | `{motion.ease-exit}` | opacity to 0.88; no scale (hit target must not move) | instant, opacity only |
| Focus-visible ring | 80ms | `{motion.ease-enter}` | opacity on the ring shadow | appears instantly, never animated away |
| Page / route transition | 250ms `{motion.duration-base}` | `{motion.ease-standard}` | opacity only; no slide across the dark→light theme flip | cross-fade ≤150ms, no travel |
| Modal / drawer enter | 250ms | `{motion.ease-enter}` | opacity + translateY 8px → 0 | opacity only at 150ms |
| Modal / drawer exit | 150ms | `{motion.ease-exit}` | reverse of enter | opacity only at 120ms |
| Dropdown enter | 150ms | `{motion.ease-enter}` | opacity + translateY 4px → 0 | opacity only at 120ms |
| Dropdown exit | 80ms | `{motion.ease-exit}` | opacity | opacity only at 80ms |
| Toast | 250ms in, 4s hold, 150ms out | enter / exit | opacity + translateY 12px → 0 | opacity only at 150ms, same hold, no travel |
| List enter | 150ms per item, 40ms `{motion.stagger-step}`, capped at 8 | `{motion.ease-enter}` | opacity only; rows never travel | all fade together at 150ms, stagger dropped |
| List exit | 80ms, no stagger | `{motion.ease-exit}` | opacity | opacity only at 80ms |
| Loading | 1200ms loop (only permitted infinite animation) | `{motion.ease-standard}` | opacity pulse 0.4→0.8; rotate() on spinner | spinner freezes to a static glyph; skeletons hold opacity 0.6 |
| Price-change flash | 80ms in, 400ms out | `{motion.ease-exit}` | opacity on a tint layer behind the cell; the number never moves | removed entirely — arrow + cell colour already carry direction |

Exit is shorter than its matching entrance in every pair. `{motion.duration-emphasis}` (600ms) is defined per SPEC §4 and has no assigned use; the file says so.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 158–161 | `check()` pairs one representative `text` token against one representative `surface` token with no theme awareness. For a dual-theme file it manufactures a failure that can never render: `ink` (#181a20, light-mode ink) against `surface-card-dark` (#1e2329, dark-mode card) = 1.10:1. The real dark-mode pair, `body` on `surface-card-dark`, is 13.36:1 and never checked. This costs binance 1 contrast point for a pairing that does not exist, and will hit every light+dark file in the collection. | Partition `colors` by theme suffix (`-dark` / `-on-dark` vs `-light` / `-on-light`, defaulting unsuffixed keys to both) and check text against surfaces within the same partition only. Minimum viable version: when a candidate fg/bg pair's key suffixes conflict (`-on-light`-family ink on a `-dark` surface), skip the pair and record it under a new `theme_mismatch_skipped` field so it is visible rather than silently dropped. |
| `theme-audit/audit.py` line 125 + 26–28 | `text-dim` resolves with `find_role` (first pattern wins) while `border` and `focus` resolve with `find_role_strongest`. So a file that follows SPEC §2 and adds a parallel accessible secondary tone is still scored on the frozen failing one, and gets no credit for the fix. | Apply `find_role_strongest` to `text-dim` as well (lines 129–132), judged against the canvas. The role's threshold is about legibility, which is exactly the argument the docstring already makes for `border`. |
| `theme-audit/audit.py` lines 170–172 | The signal-colour sweep matches `^(primary|accent|secondary|brand|cta)` only, so semantic action colours under other names escape. Here `trading-up` / `trading-down` are the fills of two real buttons whose declared labels measure 2.13:1 and 3.53:1 — the worst contrast defects in the file — and the harness reports neither. | Widen the pattern to include semantic action families (`^(success|error|danger|warning|positive|negative|up|down|trading)`), or better, derive the sweep from `components:` — any `backgroundColor` / `textColor` pair in that group is a real pairing and should be checked directly. That would catch this class in every file. |
| `theme-audit/SPEC.md` §3 | The section table fixes which sections are required but not their order, and §6 only says the motion table must exist. The briefs specify placement ("after `## Components`"); the SPEC does not, so 84 files could end up ordering them differently. | Add one line to §3: sections appear in the order listed in the table. |
| `theme-audit/SPEC.md` §4 vs §5 | §4 gives one literal token block, §5 says values are per profile and assigns Calm a "symmetric ease", but no profile's easing values are written down anywhere. Each reviewer invents its own curve for the same named profile, so `{motion.ease-standard}` will not mean the same thing across the collection. | Publish the four cubic-beziers per profile in the §5 table, the way base duration and stagger already are. |

### Needs approval

1. **White labels on the trading buttons.** `{component.button-trading-up}` and `{component.button-trading-down}` declare `{colors.on-dark}` (#ffffff): **2.13:1** on #0ecb81 and **3.53:1** on #f6465d, against 4.5:1. Nearest passing value: `{colors.on-primary}` (#181a20) → **8.18:1** and **4.93:1**, which also matches the brand's own black-on-colour logic on the yellow CTA. Not changed, because the white label is an extracted fact about the live product. Usage note that would make the real value defensible: none at AA — 3.53:1 clears the 3:1 large-text threshold only, and a 14px/600 button label is not large text, so there is no size at which the white-on-red label is conformant. If white must stay, the honest mitigation is a 1px `{colors.ink}` label shadow or a darker fill, both of which need brand approval.
2. **`{colors.muted}` #707a8a as secondary text.** 4.34:1 on canvas-light, 4.16:1 on surface-soft-light, 4.46:1 on canvas-dark, 3.65:1 on surface-card-dark. Nearest passing values: #5e6673 on light (5.79:1, added as `{colors.muted-readable}`) and the already-extracted `{colors.muted-strong}` #929aa5 on dark (5.56:1 on the card). Usage note that makes the real value defensible: `{colors.muted}` is conformant only at the 3:1 large-text threshold — 18.66px/700 or 24px/400 and above — where it passes on all four surfaces. The file currently uses it for 12px captions, footer links and table column headers, none of which qualify. Approval needed either to substitute or to accept the failure.
3. **`{colors.primary}` #FCD535 as ink on light surfaces.** 1.43:1 on #ffffff. There is no size at which this is defensible; it is below even the 3:1 non-text threshold. Nearest passing value: `{colors.focus}` #1f6feb at 4.63:1, or `{colors.ink}` with an underline. The file now scopes yellow on light to fills only; approval needed to amend `{component.text-link}`, which still documents yellow links in both themes.
4. **No light-theme green.** `{colors.trading-up}` is 2.13:1 on white, and `{component.price-chart-card}` is a white card that plots price-up in it. A light-theme-only darker green (around #0a8f5c, 4.6:1 on white) would be a new brand token and is therefore not invented here.
5. **Motion profile Calm, retained with a caveat.** Calm is correct under SPEC §5's assignment rules — Binance is dark-canvas but not luxury, and not a developer tool, so rules 1–3 do not fire and rule 4 applies. It is retained. But a trading platform has the strongest Crisp signals of any Calm site in the collection: dense tabular data, live price feeds, and controls whose latency is read as system latency. Rather than switch silently, the file resolves it inside Calm by routing price-direction and press feedback to `{motion.duration-instant}` (80ms) while editorial surfaces hold `{motion.duration-base}` (250ms). If the collection later wants a per-surface profile split, Binance is the strongest candidate for it; that is a SPEC change, not a file change.

### Identity verdict

Still unmistakably Binance. The yellow-does-everything rule survives untouched — no second brand colour was introduced, and the three prescribed tokens are deliberately *not* yellow precisely to protect that scarcity: a mid-blue focus ring, a deepened in-family grey, and #848e9c, which is Binance's own tertiary grey promoted to a boundary role. The dual-theme story (dark marketing / light transactional, one yellow CTA across both) is now stronger than before, because the focus ring is specified by the surface it is drawn against rather than by theme, which is the same logic the brand already applies to its CTA.

The motion section is the main identity risk in any of these additions, and it was written against the brand rather than from a template: no scale on press because a scaling Buy button moves the hit target in a dense order panel; no slide on route transitions because the dark→light flip would read as a flash; an 80ms price-change flash on a 250ms base because a slow fade on a changing price misrepresents when the price changed; and the Don't list gained "no spring, no bounce" in the file's own voice. The price-change flash row has no analogue in any other file in the collection — it only makes sense for a market.

Two things read as borrowed and are worth flagging. The nine motion token names and the three `duration` values I kept verbatim from SPEC §4 are collection-wide by design, so `motion:` will look identical across 84 files; that is the SPEC's intent, not drift, but it does mean the token block alone no longer identifies the brand. And the Accessibility section's structure is generic by necessity — a contrast table is a contrast table. The brand-specific content there is the red/green deuteranopia note, which matters more on this site than on any other in the set, since this brand encodes gain and loss in exactly the pair that colour-vision deficiency collapses.

Net: the file gained 220 lines and lost none of its voice. The one place it reads less confidently than before is deliberate — the elevation prose no longer claims a "clear elevation boundary" it does not have, and the touch-target line no longer claims AAA conformance it never met.
