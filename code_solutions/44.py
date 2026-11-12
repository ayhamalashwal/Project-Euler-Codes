import math

def is_pentagonal(n):
    if n <= 0:
        return False
    discriminant = 1 + 24 * n
    root = math.isqrt(discriminant)
    if root * root != discriminant:
        return False
    return (1 + root) % 6 == 0
def get_pentagonal(n):
    return n * (3 * n - 1) // 2
def solve():
    i = 1
    while True:
        i += 1
        Pk = get_pentagonal(n)
        for j in range

