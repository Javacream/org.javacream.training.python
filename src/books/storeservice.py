import mysql.connector


class DatabaseStoreService:
    def __init__(self, db_config):
        self.db_config = db_config
    def get_stock(self, category, item):
        with mysql.connector.connect(**self.db_config) as conn:
            statement = conn.cursor()
            statement.execute(f"select stock from store where category='{category}' and item = '{item}'")
            result = statement.fetchall()
            if (len(result) == 0):
                return 0
            for stockResult in result:
                return stockResult[0]
            conn.commit()
    def set_stock(self, category, item, stock):
        with mysql.connector.connect(**self.db_config) as conn:
            statement = conn.cursor()
            statement.execute(f"insert into store (category, item, stock) values('{category}', '{item}', {stock})")
            conn.commit()

        
class StoreService:
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
