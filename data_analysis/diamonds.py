import pandas as pd
import matplotlib.pyplot as plt
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
        df.hist(column='carat', color="green")
        plt.savefig("carat_hist.png")
    explore()
    visualize()

main()