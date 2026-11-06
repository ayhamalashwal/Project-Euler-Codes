total_sum = 1
for s in range(2, 1002, 2):
    step = s - 1
    top_right = s**2
    top_left = s**2 - step
    bottom_left = s**2 - 2 * step
    bottom_right = s**2 - 3 * step
    total_sum += top_right + top+left + bottom_left + bottom_right
print(total_sum)
