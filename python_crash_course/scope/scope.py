# Scope 

#Global Scope - Availible everywhere 
animal = "Lemur"

print("Outside of functions", animal)

def func():
    print("inside of functions", animal)  

    def inner_func():
            print("inside of innter function", animal)  
    inner_func()

func()

# Local Scope - Variable within a function 
def zoo():
      animal = "Harlequin Shrimp"
      print("inside zoo function", animal)
zoo()
print("outside function cannot read animal in zoo function")
