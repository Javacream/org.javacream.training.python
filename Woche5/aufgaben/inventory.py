import json
class Item:
    def __init__(self, id, name, amount, price):
        self.id = id
        self.name = name
        self.amount = amount
        self.price = price

class Inventory:
    inventory_path = "inventory.json"
    def __init__(self):
        self.items = dict()

    def add(self, item):
        self.items.update(item.id, item)
    def remove(self, item):
        self.items.pop(item.id)
    def update(self, id, amount):
        item = self.items.get(id)
        if item != None:
            item.amount = amount
        else:
            print(f"Item mit der Id {id} nicht gefunden")
    def get_value(self):
        price_list = [price for price in self.items.values()]
        total_value = sum(price_list)
        return total_value
    def load(self):
        with open(Inventory.inventory_path, 'r') as json_file:
            self.items = json.load(json_file)
    def save(self):
        with open(Inventory.inventory_path, 'w') as json_file:
            json.dump(self.items, json_file, indent=2)

def test():
    inventory = Inventory()
    item1 = Item(1, "buch", 10, 9.99)
    inventory.add(item1)
    total_value = inventory.get_value()
    print(total_value)

test()