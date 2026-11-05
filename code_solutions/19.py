sunday_count = 0
current_day = 1

for year in range(1901, 2001):
    for month in range(12):
        if current_day == 6:
            sunday_count += 1
        if month == 1:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                shift = 1
            else:
                shift = 0
        elif month in [3, 5, 8, 10]:
            shift = 2
        else:
            shift = 3
        current_day = (current_day + shift) % 7
print(sunday_count)
