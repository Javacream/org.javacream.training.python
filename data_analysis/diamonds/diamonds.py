import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

root = 'data_analysis/diamonds'
df = pd.read_csv(f'{root}/diamonds.csv')

to_rename = 'Unnamed: 0'
df.rename(columns={to_rename: 'id'}, inplace=True)
df.set_index('id', inplace=True)

categorical_columns = ['cut', 'color', 'clarity']
for column in categorical_columns:
    df[column] = pd.Categorical(df[column])

invalid_table_data = ~df['table'].astype(str).str.replace('.', '').astype(str).str.isnumeric()
df.loc[invalid_table_data, 'table'] = 0
df['table'] = df['table'].astype(float)

columns = df.select_dtypes(include='number').columns
for column in columns:
    if (df[column] < 0).sum() > 0:
        df[column] = df[column].abs()

df.to_json(f'{root}/diamonds.json', orient='records', indent=2)


