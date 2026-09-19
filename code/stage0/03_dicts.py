# 03_dicts.py — Block 3: dicts, d["key"], d.get("key"), json.dumps.
#
#   python3 03_dicts.py
#
# Expected output:
#   Ravi Teja Kanchi
#   None
#   [{"student_name": "Ravi Teja Kanchi", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}, {"student_name": "Lakshmi Prasanna Gudla", "inter_college": "Narayana Junior College", "inter_city": "Vijayawada"}, {"student_name": "Sai Kiran Bommu", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}]

import json

rows = [
    ("Ravi Teja Kanchi", "Sri Chaitanya Junior College", "Visakhapatnam"),
    ("Lakshmi Prasanna Gudla", "Narayana Junior College", "Vijayawada"),
    ("Sai Kiran Bommu", "Sri Chaitanya Junior College", "Visakhapatnam"),
]

result = []
for row in rows:
    name, college, city = row
    result.append({"student_name": name, "inter_college": college, "inter_city": city})

first = result[0]
print(first["student_name"])
print(first.get("phone"))

print(json.dumps(result))
