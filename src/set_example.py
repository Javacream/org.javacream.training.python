def main():
    # Set-Literal, {element1, ...}
    names = {'Hugo', 'Andrea', 'Helga', 'Hugo'}
    # Elementzugriff mit [index] nicht bei Set, ein Set hat keine innere Ordnung
#    second_name = names[1]
#    print(second_name)
    #out_of_bound = names[42] # Laufzeitfehler
    # negative Indizes beginnen von Hinten, nett, aber nicht essenziell
#    x = names[-1]
#    y = names[2]
#    print(x, y)

    # Die Länge des Sets wird mit der build-in-Funktion len bestimmt

    print(len(names))

    # Iteration mit while (untypisch for Collections)
#    index = 0
#    size = len(names)
#    while index < size:
#        print(names[index])
#        index = index + 1

    # Iteration mit for (so ist es viel einfacher)

    for name in names:
        print(name)
    
    if 'Hugo' in names:
        print('names contains "Hugo"')

main()