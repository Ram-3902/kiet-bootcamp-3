#!/usr/bin/env python3
"""Stage 2 self-check. Loads the sample team into a temporary database and runs
read_all.py and by_college.py against it, comparing their output.
    python3 check.py              checks the files in this folder
    python3 check.py solution     checks the solution folder (should be all PASS)
"""
import os
import sqlite3
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = HERE
if len(sys.argv) > 1 and sys.argv[1] == "solution":
    FOLDER = os.path.join(HERE, "solution")
SAMPLE_SQL = os.path.join(HERE, "..", "..", "data", "sample_team_details.sql")

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
            print(f"FAIL: {what} — expected {expected!r}, got {got!r}")


# a fresh temp DB with the 4 sample rows
tmp = os.path.join(tempfile.gettempdir(), "kiet_stage2_check.db")
if os.path.exists(tmp):
    os.remove(tmp)
conn = sqlite3.connect(tmp)
conn.executescript(open(SAMPLE_SQL, encoding="utf-8").read())
conn.commit()
conn.close()


def run(name, *args):
    folder = HERE if name == "read_all.py" else FOLDER      # read_all.py is given, it lives only in the stage folder
    p = subprocess.run([sys.executable, os.path.join(folder, name), *args],
                       capture_output=True, text=True, cwd=folder)
    if p.returncode != 0:
        err = p.stderr.strip().splitlines()
        return None, err[-1] if err else "exited with an error"
    return p.stdout, None


def expect(label, name, expected_lines, *args):
    out, err = run(name, *args)
    if err is not None:
        report(False, f"{label} runs", "no error", err)
        return
    got = out.strip("\n").splitlines()
    if got == expected_lines:
        report(True, label)
    elif not got and expected_lines:
        report(False, label, expected_lines, "nothing printed")
    else:
        report(False, label, expected_lines, got)


expect("read_all.py prints all 4 sample rows as 'name - college - city'", "read_all.py", [
    "Ravi Teja Kanchi - Sri Chaitanya Junior College - Visakhapatnam",
    "Lakshmi Prasanna Gudla - Narayana Junior College - Vijayawada",
    "Sai Kiran Bommu - Sri Chaitanya Junior College - Visakhapatnam",
    "Divya Sree Pothula - Narayana Junior College - Vijayawada",
], tmp)

expect('by_college.py "Narayana Junior College" prints the 2 Narayana names', "by_college.py",
       ["Lakshmi Prasanna Gudla", "Divya Sree Pothula"], "Narayana Junior College", tmp)

expect('by_college.py "Sri Chaitanya Junior College" prints the 2 Sri Chaitanya names', "by_college.py",
       ["Ravi Teja Kanchi", "Sai Kiran Bommu"], "Sri Chaitanya Junior College", tmp)

expect('by_college.py "Vignan Junior College" prints nothing (no such college in the DB)', "by_college.py",
       [], "Vignan Junior College", tmp)

expect("by_college.py with no argument prints the usage line", "by_college.py",
       ['usage: python3 by_college.py "Narayana Junior College"'])

os.remove(tmp)
print()
print(f"{passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
