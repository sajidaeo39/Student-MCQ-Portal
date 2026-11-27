# Class 8 — Staging Audit and Completion Gate (2026-11-27)

Repository: `sajidaeo39/Student-MCQ-Portal`
Base: `main` at `fdf7082abc1eb8725140f9a303cb88e4269e4e75`
Branch: `staging/class8-full-audit-2026-11-27`

## Executive decision

**HOLD — do not deploy Class 8 content to the live portal yet.**

This audit deliberately separates the current live bank, the V20 production tracker, the uploaded `PECTAA_Class8_MCQs.json` draft, and the full-year Science SLO register. These are not the same dataset and their counts do not reconcile. Publishing one as if it were the other would silently replace content or create incomplete SLO coverage.

## 1. Current live portal (main branch)

The current loader assembles the portal from 16 deployment parts and filters the legacy bank for Classes 3–8. In the existing live data source, Class 8 has 1,260 legacy MCQs:
- English: 360
- Urdu: 300
- Mathematics: 320
- Science: 280

The current Class 8 SLO catalogue in the live portal contains 52 entries:
- English: 14
- Urdu: 14
- Mathematics: 12
- Science: 12

These records are present in the current portal code; their presence does **not** prove full-year textbook extraction or academic validation. The portal UI says source-matched SLO records are shown, but the catalogue is not equivalent to the separate full-year register.

## 2. Uploaded Class 8 JSON draft

File: `PECTAA_Class8_MCQs.json` (640 records; 966,636 bytes).

| Subject label in file | MCQs | Distinct SLO IDs | Chapters |
|---|---:|---:|---:|
| English | 160 | 13 | 13 |
| Urdu | 160 | 11 | 11 |
| Mathematics | 160 | 14 | 12 |
| General Science | 160 | 12 | 12 |
| **Total** | **640** | **50** | **48** |

Each of the eight months (April, May, August/September, October, November, December, January, February) has 20 records per subject.

### Structural checks performed
- 640 records parsed successfully as JSON.
- 640 unique MCQ IDs; no duplicate IDs.
- All questions, four options, correct-answer fields, explanations, and SLO IDs are populated.
- All correct-answer keys are one of A/B/C/D.
- No exact duplicate (question + all four options) was found.
- Three repeated question stems were detected in Mathematics and require a human near-duplicate check.
- The file uses `General Science` whereas the portal's approved subject label is `Science`; an explicit controlled mapping is required before integration.
- The draft does not contain a reliable textbook page citation for every question; subject-level source-reference text alone is insufficient for full traceability.

### SLO-group size warning
The 640-record draft does not consistently meet the stated 20-MCQ-per-SLO target:
- English: 10 of 13 SLO groups are below 20.
- Urdu: 8 of 11 SLO groups are below 20; one group has 64 questions and eight subgroups have only 4 each.
- Mathematics: 10 of 14 SLO groups are below 20.
- General Science: 10 of 12 SLO groups are below 20.

The dataset is therefore a draft, not a completed bank.

## 3. V20 production tracker — Class 8

The repository/library V20 tracker records the following current production counts:

| Subject | Draft MCQs | Question-linked SLO groups | Groups with 20 |
|---|---:|---:|---:|
| English | 60 | 3 | 3 |
| Urdu | 40 | 2 | 2 |
| Mathematics | 2,140 | 107 | 107 |
| Science | 260 | 13 | 13 |
| **Total** | **2,500** | **125** | **125** |

The tracker itself says these counts meet quantity targets only for currently linked groups and that academic/source verification is pending. The 640-record JSON does not match this inventory (notably Mathematics 160 vs 2,140 and English 160 vs 60). Do not merge or replace banks until a canonical source-of-truth decision and reconciliation are completed.

## 4. Class 8 full-year Science SLO register

The `Class_6_8_Science_Full_Year_SLO_Register.csv` contains 96 Class 8 Science SLO rows:
- Target: 20 MCQs per SLO (1,920 total).
- Drafted: 260 MCQs across 13 currently linked SLO groups.
- Remaining: 1,660 MCQs across 83 known unlinked SLO groups.
- Independently approved: 0.
- Release status: HOLD.

The separate `Remaining_Known_SLO_Gaps.csv` contains the 83 Class 8 Science gaps. Many outcomes require practical or performance-based assessment in addition to MCQs; do not treat MCQs as a replacement for those activities.

## 5. English, Urdu, and Mathematics SLO coverage

The current V20 tracker has only 3 linked English groups and 2 linked Urdu groups and explicitly says full language SLO extraction is incomplete. Mathematics has 107 linked groups and 2,140 draft MCQs in the V20 tracker, but the available Class 8 JSON draft has only 14 SLO IDs and 160 records. A full-year, source-page-grounded Mathematics register and reconciliation are still required.

Do not invent official SLO codes. Any local IDs must be labelled as local identifiers, not official codes.

## 6. Required remaining work before release

1. Establish the authoritative Class 8 dataset and reconcile the 640-record JSON against the V20 inventory (especially Mathematics and English/Urdu).
2. Complete the source-page ledger for all four supplied Class 8 textbooks and the Class 8 Taleemi Calendar.
3. Extract and map the full-year English and Urdu SLOs; verify Mathematics SLOs against the actual textbook; reconcile the 96 Science register rows to the textbook and calendar.
4. Generate the missing 20-question sets only from verified SLOs, keeping practical SLOs separately flagged for performance assessment.
5. Run question-level subject review: correctness, ambiguity, one-best-answer validity, distractors, age appropriateness, language quality, source page, duplicate and near-duplicate checks.
6. Independently approve each SLO group. Current approved count is zero in the Science register; V20 also marks the overall bank as pending academic/source verification.
7. Integrate Class 8 into the existing portal architecture only after the release gates pass. Preserve Classes 1–7, existing UI, optional student/school fields, 9-question individual tests, 12-question Class 8 mixed test (3 per approved subject), randomization, scoring, review, and mobile layout.
8. Run automated tests and verify the deployed live URL and GitHub Pages workflow before calling the work complete.

## 7. Changes made in this audit step

- Created this isolated audit branch from the current `main`.
- Added this report only.
- No production data, portal loader, SLO menu, or live deployment was changed.
- The live site remains on the previous release until the Class 8 academic and source-verification gates are met.

## Release status

**Class 8: NOT READY FOR LIVE DEPLOYMENT.** Quantity in some draft inventories is not equivalent to verified, source-traceable, independently approved coverage.
