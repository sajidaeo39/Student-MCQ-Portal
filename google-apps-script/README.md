# Google Sheets statistics setup

The portal's four shared totals use a Google Apps Script web app. The script creates its own Google spreadsheet on first use and stores only hashes of optional school/student names plus test totals and class/subject metadata.

## Deploy the backend

1. Open https://script.google.com/ while signed in to the Google account that should own the statistics sheet.
2. Create a **New project**.
3. Replace the starter code in `Code.gs` with the complete contents of this folder's `Code.gs`.
4. Click **Deploy → New deployment**.
5. Select type **Web app**.
6. Set **Execute as** to **Me**.
7. Set **Who has access** to **Anyone** (the portal is public; do not store sensitive student data).
8. Click **Deploy**, authorize the script, and copy the Web app URL ending in `/exec`.

## Connect the portal

In the repository's `index.html`, find:

```js
const STATS_API_URL = "PASTE_YOUR_GOOGLE_APPS_SCRIPT_WEB_APP_URL_HERE";
```

Replace the placeholder with the copied URL, keep the quotation marks, and commit the change to `main`.

## What is counted

- **Total Schools:** distinct non-empty school names entered.
- **Total Students:** distinct non-empty student-name + school combinations.
- **Tests Attempted:** successfully submitted tests.
- **Questions Attempted:** questions answered (not skipped).

School and student names are optional. Names are normalized and SHA-256 hashed in the browser before sending; the sheet does not store the entered names in plain text. If no school/student names are entered, the test and answered-question totals still increase, but school/student counts do not.

Anyone can submit a test to this public endpoint. Do not use this setup for confidential records, grades, or high-stakes assessment. The spreadsheet is owned by the Google account deploying the script.
