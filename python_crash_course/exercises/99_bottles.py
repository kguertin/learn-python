for num in range(99, 0, -1):
    print(f"{num} bottles of beer on the wall.")
    print(f"{num} bottles of beer.")
    if num == 1:
        print("Take one down, pass it around, no more bottles of beer on the wall")
    else:
        print(f"Take one down, pass it around, {num - 1} bottles of beet on the wall")
    print('*' * 20) 

count = 99
while count <= 1:
    print(f"{count} bottles of beer on the wall.")
    print(f"{count} bottles of beer.")
    if count - 1 == 0:
        print("Take one down, pass it around, no more bottles of beer on the wall")
    else:
        print(f"Take one down, pass it around, {count - 1} bottles of beet on the wall")
    count -= 1
    print('*' * 20) 