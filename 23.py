def abundant(n):
    sum = 0
    checked = set()
    checked.add(n)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and n not in checked:
            sum += i
            checked.add(i)
    if sum > n:
        return True
    else:
        return False
sum_all = 0
sum_abundant = 0
for i in range(28124):
    sum_all += i
print(sum_all)
checked = set()
for i in range(1, 28124, -1):
    for j in range(1, i, -1):
        if abundant(j) and abundant(i - j) and i - j not in checked:
            sum += i
            checked.add(i - j)
            checked.add(j)
print(sum_abundant)

        

