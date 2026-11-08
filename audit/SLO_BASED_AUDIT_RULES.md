# SLO-Based Question Classification and Complete Subject Coverage

## Owner's instruction
Every grade must have all subjects represented in the source question bank. No subject that appears in the PDF may be omitted from extraction, SLO classification, subject practice or reporting. Additionally compare the PDF with the official curriculum so absent subjects are visible as gaps.

## Official reference
PECTAA Curriculum & Compliance / e-book list:
https://pectaa.edu.pk/curriculum-compliance/
The official listing distinguishes English Medium (EM), Urdu Medium (UM), compulsory subjects, and optional subjects. The grade/medium scheme must be checked before treating every curriculum title as applicable to a particular student.

English SNC I–V required standards and SLOs:
https://pectaa.edu.pk/uploads/SNC-2022/SNC_-_English_-_Required_Standards_and_SLOs%281-8%29.pdf

PECTAA's curriculum page lists SNC 2020 primary frameworks for English I–V, General Knowledge I–III, General Science IV–V, Mathematics I–V, Urdu I–V and Social Studies IV–V. It also lists grade-specific e-books for classes III–VIII.

## Grade-wise curriculum subject checklist
Use the applicable medium, religion/religious-education track and official scheme. This checklist is a coverage prompt, not a claim that every item is present in the supplied PDF.

| Grade | Core subjects / curriculum titles listed by PECTAA |
|---|---|
| 3 | English, Urdu, Mathematics; Nazra Quran for Muslim students; Waqfiyat-e-Aama and Islamiat (UM); Akhlaqiat for religious minorities |
| 4 | English, Urdu, Mathematics (EM), General Science (EM); Islamiat and Muasharti Uloom (UM); Nazra Quran; Akhlaqiat / religious education alternatives |
| 5 | English, Urdu, Mathematics (EM), General Science (EM); Islamiat and Muasharti Uloom (UM); Nazra Quran; Akhlaqiat / religious education alternatives |
| 6 | English, Urdu, Mathematics, General Science, Computer Science, Geography, History; Tarjuma-tul-Quran and Islamiat for Muslim students; Ethics/Akhlaqiat alternatives; Arabic and other scheme-specific options |
| 7 | English, Urdu, Mathematics, General Science, Computer Science, Geography, History; Tarjuma-tul-Quran and Islamiat for Muslim students; Ethics/Akhlaqiat alternatives; Arabic and other scheme-specific options |
| 8 | English, Urdu, Mathematics, General Science, Computer Science, Geography, History; Tarjuma-tul-Quran and Islamiat for Muslim students; Ethics/Akhlaqiat alternatives; Arabic and other scheme-specific options |

## Two inventories must never be confused
1. **Curriculum inventory:** all applicable subjects based on grade, medium and official scheme.
2. **PDF inventory:** every subject actually appearing in the supplied Question bank.pdf for that grade.

Extract all PDF-present subjects. For curriculum subjects not represented in the PDF, mark `MISSING_FROM_SOURCE`. Never fabricate questions. If owner later supplies approved material for missing subjects, add it with its source and SLO references.

## SLO fields required for each question
- grade, subject, student_name, source_pdf_page
- exact question text and all four options
- source_marked_answer and independently verified_correct_answer
- competency/strand, benchmark, SLO statement
- official SLO reference URL and page/section
- cognitive_level (Remembering, Understanding, Application, HOTS, only where supported)
- SLO match confidence and reviewer notes
- duplicate group/type and review status

Never invent official SLO codes. If there is no official code, use a clearly labelled internal mapping ID.

## Mapping workflow
1. Confirm student grade, medium and page grouping.
2. Determine actual subject from page heading/content.
3. Transcribe stem and A–D options from original image.
4. Solve independently; compare source-marked answer with correct answer.
5. Identify exact skill being assessed.
6. Map to the closest grade-specific official SLO, benchmark and competency.
7. Record exact source/page/section. If no defensible match, mark `UNMAPPED` or `OUT_OF_GRADE`.
8. Select final questions across different SLOs and cognitive levels where available.
9. Count questions by grade × subject × SLO and identify gaps.

## Completion and portal rules
- Every subject appearing in the PDF must be extracted, audited and listed in the portal subject inventory for that class.
- No subject is to be omitted just because an earlier draft assumed 3 or 4 subjects.
- Subject-wise test selection must use approved questions only.
- Mixed tests must include every source-present, approved subject for the grade; calculate total marks from actual selected question count, one mark per question.
- If a subject is missing from the source or has too few approved items, display the exact shortfall and do not falsely label the grade complete.
- Do not silently cap a grade to 9 or 12 marks if additional source-present subjects have been confirmed. First reconcile the agreed test design with the owner; preserve every subject.
- Maintain a grade × subject × SLO coverage matrix.

## Current evidence boundary
OCR page grouping currently suggests the source PDF has English, Urdu and Mathematics for Grades 4–5 and English, Urdu, Mathematics and Science for Grades 6–8. This is preliminary OCR evidence only; verify every candidate page visually. Do not assume no additional subject exists merely because the first grouping pass did not detect it.
