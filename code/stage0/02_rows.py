# 02_rows.py — Block 2: lists, tuples, len, append, for, unpacking.
#
#   python3 02_rows.py
#
# A list is [ ... ]. A tuple is ( ... ). A list of tuples is exactly what
# SQLite gives back in Stage 2: fetchall() returns a list, one tuple per row.
#
# Goal: add one more row with .append, then loop over the rows and print "name - city",
#       then print how many rows there are.
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

# TODO: append the tuple ("Divya Sree Pothula", "Narayana Junior College", "Vijayawada") to rows

# TODO: for each row, unpack it into three names  (name, college, city = row)  and print f"{name} - {city}"

# TODO: print f"{len(rows)} rows"
