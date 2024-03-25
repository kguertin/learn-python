welcome = "WELCOME TO THE USELESS STORE!"
print(welcome)
print("*" * len(welcome))

item_name = input("What item are you purchasing: ")
item_price = float(input(f"What is the price of {item_name}: "))
item_quantity = int(input(f"how many {item_name} are you buying: "))
subtotal = float("{:.2f}".format(item_price * item_quantity))

print(f"Added {item_quantity} {item_name}(s) to shopping cart! ")
print(f"Your subtotal is {subtotal}$")