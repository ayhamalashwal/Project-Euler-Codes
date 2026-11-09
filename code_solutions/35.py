LIMIT = 1000000
prime = [TRUE] * LIMIT 
prime[0] = prime[1] = FAlSE
for i in range(2, int(LIMIT**0.5) + 1)
    if prime[i]:
        for j in range(i * i, LIMIT, i):
            prime[j] = FALSE

