print("Welcome to the game")
print("*" * 20)

num_left = 13
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")
current_player = player1_name

while True:
    print("| " * num_left )
    print(f"There are {num_left} toothpicks left")
    choice = int(input(f"{current_player}, how many toothpicks do you take? "))
    num_left -= choice
    
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input("You can only chose 1, 2 or 3: "))

    if(num_left <= 0):
        print(f"{current_player}, wins the game!")
        break
    if current_player == player1_name:
        current_player = player2_name
    else:
        current_player =player1_name


print("GAME OVER!")