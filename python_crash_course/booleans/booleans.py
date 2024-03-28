# Booleans

# Comparison Operators 
print(10 > 3)
print(3 > 10)
age = 19
print(age > 21)
print(age < 21)
print(age >= 21)
print(21 >= 21)
print(age <= 10)

# Equality Operators 
print(10 == 10)
print(10 == 9)
print(10 != 10)
print(10 != 9)
print("a" == "a")
print("A" == "a")
print("A" != "a")
print(3.5 == 3.5)
print(3.5 != 10.1)
print(3.0 == 3)

# Truthyness and Falseyness
# Similar to how this is divided in JavaScript
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Kevin"))
print(bool([]))
print(bool([1]))

# in operator
# checks if the left value is a member of the right value. Works on sequences (strings, lists, etc )
print("a" in "bat")
print("A" in "bat")
print("onto" in "Toronto")
print("ontos" in "Toronto")

# Comparing strings
# compares the unicode number. user ord() to show unicode value
print("a" < "w")
print("a" < "$")
print("a" < "A")
print(ord("a"))
print(ord("A"))
print("100" < "9")