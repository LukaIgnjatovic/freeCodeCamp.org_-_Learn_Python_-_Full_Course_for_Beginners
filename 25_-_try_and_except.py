# "Try & Catch" blocks are defined by "try" and "except" keywords.
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input.")

# Broad "Try & Catch" block.
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input.")

# Depending on what happens, different "Except" block is activated.
try:
    # answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero.")
except ValueError:
    print("Invalid input.")

# Specific error that is thrown is printed.
try:
    # answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input.")
