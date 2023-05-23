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
        #print(dataFrame['Pclass'].describe())
        #print(dataFrame['Embarked'].describe())
        #print(dataFrame['Cabin'].unique())
        pass
    def cleanup(dataFrame):
        # PassengerId ist redundant, ist der eh vorhandene Index
        del dataFrame['PassengerId']
        del dataFrame['Ticket']
        categorizedSurvival = pd.Categorical(dataFrame["Survived"])
        categorizedSurvival = categorizedSurvival.rename_categories(['died', 'survived'])
        dataFrame["Survived"] = categorizedSurvival
        categorizedSex = pd.Categorical(dataFrame["Survived"])
        categorizedSex = categorizedSex.rename_categories({'male': 'Male', 'female': 'Female'})
        dataFrame["Sex"] = categorizedSex
        categorizedEmbarked = pd.Categorical(dataFrame["Embarked"])
        categorizedEmbarked = categorizedEmbarked.rename_categories(new_categories= {'S': 'Southhampton', 'C': 'Cherbourg', 'Q':'Queenstown'})
        dataFrame["Embarked"] = categorizedEmbarked
        categorizedPclass = pd.Categorical(dataFrame["Pclass"])
        categorizedPclass = categorizedPclass.rename_categories(new_categories= {0: 'First', 1: 'Second', 2:'Third'})
        dataFrame["Pclass"] = categorizedPclass

        cabinDataAsString = dataFrame["Cabin"].astype('str')
        corePythonCabinList = [cabin[0] for cabin in cabinDataAsString]
        numpyCabinArray = np.array(corePythonCabinList) 
        categorizedCabin = pd.Categorical(numpyCabinArray)
        dataFrame["Cabin"] = categorizedCabin
        print(dataFrame['Cabin'].unique())

        #print(dataFrame.info())

    titanicData = pd.read_csv("./titanic.csv")
    explore(titanicData)
    cleanup(titanicData)
main()

