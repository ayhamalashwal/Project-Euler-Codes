n = 100
number = 1

for i in range(100):
    number *= (n - i)
str_number = str(number)
sum = 0
for i in range(len(str_number)):
    sum += int(str_number[i])
print(sum)
