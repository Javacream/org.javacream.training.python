import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv("mtcars.csv")
mtcars =  mtcars.rename(columns={'Unnamed: 0': 'model'})
mtcars.index = mtcars.model
del mtcars["model"]
mtcars.va
print(mtcars.head())