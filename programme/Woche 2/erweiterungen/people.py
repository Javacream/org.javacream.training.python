people = [['Sawitzki', 'Rainer'], ['Muster', 'Hannah'], ['Schneider', 'Andrea']]

index = 1
for person in people:
    print(f'{index}. Person:')
    for name in person:
        print(f'    {name}')
    index += 1