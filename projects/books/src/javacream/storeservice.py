
class DatabaseStoreService:
    def __init__(self, database):
        self.database = database
    def get_stock(self, category, item):
            connection = self.database.cursor()
            connection.execute("select stock from STORE")
            result = connection.fetchall()
            if (len(result) == 0):
                return 0
            for stock in result:
                return stock[0]
    def set_stock(self, category, item, stock):
            connection = self.database.cursor()
            connection.execute(f"insert into STORE (category, item, stock) values ('{category}', '{item}', {stock})")
            self.database.commit()
            print(connection.rowcount)
    def get_categories(self):
            connection = self.database.cursor()
            connection.execute("select category from STORE")
            result = connection.fetchall()
            return [data[0] for data in result]
    def get_items_for(self, category):
            connection = self.database.cursor()
            connection.execute(f"select item from STORE where category = '{category}'")
            result = connection.fetchall()
            return [data[0] for data in result]

class StoreService(object):
    def __init__(self):
        self.store = {}
    
    def get_stock(self, category, item):
        category_dict = self.store.get(category, None)
        if not category_dict:
            return 0
        else:
            stock = category_dict.get(item, None)
            if stock:
                return stock
            else:
                return 0 
    def set_stock(self, category, item, stock):
        category_dict = self.store.get(category, None)
        if not category_dict:
            category_dict = {item:stock}
            self.store[category] = category_dict
        else:
            item_dict = category_dict.get(item, None)
            if not item_dict:
                category_dict[item] = stock
            else:
                category_dict[item] = stock
    def get_categories(self):
        return self.store.keys()
    def get_items_for(self, category):
        return self.store.get(category, {}).keys()