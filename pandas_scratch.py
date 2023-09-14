import pandas as pd

df = pd.read_csv('books.csv', index_col='ISBN')

#selection = [False]*df.index.size
#selection[66] = True

#print(df[selection])

#selection = df['Price'] > 95
#print(df[selection])

result = df[df['Price'] > 95]
print(result)