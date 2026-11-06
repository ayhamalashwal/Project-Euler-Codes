import math
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
n = 999999

for i in range(9, -1, -1):
    fact = math.factorial(i)
    index = n // fact
    n %= fact
    result.append(digits.pop(index))
print(result)
