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