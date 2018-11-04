# Lists are created by using "[]" and inserting elements between these brackets.
coordinates = [4, 5]
coordinates[1] = 10

print(coordinates[1])

# Tuples are created by using "()" and inserting elements between these brackets.
coordinates = (4, 5)
# coordinates[1] = 10 - This line of code will throw an error - tuples are immutable.

print(coordinates[1])

# Tuples can be elements of a list.
coordinates = [(4, 5), (6, 7), (80, 34)]

print(coordinates[1])
