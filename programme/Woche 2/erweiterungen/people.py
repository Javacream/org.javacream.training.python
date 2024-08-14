people = [['Sawitzki', 'Rainer'], ['Muster', 'Hannah'], ['Schneider', 'Andrea']]

index = 1
for person in people:
    print(f'{index}. Person:')
    innerindex = 1
    for name in person:
        if innerindex == 1:
            lastname = name
        else:
            firstname = name
        innerindex += 1        
    print(f'    {firstname} {lastname}')
    index += 1