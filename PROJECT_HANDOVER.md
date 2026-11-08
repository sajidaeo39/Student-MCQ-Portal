# Student MCQ Portal — Project Handover

Repository: https://github.com/sajidaeo39/Student-MCQ-Portal
Live site: https://sajidaeo39.github.io/Student-MCQ-Portal/

## Goal
Continue the existing Student MCQ Portal. Preserve its current working design and features unless a change is required for the requested question-bank update. The owner has granted GitHub access to the connected ChatGPT GitHub integration; inspect the repository before editing.

## Required question-bank structure
- Classes 3, 4, 5: English, Urdu, Mathematics; exactly 3 questions per subject; 9 questions per class.
- Classes 6, 7, 8: English, Urdu, Mathematics, Science; exactly 3 questions per subject; 12 questions per class.
- Each class must have its own correct subject list and class-specific practice tests.
- A mixed test for each class must contain all required subjects and exactly 9 or 12 questions as specified above.

## Source PDF and verification rules
The owner previously attached a 247-page file named **Question bank.pdf** in a different ChatGPT conversation. The pages contain student names, class information, and each student's questions on following pages. The correct class must be determined from the student's name/class heading and the pages belonging to that student—not by guessing from a question's difficulty or an isolated page heading.

Important file-access limitation: an attachment in another ChatGPT conversation/account is not automatically available in this repository or a new ChatGPT account. First inspect the repository for the source PDF and any extracted question-bank data. If the PDF is not present, do not claim to have reviewed it and do not invent questions or answers. Ask the owner for a way to make the source file accessible. Do not ask them to re-upload it if a valid copy is already present in the repository or another accessible source.

## Required audit before updating live data
1. Inspect all existing source files, data structures, test logic, and deployment workflow. Identify the current question-bank source of truth.
2. Read the complete source PDF if accessible. Track the student name, stated class, page range, subject, question text, all options, and marked answer.
3. Map each question to the correct class and subject using the student's class and attached page sequence.
4. Verify every correct answer independently. The marked answer in the PDF may be wrong. Store the academically correct answer for practice, and keep an audit note when the source's marked answer differs.
5. Identify exact duplicates and near-duplicates across the whole PDF. Report counts separately. Do not silently discard a question that differs meaningfully; retain class/subject attribution. Avoid duplicate entries in the final practice bank where they are genuinely the same question.
6. Where the source is unclear, incomplete, or has no defensible correct answer, flag it for review rather than guessing.
7. Produce an audit report: total source questions, unique questions, exact duplicates, near-duplicates, class-wise counts, subject-wise counts, corrected answers, and unresolved items.
8. Confirm the final data has exactly 3 questions per required subject for each class. If there are more eligible verified questions, select a transparent set of 3 per subject (prefer distinct concepts and avoid repeats). Do not fabricate missing questions to fill a quota; report any shortfall.

## Portal requirements
- Keep the existing portal's functionality, responsive/mobile layout, branding, and current working features.
- Keep optional Student Name and School Name fields; do not make student data collection compulsory.
- Keep individual subject practice and add/retain one mixed test per class.
- Mixed test totals: Classes 3–5 = 9 marks; Classes 6–8 = 12 marks (1 mark per question).
- Provide automatic checking, score, correct/incorrect review, and appropriate answer feedback.
- Keep the existing attempt summary/features if present; do not remove working features.
- Ensure class and subject menus match the required structure exactly.
- Make the portal usable on mobile phones and shareable with teachers/students.

## Technical/deployment rules
- Inspect current code before modifying it. Do not replace the entire portal with a new unrelated template.
- Keep question data separate from UI logic if the current architecture supports it.
- Validate JSON/JavaScript syntax and test every class/subject selection, individual test, mixed test, scoring, answer review, and mobile layout.
- Check GitHub Actions / GitHub Pages deployment status after committing.
- Verify the live URL after deployment. Do not say the site is updated until the live site is actually checked.
- Commit focused changes with a clear commit message. Avoid exposing secrets or tokens.

## Required final handover to owner
Provide:
- repository files changed and commit link;
- live website link and deployment verification status;
- class/subject question counts;
- duplicate-question findings;
- answer corrections and unresolved questions;
- tests performed and any remaining limitations.

## First action for the next assistant
Inspect the repository and determine whether **Question bank.pdf** or an already extracted question-bank dataset is present. If accessible, proceed with the full audit. If not accessible, explain the exact missing source and stop short of claiming that question verification or portal data updates have been completed.


## Detailed PDF investigation procedure (mandatory)
Treat the 247-page PDF as a scanned visual source if text extraction returns empty or incomplete. Do not assume an empty text layer means the PDF has no questions.

### A. Preserve and inspect the source
1. Confirm the exact source file is accessible and record its filename, page count, and page dimensions.
2. Keep an unchanged copy. Never overwrite or alter the original PDF.
3. Check representative pages visually, including the first and last pages and pages around apparent student transitions.
4. If text extraction is empty/incomplete, render every page to images and run OCR. Use English and Urdu OCR where available. OCR is only a draft transcription: visually verify every question, option, student name, class label, and answer mark against the page image.
5. Maintain a page-by-page index. Do not rely on OCR alone for Urdu text, mathematical notation, symbols, fractions, exponents, diagrams, or option markers.

