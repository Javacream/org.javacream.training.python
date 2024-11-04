name = input('Bitte Namen eingeben: ')
age = input('Bitte Alter eingeben: ') # input liefert IMMER eine Zeichenkette zurück

# out_message = name + " ist " + age + " Jahre alt"
out_message = f'{name} ist {age} Jahre alt'
print(out_message)