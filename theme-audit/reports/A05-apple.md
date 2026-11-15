## A05 · apple

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 3 | 5 |
| refs | 5 | 5 |
| contrast | 2 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

Harness command: `python3 -I theme-audit/audit.py --site apple --json`. All five harness-reported defects in the brief were reproduced exactly before editing; the contrast figures were independently recomputed with a WCAG 2.1 relative-luminance snippet and matched to two decimal places.

**Note on the contrast score.** `theme-audit/audit.py` was updated mid-review (commit `54410bb`, "score contrast on undisclosed failures, measure every tone"). Under the earlier harness this file scored contrast 4 after my edits, because the frozen `{colors.primary-on-dark}` pairing still counted against it. Under the current harness the same file scores 5: all three remaining failures are reported as `disclosed`. The before-score was re-measured against the *current* harness, on the pre-edit file restored from `git show HEAD:design-md/apple/DESIGN.md`, and is unchanged at 2 — so the before -> after comparison above is apples-to-apples. **No hex changed; three real AA failures remain and are stated plainly in the file.** The score moved because the failures are now disclosed, not because they were fixed.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. The only motion fact in the file was `transform: scale(0.95)`. Fixed. |
| P0 | G · Accessibility | whole file | No `## Accessibility` section. No contrast figure stated anywhere, despite the file shipping three AA failures. Fixed. |
| P0 | A · Tokens | `colors.focus*` | No focus colour of any kind. `{colors.primary-focus}` was described as "the focus ring root" but does not satisfy the `focus` role, and a single blue ring cannot serve this file: `#0071e3` on `{colors.primary}` measures 1.19:1. Fixed with three rings. |
| P0 | B · Colour | `{colors.hairline}` #e0e0e0 | 1.32:1 on `{colors.canvas}`, 1.21:1 on parchment, against a 3.0:1 boundary floor — and on `{component.store-utility-card}`, `{component.configurator-option-chip}` and `{component.search-input}` it is the *only* boundary of an interactive control. Frozen value; parallel `{colors.hairline-strong}` added and the failure stated plainly. |
| P0 | H · States | Components | Only `active` and `selected` were documented. `hover`, `focus-visible`, `pressed`, `disabled`, `loading`, `error` were absent, and the Iteration Guide actively forbade documenting hover. Fixed with a per-component state matrix. |
| P1 | A · Tokens | `surface` role | Four `surface-*` keys existed but none satisfied the `surface` role pattern, so the file had no addressable raised layer. `{colors.surface-card}` added. |
| P1 | B · Colour | `{colors.body-muted}` #cccccc | 1.61:1 on canvas. Legitimate at 9.28:1 on `{colors.surface-tile-1}`, but the file never scoped it to dark tiles, so it read as a general muted ink. Frozen; scoped in prose, parallel `{colors.muted-strong}` added (5.07:1). |
| P1 | B · Colour | `{colors.primary-on-dark}` #2997ff | White on it measures 3.02:1. Harmless as the text colour it actually is (4.94:1 on tile-1), fatal if ever built as a fill. Frozen — see Needs approval. |
| P1 | B · Colour | `{colors.ink-muted-48}` #7a7a7a | 4.29:1 on canvas, 3.94:1 on parchment — below AA at the 12px and 10px sizes it is used at for legal copy. The disabled-text use is exempt; the legal-copy use is a real failure the file did not mention. Frozen, stated, redirected to `{colors.muted-strong}`. |
| P1 | C · Elevation | canvas / surface / raised | Every light-mode layer pair is between 1.00:1 and 1.09:1 — `{colors.surface-card}` is the *same* white as `{colors.canvas}`. Light-mode elevation is 100% border-carried, and that border fails contrast. Measured table added. |
| P1 | A · Tokens | `shadow:` group | The prose stated three real `rgba(...)` elevation values with no token to reference them. `shadow:` group added and wired into the Elevation table. |
| P1 | D · Typography | `{typography.tagline}` | Prose claimed weight 700 for tagline and a "300 / 400 / 600 / 700" ladder; the token block sets tagline to 600 and defines no 700 anywhere. Prose corrected to match the tokens, in three places. |
| P2 | D · Typography | letter-spacing principle | "Every headline at 17px and up carries a tracking tighten" contradicted three tokens: `display-lg` is 0, `lead` is +0.196px, `tagline` is +0.231px. Principle rewritten to state the real pattern. |
| P2 | E · Borders | `{component.button-pearl-capsule}` | Uses a 3px border where the rest of the file uses 1px and 2px — no border-width ladder exists to place it on. Left as extracted; now described through `{shadow.soft-ring}`, which is what it actually behaves as. Not fixed as a token ladder (would be invention). |
| P2 | E · Radius | `{rounded.xs}` 5px | Ladder is 0 / 5 / 8 / 11 / 18 / 9999. The 5px step is used for "inline links styled as subtle chips (rare)" and is the only rung with no component in the file referencing it. Genuine Apple value; left alone. |
| P2 | E · Radius | `{rounded.pill}` / `{rounded.full}` | Duplicate values (9999px) under two names. Defensible — pill is a capsule, full is a circle — but it is a ladder with two identical rungs. Left alone. |
| P2 | A · Spacing | `{spacing.md}` 17px | Sits off the stated 8px base. The file explains it as the body font size reused as a rhythm constant, which is coherent; flagged only so it is not read as an error. |
| P2 | I · Identity | `## Motion & Animation` | Cinematic's 400–600ms base would make press feedback feel broken. Resolved by dropping press alone to `{motion.duration-instant}` (120ms) and stating the reason, rather than diluting the profile everywhere. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-strong: "#86868b"` | Parallel accessible boundary, 3.62:1 on canvas. Satisfies `border` at 3.0:1 without touching the frozen `hairline`. |
| frontmatter `colors:` | — -> `muted-strong: "#6e6e73"` | Parallel accessible secondary ink for light surfaces, 5.07:1. The extracted system had none. |
| frontmatter `colors:` | — -> `surface-card: "#ffffff"` | Satisfies the required `surface` role; makes the raised layer addressable. Alias of canvas, which is the honest fact. |
| frontmatter `colors:` | — -> `focus: "#0071e3"`, `focus-on-dark: "#2997ff"`, `focus-ink: "#1d1d1f"` | Satisfies the required `focus` role. Three rings because the file documents white canvas, near-black tiles and an accent-filled pill; no single hex clears 3.0:1 on all three. |
| frontmatter | — -> `shadow:` group (`none`, `hairline-ring`, `soft-ring`, `product`) | SPEC §1: the prose documented real `rgba(...)` values with no token behind them. |
| frontmatter | — -> `motion:` group, 9 keys, Cinematic values | SPEC §4/§5. 120 / 240 / 400 / 600 / 900ms, long-decelerate curves, 80ms stagger. |
| `## Colors` → Brand & Accent | Sky Link Blue described only as a dark-surface link -> plus "text colour, never a fill", with the 3.02:1 fill failure and the `{colors.focus-ink}` label fallback | The file's own Don'ts warned against using it on light surfaces but not against filling with it, which is the failing case. |
| `## Colors` → Surface | — -> Card White entry with the 1.00:1 / 1.09:1 measurements | Documents that light-mode elevation carries no luminance at all. |
| `## Colors` → Text | Body Muted "secondary copy on dark tiles" -> scoped to dark tiles only, with measured 9.28:1 / 13.08:1 pass and 1.61:1 prohibition; Muted Strong added | SPEC §2 parallel-token procedure. |
| `## Colors` → Text | Ink Muted 48 "disabled text and legal fine-print" -> plus the 4.29:1 / 3.94:1 failure and the size it occurs at | The legal-copy use fails AA; the disabled use does not. The file conflated them. |
| `## Colors` → Hairlines | Hairline described neutrally -> scoped to decoration, with the 1.32:1 failure stated plainly and Hairline Strong added | SPEC §2: frozen tone, parallel token, failure stated. |
| `## Colors` | — -> new `### Focus` subsection | Three prescribed rings with measured ratios on every surface each is drawn on. |
| `## Typography` → Principles | "Every headline at 17px and up carries a tracking tighten" -> the real pattern, naming the three positive/zero exceptions | Prose contradicted the token block. |
| `## Typography` → Principles | "Weight 700 is used sparingly for tagline"; ladder "300 / 400 / 600 / 700" -> tagline is 600, ladder is 300 / 400 / 600 | No token in the file defines 700. Corrected in the principle, the 500 note and the matching Don't. |
| `## Elevation & Depth` | 3-column table -> 4-column with a `{shadow.*}` token per level, plus `soft-ring` row | Elevation values were unreferencable. |
| `## Elevation & Depth` | — -> measured layer-separation table + verdict paragraph | Dimension C: layers are 1.00–1.09:1 on light, 1.03–1.41:1 on dark. Elevation is one consistent grammar per mode (border on light, surface-swap on dark, never mixed) but the light grammar is inaccessible. |
| `## Components` | — -> new `### Interaction States` matrix, 13 rows × 8 states | Every component now names its states, each tagged `extracted` or `prescribed`. Product tiles and the quote card declare two states only, as SPEC §7 allows. |
| after `## Components` | — -> `## Motion & Animation` | SPEC §3/§6. First line states the system is prescribed and unmeasured. 11-row table, transform/opacity only, exits shorter than entrances, one `@media (prefers-reduced-motion: reduce)` block. |
| after Motion | — -> `## Accessibility` | 17-row measured contrast table, 11-row focus-ring-per-surface table, tap-target note, reduced-motion note, and an explicit "not verifiable from this document" list. |
| `## Iteration Guide` item 4 | "Never document hover. Default and Active/Pressed states only." -> points at the Interaction States matrix, keeps hover restrained, adds 4a on completeness | The rule directly blocked SPEC §7. Left unchanged it would have re-broken the file on the next edit. |
| `## Known Gaps` | — -> 5 new entries | Labels the motion group, the three focus tokens, the two parallel colour tokens and `surface-card` as prescribed; notes that the palette contains no error colour at all. |

