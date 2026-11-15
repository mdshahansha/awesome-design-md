## A60 · runwayml
Scores before -> after (1-5), from the harness: tokens 1 -> 3 · refs 1 -> 5 · contrast 1 -> 5 · sections 1 -> 5 · motion 1 -> 5 · states 1 -> 1

Before: no frontmatter at all, numbered legacy headings, 0 of 12 required sections, 8 of 8 colour roles missing, no motion group, no state named anywhere.
After: full token block built only from the file's own prose, 12 of 12 sections, 0 dangling refs, 0 undisclosed contrast failures (10 disclosed), Cinematic motion group verbatim. `accent` and `on-accent` are deliberately left unfilled, and states stay at 1 because the source documents one interaction state in total.

### Findings
| Severity | Dimension | Element | Issue |
|---|---|---|---|
| P0 | J Format | whole file | Legacy format: no frontmatter token block, numbered headings (`## 1. Visual Theme & Atmosphere` … `## 9. Agent Prompt Guide`). Nothing was machine-readable. |
| P0 | C Sections | Motion & Animation, Accessibility | Both absent, as in all 84 files. |
| P0 | F Motion | whole file | No duration, easing, transition or scroll value stated anywhere in the prose. Entire motion system had to be prescribed. |
| P0 | H States | Components | The source documents exactly one interaction state in the whole file — the navigation hover. Pressed, disabled, loading, selected and error appear nowhere, for any component, and the palette holds no error/success/warning tone to express them. |
| P0 | A Tokens | `accent`, `on-accent` | Genuinely absent from the brand, not misnamed: the source says the interface is "intentionally colorless", that all colour comes from photography, and forbids adding decorative colour. Left unfilled; 2 points accepted as lost rather than aliasing `accent` onto the white ink. |
| P1 | A Tokens | `focus` | No focus treatment extracted. Prescribed as `#767d88` — Cool Slate, a tone the palette already owns — rather than introducing a chromatic ring into a palette whose first rule is that it has no accent colour. Clears 3:1 on all six surfaces (worst case 3.51:1). |
| P1 | B Colour | `text-secondary` #767d88 | Cool Slate is the brand's documented secondary text colour and was chosen against the black canvas (5.06:1). It misses AA on `surface-dark` (4.19:1) and on both light surfaces (4.12:1 / 3.51:1) — and the source's own example prompt puts it on light research sections. Real brand failure, disclosed. |
| P1 | B Colour | `ink-secondary-alt` #3f3f3f | The source calls Near Charcoal "a slightly lighter variant for dark-section secondary text". On the dark sections it measures 1.99:1 and 1.65:1 — invisible. The source's own stated usage is unusable. Disclosed. |
| P1 | B Colour | `text-soft` #6b7280 | Tailwind Gray misses AA on the canvas by a hair (4.34:1) and clearly on the dark card (3.60:1). Disclosed; defensible only at large-text sizes or on the light surfaces (4.83:1 on white). |
| P1 | E Borders | `border-dark`, `border-light-cool`, `border-light-silver` | All three documented hairlines sit far below 3:1 against the grounds they are drawn on (1.41 / 1.17 / 1.60 / 1.48 / 1.36). This is the source's own "barely visible containment", so all three are frozen and scoped to decoration. **No parallel accessible token was added**: the palette already owns `text-secondary` #767d88, which clears 3:1 against all six surfaces, so it does the boundary work and nothing new was invented. |
| P1 | D Typography | `section-heading`, `body`, `small` | Line-height and letter-spacing are stated as ranges in the source (1.00–1.10, -1px to 0px, -0.16px to -0.26px) and are recorded as ranges rather than resolved to one value. Flagged in Known Gaps, not invented. |
| P2 | A Tokens | buttons | The source hedges its own extraction: "Background: likely transparent or dark". Both readings recorded (`button-link`, `button-dark`); no padding or height stated anywhere. |
| P2 | C Elevation | canvas vs surface-dark | The layers are, by design, barely distinguishable (1.21:1), and `canvas-deep` vs `canvas` is 1.02:1. Not a defect — stated as a measured layer fact in Elevation & Depth. Elevation is expressed one way (change of ground), with Level 1's border scoped to alert containers. |
| P2 | G A11y | tap targets | The source gives font sizes and "adequate padding" but no pixel height for any control, so the 44×44px minimum can be neither confirmed nor failed from this document. Recorded as a gap. |
| P2 | C Sections | Border Radius Scale | Lived as a Layout subsection; moved verbatim into the required `## Shapes` section rather than duplicated. |
| P2 | C Sections | Agent Prompt Guide | Legacy section with no slot in the contract. Kept verbatim as an unnumbered section after Known Gaps, including its nested `### Iteration Guide`. |

