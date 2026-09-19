# server.py — Stage 5. The whole backend: HTTP in, SQL in the middle, JSON out.
#
#   Terminal 1:  python3 server.py                                   (port 8080, data/team_details.db)
#                python3 server.py --db ../../data/all_students.db   (Stage 6)
#                python3 server.py --port 8090 --db some/other.db
#
# Every route does the same three things:
#   unpack  — read the parameter from the request
#   query   — run SQL with ? for the value
#   pack    — turn the rows (tuples) into a list of dicts, return it
#
# Read the given route /students line by line before writing anything.

import os
import sys
import sqlite3
from bottle import route, run, request, response, hook

# ---- read --port and --db from the command line -------------------------
here = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(here, "..", "..", "data", "team_details.db")
port = 8080
previous = ""
for word in sys.argv:
    if previous == "--port":
        port = int(word)
    if previous == "--db":
        db_path = word
    previous = word
db_path = os.path.abspath(db_path)


# ---- the two helpers you reuse in every route ----------------------------
def query(sql, params):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    connection.close()
    return rows


def pack(rows):
    result = []
    for row in rows:
        name, college, city = row
        result.append({"student_name": name, "inter_college": college, "inter_city": city})
    return result


# ---- runs after every response ------------------------------------------
@hook("after_request")
def allow_browser():
    response.headers["Access-Control-Allow-Origin"] = "*"   # This line matters in Stage 8. Ignore it for now.


# ---- the given route: read it line by line ------------------------------
@route("/students")
def students_by_college():
    college = request.query.get("college")                           # unpack
    if college is None:
        response.status = 400
        return {"error": "college parameter is required"}
    rows = query("SELECT student_name, inter_college, inter_city "
                 "FROM students WHERE inter_college = ?", [college])  # query
    return {"count": len(rows), "students": pack(rows)}               # pack


# ---- Task 1: GET /students/by-location?location=Y  ->  same shape as /students
@route("/students/by-location")
def students_by_location():
    # TODO (Task 1): unpack "location"; 400 with {"error": "location parameter is required"} if missing;
    #                query WHERE inter_city = ?; return {"count": ..., "students": pack(rows)}
    return {"todo": "Task 1"}


# ---- Task 2: GET /students/search?college=X&location=Y  ->  both required
@route("/students/search")
def students_search():
    # TODO (Task 2): unpack both; if either is None -> 400 {"error": "college and location parameters are required"};
    #                query WHERE inter_college = ? AND inter_city = ?  with [college, location]
    return {"todo": "Task 2"}


# ---- Task 3: GET /colleges  ->  {"colleges": ["...", "..."]} ----------------
@route("/colleges")
def colleges():
    # TODO (Task 3): write the SQL. Every college once, sorted:  SELECT DISTINCT ... ORDER BY ...
    rows = query("", [])
    names = []
    for row in rows:
        names.append(row[0])          # each row is a tuple with one item
    return {"colleges": names}


# ---- Task 4: GET /count?college=X  ->  {"college": "X", "count": n} ---------
@route("/count")
def count():
    college = request.query.get("college")
    if college is None:
        response.status = 400
        return {"error": "college parameter is required"}
    # TODO (Task 4): write the SQL. How many rows have this college?  SELECT COUNT(*) ... WHERE ... = ?
    #                (until the SQL is written this route answers 500: the empty SQL has no ? for the college)
    rows = query("", [college])
    return {"college": college, "count": rows[0][0]}   # COUNT(*) gives one row with one number


# ---- start --------------------------------------------------------------
print(f"Serving on http://localhost:{port}  (DB: {db_path})  — Ctrl+C to stop")
run(host="localhost", port=port, debug=True)
