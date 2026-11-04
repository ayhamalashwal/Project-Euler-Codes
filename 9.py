import math

for c in range(334, 500):
    delta = c**2 + 2000*c - 1000000
    if delta >= 0:
        root = math.isqrt(delta)
        if root * root == delta:
            print(f"{1000 * c * (500 - c)}")
            break
