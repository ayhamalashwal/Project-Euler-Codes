LIMIT = 28124
abundant_nums = []
for n in range(12, LIMIT):
    div_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            div_sum += i
            d2 = n // i
            if d2 != i:
                div_sum += d2
    if div_sum > n:
        abundant_nums.append(n)

can_be_written = [False] * LIMIT

for i in range(len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        s = abundant_nums[i] + abundant_nums[j]
        if s < LIMIT:
            can_be_written[s] = True
        else:
            break
total_sum = sum(i for i in range(LIMIT) if not can_be_written[i])
print(total_sum)
        

