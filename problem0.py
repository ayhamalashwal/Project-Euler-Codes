n = 282500
total = 0
for i in range(1, n + 1):
    sum = (2 * i - 1)**2
    total = sum + total
print(total)
