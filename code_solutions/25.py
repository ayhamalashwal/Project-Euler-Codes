Fn1 = 1
Fn2 = 1
result = []
index = 2
def digits(n):
    return len(str(n))
while True:
    Fn = Fn1 + Fn2
    Fn1 = Fn
    Fn2 = Fn1
    index += 1
    if digits(Fn) == 1000:
        break

print(index)

