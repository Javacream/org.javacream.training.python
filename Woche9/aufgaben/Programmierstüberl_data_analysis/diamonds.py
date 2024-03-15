import numpy as np
import pandas as pd
import matplotlib

print(pd, np, matplotlib)


diamonds_dataframe = pd.read_csv('Woche9/aufgaben/Programmierstüberl_data_analysis/diamonds.csv')
diamonds_dataframe = diamonds_dataframe.drop('Unnamed: 0', axis=1)

print(diamonds_dataframe.head(5))

print(diamonds_dataframe.shape)

# ToDo: Speichern als png
diamonds_dataframe.hist(column="carat", bins=15, color="green", range=(0, 3.5))

print(diamonds_dataframe[diamonds_dataframe["carat"] > 3.5])



