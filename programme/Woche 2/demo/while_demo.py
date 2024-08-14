counter = 0
constraint  = counter < 10
while constraint:
    counter += 1
    constraint  = counter < 10
    print(f'counter: {counter}')

print("Finish")
