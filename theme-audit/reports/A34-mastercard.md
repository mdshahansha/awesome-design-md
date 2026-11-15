## A34 · mastercard

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 1 | 5 | 5 | 1 | 1 | 1 |
| after | 5 | 5 | 5 | 5 | 5 | 5 |

The before-run's `refs` and `contrast` fives are vacuous: with no frontmatter
there was nothing to dangle and nothing to measure. Treat them as unscored
rather than as passes.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | J / A | whole file | No frontmatter token block at all. All eight required colour roles, all six required groups and every `{group.token}` reference were absent; the file was unmachine-readable and unreferenceable. |
| P0 | F | whole file | No motion system of any kind: no `motion:` group, no Motion & Animation section, no `prefers-reduced-motion` rule, not one duration or easing curve. |
| P0 | G | whole file | No Accessibility section and no focus ring anywhere. A design document that prescribes an outline-free satellite CTA and a 50%-opacity input hairline, with no focus indicator defined, is unusable for keyboard users. |
| P0 | sections | headings | Eleven of twelve required sections missing because the file used the numbered legacy variant (`## 1. Visual Theme & Atmosphere` …). No `Shapes` section existed at all — the radius ladder was buried as a Layout subsection. |
| P1 | H | Components | Only `default` and `active / pressed` were documented, and only on the two body buttons. Six of the eight contract states appeared nowhere. |
| P1 | B / G | `watermark-ghost` `#E8E2DA` | Ghost watermark headlines run at 1.13:1 on the canvas. Deliberate cream-on-cream, but undisclosed and with no instruction that the text must be `aria-hidden` and non-informational. |
| P1 | B / G | Dust Taupe `#D1CDC7` | Described as placeholder-like text at 1.40:1 on the canvas. The prose said "low contrast on cream; use only for subdued content" without stating that this is a genuine AA failure, not a stylistic choice. |
| P1 | D | button labels, ghost watermark | Three type roles have size, weight and tracking but no stated line height. Not invented; recorded in Known Gaps. |
| P1 | A | footer column headers | Described as "uppercase, muted, weight 700" with no hex. The obvious guess (`ink-muted` on the ink footer) measures 3.36:1 and would fail, so no component pair could be declared. |
| P2 | C | three cream surfaces | `surface-lifted` 1.10:1, `surface-white` 1.13:1 and `surface-bone` 1.03:1 against the canvas. No layer is separable by tone; elevation rests entirely on shadow or a rule, which the file never said out loud. |
| P2 | B | `accent-signal-light` `#F37338` | 2.53:1 on the canvas, below even the 3:1 non-text floor, while the file also assigns it to carousel *active indicators* — a position signal, not pure decoration. |
| P2 | E | footer divider opacity | The Footer section specifies `rgba(255,255,255,0.4)`; the Agent Prompt Guide asks for "1px white-at-30%-opacity". The file contradicts itself. |
| P2 | E | radius ladder | Stated as ranges ("3–6px", "99px / 999px / 1000px") rather than values. The gap at 8–12px is deliberate and documented, so the ladder is internally consistent — the ranges are the only defect. |
| P2 | D | `typography.footer-column-header` | Source gives a "12–14px" range; 14px chosen because Do's and Don'ts and the Agent Prompt Guide both repeat it. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| top of file | no frontmatter -> full YAML block: `colors` (27 tokens), `typography` (14 roles), `spacing`, `rounded`, `shadow`, `motion`, `components` (21 entries) | Dimension J. Every value read out of the file's own prose; nothing measured afresh, nothing invented. |
| `colors:` | — -> `focus: #141413`, `focus-on-ink: #F3F0EE` | No file in the repo defined a focus ring. Ink on the four cream surfaces (16.25–18.43:1), cream on the ink footer (16.25:1). Two tokens because one ring cannot serve both polarities. |
| `shadow:` | three `rgba(...)` values stated in prose with no token -> `none`, `level-1`, `level-2`, `level-3` | SPEC §1: a `shadow:` group is required where the prose states real shadow values. |
| headings | `## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide` -> `## Overview`, `## Colors`, `## Typography`, `## Components`, `## Layout`, `## Elevation & Depth`, `## Do's and Don'ts`, `## Responsive Behavior`, `## Agent Prompt Guide` | SPEC §3 unnumbered set. |
| `### Border Radius Scale` | Layout subsection -> moved verbatim to a top-level `## Shapes`, heading promoted one level | Required section that existed only as a child heading. Moved, not duplicated. |
| `### Iteration Guide`, `### Known Gaps` | children of `## 9. Agent Prompt Guide` -> top-level `## Iteration Guide`, `## Known Gaps` | Both have slots in the contract; the harness only sees `## `. |
| `## Agent Prompt Guide` | section 9 in place -> kept verbatim after `## Known Gaps`, holding Quick Color Reference and Example Component Prompts | Legacy section with no slot in the contract: kept, not deleted or folded in. |
| `## Components` | — -> `### Component States` matrix, 14 components x 8 states | Dimension H. Default and active/pressed marked extracted; the rest labelled prescribed in the preamble. |
| after `## Components` | — -> `## Motion & Animation` | Dimension F. First line states the system is prescribed and unmeasured. Calm block from SPEC §5 verbatim. |
| after `## Elevation & Depth` | — -> `## Accessibility` | Dimension G. 27 measured pairs, the focus-ring spec with its offset, tap targets, reduced motion. |
| `### Shadow Philosophy` | — -> paragraph giving the three surface-to-canvas ratios and naming the two legitimate expressions of depth | Dimension C. The cream tones look like a layer ladder and are not one. |
| `## Known Gaps` | 5 entries -> 15 | Everything the conversion could not recover, plus the two internal contradictions found. |

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` `#141413` / `canvas-cream` `#F3F0EE` | 16.25:1 | 4.5:1 | pass |
| `ink` / `surface-lifted` `#FCFBFA` | 17.84:1 | 4.5:1 | pass |
| `ink` / `surface-white` `#FFFFFF` | 18.43:1 | 4.5:1 | pass |
| `ink` / `surface-bone` `#F4F4F4` | 16.76:1 | 4.5:1 | pass |
| `ink-charcoal` `#262627` / `canvas-cream` | 13.33:1 | 4.5:1 | pass |
| `ink-muted` `#696969` / `canvas-cream` | 4.84:1 | 4.5:1 | pass |
| `ink-muted` / `surface-lifted` | 5.31:1 | 4.5:1 | pass |
| `ink-granite` `#555555` / `canvas-cream` | 6.57:1 | 4.5:1 | pass |
| `ink-graphite` `#565656` / `canvas-cream` | 6.47:1 | 4.5:1 | pass |
| `link-blue` `#3860BE` / `canvas-cream` | 5.16:1 | 4.5:1 | pass |
| `accent-clay` `#9A3A0A` / `canvas-cream` | 6.20:1 | 4.5:1 | pass |
| `on-accent` `#FFFFFF` / `accent-signal` `#CF4500` | 4.66:1 | 4.5:1 | pass |
| `on-ink` `#FFFFFF` / `surface-ink-footer` `#141413` | 18.43:1 | 4.5:1 | pass |
| `border-ink` `#141413` / `canvas-cream` | 16.25:1 | 3.0:1 | pass |
| `hairline-ink-50` `rgba(20,20,19,.5)` -> `#848280` / `canvas-cream` | 3.37:1 | 3.0:1 | pass |
| `focus` `#141413` / `canvas-cream` | 16.25:1 | 3.0:1 | pass |
| `focus` / `surface-lifted` | 17.84:1 | 3.0:1 | pass |
| `focus` / `surface-white` | 18.43:1 | 3.0:1 | pass |
| `focus` / `surface-bone` | 16.76:1 | 3.0:1 | pass |
| `focus-on-ink` `#F3F0EE` / `surface-ink-footer` | 16.25:1 | 3.0:1 | pass |
| `accent-signal` `#CF4500` as text / `canvas-cream` | 4.11:1 | 4.5:1 | **fail** — fill-only, disclosed |
| `accent-signal-light` `#F37338` as text / `canvas-cream` | 2.53:1 | 4.5:1 | **fail** — decorative, disclosed |
| `ink-whisper` `#D1CDC7` as text / `canvas-cream` | 1.40:1 | 4.5:1 | **fail** — real brand failure, disclosed |
| `watermark-ghost` `#E8E2DA` / `canvas-cream` | 1.13:1 | 3.0:1 | **fail** — deliberate, disclosed |
| `brand-red` `#EB001B` / `canvas-cream` | 4.07:1 | 4.5:1 | **fail** — logo mark only, disclosed |
| `brand-yellow` `#F79E1B` / `canvas-cream` | 1.88:1 | 4.5:1 | **fail** — logo mark only, disclosed |
| `ink-muted` / `surface-ink-footer` | 3.36:1 | 4.5:1 | **fail** — never place muted grey on the footer, disclosed |
| `border-on-ink` `rgba(255,255,255,.4)` over its real ground `#141413` -> `#727271` / `surface-ink-footer` | 3.83:1 | 3.0:1 | pass (real rendering) |
| `border-on-ink` composited over `canvas-cream` -> `#f8f6f5` / `canvas-cream` | 1.05:1 | 3.0:1 | **fail** — harness artifact, disclosed |
| `border-on-ink` composited over `canvas-cream` -> `#f8f6f5` / `surface-lifted` | 1.04:1 | 3.0:1 | **fail** — harness artifact, disclosed |

