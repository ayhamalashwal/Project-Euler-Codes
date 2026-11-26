def polygonal_number(k: int, n: int):
    if k == 3:
        return n * (n + 1) // 2
    if k == 4:
        return n * n
    if k == 5:
        return n * (3 * n - 1) // 2
    if k == 6:
        return n * (2 * n - 1)
    if k == 7:
        return n * (5 * n - 3) // 2
    if k == 8:
        return n * (3 * n - 2)
    raise ValueError(f"Unsupported polygon sides: {k}")
def generate_four_digit_figurates() -> dict[int, list[int]]:
    figurates: dict[int, list[int]] = {k: [] for k in range(3, 9)}
    for k in range(3, 9):
        n = 1
        while True:
            val = polygonal_number(k, n)
            if val > 9999:
                break
            if val >= 1000 and (val % 100) >= 10:
                figurates[k].append(val)
            n += 1
    return figurates
def find_cyclical_figurate_sum():
    figurates = generate_four_digit_figurates()
    by_prefix: dict[tuple[int, int], list[int]] = {}
    for k, nums in figurates.items():
        for num in nums:
            prefix = num // 100
            by_prefix.setdefault((k, prefix), []).append(num)
    all_types = {3, 4, 5, 6, 7, 8}
    def backtrack(path: list[int], used_types: set[int]) -> list[int] | None:
        if len(path) == 6:
            if (path[-1] % 100) == (path[0] // 100):
                return path
            return None
        needed_prefix = path[-1] % 100
        for next_type in all_types - used_types:
            for candidate in by_prefix.get((next_type, needed_prefix), ())
                path.append(candidate)
                used_types.add(next_type)
                result = backtrack(path, used_types)
                if result is not None:
                    return result
                used_types.remove(next_type)
                path.pop()
        return None
    for start_num in figurates[8]:
        cycle = backtrack([start_num], {8})
        if cycle is not None:
            return sum(cycle)
    return None
print(find_cyclical_figurate_sum())
