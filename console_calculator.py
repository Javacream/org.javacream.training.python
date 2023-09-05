# simple console based calculator

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

def execute(operation):
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


def main():
    #pass # placeholder for sequence
    while(True):
        operation = select_operation()
        if (operation == 'exit'):
            break
        execute(operation)

main()