### Contrast checks

All values computed with a `python3 -I` WCAG 2.1 snippet, not estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #1d1d1f / `canvas` #ffffff | 16.83:1 | 4.5 | Pass |
| `ink` #1d1d1f / `canvas-parchment` #f5f5f7 | 15.46:1 | 4.5 | Pass |
| `ink` #1d1d1f / `surface-card` #ffffff | 16.83:1 | 4.5 | Pass |
| `ink` #1d1d1f / `surface-pearl` #fafafc | 16.14:1 | 4.5 | Pass |
| `ink` #1d1d1f / `surface-chip-translucent` #d2d2d7 | 11.17:1 | 4.5 | Pass |
| `on-dark` #ffffff / `surface-tile-1` #272729 | 14.91:1 | 4.5 | Pass |
| `on-dark` #ffffff / `surface-tile-2` #2a2a2c | 14.32:1 | 4.5 | Pass |
| `on-dark` #ffffff / `surface-tile-3` #252527 | 15.30:1 | 4.5 | Pass |
| `on-dark` #ffffff / `surface-black` #000000 | 21.00:1 | 4.5 | Pass |
| `body-muted` #cccccc / `surface-tile-1` #272729 | 9.28:1 | 4.5 | Pass |
| `body-muted` #cccccc / `surface-black` #000000 | 13.08:1 | 4.5 | Pass |
| `body-muted` #cccccc / `canvas` #ffffff | 1.61:1 | 4.5 | **Fail** — frozen; combination now forbidden in prose |
| `muted-strong` #6e6e73 / `canvas` #ffffff | 5.07:1 | 4.5 | Pass *(prescribed)* |
| `muted-strong` #6e6e73 / `canvas-parchment` #f5f5f7 | 4.66:1 | 4.5 | Pass *(prescribed)* |
| `muted-strong` #6e6e73 / `surface-pearl` #fafafc | 4.86:1 | 4.5 | Pass *(prescribed)* |
| `ink-muted-80` #333333 / `canvas` #ffffff | 12.63:1 | 4.5 | Pass |
| `ink-muted-80` #333333 / `canvas-parchment` #f5f5f7 | 11.60:1 | 4.5 | Pass |
| `ink-muted-48` #7a7a7a / `canvas` #ffffff | 4.29:1 | 4.5 | **Fail** — frozen; exempt in its disabled role, fails for legal copy |
| `ink-muted-48` #7a7a7a / `canvas-parchment` #f5f5f7 | 3.94:1 | 4.5 | **Fail** — frozen |
| `on-primary` #ffffff / `primary` #0066cc | 5.57:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary-focus` #0071e3 | 4.70:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary-on-dark` #2997ff | 3.02:1 | 4.5 | **Fail** — frozen; see Needs approval |
| `focus-ink` #1d1d1f / `primary-on-dark` #2997ff | 5.58:1 | 4.5 | Pass — the label colour that rescues it |
| `primary` #0066cc / `canvas` #ffffff | 5.57:1 | 4.5 | Pass |
| `primary` #0066cc / `canvas-parchment` #f5f5f7 | 5.11:1 | 4.5 | Pass |
| `primary-on-dark` #2997ff / `surface-tile-1` #272729 | 4.94:1 | 4.5 | Pass |
| `primary-on-dark` #2997ff / `surface-black` #000000 | 6.96:1 | 4.5 | Pass |
| `hairline` #e0e0e0 / `canvas` #ffffff | 1.32:1 | 3.0 | **Fail** — frozen; scoped to decoration |
| `hairline` #e0e0e0 / `canvas-parchment` #f5f5f7 | 1.21:1 | 3.0 | **Fail** — frozen |
| `divider-soft` #f0f0f0 / `canvas` #ffffff | 1.14:1 | 3.0 | **Fail** — frozen; a halo, never a boundary |
| `hairline-strong` #86868b / `canvas` #ffffff | 3.62:1 | 3.0 | Pass *(prescribed)* |
| `hairline-strong` #86868b / `canvas-parchment` #f5f5f7 | 3.33:1 | 3.0 | Pass *(prescribed)* |
| `hairline-strong` #86868b / `surface-pearl` #fafafc | 3.48:1 | 3.0 | Pass *(prescribed)* |
| `focus` #0071e3 / `canvas` #ffffff | 4.70:1 | 3.0 | Pass *(prescribed)* |
| `focus` #0071e3 / `canvas-parchment` #f5f5f7 | 4.31:1 | 3.0 | Pass *(prescribed)* |
| `focus` #0071e3 / `surface-pearl` #fafafc | 4.51:1 | 3.0 | Pass *(prescribed)* |
| `focus` #0071e3 / `primary` #0066cc | 1.19:1 | 3.0 | **Fail** — why a blue ring cannot be the only ring; `focus-ink` covers this surface |
| `focus-on-dark` #2997ff / `surface-tile-1` #272729 | 4.94:1 | 3.0 | Pass *(prescribed)* |
| `focus-on-dark` #2997ff / `surface-tile-2` #2a2a2c | 4.75:1 | 3.0 | Pass *(prescribed)* |
| `focus-on-dark` #2997ff / `surface-tile-3` #252527 | 5.07:1 | 3.0 | Pass *(prescribed)* |
| `focus-on-dark` #2997ff / `surface-black` #000000 | 6.96:1 | 3.0 | Pass *(prescribed)* |
| `focus-ink` #1d1d1f / `primary` #0066cc | 3.02:1 | 3.0 | Pass *(prescribed; tightest margin in the file)* |
| `focus-ink` #1d1d1f / `primary-focus` #0071e3 | 3.58:1 | 3.0 | Pass *(prescribed)* |
| `focus-ink` #1d1d1f / `surface-chip-translucent` #d2d2d7 | 11.17:1 | 3.0 | Pass *(prescribed)* |
| `focus-ink` #1d1d1f / `canvas` #ffffff | 16.83:1 | 3.0 | Pass *(prescribed)* |

