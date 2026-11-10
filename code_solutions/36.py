def palindrome():
    total_sum = 0
    for i in range(1, 10):
        if i % 2 != 0:
            b = bin(i)[2:]
            if b == b[::-1]:
                total_sum += i
    for root in range(1, 1000):
        s = str(root)
        rev = s[::-1]
        p_even = int(s + rev)
        if p_even < 1000000 and p_even % 2 != 0:
            b = bin(p_even)[2:]
            if b == b[::-1]:
                total_sum += p_even
        p_odd = int(s + rev[1:])
        if p_odd < 1000000 and p_odd % 2 != 0:
            b = bin(p_odd)[2:]
            if b == b[::-1]:
                total_sum += p_odd
    print(total_sum)
palindrome()

