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

