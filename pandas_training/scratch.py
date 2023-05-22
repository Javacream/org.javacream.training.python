import os
import numpy as np
import pandas as pd

# series1 = pd.Series(data=[188, 166, 177, 185], index=['a', 'b', 'h', 'e'])
# series2 = pd.Series(data=['Hugo', 'Emil', 'Fritz', 'Fridolin'], index=['a', 'b', 'h', 'e'])

data1 = [188, 166, 177, 185]
data2 = ['Hugo', 'Emil', 'Frida', 'Helga']
data3 = ['m', 'd', 'f', 'f']


dataDict = {"height": data1, "name": data2, "gender": data3}

dataFrame= pd.DataFrame(dataDict, index=dataDict['name'])

dataFrame["weight"] = [81, 54, 66, 64]

dataFrame["numberOfEyes"] = 2

calculated = dataFrame.height < 180
print(dataFrame.loc[calculated])
# Typisches Idiom zur Selektion von Daten
print(dataFrame.loc[dataFrame.height < 180])