### B. Build student-to-page groups before extracting questions
Create a page ledger with these fields:
- PDF page number;
- student name as printed;
- class as printed;
- start/end page of that student's question set;
- subject shown for each question;
- confidence/status and notes.

Use the student's name/class heading and the sequence of subsequent pages to associate questions with that student. A new student heading starts a new group. If a page has no visible heading, attach it only when the preceding/following page sequence clearly supports that association. Otherwise mark it unresolved; do not infer the class from question difficulty.

### C. Extract each MCQ faithfully
For every question, capture:
- source page number(s), student name, and class;
- subject;
- exact question wording (preserve Urdu script and English wording);
- options A, B, C, D exactly as printed;
- answer marked in the PDF, if any;
- diagrams/images needed to understand the question;
- transcription confidence and any ambiguity.

Do not silently rewrite a question in a way that changes its meaning. Correct obvious OCR spelling only after checking the page image. Keep a link/reference to its source page in the audit dataset.

### D. Independently verify the correct answer
1. Solve each question independently; do not copy the marked answer as the answer key.
2. For English, check the relevant grammar, vocabulary, reading, or language rule.
3. For Urdu, check the relevant grammar, vocabulary, idiom, spelling, or comprehension context.
4. For Mathematics, recompute the result step by step and check that exactly one option matches (unless the question explicitly permits multiple answers).
5. For Science, verify the underlying concept and check units, terminology, and option wording.
6. For any factual/current/ambiguous item, use reliable references where needed and record the reference or reasoning in the audit notes.
7. Compare the independently verified answer with the PDF's marked answer. Label each as: MATCH, SOURCE MARKING WRONG, NO MARKING, AMBIGUOUS, or DEFECTIVE QUESTION.
8. If no option is correct, more than one option is correct, or the question is incomplete, do not force an answer. Mark it DEFECTIVE/AMBIGUOUS and explain why. Do not insert a guessed answer into practice mode.
9. Store both source_marked_answer and verified_correct_answer in the audit data. Practice mode must use verified_correct_answer only for approved questions.

### E. Detect duplicates across the entire PDF
1. Compare normalized question text across all pages, ignoring harmless differences such as case, extra spaces, punctuation, and option-label formatting.
2. Compare Urdu text carefully without stripping meaningful characters/diacritics that could change meaning.
3. Compare options as well as question wording. The same stem with materially different options may need manual review.
4. Report separately:
   - exact duplicates (same question and materially same options);
   - near-duplicates (same concept/stem with small wording or option changes);
   - repeated question appearing under different students/classes/subjects.
5. Do not automatically merge near-duplicates. A human/manual review decision is required. Preserve all source page references even when one canonical question is selected.

### F. Produce an auditable master dataset and report
Create a structured master dataset (JSON or CSV, depending on the portal architecture) with stable question IDs and at least:
question_id, class, subject, student_name, source_page_start, source_page_end, question, option_a, option_b, option_c, option_d, source_marked_answer, verified_correct_answer, answer_status, duplicate_group_id, duplicate_type, verification_note, review_status.

Also create a readable audit report containing:
- PDF pages reviewed and any unreadable pages;
- student groups and class mapping;
- extracted question totals by class and subject;
- exact and near-duplicate totals, with question IDs and source pages;
- source answer markings that were wrong;
- defective, ambiguous, or unanswered questions;
- final selected practice questions and why selected.

### G. Quality gates before portal update
- Every selected question must have a verified answer and all four options.
- Every selected question must have a confirmed class and subject.
- No unresolved OCR/transcription or answer ambiguity may enter the live practice bank.
- Required final distribution: Classes 3–5 have 3 approved questions in each of English, Urdu, Mathematics; Classes 6–8 have 3 approved questions in each of English, Urdu, Mathematics, Science.
- If any class/subject has fewer than 3 approved unique questions, report the shortfall and request a decision; never fabricate questions.
- Keep the complete audit dataset separate from the smaller selected practice dataset.


## Owner clarification — fixed practice-test scope (2026-11-08)
This is an explicit owner-approved constraint and overrides any broader curriculum/subject inventory elsewhere in old notes:
- Classes 3–5: English, Urdu, Mathematics only.
- Classes 6–8: English, Urdu, Mathematics, Science only.
- Do not audit, map SLOs for, create MCQs for, or add tests/menus for any other subject.
- The supplied real-test PDF is only a sample/reference for practice-test style and expected content. It is not a request to reproduce a full curriculum or create a real examination.
- SLO mapping must be done only for questions in the approved subjects above, using the relevant class/subject learning outcomes. If an exact SLO cannot be substantiated, mark it provisional/unverified rather than inventing a code.
- Keep exactly 3 verified questions per approved subject. Mixed test: 9 marks for Classes 3–5; 12 marks for Classes 6–8. Do not fabricate questions to fill gaps.
- The grade-subject matrix must contain exactly 21 rows (3 subjects × 3 classes plus 4 subjects × 3 classes).
