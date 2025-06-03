with open('./programme/Präsenztag3/people.csv', 'rt', encoding='utf-8') as people_csv_file:
    content = people_csv_file.read()
rows = content.splitlines()
# strange = content.split('i')

with open('./programme/Präsenztag3/people.csv', 'rt', encoding='utf-8') as people_csv_file:
    list_of_lines = people_csv_file.readlines()

alternative_rows = []
for line in list_of_lines:
    alternative_rows.append(line.replace('\n', ''))

with open('./programme/Präsenztag3/people.csv', 'rt', encoding='utf-8') as people_csv_file:
    rows = people_csv_file.read().splitlines()

print('done')