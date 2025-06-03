text = """
Die Obsternte zählt zu den schönsten Zeiten im Gartenjahr. 
Wenn im Spätsommer und Herbst die Früchte an Bäumen und Sträuchern reifen, beginnt die Erntezeit. 
Äpfel, Birnen, Pflaumen, Zwetschgen, Kirschen oder Mirabellen – 
jede Obstsorte hat ihren eigenen Reiz und Geschmack. 
Viele Familien, Hobbygärtner und Landwirte freuen sich auf diesen Moment, 
wenn sie die Früchte ihrer Arbeit in den Händen halten.
Frisch geerntetes Obst ist nicht nur besonders aromatisch, sondern auch reich an Vitaminen. 
Zudem lässt es sich vielfältig verwenden: für Marmelade, Kompott, Kuchen 
oder einfach pur als gesunder Snack. 
Die Obsternte verbindet Natur, Genuss und Tradition.
"""

# Großbuchstaben

print(text.upper())

# Kleinbuchstaben

print(text.lower())

# Test Zeichenkette Anfang / Ende

print(text.endswith('ion.\n'))
print(text.startswith('Hugo'))

# Ersetzen

replaced = text.replace('.', '!!!')
print(replaced)

# Zählen

print(text.lower().count('obst'))

while True:
    text = input ('Bitte etwas eingeben: ')
    if text == 'x':
        break
    print(f'{text} ist eine positive ganze Zahl: {text.isnumeric()}')
    without_dots = text.replace('.', '')
    without_sign = without_dots.replace('+', '')
    without_sign = without_sign.replace('-', '')
    print(f'{text} ist eine Zahl: {without_sign.isnumeric()}')

