total = 0
e1 = 2
e2 = 8

while e1 <= 4000000:
    total += e1
    e1, e2 = e2, 4 * e2 + e1

print(total)
