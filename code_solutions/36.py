def palindrome():
    palindrome = set()
    for i in range(1, 10):
        palindrome.add(i)
    for root in range(10, 1000, 2):
        s = str(root)
        rev = s[::-1]
        p_even = int(s + rev)
        if p_even < 1000000:
            palindrome.add(root)
        p_odd = int(s + rev[1:])
        if p_odd < 1000000:
            palindrome.add(root)
    total_sum = 0
    for i in palindrome:
        b = bin(i)[2:]
        if b == b[::-1]:
            total_sum += i
    print(total_sum)
palindrome()
