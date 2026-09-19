#!/usr/bin/env python3
"""Stage 4 self-check: is YOUR server answering on port 8081?
    Terminal 1:  python3 server.py
    Terminal 2:  python3 check.py            (or: python3 check.py --port 8082)
"""
import json
import sys
import urllib.error
import urllib.request

PORT = 8081
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


def request(method, path, body=None):
    data = None
    headers = {}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(BASE + path, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=3) as r:
            return r.status, dict(r.headers), r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read().decode()
    except (urllib.error.URLError, ConnectionError, TimeoutError):
        print(f"Cannot connect to localhost:{PORT} — is the server running?  (Terminal 1: python3 server.py)")
        sys.exit(1)


def as_json(text):
    try:
        return json.loads(text)
    except ValueError:
        return None


s, h, b = request("GET", "/hai")
report(s == 200 and b == "Namasthey!!!", "GET /hai -> Namasthey!!! (given)", "Namasthey!!!", b)

s, h, b = request("GET", "/wish/Ravi")
report(s == 200 and b == "Good morning Ravi", "Task 1: GET /wish/Ravi -> Good morning Ravi", "Good morning Ravi", b)

s, h, b = request("GET", "/wish/Lakshmi")
report(s == 200 and b == "Good morning Lakshmi", "Task 1: GET /wish/Lakshmi -> Good morning Lakshmi", "Good morning Lakshmi", b)

s, h, b = request("GET", "/about")
j = as_json(b)
keys = ["student_name", "inter_college", "inter_city"]
if not isinstance(j, dict):
    report(False, "Task 2: GET /about returns a dict (JSON object)", "a dict", b[:60])
else:
    report(sorted(j.keys()) == sorted(keys), "Task 2: /about has exactly the three keys of the students table", keys, sorted(j.keys()))
    empty = [k for k in keys if not isinstance(j.get(k), str) or j.get(k).strip() == ""]
    report(not empty, "Task 2: /about values are non-empty strings", "your real details", f"empty or missing: {empty}" if empty else j)

print()
print(f"{passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
