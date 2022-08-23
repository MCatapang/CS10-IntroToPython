# Write a Python program that prompts the user for
# a name, then print a greeting with the name typed.

user_input = input("Enter your name: ")
array_input = user_input.split()
array_name = []
separator = " "

for name in array_input:
    array_name.append(name.capitalize())

name_complete = separator.join(array_name)

print(f"Hello, {name_complete}. Nice to meet you.")