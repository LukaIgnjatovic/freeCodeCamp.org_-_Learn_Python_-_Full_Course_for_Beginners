# Functions are defined by using the "def" keyword.
def say_hi(name, age):
    print("Hello " + name + ", your age is " + age + "!")


say_hi("Mike", "35")


# Functions like "say_hi" can even receive an integer if it is properly converted.
def say_hi(name, age):
    print("Hello " + name + ", your age is " + str(age) + "!")


say_hi("Steve", 70)
