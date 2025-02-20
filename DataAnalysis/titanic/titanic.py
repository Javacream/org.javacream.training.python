# %% [markdown]
# # Titanic-Datensatz

# %% [markdown]
# ## Laden der einzelnen Datensätze

# %%
import pandas as pd

# %%
titanic_part1_df = pd.read_csv('titanic.csv')
titanic_part1_df.head()

# %%
titanic_part2_incomplete_df = pd.read_csv('titanic_part2_incomplete.csv')
titanic_part2_incomplete_df.head()

# %%
titanic_part2_survival_df = pd.read_csv('titanic_part2_survival.csv')
titanic_part2_survival_df.head()

# %% [markdown]
# ## Mergen der unvollständigen Daten

# %%
titanic_part2_df = pd.merge(titanic_part2_incomplete_df, titanic_part2_survival_df, how='inner', on='PassengerId')
titanic_part2_df.head()

# %% [markdown]
# ## Erzeugen des Gesamtdatensatzes

# %%
df = pd.concat([titanic_part1_df, titanic_part2_df], ignore_index=True)
df

# %% [markdown]
# ## Exploration

# %%
df.shape

# %%
df.info()

# %%
df .describe()

# %%
df.columns

# %%
df['Cabin'].unique()

# %% [markdown]
# * Folgerungen (subjektiv, es ist meine Analyse)
#   * Es gibt Lücken in den Datensätzen
#   * PassengerID ist redundant, wir haben ja bereits den Index
#   * Ticket ist im Wesentlichen ein "Zufallswert" ohne weitere Bedeutung
#   * Survival ist eigentlich ein logischer Wert, 0=Tot, 1=überlebt
#   * Pclass = Passenger Class hat nur die Werte 1st, 2nd, 3rd, ist kategorisch
#   * Sex, Embarked = Zustiegspunkt ebenfalls eine kategorische Variable
#   * Cabin hat einen interessanten Aufbau, Zeichenkette + Nummer
#   * Parch /Sibsp: Anzahl der Eltern Kinder bzw. Angehörige

# %% [markdown]
# ## Cleanup

# %% [markdown]
# * Lücken in den Daten werden behoben
#   * Alter wird durch das mittlere Passagier-Alter ersetzt
#   * Embarked 'Unknown'
# * Die Spalten PassengerID und Ticket sind unnötig
# * Survival durch eine logische Spalte ersetzen oder als eine kategorische Variable definieren
# * Pclass muss categorial sein
# * Sex, Embarked, ebenfalls categorial machen
# * Cabin wird in 2 neue Spalten zerlegt: Bereich der Titanic (Anfangsbuchstabe) und die Kabinennummer als Ganzzahl

# %% [markdown]
# ### Löschen der überflüssigen Spalten

# %%
df.drop('PassengerId', axis=1, inplace=True)
df.drop('Ticket', axis=1, inplace=True)


# %% [markdown]
# ### Setzen eines unbekannten Alters auf das Durchschnittsalter
# * Erweiterung: Durchschnittsalter für Frauen und Männer getrennt

# %%
df.loc[(df['Sex'] == 'female') & (df['Age'].isnull())]

# %%
male_mean_age = df[df['Sex'] == 'male']['Age'].mean()
female_mean_age = df[df['Sex'] == 'female']['Age'].mean()

df.loc[(df['Sex'] == 'female') & (df['Age'].isnull()), 'Age'] = female_mean_age
df.loc[(df['Sex'] == 'male') & (df['Age'].isnull()), 'Age'] = male_mean_age


# %% [markdown]
# ### Setzen unbekannter Zustiegspunkte

# %%
df.loc[df['Embarked'].isnull(), 'Embarked'] = 'U'


# %% [markdown]
# ### Erstellung der Categorial Columns

# %% [markdown]
# ### Überlebt

# %%
surviced_categorical_series = pd.Categorical(df['Survived'])
surviced_categorical_series = surviced_categorical_series.rename_categories(['died', 'survived'])
df['Survived'] = surviced_categorical_series
df.info()

# %% [markdown]
# ### Embarked, Sex, Pclass

# %%
df['Sex'] = pd.Categorical(df['Sex'])
df['Pclass'] = pd.Categorical(df['Pclass']).rename_categories({1: 'First', 2: 'Second', 3: 'Third'})
stations = {'S': 'Southhampton', 'C': 'Cherbourg', 'Q': 'Queenstown', 'U': 'Unknown'}
embarked_categorical = pd.Categorical(df['Embarked']).rename_categories(stations)
df['Embarked'] = embarked_categorical

# %% [markdown]
# ### Split der Kabineninformation, Extrahieren des Bereichs im Schiff

# %%
df.loc[df['Cabin'].isna(), 'Cabin'] = 'Z'
cabin_area = [cabin[0] for cabin in df['Cabin']]
cabin_area_series = pd.Series(cabin_area)
df['Cabin'] = pd.Categorical(cabin_area_series)

# %% [markdown]
# ### Endergebnis

# %%
df.info()

# %%
df

# %% [markdown]
# ## Datenanalyse und -visualisierung

# %% [markdown]
# * Datenverarbeitung dieser Daten "wie üblich" mit Erzeugen einer Ergebnis-Datei
#   * "Ich hätte gerne eine Liste aller Passagiere, die in Southhampton eingestiegen sind, über dreissig Jahre, überlebt"
#   * Mittelwert des Alters der Passagiere
#   * Mittelwert des Alters der Passagiere, die überlebt haben
#   * ...

# %%



