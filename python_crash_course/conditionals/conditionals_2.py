# Nested Conditionals
fav_color = "green"
fav_movie = "Amadeus"
fav_food = "pasta"

# How nested conditionals run vs non-nested. Nested conditionals can be gated. 

if fav_color == "green":
    print("I love green too!")
    if fav_movie == "Amadeus":
        print("I love Amadeus too!")
        if fav_food == "pasta":
            print("I love pasta too!")


if fav_color == "green":
    print("I love green too!")
if fav_movie == "Amadeus":
    print("I love Amadeus too!")
if fav_food == "pasta":
    print("I love pasta too!")