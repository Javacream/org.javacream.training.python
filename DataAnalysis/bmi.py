import pandas as pd

df = pd.read_csv('./DataAnalysis/people.csv')
df['bmi'] = df['weight_kg']/(df['height_cm'] * df['height_cm']) * 10000
df['result'] = df['firstname'] + " " + df['lastname'] + "->" + df['bmi'].astype(str)
df['result'].to_csv('./DataAnalysis/bmi.csv')
df