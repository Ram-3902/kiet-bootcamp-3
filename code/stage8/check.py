#!/usr/bin/env python3
"""Stage 8 self-check: does the backend send the header the browser needs?
    Terminal 1 (in code/stage5):  python3 server.py --db ../../data/all_students.db
    Terminal 3:                   python3 check.py        (or --port 8090)
"""
import sys
import urllib.error
import urllib.request

PORT = 8080
if "--port" in sys.argv:
    PORT = int(sys.argv[sys.argv.index("--port") + 1])

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


try:
    with urllib.request.urlopen(f"http://localhost:{PORT}/colleges", timeout=3) as r:
        status, headers = r.status, dict(r.headers)
except urllib.error.HTTPError as e:
    status, headers = e.code, dict(e.headers)
except (urllib.error.URLError, ConnectionError, TimeoutError):
    print(f"Cannot connect to localhost:{PORT} — is the server running?  (Terminal 1, in code/stage5: python3 server.py --db ../../data/all_students.db)")
    sys.exit(1)

report(status == 200, "GET /colleges -> 200", 200, status)

acao = headers.get("Access-Control-Allow-Origin")
if acao == "*":
    report(True, "response has  Access-Control-Allow-Origin: *  (the browser will accept it)")
elif acao is None:
    report(False, "response has  Access-Control-Allow-Origin: *", "*", "no such header — is the allow_browser hook commented out? Put it back and restart.")
else:
    report(False, "response has  Access-Control-Allow-Origin: *", "*", acao)

report(headers.get("Content-Type", "").startswith("application/json"), "response Content-Type is application/json", "application/json", headers.get("Content-Type"))

print()
print("Compare by eye with:  curl -i localhost:%d/colleges" % PORT)
print(f"{passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
