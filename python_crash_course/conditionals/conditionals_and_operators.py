# Conditionals and Operators

# Logical AND. Both sides true
if 3 < 4 and 3 != 8:
    print("BOTH TRUE")

if 3 > 4 and 3 != 8:

    print("DOES NOT PRINT!")
if 3 < 4 and 3 != 3:
    print("DOES NOT PRINT!")

age = 19
if age > 18 and age < 21:
    print("Can enter the venue but cannot not drink") 

age = 25
if age > 18 and age < 21:
    print("Can enter the venue but cannot not drink") 

# Logical OR. One side true 
day = input("What day of the week is it? ")

if day == 'saturday' or day == "sunday":
    print("It's the weekend!")
else:
    print("Ugh, its a work day!")

age = 4
if age < 5 or age > 65:
    print("You get in for free")
else:
    print("That will be $10")

# Logical NOT. This is the ! in JS, flips the expression. 
if not 1 > 5:
    print("NOT OPERATOR")

if not 1 > 5:
    print("THIS EVALUATES TO FALSE AND DOES NOT RUN")

year = input("What year were you born in? ")
if not year.isnumeric():
    print("That was not a number, please true again")
    year = input("What year were you born in? ")

year = int(year)

CURRENT_YEAR = 2024

print(f"You were born {CURRENT_YEAR - year} years ago.")
