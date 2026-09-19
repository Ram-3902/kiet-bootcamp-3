# 02_rows.py — Block 2: lists, tuples, len, append, for, unpacking.
#
#   python3 02_rows.py
#
# Expected output:
#   Ravi Teja Kanchi - Visakhapatnam
#   Lakshmi Prasanna Gudla - Vijayawada
#   Sai Kiran Bommu - Visakhapatnam
#   Divya Sree Pothula - Vijayawada
#   4 rows

rows = [
    ("Ravi Teja Kanchi", "Sri Chaitanya Junior College", "Visakhapatnam"),
    ("Lakshmi Prasanna Gudla", "Narayana Junior College", "Vijayawada"),
    ("Sai Kiran Bommu", "Sri Chaitanya Junior College", "Visakhapatnam"),
]

rows.append(("Divya Sree Pothula", "Narayana Junior College", "Vijayawada"))

for row in rows:
    name, college, city = row
    print(f"{name} - {city}")

print(f"{len(rows)} rows")
