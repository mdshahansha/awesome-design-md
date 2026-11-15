## A58 · resend

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 3 | 4 |
| refs | 5 | 5 |
| contrast | 1 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

`tokens` is capped at 4 by a harness pattern gap, not by a missing token — see Shared issues. The role `on-accent` is present in the palette as `primary-on: "#000000"`, documented in the Colors section as "label colour on top of `{colors.primary}` surfaces", and bound by `button-primary` / `button-primary-pressed` as `textColor`. No alias was added to satisfy the regex.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F motion | whole file | No `motion:` group, no `## Motion & Animation` section, no `prefers-reduced-motion` rule. Nothing in the file said how any state change is timed. |
| P0 | G accessibility | whole file | No `## Accessibility` section. Four real non-text contrast failures (1.1:1 – 1.42:1 against a 3:1 threshold) were present and undisclosed. |
| P0 | A/E focus ring | `focus` role | No focus token anywhere, and `text-input` explicitly said "no separate ring colour". The file documented a white `#ffffff` email-inset surface as well as a `#000000` canvas, so one ring could not have served both even if it had existed. |
| P0 | B colour | `{colors.hairline-strong}` on `{colors.surface-card}` | 1.42:1. This is the *only* boundary of `{component.text-input}` on the real site — a live WCAG 1.4.11 failure on a form control, with no accessible alternative token in the palette. |
| P1 | H states | 13 of 15 component entries | Only `active` and `pressed` were documented. `hover`, `focus-visible`, `disabled`, `loading`, `selected`, `error` appeared nowhere in a structured line in `## Components`. |
| P1 | A token contract | `email-mockup` | Prose says the inset is sometimes rendered as `#ffffff` with `{colors.on-light}` ink, but the pair was never declared in `components:`, so the system's only light-on-dark surface was unmeasurable. |
| P1 | C elevation | canvas / surface-card / surface-elevated / surface-deep | The four layers separate by 1.06:1, 1.10:1, 1.04:1 and 1.04:1. The file's claim that `surface-card` is "just lighter than canvas to register a step up in elevation" is arithmetically near-invisible; what actually distinguishes the layers is the hairline border — which itself fails 3:1. Elevation is expressed consistently (border + luminance, never shadow), so this is a strength of the system's *consistency* and a weakness of its *legibility*. |
| P1 | B colour | `{colors.stone}` | 2.35:1 on `{colors.canvas}`. Documented as "disabled foreground", so WCAG-exempt, but nothing in the file said it must never carry live text. |
| P1 | harness/brief | brief line 12 | The brief's pre-measurement lists `border` and `text-dim` as missing roles. The harness resolves `border=hairline-strong` and `text-dim=mute`. Stale brief data, confirmed by running the harness before any edit. |
| P2 | harness | `divider-soft` | Escapes the `border` role (patterns include `^divider$` but not `^divider-`), so its 1.06:1 on canvas was never measured by the harness. Disclosed in the file anyway. |
| P2 | harness | `on-light-mute` | Composited over `{colors.canvas}` rather than over the white ground its name declares, because the `-on-<ground>` resolver looks for a key matching `^light($|[-_])` and the file names it `surface-light`. Produces no false failure today. |
| P2 | D typography | `{typography.caption-emph}` | Helvetica 14/600 sits outside the file's own stated four-family stack (Domaine Display / ABC Favorit / Inter / Geist Mono) and the "never bump body weight to 600" rule in Don'ts. Reads as an extraction artefact; left as extracted. |
| P2 | D typography | `{typography.display-lg}` | `letterSpacing: -2.8px` at 56px is -5%, against -1% on `display-xxl` and `display-xl`. One value sitting outside its own ladder. Left as extracted — it is a measured fact, not a mistake to correct. |
| P2 | G accessibility | Responsive Behavior | "WCAG AAA met on mobile" is stated without qualification; desktop controls at 36px meet 2.5.8 (AA, 24×24px) but not 2.5.5 (AAA, 44×44px). Scoped in the new Accessibility section rather than rewritten in place. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-control: "rgba(255,255,255,0.36)"` | SPEC §2 parallel accessible token. The frozen `hairline-strong` (1.42:1) is the sole boundary of `text-input`; 0.36 alpha is the lowest that clears 3:1 on all four dark grounds. Named inside the brand's existing "hairline" vocabulary, not as a generic `border-*`. |
| frontmatter `colors:` | — -> `focus: "#3b9eff"`, `focus-on-light: "#0075ff"` | SPEC §1: the focus role is the one exception where binding an existing hex is a real role binding. `#3b9eff` is the palette's `accent-blue` / `link`; `#0075ff` is the opaque base of `accent-blue-glow`. Two rings because the file documents both a `#000000` canvas and a white/`surface-light` inset, where the first ring drops to 2.59:1. No new hex entered the palette. |
| frontmatter | — -> `motion:` group | The **Crisp** block from SPEC §4, verbatim, no deviation. |
| frontmatter `components:` | — -> `email-mockup-light` (`#ffffff` ground, `{colors.on-light}` ink) | SPEC §1: a ground stated in prose but never bound to a label is invisible to the harness. Now measurable at 21.0:1. |
| `## Colors` | — -> `hairline-control` bullet + new `### Focus` subsection | States the measured ratios, labels all three tokens as prescribed, and names which existing tone each ring reuses so none is mistaken for a new brand colour. |
| `## Components` | 15 entries -> same 15 entries, each with a `**States**` line | SPEC §7. `hero-stripe`, `email-mockup` and `status-dot` say plainly that they have one or two states and why. |
| `## Components` → `text-input` | "Focus state thickens the border to `{colors.ink}` (no separate ring colour)." -> same fact, labelled "as extracted", plus the prescribed ring | Keeps the extracted behaviour as a fact and adds the ring as prescribed, rather than overwriting what the site does. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's visual identity and was not measured from the live site. Principles, a 10-row interaction table, and a `@media (prefers-reduced-motion: reduce)` block naming what is removed and what remains. |
| after Motion | — -> `## Accessibility` | Measured pairs, a separate disclosed-failure table, per-surface focus-ring ratios, tap targets labelled as specified-not-observed, and an explicit list of what a document cannot assess. |