Layer separation (no WCAG threshold; reported for dimension C): canvas→surface-card 1.00:1 · canvas→parchment 1.09:1 · parchment→pearl 1.04:1 · tile-1→tile-2 1.04:1 · tile-1→tile-3 1.03:1 · black→tile-1 1.41:1.

### Motion inventory

Profile: **Cinematic**. Every value prescribed, none measured. `{motion.duration-instant}` 120ms · `{motion.duration-fast}` 240ms · `{motion.duration-base}` 400ms · `{motion.duration-slow}` 600ms · `{motion.duration-emphasis}` 900ms · `{motion.stagger-step}` 80ms · `ease-standard` `cubic-bezier(0.28, 0, 0.12, 1)` · `ease-enter` `cubic-bezier(0.16, 1, 0.3, 1)` · `ease-exit` `cubic-bezier(0.4, 0, 0.9, 1)`.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | 240ms `{motion.duration-fast}` | `{motion.ease-standard}` | `opacity`; colour as a non-animated swap | Colour swap instant, no fade |
| Press / active | 120ms `{motion.duration-instant}` | `{motion.ease-exit}` | `transform: scale(0.95)` | Removed — scale is travel |
| Focus-visible | 120ms `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring only | Ring instant at full opacity |
| Page / route transition | 600ms in / 400ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(24px)` | `opacity` only, 120ms, no travel |
| Modal / drawer | 400ms in / 240ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` on scrim, `transform: translateY(100%)` on sheet | `opacity` only, 120ms; no slide |
| Dropdown | 240ms in / 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(-8px)` | `opacity` only, 120ms |
| Toast | 400ms in / 240ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `transform: translateY(16px)` | `opacity` only, 120ms; dismiss timer extends to 8s |
| List enter | 600ms per item, 80ms stagger, capped at 8 | `{motion.ease-enter}` | `opacity`, `transform: translateY(32px) scale(0.98)` | Full opacity immediately, no stagger, no travel |
| List exit | 240ms, no stagger | `{motion.ease-exit}` | `opacity` | Removed instantly |
| Loading | 1000ms spinner loop; 1600ms skeleton shimmer | `linear` | `transform: rotate()`; `opacity` 0.4↔1.0 | Frozen; static parchment block + `aria-live` text status |
| Signature full-bleed product reveal | 900ms image, type at 600ms one stagger later | `{motion.ease-enter}` | `transform: scale(1.04)→scale(1)`, `opacity` + `translateY(24px)` | Removed; tile renders final on first paint |

