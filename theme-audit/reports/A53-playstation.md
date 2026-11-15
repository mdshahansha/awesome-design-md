## A53 · playstation

Scores before -> after (1-5), from the harness: tokens 3 -> 4 · refs 5 -> 5 · contrast 2 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

`tokens` stops at 4 deliberately: the only role still reported missing is `text-dim`, and the palette plainly owns it under another name. See Shared issues — no alias token was added.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. Nothing in the file said anything about timing. |
| P0 | G Accessibility | whole file | No `## Accessibility` section; no contrast figure stated anywhere; the three real contrast failures were undisclosed. |
| P0 | A Token contract | `colors.focus` | No focus ring token. `text-input-focused` signalled focus with a 2px border-weight change only — not a 3:1 indicator, and nothing at all for buttons, tiles, paddles, nav or links. |
| P0 | B Colour | `ash-light` `#cccccc` on `canvas-light` | 1.61:1. This is the 1px border of the live `text-input` and `button-secondary-light`, so the real input boundary fails WCAG 1.4.11. Extracted value, not altered. |
| P1 | B Colour | `hairline-light` `#f3f3f3` on `canvas-light` | 1.11:1 against 3.0:1. Genuine same-theme pairing (both are light-mode tokens, the divider is drawn on the white band), not a cross-theme artefact. Extracted and frozen; now scoped to decoration and disclosed. |
| P1 | B Colour | `hairline-light` on `surface-soft` | 1.00:1 — identical hex. A `surface-soft` card with a hairline border has no visible edge at all. |
| P1 | B Colour | `hairline-dark` over `canvas-dark` | Composites to `#2e2e2e`, 1.55:1. The harness never flagged it (its `same_theme` guard skips a dark-theme token against the light canvas representative), but it is a real dark-mode boundary failure. Disclosed. |
| P1 | B Colour | `ash-dark` as `pagination-dot` fill | Composites to `#2e2e2e` over black, 1.55:1. Inactive carousel dots sit below 3:1; the active dot is `on-dark` at 21.00:1, so position is still conveyed. Disclosed. |
| P1 | H States | every component | Only default, active/pressed and disabled existed. hover, focus-visible, loading, selected and error were documented nowhere. |
| P2 | B Colour | `carousel-paddle` | Reported at 1.0:1. Measurement artefact, not a defect: the harness composites the `rgba(255,255,255,0.16)` scrim against the default white canvas, while the paddle only ever sits over dark key art (14.55:1 in situ). Disclosed with both figures. |
| P2 | C Elevation | Elevation & Depth table | Level 1 is a border and level 2 is a shadow, so elevation is expressed two ways. Defensible here — the file states cards have no resting shadow and lift only on press, so the two levels are different events rather than two idioms for the same one. Left as written. |
| P2 | E Radius ladder | `rounded.lg` 16px | The only value in the ladder with no documented use ("rare large container… e.g. dialog cards") and no component binds it. Inside the 4/8/pill rhythm, so not out of scale; left as written. |
| P2 | D Typography | `heading-md` | 18px/600 at line-height 1.0 is the only sub-1.25 line height in the file. Tight for a card label but it is an extracted value; not changed. |
| P2 | G Accessibility | `filter-pill`, `pagination-dot` | Documented geometry implies ~36px and 8px hit areas, below the 44px the file's own Touch Targets paragraph claims for "all interactive elements". Flagged in the new Accessibility section; real size needs a rendered page, so no claim is made either way. |

Contrast of body and brand pairs was checked across the whole palette, not just the representative accent: `primary`/`primary-pressed`/`primary-active`, `commerce`/`commerce-pressed`, `link-light`, `link-dark`, `warning`, `marathon-yellow` and the three PS Plus gold stops all pass at their stated use. No identity hex was altered.

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `focus: "#0070d1"`, `focus-on-dark: "#ffffff"` | SPEC section 1 requires a focus ring; no single value clears 3:1 on white, black and the PlayStation Blue band at once (blue-on-blue is 1.00:1), so the file gets the documented light/dark pair. The blue ring is the brand's own `#0070d1`; the white counterpart covers black surfaces, the blue band and orange fills. |
| frontmatter | — -> `motion:` group, Cinematic block verbatim | SPEC sections 4-5. Gaming-console identity, full-bleed photography, sparse weight-300 type: rule 1 fires. |
| `## Colors` → Surface | hairline entries -> same entries plus "decorative only" scoping with measured ratios, plus a prescribed control-boundary note pointing at `mute-light` | SPEC section 2: frozen tone scoped to decoration, with a passing tone taking the job that needs contrast. |
| `## Colors` | — -> new `### Focus` subsection | Documents both rings, their offset, and their measured ratio on every surface they can appear over. |
| `## Components` | "No hover states documented" note -> extracted/prescribed note plus a 14-row State matrix with an explicit ✓/◻/— legend | SPEC section 7. Prescribed cells are marked as such so no invented value reads as extracted. `badge-info` is stated as genuinely two-state; hero bands and the footer are surfaces with no states. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed and unmeasured. Ten-row interaction table, transform/opacity only, exit shorter than entrance everywhere, one stated ambience, plus the `prefers-reduced-motion` block clamped to `{motion.duration-reduced}`. |
| after Motion | — -> `## Accessibility` | 16 measured key pairs, the real failures stated plainly, per-surface focus-ring table, tap targets, reduced motion, and what is not measurable from a document. |
| `## Known Gaps` | hover-policy line -> that line plus three new lines | Labels motion, the focus ring and the control-boundary colour as prescribed rather than extracted. |

