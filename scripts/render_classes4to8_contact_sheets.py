from pathlib import Path
import fitz
from PIL import Image, ImageDraw

PDF = Path("Question bank.pdf")
OUT = Path("classes4to8-visual-review")
OUT.mkdir(exist_ok=True)
GROUPS = [
("C4-01",32,34),("C4-02",38,40),("C4-03",165,167),("C4-04",168,170),("C4-05",232,234),("C4-06",238,240),
("C5-01",29,31),("C5-02",77,79),("C5-03",80,82),("C5-04",138,140),("C5-05",144,146),("C5-06",147,149),("C5-07",244,246),
("C6-01",95,98),("C6-02",123,126),("C6-03",127,130),
("C7-01",57,60),("C7-02",65,68),("C7-03",115,118),("C7-04",119,122),("C7-05",181,184),("C7-06",185,188),
("C8-01",4,7),("C8-02",8,11),("C8-03",12,15),("C8-04",20,23),("C8-05",99,102),("C8-06",103,106),("C8-07-UNCONFIRMED",107,110),
]
doc=fitz.open(PDF)
index=["# Classes 4–8 Original PDF Contact Sheets","","Candidate groupings are OCR hypotheses. Inspect visible class/student header, page order, subject and question numbers. The C8-07 group is unconfirmed.",""]
for label,start,end in GROUPS:
    tiles=[]
    for n in range(start,end+1):
        if n>len(doc): continue
        pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(1.15,1.15),alpha=False)
        im=Image.frombytes("RGB",(pix.width,pix.height),pix.samples)
        im.thumbnail((420,560))
        tile=Image.new("RGB",(440,610),"white")
        tile.paste(im,((440-im.width)//2,32))
        ImageDraw.Draw(tile).text((10,8),f"{label} | PDF page {n}",fill="black")
        tiles.append(tile)
    if not tiles: continue
    sheet=Image.new("RGB",(440*len(tiles),610),"#ddd")
    for i,t in enumerate(tiles): sheet.paste(t,(440*i,0))
    name=f"{label}_pages_{start}-{end}.jpg"
    sheet.save(OUT/name,quality=88)
    index.append(f"- {name}")
(OUT/"README.md").write_text("\n".join(index)+"\n",encoding="utf-8")
print(f"Created {len(GROUPS)} sheets covering {sum(e-s+1 for _,s,e in GROUPS)} pages.")
