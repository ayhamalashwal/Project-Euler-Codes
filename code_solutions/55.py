def reverse_int(n: int):
    return int(str(n)[::-1])
def is_palindrome(n: int):
    s = str(n)
    return s == s[::-1]
def is_lychrel(n: int, max_iterations: int = 49) -> bool:
    current = n
    for _ in range(max_iterations):
        current += reverse_int(current)
        if is_palindrome(current):
            return False
    return True
def count_lychrel_below(limit: int = 10_000):
    return sum(1 for n in range(1, limit) if is_lychrel(n))
print(count_lychrel_below(10000))
