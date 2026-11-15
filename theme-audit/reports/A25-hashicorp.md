## A25 · hashicorp

Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

| Dimension | Before | After |
|---|---|---|
| tokens | 2 | 5 |
| refs | 5 | 5 |
| contrast | 2 | 5 |
| sections | 3 | 5 |
| motion | 1 | 5 |
| states | 1 | 5 |

Six contrast failures now sit in the disclosed column (frozen extracted values,
named with their measured ratios in `## Accessibility`); zero undisclosed.

### Findings

| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | A tokens | `focus` | No focus token existed. Confirmed. No single colour clears 3:1 against both the black canvas and the chromatic `product-card-*` grounds — brand blue `#2b89ff` sits at 1.03:1 on Boundary coral, 1.63:1 on Waypoint cyan. Required a two-tone ring. |
| P0 | F motion | whole file | No `motion:` group, no `## Motion & Animation`, no `prefers-reduced-motion`, zero durations, zero easings. Confirmed. |
| P0 | G accessibility | whole file | No `## Accessibility` section. Confirmed. |
| P0 | B contrast | `hairline` / `hairline-soft` | 1.94:1 and 1.42:1 on `canvas` (confirmed), and additionally 1.64:1 and 1.21:1 on the charcoal card surface. These are the only documented edge of `text-input`, a control boundary that needs 3:1. |
| P1 | A tokens | `surface`, `text-dim` | Both roles unresolved. `surface-1`…`surface-3` is a ladder, not a role name, and `ink-muted` does not satisfy `text-dim` under SPEC section 1 patterns. Confirmed. |
| P1 | B contrast | `ink-subtle` #656a76 | 3.88:1 on canvas, 3.28:1 on the card surface — below AA for normal text, and the file assigned it to "form helper text, timestamps, footnotes", i.e. 13–14px. Not flagged in the brief; found by the harness. |
| P1 | H states | all 13 component entries | Only `pressed` was documented anywhere structured. hover, focus-visible, active, disabled, loading, selected, error absent. Confirmed. |
| P1 | B contrast | `product-consul` + `ink` | White on Consul red is 4.44:1 — misses AA by 0.06. The harness does not check product tokens as surfaces, so this was invisible to it. |
| P1 | B contrast | `product-boundary` + `ink` | White on Boundary coral is 3.54:1. Same blind spot. `inverse-ink` on that ground reaches 5.93:1. |
| P2 | B contrast | `product-terraform-bright` | 3.59:1 on canvas, documented as "link emphasis" — large text only. |
| P2 | C elevation | Elevation table | Level 1 states a raw `rgba(178,182,189,0.1)` border with no token behind it; levels 2–3 use tokens. Inconsistent expression, though elevation itself is consistently border+surface and never shadow — which the file states explicitly. Left as-is: adding an rgba token would invent a value the prose already carries verbatim. |
| P2 | D typography | `{typography.caption}` | 13px at 500 weight carrying `footer` text in `ink-muted` (10.32:1, passes) — fine, but it was also the natural home for `ink-subtle`, which fails there. Noted in the Colors prose. |
| P2 | E ladders | `rounded.pill` / `rounded.full` | Two tokens, one value (9999px). Harmless duplication, both referenced in prose; left alone. |
| P2 | A tokens | `accent` role | Resolves to `primary` = `#000000` — the role is satisfied, but HashiCorp's real signal colour is the per-product set, which the file argues well in prose. No change made; renaming `primary` would break eight prose references. |

### Changes made

