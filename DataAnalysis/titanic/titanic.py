import pandas as pd

titanic_part1_df = pd.read_csv('./DataAnalysis/titanic/titanic.csv')
titanic_part1_df.head()

titanic_part2_incomplete_df = pd.read_csv('./DataAnalysis/titanic/titanic_part2_incomplete.csv')
titanic_part2_incomplete_df.head()

titanic_part2_survival_df = pd.read_csv('./DataAnalysis/titanic/titanic_part2_survival.csv')
titanic_part2_survival_df.head()

titanic_part2_df = pd.merge(titanic_part2_incomplete_df, titanic_part2_survival_df, how='inner', on='PassengerId')
titanic_part2_df.head()

df = pd.concat([titanic_part1_df, titanic_part2_df], ignore_index=True)
df

df.shape

df.info()

df .describe()

df.columns

df['Cabin'].unique()

df.drop('PassengerId', axis=1, inplace=True)
df.drop('Ticket', axis=1, inplace=True)


df.loc[(df['Sex'] == 'female') & (df['Age'].isnull())]

male_mean_age = df[df['Sex'] == 'male']['Age'].mean()
female_mean_age = df[df['Sex'] == 'female']['Age'].mean()

df.loc[(df['Sex'] == 'female') & (df['Age'].isnull()), 'Age'] = female_mean_age
df.loc[(df['Sex'] == 'male') & (df['Age'].isnull()), 'Age'] = male_mean_age


df.loc[df['Embarked'].isnull(), 'Embarked'] = 'U'



surviced_categorical_series = pd.Categorical(df['Survived'])
surviced_categorical_series = surviced_categorical_series.rename_categories(['died', 'survived'])
df['Survived'] = surviced_categorical_series
df.info()

df['Sex'] = pd.Categorical(df['Sex'])
df['Pclass'] = pd.Categorical(df['Pclass']).rename_categories({1: 'First', 2: 'Second', 3: 'Third'})
stations = {'S': 'Southhampton', 'C': 'Cherbourg', 'Q': 'Queenstown', 'U': 'Unknown'}
embarked_categorical = pd.Categorical(df['Embarked']).rename_categories(stations)
df['Embarked'] = embarked_categorical

df.loc[df['Cabin'].isna(), 'Cabin'] = 'Z'
cabin_area = [cabin[0] for cabin in df['Cabin']]
cabin_area_series = pd.Series(cabin_area)
df['Cabin'] = pd.Categorical(cabin_area_series)

df.info()

df


import matplotlib.pyplot as plt
df.hist('Age')
plt.savefig('age_hist.png')


df.hist(color = 'red')
plt.savefig('age_hist_red.png')

df.hist('Age', bins=10, by='Pclass')

df.boxplot()