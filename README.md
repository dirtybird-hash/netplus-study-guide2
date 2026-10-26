# CompTIA Network+ (N10-009) Study Guide

A written study guide and a self-contained interactive study app, organised by exam objective.

**Open `index.html` in any browser.** No install, no build step, no internet connection required.

---

## What's here

| Path | What it is |
|---|---|
| `index.html` | The interactive study app. One self-contained file |
| `Network_Plus_N10-009_Master_Study_Guide.md` | **The source of truth.** All guide content lives here |
| `kit/build.py` | Regenerates `index.html` from the markdown |
| `kit/template.html` | Page design, CSS, and app logic |
| `kit/quiz.json` | 108 hand-written practice questions |
| `kit/scan.py` | Pre-merge triage for new source material |
| `kit/UPDATE.md` | **Read this before changing anything** |

---

## The interactive app

Six modes, all generated from the markdown so nothing drifts out of sync:

- **Read** — 36 sections, searchable, with a per-section notes box that autosaves
- **Ports** — drills both directions: type the number given a protocol, pick the protocol given a number
- **Subnetting** — endlessly generated problems, graded field by field, with the magic-number working shown afterwards
- **Cards** — 292 recall cards auto-extracted from every 📌 and ⚠️ marker in the guide
- **Quiz** — 108 questions across all five domains, each explaining its reasoning
- **Progress** — section grid, card counts, drill accuracy, and notes export

The mode bar also links out to the **OSI Rack Trainer** (objective 1.1, seat each module in the
right layer), a separate app at https://dirtybird-hash.github.io/osi-rack-trainer/. It is a link
in `kit/template.html`, not a generated view, and keeps its own saved progress.

### Notes on storage

Progress and notes are kept in **browser localStorage**. That means they are:

- Private to you — nothing is uploaded anywhere
- **Per-device and per-browser** — they do not sync between your laptop and your phone

Use **Export my notes** on the Progress tab before moving between devices.

---

## Coverage

Structured to the published CompTIA N10-009 objectives.

| Domain | Weight | Sections |
|---|---|---|
| 1.0 Networking Concepts | 23% | 1.1 – 1.8 |
| 2.0 Infrastructure | 20% | 2.1 – 2.4 |
| 3.0 Network Operations | 19% | 3.1 – 3.5 |
| 4.0 Network Security | 14% | 4.1 – 4.3 |
| 5.0 Troubleshooting & Tools | 24% | 5.1 – 5.5 |

Plus seven appendices: port drill sheet, subnetting practice, command reference, acronym list, study plan, master symptom reference, and a page cross-reference to separately-purchased course notes.

Twenty-five lab stubs are marked 🔧 throughout, sized for Cisco Packet Tracer.

---

## Rebuilding after an edit

Edit the markdown, then:

```bash
pip install markdown --break-system-packages
python3 kit/build.py --guide Network_Plus_N10-009_Master_Study_Guide.md --out index.html
```

Never hand-edit `index.html` — it is generated and will be overwritten. See `kit/UPDATE.md` for the full merge procedure.

---

## Sources and licensing

Guide content is derived from personal course transcripts and original writing. Section 4.2 (attacks) and the performance material in 5.4 were written from scratch.

⚠️ **Professor Messer's course notes are not included and are not a source for this guide.** They are copyrighted and separately purchased. Appendix G maps this guide's sections to their page numbers so the two can be read side by side, but contains none of their content.

⚠️ **If you publish this repository publicly, your notes go public too.** Anything typed into the app's notes boxes lives in your browser rather than in these files, so it is not committed — but exported notes files would be. Keep the repo private if in doubt.
