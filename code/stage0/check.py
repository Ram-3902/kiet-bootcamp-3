#!/usr/bin/env python3
"""Stage 0 self-check. Runs each exercise and compares its output.
    python3 check.py              checks the files in this folder
    python3 check.py solution     checks the solution folder (should be all PASS)
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = HERE
if len(sys.argv) > 1 and sys.argv[1] == "solution":
    FOLDER = os.path.join(HERE, "solution")

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
    path = os.path.join(FOLDER, name)
    p = subprocess.run([sys.executable, path, *args], capture_output=True, text=True, cwd=FOLDER)
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
    elif not got_lines:
        report(False, f"{label} prints the expected output", exp_lines[0] + " ...", "nothing")
    else:
        for i, e in enumerate(exp_lines):
            g = got_lines[i] if i < len(got_lines) else "<missing line>"
            if g != e:
                report(False, f"{label} line {i + 1}", e, g)
                return
        report(False, f"{label} prints the expected output", f"{len(exp_lines)} lines", f"{len(got_lines)} lines")


# 01: any name is fine, the shape must match
out, err = run("01_hello.py")
if err is not None:
    report(False, "01_hello.py runs", "no error", err)
else:
    lines = out.strip("\n").splitlines()
    ok = (len(lines) == 2 and lines[0].startswith("My name is ") and len(lines[0]) > len("My name is ")
          and lines[1].startswith("I studied at ") and ", " in lines[1])
    report(ok, "01_hello.py prints 'My name is ...' and 'I studied at ..., ...'",
           "2 lines with those shapes", lines if lines else "nothing")

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

# 06 is read-only: just make sure the answers were written
text = open(os.path.join(FOLDER, "06_read_only.py"), encoding="utf-8").read()
todo_left = sum(1 for line in text.splitlines() if line.startswith("# A") and line.rstrip().endswith("TODO"))
report(todo_left == 0, "06_read_only.py has all four answers filled in", "0 TODO answers", f"{todo_left} TODO answers")

expect_exact("07_filter_pack.py", """
{"count": 2, "students": [{"student_name": "Ravi Teja Kanchi", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}, {"student_name": "Sai Kiran Bommu", "inter_college": "Sri Chaitanya Junior College", "inter_city": "Visakhapatnam"}]}
""")

print()
print(f"{passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
