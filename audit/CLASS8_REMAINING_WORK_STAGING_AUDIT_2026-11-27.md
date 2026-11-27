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

## Completed next step: Class 8 English textbook inventory
A provisional 12-unit English inventory has now been added at `audit/CLASS8_ENGLISH_TEXTBOOK_SLO_INVENTORY_STAGING.csv`. It maps the textbook's contents-list entries to the calendar months and records each unit's theme, oral communication, reading, vocabulary/grammar, and writing skills.

Calendar mapping recorded from the supplied Class 8 Taleemi Calendar:
- April: Units 1–2
- May: Units 3–4
- August/September: Units 5–6
- October: Unit 7
- November: Units 8–9
- January: Units 10–11
- February: Unit 12

Source basis: English 8 SNC 2023–24, printed contents-list pages ii–iii (PDF pages 3–4), visually inspected; Class 8 Taleemi Calendar, page 1, visually inspected. The inventory preserves the contents-list terminology. These are provisional unit-level mappings, not official granular SLO codes. Lesson-page review and independent academic validation are still required before generating or approving MCQs. The current 60 English draft MCQs remain April-only in V20; this inventory does not claim that the other months' question banks have been created.

## Completed next step: Class 8 Urdu textbook lesson inventory
A provisional 20-lesson Urdu inventory has been added at `audit/CLASS8_URDU_TEXTBOOK_SLO_INVENTORY_STAGING.csv`. It records the lesson number, title, genre, printed textbook starting page, and month/lesson range from the supplied calendar.

Calendar mapping transcribed from the Urdu row on the supplied Class 8 Taleemi Calendar:
- April: Lessons 1–2
- May: Lessons 3–6
- August/September: Lessons 7–10
- October: Lessons 11–12
- November: Lessons 13–14
- January: Lessons 15–17
- February: Lessons 18–20

Source basis: Urdu 8 SNC 2023–24 contents/index, visually inspected (PDF page 4); Taleemi Calendar 8, Urdu subject row, visually inspected (PDF page 1). The contents page supplies lesson titles and starting pages, not granular official SLOs. Two lesson-title readings (Lessons 3 and 5) are flagged for confirmation from clearer lesson-page scans. No new Urdu MCQs have been generated or marked approved from this inventory. The current V20 Urdu draft remains 40 MCQs and April-only; all other month coverage remains outstanding pending lesson-page extraction and question writing.

## Completed next step: English and Urdu MCQ draft banks compiled
A standalone downloadable package was assembled from the previous `PECTAA_Class8_MCQs.json` draft bank plus the existing Class 8 records in `Master_MCQ_DRAFT_V20.json`:
- English: 160 prior PECTAA items + 60 V20 items = 220.
- Urdu: 160 prior PECTAA items + 40 V20 items = 200.
- Combined: 420 English/Urdu items.

Structural QA passed on the compiled package:
- No duplicate MCQ IDs within either subject bank.
- No exact duplicate normalized question stems within either subject bank.
- Every item has four non-empty distinct options, a valid A–D answer key and a non-empty explanation.
- Where an explicit `correct_answer_text` exists, it matches one of the four options.
- The 160-item PECTAA English and Urdu sets each have 20 items in each month bucket (April, May, August/September, October, November, December revision, January, February). The V20 items add 60 English and 40 Urdu questions to April.
- December is classified as mid-term revision because the supplied Class 8 calendar marks December as Mid Term Exam.

Deliverable files were generated separately:
- `Class8_English_MCQ_Bank_Complete_DRAFT.json`
- `Class8_Urdu_MCQ_Bank_Complete_DRAFT.json`
- `Class8_English_Urdu_MCQ_Bank_Combined_DRAFT.json`
- `Class8_English_Urdu_MCQ_Monthly_QA_Summary.csv`
- `Class8_English_Urdu_MCQ_Completion_Report.md`

Academic release remains HOLD: the previous PECTAA items do not consistently include exact textbook page references; structural validation does not establish answer correctness, distractor quality or full lesson/SLO alignment. These compiled banks are draft deliverables and have not been imported into the live portal or merged into the Master V20 file. Classes 3–7 and student records remain unchanged.

## Completed draft expansion: English and Urdu MCQ banks
Standalone JSON packages were generated from the previous PECTAA Class 8 draft bank plus the existing V20 Class 8 language records:
- English: 160 PECTAA + 60 V20 = 220 draft MCQs.
- Urdu: 160 PECTAA + 40 V20 = 200 draft MCQs.
- Combined: 420 draft MCQs.

Structural QA on the merged packages: all IDs unique; normalized question stems unique within each subject; all four options present and distinct; A–D answer keys valid; explanations present; provided correct_answer_text matches one of the options. No structural errors were detected.

Monthly counts in the generated draft packages:
| Subject | April | May | Aug/Sep | October | November | December revision | January | February | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| English | 80 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 220 |
| Urdu | 60 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 200 |

December is explicitly treated as mid-term revision, because the supplied calendar marks December as Mid Term Exam, not a fresh unit allocation.

**Release limitation:** These are merged draft packages, not academically approved question banks. The PECTAA items do not consistently include exact textbook page references, and lesson/unit-level alignment, factual correctness, distractor quality, and answer-key correctness still need independent subject-expert review. All items remain DRAFT / HOLD. The live portal has not been modified. Generated JSON files are delivered as conversation attachments; this GitHub branch records the audit and counts only.
 
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
