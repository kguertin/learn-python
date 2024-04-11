# Basics of python functions

# Need to define the function before executing it.
def laugh():
    print("Ha!" * 20)

laugh()

def laugh_by_number(intensity):
    print("Ha!" * intensity)

laugh_by_number(1)
laugh_by_number(5)
laugh_by_number(10)

def divide(x, y):
    print(x / y)

divide(1,2)
divide(45,6.4)
divide(100, 33.3)
divide(4, 100)
divide(100, 4)

# Returning values. If we do not returning something, function implicitly returns the value None.
def divide_return(x,y):
    return x/y

num = divide_return(1,3)
print(num)

# Default Params
def laugh_strength(strength=2):
    print("HA!" * strength)
laugh_strength(10)
laugh_strength()

def slugify(url, sep="-"):
    return url.strip().lower().replace(" ", sep)

url = slugify("       HELLO world I LOVE YOU         ")
print(url)
url = slugify("       HELLO world I LOVE YOU         ", "_")
print(url)
url = slugify("       HELLO world I LOVE YOU         ", "X")
print(url)

# Default value must come after parameters without default.
def greet( person, msg = "Hi",):
    print(f"{msg}, {person}!")

greet("Kevin")