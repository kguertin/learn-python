# Logical Operators

color = input("Enter a color: ")
# Evaluate truthy vs falsy 
if color:
    print(f"{color} is my favourite colour too!")

#Order 
#not
#and
#or

day = "Tuesday"
is_vet = True
age = 56

if not (age <= 2 or is_vet and day == "Tuesday"):
    print("You have to buy a ticket")