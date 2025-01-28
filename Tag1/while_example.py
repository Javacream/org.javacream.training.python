start = input('Bitte die Startzahl eingeben: ')
end = input('Bitte die Endzahl eingeben (muss größer als der Start sein!): ')
step = input('Bitte die Schrittweite eingeben: ')

start = int(start)
end = int(end)
step = int(step)

index = start

if end > start:
    if step > 0:
        while index < end:
            print(index)
            index = index + step
    else:
        print(f'cannot loop with {start}, {end}, {step}, looping would be endless')
else:
    if step < 0:
        while index > end:
            print(index)
            index = index + step
    else:
        print(f'cannot loop with {start}, {end}, {step}, looping would be endless')

