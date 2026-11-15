# DESIGN.md Audit Spec

One standard every site file is judged against, so 84 independent reviews stay
comparable. Measured by `theme-audit/audit.py`; anything the script cannot
compute is a judgement call and must be argued for in the agent's report.

## Scope and honest limits

These files are documents, not a running UI. There is no dev server, no DOM and
no screenshot. So:

- **Computable here:** token coverage, contrast ratios, reference integrity,
  section coverage, state coverage, internal consistency of the spacing and
  radius ladders.
- **Scored honestly, after two corrections:** the states check counts a state
  only where the Components section documents it in a table row or list item,
  not anywhere the word appears in the file; and `Iteration Guide` is optional,
  so its absence costs nothing.
- **Not computable here:** overlap, horizontal overflow, clipping, tap-target
  size, frame rate, layout shift. Those need a rendered page. Any claim about
  them in a report is invalid.
- **Motion is prescribed, not extracted.** Nobody measured these brands'
  real timing functions. Every motion section added to a file must say so in
  its own first line. Do not present inferred motion as an extracted value.

## 1. Frontmatter token contract

Every file carries a YAML block. Required groups: `colors`, `typography`,
`spacing`, `rounded`, `components`, and now `motion`. Add a `shadow:` group
where the file documents real shadow values in its prose — several state an
`rgba(...)` elevation with no token to reference, which is why a `{shadow.small}`
reference once pointed at nothing.

Required colour roles. A role is satisfied by any key matching its pattern, so
`surface-cream` satisfies `surface`:

| Role | Purpose |
|---|---|
| `canvas` | page floor |
| `surface` | card, panel, raised surface |
| `text` | primary body and headline ink |
| `text-dim` | secondary, muted, caption |
| `border` | hairline, divider, component boundary |
| `accent` | the brand's signal colour |
| `on-accent` | text or icon sitting on the accent |
| `focus` | focus ring — **currently absent from all 84 files** |

Where a file documents both light and dark signature surfaces, one ring cannot
serve both: a blue that passes on white can sit at 1.2:1 on a coral card. Such a
file defines `focus` **and** `focus-on-dark`, and its Accessibility section
states which surface each one is drawn on. The ring must reach 3:1 against every
surface it can appear over, not just the canvas.

Every `{group.token}` in the prose must resolve to a key in that file's
frontmatter. The repo is at zero dangling references; keep it there.

## 2. Contrast

Measured with WCAG 2.1 relative luminance.

| Pair | Minimum |
|---|---|
| `text` on `canvas` | 4.5:1 |
| `text` on `surface` | 4.5:1 |
| `text-dim` on `canvas` | 4.5:1 |
| `on-accent` on `accent` | 4.5:1 |
| `border` on `canvas` | 3.0:1 |
| `focus` on `canvas` | 3.0:1 |

Every signal colour is checked, not just the representative accent: a brand with
two CTA colours was hiding one failure entirely. Tokens whose name contains
`disabled` are exempt, since WCAG sets no contrast requirement on them.

**Extracted values are frozen, including the utility tones.** A hairline at
1.36:1 is as much an extracted fact as the brand's red, so do not "fix" it in
place. Where a frozen tone is doing a job that needs contrast — a hairline that
is the only boundary of a text input, say — add a **parallel accessible token**
alongside it (`hairline-strong`, `divider` versus a control boundary), scope the
original to decoration in the prose, and label the new token as prescribed. Then
say plainly in the file that the real brand fails AA at that point. That is the
useful fact for anyone building on the document.

**Do not change a brand's identity colour to pass.** These files document real
brands; falsifying a hex makes the document wrong. A failing pair is recorded
under "Needs approval" with the nearest passing value *and* the usage note that
makes it defensible (for example: this muted grey is for 18px+ labels only, so
3:1 applies). Where the real brand genuinely fails AA, say that plainly — it is
useful information for anyone building on it.

## 3. Section contract

| Section | Required |
|---|---|
| Overview | yes |
| Colors | yes |
| Typography | yes |
| Layout | yes |
| Elevation & Depth | yes |
| Shapes | yes |
| Components | yes |
| **Motion & Animation** | yes — new, missing from all 84 |
| **Accessibility** | yes — new, missing from all 84 |
| Do's and Don'ts | yes |
| Responsive Behavior | yes |
| Iteration Guide | optional |
| Known Gaps | yes |

Ten early files carry no frontmatter and use a numbered variant of these
headings. Convert them to the current format: build the token block from the
hexes and type values already written in their prose, and do not invent values
that are not there. Anything unknown goes in Known Gaps.

## 4. Motion tokens

Add a `motion:` group to every file:

```yaml
motion:
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 600ms
  ease-standard: cubic-bezier(0.2, 0, 0, 1)
  ease-enter: cubic-bezier(0, 0, 0, 1)
  ease-exit: cubic-bezier(0.3, 0, 1, 1)
  stagger-step: 40ms
```

Values are per profile (§5), not identical across files.

## 5. Motion profiles

Each site gets exactly one, assigned in `roster.md` from observable signals in
its own file.

| Profile | Feel | Base duration | Easing bias | Stagger | Signature |
|---|---|---|---|---|---|
| **Crisp** | immediate, tool-like | 150ms | near-linear out | 20ms | state change reads as instant; no entrance choreography |
| **Calm** | composed, editorial | 250ms | symmetric ease | 40ms | short opacity-led fades, little travel |
| **Playful** | responsive, friendly | 200ms | overshoot on enter | 60ms | small scale pops on press, springy reveals |
| **Cinematic** | slow, deliberate, premium | 400–600ms | long decelerate | 80ms | full-bleed imagery scales slowly; type arrives late and settles |

Assignment rule, applied in order:

1. Dark canvas + luxury/automotive/hardware identity → **Cinematic**
2. Terminal, IDE, infra or developer-tool identity → **Crisp**
3. Saturated multi-colour or illustration-led consumer identity → **Playful**.
   Judge this on saturation *and role*, not on how many colours the palette
   lists. Bright tones used as static card backgrounds behind screenshots are
   not a playful identity; the test is whether saturated colour appears on
   interactive elements and whether the type voice is light and informal. A file
   whose own description says "sober" or "editorial", whose display weight is
   400, and which forbids gradients is **Calm** no matter how many hexes it
   defines.
4. Everything else → **Calm**

## 6. Motion rules (every profile)

- Animate `transform` and `opacity` only. Never `width`, `height`, `top`,
  `left` or `margin`.
- Exit duration is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content.
- No infinite animation except loaders and deliberate brand ambience, and that
  ambience must be stated as such.
- `@media (prefers-reduced-motion: reduce)`: remove all travel and scale, keep
  opacity fades at 150ms or less, and freeze ambience. Every file states this.

Each file's Motion & Animation section must cover, as a table of interaction ×
duration × easing × property × reduced-motion behaviour: hover, press,
focus, page/route transition, modal or drawer, dropdown, toast, list enter and
exit, and loading.

## 7. States

Every component entry names the states it supports, drawn from: default,
hover, focus-visible, active/pressed, disabled, loading, selected, error. A
component that genuinely has only two states says so.

## 8. Identity

After all of the above, the file must still read as the brand it documents.
A generic token block that would suit any site is a failure, even if every
individual check passes. Flag anything that reads as borrowed from another file
in the collection.
