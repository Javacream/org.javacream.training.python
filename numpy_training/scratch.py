import numpy as np


list1 = [0,0.3,2,3]
list2 = [9,8,7,6]

np1dArray = np.array(list1)
np2dArray = np.array([list1, list2])

print(np2dArray.shape)
print(np1dArray.shape)

npVector = np1dArray
npMatrice = np2dArray

print(np1dArray.dtype)