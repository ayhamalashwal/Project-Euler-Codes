n = 600851475143
factor = 3

while factor**2 <= n:
    if n % factor == 0:
        n //= factor
    else:
        factor += 2

print(n)

