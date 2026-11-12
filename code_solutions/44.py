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
        Pi = get_pentagonal(i)
        for j in range(i - 1, 0, -1):
            Pj = get_pentagonal(j)
            diff = Pi - Pj
            if is_pentagonal(diff):
                sum_val = Pi + Pj
                if is_pentagonal(sum_val):
                    return diff
print(solve())


