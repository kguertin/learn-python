first_name = input("What is your name? ").strip()
last_name = input("What is your last name? ").strip()
name_length = len(first_name) + len(last_name)

print("*" * 20)
if name_length == 12:
    print(f"{first_name} {last_name} is exactly the average length of American names")
elif name_length < 12:
    print(f"{first_name} {last_name} is shorter than the average American name")
else:
    print(f"{first_name} {last_name} is longer than the average American name")
print("*" * 20)