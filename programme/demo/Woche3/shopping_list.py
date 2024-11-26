with open ('./programme/demo/Woche3/raw_shopping_list.txt') as file:
    raw_items = file.readlines()

items = [row[:-1] if row.endswith('\n') else row for row in raw_items ]
unique_items = set(items)
shopping_list = {item: items.count(item) for item in unique_items}

with open ('./programme/demo/Woche3/shopping_list.txt', 'wt') as file:
    for item in shopping_list:
        file.write(f'{item}: {shopping_list[item]}\n')
