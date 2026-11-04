def is_prime(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

primes_found = 1
candidate = 3

while primes_found < 10001:
    if is_prime(candidate):
        primes_found += 1
        last_prime = candidate
    candidate += 2

print(last_prime)
