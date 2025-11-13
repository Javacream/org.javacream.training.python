start = input(f'please enter the start number: ')
end = input(f'please enter the end number: ')

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

