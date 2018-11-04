# If a new employee joins the company, his name should be appended to the file.
# "a" argument is used in the "open" function.
# employee_file = open("employees.txt", "a") - This line is commented out to save the integrity of the original "employees.txt" file.

# "write" function writes the string to the external file.
# employee_file.write("Toby - Human Resources") - This line is commented out to save the integrity of the original "employees.txt" file.

# "\n" is used to add the next employee to the next line.
# employee_file.write("\nKelly - Customer Service") - This line is commented out to save the integrity of the original "employees.txt" file.

# If "w" argument is used in the "open" function, everything added through Python will replace the original content in "employees.txt" file.
# employee_file = open("employees.txt", "w") - This line is commented out to save the integrity of the original "employees.txt" file.

# New "employee.txt" file will have only "Kelly - Customer Service" line when this line is executed.
# employee_file.write("\nKelly - Customer Service") - This line is commented out to save the integrity of the original "employees.txt" file.

# HTML files can be written from Python as well.
html_file = open("index.html", "w")

# HTML code for a paragraph is written inside the "index.html" file.
html_file.write("<p>This is HTML.</p>")

# "close" function is used to close the file.
html_file.close()
