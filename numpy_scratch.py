import numpy as np

list2d = [[1,2,3], [4,5,7]] # Ein Core Python Array
array2d = np.array(list2d)

array = np.arange(0, 9)
# Andere Funktionen zum Erzeugen, z.B.
#array = np.zeros((2,3)) # ones, empty, ...
reshaped_array = array.reshape(3,3)
re_reshaped_array = reshaped_array.reshape(1,9)
# print(array, reshaped_array, re_reshaped_array)
print(array2d.shape)
# Diemnsionen in numPy werden as Achsen, axis bezeichnet



list3d = [[[1,9],[2,9]], [[4,9],[5,9]]]
print(np.array(list3d).shape)

print(array[0])

list2d_1 = [[1,9],[2,9]]
list2d_2 = [[4,9],[5,9]]
list3d = [list2d_1, list2d_2]