# "Student" class is import from "Student" file.
from student import Student

# "student1" and "student2" are created.
student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

# Function "on_honor_roll" can be called on created "Student" objects.
print(student1.on_honor_roll)
print(student2.on_honor_roll)
