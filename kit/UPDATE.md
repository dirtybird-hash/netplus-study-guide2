# UPDATE.md — how to merge new transcripts into the guide

Read this first. It is written for a future session (Claude or otherwise) picking this up with no memory of how the guide was built.

---

## What these files are

| File | Role |
|---|---|
| `Network_Plus_N10-009_Master_Study_Guide.md` | **The source of truth.** Everything else derives from it |
| `build.py` | Regenerates the interactive HTML from the markdown |
| `template.html` | Page design, CSS, and app logic. Contains `__DATA__`, `__QUIZ__`, `__PORTS__` placeholders |
| `quiz.json` | 92 hand-written practice questions. **Not derived from transcripts** — preserve these |
| `scan.py` | Pre-merge triage. Reports what is new, duplicated, or conflicting. Changes nothing |
| `UPDATE.md` | This file |

**Editing rule:** change the markdown, then rerun `build.py`. Never hand-edit the generated HTML — it gets overwritten.

---

## Setup

```bash
pip install markdown --break-system-packages
```

`scan.py` also uses `pypdf` for real PDFs. It degrades gracefully without it.

---

## The procedure

### 1. Triage

```bash
python3 scan.py
```

Reads `/mnt/project`, writes `scan_report.md`, caches extracted text in `/home/claude/scan_text/`.

Read the report before reading any transcript. It tells you:

- **Real format** — extensions lie. Several original files were ZIP archives named `.pdf`
- **Target sections** — from the filename objective number, the Day-format map, or keyword matching
- **Combined coverage** — the headline number. See calibration below
- **Sentences with no match** in the guide
- **Candidate factual conflicts**

⚠️ **Keyword-matched targets are guesses.** Verify them. Filename-derived targets are reliable.

### Reading the coverage numbers

Two figures are reported, and they measure different things.

**Concept coverage** — how many of the file's 100 dominant terms already appear in the target sections. This survives paraphrasing, which matters because the guide is written in its own words rather than copied.

Calibrated against the original 23 transcripts, all of which the guide was built from:

| Combined concept coverage | Meaning |
|---|---|
| **65% and above** | Mostly already covered. Expect little to merge |
| **40–65%** | Partial. Read the unmatched sentences before deciding |
| **Below 40%** | Substantial new material |

📌 Do not expect 90%+ even for fully-covered material. A 20,000-word transcript carries far more incidental vocabulary than a 2,500-word section legitimately keeps. The original corpus scores **56–85%**, and that range *is* what "already covered" looks like.

**Verbatim reuse** — share of five-word sequences reused. **Near zero is correct and healthy.** Anything above 15% means text was copied rather than digested, and the section should be rewritten in the guide's own voice.

### Reading the conflict flags

The detector walks every explicit "port N" mention and attributes it to the nearest protocol name, which avoids flagging legitimate cases like SFTP on 22 or SNMP on 162.

⚠️ **It is triage, not a verdict.** On the original corpus it produced five flags across 250,000 words. Roughly half were genuine (a transcript mentioning SMTP on 2525, which the guide omits) and half were sentences that merely mention a protocol and an unrelated number nearby. **Read the quoted context on every flag.** A flag is a prompt to look, never a conclusion.

### 2. Classify every overlap

For each file × section pair, one of three outcomes:

| Outcome | Signal | Action |
|---|---|---|
| **Additive** | Overlap under ~25%, many unmatched sentences | Merge the new material in |
| **Duplicate** | Overlap over ~60%, few unmatched sentences | Drop it. Keep existing prose. Log it as not merged |
| **Conflicting** | Anchor-fact flag, or new text contradicts existing | **Adjudicate — see below** |

Percentages are guidance, not a rule. A file with 70% overlap can still carry one genuinely new fact worth keeping.

### 3. Adjudicate conflicts

When two sources disagree, **do not average them and do not silently prefer the newer one.** Decide on merit:

1. Check the claim against authoritative knowledge of the N10-009 objectives
2. If the new source is right, correct the guide **and** add a row to *Corrections to the source transcripts*
3. If the old source is right, keep it and note in the changelog that the new source was wrong
4. If both are defensible (vendor differences, contested layer assignments), **present both** and say which the exam expects — the SSL/TLS layer discussion in section 1.1 is the model for this

📌 Three known transcript errors are already documented in the Corrections table. If new material contradicts a correction, re-verify rather than assuming the correction was wrong.

### 4. Merge

Rewrite the affected section as **one coherent narrative** — not an original block followed by an appended block. The reader should not be able to tell where the seam is.

Preserve while merging:

- `📌` memorize markers and `⚠️` exam-trap markers — these generate the recall cards
- `🔧 LAB` stubs at the end of each section — these mark the labs to expand
- `🔗` A+ crossover markers
- Cross-references to other sections, e.g. *(see 2.1)* — update them if content moves
- Table-heavy formatting. The app renders tables well and they drill better than prose

**Structural rules the build depends on:**

- Sections start with `## ` and objective sections must begin with the number: `## 4.2 Network Segmentation`
- Parts start with `# PART n — Name (Domain n.0, xx%)`
- Callouts must be their **own paragraph** starting with the emoji, or they will not become recall cards
- Lab stubs must be `### 🔧 LAB n.n — Title` followed by one paragraph

### 5. Log it

Add an entry at the top of the **Changelog** section, above the previous entry, using the table format shown there. Fill every field. "Nothing revised" is a valid entry; a blank field is not.

Also update the **Source transcript map** in the front matter with the new files.

### 6. Rebuild and verify

```bash
python3 build.py
```

Expect output like:

```
sections : 33
callouts : 291  (recall cards)
quiz     : 92 questions
```

Sanity checks:

- Section count rose only if you added sections
- Callout count rose roughly in line with new `📌`/`⚠️` markers — a **drop** means you broke callout formatting
- Quiz count is still 92 unless you deliberately added questions
- Size stays well under 16 MB

### 7. Consider the quiz bank

New material usually deserves new questions. Append to `quiz.json`:

```json
{"d":4,"s":"4.2","q":"Question text?","a":["Correct","Wrong","Wrong","Wrong"],"c":0,"e":"Why."}
```

- `d` = domain 1–5, `s` = section number shown to the user
- `c` = index of the correct answer in `a` (the app shuffles display order)
- `e` = explanation. Explain the reasoning, never just restate the answer

---

## Known gaps worth filling

| Gap | Why it matters |
|---|---|
| **Domain 4 (Security)** | 14% of the exam, thinnest source coverage. Attack types and cryptographic concepts are lightest |
| **Attack-specific content** | On-path, DDoS, social engineering, VLAN hopping, rogue DHCP are mentioned but not systematically covered |
| **IPv6 depth** | Adequate but light relative to how the exam treats it |

If incoming material covers any of these, prioritise it.

---

## Naming convention for new files

Best: `4.2_Network_Segmentation.pdf` — leading objective number, `scan.py` maps it automatically.

Spanning two objectives: `2.1-2.2_Switching_and_Routing.pdf`.

Legacy `Day_N_Topic` files still map via the built-in table in `scan.py`.

⚠️ If a new file **supersedes** an older one rather than adding to it, say so explicitly. `scan.py` detects near-identical duplicates but cannot know intent.

---

## What not to do

- Do not hand-edit the generated HTML
- Do not regenerate `quiz.json` — it is hand-written and would be lost
- Do not merge without logging
- Do not resolve a conflict by keeping both numbers without saying which is correct
- Do not let the guide drift out of objective order — the app sorts by document order, not by number
