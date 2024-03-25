# Strings and built in functions

# len function  - get length
word = "Chicken"
print(len(word))

# input - prompts the user to enter an input
print("*** Welcome to the name app***")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = first_name + " " + last_name
print("Hi there " + full_name + "!!!!!")

# Type Casting
age = "19"
print(type(int(age)))
print(float(age))
print(type(str(55)))
print(int(1.999))
