## A15 · coinbase

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

- **Before:** 4 · 5 · 1 · 3 · 1 · 1
- **After:** 5 · 5 · 5 · 5 · 5 · 5

Every harness finding in the brief was reproduced before any edit: `focus` missing;
six undisclosed contrast failures plus one component failure (`legal-band`);
`Motion & Animation` and `Accessibility` absent; six states never documented in a
structured Components line.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A Token contract | `colors.focus` | No focus token anywhere in the file, and no component described a focus indicator, so keyboard operation was undocumented. |
| P0 | F Motion | whole file | No `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Known Gaps declared "Animation timings out of scope" — a statement of absence, not a system. |
| P0 | G Accessibility | whole file | No `## Accessibility` section. Seven measured contrast failures undisclosed, including a real small-text AA failure. |
| P0 | B Colour | `legal-band` | `{colors.muted}` #7c828a on #ffffff at `{typography.caption}` 13px = 3.88:1, needs 4.5:1. Small text, so no large-text exemption. Genuine brand failure. |
| P1 | B Colour | `hairline` / `hairline-soft` | 1.31:1 and 1.14:1 on canvas. `text-input` and `search-input-pill` named `hairline` as their only boundary, so an interactive control had a 1.31:1 edge against 3:1 required. |
| P1 | B Colour | `semantic-up` #05b169 | 2.8:1 on canvas — the "price up" green fails AA as text at any size, and the file mandates it as text colour only. No role matches it, so the harness never checked it. |
| P1 | H States | every component entry | Only `active` and `disabled` documented. Iteration Guide item 5 actively stated hover is never documented. |
| P2 | C Elevation | `surface-dark-elevated` vs `surface-dark` | The signature floating product-UI card separates from its hero canvas by 1.11:1; previously unstated. |
| P2 | C Elevation | Elevation & Depth table | Border tier and shadow tier coexist. Left as-is: it is a consistent rule (border on white cards, single shadow on hover), not random mixing. |
| P2 | B Colour | `muted-soft` #a8acb3 | 2.28:1 / 2.13:1. Defensible — scoped to disabled link text, which WCAG exempts. Now stated. |
| P2 | E Radius | `rounded` ladder | Consistent 0/4/8/12/16/24/100/9999. `pill` and `full` coexist deliberately (pill vs circle). No value outside its scale. No change. |
| P2 | D Typography | all roles | Every role carries family, size, weight, line height, letter spacing. Body 16px/1.5 reads 6.21:1 on canvas, 5.8:1 on the soft band. No change needed. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors:` | — -> `hairline-strong: "#767b85"` | Parallel accessible boundary token at 4.25:1 on canvas, so controls get an edge clearing 3:1 without touching the frozen brand hairlines. Labelled prescribed. |
| frontmatter `colors:` | — -> `focus: "#0052ff"` | Required role. Reuses Coinbase Blue rather than inventing a second voltage, which the brand's own first Don't forbids. |
| frontmatter | — -> `motion:` group, Calm block verbatim from SPEC | Required group; verbatim so sibling Calm files stay comparable. |
| `## Colors` → Hairlines | plain descriptions -> measured ratios, both hairlines scoped to decoration, new Hairline Strong entry | SPEC section 2: scope the frozen tone, add the parallel token alongside. |
| `## Colors` | — -> new `### Focus` subsection | Ring colour, mandatory 2px offset, and the fact that it is prescribed. |
| `## Components` → `text-input` | "1px hairline border" -> "1px `{colors.hairline-strong}` border" plus focus-visible ring | A text input's boundary at 1.31:1 was the clearest case of a decorative tone doing load-bearing work. |
| `## Components` → `search-input-pill` | — -> fill-vs-canvas 1.07:1 noted, boundary required | Its grey fill is not a perceptible edge on its own. |
| `## Components` | — -> new `### Component States` table | State coverage; genuinely static entries say "two states only" instead of padding the list. |
| after `## Components` | — -> new `## Motion & Animation` | First line states the system is prescribed, not measured. Interaction table, rules, `prefers-reduced-motion` block. |
| after Motion | — -> new `## Accessibility` | 26 measured pairs, focus ring per surface, tap targets, reduced motion, colour-alone rule. |
| `## Iteration Guide` item 5 | "Hover state never documented. Only Default and Active/Pressed." -> names the three observable states, labels the rest prescribed | The old line contradicted the new states table. |
| `## Known Gaps` | "Animation timings out of scope." -> four lines naming every prescribed element and the real `legal-band` AA failure | Prescribed values must be labelled; a real brand failure belongs in the document. |

No brand hex was changed. No section was reflowed.

### Contrast checks

