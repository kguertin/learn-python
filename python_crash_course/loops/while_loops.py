# Loops 

# While Loops. Loop repeats as long as expression is true

answer = input("Please say hi ")

while answer != "hi":
    answer = input("Rude. Please say hi... ")

print("Hi to you too!")

count = 10
while count > 0:
    print(f"The number is {count}")
    count -= 1

num = 1 
while num <= 10:
    print(f"The number is {num}")
    num += 1


stars = 1
while stars < 10:
    print("*" * stars)
    stars += 1


stars = 10
while stars > 0:
    print("*" * stars)
    stars -= 1

