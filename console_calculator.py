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
    operations = ("+", "-", "*", "/")
    if operation in operations:
        number1 = input_number1()
        number2 = input_number2()
        if (operation == operations[0]):
            result = plus(number1, number2)
        if (operation == operations[1]):
            result = minus(number1, number2)
        if (operation == operations[2]):
            result = times(number1, number2)
        if (operation == operations[3]):
            result = divided_by(number1, number2)
        print (str(number1) + operation + str(number2) + "=" + str(result))
    else:
        print("Unknown operation: " + operation)


def main():
    #pass # placeholder for sequence
    while(True):
        operation = select_operation()
        if (operation in ('exit', 'x')):
            break
        execute(operation)

main()