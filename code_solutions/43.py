from itertools import permutations
total_sum = 0
for p in permutations("0123456789"):
    s = "".join(p)
    if int(s[1:4]) % 2 != 0: continue
    if int(s[2:5]) % 3 != 0: continue
    if int(p[3:6]) % 5 != 0: continue
    if int(p[4:7]) % 7 != 0: continue
    if int(p[5:8]) % 11 != 0: continue
    if int(p[6:9]) % 13 != 0: continue
    if int(p[7:10]) % 17 != 0: continue
    total_sum += p
print(total_sum)


