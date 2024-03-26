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