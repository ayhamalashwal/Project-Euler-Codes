def digital_sum(n: int):
    return sum(int(ch) for ch in str(n))
def max_powerful_digit_sum(limit: int = 100):
    best_sum = 0
    for a in range(1, limit):
        for b in range(1, limit):
            value = a ** b
            num_digits = len(str(value))
            if 9 * num_digits <= best_sum:
                continue
            current_sum = digital_sum(value)
            if current_sum > best_sum:
                best_sum = current_sum
    return best_sum
print(max_powerful_digit_sum(100))
