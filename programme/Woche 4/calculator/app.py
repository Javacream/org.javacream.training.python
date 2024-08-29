import calculator # Name einer Datei ohne Endung .py
def application():
    NEW_CALCULATION_INPUT_MESSAGE = "soll eine neue Berechung durchgeführt werden (J / n):"
    FIRST_NUMBER_MESSAGE = "Bitte geben Sie die erste Zahl an: "
    SECOND_NUMBER_MESSAGE = "Bitte geben Sie die zweite Zahl an: "
    OPERATION_MESSAGE = "Bitte geben Sie die gewünschte Operation an (+, -, *, /): "

    operations = dict()
    operations['+'] = calculator.plus
    operations['-'] = calculator.minus
    operations['*'] = calculator.times
    operations['/'] = calculator.divide

    while True:
        try:
            number1 = input(FIRST_NUMBER_MESSAGE)
            number1 = float(number1)
            try:
                number2 = input(SECOND_NUMBER_MESSAGE)
                number2 = float(number2)
                operation_name = input(OPERATION_MESSAGE)
                operation = operations.get(operation_name)
                if operation == None:
                    print(f"Ungültige Operation: {operation_name}")
                else:
                    print(operation(number1, number2))
            except:
                print(f'Fehlerhafte Eingabe: {number2}')
        except:
            print(f'Fehlerhafte Eingabe: {number1}')
        new_calculation = input(NEW_CALCULATION_INPUT_MESSAGE)
        if new_calculation == 'n':
            break    

application()