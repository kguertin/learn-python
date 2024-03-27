# string methods 

# Capitalization Methods
word = "HELLO world"
print(word.title())
print(word.capitalize())
print(word.lower())
print(word.upper())

# Strip Methods
name = "        Kevin!    "
print(name.strip())
dash = "----Kevin-----"
print(dash.strip("-"))
name = ".,.,.,.,,,....Kevin,,,,,,...,,."
print(name.strip(",."))
print(name.rstrip(",."))
print(name.lstrip(",."))

# Replace
team = "Detroit Raptors"
print(team.replace("Detroit", "Toronto"))
prices = "$1.99 $2.99 $3.99"
print(prices.replace("$", ""))
print(prices.replace("$", "", 1))

# Find and Index
print(prices.find("$"))
print(prices.find("9"))
print(prices.find("$", 1))
print(prices.find("$", 7, 9))
print(prices.count("$"))
print(prices.count("9", 3, 7))

# Chaining Methods
email = "         TODD@gmail.com             "
print(email.lower().strip())