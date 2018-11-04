# "for" loops are useful in looping through a given object.
for letter in "Giraffe Academy":
    print(letter)

# The naming of the variable by which the loop is performed provisional.
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

# "range" function is especially useful in "for" loops.
for index in range(10):
    print(index)
for index in range(3, 10):
    print(index)

# "len" function can be used to loop by the number of elements in the object.
for index in range(len(friends)):
    print(index)
for index in range(len(friends)):
    print(friends[index])

# "for" loops can be combined with "if" statements.
for index in range(5):
    if index == 0:
        print("First iteration.")
    else:
        print("Not first.")