Section order after the edits matches SPEC §3 exactly: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Motion & Animation, Accessibility, Do's and Don'ts, Responsive Behavior, Iteration Guide, Known Gaps. No section was moved, reflowed or renamed.

### Contrast checks

All computed with WCAG 2.1 relative luminance; translucent tokens flattened over the ground they are drawn on.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#fcfdff` / `canvas` `#000000` | 20.63:1 | 4.5:1 | Pass |
| `ink` / `surface-card` `#0a0a0c` | 19.44:1 | 4.5:1 | Pass |
| `ink` / `surface-elevated` `#101012` | 18.67:1 | 4.5:1 | Pass |
| `ink` / `surface-deep` `#06060a` | 19.87:1 | 4.5:1 | Pass |
| `body` → `#d9dadb` / `canvas` | 15.0:1 | 4.5:1 | Pass |
| `charcoal` → `#b0b1b2` / `canvas` | 9.78:1 | 4.5:1 | Pass |
| `mute` `#a1a4a5` / `canvas` | 8.37:1 | 4.5:1 | Pass |
| `mute` / `surface-card` | 7.88:1 | 4.5:1 | Pass |
| `ash` `#888e90` / `canvas` | 6.32:1 | 4.5:1 | Pass |
| `ash` / `surface-elevated` | 5.72:1 | 4.5:1 | Pass |
| `stone` `#464a4d` / `canvas` | 2.35:1 | n/a (disabled) | Exempt |
| `primary-on` `#000000` / `primary` `#fcfdff` | 20.63:1 | 4.5:1 | Pass |
| `on-light` `#000000` / `#ffffff` inset | 21.0:1 | 4.5:1 | Pass |
| `on-light` / `surface-light` `#f1f7fe` | 19.48:1 | 4.5:1 | Pass |
| `on-light-mute` → `#4d4d70` / `#ffffff` | 8.04:1 | 4.5:1 | Pass |
| `link` / `accent-blue` `#3b9eff` / `canvas` | 7.52:1 | 4.5:1 | Pass |
| `accent-red` `#ff2047` / `canvas` | 5.55:1 | 4.5:1 | Pass |
| `accent-orange` `#ff801f` / `canvas` | 8.36:1 | 4.5:1 | Pass |
| `accent-green` `#11ff99` / `canvas` | 15.79:1 | 4.5:1 | Pass |
| `accent-yellow` `#ffc53d` / `canvas` | 13.31:1 | 4.5:1 | Pass |
| `hairline` → `#0f0f0f` / `canvas` | 1.1:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `hairline` → `#19191b` / `surface-card` | 1.13:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `hairline-strong` → `#242424` / `canvas` | 1.35:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `hairline-strong` → `#2c2c2e` / `surface-card` | 1.42:1 | 3.0:1 | **Fail** — extracted, disclosed |
| `divider-soft` → `#0a0a0a` / `canvas` | 1.06:1 | 3.0:1 | **Fail** — extracted, disclosed (harness never measures it; see Shared issues) |
| `hairline-control` → `#5c5c5c` / `canvas` | 3.14:1 | 3.0:1 | Pass (prescribed) |
| `hairline-control` → `#626263` / `surface-card` | 3.25:1 | 3.0:1 | Pass (prescribed) |
| `hairline-control` → `#666667` / `surface-elevated` | 3.31:1 | 3.0:1 | Pass (prescribed) |
| `hairline-control` → `#606062` / `surface-deep` | 3.22:1 | 3.0:1 | Pass (prescribed) |
| `focus` `#3b9eff` / `canvas` | 7.52:1 | 3.0:1 | Pass |
| `focus` / `surface-card` | 7.08:1 | 3.0:1 | Pass |
| `focus` / `surface-elevated` | 6.81:1 | 3.0:1 | Pass |
| `focus` / `surface-deep` | 7.24:1 | 3.0:1 | Pass |
| `focus` / `surface-light` `#f1f7fe` | 2.59:1 | 3.0:1 | Fail — the reason the second ring exists |
| `focus-on-light` `#0075ff` / `surface-light` | 3.9:1 | 3.0:1 | Pass |
| `focus-on-light` / `#ffffff` inset | 4.21:1 | 3.0:1 | Pass |
| Layer separation: `canvas` vs `surface-card` | 1.06:1 | — | Layers are not distinguishable by luminance alone |
| Layer separation: `canvas` vs `surface-elevated` | 1.10:1 | — | as above |
| Layer separation: `surface-card` vs `surface-elevated` | 1.04:1 | — | as above |
| Layer separation: `canvas` vs `surface-deep` | 1.04:1 | — | as above |

