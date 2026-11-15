## A04 · aljazeera

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| | tokens | refs | contrast | sections | motion | states |
|---|---|---|---|---|---|---|
| before | 2 | 5 | 3 | 1 | 1 | 1 |
| after | 5 | 5 | 4 | 5 | 5 | 5 |

Contrast stops at 4 and cannot go higher without falsifying a hex: white-on-orange (2.32:1) is an extracted brand fact and is recorded under Needs approval instead.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation` section, no reduced-motion rule. The reason this audit exists. |
| P0 | G Accessibility | whole file | No `## Accessibility` section; four real AA failures undocumented. |
| P0 | A Tokens | `colors` | No `focus` role at all — the file documented no focus ring, and the ink-pill/dark-network polarity means one ring cannot serve both surfaces. |
| P0 | B Colour | `on-primary` on `primary` | White on #fa9000 is 2.32:1 against a 4.5:1 requirement. Real brand failure; hex frozen. |
| P0 | B Colour | `section-rail-teal` | White label on `rail-teal` #00cbca is 2.02:1 — misses even the 3:1 large-text threshold. Harness never checked it (teal is not named like a signal token), so it was hiding entirely. |
| P1 | A Tokens | `colors` | No key matched the `surface` or `text-dim` roles, although the prose documents `soft` as the newsletter fill and `slate` as secondary text. Role names were simply absent. |
| P1 | B Colour | `hairline`, `silver` | 1.43:1 and 1.86:1 on canvas, below the 3.0:1 a boundary needs, while `most-popular-row` and `ex-pricing-tier` used `hairline` as their only edge. |
| P1 | B Colour | `network-nav-active` | `amber` #ffa000 active nav link on white is 2.04:1. Fails as text. |
| P1 | B Colour | `network-select` | 3px `select-gold` border is 1.59:1 on canvas — the system's loudest edge is its least visible. |
| P1 | H States | every component | Only the network nav's `active` was documented. hover, focus-visible, pressed, disabled, loading, selected, error named nowhere. |
| P1 | C Sections | — | `Responsive Behavior` and `Known Gaps` missing; responsive content existed only as `### Responsive Strategy` nested under Layout. |
| P2 | A Tokens | `shadow` | The Elevation table stated a literal `rgba(0, 0, 0, 0.175)` with no token to reference (SPEC §1). |
| P2 | C Elevation | `canvas` / `soft` | Canvas-to-surface is 1.14:1; the newsletter card is barely a layer. True to the brand, but it needs padding and type hierarchy to read as a panel — now stated. |
| P2 | D Typography | all type tokens | Every role has size, weight and line height, and body (#333333 on #ffffff, 12.63:1) is readable on every surface the file defines. `letterSpacing: 0` across eleven tokens is a default, not a measurement — logged in Known Gaps. |
| P2 | E Ladders | `rounded`, `spacing` | Both ladders are internally consistent; the radius scale is deliberately bimodal (2–10px imagery, 18–22px controls) and the file already explains why. No value sits outside its scale. No change made. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | 20 keys -> 25; added `surface-soft`, `text-secondary`, `border-control`, `focus`, `focus-on-dark` under a "prescribed, not extracted" comment | Fills the `surface`, `text-dim`, `border` and `focus` roles (SPEC §1). Four of the five reuse hexes the file already documents, so no new hue enters the palette. |
| frontmatter | added `shadow:` group with `dropdown` | SPEC §1: the prose stated a real shadow with no token. |
| frontmatter | added `motion:` group, 9 keys, Calm values | SPEC §4/§5. |
| `## Colors` | added "Prescribed Accessibility Tokens (not extracted)" subsection; hairline/silver line now states their measured ratios and scopes them to decoration | SPEC §2 requires the parallel accessible token to be labelled and the original scoped. |
| `## Elevation & Depth` | literal rgba -> `{shadow.dropdown}` plus the literal | Reference integrity. |
| `## Components` | added `### State Coverage` table, 13 rows | SPEC §7. Component-by-component rather than rewriting 25 entries, to keep the diff reviewable. Static-only components are stated as genuinely single-state. |
| new `## Motion & Animation` (after Components) | — -> full section: prescribed disclaimer as its first line, profile argument, 10-interaction table, rules, reduced-motion block | SPEC §3/§6. |
| new `## Accessibility` | — -> 19-pair measured contrast table, four named brand failures, two-ring focus system with per-surface ratios, layer ratio, tap-target intent, reduced motion | SPEC §3, brief G. |
| `## Do's and Don'ts` | added 3 Don'ts (layout-property animation, text on orange / white on teal, suppressing the focus ring) | Keeps the new rules where a reader of this file will actually hit them. |
| new `## Responsive Behavior` | — -> width table for state and motion only, cross-referencing Layout | Required section, without duplicating the breakpoint table already in Layout. |
| new `## Known Gaps` | — -> 10 items | Required section; everything prescribed or unverifiable is named there. |

Nothing outside these locations was reflowed. No extracted hex, type value, spacing or radius value was changed.

### Contrast checks

All computed with `theme-audit/audit.py`'s WCAG 2.1 luminance functions, not estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #000000 / canvas #ffffff | 21.00 | 4.5 | Pass |
| charcoal #333333 / canvas #ffffff | 12.63 | 4.5 | Pass |
| text-secondary #595959 / canvas #ffffff | 7.00 | 4.5 | Pass |
| text-secondary #595959 / surface-soft #f0f0f0 | 6.15 | 4.5 | Pass |
| ink #000000 / surface-soft #f0f0f0 | 18.43 | 4.5 | Pass |
| border-control #595959 / canvas #ffffff | 7.00 | 3.0 | Pass |
| hairline #d8d8d8 / canvas #ffffff | 1.43 | 3.0 | Fail — scoped to decoration |
| silver #bebebe / canvas #ffffff | 1.86 | 3.0 | Fail — scoped to decoration |
| on-primary #ffffff / primary #fa9000 | 2.32 | 4.5 | **Fail — frozen brand hex** |
| ink #000000 / primary #fa9000 | 9.05 | 4.5 | Pass (the accessible alternative) |
| on-primary #ffffff / live-red #c31833 | 6.00 | 4.5 | Pass |
| on-primary #ffffff / rail-red #bc0000 | 6.69 | 4.5 | Pass |
| on-primary #ffffff / rail-teal #00cbca | 2.02 | 4.5 | **Fail — frozen brand hex** |
| ink #000000 / rail-teal #00cbca | 10.40 | 4.5 | Pass (the accessible alternative) |
| on-primary #ffffff / indigo #272967 | 13.13 | 4.5 | Pass |
| on-primary #ffffff / network-canvas #181818 | 17.76 | 4.5 | Pass |
| on-primary #ffffff / night-navy #100e2f | 18.65 | 4.5 | Pass |
| mist #dddddd / network-canvas #181818 | 13.07 | 4.5 | Pass |
| mist #dddddd / ink #000000 | 15.46 | 4.5 | Pass |
| graphite #323232 / canvas #ffffff | 12.82 | 4.5 | Pass |
| amber #ffa000 / canvas #ffffff | 2.04 | 4.5 | **Fail — frozen brand hex** |
| gold #dba200 / canvas #ffffff | 2.29 | 3.0 | Fail — decorative rules only |
| select-gold #ffc500 / canvas #ffffff | 1.59 | 3.0 | **Fail — frozen brand hex (control border)** |
| focus #000000 / canvas #ffffff | 21.00 | 3.0 | Pass |
| focus #000000 / surface-soft #f0f0f0 | 18.43 | 3.0 | Pass |
| focus #000000 / primary #fa9000 | 9.05 | 3.0 | Pass |
| focus #000000 / rail-teal #00cbca | 10.40 | 3.0 | Pass |
| focus-on-dark #ffc500 / ink #000000 | 13.24 | 3.0 | Pass |
| focus-on-dark #ffc500 / network-canvas #181818 | 11.19 | 3.0 | Pass |
| focus-on-dark #ffc500 / night-navy #100e2f | 11.76 | 3.0 | Pass |
| focus-on-dark #ffc500 / indigo #272967 | 8.28 | 3.0 | Pass |
| focus-on-dark #ffc500 / rail-red #bc0000 | 4.22 | 3.0 | Pass |
| focus-on-dark #ffc500 / rail-teal #00cbca | 1.27 | 3.0 | Fail — so teal takes the black ring, stated in the file |
| canvas #ffffff / surface-soft #f0f0f0 | 1.14 | — | Layer separation, not a text pair |

### Motion inventory

Profile: **Calm**. Prescribed, not measured — stated as the first line of the file's Motion section.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | 150ms `{motion.duration-fast}` | `{motion.ease-standard}` | opacity | Opacity kept at 150ms; underline instant |
| Press | 80ms `{motion.duration-instant}` | `{motion.ease-standard}` | opacity to 0.9 | Opacity only at 80ms; no scale in either mode |
| Focus | 80ms | `{motion.ease-standard}` | opacity | Ring drawn untransitioned |
| Page / route | 250ms `{motion.duration-base}` | `{motion.ease-standard}` | opacity | Cross-fade to 150ms, no travel |
| Modal / drawer | 250ms in, 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity + translateY(8px) | Travel removed; 150ms fade |
| Dropdown | 150ms in, 80ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity + translateY(4px) | Travel removed; 150ms fade |
| Toast | 250ms in, 150ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | opacity + translateY(8px) | Travel removed; 150ms fade |
| List enter | 250ms, 40ms `{motion.stagger-step}`, 6 items max | `{motion.ease-enter}` | opacity + translateY(6px) | Stagger and travel removed; items appear at full opacity |
| List exit | 150ms | `{motion.ease-exit}` | opacity | Removed without transition |
| Loading | 600ms `{motion.duration-emphasis}` per cycle, infinite | `{motion.ease-standard}` | opacity 1 → 0.4 → 1 | Pulse frozen at full opacity; text label carries the state |

Exits are shorter than their entrances throughout; only transform and opacity are animated; the single infinite animation is the live-dot / loader pulse, declared as deliberate brand ambience.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line ~84 (`parse_frontmatter`) | A trailing YAML comment on a token line silently destroys the value: `focus: "#000000"  # ring` yields the raw string `"#000000"  # ring`, fails the hex `fullmatch`, and the token vanishes from `colors` with no warning. I hit this on my first edit and scored 2/5 on tokens with all five tokens present in the file. Real YAML strips the comment. | In the second-level branch, drop an unquoted trailing comment before stripping: `val = re.sub(r'\s+#.*$', '', m.group(2))` when the value does not itself start with `#` followed by a hex digit — or, more safely, match a quoted value first (`^"([^"]*)"`) and fall back to the bare token. |
| `theme-audit/audit.py` lines ~160-170 (signal-colour loop) | Signal colours are found by name (`^(primary\|accent\|secondary\|brand\|cta)`), so `rail-teal` at 2.02:1 under white text and `amber` at 2.04:1 as a link colour were invisible to the harness. Any brand whose signal tones are named for what they look like rather than for their role escapes the check SPEC §2 promises ("every signal colour is checked"). | Additionally check every `colors` key that any `components:` entry pairs with a `textColor`: audit the real fg/bg pairs the frontmatter asserts, not the pairs the names suggest. That is already computable from the data in every file. |
| `theme-audit/SPEC.md` §4 vs §5 | §4 prints one literal `motion:` block (`ease-standard: cubic-bezier(0.2, 0, 0, 1)`, an asymmetric decelerate) while §5 says Calm's easing bias is "symmetric ease", then adds "values are per profile, not identical across files". The two contradict for every Calm site, which is 60-odd of the 84. | State in §4 that the block is the Crisp/default literal and that profiles override easing, and add one literal easing triple per profile row in §5's table. |
| `theme-audit/SPEC.md` §1 | Requires a `focus` role in every file, and §2 requires 3:1 against "every surface it can appear over", but the required-role table lists only `focus` / `focus-on-dark`. A file like this one has three distinct polarities (white paper, ink pills, dark network ground) and the ink pill is neither the canvas nor the dark network canvas. Two rings happened to cover it here. | Say explicitly that the ring count follows the surface count, and that the Accessibility section must map ring → surface, which is what this file now does. |

### Needs approval

1. **`on-primary` on `primary` — white #ffffff on Jazeera orange #fa9000, 2.32:1, needs 4.5:1.** Hex frozen; this is the brand's identity colour. Nearest passing value: `{colors.ink}` #000000 on the same orange measures 9.05:1. Usage note that makes the real value defensible: the orange block is the logo surface and the white mark on it is the eagle calligraphy — a trademark graphic, not text, which WCAG 1.4.3 excludes. Approve either (a) the usage note, scoping `on-primary` on `primary` to logo art only and forbidding label text on orange, or (b) swapping to ink for any text that does sit on orange. The file currently documents (a) with (b) as the fix. This is the one remaining harness failure.
2. **White on `rail-teal` #00cbca, 2.02:1.** The rotated rail labels are large display type, so the applicable threshold is 3:1 — and 2.02:1 misses that too. Nearest passing value: `{colors.ink}` on teal, 10.40:1. Approve black rail labels on teal while white stays on `rail-red` (6.69:1), or approve a documented, knowing failure.
3. **`amber` #ffa000 active nav links on white, 2.04:1.** Nearest passing value from the existing palette: `{colors.graphite}` #323232 at 12.82:1 with amber kept as a 3px underline, which preserves the gilded identity at zero contrast cost. Needs approval because it changes what the active nav state looks like.
4. **3px `select-gold` #ffc500 border on white, 1.59:1 against a 3:1 boundary threshold.** Usage note: the border is 3px and decorative-emphatic, but it is also the control's only boundary, so 3:1 applies. Proposal: keep the gold edge and add a 1px `{colors.border-control}` inner edge (7.00:1). Approve the double edge or accept the failure.
5. **Five prescribed token names added to a documentary file.** `surface-soft`, `text-secondary` and `border-control` are aliases of extracted hexes; `focus` (#000000) and `focus-on-dark` (#ffc500, the extracted select-gold) are new roles for existing values. No new hex was invented, but the names are mine and should be reviewed against whatever convention the other 83 files settle on.

### Identity verdict

Still Al Jazeera. Nothing was added that a different file could have supplied: the focus ring is black because this system's controls are already black pills, the dark-surface ring is the brand's own select-gold rather than a generic blue, the motion section argues the Calm profile from this file's own evidence (flat paper, no shadows, no gradients, weight-led hierarchy, a printed eyebrow bar), and the one sanctioned infinite animation is the live-red timeline pulse — which is the brand's single loudest idea, not a borrowed loader.

The Calm assignment is correct and I did not change it. The file is sober and editorial, it forbids gradients outright, its display hierarchy is weight rather than colour, and its own prose calls the page "a printing press, not a product". Playful is excluded despite 25 hexes: the saturated tones (teal, crimson, gold) are static section rails and rules, never interactive chrome, and orange is explicitly barred from buttons and links. Cinematic is excluded because the news polarity — the primary surface — is white paper at maximum density, not a dark premium stage; the network pages are a secondary corporate surface, not the identity. Crisp is excluded because this is not a tool.

The one drift risk is the `ex-*` Examples block, which predates this audit and reads as boilerplate shared across the collection ("Re-uses feature-card chrome" refers to a `feature-card` component this file does not define — not a dangling token reference, so the harness cannot see it, but still a sentence written for a different file). I left it alone: it is labelled illustrative, and rewriting it was outside both the brief's dimensions and a reviewable diff. Flagging it per SPEC §8.
