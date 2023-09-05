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
def check_odd_or_even(number1, number2):
    number1_even = number1 % 2 == 0
    number2_even = number2 % 2 == 0
    if number1_even:
        result1 = str(number1) + " is even"
    else:
        result1 = str(number1) + " is odd"
    if number2_even:
        result2 = str(number2) + " is even"
    else:
        result2 = str(number2) + " is odd"
    return result1 + ', ' + result2 

def execute(operation):
    operations = ("+", "-", "*", "/", "oe")
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
        if (operation == operations[4]):
            print(check_odd_or_even(number1, number2))
            return
        print (str(number1) + operation + str(number2) + "=" + str(result))

    else:
        print("Unknown operation: " + operation)


def main():
    #pass # placeholder for sequence
    while(True):
        operation = select_operation()
        if (operation in ('', 'exit', 'x')):
            break
        execute(operation)

main()