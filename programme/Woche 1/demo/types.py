var1 = 42 # das ist ein int, eine Ganzzahl
# type_of_var1 = type(var1)
# print(type_of_var1)
print(type(var1))

var2 = 'Hello'
print(type(var2))# das ist ein str, eine Zeichenkette beliebiger Länge

var3 = "Hello"
print(type(var3))# das ist ein str, eine Zeichenkette beliebiger Länge

var4 = f"Hello"
print(type(var4))# das ist ein str, eine Zeichenkette beliebiger Länge

var5 = 4.2
print(type(var5))# das ist ein float, eine Fleißkommazahl

# to be continued...
# Logische, Boolschen Werte (8.8.)
# Datencontainer, z.B. Listen (Block 2)

# Python ist NICHT statisch typisiert

message = 'Hello World'
print(type(message))
message = 42 # andere Sprachen würden hier einen Laufzeitfehler erzeugen
print(type(message))


state1 = True
state2 = False
#state3 = Possibly
#state4 = Wahr

and_result = state1 and state2
or_result = state1 or state2

