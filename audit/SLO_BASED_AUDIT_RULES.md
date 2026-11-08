# SLO-Based Question Classification and Subject Completeness Rules

## Purpose
Every source MCQ for Classes 3–8 must be classified against the learning outcomes for its own grade and subject. A question is not considered fully audited merely because its answer is correct.

## Official curriculum references checked
1. PECTAA Curriculum & Compliance: https://pectaa.edu.pk/curriculum-compliance/
   - Lists SNC 2020 subject frameworks for English I–V, Urdu I–V, Mathematics I–V, General Science IV–V, Social Studies IV–V, and General Knowledge I–III.
   - Its e-book list shows Grade 3 English, Urdu and Mathematics; Grades 4–5 also include General Science (English medium), and Urdu-medium Islamiat / Muasharti Uloom.
   - Grades 6–8 lists English, Urdu, Mathematics, General Science, Computer Science, Geography, History and other compulsory/optional subjects, with medium/grade variations.
2. PECTAA Large Scale Assessment Grade 3 Report 2024: https://www.pectaa.edu.pk/uploads/Large%20Scale%20Assessments/7.%20Large%20Scale%20Assessment%20Grade%203%20Report%2C%202024.pdf
   - Describes the Grade 3 assessed literacy, numeracy and general-knowledge SLOs.
3. PECTAA Large Scale Assessment Grade 5 Report 2024: https://www.pectaa.edu.pk/uploads/Large%20Scale%20Assessments/8.%20Large%20Scale%20Assessment%20Grade%205%20Report%2C%202024.pdf
   - Includes subject-wise weak-performance SLOs for English, Urdu, Mathematics and Science.
4. PECTAA Large Scale Assessment Grade 8 Report 2022: https://www.pectaa.edu.pk/uploads/Large%20Scale%20Assessments/4.%20Large%20Scale%20Assessment%20Grade%208%20Report%2C%202022.pdf
   - Reports assessment in English, Urdu, Mathematics and Science.
5. PECTAA Item Bank System: https://pectaa.edu.pk/item-bank-system/
   - Describes curriculum-aligned item development and pedagogical, linguistic, framework and psychometric review.

## Critical distinction: curriculum subjects vs subjects present in this PDF
The audit must maintain two separate inventories:
- **Curriculum subject inventory:** all subjects applicable to that grade/medium according to the official Punjab curriculum/scheme of studies.
- **Source PDF subject inventory:** all subjects actually represented in this 247-page question-bank PDF for that grade.

Do not assume that the PDF contains every curriculum subject. Do not silently drop any subject that appears in the PDF. If a curriculum subject is absent from the PDF, report it as `MISSING_FROM_SOURCE`; do not fabricate questions. If the PDF contains an optional subject, preserve it and mark its medium/optional status.

## Grade-wise curriculum subject watchlist
This is a coverage checklist, not a claim that every listed subject appears in the source PDF. Confirm the applicable medium and scheme of studies before finalizing the exact list.

| Grade | Subject watchlist from PECTAA curriculum / e-book listings |
|---|---|
| 3 | English, Urdu, Mathematics, General Knowledge (I–III); also note applicable religious education / Waqfiyat e Aama by medium |
| 4 | English, Urdu, Mathematics, General Science (EM); Social Studies / Muasharti Uloom and Islamiat (UM) where applicable |
| 5 | English, Urdu, Mathematics, General Science (EM); Social Studies / Muasharti Uloom and Islamiat (UM) where applicable |
| 6 | English, Urdu, Mathematics, General Science, Computer Science, Geography, History, Islamiat / Tarjuma-tul-Quran and other scheme/medium-specific subjects |
| 7 | English, Urdu, Mathematics, General Science, Computer Science, Geography, History, Islamiat / Tarjuma-tul-Quran and other scheme/medium-specific subjects |
| 8 | English, Urdu, Mathematics, General Science, Computer Science, Geography, History, Islamiat / Tarjuma-tul-Quran and other scheme/medium-specific subjects |

For this MCQ portal, include every subject for which source questions are actually supplied and approved. Do not create a fake question quota for subjects absent from the PDF. Where the project owner wants a curriculum-complete portal beyond this PDF, collect the relevant approved source material first.

## Mandatory SLO tagging fields
Every transcribed MCQ must carry:
- `grade`
- `subject`
- `student_name`
- `source_pdf_page`
- `question_text`
- `option_a`, `option_b`, `option_c`, `option_d`
- `source_marked_answer`
- `verified_correct_answer`
- `competency_or_strand`
- `slo_statement` (quote or faithful paraphrase from official grade/subject curriculum)
- `slo_reference` (official document title, page/section, URL)
- `cognitive_level` (Remembering / Understanding / Application / Higher Order Thinking, where supported by the framework)
- `slo_match_confidence` (High / Medium / Low)
- `review_status`

Never invent official SLO codes. If the official source provides no code, use a transparent internal tag such as `G5-MATH-FRACTIONS-01` and label it as an internal mapping ID, not an official code.

## SLO mapping procedure
1. Determine the student's grade and page group first.
2. Identify the subject from the actual page heading and question content.
3. Transcribe the question and all four options from the original image.
4. Solve and independently verify the answer.
5. Identify the skill/concept actually assessed (e.g. subject-verb agreement, punctuation, inference, vocabulary; number operations, fractions, geometry, measurement; Urdu grammar, vocabulary, comprehension; science concepts).
6. Match that skill to the closest grade-specific official SLO. Use the same grade and subject wherever possible.
7. Record the exact official SLO wording/reference and cognitive level. Do not assign an SLO only because a question contains a keyword.
8. If the question is outside the grade's official SLOs, mark `OUT_OF_GRADE_OR_UNMAPPED` and hold it for review.
9. If the question tests two outcomes, record one primary SLO and an optional secondary SLO.
10. Run a coverage report by grade × subject × SLO, showing counts and gaps.

## Subject completeness gate
Before a grade is marked complete:
- Compare the curriculum subject watchlist with the actual source PDF subjects.
- List every source-present subject and its question count.
- List every curriculum subject not found in the source as `MISSING_FROM_SOURCE`.
- List every source-present subject with zero approved questions as `NO_APPROVED_ITEMS`.
- Do not publish a mixed test if any subject required by the agreed portal specification is missing its required number of approved questions.
- If the PDF has only a partial sample for a subject, show the shortfall explicitly.
- The final dashboard must show a subject coverage matrix for every grade. No silent omission.

## Selection rule
Where a subject has more eligible questions than needed, select items across distinct SLOs/competencies and cognitive levels rather than choosing three questions testing the same narrow skill. Report SLO coverage and the reason for selection. Where only one or two SLO areas are represented in the PDF, disclose that limitation.

## Important limitation
The official PECTAA pages/reports cited above are framework references. Exact grade-specific SLO matching for every MCQ still requires inspecting the relevant grade/subject curriculum documents or textbooks and recording page/section references. The Grade 5 LSA report's weak-SLO list is useful assessment evidence but is not a complete replacement for the Grade 5 curriculum.
