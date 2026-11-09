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
            rem_d_str = str_d.replace(common, "", 1)
            if len(rem_n_str) == 1 and len(rem_d_str):
                rn = int(rem_n_str)
                rd = int(rem_d_str)
                    if rd != 0 and n * rd == d * rn:
                        total_product *= Fraction(n, d)
print(total_product.denominator)
