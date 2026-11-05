def abundant(n):
    sum = 0
    if n < 12:
        return False
    div_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            div_sum += i
            d2 = n // i
            if d2 != i:
                div_sum += i
    return div_sum > n

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
for i in range(28124, 0, -1):
    can_be_written = False
    for j in range(i, 1, -1):
        if abundant(j) and abundant(i - j):
            can_be_written = True
            break
    if can_be_written:
        sum_abundant += i
print(sum_abundant)

        

