# Class 8 Remaining Work — Staging Audit (27 November 2026)

## Scope and safety
- Work is isolated on branch `class8-completion-staging-20261127`.
- The live `main` branch and deployed portal have not been changed.
- Classes 3–7 are out of scope and must remain unchanged.
- Source basis: supplied Class 8 Taleemi Calendar, the four Class 8 SNC 2023–24 textbooks in the supplied Drive folder, Master_MCQ_DRAFT_V20.json, and Class_6_8_Science_Full_Year_SLO_Register.csv.
- All V20 items remain drafts unless independently reviewed. A row count is not academic approval.

## Verified current V20 bank
| Subject | Draft MCQs | SLO groups | Months represented |
|---|---:|---:|---|
| English | 60 | 3 | April |
| Urdu | 40 | 2 | April |
| Mathematics | 2,140 | 107 | April, May, August/September, October, November, January, February |
| Science | 260 | 13 | April, August/September |
| **Total** | **2,500** | **125 subject/SLO groups** | — |

Exact repeated question+option sets found within V20:
- English: 0 duplicate groups.
- Urdu: 0 duplicate groups.
- Mathematics: 5 duplicate groups (10 extra copies); keep these flagged for review rather than silently deleting them.
- Science: 0 duplicate groups.

## Structural validation of V20 Class 8 records
An automated structural pass over all 2,500 Class 8 records found:
- 0 blank question stems.
- 0 blank options among the four option fields.
- 0 invalid answer keys (all are A–D).
- 0 duplicate options within an individual question.
- 0 blank SLO IDs, source references, explanations, or review-status fields.
- All 125 subject/SLO groups contain exactly 20 rows.

This is schema/structure validation only. It does not prove the answer is factually correct, the distractors are academically sound, or the SLO is officially worded.

## Calendar coverage gaps
- English and Urdu currently contain April-only draft items. Their other calendar allocations have no V20 question groups.
- Mathematics has draft coverage in all seven teaching-month labels shown in the current calendar mapping. Its five repeated groups need review; 200 questions are explicitly marked as text proxies for visual/procedural outcomes, so these must not be treated as fully verified practical/diagram assessments.
- Science has 13 draft SLO groups, but only four intersect the Class 8 Science register. The register contains 87 distinct Class 8 SLOs; 83 have no corresponding MCQs in V20. The nine existing Chapter 1 Ecology/Energy groups are not present in the current Science register and require reconciliation to the source before approval.
- The Science register records 87/87 as independently unapproved and HOLD. Its 83 missing groups represent a numeric target of 1,660 MCQs at 20 per SLO, but quantity must not be padded with repetitive or unsupported questions.

## Source and academic QA limitations
1. The four original Class 8 books are available in the user's Google Drive folder: English 8 SNC 2023–24, Urdu 8 SNC 2023–24, Mathematics 8 SNC 2023–24, and General Science 8 SNC 2023–24.
2. Their PDFs are image/scanned pages (text extraction returns empty). Full page-by-page visual/OCR extraction and SLO-to-calendar reconciliation is still required before generating the missing language and Science bank.
3. The previous 48-page `Question bank.pdf` Class 8 screening is partial, not a complete transcription. Its verified additions and exclusions remain documented in `audit/CLASS8_PDF_REVIEW_PROGRESS.md`.
4. The deployed Class 8 bank's 25-Nov audit found 1,260 records but only 35 unique question-and-options groups (1,225 repeated copies), and blank SLO descriptions in all 1,260 rows. That old deployed bank is not equivalent to the 2,500-row V20 draft.
5. No source currently supports marking the V20 bank academically approved.

## Required next steps
1. OCR/visually inspect the Class 8 textbook pages by the calendar's unit/chapter and page allocations; retain page citations.
2. Create a source-grounded SLO register for all four subjects and reconcile provisional/local SLO IDs to the official textbook wording.
3. Generate distinct, answer-verified MCQs only for outcomes supported by the source; record correct answer rationale and source page for each.
4. Complete English and Urdu month-wise coverage; complete the 83 missing Science register groups; resolve the nine unmapped existing Science groups and five Mathematics duplicate groups.
5. Run item-level checks for one correct answer, distractor plausibility, answer-key accuracy, grade level, exact/near duplicates, option shuffling, and SLO/month mapping.
6. Enable individual subject practice only when at least nine independently verified unique questions exist. Mixed tests must use exactly three questions per approved subject (Class 8 total 12).
7. Update the portal loader and its SLO list consistently on this staging branch only. Preserve all other classes, student data, current UI, offline cache, and features. Test every class/subject, monthly selection, mixed test, answer review, scoring, and offline mode.
8. Do not merge or deploy until academic review and staging QA are complete.

## Current release decision
**HOLD — not ready for production.** This is a transparent staging audit, not a claim that the remaining MCQs or live portal integration are complete.
