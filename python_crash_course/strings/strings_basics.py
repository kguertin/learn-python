# Strings in Python Basics
string = "Hello World!"
print(string)
string = 'hello world?'
print(string)
print(type(string))
string = "You can't use single strings within a string using single quotes"
print(string)

# In python we can change the types of variables
variable = 48
print(type(variable))
variable = "string"
print(type(variable))

# String Operators - No type coercion?
opp = "hello" + "World"
print(opp)

first_name = "Kyle"
last_name = "Lowry"
full_name = first_name + " " + last_name
print(full_name)
num = "4" + "5"
print(num)

print("ha" * 19)

# String Indexing
test = "hello"
print(test[0])
print(test[4])

print(full_name[-1])

# None type - Python's version of null
user = None
print(type(user))
