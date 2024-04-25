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
