class ShoppingListService:
    SEPARATOR = ':'

    def create_shopping_list(self, rows: list[str]):
        items = [row.split(self.SEPARATOR)[1] for row in rows]
        unique_items = set(items)
        shopping_list = []
        for unique_item in unique_items:
            shopping_list.append(f'{unique_item}={items.count(unique_item)}\n')
        with open('data/shopping_list.txt', 'wt', encoding='utf-8') as file:
            file.writelines(shopping_list)

    def calculate_number_of_people(self, rows: list[str]):
        people = [row.split(ShoppingListService.SEPARATOR)[0] for row in rows]
        unique_people = set(people)
        print(f'{len(unique_people)} people need items')

    def group_items(self, rows: list[str]):
        grouped_items = dict()
        for row in rows:
            splitted = row.split(ShoppingListService.SEPARATOR)
            person = splitted[0]
            item = splitted[1]
            items_for_person = grouped_items.get(person, [])
            items_for_person.append(item)
            grouped_items[person] = items_for_person
        print(grouped_items)
