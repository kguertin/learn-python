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

# List Methods
# Count returns the number of times something appears in a list

list = [True, True, False, False, False]
print(list.count(True))
print(list.count("true"))

# Reverse: Reverses a list IN PLACE (Mutates the existing list)
print(list)
list.reverse()
print(list)

# sort: sorts the list IN PLACE
evens = [6,2,4]
evens.sort()
print(evens)
evens.sort(reverse=True)
print(evens)

# Sorted by char value when working with strings
colors = ["red", "orange", "purple", "green"]
colors.sort()
print(colors)

# ID returns the identifier in memory
num = 34
print(id(num))
num = 34
print(id(num))
true = True
print(id(true))
true = True
print(id(true))

# List have their own unique identity, not the same identifier. A new list is a new container in memory.
list = []
print(id(list))
# If we dont reassign the list it keeps the same ID
list = []
print(id(list))
print(id(list))
# List2 points to the original list
list2 = list
print(id(list2))
# This updates both lists as list2 is essentially a reference to list one 
list2.append(2)
print(list)
print(list2)

# Comparing Lists 
# == compairs the contents of two lists, do they hold the same value.
# is compares the identity of two lists.
demo1 = [1,2,3]
demo2 = [1,2,3]

print(demo1 == demo2)
print(demo1 is demo2)

# Split and Join
# Split - Similar to JS
birthday = "03/27/2020"
print(birthday.split("/"))
full_name = "Teddy Richard Smith Jr"
print(full_name.split(" "))

# Join - Reverse of JS
fruits = ["Apple", "Pear", "Kiwi"]
print(" ".join(fruits))
print("!!!".join(fruits))

# Unpacking - Like JS Destructuring. Must unpack all values of an array. Can use * for left overs
color = [244, 43, 19]
red, green, blue = color
print(red,green,blue)

item = [4, "Pizza", "Plain", "16.98"]
quantity, *others, price = item
print(quantity, others, price)

# Copying Lists
# This creates a ref to an existing list.
i2 = item
print(id(item), id(i2))
print(i2 is item)
print(i2 == item)

# This creates a shallow copy (no nested data structures copied)
i2 = item.copy()
print(id(item), id(i2))
print(i2 is item)
print(i2 == item)

# Can make shallow copy with slice
i3 = i2[:]

