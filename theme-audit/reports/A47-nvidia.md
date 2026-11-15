## A47 · nvidia

Scores before -> after (1-5), from the harness: tokens 3 -> 4 · refs 5 -> 5 · contrast 1 -> 5 · sections 3 -> 5 · motion 1 -> 5 · states 1 -> 5

`tokens` stays at 4 deliberately. The only unsatisfied role is `text-dim`, and this file plainly owns that role under three names (`mute`, `stone`, `ash`, plus `on-dark-mute`). Per SPEC section 1 that is a harness pattern gap, reported under Shared issues, not a token to invent — adding a `text-dim` alias would have scored 5 and made the document worse.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A/E Token contract | `colors.focus` | No focus role at all. The file's own prose called the 2px `{colors.primary}` border on `{component.text-input-focused}` "the only focus signal in the system", and that border measures 2.41:1 against `{colors.canvas}` — below the 3.0:1 a focus indicator needs. Keyboard users had no visible focus anywhere in the system. |
| P0 | B Colour | `{colors.hairline}` `#cccccc` on `{colors.canvas}` | 1.61:1 against the required 3.0:1, undisclosed. This is the boundary of every card, every table cell and both inputs — and because `{colors.surface-soft}` separates from `{colors.canvas}` at only 1.07:1, the hairline is the *only* thing making those surfaces visible. |
| P0 | B Colour | `{component.button-ghost-link}` | `{colors.primary}` label on `{colors.canvas}` at 2.41:1 against 4.5:1, undisclosed. This is the "Learn More →" affordance at the bottom of every card — the system's most repeated text link. It also fails the 3.0:1 large-text threshold. |
| P0 | C/F Sections | document | `## Motion & Animation` absent; no `motion:` group, no duration, no easing, no reduced-motion rule anywhere in 640 lines. |
| P0 | G Sections | document | `## Accessibility` absent. Seven real AA failures in the palette were undocumented, so anyone building on the file would ship them unknowingly. |
| P1 | H States | every component entry | `hover`, `focus-visible`, `loading`, `selected` and `error` named nowhere in Components. The lead note ("No hover states documented per system policy") recorded the gap but left the document unbuildable. |
| P1 | B Colour | `{colors.warning}` 3.5:1, `{colors.warning-bright}` 2.41:1 on `{colors.canvas}` | Both documented as text tones for callouts and banners, both below 4.5:1, undisclosed. `warning-bright` is the inverse tone and passes on `{colors.surface-dark}` at 8.72:1; nothing in the file said not to use it on white. |
| P1 | B Colour | `{colors.stone}` 3.5:1, `{colors.ash}` 2.41:1 on `{colors.canvas}` | Not flagged by the harness (no role pattern matches either name — same gap as `text-dim`), but real. `stone` is documented as "least-emphasis text *and* disabled state"; the text half fails. |
| P1 | A Token contract | `shadow:` group | The Elevation table documented a real extracted value, `0 0 5px 0 rgba(0,0,0,0.3)`, with no token to reference it — exactly the case SPEC section 1 says requires a `shadow:` group. |
| P2 | E Shapes | Do's and Don'ts | "Use `{rounded.sm}` (2px) on every interactive element. Never go to 0, never go past 4." contradicts the frontmatter: `{component.button-ghost-link}` is interactive and carries `{rounded.none}` (0px), as do `{component.primary-nav}` and `{component.sub-nav-strip}`. Not fixed — the conflict is between two extracted facts and resolving it needs a call on what the brand actually intends. |
| P2 | A Token contract | `colors.blue-700` | Exact duplicate of `colors.link-blue` (`#0046a4`) and referenced nowhere in the prose. An orphan alias. Not removed: it is an extracted token and deleting it is outside this audit's remit. |
| P2 | D Typography | `{typography.heading-lg}` | Weight 400 / line-height 1.75 sits outside the file's own "flat 1.25–1.5, weight 700" ladder. The prose accounts for it (a long-form intro paragraph that doubles as a heading), so it is an intentional extracted exception, not a stray value. No change. |
| P2 | I Identity | prose correction carried in before the review | The `{rounded.lg}` -> `{rounded.sm}` fix in the Don't list is semantically correct. The sentence now reads "no radius above `{rounded.sm}` (2px) anywhere except avatars and social icons", which matches the Shapes table exactly: the ladder stops at `sm` (2px) and the only exception is `{rounded.full}` for avatar circles and social-icon dots. Verified, no change needed. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| Frontmatter `colors:` | — -> `focus: "#5a8d00"` | Fills the one genuinely absent role. One mid-luminance ring rather than a light/dark pair, because this file runs white, `#f7f7f7`, black and `#1a1a1a` grounds inside a single page; `#5a8d00` clears 3:1 against all four. It is the brand's own pressed green, so the ring does not break the one-accent rule. Labelled prescribed. |
| Frontmatter | — -> `shadow:` group with `sticky: "0 0 5px 0 rgba(0,0,0,0.3)"` | Extracted value lifted from the Elevation table prose into a referenceable token, per SPEC section 1. |
| Frontmatter | — -> `motion:` group | Cinematic profile block from SPEC section 5, verbatim, no deviation. |
| `## Colors` | — -> new `### Focus` subsection | Documents the ring, its four measured ratios, the 2px outside offset, the two-tone variant over hero photography, and that it is prescribed. |
| `## Elevation & Depth`, level 3 row | raw `0 0 5px 0 rgba(...)` -> `{shadow.sticky}` plus the literal value | Reference integrity. |
| `## Components` lead note | appended one sentence pointing at the new states table | So the "no hover states" policy note and the prescribed states do not read as contradicting each other. |
| `## Components` | — -> new `### Component States` table | 13 rows × 8 states, each cell marked extracted / prescribed / n/a. `{component.badge-tag}` and `{component.corner-square}` are stated as genuinely one- and two-state components rather than padded out. |
| after `## Components` | — -> `## Motion & Animation` | First line states the system is prescribed to match the brand's identity and was not measured from the live site. 11-row interaction table, all values as `{motion.*}` tokens, `transform` and `opacity` only, every exit shorter than its entrance, plus a `@media (prefers-reduced-motion: reduce)` block naming what is removed, frozen and kept. |
| after that | — -> `## Accessibility` | 14 passing pairs measured, 7 failures stated plainly with their ratios, focus-ring visibility on each of the five grounds, documented tap-target heights with the 40px shortfalls named, and reduced motion. |
| `## Known Gaps` | — -> 3 bullets | Marks the prescribed motion, prescribed focus ring and prescribed states so a later reader cannot mistake them for extracted facts. |

