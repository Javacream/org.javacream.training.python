# 1 bis 10

counter = 1
while counter <=10:
    print(counter)
    counter += 1

counter = 1
while True:
    print(counter)
    counter += 1
    if (counter ==11):
        break

counter = 0
while counter <10:
    counter += 1
    if counter % 2 == 1:
        continue
    print(counter)
