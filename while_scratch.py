again = True
# endless loop
#while again:
#    print('in loop')

counter = 0
while again:
    if counter < 5:
        print(counter)
        counter += 1
    else:
        again = False