def cycle(n):
    remainder = 1
    seen {}
    position = 0

    while remainder != 0:
        if remainder in seen:
            return position - seen[remainder]
        seen[remainder] = position
        remainder = (remainder * 10) % n
        position += 1
    return 0
max = 0
best_n = 0
