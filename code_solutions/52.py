def same_digits(a: int, b: int):
    return sorted(str(a)) == sorted(str(b))
def smallest(max: int = 6):
    digits = 1
    while True:
        low = 10 ** (digits - 1)
        high = (10 ** digits - 1) // max
        for x in range(low, high + 1):
            if x % 9 != 0:
                continue
            target = sorted(str(x))
            if all(
                sorted(str(m * x)) == target
                for m in range(2, max + 1)
            ):
                return x
        digits += 1
print(smallest(6))
