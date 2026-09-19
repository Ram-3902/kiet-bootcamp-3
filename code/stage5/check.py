#!/usr/bin/env python3
"""Stage 5 self-check. Builds a temporary database with the 4 sample rows, tells you
how to start your server against it, then checks all five routes.

    python3 check.py                     -> prints the server command, then checks port 8080
    python3 check.py --port 8090         -> checks another port
"""
import json
import os
import sqlite3
import sys
import tempfile
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE_SQL = os.path.join(HERE, "..", "..", "data", "sample_team_details.sql")
PORT = 8080
if "--port" in sys.argv:
    PORT = int(sys.argv[sys.argv.index("--port") + 1])
BASE = f"http://localhost:{PORT}"

# ---- the temp DB ------------------------------------------------------------
TMP = os.path.join(tempfile.gettempdir(), "kiet_stage5_check.db")
if not os.path.exists(TMP):
    conn = sqlite3.connect(TMP)
    conn.executescript(open(SAMPLE_SQL, encoding="utf-8").read())
    conn.commit()
    conn.close()

START = f"python3 server.py --db {TMP}"
if PORT != 8080:
    START += f" --port {PORT}"

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


def get(path):
    try:
        with urllib.request.urlopen(BASE + path, timeout=3) as r:
            return r.status, dict(r.headers), r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read().decode()
    except (urllib.error.URLError, ConnectionError, TimeoutError):
        print(f"Cannot connect to localhost:{PORT} — is the server running?")
        print(f"  Terminal 1 (in this folder):  {START}")
        sys.exit(1)


def as_json(text):
    try:
        return json.loads(text)
    except ValueError:
        return None


print(f"Check database: {TMP}")
print(f"Start your server against it in Terminal 1:  {START}")
print()

RAVI = {"student_name": "Ravi Teja Kanchi", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}
SAI = {"student_name": "Sai Kiran Bommu", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}
LAKSHMI = {"student_name": "Lakshmi Prasanna Gudla", "inter_college": "Narayana Junior College", "inter_city": "Vijayawada"}
DIVYA = {"student_name": "Divya Sree Pothula", "inter_college": "Narayana Junior College", "inter_city": "Vijayawada"}

# is the server on the check DB at all?
s, h, b = get("/students?college=Narayana+Junior+College")
j = as_json(b)
if s == 200 and j == {"count": 2, "students": [LAKSHMI, DIVYA]}:
    report(True, "GET /students?college=Narayana+Junior+College (given route, server is on the check DB)")
elif s == 200 and isinstance(j, dict) and "students" in j:
    report(False, "server is using the check database", "the 2 sample Narayana students", j)
    print(f"  Restart the server with:  {START}")
    print()
    print(f"{passed} passed, {failed} failed")
    sys.exit(1)
else:
    report(False, "GET /students?college=Narayana+Junior+College (given route)", "200 + count 2", f"{s} {b[:80]}")

s, h, b = get("/students")
report(s == 400 and as_json(b) == {"error": "college parameter is required"}, "GET /students without college -> 400", {"error": "college parameter is required"}, f"{s} {b[:80]}")

# Task 1
s, h, b = get("/students/by-location?location=Visakhapatnam")
report(s == 200 and as_json(b) == {"count": 2, "students": [RAVI, SAI]}, "Task 1: GET /students/by-location?location=Visakhapatnam -> 2 students", {"count": 2, "students": [RAVI, SAI]}, b[:120])
s, h, b = get("/students/by-location?location=Guntur")
report(s == 200 and as_json(b) == {"count": 0, "students": []}, "Task 1: GET /students/by-location?location=Guntur -> 0 students", {"count": 0, "students": []}, b[:120])
s, h, b = get("/students/by-location")
report(s == 400 and as_json(b) == {"error": "location parameter is required"}, "Task 1: GET /students/by-location without location -> 400", {"error": "location parameter is required"}, f"{s} {b[:80]}")

# Task 2
s, h, b = get("/students/search?college=Narayana+Junior+College&location=Vijayawada")
report(s == 200 and as_json(b) == {"count": 2, "students": [LAKSHMI, DIVYA]}, "Task 2: GET /students/search Narayana + Vijayawada -> 2 students", {"count": 2, "students": [LAKSHMI, DIVYA]}, b[:120])
s, h, b = get("/students/search?college=Narayana+Junior+College&location=Visakhapatnam")
report(s == 200 and as_json(b) == {"count": 0, "students": []}, "Task 2: GET /students/search Narayana + Visakhapatnam -> 0 students", {"count": 0, "students": []}, b[:120])
s, h, b = get("/students/search?college=Narayana+Junior+College")
report(s == 400 and as_json(b) == {"error": "college and location parameters are required"}, "Task 2: GET /students/search with only college -> 400", {"error": "college and location parameters are required"}, f"{s} {b[:80]}")

# Task 3
s, h, b = get("/colleges")
report(s == 200 and as_json(b) == {"colleges": ["Narayana Junior College", "Sri Chaitanya Junior College"]}, "Task 3: GET /colleges -> the 2 colleges, sorted", {"colleges": ["Narayana Junior College", "Sri Chaitanya Junior College"]}, b[:120])

# Task 4
s, h, b = get("/count?college=Sri+Chaitanya+Junior+College")
report(s == 200 and as_json(b) == {"college": "Sri Chaitanya Junior College", "count": 2}, "Task 4: GET /count?college=Sri+Chaitanya+Junior+College -> 2", {"college": "Sri Chaitanya Junior College", "count": 2}, b[:120])
s, h, b = get("/count?college=Vignan+Junior+College")
report(s == 200 and as_json(b) == {"college": "Vignan Junior College", "count": 0}, "Task 4: GET /count?college=Vignan+Junior+College -> 0", {"college": "Vignan Junior College", "count": 0}, b[:120])
s, h, b = get("/count")
report(s == 400 and as_json(b) == {"error": "college parameter is required"}, "Task 4: GET /count without college -> 400", {"error": "college parameter is required"}, f"{s} {b[:80]}")

print()
print(f"{passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
