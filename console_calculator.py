# simple console based calculator

def main_loop():
    input_string = input("enter exit to stop: ")
    if (input_string == "exit"):
        return False
    else:
        return True
def select_operation():
    return input("enter operation: ")
def input_number1():
    input_string = input("enter first number: ")
    return int(input_string)
def input_number2():
    input_string = input("enter second number: ")
    return int(input_string)

def plus(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def times(number1, number2):
    return number1 * number2

def divided_by(number1, number2):
    return number1 / number2


def main():
    #pass # placeholder for sequence
    go_on = main_loop()
    while(go_on):
        operation = select_operation()
        if (operation == "+" or operation == "-" or operation == "*" or operation == "/"):
            number1 = input_number1()
            number2 = input_number2()
            if (operation == "+"):
                result = plus(number1, number2)
            if (operation == "-"):
                result = minus(number1, number2)
            if (operation == "*"):
                result = times(number1, number2)
            if (operation == "/"):
                result = divided_by(number1, number2)
            print (str(number1) + operation + str(number2) + "=" + str(result))
        else:
            print("Unknown operation: " + operation)
        go_on = main_loop()

main()