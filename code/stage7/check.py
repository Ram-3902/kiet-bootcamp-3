#!/usr/bin/env python3
"""Stage 7 self-check: is the frontend served on 9000, and is the backend answering on 8080?
    Terminal 1 (in code/stage5):     python3 server.py --db ../../data/all_students.db
    Terminal 2 (in code/frontend):   python3 -m http.server 9000
    Terminal 3:                      python3 check.py
"""
import json
import sys
import urllib.error
import urllib.request

FRONT = 9000
BACK = 8080
if "--front" in sys.argv:
    FRONT = int(sys.argv[sys.argv.index("--front") + 1])
if "--back" in sys.argv:
    BACK = int(sys.argv[sys.argv.index("--back") + 1])

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


def get(port, path, hint):
    try:
        with urllib.request.urlopen(f"http://localhost:{port}{path}", timeout=3) as r:
            return r.status, r.read().decode(errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors="replace")
    except (urllib.error.URLError, ConnectionError, TimeoutError):
        print(f"Cannot connect to localhost:{port} — is the server running?  ({hint})")
        sys.exit(1)


s, b = get(FRONT, "/index.html", "Terminal 2, in code/frontend: python3 -m http.server 9000")
report(s == 200 and "<title>" in b, f"port {FRONT} serves index.html", "200 + an HTML page", f"{s} {b[:60]!r}")

s, b = get(FRONT, "/app.js", "Terminal 2, in code/frontend: python3 -m http.server 9000")
report(s == 200 and "BACKEND" in b, f"port {FRONT} serves app.js", "200 + the BACKEND constant", f"{s} {b[:60]!r}")

s, b = get(BACK, "/colleges", "Terminal 1, in code/stage5: python3 server.py --db ../../data/all_students.db")
try:
    j = json.loads(b)
except ValueError:
    j = None
report(s == 200 and isinstance(j, dict) and isinstance(j.get("colleges"), list), f"port {BACK} answers /colleges with JSON", "200 + {'colleges': [...]}", f"{s} {b[:60]!r}")

print()
print(f"{passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
