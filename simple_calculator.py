def main():
    while(True):
        should_continue = input("continue? (y)")
        if 'y' == should_continue:
            operation = input("operation? (+|-|*|/)")
            if operation != "+" and operation != "-" and operation != "*" and operation != "/":
                print("Unknow operation: " + operation)
            else:
                number1 = int(input("enter first numer: "))
                number2 = int(input("enter second numer: "))
                result = 0
                if '+' == operation:
                    result = number1 + number2
                if '-' == operation:
                    result = number1 - number2
                if '*' == operation:
                    result = number1 * number2
                if '/' == operation:
                    result = number1 / number2
                print (str(number1) + operation + str(number2) + "=" + str(result))
        else:
            break

main()