### Changes made
| Location in file | Before -> After | Why |
|---|---|---|
| Frontmatter | none -> `colors` (18), `typography` (9), `spacing` (12), `rounded` (4), `motion` (10), `components` (16) | SPEC §1. Every value read from the prose: the 17 hexes of section 2, the 9 rows of the type table, the 12-step spacing scale, the 4-step radius ladder, and the component descriptions of section 4. |
| Frontmatter `colors` | — -> `accent` and `on-accent` omitted | Genuinely absent from the brand (SPEC §1). Known Gaps carries the evidence. |
| Frontmatter `colors.focus` | — -> `"#767d88"` | SPEC §1 focus exception. Reuses Cool Slate; no new brand colour. |
| Frontmatter | — -> no `shadow:` group | SPEC §1: required only where the prose documents real shadow values. Runway documents zero shadows, and nothing references a shadow token. |
| Headings `## 1.`–`## 9.` | numbered -> unnumbered contract names, reordered to SPEC §3 order | Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Motion & Animation, Accessibility, Do's and Don'ts, Responsive Behavior, Known Gaps, then Agent Prompt Guide. |
| Layout -> Shapes | `### Border Radius Scale` moved verbatim | Shapes is required; the content already existed in Layout. Moved, not duplicated. |
| Colors | flat hex list -> same list with `{colors.*}` refs, plus `### Borders`, `### Accent`, `### Focus` | Makes the extracted values addressable and states the boundary/accent/ring decisions where a reader looks for them. |
| Components | prose only -> each entry names its states | hover where documented, focus-visible labelled prescribed, everything else "not documented on the live site"; static elements say "default state only". |
| Motion & Animation | absent -> new section after Components | First line states it is prescribed and not measured. 12-row interaction table, reduced-motion CSS block, transform/opacity only. |
| Accessibility | absent -> new section | 27 measured key pairs, 11 component pairs, ring visibility on all six surfaces, tap-target and reduced-motion notes. |
| Known Gaps | absent -> new section | 11 entries: absent accent, absent states, absent focus, hedged button fill, no tap-target sizes, no shadows, no motion, unquantified overlays, range-valued type, near-duplicate tones kept as extracted, unstated neutral polarity. |
| Do's and Don'ts | 9 + 9 -> 10 + 11 bullets | Added the boundary rule, the Cool-Slate-on-cards prohibition and the layout-property animation prohibition. Existing bullets kept verbatim with token refs. |

