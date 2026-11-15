#!/usr/bin/env python3
"""Write one disclosure line per measured contrast failure a file had not stated.

Nothing here changes a colour, a binding or a threshold. It states numbers the
harness already computes, in the one section the harness reads, so that a frozen
brand failure is documented rather than silent. Run it, then run audit.py: any
file still reporting contrast-undisclosed means a line did not match, which is a
bug here and not a reason to relax the matcher.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit as A                                   # noqa: E402

ROOT = A.ROOT
HEADING = "### Remaining measured failures"

PREAMBLE = """\
Every ratio below is computed with WCAG 2.1 relative luminance from this file's
own frontmatter hexes. These pairs were measured but not stated elsewhere in this
section. No colour and no `components:` binding was changed to produce them: the
values are extracted and frozen, so stating the number is the whole of the remedy
available without a brand-owner decision. Where a fix would mean altering a brand
tone or re-pointing a binding, that decision is listed in the audit's Needs
approval set, not taken here. Where a row says the ground was substituted, the
component states no `backgroundColor` of its own, so the page floor was measured
in its place; if the real ground is imagery, a gradient or an overlay, this file
does not record it, and the ratio describes the substitution rather than the
rendered result."""


def ref(key):
    """Token reference if the name looks like one, else the bare name."""
    return "`{colors.%s}`" % key if re.fullmatch(r"[A-Za-z0-9_.-]+", key) else key


def row(f, declared_bg):
    """One table row. It must carry the foreground hex and the measured ratio:
    those are what audit.py's disclosure matcher reads."""
    ratio = f"{f['ratio']:.2f}:1"
    need = f"{f['required']:.1f}:1"
    if "component" in f:
        name = f["component"]
        if declared_bg.get(name):
            what = (f"`components.{name}` — its own `textColor` "
                    f"(`{f['fg']}`) on its own `backgroundColor` (`{f['bg']}`)")
            note = "Fail — both tones are bound in this file"
        else:
            what = (f"`components.{name}` — its `textColor` (`{f['fg']}`) "
                    f"on the page floor (`{f['bg']}`)")
            note = ("Fail — no `backgroundColor` declared; page floor "
                    "substituted as the ground")
        return f"| {what} | {ratio} | {need} | {note} |"

    pair = f["pair"]
    role = f.get("role", "")
    if pair.startswith("no ring covers "):
        surface = pair[len("no ring covers "):].split(" (best:")[0]
        best = pair.split("(best: ")[1].rstrip(")")
        what = (f"best ring {ref(best)} (`{f['fg']}`) against "
                f"{ref(surface)} (`{f['bg']}`)")
        note = "Fail — no focus ring this file declares reaches 3:1 on that surface"
        return f"| {what} | {ratio} | {need} | {note} |"

    fg_key, bg_key = pair.split(" on ", 1)
    what = f"{ref(fg_key)} (`{f['fg']}`) on {ref(bg_key)} (`{f['bg']}`)"
    return f"| {what} | {ratio} | {need} | Fail — {role or 'measured pair'} |"


def block(f_list, declared_bg):
    lines = [HEADING, "", PREAMBLE, "",
             "| Foreground / Background | Ratio | Required | Status |",
             "|---|---:|---:|---|"]
    lines += [row(f, declared_bg) for f in f_list]
    return "\n".join(lines) + "\n"


def insert(text, body):
    """Append the block to the end of ## Accessibility, before the next ## ."""
    m = re.search(r"^## Accessibility\s*$", text, re.M)
    if not m:
        raise SystemExit("no ## Accessibility section")
    nxt = re.search(r"^## ", text[m.end():], re.M)
    cut = m.end() + nxt.start() if nxt else len(text)
    head, tail = text[:cut].rstrip("\n"), text[cut:]
    return head + "\n\n" + body + ("\n" + tail if tail else "\n")


def main():
    touched = rows = 0
    for path in sorted(A.glob.glob(os.path.join(ROOT, "design-md/*/DESIGN.md"))):
        r = A.audit(path)
        pending = r["contrast_unresolved"]
        if not pending:
            continue
        text = open(path).read()
        if HEADING in text:
            print(f"SKIP {r['site']}: already has {HEADING!r}")
            continue
        declared_bg = {n: (p.get("backgroundColor") or "").strip()
                       for n, p in A.parse_components(text).items()}
        out = insert(text, block(pending, declared_bg))
        open(path, "w").write(out)
        touched += 1
        rows += len(pending)
        print(f"{r['site']:16} +{len(pending)}")
    print(f"\n{rows} failures disclosed across {touched} files")


if __name__ == "__main__":
    main()
