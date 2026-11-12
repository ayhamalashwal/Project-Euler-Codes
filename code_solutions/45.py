import math

def is_pentagonal(n):
    if n <= 0:
        return False
    discriminant = 1 + 24 * n
    root = math.isqrt(discriminant)
    if root * root != discriminant:
        return False
    return (1 + root) % 6 == 0
def solve():
    n = 143
    while True:
        n += 1
        H = n * (2 * n - 1)
        if is_pentagonal(H):
            print(H)
