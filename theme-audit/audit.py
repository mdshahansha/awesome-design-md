#!/usr/bin/env python3
"""Measurable audit of every design-md/<site>/DESIGN.md.

No dependencies, no network, no rendering. Everything here is computed from the
file itself, so results are reproducible and comparable between runs.

  python3 theme-audit/audit.py            # table for all sites
  python3 theme-audit/audit.py --json     # machine-readable, one object per site
  python3 theme-audit/audit.py --site claude
"""
import argparse, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tokens SPEC.md requires every file to define, by role.
# A role is satisfied by any colors: key matching one of its patterns, so a file
# naming its surface "surface-cream" still counts. Patterns are ordered: the
# first match becomes the representative token used for contrast checks.
REQUIRED_COLOR_ROLES = {
    "canvas":   [r"^canvas$", r"^background$", r"^bg$", r"^base$", r"^surface-base$",
                 r"^paper$", r"^page$", r"^canvas-"],
    "surface":  [r"^surface$", r"^surface-(card|soft|raised|elevated|cream|dark|light|alt|muted|subtle|panel|deep|strong|mid)",
                 r"^card$", r"^card-", r"^panel$", r"^elevated$"],
    "text":     [r"^ink$", r"^text$", r"^text-primary$", r"^body$", r"^body-strong$",
                 r"^foreground$", r"^on-canvas$", r"^on-(light|cream|paper|white)$", r"^ink-"],
    "text-dim": [r"^muted$", r"^muted-", r"^text-(secondary|muted|soft|tertiary)$",
                 r"^body-(soft|muted|secondary)$", r"^subtle$", r"^secondary$",
                 r"^on-dark-soft$", r"^caption$"],
    "border":   [r"^hairline$", r"^hairline-", r"^border$", r"^border-", r"^divider$",
                 r"^rule$", r"^stroke$", r"^outline$", r"^line$"],
    "accent":   [r"^primary$", r"^accent$", r"^brand$", r"^accent-", r"^primary-"],
    "on-accent":[r"^on-primary$", r"^accent-contrast$", r"^on-accent$", r"^on-brand$",
                 r"^on-primary-"],
    "focus":    [r"^focus$", r"^focus-ring$", r"^focus-", r"^ring$"],
}
REQUIRED_SECTIONS = ["Overview", "Colors", "Typography", "Layout", "Elevation & Depth",
                     "Shapes", "Components", "Motion & Animation", "Accessibility",
                     "Do's and Don'ts", "Responsive Behavior", "Known Gaps"]
# Optional per SPEC section 3: tracked for reporting, never counted against a score.
OPTIONAL_SECTIONS = ["Iteration Guide"]
SECTIONS = REQUIRED_SECTIONS + OPTIONAL_SECTIONS
MOTION_KEYS_MIN = {"duration-fast", "duration-base", "ease-standard"}
STATE_WORDS = ["hover", "focus-visible", "active", "pressed", "disabled",
               "loading", "selected", "error"]


def srgb(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexstr):
    h = hexstr.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    h = h[:6]
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def parse_frontmatter(text):
    """Return {group: {key: raw_value}} for the top two indent levels."""
    if not text.startswith("---\n"):
        return {}, ""
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm, body = text[4:end], text[end + 5:]
    groups, cur = {}, None
    for line in fm.split("\n"):
        m = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            cur = m.group(1)
            groups.setdefault(cur, {})
            continue
        m = re.match(r"^  ([A-Za-z0-9][A-Za-z0-9_.-]*):\s*(.*)$", line)
        if m and cur:
            groups[cur][m.group(1)] = clean_value(m.group(2))
    return groups, body


def clean_value(raw):
    """Strip a trailing comment and surrounding quotes from a YAML scalar."""
    v = raw.strip()
    if v.startswith(('"', "'")):
        q = v[0]
        end = v.find(q, 1)
        if end != -1:
            return v[1:end]
    return re.sub(r"\s+#.*$", "", v).strip().strip("\"'")


def parse_components(text):
    """components: entries and their properties, two indent levels down."""
    if not text.startswith("---\n"):
        return {}
    fm = text[4:text.find("\n---\n", 4)]
    m = re.search(r"^components:\s*$(.*?)(?=^[a-z][a-zA-Z0-9_-]*:|\Z)", fm, re.S | re.M)
    if not m:
        return {}
    entries, cur = {}, None
    for line in m.group(1).split("\n"):
        e = re.match(r"^  ([A-Za-z0-9][A-Za-z0-9_.-]*):\s*$", line)
        if e:
            cur = e.group(1); entries[cur] = {}
            continue
        pr = re.match(r"^    ([A-Za-z0-9][A-Za-z0-9_.-]*):\s*(.*)$", line)
        if pr and cur:
            entries[cur][pr.group(1)] = clean_value(pr.group(2))
    return entries


