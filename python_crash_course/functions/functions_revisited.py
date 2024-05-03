# Functions revisited 

# *args - takes all arguments and place them in a tuple 
def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)

print(average(2,3,4,5,6))

def count(*args):
    print(f"You passed me {len(args)} arguments")

count(1,2,3)

def sum(*nums):
    print(nums)
    total = 0 
    for num in nums:
        total += num
    print(total)

sum(1,2,3)

def demo(first, second, *others):
    print(f"first is {first}")
    print(f"second is {second}")
    if len(others) > 0:
        print(f"others is {others}")

demo("Apples", "Oranges", "Mangos", "Pears", "Grapefruit")
demo("Apples", "Oranges")

# **kwargs - create a dictionary out of keyword arguments
def kwargsDemo(**kwargs):
    print(kwargs)

kwargsDemo(color="red", age=30)

# Parameter list ordering
# Defaults come after params, *args come after default, *kwargs come after default params. 

# Issue with mutable default args
def add_thrice(val, lst=[]):
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst

print(add_thrice(7, [1,2,3]))
print(add_thrice(7))
# We keep the appended items to the default list
print(add_thrice(7))

def add_thrice_v2(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst

print(add_thrice_v2(7, [1,2,3]))
print(add_thrice_v2(7))
# In this case we are setting an empty list each call if no list is passed
print(add_thrice_v2(7))

# Argument unpacking
nums = [1,2,3,4,5,6,7,8,9, 10]
# Can unpack a list of numbers as separate args using *
sum(*nums)
