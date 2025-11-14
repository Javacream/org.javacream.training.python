invalid = True
while invalid:
    start = input(f'please enter the start number: ')
    
    if start.isdigit():
        invalid = False
    else:
        print(f'invalid input: {start} is not a number!')
invalid = True
while invalid:
    end = input(f'please enter the end number: ')
    if end.isdigit():
        invalid = False
    else:
        print(f'invalid input: {end} is not a number!')
start = int(start)
end = int(end)

if start == end:
    print(f'cannot count from {start} to {end} if both are equal!')
else:
    if start < end:
        print(f'counting upwards from {start} to {end}')
        counter = start
        while counter <= end:
            print(counter)
            counter += 1
    else:
        print(f'counting downwards from {start} to {end}')
        counter = start
        while counter >= end:
            print(counter)
            counter -= 1