def find_role(colors, patterns):
    """First pattern wins, so the representative token is the canonical one."""
    for pat in patterns:
        for key in colors:
            if re.match(pat, key):
                return key
    return None


def find_role_strongest(colors, patterns, against):
    """Pick the matching key with the highest contrast against `against`.

    Used for roles whose threshold is about visibility rather than identity: a
    file that defines hairline, hairline-soft and border-strong should be judged
    on border-strong, since that is the one drawn where a boundary must be seen.
    """
    matches = [k for pat in patterns for k in colors if re.match(pat, k)]
    if not matches or against not in colors:
        return find_role(colors, patterns)
    return max(dict.fromkeys(matches), key=lambda k: contrast(colors[k], colors[against]))


def audit(path):
    site = os.path.basename(os.path.dirname(path))
    text = open(path).read()
    groups, body = parse_frontmatter(text)
    colors = {k: v for k, v in groups.get("colors", {}).items()
              if re.fullmatch(r"#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}|#[0-9a-fA-F]{8}", v)}
    r = {"site": site, "has_frontmatter": bool(groups), "color_count": len(colors)}

    # --- sections -------------------------------------------------------
    present = {s for s in SECTIONS if f"## {s}" in text}
    r["sections_present"] = sorted(present)
    r["sections_missing"] = [s for s in REQUIRED_SECTIONS if s not in present]
    r["optional_sections_missing"] = [s for s in OPTIONAL_SECTIONS if s not in present]

    # --- required token roles -------------------------------------------
    roles = {role: find_role(colors, cands) for role, cands in REQUIRED_COLOR_ROLES.items()}
    # Boundary and focus tokens are judged on the strongest variant the file owns.
    canvas_key = roles.get("canvas")
    if canvas_key:
        for role in ("border", "focus", "text-dim"):
            if roles.get(role):
                roles[role] = find_role_strongest(
                    colors, REQUIRED_COLOR_ROLES[role], canvas_key)
    r["roles_resolved"] = {k: v for k, v in roles.items() if v}
    r["roles_missing"] = sorted(k for k, v in roles.items() if not v)

    # --- dangling {group.token} references ------------------------------
    dangling = set()
    for grp, key in set(re.findall(r"\{([a-zA-Z]+)\.([A-Za-z0-9_.-]+)\}", text)):
        target = grp + "s" if grp == "component" else grp
        if target in groups:
            if key not in groups[target]:
                dangling.add(f"{grp}.{key}")
        elif grp not in ("token",):
            dangling.add(f"{grp}.{key} [no group]")
    r["dangling_refs"] = sorted(dangling)

    # --- contrast -------------------------------------------------------
    fails = []
    def check(fg_role, bg_role, minimum, label):
        fg, bg = roles.get(fg_role), roles.get(bg_role)
        if not fg or not bg:
            return
        ratio = round(contrast(colors[fg], colors[bg]), 2)
        rec = {"pair": f"{fg} on {bg}", "fg": colors[fg], "bg": colors[bg],
               "ratio": ratio, "required": minimum, "role": label}
        if ratio < minimum:
            fails.append(rec)
    def check_all(role, bg_role, minimum, label):
        """Every token in a role, not just its representative."""
        bg = roles.get(bg_role)
        if not bg:
            return
        for pat in REQUIRED_COLOR_ROLES[role]:
            for key in colors:
                if not re.match(pat, key) or "disabled" in key:
                    continue
                ratio = round(contrast(colors[key], colors[bg]), 2)
                if ratio < minimum:
                    fails.append({"pair": f"{key} on {bg}", "fg": colors[key],
                                  "bg": colors[bg], "ratio": ratio,
                                  "required": minimum, "role": label})

    check("text", "canvas", 4.5, "body text")
    check("text", "surface", 4.5, "body text on surface")
    check("text-dim", "canvas", 4.5, "secondary text")
    check("text-dim", "surface", 4.5, "secondary text on surface")
    check_all("text-dim", "canvas", 4.5, "secondary text, all tones")
    check_all("border", "canvas", 3.0, "boundary, all tones")
    check("border", "canvas", 3.0, "component boundary")
    def achromatic(hexstr):
        h = hexstr.lstrip("#")
        h = "".join(c * 2 for c in h) if len(h) == 3 else h[:6]
        rgb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        return max(rgb) - min(rgb) <= 8

    for bg in ("canvas", "surface", "accent"):
        key = roles.get(bg)
        # A monochrome brand's accent is its ink or its paper, not a surface a
        # ring sits on; forcing a ratio there invents a colour the brand lacks.
        if bg == "accent" and key and achromatic(colors[key]):
            continue
        check("focus", bg, 3.0, f"focus indicator on {bg}")

    # Signal colours, each against the file's own on-accent ink. Disabled
    # tokens are exempt: WCAG places no contrast requirement on them.
    on_accent = roles.get("on-accent")
    if on_accent:
        signals = [k for k in colors
                   if re.match(r"^(primary|accent|secondary|brand|cta)", k)
                   and "disabled" not in k]
        for key in signals:
            ratio = round(contrast(colors[on_accent], colors[key]), 2)
            if ratio < 4.5:
                fails.append({"pair": f"{on_accent} on {key}", "fg": colors[on_accent],
                              "bg": colors[key], "ratio": ratio, "required": 4.5,
                              "role": "text on signal colour"})
    # Every background/text pair the components block actually asserts — 1808
    # of them across the repo, and the name-matching check saw none.
    def deref(v):
        m = re.fullmatch(r"\{colors\.([A-Za-z0-9_.-]+)\}", v or "")
        if m:
            return colors.get(m.group(1))
        return v if re.fullmatch(r"#[0-9a-fA-F]{3,8}", v or "") else None

    comp_fails = []
    for name, props in parse_components(text).items():
        if "disabled" in name:          # WCAG sets no requirement on disabled
            continue
        bg, fg = deref(props.get("backgroundColor")), deref(props.get("textColor"))
        if not bg or not fg:
            continue
        ratio = round(contrast(fg, bg), 2)
        if ratio < 4.5:
            comp_fails.append({"component": name, "fg": fg, "bg": bg,
                               "ratio": ratio, "required": 4.5})
    # Disclosure: a failure named in the Accessibility section, by token or by
    # hex, is documented rather than hidden. SPEC section 2 asks for exactly
    # that where the value is extracted and frozen.
    m_acc = re.search(r"^## Accessibility\s*$(.*?)(?=^## |\Z)", text, re.S | re.M)
    acc = (m_acc.group(1) if m_acc else "").lower()

    def disclosed(f):
        if not acc:
            return False
        fg_name = f["pair"].split(" on ")[0] if "pair" in f else f.get("component", "")
        return fg_name.lower() in acc or f["fg"].lower() in acc

    seen, deduped = set(), []
    for f in fails:
        k = (f["pair"], f["required"])
        if k not in seen:
            seen.add(k); deduped.append(f)
    fails[:] = sorted(deduped, key=lambda f: f["ratio"])
    for f in fails:
        f["disclosed"] = disclosed(f)
    for f in comp_fails:
        f["disclosed"] = disclosed(f)
    r["component_contrast_failures"] = comp_fails
    r["contrast_unresolved"] = [f for f in fails if not f["disclosed"]] + \
                               [f for f in comp_fails if not f["disclosed"]]
    r["contrast_disclosed"] = [f for f in fails if f["disclosed"]] + \
                              [f for f in comp_fails if f["disclosed"]]
    r["contrast_failures"] = fails

    # --- motion ---------------------------------------------------------
    motion = groups.get("motion", {})
    r["motion_group"] = sorted(motion.keys())
    r["motion_keys_missing"] = sorted(MOTION_KEYS_MIN - set(motion))
    r["has_motion_section"] = "## Motion & Animation" in text
    r["has_reduced_motion"] = bool(re.search(r"prefers-reduced-motion", text))
    r["durations_found"] = sorted(set(re.findall(r"\b(\d{2,4})ms\b", text)), key=int)
    r["easings_found"] = len(re.findall(r"cubic-bezier\([^)]*\)", text))
    # motion rule violations: animating layout-triggering properties
    NEGATED = re.compile(r"\b(don't|do not|never|avoid|no|rather than|instead of|not)\b", re.I)
    bad = set()
    for line in text.split("\n"):
        for m in re.finditer(r"animat\w*[^.\n]{0,60}?\b(width|height|top|left|margin)\b",
                             line, re.I):
            # Look at the clause leading up to the match; a prohibition is fine.
            lead = line[max(0, m.start() - 80):m.start() + 10]
            if not NEGATED.search(lead):
                bad.add(m.group(1).lower())
    for m in re.finditer(r"transition:[^;`\n]*?\b(width|height|top|left|margin)\b",
                         text, re.I):
        lead = text[max(0, m.start() - 80):m.start()]
        if not NEGATED.search(lead):
            bad.add(m.group(1).lower())
    r["layout_animation_mentions"] = sorted(bad)

    # --- states ---------------------------------------------------------
    # Only the Components section counts, and only structured lines within it:
    # a bare mention elsewhere (a Known Gaps line saying loading is undocumented,
    # for instance) is not documentation of that state.
    comp = ""
    m = re.search(r"^## Components\s*$(.*?)(?=^## |\Z)", text, re.S | re.M)
    if m:
        comp = m.group(1)
    structured = "\n".join(line for line in comp.split("\n")
                           if line.lstrip().startswith(("|", "-", "*"))
                           or re.search(r"\*\*[^*]+\*\*\s*[:—-]", line))
    hay = structured.lower()
    r["states_documented"] = [w for w in STATE_WORDS if w in hay]
    r["states_missing"] = [w for w in STATE_WORDS if w not in hay]

    # --- score ----------------------------------------------------------
    r["score"] = {
        "tokens":   5 if not r["roles_missing"] else max(1, 5 - len(r["roles_missing"])),
        "refs":     5 if not r["dangling_refs"] else 2,
        # Scored on undisclosed failures only: documenting a frozen brand
        # failure is the required outcome, not a deduction.
        "contrast": 5 if not r["contrast_unresolved"]
                    else max(1, 5 - len(r["contrast_unresolved"])),
        "sections": max(1, 5 - len(r["sections_missing"])),
        "motion":   5 if (r["has_motion_section"] and not r["motion_keys_missing"]
                          and r["has_reduced_motion"]) else
                    (3 if r["durations_found"] else 1),
        "states":   max(1, 5 - len(r["states_missing"])),
    }
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--site")
    ap.add_argument("--out")
    a = ap.parse_args()

    paths = sorted(glob.glob(os.path.join(ROOT, "design-md/*/DESIGN.md")))
    if a.site:
        paths = [p for p in paths if os.path.basename(os.path.dirname(p)) == a.site]
        if not paths:
            sys.exit(f"no such site: {a.site}")
    results = [audit(p) for p in paths]

    if a.out:
        os.makedirs(a.out, exist_ok=True)
        for r in results:
            with open(os.path.join(a.out, r["site"] + ".json"), "w") as f:
                json.dump(r, f, indent=2)
    if a.json:
        print(json.dumps(results, indent=2))
        return

    hdr = f"{'site':16} {'tok':>4} {'ref':>4} {'con':>4} {'sec':>4} {'mot':>4} {'sta':>4}  issues"
    print(hdr); print("-" * len(hdr))
    for r in results:
        s = r["score"]
        issues = []
        if r["roles_missing"]:      issues.append(f"roles:{','.join(r['roles_missing'])}")
        if r["dangling_refs"]:      issues.append(f"dangling:{len(r['dangling_refs'])}")
        if r["contrast_unresolved"]:
            issues.append(f"contrast-undisclosed:{len(r['contrast_unresolved'])}")
        if r["contrast_disclosed"]:
            issues.append(f"(disclosed:{len(r['contrast_disclosed'])})")
        if not r["has_motion_section"]: issues.append("no-motion-section")
        if r["layout_animation_mentions"]: issues.append("animates-layout-props")
        print(f"{r['site']:16} {s['tokens']:>4} {s['refs']:>4} {s['contrast']:>4} "
              f"{s['sections']:>4} {s['motion']:>4} {s['states']:>4}  {'; '.join(issues)}")

    n = len(results)
    def avg(k): return round(sum(r["score"][k] for r in results) / n, 2)
    print("-" * len(hdr))
    print(f"{'MEAN ('+str(n)+' sites)':16} {avg('tokens'):>4} {avg('refs'):>4} "
          f"{avg('contrast'):>4} {avg('sections'):>4} {avg('motion'):>4} {avg('states'):>4}")


if __name__ == "__main__":
    main()
