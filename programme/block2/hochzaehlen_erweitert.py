again = True
while (again):
    start = int(input ('Bitte Startwert eingeben: '))
    end = int(input ('Bitte Endwert eingeben: '))
    step = int(input ('Bitte Inkrement eingeben: '))

    output = ''
    index = start
    while index < end:
        output += f'{index},'
        index += step
    print(output)
    again_input = input ('Nochmal? (j|n)')
    if (again_input == 'n'):
        again = False