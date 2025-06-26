SEPARATOR = ':'
path = 'data/raw_shopping_list.txt'
with open(path, 'rt', encoding='utf-8') as file:
    raw_rows = file.readlines()
rows = [raw_row.replace('\n', '') for raw_row in raw_rows if raw_row.replace('\n', '').strip() != '']

items = [row.split(SEPARATOR)[1] for row in rows]
people = [row.split(SEPARATOR)[0] for row in rows]

unique_items = set(items)


shopping_list = []
for unique_item in unique_items:
    shopping_list.append(f'{unique_item}={items.count(unique_item)}\n')

with open('data/shopping_list.txt', 'wt', encoding='utf-8') as file:
    file.writelines(shopping_list)

unique_people = set(people)
print(f'{len(unique_people)} people need items')

grouped_items = dict()
for row in rows:
    splitted = row.split(SEPARATOR)
    person = splitted[0]
    item = splitted[1]
    items_for_person = grouped_items.get(person, [])
    items_for_person.append(item)
    grouped_items[person] = items_for_person
print(grouped_items)