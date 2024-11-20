start = int(input('Bitte Start eingeben: '))
end = int(input('Bitte Ende eingeben: '))
step = int(input('Bitte Schrittweite eingeben: '))

if (step == 0):
    print(f'Kann nicht mit step=0 iterieren!')    
elif (start < end) and (step < 0) or (start > end) and (step > 0):
    print(f'Ungültige Iteration, kann nicht von {start} bis {end} mit {step} iterieren!')
else:
    counter = start
    if start < end:
        while counter < end:
            print(counter)
            counter += step
    else:
        while counter > end:
            print(counter)
            counter += step