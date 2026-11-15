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
    "surface":  [r"^surface$", r"^surface[-_]?\d", r"^surface[-_]", r"^card$",
                 r"^card[-_]", r"^panel$", r"^panel[-_]", r"^elevated$",
                 r"^tile$", r"^tile[-_]"],
    "text":     [r"^ink$", r"^text$", r"^text-primary$", r"^body$", r"^body-strong$",
                 r"^foreground$", r"^on-canvas$", r"^on-(light|cream|paper|white)$",
                 r"^ink-(strong|deep|black|primary)$"],
    "text-dim": [r"^text-dim$", r"^muted$", r"^muted-",
                 r"^ink-(muted|subtle|soft|tertiary|secondary|light)", r"^text-(secondary|muted|soft|tertiary)$",
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


def parse_nested(text, group):
    """A frontmatter group's entries and their properties, two levels down."""
    if not text.startswith("---\n"):
        return {}
    fm = text[4:text.find("\n---\n", 4)]
    m = re.search(rf"^{group}:\s*$(.*?)(?=^[a-z][a-zA-Z0-9_-]*:|\Z)", fm, re.S | re.M)
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


def parse_components(text):
    return parse_nested(text, "components")


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
    raw_colors = groups.get("colors", {})
    colors = {k: v for k, v in raw_colors.items()
              if re.fullmatch(r"#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}|#[0-9a-fA-F]{8}", v)}

    # Composite any rgba()/rgb() tokens over the canvas, so an opacity ladder is
    # measured as it renders rather than skipped.
    def _canvas_hex():
        for pat in REQUIRED_COLOR_ROLES["canvas"]:
            for k in colors:
                if re.match(pat, k):
                    return colors[k]
        return "#ffffff"

    composited = []
    base = _canvas_hex()
    bh = base.lstrip("#")
    bh = "".join(c * 2 for c in bh) if len(bh) == 3 else bh[:6]
    br, bg_, bb = (int(bh[i:i + 2], 16) for i in (0, 2, 4))
    for k, v in raw_colors.items():
        if k in colors:
            continue
        m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", v or "")
        if not m:
            continue
        r_, g_, b_ = (int(m.group(i)) for i in (1, 2, 3))
        a = float(m.group(4)) if m.group(4) else 1.0
        # A token that names its ground (border-on-ink, overlay-on-dark) is
        # drawn there, not on the canvas.
        gr, gg, gb = br, bg_, bb
        named = re.search(r"-on-([a-z0-9]+)", k)
        if named:
            for cand in colors:
                if re.match(rf"^{named.group(1)}($|[-_])", cand):
                    gh = colors[cand].lstrip("#")
                    gh = "".join(c * 2 for c in gh) if len(gh) == 3 else gh[:6]
                    gr, gg, gb = (int(gh[i:i + 2], 16) for i in (0, 2, 4))
                    break
        colors[k] = "#%02x%02x%02x" % (
            round(r_ * a + gr * (1 - a)),
            round(g_ * a + gg * (1 - a)),
            round(b_ * a + gb * (1 - a)))
        composited.append(k)
    r = {"site": site, "has_frontmatter": bool(groups), "color_count": len(colors),
         "composited_tokens": composited}

    # --- sections -------------------------------------------------------
    present = {s for s in SECTIONS if f"## {s}" in text}
    r["sections_present"] = sorted(present)
    r["sections_missing"] = [s for s in REQUIRED_SECTIONS if s not in present]
    r["optional_sections_missing"] = [s for s in OPTIONAL_SECTIONS if s not in present]

    # --- required token roles -------------------------------------------
    roles = {role: find_role(colors, cands) for role, cands in REQUIRED_COLOR_ROLES.items()}
    # A role no pattern can guess by name is still resolvable from what the
    # components bind. Mercury's boundaries are `fog` and `slate`; both are
    # declared as borderColor, which is better evidence than any regex.
    if not roles.get("border"):
        for props in parse_components(text).values():
            ref = props.get("borderColor") or props.get("border") or ""
            m = re.fullmatch(r"\{colors\.([A-Za-z0-9_.-]+)\}", ref)
            if m and m.group(1) in colors:
                roles["border"] = m.group(1)
                r.setdefault("roles_from_bindings", []).append("border=" + m.group(1))
                break

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

    # Only treat a light/dark marker as a THEME when the file actually has an
    # alternate-theme surface. In 36 of 84 files it is just a tone suffix
    # (border-light, m-blue-dark), and reading those as a separate theme
    # silenced real failures — reported by agent A14.
    dual_theme = any(re.search(r"(canvas|background|bg|base|surface)", k)
                     and re.search(r"(light|dark)", k) for k in colors)

    canvas_polarity = None
    for pat in REQUIRED_COLOR_ROLES["canvas"]:
        for k in colors:
            if re.match(pat, k):
                canvas_polarity = "dark" if luminance(colors[k]) < 0.2 else "light"
                break
        if canvas_polarity:
            break

    def theme_of(key):
        """Which theme a token belongs to. None means the file's default."""
        # An on-dark / on-light ink declares its own target surface, so it is
        # theme-scoped whether or not the file has a second theme.
        if re.search(r"(^|[-_])on-dark($|[-_])", key):
            return "dark"
        if re.search(r"(^|[-_])on-light($|[-_])", key):
            return "light"
        if not dual_theme:
            return None
        marker = None
        if re.search(r"dark($|[-_])|[-_]dark", key):
            marker = "dark"
        elif re.search(r"light($|[-_])|[-_]light", key):
            marker = "light"
        # A marker matching the file's own canvas polarity is a tone name, not a
        # second theme: ink-dark in a dark-canvas file belongs to the default.
        if marker and marker == canvas_polarity:
            return None
        return marker

    def same_theme(fg_key, bg_key):
        """A light-mode ink is never drawn on a dark-mode surface.

        Without this, the harness manufactured failures that cannot render —
        `ink on surface-card-dark` at 1.10:1, `on-dark-soft on canvas` at
        1.92:1 — and agents then documented problems that do not exist.
        """
        return (theme_of(fg_key) or "default") == (theme_of(bg_key) or "default")

    def check(fg_role, bg_role, minimum, label):
        fg, bg = roles.get(fg_role), roles.get(bg_role)
        if not fg or not bg or not same_theme(fg, bg):
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
                if not same_theme(key, bg):
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
    check_all("text", "canvas", 4.5, "body text, all tones")
    check_all("text", "surface", 4.5, "body text on surface, all tones")
    check_all("text-dim", "surface", 4.5, "secondary text on surface, all tones")
    check_all("border", "surface", 3.0, "boundary on surface, all tones")
    check_all("border", "canvas", 3.0, "boundary, all tones")

    # Semantic tones, measured as text on the canvas. Many are used as fills,
    # where 1.4.3 does not apply, so a failure here is a prompt for a usage
    # note rather than proof of a defect — but it must be visible either way.
    SEMANTIC = (r"^success", r"^warning", r"^error", r"^danger", r"^info",
                r"^semantic-", r"^positive", r"^negative")
    canvas_key = roles.get("canvas")
    if canvas_key:
        FILL_MARKER = re.compile(r"(subtle|soft|pale|faint|bg|background|fill|tint|"
                                 r"wash|surface|band|chip|badge|pill)")
        for pat in SEMANTIC:
            for key in colors:
                if not re.match(pat, key) or "disabled" in key:
                    continue
                if FILL_MARKER.search(key):
                    continue   # a fill tone, never the label drawn on it
                if not same_theme(key, canvas_key):
                    continue
                ratio = round(contrast(colors[key], colors[canvas_key]), 2)
                if ratio < 4.5:
                    fails.append({"pair": f"{key} on {canvas_key}",
                                  "fg": colors[key], "bg": colors[canvas_key],
                                  "ratio": ratio, "required": 4.5,
                                  "role": "semantic tone as text"})
    check("border", "canvas", 3.0, "component boundary")
    def achromatic(hexstr):
        h = hexstr.lstrip("#")
        h = "".join(c * 2 for c in h) if len(h) == 3 else h[:6]
        rgb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        return max(rgb) - min(rgb) <= 8

    # An inner or inset band of a composite ring is meant to match the surface
    # it sits on — WCAG 2.2 Focus Appearance measures the two bands against
    # each other, not against the background. Measured separately below.
    focus_tokens = [k for k in colors if re.match(r"^focus($|[-_])", k)
                    and not re.search(r"(inner|inset|halo)", k)]
    focus_bands = [k for k in colors if re.match(r"^focus", k)
                   and re.search(r"(inner|inset|halo)", k)]
    for props in parse_components(text).values():
        for prop in ("ringColor", "outlineColor", "focusRing", "focusColor"):
            m = re.fullmatch(r"\{colors\.([A-Za-z0-9_.-]+)\}", props.get(prop) or "")
            if m and m.group(1) in colors and m.group(1) not in focus_tokens:
                focus_tokens.append(m.group(1))
    # Not anchored: an inverse-canvas or hero-surface band is a surface a ring
    # can land on, and anchoring hid every one of them.
    surface_keys = [k for k in colors
                    if re.search(r"(canvas|background|base|surface|card|panel|tile|band)", k)
                    and not re.search(r"^(ink|text|body|muted|hairline|border|focus)", k)]
    # A token a component declares as a backgroundColor is a surface whatever it
    # is called: meta paints white type on `ink-deep`, which the name filter
    # above would drop, hiding every dark ground a ring lands on.
    ACCENTISH = re.compile(r"^(primary|accent|brand|cta|secondary|success|warning|"
                           r"error|danger|info|semantic|positive|negative|trading|"
                           r"badge|price)")
    for props in parse_components(text).values():
        m = re.fullmatch(r"\{colors\.([A-Za-z0-9_.-]+)\}", props.get("backgroundColor") or "")
        if not m or m.group(1) not in colors or m.group(1) in surface_keys:
            continue
        # A signal fill is not a ground a ring must clear: requiring both the
        # page behind a control and the control's own fill is arithmetically
        # impossible, which is why accent targets were dropped in 34a4499.
        if ACCENTISH.match(m.group(1)):
            continue
        surface_keys.append(m.group(1))
    accent_key = roles.get("accent")

    # A file's rings are a system, not independent claims. A surface is covered
    # when ANY ring clears 3:1 on it, so a ring named for one context
    # (focus-on-gradient, focus-ink) is not charged for surfaces another ring
    # serves. A failure means no ring in the file covers that surface at all.
    for s in dict.fromkeys(surface_keys):   # every surface, theme-independent
        if not focus_tokens:
            break
        best_ring, best = None, -1.0
        for ring in focus_tokens:
            ratio = round(contrast(colors[ring], colors[s]), 2)
            if ratio > best:
                best_ring, best = ring, ratio
        if best < 3.0:
            fails.append({"pair": f"no ring covers {s} (best: {best_ring})",
                          "fg": colors[best_ring], "bg": colors[s],
                          "ratio": best, "required": 3.0,
                          "role": "focus indicator coverage"})

    # Composite ring: the two bands must separate from each other by 3:1.
    for band in focus_bands:
        best = max((round(contrast(colors[band], colors[r]), 2)
                    for r in focus_tokens), default=None)
        if best is not None and best < 3.0:
            fails.append({"pair": f"{band} against its outer ring",
                          "fg": colors[band], "bg": colors[focus_tokens[0]],
                          "ratio": best, "required": 3.0,
                          "role": "composite ring band separation"})

    # Every background/text pair the components block actually asserts — 1808
    # of them across the repo, and the name-matching check saw none.
    def deref(v):
        m = re.fullmatch(r"\{colors\.([A-Za-z0-9_.-]+)\}", v or "")
        if m:
            return colors.get(m.group(1))
        return v if re.fullmatch(r"#[0-9a-fA-F]{3,8}", v or "") else None

    typo = parse_nested(text, "typography")

    def threshold_for(props):
        """4.5:1 normally, 3:1 where the component's own type is large text."""
        ref = props.get("typography", "")
        m = re.fullmatch(r"\{typography\.([A-Za-z0-9_.-]+)\}", ref or "")
        entry = typo.get(m.group(1), {}) if m else {}
        size = re.match(r"([\d.]+)", entry.get("fontSize", "") or "")
        weight = re.match(r"(\d+)", entry.get("fontWeight", "") or "")
        px = float(size.group(1)) if size else None
        wt = int(weight.group(1)) if weight else 400
        if px is not None and (px >= 24 or (px >= 18.66 and wt >= 700)):
            return 3.0
        return 4.5

    comp_fails = []
    for name, props in parse_components(text).items():
        if "disabled" in name:          # WCAG sets no requirement on disabled
            continue
        bg, fg = deref(props.get("backgroundColor")), deref(props.get("textColor"))
        declared_bg = (props.get("backgroundColor") or "").strip().lower()
        if declared_bg in ("transparent", "none", "inherit"):
            continue                            # ground not stated; nothing to measure
        if fg and not bg and roles.get("canvas"):
            bg = colors[roles["canvas"]]        # drawn on the page floor
        if not bg or not fg:
            continue
        need = threshold_for(props)
        ratio = round(contrast(fg, bg), 2)
        if ratio < need:
            comp_fails.append({"component": name, "fg": fg, "bg": bg,
                               "ratio": ratio, "required": need})
    # Disclosure: a failure named in the Accessibility section, by token or by
    # hex, is documented rather than hidden. SPEC section 2 asks for exactly
    # that where the value is extracted and frozen.
    m_acc = re.search(r"^## Accessibility\s*$(.*?)(?=^## |\Z)", text, re.S | re.M)
    acc = (m_acc.group(1) if m_acc else "").lower()

    acc_lines = [l for l in acc.split("\n") if re.search(r"\d+(\.\d+)?\s*:\s*1", l)]

    def disclosed(f):
        """Named on a line that states this pair's own measured ratio."""
        if not acc_lines:
            return False
        fg_name = (f["pair"].split(" on ")[0] if "pair" in f
                   else f.get("component", "")).lower()
        target = f["fg"].lower()
        for line in acc_lines:
            if not ((fg_name and fg_name in line) or target in line):
                continue
            for stated in re.findall(r"(\d+(?:\.\d+)?)\s*:\s*1", line):
                if abs(float(stated) - f["ratio"]) <= 0.06:
                    return True
        return False

    seen, deduped = set(), []
    for f in fails:
        k = (f["fg"], f["bg"], f["required"])
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
            # Scan the whole clause, both sides: a prohibition can put its
            # negation after the verb just as easily as before it.
            start = line.rfind(".", 0, m.start()) + 1
            end = line.find(".", m.end())
            clause = line[start:end if end != -1 else len(line)]
            if not NEGATED.search(clause):
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
    NOT_DOCUMENTED = re.compile(
        r"not (captured|documented|extracted|observed|specified|stated|available)"
        r"|undocumented|unknown|n/?a\b", re.I)
    structured = "\n".join(line for line in comp.split("\n")
                           if (line.lstrip().startswith(("|", "-", "*"))
                               or re.search(r"\*\*[^*]+\*\*\s*[:—-]", line))
                           # A row that says the state was not captured is not
                           # documentation of that state.
                           and not NOT_DOCUMENTED.search(line))
    hay = structured.lower()
    r["states_documented"] = [w for w in STATE_WORDS if w in hay]
    r["states_missing"] = [w for w in STATE_WORDS if w not in hay]

    # --- score ----------------------------------------------------------
    r["score"] = {
        "tokens":   5 if not r["roles_missing"] else max(1, 5 - len(r["roles_missing"])),
        # Floored at 1 with no frontmatter: nothing was measured, so a 5 would
        # mean "nothing to find" rather than "nothing wrong".
        "refs":     (5 if not r["dangling_refs"] else 2) if groups else 1,
        # Scored on undisclosed failures only: documenting a frozen brand
        # failure is the required outcome, not a deduction.
        "contrast": (5 if not r["contrast_unresolved"]
                     else max(1, 5 - len(r["contrast_unresolved"]))) if groups else 1,
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
