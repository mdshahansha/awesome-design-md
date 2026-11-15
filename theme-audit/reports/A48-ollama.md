## A48 · ollama

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 4 | 5 | 1 | 3 | 1 | 1 |
| after | 4 | 5 | 5 | 5 | 5 | 5 |

`tokens` stays at 4: the only unsatisfied role is `text-dim`, and the palette plainly
contains it under another name. Per SPEC section 1 that is a harness bug to report, not
a token to invent, so nothing was added for it. See "Shared issues".

Two of the brief's three "already measured" premises were stale when I ran the harness:
`focus` is **not** missing (this file already defines `focus-ring`, which satisfies the
role), and the brief's instruction that "no file in this repo defines a focus ring"
does not hold for this site. The harness instead reported this file as one of two where
**no ring covers some of its surfaces** — `surface-soft` and `canvas`, best ring
`focus-ring` at 1.77:1 and 1.85:1. That is the real finding and it is resolved below
without renaming anything. The two hairline failures and the two missing sections
confirmed exactly as stated; the state list confirmed as stated.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A/E/G | `{colors.focus-ring}` | The extracted ring is `rgba(59,130,246,0.5)`. Composited over `{colors.canvas}` it is `#9dc0fa` at **1.85:1**, over `{colors.surface-soft}` 1.77:1, and over `{colors.surface-dark}` it composites to `#294c86` at 2.11:1. It fails 3:1 on every surface in the file, light and dark. The site ships the browser default as its only focus indicator. |
| P0 | F | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion` rule. Zero durations and zero easings anywhere in 539 lines. |
| P0 | G | whole file | No `## Accessibility` section, so four measured contrast failures were undisclosed. |
| P1 | B/E | `{colors.hairline}` 1.26:1, `{colors.hairline-strong}` 1.48:1 on canvas | Both extracted hairlines sit far below the 3:1 non-text threshold, and the file documents `{colors.hairline}` as the *only* boundary of `{component.text-input}` and `{colors.hairline-strong}` as the entire visual body of `{component.button-secondary}`. Decorative dividers at 1.26:1 are defensible; a control whose only affordance is a 1.26:1 rule is not. |
| P1 | B | `{colors.mute}` `#a3a3a3` | Documented for caption text and "lowest-emphasis utility text" at 2.52:1 on canvas. Fails 4.5:1 at every size and fails the 3:1 large-text allowance too, so there is no size at which it is compliant as text. The harness never flagged it — `mute` matches no role pattern, so it is measured by nothing. |
| P1 | H | every component | Only `active`, `pressed` and `disabled` were documented. The file's `> No hover states documented` policy note left hover, focus-visible, loading, selected and error entirely unaddressed, including on `{component.text-input}`, which has no error state anywhere. |
| P1 | G | Responsive Behavior → Touch Targets | Factually wrong claim: a 36px-tall pill "exceeds the 44×44px AAA threshold via the inline padding". Horizontal padding does not raise a height. It also cited the wrong bar — WCAG 2.2 AA is 2.5.8 (24×24); 44×44 is AAA 2.5.5. |
| P2 | A | `text-dim` role | Unsatisfied by regex although `{colors.mute}`, `{colors.body}` and `{colors.charcoal}` are all explicitly documented as secondary/caption/muted inks. Harness bug, not fixed in this file. |
| P2 | C | Elevation & Depth | Checked and clean: elevation is expressed one way only (hairline border, or inversion to `{colors.surface-dark}`), with no shadow mixed in, and the file says so explicitly. `canvas` → `surface-soft` is 1.04:1 — the layers are *not* distinguishable, which is intentional and already stated ("no surface alternation — the whole page is one continuous sheet"); `surface-soft` is a fill for pills, not a layer. No change made. |
| P2 | D | Typography | Checked and clean: all 13 roles carry family, size, weight, line height and letter spacing. Body at `{colors.body}` on `{colors.surface-soft}` is 4.54:1 — passing by 0.04, which I noted in the file as the darkest ground that ink may sit on. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-control: "#8f8f8f"` | Parallel accessible token (SPEC section 2). 3.23:1 on canvas, 3.10:1 on `surface-soft`. Nothing in the extracted palette does boundary work at 3:1: both hairlines fail, `mute` is 2.52:1, and `body`/`charcoal` are inks at 4.74:1/7.81:1 — a 1px rule that dark would break a brand whose whole premise is a paper-white sheet. Labelled prescribed in prose and in Known Gaps. |
| frontmatter `colors:` | — -> `focus-ring-strong: "#3b82f6"` | The coverage fix. Same blue as the extracted ring with the alpha removed — the hue was never the problem, the 50% transparency was. One ring clears 3:1 on all five grounds the harness derives (canvas, surface-card, surface-soft, surface-dark, ink-deep), so per SPEC section 1 a mid-luminance single ring is used rather than a `focus-on-dark` pair. `{colors.focus-ring}` is untouched and keeps its name. |
| frontmatter | — -> `motion:` group | Crisp profile block from SPEC section 5, verbatim, no deviation. |
| Colors → Surface | — -> `**Hairline Control**` entry | States the new token's job, its two measured ratios, and scopes both extracted hairlines to decoration. |
| Colors → Focus | one line -> two entries | `{colors.focus-ring}` relabelled as the extracted value with its composited 1.85:1 stated; `{colors.focus-ring-strong}` added with all four surface ratios, the 2px/2px offset, and why the ring is judged against the surface behind the control rather than the black pill it surrounds. |
| Components → intro note | `> No hover states documented per system policy.` -> extraction note | The old note read as a design fact. It is an extraction gap, and the new note says which states are extracted and which are prescribed. |
| Components | — -> `### State matrix` | 10 rows × 8 states, each marked (E) extracted, (P) prescribed, or `n/a` with a reason. `faq-row` and the three presentational cards are recorded as genuinely single-state per SPEC section 7; `text-input`'s error state is recorded as **undocumented** rather than invented. |
| Components → `button-secondary`, `text-input`, `search-pill-focused` | extracted values kept, substitutes added | Each keeps its extracted hairline/ring and now names the accessible substitute inline, so a reader sees both the real value and the usable one. |
| — -> `## Motion & Animation` (after Components) | new section | First line states the system is prescribed and was not measured from the live site. 10-interaction table (hover, press, focus, page transition, modal/drawer, dropdown, toast, list enter, list exit, loading) × duration × easing × property × reduced-motion, every value referenced as `{motion.*}`. Rules section, then a `@media (prefers-reduced-motion: reduce)` block stating what is removed and what remains. `transform` and `opacity` only; every exit shorter than its entrance. |
| — -> `## Accessibility` (after Motion) | new section | 16-pair measured contrast table, a "Where the real brand fails AA" subsection naming all three real failures with ratios, a per-surface focus-ring table, documented tap targets, and reduced motion. This is what moved contrast from 1 to 5: four failures disclosed, none altered. |
| Responsive Behavior → Touch Targets | `exceeds the 44×44px AAA threshold via the inline padding` -> AA 2.5.8 pass / AAA 2.5.5 fail, documented not measured | The old sentence was false and cited the wrong threshold. |
| Do's and Don'ts | — -> 3 Do's, 3 Don'ts | Motion ceiling, focus ring, hairline scoping; and the three corresponding prohibitions. |
| Known Gaps | 5 entries -> 9 | Records that all motion is prescribed, that both new tokens are prescribed and have no live counterpart, that the (P) state rows were never observed, and that validation states and ARIA/keyboard order are absent from the captured surfaces. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via `python3`; alpha tokens composited over the ground they are drawn on first.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#000000` / `canvas` `#ffffff` | 21.0:1 | 4.5:1 | Pass |
| `ink` / `surface-soft` `#fafafa` | 20.12:1 | 4.5:1 | Pass |
| `charcoal` `#525252` / `canvas` | 7.81:1 | 4.5:1 | Pass |
| `body` `#737373` / `canvas` | 4.74:1 | 4.5:1 | Pass |
| `body` / `surface-soft` | 4.54:1 | 4.5:1 | Pass (margin 0.04) |
| `mute` `#a3a3a3` / `canvas` | 2.52:1 | 4.5:1 | **Fail — real, disclosed** |
| `mute` / `surface-soft` | 2.42:1 | 4.5:1 | Fail — disabled pairing only, no WCAG requirement |
| `on-primary` `#ffffff` / `primary` `#000000` | 21.0:1 | 4.5:1 | Pass |
| `on-dark` / `surface-dark` `#171717` | 17.93:1 | 4.5:1 | Pass |
| `on-dark-mute` → `#b3b3b3` / `surface-dark` | 8.55:1 | 4.5:1 | Pass |
| `hairline` `#e5e5e5` / `canvas` | 1.26:1 | 3.0:1 | **Fail — extracted, frozen, disclosed** |
| `hairline` / `surface-soft` | 1.21:1 | 3.0:1 | **Fail — extracted, frozen, disclosed** |
| `hairline-strong` `#d4d4d4` / `canvas` | 1.48:1 | 3.0:1 | **Fail — extracted, frozen, disclosed** |
| `hairline-strong` / `surface-soft` | 1.42:1 | 3.0:1 | **Fail — extracted, frozen, disclosed** |
| `hairline-control` `#8f8f8f` / `canvas` | 3.23:1 | 3.0:1 | Pass — prescribed |
| `hairline-control` / `surface-soft` | 3.10:1 | 3.0:1 | Pass — prescribed |
| `focus-ring` → `#9dc0fa` / `canvas` | 1.85:1 | 3.0:1 | **Fail — extracted, disclosed** |
| `focus-ring` → `#9dc0fa` / `surface-soft` | 1.77:1 | 3.0:1 | **Fail — extracted, disclosed** |
| `focus-ring` → `#294c86` / `surface-dark` | 2.11:1 | 3.0:1 | **Fail — extracted, disclosed** |
| `focus-ring-strong` `#3b82f6` / `canvas` | 3.68:1 | 3.0:1 | Pass — prescribed |
| `focus-ring-strong` / `surface-card` `#ffffff` | 3.68:1 | 3.0:1 | Pass — prescribed |
| `focus-ring-strong` / `surface-soft` | 3.52:1 | 3.0:1 | Pass — prescribed |
| `focus-ring-strong` / `surface-dark` `#171717` | 4.87:1 | 3.0:1 | Pass — prescribed |
| `focus-ring-strong` / `ink-deep` `#090909` | 5.41:1 | 3.0:1 | Pass — prescribed |

