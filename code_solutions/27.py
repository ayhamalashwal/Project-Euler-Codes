def prime(b):
    if b <= 1:
        return False
    for i in range(2, int(b**0.5) + 1):
        if b % i == 0:
            return False
    return True
max_a = 0
max_b = 0
longest = 0
for b in range(1001):
    if prime(b):
        for a in range(-999, 1000):
            n = 0
            while prime(n**2 + a*n + b):
                n += 1
            if n > longest:
                longest = n
                max_a = a
                max_b = b
                print("new record")
print("done")
print(max_a * max_b)

        


                                                                                               
