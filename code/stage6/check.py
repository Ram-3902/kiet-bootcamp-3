#!/usr/bin/env python3
"""Stage 6 self-check: was all_students.db built, and is the server on 8080 serving it?
    Terminal 1 (in code/stage5):  python3 server.py --db ../../data/all_students.db
    Terminal 2:                   python3 check.py        (or --port 8090)
"""
import json
import os
import sqlite3
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, "..", "..", "data", "all_students.db"))
PORT = 8080
if "--port" in sys.argv:
    PORT = int(sys.argv[sys.argv.index("--port") + 1])
BASE = f"http://localhost:{PORT}"

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


def finish():
    print()
    print(f"{passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)


def get(path):
    try:
        with urllib.request.urlopen(BASE + path, timeout=3) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
    except (urllib.error.URLError, ConnectionError, TimeoutError):
        print(f"Cannot connect to localhost:{PORT} — is the server running?")
        print("  Terminal 1 (in code/stage5):  python3 server.py --db ../../data/all_students.db")
        finish()


# ---- the file ----------------------------------------------------------------
if not os.path.exists(DB):
    report(False, f"all_students.db exists at {DB}", "a file", "nothing — in the data folder run: sqlite3 all_students.db < all_students.sql")
    finish()
report(True, f"all_students.db exists at {DB}")

conn = sqlite3.connect(DB)
n = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
report(n == 200, "all_students.db has 200 rows", 200, n)
colleges = [r[0] for r in conn.execute("SELECT DISTINCT inter_college FROM students ORDER BY inter_college").fetchall()]
report(len(colleges) == 12, "all_students.db has 12 colleges", 12, len(colleges))
narayana = conn.execute("SELECT COUNT(*) FROM students WHERE inter_college = 'Narayana Junior College'").fetchone()[0]
conn.close()

# ---- the server -----------------------------------------------------------
s, b = get("/colleges")
try:
    got = json.loads(b).get("colleges")
except ValueError:
    got = b[:80]
if got == colleges:
    report(True, f"server on {PORT} serves all_students.db: /colleges lists the same 12 colleges")
elif isinstance(got, list) and len(got) < 12:
    report(False, f"server on {PORT} serves all_students.db", "12 colleges", f"{len(got)} — the server is still on team_details.db; restart it with --db ../../data/all_students.db")
else:
    report(False, f"server on {PORT} serves all_students.db", colleges, got)

s, b = get("/count?college=Narayana+Junior+College")
try:
    got = json.loads(b).get("count")
except ValueError:
    got = b[:80]
report(got == narayana, f"/count?college=Narayana+Junior+College matches the file ({narayana})", narayana, got)

finish()
