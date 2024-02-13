def add(x, y):
    return x + y
def do_it(fn, a, b):
    return fn(a, b)

print(add(1,2)) # Hier wird die Funktion aufgerufen
print(add) # hier wird der Algorithmus ausgegeben -> type("hugo")
result  = add(1,3) # result wird der Rückgabewert der Funktion zugeordnet
x = add # Jetzt wird eine neue Variable namens 'x' ebenso auf den Algorithmus (x+y) deuten
print(x)
print(x(6,6))


print(do_it(add, 4, 5))