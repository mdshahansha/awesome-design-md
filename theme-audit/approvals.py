#!/usr/bin/env python3
"""Pull the Needs-approval items out of the 84 reports and group them by the
decision each one asks for.

The reports are prose, so the grouping below is keyword-derived, not parsed
semantics. Two consequences, both stated in the generated document rather than
hidden: the first matching rule wins, so an item that asks two questions lands
in one bucket; and `unclassified` is a real bucket, not a rounding error. The
item's own wording in the report is authoritative and is linked from every row.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = os.path.join(ROOT, "theme-audit/reports")

# An item starts at a list marker: "1.", "-", "*", or a range like "2-6." /
# "2–6." The range form is why an earlier count read 508 instead of 509.
ITEM_SPLIT = re.compile(r"^\s*(?:\d+(?:\s*[–—-]\s*\d+)?\.|[-*])\s+(?=\S)", re.M)
PROPOSAL = re.compile(r"\*{0,2}(#[0-9a-fA-F]{6})\*{0,2}\s*\(\s*(\d+(?:\.\d+)?)\s*:\s*1", re.I)
RATIO = re.compile(r"(\d+(?:\.\d+)?)\s*:\s*1")

# First match wins; order is the priority order, and it is printed in the doc.
RULES = (
    ("Tap target under the 44px minimum",
     r"tap target|hit area|44\s*(?:×|x)\s*44|44\s*px|44px"),
    ("Motion profile assignment",
     r"motion profile|profile switch|profile (?:switched|change)|roster rule"),
    ("Source contradicts itself",
     r"contradict|disagrees? with itself|collision|which .{0,24} is authoritative"),
    ("Token name, alias or duplicate hex",
     r"alias|duplicate|renam|token \*?names?\*?|under a second name"),
    ("Re-point an extracted binding",
     r"re-?bind|re-?point|re-?scop|binding"),
    ("No semantic palette for a state",
     r"no (?:semantic|status) (?:palette|red)|brand (?:owns|ships) no red|has no hue|no disabled tone"),
    ("Prescribed value or system awaiting sign-off",
     r"prescrib|invent"),
    ("Change an extracted hex to reach the threshold", None),   # proposal present
    ("Frozen tone disclosed, no change sought", None),          # ratio, no proposal
)


def items():
    out = []
    for fn in sorted(os.listdir(REPORTS)):
        if not fn.endswith(".md"):
            continue
        txt = open(os.path.join(REPORTS, fn)).read()
        m = re.search(r"#+ *Needs approval(.*?)(?=\n#+ |\Z)", txt, re.S | re.I)
        if not m:
            continue
        for part in ITEM_SPLIT.split(m.group(1))[1:]:
            body = " ".join(part.split())
            if not body:
                continue
            props = PROPOSAL.findall(part)
            ratios = [float(x) for x in RATIO.findall(part)]
            out.append({
                "report": fn,
                "site": fn.split("-", 1)[1][:-3],
                "text": body,
                "proposals": props,
                # The lowest ratio an item names is the failure it is about;
                # the higher ones are thresholds and proposed replacements.
                "worst": min(ratios) if ratios else None,
                "bucket": None,
            })
    for it in out:
        it["bucket"] = classify(it)
    return out


def classify(it):
    low = it["text"].lower()
    for name, pat in RULES:
        if pat and re.search(pat, low):
            return name
    if it["proposals"]:
        return "Change an extracted hex to reach the threshold"
    if it["worst"] is not None:
        return "Frozen tone disclosed, no change sought"
    return "Unclassified — read the item"


def first_sentence(text, limit=240):
    s = re.split(r"(?<=[.?!])\s+(?=[A-Z*`#])", text, maxsplit=1)[0]
    s = s.strip()
    return s if len(s) <= limit else s[:limit - 1].rstrip() + "…"


def main():
    its = items()
    order = [n for n, _ in RULES] + ["Unclassified — read the item"]
    by = {n: [i for i in its if i["bucket"] == n] for n in order}

    o = []
    w = o.append
    w("# Needs approval\n")
    w(f"**{len(its)} items, from the Needs-approval section of all 84 reports.** "
      "Not one of them is a change already made: everything in this file is a "
      "question for whoever owns the brand value, and the audit's standing rule "
      "was to leave the extracted value alone and write the question down.\n")
    w("## How this document was built, and where it is weak\n")
    w("The reports are prose. Items are split on list markers and sorted into "
      "buckets by keyword, first matching rule winning, in the order the next "
      "table gives. Two honest consequences:\n")
    w("- An item that asks two questions appears once, under whichever rule "
      "matched first. The row's own wording usually shows this.")
    w("- **Unclassified is a real bucket.** It means no rule matched, not that "
      "the item is empty.\n")
    w("The excerpt in each row is the item's first sentence, cut to 240 "
      "characters. **The report is authoritative, not the excerpt.** Every row "
      "links to it.\n")
    w("An earlier count of these items read 508. It missed items numbered as a "
      "range (`2–6.`); the correct figure is "
      f"{len(its)}.\n")

    # The headline count is misleading on its own: two of the buckets ask for
    # nothing. Say which, before the table of all ten.
    record = len(by["Frozen tone disclosed, no change sought"])
    signoff = len(by["Prescribed value or system awaiting sign-off"])
    live = len(its) - record - signoff
    w("## What actually needs a decision\n")
    w(f"Of the {len(its)} items, **{record} ask for nothing.** They are frozen "
      "extracted tones whose failure is now disclosed in the file with its "
      "measured ratio; the reviewer recorded them for completeness and "
      "recommended no change. Reading the whole set as a backlog overstates it "
      "by that much.\n")
    w(f"**{signoff}** are sign-offs rather than choices: a value or a whole "
      "system the audit prescribed because the brand documents none, labelled "
      "prescribed everywhere it appears. The question is whether the inference "
      "may stay, not which of two values to pick.\n")
    w(f"**{live}** are live decisions — a hex, a binding, a name, a tap target "
      "or a contradiction in the source, each with two or more real answers.\n")

    w("## Totals\n")
    w("| Decision | Items | Files |")
    w("|---|---:|---:|")
    for n in order:
        g = by[n]
        if g:
            w(f"| {n} | {len(g)} | {len({i['site'] for i in g})} |")
    w(f"| **Total** | **{len(its)}** | **{len({i['site'] for i in its})}** |")
    w("")

    for n in order:
        g = by[n]
        if not g:
            continue
        w(f"## {n}\n")
        w(f"{len(g)} items across {len({i['site'] for i in g})} files.\n")
        has_num = any(i["worst"] is not None for i in g)
        if has_num:
            # Worst measured ratio first: the queue a brand owner should work
            # down. Items naming no ratio sort last, not first.
            g = sorted(g, key=lambda i: (i["worst"] is None, i["worst"] or 0))
            w("| Site | Worst ratio named | Proposed value | Item | Report |")
            w("|---|---:|---|---|---|")
            for i in g:
                worst = f"{i['worst']:.2f}:1" if i["worst"] is not None else "—"
                prop = ", ".join(f"`{h}` ({r}:1)" for h, r in i["proposals"][:2]) or "—"
                w(f"| `{i['site']}` | {worst} | {prop} | {first_sentence(i['text'])} "
                  f"| [{i['report']}](reports/{i['report']}) |")
        else:
            g = sorted(g, key=lambda i: i["site"])
            w("| Site | Item | Report |")
            w("|---|---|---|")
            for i in g:
                w(f"| `{i['site']}` | {first_sentence(i['text'])} "
                  f"| [{i['report']}](reports/{i['report']}) |")
        w("")

    path = os.path.join(ROOT, "theme-audit/APPROVALS.md")
    open(path, "w").write("\n".join(o) + "\n")
    print(f"APPROVALS.md written: {len(o)} blocks, {len(its)} items")


if __name__ == "__main__":
    sys.exit(main())
