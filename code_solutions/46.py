import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2):
            return False
        i += 6
    return True
def goldbach():
    n = 9
    while True:
        if not is_prime(n):
            found = False
            s = 1
            while 2 * (s * s) < n:
                remainder = n - 2 * (s * s)
                if is_prime(remainder):
                    found = True
                    break
                s += 1
            if not found:
                return n
        n += 2
print(goldbach())
