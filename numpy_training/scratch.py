import numpy as np


list1 = [0,1,2,3]
list2 = [9,8,7,6]
list3 = [5,2,1,6]

np2dArray = np.array([list1, list2, list3])

#print(np.zeros(shape = [2,3]))
#print(np.ones(shape = [2,3]))
#print(np.identity(3))

# Reshaping
print(np2dArray.shape)

print(np2dArray.flatten())


reshaped = np.reshape(a=np2dArray, newshape=(4,3), order="F")
print(reshaped)

print(np.flipud(np2dArray))
