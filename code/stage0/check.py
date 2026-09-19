#!/usr/bin/env python3
"""Stage 0 self-check. Runs each example program and compares its output with the
expected output written in its header comment.
    python3 check.py
Nothing to write in Stage 0: this only confirms python3 runs the seven files on your machine.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

passed = 0
failed = 0


def report(ok, what, expected=None, got=None):
    global passed, failed
    if ok:
        passed += 1
        print(f"PASS: {what}")
    else:
        failed += 1
        if expected is None:
            print(f"FAIL: {what}")
        else:
            print(f"FAIL: {what} — expected {expected!r}, got {got!r}")


def run(name, *args):
    p = subprocess.run([sys.executable, os.path.join(HERE, name), *args], capture_output=True, text=True, cwd=HERE)
    if p.returncode != 0:
        err = p.stderr.strip().splitlines()
        return None, err[-1] if err else "exited with an error"
    return p.stdout, None


def expect_exact(name, expected, *args):
    out, err = run(name, *args)
    label = name if not args else f"{name} {' '.join(args)}"
    if err is not None:
        report(False, f"{label} runs", "no error", err)
        return
    exp_lines = expected.strip("\n").splitlines()
    got_lines = out.strip("\n").splitlines()
    if got_lines == exp_lines:
        report(True, f"{label} prints the expected output")
    else:
        for i, e in enumerate(exp_lines):
            g = got_lines[i] if i < len(got_lines) else "<missing line>"
            if g != e:
                report(False, f"{label} line {i + 1}", e, g)
                return
        report(False, f"{label} prints the expected output", f"{len(exp_lines)} lines", f"{len(got_lines)} lines")


expect_exact("01_hello.py", """
My name is Ravi Teja Kanchi
I studied at Sri Chaitanya Junior College, Visakhapatnam
""")

expect_exact("02_rows.py", """
Ravi Teja Kanchi - Visakhapatnam
Lakshmi Prasanna Gudla - Vijayawada
Sai Kiran Bommu - Visakhapatnam
Divya Sree Pothula - Vijayawada
4 rows
""")

expect_exact("03_dicts.py", """
Ravi Teja Kanchi
None
[{"student_name": "Ravi Teja Kanchi", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}, {"student_name": "Lakshmi Prasanna Gudla", "inter_college": "Narayana Junior College", "inter_city": "Vijayawada"}, {"student_name": "Sai Kiran Bommu", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}]
""")

expect_exact("04_prime_even.py", """
18
2 prime=True even=True
4 prime=False even=True
17 prime=True even=False
18 prime=False even=True
1 prime=False even=False
""")

expect_exact("05_greet.py", "Namasthey Ravi\n", "Ravi")
expect_exact("05_greet.py", "usage: python3 05_greet.py <name>\n")

report(os.path.exists(os.path.join(HERE, "06_read_only.py")), "06_read_only.py is present (read it; it is not run)")

expect_exact("07_filter_pack.py", """
{"count": 2, "students": [{"student_name": "Ravi Teja Kanchi", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}, {"student_name": "Sai Kiran Bommu", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}]}
""")

print()
print(f"{passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
