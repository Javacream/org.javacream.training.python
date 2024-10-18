import pandas as pd
import matplotlib.pyplot as plt
diamonds_dataframe = pd.read_csv('programme/Woche 9/data_analysis/exploration/diamonds.csv')

#diamonds_dataframe = diamonds_dataframe.drop('Unnamed: 0', axis=
diamonds_dataframe.drop('Unnamed: 0', axis=1, inplace=True)
# print(diamonds_dataframe.head(10))
# print(diamonds_dataframe.tail(4))
# print(diamonds_dataframe.shape)
# print(diamonds_dataframe.info())

diamonds_dataframe.hist(column='carat')
plt.savefig('demo.png')
