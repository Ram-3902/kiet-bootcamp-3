# by_college.py — Stage 2. Prints the names of the students from one college.
#
#   python3 by_college.py "Narayana Junior College"
#   python3 by_college.py "Narayana Junior College" ../../data/all_students.db
#
# The college name comes from the command line, so the SAME program answers
# for any college. The value goes into the SQL through ?, never into the string.

import os
import sys
import sqlite3

here = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(here, "..", "..", "data", "team_details.db")
if len(sys.argv) > 2:
    db_path = sys.argv[2]

if len(sys.argv) < 2:
    print('usage: python3 by_college.py "Narayana Junior College"')
else:
    college = sys.argv[1]

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # TODO (Task 2): execute the query with ? and print each student_name.
    #   Same shape as read_all.py, but:
    #     - the SQL ends with   WHERE inter_college = ?
    #     - execute() takes a second argument: the list of values for the ?s
    #     - each row has one item, so use row[0]

    connection.close()
