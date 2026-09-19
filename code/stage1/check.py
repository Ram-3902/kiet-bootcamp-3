#!/usr/bin/env python3
"""Stage 1 self-check: is data/team_details.db there, with the right table and real rows?
    python3 check.py                 (from any folder)
    python3 check.py path/to/other.db
"""
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "..", "..", "data", "team_details.db")
if len(sys.argv) > 1:
    DB = sys.argv[1]
DB = os.path.abspath(DB)

passed = 0
failed = 0


def report(ok, what, expected=None, got=None):
    global passed, failed
    if ok:
        passed += 1
        print(f"PASS: {what}")
    else:
        failed += 1
        if expected is None:
            print(f"FAIL: {what}")
        else:
            print(f"FAIL: {what} — expected {expected}, got {got}")


def finish():
    print()
    print(f"{passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)


if not os.path.exists(DB):
    report(False, f"database file exists at {DB}", "a file", "nothing — run sqlite3 team_details.db in the data folder first")
    finish()
report(True, f"database file exists at {DB}")

conn = sqlite3.connect(DB)
cur = conn.cursor()

tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()]
if "students" not in tables:
    report(False, "table 'students' exists", "students", tables if tables else "no tables at all — paste the CREATE TABLE from schema.sql")
    finish()
report(True, "table 'students' exists")

cols = [r[1] for r in cur.execute("PRAGMA table_info(students)").fetchall()]
expected_cols = ["student_name", "inter_college", "inter_city"]
report(cols == expected_cols, "students has the three columns in order", expected_cols, cols)

n = cur.execute("SELECT COUNT(*) FROM students").fetchone()[0]
report(n >= 3, "at least 3 rows (one per team member)", "3 or more", n)

bad = cur.execute(
    "SELECT COUNT(*) FROM students WHERE student_name IS NULL OR student_name = '' "
    "OR inter_college IS NULL OR inter_college = '' OR inter_city IS NULL OR inter_city = ''").fetchone()[0]
report(bad == 0, "no empty names, colleges or cities", "0 empty values", f"{bad} rows with an empty value")

conn.close()
finish()
