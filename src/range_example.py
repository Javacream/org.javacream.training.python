def main():
    # Es gibt kein range-Literal, statt dessen wird die range-Funktion benutzt
    interval = range(1, 10, 2) # start, stop, optional: step, default ist 1
    # anything=  [42, True, 'Egal']
    # Elementzugriff mit [index], index beginnt bei 0
    second_element = interval[1]
    print(second_element)
    #out_of_bound = names[42] # Laufzeitfehler
    # negative Indizes beginnen von Hinten, nett, aber nicht essenziell
    x = interval[-1]
    y = interval[2]
    print(x, y)

    # Die Länge eines Tuples wird mit der build-in-Funktion len bestimmt

    print(len(interval))

    # Iteration mit while (untypisch for Collections)
    index = 0
    size = len(interval)
    while index < size:
        print(interval[index])
        index = index + 1

    # Iteration mit for (so ist es viel einfacher)

    for name in interval:
        print(name)
    
    if 'Hugo' in interval:
        print('names contains "Hugo"')

   # Iteration über einen Wertebereich typisch in Python
    for number in range (1,4):
        print(number)

main()