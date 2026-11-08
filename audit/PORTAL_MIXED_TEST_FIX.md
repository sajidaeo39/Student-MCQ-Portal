# Portal Mixed-Test Logic Fix

Updated `index.html` so the mixed test now follows the project specification:

- Classes 3, 4 and 5: English 3 + Urdu 3 + Mathematics 3 = **9 questions / 9 marks**.
- Classes 6, 7 and 8: English 3 + Urdu 3 + Mathematics 3 + Science 3 = **12 questions / 12 marks**.
- Each subject pool combines the class's main bank and any configured supplemental questions.
- The mixed-test card now displays the class-appropriate subject distribution and total.
- The test still uses the existing random question and option shuffling, scoring, review and attempt-statistics functions.
- No student record, attempt data, subject-wise practice bank, or Google Apps Script endpoint was changed.

## Validation
- Code review confirms all selected subjects require at least three available questions; a clear alert appears if a subject pool is short.
- Full browser/device QA remains necessary after GitHub Pages deployment.