All computed with a `python3` snippet using WCAG 2.1 relative luminance; none
estimated. Undisclosed failures after the edit: zero.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | `opacity`, `translateY(-1px)` | travel removed; opacity at `{motion.duration-reduced}` |
| Press / active | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | `scale(0.98)` | no scale, no substitute |
| Focus ring appears | `{motion.duration-instant}` 80ms | `{motion.ease-enter}` | `opacity` | unchanged — never delayed or faded out |
| Page / route transition | `{motion.duration-base}` 250ms | `{motion.ease-standard}` | `opacity` | opacity at `{motion.duration-reduced}` |
| Modal or drawer enter | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | `opacity`, `translateY(12px)` | travel removed; opacity at `{motion.duration-reduced}` |
| Modal or drawer exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | `opacity`, `translateY(8px)` | travel removed; opacity at `{motion.duration-reduced}` |
| Dropdown | `{motion.duration-fast}` 150ms | `{motion.ease-enter}` | `opacity`, `translateY(-4px)` | travel removed; opacity at `{motion.duration-reduced}` |
| Toast | in 250ms, out 150ms | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity`, `translateY(8px)` | travel removed; opacity at `{motion.duration-reduced}` |
| List enter | `{motion.duration-base}` 250ms, stagger `{motion.stagger-step}` 40ms | `{motion.ease-enter}` | `opacity`, `translateY(8px)` | stagger and travel removed; one opacity fade at `{motion.duration-reduced}` |
| List exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | `opacity` | opacity at `{motion.duration-reduced}` |
| Loading | 1200ms loop | linear | `rotate()`, `opacity` | spinner frozen; static cream-tinted placeholder remains |

`transform` and `opacity` only. Every exit is shorter than its entrance. The
spinner is the only infinite animation; the orbital arcs are static geometry,
not ambience, so nothing else loops.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, lines 170–182 | Every `rgba()` token is composited over the canvas regardless of the ground the prose binds it to. `border-on-ink` is stated as `rgba(255,255,255,0.4)` and only ever drawn on the `#141413` footer, where it is 3.83:1 and passes; the harness composites it over cream and reports 1.05:1 and 1.04:1. Two of this file's three remaining failures are manufactured by this, and an agent reading the JSON without checking would "fix" a token that is already correct. | Let a token declare its ground — e.g. composite over the `backgroundColor` of any `components:` entry that references the token, falling back to the canvas only when nothing binds it. Minimal version: skip `check_all("border", …)` for a composited token that appears as a `border:` property on a component whose own `backgroundColor` is a different surface. |
| `theme-audit/audit.py`, lines 276–306 | SPEC §2's table requires `on-accent` on `accent` at 4.5:1, and no `check()` call measures that pair. It is caught only indirectly, and only when a `components:` entry happens to bind the two. A file with an `accent` and an `on-accent` token and no component using them is never checked. | Add `check("on-accent", "accent", 4.5, "ink on accent")` beside the existing calls. (This file passes the pair at 4.66:1 either way.) |
| `theme-audit/audit.py`, lines 28–31 | The `text-dim` pattern list enumerates suffixes (`^ink-(muted|subtle|soft|tertiary|secondary|light)`), so a muted ink named for a brand tone escapes every check. This file's `ink-whisper` (`#D1CDC7`, 1.40:1) is documented as placeholder text and is invisible to the harness; it is disclosed here only because I measured it by hand. Widening the regex is the wrong fix — it would start matching decorative tones too. | Measure every `colors:` token that any `components:` entry uses as a `textColor`, whatever its name, and leave the role patterns for role resolution only. The component bindings already encode which tokens are ink. |
| `theme-audit/audit.py`, line 435 | `durations_found` uses `\b(\d{2,4})ms\b`, so `{motion.stagger-step}`'s 40ms is reported as a duration. Cosmetic — it only feeds the fallback score of 3 — but it makes the JSON misleading. | Exclude the `stagger-step` value, or report stagger separately. |

