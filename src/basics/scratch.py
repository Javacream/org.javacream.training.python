# loops

i = 1

# while
while(i < 5):
    print(i)
    i = i + 1
    # i++
    i +=1
else:
    print("end loop")    

#break, continue als Schlüsselwörter existieren

# classic for existiert nicht

#for (i = 0; i < 5; i +=1):
#    print(i)

# Iteration über etwas iterierbares, bisher ist nur eine Zeichenkette iterierbar

for character in 'Hello':
    print(character)