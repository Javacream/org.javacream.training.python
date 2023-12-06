def main():
    # Liste-Literal, [element1, ...]
    names = ['Hugo', 'Andrea', 'Helga', 'Hugo']
    # anything=  [42, True, 'Egal']
    # Elementzugriff mit [index], index beginnt bei 0
    second_name = names[1]
    print(second_name)
    #out_of_bound = names[42] # Laufzeitfehler
    # negative Indizes beginnen von Hinten, nett, aber nicht essenziell
    x = names[-1]
    y = names[2]
    print(x, y)

    # Die Länge einer Liste wird mit der build-in-Funktion len bestimmt

    print(len(names))

    # Iteration mit while (untypisch for Collections)
    index = 0
    size = len(names)
    while index < size:
        print(names[index])
        index = index + 1

    # Iteration mit for (so ist es viel einfacher)

    for name in names:
        print(name)
    
    if 'Hugo' in names:
        print('names contains "Hugo"')

main()