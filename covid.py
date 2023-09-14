import pandas as pd

def cleanup(df):
    df.drop(['day', 'month', 'year'], axis = 1, inplace=True) # axis = 1: Spalten löschen, axis = 0: Zeilen nach Index-Wert löschen
def explore(df):
    print(df.head())
    print(df.dtypes)
    print(df.size)
    print(df.columns)
def analyse(df):
    normalized_deaths = df['deaths'] / df['population']
    df['normalized deaths'] = normalized_deaths
    df['normalized cases'] = df['cases'] / df['population']
    df.to_csv("covid_data.csv")
    with open('means.txt', 'w') as file:
        file.write("Deaths worldwide: " + str(df['deaths'].mean()) + "\n")
        file.write("Cases worldwide: " + str(df['cases'].mean()) + "\n")
        for continent in df['continent'].unique():
            selection = df['continent'] == continent
            file.write("Deaths " + continent + ": " + str(df[selection]['deaths'].mean()) + "\n")
            file.write("Cases " + continent + ": " + str(df[selection]['cases'].mean()) + "\n")

def main():
    covid_data_file = input("Enter convid data file: ")
    if (covid_data_file == ""):
        covid_data_file = "subset-covid-data.csv"
    data_frame = pd.read_csv(covid_data_file)
    explore(data_frame)
    cleanup(data_frame)
    analyse(data_frame)
main()