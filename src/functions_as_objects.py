s = 'Hugo'
def my_fn(p):
    print(p)

my_fn(42)

s = 'Emil'
def my_fn():
    print("egal")

my_fn()


s2 = s # Assignment des Wertes der Referenz s zu s2
x = my_fn # WICHTIG: Kein Aufruf der Funktion my_fn, deshalb keine runden Klammern! Es ist eine Assignement

#s2() not callable
x() # x referenziert das selbe Objekt, eine function, wie my_fn