# Student MCQ Portal — Question Limits and Mixed Test Rules

Updated: 2026-11-09

## Fixed question-bank limit

The practice bank contains exactly **3 questions per class-subject set** (21 sets; 63 questions total).

- Classes 3, 4, 5: English, Urdu, Mathematics only.
- Classes 6, 7, 8: English, Urdu, Mathematics, Science only.
- No extra questions or additional subjects are included.
- Subject-wise practice always selects all 3 questions from the selected class and subject.
- Each question retains four options and its correct-answer index.

The selected three-question sets are retained from the portal's existing reviewed bank. The previous two supplemental questions per subject have been removed. The current set is not being represented as a newly completed page-by-page review of the entire source PDF.

## Test formats

| Test mode | Question rule | Total |
|---|---|---:|
| Individual class, subject-wise | 3 questions from the selected subject | 3 |
| Individual class, Classes 3–5 mixed | 3 English + 3 Urdu + 3 Mathematics | 9 |
| Individual class, Classes 6–8 mixed | 3 English + 3 Urdu + 3 Mathematics + 3 Science | 12 |
| Group Mix, Classes 3–5 | One random question from every class-subject set (3 classes × 3 subjects) | 9 |
| Group Mix, Classes 6–8 | One random question from every class-subject set (3 classes × 4 subjects) | 12 |
| Overall Mix, Classes 3–8 | Two random questions per class, from two distinct approved subjects per class | 12 |

The Overall Mix includes all six classes. Because it is limited to 12 questions, it samples two distinct subjects per class; the subjects are selected randomly from that class's approved list. It does not claim to cover every subject in all six classes in a single attempt.

## Timer and result

- Fixed total duration: 5 minutes per test.
- When time expires, the test submits automatically.
- Subject-wise performance is calculated from the questions in the submitted test.
- Student and school names remain optional.

## Google Apps Script

The unused legacy `google-apps-script/` folder (Code.gs and its deployment guide) has been removed. The active portal HTML does not reference Google Apps Script or a Google Apps Script endpoint.

The existing shared statistics counter in the portal uses a separate third-party counter endpoint. This change does not remove the statistics display or that separate counter integration.

## Verification limitations

The question bank has been checked for exactly 3 questions in each of the 21 approved class-subject sets and for valid four-option answer-key structure. This structural check does not replace a full visual re-audit of all 247 scanned PDF pages or independent confirmation of official PECTAA SLO codes.
