# Statements are printed one by one, but changing the character's name or age can be tedious.
print("There once was a man named John, ")
print("he was 70 years old, ")
print("He really liked the name John, ")
print("but didn't like being 70.")

# Character's name and age can be stored in variables, so that changes can be executed at once.
character_name = "Toby"
character_age = "35"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old, ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

# The variable can be changed mid-execution.
character_name = "Tom"
character_age = "50"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old, ")

character_name = "Mike"

print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
