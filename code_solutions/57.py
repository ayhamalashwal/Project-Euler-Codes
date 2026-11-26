def count(expansions: int = 1000):
    num = 3
    den = 2
    count = 0
    for _ in range(expansions):
        if len(str(num)) > len(str(den)):
            count += 1
        num, den = num + 2 * den, num + den
    return count
print(count(1000))
