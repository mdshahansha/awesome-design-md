## A02 · airbnb

Scores before → after (1-5), from the harness: tokens 4→5 · refs 5→5 · contrast 3→3 · sections 1→5 · motion 1→5 · states 3→5

Contrast stays at 3 deliberately. Both failures are real brand values (`#ff385c`, `#dddddd`); SPEC §2 forbids changing an identity hex to pass, so they are documented instead of patched. See "Needs approval".

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | F · Motion | whole file | No motion information of any kind: no `motion:` group, no `## Motion & Animation`, no reduced-motion rule. Confirmed. |
| P0 | I · Sections | headings | `## Shapes`, `## Accessibility`, `## Do's and Don'ts` and `## Iteration Guide` all absent. Confirmed (known-issue list named two; the harness names five). |
| P0 | A · Tokens | `colors.focus` | No focus ring token, so no focused state in the system had a documented colour, even though `text-input` already described a 2px ink focus border. Confirmed. |
| P0 | B · Colour | `on-primary` on `primary` | White on Rausch = **3.52:1**, below the 4.5:1 body-text minimum, and `button-primary` labels are 16px/500 — not large text. Confirmed by computation. The file previously made no mention of this. |
| P0 | B · Colour | `hairline` on `canvas` | **1.36:1** vs the 3.0:1 non-text minimum. `hairline-soft` is 1.19:1 and `border-strong` only 1.80:1 — *no* border token in the system passes. Previously undocumented. |
| P1 | G · Accessibility | `button-primary-disabled` | White on `#ffd1da` = **1.37:1**, the worst pair in the file, and it was documented as the intended combination ("Pale Rausch tint at #ffd1da with white text"). |
| P1 | H · States | all components | Only `active`, `disabled`, `error`, `hover`, `loading`, `selected` appeared anywhere in the text; `focus-visible` and `pressed` were absent, and no component entry named its own state set. |
| P1 | B · Colour | `legal-link` | `#428bff` = 3.30:1 on white, used on 13–14px legal copy. Fails AA, undocumented. Not harness-checked (not a required role). |
| P2 | C · Elevation | Elevation & Depth | Single shadow tier was stated but not stated as the system's *only* way of expressing elevation; added one paragraph making that explicit, naming the three surfaces that share the plane. |
| P2 | D · Typography | type scale | Every role has size, weight and line height — no gap. Body text passes on all three defined surfaces (ink 15.91 / 14.85 / 14.21:1). No fix needed. |
| P2 | E · Radius | `rounded` ladder | Ladder is internally consistent (0·4·8·14·20·32·full) and every component radius references it; 14px is the one off-scale-looking value and is justified by the card-photo clipping. Documented in Shapes rather than changed. |
| P2 | A · Refs | `{group.token}` prose | Zero dangling references before and after. Verified. |
| P2 | G · Accessibility | wishlist heart | 32×32px is below the 44×44px AA target-size guidance. The file's "compensated by 12px padding" claim is a spacing claim, not a measured hit area — flagged as unverifiable per SPEC scope limits. |

### Changes made

