# Student MCQ Portal — Final Quality Audit

Audit date: 2026-11-09
Repository: https://github.com/sajidaeo39/Student-MCQ-Portal
Live portal: https://sajidaeo39.github.io/Student-MCQ-Portal/

## Scope and counts
- Source reference PDF `Question bank.pdf` is present in the repository (247 pages; original file retained).
- Classes 3–5: English, Urdu, Mathematics only; 3 questions per subject.
- Classes 6–8: English, Urdu, Mathematics, Science only; 3 questions per subject.
- Current bank: 63 MCQs across 21 class-subject sets.
- Class 3–5 mixed tests: 9 questions / 9 marks.
- Class 6–8 mixed tests: 12 questions / 12 marks.
- Each subject-wise test selects 3 questions.

## Final corrections in this pass
- Class 5 Urdu question 3 changed from a dangling reference to a missing verse into a standalone question about cultivation. Correct option remains C (کھیتی کا).
- Class 6 Urdu question 1 changed from a dangling reference to an absent newspaper report into a standalone storm-supply question. Correct option remains B (بجلی).
- Class 8 Urdu question 3 changed from a dangling reference to an absent passage into a standalone idiom question. Correct option remains A (آسمان سر پر اٹھانا).
- Portal statistic label changed from “Questions Attempted” to “Answered Questions” because only answered questions increment that counter.
- “School Entries” and “Student Entries” are entry counters, not unique school/student counts. The portal does not currently deduplicate names.

## Functional logic reviewed
- Subject menus are restricted to the approved subjects for each class.
- Mixed-test builder checks every required subject and requires at least three questions in each.
- Subject-wise test start checks for three questions.
- Options are shuffled while preserving the correct answer.
- Submission calculates correct, incorrect, unanswered, and percentage; answer review is available.
- Optional school/student name fields remain optional.

## Limitations — not to be represented as fully verified
- Skill tags are provisional; official grade-specific PECTAA SLO codes have not been independently confirmed. They must not be presented as official SLO codes.
- This pass corrected three context-dependent Urdu stems, but does not claim a complete page-by-page visual re-audit of all 247 scanned PDF pages.
- Exact and near-duplicate counts across the entire PDF have not been independently recomputed in this final pass.
- Automated static/runtime and real-device browser click testing was not completed here. A successful Pages workflow confirms deployment build, not every interactive path.
- School Entries / Student Entries are not unique entities. A reliable unique-school/student total requires a deduplicating data store and normalized identifiers.

## Acceptance summary
The configured class/subject structure and question counts meet the requested 63-question layout. The portal is suitable for a supervised review run, but should not be described as a fully certified question bank until official SLO mapping, full-PDF duplicate analysis, and end-to-end browser testing are completed.