No role on this file looked unsatisfied while plainly present under another
name, so there is no harness bug of that kind to report: all eight roles were
missing because the file had no frontmatter at all. No alias token was added to
satisfy a pattern. `focus` and `focus-on-ink` are new values for a role the file
genuinely did not have, not renames of existing tokens.

### Needs approval

1. **`focus` and `focus-on-ink` are prescribed, not extracted.** Mastercard's
   real focus treatment was never captured. I chose the brand's own ink
   (`#141413`) and canvas cream (`#F3F0EE`) at 2px with a 2px offset rather than
   a chromatic ring, because the file is explicit that Signal Orange belongs to
   consent and compliance signalling and a ring in that colour would dilute the
   legal signal. Measured: 16.25:1 on `canvas-cream`, 17.84:1 on
   `surface-lifted`, 18.43:1 on `surface-white`, 16.76:1 on `surface-bone`,
   16.25:1 for `focus-on-ink` on the ink footer. If Mastercard's real ring is
   ever captured, these two tokens should be replaced wholesale.
2. **`watermark-ghost` `#E8E2DA` on `canvas-cream` is 1.13:1** against a 3:1
   requirement for 72px+ display text. Nearest passing value `#8E8A85`
   (3.02:1) — which destroys the treatment, since cream-on-cream *is* the
   gesture. Usage note that makes the real value defensible: the watermark is
   decorative only, must be `aria-hidden`, and must never carry information not
   also present in the eyebrow label and the H2 beside it. Recommend keeping the
   real value with that constraint.
