import os
import numpy as np
import pandas as pd

def main():
    def explore(dataFrame):
        pass
    def cleanup(dataFrame):
        del dataFrame['PassengerId']
        del dataFrame['Ticket']
        dataFrame.loc[dataFrame["Age"].isnull(),"Age"] = 42.2
        dataFrame.loc[dataFrame["Embarked"].isnull(),"Embarked"] = "U"

        categorizedSurvival = pd.Categorical(dataFrame["Survived"])
        categorizedSurvival = categorizedSurvival.rename_categories(['died', 'survived'])
        dataFrame["Survived"] = categorizedSurvival
        categorizedSex = pd.Categorical(dataFrame["Survived"])
        categorizedSex = categorizedSex.rename_categories({'male': 'Male', 'female': 'Female'})
        dataFrame["Sex"] = categorizedSex
        categorizedEmbarked = pd.Categorical(dataFrame["Embarked"])
        categorizedEmbarked = categorizedEmbarked.rename_categories(new_categories= {'S': 'Southhampton', 'C': 'Cherbourg', 'Q':'Queenstown', 'U': "Unknown"})
        dataFrame["Embarked"] = categorizedEmbarked
        categorizedPclass = pd.Categorical(dataFrame["Pclass"])
        categorizedPclass = categorizedPclass.rename_categories(new_categories= {0: 'First', 1: 'Second', 2:'Third'})
        dataFrame["Pclass"] = categorizedPclass

        cabinDataAsString = dataFrame["Cabin"].astype('str')
        corePythonCabinList = [cabin[0] for cabin in cabinDataAsString]
        numpyCabinArray = np.array(corePythonCabinList) 
        categorizedCabin = pd.Categorical(numpyCabinArray)
        dataFrame["Cabin"] = categorizedCabin

    titanicData = pd.read_csv("./titanic.csv")
    explore(titanicData)
    cleanup(titanicData)
main()

