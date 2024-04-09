import random

num_dice = int(input("How many dice are we rolling? "))
num_sides = int(input("How many sides on each die? "))

while True:
    result = "|"
    for num in range(0, num_dice):
        roll = random.randint(1, num_sides)
        result += f"{roll}|"
    print(result)
    reply = input("Roll again? ('q' to quit) ")
    if reply == "q":
        break
  
    