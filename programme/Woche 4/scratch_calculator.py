def plus(n1, n2):
    return n1 + n2

def application():
    operations = dict()
    minus = lambda n1, n2: n1 - n2
    operations['+'] = plus
    operations['-'] = minus
    operation_name = input("Operation?: ")
    operation = operations.get(operation_name)
    print(operation(20, 22))

application()