# Scope 

# LEGB - Scope Order

#Global Scope - Availible everywhere 
animal = "Lemur"

print("Outside of functions", animal)

def func():
    print("inside of functions", animal)  

    def inner_func():
            print("inside of innter function", animal)  
    inner_func()

func()

# Local Scope - Variable within a function - Local score doesn't apply to conditionals and loops.
def zoo():
      animal = "Harlequin Shrimp"
      print("inside zoo function", animal)
zoo()
print("outside function cannot read animal in zoo function")

# Enclosing Scope - Nested functions can access parent functions variables.

# Built in score are available throughout python 

# Global - can put in front of vars to define if variable is global
def outer(): 
    global new_animal
    new_animal = "spider Crab"
outer()

print(new_animal)