Computed with WCAG 2.1 relative luminance via the harness's own `contrast()`.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #0a0b0d / canvas #ffffff | 19.69:1 | 4.5:1 | Pass |
| ink #0a0b0d / surface-soft #f7f7f7 | 18.38:1 | 4.5:1 | Pass |
| body #5b616e / canvas #ffffff | 6.21:1 | 4.5:1 | Pass |
| body #5b616e / surface-soft #f7f7f7 | 5.8:1 | 4.5:1 | Pass |
| on-primary #ffffff / primary #0052ff | 5.75:1 | 4.5:1 | Pass |
| on-dark #ffffff / surface-dark #0a0b0d | 19.69:1 | 4.5:1 | Pass |
| on-dark-soft #a8acb3 / surface-dark #0a0b0d | 8.64:1 | 4.5:1 | Pass |
| hairline-strong #767b85 / canvas #ffffff | 4.25:1 | 3.0:1 | Pass (prescribed) |
| focus #0052ff / canvas #ffffff | 5.75:1 | 3.0:1 | Pass |
| focus #0052ff / surface-soft #f7f7f7 | 5.37:1 | 3.0:1 | Pass |
| focus #0052ff / surface-strong #eef0f3 | 5.04:1 | 3.0:1 | Pass |
| focus #0052ff / surface-dark #0a0b0d | 3.42:1 | 3.0:1 | Pass |
| focus #0052ff / surface-dark-elevated #16181c | 3.09:1 | 3.0:1 | Pass, no margin |
| focus #0052ff / primary #0052ff | 1.0:1 | 3.0:1 | Fail by construction — ring never drawn on the blue fill; 2px canvas offset sits between them. Disclosed |
| muted #7c828a / canvas #ffffff | 3.88:1 | 4.5:1 | Fail — disclosed, large text only |
| muted #7c828a / surface-soft #f7f7f7 | 3.62:1 | 4.5:1 | Fail — disclosed |
| muted #7c828a in legal-band at 13px / canvas #ffffff | 3.88:1 | 4.5:1 | Fail — real small-text AA failure, disclosed |
| muted-soft #a8acb3 / canvas #ffffff | 2.28:1 | 4.5:1 | Fail — disabled-text use only, disclosed |
| muted-soft #a8acb3 / surface-soft #f7f7f7 | 2.13:1 | 4.5:1 | Fail — disclosed |
| hairline #dee1e6 / canvas #ffffff | 1.31:1 | 3.0:1 | Fail — scoped to decoration, disclosed |
| hairline-soft #eef0f3 / canvas #ffffff | 1.14:1 | 3.0:1 | Fail — scoped to decoration, disclosed |
| semantic-up #05b169 / canvas #ffffff | 2.8:1 | 4.5:1 | Fail — disclosed, glyph required alongside |
| semantic-down #cf202f / canvas #ffffff | 5.38:1 | 4.5:1 | Pass |
| accent-yellow #f4b000 / canvas #ffffff | 1.9:1 | 4.5:1 | Fail as text — illustrative glyph fill only, disclosed |
| on-primary #ffffff / primary-active #003ecc | 8.2:1 | 4.5:1 | Pass |
| on-primary #ffffff / primary-disabled #a8b8cc | 2.02:1 | — | Exempt (disabled) |
| surface-soft #f7f7f7 / canvas #ffffff | 1.07:1 | — | Layer separation, not a boundary; band rhythm comes from spacing |
| surface-strong #eef0f3 / surface-soft #f7f7f7 | 1.07:1 | — | Same |
| surface-dark-elevated #16181c / surface-dark #0a0b0d | 1.11:1 | — | The signature floating card barely separates from its hero; now stated |

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 150ms | `{motion.ease-standard}` | opacity, scale(1.01) on cards only | Scale removed, opacity at 150ms |
| Press | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | scale(0.98) plus fill swap | Scale removed, colour change kept |
| Focus ring | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | opacity | Instant, never animated away |
| Page / route | `{motion.duration-base}` 250ms | `{motion.ease-standard}` | opacity, translateY 8px | Travel removed, cross-fade 150ms |
| Modal / drawer enter | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | opacity, translateY or translateX 8px | Travel removed, fade 150ms |
| Modal / drawer exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | opacity, transform | Travel removed, fade 150ms |
| Dropdown enter | `{motion.duration-fast}` 150ms | `{motion.ease-enter}` | opacity, translateY 4px | Travel removed, fade 150ms |
| Dropdown exit | `{motion.duration-instant}` 80ms | `{motion.ease-exit}` | opacity | Fade 150ms |
| Toast enter | `{motion.duration-base}` 250ms | `{motion.ease-enter}` | opacity, translateY 8px | Travel removed, fade 150ms |
| Toast exit | `{motion.duration-fast}` 150ms | `{motion.ease-exit}` | opacity, transform | Travel removed, fade 150ms |
| List enter | `{motion.duration-base}` 250ms, stagger `{motion.stagger-step}` 40ms | `{motion.ease-enter}` | opacity, translateY 4px | Stagger and travel removed, one fade at 150ms |
| List exit | `{motion.duration-fast}` 150ms, no stagger | `{motion.ease-exit}` | opacity | Fade 150ms |
| Loading | `{motion.duration-emphasis}` 500ms loop | linear | rotate / opacity pulse | Frozen, static indicator remains |
| Hero product-UI card reveal | `{motion.duration-emphasis}` 500ms | `{motion.ease-enter}` | opacity, translateY 8px | Travel removed, fade 150ms, content never delayed |

