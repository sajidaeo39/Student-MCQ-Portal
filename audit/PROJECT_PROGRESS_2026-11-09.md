# Student MCQ Portal — Reconciled Project Progress
Updated: 2026-11-09

## Current snapshot
- Live question-bank source in `index.html`: **189 MCQs** across 21 approved class-subject sets.
- **63 PDF-source MCQs** belong to the documented visually reviewed and answer-checked first set (3 per approved class-subject set).
- **126 additional MCQs** are explicitly labelled `Generated • Concept Based`; they are not presented as PDF transcriptions.
- All 21 class-subject sets now contain **9 questions**, so all individual subject-practice cards can open.
- Classes 3–5: 3 approved subjects × 9 questions = 27 per class.
- Classes 6–8: 4 approved subjects × 9 questions = 36 per class, including Science.
- Class Mix remains 9 questions for Classes 3–5 and 12 questions for Classes 6–8.
- Fresh-question selection and local rotation history are implemented for subject, class-mix and group-mix selection. Because individual subject practice currently uses all 9 items in a 9-item pool, it cannot yet provide a completely new 9-question set on every repeat attempt; expand each pool beyond 9 for that guarantee.

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
6. Keep the 126 generated concept-based questions distinct from the 63 PDF-source verified MCQs; review generated answers and difficulty before formal endorsement.
7. Expand the pools beyond 9 items per subject if every repeated individual practice attempt must contain 9 entirely unseen questions.
8. Complete rotation testing in a real browser, including localStorage persistence and wrap-around after the unused pool is exhausted.
9. Complete end-to-end portal testing after deployment.

## Fixed subject scope
- Classes 3–5: English, Urdu, Mathematics only.
- Classes 6–8: English, Urdu, Mathematics, Science only.

## Interpretation note
The Stage 2 OCR report was an intermediate checkpoint and says no questions had yet been promoted at that stage. Later class-wise verification reports document a 63-question verified first set. The current live bank was subsequently expanded to 189 (63 PDF-source verified + 126 generated concept-based). This progress file reconciles those different dates/stages; it does not upgrade OCR-only candidates to verified questions.