| Location in file | Before -> After | Why |
|---|---|---|
| frontmatter `colors` | added `surface-card: "#15181e"` | Satisfies the `surface` role. Alias of `surface-1`, same extracted hex — no new value invented. |
| frontmatter `colors` | added `text-dim: "#b2b6bd"` | Satisfies the `text-dim` role. Alias of `ink-muted`, same extracted hex. |
| frontmatter `colors` | added `hairline-strong: "#8a8f99"` | Parallel accessible boundary token per SPEC section 2. 6.47:1 on canvas, 5.48:1 on the card surface. Labelled prescribed. |
| frontmatter `colors` | added `focus: "#2b89ff"`, `focus-inset: "#000000"` | Two-tone focus ring. Blue is the brand's own link colour; the black inner band is the carrier over product-chromatic grounds. |
| frontmatter | added `motion:` group | SPEC section 4/5 Crisp block, verbatim. |
| `## Colors` → Surface | added `surface-card`, `hairline-strong` entries; scoped `hairline` and `hairline-soft` to decoration with their measured ratios | Tells the truth about the edge tokens instead of silently reusing them on controls. |
| `## Colors` → Text | added `text-dim`; annotated `ink-subtle` with 3.88:1 / 3.28:1 and a large-text-only scope | The failure is real and the file was assigning the token to small text. |
| `## Colors` | new `### Focus` subsection | Documents both ring bands and every measured ratio. |
| `## Components` → Inputs | focus ring was "1px `{colors.accent-blue}` outline" -> 2px `{colors.focus}` + 1px `{colors.focus-inset}`, offset 2px; resting border moved to `{colors.hairline-strong}` | A 1px ring on an untokenised colour is not a focus spec, and the input's edge must clear 3:1. |
| `## Components` | new `### States` table, 13 rows x 8 states | SPEC section 7. First line of the subsection says only the two extracted states were observed; the rest is prescribed. |
| after `## Components` | new `## Motion & Animation` | First line states the system is prescribed and unmeasured. Full interaction table plus the `prefers-reduced-motion` block. |
| after Motion | new `## Accessibility` | Measured key pairs, the real AA failures, per-surface ring visibility, tap target, reduced motion. |
| `## Do's and Don'ts` → Don't | 4 lines added (duration cap, no layout-property animation, no hairline as sole control edge, never suppress the ring) | Keeps the new rules enforceable in the brand's own voice. |
| `## Known Gaps` | 6 lines added | Every prescribed value labelled; tap-target and state claims marked unverifiable. |

### Contrast checks

All computed with WCAG 2.1 relative luminance via `python3`, not estimated.

| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| ink #ffffff / canvas #000000 | 21.0:1 | 4.5:1 | Pass |
| ink #ffffff / surface-card #15181e | 17.78:1 | 4.5:1 | Pass |
| text-dim (= ink-muted) #b2b6bd / canvas | 10.32:1 | 4.5:1 | Pass |
| text-dim / surface-card | 8.74:1 | 4.5:1 | Pass |
| ink-subtle #656a76 / canvas | 3.88:1 | 4.5:1 | **Fail** (disclosed; 3:1 met, large text only) |
| ink-subtle / surface-card | 3.28:1 | 4.5:1 | **Fail** (disclosed) |
| on-primary #ffffff / primary #000000 | 21.0:1 | 4.5:1 | Pass |
| accent-blue #2b89ff / canvas | 6.12:1 | 4.5:1 | Pass |
| hairline #3b3d45 / canvas | 1.94:1 | 3.0:1 | **Fail** (disclosed, scoped decorative) |
| hairline / surface-card | 1.64:1 | 3.0:1 | **Fail** (disclosed) |
| hairline-soft #252830 / canvas | 1.42:1 | 3.0:1 | **Fail** (disclosed) |
| hairline-soft / surface-card | 1.21:1 | 3.0:1 | **Fail** (disclosed) |
| hairline-strong #8a8f99 / canvas | 6.47:1 | 3.0:1 | Pass (prescribed) |
| hairline-strong / surface-card | 5.48:1 | 3.0:1 | Pass (prescribed) |
| hairline-strong / surface-2 #1f232b | 4.85:1 | 3.0:1 | Pass |
| hairline-strong / surface-3 #3b3d45 | 3.34:1 | 3.0:1 | Pass |
| focus #2b89ff / canvas | 6.12:1 | 3.0:1 | Pass |
| focus / surface-1 | 5.19:1 | 3.0:1 | Pass |
| focus / surface-2 | 4.59:1 | 3.0:1 | Pass |
| focus / surface-3 | 3.16:1 | 3.0:1 | Pass (at the floor) |
| focus / inverse-canvas #ffffff | 3.43:1 | 3.0:1 | Pass |
| focus-inset #000000 / focus #2b89ff (band separation) | 6.12:1 | 3.0:1 | Pass |
| focus-inset / product-terraform #7b42bc | 3.35:1 | 3.0:1 | Pass |
| focus-inset / product-terraform-bright | 3.59:1 | 3.0:1 | Pass |
| focus-inset / product-vault #ffcf25 | 14.2:1 | 3.0:1 | Pass |
| focus-inset / product-consul #e62b1e | 4.73:1 | 3.0:1 | Pass |
| focus-inset / product-waypoint #14c6cb | 9.97:1 | 3.0:1 | Pass |
| focus-inset / product-waypoint-deep | 8.43:1 | 3.0:1 | Pass |
| focus-inset / product-vagrant #1868f2 | 4.3:1 | 3.0:1 | Pass |
| focus-inset / product-nomad #00ca8e | 9.84:1 | 3.0:1 | Pass |
| focus-inset / product-boundary #f24c53 | 5.93:1 | 3.0:1 | Pass |
| ink / product-terraform | 6.27:1 | 4.5:1 | Pass |
| inverse-ink / product-vault | 14.2:1 | 4.5:1 | Pass |
| inverse-ink / product-waypoint | 9.97:1 | 4.5:1 | Pass |
| ink / product-consul | 4.44:1 | 4.5:1 | **Fail** by 0.06 (disclosed) |
| ink / product-vagrant | 4.88:1 | 4.5:1 | Pass |
| inverse-ink / product-nomad | 9.84:1 | 4.5:1 | Pass |
| ink / product-boundary | 3.54:1 | 4.5:1 | **Fail** (disclosed, large text only) |
| product-terraform-bright / canvas | 3.59:1 | 4.5:1 | **Fail** (disclosed, large text / non-text) |
| semantic-success #00ca8e / canvas | 9.84:1 | 4.5:1 | Pass |
| semantic-warning #ffcf25 / canvas | 14.2:1 | 4.5:1 | Pass |
| semantic-error #e62b1e / canvas | 4.73:1 | 4.5:1 | Pass |
| semantic-visited #a737ff / canvas | 4.63:1 | 4.5:1 | Pass |
| amber-200 #bb5a00 / canvas | 4.58:1 | 4.5:1 | Pass |
| amber-100 #fbeabf / canvas | 17.62:1 | 4.5:1 | Pass |
| blue-7 #101a59 / canvas | 1.31:1 | n/a | Gradient stop, no threshold |

