import pandas as pd

def main():
    df = pd.read_csv('data_analysis/diamonds.csv')

    def explore():
        print(df.info())
        print(df.head())
    #    print(df.dtypes)
    #    print(df.size)
    #    print(df.columns)
        print(df.isna().sum())

    def visualize():
        pass
    explore()

main()