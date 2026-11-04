LIMIT = 2_000_000


is_prime = [True] * LIMIT
is_prime[0] = is_prime[1] = False  


for p in range(2, int(LIMIT**0.5) + 1):
    if is_prime[p]:
        for multiple in range(p * p, LIMIT, p):
            is_prime[multiple] = False

prime_sum = sum(i for i, prime in enumerate(is_prime) if prime)

print(prime_sum)
