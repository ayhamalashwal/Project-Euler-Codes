from itertools import permutations
total_sum = 0
for p in permutations("0123456789"):
    if p[1:4] % 2 != 0: continue
    if p[2:5] % 3 != 0: continue
    if p[3:6] % 5 != 0: continue


