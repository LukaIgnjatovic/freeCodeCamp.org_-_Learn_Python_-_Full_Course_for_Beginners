# "open" function can be used to open external files; "r" argument means that file is only read.
employee_file = open("employees.txt", "r")

# Additional arguments that are used in "open" functions are:
# 1) "w" to write in the file,
# 2) "a" to append data to the end of the file,
# 3) "r+" to read and write.

# "readable" function checks if the file loaded is readable.
print(employee_file.readable())

# "read" function prints the information in the file.
employee_file = open("employees.txt", "r")
print(employee_file.read())

# "close" function is used to close the file.
employee_file.close()

# "readline" function prints the lines in the file one by one.
employee_file = open("employees.txt", "r")
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())

# "readlines" function stores the lines in the file in a list.
employee_file = open("employees.txt", "r")
print(employee_file.readlines())

# Individual lines in the file that are stored in a list can be indexed.
employee_file = open("employees.txt", "r")
print(employee_file.readlines()[1])

# "for" loop can be use to loop through the lines in the file.
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
