#!/usr/bin/env python3
"""Generate theme-audit/roster.md: one row per site, with an inferred intent
and a motion profile assigned by the rule set in SPEC.md section 5."""
import glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CINEMATIC_SIGNAL = re.compile(
    r"automotive|hypercar|luxury|motorsport|console|cinematic|film|space|"
    r"aerospace|premium|watch|fragrance|hardware flagship", re.I)
CRISP_SIGNAL = re.compile(
    r"terminal|\bIDE\b|developer|infrastructure|devops|database|code editor|"
    r"\bCLI\b|observability|monitoring|deployment|API|open-source|analytics|"
    r"documentation|agent framework", re.I)
PLAYFUL_SIGNAL = re.compile(
    r"illustration|playful|friendly|colorful|colourful|whimsical|mascot|"
    r"hedgehog|multi-colour|multi-color|pastel|candy|rainbow", re.I)

AUTOMOTIVE = {"bmw", "bmw-m", "bugatti", "ferrari", "lamborghini", "renault", "tesla"}
DEVTOOL = {"cursor", "expo", "raycast", "superhuman", "vercel", "warp", "ollama",
           "opencode.ai", "clickhouse", "composio", "hashicorp", "mongodb",
           "posthog", "sanity", "sentry", "supabase", "replicate", "resend",
           "together.ai", "voltagent", "x.ai", "mintlify", "linear.app",
           "cohere", "minimax", "mistral.ai"}
# airtable was here until agent A03 argued it out on evidence from the file:
# its own description says sober and editorial, display weight is 400 with an
# explicit Don't against bolding, gradients are forbidden, and the bright tones
# are static card backgrounds rather than interactive surfaces. Rule 3 had been
# firing on colour count. See SPEC section 5.
PLAYFUL = {"figma", "miro", "zapier", "lovable", "clay", "pinterest",
           "nintendo-2001", "starbucks", "slack", "intercom", "mydealz"}
CINEMATIC = AUTOMOTIVE | {"apple", "spacex", "playstation", "nike", "spotify",
                          "shopify", "runwayml", "elevenlabs", "revolut",
                          "lamborghini", "dji", "oura", "meta", "nvidia"}


def luminance(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    h = h[:6]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    fm, body = text[4:end], text[end + 5:]
    groups, cur = {}, None
    for line in fm.split("\n"):
        m = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            cur = m.group(1); groups.setdefault(cur, {})
            if m.group(2).strip():
                groups[cur]["__inline__"] = m.group(2).strip()
            continue
        m = re.match(r"^  ([A-Za-z0-9][A-Za-z0-9_.-]*):\s*(.*)$", line)
        if m and cur:
            groups[cur][m.group(1)] = m.group(2).strip().strip('"')
    return groups, body


def intent(site, groups, text):
    desc = groups.get("description", {}).get("__inline__", "")
    if not desc:
        m = re.search(r"^## (?:1\. )?(?:Visual Theme|Overview).*?\n+(.+?)(?:\.|\n)", text, re.S | re.M)
        desc = m.group(1) if m else site
    desc = re.sub(r"[*`{}]", "", desc)
    words = desc.split()
    return " ".join(words[:9]).rstrip(",.;:—-")


def profile(site, groups, text):
    if site in CINEMATIC:
        return "Cinematic"
    if site in DEVTOOL:
        return "Crisp"
    if site in PLAYFUL:
        return "Playful"
    blob = (groups.get("description", {}).get("__inline__", "") + " " + text[:4000])
    canvas = None
    for k, v in groups.get("colors", {}).items():
        if re.match(r"^(canvas|background|bg|base|page|paper)", k) and v.startswith("#"):
            canvas = v; break
    dark = canvas is not None and luminance(canvas) < 0.2
    if dark and CINEMATIC_SIGNAL.search(blob):
        return "Cinematic"
    if CRISP_SIGNAL.search(blob):
        return "Crisp"
    if PLAYFUL_SIGNAL.search(blob):
        return "Playful"
    return "Calm"


rows = []
for path in sorted(glob.glob(os.path.join(ROOT, "design-md/*/DESIGN.md"))):
    site = os.path.basename(os.path.dirname(path))
    text = open(path).read()
    groups, body = frontmatter(text)
    rows.append({
        "agent": "",
        "site": site,
        "intent": intent(site, groups, text),
        "owned": f"design-md/{site}/DESIGN.md",
        "profile": profile(site, groups, text),
        "legacy": not bool(groups),
    })
for i, r in enumerate(rows, 1):
    r["agent"] = f"A{i:02d}"

with open(os.path.join(ROOT, "theme-audit/roster.json"), "w") as f:
    json.dump(rows, f, indent=2)

lines = ["# Roster", "",
         f"{len(rows)} sites, one agent each. Profiles assigned by SPEC.md section 5.",
         "`legacy` marks the files with no frontmatter token block.", "",
         "| Agent | Site | Intent | Owned file | Motion profile | Legacy |",
         "|---|---|---|---|---|---|"]
for r in rows:
    lines.append(f"| {r['agent']} | `{r['site']}` | {r['intent']} | `{r['owned']}` | "
                 f"{r['profile']} | {'yes' if r['legacy'] else ''} |")
counts = {}
for r in rows:
    counts[r["profile"]] = counts.get(r["profile"], 0) + 1
lines += ["", "## Profile distribution", ""]
for k in sorted(counts, key=lambda k: -counts[k]):
    lines.append(f"- **{k}**: {counts[k]}")
open(os.path.join(ROOT, "theme-audit/roster.md"), "w").write("\n".join(lines) + "\n")
print(f"{len(rows)} rows")
for k in sorted(counts, key=lambda k: -counts[k]):
    print(f"  {k}: {counts[k]}")
print("legacy:", sum(1 for r in rows if r["legacy"]))
