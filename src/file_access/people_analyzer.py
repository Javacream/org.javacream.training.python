def read_people_data():
    inpath = 'data/people.txt'
    with open(inpath, encoding='utf-8') as people_file:
        content = people_file.read()
    names = content.split('\n')
    return names

def write_people_upper(names):
    upper_names = {f'{name.upper()}\n' for name in names}
    upper_names_outpath = 'data/people_upper.txt'
    with open(upper_names_outpath, 'wt', encoding='utf-8') as people_file:
        people_file.writelines(upper_names)

def write_people_unique(names):
    unique_names = {f'{name}\n' for name in names}
    unique_names_outpath = 'data/unique_people.txt'
    with open(unique_names_outpath, 'wt', encoding='utf-8') as people_file:
        people_file.writelines(unique_names)

def write_people_descriptions(names):
    name_descriptions = [f'the name {name} has {len(name)} characters\n' for name in names]
    name_descriptions_outpath = 'data/people_descriptions.txt'
    with open(name_descriptions_outpath, 'wt', encoding='utf-8') as people_file:
        people_file.writelines(name_descriptions)

def write_people_lower(names):
    lower_names = {f'{name.lower()}\n' for name in names}
    lower_names_outpath = 'data/people_lower.txt'
    with open(lower_names_outpath, 'wt', encoding='utf-8') as people_file:
        people_file.writelines(lower_names)

def main():
    people_data = read_people_data()
    write_people_upper(people_data)
    write_people_unique(people_data)
    write_people_descriptions(people_data)
    write_people_lower(people_data)

main()