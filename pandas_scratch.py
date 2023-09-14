import pandas as pd

df = pd.read_csv('books.csv', index_col='ISBN')

print(df.dtypes)

print(df.tail(1))