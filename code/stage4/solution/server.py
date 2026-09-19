# server.py — Stage 4 (solution). Your first server.
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
    return f"Good morning {name}"


# ---- Task 2: GET /about  ->  your own details, the three keys of the table --
@route("/about")
def about():
    return {"student_name": "Ravi Teja Kanchi",
            "inter_college": "Sri Chaitanya Junior College",
            "inter_city": "Visakhapatnam"}


# ---- start --------------------------------------------------------------
print(f"Serving on http://localhost:{port}  — Ctrl+C to stop")
run(host="localhost", port=port, debug=True)
