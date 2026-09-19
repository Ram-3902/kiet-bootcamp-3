# 04_prime_even.py — Block 4: def / return, if / elif / else, %, range, int().
#
#   python3 04_prime_even.py
#
# Expected output:
#   18
#   2 prime=True even=True
#   4 prime=False even=True
#   17 prime=True even=False
#   18 prime=False even=True
#   1 prime=False even=False


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def is_even(n):
    return n % 2 == 0


print(int("17") + 1)

for n in [2, 4, 17, 18, 1]:
    print(f"{n} prime={is_prime(n)} even={is_even(n)}")
