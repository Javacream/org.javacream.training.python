import pandas as pd

df = pd.read_csv('books.csv', index_col='ISBN')
df2 = pd.read_csv('books2.csv', index_col='ISBN')

#print(df.index.union(df2.index)) # Indizes aus beiden DataFrames aber natürlich ohne Duplikate
print(df.index.symmetric_difference(df2.index))