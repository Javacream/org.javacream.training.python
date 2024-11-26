end = int(input ('Bitte Ganzzahl eingeben: '))
squares = dict()
for n in range(1, end + 1):
    squares[n] = n*n

print(squares)