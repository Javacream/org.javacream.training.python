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

# Mathematische Operatoren
result = number + 5 # +, -, *, /, %

# Logische Operatoren
state = True and False
state = True or False

# + für Zeichenketten


# Abkürzende Schreibweisen
number += 5 # number = number + 5
# number++ inkrement um 1 wird nicht unterstützt

# + mit Zeichenketten, auch * wird unterstützt
message = 'Hello'
message = 5*message + '!'
#print(message)

# Kombination von Zeichenketten- und mathematischen Operatoren wird nicht unterstützt
#message = message + number # TypeError: can only concatenate str (not "int") to str

# string interpolation = Zugriff auf Variablen in einem formatted String
output = f"the message is: {message}, the number is: {number}" # Freitext mit Zugriff auf Variablen
print(output)