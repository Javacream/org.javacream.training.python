if 2 < 5:
    print('2 ist kleiner als fünf')

print('1')
#  print('2') unexpected indent
print('3')

if 2 < 5:
    pass
else:
    pass

print('fertig') 

b1 = True
b2 = False

print(type(b2))

print (not b1)
print (b1 and b2)
result = b1 or b2
print(result)

var1 = 25
var2 = var1
var3 = var2 = 42 # var3 und var2 werden auf den Wert 42 gesetzt
var3 = var2 == 42 # var3 ist der Wert des Vergleichs
var3 = (var2 == 42) # runde Klammern ändern die Prioisierung der Ausführung, hier eigentlich nicht notwendig, == wird vor der Zuweisung = ausgeführt
print('done')
