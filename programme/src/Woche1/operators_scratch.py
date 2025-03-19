lastname = 'Sawitzki'
firstname = 'Rainer'

# Name soll zusammengesetzt sein
name = firstname + ' ' + lastname
print(name)

# Das ist die bessere Alternative
name = f'{firstname} {lastname}'
print(name)

# Sowas geht, Zeichenkette Multiplizieren, aber eher skurril
big_ego = 10*lastname
print(big_ego)

#bmi = 22.4
#print('Der Bmi ist ' + 22.4)

# wrong = lastname - firstname
# wrong = lastname* firstname