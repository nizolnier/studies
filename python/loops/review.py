single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = []

for temp in single_digits:
    squares.append(temp*temp)
    print(temp)

print(squares)

cubes = [temp ** 3 for temp in single_digits]

print(cubes)