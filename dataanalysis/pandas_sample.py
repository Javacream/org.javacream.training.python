import pandas as pd

def main():
    df = pd.read_csv('./covid_data.csv')
    print(df.describe())
main()
