# Define two new list.
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# "extend" function extends the original list with the one used as argument.
friends.extend(lucky_numbers)
print(friends)

# "append" function appends a new element to the end of the list.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)

# "insert" function inserts a new element at the place given by the first argument.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

# "remove" function removes an element given by the argument.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)

# "clear" function empties the list.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)

# "pop" function removes the last element of the list.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()

print(friends)

# "index" function return the index of the element given by the argument.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends.index("Oscar"))

# "count" function returns the number of times the element given by the argument appears in the list.
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends.count("Jim"))

# "sort" function sorts all the items in the list in alphabetical order.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()

print(friends)

# "reverse" function sorts all the items in the list in reverse alphabetical order.
lucky_numbers.reverse()

print(lucky_numbers)

# "copy" function copies the whole list.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()

print(friends2)
