while True:
    input_text = input("enter first number or 'exit': ")
    if (input_text == 'exit'):
        break
    else:
        number1 = input_text
        number2 = input("enter second number: ")
        try:
            number1 = float(number1)
            number2 = float(number2)
        except:
            print(f"you entered invalid numbers: {number1}, {number2}")
            continue
        operation = input("enter operation (+, -): ")
        if operation == '+':
            print(f"the sum of {number1} and {number2} is {number1 + number2}")
        elif operation == '-':
            print(f"the difference of {number1} and {number2} is {number1 - number2}") 
        else:
            print (f"you entered an invalid operation: {operation}")        
