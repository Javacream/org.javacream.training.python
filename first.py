def main():
    message = "Hello!"
    x = message
    x = "any..." # again a reassignment, not an object modification
    print_out(message)


def print_out(p):
    number = 9 
    print(p)
    p = "Goodbye" # reassignment
    print(p)
    print(number)

main()