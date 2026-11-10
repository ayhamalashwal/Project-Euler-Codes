def palindrome():
    palindrome = set()
    for root in range(1, 1000):
        s = str(root)
        rev = s[::-1]
        p_even = int(s + rev)
        if p_even < 1000000:
            palindrome.add(p_even)
        p_odd = int(s + rev[1:])
        if p_odd < 1000000:
            palindrome.add(p_odd)
    total_sum = 0
    for i in palindrome:
        b = bin(i)[2:]
        if i % 2 != 0:
            if b == b[::-1]:
                total_sum += i
    print(total_sum)
palindrome()
