import pandas as pd

df = pd.read_csv('books.csv', index_col='ISBN')

#x = df.loc
#x[3:7, ['Title', 'Price']]
#df.loc[3:7, ['Title', 'Price']]

#l = [1,2,3,4]
#l[1:3] = 666
#print(l)
print(df.loc['ISBN-2', 'Price'])
print(df.iloc[1:3])