3. **`ink-whisper` `#D1CDC7` on `canvas-cream` is 1.40:1** where the file
   assigns it to placeholder-like empty-state labels. Nearest passing value is
   already in the palette: `ink-muted` `#696969` at 4.84:1. Usage note:
   `ink-whisper` is defensible only as hairline-weight decoration, never as text
   a reader must parse. I did not change the hex; I scoped it in the prose and
   disclosed the ratio.
4. **`accent-signal-light` `#F37338` is 2.53:1 on the canvas** and the file
   assigns it both to decorative orbital arcs (fine) and to *carousel active
   indicators* (not fine — that is a position signal below the 3:1 non-text
   floor). Nearest passing value for the indicator role `#A85020` (4.83:1), but
   it stops reading as the same carroty orange. Usage note I put in the file
   instead: pair the active dot with a size or shape change so colour is not the
   sole indicator. Needs a decision on whether the dot keeps the brand hex.
5. **`accent-signal` `#CF4500` is 4.11:1 as text on cream.** It passes as a fill
   behind white (4.66:1), which is the file's only documented use. Nearest
   passing text value `#B83C00` (5.02:1). Usage note: the token is fill-only;
   it must not be set as text or as a meaning-bearing icon on cream. No change
   made to the hex.
6. **`ink-muted` `#696969` on the ink footer is 3.36:1.** The source describes
   footer column headers as "uppercase, muted, weight 700" without a hex. I did
   **not** bind that pair, because guessing it would have manufactured a failure
   the real page may not have. Needs the real value.
7. **The footer divider contradiction** (`rgba(255,255,255,0.4)` in the Footer
   section vs "white-at-30%-opacity" in the Agent Prompt Guide) needs a ruling.
   `border-on-ink` currently takes 40%, the figure attached to a named
   component.
8. **Three type roles have no line height** in the source
   (`button-primary-label`, `button-consent-label`, `ghost-watermark`). I left
   them absent rather than deriving one from a sibling role.

### Identity verdict

Still unmistakably Mastercard. The conversion is additive: the whole of the
original prose survives, including the orbit-and-trajectory paragraph, the
satellite-CTA mechanics, the hand-drawn arc motif and the ghost-watermark
treatment, and the new frontmatter is named in the brand's own vocabulary —
`canvas-cream`, `ink-whisper`, `accent-signal`, `watermark-ghost`,
`surface-ink-footer` — rather than in a generic `surface-1` / `gray-500` ladder.
Nothing in the token block would suit another file in the collection: the 450
body weight, the 20 / 40 / 999 radius ladder with its deliberate 8–12px hole,
and a palette whose brand red and yellow are explicitly barred from the UI are
all specific to this document.

**Calm is the right profile and I kept it.** SPEC §5's assignment rule lands
there by both routes. Rule 1 does not fire: there is full-bleed photography, but
the identity is a payments network, not luxury, automotive, hardware, gaming or
aerospace, and the type is dense rather than sparse. Rule 2 does not fire. Rule
3 is the only real temptation — the palette lists a red, a yellow, two oranges
and a clay — and it fails on role, exactly as SPEC's worked example describes:
the saturated colours are barred from interactive elements by the file's own
rules (brand red and yellow are logo-only; Signal Orange is quarantined to
consent flows; the light orange draws decorative arcs), the primary CTA is a
black pill, the file forbids programmatic gradients, and its own description is
"editorial". Rule 4 is therefore the terminal answer. The file's independent
evidence agrees: a display weight of 500 rather than 700+, "slow down, read one
thing at a time" as the stated whitespace philosophy, shadows described as
"atmospheric cushioning", and circles that "feel like they're in motion even
though the page is still" — which is a brief for short opacity-led fades with
little travel, i.e. Calm.
