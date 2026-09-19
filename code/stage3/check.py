#!/usr/bin/env python3
"""Stage 3 self-check: is demo_server.py answering on port 8080 the way it should?
    Terminal 1:  python3 demo_server.py
    Terminal 2:  python3 check.py            (or: python3 check.py --port 8090)
"""
import json
import sys
import urllib.error
import urllib.request

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


def request(method, path, body=None):
    """Returns (status, headers, body_text). Exits with a clear message if the server is down."""
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
        print(f"Cannot connect to localhost:{PORT} — is the server running?  (Terminal 1: python3 demo_server.py)")
        sys.exit(1)


def as_json(text):
    try:
        return json.loads(text)
    except ValueError:
        return None


s, h, b = request("GET", "/hai")
report(s == 200 and b == "Namasthey!!!", "GET /hai -> Namasthey!!!", "Namasthey!!!", b)

s, h, b = request("GET", "/hello/Ravi")
report(s == 200 and b == "How are you doing Ravi", "GET /hello/Ravi -> How are you doing Ravi", "How are you doing Ravi", b)

s, h, b = request("POST", "/isprime", {"number": 17})
report(s == 200 and as_json(b) == {"number": 17, "is_prime": True}, "POST /isprime 17 -> is_prime true", {"number": 17, "is_prime": True}, b)

s, h, b = request("POST", "/isprime", {"number": 18})
report(s == 200 and as_json(b) == {"number": 18, "is_prime": False}, "POST /isprime 18 -> is_prime false", {"number": 18, "is_prime": False}, b)

s, h, b = request("POST", "/isprime")
j = as_json(b)
report(s == 400 and isinstance(j, dict) and "error" in j, "POST /isprime with no body -> 400 with an error", "400 + {'error': ...}", f"{s} {b[:60]}")

s, h, b = request("GET", "/greet?name=Ravi&lang=te")
report(s == 200 and as_json(b) == {"greeting": "Namasthey Ravi", "lang": "te"}, "GET /greet?name=Ravi&lang=te", {"greeting": "Namasthey Ravi", "lang": "te"}, b)

s, h, b = request("GET", "/greet?name=Ravi&lang=en")
report(s == 200 and as_json(b) == {"greeting": "Hello Ravi", "lang": "en"}, "GET /greet?name=Ravi&lang=en", {"greeting": "Hello Ravi", "lang": "en"}, b)

s, h, b = request("GET", "/greet?name=Ravi")
report(s == 200 and as_json(b) == {"greeting": "Namasthey Ravi", "lang": "te"}, "GET /greet?name=Ravi (lang defaults to te)", {"greeting": "Namasthey Ravi", "lang": "te"}, b)

s, h, b = request("GET", "/greet?lang=te")
report(s == 400 and as_json(b) == {"error": "name is required"}, "GET /greet without name -> 400", {"error": "name is required"}, f"{s} {b[:60]}")

s, h, b = request("GET", "/nothing")
report(s == 404, "GET /nothing -> 404", 404, s)

print()
print(f"{passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
