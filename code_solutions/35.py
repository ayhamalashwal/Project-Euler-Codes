LIMIT = 1000000
prime = [True] * LIMIT 
prime[0] = prime[1] = False
for i in range(2, int(LIMIT**0.5) + 1):
    if prime[i]:
        for j in range(i * i, LIMIT, i):
            prime[j] = FALSE
count = 0
for n in range(2, LIMIT):
    if not prime[n]:
        continue
    s = str(n)
    if len(s) > 1 and any(digit in '024568' for digit in s):
        continue
    if all(prime[s[i:] + s[:i]] for i in range(len(s))):
        counter += 1
print(counter)

