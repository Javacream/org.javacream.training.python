number1 = input("Bitte geben Sie die erste Ganzzahl ein: ")
number2 = input("Bitte geben Sie die zweite Ganzzahl ein: ")
number1 = int(number1)
number2 = int(number2)

result = number1 + number2
print(f"Die Summe von {number1} und {number2} ist {result}")
# Ginge übrigens auch kürzer, in der String-Interpolation sind einfache Python-Aufrufe valide
print(f"Die Summe von {number1} und {number2} ist {number1 + number2}")

# Ach ja: Gleitkommazahlen sind float
number1 = input("Bitte geben Sie die erste Gleitkommazahl ein, Trenner ist der Punkt '.': ")
number2 = input("Bitte geben Sie die zweite Gleitkommazahl ein, Trenner ist der Punkt '.':")
number1 = float(number1)
number2 = float(number2)

print(f"Die Summe von {number1} und {number2} ist {number1 + number2}")

