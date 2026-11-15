# Needs approval

**509 items, from the Needs-approval section of all 84 reports.** Not one of them is a change already made: everything in this file is a question for whoever owns the brand value, and the audit's standing rule was to leave the extracted value alone and write the question down.

## How this document was built, and where it is weak

The reports are prose. Items are split on list markers and sorted into buckets by keyword, first matching rule winning, in the order the next table gives. Two honest consequences:

- An item that asks two questions appears once, under whichever rule matched first. The row's own wording usually shows this.
- **Unclassified is a real bucket.** It means no rule matched, not that the item is empty.

The excerpt in each row is the item's first sentence, cut to 240 characters. **The report is authoritative, not the excerpt.** Every row links to it.

An earlier count of these items read 508. It missed items numbered as a range (`2–6.`); the correct figure is 509.

## What actually needs a decision

Of the 509 items, **197 ask for nothing.** They are frozen extracted tones whose failure is now disclosed in the file with its measured ratio; the reviewer recorded them for completeness and recommended no change. Reading the whole set as a backlog overstates it by that much.

**106** are sign-offs rather than choices: a value or a whole system the audit prescribed because the brand documents none, labelled prescribed everywhere it appears. The question is whether the inference may stay, not which of two values to pick.

**206** are live decisions — a hex, a binding, a name, a tap target or a contradiction in the source, each with two or more real answers.

## Totals

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
| **Total** | **509** | **84** |

## Tap target under the 44px minimum

14 items across 14 files.

| Site | Worst ratio named | Proposed value | Item | Report |
|---|---:|---|---|---|
| `nintendo-2001` | 3.00:1 | — | Usage note: the 3:1 threshold applies because the wordmark is 44px/900. | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `airtable` | — | — | **`components.button-icon-circular` 40 × 40px.** Left at the extracted value. | [A03-airtable.md](reports/A03-airtable.md) |
| `bugatti` | — | — | **`components.button-icon` at 40 × 40px.** Below the 44px AAA target the file claims elsewhere. | [A09-bugatti.md](reports/A09-bugatti.md) |
| `clickhouse` | — | — | **Declared tap targets below 44 × 44 everywhere** (40px buttons and inputs, 36px icon button, ~36px tabs). | [A13-clickhouse.md](reports/A13-clickhouse.md) |
| `cohere` | — | — | **`announcement-bar` is 36px tall**, so its close control cannot meet a 44px tap target without an invisible extended hit area. | [A14-cohere.md](reports/A14-cohere.md) |
| `expo` | — | — | **Tap targets.** `button-primary` and `button-secondary` are declared at 40px, below WCAG 2.5.5's 44px. | [A21-expo.md](reports/A21-expo.md) |
| `linear.app` | — | — | **"CTAs hold ≥40px tap height"** in Responsive Behavior is 4px under WCAG 2.5.5. | [A32-linear.app.md](reports/A32-linear.app.md) |
| `lovable` | — | — | **Tap targets.** Declared button height is ~40px against a 44 × 44 minimum. | [A33-lovable.md](reports/A33-lovable.md) |
| `notion` | — | — | **Tap targets** — 40px buttons and ~32px desktop pill tabs, both from the file's own Responsive Behavior text. | [A46-notion.md](reports/A46-notion.md) |
| `playstation` | — | — | **`filter-pill` tap target.** The documented `8px 16px` padding on 14px type yields roughly 36px, which contradicts the file's own "all interactive elements meet WCAG AAA (≥ 44×44px)" claim. | [A53-playstation.md](reports/A53-playstation.md) |
| `renault` | — | — | **Tap targets below 44px.** `{component.button-icon-square}` declares 40px and `{component.button-pill}` 36px (40px on mobile). | [A56-renault.md](reports/A56-renault.md) |
| `vercel` | — | — | **The 44 px nav hit area.** `nav-cta-signup`, `nav-cta-login` and `nav-cta-ask-ai` are 28 px tall with `0px {spacing.xs}` (horizontal) padding. | [A76-vercel.md](reports/A76-vercel.md) |
| `wired` | — | — | **`button-icon-circular` at 36 px** needs `{spacing.md}` padding or an extended hit area to reach 44 px. | [A81-wired.md](reports/A81-wired.md) |
| `wise` | — | — | **`button-icon-circular` at 40 px.** Token arithmetic puts it under the 44 px minimum. | [A82-wise.md](reports/A82-wise.md) |

## Motion profile assignment

4 items across 4 files.

| Site | Item | Report |
|---|---|---|
| `airtable` | **Profile switch Playful → Calm.** Roster rule change needed, see below. | [A03-airtable.md](reports/A03-airtable.md) |
| `binance` | **Motion profile Calm, retained with a caveat.** Calm is correct under SPEC §5's assignment rules — Binance is dark-canvas but not luxury, and not a developer tool, so rules 1–3 do not fire and rule 4 applies. | [A06-binance.md](reports/A06-binance.md) |
| `cal` | **Motion profile switched from Playful to Calm**, per the brief's instruction to argue rather than switch silently. | [A10-cal.md](reports/A10-cal.md) |
| `figma` | **Motion profile switched from Playful to Calm.** Stated in the file and argued below. | [A23-figma.md](reports/A23-figma.md) |

## Source contradicts itself

8 items across 8 files.

| Site | Worst ratio named | Proposed value | Item | Report |
|---|---:|---|---|---|
| `mydealz` | 3.09:1 | — | **`button-outline-green` — `primary` label on white, 3.09:1 vs 4.5:1.** Nearest passing value: **`#197e25`** at 5.18:1. | [A42-mydealz.md](reports/A42-mydealz.md) |
| `cal` | — | — | **One Iteration Guide rule rewritten** ("Never document hover" → document every supported state). | [A10-cal.md](reports/A10-cal.md) |
| `claude` | — | — | **Two documented rules were rewritten**: the Don't `Don't add hover state styling beyond what the system already encodes` and Iteration Guide item 4 `Never document hover. | [A11-claude.md](reports/A11-claude.md) |
| `lovable` | — | — | Recommendation: this one should be fixed in the product, not merely documented. | [A33-lovable.md](reports/A33-lovable.md) |
| `mastercard` | — | — | **The footer divider contradiction** (`rgba(255,255,255,0.4)` in the Footer section vs "white-at-30%-opacity" in the Agent Prompt Guide) needs a ruling. | [A34-mastercard.md](reports/A34-mastercard.md) |
| `meta` | — | — | **`rounded.circle` disagrees with itself** — `9999px` in the frontmatter, `50%` in the Shapes table. | [A36-meta.md](reports/A36-meta.md) |
| `shopify` | — | — | **Resolve the `hairline-dark` / `surface-elevated-dark` collision.** Both are `#1e2c31`. | [A64-shopify.md](reports/A64-shopify.md) |
| `together.ai` | — | — | **Which hairline hex is authoritative.** The token is now `#ebebeb`, on the strength of the prose plus the exact `rgba(0, 0, 0, 0.08)` composite. | [A74-together.ai.md](reports/A74-together.ai.md) |

## Token name, alias or duplicate hex

18 items across 16 files.

