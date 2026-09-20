#!/usr/bin/env python3
"""Is this machine ready for the bootcamp?  Run it after setup, and again on the day.
    python3 ~/kiet-bootcamp-3/check_env.py
Exit code 0 means everything that matters passed.
"""
import os
import shutil
import sqlite3
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
fatal_failed = False


def report(ok, what, detail="", fatal=True):
    global fatal_failed
    tag = "PASS" if ok else ("FAIL" if fatal else "WARN")
    if not ok and fatal:
        fatal_failed = True
    line = f"{tag}: {what}"
    if detail:
        line += f" — {detail}"
    print(line)


# 1. python3 version
v = sys.version_info
report(v >= (3, 12), f"python3 is {v.major}.{v.minor}.{v.micro}",
       "" if v >= (3, 12) else "need 3.12 or newer")

# 2. curl
report(shutil.which("curl") is not None, "curl is on PATH",
       "" if shutil.which("curl") else "install it: sudo apt install curl  (Ubuntu)  /  sudo pacman -S curl  (Arch)")

# 3. sqlite3 CLI (non-fatal)
report(shutil.which("sqlite3") is not None, "sqlite3 command-line tool is on PATH",
       "" if shutil.which("sqlite3") else "not found. You can use  python3 -m sqlite3 team_details.db  instead", fatal=False)

# 4. bottle.py imports from code/stage3
stage3 = os.path.join(HERE, "code", "stage3")
p = subprocess.run([sys.executable, "-c", "import bottle; print(bottle.__version__)"],
                   cwd=stage3, capture_output=True, text=True)
ok = p.returncode == 0
report(ok, "bottle.py imports from code/stage3", p.stdout.strip() if ok else p.stderr.strip().splitlines()[-1] if p.stderr.strip() else "failed")

# 5. sqlite3 module works
try:
    conn = sqlite3.connect(":memory:")
    one = conn.execute("SELECT 1").fetchone()[0]
    conn.close()
    report(one == 1, "Python's sqlite3 module works (SELECT 1)")
except Exception as e:  # noqa: BLE001
    report(False, "Python's sqlite3 module works (SELECT 1)", str(e))

# 6. data files present
for name in ("schema.sql", "sample_team_details.sql", "all_students.sql"):
    path = os.path.join(HERE, "data", name)
    report(os.path.exists(path), f"data/{name} is present", "" if os.path.exists(path) else "git pull in ~/kiet-bootcamp-3")

# 7. frontend present (warn only)
fe = os.path.join(HERE, "code", "frontend", "index.html")
report(os.path.exists(fe), "code/frontend/index.html is present (needed in Stage 7)",
       "" if os.path.exists(fe) else "git pull in ~/kiet-bootcamp-3", fatal=False)

# 8. bootcamp guide present
mat = os.path.join(HERE, "docs", "index.html")
report(os.path.exists(mat), "docs/index.html is present (the bootcamp guide)",
       "" if os.path.exists(mat) else "git pull in ~/kiet-bootcamp-3")

print()
if fatal_failed:
    print("Something above needs fixing before the bootcamp.")
    sys.exit(1)
print("Ready. Start the bootcamp guide with:")
print("    cd ~/kiet-bootcamp-3/docs && python3 -m http.server 8000")
print("then open http://localhost:8000 in your browser.")
