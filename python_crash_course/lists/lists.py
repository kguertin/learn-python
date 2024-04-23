# Lists

# Creating Lists
tasks = ["Trash", "Dishes", "Laundry", "Dinner"]
high_scores = [99, 78, 56, 50, 20, 12]

print(type(high_scores))
print(high_scores)

stuff = [4, 5.6, True, False, "hi", []]

print(list("hello"))
print(list(range(1,10)))

# Accessing List Items 
wait_list = ["Tom", "Arya", "Amir"]
print(wait_list[0])
print(wait_list[1])
print(wait_list[2])
print(wait_list[-1])

wait_list[1] = "Aria"
print(wait_list[1])

# List Methods
# Append adds item to end of list
nums = [1,2,3,4]
nums.append(5)
print(nums)

# Extend takes an iterable
letters = list("abc")
letters.extend("defg")
print(letters)
teams = ["CF Montreal", "Toronto FC", "Vancouver Whitecaps"]
teams.extend(["LA Galaxy", "LAFC"])
print(teams)

# Insert
nums = [1,2,4]
nums.insert(2, 3)
print(nums)

# List Slices
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[0:4])
print(list1[0:9:2])
print(list1[5:])
print(list1[:5])

nums = [4,5,6,7]
print(nums)
nums = [4,5,6,7]
nums[1:3] = ["a", "b", "c", "d"]
print(nums)
nums[1:5] = [5]
print(nums)

# Clear - Empties a list
letters = ["a", "b", "c"]
print(letters)
letters.clear()
print(letters)

# Remove - removes the first match of a value
cities = ["TOR", "VAN" , "CGY", "MTL", "CGY"]
print(cities)
cities.remove("CGY")
print(cities)

# Pop - removes last element from list, returns it. 
print(cities.pop())
print(cities)
cities.append("OTT")
print(cities)
# Can also pop an index
print(cities.pop(1))
print(cities)
# Del statement can be used to delete indexes - can  be used with slices. 
del cities[2]
print(cities)

# Loops and lists
num_list = [1,2,3,4,5,6,7,8,9,10]
for num in num_list:
    print(num)

idx = 0
while idx < len(num_list):
    print(f"The index is {idx}, the value is {num_list[idx]}")
    idx += 1