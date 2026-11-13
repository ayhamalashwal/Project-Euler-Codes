LIMIT = 200000
factor_count = [0] * LIMIT

for i in range(2, LIMIT):
    if factor_count[i] == 0:
        for j in range(i, LIMIT, i):
            factor_count[j] += 1
consecutive = 0
for n in range(2, LIMIT):
    if factor_count[n] == 4:
        consecutive += 1
        if consecutive == 4:
            print(f"{n - 3}")
    else:
        consecutive = 0
