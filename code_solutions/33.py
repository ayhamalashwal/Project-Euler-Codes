from fractions import Fraction
total_product = Fraction(1, 1)
for n in range(10, 100):
    for d in range(n + 1, 100):
        str_n = str(n)
        str_d = str(d)
        if n % 10 == 0 and d % 10 == 0:
            continue
        common_digits = set(str_n).intersection(set(str_d))
        for common in common_digits:
            if common == '0':
                continue
            rem_n_str = str_n.replace(common, "", 1)
