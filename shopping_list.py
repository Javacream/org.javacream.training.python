with open ('./data/raw_shopping_list.txt') as file:
    raw_items = file.readlines()

items = list()
for raw_item in raw_items:
    if raw_item.endswith('\n'):
        items.append(raw_item[0:-1])
    else:
        items.append(raw_item)

unique_items = set(items)
print(unique_items)
print(len(items))

shopping_list = dict()

for item in unique_items:
    print(f'{item}: {items.count(item)}')
    shopping_list[item] = items.count(item)

print(shopping_list)

with open ('./data/shopping_list.txt', 'wt') as file:
    for item in shopping_list:
        file.write(f'{item}: {shopping_list[item]}\n')
