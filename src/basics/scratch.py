# Funktionen
# def myFunc():
#     print("called myFunc")
# myFunc()

# Beim Aufruf müssen die Argumente und die Parameterliste passen!
# Hinweis: *args, **kwargs -> später
def myFunc(name):
    print(name)
    return 42

print(myFunc('Hugo'))
# print(myFunc('Hugo', 'Emil')) # Fehler

# Überladen von Funktions-Parameter-Listen ist nicht möglich, eine Re-Deklaration überschreibt die ursprüngliche Definition komplett
def myFunc(name, name2):
    print(name + name2)
    return 42


#print(myFunc('Hugo'))# Fehler
print(myFunc('Hugo', 'Emil')) 
