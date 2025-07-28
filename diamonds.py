import pandas as pd

def main():
    df = pd.read_csv('diamonds.csv')
    print(df.head())
    print(df.info())
    print(df.describe())
main()