# Endlosschleife, nur als Demo!

# while True:
#     counter = 0
#     counter = counter + 1

# Variationen einer Schleife von 1 bis 5

# Hochzählen eines Zählers
counter = 0
while True:
    counter = counter + 1
    print(f'while with break: actual counter: {counter}')
    if counter == 5:
        break
# Verändern einer Condition

condition = True
counter = 0
while condition:
    counter += 1 # Identisch zu counter = counter + 1
    print(f'while with condition: actual counter: {counter}')
    if counter == 5:
        condition = False

# Prüfen der Condition im Kopf der while-Schleife

counter = 0
while counter < 5:
    counter += 1 # Identisch zu counter = counter + 1
    print(f'standard while: actual counter: {counter}')


# Abbruch eines Schleifendurchlaufs mit continue    

counter = 0
while counter < 5:
    counter += 1 # Identisch zu counter = counter + 1
    if counter % 2 == 1:
        continue
    print(f'standard while with continue: actual counter: {counter}')

# nicht unterstützt in Python
# for counter = 0; counter < 5; counter += 1:
#     print(counter)
