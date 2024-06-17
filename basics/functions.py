#def greet(param):
#    print(f"Hello, {param}")

def greet(param, friendly):
    if friendly:
        print(f"Hi, {param}, nice to meet you!")
    else:
        print(f"Hello, {param}")

def retrieve_name():
    return input("enter your name: ")

def main():
    name = retrieve_name()
#    greet(name) Funktionen können in Python nicht überladen werden!
    greet(name, False)

main()