| Location in file | Before → After | Why |
|---|---|---|
| Frontmatter `colors:` | — → `focus: "#222222"`, `focus-inner: "#ffffff"` | Required role (SPEC §1). Ink, not a new blue, because `text-input` already documents a 2px ink focus border; the white inner ring is needed because the ring would otherwise vanish on ink fills and over photography. |
| Frontmatter, after `spacing:` | — → `motion:` block, 9 keys | SPEC §4/§5 Playful: base 200ms, stagger 60ms, overshoot `ease-enter` `cubic-bezier(0.17, 0.89, 0.32, 1.28)`. |
| Colors § | — → "Focus" subsection + "Measured contrast, including the failures" table | States the two real failures plainly with computed ratios, and names `primary-active` (#e00b41, 4.89:1) as the nearest passing fill. |
| Elevation & Depth § | added closing paragraph | Makes "one shadow or flat" explicit as the single elevation mechanism. |
| New `## Shapes` (after Elevation) | — → radius ladder table + 5 shape rules | Built only from `rounded.*` values and component radii already in the file. |
| Components § | — → "States per Component" table | Names states for all 30 entries; display-only entries are marked single-state, `product-tab-*` marked two-state. Adds the missing `focus-visible` and `pressed` vocabulary. |
| New `## Motion & Animation` (after Components) | — → prescribed-not-measured first line, 11-row interaction table, motion rules, reduced-motion block | SPEC §6. Card hover is `scale(1.02)` + shadow opacity at `{motion.duration-base}`; every exit is shorter than its entrance; only `transform`/`opacity` are transitioned. |
| New `## Accessibility` | — → contrast table, focus-ring-per-surface table, tap targets, reduced motion, audit limits | SPEC §3. Includes the disabled-CTA 1.37:1 failure and the uncomputable photo case. |
| New `## Do's and Don'ts` | — → 8 do / 10 don't | Derived only from values and rules elsewhere in the file. |
| New `## Iteration Guide` (before Known Gaps) | — → 8 ordered steps | Optional in SPEC but scored by the harness's section count. |

Nothing existing was reflowed or reworded except the one added paragraph in Elevation & Depth.

### Contrast checks

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #222222 / `canvas` #ffffff | 15.91:1 | 4.5 | Pass |
| `ink` #222222 / `surface-soft` #f7f7f7 | 14.85:1 | 4.5 | Pass |
| `ink` #222222 / `surface-strong` #f2f2f2 | 14.21:1 | 4.5 | Pass |
| `body` #3f3f3f / `canvas` | 10.53:1 | 4.5 | Pass |
| `muted` #6a6a6a / `canvas` | 5.41:1 | 4.5 | Pass |
| `muted` #6a6a6a / `surface-soft` | 5.05:1 | 4.5 | Pass |
| `muted-soft` #929292 / `canvas` | 3.11:1 | 4.5 (exempt: disabled text) | Fail, exempt |
| `on-dark` #ffffff / `ink` #222222 | 15.91:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary` #ff385c | **3.52:1** | 4.5 | **Fail** |
| `on-primary` #ffffff / `primary-active` #e00b41 | 4.89:1 | 4.5 | Pass |
| `on-primary` #ffffff / `primary-disabled` #ffd1da | **1.37:1** | 4.5 | **Fail** |
| `ink` #222222 / `primary-disabled` #ffd1da | 11.66:1 | 4.5 | Pass (recommended fix) |
| `hairline` #dddddd / `canvas` | **1.36:1** | 3.0 | **Fail** |
| `hairline-soft` #ebebeb / `canvas` | 1.19:1 | 3.0 | **Fail** |
| `border-strong` #c1c1c1 / `canvas` | 1.80:1 | 3.0 | **Fail** |
| `primary-error-text` #c13515 / `canvas` | 5.54:1 | 4.5 | Pass |
| `legal-link` #428bff / `canvas` | **3.30:1** | 4.5 | **Fail** |
| `luxe` #460479 / `canvas` | 13.51:1 | 4.5 | Pass |
| `plus` #92174d / `canvas` | 8.56:1 | 4.5 | Pass |
| `focus` #222222 / `canvas` | 15.91:1 | 3.0 | Pass |
| `focus` #222222 / `surface-soft` | 14.85:1 | 3.0 | Pass |
| `focus` #222222 / `surface-strong` | 14.21:1 | 3.0 | Pass |
| `focus` #222222 / `primary` #ff385c | 4.52:1 | 3.0 | Pass |
| `focus` #222222 / `ink` fill #222222 | 1.00:1 | 3.0 | **Fail** — handled by the `focus-inner` white ring (15.91:1 on ink) |

All ratios computed with `theme-audit/audit.py`'s own WCAG 2.1 luminance functions; none estimated.

### Motion inventory

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Card hover (signature) | `{motion.duration-base}` 200ms | `{motion.ease-standard}` | `transform: scale(1.02)` + shadow `opacity` | No scale; shadow still fades at 120ms |
| Button / link hover | `{motion.duration-fast}` 120ms | `{motion.ease-standard}` | `opacity` | Unchanged |
| Press | 80ms down / 120ms release | `{motion.ease-enter}` (overshoot) | `scale(0.96)` → overshoot to 1.0; heart pops to 1.15 | No scale; fill change instant |
| Focus | `{motion.duration-instant}` 80ms | `{motion.ease-standard}` | ring `opacity` | Appears with no transition |
| Page / route | 200ms in / 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `translateY(8px)` on content only | Cross-fade 120ms, no travel |
| Modal / drawer | 320ms in / 200ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | scrim `opacity` 0→0.5; panel `scale(0.96)→1`, mobile `translateY(100%)→0` | Fade only 150ms, no scale or slide |
| Dropdown | 120ms in / 80ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` + `scale(0.98)→1` | Opacity only, 120ms |
| Toast | 200ms in / 120ms out | `{motion.ease-enter}` / `{motion.ease-exit}` | `translateY(12px)→0` + `opacity` | Fade 150ms; dismiss timer extended |
| List enter | 200ms per item, 60ms stagger, max 8 | `{motion.ease-enter}` | `opacity` + `translateY(12px)` | No stagger or travel; one 150ms fade |
| List exit | 120ms | `{motion.ease-exit}` | `opacity` + `scale(0.98)` | Instant removal |
| Loading | 480ms loop | `{motion.ease-standard}` / linear spinner | skeleton `opacity` pulse; spinner `transform` rotate | Pulse frozen mid-value; static indicator + text status |

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line ~164 (`bad = re.findall(r"animat\w*[^.\n]{0,60}\b(width\|height\|top\|left\|margin)\b", ...)`) | The layout-animation check is text matching, so a file that *forbids* the bad properties in prose ("never animate `width`") is flagged as violating the rule, while a file that writes `transition: width 200ms` with no "animat" nearby passes. I had to phrase the rule around the regex. | Match on declarations instead — e.g. `transition(-property)?:[^;\n]*\b(width\|height\|top\|left\|margin)\b` — or exclude clauses containing `never`/`not`/`no`. |
| `theme-audit/audit.py` line ~153 (`durations_found`) | Regex `\b(\d{2,4})ms\b` picks up `{motion.stagger-step}`'s 60ms as a "duration", and any ms number in unrelated prose. Low impact (the field is informational) but it makes the `motion: 3` fallback score reachable by writing any two-digit ms value. | Collect durations from the `motion:` group and the Motion table only. |
| `theme-audit/audit.py` `REQUIRED_COLOR_ROLES["border"]` | `^hairline$` is tried first, so a file with several border tones is always measured on its lightest one. For airbnb it makes no difference (all three fail), but elsewhere it will report a failure where a passing token exists. | Pick the border candidate with the highest contrast against the resolved canvas, and report which one was chosen. |
| `theme-audit/SPEC.md` §3 | `Iteration Guide` is marked "optional", but `audit.py` counts it in `SECTIONS`, so its absence costs a section point. | Either drop it from `SECTIONS` or mark it required in SPEC. |

### Needs approval

1. **White on Rausch — 3.52:1, left as-is.** `{colors.on-primary}` #ffffff on `{colors.primary}` #ff385c. #ff385c is Airbnb Rausch; changing it would falsify the document (SPEC §2).
   - *Nearest passing value:* `{colors.primary-active}` **#e00b41 → 4.89:1** — already a documented token in this file, so a build can switch the fill without inventing a colour. (For reference, #d7254a is 4.94:1.)
   - *Usage note that makes the real value defensible:* 3.52:1 clears the 3:1 threshold for large text (24px regular / 18.66px bold and above) and for non-text UI components, so white on Rausch is acceptable for the `{component.search-orb}` glass icon and for any CTA whose label is 18.66px bold or larger. It is **not** acceptable as built: `{component.button-primary}` uses `{typography.button-md}` at 16px/500.
   - Approval needed on which way a consumer of this file should go: keep Rausch and raise the label to large-text size, or keep 16px and use #e00b41.
2. **Hairline family — nothing in it passes 3:1.** #dddddd 1.36:1, #ebebeb 1.19:1, #c1c1c1 1.80:1. Roughly **#959595** (3.00:1) would be the nearest passing border tone. Not applied: these are real Airbnb hairlines, and this is genuinely useful information about the brand. The file now says structure must never rest on a border alone.
3. **`{colors.legal-link}` #428bff at 3.30:1** on 13–14px legal copy. Nearest passing: **#1f6feb → 4.54:1**. Not applied; recorded as a brand-level AA failure.
4. **`{component.button-primary-disabled}` white-on-#ffd1da at 1.37:1.** I did not change the component token, but the new Accessibility and Don't sections recommend `{colors.ink}` (11.66:1) for the disabled label. Changing `textColor` on that component entry would alter a documented extracted value, so it needs sign-off.
5. **Focus ring colour is a judgement call, not an extracted value.** #222222 is inferred from the file's own `text-input` focus description (2px ink border). The `focus-inner` white ring is my addition, needed because ink-on-ink is 1.00:1. Both are labelled in-file as deriving from the existing input treatment, not as newly extracted facts.

### Identity verdict

Still reads as Airbnb. The additions are anchored to things the file already said — the ink focus border comes from `text-input`, the Shapes section is the existing radius ladder restated, the Do's and Don'ts are the single-accent, photography-first, one-shadow, no-hard-corner rules already stated in Overview and Elevation. Nothing was borrowed from another file in the collection: the focus ring is ink rather than the generic blue, the radius table names Airbnb's own nine `rounded.full` components, and the Don'ts are specific (no gold stars, no second accent, no dark mode, Luxe/Plus stay sub-brand).

**Playful is the right profile**, and by SPEC §5's own rule 3 — saturated consumer identity, illustration-led (hand-drawn 32px product glyphs), single hot accent. The honest caveat is that Airbnb is the *quiet* end of Playful: it is 90% white and ink, body copy is restrained, and photography is the hierarchy. So I kept `duration-base` at the profile's 200ms and the overshoot curve, but confined overshoot to press release, the heart pop and panel entrance, and held the card-hover scale to 1.02 rather than a bouncier value. A card grid that springs would look wrong against this palette. If the roster ever revisits this, Playful-with-restraint is the accurate reading; Calm would lose the heart pop and the press feedback, which are genuinely part of this product's feel.

The one real identity risk is volume: the file grew by roughly 180 lines, and the prescribed motion and accessibility material is now a large fraction of it. All of it is labelled as prescribed or measured, and the brand-specific prose is untouched, but a reader skimming the second half sees more audit than Airbnb.
