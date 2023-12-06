def main():
    # Set-Literal, {element1, ...}
    names = {'Hugo', 'Andrea', 'Helga', 'Hugo'}

    # Die Länge des Sets wird mit der build-in-Funktion len bestimmt

    print(len(names))

    # Iteration mit for (so ist es viel einfacher)

    for name in names:
        print(name)
    
    if 'Hugo' in names:
        print('names contains "Hugo"')

main()