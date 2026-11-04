def divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            partner = n // i
            if partner != i and partner != n:
                total += partner
    return total

amicable_sum = 0
checked = set()
for a in range(1, 10000):
    if a in checked:
        continue
    b = divisors(a)

    if b != a and divisors(b) == a and b < 10000:
        amicable_sum += a + b
        checked.add(b)

print(amicable_sum)