Rules held: transform/opacity only; every exit shorter than its entrance; above-fold hero renders final so nothing is delayed on first paint; no infinite animation except the two loaders; no brand ambience, which matches the file's own no-decorative-chrome posture.

### Shared issues (not fixed)

All three `audit.py` issues below were re-checked against the updated harness (`54410bb`) and still stand. The new `check_all` and component-pair checks are a clear improvement: with them, this file reports zero unresolved contrast failures and zero component `backgroundColor`/`textColor` failures.

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` lines 160–176 (`check("focus", bg, ...)` and the signal-colour loop) | The `focus` role is reduced to one representative token via `find_role_strongest(..., canvas)`, then checked against canvas, surface *and* accent. A file that correctly ships a light-surface ring, a dark-surface ring and an on-accent ring is scored on whichever is darkest against the canvas; the other two are never measured. Apple needs three rings and only `focus-ink` is tested. | Check every `focus*` key against every surface the file defines, or let the file declare which ring belongs to which surface (SPEC §1 already contemplates `focus` + `focus-on-dark`). |
| `theme-audit/audit.py` lines 170–176 (signal-colour loop) | Every key matching `^(primary\|accent\|secondary\|brand\|cta)` is treated as a *fill* and tested against `on-accent`. `{colors.primary-on-dark}` is a text colour on dark tiles; white never sits on it. The loop reports a failure that cannot occur, and the only escape hatch is the substring `disabled`. | Exempt keys whose name marks them as text-on-surface (`-on-dark`, `-on-light`, `-link`), the same way `disabled` is exempted, or let a file declare a token's role. |
| `theme-audit/audit.py` line 22 (`REQUIRED_COLOR_ROLES["surface"]`) | The `surface` pattern list enumerates adjectives (`card`, `cream`, `pearl` absent). Apple shipped `surface-pearl`, `surface-tile-1`, `surface-black`, `surface-chip-translucent` — four real surfaces — and still scored `surface: missing`. The fix across 84 files will be 84 alias tokens that exist only to match a regex. | Treat any `^surface(-\|$)` key as satisfying the role, and pick the representative by contrast against canvas as `border` and `focus` already do. |
| `theme-audit/SPEC.md` §6 | "remove all travel and scale, keep opacity fades at 150ms or less" — but no profile's token block contains a duration ≤150ms except Crisp. Cinematic's smallest SPEC-listed key is `duration-fast`. Files must either invent an extra token or reference a bare `150ms`, which breaks the "reference every value as `{motion.*}`" instruction. | Add `duration-reduced: 150ms` to the SPEC §4 key list for every profile. (Worked around here by setting `duration-instant` to 120ms, which is ≤150ms and so can carry the reduced-motion cap.) |
| `theme-audit/SPEC.md` §5 | Cinematic prescribes a 400–600ms base with no exception for press feedback, which at 400ms reads as a broken control. Apple's one extracted motion fact is a press. | State that acknowledgement states (press, focus) sit at the profile's instant/fast tier regardless of profile, and that only arrival states take the base duration. |

### Needs approval

1. **`{colors.primary-on-dark}` #2997ff — white on it measures 3.02:1, required 4.5:1.** Not changed; it is Sky Link Blue, a real brand hex. Nearest passing value, hue and saturation locked, is **#0075e4** (4.50:1 with white) — but that is self-defeating: it drops to 3.31:1 on `{colors.surface-tile-1}`, versus 4.94:1 today, so it would fail the only job the colour actually has. Usage note that makes the real value defensible: *Sky Link Blue is a text colour on dark tiles only, where it measures 4.94:1 to 6.96:1. It is never a fill. The harness pairing is hypothetical. If a Sky-Blue filled surface is ever required, its label must be `{colors.focus-ink}` #1d1d1f at 5.58:1, not white.* Under the current harness this counts as a disclosed failure, so it no longer costs score — but it is still a genuine AA failure in the brand, not a resolved one.
2. **`{colors.hairline}` #e0e0e0 at 1.32:1 on canvas, required 3.0:1.** Not changed. Nearest passing value is **#949499** (3.00:1) or, with margin, the prescribed `{colors.hairline-strong}` #86868b (3.62:1). Usage note: *the extracted hairline is decorative only — card edges, section rules, anything carrying no interactive meaning. Wherever the border is the sole edge of a control it must be `{colors.hairline-strong}`.* Approval needed because this changes the visible weight of `{component.store-utility-card}`, `{component.configurator-option-chip}` and `{component.search-input}` — a visibly heavier border on Apple's quietest surfaces is a real design change, not a token swap.
3. **`{colors.ink-muted-48}` #7a7a7a at 4.29:1 on canvas, 3.94:1 on parchment.** Not changed. Nearest passing value is **#767679** (4.50:1 on canvas, still 4.14:1 on parchment, so parchment needs #6e6e73). Usage note: *legitimate with no threshold in its disabled-text role; as live legal copy at 12px `{typography.fine-print}` and 10px `{typography.micro-legal}` it fails AA and the 3:1 large-text allowance does not apply at those sizes.* Approval needed to redirect legal copy to `{colors.muted-strong}`.
4. **`{colors.divider-soft}` #f0f0f0 at 1.14:1.** Not changed and no replacement proposed: the file itself describes it as a ring/halo (`rgba(0, 0, 0, 0.04)`), not a boundary. Flagged only so nobody promotes it to a control edge.
5. **Three prescribed focus tokens and the whole `motion:` group** are inferences, not extractions. They are labelled as such in Known Gaps and in the first line of `## Motion & Animation`, but anyone with live-site access should overwrite them with measured values rather than trust them.

