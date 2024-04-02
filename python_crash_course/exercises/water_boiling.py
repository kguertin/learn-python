unit = input("What unit are you using? ")
temp = int(input("What temperature are you using? "))

if unit == 'f':
    if temp >= 212:
        print("Water is boiling!")
    else:
        print("Water is not boiling, must hit 212F")
elif unit == 'c':
    if temp >= 100:
        print("Water is boiling!")
    else:
        print("Water is not boiling, must hit 100C")
elif unit == 'k':
    if temp >= 373:
        print("Water is boiling!")
    else:
        print("Water is not boiling, must hit 373k")
else: 
    print("I don't know that unit, sorry!")