import os
import numpy as np
import pandas as pd

frame = pd.Series(data=[2.4,3,4,5], index=['a', 'b', 'h', 'e'])
print(frame)

frame2 = pd.Series({'a': 2.4, 'b': 3, 'h': 4, 'e': 5})
print(frame2)

frame3 = pd.Series(data=[2.4,3,4,5])


#print(frame3['a'])
print(frame3[0])

# Slicen
print(frame3[1:2])

print(frame['b':'e'])

# Mathematische Operationen

frame4 = pd.Series({'a': 1, 'b': 2, 'h': 3, 'e': 4})
print(frame  + frame4)

frame5 = pd.Series({'a': 1, 'b': 2, 'x': 3, 'y': 4})

print(frame  - frame4)



