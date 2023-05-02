number1 = 333
while number1 < 10:
    print(number1)
    number1 = number1 + 2	
print(f"while loop ist beendet mit dem Wert {number1} für number1") #f"..."", ein Formatted String mit Zugriff auf die Variablen
 #print(number1)

number2 = 42

if number1 > number2:
    print("number1 is greater than number2")
else:
    print("number1 is smaller or equals than number2")

names = ["Hugo", "Emil", "Fritz", "Egon"]

#allgemeine form: for element in list
for name in names:
    print(name)