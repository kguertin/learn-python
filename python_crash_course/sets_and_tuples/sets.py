# Sets
# Unordered collections with no duplicate elements, can only contain immutable elements 

evens = {2,4,6,8}
print(type(evens))

# empty set, {} makes dict
s = set({2,4,6,8,4,2})
print(s)

# methods
evens.add(10)
print(evens)

# Remove will throw and error if not present, discard will not
evens.add(7)
print(evens)
evens.remove(7)
print(evens)
evens.discard(21)
evens.clear()
print(evens)

print({1,2,3} is {1,2,3})
print({1,2,3} == {1,2,3})

evens = {2,4,6,8}
print(2 in evens)
print(3 in evens)

for num in evens:
    print(num)

# Set Operators
webdev = {'SQL', "css", "html", 'js', 'python'}
data = {"SQL", "R", "python"}

# Intersection
print(webdev & data)
print(webdev.intersection(data))

# Union
print(data | webdev)
print(data.union(webdev))

# Difference -  what is unique to the left set 
print(webdev - data)
print(webdev.difference(data))
print(data - webdev)
print(data.difference(webdev))
