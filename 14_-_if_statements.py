# "if" keyword is followed by one or more logical conditions.
# "else" keyword executes if the condition in "if" statement is not satisfied.
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are neither male nor tall.")

# If multiple logical conditions are chained together, they have to be separated by "and" or "or" keywords.
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are neither male nor tall.")

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You are either not male or not tall or both.")

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You are either not male or not tall or both.")

# If the "if" condition is not met, "elif" statements can be used to further branch the block of code.
# "else" statement always comes at the end of the block.
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are not a male, but are tall.")
else:
    print("You are either not male or not tall or both.")
