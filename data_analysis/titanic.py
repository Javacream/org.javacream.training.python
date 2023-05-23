import os
import numpy as np
import pandas as pd

def main():
    def explore(dataFrame):
        #print(dataFrame.shape)
        #print(dataFrame.dtypes)
        #print(dataFrame.head())
        #print(dataFrame.info())
        #print(dataFrame.describe()) #-> in der explore Phase zu früh!
        #categoricalColumnNames = dataFrame.dtypes[dataFrame.dtypes == 'object'].index
        #print(dataFrame[categoricalColumnNames].describe())
        #print(dataFrame['Ticket'].head(15))
        #print(dataFrame['Ticket'].describe())
        #print(dataFrame['Cabin'].describe())
        #print(dataFrame['Cabin'].head(15))
        #pass
        #print(dataFrame['Pclass'].describe())
        print(dataFrame['Pclass'].head(15))
    def cleanup(dataFrame):
        # PassengerId ist redundant, ist der eh vorhandene Index
        del dataFrame['PassengerId']
        del dataFrame['Ticket']
        categorizedSurvival = pd.Categorical(dataFrame["Survived"])
        categorizedSurvival = categorizedSurvival.rename_categories(['died', 'survived'])
        print(categorizedSurvival.describe())
        dataFrame["Survived"] = categorizedSurvival
        print(dataFrame.info())
    
    titanicData = pd.read_csv("./titanic.csv")
    explore(titanicData)
    cleanup(titanicData)
main()

