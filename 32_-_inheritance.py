# "Chef" class is import from "Chef" file.
from chef import Chef
from chinese_chef import ChineseChef

# Objects of classes "Chef" and "ChineseChef" are created.
myChef = Chef()
myChineseChef = ChineseChef()

# Functions from "Chef" object can be used as usual.
myChef.make_chicken()
myChef.make_special_dish()

# "make_chicken" can be called on "ChineseChef" object because it inherits the "Chef" class.
myChineseChef.make_chicken()

# Name of "make_special_dish" is inherited from the "Chef" class, but its content is changed.
myChineseChef.make_special_dish()
