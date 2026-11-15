#!/usr/bin/env python3
"""Write one agent brief per site into theme-audit/briefs/.

Each brief is self-contained: the shared process and rules, plus the facts the
repo-wide harness already measured for that specific site, so the agent spends
its budget reviewing rather than rediscovering.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRIEFS = os.path.join(ROOT, "theme-audit/briefs")
os.makedirs(BRIEFS, exist_ok=True)

roster = json.load(open(os.path.join(ROOT, "theme-audit/roster.json")))
checks = {}
for r in roster:
    p = os.path.join(ROOT, "theme-audit/checks", r["site"] + ".json")
    if os.path.exists(p):
        checks[r["site"]] = json.load(open(p))

TEMPLATE = """You are Agent {agent}, the dedicated reviewer for the site file `{site}` in the repo at {root}.

Theme intent: {intent}
Motion profile: {profile}
Files you may write: `design-md/{site}/DESIGN.md`, which you edit, and `theme-audit/reports/{agent}-{site}.md`, which you create. Nothing else: every other site's DESIGN.md, README.md, CONTRIBUTING.md and the rest of theme-audit/ (SPEC.md, audit.py, roster, briefs, other agents' reports) are read-only. Those two paths are yours and you are expected to write both.

Judge against `theme-audit/SPEC.md`. Read it first, in full. It defines the token contract, the contrast thresholds, the section contract, the motion token block, the four motion profiles and their values, the motion rules, and the honest limits of this audit. Follow it exactly.

WHAT THE HARNESS ALREADY MEASURED FOR YOUR SITE
Confirm each of these yourself; do not take them on trust.
{measured}

PROCESS
1. Read theme-audit/SPEC.md, then read your owned file end to end.
2. Run the harness on your site:
   cd {root} && python3 -I theme-audit/audit.py --site {site} --json
3. Review every dimension below. Log each finding with severity: P0 = wrong or unusable, P1 = clearly incomplete, P2 = polish. Compute every contrast ratio with a short python3 snippet; never estimate one.
4. Fix what you can inside your owned file. Prefer adding or correcting token values over bolting on prose caveats.
5. Write your report to theme-audit/reports/{agent}-{site}.md using the structure below. Create that file; do not touch any other report.
6. Re-run the harness on your site and record the after-scores.

REVIEW DIMENSIONS
A. Token contract: are all required colour roles present (SPEC section 1)? No file in this repo defines a focus ring — add one that suits this brand and state its measured contrast against the canvas. Does every {{group.token}} reference in the prose resolve to a key in this file's frontmatter?
B. Colour: measure every pair SPEC section 2 lists. Do NOT change a brand identity hex to make a ratio pass; these files document real brands and a falsified hex makes the document wrong. Record each failure under "Needs approval" with the nearest passing value and the usage note that would make the real value defensible (for example the minimum text size at which the 3:1 threshold applies). Where the real brand genuinely fails AA, say so plainly in the file.
C. Background and elevation: compute the ratios between canvas, surface and raised — are the layers actually distinguishable? Is elevation expressed one consistent way rather than shadow and border mixed at random?
D. Typography: does every role have size, weight and line height? Is body text readable on this file's own surfaces?
E. Borders, radius, focus ring: internally consistent ladders, with no value sitting outside its own scale.
F. Motion and animation — the main gap, and the reason this audit exists. Add:
   - a `motion:` group to the frontmatter carrying the **{profile}** profile's values per SPEC section 5;
   - a `## Motion & Animation` section placed after `## Components`, whose FIRST line states that this motion system is prescribed to match the brand's visual identity and was not measured from the live site;
   - inside it, a table of interaction x duration x easing x property x reduced-motion behaviour covering hover, press, focus, page transition, modal or drawer, dropdown, toast, list enter, list exit and loading;
   - a `@media (prefers-reduced-motion: reduce)` rule stating what is removed and what remains.
   Reference every value as {{motion.duration-base}} and so on. Animate transform and opacity only.