| Site | Worst ratio named | Proposed value | Item | Report |
|---|---:|---|---|---|
| `ibm` | 1.00:1 | — | **`colors.focus` #0f62fe on `colors.primary` #0f62fe at 1.0:1.** There is exactly one passing single-colour answer, and it is already in the palette: `{colors.hairline-strong}` #161616 clears 3:1 against every surface this file defines — 1… | [A27-ibm.md](reports/A27-ibm.md) |
| `expo` | 1.61:1 | — | **`muted-soft` #cccccc — 1.61:1.** Documented as disabled text, for which WCAG sets no requirement, so defensible provided it never carries live copy. | [A21-expo.md](reports/A21-expo.md) |
| `mintlify` | 1.92:1 | `#007f62` (4.99:1) | **`brand-green` #00d4a4 on `canvas`, 1.92:1**, as `text-input-focused`'s 2px activation border. | [A38-mintlify.md](reports/A38-mintlify.md) |
| `nerdwallet` | 2.10:1 | — | **`{colors.faint}` #b1b3b5 — 2.1:1, needs 4.5.** Nearest passing: **#75777b at 4.49:1**. | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `elevenlabs` | 2.31:1 | `#757068` (4.51:1) | **`colors.muted-soft` #a8a29e — 2.31:1 on canvas, 2.52:1 on white.** Nearest passing value for live text: **#757068** (4.51:1 / 4.91:1) — a substantial change in appearance, not a nudge. | [A20-elevenlabs.md](reports/A20-elevenlabs.md) |
| `notion` | 2.66:1 | `#c4267f` (5.34:1), `#a02e6d` (6.76:1) | **`badge-pink` white on #ff64c8** — 2.66:1 at 13px/600. | [A46-notion.md](reports/A46-notion.md) |
| `meta` | 3.00:1 | — | **`colors.focus` duplicates `colors.primary`.** Both are #0064e0. | [A36-meta.md](reports/A36-meta.md) |
| `dell-1996` | 4.67:1 | — | *Alternative with no hex change:* `{colors.ink}` #000000 on the red fill measures 4.67:1 and passes at any size, at the cost of the white-on-red look the 1996 panel actually had. | [A18-dell-1996.md](reports/A18-dell-1996.md) |
| `aljazeera` | — | — | **Five prescribed token names added to a documentary file.** `surface-soft`, `text-secondary` and `border-control` are aliases of extracted hexes; `focus` (#000000) and `focus-on-dark` (#ffc500, the extracted select-gold) are new roles for… | [A04-aljazeera.md](reports/A04-aljazeera.md) |
| `claude` | — | — | **Renaming `accent-teal` / `accent-amber` was considered and rejected.** Scoping them to `status-teal` / `highlight-amber` would clear two harness failures legitimately — neither is an accent that carries text — but SPEC §2 explicitly warn… | [A11-claude.md](reports/A11-claude.md) |
| `dell-1996` | — | — | **`{colors.hairline}` duplicates `{colors.frame-ink}` at #000000.** This is extracted, not invented — the page has exactly one rule colour — but it does add a second token for a single value. | [A18-dell-1996.md](reports/A18-dell-1996.md) |
| `hashicorp` | — | — | **`surface-card` and `text-dim` are pure aliases.** They add no hex. | [A25-hashicorp.md](reports/A25-hashicorp.md) |
| `intercom` | — | — | **`surface` and `text-dim` are alias tokens** duplicating `surface-1` and `ink-muted` exactly. | [A28-intercom.md](reports/A28-intercom.md) |
| `linear.app` | — | — | **`{colors.surface}` and `{colors.text-dim}` are duplicate-hex role aliases.** They add two keys with no new colour. | [A32-linear.app.md](reports/A32-linear.app.md) |
| `mydealz` | — | — | **`focus` #197e25 reuses `green-strong`'s hex under a new role name.** If a repo-wide convention prefers aliasing (`focus: "{colors.green-strong}"`), this should change everywhere at once rather than in one file. | [A42-mydealz.md](reports/A42-mydealz.md) |
| `pinterest` | — | — | **`{colors.focus-on-dark}` duplicates an existing hex.** `#617bff` is already in the palette as `{colors.accent-pressed-blue}`. | [A52-pinterest.md](reports/A52-pinterest.md) |
| `sentry` | — | — | **The second focus ring.** `focus-on-light` carries the same hex as `{colors.accent-violet-deep}`. | [A63-sentry.md](reports/A63-sentry.md) |
| `sentry` | — | — | **Renaming `ring-focus` to `focus`.** The hex is unchanged and the single prose reference was updated. | [A63-sentry.md](reports/A63-sentry.md) |

## Re-point an extracted binding

53 items across 37 files.

| Site | Worst ratio named | Proposed value | Item | Report |
|---|---:|---|---|---|
| `wise` | 1.07:1 | — | **`badge-negative` label token.** The prose says "text white"; the frontmatter said `{colors.on-primary}` (near-black, 1.07:1). | [A82-wise.md](reports/A82-wise.md) |
| `x.ai` | 1.08:1 | — | **Re-binding `text-input.borderColor` from `{colors.hairline}` to `{colors.body-mid}`.** The hairline is the field's only boundary and measures 1.08:1 against `{colors.canvas-soft}`; `{colors.body-mid}` #7d8187 reaches 4.36:1 on the same g… | [A83-x.ai.md](reports/A83-x.ai.md) |
| `warp` | 1.11:1 | — | **Re-point `text-input.borderColor` from `{colors.hairline}` to `{colors.mute}`.** The extracted border measures 1.11:1 against the input's own `{colors.canvas-soft}` fill, and on `text-input` that line is the control's only boundary. | [A79-warp.md](reports/A79-warp.md) |
| `renault` | 1.12:1 | — | **Re-binding the frozen `{colors.hairline}` in `components:`.** `configurator-row` and `nav-bar` still declare `{colors.hairline}` exactly as extracted (1.12:1 on canvas). | [A56-renault.md](reports/A56-renault.md) |
| `uber` | 1.13:1 | — | **`surface-pressed` as a divider on the real site.** I re-pointed only the three auto-derived `ex-*` boundaries. | [A75-uber.md](reports/A75-uber.md) |
| `supabase` | 1.15:1 | — | **Re-binding the card, table and divider hairlines.** `{colors.hairline}` `#dfdfdf` 1.33:1, `hairline-cool` `#ededed` 1.17:1, `hairline-cool-2` `#efefef` 1.15:1, `hairline-cool-3` `#d4d4d4` 1.48:1 and `hairline-strong` `#c7c7c7` 1.69:1 are… | [A70-supabase.md](reports/A70-supabase.md) |
| `spacex` | 1.16:1 | `#5a5a5f` (6.86:1) | **Re-binding the extracted light hairline.** `hairline-on-light` #e0e0e8 is 1.31:1 on `canvas-light` and 1.16:1 on `canvas-cool`. | [A66-spacex.md](reports/A66-spacex.md) |
| `tesla` | 1.16:1 | `#949494` (3.03:1), `#8D8D8D` (3.02:1) | **Re-binding the extracted hairlines.** `{colors.border}` (#EEEEEE, 1.16:1) and `{colors.border-strong}` (#D0D1D2, 1.53:1) are the only boundary tones Tesla's site defines, and neither reaches 3:1 on any surface in this file. | [A72-tesla.md](reports/A72-tesla.md) |
| `runwayml` | 1.17:1 | — | **Re-binding the three frozen hairlines.** `{components.card-dark}`, `{components.card-light}` and `{components.alert-container}` are left bound to the extracted hairlines (1.17:1 / 1.36:1 / 1.17:1) exactly as recorded, per SPEC §2. | [A60-runwayml.md](reports/A60-runwayml.md) |
| `together.ai` | 1.19:1 | — | **Re-binding the frozen control boundaries.** `text-input` and `button-outline` keep their extracted `rgba(0, 0, 0, 0.08)` → `#ebebeb` border at 1.19:1, which is the control's only boundary. | [A74-together.ai.md](reports/A74-together.ai.md) |
| `vercel` | 1.19:1 | — | **Re-bind the interactive boundaries from `{colors.hairline}` to `{colors.mute}`.** Six `components:` entries declare `borderColor: "{colors.hairline}"` — `form-input`, `form-input-sm`, `form-input-lg`, `nav-cta-ask-ai`, `icon-button-circu… | [A76-vercel.md](reports/A76-vercel.md) |
| `wired` | 1.21:1 | — | **Re-bind the `ex-*` card borders off `{colors.hairline}`.** `ex-pricing-tier` and `ex-data-table-cell` use `{colors.hairline}` #e0e0e0 as a card's or a row's only boundary, at 1.21:1 on `{colors.canvas-soft}` against a 3:1 requirement. | [A81-wired.md](reports/A81-wired.md) |
| `oura` | 1.22:1 | `#8a8171` (3.43:1), `#938a7a` (3.41:1) | **`colors.hairline` #e1dcd3 — 1.22:1 on canvas, 1.37:1 on surface (needs 3.0:1).** Nearest passing on canvas: #8a8171 (3.43:1); the lightest warm tone that clears 3:1 on *white* as well is around #938a7a (3.41:1 on white, 3.04:1 on cream). | [A51-oura.md](reports/A51-oura.md) |
| `sanity` | 1.22:1 | — | **Re-binding the input and ghost-button boundary.** `text-input`, `search-input`, `button-ghost` and the nav rule are extracted as 1px `#212121`, measured at 1.22:1 on the canvas. | [A61-sanity.md](reports/A61-sanity.md) |
| `shopify` | 1.22:1 | — | **Re-point the extracted `hairline-light` where a boundary must be seen.** `hairline-light` `#e4e4e7` measures 1.27:1 on `canvas-light` and 1.22:1 on `canvas-cream`, against a 3:1 minimum. | [A64-shopify.md](reports/A64-shopify.md) |
| `stripe` | 1.23:1 | — | **Re-point `card-feature-light` / `card-pricing` boundaries.** `{colors.hairline}` `#e3e8ee` at 1.23:1 on white. | [A69-stripe.md](reports/A69-stripe.md) |
| `linear.app` | 1.24:1 | — | **The three hairlines (1.24:1 – 1.96:1 against 3.0:1).** Nearest passing value against the worst case (`surface-4`) is about **#6a6e78**, which is exactly the prescribed `{colors.hairline-control}` I added *alongside* them. | [A32-linear.app.md](reports/A32-linear.app.md) |
| `sentry` | 1.24:1 | — | **Re-binding `card-pricing`'s border.** `{colors.hairline-cloud}` #e5e7eb at **1.24:1**. | [A63-sentry.md](reports/A63-sentry.md) |
| `slack` | 1.25:1 | — | **Re-binding the extracted hairline.** `text-input` and `card-pricing` document a `1px {colors.hairline}` border at **1.25:1** on white. | [A65-slack.md](reports/A65-slack.md) |
| `replicate` | 1.27:1 | — | **Re-binding the three `{colors.hairline}` boundaries.** `{component.text-input}`, `{component.button-icon}` and `{component.badge-tag}` are drawn with a 1.27:1 edge on the live site. | [A57-replicate.md](reports/A57-replicate.md) |
| `spotify` | 1.27:1 | — | **Re-bind the search input's focus border.** `{components.input-search-focus}` binds `borderColor: {colors.border-focus}` (`#000000`), measured at **1.27:1** against the input's own `#1f1f1f` fill. | [A67-spotify.md](reports/A67-spotify.md) |
| `superhuman` | 1.27:1 | `#a3a3a3` (3.03:1) | **Re-bind the input and card boundary from `{colors.hairline}` to `{colors.hairline-dark}`.** `{colors.hairline}` #e8e4dd is extracted and frozen at 1.27:1 on white; it is the only boundary of `text-input`, `card-pricing` and `card-feature… | [A71-superhuman.md](reports/A71-superhuman.md) |
| `revolut` | 1.29:1 | — | **Re-binding the `text-input` boundary.** `text-input` and `feature-card-light` are documented with a 1px `{colors.hairline-light}` `#e2e2e7` border, measuring 1.29:1 on `#ffffff` against the 3.0:1 a control boundary needs. | [A59-revolut.md](reports/A59-revolut.md) |
| `resend` | 1.35:1 | — | **Re-binding the control boundaries.** `{component.text-input}`, `{component.button-outline}`, `{component.button-ghost}`, `{component.feature-card-bordered}`, `{component.pricing-tier}` and `{component.code-window}` are all documented in… | [A58-resend.md](reports/A58-resend.md) |
| `sentry` | 1.37:1 | `#79628c` (3.23:1) | **Re-binding the dark-card hairline.** `{colors.hairline-violet}` #362d59 at **1.37:1** / **1.49:1**. | [A63-sentry.md](reports/A63-sentry.md) |
| `shopify` | 1.38:1 | — | **Re-point or re-scope the extracted `hairline-dark`.** 1.46:1 on `canvas-night`, 1.38:1 on `canvas-night-elevated`. | [A64-shopify.md](reports/A64-shopify.md) |
| `meta` | 1.40:1 | `#868b92` (3.43:1) | **`colors.hairline` as a control boundary — real 1.4.11 failure.** 1.54:1 on canvas, 1.40:1 on surface-soft against 3:1, as the sole boundary of `text-input` and inactive `button-pill-tab`. | [A36-meta.md](reports/A36-meta.md) |
| `starbucks` | 1.40:1 | `#929597` (3.01:1), `#878a8c` (3.05:1) | **Re-binding the form field's boundary.** `{colors.border-input}` #d6dbde is extracted and frozen, and it is the only visible edge of every text input, select and stepper at 1.40:1 on white. | [A68-starbucks.md](reports/A68-starbucks.md) |
| `theverge` | 1.43:1 | `#313131` (1.43:1), `#3d00bf` (1.73:1) | **Re-binding the two frozen hairlines.** `{colors.border-image}` #313131 (1.43:1) and `{colors.ultraviolet-rule}` #3d00bf (1.73:1) keep their extracted `components:` bindings. | [A73-theverge.md](reports/A73-theverge.md) |
| `webflow` | 1.43:1 | — | **Re-pointing `text-input.borderColor` and `button-secondary.borderColor`** from `{colors.hairline}` (1.43:1) to `{colors.mute}` (3.5:1). | [A80-webflow.md](reports/A80-webflow.md) |
| `sentry` | 1.54:1 | `#8e8ea0` (3.05:1) | **Re-binding `text-input`'s border.** The extracted boundary is `{colors.hairline-cool}` #cfcfdb at **1.54:1** on white, and on the real site it is the field's only boundary — a WCAG 1.4.11 failure. | [A63-sentry.md](reports/A63-sentry.md) |
| `raycast` | 1.56:1 | — | **Re-binding `{component.text-input-focused}` to the focus ring.** Its extracted binding — border brightening to `{colors.hairline-strong}`, 1.56:1 composited on `{colors.surface}` — is left exactly as captured, because it is a fact about… | [A55-raycast.md](reports/A55-raycast.md) |
| `posthog` | 1.58:1 | — | **Re-point the input boundary.** `{component.text-input}` and `{component.search-input}` are documented with a 1px `{colors.hairline}` boundary at 1.58:1 on cream — for a field whose boundary is its only affordance. | [A54-posthog.md](reports/A54-posthog.md) |
| `runwayml` | 1.65:1 | — | **`ink-secondary-alt` #3f3f3f used as the source describes it** — "dark-section secondary text" at 1.99:1 / 1.65:1. | [A60-runwayml.md](reports/A60-runwayml.md) |
| `zapier` | 1.66:1 | — | **Re-pointing the `ex-*` `mute` boundary bindings.** `ex-pricing-tier.borderColor`, `ex-cart-drawer.item-divider` and `ex-data-table-cell.rowBorder` all resolve to `{colors.mute}` at 1.66:1 on their own cream ground, below the 3:1 a visibl… | [A84-zapier.md](reports/A84-zapier.md) |
| `voltagent` | 1.69:1 | — | **Re-binding the frozen hairline in `components:`.** Seven components bind `borderColor: "{colors.hairline}"` (`button-outline-on-dark`, `button-pill-tag`, `text-input`, `card-feature`, `card-feature-emphasized`, `code-mockup`, plus `ex-pr… | [A78-voltagent.md](reports/A78-voltagent.md) |
| `spotify` | 1.77:1 | — | **Re-scope `{colors.border}` (`#4d4d4d`) to decoration permanently.** The prose calls it "button borders on dark" and it clears 3:1 on no surface in the file (2.22:1 / 2.10:1 / 1.95:1 / 1.81:1 / 1.77:1). | [A67-spotify.md](reports/A67-spotify.md) |
| `stripe` | 1.82:1 | — | **Re-point `text-input`'s boundary.** The extracted `borderColor: {colors.hairline-input}` `#a8c3de` measures 1.82:1 on `{colors.canvas}` and is the field's only affordance, so the real product fails WCAG 1.4.11. | [A69-stripe.md](reports/A69-stripe.md) |
| `spacex` | 1.86:1 | `#5a5a5a` (3.04:1) | **Re-scoping the extracted dark hairline.** `hairline-on-dark` #3a3a3f is 1.86:1 on `canvas-night`. | [A66-spacex.md](reports/A66-spacex.md) |
| `framer` | 2.59:1 | — | **`gradient-spotlight-card-orange`: white on `#ff7a3d` is 2.59:1 and fails at every text size.** Verified as a brand failure, not a binding error — the card binds `{colors.ink}` exactly as the violet, magenta and coral variants do, and tha… | [A24-framer.md](reports/A24-framer.md) |
| `theverge` | 2.79:1 | — | **`border-mint` #309875 on a mint tile = 2.79:1.** The palette's own passing alternative is `{colors.text-inverted}` #131313 at 14.52:1. | [A73-theverge.md](reports/A73-theverge.md) |
| `webflow` | 2.86:1 | — | **`category-card-orange` — white on `#ff6b00` at 2.86:1.** Verdict: **genuine brand failure, not a binding error.** The evidence: `category-card-green` in the same five-card set deliberately flips its label to `{colors.primary}` ink and th… | [A80-webflow.md](reports/A80-webflow.md) |
| `oura` | 3.00:1 | `#6e6c69` (4.66:1) | **`colors.ash` #838280 — 3.42:1 on canvas, 3.84:1 on surface (needs 4.5:1).** Nearest passing: #6e6c69 (4.66:1 on cream, 5.23:1 on white). | [A51-oura.md](reports/A51-oura.md) |
| `sanity` | 3.00:1 | — | **`button-primary` label.** `#ffffff` on `#f36458` is 3.10:1. | [A61-sanity.md](reports/A61-sanity.md) |
| `sap` | 3.00:1 | — | **Blue type is now forbidden on `{colors.sky}` (3.22:1) and `{colors.ink}` (3.29:1).** Both clear the 3:1 non-text minimum, so the usage note that makes them defensible is: these values are legitimate for the focus ring and for non-text bo… | [A62-sap.md](reports/A62-sap.md) |
| `voltagent` | 3.03:1 | — | **Using `{colors.hairline-soft}` on dark at all.** It was extracted as a tint for "rare on-light secondary contexts". | [A78-voltagent.md](reports/A78-voltagent.md) |
| `minimax` | 3.26:1 | — | **`stone` #8e8e93 at 3.26:1 on canvas, described as "muted captions".** Either re-scope the prose to 24px+ labels only, or substitute `{colors.muted-strong}` for captions. | [A37-minimax.md](reports/A37-minimax.md) |
| `sap` | 6.72:1 | — | **`{colors.hairline}` is bound as a boundary at 6.72:1 on canvas and passes — but it is the same hex as `{colors.ink-meta}`.** The file documents this ("The same value as `{colors.ink-meta}`, used as a border rather than as type"). | [A62-sap.md](reports/A62-sap.md) |
| `oracle` | — | — | **`{components.button-secondary-inverse}` now declares `backgroundColor: "{colors.ink-deep}"`.** This commits the component to a specific ground the prose only described as "a dark band". | [A50-oracle.md](reports/A50-oracle.md) |
| `revolut` | — | — | **The two focus rings.** Both are prescribed bindings onto existing hexes, not extracted facts. | [A59-revolut.md](reports/A59-revolut.md) |
| `slack` | — | — | **The origin of `{colors.hairline-strong}` `#000000`.** It has no prose binding, no attributed source page and no mention in the document, yet it holds the `border` role. | [A65-slack.md](reports/A65-slack.md) |
| `vodafone` | — | — | **Re-binding the frozen tones.** SPEC §2 step 3 requires the extracted `components:` bindings be left as extracted, so `{colors.mute}`'s remaining role as placeholder text and low-key footer links stands in the document. | [A77-vodafone.md](reports/A77-vodafone.md) |
| `wise` | — | — | **Re-binding the `{colors.canvas-soft}` divider.** I re-scoped the two auto-derived divider bindings to `{colors.mute}`. | [A82-wise.md](reports/A82-wise.md) |

## No semantic palette for a state

6 items across 5 files.

| Site | Worst ratio named | Proposed value | Item | Report |
|---|---:|---|---|---|
| `x.ai` | 6.54:1 | — | **Error state borrows `{colors.accent-sunset}`.** The brand surfaces no semantic palette. | [A83-x.ai.md](reports/A83-x.ai.md) |
| `sap` | — | — | **No status palette.** `ex-auth-form-card`'s error state is marked structurally and by text because the brand owns no red. | [A62-sap.md](reports/A62-sap.md) |
| `uber` | — | — | **Disabled treatment.** Specified as 38% opacity on the live fill and label, because the palette contains no disabled tone and inventing a grey hex would falsify a monochrome brand. | [A75-uber.md](reports/A75-uber.md) |
| `uber` | — | — | **Error signalling with no semantic palette.** Specified as a 2px `{colors.ink}` boundary plus a `{typography.caption}` message. | [A75-uber.md](reports/A75-uber.md) |
| `voltagent` | — | — | **The `error` state has no colour.** The brand ships no red anywhere in the extracted material. | [A78-voltagent.md](reports/A78-voltagent.md) |
| `warp` | — | — | **The error state has no hue.** `text-input`'s error is specified as a mono `!` glyph plus `{colors.body-strong}` helper text, because the brand surfaces no red. | [A79-warp.md](reports/A79-warp.md) |

## Prescribed value or system awaiting sign-off

106 items across 66 files.

| Site | Worst ratio named | Proposed value | Item | Report |
|---|---:|---|---|---|
| `bugatti` | 1.00:1 | — | **`colors.focus` #5b7fa6 is an invention.** Nothing in the analyzed set showed a focus indicator. | [A09-bugatti.md](reports/A09-bugatti.md) |
| `claude` | 1.00:1 | — | **`focus` #141413 and `focus-on-dark` #faf9f5 are invented.** claude.com's real focus treatment is unmeasured. | [A11-claude.md](reports/A11-claude.md) |
| `warp` | 1.00:1 | — | **Focus ring geometry.** 2 px ring, 2 px `{colors.canvas}` offset, drawn outside the control. | [A79-warp.md](reports/A79-warp.md) |
| `linear.app` | 1.01:1 | — | **`primary-focus` #5e69d1 as the ring on the lavender CTA: 1.01:1.** No nearby value fixes this — any ring close enough to the brand lavender to read as lavender is invisible on a lavender fill. | [A32-linear.app.md](reports/A32-linear.app.md) |
| `mercury` | 1.03:1 | — | **Tonal elevation at 1.03:1 to 1.14:1** between canvas, surface, surface-tint, lavender and the two night layers. | [A35-mercury.md](reports/A35-mercury.md) |
| `elevenlabs` | 1.05:1 | `#f0efed` (1.05:1), `#e7e5e4` (1.15:1) | **The three extracted hairlines — #f0efed (1.05:1), #e7e5e4 (1.15:1), #d6d3d1 (1.37:1) on the canvas, all needing 3:1.** Nearest passing value: **#8a8580** (3.35:1), added as the prescribed `{colors.hairline-control}` rather than altering… | [A20-elevenlabs.md](reports/A20-elevenlabs.md) |
| `jobright` | 1.12:1 | `#7a8290` (3.62:1) | **`{colors.hairline}` #e5e7eb as a control boundary.** 1.24:1 on canvas, 1.12:1 on surface-soft. | [A29-jobright.md](reports/A29-jobright.md) |
| `framer` | 1.14:1 | — | **The two frozen hairlines, 1.32:1 and 1.14:1 on canvas, are real brand values that fail.** Kept and scoped to decoration, with `hairline-strong` (#6b6b6b, 3.74:1, prescribed) added alongside for boundaries that carry meaning. | [A24-framer.md](reports/A24-framer.md) |
| `ferrari` | 1.17:1 | — | `{colors.semantic-success}` #03904a on canvas — 4.31:1. | [A22-ferrari.md](reports/A22-ferrari.md) |
| `oracle` | 1.23:1 | — | **`{colors.hairline-strong}` #857f79 — new prescribed token.** Not a brand value. | [A50-oracle.md](reports/A50-oracle.md) |
| `lamborghini` | 1.25:1 | — | **Ash `#7D7D7D` as body text on Charcoal `#202020` — 3.96:1 (and the `card-news` component built from it).** Nearest passing value: Smoke `#F5F5F5`, 14.94:1 — the file's own secondary-text tone. | [A31-lamborghini.md](reports/A31-lamborghini.md) |
| `ollama` | 1.26:1 | — | **`{colors.hairline-control}` `#8f8f8f` is an invented hex.** It is prescribed, labelled as such in the Colors section and in Known Gaps, and has no counterpart on ollama.com. | [A48-ollama.md](reports/A48-ollama.md) |
| `apple` | 1.32:1 | `#949499` (3.00:1), `#86868b` (3.62:1) | **`{colors.hairline}` #e0e0e0 at 1.32:1 on canvas, required 3.0:1.** Not changed. | [A05-apple.md](reports/A05-apple.md) |
| `dji` | 1.36:1 | `#767676` (4.54:1) | **The four interactive boundaries — `card-border` 1.41:1, `dashed-border` 1.36:1, `input-border` 1.45:1, `control-border` 1.61:1 (all need 3.0:1).** I prescribed `{colors.hairline-strong}` #767676 (4.54:1) for these four in the prose but d… | [A19-dji.md](reports/A19-dji.md) |
| `kraken` | 1.37:1 | `#026b3f` (6.61:1) | Defensible usage note: fill-only, at 16% opacity, with `success-text` #026b3f (6.61:1 on canvas, 5.49:1 on the composited fill) carrying every label. | [A30-kraken.md](reports/A30-kraken.md) |
| `clickhouse` | 1.38:1 | — | **The extracted hairlines, 1.38:1 and 1.74:1 on canvas.** Handled per SPEC §2 with a parallel prescribed token and the failure stated plainly in the file. | [A13-clickhouse.md](reports/A13-clickhouse.md) |
| `bugatti` | 1.39:1 | `#262626` (1.39:1), `#3a3a3a` (1.85:1) | **`colors.hairline` #262626 (1.39:1) and `colors.hairline-strong` #3a3a3a (1.85:1) — required 3.0:1.** Both left in place and scoped to decoration per SPEC §2. | [A09-bugatti.md](reports/A09-bugatti.md) |
| `nerdwallet` | 1.41:1 | — | **`{colors.hairline-strong}` #d8d9da as a control boundary — 1.41:1 on canvas, needs 3.0.** It is the extracted border of `{button-outline}` and `{product-card}`. | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `hashicorp` | 1.42:1 | `#8a8f99` (6.47:1) | **`hairline` #3b3d45 / `hairline-soft` #252830** — 1.94:1 and 1.42:1 on canvas, required 3.0:1. | [A25-hashicorp.md](reports/A25-hashicorp.md) |
| `jobright` | 1.43:1 | `#00664a` (7.00:1) | **`{colors.primary}` #00f0a0 as text on light surfaces.** 1.50:1 on `{colors.canvas}` (the `{component.score-ring}` numeral) and 1.43:1 on `{colors.canvas-mint}`; the Colors section also gives mint to inline links. | [A29-jobright.md](reports/A29-jobright.md) |
| `oura` | 1.46:1 | `#8f8f8f` (3.23:1) | **`colors.silver` #cccac7 as the `pill-tab` selected border — 1.46:1 on canvas (needs 3.0:1).** Nearest passing: #8a8171, i.e. | [A51-oura.md](reports/A51-oura.md) |
| `composio` | 1.52:1 | `#606060` (3.05:1) | **`hairline-control: "#757575"`** — prescribed accessible parallel to the three frozen hairlines (1.10 / 1.20 / 1.52:1 on canvas). | [A16-composio.md](reports/A16-composio.md) |
| `miro` | 1.54:1 | — | **`hairline-strong` `#c7cad5` as a control boundary — 1.64:1 on canvas, 1.54:1 on surface (needs 3:1).** This is the live border of `text-input`, `button-secondary` and `filter-dropdown`. | [A39-miro.md](reports/A39-miro.md) |
| `nvidia` | 1.61:1 | `#949494` (3.03:1), `#757575` (4.61:1) | **`{colors.hairline}` #cccccc on `{colors.canvas}` — 1.61:1, needs 3.0:1.** Nearest passing value: **#949494** (3.03:1). | [A47-nvidia.md](reports/A47-nvidia.md) |
| `playstation` | 1.61:1 | — | **`ash-light` #cccccc as the live input and secondary-button border — 1.61:1 against 3.0:1.** Nearest passing value on `canvas-light` is `#949494` (3.00:1); the safe choice is the file's own `mute-light` #6b6b6b at 5.33:1, which is what th… | [A53-playstation.md](reports/A53-playstation.md) |
| `mongodb` | 1.63:1 | `#6b7a88` (4.41:1) | **`hairline-strong` as the `text-input` boundary = 1.63:1.** I added the prescribed `{colors.hairline-control}` #6b7a88 (4.41:1) alongside and scoped the extracted hairlines to decoration, rather than changing the input's documented border. | [A41-mongodb.md](reports/A41-mongodb.md) |
| `nike` | 1.64:1 | — | **Control boundaries moved off an extracted hex.** `filter-chip`, `badge-promo` and the light-colorway `swatch-dot` ring were documented with a 1px `{colors.hairline}` `#cacacb` edge at 1.64:1. | [A44-nike.md](reports/A44-nike.md) |
| `ibm` | 1.68:1 | — | **`colors.semantic-success` #24a148 at 3.35:1 and `colors.semantic-warning` #f1c21b at 1.68:1 on canvas.** Nearest passing green is Carbon's own `green-60` #198038 at 5.02:1. | [A27-ibm.md](reports/A27-ibm.md) |
| `mercury` | 1.70:1 | `#8a8a93` (3.01:1) | **`{colors.fog}` #c3c3cc on `{colors.canvas}` at 1.70:1** (needs 3:1 as a non-text boundary). | [A35-mercury.md](reports/A35-mercury.md) |
| `composio` | 1.75:1 | `#3d4bff` (3.33:1) | **`focus: "#6b7bff"`** — prescribed, not extracted. | [A16-composio.md](reports/A16-composio.md) |
| `supabase` | 2.00:1 | — | **Focus ring colour.** `{colors.focus}` `#707070` is prescribed and is grey, not emerald. | [A70-supabase.md](reports/A70-supabase.md) |
| `posthog` | 2.03:1 | — | **The prescribed ring colour.** `focus: #2c84e0` reuses `accent-blue`. | [A54-posthog.md](reports/A54-posthog.md) |
| `tesla` | 2.12:1 | — | **The prescribed focus ring.** `focus: #3E6AE1` reuses Electric Blue, which the file's own Don'ts reserve for primary CTAs ("never for decorative purposes"). | [A72-tesla.md](reports/A72-tesla.md) |
| `binance` | 2.13:1 | — | **No light-theme green.** `{colors.trading-up}` is 2.13:1 on white, and `{component.price-chart-card}` is a white card that plots price-up in it. | [A06-binance.md](reports/A06-binance.md) |
| `oracle` | 2.24:1 | — | **`text-dim` left unfilled.** I did not add one. | [A50-oracle.md](reports/A50-oracle.md) |
| `mercury` | 2.64:1 | `#3b4bd1` (6.57:1) | **`{colors.focus}` = #5266eb is prescribed, not extracted.** It reuses Mercury Indigo and clears 3:1 on all six surfaces, so it needs no light/dark pair. | [A35-mercury.md](reports/A35-mercury.md) |
| `expo` | 2.74:1 | — | **Focus ring on the hero gradient.** `focus` #0d74ce reaches only 2.74:1 against `gradient-sky-mid` #a8c8e8. | [A21-expo.md](reports/A21-expo.md) |
| `opencode.ai` | 2.80:1 | — | `ash` `#9a9898` as the 2px active-tab underline, 2.8:1 against `canvas` where 3:1 is required. | [A49-opencode.ai.md](reports/A49-opencode.ai.md) |
| `jobright` | 2.94:1 | `#616a75` (5.49:1) | **`{colors.muted}` #86909c as secondary text.** Measures 3.24:1 on `{colors.canvas}` and 2.94:1 on `{colors.surface-soft}`; the brand uses it for 14px footer links and captions. | [A29-jobright.md](reports/A29-jobright.md) |
| `minimax` | 2.95:1 | `#0f7a50` (5.08:1) | **`badge-success` — `success-text` on `success-bg` at 13px, 2.95:1.** Shipped `badge-success-accessible` alongside it using the prescribed `{colors.success-text-strong}` #0f7a50 (5.08:1). | [A37-minimax.md](reports/A37-minimax.md) |
| `coinbase` | 3.00:1 | — | **`{colors.focus}` reusing `{colors.primary}`.** Prescribed. | [A15-coinbase.md](reports/A15-coinbase.md) |
| `dji` | 3.00:1 | — | **`button-store-cart` — `store-blue` #0060ef on `store-blue-tint` #deeafd, 4.41:1 (needs 4.5:1).** Fails by 0.09. | [A19-dji.md](reports/A19-dji.md) |
| `dji` | 3.00:1 | — | **`focus` #00142b, `focus-on-dark` #ffffff and `hairline-strong` #767676 are all invented.** DJI ships no documented focus ring and no 3:1 boundary. | [A19-dji.md](reports/A19-dji.md) |
| `playstation` | 3.00:1 | — | **Two focus rings rather than one.** No single value clears 3:1 on `#ffffff`, `#000000` and `#0070d1` simultaneously — a white canvas caps the ring's luminance at L≤0.30 while the blue band needs a much higher or much lower one. | [A53-playstation.md](reports/A53-playstation.md) |
| `sap` | 3.00:1 | — | **Two rings, prescribed.** `{colors.focus}` = `{colors.primary}` #0057d2 and `{colors.focus-on-dark}` = `{colors.on-primary}` #ffffff, 2px at 2px offset. | [A62-sap.md](reports/A62-sap.md) |
| `spacex` | 3.00:1 | — | **Both focus rings are prescribed.** The source pages define no focus style. | [A66-spacex.md](reports/A66-spacex.md) |
| `uber` | 3.00:1 | — | **`hairline-mid` `#4b4b4b` as the boundary tone.** It passes comfortably (7.59:1 on canvas-soft) but is visually heavy for a hairline. | [A75-uber.md](reports/A75-uber.md) |
| `claude` | 3.11:1 | — | **Coral as inline link ink fails AA.** `primary` on `canvas` = **3.11:1** at `body-md` 16px. | [A11-claude.md](reports/A11-claude.md) |
| `lovable` | 3.22:1 | `#8a8884` (3.22:1) | Nearest passing value: **#8a8884** (3.22:1), which is `#1c1c1c` at 50% over cream and is already in the file as the prescribed `hairline-strong`. | [A33-lovable.md](reports/A33-lovable.md) |
| `runwayml` | 3.51:1 | — | **The prescribed focus ring.** `#767d88` at 2px with a 2px offset, two-tone over photography. | [A60-runwayml.md](reports/A60-runwayml.md) |
| `hashicorp` | 3.54:1 | `#000000` (5.93:1), `#c62f36` (4.59:1) | **`ink` on `product-boundary`** — 3.54:1, required 4.5:1. | [A25-hashicorp.md](reports/A25-hashicorp.md) |
| `supabase` | 3.83:1 | — | **Prescribed error tone.** `text-input` and `code-block` error states fall back to `{colors.accent-tomato}` `#ff2201` (3.83:1 on `canvas`), an integration-logo accent promoted to a semantic role because this palette holds no error tone. | [A70-supabase.md](reports/A70-supabase.md) |
| `cursor` | 3.84:1 | — | Cheaper fix, no hex change: swap the label to `{colors.ink}`, which measures **4.86:1 on the real gold** and passes. | [A17-cursor.md](reports/A17-cursor.md) |
| `notion` | 4.19:1 | `#0070d4` (4.52:1) | **`link-blue` #0075de on `surface`** — 4.19:1. | [A46-notion.md](reports/A46-notion.md) |
| `nintendo-2001` | 4.23:1 | — | Usage note: none of these is actually drawn on bare canvas in the extracted layout — `ink-soft` and `error` appear on `platinum` (5.65:1) and `surface` (7.60:1/4.80:1); `hairline` borders white and platinum controls (6.09:1, 4.52:1); `mute… | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `webflow` | 4.32:1 | — | **`{colors.accent-red}` at 4.32:1** for validation text. | [A80-webflow.md](reports/A80-webflow.md) |
| `airbnb` | 4.89:1 | — | *Nearest passing value:* `{colors.primary-active}` **#e00b41 → 4.89:1** — already a documented token in this file, so a build can switch the fill without inventing a colour. (For reference, #d7254a is 4.94:1.) | [A02-airbnb.md](reports/A02-airbnb.md) |
| `kraken` | 6.66:1 | — | Defensible usage note: decorative dividers and section rules only, never the sole boundary of a control. | [A30-kraken.md](reports/A30-kraken.md) |
| `mastercard` | 16.25:1 | — | **`focus` and `focus-on-ink` are prescribed, not extracted.** Mastercard's real focus treatment was never captured. | [A34-mastercard.md](reports/A34-mastercard.md) |
| `zapier` | 17.65:1 | — | **`{colors.focus}` as a prescribed ring.** The hex is a brand fact; its use as a focus ring is this audit's prescription, and the 2px offset is load-bearing (0.01 of margin on `canvas-soft`, and identical to the fill on `button-primary`). | [A84-zapier.md](reports/A84-zapier.md) |
| `ollama` | 21.00:1 | — | **`{colors.focus-ring-strong}` `#3b82f6` is prescribed.** It is the extracted ring's own `rgb(59,130,246)` with the alpha dropped, so no new hue enters a system whose stated rule is "don't add brand colors" — but the live site does not dra… | [A48-ollama.md](reports/A48-ollama.md) |
| `1win` | — | — | **`hairline-strong` #77797d is a prescribed value, not an extracted one.** It is labelled as such in the file. | [A01-1win.md](reports/A01-1win.md) |
| `1win` | — | — | **`focus` #4da3ff is prescribed.** Chosen as a lifted step of the brand blue so the ring stays identifiably 1win rather than a generic system blue. | [A01-1win.md](reports/A01-1win.md) |
| `apple` | — | — | **Three prescribed focus tokens and the whole `motion:` group** are inferences, not extractions. | [A05-apple.md](reports/A05-apple.md) |
| `bmw-m` | — | — | **Prescribed tokens, flagged for sign-off because they are inventions, not extractions:** `{colors.focus}` #2b7de9 and `{colors.hairline-control}` #767676. | [A07-bmw-m.md](reports/A07-bmw-m.md) |
| `bmw` | — | — | **Three prescribed colour tokens added to a frontmatter that otherwise holds only extracted hexes:** `focus` #0a1929, `focus-on-dark` #ffffff, `hairline-control` #8a8a8a. | [A08-bmw.md](reports/A08-bmw.md) |
| `claude` | — | — | **`hairline-strong` #848075 is an invented hex.** Prescribed, not extracted. | [A11-claude.md](reports/A11-claude.md) |
| `clay` | — | — | **Prescribed values introduced, listed for the record:** `{colors.focus}` #c2185b, `{colors.focus-inset}` #fffaf0, `{colors.hairline-strong}` #7a736a, the whole `motion:` group, the `shadow:` group, and `{component.text-input-error}`. | [A12-clay.md](reports/A12-clay.md) |
| `clickhouse` | — | — | **Prescribed `{colors.focus}` #7a7f10 and `{colors.border-control}` #6e6e6e.** Neither was sampled from ClickHouse. | [A13-clickhouse.md](reports/A13-clickhouse.md) |
| `cohere` | — | — | **`focus-on-dark` `#ffad9b` is prescribed for this file.** No focus ring was observed on Cohere's live pages, so both ring colours and the geometry (2px ring, 2px offset, two-tone over photography) are specifications. | [A14-cohere.md](reports/A14-cohere.md) |
| `coinbase` | — | — | **`{colors.hairline-strong}` #767b85.** Prescribed, not extracted. | [A15-coinbase.md](reports/A15-coinbase.md) |
| `composio` | — | — | **The whole Interaction States table and the whole motion system are prescribed.** If the owner holds captures of real hover or dropdown behaviour, these should be replaced with extracted values. | [A16-composio.md](reports/A16-composio.md) |
| `dell-1996` | — | — | **Three prescribed hexes now sit in `colors:`** — `{colors.focus}` #000000, `{colors.focus-on-dark}` #ffffff and `{colors.text-muted}` #666666. | [A18-dell-1996.md](reports/A18-dell-1996.md) |
| `elevenlabs` | — | — | **`colors.focus` #78716c, `colors.hairline-control` #8a8580 and `colors.muted-strong` #757068 are inventions.** ElevenLabs documents no focus ring and no accessible boundary tone. | [A20-elevenlabs.md](reports/A20-elevenlabs.md) |
| `figma` | — | — | **`{shadow.modal}` = `0 24px 64px rgba(0,0,0,0.18)`** is prescribed, not extracted. | [A23-figma.md](reports/A23-figma.md) |
| `framer` | — | — | **Three prescribed colour tokens and an entire prescribed motion system** now sit in a file that otherwise documents extracted facts. | [A24-framer.md](reports/A24-framer.md) |
| `hp` | — | — | **`hairline-control` `#767676` is an invented value**, not an HP colour. | [A26-hp.md](reports/A26-hp.md) |
| `intercom` | — | — | **`hairline-strong: "#857f75"` is a prescribed token, not an extracted one.** It is labelled as prescribed in the file. | [A28-intercom.md](reports/A28-intercom.md) |
| `intercom` | — | — | **`focus: "#0007cb"` and `focus-on-dark: "#65b5ff"` reuse extracted brand hexes for a role the brand does not document.** The hexes are real (`brand-blue`, `report-blue`); their use as focus rings is prescribed. | [A28-intercom.md](reports/A28-intercom.md) |
| `linear.app` | — | — | **Prescribed tokens awaiting sign-off**, all labelled prescribed in the file and in Known Gaps: `focus` #dfe3fb, `focus-on-light` #5e6ad2, `hairline-control` #6a6e78. | [A32-linear.app.md](reports/A32-linear.app.md) |
| `mistral.ai` | — | — | **Prescribed focus tokens.** `focus` #8f2600 and `focus-on-dark` #fff8e0 are added by this audit; the brand ships no visible ring. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `mistral.ai` | — | — | **Prescribed interaction states.** Hover, focus-visible, loading, selected and error treatments on 40 components are inferred from the palette, not observed. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `mongodb` | — | — | **Both focus tokens and the 2px/2px ring geometry are prescribed**, as is `hairline-control`. | [A41-mongodb.md](reports/A41-mongodb.md) |
| `mydealz` | — | — | **`hairline-strong` #8a8d91 is a new prescribed colour**, not a brand tone. | [A42-mydealz.md](reports/A42-mydealz.md) |
| `nerdwallet` | — | — | **The three prescribed tokens themselves** — `{colors.focus}` #003d28, `{colors.focus-on-dark}` #f2ffd6, `{colors.boundary-strong}` #8e9094 — are invented values in a document whose purpose is to record real ones. | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `nintendo-2001` | — | — | **Prescribed, not approved:** `focus: #13275e` and `focus-on-dark: #ecab37` are inventions of this audit, as is the entire state and motion ladder. | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `nvidia` | — | — | **`{colors.focus}` #5a8d00 is prescribed, not extracted.** NVIDIA documents no focus ring anywhere. | [A47-nvidia.md](reports/A47-nvidia.md) |
| `nvidia` | — | — | **The Component States table is largely prescribed.** NVIDIA's documented system policy is that hover states do not exist. | [A47-nvidia.md](reports/A47-nvidia.md) |
| `ollama` | — | — | **Hover, loading and selected behaviour across 10 components is prescribed, not observed.** Marked (P) throughout the state matrix and recorded in Known Gaps. | [A48-ollama.md](reports/A48-ollama.md) |
| `oracle` | — | — | **`{colors.focus-on-dark}` #9ad5e8 — new prescribed token.** Required by SPEC §1's two-ring rule. | [A50-oracle.md](reports/A50-oracle.md) |
| `oracle` | — | — | **Interaction States are almost entirely prescribed.** Only `{colors.primary-pressed}` and `{components.subnav-active-bar}` are extracted. | [A50-oracle.md](reports/A50-oracle.md) |
| `pinterest` | — | — | **Prescribed hover / loading / error / saved-pin states.** The file's own policy line says hover is undocumented. | [A52-pinterest.md](reports/A52-pinterest.md) |
| `posthog` | — | — | **The whole Motion & Animation section and the prescribed half of the States matrix** are the audit's prescriptions, not observations, and are open to being overruled wholesale. | [A54-posthog.md](reports/A54-posthog.md) |
| `renault` | — | — | **Two focus rings, both prescribed.** `{colors.focus}` = `#000000` and `{colors.focus-on-dark}` = `#ffed00` reuse existing palette values and introduce no new colour, but Renault has published no focus treatment that was captured here. | [A56-renault.md](reports/A56-renault.md) |
| `resend` | — | — | **The two prescribed focus rings.** `{colors.focus}` `#3b9eff` and `{colors.focus-on-light}` `#0075ff`. | [A58-resend.md](reports/A58-resend.md) |
| `sap` | — | — | **Prescribed state matrix.** Eighteen rows of interaction states, none extracted. | [A62-sap.md](reports/A62-sap.md) |
| `shopify` | — | — | **Focus-ring geometry.** The 2px stroke and 2px outer offset are prescribed, not extracted. | [A64-shopify.md](reports/A64-shopify.md) |
| `shopify` | — | — | **All motion values**, as prescribed from the Cinematic profile, and all hover / disabled / loading / selected / error treatments in `## Components`. | [A64-shopify.md](reports/A64-shopify.md) |
| `stripe` | — | — | **The prescribed `error` tone.** `{colors.ruby}` `#ea2261` is documented as a gradient and chart accent, never a state colour. | [A69-stripe.md](reports/A69-stripe.md) |
| `supabase` | — | — | **Prescribed `nav-bar-light` selected underline.** A 2px `{colors.primary}` underline on the current route is the one new non-CTA use of emerald in the file. | [A70-supabase.md](reports/A70-supabase.md) |
| `superhuman` | — | — | **A semantic error tone.** The Don'ts forbid any accent beyond indigo / violet-soft / teal / warm greys, so the prescribed error state uses `{colors.primary}` and copy alone. | [A71-superhuman.md](reports/A71-superhuman.md) |
| `superhuman` | — | — | **Both focus rings are prescribed.** `focus` reuses `{colors.primary}` and `focus-on-dark` reuses `{colors.surface-violet-soft}`; neither is a new brand colour, but the brand has never shipped a ring and should confirm the geometry (2px ri… | [A71-superhuman.md](reports/A71-superhuman.md) |
| `together.ai` | — | — | **Both focus rings are prescribed**, including the 2 px width and 2 px offset. | [A74-together.ai.md](reports/A74-together.ai.md) |
| `uber` | — | — | **Applying `{colors.black-elevated}` to the hover state of other ink pills.** Extracted for one control (the hero tab pill) only; extending it is prescribed consistency. | [A75-uber.md](reports/A75-uber.md) |
| `vercel` | — | — | **The focus ring itself.** `{colors.focus}` reuses the existing `#0070f3` so no brand colour is invented, but the 2 px width, the 2 px offset and the "control radius + 2 px" corner rule are all prescribed — the captured surfaces record no… | [A76-vercel.md](reports/A76-vercel.md) |
| `x.ai` | — | — | **Prescribed focus ring.** `{colors.focus}` `#ffffff`, 2px outside the control with a 2px `{colors.canvas}` offset. | [A83-x.ai.md](reports/A83-x.ai.md) |

## Change an extracted hex to reach the threshold

78 items across 36 files.

| Site | Worst ratio named | Proposed value | Item | Report |
|---|---:|---|---|---|
| `notion` | 1.09:1 | `#918c85` (3.34:1) | **`hairline` #e5e3df as the universal card border** — 1.28:1 on canvas. | [A46-notion.md](reports/A46-notion.md) |
| `airbnb` | 1.19:1 | `#959595` (3.00:1) | **Hairline family — nothing in it passes 3:1.** #dddddd 1.36:1, #ebebeb 1.19:1, #c1c1c1 1.80:1. | [A02-airbnb.md](reports/A02-airbnb.md) |
| `ibm` | 1.20:1 | `#949494` (3.03:1) | **`colors.hairline` #e0e0e0 at 1.32:1 on canvas, 1.2:1 on surface.** Nearest passing value for a 3:1 boundary is #949494 (3.03:1 on white); Carbon's own `$border-strong-01` #8d8d8d reaches only 3.32:1 on white and 3.02:1 on #f4f4f4, so eve… | [A27-ibm.md](reports/A27-ibm.md) |
| `cal` | 1.24:1 | `#868d97` (3.35:1) | **`colors.hairline` #e5e7eb on canvas, 1.24:1 (required 3.0:1).** Not changed. | [A10-cal.md](reports/A10-cal.md) |
| `starbucks` | 1.24:1 | `#949494` (3.03:1) | **`{colors.border-hairline}` #e7e7e7 on the nutrition table**, 1.24:1 on white. | [A68-starbucks.md](reports/A68-starbucks.md) |
| `bmw` | 1.25:1 | `#e6e6e6` (1.25:1), `#cccccc` (1.61:1) | **`colors.hairline` #e6e6e6 (1.25:1) and `colors.hairline-strong` #cccccc (1.61:1).** Extracted; not changed, per SPEC's frozen-value rule. | [A08-bmw.md](reports/A08-bmw.md) |
| `raycast` | 1.29:1 | `#646869` (3.55:1) | **`{colors.hairline}` #242728 as a control boundary.** 1.33:1 on canvas, 1.29:1 on surface, against a 3:1 non-text minimum. | [A55-raycast.md](reports/A55-raycast.md) |
| `expo` | 1.35:1 | `#86888f` (3.54:1) | **Hairline ladder #f5f5f7 / #f0f0f3 / #dcdee0 — 1.09 / 1.14 / 1.35:1, needs 3:1.** Nearest passing value #86888f (3.54:1), added as `border-control`. | [A21-expo.md](reports/A21-expo.md) |
| `airtable` | 1.36:1 | `#949494` (3.03:1), `#888888` (3.54:1) | **`colors.hairline` #dddddd — 1.36:1 on white, needs 3.0:1.** Not changed. | [A03-airtable.md](reports/A03-airtable.md) |
| `superhuman` | 1.56:1 | `#6d6885` (3.03:1) | **Dark-ground divider.** `{colors.hairline-dark}` on `{colors.primary}` is 1.56:1. | [A71-superhuman.md](reports/A71-superhuman.md) |
| `notion` | 1.59:1 | `#918c85` (3.34:1) | **`hairline-strong` #c8c4be as the `text-input` border** — 1.74:1 on canvas, 1.59:1 on surface, against the 3:1 of WCAG 1.4.11. | [A46-notion.md](reports/A46-notion.md) |
| `vodafone` | 1.66:1 | `#959595` (3.0:1), `#8c8c8c` (3.0:1) | **`{colors.mute}` #bebebe as text.** 1.86:1 / 1.66:1. | [A77-vodafone.md](reports/A77-vodafone.md) |
| `mistral.ai` | 1.69:1 | `#949494` (3.03:1) | **Three hairline tones at 1.12–1.69:1, needing 3:1.** Left frozen and scoped to decoration. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `notion` | 1.82:1 | `#73706a` (4.94:1) | **`muted` #bbb8b1 as placeholder text** — 1.98:1 on canvas, 1.82:1 on surface. | [A46-notion.md](reports/A46-notion.md) |
| `bmw` | 2.15:1 | `#22c55e` (2.28:1), `#f59e0b` (2.15:1) | **`colors.success` #22c55e (2.28:1) and `colors.warning` #f59e0b (2.15:1) on canvas.** Extracted; not changed. | [A08-bmw.md](reports/A08-bmw.md) |
| `oura` | 2.19:1 | `#707072` (4.94:1) | **`colors.mute` #a8a5a0 — 2.19:1 on canvas (needs 4.5:1).** Nearest passing on cream: #707072 (4.94:1). | [A51-oura.md](reports/A51-oura.md) |
| `theverge` | 2.35:1 | `#5a7bc9` (4.52:1) | **`link-hover` #3860be — 3.17:1 on canvas, 2.35:1 on slate**, applied to every link on the site. | [A73-theverge.md](reports/A73-theverge.md) |
| `dji` | 2.38:1 | `#9a5100` (5.91:1) | **`option-badge` — white on `badge-orange` #fa8c16, 2.38:1 (needs 4.5:1 at 12px/600).** The worst failure in the file. | [A19-dji.md](reports/A19-dji.md) |
| `expo` | 2.39:1 | `#b3261e` (6.54:1) | **`semantic-error` #eb8e90 — 2.39:1, needs 4.5:1.** Nearest passing value #b3261e (6.54:1), added as `semantic-error-text`. | [A21-expo.md](reports/A21-expo.md) |
| `airtable` | 2.41:1 | `#2a8f33` (4.14:1) | **`colors.success-border` #39bf45 — 2.41:1.** Not changed. | [A03-airtable.md](reports/A03-airtable.md) |
| `nvidia` | 2.41:1 | `#528400` (4.51:1) | **`{component.button-ghost-link}`: `{colors.primary}` #76b900 label on `{colors.canvas}` #ffffff — 2.41:1, needs 4.5:1.** Nearest passing green in the brand family: **#528400** (4.51:1 on white, 4.66:1 on black). | [A47-nvidia.md](reports/A47-nvidia.md) |
| `sentry` | 2.42:1 | `#d13f70` (4.56:1) | **`accent-pink` as a chart-point colour.** #fa7faa is **2.42:1** on the light canvas, below the 3:1 of 1.4.11 for meaningful non-text graphics. | [A63-sentry.md](reports/A63-sentry.md) |
| `superhuman` | 2.45:1 | `#5a5772` (2.45:1), `#8e8aa6` (4.52:1) | **Usage note for `{colors.on-dark-faint}` #5a5772 (2.45:1 on `{colors.primary}`).** Nearest passing value on the indigo: **#8e8aa6** (4.52:1). | [A71-superhuman.md](reports/A71-superhuman.md) |
| `mintlify` | 2.48:1 | `#4a6f94` (5.26:1) | **`on-dark` #ffffff on `hero-sky-from` #87a8c8 — `hero-band-sky`, 2.48:1** (needs 4.5:1; fails the 3:1 large-text threshold too, even at 72px). | [A38-mintlify.md](reports/A38-mintlify.md) |
| `theverge` | 2.48:1 | `#6e29ff` (3.03:1) | **`ultraviolet` #5200ff as a 1px boundary = 2.48:1**, including as the sole signal of the input error state. | [A73-theverge.md](reports/A73-theverge.md) |
| `dji` | 2.54:1 | `#767676` (4.54:1) | **`steel` #9fa3a6 on canvas, 2.54:1 (needs 4.5:1).** Comparison-table spec captions at 14px/400. | [A19-dji.md](reports/A19-dji.md) |
| `coinbase` | 2.80:1 | `#047a49` (4.57:1) | **`{colors.semantic-up}` #05b169.** 2.8:1 on white — fails AA as text at every size, and the file mandates it as text colour only. | [A15-coinbase.md](reports/A15-coinbase.md) |
| `bmw` | 2.81:1 | `#767676` (4.54:1), `#949494` (3.03:1) | **`colors.muted-soft` #9a9a9a at 2.81:1 on canvas.** Extracted; not changed. | [A08-bmw.md](reports/A08-bmw.md) |
| `expo` | 2.85:1 | `#6b6f76` (5.05:1) | **`muted` #999999 — 2.85:1 on white, needs 4.5:1.** Nearest passing value #6b6f76 (5.05:1), added alongside as `muted-strong`. | [A21-expo.md](reports/A21-expo.md) |
| `clickhouse` | 2.87:1 | `#7a7a7a` (4.61:1), `#606060` (3.15:1) | **`{colors.muted-soft}` #5a5a5a at 2.87:1 on canvas.** Extracted value, documented as "tertiary text — fine print." It fails AA for normal text (4.5:1) and also fails the 3:1 large-text threshold, so no usage note rescues it as written. | [A13-clickhouse.md](reports/A13-clickhouse.md) |
| `linear.app` | 2.87:1 | `#646ec4` (4.60:1) | **`button-primary-hover`: white label on `#828fff` at 2.87:1.** Both hexes are extracted. | [A32-linear.app.md](reports/A32-linear.app.md) |
| `bmw` | 2.90:1 | `#858585` (3.69:1) | **`hairline-control` on `surface-strong` is 2.90:1**, just under 3.0. | [A08-bmw.md](reports/A08-bmw.md) |
| `superhuman` | 2.91:1 | `#9a9794` (2.91:1), `#767472` (4.51:1) | **Usage note for `{colors.ink-faint}` #9a9794 (2.91:1).** Defensible as written only if scoped to disabled controls (no WCAG minimum) or to 24px+ text where 3:1 applies. | [A71-superhuman.md](reports/A71-superhuman.md) |
| `bmw-m` | 2.92:1 | `#0066b1` (3.54:1), `#0653b6` (2.92:1) | **`{colors.m-blue-light}` #0066b1 (3.54:1) and `{colors.electric-blue}` #0653b6 (2.92:1) on `{colors.canvas}` fail as text.** Not changed; both are brand hexes. | [A07-bmw-m.md](reports/A07-bmw-m.md) |
| `airtable` | 2.93:1 | `#8f949d` (3.05:1) | **`colors.border-strong` #9297a0 — 2.93:1, needs 3.0:1.** Not changed, 0.07 short. | [A03-airtable.md](reports/A03-airtable.md) |
| `notion` | 2.93:1 | `#157a28` (5.46:1) | **`semantic-success` #1aae39 as text on canvas** — 2.93:1. | [A46-notion.md](reports/A46-notion.md) |
| `spacex` | 2.93:1 | `#8c8c99` (3.32:1), `#767680` (4.49:1) | Nearest passing value if the brand insists on a pale cool hairline: **#8c8c99** (3.32:1 on white, but still only 2.93:1 on `canvas-cool`) or **#767680** (4.49:1 / 3.97:1, passes on both). | [A66-spacex.md](reports/A66-spacex.md) |
| `tesla` | 2.98:1 | `#767676` (4.54:1) | **Silver Fog as placeholder text.** #8E8E8E measures 3.28:1 on the canvas and 2.98:1 on Light Ash. | [A72-tesla.md](reports/A72-tesla.md) |
| `apple` | 3.00:1 | `#767679` (4.50:1) | **`{colors.ink-muted-48}` #7a7a7a at 4.29:1 on canvas, 3.94:1 on parchment.** Not changed. | [A05-apple.md](reports/A05-apple.md) |
| `bmw-m` | 3.00:1 | `#828282` (4.53:1), `#8c8c8c` (5.18:1) | **`{colors.muted}` #7e7e7e on `{colors.surface-card}` #1a1a1a — 4.29:1, needs 4.5:1.** Nearest passing value on that surface: **#828282** (4.53:1), or **#8c8c8c** (5.18:1 on `surface-card`, 4.50:1 on `surface-elevated`) to clear both card… | [A07-bmw-m.md](reports/A07-bmw-m.md) |
| `bugatti` | 3.00:1 | `#757575` (4.56:1) | **`colors.muted-soft` #666666 — 3.66:1 on `canvas`, required 4.5:1.** Extracted brand tone, used at 14px for legal and copyright lines. | [A09-bugatti.md](reports/A09-bugatti.md) |
| `cal` | 3.00:1 | `#1d4ed8` (6.70:1) | **`colors.brand-accent` #3b82f6 — white text on it, 3.68:1 (required 4.5:1).** Not changed; it is the extracted brand hue. | [A10-cal.md](reports/A10-cal.md) |
| `cal` | 3.00:1 | `#757575` (4.61:1) | **`colors.muted-soft` #898989 on canvas, 3.50:1.** Not changed. | [A10-cal.md](reports/A10-cal.md) |
| `clay` | 3.00:1 | `#d13f72` (4.50:1) | **`on-primary` #ffffff on `brand-pink` #ff4d8b — 3.14:1, needs 4.5:1.** This is a real combination on the live site: white copy on the hot-pink feature card. | [A12-clay.md](reports/A12-clay.md) |
| `clickhouse` | 3.00:1 | `#8e8e8e` (4.74:1) | **`{colors.muted}` #888888 on `{colors.surface-elevated}` #242424 at 4.38:1.** Fails 4.5:1 by a hair. | [A13-clickhouse.md](reports/A13-clickhouse.md) |
| `coinbase` | 3.00:1 | `#5b616e` (6.21:1), `#6e737b` (4.51:1) | **`{colors.muted}` as general secondary text.** 3.88:1 / 3.62:1. | [A15-coinbase.md](reports/A15-coinbase.md) |
| `composio` | 3.00:1 | `#8a8a8a` (4.61:1) | **`muted` #888888 on `surface-card-elevated` at 4.49:1** — no hex change proposed. | [A16-composio.md](reports/A16-composio.md) |
| `composio` | 3.00:1 | `#949494` (6.32:1) | **`muted-soft` #666666 kept frozen.** Nearest passing value for body text: #949494 (6.32:1 canvas / 5.85:1 surface-card). | [A16-composio.md](reports/A16-composio.md) |
| `dji` | 3.00:1 | `#767676` (4.54:1) | **`ink-tertiary` #8c8c8c on canvas, 3.36:1 (needs 4.5:1).** 14px tile eyebrows. | [A19-dji.md](reports/A19-dji.md) |
| `elevenlabs` | 3.00:1 | `#757068` (4.51:1) | **`colors.muted` #777169 on `colors.canvas` #f5f5f5 — 4.43:1, needs 4.5:1.** Nearest passing value: **#757068** (4.51:1), a two-step darkening, visually indistinguishable. | [A20-elevenlabs.md](reports/A20-elevenlabs.md) |
| `expo` | 3.00:1 | `#3f61e8` (4.78:1) | **`text-link-secondary` #476cff — 4.32:1, needs 4.5:1.** Nearest passing value #3f61e8 (4.78:1). | [A21-expo.md](reports/A21-expo.md) |
| `hashicorp` | 3.00:1 | `#7d828e` (5.46:1) | **`ink-subtle` #656a76** — 3.88:1 on canvas, 3.28:1 on charcoal, required 4.5:1. | [A25-hashicorp.md](reports/A25-hashicorp.md) |
| `hashicorp` | 3.00:1 | `#000000` (4.73:1), `#d9271a` (4.61:1) | **`ink` on `product-consul`** — 4.44:1, required 4.5:1, short by 0.06. | [A25-hashicorp.md](reports/A25-hashicorp.md) |
| `ibm` | 3.00:1 | `#767676` (4.54:1) | **`colors.ink-subtle` #8c8c8c at 3.36:1 on canvas.** Nearest passing value is #767676 (4.54:1 on white); Carbon's `$text-helper` #6f6f6f reaches 5.02:1 and would pass. | [A27-ibm.md](reports/A27-ibm.md) |
| `kraken` | 3.00:1 | `#9194a6` (3.00:1) | Nearest passing for the 3:1 large-text threshold: **#9194a6** (3.00:1) — a change of 3 steps in each channel. | [A30-kraken.md](reports/A30-kraken.md) |
| `linear.app` | 3.00:1 | `#5f6bd4` (4.51:1) | **`primary` #5e6ad2 as link ink on the canvas: 4.44:1, short by 0.06.** Nearest passing value is **#5f6bd4 (4.51:1)**. | [A32-linear.app.md](reports/A32-linear.app.md) |
| `notion` | 3.00:1 | `#c24e00` (4.79:1) | **`badge-orange` white on #dd5b00** — 3.77:1 at 13px/600. | [A46-notion.md](reports/A46-notion.md) |
| `nvidia` | 3.00:1 | `#c25400` (4.6:1) | **`{colors.warning}` #df6500 on `{colors.canvas}` — 3.5:1, needs 4.5:1.** Nearest passing: **#c25400** (4.6:1). | [A47-nvidia.md](reports/A47-nvidia.md) |
| `runwayml` | 3.00:1 | `#646b76` (4.54:1) | **`text-secondary` #767d88 as body/label text on `surface-dark` (4.19:1) and on the light surfaces (4.12:1 / 3.51:1).** This is Runway's documented secondary text colour and its own example prompt specifies it on both polarities. | [A60-runwayml.md](reports/A60-runwayml.md) |
| `vodafone` | 3.00:1 | `#767676` (4.54:1), `#6e6e6e` (4.55:1) | **`{colors.body}` #7e7e7e as normal-size text.** 4.06:1 on `{colors.canvas}`, 3.63:1 on `{colors.canvas-soft}`; AA needs 4.5:1. | [A77-vodafone.md](reports/A77-vodafone.md) |
| `wired` | 3.00:1 | `#707070` (4.54:1) | **`{colors.body}` #757575 on `{colors.canvas-soft}` #f5f5f5 at 4.23:1.** Nearest passing grey: #707070 (4.54:1 on canvas-soft, 4.95:1 on canvas). | [A81-wired.md](reports/A81-wired.md) |
| `1win` | 3.01:1 | `#606266` (3.01:1) | Nearest passing value: **#606266** (3.01:1) or the #77797d added here as `hairline-strong` (4.22:1 on canvas, 3.03:1 on surface). | [A01-1win.md](reports/A01-1win.md) |
| `apple` | 3.02:1 | `#0075e4` (4.50:1) | **`{colors.primary-on-dark}` #2997ff — white on it measures 3.02:1, required 4.5:1.** Not changed; it is Sky Link Blue, a real brand hex. | [A05-apple.md](reports/A05-apple.md) |
| `linear.app` | 3.02:1 | `#7c828a` (5.38:1) | **`ink-tertiary` #62666d below AA on every surface (3.62:1 down to 3.02:1).** Nearest value passing 4.5:1 on all four surfaces and the canvas is about **#7c828a** (5.38:1 on canvas, 4.91:1 on surface-1, 4.50:1 on surface-4). | [A32-linear.app.md](reports/A32-linear.app.md) |
| `kraken` | 3.06:1 | `#939397` (3.06:1) | Nearest passing: **#939397** (3.06:1). | [A30-kraken.md](reports/A30-kraken.md) |
| `expo` | 3.30:1 | `#157f3c` (4.52:1) | **`semantic-success` #16a34a — 3.30:1, needs 4.5:1.** Nearest passing value #157f3c (4.52:1). | [A21-expo.md](reports/A21-expo.md) |
| `notion` | 3.77:1 | `#c24e00` (4.79:1) | **`semantic-warning` #dd5b00 as text on canvas** — 3.77:1. | [A46-notion.md](reports/A46-notion.md) |
| `coinbase` | 3.88:1 | `#6e737b` (4.51:1) | **`legal-band` legal text — real AA failure.** `{colors.muted}` #7c828a at 13px on #ffffff is 3.88:1 against 4.5:1 required. | [A15-coinbase.md](reports/A15-coinbase.md) |
| `mongodb` | 3.93:1 | `#009b3d` (4.72:1) | **`button-primary-pressed`: ink on `{colors.primary-pressed}` #008c34 = 3.93:1** (required 4.5:1). | [A41-mongodb.md](reports/A41-mongodb.md) |
| `mintlify` | 3.99:1 | `#b32424` (6.57:1) | **`on-dark` on `brand-error` #d45656 — `badge-required`, 3.99:1.** Nearest passing: **#b32424** (6.57:1) as a label-only error tone, keeping #d45656 for borders and fills. | [A38-mintlify.md](reports/A38-mintlify.md) |
| `dji` | 4.08:1 | `#e01020` (4.92:1) | **`error` #f5222d on canvas, 4.08:1 (needs 4.5:1).** 12px "Out of Stock". | [A19-dji.md](reports/A19-dji.md) |
| `notion` | 4.17:1 | `#73706a` (4.53:1) | **`search-pill` placeholder `steel` on `surface`** — 4.17:1 at 16px, missing AA by 0.33. | [A46-notion.md](reports/A46-notion.md) |
| `cal` | 4.46:1 | `#6d28d9` (7.10:1) | **`colors.ink` on `colors.badge-violet` #8b5cf6, 4.46:1.** Fails by 0.04. | [A10-cal.md](reports/A10-cal.md) |
| `kraken` | 4.51:1 | `#737684` (4.51:1) | Nearest passing for body text: **#737684** (4.51:1). | [A30-kraken.md](reports/A30-kraken.md) |
| `dell-1996` | 4.52:1 | `#e71c29` (4.52:1) | *Nearest passing background:* #e71c29 (4.52:1) — a single step darker and visually indistinguishable, but still a falsified identity hex. | [A18-dell-1996.md](reports/A18-dell-1996.md) |
| `mistral.ai` | 4.52:1 | `#c24000` (4.52:1) | Keeping a white label instead requires darkening the fill to about **#c24000** (4.52:1 with #ffffff), which is no longer Mistral orange. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `kraken` | 4.61:1 | `#118652` (4.61:1) | Nearest passing: **#118652** (4.61:1). | [A30-kraken.md](reports/A30-kraken.md) |
| `1win` | 9.68:1 | `#005021` (9.68:1) | Nearest passing value, keeping white: green darkened to **#005021** (9.68:1) — a different, much heavier green that no longer reads as the brand. | [A01-1win.md](reports/A01-1win.md) |

## Frozen tone disclosed, no change sought

197 items across 68 files.

| Site | Worst ratio named | Proposed value | Item | Report |
|---|---:|---|---|---|
| `airbnb` | 1.00:1 | — | **Focus ring colour is a judgement call, not an extracted value.** #222222 is inferred from the file's own `text-input` focus description (2px ink border). | [A02-airbnb.md](reports/A02-airbnb.md) |
| `playstation` | 1.00:1 | — | **`hairline-light` #f3f3f3 — 1.11:1 on `canvas-light`, 1.00:1 on `surface-soft`.** Nearest passing value is `#949494` (3.00:1 on white). | [A53-playstation.md](reports/A53-playstation.md) |
| `starbucks` | 1.00:1 | — | **The self-coloured 1px borders on the filled pills.** Extracted facts (`1px solid #00754A` on a `#00754A` fill, and the same pattern in black and white) that produce three 1.00:1 artefact failures in the harness. | [A68-starbucks.md](reports/A68-starbucks.md) |
| `vodafone` | 1.00:1 | — | **`button-icon-circular` needs a hairline on light bands.** Over hero photography the white circle reads; on `{colors.canvas}` it is a 1.0:1 edge. | [A77-vodafone.md](reports/A77-vodafone.md) |
| `voltagent` | 1.09:1 | — | **The two-layer surface system.** `{colors.canvas}` and `{colors.canvas-soft}` are 1.09:1 apart. | [A78-voltagent.md](reports/A78-voltagent.md) |
| `clay` | 1.10:1 | — | **Frozen utility tones, no approval sought, listed for completeness:** `{colors.hairline}` 1.21:1 and `{colors.hairline-soft}` 1.10:1 on canvas; `{colors.muted-soft}` 2.70:1 and `{colors.on-dark-soft}` 2.51:1 on canvas; `{colors.success}`… | [A12-clay.md](reports/A12-clay.md) |
| `lovable` | 1.10:1 | — | **`hairline` #eceae4 on `canvas` #f7f4ed — 1.10:1, needs 3.0:1 (WCAG 1.4.11).** | [A33-lovable.md](reports/A33-lovable.md) |
| `figma` | 1.13:1 | — | **`hairline` `#e6e6e6` (1.25:1) and `hairline-soft` `#f1f1f1` (1.13:1) on canvas.** Both frozen and disclosed; no hex change requested. | [A23-figma.md](reports/A23-figma.md) |
| `mastercard` | 1.13:1 | — | **`watermark-ghost` `#E8E2DA` on `canvas-cream` is 1.13:1** against a 3:1 requirement for 72px+ display text. | [A34-mastercard.md](reports/A34-mastercard.md) |
| `apple` | 1.14:1 | — | **`{colors.divider-soft}` #f0f0f0 at 1.14:1.** Not changed and no replacement proposed: the file itself describes it as a ring/halo (`rgba(0, 0, 0, 0.04)`), not a boundary. | [A05-apple.md](reports/A05-apple.md) |
| `nerdwallet` | 1.19:1 | — | **`{colors.hairline}` #ebebec — 1.19:1, needs 3.0.** Nearest passing: #8e9094 at 3.2:1. | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `wise` | 1.20:1 | — | **Layer separation at 1.2:1.** Whether the white-card-on-sage boundary is decorative (current reading, disclosed) or load-bearing. | [A82-wise.md](reports/A82-wise.md) |
| `pinterest` | 1.22:1 | — | **`{colors.hairline}` 1.4:1 / 1.36:1 and `{colors.hairline-soft}` 1.26:1 / 1.22:1.** Left frozen and disclosed. | [A52-pinterest.md](reports/A52-pinterest.md) |
| `slack` | 1.25:1 | — | **The aubergine seam.** `{colors.primary-tint}` `#592466` on `#4a154b` is **1.25:1** for a stated border accent. | [A65-slack.md](reports/A65-slack.md) |
| `nike` | 1.26:1 | — | **`{colors.hairline-soft}` `#e5e5e5` — 1.26:1, needs 3:1.** Nearest passing `#949494` (3.03:1). | [A44-nike.md](reports/A44-nike.md) |
| `lamborghini` | 1.29:1 | — | **`button-black-filled`: text `#202020` on `#000000` — 1.29:1.** Nearest passing value: `#FFFFFF` (21.00:1), or keep the charcoal label and change the fill to `#FFFFFF` (16.29:1), which is what the "Inverted CTA on light sections" usage no… | [A31-lamborghini.md](reports/A31-lamborghini.md) |
| `opencode.ai` | 1.31:1 | — | `hairline` `rgba(15,0,0,0.12)` at 1.31:1 on all three light grounds. | [A49-opencode.ai.md](reports/A49-opencode.ai.md) |
| `kraken` | 1.34:1 | — | **`border-subtle` #dedee5 — 1.34:1 on #ffffff, needs 3.0:1.** | [A30-kraken.md](reports/A30-kraken.md) |
| `1win` | 1.37:1 | — | **`{colors.hairline}` #2d2f33 on `{colors.canvas}` #141415 — 1.37:1, needs 3.0:1.** An extracted decorative value, left untouched. | [A01-1win.md](reports/A01-1win.md) |
| `airbnb` | 1.37:1 | — | **`{component.button-primary-disabled}` white-on-#ffd1da at 1.37:1.** I did not change the component token, but the new Accessibility and Don't sections recommend `{colors.ink}` (11.66:1) for the disabled label. | [A02-airbnb.md](reports/A02-airbnb.md) |
| `hashicorp` | 1.38:1 | — | **The focus ring is two-tone** (`focus` #2b89ff + 1px `focus-inset` #000000) rather than a `focus` / `focus-on-dark` pair. | [A25-hashicorp.md](reports/A25-hashicorp.md) |
| `mastercard` | 1.40:1 | — | **`ink-whisper` `#D1CDC7` on `canvas-cream` is 1.40:1** where the file assigns it to placeholder-like empty-state labels. | [A34-mastercard.md](reports/A34-mastercard.md) |
| `cohere` | 1.41:1 | — | **`hairline` `#d9d9dd` fails the 3:1 boundary threshold** at 1.41:1 on `canvas`. | [A14-cohere.md](reports/A14-cohere.md) |
| `nintendo-2001` | 1.41:1 | — | **The cool-ink-on-periwinkle family: `ink-soft` 2.23:1, `muted-indigo` 1.67:1, `hairline` 1.79:1, `error` 1.41:1, all against `canvas` `#7a8aba`.** | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `binance` | 1.43:1 | — | **`{colors.primary}` #FCD535 as ink on light surfaces.** 1.43:1 on #ffffff. | [A06-binance.md](reports/A06-binance.md) |
| `wise` | 1.46:1 | — | **`{colors.warning}` `#ffd11a` at 1.46:1.** Nearest passing on white would be **`#8c720e`** (4.64:1), which is no longer the brand's yellow — do not apply it. | [A82-wise.md](reports/A82-wise.md) |
| `sentry` | 1.53:1 | — | **`button-ghost-on-dark` has no perceivable edge.** Fill `{colors.on-dark-faint}` at **1.53:1** on the dark canvas, with no border token. | [A63-sentry.md](reports/A63-sentry.md) |
| `playstation` | 1.55:1 | — | **`hairline-dark` and `ash-dark` — both composite to #2e2e2e at 1.55:1 over `canvas-dark`.** Nearest passing value over black is `#5e5e5e` (3.04:1). | [A53-playstation.md](reports/A53-playstation.md) |
| `aljazeera` | 1.59:1 | — | **3px `select-gold` #ffc500 border on white, 1.59:1 against a 3:1 boundary threshold.** Usage note: the border is 3px and decorative-emphatic, but it is also the control's only boundary, so 3:1 applies. | [A04-aljazeera.md](reports/A04-aljazeera.md) |
| `clay` | 1.64:1 | — | **`on-primary` on `brand-lavender` (2.19:1), `brand-peach` (1.78:1), `brand-ochre` (1.83:1), `brand-mint` (1.64:1), `brand-coral` (2.80:1).** These are harness pairings, not documented combinations — the file routes all five to `{colors.in… | [A12-clay.md](reports/A12-clay.md) |
| `nike` | 1.64:1 | — | **`{colors.hairline}` `#cacacb` — 1.64:1 on canvas, needs 3:1.** Nearest passing value `#949494` (3.03:1). | [A44-nike.md](reports/A44-nike.md) |
| `replicate` | 1.66:1 | — | **`{colors.divider-dark}` alpha.** At `0.2` it measures 1.93:1 on `{colors.surface-dark}` and 1.66:1 on `{colors.surface-deep}`. | [A57-replicate.md](reports/A57-replicate.md) |
| `posthog` | 1.75:1 | — | **`stone` `#b6b7af` at 1.75:1 on canvas.** Documented as "least-emphasis caption text". | [A54-posthog.md](reports/A54-posthog.md) |
| `lovable` | 1.78:1 | — | **`ring-brand` rgba(59,130,246,0.5) — 1.78:1 on cream, 2.10:1 on the dark button, needs 3.0:1.** | [A33-lovable.md](reports/A33-lovable.md) |
| `lovable` | 1.78:1 | — | Usage note: there is no usage at which 1.78:1 is defensible for a focus indicator. | [A33-lovable.md](reports/A33-lovable.md) |
| `renault` | 1.95:1 | — | **`{colors.warning}` `#f0ad4e` (1.95:1) and `{colors.success}` `#8dc572` (2.03:1) on `{colors.canvas}`.** Both miss 3.0:1 as well, so no text size rescues them. | [A56-renault.md](reports/A56-renault.md) |
| `expo` | 2.01:1 | — | **`accent-link-bright` #47c2ff — 2.01:1 on white.** Defensible only on `surface-dark`, where it reaches 8.90:1. | [A21-expo.md](reports/A21-expo.md) |
| `meta` | 2.01:1 | — | **`badge-attention` label — real AA failure.** `{colors.canvas}` #ffffff on `{colors.attention}` #f2a918 measures **2.01:1** against 4.5:1 for its 12px `{typography.caption-bold}` label. | [A36-meta.md](reports/A36-meta.md) |
| `aljazeera` | 2.02:1 | — | **White on `rail-teal` #00cbca, 2.02:1.** The rotated rail labels are large display type, so the applicable threshold is 3:1 — and 2.02:1 misses that too. | [A04-aljazeera.md](reports/A04-aljazeera.md) |
| `sanity` | 2.02:1 | — | **`accent-blue` `#0052ef` as link ink on dark.** 3.24:1 on canvas, 2.65:1 on `#212121`, 2.02:1 on `#353535`. | [A61-sanity.md](reports/A61-sanity.md) |
| `raycast` | 2.03:1 | — | **`{colors.stone}` #434345 as caption text.** 2.03:1 on canvas against 4.5:1. | [A55-raycast.md](reports/A55-raycast.md) |
| `vercel` | 2.03:1 | — | **`{colors.warning}` `#f5a623` as text.** 2.03:1 — it fails AA and also fails the 3:1 large-text bar, so no minimum text size rescues it. | [A76-vercel.md](reports/A76-vercel.md) |
| `aljazeera` | 2.04:1 | — | **`amber` #ffa000 active nav links on white, 2.04:1.** Nearest passing value from the existing palette: `{colors.graphite}` #323232 at 12.82:1 with amber kept as a 3px underline, which preserves the gilded identity at zero contrast cost. | [A04-aljazeera.md](reports/A04-aljazeera.md) |
| `starbucks` | 2.08:1 | — | **`{colors.gold}` #cba258 as a text colour on light grounds**, 2.08:1 on canvas and 2.20:1 on its own partnership wash. | [A68-starbucks.md](reports/A68-starbucks.md) |
| `theverge` | 2.09:1 | — | **`button-primary` hover label — #000000 on `rgba(255,255,255,0.2)` over the canvas, composited #424242 = 2.09:1.** Nearest passing value: invert the label to `{colors.text}` #ffffff, which measures **10.05:1** on the same fill. | [A73-theverge.md](reports/A73-theverge.md) |
| `clay` | 2.10:1 | — | **Focus ring on `brand-lavender` and `brand-coral`.** Neither band of the composite ring reaches 3:1 against those two fills (outer 2.68:1 / 2.10:1, inner 2.11:1 / 2.69:1), and no single luminance can clear 3:1 against both `{colors.primar… | [A12-clay.md](reports/A12-clay.md) |
| `replicate` | 2.10:1 | — | **Replacing the shipped focus ring.** `{colors.focus}` and `{colors.focus-on-dark}` reuse tones the palette owns and are measured in `## Accessibility`, but adopting them means the product stops drawing the blue `{colors.ring-focus}` it cu… | [A57-replicate.md](reports/A57-replicate.md) |
| `binance` | 2.13:1 | — | **White labels on the trading buttons.** `{component.button-trading-up}` and `{component.button-trading-down}` declare `{colors.on-dark}` (#ffffff): **2.13:1** on #0ecb81 and **3.53:1** on #f6465d, against 4.5:1. | [A06-binance.md](reports/A06-binance.md) |
| `x.ai` | 2.13:1 | — | **The outline pill's `rgba(255, 255, 255, 0.25)` border, at 2.13:1 over canvas.** This is the brand's single most-used interactive edge. | [A83-x.ai.md](reports/A83-x.ai.md) |
| `nintendo-2001` | 2.14:1 | — | **White `{typography.display}` on `lavender` `#acace7` — 2.14:1, needs 3.0** (`hero-panel`, Home only). | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `cal` | 2.15:1 | — | **`colors.error` / `success` / `warning` as text, 3.76 / 2.54 / 2.15:1.** Not changed. | [A10-cal.md](reports/A10-cal.md) |
| `uber` | 2.19:1 | — | **`mute` `#afafaf` on light grounds.** Extracted and unchanged. | [A75-uber.md](reports/A75-uber.md) |
| `miro` | 2.23:1 | — | **`muted` `#a5a8b5` as secondary text — 2.37:1 on canvas, 2.23:1 on surface (needs 4.5:1).** Nearest passing: `#6f727e` (4.79:1 / 4.51:1). | [A39-miro.md](reports/A39-miro.md) |
| `airtable` | 2.25:1 | — | **White type on `colors.signature-mustard` — 2.25:1.** Not a change request; the file now says ink-on-mustard (7.51:1) only. | [A03-airtable.md](reports/A03-airtable.md) |
| `slack` | 2.25:1 | — | **The focus system is a prescription.** Both rings reuse palette hexes, but ring existence, 2px width and 2px offset (1px on `text-input`) are proposals. | [A65-slack.md](reports/A65-slack.md) |
| `webflow` | 2.30:1 | — | **`{colors.mute-soft}` as placeholder text at 2.3:1.** No passing value exists in this role without abandoning the tone; nearest passing grey is `#767676` (4.54:1). | [A80-webflow.md](reports/A80-webflow.md) |
| `aljazeera` | 2.32:1 | — | **`on-primary` on `primary` — white #ffffff on Jazeera orange #fa9000, 2.32:1, needs 4.5:1.** Hex frozen; this is the brand's identity colour. | [A04-aljazeera.md](reports/A04-aljazeera.md) |
| `mistral.ai` | 2.38:1 | — | **`{colors.muted}` at 2.38:1.** No change requested: WCAG sets no contrast requirement on disabled text, and placeholders are never the only label in this system. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `nintendo-2001` | 2.40:1 | — | **White on Signal Orange `#f68d1f` — 2.40:1, needs 4.5** (`button-submit`, `button-icon-arrow`, `button-arrow-chip`). | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `nvidia` | 2.41:1 | — | **`{colors.warning-bright}` #ef9100 on `{colors.canvas}` — 2.41:1.** No usage note rescues it on white. | [A47-nvidia.md](reports/A47-nvidia.md) |
| `lovable` | 2.44:1 | — | **`ink-40` rgba(28,28,28,0.4) -> #9f9e99 on cream — 2.44:1, needs 3.0:1.** | [A33-lovable.md](reports/A33-lovable.md) |
| `lovable` | 2.44:1 | — | Usage note: 2.44:1 is defensible where the border is accompanied by a text label at 4.5:1 or better and is not the only affordance — which describes `button-ghost`, whose label is `ink` at 15.51:1. | [A33-lovable.md](reports/A33-lovable.md) |
| `vercel` | 2.48:1 | — | **`{colors.hairline-strong}` `#a1a1a1` as a boundary.** 2.58:1 / 2.48:1 against 3.0:1 — short by 0.42 and 0.52. | [A76-vercel.md](reports/A76-vercel.md) |
| `notion` | 2.50:1 | — | **`badge-tag-green` #1aae39 on #d9f3e1** — 2.50:1 at 13px/600. | [A46-notion.md](reports/A46-notion.md) |
| `ollama` | 2.52:1 | — | **`{colors.mute}` fails as text at 2.52:1 with no compliant size.** Nearest passing value is `#767676` (4.54:1), which is within 3 units of `{colors.body}` `#737373` and would make the token redundant. | [A48-ollama.md](reports/A48-ollama.md) |
| `mastercard` | 2.53:1 | — | **`accent-signal-light` `#F37338` is 2.53:1 on the canvas** and the file assigns it both to decorative orbital arcs (fine) and to *carousel active indicators* (not fine — that is a position signal below the 3:1 non-text floor). | [A34-mastercard.md](reports/A34-mastercard.md) |
| `together.ai` | 2.54:1 | — | **The same ink on `{colors.hairline}` `#ebebeb` — 2.54:1, required 4.5:1.** This is `data-table-header`, the row that labels the price columns, set at 11 px uppercase mono. | [A74-together.ai.md](reports/A74-together.ai.md) |
| `shopify` | 2.56:1 | — | **`shade-40` on the light track.** 2.56:1 on `canvas-light`, while `## Colors` describes it as tertiary text on light. | [A64-shopify.md](reports/A64-shopify.md) |
| `cohere` | 2.57:1 | — | **`muted` `#93939f` fails AA for body text.** 3.04:1 on `canvas`, 2.71:1 on `card-border`, 2.57:1 on `soft-stone`, against 4.5:1. | [A14-cohere.md](reports/A14-cohere.md) |
| `lamborghini` | 2.58:1 | — | **Ghost button hover: `#FFFFFF` on Teal Action `#1EAEDB` — 2.58:1.** Nearest passing value with the brand's own palette: `{colors.on-accent}` `#000000` on the same teal, 8.13:1. | [A31-lamborghini.md](reports/A31-lamborghini.md) |
| `theverge` | 2.58:1 | — | **`button-primary` focus label — #ffffff on `focus` #1eaedb = 2.58:1.** Nearest passing value: `{colors.on-accent}` #000000 on the same cyan fill = **8.13:1**, which also matches the brand's own rule that black ink belongs on light fills. | [A73-theverge.md](reports/A73-theverge.md) |
| `cohere` | 2.61:1 | — | **`coral` `#ff7759` at 2.61:1 on white** means a 1px coral chip outline is not a sufficient boundary. | [A14-cohere.md](reports/A14-cohere.md) |
| `nike` | 2.67:1 | — | **`{colors.stone}` `#9e9ea0` — 2.67:1 on canvas.** Nearest passing `#767676` (4.54:1). | [A44-nike.md](reports/A44-nike.md) |
| `miro` | 2.70:1 | — | **`badge-success` — white `#ffffff` on `#00b473` at 2.7:1 (needs 4.5:1).** Two routes, both in-palette or near it: swap the label to `{colors.primary}` on the same green, which measures 6.3:1 and changes no brand hex at all (**recommended*… | [A39-miro.md](reports/A39-miro.md) |
| `elevenlabs` | 2.76:1 | — | **Two-tone focus ring over the gradient orbs and over photography.** `{colors.focus}` falls to 2.60–2.76:1 over lavender, sky and rose. | [A20-elevenlabs.md](reports/A20-elevenlabs.md) |
| `revolut` | 2.78:1 | — | **`accent-warning` `#ec7e00` on white.** 2.78:1 — fails the graphical 3:1 threshold as well as the text threshold, so it is not defensible on white at any size. | [A59-revolut.md](reports/A59-revolut.md) |
| `1win` | 2.81:1 | — | **`{colors.on-primary}` #ffffff on `{colors.primary}` #00b24b — 2.81:1, needs 4.5:1.** This is 1win's Registration button, the single most important control on the site. | [A01-1win.md](reports/A01-1win.md) |
| `1win` | 2.81:1 | — | Usage note that would make the real value defensible: *white on green is used only at `{typography.display}` / `{typography.heading}` (33px and 20px at weight 800), where the 3:1 large-text threshold applies.* Note this is **still not enou… | [A01-1win.md](reports/A01-1win.md) |
| `supabase` | 2.81:1 | — | **`{colors.ink-mute-2}` `#9a9a9a` on the light track.** 2.81:1 on `canvas`, so it fails AA at every text size — it does not even reach the 3:1 that applies to 18px+ / 14px-bold large text. | [A70-supabase.md](reports/A70-supabase.md) |
| `sanity` | 2.82:1 | — | **`ink-tertiary` `#797979` inside cards.** 3.70:1 on `#212121`, 2.82:1 on `#353535`. | [A61-sanity.md](reports/A61-sanity.md) |
| `mydealz` | 2.83:1 | — | **`price-lockup` — `primary` on `canvas`, 2.83:1 vs the 3:1 large-text threshold.** Nearest passing value: **`#197e25`** at 4.74:1. | [A42-mydealz.md](reports/A42-mydealz.md) |
| `mydealz` | 2.84:1 | — | **`warm` #fb6001 at 3.1:1 / 2.84:1.** Disclosed with a size restriction (24px+ numerals or icon-plus-text only) rather than changed, since it is a status colour on a small footprint. | [A42-mydealz.md](reports/A42-mydealz.md) |
| `mongodb` | 2.86:1 | — | **`badge-orange`: white on `{colors.accent-orange}` #fa6e39 = 2.86:1** (required 4.5:1; 13px `caption-bold`). | [A41-mongodb.md](reports/A41-mongodb.md) |
| `kraken` | 2.89:1 | — | **`text-secondary` #9497a9 — 2.89:1 on #ffffff, needs 4.5:1.** | [A30-kraken.md](reports/A30-kraken.md) |
| `kraken` | 2.89:1 | — | Defensible usage note, if the hex is frozen: *none exists.* This is the important finding. | [A30-kraken.md](reports/A30-kraken.md) |
| `theverge` | 2.90:1 | — | **The ultraviolet tile's focus ring.** No single tone in the palette clears 3:1 on a full-opacity #5200ff fill (best: `focus` at 2.90:1). | [A73-theverge.md](reports/A73-theverge.md) |
| `pinterest` | 2.92:1 | — | **`{colors.ash}` at 2.92:1 on `{colors.surface-card}`.** Usage note: boundary use is restricted to `{colors.canvas}` grounds. | [A52-pinterest.md](reports/A52-pinterest.md) |
| `wise` | 2.92:1 | — | **`{colors.positive}` `#2ead4b` at 2.92:1.** Nearest passing: **`#24883b`** (4.51:1). | [A82-wise.md](reports/A82-wise.md) |
| `zapier` | 2.92:1 | — | **`{colors.body-mid}` `#939084` as metadata text**, 3.17:1 on canvas and 2.92:1 on canvas-soft. | [A84-zapier.md](reports/A84-zapier.md) |
| `miro` | 2.95:1 | — | **`badge-tag-purple` — `{colors.brand-blue}` on `{colors.surface-pricing-featured}` at 4.33:1 (needs 4.5:1).** Nearest passing: `#3a59f5` (4.88:1), a 0.4% luminance move off the brand blue. | [A39-miro.md](reports/A39-miro.md) |
| `lamborghini` | 2.96:1 | — | **`badge`: `#FFFFFF` on Steel `#969696` at 10px — 2.96:1.** Nearest passing value: `#202020` label on the same steel, 5.51:1 (already proven on `button-gray`). | [A31-lamborghini.md](reports/A31-lamborghini.md) |
| `dji` | 2.98:1 | — | **`link-blue` #1890ff on canvas, 3.24:1 (needs 4.5:1), and 2.98:1 on `fog`.** Every "Learn More ›" and "Buy Now ›" text link at 16px. | [A19-dji.md](reports/A19-dji.md) |
| `1win` | 3.00:1 | — | Usage note that makes the real value defensible: *white on blue is restricted to 14px+ at weight 700/800 — the only weights this system uses — so the 3:1 large-text threshold applies and 4.21:1 clears it comfortably.* Given that every role… | [A01-1win.md](reports/A01-1win.md) |
| `airbnb` | 3.00:1 | — | *Usage note that makes the real value defensible:* 3.52:1 clears the 3:1 threshold for large text (24px regular / 18.66px bold and above) and for non-text UI components, so white on Rausch is acceptable for the `{component.search-orb}` gla… | [A02-airbnb.md](reports/A02-airbnb.md) |
| `binance` | 3.00:1 | — | **`{colors.muted}` #707a8a as secondary text.** 4.34:1 on canvas-light, 4.16:1 on surface-soft-light, 4.46:1 on canvas-dark, 3.65:1 on surface-card-dark. | [A06-binance.md](reports/A06-binance.md) |
| `cursor` | 3.00:1 | — | Usage note that would make the real value defensible: **the 3:1 AA-Large threshold applies only at 24px+, or 18.66px+ at weight 700.** The CTA label is 14px/500 and this brand's own rules forbid bold, so no size note makes #f54e00 + white… | [A17-cursor.md](reports/A17-cursor.md) |
| `dell-1996` | 3.00:1 | — | *Usage note, recommended:* set the panel copy at `{typography.heading-1}` 24px/900, where WCAG's large-text threshold of 3:1 applies and 4.49:1 passes with margin. | [A18-dell-1996.md](reports/A18-dell-1996.md) |
| `figma` | 3.00:1 | — | Usage note that would make the real value defensible as-is: white on `#ff3d8b` clears the 3:1 large-text threshold, so it is acceptable at **24px+, or 18.66px+ at weight 700**. | [A23-figma.md](reports/A23-figma.md) |
| `figma` | 3.00:1 | — | It **passes** the 3:1 non-text minimum that actually applies to a glyph, so I recommend approving no colour change and accepting the mitigation already written into the file: the glyph carries `aria-label="Included"` and the matrix headers… | [A23-figma.md](reports/A23-figma.md) |
| `framer` | 3.00:1 | — | *Nearest passing value, same type colour:* darken the ground to `#e05f20`, which carries white at 3.60:1. | [A24-framer.md](reports/A24-framer.md) |
| `framer` | 3.00:1 | — | **White on magenta (3.43:1) and coral (3.08:1) is large-text-only.** Acceptable as-is under AA large text at the 24px subhead the cards use, but coral has no margin — any drift darker in the real gradient drops it below 3:1. | [A24-framer.md](reports/A24-framer.md) |
| `framer` | 3.00:1 | — | **`focus` #0099ff clears the white surface at exactly 3.00:1.** No margin. | [A24-framer.md](reports/A24-framer.md) |
| `hp` | 3.00:1 | — | Usage note that would make the real value defensible: white on `#ff5050` clears the 3:1 large-text threshold, so the chip is defensible only if its label is set at 24px+, or 18.66px+ at weight 700. | [A26-hp.md](reports/A26-hp.md) |
| `hp` | 3.00:1 | — | **`focus` `#0e3191` reuses the pressed-CTA navy for a second job.** Defensible — it is HP's own blue and clears 3:1 on every light surface — but a brand team may prefer a dedicated ring hex. | [A26-hp.md](reports/A26-hp.md) |
| `intercom` | 3.00:1 | — | *Usage note that makes the real value defensible:* the pair clears 3:1, so it is compliant as **large text** — `{typography.headline}` 28px, or 18.66px+ at weight 700. | [A28-intercom.md](reports/A28-intercom.md) |
| `meta` | 3.00:1 | — | **`badge-success` label and `colors.success` as text — real AA failure.** #ffffff on #31a24c and #31a24c on #ffffff both measure **3.28:1** against 4.5:1. | [A36-meta.md](reports/A36-meta.md) |
| `minimax` | 3.00:1 | — | **`product-card-*` taglines — 14px white at 80% opacity on coral/magenta.** Below 3.18:1 and 3.06:1 respectively. | [A37-minimax.md](reports/A37-minimax.md) |
| `mintlify` | 3.00:1 | — | **`on-dark` on `testimonial-orange` #f55a3c — `testimonial-card-feature`, 3.28:1.** Nearest passing: `{colors.ink}` on the same orange is **6.04:1**, or the palette's own `{colors.testimonial-orange-deep}` #cc3a1f carries white at **5.01:1… | [A38-mintlify.md](reports/A38-mintlify.md) |
| `mistral.ai` | 3.00:1 | — | Usage note that would make the real value defensible: at `{typography.button-md}` (14px/500) the 4.5:1 threshold applies, so there is no size at which 3.34:1 is compliant. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `mistral.ai` | 3.00:1 | — | Usage note for keeping #fa520f: it would be defensible only on 24px+ text (3:1 threshold), which rules out links at 14px and tab labels at 14px. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `mongodb` | 3.00:1 | — | **`stone` #7c8c9a on canvas = 3.46:1.** Usage note that makes it defensible: 18px+ labels only, where 3:1 applies. | [A41-mongodb.md](reports/A41-mongodb.md) |
| `mydealz` | 3.00:1 | — | **`button-primary` — white on `primary` #30a83c, 3.09:1 vs 4.5:1.** Nearest passing value: **`#197e25`** (`green-strong`, already in the palette) at 5.18:1, visually a deeper version of the same green. | [A42-mydealz.md](reports/A42-mydealz.md) |
| `nerdwallet` | 3.00:1 | — | **`{colors.info}` #4b99e6 — 3.0:1, needs 4.5.** Nearest passing: **#2b79c4 at 4.53:1**. | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `nerdwallet` | 3.00:1 | — | **`{marquee-ribbon}`: `{colors.primary}` on `{colors.lime-ribbon}` — 3.36:1, needs 4.5.** Its label is 14px bold, below the large-text threshold. | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `nerdwallet` | 3.00:1 | — | **`{award-ribbon-pill}`: `{colors.primary}` on `{colors.mint-100}` — 4.45:1, needs 4.5**, and **`{badge-compare}`: `{colors.primary}` on `{colors.lime-panel}` — 4.41:1.** Both labels are 12px bold `{typography.eyebrow}`, which is not WCAG… | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `nike` | 3.00:1 | — | **`{colors.accent-pink}` `#ed1aa0` — 4.00:1 on canvas.** Clears 3:1, so it is defensible for 24px+ text or 18.66px+ at weight 700, and for chip and swatch fills. | [A44-nike.md](reports/A44-nike.md) |
| `nintendo-2001` | 3.00:1 | — | Nearest passing orange for a white label: `#ae6416` (4.53:1). | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `posthog` | 3.00:1 | — | **`mute` at 4.49:1 / 4.16:1.** Nearest passing value `#67685e` (4.88:1 on canvas, 4.53:1 on `surface-soft`). | [A54-posthog.md](reports/A54-posthog.md) |
| `raycast` | 3.00:1 | — | **The focus ring itself is a brand decision.** `{colors.focus}` reuses white rather than introducing a new hex, and an offset-outside ring is a visible change to Raycast's chrome. | [A55-raycast.md](reports/A55-raycast.md) |
| `renault` | 3.00:1 | — | **`{colors.error}` `#be6464` on `{colors.canvas}` — 4.04:1, needs 4.5:1.** The file's own prose puts this tone on inline form error messages, which are set in `{typography.body-sm}` (14px / 400), so those messages fail AA by a small margin. | [A56-renault.md](reports/A56-renault.md) |
| `replicate` | 3.00:1 | — | **`{colors.primary}` `#ea2804` with `{colors.on-primary}` `#ffffff` — 4.37:1, needs 4.5:1.** Nearest passing value: **`#e52704`** (4.54:1), a 2% luminance step that is visually indistinguishable but is still a falsified brand hex. | [A57-replicate.md](reports/A57-replicate.md) |
| `resend` | 3.00:1 | — | **`{colors.hairline-control}` `rgba(255,255,255,0.36)`.** A new tone in a palette whose identity is partly *how faint its edges are*. | [A58-resend.md](reports/A58-resend.md) |
| `revolut` | 3.00:1 | — | **`stone` `#8d969e` for metadata.** 3.00:1. | [A59-revolut.md](reports/A59-revolut.md) |
| `stripe` | 3.00:1 | — | **`pill-tag-soft` ink.** `{colors.primary-deep}` on `{colors.primary-bg-subdued-hover}` is 4.23:1 at 10px. | [A69-stripe.md](reports/A69-stripe.md) |
| `together.ai` | 3.00:1 | — | **`{colors.body}` `#959494` as secondary text — 3.03:1 on `{colors.canvas}`, required 4.5:1.** Extracted; not changed. | [A74-together.ai.md](reports/A74-together.ai.md) |
| `vercel` | 3.00:1 | — | **`{colors.mute}` `#888888` as text.** 3.54:1 / 3.40:1 against 4.5:1. | [A76-vercel.md](reports/A76-vercel.md) |
| `warp` | 3.00:1 | — | **Nearest passing value if the brand would rather keep one hairline token than split the job.** `{colors.hairline}` `#3f3a36` would need to reach roughly `#6f6862` to clear 3:1 against `{colors.canvas-soft}` `#383330` — a visibly heavier l… | [A79-warp.md](reports/A79-warp.md) |
| `wired` | 3.00:1 | — | **`{colors.focus}` reuses `{colors.link}`.** Confirm the brand accepts its inline-link blue appearing as a 2 px keyboard focus ring on chrome, given the file's own Don't reserves that blue for article body links. | [A81-wired.md](reports/A81-wired.md) |
| `wise` | 3.00:1 | — | **`{colors.mute}` `#868685` at 3.64:1 on white.** Nearest passing value: **`#757575`** (4.61:1). | [A82-wise.md](reports/A82-wise.md) |
| `wise` | 3.00:1 | — | **`{colors.warning-deep}` `#b86700` at 4.22:1.** Nearest passing: **`#b06200`** (4.57:1) — a change invisible to the eye. | [A82-wise.md](reports/A82-wise.md) |
| `x.ai` | 3.00:1 | — | **`{colors.mute}` on `{colors.canvas-card}` at 4.49:1, 0.01 short of 4.5:1.** Nearest passing value `#7e8288`. | [A83-x.ai.md](reports/A83-x.ai.md) |
| `zapier` | 3.00:1 | — | *Usage note:* restrict warm-white labels on orange to `{typography.display-xs}` 20px/700 or larger, where the 3:1 large-text threshold applies and 3.27:1 passes. | [A84-zapier.md](reports/A84-zapier.md) |
| `elevenlabs` | 3.02:1 | — | **`colors.semantic-success` #16a34a — 3.02:1 on canvas, 3.30:1 on white.** Not flagged by the harness (it matches no required role) but it fails AA for text. | [A20-elevenlabs.md](reports/A20-elevenlabs.md) |
| `nintendo-2001` | 3.02:1 | — | Nearest passing lavender for white large text: `#9090c2` (3.02:1); for the full 4.5 threshold, `#73739a` (4.52:1). | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `nike` | 3.03:1 | — | **`{colors.success-bright}` `#1eaa52` — 3.03:1 as text on canvas, needs 4.5:1.** Nearest passing `#157c3b` (5.28:1) or `#167f3d` (5.08:1). | [A44-nike.md](reports/A44-nike.md) |
| `nintendo-2001` | 3.04:1 | — | Nearest passing values, if the periwinkle body is ever used as a text ground: `ink-soft` -> `#1b2343` (4.51:1), `muted-indigo` -> `#232339` (4.50:1), `hairline` -> `#3b3e5c` (3.04:1), `error` -> `#520006` (4.53:1). | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `minimax` | 3.06:1 | — | **`focus-on-dark` on `brand-magenta` at 3.06:1.** Clears the bar with 0.06 to spare. | [A37-minimax.md](reports/A37-minimax.md) |
| `starbucks` | 3.09:1 | — | **`{colors.warning}` #fbbc05 as a text colour.** Usage note that makes the real value defensible: yellow is a chip, icon or band fill with `{colors.text}` drawn on it, never a label colour. | [A68-starbucks.md](reports/A68-starbucks.md) |
| `sanity` | 3.12:1 | — | **`error` `#dd0000` as validation text.** 3.82:1 on the canvas, 3.12:1 on `#212121`. | [A61-sanity.md](reports/A61-sanity.md) |
| `cursor` | 3.16:1 | — | **`timeline-pill-done` — white #ffffff on gold #c08532, 3.16:1, needs 4.5:1** at 11px uppercase. | [A17-cursor.md](reports/A17-cursor.md) |
| `figma` | 3.18:1 | — | **`comparison-checkmark` — `#1ea64a` on `#ffffff` at 3.18:1, required 4.5:1 by the harness.** | [A23-figma.md](reports/A23-figma.md) |
| `minimax` | 3.18:1 | — | **`badge-new` — white on `brand-coral` at 13px, 2.95–3.18:1.** Coral is the brand's signature signal colour and the "NEW" pill is one of its most recognisable marks, so the hex is unchanged. | [A37-minimax.md](reports/A37-minimax.md) |
| `intercom` | 3.19:1 | — | **`button-fin` fails AA at 3.19:1** — `{colors.on-primary}` white on `{colors.fin-orange}` #ff5600. | [A28-intercom.md](reports/A28-intercom.md) |
| `hp` | 3.22:1 | — | **`badge-sale-coral` — white on `bloom-coral` `#ff5050` at 3.22:1, requires 4.5:1.** `#ff5050` is a real HP sale-tag colour and is not changed here. | [A26-hp.md](reports/A26-hp.md) |
| `lovable` | 3.22:1 | — | Nearest passing value: the same charcoal at **0.5 opacity** -> #8a8884, 3.22:1. | [A33-lovable.md](reports/A33-lovable.md) |
| `zapier` | 3.27:1 | — | **`button-primary` label contrast, 3.27:1 against 4.5:1 required.** `{colors.on-primary}` `#fffefb` on `{colors.primary}` `#ff4f00`. | [A84-zapier.md](reports/A84-zapier.md) |
| `claude` | 3.28:1 | — | **White on coral fails AA at the button label size.** `on-primary` #ffffff on `primary` #cc785c = **3.28:1**; `button-primary` labels are `typography.button` 14px/500, so 4.5:1 applies. | [A11-claude.md](reports/A11-claude.md) |
| `mintlify` | 3.28:1 | — | **`on-dark` on `testimonial-orange` — `founder-quote-card`, 3.28:1.** Same pair, but this card's copy is `{typography.body-sm}` throughout, so no large-text note rescues it. | [A38-mintlify.md](reports/A38-mintlify.md) |
| `airbnb` | 3.30:1 | — | **`{colors.legal-link}` #428bff at 3.30:1** on 13–14px legal copy. | [A02-airbnb.md](reports/A02-airbnb.md) |
| `figma` | 3.34:1 | — | **`button-magenta-promo` — white on `#ff3d8b` at 3.34:1, required 4.5:1.** | [A23-figma.md](reports/A23-figma.md) |
| `mistral.ai` | 3.34:1 | — | **`#ffffff` on `#fa520f` — 3.34:1, needs 4.5:1.** Affects `button-primary`, `badge-orange` and any copy on `sunset-stripe-band`. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `mistral.ai` | 3.34:1 | — | **`#fa520f` on `#ffffff` — 3.34:1, needs 4.5:1.** Affects `button-link`, `footer-link` and `segmented-tab-active`. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `composio` | 3.35:1 | — | **`accent-violet` #7b3aed at 3.35:1 on canvas** — illustration-only, carries no text and no boundary. | [A16-composio.md](reports/A16-composio.md) |
| `lovable` | 3.35:1 | — | Nearest passing value: **#3b82f6** at full opacity — 3.35:1 and 4.63:1. | [A33-lovable.md](reports/A33-lovable.md) |
| `mastercard` | 3.36:1 | — | **`ink-muted` `#696969` on the ink footer is 3.36:1.** The source describes footer column headers as "uppercase, muted, weight 700" without a hex. | [A34-mastercard.md](reports/A34-mastercard.md) |
| `kraken` | 3.45:1 | — | **`success` #149e61 — 3.45:1 on #ffffff as text, needs 4.5:1.** | [A30-kraken.md](reports/A30-kraken.md) |
| `replicate` | 3.46:1 | — | **`{colors.badge-success}` `#2b9a66` with `{colors.on-dark}` `#fcfcfc` — 3.46:1 at 12px, needs 4.5:1.** Nearest passing green: **`#258458`** (4.53:1). | [A57-replicate.md](reports/A57-replicate.md) |
| `revolut` | 3.47:1 | — | **`primary` `#494fdf` as text on black.** 3.47:1. | [A59-revolut.md](reports/A59-revolut.md) |
| `airbnb` | 3.52:1 | — | **White on Rausch — 3.52:1, left as-is.** `{colors.on-primary}` #ffffff on `{colors.primary}` #ff385c. | [A02-airbnb.md](reports/A02-airbnb.md) |
| `cursor` | 3.52:1 | — | **`button-primary` — white #ffffff on Cursor Orange #f54e00, 3.52:1, needs 4.5:1.** This is the brand's signature CTA. | [A17-cursor.md](reports/A17-cursor.md) |
| `cal` | 3.68:1 | — | **`colors.brand-accent` as link text on canvas, 3.68:1.** Same token, same decision. | [A10-cal.md](reports/A10-cal.md) |
| `raycast` | 3.75:1 | — | **`{colors.ash}` #6a6b6c at 3.75:1.** No change proposed. | [A55-raycast.md](reports/A55-raycast.md) |
| `intercom` | 3.78:1 | — | **`{colors.ink-subtle}` at 14px and 12px.** The file assigns it to footer columns and helper text, where it measures 3.78:1 — a real AA failure at those sizes. | [A28-intercom.md](reports/A28-intercom.md) |
| `hp` | 3.89:1 | — | **`primary-bright` `#296ef9` on `ink` `#1a1a1a` at 3.89:1, requires 4.5:1.** Used for dark-band CTA links. | [A26-hp.md](reports/A26-hp.md) |
| `opencode.ai` | 3.92:1 | — | `accent` `#007aff` at 3.92:1 on `canvas` and 4.17:1 on `surface-dark`. | [A49-opencode.ai.md](reports/A49-opencode.ai.md) |
| `stripe` | 3.95:1 | — | **`{colors.ink-mute}` and `{colors.ink-mute-2}` on `{colors.canvas-cream}`.** 3.95:1 and 4.13:1. | [A69-stripe.md](reports/A69-stripe.md) |
| `framer` | 3.97:1 | — | *Keep the extracted hex, change the type:* set the card's text to `{colors.on-primary}` black, 8.10:1 on this ground and ≥3.97:1 on all four gradients. | [A24-framer.md](reports/A24-framer.md) |
| `replicate` | 4.09:1 | — | **`{colors.link}` `#ea2804` on `{colors.canvas}` — 4.09:1.** Recommend `{colors.primary-deep}` `#c01f00` (**5.71:1**) for link *text*, keeping `#ea2804` for the CTA fill. | [A57-replicate.md](reports/A57-replicate.md) |
| `mastercard` | 4.11:1 | — | **`accent-signal` `#CF4500` is 4.11:1 as text on cream.** It passes as a fill behind white (4.66:1), which is the file's only documented use. | [A34-mastercard.md](reports/A34-mastercard.md) |
| `1win` | 4.21:1 | — | **`{colors.on-primary}` #ffffff on `{colors.secondary}` #0075ff — 4.21:1, needs 4.5:1.** The "Log In" button and `pill-badge`. | [A01-1win.md](reports/A01-1win.md) |
| `revolut` | 4.24:1 | — | **`accent-danger` `#e23b4a` as error text on white.** 4.24:1. | [A59-revolut.md](reports/A59-revolut.md) |
| `revolut` | 4.27:1 | — | **`link` `#376cd5` on the dark canvas.** 4.27:1. | [A59-revolut.md](reports/A59-revolut.md) |
| `posthog` | 4.29:1 | — | **`link-inline` at 4.29:1.** Nearest passing value `#10749e` (4.52:1 on canvas). | [A54-posthog.md](reports/A54-posthog.md) |
| `vodafone` | 4.30:1 | — | **`{colors.primary}` as small text on `{colors.canvas-soft}`.** 4.3:1, short of 4.5:1. | [A77-vodafone.md](reports/A77-vodafone.md) |
| `cursor` | 4.37:1 | — | Alternative that keeps the real orange: an ink label instead of white. | [A17-cursor.md](reports/A17-cursor.md) |
| `nerdwallet` | 4.41:1 | — | **`{editorial-badge}`: `{colors.lime-panel}` on `{colors.primary}` — 4.41:1, needs 4.5.** 11px `{typography.micro}`. | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `ferrari` | 4.46:1 | — | `{colors.body}` #969696 on `{colors.surface-card}` — 4.46:1, short of 4.5 by 0.04. | [A22-ferrari.md](reports/A22-ferrari.md) |
| `dell-1996` | 4.49:1 | — | **`{colors.on-primary}` #ffffff on `{colors.primary}` #e91d2a — 4.49:1, required 4.5:1.** Affects `cta-block-red` and `cert-seal`. | [A18-dell-1996.md](reports/A18-dell-1996.md) |
| `figma` | 4.50:1 | — | Nearest passing fill at 4.5:1: `#d83376` (4.51:1). | [A23-figma.md](reports/A23-figma.md) |
| `figma` | 4.50:1 | — | If a hex change is wanted anyway, the nearest passing green at 4.5:1 is `#18883d` (4.54:1). | [A23-figma.md](reports/A23-figma.md) |
| `wired` | 4.50:1 | — | **`{colors.link}` #057dbc at 4.5006:1 on white.** Technically AA, with no margin. | [A81-wired.md](reports/A81-wired.md) |
| `cursor` | 4.51:1 | — | Nearest passing value, same hue: **#c23d00** at 4.51:1 with white. | [A17-cursor.md](reports/A17-cursor.md) |
| `cursor` | 4.54:1 | — | Nearest passing value, same hue: **#8a5e1f** at 4.54:1 with white. | [A17-cursor.md](reports/A17-cursor.md) |
| `hp` | 4.54:1 | — | Nearest passing value, keeping white text: darken the chip to `#c2403f` → 4.54:1. | [A26-hp.md](reports/A26-hp.md) |
| `hp` | 4.54:1 | — | Nearest passing value if it must carry body copy: `#4e86fb` → 4.54:1 on `#1a1a1a`. | [A26-hp.md](reports/A26-hp.md) |
| `intercom` | 4.54:1 | — | *Nearest passing value:* #cc4500 reaches 4.54:1 with white, but it is visibly a different, muddier orange and would falsify the brand. | [A28-intercom.md](reports/A28-intercom.md) |
| `mercury` | 4.71:1 | — | **`{colors.on-primary}` on `{colors.primary}` at 4.71:1** passes with 0.21 of margin. | [A35-mercury.md](reports/A35-mercury.md) |
| `pinterest` | 4.78:1 | — | **`{colors.on-primary}` on `{colors.primary}` at 4.78:1.** Passes, but with 0.28 of headroom. | [A52-pinterest.md](reports/A52-pinterest.md) |
| `nerdwallet` | 4.86:1 | — | **`{colors.on-primary}` on `{colors.primary}` at 4.86:1** passes with 0.36 of headroom. | [A43-nerdwallet.md](reports/A43-nerdwallet.md) |
| `mistral.ai` | 4.93:1 | — | Nearest passing value, keeping the orange: swap the label to `{colors.ink}` #1f1f1f, which measures **4.93:1** on the same orange. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `1win` | 4.99:1 | — | Preferred remedy: `{colors.black}` label → 4.99:1. | [A01-1win.md](reports/A01-1win.md) |
| `mistral.ai` | 5.03:1 | — | Nearest passing value: `{colors.primary-deep}` #cc3a05, already in the palette, at **5.03:1**. | [A40-mistral.ai.md](reports/A40-mistral.ai.md) |
| `hp` | 5.40:1 | — | Nearest passing value, keeping the coral: switch the chip label to `{colors.ink}` `#1a1a1a` on `#ff5050` → **5.4:1**. | [A26-hp.md](reports/A26-hp.md) |
| `zapier` | 5.40:1 | — | *Nearest passing value:* ink the label in `{colors.ink}` `#201515`, which measures 5.40:1 on the same orange and changes no brand hex. | [A84-zapier.md](reports/A84-zapier.md) |
| `figma` | 6.29:1 | — | Alternative with **no hex change** (my recommendation): swap the label to `{colors.ink}`, which measures **6.29:1** on the existing magenta and matches the rest of the system, where every pill is black-on-light or white-on-black. | [A23-figma.md](reports/A23-figma.md) |
| `nintendo-2001` | 6.45:1 | — | Usage note that makes the real value defensible: keep `#f68d1f` and set the label in `{colors.carbon}` instead of white — the same orange measures **6.45:1** with carbon text, so the brand hex survives and the pair passes. | [A45-nintendo-2001.md](reports/A45-nintendo-2001.md) |
| `1win` | 7.47:1 | — | Preferred remedy: keep #00b24b and set the label in `{colors.black}` → **7.47:1**. | [A01-1win.md](reports/A01-1win.md) |

## Unclassified — read the item

25 items across 19 files.

| Site | Item | Report |
|---|---|---|
| `1win` | Usage note that makes the real value defensible: *this is a decorative tonal seam between same-family darks, never the sole boundary of an interactive control; every focusable element carries `hairline-strong` or the focus ring.* That note… | [A01-1win.md](reports/A01-1win.md) |
| `airbnb` | Approval needed on which way a consumer of this file should go: keep Rausch and raise the label to large-text size, or keep 16px and use #e00b41. | [A02-airbnb.md](reports/A02-airbnb.md) |
| `claude` | **The contrast score of 5 is a disclosure score, not a compliance score.** Eleven measured failures remain in this file. | [A11-claude.md](reports/A11-claude.md) |
| `claude` | **The homepage typewriter effect.** Known Gaps records a code-block typewriter on the live site. | [A11-claude.md](reports/A11-claude.md) |
| `clickhouse` | **Two Iteration Guide / Don'ts rules were reversed**, not just extended: the file previously instructed readers never to document hover. | [A13-clickhouse.md](reports/A13-clickhouse.md) |
| `hp` | Usage note now written into the file: valid for `{typography.display-sm}` (24px) and larger only; body links inside `ink` slabs use `{colors.on-ink}`. | [A26-hp.md](reports/A26-hp.md) |
| `lovable` | Usage note that makes the real value defensible: #eceae4 is acceptable wherever the boundary is decorative and the content is identifiable without it — card containment, image outlines, dividers, the footer container. | [A33-lovable.md](reports/A33-lovable.md) |
| `lovable` | Recommendation: keep #eceae4 as the documented brand value, scope it to decoration in prose (done), and apply `hairline-strong` to control boundaries only. | [A33-lovable.md](reports/A33-lovable.md) |
| `lovable` | Recommendation: raise interactive borders to 0.5 and leave passive ones alone. | [A33-lovable.md](reports/A33-lovable.md) |
| `mastercard` | **Three type roles have no line height** in the source (`button-primary-label`, `button-consent-label`, `ghost-watermark`). | [A34-mastercard.md](reports/A34-mastercard.md) |
| `nike` | **`{rounded.full}` vs `{rounded.lg}` on every pill.** Frontmatter and prose disagree (9999px vs 30px) and Key Characteristics labels `{rounded.full}` as "30px". | [A44-nike.md](reports/A44-nike.md) |
| `resend` | **Usage note that would make the frozen values defensible.** `{colors.hairline}` and `{colors.divider-soft}` are defensible as-is if scoped in writing to purely decorative separation — row rules, footer column dividers, nav underline — whe… | [A58-resend.md](reports/A58-resend.md) |
| `resend` | **The AAA tap-target claim.** "WCAG AAA met on mobile" in Responsive Behavior was left in place and scoped in the Accessibility section rather than edited. | [A58-resend.md](reports/A58-resend.md) |
| `runwayml` | **The empty `accent` / `on-accent` roles.** Confirming that Runway has no signal colour, and that the two lost token points are correct rather than a naming miss, needs a brand owner's yes. | [A60-runwayml.md](reports/A60-runwayml.md) |
| `sanity` | **`shadow.ring-focus-extracted`.** The source states `0 0 0 2px var(--color-blue-500)` and never gives `--color-blue-500` a hex. | [A61-sanity.md](reports/A61-sanity.md) |
| `spacex` | Usage note that makes #e0e0e8 defensible where it stays: on `card-shop-product` the hairline is decorative separation between same-coloured cards and carries no information a user needs to identify or operate a control, so 1.4.11 does not… | [A66-spacex.md](reports/A66-spacex.md) |
| `spacex` | **Error styling without a red.** The brand forbids accent colour, so I expressed the error state through border weight, position and caption copy rather than a semantic hue. | [A66-spacex.md](reports/A66-spacex.md) |
| `spotify` | **Confirm the Calm profile** and the two roster changes under Shared issues. | [A67-spotify.md](reports/A67-spotify.md) |
| `spotify` | **Quantify the card hover.** "Slight background lightening" names no target tone and no overlay opacity, so there is no hover token and the Motion table expresses it as an overlay `opacity` fade. | [A67-spotify.md](reports/A67-spotify.md) |
| `starbucks` | **The expander's animated property.** The source gives the accordion a `300ms` `cubic-bezier(0.25, 0.46, 0.45, 0.94)` transition but never says what it animates; a real FAQ accordion almost certainly animates `height`, which SPEC section 6… | [A68-starbucks.md](reports/A68-starbucks.md) |
| `tesla` | **Two extra `motion:` keys.** `duration-extracted-state: 330ms` and `ease-extracted-state: cubic-bezier(0.5, 0, 0, 0.75)` sit beside the ten verbatim Cinematic values, and the hover row uses 330ms rather than the profile's 240ms. | [A72-tesla.md](reports/A72-tesla.md) |
| `together.ai` | **`badge-neutral` fill.** Prose said `{colors.hairline}`, the components block says `{colors.canvas}`. | [A74-together.ai.md](reports/A74-together.ai.md) |
| `uber` | **The 900ms spinner revolution**, the one value outside the Playful scale (the profile's longest token, 450ms, spins too fast to read as a loader). | [A75-uber.md](reports/A75-uber.md) |
| `voltagent` | **`focus-on-light` in a dark-only brand.** Defensible under SPEC section 1 because the file declares a light fill, but if `ex-pricing-tier-featured` is corrected to the brand's real dark "featured" treatment (see Shared issues), `focus-on-… | [A78-voltagent.md](reports/A78-voltagent.md) |
| `webflow` | **No `shadow:` group added.** The five elevation levels are multi-offset `rgba(...)` recipes, not single values, so tokenising them is a structural decision about the token format rather than an audit fix. | [A80-webflow.md](reports/A80-webflow.md) |

