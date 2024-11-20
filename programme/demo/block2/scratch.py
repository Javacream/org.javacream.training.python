# # Endlos-Schleife
# condition = True
# while condition:
#     pass

# Von-bis-Schleife

start = 0
counter = start
end = 5
# condition = counter < end: Hier wird die Bedingung nur einmal geprüft -> True -> Endlos
while counter < end:
    # pass # Nicht vergessen: counter hochzählen -> Endlos
    print(f'{counter}')
    #counter = counter + 1
    counter += 1
    #counter++ # in Python gibt es kein PlusPlus

counter = 0
while True:
    counter += 1
    print(f'{counter}')
    if counter >= 5:
        break
counter = 0
while counter < 5:
    print(f'{counter}')
    counter += 1
    if counter % 2:
        continue
    print('nächster Durchlauf')

