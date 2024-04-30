# Todo Script
todo_list = []
completed = []

print("""
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
""")

quit = False
while quit == False:
    print("*" * 25)
    command = input("Enter a command. Type 'h' for help:\n> ")

    if command == "q":
        print(f"Today you completed {len(completed)} todos:")
        for item in completed: 
            print(f"* {item}")
        quit = True
    elif command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list type it and hit enter")
        print("To complete a todo enter its number")
    elif command.isdigit():
        item = int(command)
        if item <= len(todo_list):
            completed.append(todo_list.pop(item - 1))
    else:
        if len(command.strip()) > 0:
            todo_list.append(command)

    idx = 0
    while idx < len(todo_list):
        print(f"{idx + 1}) {todo_list[idx]}")
        idx += 1