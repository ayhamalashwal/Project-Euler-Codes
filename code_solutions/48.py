MOD = 10**10
total_sum = 0
for i in range(1, 1001):
    total_sum += pow(i, i, MOD)
last = total_sum % MOD
print(last)
