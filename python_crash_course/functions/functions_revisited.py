# Functions revisited 

# *args - takes all arguments and place them in a tuple 
def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)

print(average(2,3,4,5,6))

def count(*args):
    print(f"You passed me {len(args)} arguments")

count(1,2,3)

def sum(*nums):
    total = 0 
    for num in nums:
        total += num
    print(total)

sum(1,2,3)

def demo(first, second, *others):
    print(f"first is {first}")
    print(f"second is {second}")
    if len(others) > 0:
        print(f"others is {others}")

demo("Apples", "Oranges", "Mangos", "Pears", "Grapefruit")
demo("Apples", "Oranges")