# Input from a user is stored as a string by default.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)

# If the input is valid, "float" function can turn the input string into float and then perform the desired operation.
result = float(num1) + float(num2)

print(result)
