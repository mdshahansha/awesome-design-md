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
`spacing`, `rounded`, `components`, and now `motion`. A `shadow:` group is
required only where the file documents real shadow values in its prose — several state an
`rgba(...)` elevation with no token to reference, which is why a `{shadow.small}`
reference once pointed at nothing.

Required colour roles. A role is satisfied by any key matching its pattern, so
`surface-cream`, `surface-1` and `layer-01` all satisfy `surface`. **Never add
an alias token purely to satisfy a pattern**, and note the difference from the
parallel accessible token of section 2: that one has a real job — it is drawn
where contrast is needed, and the frozen tone is scoped to decoration. An alias
has no job but to match a regex. So where the file already owns a passing tone
that does the boundary work, use it and add nothing; add a parallel token only
when nothing in the palette can carry the job.

Adding one does **not** hide the original failure, which several agents have
worried about: the role's representative token only decides which name the
role reports, while every tone in the role is measured separately. mydealz's
extracted hairline is still reported at 1.2:1 and 1.31:1 after a passing
`hairline-strong` took the role name — if a role looks unsatisfied but
the palette plainly contains it under another name, that is a harness bug to
report under Shared issues, not a token to invent. Brand documents should not
carry tokens that exist only to please a regex:

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
file defines two rings: `focus` for its default surfaces and a counterpart
named for the other polarity — `focus-on-dark` in a light-default file,
`focus-on-light` in a dark-default one. Its Accessibility section states which
surface each one is drawn on.

Polarity naming breaks down in two real cases, so prefer the simpler answer
where it works. A monochrome brand whose accent **is** its ink or its paper has
no coloured surface for a ring to sit on: use the brand's own ink or paper with
a mandatory offset of the opposite polarity, and do not invent a chromatic ring
for a brand whose first rule is that it has no accent colour. A brand with
three surface polarities, or a dark canvas plus a near-white accent band, is
better served by one mid-luminance ring that clears 3:1 against all of them
than by a pair named for light and dark. Over full-bleed photography, which has
no measurable colour, specify a two-tone ring: the brand colour with a 1px
outer edge in the opposite polarity. The ring must reach 3:1 against every
surface it can appear over, not just the canvas — meaning the surfaces it is
drawn *on*, not the control fill it surrounds. Requiring both is often
arithmetically impossible: a white canvas caps a ring's luminance while a
saturated CTA fill demands a higher one, with no value satisfying each. A ring
drawn outside its control, with a stated offset, is judged against the surface
behind it, which is what WCAG 2.2 Focus Appearance asks for. State the offset.

Where the prose says a particular ink is drawn on a particular ground — a
label on a product colour, a caption on a tinted band — declare that pair in
`components:` with its `backgroundColor` and `textColor`. Only a declared pair
is measurable; a ground that exists as a colour token and is never bound to a
label is invisible to the harness, and guessing those pairings by token name
produced failures that the files never actually used.

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

**A disclosed failure is a handled failure.** The harness scores contrast on
*undisclosed* failures only: name the failing pair in the Accessibility section,
with its measured ratio, and it stops counting against the file. That is the
intended outcome for every frozen value — the document's job is to tell the
truth about the brand, not to score well.

**Do not change a brand's identity colour to pass.** These files document real
brands; falsifying a hex makes the document wrong. A failing pair is recorded
under "Needs approval" with the nearest passing value *and* the usage note that
makes it defensible (for example: this muted grey is for 18px+ labels only, so
3:1 applies). Where the real brand genuinely fails AA, say that plainly — it is
useful information for anyone building on it.

## 3. Section contract

**This table's order is the required document order.** Motion & Animation and
Accessibility sit between Components and Do's and Don'ts. The harness does not
enforce order, so without this the files drift apart section by section.

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
| Responsive Behavior | yes — as a top-level `##`; where a file already carries it as a Layout subsection, **move** it verbatim, never duplicate it, promoting its child headings one level so the section reads at the same depth as its peers |
| Iteration Guide | optional |
| Known Gaps | yes |

A legacy section with no slot in this contract — `## 9. Agent Prompt Guide`,
for instance — is kept verbatim as an unnumbered section after Known Gaps, not
deleted and not folded into another section. Its content was extracted; losing
it would be a regression.

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
  duration-reduced: 150ms
```

Values are per profile. Use your profile's block from section 5 verbatim, so the same
interaction is comparable across every file that shares a profile:

**Crisp**
```yaml
motion:
  duration-instant: 60ms
  duration-fast: 100ms
  duration-base: 150ms
  duration-slow: 220ms
  duration-emphasis: 300ms
  ease-standard: cubic-bezier(0.2, 0, 0.2, 1)
  ease-enter: cubic-bezier(0, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 20ms
  duration-reduced: 100ms
```

**Calm**
```yaml
motion:
  duration-instant: 80ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-emphasis: 500ms
  ease-standard: cubic-bezier(0.4, 0, 0.2, 1)
  ease-enter: cubic-bezier(0.2, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 40ms
  duration-reduced: 150ms
```

**Playful**
```yaml
motion:
  duration-instant: 70ms
  duration-fast: 130ms
  duration-base: 200ms
  duration-slow: 320ms
  duration-emphasis: 450ms
  ease-standard: cubic-bezier(0.3, 0, 0.2, 1)
  ease-enter: cubic-bezier(0.17, 0.89, 0.32, 1.28)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 60ms
  duration-reduced: 130ms
```

**Cinematic**
```yaml
motion:
  duration-instant: 120ms
  duration-fast: 240ms
  duration-base: 400ms
  duration-slow: 600ms
  duration-emphasis: 900ms
  ease-standard: cubic-bezier(0.22, 1, 0.36, 1)
  ease-enter: cubic-bezier(0.16, 1, 0.3, 1)
  ease-exit: cubic-bezier(0.5, 0, 0.75, 0)
  stagger-step: 80ms
  duration-reduced: 150ms
```

Deviate from a value only with a reason stated in the file, and never to the
point where two files sharing a profile stop feeling like siblings.

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

1. Luxury, automotive, hardware-flagship, gaming-console or aerospace identity
   → **Cinematic**, whatever the canvas polarity. A white-canvas luxury brand is
   still cinematic; the tell is full-bleed photography, sparse type and a slow
   reveal, not a dark background.
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

Rules 1-3 are conjunctions, so a file can fail all three and still sit between
two profiles. Rule 4 is the terminal answer, not a default of last resort: when
nothing above fires, the file is **Calm**, and a file already rostered as
something else stays there unless an agent argues the switch from evidence in
the file. Do not leave a borderline case undecided, and do not switch silently
— cross-file comparability depends on the roster matching what the files do.

## 6. Motion rules (every profile)

- Animate `transform` and `opacity` only. Never `width`, `height`, `top`,
  `left` or `margin`.
- Exit duration is shorter than its matching entrance.
- Nothing animates on first paint in a way that delays content.
- No infinite animation except loaders and deliberate brand ambience, and that
  ambience must be stated as such.
- `@media (prefers-reduced-motion: reduce)`: remove all travel and scale, keep
  opacity fades at `{motion.duration-reduced}` — never more than 150ms, whatever
  the profile's own base — and freeze ambience. Every file states this. The
  token exists so a Cinematic file never has to hardcode a bare value to satisfy
  this rule, since its own `duration-fast` is 240ms.

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
