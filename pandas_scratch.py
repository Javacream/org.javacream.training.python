import pandas as pd

df = pd.read_csv('books.csv')

# Rename einer Column
renamed_df = df.rename(columns={'ISBN': 'isbn', 'Title': 'title', 'Price': 'books_price'})
print(renamed_df)

df.rename(columns={'ISBN': 'isbn', 'Title': 'title', 'Price': 'books_price'}, inplace=True)
print(df)
