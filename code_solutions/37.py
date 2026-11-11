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
    if curr > 10 and left_truncatable(curr):
        truncatable_primes.append(curr)
    for digit in [1, 3, 7, 9]:
        next_val = curr * 10 + digit
        if is_prime(next_val):
            queue.append(next_val)
print(sum(truncatable_primes))
