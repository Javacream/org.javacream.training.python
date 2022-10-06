myList = ['A', 'B', 'C']
myList2 = myList

myList2[1] = 'CHANGED'
print(myList2[1])

#TODO
#Was wird ausgegeben bei print(myList[1])?
#Schreiben Sie eine Funktion mit einem Parameter, dem Sie eine Liste übergeben und ändern in der Funktion einen Wert der Liste

def changeList(l):
    l[2] = "ALSO CHANGED"

print(myList[2])
changeList(myList)
print(myList[2])