Every exit is shorter than its entrance. Only `transform` and `opacity` animate.
The loader is the only loop; the file states there is no brand ambience, which
matches a brand whose identity is composure.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py`, the `check_all` call block (only `text-dim` and `border` passed) | Signal colours outside the `accent` role are never contrast-checked. `semantic-up` #05b169 at 2.8:1 on canvas is a real text failure here and the harness reported nothing, although SPEC section 2 says every signal colour is checked. | Add `check_all("accent", "canvas", 4.5, ...)` and extend the `accent` patterns with `^semantic-`, or add a `signal` role covering `^semantic-`, `^success`, `^error`, `^warning`, `^danger`. |
| `theme-audit/audit.py`, `find_role_strongest` (applied to `border`) | Adding a passing `hairline-strong` silently re-represents the role, so `check("border","canvas")` passes while the tones actually drawn on most surfaces still fail. Only `check_all` catches them. | Keep `find_role_strongest` for reporting but also run the representative check on `find_role`, or report both variants. |
| `theme-audit/audit.py`, `disclosed()` | Disclosure matches a substring of the token name on any line that states any ratio, so a line about `hairline` also discloses `hairline-soft`, and one line naming `muted` clears four distinct pairs. | Match the token name as a whole word and require the stated ratio to equal the measured one. |
| `theme-audit/SPEC.md`, headings 4 and 5 | The literal motion token blocks sit under "## 4. Motion tokens" while the profile table is "## 5. Motion profiles"; the briefs cite "SPEC section 5" for the token block. | Renumber, or have the briefs cite section 4 for values and 5 for profile choice. |
| `theme-audit/__pycache__/audit.cpython-315.pyc` | A compiled artifact is tracked in git, so any agent importing `audit.py` dirties the working tree. | Remove it from the index and add `__pycache__/` to `.gitignore`. |

### Needs approval

1. **`legal-band` legal text — real AA failure.** `{colors.muted}` #7c828a at 13px
   on #ffffff is 3.88:1 against 4.5:1 required. Nearest passing value in the same
   grey family: **#6e737b** (4.51:1 on #ffffff; only 4.21:1 on #f7f7f7, so
   **#686d75** at 4.84:1 / 4.52:1 is safer if the token must also work on the soft
   band). Usage note that would make the real value defensible: none at 13px — the
   large-text exemption starts at 24px, or 18.66px at weight 700. Either the hex or
   the type size has to move, and both are brand decisions.
2. **`{colors.muted}` as general secondary text.** 3.88:1 / 3.62:1. Defensible
   unchanged only with the usage note "24px+, or 18.66px+ at weight 700, where 3:1
   applies". Below that, `{colors.body}` #5b616e (6.21:1 / 5.8:1) is already in the
   palette and should be the default secondary ink. Nearest passing replacement if
   the token itself must change: #6e737b (4.51:1).
3. **`{colors.semantic-up}` #05b169.** 2.8:1 on white — fails AA as text at every
   size, and the file mandates it as text colour only. Nearest passing green:
   **#047a49** (4.57:1 on #ffffff). Keeping the brand green requires a non-text
   role or the mandatory sign/arrow glyph the file now specifies.
4. **`{colors.focus}` reusing `{colors.primary}`.** Prescribed. The offset is what
   makes it work on blue CTAs; no single hex clears 3:1 against both #ffffff and
   #0052ff, so a distinct ring would mean a `focus` / `focus-on-accent` pair rather
   than one colour.
5. **`{colors.hairline-strong}` #767b85.** Prescribed, not extracted. Needs brand
   sign-off as the control-boundary grey.

### Identity verdict

Still unmistakably Coinbase. The additions are brand-derived, not generic: the
focus ring is Coinbase Blue plus an offset precisely because the file's own first
Don't forbids a second action colour; the motion section's distinctive rules —
numbers never tween, no ambience loop — are argued from display weight 400 and the
institutional-not-trading-floor voice, and would be wrong in most other files. The
states table keeps the brand's own asymmetry (price cells genuinely static, pill
CTAs fully stateful) instead of giving every component the full eight-state list.

**Profile: Calm is correct, used as assigned.** Rule 1 tempts via the full-bleed
dark heroes, but the tell for Cinematic is sparse type over photography with a slow
reveal; these heroes carry product-UI mockup cards plus a headline and two CTAs,
which is editorial layout, not cinema. Rule 2 does not apply — the Developer
Platform pricing page is one section of a marketing site, not a developer-tool
identity. Rule 3 is excluded by its own wording: the description says "editorial
calm", display weight is 400, the Don'ts forbid gradients and a second action
colour, and the only saturated tones (`semantic-up`, `semantic-down`,
`accent-yellow`) are documented as text-or-illustration only, never on interactive
elements. Everything else → Calm. No deviation from the Calm block.
