def greet(param):
    print(f"Hello, {param}")

def retrieve_name():
    return input("enter your name: ")

def main():
    name = retrieve_name()
    greet(name)

main()
