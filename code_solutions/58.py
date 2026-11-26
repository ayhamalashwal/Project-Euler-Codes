def is_prime(n: int):
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    bases = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for a in bases:
        if a >= n:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def spiral_prime_side_length(target_ratio: float = 0.10):
    side = 1
    prime_count = 0
    total_diagonals = 1
    while True:
        side += 2
        total_diagonals += 4
        step = side - 1
        sq = side * side
        for corner in (sq - step, sq - 2 * step, sq - 3 * step):
            if is_prime(corner):
                prime_count += 1
        if prime_count / total_diagonals < target_ratio:
            return side
print(sprial_prime_side_length(0.1))
