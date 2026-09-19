# 05_greet.py — Block 5: import, sys.argv.
#
#   python3 05_greet.py Ravi
#   python3 05_greet.py
#
# import brings in a module: something from the standard library (sys, sqlite3, json)
# or a file sitting next to yours (from bottle import route, run — Stage 3).
# sys.argv is the C argv: a list of strings, sys.argv[0] is the file name.
#
# Goal: greet the name given on the command line; print a usage line if there is none.
# Expected output:
#   $ python3 05_greet.py Ravi
#   Namasthey Ravi
#   $ python3 05_greet.py
#   usage: python3 05_greet.py <name>

import sys

# TODO: if len(sys.argv) < 2, print the usage line. Otherwise print f"Namasthey {sys.argv[1]}".
