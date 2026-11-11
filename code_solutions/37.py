def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(i**0.5) + 1):
        if n % i == 0:
            return False
    return True
def left_truncatable(n):
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True
queue = [2, 3, 5, 7]
truncatable_primes = []
while queue:
    curr = queue.pop(0)
