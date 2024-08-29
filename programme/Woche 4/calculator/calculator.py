def calculator():
    def plus(n1, n2):
        return n1 + n2
    def minus(n1, n2):
        return n1 - n2
    def times(n1, n2):
        return n1 * n2
    def divide(n1, n2):
        return n1 / n2
    def modulo(n1, n2):
        return n1 % n2

    calculator = dict()
    calculator['+'] = plus
    calculator['-'] = minus
    calculator['*'] = times
    calculator['/'] = divide
    calculator['%'] = modulo
    return calculator

supported_operations = ('+', '-', '*', '/', '%')