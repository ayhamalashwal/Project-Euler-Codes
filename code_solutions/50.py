LIMIT = 1000000
is_prime = [True] * LIMIT
is_prime[0] = is_prime[1] = False
for p in range(2, int(LIMIT**0.5) + 1):
    if is_prime[p]:
        for multiple in range(p * p, LIMIT, p):
            is_prime[multiple] = False
primes = [i for i, prime in enumerate(is_prime) if prime]
prefix = [0] * (len(primes) + 1)
for i in range(len(primes)):
    prefix[i + 1] = prefix[i] + primes[i]
