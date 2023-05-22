import numpy as np


list1 = [0,1,2,3]
list2 = [9,8,7,6]
list3 = [5,2,1,6]

corePythonArray = [list1, list2, list3]

def flattenCorePython(list):
    result = []
    [result.append(sublist) for sublist in list]
    return result

print(flattenCorePython(corePythonArray))