### Motion inventory

Prescribed, not extracted. **Crisp** profile, values verbatim from SPEC §4.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `duration-fast` 100ms | `ease-standard` | `opacity`; colour / border-colour step | Kept, clamped to `duration-reduced` 100ms; no travel |
| Press / active | `duration-instant` 60ms | `ease-standard` | `opacity` 1 → 0.92; no scale pop | Unchanged — already opacity-only and ≤100ms |
| Focus | 0ms, same frame | none | `opacity` 0 → 1 on the ring | Identical; a ring never animates |
| Page / route transition | enter 150ms (`duration-base`), exit 100ms (`duration-fast`) | `ease-enter` / `ease-exit` | `opacity` + `translateY(4px → 0)` | Travel removed; cross-fade at `duration-reduced` |
| Modal / drawer | enter 150ms, exit 100ms | `ease-enter` / `ease-exit` | `opacity` + `scale(0.98 → 1)` (modal) or `translateX(100% → 0)` (drawer); backdrop `opacity` | Scale and translate removed; both fade at `duration-reduced` |
| Dropdown / popover | enter 100ms, exit 60ms (`duration-instant`) | `ease-enter` / `ease-exit` | `opacity` + `translateY(-4px → 0)` | Travel removed; opacity at `duration-reduced` |
| Toast | enter 150ms, exit 100ms | `ease-enter` / `ease-exit` | `opacity` + `translateY(8px → 0)` | Travel removed; opacity at `duration-reduced`; dismiss timer unchanged |
| List enter | 100ms per item, `stagger-step` 20ms, capped at 6 | `ease-enter` | `opacity` + `translateY(4px → 0)` | Stagger and travel removed; one fade at `duration-reduced` |
| List exit | 60ms, no stagger | `ease-exit` | `opacity` 1 → 0 | Kept, clamped to `duration-reduced` |
| Loading | spinner 800ms/rotation infinite; skeleton shimmer 1200ms infinite | linear | spinner `transform: rotate()`; skeleton `opacity` oscillation | Spinner freezes to a static indeterminate bar; shimmer removed to a flat `hairline-strong` block; progress announced via `aria-busy` / `aria-live` |