Note on the composite: the harness composites `focus-ring` over the canvas only, so its
`surface-dark` reading of 9.69:1 is a fiction — the ring is translucent, so on the dark
card it darkens to `#294c86` and fails there too. I measured it the way it renders and
disclosed that figure, which is why the fix is a single opaque ring rather than a
light/dark pair that would have left the real dark-surface failure unexamined.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | `opacity`; colour swaps discrete | Unchanged — already ≤ 100ms |
| Press | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity`; fill step discrete, no scale | Discrete fill step only |
| Focus | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | `opacity` on ring | No transition; ring never suppressed |
| Page / route transition | 100ms in / 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` on content column | Opacity at `{motion.duration-reduced}` |
| Modal / drawer | `{motion.duration-base}` 150ms in / 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `transform: translateX()` + scrim `opacity` | Travel removed; fade at 100ms |
| Dropdown | 100ms in / 60ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(-2px → 0)` | Travel removed; opacity at 100ms |
| Toast | 150ms in / 100ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(4px → 0)` | Travel removed; opacity at 100ms |
| List enter | 100ms per item, `{motion.stagger-step}` 20ms between, capped at 5 | `{motion.ease-enter}` | `opacity` | Stagger removed; renders at full opacity |
| List exit | `{motion.duration-instant}` 60ms | `{motion.ease-exit}` | `opacity`, no stagger | No transition |
| Loading | spinner 800ms linear loop; confirm tick `{motion.duration-slow}` 220ms | linear / `{motion.ease-standard}` | `transform: rotate()`, `opacity` | Spinner replaced by a static "Loading…" label |

