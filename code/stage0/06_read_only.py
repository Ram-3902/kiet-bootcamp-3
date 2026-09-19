# 06_read_only.py — Block 6: two strange things. READ this file. Do not run it (bottle.py is not in this folder).
#
# Strange thing 1: the line starting with @.
#   @route("/hai") is a decorator. It means one thing only:
#   "register the function below at the address /hai". Nothing more.
#
# Strange thing 2: None.
#   None is Python's NULL. A function that finds nothing gives you None.
#   You guard against it with:   if x is None:

from bottle import route, run, request

@route("/hai")
def hai():
    return "Namasthey!!!"

@route("/greet")
def greet():
    name = request.query.get("name")
    if name is None:
        return "name is required"
    return f"Namasthey {name}"

run(host="localhost", port=8080)

# Q1. Which function runs when a browser asks for /greet?name=Ravi ?
# A1: greet() — because of the @route("/greet") line above it.
# Q2. What does request.query.get("name") return when the URL is just /greet ?
# A2: None — there is no name in the query string.
# Q3. Which line stops that from crashing?
# A3: if name is None:  — it returns before the f-string tries to use name.
# Q4. What would you change so /hai answers "Hello" instead?
# A4: Only the return line inside hai(): return "Hello". The @route line stays the same.
