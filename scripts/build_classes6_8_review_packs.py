#!/usr/bin/env python3
"""Render candidate source pages for visual audit; does not publish questions."""
from pathlib import Path
import subprocess,csv,fitz
PDF=Path("Question bank.pdf")
GROUPS={
6:[95,96,97,98,123,124,125,126,127,128,129,130],
7:[57,58,59,60,65,66,67,68,115,116,117,118,119,120,121,122,181,182,183,184,185,186,187,188],
8:[4,5,6,7,8,9,10,11,12,13,14,15,20,21,22,23,99,100,101,102,103,104,105,106],
}
doc=fitz.open(PDF)
for grade,pages in GROUPS.items():
 out=Path(f"class{grade}-review");out.mkdir(exist_ok=True); rows=[]; chunks=[]
 for n in pages:
  image=out/f"page-{n:03d}.png"
  doc[n-1].get_pixmap(matrix=fitz.Matrix(2.4,2.4),alpha=False).save(image)
  p=subprocess.run(["tesseract",str(image),"stdout","-l","eng+urd","--psm","6"],text=True,capture_output=True)
  txt=p.stdout.strip();(out/f"page-{n:03d}.txt").write_text(txt,encoding="utf-8")
  rows.append({"pdf_page":n,"ocr_chars":len(txt),"review_status":"NOT_VISUALLY_VERIFIED"})
  chunks.append(f"\\n\\n===== PDF PAGE {n} =====\\n{txt}")
  print(f"Class {grade} page {n}",flush=True)
 (out/f"CLASS{grade}_CANDIDATE_PAGES_OCR.txt").write_text("".join(chunks),encoding="utf-8")
 with (out/f"CLASS{grade}_PAGE_INDEX.csv").open("w",newline="",encoding="utf-8-sig") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (out/"README.md").write_text(f"Class {grade} visual review pack. OCR is not approval. Inspect source images, transcribe all options, solve independently, check duplicates and SLO mapping before publication.\\n",encoding="utf-8")
