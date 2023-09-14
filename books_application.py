import pandas as pd
import numpy as np
df = pd.read_csv("books.csv")
print(len(df))
print(df.loc[df['ISBN'].duplicated(), 'ISBN'].unique()) # prints the list of duplicated ISBNs, should be ISBN-2 and ISBN-42
cleaned = df.drop_duplicates(['ISBN'], keep=False)
print(len(cleaned))
cleaned.to_csv('cleaned_books.csv')