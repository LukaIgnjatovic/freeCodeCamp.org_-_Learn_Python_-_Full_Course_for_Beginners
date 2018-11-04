# Print a simple string.
print("Giraffe Academy")

# Print a string with two words which are separated by new line.
print("Giraffe \nAcademy")

# String can stored in a variable.
phrase = "Giraffe Academy"

# String can be concatenated inside the "print" function.
print(phrase + " is cool.")

# Every letter in the string is capitalized with the "upper" function.
print(phrase.upper())

# Different string functions can be chained together.
print(phrase.upper().isupper())

# "len" function returns the length of the string.
print(len(phrase))

# Letters from string can be printed using "[]" and their index.
print(phrase[0])

# "index" function returns the index number of the letter where it first encountered it.
print(phrase.index("G"))

# "index" function can even return the index number of the phrase where it first encountered it.
print(phrase.index("Acad"))

# "replace" function replace a portion of the string it matches.
print(phrase.replace("Giraffe", "Elephant"))
