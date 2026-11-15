# Audit summary

84 DESIGN.md files, one reviewer each. Harness revision `a7042ea`.

**Both columns of every figure below come from that one revision.** The before-column is the pre-audit tree re-scored with the finished harness, not the numbers reported while the run was in progress. That distinction matters: the checks were corrected around forty times during the audit, mostly for defects that had been letting files pass, so the figures quoted mid-run understated the improvement. Contrast in particular reads 1.21 at baseline under the finished checks, against 3.17 under the blinder ones that produced it.

## What this audit could and could not measure

These files are documents, not a running UI. Token coverage, contrast ratios, reference integrity, section coverage and state coverage are computed from each file. Overlap, horizontal overflow, clipping, rendered tap-target size, frame rate and layout shift are **not measurable from a document** and no claim about them appears in any report.

**Motion is prescribed, not extracted.** Nobody measured these brands' real timing functions. Every Motion & Animation section states that in its first line. Where a source did record real timings — tesla's 0.33s and its one cubic-bezier — they are kept as extracted and displace the profile value, with the seam named in the file.

## Headline

| Dimension | Before | After |
|---|---|---|
| tokens | 3.65 | **4.90** |
| refs | 4.52 | **5.00** |
| contrast | 1.21 | **5.00** |
| sections | 2.10 | **5.00** |
| motion | 1.21 | **5.00** |
| states | 1.02 | **4.82** |

| | Before | After |
|---|---|---|
| Motion & Animation section | 0 / 84 | **84 / 84** |
| reduced-motion rule | 0 / 84 | **84 / 84** |
| `motion:` token group | 0 / 84 | **84 / 84** |
| focus ring token | 0 / 84 | **84 / 84** |
| Accessibility section | 0 / 84 | **84 / 84** |

74 of 84 files score 5 on every dimension. 633 contrast failures are documented with measured ratios; 0 remain undisclosed.

**A contrast score of 5 means every measured failure in that file is stated with its ratio, not that every pair passes.** The failures are real and still there: 633 of them. Disclosure is the only remedy available without changing an extracted brand hex, which this audit does not do.

## Matrix

Before → after, per dimension. `tok` tokens, `ref` references, `con` contrast, `sec` sections, `mot` motion, `sta` states.

