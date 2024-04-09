# Break and Continue - key words in a loop

# break stops the loop
for char in "TorontoRaptorsDetroitPistons":
    if char == "D":
        break 
    print(char)

# Continue stops current iteration
for char in "TorontoRaptorsDetroitPistons":
    if char in "aeiou":
        continue
    print(char)