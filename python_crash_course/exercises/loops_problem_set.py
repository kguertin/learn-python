
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable

for char in word: 
    print(char)


# Write a while loop that does the same thing!
count = 0 
while count < len(word):
    print(word[count])
    count += 1


#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
count = 100 
while count <= 140:
    if not count % 2: 
        print(count)
    count += 1

# Write a for loop that does the same thing (with range())
for num in range(100, 142, 2):
    print(num)


#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
correct_pass = "sillygoose"
password = input(f"Enter the passphrase '{correct_pass}': ")
while password != correct_pass:
    password = input(f"Enter the passphrase '{correct_pass}': ")
print("You are a silly goose!")
