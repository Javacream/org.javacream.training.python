NEW_CALCULATION_INPUT_MESSAGE = "soll eine neue Berechung durchgeführt werden (J / n):"
FIRST_NUMBER_MESSAGE = "Bitte geben Sie die erste Zahl an: "
SECOND_NUMBER_MESSAGE = "Bitte geben Sie die zweite Zahl an: "
OPERATION_MESSAGE = "Bitte geben Sie die gewünschte Operation an (+, -, *, /): "


while True:
    number1 = input(FIRST_NUMBER_MESSAGE)
    number2 = input(SECOND_NUMBER_MESSAGE)
    operation = input(OPERATION_MESSAGE)
    number1 = float(number1)
    number2 = float(number2)

    if operation == '+':
        sum = number1 + number2
        print(f'Die Summe aus {number1} und {number2} = {sum}')
    elif operation == '-':
        diff = number1 - number2
        print(f'Die Differenz von {number1} und {number2} = {diff}')
    elif operation == '*':
        print(f'Das Produkt von {number1} und {number2} = {number1 * number2}')
    elif operation == '/':
        print(f'Der Quotient von {number1} und {number2} = {number1 / number2}')
    else:
        print(f"ungültige Operation: {operation}")
    new_calculation = input(NEW_CALCULATION_INPUT_MESSAGE)
    if new_calculation == 'n':
        break    