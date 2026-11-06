matching = []
for num in range(2, 355000):
    digit_power_sum = sum(int(digit)**5 for digit in str(num))
    if digit_power_sum == num:
        matching.append(num)
print(sum(matching))
