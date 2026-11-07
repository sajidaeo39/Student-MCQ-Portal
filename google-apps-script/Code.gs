/**
 * The Educational Helper - Student MCQ Portal aggregate statistics
 * Deploy as a Web App: Execute as Me; Who has access: Anyone.
 * Only SHA-256 hashes of optional school/student names are stored.
 */
const SHEET_NAME = 'Test Statistics';

function doGet(e) {
  const p = (e && e.parameter) || {};
  const callback = /^[a-zA-Z_$][0-9a-zA-Z_$\.]*$/.test(p.callback || '') ? p.callback : '';
  let result;
  try {
    if (p.action === 'record') {
      result = recordAttempt_(p);
    } else {
      result = getSummary_();
    }
  } catch (err) {
    result = { ok: false, error: String(err) };
  }
  const body = callback
    ? callback + '(' + JSON.stringify(result) + ');'
    : JSON.stringify(result);
  return ContentService.createTextOutput(body).setMimeType(
    callback ? ContentService.MimeType.JAVASCRIPT : ContentService.MimeType.JSON
  );
}

function getSheet_() {
  const props = PropertiesService.getScriptProperties();
  let id = props.getProperty('STATS_SPREADSHEET_ID');
  let ss;
  if (id) {
    ss = SpreadsheetApp.openById(id);
  } else {
    ss = SpreadsheetApp.create('Educational Helper - MCQ Portal Statistics');
    props.setProperty('STATS_SPREADSHEET_ID', ss.getId());
  }
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) sheet = ss.insertSheet(SHEET_NAME);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Timestamp', 'School Hash', 'Student Hash', 'Class', 'Subject', 'Total Questions', 'Questions Answered', 'Correct', 'Wrong']);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function recordAttempt_(p) {
  const total = Math.max(0, Math.min(500, Number(p.total) || 0));
  const answered = Math.max(0, Math.min(total, Number(p.answered) || 0));
  const correct = Math.max(0, Math.min(answered, Number(p.correct) || 0));
  const wrong = Math.max(0, Math.min(answered - correct, Number(p.wrong) || 0));
  if (!total) throw new Error('Invalid test submission');
  const schoolHash = cleanHash_(p.school);
  const studentHash = cleanHash_(p.student);
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    getSheet_().appendRow([new Date(), schoolHash, studentHash, safeText_(p.className), safeText_(p.subject), total, answered, correct, wrong]);
  } finally {
    lock.releaseLock();
  }
  return { ok: true };
}

function getSummary_() {
  const sheet = getSheet_();
  const values = sheet.getDataRange().getValues();
  const schools = {};
  const students = {};
  let attempts = 0;
  let questionsAttempted = 0;
  for (let i = 1; i < values.length; i++) {
    const row = values[i];
    attempts++;
    if (row[1]) schools[row[1]] = true;
    if (row[2]) students[row[2]] = true;
    questionsAttempted += Number(row[6]) || 0;
  }
  return {
    ok: true,
    totalSchools: Object.keys(schools).length,
    totalStudents: Object.keys(students).length,
    testsAttempted: attempts,
    questionsAttempted: questionsAttempted
  };
}

function cleanHash_(value) {
  const s = String(value || '').trim();
  return /^[a-f0-9]{64}$/i.test(s) ? s.toLowerCase() : '';
}
function safeText_(value) {
  return String(value || '').replace(/[<>\r\n]/g, '').slice(0, 80);
}
