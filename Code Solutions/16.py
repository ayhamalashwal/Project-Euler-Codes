number = 2**1000
number_str = str(number)
total_sum = 0
for digits in number_str:
    total_sum += int(digits)

print(total_sum)
