# User-defined data types can be defined through classes.
class Student:
    def __init__(self, name, major, gpa):
        self.name = name  # Name of the "Student" object is going to be equal to the "name" variable.
        self.major = major  # Major of the "Student" object is going to be equal to the "major" variable.
        self.gpa = gpa  # GPA of the "Student" object is going to be equal to the "gpa" variable.

# Functions for classes can be defined inside the classes.
    @property
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
