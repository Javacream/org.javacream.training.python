import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('diamonds.csv')
    #print(df.head())
    #print(df.info())
    #print(df.describe())
    df['carat'].hist()
    plt.savefig('diamonds_carat.png')
main()