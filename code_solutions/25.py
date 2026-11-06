Fn1 = 1
Fn2 = 1
index = 2
def digits(n):
    return len(str(n))
while True:
    Fn = Fn1 + Fn2
    Fn2 = Fn1
    Fn1 = Fn
    index += 1
    if digits(Fn) == 1000:
        break

print(index)

