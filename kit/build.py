#!/usr/bin/env python3
"""
build.py — regenerates the interactive study guide from the master markdown.

Everything in the app (sections, recall cards, search index, progress grid) is
derived from the markdown. Edit the markdown, rerun this, and the app follows.
The quiz bank and the page design live in quiz.json and template.html beside
this script.

Usage:
    python3 build.py
    python3 build.py --guide PATH.md --out PATH.html

Requires: pip install markdown --break-system-packages
"""

import argparse, html as ihtml, json, os, re, sys

try:
    import markdown
except ImportError:
    sys.exit("Missing dependency. Run:\n  pip install markdown --break-system-packages")

HERE = os.path.dirname(os.path.abspath(__file__))

ap = argparse.ArgumentParser()
ap.add_argument("--guide", default="/mnt/user-data/outputs/Network_Plus_N10-009_Master_Study_Guide.md")
ap.add_argument("--out",   default="/mnt/user-data/outputs/netplus_interactive.html")
ap.add_argument("--template", default=os.path.join(HERE, "template.html"))
ap.add_argument("--quiz",     default=os.path.join(HERE, "quiz.json"))
A = ap.parse_args()

for p, what in ((A.guide, "guide markdown"), (A.template, "template"), (A.quiz, "quiz bank")):
    if not os.path.exists(p):
        sys.exit("Cannot find %s at: %s" % (what, p))

raw = open(A.guide, encoding="utf-8").read()

# ---------- split into sections ----------
sections, part, buf, title = [], "Overview", [], None

def flush():
    if title is not None:
        sections.append({"part": part, "title": title, "md": "\n".join(buf).strip()})

for ln in raw.split("\n"):
    if ln.startswith("# PART") or ln.strip() == "# APPENDICES":
        flush(); buf, title = [], None
        part = ln[2:].strip()
        if part == "APPENDICES":
            part = "Appendices"
        continue
    if ln.startswith("# "):
        continue
    if ln.startswith("## "):
        flush(); buf = []
        title = ln[3:].strip()
        continue
    buf.append(ln)
flush()

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])

PIN  = "\U0001F4CC"
TRAP = "\u26A0\uFE0F"
CALLOUT_RE = re.compile(r"<p>((?:\s*(?:" + PIN + "|" + TRAP + r"|\u2705|\u274C))+)\s*(.*?)</p>", re.S)
LAB_RE   = re.compile(r"(<h3>\U0001F527\s*LAB.*?</h3>\s*<p>.*?</p>)", re.S)
TABLE_RE = re.compile(r"(<table>.*?</table>)", re.S)

def classify(marks):
    pin, trap = PIN in marks, TRAP in marks
    if pin and trap: return "both", "pin"
    if trap:         return "trap", "trap"
    return "pin", "pin"

data = []
for i, s in enumerate(sections):
    body = md.reset().convert(s["md"])
    callouts = []

    def repl(m):
        marks, inner = m.group(1), m.group(2)
        cls, kind = classify(marks)
        callouts.append({"kind": kind, "html": inner.strip()})
        return '<div class="callout %s"><p>%s %s</p></div>' % (cls, marks.strip(), inner)

    body = CALLOUT_RE.sub(repl, body)
    body = LAB_RE.sub(lambda m: '<div class="lab">%s</div>' % m.group(1), body)
    body = TABLE_RE.sub(lambda m: '<div class="tablewrap">%s</div>' % m.group(1), body)

    t = s["title"]
    mnum = re.match(r"^(\d+\.\d+)\s+(.*)$", t)
    mapp = re.match(r"^Appendix ([A-Z])\s*[\u2014-]\s*(.*)$", t)
    if mnum:   num, short = mnum.group(1), mnum.group(2)
    elif mapp: num, short = mapp.group(1), mapp.group(2)
    else:      num, short = "\u2022", t
    short = short if len(short) <= 34 else short[:32].rstrip() + "\u2026"

    plain = ihtml.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)))

    data.append({"id": "s%02d" % i, "num": num, "title": t, "short": short,
                 "part": s["part"], "html": body, "text": plain[:6000],
                 "callouts": callouts})

