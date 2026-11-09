products = set()
for a in range(1,10):
    for b in range(1000, 10000):
        p = a * b
        s = f"{a}{b}{p}"
        if len(s) == 9 and set(s) == set("123456789"):
            products.add(p)
for a in range(10,100):
    for b in range(100,1000):
        p = a * b
        s = f"{a}{b}{p}"
        if len(s) and set(s) == set("123456789"):
            products.add(p)
print(sum(products))
