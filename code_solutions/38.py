def pandigital(n):
    return len(n) == 9 and set(n) == set("123456789")
max = 0
for i in range(1, 10000):
    concatenated = ""
    n = 1
    while len(concatenated) < 9:
        concatenated += str(i * n)
        n += 1
    if pandigital(concatenated):
        val = int(concatenated)
        if val > max:
            max = val
print(max)
