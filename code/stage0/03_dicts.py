# 03_dicts.py — Block 3: dicts, d["key"], d.get("key"), json.dumps.
#
#   python3 03_dicts.py
#
# A dict is { "key": value, ... } — a struct whose field names are strings.
# A dict IS JSON, near enough: json.dumps(d) prints it as JSON text.
# In Stage 4 you will return a dict from a route and Bottle sends it as JSON.
#
# Goal: turn the list of tuples into a list of dicts with the three keys of the students table,
#       show d["key"] and d.get("missing key"), then print the whole list as JSON.
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
# TODO: for each row, unpack it and append a dict:
#       {"student_name": name, "inter_college": college, "inter_city": city}

# TODO: first = result[0]
# TODO: print first["student_name"]
# TODO: print first.get("phone")      — a key that is not there: .get gives None, no crash

# TODO: print json.dumps(result)