Section order after the edits matches SPEC section 3 exactly: Components -> Motion & Animation -> Accessibility -> Do's and Don'ts -> Responsive Behavior -> Iteration Guide -> Known Gaps. `## Responsive Behavior` was already top-level, so nothing was moved. Nothing outside these insertions was reflowed.

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #000000 / `canvas` #ffffff | 21.0:1 | 4.5 | Pass |
| `body` #1a1a1a / `canvas` | 17.4:1 | 4.5 | Pass |
| `ink` / `surface-soft` #f7f7f7 | 19.6:1 | 4.5 | Pass |
| `on-dark` #ffffff / `surface-dark` #000000 | 21.0:1 | 4.5 | Pass |
| `on-dark-mute` (composited #b3b3b3) / `surface-dark` | 10.02:1 | 4.5 | Pass |
| `on-primary` #000000 / `primary` #76b900 | 8.71:1 | 4.5 | Pass |
| `mute` #757575 / `canvas` | 4.61:1 | 4.5 | Pass |
| `link-blue` #0046a4 / `canvas` | 8.71:1 | 4.5 | Pass |
| `hairline-strong` #5e5e5e / `canvas` | 6.48:1 | 3.0 | Pass |
| `hairline-strong` / `surface-dark` | 3.24:1 | 3.0 | Pass |
| `focus` #5a8d00 / `canvas` | 4.0:1 | 3.0 | Pass |
| `focus` / `surface-soft` | 3.74:1 | 3.0 | Pass |
| `focus` / `surface-dark` | 5.24:1 | 3.0 | Pass |
| `focus` / `surface-elevated` #1a1a1a | 4.35:1 | 3.0 | Pass |
| `primary-dark` #5a8d00 / `canvas` | 4.0:1 | 4.5 | Fail as text, Pass as boundary |
| `hairline` #cccccc / `canvas` | 1.61:1 | 3.0 | **Fail** — extracted, disclosed |
| `primary` #76b900 as text / `canvas` | 2.41:1 | 4.5 | **Fail** — extracted, disclosed |
| `button-ghost-link` `primary` label / `canvas` | 2.41:1 | 4.5 | **Fail** — extracted, disclosed |
| `warning` #df6500 / `canvas` | 3.5:1 | 4.5 | **Fail** — extracted, disclosed (clears 3.0 for large text) |
| `warning-bright` #ef9100 / `canvas` | 2.41:1 | 4.5 | **Fail** — extracted, disclosed |
| `warning-bright` / `surface-dark` | 8.72:1 | 4.5 | Pass — its documented use |
| `stone` #898989 / `canvas` | 3.5:1 | 4.5 | **Fail** as text — disclosed; exempt as disabled |
| `ash` #a7a7a7 / `canvas` | 2.41:1 | 4.5 | **Fail** as text — disclosed; exempt as disabled |
| `canvas` / `surface-soft` (layer separation) | 1.07:1 | — | Layers not self-evident; both rely on the hairline |
| `surface-dark` / `surface-elevated` (layer separation) | 1.21:1 | — | Same, on dark |

All ratios computed with a python3 standard-library snippet using WCAG 2.1 relative luminance; none estimated.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity` | Kept, at `{motion.duration-reduced}` |
| Press | `{motion.duration-instant}` 120ms | `{motion.ease-exit}` | `transform: scale(0.98)` | Scale removed; fill swap untransitioned |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` | Ring appears instantly, never delayed |
| Page / route transition | `{motion.duration-slow}` 600ms | `{motion.ease-enter}` | `opacity` + `translateY(16px -> 0)` | Travel removed, fade at `{motion.duration-reduced}` |
| Modal / drawer | `{motion.duration-base}` in · `{motion.duration-fast}` out | `ease-enter` / `ease-exit` | `opacity` + `translateX(100% -> 0)` | Travel removed, cross-fade |
| Dropdown | `{motion.duration-fast}` in · `{motion.duration-instant}` out | `ease-enter` / `ease-exit` | `opacity` + `translateY(-8px -> 0)` | Travel removed, opacity only |
| Toast | `{motion.duration-base}` in · `{motion.duration-fast}` out | `ease-enter` / `ease-exit` | `opacity` + `translateY(8px -> 0)` | Travel removed, opacity only |
| List enter | `{motion.duration-slow}`, `{motion.stagger-step}` 80ms stagger | `{motion.ease-enter}` | `opacity` + `translateY(24px -> 0)` | Stagger and travel removed; items fade together |
| List exit | `{motion.duration-fast}` | `{motion.ease-exit}` | `opacity` + `translateY(-8px)` | Travel removed, opacity only |
| Loading | `{motion.duration-emphasis}` 900ms per cycle, repeating | linear | `transform: scaleX()` on a 2px `{colors.focus}` bar; `opacity` pulse on skeletons | Bar holds static; skeleton pulse at `{motion.duration-reduced}` |
| Hero reveal (declared brand ambience) | `{motion.duration-emphasis}` image · `{motion.duration-slow}` type, one `{motion.stagger-step}` later | `{motion.ease-enter}` | `transform: scale(1.04 -> 1)` + `opacity` | Frozen at final state |

Every exit is shorter than its entrance. No `width`, `height`, `top`, `left` or `margin` is animated; the harness reports no layout-animation mentions. The only repeating animations are the loader and the one hero reveal, which is stated as ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, `REQUIRED_COLOR_ROLES["text-dim"]`, lines 28-31 | The `text-dim` role is reported missing although this palette carries four muted-text tones: `mute` #757575 ("metadata, breadcrumb separators, footer copyright"), `stone`, `ash` and `on-dark-mute`. The pattern list has `^muted$` and `^muted-` but nothing for the equally common `mute`, and nothing for `on-dark-mute` although it does carry `^on-dark-soft$`. Per SPEC section 1 this is a harness bug, so no alias was added and `tokens` stays at 4. | Add `r"^mute$"`, `r"^mute-"` and `r"^on-dark-mute$"` to the `text-dim` pattern list. Representative-token selection already uses `find_role_strongest` against the canvas for this role, so `mute` (4.61:1) would be picked and `stone`/`ash` would still be measured separately by `check_all` — the failures stay visible. |
| `theme-audit/audit.py`, same list | Because no pattern matches, `check_all("text-dim", ...)` never runs for this file, so the real failures of `stone` (3.5:1) and `ash` (2.41:1) as text on `canvas` were invisible to the harness. They are disclosed in the file by hand. | Same fix; the patterns above make them measured rather than skipped. |
| `theme-audit/audit.py`, `roles_resolved` | `surface` resolves to `surface-dark` #000000 because `^surface[-_]` matches it first, so "text on surface" is measured against the black chapter rather than the light panel surface. It happens to pass here (`ink` on black would have failed, but `check` uses the representative token and `ink` on `surface-dark` is 1.0:1 — it is not reported, so the pairing is being skipped somewhere rather than failing honestly). Worth a look across the roster for two-polarity files. | For files with both polarities, resolve `surface` against the canvas's own polarity (nearest luminance to `canvas`) instead of first-pattern-wins; here that would pick `surface-soft` #f7f7f7. |

### Needs approval

1. **`{component.button-ghost-link}`: `{colors.primary}` #76b900 label on `{colors.canvas}` #ffffff — 2.41:1, needs 4.5:1.** Nearest passing green in the brand family: **#528400** (4.51:1 on white, 4.66:1 on black). The brand's existing `{colors.primary-dark}` #5a8d00 reaches only 4.0:1, so it is not sufficient for body-size text either. No usage note makes #76b900 defensible as text on white: it fails the 3.0:1 large-text threshold too. The alternative to a hex change is a structural one — make the "Learn More →" affordance `{colors.ink}` text with the arrow glyph in `{colors.primary}`, keeping the green as decoration. I did not apply either; the identity hex is frozen and the structural change rewrites a documented component.
2. **`{colors.hairline}` #cccccc on `{colors.canvas}` — 1.61:1, needs 3.0:1.** Nearest passing value: **#949494** (3.0:1). Usage note that makes the real value defensible: #cccccc is scoped to separation between non-interactive blocks, where WCAG 1.4.11 does not apply; the file now prescribes `{colors.mute}` #757575 (4.61:1) wherever a hairline is the only boundary of a control. The frozen hex is unchanged and the failure is disclosed.
3. **`{colors.warning}` #df6500 on `{colors.canvas}` — 3.5:1, needs 4.5:1.** Nearest passing: **#c25400** (4.52:1). Usage note: 3.5:1 clears the 3.0:1 large-text threshold, so #df6500 is defensible at 18px+ or 14px+ bold — which is how a caution banner heading would actually render.
4. **`{colors.warning-bright}` #ef9100 on `{colors.canvas}` — 2.41:1.** No usage note rescues it on white. It is documented as the *inverse* warning tone and passes at 8.72:1 on `{colors.surface-dark}`; the file now says so and forbids the light-canvas use. No value change proposed.
5. **`{colors.focus}` #5a8d00 is prescribed, not extracted.** NVIDIA documents no focus ring anywhere. The value, the 2px outside offset, the single-ring choice over a light/dark pair, and the two-tone variant over hero photography are all this audit's decisions and need a brand sign-off, not just an accessibility one.
6. **The Component States table is largely prescribed.** NVIDIA's documented system policy is that hover states do not exist. Prescribing them is a deliberate departure from an extracted fact, flagged in Known Gaps; if the policy is real rather than an artefact of what was captured, the hover column should be struck and the components declared hover-less.

### Identity verdict

Still unmistakably NVIDIA, and the Cinematic assignment is right — SPEC section 5 rule 1 fires on a hardware-flagship identity, and the tell it names is exactly what this file documents: full-bleed photographic and 3D-rendered hero chapters, sparse 48px type, a single CTA. The white body canvas does not argue against it, as rule 1 says explicitly.

The one tension worth recording is that NVIDIA is both a hardware-flagship brand *and* an engineering-tool brand — a file describing its developer console rather than its marketing pages would be Crisp. I did not switch, because rule 1 is unconditional and because the switch would be argued from a surface this file does not document. Instead the Motion section resolves the tension inside the profile: the hero and content reveals spend the profile's long durations (`duration-slow`, `duration-emphasis`), while chrome state changes sit on `duration-instant` and `duration-fast`, the shortest rungs Cinematic provides. No token value deviates from the profile block, so the file stays a sibling of its profile peers.

The additions stay in the brand's voice rather than drifting to a generic token dump: the focus ring is the brand's own pressed green rather than a borrowed blue, the loading indicator is a 2px bar matching the system's 2px radius and hairline vocabulary, the press state is a 2% scale rather than a shadow lift (the file forbids card shadows), and the states table names NVIDIA's own components — `corner-square`, `pill-tab`, `hero-card-dark` — rather than abstract ones. The single-accent rule is intact: nothing added introduces a second accent colour.
