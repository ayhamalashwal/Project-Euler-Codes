def sum_of_squares():
    initial = 1
    sum_of_squares = 0
    for _ in range(100):
        squared = initial**2
        sum_of_squares += squared
        initial += 1
    return sum_of_squares

def square_of_sums():
    initial = 1
    square_of_sums = 0
    for _ in range(100):
        square_of_sums += initial
        initial += 1
    return square_of_sums**2

print(sum_of_squares())
print(square_of_sums())
print(square_of_sums() - sum_of_squares())
