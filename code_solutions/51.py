def sieve(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for num in range(2, (limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]
def build
