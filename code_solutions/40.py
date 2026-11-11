s = ""
i += 1
while len(s) <= 1000000:
    s += str(i)
    i += 1
d1 = int(s[1 - 1])
d10 = int(s[10 - 1])
d100 = int(s[100 - 1])
d1000 = int(s[1000 - 1])
d10000 = int(s[10000 - 1])
d1000000 = int(s[1000000 - 1])
result = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
print(result)
