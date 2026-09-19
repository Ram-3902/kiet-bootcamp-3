# 07_filter_pack.py — Block 7: put it together. This is Stage 5 without SQL and without HTTP.
#
#   python3 07_filter_pack.py
#
# Take rows (list of tuples) -> keep only one city (the for-loop with the if inside)
# -> pack the kept rows into a list of dicts -> print the answer as JSON.
#
# Expected output:
#   {"count": 2, "students": [{"student_name": "Ravi Teja Kanchi", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}, {"student_name": "Sai Kiran Bommu", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}]}

import json

rows = [
    ("Ravi Teja Kanchi", "Sri Chaitanya Junior College", "Visakhapatnam"),
    ("Lakshmi Prasanna Gudla", "Narayana Junior College", "Vijayawada"),
    ("Sai Kiran Bommu", "Sri Chaitanya Junior College", "Visakhapatnam"),
    ("Divya Sree Pothula", "Narayana Junior College", "Vijayawada"),
]

wanted_city = "Visakhapatnam"

students = []
# TODO: for each row: unpack; if city == wanted_city, append the dict with the three keys to students

answer = {"count": len(students), "students": students}
# TODO: print json.dumps(answer)
