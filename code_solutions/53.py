import math
def count(max_n: int = 100, threshold: int = 1000000):
    total = 0
    for n in range(1, max_n + 1):
        first_r = None
        for r in range(0, n + 1):
            if math.comb(n, r) > threshold:
                first_r = r
                break
        if first_r is not None:
            last_r = n - first_r
            total += last_r - first_r + 1
    return total
print(count(100, 1000000)
