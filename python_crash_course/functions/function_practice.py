def isEven(num):
    return num % 2 == 0

print(isEven(24))
print(isEven(69))
print(isEven(420))

def slugify(url):
    return url.strip().lower().replace(" ", "-")

url = slugify("       HELLO world I LOVE YOU         ")
print(url)


def countVowels(str):
    vowels = 0
    for char in str:
        if char in "aeiou":
            vowels += 1
    return vowels

print(countVowels("ooolooo"))
print(countVowels("Toronto Raptors"))
print(countVowels("sdsdsdsdsdsdsds"))