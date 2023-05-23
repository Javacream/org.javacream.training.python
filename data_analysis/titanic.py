import os
import numpy as np
import pandas as pd

def main():
    def explore(dataFrame):
        #print(dataFrame.shape)
        #print(dataFrame.dtypes)
        print(dataFrame.head())
        #print(dataFrame.info())
        #print(dataFrame.describe()) #-> in der explore Phase zu früh!
        categoricalColumnNames = dataFrame.dtypes[dataFrame.dtypes == 'object'].index
        print(dataFrame[categoricalColumnNames].describe())
    titanicData = pd.read_csv("./titanic.csv")
    explore(titanicData)
main()

