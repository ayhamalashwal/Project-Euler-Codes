n1 = 999
n2 = 999

def palindrome_product():
    max = 0
    for i in range(n1, 99, -1):
        for j in range (i, 99, -1):
            n3 = i * j
            if str(n3) == str(n3)[::-1]:
                if n3 > max:
                    max = n3
    return max
print(palindrome_product())


