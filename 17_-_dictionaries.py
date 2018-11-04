# Dictionaries are defined by using "{}" and inserting elements between these brackets.
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Keys have to be UNIQUE!
print(month_conversions)
print(month_conversions["Nov"])
print(month_conversions.get("Dec"))

# "None" is printed if the key is not present in the dictionary.
print(month_conversions.get("Par"))

# Default value if the key value is not found.
print(month_conversions.get("Par", "Not a valid key."))

# Key-value pairs in dictionary do not have to be of the same data type.
month_conversions = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
