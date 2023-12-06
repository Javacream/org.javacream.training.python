def main():
    names = ['Hugo', 'Emil', "Hannah"]
    # Filtere alle Namen, die mit 'H' beginnen

    # Klassisch (untypisch, aber möglich)
    result = list()
    for name in names:
        if name.startswith('H'):
            result.append(name)
    print(result)

    # comprehension
    comprehension_result = [name for name in names if name.startswith('H')]
    print(comprehension_result)

    # Filtere alle Namen, die mit 'H' beginnen und transformiere das Ergebnis in die Länge des Namens

    # Klassisch (untypisch, aber möglich)
    result = list()
    for name in names:
        if name.startswith('H'):
            result.append(len(name))
    print(result)

    # comprehension
    comprehension_result = [len(name) for name in names if name.startswith('H')]
    print(comprehension_result)

    # Filtere alle Namen, die mit 'H' beginnen und transformiere das Ergebnis in Upper Case

    # Klassisch (untypisch, aber möglich)
    result = list()
    for name in names:
        if name.startswith('H'):
            result.append(name.upper())
    print(result)

    # comprehension
    comprehension_result = [name.upper() for name in names if name.startswith('H')]
    print(comprehension_result)

    # comprehension, ein ziemlich theoretisches Beispiel
    comprehension_result = ['OK' for name in names if name.startswith('H')]
    print(comprehension_result)


main()