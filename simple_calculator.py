def main():
    plus = lambda n1, n2: n1 + n2
    minus = lambda n1, n2: n1 - n2
    times = lambda n1, n2: n1 * n2
    divided_by = lambda n1, n2: n1 / n2


    operations = {'+': plus, '-': minus, '*': times, '/': divided_by}
    operation_names = {'+', '-', '*', '/'} # later we will use the keys from our dictionary, but for now let's accept some code replication
    while (True):
        should_continue = input("continue? (y)")
        if 'y' == should_continue:
            operation = input("operation? (+|-|*|/)")
            if not operation in operation_names:
                print("Unknow operation: " + operation)
            else:
                number1 = int(input("enter first numer: "))
                number2 = int(input("enter second numer: "))
                result = operations[operation](number1, number2)
                print(str(number1) + operation +
                      str(number2) + "=" + str(result))
        else:
            break


main()
