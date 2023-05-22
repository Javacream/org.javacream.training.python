import numpy as np


list1 = [0,1,2,3]
list2 = [9,8,7,6]
list3 = [5,2,1,6]

np2dArray = np.array([list1, list2, list3])

#print(np2dArray)

## Elementzugriff
print(np2dArray[1,2])

## Slicing
print(np2dArray[1:2])


#ToDo
## Variieren Sie die Syntax des Slice- und Element-Zugriffs!