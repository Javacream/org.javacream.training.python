number1 = float(input("Bitte die erste Zahl eingeben: "))
number2 = float(input("Bitte die zweite Zahl eingeben: "))

result = number1 + number2
print(result) # prinzipiell richtig, aber nicht "schön"

result = number1 - number2
print('Die Differenz der Zahl ' + str(number1) + ' und ' + str(number2) + ' ist ' + str(result)) # viel zu fehleranfällig, Konvertierung in str notwendig

result = number1 * number2
print(f'Das Produkt der Zahlen {number1} und {number2} ist {result}') # viel besser

print(f'Der Quotient der Zahlen {number1} und {number2} ist {number1 / number2}') # das geht übrigens auch in den geschweiften Klammern
