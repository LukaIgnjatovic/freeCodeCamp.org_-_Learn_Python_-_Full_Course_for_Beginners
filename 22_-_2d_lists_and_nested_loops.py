# 2D lists are defined by using consecutive "[]" brackets.
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# This piece of code will print the element in the third row and second column.
print(number_grid[2][1])

# Nested loops can loop through a 2D list.
for row in number_grid:
    for column in row:
        print(column)

# The looping can be done with a condition.
for row in number_grid:
    for column in row:
        if column % 2 == 0:
            print(column)
