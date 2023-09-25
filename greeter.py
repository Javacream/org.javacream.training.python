def main():
    name = user_input()
    greeting = compose_greeting(name)
    print_out(greeting)

def user_input():
    name_input = input("Enter username: ")
    return name_input

def compose_greeting(name):
    greeting_message = "Hello " + name + "!"
    return greeting_message

def print_out(greeting):
    print(greeting)

main()