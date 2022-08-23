# Write a Python program that prints your name,
# CS classes taken (or other relevant experience),
# and the date on separate lines. Use one variable
# each for the month, day, and year (3 total).
# Make sure there are no spaces between the
# forward slash and numbers. Submit the .py file.

name = "Michael Catapang"
class_array = [
    "CS 10 - Python Programming", 
    "CS XX - Another Class",
    "and",
    "CS XX - One More Class"
]
separator = ", "
classes = separator.join(class_array)
month = 8
day = 22
year = 2022

print(f"My name is {name}")
print(f"I have taken {classes}")
print(f"Today's date is {month}/{day}/{year}")