# Tuples 
# Immutable, ordered indexed collections
t = (1,2,3)
print(type(t))
t = ("test", 8, [1,2,3], False)
print(type(t))

# 1 Item tuples cant be in parens without a comma
t1 = ("First",)
print(type(t))
t1 = "First",
print(type(t))

# Functionality 
colors = ("red", "orange", "yellow")
print(len(colors))
print(colors[1])
print(colors[:2])
print(colors.index("red"))
print(colors.count("red"))

print("red" in colors)
print("blue" in colors)