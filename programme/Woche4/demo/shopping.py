def create_unique_items(items :list[str]):
    return set(items)

def create_shopping_collection(items :list[str]):
    items_and_number = dict()
    for item in items:
        number = items_and_number.get(item)
        if number == None:
            number = 1
        else:
            number += 1
        items_and_number[item] = number
    return [f'{item} -> {items_and_number[item]}' for item in items_and_number]    