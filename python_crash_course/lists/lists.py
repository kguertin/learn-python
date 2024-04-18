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