Section order is now Components → Motion & Animation → Accessibility → Do's and Don'ts → Responsive Behavior → Iteration Guide → Known Gaps. `Responsive Behavior` was already top-level and `Iteration Guide` was kept verbatim. Nothing else in the file was reflowed.

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #000000 on `canvas-light` #ffffff | 21.00:1 | 4.5:1 | Pass |
| `ink` on `surface-soft` #f3f3f3 | 18.93:1 | 4.5:1 | Pass |
| `ink` on `surface-card` #f5f7fa | 19.57:1 | 4.5:1 | Pass |
| `body-light` (composited #666666) on `canvas-light` | 5.74:1 | 4.5:1 | Pass |
| `mute-light` #6b6b6b on `canvas-light` | 5.33:1 | 4.5:1 | Pass |
| `mute-light` on `surface-soft` | 4.80:1 | 4.5:1 | Pass |
| `mute-light` on `surface-card` | 4.97:1 | 4.5:1 | Pass |
| `on-dark` #ffffff on `canvas-dark` #000000 | 21.00:1 | 4.5:1 | Pass |
| `on-dark` on `surface-dark-elevated` #121314 | 18.60:1 | 4.5:1 | Pass |
| `on-dark` on `surface-dark-card` #181818 | 17.76:1 | 4.5:1 | Pass |
| `on-dark-mute` #cccccc on `canvas-dark` | 13.08:1 | 4.5:1 | Pass |
| `body-dark` (composited #b3b3b3) on `canvas-dark` | 10.02:1 | 4.5:1 | Pass |
| `mute-dark` (composited #7e7e7e) on `canvas-dark` | 5.17:1 | 4.5:1 | Pass |
| `on-primary` #ffffff on `primary` #0070d1 | 4.95:1 | 4.5:1 | Pass |
| `on-primary` on `primary-pressed` #0064b7 | 5.99:1 | 4.5:1 | Pass |
| `on-primary` on `primary-active` #004d8d | 8.58:1 | 4.5:1 | Pass |
| `on-commerce` #ffffff on `commerce` #d53b00 | 4.71:1 | 4.5:1 | Pass |
| `on-commerce` on `commerce-pressed` #aa2f00 | 6.74:1 | 4.5:1 | Pass |
| `link-light` #0064b7 on `canvas-light` | 5.99:1 | 4.5:1 | Pass |
| `link-dark` #53b1ff on `canvas-dark` | 9.10:1 | 4.5:1 | Pass |
| `warning` #c81b3a on `canvas-light` | 5.72:1 | 4.5:1 | Pass |
| `marathon-yellow` #deff20 on `canvas-dark` | 18.43:1 | 4.5:1 | Pass |
| `ink` on `ps-plus-gold-start` #ffce21 | 14.10:1 | 4.5:1 | Pass |
| `focus` #0070d1 on `canvas-light` | 4.95:1 | 3.0:1 | Pass |
| `focus` on `surface-soft` | 4.47:1 | 3.0:1 | Pass |
| `focus` on `surface-card` | 4.62:1 | 3.0:1 | Pass |
| `focus` on `surface-filter` (composited #fbfcfd) | 4.82:1 | 3.0:1 | Pass |
| `focus` on `surface-dark-card` | 3.58:1 | 3.0:1 | Pass |
| `focus-on-dark` #ffffff on `canvas-dark` | 21.00:1 | 3.0:1 | Pass |
| `focus-on-dark` on `surface-dark-elevated` | 18.60:1 | 3.0:1 | Pass |
| `focus-on-dark` on `primary` band | 4.95:1 | 3.0:1 | Pass |
| `focus-on-dark` on `commerce` fill | 4.71:1 | 3.0:1 | Pass |
| `focus` on `primary` band | 1.00:1 | 3.0:1 | Fail — why the pair exists; the band takes `focus-on-dark` |
| `hairline-light` #f3f3f3 on `canvas-light` | 1.11:1 | 3.0:1 | **Fail — extracted, disclosed, scoped to decoration** |
| `hairline-light` on `surface-soft` | 1.00:1 | 3.0:1 | **Fail — extracted, disclosed** |
| `hairline-dark` (composited #2e2e2e) on `canvas-dark` | 1.55:1 | 3.0:1 | **Fail — extracted, disclosed** |
| `ash-light` #cccccc on `canvas-light` | 1.61:1 | 3.0:1 | **Fail — extracted input border, disclosed** |
| `ash-dark` (composited #2e2e2e) on `canvas-dark` | 1.55:1 | 3.0:1 | **Fail — extracted dot fill, disclosed** |
| `carousel-paddle` icon #ffffff on its scrim over `canvas-dark` (#292929) | 14.55:1 | 4.5:1 | Pass in situ (harness reports 1.0:1 against the white canvas) |

Elevation layers: `canvas-light`→`surface-soft` 1.11:1, `canvas-light`→`surface-card` 1.07:1, `canvas-dark`→`surface-dark-elevated` 1.13:1, `surface-dark-elevated`→`surface-dark-card` 1.05:1. The layers are barely distinguishable by luminance alone — which matches what the file already says: depth comes from full-bleed band changes and imagery, not from stacked panels. Not a defect to fix, but it is the reason a card on `surface-soft` needs the stronger boundary rather than a tint difference.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity`; `scale()` on game-tile art only | Opacity at `{motion.duration-reduced}`; scale removed |
| Press | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `transform: scale(0.98)`, `opacity` | Scale removed; opacity at 150ms |
| Focus ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring | Appears instantly, no fade |
| Page / band transition | `{motion.duration-emphasis}` 900ms in, `{motion.duration-slow}` 600ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(16px)` copy, `scale(1.04→1)` hero image | Opacity cross-fade at 150ms; no travel, no scale |
| Modal / drawer | `{motion.duration-base}` 400ms in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `translateX`, scrim `opacity` | Fade at 150ms; no slide |
| Dropdown | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(-4px→0)` | Opacity at 150ms |
| Toast / Action Required banner | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(8px→0)` | Opacity at 150ms |
| List enter | `{motion.duration-slow}` per item, `{motion.stagger-step}` 80ms between | `{motion.ease-enter}` | `opacity`, `translateY(24px→0)` | Stagger and travel removed; one fade at 150ms |
| List exit | `{motion.duration-fast}`, no stagger | `{motion.ease-exit}` | `opacity`, `scale(0.98)` | Opacity at 150ms |
| Loading | `{motion.duration-emphasis}` loop | `{motion.ease-standard}` | `opacity` pulse on skeleton; `rotate()` on spinner | Loop frozen to a static fill; spinner replaced by static text |

Exit is shorter than its entrance in every row. Only `transform` and `opacity` appear. The single looping animation is the loader; the one piece of ambience (the hero-image settle) is labelled as ambience and frozen under reduced motion.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line 28-31 (`REQUIRED_COLOR_ROLES["text-dim"]`) | **Harness bug.** `text-dim` is reported missing although the palette plainly carries it five times over: `mute-light` #6b6b6b (5.33:1 on canvas, documented as "metadata text and footer link captions"), `mute-dark`, `body-light`, `body-dark`, `on-dark-mute`. The pattern list has `^muted$`/`^muted-` but not `^mute-`, and `^on-dark-soft$` but not `^on-dark-mute$`. Per SPEC section 1 no alias was invented, so this file scores 4 on tokens for a token it owns. | Add `r"^mute$"`, `r"^mute-"` and `r"^on-dark-mute$"` to the `text-dim` pattern list. Likely affects other files using "mute" rather than "muted". |
| `theme-audit/audit.py` line 170-191 (rgba compositing) and line ~442 (`deref`) | A translucent fill is composited over the *canvas* unless its key spells `-on-<ground>`, and a component whose `backgroundColor` is an inline `rgba(...)` literal derefs to `None` and then falls back to the canvas. Both make `carousel-paddle` read as white-on-white at 1.0:1 when it only ever renders over dark key art (14.55:1). `canvas-dark` also cannot be reached by the `-on-dark` naming hook, since the lookup is `^dark` and the token is `canvas-dark`. | Composite an inline `rgba()` `backgroundColor` over the ground, and let the `-on-<ground>` hook match `canvas-<ground>` as well as `^<ground>`. |
| `theme-audit/audit.py` line ~299 (`check_all` via `same_theme`) | A dark-theme boundary is never measured, because `check_all("border", "canvas")` compares against the light canvas representative and `same_theme` then drops every `*-dark` token. `hairline-dark` at 1.55:1 over `canvas-dark` was invisible to the harness; I found it by hand. | In a dual-theme file, run the boundary and text checks a second time against the opposite-polarity canvas, pairing same-theme tokens. |
| `theme-audit/audit.py` line ~386 (`ACCENTISH`) | `commerce` is a signal fill in exactly the sense the comment describes, but the pattern list does not include it, so the ring is charged for covering `#d53b00`. Harmless here (the white ring clears it at 4.71:1), but it will force a second ring on any brand whose CTA fill is named for commerce. | Add `commerce|shop|store|buy` to `ACCENTISH`. |

### Needs approval

1. **`ash-light` #cccccc as the live input and secondary-button border — 1.61:1 against 3.0:1.** Nearest passing value on `canvas-light` is `#949494` (3.00:1); the safe choice is the file's own `mute-light` #6b6b6b at 5.33:1, which is what the document now prescribes while leaving `ash-light` extracted and untouched. Approval needed to say that PlayStation's real input boundary fails WCAG 1.4.11. Usage note that would make the real value defensible: `ash-light` is acceptable only as a decorative rule and as disabled-state ink, where WCAG sets no requirement.
2. **`hairline-light` #f3f3f3 — 1.11:1 on `canvas-light`, 1.00:1 on `surface-soft`.** Nearest passing value is `#949494` (3.00:1 on white). Not changed; scoped to decoration. Usage note: a 1px divider between stacked text rows is a decorative separator, not a meaningful boundary under 1.4.11, provided the rows are also separated by the 16px padding the file documents. That argument does not extend to the card border, where there is nothing else carrying the edge.
3. **`hairline-dark` and `ash-dark` — both composite to #2e2e2e at 1.55:1 over `canvas-dark`.** Nearest passing value over black is `#5e5e5e` (3.04:1). Not changed. `ash-dark` is the inactive `pagination-dot` fill; the usage note is that the active dot carries the state at 21.00:1, so the control is not state-ambiguous even though the inactive dots are below 3:1.
4. **Two focus rings rather than one.** No single value clears 3:1 on `#ffffff`, `#000000` and `#0070d1` simultaneously — a white canvas caps the ring's luminance at L≤0.30 while the blue band needs a much higher or much lower one. The pair is `focus` #0070d1 and `focus-on-dark` #ffffff, both prescribed. Approval needed on using the brand blue itself as the ring, which means a focused blue CTA shows a white ring instead.
5. **`filter-pill` tap target.** The documented `8px 16px` padding on 14px type yields roughly 36px, which contradicts the file's own "all interactive elements meet WCAG AAA (≥ 44×44px)" claim. The Accessibility section now flags it as at-risk rather than silently correcting either statement; real size needs a rendered page.

### Identity verdict

Cinematic is right and I kept it. SPEC section 5 rule 1 fires on the first clause — gaming-console identity — and the file's own evidence supports it rather than just the category: full-bleed chapter bands, imagery at 60-90% of each section, weight-300 display type at 54px, and a "scrolls past the viewer like a console launch trailer" description. The 900ms emphasis and 80ms stagger land on the band transitions and the game-tile rail, which is exactly where this site's motion would live.

The file still reads as PlayStation. The additions reuse its own vocabulary rather than importing a generic one: the ring is `#0070d1`, the prescribed boundary is the palette's existing `#6b6b6b` instead of a new grey, the loading states use `surface-dark-card` skeletons, and the motion table names this site's real furniture — the band chapters, the mobile drawer, the game-tile rail, the PS5 games filter strip, the Action Required banner. No token was added that only exists to satisfy a regex: two focus tokens, one motion group, nothing else. The State matrix is the heaviest addition and the one place where drift is a risk — it is a 14-row table where the rest of the file is prose — but every cell is either an extracted fact or marked `◻` prescribed, and the hover column stays deliberately thin (opacity shifts, one 1.02 scale) because a brand that documents no hover states should not suddenly acquire an elaborate hover language.
