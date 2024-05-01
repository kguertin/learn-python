# Dictionaries
empty_dict = {}
print(type(empty_dict))

# Key / Value pairs 
movie = {"title": "Amadeus", "imdb_score": 8.3}
print(movie)

# Accessing Dictionary Values 
print(movie["title"])

# Updating Values
movie["title"] = "King Kong"
movie["imdb_score"] -= 0.5
print(movie)

# Adding new key / value pairs
movie["rating"] = "R"
print(movie)

# in operator - Only checks the keys 
print("title" in movie)

# get() - pass a key, returns value or none
print(movie.get("title"))
print(movie.get("cast"))

# pop
movie.pop('rating')
print(movie)
# pop item removes the most recently added kay value pair and returns both the key and the value
movie["rating"] = "R"
key, value = movie.popitem() 
print(key,value)
# clear deletes all values from dict - still the same dict
# del deletes a key value pair based on key 

# Iterables 
test_scores = {
    "Marsha": 78,
    "Boker": 69,
    "Rosa": 92,
    "Leif": 97,
    "Peng": 61,
    "Juan": 73,
    "Esteban": 84,
    "Amir": 91, 
    "Sakura": 99
}

# Default behavior of iterating over a dictionary is .keys()
print(test_scores.keys())
print(test_scores.values())

for student in test_scores.keys():
    print(student)

total = 0
for score in test_scores.values():
    total += score
    print(score)
print(f"Average Score is {total/len(test_scores)}")

print(test_scores.items())
max_score = 0
best_student = ""
for student, score in test_scores.items():
    if score > max_score: 
        max_score = score
        best_student = student
    print(f"{student} got a score of {score}")
print(f"Highest score was {max_score} by {best_student}")

#Update - joining dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4, "e": 5, "a": "apple"}
d1.update(d2)
print(d1)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4, "e": 5, "a": "apple"}
#last dictionary takes precedence if there are two keys 
d3 = {**d1, **d2}
print(d3)
 # Python 3.9 or higher
d4 = d1 | d2
print(d4)