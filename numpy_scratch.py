import numpy as np

a1 = np.array([[1,1], [2,3]])
a2 = np.array([[4,5], [6,7]])

result = np.concatenate((a1, a2), axis=1) # keine Objektorientierte-Programmierung=OOP -Formulierung
#print(result)
#print(result.shape)

# append: 
#print(np.append(a1, a2))

# vstack und hstack


# print(np.arange(0,9).reshape(3,3).shape)

a = np.arange(0,8)
print(a)
reshaped = a.reshape(2,4)
print(a)
print(reshaped)
a.shape = (4,2)
print(a)