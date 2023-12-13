def main():
    def plus(number1, number2):
        operation_message = "plus"
        result = number1 + number2
        return operation_message, result
    def minus(number1, number2):
        operation_message = "minus"
        result = number1 - number2
        return operation_message, result
    def multiply(number1, number2):
        operation_message = "times"
        result = number1 * number2
        return operation_message, result
    def divideby(number1, number2):
        operation_message = "divided by"
        result = number1 / number2
        return operation_message, result

    operations = {
        'plus': plus,
        'minus': minus,
        'multiply': multiply,
        'divideby': divideby, 
    }
    
    while True:

        # User input
        # User input
        input_string = input("Input number1 or exit: ")
        if input_string.lower() == 'exit':
            break
        else:    
            number1_as_string = input_string
            number2_as_string = input("Input number2: ")
            if number1_as_string.replace(".", "").isnumeric() and number2_as_string.replace(".", "").isnumeric():
                number1 = float(number1_as_string)
                number2 = float(number2_as_string)
                while True:
                    operation = input("enter operation (plus, minus, multiply, divideby): ")
                    operation_function  = operations.get(operation)
                    if operation_function == None:
                        print(f"invalid operation: {operation}")
                    else:
                        operation_message, result = operation_function(number1, number2)
                        output_string = f'{number1} {operation_message} {number2} is {result}'
                        print(output_string)
                        break
            else:
                print(f'invalid number, you entered {number1_as_string}, {number2_as_string}')    

main()