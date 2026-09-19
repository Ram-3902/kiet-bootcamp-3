# 04_prime_even.py — Block 4: def / return, if / elif / else, %, range, int().
#
#   python3 04_prime_even.py
#
# def starts a function. No prototype, no return type. return gives the value back.
# % is remainder, same as C.  int("17") turns text into a number, like atoi.
# range(2, n) counts 2, 3, ..., n-1 — the C for-loop with i++.
#
# Goal: fill in is_prime and is_even so the loop at the bottom prints:
# Expected output:
#   18
#   2 prime=True even=True
#   4 prime=False even=True
#   17 prime=True even=False
#   18 prime=False even=True
#   1 prime=False even=False


def is_prime(n):
    # TODO: less than 2 -> False. Otherwise, for d in range(2, n): if n % d == 0 -> False. Else True.
    return False


def is_even(n):
    # TODO: True when n % 2 == 0
    return False


print(int("17") + 1)

for n in [2, 4, 17, 18, 1]:
    print(f"{n} prime={is_prime(n)} even={is_even(n)}")
