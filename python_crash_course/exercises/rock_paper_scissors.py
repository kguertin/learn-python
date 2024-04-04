from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
computer_action = None

if num == 1: 
    computer_action = rock
elif num == 2:
    computer_action = paper
elif num == 3:
    computer_action = scissors

# Ask a user to enter their move
user_action = None
user_input = input("Select rock, paper or scissors: ").lower()
valid_entry = user_input == "rock" or user_input == "paper" or user_input == "scissors"

if not valid_entry:
    user_input = input("Select rock, paper or scissors: ")

if user_input == "rock": 
    user_action = rock
elif user_input == "paper":
    user_action = paper
else:
    user_action = scissors

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("USER SELECTS")
print(user_action)
print("\n")


# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("COMPUTER SELECTS")
print(computer_action)

# Figure out who wins and print the result!
user_win_conditions = computer_action == rock and user_action == paper or computer_action == paper and user_action == scissors or computer_action == scissors and user_action == rock
if user_action == computer_action:
    print("Its a draw!")
elif user_win_conditions:
    print("User wins!")
else:
    print("Computer wins")