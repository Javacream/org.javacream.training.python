import os
import numpy as np
import pandas as pd

df = pd.read_csv("./titanic.csv")
df.index = df['PassengerId']
#print(df.shape)
#print(df.head())
#print(df.head())
#print(df.index[0:3])
#print(df.columns)
#print(df.info())
#print(df.describe())