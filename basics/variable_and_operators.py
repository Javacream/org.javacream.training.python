# Variablen-Deklaration
# Variablen-Name = Literal
message = "Hello" # "Zeichenketten-Literal" -> intern ist message ein String, str
number = 9 # Eine Ganzzahl
value = 4.2 # Kommazahl
state = True # Logischer Werte, True False
# Hinweis: Weitere Literale wie Listen, Bereiche -> später

# print(number) # Verwendung von Variablen

# Variable oder Konstante? -> Variable, Neuzuweisung ist möglich
message = "World!"
# print(message)

# Typisierung, ist message immer ein str, prüft Python das?
message = 42 # Diese Zuweisung ist möglich, Python ist "untyped"
print(message)

# Verwendung einer nicht-deklarierten Variable
# print(hugo) # NameError: name 'hugo' is not defined