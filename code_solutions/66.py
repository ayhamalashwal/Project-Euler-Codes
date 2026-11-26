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

        if p + p - D * q * q == 1:
            return p
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
def solve_pell(limit: int = 1000)
