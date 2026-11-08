#!/usr/bin/env python3
"""OCR the source PDF page-by-page and create a review index.

This is a transcription aid, NOT an answer-key verifier or final class/subject audit.
"""
from pathlib import Path
import csv, re, subprocess
import fitz

PDF = Path("Question bank.pdf")
OUT = Path("audit-output")
PAGES = OUT / "pages"
OUT.mkdir(exist_ok=True)
PAGES.mkdir(exist_ok=True)

if not PDF.exists():
    raise SystemExit("Source PDF not found at repository root: Question bank.pdf")

doc = fitz.open(PDF)
if len(doc) == 0:
    raise SystemExit("PDF contains no pages")

rows = []
all_text = []
class_patterns = {
    n: re.compile(rf"(?i)(?:class|grade|کلاس)\s*[-:]?\s*{n}(?!\d)")
    for n in range(3, 9)
}
for i, page in enumerate(doc, start=1):
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
    image_path = PAGES / f"page-{i:03d}.png"
    pix.save(image_path)
    result = subprocess.run(
        ["tesseract", str(image_path), "stdout", "-l", "eng+urd", "--psm", "6"],
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    text = result.stdout.strip()
    (PAGES / f"page-{i:03d}.txt").write_text(text, encoding="utf-8")
    image_path.unlink(missing_ok=True)
    found = [str(n) for n, pat in class_patterns.items() if pat.search(text)]
    rows.append({
        "pdf_page": i,
        "width_pt": round(page.rect.width, 1),
        "height_pt": round(page.rect.height, 1),
        "ocr_chars": len(text),
        "possible_class_mentions": ";".join(found),
        "manual_review": "YES"
    })
    all_text.append(f"\n\n===== PDF PAGE {i} =====\n{text}")
    print(f"OCR page {i}/{len(doc)}", flush=True)

(OUT / "all_pages_ocr.txt").write_text("".join(all_text), encoding="utf-8")
with (OUT / "page_index.csv").open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

counts = {str(n): sum(str(n) in row["possible_class_mentions"].split(";") for row in rows) for n in range(3, 9)}
report = [
    "# Question Bank PDF — Automated OCR Run",
    "",
    f"- Source: {PDF.name}",
    f"- Pages processed: **{len(doc)}**",
    "- OCR language: eng+urd",
    "- Page images rendered at 2x PDF point scale.",
    f"- Pages with no OCR text: **{sum(row['ocr_chars'] == 0 for row in rows)}**",
    "",
    "## Possible class-heading mentions (OCR only)",
    "",
    "| Class marker | Pages containing a possible marker |",
    "|---|---:|",
]
report += [f"| Class {n} | {counts[str(n)]} |" for n in range(3, 9)]
report += [
    "",
    "## Important limitations",
    "",
    "- This is machine OCR, not a human-verified transcription.",
    "- A class mention may be part of a question or OCR error; it does not prove the page belongs to that class.",
    "- Student names, page-group boundaries, subject labels, MCQ options and answer marks require visual verification against the original page.",
    "- Duplicate detection and independent answer verification have NOT been performed by this workflow.",
    "- Do not import OCR output directly into the live portal.",
    "",
    "## Output files",
    "",
    "- all_pages_ocr.txt: OCR text with page separators.",
    "- page_index.csv: per-page metadata and possible class markers.",
    "- pages/: per-page OCR text files.",
    "",
    "## Required next review",
    "",
    "Manually build student-to-page groups, transcribe MCQs and options, classify subjects, verify answers independently, and then perform exact/near-duplicate review. Keep unresolved items out of the live practice bank."
]
(OUT / "AUDIT_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
print(f"Finished: {len(doc)} pages", flush=True)