### Contrast checks
| Foreground / Background | Ratio | Required | Pass/Fail |
|---|---|---|---|
| `ink` #ffffff / `canvas` #000000 | 21.00:1 | 4.5:1 | Pass |
| `ink` #ffffff / `canvas-deep` #030303 | 20.62:1 | 4.5:1 | Pass |
| `ink` #ffffff / `surface-dark` #1a1a1a | 17.40:1 | 4.5:1 | Pass |
| `muted` #a7a7a7 / `canvas` | 8.73:1 | 4.5:1 | Pass |
| `muted` #a7a7a7 / `surface-dark` | 7.23:1 | 4.5:1 | Pass |
| `muted-footer` #999999 / `canvas` | 7.37:1 | 4.5:1 | Pass |
| `muted-footer` #999999 / `surface-dark` | 6.11:1 | 4.5:1 | Pass |
| `text-tertiary` #7d848e / `canvas` | 5.56:1 | 4.5:1 | Pass |
| `text-tertiary` #7d848e / `surface-dark` | 4.61:1 | 4.5:1 | Pass (thin margin) |
| `text-secondary` #767d88 / `canvas` | 5.06:1 | 4.5:1 | Pass |
| `text-secondary` #767d88 / `surface-dark` | 4.19:1 | 4.5:1 | **Fail — disclosed** |
| `text-secondary` #767d88 / `surface-light` #fefefe | 4.12:1 | 4.5:1 | **Fail — disclosed** |
| `text-secondary` #767d88 / `surface-light-cool` #e9ecf2 | 3.51:1 | 4.5:1 | **Fail — disclosed** |
| `text-soft` #6b7280 / `canvas` | 4.34:1 | 4.5:1 | **Fail — disclosed** |
| `text-soft` #6b7280 / `surface-dark` | 3.60:1 | 4.5:1 | **Fail — disclosed** |
| `ink-secondary-alt` #3f3f3f / `canvas` | 1.99:1 | 4.5:1 | **Fail — disclosed** |
| `ink-secondary-alt` #3f3f3f / `surface-dark` | 1.65:1 | 4.5:1 | **Fail — disclosed** |
| `on-light` #404040 / `surface-light` | 10.28:1 | 4.5:1 | Pass |
| `on-light` #404040 / `surface-light-cool` | 8.76:1 | 4.5:1 | Pass |
| `link-on-light` #0c0c0c / `surface-light` | 19.40:1 | 4.5:1 | Pass |
| `link-on-light` #0c0c0c / `surface-light-cool` | 16.53:1 | 4.5:1 | Pass |
| `border-dark` #27272a / `canvas` | 1.41:1 | 3:1 | **Fail — frozen decoration, disclosed** |
| `border-dark` #27272a / `surface-dark` | 1.17:1 | 3:1 | **Fail — frozen decoration, disclosed** |
| `border-light-cool` #c9ccd1 / `surface-light` | 1.60:1 | 3:1 | **Fail — frozen decoration, disclosed** |
| `border-light-cool` #c9ccd1 / `surface-light-cool` | 1.36:1 | 3:1 | **Fail — frozen decoration, disclosed** (the pair `card-light` actually binds) |
| `border-light-silver` #d0d4d4 / `surface-light` | 1.48:1 | 3:1 | **Fail — frozen decoration, disclosed** |
| `text-secondary` as boundary / `canvas` | 5.06:1 | 3:1 | Pass — the perceivable boundary, no new token |
| `text-secondary` as boundary / `surface-light-cool` | 3.51:1 | 3:1 | Pass — worst case of six surfaces |
| `focus` #767d88 / `canvas` | 5.06:1 | 3:1 | Pass |
| `focus` #767d88 / `canvas-deep` | 4.97:1 | 3:1 | Pass |
| `focus` #767d88 / `surface-dark` | 4.19:1 | 3:1 | Pass |
| `focus` #767d88 / `surface-light` | 4.12:1 | 3:1 | Pass |
| `focus` #767d88 / `ink` #ffffff | 4.15:1 | 3:1 | Pass |
| `focus` #767d88 / `surface-light-cool` | 3.51:1 | 3:1 | Pass |
| `surface-dark` / `canvas` (layer separation) | 1.21:1 | — | Not a WCAG pair; by design |
| `canvas-deep` / `canvas` (layer separation) | 1.02:1 | — | "Near-imperceptible", per the source |
| `card-light` — #404040 on #e9ecf2 | 8.76:1 | 3:1 (24px) | Pass |
| `article-card-light` — #404040 on #fefefe | 10.28:1 | 3:1 (24px) | Pass |
| `section-label` — #767d88 on #000000 at 14px | 5.06:1 | 4.5:1 | Pass on canvas; fails on either light surface |
| `footer` — #999999 on #000000 | 7.37:1 | 4.5:1 | Pass |
| `link-light` — #0c0c0c on #fefefe | 19.40:1 | 4.5:1 | Pass |

Harness after the edit: 10 disclosed failures, 0 undisclosed, 0 component-pair failures, 0 dangling refs.

### Motion inventory
Prescribed, not measured — the Cinematic block of SPEC §5 verbatim. Profile confirmed, not switched: rule 1's tell is full-bleed photography, sparse type and a slow reveal, which is this file's entire thesis ("a cinematic reel brought to life", "each section transition is a scroll through darkness into the next revelation").

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover | `{motion.duration-fast}` 240ms | `{motion.ease-standard}` | `opacity` of text and image | Same crossfade, capped at 150ms |
| Press / active | `{motion.duration-instant}` 120ms | `{motion.ease-standard}` | `opacity` only — no scale pop | Unchanged |
| Focus | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` of the `{colors.focus}` ring | Instant, never suppressed |
| Page / route transition | `{motion.duration-emphasis}` 900ms | `{motion.ease-enter}` | `opacity`, `translateY(24px)`→0 | Travel removed; 150ms fade |
| Modal / drawer enter | `{motion.duration-slow}` 600ms | `{motion.ease-enter}` | `opacity`, `translateY(32px)`→0 | Travel removed; 150ms fade |
| Modal / drawer exit | `{motion.duration-base}` 400ms | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; 150ms fade |
| Dropdown enter / exit | 400ms / 240ms | `ease-enter` / `ease-exit` | `opacity`, `translateY(-8px)`→0 | Travel removed; 150ms fade |
| Toast enter / exit | 400ms / 240ms | `ease-enter` / `ease-exit` | `opacity`, `translateY(16px)`→0 | Travel removed; 150ms fade |
| List enter (image grid) | 400ms, stagger 80ms | `{motion.ease-enter}` | `opacity`, `translateY(16px)`→0 | Stagger and travel removed; one 150ms fade |
| List exit | 240ms, no stagger | `{motion.ease-exit}` | `opacity`, `transform` | Travel removed; 150ms fade |
| Loading | 1600ms, infinite | linear | `opacity` pulse on the image placeholder | Frozen; static placeholder |
| Hero reveal + continuous slow scale (**stated as deliberate brand ambience**) | 900ms reveal | `{motion.ease-enter}` | `opacity`, `scale(1)`→`scale(1.04)` | Ambience frozen at `scale(1)`; video paused, poster shown |

Exit is always shorter than its entrance; `transform` and `opacity` only; nothing on first paint gates content.

### Shared issues (not fixed)
| File | Issue | Proposed fix |
|---|---|---|
| `theme-audit/audit.py` (states check, ~line 634) | `STATE_WORDS` are matched as bare substrings, so `active` is credited by the extracted line "Interactive elements blend into the editorial flow". runwayml is credited with an `active` state it does not document, and I left the extracted line alone rather than reword it to game the count. Repo-wide, every file saying "interactive" gets a free `active`. | Match on a word boundary and require the state to be the subject of its row: `re.search(r"(?<![a-z])active(?![a-z])", line)`, or require one of `active/pressed` to appear adjacent to a state marker. |
| `theme-audit/audit.py` (`find_role_strongest`, ~line 147) | The representative for `border`/`focus`/`text-dim` is chosen by highest contrast against the canvas **without a theme check**, so this dark-canvas file's `border` role resolves to `border-light-silver`, a light-theme hairline. `check("border", "canvas")` is then skipped by `same_theme` and the representative boundary is never measured against its own ground. Only `check_all` catches the real dark hairline. | Restrict candidates to `same_theme(key, canvas_key)` before taking the max, falling back to `find_role` when none match. |
| `theme-audit/audit.py` (section detection, ~line 219) | `f"## {s}" in text` matches inside deeper headings, so `### Iteration Guide` registers as the optional `## Iteration Guide` section — which is why the legacy file scored that section as present with no frontmatter at all. | Anchor to line start with exactly two hashes: `re.search(rf"^## {re.escape(s)}\s*$", text, re.M)`. |

