# Todo Script
print("""
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
""")
todo_list = []
completed = []

while True:
    for i in range(len(todo_list)):
        print(f"{i + 1}) {todo_list[i]}")
    print("*" * 25)
    print("Enter a command. Type 'h' for help:")
    command = input("> ")

    if command == "q":
        break
    elif command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list type it and hit enter")
        print("To complete a todo enter its number")
    elif command.isnumeric():
        idx = int(command) - 1
        if idx >= len(todo_list):
            print("There is no todo with that number")
        else:
            completed.append(todo_list.pop(idx))
    else:
        if len(command.strip()) > 0:
            todo_list.append(command)

if len(completed) > 0:
    print(f"Today you completed {len(completed)} todos:")
    for item in completed: 
        print(f"* {item}")
