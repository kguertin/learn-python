# Errors and Exceptions

# Raising exceptions
    # raise Exception
    # raise IndexError
    # raise NameError
    # raise ValueError("Invalid Character") 

def Database(user):
    print(user)

def get_user_name():
    inp = input("Please enter your name: ")
    if not inp.isalpha():
        raise ValueError("alpha chars only")
    return inp

def register_user():
    user = get_user_name()
    Database.save(user)

try:
    num = int(input("Enter a number: "))
except ValueError: 
    print("Fine I will pick for you.....7")
    num = 7
except EOFError:
    print("You didn't enter anything")
    num = 0

print(f"You entered {num}")