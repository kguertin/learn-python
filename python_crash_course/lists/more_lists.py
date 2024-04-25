# Nested Lists

couples = [
    ["Beyonce", "Jay Z"],
    ["Johnny", "June"],
    ["John", "Yoko"],
    ["Will", "Jada"]
]

print(len(couples))
print(couples[1][0])
print(couples[1][0][-1])

for couple in couples:
    print(couple)
    for person in couple: 
        print(f"Sending email to: {person}")

# List Operators
# "+" Concatenates lists creating a new list 
list = [1,2] + [3,4]
print(list)

# "*" makes a new list that is a result of repeating the existing list values
list = [1,2,3] * 3
print(list)

# "in" checks if a value is in a list
print(1 in [2,3,4])
print(4 in [2,3,4])

def buyIceCream():
    flavors = ["Chocolate", "vanilla", "lemon", "strawberry"]

    response = input("What flavor would you like? ")

    while response.lower() not in flavors:
        response = input("I dont know that flavor. What flavor would you like? ")

    print(f"OK, {response} ice cream coming right up")

# buyIceCream()