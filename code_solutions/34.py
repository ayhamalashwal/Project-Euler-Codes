import math
factorials = [math.factorial(i) for i in range(10)]
curious = []
for n in range(10, 7 * math.factorial(9) + 1):
    factorial_sum = sum(factorials[int(digit)] for digit in str(n))
    if factorial_sum == n:
        curious.append(n)
print
