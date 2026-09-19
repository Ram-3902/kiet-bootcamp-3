# 07_filter_pack.py — Block 7 (solution): put it together. This is Stage 5 without SQL and without HTTP.
#
#   python3 07_filter_pack.py
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
for row in rows:
    name, college, city = row
    if city == wanted_city:
        students.append({"student_name": name, "inter_college": college, "inter_city": city})

answer = {"count": len(students), "students": students}
print(json.dumps(answer))
