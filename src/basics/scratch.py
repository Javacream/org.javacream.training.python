myList = ['A', 'B', 'C']
print(myList)
def changeList():
    #global myList
    myList = [1,2,3]
    myList[2] = "ALSO CHANGED"
    print(myList)
    return myList

changeList()
print(myList)
myList = changeList()
print(myList)

