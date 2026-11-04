ones = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [6,6,5,5,5,7,6,6]

sum_1_19 = 0
for i in ones:
    sum_1_19 += i

print(sum_1_19)

sum_21_29 = 0
for i in tens:
    for j in ones[:9]:
        sum_21_29 += i + j
        
print(sum_21_29)

sum_tens = 0
for i in tens:
    sum_tens += i
print(sum_tens)

#hundreds:
sum_hundreds = 0
for i in ones[:9]:
    sum_hundreds += i + 7
print(sum_hundreds)

#hundreds and
sum_hundreds_and_1_19 = 0
for i in ones[:9]:
    for j in ones:
        sum_hundreds_and_1_19 += i + 10 + j
print(sum_hundreds_and_1_19)

sum_hundreds_and_21_29 = 0
for i in ones[:9]:
    for j in tens:
        for k in ones[:9]:
            sum_hundreds_and_21_29 += i + 10 + j + k
print(sum_hundreds_and_21_29)

sum_hundreds_and_tens = 0
for i in ones[:9]:
    for j in tens:
        sum_hundreds_and_tens += i + 10 + j
print(sum_hundreds_and_tens)

#thousand
sum_thousand = 11
print(sum_thousand)

print(sum_1_19 + sum_21_29 + sum_tens + sum_hundreds + sum_hundreds_and_1_19 + sum_hundreds_and_21_29 + sum_hundreds_and_tens + sum_thousand)

    

