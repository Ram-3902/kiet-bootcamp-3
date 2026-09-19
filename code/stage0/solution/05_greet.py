# 05_greet.py — Block 5 (solution): import, sys.argv.
#
#   python3 05_greet.py Ravi
#   python3 05_greet.py
#
# Expected output:
#   $ python3 05_greet.py Ravi
#   Namasthey Ravi
#   $ python3 05_greet.py
#   usage: python3 05_greet.py <name>

import sys

if len(sys.argv) < 2:
    print("usage: python3 05_greet.py <name>")
else:
    print(f"Namasthey {sys.argv[1]}")
