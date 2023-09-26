

def main():
    def plus(n1, n2):
        return n1 + n2


    def minus(n1, n2):
        return n1 - n2


    def times(n1, n2):
        return n1 * n2


    def diviced_by(n1, n2):
        return n1 / n2
    operations = {'+': plus, '-': minus, '*': times, '/': diviced_by}
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
