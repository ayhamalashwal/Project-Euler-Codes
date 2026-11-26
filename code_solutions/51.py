def sieve(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for num in range(2, (limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]
def build(pattern: str, prime_set: set[int]):
    family: list[int] = []
    start = pattern[0] == "*"
    for digit in "0123456789":
        if digit == "0" and start:
            continue
        candidate = int(pattern.replace("*", digit))
        if candidate in prime_set:
            family.append(candidate)
    return family
def find_smallest(target_size: int, limit: int = 1000000):
    primes = sieve(limit)
    prime_set = set(primes)
    checked_patterns: set[str] = set()
    for prime in primes:
        s = str(prime)
        for digit in set(s):
            if s.count(digit) < 3:
                continue
            pattern = s.replace(digit, "*")
            if pattern in checked_patterns:
                continue
            checked_patterns.add(pattern)
            family = build(pattern, prime_set)
            if len(family) == target_size and prime in family:
                return prime
print(find_smallest(8))