Every exit is shorter than its matching entrance. Only `transform` and `opacity` are animated; the one stated deviation is that colour and border-colour steps share the same duration token, and neither triggers layout. The atmospheric glows are declared static — explicitly not brand ambience — so there is no infinite animation outside the two loaders. Spinner and shimmer durations sit outside the token ladder on purpose, stated in the table: a loader has no entrance to shape.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` | `REQUIRED_COLOR_ROLES["on-accent"]` (line 37-38) only matches the `on-<role>` word order. resend documents `primary-on: "#000000"` as the label colour on `{colors.primary}` and binds it as `textColor` on `button-primary`, so the role is plainly present under another name, yet reports missing and caps `tokens` at 4. Per SPEC §1 this is a harness bug, not a token to invent. | Add `r"^primary-on$"`, `r"^accent-on$"`, `r"^brand-on$"` to the `on-accent` pattern list. |
| `theme-audit/audit.py` | `REQUIRED_COLOR_ROLES["border"]` (line 32-33) matches `^divider$` but not `^divider-`, so `divider-soft` at 1.06:1 on canvas is never measured anywhere in the repo. | Add `r"^divider-"`. |
| `theme-audit/audit.py` | The `-on-<ground>` ground resolver (around line 190) matches `^{ground}($|[-_])`, so `on-light-mute` cannot find `surface-light` and is flattened over the canvas instead of over the light ground its own name declares. Harmless here (the token matches no checked role) but it would manufacture or hide failures elsewhere. | Also try `^surface-{ground}$` and `^{ground}$` as a suffix match before falling back to the canvas. |
| `theme-audit/briefs/A58-resend.md` | Line 12 lists `border` and `text-dim` among the missing colour roles; the current harness resolves `border=hairline-strong` and `text-dim=mute`. Verified by running `audit.py` before making any edit. | Regenerate the briefs from current `audit.py` output. |

### Needs approval

1. **Re-binding the control boundaries.** `{component.text-input}`, `{component.button-outline}`, `{component.button-ghost}`, `{component.feature-card-bordered}`, `{component.pricing-tier}` and `{component.code-window}` are all documented in prose as carrying a 1px `{colors.hairline-strong}` border, measured at 1.35:1 on canvas and 1.42:1 on `surface-card` against a 3:1 requirement. Those bindings have been left exactly as extracted, because they describe the product that actually ships. Pointing at least `text-input`, `button-outline` and `button-ghost` at `{colors.hairline-control}` is the fix, and it is a brand-owner decision because it visibly brightens the UI — the whole system is built on 6–14% white edges and 36% will read as a different brand.
2. **The two prescribed focus rings.** `{colors.focus}` `#3b9eff` and `{colors.focus-on-light}` `#0075ff`. Resend ships no ring of its own; both reuse hexes the palette already owns, but the brand's stated rule is "don't introduce a secondary brand accent", and a blue ring is visible chrome. Approval needed on the hexes, the 2px/2px-offset geometry, and the dark/light switch rule.
3. **`{colors.hairline-control}` `rgba(255,255,255,0.36)`.** A new tone in a palette whose identity is partly *how faint its edges are*. Nearest passing values for the frozen tones, if the brand would rather raise them in place than add a parallel token: `hairline` and `hairline-strong` would both need to reach `rgba(255,255,255,0.36)` to clear 3:1 on `{colors.canvas}` — i.e. 6× and 2.6× their extracted alpha. That is not a tweak, it is a different visual system, which is why the parallel token is the recommendation.
4. **Usage note that would make the frozen values defensible.** `{colors.hairline}` and `{colors.divider-soft}` are defensible as-is if scoped in writing to purely decorative separation — row rules, footer column dividers, nav underline — where WCAG 1.4.11 does not apply because no state or boundary of a control depends on seeing them. That scoping is now written into the file. `{colors.hairline-strong}` on `{component.text-input}` is **not** defensible on that argument: it is the only thing delimiting a form control, and 1.4.11 applies. Needs an owner decision, not a usage note.
5. **The AAA tap-target claim.** "WCAG AAA met on mobile" in Responsive Behavior was left in place and scoped in the Accessibility section rather than edited. If the brand wants the claim removed from Responsive Behavior itself, that is a one-line change outside what this audit altered.

### Identity verdict

Still unmistakably Resend. The file's signature is intact: a true-`#000000` canvas, 96px Domaine Display with `ss01 / ss04 / ss11`, a white CTA as the single brightest pixel, six accent colours that only ever appear as low-opacity atmospheric washes, and depth built from translucent-white hairlines with no shadow language at all. Nothing added is generic: the three new tokens are the palette's own `accent-blue`, the opaque base of its own `accent-blue-glow`, and one translucent white in the file's own `hairline-*` series. The Motion section's own argument — "a terminal, not a showreel", static glows that must never breathe, no entrance choreography — is specific to this brand and could not be lifted into another file in the collection unchanged.

**Crisp is the right profile and I kept it.** SPEC §5 rule 2 fires first and cleanly: Resend is a developer-tool identity — an email API, documented around code windows, traffic-light shells, Geist Mono and `{component.code-window}` as a recurring page unit. There is a real pull toward Calm, and it deserves stating: the display face is an editorial serif at weight 400, the file describes itself in print-magazine terms, and the whole system is opacity-led with almost no travel, which is Calm's signature. But Calm is rule 4, the terminal answer, and rule 2 is above it. The deciding evidence inside the file is that the editorial register lives entirely in *static* typography while every interactive surface — buttons at 36px, code tabs, nav pills, form inputs — is small, dense and tool-like. Crisp's 150ms base and 20ms stagger serve those; a 250ms Calm base would make a developer console feel sluggish without making the serif any more editorial.

One honest tension worth recording for whoever reads across the collection: the brand's elevation story and its accessibility story are in direct conflict. Resend's layers separate by 1.04:1 to 1.10:1 and its boundaries by 1.1:1 to 1.42:1 — the atmosphere *is* the near-invisibility. Every accessible value added here works against that, which is exactly why all three sit under Needs approval rather than silently replacing what was extracted.
