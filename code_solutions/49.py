from collections import defaultdict
anagram = defaultdict(list)
LIMIT = 10000
is_prime = [True] * LIMIT
is_prime[0] = is_prime[1] = False
for i in range(2, int(LIMIT**0.5) + 1):
    if is_prime[i]:
        for j in range(i, LIMIT, i):
            is_prime[j] = False
for n in range(1000, LIMIT):
    if is_prime[n]:
        signature = "".join(sorted(str(n)))
        anagram[signature].append(n)
for signature, primes in anagram.items():
    if len(primes) >= 3:
        n = len(primes)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = primes[i], primes[j], primes[k]
                    if b - a == c - b:
                        if a != 1487:
                            print(f"

