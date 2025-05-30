counter = 0
while counter < 10:
    counter +=1
    if counter % 2 == 0:
        print(counter)
    else:
        continue # im Endeffekt zurück zu Zeile 2
    print("Eine Zahl wurde ausgegeben")