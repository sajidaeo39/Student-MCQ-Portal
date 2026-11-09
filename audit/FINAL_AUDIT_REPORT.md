# Final Structural Audit — Student MCQ Portal

Audit date: 10 November 2026
Repository: https://github.com/sajidaeo39/Student-MCQ-Portal
Source of inventory: current `index.html` questionBank (commit checked before this report).

## Executive result
- Total records in portal bank: **380**
- Invalid record structures (question/options/correct-index): **0**
- Unapproved subject placements: **0**
- Exact normalized duplicate stems within the same class and subject: **0**
- Records tagged as PDF-sourced: **254**
- Records tagged as generated/concept-based: **126**

## Class-wise inventory
| Class | English | Urdu | Mathematics | Science | Total |
|---|---:|---:|---:|---:|---:|
| 3 | 25 | 18 | 22 | 0 | 65 |
| 4 | 23 | 15 | 23 | 0 | 61 |
| 5 | 18 | 13 | 24 | 0 | 55 |
| 6 | 16 | 16 | 22 | 20 | 74 |
| 7 | 16 | 9 | 18 | 18 | 61 |
| 8 | 18 | 9 | 18 | 19 | 64 |
| **Total** | **116** | **80** | **127** | **57** | **380** |

## Checks completed
1. Every bank entry has a non-empty question, exactly four options, and an integer correct-answer index from 0 to 3.
2. Every subject belongs to the approved class-subject scheme: Classes 3–5 (English, Urdu, Mathematics); Classes 6–8 (English, Urdu, Mathematics, Science).
3. No exact normalized duplicate question stem was found within the same class and subject.
4. Full inventory exported to `MCQ_Master.csv`, preserving current option order and answer index.

## Important limitations — do not treat this as full content verification
- The current portal bank stores only question, four options, correct-option index and a source label. It does **not** store original PDF page numbers, official SLO codes, SLO descriptions, topic/subtopic, difficulty, or individual answer-verification notes.
- The source labels indicate 254 PDF-tagged records and 126 generated/concept-based records. These labels alone do not prove that every answer was independently verified against the original PDF.
- Therefore this audit verifies the live bank's structure, approved subjects, counts and exact within-class/subject duplicate stems. It does **not** certify the factual correctness of all 380 answer keys, nor can it certify PDF page-by-page completeness or SLO alignment.
- No question has been silently deleted or changed as part of this audit.

## Required next phase for a fully certified question bank
Re-open each of the six source PDFs, map every PDF-tagged MCQ to its exact page, independently solve/check the answer, assign SLO/topic, identify visual-dependent and ambiguous questions, then produce the answer-verification, duplicate and pending-question registers. Missing metadata is deliberately marked "Not recorded" in the master export rather than guessed.
