# Question Bank PDF — Stage 2 OCR Review Inventory

## Source and OCR status
- Source PDF: `Question bank.pdf` in the GitHub repository
- PDF pages processed: **247**
- OCR characters across pages: **125,728**
- Pages with empty OCR output: **0**
- OCR-detected question-heading occurrences: **649**
- Pages with a possible Question 1 start: **71**
- Heading-delimited OCR chunks retained for review: **410**

## Explicit class labels seen in OCR

| Class label | Page mentions |
|---|---:|
| Class 3 | 10 |
| Class 4 | 6 |
| Class 5 | 7 |
| Class 6 | 3 |
| Class 7 | 5 |
| Class 8 | 3 |

These are mentions on pages, not counts of students or complete papers. A label may appear only on one page of a multi-page paper. No class has been assigned to continuation pages automatically.

## Subject labels captured on question headings

| Subject | OCR heading labels |
|---|---:|
| English | 142 |
| Urdu | 159 |
| Mathematics | 130 |
| Science | 94 |

## Duplicate screening
- Exact normalized OCR duplicate groups flagged: **21**
- OCR chunks involved in those groups: **43**
- See `DUPLICATE_CANDIDATES_SUMMARY.md`.

These are candidates only. OCR can omit words, merge options, or misread Urdu/English characters. The same question may legitimately occur in separate student papers; duplicates should be excluded only after comparing the original PDF pages and confirming the complete question/options.

## Downloadable detailed files
The complete page and question inventories are included in the GitHub Actions artifact named `question-bank-ocr-audit` for run #1. The artifact includes:
- `all_pages_ocr.txt`: OCR text with page separators.
- `page_index.csv`: per-page metadata and possible class markers.
- `pages/`: per-page OCR text files.

Stage 2's detailed local analysis generated:
- `page_inventory.csv`: per-page OCR counts, visible class labels and question headings.
- `question_inventory_ocr_candidates.csv`: heading-delimited OCR chunks with original page numbers.
- `duplicate_candidates.csv`: exact-normalized duplicate candidates with source page numbers.

## Quality gate — not yet passed
1. Verify each student name and class heading visually; group all continuation pages belonging to that student's paper.
2. Confirm subject, question stem, all four options and selected/correct answer against the original PDF.
3. Independently verify answer keys; OCR circles/checkmarks are not treated as correct answers.
4. Review duplicate candidates visually and then run near-duplicate comparison on verified text.
5. Select exactly 3 questions per required subject/class and create the class-wise mixed tests only after the above checks.

**No questions have been promoted to the live portal. This stage is an OCR review inventory, not the final verified MCQ audit.**
