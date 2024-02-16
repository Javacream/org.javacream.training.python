import json
class Item:
    def __init__(self, id, name, amount, price):
        self.id = id
        self.name = name
        self.amount = amount
        self.price = price
class ItemEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Item):
            return obj.__dict__
        return super().default(obj)    
class InventoryDecoder(json.JSONDecoder):
    def decode(self, json_str):
        data = json.loads(json_str)
        for id in data:
            data[id] = Item(data[id]["id"], data[id]["name"], data[id]["amount"], data[id]["price"])
        return data    
class Inventory:
    inventory_path = "inventory.json"
    def __init__(self):
        self.items = dict()

    def add(self, item):
        self.items.update({item.id: item})
    def remove(self, item):
        self.items.pop(item.id)
    def update(self, id, amount):
        item = self.items.get(id)
        if item != None:
            item.amount = amount
        else:
            print(f"Item mit der Id {id} nicht gefunden")
    def get_value(self):
        price_list = [item.price for item in self.items.values()]
        total_value = sum(price_list)
        return total_value
    def load(self):
        with open(Inventory.inventory_path, 'r') as json_file:
            self.items = json.load(json_file,cls=InventoryDecoder)
    def save(self):
        with open(Inventory.inventory_path, 'w') as json_file:
            json.dump(self.items, json_file, indent=2, cls=ItemEncoder)

def test():
    inventory = Inventory()
    item1 = Item(1, "buch", 10, 9.99)
    item2 = Item(2, "dvd", 5, 19.99)
    item3 = Item(3, "cd", 100, 1.99)
    inventory.add(item1)
    inventory.add(item2)
    inventory.add(item3)
    total_value = inventory.get_value()
    print(total_value)
    inventory.remove(item3)
    total_value = inventory.get_value()
    print(total_value)
    inventory.save()
    inventory = Inventory() # erzeuge neues leeres Inventory und lade Daten
    inventory.load()
    total_value = inventory.get_value()
    print(total_value)

test()