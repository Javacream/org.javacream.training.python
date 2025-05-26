# %% [markdown]
# # Die Pandas Bibliothek
# 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %% [markdown]
# ## Lese-Methoden
# 
# ### Lesen einer lokalen CSV-Datei

# %%
df = pd.read_csv('programme/Woche9/pandas/people.csv')
df.head()

# %% [markdown]
# ### Lesen einer lokalen JSON-Datei

# %%
df = pd.read_json('programme/Woche9/pandas/people.json')
df.head()

# %% [markdown]
# ### Lesen eines RESTful WebServices

# %%
df = pd.read_json('http://javacream.eu:8080/people')
df.head()

# %% [markdown]
# ### Lesen einer CSV-Datei vom Internet

# %%
df = pd.read_csv('https://raw.githubusercontent.com/lawlesst/vivo-sample-data/refs/heads/master/data/csv/people.csv')
df.head()

# %% [markdown]
# ### Lesen von Daten aus einer Datenbank

# %%
import mysql.connector

connection = mysql.connector.connect(
    host='javacream.eu', port=3406, username='user', password='user', database='javacream'
)

df = pd.read_sql('select * from PEOPLE', connection)
df.head()



# %% [markdown]
# ## Datenexploration
# 
# * Siehe Diamonds
#   * head, tail
#   * info
#   * describe
# * Neu: Prüfung auf unsaubere Daten
#   * None-Werte
#   * NaN-Werte

# %%
df = pd.read_csv('programme/Woche9/pandas/people.csv')
df.isna()

# %%
df.isna().sum()

# %%
df['Height'].isna()

# %%
df['Height'].isna().sum()

# %% [markdown]
# * Selektion mit dem DataFrame
#   * Wie ein Dictionary selektiert der DataFrame auf Spalten

# %%
df['Height']

# %% [markdown]
# * Selektion mit einem Boolean Vektor

# %%
criterion_vector = df['Height'].isna()
criterion_vector


# %%
df[criterion_vector]

# %%
df[df['Height'].isna()]

# %%
df[df['Height'] > 180]


# %%
df['Name'][(df['Height'] > 180) & (df['Weight'] < 85)]


# %% [markdown]
# ## Cleanup

# %% [markdown]
# ### Droppen von Daten mit NaN

# %%
df.dropna()

# %%
df.dropna(axis=1)


# %% [markdown]
# * Bisher wurde der DataFrame nicht geändert!

# %%
df

# %% [markdown]
# * Änderung des originalen DataFrames mit inplace= True

# %%
df.dropna(inplace=True)
df

# %%
df = pd.read_csv('programme/Woche9/pandas/people.csv')

# %% [markdown]
# ### Füllen der NaN-Werte

# %% [markdown]
# * Fixer Wert

# %%
df.fillna({'Weight': 66.6, 'Height': 177})

# %% [markdown]
# ### Exkurs: Schreiben des DataFrames

# %%
filled = df.fillna({'Weight': 66.6, 'Height': 177})
filled.to_csv('people_filled.csv')

# %% [markdown]
# * Extrapolation der Werte Vorgänger / Nachfolger
#   * Hinweis: Für dieses Beispiel Unsinn

# %%
df.ffill()

# %% [markdown]
# ## Programmlogik mit DataFrames

# %%
df = filled
df['Weight'] + 20

# %%
df['Height'] * .8

# %%
converted = df.astype(str)
converted.info()

# %% [markdown]
# ### Exkurs Python Listen und DataFrames

# %%
df['Height'].to_list()

# %%
names = ['A', 'B', 'C']
names_series = pd.Series(names)
names_series

# %% [markdown]
# * Erzeugen einer neuen Spalte

# %%
df['Hugo'] = 42
df

# %% [markdown]
# * Spalte entfernen

# %%
print(df.columns)
if 'Hugo' in df.columns:
    df.drop('Hugo', axis=1, inplace=True)
df.columns

# %%
df['BMI'] = df['Weight']/(df['Height']/100)** 2
df

# %% [markdown]
# * Zuweisung an eine Selektion, die loc-Eigenschaft

# %%
# df[19, 'Name'] -> Nicht zulässig
df.loc[19, 'Weight'] = 59.8
df.loc[19, 'Weight']

# %%
df['BMI'] > 23

# %%
df.loc[[3, 6, 9], 'Height']

# %%
df.loc[df['BMI'] > 23, ['Name', 'Height']]

# %%
df['BMI_CATEGORY'] = 'normal weight'
df

# %%
df.loc[df['BMI'] > 23, ['Name', 'BMI_CATEGORY']] = 'overweight'
df

# %% [markdown]
# ### "Wegschreiben" der Ergebnisse

# %%
df.to_csv('people_bmi.csv')

# %%
df.hist('BMI')
plt.savefig('bmi_hist.jpg')
# %%
df.boxplot('BMI')
plt.savefig('bmi_boxplot.jpg')


