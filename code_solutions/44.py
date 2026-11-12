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

