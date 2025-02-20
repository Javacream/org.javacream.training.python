import pandas as pd
import matplotlib.pyplot as plt
directory = './DataAnalysis/titanic'
def load_data():
    titanic_part1_df = pd.read_csv(f'{directory}/titanic.csv')
    titanic_part1_df.head()

    titanic_part2_incomplete_df = pd.read_csv(f'{directory}/titanic_part2_incomplete.csv')
    titanic_part2_incomplete_df.head()

    titanic_part2_survival_df = pd.read_csv(f'{directory}/titanic_part2_survival.csv')
    titanic_part2_survival_df.head()

    titanic_part2_df = pd.merge(titanic_part2_incomplete_df, titanic_part2_survival_df, how='inner', on='PassengerId')
    df = pd.concat([titanic_part1_df, titanic_part2_df], ignore_index=True)
    return df
def drop_columns(raw_data):
    raw_data.drop('PassengerId', axis=1, inplace=True)
    raw_data.drop('Ticket', axis=1, inplace=True)
    return raw_data
def fill_missing_ages(raw_data):
    male_mean_age = raw_data[raw_data['Sex'] == 'male']['Age'].mean()
    female_mean_age = raw_data[raw_data['Sex'] == 'female']['Age'].mean()

    raw_data.loc[(raw_data['Sex'] == 'female') & (raw_data['Age'].isnull()), 'Age'] = female_mean_age
    raw_data.loc[(raw_data['Sex'] == 'male') & (raw_data['Age'].isnull()), 'Age'] = male_mean_age
    return raw_data

def create_embarkment_category(raw_data):
    raw_data.loc[raw_data['Embarked'].isnull(), 'Embarked'] = 'U'
    stations = {'S': 'Southhampton', 'C': 'Cherbourg', 'Q': 'Queenstown', 'U': 'Unknown'}
    embarked_categorical = pd.Categorical(raw_data['Embarked']).rename_categories(stations)
    raw_data['Embarked'] = embarked_categorical
    return raw_data
def create_sex_category(raw_data):
    raw_data['Sex'] = pd.Categorical(raw_data['Sex'])
    return raw_data
def create_pclass_category(raw_data):
    raw_data['Pclass'] = pd.Categorical(raw_data['Pclass']).rename_categories({1: 'First', 2: 'Second', 3: 'Third'})
    return raw_data
def create_survived_category(raw_data):
    surviced_categorical_series = pd.Categorical(raw_data['Survived'])
    surviced_categorical_series = surviced_categorical_series.rename_categories(['died', 'survived'])
    raw_data['Survived'] = surviced_categorical_series
    return raw_data
def create_cabin_category(raw_data):
    raw_data.loc[raw_data['Cabin'].isna(), 'Cabin'] = 'Z'
    cabin_area = [cabin[0] for cabin in raw_data['Cabin']]
    cabin_area_series = pd.Series(cabin_area)
    raw_data['Cabin'] = pd.Categorical(cabin_area_series)
    return raw_data

def clean (raw_data):
    dropped_data = drop_columns(raw_data)
    filled_ages = fill_missing_ages(dropped_data)
    embarked_categorical = create_embarkment_category(filled_ages)
    sex_categorical = create_sex_category(embarked_categorical)
    plcass_categorial = create_pclass_category(sex_categorical)
    survived_categorial = create_survived_category(plcass_categorial)
    cabin_categorial = create_cabin_category(survived_categorial)
    return cabin_categorial

def plot(data):
    data.hist('Age')
    plt.savefig(f'{directory}/age_hist.png')

    data.hist(color = 'red')
    plt.savefig(f'{directory}/age_hist_red.png')

    data.hist('Age', bins=10, by='Pclass')
    plt.savefig(f'{directory}/age_hist_group_by_pclass.png')
    data.boxplot('Age')
    plt.savefig(f'{directory}/boxplots.png')

def main():
    raw_data = load_data()
    data = clean(raw_data)
    plot(data)

if __name__ == '__main__':
    main()