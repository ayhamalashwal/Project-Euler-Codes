def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count

triangle_num = 0
n = 1

while True:
    triangle_num += n
    if count_divisors(triangle_num) > 500:
        print(f"{triangle_num}")
        break
    n += 1
