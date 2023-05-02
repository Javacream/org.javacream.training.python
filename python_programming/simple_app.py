userInput = input("Bitte Kommado eingeben, exit zum beenden oder '+': ")
while userInput != "exit":
    try:
        if userInput == '+':
            number1AsString = input("Bitte die erste Zahl eingeben: ")
            number2AsString = input("Bitte die zweite Zahl eingeben: ")
            number1 = int(number1AsString)
            number2 = int(number2AsString)
            sum = number1 + number2
            print(f"das ergebnis der addition von {number1} und {number2} ist {sum}")
        elif userInput == '-':
            number1AsString = input("Bitte die erste Zahl eingeben: ")
            number2AsString = input("Bitte die zweite Zahl eingeben: ")
            number1 = int(number1AsString)
            number2 = int(number2AsString)
            diff = number1 - number2
            print(f"das ergebnis der subtraktion von {number1} und {number2} ist {diff}")
        elif userInput == '*':
            number1AsString = input("Bitte die erste Zahl eingeben: ")
            number2AsString = input("Bitte die zweite Zahl eingeben: ")
            number1 = int(number1AsString)
            number2 = int(number2AsString)
            product  = number1 * number2
            print(f"das ergebnis der multiplikation von {number1} und {number2} ist {product}")
        elif userInput == '/':
            number1AsString = input("Bitte die erste Zahl eingeben: ")
            number2AsString = input("Bitte die zweite Zahl eingeben: ")
            number1 = int(number1AsString)
            number2 = int(number2AsString)
            quotient  = number1 / number2
            print(f"das ergebnis der division von {number1} und {number2} ist {quotient}")
        else:
            print(f"unbekannte eingabe: {userInput}")
    except:
        print(f"Eine der Eingaben kann nicht in eine Zahl umgewandelt werden, eingabe1={number1AsString} oder eingabe2={number2AsString}")        
    userInput = input("Bitte Kommado eingeben, exit zum beenden oder '+': ")