# ---------- port bank (drives the Ports drill) ----------
PORTS = [
 {"n":"FTP data","p":20,"t":"TCP","note":"Data channel; 21 carries the commands."},
 {"n":"FTP control","p":21,"t":"TCP","note":"Secured by FTPS (989/990), not by SFTP."},
 {"n":"SSH / SFTP / SCP","p":22,"t":"TCP","note":"SFTP runs over SSH \u2014 a different protocol from FTPS."},
 {"n":"Telnet","p":23,"t":"TCP","note":"Cleartext including credentials. Replaced by SSH on 22."},
 {"n":"SMTP","p":25,"t":"TCP","note":"Sends mail only. Retrieval is POP3 or IMAP."},
 {"n":"DNS","p":53,"t":"TCP and UDP","note":"UDP for queries, TCP for zone transfers."},
 {"n":"DHCP server","p":67,"t":"UDP","note":"Client listens on 68. Discover is a broadcast."},
 {"n":"DHCP client","p":68,"t":"UDP","note":"Server listens on 67."},
 {"n":"TFTP","p":69,"t":"UDP","note":"No authentication, no directory browsing."},
 {"n":"HTTP","p":80,"t":"TCP","note":"Secured version is HTTPS on 443."},
 {"n":"POP3","p":110,"t":"TCP","note":"Downloads and usually removes mail from the server."},
 {"n":"NTP","p":123,"t":"UDP","note":"Clock skew breaks Kerberos and certificate validation."},
 {"n":"IMAP","p":143,"t":"TCP","note":"Keeps mail on the server and syncs across devices."},
 {"n":"SNMP query","p":161,"t":"UDP","note":"162 carries traps."},
 {"n":"SNMP trap","p":162,"t":"UDP","note":"Unsolicited alert pushed by the device."},
 {"n":"LDAP","p":389,"t":"TCP","note":"LDAPS is 636."},
 {"n":"HTTPS","p":443,"t":"TCP","note":"HTTP inside TLS."},
 {"n":"SMB","p":445,"t":"TCP","note":"Windows file and printer sharing. NFS is the Linux equivalent."},
 {"n":"Syslog","p":514,"t":"UDP","note":"Centralised logging."},
 {"n":"SMTP submission","p":587,"t":"TCP","note":"Authenticated submission with TLS."},
 {"n":"LDAPS","p":636,"t":"TCP","note":"LDAP over SSL/TLS."},
 {"n":"FTPS","p":"989/990","t":"TCP","note":"FTP wrapped in TLS \u2014 not the same as SFTP."},
 {"n":"IMAPS","p":993,"t":"TCP","note":"Secure IMAP."},
 {"n":"POP3S","p":995,"t":"TCP","note":"Secure POP3."},
 {"n":"Microsoft SQL Server","p":1433,"t":"TCP","note":""},
 {"n":"MySQL","p":3306,"t":"TCP","note":""},
 {"n":"RDP","p":3389,"t":"TCP","note":"Never expose directly to the internet."},
 {"n":"SIP","p":"5060/5061","t":"TCP/UDP","note":"VoIP signalling; 5061 is the secure port."},
]

QUIZ = json.load(open(A.quiz, encoding="utf-8"))
tpl  = open(A.template, encoding="utf-8").read()

out = (tpl.replace("__DATA__",  json.dumps(data,  ensure_ascii=False))
          .replace("__QUIZ__",  json.dumps(QUIZ,  ensure_ascii=False))
          .replace("__PORTS__", json.dumps(PORTS, ensure_ascii=False)))

d = os.path.dirname(A.out)
if d:
    os.makedirs(d, exist_ok=True)
open(A.out, "w", encoding="utf-8").write(out)

print("sections : %d" % len(data))
print("callouts : %d  (recall cards)" % sum(len(x["callouts"]) for x in data))
print("quiz     : %d questions" % len(QUIZ))
print("ports    : %d" % len(PORTS))
print("size     : %.2f MB" % (len(out) / 1024 / 1024))
print("written  : %s" % A.out)
