from functools import lru_cache
def sieve_primes(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for m in range(i * i, limit + 1, i):
                is_prime[m] = False
    return [i for i, val in enumerate(is_prime) if val]
def is_prime_mr(n: int):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
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
@lru_cache(maxsize=None)
def pair_compatible(p: int, q: int) -> bool:
    return is_prime_mr(int(f"{p}{q}")) and is_prime_mr(int(f"{q}{p}"))
def lowest_prime_pair_set_sum(target_size: int = 5, prime_limit: int = 10_000) -> int | None:
    primes = sieve_primes(prime_limit)
    n_primes = len(primes)
    best_sum: int | None = None
    def search(start_idx: int, current_set: list[int], current_sum: int) -> None:
        nonlocal best_sum
        needed = target_size - len(current_set)
        if needed == 0:
            if best_sum is None or current_sum < best_sum:
                best_sum = current_sum
            return
        for idx in range(start_idx, n_primes):
            candidate = primes[idx]
            if best_sum is not None and current_sum + candidate * needed >= best_sum:
                break
            if all(pair_compatible(existing, candidate) for existing in current_set):
                current_set.append(candidate)
                search(idx + 1, current_set, current_sum + candidate)
                current_set.pop()
    search(0, [], 0)
    return best_sum
print(lowest_prime_pair_set_sum(5, 10000))
