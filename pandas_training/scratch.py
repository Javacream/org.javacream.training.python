import os
import numpy as np
import pandas as pd

# series1 = pd.Series(data=[188, 166, 177, 185], index=['a', 'b', 'h', 'e'])
# series2 = pd.Series(data=['Hugo', 'Emil', 'Fritz', 'Fridolin'], index=['a', 'b', 'h', 'e'])

series1 = pd.Series(data=[188, 166, 177, 185])
series2 = pd.Series(data=['Hugo', 'Emil', 'Fritz', 'Fridolin'])


dataDict = {"height": series1, "name": series2}

print(dataDict)

dataFrame= pd.DataFrame(dataDict)

print(dataFrame)