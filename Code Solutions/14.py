n = 1
biggest = 0
def sequence(n):
    chain = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            chain += 1
        else:
            n = 3 * n + 1
            chain += 1
    return chain
m = 999999
starting_number = 0
while m > 1:
    if sequence(m) > biggest:
        biggest = sequence(m)
        starting_number = m
    m -= 1
print(starting_number)

