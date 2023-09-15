import pandas as pd

def explore(df):
    print(df.info())
    print(df.head())
#    print(df.dtypes)
#    print(df.size)
#    print(df.columns)
    print(df.isna().sum())

def main():
    df = pd.read_csv('data_analysis/diamonds.csv')
    explore(df)

main()