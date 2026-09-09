#!/usr/bin/env python3
"""
scan.py — pre-merge triage for new Network+ transcripts.

Reads every file in the project folder, works out which guide section each one
belongs to, and reports what is genuinely new versus what the guide already
says. It does NOT change the guide. Its job is to turn "reread 250,000 words"
into "review a diff".

Usage:
    python3 scan.py                     # scan /mnt/project against the guide
    python3 scan.py --src DIR --guide FILE --out REPORT.md

Output: a markdown report listing, per file:
    - detected real format (extensions lie; several source files are ZIPs)
    - target guide section(s)
    - overlap % against the existing section text
    - sentences that look new
    - candidate factual conflicts against anchor facts
"""

import argparse, io, os, re, sys, json, zipfile, hashlib
from collections import defaultdict

# ---------------------------------------------------------------- extraction

def sniff(path):
    """Return the real format, ignoring the extension."""
    with open(path, "rb") as f:
        head = f.read(8)
    if head[:4] == b"PK\x03\x04":
        try:
            names = zipfile.ZipFile(path).namelist()
        except Exception:
            return "zip-unreadable"
        if any(n.startswith("word/") for n in names):
            return "docx"
        if any(n.startswith("ppt/") for n in names):
            return "pptx"
        if any(n.endswith(".txt") for n in names):
            return "zip-transcript"
        return "zip-other"
    if head[:5] == b"%PDF-":
        return "pdf"
    return "text"


