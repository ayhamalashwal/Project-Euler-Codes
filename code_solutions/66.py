import math
def minimal_x(D: int):
    a0 = math.isqrt(D)
    if a0 * a0 == D:
        return None
    if a0 * a0 - D == 1:
        return a0
    m = 0
    d = 1
    a = a0
    p_prev2, p_prev1 = 1, a0
    q_prev2, q_prev1 = 0, 1
    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2

        if p * p - D * q * q == 1:
            return p
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
def solve_pell(limit: int = 1000):
    max_x = -1
    best_d = -1
    for D in range(2, limit + 1):
        x = minimal_x(D)
        if x is not None and x > max_x:
            max_x = x
            best_d = D
    return best_d, max_x
d_result, x_result = solve_pell(1000)
print(d_result)
print(len(str(x_result)))

