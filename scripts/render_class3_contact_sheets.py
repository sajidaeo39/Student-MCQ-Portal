#!/usr/bin/env python3
"""Render provisional Class 3 PDF pages into legible review images/contact sheets."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

PDF = Path("Question bank.pdf")
OUT = Path("class3-visual-review")
PAGES = OUT / "pages"
SHEETS = OUT / "contact-sheets"
PAGES.mkdir(parents=True, exist_ok=True)
SHEETS.mkdir(parents=True, exist_ok=True)

if not PDF.is_file():
    raise SystemExit("Question bank.pdf not found")
doc = fitz.open(PDF)
ranges = [(44, 52), (68, 76), (171, 180), (199, 208)]
page_numbers = sorted({p for start, end in ranges for p in range(start, end + 1)})
thumbs = []

for page_no in page_numbers:
    if page_no < 1 or page_no > len(doc):
        raise SystemExit(f"Requested page {page_no} is outside PDF")
    page = doc[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
    img_path = PAGES / f"pdf-page-{page_no:03d}.jpg"
    pix.save(str(img_path), jpg_quality=88)
    im = Image.open(img_path).convert("RGB")
    im.thumbnail((460, 650))
    thumbs.append((page_no, im.copy()))

font = ImageFont.load_default()
for idx in range(0, len(thumbs), 4):
    group = thumbs[idx:idx + 4]
    cell_w, cell_h = 480, 690
    sheet = Image.new("RGB", (cell_w * 2, cell_h * 2), "white")
    draw = ImageDraw.Draw(sheet)
    for offset, (page_no, im) in enumerate(group):
        x = (offset % 2) * cell_w
        y = (offset // 2) * cell_h
        draw.text((x + 8, y + 6), f"ORIGINAL PDF PAGE {page_no}", fill="black", font=font)
        im.thumbnail((460, 650))
        sheet.paste(im, (x + 8, y + 28))
    first, last = group[0][0], group[-1][0]
    sheet.save(SHEETS / f"contact-{first:03d}-{last:03d}.jpg", quality=90)

(OUT / "README.txt").write_text(
    "Class 3 provisional page review images. Page labels refer to original PDF page numbers. "
    "These ranges were selected from OCR-based grouping and have not been visually verified. "
    "Check student names, true page order, class headings, subject sections, question stems, options, "
    "diagrams and marked answers before approving any MCQ.\n",
    encoding="utf-8"
)
print(f"Rendered {len(page_numbers)} original PDF pages into {len(list(SHEETS.glob('*.jpg')))} contact sheets.")

# Re-run marker: render original source pages for manual Class 3 verification.
