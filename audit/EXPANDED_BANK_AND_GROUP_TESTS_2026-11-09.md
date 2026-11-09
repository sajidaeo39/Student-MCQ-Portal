# Student MCQ Portal — Current Question Bank and Test Rules

Updated: 2026-11-09

## Current bank inventory

The current portal bank has **117 MCQs across 21 class-subject sets**.

| Class | Approved subjects | Questions per subject currently in bank | Total in class | Individual subject practice |
|---|---|---:|---:|---|
| Class 3 | English, Urdu, Mathematics | 9 each | 27 | Available |
| Class 4 | English, Urdu, Mathematics | 9 each | 27 | Available |
| Class 5 | English, Urdu, Mathematics | 9 each | 27 | Available |
| Class 6 | English, Urdu, Mathematics, Science | 3 each | 12 | Locked until each set reaches 9 |
| Class 7 | English, Urdu, Mathematics, Science | 3 each | 12 | Locked until each set reaches 9 |
| Class 8 | English, Urdu, Mathematics, Science | 3 each | 12 | Locked until each set reaches 9 |
| **Total** | **21 class-subject sets** | — | **117** | **9 sets ready; 12 pending** |

Classes 3–5 contain 81 questions (9 sets × 9). Classes 6–8 contain 36 questions (12 sets × 3). The bank must not be described as fully complete: 12 middle-class subject sets still need six additional verified questions each to support 9-question individual subject practice.

The 6-question expansions in Classes 3–5 are present in the code, but their full page-by-page provenance against the 247-page scanned PDF and their official SLO mapping have not yet been completed. Do not describe those additions as verbatim PDF transcriptions or officially SLO-verified until that audit is finished.

## Approved subjects

- Classes 3, 4, 5: English, Urdu, Mathematics only.
- Classes 6, 7, 8: English, Urdu, Mathematics, Science only.
- No other subjects or classes are permitted.

## Test formats

| Test mode | Question rule | Total |
|---|---|---:|
| Individual subject practice, Classes 3–5 | 9 questions from the selected class and subject | 9 |
| Individual subject practice, Classes 6–8 | Opens only after 9 questions are available in the selected class-subject set | 9 |
| Class-specific Mix, Classes 3–5 | 3 English + 3 Urdu + 3 Mathematics | 9 |
| Class-specific Mix, Classes 6–8 | 3 English + 3 Urdu + 3 Mathematics + 3 Science | 12 |
| Group Mix, Classes 3–5 | One question from every class-subject set (3 classes × 3 subjects) | 9 |
| Group Mix, Classes 6–8 | One question from every class-subject set (3 classes × 4 subjects) | 12 |

**Overall Mix Classes 3–8 has been removed completely.** It must not be reintroduced unless the owner explicitly requests it.

Mixed tests intentionally use 3 questions per subject. Individual subject tests use 9 questions and remain unavailable for a set with fewer than 9.

## Source PDF review status

- Source: `Question bank.pdf`, 247 scanned pages, A4.
- The uploaded PDF is image/scanned content; automated text extraction returned no readable text.
- Visual sampling of pages confirmed test headings for Classes 3, 4, 5, and 8. The sampled Class 8 form is a 12-question test; sampled Classes 3–5 forms are 9-question tests.
- The full student-to-page ledger, complete OCR/visual transcription, and exhaustive class/subject inventory have **not** been completed. Do not infer that Classes 6 or 7 are absent from the entire PDF based only on the sampled pages.
- The sampled page images show unselected answer circles. Whether any other pages contain answer markings has not yet been checked comprehensively. Do not claim that the PDF supplies a verified answer key.
- Every answer must be independently solved and checked. OCR is a draft only; visually verify Urdu, mathematical notation, options, names, class headings, and subject labels.
- No official PECTAA SLO codes have yet been confirmed in this report. SLO mapping remains pending.

## Current functional rules

- Individual subject practice requires exactly 9 questions.
- Class-specific mixed practice requires 3 questions from each approved subject.
- Group Mix buttons are limited to Classes 3–5 and Classes 6–8.
- Timer remains 5 minutes; automatic submission on timeout remains enabled.
- Student Name and School Name remain optional.
- Preserve score, answer review, attempt summary, and other working portal features.

## Verification status

Completed in code:
- Removed the Overall Mix button and its execution branch.
- Changed individual subject practice gating and selection to 9 questions.
- Kept class-specific mixed tests at 3 questions per approved subject.
- Kept the two group mixes (9 and 12 questions).
- Kept approved subject scope unchanged.

Pending:
- Full 247-page PDF page ledger and transcription.
- Independent answer verification and duplicate/near-duplicate audit.
- Official SLO mapping and grouping.
- Add six additional verified questions to each of the 12 Classes 6–8 subject sets.
- Verify GitHub Pages deployment and test the live portal after the current deployment run completes.

Do not claim full source audit or full portal completion until the pending items are resolved.
