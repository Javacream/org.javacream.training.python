import pandas as pd
import matplotlib.pyplot as plt
def main():
    df = pd.read_csv('./covid_data.csv')
    print(df.describe())
    df.hist(column='normalized deaths', bins=100)
    plt.savefig("convid.png")
main()
