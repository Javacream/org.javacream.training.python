#def greet(param):
#    print(f"Hello, {param}")

def greet(param, friendly=True):
    if friendly:
        print(f"Hi, {param}, nice to meet you!")
    else:
        print(f"Hello, {param}")

def greet_with_varargs(*params): # variable Parameter-Liste -> List
   for param in params:
       print(param)
def greet_with_kwargs(**params): # keyworded Parameter -> Dictionary
   print(params["lastname"])



def retrieve_name():
    return input("enter your name: ")

def main():
    # name = retrieve_name()
#    greet(name) Funktionen können in Python nicht überladen werden!
#    greet(name, False)
#    greet(name)
    # greet_with_varargs('Hugo', 'Emil', "Fritz")
    greet_with_kwargs(lastname="Sawitzki", firstname="Rainer")
main()
