# Kontroll-Strukturen

# Keywords if elif else, Einrückungen syntaktisch notwenig

n1 = 2
n2 = 2

if n1 > n2:
    print('n1 greater than n2')
elif n1 < n2:
    print('n2 less n2')
else:
    print('n2 equal n2')

# switch-Anweisung existiert, heißt in Python aber "match"

command = "c1"
#match gibt es erst seit python 3.10
match command:
    case 'c1':
        print ("detected command c1")