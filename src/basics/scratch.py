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

#Todo: Zeichnen Sie ein Stack-Heap-Diagramm und machen Sie sich daran das Verhalten des Programms klar
#Frage: Arbeitet Python mit Call By Value oder einem Call by Reference? 
#Recherche: Wie kann dieses Verhalten geändert werden? Hinweis: Gar nicht...