Every exit is shorter than its entrance. The 800ms spinner period is the only bare value
in the section; it is a loop period, not a transition duration, and the Crisp block has no
token for one. Stated as such in the file.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py:28-31` | `text-dim` reports missing for this file although the palette documents three secondary inks by name: `mute` ("caption text … lowest-emphasis utility text"), `body` and `charcoal`. `mute` misses `^muted$` by one character, and `^body$` is claimed first by the `text` role. Per SPEC section 1 this is a harness bug, so no alias token was added — `tokens` therefore stays at 4 for a file that owns the role three times over. | Add `r"^mute$"`, `r"^mute-"`, `r"^charcoal$"`, `r"^dim$"` to `REQUIRED_COLOR_ROLES["text-dim"]`. Fair warning: doing so surfaces a real failure the harness currently cannot see — `mute` on `canvas` is 2.52:1 against a 4.5:1 bar. I have disclosed it in the file's Accessibility section ahead of that fix, so it will land already handled. |
| `theme-audit/audit.py:171-193` | The rgba composite always uses the canvas unless the token name contains `-on-<ground>`. `focus-ring` is reported at 9.69:1 against `surface-dark`, which cannot happen: a 50%-alpha ring over `#171717` renders `#294c86` at 2.11:1. A translucent ring that fails on a dark surface is scored as comfortably passing there. | For tokens matching `^focus`, composite over *each* candidate surface in the coverage loop rather than once over the canvas — the loop already iterates every surface, so the ground is in hand at that point. |
| `theme-audit/audit.py:357-358` | `focus_tokens` excludes bands named `inner|inset|halo` but has no concept of a ring **offset**, which is what WCAG 2.2 Focus Appearance actually measures a ring against. Files that state an offset and files that do not are scored identically. | Out of scope for a regex, but worth recording in SPEC section 1: the offset is currently an unverifiable prose claim, and the harness cannot tell a stated offset from a decorative one. |

