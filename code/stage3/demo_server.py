# demo_server.py — the Stage 3 server. You run it and watch it. You do not edit it.
#
#   Terminal 1:  python3 demo_server.py              (listens on port 8080)
#                python3 demo_server.py --port 8090  (any other port)
#
# Four routes. Each one takes its input from a different place:
#   GET  /hai                 nothing
#   GET  /hello/<name>        the path
#   POST /isprime             the body, as JSON  {"number": 17}
#   GET  /greet?name=&lang=   the query string

import sys
from bottle import route, run, request, response

# ---- read --port from the command line ---------------------------------
port = 8080
previous = ""
for word in sys.argv:
    if previous == "--port":
        port = int(word)
    previous = word


# ---- helpers ------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


# ---- routes -------------------------------------------------------------
@route("/hai")
def hai():
    return "Namasthey!!!"


@route("/hello/<name>")
def hello(name):
    return f"How are you doing {name}"


@route("/isprime", method="POST")
def isprime():
    data = request.json            # the body, already parsed into a dict (or None)
    if data is None:
        response.status = 400
        return {"error": "send JSON like {\"number\": 17}"}
    number = data.get("number")
    if number is None:
        response.status = 400
        return {"error": "send JSON like {\"number\": 17}"}
    return {"number": number, "is_prime": is_prime(number)}


@route("/greet")
def greet():
    name = request.query.get("name")   # None if ?name= is not in the URL
    lang = request.query.get("lang")
    if name is None:
        response.status = 400
        return {"error": "name is required"}
    if lang is None:
        lang = "te"
    if lang == "en":
        greeting = f"Hello {name}"
    else:
        greeting = f"Namasthey {name}"
    return {"greeting": greeting, "lang": lang}


# ---- start --------------------------------------------------------------
print(f"Serving on http://localhost:{port}  — Ctrl+C to stop")
run(host="localhost", port=port, debug=True)
