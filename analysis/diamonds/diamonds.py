import pandas as pd

def main():
    df = pd.read_csv('analysis/diamonds/diamonds.csv')
    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.to_json('analysis/diamonds/diamonds_app.json', orient="records", indent=4)
if __name__ == '__main__': 
    main()