### Identity verdict

Still unmistakably Apple. The file's own thesis — photography-first, UI recedes, one blue, exactly one shadow, the colour change is the divider — survives intact, and the additions mostly *sharpen* it rather than dilute it. Three things in particular read as this brand and could not be lifted from another file in the collection: the measured proof that light-mode elevation carries no luminance at all and is entirely border-carried (1.00:1 canvas-to-card) is a specifically Apple finding; the three-ring focus set exists because this brand alternates white canvases with near-black tiles and fills its pills with the accent, a combination no single ring can serve; and the `## Motion & Animation` signature row — a 900ms `scale(1.04)→scale(1)` on the full-bleed product image with the headline, tagline and CTAs arriving 80ms apart behind it — is the museum-gallery reveal the Overview describes, not a generic fade-up.

The Cinematic profile is **correct** and I kept it. SPEC §5 rule 1 fires cleanly: hardware-luxury identity, dark canvas in the signature tiles. The brand's own language — "reverent product photography", "the wall disappears and the artifact takes over", a layout where each tile occupies one viewport — is cinematic in the literal sense, and the alternatives are all wrong: Crisp would make the gallery feel like a settings panel, Playful contradicts a palette with one accent and zero gradients, and Calm understates a brand whose entire layout exists to let an image fill the screen slowly. The one adjustment I made rather than switching profiles is press feedback at 120ms, argued in the section itself: Cinematic governs *arrival*, not *acknowledgement*, and the file's single extracted motion fact is a fast `scale(0.95)` press that the profile must not override.

The two places where drift is a genuine risk: the 13×8 Interaction States matrix is the largest single block in the file now, and a matrix that size inherently reads more like a design system than like a brand document — mitigated by tagging each cell `extracted` or `prescribed`, so the reader can see at a glance how little of it Apple actually ships. And the `error` column had to invent treatments for a palette that contains **no error colour whatsoever** — no red, no amber. Rather than import a red from nowhere, error states are expressed with `{colors.hairline-strong}` borders plus `{colors.muted-strong}` message text, and Known Gaps records that the first production error colour will be the token that finally breaks Apple's single-accent rule. That is the most interesting thing this audit surfaced about the brand.
