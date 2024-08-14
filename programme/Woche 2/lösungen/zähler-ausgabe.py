START = 0
END = 10
STEP = 1

counter = START
while counter < END:
    counter += STEP
    if counter == 3:
        continue
    print(counter)
