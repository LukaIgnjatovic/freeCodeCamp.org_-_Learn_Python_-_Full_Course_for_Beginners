# "Chef" class is import from "Chef" file.
from chef import Chef


# "ChineseChef" class inherits the "Chef" class.
class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken.")

    def make_fried_rice(self):
        print("The chef makes fried rice.")