G. Accessibility: add a `## Accessibility` section covering measured contrast for the key pairs, focus ring visibility on each surface this file defines, minimum tap target, and reduced-motion. State real failures rather than hiding them.
H. States: every component entry names its states, from default, hover, focus-visible, active/pressed, disabled, loading, selected, error. A component with genuinely two states says so.
I. Identity: after your edits, does the file still read as this specific brand, or has it drifted toward a generic token dump? If the assigned {profile} profile is wrong for this brand, argue for a different one in the report and use the one you conclude is right — do not switch silently.
{extra}
RULES
- One file only. If the root cause sits in README.md, CONTRIBUTING.md or the harness, do not edit it: list it under "Shared issues" with the file, the line and your proposed fix.
- No new dependencies. python3 standard library only.
- Do not invent extracted facts. Anything you cannot verify from the file's own content goes in Known Gaps or is labelled as prescribed.
- Do not reflow or rewrite parts of the file you are not fixing. Keep the diff reviewable.

REPORT STRUCTURE for theme-audit/reports/{agent}-{site}.md

## {agent} · {site}
Scores before -> after (1-5), from the harness: tokens · refs · contrast · sections · motion · states

### Findings
| Severity | Dimension | Element | Issue |

### Changes made
| Location in file | Before -> After | Why |

### Contrast checks
| Foreground / Background | Ratio | Required | Pass/Fail |

### Motion inventory
| Interaction | Duration | Easing | Property | Reduced-motion behaviour |

### Shared issues (not fixed)
| File | Issue | Proposed fix |

### Needs approval
### Identity verdict

In your reply to me, give only: before/after harness scores, findings counted by severity, anything under Needs approval, and one sentence on where the SPEC was ambiguous. Be concise; I am reading 84 of these.
"""

LEGACY_EXTRA = """J. Format conversion: this file has no frontmatter token block and uses the numbered heading variant (`## 1. Visual Theme & Atmosphere` and so on). Convert it to the current format. Build `colors`, `typography`, `spacing`, `rounded` and `components` from the hex values, type values and component descriptions already written in its prose, and rename the headings to the unnumbered set in SPEC section 3. Do not invent a value that is not already stated somewhere in the file; anything genuinely absent goes in Known Gaps.
"""

written = 0
for r in roster:
    c = checks.get(r["site"], {})
    bullets = []
    if c:
        if c.get("roles_missing"):
            bullets.append(f"- Missing colour roles: {', '.join(c['roles_missing'])}.")
        for f in c.get("contrast_failures", []):
            bullets.append(f"- Contrast: {f['pair']} ({f['fg']} on {f['bg']}) measures "
                           f"{f['ratio']}:1, below the {f['required']}:1 required for {f['role']}.")
        if c.get("sections_missing"):
            bullets.append(f"- Missing sections: {', '.join(c['sections_missing'])}.")
        if c.get("dangling_refs"):
            bullets.append(f"- Dangling references: {', '.join(c['dangling_refs'])}.")
        if c.get("states_missing"):
            bullets.append(f"- States never named anywhere in the file: {', '.join(c['states_missing'])}.")
        if c.get("layout_animation_mentions"):
            bullets.append(f"- Mentions animating layout-triggering properties: "
                           f"{', '.join(c['layout_animation_mentions'])}. Check and correct.")
        if not c.get("has_frontmatter"):
            bullets.append("- No frontmatter token block at all (legacy format file).")
    measured = "\n".join(bullets) if bullets else "- Nothing flagged automatically; review on judgement."
    body = TEMPLATE.format(agent=r["agent"], site=r["site"], intent=r["intent"],
                           profile=r["profile"], root=ROOT, measured=measured,
                           extra=LEGACY_EXTRA if r["legacy"] else "")
    open(os.path.join(BRIEFS, f"{r['agent']}-{r['site']}.md"), "w").write(body)
    written += 1
print(f"{written} briefs written to theme-audit/briefs/")
