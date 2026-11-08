#!/usr/bin/env python3
"""Prepare a visual/OCR review pack for Class 4 candidate pages.
This does not certify answers or publish questions.
"""
from pathlib import Path
import subprocess, csv
import fitz

PDF=Path("Question bank.pdf")
OUT=Path("class4-review")
OUT.mkdir(exist_ok=True)
PAGES=[32,33,34,38,39,40,165,166,167,168,169,170,232,233,234,238,239,240]
doc=fitz.open(PDF)
rows=[]
chunks=[]
for n in PAGES:
    page=doc[n-1]
    image=OUT/f"page-{n:03d}.png"
    page.get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(image)
    proc=subprocess.run(["tesseract",str(image),"stdout","-l","eng+urd","--psm","6"],text=True,capture_output=True)
    txt=proc.stdout.strip()
    (OUT/f"page-{n:03d}.txt").write_text(txt,encoding="utf-8")
    rows.append({"pdf_page":n,"ocr_chars":len(txt),"review_status":"NOT_VISUALLY_VERIFIED"})
    chunks.append(f"\n\n===== PDF PAGE {n} =====\n{txt}")
    print(f"Class 4 review page {n}",flush=True)
(OUT/"CLASS4_CANDIDATE_PAGES_OCR.txt").write_text("".join(chunks),encoding="utf-8")
with (OUT/"CLASS4_PAGE_INDEX.csv").open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(OUT/"README.md").write_text("""# Class 4 review pack

Candidate pages: 32–34, 38–40, 165–170, 232–234, 238–240.

Expected approved subjects only: English, Urdu, Mathematics (3 questions each).

This pack contains OCR text and original page renders for visual review. OCR is not authoritative. Do not publish any item until stem/options are checked against the page image, answer solved independently, duplicate status checked, and the relevant Class 4 subject SLO mapped defensibly.
""",encoding="utf-8")
