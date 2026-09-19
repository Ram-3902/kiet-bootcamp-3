# server.py — Stage 4. Your first server.
#
#   Terminal 1:  python3 server.py              (port 8081, so it can run beside the Stage 3 server on 8080)
#                python3 server.py --port 8082
#
# A route is a function with an address.
#   @route("/hai") means: when someone asks for /hai, call the function below.
#   Return a string  -> a text response.
#   Return a dict    -> Bottle turns it into JSON for you.

import sys
from bottle import route, run, request, response

# ---- read --port from the command line ---------------------------------
port = 8081
previous = ""
for word in sys.argv:
    if previous == "--port":
        port = int(word)
    previous = word


# ---- this one already works -------------------------------------------
@route("/hai")
def hai():
    return "Namasthey!!!"


# ---- Task 1: GET /wish/<name>  ->  Good morning <name> ----------------------
@route("/wish/<name>")
def wish(name):
    # TODO (Task 1): return the text "Good morning " followed by the name
    return "TODO (Task 1)"


# ---- Task 2: POST /iseven, body {"number": 4}  ->  {"number": 4, "is_even": true}
@route("/iseven", method="POST")
def iseven():
    data = request.json            # the body, already a dict (or None if no JSON was sent)
    # TODO (Task 2): if data is None, or data has no "number", answer with status 400 and an error dict.
    #                otherwise return a dict with "number" and "is_even"  (hint: number % 2 == 0)
    return "TODO (Task 2)"


# ---- Task 3: GET /about  ->  your own details, the three keys of the table --
@route("/about")
def about():
    # TODO (Task 3): return a dict with exactly these three keys, filled with YOUR details:
    #                "student_name", "inter_college", "inter_city"
    return "TODO (Task 3)"


# ---- start --------------------------------------------------------------
print(f"Serving on http://localhost:{port}  — Ctrl+C to stop")
run(host="localhost", port=port, debug=True)