| Site | Profile | tok | ref | con | sec | mot | sta |
|---|---|---|---|---|---|---|---|
| `1win` | Calm | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `airbnb` | Playful | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `airtable` | Calm | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `aljazeera` | Calm | 3→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `apple` | Cinematic | 5→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `binance` | Calm | 5→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `bmw` | Cinematic | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `bmw-m` | Cinematic | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `bugatti` | Cinematic | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `cal` | Calm | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `claude` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `clay` | Playful | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `clickhouse` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `cohere` | Crisp | 5→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `coinbase` | Calm | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `composio` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `cursor` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `dell-1996` | Calm | 3→5 | 5→5 | 3→5 | 1→5 | 1→5 | 1→5 |
| `dji` | Cinematic | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `elevenlabs` | Cinematic | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `expo` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `ferrari` | Cinematic | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `figma` | Playful | 3→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `framer` | Calm | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `hashicorp` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `hp` | Calm | 4→5 | 5→5 | 1→5 | 2→5 | 1→5 | 1→5 |
| `ibm` | Calm | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `intercom` | Playful | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `jobright` | Playful | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `kraken` | Calm | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `lamborghini` | Cinematic | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `linear.app` | Crisp | 5→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `lovable` | Playful | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `mastercard` | Calm | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `mercury` | Calm | 4→5 | 5→5 | 2→5 | 1→5 | 1→5 | 1→5 |
| `meta` | Cinematic | 3→4 | 5→5 | 1→5 | 3→5 | 3→5 | 2→5 |
| `minimax` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 3→5 | 1→5 |
| `mintlify` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 3→5 | 2→5 |
| `miro` | Playful | 4→5 | 5→5 | 1→5 | 3→5 | 3→5 | 1→5 |
| `mistral.ai` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 3→5 | 1→5 |
| `mongodb` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 3→5 | 1→5 |
| `mydealz` | Playful | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `nerdwallet` | Calm | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `nike` | Cinematic | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `nintendo-2001` | Playful | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `notion` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 3→5 | 1→5 |
| `nvidia` | Cinematic | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `ollama` | Crisp | 5→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `opencode.ai` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `oracle` | Calm | 4→4 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `oura` | Cinematic | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `pinterest` | Playful | 5→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `playstation` | Cinematic | 4→5 | 5→5 | 3→5 | 3→5 | 1→5 | 1→5 |
| `posthog` | Crisp | 5→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `raycast` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `renault` | Cinematic | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `replicate` | Crisp | 5→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `resend` | Crisp | 4→5 | 5→5 | 1→5 | 3→5 | 1→5 | 1→5 |
| `revolut` | Cinematic | 4→5 | 5→5 | 2→5 | 3→5 | 1→5 | 1→5 |
| `runwayml` | Cinematic | 1→3 | 1→5 | 1→5 | 1→5 | 1→5 | 1→1 |
| `sanity` | Crisp | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `sap` | Calm | 4→5 | 5→5 | 5→5 | 1→5 | 1→5 | 1→5 |
| `sentry` | Crisp | 4→4 | 5→5 | 1→5 | 2→5 | 1→5 | 1→5 |
| `shopify` | Cinematic | 2→3 | 5→5 | 2→5 | 2→5 | 1→5 | 1→5 |
| `slack` | Playful | 4→5 | 5→5 | 1→5 | 2→5 | 1→5 | 1→5 |
| `spacex` | Cinematic | 3→4 | 5→5 | 2→5 | 2→5 | 1→5 | 1→5 |
| `spotify` | Crisp | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 | 1→1 |
| `starbucks` | Playful | 1→5 | 1→5 | 1→5 | 1→5 | 3→5 | 1→2 |
| `stripe` | Crisp | 4→5 | 5→5 | 1→5 | 2→5 | 1→5 | 1→5 |
| `supabase` | Crisp | 4→5 | 5→5 | 1→5 | 2→5 | 1→5 | 1→5 |
| `superhuman` | Crisp | 4→5 | 5→5 | 1→5 | 2→5 | 1→5 | 1→5 |
| `tesla` | Cinematic | 1→5 | 1→5 | 1→5 | 1→5 | 1→5 | 1→3 |
| `theverge` | Cinematic | 1→5 | 1→5 | 1→5 | 1→5 | 3→5 | 1→3 |
| `together.ai` | Crisp | 4→5 | 5→5 | 3→5 | 1→5 | 1→5 | 1→5 |
| `uber` | Playful | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `vercel` | Crisp | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `vodafone` | Calm | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `voltagent` | Crisp | 4→5 | 5→5 | 3→5 | 1→5 | 1→5 | 1→5 |
| `warp` | Crisp | 4→5 | 5→5 | 3→5 | 1→5 | 1→5 | 1→5 |
| `webflow` | Calm | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `wired` | Calm | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `wise` | Calm | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `x.ai` | Crisp | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |
| `zapier` | Playful | 4→5 | 5→5 | 1→5 | 1→5 | 1→5 | 1→5 |

## Deliberate shortfalls

Eleven scores on tokens and states are short because the brand genuinely lacks what the column asks for. Each is recorded in that file's Known Gaps with the evidence. Filling them would have meant inventing facts about a real brand.

| Site | Dimension | Score | Why |
|---|---|---|---|
| `meta` | tokens | 4 | four muted tiers under brand names; reported as a harness gap |
| `oracle` | tokens | 4 | one ink per polarity; no muted tone exists to name |
| `runwayml` | tokens | 3 | accent and on-accent genuinely absent from the brand |
| `runwayml` | states | 1 | source documents one interaction, the nav hover |
| `sentry` | tokens | 4 | canvas and dim tones named outside the role patterns |
| `shopify` | tokens | 3 | dim ladder is numeric (shade-40/50/60); no alias added |
| `spacex` | tokens | 4 | text role cannot serve a dark canvas; recorded, not forced |
| `spotify` | states | 1 | source yields three states; five columns left empty |
| `starbucks` | states | 2 | hover, disabled and loading appear nowhere, and no disabled tone exists |
| `tesla` | states | 3 | pressed and selected recorded nowhere, including the carousel dots |
| `theverge` | states | 3 | disabled and loading exist for no component |

## Needs approval

**509 items across all 84 reports**, grouped by the decision each one asks for in `theme-audit/APPROVALS.md`. In every case the reviewer left the extracted value alone and recorded the measured ratio: no brand hex was altered anywhere in this audit, and no extracted `components:` binding was re-pointed.

