# Student MCQ Portal — Reconciled Project Progress
Updated: 2026-11-09

## Current snapshot
- Live question-bank source in `index.html`: **117 MCQs**.
- Independently verified first set documented by the later class-wise verification reports: **63 MCQs**.
- Additional current-bank entries awaiting source/answer confirmation: **54 MCQs** (117 minus 63).
- Current verified share of the 117 live entries: **53.85%**.
- This ratio is a project-tracking measure, not a claim that 54% of the 247-page source PDF has been fully audited.

## OCR work already completed
The Stage 2 OCR report records:
- Source PDF: `Question bank.pdf`, 247 pages.
- OCR processed pages: 247; empty OCR pages: 0.
- OCR characters: 125,728.
- Question-heading occurrences: 649.
- Heading-delimited OCR chunks retained for review: 410.
- Possible Question 1 starts: 71 pages.
- OCR page mentions: Class 3 (10), Class 4 (6), Class 5 (7), Class 6 (3), Class 7 (5), Class 8 (3).
- Subject-heading counts: English 142, Urdu 159, Mathematics 130, Science 94.
- 21 exact-normalized OCR duplicate candidate groups involving 43 chunks.

These are OCR detection counts, not final unique-question counts. OCR chunks may be incomplete, repeated, incorrectly grouped, or contain misread text/options.

## Later verified set
The later verification reports document a 63-question first set across 21 class-subject sets:
- Classes 3–5: English, Urdu, Mathematics.
- Classes 6–8: English, Urdu, Mathematics, Science.
- Three questions per approved class-subject set.
- Selected questions were visually checked against source pages and answers independently checked, according to `CLASSES6_8_VERIFICATION_REPORT.md`, `CLASS3_VERIFIED_MIXED_TEST_READINESS.md`, and class-wise reports.

## Work still outstanding
1. Reconcile all 410 OCR review chunks against the original page images and saved page-grouping reports.
2. Transcribe and validate all stems and four options; independently check every answer.
3. Review the 21 duplicate candidate groups and near-duplicates; do not deduplicate on OCR text alone.
4. Resolve page-order anomalies and quarantined/unclear student groups in Classes 3–8.
5. Confirm official PECTAA SLO codes. Existing skill tags are provisional, not certified official codes.
6. Review the 54 current portal entries that are not included in the documented 63-question verified set.
7. Expand the bank with additional source-verified questions and clearly label generated concept-based variants separately.
8. Add question rotation so repeated attempts draw fresh questions where the available pool permits; never repeat a question within a single test.
9. Complete end-to-end portal testing after deployment.

## Fixed subject scope
- Classes 3–5: English, Urdu, Mathematics only.
- Classes 6–8: English, Urdu, Mathematics, Science only.

## Interpretation note
The Stage 2 OCR report was an intermediate checkpoint and says no questions had yet been promoted at that stage. Later class-wise verification reports document a 63-question verified first set. The current live bank was subsequently expanded to 117. This progress file reconciles those different dates/stages; it does not upgrade OCR-only candidates to verified questions.