### Needs approval
1. **`text-secondary` #767d88 as body/label text on `surface-dark` (4.19:1) and on the light surfaces (4.12:1 / 3.51:1).** This is Runway's documented secondary text colour and its own example prompt specifies it on both polarities. Nearest passing values: **#7d848e** (Mid Slate, already in the palette) reaches 4.61:1 on `surface-dark`; for the light surfaces the nearest passing cool-gray on the same hue is **#646b76** (4.54:1 on Cool Cloud, 5.33:1 on Near White, but 3.91:1 on the canvas, so it cannot replace Cool Slate everywhere). Defensible as extracted only where the label is 18.66px+/700 or 24px+, where the 3:1 large-text threshold applies — which does cover the 24px card titles but not the 14px section labels or 16px body. A brand owner must decide between restricting Cool Slate to the black canvas or shifting the light-surface secondary ink.
2. **`ink-secondary-alt` #3f3f3f used as the source describes it** — "dark-section secondary text" at 1.99:1 / 1.65:1. No usage note can make this defensible; it is not legible. Proposal: re-scope it in the document to light surfaces only (10.44:1 on `surface-light`), which is almost certainly what the live site does, but the prose says otherwise and I did not silently re-point it.
3. **Re-binding the three frozen hairlines.** `{components.card-dark}`, `{components.card-light}` and `{components.alert-container}` are left bound to the extracted hairlines (1.17:1 / 1.36:1 / 1.17:1) exactly as recorded, per SPEC §2. Whether a control whose only boundary is one of these should be re-bound to `text-secondary` #767d88 is a brand-owner call, not mine.
4. **The empty `accent` / `on-accent` roles.** Confirming that Runway has no signal colour, and that the two lost token points are correct rather than a naming miss, needs a brand owner's yes. The alternative — declaring `{colors.ink}` the accent — would read as a passing score bought with a false fact.
5. **The prescribed focus ring.** `#767d88` at 2px with a 2px offset, two-tone over photography. Reusing an existing tone keeps the no-accent rule intact, but a 3.51:1 worst case on Cool Cloud is close to the floor; a brand owner may prefer a dedicated ring value and accept a new colour in the palette.

### Identity verdict
Still unmistakably Runway. The token names carry the brand's own vocabulary rather than a generic ladder: `canvas` is true black, `canvas-deep` is the 1.02:1 near-duplicate the source insists on, every secondary voice is a cool blue-gray (#767d88, #7d848e, #c9ccd1) rather than a warm or neutral grey, the type group is one family at nine sizes with line-height 1.00 at the top and a weight-450 micro label at the bottom, and the radius ladder stops at 16px with no pill anywhere. The clearest identity signal is what the block does *not* contain: no accent, no `on-accent`, no `shadow:` group, no gradient. A token dump borrowed from another file in this collection would have all four. The one addition that is not Runway's own is the focus ring, and it is a brand tone reused rather than a colour introduced — stated as prescribed in both Colors and Accessibility.

The honest weakness is states, and it is the brand document's, not the conversion's: with one documented interaction state in the whole source, the Components section marks coverage rather than filling it, and the harness's 1 is the correct score.
