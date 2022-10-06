myList = ['Hugo', 'Emil', 'Hugo']

for name in myList:
    print(name)

hugo = myList[0]
print(hugo)


myList[0] = "Fritz" #Fehler, schreibender Zugriff it nicht möglich
print(myList[0])

#print(myList[3]) # Fehler

#myList[3] = 'fritz' #Fehler -> List-Methode ermöglicht dies
#print(myList[3])

myList = ('Sawitzki', 183, 'm', True)