### Motion inventory

Profile: **Crisp** (SPEC section 5 block used verbatim). Prescribed, not measured.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 100ms | `{motion.ease-standard}` | opacity, transform (no card travel) | Instant colour/opacity, no transform |
| Press / active | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | opacity, `scale(0.99)` | Opacity only at 100ms, scale removed |
| Focus ring appear | `{motion.duration-instant}` 60ms | `{motion.ease-standard}` | opacity | No transition at all |
| Page / route transition | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | opacity | Cross-fade at 100ms |
| Modal / drawer enter | `{motion.duration-base}` 150ms | `{motion.ease-enter}` | opacity, `translateY(8px → 0)` | Opacity at 100ms, translate removed |
| Modal / drawer exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | opacity, transform | Opacity at 100ms |
| Dropdown / mega-menu | 100ms enter / 60ms exit | `ease-enter` / `ease-exit` | opacity, `translateY(4px → 0)` | Opacity only at 100ms |
| Toast | 150ms enter / 100ms exit | `ease-enter` / `ease-exit` | opacity, `translateY(8px → 0)` | Opacity only at 100ms, timer unchanged |
| List enter | 150ms per item, `{motion.stagger-step}` 20ms between | `{motion.ease-enter}` | opacity, `translateY(6px → 0)` | All items fade together at 100ms, no stagger |
| List exit | `{motion.duration-fast}` 100ms | `{motion.ease-exit}` | opacity, transform | Opacity only at 100ms, no stagger |
| Loading | `{motion.duration-emphasis}` 300ms loop | `{motion.ease-standard}` | opacity, `translateX` sweep | Loop frozen, static skeleton + `aria-busy` |

Every exit is shorter than its entrance. No layout-triggering property appears.
The loading sweep is the only infinite animation; no brand ambience is claimed.

### Shared issues (not fixed)

| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` line ~22 (`REQUIRED_COLOR_ROLES["surface"]`) | The `surface` pattern list enumerates suffixes (`card|soft|raised|…`) but not numeric ladders, so the very common `surface-1` / `surface-2` / `surface-3` convention resolves to no surface at all. This file had three surfaces and still scored `roles_missing: surface`, which pushes agents toward alias tokens that add nothing. | Add `r"^surface-\d+$"` to the `surface` pattern list, ranked after the named variants so the representative token stays canonical. |
| `theme-audit/audit.py` line ~26 (`REQUIRED_COLOR_ROLES["text-dim"]`) | `ink-` is accepted for `text`, so `ink-muted` and `ink-subtle` both land in `text` at 4.5:1, while `text-dim` resolves to nothing. A brand that names its ink ladder `ink-*` cannot satisfy `text-dim` without an alias. | Add `r"^ink-(muted|soft|secondary|dim)$"` to `text-dim`, and exclude those keys from the `text` role's `^ink-` pattern so a muted ink is judged once, in the right role. |
| `theme-audit/audit.py` line ~292 (`surface_keys`) | The focus check treats only `canvas|background|bg|base|surface|card|panel` prefixes as surfaces. A file whose signature surfaces are `product-*` chromatic cards — exactly this one — gets a passing focus score from a ring that measures 1.03:1 on one of its real grounds. | Also include any `colors:` key referenced as a `backgroundColor` in the `components:` block; that is where a file declares what is actually a surface. |
| `theme-audit/SPEC.md` section 2 table | The six listed pairs omit `text` on `accent` and `on-accent` on each signal fill, so a multi-accent brand's worst text pairing (here `ink` on `product-consul`, 4.44:1) is only caught by hand. | Add a row: every `on-*` ink against every signal fill it is paired with in `components:`, at 4.5:1. |

### Needs approval

Nothing in the file was changed to make a ratio pass. Four real brand values
fail AA and remain as extracted, disclosed with their measured ratios. Each
needs a product decision:

1. **`ink-subtle` #656a76** — 3.88:1 on canvas, 3.28:1 on charcoal, required 4.5:1.
   Nearest passing value on canvas: **#7d828e** (5.46:1 on canvas, 4.62:1 on
   surface-card). Usage note that makes the real value defensible: it clears 3:1
   on both surfaces, so it is valid for 24px+ text or 18.66px+ at weight 700
   only — not for the 13–14px helper text and timestamps the file currently
   assigns it to.
2. **`hairline` #3b3d45 / `hairline-soft` #252830** — 1.94:1 and 1.42:1 on
   canvas, required 3.0:1. Nearest passing value: **#8a8f99** (6.47:1), added as
   the prescribed `hairline-strong`. Usage note: the extracted hairlines are
   valid as decoration (card texture, table row rules) where the boundary is not
   the only way to perceive the element; 1.4.11 does not apply to purely
   decorative edges. They are not valid as the sole edge of `text-input`.
3. **`ink` on `product-consul`** — 4.44:1, required 4.5:1, short by 0.06.
   Nearest passing value: use the existing `inverse-ink` #000000 (4.73:1), or
   darken the red to **#d9271a** (4.61:1 with white). Usage note: white on
   Consul red is valid at 24px+ display sizes, where 3:1 applies.
4. **`ink` on `product-boundary`** — 3.54:1, required 4.5:1. Nearest passing
   value: use the existing `inverse-ink` #000000 (5.93:1), or darken coral to
   **#c62f36** (4.59:1 with white). Usage note: white on Boundary coral is
   valid for 24px+ display type only.

Also for approval, as prescribed rather than extracted:

5. **The focus ring is two-tone** (`focus` #2b89ff + 1px `focus-inset` #000000)
   rather than a `focus` / `focus-on-dark` pair. Justification: the ring must
   appear over a black canvas, three charcoals, a white button and eight
   chromatic product grounds. No single colour clears 3:1 across that set —
   the best achromatic mid-tone tried, #8a8f99, sits at 1.38:1 on Vault yellow.
   SPEC section 1 sanctions a two-tone ring for grounds with no measurable
   colour; this applies the same device to grounds whose colour varies by product.
6. **`surface-card` and `text-dim` are pure aliases.** They add no hex. If the
   repo would rather rename `surface-1` → `surface-card` and `ink-muted` →
   `text-dim` across all prose, say so — that is a larger diff and it loses the
   ladder naming the Elevation section depends on, so it was not done here.

### Identity verdict

Still unmistakably HashiCorp. The per-product accent system is untouched and is
now load-bearing in two more places: the focus ring's inner band exists
*because* the product grounds are chromatic, and the States table routes each
`button-product-*` hover to its own deep variant rather than to a generic
hover token. The one risk was the States table turning into a generic token
dump; it is anchored instead to the file's own surface-lift ladder
(canvas → surface-1 → surface-2 → surface-3) and never introduces a shadow,
which the Don'ts forbid.

The assigned **Crisp** profile is right, and not only by SPEC rule 2's
infra/developer-tool clause. The file's own evidence agrees: it argues twice
that the 8px CTA corner exists to read "developer-tool rather than
consumer-app", its weight range is a deliberately narrow 500/600/700, and it
documents no gradient reveal, no parallax and no shadow. The one pull toward
Cinematic — hero 3D product visuals — is explicitly described as static right-
column illustration, not full-bleed photography, so it does not meet rule 1.
Playful is ruled out despite nine saturated hexes: the saturation is identity
signalling on card grounds, and the Don'ts forbid mixing product accents in a
viewport, which is the opposite of a playful palette's behaviour. No profile
switch made.

Two things in the file read as borrowed from nothing — the eyebrow-above-every-
section rule and the "don't mix two product accents in one viewport" rule are
both specific enough that no other file in the collection could carry them.
That is the identity test passing.
