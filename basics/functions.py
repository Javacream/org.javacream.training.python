#def greet(param):
#    print(f"Hello, {param}")

def greet(param, friendly=True):
    if friendly:
        print(f"Hi, {param}, nice to meet you!")
    else:
        print(f"Hello, {param}")

# def greet(*param): # variable Parameter-Liste -> List
#    pass
# def greet(**param): # keyworded Parameter -> Dictionary
#    pass

def retrieve_name():
    return input("enter your name: ")

def main():
    name = retrieve_name()
#    greet(name) Funktionen können in Python nicht überladen werden!
    greet(name, False)
    greet(name)

main()
