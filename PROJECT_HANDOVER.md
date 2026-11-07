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
