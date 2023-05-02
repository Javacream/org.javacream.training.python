userInput = input("Bitte Kommado eingeben, exit zum beenden oder '+': ")
while userInput != "exit":
    if userInput == '+':
        number1AsString = input("Bitte die erste Zahl eingeben: ")
        number2AsString = input("Bitte die zweite Zahl eingeben: ")
        number1 = int(number1AsString)
        number2 = int(number2AsString)
        sum = number1 + number2
        print(f"das ergebnis der addition von {number1} und {number2} ist {sum}")
    else:
        print(f"unbekannte eingabe: {userInput}")
    userInput = input("Bitte Kommado eingeben, exit zum beenden oder '+': ")