#!/usr/bin/env python3
"""Create Class 5 original-page renders and OCR review pack; no questions auto-published."""
from pathlib import Path
import subprocess,csv
import fitz
PDF=Path("Question bank.pdf"); OUT=Path("class5-review"); OUT.mkdir(exist_ok=True)
PAGES=[29,30,31,77,78,79,80,81,82,138,139,140,144,145,146,147,148,149,244,245,246]
doc=fitz.open(PDF); rows=[]; chunks=[]
for n in PAGES:
    image=OUT/f"page-{n:03d}.png"
    doc[n-1].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(image)
    p=subprocess.run(["tesseract",str(image),"stdout","-l","eng+urd","--psm","6"],text=True,capture_output=True)
    txt=p.stdout.strip()
    (OUT/f"page-{n:03d}.txt").write_text(txt,encoding="utf-8")
    rows.append({"pdf_page":n,"ocr_chars":len(txt),"review_status":"NOT_VISUALLY_VERIFIED"})
    chunks.append(f"\n\n===== PDF PAGE {n} =====\n{txt}")
    print(f"Class 5 review page {n}",flush=True)
(OUT/"CLASS5_CANDIDATE_PAGES_OCR.txt").write_text("".join(chunks),encoding="utf-8")
with (OUT/"CLASS5_PAGE_INDEX.csv").open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(OUT/"README.md").write_text("""# Class 5 review pack
Candidate pages: 29–31, 77–82, 138–149, 244–246.
Approved subjects only: English, Urdu, Mathematics; 3 questions each.
OCR is only a review aid. Verify every stem and all four options against page images, solve answers independently, check duplicates and map skills to defensible Class 5 outcomes before publication.
""",encoding="utf-8")
