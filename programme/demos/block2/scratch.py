counter = 0
condition = counter < 10
#while condition: # Das ist eine Endlosschleife
#    print(counter)

#while condition: # Das ist immer noch eine eine Endlosschleife
#    condition = counter < 10
#    print(counter)


while condition:
    condition = counter < 10
    print(counter)
    counter = counter + 1

while counter < 10:
    print(counter)
#    counter = counter + 1
    counter +=1 # Eine häufig genutzte Verkürzung
    #counter++ # Ein Inkrement um 1, unterstützt in vielen Programmiersprache    


start = 42
end_exclusive = 47
index = start
while index < end_exclusive:
    print(index)
    index += 1