### Needs approval

1. **`{colors.hairline-control}` `#8f8f8f` is an invented hex.** It is prescribed, labelled as such in the Colors section and in Known Gaps, and has no counterpart on ollama.com. Nearest in-palette passing alternative is `{colors.body}` `#737373` at 4.74:1, which needs no new token at all — I judged a 4.74:1 near-black 1px rule too heavy for a brand whose first rule is an unbroken paper-white sheet, and chose the lightest grey that clears 3:1 with margin instead. Usage note that makes the real values defensible: `{colors.hairline}` at 1.26:1 and `{colors.hairline-strong}` at 1.48:1 are compliant *as decoration* — card edges, FAQ dividers, the footer rule — because WCAG 1.4.11 applies only where a boundary is required to identify a control. Swap to `{colors.body}` if the reviewer would rather add no hex at all.
2. **`{colors.focus-ring-strong}` `#3b82f6` is prescribed.** It is the extracted ring's own `rgb(59,130,246)` with the alpha dropped, so no new hue enters a system whose stated rule is "don't add brand colors" — but the live site does not draw it. Nearest alternative that avoids blue entirely: `{colors.ink}` `#000000` as the ring with a mandatory `{colors.canvas}` offset, which is 21:1 on light surfaces but invisible on `{colors.surface-dark}` and `{colors.ink-deep}` and would then need a second ring. I chose the single blue; a monochrome-purist reviewer may prefer the black/white pair.
3. **`{colors.mute}` fails as text at 2.52:1 with no compliant size.** Nearest passing value is `#767676` (4.54:1), which is within 3 units of `{colors.body}` `#737373` and would make the token redundant. I did not change it. Usage note recorded in the file: no size allowance rescues 2.52:1, so `{colors.mute}` is defensible only inside `{component.terminal-card}`, where it renders simulated terminal comments — screenshot content, not page copy.
4. **Hover, loading and selected behaviour across 10 components is prescribed, not observed.** Marked (P) throughout the state matrix and recorded in Known Gaps. If the collection's policy is that an undocumented state must stay blank, the matrix's (P) column should be struck rather than silently kept.

### Identity verdict

Still unmistakably Ollama. The diff adds two hexes and a motion block to a 21-colour
palette and otherwise changes prose only; the paper-white canvas, the single black pill,
the pill-everything geometry, the SF Pro Rounded headline, the `curl` snippet as the
page's real CTA and the one inverted Max card are all untouched. The new material argues
*from* the brand rather than over it: the ring is the brand's own blue de-aliased, the
boundary token is the lightest grey that clears the bar rather than a safe dark one, and
the motion section's reasoning is that a developer tool should feel like a key press.

**Crisp is the right profile and I kept it.** SPEC section 5 rule 2 fires on the first
read — this is a developer-tool identity whose home page is a README, whose signature
component is a terminal mockup, and whose own description calls it "defiantly minimal".
Rule 1 cannot fire: there is no photography in the entire system. Rule 3 cannot fire
either, and it is worth saying why, since the palette does list three saturated hexes:
`terminal-red`, `terminal-yellow` and `terminal-green` are a macOS window-chrome likeness
inside a screenshot, never drawn on an interactive element, which is exactly the
"saturation *and role*" test rule 3 asks for. No entrance choreography, 150ms base and a
20ms stagger are what this file would have specified if anyone had measured it.

One identity risk I want flagged rather than buried: the `### State matrix` is the single
largest addition, and a 10×8 table is the most generic-looking thing in the document. I
kept it honest instead of full — four components carry `n/a` across most of the row with
a stated reason, which is itself a fact about this brand: a site with no validation, no
accordions and no toggles genuinely has fewer states than the matrix has columns.
