names = ['Hugo', 'Andrea', "Walther", "Emil"]

names.sort()
print(names)
names.sort(reverse=True)
print(names)

# Sortieren nach der Länge der Namen:
names.sort(key = lambda name: len(name))
print(names)

# Sortieren nach dem zweiten Buchstaben des Namen:
names.sort(key = lambda name: name[1])
print(names)

# Lösung ohne Lambdas

def string_length(s):
    return len(s)

def second_char_of_string(s):
    return s[1]

names.sort(key = string_length) # KEINE RUNDEN KLAMMERN, WIR ÜBERGEBEN DIE REFERENZ AUF DIE FUNKTION
print(names)

names.sort(key = second_char_of_string) # KEINE RUNDEN KLAMMERN, WIR ÜBERGEBEN DIE REFERENZ AUF DIE FUNKTION
print(names)

names.sort(key = len) # KEINE RUNDEN KLAMMERN, WIR ÜBERGEBEN DIE REFERENZ AUF DIE FUNKTION
print(names)