def extract(path, kind):
    """Return plain text, or '' if we cannot read it."""
    try:
        if kind == "zip-transcript":
            z = zipfile.ZipFile(path)
            txts = [n for n in z.namelist() if n.endswith(".txt")]
            def key(n):
                m = re.match(r"(\d+)", os.path.basename(n))
                return int(m.group(1)) if m else 0
            return "\n".join(z.read(t).decode("utf-8", "ignore")
                             for t in sorted(txts, key=key))

        if kind == "docx":
            z = zipfile.ZipFile(path)
            xml = z.read("word/document.xml").decode("utf-8", "ignore")
            xml = re.sub(r"</w:p>", "\n", xml)
            return re.sub(r"<[^>]+>", "", xml)

        if kind == "pptx":
            z = zipfile.ZipFile(path)
            out = []
            slides = sorted(n for n in z.namelist()
                            if re.match(r"ppt/slides/slide\d+\.xml$", n))
            for s in slides:
                xml = z.read(s).decode("utf-8", "ignore")
                xml = re.sub(r"</a:p>", "\n", xml)
                out.append(re.sub(r"<[^>]+>", "", xml))
            return "\n".join(out)

        if kind == "pdf":
            try:
                import pypdf
            except ImportError:
                return ""
            r = pypdf.PdfReader(path)
            return "\n".join(p.extract_text() or "" for p in r.pages)

        return open(path, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        return ""


def norm(t):
    t = t.replace("\u2019", "'").replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", t).strip()


# ---------------------------------------------------------------- guide model

def load_guide(path):
    """Split the master guide into sections keyed by objective number."""
    raw = open(path, encoding="utf-8").read()
    secs, part, title, buf = [], "Overview", None, []

    def flush():
        if title is not None:
            secs.append({"part": part, "title": title,
                         "text": norm("\n".join(buf))})

    for ln in raw.split("\n"):
        if ln.startswith("# PART") or ln.strip() == "# APPENDICES":
            flush(); buf, title = [], None
            part = ln[2:].strip()
            continue
        if ln.startswith("# "):
            continue
        if ln.startswith("## "):
            flush(); buf = []
            title = ln[3:].strip()
            continue
        buf.append(ln)
    flush()

    for s in secs:
        m = re.match(r"^(\d+\.\d+)\s", s["title"])
        s["num"] = m.group(1) if m else None
    return secs


# Day-format fallback map (the original transcript naming).
DAY_MAP = {
    1: ["1.1"], 2: ["1.6", "2.3", "1.5"], 3: ["1.5"], 4: ["1.2"],
    5: ["2.1", "2.3"], 6: ["1.7"], 7: ["1.7"], 8: ["2.1", "2.2"],
    9: ["2.2", "2.4"], 10: ["1.4"], 11: ["1.8"], 12: ["5.2", "5.3"],
    13: ["3.3"], 14: ["3.1", "3.2", "3.4"], 15: ["4.1", "4.2", "4.3", "4.4"],
    16: ["3.2", "3.3", "5.1"], 17: ["2.3", "2.4"], 18: ["1.3", "3.4"],
}

# Keyword fallback when the filename tells us nothing.
KEYWORDS = {
    "1.1": ["osi", "layer", "encapsulation"],
    "1.2": ["firewall", "load balancer", "proxy", "ids", "ips", "nas", "san", "cdn"],
    "1.3": ["cloud", "iaas", "paas", "saas", "elasticity", "multitenancy"],
    "1.4": ["port", "protocol", "smtp", "imap", "dns", "dhcp"],
    "1.5": ["cable", "fiber", "fibre", "connector", "transceiver", "cat 6", "single-mode"],
    "1.6": ["topology", "spine", "leaf", "mesh", "star", "east-west", "three-tier"],
    "1.7": ["subnet", "ipv4", "ipv6", "cidr", "vlsm", "nat", "apipa"],
    "1.8": ["sdn", "sd-wan", "vxlan", "zero trust", "sase", "infrastructure as code"],
    "2.1": ["vlan", "spanning tree", "stp", "trunk", "poe", "port security", "802.1q"],
    "2.2": ["routing", "ospf", "bgp", "eigrp", "rip", "fhrp", "hsrp", "vrrp"],
    "2.3": ["wireless", "wifi", "wi-fi", "wpa", "ssid", "antenna", "802.11"],
    "2.4": ["rack", "mdf", "idf", "hvac", "voip", "iot", "scada", "patch panel"],
    "3.1": ["dhcp", "dns", "ntp", "vpn", "jump server", "out-of-band"],
    "3.2": ["snmp", "syslog", "netflow", "baseline", "monitoring", "uptime"],
    "3.3": ["disaster recovery", "high availability", "rpo", "rto", "mtbf", "backup", "cold site"],
    "3.4": ["change management", "ipam", "asset", "policy", "documentation", "end of life"],
    "4.1": ["encryption", "risk", "honeypot", "compliance", "cia"],
    "4.2": ["segmentation", "802.1x", "radius", "tacacs", "acl", "access control"],
    "4.3": ["physical security", "mantrap", "badge", "geofencing", "camera"],
    "4.4": ["hardening", "password", "default credential", "firewall rule"],
    "5.1": ["methodology", "probable cause", "escalate", "theory"],
    "5.2": ["ping", "traceroute", "ipconfig", "nmap", "wireshark", "tdr", "tool"],
    "5.3": ["crosstalk", "duplex mismatch", "duplicate ip", "certificate", "symptom"],
}


def target_sections(fname, text):
    """Best guess at which guide sections a file belongs to."""
    base = os.path.basename(fname)

    nums = re.findall(r"(?<!\d)([1-5]\.\d)(?!\d)", base)
    if nums:
        return sorted(set(nums)), "filename objective number"

    m = re.match(r"[Dd]ay[_\s-]*(\d+)", base)
    if m and int(m.group(1)) in DAY_MAP:
        return DAY_MAP[int(m.group(1))], "Day-format filename"

    low = (base + " " + text[:20000]).lower()
    scored = []
    for num, kws in KEYWORDS.items():
        hits = sum(low.count(k) for k in kws)
        if hits:
            scored.append((hits, num))
    scored.sort(reverse=True)
    if scored:
        top = [n for h, n in scored[:3] if h >= scored[0][0] * 0.3]
        return top, "keyword match (verify this)"
    return [], "UNMAPPED - assign manually"


# ---------------------------------------------------------------- comparison

def sentences(t):
    parts = re.split(r"(?<=[.!?])\s+", t)
    return [norm(p) for p in parts if len(norm(p).split()) >= 6]


def shingles(t, n=5):
    w = re.findall(r"[a-z0-9]+", t.lower())
    return {hashlib.md5(" ".join(w[i:i + n]).encode()).hexdigest()[:12]
            for i in range(max(0, len(w) - n + 1))}


STOP = set("""the a an and or but if of to in on for with as is are was were be been being it its this that
these those we you they he she i not no can will would should could may might have has had do does did
so then than there here what which who when where how why all any some more most other into over under
about after before because while during through very just also only even much many such own same both
each few own too s t don now use used using one two three first second next last new old good great""".split())

def content_terms(t, top=None, minfreq=1):
    """
    Distinctive vocabulary, robust to paraphrasing.
    With `top`, returns only the N most frequent terms — the document's
    dominant concepts. A verbose transcript carries a long tail of incidental
    vocabulary that a condensed guide section rightly drops, so comparing full
    vocabularies understates coverage badly.
    """
    words = re.findall(r"[a-z][a-z0-9\-\.]{2,}", t.lower())
    freq = defaultdict(int)
    for w in words:
        if w not in STOP and not w.isdigit() and len(w) > 2:
            freq[w] += 1
    items = [(n, w) for w, n in freq.items() if n >= minfreq]
    items.sort(reverse=True)
    if top:
        items = items[:top]
    return {w for _, w in items}


def coverage(new_text, guide_text):
    """
    Two numbers, measuring different things:
      concept  - share of the new file's 100 dominant concepts already present
                 in the guide section. Survives paraphrasing. Trust this one
                 when deciding whether material is already covered.
      verbatim - share of 5-word sequences reused. Near zero is normal and
                 healthy: the guide is written in its own words. A high number
                 means text was copied rather than digested.
    """
    nt = content_terms(new_text, top=100, minfreq=2)
    gt = content_terms(guide_text)
    concept = (len(nt & gt) / len(nt) * 100) if nt else 0.0

    a, b = shingles(new_text), shingles(guide_text)
    verbatim = (len(a & b) / len(a) * 100) if a else 0.0
    return concept, verbatim


# A protocol's legitimate port set. A number outside this set, attributed to
# this protocol, is a real conflict. Numbers inside it are not.
PROTO_PORTS = {
    "ftp": {"20", "21"}, "sftp": {"22"}, "ftps": {"989", "990"},
    "ssh": {"22"}, "scp": {"22"}, "telnet": {"23"},
    "smtp": {"25", "587", "465"}, "dns": {"53"},
    "dhcp": {"67", "68"}, "tftp": {"69"},
    "http": {"80"}, "https": {"443"},
    "pop3": {"110", "995"}, "ntp": {"123"}, "imap": {"143", "993"},
    "snmp": {"161", "162"}, "ldap": {"389", "636"}, "ldaps": {"636"},
    "smb": {"445"}, "syslog": {"514"}, "rdp": {"3389"},
    "sip": {"5060", "5061"}, "vnc": {"5900"},
    "mysql": {"3306"}, "sql": {"1433", "3306"},
}

# Non-port facts: term, the value(s) the guide asserts, and the unit that must
# appear nearby for the number to count as the same kind of claim.
FACT_ANCHORS = [
    ("ethernet maximum distance", {"100"}, r"met(?:er|re)s?",
     r"ethernet.{0,60}(?:distance|length|limit)|(?:distance|length|limit).{0,60}ethernet"),
    ("horizontal run limit",      {"90"},  r"met(?:er|re)s?", r"horizontal run|equipment room"),
    ("standard MTU",              {"1500"}, r"byte", r"\bmtu\b"),
    ("jumbo frame size",          {"9000"}, r"byte", r"jumbo"),
    ("VLAN maximum",              {"4096", "4000"}, r"vlan", r"maximum.{0,40}vlan|vlan.{0,40}maximum"),
    ("RIP maximum hops",          {"15", "16"}, r"hop", r"\brip\b"),
    ("IPv6 address length",       {"128"}, r"bit", r"ipv6"),
    ("IPv4 address length",       {"32"},  r"bit", r"ipv4"),
]

PORT_RE = re.compile(r"\bport\s*(?:number\s*)?(\d{2,5})\b")


def find_conflicts(text):
    """
    Walk every explicit 'port N' mention, attribute it to the nearest protocol
    name, and flag only genuine mismatches. Attributing by proximity is what
    stops SFTP-on-22 or SNMP-on-162 being reported as errors.
    """
    low = text.lower()
    out, seen = [], set()

    for m in PORT_RE.finditer(low):
        num = m.group(1)
        lo, hi = max(0, m.start() - 130), m.end() + 130
        window = low[lo:hi]

        nearest, dist = None, 10**6
        for proto in PROTO_PORTS:
            for pm in re.finditer(r"\b" + re.escape(proto) + r"\b", window):
                d = abs((pm.start() + lo) - m.start())
                if d < dist:
                    nearest, dist = proto, d
        if not nearest:
            continue
        if num in PROTO_PORTS[nearest]:
            continue
        key = (nearest, num)
        if key in seen:
            continue
        seen.add(key)
        out.append(("port: " + nearest, sorted(PROTO_PORTS[nearest]), [num],
                    norm(text[lo:hi])))

    for label, expected, unit, subject in FACT_ANCHORS:
        for m in re.finditer(subject, low):
            lo, hi = max(0, m.start() - 130), m.end() + 130
            window = low[lo:hi]
            if not re.search(unit, window):
                continue
            nums = {n.replace(",", "") for n in re.findall(r"\b\d[\d,]*\b", window)}
            if nums & expected or not nums:
                break
            if ("fact", label) in seen:
                break
            seen.add(("fact", label))
            out.append((label, sorted(expected), sorted(nums)[:5],
                        norm(text[lo:hi])))
            break
    return out


# ---------------------------------------------------------------- report

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="/mnt/project")
    ap.add_argument("--guide",
                    default="/mnt/user-data/outputs/Network_Plus_N10-009_Master_Study_Guide.md")
    ap.add_argument("--out", default="/mnt/user-data/outputs/scan_report.md")
    ap.add_argument("--textdir", default="/home/claude/scan_text")
    a = ap.parse_args()

    if not os.path.exists(a.guide):
        sys.exit("Guide not found: %s\nPoint --guide at the master markdown file." % a.guide)

    secs = load_guide(a.guide)
    by_num = {s["num"]: s for s in secs if s["num"]}
    os.makedirs(a.textdir, exist_ok=True)

    files = sorted(f for f in os.listdir(a.src)
                   if not f.startswith(".") and
                   os.path.isfile(os.path.join(a.src, f)))

    seen_hash = {}
    rows, L = [], []
    L.append("# Transcript scan report\n")
    L.append("Source: `%s`  ·  Guide: `%s`\n" % (a.src, os.path.basename(a.guide)))
    L.append("**This report changes nothing.** It is triage for a merge pass.\n")
    L.append("---\n")

    for fn in files:
        path = os.path.join(a.src, fn)
        kind = sniff(path)
        text = norm(extract(path, kind))
        words = len(text.split())

        h = hashlib.md5(re.sub(r"[^a-z0-9]", "", text.lower())[:20000].encode()).hexdigest()
        dup_of = seen_hash.get(h)
        seen_hash.setdefault(h, fn)

        targets, how = target_sections(fn, text)
        rows.append((fn, kind, words, ",".join(targets) or "-"))

        L.append("## %s\n" % fn)
        L.append("- **Real format:** `%s`%s" %
                 (kind, "  ⚠️ extension does not match" if kind.startswith("zip") and fn.lower().endswith(".pdf") else ""))
        L.append("- **Words extracted:** %s" % ("{:,}".format(words) if words else "0  ⚠️ nothing readable — may need OCR"))
        L.append("- **Target section(s):** %s  *(%s)*" % (", ".join(targets) or "none", how))

        if dup_of:
            L.append("- 🔁 **Appears to duplicate `%s`** — same opening content. Confirm before merging.\n" % dup_of)
            continue
        if not words:
            L.append("")
            continue

        open(os.path.join(a.textdir, fn + ".txt"), "w").write(text)

        for t in targets:
            g = by_num.get(t)
            if not g:
                L.append("- Section %s not found in the guide — new section?" % t)
                continue
            con, ver = coverage(text, g["text"])
            L.append("  - vs %s %s: %.0f%% concept, %.0f%% verbatim" %
                     (t, g["title"], con, ver))

        gtext = " ".join(by_num[t]["text"] for t in targets if t in by_num)
        if gtext:
            ucon, uver = coverage(text, gtext)
            verdict = ("mostly already covered — expect little to merge" if ucon >= 65 else
                       "substantial new material" if ucon < 40 else
                       "partial — read the unmatched sentences before deciding")
            L.insert(len(L) - len([t for t in targets if t in by_num]),
                     "- **Combined coverage across target sections: %.0f%% concept, %.0f%% verbatim — %s**"
                     % (ucon, uver, verdict))
            if uver > 15:
                L.append("  - ⚠️ verbatim reuse above 15%% suggests copied text rather than digested material")
        gsh = shingles(gtext)
        new_lines = [s for s in sentences(text)
                     if len(shingles(s) - gsh) / max(1, len(shingles(s))) > 0.8]
        L.append("- **Sentences with no match in the guide:** %d" % len(new_lines))
        if new_lines:
            L.append("\n  <details><summary>show first 12</summary>\n")
            for s in new_lines[:12]:
                L.append("  - %s" % (s[:300] + ("…" if len(s) > 300 else "")))
            L.append("\n  </details>\n")

        cf = find_conflicts(text)
        if cf:
            L.append("- ⚠️ **Possible factual conflicts (%d)** — adjudicate each:\n" % len(cf))
            for term, exp, got, ctx in cf[:10]:
                L.append("  - `%s` — guide says **%s**, this file has %s near it" %
                         (term, "/".join(exp), ", ".join(got)))
                L.append("    > %s" % (ctx[:260] + ("…" if len(ctx) > 260 else "")))
        else:
            L.append("- No anchor-fact conflicts detected.")
        L.append("")

    L.append("---\n\n## Inventory\n")
    L.append("| File | Format | Words | Targets |")
    L.append("|---|---|---|---|")
    for r in rows:
        L.append("| %s | `%s` | %s | %s |" % (r[0], r[1], "{:,}".format(r[2]), r[3]))

    L.append("\n## Next step\n")
    L.append("Work `UPDATE.md`. Merge section by section, log every change, then run `build.py`.")

    open(a.out, "w").write("\n".join(L))
    print("Scanned %d file(s). Report: %s" % (len(files), a.out))
    print("Extracted text cached in: %s" % a.textdir)


if __name__ == "__main__":
    main()