The full count overstates the backlog. **197 of the items ask for nothing** — frozen tones recorded for completeness, now disclosed in their files with the measured ratio. **106** are sign-offs on a value the audit prescribed because the brand documents none. That leaves **206 live decisions.**

| Decision | Items | Files |
|---|---:|---:|
| Tap target under the 44px minimum | 14 | 14 |
| Motion profile assignment | 4 | 4 |
| Source contradicts itself | 8 | 8 |
| Token name, alias or duplicate hex | 18 | 16 |
| Re-point an extracted binding | 53 | 37 |
| No semantic palette for a state | 6 | 5 |
| Prescribed value or system awaiting sign-off | 106 | 66 |
| Change an extracted hex to reach the threshold | 78 | 36 |
| Frozen tone disclosed, no change sought | 197 | 68 |
| Unclassified — read the item | 25 | 19 |

The recurring shape is a frozen tone doing a job that needs contrast — most often a hairline at 1.1–1.9:1 serving as a text input's only boundary, which is a WCAG 1.4.11 failure with no size exemption. The second is a white label on a brand colour: binance's Buy/Sell at 2.13:1, clay's signature pink at 3.14:1, sanity's coral CTA at 3.10:1, cursor's orange at 3.52:1.

Per-file detail is in `theme-audit/reports/<agent>-<site>.md`.

## Undisclosed contrast failures

None. Every measured failure in all 84 files is stated with its ratio in that file's `## Accessibility` section.

143 of them, across 45 files, were disclosed by `theme-audit/disclose.py` after their reviewers had finished, as the harness got stricter. That script writes rows into the one section the harness reads; it changes no colour, no binding and no threshold. The rows carry the role the harness assigned, and, where a component states no `backgroundColor` of its own, say so and name the page floor as the substituted ground rather than implying the rendered result was measured.

## Shared fixes

The reviewers found roughly forty defects in the audit harness itself. The consequential ones all pushed scores **up**, not down:

- The `surface` role was a whitelist of adjectives that never matched a numbered surface, so files with no resolved role had every `on surface` check **short-circuit and pass**. Found by A28.
- `ink` was in the dark-theme vocabulary, so in every light-canvas file whose ink is named `ink`, `text on canvas` — the first row of the spec — was never checked. My own regression, found by A74.
- The states metric counted any occurrence of a word, so "**Inter**active" credited an `active` state and a row reading "hover — not captured" credited hover. Found by A60 and A52.
- Files with no frontmatter scored a vacuous 5 on refs and contrast, because nothing was measured. Found by A31.
- The disclosure matcher harvested a table's **Required** column, so a row stating "3.0:1" auto-disclosed any failure near 3.0. Found by A50.
- A single component binding could re-theme a token and make the harness skip a required pair — a loophole a file could exploit by adding a binding. My own regression, found by A75.

Eight rules were argued out by reviewers and written into SPEC.md: an apparently unsatisfied role (or one satisfied wrongly) is a harness bug to report rather than a token to invent; a frozen tone doing contrast work follows four ordered steps; a genuinely absent role stays unfilled; a focus token at an existing hex is a real role binding; an extracted timing beats a prescribed one; a paint-only state change is permitted; the illustration branch of the Playful rule stands alone; and "verbatim" governs a moved section's body, not its heading.

Four profile assignments were corrected on evidence from the files themselves — airtable, cal, figma and spotify all moved to Calm after their reviewers showed the rule had fired on palette size rather than on saturation and role.

## Known limitations

- About forty reported pairs sit near 1.0:1 because an ink and a ground of the same polarity were paired. Some are real (a hairline whose tone equals a surface); some are artefacts (a dark ink against a dark band in a light-canvas file). Luminance cannot separate them — a light-track ink is itself dark — so only a file's own declared bindings settle it. A guard I wrote for this fired on nothing and was reverted rather than left in.
- Three files (`sentry`, `shopify`, `spacex`) have a text role that cannot serve their canvas, because their inks for that ground are named outside the role patterns. Recorded rather than forced.
- An unsourced "no-hover policy" line appears in seven files and is defined nowhere in README.md or CONTRIBUTING.md. It suppressed state documentation collection-wide until each reviewer withdrew it. It should be removed from whatever generator produced it, not patched file by file.
- `raycast` carried a frontmatter key that was the Chinese word for "belongs to" alongside a real `description:`. Converted to a comment so its 942 characters of extracted prose survive and the schema is valid.
