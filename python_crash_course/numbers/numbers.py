# INTEGERS AND FLOATS

# Float has decimal points, integers are whole numbers (negative or positive)
# floats are bound by a limit of precision. 
num = 12
print(num)
print(type(num))

num = -15
print(num)
print(type(num))

num = 6.66
print(num)
print(type(num))

# below is a valid number as well
num = 1_000_000
print(num)
print(type(num))


# BASIC OPERATORS

num = 1 + 4
print(num)
num = 7 - 2
print(num)
num = 5 - 2.5
print(num)
num = 45 * 45
print(num)
num = 5 / 2
print(num)
num = 10 / 3.6
print(num)
# Order of operations 
num = 6 * 3 - 10
print(num)
num = 6 * (3 - 10)
print(num)

# Exponentiation
num = 4 ** 3
print(num)
# Integer Division (always rounds down)
num = 10 / 3
print(num)
num = 10 // 3
print(num)
# Modulo (Remainder)
num = 38 % 10
print(num)