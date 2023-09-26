def plus(n1, n2):
    return n1 + n2
def minus(n1, n2):
    return n1 - n2
def times(n1, n2):
    return n1 * n2
def diviced_by(n1, n2):
    return n1 / n2

def main():
    operations = {'+': plus, '-': minus, '*': times, '/': diviced_by}
    while(True):
        should_continue = input("continue? (y)")
        if 'y' == should_continue:
            operation = input("operation? (+|-|*|/)")
            # ToDo: use a set as valid operations
            if operation != "+" and operation != "-" and operation != "*" and operation != "/":
                print("Unknow operation: " + operation)
            else:
                number1 = int(input("enter first numer: "))
                number2 = int(input("enter second numer: "))
                result = operations[operation](number1, number2)
                print (str(number1) + operation + str(number2) + "=" + str(result))
        else:
            break

main()