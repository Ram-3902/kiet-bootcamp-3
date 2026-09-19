# read_all.py — Stage 2. Reads every row of the team database and prints it.
#
#   python3 read_all.py                          (uses ../../data/team_details.db)
#   python3 read_all.py ../../data/all_students.db
#
# Three objects, in order:
#   sqlite3      the module — the driver, like #include <stdio.h>
#   connection   the open file — like FILE *
#   cursor       where you run a query and read its rows — like the file position

import os
import sys
import sqlite3

here = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(here, "..", "..", "data", "team_details.db")
if len(sys.argv) > 1:
    db_path = sys.argv[1]

if not os.path.exists(db_path):
    print(f"No database at {db_path}")
    print("Go back to Stage 1 and create team_details.db first.")
else:
    connection = sqlite3.connect(db_path)          # open the file
    cursor = connection.cursor()                   # get a cursor

    cursor.execute("SELECT student_name, inter_college, inter_city FROM students")
    # execute() only positions. It does not give you rows.

    rows = cursor.fetchall()
    # fetchall() reads. rows is a list of tuples, one tuple per row.

    for row in rows:
        name, college, city = row                  # unpack the tuple
        print(f"{name} - {college} - {city}")

    connection.close()
