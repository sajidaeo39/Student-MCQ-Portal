# Class 8 MCQ Audit — PECTAA Smart Practice Portal

**Audit date:** 25 November 2026  
**Scope:** Class 8 records only. Read-only analysis of the deployed data recovered from the portal's 16 deployment parts. No MCQ data, portal code, layout, or other class was changed by this audit.

## Executive result
- Class 8 records: **1,260**
- Unique question-and-options groups: **35**
- Repeated copies beyond the first instance: **1,225**
- Duplicate groups: **35**
- Record IDs: **No duplicate mcq_id values detected**
- Blank question/options: **0**
- SLO description field blank: **1260 of 1260**
- Answer-key consistency: no conflicting answer-content groups were detected in the prior comparison; this is not independent factual validation.

## Subject summary
| Subject | Rows | Unique MCQs | Duplicate copies |
|---|---:|---:|---:|
| English | 360 | 8 | 352 |
| Mathematics | 320 | 15 | 305 |
| Science | 280 | 6 | 274 |
| Urdu | 300 | 6 | 294 |
| **Total** | **1260** | **35** | **1225** |

## Repetition pattern
The same question and same four option contents recur under different month/SLO labels. Matching ignores metadata suffixes and option order, so shuffled options do not hide duplicates. All 35 unique content groups appear in all eight scheduled month labels (April, May, August / September, October, November, December, January, February).

## Unique-bank sufficiency for a 9-question subject test
| Subject | Unique MCQs | Shortfall for 9 |
|---|---:|---:|---:|
| English | 8 | 1 |
| Mathematics | 15 | 0 |
| Science | 6 | 3 |
| Urdu | 6 | 3 |

A 9-question test cannot be generated without reuse for English, Science, or Urdu from the current unique bank. Mathematics has 15 unique records.

## Academic quality and alignment findings
1. **Critical:** SLO description is empty in all 1,260 Class 8 rows, so alignment to official SLO wording cannot be verified from this field.
2. **Critical:** Only 35 unique MCQs support the Class 8 dataset; the raw record count substantially overstates question-bank breadth.
3. **High:** Several questions appear below typical Class 8 cognitive demand (e.g. phonics initial letter, basic noun recognition, 6×6, identifying the heart, melting ice, simple antonym/synonym). These are review flags, not definitive curriculum judgments; official textbook/SLO reference is needed.
4. **High:** Difficulty/cognitive labels appear to follow a repeating Easy/Knowledge, Medium/Understanding, Hard/Application pattern. Labels require independent review.
5. **High:** Some different stems test the same elementary skill with only small numerical changes. These are not exact duplicates but provide limited breadth.
6. **Data integrity:** No missing question/options were found. Duplicate answer keys were consistent by answer content; correctness still needs subject-expert validation.

## Recommended correction sequence
1. Do not simply delete 1,225 repeated copies: only 35 unique items would remain, insufficient for 9 questions in three subjects, and month/SLO mapping would be lost.
2. Validate the official Class 8 monthly SLO plan and source material, then create genuinely distinct MCQs for each required SLO/month.
3. Preserve month/SLO metadata and reject duplicate content during import using normalized stem + normalized option contents, independent of option order.
4. Add a test-generation guard so a single test never contains the same canonical MCQ twice.
5. Re-audit before deploying. Keep all other classes and unrelated portal functionality unchanged.

## Duplicate-group index
The companion CSV lists every Class 8 record, its duplicate group, month, SLO, question, options, and answer. The first row in each group is marked KEEP_CANDIDATE for review only; it is not a recommendation to delete other rows until month/SLO references are reconciled.

| Group | Subject | Question (metadata suffix omitted) | Occurrences |
|---|---|---|---:|
| G01 | Urdu | درج ذیل میں سے اسم معرفہ (خاص نام) کی نشاندہی کریں: | 60 |
| G02 | Urdu | لفظ 'روشنی' کا درست متضاد لفظ کون سا ہے؟ | 60 |
| G03 | Science | Which of the following is a basic survival need of all animals? | 56 |
| G04 | Science | Which human organ is responsible for pumping blood? | 56 |
| G05 | English | Which letter represents the initial sound in 'Apple'? | 54 |
| G06 | English | Identify the naming word (noun) in: 'The cat sleeps on the rug.' | 54 |
| G07 | English | Choose the correct contracted form of 'do not': | 54 |
| G08 | English | Which pronoun correctly replaces 'Sara' in: 'Sara is reading.'? | 54 |
| G09 | Mathematics | Which fraction represents two shaded parts out of four equal parts? | 48 |
| G10 | Mathematics | How many vertices (corners) does a rectangle have? | 48 |
| G11 | Urdu | لفظ 'شجر' کا ہم معنی (مترادف) لفظ کیا ہے؟ | 45 |
| G12 | Urdu | لفظ 'کتاب' کی درست جمع کیا ہوگی؟ | 45 |
| G13 | Urdu | لفظ 'استاد' کا مؤنث لفظ کیا ہے؟ | 45 |
| G14 | Urdu | نظامِ قواعد کے مطابق درست جملے کا انتخاب کریں: | 45 |
| G15 | Science | Which vital gas do green plants produce during photosynthesis? | 42 |
| G16 | Science | Changing ice (solid) into water (liquid) is called: | 42 |
| G17 | Science | What force pulls objects toward the center of Earth? | 42 |
| G18 | Science | Organisms that make their own food using sunlight are: | 42 |
| G19 | English | Which mark should end a question sentence? | 36 |
| G20 | English | Fill in the blank: 'The book is ___ the desk.' | 36 |
| G21 | English | Which word is an adjective in 'a big red ball'? | 36 |
| G22 | English | Select the action verb in: 'Ali runs fast in the park.' | 36 |
| G23 | Mathematics | Which standard unit measures the length of a classroom desk? | 32 |
| G24 | Mathematics | What is the place value of digit 5 in 503? | 16 |
| G25 | Mathematics | Calculate the sum: 121 + 46 = ? | 16 |
| G26 | Mathematics | Solve: 252 - 32 = ? | 16 |
| G27 | Mathematics | Multiply: 6 x 6 = ? | 16 |
| G28 | Mathematics | What is the place value of digit 5 in 573? | 16 |
| G29 | Mathematics | Calculate the sum: 128 + 53 = ? | 16 |
| G30 | Mathematics | Solve: 259 - 39 = ? | 16 |
| G31 | Mathematics | Multiply: 7 x 6 = ? | 16 |
| G32 | Mathematics | What is the place value of digit 5 in 643? | 16 |
| G33 | Mathematics | Calculate the sum: 135 + 60 = ? | 16 |
| G34 | Mathematics | Solve: 266 - 46 = ? | 16 |
| G35 | Mathematics | Multiply: 5 x 6 = ? | 16 |

**Important:** No production code or live Class 8 data has been changed. This report records the audit findings only.