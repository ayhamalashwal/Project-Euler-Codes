max_solutions = 0
best_p = 0

for p in range(1, 1001):
    solutions = 0
    for a in range(1, p // 3):
        for b in range(1, (p - a) // 3):
            c = p - a - b
            if (a**2 + b**2) == c**2:
                solutions += 1
    if solutions > max_solutions:
        max_solutions = solutions


