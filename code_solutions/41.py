from itertools import permutations
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
digits = "7654321"
for p in permutations(digits):
    val = int("".join(p))
    if is_prime(val):
        print(val)
        break
